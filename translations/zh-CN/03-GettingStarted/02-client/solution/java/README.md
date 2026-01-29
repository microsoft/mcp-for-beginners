# MCP Java 客户端 - 计算器演示

本项目演示如何创建一个 Java 客户端，连接并与 MCP（模型上下文协议）服务器交互。在本例中，我们将连接到第01章的计算器服务器，并执行各种数学运算。

## 前提条件

在运行此客户端之前，您需要：

1. **启动第01章的计算器服务器**：
   - 进入计算器服务器目录：`03-GettingStarted/01-first-server/solution/java/`
   - 构建并运行计算器服务器：
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - 服务器应运行在 `http://localhost:8080`

2. 在系统中安装 **Java 21 或更高版本**
3. 安装 **Maven**（通过 Maven Wrapper 包含）

## 什么是 SDKClient？

`SDKClient` 是一个 Java 应用程序，演示如何：
- 使用 Server-Sent Events (SSE) 传输连接到 MCP 服务器
- 列出服务器上可用的工具
- 远程调用各种计算器函数
- 处理响应并显示结果

## 工作原理

客户端使用 Spring AI MCP 框架来：

1. **建立连接**：创建一个 WebFlux SSE 客户端传输，连接到计算器服务器
2. **初始化客户端**：设置 MCP 客户端并建立连接
3. **发现工具**：列出所有可用的计算器操作
4. **执行操作**：使用示例数据调用各种数学函数
5. **显示结果**：展示每个计算结果

## 项目结构

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## 主要依赖

项目使用以下主要依赖：

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

该依赖提供：
- `McpClient` - 主要客户端接口
- `WebFluxSseClientTransport` - 用于基于 Web 的 SSE 传输
- MCP 协议的模式和请求/响应类型

## 构建项目

使用 Maven Wrapper 构建项目：

```cmd
.\mvnw clean install
```

## 运行客户端

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**注意**：执行这些命令前，请确保计算器服务器正在 `http://localhost:8080` 运行。

## 客户端功能

运行客户端时，它将：

1. **连接** 到 `http://localhost:8080` 的计算器服务器
2. **列出工具** - 显示所有可用的计算器操作
3. **执行计算**：
   - 加法：5 + 3 = 8
   - 减法：10 - 4 = 6
   - 乘法：6 × 7 = 42
   - 除法：20 ÷ 4 = 5
   - 幂运算：2^8 = 256
   - 平方根：√16 = 4
   - 绝对值：|-5.5| = 5.5
   - 帮助：显示可用操作

## 预期输出

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**注意**：你可能会看到 Maven 关于残留线程的警告——这是响应式应用的正常现象，不代表错误。

## 代码解析

### 1. 传输设置
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
这段代码创建了一个 SSE（服务器发送事件）传输，连接到计算器服务器。

### 2. 客户端创建
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
创建一个同步的 MCP 客户端并初始化连接。

### 3. 调用工具
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
调用名为 "add" 的工具，参数为 a=5.0 和 b=3.0。

## 故障排除

### 服务器未运行
如果出现连接错误，请确保第01章的计算器服务器正在运行：
```
Error: Connection refused
```
**解决方案**：先启动计算器服务器。

### 端口已被占用
如果端口 8080 被占用：
```
Error: Address already in use
```
**解决方案**：停止占用端口 8080 的其他应用，或修改服务器使用其他端口。

### 构建错误
如果遇到构建错误：
```cmd
.\mvnw clean install -DskipTests
```

## 了解更多

- [Spring AI MCP 文档](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [模型上下文协议规范](https://modelcontextprotocol.io/)
- [Spring WebFlux 文档](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。