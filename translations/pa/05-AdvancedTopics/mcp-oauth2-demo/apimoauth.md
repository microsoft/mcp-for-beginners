# ਸਪਰਿੰਗ ਏਆਈ MCP ਐਪ ਨੂੰ Azure ਕੰਟੇਨਰ ਐਪਸ 'ਤੇ ਤਾਇਨਾਤ ਕਰਨਾ

> [!WARNING]
> ਇਹ ਮਿਲੀ-ਜੁਲੀ ਅਥਰਾਈਜੇਸ਼ਨ/ਸੰਸਾਧਨ ਸਰਵਰ ਸਿੱਖਣ ਅਤੇ ਵਿਕਾਸ/ਟੈਸਟ ਉਪਯੋਗ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। ਪ੍ਰੋਡਕਸ਼ਨ ਸਿਸਟਮਾਂ ਲਈ ਸਮਰਪਿਤ ਪਹਿਚਾਣ ਪ੍ਰਦਾਤਾ, ਸਥਾਈ ਸਾਈਨਿੰਗ ਕੁੰਜੀਆਂ, ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਸੁਰੱਖਿਅਤ ਸਟੋਰ ਵਿੱਚ ਰੱਖੇ ਗਏ ਪ੍ਰਮਾਣਪੱਤਰ ਵਰਤੇ ਜਾਣ ਚਾਹੀਦੇ ਹਨ।
> 




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

ਇਹ HTTPS ਸਮਰਥਿਤ ਪਬਲਿਕ ਤੌਰ 'ਤੇ ਪਹੁੰਚਯੋਗ ਕੰਟੇਨਰ ਐਪ ਬਣਾਉਂਦਾ ਹੈ (Azure ਮੂਲ `*.azurecontainerapps.io` ਡੋਮੇਨ ਲਈ ਮੁਫ਼ਤ TLS ਸਰਟੀਫਿਕੇਟ ਜਾਰੀ ਕਰਦਾ ਹੈ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ਕਮਾਂਡ ਆਉਟਪੁੱਟ ਵਿੱਚ ਐਪ ਦਾ FQDN ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ (ਜਿਵੇਂ ਕਿ `my-mcp-app.eastus.azurecontainerapps.io`), ਜੋ **issuer URL** ਆਧਾਰ ਬਣਦਾ ਹੈ। ਇਹ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ HTTP ਇੰਗਰੈਸ ਸਮਰਥਿਤ ਹੋਵੇ (ਜਿਵੇਂ ਉਪਰ ਦਿੱਤਾ ਗਿਆ ਹੈ) ਤਾਂ ਜੋ APIM ਐਪ ਤੱਕ ਪਹੁੰਚ ਸਕੇ। ਚੈੱਕ/ਡਿਵ ਵਿੱਚ, `--ingress external` ਵਿਕਲਪ ਵਰਤੋ (ਜਾਂ ਮਾਈਕ੍ਰੋਸੋਫਟ ਦੇ ਦਸਤਾਵੇਜ਼ਾਂ ਦੇ ਅਨੁਸਾਰTLS ਵਾਲਾ ਕਸਟਮ ਡੋਮੇਨ ਬਾਈਂਡ ਕਰੋ) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। ਜੇਕਰ ਕੋਈ ਸੰਵੇਦਨਸ਼ੀਲ ਪ੍ਰਾਪਰਟੀ ਹੈ (ਜਿਵੇਂ OAuth ਕਲਾਇੰਟ ਸੀਕ੍ਰੇਟ) ਤਾਂ ਉਸਨੂੰ Container Apps ਸਕ੍ਰਿਪਟਾਂ ਜਾਂ Azure Key Vault ਵਿੱਚ ਸਟੋਰ ਕਰੋ, ਅਤੇ ਕੰਟੇਨਰ ਵਿੱਚ ਵਾਤਾਵਰਨੀਆ ਪਰਿਵਰਤਨਸ਼ੀਲਾਂ ਵਜੋਂ ਮੈਪ ਕਰੋ। 

## ਸਪਰਿੰਗ ਅਥਰਾਈਜੇਸ਼ਨ ਸਰਵਰ ਕੰਫਿਗਰ ਕਰਨਾ

