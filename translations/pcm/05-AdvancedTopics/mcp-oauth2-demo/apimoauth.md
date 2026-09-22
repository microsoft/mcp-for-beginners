# Deploy di Spring AI MCP App to Azure Container Apps

> [!WARNING]
> Dis combined authorization/resource server na for learning and
> dev/test use. For production system, una suppose use dedicated identity provider,
> persistent signing keys, plus credentials wey dey stored for managed secret store.

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figure: Spring AI MCP server wey Spring Authorization Server don secure. Di server dey give clients access tokens and e dey check dem on incoming requests (source: Spring blog) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* To deploy di Spring MCP server, build am as container and use Azure Container Apps with external ingress. For example, if you dey use di Azure CLI, you fit run:

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

Dis one go create publicly-accessible Container App with HTTPS enabled (Azure dey provide free TLS certificate for di default `*.azurecontainerapps.io` domain ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Di command output go show di app’s FQDN (for example `my-mcp-app.eastus.azurecontainerapps.io`), wey go become di **issuer URL** base. Make sure say HTTP ingress dey enabled (just like di one wey dey up) so APIM fit reach di app. For test or dev setup, use di `--ingress external` option (or bind custom domain with TLS as per [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Put any sensitive settings (like OAuth client secrets) inside Container Apps secrets or Azure Key Vault, and map dem to di container as environment variables.

## Configuring Spring Authorization Server

For your Spring Boot app code, include di Spring Authorization Server and Resource Server starters. Configure one `RegisteredClient` (for di `client_credentials` grant wey dey for dev/test) plus one JWT key source. For example, inside `application.properties` you fit set:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Enable di Authorization Server and Resource Server by defining security filter chain. Example be this:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Make Authorization Server endpoints dey active
            .apply(authzServer.and())
            // Make Resource Server dey active (check JWT for incoming requests)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Turn off CSRF (MCP server no be browser-based)
            .csrf(csrf -> csrf.disable())
            // Allow CORS for client demo tools
            .cors(withDefaults());
        return http.build();
    }

    // Set up in-memory client (RegisteredClient) plus JWK source:
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
        // Generate RSA key (for dev/test, generate new one when e start)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Dis setup go expose di default OAuth2 endpoints: `/oauth2/token` for tokens and `/oauth2/jwks` for di JSON Web Key Set. (By default, Spring’s `AuthorizationServerSettings` dey map `/oauth2/token` and `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) Di server go issue JWT access tokens wey RSA key sign top, plus e go publish e public key for `https://<your-app>:/oauth2/jwks`.

**Enable OpenID Connect discovery:** To make APIM fit automatically get di issuer and JWKS, enable di OIDC provider configuration endpoint by adding `.oidc(Customizer.withDefaults())` for your security config ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Example:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– dey enable /.well-known/openid-configuration
```

Dis one expose `/.well-known/openid-configuration` wey APIM fit use for metadata. Last last, you fit wan customize di JWT **audience** claim so APIM’s `<audiences>` check go pass. Example, add token customizer:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set one custom audience (for example di client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Dis go make sure tokens carry `"aud": ["mcp-client"]`, wey match di client ID or scope wey APIM dey expect.

## Exposing Token and JWKS Endpoints

After you don deploy, your app’s **issuer URL** go be `https://<app-fqdn>`, for example `https://my-mcp-app.eastus.azurecontainerapps.io`. Di OAuth2 endpoints be:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – na here clients go get tokens (client_credentials flow).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – dis one go return di JWK set (APIM dey use am to get signing keys).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – na OIDC discovery JSON (e get `issuer`, `token_endpoint`, `jwks_uri`, etc.).

APIM go point to di **OpenID configuration URL**, where e go find di `jwks_uri`. For example, if your Container App FQDN na `my-mcp-app.eastus.azurecontainerapps.io`, then APIM’s `<openid-config url="...">` suppose be `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (By default Spring go set di `issuer` for di metadata to di same base URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configuring Azure API Management (`validate-jwt`)

For Azure APIM, add inbound policy wey go use `<validate-jwt>` policy to check JWTs wey dey come against your Spring Authorization Server. For simple setup, you fit use OpenID Connect metadata URL. Example policy snippet:

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

Dis policy dey tell APIM to fetch OpenID configuration from Spring Auth Server, carry di JWKS, and check say each token sign with trusted key and e get correct audience. (If you no put `<issuers>`, APIM go use di `issuer` claim from di metadata automatically.) Di `<audience>` suppose match your client ID or API resource identifier (for di example above, e dey set to `"mcp-client"`). Dis one make sense with Microsoft docs on using `validate-jwt` with `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

After validation, APIM go forward di request (including di original `Authorization` header) go backend. Since di Spring app still be resource server, e go check di token again, but APIM don already confirm say e valid. (For development, you fit rely on APIM check alone and turn off extra checks for app if you want, but e better make both dey run.)

## Example Settings

| Setting            | Example Value                                                        | Notes                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | Your Container App URL (base URI)          |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Default Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Default JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery document (auto-generated)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID or API resource name       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` dey use dis URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Common Pitfalls

- **HTTPS/TLS:** APIM gateway want make OpenID/JWKS endpoint get HTTPS wey get valid certificate. By default, Azure Container Apps dey provide trusted TLS cert for Azure-managed domain ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). If you dey use custom domain, make sure you bind certificate (you fit use Azure free managed cert) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). If APIM no fit trust di cert, `<validate-jwt>` no go fit fetch di metadata.

- **Endpoint Accessibility:** Make sure di Spring app endpoints dey reachable from APIM. Using `--ingress external` (or enable ingress for portal) na easiest way. If you choose internal or vNet-bound environment, APIM (wey by default na public) fit no reach am unless e dey the same VNet. For test setup, make public ingress make APIM fit call `.well-known` and `/jwks` URLs.

- **OpenID Discovery Enabled:** By default, Spring Authorization Server **no dey expose** `/.well-known/openid-configuration` unless OIDC dey enabled. Make sure say you add `.oidc(Customizer.withDefaults())` for your security config (see above) so di provider configuration endpoint go active ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Otherwise, APIM `<openid-config>` go call and e go show 404.

- **Audience Claim:** Spring default dey set `aud` claim to client ID. If APIM `<audience>` check no pass, you go need to customize token (like we show above) or change APIM policy. Make sure di audience for your JWT match di one you set for `<audience>`.

- **JSON Metadata Parsing:** OpenID config JSON must valid. Spring default config go emit standard OIDC metadata document. Confirm say e get correct `issuer` and `jwks_uri`. If you dey host Spring behind proxy or path-based route, double check URLs for dis metadata. APIM go use di values as dem be.

- **Policy Ordering:** For APIM policy, put `<validate-jwt>` **before** any routing go backend. If no, calls fit reach your app without valid token. Make sure `<validate-jwt>` dey right under `<inbound>` (no nest am inside another condition) so APIM go apply am well.

If you follow all dis steps, you fit run your Spring AI MCP server for Azure Container Apps and fit get Azure API Management to validate incoming OAuth2 JWTs with minimal policy. Di main tins na: expose Spring Auth endpoints publicly with TLS, enable OIDC discovery, and make APIM `validate-jwt` point to OpenID config URL (so e fit fetch JWKS automatically). Dis one good for dev/test environment; for production, make sure proper secret management, token lifetimes, and rotating keys for JWKS dey as e suppose be.


**References:** See Spring Authorization Server docs for default endpoints ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) and OIDC configuration ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); see Microsoft APIM docs for `validate-jwt` examples ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); and Azure Container Apps docs for deployment and certificates ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->