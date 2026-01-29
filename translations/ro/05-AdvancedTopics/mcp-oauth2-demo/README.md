# MCP OAuth2 Demo

Acest proiect este o **aplicație minimală Spring Boot** care funcționează atât ca:

* un **Spring Authorization Server** (emitând tokenuri JWT de acces prin fluxul `client_credentials`), cât și  
* un **Resource Server** (protejând propriul endpoint `/hello`).

Reprezintă configurația prezentată în [postarea de pe blogul Spring (2 apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Pornire rapidă (local)

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

## Testarea configurației OAuth2

Poți testa configurația de securitate OAuth2 urmând pașii de mai jos:

### 1. Verifică dacă serverul este pornit și securizat

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Obține un token de acces folosind client credentials

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

Notă: Header-ul Basic Authentication (`bWNwLWNsaWVudDpzZWNyZXQ=`) este codificarea Base64 a șirului `mcp-client:secret`.

### 3. Accesează endpoint-ul protejat folosind tokenul

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Un răspuns de succes cu mesajul "Hello from MCP OAuth2 Demo!" confirmă că configurația OAuth2 funcționează corect.

---

## Construirea containerului

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Deploy pe **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN devine **issuer-ul** tău (`https://<fqdn>`).  
Azure oferă automat un certificat TLS de încredere pentru `*.azurecontainerapps.io`.

---

## Integrare cu **Azure API Management**

Adaugă această politică inbound la API-ul tău:

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

APIM va prelua JWKS și va valida fiecare cerere.

---

## Ce urmează

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.