# MCP OAuth2 Demo

Ang proyektong ito ay isang **minimal na Spring Boot application** na gumaganap bilang:

* isang **Spring Authorization Server** (nagbibigay ng JWT access tokens gamit ang `client_credentials` flow), at  
* isang **Resource Server** (pinoprotektahan ang sariling `/hello` endpoint).

Ito ay sumusunod sa setup na ipinakita sa [Spring blog post (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Mabilis na pagsisimula (lokal)

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

## Pagsubok sa OAuth2 Configuration

Maaari mong subukan ang OAuth2 security configuration gamit ang mga sumusunod na hakbang:

### 1. Siguraduhing tumatakbo at secured ang server

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Kumuha ng access token gamit ang client credentials

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

Tandaan: Ang Basic Authentication header (`bWNwLWNsaWVudDpzZWNyZXQ=`) ay ang Base64 encoding ng `mcp-client:secret`.

### 3. I-access ang protektadong endpoint gamit ang token

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Ang matagumpay na tugon na may "Hello from MCP OAuth2 Demo!" ay nagpapatunay na tama ang OAuth2 configuration.

---

## Pagbuo ng Container

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## I-deploy sa **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ang ingress FQDN ang magiging iyong **issuer** (`https://<fqdn>`).  
Awtomatikong nagbibigay ang Azure ng trusted TLS certificate para sa `*.azurecontainerapps.io`.

---

## I-integrate sa **Azure API Management**

Idagdag ang inbound policy na ito sa iyong API:

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

Kukunin ng APIM ang JWKS at susuriin ang bawat request.

---

## Ano ang susunod

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.