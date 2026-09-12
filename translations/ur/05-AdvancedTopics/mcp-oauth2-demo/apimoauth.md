# اسپرنگ AI MCP ایپ کو Azure Container Apps پر تعینات کرنا

> [!WARNING]
> یہ مشترکہ اجازت / وسائل سرور سیکھنے اور
> ترقی / تجربہ کے استعمال کے لیے ہے۔ پیداواری نظاموں کو ایک اختصاصی شناخت فراہم کرنے والے،
> مستقل سائننگ کیز، اور منظم خفیہ اسٹور میں محفوظ اسناد استعمال کرنی چاہیے۔

 ([OAuth2 کے ساتھ Spring AI MCP سرور کو محفوظ بنانا](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *تصویر: Spring Authorization Server کے ساتھ محفوظ شدہ Spring AI MCP سرور۔ سرور کلائنٹس کو رسائی کے ٹوکن جاری کرتا ہے اور آنے والی درخواستوں پر ان کی تصدیق کرتا ہے (ماخذ: Spring بلاگ) ([OAuth2 کے ساتھ Spring AI MCP سرور کو محفوظ بنانا](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP سرور کو تعینات کرنے کے لیے، اسے کنٹینر کے طور پر بنائیں اور Azure Container Apps کو بیرونی انگریس کے ساتھ استعمال کریں۔ مثال کے طور پر، Azure CLI استعمال کرتے ہوئے آپ چل سکتے ہیں:

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

یہ ایک عوامی رسائی کے قابل Container App بناتا ہے جس میں HTTPS فعال ہے (Azure ڈیفالٹ `*.azurecontainerapps.io` ڈومین کے لیے مفت TLS سرٹیفکیٹ جاری کرتا ہے ([Azure Container Apps میں کسٹم ڈومین نام اور مفت منظم سرٹیفکیٹس | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)))۔ کمانڈ کے آؤٹ پٹ میں ایپ کا FQDN شامل ہوتا ہے (مثلاً `my-mcp-app.eastus.azurecontainerapps.io`)، جو **issuer URL** بیس بن جاتا ہے۔ HTTP انگریس کو فعال کرنا یقینی بنائیں (جیسا کہ اوپر ہے) تاکہ APIM ایپ تک پہنچ سکے۔ ٹیسٹ / ترقیاتی سیٹ اپ میں، `--ingress external` آپشن استعمال کریں (یا TLS کے ساتھ کسٹم ڈومین باندھیں جیسا کہ [Microsoft دستاویزات](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Azure Container Apps میں کسٹم ڈومین نام اور مفت منظم سرٹیفکیٹس | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))) میں بیان کیا گیا ہے۔ کسی بھی حساس خصوصیات (جیسے OAuth کلائنٹ سیکرٹس) کو Container Apps کے خفیہ ذخیرہ یا Azure کی والٹ میں محفوظ کریں، اور انہیں کنٹینر میں ماحول کے متغیرات کے طور پر نقش کریں۔

## Spring Authorization Server کی ترتیب

اپنی Spring Boot ایپ کے کوڈ میں، Spring Authorization Server اور Resource Server starters شامل کریں۔ ایک `RegisteredClient` تشکیل دیں (dev/test میں `client_credentials` گرانٹ کے لیے) اور ایک JWT کی سورس۔ مثال کے طور پر، `application.properties` میں آپ سیٹ کر سکتے ہیں:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

اجازت سرور اور وسائل سرور کو ایک سیکیورٹی فلٹر چین کی تعریف کر کے فعال کریں۔ مثال کے طور پر:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // اجازت دہندہ سرور کے اینڈ پوائنٹس کو فعال کریں
            .apply(authzServer.and())
            // وسائل کے سرور کو فعال کریں (آنے والی درخواستوں پر JWT کی توثیق کریں)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // CSRF کو غیر فعال کریں (MCP سرور براؤزر پر مبنی نہیں ہے)
            .csrf(csrf -> csrf.disable())
            // کلائنٹ ڈیمو ٹولز کے لیے CORS کی اجازت دیں
            .cors(withDefaults());
        return http.build();
    }

    // ایک ان میموری کلائنٹ (RegisteredClient) اور JWK ذريعہ کی تعریف کریں:
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
        // ایک RSA کلید بنائیں (ڈویلپمنٹ/ٹیسٹ کے لیے، ابتدائی شروع میں نئی پیدا کریں)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

یہ ترتیب ڈیفالٹ OAuth2 اینڈپوائنٹس کو ظاہر کرے گی: ٹوکن کے لیے `/oauth2/token` اور JSON Web Key Set کے لیے `/oauth2/jwks`۔ (ڈیفالٹ کے طور پر Spring کا `AuthorizationServerSettings` `/oauth2/token` اور `/oauth2/jwks` کو میپ کرتا ہے ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) سرور JWT رسائی کے ٹوکن جاری کرے گا جو اوپر کے RSA کلید سے دستخط شدہ ہوں گے، اور اپنی عوامی کلید `https://<your-app>:/oauth2/jwks` پر شائع کرے گا۔

**OpenID Connect دریافت کو فعال کریں:** تاکہ APIM خودکار طور پر issuer اور JWKS حاصل کر سکے، `.oidc(Customizer.withDefaults())` کو اپنی سیکیورٹی کنفیگریشن میں شامل کریں ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))۔ مثال کے طور پر:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– /.well-known/openid-configuration کو فعال کرتا ہے
```

یہ `/.well-known/openid-configuration` کو ظاہر کرتا ہے، جسے APIM میٹا ڈیٹا کے لیے استعمال کر سکتا ہے۔ آخر میں، آپ JWT کے **audience** کلیم کو حسب ضرورت بنانا چاہیں گے تاکہ APIM کا `<audiences>` چیک کامیاب ہو جائے۔ مثال کے طور پر، ایک ٹوکن کسٹمائزر شامل کریں:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // ایک حسب ضرورت سامعین مقرر کریں (مثلاً کلائنٹ ID یا API شناخت کار)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

یہ یقینی بناتا ہے کہ ٹوکن `"aud": ["mcp-client"]` لے کر آتے ہیں، جو APIM کی توقع کے مطابق کلائنٹ ID یا سکوپ سے میل کھاتا ہے۔

## ٹوکن اور JWKS اینڈپوائنٹس کو ظاہر کرنا

تعیناتی کے بعد، آپ کی ایپ کا **issuer URL** ہوگا `https://<app-fqdn>`، مثلاً `https://my-mcp-app.eastus.azurecontainerapps.io`۔ اس کے OAuth2 اینڈپوائنٹس ہیں:

