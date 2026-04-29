# ជាមួយការដាក់អនុវត្តកម្មវិធី Spring AI MCP នៅលើ Azure Container Apps

 ([ការពារ Spring AI MCP ស៊ឺវើស៍ជាមួយ OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *រូបភាព៖ ស៊ឺវើស៍ Spring AI MCP ដែលបានការពារជាមួយ Spring Authorization Server។ ស៊ឺវើស៍នេះ​ចេញកូដ token ចូលដំណើរការដល់អ្នកអតិថិជន ហើយធ្វើការត្រួតពិនិត្យពេលមានសំណើចូល (ប្រភព៖ Spring blog) ([ការពារ Spring AI MCP ស៊ឺវើស៍ជាមួយ OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* ដើម្បីដាក់អនុវត្ត Spring MCP server អ្នកត្រូវកសាងវាជា container ហើយប្រើ Azure Container Apps ជាមួយ ingress ខាងក្រៅ។ ឧទាហរណ៍ ប្រើ Azure CLI អ្នកអាចដំណើរការ៖

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

នេះបង្កើត Container App ដែលអាចចូលប្រើបានសាធារណៈជាមួយ HTTPS ដែលបានបើកសមត្ថភាព (Azure ផ្ដល់វិញ្ញាបនប័ត្រ TLS មិនគិតថ្លៃសម្រាប់ domain `*.azurecontainerapps.io` ដើមទិស ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ការបញ្ចូលសេចក្តីបញ្ជា​នេះ​រួមបញ្ចូល URL ពេញលេញ (FQDN) របស់កម្មវិធី (ឧ. `my-mcp-app.eastus.azurecontainerapps.io`), ដែលក្លាយជាប្រភព URL **issuer**។ សូមប្រាកដថា HTTP ingress ត្រូវបានបើកដូចដែលបានបង្ហាញខាងលើ ដើម្បី APIM អាចទាក់ទងដល់កម្មវិធីបាន។ ក្នុងសិ្ថិតិតេស្ត/អភិវឌ្ឍន៍ សូមប្រើជម្រើស `--ingress external` (ឬភ្ជាប់ domain ផ្ទាល់ខ្លួនជាមួយ TLS ដោយយោងតាម [ឯកសារ Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). រក្សាទុកគុណលក្ខណ: sensitive (ដូចជា client secrets របស់ OAuth) នៅក្នុង Container Apps secrets ឬ Azure Key Vault ហើយផ្ទេរសម្រាប់ប្រើក្នុង container ជា environment variables។

## ការកំណត់ Spring Authorization Server

ក្នុងកូដកម្មវិធី Spring Boot របស់អ្នក សូមបញ្ចូល Spring Authorization Server និង Resource Server starters។ កំណត់ `RegisteredClient` (សម្រាប់ `client_credentials` grant នៅក្នុង dev/test) និង JWT key source។ ឧទាហរណ៍ នៅក្នុង `application.properties` អ្នកអាចកំណត់៖

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

បើកដំណើរការ Authorization Server និង Resource Server ដោយកំណត់ security filter chain។ ឧទាហរណ៍៖

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // ចូលដំណើរការចំណុចចេញសេវាកម្មអនុម័ត
            .apply(authzServer.and())
            // ចូលដំណើរការសេវាកម្មធនធាន (ផ្ទៀងផ្ទាត់ JWT ក្នុងសំណើចូល)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // បិទ CSRF (ម៉ាស៊ីនមេ MCP មិនមែនផ្អែកលើកម្មវិធីរុករក)
            .csrf(csrf -> csrf.disable())
            // អនុញ្ញាត CORS សម្រាប់ឧបករណ៍សាកល្បងអតិថិជន
            .cors(withDefaults());
        return http.build();
    }

    // កំណត់អតិថិជននៅក្នុងចងចាំ (RegisteredClient) និងប្រភព JWK:
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
        // បង្កើតក(Keys) RSA (សម្រាប់ការអភិវឌ្ឍ/សាកល្បង បង្កើតឡើងតាមចាប់ផ្តើម)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ការកំណត់នេះនឹងបង្ហាញច្រក OAuth2 ដើមទិស៖ `/oauth2/token` សម្រាប់ទទួលបាន tokens និង `/oauth2/jwks` សម្រាប់ JSON Web Key Set។ (ដោយលំនាំដើម Spring’s `AuthorizationServerSettings` បង្រៀនផ្លូវ `/oauth2/token` និង `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) ស៊ឺវើស៍នឹងចេញ JWT access tokens ដែលបានចុះហត្ថលេខាដោយកូនសោរ RSA ខាងលើ ហើយផ្សព្វផ្សាយកូនសោសាធារណៈនៅ `https://<your-app>:/oauth2/jwks`។

**បើកដំណើរការ OpenID Connect discovery:** ដើម្បីអនុញ្ញាតឲ្យ APIM យក issuer និង JWKS យ៉ាងស្វ័យប្រវត្តិ សូមបើកការកំណត់ OIDC provider configuration endpoint ដោយបន្ថែម `.oidc(Customizer.withDefaults())` ក្នុងការកំណត់សុវត្ថិភាពរបស់អ្នក ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ឧទាហរណ៍៖

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– អនុញ្ញាត /.well-known/openid-configuration
```

នេះបង្ហាញផ្លូវ `/.well-known/openid-configuration` ដែល APIM អាចប្រើសម្រាប់ metadata។ ចុងក្រោយ អ្នកអាចចង់ប្ដូរប្រកាស JWT **audience** ដើម្បីឲ្យការត្រួតពិនិត្យ `<audiences>` របស់ APIM អាចជោគជ័យ។ ឧទាហរណ៍ បន្ថែម token customizer៖

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // កំណត់អ្នកទស្សនាប្ដូរតាមបំណង (ដូចជា អត្តសញ្ញាណអតិថិជន ឬ អត្តសញ្ញាណ API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

នេះធានាថា token របស់អ្នកមាន `"aud": ["mcp-client"]` ដែលសមស្របជាមួយ client ID ឬ scope ដែល APIM គិតថាត្រូវការ។

## ការបង្ហាញ Token និង JWKS Endpoints

បន្ទាប់ពីដាក់អនុវត្តរួច អ្នកនឹងមាន URL **issuer** នៃកម្មវិធីៈ `https://<app-fqdn>` ឧ. `https://my-mcp-app.eastus.azurecontainerapps.io`។ OAuth2 endpoints របស់វា​មាន៖

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – អតិថិជនទទួលបាន tokens នៅទីនេះ (client_credentials flow)។
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – ត្រឡប់ JWK set (APIM ប្រើសម្រាប់ទទួល keys ចុះហត្ថលេខា)។
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (មាន `issuer`, `token_endpoint`, `jwks_uri` ជាដើម)។

APIM នឹងចុះអាស្រ័យទៅ URL **OpenID configuration** ដែលវាកំណត់គ្រប់យ៉ាងពី `jwks_uri`។ ឧទាហរណ៍ ប្រសិនសិនអ្នក Container App FQDN គឺ `my-mcp-app.eastus.azurecontainerapps.io` APIM `<openid-config url="...">` គួរប្រើ `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`។ (ដោយលំនាំដើម Spring នឹងកំណត់ `issuer` ក្នុង metadata នោះទៅ URL ដើមដូចគ្នា ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## ការកំណត់ Azure API Management (`validate-jwt`)

នៅ Azure APIM សូមបន្ថែម policy inbound ដែលប្រើ `<validate-jwt>` ដើម្បីធ្វើការត្រួតពិនិត្យ JWT ចូលដំណើរការជាមួយ Spring Authorization Server របស់អ្នក។ សម្រាប់ការកំណត់មូលដ្ឋាន អ្នកអាចប្រើ OpenID Connect metadata URL។ ឧទាហរណ៍ policy snippet ៖

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

Policy នេះប្រាប់ APIM អោយទាញយក OpenID configuration ពី Spring Auth Server ទាញយក JWKS ហើយផ្ទៀងផ្ទាត់ថា token ទាំងអស់ត្រូវបានចុះហត្ថលេខា​ដោយ key ដែលទទួលបានជម្រៅ និងមាន audience ត្រឹមត្រូវ។ (បើអ្នកមិនបញ្ចូល `<issuers>` ទេ APIM នឹងប្រើ claim `issuer` ពី metadata ដោយស្វ័យប្រវត្តិ។) `<audience>` គួរតែសមស្របជាមួយ client ID រឺ resource API ដែលមានក្នុង token (នៅឧទាហរណ៍ខាងលើ យើងកំណត់ជា `"mcp-client"`។) នេះស្របទៅតាមឯកសារ Microsoft ស្តីពីការប្រើប្រាស់ `validate-jwt` ជាមួយ `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))។

បន្ទាប់ពីការផ្ទៀងផ្ទាត់ APIM នឹងផ្ញើសំណើ (រួមទាំង Header `Authorization` ដើមដំណើរការ) ទៅ backend។ ព្រោះកម្មវិធី Spring ក៏ជាស៊ឺវើស៍ resource ផងដែរ វានឹងបន្ថែមការផ្ទៀងផ្ទាត់ token ពីម្តងទៀត ប៉ុន្ដែ APIM បានធានាថា token ត្រឹមត្រូវរួចហើយ។ (សម្រាប់អភិវឌ្ឍន៍ អ្នកអាចពឹងផ្អែកលើការត្រួតពិនិត្យរបស់ APIM ប៉ុណ្ណោះ ហើយបិទការត្រួតពិនិត្យបន្ថែមនៅក្នុង app បើចង់ ប៉ុន្តែការរក្សាទុកទាំងពីរនោះប្រសើរជាង។)

## ការកំណត់គំរូ

| ការកំណត់           | តម្លៃគំរូ                                                         | កំណោត                                      |
|---------------------|------------------------------------------------------------------|--------------------------------------------|
| **Issuer**          | `https://my-mcp-app.eastus.azurecontainerapps.io`               | URL ដើមនៃ Container App                     |
| **Token endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`  | ច្រក token ដើមទិស Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**   | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`   | ច្រក JWK Set ដើមទិស ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **OpenID Config**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | ឯកសារ OIDC discovery (បង្កើតស្វ័យប្រវត្តិ)    |
| **APIM audience**   | `mcp-client`                                                    | Client ID របស់ OAuth ឬឈ្មោះ resource API     |
| **APIM policy**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ប្រើ URL នេះ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## បញ្ហាធម្មតា

- **HTTPS/TLS:** ទ្វារ APIM ត្រូវការថា OpenID/JWKS endpoint ត្រូវមាន HTTPS និងវិញ្ញាបនបត្រដែលត្រឹមត្រូវ។ ដោយលំនាំដើម Azure Container Apps ផ្ដល់វិញ្ញាបនបត្រ TLS ដែលទំនុកចិត្តសម្រាប់ domain ដែលគ្រប់គ្រងដោយ Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))។ ប្រសិនបើអ្នកប្រើ domain ផ្ទាល់ខ្លួន សូមភ្ជាប់វិញ្ញាបនបត្រឲ្យបាន ដោយអាចប្រើ function managed cert មិនគិតថ្លៃរបស់ Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))។ ប្រសិនបើ APIM មិនអាចទុកចិត្តវិញ្ញាបនបត្រនោះ `<validate-jwt>` នឹងមិនអាចទាញយក metadata នៅលើបាន។

- **ការចូលដំណើរក្នុង Endpoint:** ត្រូវប្រាកដថា endpoints របស់ Spring app អាចចូលដំណើរការពី APIM។ ប្រើ `--ingress external` (ឬបើក ingress នៅក្នុង portal) គឺងាយស្រួលបំផុត។ ប្រសិនប្រសើរអ្នកជ្រើសរើសបរិស្ថាន internal ឬ ស្ថិតក្នុង vNet មួយ APIM (ដែលឈរជាសាធារណៈ) អាចមិនអាចទាក់ទងបានទេ ដោយឡែកល្ងង់នៅក្នុង vNet ដូចគ្នា។ ក្នុងស្ថានភាពធ្វើតេស្ត សូមបញ្ជាក់ public ingress ដើម្បី APIM អាចទាក់ទង `.well-known` និង `/jwks` URLs បាន។

- **បើក OpenID Discovery:** ដោយលំនាំដើម Spring Authorization Server **មិនបង្ហាញ** `/.well-known/openid-configuration` លក់ពេលដែល OIDC មិនបានបើក។ សូមប្រាកដថាបានបញ្ចូល `.oidc(Customizer.withDefaults())` ក្នុងកំណត់សុវត្ថិភាពរបស់អ្នក (មើលខាងលើ) ដើម្បីវាចេញ provider configuration endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))។ បើមិនដូច្នេះការហៅ `<openid-config>` នៃ APIM នឹងបាន 404។

