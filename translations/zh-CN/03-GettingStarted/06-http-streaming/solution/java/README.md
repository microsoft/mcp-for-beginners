# Calculator HTTP Streaming 演示

本项目演示了使用 Spring Boot WebFlux 通过 Server-Sent Events (SSE) 实现 HTTP 流式传输。它包含两个应用：

- **Calculator Server**：一个响应式 Web 服务，执行计算并通过 SSE 传输结果
- **Calculator Client**：一个客户端应用，消费流式传输的端点

## 前提条件

- Java 17 或更高版本
- Maven 3.6 或更高版本

## 项目结构

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## 工作原理

1. **Calculator Server** 提供 `/calculate` 端点：
   - 接收查询参数：`a`（数字）、`b`（数字）、`op`（操作）
   - 支持的操作：`add`、`sub`、`mul`、`div`
   - 返回带有计算进度和结果的 Server-Sent Events

2. **Calculator Client** 连接服务器：
   - 发送请求计算 `7 * 5`
   - 消费流式响应
   - 将每个事件打印到控制台

## 运行应用程序

### 选项 1：使用 Maven（推荐）

#### 1. 启动 Calculator Server

打开终端，进入服务器目录：

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

服务器将在 `http://localhost:8080` 启动

你应该会看到类似如下的输出：
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. 运行 Calculator Client

打开**新终端**，进入客户端目录：

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

客户端将连接服务器，执行计算，并显示流式结果。

### 选项 2：直接使用 Java

#### 1. 编译并运行服务器：

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. 编译并运行客户端：

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## 手动测试服务器

你也可以使用浏览器或 curl 测试服务器：

### 使用浏览器：
访问：`http://localhost:8080/calculate?a=10&b=5&op=add`

### 使用 curl：
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## 预期输出

运行客户端时，你应该看到类似如下的流式输出：

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## 支持的操作

- `add` - 加法 (a + b)
- `sub` - 减法 (a - b)
- `mul` - 乘法 (a * b)
- `div` - 除法 (a / b，若 b = 0 返回 NaN)

## API 参考

### GET /calculate

**参数：**
- `a`（必填）：第一个数字（double）
- `b`（必填）：第二个数字（double）
- `op`（必填）：操作类型（`add`、`sub`、`mul`、`div`）

**响应：**
- Content-Type: `text/event-stream`
- 返回带有计算进度和结果的 Server-Sent Events

**示例请求：**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**示例响应：**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## 故障排除

### 常见问题

1. **端口 8080 已被占用**
   - 停止占用端口 8080 的其他应用
   - 或修改 `calculator-server/src/main/resources/application.yml` 中的服务器端口

2. **连接被拒绝**
   - 确保服务器已启动后再启动客户端
   - 检查服务器是否成功启动并监听端口 8080

3. **参数名问题**
   - 本项目包含带有 `-parameters` 标志的 Maven 编译配置
   - 如果遇到参数绑定问题，确认项目已使用该配置构建

### 停止应用程序

- 在运行应用的终端按 `Ctrl+C`
- 或者如果作为后台进程运行，使用 `mvn spring-boot:stop`

## 技术栈

- **Spring Boot 3.3.1** - 应用框架
- **Spring WebFlux** - 响应式 Web 框架
- **Project Reactor** - 响应式流库
- **Netty** - 非阻塞 I/O 服务器
- **Maven** - 构建工具
- **Java 17+** - 编程语言

## 后续步骤

尝试修改代码以：
- 添加更多数学运算
- 包含无效操作的错误处理
- 添加请求/响应日志
- 实现身份验证
- 添加单元测试

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。