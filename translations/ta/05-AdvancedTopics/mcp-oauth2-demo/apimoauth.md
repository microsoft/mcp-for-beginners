# Spring AI MCP பயன்பாட்டை Azure Container Apps-க்கு வெளியிடுதல்

([Spring AI MCP சேவையகங்களை OAuth2 மூலம் பாதுகாப்பது](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *படம்: Spring Authorization Server மூலம் பாதுகாக்கப்பட்ட Spring AI MCP சேவையகம். இந்த சேவையகம் கிளையண்ட்களுக்கு அணுகல் டோக்கன்களை வழங்குகிறது மற்றும் வரும் கோரிக்கைகளில் அவற்றை சரிபார்க்கிறது (மூலம்: Spring blog) ([Spring AI MCP சேவையகங்களை OAuth2 மூலம் பாதுகாப்பது](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP சேவையகத்தை வெளியிட, அதை ஒரு கன்டெய்னராக உருவாக்கி, Azure Container Apps-இல் வெளிப்புற ingress-ஐ பயன்படுத்தவும். உதாரணமாக, Azure CLI-யை பயன்படுத்தி நீங்கள் இயக்கலாம்:

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

இது HTTPS-ஐ இயக்கியுள்ள பொதுவாக அணுகக்கூடிய Container App-ஐ உருவாக்குகிறது (Azure `*.azurecontainerapps.io` இயல்புநிலை டொமைனுக்கு இலவச TLS சான்றிதழை வழங்குகிறது ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). கட்டளையின் வெளியீட்டில் பயன்பாட்டின் FQDN (எ.கா. `my-mcp-app.eastus.azurecontainerapps.io`) அடங்கும், இது **issuer URL** அடிப்படையாக மாறுகிறது. HTTP ingress இயக்கப்பட்டிருப்பதை உறுதிப்படுத்தவும் (மேலே உள்ளபடி) APIM பயன்பாட்டை அணுக முடியும். ஒரு சோதனை/மேம்பாட்டு அமைப்பில், `--ingress external` விருப்பத்தை பயன்படுத்தவும் (அல்லது [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)) படி TLS உடன் தனிப்பயன் டொமைனை இணைக்கவும்). எந்தவொரு உணர்திறனான பண்புகளையும் (உதாரணமாக OAuth கிளையண்ட் ரகசியங்கள்) Container Apps ரகசியங்களில் அல்லது Azure Key Vault-இல் சேமிக்கவும், அவற்றை சூழல் மாறிகள் ஆக கன்டெய்னரில் வரைபடமாக்கவும்.

## Spring Authorization Server-ஐ அமைத்தல்

உங்கள் Spring Boot பயன்பாட்டின் குறியீட்டில், Spring Authorization Server மற்றும் Resource Server தொடக்கங்களை சேர்க்கவும். ஒரு `RegisteredClient` (dev/test-இல் `client_credentials` வழங்குவதற்காக) மற்றும் ஒரு JWT முக்கிய மூலத்தை அமைக்கவும். உதாரணமாக, `application.properties`-இல் நீங்கள் அமைக்கலாம்:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server மற்றும் Resource Server-ஐ ஒரு பாதுகாப்பு வடிகட்டி சங்கிலியை வரையறுத்து இயக்கவும். உதாரணமாக:

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

இந்த அமைப்பு இயல்புநிலை OAuth2 முடுக்கங்களை வெளிப்படுத்தும்: டோக்கன்களுக்கு `/oauth2/token` மற்றும் JSON Web Key Set-க்கு `/oauth2/jwks`. (Spring இன் `AuthorizationServerSettings` இயல்புநிலை `/oauth2/token` மற்றும் `/oauth2/jwks`-ஐ வரைபடமாக்குகிறது ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) சேவையகம் மேலே RSA முக்கியத்தால் கையொப்பமிடப்பட்ட JWT அணுகல் டோக்கன்களை வழங்கும் மற்றும் அதன் பொது முக்கியத்தை `https://<your-app>:/oauth2/jwks`-இல் வெளியிடும்.

**OpenID Connect கண்டுபிடிப்பை இயக்கவும்:** APIM issuer மற்றும் JWKS-ஐ தானாகவே பெற அனுமதிக்க, உங்கள் பாதுகாப்பு அமைப்பில் `.oidc(Customizer.withDefaults())` சேர்த்து OIDC வழங்குநர் கட்டமைப்பு முடுக்கத்தை இயக்கவும் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). உதாரணமாக:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

இது `/.well-known/openid-configuration`-ஐ வெளிப்படுத்தும், இதை APIM metadata-க்கு பயன்படுத்தலாம். இறுதியாக, APIM இன் `<audiences>` சரிபார்ப்பு பாஸ் ஆகும் வகையில் JWT **audience** கோரிக்கையை தனிப்பயனாக்க விரும்பலாம். உதாரணமாக, ஒரு டோக்கன் customizer சேர்க்கவும்:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

இது `"aud": ["mcp-client"]`-ஐ டோக்கன்களில் சேர்க்கும், இது APIM எதிர்பார்க்கும் கிளையண்ட் ஐடி அல்லது scope-ஐ பொருந்தும்.

## டோக்கன் மற்றும் JWKS முடுக்கங்களை வெளிப்படுத்துதல்

வெளியிடப்பட்ட பிறகு, உங்கள் பயன்பாட்டின் **issuer URL** `https://<app-fqdn>` ஆக இருக்கும், உதாரணமாக `https://my-mcp-app.eastus.azurecontainerapps.io`. அதன் OAuth2 முடுக்கங்கள்:

- **டோக்கன் முடுக்கம்:** `https://<app-fqdn>/oauth2/token` – கிளையண்ட்கள் இங்கு டோக்கன்களை பெறுகின்றன (client_credentials flow).
- **JWKS முடுக்கம்:** `https://<app-fqdn>/oauth2/jwks` – JWK தொகுப்பை திருப்புகிறது (APIM கையொப்ப முக்கியங்களை பெற பயன்படுத்துகிறது).
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC கண்டுபிடிப்பு JSON (`issuer`, `token_endpoint`, `jwks_uri`, போன்றவை அடங்கும்).

APIM **OpenID configuration URL**-ஐ சுட்டிக்காட்டும், இதிலிருந்து `jwks_uri`-ஐ கண்டுபிடிக்கும். உதாரணமாக, உங்கள் Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` என்றால், APIM இன் `<openid-config url="...">` `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`-ஐ பயன்படுத்த வேண்டும். (Spring இயல்பாக அந்த metadata-இல் `issuer`-ஐ அதே அடிப்படை URL-க்கு அமைக்கும் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) அமைத்தல்

Azure APIM-இல், `<validate-jwt>` கொள்கையை பயன்படுத்தி Spring Authorization Server-இன் JWT-களை சரிபார்க்க ஒரு inbound கொள்கையை சேர்க்கவும். ஒரு எளிய அமைப்புக்கு, OpenID Connect metadata URL-ஐ பயன்படுத்தலாம். கொள்கை துணுக்கின் உதாரணம்:

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

இந்த கொள்கை APIM-க்கு Spring Auth Server-இன் OpenID configuration-ஐ பெற, அதன் JWKS-ஐ பெற மற்றும் ஒவ்வொரு டோக்கனும் நம்பகமான முக்கியத்தால் கையொப்பமிடப்பட்டதா மற்றும் சரியான audience-ஐ கொண்டதா என்பதை சரிபார்க்கச் சொல்கிறது. (`<issuers>`-ஐ தவிர்த்தால், APIM metadata-இல் உள்ள `issuer` கோரிக்கையை தானாகவே பயன்படுத்தும்.) `<audience>` உங்கள் டோக்கனில் உள்ள கிளையண்ட் ஐடி அல்லது API resource identifier-ஐ பொருந்த வேண்டும் (மேலே உள்ள உதாரணத்தில், அதை `"mcp-client"`-க்கு அமைத்தோம்). இது `<openid-config>` உடன் `validate-jwt` பயன்படுத்த Microsoft-இன் ஆவணங்களுடன் இணங்குகிறது ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

சரிபார்ப்புக்குப் பிறகு, APIM கோரிக்கையை (மூல `Authorization` தலைப்பை உட்பட) backend-க்கு அனுப்பும். Spring பயன்பாட்டும் resource server ஆக இருப்பதால், அது டோக்கனை மீண்டும் சரிபார்க்கும், ஆனால் APIM ஏற்கனவே அதன் செல்லுபடியாக்தன்மையை உறுதிப்படுத்தியுள்ளது. (மேம்பாட்டுக்காக, நீங்கள் APIM இன் சரிபார்ப்பை நம்பி பயன்பாட்டில் கூடுதல் சரிபார்ப்புகளை முடக்கலாம், ஆனால் இரண்டையும் வைத்திருப்பது பாதுகாப்பானது.)

## அமைப்பின் உதாரணங்கள்

| அமைப்பு            | உதாரண மதிப்பு                                                        | குறிப்புகள்                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | உங்கள் Container App-இன் URL (அடிப்படை URI)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | இயல்புநிலை Spring டோக்கன் முடுக்கம் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | இயல்புநிலை JWK Set முடுக்கம் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC கண்டுபிடிப்பு ஆவணம் (தானாக உருவாக்கப்பட்டது)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth கிளையண்ட் ஐடி அல்லது API resource பெயர்       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` இந்த URL-ஐ பயன்படுத்துகிறது ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## பொதுவான சிக்கல்கள்

- **HTTPS/TLS:** APIM கேட்வே OpenID/JWKS முடுக்கம் HTTPS மற்றும் செல்லுபடியாகும் சான்றிதழுடன் இருக்க வேண்டும். இயல்பாக, Azure Container Apps Azure-இல் நிர்வகிக்கப்படும் டொமைனுக்கு நம்பகமான TLS சான்றிதழை வழங்குகிறது ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). நீங்கள் தனிப்பயன் டொமைனை பயன்படுத்தினால், ஒரு சான்றிதழை இணைக்கவும் (Azure இன் இலவச நிர்வகிக்கப்பட்ட சான்றிதழ் அம்சத்தை பயன்படுத்தலாம்) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM முடுக்கத்தின் சான்றிதழை நம்ப முடியாவிட்டால், `<validate-jwt>` metadata-ஐ பெற முடியாது.

- **முடுக்கம் அணுகல்:** Spring பயன்பாட்டின் முடுக்கங்கள் APIM-இல் இருந்து அணுகக்கூடியதாக இருக்க வேண்டும். `--ingress external` (அல்லது போர்ட்டலில் ingress-ஐ இயக்குதல்) எளிமையானது. நீங்கள் ஒரு internal அல்லது vNet-bound சூழலை தேர்ந்தெடுத்தால், APIM (இயல்பாக public) அதை அணுக முடியாது, அது அதே VNet-இல் வைக்கப்படாவிட்டால். ஒரு சோதனை அமைப்பில், `.well-known` மற்றும் `/jwks` URL-களை APIM அழைக்க public ingress-ஐ விரும்பவும்.

- **OpenID Discovery Enabled:** இயல்பாக, Spring Authorization Server `/.well-known/openid-configuration`-ஐ **வெளிப்படுத்தாது**, OIDC இயக்கப்படாவிட்டால். OIDC வழங்குநர் கட்டமைப்பு முடுக்கம் செயல்பட `.oidc(Customizer.withDefaults())` உங்கள் பாதுகாப்பு அமைப்பில் சேர்க்கவும் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). இல்லையெனில் APIM இன் `<openid-config>` அழைப்பு 404 ஆகும்.

