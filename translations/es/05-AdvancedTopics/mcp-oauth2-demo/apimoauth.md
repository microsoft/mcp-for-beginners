# Desplegando la aplicación Spring AI MCP en Azure Container Apps

> [!WARNING]
> Este servidor combinado de autorización/recursos está destinado para aprendizaje y
> uso de desarrollo/pruebas. Los sistemas de producción deben usar un proveedor de identidad dedicado,
> claves de firma persistentes y credenciales almacenadas en un almacén de secretos gestionado.

 ([Asegurando los servidores Spring AI MCP con OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *Figura: Servidor Spring AI MCP asegurado con Spring Authorization Server. El servidor emite tokens de acceso a los clientes y los valida en las peticiones entrantes (fuente: blog de Spring) ([Asegurando los servidores Spring AI MCP con OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* Para desplegar el servidor Spring MCP, constrúyalo como un contenedor y use Azure Container Apps con ingreso externo. Por ejemplo, usando la CLI de Azure puede ejecutar:

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

Esto crea una Container App accesible públicamente con HTTPS habilitado (Azure emite un certificado TLS gratuito para el dominio predeterminado `*.azurecontainerapps.io` ([Nombres de dominio personalizados y certificados gestionados gratuitos en Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). La salida del comando incluye el FQDN de la aplicación (por ejemplo `my-mcp-app.eastus.azurecontainerapps.io`), que se convierte en la base de la **URL del emisor**. Asegúrese de habilitar el ingreso HTTP (como arriba) para que APIM pueda alcanzar la aplicación. En un entorno de prueba/desarrollo, use la opción `--ingress external` (o vincule un dominio personalizado con TLS según [documentación de Microsoft](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) ([Nombres de dominio personalizados y certificados gestionados gratuitos en Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))). Almacene cualquier propiedad sensible (como secretos de cliente OAuth) en secretos de Container Apps o Azure Key Vault, y mapéelos dentro del contenedor como variables de entorno. 

## Configurando Spring Authorization Server

En el código de su aplicación Spring Boot, incluya los starters de Spring Authorization Server y Resource Server. Configure un `RegisteredClient` (para el tipo de concesión `client_credentials` en desarrollo/pruebas) y una fuente de clave JWT. Por ejemplo, en `application.properties` podría establecer:

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

Habilite el Authorization Server y Resource Server definiendo una cadena de filtros de seguridad. Por ejemplo:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // Habilitar los endpoints del Servidor de Autorización
            .apply(authzServer.and())
            // Habilitar el Servidor de Recursos (validar JWT en las solicitudes entrantes)
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // Deshabilitar CSRF (el servidor MCP no está basado en navegador)
            .csrf(csrf -> csrf.disable())
            // Permitir CORS para las herramientas de demostración del cliente
            .cors(withDefaults());
        return http.build();
    }

    // Definir un cliente en memoria (RegisteredClient) y una fuente JWK:
    @Bean
    public RegisteredClientRepository registeredClientRepository(
        @Value("${demo.oauth.client-id}") String clientId,
        @Value("${demo.oauth.client-secret}") String clientSecret) {
      PasswordEncoder encoder = PasswordEncoderFactories.createDelegatingPasswordEncoder();
        RegisteredClient client = RegisteredClient.withId("1")
        .clientId(clientId)
        .clientSecret(encoder.encode(clientSecret))
            .authorizationGrantType(AuthorizationGrantType.CLIENT_CREDENTIALS)
            .scope("mcp.read")
            .clientSettings(ClientSettings.builder().build())
            .tokenSettings(TokenSettings.builder().build())
            .build();
        return new InMemoryRegisteredClientRepository(client);
    }

    @Bean
    public JWKSource<SecurityContext> jwkSource() {
        // Generar una clave RSA (para desarrollo/pruebas, generar de nuevo al iniciar)
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

Esta configuración expondrá los endpoints OAuth2 por defecto: `/oauth2/token` para tokens y `/oauth2/jwks` para el conjunto de claves JSON Web Key Set. (Por defecto, `AuthorizationServerSettings` de Spring asigna `/oauth2/token` y `/oauth2/jwks` ([Modelo de Configuración :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).) El servidor emitirá tokens de acceso JWT firmados con la clave RSA anterior, y publicará su clave pública en `https://<su-app>:/oauth2/jwks`. 

**Habilitar descubrimiento OpenID Connect:** Para que APIM recupere automáticamente el emisor y JWKS, habilite el endpoint de configuración del proveedor OIDC añadiendo `.oidc(Customizer.withDefaults())` en la configuración de seguridad ([Modelo de Configuración :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). Por ejemplo:

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– habilita /.well-known/openid-configuration
```

Esto expone `/.well-known/openid-configuration`, que APIM puede usar para metadatos. Finalmente, puede querer personalizar la afirmación **audience** del JWT para que la verificación `<audiences>` de APIM pase. Por ejemplo, agregue un personalizador de token:

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Establecer una audiencia personalizada (por ejemplo, el ID del cliente o el identificador de la API)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

Esto asegura que los tokens lleven `"aud": ["mcp-client"]`, coincidiendo con el ID de cliente o el ámbito esperado por APIM. 

## Exponiendo los endpoints de Token y JWKS

Después del despliegue, la **URL del emisor** de su aplicación será `https://<app-fqdn>`, por ejemplo `https://my-mcp-app.eastus.azurecontainerapps.io`. Sus endpoints OAuth2 son:

- **Endpoint de Token:** `https://<app-fqdn>/oauth2/token` – los clientes obtienen tokens aquí (flujo client_credentials).
- **Endpoint de JWKS:** `https://<app-fqdn>/oauth2/jwks` – devuelve el conjunto de JWK (usado por APIM para obtener claves de firma).
- **Configuración OpenID:** `https://<app-fqdn>/.well-known/openid-configuration` – JSON de descubrimiento OIDC (contiene `issuer`, `token_endpoint`, `jwks_uri`, etc.).  

APIM apuntará a la **URL de configuración OpenID**, desde la cual descubre el `jwks_uri`. Por ejemplo, si el FQDN de su Container App es `my-mcp-app.eastus.azurecontainerapps.io`, entonces el `<openid-config url="...">` de APIM debe usar `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`. (Por defecto, Spring establece el `issuer` en esa metadata con la misma URL base ([Modelo de Configuración :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)).)

## Configurando Azure API Management (`validate-jwt`)

En Azure APIM, agregue una política de entrada que use la política `<validate-jwt>` para verificar los JWT entrantes contra su Spring Authorization Server. Para una configuración simple, puede usar la URL de metadatos OpenID Connect. Fragmento de política de ejemplo:

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

Esta política indica a APIM que obtenga la configuración OpenID del servidor de Spring Auth, recupere su JWKS y valide que cada token esté firmado por una clave confiable y tenga la audiencia correcta. (Si omite `<issuers>`, APIM usará automáticamente la afirmación `issuer` de los metadatos.) El `<audience>` debe coincidir con el ID de cliente o identificador del recurso API en el token (en el ejemplo arriba, lo configuramos como `"mcp-client"`). Esto es consistente con la documentación de Microsoft sobre el uso de `validate-jwt` con `<openid-config>` ([Referencia de política de Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)).

Tras la validación, APIM reenviará la solicitud (incluyendo el encabezado `Authorization` original) al backend. Dado que la aplicación Spring también es un servidor de recursos, revalidará el token, pero APIM ya ha garantizado su validez. (Para desarrollo, puede confiar en la comprobación de APIM y desactivar las validaciones adicionales en la app si lo desea, pero es más seguro mantener ambas.)

## Configuración de ejemplo

| Configuración       | Valor de ejemplo                                                  | Notas                                      |
|--------------------|------------------------------------------------------------------|--------------------------------------------|
| **Emisor**          | `https://my-mcp-app.eastus.azurecontainerapps.io`                | URL de su Container App (URI base)         |
| **Endpoint de token** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`   | Endpoint de token por defecto de Spring ([Modelo de Configuración :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **Endpoint JWKS**    | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`    | Endpoint por defecto del conjunto JWK ([Modelo de Configuración :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **Config. OpenID**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | Documento de descubrimiento OIDC (autogenerado)    |
| **Audiencia APIM**  | `mcp-client`                                                     | ID del cliente OAuth o nombre del recurso API |
| **Política APIM**   | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` usa esta URL ([Referencia de política de Azure API Management - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## Errores comunes

- **HTTPS/TLS:** La pasarela APIM requiere que el endpoint OpenID/JWKS use HTTPS con un certificado válido. Por defecto, Azure Container Apps proporciona un certificado TLS confiable para el dominio gestionado por Azure ([Nombres de dominio personalizados y certificados gestionados gratuitos en Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Si usa un dominio personalizado, asegúrese de vincular un certificado (puede usar la función de certificado gestionado gratuito de Azure) ([Nombres de dominio personalizados y certificados gestionados gratuitos en Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)). Si APIM no puede confiar en el certificado del endpoint, `<validate-jwt>` no podrá obtener los metadatos.  

- **Accesibilidad del endpoint:** Asegúrese de que los endpoints de la aplicación Spring sean accesibles desde APIM. Usar `--ingress external` (o habilitar ingreso en el portal) es lo más sencillo. Si eligió un entorno interno o vinculado a vNet, APIM (que por defecto es público) podría no alcanzarlo a menos que esté en la misma VNet. En un entorno de prueba, prefiera ingreso público para que APIM pueda llamar a las URLs `.well-known` y `/jwks`. 

- **Descubrimiento OpenID habilitado:** Por defecto, Spring Authorization Server **no expone** `/.well-known/openid-configuration` a menos que OIDC esté habilitado. Asegúrese de incluir `.oidc(Customizer.withDefaults())` en su configuración de seguridad (ver arriba) para que el endpoint de configuración del proveedor esté activo ([Modelo de Configuración :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)). De lo contrario, la llamada `<openid-config>` de APIM devolverá un 404.

- **Afirmación Audience:** El comportamiento por defecto de Spring es establecer la afirmación `aud` al ID del cliente. Si la validación `<audience>` de APIM falla, podría necesitar personalizar el token (como se muestra arriba) o ajustar la política de APIM. Asegúrese de que la audiencia en su JWT coincida con lo que configura en `<audience>`. 

- **Análisis del JSON de metadatos:** El JSON de configuración OpenID debe ser válido. La configuración por defecto de Spring emitirá un documento estándar OIDC. Verifique que contenga el `issuer` y `jwks_uri` correctos. Si aloja Spring detrás de un proxy o ruta basada en ruta, revise bien las URLs en estos metadatos. APIM usará estos valores tal cual. 

- **Orden de políticas:** En la política de APIM, coloque `<validate-jwt>` **antes** de cualquier enrutamiento al backend. De lo contrario, las llamadas podrían llegar a su aplicación sin un token válido. También asegúrese de que `<validate-jwt>` aparezca inmediatamente bajo `<inbound>` (no anidado dentro de otra condición) para que APIM lo aplique.

Siguiendo los pasos anteriores, puede ejecutar su servidor Spring AI MCP en Azure Container Apps y hacer que Azure API Management valide los JWT OAuth2 entrantes con una política mínima. Los puntos clave son: exponer los endpoints de Spring Auth públicamente con TLS, habilitar el descubrimiento OIDC y apuntar el `validate-jwt` de APIM a la URL de configuración OpenID (para que obtenga el JWKS automáticamente). Esta configuración es adecuada para un entorno de desarrollo/pruebas; para producción, considere una gestión adecuada de secretos, duración de tokens y rotación de claves en JWKS según sea necesario. 


**Referencias:** Consulte la documentación de Spring Authorization Server para los endpoints predeterminados ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) y la configuración de OIDC ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); consulte la documentación de Microsoft APIM para ejemplos de `validate-jwt` ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); y la documentación de Azure Container Apps para el despliegue y certificados ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->