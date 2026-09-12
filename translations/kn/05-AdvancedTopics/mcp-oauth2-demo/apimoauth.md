# ಸ್ಪ್ರಿಂಗ್ AI MCP ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಅಜೂರ್ ಕಂಟೇನರ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ನಿಯೋಜನ ಮಾಡುವುದು

> [!WARNING]
> ಈ ಸಂಯೋಜಿತ ಅನುಮತಿ/ಸಂಪನ್ಮೂಲ ಸೆರ್ವರ್ ಕಲಿಕೆ ಮತ್ತು
> ಡೆವ್/ಟೆಸ್ಟ್ ಉಪಯೋಗಕ್ಕೆ ಉದ್ದೇಶಿಸಲಾಗಿದ್ದು, ಪ್ರೊಡಕ್ಷನ್ ಸಿಸ್ಟಮ್‌ಗಳು ಸಮರ್ಪಿತ ಗುರುತಿನ ಪ್ರೊವೈಡರ್,
> ಸದೃಢ ಸೈನ್ ಕೀಗಳು ಮತ್ತು ನಿರ್ವಹಿತ ರಹಸ್ಯ ಅಂಗಡಿಯಲ್ಲಿ ಸಂಗ್ರಹಿಸಿದ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಬಳಸಬೇಕು.

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *ಚಿತ್ರ: ಸ್ಪ್ರಿಂಗ್ ಅಡಳಿತ ಸರ್ವರ್‌ೊಂದಿಗೆ ಭದ್ರಗೊಳಿಸಲಾದ ಸ್ಪ್ರಿಂಗ್ AI MCP ಸರ್ವರ್. ಸರ್ವರ್ ಅಕ್ಸೆಸ್ ಟೋಕನ್‌ಗಳನ್ನು ಕ್ಲೈಂಟ್‌ಗಳಿಗೆ ನೀಡುತ್ತದೆ ಮತ್ತು ಅವುಗಳನ್ನು ಇನ್‌ಕಮಿಂಗ್ ವಿನಂತಿಗಳ ಮೇಲೆ ಪರಿಶೀಲಿಸುತ್ತದೆ (ಮೂಲ: ಸ್ಪ್ರಿಂಗ್ ಬ್ಲಾಗ್) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* ಸ್ಪ್ರಿಂಗ್ MCP ಸರ್ವರ್ ಅನ್ನು ನಿಯೋಜಿಸಲು, ಅದನ್ನು ಕಂಟೇನರ್ ಆಗಿ ಬಿಲ್ಡ್ ಮಾಡಿ ಅಜೂರ್ ಕಂಟೇನರ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಸಾರ್ವಜನಿಕ ಇಂಗ್ರೆಸ್ ಜೊತೆಗೆ ಬಳಸಿ. ಉದಾಹರಣೆಗೆ, ಅಜೂರ್ CLI ಬಳಸಿ ನೀವು ಈ ಕೆಳಗಿನಂತೆ ಕಾರ್ಯನಿರ್ವಹಿಸಬಹುದು:

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

