# استقرار برنامه Spring AI MCP در Azure Container Apps

> [!WARNING]
> این سرور ترکیبی مجوز/منبع برای آموزش و استفاده توسعه/آزمایشی در نظر گرفته شده است. سیستم‌های تولیدی باید از ارائه‌دهنده هویت اختصاصی، کلیدهای امضای پایدار و اعتبارنامه‌های ذخیره‌شده در فروشگاه مخفی مدیریت‌شده استفاده کنند.
> 




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

این دستور یک برنامه کانتینری قابل دسترسی عمومی با HTTPS فعال ایجاد می‌کند (Azure یک گواهی TLS رایگان برای دامنه پیش‌فرض `*.azurecontainerapps.io` صادر می‌کند ([نام‌های دامنه سفارشی و گواهی‌های مدیریت شده رایگان در Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). خروجی دستور شامل نام دامنه کامل برنامه (مانند `my-mcp-app.eastus.azurecontainerapps.io`) است که به عنوان پایه **آدرس صادرکننده** استفاده می‌شود. اطمینان حاصل کنید ورودی HTTP فعال است (همانطور که بالاتر است) تا APIM بتواند به برنامه دسترسی داشته باشد. در یک محیط تست/توسعه، از گزینه `--ingress external` استفاده کنید (یا دامنه سفارشی با TLS طبق [مستندات مایکروسافت](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([نام‌های دامنه سفارشی و گواهی‌های مدیریت شده رایگان در Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). هر خاصیت حساس (مانند کلیدهای مشتری OAuth) را در اسرار Container Apps یا Azure Key Vault ذخیره و به صورت متغیرهای محیطی به کانتینر مپ کنید.

## پیکربندی Spring Authorization Server

در کد برنامه Spring Boot خود، استارت‌رهای Spring Authorization Server و Resource Server را وارد کنید. یک `RegisteredClient` (برای مجوز `client_credentials` در محیط توسعه/تست) و منبع کلید JWT پیکربندی کنید. برای نمونه، در `application.properties` می‌توانید تنظیم کنید:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

با تعریف یک زنجیره فیلتر امنیتی، Authorization Server و Resource Server را فعال کنید. به عنوان مثال:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // فعال‌کردن نقاط پایانی سرور مجوزدهی
            .apply(authzServer.and())
            // فعال‌کردن سرور منبع (اعتبارسنجی JWT در درخواست‌های ورودی)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // غیرفعال‌کردن CSRF (سرور MCP مبتنی بر مرورگر نیست)
            .csrf(csrf -> csrf.disable())
            // اجازه دادن به CORS برای ابزارهای نمایشی کلاینت
            .cors(withDefaults());
        return http.build();
    }

    // تعریف یک کلاینت در حافظه (RegisteredClient) و منبع JWK:
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
        // تولید کلید RSA (برای توسعه/آزمایش، در شروع مجدد کلید جدید تولید شود)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

این تنظیمات نقاط پایانی پیش‌فرض OAuth2 را در معرض قرار می‌دهد: `/oauth2/token` برای توکن‌ها و `/oauth2/jwks` برای مجموعه کلیدهای JSON Web Key. (به طور پیش‌فرض Spring’s `AuthorizationServerSettings` مپ‌های `/oauth2/token` و `/oauth2/jwks` را ایجاد می‌کند ([مدل پیکربندی :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) سرور توکن‌های دسترسی JWT را که با کلید RSA فوق امضا شده‌اند صادر می‌کند و کلید عمومی خود را در `https://<your-app>:/oauth2/jwks` منتشر می‌کند.

**فعال‌سازی کشف OpenID Connect:** برای اینکه APIM بتواند به طور خودکار صادر‌کننده و JWKS را دریافت کند، نقطه پیکربندی ارائه‌دهنده OIDC را با افزودن `.oidc(Customizer.withDefaults())` در پیکربندی امنیتی خود فعال کنید ([مدل پیکربندی :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). مثلاً:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– فعال‌سازی /.well-known/openid-configuration
```

این آدرس `/.well-known/openid-configuration` را در معرض قرار می‌دهد که APIM می‌تواند برای دریافت فراداده‌ها (metadata) از آن استفاده کند. در نهایت، ممکن است بخواهید ادعای مخاطب JWT را به گونه‌ای سفارشی کنید که بررسی `<audiences>` توسط APIM موفق شود. به عنوان مثال، یک توکن کاستومایزر اضافه کنید:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // تنظیم یک گروه هدف سفارشی (مثلاً شناسه مشتری یا شناسه API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

این اطمینان می‌دهد که توکن‌ها مقدار `"aud": ["mcp-client"]` را دارند که با شناسه کلاینت یا دسترسی مورد انتظار APIM مطابقت دارد.

## در معرض قرار دادن نقاط پایانی Token و JWKS

پس از استقرار، آدرس **صادرکننده** برنامه شما `https://<app-fqdn>` خواهد بود، مثلاً `https://my-mcp-app.eastus.azurecontainerapps.io`. نقاط پایانی OAuth2 آن عبارتند از:

- **نقطه پایانی توکن:** `https://<app-fqdn>/oauth2/token` – مشتری‌ها توکن‌ها را از اینجا دریافت می‌کنند (جریان client_credentials).
- **نقطه پایانی JWKS:** `https://<app-fqdn>/oauth2/jwks` – مجموعه کلیدهای JWK را بازمی‌گرداند (که APIM برای دریافت کلیدهای امضا استفاده می‌کند).
- **پیکربندی OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON کشف OIDC (شامل `issuer`، `token_endpoint`، `jwks_uri` و غیره).

APIM به **آدرس پیکربندی OpenID** اشاره می‌کند که از آن `jwks_uri` را کشف می‌کند. برای مثال، اگر نام دامنه برنامه کانتینر شما `my-mcp-app.eastus.azurecontainerapps.io` باشد، آدرس `<openid-config url="...">` در APIM باید `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` باشد. (به طور پیش‌فرض Spring آدرس `issuer` را در این فراداده به همان آدرس پایه تنظیم می‌کند ([مدل پیکربندی :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## پیکربندی Azure API Management (`validate-jwt`)

در Azure APIM، یک سیاست ورودی اضافه کنید که از سیاست `<validate-jwt>` برای اعتبارسنجی JWTهای ورودی بر اساس Spring Authorization Server شما استفاده می‌کند. برای یک پیکربندی ساده می‌توانید از آدرس فراداده OpenID Connect استفاده کنید. نمونه قطعه کد سیاست:

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

این سیاست به APIM می‌گوید که پیکربندی OpenID را از سرور احراز هویت Spring دریافت کرده، JWKS آن را بگیرد، و بررسی کند که هر توکن توسط کلید مورد اعتماد امضا شده و مخاطب (audience) آن صحیح است. (اگر `<issuers>` را حذف کنید، APIM به طور خودکار از ادعای `issuer` در فراداده استفاده خواهد کرد.) `<audience>` باید با شناسه کلاین یا شناسه منبع API در توکن مطابقت داشته باشد (در مثال بالا، ما آن را `"mcp-client"` تنظیم کردیم). این مطابق با مستندات مایکروسافت درباره استفاده از `validate-jwt` با `<openid-config>` است ([مرجع سیاست Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

پس از اعتبارسنجی، APIM درخواست را (شامل هدر `Authorization` اصلی) به بک‌اند ارسال می‌کند. از آنجا که برنامه Spring نیز یک سرور منبع است، دوباره توکن را اعتبارسنجی می‌کند، اما APIM قبلاً اعتبار آن را تضمین کرده است. (برای توسعه، می‌توانید به بررسی APIM تکیه کنید و در صورت تمایل بررسی‌های اضافی در برنامه را غیرفعال کنید، اما حفظ هر دو امن‌تر است.)

## تنظیمات نمونه

| تنظیم            | مقدار نمونه                                                        | نکات                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **صادرکننده**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | آدرس URL برنامه کانتینری شما (آدرس پایه)        |
| **نقطه پایانی توکن** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | نقطه پایان پیش‌فرض توکن Spring ([مدل پیکربندی :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **نقطه پایانی JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | نقطه پایان مجموعه JWK پیش‌فرض ([مدل پیکربندی :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **پیکربندی OpenID**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | سند کشف OIDC (خودکار تولید شده)    |
| **مخاطب APIM**  | `mcp-client`                                                         | شناسه مشتری OAuth یا نام منبع API       |
| **سیاست APIM**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` از این آدرس استفاده می‌کند ([مرجع سیاست Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## مشکلات رایج

- **HTTPS/TLS:** دروازه APIM نیاز دارد که نقطه پایانی OpenID/JWKS باید HTTPS با گواهی معتبر باشد. به طور پیش‌فرض، Azure Container Apps یک گواهی TLS قابل اعتماد برای دامنه مدیریت شده Azure ارائه می‌کند ([نام‌های دامنه سفارشی و گواهی‌های مدیریت شده رایگان در Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). اگر از دامنه سفارشی استفاده می‌کنید، حتماً گواهی را متصل کنید (می‌توانید از ویژگی گواهی مدیریت شده رایگان Azure استفاده کنید) ([نام‌های دامنه سفارشی و گواهی‌های مدیریت شده رایگان در Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). اگر APIM نمی‌تواند به گواهی نقطه پایانی اعتماد کند، `<validate-jwt>` نمی‌تواند فراداده‌ها را دریافت کند.

- **دسترسی به نقطه پایانی:** مطمئن شوید نقاط پایانی برنامه Spring از APIM در دسترس باشند. استفاده از `--ingress external` (یا فعال‌سازی ورودی در پرتال) ساده‌ترین راه است. اگر محیط داخلی یا متصل به vNet انتخاب کردید، APIM (که به طور پیش‌فرض عمومی است) ممکن است بدون قرارگیری در همان VNet به آن دسترسی نداشته باشد. در یک محیط آزمایشی، ورودی عمومی را ترجیح دهید تا APIM بتواند آدرس‌های `.well-known` و `/jwks` را بخواند.

- **فعال بودن کشف OpenID:** به طور پیش‌فرض، Spring Authorization Server **نقطه `/.well-known/openid-configuration` را نمایش نمی‌دهد** مگر اینکه OIDC فعال شده باشد. مطمئن شوید `.oidc(Customizer.withDefaults())` را در پیکربندی امنیتی خود وارد کنید (مطابق بالا) تا نقطه پیکربندی ارائه‌دهنده فعال شود ([مدل پیکربندی :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). در غیر این صورت، فراخوانی `<openid-config>` در APIM منجر به ۴۰۴ خواهد شد.

- **ادعای مخاطب (Audience)‌:** رفتار پیش‌فرض Spring تنظیم ادعای `aud` بر روی شناسه کلاینت است. اگر بررسی `<audience>` در APIM رد شود، ممکن است نیاز باشد توکن را سفارشی کنید (همانطور که بالا نشان داده شد) یا سیاست APIM را تنظیم کنید. مطمئن شوید مخاطب در JWT شما با مقداری که در `<audience>` پیکربندی شده است مطابقت دارد.

- **تجزیه فراداده JSON:** فراداده پیکربندی OpenID باید معتبر باشد. پیکربندی پیش‌فرض Spring یک سند متادیتای استاندارد OIDC صادر می‌کند. اطمینان حاصل کنید که شامل `issuer` و `jwks_uri` درست است. اگر Spring را پشت پراکسی یا مسیر مبتنی بر مسیر میزبانی می‌کنید، URLهای در این فراداده را دوباره بررسی کنید. APIM این مقادیر را همانطور که هستند استفاده می‌کند.

- **ترتیب سیاست:** در سیاست APIM، `<validate-jwt>` را **قبل از** هر مسیریابی به بک‌اند قرار دهید. در غیر این صورت، ممکن است تماس‌ها بدون توکن معتبر به برنامه دست یابند. همچنین اطمینان حاصل کنید که `<validate-jwt>` دقیقاً زیر `<inbound>` قرار گیرد (نه درون شرط دیگری) تا APIM آن را اعمال کند.

با دنبال کردن مراحل بالا، می‌توانید سرور Spring AI MCP خود را در Azure Container Apps اجرا کنید و Azure API Management را برای اعتبارسنجی JWTهای OAuth2 ورودی با سیاستی حداقلی پیکربندی نمائید. نکات کلیدی: نقاط پایانی احراز هویت Spring را به صورت عمومی با TLS در معرض قرار دهید، کشف OIDC را فعال کنید، و `validate-jwt` در APIM را به آدرس پیکربندی OpenID اشاره دهید (تا JWKS را به صورت خودکار دریافت کند). این پیکربندی برای محیط توسعه/تست مناسب است؛ برای تولید، مدیریت صحیح اسرار، زمان عمر توکن‌ها و چرخش کلیدها در JWKS را مدنظر قرار دهید.


**مراجع:** برای نقاط انتهایی پیش‌فرض به مستندات Spring Authorization Server مراجعه کنید ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) و پیکربندی OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); برای مثال‌های `validate-jwt` به مستندات Microsoft APIM مراجعه کنید ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); و برای استقرار و گواهینامه‌ها به مستندات Azure Container Apps مراجعه نمایید ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->