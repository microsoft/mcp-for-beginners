# Spring AI MCP App ကို Azure Container Apps တွင် တပ်ဆင်ခြင်း

([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *ပုံရိပ် - Spring AI MCP server ကို Spring Authorization Server ဖြင့် လုံခြုံစေထားသည်။ Server သည် client များအား access token များထုတ်ပေးပြီး လာရောက်သော request များတွင် token များကို စစ်ဆေးသည် (အရင်းအမြစ် - Spring blog) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP server ကို deploy လုပ်ရန် container အဖြစ် တည်ဆောက်ပြီး Azure Container Apps တွင် external ingress ဖြင့် အသုံးပြုပါ။ ဥပမာအားဖြင့် Azure CLI ကို အသုံးပြု၍ အောက်ပါ command ကို run နိုင်သည်-

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

ဤ command သည် HTTPS ဖြင့် public access ရရှိနိုင်သော Container App တစ်ခုကို ဖန်တီးပေးသည် (Azure သည် default `*.azurecontainerapps.io` domain အတွက် အခမဲ့ TLS certificate ထုတ်ပေးသည် ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)))။ Command output တွင် app ၏ FQDN (ဥပမာ - `my-mcp-app.eastus.azurecontainerapps.io`) ပါဝင်ပြီး ၎င်းသည် **issuer URL** အခြေခံ URL ဖြစ်လာမည်။ HTTP ingress ကို enabled ထားရန် သေချာစေပါ (အထက်ပါအတိုင်း)၊ APIM သည် app ကို ရောက်ရှိနိုင်ရန်ဖြစ်သည်။ စမ်းသပ်/ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်တွင် `--ingress external` option ကို သုံးပါ (သို့မဟုတ် Microsoft စာရွက်စာတမ်းအတိုင်း TLS ဖြင့် custom domain ကို bind လုပ်ပါ) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates))။ OAuth client secrets ကဲ့သို့သော sensitive properties များကို Container Apps secrets သို့မဟုတ် Azure Key Vault တွင် သိမ်းဆည်းပြီး container ထဲသို့ environment variables အဖြစ် map လုပ်ပါ။

## Spring Authorization Server ကို ပြင်ဆင်ခြင်း

သင့် Spring Boot app ၏ code တွင် Spring Authorization Server နှင့် Resource Server starters များကို ထည့်သွင်းပါ။ `RegisteredClient` (dev/test အတွက် `client_credentials` grant အတွက်) နှင့် JWT key source ကို configure လုပ်ပါ။ ဥပမာအားဖြင့် `application.properties` တွင် အောက်ပါအတိုင်း သတ်မှတ်နိုင်သည်-

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server နှင့် Resource Server ကို security filter chain ဖြင့် ဖွင့်ပါ။ ဥပမာ-

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

ဤ setup သည် default OAuth2 endpoints များဖြစ်သည့် `/oauth2/token` (token များအတွက်) နှင့် `/oauth2/jwks` (JSON Web Key Set အတွက်) ကို ဖော်ပြပေးမည်။ (Spring ၏ `AuthorizationServerSettings` သည် default အနေဖြင့် `/oauth2/token` နှင့် `/oauth2/jwks` ကို map လုပ်ထားသည် ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)))။ Server သည် RSA key ဖြင့် လက်မှတ်ရေးထိုးထားသော JWT access token များ ထုတ်ပေးပြီး ၎င်း၏ public key ကို `https://<your-app>:/oauth2/jwks` တွင် ထုတ်ပြန်မည်။

**OpenID Connect discovery ကို ဖွင့်ပါ:** APIM သည် issuer နှင့် JWKS ကို အလိုအလျောက် ရယူနိုင်ရန် security configuration တွင် `.oidc(Customizer.withDefaults())` ကို ထည့်သွင်းပါ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))။ ဥပမာ-

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

ဤသည်က `/.well-known/openid-configuration` ကို ဖော်ပြပေးပြီး APIM သည် metadata အတွက် အသုံးပြုနိုင်သည်။ နောက်ဆုံးတွင် JWT **audience** claim ကို APIM ၏ `<audiences>` စစ်ဆေးမှု ဖြတ်သန်းနိုင်ရန် အလိုအလျောက် ပြင်ဆင်လိုနိုင်သည်။ ဥပမာ token customizer ကို ထည့်သွင်းပါ-

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

ဤက token များတွင် `"aud": ["mcp-client"]` ပါဝင်စေရန် သေချာစေပြီး APIM ၏ client ID သို့မဟုတ် scope နှင့် ကိုက်ညီစေသည်။

## Token နှင့် JWKS Endpoints များကို ဖော်ပြခြင်း

