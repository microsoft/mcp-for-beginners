# Spring AI MCP अॅप Azure Container Apps मध्ये तैनात करणे

([Spring AI MCP सर्व्हर OAuth2 सह सुरक्षित करणे](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *आकृती: Spring Authorization Server सह सुरक्षित केलेला Spring AI MCP सर्व्हर. सर्व्हर क्लायंटसाठी access tokens जारी करतो आणि येणाऱ्या विनंत्यांवर त्यांची पडताळणी करतो (स्रोत: Spring ब्लॉग) ([Spring AI MCP सर्व्हर OAuth2 सह सुरक्षित करणे](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP सर्व्हर तैनात करण्यासाठी, त्याला कंटेनर म्हणून तयार करा आणि Azure Container Apps सह external ingress वापरा. उदाहरणार्थ, Azure CLI वापरून तुम्ही खालीलप्रमाणे चालवू शकता:

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

हे HTTPS सक्षम असलेले सार्वजनिकपणे प्रवेशयोग्य Container App तयार करते (Azure `*.azurecontainerapps.io` डोमेनसाठी मोफत TLS प्रमाणपत्र जारी करते ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). कमांड आउटपुटमध्ये अॅपचे FQDN (उदा. `my-mcp-app.eastus.azurecontainerapps.io`) समाविष्ट असते, जे **issuer URL** चा आधार बनते. HTTP ingress सक्षम असल्याची खात्री करा (वरीलप्रमाणे) जेणेकरून APIM अॅपपर्यंत पोहोचू शकेल. चाचणी/विकास सेटअपमध्ये, `--ingress external` पर्याय वापरा (किंवा TLS सह कस्टम डोमेन बाइंड करा [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). कोणत्याही संवेदनशील गुणधर्मांना (जसे की OAuth क्लायंट सीक्रेट्स) Container Apps secrets किंवा Azure Key Vault मध्ये साठवा आणि त्यांना कंटेनरमध्ये environment variables म्हणून मॅप करा.

## Spring Authorization Server चे कॉन्फिगरेशन

तुमच्या Spring Boot अॅपच्या कोडमध्ये, Spring Authorization Server आणि Resource Server starters समाविष्ट करा. `RegisteredClient` (dev/test मध्ये `client_credentials` ग्रांटसाठी) आणि JWT की स्रोत कॉन्फिगर करा. उदाहरणार्थ, `application.properties` मध्ये तुम्ही सेट करू शकता:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server आणि Resource Server सक्षम करण्यासाठी सुरक्षा फिल्टर चेन परिभाषित करा. उदाहरणार्थ:

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

हा सेटअप डिफॉल्ट OAuth2 endpoints उघडेल: `/oauth2/token` टोकन्ससाठी आणि `/oauth2/jwks` JSON Web Key Set साठी. (डिफॉल्टनुसार Spring चे `AuthorizationServerSettings` `/oauth2/token` आणि `/oauth2/jwks` मॅप करतात ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) सर्व्हर RSA कीने स्वाक्षरी केलेले JWT access tokens जारी करेल आणि त्याची सार्वजनिक की `https://<your-app>:/oauth2/jwks` येथे प्रकाशित करेल.

**OpenID Connect डिस्कव्हरी सक्षम करा:** APIM ला issuer आणि JWKS आपोआप मिळवता यावेत म्हणून, तुमच्या सुरक्षा कॉन्फिगरेशनमध्ये `.oidc(Customizer.withDefaults())` जोडा ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). उदाहरणार्थ:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

हे `/.well-known/openid-configuration` उघडेल, जे APIM मेटाडेटासाठी वापरू शकते. शेवटी, तुम्हाला JWT **audience** क्लेम सानुकूलित करायचा असेल तर APIM च्या `<audiences>` तपासणीसाठी तो जुळेल. उदाहरणार्थ, टोकन कस्टमायझर जोडा:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

हे सुनिश्चित करते की टोकन्समध्ये `"aud": ["mcp-client"]` असेल, जे APIM कडून अपेक्षित क्लायंट आयडी किंवा स्कोपशी जुळते.

## Token आणि JWKS Endpoints उघडणे

तैनाती नंतर, तुमच्या अॅपचा **issuer URL** असेल `https://<app-fqdn>`, उदा. `https://my-mcp-app.eastus.azurecontainerapps.io`. त्याचे OAuth2 endpoints:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – क्लायंट येथे टोकन्स मिळवतात (`client_credentials` फ्लो).
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – JWK सेट परत करते (APIM साठी साइनिंग की मिळवण्यासाठी).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC डिस्कव्हरी JSON (यामध्ये `issuer`, `token_endpoint`, `jwks_uri` इत्यादी असतात).

APIM **OpenID configuration URL** कडे निर्देशित होईल, जिथून ते `jwks_uri` शोधते. उदाहरणार्थ, जर तुमचा Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` असेल, तर APIM चा `<openid-config url="...">` वापरावा `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (डिफॉल्टनुसार Spring त्या मेटाडेटामध्ये `issuer` म्हणून तोच बेस URL सेट करतो ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) चे कॉन्फिगरेशन

Azure APIM मध्ये, `<validate-jwt>` पॉलिसी वापरून येणाऱ्या JWTs ची पडताळणी करणारी inbound पॉलिसी जोडा. सोप्या सेटअपसाठी OpenID Connect मेटाडेटा URL वापरू शकता. पॉलिसीचा उदाहरण भाग:

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

ही पॉलिसी APIM ला Spring Auth Server कडून OpenID कॉन्फिगरेशन मिळवण्यास, त्याचा JWKS प्राप्त करण्यास आणि प्रत्येक टोकन विश्वसनीय कीने स्वाक्षरी केलेले आहे का आणि योग्य audience आहे का हे तपासण्यास सांगते. (`<issuers>` वगळल्यास, APIM मेटाडेटामधील `issuer` क्लेम आपोआप वापरते.) `<audience>` तुमच्या क्लायंट आयडी किंवा API रिसोर्स आयडेंटिफायरशी जुळले पाहिजे (वरील उदाहरणात `"mcp-client"` सेट केले आहे). हे Microsoft च्या `validate-jwt` आणि `<openid-config>` वापरण्याच्या दस्तऐवजांशी सुसंगत आहे ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

पडताळणी नंतर, APIM विनंती (मूळ `Authorization` हेडरसह) बॅकएंडकडे पुढे पाठवेल. Spring अॅप देखील resource server असल्याने टोकन पुन्हा पडताळेल, पण APIM आधीच त्याची वैधता सुनिश्चित केली आहे. (विकासासाठी, तुम्ही APIM च्या तपासणीवर अवलंबून राहू शकता आणि अॅपमधील अतिरिक्त तपासण्या अक्षम करू शकता, पण दोन्ही ठेवणे सुरक्षित आहे.)

## उदाहरण सेटिंग्ज

| सेटिंग            | उदाहरण मूल्य                                                        | टीपा                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | तुमच्या Container App चा URL (बेस URI)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | डिफॉल्ट Spring टोकन endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | डिफॉल्ट JWK सेट endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC डिस्कव्हरी दस्तऐवज (स्वतः तयार होणारा)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth क्लायंट आयडी किंवा API रिसोर्स नाव       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` या URL वापरते ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## सामान्य चुका

- **HTTPS/TLS:** APIM गेटवेला OpenID/JWKS endpoint HTTPS आणि वैध प्रमाणपत्र असणे आवश्यक आहे. डिफॉल्टनुसार, Azure Container Apps Azure-व्यवस्थापित डोमेनसाठी विश्वासार्ह TLS प्रमाणपत्र पुरवते ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). जर तुम्ही कस्टम डोमेन वापरत असाल, तर प्रमाणपत्र बाइंड करणे आवश्यक आहे (Azure चे मोफत व्यवस्थापित प्रमाणपत्र वैशिष्ट्य वापरू शकता) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM ला endpoint चे प्रमाणपत्र विश्वासार्ह वाटले नाही तर `<validate-jwt>` मेटाडेटा मिळवण्यात अयशस्वी होईल.

- **Endpoint प्रवेशयोग्यता:** Spring अॅपचे endpoints APIM कडून पोहोचण्यायोग्य असावेत. `--ingress external` वापरणे (किंवा पोर्टलमध्ये ingress सक्षम करणे) सोपे आहे. जर तुम्ही internal किंवा vNet-बाउंड वातावरण निवडले असेल, तर APIM (डिफॉल्टनुसार सार्वजनिक) कदाचित पोहोचू शकणार नाही जोपर्यंत ते त्याच VNet मध्ये नसेल. चाचणी सेटअपमध्ये, सार्वजनिक ingress प्राधान्य द्या जेणेकरून APIM `.well-known` आणि `/jwks` URLs कॉल करू शकेल.

- **OpenID डिस्कव्हरी सक्षम:** डिफॉल्टनुसार, Spring Authorization Server `/.well-known/openid-configuration` **प्रदर्शित करत नाही** जोपर्यंत OIDC सक्षम केलेले नाही. `.oidc(Customizer.withDefaults())` तुमच्या सुरक्षा कॉन्फिगमध्ये समाविष्ट करा (वरील पहा) जेणेकरून प्रदाता कॉन्फिगरेशन endpoint सक्रिय होईल ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). अन्यथा APIM चा `<openid-config>` कॉल 404 देईल.

- **Audience क्लेम:** Spring चा डिफॉल्ट वर्तन म्हणजे `aud` क्लेम क्लायंट आयडीवर सेट करणे. जर APIM चा `<audience>` तपासणी अयशस्वी झाली, तर तुम्हाला टोकन सानुकूलित करावे लागू शकते (वरीलप्रमाणे) किंवा APIM पॉलिसी समायोजित करावी लागेल. तुमच्या JWT मधील audience `<audience>` शी जुळले पाहिजे.

- **JSON मेटाडेटा पार्सिंग:** OpenID कॉन्फिगरेशन JSON वैध असणे आवश्यक आहे. Spring चा डिफॉल्ट कॉन्फिग मानक OIDC मेटाडेटा दस्तऐवज तयार करतो. त्यात योग्य `issuer` आणि `jwks_uri` आहेत का ते तपासा. जर तुम्ही Spring प्रॉक्सी किंवा पाथ-आधारित रूट मागे होस्ट करत असाल, तर URLs नीट तपासा. APIM हे मूल्ये तशीच वापरेल.

- **पॉलिसी क्रम:** APIM पॉलिसीमध्ये, `<validate-jwt>` **बॅकएंडकडे रूटिंग करण्यापूर्वी** ठेवा. अन्यथा, कॉल्स वैध टोकनशिवाय अॅपपर्यंत पोहोचू शकतात. तसेच `<validate-jwt>` `<inbound>` च्या खाली लगेच असावे (इतर कंडिशनमध्ये नेस्टेड नसावे) जेणेकरून APIM ते लागू करू शकेल.

वरील पायऱ्या पाळून, तुम्ही तुमचा Spring AI MCP सर्व्हर Azure Container Apps मध्ये चालवू शकता आणि Azure API Management वापरून येणाऱ्या OAuth2 JWTs ची पडताळणी करू शकता. मुख्य मुद्दे: Spring Auth endpoints सार्वजनिकपणे TLS सह उघडा, OIDC डिस्कव्हरी सक्षम करा, आणि APIM चा `validate-jwt` OpenID कॉन्फिग URL कडे निर्देशित करा (जेणेकरून ते JWKS आपोआप मिळवू शकेल). हा सेटअप dev/test वातावरणासाठी योग्य आहे; उत्पादनासाठी योग्य सीक्रेट व्यवस्थापन, टोकन कालावधी आणि JWKS मधील की रोटेशन विचारात घ्या.
**References:** Spring Authorization Server च्या डिफॉल्ट endpoints साठी docs पहा ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) आणि OIDC कॉन्फिगरेशनसाठी ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); Microsoft APIM docs मध्ये `validate-jwt` चे उदाहरणे पहा ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); आणि Azure Container Apps च्या deployment व certificates साठी docs पहा ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.