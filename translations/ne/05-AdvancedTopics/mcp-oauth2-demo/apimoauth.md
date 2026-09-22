# स्प्रिंग AI MCP एपलाई Azure Container Apps मा डिप्लोय गर्दै

> [!WARNING]
> यो संयुक्त अधिकार/स्रोत सर्भर सिकाइ र विकास/टेस्ट प्रयोजनका लागि हो। उत्पादन प्रणालीहरूले समर्पित पहिचान प्रदायक,
> स्थायी साइनिंग कुञ्जीहरू, र व्यवस्थापित गोप्य स्टोरमा भण्डारण गरिएका प्रमाणपत्रहरू प्रयोग गर्नुपर्छ।
> 

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *आकृति: Spring Authorization Server द्वारा सुरक्षित Spring AI MCP सर्भर। सर्भरले क्लाइन्टहरूलाई पहुँच टोकनहरू जारी गर्छ र आउने अनुरोधहरूमा तिनीहरूलाई मान्य गर्छ (स्रोत: Spring ब्लग) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP सर्भरलाई डिप्लोय गर्नको लागि यसलाई कन्टेनरको रूपमा निर्माण गर्नुहोस् र Azure Container Apps सँग बाहिरी ईनग्रस प्रयोग गर्नुहोस्। उदाहरणको लागि, Azure CLI प्रयोग गरेर तपाईं चलाउन सक्नुहुन्छ:

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

यसले HTTPS सक्षम गरिएको सार्वजनिक रूपले पहुँचयोग्य Container App सिर्जना गर्छ (Azure ले पूर्वनिर्धारित `*.azurecontainerapps.io` डोमेनको लागि नि:शुल्क TLS प्रमाणपत्र जारी गर्छ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). आदेशको आउटपुटमा एपको FQDN (जस्तै `my-mcp-app.eastus.azurecontainerapps.io`) समावेश हुन्छ, जुन **issuer URL** आधार बन्न जान्छ। HTTP ingress सक्षम छ कि छैन सुनिश्चित गर्नुहोस् (जसरी माथि भनेको छ) ताकि APIM एपसम्म पुग्न सकोस्। टेस्ट/डेभ सेटअपमा, `--ingress external` विकल्प प्रयोग गर्नुहोस् (वा TLS सहित कस्टम डोमेन बाँध्नुहोस् [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). कुनै पनि संवेदनशील सम्पत्ति (जस्तै OAuth क्लाइन्ट गोप्य कुञ्जीहरू) Container Apps secrets वा Azure Key Vault मा भण्डारण गर्नुहोस् र तिनीहरूलाई कन्टेनर भित्र वातावरण भेरिएबलहरूका रूपमा म्याप गर्नुहोस्। 

## Spring Authorization Server कन्फिगर गर्दै

तपाईंको Spring Boot एपको कोडमा, Spring Authorization Server र Resource Server starters समावेश गर्नुहोस्। `RegisteredClient` कन्फिगर गर्नुहोस् (डेभ/टेस्टमा `client_credentials` अनुदानको लागि) र JWT कुञ्जी स्रोत। उदाहरणका लागि, `application.properties` मा तपाइँले यस्तो सेट गर्न सक्नुहुन्छ:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

सुरक्षा फिल्टर चेनलाई परिभाषित गरेर Authorization Server र Resource Server सक्षम गर्नुहोस्। उदाहरणका लागि:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // प्रमाणीकरण सर्भर अन्तिम बिन्दुहरू सक्षम गर्नुहोस्
            .apply(authzServer.and())
            // स्रोत सर्भर सक्षम गर्नुहोस् (आउँदै गरेको अनुरोधहरूमा JWT जाँच गर्नुहोस्)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF अक्षम गर्नुहोस् (MCP सर्भर ब्राउजर-आधारित छैन)
            .csrf(csrf -> csrf.disable())
            // क्लाइन्ट डेमो उपकरणहरूको लागि CORS अनुमति दिनुहोस्
            .cors(withDefaults());
        return http.build();
    }

    // एक इन-मेमोरी क्लाइन्ट (RegisteredClient) र JWK स्रोत परिभाषित गर्नुहोस्:
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
        // RSA कुञ्जी उत्पन्न गर्नुहोस् (विकास/परीक्षणका लागि, सुरूवातमा नयाँ कुञ्जी उत्पन्न गर्नुहोस्)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

