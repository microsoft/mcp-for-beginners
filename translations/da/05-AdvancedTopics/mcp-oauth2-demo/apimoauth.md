# Udrulning af Spring AI MCP App til Azure Container Apps

 ([Sikring af Spring AI MCP-servere med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figur: Spring AI MCP-server sikret med Spring Authorization Server. Serveren udsteder adgangstokens til klienter og validerer dem ved indkommende forespørgsler (kilde: Spring blog) ([Sikring af Spring AI MCP-servere med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* For at udrulle Spring MCP-serveren, byg den som en container og brug Azure Container Apps med ekstern ingress. For eksempel kan du med Azure CLI køre:

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

Dette opretter en offentligt tilgængelig Container App med HTTPS aktiveret (Azure udsteder et gratis TLS-certifikat til standarddomænet `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Kommandoens output inkluderer app’ens FQDN (f.eks. `my-mcp-app.eastus.azurecontainerapps.io`), som bliver basis for **issuer URL**. Sørg for, at HTTP ingress er aktiveret (som ovenfor), så APIM kan nå appen. I et test-/dev-miljø, brug `--ingress external`-optionen (eller bind et brugerdefineret domæne med TLS ifølge [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Gem eventuelle følsomme egenskaber (som OAuth client secrets) i Container Apps secrets eller Azure Key Vault, og map dem ind i containeren som miljøvariabler.

## Konfiguration af Spring Authorization Server

I din Spring Boot-apps kode, inkluder Spring Authorization Server og Resource Server starters. Konfigurer en `RegisteredClient` (til `client_credentials` grant i dev/test) og en JWT nøglekilde. For eksempel kan du i `application.properties` sætte:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Aktivér Authorization Server og Resource Server ved at definere en security filter chain. For eksempel:

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

Denne opsætning eksponerer standard OAuth2 endpoints: `/oauth2/token` til tokens og `/oauth2/jwks` til JSON Web Key Set. (Som standard mapper Spring’s `AuthorizationServerSettings` `/oauth2/token` og `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Serveren udsteder JWT adgangstokens signeret med RSA-nøglen ovenfor og offentliggør sin offentlige nøgle på `https://<your-app>:/oauth2/jwks`.

**Aktivér OpenID Connect discovery:** For at lade APIM automatisk hente issuer og JWKS, aktiver OIDC provider konfigurations-endpoint ved at tilføje `.oidc(Customizer.withDefaults())` i din sikkerhedskonfiguration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). For eksempel:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Dette eksponerer `/.well-known/openid-configuration`, som APIM kan bruge til metadata. Til sidst vil du måske tilpasse JWT **audience** claim, så APIM’s `<audiences>`-check passer. For eksempel, tilføj en token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Dette sikrer, at tokens indeholder `"aud": ["mcp-client"]`, som matcher klient-ID eller scope forventet af APIM.

## Eksponering af Token- og JWKS-endpoints

Efter udrulning vil din apps **issuer URL** være `https://<app-fqdn>`, f.eks. `https://my-mcp-app.eastus.azurecontainerapps.io`. Dens OAuth2 endpoints er:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – her henter klienter tokens (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – returnerer JWK-sættet (bruges af APIM til at hente signeringsnøgler).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (indeholder `issuer`, `token_endpoint`, `jwks_uri` osv.).

APIM peger på **OpenID konfigurations-URL’en**, hvorfra den finder `jwks_uri`. For eksempel, hvis din Container App FQDN er `my-mcp-app.eastus.azurecontainerapps.io`, skal APIM’s `<openid-config url="...">` bruge `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Som standard sætter Spring `issuer` i denne metadata til samme basis-URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfiguration af Azure API Management (`validate-jwt`)

I Azure APIM, tilføj en inbound policy, der bruger `<validate-jwt>` til at validere indkommende JWT’er mod din Spring Authorization Server. Til en simpel opsætning kan du bruge OpenID Connect metadata-URL’en. Eksempel på policy snippet:

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

Denne policy fortæller APIM at hente OpenID konfigurationen fra Spring Auth Server, hente dens JWKS og validere, at hvert token er signeret med en betroet nøgle og har korrekt audience. (Hvis du udelader `<issuers>`, bruger APIM automatisk `issuer`-claim fra metadata.) `<audience>` skal matche dit klient-ID eller API-ressourceidentifikator i tokenet (i eksemplet ovenfor satte vi det til `"mcp-client"`). Dette er i overensstemmelse med Microsofts dokumentation om brug af `validate-jwt` med `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Efter validering videresender APIM forespørgslen (inklusive den oprindelige `Authorization` header) til backend. Da Spring-appen også er en resource server, vil den genvalidere tokenet, men APIM har allerede sikret dets gyldighed. (Til udvikling kan du stole på APIM’s check og deaktivere yderligere checks i appen, hvis ønsket, men det er sikrere at beholde begge.)

## Eksempelindstillinger

| Indstilling         | Eksempelværdi                                                      | Noter                                      |
|---------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | Din Container Apps URL (basis-URI)         |
| **Token endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Standard Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Standard JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery dokument (automatisk genereret) |
| **APIM audience**   | `mcp-client`                                                      | OAuth client ID eller API-ressourcenavn    |
| **APIM policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` bruger denne URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Almindelige faldgruber

- **HTTPS/TLS:** APIM gateway kræver, at OpenID/JWKS endpoint er HTTPS med et gyldigt certifikat. Som standard leverer Azure Container Apps et betroet TLS-certifikat til det Azure-administrerede domæne ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Hvis du bruger et brugerdefineret domæne, skal du sørge for at binde et certifikat (du kan bruge Azures gratis managed cert-funktion) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Hvis APIM ikke kan stole på endpointets certifikat, vil `<validate-jwt>` fejle i at hente metadata.

- **Endpoint tilgængelighed:** Sørg for, at Spring-appens endpoints er tilgængelige fra APIM. Brug af `--ingress external` (eller aktivering af ingress i portalen) er det nemmeste. Hvis du valgte et internt eller vNet-bundet miljø, kan APIM (som som standard er offentligt) muligvis ikke nå det, medmindre det placeres i samme VNet. I et testmiljø anbefales offentlig ingress, så APIM kan kalde `.well-known` og `/jwks` URL’erne.

- **OpenID Discovery aktiveret:** Som standard eksponerer Spring Authorization Server **ikke** `/.well-known/openid-configuration`, medmindre OIDC er aktiveret. Sørg for at inkludere `.oidc(Customizer.withDefaults())` i din sikkerhedskonfiguration (se ovenfor), så provider konfigurations-endpoint er aktivt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Ellers vil APIM’s `<openid-config>` kald returnere 404.

- **Audience Claim:** Spring sætter som standard `aud` claim til klient-ID. Hvis APIM’s `<audience>` check fejler, kan du have behov for at tilpasse tokenet (som vist ovenfor) eller justere APIM policyen. Sørg for, at audience i din JWT matcher det, du konfigurerer i `<audience>`.

- **JSON Metadata Parsing:** OpenID konfigurations-JSON skal være gyldig. Spring’s standardkonfiguration udsender et standard OIDC metadata dokument. Kontroller, at det indeholder korrekt `issuer` og `jwks_uri`. Hvis du hoster Spring bag en proxy eller path-baseret rute, dobbelttjek URL’erne i denne metadata. APIM bruger disse værdier som de er.

- **Policy rækkefølge:** I APIM policyen skal `<validate-jwt>` placeres **før** routing til backend. Ellers kan kald nå din app uden et gyldigt token. Sørg også for, at `<validate-jwt>` står direkte under `<inbound>` (ikke indlejret i en anden betingelse), så APIM anvender den.

Ved at følge ovenstående trin kan du køre din Spring AI MCP-server i Azure Container Apps og lade Azure API Management validere indkommende OAuth2 JWT’er med en minimal policy. De vigtigste punkter er: eksponer Spring Auth endpoints offentligt med TLS, aktiver OIDC discovery, og peg APIM’s `validate-jwt` på OpenID konfigurations-URL’en (så den automatisk kan hente JWKS). Denne opsætning er velegnet til dev/test-miljø; til produktion bør du overveje korrekt hemmelighedshåndtering, token-levetider og rotation af nøgler i JWKS efter behov.
**Referencer:** Se Spring Authorization Server-dokumentationen for standardendepunkter ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) og OIDC-konfiguration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); se Microsoft APIM-dokumentationen for `validate-jwt`-eksempler ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); og Azure Container Apps-dokumentationen for udrulning og certifikater ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.