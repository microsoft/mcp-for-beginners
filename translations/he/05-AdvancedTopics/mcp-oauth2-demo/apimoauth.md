# פריסת אפליקציית Spring AI MCP ב-Azure Container Apps

 ([אבטחת שרתי Spring AI MCP עם OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *איור: שרת Spring AI MCP מאובטח עם Spring Authorization Server. השרת מנפיק אסימוני גישה ללקוחות ומאמת אותם בבקשות נכנסות (מקור: בלוג Spring) ([אבטחת שרתי Spring AI MCP עם OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* כדי לפרוס את שרת Spring MCP, יש לבנות אותו כמכולה ולהשתמש ב-Azure Container Apps עם כניסה חיצונית. לדוגמה, באמצעות Azure CLI ניתן להריץ:

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

פעולה זו יוצרת Container App נגיש לציבור עם HTTPS מופעל (Azure מנפיק תעודת TLS חינמית לדומיין ברירת המחדל `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). הפלט של הפקודה כולל את ה-FQDN של האפליקציה (למשל `my-mcp-app.eastus.azurecontainerapps.io`), שיהפוך לבסיס של **issuer URL**. ודא שכניסת HTTP מופעלת (כמו למעלה) כדי ש-APIM יוכל להגיע לאפליקציה. בסביבת בדיקה/פיתוח, השתמש באפשרות `--ingress external` (או קשר דומיין מותאם אישית עם TLS לפי [תיעוד מיקרוסופט](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). אחסן כל מאפיין רגיש (כמו סודות לקוח OAuth) ב-Container Apps secrets או ב-Azure Key Vault, ומפה אותם למכולה כמשתני סביבה.

## הגדרת Spring Authorization Server

בקוד של אפליקציית Spring Boot שלך, כלול את ה-starters של Spring Authorization Server ו-Resource Server. הגדר `RegisteredClient` (ל-grant מסוג `client_credentials` בסביבת פיתוח/בדיקה) ומקור מפתחות JWT. לדוגמה, ב-`application.properties` תוכל להגדיר:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

אפשר את Authorization Server ו-Resource Server על ידי הגדרת security filter chain. לדוגמה:

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

הגדרה זו תחשוף את נקודות הקצה OAuth2 ברירת המחדל: `/oauth2/token` לאסימונים ו-`/oauth2/jwks` ל-JSON Web Key Set. (ברירת המחדל, `AuthorizationServerSettings` של Spring ממפה את `/oauth2/token` ו-`/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) השרת ינפיק אסימוני גישה JWT חתומים עם מפתח RSA שהוגדר למעלה, ויפרסם את המפתח הציבורי בכתובת `https://<your-app>:/oauth2/jwks`.

**אפשר גילוי OpenID Connect:** כדי לאפשר ל-APIM לאחזר אוטומטית את ה-issuer וה-JWKS, הפעל את נקודת הקצה של הגדרת ספק OIDC על ידי הוספת `.oidc(Customizer.withDefaults())` בהגדרת האבטחה שלך ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). לדוגמה:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

זה יחשוף את `/.well-known/openid-configuration`, ש-APIM יכול להשתמש בו למטא-נתונים. לבסוף, ייתכן שתרצה להתאים את טענת ה-**audience** של ה-JWT כך שבדיקת `<audiences>` של APIM תעבור. לדוגמה, הוסף customizer לאסימון:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

זה מבטיח שהאסימונים יכילו `"aud": ["mcp-client"]`, התואם ל-client ID או לסקופ ש-APIM מצפה לו.

## חשיפת נקודות הקצה Token ו-JWKS

לאחר הפריסה, ה-**issuer URL** של האפליקציה שלך יהיה `https://<app-fqdn>`, לדוגמה `https://my-mcp-app.eastus.azurecontainerapps.io`. נקודות הקצה OAuth2 שלה הן:

- **נקודת קצה Token:** `https://<app-fqdn>/oauth2/token` – כאן הלקוחות מקבלים אסימונים (זרימת client_credentials).
- **נקודת קצה JWKS:** `https://<app-fqdn>/oauth2/jwks` – מחזירה את סט המפתחות JWK (ש-APIM משתמש בו לקבלת מפתחות חתימה).
- **קונפיגורציית OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON לגילוי OIDC (מכיל `issuer`, `token_endpoint`, `jwks_uri` וכו').

APIM יפנה ל-**כתובת קונפיגורציית OpenID**, ממנה יגלה את ה-`jwks_uri`. לדוגמה, אם ה-FQDN של Container App שלך הוא `my-mcp-app.eastus.azurecontainerapps.io`, אז `<openid-config url="...">` של APIM צריך להשתמש ב-`https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (ברירת המחדל, Spring יגדיר את ה-`issuer` במטא-נתונים לכתובת הבסיסית הזו ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## הגדרת Azure API Management (`validate-jwt`)

ב-Azure APIM, הוסף מדיניות נכנסת שמשתמשת ב-`<validate-jwt>` כדי לבדוק JWTs נכנסים מול Spring Authorization Server שלך. להגדרה פשוטה, ניתן להשתמש בכתובת המטא-נתונים של OpenID Connect. קטע מדיניות לדוגמה:

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

מדיניות זו מורה ל-APIM לאחזר את קונפיגורציית OpenID משרת האימות של Spring, לקבל את ה-JWKS שלו, ולאמת שכל אסימון חתום במפתח מהימן ויש לו את ה-audience הנכון. (אם תוותר על `<issuers>`, APIM ישתמש אוטומטית בטענת `issuer` מהמטא-נתונים.) ה-`<audience>` צריך להתאים ל-client ID או למזהה משאב ה-API שבאסימון (בדוגמה למעלה, הגדרנו אותו ל-`"mcp-client"`). זה תואם לתיעוד של מיקרוסופט לשימוש ב-`validate-jwt` עם `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

לאחר האימות, APIM ימשיך להעביר את הבקשה (כולל כותרת `Authorization` המקורית) ל-backend. מכיוון שאפליקציית Spring היא גם שרת משאבים, היא תאמת מחדש את האסימון, אך APIM כבר הבטיח את תקינותו. (לצורך פיתוח, ניתן להסתמך על בדיקת APIM ולבטל בדיקות נוספות באפליקציה אם רוצים, אך עדיף לשמור על שניהם.)

## דוגמאות הגדרות

| הגדרה             | ערך לדוגמה                                                        | הערות                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | כתובת ה-URL של Container App שלך (כתובת בסיס)        |
| **נקודת קצה Token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | נקודת הקצה של אסימון ברירת המחדל של Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **נקודת קצה JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | נקודת הקצה של סט מפתחות JWK ברירת המחדל ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **קונפיגורציית OpenID**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | מסמך גילוי OIDC (נוצר אוטומטית)    |
| **Audience ב-APIM**  | `mcp-client`                                                         | מזהה לקוח OAuth או שם משאב API       |
| **מדיניות APIM**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` משתמש בכתובת זו ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## בעיות נפוצות

- **HTTPS/TLS:** שער ה-APIM דורש שנקודת הקצה OpenID/JWKS תהיה HTTPS עם תעודה תקפה. ברירת המחדל, Azure Container Apps מספק תעודת TLS מהימנה לדומיין מנוהל על ידי Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). אם אתה משתמש בדומיין מותאם אישית, ודא שקישרת תעודה (ניתן להשתמש בתעודה מנוהלת חינמית של Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). אם APIM לא יכול לסמוך על תעודת נקודת הקצה, `<validate-jwt>` ייכשל באחזור המטא-נתונים.

- **נגישות נקודת הקצה:** ודא שנקודות הקצה של אפליקציית Spring נגישות מ-APIM. שימוש ב-`--ingress external` (או הפעלת כניסה בפורטל) הוא הפשוט ביותר. אם בחרת בסביבה פנימית או מחוברת ל-vNet, ייתכן ש-APIM (ברירת מחדל ציבורית) לא יוכל להגיע אליה אלא אם היא באותו VNet. בסביבת בדיקה, העדף כניסה ציבורית כדי ש-APIM יוכל לקרוא את כתובות ה-`.well-known` ו-`/jwks`.

- **גילוי OpenID מופעל:** ברירת המחדל, Spring Authorization Server **לא חושף** את `/.well-known/openid-configuration` אלא אם OIDC מופעל. ודא שהוספת `.oidc(Customizer.withDefaults())` בהגדרת האבטחה (כפי שמוצג למעלה) כדי להפעיל את נקודת הקצה של הגדרת הספק ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). אחרת קריאת `<openid-config>` של APIM תחזיר שגיאת 404.

- **טענת Audience:** ההתנהגות ברירת המחדל של Spring היא להגדיר את טענת `aud` ל-client ID. אם בדיקת `<audience>` של APIM נכשלת, ייתכן שתצטרך להתאים אישית את האסימון (כפי שמוצג למעלה) או לשנות את מדיניות APIM. ודא שה-audience ב-JWT תואם למה שהגדרת ב-`<audience>`.

- **ניתוח מטא-נתונים JSON:** מסמך קונפיגורציית OpenID חייב להיות תקין. ברירת המחדל של Spring תפיק מסמך מטא-נתונים סטנדרטי של OIDC. ודא שהוא מכיל את ה-`issuer` וה-`jwks_uri` הנכונים. אם אתה מארח את Spring מאחורי פרוקסי או נתיב מותאם, בדוק היטב את הכתובות במטא-נתונים. APIM ישתמש בערכים כפי שהם.

- **סדר המדיניות:** במדיניות APIM, מקם את `<validate-jwt>` **לפני** כל ניתוב ל-backend. אחרת, קריאות עלולות להגיע לאפליקציה ללא אסימון תקף. ודא ש-`<validate-jwt>` מופיע מיד תחת `<inbound>` (ולא בתוך תנאי אחר) כדי ש-APIM יפעיל אותו.

על ידי ביצוע השלבים שלמעלה, תוכל להפעיל את שרת Spring AI MCP שלך ב-Azure Container Apps ולתת ל-Azure API Management לאמת JWTs נכנסים של OAuth2 עם מדיניות מינימלית. הנקודות המרכזיות הן: לחשוף את נקודות הקצה של Spring Auth לציבור עם TLS, להפעיל גילוי OIDC, ולהפנות את `validate-jwt` של APIM לכתובת קונפיגורציית OpenID (כדי שיאחזר את ה-JWKS אוטומטית). הגדרה זו מתאימה לסביבת פיתוח/בדיקה; לפרודקשן שקול ניהול סודות נכון, זמני חיים של אסימונים, וסיבוב מפתחות ב-JWKS לפי הצורך.
**References:** ראה את תיעוד Spring Authorization Server עבור נקודות הקצה המוגדרות מראש ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ואת תצורת OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); ראה את תיעוד Microsoft APIM לדוגמאות של `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ואת תיעוד Azure Container Apps לפריסה ותעודות ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.