ಇದು ಸಾಮಾಜಿಕ ಪ್ರವೇಶ ಹೊಂದಿರುವ ಕಂಟೇನರ್ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು HTTPS ಸಕ್ರಿಯಗೊಂಡು ಸೃಷ್ಟಿಸುತ್ತದೆ (ಡೀಫಾಲ್ಟ್ `*.azurecontainerapps.io` ಡೊಮೇನ್‌ನಲ್ಲಿ ಅಜೂರ್ ಉಚಿತ TLS ಪ್ರಮಾಣಪತ್ರವನ್ನು ನೀಡುತ್ತದೆ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ಆ ಸೂಚನೆಯಲ್ಲಿ ಆ್ಯಪ್‌ನ FQDN (ಉದಾ. `my-mcp-app.eastus.azurecontainerapps.io`) ಸೇರಿದೆ, ಇದು **issuer URL** ನೇಮಕೆಯಾಗುತ್ತದೆ. APIM ಆ್ಯಪ್‌ನ್ನು ತಲುಪಲು HTTP ಇಂಗ್ರೆಸ್ ಸಕ್ರಿಯವಾಗಿರಬೇಕು (ಮೇಲಿನಂತೆ). ಪರೀಕ್ಷೆ/ಡೆವ್ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ, `--ingress external` ಆಯ್ಕೆಯನ್ನು ಬಳಸಿಕೊಳ್ಳಿ (ಅಥವಾ TLS ಸಹಿತ ಕಸ್ಟಮ್ ಡೊಮೇನ್ ಅನ್ನು ಬಂಧಿಸಿ ಮೈಸ್ರೋಸಾಫ್ಟ್ ಡಾಕ್ಸ್ ಪ್ರಕಾರ ([Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ಯಾವುದೇ ಸಂವೇದನಾಶೀಲ ಗುಣಲಕ್ಷಣಗಳನ್ನು (ಜೊತೆಗೆ OAuth ಕ್ಲೈಂಟ್ ಸೀಕ್ರೆಟ್‌ಗಳು) ಕಂಟೇನರ್ ಅಪ್ಲಿಕೇಶನ್ ರಹಸ್ಯಗಳಲ್ಲಿ ಅಥವಾ ಅಜೂರ್ ಕೀ ವಾಲ್ಟ್‌ನಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ, ಮತ್ತು ಅವುಗಳನ್ನು ಪಾರಿಸರ ವದಂತಿಗಳಂತೆ ಕಂಟೇನರ್‌ಗೆ ನಕ್ಷೆಮಾಡಿ.

## ಸ್ಪ್ರಿಂಗ್ ಅಡಳಿತ ಸರ್ವರ್ ಅನ್ನು ಸಂರಚಿಸುವುದು

ನಿಮ್ಮ ಸ್ಪ್ರಿಂಗ್ ಬೂಟ್ ಆ್ಯಪ್ ಕೋಡ್‌ನಲ್ಲಿ, ಸ್ಪ್ರಿಂಗ್ ಅಡಳಿತ ಸರ್ವರ್ ಮತ್ತು ಸಂಪನ್ಮೂಲ ಸರ್ವರ್ ಸ್ಟಾರ್‌ಟರ್‌ಗಳನ್ನು ಸೇರಿಸಿ. ಡೆವ್/ಟೆಸ್ಟ್‌ನಲ್ಲಿ `client_credentials` ಗ್ರ್ಯಾಂಟ್‌ಗಾಗಿ `RegisteredClient` ಮತ್ತು JWT ಕೀ ಮೂಲವನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ. ಉದಾಹರಣೆಗಾಗಿ, `application.properties` ನಲ್ಲಿ ನೀವು ಕೆಳಕಂಡಂತೆ ಹೊಂದಿಸಬಹುದು:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

ಅಡಳಿತ ಸರ್ವರ್ ಮತ್ತು ಸಂಪನ್ಮೂಲ ಸರ್ವರ್ ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಲು ಸیکیೂರಿಟಿ ಫಿಲ್ಟರ್ ಚೈನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ. ಉದಾಹರಣೆಗೆ:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // ಪ್ರಾಧಿಕಾರದ ಸರ್ವರ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ
            .apply(authzServer.and())
            // ಸಂಪನ್ಮೂಲ ಸರ್ವರ್ ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ (ಬರುವ ವಿನಂತಿಗಳಲ್ಲಿ JWT ಅನ್ನು ಪರಿಶೀಲಿಸಿ)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಿ (MCP ಸರ್ವರ್ ಬ್ರೌಸರ್-ಆಧಾರಿತವಲ್ಲ)
            .csrf(csrf -> csrf.disable())
            // ಕ್ಲೈಂಟ್ ಡೆಮೊ ಸಲಕರಣೆಗಳಿಗೆ CORS ಅನುಮತಿಸಿ
            .cors(withDefaults());
        return http.build();
    }

    // ಒಂದು ಇನ್‌ಮೆಮೊರಿ ಕ್ಲೈಂಟ್ (RegisteredClient) ಮತ್ತು JWK ಮೂಲವನ್ನು ನಿಶ್ಚಯಿಸಿ:
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
        // RSA ಕೀ ಅನ್ನು ರಚಿಸಿ (ಡೆವ್/ಟೆಸ್ಟ್‌ಗಾಗಿ, ಆರಂಭಿಸುವಾಗ ಹೊಸದಾಗಿ ರಚಿಸಿ)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ಈ ವ್ಯವಸ್ಥೆಯು ಡೀಫಾಲ್ಟ್ OAuth2 ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬಹಿರಂಗ ಮಾಡುತ್ತದೆ: ಟೋಕನ್‌ಗಳಿಗಾಗಿ `/oauth2/token` ಮತ್ತು JSON ವೆಬ್ ಕೀ ಸೆಟ್ ಗಾಗಿ `/oauth2/jwks`. (ಡೀಫಾಲ್ಟ್ ಸ್ಪ್ರಿಂಗ್‌ನ `AuthorizationServerSettings` `/oauth2/token` ಮತ್ತು `/oauth2/jwks` ಅನ್ನು ನಕ್ಷೆ ಮಾಡುತ್ತದೆ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) ಸರ್ವರ್ RSA ಕೀ ಆಹರಿಸಿ ಸಹಿ ಮಾಡಿದ JWT ಅಕ್ಸೆಸ್ ಟೋಕನ್‌ಗಳನ್ನು ನೀಡುತ್ತದೆ ಮತ್ತು ತನ್ನ ಸರಕಾರಿ ಕೀ ಅನ್ನು `https://<your-app>:/oauth2/jwks` ನಲ್ಲಿ ಪ್ರಕಟಿಸುತ್ತದೆ.

**OpenID Connect ಅನ್ವೇಷಣೆಯನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ:** APIMಗೆ issuer ಮತ್ತು JWKS ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪಡೆದುಕೊಳ್ಳಲು OIDC ಪ್ರೊವೈಡರ್ ಸಂರಚನಾ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ನೀವು ನಿಮ್ಮ ಸುರಕ್ಷತಾ ಸಂರಚನೆಗೆ `.oidc(Customizer.withDefaults())` ಸೇರಿಸುವ ಮೂಲಕ ಸಕ್ರಿಯಗೊಳಿಸಿ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ಉದಾಹರಣೆಗೆ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // </.well-known/openid-configuration ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸುತ್ತದೆ>
```

ಇದು `/.well-known/openid-configuration` ಅನ್ನು ಬಹಿರಂಗ ಮಾಡುತ್ತದೆ, APIM ಇದನ್ನು ಮೆಟಾಡೇಟಾ ಪಡೆಯಲು ಬಳಸಬಹುದು. ಕೊನೆಗೆ, ನೀವು JWT **audience** ಕ್ಲೇಮ್ ಅನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಲು ಬಯಸಬಹುದು, যাতে APIMನ `<audiences>` ಪರಿಶೀಲನೆ ಪಾಸಾಗಿ ಬಹುದು. ಉದಾಹರಣೆಗೆ, ಒಂದು ಟೋಕನ್ ಕಸ್ಟಮೈಸರ್ ಸೇರಿಸಿ:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // ಕಸ್ಟಮ್ ಪ್ರೇಕ್ಷಕರನ್ನು ಸೆಟ್ ಮಾಡಿ (ಉದಾ. ಗ್ರಾಹಕ ID ಅಥವಾ API ಗುರುತಿನೋಡು)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

ಇದು ಟೋಕನ್‌ಗಳು `"aud": ["mcp-client"]` ಅನ್ನು ಸಾಗಿಸುವಂತೆ ಖಚಿತಪಡಿಸುತ್ತದೆ, ಇದು APIM ನಿರೀಕ್ಷಿಸುವ ಕ್ಲೈಂಟ್ ಐಡಿ ಅಥವಾ ಸ್ಕೋಪ್‌ಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ.

## ಟೋಕನ್ ಮತ್ತು JWKS ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸುವುದು

ನಿಯೋಜನೆಯ ನಂತರ, ನಿಮ್ಮ ಆ್ಯಪ್‌ನ **issuer URL** `https://<app-fqdn>` ಆಗಿರುತ್ತದೆ, ಉದಾ. `https://my-mcp-app.eastus.azurecontainerapps.io`. ಅದರ OAuth2 ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳು:

- **ಟೋಕನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್:** `https://<app-fqdn>/oauth2/token` – ಇಲ್ಲಿ ಕ್ಲೈಂಟ್‌ಗಳು ಟೋಕನ್‌ಗಳನ್ನು ಪಡೆಯಬಹುದು (client_credentials ಫ್ಲೋ).
- **JWKS ಎಂಡ್‌ಪಾಯಿಂಟ್:** `https://<app-fqdn>/oauth2/jwks` – JWK ಸೆಟ್ ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ (APIM ಸಹಿ ಕೀಗಳನ್ನು ಪಡೆಯಲು ಬಳಸುತ್ತದೆ).
- **OpenID ಸಂರಚನೆ:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC ಅನ್ವೇಷಣೆ JSON (ಇಲ್ಲಿ `issuer`, `token_endpoint`, `jwks_uri` ಇತ್ಯಾದಿ ಇವೆ).  

APIM **OpenID ಸಂರಚನೆ URL** ಅನ್ನು ಸೂಚಿಸುತ್ತದೆ, ಇದರಿಂದ ಅದು `jwks_uri` ಅನ್ನು ಹುಡುಕುತ್ತದೆ. ಉದಾಹರಣೆಗೆ, ನಿಮ್ಮ ಕಂಟೇನರ್ ಆ್ಯಪ್ FQDN `my-mcp-app.eastus.azurecontainerapps.io` ಆಗಿದ್ದರೆ, APIMನ `<openid-config url="...">` ಬಳಸಬೇಕಾದ URL ಆಗಿರುತ್ತದೆ `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (ಡೀಫಾಲ್ಟ್ ಸ್ಪ್ರಿಂಗ್ ಆ ಮೆಟಾಡೇಟಾದಲ್ಲಿ `issuer` ಅನ್ನು ಅದೇ ಬೇಸ್ URL ಗೆ ಹೊಂದಿಸುತ್ತದೆ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## ಅಜೂರ್ API ನಿರ್ವಹಣೆಯನ್ನು ಸಂರಚಿಸುವುದು (`validate-jwt`)

ಅಜೂರ್ APIMನಲ್ಲಿ, `<validate-jwt>` ನೀತಿಯನ್ನು ಬಳಸಿ ಒಳಬರುವ JWTಗಳನ್ನು ನಿಮ್ಮ ಸ್ಪ್ರಿಂಗ್ ಅಡಳಿತ ಸರ್ವರ್ ವಿರುದ್ಧ ಪರಿಶೀಲಿಸುವ ಇನ್‌ಬೌಂಡ್ ನೀತಿ ಸೇರಿಸಿ. ಸರಳ ವ್ಯವಸ್ಥೆಗೆ, ನೀವು OpenID Connect ಮೆಟಾಡೇಟಾ URL ಅನ್ನು ಬಳಸಬಹುದು. ಉದಾಹರಣೆ ನೀತಿ ತುಣುಕನು:

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

ಈ ನೀತಿ APIMಗೆ ಸ್ಪ್ರಿಂಗ್ ಅಡಳಿತ ಸರ್ವರ್‌ನಿಂದ OpenID ಸಂರಚನೆಯನ್ನು ಪಡೆದುಕೊಂಡು JWKS ಅನ್ನು ಪಡೆಯಿಸಲು ಮತ್ತು ಪ್ರತಿಯೊಂದು ಟೋಕನ್ https://ASN1 ಮಾಲೀಕತ್ವ ಹೊಂದಿದ ನಂಬಿಕೆಯ ಕೀ ಸಹಿ ಮಾಡಲಾಗಿದೆ ಮತ್ತು ಸರಿಯಾದ ಪ್ರೇಕ್ಷಣೀಯತೆಗೆ (audience) ಹೊಂದಿರುತ್ತದೆ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸಲು ಸೂಚಿಸುತ್ತದೆ. (`<issuers>` ಅನ್ನು ತೆಗೆದುಹಾಕಿದರೆ, APIM ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಮೆಟಾಡೇಟಾದ `issuer` ಕ್ಲೇಮ್ ಅನ್ನು ಬಳಕೆ ಮಾಡುತ್ತದೆ.) `<audience>` ನಿಮ್ಮ ಕ್ಲೈಂಟ್ ಐಡಿ ಅಥವಾ API ಸಂಪನ್ಮೂಲ ಗುರುತಿಗೇರಿದೆ (ಮೇಲಿನ ಉದಾಹರಣೆಯಲ್ಲಿ `"mcp-client"` ಎಂದು ಹೊಂದಿಸಲಾಗಿದೆ). ಇದು ಮೈಕ್ರೋಸಾಫ್ಟ್ ದಸ್ತಾವೇಜುಗಳಲ್ಲಿ `<openid-config>` ಜೊತೆಗೆ `validate-jwt` ಬಳಕೆಯ ಅನುಕೂಲವಾಗಿದೆ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

ಪರಿಶೀಲನೆಯ ನಂತರ, APIM ವಿನಂತಿಯನ್ನು (ಅಸ್ಯಲ್ಡ್ `Authorization` ಹೆಡರ್ ಸೇರಿದಂತೆ) ಬ್ಯಾಕ್ಎಂಡ್ ಗೆ ಮುಂದುವರಿಸುತ್ತದೆ. ಸ್ಪ್ರಿಂಗ್ ಆ್ಯಪ್ ಕೂಡ ಸಂಪನ್ಮೂಲ ಸರ್ವರ್ ಆಗಿದ್ದರಿಂದ ಟೋಕನ್ ಅನ್ನು ಮರುಪರಿಶೀಲಿಸುತ್ತದೆ, ಆದರೆ APIM ಈಗಾಗಲೇ ಅದರ ಮಾನ್ಯತೆಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿದೆ. (ಡೆವಲಪ್ಮೆಂಟ್‌ನಲ್ಲಿ, ನೀವು APIMನ ಪರಿಶೀಲನೆಗೆ ನಂಬಿಕೆ ಇಟ್ಟುಕೊಂಡು ಆ್ಯಪ್‌ನಲ್ಲಿ ಹೆಚ್ಚುವರಿ ಪರಿಶೀಲನೆಗಳನ್ನು ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಬಹುದು, ಆದರೆ ಎರಡನ್ನು ಇಟ್ಟುಕೊಂಡಿರುವುದು ಸುರಕ್ಷಿತ.)

## ಉದಾಹರಣೆ ಸೆಟ್ಟಿಂಗ್‌ಗಳು

| ಸೆಟ್ಟಿಂಗ್             | ಉದಾಹರಣೆ ಮೌಲ್ಯ                                                    | ಟಿಪ್ಪಣಿಗಳು                                    |
|---------------------|------------------------------------------------------------------|--------------------------------------------|
| **issuer**           | `https://my-mcp-app.eastus.azurecontainerapps.io`                | ನಿಮ್ಮ ಕಂಟೇನರ್ ಆಪ್ URL (ಆಧಾರ URI)               |
| **ಟೋಕನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | ಡೀಫಾಲ್ಟ್ ಸ್ಪ್ರಿಂಗ್ ಟೋಕನ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))   |
| **JWKS ಎಂಡ್‌ಪಾಯಿಂಟ್** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | ಡೀಫಾಲ್ಟ್ JWK ಸೆಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))     |
| **OpenID ಸಂರಚನೆ**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC ಅನ್ವೇಷಣಾ ಡಾಕ್ಯುಮೆಂಟ್ (ಸ್ವಯಂಚಾಲಿತವಾಗಿ ರಚಿತ) |
| **APIM ಪ್ರೇಕ್ಷಣೀಯತೆ** | `mcp-client`                                                     | OAuth ಕ್ಲೈಂಟ್ ಐಡಿ ಅಥವಾ API ಸಂಪನ್ಮೂಲ ಹೆಸರು       |
| **APIM ನೀತಿ**         | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ಈ URL ಅನ್ನು ಬಳಕೆ ಮಾಡುತ್ತದೆ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## ಸಾಮಾನ್ಯ ತಪ್ಪುಗಳು

