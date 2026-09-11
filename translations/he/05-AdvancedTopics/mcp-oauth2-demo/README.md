# הדגמת OAuth2 של MCP

> [!WARNING]
> זוהי דוגמת למידה מקומית, לא שירות הרשאות פרודקשן. הוא
> משתמש בלקוח בזיכרון ומייצר מפתח חתימה חדש בהפעלה. אין
> לפרוס אותו עם סוד לקוח משותף, ברירת מחדל או נשלט מקור.

## מבוא

OAuth2 הוא פרוטוקול התקן התעשייתי להרשאה, המאפשר גישה מאובטחת למשאבים מבלי לשתף אישורים. במימושים של MCP (פרוטוקול הקשר מודל), OAuth2 מספק דרך איתנה לאמת ולהעניק הרשאות ללקוחות (כגון סוכני AI) לגשת לשרת MCP וכלים שלהם.

שיעור זה מדגים כיצד ליישם אימות OAuth2 עבור שרתי MCP באמצעות Spring Boot, תבנית נפוצה לפריסות ארגוניות וייצור.

## יעדי למידה

בסוף שיעור זה תוכל:
- להבין כיצד OAuth2 משתלב עם שרתי MCP
- ליישם שרת הרשאות בספרינג להנפקת טוקנים
- להגן על נקודות קצה של MCP עם אימות מבוסס JWT
- להגדיר זרימת אישורי לקוח לתקשורת בין מכונות

## דרישות מוקדמות

- הבנה בסיסית של Java ו-Spring Boot
- היכרות עם מושגי MCP מתוך מודולים קודמים
- Maven או Gradle מותקן

---

## סקירת הפרויקט

פרויקט זה הוא **יישום מינימלי של Spring Boot** הפועל כ:

* **שרת הרשאות בספרינג** (מנפיק טוקני גישה JWT דרך `client_credentials`), ו-
* **שרת משאבים** (המגן על נקודת הקצה הפרטית שלו `/hello`).

הוא משקף את ההגדרה המוצגת ב-[פוסט הבלוג של ספרינג (2 אפריל 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## התחלה מהירה (מקומית)

```bash
# השתמש בערך מקומי ייחודי ושמור אותו מחוץ להיסטוריית השלו אם אפשרי.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# השג אסימון
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# קרא לנקודת הקצה המוגנת
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## בדיקת קונפיגורציית OAuth2

ניתן לבדוק את קונפיגורציית האבטחה של OAuth2 באמצעות השלבים הבאים:

### 1. אמת שהשרת רץ ומאובטח

```bash
# זה אמור להחזיר 401 לא מאושר, כדי לאשר ש-OAuth2 פעיל כאבטחה
curl -v http://localhost:8081/
```

### 2. קבל טוקן גישה באמצעות אישורי לקוח

```bash
# קבל וחלץ את תגובת הטוקן המלאה
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# או לחלץ רק את הטוקן (דורש jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

ב-PowerShell, הגדר את הסוד המקומי לפני הרצת Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. גש לנקודת הקצה המוגנת באמצעות הטוקן

```bash
# משתמשים באסימון השמור
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# או ישירות עם הערך של האסימון
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

תגובה מוצלחת עם "Hello from MCP OAuth2 Demo!" מאשרת שקונפיגורציית OAuth2 פועלת כהלכה.

---

## בניית מכולה

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## אבטחה בפרודקשן

לפריסה בפרודקשן, השתמש בספק זהות ייעודי במקום
בשרת הרשאות הדמה בתהליך זה. אחסן את האישורים במחסן
סודי מנוהל, סובב אותם, השתמש במפתחות חתימה מתמשכים, הגבל תחומי גישה, ו
הגדר מפיק מפורש. לעולם אל תכניס סוד לקוח בקוד המקור, בתמונות מכולה,
במניפסטי פריסה, או ביציאות פקודה.

עבור Azure Container Apps, אחסן את הערך כסוד Container Apps מגובה ב-
Key Vault ככל האפשר, ואז חשוף רק הפניה סודית באמצעות
משתנה הסביבה `OAUTH_CLIENT_SECRET`.

---

## פרוס ל-**Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

שם ה-FQDN לכניסה הופך ל-**המפיק** שלך (`https://<fqdn>`).  
Azure מספקת תעודת TLS מאובטחת אוטומטית ל-`*.azurecontainerapps.io`.

---

## התחבר ל-**Azure API Management**

הוסף מדיניות נכנסת זו ל-API שלך:

```xml
<inbound>
  <validate-jwt header-name="Authorization">
    <openid-config url="https://<fqdn>/.well-known/openid-configuration"/>
    <audiences>
      <audience>mcp-client</audience>
    </audiences>
  </validate-jwt>
  <base/>
</inbound>
```

APIM יקבל את ה-JWKS ויאמת כל בקשה.

---

## מה הלאה

- [5.4 הקשר שורש](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->