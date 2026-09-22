# Bereitstellung der Spring AI MCP-App in Azure Container Apps

> [!WARNING]
> Dieser kombinierte Autorisierungs-/Ressourcenserver ist für Lern- und
> Entwicklungs-/Testzwecke gedacht. Produktionssysteme sollten einen dedizierten Identitätsanbieter,
> persistente Signaturschlüssel und in einem verwalteten Geheimnisspeicher gespeicherte Anmeldeinformationen verwenden.

 ([Spring AI MCP-Server mit OAuth2 absichern](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Abbildung: Spring AI MCP-Server gesichert mit Spring Authorization Server. Der Server stellt Zugriffstoken für Clients aus und validiert diese bei eingehenden Anfragen (Quelle: Spring-Blog) ([Spring AI MCP-Server mit OAuth2 absichern](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Zur Bereitstellung des Spring MCP-Servers bauen Sie ihn als Container und verwenden Azure Container Apps mit externem Ingress. Zum Beispiel können Sie mit der Azure CLI ausführen:

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

Dies erstellt eine öffentlich zugängliche Container App mit aktiviertem HTTPS (Azure stellt ein kostenloses TLS-Zertifikat für die Standarddomain `*.azurecontainerapps.io` aus ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Die Befehlsausgabe enthält den FQDN der App (z. B. `my-mcp-app.eastus.azurecontainerapps.io`), der zur **Issuer-URL**-Basis wird. Stellen Sie sicher, dass HTTP-Ingress aktiviert ist (wie oben), damit APIM die App erreichen kann. In einer Test-/Entwicklungsumgebung verwenden Sie die Option `--ingress external` (oder binden eine benutzerdefinierte Domain mit TLS entsprechend den [Microsoft-Dokumenten](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Speichern Sie alle sensiblen Eigenschaften (wie OAuth-Clientgeheimnisse) in Container Apps-Geheimnissen oder Azure Key Vault und binden Sie sie als Umgebungsvariablen im Container ein.

## Konfiguration des Spring Authorization Servers

Binden Sie in Ihrem Spring Boot-App-Code die Spring Authorization Server- und Resource Server-Starter ein. Konfigurieren Sie einen `RegisteredClient` (für das `client_credentials`-Grant in Entwicklung/Test) und eine JWT-Schlüsselquelle. Zum Beispiel könnten Sie in `application.properties` Folgendes setzen:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Aktivieren Sie den Authorization Server und Resource Server, indem Sie eine Security-Filterkette definieren. Zum Beispiel:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Aktivieren Sie die Endpunkte des Autorisierungsservers
            .apply(authzServer.and())
            // Aktivieren Sie den Resource Server (validieren Sie JWT bei eingehenden Anfragen)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Deaktivieren Sie CSRF (MCP-Server ist nicht browserbasiert)
            .csrf(csrf -> csrf.disable())
            // Erlauben Sie CORS für Client-Demotools
            .cors(withDefaults());
        return http.build();
    }

    // Definieren Sie einen In-Memory-Client (RegisteredClient) und eine JWK-Quelle:
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
        // Generieren Sie einen RSA-Schlüssel (für Entwicklung/Test, bei jedem Start neu generieren)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Diese Konfiguration stellt die Standard-OAuth2-Endpunkte bereit: `/oauth2/token` für Token und `/oauth2/jwks` für das JSON Web Key Set. (Standardmäßig mappt Spring’s `AuthorizationServerSettings` `/oauth2/token` und `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Der Server gibt JWT-Zugriffstoken aus, die mit dem RSA-Schlüssel oben signiert sind, und veröffentlicht seinen öffentlichen Schlüssel unter `https://<your-app>:/oauth2/jwks`.

**OpenID Connect Discovery aktivieren:** Damit APIM automatisch den Issuer und JWKS abruft, aktivieren Sie den OIDC-Provider-Konfigurationsendpunkt, indem Sie `.oidc(Customizer.withDefaults())` in Ihrer Sicherheitskonfiguration hinzufügen ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Zum Beispiel:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– aktiviert /.well-known/openid-configuration
```

Dies stellt `/.well-known/openid-configuration` bereit, welches APIM für Metadaten verwenden kann. Schließlich möchten Sie vielleicht die JWT-**Audience**-Anspruch anpassen, damit die `<audiences>`-Prüfung von APIM besteht. Zum Beispiel fügen Sie einen Token-Customizer hinzu:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Legen Sie eine benutzerdefinierte Zielgruppe fest (z. B. die Kunden-ID oder API-Kennung)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Dies stellt sicher, dass Token `"aud": ["mcp-client"]` enthalten, was der erwarteten Client-ID oder dem Scope von APIM entspricht.

## Exponieren der Token- und JWKS-Endpunkte

Nach der Bereitstellung wird die **Issuer-URL** Ihrer App `https://<app-fqdn>` sein, z. B. `https://my-mcp-app.eastus.azurecontainerapps.io`. Ihre OAuth2-Endpunkte sind:

- **Token-Endpunkt:** `https://<app-fqdn>/oauth2/token` – Clients erhalten hier Token (client_credentials-Flow).
- **JWKS-Endpunkt:** `https://<app-fqdn>/oauth2/jwks` – gibt das JWK-Set zurück (wird von APIM verwendet, um Signaturschlüssel abzurufen).
- **OpenID-Konfig:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC-Discovery-JSON (enthält `issuer`, `token_endpoint`, `jwks_uri` usw.).

APIM wird auf die **OpenID-Konfigurations-URL** zeigen, von der es die `jwks_uri` entdeckt. Wenn zum Beispiel Ihr Container App-FQDN `my-mcp-app.eastus.azurecontainerapps.io` ist, sollte APIMs `<openid-config url="...">` `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` verwenden. (Standardmäßig setzt Spring im Metadaten die `issuer`-Angabe auf dieselbe Basis-URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Konfiguration von Azure API Management (`validate-jwt`)

Fügen Sie in Azure APIM eine Eingangsrichtlinie hinzu, die die `<validate-jwt>`-Richtlinie verwendet, um eingehende JWTs gegen Ihren Spring Authorization Server zu überprüfen. Für eine einfache Einrichtung können Sie die OpenID Connect-Metadaten-URL verwenden. Beispiel eines Richtlinienausschnitts:

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

Diese Richtlinie weist APIM an, die OpenID-Konfiguration vom Spring Auth Server abzurufen, dessen JWKS zu erhalten und zu validieren, dass jedes Token von einem vertrauenswürdigen Schlüssel signiert ist und die richtige Audience hat. (Wenn Sie `<issuers>` weglassen, verwendet APIM automatisch den `issuer`-Anspruch aus den Metadaten.) Die `<audience>` sollte mit Ihrer Client-ID oder dem API-Ressourcennamen im Token übereinstimmen (im obigen Beispiel setzen wir sie auf `"mcp-client"`). Dies entspricht der Microsoft-Dokumentation zur Verwendung von `validate-jwt` mit `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Nach der Validierung leitet APIM die Anforderung (einschließlich des ursprünglichen `Authorization`-Headers) an das Backend weiter. Da die Spring-App auch ein Ressourcenserver ist, validiert sie das Token erneut, aber APIM hat bereits die Gültigkeit bestätigt. (Für die Entwicklung können Sie sich auf die APIM-Prüfung verlassen und zusätzliche Prüfungen in der App bei Bedarf deaktivieren, aber es ist sicherer, beide beizubehalten.)

## Beispiel-Einstellungen

| Einstellung          | Beispielwert                                                      | Anmerkungen                               |
|--------------------|-----------------------------------------------------------------|------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`               | Ihre Container-App-URL (Basis-URI)       |
| **Token-Endpunkt**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`  | Standard-Spring-Token-Endpunkt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **JWKS-Endpunkt**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`   | Standard-JWK-Set-Endpunkt ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))   |
| **OpenID-Konfig**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC-Discovery-Dokument (automatisch generiert) |
| **APIM-Audience**   | `mcp-client`                                                    | OAuth-Client-ID oder API-Ressourcenname  |
| **APIM-Richtlinie** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` verwendet diese URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Häufige Stolperfallen

- **HTTPS/TLS:** Das APIM-Gateway erfordert, dass der OpenID-/JWKS-Endpunkt HTTPS mit einem gültigen Zertifikat verwendet. Standardmäßig stellt Azure Container Apps ein vertrauenswürdiges TLS-Zertifikat für die Azure-verwaltete Domain bereit ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Wenn Sie eine benutzerdefinierte Domain verwenden, binden Sie unbedingt ein Zertifikat (Sie können das kostenfreie verwaltete Zertifikat von Azure verwenden) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Wenn APIM dem Zertifikat des Endpunkts nicht vertraut, schlägt das Abrufen der Metadaten mit `<validate-jwt>` fehl.  

- **Endpunktzugänglichkeit:** Stellen Sie sicher, dass die Spring-App-Endpunkte von APIM erreichbar sind. Die Verwendung von `--ingress external` (oder das Aktivieren des Ingress im Portal) ist am einfachsten. Wenn Sie eine interne oder vNet-gebundene Umgebung gewählt haben, könnte APIM (standardmäßig öffentlich) sie nicht erreichen, es sei denn, es befindet sich im selben vNet. In einer Testumgebung ist öffentlicher Ingress vorzuziehen, damit APIM die `.well-known`- und `/jwks`-URLs aufrufen kann.

- **OpenID Discovery aktiviert:** Standardmäßig **stellt Spring Authorization Server nicht bereit** `/.well-known/openid-configuration`, es sei denn, OIDC ist aktiviert. Stellen Sie sicher, dass Sie `.oidc(Customizer.withDefaults())` in Ihrer Sicherheitskonfiguration einschließen (siehe oben), damit der Provider-Konfigurationsendpunkt aktiv ist ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Andernfalls führt der `<openid-config>`-Aufruf von APIM zu einem 404-Fehler.

- **Audience-Prüfung:** Standardverhalten von Spring ist, die `aud`-Angabe auf die Client-ID zu setzen. Wenn die `<audience>`-Prüfung von APIM fehlschlägt, müssen Sie möglicherweise das Token anpassen (wie oben gezeigt) oder die APIM-Richtlinie ändern. Stellen Sie sicher, dass die Audience im JWT mit der in `<audience>` konfigurierten übereinstimmt.

- **JSON-Metadaten-Parsing:** Das OpenID-Konfigurations-JSON muss gültig sein. Die Standardkonfiguration von Spring gibt ein standardmäßiges OIDC-Metadatendokument aus. Vergewissern Sie sich, dass es die korrekten `issuer`- und `jwks_uri`-Werte enthält. Wenn Sie Spring hinter einem Proxy oder einer pfadbasierten Route hosten, prüfen Sie die URLs in diesen Metadaten sorgfältig. APIM verwendet diese Werte unverändert.

- **Reihenfolge der Richtlinien:** Platzieren Sie `<validate-jwt>` in der APIM-Richtlinie **vor** jeglicher Weiterleitung an das Backend. Andernfalls könnten Aufrufe Ihre App ohne gültiges Token erreichen. Stellen Sie außerdem sicher, dass `<validate-jwt>` direkt unter `<inbound>` steht (nicht verschachtelt in einer anderen Bedingung), damit APIM es anwendet.

Indem Sie die obigen Schritte befolgen, können Sie Ihren Spring AI MCP-Server in Azure Container Apps betreiben und Azure API Management mit einer minimalen Richtlinie eingehende OAuth2-JWTs validieren lassen. Die wichtigsten Punkte sind: exponieren Sie die Spring-Auth-Endpunkte öffentlich mit TLS, aktivieren Sie die OIDC-Discovery und richten Sie APIMs `validate-jwt` auf die OpenID-Konfigurations-URL, damit es die JWKS automatisch abrufen kann. Diese Einrichtung ist für eine Entwicklungs-/Testumgebung geeignet; für Produktion sollten Sie eine ordnungsgemäße Geheimnisverwaltung, Token-Lebensdauern und Schlüsselrotation in JWKS berücksichtigen.


**Verweise:** Siehe Spring Authorization Server-Dokumentation für Standardendpunkte ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) und OIDC-Konfiguration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); siehe Microsoft APIM-Dokumentation für Beispiele zu `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); und Azure Container Apps-Dokumentation für Bereitstellung und Zertifikate ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->