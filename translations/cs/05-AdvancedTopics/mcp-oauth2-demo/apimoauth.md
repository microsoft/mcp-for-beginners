# Nasazení aplikace Spring AI MCP do Azure Container Apps

 ([Zabezpečení Spring AI MCP serverů pomocí OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Obrázek: Spring AI MCP server zabezpečený pomocí Spring Authorization Server. Server vydává přístupové tokeny klientům a ověřuje je při příchozích požadavcích (zdroj: Spring blog) ([Zabezpečení Spring AI MCP serverů pomocí OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Pro nasazení Spring MCP serveru jej sestavte jako kontejner a použijte Azure Container Apps s externím přístupem. Například pomocí Azure CLI můžete spustit:

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

Tím se vytvoří veřejně přístupná Container App s povoleným HTTPS (Azure vydává zdarma TLS certifikát pro výchozí doménu `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Výstup příkazu obsahuje plně kvalifikovaný název aplikace (FQDN), např. `my-mcp-app.eastus.azurecontainerapps.io`, který se stává základem **issuer URL**. Ujistěte se, že je povolen HTTP ingress (jak je uvedeno výše), aby APIM mohl aplikaci dosáhnout. V testovacím nebo vývojovém prostředí použijte volbu `--ingress external` (nebo připojte vlastní doménu s TLS podle [Microsoft dokumentace](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Citlivé vlastnosti (např. OAuth client secrets) ukládejte do Container Apps secrets nebo Azure Key Vault a mapujte je do kontejneru jako proměnné prostředí.

## Konfigurace Spring Authorization Serveru

Ve vašem Spring Boot kódu zahrňte startéry Spring Authorization Server a Resource Server. Nakonfigurujte `RegisteredClient` (pro grant `client_credentials` v dev/test prostředí) a zdroj klíčů JWT. Například v `application.properties` můžete nastavit:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
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
            // Enable the Authorization Server endpoints
            .apply(authzServer.and())
            // Enable the Resource Server (validate JWT on incoming requests)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Disable CSRF (MCP server is not browser-based)
            .csrf(csrf -> csrf.disable())
            // Allow CORS for client demo tools
            .cors(withDefaults());
        return http.build();
    }

    // Define an in-memory client (RegisteredClient) and a JWK source:
    @Bean
    public RegisteredClientRepository registeredClientRepository() {
        RegisteredClient client = RegisteredClient.withId("1")
            .clientId("mcp-client")
            .clientSecret("{noop}secret")
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Generate an RSA key (for dev/test, generate anew at startup)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Toto nastavení zpřístupní výchozí OAuth2 endpointy: `/oauth2/token` pro tokeny a `/oauth2/jwks` pro JSON Web Key Set. (Ve výchozím nastavení Spring `AuthorizationServerSettings` mapuje `/oauth2/token` a `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Server vydává JWT přístupové tokeny podepsané RSA klíčem výše a zveřejňuje svůj veřejný klíč na `https://<your-app>:/oauth2/jwks`.

**Povolení OpenID Connect discovery:** Aby APIM mohl automaticky získat issuer a JWKS, povolte endpoint konfigurace OIDC provideru přidáním `.oidc(Customizer.withDefaults())` do vaší bezpečnostní konfigurace ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Například:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Tím zpřístupníte `/.well-known/openid-configuration`, které APIM využívá pro metadata. Nakonec možná budete chtít přizpůsobit JWT claim **audience**, aby APIM kontrola `<audiences>` prošla. Přidejte například token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Tím zajistíte, že tokeny budou obsahovat `"aud": ["mcp-client"]`, což odpovídá client ID nebo scope očekávanému APIM.

## Zpřístupnění token a JWKS endpointů

Po nasazení bude vaše **issuer URL** `https://<app-fqdn>`, např. `https://my-mcp-app.eastus.azurecontainerapps.io`. Její OAuth2 endpointy jsou:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – zde klienti získávají tokeny (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – vrací JWK set (APIM jej používá k získání podpisových klíčů).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (obsahuje `issuer`, `token_endpoint`, `jwks_uri` atd.).

APIM bude směřovat na **OpenID configuration URL**, odkud zjistí `jwks_uri`. Například pokud je FQDN vaší Container App `my-mcp-app.eastus.azurecontainerapps.io`, pak APIM `<openid-config url="...">` by mělo používat `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Ve výchozím nastavení Spring nastaví `issuer` v těchto datech na stejnou základní URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfigurace Azure API Management (`validate-jwt`)

V Azure APIM přidejte inbound politiku, která používá `<validate-jwt>` k ověření příchozích JWT proti vašemu Spring Authorization Serveru. Pro jednoduché nastavení můžete použít OpenID Connect metadata URL. Ukázka politiky:

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

Tato politika říká APIM, aby načetl OpenID konfiguraci ze Spring Auth Serveru, získal jeho JWKS a ověřil, že každý token je podepsán důvěryhodným klíčem a má správné audience. (Pokud vynecháte `<issuers>`, APIM automaticky použije `issuer` claim z metadat.) `<audience>` by mělo odpovídat vašemu client ID nebo identifikátoru API zdroje v tokenu (v příkladu výše jsme nastavili `"mcp-client"`). To odpovídá dokumentaci Microsoftu o použití `validate-jwt` s `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Po ověření APIM přepošle požadavek (včetně původního hlavičky `Authorization`) na backend. Protože Spring aplikace je také resource server, token znovu ověří, ale APIM už jeho platnost potvrdil. (Pro vývoj můžete spoléhat na kontrolu APIM a v aplikaci další kontroly vypnout, ale bezpečnější je mít obojí.)

## Příklad nastavení

| Nastavení          | Příklad hodnoty                                                    | Poznámky                                   |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL vaší Container App (základní URI)      |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Výchozí Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Výchozí JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery dokument (automaticky generovaný) |
| **APIM audience**  | `mcp-client`                                                      | OAuth client ID nebo název API zdroje      |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` používá tuto URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Běžné problémy

- **HTTPS/TLS:** APIM gateway vyžaduje, aby OpenID/JWKS endpoint byl HTTPS s platným certifikátem. Ve výchozím nastavení Azure Container Apps poskytuje důvěryhodný TLS certifikát pro Azure spravovanou doménu ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Pokud používáte vlastní doménu, nezapomeňte připojit certifikát (můžete využít Azure free managed certifikát) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Pokud APIM nebude důvěřovat certifikátu endpointu, `<validate-jwt>` nezíská metadata.

- **Dostupnost endpointů:** Ujistěte se, že endpointy Spring aplikace jsou dostupné z APIM. Nejjednodušší je použít `--ingress external` (nebo povolit ingress v portálu). Pokud jste zvolili interní nebo vNet-bound prostředí, APIM (který je ve výchozím nastavení veřejný) nemusí mít přístup, pokud není ve stejné VNet. V testovacím prostředí preferujte veřejný ingress, aby APIM mohl volat `.well-known` a `/jwks` URL.

- **Povolení OpenID discovery:** Ve výchozím nastavení Spring Authorization Server **nezpřístupňuje** `/.well-known/openid-configuration`, pokud není povolen OIDC. Nezapomeňte přidat `.oidc(Customizer.withDefaults())` do bezpečnostní konfigurace (viz výše), aby byl endpoint aktivní ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Jinak APIM `<openid-config>` zavolá 404.

- **Audience claim:** Výchozí chování Spring je nastavit `aud` claim na client ID. Pokud APIM kontrola `<audience>` selže, možná budete muset token přizpůsobit (jak je ukázáno výše) nebo upravit APIM politiku. Ujistěte se, že audience v JWT odpovídá tomu, co máte v `<audience>`.

- **Parsování JSON metadat:** OpenID konfigurační JSON musí být platný. Výchozí Spring konfigurace vygeneruje standardní OIDC metadata. Ověřte, že obsahují správné `issuer` a `jwks_uri`. Pokud hostujete Spring za proxy nebo s cestou, zkontrolujte URL v metadatech. APIM je použije tak, jak jsou.

- **Pořadí politik:** V APIM politice umístěte `<validate-jwt>` **před** jakýmkoliv směrováním na backend. Jinak by mohly požadavky dorazit do aplikace bez platného tokenu. Také zajistěte, aby `<validate-jwt>` bylo přímo pod `<inbound>` (ne vnořené v jiné podmínce), aby APIM politiku aplikoval.

Dodržením výše uvedených kroků můžete provozovat Spring AI MCP server v Azure Container Apps a nechat Azure API Management ověřovat příchozí OAuth2 JWT pomocí minimální politiky. Klíčové body jsou: zpřístupnit Spring Auth endpointy veřejně s TLS, povolit OIDC discovery a nasměrovat APIM `validate-jwt` na OpenID config URL (pro automatické získání JWKS). Toto nastavení je vhodné pro dev/test prostředí; do produkce zvažte správu tajemství, životnost tokenů a rotaci klíčů v JWKS podle potřeby.
**Reference:** Viz dokumentace Spring Authorization Server pro výchozí koncové body ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) a konfiguraci OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); viz dokumentace Microsoft APIM pro příklady `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); a dokumentace Azure Container Apps pro nasazení a certifikáty ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.