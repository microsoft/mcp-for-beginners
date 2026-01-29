# Spring AI MCP एपलाई Azure Container Apps मा डिप्लोय गर्ने तरिका

([Spring AI MCP सर्भरलाई OAuth2 सँग सुरक्षित गर्ने](https://spring.io/blog/2025/04/02/mcp-server-oauth2))  
*चित्र: Spring Authorization Server सँग सुरक्षित गरिएको Spring AI MCP सर्भर। सर्भरले क्लाइन्टहरूलाई एक्सेस टोकनहरू जारी गर्छ र आउने अनुरोधहरूमा तिनीहरूको प्रमाणीकरण गर्छ (स्रोत: Spring ब्लग) ([Spring AI MCP सर्भरलाई OAuth2 सँग सुरक्षित गर्ने](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).*  
Spring MCP सर्भरलाई डिप्लोय गर्न, यसलाई कन्टेनरको रूपमा बनाउनुहोस् र Azure Container Apps सँग बाह्य इन्ग्रेस प्रयोग गर्नुहोस्। उदाहरणका लागि, Azure CLI प्रयोग गरेर तपाईं यसरी चलाउन सक्नुहुन्छ:

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

यसले HTTPS सक्षम गरिएको सार्वजनिक रूपमा पहुँचयोग्य Container App सिर्जना गर्छ (Azure ले डिफल्ट `*.azurecontainerapps.io` डोमेनका लागि निःशुल्क TLS प्रमाणपत्र जारी गर्छ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). कमाण्डको आउटपुटमा एपको FQDN (जस्तै `my-mcp-app.eastus.azurecontainerapps.io`) समावेश हुन्छ, जुन **issuer URL** को आधार हुन्छ। HTTP इन्ग्रेस सक्षम छ कि छैन सुनिश्चित गर्नुहोस् (जसरी माथि देखाइएको छ) ताकि APIM एपसम्म पुग्न सकोस्। टेस्ट/डेभ सेटअपमा, `--ingress external` विकल्प प्रयोग गर्नुहोस् (वा TLS सहित कस्टम डोमेन बाँध्नुहोस् [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) अनुसार ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)))। संवेदनशील गुणहरू (जस्तै OAuth क्लाइन्ट सिक्रेटहरू) Container Apps secrets वा Azure Key Vault मा सुरक्षित राख्नुहोस् र तिनीहरूलाई कन्टेनरमा वातावरण चरको रूपमा म्याप गर्नुहोस्। 

## Spring Authorization Server कन्फिगर गर्ने तरिका

तपाईंको Spring Boot एपको कोडमा Spring Authorization Server र Resource Server स्टार्टरहरू समावेश गर्नुहोस्। `RegisteredClient` कन्फिगर गर्नुहोस् (डेभ/टेस्टमा `client_credentials` ग्रान्टका लागि) र JWT की स्रोत सेट गर्नुहोस्। उदाहरणका लागि, `application.properties` मा यसरी सेट गर्न सकिन्छ:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server र Resource Server सक्षम गर्न सुरक्षा फिल्टर चेन परिभाषित गर्नुहोस्। उदाहरणका लागि:

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

यस सेटअपले डिफल्ट OAuth2 एन्डपोइन्टहरू खोल्नेछ: `/oauth2/token` टोकनहरूको लागि र `/oauth2/jwks` JSON Web Key Set को लागि। (डिफल्ट रूपमा Spring को `AuthorizationServerSettings` ले `/oauth2/token` र `/oauth2/jwks` लाई म्याप गर्छ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) सर्भरले माथि उल्लेखित RSA कीद्वारा हस्ताक्षर गरिएको JWT एक्सेस टोकनहरू जारी गर्नेछ र यसको सार्वजनिक की `https://<your-app>:/oauth2/jwks` मा प्रकाशित गर्नेछ। 

**OpenID Connect डिस्कभरी सक्षम पार्नुहोस्:** APIM ले issuer र JWKS स्वचालित रूपमा प्राप्त गर्न सकून् भनेर, तपाईंको सुरक्षा कन्फिगरेसनमा `.oidc(Customizer.withDefaults())` थप्नुहोस् ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))। उदाहरणका लागि:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

यसले `/.well-known/openid-configuration` एक्स्पोज गर्नेछ, जुन APIM ले मेटाडाटा प्राप्त गर्न प्रयोग गर्न सक्छ। अन्तमा, तपाईं JWT को **audience** क्लेम अनुकूलन गर्न चाहनुहुन्छ ताकि APIM को `<audiences>` जाँच पास होस्। उदाहरणका लागि, टोकन कस्टमाइजर थप्नुहोस्:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

यसले टोकनहरूमा `"aud": ["mcp-client"]` समावेश गराउँछ, जुन APIM ले अपेक्षा गरेको क्लाइन्ट ID वा स्कोपसँग मेल खान्छ। 

