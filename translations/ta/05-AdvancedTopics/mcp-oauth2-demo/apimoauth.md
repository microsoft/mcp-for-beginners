# Spring AI MCP பயன்பாட்டை Azure Container Apps-க்கு செருகுதல்

> [!WARNING]
> இந்த இணைந்த அங்கீகாரம்/வள சேவையகத்தை கற்பது மற்றும்
> மேம்பாடு/தேர்வு பயன்பாட்டிற்காக எதிர்பார்க்கப்படுகிறது. உற்பத்தி அமைப்புகள் தனிப்பட்ட அடையாள வழங்குநர்,
> நிலைத்த கையொப்ப விசைகள் மற்றும் நிர்வகிக்கப்பட்ட ரகசிய அங்காடியில் சேமிக்கப்பட்ட கடவுச்சொற்களைப் பயன்படுத்த வேண்டும்.

 ([Spring AI MCP சேவையகங்களை OAuth2 உடன் பாதுகாப்பது](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *படம்: Spring AI MCP சேவையகம் Spring Authorization Server உதவியுடன் பாதுகாக்கப்பட்டது. இந்த சேவையகம் கடவுச்சீட்டுகளை கிளையன்ட்களுக்கு வழங்கி வரும் மற்றும் வரும் கோரிக்கைகளில் அவற்றை சரிபார்க்கிறது (மூலம்: Spring blog) ([Spring AI MCP சேவையகங்களை OAuth2 உடன் பாதுகாப்பது](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP சேவையகத்தை நிலையாக்க, அதை ஒரு கன்டெய்னராக கட்டி Azure Container Apps உடன் வெளிப்புற நுழைவுடன் பயன்படுத்தவும். உதாரணமாக, Azure CLI மூலம் கீழ்க்கண்ட கட்டளை இயக்கலாம்:

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

இது HTTPS இயல்பூட்டப்பட்ட பொதுமுக கன்டெய்னர் பயன்பாட்டை உருவாக்கும் (Azure `*.azurecontainerapps.io` இயல்புநிலை டொமைனுக்கான இலவச TLS சான்றிதழை வழங்குகிறது ([Azure Container Apps இல் தனிப்பயன் டொமைன் பெயர்கள் மற்றும் இலவச நிர்வகிக்கப்பட்ட சான்றிதழ்கள் | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). கட்டளையின் வெளியீடு பயன்பாட்டின் FQDN-ஐ (உதா: `my-mcp-app.eastus.azurecontainerapps.io`) காட்டும், இது **issuer URL** அடிப்படையாக இருக்கும். HTTP நுழைவுத் திறவு இயல்பூட்டப்பட்டுள்ளதாக உறுதி செய்யவும் (மேலே போல) எனவே APIM பயன்பாட்டை அணுக முடியும். சோதனை/மேம்பாட்டு அமைப்பில் `--ingress external` விருப்பத்தை பயன்படுத்தவும் (அல்லது [Microsoft கோப்புக்கள்](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) அடி TLS கொண்ட தனிப்பயன் டொமைனுடன் இணைக்கவும் ([Azure Container Apps இல் தனிப்பயன் டொமைன் பெயர்கள் மற்றும் இலவச நிர்வகிக்கப்பட்ட சான்றிதழ்கள் | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). எந்தவொரு உணர்ச்சிபூர்வமான பண்புகளை (உதா: OAuth கிளையன்ட் ரகசியங்கள்) Container Apps ரகசியங்களில் அல்லது Azure Key Vault-ல் சேமித்து அவற்றை கன்டெய்னரில் சுற்றுச்சூழல் மாறிலிகளாக அமைக்கவும்.

## Spring Authorization Server ஐ கட்டமைக்கும் முறை

உங்கள் Spring Boot பயன்பாட்டின் குறியீட்டில், Spring Authorization Server மற்றும் Resource Server ஸ்டார்டர்களை சேர்க்கவும். `RegisteredClient` (dev/test இல் `client_credentials` க்கான) மற்றும் JWT விசை ஊற்றினை அமைக்கவும். உதாரணமாக, `application.properties` இல் நீங்கள் இதைப் பொருந்தலாம்:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Authorization Server மற்றும் Resource Server-ஐ பாதுகாப்புக் கடத்தலுக்கான சங்கிலியை வரையறுத்து இயக்கவும். உதாரணம்:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // அங்கீகார சேவையகத்தின் முடிவுகளை செயல்படுத்தவும்
            .apply(authzServer.and())
            // வளங்களை சேவையகத்தை செயல்படுத்தவும் (வருவாய் கோரிக்கைகளில் JWT ஐ உறுதிப்படுத்தவும்)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF ஐ முடக்கு (MCP சேவையகம் உலாவி அடிப்படையிலல்ல)
            .csrf(csrf -> csrf.disable())
            // கிளையெண்ட் டெமோ கருவிகளுக்கு CORS ஐ அனுமதிக்கவும்
            .cors(withDefaults());
        return http.build();
    }

    // ஒரு நினைவகத்தில் உள்ள கிளையெண்டை (பதிவு செய்யப்பட்ட கிளையெண்ட்) மற்றும் ஒரு JWK மூலத்தை வரையறுக்கவும்:
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
        // ஒரு RSA விசையை உருவாக்கவும் (வளர்ச்சி/சோதனைக்காக, துவக்கத்தில் புதியதாக உருவாக்கவும்)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

இந்த அமைப்பு இயல்புநிலையில் OAuth2 முனையங்களை வெளிப்படுத்தும்: டோக்கன்களுக்கு `/oauth2/token` மற்றும் JSON இணைய அங்கங்கள் தொகுப்புக்கு `/oauth2/jwks`. (இயல்பாக Spring இன் `AuthorizationServerSettings` `/oauth2/token` மற்றும் `/oauth2/jwks` ஐ திகைச்சு அமர்த்துகிறது ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) சேவையகம் மேலே காட்டிய RSA விசையால் கையொப்பமிடப்பட்ட JWT அணுகல் டோக்கன்களை வழங்கும் மற்றும் அதன் பொதுவான விசையை `https://<your-app>:/oauth2/jwks` இல் வெளியிடும்.

**OpenID Connect கண்டுபிடிப்பை இயக்கவும்:** APIM தானாக issuer மற்றும் JWKS ஐ பெற OIDC வழங்குநர் கட்டமைப்பு முனையை `.oidc(Customizer.withDefaults())` சேர்த்து உங்கள் பாதுகாப்பு அமைப்பில் இயக்கவும் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). உதாரணம்:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration ஐ செயல்படுத்துகிறது
```

இது `/.well-known/openid-configuration` ஐ வெளிப்படுத்தும், APIM இதைப் பயன்ப metadata க்கு பயன்படுத்தலாம். கடைசியாக, APIM இன் `<audiences>` சரிபார்ப்பை பூர்த்தி செய்ய JWT **audience** உரிமையை மாற்ற விரும்பலாம். உதாரணமாக, டோக்கன் தனிப்பயன் செயற்பாட்டை சேர்க்கவும்:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // தனிப்பட்ட பார்வையாளர் (எ.கா. கிளையंट் ஐடி அல்லது API அடையாளம்) அமைக்கவும்
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

இது டோக்கன்களில் `"aud": ["mcp-client"]` இருக்கும் என்பதை உறுதி செய்யும், இது APIM எதிர்பார்க்கும் கிளையன்ட் ஐடி அல்லது களத்திற்கு பொருந்தும்.

## Token மற்றும் JWKS முனையங்களை வெளிப்படுத்துதல்

வைப்புத்தேர்வுக்குப் பிறகு, உங்கள் பயன்பாட்டின் **issuer URL** `https://<app-fqdn>`, உதா: `https://my-mcp-app.eastus.azurecontainerapps.io` ஆகும். அதன் OAuth2 முனைகளாக:

- **Token முனை:** `https://<app-fqdn>/oauth2/token` – இல் கிளையன்ட்கள் டோக்கன்களை பெறுவார்கள் (client_credentials ஓட்டம்).
- **JWKS முனை:** `https://<app-fqdn>/oauth2/jwks` – JWK தொகுப்பை வழங்கும் (APIM கையொப்ப விசைகள் பெற பயன்படுத்தும்).
- **OpenID கட்டமைப்பு:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC கண்டுபிடிப்பு JSON (உள்ளடக்கியது `issuer`, `token_endpoint`, `jwks_uri` மற்றும் பிற).

APIM **OpenID கட்டமைப்பு URL** நோக்கி, அதில் உள்ள `jwks_uri` ஐ கண்டுபிடிக்கும். உதா: உங்கள் Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` என்றால், APIM இன் `<openid-config url="...">` `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` ஐப் பயன்படுத்த வேண்டும். (இயல்பாக Spring அந்த metadata இல் `issuer` ஐ அதே அடிப்படை URL ஆக அமைக்கும் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management ஐ கட்டமைத்தல் (`validate-jwt`)

Azure APIM இல், வரும் JWT களை உங்கள் Spring Authorization Server அடிப்படையில் சரிபார்க்க `<validate-jwt>` நுழைவு கொள்கையை சேர்க்கவும். எளிய அமைப்பிற்கு OpenID Connect metadata URL பயன்படுத்தலாம். கொள்கை எடுத்துக்காட்டு:

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

இந்த கொள்கை APIM இற்கு Spring Auth Server இலிருந்து OpenID கட்டமைப்பைப் பெற, அதன் JWKS ஐ மீட்டு, ஒவ்வொரு டோக்கனும் நம்பகமான விசையால் கையொப்பமிடப்பட்டதா மற்றும் சரியான audience-வை கொண்டதா என பரிசோதிக்கச் சொல்கிறது. (`<issuers>` விட்டு வைக்கும் போது APIM தானாக metadata வழியாக `issuer` உரிமையைப் பயன்படுத்தும்.) `<audience>` உங்கள் கிளையன்ட் ஐடி அல்லது API வள அடையாளத்துடன் பொருந்த வேண்டும் (மேலே உதாரணத்தில் `"mcp-client"` ஆக அமைக்கப்பட்டது). இது Microsoft இன் `validate-jwt` மற்றும் `<openid-config>` பயன்படுத்துதலின் ஆவணங்களுக்கு உடன்படுகிறது ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

சரிபார்ப்புக்குப் பிறகு, APIM கோரிக்கையை (அடங்கியது மூல `Authorization` தலைப்பும்) பின்னணி சேவையகத்திற்கு அனுப்பும். Spring பயன்பாடு ஒரு வள சேவையகமாக இருக்கையால், டோக்கனைக் மீண்டும் சரிபார்க்கும், ஆனால் APIM ஏற்கனவே அதன் செல்லுபடித்தன்மையை உறுதி செய்திருக்கும். (மேம்பாட்டிற்கு, நீங்கள் APIM சரிபார்ப்பை பொறுத்துக் கொண்டு பயன்பாட்டின் கூடுதல் சரிபார்ப்பை முடக்கலாம், ஆனால் இரண்டையும் வைத்திருப்பது பாதுகாப்பானது.)

## எடுத்துக்காட்டு அமைப்புகள்

| அமைப்பு               | எடுத்துக்காட்டு மதிப்பு                                               | குறிப்பு                                  |
|--------------------|------------------------------------------------------------------|------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                   | உங்கள் Container App URL (அடிப்படை URI)  |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`      | இயல்புநிலை Spring டோக்கன் முனை ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`       | இயல்புநிலை JWK தொகுப்பு முனை ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC கண்டுபிடிப்பு ஆவணம் (தானாக உருவாக்கப்பட்டது)   |
| **APIM audience**  | `mcp-client`                                                        | OAuth கிளையன்ட் ஐடி அல்லது API வள பெயர்    |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` இந்த URL ஐப் பயன்படுத்து ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## பொதுவான தவறுகள்

- **HTTPS/TLS:** APIM கதவு OpenID/JWKS முனை HTTPS மற்றும் செல்லுபடும் சான்றிதழுடன் இருக்க வேண்டும். இயல்பாக Azure Container Apps Azure நிர்வகிக்கும் டொமைனுக்கு நம்பகமான TLS சான்றிதழ் வழங்கும் ([Azure Container Apps இல் தனிப்பயன் டொமைன் பெயர்கள் மற்றும் இலவச நிர்வகிக்கப்பட்ட சான்றிதழ்கள் | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). நீங்கள் தனிப்பயன் டொமைனைக் கையாளின், சான்றிதழ் இணைக்க உறுதி செய்யவும் (Azure இலவச நிர்வகிக்கப்பட்ட சான்று வசதியைக் பயன்படுத்தலாம்) ([Azure Container Apps இல் தனிப்பயன் டொமைன் பெயர்கள் மற்றும் இலவச நிர்வகிக்கப்பட்ட சான்றிதழ்கள் | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). APIM அந்த முனையின் சான்றிதழை நம்பவில்லை என்றால் `<validate-jwt>` metadata பெற்றதில் தோல்வி அடையும்.

- **முனை அணுகல்:** Spring பயன்பாட்டின் முனைகள் APIM இலிருந்து அணுகக்கூடியதாக இருப்பதை உறுதி செய்யவும். `--ingress external` பயன்படுத்துவது (அல்லது உலாவி மூலமாக நுழைவைக் கோரிக்கைகர அழைப்பது) எளிமையானது. நீங்கள் உள்ளக அல்லது VNet-படிவமைப்பை தேர்ந்தெடுத்தால், APIM பொதுவாக இல்லாதபோது அதனை அணுக முடியாது. சோதனை சூழலில், பொதுமுக நுழைவு விரும்பப்படுகிறது, APIM `.well-known` மற்றும் `/jwks` URL-களை அழைக்க உதவும்.

- **OpenID கண்டுபிடிப்பு இயக்கப்பட்டது:** Spring Authorization Server இயல்பில் `/.well-known/openid-configuration` ஐ வெளியிடாது தவிர OIDC இயக்கப்பட்டால் மட்டுமே. மேற்கண்டபடி `.oidc(Customizer.withDefaults())` உங்கள் பாதுகாப்பு அமைப்பில் சேர்க்க வேண்டும் (மேலே பார்க்கவும்) அதனால் வழங்குநர் கட்டமைப்பு முனை செயல்படும் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). இல்லையெனில் APIM இன் `<openid-config>` கோரிக்கை 404 க்கு உட்படும்.

- **Audience உரிமை:** Spring இயல்பை `aud` உரிமையை கிளையன்ட் ஐடியாக அமைக்கும். APIM இன் `<audience>` சோதனை தோல்வியுற்றால், நீங்கள் டோக்கன் தனிப்பயனாக்கம் செய்ய வேண்டியிருப்பதோ அல்லது APIM கொள்கையை திருத்த வேண்டியிருப்பதோ இருக்கலாம். உங்கள் JWT இல் audience நீங்கள் `<audience>` இல் அமைத்ததைப் பொருந்த வேண்டும்.

- **JSON Metadata பகுப்பு:** OpenID கட்டமைப்பு JSON செல்லுபடியானதாக இருக்க வேண்டும். Spring இயல்புநிலை OIDC metadata ஆவணத்தைக் வெளியிடும். சரியான `issuer` மற்றும் `jwks_uri` உள்ளதா என்று சரிபார்க்கவும். நீங்கள் Spring ஐ முகப்புருவான வழிமுறையுடன் அல்லது பாதை-அடிப்படையிலான வழியுடன் நடத்தியால், இந்த metadata இல் URLs சரிபார்க்கவும். APIM இவை அப்படியே பயன்படுத்தும்.

- **கொள்கை வரிசை:** APIM கொள்கையில் `<validate-jwt>` பிறகு எந்தவொரு பின்னணி வழித்தடத்துக்குமே முன்பே வைக்கவும். இல்லையெனில், செல்லுபடியாகாத டோக்கன் உடன் கோரிக்கைகள் உங்கள் பயன்பாட்டை எட்டலாம். மேலும் `<validate-jwt>` உட்பட `<inbound>` உடனடியாக கீழ் இருக்க வேண்டும் (வேறு நிபந்தனையிற்குள் வைதல் தவிர) எனவே APIM அதை செயல்படுத்தும்.

மேலேயுள்ள படிகளையெல்லாம் பின்பற்றுவதன் மூலம், நீங்கள் Spring AI MCP சேவையகத்தை Azure Container Apps இல் இயக்கி, Azure API Management வந்து வரும் OAuth2 JWT களை குறைந்தபட்ச கொள்கை கொண்டு சரிபார்க்க செய்யலாம். முக்கிய அம்சங்கள்: Spring Auth முனைகளை பொதுமுகமாக TLS உடன் வெளிப்படுத்தவும், OIDC கண்டுபிடிப்பை இயக்கு, APIM `validate-jwt` ஐ OpenID கட்டமைப்பு URL ஐ நோக்கி அமைக்க (இதனால் JWKS தானாக பெறப்படும்). இது மேம்பாடு/தேர்வு சூழலுக்கு பொருத்தமானது; உற்பத்திக்கான போது சரியான ரகசிய மேலாண்மை, டோக்கன் ஆயுள் மற்றும் JWKS விசைகள் பரிமாற்றத்தை கவனிக்க வேண்டும்.


**அறிமுகங்கள்:** இயல்பூா்வ் முனைகளுக்கான Spring Authorization Server ஆவணங்களை பாருங்கள் ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) மற்றும் OIDC கட்டமைப்புக்கான ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); Microsoft APIM ஆவணங்களில் `validate-jwt` உதாரணங்களை பாருங்கள் ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); மற்றும் Azure Container Apps ஆவணங்கள் டிப்ளாய்மென்ட் மற்றும் சான்றிதழ்களுக்கானவை ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->