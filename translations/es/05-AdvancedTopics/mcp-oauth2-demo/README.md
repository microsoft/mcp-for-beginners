# MCP OAuth2 Demo

Este proyecto es una **aplicación mínima de Spring Boot** que funciona como:

* un **Spring Authorization Server** (emitiendo tokens de acceso JWT mediante el flujo `client_credentials`), y  
* un **Resource Server** (protegiendo su propio endpoint `/hello`).

Refleja la configuración mostrada en la [entrada del blog de Spring (2 Abr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Inicio rápido (local)

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

## Probando la configuración OAuth2

Puedes probar la configuración de seguridad OAuth2 con los siguientes pasos:

### 1. Verifica que el servidor esté en funcionamiento y protegido

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. Obtén un token de acceso usando las credenciales del cliente

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

Nota: El encabezado de Autenticación Básica (`bWNwLWNsaWVudDpzZWNyZXQ=`) es la codificación Base64 de `mcp-client:secret`.

### 3. Accede al endpoint protegido usando el token

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Una respuesta exitosa con "Hello from MCP OAuth2 Demo!" confirma que la configuración OAuth2 está funcionando correctamente.

---

## Construcción del contenedor

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## Despliegue en **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

El FQDN de ingreso se convierte en tu **issuer** (`https://<fqdn>`).  
Azure proporciona automáticamente un certificado TLS confiable para `*.azurecontainerapps.io`.

---

## Integración con **Azure API Management**

Agrega esta política de entrada a tu API:

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

APIM obtendrá el JWKS y validará cada solicitud.

---

## Qué sigue

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.