# Spring AI MCP ആപ്പ് Azure Container Apps-ലേക്ക് വിന്യസിക്കുക

> [!WARNING]
> ഈ സംയുക്ത അനുമതി/വിഭവ സെർവർ പഠനത്തിനും ഡെവ്/ടെസ്റ്റ് ഉപയോഗത്തിനും ഉദ്ദേശിച്ചാണ്. പ്രൊഡക്ഷൻ സിസ്റ്റങ്ങൾ സമർപ്പിത ഐഡന്റിറ്റി പ്രൊവൈഡർ, സ്ഥിരതയുള്ള സൈൻ ചെയിത ചാപുകള്‍, നു സംരക്ഷിത രഹസ്യ സ്റ്റോറിൽ സംഭരിയ്ക്കപ്പെട്ട ക്രെഡൻഷ്യലുകൾ ഉപയോഗിക്കണം.
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

ഇത് HTTPS സജ്ജീകരിച്ച പൊതുഗത ഗതാഗതം സൃഷ്ടിക്കുന്ന ഒരു കണ്ടെയ്‌നർ ആപ്പ് ഉണ്ടാക്കുന്നു (Azure സ്വതന്ത്ര TLS സർട്ടിഫിക്കറ്റ് നൽകുന്നു `*.azurecontainerapps.io` ഡൊമെയ്ൻ‌ക്കായി ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ആപ്പിന്റെ FQDN (ഉദാ: `my-mcp-app.eastus.azurecontainerapps.io`) കമാൻഡ് ഔട്ട്പുട്ടിൽ ഉൾപ്പെടുന്നു, അത് **issuer URL** ആധാരമാകും. HTTP നല്ലത് സാധ്യമാക്കിയിരിക്കണം (മുകളിൽ പറഞ്ഞതുപോലെ) APIM ആപ്പിലേക്ക് എത്താൻ. ടെസ്റ്റ്/ഡെവ് സെറ്റപ്പിൽ `--ingress external` ഓപ്ഷൻ ഉപയോഗിക്കുക (അല്ലെങ്കിൽ [Microsoft ഡോക്സ്](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) പ്രകാരം TLS ഉപയോഗിച്ച് കസ്റ്റം ഡൊമെയ്ൻ ബൈണ്ടും ചെയ്യുക). കോൺടെയ്‌നർ ആപ്പുകളുടെ രഹസ്യങ്ങളിൽ (ഒAuth ക്ലയന്റ് സീക്രറ്റുകൾ പോലുള്ള) എന്തെങ്കിലും حساس വിവരങ്ങൾ സൂക്ഷിക്കുക Azure Key Vault അല്ലെങ്കിൽ Container Apps Secrets-ൽ, അവയെ പ്ലാറ്റ്ഫോം പരിസ്ഥിതി ചാരങ്ങളിൽ മാപ്പ് ചെയ്യുക.

## Spring Authorization Server ക്രമീകരിക്കൽ

നിങ്ങളുടെ Spring Boot ആപ്പിൻ്റെ കോഡിൽ, Spring Authorization Server, Resource Server സ്റ്റാർട്ടറുകൾ ഉൾപ്പെടുത്തുക. ഒരു `RegisteredClient` (`client_credentials` ഗ്രാന്റ് ഡെവ്/ടെസ്റ്റ്-ലേക്ക്) ക്രമീകരിച്ച്, JWT കീ ഉറവിടം സജ്ജികരിക്കുക. ഉദാഹരണത്തിന്, `application.properties`-ൽ നിങ്ങൾ ഇങ്ങനെ ക്രമീകരിച്ചേക്കാം:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

സുരക്ഷാ ഫിൽട്ടർ ചെയിൻ നിർവ്വചിച്ച് Authorization Server, Resource Server സജ്ജമാക്കുക. ഉദാഹരണത്തിന്:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // അതോറൈസേഷൻ സെർവർ എൻഡ്‌പോയിന്റുകൾ അനുവദിക്കുക
            .apply(authzServer.and())
            // റിസോഴ്സ് സെർവർ സജീവമാക്കുക (ഉള്ളിലെ അഭ്യർത്ഥനകളിൽ JWT വാലിഡേറ്റ് ചെയ്യുക)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF നിഷ്ക്രിയമാക്കുക (MCP സർവർ ബ്രൗസർ അടിസ്ഥാനമാക്കിയിട്ടില്ല)
            .csrf(csrf -> csrf.disable())
            // ക്ലയന്റ് ഡെമോ ടൂളുകൾക്ക് CORS അനുവദിക്കുക
            .cors(withDefaults());
        return http.build();
    }

    // ഒരു ഇൻ-മെമ്മറി ക്ലയന്റ് (RegisteredClient) மற்றும் ഒരു JWK സോഴ്സ് നിർവചിക്കുക:
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
        // ഒരു RSA കീ സൃഷ്ടിക്കുക (ഡെവ്/ടെസ്റ്റ്‌ക്കായി, സ്റ്റാർട്ടപ്പിൽ പുതിയതായി സൃഷ്ടിക്കുക)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ഈ ക്രമീകരണം ഡിഫാൾട്ട് OAuth2 എന്റ്പോയിന്റുകൾ പരസ്യപ്പെടുത്തും: `/oauth2/token` ടോക്കണുകൾക്കായി, `/oauth2/jwks` JSON Web Key Set-നായി. (Spring-ന്റെ `AuthorizationServerSettings` ഡിഫാള്റ്റ് `/oauth2/token` , `/oauth2/jwks` നെ മാപ്പ് ചെയ്യുന്നു ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) സെർവർ RSA കീ ഉപയോഗിച്ച് സൈൻ ചെയ്ത JWT ആക്സസ് ടോക്കണുകൾ നൽകുകയും, പബ്ലിക് കീ `https://<your-app>:/oauth2/jwks` ൽ പ്രസിദ്ധീകരിക്കുകയും ചെയ്യും.

