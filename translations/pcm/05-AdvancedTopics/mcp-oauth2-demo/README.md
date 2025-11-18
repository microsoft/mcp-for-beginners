<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0a7083e660ca0d85fd6a947514c61993",
  "translation_date": "2025-11-18T19:28:17+00:00",
  "source_file": "05-AdvancedTopics/mcp-oauth2-demo/README.md",
  "language_code": "pcm"
}
-->
# MCP OAuth2 Demo

Dis project na **small Spring Boot application** wey dey do two things:

* e be **Spring Authorization Server** (e dey give JWT access tokens wit di `client_credentials` flow), and  
* e be **Resource Server** (e dey protect im own `/hello` endpoint).

E dey follow di setup wey dem show for [Spring blog post (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Quick start (local)

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

## How to test di OAuth2 Configuration

You fit test di OAuth2 security configuration wit dis steps:

### 1. Check say di server dey run and e secure

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Collect access token wit client credentials

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

Note: Di Basic Authentication header (`bWNwLWNsaWVudDpzZWNyZXQ=`) na di Base64 encoding of `mcp-client:secret`.

### 3. Use di token take access di protected endpoint

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

If you see response wey talk "Hello from MCP OAuth2 Demo!", e mean say di OAuth2 configuration dey work well.

---

## How to build container

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## How to deploy go **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Di ingress FQDN go turn your **issuer** (`https://<fqdn>`).  
Azure go automatically provide trusted TLS certificate for `*.azurecontainerapps.io`.

---

## How to connect am to **Azure API Management**

Add dis inbound policy to your API:

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

APIM go fetch di JWKS and e go validate every request.

---

## Wetin next

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am correct, abeg make you sabi say machine transle-shon fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->