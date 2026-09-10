# ការដាក់បង្ហោះកម្មវិធី Spring AI MCP ទៅកាន់ Azure Container Apps

> [!WARNING]
> ម៉ាស៊ីនបម្រើបញ្ជាក់សម្ងាត់/ធនធានបញ្ចូលគ្នានេះមានគោលបំណងសម្រាប់ការសិក្សារៀន និង
> ការអភិវឌ្ឍ/សាកល្បង។ ប្រព័ន្ធផលិតកម្មគួរតែប្រើអ្នកផ្គត់ផ្គង់អត្តសញ្ញាណពីរប្រភេទ,
> កូនសោហត្ថលេខាអចិន្ត្រៃយ៍ និងពាក្យសម្ងាត់ដែលបានផ្ទុកនៅក្នុងហាងសម្ងាត់ដែលគ្រប់គ្រង។

 ([ការការពារម៉ាស៊ិនបម្រើ Spring AI MCP ជាមួយ OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *រូបភាព៖ ម៉ាស៊ីនបម្រើ Spring AI MCP ដែលមានការការពារជាមួយ Spring Authorization Server។ ម៉ាស៊ីនបម្រើចេញសញ្ញាស្នាក់កាសចូលទៅកាន់អតិថិជន និងផ្ទៀងផ្ទាត់ពួកវា នៅពេលទទួលបានការស្នើសុំ (ប្រភព៖ ប្លុក Spring) ([ការការពារម៉ាស៊ិនបម្រើ Spring AI MCP ជាមួយ OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* ដើម្បីដាក់បង្ហោះម៉ាស៊ីនបម្រើ Spring MCP សាងសង់វាជាគំណែកផ្ទុក និងប្រើ Azure Container Apps ជាមួយការចូលរួមពីខាងក្រៅ។ ឧទាហរណ៍ ដោយប្រើ Azure CLI អ្នកអាចបើកដំណើរការ៖

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

វានេះបង្កើតកម្មវិធី Container App ដែលអាចចូលរកបានសាធារណៈជាមួយ HTTPS បានបើក (Azure ផ្តល់វិញ្ញាបនបត្រចុះហត្ថលេខា TLS ដោយឥតគិតថ្លៃសម្រាប់ដែនកំណត់លំនាំដើម `*.azurecontainerapps.io` ([ឈ្មោះដែនផ្ទាល់ខ្លួន និងវិញ្ញាបនបត្រដែលគ្រប់គ្រងដោយឥតគិតថ្លៃនៅក្នុង Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). លទ្ធផលការបញ្ជាលោតបង្ហាញ FQDN នៃកម្មវិធី (ឧ. `my-mcp-app.eastus.azurecontainerapps.io`) ដែលក្លាយទៅជាមូលដ្ឋានអាសយដ្ឋាន **issuer URL**។ ធានាថាការចូលរួម HTTP ត្រូវបានបើក (ដូចខាងលើ) ដើម្បីអោយ APIM អាចចូលទៅកាន់កម្មវិធី។ ក្នុងការតំឡើងសាកល្បង/អភិវឌ្ឍ ប្រើជម្រើស `--ingress external` (ឬភ្ជាប់ដែនផ្ទាល់ខ្លួនជាមួយ TLS តាម [ឯកសាររបស់ Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([ឈ្មោះដែនផ្ទាល់ខ្លួន និងវិញ្ញាបនបត្រដែលគ្រប់គ្រងដោយឥតគិតថ្លៃនៅក្នុង Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)))។ រក្សាទុកគុណលក្ខណៈដែលមានភាពងាយរងគ្រោះ (ដូចជា របស់សម្ងាត់អតិថិជន OAuth) នៅក្នុង Container Apps secrets ឬ Azure Key Vault ហើយផ្ញើវាចូលទៅកុងតឺនឺរជាផ្លាស់ប្តូរការបរិស្ថាន។

## ការកំណត់ Spring Authorization Server

នៅក្នុងកូដកម្មវិធី Spring Boot របស់អ្នក សូមបញ្ចូល Spring Authorization Server និង Resource Server starters។ កំណត់ `RegisteredClient` (សម្រាប់ `client_credentials` grant ក្នុងការអភិវឌ្ឍ/សាកល្បង) និងចំណុចប្រភពកូនសោ JWT។ ឧទាហរណ៍ ក្នុង `application.properties` អ្នកអាចកំណត់៖

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

បើក Spring Authorization Server និង Resource Server ដោយកំណត់ security filter chain។ ឧទាហរណ៍៖

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // បើកបង្ហាញចំណុចជាច្រើនរបស់ម៉ាស៊ីនបម្រើអនុញ្ញាត
            .apply(authzServer.and())
            // បើកម៉ាស៊ីនបម្រើធនធាន (ផ្ទៀងផ្ទាត់ JWT លើសំណើដែលចូលមក)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // ពន្លត់ CSRF (ម៉ាស៊ីនបម្រើ MCP មិនមែនផ្អែកលើកម្មវិធីរុករក)
            .csrf(csrf -> csrf.disable())
            // អនុញ្ញាត CORS សម្រាប់ឧបករណ៍សាកល្បងអតិថិជន
            .cors(withDefaults());
        return http.build();
    }

    // ប្រកាសអតិថិជនក្នុងម៉ោនមេទោ (RegisteredClient) និងប្រភព JWK មួយ៖
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
        // បង្កើតកូនសោ RSA (សម្រាប់ dev/test បង្កើតឡើងថ្មីពេលចាប់ផ្តើម)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ការតំឡើងនេះនឹងបង្ហាញច្រក OAuth2 លំនាំដើម៖ `/oauth2/token` សម្រាប់សញ្ញាស្នាក់កាស និង `/oauth2/jwks` សម្រាប់ JSON Web Key Set។ (លំនាំដើម Spring `AuthorizationServerSettings` នឹងផ្ទៀងផ្ទាត់ `/oauth2/token` និង `/oauth2/jwks` ([គំរូការកំណត់ :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) ម៉ាស៊ីនបម្រើនឹងចេញសញ្ញាស្នាក់ JWT ដែលបានចុះហត្ថលេខាដោយកូនសោ RSA ខាងលើ ហើយបង្ហាញកូនសោសាធារណៈរបស់វានៅ `https://<your-app>:/oauth2/jwks`។

**បើកការរកឃើញ OpenID Connect:** ដើម្បីអោយ APIM អាចយក issuer និង JWKS ដោយស្វ័យប្រវត្តិ សូមបើកច្រកបញ្ជាក់កំណត់រចនាសម្ព័ន្ធ OIDC provider ដោយបន្ថែម `.oidc(Customizer.withDefaults())` ក្នុងការកំណត់សុវត្ថិភាពរបស់អ្នក ([គំរូការកំណត់ :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))។ ឧទាហរណ៍៖

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– អនុញ្ញាត /.well-known/openid-configuration
```

វានេះបង្ហាញ `/.well-known/openid-configuration` ដែល APIM អាចប្រើសម្រាប់ម៉ែតាដាតា។ ចុងក្រោយ អ្នកប្រហែលជាចង់ប្ដូរចំណាប់អារម្មណ៍ JWT **audience** ដើម្បីអោយការត្រួតពិនិត្យ `<audiences>` របស់ APIM អាចជោគជ័យ។ ឧទាហរណ៍ បន្ថែម token customizer៖

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // ដាក់ក្រុមគោលដៅផ្ទាល់ខ្លួន (ឧ. អត្តសញ្ញាណអតិថិជន ឬ អត្តសញ្ញាណ API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

វា​ធានាថាសញ្ញាស្នាក់មាន `"aud": ["mcp-client"]` ដែលដូចគ្នានឹងលេខអត្តសញ្ញាណអតិថិជន (client ID) ឬ scope ដែល APIM គិតទុក។

## ការបង្ហាញច្រក Token និង JWKS

បន្ទាប់ពីដាក់បង្ហោះ អាសយដ្ឋាន **issuer URL** នៃកម្មវិធីរបស់អ្នកនឹងជារំលង `https://<app-fqdn>` ឧ. `https://my-mcp-app.eastus.azurecontainerapps.io`។ ច្រក OAuth2 របស់វាគឺ៖

- **ច្រក Token:** `https://<app-fqdn>/oauth2/token` – អតិថិជនទទួលយកសញ្ញាស្នាក់កាននៅទីនេះ (client_credentials flow)។
- **ច្រក JWKS:** `https://<app-fqdn>/oauth2/jwks` – ផ្ដល់ហ៊ុម JWK (APIM ប្រើសម្រាប់យកកូនសោចុះហត្ថលេខា)។
- **កំណត់ OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON ដើម្បីស្វែងរក OIDC (រួមមាន `issuer`, `token_endpoint`, `jwks_uri`, ល។)។  

APIM នឹងបង្ហាញទៅ URL **OpenID configuration** ដែលវាស្វែងរក `jwks_uri`។ ឧ. ប្រសិនបើ FQDN Container App របស់អ្នកគឺ `my-mcp-app.eastus.azurecontainerapps.io` ទៅហើយ `<openid-config url="...">` របស់ APIM គួរតែប្រើ `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`។ (លំនាំដើម Spring នឹងកំណត់ `issuer` នៅក្នុងម៉ែតាដាតានោះដោយប្រើ URL មូលដ្ឋានដូចគ្នា ([គំរូការកំណត់ :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))។

## ការកំណត់ Azure API Management (`validate-jwt`)

នៅ Azure APIM សូមបន្ថែមគោលនយោបាយ inbound ដែលប្រើ `<validate-jwt>` ដើម្បីត្រួតពិនិត្យ JWT ចូលមក ប្រកួតប្រជែងជាមួយ Spring Authorization Server របស់អ្នក។ សម្រាប់ការតំឡើងសាមញ្ញ អ្នកអាចប្រើ URL ម៉ែតាដាតា OpenID Connect។ ផ្នែកគោលនយោបាយឧទាហរណ៍៖

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

គោលនយោបាយនេះប្រាប់ APIM ឲ្យយកកំណត់រចនាសម្ព័ន្ធ OpenID ពី Spring Auth Server, ថតរូប JWKS របស់វា ហើយផ្ទៀងផ្ទាត់ថាសញ្ញាស្នាក់នីមួយៗ ឆ្លងកាត់កូនសោដែលទុកចិត្ត និងមាន audience ត្រឹមត្រូវ។ (បើអ្នកមិនមាន `<issuers>`, APIM នឹងប្រើ `issuer` claims ពីម៉ែតាដាតាដោយស្វ័យប្រវត្តិ)។ `<audience>` គួរតែផ្គូផ្គងទៅនឹង client ID របស់អ្នក ឬ លេខសម្គាល់ធនធាន API ក្នុងសញ្ញាស្នាក់ (ក្នុងឧទាហរណ៍ខាងលើ យើងកំណត់ទៅ `"mcp-client"`)។ នេះស្របតាមឯកសាររបស់ Microsoft ស្ដីពីការប្រើប្រាស់ `validate-jwt` ជាមួយ `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))។

បន្ទាប់ពីវីរុសផ្ទៀងផ្ទាត់ហើយ APIM នឹងផ្ញើសំណើ (រួមទាំងមួក `Authorization` ដើម) ទៅបន្ទុកក្រោយ។ ព្រោះកម្មវិធី Spring ក៏ជាម៉ាស៊ីនបម្រើធនធានដែរ វានឹងផ្ទៀងផ្ទាត់សញ្ញាស្នាក់ម្តងទៀត ប៉ុន្តែ APIM មានដំណឹងអំពីភាពត្រឹមត្រូវរបស់វា។ (សម្រាប់ការអភិវឌ្ឍ អ្នកអាចពឹងផ្អែកលើការត្រួតពិនិត្យរបស់ APIM ហើយបិទការត្រួតពិនិត្យបន្ថែមនៅកម្មវិធី ប្រសិនបើចង់បាន ប៉ុន្តែការរក្សាទុកទាំងពីរមានសុវត្ថិភាពជាង)

## ការកំណត់ឧទាហរណ៍

| ការកំណត់            | តម្លៃឧទាហរណ៍                                                   | កំណត់សម្គាល់                              |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | URL នៃ Container App របស់អ្នក (URI មូលដ្ឋាន)        |
| **ច្រក Token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | ច្រក Token លំនាំដើមរបស់ Spring ([គំរូការកំណត់ :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **ច្រក JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | ច្រក JWK Set លំនាំដើម ([គំរូការកំណត់ :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **កំណត់ OpenID**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | ឯកសារស្វែងរក OIDC (បង្កើតដោយស្វ័យប្រវត្តិ)    |
| **គោលដៅ APIM**  | `mcp-client`                                                         | Client ID OAuth ឬឈ្មោះធនធាន API       |
| **គោលនយោបាយ APIM**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ប្រើ URL នេះ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## បញ្ហាធម្មតា

- **HTTPS/TLS៖** កំពង់ផែក្រាម APIM ត្រូវការឱ្យច្រក OpenID/JWKS ដែលមាន HTTPS និងវិញ្ញាបនបត្រត្រឹមត្រូវ។ ដោយលំនាំដើម Azure Container Apps ផ្តល់វិញ្ញាបនបត្រ TLS ដែលទុកចិត្តសម្រាប់ដែនផ្ទាល់ខ្លួនដែលគ្រប់គ្រងដោយ Azure ([ឈ្មោះដែនផ្ទាល់ខ្លួន និងវិញ្ញាបនបត្រដែលគ្រប់គ្រងដោយឥតគិតថ្លៃនៅក្នុង Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))។ ប្រសិនបើអ្នកប្រើដែនផ្ទាល់ខ្លួន សូមភ្ជាប់វិញ្ញាបនបត្រ (អ្នកអាចប្រើលក្ខណៈសម្បត្តិវិញ្ញាបនបត្រដែលគ្រប់គ្រងដោយឥតគិតថ្លៃរបស់ Azure) ([ឈ្មោះដែនផ្ទាល់ខ្លួន និងវិញ្ញាបនបត្រដែលគ្រប់គ្រងដោយឥតគិតថ្លៃនៅក្នុង Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))។ ប្រសិនបើ APIM មិនអាចទុកចិត្តវិញ្ញាបនបត្រច្រកនេះ អំពើ `<validate-jwt>` នឹងបរាជ័យក្នុងការទាញយកម៉ែតាដាតា។

- **ការចូលដល់ច្រក៖** ចូរធានាថាច្រករបស់កម្មវិធី Spring អាចប្រើបានពី APIM។ ការប្រើ `--ingress external` (ឬបើក ingress ក្នុងផ្ទៃទំព័រ) គឺសាមញ្ញជាងគេ។ ប្រសិនបើអ្នកជ្រើសរើសបរិយាកាសក្នុងរឺចាប់ពី vNet, APIM (ដែលលំនាំដើមជាសាធារណៈ) អាចមិនចូលដល់វាបើមិនបានដាក់ក្នុង VNet ដូចគ្នា។ ក្នុងការតេស្ត សូមមើលទៅការចូលរួមសាធារណៈ ដើម្បីអោយ APIM អាចហៅ URL `.well-known` និង `/jwks` បាន។

- **ការរកឃើញ OpenID បានបើក៖** ដោយលំនាំដើម Spring Authorization Server **មិនបង្ហាញ** `/.well-known/openid-configuration` លុះត្រាតែ OIDC ត្រូវបានបើក។ សូមប្រាកដថាបញ្ចូល `.oidc(Customizer.withDefaults())` នៅក្នុងការកំណត់សុវត្ថិភាពរបស់អ្នក (មើលខាងលើ) ដើម្បីឲ្យច្រកកំណត់រចនាសម្ព័ន្ធរបស់អ្នកផ្គត់ផ្គង់ដំណើរការ ([គំរូការកំណត់ :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))។ ផ្ទុយទៅវិញហើយ APIM `<openid-config>` នឹងទទួលបានកូដ 404។

- **Audience Claim៖** អាកប្បកិរិយាលំនាំដើម Spring គឺកំណត់ claims `aud` ជាលេខសម្គាល់ client។ ប្រសិនបើការត្រួតពិនិត្យ `<audience>` របស់ APIM មិនជោគជ័យ អ្នកប្រហែលជាត្រូវប្តូរសញ្ញាស្នាក់ (ដូចបានបង្ហាញខាងលើ) ឬកែសំរួលគោលនយោបាយ APIM។ សូមដឹងថា audience នៅក្នុង JWT របស់អ្នកត្រូវតែដូចគ្នានឹងដែលបានកំណត់ក្នុង `<audience>`។

- **ការពិនិត្យម៉ែតា JSON៖** JSON កំណត់រចនាសម្ព័ន្ធ OpenID ត្រូវតែត្រឹមត្រូវ។ កំណត់រចនាសម្ព័ន្ធលំនាំដើមរបស់ Spring នឹងបញ្ចេញឯកសារម៉ែតាដាតា OIDC ស្តង់ដា។ សូមពិនិត្យថាវាអាចរួមបញ្ចូល `issuer` និង `jwks_uri` ត្រឹមត្រូវ។ ប្រសិនបើអ្នកផ្ដល់ Spring ពីក្រោយ proxy ឬផ្លូវតាមផ្លូវ, សូមពិនិត្យ URL ទាំងនេះម្តងទៀតក្នុងម៉ែតាដាតា។ APIM នឹងប្រើតម្លៃទាំងនេះដូចដែលមាន។

- **លំដាប់គោលនយោបាយ៖** ក្នុងគោលនយោបាយ APIM, សូមដាក់ `<validate-jwt>` **មុន** ការបញ្ជូនទៅបន្ទុកក្រោយ។ ផ្ទុយទៅវិញ, ការហៅអាចទៅដល់កម្មវិធីដោយគ្មានសញ្ញាស្នាក់ត្រឹមត្រូវបាន។ សូមធានាថា `<validate-jwt>` បង្ហាញភ្លាមៗក្រោម `<inbound>` (មិនចាក់ក្នុងលក្ខខណ្ឌផ្សេងទៀត) ដើម្បីអោយ APIM អនុវត្តវា។

ដោយអនុវត្តវិធីសាស្រ្តខាងលើ អ្នកអាចរត់ម៉ាស៊ីនបម្រើ Spring AI MCP របស់អ្នកនៅក្នុង Azure Container Apps ហើយឲ្យ Azure API Management ត្រួតពិនិត្យ JWT OAuth2 ចូលមកជាមួយគោលនយោបាយបន្ថែមតិចតួច។ ចំណុចសំខាន់គឺ៖ បង្ហាញច្រក Spring Auth ជាសាធារណៈជាមួយ TLS, បើកការរកឃើញ OIDC និងបញ្ជាក់ APIM `validate-jwt` ទៅ URL កំណត់រចនាសម្ព័ន្ធ OpenID (ដើម្បីអោយវាអាចទាញយក JWKS ដោយស្វ័យប្រវត្តិ)។ ការតំឡើងនេះសមស្របសម្រាប់បរិយាកាសអភិវឌ្ឍ/សាកល្បង; សម្រាប់ផលិតកម្ម សូមពិចារណាការគ្រប់គ្រងសម្ងាត់ត្រឹមត្រូវ, អាយុកាលសញ្ញាស្នាក់ និងការបង្វិលកូនសោក្នុង JWKS ឲ្យបានត្រឹមត្រូវ។


**ឯកសារ​ឯករាជ្យ៖** សូមមើលឯកសារ Spring Authorization Server សម្រាប់ចំនុចបញ្ចប់លំនាំដើម ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) និងការកំណត់ OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); សូមមើលឯកសារ Microsoft APIM សម្រាប់ឧទាហរណ៍ `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); និងឯកសារ Azure Container Apps សម្រាប់ការដាក់ពពួកនិងសញ្ញាប័ត្រ ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->