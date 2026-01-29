# 完整的 MCP 客户端示例

此目录包含用不同编程语言编写的完整、可运行的 MCP 客户端示例。每个客户端都展示了主教程 README.md 中描述的全部功能。

## 可用客户端

### 1. Java 客户端 (`client_example_java.java`)

- **传输方式**: 基于 HTTP 的 SSE（服务器发送事件）
- **目标服务器**: `http://localhost:8080`
- **功能**:
  - 建立连接并发送 ping
  - 工具列表
  - 计算器操作（加、减、乘、除、帮助）
  - 错误处理和结果提取

**运行方式:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# 客户端 (`client_example_csharp.cs`)

- **传输方式**: 标准输入/输出（Stdio）
- **目标服务器**: 本地 .NET MCP 服务器，通过 dotnet run 启动
- **功能**:
  - 通过 stdio 传输自动启动服务器
  - 工具和资源列表
  - 计算器操作
  - JSON 结果解析
  - 全面的错误处理

**运行方式:**

```bash
dotnet run
```

### 3. TypeScript 客户端 (`client_example_typescript.ts`)

- **传输方式**: 标准输入/输出（Stdio）
- **目标服务器**: 本地 Node.js MCP 服务器
- **功能**:
  - 完整的 MCP 协议支持
  - 工具、资源和提示操作
  - 计算器操作
  - 资源读取和提示执行
  - 强大的错误处理

**运行方式:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python 客户端 (`client_example_python.py`)

- **传输方式**: 标准输入/输出（Stdio）  
- **目标服务器**: 本地 Python MCP 服务器
- **功能**:
  - 使用 Async/Await 模式进行操作
  - 工具和资源发现
  - 测试计算器操作
  - 读取资源内容
  - 基于类的组织结构

**运行方式:**

```bash
python client_example_python.py
```

## 所有客户端的通用功能

每个客户端实现都展示了以下内容：

1. **连接管理**
   - 建立与 MCP 服务器的连接
   - 处理连接错误
   - 正确的清理和资源管理

2. **服务器发现**
   - 列出可用工具
   - 列出可用资源（如果支持）
   - 列出可用提示（如果支持）

3. **工具调用**
   - 基本的计算器操作（加、减、乘、除）
   - 获取服务器信息的帮助命令
   - 正确的参数传递和结果处理

4. **错误处理**
   - 连接错误
   - 工具执行错误
   - 优雅的失败处理和用户反馈

5. **结果处理**
   - 从响应中提取文本内容
   - 格式化输出以提高可读性
   - 处理不同的响应格式

## 前置条件

在运行这些客户端之前，请确保：

1. **对应的 MCP 服务器正在运行**（位于 `../01-first-server/`）
2. **已安装所选语言的必要依赖**
3. **网络连接正常**（对于基于 HTTP 的传输）

## 各实现之间的主要区别

| 编程语言   | 传输方式   | 服务器启动方式 | 异步模型     | 关键库              |
|------------|------------|----------------|--------------|---------------------|
| Java       | SSE/HTTP   | 外部启动       | 同步         | WebFlux, MCP SDK    |
| C#         | Stdio      | 自动启动       | Async/Await  | .NET MCP SDK        |
| TypeScript | Stdio      | 自动启动       | Async/Await  | Node MCP SDK        |
| Python     | Stdio      | 自动启动       | AsyncIO      | Python MCP SDK      |
| Rust       | Stdio      | 自动启动       | Async/Await  | Rust MCP SDK, Tokio |

## 下一步

在探索这些客户端示例之后：

1. **修改客户端**以添加新功能或操作
2. **创建自己的服务器**并使用这些客户端进行测试
3. **尝试不同的传输方式**（如 SSE 和 Stdio）
4. **构建更复杂的应用程序**，集成 MCP 功能

## 故障排除

### 常见问题

1. **连接被拒绝**: 确保 MCP 服务器正在预期的端口/路径上运行
2. **模块未找到**: 安装所需语言的 MCP SDK
3. **权限被拒绝**: 检查 stdio 传输的文件权限
4. **工具未找到**: 确认服务器实现了预期的工具

### 调试提示

1. **启用 MCP SDK 的详细日志记录**
2. **检查服务器日志**以获取错误信息
3. **验证工具名称和签名**是否在客户端和服务器之间匹配
4. **先使用 MCP Inspector 测试**以验证服务器功能

## 相关文档

- [主客户端教程](./README.md)
- [MCP 服务器示例](../../../../03-GettingStarted/01-first-server)
- [MCP 与 LLM 集成](../../../../03-GettingStarted/03-llm-client)
- [官方 MCP 文档](https://modelcontextprotocol.io/)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。