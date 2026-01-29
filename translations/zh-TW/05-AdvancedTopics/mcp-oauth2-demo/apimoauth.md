# 將 Spring AI MCP 應用程式部署到 Azure Container Apps

 ([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2)) *圖示：使用 Spring Authorization Server 保護的 Spring AI MCP 伺服器。伺服器向客戶端發行存取權杖，並在收到請求時驗證它們（來源：Spring 部落格）([Securing Spring AI MCP servers with OAuth2](https://spring.io/blog/2025/04/02/mcp-server-oauth2#:~:text=,server%20with%20the%20MCP%20inspector)).* 要部署 Spring MCP 伺服器，請將其建置為容器，並使用帶有外部入口的 Azure Container Apps。例如，使用 Azure CLI 可以執行：

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

這會建立一個公開可存取且啟用 HTTPS 的 Container App（Azure 會為預設的 `*.azurecontainerapps.io` 網域發行免費的 TLS 憑證 ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。指令輸出會包含應用程式的完整網域名稱（FQDN），例如 `my-mcp-app.eastus.azurecontainerapps.io`，這將成為 **issuer URL** 的基底。請確保啟用 HTTP 入口（如上所述），以便 APIM 能夠存取應用程式。在測試/開發環境中，使用 `--ingress external` 選項（或依照 [Microsoft 文件](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) 綁定帶 TLS 的自訂網域 ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))）。將任何敏感屬性（例如 OAuth 用戶端密鑰）儲存在 Container Apps 的 secrets 或 Azure Key Vault，並將它們映射為容器的環境變數。

## 配置 Spring Authorization Server

在你的 Spring Boot 應用程式程式碼中，加入 Spring Authorization Server 和 Resource Server 的啟動器。配置一個 `RegisteredClient`（用於開發/測試環境的 `client_credentials` 授權類型）以及 JWT 金鑰來源。例如，在 `application.properties` 中可以設定：

```properties
# OAuth2 client (for testing token issuance)
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-id=mcp-client
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-secret={noop}secret
spring.security.oauth2.authorizationserver.client.oidc-client.registration.authorization-grant-types=client_credentials
spring.security.oauth2.authorizationserver.client.oidc-client.registration.client-authentication-methods=client_secret_basic
```

透過定義安全過濾鏈來啟用 Authorization Server 和 Resource Server。例如：

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

此設定會公開預設的 OAuth2 端點：`/oauth2/token` 用於取得權杖，`/oauth2/jwks` 用於 JSON Web Key Set。（Spring 的 `AuthorizationServerSettings` 預設會將 `/oauth2/token` 和 `/oauth2/jwks` 映射好 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))。）伺服器會發行由上述 RSA 金鑰簽署的 JWT 存取權杖，並在 `https://<your-app>:/oauth2/jwks` 公開其公鑰。

**啟用 OpenID Connect 探索：** 為了讓 APIM 自動取得 issuer 和 JWKS，請在安全性設定中加入 `.oidc(Customizer.withDefaults())` 以啟用 OIDC 提供者設定端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。例如：

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– enables /.well-known/openid-configuration
```

這會公開 `/.well-known/openid-configuration`，APIM 可用此取得元資料。最後，你可能想自訂 JWT 的 **audience** 聲明，以通過 APIM 的 `<audiences>` 檢查。例如，加入一個權杖自訂器：

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // Set a custom audience (e.g. the client ID or API identifier)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

這確保權杖攜帶 `"aud": ["mcp-client"]`，與 APIM 預期的用戶端 ID 或範圍相符。

## 公開 Token 和 JWKS 端點

部署後，你的應用程式 **issuer URL** 將是 `https://<app-fqdn>`，例如 `https://my-mcp-app.eastus.azurecontainerapps.io`。其 OAuth2 端點為：

- **Token 端點：** `https://<app-fqdn>/oauth2/token` – 用戶端在此取得權杖（client_credentials 流程）。
- **JWKS 端點：** `https://<app-fqdn>/oauth2/jwks` – 回傳 JWK 集合（APIM 用來取得簽署金鑰）。
- **OpenID 配置：** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC 探索 JSON（包含 `issuer`、`token_endpoint`、`jwks_uri` 等）。

APIM 會指向 **OpenID 配置 URL**，從中發現 `jwks_uri`。例如，若你的 Container App FQDN 是 `my-mcp-app.eastus.azurecontainerapps.io`，則 APIM 的 `<openid-config url="...">` 應使用 `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`。（Spring 預設會將該元資料中的 `issuer` 設為相同的基底 URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))。）

## 配置 Azure API Management (`validate-jwt`)

