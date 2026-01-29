# 运行此示例

建议安装 `uv`，但不是必须，详情请参见 [instructions](https://docs.astral.sh/uv/#highlights)

## -1- 安装依赖

```bash
npm install
```

## -3- 启动服务器

```bash
npm run build
```

## -4- 启动客户端

```sh
npm run client
```

你应该会看到类似以下的结果：

```text
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。