- **HTTPS/TLS:** APIM ಗೇಟ್ವೇಗೆ OpenID/JWKS ಎಂಡ್‌ಪಾಯಿಂಟ್ HTTPS ಆಗಿದ್ದು ಮಾನ್ಯ ಪ್ರಮಾಣಪತ್ರ ಹೊಂದಿರಬೇಕು. ಡೀಫಾಲ್ಟ್ ಅಜೂರ್ ಕಂಟೇನರ್ ಅಪ್ಲಿಕೇಶನ್ಗಳು ಆಜೂರ್ ನಿರ್ವಹಿಸುವ ಡೊಮೇನ್‌ಗೆ ವಿಶ್ವಾಸಾರ್ಹ TLS ಪ್ರಮಾಣಪತ್ರವನ್ನು ಒದಗಿಸುತ್ತದೆ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). ನೀವು ಕಸ್ಟಮ್ ಡೊಮೇನ್ ಬಳಸದಿದ್ದರೆ, ಒಂದು ಪ್ರಮಾಣಪತ್ರವನ್ನು ಬಂಧಿಸಲು ಖಚಿತವಾಗಿರಿ (ನೀವು ಅಜೂರ್ ಉಚಿತ ನಿರ್ವಹಿತ ಪ್ರಮಾಣಪತ್ರ ವೈಶಿಷ್ಟ್ಯವನ್ನು ಬಳಸಬಹುದು) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM ಎಂಡ್‌ಪಾಯಿಂಟ್‌ನ ಪ್ರಮಾಣಪತ್ರವನ್ನು ನಂಬದೇ ಇದ್ದರೆ `<validate-jwt>` ಮೆಟಾಡೇಟಾವನ್ನು ಪಡೆದುಕೊಳ್ಳಲು ವಿಫಲವಾಗುತ್ತದೆ.

