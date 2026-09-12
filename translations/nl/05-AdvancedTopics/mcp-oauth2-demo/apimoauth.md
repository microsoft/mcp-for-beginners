# Implementatie van de Spring AI MCP-app op Azure Container Apps

> [!WARNING]
> Deze gecombineerde autorisatie-/resource-server is bedoeld voor leer- en
> ontwikkel-/testgebruik. Productiesystemen moeten een toegewijde identiteitsprovider,
> persistente ondertekeningssleutels en referenties opgeslagen in een beheerde geheime opslag gebruiken.

 ([Beveiliging van Spring AI MCP-servers met OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figuur: Spring AI MCP-server beveiligd met Spring Authorization Server. De server geeft toegangstokens uit aan clients en valideert deze bij inkomende verzoeken (bron: Spring blog) ([Beveiliging van Spring AI MCP-servers met OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Om de Spring MCP-server te implementeren, bouwt u deze als een container en gebruikt u Azure Container Apps met externe ingress. Bijvoorbeeld, met de Azure CLI kunt u het volgende uitvoeren:

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

Dit maakt een publiek toegankelijke Container App met HTTPS ingeschakeld (Azure verstrekt een gratis TLS-certificaat voor het standaard `*.azurecontainerapps.io`-domein ([Aangepaste domeinnamen en gratis beheerde certificaten in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). De uitvoer van het commando bevat de FQDN van de app (bijv. `my-mcp-app.eastus.azurecontainerapps.io`), die de basis wordt van de **issuer URL**. Zorg ervoor dat HTTP ingress is ingeschakeld (zoals hierboven) zodat APIM de app kan bereiken. In een test-/ontwikkelomgeving gebruikt u de optie `--ingress external` (of koppel een aangepast domein met TLS volgens de [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Aangepaste domeinnamen en gratis beheerde certificaten in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Sla gevoelige eigenschappen (zoals OAuth client secrets) op in Container Apps secrets of Azure Key Vault en koppel deze als omgevingsvariabelen in de container.

## Configureren van Spring Authorization Server

Voeg in de code van uw Spring Boot-app de starters voor Spring Authorization Server en Resource Server toe. Configureer een `RegisteredClient` (voor de `client_credentials`-toewijzing in dev/test) en een JWT-sleutelbron. Bijvoorbeeld kunt u in `application.properties` instellen:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Schakel de Authorization Server en Resource Server in door een security filter chain te definiëren. Bijvoorbeeld:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Schakel de eindpunten van de Autorisatieserver in
            .apply(authzServer.and())
            // Schakel de Resource Server in (valideer JWT bij binnenkomende verzoeken)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Schakel CSRF uit (MCP-server is niet browsergebaseerd)
            .csrf(csrf -> csrf.disable())
            // Sta CORS toe voor client demo tools
            .cors(withDefaults());
        return http.build();
    }

    // Definieer een client in het geheugen (RegisteredClient) en een JWK-bron:
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
        // Genereer een RSA-sleutel (voor ontwikkel/test, genereer opnieuw bij opstarten)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Deze configuratie zal de standaard OAuth2-eindpunten blootstellen: `/oauth2/token` voor tokens en `/oauth2/jwks` voor de JSON Web Key Set. (Standaard mapt Spring’s `AuthorizationServerSettings` `/oauth2/token` en `/oauth2/jwks` ([Configuratiemodel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) De server zal JWT toegangstokens uitgeven die ondertekend zijn met de hierboven genoemde RSA-sleutel en de publieke sleutel publiceren op `https://<your-app>:/oauth2/jwks`.

**Schakel OpenID Connect discovery in:** Om APIM automatisch de issuer en JWKS te laten ophalen, schakel het OIDC-providerconfiguratie-eindpunt in door `.oidc(Customizer.withDefaults())` toe te voegen in uw beveiligingsconfiguratie ([Configuratiemodel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Bijvoorbeeld:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– stelt /.well-known/openid-configuration in staat
```

Dit maakt `/.well-known/openid-configuration` beschikbaar, dat APIM kan gebruiken voor metadata. Ten slotte wilt u wellicht de JWT **audience** claim aanpassen zodat de `<audiences>` check van APIM slaagt. Voeg bijvoorbeeld een token customizer toe:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Stel een aangepast publiek in (bijv. de klant-ID of API-identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Dit zorgt ervoor dat tokens `"aud": ["mcp-client"]` bevatten, wat overeenkomt met de client-ID of scope die APIM verwacht.

## Blootstellen van Token- en JWKS-eindpunten

Na implementatie zal de **issuer URL** van uw app `https://<app-fqdn>` zijn, bv. `https://my-mcp-app.eastus.azurecontainerapps.io`. De OAuth2-eindpunten zijn:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – clients verkrijgen hier tokens (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – retourneert de JWK-set (gebruikt door APIM om ondertekeningssleutels op te halen).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (bevat `issuer`, `token_endpoint`, `jwks_uri`, etc.).

APIM wijst naar de **OpenID-configuratie URL**, waarvan het `jwks_uri` ontdekt. Bijvoorbeeld: als uw Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` is, dan moet APIM’s `<openid-config url="...">` gebruiken: `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Standaard zal Spring de `issuer` in die metadata instellen op dezelfde basis-URL ([Configuratiemodel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configureren van Azure API Management (`validate-jwt`)

Voeg in Azure APIM een inbound policy toe die de `<validate-jwt>` policy gebruikt om inkomende JWT’s te controleren tegen uw Spring Authorization Server. Voor een eenvoudige setup kunt u de OpenID Connect metadata URL gebruiken. Voorbeeld van een beleidsfragment:

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

Deze policy vertelt APIM de OpenID-configuratie op te halen van de Spring Auth Server, de JWKS op te halen en te valideren dat elk token is ondertekend met een vertrouwde sleutel en de juiste audience heeft. (Als u `<issuers>` weglaat, gebruikt APIM automatisch de `issuer` claim uit de metadata.) De `<audience>` moet overeenkomen met uw client-ID of API resource identifier in het token (in het bovenstaande voorbeeld is dat `"mcp-client"`). Dit is consistent met Microsoft’s documentatie over het gebruik van `validate-jwt` met `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Na validatie zal APIM het verzoek doorsturen (inclusief de oorspronkelijke `Authorization` header) naar de backend. Omdat de Spring-app ook een resource server is, zal deze het token opnieuw valideren, maar APIM heeft de geldigheid al bevestigd. (Voor ontwikkeling kunt u vertrouwen op de controle van APIM en extra controles in de app uitschakelen, maar het is veiliger om beide te behouden.)

## Voorbeeldinstellingen

| Instelling           | Voorbeeldwaarde                                                      | Opmerkingen                                |
|---------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL van uw Container App (basis URI)      |
| **Token endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Standaard Spring token endpoint ([Configuratiemodel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Standaard JWK Set endpoint ([Configuratiemodel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery document (automatisch gegenereerd) |
| **APIM audience**   | `mcp-client`                                                         | OAuth client ID of API resource naam      |
| **APIM policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` gebruikt deze URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Veelvoorkomende valkuilen

- **HTTPS/TLS:** De APIM gateway vereist dat het OpenID/JWKS-eindpunt HTTPS met een geldig certificaat is. Standaard levert Azure Container Apps een vertrouwd TLS-certificaat voor het Azure-beheerde domein ([Aangepaste domeinnamen en gratis beheerde certificaten in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Als u een aangepast domein gebruikt, zorg dan dat u een certificaat koppelt (u kunt gebruik maken van Azure’s gratis beheerde certificaatfunctie) ([Aangepaste domeinnamen en gratis beheerde certificaten in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Als APIM het certificaat van het eindpunt niet vertrouwt, zal `<validate-jwt>` het ophalen van de metadata niet kunnen voltooien.

- **Toegankelijkheid van het eindpunt:** Zorg dat de eindpunten van de Spring-app bereikbaar zijn vanuit APIM. Gebruik van `--ingress external` (of het inschakelen van ingress in de portal) is het eenvoudigst. Als u een interne of vNet-gebonden omgeving koos, kan APIM (standaard publiek) deze mogelijk niet bereiken tenzij ze in hetzelfde vNet geplaatst zijn. In een testopstelling verdient openbaar ingress de voorkeur zodat APIM de URL’s van `.well-known` en `/jwks` kan aanroepen.

- **OpenID Discovery ingeschakeld:** Standaard stelt Spring Authorization Server **niet beschikbaar** `/.well-known/openid-configuration` tenzij OIDC is ingeschakeld. Zorg ervoor dat u `.oidc(Customizer.withDefaults())` in uw beveiligingsconfiguratie opneemt (zie hierboven) zodat het providerconfiguratie-eindpunt actief is ([Configuratiemodel :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Anders zal APIM’s `<openid-config>` oproep een 404-fout geven.

- **Audience Claim:** De standaardinstelling van Spring is om de `aud`-claim te zetten op de client-ID. Als APIM’s `<audience>`-controle faalt, moet u mogelijk het token aanpassen (zoals hierboven getoond) of de APIM-policy aanpassen. Zorg dat de audience in uw JWT overeenkomt met wat u in `<audience>` configureert.

- **Parsing van JSON-metadata:** De OpenID-configuratie JSON moet geldig zijn. Spring’s standaardconfiguratie zal een standaard OIDC-metadata document uitgeven. Controleer dat het de correcte `issuer` en `jwks_uri` bevat. Als u Spring achter een proxy of padgebaseerde route host, controleer dan de URLs in deze metadata. APIM gebruikt deze waarden precies zoals ze zijn.

- **Volgorde van policies:** Plaats `<validate-jwt>` in de APIM-policy **voor** elke routering naar de backend. Anders kunnen aanvragen uw app bereiken zonder geldig token. Zorg er ook voor dat `<validate-jwt>` onmiddellijk onder `<inbound>` staat (niet genest binnen een andere voorwaarde) zodat APIM het toepast.

Door bovenstaande stappen te volgen kunt u uw Spring AI MCP-server in Azure Container Apps draaien en Azure API Management laten valideren van binnenkomende OAuth2 JWT’s met een minimale policy. De belangrijkste punten zijn: stel de Spring Auth-eindpunten publiekelijk bloot met TLS, schakel OIDC-discovery in en wijs APIM’s `validate-jwt` toe naar de OpenID-configuratie-URL (zodat het automatisch de JWKS kan ophalen). Deze opzet is geschikt voor een dev/test-omgeving; voor productie overweeg goede geheimbeheer, tokenlevensduur en rotatie van sleutels in JWKS waar nodig.


**Referenties:** Zie de Spring Authorization Server documentatie voor standaard eindpunten ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) en OIDC-configuratie ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); zie Microsoft APIM-documentatie voor `validate-jwt` voorbeelden ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); en Azure Container Apps documentatie voor implementatie en certificaten ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->