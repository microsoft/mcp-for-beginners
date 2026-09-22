# 將 Spring AI MCP 應用程式部署到 Azure Container Apps

> [!WARNING]
> 此綜合授權/資源伺服器僅適用於學習及開發/測試用途。生產環境系統應使用專用的身份提供者、
> 持久的簽名金鑰，以及存放於受管理秘密庫的憑證。




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

這會建立一個公開可存取、啟用 HTTPS 的 Container App（Azure 會為預設的 `*.azurecontainerapps.io` 網域自動簽發免費 TLS 憑證 ([Azure Container Apps 的自訂網域名稱與免費托管憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))）。該命令的輸出會包含應用程式的完整限定網域名稱（FQDN），例如 `my-mcp-app.eastus.azurecontainerapps.io`，這將成為 **issuer URL** 的基礎。請確保啟用 HTTP 入口（如上所示），使 APIM 能存取該應用程式。在測試/開發環境中，請使用 `--ingress external` 選項（或者依照 [Microsoft 文件](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) 綁定自訂網域並啟用 TLS ([Azure Container Apps 的自訂網域名稱與免費托管憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))）。將任何敏感屬性（例如 OAuth 用戶端密鑰）存放在 Container Apps Secrets 或 Azure Key Vault 中，並映射為容器的環境變數。

## 配置 Spring Authorization Server

在您的 Spring Boot 應用程式代碼中，包含 Spring Authorization Server 和 Resource Server 的啟動器。配置一個 `RegisteredClient`（用於開發/測試時的 `client_credentials` 授權類型）及 JWT 金鑰來源。例如，在 `application.properties` 中您可能會設置：

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

透過定義安全性過濾鏈來啟用授權伺服器與資源伺服器。例如：

```java
@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Bean
    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        OAuth2AuthorizationServerConfigurer<HttpSecurity> authzServer = OAuth2AuthorizationServerConfigurer.authorizationServer();
        http
            .authorizeHttpRequests(auth -> auth.anyRequest().authenticated())
            // 啟用授權伺服器端點
            .apply(authzServer.and())
            // 啟用資源伺服器（驗證傳入請求的 JWT）
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // 禁用 CSRF（MCP 伺服器非基於瀏覽器）
            .csrf(csrf -> csrf.disable())
            // 允許客戶端示範工具的 CORS
            .cors(withDefaults());
        return http.build();
    }

    // 定義一個記憶體內的客戶端（RegisteredClient）和 JWK 資源：
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
        // 產生 RSA 金鑰（用於開發/測試，啟動時重新產生）
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

此配置將曝光預設的 OAuth2 端點：`/oauth2/token` 用於存取權杖發行，`/oauth2/jwks` 用於 JSON Web 金鑰集合。（Spring 預設會將 `/oauth2/token` 和 `/oauth2/jwks` 映射至 `AuthorizationServerSettings` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))）。伺服器將發行由上述 RSA 金鑰簽署的 JWT 存取權杖，並在 `https://<your-app>:/oauth2/jwks` 公開其公鑰。

**啟用 OpenID Connect 探索功能：** 要讓 APIM 自動擷取 issuer 與 JWKS，請在安全性配置中新增 `.oidc(Customizer.withDefaults())` 以啟用 OIDC 供應者設定端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。例如：

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– 啟用 /.well-known/openid-configuration
```

這會公開 `/.well-known/openid-configuration`，APIM 可用它來取得元資料。最後，您可能想自訂 JWT 的 **audience** 聲明，使 APIM 的 `<audiences>` 驗證能通過。例如，新增一個 token 自訂器：

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // 設定自訂受眾（例如客戶端 ID 或 API 識別碼）
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

這可確保權杖中包含 `"aud": ["mcp-client"]`，與 APIM 預期的用戶端 ID 或範圍相符。

## 暴露 Token 與 JWKS 端點

部署後，您的應用程式 **issuer URL** 將為 `https://<app-fqdn>`，例如 `https://my-mcp-app.eastus.azurecontainerapps.io`。其 OAuth2 端點為：

- **Token 端點：** `https://<app-fqdn>/oauth2/token` – 客戶端於此取得權杖（client_credentials 流程）。
- **JWKS 端點：** `https://<app-fqdn>/oauth2/jwks` – 傳回 JSON Web 金鑰集合（供 APIM 取得簽署金鑰）。
- **OpenID 配置：** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC 探索的 JSON 檔（包含 `issuer`、`token_endpoint`、`jwks_uri` 等）。

APIM 會指向 **OpenID 配置 URL**，並從該處取得 `jwks_uri`。舉例來說，若您的 Container App FQDN 是 `my-mcp-app.eastus.azurecontainerapps.io`，那麼 APIM 的 `<openid-config url="...">` 便應使用 `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`。（Spring 預設會將該元資料中的 `issuer` 設為相同的基底 URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))。）

## 配置 Azure API Management（`validate-jwt`）

