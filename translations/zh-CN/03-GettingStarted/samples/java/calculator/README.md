# Basic Calculator MCP Service

该服务通过使用 Spring Boot 和 WebFlux 传输的 Model Context Protocol (MCP) 提供基本的计算器操作。它设计为一个简单示例，适合初学者学习 MCP 实现。

更多信息请参见 [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) 参考文档。

## 概述

该服务展示了：
- 支持 SSE（服务器发送事件）
- 使用 Spring AI 的 `@Tool` 注解实现自动工具注册
- 基本计算器功能：
  - 加法、减法、乘法、除法
  - 幂运算和平方根
  - 取模（余数）和绝对值
  - 帮助功能，提供操作说明

## 功能特点

该计算器服务提供以下功能：

1. **基本算术运算**：
   - 两数相加
   - 一数减去另一数
   - 两数相乘
   - 一数除以另一数（含除零检查）

2. **高级运算**：
   - 幂运算（底数的指数次方）
   - 平方根计算（含负数检查）
   - 取模（余数）计算
   - 绝对值计算

3. **帮助系统**：
   - 内置帮助函数，解释所有可用操作

## 使用该服务

该服务通过 MCP 协议暴露以下 API 端点：

- `add(a, b)`：两个数相加
- `subtract(a, b)`：第一个数减去第二个数
- `multiply(a, b)`：两个数相乘
- `divide(a, b)`：第一个数除以第二个数（含除零检查）
- `power(base, exponent)`：计算幂
- `squareRoot(number)`：计算平方根（含负数检查）
- `modulus(a, b)`：计算除法余数
- `absolute(number)`：计算绝对值
- `help()`：获取可用操作的信息

## 测试客户端

在 `com.microsoft.mcp.sample.client` 包中包含了一个简单的测试客户端。`SampleCalculatorClient` 类演示了计算器服务的可用操作。

## 使用 LangChain4j 客户端

项目中包含了一个 LangChain4j 示例客户端 `com.microsoft.mcp.sample.client.LangChain4jClient`，演示如何将计算器服务与 LangChain4j 及 GitHub 模型集成：

### 前提条件

1. **GitHub 令牌设置**：

   要使用 GitHub 的 AI 模型（如 phi-4），需要 GitHub 个人访问令牌：

   a. 访问你的 GitHub 账户设置：https://github.com/settings/tokens

   b. 点击“Generate new token” → “Generate new token (classic)”

   c. 给令牌起一个描述性名称

   d. 选择以下权限范围：
      - `repo`（私有仓库的完全控制权限）
      - `read:org`（读取组织和团队成员资格，读取组织项目）
      - `gist`（创建 Gist）
      - `user:email`（访问用户邮箱地址（只读））

   e. 点击“Generate token”并复制新令牌

   f. 设置为环境变量：

      Windows 系统：
      ```
      set GITHUB_TOKEN=your-github-token
      ```

      macOS/Linux 系统：
      ```bash
      export GITHUB_TOKEN=your-github-token
      ```

   g. 若需持久化设置，请通过系统设置将其添加到环境变量中

2. 将 LangChain4j GitHub 依赖添加到项目中（已包含在 pom.xml）：
   ```xml
   <dependency>
       <groupId>dev.langchain4j</groupId>
       <artifactId>langchain4j-github</artifactId>
       <version>${langchain4j.version}</version>
   </dependency>
   ```

3. 确保计算器服务器正在 `localhost:8080` 运行

### 运行 LangChain4j 客户端

该示例演示了：
- 通过 SSE 传输连接计算器 MCP 服务器
- 使用 LangChain4j 创建一个利用计算器操作的聊天机器人
- 集成 GitHub AI 模型（当前使用 phi-4 模型）

客户端发送以下示例查询以展示功能：
1. 计算两个数字的和
2. 计算一个数字的平方根
3. 获取关于可用计算器操作的帮助信息

运行示例并查看控制台输出，了解 AI 模型如何使用计算器工具响应查询。

### GitHub 模型配置

LangChain4j 客户端配置为使用 GitHub 的 phi-4 模型，配置如下：

```java
ChatLanguageModel model = GitHubChatModel.builder()
    .apiKey(System.getenv("GITHUB_TOKEN"))
    .timeout(Duration.ofSeconds(60))
    .modelName("phi-4")
    .logRequests(true)
    .logResponses(true)
    .build();
```

若要使用其他 GitHub 模型，只需将 `modelName` 参数更改为支持的其他模型（例如 "claude-3-haiku-20240307"、"llama-3-70b-8192" 等）。

## 依赖项

项目需要以下关键依赖：

```xml
<!-- For MCP Server -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>

<!-- For LangChain4j integration -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-mcp</artifactId>
    <version>${langchain4j.version}</version>
</dependency>

<!-- For GitHub models support -->
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-github</artifactId>
    <version>${langchain4j.version}</version>
</dependency>
```

## 构建项目

使用 Maven 构建项目：
```bash
./mvnw clean install -DskipTests
```

## 运行服务器

### 使用 Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### 使用 MCP Inspector

MCP Inspector 是一个方便与 MCP 服务交互的工具。使用该计算器服务时：

1. **安装并运行 MCP Inspector**，在新终端窗口执行：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **通过应用显示的 URL 访问 Web UI**（通常是 http://localhost:6274）

3. **配置连接**：
   - 传输类型选择“SSE”
   - URL 设置为正在运行服务器的 SSE 端点：`http://localhost:8080/sse`
   - 点击“Connect”

4. **使用工具**：
   - 点击“List Tools”查看可用的计算器操作
   - 选择一个工具，点击“Run Tool”执行操作

![MCP Inspector Screenshot](../../../../../../translated_images/zh-CN/tool.c75a0b2380efcf1a47a8478f54380a36ddcca7943b98f56dabbac8b07e15c3bb.png)

### 使用 Docker

项目包含用于容器化部署的 Dockerfile：

1. **构建 Docker 镜像**：
   ```bash
   docker build -t calculator-mcp-service .
   ```

2. **运行 Docker 容器**：
   ```bash
   docker run -p 8080:8080 calculator-mcp-service
   ```

这将：
- 使用 Maven 3.9.9 和 Eclipse Temurin 24 JDK 构建多阶段 Docker 镜像
- 创建优化后的容器镜像
- 开放 8080 端口
- 在容器内启动 MCP 计算器服务

容器启动后，可通过 `http://localhost:8080` 访问服务。

## 故障排除

### GitHub 令牌常见问题

1. **令牌权限问题**：如果出现 403 Forbidden 错误，请检查令牌是否具有前述权限。

2. **找不到令牌**：如果出现“No API key found”错误，确认 GITHUB_TOKEN 环境变量已正确设置。

3. **速率限制**：GitHub API 有调用频率限制，遇到 429 错误时，请等待几分钟后重试。

4. **令牌过期**：GitHub 令牌可能会过期，若出现认证错误，请生成新令牌并更新环境变量。

如需更多帮助，请查阅 [LangChain4j 文档](https://github.com/langchain4j/langchain4j) 或 [GitHub API 文档](https://docs.github.com/en/rest)。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。