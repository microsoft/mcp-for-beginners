<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "32c9a4263be08f9050c8044bb26267c4",
  "translation_date": "2025-12-11T16:17:26+00:00",
  "source_file": "05-AdvancedTopics/mcp-oauth2-demo/apimoauth.md",
  "language_code": "te"
}
-->
# Spring AI MCP యాప్‌ను Azure కంటైనర్ యాప్స్‌కు డిప్లాయ్ చేయడం

 ([OAuth2తో Spring AI MCP సర్వర్‌లను సురక్షితం చేయడం](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *చిత్రం: Spring Authorization Serverతో సురక్షితం చేయబడిన Spring AI MCP సర్వర్. సర్వర్ క్లయింట్లకు యాక్సెస్ టోకెన్లను జారీ చేస్తుంది మరియు వాటిని వచ్చే అభ్యర్థనలపై ధృవీకరిస్తుంది (మూలం: Spring బ్లాగ్) ([OAuth2తో Spring AI MCP సర్వర్‌లను సురక్షితం చేయడం](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP సర్వర్‌ను డిప్లాయ్ చేయడానికి, దాన్ని కంటైనర్‌గా నిర్మించి Azure కంటైనర్ యాప్స్‌తో బాహ్య ఇంగ్రెస్ ఉపయోగించండి. ఉదాహరణకు, Azure CLI ఉపయోగించి మీరు ఈ క్రింది విధంగా నడపవచ్చు:

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

ఇది HTTPS ఎనేబుల్ చేసిన ప్రజలకు అందుబాటులో ఉన్న కంటైనర్ యాప్‌ను సృష్టిస్తుంది (Azure డిఫాల్ట్ `*.azurecontainerapps.io` డొమైన్ కోసం ఉచిత TLS సర్టిఫికేట్ జారీ చేస్తుంది ([Azure Container Appsలో కస్టమ్ డొమైన్ పేర్లు మరియు ఉచిత నిర్వహించబడిన సర్టిఫికేట్లు | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ఆదేశం అవుట్‌పుట్‌లో యాప్ యొక్క FQDN (ఉదా: `my-mcp-app.eastus.azurecontainerapps.io`) ఉంటుంది, ఇది **issuer URL** బేస్ అవుతుంది. APIM యాప్‌ను చేరుకునేందుకు HTTP ఇంగ్రెస్ ఎనేబుల్ చేయబడిందని నిర్ధారించుకోండి (పైన ఉన్నట్లుగా). టెస్ట్/డెవ్ సెటప్‌లో, `--ingress external` ఆప్షన్ ఉపయోగించండి (లేదా [Microsoft డాక్స్](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ప్రకారం TLSతో కస్టమ్ డొమైన్ బైండ్ చేయండి ([Azure Container Appsలో కస్టమ్ డొమైన్ పేర్లు మరియు ఉచిత నిర్వహించబడిన సర్టిఫికేట్లు | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ఏదైనా సున్నితమైన ప్రాపర్టీలను (OAuth క్లయింట్ సీక్రెట్స్ వంటి) కంటైనర్ యాప్స్ సీక్రెట్స్ లేదా Azure కీ వాల్ట్‌లో నిల్వ చేసి, వాటిని కంటైనర్‌లో ఎన్విరాన్‌మెంట్ వేరియబుల్స్‌గా మ్యాప్ చేయండి.

## Spring Authorization Server కాన్ఫిగర్ చేయడం

మీ Spring Boot యాప్ కోడ్‌లో, Spring Authorization Server మరియు Resource Server స్టార్టర్స్‌ను చేర్చండి. `RegisteredClient` (డెవ్/టెస్ట్‌లో `client_credentials` గ్రాంట్ కోసం) మరియు JWT కీ సోర్స్‌ను కాన్ఫిగర్ చేయండి. ఉదాహరణకు, `application.properties`లో మీరు ఇలా సెట్ చేయవచ్చు:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server మరియు Resource Serverని సెక్యూరిటీ ఫిల్టర్ చైన్ నిర్వచించడం ద్వారా ఎనేబుల్ చేయండి. ఉదాహరణకు:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // అథారైజేషన్ సర్వర్ ఎండ్‌పాయింట్లను ఎనేబుల్ చేయండి
            .apply(authzServer.and())
            // రిసోర్స్ సర్వర్‌ను ఎనేబుల్ చేయండి (వచ్చే అభ్యర్థనలపై JWTని ధృవీకరించండి)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRFని డిసేబుల్ చేయండి (MCP సర్వర్ బ్రౌజర్ ఆధారితం కాదు)
            .csrf(csrf -> csrf.disable())
            // క్లయింట్ డెమో టూల్స్ కోసం CORS అనుమతించండి
            .cors(withDefaults());
        return http.build();
    }

    // ఒక ఇన్-మెమరీ క్లయింట్ (RegisteredClient) మరియు JWK సోర్స్‌ను నిర్వచించండి:
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
        // RSA కీని జనరేట్ చేయండి (డెవ్/టెస్ట్ కోసం, స్టార్ట్‌అప్ వద్ద కొత్తదిగా జనరేట్ చేయండి)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ఈ సెటప్ డిఫాల్ట్ OAuth2 ఎండ్‌పాయింట్లను ఎక్స్‌పోజ్ చేస్తుంది: టోకెన్ల కోసం `/oauth2/token` మరియు JSON వెబ్ కీ సెట్ కోసం `/oauth2/jwks`. (డిఫాల్ట్‌గా Spring యొక్క `AuthorizationServerSettings` `/oauth2/token` మరియు `/oauth2/jwks`కి మ్యాప్ చేస్తుంది ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) సర్వర్ పై పేర్కొన్న RSA కీతో సంతకం చేసిన JWT యాక్సెస్ టోకెన్లను జారీ చేస్తుంది, మరియు దాని పబ్లిక్ కీని `https://<your-app>:/oauth2/jwks` వద్ద ప్రచురిస్తుంది.

**OpenID Connect డిస్కవరీని ఎనేబుల్ చేయండి:** APIM ఆటోమేటిక్‌గా issuer మరియు JWKS పొందేందుకు, మీ సెక్యూరిటీ కాన్ఫిగరేషన్‌లో `.oidc(Customizer.withDefaults())`ని చేర్చండి ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ఉదాహరణకు:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration ను సక్రియం చేస్తుంది
```

ఇది `/.well-known/openid-configuration`ని ఎక్స్‌పోజ్ చేస్తుంది, దీన్ని APIM మెటాడేటా కోసం ఉపయోగించవచ్చు. చివరగా, APIM యొక్క `<audiences>` చెక్ పాస్ అవ్వడానికి JWT **audience** క్లెయిమ్‌ను కస్టమైజ్ చేయవచ్చు. ఉదాహరణకు, టోకెన్ కస్టమైజర్‌ను చేర్చండి:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // కస్టమ్ ఆడియెన్స్‌ను సెట్ చేయండి (ఉదా: క్లయింట్ ID లేదా API గుర్తింపు)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

ఇది టోకెన్లు `"aud": ["mcp-client"]` కలిగి ఉంటాయని నిర్ధారిస్తుంది, ఇది APIM ఆశించే క్లయింట్ ID లేదా స్కోప్‌కు సరిపోతుంది.

## టోకెన్ మరియు JWKS ఎండ్‌పాయింట్లను ఎక్స్‌పోజ్ చేయడం

డిప్లాయ్ చేసిన తర్వాత, మీ యాప్ యొక్క **issuer URL** `https://<app-fqdn>` అవుతుంది, ఉదా: `https://my-mcp-app.eastus.azurecontainerapps.io`. దాని OAuth2 ఎండ్‌పాయింట్లు:

- **టోకెన్ ఎండ్‌పాయింట్:** `https://<app-fqdn>/oauth2/token` – క్లయింట్లు ఇక్కడ టోకెన్లు పొందుతారు (client_credentials ఫ్లో).
- **JWKS ఎండ్‌పాయింట్:** `https://<app-fqdn>/oauth2/jwks` – JWK సెట్‌ను తిరిగి ఇస్తుంది (APIM సంతకం కీలు పొందడానికి ఉపయోగిస్తుంది).
- **OpenID కాన్ఫిగ్:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC డిస్కవరీ JSON (issuer, token_endpoint, jwks_uri మొదలైనవి ఉంటాయి).

APIM **OpenID కాన్ఫిగరేషన్ URL**ను పాయింట్ చేస్తుంది, అక్కడి నుండి `jwks_uri`ని కనుగొంటుంది. ఉదాహరణకు, మీ కంటైనర్ యాప్ FQDN `my-mcp-app.eastus.azurecontainerapps.io` అయితే, APIM యొక్క `<openid-config url="...">` `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` ఉపయోగించాలి. (డిఫాల్ట్‌గా Spring ఆ మెటాడేటాలో issuerని అదే బేస్ URLగా సెట్ చేస్తుంది ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) కాన్ఫిగర్ చేయడం

Azure APIMలో, `<validate-jwt>` పాలసీని ఉపయోగించి వచ్చే JWTలను మీ Spring Authorization Serverతో తనిఖీ చేసే ఇన్‌బౌండ్ పాలసీని జోడించండి. సింపుల్ సెటప్ కోసం, OpenID Connect మెటాడేటా URL ఉపయోగించవచ్చు. ఉదాహరణ పాలసీ స్నిపెట్:

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

ఈ పాలసీ APIMకి Spring Auth Server నుండి OpenID కాన్ఫిగరేషన్‌ను పొందమని, దాని JWKSను రీట్రీవ్ చేసి, ప్రతి టోకెన్ విశ్వసనీయ కీతో సంతకం చేయబడిందని మరియు సరైన audience కలిగి ఉందని ధృవీకరించమని చెబుతుంది. (`<issuers>`ని మిస్ చేస్తే, APIM మెటాడేటాలోని `issuer` క్లెయిమ్‌ను ఆటోమేటిక్‌గా ఉపయోగిస్తుంది.) `<audience>` టోకెన్‌లో మీ క్లయింట్ ID లేదా API రిసోర్స్ ఐడెంటిఫయర్‌కు సరిపోవాలి (పైన ఉదాహరణలో `"mcp-client"`గా సెట్ చేశాము). ఇది Microsoft డాక్యుమెంటేషన్‌లో `<openid-config>`తో `validate-jwt` ఉపయోగించే విధానానికి అనుగుణంగా ఉంటుంది ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

ధృవీకరణ తర్వాత, APIM అభ్యర్థనను (మూల `Authorization` హెడ్డర్ సహా) బ్యాక్‌ఎండ్‌కు ఫార్వర్డ్ చేస్తుంది. Spring యాప్ కూడా రిసోర్స్ సర్వర్ కావడంతో టోకెన్‌ను మళ్లీ ధృవీకరిస్తుంది, కానీ APIM ఇప్పటికే దాని చెల్లుబాటు తత్వాన్ని నిర్ధారించింది. (డెవలప్‌మెంట్ కోసం, APIM తన తనిఖీపై ఆధారపడవచ్చు మరియు యాప్‌లో అదనపు తనిఖీలను డిసేబుల్ చేయవచ్చు, కానీ రెండింటినీ ఉంచడం సురక్షితం.)

## ఉదాహరణ సెట్టింగ్స్

| సెట్టింగ్            | ఉదాహరణ విలువ                                                        | గమనికలు                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | మీ కంటైనర్ యాప్ URL (బేస్ URI)             |
| **టోకెన్ ఎండ్‌పాయింట్** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | డిఫాల్ట్ Spring టోకెన్ ఎండ్‌పాయింట్ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS ఎండ్‌పాయింట్**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | డిఫాల్ట్ JWK సెట్ ఎండ్‌పాయింట్ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID కాన్ఫిగ్**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC డిస్కవరీ డాక్యుమెంట్ (ఆటో-జనరేట్ చేయబడింది)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth క్లయింట్ ID లేదా API రిసోర్స్ పేరు       |
| **APIM పాలసీ**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ఈ URL ఉపయోగిస్తుంది ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## సాధారణ జాగ్రత్తలు

- **HTTPS/TLS:** APIM గేట్‌వే OpenID/JWKS ఎండ్‌పాయింట్ HTTPSతో సరైన సర్టిఫికేట్ కలిగి ఉండాలి. డిఫాల్ట్‌గా, Azure కంటైనర్ యాప్స్ Azure-నిర్వహించబడే డొమైన్ కోసం విశ్వసనీయ TLS సర్టిఫికేట్ అందిస్తుంది ([Azure Container Appsలో కస్టమ్ డొమైన్ పేర్లు మరియు ఉచిత నిర్వహించబడిన సర్టిఫికేట్లు | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). మీరు కస్టమ్ డొమైన్ ఉపయోగిస్తే, సర్టిఫికేట్ బైండ్ చేయడం నిర్ధారించుకోండి (Azure ఉచిత నిర్వహించబడిన సర్టిఫికేట్ ఫీచర్ ఉపయోగించవచ్చు) ([Azure Container Appsలో కస్టమ్ డొమైన్ పేర్లు మరియు ఉచిత నిర్వహించబడిన సర్టిఫికేట్లు | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM ఎండ్‌పాయింట్ సర్టిఫికేట్‌పై నమ్మకం లేకపోతే, `<validate-jwt>` మెటాడేటాను పొందడంలో విఫలమవుతుంది.

- **ఎండ్‌పాయింట్ యాక్సెసిబిలిటీ:** Spring యాప్ ఎండ్‌పాయింట్లు APIM నుండి చేరుకోగలిగేలా ఉండాలి. `--ingress external` (లేదా పోర్టల్‌లో ఇంగ్రెస్ ఎనేబుల్ చేయడం) సులభమైనది. మీరు ఇంటర్నల్ లేదా vNet-బౌండ్ ఎన్విరాన్‌మెంట్ ఎంచుకున్నట్లయితే, APIM (డిఫాల్ట్‌గా పబ్లిక్) దానిని చేరుకోకపోవచ్చు, unless అదే VNetలో ఉంచబడితే. టెస్ట్ సెటప్‌లో, APIM `.well-known` మరియు `/jwks` URLలను కాల్ చేయగలిగేలా పబ్లిక్ ఇంగ్రెస్ ప్రాధాన్యం ఇవ్వండి.

- **OpenID డిస్కవరీ ఎనేబుల్ చేయడం:** డిఫాల్ట్‌గా, Spring Authorization Server `/.well-known/openid-configuration`ని OIDC ఎనేబుల్ చేయకపోతే ఎక్స్‌పోజ్ చేయదు. మీ సెక్యూరిటీ కాన్ఫిగరేషన్‌లో `.oidc(Customizer.withDefaults())` చేర్చడం నిర్ధారించుకోండి (పైన చూడండి) తద్వారా ప్రొవైడర్ కాన్ఫిగరేషన్ ఎండ్‌పాయింట్ యాక్టివ్ అవుతుంది ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). లేకపోతే APIM యొక్క `<openid-config>` కాల్ 404 వస్తుంది.

- **Audience క్లెయిమ్:** Spring డిఫాల్ట్ ప్రవర్తన `aud` క్లెయిమ్‌ను క్లయింట్ IDగా సెట్ చేయడం. APIM యొక్క `<audience>` చెక్ ఫెయిల్ అయితే, టోకెన్‌ను కస్టమైజ్ చేయవలసి ఉంటుంది (పైన చూపినట్లుగా) లేదా APIM పాలసీని సర్దుబాటు చేయండి. JWTలో audience మీరు `<audience>`లో కాన్ఫిగర్ చేసినదానికి సరిపోవాలి.

- **JSON మెటాడేటా పార్సింగ్:** OpenID కాన్ఫిగరేషన్ JSON సరైనది కావాలి. Spring డిఫాల్ట్ కాన్ఫిగరేషన్ ఒక స్టాండర్డ్ OIDC మెటాడేటా డాక్యుమెంట్‌ను ఉత్పత్తి చేస్తుంది. దానిలో సరైన `issuer` మరియు `jwks_uri` ఉన్నాయో నిర్ధారించుకోండి. మీరు Springని ప్రాక్సీ లేదా పాత్-ఆధారిత రూట్ వెనుక హోస్ట్ చేస్తే, ఈ మెటాడేటాలో URLలను డబుల్ చెక్ చేయండి. APIM ఈ విలువలను అలాగే ఉపయోగిస్తుంది.

- **పాలసీ ఆర్డరింగ్:** APIM పాలసీలో, `<validate-jwt>`ని బ్యాక్‌ఎండ్‌కు రూటింగ్ చేసే ముందు ఉంచండి. లేకపోతే, కాల్స్ సరైన టోకెన్ లేకుండా యాప్‌కు చేరవచ్చు. అలాగే `<validate-jwt>` `<inbound>` కింద తక్షణమే ఉండాలి (ఇంకొక కండిషన్ లోపల కాకుండా) తద్వారా APIM దాన్ని వర్తింపజేస్తుంది.

పై దశలను అనుసరించడం ద్వారా, మీరు Spring AI MCP సర్వర్‌ను Azure కంటైనర్ యాప్స్‌లో నడిపించి, Azure API Management ద్వారా వచ్చే OAuth2 JWTలను కనిష్ట పాలసీతో ధృవీకరించవచ్చు. ముఖ్యాంశాలు: Spring Auth ఎండ్‌పాయింట్లను TLSతో ప్రజలకు అందుబాటులో ఉంచడం, OIDC డిస్కవరీని ఎనేబుల్ చేయడం, APIM యొక్క `validate-jwt`ని OpenID కాన్ఫిగ్ URLకు పాయింట్ చేయడం (JWKS ఆటోమేటిక్‌గా పొందేందుకు). ఇది డెవ్/టెస్ట్ వాతావరణానికి అనుకూలం; ప్రొడక్షన్ కోసం సరైన సీక్రెట్ నిర్వహణ, టోకెన్ లైఫ్‌టైమ్స్, JWKSలో కీలు రొటేట్ చేయడం వంటి అంశాలను పరిగణించండి.
**సూచనలు:** డిఫాల్ట్ ఎండ్పాయింట్ల కోసం Spring Authorization Server డాక్స్ చూడండి ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) మరియు OIDC కాన్ఫిగరేషన్ కోసం ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` ఉదాహరణల కోసం Microsoft APIM డాక్స్ చూడండి ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); మరియు డిప్లాయ్‌మెంట్ మరియు సర్టిఫికెట్ల కోసం Azure Container Apps డాక్స్ చూడండి ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారుల బాధ్యత మేము తీసుకోము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->