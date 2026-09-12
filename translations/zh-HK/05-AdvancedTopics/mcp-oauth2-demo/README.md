# MCP OAuth2 示範

> [!WARNING]
> 這是一個本地學習範例，不是生產授權服務。它
> 使用記憶體中的客戶端並在啟動時產生新的簽名金鑰。切勿
> 將其與共用、預設或版本控制中的客戶端密鑰一起部署。

## 介紹

OAuth2 是產業標準的授權協定，可在不分享憑證的情況下安全存取資源。在 MCP（模型上下文協定）實作中，OAuth2 提供了一種強健的方式，用來認證並授權客戶端（例如人工智慧代理）存取 MCP 伺服器及其工具。

本課程示範如何使用 Spring Boot 為 MCP 伺服器實作 OAuth2 認證，這是在企業與生產部署中常見的模式。

## 學習目標

完成本課程後，您將能：
- 理解 OAuth2 如何整合到 MCP 伺服器中
- 實作 Spring 授權伺服器以發行存取權杖
- 使用基於 JWT 的認證來保護 MCP 端點
- 為機器對機器通訊配置客戶端憑證流程

## 先決條件

- 基本 Java 與 Spring Boot 知識
- 熟悉早期模組中的 MCP 概念
- 已安裝 Maven 或 Gradle

---

## 專案概覽

本專案是一個<strong>極簡 Spring Boot 應用程式</strong>，同時扮演：

* 一個<strong>Spring 授權伺服器</strong>（透過 `client_credentials` 流程發行 JWT 存取權杖），及  
* 一個<strong>資源伺服器</strong>（保護其自身的 `/hello` 端點）。

它符合 [Spring 部落格文章 (2025 年 4 月 2 日)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) 中展示的設定。

---

## 快速開始（本地）

```bash
# 使用獨特的本地值，並盡可能避免被記錄在 shell 歷史紀錄中。
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# 獲取一個令牌
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# 調用受保護的端點
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## 測試 OAuth2 設定

你可以透過以下步驟測試 OAuth2 安全設定：

### 1. 確認伺服器正在運行且安全

```bash
# 這應該返回 401 未經授權，確認 OAuth2 安全性已啟用
curl -v http://localhost:8081/
```

### 2. 使用客戶端憑證取得存取權杖

```bash
# 獲取並提取完整的令牌回應
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# 或者只提取令牌（需要 jq）
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

在 PowerShell 中，請先設定本地密鑰再執行 Maven：

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. 使用權杖存取受保護的端點

```bash
# 使用已儲存的令牌
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# 或直接使用令牌值
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

若成功回應顯示 "Hello from MCP OAuth2 Demo!"，表示 OAuth2 設定運作正常。

---

## 容器建置

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## 生產安全

對於生產部署，請使用專用的身份提供者，而非
此內建示範授權伺服器。請將憑證存放在受管理的
秘密資料庫，定期輪替，使用持久簽名金鑰，限制作用範圍，
且設定明確的發行者。切勿將客戶端密鑰置於原始碼、容器
映像、部署清單或命令輸出中。

對於 Azure Container Apps，請將值儲存在由 Key Vault 支援的 Container Apps 秘密中，
然後透過 `OAUTH_CLIENT_SECRET` 環境變數只暴露秘密參考。


---

## 部署到 **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

入口 FQDN 將成為您的<strong>發行者</strong> (`https://<fqdn>`)。  
Azure 會自動為 `*.azurecontainerapps.io` 提供受信任的 TLS 憑證。

---

## 整合至 **Azure API 管理**

將此入站政策新增到您的 API：

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

APIM 將擷取 JWKS 並驗證每個請求。

---

## 下一步

- [5.4 根上下文](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->