# MCP OAuth2 Demo

Dette projekt er en **minimal Spring Boot-applikation**, der fungerer som både:

* en **Spring Authorization Server** (udsteder JWT-adgangstokens via `client_credentials` flowet), og  
* en **Resource Server** (beskytter sin egen `/hello` endpoint).

Det afspejler opsætningen vist i [Spring blogindlægget (2. apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Hurtig start (lokalt)

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

## Test af OAuth2-konfigurationen

Du kan teste OAuth2-sikkerhedskonfigurationen med følgende trin:

### 1. Bekræft at serveren kører og er sikret

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Hent et adgangstoken ved hjælp af client credentials

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

Bemærk: Basic Authentication-headeren (`bWNwLWNsaWVudDpzZWNyZXQ=`) er Base64-kodningen af `mcp-client:secret`.

### 3. Få adgang til den beskyttede endpoint med tokenet

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Et succesfuldt svar med "Hello from MCP OAuth2 Demo!" bekræfter, at OAuth2-konfigurationen fungerer korrekt.

---

## Container build

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Deploy til **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN bliver din **issuer** (`https://<fqdn>`).  
Azure leverer automatisk et betroet TLS-certifikat til `*.azurecontainerapps.io`.

---

## Integrer med **Azure API Management**

Tilføj denne inbound policy til din API:

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

APIM henter JWKS og validerer hver anmodning.

---

## Hvad er det næste

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.