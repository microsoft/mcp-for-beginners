# MCP OAuth2 Demo

Tämä projekti on **minimaalinen Spring Boot -sovellus**, joka toimii sekä:

* **Spring Authorization Serverina** (joka myöntää JWT-pääsytunnuksia `client_credentials`-virran kautta), että  
* **Resource Serverina** (suojaten oman `/hello`-päätepisteensä).

Se vastaa asetusta, joka on esitelty [Springin blogikirjoituksessa (2.4.2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Nopeasti käyntiin (paikallinen)

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

## OAuth2-konfiguraation testaaminen

Voit testata OAuth2-turvakonfiguraatiota seuraavilla vaiheilla:

### 1. Varmista, että palvelin on käynnissä ja suojattu

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Hanki pääsytunnus client credentials -menetelmällä

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

Huom: Basic Authentication -otsikko (`bWNwLWNsaWVudDpzZWNyZXQ=`) on Base64-koodaus merkkijonosta `mcp-client:secret`.

### 3. Käytä suojattua päätepistettä tunnuksella

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Onnistunut vastaus, jossa lukee "Hello from MCP OAuth2 Demo!", vahvistaa, että OAuth2-konfiguraatio toimii oikein.

---

## Kontin rakentaminen

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Julkaisu **Azure Container Apps** -ympäristöön

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingressin FQDN toimii **issuerinä** (`https://<fqdn>`).  
Azure tarjoaa automaattisesti luotettavan TLS-varmenteen osoitteelle `*.azurecontainerapps.io`.

---

## Integrointi **Azure API Managementiin**

Lisää tämä inbound-politiikka API:si:

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

APIM hakee JWKS:n ja validoi jokaisen pyynnön.

---

## Mitä seuraavaksi

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.