# Bereitstellung der Spring AI MCP App in Azure Container Apps

 ([Absicherung von Spring AI MCP-Servern mit OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Abbildung: Spring AI MCP-Server gesichert mit Spring Authorization Server. Der Server stellt Zugriffstoken für Clients aus und validiert diese bei eingehenden Anfragen (Quelle: Spring Blog) ([Absicherung von Spring AI MCP-Servern mit OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Um den Spring MCP-Server bereitzustellen, bauen Sie ihn als Container und verwenden Azure Container Apps mit externem Ingress. Zum Beispiel können Sie mit der Azure CLI folgenden Befehl ausführen:

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

Dies erstellt eine öffentlich zugängliche Container App mit aktiviertem HTTPS (Azure stellt ein kostenloses TLS-Zertifikat für die Standarddomain `*.azurecontainerapps.io` aus ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Die Ausgabe des Befehls enthält den FQDN der App (z. B. `my-mcp-app.eastus.azurecontainerapps.io`), der zur Basis-URL des **Issuer** wird. Stellen Sie sicher, dass HTTP-Ingress aktiviert ist (wie oben), damit APIM die App erreichen kann. In einer Test-/Entwicklungsumgebung verwenden Sie die Option `--ingress external` (oder binden eine benutzerdefinierte Domain mit TLS gemäß [Microsoft-Dokumentation](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Speichern Sie sensible Eigenschaften (wie OAuth-Client-Geheimnisse) in Container Apps Secrets oder Azure Key Vault und binden Sie diese als Umgebungsvariablen in den Container ein.

## Konfiguration des Spring Authorization Server

Binden Sie in Ihrem Spring Boot-Code die Starter für Spring Authorization Server und Resource Server ein. Konfigurieren Sie einen `RegisteredClient` (für das `client_credentials`-Grant in Dev/Test) und eine JWT-Schlüsselquelle. Zum Beispiel könnten Sie in `application.properties` folgendes setzen:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Aktivieren Sie den Authorization Server und Resource Server, indem Sie eine Security Filter Chain definieren. Zum Beispiel:

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

Diese Konfiguration stellt die Standard-OAuth2-Endpunkte bereit: `/oauth2/token` für Token und `/oauth2/jwks` für das JSON Web Key Set. (Standardmäßig mappt Spring’s `AuthorizationServerSettings` `/oauth2/token` und `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Der Server stellt JWT-Zugriffstoken aus, die mit dem oben definierten RSA-Schlüssel signiert sind, und veröffentlicht seinen öffentlichen Schlüssel unter `https://<your-app>:/oauth2/jwks`.

**OpenID Connect Discovery aktivieren:** Damit APIM automatisch den Issuer und JWKS abrufen kann, aktivieren Sie den OIDC-Provider-Konfigurationsendpunkt, indem Sie `.oidc(Customizer.withDefaults())` in Ihrer Sicherheitskonfiguration hinzufügen ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Zum Beispiel:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Dies stellt `/.well-known/openid-configuration` bereit, das APIM für Metadaten nutzen kann. Abschließend möchten Sie möglicherweise die JWT-**Audience**-Claim anpassen, damit die `<audiences>`-Prüfung von APIM erfolgreich ist. Zum Beispiel fügen Sie einen Token-Customizer hinzu:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

So tragen die Tokens `"aud": ["mcp-client"]`, was mit der Client-ID oder dem von APIM erwarteten Scope übereinstimmt.

## Bereitstellung der Token- und JWKS-Endpunkte

Nach der Bereitstellung ist die **Issuer-URL** Ihrer App `https://<app-fqdn>`, z. B. `https://my-mcp-app.eastus.azurecontainerapps.io`. Die OAuth2-Endpunkte lauten:

- **Token-Endpunkt:** `https://<app-fqdn>/oauth2/token` – hier erhalten Clients Tokens (client_credentials Flow).
- **JWKS-Endpunkt:** `https://<app-fqdn>/oauth2/jwks` – liefert das JWK-Set (wird von APIM zum Abruf der Signaturschlüssel verwendet).
- **OpenID-Konfiguration:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC-Discovery-JSON (enthält `issuer`, `token_endpoint`, `jwks_uri` usw.).

APIM verweist auf die **OpenID-Konfigurations-URL**, von der es die `jwks_uri` ermittelt. Wenn der FQDN Ihrer Container App z. B. `my-mcp-app.eastus.azurecontainerapps.io` ist, sollte APIMs `<openid-config url="...">` `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` verwenden. (Standardmäßig setzt Spring den `issuer` in diesen Metadaten auf dieselbe Basis-URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfiguration von Azure API Management (`validate-jwt`)

Fügen Sie in Azure APIM eine Inbound-Policy hinzu, die die `<validate-jwt>`-Policy verwendet, um eingehende JWTs gegen Ihren Spring Authorization Server zu prüfen. Für eine einfache Konfiguration können Sie die OpenID Connect-Metadaten-URL verwenden. Beispiel für einen Policy-Ausschnitt:

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

Diese Policy weist APIM an, die OpenID-Konfiguration vom Spring Auth Server abzurufen, dessen JWKS zu laden und zu prüfen, dass jedes Token mit einem vertrauenswürdigen Schlüssel signiert ist und die korrekte Audience enthält. (Wenn Sie `<issuers>` weglassen, verwendet APIM automatisch den `issuer`-Claim aus den Metadaten.) Die `<audience>` sollte mit Ihrer Client-ID oder dem API-Ressourcennamen im Token übereinstimmen (im obigen Beispiel haben wir `"mcp-client"` gesetzt). Dies entspricht der Microsoft-Dokumentation zur Verwendung von `validate-jwt` mit `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Nach der Validierung leitet APIM die Anfrage (inklusive des ursprünglichen `Authorization`-Headers) an das Backend weiter. Da die Spring-App ebenfalls ein Resource Server ist, validiert sie das Token erneut, aber APIM hat bereits dessen Gültigkeit sichergestellt. (Für die Entwicklung können Sie sich auf die Prüfung von APIM verlassen und zusätzliche Prüfungen in der App deaktivieren, aber es ist sicherer, beide Prüfungen beizubehalten.)

## Beispielhafte Einstellungen

| Einstellung         | Beispielwert                                                       | Hinweise                                   |
|---------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL Ihrer Container App (Basis-URI)        |
| **Token-Endpunkt**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Standard-Spring-Token-Endpunkt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS-Endpunkt**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Standard-JWK-Set-Endpunkt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC-Discovery-Dokument (automatisch generiert) |
| **APIM Audience**   | `mcp-client`                                                      | OAuth-Client-ID oder API-Ressourcenname    |
| **APIM Policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` verwendet diese URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Häufige Stolperfallen

- **HTTPS/TLS:** Das APIM-Gateway verlangt, dass der OpenID/JWKS-Endpunkt HTTPS mit einem gültigen Zertifikat verwendet. Standardmäßig stellt Azure Container Apps ein vertrauenswürdiges TLS-Zertifikat für die Azure-verwaltete Domain bereit ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Wenn Sie eine benutzerdefinierte Domain verwenden, binden Sie unbedingt ein Zertifikat (Sie können das kostenlose verwaltete Zertifikat von Azure nutzen) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Wenn APIM dem Zertifikat des Endpunkts nicht vertraut, schlägt `<validate-jwt>` beim Abruf der Metadaten fehl.

- **Erreichbarkeit der Endpunkte:** Stellen Sie sicher, dass die Endpunkte der Spring-App von APIM erreichbar sind. Die Verwendung von `--ingress external` (oder das Aktivieren des Ingress im Portal) ist am einfachsten. Wenn Sie eine interne oder vNet-gebundene Umgebung gewählt haben, kann APIM (standardmäßig öffentlich) diese möglicherweise nicht erreichen, es sei denn, es befindet sich im selben VNet. In einer Testumgebung empfiehlt sich öffentlicher Ingress, damit APIM die `.well-known`- und `/jwks`-URLs aufrufen kann.

- **OpenID Discovery aktiviert:** Standardmäßig stellt Spring Authorization Server **nicht** `/.well-known/openid-configuration` bereit, wenn OIDC nicht aktiviert ist. Stellen Sie sicher, dass Sie `.oidc(Customizer.withDefaults())` in Ihrer Sicherheitskonfiguration einbinden (siehe oben), damit der Provider-Konfigurationsendpunkt aktiv ist ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Andernfalls führt der `<openid-config>`-Aufruf von APIM zu einem 404.

- **Audience-Claim:** Spring setzt standardmäßig den `aud`-Claim auf die Client-ID. Wenn die `<audience>`-Prüfung von APIM fehlschlägt, müssen Sie möglicherweise das Token anpassen (wie oben gezeigt) oder die APIM-Policy anpassen. Stellen Sie sicher, dass die Audience im JWT mit der in `<audience>` konfigurierten übereinstimmt.

- **JSON-Metadaten-Parsing:** Das OpenID-Konfigurations-JSON muss gültig sein. Die Standardkonfiguration von Spring liefert ein standardmäßiges OIDC-Metadaten-Dokument. Prüfen Sie, ob es den korrekten `issuer` und `jwks_uri` enthält. Wenn Sie Spring hinter einem Proxy oder mit pfadbasierter Weiterleitung betreiben, überprüfen Sie die URLs in diesen Metadaten sorgfältig. APIM verwendet diese Werte unverändert.

- **Reihenfolge der Policy:** Platzieren Sie `<validate-jwt>` in der APIM-Policy **vor** jeglichem Routing zum Backend. Andernfalls könnten Anfragen ohne gültiges Token Ihre App erreichen. Stellen Sie außerdem sicher, dass `<validate-jwt>` direkt unter `<inbound>` steht (nicht verschachtelt in einer anderen Bedingung), damit APIM die Prüfung anwendet.

Wenn Sie die oben genannten Schritte befolgen, können Sie Ihren Spring AI MCP-Server in Azure Container Apps betreiben und Azure API Management so konfigurieren, dass eingehende OAuth2-JWTs mit einer minimalen Policy validiert werden. Die wichtigsten Punkte sind: Stellen Sie die Spring Auth-Endpunkte öffentlich mit TLS bereit, aktivieren Sie die OIDC-Discovery und verweisen Sie APIMs `validate-jwt` auf die OpenID-Konfigurations-URL (damit es die JWKS automatisch abrufen kann). Diese Konfiguration eignet sich für Entwicklungs- und Testumgebungen; für den produktiven Einsatz sollten Sie eine ordnungsgemäße Geheimnisverwaltung, Token-Lebensdauern und das Rotieren von Schlüsseln im JWKS berücksichtigen.
**Referenzen:** Siehe die Spring Authorization Server-Dokumentation für Standardendpunkte ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) und OIDC-Konfiguration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); siehe Microsoft APIM-Dokumentation für `validate-jwt`-Beispiele ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); und Azure Container Apps-Dokumentation für Bereitstellung und Zertifikate ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.