- **Audience Claim:** Spring இன் இயல்புநிலை நடத்தை `aud` கோரிக்கையை கிளையண்ட் ஐடிக்கு அமைக்கிறது. APIM இன் `<audience>` சரிபார்ப்பு தோல்வியடைந்தால், நீங்கள் டோக்கனை (மேலே காட்டியபடி) தனிப்பயனாக்க வேண்டும் அல்லது APIM கொள்கையை சரிசெய்ய வேண்டும். உங்கள் JWT-இல் உள்ள audience `<audience>`-இல் நீங்கள் அமைக்கிறதுடன் பொருந்த வேண்டும்.

- **JSON Metadata Parsing:** OpenID configuration JSON செல்லுபடியாக இருக்க வேண்டும். Spring இன் இயல்புநிலை அமைப்பு ஒரு நிலையான OIDC metadata ஆவணத்தை வெளியிடும். இதில் சரியான `issuer` மற்றும் `jwks_uri` உள்ளதா என்பதை உறுதிப்படுத்தவும். நீங்கள் Spring-ஐ proxy அல்லது path-based வழியில் ஹோஸ்ட் செய்தால், இந்த metadata-இல் உள்ள URL-களை இருமுறை சரிபார்க்கவும். APIM இந்த மதிப்புகளை அப்படியே பயன்படுத்தும்.

