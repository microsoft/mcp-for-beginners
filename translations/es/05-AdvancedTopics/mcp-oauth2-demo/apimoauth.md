# Desplegando la aplicación Spring AI MCP en Azure Container Apps

([Asegurando los servidores Spring AI MCP con OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figura: Servidor Spring AI MCP asegurado con Spring Authorization Server. El servidor emite tokens de acceso a los clientes y los valida en las solicitudes entrantes (fuente: blog de Spring) ([Asegurando los servidores Spring AI MCP con OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Para desplegar el servidor Spring MCP, constrúyelo como un contenedor y usa Azure Container Apps con ingreso externo. Por ejemplo, usando la CLI de Azure puedes ejecutar:

```bash
az containerapp up \
  --name my-mcp-app \
  --resource-group MyResourceGroup \
  --location eastus \
  --environment MyContainerEnv \
  --image myregistry.azurecr.io/my-mcp-server:latest \
  --ingress external \
  --target-port 8080 \
  --query properties.configuration.ingress.fqdn
```

Esto crea una Container App accesible públicamente con HTTPS habilitado (Azure emite un certificado TLS gratuito para el dominio predeterminado `*.azurecontainerapps.io` ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). La salida del comando incluye el FQDN de la app (por ejemplo, `my-mcp-app.eastus.azurecontainerapps.io`), que se convierte en la base de la **URL del emisor**. Asegúrate de que el ingreso HTTP esté habilitado (como se indicó arriba) para que APIM pueda acceder a la app. En un entorno de prueba/desarrollo, usa la opción `--ingress external` (o vincula un dominio personalizado con TLS según [documentación de Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Guarda cualquier propiedad sensible (como secretos de clientes OAuth) en los secretos de Container Apps o en Azure Key Vault, y mapea estos secretos al contenedor como variables de entorno.

## Configuración de Spring Authorization Server

En el código de tu aplicación Spring Boot, incluye los starters de Spring Authorization Server y Resource Server. Configura un `RegisteredClient` (para el grant `client_credentials` en dev/test) y una fuente de claves JWT. Por ejemplo, en `application.properties` podrías establecer:

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

Habilita el Authorization Server y Resource Server definiendo una cadena de filtros de seguridad. Por ejemplo:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Enable the Authorization Server endpoints
            .apply(authzServer.and())
            // Enable the Resource Server (validate JWT on incoming requests)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Disable CSRF (MCP server is not browser-based)
            .csrf(csrf -> csrf.disable())
            // Allow CORS for client demo tools
            .cors(withDefaults());
        return http.build();
    }

    // Define an in-memory client (RegisteredClient) and a JWK source:
    @Bean
    public RegisteredClientRepository registeredClientRepository() {
        RegisteredClient client = RegisteredClient.withId("1")
            .clientId("mcp-client")
            .clientSecret("{noop}secret")
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Generate an RSA key (for dev/test, generate anew at startup)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Esta configuración expondrá los endpoints OAuth2 predeterminados: `/oauth2/token` para tokens y `/oauth2/jwks` para el conjunto de claves JSON Web Key Set. (Por defecto, `AuthorizationServerSettings` de Spring mapea `/oauth2/token` y `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) El servidor emitirá tokens de acceso JWT firmados con la clave RSA mencionada arriba y publicará su clave pública en `https://<tu-app>:/oauth2/jwks`.

**Habilita el descubrimiento OpenID Connect:** Para que APIM recupere automáticamente el emisor y JWKS, habilita el endpoint de configuración del proveedor OIDC agregando `.oidc(Customizer.withDefaults())` en tu configuración de seguridad ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Por ejemplo:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

Esto expone `/.well-known/openid-configuration`, que APIM puede usar para obtener metadatos. Finalmente, es posible que quieras personalizar la reclamación **audience** del JWT para que la verificación `<audiences>` de APIM pase correctamente. Por ejemplo, añade un personalizador de tokens:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Esto asegura que los tokens lleven `"aud": ["mcp-client"]`, coincidiendo con el ID de cliente o el scope esperado por APIM.

## Exponiendo los endpoints de Token y JWKS

Después del despliegue, la **URL del emisor** de tu app será `https://<app-fqdn>`, por ejemplo `https://my-mcp-app.eastus.azurecontainerapps.io`. Sus endpoints OAuth2 son:

- **Endpoint de token:** `https://<app-fqdn>/oauth2/token` – aquí los clientes obtienen tokens (flujo client_credentials).
- **Endpoint JWKS:** `https://<app-fqdn>/oauth2/jwks` – devuelve el conjunto JWK (usado por APIM para obtener las claves de firma).
- **Configuración OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON de descubrimiento OIDC (contiene `issuer`, `token_endpoint`, `jwks_uri`, etc.).

APIM apuntará a la **URL de configuración OpenID**, desde donde descubrirá el `jwks_uri`. Por ejemplo, si el FQDN de tu Container App es `my-mcp-app.eastus.azurecontainerapps.io`, entonces el `<openid-config url="...">` de APIM debería usar `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Por defecto, Spring establecerá el `issuer` en esos metadatos con la misma URL base ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configuración de Azure API Management (`validate-jwt`)

En Azure APIM, añade una política de entrada que use la política `<validate-jwt>` para validar los JWT entrantes contra tu Spring Authorization Server. Para una configuración sencilla, puedes usar la URL de metadatos OpenID Connect. Fragmento de política de ejemplo:

```xml
<inbound>
  <validate-jwt header-name="Authorization" require-scheme="Bearer">
    <openid-config url="https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration" />
    <audiences>
      <audience>mcp-client</audience>  <!-- Expected audience in the JWT -->
    </audiences>
    <issuers>
      <issuer>https://my-mcp-app.eastus.azurecontainerapps.io</issuer>
    </issuers>
  </validate-jwt>
  <!-- (optional) other policies -->
</inbound>
```

Esta política indica a APIM que obtenga la configuración OpenID del Spring Auth Server, recupere su JWKS y valide que cada token esté firmado por una clave confiable y tenga la audiencia correcta. (Si omites `<issuers>`, APIM usará automáticamente la reclamación `issuer` de los metadatos.) El `<audience>` debe coincidir con tu ID de cliente o identificador del recurso API en el token (en el ejemplo anterior, lo configuramos como `"mcp-client"`). Esto es consistente con la documentación de Microsoft sobre el uso de `validate-jwt` con `<openid-config>` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Después de la validación, APIM reenviará la solicitud (incluyendo el encabezado `Authorization` original) al backend. Dado que la app Spring también es un resource server, volverá a validar el token, pero APIM ya habrá asegurado su validez. (Para desarrollo, puedes confiar en la validación de APIM y deshabilitar las comprobaciones adicionales en la app si lo deseas, pero es más seguro mantener ambas.)

## Ejemplo de configuración

| Configuración      | Valor de ejemplo                                                   | Notas                                      |
|--------------------|-------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | URL de tu Container App (URI base)         |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | Endpoint de token predeterminado de Spring ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | Endpoint predeterminado del conjunto JWK ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Documento de descubrimiento OIDC (generado automáticamente)    |
| **Audiencia APIM** | `mcp-client`                                                      | ID de cliente OAuth o nombre del recurso API |
| **Política APIM**  | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` usa esta URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Errores comunes

- **HTTPS/TLS:** El gateway de APIM requiere que el endpoint OpenID/JWKS sea HTTPS con un certificado válido. Por defecto, Azure Container Apps proporciona un certificado TLS confiable para el dominio gestionado por Azure ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Si usas un dominio personalizado, asegúrate de vincular un certificado (puedes usar la función de certificado gestionado gratuito de Azure) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Si APIM no puede confiar en el certificado del endpoint, `<validate-jwt>` fallará al obtener los metadatos.

- **Accesibilidad del endpoint:** Asegúrate de que los endpoints de la app Spring sean accesibles desde APIM. Usar `--ingress external` (o habilitar ingreso en el portal) es lo más sencillo. Si elegiste un entorno interno o vinculado a una vNet, APIM (que por defecto es público) podría no alcanzarlo a menos que esté en la misma vNet. En un entorno de prueba, prefiere ingreso público para que APIM pueda llamar a las URLs `.well-known` y `/jwks`.

- **Descubrimiento OpenID habilitado:** Por defecto, Spring Authorization Server **no expone** `/.well-known/openid-configuration` a menos que OIDC esté habilitado. Asegúrate de incluir `.oidc(Customizer.withDefaults())` en tu configuración de seguridad (ver arriba) para que el endpoint de configuración del proveedor esté activo ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). De lo contrario, la llamada `<openid-config>` de APIM devolverá un error 404.

- **Reclamación Audience:** El comportamiento predeterminado de Spring es establecer la reclamación `aud` con el ID de cliente. Si la verificación `<audience>` de APIM falla, puede que necesites personalizar el token (como se mostró arriba) o ajustar la política de APIM. Asegúrate de que la audiencia en tu JWT coincida con lo que configures en `<audience>`.

- **Análisis del JSON de metadatos:** El JSON de configuración OpenID debe ser válido. La configuración predeterminada de Spring emitirá un documento estándar de metadatos OIDC. Verifica que contenga el `issuer` y `jwks_uri` correctos. Si alojas Spring detrás de un proxy o ruta basada en path, revisa bien las URLs en estos metadatos. APIM usará estos valores tal cual.

- **Orden de la política:** En la política de APIM, coloca `<validate-jwt>` **antes** de cualquier enrutamiento al backend. De lo contrario, las llamadas podrían llegar a tu app sin un token válido. También asegúrate de que `<validate-jwt>` aparezca inmediatamente bajo `<inbound>` (no anidado dentro de otra condición) para que APIM lo aplique.

Siguiendo estos pasos, puedes ejecutar tu servidor Spring AI MCP en Azure Container Apps y hacer que Azure API Management valide los JWT OAuth2 entrantes con una política mínima. Los puntos clave son: exponer los endpoints de Spring Auth públicamente con TLS, habilitar el descubrimiento OIDC y apuntar el `validate-jwt` de APIM a la URL de configuración OpenID (para que pueda obtener el JWKS automáticamente). Esta configuración es adecuada para un entorno de desarrollo/prueba; para producción, considera una gestión adecuada de secretos, tiempos de vida de tokens y rotación de claves en JWKS según sea necesario.
**Referencias:** Consulta la documentación de Spring Authorization Server para los endpoints predeterminados ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) y la configuración OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); consulta la documentación de Microsoft APIM para ejemplos de `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); y la documentación de Azure Container Apps para despliegue y certificados ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.