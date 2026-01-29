# MCP OAuth2 Demo

Det här projektet är en **minimal Spring Boot-applikation** som fungerar både som:

* en **Spring Authorization Server** (utfärdar JWT-access tokens via `client_credentials`-flödet), och  
* en **Resource Server** (skyddar sin egen `/hello`-endpoint).

Det speglar upplägget som visas i [Spring-blogginlägget (2 apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Snabbstart (lokalt)

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

## Testa OAuth2-konfigurationen

Du kan testa OAuth2-säkerhetskonfigurationen med följande steg:

### 1. Kontrollera att servern körs och är säkrad

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Hämta en access token med client credentials

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

Notera: Basic Authentication-headern (`bWNwLWNsaWVudDpzZWNyZXQ=`) är Base64-kodningen av `mcp-client:secret`.

### 3. Använd token för att nå den skyddade endpointen

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Ett lyckat svar med "Hello from MCP OAuth2 Demo!" bekräftar att OAuth2-konfigurationen fungerar som den ska.

---

## Bygg container

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Distribuera till **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingressens FQDN blir din **issuer** (`https://<fqdn>`).  
Azure tillhandahåller automatiskt ett betrott TLS-certifikat för `*.azurecontainerapps.io`.

---

## Koppla till **Azure API Management**

Lägg till denna inbound-policy i din API:

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

APIM hämtar JWKS och validerar varje förfrågan.

---

## Vad händer härnäst

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.