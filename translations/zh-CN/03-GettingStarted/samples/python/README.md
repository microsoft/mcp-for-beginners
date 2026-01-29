# MCP计算器服务器 (Python)

一个简单的模型上下文协议 (MCP) 服务器的Python实现，提供基本的计算器功能。

## 安装

安装所需的依赖项：

```bash
pip install -r requirements.txt
```

或者直接安装MCP Python SDK：

```bash
pip install mcp>=1.18.0
```

## 使用方法

### 启动服务器

该服务器设计用于MCP客户端（例如Claude Desktop）。启动服务器：

```bash
python mcp_calculator_server.py
```

**注意**：直接在终端运行时，您可能会看到JSON-RPC验证错误。这是正常现象——服务器正在等待格式正确的MCP客户端消息。

### 测试功能

测试计算器功能是否正常工作：

```bash
python test_calculator.py
```

## 故障排除

### 导入错误

如果您看到`ModuleNotFoundError: No module named 'mcp'`，请安装MCP Python SDK：

```bash
pip install mcp>=1.18.0
```

### 直接运行时的JSON-RPC错误

直接运行服务器时出现类似“Invalid JSON: EOF while parsing a value”的错误是预期的。服务器需要MCP客户端消息，而不是直接的终端输入。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。