# Spring AI MCP အက်ပ်ကို Azure Container Apps တွင် ဖြန့်ချိခြင်း

> [!WARNING]
> ဤပေါင်းစပ်ခွင့်ပြုချက်/ရင်းမြစ်ဆာဗာသည် သင်ယူခြင်းနှင့်
> လေ့လာစမ်းသပ်မှုများအတွက်သာ ရည်ရွယ်ထားသည်။ ထုတ်လုပ်မှုစနစ်များမှာ မူရင်းသက်တမ်းနှင့် တည်ရှိသော လက်မှတ်များ၊ လျှို့ဝှက်စာရင်းများကို စီမံခန့်ခွဲသော လျှို့ဝှက်အရင်းအမြစ်များတွင် သိမ်းဆည်းထားသင့်သည်။




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

၎င်းသည် HTTPS ဖြင့် public အားဖြင့် ဝင်ရောက်နိုင်သော Container App တစ်ခုကို ဖန်တီးသည် (Azure သည် ပုံမှန် `*.azurecontainerapps.io` ဒိုမိန်းအတွက် အခမဲ့ TLS လက်မှတ်ထုတ်ပေးသည် ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). အမိန့်၏ output တွင် အက်ပ်၏ FQDN ပါဝင်ပြီး (ဥပမာ `my-mcp-app.eastus.azurecontainerapps.io`), ၎င်းသည် **issuer URL** အခြေခံဖြစ်သွားသည်။ HTTP ingress ကို အထက်ဖော်ပြပါအတိုင်း enabled လုပ်ထားမှ APIM အက်ပ်သို့ များပြောနိုင်ပါသည်။ စမ်းသပ်/ဖွံ့ဖြိုးရေး ပတ်ဝန်းကျင်တွင် `--ingress external` option ကို သုံးပါ (သို့မဟုတ် TLS ဖြင့် custom domain ကို [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)) ပြုလုပ်၍ bind လုပ်ပါ). OAuth client secrets ကဲ့သို့သော အချက်အလက်များကို Container Apps secrets သို့မဟုတ် Azure Key Vault တွင် သိမ်းဆည်းပြီး container ထဲတွင် environment variables အဖြစ် မြှုပ်နှံပါ။

## Spring Authorization Server ကို ဖန်တီးခြင်း

သင့် Spring Boot အက်ပ်၏ code တွင် Spring Authorization Server နှင့် Resource Server starters များ ပါဝင်စေပါ။ `RegisteredClient` (dev/test အတွက် `client_credentials` grant အတွက်) နှင့် JWT key source ကို ဆက်တင်ပါ။ ဥပမာ `application.properties` တွင် အောက်ပါအတိုင်း ရေးသွင်းနိုင်သည်-

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Authorization Server နှင့် Resource Server ကို security filter chain သတ်မှတ်ခြင်းဖြင့် enabled ဖွင့်ပါ။ ဥပမာ-

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Authorization Server endpoints ကို ဖွင့်ပါ
            .apply(authzServer.and())
            // Resource Server ကို ဖွင့်ပါ (ဝင်ရောက်လာသော တောင်းဆိုမှုများတွင် JWT ကို စစ်ဆေးပါ)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF ကို ပိတ်ပါ (MCP server သည် browser အခြေခံ မဟုတ်ပါ)
            .csrf(csrf -> csrf.disable())
            // client demo tools များအတွက် CORS ခွင့်ပြုပါ
            .cors(withDefaults());
        return http.build();
    }

    // in-memory client (RegisteredClient) နှင့် JWK source ကို သတ်မှတ်ပါ
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
        // RSA key ကို ဖန်တီးပါ (ဖွံ့ဖြိုးရေး/စမ်းသပ်မှုအတွက်၊ startup မှာအသစ်ဖန်တီးပေးပါ)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ဤစနစ်ဖြင့် ပုံမှန် OAuth2 endpoints များဖြစ်သော `/oauth2/token` (token များအတွက်) နှင့် `/oauth2/jwks` (JSON Web Key Set အတွက်) ကို access လုပ်နိုင်ပါသည်။ (ပုံမှန်အားဖြင့် Spring ၏ `AuthorizationServerSettings` သည် `/oauth2/token` နှင့် `/oauth2/jwks` ကို mapping လုပ်သည် ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) ဆာဗာသည် RSA ကီးဖြင့် လက်မှတ်ရေးထိုးထားသော JWT access token များ ထုတ်ပေးပြီး ၎င်း၏ public key ကို `https://<your-app>:/oauth2/jwks` တွင် မျှဝေပါမည်။

