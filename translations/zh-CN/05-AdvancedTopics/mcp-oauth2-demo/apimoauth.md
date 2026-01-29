# 将 Spring AI MCP 应用部署到 Azure Container Apps

([使用 OAuth2 保护 Spring AI MCP 服务器](https://spring.io/blog/2025/04/02/mcp-server-oauth2))  
*图示：使用 Spring Authorization Server 保护的 Spring AI MCP 服务器。服务器向客户端颁发访问令牌，并在接收请求时验证令牌（来源：Spring 博客）([使用 OAuth2 保护 Spring AI MCP 服务器](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector))。*  
要部署 Spring MCP 服务器，请将其构建为容器，并使用带有外部入口的 Azure Container Apps。例如，使用 Azure CLI 可以运行：

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

这将创建一个启用 HTTPS 的公开访问 Container App（Azure 会为默认的 `*.azurecontainerapps.io` 域颁发免费的 TLS 证书（[Azure Container Apps 中的自定义域名和免费托管证书 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)））。命令输出中包含应用的 FQDN（例如 `my-mcp-app.eastus.azurecontainerapps.io`），它将作为**发行者 URL** 的基础。确保启用了 HTTP 入口（如上所述），以便 APIM 能够访问该应用。在测试/开发环境中，使用 `--ingress external` 选项（或者根据 [Microsoft 文档](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) 绑定带 TLS 的自定义域名（[Azure Container Apps 中的自定义域名和免费托管证书 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)））。将任何敏感属性（如 OAuth 客户端密钥）存储在 Container Apps 的 secrets 或 Azure Key Vault 中，并映射为容器的环境变量。

## 配置 Spring Authorization Server

在你的 Spring Boot 应用代码中，包含 Spring Authorization Server 和 Resource Server 的启动器。配置一个 `RegisteredClient`（用于开发/测试环境中的 `client_credentials` 授权类型）和 JWT 密钥源。例如，在 `application.properties` 中可以设置：

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

通过定义安全过滤链启用 Authorization Server 和 Resource Server。例如：

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

此配置将暴露默认的 OAuth2 端点：`/oauth2/token` 用于获取令牌，`/oauth2/jwks` 用于 JSON Web Key Set。（默认情况下，Spring 的 `AuthorizationServerSettings` 会映射 `/oauth2/token` 和 `/oauth2/jwks`（[配置模型 :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)）。服务器将颁发由上述 RSA 密钥签名的 JWT 访问令牌，并在 `https://<your-app>:/oauth2/jwks` 发布其公钥。

**启用 OpenID Connect 发现：** 为了让 APIM 自动获取发行者和 JWKS，需通过在安全配置中添加 `.oidc(Customizer.withDefaults())` 来启用 OIDC 提供者配置端点（[配置模型 :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)）。例如：

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

这将暴露 `/.well-known/openid-configuration`，APIM 可用其获取元数据。最后，你可能需要自定义 JWT 的 **audience** 声明，以确保 APIM 的 `<audiences>` 校验通过。例如，添加一个令牌定制器：

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

这样令牌中会包含 `"aud": ["mcp-client"]`，与 APIM 期望的客户端 ID 或作用域匹配。

## 暴露令牌和 JWKS 端点

部署后，你的应用**发行者 URL** 将是 `https://<app-fqdn>`，例如 `https://my-mcp-app.eastus.azurecontainerapps.io`。其 OAuth2 端点包括：

- **令牌端点：** `https://<app-fqdn>/oauth2/token` – 客户端在此获取令牌（client_credentials 流程）。
- **JWKS 端点：** `https://<app-fqdn>/oauth2/jwks` – 返回 JWK 集（APIM 用于获取签名密钥）。
- **OpenID 配置：** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC 发现 JSON（包含 `issuer`、`token_endpoint`、`jwks_uri` 等）。

APIM 会指向**OpenID 配置 URL**，从中发现 `jwks_uri`。例如，如果你的 Container App FQDN 是 `my-mcp-app.eastus.azurecontainerapps.io`，则 APIM 的 `<openid-config url="...">` 应使用 `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`。（默认情况下，Spring 会将该元数据中的 `issuer` 设置为相同的基础 URL（[配置模型 :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)）。）

## 配置 Azure API Management (`validate-jwt`)

在 Azure APIM 中，添加一个入站策略，使用 `<validate-jwt>` 策略根据你的 Spring Authorization Server 验证传入的 JWT。简单配置可以使用 OpenID Connect 元数据 URL。示例策略片段：

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

该策略指示 APIM 从 Spring Auth Server 获取 OpenID 配置，检索其 JWKS，并验证每个令牌是否由受信任的密钥签名且具有正确的受众。（如果省略 `<issuers>`，APIM 会自动使用元数据中的 `issuer` 声明。）`<audience>` 应与令牌中的客户端 ID 或 API 资源标识符匹配（上例中设置为 `"mcp-client"`）。这与微软关于使用 `<openid-config>` 的 `validate-jwt` 文档一致（[Azure API Management 策略参考 - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)）。

验证通过后，APIM 会将请求（包括原始的 `Authorization` 头）转发到后端。由于 Spring 应用也是资源服务器，它会再次验证令牌，但 APIM 已经确保了令牌的有效性。（开发时，你可以只依赖 APIM 的校验并禁用应用中的额外校验，但保持双重校验更安全。）

## 示例设置

| 设置               | 示例值                                                             | 说明                                       |
|--------------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | 你的 Container App 的 URL（基础 URI）      |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | 默认 Spring 令牌端点（[配置模型 :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)） |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | 默认 JWK 集端点（[配置模型 :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)） |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC 发现文档（自动生成）                   |
| **APIM audience**  | `mcp-client`                                                       | OAuth 客户端 ID 或 API 资源名称             |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` 使用此 URL（[Azure API Management 策略参考 - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)） |

## 常见问题

- **HTTPS/TLS：** APIM 网关要求 OpenID/JWKS 端点必须是 HTTPS 且证书有效。默认情况下，Azure Container Apps 会为 Azure 托管域提供受信任的 TLS 证书（[Azure Container Apps 中的自定义域名和免费托管证书 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。如果使用自定义域名，务必绑定证书（可以使用 Azure 的免费托管证书功能）（[Azure Container Apps 中的自定义域名和免费托管证书 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。如果 APIM 无法信任端点证书，`<validate-jwt>` 将无法获取元数据。

- **端点可访问性：** 确保 Spring 应用的端点对 APIM 可达。使用 `--ingress external`（或在门户中启用入口）是最简单的方式。如果选择了内部或 vNet 绑定环境，APIM（默认是公共的）可能无法访问，除非它们在同一 VNet 中。测试环境建议使用公共入口，以便 APIM 能调用 `.well-known` 和 `/jwks` URL。

- **启用 OpenID 发现：** 默认情况下，Spring Authorization Server **不会暴露** `/.well-known/openid-configuration`，除非启用了 OIDC。确保在安全配置中包含 `.oidc(Customizer.withDefaults())`（见上文），以激活提供者配置端点（[配置模型 :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)）。否则 APIM 的 `<openid-config>` 调用会返回 404。

- **Audience 声明：** Spring 默认将 `aud` 声明设置为客户端 ID。如果 APIM 的 `<audience>` 校验失败，可能需要自定义令牌（如上所示）或调整 APIM 策略。确保 JWT 中的受众与 `<audience>` 配置匹配。

- **JSON 元数据解析：** OpenID 配置的 JSON 必须有效。Spring 默认配置会输出标准的 OIDC 元数据文档。请确认其中包含正确的 `issuer` 和 `jwks_uri`。如果 Spring 部署在代理或基于路径的路由后面，请仔细检查元数据中的 URL，APIM 会直接使用这些值。

- **策略顺序：** 在 APIM 策略中，确保 `<validate-jwt>` **位于** 任何路由到后端之前。否则，可能会有请求未经过有效令牌验证就到达应用。同时确保 `<validate-jwt>` 直接放在 `<inbound>` 下（不要嵌套在其他条件中），以保证 APIM 正确应用。

按照上述步骤，你可以在 Azure Container Apps 中运行 Spring AI MCP 服务器，并让 Azure API Management 使用最简策略验证传入的 OAuth2 JWT。关键点是：公开暴露带 TLS 的 Spring Auth 端点，启用 OIDC 发现，并将 APIM 的 `validate-jwt` 指向 OpenID 配置 URL（以便自动获取 JWKS）。此配置适合开发/测试环境；生产环境中请考虑妥善管理密钥、令牌生命周期及 JWKS 的密钥轮换。
**参考资料：** 请参阅 Spring Authorization Server 文档了解默认端点（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)）和 OIDC 配置（[Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)）；请参阅 Microsoft APIM 文档中的 `validate-jwt` 示例（[Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)）；以及 Azure Container Apps 文档中的部署和证书（[Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)）（[Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的原文应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。