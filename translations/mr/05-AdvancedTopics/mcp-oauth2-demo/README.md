# MCP OAuth2 डेमो

हा प्रकल्प एक **मिनिमल Spring Boot अॅप्लिकेशन** आहे जो दोन्ही म्हणून कार्य करतो:

* एक **Spring Authorization Server** (जो `client_credentials` फ्लो वापरून JWT ऍक्सेस टोकन्स जारी करतो), आणि  
* एक **Resource Server** (जो स्वतःच्या `/hello` एंडपॉइंटचे संरक्षण करतो).

हे [Spring ब्लॉग पोस्ट (2 एप्रिल 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) मध्ये दाखवलेल्या सेटअपचे प्रतिबिंब आहे.

---

## जलद सुरुवात (स्थानिक)

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

## OAuth2 कॉन्फिगरेशनची चाचणी

खालील टप्प्यांद्वारे तुम्ही OAuth2 सुरक्षा कॉन्फिगरेशनची चाचणी करू शकता:

### 1. सर्व्हर चालू आहे आणि सुरक्षित आहे याची खात्री करा

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. क्लायंट क्रेडेन्शियल्स वापरून ऍक्सेस टोकन मिळवा

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

टीप: Basic Authentication हेडर (`bWNwLWNsaWVudDpzZWNyZXQ=`) हा `mcp-client:secret` चा Base64 एन्कोडिंग आहे.

### 3. टोकन वापरून संरक्षित एंडपॉइंटवर प्रवेश करा

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" असा यशस्वी प्रतिसाद मिळाल्यास OAuth2 कॉन्फिगरेशन योग्यरित्या कार्यरत आहे हे पुष्टी होते.

---

## कंटेनर बिल्ड

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** मध्ये डिप्लॉय करा

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

इंग्रेस FQDN तुमचा **issuer** (`https://<fqdn>`) बनतो.  
Azure आपोआप `*.azurecontainerapps.io` साठी विश्वासार्ह TLS प्रमाणपत्र प्रदान करते.

---

## **Azure API Management** मध्ये कनेक्ट करा

तुमच्या API मध्ये हा इनबाउंड पॉलिसी जोडा:

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

APIM JWKS प्राप्त करेल आणि प्रत्येक विनंतीची पडताळणी करेल.

---

## पुढे काय

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.