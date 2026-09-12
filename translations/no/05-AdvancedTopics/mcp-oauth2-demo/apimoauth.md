# Distribuere Spring AI MCP-appen til Azure Container Apps

> [!WARNING]
> Denne kombinerte autorisasjons-/ressursserveren er ment for opplæring og
> utviklings-/testbruk. Produksjonssystemer bør bruke en dedikert identitetsleverandør,
> permanente signeringsnøkler og legitimasjon lagret i en administrert hemmelighetslagring.

 ([Sikring av Spring AI MCP-servere med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figur: Spring AI MCP-server sikret med Spring Authorization Server. Serveren utsteder tilgangstokener til klienter og validerer dem ved innkommende forespørsler (kilde: Spring-blogg) ([Sikring av Spring AI MCP-servere med OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* For å distribuere Spring MCP-serveren, bygg den som en container og bruk Azure Container Apps med ekstern inngang. For eksempel kan du med Azure CLI kjøre:

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

Dette oppretter en offentlig tilgjengelig Container App med HTTPS aktivert (Azure utsteder et gratis TLS-sertifikat for standarddomene `*.azurecontainerapps.io` ([Egendefinerte domenenavn og gratis administrerte sertifikater i Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Kommandoresultatet inkluderer appens FQDN (f.eks. `my-mcp-app.eastus.azurecontainerapps.io`), som blir grunnlaget for **issuer URL**. Sørg for at HTTP-inngang er aktivert (som ovenfor) slik at APIM kan nå appen. I en test-/dev-oppsett, bruk `--ingress external`-alternativet (eller bind et egendefinert domene med TLS i henhold til [Microsoft-dokumentasjon](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Egendefinerte domenenavn og gratis administrerte sertifikater i Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Lagre sensitive egenskaper (som OAuth-klienthemmeligheter) i Container Apps secrets eller Azure Key Vault, og kartlegg dem inn i containeren som miljøvariabler. 

## Konfigurere Spring Authorization Server

I koden til din Spring Boot-app, inkluder Spring Authorization Server- og Resource Server-startere. Konfigurer en `RegisteredClient` (for `client_credentials`-grant i dev/test) og en JWT nøkkelkilde. For eksempel, i `application.properties` kan du sette:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
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
            // Aktiver Autorisasjonsserver-endepunktene
            .apply(authzServer.and())
            // Aktiver Ressursserveren (valider JWT på innkommende forespørsler)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Deaktiver CSRF (MCP-serveren er ikke nettleserbasert)
            .csrf(csrf -> csrf.disable())
            // Tillat CORS for klientdemo-verktøy
            .cors(withDefaults());
        return http.build();
    }

    // Definer en klient i minnet (RegisteredClient) og en JWK-kilde:
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
        // Generer en RSA-nøkkel (for utvikling/test, generer på nytt ved oppstart)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Dette oppsettet vil eksponere standard OAuth2-endepunkter: `/oauth2/token` for token og `/oauth2/jwks` for JSON Web Key Set. (Som standard mapper Spring sin `AuthorizationServerSettings` `/oauth2/token` og `/oauth2/jwks` ([Konfigurasjonsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Serveren vil utstede JWT-tilgangstokener signert med RSA-nøkkelen over, og publisere sin offentlige nøkkel på `https://<ditt-app>:/oauth2/jwks`. 

**Aktiver OpenID Connect-discovery:** For å la APIM automatisk hente issuer og JWKS, aktiver OIDC provider-config-endepunktet ved å legge til `.oidc(Customizer.withDefaults())` i sikkerhetskonfigurasjonen din ([Konfigurasjonsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). For eksempel:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– aktiverer /.well-known/openid-configuration
```

Dette eksponerer `/.well-known/openid-configuration`, som APIM kan bruke for metadata. Til slutt kan det hende du vil tilpasse JWT **audience**-kravet slik at APIMs `<audiences>`-sjekk godtar det. For eksempel, legg til en token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Sett et egendefinert publikum (f.eks. klient-ID eller API-identifikator)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Dette sikrer at tokens bærer `"aud": ["mcp-client"]`, som samsvarer med klient-ID eller omfanget som APIM forventer. 

## Eksponere Token- og JWKS-endepunkter

Etter distribusjon vil appens **issuer URL** være `https://<app-fqdn>`, f.eks. `https://my-mcp-app.eastus.azurecontainerapps.io`. Dets OAuth2-endepunkter er:

- **Token-endepunkt:** `https://<app-fqdn>/oauth2/token` – klienter henter token her (client_credentials flyt).
- **JWKS-endepunkt:** `https://<app-fqdn>/oauth2/jwks` – returnerer JWK-settet (brukes av APIM for å hente signeringsnøkler).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (inneholder `issuer`, `token_endpoint`, `jwks_uri`, osv.).  

APIM vil peke på **OpenID-config URL**, som den bruker for å oppdage `jwks_uri`. For eksempel, hvis Container App FQDN er `my-mcp-app.eastus.azurecontainerapps.io`, skal APIMs `<openid-config url="...">` bruke `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Som standard setter Spring `issuer` i denne metadataen til samme basis-URL ([Konfigurasjonsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfigurere Azure API Management (`validate-jwt`)

I Azure APIM, legg til en inbound policy som bruker `<validate-jwt>` for å sjekke innkommende JWT-er mot din Spring Authorization Server. For en enkel oppsett kan du bruke OpenID Connect metadata-URL. Eksempel policy-snutt:

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

Denne policyen instruerer APIM til å hente OpenID-konfigurasjonen fra Spring Auth Server, hente dens JWKS, og validere at hvert token er signert med en pålitelig nøkkel og har riktig audience. (Hvis du utelater `<issuers>`, vil APIM automatisk bruke `issuer`-kravet fra metadata.) `<audience>` bør samsvare med klient-ID eller API-ressursidentifikator i tokenet (i eksemplet over satte vi den til `"mcp-client"`). Dette er i tråd med Microsofts dokumentasjon om bruk av `validate-jwt` med `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Etter validering vil APIM videresende forespørselen (inkludert den opprinnelige `Authorization` headeren) til backend. Siden Spring-appen også er en ressursserver, vil den validere tokenet på nytt, men APIM har allerede sikret gyldigheten. (For utvikling kan du stole på APIMs sjekk og deaktivere ytterligere sjekker i appen om ønskelig, men det er sikrere å beholde begge.)

## Eksempelinnstillinger

| Innstilling          | Eksempelverdi                                                       | Notater                                    |
|---------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**           | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL-en til din Container App (base-URI)   |
| **Token-endepunkt**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Standard Spring token-endepunkt ([Konfigurasjonsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS-endepunkt**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Standard JWK Set-endepunkt ([Konfigurasjonsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**    | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery-dokument (automatisk generert)    |
| **APIM audience**    | `mcp-client`                                                      | OAuth klient-ID eller navn på API-ressurs  |
| **APIM policy**      | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` bruker denne URL-en ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Vanlige fallgruver

- **HTTPS/TLS:** APIM-gatewayen krever at OpenID/JWKS-endepunktet er på HTTPS med et gyldig sertifikat. Som standard gir Azure Container Apps et betrodd TLS-sertifikat for det Azure-administrerte domenet ([Egendefinerte domenenavn og gratis administrerte sertifikater i Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Hvis du bruker et egendefinert domene, sørg for å binde et sertifikat (du kan bruke Azures gratis administrerte sertifikat-funksjon) ([Egendefinerte domenenavn og gratis administrerte sertifikater i Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Hvis APIM ikke kan stole på endpoint-sertifikatet, vil `<validate-jwt>` mislykkes i å hente metadataen.  

- **Tilgjengelighet av endepunkt:** Sørg for at Spring-appens endepunkter er tilgjengelige fra APIM. Bruk av `--ingress external` (eller å aktivere ingress i portalen) er enklest. Hvis du har valgt et internt eller vNet-avgrenset miljø, kanskje ikke APIM (som er offentlig som standard) når det med mindre det er i samme VNet. I en testoppsett, foretrekk offentlig ingress slik at APIM kan nå `.well-known` og `/jwks` URL-ene. 

- **OpenID Discovery aktivert:** Som standard eksponerer ikke Spring Authorization Server `/.well-known/openid-configuration` med mindre OIDC er aktivert. Husk å inkludere `.oidc(Customizer.withDefaults())` i sikkerhetskonfigurasjonen din (se over) slik at provider-konfigurasjonsendepunktet er aktivt ([Konfigurasjonsmodell :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Ellers vil APIMs `<openid-config>`-kall returnere 404.

- **Audience Claim:** Spring-standardatferd er å sette `aud`-kravet til klient-ID. Hvis APIMs `<audience>`-sjekk feiler, kan du måtte tilpasse tokenet (som vist over) eller justere APIM-policyen. Sørg for at audience i JWT samsvarer med det du konfigurerer i `<audience>`. 

- **Parsing av JSON-metadata:** OpenID konfigurasjons-JSON må være gyldig. Springs standardkonfigurasjon vil generere et standard OIDC metadata-dokument. Bekreft at det inneholder riktig `issuer` og `jwks_uri`. Hvis du kjører Spring bak en proxy eller stibasert rute, sjekk URL-er i denne metadataen nøye. APIM bruker disse verdiene som de er. 

- **Rekkefølge på policy:** I APIM-policyen plasser `<validate-jwt>` **før** eventuelle rutinger til backend. Ellers kan kall nå appen uten gyldig token. Sørg også for at `<validate-jwt>` vises umiddelbart under `<inbound>` (ikke inne i en annen betingelse) slik at APIM anvender den.

Ved å følge trinnene over kan du kjøre din Spring AI MCP-server i Azure Container Apps og la Azure API Management validere innkommende OAuth2 JWT-er med en minimal policy. Nøkkelpunktene er: eksponer Spring Auth-endepunktene offentlig med TLS, aktiver OIDC discovery, og pek APIMs `validate-jwt` til OpenID-config URL (slik at den kan hente JWKS automatisk). Dette oppsettet er egnet for dev/test-miljø; for produksjon bør du vurdere riktig hemmelighetshåndtering, token-livslengder og rotering av nøkler i JWKS etter behov. 


**Referanser:** Se Spring Authorization Server-dokumentasjonen for standard endepunkter ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) og OIDC-konfigurasjon ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); se Microsoft APIM-dokumentasjon for `validate-jwt`-eksempler ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); og Azure Container Apps-dokumentasjon for distribusjon og sertifikater ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->