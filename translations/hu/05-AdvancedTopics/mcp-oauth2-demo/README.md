# MCP OAuth2 Demo

Ez a projekt egy **minimális Spring Boot alkalmazás**, amely egyszerre működik:

* **Spring Authorization Server-ként** (JWT hozzáférési tokeneket bocsát ki a `client_credentials` folyamat segítségével), és  
* **Resource Server-ként** (védi a saját `/hello` végpontját).

Ez a beállítás megegyezik a [Spring blogbejegyzésben (2025. április 2.)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) bemutatottal.

---

## Gyors kezdés (helyi)

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

## Az OAuth2 konfiguráció tesztelése

Az OAuth2 biztonsági beállításokat a következő lépésekkel tesztelheted:

### 1. Ellenőrizd, hogy a szerver fut és védett

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Szerezz hozzáférési tokent client credentials segítségével

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

Megjegyzés: A Basic Authentication fejléc (`bWNwLWNsaWVudDpzZWNyZXQ=`) a `mcp-client:secret` Base64 kódolása.

### 3. Érd el a védett végpontot a tokennel

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Ha a válasz sikeres és a "Hello from MCP OAuth2 Demo!" üzenetet kapod, az azt jelenti, hogy az OAuth2 konfiguráció helyesen működik.

---

## Konténer építése

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Telepítés **Azure Container Apps**-re

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Az ingress FQDN lesz az **issuer** (`https://<fqdn>`).  
Az Azure automatikusan biztosít egy megbízható TLS tanúsítványt a `*.azurecontainerapps.io` domainhez.

---

## Integráció az **Azure API Management**-be

Add hozzá ezt a bejövő szabályt az API-dhoz:

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

Az APIM lekéri a JWKS-t és minden kérést érvényesít.

---

## Mi következik

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.