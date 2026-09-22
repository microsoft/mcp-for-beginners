# نشر تطبيق Spring AI MCP على Azure Container Apps

> [!WARNING]
> يجمع هذا الخادم الموحد للمصادقة / الموارد لأغراض التعلم والاختبار والتطوير. ينبغي على أنظمة الإنتاج استخدام مزود هوية مخصص،
> ومفاتيح توقيع دائمة، وبيانات اعتماد مخزنة في مخزن أسرار مدارة.




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

هذا ينشئ تطبيق حاوية متاح للعامة مع تمكين HTTPS (تقوم Azure بإصدار شهادة TLS مجانية لنطاق `*.azurecontainerapps.io` الافتراضي ([أسماء النطاقات المخصصة والشهادات المدارة المجانية في Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). تتضمن نتيجة الأمر اسم المجال الكامل للتطبيق (مثلاً `my-mcp-app.eastus.azurecontainerapps.io`)، والذي يصبح قاعدة **عنوان الناشر**. تأكد من تمكين دخول HTTP (كما في الأعلى) حتى يمكن لـ APIM الوصول إلى التطبيق. في بيئة اختبار / تطوير، استخدم الخيار `--ingress external` (أو اربط نطاقًا مخصصًا مع TLS بحسب [وثائق Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([أسماء النطاقات المخصصة والشهادات المدارة المجانية في Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). قم بتخزين أي خصائص حساسة (مثل أسرار عملاء OAuth) في أسرار تطبيقات الحاوية أو Azure Key Vault، وقم بربطها مع الحاوية كمتغيرات بيئة.

## تكوين خادم التفويض Spring Authorization Server

في كود تطبيق Spring Boot الخاص بك، أدرج مكتبات بدء تشغيل خادم التفويض وخادم الموارد. قم بتكوين `RegisteredClient` (لمنح `client_credentials` في بيئة التطوير/الاختبار) ومصدر مفتاح JWT. على سبيل المثال، في `application.properties` قد تحدد:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

فعّل خادم التفويض وخادم الموارد بتعريف سلسلة مرشحات الأمان. على سبيل المثال:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // تمكين نقاط نهاية خادم التفويض
            .apply(authzServer.and())
            // تمكين خادم الموارد (التحقق من JWT على الطلبات الواردة)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // تعطيل CSRF (خادم MCP ليس قائمًا على المتصفح)
            .csrf(csrf -> csrf.disable())
            // السماح بـ CORS لأدوات عرض العميل
            .cors(withDefaults());
        return http.build();
    }

    // تعريف عميل في الذاكرة (RegisteredClient) ومصدر JWK:
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
        // إنشاء مفتاح RSA (للتطوير/الاختبار، إنشاء جديد عند بدء التشغيل)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

ستعرض هذه الإعدادات نقاط نهاية OAuth2 الافتراضية: `/oauth2/token` لرموز التوكن و `/oauth2/jwks` لمجموعة مفاتيح JSON Web Key Set. (افتراضيًا، يقوم Spring `AuthorizationServerSettings` بربط `/oauth2/token` و `/oauth2/jwks` ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) سيصدر الخادم رموز وصول JWT موقعة بمفتاح RSA أعلاه، ويقوم بنشر مفتاحه العام على `https://<your-app>:/oauth2/jwks`.

**تمكين اكتشاف OpenID Connect:** للسماح لـ APIM باسترداد عنوان الناشر و JWKS تلقائيًا، فعّل نقطة تكوين مزود OIDC بإضافة `.oidc(Customizer.withDefaults())` في إعدادات الأمان الخاصة بك ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). على سبيل المثال:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– يُمكّن /.well-known/openid-configuration
```

هذا يعرض `/.well-known/openid-configuration`، والتي يمكن لـ APIM استخدامها لاستخلاص البيانات الوصفية. وأخيرًا، قد ترغب في تخصيص مطالبة الجمهور JWT **audience** بحيث يجتاز تحقق `<audiences>` الخاص بـ APIM. على سبيل المثال، أضف مخصص رمز:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // تعيين جمهور مخصص (مثل معرف العميل أو معرف واجهة برمجة التطبيقات)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

هذا يضمن أن الرموز تحمل `"aud": ["mcp-client"]`، مما يتطابق مع معرف العميل أو النطاق المتوقع من APIM.

## عرض نقاط نهاية التوكن و JWKS

بعد النشر، سيكون **عنوان الناشر** الخاص بتطبيقك `https://<app-fqdn>`، مثلًا `https://my-mcp-app.eastus.azurecontainerapps.io`. ونقاط النهاية الخاصة بـ OAuth2 هي:

- **نقطة نهاية التوكن:** `https://<app-fqdn>/oauth2/token` – يستخرج العملاء الرموز هنا (تدفق client_credentials).
- **نقطة نهاية JWKS:** `https://<app-fqdn>/oauth2/jwks` – يعيد مجموعة مفاتيح JWK (يستخدمها APIM للحصول على مفاتيح التوقيع).
- **تكوين OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON لاكتشاف OIDC (يحتوي على `issuer`, `token_endpoint`, `jwks_uri`، إلخ).

ستوجه APIM إلى **عنوان تكوين OpenID**، الذي يعثر من خلاله على `jwks_uri`. على سبيل المثال، إذا كان اسم المجال الكامل لتطبيق الحاوية هو `my-mcp-app.eastus.azurecontainerapps.io`، فيجب أن يستخدم `<openid-config url="...">` في APIM العنوان `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (افتراضيًا، سيعيّن Spring الـ `issuer` في تلك البيانات الوصفية إلى نفس عنوان القاعدة ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## تكوين Azure API Management (`validate-jwt`)

في Azure APIM، أضف سياسة وصول وارد تستخدم سياسة `<validate-jwt>` للتحقق من JWTs الواردة مقابل خادم التفويض Spring Authorization Server الخاص بك. من أجل إعداد بسيط، يمكنك استخدام عنوان بيانات التعريف لاكتشاف OpenID Connect. مقطع سياسة نموذجي:

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

تخبر هذه السياسة APIM بجلب تكوين OpenID من خادم تفويض Spring، واسترداد JWKS، والتحقق من أن كل رمز موقع بواسطة مفتاح موثوق وله الجمهور الصحيح. (إذا تجاهلت `<issuers>`، سيستخدم APIM مطالبة `issuer` من البيانات الوصفية تلقائيًا.) يجب أن يتطابق `<audience>` مع معرف العميل أو معرف مورد API في التوكن (في المثال أعلاه، قمنا بضبطه على `"mcp-client"`). هذا يتماشى مع توثيق Microsoft لاستخدام `validate-jwt` مع `<openid-config>` ([مرجع سياسة إدارة API لـ Azure - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

بعد التحقق، يقوم APIM بتمرير الطلب (بما في ذلك رأس `Authorization` الأصلي) إلى الخادم الخلفي. بما أن تطبيق Spring هو أيضًا خادم موارد، فسيعيد التحقق من التوكن، لكن APIM قد أكد بالفعل صلاحيتها. (للتطوير، يمكنك الاعتماد على تحقق APIM وتعطيل التحقق الإضافي في التطبيق إذا رغبت، لكن من الأكثر أمانًا الاحتفاظ بكليهما.)

## إعدادات نموذجية

| الإعداد               | قيمة نموذجية                                                      | ملاحظات                                   |
|--------------------|------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                | عنوان URL الخاص بتطبيق الحاوية (قاعدة URI)    |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | نقطة نهاية توكن Spring الافتراضية ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | نقطة نهاية مجموعة مفاتيح JWK الافتراضية ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | وثيقة اكتشاف OIDC (تُولد تلقائيًا)              |
| **APIM audience**  | `mcp-client`                                                     | معرف عميل OAuth أو اسم مورد API              |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | يستخدم `<validate-jwt>` هذا العنوان ([مرجع سياسة إدارة API لـ Azure - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## الأخطاء الشائعة

- **HTTPS/TLS:** يتطلب بوابة APIM أن تكون نقطة نهاية OpenID/JWKS عبر HTTPS مع شهادة صالحة. افتراضيًا، توفر Azure Container Apps شهادة TLS موثوقة للنطاق المدار من Azure ([أسماء النطاقات المخصصة والشهادات المدارة المجانية في Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). إذا استخدمت نطاقًا مخصصًا، تأكد من ربط شهادة (يمكنك استخدام ميزة الشهادات المدارة المجانية في Azure) ([أسماء النطاقات المخصصة والشهادات المدارة المجانية في Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). إذا لم يتمكن APIM من الوثوق بشهادة نقطة النهاية، سيفشل `<validate-jwt>` في جلب البيانات الوصفية.

- **وصول نقطة النهاية:** تأكد من إمكانية وصول نقاط نهاية تطبيق Spring من APIM. استخدام `--ingress external` (أو تمكين الدخول في البوابة) هو الأبسط. إذا اخترت بيئة داخلية أو مرتبطة بشبكة افتراضية، قد لا يتمكن APIM (التي تكون عامة افتراضيًا) من الوصول إليها إلا إذا وُضعت في نفس الشبكة الافتراضية. في بيئة اختبار، يفضل الدخول العام حتى يتمكن APIM من استدعاء عناوين `.well-known` و `/jwks`.

- **تمكين اكتشاف OpenID:** افتراضيًا، لا يعرض خادم التفويض Spring Authorization Server **`/.well-known/openid-configuration`** إلا إذا تم تمكين OpenID Connect. تأكد من تضمين `.oidc(Customizer.withDefaults())` في تكوين الأمان الخاص بك (انظر أعلاه) لتفعيل نقطة تكوين المزود ([نموذج التكوين :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). وإلا فإن استدعاء `<openid-config>` الخاص بـ APIM سيرجع 404.

- **مطالبة الجمهور:** السلوك الافتراضي لـ Spring هو تعيين مطالبة `aud` إلى معرف العميل. إذا فشل تحقق APIM `<audience>`, قد تحتاج إلى تخصيص الرمز (كما هو موضح أعلاه) أو ضبط سياسة APIM. تأكد من تطابق الجمهور في JWT مع ما تهيئه في `<audience>`.

- **تحليل بيانات JSON الوصفية:** يجب أن يكون JSON لتكوين OpenID صالحًا. كافتراضي، يصدر تكوين Spring وثيقة بيانات وصفية OIDC قياسية. تحقق من أنها تحتوي على `issuer` و `jwks_uri` الصحيحة. إذا كنت تستضيف Spring خلف وكيل أو مسار محدد، تحقق من صحة العناوين في هذه البيانات الوصفية. سيستخدم APIM هذه القيم كما هي.

- **ترتيب السياسات:** في سياسة APIM، ضع `<validate-jwt>` **قبل** أي توجيه إلى الخادم الخلفي. وإلا، قد تصل المكالمات إلى تطبيقك بدون رمز صالح. تأكد أيضًا من أن `<validate-jwt>` يظهر مباشرة تحت `<inbound>` (ليس داخل شرط آخر) بحيث يطبق APIM السياسة.

باتباع الخطوات أعلاه، يمكنك تشغيل خادم Spring AI MCP في Azure Container Apps وجعل Azure API Management يتحقق من JWTs الخاصة بـ OAuth2 الواردة بسياسة بسيطة. النقاط الأساسية هي: عرض نقاط نهاية Spring Auth علنًا مع TLS، تفعيل اكتشاف OIDC، وتوجيه `validate-jwt` في APIM إلى عنوان تكوين OpenID (حتى يتمكن من جلب JWKS تلقائيًا). هذا الإعداد مناسب لبيئة تطوير / اختبار؛ للإنتاج، فكر في إدارة الأسرار بشكل مناسب، وأوقات صلاحية الرموز، وتدوير المفاتيح في JWKS حسب الحاجة.


**المراجع:** راجع مستندات Spring Authorization Server للنقاط النهائية الافتراضية ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) وتكوين OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); راجع مستندات Microsoft APIM لأمثلة `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ومستندات Azure Container Apps للنشر والشهادات ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->