# Nasazení aplikace Spring AI MCP na Azure Container Apps

> [!WARNING]
> Tento kombinovaný autorizační/resource server je určen pro účely výuky a
> vývoje/testování. Produkční systémy by měly používat dedikovaného poskytovatele identity,
> trvalé podepisovací klíče a přihlašovací údaje uložené v řízeném úložišti tajemství.

 ([Zabezpečení Spring AI MCP serverů pomocí OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Obrázek: Spring AI MCP server zabezpečený pomocí Spring Authorization Server. Server vydává přístupové tokeny klientům a ověřuje je při příchozích požadavcích (zdroj: Spring blog) ([Zabezpečení Spring AI MCP serverů pomocí OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Pro nasazení Spring MCP serveru ho sestavte jako kontejner a použijte Azure Container Apps s externím přístupem. Například pomocí Azure CLI můžete spustit:

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

Toto vytvoří veřejně přístupnou Container App s povoleným HTTPS (Azure vydává bezplatný TLS certifikát pro výchozí doménu `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Výstup příkazu obsahuje plně kvalifikovaný název aplikace (např. `my-mcp-app.eastus.azurecontainerapps.io`), který se stane základem **issuer URL**. Ujistěte se, že je povolen HTTP ingress (jak je uvedeno výše), aby na aplikaci mohl APIM dosáhnout. V testovacím/vývojovém prostředí použijte volbu `--ingress external` (nebo přidejte vlastní doménu s TLS dle [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Veškeré citlivé vlastnosti (například OAuth client secrets) ukládejte do tajemství Container Apps nebo Azure Key Vault a mapujte je do kontejneru jako proměnné prostředí. 

## Konfigurace Spring Authorization Serveru

Ve vašem kódu Spring Boot aplikace zahrňte startéry Spring Authorization Server a Resource Server. Nakonfigurujte `RegisteredClient` (pro grant `client_credentials` v dev/test) a zdroj klíče JWT. Například v `application.properties` můžete nastavit:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Povolte Authorization Server a Resource Server definováním bezpečnostního filtru. Například:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Povolit koncové body serveru autorizace
            .apply(authzServer.and())
            // Povolit server zdrojů (ověřit JWT u příchozích požadavků)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Zakázat CSRF (MCP server není založený na prohlížeči)
            .csrf(csrf -> csrf.disable())
            // Povolit CORS pro klientské demonstrační nástroje
            .cors(withDefaults());
        return http.build();
    }

    // Definovat klienta v paměti (RegisteredClient) a zdroj JWK:
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
        // Vygenerovat RSA klíč (pro vývoj/test znovu při spuštění)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Toto nastavení vystaví výchozí OAuth2 koncové body: `/oauth2/token` pro tokeny a `/oauth2/jwks` pro JSON Web Key Set. (Ve výchozím nastavení Spring `AuthorizationServerSettings` mapuje `/oauth2/token` a `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server vydá JWT přístupové tokeny podepsané RSA klíčem výše a publikuje svůj veřejný klíč na `https://<your-app>:/oauth2/jwks`. 

**Povolte OpenID Connect discovery:** Aby APIM automaticky získal issuer a JWKS, povolte OIDC poskytovatelovskou konfigurační endpoint přidáním `.oidc(Customizer.withDefaults())` do vaší bezpečnostní konfigurace ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Například:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– povoluje /.well-known/openid-configuration
```

Toto vystaví `/.well-known/openid-configuration`, které APIM může použít pro metadata. Nakonec možná budete chtít přizpůsobit JWT tvrzení **audience**, aby kontrola `<audiences>` v APIM prošla. Například přidejte token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Nastavte vlastní publikum (např. ID klienta nebo identifikátor API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

To zajistí, že tokeny budou nést `"aud": ["mcp-client"]`, což odpovídá ID klienta nebo rozsahu očekávanému APIM. 

## Zpřístupnění Token a JWKS koncových bodů

Po nasazení bude **issuer URL** vaší aplikace `https://<app-fqdn>`, např. `https://my-mcp-app.eastus.azurecontainerapps.io`. Její OAuth2 koncové body jsou:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – klienti zde získávají tokeny (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – vrací JWK set (APIM ho používá k získání podepisovacích klíčů).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON OIDC discovery (obsahuje `issuer`, `token_endpoint`, `jwks_uri` atd.).  

APIM bude směřovat na **OpenID konfigurační URL**, odkud objeví `jwks_uri`. Například pokud je FQDN vaší Container App `my-mcp-app.eastus.azurecontainerapps.io`, pak by APIM `<openid-config url="...">` mělo používat `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Ve výchozím stavu Spring nastaví `issuer` v těchto datech na stejnou základní URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfigurace Azure API Management (`validate-jwt`)

V Azure APIM přidejte příchozí politiku, která použije `<validate-jwt>` politiku k ověření příchozích JWT proti vašemu Spring Authorization Serveru. Pro jednoduché nastavení můžete použít OpenID Connect metadata URL. Ukázka úryvku politiky:

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

Tato politika říká APIM, aby načetl OpenID konfiguraci ze Spring Auth Serveru, získal její JWKS a ověřil, že každý token je podepsán důvěryhodným klíčem a má správné publikum. (Pokud vynecháte `<issuers>`, APIM automaticky použije `issuer` tvrzení z metadat.) `<audience>` by měl odpovídat vašemu klientskému ID nebo API identifikátoru v tokenu (v ukázce výše jsme nastavili `"mcp-client"`). Toto odpovídá dokumentaci Microsoftu o použití `validate-jwt` s `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po ověření APIM přepošle požadavek (včetně původního záhlaví `Authorization`) na backend. Jelikož je Spring aplikace také resource server, znovu ověří token, ale APIM už zajistil jeho platnost. (Pro vývoj můžete spoléhat na kontrolu APIM a případně v aplikaci další kontroly vypnout, ale bezpečnější je mít obě.)

## Příklad nastavení

| Nastavení         | Příklad hodnoty                                                      | Poznámky                                   |
|-------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL vaší Container App (základní URI)      |
| **Token endpoint**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Výchozí Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Výchozí endpoint JWK Set ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC dokument pro discovery (automaticky generován) |
| **APIM audience** | `mcp-client`                                                        | OAuth client ID nebo jméno API resource    |
| **APIM policy**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` používá tuto URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Běžné problémy

- **HTTPS/TLS:** Brána APIM vyžaduje, aby endpoint OpenID/JWKS byl přes HTTPS s platným certifikátem. Ve výchozím nastavení Azure Container Apps poskytuje důvěryhodný TLS certifikát pro doménu spravovanou Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Pokud používáte vlastní doménu, ujistěte se, že je přidán certifikát (můžete využít bezplatnou funkci spravovaných certifikátů Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Pokud APIM nemůže důvěřovat certifikátu endpointu, `<validate-jwt>` nebude schopen metadata načíst.  

- **Dostupnost endpointu:** Ujistěte se, že jsou koncové body Spring aplikace dostupné z APIM. Použití `--ingress external` (nebo povolení ingress v portálu) je nejjednodušší. Pokud jste zvolili interní nebo vNet-bound prostředí, APIM (standardně veřejné) nemusí mít přístup, pokud není v té samé vNet síti. V testovacím prostředí preferujte veřejný ingress, aby APIM mohl volat `.well-known` a `/jwks` URL. 

- **Povolené OpenID Discovery:** Ve výchozím nastavení Spring Authorization Server **nevystavuje** `/.well-known/openid-configuration`, pokud není OIDC povoleno. Ujistěte se, že v bezpečnostní konfiguraci obsahujete `.oidc(Customizer.withDefaults())` (viz výše), takže endpoint poskytovatele konfigurace je aktivní ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Jinak APIM volání `<openid-config>` skončí chybou 404.

- **Audience claim:** Výchozí chování Springu je nastavit tvrzení `aud` na klientské ID. Pokud kontrola `<audience>` v APIM selže, může být potřeba token přizpůsobit (jak je ukázáno výše) nebo upravit APIM politiku. Ujistěte se, že publikum v JWT odpovídá tomu, co konfigurujete v `<audience>`. 

- **Zpracování JSON metadat:** JSON OpenID konfigurace musí být platný. Výchozí konfigurace Springu vydá standardní OIDC metadata dokument. Ověřte, že obsahuje správné hodnoty `issuer` a `jwks_uri`. Pokud máte Spring za proxy nebo cestou s prefixem, důkladně zkontrolujte URL v těchto metadatech. APIM je použije tak, jak jsou.

- **Pořadí politik:** V APIM politice umístěte `<validate-jwt>` **před** jakýmkoli směrováním na backend. Jinak mohou požadavky přijít do vaší aplikace bez platného tokenu. Také zajistěte, aby `<validate-jwt>` byl umístěn přímo pod `<inbound>` (ne vnořený v jiné podmínce), aby APIM politiku aplikoval.

Dodržením výše uvedených kroků můžete provozovat váš Spring AI MCP server v Azure Container Apps a mít Azure API Management, které ověřuje přicházející OAuth2 JWT s minimální politikou. Klíčové body jsou: zpřístupnit Spring Auth endpointy veřejně s TLS, povolit OIDC discovery a nasměrovat APIM `validate-jwt` na OpenID konfigurační URL (aby mohl automaticky načíst JWKS). Toto nastavení je vhodné pro dev/test prostředí; do produkce zvažte správu tajemství, životnosti tokenů a rotaci klíčů v JWKS dle potřeby. 


**Reference:** Viz dokumentace Spring Authorization Server pro výchozí koncové body ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) a konfiguraci OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); viz dokumentace Microsoft APIM pro příklady `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); a dokumentace Azure Container Apps pro nasazení a certifikáty ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->