ਆਪਣੇ Spring Boot ਐਪ ਦੇ ਕੋਡ ਵਿੱਚ Spring Authorization Server ਅਤੇ Resource Server ਸਟਾਰਟਰ ਸ਼ਾਮਿਲ ਕਰੋ। ਇੱਕ `RegisteredClient` (ਵਿਕਾਸ/ਟੈਸਟ ਵਿਚ `client_credentials` ਗ੍ਰਾਂਟ ਲਈ) ਅਤੇ ਇੱਕ JWT ਕੀ ਸੋਰਸ ਨੂੰ ਕੰਫਿਗਰ ਕਰੋ। ਉਦਾਹਰਨ ਵਜੋਂ, `application.properties` ਵਿੱਚ ਤੁਰੰਤ ਇਹ ਲਿਖੋ:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Authorization Server ਅਤੇ Resource Server ਨੂੰ ਸੁਰੱਖਿਆ ਫਿਲਟਰ ਚੇਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰਕੇ ਸਰਗਰਮ ਕਰੋ। ਉਦਾਹਰਨ ਵਜੋਂ:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // ਥੀਕਰਾ ਸਰਵਰ ਦੇ ਐਂਡਪੌਇੰਟਸ ਸਰਗਰਮ ਕਰੋ
            .apply(authzServer.and())
            // ਰਿਸੋਰਸ ਸਰਵਰ ਨੂੰ ਸਰਗਰਮ ਕਰੋ (ਆਉਣ ਵਾਲੀਆਂ ਬੇਨਤੀਆਂ 'ਤੇ JWT ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF ਨੂੰ ਅਣਚਲ ਕਰੋ (MCP ਸਰਵਰ ਬ੍ਰਾਊਜ਼ਰ-ਅਧਾਰਿਤ ਨਹੀਂ ਹੈ)
            .csrf(csrf -> csrf.disable())
            // ਕਲਾਇੰਟ ਡੈਮੋ ਟੂਲਜ਼ ਲਈ CORS ਦੀ ਸਹੂਲਤ ਦਿਓ
            .cors(withDefaults());
        return http.build();
    }

    // ਇੱਕ ਇਨ-ਮੇਮੋਰੀ ਕਲਾਇੰਟ (RegisteredClient) ਅਤੇ ਇੱਕ JWK ਸਰੋਤ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ:
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
        // ਇੱਕ RSA ਕੁੰਜੀ ਬਣਾਓ (ਡੈਵ/ਟੈਸਟ ਲਈ, ਸ਼ੁਰੂਆਤ 'ਤੇ ਨਵੀਂ ਬਣਾਓ)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ਇਹ ਸੈੱਟਅੱਪ ਮੂਲ OAuth2 ਐਂਡਪੌਇੰਟ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰੇਗਾ: `/oauth2/token` ਟੋਕਨਾਂ ਲਈ ਅਤੇ `/oauth2/jwks` JSON ਵਿਬ ਤੋਂ (JSON Web Key Set) ਲਈ। (ਮੂਲ ਰੂਪ ਵਿੱਚ Spring ਦਾ `AuthorizationServerSettings` `/oauth2/token` ਅਤੇ `/oauth2/jwks` ਨੂੰ ਨਕਸ਼ਾ ਕਰਦਾ ਹੈ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) ਸਰਵਰ RSA ਕੁੰਜੀ ਨਾਲ ਸਮਰੱਜਿਤJWT ਐਕਸੈਸ ਟੋਕਨ ਜਾਰੀ ਕਰੇਗਾ ਅਤੇ ਆਪਣਾ ਜਨਤਕ ਕੁੰਜੀ `https://<your-app>:/oauth2/jwks` 'ਤੇ ਪ੍ਰਕਾਸ਼ਿਤ ਕਰੇਗਾ।