- **ٹوکن اینڈپوائنٹ:** `https://<app-fqdn>/oauth2/token` – کلائنٹس یہاں سے ٹوکن حاصل کرتے ہیں (client_credentials فلو)۔
- **JWKS اینڈپوائنٹ:** `https://<app-fqdn>/oauth2/jwks` – JWK سیٹ واپس کرتا ہے (APIM دستخطی چابیاں حاصل کرنے کے لیے استعمال کرتا ہے)۔
- **OpenID کنفیگریشن:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC دریافت JSON (جس میں `issuer`، `token_endpoint`، `jwks_uri` وغیرہ شامل ہیں)۔

APIM **OpenID کنفیگریشن URL** کی طرف اشارہ کرے گا، جہاں سے یہ `jwks_uri` دریافت کرتا ہے۔ مثال کے طور پر، اگر آپ کا Container App FQDN `my-mcp-app.eastus.azurecontainerapps.io` ہے، تو APIM کا `<openid-config url="...">` کو `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` استعمال کرنا چاہیے۔ (ڈیفالٹ کے طور پر Spring اس میٹا ڈیٹا میں `issuer` کو وہی بیس URL سیٹ کرتا ہے ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))۔)

## Azure API مینجمنٹ کی ترتیب (`validate-jwt`)

Azure APIM میں ایک inbound پالیسی شامل کریں جو `<validate-jwt>` پالیسی کا استعمال کرتے ہوئے آنے والے JWTs کو آپ کے Spring Authorization Server کے خلاف چیک کرے۔ ایک آسان ترتیب کے لیے، آپ OpenID Connect میٹا ڈیٹا URL استعمال کر سکتے ہیں۔ پالیسی کا مثال ٹکڑا:

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