**OpenID Connect discovery ကို enabled လုပ်ခြင်း:** APIM ဖြင့် issuer နှင့် JWKS ကို အလိုအလျောက် ရယူနိုင်ရန် security configuration တွင် `.oidc(Customizer.withDefaults())` ကို ထည့်သွင်း၍ OIDC provider configuration endpoint ကို enable ပြုလုပ်ပါ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))။ ဥပမာ-

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration ကို ဖွင့်လှစ်ရန် ခွင့်ပြုသည်။
```

၎င်းက `/.well-known/openid-configuration` ကို ဖော်ပြသွားပြီး APIM သည် ဤနေရာမှ metadata ရယူနိုင်ပါသည်။ အဆုံးတွင် JWT **audience** claim ကို စိတ်ကြိုက်ပြင်ဆင်လိုပါက token customizer တစ်ခု ထည့်သွင်းနိုင်သည်-

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // ပုဂ္ဂိုလ်ရေးအသံအုပ်စုတစ်ခုသတ်မှတ်ပါ (ဥပမာ - client ID သို့မဟုတ် API အမှတ်စဉ်)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

၎င်းသည် token များတွင် `"aud": ["mcp-client"]` ပါဝင်ရန် သေချာစေပြီး APIM မှ မျှော်လင့်သော client ID သို့မဟုတ် scope နှင့် တွဲလျက်ဖြစ်စေသည်။

## Token နှင့် JWKS Endpoints များကို ထုတ်ဖော်ခြင်း

ဖြန့်ချိပြီးနောက် သင့်အက်ပ်၏ **issuer URL** သည် `https://<app-fqdn>` ဖြစ်မည်၊ ဥပမာ `https://my-mcp-app.eastus.azurecontainerapps.io` ဖြစ်သည်။ ၎င်း၏ OAuth2 endpoints များမှာ-

- **Token endpoint:** `https://<app-fqdn>/oauth2/token` – client များက token များရယူရာနေရာ (client_credentials flow)။
- **JWKS endpoint:** `https://<app-fqdn>/oauth2/jwks` – JWK set ကို ပြန်ပေးသည် (APIM သည် signing keys ရယူရာတွင်အသုံးပြု)။
- **OpenID Config:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC discovery JSON (issuer, token_endpoint, jwks_uri စသည်တို့ပါဝင်သည်)။

APIM သည် **OpenID configuration URL** ကို ရည်ညွှန်းပြီး ၎င်းမှ `jwks_uri` ကို ရှာဖွေပါသည်။ ဥပမာ၊ သင့် Container App FQDN が `my-mcp-app.eastus.azurecontainerapps.io` ဖြစ်လျှင် APIM ၏ `<openid-config url="...">` သည် `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` ကို အသုံးပြုသင့်သည်။ (ပုံမှန်အားဖြင့် Spring သည် ဤ metadata တွင် issuer ကို အခြေခံ URL နှင့် တူညီစွာ သတ်မှတ်သည် ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Azure API Management (`validate-jwt`) ကို ဖန်တီးခြင်း

Azure APIM တွင် inbound policy အဖြစ် `<validate-jwt>` ကို အသုံးပြု၍ Spring Authorization Server နှင့် တိုက်ဆိုင်စစ်ဆေးမှုလုပ်ဆောင်ပါ။ ရိုးရှင်းသော စနစ်တွင် OpenID Connect metadata URL ကို အသုံးပြုနိုင်သည်။ ဥပမာ policy snippet-

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

၎င်းမှ APIM သည် Spring Auth Server မှ OpenID configuration ကို ရယူပြီး ၎င်း၏ JWKS ကို ရယူကာ တိုက်ဆိုင်ရမည့် token များသည် ယုံကြည်စိတ်ချရသော key ဖြင့် လက်မှတ်ရေးထိုးထားပြီး 正確 な audience を 持っているか 確認する よう 指示します。 (`<issuers>` ကို မထည့်ပါက APIM သည် metadata မှ `issuer` claim ကို အလိုအလျောက် အသုံးပြုမည်။) `<audience>` သည် သင့် client ID သို့မဟုတ် API resource အမည်နှင့် ကိုက်ညီရမည် (ဥပမာ၌ `"mcp-client"` ဖြစ်သည်)။ ၎င်းသည် Microsoft ၏ `validate-jwt` နှင့် `<openid-config>` အသုံးပြုမှုဆိုင်ရာ စာရွက်စာတမ်းနှင့် ကိုက်ညီသည် ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))။

