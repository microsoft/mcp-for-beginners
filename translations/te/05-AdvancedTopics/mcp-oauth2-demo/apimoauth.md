# స్ప్రింగ్ AI MCP యాప్‌ను ఆజ్యూర్ కంటైనర్ యాప్స్‌కి డిప్లాయ్ చేయడం

> [!WARNING]
> ఈ కలిపిన అథారైజేషన్/రిసోర్స్ సర్వర్ నేర్చుకోడానికి మరియు
> డెవ్/టెస్ట్ వినియోగానికి ఉద్దేశించబడింది. ప్రొడక్షన్ సిస్టమ్స్ ప్రత్యేక గుర్తింపు అందించే ప్రొవైడర్,
> నిలకడైన సైన్ చేయడం కీలు మరియు మేనేజ్డ్ సీక్రెట్ స్టోర్‌లో నిల్వ చేసిన ప్రమాణపత్రాలను ఉపయోగించాలి.

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *ఫిగర్: స్ప్రింగ్ అథారైజేషన్ సర్వర్‌తో సురక్షితమైన స్ప్రింగ్ AI MCP సర్వర్. సర్వర్ క్లయింట్లకు యాక్సెస్ టోకెన్లను జరిపించి, రిక్వెస్ట్లలో వాటిని ధృవీకరిస్తుంది (మూలం: స్ప్రింగ్ బ్లాగ్) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* స్ప్రింగ్ MCP సర్వర్‌ను డిప్లాయ్ చేయాలంటే, దాన్ని కంటైనర్‌గా నిర్మించి, ఆజ్యూర్ కంటైనర్ యాప్స్‌ని బాహ్య ఇన్‌లాగా ఉపయోగించాలి. ఉదాహరణకు, ఆజ్యూర్ CLI ఉపయోగించి మీరు ఈ కింద ఇచ్చిన కమాండ్‌ను అమలు చేయవచ్చు:

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

