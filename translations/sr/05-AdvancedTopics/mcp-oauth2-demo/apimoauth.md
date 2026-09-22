# Деплојовање Spring AI MCP апликације на Azure Container Apps

> [!WARNING]
> Овај комбиновани сервер за ауторизацију/ресурсе намењен је за учење и
> развој/тестирање. Продукцијски системи треба да користе посебног провајдера идентитета,
> имају упорне кључеве за потписивање и креденцијале који се чувају у менаџованом тајном складишту.

 ([Осигуравање Spring AI MCP сервера помоћу OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Слика: Spring AI MCP сервер осигурани помоћу Spring Authorization Server. Сервер издаје приступне токене клијентима и верификује их при долазним захтевима (извор: Spring блог) ([Осигуравање Spring AI MCP сервера помоћу OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Да бисте деплојовали Spring MCP сервер, изградите га као контејнер и користите Azure Container Apps са екстерним приступом. На пример, коришћењем Azure CLI-а можете покренути:

```bash
az containerapp up \
  --name my-mcp-app \
  --resource-group MyResourceGroup \
  --location eastus \
  --environment MyContainerEnv \
  --image myregistry.azurecr.io/my-mcp-server:latest \
  --ingress external \
  --target-port 8080 \
  --query properties.configuration.ingress.fqdn
```

Ово ствара Container App доступну јавности са омогућеним HTTPS-ом (Azure издаје бесплатан TLS сертификат за подразумевани `*.azurecontainerapps.io` домен ([Прилагођени домени и бесплатни менаџовани сертификати у Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Излаз команде укључује FQDN апликације (нпр. `my-mcp-app.eastus.azurecontainerapps.io`), који постаје основа за **issuer URL**. Осигурајте да је HTTP приступ омогућен (као горе) како би APIM могао да приступи апликацији. У тест/развојном окружењу, користите опцију `--ingress external` (или вежите прилагођени домен са TLS-ом према [Microsoft документацији](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Прилагођени домени и бесплатни менаџовани сертификати у Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Све осетљиве особине (као што су OAuth клијентски тајни) чувајте у Container Apps секретима или Azure Key Vault-у, и мапирајте их у контејнер као променљиве окружења.

## Конфигурисање Spring Authorization Server-а

У коду ваше Spring Boot апликације укључите стартере за Spring Authorization Server и Resource Server. Конфигуришите `RegisteredClient` (за `client_credentials` грант у развоју/тестирању) и извор кључева за JWT. На пример, у `application.properties` можете поставити:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Омогућите Authorization Server и Resource Server дефинисањем security filter chain-а. На пример:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Омогући крајње тачке овлашћења сервера
            .apply(authzServer.and())
            // Омогући ресурсни сервер (валидација JWT на долазним захтевима)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Онемогући CSRF (MCP сервер није базиран на прегледачу)
            .csrf(csrf -> csrf.disable())
            // Дозволи CORS за алате за демонстрацију клијента
            .cors(withDefaults());
        return http.build();
    }

    // Дефиниши клијента у меморији (RegisteredClient) и JWK извор:
    @Bean
    public RegisteredClientRepository registeredClientRepository(
        @Value("${demo.oauth.client-id}") String clientId,
        @Value("${demo.oauth.client-secret}") String clientSecret) {
      PasswordEncoder encoder = PasswordEncoderFactories.createDelegatingPasswordEncoder();
        RegisteredClient client = RegisteredClient.withId("1")
        .clientId(clientId)
        .clientSecret(encoder.encode(clientSecret))
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Генериши RSA кључ (за развој/тест, генериши на почетку сваки пут)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Ова конфигурација ће изложити подразумеване OAuth2 крајње тачке: `/oauth2/token` за токене и `/oauth2/jwks` за JSON Web Key Set. (Подразумевано, Spring `AuthorizationServerSettings` мапира `/oauth2/token` и `/oauth2/jwks` ([Конфигурациони модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Сервер ће издавати JWT приступне токене потписане RSA кључем наведеним горе, и објављивати свој јавни кључ на `https://<your-app>:/oauth2/jwks`.

**Омогућите OpenID Connect откривање:** Да би APIM аутоматски преузео issuer и JWKS, омогућите OIDC provider конфигурациони endpoint додавањем `.oidc(Customizer.withDefaults())` у вашу безбедносну конфигурацију ([Конфигурациони модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). На пример:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– омогућава /.well-known/openid-configuration
```

Ово излаже `/.well-known/openid-configuration`, коју APIM може користити за метаподатке. На крају, можда ћете желети да прилагодите JWT **audience** claim тако да APIM-ов `<audiences>` проверу прође. На пример, додајте token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Поставите прилагођену публику (нпр. ИД клијента или идентификатор API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Ово осигурава да токени носе `"aud": ["mcp-client"]`, што одговара ID-у клијента или очекиваном периоду од стране APIM-а.

## Излагање Token и JWKS крајњих тачака

Након деплоја, **issuer URL** ваше апликације ће бити `https://<app-fqdn>`, нпр. `https://my-mcp-app.eastus.azurecontainerapps.io`. Њене OAuth2 крајње тачке су:

- **Крајња тачка за токен:** `https://<app-fqdn>/oauth2/token` – клијенти овде добијају токене (client_credentials флоу).
- **JWKS крајња тачка:** `https://<app-fqdn>/oauth2/jwks` – враћа JWK скуп (који APIM користи за добијање кључева за потписивање).
- **OpenID конфиг:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC откривачки JSON (садржи `issuer`, `token_endpoint`, `jwks_uri`, итд.).

APIM ће указивати на **OpenID конфигурациони URL**, одакле открива `jwks_uri`. На пример, ако је FQDN ваше Container App-а `my-mcp-app.eastus.azurecontainerapps.io`, онда `<openid-config url="...">` у APIM-у треба да користи `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Подразумевано, Spring ће у те метаподатке поставити исти `issuer` URL као основу ([Конфигурациони модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Конфигурисање Azure API Management-а (`validate-jwt`)

У Azure APIM-у додајте inbound policy који користи `<validate-jwt>` да провери долазне JWT токене у односу на ваш Spring Authorization Server. За једноставну поставку, можете користити OpenID Connect metadata URL. Пример политика:

```xml
<inbound>
  <validate-jwt header-name="Authorization" require-scheme="Bearer">
    <openid-config url="https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration" />
    <audiences>
      <audience>mcp-client</audience>  <!-- Expected audience in the JWT -->
    </audiences>
    <issuers>
      <issuer>https://my-mcp-app.eastus.azurecontainerapps.io</issuer>
    </issuers>
  </validate-jwt>
  <!-- (optional) other policies -->
</inbound>
```

Ова политика каже APIM-у да преузме OpenID конфигурацију са Spring Auth Server-а, прибави његов JWKS, и потврди да је сваки токен потписан поузданим кључем и да има исправну публику. (Ако прескочите `<issuers>`, APIM ће аутоматски користити `issuer` claim из метаподатака.) `<audience>` треба да одговара вашем client ID-у или API resource идентификатору у токену (у примеру изнад поставили смо га на `"mcp-client"`). Ово је у складу са Microsoft документацијом о коришћењу `validate-jwt` са `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Након валидације, APIM ће проследити захтев (укључујући оригинални `Authorization` хедер) backend-у. Пошто је Spring апликација такође resource server, поново ће верификовати токен, али APIM је већ осигурао његову валидност. (За развој можете се ослонити на проверу APIM-а и онемогућити додатне провере у апликацији ако желите, али је безбедније задржати обе.)

## Пример подешавања

| Подешавање        | Пример вредности                                                   | Напомене                                   |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL ваше Container App апликације (базни URI)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Подразумевана Spring крајња тачка за токен ([Конфигурациони модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Подразумевана крајња тачка за JWK Set ([Конфигурациони модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC документ за откривање (аутоматски генерисан)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID или назив API ресурса       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` користи овај URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Чести проблеми

- **HTTPS/TLS:** APIM gateway захтева да OpenID/JWKS крајња тачка буде HTTPS са валидним сертификатом. Подразумевано, Azure Container Apps обезбеђује поуздан TLS сертификат за Azure-ово управљани домен ([Прилагођени домени и бесплатни менаџовани сертификати у Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ако користите прилагођени домен, обавезно вежите сертификат (можете користити бесплатну менаџовану функцију сертификата у Azure) ([Прилагођени домени и бесплатни менаџовани сертификати у Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Ако APIM не може да верује сертификату крајње тачке, `<validate-jwt>` ће пропасти приликом преузимања метаподатака.

- **Приступачност крајњих тачака:** Осигурајте да су крајње тачке Spring апликације доступне из APIM-а. Коришћење `--ingress external` (или омогућавање приступа у порталу) је најједноставније. Ако сте изабрали унутрашње или везано окружење у vNet-у, APIM (који је подразумевано јаван) можда неће моћи да му приступи осим ако није смештен у исти VNet. У тест окружењу, преферирајте јавни приступ како би APIM могао да позове `.well-known` и `/jwks` URL-ове.

- **Omogućen OpenID Discovery:** По подразумеваној вредности, Spring Authorization Server **не излаже** `/.well-known/openid-configuration` ако OIDC није омогућен. Обавезно укључите `.oidc(Customizer.withDefaults())` у вашу безбедносну конфигурацију (погледајте горе) како би endpoint за провајдер конфигурацију био активан ([Конфигурациони модел :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). У супротном, APIM-ов `<openid-config>` позив ће вратити 404.

- **Audience Claim:** Подразумевано понашање Spring-а је да постави `aud` claim на client ID. Ако APIM-ова `<audience>` провера не успе, можда ћете морати да прилагодите токен (као горе приказано) или конфигуришете APIM политику. Осигурајте да публику у JWT-у одговара ономе што постављате у `<audience>`.

- **Парсирање JSON метаподатака:** OpenID конфигурациони JSON мора бити валидан. Подразумевана Spring конфигурација ће избацити стандардни OIDC метаподатке. Потврдите да садржи тачан `issuer` и `jwks_uri`. Ако хостујете Spring иза проксија или путањског рутирања, двапут проверите URL адресе у овим метаподацима. APIM ће користити ове вредности директно.

- **Редослед политика:** У APIM политици поставите `<validate-jwt>` **пре** било каквог рутирања ка backend-у. У супротном, позиви могу доћи до ваше апликације без важећег токена. Такође, осигурајте да се `<validate-jwt>` налази одмах испод `<inbound>` (а не угнежђен у неки други услов) како би га APIM стварно применило.

Пратећи горе наведене кораке, можете покренути свој Spring AI MCP сервер у Azure Container Apps и имати Azure API Management који валида долазне OAuth2 JWT токене са минималном политиком. Кључне тачке су: изложите Spring Auth крајње тачке јавно са TLS-ом, омогућите OIDC откривање и усмерите APIM-ов `validate-jwt` на OpenID конфигурациони URL (да може аутоматски преузимати JWKS). Ова поставка је погодна за развојно/тест окружење; за продукцију размислите о правилном управљању тајнама, временима важења токена и ротирању кључева у JWKS према потреби.


**Референце:** Погледајте документацију Spring Authorization Server за подразумеване крајње тачке ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) и конфигурацију OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); погледајте Microsoft APIM документацију за примере `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); и Azure Container Apps документацију за деплојмент и сертификате ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->