## टोकन र JWKS एन्डपोइन्टहरू सार्वजनिक गर्ने

डिप्लोय गरेपछि, तपाईंको एपको **issuer URL** हुनेछ `https://<app-fqdn>`, जस्तै `https://my-mcp-app.eastus.azurecontainerapps.io`। यसको OAuth2 एन्डपोइन्टहरू:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – क्लाइन्टहरूले यहाँबाट टोकन प्राप्त गर्छन् (client_credentials फ्लो)।
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – JWK सेट फर्काउँछ (APIM ले साइनिङ कीहरू प्राप्त गर्न प्रयोग गर्छ)।
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC डिस्कभरी JSON (जसमा `issuer`, `token_endpoint`, `jwks_uri` आदि हुन्छन्)।  

APIM ले **OpenID configuration URL** तर्फ इशारा गर्नेछ, जहाँबाट यसले `jwks_uri` पत्ता लगाउँछ। उदाहरणका लागि, यदि तपाईंको Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` हो भने, APIM को `<openid-config url="...">` यसरी हुनुपर्छ: `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`। (डिफल्ट रूपमा Spring ले उक्त मेटाडाटामा `issuer` लाई सोही आधार URL मा सेट गर्छ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) कन्फिगर गर्ने

Azure APIM मा, इनबाउन्ड पोलिसी थप्नुहोस् जसले `<validate-jwt>` प्रयोग गरेर आउने JWT हरूलाई तपाईंको Spring Authorization Server विरुद्ध जाँच गर्छ। सरल सेटअपका लागि OpenID Connect मेटाडाटा URL प्रयोग गर्न सकिन्छ। उदाहरण पोलिसी स्निपेट:

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

यस पोलिसीले APIM लाई Spring Auth Server बाट OpenID कन्फिगरेसन ल्याउन, यसको JWKS प्राप्त गर्न, र प्रत्येक टोकनलाई विश्वसनीय कीद्वारा हस्ताक्षर गरिएको छ कि छैन र सही audience छ कि छैन भनेर जाँच गर्न निर्देशन दिन्छ। (`<issuers>` नदिएमा, APIM ले मेटाडाटाबाट `issuer` क्लेम स्वचालित रूपमा प्रयोग गर्छ।) `<audience>` ले तपाईंको क्लाइन्ट ID वा API स्रोत पहिचानकर्तासँग मेल खानुपर्छ (माथिको उदाहरणमा `"mcp-client"` सेट गरिएको छ)। यो Microsoft को `validate-jwt` र `<openid-config>` प्रयोग गर्ने डकुमेन्टेसनसँग मेल खान्छ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))।

प्रमाणीकरण पछि, APIM ले अनुरोध (मूल `Authorization` हेडर सहित) ब्याकएन्डमा फर्वार्ड गर्नेछ। Spring एप पनि रिसोर्स सर्भर भएकाले टोकन पुनः प्रमाणीकरण गर्नेछ, तर APIM ले पहिले नै यसको वैधता सुनिश्चित गरिसकेको हुन्छ। (डेभलपमेन्टका लागि, तपाईं APIM को जाँचमा भर पर्न सक्नुहुन्छ र एपमा थप जाँचहरू अक्षम गर्न सक्नुहुन्छ, तर दुवै राख्नु सुरक्षित हुन्छ।)

## उदाहरण सेटिङहरू

| सेटिङ              | उदाहरण मान                                                        | टिप्पणी                                      |
|--------------------|------------------------------------------------------------------|----------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                | तपाईंको Container App को URL (आधार URI)      |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | डिफल्ट Spring टोकन एन्डपोइन्ट ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | डिफल्ट JWK सेट एन्डपोइन्ट ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC डिस्कभरी डकुमेन्ट (स्वतः उत्पन्न)       |
| **APIM audience**  | `mcp-client`                                                     | OAuth क्लाइन्ट ID वा API स्रोत नाम           |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` यस URL प्रयोग गर्छ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## सामान्य समस्याहरू

- **HTTPS/TLS:** APIM गेटवेले OpenID/JWKS एन्डपोइन्ट HTTPS र मान्य प्रमाणपत्र भएको हुनुपर्नेछ। डिफल्ट रूपमा Azure Container Apps ले Azure-प्रबन्धित डोमेनका लागि विश्वसनीय TLS प्रमाणपत्र प्रदान गर्छ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। यदि तपाईं कस्टम डोमेन प्रयोग गर्नुहुन्छ भने, प्रमाणपत्र बाँध्न निश्चित गर्नुहोस् (Azure को निःशुल्क प्रबन्धित प्रमाणपत्र सुविधा प्रयोग गर्न सक्नुहुन्छ) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। यदि APIM ले एन्डपोइन्टको प्रमाणपत्रमा विश्वास गर्न सकेन भने `<validate-jwt>` मेटाडाटा ल्याउन असफल हुनेछ।  

