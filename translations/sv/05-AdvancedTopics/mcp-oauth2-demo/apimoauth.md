# Distribuera Spring AI MCP-appen till Azure Container Apps

 ([Säkra Spring AI MCP-servrar med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figur: Spring AI MCP-server säkrad med Spring Authorization Server. Servern utfärdar access tokens till klienter och validerar dem vid inkommande förfrågningar (källa: Spring-bloggen) ([Säkra Spring AI MCP-servrar med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* För att distribuera Spring MCP-servern, bygg den som en container och använd Azure Container Apps med extern ingress. Till exempel kan du med Azure CLI köra:

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

Detta skapar en publikt tillgänglig Container App med HTTPS aktiverat (Azure utfärdar ett gratis TLS-certifikat för standarddomänen `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Kommandots utdata inkluderar appens FQDN (t.ex. `my-mcp-app.eastus.azurecontainerapps.io`), vilket blir basen för **issuer URL**. Se till att HTTP-ingress är aktiverat (som ovan) så att APIM kan nå appen. I en test-/utvecklingsmiljö, använd alternativet `--ingress external` (eller bind en anpassad domän med TLS enligt [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Spara känsliga egenskaper (som OAuth-klienthemligheter) i Container Apps secrets eller Azure Key Vault, och mappa dem in i containern som miljövariabler.

## Konfigurera Spring Authorization Server

I din Spring Boot-apps kod, inkludera Spring Authorization Server och Resource Server starters. Konfigurera en `RegisteredClient` (för `client_credentials`-grant i dev/test) och en JWT-nyckelkälla. Till exempel kan du i `application.properties` ange:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Aktivera Authorization Server och Resource Server genom att definiera en säkerhetsfilterkedja. Exempel:

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

Denna konfiguration exponerar standard OAuth2-endpoints: `/oauth2/token` för tokens och `/oauth2/jwks` för JSON Web Key Set. (Som standard mappar Spring’s `AuthorizationServerSettings` `/oauth2/token` och `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Servern utfärdar JWT-access tokens signerade med RSA-nyckeln ovan och publicerar sin publika nyckel på `https://<your-app>:/oauth2/jwks`.

**Aktivera OpenID Connect-discovery:** För att låta APIM automatiskt hämta issuer och JWKS, aktivera OIDC provider-konfigurationsendpoint genom att lägga till `.oidc(Customizer.withDefaults())` i din säkerhetskonfiguration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Exempel:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Detta exponerar `/.well-known/openid-configuration`, som APIM kan använda för metadata. Slutligen kan du vilja anpassa JWT:s **audience**-claim så att APIM:s `<audiences>`-kontroll godkänns. Till exempel, lägg till en token-customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Detta säkerställer att token innehåller `"aud": ["mcp-client"]`, vilket matchar klient-ID eller scope som APIM förväntar sig.

## Exponera Token- och JWKS-endpoints

Efter distribution kommer din apps **issuer URL** vara `https://<app-fqdn>`, t.ex. `https://my-mcp-app.eastus.azurecontainerapps.io`. Dess OAuth2-endpoints är:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – här hämtar klienter tokens (client_credentials-flöde).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – returnerar JWK-setet (används av APIM för att hämta signeringsnycklar).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC-discovery JSON (innehåller `issuer`, `token_endpoint`, `jwks_uri` osv.).

APIM pekar på **OpenID-konfigurations-URL:en**, från vilken den upptäcker `jwks_uri`. Om din Container App FQDN är `my-mcp-app.eastus.azurecontainerapps.io`, ska APIM:s `<openid-config url="...">` använda `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Som standard sätter Spring `issuer` i den metadata till samma bas-URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfigurera Azure API Management (`validate-jwt`)

I Azure APIM, lägg till en inbound-policy som använder `<validate-jwt>` för att kontrollera inkommande JWT mot din Spring Authorization Server. För en enkel konfiguration kan du använda OpenID Connect metadata-URL. Exempel på policy-snippet:

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

Denna policy instruerar APIM att hämta OpenID-konfigurationen från Spring Auth Server, hämta dess JWKS och validera att varje token är signerad med en betrodd nyckel och har rätt audience. (Om du utelämnar `<issuers>`, använder APIM automatiskt `issuer`-claim från metadata.) `<audience>` ska matcha ditt klient-ID eller API-resursnamn i token (i exemplet ovan satte vi det till `"mcp-client"`). Detta är i linje med Microsofts dokumentation om att använda `validate-jwt` med `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Efter validering vidarebefordrar APIM förfrågan (inklusive originalet `Authorization`-headern) till backend. Eftersom Spring-appen också är en resource server, kommer den att validera token igen, men APIM har redan säkerställt dess giltighet. (För utveckling kan du förlita dig på APIM:s kontroll och inaktivera ytterligare kontroller i appen om du vill, men det är säkrare att ha båda.)

## Exempelinställningar

| Inställning         | Exempelvärde                                                       | Kommentarer                                |
|---------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | Din Container Apps URL (bas-URI)           |
| **Token endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Standard Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Standard JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC-discoverydokument (auto-genererat)    |
| **APIM audience**   | `mcp-client`                                                      | OAuth klient-ID eller API-resursnamn       |
| **APIM policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` använder denna URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Vanliga fallgropar

- **HTTPS/TLS:** APIM-gatewayen kräver att OpenID/JWKS-endpoint är HTTPS med ett giltigt certifikat. Som standard tillhandahåller Azure Container Apps ett betrott TLS-certifikat för Azure-hanterad domän ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Om du använder en anpassad domän, se till att binda ett certifikat (du kan använda Azures gratis hanterade certifikatfunktion) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Om APIM inte kan lita på endpointens certifikat, kommer `<validate-jwt>` att misslyckas med att hämta metadata.

- **Endpoint-tillgänglighet:** Säkerställ att Spring-appens endpoints är nåbara från APIM. Att använda `--ingress external` (eller aktivera ingress i portalen) är enklast. Om du valt en intern eller vNet-bunden miljö, kan APIM (som standard publikt) kanske inte nå den om den inte är i samma vNet. I en testmiljö är det bäst med publik ingress så att APIM kan anropa `.well-known` och `/jwks` URL:erna.

- **OpenID Discovery aktiverad:** Som standard exponerar inte Spring Authorization Server `/.well-known/openid-configuration` om inte OIDC är aktiverat. Se till att inkludera `.oidc(Customizer.withDefaults())` i din säkerhetskonfiguration (se ovan) så att provider-konfigurationsendpointen är aktiv ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Annars kommer APIM:s `<openid-config>`-anrop att ge 404.

- **Audience-claim:** Springs standardbeteende är att sätta `aud`-claim till klient-ID. Om APIM:s `<audience>`-kontroll misslyckas kan du behöva anpassa token (som visat ovan) eller justera APIM-policyn. Se till att audience i din JWT matchar vad du konfigurerar i `<audience>`.

- **JSON Metadata Parsing:** OpenID-konfigurations-JSON måste vara giltig. Springs standardkonfiguration genererar ett standard OIDC-metadata-dokument. Kontrollera att det innehåller korrekt `issuer` och `jwks_uri`. Om du kör Spring bakom en proxy eller path-baserad routning, dubbelkolla URL:erna i denna metadata. APIM använder dessa värden som de är.

- **Policyordning:** I APIM-policyn, placera `<validate-jwt>` **före** all routing till backend. Annars kan anrop nå din app utan giltig token. Se också till att `<validate-jwt>` ligger direkt under `<inbound>` (inte inbäddad i en annan condition) så att APIM tillämpar den.

Genom att följa ovanstående steg kan du köra din Spring AI MCP-server i Azure Container Apps och låta Azure API Management validera inkommande OAuth2 JWT med en minimal policy. Nyckelpunkterna är: exponera Spring Auth-endpoints publikt med TLS, aktivera OIDC-discovery och peka APIM:s `validate-jwt` mot OpenID-konfigurations-URL:en (så att den kan hämta JWKS automatiskt). Denna setup passar för dev/test-miljö; för produktion bör du överväga korrekt hantering av hemligheter, tokenlivslängder och rotation av nycklar i JWKS vid behov.
**Referenser:** Se Spring Authorization Server-dokumentationen för standardendpoints ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) och OIDC-konfiguration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); se Microsoft APIM-dokumentationen för exempel på `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); och Azure Container Apps-dokumentationen för distribution och certifikat ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.