在 Azure APIM 中，新增一個入站政策，使用 `<validate-jwt>` 來驗證傳入的 JWT 是否符合你的 Spring Authorization Server。簡單設定可使用 OpenID Connect 元資料 URL。範例政策片段：

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

此政策指示 APIM 從 Spring Auth Server 取得 OpenID 配置，抓取其 JWKS，並驗證每個權杖是否由受信任的金鑰簽署且擁有正確的 audience。（若省略 `<issuers>`，APIM 會自動使用元資料中的 `issuer` 聲明。）`<audience>` 應與權杖中的用戶端 ID 或 API 資源識別碼相符（上述範例中設定為 `"mcp-client"`）。這與 Microsoft 使用 `<openid-config>` 搭配 `validate-jwt` 的文件一致 ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))。

驗證通過後，APIM 會將請求（包含原始的 `Authorization` 標頭）轉發到後端。由於 Spring 應用程式同時是資源伺服器，它會再次驗證權杖，但 APIM 已先確保其有效性。（開發時，你可以只依賴 APIM 的檢查並在應用程式中停用額外檢查，但保留雙重檢查會更安全。）

## 範例設定

| 設定項目           | 範例值                                                             | 備註                                       |
|--------------------|--------------------------------------------------------------------|--------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                  | 你的 Container App 網址（基底 URI）        |
| **Token endpoint** | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`     | 預設 Spring 權杖端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS endpoint**  | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`      | 預設 JWK 集合端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID Config**  | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC 探索文件（自動產生）                    |
| **APIM audience**  | `mcp-client`                                                       | OAuth 用戶端 ID 或 API 資源名稱             |
| **APIM policy**    | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` 使用此 URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## 常見陷阱

- **HTTPS/TLS：** APIM 閘道要求 OpenID/JWKS 端點必須使用有效憑證的 HTTPS。Azure Container Apps 預設會為 Azure 管理的網域提供受信任的 TLS 憑證 ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。若使用自訂網域，務必綁定憑證（可使用 Azure 的免費管理憑證功能） ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。若 APIM 無法信任端點憑證，`<validate-jwt>` 將無法取得元資料。

- **端點可存取性：** 確保 Spring 應用程式的端點可由 APIM 存取。使用 `--ingress external`（或在入口網站啟用入口）是最簡單的方式。若選擇內部或 vNet 綁定環境，APIM（預設為公開）可能無法存取，除非放在相同的 VNet。測試環境建議使用公開入口，讓 APIM 能呼叫 `.well-known` 和 `/jwks` URL。

- **啟用 OpenID 探索：** Spring Authorization Server 預設 **不會公開** `/.well-known/openid-configuration`，除非啟用 OIDC。請務必在安全性設定中加入 `.oidc(Customizer.withDefaults())`（見上文），以啟用提供者設定端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。否則 APIM 的 `<openid-config>` 呼叫會回傳 404。

- **Audience 聲明：** Spring 預設會將 `aud` 聲明設為用戶端 ID。若 APIM 的 `<audience>` 檢查失敗，可能需要自訂權杖（如上所示）或調整 APIM 政策。確保 JWT 中的 audience 與 `<audience>` 設定相符。

- **JSON 元資料解析：** OpenID 配置的 JSON 必須有效。Spring 預設會輸出標準的 OIDC 元資料文件。請確認其中包含正確的 `issuer` 和 `jwks_uri`。若 Spring 部署在代理或路徑路由後方，請再次確認元資料中的 URL。APIM 會直接使用這些值。

- **政策順序：** 在 APIM 政策中，請將 `<validate-jwt>` 放在任何路由到後端之前。否則請求可能在未驗證權杖的情況下到達應用程式。並確保 `<validate-jwt>` 直接置於 `<inbound>` 下（不要巢狀在其他條件中），以確保 APIM 正確套用。

依照上述步驟，你可以在 Azure Container Apps 上執行 Spring AI MCP 伺服器，並使用 Azure API Management 以最簡單的政策驗證傳入的 OAuth2 JWT。重點是：公開 Spring Auth 端點並啟用 TLS，啟用 OIDC 探索，並將 APIM 的 `validate-jwt` 指向 OpenID 配置 URL（以自動取得 JWKS）。此設定適合開發/測試環境；生產環境則需考慮妥善的密鑰管理、權杖有效期限及 JWKS 金鑰輪替等。
**References:** 請參考 Spring Authorization Server 文件了解預設端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) 及 OIDC 配置 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))；參考 Microsoft APIM 文件中的 `validate-jwt` 範例 ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))；以及 Azure Container Apps 文件中關於部署與憑證的說明 ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。