यो सेटअपले पूर्वनिर्धारित OAuth2 अन्त्यबिन्दुहरू खोल्नेछ: `/oauth2/token` टोकनका लागि र `/oauth2/jwks` JSON Web Key Set का लागि। (पूर्वनिर्धारित रूपमा Spring को `AuthorizationServerSettings` ले `/oauth2/token` र `/oauth2/jwks` म्याप गर्छ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) सर्भरले माथि उल्लिखित RSA कुञ्जीद्वारा हस्ताक्षर गरिएको JWT पहुँच टोकनहरू जारी गर्नेछ र यसको सार्वजनिक कुञ्जी `https://<your-app>:/oauth2/jwks` मा प्रकाशित गर्नेछ।

**OpenID Connect डिस्कवरी सक्षम गर्नुहोस्:** APIMले issuer र JWKS स्वचालित रूपमा प्राप्त गर्न सक्नुको लागि, तपाईंको सुरक्षा कन्फिगरेसनमा `.oidc(Customizer.withDefaults())` थपेर OIDC प्रदायक कन्फिगरेसन अन्त्यबिन्दु सक्षम गर्नुहोस् ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). उदाहरणका लागि:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration सक्षम पार्दछ
```

यसले `/.well-known/openid-configuration`लाई खोल्छ, जुन APIMले मेटाडाटा लागि प्रयोग गर्न सक्छ। अन्तमा, तपाइँले JWT **audience** दाबी अनुकूलन गर्न सक्नुहुन्छ ताकि APIM को `<audiences>` चेक पुरा होस्। उदाहरणका लागि, टोकन कस्टमाइजर थप्नुहोस्:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // अनुकूलित दर्शक सेट गर्नुहोस् (जस्तै क्लाइंट ID वा API परिचायक)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

यसले सुनिश्चित गर्छ कि टोकनहरूले `"aud": ["mcp-client"]` बोकेको छ, जुन APIM द्वारा अपेक्षित क्लाइन्ट ID वा स्कोपसँग मेल खान्छ।

## टोकन र JWKS अन्त्यबिन्दुहरू खुला गर्ने

डिप्लोय गरेपछि, तपाईंको एपको **issuer URL** हुनेछ `https://<app-fqdn>`, जस्तै `https://my-mcp-app.eastus.azurecontainerapps.io`। यसको OAuth2 अन्त्यबिन्दुहरू हुन्:

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – क्लाइन्टहरू यहाँबाट टोकन प्राप्त गर्छन् (`client_credentials` प्रवाह)।
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – JWK सेट फर्काउँछ (APIMले हस्ताक्षर कुञ्जीहरू पाउन यसको प्रयोग गर्छ)।
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC डिस्कवरी JSON (मा `issuer`, `token_endpoint`, `jwks_uri`, आदि समावेश छन्)।  

