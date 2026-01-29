# MCP OAuth2 Demo

Dette prosjektet er en **minimal Spring Boot-applikasjon** som fungerer som både:

* en **Spring Authorization Server** (utsteder JWT-tilgangstokener via `client_credentials`-flyten), og  
* en **Resource Server** (beskytter sin egen `/hello`-endepunkt).

Det speiler oppsettet vist i [Spring-blogginnlegget (2. april 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Rask start (lokalt)

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

## Testing av OAuth2-konfigurasjonen

Du kan teste OAuth2-sikkerhetskonfigurasjonen med følgende steg:

### 1. Bekreft at serveren kjører og er sikret

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Skaff et tilgangstoken ved bruk av klientlegitimasjon

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

Merk: Basic Authentication-headeren (`bWNwLWNsaWVudDpzZWNyZXQ=`) er Base64-kodingen av `mcp-client:secret`.

### 3. Få tilgang til det beskyttede endepunktet med tokenet

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Et vellykket svar med "Hello from MCP OAuth2 Demo!" bekrefter at OAuth2-konfigurasjonen fungerer som den skal.

---

## Bygg container

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Distribuer til **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress FQDN blir din **issuer** (`https://<fqdn>`).  
Azure leverer automatisk et betrodd TLS-sertifikat for `*.azurecontainerapps.io`.

---

## Koble til **Azure API Management**

Legg til denne inbound policyen i API-et ditt:

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

APIM vil hente JWKS og validere hver forespørsel.

---

## Hva nå

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.