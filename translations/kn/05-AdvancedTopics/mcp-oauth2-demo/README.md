<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0a7083e660ca0d85fd6a947514c61993",
  "translation_date": "2025-12-11T16:17:06+00:00",
  "source_file": "05-AdvancedTopics/mcp-oauth2-demo/README.md",
  "language_code": "kn"
}
-->
# MCP OAuth2 ಡೆಮೊ

ಈ ಪ್ರಾಜೆಕ್ಟ್ ಒಂದು **ಕನಿಷ್ಠ ಸ್ಪ್ರಿಂಗ್ ಬೂಟ್ ಅಪ್ಲಿಕೇಶನ್** ಆಗಿದ್ದು, ಎರಡೂ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ:

* **ಸ್ಪ್ರಿಂಗ್ ಪ್ರಾಧಿಕಾರ ಸರ್ವರ್** ಆಗಿ (`client_credentials` ಫ್ಲೋ ಮೂಲಕ JWT ಪ್ರವೇಶ ಟೋಕನ್‌ಗಳನ್ನು ನೀಡುತ್ತದೆ), ಮತ್ತು  
* **ಸಂಪನ್ಮೂಲ ಸರ್ವರ್** ಆಗಿ (ತನ್ನದೇ `/hello` ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ರಕ್ಷಿಸುತ್ತದೆ).

ಇದು [ಸ್ಪ್ರಿಂಗ್ ಬ್ಲಾಗ್ ಪೋಸ್ಟ್ (2 ಏಪ್ರಿಲ್ 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) ನಲ್ಲಿ ತೋರಿಸಿದ ಸೆಟಪ್ ಅನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ.

---

## ತ್ವರಿತ ಪ್ರಾರಂಭ (ಸ್ಥಳೀಯ)

```bash
# ನಿರ್ಮಿಸಿ ಮತ್ತು ಚಾಲನೆ ಮಾಡಿ
./mvnw spring-boot:run

# ಟೋಕನ್ ಪಡೆಯಿರಿ
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# ರಕ್ಷಿತ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಕರೆಮಾಡಿ
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## OAuth2 ಸಂರಚನೆಯನ್ನು ಪರೀಕ್ಷಿಸುವುದು

ನೀವು ಕೆಳಗಿನ ಹಂತಗಳ ಮೂಲಕ OAuth2 ಭದ್ರತಾ ಸಂರಚನೆಯನ್ನು ಪರೀಕ್ಷಿಸಬಹುದು:

### 1. ಸರ್ವರ್ ಚಾಲನೆಯಲ್ಲಿದೆ ಮತ್ತು ಭದ್ರವಾಗಿದೆ ಎಂದು ಪರಿಶೀಲಿಸಿ

```bash
# ಇದು 401 ಅನಧಿಕೃತ ಎಂದು ಹಿಂತಿರುಗಿಸಬೇಕು, OAuth2 ಭದ್ರತೆ ಸಕ್ರಿಯವಾಗಿದೆ ಎಂದು ದೃಢೀಕರಿಸುತ್ತದೆ
curl -v http://localhost:8081/
```

### 2. ಕ್ಲೈಂಟ್ ಕ್ರೆಡೆನ್ಷಿಯಲ್ಸ್ ಬಳಸಿ ಪ್ರವೇಶ ಟೋಕನ್ ಪಡೆಯಿರಿ

```bash
# ಸಂಪೂರ್ಣ ಟೋಕನ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯಿರಿ ಮತ್ತು ಹೊರತೆಗೆಯಿರಿ
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# ಅಥವಾ ಕೇವಲ ಟೋಕನ್ ಅನ್ನು ಹೊರತೆಗೆಯಲು (jq ಅಗತ್ಯವಿದೆ)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

ಗಮನಿಸಿ: Basic Authentication ಹೆಡರ್ (`bWNwLWNsaWVudDpzZWNyZXQ=`) `mcp-client:secret` ನ Base64 ಎನ್‌ಕೋಡಿಂಗ್ ಆಗಿದೆ.

### 3. ಟೋಕನ್ ಬಳಸಿ ರಕ್ಷಿತ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗೆ ಪ್ರವೇಶಿಸಿ

```bash
# ಉಳಿಸಿದ ಟೋಕನ್ ಬಳಸಿ
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# ಅಥವಾ ನೇರವಾಗಿ ಟೋಕನ್ ಮೌಲ್ಯದಿಂದ
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

"Hello from MCP OAuth2 Demo!" ಎಂಬ ಯಶಸ್ವಿ ಪ್ರತಿಕ್ರಿಯೆ OAuth2 ಸಂರಚನೆ ಸರಿಯಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದೆ ಎಂದು ದೃಢೀಕರಿಸುತ್ತದೆ.

---

## ಕಂಟೈನರ್ ನಿರ್ಮಾಣ

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## **Azure Container Apps** ಗೆ ನಿಯೋಜಿಸಿ

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

ಇನ್‌ಗ್ರೆಸ್ FQDN ನಿಮ್ಮ **ಇಶ್ಯೂವರ್** ಆಗುತ್ತದೆ (`https://<fqdn>`).  
Azure ಸ್ವಯಂಚಾಲಿತವಾಗಿ `*.azurecontainerapps.io` ಗೆ ವಿಶ್ವಾಸಾರ್ಹ TLS ಪ್ರಮಾಣಪತ್ರವನ್ನು ಒದಗಿಸುತ್ತದೆ.

---

## **Azure API Management** ಗೆ ಸಂಪರ್ಕಿಸಿ

ನಿಮ್ಮ API ಗೆ ಈ ಇನ್‌ಬೌಂಡ್ ಪಾಲಿಸಿಯನ್ನು ಸೇರಿಸಿ:

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

APIM JWKS ಅನ್ನು ಪಡೆದು ಪ್ರತಿ ವಿನಂತಿಯನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ.

---

## ಮುಂದೇನು

- [5.4 ರೂಟ್ ಕಾಂಟೆಕ್ಸ್ಟ್‌ಗಳು](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->