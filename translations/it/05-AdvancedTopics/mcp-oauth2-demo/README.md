# MCP OAuth2 Demo

Questo progetto è una **applicazione Spring Boot minimale** che funge sia da:

* **Spring Authorization Server** (emettendo token di accesso JWT tramite il flusso `client_credentials`), sia  
* **Resource Server** (proteggendo il proprio endpoint `/hello`).

Ricalca la configurazione mostrata nel [post del blog Spring (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Avvio rapido (locale)

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

## Testare la configurazione OAuth2

Puoi testare la configurazione di sicurezza OAuth2 con i seguenti passaggi:

### 1. Verifica che il server sia in esecuzione e protetto

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Ottieni un token di accesso usando le credenziali client

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

Nota: L’header di Basic Authentication (`bWNwLWNsaWVudDpzZWNyZXQ=`) è la codifica Base64 di `mcp-client:secret`.

### 3. Accedi all’endpoint protetto usando il token

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Una risposta positiva con "Hello from MCP OAuth2 Demo!" conferma che la configurazione OAuth2 funziona correttamente.

---

## Build del container

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Deploy su **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

L’ingress FQDN diventa il tuo **issuer** (`https://<fqdn>`).  
Azure fornisce automaticamente un certificato TLS attendibile per `*.azurecontainerapps.io`.

---

## Integrazione con **Azure API Management**

Aggiungi questa policy inbound alla tua API:

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

APIM recupererà il JWKS e convaliderà ogni richiesta.

---

## Cosa fare dopo

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.