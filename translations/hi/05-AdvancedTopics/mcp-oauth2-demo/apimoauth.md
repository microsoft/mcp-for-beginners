# Spring AI MCP ऐप को Azure Container Apps पर डिप्लॉय करना

([Spring AI MCP सर्वर को OAuth2 के साथ सुरक्षित करना](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *चित्र: Spring Authorization Server के साथ सुरक्षित Spring AI MCP सर्वर। सर्वर क्लाइंट्स को एक्सेस टोकन जारी करता है और आने वाले अनुरोधों पर उन्हें वैधता प्रदान करता है (स्रोत: Spring ब्लॉग) ([Spring AI MCP सर्वर को OAuth2 के साथ सुरक्षित करना](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP सर्वर को डिप्लॉय करने के लिए, इसे कंटेनर के रूप में बनाएं और Azure Container Apps का उपयोग करें जिसमें बाहरी इनग्रैस हो। उदाहरण के लिए, Azure CLI का उपयोग करके आप चला सकते हैं:

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

यह एक सार्वजनिक रूप से सुलभ Container App बनाता है जिसमें HTTPS सक्षम होता है (Azure डिफ़ॉल्ट `*.azurecontainerapps.io` डोमेन के लिए मुफ्त TLS प्रमाणपत्र जारी करता है ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). कमांड आउटपुट में ऐप का FQDN शामिल होता है (जैसे `my-mcp-app.eastus.azurecontainerapps.io`), जो **issuer URL** बेस बन जाता है। सुनिश्चित करें कि HTTP इनग्रैस सक्षम है (जैसा ऊपर बताया गया है) ताकि APIM ऐप तक पहुंच सके। टेस्ट/डेव सेटअप में, `--ingress external` विकल्प का उपयोग करें (या TLS के साथ कस्टम डोमेन बाइंड करें जैसा कि [Microsoft डॉक](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) में बताया गया है ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)))। किसी भी संवेदनशील प्रॉपर्टी (जैसे OAuth क्लाइंट सीक्रेट्स) को Container Apps secrets या Azure Key Vault में स्टोर करें, और उन्हें कंटेनर में पर्यावरण चर के रूप में मैप करें।

## Spring Authorization Server को कॉन्फ़िगर करना

अपने Spring Boot ऐप के कोड में, Spring Authorization Server और Resource Server स्टार्टर शामिल करें। एक `RegisteredClient` कॉन्फ़िगर करें (डेव/टेस्ट में `client_credentials` ग्रांट के लिए) और एक JWT की सोर्स सेट करें। उदाहरण के लिए, `application.properties` में आप सेट कर सकते हैं:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server और Resource Server को सक्षम करने के लिए एक सुरक्षा फ़िल्टर चेन परिभाषित करें। उदाहरण के लिए:

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

यह सेटअप डिफ़ॉल्ट OAuth2 एंडपॉइंट्स को एक्सपोज़ करेगा: `/oauth2/token` टोकन के लिए और `/oauth2/jwks` JSON वेब की सेट के लिए। (डिफ़ॉल्ट रूप से Spring का `AuthorizationServerSettings` `/oauth2/token` और `/oauth2/jwks` को मैप करता है ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) सर्वर RSA की द्वारा साइन किए गए JWT एक्सेस टोकन जारी करेगा, और इसका सार्वजनिक की `https://<your-app>:/oauth2/jwks` पर प्रकाशित करेगा।

**OpenID Connect डिस्कवरी सक्षम करें:** APIM को issuer और JWKS स्वचालित रूप से प्राप्त करने देने के लिए, अपनी सुरक्षा कॉन्फ़िगरेशन में `.oidc(Customizer.withDefaults())` जोड़ें ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))। उदाहरण के लिए:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

यह `/.well-known/openid-configuration` को एक्सपोज़ करता है, जिसका उपयोग APIM मेटाडेटा के लिए कर सकता है। अंत में, आप JWT **audience** क्लेम को कस्टमाइज़ करना चाह सकते हैं ताकि APIM का `<audiences>` चेक पास हो जाए। उदाहरण के लिए, एक टोकन कस्टमाइज़र जोड़ें:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

यह सुनिश्चित करता है कि टोकन में `"aud": ["mcp-client"]` हो, जो APIM द्वारा अपेक्षित क्लाइंट ID या स्कोप से मेल खाता है।

## टोकन और JWKS एंडपॉइंट्स को एक्सपोज़ करना