**OpenID Connect കണ്ടെത്തൽ സജീവമാക്കുക:** APIM സ്വയം പുറത്തിറക്കുന്ന ISSUER, JWKS ലഭിക്കാൻ, സുരക്ഷാ കോൺഫിഗറേഷനിൽ `.oidc(Customizer.withDefaults())` ചേർക്കുക ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ഉദാഹരണത്തിന്:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration സജീവമാക്കുന്നു
```

ഇത് `/.well-known/openid-configuration` തുറക്കുന്നു, APIM ഇതെ മെറ്റാഡേറ്റായി ഉപയോഗിക്കാം. ഒടുവിൽ, APIM-ന്റെ `<audiences>` പരിശോധന കഴിയാൻ JWT **audience** ക്ലെയിം ആണ് ഇഷ്ടാനുസൃതമാക്കേണ്ടത്. ഉദാഹരണത്തിന്, ടോക്കൺ കസ്റ്റമൈസർ ചേർക്കുക:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // ഒരു കസ്റ്റം പ്രേക്ഷകർ (ഉദാഹരണം, ക്ലയന്റ് ഐഡി അല്ലെങ്കിൽ API അയഡന്റിഫയർ) സജ്ജമാക്കുക
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

ഇത് ടോക്കണുകൾ `"aud": ["mcp-client"]` കയറ്റും, APIM പ്രതീക്ഷിക്കുന്ന ക്ലയന്റ് ഐഡിഎ അല്ലെങ്കിൽ സ്കോപ്പിനോട് പൊരുത്തപ്പെടുന്നു.

## ടോക്കൺ, JWKS എന്റ്പോയിന്റുകൾ തുറന്നിരിക്കണം

വിന്യസിച്ച ശേഷം, നിങ്ങളുടെ ആപ്പിൻ്റെ **issuer URL** ആയിരിക്കും `https://<app-fqdn>`, ഉദാ: `https://my-mcp-app.eastus.azurecontainerapps.io`. അതിന്റെ OAuth2 എന്റ്പോയിന്റുകൾ:

- **ടോക്കൺ എന്റ്പോയിന്റ്:** `https://<app-fqdn>/oauth2/token` - ടോക്കണുകൾ ഇവിടെ ലഭിക്കും (client_credentials ഫ്‌ളോ).
- **JWKS എന്റ്പോയിന്റ്:** `https://<app-fqdn>/oauth2/jwks` - JWK സെറ്റ് തിരിച്ചു നൽകുന്നു (APIM സൈൻ ചെയിത ചാപുകള്‍ നേടാന്‍).
- **OpenID കോൺഫിഗ്:** `https://<app-fqdn>/.well-known/openid-configuration` - OIDC കണ്ടെത്തൽ JSON (ഉൾപ്പെടുന്നു `issuer`, `token_endpoint`, `jwks_uri` മുതലായവ).