APIMले **OpenID कन्फिगरेसन URL**लाई निर्देशन गर्नेछ, जहाँबाट यसले `jwks_uri` खोज्छ। उदाहरणका लागि, यदि तपाईंको Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` हो भने, APIMको `<openid-config url="...">`ले `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` प्रयोग गर्नुपर्छ। (पूर्वनिर्धारित रूपमा Spring ले उक्त मेटाडाटामा `issuer`लाई सोही आधार URL मा सेट गर्नेछ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) कन्फिगर गर्दै

Azure APIM मा, `<validate-jwt>` नीतिको साथ एक इनबाउन्ड नीति थप्नुहोस् जुन तपाईंको Spring Authorization Server विरुद्ध आउने JWT जाँच गर्छ। साधारण सेटअपका लागि तपाईं OpenID Connect मेटाडाटा URL प्रयोग गर्न सक्नुहुन्छ। उदाहरण नीति अंश:

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

यस नीतिले APIMलाई Spring Auth Server बाट OpenID कन्फिगरेसन ल्याउन, यसको JWKS प्राप्त गर्न, र प्रत्येक टोकन एक विश्वसनीय कुञ्जीद्वारा हस्ताक्षर गरिएको छ र सही audience छ कि छैन भेरिफाइ गर्न निर्देशन दिन्छ। (`<issuers>` बाहेक राखेमा, APIMले मेटाडाटाबाट `issuer` दाबी स्वतः प्रयोग गर्नेछ।) `<audience>` टोकनमा तपाईँको क्लाइन्ट ID वा API स्रोत पहिचानकर्ता संग मेल खानुपर्छ (माथिको उदाहरणमा हामीले यसलाई `"mcp-client"` सेट गरेका छौं)। यो Microsoft को `validate-jwt` र `<openid-config>` बारेको डक्युमेन्टेसनसँग मेल खान्छ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

मान्यताको पछि, APIMले अनुरोध (मूल `Authorization` हेडर सहित) ब्याकएन्डमा अग्रेषित गर्नेछ। किनकि Spring एप पनि स्रोत सर्भर हो, यसले टोकन पुनः मान्य गर्नेछ, तर APIMले यसलाई पहिले नै प्रमाणित गरिसकेको हुन्छ। (डेभलपमेन्टका लागि, तपाईं APIMको जाँचमा भर पर्न सक्नुहुन्छ र एपमा अतिरिक्त जाँचहरू अक्षम गर्न सक्नुहुन्छ यदि चाहनुहुन्छ, तर दुवै राख्नु बढी सुरक्षित हुन्छ।)

## उदाहरण सेटिङहरू

| सेटिङ              | उदाहरण मान                                                        | टिप्पणीहरू                                   |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                   | तपाईंको Container App को URL (आधार URI)       |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`      | पूर्वनिर्धारित Spring टोकन अन्त्यबिन्दु ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`       | पूर्वनिर्धारित JWK सेट अन्त्यबिन्दु ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC डिस्कवरी कागजात (स्वयं-उत्पन्न)          |
| **APIM audience**  | `mcp-client`                                                       | OAuth क्लाइन्ट ID वा API स्रोत नाम              |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` यस URL प्रयोग गर्छ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## सामान्य समस्याहरू

- **HTTPS/TLS:** APIM गेटवेजले OpenID/JWKS अन्त्यबिन्दु HTTPS र मान्य प्रमाणपत्र सहित हुनु आवश्यक छ। पूर्वनिर्धारित रूपमा, Azure Container Apps ले Azure-प्रबन्धित डोमेनका लागि विश्वसनीय TLS प्रमाणपत्र प्रदान गर्छ ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). यदि तपाईंले कस्टम डोमेन प्रयोग गर्नु हुन्छ भने, प्रमाणपत्र बाँध्न निश्चित गर्नुहोस् (Azure को नि:शुल्क प्रबन्धित प्रमाणपत्र सुविधा प्रयोग गर्न सक्नुहुन्छ) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). यदि APIM ले उक्त अन्त्यबिन्दुको प्रमाणपत्रमा भरोसा गर्न सक्दैन भने, `<validate-jwt>`ले मेटाडाटा ल्याउन असफल हुनेछ।  

- **अन्त्यबिन्दु पहुँचयोग्यता:** Spring एपका अन्त्यबिन्दुहरू APIM बाट पहुँचयोग्य हुनु पर्छ। `--ingress external` (वा पोर्टलमा ईनग्रस सक्षम गर्नु) सबैभन्दा सजिलो हुन्छ। यदि तपाईंले भित्री वा vNet-बद्ध वातावरण चयन गर्नुभयो भने, APIM (पूर्वनिर्धारित रूपमा सार्वजनिक) ले त्यो पहुँच नपाउन सक्छ जबसम्म यसलाई समान VNet मा राखिँदैन। टेस्ट सेटअपमा, सार्वजनिक ईनग्रस प्राथमिकता दिनुहोस् ताकि APIMले `.well-known` र `/jwks` URL कल गर्न सकोस्। 