**OpenID Connect ਖੋਜ ਸਰਗਰਮ ਕਰੋ:** APIM ਲਈ issuer ਅਤੇ JWKS ਨੂੰ ਆਪਣੇ ਆਪ ਲੈਣ ਲਈ, ਸੁਰੱਖਿਆ ਕੰਫਿਗਰੇਸ਼ਨ ਵਿੱਚ `.oidc(Customizer.withDefaults())` ਜੋੜੋ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ਉਦਾਹਰਨ ਵਜੋਂ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration ਨੂੰ ਯੋਗ ਕਰਦਾ ਹੈ
```

ਇਹ `/.well-known/openid-configuration` ਨੂੰ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰਦਾ ਹੈ ਜਿਸਨੂੰ APIM ਮੈਟਾਂਡਾਟਾ ਲਈ ਵਰਤ ਸਕਦਾ ਹੈ। ਆਖਿਰ ਵਿੱਚ, ਤੁਸੀਂ JWT **audience** ਕਲੇਮ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰਨਾ ਚਾਹੋਗੇ ਤਾਂ ਜੋ APIM ਦਾ `<audiences>` ਚੈੱਕ ਪਾਸ ਹੋ ਜਾਵੇ। ਉਦਾਹਰਨ ਵਜੋਂ, ਟੋਕਨ ਕਸਟਮਾਈਜ਼ਰ ਜੋੜੋ:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // ਇੱਕ ਕਸਟਮ ਦਰਸ਼ਕ ਸੈੱਟ ਕਰੋ (ਜਿਵੇਂ ਕਿ ਕਲਾਇੰਟ ID ਜਾਂ API ਪਹਿਚਾਣਕਾਰ)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਟੋਕਨਾਂ ਵਿੱਚ `"aud": ["mcp-client"]` ਸ਼ਾਮਲ ਹੈ, ਜੋ APIM ਦੇ ਉਮੀਦ ਕੀਤਾ ਕਲਾਇੰਟ ID ਜਾਂ ਸਕੋਪ ਨਾਲ ਮਿਲਦਾ ਹੈ। 

## ਟੋਕਨ ਅਤੇ JWKS ਐਂਡਪੌਇੰਟ ਖੁਲਾਸਾ

ਤਾਇਨਾਤੀ ਤੋਂ ਬਾਅਦ, ਤੁਹਾਡੇ ਐਪ ਦਾ **issuer URL** `https://<app-fqdn>` ਹੋਵੇਗਾ, ਜਿਵੇਂ ਕਿ `https://my-mcp-app.eastus.azurecontainerapps.io`। ਇਸਦੇ OAuth2 ਐਂਡਪੌਇੰਟ ਹਨ:

- **ਟੋਕਨ ਐਂਡਪੌਇੰਟ:** `https://<app-fqdn>/oauth2/token` – ਕਲਾਇੰਟ ਇੱਥੋਂ ਟੋਕਨ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਨ (client_credentials ਫਲੋ ਲਈ)।
- **JWKS ਐਂਡਪੌਇੰਟ:** `https://<app-fqdn>/oauth2/jwks` – JWK ਸੈੱਟ ਵਾਪਸ ਕਰਦਾ ਹੈ (APIM ਸਾਈਨਿੰਗ ਕੁੰਜੀਆਂ ਲਈ ਵਰਤਦਾ ਹੈ)।
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC ਖੋਜ JSON (ਜਿਸ ਵਿੱਚ `issuer`, `token_endpoint`, `jwks_uri` ਆਦਿ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ)।  

