# MCP OAuth2 Demo

Mradi huu ni **programu ndogo ya Spring Boot** inayofanya kazi kama:

* **Seva ya Uidhinishaji ya Spring** (inatoa tokeni za JWT kupitia mtiririko wa `client_credentials`), na  
* **Seva ya Rasilimali** (inailinda endpoint yake ya `/hello`).

Inafanana na usanidi ulioonyeshwa katika [chapisho la blogu la Spring (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Anza haraka (ndani ya kompyuta)

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

## Kupima Usanidi wa OAuth2

Unaweza kupima usanidi wa usalama wa OAuth2 kwa hatua zifuatazo:

### 1. Hakiki kuwa seva inaendesha na imehifadhiwa

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Pata tokeni ya ufikiaji kwa kutumia sifa za mteja

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

Note: Kichwa cha Basic Authentication (`bWNwLWNsaWVudDpzZWNyZXQ=`) ni usimbaji wa Base64 wa `mcp-client:secret`.

### 3. Fikia endpoint iliyolindwa kwa kutumia tokeni

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Jibu lenye mafanikio lenye "Hello from MCP OAuth2 Demo!" linathibitisha kuwa usanidi wa OAuth2 unafanya kazi ipasavyo.

---

## Kujenga kontena

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Weka kwenye **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

FQDN ya kuingilia itakuwa **issuer** yako (`https://<fqdn>`).  
Azure hutoa cheti cha TLS kinachotegemewa moja kwa moja kwa `*.azurecontainerapps.io`.

---

## Unganisha na **Azure API Management**

Ongeza sera hii ya kuingiza kwenye API yako:

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

APIM itachukua JWKS na kuthibitisha kila ombi.

---

## Nini kinachofuata

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.