Deploy ပြီးနောက် သင့် app ၏ **issuer URL** သည် `https://<app-fqdn>` ဖြစ်မည်၊ ဥပမာ `https://my-mcp-app.eastus.azurecontainerapps.io` ဖြစ်သည်။ ၎င်း၏ OAuth2 endpoints များမှာ-

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – client များ token ရယူရန် (client_credentials flow)
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – JWK set ကို ပြန်ပေးပို့သည် (APIM သည် signing keys ရယူရန် အသုံးပြုသည်)
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (issuer, token_endpoint, jwks_uri စသည်တို့ ပါဝင်သည်)

APIM သည် **OpenID configuration URL** ကို ရည်ညွှန်းပြီး `jwks_uri` ကို ရှာဖွေသည်။ ဥပမာ Container App FQDN သည် `my-mcp-app.eastus.azurecontainerapps.io` ဖြစ်ပါက APIM ၏ `<openid-config url="...">` သည် `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` ကို အသုံးပြုသင့်သည်။ (Spring သည် default အနေဖြင့် metadata တွင် issuer ကို အခြေခံ URL အတိုင်း သတ်မှတ်ပေးသည် ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)))။

## Azure API Management (`validate-jwt`) ကို ပြင်ဆင်ခြင်း

Azure APIM တွင် inbound policy တစ်ခု ထည့်သွင်းပြီး `<validate-jwt>` policy ကို အသုံးပြု၍ လာရောက်သော JWT များကို သင့် Spring Authorization Server နှင့် နှိုင်းယှဉ်စစ်ဆေးပါ။ ရိုးရှင်းသော setup အတွက် OpenID Connect metadata URL ကို အသုံးပြုနိုင်သည်။ ဥပမာ policy snippet-

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

ဤ policy သည် APIM ကို Spring Auth Server မှ OpenID configuration ကို ရယူရန်၊ JWKS ကို ရယူရန်နှင့် token တစ်ခုချင်းစီသည် ယုံကြည်စိတ်ချရသော key ဖြင့် လက်မှတ်ရေးထိုးထားပြီး audience မှန်ကန်မှုရှိကြောင်း စစ်ဆေးရန် ပြောကြားသည်။ (`<issuers>` ကို မထည့်ပါက APIM သည် metadata မှ issuer claim ကို အလိုအလျောက် အသုံးပြုမည်)။ `<audience>` သည် token အတွင်း client ID သို့မဟုတ် API resource identifier နှင့် ကိုက်ညီရမည် (အထက်ပါ ဥပမာတွင် `"mcp-client"` ဟု သတ်မှတ်ထားသည်)။ ၎င်းသည် Microsoft ၏ `validate-jwt` နှင့် `<openid-config>` အသုံးပြုမှုဆိုင်ရာ စာရွက်စာတမ်းနှင့် ကိုက်ညီသည် ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))။

စစ်ဆေးပြီးနောက် APIM သည် request ကို (မူလ `Authorization` header ပါဝင်သည့်) backend သို့ ပို့ဆောင်မည်။ Spring app သည် resource server ဖြစ်သောကြောင့် token ကို ထပ်မံစစ်ဆေးမည်ဖြစ်သော်လည်း APIM သည် token ၏ တရားဝင်မှုကို အရင်စစ်ဆေးပြီးဖြစ်သည်။ (ဖွံ့ဖြိုးရေးအတွက် APIM ၏ စစ်ဆေးမှုကို အခြေခံပြီး app ၏ ထပ်မံစစ်ဆေးမှုကို ပိတ်ထားနိုင်သော်လည်း နှစ်ဖက်စစ်ဆေးထားသည့်အခြေအနေမှာ ပိုလုံခြုံသည်)။

## ဥပမာ ဆက်တင်များ