- **សក្ខីបត្រអ្នកទស្សនា Audience Claim:** លំនាំដើមរបស់ Spring គឺកំណត់ claim `aud` ទៅ client ID។ ប្រសិនបើ APIM ពិនិត្យ `<audience>` មិនជោគជ័យ អ្នកប្រហែលជាចាំបាច់ត្រូវផ្លាស់ប្តូរប្រភេទ token (ដូចបានបង្ហាញខាងលើ) ឬកែប្រែ policy APIM។ សូមប្រាកដថា audience ក្នុង JWT របស់អ្នកសមស្របទៅនឹង ការកំណត់ `<audience>` ។

- **ការបកប្រែ JSON Metadata:** ឯកសារ OpenID configuration JSON ត្រូវតែមានសុពលភាព។ កំណត់លំនាំដើមរបស់ Spring នឹងបញ្ចេញឯកសារ OIDC metadata ស្តង់ដារ។ សូមពិនិត្យថាវាបញ្ចូល `issuer` និង `jwks_uri` ត្រឹមត្រូវ។ ប្រសិនបើអ្នកបម្រុង Spring នៅក្រោយ proxy ឬច្រកផ្លូវ ពិនិត្យឲ្យបានត្រឹមត្រូវ URL ក្នុង metadata នេះ។ APIM នឹងប្រើតម្លៃទាំងនេះ ដោយមិនផ្លាស់ប្ដូរឡើយ។