- **OpenID डिस्कवरी सक्षम:** पूर्वनिर्धारित रूपमा, Spring Authorization Serverले `/.well-known/openid-configuration` **खुल्दैन** जबसम्म OIDC सक्षम गरिएको हुँदैन। सुनिश्चित गर्नुहोस् कि तपाईंको सुरक्षा कन्फिगमा `.oidc(Customizer.withDefaults())` समावेश छ (माथि हेर्नुहोस्) जसले प्रदायक कन्फिगरेसन अन्त्यबिन्दु सक्रिय बनाउँछ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). नत्र APIMको `<openid-config>` कलले 404 फर्काउनेछ।

- **Audience दाबी:** Spring को पूर्वनिर्धारित व्यवहारले `aud` दाबीलाई क्लाइन्ट ID मा सेट गर्छ। यदि APIMको `<audience>` जाँच असफल भयो भने, तपाईंले टोकन अनुकूलन गर्नुपर्ने हुन सक्छ (जसरी माथि देखाइएको छ) वा APIM नीतिमा समायोजन गर्नुपर्ने हुन सक्छ। तपाईंको JWT मा दर्शकले `<audience>` मा कन्फिगृत भएकोसँग मेल खान्छ भनेर सुनिश्चित गर्नुहोस्। 

- **JSON मेटाडाटा पार्सिङ:** OpenID कन्फिगरेसन JSON वैध हुनुपर्छ। Spring को पूर्वनिर्धारित कन्फिगले मानक OIDC मेटाडाटा कागजात निकाल्नेछ। यो सही `issuer` र `jwks_uri` छ कि छैन प्रमाणित गर्नुहोस्। यदि तपाईं Spring लाई प्रोक्सी वा पथ-आधारित राउटको पछाडि होस्ट गर्नुहुन्छ भने, मेटाडाटामा URLहरू दोहोरो जाँच गर्नुहोस्। APIMले यी मानहरू जसरी छन् त्यस्तै प्रयोग गर्नेछ। 

- **नीति क्रम:** APIM नीतिमा, `<validate-jwt>`लाई ब्याकएन्डतर्फ कुनै रुटिङ गर्नु अघि राख्नुहोस्। नत्र, कलहरू तपाईंको एपमा मान्य टोकन बिना पुग्न सक्छन्। साथै सुनिश्चित गर्नुहोस् कि `<validate-jwt>` तत्काल `<inbound>` अन्तर्गत देखिन्छ (अर्को सर्त भित्र भएन) ताकि APIM यसलाई लागू गर्न सकोस्।

माथि उल्लिखित चरणहरू पालना गरेर, तपाईं आफ्नो Spring AI MCP सर्भरलाई Azure Container Apps मा चलाउन सक्नुहुन्छ र Azure API Management लाई OAuth2 JWTs को भेरिफिकेशन गर्न एक न्यूनतम नीति प्रयोग गरेर सक्षम पार्न सक्नुहुन्छ। मुख्य कुराहरू हुन्: Spring Auth अन्त्यबिन्दुहरू TLS सहित सार्वजनिक रूपमा खोल्नु, OIDC डिस्कवरी सक्षम गर्नु, र APIM को `validate-jwt`लाई OpenID कन्फिग URLमा निर्देशित गर्नु (जसले JWKS स्वचालित रूपमा ल्याउँछ)। यो सेटअप विकास/टेस्ट वातावरणका लागि उपयुक्त छ; उत्पादनको लागि उचित गोप्य व्यवस्थापन, टोकन अवधि, र JWKSमा कुञ्जीहरू घुमाउने विचार गर्नुपर्छ। 


**सन्दर्भहरू:** डिफ़ल्ट अन्तबिन्दुहरूको लागि Spring Authorization Server कागजातहरू हेर्नुहोस् ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) र OIDC कन्फिगरेसन ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` उदाहरणहरूको लागि Microsoft APIM कागजातहरू हेर्नुहोस् ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); र Azure Container Apps का लागि डेप्लोयमेन्ट र प्रमाणपत्रहरूका लागि कागजातहरू हेर्नुहोस् ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->