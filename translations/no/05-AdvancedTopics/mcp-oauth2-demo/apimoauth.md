# Distribuere Spring AI MCP-app til Azure Container Apps

 ([Sikring av Spring AI MCP-servere med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figur: Spring AI MCP-server sikret med Spring Authorization Server. Serveren utsteder tilgangstokener til klienter og validerer dem ved innkommende forespørsler (kilde: Spring-bloggen) ([Sikring av Spring AI MCP-servere med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* For å distribuere Spring MCP-serveren, bygg den som en container og bruk Azure Container Apps med ekstern ingress. For eksempel kan du med Azure CLI kjøre:

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

Dette oppretter en offentlig tilgjengelig Container App med HTTPS aktivert (Azure utsteder et gratis TLS-sertifikat for standard `*.azurecontainerapps.io`-domene ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Kommandoens utdata inkluderer appens FQDN (f.eks. `my-mcp-app.eastus.azurecontainerapps.io`), som blir basis for **issuer URL**. Sørg for at HTTP-ingress er aktivert (som vist over) slik at APIM kan nå appen. I en test-/utviklingsoppsett, bruk `--ingress external`-alternativet (eller bind et egendefinert domene med TLS i henhold til [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Lagre sensitive egenskaper (som OAuth-klienthemmeligheter) i Container Apps secrets eller Azure Key Vault, og map dem inn i containeren som miljøvariabler.

## Konfigurere Spring Authorization Server

I koden til din Spring Boot-app, inkluder Spring Authorization Server og Resource Server starters. Konfigurer en `RegisteredClient` (for `client_credentials`-grant i dev/test) og en JWT-nøkkelkilde. For eksempel kan du i `application.properties` sette:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Aktiver Authorization Server og Resource Server ved å definere en sikkerhetsfilterkjede. For eksempel:

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

Denne oppsettet vil eksponere standard OAuth2-endepunkter: `/oauth2/token` for tokens og `/oauth2/jwks` for JSON Web Key Set. (Som standard mapper Spring sin `AuthorizationServerSettings` `/oauth2/token` og `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Serveren vil utstede JWT-tilgangstokener signert med RSA-nøkkelen over, og publisere sin offentlige nøkkel på `https://<your-app>:/oauth2/jwks`.

**Aktiver OpenID Connect discovery:** For at APIM automatisk skal hente issuer og JWKS, aktiver OIDC provider-konfigurasjonsendepunktet ved å legge til `.oidc(Customizer.withDefaults())` i sikkerhetskonfigurasjonen din ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). For eksempel:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Dette eksponerer `/.well-known/openid-configuration`, som APIM kan bruke for metadata. Til slutt kan det være ønskelig å tilpasse JWT-**audience**-claim slik at APIMs `<audiences>`-sjekk vil godkjennes. For eksempel, legg til en token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Dette sikrer at tokenene inneholder `"aud": ["mcp-client"]`, som matcher klient-ID eller scope forventet av APIM.

## Eksponere Token- og JWKS-endepunkter

Etter distribusjon vil appens **issuer URL** være `https://<app-fqdn>`, f.eks. `https://my-mcp-app.eastus.azurecontainerapps.io`. Dens OAuth2-endepunkter er:

- **Token-endepunkt:** `https://<app-fqdn>/oauth2/token` – klienter henter tokens her (client_credentials flow).
- **JWKS-endepunkt:** `https://<app-fqdn>/oauth2/jwks` – returnerer JWK-settet (brukes av APIM for å hente signeringsnøkler).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (inneholder `issuer`, `token_endpoint`, `jwks_uri`, osv.).

APIM vil peke til **OpenID-konfigurasjons-URLen**, hvorfra den oppdager `jwks_uri`. For eksempel, hvis Container App FQDN er `my-mcp-app.eastus.azurecontainerapps.io`, skal APIMs `<openid-config url="...">` bruke `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Som standard setter Spring `issuer` i denne metadataen til samme basis-URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfigurere Azure API Management (`validate-jwt`)

I Azure APIM, legg til en inbound policy som bruker `<validate-jwt>` for å sjekke innkommende JWT-er mot din Spring Authorization Server. For en enkel oppsett kan du bruke OpenID Connect metadata-URL. Eksempel på policy-snutt:

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

Denne policyen forteller APIM å hente OpenID-konfigurasjonen fra Spring Auth Server, hente JWKS, og validere at hvert token er signert med en betrodd nøkkel og har riktig audience. (Hvis du utelater `<issuers>`, vil APIM automatisk bruke `issuer`-claim fra metadataen.) `<audience>` bør matche klient-ID eller API-ressursnavnet i tokenet (i eksempelet over satte vi det til `"mcp-client"`). Dette er i tråd med Microsofts dokumentasjon om bruk av `validate-jwt` med `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Etter validering vil APIM videresende forespørselen (inkludert original `Authorization`-header) til backend. Siden Spring-appen også er en resource server, vil den re-validere tokenet, men APIM har allerede sikret gyldigheten. (For utvikling kan du stole på APIMs sjekk og deaktivere ekstra sjekker i appen om ønskelig, men det er tryggere å beholde begge.)

## Eksempelinnstillinger

| Innstilling         | Eksempelverdi                                                      | Notater                                    |
|---------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL-en til din Container App (base URI)   |
| **Token endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Standard Spring token-endepunkt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Standard JWK Set-endepunkt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery-dokument (auto-generert)    |
| **APIM audience**   | `mcp-client`                                                      | OAuth klient-ID eller API-ressursnavn      |
| **APIM policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` bruker denne URL-en ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Vanlige fallgruver

- **HTTPS/TLS:** APIM-gatewayen krever at OpenID/JWKS-endepunktet bruker HTTPS med gyldig sertifikat. Som standard tilbyr Azure Container Apps et betrodd TLS-sertifikat for Azure-administrerte domener ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Hvis du bruker et egendefinert domene, må du sørge for å binde et sertifikat (du kan bruke Azures gratis administrerte sertifikat-funksjon) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Hvis APIM ikke kan stole på sertifikatet til endepunktet, vil `<validate-jwt>` feile i å hente metadata.

- **Endepunkt-tilgjengelighet:** Sørg for at Spring-appens endepunkter er tilgjengelige fra APIM. Å bruke `--ingress external` (eller aktivere ingress i portalen) er enklest. Hvis du valgte et internt eller vNet-begrenset miljø, kan det hende APIM (som som standard er offentlig) ikke når det med mindre det er i samme VNet. I en testoppsett anbefales offentlig ingress slik at APIM kan nå `.well-known` og `/jwks`-URLene.

- **OpenID Discovery aktivert:** Som standard eksponerer ikke Spring Authorization Server `/.well-known/openid-configuration` med mindre OIDC er aktivert. Sørg for å inkludere `.oidc(Customizer.withDefaults())` i sikkerhetskonfigurasjonen (se over) slik at provider-konfigurasjonsendepunktet er aktivt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Ellers vil APIMs `<openid-config>`-kall gi 404.

- **Audience-claim:** Spring setter som standard `aud`-claim til klient-ID. Hvis APIMs `<audience>`-sjekk feiler, må du kanskje tilpasse tokenet (som vist over) eller justere APIM-policyen. Sørg for at audience i JWT matcher det du konfigurerer i `<audience>`.

- **JSON Metadata Parsing:** OpenID-konfigurasjons-JSON må være gyldig. Spring sin standardkonfigurasjon vil generere et standard OIDC-metadata-dokument. Verifiser at det inneholder korrekt `issuer` og `jwks_uri`. Hvis du kjører Spring bak en proxy eller path-basert rute, dobbeltsjekk URLene i metadataen. APIM bruker disse verdiene som de er.

- **Policy-rekkefølge:** I APIM-policyen må `<validate-jwt>` plasseres **før** all ruting til backend. Ellers kan kall nå appen uten gyldig token. Sørg også for at `<validate-jwt>` vises rett under `<inbound>` (ikke inne i en annen betingelse) slik at APIM anvender den.

Ved å følge stegene over kan du kjøre din Spring AI MCP-server i Azure Container Apps og la Azure API Management validere innkommende OAuth2 JWT-er med en minimal policy. Hovedpunktene er: eksponer Spring Auth-endepunktene offentlig med TLS, aktiver OIDC discovery, og pek APIMs `validate-jwt` til OpenID-konfigurasjons-URLen (slik at den kan hente JWKS automatisk). Dette oppsettet passer for dev/test-miljø; for produksjon bør du vurdere riktig hemmelighetshåndtering, token-levetider og rotering av nøkler i JWKS etter behov.
**Referanser:** Se Spring Authorization Server-dokumentasjonen for standardendepunkter ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) og OIDC-konfigurasjon ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); se Microsoft APIM-dokumentasjonen for `validate-jwt`-eksempler ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); og Azure Container Apps-dokumentasjonen for distribusjon og sertifikater ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.