डिप्लॉयमेंट के बाद, आपके ऐप का **issuer URL** होगा `https://<app-fqdn>`, जैसे `https://my-mcp-app.eastus.azurecontainerapps.io`। इसके OAuth2 एंडपॉइंट्स हैं:

- **टोकन एंडपॉइंट:** `https://<app-fqdn>/oauth2/token` – क्लाइंट्स यहां से टोकन प्राप्त करते हैं (client_credentials फ्लो)।
- **JWKS एंडपॉइंट:** `https://<app-fqdn>/oauth2/jwks` – JWK सेट लौटाता है (APIM सिग्निंग कीज़ प्राप्त करने के लिए उपयोग करता है)।
- **OpenID कॉन्फ़िग:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC डिस्कवरी JSON (जिसमें `issuer`, `token_endpoint`, `jwks_uri` आदि होते हैं)।

APIM **OpenID कॉन्फ़िगरेशन URL** की ओर पॉइंट करेगा, जहां से यह `jwks_uri` खोजता है। उदाहरण के लिए, यदि आपका Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` है, तो APIM का `<openid-config url="...">` उपयोग करना चाहिए `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`। (डिफ़ॉल्ट रूप से Spring उस मेटाडेटा में `issuer` को उसी बेस URL पर सेट करता है ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))।

## Azure API Management (`validate-jwt`) को कॉन्फ़िगर करना

Azure APIM में, एक इनबाउंड पॉलिसी जोड़ें जो `<validate-jwt>` पॉलिसी का उपयोग करके आपके Spring Authorization Server के खिलाफ आने वाले JWTs की जांच करे। एक सरल सेटअप के लिए, आप OpenID Connect मेटाडेटा URL का उपयोग कर सकते हैं। उदाहरण पॉलिसी स्निपेट:

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

यह पॉलिसी APIM को Spring Auth Server से OpenID कॉन्फ़िगरेशन प्राप्त करने, उसका JWKS लाने, और यह सत्यापित करने के लिए कहती है कि प्रत्येक टोकन एक विश्वसनीय की द्वारा साइन किया गया है और उसमें सही audience है। (यदि आप `<issuers>` छोड़ देते हैं, तो APIM मेटाडेटा से `issuer` क्लेम का स्वचालित उपयोग करेगा।) `<audience>` को आपके क्लाइंट ID या API रिसोर्स आइडेंटिफायर से मेल खाना चाहिए (उपरोक्त उदाहरण में, हमने इसे `"mcp-client"` सेट किया है)। यह Microsoft के `validate-jwt` के साथ `<openid-config>` उपयोग करने के दस्तावेज़ के अनुरूप है ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))।

सत्यापन के बाद, APIM अनुरोध (मूल `Authorization` हेडर सहित) को बैकएंड को अग्रेषित करेगा। चूंकि Spring ऐप भी एक रिसोर्स सर्वर है, यह टोकन को पुनः सत्यापित करेगा, लेकिन APIM पहले ही इसकी वैधता सुनिश्चित कर चुका होगा। (डेवलपमेंट के लिए, आप APIM के चेक पर भरोसा कर सकते हैं और ऐप में अतिरिक्त चेक को अक्षम कर सकते हैं, लेकिन दोनों को रखना सुरक्षित होता है।)

## उदाहरण सेटिंग्स

| सेटिंग            | उदाहरण मान                                                        | नोट्स                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | आपके Container App का URL (बेस URI)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | डिफ़ॉल्ट Spring टोकन एंडपॉइंट ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | डिफ़ॉल्ट JWK सेट एंडपॉइंट ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC डिस्कवरी डॉक्यूमेंट (स्वतः जनरेटेड)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth क्लाइंट ID या API रिसोर्स नाम       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` इस URL का उपयोग करता है ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## सामान्य समस्याएं

- **HTTPS/TLS:** APIM गेटवे को OpenID/JWKS एंडपॉइंट HTTPS के साथ वैध प्रमाणपत्र के साथ चाहिए। डिफ़ॉल्ट रूप से, Azure Container Apps Azure-मैनेज्ड डोमेन के लिए विश्वसनीय TLS सर्टिफिकेट प्रदान करता है ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। यदि आप कस्टम डोमेन का उपयोग करते हैं, तो प्रमाणपत्र बाइंड करना सुनिश्चित करें (आप Azure के मुफ्त मैनेज्ड सर्ट फीचर का उपयोग कर सकते हैं) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। यदि APIM एंडपॉइंट के प्रमाणपत्र पर भरोसा नहीं कर पाता, तो `<validate-jwt>` मेटाडेटा प्राप्त करने में विफल होगा।

