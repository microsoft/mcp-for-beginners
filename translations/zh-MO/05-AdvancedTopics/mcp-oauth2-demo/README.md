# MCP OAuth2 示範

> [!WARNING]
> 這是一個本地學習範例，而非生產授權服務。它
> 使用記憶體中的客戶端，並於啟動時產生新的簽名金鑰。絕對不要
> 以共用、預設或原始碼控管的客戶端密鑰部署。

## 介紹

OAuth2 是業界標準的授權協定，能在不共享憑證的情況下提供安全訪問資源。在 MCP（模型上下文協定）實作中，OAuth2 提供了穩健的方式來驗證及授權客戶端（例如 AI 代理）訪問 MCP 伺服器及其工具。

本課程示範如何使用 Spring Boot 為 MCP 伺服器實作 OAuth2 認證，這是企業及生產部署中的常見模式。

## 學習目標

完成本課程後，您將能夠：
- 理解 OAuth2 如何整合進 MCP 伺服器
- 實作 Spring 授權伺服器以進行令牌簽發
- 以基於 JWT 的認證保護 MCP 端點
- 設定用於機器對機器通訊的客戶端憑證流程

## 先決條件

- 具備 Java 與 Spring Boot 基本知識
- 熟悉先前模組中的 MCP 概念
- 已安裝 Maven 或 Gradle

---

## 專案概述

此專案為一個<strong>極簡 Spring Boot 應用程式</strong>，同時扮演：

* **Spring 授權伺服器**（透過 `client_credentials` 流程簽發 JWT 存取令牌），及  
* <strong>資源伺服器</strong>（保護自身的 `/hello` 端點）。

它模擬了 [Spring 部落格文章 (2025年4月2日)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) 中展示的設置。

---

## 快速開始（本地）

```bash
# 使用獨特的本地值，並盡可能避免將其保存在 shell 歷史中。
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# 獲取一個令牌
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# 呼叫受保護的端點
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## 測試 OAuth2 設定

您可以透過以下步驟測試 OAuth2 安全設定：

### 1. 確認伺服器正在運行且受到保護

```bash
# 這應該返回 401 未經授權，確認 OAuth2 安全性已啟用
curl -v http://localhost:8081/
```

### 2. 使用客戶端憑證取得存取令牌

```bash
# 獲取並提取完整的令牌響應
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# 或僅提取令牌（需要 jq）
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

在 PowerShell 中執行 Maven 前，先設定本地密鑰：

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. 使用令牌存取受保護的端點

```bash
# 使用已儲存的令牌
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# 或直接使用令牌值
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

若成功回應 "Hello from MCP OAuth2 Demo!"，代表 OAuth2 設定運作正常。

---

## 建置容器映像

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## 生產環境安全性

在生產部署時，請使用專屬的身分識別供應商，而非
此內嵌演示授權伺服器。請將憑證存放於受管控的
秘密庫，定期輪換，採用持久化簽名金鑰、限制作用域，並
明確設定發行者。切勿將客戶端密鑰置入原始碼、容器
映像、部署清單或指令輸出中。

若使用 Azure 容器應用服務，請將該值存放為由密鑰保管庫支援的容器應用秘密，
並透過 `OAUTH_CLIENT_SECRET` 環境變數僅揭露秘密參考值。


---

## 部署於 **Azure 容器應用服務**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

入口 FQDN 將成為您的<strong>發行者</strong> (`https://<fqdn>`)。  
Azure 會自動為 `*.azurecontainerapps.io` 提供受信任的 TLS 證書。

---

## 整合至 **Azure API 管理**

為您的 API 新增此入口政策：

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
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->