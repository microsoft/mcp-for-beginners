# 运行示例

> [!WARNING]
> 此示例使用了弃用的 Sampling 及传统的 HTTP+SSE 端点。
> 保留此示例以兼容 MCP `2025-11-25`。
> 新实现应直接调用 LLM 提供商并使用 Streamable HTTP 进行远程 MCP 流量。

## 创建虚拟环境

```sh
python -m venv venv
source ./venv/bin/activate
```

## 安装依赖

```sh
pip install "mcp[cli]"
```

## 启动服务器

```sh
uvicorn server:app --port 8000
```

## 使用 GitHub Copilot 和 VS Code 测试服务器

按如下方式将条目添加到 mcp.json：

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

确保点击服务器上的“start”按钮。

在 GitHub Copilot 中粘贴以下提示：

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

第一次会询问是否接受 Sampling 操作，然后会要求接受运行名为 “create_blog” 的工具。你应该看到类似的响应：

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->