စစ်ဆေးပြီးနောက် APIM သည် မူရင်း `Authorization` header ပါအောင် တောင်းဆိုမှုကို backend သို့ ရောက်အောင် ပို့ပေးမည်။ Spring app သည် resource server ဖြစ်သောကြောင့် ခုလက်ရှိ token ကို ထပ်မံ စစ်ဆေးမည်ဖြစ်သော်လည်း APIM သည် အတည်ပြုထားပြီးဖြစ်သည်။ (ဖွံ့ဖြိုးရေးအတွက် APIM စစ်ဆေးမှုကို အားကိုး၍ အက်ပ်အတွင်း စစ်ဆေးမှုများကို ပိတ်ထားနိုင်သည်၊ သို့သော် နှစ်ဖက်စစ်ဆေးမှု ကောင်းမွန်သည်)။

## ဥပမာ ဆက်တင်များ

| ဆက်တင်               | ဥပမာတန်ဖိုး                                                     | မှတ်ချက်                                  |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | သင့် Container App ၏ URL (base URI)       |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | ပုံမှန် Spring token endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | ပုံမှန် JWK Set endpoint ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC discovery စာရွက်စာတမ်း (auto-generated)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth client ID သို့မဟုတ် API resource အမည်       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` သည် ဤ URL ကို အသုံးပြုသည် ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## အထွေထွေ ကျရှုံးဆဲွမှုများ

- **HTTPS/TLS:** APIM gateway သည် OpenID/JWKS endpoint ကို HTTPS နှင့် တရားဝင်လက်မှတ်ဖြင့် မပြုမီ အတည်ပြုရန် လိုအပ်သည်။ ပုံမှန်အားဖြင့် Azure Container Apps သည် Azure ရည်ညွှန်းသော domain အတွက် ယုံကြည်စိတ်ချရသော TLS လက်မှတ်ကို ပေးသည် ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))။ custom domain အသုံးပြုပါက လက်မှတ်ကို bind လုပ်မှာ ဖြစ်ပြီး Azure ၏ အခမဲ့ managed cert feature ကို သုံးနိုင်သည် ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))။ APIM သည် endpoint ၏လက်မှတ်ကို ယုံကြည်မရပါက `<validate-jwt>` သည် metadata ရယူမှု မအောင်မြင်နိုင်ပါ။

- **Endpoint ဝင်ရောက်နိုင်ခြင်း:** Spring app ၏ endpoints များသည် APIM မှ ဝင်ရောက်နိုင်ကြောင်း သေချာစေရန်လိုသည်။ `--ingress external` သို့မဟုတ် portal တွင် ingress ဖွင့်ခြင်းကို အသုံးပြုပါ။ internal သို့မဟုတ် vNet ပြဿနာရှိသောပတ်ဝန်းကျင်တစ်ခုကိုရွေးချယ်ပါက APIM (ပုံမှန်အားဖြင့် public) သည် အဲဒီမှာမရောက်နိုင်ဘူး၊ သို့ဖြစ်လျှင် APIM သည် တူညီသော VNet တွင်ထားရမည်။ စမ်းသပ်မှုအတွက် public ingress ကို နှစ်သက်သည်။ အဲဒါက APIM သည် `.well-known` နှင့် `/jwks` URL များကို အလုပ်လုပ်စေပါသည်။

- **OpenID Discovery Enabled:** ပုံမှန်အားဖြင့် Spring Authorization Server သည် OIDC enable လုပ်ထားခြင်းမရှိလျှင် `/.well-known/openid-configuration` ကို မဖေါ်ပြပါ။ security config တွင် `.oidc(Customizer.withDefaults())` ထည့်သွင်းထားမှုရှိကြောင်း သေချာစေပါ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))။ မဟုတ်လျှင် APIM ၏ `<openid-config>` ခေါ်ဆိုမှုသည် 404 ပြချိန်မျှသာ ဖြစ်စေနိုင်သည်။

- **Audience Claim:** Spring မှ ပုံမှန်အားဖြင့် `aud` claim ကို client ID အဖြစ် သတ်မှတ်ထားသည်။ APIM ၏ `<audience>` စစ်ဆေးမှု မအောင်မြင်လျှင် token ကို စိတ်ကြိုက်ပြင်ဆင်ပေးရန် လိုအပ်နိုင်သည် (အထက်တွင် ဖော်ပြထားသည့် အတိုင်း) သို့မဟုတ် APIM policy ကို ပြင်ဆင်ပါ။ JWT ၏ audience သည် `<audience>` တွင် သတ်မှတ်ထားသည့်အရာနှင့် ကိုက်ညီစေရန် သေချာစေပါ။

- **JSON Metadata Parsing:** OpenID configuration JSON သည် တိကျမှန်ကန်ရမည်။ Spring ၏ ပုံမှန် configuration သည် စံ OIDC metadata စာရွက်စာတမ်းကို ထုတ်ပေးသည်။ `issuer` နှင့် `jwks_uri` များမှန်ကန် ဖော်ပြထားကြောင်း အတည်ပြုပါ။ Spring ကို proxy သို့မဟုတ် path-based route အောက်တွင် host လုပ်ပါက metadata တွင် URL များကို သေချာစွာ စစ်ဆေးပါ။ APIM သည် အဲဒီတန်ဖိုးများကို အတိုင်းအသုံးပြုပါမည်။

- **Policy Ordering:** APIM policy တွင် `<validate-jwt>` ကို backend သို့ လမ်းညွှန်မှုမလုပ်ခင် အစဥ်လိုက်ထားပါ။ မဟုတ်လျှင် တောင်းဆိုမှုများသည် မမှန်ကန်သော token ဖြင့် သို့မဟုတ် token မရှိဘဲ app သို့ ရောက်နိုင်ပါသည်။ ထို့အပြင် `<validate-jwt>` သည် `<inbound>` ၏ အောက်တွင် တိုက်ရိုက်ရှိစေရန် အာမခံပါ (အခြား condition အတွင်း မထားရ)၊ APIM သည် ထိုနည်းမျှသာ policy ကို အကောင်အထည်ဖော်ပါသည်။

အထက်ဖော်ပြသည့် လမ်းညွှန်ချက်များကို လိုက်နာခြင်းဖြင့် သင်သည် Azure Container Apps တွင် Spring AI MCP ဆာဗာကို လုပ်ဆောင်နိုင်ပြီး Azure API Management သည် OAuth2 JWT များကို အနိမ့်ဆုံး ဖော်ပြထားသော policy ဖြင့် စစ်ဆေးနိုင်မည်ဖြစ်သည်။ အရေးပါသော အချက်များမှာ - Spring Authorization Server ၏ endpoints များကို TLS ဖြင့် ပြင်ပသို့ ထုတ်ဖော်ခြင်း၊ OIDC discovery ကို enabled လုပ်ခြင်း၊ APIM ၏ `validate-jwt` ကို OpenID config URL တွင် ဖြည့်သွင်းခြင်း (JWKS ကို အလိုအလျောက် ရယူရန်) ဖြစ်သည်။ ဤစနစ်သည် dev/test ပတ်ဝန်းကျင်များအတွက်သင့်တော်ပြီး ထုတ်လုပ်မှုအတွက် သီးခြားသော secret စီမံခန့်ခွဲမှု၊ token အသက်တာနှင့် JWKS အတွက် key အလဲအလှယ်များကို ထည့်သွင်းစဉ်းစားပါ။ 


**ရင်းမြစ်များ:** အကယ်၍ အခြေခံ endpoints များအတွက် Spring Authorization Server စာတမ်းများကို ကြည့်ပါ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) နှင့် OIDC ဖွင့်ဆိုချက်များ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); Microsoft APIM စာတမ်းများတွင် `validate-jwt` ဥပမာများအတွက် ကြည့်ပါ ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); နောက်ပြီး Azure Container Apps စာတမ်းများမှ deployment နှင့် certificates များအတွက် ကြည့်ပါ ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->