# 部署 Spring AI MCP 應用程式到 Azure Container Apps

> [!WARNING]
> 此組合授權/資源伺服器旨在學習及開發/測試用途。生產系統應使用專用的身份提供者、
> 持久化簽署金鑰，以及儲存在受控祕密庫中的憑證。




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

此指令會建立一個公開可存取且啟用 HTTPS 的 Container App（Azure 會為預設的 `*.azurecontainerapps.io` 網域頒發免費 TLS 憑證 ([在 Azure Container Apps 中自訂網域名稱與免費管理憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))）。指令輸出包含應用程式的完全限定網域名稱 (FQDN)（如 `my-mcp-app.eastus.azurecontainerapps.io`），該地址即為 **issuer URL** 基底。確保已啟用 HTTP ingress（如上），以便 APIM 可以連接到應用程式。在測試/開發環境中，使用 `--ingress external` 選項（或依照 [Microsoft 文件](https://learn.microsoft.com/azure/container-apps/custom-domains-managed-certificates) 綁定帶 TLS 的自訂網域 ([在 Azure Container Apps 中自訂網域名稱與免費管理憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))）。將任何敏感屬性（如 OAuth 用戶端密鑰）存放在 Container Apps 秘密或 Azure Key Vault 中，並映射到容器內作為環境變數。

## 配置 Spring 授權伺服器

在您的 Spring Boot 應用程式代碼中，包含 Spring 授權伺服器與資源伺服器啟動器。配置一個 `RegisteredClient`（用於開發/測試中的 `client_credentials` 授權）及 JWT 金鑰來源。例如，在 `application.properties` 中設定：

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
            // 啟用資源伺服器（驗證傳入請求的 JWT）
            .oauth2ResourceServer(oauth2 -> oauth2.jwt(withDefaults()))
            // 禁用 CSRF（MCP 伺服器非瀏覽器基礎）
            .csrf(csrf -> csrf.disable())
            // 允許 CORS 給客戶端示範工具
            .cors(withDefaults());
        return http.build();
    }

    // 定義一個記憶體內客戶端（RegisteredClient）和 JWK 來源：
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
        // 產生 RSA 金鑰（開發／測試用，啟動時重新產生）
        RSAKey rsaKey = new RSAKeyGenerator(2048).keyID("1").generate();
        JWKSet jwkSet = new JWKSet(rsaKey);
        return (selector, context) -> selector.select(jwkSet);
    }
}
```

此設定會公布預設的 OAuth2 端點：用於取得令牌的 `/oauth2/token` 以及用於 JSON Web Key Set 的 `/oauth2/jwks`。（Spring 的 `AuthorizationServerSettings` 預設將 `/oauth2/token` 和 `/oauth2/jwks` 映射於此 ([配置模型 :: Spring 授權伺服器](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))。）伺服器將簽署 RSA 金鑰下的 JWT 存取令牌，並在 `https://<your-app>:/oauth2/jwks` 發佈公鑰。