یہ پالیسی APIM کو کہتی ہے کہ Spring Auth Server سے OpenID کنفیگریشن حاصل کرے، اس کا JWKS لے، اور ہر ٹوکن کی تصدیق کرے کہ وہ ایک معتبر کلید سے دستخط شدہ ہے اور درست audience رکھتا ہے۔ (اگر آپ `<issuers>` کو چھوڑ دیں تو APIM خود بخود میٹا ڈیٹا سے `issuer` کلیم استعمال کرے گا)۔ `<audience>` آپ کے کلائنٹ ID یا API وسائل کے شناخت کنندہ سے میل کھانا چاہیے (اوپر دی گئی مثال میں ہم نے اسے `"mcp-client"` پر سیٹ کیا ہے)۔ یہ Microsoft کی دستاویزات کے مطابق ہے کہ `validate-jwt` کو `<openid-config>` کے ساتھ کیسے استعمال کریں ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))۔

تصدیق کے بعد، APIM درخواست کو اصل `Authorization` ہیڈر سمیت بیک اینڈ کو فارورڈ کرے گا۔ چونکہ Spring ایپ بھی ایک وسائل سرور ہے، یہ ٹوکن کو دوبارہ تصدیق کرے گا، لیکن APIM پہلے ہی اس کی صحت مندی کا یقین کر چکا ہوتا ہے۔ (ترقیاتی مراحل میں، آپ APIM کے چیک پر انحصار کر سکتے ہیں اور اگر چاہیں تو ایپ میں اضافی چیکس غیر فعال کر سکتے ہیں، لیکن دونوں کو رکھنا محفوظ ہے۔)

## مثال کی ترتیبات

