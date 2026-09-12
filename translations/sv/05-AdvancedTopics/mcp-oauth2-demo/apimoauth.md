# Distribuerar Spring AI MCP-app till Azure Container Apps

> [!WARNING]
> Denna kombinerade auktoriserings-/resursserver är avsedd för lärande och
> utvecklings-/testanvändning. Produktionssystem bör använda en dedikerad identitetsleverantör,
> persistenta signeringsnycklar och autentiseringsuppgifter som lagras i en hanterad hemlighetshanterare.

 ([Säkra Spring AI MCP-servrar med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figur: Spring AI MCP-server säkrad med Spring Authorization Server. Servern utfärdar åtkomsttoken till klienter och validerar dem vid inkommande förfrågningar (källa: Spring blog) ([Säkra Spring AI MCP-servrar med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* För att distribuera Spring MCP-servern, bygg den som en container och använd Azure Container Apps med extern ingress. Till exempel kan du med Azure CLI köra:

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

Detta skapar en publikt tillgänglig Container App med HTTPS aktiverat (Azure utfärdar ett gratis TLS-certifikat för standarddomänen `*.azurecontainerapps.io` ([Anpassade domännamn och gratis hanterade certifikat i Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Kommandots utdata inkluderar appens FQDN (t.ex. `my-mcp-app.eastus.azurecontainerapps.io`), vilket blir basen för **issuer URL**. Säkerställ att HTTP-ingress är aktiverat (som ovan) så att APIM kan nå appen. I en test-/utvecklingsmiljö, använd alternativet `--ingress external` (eller bind en anpassad domän med TLS enligt [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Anpassade domännamn och gratis hanterade certifikat i Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Lagra eventuella känsliga egenskaper (som OAuth-klienthemligheter) i Container Apps hemligheter eller Azure Key Vault och mappa dem in i containern som miljövariabler.

## Konfigurera Spring Authorization Server

Inkludera i din Spring Boot-apps kod Spring Authorization Server och Resource Server starters. Konfigurera en `RegisteredClient` (för `client_credentials`-beviljandet i utveckling/test) och en JWT-nyckelkälla. Till exempel, i `application.properties` kan du ställa in:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Aktivera Authorization Server och Resource Server genom att definiera en säkerhetsfilterkedja. Till exempel:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Aktivera auktoriseringsserverns slutpunkter
            .apply(authzServer.and())
            // Aktivera resurservern (validera JWT på inkommande förfrågningar)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Inaktivera CSRF (MCP-servern är inte webbläsarbaserad)
            .csrf(csrf -> csrf.disable())
            // Tillåt CORS för klientdemoverktyg
            .cors(withDefaults());
        return http.build();
    }

    // Definiera en klient i minnet (RegisteredClient) och en JWK-källa:
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
        // Generera en RSA-nyckel (för utveckling/test, generera på nytt vid uppstart)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Denna setup kommer exponera standard OAuth2-endpoints: `/oauth2/token` för token och `/oauth2/jwks` för JSON Web Key Set. (Som standard mappar Spring’s `AuthorizationServerSettings` `/oauth2/token` och `/oauth2/jwks` ([Konfigurationsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Servern kommer att utfärda JWT-åtkomsttoken signerade med RSA-nyckeln ovan, och publicera sin publika nyckel på `https://<your-app>:/oauth2/jwks`.

**Aktivera OpenID Connect discovery:** För att låta APIM automatiskt hämta issuer och JWKS, aktivera OIDC-provider-konfigurationsendpoint genom att lägga till `.oidc(Customizer.withDefaults())` i din säkerhetskonfiguration ([Konfigurationsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Till exempel:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– aktiverar /.well-known/openid-configuration
```

Detta exponerar `/.well-known/openid-configuration`, som APIM kan använda för metadata. Slutligen kan du vilja anpassa JWT:s **audience**-claim så att APIM:s `<audiences>`-kontroll klaras. Till exempel, lägg till en tokenanpassare:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Ange en anpassad målgrupp (t.ex. klient-ID eller API-identifierare)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Detta säkerställer att token innehåller `"aud": ["mcp-client"]`, som matchar klient-ID eller scope som APIM förväntar sig.

## Exponera Token- och JWKS-endpoints

Efter distribution kommer din apps **issuer URL** vara `https://<app-fqdn>`, t.ex. `https://my-mcp-app.eastus.azurecontainerapps.io`. Dess OAuth2-endpoints är:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – här hämtar klienter token (client_credentials-flöde).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – returnerar JWK-setet (används av APIM för att hämta signeringsnycklar).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (innehåller `issuer`, `token_endpoint`, `jwks_uri`, etc.).

APIM pekar på **OpenID-konfigurations-URL**, från vilken det upptäcker `jwks_uri`. Till exempel, om din Container Apps FQDN är `my-mcp-app.eastus.azurecontainerapps.io`, då ska APIM:s `<openid-config url="...">` använda `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Som standard sätter Spring `issuer` i denna metadata till samma bas-URL ([Konfigurationsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfigurera Azure API Management (`validate-jwt`)

I Azure APIM lägger du till en inbound-policy som använder `<validate-jwt>`-policyn för att kontrollera inkommande JWT mot din Spring Authorization Server. För en enkel setup kan du använda OpenID Connect metadata-URL. Exempel på policyskicka:

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

Denna policy instruerar APIM att hämta OpenID-konfigurationen från Spring Auth Server, hämta dess JWKS och validera att varje token är signerad av en betrodd nyckel och har rätt audience. (Om du utelämnar `<issuers>` kommer APIM automatiskt använda `issuer`-claimen från metadata.) `<audience>` ska matcha ditt klient-ID eller API-resursidentifierare i token (i exemplet ovan satte vi det till `"mcp-client"`). Detta är i linje med Microsofts dokumentation om att använda `validate-jwt` med `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Efter validering skickar APIM vidare förfrågan (inklusive det ursprungliga `Authorization`-huvudet) till backend. Eftersom Spring-appen även är en resursserver kommer den att validera token igen, men APIM har redan säkerställt dess giltighet. (För utveckling kan du förlita dig på APIM:s kontroll och inaktivera ytterligare kontroller i appen om så önskas, men det är säkrare att behålla båda.)

## Exempelininställningar

| Inställning         | Exempelvärde                                                      | Noteringar                                  |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | Din Container Apps URL (bas-URI)            |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Standard endpoint för Spring-token ([Konfigurationsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Standard JWK Set-endpoint ([Konfigurationsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery-dokument (auto-genererat)      |
| **APIM audience**  | `mcp-client`                                                      | OAuth klient-ID eller API-resursnamn        |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` använder denna URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Vanliga fallgropar

- **HTTPS/TLS:** APIM-gateway kräver att OpenID/JWKS-endpoint är HTTPS med ett giltigt certifikat. Som standard tillhandahåller Azure Container Apps ett betrott TLS-certifikat för Azure-hanterad domän ([Anpassade domännamn och gratis hanterade certifikat i Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Om du använder en anpassad domän, se till att binda ett certifikat (du kan använda Azures gratis hanterade certifikatfunktion) ([Anpassade domännamn och gratis hanterade certifikat i Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Om APIM inte kan lita på endpointens certifikat kommer `<validate-jwt>` att misslyckas med att hämta metadata.  

- **Endpoint-tillgänglighet:** Säkerställ att Spring-appens endpoints är nåbara från APIM. Att använda `--ingress external` (eller aktivera ingress i portalen) är enklast. Om du valt en intern eller VNet-bunden miljö kanske inte APIM (som standard publik) når den om den inte är i samma VNet. I en testmiljö, föredra publik ingress så att APIM kan nå `.well-known` och `/jwks` URL:erna.

- **OpenID Discovery aktiverat:** Som standard exponerar inte Spring Authorization Server `/.well-known/openid-configuration` om inte OIDC är aktiverat. Se till att inkludera `.oidc(Customizer.withDefaults())` i din säkerhetskonfiguration (se ovan) så att provider-konfigurationsendpointen är aktiv ([Konfigurationsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Annars kommer APIM:s `<openid-config>`-anrop att ge 404.

- **Audience Claim:** Springs standardbeteende är att sätta `aud`-claimen till klient-ID. Om APIM:s `<audience>`-kontroll misslyckas kan du behöva anpassa token (som visat ovan) eller justera APIM-policyn. Säkerställ att audience i din JWT matchar det du konfigurerar i `<audience>`.

- **Parsing av JSON-metadata:** OpenID-konfigurations-JSON måste vara giltig. Springs standardkonfiguration genererar ett standard OIDC-metadata-dokument. Verifiera att det innehåller korrekt `issuer` och `jwks_uri`. Om du hostar Spring bakom en proxy eller path-baserad route, dubbelkolla URL:erna i denna metadata. APIM kommer att använda dessa värden som de är.

- **Policy-ordning:** I APIM-policyn, placera `<validate-jwt>` **före** alla routing till backend. Annars kan anrop nå din app utan giltig token. Se också till att `<validate-jwt>` ligger direkt under `<inbound>` (inte inuti ett annat villkor) så att APIM tillämpar det.

Genom att följa ovanstående steg kan du köra din Spring AI MCP-server i Azure Container Apps och låta Azure API Management validera inkommande OAuth2 JWT med en minimal policy. Nyckelpunkterna är: exponera Spring Auth-endpoints publikt med TLS, aktivera OIDC discovery och peka APIM:s `validate-jwt` mot OpenID-konfigurations-URL:en (så att den automatiskt kan hämta JWKS). Denna setup är lämplig för en utvecklings-/testmiljö; för produktion, överväg korrekt hemlighetshantering, tokenlivslängder och rotering av nycklar i JWKS vid behov.


**Referenser:** Se Spring Authorization Server-dokumentationen för standardendpunkter ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) och OIDC-konfiguration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); se Microsoft APIM-dokument för exempel på `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); och Azure Container Apps-dokument för distribution och certifikat ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->