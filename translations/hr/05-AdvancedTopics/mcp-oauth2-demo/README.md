# MCP OAuth2 Demo

Ovaj projekt je **minimalna Spring Boot aplikacija** koja djeluje kao:

* **Spring Authorization Server** (izdaje JWT pristupne tokene putem `client_credentials` toka), i  
* **Resource Server** (štiti vlastiti `/hello` endpoint).

Ona replicira postavke prikazane u [Spring blog postu (2. travnja 2025.)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Brzi početak (lokalno)

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

## Testiranje OAuth2 konfiguracije

OAuth2 sigurnosnu konfiguraciju možete testirati sljedećim koracima:

### 1. Provjerite je li server pokrenut i zaštićen

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Dohvatite pristupni token koristeći client credentials

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

Napomena: Basic Authentication header (`bWNwLWNsaWVudDpzZWNyZXQ=`) je Base64 kodiranje za `mcp-client:secret`.

### 3. Pristupite zaštićenom endpointu koristeći token

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Uspješan odgovor s "Hello from MCP OAuth2 Demo!" potvrđuje da OAuth2 konfiguracija ispravno radi.

---

## Izgradnja kontejnera

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Deploy na **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN postaje vaš **issuer** (`https://<fqdn>`).  
Azure automatski osigurava pouzdani TLS certifikat za `*.azurecontainerapps.io`.

---

## Povezivanje s **Azure API Management**

Dodajte ovu inbound politiku svojem API-ju:

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

APIM će dohvatiti JWKS i validirati svaki zahtjev.

---

## Što slijedi

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.