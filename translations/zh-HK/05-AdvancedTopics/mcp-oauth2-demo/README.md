# MCP OAuth2 示範

這個專案是一個**簡約的 Spring Boot 應用程式**，同時扮演：

* **Spring 授權伺服器**（透過 `client_credentials` 流程發行 JWT 存取權杖），以及  
* **資源伺服器**（保護自己的 `/hello` 端點）。

它模擬了[Spring 部落格文章（2025 年 4 月 2 日）](https://spring.io/blog/2025/04/02/mcp-server-oauth2)中展示的設定。

---

## 快速開始（本地）

```bash
# build & run
./mvnw spring-boot:run

# obtain a token
curl -u mcp-client:secret -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# call the protected endpoint
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## 測試 OAuth2 設定

你可以透過以下步驟測試 OAuth2 的安全設定：

### 1. 確認伺服器正在運行且已保護

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. 使用 client credentials 取得存取權杖

```bash
# Get and extract the full token response
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access"

# Or to extract just the token (requires jq)
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Authorization: Basic bWNwLWNsaWVudDpzZWNyZXQ=" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

注意：Basic Authentication 標頭（`bWNwLWNsaWVudDpzZWNyZXQ=`）是 `mcp-client:secret` 的 Base64 編碼。

### 3. 使用存取權杖存取受保護的端點

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

若成功回應「Hello from MCP OAuth2 Demo!」，表示 OAuth2 設定運作正常。

---

## 建置容器映像檔

```bash
docker build -t mcp-oauth2-demo .
docker run -p 8081:8081 mcp-oauth2-demo
```

---

## 部署到 **Azure Container Apps**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

Ingress 的 FQDN 將成為你的**issuer**（`https://<fqdn>`）。  
Azure 會自動為 `*.azurecontainerapps.io` 提供受信任的 TLS 憑證。

---

## 整合到 **Azure API Management**

將以下 inbound policy 加入你的 API：

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

APIM 會擷取 JWKS 並驗證每一個請求。

---

## 下一步

- [5.4 Root contexts](../mcp-root-contexts/README.md)

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。