**啟用 OpenID Connect 探索功能：** 為了讓 APIM 自動取得 issuer 與 JWKS，可在安全配置中新增 `.oidc(Customizer.withDefaults())` 啟用 OIDC 提供者設定端點 ([配置模型 :: Spring 授權伺服器](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。例如：

```java
http
  .apply(authzServer.and())
  .securityMatcher(authzServer.getEndpointsMatcher())
  .with(authzServer, authz -> authz
      .oidc(Customizer.withDefaults()));  // <– 啟用 /.well-known/openid-configuration
```

此設定會公開 `/.well-known/openid-configuration`，APIM 可使用之作為元資料來源。最後，您可能想自訂 JWT 的 **audience** 聲明，以便通過 APIM 的 `<audiences>` 檢查。例如，新增一個令牌自訂器：

```java
@Bean
public OAuth2TokenCustomizer<OAuth2TokenClaimsContext> tokenCustomizer() {
    return context -> {
        // 設定自訂受眾（例如客戶編號或 API 識別碼）
        context.getClaims().audience(Collections.singletonList("mcp-client"));
    };
}
```

這確保令牌攜帶 `"aud": ["mcp-client"]`，與 APIM 預期的用戶端 ID 或作用域相符。

## 公開令牌和 JWKS 端點

部署後，您的應用程式 **issuer URL** 將是 `https://<app-fqdn>`，例如 `https://my-mcp-app.eastus.azurecontainerapps.io`。其 OAuth2 端點有：

- **令牌端點：** `https://<app-fqdn>/oauth2/token` — 用戶端在此取得令牌（client_credentials 流程）。
- **JWKS 端點：** `https://<app-fqdn>/oauth2/jwks` — 傳回 JWK 集合（APIM 用於取得簽署金鑰）。
- **OpenID 配置：** `https://<app-fqdn>/.well-known/openid-configuration` — OIDC 探索 JSON（包含 `issuer`、`token_endpoint`、`jwks_uri` 等）。

APIM 將指向 **OpenID 配置 URL**，從該處發掘 `jwks_uri`。例如，若您的 Container App FQDN 為 `my-mcp-app.eastus.azurecontainerapps.io`，則 APIM 的 `<openid-config url="...">` 應為 `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration`。（Spring 預設會將該元資料中的 `issuer` 設為相同的基本 URL ([配置模型 :: Spring 授權伺服器](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))。）

## 配置 Azure API 管理（`validate-jwt`）

在 Azure APIM 中，新增入站政策以使用 `<validate-jwt>` 政策檢查傳入的 JWT 是否符合您的 Spring 授權伺服器。簡易設定可使用 OpenID Connect 元資料 URL。範例政策片段：

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

此策略指示 APIM 從 Spring 授權伺服器擷取 OpenID 配置，取得其 JWKS，並驗證每個令牌是否由可信任金鑰簽署且具備正確的受眾。（若省略 `<issuers>`，APIM 會自動使用元資料中的 `issuer` 聲明。）`<audience>` 應與您在令牌中設定的用戶端 ID 或 API 資源識別碼相符（上述範例設為 `"mcp-client"`）。此用法與 Microsoft 關於使用 `<openid-config>` 的 `validate-jwt` 文件一致 ([Azure API 管理政策參考 - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation))。

驗證後，APIM 將轉送請求（含原始 `Authorization` 標頭）到後端。因 Spring 應用同時為資源伺服器，會對令牌再次驗證，但 APIM 已確保令牌有效。（開發時，您可僅依賴 APIM 的檢查並視情況關閉應用的額外檢查，但保持雙重檢查較為安全。）

## 範例設定

| 設定               | 範例值                                                             | 備註                                       |
|-------------------|-------------------------------------------------------------------|------------------------------------------|
| **Issuer**         | `https://my-mcp-app.eastus.azurecontainerapps.io`                 | 您的 Container App URL（基底 URI）          |
| <strong>令牌端點</strong>       | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/token`    | 預設 Spring 令牌端點 ([配置模型 :: Spring 授權伺服器](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) |
| **JWKS 端點**      | `https://my-mcp-app.eastus.azurecontainerapps.io/oauth2/jwks`     | 預設 JWK Set 端點 ([配置模型 :: Spring 授權伺服器](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize))   |
| **OpenID 配置**    | `https://my-mcp-app.eastus.azurecontainerapps.io/.well-known/openid-configuration` | OIDC 探索文件（自動生成）                    |
| **APIM 受眾**      | `mcp-client`                                                      | OAuth 用戶端 ID 或 API 資源名稱              |
| **APIM 政策**      | `<openid-config url="https://.../.well-known/openid-configuration" />` | `<validate-jwt>` 使用此 URL ([Azure API 管理政策參考 - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)) |

## 常見陷阱

- **HTTPS/TLS：** APIM 閘道要求 OpenID/JWKS 端點必須是使用有效憑證的 HTTPS。Azure Container Apps 預設會為 Azure 管理域提供受信任的 TLS 憑證 ([在 Azure Container Apps 中自訂網域名稱與免費管理憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。若使用自訂網域，務必綁定憑證（可使用 Azure 免費管理憑證功能）([在 Azure Container Apps 中自訂網域名稱與免費管理憑證 | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements))。若 APIM 無法信任端點的憑證， `<validate-jwt>` 將無法擷取元資料。

- **端點可存取性：** 確保 Spring 應用端點從 APIM 可達。使用 `--ingress external`（或在入口網站中啟用入口）是最簡單的方法。若選擇內部或 vNet 綁定環境，APIM（預設為公開）可能無法存取，除非與其位於同一 VNet。測試環境建議使用公開入口，方便 APIM 呼叫 `.well-known` 與 `/jwks` URL。

- **啟用 OpenID 探索：** Spring 授權伺服器預設<strong>不公開</strong> `/.well-known/openid-configuration`，除非啟用 OIDC。請務必在安全配置中包含 `.oidc(Customizer.withDefaults())`（見上文），使提供者配置端點生效 ([配置模型 :: Spring 授權伺服器](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build))。否則 APIM 的 `<openid-config>` 呼叫會回傳 404。

- **受眾聲明：** Spring 的預設行為是將 `aud` 聲明設為用戶端 ID。若 APIM 的 `<audience>` 檢查失敗，您可能需要自訂令牌（如上所示）或調整 APIM 政策。確保 JWT 中的受眾與您在 `<audience>` 中設定的一致。

- **JSON 元資料解析：** OpenID 配置 JSON 必須有效。Spring 預設會發出標準的 OIDC 元資料文件。請確認其中含有正確的 `issuer` 和 `jwks_uri`。若您將 Spring 放在代理或路由路徑後方，請務必再次檢查此元資料中的 URL。APIM 會照原樣使用這些值。

- **政策排序：** 在 APIM 政策中，請將 `<validate-jwt>` 放在任何後端路由之前。否則，有效令牌的請求可能無法正確檢查即達應用程式。且確保 `<validate-jwt>` 直接置於 `<inbound>` 下方（非巢狀於其他條件內），以便 APIM 正確套用。

依循上述步驟，您即可在 Azure Container Apps 運行 Spring AI MCP 伺服器，並使用 Azure API 管理以最低限度政策驗證傳入的 OAuth2 JWT。關鍵點為：公開帶 TLS 的 Spring 授權端點、啟用 OIDC 探索，並指向 APIM 的 `validate-jwt` 至 OpenID 配置 URL（以自動擷取 JWKS）。此設定適用於開發/測試環境；生產環境則應考慮適當的祕密管理、令牌壽命與 JWKS 金鑰輪替。


**參考資料：** 請參閱 Spring Authorization Server 文件以了解預設端點 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=public%20static%20Builder%20builder%28%29%20,oauth2%2Fauthorize)) 及 OIDC 配置 ([Configuration Model :: Spring Authorization Server](https://docs.spring.io/spring-authorization-server/reference/configuration-model.html#:~:text=.securityMatcher%28authorizationServerConfigurer.getEndpointsMatcher%28%29%29%20.with%28authorizationServerConfigurer%2C%20%28authorizationServer%29%20,%29%3B%20return%20http.build)); 請參閱 Microsoft APIM 文件了解 `validate-jwt` 範例 ([Azure API Management policy reference - validate-jwt | Microsoft Learn](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy#:~:text=Microsoft%20Entra%20ID%20single%20tenant,token%20validation)); 以及 Azure Container Apps 文件了解部署與證書 ([Deploy Java Spring Boot apps to Azure Container Apps - Java on Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/developer/java/identity/deploy-spring-boot-to-azure-container-apps#:~:text=Now%20you%20can%20deploy%20your,CLI%20command)) ([Custom domain names and free managed certificates in Azure Container Apps | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/custom-domains-managed-certificates#:~:text=Free%20certificate%20requirements)).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->