# 將 Spring AI MCP 應用程式部署到 Azure Container Apps

> [!WARNING]
> 此組合授權/資源伺服器僅供學習及開發/測試使用。生產系統應使用專用的身份提供者、
> 永續簽署金鑰，以及儲存在管理式機密庫中的憑證。




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

這將建立一個具有 HTTPS 的公開可存取 Container App（Azure 為預設的 `*.azurecontainerapps.io` 網域免費發行 TLS 憑證（[Azure Container Apps 的自訂網域名稱和免費受管理憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)））。命令輸出會包含 App 的完全限定網域名稱（FQDN）（例如 `my-mcp-app.eastus.azurecontainerapps.io`），該網域成為 **issuer URL** 的基底。請確定啟用 HTTP 入口（如上所示），以便 APIM 可以存取該應用程式。測試/開發環境中使用 `--ingress external` 選項（或依照 [Microsoft 文件](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) 綁定帶 TLS 的自訂網域（[Azure Container Apps 的自訂網域名稱和免費受管理憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)））。將任何敏感屬性（例如 OAuth 用戶端密鑰）存放在 Container Apps 機密或 Azure Key Vault 中，並以環境變數映射到容器中。

## 設定 Spring Authorization Server

在您的 Spring Boot 應用程式程式碼中，包含 Spring Authorization Server 和 Resource Server Starter。設定一個 `RegisteredClient`（用於 dev/test 的 `client_credentials` 授權模式）及 JWT 金鑰來源。例如，在 `application.properties` 中您可以設定：

```properties
# OAuth2 client (for testing token issuance)
demo.oauth.client-id=${OAUTH_CLIENT_ID:mcp-client}
demo.oauth.client-secret=${OAUTH_CLIENT_SECRET}
```

透過定義安全性過濾鏈啟用授權伺服器和資源伺服器。例如：

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
            // 啟用資源伺服器（驗證入站請求中的 JWT）
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // 停用 CSRF（MCP 伺服器不是基於瀏覽器）
            .csrf(csrf -> csrf.disable())
            // 允許 CORS 給客戶端示範工具
            .cors(withDefaults());
        return http.build();
    }

    // 定義一個記憶體中客戶端（RegisteredClient）與 JWK 來源：
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
        // 產生 RSA 金鑰（開發/測試用，啟動時重新產生）
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

此設定將開放預設的 OAuth2 端點：用於取得權杖的 `/oauth2/token` 與用於 JSON Web Key Set 的 `/oauth2/jwks`。（Spring 的 `AuthorizationServerSettings` 預設會對應到 `/oauth2/token` 和 `/oauth2/jwks` ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))。）伺服器將發布由上述 RSA 金鑰簽署的 JWT 存取權杖，並在 `https://<your-app>:/oauth2/jwks` 發布其公開金鑰。

**啟用 OpenID Connect 探索：** 為了讓 APIM 自動擷取發行者及 JWKS，請透過在安全性設定中加入 `.oidc(Customizer.withDefaults())` 來啟用 OIDC 提供者設定端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。例如：

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– 啟用 /.well-known/openid-configuration
```

這會公開 `/.well-known/openid-configuration`，APIM 可利用該檔案取得元資料。最後，您可能需要自訂 JWT 的 **audience** 聲明，以通過 APIM 的 `<audiences>` 檢查。例如，加入權杖自訂器：

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // 設定自訂受眾 (例如客戶編號或 API 識別碼)
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

這確保權杖攜帶 `"aud": ["mcp-client"]`，與 APIM 預期的用戶端 ID 或範圍吻合。

## 開放 Token 及 JWKS 端點

部署後，您的應用程式 **issuer URL** 為 `https://<app-fqdn>`，例如 `https://my-mcp-app.eastus.azurecontainerapps.io`。其 OAuth2 端點如下：

- **Token 端點：** `https://<app-fqdn>/oauth2/token` – 用戶端於此取得權杖（client_credentials 流程）。
- **JWKS 端點：** `https://<app-fqdn>/oauth2/jwks` – 傳回 JWK 集合（APIM 用於取得簽署金鑰）。
- **OpenID 設定：** `https://<app-fqdn>/.well-known/openid-configuration` – OIDC 探索 JSON（包含 `issuer`、`token_endpoint`、`jwks_uri` 等）。

APIM 將指向 **OpenID 設定 URL**，藉此發現 `jwks_uri`。例如，如果您的 Container App FQDN 是 `my-mcp-app.eastus.azurecontainerapps.io`，則 APIM 的 `<openid-config url="...">` 應使用 `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`。（Spring 預設會將該元資料中的 `issuer` 設為相同基底 URL ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))。）

## 設定 Azure API Management（`validate-jwt`）

在 Azure APIM 中，新增一個 inbound 策略，使用 `<validate-jwt>` 來驗證傳入的 JWT 是否符合您的 Spring Authorization Server。簡易設定中，可以使用 OpenID Connect 元資料 URL。範例策略片段：

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

