# MCP OAuth2 演示

> [!WARNING]
> 这是一个本地学习示例，不是生产授权服务。它
> 使用内存中的客户端并在启动时生成新的签名密钥。切勿
> 在共享、默认或源代码控制的客户端密钥下部署。

## 介绍

OAuth2 是行业标准的授权协议，实现了不共享凭据的安全访问资源。在 MCP（模型上下文协议）实现中，OAuth2 提供了一种强大方式，验证和授权客户端（例如 AI 代理）访问 MCP 服务器及其工具。

本课演示如何使用 Spring Boot 实现 MCP 服务器的 OAuth2 身份验证，这是一种企业和生产部署的常见模式。

## 学习目标

到本课结束，您将能够：
- 理解 OAuth2 如何与 MCP 服务器集成
- 实现用于令牌发行的 Spring 授权服务器
- 用基于 JWT 的身份验证保护 MCP 端点
- 配置客户端凭据流实现机器对机器通信

## 先决条件

- 基本的 Java 和 Spring Boot 知识
- 熟悉早期模块中的 MCP 概念
- 已安装 Maven 或 Gradle

---

## 项目概览

该项目是一个<strong>最简化的 Spring Boot 应用程序</strong>，同时作为：

* 一个<strong>Spring 授权服务器</strong>（通过 `client_credentials` 流发放 JWT 访问令牌），以及  
* 一个<strong>资源服务器</strong>（保护其自身的 `/hello` 端点）。

它映射了 [Spring 博客文章 (2025 年 4 月 2 日)](https://spring.io/blog/2025/04/02/mcp-server-oauth2) 中展示的设置。

---

## 快速开始（本地）

```bash
# 使用唯一的本地值，并在可能的情况下将其排除在shell历史之外。
export OAUTH_CLIENT_SECRET="replace-with-a-random-local-secret"
mvn spring-boot:run

# 获取令牌
curl -u "mcp-client:${OAUTH_CLIENT_SECRET}" -d grant_type=client_credentials \
     http://localhost:8081/oauth2/token | jq -r .access_token > token.txt

# 调用受保护的端点
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello
```

---

## 测试 OAuth2 配置

你可以通过以下步骤测试 OAuth2 安全配置：

### 1. 验证服务器是否运行并已加固

```bash
# 这应返回401未授权，确认OAuth2安全性已启用
curl -v http://localhost:8081/
```

### 2. 使用客户端凭据获取访问令牌

```bash
# 获取并提取完整的令牌响应
curl -v -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access"

# 或仅提取令牌（需要 jq）
curl -s -X POST http://localhost:8081/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -u "mcp-client:${OAUTH_CLIENT_SECRET}" \
  -d "grant_type=client_credentials&scope=mcp.access" | jq -r .access_token > token.txt
```

在 PowerShell 中，在运行 Maven 之前设置本地密钥：

```powershell
$env:OAUTH_CLIENT_SECRET = "replace-with-a-random-local-secret"
mvn spring-boot:run
```

### 3. 使用令牌访问受保护端点

```bash
# 使用保存的令牌
curl -H "Authorization: Bearer $(cat token.txt)" http://localhost:8081/hello

# 或者直接使用令牌值
curl -H "Authorization: Bearer eyJra...token_value...xyz" http://localhost:8081/hello
```

返回 "Hello from MCP OAuth2 Demo!" 的成功响应确认 OAuth2 配置运行正常。

---

## 容器构建

```bash
docker build -t mcp-oauth2-demo .
docker run --rm -p 8081:8081 \
  -e OAUTH_CLIENT_SECRET="$OAUTH_CLIENT_SECRET" \
  mcp-oauth2-demo
```

## 生产环境安全

对于生产部署，应使用专门的身份提供者，而非
此进程内示范授权服务器。将凭据存储在托管的
密钥库中，定期轮换，使用持久签名密钥，限制范围，
并设置明确的签发者。切勿将客户端密钥放入源代码、容器
镜像、部署清单或命令输出。

对于 Azure 容器应用，尽可能将值存储为基于
Key Vault 的容器应用密钥，然后仅通过
`OAUTH_CLIENT_SECRET` 环境变量暴露密钥引用。

---

## 部署到 **Azure 容器应用**

```bash
az containerapp up -n mcp-oauth2 \
  -g demo-rg -l westeurope \
  --image <your-registry>/mcp-oauth2-demo:latest \
  --ingress external --target-port 8081
```

入口 FQDN 将成为你的<strong>签发者</strong> (`https://<fqdn>`)。  
Azure 自动为 `*.azurecontainerapps.io` 提供受信任的 TLS 证书。

---

## 集成到 **Azure API 管理**

在你的 API 中添加此入站策略：

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

APIM 将获取 JWKS，并验证每一个请求。

---

## 下一步

- [5.4 根上下文](../mcp-root-contexts/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->