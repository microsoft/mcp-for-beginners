# How to Deploy Spring AI MCP App for Azure Container Apps

([How to Secure Spring AI MCP servers wit OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figure: Spring AI MCP server wey secure wit Spring Authorization Server. Di server dey issue access tokens to clients and dey validate dem wen request dey come (source: Spring blog) ([How to Secure Spring AI MCP servers wit OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* To deploy di Spring MCP server, you go build am as container and use Azure Container Apps wit external ingress. Example, if you use Azure CLI, you fit run:

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

Dis one go create Container App wey people fit access publicly wit HTTPS enabled (Azure go give free TLS certificate for di default `*.azurecontainerapps.io` domain ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Di command output go show di app FQDN (e.g. `my-mcp-app.eastus.azurecontainerapps.io`), wey go be di **issuer URL** base. Make sure say HTTP ingress dey enabled (like di example above) so APIM fit reach di app. For test/dev setup, use di `--ingress external` option (or bind custom domain wit TLS as Microsoft docs talk [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Keep any sensitive properties (like OAuth client secrets) for Container Apps secrets or Azure Key Vault, and map dem into di container as environment variables.

## How to Configure Spring Authorization Server

For your Spring Boot app code, add di Spring Authorization Server and Resource Server starters. Configure one `RegisteredClient` (for di `client_credentials` grant for dev/test) and one JWT key source. Example, for `application.properties` you fit set:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Enable di Authorization Server and Resource Server by defining one security filter chain. Example:

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

Dis setup go expose di default OAuth2 endpoints: `/oauth2/token` for tokens and `/oauth2/jwks` for di JSON Web Key Set. (By default Spring `AuthorizationServerSettings` dey map `/oauth2/token` and `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Di server go dey issue JWT access tokens wey RSA key sign, and go publish di public key for `https://<your-app>:/oauth2/jwks`.

**Enable OpenID Connect discovery:** To make APIM fit automatically collect di issuer and JWKS, enable di OIDC provider configuration endpoint by adding `.oidc(Customizer.withDefaults())` for your security configuration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Example:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Dis one go expose `/.well-known/openid-configuration`, wey APIM fit use for metadata. Finally, you fit wan customize di JWT **audience** claim so APIM `<audiences>` check go pass. Example, add token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Dis one go make sure say tokens carry `"aud": ["mcp-client"]`, wey match di client ID or scope wey APIM dey expect.

## How to Expose Token and JWKS Endpoints

After you don deploy, di app **issuer URL** go be `https://<app-fqdn>`, e.g. `https://my-mcp-app.eastus.azurecontainerapps.io`. Di OAuth2 endpoints na:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – clients dey collect tokens here (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – dey return di JWK set (APIM dey use am to collect signing keys).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (e dey contain `issuer`, `token_endpoint`, `jwks_uri`, etc.).

APIM go dey point to di **OpenID configuration URL**, wey e go use collect di `jwks_uri`. Example, if your Container App FQDN na `my-mcp-app.eastus.azurecontainerapps.io`, APIM `<openid-config url="...">` go use `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (By default Spring go set di `issuer` for dat metadata to di same base URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## How to Configure Azure API Management (`validate-jwt`)

For Azure APIM, add one inbound policy wey dey use `<validate-jwt>` policy to check di JWTs wey dey come from your Spring Authorization Server. For simple setup, you fit use di OpenID Connect metadata URL. Example policy snippet:

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

Dis policy dey tell APIM to collect di OpenID configuration from Spring Auth Server, collect di JWKS, and validate say each token dey signed by trusted key and get di correct audience. (If you no put `<issuers>`, APIM go use di `issuer` claim from di metadata automatically.) Di `<audience>` suppose match your client ID or API resource identifier for di token (for di example above, we set am to `"mcp-client"`). Dis one dey consistent wit Microsoft documentation on how to use `validate-jwt` wit `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

After validation, APIM go forward di request (including di original `Authorization` header) to di backend. Since di Spring app na resource server too, e go re-validate di token, but APIM don already confirm say e valid. (For development, you fit rely on APIM check and disable extra checks for di app if you wan, but e better to keep both.)

## Example Settings

| Setting            | Example Value                                                        | Notes                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | Di Container App URL (base URI)            |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Default Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Default JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery document (auto-generated)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID or API resource name       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` dey use dis URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Common Mistakes

- **HTTPS/TLS:** Di APIM gateway dey require say di OpenID/JWKS endpoint go be HTTPS wit valid certificate. By default, Azure Container Apps dey provide trusted TLS cert for di Azure-managed domain ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). If you dey use custom domain, make sure say you bind certificate (you fit use Azure free managed cert feature) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). If APIM no fit trust di endpoint certificate, `<validate-jwt>` go fail to collect di metadata.

- **Endpoint Accessibility:** Make sure say di Spring app endpoints dey reachable from APIM. Using `--ingress external` (or enabling ingress for di portal) na di simplest. If you choose internal or vNet-bound environment, APIM (wey by default dey public) fit no reach am unless e dey di same VNet. For test setup, e better make ingress public so APIM fit call di `.well-known` and `/jwks` URLs.

- **OpenID Discovery Enabled:** By default, Spring Authorization Server **no dey expose** di `/.well-known/openid-configuration` unless OIDC dey enabled. Make sure say you include `.oidc(Customizer.withDefaults())` for your security config (check di example above) so di provider configuration endpoint go dey active ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). If not, APIM `<openid-config>` call go return 404.

- **Audience Claim:** Di default behavior for Spring na to set di `aud` claim to di client ID. If APIM `<audience>` check fail, you fit need customize di token (like di example above) or adjust di APIM policy. Make sure say di audience for your JWT match wetin you configure for `<audience>`.

- **JSON Metadata Parsing:** Di OpenID configuration JSON suppose dey valid. Di default config for Spring go emit standard OIDC metadata document. Check say e dey contain di correct `issuer` and `jwks_uri`. If you dey host Spring behind proxy or path-based route, double-check di URLs for dis metadata. APIM go use di values as e dey.

- **Policy Ordering:** For di APIM policy, put `<validate-jwt>` **before** any routing to di backend. If not, calls fit reach your app without valid token. Also make sure say `<validate-jwt>` dey immediately under `<inbound>` (no put am inside another condition) so APIM go apply am.

If you follow di steps wey dey above, you fit run your Spring AI MCP server for Azure Container Apps and make Azure API Management dey validate di OAuth2 JWTs wey dey come wit simple policy. Di main points na: expose di Spring Auth endpoints publicly wit TLS, enable OIDC discovery, and point APIM `validate-jwt` to di OpenID config URL (so e fit collect di JWKS automatically). Dis setup dey good for dev/test environment; for production, make sure say you manage secrets well, set token lifetimes, and dey rotate keys for JWKS as e dey needed.
**References:** Check Spring Authorization Server docs for di default endpoints ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) and OIDC configuration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); check Microsoft APIM docs for `validate-jwt` examples ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); and Azure Container Apps docs for deployment and certificates ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for di native language na di main source wey you go trust. For important mata, na beta make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->