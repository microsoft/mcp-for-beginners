# 运行示例

此示例启动一个 MCP 服务器，并添加一个中间件，用于检查是否存在有效的 Authorization 头。

## 安装依赖项

```bash
pip install "mcp[cli]" 
```

## 启动服务器

```bash
python server.py
```

在另一个终端中启动客户端

```bash
python client.py
```

你应该会看到类似以下的结果：

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

这表示发送的凭据被允许通过。

尝试将 `client.py` 中的凭据更改为 "secret-token2"，然后你应该会在响应中看到以下文本：

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

这表示你已通过身份验证（你提供了凭据），但凭据无效。

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。