# 运行此示例

建议安装 `uv`，但不是必须的，详见 [说明](https://docs.astral.sh/uv/#highlights)

## -0- 创建虚拟环境

```bash
python -m venv venv
```

## -1- 激活虚拟环境

```bash
venv\Scripts\activate
```

## -2- 安装依赖项

```bash
pip install "mcp[cli]"
```

## -3- 运行示例

```bash
mcp run server.py
```

## -4- 测试示例

在一个终端中运行服务器后，打开另一个终端并运行以下命令：

```bash
mcp dev server.py
```

这将启动一个带有可视化界面的网络服务器，允许你测试该示例。

服务器连接后：

- 尝试列出工具并运行 `add`，参数为 2 和 4，你应该在结果中看到 6。

- 转到资源和资源模板，调用 `get_greeting`，输入一个名字，你应该会看到包含你提供的名字的问候语。

### 在 CLI 模式下测试

你运行的 inspector 实际上是一个 Node.js 应用程序，而 `mcp dev` 是它的一个封装。

你可以通过运行以下命令直接以 CLI 模式启动它：

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

这将列出服务器中所有可用的工具。你应该会看到以下输出：

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

要调用某个工具，请输入：

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

你应该会看到以下输出：

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> 通常在 CLI 模式下运行 inspector 比在浏览器中快得多。
> 在 [这里](https://github.com/modelcontextprotocol/inspector) 阅读更多关于 inspector 的信息。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。