# MCP OAuth2 Demo

> [!WARNING]
> Dis na local learning sample, e no be production authorization service. E
> dey use in-memory client and e go generate new signing key when e start. No
> ever deploy am wit shared, default, or source-controlled client secret.

## Introduction

OAuth2 na di industry-standard protocol for authorization, e dey enable secure access to resources without make person share credentials. For MCP (Model Context Protocol) implementations, OAuth2 dey provide strong way to authenticate and authorize clients (like AI agents) to fit access MCP servers and their tools.

Dis lesson dey show how to implement OAuth2 authentication for MCP servers using Spring Boot, wey be common style for enterprise and production deployments.

## Learning Objectives

By di end of dis lesson, you go:
- Understand how OAuth2 dey join with MCP servers
- Implement Spring Authorization Server for token issuance
- Protect MCP endpoints wit JWT-based authentication
- Configure client credentials flow for machine-to-machine communication

## Prerequisites

- Basic knowledge of Java and Spring Boot
- Familiarity wit MCP concepts from earlier modules
- Maven or Gradle wey you don install

---

## Project Overview

Dis project na **minimal Spring Boot application** wey dey act as:

* a **Spring Authorization Server** (wey dey issue JWT access tokens via `client_credentials` flow), and  
* a **Resource Server** (wey dey protect its own `/hello` endpoint).

E dey mirror the setup wey spring show for [Spring blog post (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Quick start (local)

```bash
# Use one unique local value and keep am outside shell history wen e possible.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# make you get token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# call di protected endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testing the OAuth2 Configuration

You fit test the OAuth2 security configuration wit dis steps:

### 1. Check say di server dey run and e dey secured

```bash
# Dis go return 401 Unauthorized, e show say OAuth2 security dey active
curl -v http://localhost:8081/
```

### 2. Get access token using client credentials

```bash
# Comot and open full token response
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Or make you comot only the token (e go need jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

For PowerShell, set the local secret before you run Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Access the protected endpoint wit the token

```bash
# Using di saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or straight wit di token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

If you receive "Hello from MCP OAuth2 Demo!" e mean say the OAuth2 configuration dey work well.

---

## Container build

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Production Security

For production deployment, make you use dedicated identity provider no be
dis in-process demo authorization server. Make you store credentials for managed
secret store, rotate dem, use persistent signing keys, limit scopes, and
set explicit issuer. No ever put client secret for source code, container
images, deployment manifests, or command output.

For Azure Container Apps, store the value as Container Apps secret backed by
Key Vault if you fit, then make only secret reference dey through
`OAUTH_CLIENT_SECRET` environment variable.

---

## Deploy to **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

The ingress FQDN go become your **issuer** (`https://<fqdn>`).  
Azure go provide trusted TLS certificate automatically for `*.azurecontainerapps.io`.

---

## Wire into **Azure API Management**

Add dis inbound policy to your API:

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

APIM go dey fetch the JWKS and dey validate every request.

---

## Wetin dey next

- [5.4 Root contexts](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->