APIM **OpenID configuration URL** ਤੇ ਇਸ਼ਾਰਾ ਕਰੇਗਾ, ਜਿੱਥੋਂ ਇਹ `jwks_uri` ਦੀ ਖੋਜ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਹਾਡਾ Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` ਹੈ ਤਾਂ APIM ਦਾ `<openid-config url="...">` `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। (Spring ਮੂਲ ਰੂਪ ਵਿੱਚ ਉਸ ਮੈਟਾਂਡਾਟਾ ਵਿੱਚissuer ਨੂੰ ਉਸੇ ਬੇਸ URL ਤੇ ਸੈੱਟ ਕਰੇਗਾ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API ਪ੍ਰਬੰਧਨ ਲਈ ਕੰਫਿਗਰੇਸ਼ਨ (`validate-jwt`)

Azure APIM ਵਿੱਚ, ਇੱਕ Inbound ਪਾਲੀਸੀ ਸ਼ਾਮਿਲ ਕਰੋ ਜੋ `<validate-jwt>` ਪਾਲੀਸੀ ਵਰਤ ਕੇ ਆ ਰਹੇ JWT ਦੀSpring Authorization Server ਮੁਕਾਬਲੇ ਜਾਂਚ ਕਰਦੀ ਹੈ। ਇੱਕ ਸਧਾਰਨ ਸੈੱਟਅੱਪ ਲਈ, OpenID Connect ਮੈਟਾਂਡਾਟਾ URL ਵਰਤ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਪਾਲੀਸੀ ਟੁਕੜਾ:

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

ਇਹ ਪਾਲੀਸੀ APIM ਨੂੰ ਕਹਿੰਦੀ ਹੈ ਕਿ ਇਹ Spring Auth Server ਤੋਂ OpenID ਕনਫিগਰੇਸ਼ਨ ਲੈ ਅਤੇ ਉਸ ਦਾ JWKS ਪ੍ਰਾਪਤ ਕਰੇ ਅਤੇ ਭਰੋਸੇਯੋਗ ਕੁੰਜੀ ਨਾਲ ਸਾਈਨ ਕੀਤੇ ਹਰ ਟੋਕਨ ਦੀ ਜਾਂਚ ਕਰੇ ਅਤੇ ਠੀਕ audience ਹੋਣ ਦੀ ਪੁਸ਼ਟੀ ਕਰੇ। (ਜੇ ਤੁਸੀਂ `<issuers>` ਅਨੁਪਸਥਿਤ ਰੱਖਦੇ ਹੋ, APIM ਮੈਟਾਂਡਾਟਾ ਤੋਂ issuer ਕਲੇਮ ਨੂੰ ਆਪਣੇ ਆਪ ਵਰਤੇਗਾ।) `<audience>` ਤੁਹਾਡੇ ਕਲਾਇੰਟ ID ਜਾਂ API ਰਿਸੋਰਸ ਆਈਡੈਂਟੀਫਾਇਰ ਨਾਲ ਮੇਲ ਖਾਣਾ ਚਾਹੀਦਾ ਹੈ (ਉਪਰਲੇ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ `"mcp-client"` ਸੈੱਟ ਕੀਤਾ)। ਇਹ Microsoft ਦੇ ਦਸਤਾਵੇਜ਼ਾਂ ਨਾਲ ਸਮਰੂਪ ਹੈ ਜੋ `validate-jwt` ਨੂੰ `<openid-config>` ਨਾਲ ਵਰਤਣ ਬਾਰੇ ਹੈ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

ਜਾਂਚ ਤੋਂ ਬਾਅਦ, APIM ਬੈਕਐਂਡ ਨੂੰ ਬੇਨਤੀ ਅੱਗੇ ਭੇਜੇਗਾ (ਮੂਲ `Authorization` ਹੈਡਰ ਸਮੇਤ)। ਕਿਉਂਕਿ ਸਪਰਿੰਗ ਐਪ ਵੀ ਇੱਕ ਰਿਸੋਰਸ ਸਰਵਰ ਹੈ, ਇਹ ਟੋਕਨ ਦੀ ਦੁਬਾਰਾ ਜਾਂਚ ਕਰੇਗਾ, ਪਰ APIM ਪਹਿਲਾਂ ਹੀ ਇਸ ਦੀ ਵੈਧਤਾ ਦੀਆਂ ਪੁਸ਼ਟੀਆਂ ਕਰ ਚੁੱਕਾ ਹੈ। (ਵਿਕਾਸ ਲਈ, ਤੁਸੀਂ APIM ਦੀ ਜਾਂਚ 'ਤੇ ਨਿਰਭਰ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਐਪ ਵਿੱਚ ਵਾਧੂ ਜਾਂਚਾਂ ਨੂੰ ਅਣਸਰਗਰਮ ਕਰ ਸਕਦੇ ਹੋ, ਪਰ ਇਹ ਦੋਹਾਂ ਨੂੰ ਜਾਰੀ ਰੱਖਣਾ ਸੁਰੱਖਿਅਤ ਹੈ।)

## ਉਦਾਹਰਣ ਸੈਟਿੰਗਜ਼

| ਸੈਟਿੰਗ           | ਉਦਾਹਰਣ ਮੁੱਲ                                                        | ਨੋਟਸ                                      |
|-----------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**       | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | ਤੁਹਾਡੇ ਕੰਟੇਨਰ ਐਪ ਦਾ URL (ਬੇਸ URI)        |
| **ਟੋਕਨ ਐਂਡਪੌਇੰਟ** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | ਡਿਫੌਲਟ ਸਪਰਿੰਗ ਟੋਕਨ ਐਂਡਪੌਇੰਟ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS ਐਂਡਪੌਇੰਟ** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | ਡਿਫੌਲਟ JWK ਸੈੱਟ ਐਂਡਪੌਇੰਟ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC ਖੋਜ ਦਸਤਾਵੇਜ਼ (ਆਪਮੈਡ)                |
| **APIM audience** | `mcp-client`                                                       | OAuth ਕਲਾਇੰਟ ID ਜਾਂ API ਰਿਸੋਰਸ ਨਾਮ           |
| **APIM ਪਾਲੀਸੀ**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ਇਸ URL ਨੂੰ ਵਰਤਦਾ ਹੈ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## ਆਮ ਗਲਤੀਆਂ

- **HTTPS/TLS:** APIM ਗੇਟਵੇ ਨੂੰ ਲੋੜ ਹੈ ਕਿ OpenID/JWKS ਐਂਡਪੌਇੰਟ HTTPS ਹੋਵੇ ਅਤੇ ਮਾਨਯ ਸਰਟੀਫਿਕੇਟ ਦੇ ਨਾਲ ਹੋਵੇ। ਮੂਲ ਰੂਪ ਵਿੱਚ, Azure Container Apps Azure ਪ੍ਰਬੰਧਿਤ ਡੋਮੇਨ ਲਈ ਭਰੋਸੇਯੋਗ TLS ਸਰਟੀਫਿਕੇਟ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। ਜੇਕਰ ਤੁਸੀਂ ਕਸਟਮ ਡੋਮੇਨ ਵਰਤਦੇ ਹੋ, ਤਾਂ ਸਰਟੀਫਿਕੇਟ ਬਾਈਂਡ ਕਰਨ ਦੀ ਯਕੀਨੀ ਬਣਾ ਲਓ (ਤੁਸੀਂ Azure ਦੀ ਮੁਫ਼ਤ ਪ੍ਰਬੰਧਿਤ ਸਰਟੀਫਿਕੇਟ ਵਿਸ਼ੇਸ਼ਤਾ ਵਰਤ ਸਕਦੇ ਹੋ) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। ਜੇ APIM ਐਂਡਪੌਇੰਟ ਦੇ ਸਰਟੀਫਿਕੇਟ 'ਤੇ ਭਰੋਸਾ ਨਹੀਂ ਕਰ ਸਕਦਾ, `<validate-jwt>` ਮੈਟਾਂਡਾਟਾ ਪ੍ਰਾਪਤ ਕਰਨ ਵਿੱਚ ਅਸਫਲ ਹੋਵੇਗਾ।

- **ਐਂਡਪੌਇੰਟ ਪਹੁੰਚਯੋਗਤਾ:** ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਪਰਿੰਗ ਐਪ ਦੇ ਐਂਡਪੌਇੰਟ APIM ਤੋਂ ਪਹੁੰਚਯੋਗ ਹਨ। `--ingress external` (ਜਾਂ ਪੋਰਟਲ ਵਿੱਚ ਇੰਗਰੈਸ ਸਮਰਥਿਤ ਕਰਨਾ) ਸਭ ਤੋਂ ਸੌਖਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਅੰਦਰੂਨੀ ਜਾਂ vNet-ਬੰਨ੍ਹੀ ਵਾਤਾਵਰਨ ਦੀ ਚੋਣ ਕੀਤੀ ਹੈ, APIM (ਡਿਫੌਲਟ ਵਜੋਂ ਪਬਲਿਕ) ਅਕਸਰ ਇਸ ਤੱਕ ਨਹੀਂ ਪਹੁੰਚ ਸਕਦੀ ਜੇ ਉਸਨੂੰ ਇਕੋ VNet ਵਿੱਚ ਨਹੀਂ ਰੱਖਿਆ ਗਿਆ। ਟੈਸਟ ਸੈੱਟਅੱਪ ਵਿੱਚ, ਜਨਤਕ ਇੰਗਰੈਸ ਅਗਰ੍ਹਾ ਕਰੋ ਤਾਂ ਜੋ APIM `.well-known` ਅਤੇ `/jwks` URL ਨੂੰ ਕਾਲ ਕਰ ਸਕੇ।

- **OpenID ਖੋਜ ਸਰਗਰਮ:** ਮੂਲ ਰੂਪ ਵਿੱਚ, Spring Authorization Server `/.well-known/openid-configuration` ਨਹੀਂ ਖੋਲ੍ਹਦਾ ਜਦ ਤੱਕ OIDC ਸਰਗਰਮ ਨਾ ਕੀਤਾ ਹੋਵੇ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸੁਰੱਖਿਆ ਕਨਫਿਗਰੇਸ਼ਨ ਵਿੱਚ `.oidc(Customizer.withDefaults())` ਸ਼ਾਮਿਲ ਹੈ (ਜਿਵੇਂ ਉਪਰ ਦਿੱਤਾ ਗਿਆ ਹੈ) ਤਾਂ ਜੋ ਪ੍ਰਦਾਤਾ ਕੰਫਿਗਰੇਸ਼ਨ ਐਂਡਪੌਇੰਟ ਸਰਗਰਮ ਰਹੇ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ਨਹੀਂ ਤਾਂ APIM ਦਾ `<openid-config>` ਕਾਲ 404 ਦਿਖਾਵੇਗਾ।

- **Audience ਕਲੇਮ:** ਸਪਰਿੰਗ ਦਾ ਮੂਲਵਾਰਤਾਵਿਹਾਰ `aud` ਕਲੇਮ ਨੂੰ ਕਲਾਇੰਟ ID ਤੇ ਸੈੱਟ ਕਰਦਾ ਹੈ। ਜੇ APIM ਦਾ `<audience>` ਚੈੱਕ ਅਸਫਲ ਰਹਿੰਦਾ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਟੋਕਨ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰਨਾ ਪੈ ਸਕਦਾ ਹੈ (ਜਿਵੇਂ ਉਪਰ ਦਿਖਾਇਆ) ਜਾਂ APIM ਪਾਲੀਸੀ ਨੂੰ ਸੰਸ਼ੋਧਿਤ ਕਰੋ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ JWT ਦਾ ਦਰਸ਼ਿਤ ਦਰਸ਼ਕ (`audience`) `<audience>` ਵਿੱਚ ਦਿੱਤੇ ਮੁੱਲ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੋਵੇ।

- **JSON ਮੈਟਾਂਡਾਟਾ ਵਿਵਾਦ ਮੁਕਾਬਲਾ:** OpenID ਕਨਫਿਗਰੇਸ਼ਨ JSON ਵੈਧ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। Spring ਦਾ ਡਿਫੌਲਟ ਕਨਫਿਗਰੇਸ਼ਨ ਸਧਾਰਣ OIDC ਮੈਟਾਂਡਾਟਾ ਦਸਤਾਵੇਜ਼ ਜਾਰੀ ਕਰਦਾ ਹੈ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਸ ਵਿੱਚ ਸਹੀ `issuer` ਅਤੇ `jwks_uri` ਸ਼ਾਮਿਲ ਹਨ। ਜੇ ਤੁਸੀਂ	Spring ਨੂੰ ਪ੍ਰਾਕਸੀ ਜਾਂ ਪਾਥ-ਅਧਾਰਤ ਰੂਟ ਪਿੱਛੇ ਹੋਸਟ ਕਰਦੇ ਹੋ, ਤਾਂ URLs ਨੂੰ ਦੁਬਾਰਾ ਚੈੱਕ ਕਰੋ। APIM ਇਨ੍ਹਾਂ ਮੁੱਲਾਂ ਨੂੰ ਜਿਵੇਂ ਹਨ ਵਰਤੇਗਾ। 

- **ਪਾਲੀਸੀ ਕ੍ਰਮ:** APIM ਪਾਲੀਸੀ ਵਿੱਚ, `<validate-jwt>` ਨੂੰ ਬੈਕਐਂਡ ਤੱਕ ਕਿਸੇ ਵੀ ਰੂਟਿੰਗ ਤੋਂ **ਪਹਿਲਾਂ** ਰੱਖੋ। ਨਹੀਂ ਤਾਂ ਬੇਨਤੀਆਂ ਤੁਹਾਡੇ ਐਪ ਤੱਕ ਬਿਨਾਂ ਵੈਧ ਟੋਕਨ ਦੇ ਪਹੁੰਚ ਸਕਦੀਆਂ ਹਨ। ਇਹ ਵੀ ਯਕੀਨੀ ਬਣਾਓ ਕਿ `<validate-jwt>` `<inbound>` ਦੇ ਤਾਹਤ ਤੁਰੰਤ ਦਿੱਖਾਈ ਦੇ ਰਿਹਾ ਹੋਵੇ (ਕਿਸੇ ਹੋਰ ਸ਼ਰਤ ਵਿੱਚ ਲੁਕਿਆ ਨਾ ਹੋਵੇ) ਤਾਂ ਜੋ APIM ਇਸ ਨੂੰ ਲਾਗੂ ਕਰ ਸਕੇ।

ਉਪਰੋਕਤ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ, ਤੁਸੀਂ ਆਪਣੇ Spring AI MCP ਸਰਵਰ ਨੂੰ Azure Container Apps ਵਿੱਚ ਚਲਾ ਸਕਦੇ ਹੋ ਅਤੇ Azure API ਪ੍ਰਬੰਧਨ ਨੂੰ ਆਉਣ ਵਾਲੇ OAuth2 JWTs ਦੀ ਘੱਟੋ-ਘੱਟ ਪਾਲੀਸੀ ਨਾਲ ਜਾਂਚ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾ ਸਕਦੇ ਹੋ। ਮੁੱਖ ਬਿੰਦੂ ਹਨ: ਸਪਰਿੰਗ ਔਥ ਐਂਡਪੌਇੰਟ ਨੂੰ TLS ਨਾਲ ਜਨਤਕ ਤੌਰ 'ਤੇ ਖੋਲ੍ਹੋ, OIDC ਖੋਜ ਸਰਗਰਮ ਕਰੋ, ਅਤੇ APIM ਦੇ `validate-jwt` ਨੂੰ OpenID ਕਨਫਿਗਰੇਸ਼ਨ URL 'ਤੇ ਇਸ਼ਾਰਾ ਕਰੋ (ਤਾਂ ਜੋ ਇਹ JWKS ਆਪਣੇ ਆਪ ਪ੍ਰਾਪਤ ਕਰ ਸਕੇ)। ਇਹ ਸੈੱਟਅੱਪ ਵਿਕਾਸ/ਟੈਸਟ ਵਾਤਾਵਰਨ ਲਈ مناسب ਹੈ; ਉਤਪਾਦਨ ਲਈ, ਸਹੀ ਸੁਰੱਖਿਅਤ ਪ੍ਰਬੰਧਨ, ਟੋਕਨ ਦੀ ਉਮਰ ਅਤੇ JWKS ਵਿੱਚ ਕੁੰਜੀਆਂ ਨੂੰ ਘੁਮਾਉਣ ਬਾਰੇ ਸੋਚੋ।


**ਸੰਦ:** ਡੀਫਾਲਟ ਐਂਡਪੋਇੰਟਾਂ ਲਈ Spring Authorization Server ਦਸਤਾਵੇਜ਼ ਵੇਖੋ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ਅਤੇ OIDC ਸੰਰਚਨਾ ਲਈ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` ਉਦਾਹਰਨਾਂ ਲਈ Microsoft APIM ਦਸਤਾਵੇਜ਼ ਵੇਖੋ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ ਅਤੇ ਸਰਟੀਫਿਕੇਟਾਂ ਲਈ Azure Container Apps ਦਸਤਾਵੇਜ਼ ਵੇਖੋ ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->