- **លំដាប់នៃ Policy:** នៅក្នុង policy APIM សូមដាក់ `<validate-jwt>` នៅមុនការបញ្ជូនទៅ backend។ មិនដូច្នេះ សំណើប្រហែលជាចូលទៅកម្មវិធីដោយគ្មាន token ត្រឹមត្រូវ។ ត្រូវប្រាកដថា `<validate-jwt>` មាននៅភាគច្រើននៅតែមុខ `<inbound>` (មិនត្រូវទៅក្រោមលក្ខខណ្ឌផ្សេងទេ) ដើម្បី APIM អនុវត្តវាទៅតាមច្បាប់។

ដោយអនុវត្តតាមជំហានខាងលើ អ្នកអាចរត់ Spring AI MCP server នៅលើ Azure Container Apps ហើយអនុញាតឲ្យ Azure API Management ផ្ទៀងផ្ទាត់ JWT OAuth2 ចូលដោយនយោបាយសាមញ្ញ។ ចំណុចសំខាន់គឺ៖ បង្ហាញ endpoints Spring Auth ទៅសាធារណៈជាមួយ TLS, បើក OIDC discovery, ហើយផ្ញើ APIM `validate-jwt` ទៅ URL OpenID config (ដូច្នេះវាអាចទាញយក JWKS ស្វ័យប្រវត្តិបាន)។ ការកំណត់នេះសមស្របសម្រាប់បរិស្ថាន dev/test; សម្រាប់លទ្ធផល អ្នកគួរពិចារណាអំពីការគ្រប់គ្រងសម្ងាត់ សីតុណ្ហភាព token និងការប្តូរជារៀងរហូតនៃ keys នៅ JWKS ដូចត្រូវការ។
**យោង:** មើលឯកសារ Spring Authorization Server សម្រាប់ចំណុចចេញដើម ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) និងការកំណត់ OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); មើលឯកសារ Microsoft APIM សម្រាប់ឧទាហរណ៍ `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); និងឯកសារ Azure Container Apps សម្រាប់ការដាក់បញ្ជូន និងវិញ្ញាបនប័ត្រ ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំរកភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយម៉ាស៊ីនឆ្លាតអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាគ្រិស្តស័ក្សរបស់វាគួរត្រូវបានគិតថាជាប្រភពផ្លូវការបំផុត។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងស្នើឱ្យបកប្រែដោយមនុស្សដែលមានជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសប្លែកណាមួយ ដែលបង្កឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->