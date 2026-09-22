# Spring AI MCP अॅप Azure Container Apps मध्ये तैनात करणे

> [!WARNING]
> हा संमिश्रित प्राधिकरण/संसाधन सर्व्हर शिकण्याच्या आणि विकास/चाचणीसाठी वापरासाठी आहे. उत्पादन प्रणालींसाठी समर्पित ओळख पुरवठादार,
> कायमस्वरूपी साइनिंग कीज आणि व्यवस्थापित गुपित साठ्यात संग्रहित प्रमाणपत्रे वापरावी.
> 

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *आकृती: Spring Authorization Server सह सुरक्षित केलेला Spring AI MCP सर्व्हर. सर्व्हर ग्राहकांना प्रवेश टोकन जारी करतो आणि येणाऱ्या विनंत्यांवर त्याची पडताळणी करतो (स्रोत: Spring ब्लॉग) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP सर्व्हर तैनात करण्यासाठी ते कंटेनर म्हणून तयार करा आणि Azure Container Apps सह बाह्य प्रवेश वापरा. उदाहरणार्थ, Azure CLI वापरून आपण चालवू शकता:

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

हे एक सार्वजनिकरित्या प्रवेशयोग्य कंटेनर अॅप तयार करते ज्यात HTTPS सक्षम केलेले असते (Azure `*.azurecontainerapps.io` डोमेनसाठी विनामूल्य TLS प्रमाणपत्र जारी करते ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). आदेशाच्या आउटपुटमध्ये अॅपची FQDN समाविष्ट असते (उदा. `my-mcp-app.eastus.azurecontainerapps.io`), जी **issuer URL** बेस बनते. APIM अॅपपर्यंत पोहोचू शकण्यासाठी HTTP प्रवेश सक्षम असल्याची खात्री करा (वरप्रमाणे). चाचणी/विकास सेटअपने, `--ingress external` पर्याय वापरा (किंवा TLS सह सानुकूल डोमेन बांधणी करा [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). कोणत्याही संवेदनशील वैशिष्ट्यांना (जसे OAuth क्लायंट रहस्ये) Container Apps चे गुपित किंवा Azure Key Vault मध्ये संग्रहित करा, आणि त्यांना पर्यावरणीय चल म्हणून कंटेनरमध्ये नकाशित करा.

## Spring Authorization Server चे कॉन्फिगरेशन

आपल्या Spring Boot अॅपच्या कोडमध्ये Spring Authorization Server आणि Resource Server स्टार्टर समाविष्ट करा. `RegisteredClient` (dev/test मध्ये `client_credentials` ग्रॅंटसाठी) आणि JWT की स्रोत कॉन्फिगर करा. उदाहरणार्थ, `application.properties` मध्ये आपण सेट करू शकता:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

सुरक्षेचा फिल्टर चेन परिभाषित करून Authorization Server आणि Resource Server सक्षम करा. उदाहरणार्थ:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // प्रमाणन सर्व्हर एंडपॉइंट्स सक्षम करा
            .apply(authzServer.and())
            // रिसोर्स सर्व्हर सक्षम करा (आगमन विनंत्यांवर JWT सत्यापित करा)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF अक्षम करा (MCP सर्व्हर ब्राउझर-आधारित नाही)
            .csrf(csrf -> csrf.disable())
            // क्लायंट डेमो टूल्ससाठी CORS अनुमति द्या
            .cors(withDefaults());
        return http.build();
    }

    // इन-मेमरी क्लायंट (RegisteredClient) आणि JWK स्रोत परिभाषित करा:
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
        // RSA की तयार करा (डेव्ह/टेस्टसाठी, स्टार्टअपवर नवीन तयार करा)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

हा सेटअप डीफॉल्ट OAuth2 एंडपॉइंट्स उघडेल: टोकन्ससाठी `/oauth2/token` आणि JSON Web Key Set साठी `/oauth2/jwks`. (डीफॉल्टनुसार Spring चा `AuthorizationServerSettings` `/oauth2/token` आणि `/oauth2/jwks` ला नकाशित करतो ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) सर्व्हर RSA कीने स्वाक्षरी केलेले JWT प्रवेश टोकन्स जारी करेल, आणि त्याची सार्वजनिक की `https://<your-app>:/oauth2/jwks` वर प्रसिद्ध करेल.