APIM **OpenID configuration URL** സൂചിപ്പിക്കും, അത് കൊണ്ട് `jwks_uri` കണ്ടെത്തും. ഉദാഹരണത്തിന്, നിങ്ങളുടെ Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` ആണെങ്കിൽ, APIM ന് `<openid-config url="...">` ഉപയോഗിക്കണം `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (ഡിഫോൾട്ട് Spring നിർവ്വചനം ആ മെടാഡേറ്റയിൽ `issuer` ആ URL ആക്കി സജ്ജമാക്കും ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (APIM) ക്രമീകരിക്കല്‍ (`validate-jwt`)

Azure APIM-ൽ, inbound പോളിസിയായ `<validate-jwt>` നു സമർപ്പിച്ച JWT-കൾ Spring Authorization Server-ന്റെ വിധേയമാകുന്നുവെന്ന് പരിശോധിക്കുന്ന പോളിസി ചേർക്കുക. ലളിതമായ ക്രമീകരണത്തിന് OpenID Connect മെറ്റാഡേറ്റ URL ഉപയോഗിക്കാം. ഉദാഹരണ പോളിസി ഭാഗം:

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

ഈ പോളിസി APIM ക്ക് Spring Auth Server-ന്റെ OpenID കോൺഫിഗറേഷൻ പെടുത്താനും JWKS നേടാനും, ഓരോ ടോക്കണും വിശ്വസനീയമായ കീയിൽ സൈൻ ചെയ്തതാണെന്നും ശരിയായ audience ഉണ്ട് എന്നും പരിശോധിക്കാനും പറയുന്നു. (`<issuers>` ഒഴിവാക്കിയാൽ APIM സ്വയം മെറ്റാഡേറ്റയിൽ നിന്നുള്ള `issuer` ക്ലെയിം ഉപയോഗിക്കും.) `<audience>` നിങ്ങളുടെ ക്ലയന്റ് ID അല്ലെങ്കിൽ API റിസോഴ്‌സ് ഐഡിയന്റിഫയർ ടോക്കണിൽ പൊരുത്തപ്പെടണം (മുകളിൽ `"mcp-client"` ആയി ക്രമീകരിച്ചിരിക്കുന്നു). ഇത് Microsoft ന്റെ ഡോക്യുമെന്റേഷനിലെ `validate-jwt` `<openid-config>` ഉപയോഗത്തിന്റെ അനുസരണമാണു് ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

പരിശോധന കഴിഞ്ഞുകഴിഞ്ഞാൽ, APIM അഭ്യർത്ഥന (മൂല്യ `Authorization` ഹെഡർ ഉൾപ്പെടെ) ബാക്ക്‌എൻഡിലേക്ക് ഫോർവേർഡ് ചെയ്യും. Spring ആപ്പ് റെസോഴ്‌സ് സെർവർ ആയതിനാൽ, ടോക്കൺ വീണ്ടും സ്ഥിരീകരിക്കും, എന്നാൽ APIM ഇതിനകം വസ്തുത ഉറപ്പാക്കിയിട്ടുണ്ട്. (ഡെവലപ്മെന്റിന്, APIM ന്റെ പരിശോധനയ്ക്ക് ആശ്രയിക്കാം, ആപ്പിൽ അധിക പരിശോധനകൾ നിർത്താം, എന്നാൽ ഇരുവരും സൂക്ഷിക്കുന്നത് സുരക്ഷിതമാണ്.)

## ഉദാഹരണ ക്രമീകരണങ്ങൾ

| ക്രമീകരണം      | ഉദാഹരണ മൂല്യം                                                     | കുറിപ്പുകൾ                                |
|-----------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**      | `https://my-mcp-app.eastus.azurecontainerapps.io`                   | നിങ്ങളുടെ Container App-ന്റെ URL (അധിഷ്ഠിത URI)  |
| **ടോക്കൺ എന്റ്പോയിന്റ്** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`      | ഡിഫാൾട്ട് Spring ടോക്കൺ എന്റ്പോയിന്റ് ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS എന്റ്പോയിന്റ്** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | ഡിഫാൾട്ട് JWK സെറ്റ് എന്റ്പോയിന്റ് ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID കോൺഫിഗ്** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC കണ്ടെത്തൽ ഡോക്യുമെന്റ് (സ്വയം സൃഷ്ടിച്ചത്)    |
| **APIM audience** | `mcp-client`                                                        | OAuth ക്ലയന്റ് ID അല്ലെങ്കിൽ API റിസോഴ്‌സ് പേര്    |
| **APIM പോളിസി** | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ഈ URL ഉപയോഗിക്കുന്നു ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## പൊതുവായ വീഴ്ചകൾ

- **HTTPS/TLS:** APIM ഗേറ്റ്‌വേയ് ഓപ്പൺഐഡി/JWKS എന്റ്പോയിന്റ് HTTPS ൽ അംഗീകരിച്ച സർട്ടിഫിക്കറ്റ് ഉണ്ടായിരിക്കണം. ഡിഫോൾട്ടായി Azure Container Apps Azure-നടത്തിയ TLS സർട്ടിഫിക്കറ്റ് നൽകുന്നു ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). നിങ്ങൾ കസ്റ്റം ഡൊമെയ്ൻ ഉപയോഗിക്കുന്നുവെങ്കിൽ, സർട്ടിഫിക്കറ്റ് ബൈൻഡ് ചെയ്യുക (Azure യുടെ സൗജന്യ മാനേജുചെയ്ത സർട്ടിഫിക്കറ്റ് ആപ്ഷൻ ഉപയോഗിക്കാം) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM സർട്ടിഫിക്കറ്റ് വിശ്വാസ്യമല്ലെങ്കിൽ, `<validate-jwt>` മെറ്റാഡേറ്റ സഞ്ചയം പരാജയപ്പെടും.

- **എന്റ്പോയിന്റ് ആക്‌സസിബിലിറ്റി:** Spring ആപ്പിന്റെ എന്റ്പോയിന്റുകൾ APIM എത്താൻ സാധിക്കുന്നുണ്ടെന്ന് ഉറപ്പ് വരുത്തുക. `--ingress external` ഉപയോഗിക്കൽ (അല്ലെങ്കിൽ പോർട്ടലിൽ ഇംഗ്രസ്സ് സജ്ജീകരിക്കൽ) ഏറ്റവും ലളിതമാണ്. നിങ്ങൾ ഇന്റേണൽ അല്ലെങ്കിൽ VNet-ബൗണ്ട് പരിസ്ഥിതി തിരഞ്ഞെടുക്കുകയാണെങ്കിൽ, APIM (ഡിഫാൾട്ട് പൊതു) അത് കാണാതെപോകാം അതിന്റെ VNet യിൽ സ്ഥലം നൽകാതെ പോയാൽ. ടെസ്റ്റ് സെറ്റപ്പിൽ പൊതു ഇംഗ്രസ്സ് ഉപയോഗിക്കുക, APIM `.well-known` , `/jwks` URLs വിളിക്കാൻ കഴിയും.

- **OpenID കണ്ടെത്തൽ സജീവം:** ഡിഫോൾട്ടായി, Spring Authorization Server `/.well-known/openid-configuration` പുറത്തുവരുത്തുന്നില്ല OIDC സജീവമായില്ലെങ്കിൽ. `.oidc(Customizer.withDefaults())` നിങ്ങളുടെ സുരക്ഷാ കോൺഫിഗറേഷനിൽ ഉൾപ്പെടുത്തുക (മുകളിൽ കാണുക) പ്രൊവൈഡർ കോൺഫിഗറേഷൻ എൻഡ്‌പോയിന്റ് സജീവമാക്കാൻ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). അല്ലെങ്കിൽ APIM ന്റെ `<openid-config>` കോൾ 404 ആയി പരാജയപ്പെടും.

- **Audience Claim:** Spring-ന്റെ ഡിഫോൾഡ് പെരുമാറ്റം `aud` ക്ലെയിം ക്ലയന്റ് ID ആക്കി ക്രമീകരിക്കുന്നു. APIM-ന്റെ `<audience>` പരിശോധന പരാജയപ്പെട്ടാൽ, ടോക്കൺ ഇഷ്ടാനുസൃതമാക്കേണ്ടതുണ്ടാകും (മുകളിലെ മാതൃക പോലെ) അല്ലെങ്കിൽ APIM പോളിസി ഭേദഗതി. നിങ്ങളുടെ JWT ലെ audience `<audience>` യുമായി പൊരുത്തപ്പെടുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക.

- **JSON Metadata Parsing:** OpenID കോൺഫിഗറേഷൻ JSON സാധുവായിരിക്കണം. Spring-ന്റെ ഡിഫോൾട്ട് കോൺഫിഗരേഷൻ സാധാരണ OIDC മെറ്റാഡേറ്റാ ഡോക്യുമെന്റ് പൊയ്ക്കോളും. ശരിയായ `issuer` , `jwks_uri` ഉള്ളതായി ഉറപ്പാക്കുക. നിങ്ങൾ Spring ഒരു പ്രോക്സി അല്ലെങ്കിൽ പാത്ത്-അധിഷ്ഠിത റൂട്ടിനു പിന്നിൽ ഹോസ്റ്റ് ചെയ്താൽ URLs ഈ മെറ്റാഡേറ്റയിൽ ശരിയാണെന്ന് പരിശോധിക്കുക. APIM ഈ മൂല്യങ്ങൾ മാറ്റാതെ ഉപയോഗിക്കും.

- **പോളിസി ക്രമീകരണം:** APIM പോളിസിയിൽ, `<validate-jwt>` ബാക്ക്‌എൻഡിലേക്ക് റൂട്ടിംഗ് ചെയ്‌തതിനുമുമ്പേയ് വെക്കുക. അല്ലെങ്കിൽ നിങ്ങൾക്ക് തടസ്സമില്ലാതെ ടോക്കൺ ഇല്ലാതെ ആപ്പിലേക്ക് വിളികൾ എത്താം. `<validate-jwt>` ആദ്യം `<inbound>` താഴെ തന്നെ (മറ്റൊരു കണ്ടീഷനിൽ നിക്ഷേപിക്കാതെ) വേണം വരുത്തുക, APIM അത് എന്ത് ആവശ്യമുണ്ടോ അതുപോലെ പ്രയോഗിക്കും.

മുകളിൽ പറഞ്ഞ നിലപാടുകൾ പാലിച്ച്, നിങ്ങൾക്ക് Spring AI MCP സെർവർ Azure Container Apps-ൽ ഓടിക്കുകയും Azure API Management ജീവിതത്തിലെ OAuth2 JWTകൾ സാധൂകരിക്കുകയും ചെയ്യാം കുറഞ്ഞ പോളിസിയോടെ. പ്രധാനം: Spring Auth എന്റ്പോയിന്റുകൾ TLS সহ പൊതുഗത സജ്ജമാക്കുക, OIDC കണ്ടെത്തൽ സജീവമാക്കുക, APIM-ന്റെ `validate-jwt` OpenID കോൺഫിഗ് URL-യിൽ സൂചിപ്പിക്കുക (JWKS സ്വയം നേടി കഴിഞ്ഞു). ഇത് ഡെവ്/ടെസ്റ്റ് പരിസ്ഥിതിക്ക് അനുയോജ്യമാണ്; പ്രൊഡക്ഷനിൽ ശരിയായ രഹസ്യ മാനേജ്മെന്റ്, ടോക്കൺ കാലാവധി, JWKS കീകളുടെ തിരിഞ്ഞ് കൈമാറ്റം പരിഗണിക്കുക.


**റിയഫറൻസുകൾ:** ഡീഫോൾട്ട് എൻഡ്പോയിൻറുകൾക്കായി സ്പ്രിങ് ഓതറൈസേഷൻ സർവർ ഡോക്യുമെന്റേഷൻ കാണുക ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ഒപ്പം OIDC കോൺഫിഗറേഷൻ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` ഉദാഹരണങ്ങൾക്ക് മൈക്രോസോഫ്റ്റ് APIM ഡോക്യുമെന്റേഷൻ കാണുക ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ഡിപ്പ്ലോയ്‌മെന്റിനും സർട്ടിഫിക്കേറ്റുകൾക്കുമായി ആസ്യൂർ കണ്ടെയ്നർ ആപ്പുകളുടെ ഡോക്യുമെന്റേഷൻ കാണുക ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->