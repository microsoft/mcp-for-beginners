# פריסת אפליקציית Spring AI MCP ל-Azure Container Apps

> [!WARNING]
> שרת הרשאה/משאבים משולב זה מיועד ללמידה ולשימוש בפיתוח/בדיקות.
> מערכות ייצור אמורות להשתמש בספק זהות ייעודי,
> במפתחות חתימה מתמשכים ובאישורים המאוחסנים בחנות סודות מנוהלת.

 ([אבטחת שרתי Spring AI MCP עם OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *איור: שרת Spring AI MCP מאובטח עם Spring Authorization Server. השרת מנפיק אסימוני גישה ללקוחות ומאמת אותם בבקשות נכנסות (מקור: בלוג Spring) ([אבטחת שרתי Spring AI MCP עם OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* לפריסת שרת Spring MCP, בנו אותו כמיכל והשתמשו ב-Azure Container Apps עם כניסה חיצונית. לדוגמה, באמצעות Azure CLI ניתן להריץ:

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

זה יוצר Container App נגיש לציבור עם HTTPS מופעל (Azure מנפיק תעודת TLS חינמית לדומיין ברירת המחדל `*.azurecontainerapps.io` ([שמות דומיין מותאמים ותעודות מנוהלות חינמיות ב-Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). פלט הפקודה כולל את ה-FQDN של האפליקציה (למשל `my-mcp-app.eastus.azurecontainerapps.io`), שמשמש כתשתית **כתובת המנפיק**. ודאו שהכניסה דרך HTTP מופעלת (כמו למעלה) כדי ש-APIM יוכל להגיע לאפליקציה. בסביבת פיתוח/בדיקה השתמשו באפשרות `--ingress external` (או הקשר דומיין מותאם עם TLS לפי [מסמכי מיקרוסופט](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([שמות דומיין מותאמים ותעודות מנוהלות חינמיות ב-Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). אחסנו כל מאפיין רגיש (כמו סודות לקוח OAuth) בסודות Container Apps או ב-Azure Key Vault, ומיפו אותם למיכל כמשתני סביבה. 

## הגדרת Spring Authorization Server

בקוד אפליקציית Spring Boot שלכם, כללו את מתחילי Spring Authorization Server ו-Resource Server. הגדירו `RegisteredClient` (למענק `client_credentials` בפיתוח/בדיקה) ומקור מפתחות JWT. לדוגמה, ב-`application.properties` תוכלו להגדיר:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

אפשרו את Authorization Server ו-Resource Server על ידי הגדרת שרשרת מסנני אבטחה. לדוגמה:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // הפעל את נקודות הקצה של שרת האישור
            .apply(authzServer.and())
            // הפעל את שרת המשאבים (אמת JWT על בקשות נכנסות)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // השבת CSRF (שרת MCP אינו מבוסס דפדפן)
            .csrf(csrf -> csrf.disable())
            // אפשר CORS לכלי הדגמת לקוח
            .cors(withDefaults());
        return http.build();
    }

    // הגדר לקוח בזיכרון (RegisteredClient) ומקור JWK:
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
        // צור מפתח RSA (לפיתוח/בדיקה, צור מחדש בעת ההפעלה)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

הגדרה זו תחשוף את נקודות הקצה OAuth2 ברירת המחדל: `/oauth2/token` לאסימונים ו-`/oauth2/jwks` למערך מפתחות JSON Web Key Set. (ברירת המחדל, Spring’s `AuthorizationServerSettings` ממפה את `/oauth2/token` ואת `/oauth2/jwks` ([דגם ההגדרות :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) השרת ינפיק אסימוני גישה JWT חתומים במפתח RSA שלמעלה, ויפרסם את המפתח הציבורי ב-`https://<your-app>:/oauth2/jwks`. 

**אפשרו גילוי OpenID Connect:** כדי ש-APIM יוכל למשוך אוטומטית את מנפיק ה-JWKS, אפשרו את נקודת קונפיגורציית ספק OIDC על ידי הוספת `.oidc(Customizer.withDefaults())` בהגדרות האבטחה שלכם ([דגם ההגדרות :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). לדוגמה:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– מאפשר /.well-known/openid-configuration
```

זה חושף את `/.well-known/openid-configuration`, שאותו APIM יכול להשתמש עבור המטא-דטה. לבסוף, ייתכן שתרצו להתאים אישית את טענת **audience** של ה-JWT כדי שמבחן `<audiences>` של APIM יעבור. לדוגמה, הוסיפו customizer לאסימון:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // הגדר קהל מותאם אישית (למשל מזהה לקוח או מזהה API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

זה מבטיח שהאסימונים יכילו `"aud": ["mcp-client"]`, התואם ל-ID של הלקוח או טווח הצפוי על ידי APIM. 

## חשיפת נקודות הקצה Token ו-JWKS

לאחר הפריסה, **כתובת המנפיק** של האפליקציה שלכם תהיה `https://<app-fqdn>`, למשל `https://my-mcp-app.eastus.azurecontainerapps.io`. נקודות הקצה OAuth2 הן:

- **נקודת קצה Token:** `https://<app-fqdn>/oauth2/token` – כאן הלקוחות מקבלים אסימונים (זרימת client_credentials).
- **נקודת קצה JWKS:** `https://<app-fqdn>/oauth2/jwks` – מחזיר את מערך מפתחות JWK (ש-APIM משתמש כדי לקבל מפתחות חתימה).
- **קונפיגורציית OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – גילוי OIDC JSON (מכיל `issuer`, `token_endpoint`, `jwks_uri` וכו').  

APIM יכוון אל **כתובת הקונפיגורציה של OpenID**, שממנה יגלה את `jwks_uri`. לדוגמה, אם FQDN של Container App הוא `my-mcp-app.eastus.azurecontainerapps.io`, אז `<openid-config url="...">` של APIM צריך להשתמש ב-`https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (ברירת המחדל, Spring קובע את `issuer` במטא-דטה לכתובת הבסיסית הזו ([דגם ההגדרות :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## הגדרת Azure API Management (`validate-jwt`)

ב-Azure APIM, הוסיפו מדיניות נכנסת שמשתמשת ב-`<validate-jwt>` כדי לבדוק JWTs נכנסים מול Spring Authorization Server שלכם. להגדרה פשוטה, ניתן להשתמש בכתובת המטא-דטה של OpenID Connect. דוגמת מדיניות:

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

מדיניות זו מורה ל-APIM למשוך את קונפיגורציית OpenID מ-Spring Auth Server, להוריד את JWKS שלו ולוודא שכל אסימון חתום במפתח מהימן ויש לו את הקהל הנכון. (אם לא תוסיפו `<issuers>`, APIM ישתמש ב-`issuer` מהמטא-דטה אוטומטית.) `<audience>` צריך להתאים ל-ID של הלקוח שלכם או למזהה משאב ה-API באסימון (בדוגמה שלמעלה, הגדרנו אותו ל-`"mcp-client"`). זה תואם את תיעוד Microsoft לשימוש ב-`validate-jwt` עם `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

לאחר האימות, APIM י.forward את הבקשה (כולל הכותרת המקורית `Authorization`) ל-backend. מאחר שהאפליקציית Spring היא גם שרת משאבים, היא תואמת מחדש את האסימון, אבל APIM כבר הבטיחה את תקפותו. (למטרות פיתוח, אתם יכולים להסתמך על בדיקת APIM ולכבות בדיקות נוספות באפליקציה אם תרצו, אבל זה בטוח יותר לשמור על שניהם.)

## הגדרות לדוגמה

| הגדרה            | ערך לדוגמה                                                        | הערות                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **מנפיק**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | כתובת ה-URL של Container App שלכם (כתובת בסיס)        |
| **נקודת קצה Token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | נקודת הקצה ברירת המחדל של אסימוני Spring ([דגם ההגדרות :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **נקודת קצה JWKS**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | נקודת קצה ברירת מחדל למערך מפתחות JWK ([דגם ההגדרות :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **קונפיגורציית OpenID**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | מסמך גילוי OIDC (נוצר אוטומטית)    |
| **קהל APIM**  | `mcp-client`                                                         | מזהה הלקוח של OAuth או שם משאב ה-API       |
| **מדיניות APIM**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` משתמש בכתובת זו ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## מכשולים נפוצים

- **HTTPS/TLS:** שער APIM דורש שנקודת הקצה OpenID/JWKS תהיה HTTPS עם תעודה תקפה. כברירת מחדל, Azure Container Apps מספקת תעודת TLS מהימנה לדומיין מנוהל של Azure ([שמות דומיין מותאמים ותעודות מנוהלות חינמיות ב-Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). אם אתם משתמשים בדומיין מותאם, ודאו שקשרתם תעודה (ניתן להשתמש בתכונת התעודה המנוהלת החינמית של Azure) ([שמות דומיין מותאמים ותעודות מנוהלות חינמיות ב-Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). אם APIM לא יוכל לסמוך על תעודת נקודת הקצה, `<validate-jwt>` יכשל בטעינת המטא-דטה.  

- **נגישות נקודות קצה:** ודאו שנקודות הקצה באפליקציית Spring נגישות מ-APIM. שימוש ב-`--ingress external` (או הפעלת כניסה בפורטל) הוא הפשוט ביותר. אם בחרתם בסביבה פנימית או מקושרת ל-vNet, APIM (ברירת מחדל ציבורי) עשוי שלא להגיע אליה אלא אם תמוקם באותו VNet. בסביבת בדיקה, העדיפו כניסה ציבורית כדי ש-APIM יכול לגשת לכתובות `.well-known` ו-`/jwks`. 

- **גילוי OpenID מופעל:** כברירת מחדל, Spring Authorization Server **לא חושף** את `/.well-known/openid-configuration` אלא אם OIDC מופעל. ודאו להכליל `.oidc(Customizer.withDefaults())` בקונפיגורציית האבטחה (ראה למעלה) כדי שנקודת קונפיגורציית הספק תהיה פעילה ([דגם ההגדרות :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). אחרת קריאת `<openid-config>` של APIM תחזיר 404.

- **טענת הקהל:** ההתנהגות ברירת המחדל של Spring היא להגדיר את טענת `aud` ל-ID של הלקוח. אם מבחן `<audience>` של APIM נכשל, ייתכן שתצטרכו להתאים אישית את האסימון (כמו שהודגם למעלה) או לכוונן את מדיניות APIM. ודאו שהקהל ב-JWT שלכם תואם למה שהגדרתם ב-`<audience>`. 

- **ניתוח מטא-דטה JSON:** קובץ הקונפיגורציה OpenID JSON חייב להיות תקף. קונפיגורציית ברירת המחדל של Spring תפיק מסמך מטא-דטה OIDC תקני. וודאו שהוא מכיל את `issuer` ו-`jwks_uri` הנכונים. אם אתם מארחים את Spring מאחורי פרוקסי או מסלול מבוסס נתיב, בדקו שוב את ה-URLs במטא-דטה זו. APIM ישתמש בערכים כפי שהם. 

- **סדר המדיניות:** במדיניות APIM, הניחו את `<validate-jwt>` **לפני** כל ניתוב ל-backend. אחרת, עשויות להגיע קריאות לאפליקציה שלכם ללא אסימון תקף. ודאו גם ש-`<validate-jwt>` מופיע מיד מתחת ל-`<inbound>` (לא מקונן בתוך תנאי אחר) כך ש-APIM יחל אותו.

באמצעות ביצוע הצעדים שלמעלה, תוכלו להריץ את שרת Spring AI MCP ב-Azure Container Apps ולגרום ל-Azure API Management לאמת אסימוני JWT OAuth2 נכנסים עם מדיניות מינימלית. הנקודות המרכזיות הן: חשפו את נקודות הקצה של Spring Auth בצורה ציבורית עם TLS, אפשרו גילוי OIDC, וכווונו את `validate-jwt` של APIM אל כתובת ה-OpenID config (כדי שיוכל למשוך את ה-JWKS אוטומטית). הגדרה זו מתאימה לסביבת פיתוח/בדיקה; עבור ייצור, שקלו ניהול סודות נכון, חיי אסימון, וסיבוב מפתחות ב-JWKS כנדרש. 


**הפניות:** ראו את תיעוד Spring Authorization Server עבור נקודות קצה ברירת מחדל ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) ותצורת OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); ראו את תיעוד Microsoft APIM עבור דוגמאות `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); ואת תיעוד Azure Container Apps עבור פריסה ואישורים ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->