**OpenID Connect शोध सक्षम करा:** APIM ला स्वयंचलितपणे issuer आणि JWKS मिळवण्यासाठी, आपली सुरक्षा कॉन्फिगरेशनमध्ये `.oidc(Customizer.withDefaults())` जोडून OIDC प्रदाता कॉन्फिगरेशन एंडपॉइंट सक्षम करा ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). उदाहरणार्थ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration सक्षम करते
```

हे `/.well-known/openid-configuration` सार्वजनिक करते, जे APIM मेटाडेटासाठी वापरू शकतो. शेवटी, आपण JWT चे **audience** दावा कस्टमाइझ करू इच्छित असाल ज्यामुळे APIM च्या `<audiences>` तपासणीत पास होईल. उदाहरणार्थ, एक टोकन कस्टमाइजर जोडा:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // सानुकूल प्रेक्षक सेट करा (उदा. क्लायंट आयडी किंवा API ओळखपत्र)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

हे सुनिश्चित करते की टोकन्स मध्ये `"aud": ["mcp-client"]` असे असेल, जे APIM कडून अपेक्षित क्लायंट ID किंवा स्कोपशी जुळते.

## टोकन आणि JWKS एंडपॉइंट्स उघडणे

तैनात केल्यानंतर, आपल्या अॅपचा **issuer URL** असेल `https://<app-fqdn>`, उदा. `https://my-mcp-app.eastus.azurecontainerapps.io`. त्याचे OAuth2 एंडपॉइंट्स आहेत:

- **टोकन एंडपॉइंट:** `https://<app-fqdn>/oauth2/token` – येथे क्लायंट्स टोकन्स प्राप्त करतात (client_credentials प्रवाह).
- **JWKS एंडपॉइंट:** `https://<app-fqdn>/oauth2/jwks` – JWK सेट परत करते (APIM साठी साइनिंग की मिळवण्यासाठी वापरली जाते).
- **OpenID कॉन्फिग:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC शोध JSON (यामध्ये `issuer`, `token_endpoint`, `jwks_uri`, इत्यादी असतात).  