- **ಎಂಡ್‌ಪಾಯಿಂಟ್ ಲಭ್ಯತೆ:** APIMರಿಂದ ಸ್ಪ್ರಿಂಗ್ ಆ್ಯಪ್‌ನ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳು ತಲುಪಬಹುದಾಗಿರಬೇಕು. `--ingress external` ಅನ್ನು ಬಳಸುವುದು (ಅಥವಾ ಪೋರ್ಟಲ್ನಲ್ಲಿ ಇಂಗ್ರೆಸ್ ಸಕ್ರಿಯಗೊಳಿಸುವುದು) ಸುಲಭವಲ್ಲ. ನೀವು ಅಂತರ್ಗತ ಅಥವಾ vNet-ಬೌಂಡ್ ಪರಿಸರವನ್ನು ಆಯ್ದುಕೊಂಡಿದ್ದರೆ, APIM (ಡೀಫಾಲ್ಟ್‌ನಲ್ಲಿ ಸಾರ್ವಜನಿಕ) ಅದನ್ನು ತಲುಪದಿರಬಹುದು. ಪರೀಕ್ಷೆ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ, ಸಾರ್ವಜನಿಕ ಇಂಗ್ರೆಸ್ ಬರುವುದು ಹೆಚ್ಚು ಬೇಸರವಿಲ್ಲದೆ `.well-known` ಮತ್ತು `/jwks` URL‌ಗಳಿಗೆ APIM ಕರೆ ಮಾಡಲು ಅನುಕೂಲಕರ.

