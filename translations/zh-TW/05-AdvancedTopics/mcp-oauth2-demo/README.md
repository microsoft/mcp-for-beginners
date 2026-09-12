# MCP OAuth2 示範

> [!WARNING]
> 這是一個本地學習範例，非生產授權服務。它使用記憶體中的用戶端並於啟動時產生新的簽章金鑰。切勿使用共享的、預設的或源代碼控制的用戶端密鑰進行部署。
> 
> 

## 介紹

OAuth2 是業界標準的授權協議，能在不共享憑證的情況下安全存取資源。在 MCP（模型上下文協議）實作中，OAuth2 提供穩健的方式來驗證與授權用戶端（例如 AI 代理）存取 MCP 伺服器及其工具。

本課程示範如何使用 Spring Boot 為 MCP 伺服器實作 OAuth2 驗證，這是企業及生產環境部署的常見模式。

## 學習目標

課程結束時，您將能：
- 了解 OAuth2 如何整合 MCP 伺服器
- 實作 Spring 授權伺服器以發行 token
- 使用基於 JWT 的認證保護 MCP 端點
- 配置用戶端憑證流程以實現機器對機器通訊

## 前置條件

- 具備基本的 Java 與 Spring Boot 知識
- 熟悉先前模組中的 MCP 概念
- 已安裝 Maven 或 Gradle

---

## 專案概覽

此專案是一個 **最小化 Spring Boot 應用程式**，同時擔任：

* **Spring 授權伺服器**（透過 `client_credentials` 流程簽發 JWT 存取權杖），以及  
* <strong>資源伺服器</strong>（保護自身的 `/hello` 端點）。

它模擬 [Spring 部落格文章 (2025年4月2日)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) 中展示的設置。

---

## 快速開始（本地）

```bash
# 使用唯一的本地值，並盡可能將其排除在 shell 歷史之外。
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# 取得一個令牌
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# 呼叫受保護的端點
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## 測試 OAuth2 設定

您可以依照以下步驟測試 OAuth2 安全設定：

### 1. 驗證伺服器是否運行且已保護

```bash
# 這應該回傳 401 未經授權，確認 OAuth2 安全性已啟用
curl -v http://localhost:8081/
```

### 2. 使用用戶端憑證取得存取權杖

```bash
# 獲取並提取完整的 token 響應
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# 或僅提取 token（需要 jq）
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

在 PowerShell 中，執行 Maven 前請設定本地密鑰：

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. 使用權杖存取受保護端點

```bash
# 使用已保存的令牌
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# 或直接使用令牌值
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

若回應成功並包含 "Hello from MCP OAuth2 Demo!"，表示 OAuth2 設定正常運作。

---

## 容器建置

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## 生產安全性

對於生產環境部署，請使用專用的身分識別提供者，而非此內嵌式示範授權伺服器。應將憑證存於管理式密鑰庫，定期輪替，使用持續的簽章金鑰，限制作用範圍，並設定明確的發行者。切勿將用戶端密鑰置於源代碼、容器映像、部署清單或命令輸出中。

對於 Azure Container Apps，請將該值存為以 Key Vault 支持的 Container Apps 秘密，然後只通過 `OAUTH_CLIENT_SECRET` 環境變數暴露秘密參考。







---

## 部署至 **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

入口的 FQDN 將成為您的 <strong>發行者</strong> (`https://<fqdn>`)。  
Azure 自動提供受信任的 TLS 證書給 `*.azurecontainerapps.io`。

---

## 整合 **Azure API 管理**

將此入站政策加入您的 API：

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

APIM 將會取得 JWKS 並驗證每一個請求。

---

## 後續步驟

- [5.4 根上下文](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->