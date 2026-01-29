# MCP OAuth2 Demo

See projekt on **minimalistlik Spring Boot rakendus**, mis toimib nii:

* **Spring Authorization Serverina** (väljastab JWT ligipääsutokenid `client_credentials` voo kaudu) kui ka  
* **Resource Serverina** (kaitseb oma `/hello` lõpp-punkti).

See peegeldab seadistust, mis on näidatud [Springi blogipostituses (2. aprill 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Kiire alustamine (kohalik)

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

## OAuth2 konfiguratsiooni testimine

Saate testida OAuth2 turvakonfiguratsiooni järgmiste sammudega:

### 1. Kontrollige, kas server töötab ja on kaitstud

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Hankige ligipääsutoken, kasutades kliendi mandaate

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

Märkus: Basic Authentication päis (`bWNwLWNsaWVudDpzZWNyZXQ=`) on Base64 kodeering `mcp-client:secret`.

### 3. Juurdepääs kaitstud lõpp-punktile, kasutades tokenit

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Edukas vastus "Hello from MCP OAuth2 Demo!" kinnitab, et OAuth2 konfiguratsioon töötab õigesti.

---

## Konteineri ehitamine

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Paigaldamine **Azure Container Apps**-i

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN-st saab teie **issuer** (`https://<fqdn>`).  
Azure pakub automaatselt usaldusväärse TLS-sertifikaadi `*.azurecontainerapps.io` jaoks.

---

## Ühendamine **Azure API Management**-iga

Lisage see sissetulev poliitika oma API-le:

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

APIM hangib JWKS-i ja valideerib iga päringu.

---

## Mis edasi

- [5.4 Juurekontekstid](../mcp-root-contexts/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.