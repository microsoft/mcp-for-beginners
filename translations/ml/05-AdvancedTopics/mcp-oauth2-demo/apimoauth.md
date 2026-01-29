# Spring AI MCP ആപ്പ് Azure Container Apps-ലേക്ക് ഡിപ്ലോയ് ചെയ്യൽ

 ([OAuth2 ഉപയോഗിച്ച് Spring AI MCP സെർവറുകൾ സുരക്ഷിതമാക്കൽ](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *ചിത്രം: Spring Authorization Server ഉപയോഗിച്ച് സുരക്ഷിതമാക്കിയ Spring AI MCP സെർവർ. സെർവർ ക്ലയന്റുകൾക്ക് ആക്സസ് ടോക്കണുകൾ നൽകുകയും വരവു അഭ്യർത്ഥനകളിൽ അവ പരിശോധിക്കുകയും ചെയ്യുന്നു (മൂലം: Spring ബ്ലോഗ്) ([OAuth2 ഉപയോഗിച്ച് Spring AI MCP സെർവറുകൾ സുരക്ഷിതമാക്കൽ](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP സെർവർ ഡിപ്ലോയ് ചെയ്യാൻ, അത് ഒരു കണ്ടെയ്‌നറായി നിർമ്മിച്ച് Azure Container Apps-ൽ external ingress ഉപയോഗിച്ച് പ്രവർത്തിപ്പിക്കുക. ഉദാഹരണത്തിന്, Azure CLI ഉപയോഗിച്ച് നിങ്ങൾക്ക് താഴെപറയുന്ന കമാൻഡ് ഓടിക്കാം:

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

ഇത് HTTPS സജ്ജമാക്കിയ പൊതു ആക്സസ് ലഭ്യമാകുന്ന Container App സൃഷ്ടിക്കുന്നു (Azure ഡിഫോൾട്ട് `*.azurecontainerapps.io` ഡൊമെയ്‌നിനായി സൗജന്യ TLS സർട്ടിഫിക്കറ്റ് നൽകുന്നു ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). കമാൻഡ് ഔട്ട്പുട്ടിൽ ആപ്പിന്റെ FQDN (ഉദാ. `my-mcp-app.eastus.azurecontainerapps.io`) ഉൾപ്പെടുന്നു, ഇത് **issuer URL** ബേസ് ആകുന്നു. APIM ആപ്പിൽ എത്താൻ HTTP ingress സജ്ജമാക്കിയിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക (മുകളിൽ കാണിച്ചതുപോലെ). ടെസ്റ്റ്/ഡെവ് സെറ്റപ്പിൽ `--ingress external` ഓപ്ഷൻ ഉപയോഗിക്കുക (അല്ലെങ്കിൽ TLS ഉപയോഗിച്ച് കസ്റ്റം ഡൊമെയ്ൻ ബൈൻഡ് ചെയ്യുക [Microsoft ഡോക്സ്](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). OAuth ക്ലയന്റ് സീക്രറ്റുകൾ പോലുള്ള സენსിറ്റീവ് പ്രോപ്പർട്ടികൾ Container Apps secrets അല്ലെങ്കിൽ Azure Key Vault-ൽ സൂക്ഷിച്ച്, അവ കണ്ടെയ്‌നറിലേക്ക് എൻവയോൺമെന്റ് വേരിയബിളുകളായി മാപ്പ് ചെയ്യുക.

## Spring Authorization Server കോൺഫിഗർ ചെയ്യൽ

നിങ്ങളുടെ Spring Boot ആപ്പിന്റെ കോഡിൽ Spring Authorization Server, Resource Server സ്റ്റാർട്ടറുകൾ ഉൾപ്പെടുത്തുക. `RegisteredClient` (dev/test-ൽ `client_credentials` ഗ്രാന്റിനായി) ഒപ്പം JWT കീ സോഴ്‌സ് കോൺഫിഗർ ചെയ്യുക. ഉദാഹരണത്തിന്, `application.properties`-ൽ നിങ്ങൾക്ക് ഇങ്ങനെ സജ്ജമാക്കാം:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server, Resource Server സജ്ജമാക്കാൻ സെക്യൂരിറ്റി ഫിൽട്ടർ ചെയിൻ നിർവചിക്കുക. ഉദാഹരണത്തിന്:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // അഥോറൈസേഷൻ സർവർ എൻഡ്‌പോയിന്റുകൾ സജീവമാക്കുക
            .apply(authzServer.and())
            // റിസോഴ്‌സ് സർവർ സജീവമാക്കുക (വരുന്ന അഭ്യർത്ഥനകളിൽ JWT സാധുത പരിശോധിക്കുക)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF അപ്രാപ്തമാക്കുക (MCP സർവർ ബ്രൗസർ അടിസ്ഥാനമല്ല)
            .csrf(csrf -> csrf.disable())
            // ക്ലയന്റ് ഡെമോ ടൂളുകൾക്ക് CORS അനുവദിക്കുക
            .cors(withDefaults());
        return http.build();
    }

    // ഒരു ഇൻ-മെമ്മറി ക്ലയന്റ് (RegisteredClient)യും JWK സ്രോതസ്സും നിർവചിക്കുക:
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
        // RSA കീ ജനറേറ്റ് ചെയ്യുക (ഡെവ്/ടെസ്റ്റ് വേണ്ടി, സ്റ്റാർട്ടപ്പിൽ പുതുതായി ജനറേറ്റ് ചെയ്യുക)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ഈ സജ്ജീകരണം ഡിഫോൾട്ട് OAuth2 എൻഡ്‌പോയിന്റുകൾ തുറക്കും: ടോക്കണുകൾക്കായി `/oauth2/token` ഒപ്പം JSON Web Key Set-ക്കായി `/oauth2/jwks`. (ഡിഫോൾട്ട് ആയി Spring-ന്റെ `AuthorizationServerSettings` `/oauth2/token` ഒപ്പം `/oauth2/jwks` മാപ്പ് ചെയ്യുന്നു ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) സെർവർ RSA കീ ഉപയോഗിച്ച് ഒപ്പിട്ട JWT ആക്സസ് ടോക്കണുകൾ നൽകുകയും, പൊതു കീ `https://<your-app>:/oauth2/jwks`-ൽ പ്രസിദ്ധീകരിക്കുകയും ചെയ്യും.

**OpenID Connect ഡിസ്കവറി സജ്ജമാക്കുക:** APIM ഓട്ടോമാറ്റിക്കായി issuer, JWKS ലഭിക്കാൻ OIDC പ്രൊവൈഡർ കോൺഫിഗറേഷൻ എൻഡ്‌പോയിന്റ് സജ്ജമാക്കാൻ `.oidc(Customizer.withDefaults())` നിങ്ങളുടെ സെക്യൂരിറ്റി കോൺഫിഗറേഷനിൽ ചേർക്കുക ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ഉദാഹരണത്തിന്:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration സജ്ജമാക്കുന്നു
```

ഇത് `/.well-known/openid-configuration` തുറക്കും, APIM മെടാഡേറ്റയ്ക്ക് ഇത് ഉപയോഗിക്കും. അവസാനം, APIM-ന്റെ `<audiences>` പരിശോധന പാസാകാൻ JWT **audience** ക്ലെയിം കസ്റ്റമൈസ് ചെയ്യാൻ നിങ്ങൾക്ക് ടോക്കൺ കസ്റ്റമൈസർ ചേർക്കാം:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // ഒരു കസ്റ്റം പ്രേക്ഷകസംഘം സജ്ജമാക്കുക (ഉദാ: ക്ലയന്റ് ഐഡി അല്ലെങ്കിൽ API തിരിച്ചറിയൽ)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

ഇത് ടോക്കണുകളിൽ `"aud": ["mcp-client"]` ഉൾപ്പെടുന്നതായി ഉറപ്പാക്കും, APIM പ്രതീക്ഷിക്കുന്ന ക്ലയന്റ് ഐഡി അല്ലെങ്കിൽ സ്കോപ്പുമായി പൊരുത്തപ്പെടുന്നു.

## ടോക്കൺ, JWKS എൻഡ്‌പോയിന്റുകൾ എക്സ്പോസ് ചെയ്യൽ

ഡിപ്ലോയ് ചെയ്ത ശേഷം, നിങ്ങളുടെ ആപ്പിന്റെ **issuer URL** ആയിരിക്കും `https://<app-fqdn>`, ഉദാ. `https://my-mcp-app.eastus.azurecontainerapps.io`. അതിന്റെ OAuth2 എൻഡ്‌പോയിന്റുകൾ:

- **ടോക്കൺ എൻഡ്‌പോയിന്റ്:** `https://<app-fqdn>/oauth2/token` – ക്ലയന്റുകൾ ഇവിടെ ടോക്കണുകൾ നേടും (client_credentials ഫ്ലോ).
- **JWKS എൻഡ്‌പോയിന്റ്:** `https://<app-fqdn>/oauth2/jwks` – JWK സെറ്റ് നൽകുന്നു (APIM സൈൻ ചെയ്യാനുള്ള കീകൾ നേടാൻ ഉപയോഗിക്കുന്നു).
- **OpenID കോൺഫിഗ്:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC ഡിസ്കവറി JSON (ഇതിൽ `issuer`, `token_endpoint`, `jwks_uri` തുടങ്ങിയവ അടങ്ങിയിരിക്കുന്നു).

APIM **OpenID കോൺഫിഗറേഷൻ URL**-നെ സൂചിപ്പിക്കും, അതിൽ നിന്ന് `jwks_uri` കണ്ടെത്തും. ഉദാഹരണത്തിന്, നിങ്ങളുടെ Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` ആണെങ്കിൽ, APIM-ന്റെ `<openid-config url="...">` ഇങ്ങനെ ആയിരിക്കണം: `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (ഡിഫോൾട്ട് ആയി Spring ആ മെടാഡേറ്റയിൽ `issuer`-നെ ആ ബേസ് URL ആയി സജ്ജമാക്കും ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) കോൺഫിഗർ ചെയ്യൽ

Azure APIM-ൽ, `<validate-jwt>` പോളിസി ഉപയോഗിച്ച് വരവു JWT-കൾ നിങ്ങളുടെ Spring Authorization Server-നോട് പരിശോധിക്കുന്ന ഇൻബൗണ്ട് പോളിസി ചേർക്കുക. ലളിതമായ സെറ്റപ്പിനായി OpenID Connect മെടാഡേറ്റ URL ഉപയോഗിക്കാം. ഉദാഹരണ പോളിസി സ്നിപ്പെറ്റ്:

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

ഈ പോളിസി APIM-നെ Spring Auth Server-ൽ നിന്നുള്ള OpenID കോൺഫിഗറേഷൻ ഫെച്ച് ചെയ്യാൻ, അതിന്റെ JWKS ലഭിക്കാൻ, ഓരോ ടോക്കണും വിശ്വസനീയമായ കീ ഉപയോഗിച്ച് ഒപ്പിട്ടതാണെന്ന് പരിശോധിക്കാൻ നിർദ്ദേശിക്കുന്നു. `<issuers>` ഒഴിവാക്കിയാൽ APIM മെടാഡേറ്റയിൽ നിന്നുള്ള `issuer` ക്ലെയിം സ്വയം ഉപയോഗിക്കും. `<audience>` ടോക്കണിലെ ക്ലയന്റ് ഐഡി അല്ലെങ്കിൽ API റിസോഴ്‌സ് ഐഡന്റിഫയർ (മുകളിൽ ഉദാഹരണത്തിൽ `"mcp-client"`) ഒത്തിരിക്കണം. ഇത് Microsoft-ന്റെ `validate-jwt`-ഉം `<openid-config>`-ഉം ഉപയോഗിക്കുന്ന ഡോക്യുമെന്റേഷനുമായി പൊരുത്തപ്പെടുന്നു ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

വാലിഡേഷൻ കഴിഞ്ഞ്, APIM അഭ്യർത്ഥന (മൂല `Authorization` ഹെഡർ ഉൾപ്പെടെ) ബാക്ക്‌എൻഡിലേക്ക് ഫോർവേഡ് ചെയ്യും. Spring ആപ്പ് ഒരു റിസോഴ്‌സ് സെർവറായതിനാൽ ടോക്കൺ വീണ്ടും പരിശോധിക്കും, പക്ഷേ APIM ഇതിനകം അതിന്റെ സാധുത ഉറപ്പാക്കിയിട്ടുണ്ട്. (ഡെവലപ്മെന്റിനായി APIM-ന്റെ പരിശോധനയിൽ ആശ്രയിച്ച് ആപ്പിലെ അധിക പരിശോധനകൾ അപ്രാപ്തമാക്കാം, പക്ഷേ ഇരുവരും നിലനിർത്തുന്നത് സുരക്ഷിതമാണ്.)

## ഉദാഹരണ സെറ്റിംഗുകൾ

| സെറ്റിംഗ്            | ഉദാഹരണ മൂല്യം                                                        | കുറിപ്പുകൾ                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | നിങ്ങളുടെ Container App-ന്റെ URL (ബേസ് URI)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | ഡിഫോൾട്ട് Spring ടോക്കൺ എൻഡ്‌പോയിന്റ് ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | ഡിഫോൾട്ട് JWK സെറ്റ് എൻഡ്‌പോയിന്റ് ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC ഡിസ്കവറി ഡോക്യുമെന്റ് (സ്വയം സൃഷ്ടിക്കപ്പെട്ടത്)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth ക്ലയന്റ് ഐഡി അല്ലെങ്കിൽ API റിസോഴ്‌സ് പേര്       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ഈ URL ഉപയോഗിക്കുന്നു ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## സാധാരണ പിഴവുകൾ

- **HTTPS/TLS:** APIM ഗേറ്റ്വേ OpenID/JWKS എൻഡ്‌പോയിന്റ് HTTPS ആയിരിക്കണം, സാധുവായ സർട്ടിഫിക്കറ്റ് ഉണ്ടായിരിക്കണം. ഡിഫോൾട്ട് ആയി Azure Container Apps Azure-നിർവഹിക്കുന്ന ഡൊമെയ്‌നിനായി വിശ്വസനീയമായ TLS സർട്ടിഫിക്കറ്റ് നൽകുന്നു ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). കസ്റ്റം ഡൊമെയ്ൻ ഉപയോഗിക്കുന്നുവെങ്കിൽ സർട്ടിഫിക്കറ്റ് ബൈൻഡ് ചെയ്യുക (Azure-യുടെ സൗജന്യ മാനേജ്ഡ് സർട്ടിഫിക്കറ്റ് ഫീച്ചർ ഉപയോഗിക്കാം) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM സർട്ടിഫിക്കറ്റ് വിശ്വസിക്കാതെപോകുകയാണെങ്കിൽ `<validate-jwt>` മെടാഡേറ്റ ഫെച്ച് ചെയ്യാൻ പരാജയപ്പെടും.

- **എൻഡ്‌പോയിന്റ് ആക്സസിബിലിറ്റി:** Spring ആപ്പിന്റെ എൻഡ്‌പോയിന്റുകൾ APIM-നിന്ന് എത്താൻ കഴിയണം. `--ingress external` (അല്ലെങ്കിൽ പോർട്ടലിൽ ഇൻഗ്രസ് സജ്ജമാക്കൽ) ഏറ്റവും ലളിതമാണ്. നിങ്ങൾ ഇന്റേണൽ അല്ലെങ്കിൽ vNet-ബൗണ്ട് എൻവയോൺമെന്റ് തിരഞ്ഞെടുക്കുകയാണെങ്കിൽ, APIM (ഡിഫോൾട്ട് പൊതു) അതിൽ എത്താൻ കഴിയില്ല, ഒരേ VNet-ൽ വെച്ചിരിക്കണം. ടെസ്റ്റ് സെറ്റപ്പിൽ പൊതു ഇൻഗ്രസ് ഉപയോഗിക്കുക, APIM `.well-known` ഒപ്പം `/jwks` URL-കൾക്ക് വിളിക്കാനാകും.

- **OpenID ഡിസ്കവറി സജ്ജമാക്കൽ:** ഡിഫോൾട്ട് ആയി Spring Authorization Server `/.well-known/openid-configuration` തുറക്കില്ല, OIDC സജ്ജമാക്കിയിട്ടില്ലെങ്കിൽ. `.oidc(Customizer.withDefaults())` നിങ്ങളുടെ സെക്യൂരിറ്റി കോൺഫിഗറേഷനിൽ ഉൾപ്പെടുത്തുക (മുകളിൽ കാണിച്ചിരിക്കുന്നു) പ്രൊവൈഡർ കോൺഫിഗറേഷൻ എൻഡ്‌പോയിന്റ് സജീവമാക്കാൻ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). അല്ലെങ്കിൽ APIM-ന്റെ `<openid-config>` വിളി 404 നൽകും.

- **Audience ക്ലെയിം:** Spring ഡിഫോൾട്ട് പെരുമാറ്റം `aud` ക്ലെയിം ക്ലയന്റ് ഐഡിയായി സജ്ജമാക്കുക ആണ്. APIM-ന്റെ `<audience>` പരിശോധന പരാജയപ്പെട്ടാൽ, ടോക്കൺ കസ്റ്റമൈസ് ചെയ്യേണ്ടതുണ്ടാകും (മുകളിൽ കാണിച്ചിരിക്കുന്നു) അല്ലെങ്കിൽ APIM പോളിസി ക്രമീകരിക്കുക. JWT-യിലെ audience `<audience>`-ൽ സജ്ജമാക്കിയതുമായി പൊരുത്തപ്പെടണം.

- **JSON മെടാഡേറ്റ പാഴ്സിംഗ്:** OpenID കോൺഫിഗറേഷൻ JSON സാധുവായിരിക്കണം. Spring ഡിഫോൾട്ട് കോൺഫിഗറേഷൻ സാധാരണ OIDC മെടാഡേറ്റ ഡോക്യുമെന്റ് പുറപ്പെടുവിക്കും. ശരിയായ `issuer` ഒപ്പം `jwks_uri` ഉള്ളതായി ഉറപ്പാക്കുക. Spring പ്രോക്സി അല്ലെങ്കിൽ പാത്ത്-ബേസ് റൂട്ടിനുശേഷം ഹോസ്റ്റ് ചെയ്താൽ, ഈ മെടാഡേറ്റയിലെ URL-കൾ രണ്ടാമതും പരിശോധിക്കുക. APIM ഈ മൂല്യങ്ങൾ 그대로 ഉപയോഗിക്കും.

- **പോളിസി ഓർഡറിംഗ്:** APIM പോളിസിയിൽ `<validate-jwt>` ബാക്ക്‌എൻഡിലേക്ക് റൂട്ടിംഗ് ചെയ്യുന്നതിന് മുമ്പ് വയ്ക്കുക. അല്ലെങ്കിൽ, ടോക്കൺ ഇല്ലാതെ ആപ്പിലേക്ക് വിളികൾ എത്താം. കൂടാതെ `<validate-jwt>` `<inbound>`-ന്റെ ഉടൻ കീഴിൽ (മറ്റൊരു കണ്ടീഷനിൽ അല്ല) വരണം, APIM അത് പ്രയോഗിക്കാനായി.

മുകളിൽ പറഞ്ഞ ഘട്ടങ്ങൾ പാലിച്ചാൽ, നിങ്ങൾക്ക് Spring AI MCP സെർവർ Azure Container Apps-ൽ ഓടിക്കാനും Azure API Management വരവു OAuth2 JWT-കൾ കുറഞ്ഞ പോളിസി ഉപയോഗിച്ച് പരിശോധിക്കാനും കഴിയും. പ്രധാന കാര്യങ്ങൾ: Spring Auth എൻഡ്‌പോയിന്റുകൾ TLS-ഉം പൊതു ആക്സസും ഉള്ളതായി എക്സ്പോസ് ചെയ്യുക, OIDC ഡിസ്കവറി സജ്ജമാക്കുക, APIM-ന്റെ `validate-jwt` OpenID കോൺഫിഗ് URL-നു സൂചിപ്പിക്കുക (JWKS സ്വയം ഫെച്ച് ചെയ്യാൻ). ഇത് ഡെവ്/ടെസ്റ്റ് പരിസ്ഥിതിക്ക് അനുയോജ്യമാണ്; പ്രൊഡക്ഷനിൽ ശരിയായ സീക്രട്ട് മാനേജ്മെന്റ്, ടോക്കൺ കാലാവധി, JWKS കീകൾ റൊട്ടേറ്റ് ചെയ്യൽ എന്നിവ പരിഗണിക്കുക.
**റഫറൻസുകൾ:** ഡിഫോൾട്ട് എൻഡ്‌പോയിന്റുകൾക്കായി Spring Authorization Server ഡോക്യുമെന്റേഷൻ കാണുക ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) കൂടാതെ OIDC കോൺഫിഗറേഷൻ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` ഉദാഹരണങ്ങൾക്ക് Microsoft APIM ഡോക്യുമെന്റേഷൻ കാണുക ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ഡിപ്ലോയ്മെന്റിനും സർട്ടിഫിക്കറ്റുകൾക്കും Azure Container Apps ഡോക്യുമെന്റേഷൻ കാണുക ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->