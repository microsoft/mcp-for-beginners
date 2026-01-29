# Spring AI MCP ਐਪ ਨੂੰ Azure Container Apps 'ਤੇ ਡਿਪਲੋਇ ਕਰਨਾ

([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *ਫਿਗਰ: Spring AI MCP ਸਰਵਰ ਨੂੰ Spring Authorization Server ਨਾਲ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ। ਸਰਵਰ ਕਲਾਇੰਟਾਂ ਨੂੰ ਐਕਸੈਸ ਟੋਕਨ ਜਾਰੀ ਕਰਦਾ ਹੈ ਅਤੇ ਆਉਣ ਵਾਲੀਆਂ ਬੇਨਤੀਆਂ 'ਤੇ ਉਹਨਾਂ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ (ਸਰੋਤ: Spring ਬਲੌਗ) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP ਸਰਵਰ ਨੂੰ ਡਿਪਲੋਇ ਕਰਨ ਲਈ, ਇਸਨੂੰ ਇੱਕ ਕੰਟੇਨਰ ਵਜੋਂ ਬਣਾਓ ਅਤੇ Azure Container Apps ਨਾਲ ਬਾਹਰੀ ਇੰਗ੍ਰੈੱਸ ਵਰਤੋਂ। ਉਦਾਹਰਨ ਵਜੋਂ, Azure CLI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤੁਸੀਂ ਚਲਾ ਸਕਦੇ ਹੋ:

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

ਇਹ ਇੱਕ ਪਬਲਿਕਲੀ-ਐਕਸੈਸਿਬਲ Container App ਬਣਾਉਂਦਾ ਹੈ ਜਿਸ ਵਿੱਚ HTTPS ਚਾਲੂ ਹੁੰਦਾ ਹੈ (Azure ਡਿਫਾਲਟ `*.azurecontainerapps.io` ਡੋਮੇਨ ਲਈ ਮੁਫ਼ਤ TLS ਸਰਟੀਫਿਕੇਟ ਜਾਰੀ ਕਰਦਾ ਹੈ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ਕਮਾਂਡ ਆਉਟਪੁੱਟ ਵਿੱਚ ਐਪ ਦਾ FQDN ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ (ਜਿਵੇਂ `my-mcp-app.eastus.azurecontainerapps.io`), ਜੋ ਕਿ **issuer URL** ਦਾ ਬੇਸ ਬਣ ਜਾਂਦਾ ਹੈ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ HTTP ਇੰਗ੍ਰੈੱਸ ਚਾਲੂ ਹੈ (ਜਿਵੇਂ ਉੱਪਰ ਦਿੱਤਾ ਗਿਆ) ਤਾਂ ਜੋ APIM ਐਪ ਤੱਕ ਪਹੁੰਚ ਸਕੇ। ਟੈਸਟ/ਡਿਵੈਲਪਮੈਂਟ ਸੈਟਅੱਪ ਵਿੱਚ, `--ingress external` ਵਿਕਲਪ ਵਰਤੋਂ (ਜਾਂ TLS ਨਾਲ ਕਸਟਮ ਡੋਮੇਨ ਬਾਈਂਡ ਕਰੋ [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ਕੋਈ ਵੀ ਸੰਵੇਦਨਸ਼ੀਲ ਪ੍ਰਾਪਰਟੀਜ਼ (ਜਿਵੇਂ OAuth ਕਲਾਇੰਟ ਸੀਕ੍ਰੇਟ) Container Apps secrets ਜਾਂ Azure Key Vault ਵਿੱਚ ਸਟੋਰ ਕਰੋ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਕੰਟੇਨਰ ਵਿੱਚ ਇਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲ ਵਜੋਂ ਮੈਪ ਕਰੋ।

## Spring Authorization Server ਦੀ ਸੰਰਚਨਾ

ਆਪਣੇ Spring Boot ਐਪ ਦੇ ਕੋਡ ਵਿੱਚ, Spring Authorization Server ਅਤੇ Resource Server starters ਸ਼ਾਮਲ ਕਰੋ। ਇੱਕ `RegisteredClient` (ਡਿਵ/ਟੈਸਟ ਵਿੱਚ `client_credentials` ਗ੍ਰਾਂਟ ਲਈ) ਅਤੇ JWT ਕੀ ਸੋਰਸ ਕਨਫਿਗਰ ਕਰੋ। ਉਦਾਹਰਨ ਵਜੋਂ, `application.properties` ਵਿੱਚ ਤੁਸੀਂ ਇਹ ਸੈਟ ਕਰ ਸਕਦੇ ਹੋ:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server ਅਤੇ Resource Server ਨੂੰ ਸੁਰੱਖਿਆ ਫਿਲਟਰ ਚੇਨ ਦੀ ਪਰਿਭਾਸ਼ਾ ਕਰਕੇ ਚਾਲੂ ਕਰੋ। ਉਦਾਹਰਨ ਵਜੋਂ:

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

ਇਹ ਸੈਟਅੱਪ ਡਿਫਾਲਟ OAuth2 ਐਂਡਪੌਇੰਟ ਖੋਲ੍ਹੇਗਾ: `/oauth2/token` ਟੋਕਨ ਲਈ ਅਤੇ `/oauth2/jwks` JSON Web Key Set ਲਈ। (ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ Spring ਦਾ `AuthorizationServerSettings` `/oauth2/token` ਅਤੇ `/oauth2/jwks` ਨੂੰ ਮੈਪ ਕਰਦਾ ਹੈ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) ਸਰਵਰ RSA ਕੀ ਨਾਲ ਸਾਈਨ ਕੀਤੇ JWT ਐਕਸੈਸ ਟੋਕਨ ਜਾਰੀ ਕਰੇਗਾ ਅਤੇ ਆਪਣੀ ਪਬਲਿਕ ਕੀ `https://<your-app>:/oauth2/jwks` 'ਤੇ ਪ੍ਰਕਾਸ਼ਿਤ ਕਰੇਗਾ।

**OpenID Connect ਡਿਸਕਵਰੀ ਚਾਲੂ ਕਰੋ:** APIM ਨੂੰ issuer ਅਤੇ JWKS ਆਪਣੇ ਆਪ ਪ੍ਰਾਪਤ ਕਰਨ ਦੇ ਲਈ, ਆਪਣੀ ਸੁਰੱਖਿਆ ਸੰਰਚਨਾ ਵਿੱਚ `.oidc(Customizer.withDefaults())` ਸ਼ਾਮਲ ਕਰੋ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ਉਦਾਹਰਨ ਵਜੋਂ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

ਇਹ `/.well-known/openid-configuration` ਨੂੰ ਖੋਲ੍ਹਦਾ ਹੈ, ਜਿਸਨੂੰ APIM ਮੈਟਾਡੇਟਾ ਲਈ ਵਰਤ ਸਕਦਾ ਹੈ। ਆਖ਼ਿਰ ਵਿੱਚ, ਤੁਸੀਂ JWT **audience** ਕਲੇਮ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰਨਾ ਚਾਹੋਗੇ ਤਾਂ ਜੋ APIM ਦਾ `<audiences>` ਚੈੱਕ ਪਾਸ ਹੋ ਜਾਵੇ। ਉਦਾਹਰਨ ਵਜੋਂ, ਇੱਕ ਟੋਕਨ ਕਸਟਮਾਈਜ਼ਰ ਸ਼ਾਮਲ ਕਰੋ:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

ਇਸ ਨਾਲ ਟੋਕਨਾਂ ਵਿੱਚ `"aud": ["mcp-client"]` ਸ਼ਾਮਲ ਹੋਵੇਗਾ, ਜੋ APIM ਵੱਲੋਂ ਉਮੀਦ ਕੀਤੇ ਗਏ ਕਲਾਇੰਟ ID ਜਾਂ ਸਕੋਪ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ।

## ਟੋਕਨ ਅਤੇ JWKS ਐਂਡਪੌਇੰਟ ਖੋਲ੍ਹਣਾ

ਡਿਪਲੋਇਮੈਂਟ ਤੋਂ ਬਾਅਦ, ਤੁਹਾਡੇ ਐਪ ਦਾ **issuer URL** `https://<app-fqdn>` ਹੋਵੇਗਾ, ਉਦਾਹਰਨ ਵਜੋਂ `https://my-mcp-app.eastus.azurecontainerapps.io`। ਇਸਦੇ OAuth2 ਐਂਡਪੌਇੰਟ ਹਨ:

- **ਟੋਕਨ ਐਂਡਪੌਇੰਟ:** `https://<app-fqdn>/oauth2/token` – ਕਲਾਇੰਟ ਇੱਥੋਂ ਟੋਕਨ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਨ (`client_credentials` ਫਲੋ)।
- **JWKS ਐਂਡਪੌਇੰਟ:** `https://<app-fqdn>/oauth2/jwks` – JWK ਸੈੱਟ ਵਾਪਸ ਕਰਦਾ ਹੈ (APIM ਸਾਈਨਿੰਗ ਕੀਜ਼ ਲਈ ਵਰਤਦਾ ਹੈ)।
- **OpenID ਕਨਫਿਗ:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC ਡਿਸਕਵਰੀ JSON (ਜਿਸ ਵਿੱਚ `issuer`, `token_endpoint`, `jwks_uri` ਆਦਿ ਹੁੰਦੇ ਹਨ)।

APIM **OpenID configuration URL** ਵੱਲ ਇਸ਼ਾਰਾ ਕਰੇਗਾ, ਜਿੱਥੋਂ ਇਹ `jwks_uri` ਨੂੰ ਖੋਜੇਗਾ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਹਾਡੇ Container App ਦਾ FQDN `my-mcp-app.eastus.azurecontainerapps.io` ਹੈ, ਤਾਂ APIM ਦਾ `<openid-config url="...">` ਇਸ ਤਰ੍ਹਾਂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ: `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`। (ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ Spring ਉਸ ਮੈਟਾਡੇਟਾ ਵਿੱਚ `issuer` ਨੂੰ ਇਸੇ ਬੇਸ URL ਤੇ ਸੈਟ ਕਰਦਾ ਹੈ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) ਦੀ ਸੰਰਚਨਾ

Azure APIM ਵਿੱਚ, ਇੱਕ inbound policy ਸ਼ਾਮਲ ਕਰੋ ਜੋ `<validate-jwt>` ਪਾਲਿਸੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤੁਹਾਡੇ Spring Authorization Server ਵੱਲੋਂ ਜਾਰੀ ਕੀਤੇ JWTs ਦੀ ਜਾਂਚ ਕਰੇ। ਸਧਾਰਣ ਸੈਟਅੱਪ ਲਈ, ਤੁਸੀਂ OpenID Connect ਮੈਟਾਡੇਟਾ URL ਵਰਤ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਪਾਲਿਸੀ ਸਨਿੱਪੇਟ:

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

ਇਹ ਪਾਲਿਸੀ APIM ਨੂੰ ਕਹਿੰਦੀ ਹੈ ਕਿ Spring Auth Server ਤੋਂ OpenID configuration ਲੈ ਕੇ, ਉਸਦੀ JWKS ਪ੍ਰਾਪਤ ਕਰੇ ਅਤੇ ਹਰ ਟੋਕਨ ਦੀ ਸਾਈਨਿੰਗ ਕੀ ਅਤੇ audience ਦੀ ਸਹੀਤਾ ਦੀ ਜਾਂਚ ਕਰੇ। (ਜੇ ਤੁਸੀਂ `<issuers>` ਨਹੀਂ ਦਿੰਦੇ, ਤਾਂ APIM ਮੈਟਾਡੇਟਾ ਵਿੱਚੋਂ `issuer` ਕਲੇਮ ਨੂੰ ਆਪਣੇ ਆਪ ਵਰਤੇਗਾ।) `<audience>` ਤੁਹਾਡੇ ਕਲਾਇੰਟ ID ਜਾਂ API ਰਿਸੋਰਸ ਆਈਡੈਂਟੀਫਾਇਰ ਨਾਲ ਮੇਲ ਖਾਣਾ ਚਾਹੀਦਾ ਹੈ (ਉਪਰ ਦਿੱਤੇ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ ਇਸਨੂੰ `"mcp-client"` ਸੈਟ ਕੀਤਾ ਹੈ)। ਇਹ Microsoft ਦੀ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਨਾਲ ਸੰਗਤ ਹੈ ਜੋ `<openid-config>` ਨਾਲ `validate-jwt` ਦੀ ਵਰਤੋਂ ਬਾਰੇ ਹੈ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))।

ਵੈਰੀਫਿਕੇਸ਼ਨ ਤੋਂ ਬਾਅਦ, APIM ਬੈਕਐਂਡ ਨੂੰ ਬੇਨਤੀ ਅੱਗੇ ਭੇਜੇਗਾ (ਮੂਲ `Authorization` ਹੈਡਰ ਸਮੇਤ)। ਕਿਉਂਕਿ Spring ਐਪ ਵੀ ਇੱਕ resource server ਹੈ, ਇਹ ਟੋਕਨ ਨੂੰ ਦੁਬਾਰਾ ਵੈਰੀਫਾਈ ਕਰੇਗਾ, ਪਰ APIM ਪਹਿਲਾਂ ਹੀ ਇਸਦੀ ਵੈਧਤਾ ਯਕੀਨੀ ਬਣਾ ਚੁੱਕਾ ਹੋਵੇਗਾ। (ਡਿਵੈਲਪਮੈਂਟ ਲਈ, ਤੁਸੀਂ APIM ਦੀ ਜਾਂਚ 'ਤੇ ਨਿਰਭਰ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਐਪ ਵਿੱਚ ਵਾਧੂ ਜਾਂਚਾਂ ਨੂੰ ਅਣਚਾਲੂ ਕਰ ਸਕਦੇ ਹੋ, ਪਰ ਦੋਹਾਂ ਨੂੰ ਚਾਲੂ ਰੱਖਣਾ ਜ਼ਿਆਦਾ ਸੁਰੱਖਿਅਤ ਹੈ।)

## ਉਦਾਹਰਨ ਸੈਟਿੰਗਜ਼

| ਸੈਟਿੰਗ            | ਉਦਾਹਰਨ ਮੁੱਲ                                                        | ਨੋਟਸ                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | ਤੁਹਾਡੇ Container App ਦਾ URL (ਬੇਸ URI)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | ਡਿਫਾਲਟ Spring ਟੋਕਨ ਐਂਡਪੌਇੰਟ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | ਡਿਫਾਲਟ JWK ਸੈੱਟ ਐਂਡਪੌਇੰਟ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC ਡਿਸਕਵਰੀ ਦਸਤਾਵੇਜ਼ (ਆਟੋ-ਜਨਰੇਟ ਕੀਤਾ)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth ਕਲਾਇੰਟ ID ਜਾਂ API ਰਿਸੋਰਸ ਨਾਮ       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ਇਸ URL ਨੂੰ ਵਰਤਦਾ ਹੈ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## ਆਮ ਗਲਤੀਆਂ

- **HTTPS/TLS:** APIM ਗੇਟਵੇ ਲਈ ਜ਼ਰੂਰੀ ਹੈ ਕਿ OpenID/JWKS ਐਂਡਪੌਇੰਟ HTTPS ਹੋਵੇ ਅਤੇ ਵੈਧ ਸਰਟੀਫਿਕੇਟ ਹੋਵੇ। ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ, Azure Container Apps Azure-ਮੈਨੇਜਡ ਡੋਮੇਨ ਲਈ ਭਰੋਸੇਯੋਗ TLS ਸਰਟੀਫਿਕੇਟ ਦਿੰਦਾ ਹੈ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). ਜੇ ਤੁਸੀਂ ਕਸਟਮ ਡੋਮੇਨ ਵਰਤਦੇ ਹੋ, ਤਾਂ ਸਰਟੀਫਿਕੇਟ ਬਾਈਂਡ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ (ਤੁਸੀਂ Azure ਦੀ ਮੁਫ਼ਤ ਮੈਨੇਜਡ ਸਰਟੀਫਿਕੇਟ ਫੀਚਰ ਵਰਤ ਸਕਦੇ ਹੋ) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). ਜੇ APIM ਐਂਡਪੌਇੰਟ ਦੇ ਸਰਟੀਫਿਕੇਟ 'ਤੇ ਭਰੋਸਾ ਨਹੀਂ ਕਰਦਾ, ਤਾਂ `<validate-jwt>` ਮੈਟਾਡੇਟਾ ਲੈਣ ਵਿੱਚ ਅਸਫਲ ਰਹੇਗਾ।

- **ਐਂਡਪੌਇੰਟ ਪਹੁੰਚਯੋਗਤਾ:** ਯਕੀਨੀ ਬਣਾਓ ਕਿ Spring ਐਪ ਦੇ ਐਂਡਪੌਇੰਟ APIM ਤੋਂ ਪਹੁੰਚਯੋਗ ਹਨ। `--ingress external` ਵਰਤਣਾ (ਜਾਂ ਪੋਰਟਲ ਵਿੱਚ ਇੰਗ੍ਰੈੱਸ ਚਾਲੂ ਕਰਨਾ) ਸਭ ਤੋਂ ਆਸਾਨ ਹੈ। ਜੇ ਤੁਸੀਂ ਇੰਟਰਨਲ ਜਾਂ vNet-ਬਾਊਂਡ ਵਾਤਾਵਰਣ ਚੁਣਿਆ ਹੈ, ਤਾਂ APIM (ਜੋ ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਪਬਲਿਕ ਹੈ) ਸ਼ਾਇਦ ਇਸ ਤੱਕ ਪਹੁੰਚ ਨਾ ਕਰ ਸਕੇ ਜੇ ਤੱਕ ਇਹ ਇੱਕੋ VNet ਵਿੱਚ ਨਾ ਹੋਵੇ। ਟੈਸਟ ਸੈਟਅੱਪ ਵਿੱਚ, ਪਬਲਿਕ ਇੰਗ੍ਰੈੱਸ ਨੂੰ ਤਰਜੀਹ ਦਿਓ ਤਾਂ ਜੋ APIM `.well-known` ਅਤੇ `/jwks` URLs ਨੂੰ ਕਾਲ ਕਰ ਸਕੇ।

- **OpenID ਡਿਸਕਵਰੀ ਚਾਲੂ ਹੈ:** ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ Spring Authorization Server `/.well-known/openid-configuration` ਨੂੰ **ਖੋਲ੍ਹਦਾ ਨਹੀਂ** ਜਦ ਤੱਕ OIDC ਚਾਲੂ ਨਾ ਹੋਵੇ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ `.oidc(Customizer.withDefaults())` ਤੁਹਾਡੇ ਸੁਰੱਖਿਆ ਸੰਰਚਨਾ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ (ਉਪਰ ਵੇਖੋ) ਤਾਂ ਜੋ ਪ੍ਰੋਵਾਈਡਰ ਕਨਫਿਗ ਐਂਡਪੌਇੰਟ ਸਰਗਰਮ ਹੋਵੇ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ਨਹੀਂ ਤਾਂ APIM ਦਾ `<openid-config>` ਕਾਲ 404 ਦੇਵੇਗਾ।

- **Audience ਕਲੇਮ:** Spring ਦਾ ਡਿਫਾਲਟ ਵਿਹਾਰ `aud` ਕਲੇਮ ਨੂੰ ਕਲਾਇੰਟ ID 'ਤੇ ਸੈਟ ਕਰਦਾ ਹੈ। ਜੇ APIM ਦਾ `<audience>` ਚੈੱਕ ਫੇਲ੍ਹ ਹੁੰਦਾ ਹੈ, ਤਾਂ ਤੁਹਾਨੂੰ ਟੋਕਨ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰਨ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ (ਜਿਵੇਂ ਉਪਰ ਦਿਖਾਇਆ ਗਿਆ) ਜਾਂ APIM ਪਾਲਿਸੀ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰਨਾ ਪਵੇ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ JWT ਵਿੱਚ audience ਤੁਹਾਡੇ `<audience>` ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ।

- **JSON ਮੈਟਾਡੇਟਾ ਪਾਰਸਿੰਗ:** OpenID configuration JSON ਵੈਧ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। Spring ਦਾ ਡਿਫਾਲਟ ਕਨਫਿਗ ਇੱਕ ਸਟੈਂਡਰਡ OIDC ਮੈਟਾਡੇਟਾ ਦਸਤਾਵੇਜ਼ ਜਾਰੀ ਕਰੇਗਾ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਸ ਵਿੱਚ ਸਹੀ `issuer` ਅਤੇ `jwks_uri` ਹਨ। ਜੇ ਤੁਸੀਂ Spring ਨੂੰ ਪ੍ਰਾਕਸੀ ਜਾਂ ਪਾਥ-ਆਧਾਰਿਤ ਰੂਟ ਦੇ ਪਿੱਛੇ ਹੋਸਟ ਕਰਦੇ ਹੋ, ਤਾਂ URLs ਨੂੰ ਦੁਬਾਰਾ ਚੈੱਕ ਕਰੋ। APIM ਇਨ੍ਹਾਂ ਮੁੱਲਾਂ ਨੂੰ ਬਿਨਾਂ ਬਦਲੇ ਵਰਤੇਗਾ।

- **ਪਾਲਿਸੀ ਕ੍ਰਮ:** APIM ਪਾਲਿਸੀ ਵਿੱਚ, `<validate-jwt>` ਨੂੰ ਬੈਕਐਂਡ ਰੂਟਿੰਗ ਤੋਂ **ਪਹਿਲਾਂ** ਰੱਖੋ। ਨਹੀਂ ਤਾਂ ਬੇਨਤੀਆਂ ਤੁਹਾਡੇ ਐਪ ਤੱਕ ਬਿਨਾਂ ਵੈਧ ਟੋਕਨ ਦੇ ਪਹੁੰਚ ਸਕਦੀਆਂ ਹਨ। ਇਹ ਵੀ ਯਕੀਨੀ ਬਣਾਓ ਕਿ `<validate-jwt>` ਸਿੱਧਾ `<inbound>` ਦੇ ਅੰਦਰ ਹੈ (ਕਿਸੇ ਹੋਰ ਸ਼ਰਤ ਦੇ ਅੰਦਰ ਨਹੀਂ) ਤਾਂ ਜੋ APIM ਇਸਨੂੰ ਲਾਗੂ ਕਰੇ।

ਉਪਰ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ, ਤੁਸੀਂ ਆਪਣੇ Spring AI MCP ਸਰਵਰ ਨੂੰ Azure Container Apps ਵਿੱਚ ਚਲਾ ਸਕਦੇ ਹੋ ਅਤੇ Azure API Management ਨੂੰ ਆਉਣ ਵਾਲੇ OAuth2 JWTs ਦੀ ਘੱਟੋ-ਘੱਟ ਪਾਲਿਸੀ ਨਾਲ ਵੈਰੀਫਾਈ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾ ਸਕਦੇ ਹੋ। ਮੁੱਖ ਗੱਲਾਂ ਹਨ: Spring Auth ਐਂਡਪੌਇੰਟਸ ਨੂੰ TLS ਨਾਲ ਪਬਲਿਕਲੀ ਖੋਲ੍ਹੋ, OIDC ਡਿਸਕਵਰੀ ਚਾਲੂ ਕਰੋ, ਅਤੇ APIM ਦੇ `validate-jwt` ਨੂੰ OpenID ਕਨਫਿਗ URL ਵ
**References:** ਡਿਫਾਲਟ ਐਂਡਪੌਇੰਟਸ ਲਈ Spring Authorization Server ਦੇ ਦਸਤਾਵੇਜ਼ ਵੇਖੋ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ਅਤੇ OIDC ਕਨਫਿਗਰੇਸ਼ਨ ਲਈ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); Microsoft APIM ਦੇ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ `validate-jwt` ਉਦਾਹਰਣਾਂ ਲਈ ਵੇਖੋ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ਅਤੇ Azure Container Apps ਦੇ ਦਸਤਾਵੇਜ਼ ਡਿਪਲੋਇਮੈਂਟ ਅਤੇ ਸਰਟੀਫਿਕੇਟਸ ਲਈ ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।