# MCP OAuth2 演示

该项目是一个**最简化的 Spring Boot 应用程序**，同时扮演以下两个角色：

* **Spring 授权服务器**（通过 `client_credentials` 流程颁发 JWT 访问令牌），以及  
* **资源服务器**（保护自身的 `/hello` 端点）。

它复刻了[Spring 博客文章（2025 年 4 月 2 日）](https://spring.io/blog/2025/04/02/mcp-server-oauth2)中展示的配置。

---

## 快速开始（本地）

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

## 测试 OAuth2 配置

你可以通过以下步骤测试 OAuth2 安全配置：

### 1. 验证服务器是否运行且已启用安全保护

```bash
# This should return 401 Unauthorized, confirming OAuth2 security is active
curl -v http://localhost:8081/
```

### 2. 使用客户端凭据获取访问令牌

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

注意：Basic 认证头（`bWNwLWNsaWVudDpzZWNyZXQ=`）是 `mcp-client:secret` 的 Base64 编码。

### 3. 使用令牌访问受保护的端点

```bash
# Using the saved token
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# Or directly with the token value
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

如果成功响应并显示 “Hello from MCP OAuth2 Demo!”，则说明 OAuth2 配置工作正常。

---

## 容器构建

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

入口 FQDN 将成为你的**发行者**（`https://<fqdn>`）。  
Azure 会自动为 `*.azurecontainerapps.io` 提供受信任的 TLS 证书。

---

## 集成到 **Azure API Management**

将以下入站策略添加到你的 API：

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

APIM 会获取 JWKS 并验证每个请求。

---

## 后续内容

- [5.4 根上下文](../mcp-root-contexts/README.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。