- **OpenID ಅನ್ವೇಷಣೆ ಸಕ್ರಿಯಗೊಳಿಸಲಾಗಿದೆ:** ಡೀಫಾಲ್ಟ್ ಸ್ಪ್ರಿಂಗ್ ಅಡಳಿತ ಸರ್ವರ್ `/.well-known/openid-configuration` ಅನ್ನು OIDC ಸಕ್ರಿಯಗೊಳಿಸದೆ ಬಹಿರಂಗಪಡಿಸುವುದಿಲ್ಲ. ಮೇಲಿನಂತೆ `.oidc(Customizer.withDefaults())` ಅನ್ನು ನಿಮ್ಮ ಸುರಕ್ಷತಾ ಸಂರಚನೆಯಲ್ಲಿ ಸೇರಿಸಿ, ಇದರಿಂದ ಪ್ರೊವೈಡರ್ ಸಂರಚನಾ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಸಕ್ರಿಯವಾಗಿರುತ್ತದೆ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ಇಲ್ಲದಿದ್ದರೆ APIMನ `<openid-config>` ಕರೆದಾಗ 404 ತಪ್ಪು ಬರುತ್ತದೆ.

- **ಪ್ರೇಕ್ಷಣೀಯತೆ ಕ್ಲೇಮ್:** ಸ್ಪ್ರಿಂಗ್ ಡೀಫಾಲ್ಟ್ ವರ್ತನೆ `aud` ಕ್ಲೇಮ್ ಅನ್ನು ಕ್ಲೈಂಟ್ ಐಡಿ ಆಗಿ ಹೊಂದಿಸುತ್ತದೆ. APIMನ `<audience>` ಪರಿಶೀಲನೆ ವಿಫಲವಾಗಿದ್ದರೆ, ನೀವು ಮೇಲ್ಕಾಣಿಸಿದಂತೆ ಟೋಕನ್ ಅನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಬೇಕಾಗಬಹುದು ಅಥವಾ APIM ನೀತಿಯನ್ನೊಂದಕ್ಕೆ ತಿದ್ದುಪಡಿ ಮಾಡಬೇಕಾಗಬಹುದು. ನಿಮ್ಮ JWTಯಲ್ಲಿನ ಪ್ರೇಕ್ಷಣೀಯತೆ `<audience>` ನಲ್ಲಿ ನೀವು ಹೊಂದಿಸಿರುವದಕ್ಕೆ ಹೊಂದಿರಬೇಕು.

