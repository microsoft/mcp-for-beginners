# نشر تطبيق Spring AI MCP على Azure Container Apps

([تأمين خوادم Spring AI MCP باستخدام OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *الشكل: خادم Spring AI MCP مؤمن باستخدام Spring Authorization Server. يقوم الخادم بإصدار رموز وصول للعملاء والتحقق منها عند الطلبات الواردة (المصدر: مدونة Spring) ([تأمين خوادم Spring AI MCP باستخدام OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* لنشر خادم Spring MCP، قم ببنائه كحاوية واستخدم Azure Container Apps مع دخول خارجي. على سبيل المثال، باستخدام Azure CLI يمكنك تشغيل الأمر التالي:

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

هذا ينشئ تطبيق حاوية متاح للعامة مع تمكين HTTPS (تصدر Azure شهادة TLS مجانية للنطاق الافتراضي `*.azurecontainerapps.io` ([أسماء النطاقات المخصصة والشهادات المدارة المجانية في Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). يتضمن مخرجات الأمر اسم النطاق الكامل للتطبيق (مثل `my-mcp-app.eastus.azurecontainerapps.io`)، والذي يصبح قاعدة **عنوان المصدر**. تأكد من تمكين دخول HTTP (كما في الأعلى) حتى يتمكن APIM من الوصول إلى التطبيق. في بيئة اختبار/تطوير، استخدم خيار `--ingress external` (أو اربط نطاقًا مخصصًا مع TLS حسب [وثائق Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([أسماء النطاقات المخصصة والشهادات المدارة المجانية في Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). خزّن أي خصائص حساسة (مثل أسرار عملاء OAuth) في أسرار Container Apps أو Azure Key Vault، واربطها داخل الحاوية كمتغيرات بيئة.

## تكوين Spring Authorization Server

في كود تطبيق Spring Boot الخاص بك، أضف Spring Authorization Server و Resource Server starters. قم بتكوين `RegisteredClient` (لمنح `client_credentials` في بيئة التطوير/الاختبار) ومصدر مفتاح JWT. على سبيل المثال، في `application.properties` يمكنك تعيين:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

قم بتمكين Authorization Server و Resource Server عن طريق تعريف سلسلة مرشحات الأمان. على سبيل المثال:

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

سيكشف هذا الإعداد نقاط نهاية OAuth2 الافتراضية: `/oauth2/token` للحصول على الرموز و `/oauth2/jwks` لمجموعة مفاتيح JSON Web Key Set. (افتراضيًا، يقوم Spring `AuthorizationServerSettings` بتعيين `/oauth2/token` و `/oauth2/jwks` ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) سيصدر الخادم رموز وصول JWT موقعة بمفتاح RSA أعلاه، وينشر مفتاحه العام على `https://<your-app>:/oauth2/jwks`.

**تمكين اكتشاف OpenID Connect:** للسماح لـ APIM باسترداد عنوان المصدر و JWKS تلقائيًا، فعّل نقطة تكوين مزود OIDC بإضافة `.oidc(Customizer.withDefaults())` في تكوين الأمان الخاص بك ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). على سبيل المثال:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

هذا يكشف عن `/.well-known/openid-configuration`، والتي يمكن لـ APIM استخدامها للحصول على بيانات التعريف. أخيرًا، قد ترغب في تخصيص مطالبة JWT **audience** بحيث يمر فحص `<audiences>` الخاص بـ APIM. على سبيل المثال، أضف مخصص رمز:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

هذا يضمن أن الرموز تحمل `"aud": ["mcp-client"]`، متطابقة مع معرف العميل أو النطاق المتوقع من APIM.

## كشف نقاط نهاية Token و JWKS

بعد النشر، سيكون **عنوان المصدر** لتطبيقك هو `https://<app-fqdn>`، مثل `https://my-mcp-app.eastus.azurecontainerapps.io`. ونقاط نهاية OAuth2 الخاصة به هي:

- **نقطة نهاية الرمز:** `https://<app-fqdn>/oauth2/token` – يحصل العملاء على الرموز هنا (تدفق client_credentials).
- **نقطة نهاية JWKS:** `https://<app-fqdn>/oauth2/jwks` – تعيد مجموعة مفاتيح JWK (يستخدمها APIM للحصول على مفاتيح التوقيع).
- **تكوين OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON لاكتشاف OIDC (يحتوي على `issuer`، `token_endpoint`، `jwks_uri`، إلخ).

سيشير APIM إلى **عنوان تكوين OpenID**، الذي يكتشف منه `jwks_uri`. على سبيل المثال، إذا كان اسم نطاق تطبيق الحاوية الخاص بك هو `my-mcp-app.eastus.azurecontainerapps.io`، فيجب أن يستخدم `<openid-config url="...">` الخاص بـ APIM العنوان `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (افتراضيًا، سيحدد Spring `issuer` في تلك البيانات إلى نفس عنوان القاعدة ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## تكوين Azure API Management (`validate-jwt`)

في Azure APIM، أضف سياسة واردة تستخدم سياسة `<validate-jwt>` للتحقق من JWTs الواردة مقابل Spring Authorization Server الخاص بك. لإعداد بسيط، يمكنك استخدام عنوان بيانات تعريف OpenID Connect. مثال على مقتطف سياسة:

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

تخبر هذه السياسة APIM بجلب تكوين OpenID من خادم Spring Auth، واسترداد JWKS الخاص به، والتحقق من أن كل رمز موقع بواسطة مفتاح موثوق وله الجمهور الصحيح. (إذا حذفت `<issuers>`، سيستخدم APIM مطالبة `issuer` من البيانات تلقائيًا.) يجب أن يتطابق `<audience>` مع معرف العميل أو معرف مورد API في الرمز (في المثال أعلاه، قمنا بتعيينه إلى `"mcp-client"`). هذا يتوافق مع وثائق Microsoft حول استخدام `validate-jwt` مع `<openid-config>` ([مرجع سياسة Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

بعد التحقق، يقوم APIM بتمرير الطلب (بما في ذلك رأس `Authorization` الأصلي) إلى الخلفية. بما أن تطبيق Spring هو أيضًا خادم موارد، فسيعيد التحقق من الرمز، لكن APIM قد ضمن بالفعل صحته. (للتطوير، يمكنك الاعتماد على فحص APIM وتعطيل الفحوصات الإضافية في التطبيق إذا رغبت، لكن من الأفضل الاحتفاظ بكليهما.)

## إعدادات مثال

| الإعداد             | القيمة المثال                                                        | ملاحظات                                    |
|---------------------|----------------------------------------------------------------------|--------------------------------------------|
| **المصدر**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | عنوان URL الخاص بتطبيق الحاوية (قاعدة URI) |
| **نقطة نهاية الرمز** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | نقطة نهاية الرمز الافتراضية في Spring ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **نقطة نهاية JWKS** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | نقطة نهاية مجموعة مفاتيح JWK الافتراضية ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **تكوين OpenID**    | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | مستند اكتشاف OIDC (يتم إنشاؤه تلقائيًا)    |
| **جمهور APIM**      | `mcp-client`                                                         | معرف عميل OAuth أو اسم مورد API            |
| **سياسة APIM**      | `<openid-config url="https://.../.well-known/openid-configuration" />` | يستخدم `<validate-jwt>` هذا العنوان ([مرجع سياسة Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## الأخطاء الشائعة

- **HTTPS/TLS:** يتطلب بوابة APIM أن تكون نقطة نهاية OpenID/JWKS عبر HTTPS مع شهادة صالحة. بشكل افتراضي، توفر Azure Container Apps شهادة TLS موثوقة للنطاق المدار من Azure ([أسماء النطاقات المخصصة والشهادات المدارة المجانية في Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). إذا استخدمت نطاقًا مخصصًا، تأكد من ربط شهادة (يمكنك استخدام ميزة الشهادة المدارة المجانية من Azure) ([أسماء النطاقات المخصصة والشهادات المدارة المجانية في Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). إذا لم يتمكن APIM من الوثوق بشهادة نقطة النهاية، سيفشل `<validate-jwt>` في جلب بيانات التعريف.

- **إمكانية الوصول إلى نقطة النهاية:** تأكد من أن نقاط نهاية تطبيق Spring متاحة من APIM. استخدام `--ingress external` (أو تمكين الدخول في البوابة) هو الأسهل. إذا اخترت بيئة داخلية أو مرتبطة بشبكة افتراضية، قد لا يتمكن APIM (الذي يكون عامًا افتراضيًا) من الوصول إليها إلا إذا كانت في نفس الشبكة الافتراضية. في بيئة اختبار، يفضل الدخول العام حتى يتمكن APIM من استدعاء عناوين `.well-known` و `/jwks`.

- **تمكين اكتشاف OpenID:** بشكل افتراضي، لا يكشف Spring Authorization Server عن `/.well-known/openid-configuration` إلا إذا تم تمكين OIDC. تأكد من تضمين `.oidc(Customizer.withDefaults())` في تكوين الأمان الخاص بك (انظر أعلاه) حتى تكون نقطة تكوين المزود نشطة ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). وإلا، ستعيد مكالمة `<openid-config>` الخاصة بـ APIM خطأ 404.

- **مطالبة الجمهور (Audience):** السلوك الافتراضي لـ Spring هو تعيين مطالبة `aud` إلى معرف العميل. إذا فشل فحص `<audience>` الخاص بـ APIM، قد تحتاج إلى تخصيص الرمز (كما هو موضح أعلاه) أو تعديل سياسة APIM. تأكد من أن الجمهور في JWT يطابق ما تم تكوينه في `<audience>`.

- **تحليل بيانات تعريف JSON:** يجب أن يكون JSON الخاص بتكوين OpenID صالحًا. سيصدر تكوين Spring الافتراضي مستند بيانات تعريف OIDC قياسي. تحقق من احتوائه على `issuer` و `jwks_uri` الصحيحين. إذا استضفت Spring خلف وكيل أو مسار موجه، تحقق جيدًا من عناوين URL في هذه البيانات. سيستخدم APIM هذه القيم كما هي.

- **ترتيب السياسة:** في سياسة APIM، ضع `<validate-jwt>` **قبل** أي توجيه إلى الخلفية. وإلا، قد تصل المكالمات إلى تطبيقك بدون رمز صالح. كما تأكد من ظهور `<validate-jwt>` مباشرة تحت `<inbound>` (وليس داخل شرط آخر) حتى يطبقها APIM.

باتباع الخطوات أعلاه، يمكنك تشغيل خادم Spring AI MCP الخاص بك في Azure Container Apps وجعل Azure API Management يتحقق من JWTs الواردة الخاصة بـ OAuth2 بسياسة بسيطة. النقاط الأساسية هي: كشف نقاط نهاية Spring Auth علنًا مع TLS، تمكين اكتشاف OIDC، وتوجيه `validate-jwt` في APIM إلى عنوان تكوين OpenID (حتى يتمكن من جلب JWKS تلقائيًا). هذا الإعداد مناسب لبيئة تطوير/اختبار؛ للإنتاج، فكر في إدارة الأسرار بشكل صحيح، وأوقات صلاحية الرموز، وتدوير المفاتيح في JWKS حسب الحاجة.
**المراجع:** راجع مستندات Spring Authorization Server للنقاط النهائية الافتراضية ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) وتكوين OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); اطلع على مستندات Microsoft APIM لأمثلة `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ومستندات Azure Container Apps للنشر والشهادات ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.