ఇది HTTPS ఎనేబుల్‌తో పబ్లిక్‌గా యాక్సెస్ అయ్యే కంటైనర్ యాప్‌ను సృష్టిస్తుంది (ఆజ్యూర్ డిఫాల్ట్ `*.azurecontainerapps.io` డొమైన్‌కు ఉచిత TLS సర్టిఫికేట్‌ను ఇవ్వనుంది ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ఆ పంథాలో ఆప్ యొక్క FQDN (ఉదా. `my-mcp-app.eastus.azurecontainerapps.io`) ఉంటుంది, ఇది **issuer URL** బేస్ అవుతుంది. APIM యాప్‌కి చేరుకోగలిగేలా HTTP ఇన్‌లాగ్ ఎనేబుల్ చేసినట్టు నిర్ధారించుకోండి (పైన చూపినట్లు). టెస్ట్/డెవ్ సెటప్‌లో, `--ingress external` ఆప్షన్ ఉపయోగించండి (లేదా కస్టమ్ డొమైన్‌తో TLS బైండ్ చేయండి [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). ఏవైనా సున్నితమైన గుణాలు (OAuth క్లయింట్ సీక్రెట్లు వంటి) Container Apps సీక్రెట్స్ లేదా ఆజ్యూర్ కీ వాల్ట్‌లో నిల్వ చేసి, వాటిని ఎన్విరాన్మెంట్ వేరియబుల్స్‌గా కంటైనర్‌లో మ్యాప్ చేయండి. 

## స్ప్రింగ్ అథారైజేషన్ సర్వర్ కాంఫిగర్ చేయడం

మీ స్ప్రింగ్ బూట్ యాప్ కోడ్‌లో స్ప్రింగ్ అథారైజేషన్ సర్వర్ మరియు రిసోర్స్ సర్వర్ స్టార్టర్స్‌ను చేర్చండి. `client_credentials` గ్రాంట్ కోసం `RegisteredClient` మరియు JWT కీ సోర్స్‌ను కాంఫిగర్ చేయండి. ఉదాహరణకు, `application.properties`లో మీరు ఈ విధంగా సెట్ చేస్తారు:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

సెక్యూరిటీ ఫిల్టర్ చైన్ నిర్వచించి అథారైజేషన్ సర్వర్ మరియు రిసోర్స్ సర్వర్‌ను ఎనేబుల్ చేయండి. ఉదాహరణకు:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // ఆథరైజేషన్ సర్వర్ ఎండ్‌పాయింట్లను అనుమతించండి
            .apply(authzServer.and())
            // రిసోర్స్ సర్వర్‌ను అనుమతించండి (వచ్చే అభ్యర్థనలపై JWTని ధృవీకరించండి)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRFని అచేతనం చేయండి (MCP సర్వర్ బ్రౌజర్-ఆధారితం కాదు)
            .csrf(csrf -> csrf.disable())
            // క్లయింట్ డెమో టూల్స్ కోసం CORS అనుమతించండి
            .cors(withDefaults());
        return http.build();
    }

    // ఒక ఇన్-మెమరీ క్లయింట్ (RegisteredClient) మరియు JWK మూలాన్ని నిర్వర్తించండి:
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
        // RSA కీని ఉత్పత్తి చేయండి (డెవ్/టెస్ట్ కోసం, ప్రారంభంలో కొత్తదిగా ఉత్పత్తి చేయండి)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ఈ సెట్ అప్ డిఫాల్ట్ OAuth2 ఎండ్‌పాయింట్లను ( `/oauth2/token` టోకెన్ల కోసం మరియు `/oauth2/jwks` JSON వెబ్ కీ సెట్ కోసం) ప్రదర్శిస్తుంది. (డిఫాల్ట్‌గా స్ప్రింగ్ యొక్క `AuthorizationServerSettings` `/oauth2/token` మరియు `/oauth2/jwks` ను మ్యాప్ చేస్తుంది ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) సర్వర్ RSA కీతో సంతకం చేసిన JWT యాక్సెస్ టోకెన్లను జారీ చేస్తుంది మరియు దాని పబ్లిక్ కీని `https://<your-app>:/oauth2/jwks` వద్ద ప్రచురిస్తుంది.

**OpenID Connect డిస్కవరీని ఎనేబుల్ చేయండి:** APIM ఆర్గనైజర్ మరియు JWKS పొందేందుకు స్వయంచాలకంగా OIDC ప్రొవైడర్ కాంఫిగరేషన్ ఎండ్‌పాయింట్‌ను `.oidc(Customizer.withDefaults())` చేర్చడం ద్వారా ఎనేబుల్ చేయండి ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). ఉదాహరణకు:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration ను సక్రియం చేస్తుంది
```

ఇది `/.well-known/openid-configuration`ని ప్రదర్శిస్తుంది, దీన్ని APIM మేటాడేటా కోసం ఉపయోగించవచ్చు. చివరిగా, APIM యొక్క `<audiences>` చెక్ పాస్ కావడానికి JWT **audience** క్లైమ్ ను కస్టమైజ్ చేయాలనుకుంటే, టోకెన్ కస్టమైజర్‌ని జోడించండి:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // అనుకూల ప్రేక్షకులను సెట్ చేయండి (ఉదా. క్లయింట్ ID లేదా API గుర్తింపు)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

ఇది టోకెన్లు `"aud": ["mcp-client"]` ను కలిగి ఉండేలా చూస్తుంది, ఇది APIM ఆశించే క్లయింట్ ID లేదా స్కోపు కి సరిపోతుంది.

## టోకెన్ మరియు JWKS ఎండ్‌పాయింట్లను ఎక్స్‌పోజ్ చేయడం

డిప్లాయ్ చేసిన తరువాత, మీ యాప్ యొక్క **issuer URL** ఉంటుందిః `https://<app-fqdn>` ఉదా: `https://my-mcp-app.eastus.azurecontainerapps.io`. దాని OAuth2 ఎండ్‌పాయింట్లు:

- **టోకెన్ ఎండ్‌పాయింట్:** `https://<app-fqdn>/oauth2/token` – క్లయింట్లు ఇక్కడ టోకెన్లు పొందుతారు (client_credentials ఫ్లో).
- **JWKS ఎండ్‌పాయింట్:** `https://<app-fqdn>/oauth2/jwks` – JWK సెట్‌ను తిరిగి ఇస్తుంది (APIM సంతకం కీలు పొందటానికి ఉపయోగిస్తుంది).
- **OpenID కంఫిగ్:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC డిస్కవరీ JSON (ఉన్నవి `issuer`, `token_endpoint`, `jwks_uri` మరియు ఇతరాలు).

