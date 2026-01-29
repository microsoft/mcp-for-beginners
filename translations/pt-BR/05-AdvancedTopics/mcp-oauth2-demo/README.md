# MCP OAuth2 Demo

Este projeto é uma **aplicação Spring Boot minimalista** que atua como:

* um **Spring Authorization Server** (emitindo tokens de acesso JWT via o fluxo `client_credentials`), e  
* um **Resource Server** (protegendo seu próprio endpoint `/hello`).

Ele espelha a configuração mostrada no [post do blog Spring (2 de abril de 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Início rápido (local)

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

## Testando a configuração OAuth2

Você pode testar a configuração de segurança OAuth2 com os seguintes passos:

### 1. Verifique se o servidor está rodando e protegido

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Obtenha um token de acesso usando client credentials

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

Nota: O cabeçalho de Autenticação Basic (`bWNwLWNsaWVudDpzZWNyZXQ=`) é a codificação Base64 de `mcp-client:secret`.

### 3. Acesse o endpoint protegido usando o token

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Uma resposta bem-sucedida com "Hello from MCP OAuth2 Demo!" confirma que a configuração OAuth2 está funcionando corretamente.

---

## Build do container

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Deploy para **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

O FQDN de ingresso se torna seu **issuer** (`https://<fqdn>`).  
O Azure fornece automaticamente um certificado TLS confiável para `*.azurecontainerapps.io`.

---

## Integração com **Azure API Management**

Adicione esta política inbound à sua API:

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

O APIM buscará o JWKS e validará cada requisição.

---

## Próximos passos

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.