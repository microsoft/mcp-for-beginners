# 运行此示例

## -1- 安装依赖项

```bash
dotnet restore
```

## -2- 运行示例

```bash
dotnet run
```

## -3- 测试示例

在运行以下命令之前，请先启动一个单独的终端（确保服务器仍在运行）。

当服务器在一个终端中运行时，打开另一个终端并运行以下命令：

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

这将启动一个带有可视化界面的网络服务器，允许您测试该示例。

> 请确保将 **Streamable HTTP** 选为传输类型，并且 URL 为 `http://localhost:3001/mcp`。

连接到服务器后：

- 尝试列出工具并运行 `add`，参数为 2 和 4，您应该在结果中看到 6。
- 转到资源和资源模板，调用 "greeting"，输入一个名字，您应该会看到带有您提供名字的问候语。

### 在 CLI 模式下测试

您可以通过运行以下命令直接启动 CLI 模式：

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

这将列出服务器中所有可用的工具。您应该会看到以下输出：

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

要调用工具，请输入：

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

您应该会看到以下输出：

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
> 通常在 CLI 模式下运行检查器比在浏览器中快得多。
> 在 [这里](https://github.com/modelcontextprotocol/inspector) 阅读更多关于检查器的信息。

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。