- **JSON ಮೆಟಾಡೇಟಾ ಪರಶೀಲನೆ:** OpenID ಸಂರಚನಾ JSON ಮಾನ್ಯವಾಗಿರಬೇಕು. ಸ್ಪ್ರಿಂಗ್ ಡೀಫಾಲ್ಟ್ ಕಾನ್ಫಿಗ್ ಒಂದು ಸ್ಟ್ಯಾಂಡರ್ಡ್ OIDC ಮೆಟಾಡೇಟಾ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಹೊರತರುತ್ತದೆ. ಅದು ಸರಿಯಾದ `issuer` ಮತ್ತು `jwks_uri` ಒಳಗೊಂಡಿರುತ್ತದೆಯೆಂದು ಪರಿಶೀಲಿಸಿ. ನೀವು ಸ್ಪ್ರಿಂಗ್ ಅನ್ನು ಪ್ರಾಕ್ಸಿ ಅಥವಾ ಪಥಾಧಾರಿತ ಮಾರ್ಗದ ಹಿಂದೆ ಹೋಸ್ಟ್ ಮಾಡುತ್ತಿದ್ದರೆ, ಈ ಮೆಟಾಡೇಟಾದಲ್ಲಿ URL-ಗಳನ್ನು ದ್ವಿಗುಣವಾಗಿ ಪರಿಶೀಲಿಸಿ. APIM ಈ ಮೌಲ್ಯಗಳನ್ನು ಹಾಗೆಯೇ ಬಳಸಲಿದೆ.

