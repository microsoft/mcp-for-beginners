# Demostración MCP OAuth2

> [!WARNING]
> Esta es una muestra local para aprendizaje, no un servicio de autorización para producción. Utiliza un cliente en memoria y genera una nueva clave de firma al iniciar. Nunca
> lo despliegue con un secreto de cliente compartido, predeterminado o controlado por código fuente.


## Introducción

OAuth2 es el protocolo estándar de la industria para autorización, que permite acceso seguro a recursos sin compartir credenciales. En implementaciones MCP (Model Context Protocol), OAuth2 proporciona una forma robusta de autenticar y autorizar clientes (como agentes de IA) para acceder a servidores MCP y sus herramientas.

Esta lección demuestra cómo implementar autenticación OAuth2 para servidores MCP usando Spring Boot, un patrón común para despliegues empresariales y de producción.

## Objetivos de aprendizaje

Al final de esta lección, usted:
- Entenderá cómo se integra OAuth2 con servidores MCP
- Implementará un Servidor de Autorización Spring para emisión de tokens
- Protegerá los endpoints MCP con autenticación basada en JWT
- Configurará el flujo de credenciales de cliente para comunicación máquina a máquina

## Requisitos previos

- Conocimientos básicos de Java y Spring Boot
- Familiaridad con conceptos MCP de módulos anteriores
- Maven o Gradle instalados

---

## Descripción del proyecto

Este proyecto es una **aplicación mínima Spring Boot** que actúa como ambos:

* un **Servidor de Autorización Spring** (emitiendo tokens JWT mediante el flujo `client_credentials`), y  
* un **Servidor de Recursos** (protegiendo su propio endpoint `/hello`).

Refleja la configuración mostrada en la [publicación del blog de Spring (2 Abr 2025)](https://spring.io/blog/2025/04/02/mcp-server-oauth2).

---

## Inicio rápido (local)

```bash
# Usa un valor local único y mantenlo fuera del historial de shell cuando sea posible.
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# obtener un token
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# llamar al endpoint protegido
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## Prueba de la configuración OAuth2

Puede probar la configuración de seguridad OAuth2 con los siguientes pasos:

### 1. Verifique que el servidor esté en ejecución y seguro

```bash
# Esto debería devolver 401 No autorizado, confirmando que la seguridad OAuth2 está activa
curl -v http://localhost:8081/
```

### 2. Obtenga un token de acceso usando las credenciales del cliente

```bash
# Obtener y extraer la respuesta completa del token
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# O para extraer solo el token (requiere jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

En PowerShell, establezca el secreto local antes de ejecutar Maven:

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. Acceda al endpoint protegido usando el token

```bash
# Usando el token guardado
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# O directamente con el valor del token
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

Una respuesta exitosa con "¡Hola desde MCP OAuth2 Demo!" confirma que la configuración OAuth2 funciona correctamente.

---

## Construcción de contenedor

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## Seguridad en producción

Para un despliegue en producción, use un proveedor de identidad dedicado en lugar de
este servidor de autorización de demostración en proceso. Guarde las credenciales en
un almacenamiento secreto gestionado, rote las claves, use claves de firma persistentes, restrinja los alcances, y
establezca un emisor explícito. Nunca incluya un secreto de cliente en código fuente, imágenes
de contenedor, manifiestos de despliegue o salidas de comandos.

Para Azure Container Apps, almacene el valor como un secreto de Container Apps respaldado por
Key Vault cuando sea posible, y luego exponga solo una referencia secreta a través de la variable de entorno
`OAUTH_CLIENT_SECRET`.

---

## Despliegue en **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

El FQDN de ingreso se convierte en su **emisor** (`https://<fqdn>`).  
Azure proporciona automáticamente un certificado TLS confiable para `*.azurecontainerapps.io`.

---

## Integración con **Azure API Management**

Agregue esta política entrante a su API:

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

- [5.4 Contextos raíz](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->