<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "32c9a4263be08f9050c8044bb26267c4",
  "translation_date": "2025-12-11T16:20:06+00:00",
  "source_file": "05-AdvancedTopics/mcp-oauth2-demo/apimoauth.md",
  "language_code": "kn"
}
-->
# Spring AI MCP ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು Azure Container Apps ಗೆ ನಿಯೋಜಿಸುವುದು

 ([OAuth2 ಮೂಲಕ Spring AI MCP ಸರ್ವರ್‌ಗಳನ್ನು ಸುರಕ್ಷಿತಗೊಳಿಸುವುದು](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *ಚಿತ್ರ: Spring Authorization Server ಮೂಲಕ ಸುರಕ್ಷಿತಗೊಳಿಸಲಾದ Spring AI MCP ಸರ್ವರ್. ಸರ್ವರ್ ಕ್ಲೈಂಟ್‌ಗಳಿಗೆ ಪ್ರವೇಶ ಟೋಕನ್‌ಗಳನ್ನು ನೀಡುತ್ತದೆ ಮತ್ತು ಇನ್‌ಕಮಿಂಗ್ ವಿನಂತಿಗಳಲ್ಲಿ ಅವುಗಳನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ (ಮೂಲ: Spring ಬ್ಲಾಗ್) ([OAuth2 ಮೂಲಕ Spring AI MCP ಸರ್ವರ್‌ಗಳನ್ನು ಸುರಕ್ಷಿತಗೊಳಿಸುವುದು](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP ಸರ್ವರ್ ಅನ್ನು ನಿಯೋಜಿಸಲು, ಅದನ್ನು ಕಂಟೇನರ್ ಆಗಿ ನಿರ್ಮಿಸಿ ಮತ್ತು ಹೊರಗಿನ ಇನ್‌ಗ್ರೆಸ್ ಹೊಂದಿರುವ Azure Container Apps ಅನ್ನು ಬಳಸಿ. ಉದಾಹರಣೆಗೆ, Azure CLI ಬಳಸಿ ನೀವು ಈ ಕೆಳಗಿನಂತೆ ಚಾಲನೆ ಮಾಡಬಹುದು:

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

ಇದು HTTPS ಸಕ್ರಿಯಗೊಂಡ ಸಾರ್ವಜನಿಕವಾಗಿ ಪ್ರವೇಶಿಸಬಹುದಾದ Container App ಅನ್ನು ರಚಿಸುತ್ತದೆ (Azure ಡೀಫಾಲ್ಟ್ `*.azurecontainerapps.io` ಡೊಮೇನ್‌ಗೆ ಉಚಿತ TLS ಪ್ರಮಾಣಪತ್ರವನ್ನು ನೀಡುತ್ತದೆ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ಆಜ್ಞೆಯ ಔಟ್‌ಪುಟ್‌ನಲ್ಲಿ ಅಪ್ಲಿಕೇಶನ್‌ನ FQDN (ಉದಾ. `my-mcp-app.eastus.azurecontainerapps.io`) ಸೇರಿದೆ, ಇದು **issuer URL** ಆಧಾರವಾಗುತ್ತದೆ. APIM ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ತಲುಪಲು HTTP ಇನ್‌ಗ್ರೆಸ್ ಸಕ್ರಿಯವಾಗಿರಬೇಕು (ಮೇಲಿನಂತೆ). ಪರೀಕ್ಷಾ/ವಿಕಸನ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ, `--ingress external` ಆಯ್ಕೆಯನ್ನು ಬಳಸಿ (ಅಥವಾ [Microsoft ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳು](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ಪ್ರಕಾರ TLS ಹೊಂದಿರುವ ಕಸ್ಟಮ್ ಡೊಮೇನ್ ಅನ್ನು ಬಾಂಡ್ ಮಾಡಿ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ಯಾವುದೇ ಸಂವೇದನಾಶೀಲ ಗುಣಲಕ್ಷಣಗಳನ್ನು (OAuth ಕ್ಲೈಂಟ್ ರಹಸ್ಯಗಳು ಮುಂತಾದವು) Container Apps ರಹಸ್ಯಗಳಲ್ಲಿ ಅಥವಾ Azure Key Vault ನಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ, ಅವುಗಳನ್ನು ಪರಿಸರ ಚರಗಳಾಗಿ ಕಂಟೇನರ್‌ಗೆ ನಕ್ಷೆಮಾಡಿ.

## Spring Authorization Server ಅನ್ನು ಸಂರಚಿಸುವುದು

ನಿಮ್ಮ Spring Boot ಅಪ್ಲಿಕೇಶನ್ ಕೋಡ್‌ನಲ್ಲಿ Spring Authorization Server ಮತ್ತು Resource Server ಸ್ಟಾರ್ಟರ್‌ಗಳನ್ನು ಸೇರಿಸಿ. `RegisteredClient` ಅನ್ನು (dev/test ನಲ್ಲಿ `client_credentials` ಗ್ರಾಂಟ್‌ಗಾಗಿ) ಮತ್ತು JWT ಕೀ ಮೂಲವನ್ನು ಸಂರಚಿಸಿ. ಉದಾಹರಣೆಗೆ, `application.properties` ನಲ್ಲಿ ನೀವು ಈ ಕೆಳಗಿನಂತೆ ಹೊಂದಿಸಬಹುದು:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server ಮತ್ತು Resource Server ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಲು ಸೆಕ್ಯುರಿಟಿ ಫಿಲ್ಟರ್ ಚೈನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ. ಉದಾಹರಣೆಗೆ:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // ಪ್ರಾಧಿಕಾರ ಸರ್ವರ್ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ
            .apply(authzServer.and())
            // ಸಂಪನ್ಮೂಲ ಸರ್ವರ್ ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ (ಬರುವ ವಿನಂತಿಗಳ ಮೇಲೆ JWT ಪರಿಶೀಲಿಸಿ)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಿ (MCP ಸರ್ವರ್ ಬ್ರೌಸರ್ ಆಧಾರಿತವಲ್ಲ)
            .csrf(csrf -> csrf.disable())
            // ಕ್ಲೈಂಟ್ ಡೆಮೊ ಉಪಕರಣಗಳಿಗೆ CORS ಅನುಮತಿಸಿ
            .cors(withDefaults());
        return http.build();
    }

    // ಒಂದು ಇನ್-ಮೆಮೊರಿ ಕ್ಲೈಂಟ್ (RegisteredClient) ಮತ್ತು JWK ಮೂಲವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ:
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
        // RSA ಕೀ ಅನ್ನು ರಚಿಸಿ (ಡೆವ್/ಟೆಸ್ಟ್ ಗಾಗಿ, ಪ್ರಾರಂಭದಲ್ಲಿ ಹೊಸದಾಗಿ ರಚಿಸಿ)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ಈ ವ್ಯವಸ್ಥೆ ಡೀಫಾಲ್ಟ್ OAuth2 ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸುತ್ತದೆ: ಟೋಕನ್‌ಗಳಿಗೆ `/oauth2/token` ಮತ್ತು JSON ವೆಬ್ ಕೀ ಸೆಟ್‌ಗೆ `/oauth2/jwks`. (ಡೀಫಾಲ್ಟ್ ಆಗಿ Spring ನ `AuthorizationServerSettings` `/oauth2/token` ಮತ್ತು `/oauth2/jwks` ನಕ್ಷೆಮಾಡುತ್ತದೆ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) ಸರ್ವರ್ ಮೇಲಿನ RSA ಕೀ ಮೂಲಕ ಸಹಿ ಮಾಡಲಾದ JWT ಪ್ರವೇಶ ಟೋಕನ್‌ಗಳನ್ನು ನೀಡುತ್ತದೆ ಮತ್ತು ತನ್ನ ಸಾರ್ವಜನಿಕ ಕೀ ಅನ್ನು `https://<your-app>:/oauth2/jwks` ನಲ್ಲಿ ಪ್ರಕಟಿಸುತ್ತದೆ.

**OpenID Connect ಅನ್ವೇಷಣೆಯನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ:** APIM ಸ್ವಯಂಚಾಲಿತವಾಗಿ issuer ಮತ್ತು JWKS ಅನ್ನು ಪಡೆಯಲು, ನಿಮ್ಮ ಸೆಕ್ಯುರಿಟಿ ಸಂರಚನೆಯಲ್ಲಿ `.oidc(Customizer.withDefaults())` ಅನ್ನು ಸೇರಿಸಿ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ಉದಾಹರಣೆಗೆ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸುತ್ತದೆ
```

ಇದು `/.well-known/openid-configuration` ಅನ್ನು ಬಹಿರಂಗಪಡಿಸುತ್ತದೆ, ಇದನ್ನು APIM ಮೆಟಾಡೇಟಾ ಪಡೆಯಲು ಬಳಸಬಹುದು. ಕೊನೆಗೆ, APIM ನ `<audiences>` ಪರಿಶೀಲನೆ ಪಾಸಾಗಲು JWT **audience** ಕ್ಲೇಮ್ ಅನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಬಹುದು. ಉದಾಹರಣೆಗೆ, ಟೋಕನ್ ಕಸ್ಟಮೈಜರ್ ಸೇರಿಸಿ:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // ಕಸ್ಟಮ್ ಪ್ರೇಕ್ಷಕರನ್ನು ಹೊಂದಿಸಿ (ಉದಾ. ಕ್ಲೈಂಟ್ ID ಅಥವಾ API ಗುರುತು)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

ಇದು ಟೋಕನ್‌ಗಳಲ್ಲಿ `"aud": ["mcp-client"]` ಇರಿಸುವುದನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ, ಇದು APIM ನಿರೀಕ್ಷಿಸುವ ಕ್ಲೈಂಟ್ ID ಅಥವಾ ಸ್ಕೋಪ್‌ಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ.

## ಟೋಕನ್ ಮತ್ತು JWKS ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸುವುದು

ನಿಯೋಜನೆಯ ನಂತರ, ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ನ **issuer URL** `https://<app-fqdn>` ಆಗಿರುತ್ತದೆ, ಉದಾ. `https://my-mcp-app.eastus.azurecontainerapps.io`. ಅದರ OAuth2 ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳು:

- **ಟೋಕನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್:** `https://<app-fqdn>/oauth2/token` – ಇಲ್ಲಿ ಕ್ಲೈಂಟ್‌ಗಳು ಟೋಕನ್‌ಗಳನ್ನು ಪಡೆಯುತ್ತಾರೆ (`client_credentials` ಫ್ಲೋ).
- **JWKS ಎಂಡ್‌ಪಾಯಿಂಟ್:** `https://<app-fqdn>/oauth2/jwks` – JWK ಸೆಟ್ ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ (APIM ಸಹಿ ಕೀಗಳನ್ನು ಪಡೆಯಲು ಬಳಸುತ್ತದೆ).
- **OpenID ಸಂರಚನೆ:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC ಅನ್ವೇಷಣಾ JSON (ಇದರಲ್ಲಿ `issuer`, `token_endpoint`, `jwks_uri` ಇತ್ಯಾದಿ ಇರುತ್ತವೆ).

APIM **OpenID ಸಂರಚನಾ URL** ಅನ್ನು ಸೂಚಿಸುತ್ತದೆ, ಇದರಿಂದ ಅದು `jwks_uri` ಅನ್ನು ಕಂಡುಹಿಡಿಯುತ್ತದೆ. ಉದಾಹರಣೆಗೆ, ನಿಮ್ಮ Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` ಆಗಿದ್ದರೆ, APIM ನ `<openid-config url="...">` ನಲ್ಲಿ `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` ಬಳಸಬೇಕು. (ಡೀಫಾಲ್ಟ್ ಆಗಿ Spring ಆ ಮೆಟಾಡೇಟಾದಲ್ಲಿ `issuer` ಅನ್ನು ಅದೇ ಮೂಲ URL ಗೆ ಹೊಂದಿಸುತ್ತದೆ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) ಅನ್ನು ಸಂರಚಿಸುವುದು

Azure APIM ನಲ್ಲಿ, `<validate-jwt>` ನೀತಿಯನ್ನು ಬಳಸಿ ಇನ್‌ಬೌಂಡ್ ಪಾಲಿಸಿ ಸೇರಿಸಿ, ಇದು ನಿಮ್ಮ Spring Authorization Server ವಿರುದ್ಧ JWTಗಳನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ. ಸರಳ ವ್ಯವಸ್ಥೆಗೆ, OpenID Connect ಮೆಟಾಡೇಟಾ URL ಅನ್ನು ಬಳಸಬಹುದು. ಉದಾಹರಣೆಯ ನೀತಿ ತುಣುಕು:

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

ಈ ನೀತಿ APIM ಗೆ Spring Auth Server ನಿಂದ OpenID ಸಂರಚನೆಯನ್ನು ಪಡೆಯಲು, ಅದರ JWKS ಅನ್ನು ಪಡೆಯಲು ಮತ್ತು ಪ್ರತಿಯೊಂದು ಟೋಕನ್ ಅನ್ನು ವಿಶ್ವಾಸಾರ್ಹ ಕೀ ಮೂಲಕ ಸಹಿ ಮಾಡಲಾಗಿದೆ ಮತ್ತು ಸರಿಯಾದ audience ಹೊಂದಿದೆ ಎಂದು ಪರಿಶೀಲಿಸಲು ಹೇಳುತ್ತದೆ. (`<issuers>` ಅನ್ನು ಹೊರತುಪಡಿಸಿದರೆ, APIM ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಮೆಟಾಡೇಟಾದ issuer ಕ್ಲೇಮ್ ಅನ್ನು ಬಳಸುತ್ತದೆ.) `<audience>` ಟೋಕನ್‌ನಲ್ಲಿನ ನಿಮ್ಮ ಕ್ಲೈಂಟ್ ID ಅಥವಾ API ಸಂಪನ್ಮೂಲ ಗುರುತಿನೊಂದಿಗೆ ಹೊಂದಿಕೆಯಾಗಬೇಕು (ಮೇಲಿನ ಉದಾಹರಣೆಯಲ್ಲಿ `"mcp-client"` ಆಗಿದೆ). ಇದು Microsoft ನ `validate-jwt` ಮತ್ತು `<openid-config>` ಬಳಕೆಯ ಡಾಕ್ಯುಮೆಂಟೇಶನ್‌ಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

ಪರಿಶೀಲನೆಯ ನಂತರ, APIM ವಿನಂತಿಯನ್ನು (ಮೂಲ `Authorization` ಹೆಡರ್ ಸೇರಿದಂತೆ) ಬ್ಯಾಕೆಂಡ್‌ಗೆ ಫಾರ್ವರ್ಡ್ ಮಾಡುತ್ತದೆ. Spring ಅಪ್ಲಿಕೇಶನ್ ಕೂಡ ರಿಸೋರ್ಸ್ ಸರ್ವರ್ ಆಗಿರುವುದರಿಂದ ಟೋಕನ್ ಅನ್ನು ಮರುಪರಿಶೀಲಿಸುತ್ತದೆ, ಆದರೆ APIM ಈಗಾಗಲೇ ಅದರ ಮಾನ್ಯತೆಯನ್ನು ಖಚಿತಪಡಿಸಿದೆ. (ವಿಕಸನಕ್ಕಾಗಿ, ನೀವು APIM ಪರಿಶೀಲನೆ ಮೇಲೆ ಅವಲಂಬಿಸಿ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಹೆಚ್ಚುವರಿ ಪರಿಶೀಲನೆಗಳನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಬಹುದು, ಆದರೆ ಎರಡನ್ನೂ ಇಡುವುದು ಸುರಕ್ಷಿತ.)

## ಉದಾಹರಣೆಯ ಸೆಟ್ಟಿಂಗ್‌ಗಳು

| ಸೆಟ್ಟಿಂಗ್            | ಉದಾಹರಣೆಯ ಮೌಲ್ಯ                                                        | ಟಿಪ್ಪಣಿಗಳು                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | ನಿಮ್ಮ Container App URL (ಮೂಲ URI)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | ಡೀಫಾಲ್ಟ್ Spring ಟೋಕನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | ಡೀಫಾಲ್ಟ್ JWK ಸೆಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC ಅನ್ವೇಷಣಾ ಡಾಕ್ಯುಮೆಂಟ್ (ಸ್ವಯಂ-ಉತ್ಪಾದಿತ)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth ಕ್ಲೈಂಟ್ ID ಅಥವಾ API ಸಂಪನ್ಮೂಲ ಹೆಸರು       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ಈ URL ಅನ್ನು ಬಳಸುತ್ತದೆ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## ಸಾಮಾನ್ಯ ತಪ್ಪುಗಳು

- **HTTPS/TLS:** APIM ಗೇಟ್ವೇಗೆ OpenID/JWKS ಎಂಡ್‌ಪಾಯಿಂಟ್ HTTPS ಮತ್ತು ಮಾನ್ಯ ಪ್ರಮಾಣಪತ್ರ ಹೊಂದಿರಬೇಕು. ಡೀಫಾಲ್ಟ್ ಆಗಿ, Azure Container Apps Azure ನಿರ್ವಹಿತ ಡೊಮೇನ್‌ಗೆ ವಿಶ್ವಾಸಾರ್ಹ TLS ಪ್ರಮಾಣಪತ್ರವನ್ನು ಒದಗಿಸುತ್ತದೆ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). ನೀವು ಕಸ್ಟಮ್ ಡೊಮೇನ್ ಬಳಸಿದರೆ, ಪ್ರಮಾಣಪತ್ರವನ್ನು ಬಾಂಡ್ ಮಾಡಬೇಕು (ನೀವು Azure ಉಚಿತ ನಿರ್ವಹಿತ ಪ್ರಮಾಣಪತ್ರ ವೈಶಿಷ್ಟ್ಯವನ್ನು ಬಳಸಬಹುದು) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM ಪ್ರಮಾಣಪತ್ರವನ್ನು ವಿಶ್ವಾಸಾರ್ಹವೆಂದು ಪರಿಗಣಿಸದಿದ್ದರೆ, `<validate-jwt>` ಮೆಟಾಡೇಟಾ ಪಡೆಯಲು ವಿಫಲವಾಗುತ್ತದೆ.

- **ಎಂಡ್‌ಪಾಯಿಂಟ್ ಪ್ರವೇಶ:** Spring ಅಪ್ಲಿಕೇಶನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳು APIM ನಿಂದ ತಲುಪಬಹುದಾಗಿರಬೇಕು. `--ingress external` (ಅಥವಾ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಇನ್‌ಗ್ರೆಸ್ ಸಕ್ರಿಯಗೊಳಿಸುವುದು) ಸರಳವಾಗಿದೆ. ನೀವು ಆಂತರಿಕ ಅಥವಾ vNet-ಬಂಧಿತ ಪರಿಸರವನ್ನು ಆಯ್ಕೆಮಾಡಿದರೆ, APIM (ಡೀಫಾಲ್ಟ್ ಸಾರ್ವಜನಿಕ) ಅದನ್ನು ತಲುಪಲು ಸಾಧ್ಯವಿಲ್ಲ, ಅದನ್ನು ಅದೇ VNet ನಲ್ಲಿ ಇರಿಸಬೇಕು. ಪರೀಕ್ಷಾ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ, ಸಾರ್ವಜನಿಕ ಇನ್‌ಗ್ರೆಸ್ ಅನ್ನು ಆದ್ಯತೆ ನೀಡಿ, APIM `.well-known` ಮತ್ತು `/jwks` URL ಗಳನ್ನು ಕರೆ ಮಾಡಬಹುದು.

- **OpenID ಅನ್ವೇಷಣೆ ಸಕ್ರಿಯ:** ಡೀಫಾಲ್ಟ್ ಆಗಿ, Spring Authorization Server `/.well-known/openid-configuration` ಅನ್ನು ಬಹಿರಂಗಪಡಿಸುವುದಿಲ್ಲ, OIDC ಸಕ್ರಿಯಗೊಳಿಸದಿದ್ದರೆ. `.oidc(Customizer.withDefaults())` ಅನ್ನು ನಿಮ್ಮ ಸೆಕ್ಯುರಿಟಿ ಸಂರಚನೆಯಲ್ಲಿ ಸೇರಿಸಿ (ಮೇಲಿನಂತೆ) ताकि ಪ್ರೊವೈಡರ್ ಸಂರಚನಾ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಸಕ್ರಿಯವಾಗಿರುತ್ತದೆ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ಇಲ್ಲದಿದ್ದರೆ APIM ನ `<openid-config>` ಕರೆ 404 ಆಗುತ್ತದೆ.

- **Audience ಕ್ಲೇಮ್:** Spring ಡೀಫಾಲ್ಟ್ ವರ್ತನೆ `aud` ಕ್ಲೇಮ್ ಅನ್ನು ಕ್ಲೈಂಟ್ ID ಗೆ ಹೊಂದಿಸುವುದು. APIM ನ `<audience>` ಪರಿಶೀಲನೆ ವಿಫಲವಾದರೆ, ಟೋಕನ್ ಅನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಬೇಕಾಗಬಹುದು (ಮೇಲಿನಂತೆ) ಅಥವಾ APIM ನೀತಿಯನ್ನು ಸರಿಪಡಿಸಬಹುದು. ನಿಮ್ಮ JWT ಯಲ್ಲಿ audience ನಿಮ್ಮ `<audience>` ನಲ್ಲಿ ಹೊಂದಿಕೆಯಾಗಿರಬೇಕು.

- **JSON ಮೆಟಾಡೇಟಾ ವಿಶ್ಲೇಷಣೆ:** OpenID ಸಂರಚನಾ JSON ಮಾನ್ಯವಾಗಿರಬೇಕು. Spring ಡೀಫಾಲ್ಟ್ ಸಂರಚನೆ ಮಾನಕ OIDC ಮೆಟಾಡೇಟಾ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಹೊರಡಿಸುತ್ತದೆ. ಅದರಲ್ಲಿ ಸರಿಯಾದ `issuer` ಮತ್ತು `jwks_uri` ಇದ್ದಾರೆ ಎಂದು ಪರಿಶೀಲಿಸಿ. ನೀವು Spring ಅನ್ನು ಪ್ರಾಕ್ಸಿ ಅಥವಾ ಪಾತ್ ಆಧಾರಿತ ಮಾರ್ಗದ ಹಿಂದೆ ಹೋಸ್ಟ್ ಮಾಡಿದರೆ, ಈ ಮೆಟಾಡೇಟಾದ URL ಗಳನ್ನು ದ್ವಿಗುಣ ಪರಿಶೀಲಿಸಿ. APIM ಈ ಮೌಲ್ಯಗಳನ್ನು ಹಾಗೆಯೇ ಬಳಸುತ್ತದೆ.

- **ನೀತಿ ಕ್ರಮ:** APIM ನೀತಿಯಲ್ಲಿ, `<validate-jwt>` ಅನ್ನು ಬ್ಯಾಕೆಂಡ್‌ಗೆ ಯಾವುದೇ ರೌಟಿಂಗ್‌ಗಿಂತ ಮುಂಚೆ ಇರಿಸಿ. ಇಲ್ಲದಿದ್ದರೆ, ಕರೆಗಳು ಮಾನ್ಯ ಟೋಕನ್ ಇಲ್ಲದೆ ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ತಲುಪಬಹುದು. `<validate-jwt>` ಅನ್ನು `<inbound>` ಅಡಿಯಲ್ಲಿ ತಕ್ಷಣ ಇರಿಸಬೇಕು (ಇನ್ನೊಂದು ಶರತ್ತು ಒಳಗಿಲ್ಲದೆ) APIM ಅದನ್ನು ಅನ್ವಯಿಸುತ್ತದೆ.

ಮೇಲಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸುವ ಮೂಲಕ, ನೀವು ನಿಮ್ಮ Spring AI MCP ಸರ್ವರ್ ಅನ್ನು Azure Container Apps ನಲ್ಲಿ ಚಾಲನೆ ಮಾಡಬಹುದು ಮತ್ತು Azure API Management ಮೂಲಕ ಇನ್‌ಕಮಿಂಗ್ OAuth2 JWT ಗಳನ್ನು ಕನಿಷ್ಠ ನೀತಿಯೊಂದಿಗೆ ಪರಿಶೀಲಿಸಬಹುದು. ಮುಖ್ಯ ಅಂಶಗಳು: Spring Auth ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು TLS ಜೊತೆಗೆ ಸಾರ್ವಜನಿಕವಾಗಿ ಬಹಿರಂಗಪಡಿಸಿ, OIDC ಅನ್ವೇಷಣೆಯನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ, ಮತ್ತು APIM ನ `validate-jwt` ಅನ್ನು OpenID ಸಂರಚನಾ URL ಗೆ ಸೂಚಿಸಿ (ಹಾಗಾಗಿ ಅದು JWKS ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪಡೆಯಬಹುದು). ಈ ವ್ಯವಸ್ಥೆ dev/test ಪರಿಸರಕ್ಕೆ ಸೂಕ್ತವಾಗಿದೆ; ಉತ್ಪಾದನೆಗಾಗಿ ಸರಿಯಾದ ರಹಸ್ಯ ನಿರ್ವಹಣೆ, ಟೋಕನ್ ಅವಧಿಗಳು ಮತ್ತು JWKS ನಲ್ಲಿ ಕೀಗಳ ರೋಟೇಶನ್ ಅನ್ನು ಪರಿಗಣಿಸಿ.
**ಉಲ್ಲೇಖಗಳು:** ಡೀಫಾಲ್ಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳಿಗಾಗಿ ಸ್ಪ್ರಿಂಗ್ ಅಥೋರೈಜೆಷನ್ ಸರ್ವರ್ ಡಾಕ್ಸ್ ನೋಡಿ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ಮತ್ತು OIDC ಸಂರಚನೆಗಾಗಿ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` ಉದಾಹರಣೆಗಳಿಗಾಗಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ APIM ಡಾಕ್ಸ್ ನೋಡಿ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ಮತ್ತು ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಮತ್ತು ಪ್ರಮಾಣಪತ್ರಗಳಿಗಾಗಿ ಅಜೂರ್ ಕಂಟೈನರ್ ಅಪ್ಸ್ ಡಾಕ್ಸ್ ನೋಡಿ ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->