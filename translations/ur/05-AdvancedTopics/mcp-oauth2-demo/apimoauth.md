# Spring AI MCP ایپ کو Azure Container Apps پر تعینات کرنا

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *تصویر: Spring AI MCP سرور کو Spring Authorization Server کے ذریعے محفوظ کیا گیا ہے۔ سرور کلائنٹس کو ایکسیس ٹوکن جاری کرتا ہے اور آنے والی درخواستوں پر ان کی تصدیق کرتا ہے (ماخذ: Spring بلاگ) ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Spring MCP سرور کو تعینات کرنے کے لیے، اسے کنٹینر کے طور پر بنائیں اور Azure Container Apps کے ساتھ external ingress استعمال کریں۔ مثال کے طور پر، Azure CLI کے ذریعے آپ یہ کمانڈ چلا سکتے ہیں:

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

یہ ایک عوامی طور پر قابل رسائی Container App بناتا ہے جس میں HTTPS فعال ہوتا ہے (Azure ڈیفالٹ `*.azurecontainerapps.io` ڈومین کے لیے مفت TLS سرٹیفکیٹ جاری کرتا ہے ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). کمانڈ کے نتیجے میں ایپ کا FQDN ملتا ہے (مثلاً `my-mcp-app.eastus.azurecontainerapps.io`)، جو **issuer URL** کی بنیاد بنتا ہے۔ یقینی بنائیں کہ HTTP ingress فعال ہے (جیسا کہ اوپر بتایا گیا ہے) تاکہ APIM ایپ تک پہنچ سکے۔ ٹیسٹ/ڈویلپمنٹ سیٹ اپ میں، `--ingress external` آپشن استعمال کریں (یا TLS کے ساتھ کسٹم ڈومین باندھیں جیسا کہ [Microsoft docs](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) میں بتایا گیا ہے ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)))۔ حساس پراپرٹیز (جیسے OAuth کلائنٹ سیکریٹس) کو Container Apps secrets یا Azure Key Vault میں محفوظ کریں اور انہیں کنٹینر میں environment variables کے طور پر میپ کریں۔

## Spring Authorization Server کی ترتیب

اپنی Spring Boot ایپ کے کوڈ میں Spring Authorization Server اور Resource Server starters شامل کریں۔ `RegisteredClient` کو ترتیب دیں (dev/test میں `client_credentials` گرانٹ کے لیے) اور JWT key source بنائیں۔ مثال کے طور پر، `application.properties` میں آپ یہ سیٹنگ کر سکتے ہیں:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Authorization Server اور Resource Server کو فعال کرنے کے لیے سیکیورٹی فلٹر چین ڈیفائن کریں۔ مثال کے طور پر:

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

یہ ترتیب ڈیفالٹ OAuth2 اینڈپوائنٹس کو ظاہر کرے گی: `/oauth2/token` ٹوکنز کے لیے اور `/oauth2/jwks` JSON Web Key Set کے لیے۔ (Spring کی `AuthorizationServerSettings` ڈیفالٹ میں `/oauth2/token` اور `/oauth2/jwks` کو میپ کرتی ہے ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))۔) سرور RSA کی کے ذریعے دستخط شدہ JWT ایکسیس ٹوکن جاری کرے گا، اور اپنا پبلک کی `https://<your-app>:/oauth2/jwks` پر شائع کرے گا۔

**OpenID Connect دریافت کو فعال کریں:** تاکہ APIM خود بخود issuer اور JWKS حاصل کر سکے، اپنی سیکیورٹی کنفیگریشن میں `.oidc(Customizer.withDefaults())` شامل کریں ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))۔ مثال کے طور پر:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

یہ `/.well-known/openid-configuration` کو ظاہر کرتا ہے، جسے APIM میٹا ڈیٹا کے لیے استعمال کر سکتا ہے۔ آخر میں، آپ JWT **audience** کلیم کو حسب ضرورت بنا سکتے ہیں تاکہ APIM کا `<audiences>` چیک کامیاب ہو۔ مثال کے طور پر، ایک ٹوکن کسٹمائزر شامل کریں:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

یہ یقینی بناتا ہے کہ ٹوکنز میں `"aud": ["mcp-client"]` شامل ہو، جو APIM کی توقع کردہ کلائنٹ ID یا اسکوپ سے میل کھاتا ہے۔

## ٹوکن اور JWKS اینڈپوائنٹس کو ظاہر کرنا

تعیناتی کے بعد، آپ کی ایپ کا **issuer URL** ہوگا `https://<app-fqdn>`، مثلاً `https://my-mcp-app.eastus.azurecontainerapps.io`۔ اس کے OAuth2 اینڈپوائنٹس یہ ہیں:

- **ٹوکن اینڈپوائنٹ:** `https://<app-fqdn>/oauth2/token` – کلائنٹس یہاں سے ٹوکن حاصل کرتے ہیں (client_credentials فلو)۔
- **JWKS اینڈپوائنٹ:** `https://<app-fqdn>/oauth2/jwks` – JWK سیٹ واپس کرتا ہے (APIM دستخطی کیز حاصل کرنے کے لیے استعمال کرتا ہے)۔
- **OpenID کنفیگریشن:** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC دریافت کا JSON (جس میں `issuer`, `token_endpoint`, `jwks_uri` وغیرہ شامل ہیں)۔

APIM **OpenID configuration URL** کی طرف اشارہ کرے گا، جہاں سے وہ `jwks_uri` دریافت کرتا ہے۔ مثال کے طور پر، اگر آپ کی Container App کا FQDN `my-mcp-app.eastus.azurecontainerapps.io` ہے، تو APIM کا `<openid-config url="...">` ہونا چاہیے `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`۔ (Spring ڈیفالٹ میں اس میٹا ڈیٹا میں `issuer` کو اسی بیس URL پر سیٹ کرے گا ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))۔

## Azure API Management (`validate-jwt`) کی ترتیب

Azure APIM میں، ایک inbound پالیسی شامل کریں جو `<validate-jwt>` پالیسی استعمال کرے تاکہ آنے والے JWTs کو آپ کے Spring Authorization Server کے خلاف چیک کیا جا سکے۔ سادہ سیٹ اپ کے لیے، OpenID Connect میٹا ڈیٹا URL استعمال کریں۔ مثال کے طور پر پالیسی کا ٹکڑا:

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

یہ پالیسی APIM کو ہدایت دیتی ہے کہ وہ Spring Auth Server سے OpenID کنفیگریشن حاصل کرے، اس کا JWKS لائے، اور ہر ٹوکن کی دستخط شدہ کلید کی تصدیق کرے اور درست audience چیک کرے۔ (اگر آپ `<issuers>` کو چھوڑ دیں، تو APIM خود بخود میٹا ڈیٹا سے `issuer` کلیم استعمال کرے گا۔) `<audience>` کو آپ کے کلائنٹ ID یا API resource identifier سے میل کھانا چاہیے (اوپر کی مثال میں ہم نے اسے `"mcp-client"` رکھا ہے)۔ یہ Microsoft کی دستاویزات کے مطابق ہے جو `validate-jwt` کو `<openid-config>` کے ساتھ استعمال کرنے پر روشنی ڈالتی ہے ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))۔

تصدیق کے بعد، APIM درخواست کو (اصل `Authorization` ہیڈر سمیت) بیک اینڈ کو بھیج دے گا۔ چونکہ Spring ایپ بھی resource server ہے، وہ ٹوکن کو دوبارہ چیک کرے گی، لیکن APIM پہلے ہی اس کی درستگی کو یقینی بنا چکا ہوتا ہے۔ (ڈویلپمنٹ کے لیے، آپ APIM کے چیک پر انحصار کر سکتے ہیں اور ایپ میں اضافی چیکس کو غیر فعال کر سکتے ہیں، لیکن دونوں کو فعال رکھنا زیادہ محفوظ ہے۔)

## مثال کی ترتیبات

