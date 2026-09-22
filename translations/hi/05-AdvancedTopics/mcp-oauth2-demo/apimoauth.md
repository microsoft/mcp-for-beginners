# स्प्रिंग AI MCP ऐप को Azure कंटेनर ऐप्स पर डिप्लॉय करना

> [!WARNING]
> यह संयुक्त प्राधिकरण/संसाधन सर्वर सीखने और विकास/परीक्षण उपयोग के लिए है। प्रोडक्शन सिस्टम के लिए एक समर्पित पहचान प्रदाता,
> स्थायी साइनिंग कुंजियों, और प्रबंधित सीक्रेट स्टोर में संग्रहीत क्रेडेंशियल्स का उपयोग किया जाना चाहिए।




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

यह HTTPS सक्षम एक सार्वजनिक रूप से सुलभ कंटेनर ऐप बनाता है (Azure डिफ़ॉल्ट `*.azurecontainerapps.io` डोमेन के लिए एक मुफ्त TLS सर्टिफिकेट जारी करता है ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). कमांड आउटपुट में ऐप का FQDN शामिल होता है (जैसे `my-mcp-app.eastus.azurecontainerapps.io`), जो **issuer URL** बेस बन जाता है। सुनिश्चित करें कि HTTP इनग्रैस सक्षम है (जैसा ऊपर बताया गया) ताकि APIM ऐप तक पहुँच सके। परीक्षण/विकास सेटअप में, `--ingress external` विकल्प का उपयोग करें (या कस्टम डोमेन को TLS के साथ बाँधें जैसा कि [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)) में बताया गया है)। किसी भी संवेदनशील संपत्ति (जैसे OAuth क्लाइंट सीक्रेट) को कंटेनर ऐप्स के सीक्रेट्स या Azure Key Vault में संग्रहित करें, और उन्हें कंटेनर में पर्यावरण चर के रूप में मैप करें। 

## स्प्रिंग प्राधिकरण सर्वर कॉन्फ़िगर करना

अपने स्प्रिंग बूट ऐप की कोड में, स्प्रिंग प्राधिकरण सर्वर और संसाधन सर्वर स्टार्टर शामिल करें। एक `RegisteredClient` कॉन्फ़िगर करें (डेव/टेस्ट में `client_credentials` ग्रांट के लिए) और JWT कुंजी स्रोत दें। उदाहरण के लिए, `application.properties` में आप सेट कर सकते हैं:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

प्राधिकरण सर्वर और संसाधन सर्वर को एक सुरक्षा फ़िल्टर चेन परिभाषित करके सक्षम करें। उदाहरण के लिए:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // ऑथराइजेशन सर्वर एंडपॉइंट्स सक्षम करें
            .apply(authzServer.and())
            // रिसोर्स सर्वर सक्षम करें (आने वाले अनुरोधों पर JWT सत्यापित करें)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF अक्षम करें (MCP सर्वर ब्राउज़र-आधारित नहीं है)
            .csrf(csrf -> csrf.disable())
            // क्लाइंट डेमो टूल्स के लिए CORS की अनुमति दें
            .cors(withDefaults());
        return http.build();
    }

    // एक इन-मेमोरी क्लाइंट (RegisteredClient) और एक JWK स्रोत परिभाषित करें:
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
        // एक RSA कुंजी उत्पन्न करें (डेव/टेस्ट के लिए, स्टार्टअप पर नया उत्पन्न करें)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

यह सेटअप डिफ़ॉल्ट OAuth2 एंडपॉइंट्स को प्रदर्शित करेगा: `/oauth2/token` टोकन के लिए और `/oauth2/jwks` JSON वेब की सेट के लिए। (डिफ़ॉल्ट रूप से स्प्रिंग का `AuthorizationServerSettings` `/oauth2/token` और `/oauth2/jwks` को मैप करता है ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) सर्वर RSA कुंजी द्वारा हस्ताक्षरित JWT एक्सेस टोकन जारी करेगा, और अपना सार्वजनिक कुंजी `https://<your-app>:/oauth2/jwks` पर प्रकाशित करेगा। 

**OpenID Connect डिस्कवरी सक्षम करें:** APIM को स्वचालित रूप से issuer और JWKS प्राप्त करने देने के लिए अपने सुरक्षा कॉन्फ़िग में `.oidc(Customizer.withDefaults())` जोड़ें ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))। उदाहरण के लिए:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration सक्षम करता है
```

यह `/.well-known/openid-configuration` को एक्सपोज़ करता है, जिसे APIM मेटाडेटा के लिए उपयोग कर सकता है। अंत में, आप JWT के **audience** क्लेम को कस्टमाइज़ करना चाह सकते हैं ताकि APIM के `<audiences>` चेक पास हो जाए। उदाहरण के लिए, एक टोकन कस्टमाइजर जोड़ें:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // एक कस्टम ऑडियंस सेट करें (जैसे क्लाइंट आईडी या एपीआई पहचानकर्ता)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

यह सुनिश्चित करता है कि टोकन में `"aud": ["mcp-client"]` शामिल हो, जो APIM द्वारा अपेक्षित क्लाइंट ID या स्कोप से मेल खाता है। 

## टोकन और JWKS एंडपॉइंट्स को एक्सपोज़ करना

डिप्लॉय करने के बाद, आपके ऐप का **issuer URL** होगा `https://<app-fqdn>`, जैसे `https://my-mcp-app.eastus.azurecontainerapps.io`। इसके OAuth2 एंडपॉइंट्स हैं:

- **टोकन एंडपॉइंट:** `https://<app-fqdn>/oauth2/token` – क्लाइंट यहाँ से टोकन प्राप्त करते हैं (client_credentials फ्लो)।
- **JWKS एंडपॉइंट:** `https://<app-fqdn>/oauth2/jwks` – JWK सेट लौटाता है (APIM द्वारा साइनिंग कुंजियों को प्राप्त करने के लिए उपयोग किया जाता है)।
- **OpenID कॉन्फ़िग:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC डिस्कवरी JSON (जिसमें `issuer`, `token_endpoint`, `jwks_uri` आदि शामिल हैं)।  

APIM **OpenID कॉन्फ़िग URL** की ओर इंगित करेगा, जहां से यह `jwks_uri` खोजता है। उदाहरण के लिए, यदि आपका कंटेनर ऐप FQDN `my-mcp-app.eastus.azurecontainerapps.io` है, तो APIM का `<openid-config url="...">` होना चाहिए `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`। (डिफ़ॉल्ट रूप से स्प्रिंग वहाँ के मेटाडेटा में `issuer` को उसी बेस URL पर सेट करेगा ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) को कॉन्फ़िगर करना

Azure APIM में, एक inbound नीति जोड़ें जो `<validate-jwt>` नीति का उपयोग करके आने वाले JWTs को आपके स्प्रिंग प्राधिकरण सर्वर के खिलाफ जांचे। एक सरल सेटअप के लिए, आप OpenID Connect मेटाडेटा URL का उपयोग कर सकते हैं। नीति स्निपेट उदाहरण:

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

यह नीति APIM को Spring Auth Server से OpenID कॉन्फ़िगरेशन प्राप्त करने, उसका JWKS पुनः प्राप्त करने, और प्रत्येक टोकन की जांच करने के लिए कहती है कि वह एक भरोसेमंद कुंजी द्वारा हस्ताक्षरित है और उसमें सही audience है। (यदि आप `<issuers>` छोड़ देते हैं, तो APIM स्वतः ही मेटाडेटा से `issuer` क्लेम का उपयोग करेगा।) `<audience>` को आपके क्लाइंट ID या API संसाधन पहचानकर्ता से मेल खाना चाहिए (ऊपर के उदाहरण में, हमने इसे `"mcp-client"` सेट किया है)। यह Microsoft की `validate-jwt` के साथ `<openid-config>` उपयोग की डाक्यूमेंटेशन के अनुरूप है ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

सत्यापन के बाद, APIM अनुरोध को मूल `Authorization` हेडर सहित बैकएंड को आगे बढ़ाएगा। चूंकि स्प्रिंग ऐप भी एक संसाधन सर्वर है, यह टोकन को फिर से जांचेगा, लेकिन APIM ने पहले ही इसकी वैधता सुनिश्चित कर ली है। (विकास के लिए, आप APIM की जांच पर भरोसा कर सकते हैं और यदि चाहें तो ऐप में अतिरिक्त जांच निष्क्रिय कर सकते हैं, लेकिन दोनों रखना सुरक्षित होता है।)

## उदाहरण सेटिंग्स