- **एन्डपोइन्ट पहुँचयोग्यता:** Spring एपका एन्डपोइन्टहरू APIM बाट पहुँचयोग्य हुनुपर्छ। `--ingress external` प्रयोग गर्नु (वा पोर्टलमा इन्ग्रेस सक्षम गर्नु) सबैभन्दा सजिलो हो। यदि तपाईंले आन्तरिक वा vNet-सम्बन्धित वातावरण रोज्नुभयो भने, APIM (डिफल्ट रूपमा सार्वजनिक) ले त्यहाँ पुग्न नपाउन सक्छ जबसम्म दुवै एउटै VNet मा राखिएको छैन। टेस्ट सेटअपमा, सार्वजनिक इन्ग्रेस रोज्नुहोस् ताकि APIM ले `.well-known` र `/jwks` URL हरू कल गर्न सकोस्। 

- **OpenID डिस्कभरी सक्षम:** डिफल्ट रूपमा Spring Authorization Server ले `/.well-known/openid-configuration` एक्स्पोज गर्दैन जबसम्म OIDC सक्षम गरिएको छैन। `.oidc(Customizer.withDefaults())` तपाईंको सुरक्षा कन्फिगमा समावेश गर्न निश्चित गर्नुहोस् (माथि देखाइएको जस्तै) ताकि प्रदायक कन्फिगरेसन एन्डपोइन्ट सक्रिय होस् ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))। नत्र APIM को `<openid-config>` कलले 404 फर्काउनेछ।

- **Audience क्लेम:** Spring को डिफल्ट व्यवहारले `aud` क्लेमलाई क्लाइन्ट ID मा सेट गर्छ। यदि APIM को `<audience>` जाँच असफल भयो भने, तपाईंले टोकन अनुकूलन गर्नुपर्ने हुन सक्छ (माथि देखाइएको जस्तै) वा APIM पोलिसी समायोजन गर्नुपर्ने हुन सक्छ। JWT मा audience तपाईंले `<audience>` मा सेट गरेको मानसँग मेल खानुपर्छ। 

- **JSON मेटाडाटा पार्सिङ:** OpenID कन्फिगरेसन JSON मान्य हुनुपर्छ। Spring को डिफल्ट कन्फिगले मानक OIDC मेटाडाटा डकुमेन्ट निकाल्छ। यसमा सही `issuer` र `jwks_uri` समावेश छ कि छैन जाँच गर्नुहोस्। यदि तपाईं Spring लाई प्रोक्सी वा पाथ-आधारित रुट पछाडि होस्ट गर्दै हुनुहुन्छ भने, यस मेटाडाटामा URL हरू ठीक छन् कि छैनन् दोहोरो जाँच गर्नुहोस्। APIM ले यी मानहरू जस्तै छन् त्यस्तै प्रयोग गर्नेछ। 

- **पोलिसी क्रम:** APIM पोलिसीमा `<validate-jwt>` लाई ब्याकएन्डमा रुटिङ गर्नु अघि राख्नुहोस्। नत्र, कलहरू टोकन बिना नै तपाईंको एपमा पुग्न सक्छन्। साथै `<validate-jwt>` लाई `<inbound>` भित्र तुरुन्तै राख्नुहोस् (अर्को सर्त भित्र नेस्ट नगरिकन) ताकि APIM ले यसलाई लागू गरोस्।

माथिका चरणहरू पालना गरेर, तपाईं आफ्नो Spring AI MCP सर्भर Azure Container Apps मा चलाउन सक्नुहुन्छ र Azure API Management मार्फत आउने OAuth2 JWT हरूलाई न्यूनतम पोलिसीका साथ प्रमाणीकरण गर्न सक्नुहुन्छ। मुख्य कुरा: Spring Auth एन्डपोइन्टहरू TLS सहित सार्वजनिक रूपमा उपलब्ध गराउनुहोस्, OIDC डिस्कभरी सक्षम गर्नुहोस्, र APIM को `validate-jwt` लाई OpenID कन्फिग URL तर्फ निर्देशित गर्नुहोस् (यसले JWKS स्वचालित रूपमा ल्याउन सक्छ)। यो सेटअप डेभ/टेस्ट वातावरणका लागि उपयुक्त छ; प्रोडक्सनका लागि उचित सिक्रेट व्यवस्थापन, टोकनको आयु, र JWKS मा कुञ्जीहरू घुमाउने कुरा विचार गर्नुहोस्।
**सन्दर्भहरू:** डिफल्ट एन्डपोइन्टहरूको लागि Spring Authorization Server कागजातहरू हेर्नुहोस् ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) र OIDC कन्फिगरेसन ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` का उदाहरणहरूको लागि Microsoft APIM कागजातहरू हेर्नुहोस् ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); र डिप्लोयमेन्ट र प्रमाणपत्रहरूको लागि Azure Container Apps कागजातहरू हेर्नुहोस् ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।