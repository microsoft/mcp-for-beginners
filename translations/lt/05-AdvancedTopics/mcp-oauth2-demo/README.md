# MCP OAuth2 Demo

Šis projektas yra **minimalus Spring Boot taikymas**, kuris veikia kaip:

* **Spring Authorization Server** (išduodantis JWT prieigos žetonus per `client_credentials` srautą), ir  
* **Resource Server** (apsaugantis savo `/hello` galinį tašką).

Jis atspindi konfigūraciją, aprašytą [Spring tinklaraščio įraše (2025 m. balandžio 2 d.)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Greitas startas (lokaliai)

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

## OAuth2 konfigūracijos testavimas

OAuth2 saugumo konfigūraciją galite patikrinti atlikdami šiuos veiksmus:

### 1. Patikrinkite, ar serveris veikia ir yra apsaugotas

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Gaukite prieigos žetoną naudodami klientų kredencialus

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

Pastaba: Basic Authentication antraštė (`bWNwLWNsaWVudDpzZWNyZXQ=`) yra Base64 kodavimas iš `mcp-client:secret`.

### 3. Pasiekite apsaugotą galinį tašką naudodami žetoną

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Sėkmingas atsakymas su "Hello from MCP OAuth2 Demo!" patvirtina, kad OAuth2 konfigūracija veikia tinkamai.

---

## Konteinerio kūrimas

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Diegimas į **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Įėjimo FQDN tampa jūsų **issuer** (`https://<fqdn>`).  
Azure automatiškai suteikia patikimą TLS sertifikatą `*.azurecontainerapps.io`.

---

## Integracija su **Azure API Management**

Pridėkite šią įeinančią politiką prie savo API:

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

APIM gaus JWKS ir patikrins kiekvieną užklausą.

---

## Kas toliau

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.