# MCP 计算器服务器（Python）



一个用 Python 实现的简单模型上下文协议（MCP）服务器，提供基本的计算器功能。


## 安装

安装所需依赖：

```bash
pip install -r requirements.txt
```

或者直接安装 MCP Python SDK：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## 使用方法

### 运行服务器

该服务器设计用于 MCP 客户端（如 Claude Desktop）使用。启动服务器：

```bash
python mcp_calculator_server.py
```

<strong>注意</strong>：直接在终端运行时，你会看到 JSON-RPC 验证错误。这是正常现象——服务器正在等待格式正确的 MCP 客户端消息。

### 测试功能

测试计算器功能是否正常：

```bash
python test_calculator.py
```

## 故障排查

### 导入错误

如果看到 `ModuleNotFoundError: No module named 'mcp'`，请安装 MCP Python SDK：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### 直接运行时的 JSON-RPC 错误

直接运行服务器时出现“Invalid JSON: EOF while parsing a value”这类错误是预期中的。服务器需要 MCP 客户端消息，而不是直接终端输入。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->