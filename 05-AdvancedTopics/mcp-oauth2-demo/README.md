# MCP OAuth2 Demo

> [!WARNING]
> This is a local learning sample, not a production authorization service. It
> uses an in-memory client and generates a new signing key at startup. Never
> deploy it with a shared, default, or source-controlled client secret.

## Introduction

OAuth2 is the industry-standard protocol for authorization, enabling secure access to resources without sharing credentials. In MCP (Model Context Protocol) implementations, OAuth2 provides a robust way to authenticate and authorize clients (such as AI agents) to access MCP servers and their tools.

This lesson demonstrates how to implement OAuth2 authentication for MCP servers using Spring Boot, a common pattern for enterprise and production deployments.

## Learning Objectives

By the end of this lesson, you will:
- Understand how OAuth2 integrates with MCP servers
- Implement a Spring Authorization Server for token issuance
- Protect MCP endpoints with JWT-based authentication
- Configure client credentials flow for machine-to-machine communication

## Prerequisites

- Basic understanding of Java and Spring Boot
- Familiarity with MCP concepts from earlier modules
- Maven or Gradle installed

---

## Project Overview

This project is a **minimal Spring Boot application** that acts as both:

* a **Spring Authorization Server** (issuing JWT access tokens via the `client_credentials` flow), and  
* a **Resource Server** (protecting its own `/hello` endpoint).

It mirrors the setup shown in the [Spring blog post (2 Apr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Quick start (local)

```bash
# Use a unique local value and keep it out of shell history where possible.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# obtain a token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# call the protected endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Testing the OAuth2 Configuration

You can test the OAuth2 security configuration with the following steps:

### 1. Verify the server is running and secured

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Get an access token using client credentials

```bash
# Get and extract the full token response
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Or to extract just the token (requires jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

On PowerShell, set the local secret before running Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Access the protected endpoint using the token

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

A successful response with "Hello from MCP OAuth2 Demo!" confirms that the OAuth2 configuration is working correctly.

---

## Container build

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Production Security

For a production deployment, use a dedicated identity provider rather than
this in-process demo authorization server. Store credentials in a managed
secret store, rotate them, use persistent signing keys, restrict scopes, and
set an explicit issuer. Never place a client secret in source code, container
images, deployment manifests, or command output.

For Azure Container Apps, store the value as a Container Apps secret backed by
Key Vault where possible, then expose only a secret reference through the
`OAUTH_CLIENT_SECRET` environment variable.

---

## Deploy to **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

The ingress FQDN becomes your **issuer** (`https://<fqdn>`).  
Azure provides a trusted TLS certificate automatically for `*.azurecontainerapps.io`.

---

## Wire into **Azure API Management**

Add this inbound policy to your API:

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

APIM will fetch the JWKS and validate every request.

---

## What's next

- [5.4 Root contexts](../mcp-root-contexts/README.md)