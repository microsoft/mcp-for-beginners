# MCP OAuth2 Demo

Dieses Projekt ist eine **minimalistische Spring Boot-Anwendung**, die sowohl als:

* **Spring Authorization Server** (stellt JWT-Zugriffstoken über den `client_credentials`-Flow aus), als auch  
* **Resource Server** (schützt den eigenen `/hello` Endpunkt).

Es spiegelt die im [Spring Blogbeitrag (2. Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) gezeigte Konfiguration wider.

---

## Schnellstart (lokal)

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

## Testen der OAuth2-Konfiguration

Du kannst die OAuth2-Sicherheitskonfiguration mit den folgenden Schritten testen:

### 1. Überprüfe, ob der Server läuft und gesichert ist

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Hole ein Zugriffstoken mit Client-Credentials

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

Hinweis: Der Basic-Authentication-Header (`bWNwLWNsaWVudDpzZWNyZXQ=`) ist die Base64-Codierung von `mcp-client:secret`.

### 3. Greife mit dem Token auf den geschützten Endpunkt zu

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Eine erfolgreiche Antwort mit "Hello from MCP OAuth2 Demo!" bestätigt, dass die OAuth2-Konfiguration korrekt funktioniert.

---

## Container-Build

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Deployment zu **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Der Ingress-FQDN wird zu deinem **Issuer** (`https://<fqdn>`).  
Azure stellt automatisch ein vertrauenswürdiges TLS-Zertifikat für `*.azurecontainerapps.io` bereit.

---

## Integration in **Azure API Management**

Füge diese Inbound-Policy zu deiner API hinzu:

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

APIM ruft das JWKS ab und validiert jede Anfrage.

---

## Was kommt als Nächstes

- [5.4 Root-Kontexte](../mcp-root-contexts/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.