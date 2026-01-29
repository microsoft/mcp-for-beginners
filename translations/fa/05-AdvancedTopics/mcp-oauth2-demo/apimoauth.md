# استقرار برنامه Spring AI MCP در Azure Container Apps

 ([امن‌سازی سرورهای Spring AI MCP با OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *شکل: سرور Spring AI MCP با Spring Authorization Server ایمن شده است. سرور توکن‌های دسترسی را به کلاینت‌ها صادر می‌کند و آن‌ها را در درخواست‌های ورودی اعتبارسنجی می‌کند (منبع: بلاگ Spring) ([امن‌سازی سرورهای Spring AI MCP با OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* برای استقرار سرور Spring MCP، آن را به صورت یک کانتینر بسازید و از Azure Container Apps با ورودی خارجی استفاده کنید. به عنوان مثال، با استفاده از Azure CLI می‌توانید دستور زیر را اجرا کنید:

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

این دستور یک Container App با دسترسی عمومی و HTTPS فعال ایجاد می‌کند (Azure برای دامنه پیش‌فرض `*.azurecontainerapps.io` گواهی TLS رایگان صادر می‌کند ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). خروجی دستور شامل FQDN برنامه (مثلاً `my-mcp-app.eastus.azurecontainerapps.io`) است که به عنوان پایه **آدرس صادرکننده (issuer URL)** استفاده می‌شود. مطمئن شوید که ورودی HTTP فعال است (همانطور که بالا گفته شد) تا APIM بتواند به برنامه دسترسی داشته باشد. در محیط تست/توسعه، از گزینه `--ingress external` استفاده کنید (یا دامنه سفارشی با TLS طبق [مستندات مایکروسافت](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) متصل کنید ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). هرگونه اطلاعات حساس (مانند اسرار کلاینت OAuth) را در اسرار Container Apps یا Azure Key Vault ذخیره کرده و به صورت متغیرهای محیطی به کانتینر نگاشت کنید.

## پیکربندی Spring Authorization Server

در کد برنامه Spring Boot خود، استارترهای Spring Authorization Server و Resource Server را اضافه کنید. یک `RegisteredClient` برای grant نوع `client_credentials` در محیط توسعه/تست و یک منبع کلید JWT پیکربندی کنید. به عنوان مثال، در `application.properties` ممکن است موارد زیر را تنظیم کنید:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

با تعریف یک security filter chain، Authorization Server و Resource Server را فعال کنید. برای مثال:

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

این تنظیمات نقاط انتهایی پیش‌فرض OAuth2 را در دسترس قرار می‌دهد: `/oauth2/token` برای دریافت توکن‌ها و `/oauth2/jwks` برای JSON Web Key Set. (به طور پیش‌فرض، `AuthorizationServerSettings` در Spring مسیرهای `/oauth2/token` و `/oauth2/jwks` را نگاشت می‌کند ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) سرور توکن‌های دسترسی JWT را با کلید RSA بالا امضا می‌کند و کلید عمومی خود را در `https://<your-app>:/oauth2/jwks` منتشر می‌کند.

**فعال‌سازی کشف OpenID Connect:** برای اینکه APIM بتواند به صورت خودکار آدرس صادرکننده و JWKS را دریافت کند، نقطه پیکربندی ارائه‌دهنده OIDC را با افزودن `.oidc(Customizer.withDefaults())` در پیکربندی امنیتی خود فعال کنید ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). برای مثال:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

این مسیر `/.well-known/openid-configuration` را در دسترس قرار می‌دهد که APIM می‌تواند برای دریافت متادیتا از آن استفاده کند. در نهایت، ممکن است بخواهید ادعای **audience** در JWT را سفارشی کنید تا بررسی `<audiences>` در APIM موفق باشد. به عنوان مثال، یک توکن کاستومایزر اضافه کنید:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

این تضمین می‌کند که توکن‌ها شامل `"aud": ["mcp-client"]` باشند که با شناسه کلاینت یا scope مورد انتظار APIM مطابقت دارد.

## در دسترس قرار دادن نقاط انتهایی Token و JWKS

پس از استقرار، **آدرس صادرکننده (issuer URL)** برنامه شما به صورت `https://<app-fqdn>` خواهد بود، مثلاً `https://my-mcp-app.eastus.azurecontainerapps.io`. نقاط انتهایی OAuth2 آن عبارتند از:

- **نقطه انتهایی توکن:** `https://<app-fqdn>/oauth2/token` – کلاینت‌ها در اینجا توکن دریافت می‌کنند (جریان client_credentials).
- **نقطه انتهایی JWKS:** `https://<app-fqdn>/oauth2/jwks` – مجموعه کلیدهای JWK را برمی‌گرداند (که APIM برای دریافت کلیدهای امضا استفاده می‌کند).
- **پیکربندی OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON کشف OIDC (شامل `issuer`، `token_endpoint`، `jwks_uri` و غیره).

APIM به **آدرس پیکربندی OpenID** اشاره می‌کند و از آنجا `jwks_uri` را کشف می‌کند. برای مثال، اگر FQDN برنامه Container App شما `my-mcp-app.eastus.azurecontainerapps.io` باشد، `<openid-config url="...">` در APIM باید از `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` استفاده کند. (به طور پیش‌فرض Spring مقدار `issuer` را در این متادیتا به همان آدرس پایه تنظیم می‌کند ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## پیکربندی Azure API Management (`validate-jwt`)

در Azure APIM، یک سیاست inbound اضافه کنید که از `<validate-jwt>` برای اعتبارسنجی JWTهای ورودی در برابر Spring Authorization Server شما استفاده کند. برای یک پیکربندی ساده، می‌توانید از URL متادیتای OpenID Connect استفاده کنید. نمونه قطعه سیاست:

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

این سیاست به APIM می‌گوید که پیکربندی OpenID را از Spring Auth Server دریافت کند، JWKS آن را بازیابی کند و اعتبارسنجی کند که هر توکن با کلید مورد اعتماد امضا شده و audience صحیح دارد. (اگر `<issuers>` را حذف کنید، APIM به طور خودکار از ادعای `issuer` در متادیتا استفاده می‌کند.) مقدار `<audience>` باید با شناسه کلاینت یا شناسه منبع API در توکن مطابقت داشته باشد (در مثال بالا، مقدار `"mcp-client"` تنظیم شده است). این مطابق با مستندات مایکروسافت درباره استفاده از `validate-jwt` با `<openid-config>` است ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

پس از اعتبارسنجی، APIM درخواست را (شامل هدر اصلی `Authorization`) به بک‌اند ارسال می‌کند. از آنجا که برنامه Spring نیز یک resource server است، توکن را دوباره اعتبارسنجی می‌کند، اما APIM قبلاً اعتبار آن را تضمین کرده است. (برای توسعه، می‌توانید به اعتبارسنجی APIM اعتماد کنید و اعتبارسنجی اضافی در برنامه را غیرفعال کنید، اما نگه داشتن هر دو امن‌تر است.)

## تنظیمات نمونه

| تنظیم             | مقدار نمونه                                                        | توضیحات                                    |
|-------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | آدرس برنامه Container App شما (آدرس پایه) |
| **Token endpoint**| `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | نقطه انتهایی توکن پیش‌فرض Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | نقطه انتهایی مجموعه کلید JWK پیش‌فرض ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config** | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | سند کشف OIDC (به صورت خودکار تولید شده)    |
| **APIM audience** | `mcp-client`                                                      | شناسه کلاینت OAuth یا نام منبع API          |
| **APIM policy**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` از این URL استفاده می‌کند ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## مشکلات رایج

- **HTTPS/TLS:** درگاه APIM نیاز دارد که نقطه انتهایی OpenID/JWKS با HTTPS و گواهی معتبر در دسترس باشد. به طور پیش‌فرض، Azure Container Apps گواهی TLS معتبری برای دامنه مدیریت شده Azure ارائه می‌دهد ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). اگر از دامنه سفارشی استفاده می‌کنید، حتماً گواهی را متصل کنید (می‌توانید از قابلیت گواهی مدیریت شده رایگان Azure استفاده کنید) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). اگر APIM نتواند به گواهی نقطه انتهایی اعتماد کند، `<validate-jwt>` نمی‌تواند متادیتا را دریافت کند.

- **دسترس‌پذیری نقطه انتهایی:** اطمینان حاصل کنید که نقاط انتهایی برنامه Spring از APIM قابل دسترسی باشند. استفاده از `--ingress external` (یا فعال‌سازی ingress در پورتال) ساده‌ترین روش است. اگر محیط داخلی یا متصل به vNet انتخاب کرده‌اید، APIM (که به طور پیش‌فرض عمومی است) ممکن است نتواند به آن دسترسی داشته باشد مگر اینکه در همان vNet قرار داشته باشد. در محیط تست، بهتر است از ورودی عمومی استفاده کنید تا APIM بتواند به آدرس‌های `.well-known` و `/jwks` دسترسی داشته باشد.

- **فعال بودن کشف OpenID:** به طور پیش‌فرض، Spring Authorization Server **مسیر `/.well-known/openid-configuration` را منتشر نمی‌کند مگر اینکه OIDC فعال شده باشد.** مطمئن شوید که `.oidc(Customizer.withDefaults())` را در پیکربندی امنیتی خود اضافه کرده‌اید (مطابق بالا) تا نقطه پیکربندی ارائه‌دهنده فعال شود ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). در غیر این صورت، فراخوانی `<openid-config>` در APIM با خطای 404 مواجه خواهد شد.

- **ادعای Audience:** رفتار پیش‌فرض Spring این است که ادعای `aud` را به شناسه کلاینت تنظیم کند. اگر بررسی `<audience>` در APIM ناموفق بود، ممکن است نیاز باشد توکن را سفارشی کنید (همانطور که بالا نشان داده شد) یا سیاست APIM را تنظیم کنید. مطمئن شوید که audience در JWT با مقدار تنظیم شده در `<audience>` مطابقت دارد.

- **تحلیل متادیتای JSON:** سند پیکربندی OpenID باید معتبر باشد. پیکربندی پیش‌فرض Spring یک سند متادیتای استاندارد OIDC تولید می‌کند. بررسی کنید که شامل `issuer` و `jwks_uri` صحیح باشد. اگر Spring را پشت پراکسی یا مسیر مبتنی بر روت میزبانی می‌کنید، آدرس‌های موجود در این متادیتا را دوباره بررسی کنید. APIM این مقادیر را بدون تغییر استفاده خواهد کرد.

- **ترتیب سیاست‌ها:** در سیاست APIM، `<validate-jwt>` را **قبل از هر مسیریابی به بک‌اند قرار دهید.** در غیر این صورت، ممکن است درخواست‌ها بدون توکن معتبر به برنامه برسند. همچنین مطمئن شوید که `<validate-jwt>` مستقیماً زیر `<inbound>` قرار دارد (نه داخل شرط دیگری) تا APIM آن را اعمال کند.

با دنبال کردن مراحل بالا، می‌توانید سرور Spring AI MCP خود را در Azure Container Apps اجرا کنید و Azure API Management را برای اعتبارسنجی JWTهای OAuth2 ورودی با سیاستی حداقلی تنظیم کنید. نکات کلیدی عبارتند از: در دسترس قرار دادن نقاط انتهایی Spring Auth به صورت عمومی با TLS، فعال کردن کشف OIDC و تنظیم `validate-jwt` در APIM به آدرس پیکربندی OpenID (تا بتواند به صورت خودکار JWKS را دریافت کند). این تنظیم برای محیط توسعه/تست مناسب است؛ برای محیط تولید، مدیریت مناسب اسرار، زمان عمر توکن‌ها و چرخش کلیدها در JWKS را در نظر بگیرید.
**مراجع:** برای مشاهده نقاط انتهایی پیش‌فرض به مستندات Spring Authorization Server مراجعه کنید ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) و پیکربندی OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); برای مثال‌های `validate-jwt` به مستندات Microsoft APIM مراجعه کنید ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))؛ و برای استقرار و گواهی‌ها به مستندات Azure Container Apps مراجعه نمایید ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.