此策略指示 APIM 從 Spring Auth Server 擷取 OpenID 設定，取得 JWKS，驗證每個權杖是否由信任金鑰簽署，並擁有正確的 audience。（若省略 `<issuers>`，APIM 將自動使用元資料中的 `issuer` 聲明。）`<audience>` 應與權杖中的用戶端 ID 或 API 資源識別碼匹配（上述範例設定為 `"mcp-client"`）。這與 Microsoft 對於使用 `<openid-config>` 的 `validate-jwt` 文件一致 ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))。

驗證之後，APIM 將轉送請求（包括原始 `Authorization` 標頭）至後端。因為 Spring 應用同時也是資源伺服器，它會再次驗證權杖，但 APIM 已先確保其有效。（開發時，您可仰賴 APIM 的檢查並視需求停用應用的額外檢查，但安全起見建議兩者都保留。）

## 範例設定

| 設定              | 範例值                                                             | 註解                                      |
|--------------------|----------------------------------------------------------------------|--------------------------------------------|
| **Issuer**        | `https://my-mcp-app.eastus.azurecontainerapps.io`                    | 您的 Container App 網址（基底 URI）       |
| **Token 端點**    | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`       | 預設 Spring 權杖端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))  |
| **JWKS 端點**     | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`        | 預設 JWK 集合端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))    |
| **OpenID 設定**   | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC 探索文件（自動產生）                  |
| **APIM 受眾**     | `mcp-client`                                                         | OAuth 用戶端 ID 或 API 資源名稱            |
| **APIM 策略**     | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` 使用此 URL ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## 常見陷阱

- **HTTPS/TLS：** APIM 閘道要求 OpenID/JWKS 端點為 HTTPS 且擁有有效憑證。Azure Container Apps 預設會為 Azure 管理的網域提供受信任的 TLS 憑證（[Azure Container Apps 的自訂網域名稱和免費受管理憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。如果您使用自訂網域，請確保綁定憑證（可使用 Azure 免費管理憑證功能）（[Azure Container Apps 的自訂網域名稱和免費受管理憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)）。若 APIM 無法信任端點的憑證，`<validate-jwt>` 會無法取得元資料。

- **端點可存取性：** 確保 Spring 應用的端點能從 APIM 存取。使用 `--ingress external`（或在入口網站開啟入口）是最簡單的方式。如果您選擇內部或 vNet 綁定環境，APIM（預設為公開）可能無法存取，除非置於相同 vNet。測試環境建議使用公開入口，讓 APIM 能呼叫 `.well-known` 與 `/jwks` URL。

- **開啟 OpenID 探索功能：** Spring Authorization Server 預設 <strong>不會公開</strong> `/.well-known/openid-configuration`，除非啟用 OIDC。請確保在安全性設定中加入 `.oidc(Customizer.withDefaults())`（如上）以啟用提供者設定端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。否則 APIM 的 `<openid-config>` 請求會回傳 404。

- **Audience 聲明：** Spring 預設是將 `aud` 聲明設為用戶端 ID。若 APIM 的 `<audience>` 檢查失敗，您可能需要自訂權杖（如上所示）或調整 APIM 策略。確保 JWT 中的受眾與 `<audience>` 中的設定相符。

- **JSON 元資料解析：** OpenID 配置 JSON 必須有效。Spring 預設會發出標準 OIDC 元資料文件。請確認它含有正確的 `issuer` 與 `jwks_uri`。若您將 Spring 放在代理或基於路徑的路由後方，請再次確認此元資料中的 URL。APIM 會直接使用這些值。

- **策略順序：** 在 APIM 策略中，將 `<validate-jwt>` <strong>放在</strong> 往後端路由之前。否則，請求可能在沒有有效權杖的狀況下就到達您的應用程式。並確保 `<validate-jwt>` 緊接在 `<inbound>` 之下（不要巢狀於其他條件內），讓 APIM 正確套用該策略。

遵循上述步驟，您即可在 Azure Container Apps 運行 Spring AI MCP 伺服器，並使用 Azure API Management 以最簡政策驗證進入的 OAuth2 JWT。重點包括：公開 Spring 授權端點並啟用 TLS、開啟 OIDC 探索，以及將 APIM 的 `validate-jwt` 指向 OpenID 配置 URL（讓它能自動取得 JWKS）。此配置適用於開發/測試環境；在生產環境中，請考慮妥善的機密管理、權杖有效期限及 JWKS 私鑰輪替需求。


**參考資料：** 請參閱 Spring Authorization Server 文件中的預設端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) 及 OIDC 配置 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); 請參閱 Microsoft APIM 文件中的 `validate-jwt` 範例 ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); 以及 Azure Container Apps 文件中有關部署及憑證的說明 ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->