APIM **OpenID కంఫిగరేషన్ URL** పాయింట్ చేస్తుంది, అక్కడి నుండి ఇది `jwks_uri` ని కనుగొంటుంది. ఉదా, మీ కంటైనర్ యాప్ FQDN `my-mcp-app.eastus.azurecontainerapps.io` అయితే, APIM యొక్క `<openid-config url="...">` ఈ URL ను ఉపయోగించాలి: `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (డిఫాల్ట్‌గా స్ప్రింగ్ ఆ మెటాడేటాలో `issuer`ను అదే బేస్ URLతో సెట్ చేస్తుంది ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## ఆజ్యూర్ API మేనేజ్‌మెంట్‌ను కాన్ఫిగర్ చేయడం (`validate-jwt`)

ఆజ్యూర్ APIM లో, ఇన్‌బౌండ్ పాలసీ చేర్చి ప్ర‌వేశించే JWTలను జ‌రిగే స్ప్రింగ్ అథారైజేషన్ సర్వర్‌తో `<validate-jwt>` పాలసీ ద్వారా చెక్ చేయండి. సరళమైన సెటప్‌కు OpenID Connect మేటాడేటా URL ఉపయోగించవచ్చు. ఉదాహరణ పాలసీ స్నిపెట్:

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

ఈ పాలసీ APIM కు స్ప్రింగ్ అథ్ సర్వర్ నుండి OpenID కంఫిగరేషన్‌ను తెచ్చుకోవాలని, దాని JWKS పొందాలని, ప్రతి టోకెన్ సంతకం చేసిన కీతో సరిపోయేలా, సరైన ఆడియన్స్ ఉన్నదో లేదో ధృవీకరించమని చెబుతుంది. (`<issuers>`ని మాడు తీయకపోతే APIM ఆటోమాటిక్‌గా మెటాడేటాలోని `issuer` క్లైమ్ ఉపయోగిస్తుంది.) `<audience>` మానిపి టోకెన్లో ఉన్న క్లయింట్ ID లేదా API రిసోర్స్ IDకి సరిపోనిది (పైన ఉదాహరణలో `"mcp-client"`గా సెట్ చేసింది.) ఇది మైక్రోసాఫ్ట్ డాక్యుమెంటేషన్‌తో సరిపోయే విధంగా ఉంది ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

ధృవీకరణ తరువాత, APIM కోరికను బ్యాక్‌ఏండ్‌కు (అంతర్గత `Authorization` హెడ్డర్‌తో సహా) ఫార్వార్డ్ చేస్తుంది. స్ప్రింగ్ యాప్ కూడా రిసోర్స్ సర్వర్ గాబట్టి టోకెన్ తిరిగి ధృవీకరించగలదు, కానీ APIM ఇప్పటికే దాని చెలామణిని నిర్ధారించింది. (డెవలప్‌మెంట్ కోసం, APIM చెక్‌పై ఆధారపడటం సరిపోతుంది మరియు యాప్ లో అదనపు చెక్స్ తొలగించవచ్చు, కానీ రెండింటినీ ఉంచడం మరింత భద్ర.)

## ఉదాహరణ సెట్టింగులు

| సెట్టింగ్            | ఉదాహరణ విలువ                                                    | గమనికలు                                      |
|--------------------|------------------------------------------------------------------|-----------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                | మీ కంటైనర్ యాప్ URL (బేస్ URI)               |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | డిఫాల్ట్ స్ప్రింగ్ టోకెన్ ఎండ్‌పాయింట్ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | డిఫాల్ట్ JWK సెట్ ఎండ్‌పాయింట్ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC డిస్కవరీ డాక్యుమెంట్ (ఆటో జెనరేటెడ్)    |
| **APIM audience**  | `mcp-client`                                                     | OAuth క్లయింట్ ID లేదా API రిసోర్స్ పేరు      |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` ఈ URL ను ఉపయోగిస్తుంది ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## సాధారణ తప్పులు

- **HTTPS/TLS:** APIM గేట్‌వే OpenID/JWKS ఎండ్‌పాయింట్ HTTPS మరియు చిహ్నితమైన సర్టిఫికేట్‌తో ఉండాలి. డిఫాల్ట్‌గా ఆజ్యూర్ కంటైనర్ యాప్స్ ఆజ్యూర్ నిర్వహించే డొమైన్‌కు విశ్వసనీయ TLS సర్టిఫికేట్‌ను ఇస్తుంది ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). కస్టమ్ డొమైన్ ఉపయోగిస్తే, సర్టిఫికేట్ బైండ్ చేయండి (ఆజ్యూర్ ఉచిత మేనేజ్డ్ సర్ట్ ఫీచర్ ఉపయోగించవచ్చు) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM ఎండ్‌పాయింట్ సర్టిఫికేట్‌పై నమ్మకాన్ని లేకపోతే, `<validate-jwt>` మేటాడేటాను పొందడంలో విఫలమవుతుంది.  

- **ఎండ్‌పాయింట్ లభ్యత:** APIM నుంచి స్ప్రింగ్ యాప్ యొక్క ఎండ్‌పాయింట్లు చేరుకోవడాన్ని నిర్ధారించండి. సరళంగా `--ingress external` లేదా పోర్టల్ లో ఇన్‌లాగ్ ఎనేబుల్ చేయడం మేలైంది. మీరు ఇంటర్నల్ లేదా వి-నెట్ గూఢచర్యను ఎంచుకున్నట్లయితే, APIM (డిఫాల్ట్ పబ్లిక్) అదే వి-నెట్‌లో లేకపోతే అది చేరదు. టెస్ట్ సెటప్‌లో, APIM `.well-known` మరియు `/jwks` URLలను పిలవగలిగేలా పబ్లిక్ ఇన్‌లాగ్ ప్రాధాన్యత ఇవ్వండి. 