| سیٹنگ            | مثال کی قیمت                                                        | نوٹس                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | آپ کی Container App کا URL (بنیادی URI)     |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | ڈیفالٹ Spring ٹوکن اینڈپوائنٹ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | ڈیفالٹ JWK سیٹ اینڈپوائنٹ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC دریافت دستاویز (خودکار طور پر تیار)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth کلائنٹ ID یا API وسائل کا نام          |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` اس URL کا استعمال کرتا ہے ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## عام مسائل

- **HTTPS/TLS:** APIM گیٹ وے کے لیے ضروری ہے کہ OpenID/JWKS اینڈپوائنٹ HTTPS ہو اور اس کے پاس ایک درست سرٹیفکیٹ ہونا چاہیے۔ ڈیفالٹ کے طور پر، Azure Container Apps Azure کے زیر انتظام ڈومین کے لیے قابل اعتماد TLS سرٹیفکیٹ فراہم کرتا ہے ([Azure Container Apps میں کسٹم ڈومین نام اور مفت منظم سرٹیفکیٹس | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))۔ اگر آپ کسٹم ڈومین استعمال کرتے ہیں، تو سرٹیفکیٹ کا بندھن یقینی بنائیں (آپ Azure کی مفت منظم سرٹیفکیٹ خصوصیت استعمال کر سکتے ہیں) ([Azure Container Apps میں کسٹم ڈومین نام اور مفت منظم سرٹیفکیٹس | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))۔ اگر APIM اینڈپوائنٹ کے سرٹیفکیٹ پر اعتماد نہیں کر پاتا تو `<validate-jwt>` میٹا ڈیٹا حاصل کرنے میں ناکام ہو جائے گا۔

- **اینڈپوائنٹ کی دستیابی:** یقینی بنائیں کہ Spring ایپ کے اینڈپوائنٹس APIM سے قابل رسائی ہوں۔ `--ingress external` استعمال کرنا (یا پورٹل میں انگریس کو فعال کرنا) سب سے آسان ہے۔ اگر آپ نے اندرونی یا vNet بند ماحول منتخب کیا ہے، تو APIM (جو ڈیفالٹ میں عوامی ہوتا ہے) ممکن ہے کہ اسے اس صورت میں نہ پہنچ پائے جب تک کہ وہ ایک ہی vNet میں نہ رکھا جائے۔ تجرباتی سیٹ اپ میں، عوامی انگریس کو ترجیح دیں تاکہ APIM `.well-known` اور `/jwks` URLs کال کر سکے۔

- **OpenID دریافت فعال ہے:** ڈیفالٹ کے طور پر، Spring Authorization Server `/.well-known/openid-configuration` ظاہر نہیں کرتا جب تک کہ OIDC فعال نہ کیا جائے۔ یقینی بنائیں کہ اپنی سیکیورٹی کنفیگریشن میں `.oidc(Customizer.withDefaults())` شامل ہو (جیسے اوپر ہے) تاکہ پرووائیڈر کنفیگریشن اینڈپوائنٹ فعال ہو ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))۔ ورنہ APIM کی `<openid-config>` کال 404 دے گی۔

- **Audience کلیم:** Spring کا ڈیفالٹ رویہ `aud` کلیم کو کلائنٹ ID پر سیٹ کرنا ہے۔ اگر APIM کا `<audience>` چیک ناکام ہو جاتا ہے، تو آپ کو ممکنہ طور پر ٹوکن حسب ضرورت بنانا ہوگا (جیسا کہ اوپر دکھایا گیا ہے) یا APIM پالیسی کو ایڈجسٹ کرنا ہوگا۔ یقینی بنائیں کہ JWT میں audience اس کے مطابق ہو جو آپ `<audience>` میں ترتیب دیتے ہیں۔

- **JSON میٹا ڈیٹا کی تجزیہ:** OpenID کنفیگریشن JSON درست ہونا چاہیے۔ Spring کی ڈیفالٹ ترتیب ایک معیاری OIDC میٹا ڈیٹا دستاویز جاری کرے گی۔ تصدیق کریں کہ اس میں درست `issuer` اور `jwks_uri` شامل ہیں۔ اگر آپ Spring کو پروکسی یا راستہ-بنیاد روٹ کے پیچھے ہوسٹ کرتے ہیں، تو اس میٹا ڈیٹا میں URLs دوبارہ چیک کریں۔ APIM ان اقدار کو جیسا ہے ویسا استعمال کرے گا۔

- **پالیسی کی ترتیب:** APIM پالیسی میں، `<validate-jwt>` کو بیک اینڈ کی کسی بھی روٹنگ سے **پہلے** رکھیں۔ ورنہ کالز آپ کی ایپ تک بغیر معتبر ٹوکن کے پہنچ سکتی ہیں۔ یقینی بنائیں کہ `<validate-jwt>` `<inbound>` کے فوراً نیچے ہو (کسی دوسرے شرط کے اندر نہ ہو) تاکہ APIM اسے لاگو کرے۔

اوپر دیے گئے مراحل پر عمل کرکے، آپ اپنا Spring AI MCP سرور Azure Container Apps میں چلا سکتے ہیں اور Azure API مینجمنٹ کو آنے والے OAuth2 JWTs کی کم سے کم پالیسی کے ساتھ تصدیق کرنے دے سکتے ہیں۔ اہم نکات یہ ہیں: Spring Auth اینڈپوائنٹس کو TLS کے ساتھ عوامی طور پر ظاہر کریں، OIDC دریافت کو فعال کریں، اور APIM کے `validate-jwt` کو OpenID کنفیگریشن URL کی طرف اشارہ کریں (تاکہ یہ JWKS خودکار طریقے سے حاصل کر سکے)۔ یہ ترتیب ترقی / تجربہ کے ماحول کے لیے مناسب ہے؛ پیداواری ماحول کے لیے مناسب خفیہ انتظام، ٹوکن کی زندگی، اور JWKS میں چابیاں گھمانے پر غور کریں جیسا کہ ضرورت ہو۔


**حوالہ جات:** ڈیفالٹ اینڈپوائنٹس کے لیے Spring Authorization Server کی دستاویزات دیکھیں ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) اور OIDC کنفیگریشن ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); `validate-jwt` کے مثالوں کے لیے Microsoft APIM کی دستاویزات دیکھیں ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); اور Azure Container Apps کی تعیناتی اور سرٹیفکیٹس کے لیے دستاویزات دیکھیں ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->