# MCP OAuth2 Demo

Tento projekt je **minimálna Spring Boot aplikácia**, ktorá slúži zároveň ako:

* **Spring Authorization Server** (vydáva JWT prístupové tokeny cez `client_credentials` flow), a  
* **Resource Server** (chráni vlastný endpoint `/hello`).

Zrkadlí nastavenie z [Spring blogu (2. apríl 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Rýchly štart (lokálne)

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

## Testovanie OAuth2 konfigurácie

OAuth2 bezpečnostnú konfiguráciu môžete otestovať nasledovne:

### 1. Overte, že server beží a je zabezpečený

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Získajte prístupový token pomocou klientskych údajov

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

Poznámka: Basic Authentication hlavička (`bWNwLWNsaWVudDpzZWNyZXQ=`) je Base64 kódovanie reťazca `mcp-client:secret`.

### 3. Pristúpte k chránenému endpointu pomocou tokenu

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Úspešná odpoveď s textom "Hello from MCP OAuth2 Demo!" potvrdzuje, že OAuth2 konfigurácia funguje správne.

---

## Vytvorenie kontajnera

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Nasadenie do **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN sa stáva vaším **issuerom** (`https://<fqdn>`).  
Azure automaticky poskytuje dôveryhodný TLS certifikát pre `*.azurecontainerapps.io`.

---

## Prepojenie s **Azure API Management**

Pridajte túto inbound politiku do vášho API:

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

APIM stiahne JWKS a overí každý request.

---

## Čo ďalej

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.