- **OpenID డిస్కవరీ ఎనేబుల్ చేయడం:** డిఫాల్ట్‌గా స్ప్రింగ్ అథారైజేషన్ సర్వర్ `/.well-known/openid-configuration`ని ప్రదర్శించదు, OIDC ఎనేబుల్ చేసినప్పుడు మాత్రమే అవుతుంది. ప్రొవైడర్ కంఫిగరేషన్ ఎండ్‌పాయింట్ సక్రియం కావటానికి `.oidc(Customizer.withDefaults())` మీ సెక్యూరిటీ కాన్ఫిగ్‌లో చేర్చండి (పైన చూడండి) ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). లేకపోతే APIM `<openid-config>` కాల్ 404 ఇస్తుంది.

- **ఆడియన్స్ క్లైమ్:** స్ప్రింగ్ డిఫాల్ట్ ప్రవర్తన `aud` క్లైమ్‌ను క్లయింట్ IDగా సెట్ చేస్తుంది. APIM `<audience>` చెక్ ఫెయిలయితే, టోకెన్‌ను కస్టమైజ్ చేయాలసి ఉంటుంది (పైన చూపినట్టు) లేదా APIM పాలసీని సరిచూడండి. JWTలో ఉన్న ఆడియన్స్ `<audience>`లో ఉన్నదిగా ఉండాలి. 

- **JSON మేటాడేటా పార్సింగ్:** OpenID కంఫిగరేషన్ JSON సరైనదిగా ఉండాలి. స్ప్రింగ్ డిఫాల్ట్ కాన్ఫిగ్ OIDC మేటాడేటా డాక్యుమెంట్‌ను విడుదల చేస్తుంది. దీని లో సరైన `issuer` మరియు `jwks_uri` ఉండగా అనుమతించండి. మీరు స్ప్రింగ్‌ను ప్రోక్సీ లేదా పాత్ ఆధారిత మార్గం వెనుక హోస్ట్ చేస్తే, ఈ మేటాడేటాలో URLలను పర్యవేక్షించండి. APIM వాటిని అదే విధంగా ఉపయోగిస్తుంది. 

- **పాలసీ ఆర్డరింగ్:** APIM పాలసీలో, బ్యాక్‌ఎండ్‌కి రూటింగ్‌కి ముందు `<validate-jwt>`ని ఉంచండి. లేకపోతే, కాల్స్ మీ యాప్‌కు సరైన టోకెన్ లేకుండా చేరవచ్చు. అలాగే `<validate-jwt>` `<inbound>` కిందనే ఉండాలి (ఇంకో షరతు లోపల కాకుండా) APIM దీనిని వర్తింపజేస్తుంది.

పై స్టెప్స్ పాటించడం ద్వారా మీరు మీ స్ప్రింగ్ AI MCP సర్వర్‌ను ఆజ్యూర్ కంటైనర్ యాప్స్‌లో నడిపించి, ఆజ్యూర్ API మేనేజ్‌మెంట్ ద్వారా సులభ పాలసీతో OAuth2 JWTలు ధృవీకరించవచ్చు. ముఖ్యాంశాలు: స్ప్రింగ్ అథ్ ఎండ్‌పాయింట్లను TLSతో ప్రజలకు అందుబాటులో ఉండేలా చేయండి, OIDC డిస్కవరీని ఎనేబుల్ చేయండి, మరియు APIM యొక్క `validate-jwt`ను OpenID కంఫిగ్ URL పాయింట్ చేయండి (JWKS ఆటోమాటిక్‌గా తెస్తుంది). ఇది డెవ్/టెస్ట్ పరిసరాలకు అనుకూలంగా ఉంటుంది; ప్రొడక్షన్‌కు సరైన సీక్రెట్ నిర్వహణ, టోకెన్ వ్యవధులు మరియు JWKSలో కీలు తిప్పుకోవడం వంటి అంశాలు పరిగణించండి. 


**సూచనలు:** డిఫాల్ట్ ఎండ్‌పాయింట్ల కోసం Spring Authorization Server డాక్స్ చూడండి ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) మరియు OIDC సెటప్ కోసం ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` ఉదాహరణల కోసం Microsoft APIM డాక్స్ చూడండి ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); మరియు డిప్లయ్‌మెంట్ మరియు సర్టిఫికెట్ల కోసం Azure Container Apps డాక్స్ చూడండి ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->