| سیٹنگ              | مثال کی قیمت                                                        | نوٹس                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | آپ کی Container App کا URL (بنیادی URI)        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | ڈیفالٹ Spring ٹوکن اینڈپوائنٹ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | ڈیفالٹ JWK سیٹ اینڈپوائنٹ ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC دریافت دستاویز (خودکار جنریٹڈ)    |
| **APIM audience**  | `mcp-client`                                                         | OAuth کلائنٹ ID یا API resource نام       |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` اس URL کو استعمال کرتا ہے ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## عام مسائل

- **HTTPS/TLS:** APIM گیٹ وے کو ضرورت ہوتی ہے کہ OpenID/JWKS اینڈپوائنٹ HTTPS پر ہو اور اس کا سرٹیفکیٹ درست ہو۔ ڈیفالٹ میں، Azure Container Apps Azure کے زیر انتظام ڈومین کے لیے معتبر TLS سرٹیفکیٹ فراہم کرتا ہے ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))۔ اگر آپ کسٹم ڈومین استعمال کرتے ہیں، تو سرٹیفکیٹ باندھنا یقینی بنائیں (آپ Azure کا مفت managed cert فیچر استعمال کر سکتے ہیں) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))۔ اگر APIM سرٹیفکیٹ پر اعتماد نہیں کرتا، تو `<validate-jwt>` میٹا ڈیٹا حاصل کرنے میں ناکام ہو جائے گا۔

- **اینڈپوائنٹ کی رسائی:** یقینی بنائیں کہ Spring ایپ کے اینڈپوائنٹس APIM سے قابل رسائی ہوں۔ `--ingress external` استعمال کرنا (یا پورٹل میں ingress کو فعال کرنا) سب سے آسان طریقہ ہے۔ اگر آپ نے internal یا vNet-bound ماحول منتخب کیا ہے، تو APIM (جو ڈیفالٹ میں public ہے) اسے اس وقت تک نہیں پہنچ پائے گا جب تک کہ وہ اسی VNet میں نہ ہو۔ ٹیسٹ سیٹ اپ میں، عوامی ingress کو ترجیح دیں تاکہ APIM `.well-known` اور `/jwks` URLs کو کال کر سکے۔

- **OpenID دریافت فعال ہونا:** Spring Authorization Server ڈیفالٹ میں `/.well-known/openid-configuration` ظاہر نہیں کرتا جب تک کہ OIDC فعال نہ ہو۔ اپنی سیکیورٹی کنفیگریشن میں `.oidc(Customizer.withDefaults())` شامل کرنا یقینی بنائیں (اوپر دیکھیں) تاکہ provider configuration endpoint فعال ہو ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))۔ ورنہ APIM کا `<openid-config>` کال 404 دے گا۔

- **Audience کلیم:** Spring کی ڈیفالٹ پالیسی `aud` کلیم کو کلائنٹ ID پر سیٹ کرتی ہے۔ اگر APIM کا `<audience>` چیک ناکام ہو، تو آپ کو ٹوکن کو حسب ضرورت بنانا پڑ سکتا ہے (جیسا کہ اوپر دکھایا گیا ہے) یا APIM پالیسی کو ایڈجسٹ کرنا ہوگا۔ یقینی بنائیں کہ JWT میں audience وہی ہو جو آپ `<audience>` میں سیٹ کرتے ہیں۔

- **JSON میٹا ڈیٹا کی پارسنگ:** OpenID کنفیگریشن JSON درست ہونا چاہیے۔ Spring کی ڈیفالٹ کنفیگریشن ایک معیاری OIDC میٹا ڈیٹا دستاویز جاری کرے گی۔ تصدیق کریں کہ اس میں درست `issuer` اور `jwks_uri` شامل ہوں۔ اگر آپ Spring کو پراکسی یا path-based روٹنگ کے پیچھے ہوسٹ کر رہے ہیں، تو URLs کو اچھی طرح چیک کریں۔ APIM ان ویلیوز کو جیسا ہے ویسا استعمال کرے گا۔

- **پالیسی کی ترتیب:** APIM پالیسی میں `<validate-jwt>` کو بیک اینڈ کی طرف روٹنگ سے **پہلے** رکھیں۔ ورنہ کالز آپ کی ایپ تک بغیر درست ٹوکن کے پہنچ سکتی ہیں۔ اس کے علاوہ، `<validate-jwt>` کو `<inbound>` کے فوراً نیچے رکھیں (کسی اور کنڈیشن کے اندر نہیں) تاکہ APIM اسے لاگو کرے۔

مندرجہ بالا مراحل پر عمل کرتے ہوئے، آپ اپنے Spring AI MCP سرور کو Azure Container Apps میں چلا سکتے ہیں اور Azure API Management کے ذریعے آنے والے OAuth2 JWTs کی تصدیق کر سکتے ہیں۔ اہم نکات یہ ہیں: Spring Auth اینڈپوائنٹس کو TLS کے ساتھ عوامی طور پر ظاہر کریں، OIDC دریافت کو فعال کریں، اور APIM کے `validate-jwt` کو OpenID کنفیگریشن URL کی طرف اشارہ کریں تاکہ وہ JWKS خودکار طریقے سے حاصل کر سکے۔ یہ سیٹ اپ dev/test ماحول کے لیے موزوں ہے؛ پروڈکشن کے لیے مناسب سیکریٹ مینجمنٹ، ٹوکن کی مدت، اور JWKS میں کیز کی گردش پر غور کریں۔
**حوالہ جات:** Spring Authorization Server کی دستاویزات میں ڈیفالٹ اینڈ پوائنٹس دیکھیں ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) اور OIDC کنفیگریشن ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); Microsoft APIM کی دستاویزات میں `validate-jwt` کی مثالیں دیکھیں ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); اور Azure Container Apps کی دستاویزات میں تعیناتی اور سرٹیفیکیٹس کے بارے میں معلومات حاصل کریں ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