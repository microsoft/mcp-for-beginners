# このサンプルの実行

`uv` のインストールを推奨しますが、必須ではありません。詳しくは [instructions](https://docs.astral.sh/uv/#highlights) をご覧ください。

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
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  file
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。