在 Azure APIM 中，新增一個入口策略，使用 `<validate-jwt>` 政策來驗證來自您的 Spring Authorization Server 的 JWT。簡單設置可直接使用 OpenID Connect 元資料 URL。範例策略片段：

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

此策略指示 APIM 從 Spring 授權伺服器擷取 OpenID 配置，取得 JWKS，並驗證每個權杖是否由受信任的金鑰簽署且擁有正確的 audience。（若不指定 `<issuers>`，APIM 會自動使用元資料中的 `issuer` 聲明。）`<audience>` 應與權杖中的用戶端 ID 或 API 資源識別碼一致（以上範例中設定為 `"mcp-client"`）。此做法與 Microsoft 文件中使用帶 `<openid-config>` 的 `validate-jwt` 相符 ([Azure API 管理政策參考 - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))。

驗證通過後，APIM 將轉送請求（包含原始 `Authorization` 標頭）到後端。因為 Spring 應用程式同時是資源伺服器，也會重新驗證權杖，但 APIM 已確保其有效性。（開發時您可以只依賴 APIM 的檢查，如果需要可在應用程式禁用額外檢查，但保持兩者皆開啟會更安全。）

## 範例設定

| 設定               | 範例值                                                              | 備註                                       |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| <strong>發行者</strong>         | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | 您的 Container App 網址（基底 URI）          |
| **Token 端點**     | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | 預設 Spring Token 端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **JWKS 端點**      | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | 預設 JWK 集合端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **OpenID 配置**    | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC 探索文件（自動生成）                     |
| **APIM 受眾**      | `mcp-client`                                                         | OAuth 用戶端 ID 或 API 資源名稱               |
| **APIM 政策**      | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` 使用此 URL ([Azure API 管理政策參考 - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## 常見問題

- **HTTPS/TLS：** APIM 閘道要求 OpenID/JWKS 端點須為 HTTPS 且持有有效憑證。Azure Container Apps 預設會為 Azure 托管網域提供受信任的 TLS 憑證 ([Azure Container Apps 的自訂網域名稱與免費托管憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。若您使用自訂網域，務必綁定憑證（可利用 Azure 免費托管憑證功能） ([Azure Container Apps 的自訂網域名稱與免費托管憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。若 APIM 無法信任端點憑證，`<validate-jwt>` 會無法取得元資料。

- **端點存取性：** 確保 Spring 應用程式的端點能從 APIM 訪問。使用 `--ingress external`（或在入口網站啟用入口）是最簡單的方式。若您選擇內部或綁定虛擬網路的環境，APIM（預設為公用）可能無法連線，除非兩者在同一虛擬網路中。測試環境時，建議使用公開入口，讓 APIM 可調用 `.well-known` 與 `/jwks` URL。

- **啟用 OpenID 探索：** 預設情況下，Spring Authorization Server <strong>不會公開</strong> `/.well-known/openid-configuration`，除非啟用了 OIDC。務必在安全性配置中包含 `.oidc(Customizer.withDefaults())`（如上所示），以確保供應者設定端點啟用 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。否則 APIM 的 `<openid-config>` 請求將回傳 404。

- **Audience 聲明：** Spring 預設會將 `aud` 聲明設為用戶端 ID。若 APIM 的 `<audience>` 驗證失敗，您可能需要自訂權杖（如上所示）或調整 APIM 政策。確保 JWT 中的受眾與您配置的 `<audience>` 一致。

- **JSON 元資料解析：** OpenID 配置 JSON 必須是有效格式。Spring 預設配置會輸出標準的 OIDC 元資料文件。請確認它包含正確的 `issuer` 與 `jwks_uri`。若您將 Spring 放在代理或路徑路由後方，請再次檢查該元資料中的 URL。APIM 將直接使用這些值。

- **政策順序：** 在 APIM 政策中，請將 `<validate-jwt>` 放置在任何導向後端之前。否則呼叫可能在沒有有效權杖的情況下到達您的應用程式。也請確保 `<validate-jwt>` 直接位於 `<inbound>` 底下（不要巢狀於其他條件內），以便於 APIM 應用它。

按照上述步驟，您可以在 Azure Container Apps 中執行 Spring AI MCP 伺服器，並讓 Azure API Management 透過最簡策略驗證進來的 OAuth2 JWT。重點是：對外公開 Spring 授權端點並啟用 TLS、啟用 OIDC 探索，並讓 APIM 的 `validate-jwt` 指向 OpenID 配置 URL（以便自動獲取 JWKS）。此配置適合開發/測試環境；生產環境則需考量妥善的秘密管理、令牌生命週期與 JWKS 中金鑰的輪替。


**參考資料：** 請參見 Spring Authorization Server 文件中的預設端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) 與 OIDC 設定 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))；請參見 Microsoft APIM 文件中 `validate-jwt` 範例 ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))；以及 Azure Container Apps 文件中關於部署與憑證的說明 ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->