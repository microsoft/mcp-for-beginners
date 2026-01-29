# הדגמת MCP OAuth2

הפרויקט הזה הוא **יישום מינימלי ב-Spring Boot** שמשמש גם כ:

* **שרת הרשאות Spring** (המנפיק אסימוני גישה JWT דרך זרימת `client_credentials`), וגם  
* **שרת משאבים** (המגן על נקודת הקצה שלו `/hello`).

הוא משקף את ההגדרות המוצגות ב-[פוסט הבלוג של Spring (2 באפריל 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## התחלה מהירה (מקומית)

```bash
# build & run
./mvnw spring-boot:run

# obtain a token
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# call the protected endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## בדיקת תצורת OAuth2

ניתן לבדוק את תצורת האבטחה של OAuth2 באמצעות השלבים הבאים:

### 1. ודא שהשרת פועל ומאובטח

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. קבל אסימון גישה באמצעות אישורי לקוח

```bash
# Get and extract the full token response
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Or to extract just the token (requires jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

הערה: כותרת ה-Basic Authentication (`bWNwLWNsaWVudDpzZWNyZXQ=`) היא קידוד Base64 של `mcp-client:secret`.

### 3. גש לנקודת הקצה המוגנת באמצעות האסימון

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

תגובה מוצלחת עם "Hello from MCP OAuth2 Demo!" מאשרת שהתצורה של OAuth2 פועלת כראוי.

---

## בניית מכולה

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## פריסה ל-**Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

שם המארח המלא (FQDN) של ה-ingress יהפוך ל-**issuer** שלך (`https://<fqdn>`).  
Azure מספקת תעודת TLS מהימנה אוטומטית עבור `*.azurecontainerapps.io`.

---

## חיבור ל-**Azure API Management**

הוסף מדיניות inbound זו ל-API שלך:

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

APIM ימשוך את ה-JWKS ויוודא כל בקשה.

---

## מה הלאה

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.