- **Policy Ordering:** APIM கொள்கையில், `<validate-jwt>` **backend-க்கு எந்தவொரு வழிமாற்றத்திற்கும் முன்** வைக்கவும். இல்லையெனில், செல்லுபடியாகாத டோக்கனுடன் உங்கள் பயன்பாட்டை அழைப்புகள் அடையலாம். மேலும் `<validate-jwt>` `<inbound>`-இன் கீழே உடனடியாக தோன்றுவதை உறுதிப்படுத்தவும் (மற்றொரு நிலைமையின் உள்ளே இடம் பெறாமல்) APIM அதை பயன்படுத்தும்.

மேலே உள்ள படிகளைப் பின்பற்றுவதன் மூலம், நீங்கள் உங்கள் Spring AI MCP சேவையகத்தை Azure Container Apps-இல் இயக்கலாம் மற்றும் Azure API Management-ஐ குறைந்த கொள்கையுடன் வரும் OAuth2 JWT-களை சரிபார்க்கச் செய்யலாம். முக்கியமான புள்ளிகள்: Spring Auth முடுக்கங்களை TLS உடன் பொதுவாக வெளிப்படுத்தவும், OIDC கண்டுபிடிப்பை இயக்கவும், மற்றும் APIM இன் `validate-jwt`-ஐ OpenID config URL-க்கு சுட்டிக்காட்டவும் (JWKS-ஐ தானாகவே பெற APIM-க்கு அனுமதிக்க). இந்த அமைப்பு dev/test சூழலுக்கு ஏற்றது; உற்பத்திக்காக, சரியான ரகசிய மேலாண்மை, டோக்கன் காலங்கள் மற்றும் JWKS-இல் முக்கியங்களை சுழற்றுதல் போன்றவற்றை பரிசீலிக்கவும்.
**குறிப்புகள்:** Spring Authorization Server-இன் இயல்புநிலை முடுக்கங்கள் பற்றிய ஆவணங்களைப் பார்க்கவும் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) மற்றும் OIDC அமைப்பைச் சுட்டிக்காட்டவும் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` உதாரணங்களுக்கான Microsoft APIM ஆவணங்களைப் பார்க்கவும் ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); மற்றும் Azure Container Apps ஆவணங்களைப் பார்க்கவும், இடமாற்றம் மற்றும் சான்றிதழ்கள் தொடர்பான தகவலுக்கு ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.