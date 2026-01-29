# 运行此示例

此示例涉及在客户端使用一个大型语言模型（LLM）。LLM 需要你在 Codespaces 中运行，或者在 GitHub 中设置个人访问令牌才能工作。

## -1- 安装依赖

```bash
npm install
```

## -3- 运行服务器

```bash
npm run build
```

## -4- 运行客户端

```sh
npm run client
```

你应该会看到类似以下的结果：

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。