- **एंडपॉइंट पहुंच:** सुनिश्चित करें कि Spring ऐप के एंडपॉइंट्स APIM से पहुंच योग्य हों। `--ingress external` (या पोर्टल में इनग्रैस सक्षम करना) सबसे सरल है। यदि आपने आंतरिक या vNet-बाउंड वातावरण चुना है, तो APIM (जो डिफ़ॉल्ट रूप से सार्वजनिक है) उसे तब तक नहीं पहुंच पाएगा जब तक कि वे एक ही VNet में न हों। टेस्ट सेटअप में, सार्वजनिक इनग्रैस प्राथमिकता दें ताकि APIM `.well-known` और `/jwks` URLs को कॉल कर सके।

- **OpenID डिस्कवरी सक्षम:** डिफ़ॉल्ट रूप से, Spring Authorization Server `/.well-known/openid-configuration` को **एक्सपोज़ नहीं करता** जब तक कि OIDC सक्षम न हो। सुनिश्चित करें कि आपने `.oidc(Customizer.withDefaults())` अपनी सुरक्षा कॉन्फ़िग में शामिल किया है (जैसा ऊपर बताया गया है) ताकि प्रदाता कॉन्फ़िगरेशन एंडपॉइंट सक्रिय हो ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))। अन्यथा APIM का `<openid-config>` कॉल 404 देगा।

- **Audience क्लेम:** Spring का डिफ़ॉल्ट व्यवहार `aud` क्लेम को क्लाइंट ID पर सेट करना है। यदि APIM का `<audience>` चेक विफल होता है, तो आपको टोकन को कस्टमाइज़ करना पड़ सकता है (जैसा ऊपर दिखाया गया है) या APIM पॉलिसी को समायोजित करना पड़ सकता है। सुनिश्चित करें कि आपके JWT में audience वही हो जो आप `<audience>` में कॉन्फ़िगर करते हैं।

- **JSON मेटाडेटा पार्सिंग:** OpenID कॉन्फ़िगरेशन JSON मान्य होना चाहिए। Spring का डिफ़ॉल्ट कॉन्फ़िग एक मानक OIDC मेटाडेटा डॉक्यूमेंट जारी करेगा। जांचें कि इसमें सही `issuer` और `jwks_uri` शामिल हैं। यदि आप Spring को प्रॉक्सी या पाथ-आधारित रूट के पीछे होस्ट करते हैं, तो URLs को इस मेटाडेटा में दोबारा जांचें। APIM इन्हें वैसे ही उपयोग करेगा।

- **पॉलिसी क्रम:** APIM पॉलिसी में, `<validate-jwt>` को बैकएंड रूटिंग से **पहले** रखें। अन्यथा, कॉल्स बिना वैध टोकन के आपके ऐप तक पहुंच सकते हैं। साथ ही सुनिश्चित करें कि `<validate-jwt>` सीधे `<inbound>` के अंदर हो (किसी अन्य कंडीशन के अंदर नेस्टेड न हो) ताकि APIM इसे लागू करे।

उपरोक्त चरणों का पालन करके, आप अपने Spring AI MCP सर्वर को Azure Container Apps में चला सकते हैं और Azure API Management के साथ आने वाले OAuth2 JWTs को न्यूनतम पॉलिसी के साथ वैध करवा सकते हैं। मुख्य बिंदु हैं: Spring Auth एंडपॉइंट्स को TLS के साथ सार्वजनिक रूप से एक्सपोज़ करना, OIDC डिस्कवरी सक्षम करना, और APIM के `validate-jwt` को OpenID कॉन्फ़िग URL की ओर पॉइंट करना (ताकि यह JWKS स्वचालित रूप से प्राप्त कर सके)। यह सेटअप डेवलपमेंट/टेस्ट वातावरण के लिए उपयुक्त है; प्रोडक्शन के लिए उचित सीक्रेट प्रबंधन, टोकन की लाइफटाइम, और JWKS में की रोटेशन पर विचार करें।
**References:** Spring Authorization Server डॉक्यूमेंट्स में डिफ़ॉल्ट endpoints देखें ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) और OIDC कॉन्फ़िगरेशन ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); Microsoft APIM डॉक्यूमेंट्स में `validate-jwt` उदाहरण देखें ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); और Azure Container Apps डॉक्यूमेंट्स में डिप्लॉयमेंट और सर्टिफिकेट्स के लिए देखें ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।