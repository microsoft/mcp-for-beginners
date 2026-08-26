# 计算器 LLM 客户端

一个 Java 应用程序，演示如何使用 LangChain4j 通过 MiniMax OpenAI 兼容 API 连接到 MCP（模型上下文协议）计算器服务。

## 先决条件

- Java 21 或更高版本
- Maven 3.6+（或使用自带的 Maven 包装器）
- 一个 MiniMax API 密钥
- 一个运行在 `http://localhost:8080` 上的 MCP 计算器服务

## 获取 API 密钥

本应用程序使用 MiniMax OpenAI 兼容 API。按照以下步骤获取您的密钥和端点：

### 1. 选择端点
1. 使用 `https://api.minimax.io/v1` 作为全球端点
2. 使用 `https://api.minimaxi.com/v1` 作为中国端点

### 2. 创建 API 密钥
1. 从您的 MiniMax 账号创建一个 MiniMax API 密钥
2. 将密钥妥善保存

### 3. 设置环境变量

#### 在 Windows（命令提示符）:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### 在 Windows（PowerShell）:
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### 在 macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## 设置与安装

1. <strong>克隆或进入项目目录</strong>

2. <strong>安装依赖</strong>：
   ```cmd
   mvnw clean install
   ```
   或者如果你全局安装了 Maven:
   ```cmd
   mvn clean install
   ```

3. <strong>设置环境变量</strong>（参见上述“获取 API 密钥”部分）

4. **启动 MCP 计算器服务**：
   确保第1章的 MCP 计算器服务运行在 `http://localhost:8080/sse`。该服务应在启动客户端前运行。

## 运行应用程序

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 应用功能介绍

应用演示了与计算器服务的三种主要交互方式：

1. <strong>加法</strong>：计算 24.5 与 17.3 的和
2. <strong>平方根</strong>：计算 144 的平方根
3. <strong>帮助</strong>：展示可用的计算器功能

## 预期输出

成功运行时，您应看到类似以下的输出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 故障排除

### 常见问题

1. **“未设置 OPENAI_API_KEY 环境变量”**
   - 确认已设置 `OPENAI_API_KEY` 环境变量
   - 设置变量后重启终端/命令提示符

2. **“连接被拒绝到 localhost:8080”**
   - 确保 MCP 计算器服务运行在端口 8080
   - 检查端口 8080 是否被其他服务占用

3. **“认证失败”**
   - 验证您的 API 密钥是否有效
   - 检查 `OPENAI_BASE_URL` 是否与您想使用的端点匹配

4. **Maven 构建错误**
   - 确保使用 Java 21 或更高版本：`java -version`
   - 尝试清理构建：`mvnw clean`

### 调试

运行时添加以下 JVM 参数以启用调试日志：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 配置

应用配置为：
- 默认使用 MiniMax-M3，或当设置了 `MINIMAX_MODEL_ID` 时使用 MiniMax-M2.7
- 连接到 `OPENAI_BASE_URL`（如果设置），否则当 `MINIMAX_REGION=cn_zh` 时使用 `https://api.minimaxi.com/v1`，默认使用 `https://api.minimax.io/v1`
- 连接到 `http://localhost:8080/sse` 的 MCP 服务
- 请求超时设置为 60 秒

## 依赖

本项目使用的主要依赖：
- **LangChain4j**：用于 AI 集成和工具管理
- **LangChain4j MCP**：用于模型上下文协议支持
- **LangChain4j OpenAI official**：用于 MiniMax OpenAI 兼容 API 集成
- **Spring Boot**：用于应用框架和依赖注入

## 许可证

本项目采用 Apache License 2.0 许可 - 详细信息请参阅 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 文件。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->