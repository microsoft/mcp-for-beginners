# MCP OAuth2 டெமோ

இந்த திட்டம் **குறைந்தபட்சமான ஸ்பிரிங் பூட் பயன்பாடு** ஆகும், இது இரண்டையும் செய்கிறது:

* **ஸ்பிரிங் ஆத்தரைசேஷன் சர்வர்** (JWT அணுகல் டோக்கன்களை `client_credentials` வழியாக வழங்குகிறது), மற்றும்  
* **ரிசோர்ஸ் சர்வர்** (தனது சொந்த `/hello` எண்ட்பாயிண்டை பாதுகாக்கிறது).

இது [ஸ்பிரிங் வலைப்பதிவு (2 ஏப்ரல் 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) இல் காட்டப்பட்ட அமைப்பை பிரதிபலிக்கிறது.

---

## விரைவான தொடக்கம் (உள்ளூர்)

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

## OAuth2 கட்டமைப்பை சோதித்தல்

OAuth2 பாதுகாப்பு அமைப்பை கீழ்க்கண்ட படிகளுடன் சோதிக்கலாம்:

### 1. சர்வர் இயங்குகிறது மற்றும் பாதுகாக்கப்பட்டுள்ளது என்பதை உறுதிப்படுத்தவும்

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. கிளையன்ட் சான்றுகள் மூலம் அணுகல் டோக்கனைப் பெறவும்

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

குறிப்பு: அடிப்படை அங்கீகார தலைப்பு (`bWNwLWNsaWVudDpzZWNyZXQ=`) என்பது `mcp-client:secret` இன் Base64 குறியாக்கமாகும்.

### 3. டோக்கனைப் பயன்படுத்தி பாதுகாக்கப்பட்ட எண்ட்பாயிண்டை அணுகவும்

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" என்ற வெற்றிகரமான பதில், OAuth2 அமைப்பு சரியாக செயல்படுகிறது என்பதை உறுதிப்படுத்துகிறது.

---

## கண்டெய்னர் கட்டமைப்பு

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** க்கு பிரசுரிக்கவும்

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

இன்கிரஸ் FQDN உங்கள் **issuer** ஆக மாறுகிறது (`https://<fqdn>`).  
Azure `*.azurecontainerapps.io` க்கு தானாகவே நம்பகமான TLS சான்றிதழை வழங்குகிறது.

---

## **Azure API Management** உடன் இணைக்கவும்

உங்கள் API இல் இந்த இன்பவுண்ட் கொள்கையைச் சேர்க்கவும்:

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

APIM JWKS ஐப் பெறும் மற்றும் ஒவ்வொரு கோரிக்கையையும் சரிபார்க்கும்.

---

## அடுத்தது என்ன

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.