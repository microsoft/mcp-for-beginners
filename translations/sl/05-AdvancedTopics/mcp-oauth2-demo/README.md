# MCP OAuth2 Demo

Ta projekt je **minimalna Spring Boot aplikacija**, ki deluje kot:

* **Spring Authorization Server** (izdaja JWT dostopne žetone preko `client_credentials` toka), in  
* **Resource Server** (varuje svoj `/hello` endpoint).

Sledi nastavitvi, prikazani v [Spring blog objavi (2. aprila 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Hiter začetek (lokalno)

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

OAuth2 varnostno konfiguracijo lahko preizkusite z naslednjimi koraki:

### 1. Preverite, da strežnik teče in je zaščiten

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Pridobite dostopni žeton z uporabo klientovih poverilnic

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

Opomba: Basic Authentication header (`bWNwLWNsaWVudDpzZWNyZXQ=`) je Base64 kodiranje za `mcp-client:secret`.

### 3. Dostopajte do zaščitenega endpointa z žetonom

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Uspešen odgovor z "Hello from MCP OAuth2 Demo!" potrjuje, da OAuth2 konfiguracija deluje pravilno.

---

## Gradnja kontejnerja

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Namestitev v **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN postane vaš **issuer** (`https://<fqdn>`).  
Azure samodejno zagotovi zaupanja vreden TLS certifikat za `*.azurecontainerapps.io`.

---

## Povezava z **Azure API Management**

Dodajte to inbound politiko vaši API:

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

APIM bo pridobil JWKS in preverjal vsak zahtevek.

---

## Kaj sledi

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.