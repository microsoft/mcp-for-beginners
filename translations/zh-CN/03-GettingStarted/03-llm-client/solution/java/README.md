# Calculator LLM Client

一个 Java 应用程序，演示如何使用 LangChain4j 连接带有 GitHub Models 集成的 MCP（模型上下文协议）计算器服务。

## 前提条件

- Java 21 或更高版本
- Maven 3.6+（或使用附带的 Maven 包装器）
- 拥有访问 GitHub Models 权限的 GitHub 账号
- 在 `http://localhost:8080` 运行的 MCP 计算器服务

## 获取 GitHub Token

该应用使用 GitHub Models，需要 GitHub 个人访问令牌。请按照以下步骤获取令牌：

### 1. 访问 GitHub Models
1. 访问 [GitHub Models](https://github.com/marketplace/models)
2. 使用你的 GitHub 账号登录
3. 如果尚未获得访问权限，请申请访问 GitHub Models

### 2. 创建个人访问令牌
1. 进入 [GitHub 设置 → 开发者设置 → 个人访问令牌 → 令牌（经典）](https://github.com/settings/tokens)
2. 点击“生成新令牌” → “生成新令牌（经典）”
3. 给令牌起一个描述性名称（例如，“MCP Calculator Client”）
4. 根据需要设置过期时间
5. 选择以下权限范围：
   - `repo`（如果需要访问私有仓库）
   - `user:email`
6. 点击“生成令牌”
7. **重要**：请立即复制令牌，之后将无法再次查看！

### 3. 设置环境变量

#### Windows（命令提示符）：
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows（PowerShell）：
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux：
```bash
export GITHUB_TOKEN=your_github_token_here
```

## 设置与安装

1. **克隆或进入项目目录**

2. **安装依赖**：
   ```cmd
   mvnw clean install
   ```
   如果你已全局安装 Maven：
   ```cmd
   mvn clean install
   ```

3. **设置环境变量**（参见上文“获取 GitHub Token”部分）

4. **启动 MCP 计算器服务**：
   确保第 1 章的 MCP 计算器服务已在 `http://localhost:8080/sse` 运行。启动客户端前需先启动该服务。

## 运行应用程序

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 应用功能说明

该应用演示了与计算器服务的三种主要交互：

1. **加法**：计算 24.5 和 17.3 的和
2. **平方根**：计算 144 的平方根
3. **帮助**：显示可用的计算器功能

## 预期输出

成功运行时，你应看到类似如下输出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 故障排除

### 常见问题

1. **“GITHUB_TOKEN 环境变量未设置”**
   - 确认已设置 `GITHUB_TOKEN` 环境变量
   - 设置后重启终端或命令提示符

2. **“连接被拒绝 localhost:8080”**
   - 确认 MCP 计算器服务已在 8080 端口运行
   - 检查是否有其他服务占用了 8080 端口

3. **“身份验证失败”**
   - 验证 GitHub 令牌是否有效且权限正确
   - 确认你有访问 GitHub Models 的权限

4. **Maven 构建错误**
   - 确认使用的是 Java 21 或更高版本：`java -version`
   - 尝试清理构建：`mvnw clean`

### 调试

要启用调试日志，运行时添加以下 JVM 参数：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 配置

应用配置如下：
- 使用 GitHub Models，模型为 `gpt-4.1-nano`
- 连接 MCP 服务地址为 `http://localhost:8080/sse`
- 请求超时设置为 60 秒
- 启用请求/响应日志以便调试

## 依赖

本项目主要依赖：
- **LangChain4j**：用于 AI 集成和工具管理
- **LangChain4j MCP**：支持模型上下文协议
- **LangChain4j GitHub Models**：集成 GitHub Models
- **Spring Boot**：应用框架和依赖注入

## 许可证

本项目采用 Apache License 2.0 许可，详情请参见 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 文件。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的原文应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。