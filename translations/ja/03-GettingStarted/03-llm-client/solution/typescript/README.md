# このサンプルの実行

このサンプルではクライアント側にLLMを用います。LLMを動かすには、Codespacesで実行するか、GitHubでパーソナルアクセストークンを設定する必要があります。

## -1- 依存関係のインストール

```bash
npm install
```

## -3- サーバーの起動

```bash
npm run build
```

## -4- クライアントの起動

```sh
npm run client
```

以下のような結果が表示されるはずです：

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。