# Het Spring AI MCP App implementeren naar Azure Container Apps

 ([Beveiliging van Spring AI MCP-servers met OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figuur: Spring AI MCP-server beveiligd met Spring Authorization Server. De server geeft toegangstokens uit aan clients en valideert deze bij binnenkomende verzoeken (bron: Spring blog) ([Beveiliging van Spring AI MCP-servers met OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Om de Spring MCP-server te implementeren, bouw je deze als een container en gebruik je Azure Container Apps met externe ingress. Bijvoorbeeld, met de Azure CLI kun je het volgende uitvoeren:

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

Dit maakt een publiek toegankelijke Container App aan met HTTPS ingeschakeld (Azure verstrekt een gratis TLS-certificaat voor het standaard `*.azurecontainerapps.io` domein ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). De uitvoer van het commando bevat de FQDN van de app (bijv. `my-mcp-app.eastus.azurecontainerapps.io`), wat de basis wordt van de **issuer URL**. Zorg dat HTTP ingress is ingeschakeld (zoals hierboven) zodat APIM de app kan bereiken. In een test-/ontwikkelomgeving gebruik je de optie `--ingress external` (of koppel een aangepast domein met TLS volgens [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Bewaar gevoelige eigenschappen (zoals OAuth client secrets) in Container Apps secrets of Azure Key Vault en koppel deze als omgevingsvariabelen in de container.

## Spring Authorization Server configureren

Voeg in de code van je Spring Boot-app de Spring Authorization Server en Resource Server starters toe. Configureer een `RegisteredClient` (voor de `client_credentials` grant in dev/test) en een JWT key source. Bijvoorbeeld, in `application.properties` kun je instellen:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
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

Deze configuratie maakt de standaard OAuth2-eindpunten beschikbaar: `/oauth2/token` voor tokens en `/oauth2/jwks` voor de JSON Web Key Set. (Standaard mapt Spring’s `AuthorizationServerSettings` `/oauth2/token` en `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) De server geeft JWT toegangstokens uit die zijn ondertekend met de RSA-sleutel hierboven en publiceert de publieke sleutel op `https://<your-app>:/oauth2/jwks`.

**OpenID Connect discovery inschakelen:** Om APIM automatisch de issuer en JWKS te laten ophalen, schakel je het OIDC provider configuratie-eindpunt in door `.oidc(Customizer.withDefaults())` toe te voegen in je securityconfiguratie ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Bijvoorbeeld:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Dit maakt `/.well-known/openid-configuration` beschikbaar, wat APIM kan gebruiken voor metadata. Tot slot wil je mogelijk de JWT **audience** claim aanpassen zodat de `<audiences>` check van APIM slaagt. Voeg bijvoorbeeld een token customizer toe:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Dit zorgt ervoor dat tokens `"aud": ["mcp-client"]` bevatten, wat overeenkomt met de client ID of scope die APIM verwacht.

## Token- en JWKS-eindpunten beschikbaar maken

Na implementatie is de **issuer URL** van je app `https://<app-fqdn>`, bijvoorbeeld `https://my-mcp-app.eastus.azurecontainerapps.io`. De OAuth2-eindpunten zijn:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – hier halen clients tokens op (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – retourneert de JWK set (gebruikt door APIM om ondertekeningssleutels op te halen).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (bevat `issuer`, `token_endpoint`, `jwks_uri`, enz.).

APIM verwijst naar de **OpenID configuratie URL**, waaruit het de `jwks_uri` ontdekt. Bijvoorbeeld, als de FQDN van je Container App `my-mcp-app.eastus.azurecontainerapps.io` is, dan moet APIM’s `<openid-config url="...">` `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` gebruiken. (Standaard stelt Spring de `issuer` in die metadata in op dezelfde basis-URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management configureren (`validate-jwt`)

Voeg in Azure APIM een inbound policy toe die de `<validate-jwt>` policy gebruikt om binnenkomende JWT’s te controleren tegen je Spring Authorization Server. Voor een eenvoudige setup kun je de OpenID Connect metadata URL gebruiken. Voorbeeld van een policy snippet:

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

Deze policy zorgt ervoor dat APIM de OpenID-configuratie van de Spring Auth Server ophaalt, de JWKS verkrijgt en controleert of elk token is ondertekend met een vertrouwde sleutel en de juiste audience bevat. (Als je `<issuers>` weglaat, gebruikt APIM automatisch de `issuer` claim uit de metadata.) De `<audience>` moet overeenkomen met je client ID of API resource identifier in het token (in het bovenstaande voorbeeld is dat `"mcp-client"`). Dit is in lijn met de Microsoft-documentatie over het gebruik van `validate-jwt` met `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Na validatie stuurt APIM het verzoek (inclusief de originele `Authorization` header) door naar de backend. Omdat de Spring-app ook een resource server is, zal deze het token opnieuw valideren, maar APIM heeft de geldigheid al gecontroleerd. (Voor ontwikkeling kun je vertrouwen op de controle van APIM en extra controles in de app uitschakelen als je wilt, maar het is veiliger om beide te behouden.)

## Voorbeeldinstellingen

| Instelling          | Voorbeeldwaarde                                                    | Opmerkingen                                |
|---------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                | De URL van je Container App (basis-URI)   |
| **Token endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | Standaard Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | Standaard JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery document (automatisch gegenereerd) |
| **APIM audience**   | `mcp-client`                                                     | OAuth client ID of API resource naam       |
| **APIM policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` gebruikt deze URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Veelvoorkomende valkuilen

- **HTTPS/TLS:** De APIM gateway vereist dat het OpenID/JWKS-eindpunt HTTPS gebruikt met een geldig certificaat. Standaard levert Azure Container Apps een vertrouwd TLS-certificaat voor het Azure-beheerde domein ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Gebruik je een aangepast domein, zorg dan dat je een certificaat koppelt (je kunt Azure’s gratis beheerde certificaatfunctie gebruiken) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Als APIM het certificaat van het eindpunt niet vertrouwt, zal `<validate-jwt>` falen bij het ophalen van de metadata.

- **Toegankelijkheid van eindpunten:** Zorg dat de eindpunten van de Spring-app bereikbaar zijn vanuit APIM. Gebruik `--ingress external` (of schakel ingress in via het portal) voor de eenvoudigste toegang. Kies je voor een interne of vNet-gebonden omgeving, dan kan APIM (standaard publiek) deze mogelijk niet bereiken tenzij het in hetzelfde vNet zit. In een testomgeving verdient publieke ingress de voorkeur zodat APIM de `.well-known` en `/jwks` URL’s kan aanroepen.

- **OpenID Discovery ingeschakeld:** Standaard maakt Spring Authorization Server **niet** het `/.well-known/openid-configuration` eindpunt beschikbaar tenzij OIDC is ingeschakeld. Zorg dat je `.oidc(Customizer.withDefaults())` opneemt in je securityconfiguratie (zie hierboven) zodat het provider configuratie-eindpunt actief is ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Anders zal APIM’s `<openid-config>` oproep een 404 teruggeven.

- **Audience Claim:** Standaard zet Spring de `aud` claim op de client ID. Als APIM’s `<audience>` check faalt, moet je mogelijk het token aanpassen (zoals hierboven getoond) of de APIM policy bijstellen. Zorg dat de audience in je JWT overeenkomt met wat je in `<audience>` configureert.

- **JSON Metadata Parsing:** De OpenID configuratie JSON moet geldig zijn. De standaardconfiguratie van Spring genereert een standaard OIDC metadata document. Controleer dat het de juiste `issuer` en `jwks_uri` bevat. Host je Spring achter een proxy of via een pad-gebaseerde route, controleer dan de URLs in deze metadata goed. APIM gebruikt deze waarden zoals ze zijn.

- **Policy volgorde:** Plaats `<validate-jwt>` in de APIM policy **voor** elke routering naar de backend. Anders kunnen verzoeken je app bereiken zonder geldig token. Zorg er ook voor dat `<validate-jwt>` direct onder `<inbound>` staat (niet genest in een andere conditie) zodat APIM het toepast.

Door bovenstaande stappen te volgen, kun je je Spring AI MCP-server draaien in Azure Container Apps en Azure API Management OAuth2 JWT’s laten valideren met een minimale policy. De belangrijkste punten zijn: maak de Spring Auth-eindpunten publiek toegankelijk met TLS, schakel OIDC discovery in en richt APIM’s `validate-jwt` in op de OpenID configuratie URL (zodat het automatisch de JWKS kan ophalen). Deze setup is geschikt voor een dev/test omgeving; voor productie is het verstandig om goede geheimbeheer, tokenlevensduur en rotatie van sleutels in JWKS te overwegen.
**Referenties:** Zie de Spring Authorization Server documentatie voor standaard endpoints ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) en OIDC-configuratie ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); zie Microsoft APIM documentatie voor `validate-jwt` voorbeelden ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); en Azure Container Apps documentatie voor deployment en certificaten ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.