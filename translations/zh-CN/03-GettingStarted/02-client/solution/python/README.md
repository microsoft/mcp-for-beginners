# 运行此示例

建议安装 `uv`，但不是必须，详见 [说明](https://docs.astral.sh/uv/#highlights)

## -0- 创建虚拟环境

```bash
python -m venv venv
```

## -1- 激活虚拟环境

```bash
venv\Scripts\activate
```

## -2- 安装依赖

```bash
pip install "mcp[cli]"
```

## -3- 运行示例

```bash
python client.py
```

你应该会看到类似以下的输出：

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->