| सेटिंग            | उदाहरण मान                                                        | टिप्पणियाँ                                   |
|--------------------|----------------------------------------------------------------------|---------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | आपके कंटेनर ऐप का URL (बेस URI)             |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | डिफॉल्ट स्प्रिंग टोकन एंडपॉइंट ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | डिफॉल्ट JWK सेट एंडपॉइंट ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC डिस्कवरी दस्तावेज़ (स्वतः-उत्पन्न)       |
| **APIM audience**  | `mcp-client`                                                         | OAuth क्लाइंट ID या API संसाधन नाम         |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` इस URL का उपयोग करता है ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## सामान्य गलतियाँ

- **HTTPS/TLS:** APIM गेटवे को OpenID/JWKS एंडपॉइंट HTTPS के साथ एक मान्य सर्टिफिकेट होना चाहिए। डिफ़ॉल्ट रूप से, Azure कंटेनर ऐप्स Azure द्वारा प्रबंधित डोमेन के लिए एक विश्वसनीय TLS सर्टिफिकेट प्रदान करता है ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). यदि आप कस्टम डोमेन उपयोग करते हैं, तो सुनिश्चित करें कि एक सर्टिफिकेट बाँधा गया हो (आप Azure की मुफ्त प्रबंधित सर्ट सुविधा का उपयोग कर सकते हैं) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))। यदि APIM एंडपॉइंट के सर्टिफिकेट पर भरोसा नहीं कर पाता है, तो `<validate-jwt>` मेटाडेटा प्राप्त करने में विफल होगा।  

- **एंडपॉइंट पहुँच:** सुनिश्चित करें कि स्प्रिंग ऐप के एंडपॉइंट APIM से सुलभ हों। `--ingress external` उपयोग करना (या पोर्टल में इनग्रैस सक्षम करना) सबसे सरल है। यदि आपने आंतरिक या vNet-बंधित पर्यावरण चुना है, तो APIM (डिफ़ॉल्ट रूप से सार्वजनिक) इसे तब तक नहीं पहुंच पाएगा जब तक कि उसे उसी VNet में न रखा जाए। परीक्षण सेटअप में, सार्वजनिक इनग्रैस को प्राथमिकता दें ताकि APIM `.well-known` और `/jwks` URLs को कॉल कर सके। 

- **OpenID डिस्कवरी सक्षम:** डिफ़ॉल्ट रूप से, स्प्रिंग प्राधिकरण सर्वर `/.well-known/openid-configuration` एक्सपोज़ **नहीं करता** जब तक OIDC सक्षम न हो। सुनिश्चित करें कि सुरक्षा कॉन्फ़िग में `.oidc(Customizer.withDefaults())` शामिल करें (जैसा ऊपर दिखाया गया) ताकि प्रदाता कॉन्फ़िगरेशन एंडपॉइंट सक्रिय हो ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))। अन्यथा APIM का `<openid-config>` कॉल 404 देगा।

- **Audience क्लेम:** स्प्रिंग की डिफ़ॉल्ट व्यवहार `aud` क्लेम को क्लाइंट ID पर सेट करना है। यदि APIM के `<audience>` चेक फेल होते हैं, तो आपको टोकन को कस्टमाइज़ करना पड़ सकता है (जैसा ऊपर दिखाया गया है) या APIM नीति समायोजित करनी पड़ सकती है। सुनिश्चित करें कि JWT में audience वही हो जो आप `<audience>` में कॉन्फ़िगर करते हैं। 

- **JSON मेटाडेटा पार्सिंग:** OpenID कॉन्फ़िगरेशन JSON मान्य होना चाहिए। स्प्रिंग की डिफ़ॉल्ट कॉन्फ़िग एक मानक OIDC मेटाडेटा दस्तावेज़ उत्पन्न करेगी। सत्यापित करें कि इसमें सही `issuer` और `jwks_uri` हो। यदि आप स्प्रिंग को प्रॉक्सी या पाथ-आधारित रूट के पीछे होस्ट करते हैं, तो इस मेटाडेटा में URLs को दोबारा जांचें। APIM इन्हें वैसे ही उपयोग करेगा। 

- **नीति क्रम:** APIM नीति में, `<validate-jwt>` को बैकएंड को रूटिंग करने से **पहले** रखें। अन्यथा, कॉल बिना वैध टोकन के आपके ऐप तक पहुँच सकते हैं। यह भी सुनिश्चित करें कि `<validate-jwt>` तुरंत `<inbound>` के अंतर्गत हो (किसी अन्य कंडीशन के अंदर नहीं) ताकि APIM इसे लागू कर सके।

उपरोक्त चरणों का पालन करके, आप अपने स्प्रिंग AI MCP सर्वर को Azure कंटेनर ऐप्स में चला सकते हैं और Azure API Management को आ रहे OAuth2 JWTs को एक न्यूनतमतम नीति से मान्य करने दे सकते हैं। मुख्य बिंदु हैं: स्प्रिंग ऑथ एंडपॉइंट्स को TLS के साथ सार्वजनिक रूप से एक्सपोज़ करना, OIDC डिस्कवरी सक्षम करना, और APIM के `validate-jwt` को OpenID कॉन्फ़िगरेशन URL की ओर इशारा करना (जिससे वह JWKS स्वचालित रूप से प्राप्त कर सके)। यह सेटअप dev/test वातावरण के लिए उपयुक्त है; प्रोडक्शन में उचित सीक्रेट प्रबंधन, टोकन की जीवन अवधि, और JWKS में कुंजी घुमाव पर विचार करें। 


**संदर्भ:** डिफ़ॉल्ट एंडपॉइंट्स के लिए Spring Authorization Server दस्तावेज़ देखें ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) और OIDC कॉन्फ़िगरेशन ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` उदाहरणों के लिए Microsoft APIM दस्तावेज़ देखें ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); और परिनियोजन तथा प्रमाणपत्रों के लिए Azure Container Apps दस्तावेज़ देखें ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->