- **ನೀತಿ ಕ್ರಮ:** APIM ನೀತಿಯಲ್ಲಿ, `<validate-jwt>` ಅನ್ನು ಬ್ಯಾಕ್ಎಂಡ್‌ ಜೊತೆ ಯಾವುದೇ ಮಾರ್ಗ ನಿರ್ದೇಶನಕ್ಕೂ ಮುಂಚಿತವಾಗಿ ಇರಿಸಿ. ಇಲ್ಲದಿದ್ದರೆ, ಕರೆಗಳು ಮಾನ್ಯ ಟೋಕನ್ ಇಲ್ಲದೆ ನಿಮ್ಮ ಆ್ಯಪ್‌ ಅನ್ನು ತಲುಪಬಹುದು. ಮತ್ತು `<validate-jwt>` ನು `<inbound>` ಅಡಿ ತಕ್ಷಣವಾಗಿರಬೇಕು (ಇನ್ನೊಂದು ಶರತ್ತು ಒಳಗಲ್ಲ) ಇದರಿಂದ APIM ಅದನ್ನು ಅನ್ವಯಿಸುತ್ತದೆ.

ಮೇಲಿನ ಕ್ರಮಗಳನ್ನು ಅನುಸರಿಸುವ ಮೂಲಕ, ನೀವು ನಿಮ್ಮ ಸ್ಪ್ರಿಂಗ್ AI MCP ಸರ್ವರ್ ಅನ್ನು ಅಜೂರ್ ಕಂಟೇನರ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಚಾಲನೆ ಮಾಡಿ, ಅಜೂರ್ API ನಿರ್ವಹಣೆ ಮೂಲಕ ಒಳಬರುವ OAuth2 JWT ಗಳನ್ನು ಕಡಿಮೆ ನೀತಿಯೊಂದಿಗೆ ಪರಿಶೀಲಿಸಬಹುದು. ಮುಖ್ಯ ಅಂಶಗಳು: ಸ್ಪ್ರಿಂಗ್ ಅಡಳಿತ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು TLS ಜತೆ ಸಾರ್ವಜನಿಕವಾಗಿ ಬಹಿರಂಗಗೊಳಿಸಿ, OIDC ಅನ್ವೇಷಣೆಯನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ, ಮತ್ತು APIMನ `validate-jwt` ಅನ್ನು OpenID ಸಂರಚನಾ URL ಗೆ ಸೂಚಿಸಿ (ಅದರಿಂದ ಅದು JWKS ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪಡೆದ್ಕೊಳ್ಳುತ್ತದೆ). ಇದು ಡೆವ್/ಟೆಸ್ಟ್ ಪರಿಸರಕ್ಕಾಗಿ ಸೂಕ್ತ; ಪ್ರೊಡಕ್ಷನ್‌ಗೆ ಸರಿಯಾದ ರಹಸ್ಯ ನಿರ್ವಹಣೆ, ಟೋಕನ್ ಅವಧಿಗಳು ಮತ್ತು JWKS ತಿರುಗಿಸುವಿಕೆಗಳನ್ನು ಪರಿಗಣಿಸಿ.


**ಉಲ್ಲೇಖಗಳು:** ಡೀಫಾಲ್ಟ್ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳಿಗಾಗಿ ಸ್ಪ್ರಿಂಗ್ ಅಥೋರೈಸೇಷನ್ ಸರ್ವರ್ ಡಾಕ್ಸ್ ನೋಡಿ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ಮತ್ತು OIDC ಸಂರಚನೆಗಾಗಿ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` ಉದಾಹರಣೆಗಳಿಗೆ ಮೈಸ್ರೋಸಾಫ್ಟ್ APIM ಡಾಕ್ಸ್ ನೋಡಿ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ಮತ್ತು ಅಜೂರ್ ಕಂಟೇನರ್ ಅಪ್ಸ್ ಡಾಕ್ಸ್ ವಿತರಣೆ ಮತ್ತು ಪ್ರಮಾಣಪತ್ರಗಳಿಗಾಗಿ ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->