APIM **OpenID कॉन्फिगरेशन URL** कडे निर्देश करेल, ज्यापासून हे `jwks_uri` शोधते. उदाहरणार्थ, जर आपला कंटेनर अॅप FQDN `my-mcp-app.eastus.azurecontainerapps.io` असेल, तर APIM च्या `<openid-config url="...">` मध्ये `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` वापरावा. (डीफॉल्टनुसार Spring त्या मेटाडेटामध्ये समान बेस URL म्हणून `issuer` सेट करेल ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (APIM) मध्ये `validate-jwt` कॉन्फिगर करणे

Azure APIM मध्ये, इनबाउंड धोरणातील `<validate-jwt>` वापरून येणाऱ्या JWT वर आपल्या Spring Authorization Server विरुद्ध तपासणी करण्यासाठी एक धोरण जोडा. सोप्या सेटअपसाठी OpenID Connect मेटाडेटा URL वापरू शकता. धोरण स्निपेटचे उदाहरण:

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

हे धोरण APIM ला Spring Auth Server कडून OpenID कॉन्फिगरेशन मिळवण्यास, त्याचा JWKS मिळवण्यास आणि प्रत्येक टोकन एका विश्वासार्ह कीने स्वाक्षरी केले गेले आहे आणि योग्य audience आहे का हे पडताळण्यास सांगते. (जर `<issuers>` वगळले तर APIM मेटाडेटातून आपोआप `issuer` दावा वापरेल.) `<audience>` हा टोकनमधील क्लायंट ID किंवा API संसाधन ओळखीस जुळला पाहिजे (वरील उदाहरणात, आम्ही `"mcp-client"` म्हणून सेट केले आहे). हे Microsoft च्या `<openid-config>` सह `validate-jwt` वापरण्याच्या दस्तऐवजात सुसंगत आहे ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

पडताळणी नंतर, APIM विनंती (मूळ `Authorization` हेडरसह) बॅकएंडकडे पुढे पाठवेल. Spring अॅप देखील एक Resource Server असल्यामुळे, तो टोकन पुन्हा पडताळेल, पण APIM आधीच त्याची वैधता सुनिश्चित केली आहे. (विकासासाठी, तुम्ही APIM ची पडताळणीवर अवलंबून राहू शकता आणि अॅपमधील अतिरिक्त पडताळण्या अक्षम करू शकता, परंतु दोन्ही ठेवणे सुरक्षित आहे.)

## उदाहरण सेटिंग्ज

| सेटिंग              | उदाहरण मूल्य                                                        | टीप्स                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | आपल्या Container App ची URL (बेस URI)       |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | डीफॉल्ट Spring टोकन एंडपॉइंट ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | डीफॉल्ट JWK सेट एंडपॉइंट ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC शोध दस्तऐवज (स्वयंनिर्मित)              |
| **APIM audience**  | `mcp-client`                                                         | OAuth क्लायंट ID किंवा API संसाधन नाव        |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` हा URL वापरतो ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## सामान्य चुका

- **HTTPS/TLS:** APIM गेटवेसाठी OpenID/JWKS एंडपॉइंट HTTPS सह वैध प्रमाणपत्र असणे आवश्यक आहे. डीफॉल्टनुसार Azure Container Apps या Azure-व्यवस्थापित डोमेनसाठी विश्वासार्ह TLS प्रमाणपत्र प्रदान करतो ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). जर तुम्ही सानुकूल डोमेन वापरत असाल तर प्रमाणपत्र बांधणी करणे आवश्यक आहे (Azure ची विनामूल्य व्यवस्थापित प्रमाणपत्र वैशिष्ट्य वापरू शकता) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). जर APIM त्या प्रमाणपत्रावर विश्वास ठेवू शकत नसेल, तर `<validate-jwt>` मेटाडेटा मिळवण्यात अयशस्वी होईल.

- **एंडपॉइंट प्रवेशयोग्यता:** Spring अॅपचे एंडपॉइंट APIM कडून पोहोचता येण्यासारखे असावेत. `--ingress external` वापरणे (किंवा पोर्टलमध्ये प्रवेश सक्षम करणे) सर्वात सोपे आहे. जर तुम्ही आतील किंवा vNet-बाउंड वातावरण निवडले असेल, तर APIM (डीफॉल्टनुसार सार्वजनिक) त्याला पोहोचू शकत नाही जोपर्यंत ते एकाच VNet मध्ये नसेल. चाचणी सेटअपने, सार्वजनिक प्रवेश प्राधान्य द्या ज्यामुळे APIM `.well-known` आणि `/jwks` URLs कॉल करू शकेल.

- **OpenID शोध सक्षम:** डीफॉल्टनुसार, Spring Authorization Server `/.well-known/openid-configuration` उघडत नाही जोपर्यंत OIDC सक्षम केलेले नाही. आपल्या सुरक्षा कॉन्फिगरेशनमध्ये `.oidc(Customizer.withDefaults())` समाविष्ट करणे सुनिश्चित करा (वर पहा) ज्यामुळे प्रदाता कॉन्फिगरेशन एंडपॉइंट सक्रिय होतो ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). अन्यथा APIM चा `<openid-config>` कॉल 404 देईल.

- **Audience दावा:** Spring ची डीफॉल्ट विधान client ID साठी `aud` दावा सेट करणे आहे. जर APIM चा `<audience>` तपासणी अयशस्वी झाली, तर तुम्हाला वर दाखवल्याप्रमाणे टोकन कस्टमाइझ करणे किंवा APIM धोरण समायोजित करावे लागेल. तुमच्या JWT मध्ये audience ही `<audience>` मध्ये कॉन्फिगर केलेल्या संघटनेशी जुळली पाहिजे.

- **JSON मेटाडेटा पार्सिंग:** OpenID कॉन्फिगरेशन JSON वैध असणे आवश्यक आहे. Spring चा डीफॉल्ट कॉन्फिग सत्य OIDC मेटाडेटा दस्तऐवज दूर करेल. यात योग्य `issuer` आणि `jwks_uri` असल्याची खात्री करा. जर तुम्ही Spring चे प्रॉक्सी किंवा पाथ-आधारित रूटमागे होस्ट करत असाल, तर या मेटाडेटामधील URL पुन्हा तपासा. APIM ही मूल्ये तशीच वापरेल.

- **धोरण क्रमवारी:** APIM धोरणात, `<validate-jwt>` **बॅकएंडकडे कोणतेही रूटिंग होण्यापूर्वी** ठेवा. अन्यथा, कॉल्स वैध टोकन शिवाय तुमच्या अॅपपर्यंत पोहोचू शकतात. याशिवाय, `<validate-jwt>` `<inbound>` खाली थेट असावा (इतर स्थितीमध्ये नसावा) ज्यामुळे APIM तो लागू करते.

वर दिलेल्या टप्प्यांचे पालन करून, तुम्ही Azure Container Apps मध्ये तुमचा Spring AI MCP सर्व्हर चालवू शकता आणि Azure API Management आतील OAuth2 JWT पडताळणीसाठी कमी धोरण वापरू शकता. महत्वाच्या मुद्द्यांमध्ये आहेत: Spring Auth एंडपॉइंट्स सार्वजनिक TLS सह उघडणे, OIDC शोध सक्षम करणे, आणि APIM चा `validate-jwt` OpenID कॉन्फिग URL कडे निर्देश करणे (जे JWKS स्वयंचलितरीत्या मिळवू शकेल). हा सेटअप विकास/चाचणीसाठी योग्य आहे; उत्पादनासाठी, योग्य गुपित व्यवस्थापन, टोकन कालावधी, आणि आवश्यकतेनुसार JWKS मध्ये की फिरवणे विचार करा.


**संदर्भ:** डीफॉल्ट एंडपॉइंटसाठी Spring Authorization Server च्या दस्तऐवजांचा अभ्यास करा ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) आणि OIDC कॉन्फिगरेशन साठी ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` चे उदाहरणांसाठी Microsoft APIM दस्तऐवज पहा ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); आणि डिप्लॉयमेंट व सर्टिफिकेट साठी Azure Container Apps दस्तऐवज पहा ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->