| ဆက်တင်အမည်       | ဥပမာတန်ဖိုး                                                        | မှတ်ချက်                                  |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | သင့် Container App ၏ URL (base URI)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | Default Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | Default JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery document (auto-generated)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID သို့မဟုတ် API resource name       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` သည် ဤ URL ကို အသုံးပြုသည် ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## အထူးသတိပြုရန် အချက်များ

- **HTTPS/TLS:** APIM gateway သည် OpenID/JWKS endpoint ကို HTTPS နှင့် တရားဝင် certificate ဖြင့်သာ လက်ခံသည်။ Default အနေဖြင့် Azure Container Apps သည် Azure-managed domain အတွက် ယုံကြည်စိတ်ချရသော TLS certificate ကို ပေးသည် ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))။ Custom domain အသုံးပြုပါက certificate ကို bind လုပ်ရန် သေချာပါ (Azure ၏ အခမဲ့ managed cert feature ကို အသုံးပြုနိုင်သည်) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))။ APIM သည် endpoint ၏ certificate ကို ယုံကြည်မရပါက `<validate-jwt>` သည် metadata ရယူမှု မအောင်မြင်ပါ။

- **Endpoint ရောက်ရှိနိုင်မှု:** Spring app ၏ endpoints များကို APIM မှ ရောက်ရှိနိုင်ရန် သေချာစေပါ။ `--ingress external` (သို့မဟုတ် portal တွင် ingress ကို enabled) သည် အလွယ်တကူဆုံးဖြစ်သည်။ Internal သို့မဟုတ် vNet-bound ပတ်ဝန်းကျင်ကို ရွေးချယ်ပါက APIM (default public) သည် တူညီသော VNet တွင် မရှိပါက ရောက်ရှိနိုင်မှု မရှိနိုင်ပါ။ စမ်းသပ်ပတ်ဝန်းကျင်တွင် public ingress ကို ဦးစားပေးသုံးပါ၊ APIM သည် `.well-known` နှင့် `/jwks` URLs များကို ခေါ်ယူနိုင်ရန်ဖြစ်သည်။

- **OpenID Discovery ဖွင့်ထားခြင်း:** Default အနေဖြင့် Spring Authorization Server သည် `/.well-known/openid-configuration` ကို မဖော်ပြပါ၊ OIDC ကို enabled လုပ်ထားမှသာ ဖြစ်သည်။ Security config တွင် `.oidc(Customizer.withDefaults())` ထည့်သွင်းထားရန် သေချာပါ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))။ မဟုတ်ပါက APIM ၏ `<openid-config>` ခေါ်ဆိုမှုသည် 404 ဖြစ်မည်။

- **Audience Claim:** Spring ၏ default အပြုအမူမှာ `aud` claim ကို client ID သတ်မှတ်သည်။ APIM ၏ `<audience>` စစ်ဆေးမှု မအောင်မြင်ပါက token ကို ပြင်ဆင်ရန် (အထက်ပါအတိုင်း) သို့မဟုတ် APIM policy ကို ပြင်ဆင်ရန် လိုအပ်နိုင်သည်။ JWT ၏ audience သည် `<audience>` တွင် သတ်မှတ်ထားသည့် တန်ဖိုးနှင့် ကိုက်ညီရမည်။

- **JSON Metadata Parsing:** OpenID configuration JSON သည် မှန်ကန်ရမည်။ Spring ၏ default config သည် standard OIDC metadata document ကို ထုတ်ပေးမည်။ issuer နှင့် jwks_uri တို့မှန်ကန်မှုကို စစ်ဆေးပါ။ Spring ကို proxy သို့မဟုတ် path-based route အောက်တွင် host လုပ်ပါက metadata တွင် URL များကို သေချာစစ်ဆေးပါ။ APIM သည် ၎င်းတန်ဖိုးများကို တိတိကျကျ အသုံးပြုမည်။

- **Policy အဆင့်သတ်မှတ်ခြင်း:** APIM policy တွင် `<validate-jwt>` ကို backend သို့ routing မပြုမီ **ရှေ့တွင်**ထားပါ။ မဟုတ်ပါက valid token မပါဘဲ app သို့ ခေါ်ဆိုမှုများ ရောက်ရှိနိုင်သည်။ `<validate-jwt>` သည် `<inbound>` အောက်တွင် တိုက်ရိုက် ရှိရမည် (အခြား condition အတွင်း မရှိရ)၊ APIM သည် ၎င်းကို အကောင်အထည်ဖော်မည်။

အထက်ပါ အဆင့်များကို လိုက်နာခြင်းဖြင့် သင်၏ Spring AI MCP server ကို Azure Container Apps တွင် တပ်ဆင်နိုင်ပြီး Azure API Management သည် လာရောက်သော OAuth2 JWT များကို အနည်းဆုံး policy ဖြင့် စစ်ဆေးပေးနိုင်မည်ဖြစ်သည်။ အဓိကအချက်များမှာ - Spring Auth endpoints များကို TLS ဖြင့် public access ဖြင့် ဖော်ပြခြင်း၊ OIDC discovery ကို enabled လုပ်ခြင်း၊ APIM ၏ `validate-jwt` ကို OpenID config URL သို့ ရည်ညွှန်းခြင်းဖြစ်သည်။ ဤ setup သည် dev/test ပတ်ဝန်းကျင်အတွက် သင့်တော်ပြီး production အတွက် secret management, token lifetime, JWKS key rotation စသည့် အချက်များကို သေချာစွာ စီမံရန် လိုအပ်သည်။
**အညွှန်းများ:** Spring Authorization Server စာရွက်စာတမ်းများတွင် default endpoints များအတွက် ကြည့်ရှုနိုင်ပါသည် ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) နှင့် OIDC configuration အတွက် ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); Microsoft APIM စာရွက်စာတမ်းများတွင် `validate-jwt` နမူနာများအတွက် ကြည့်ရှုနိုင်ပါသည် ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); နှင့် Azure Container Apps စာရွက်စာတမ်းများတွင် deployment နှင့် certificates အတွက် ကြည့်ရှုနိုင်ပါသည် ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။