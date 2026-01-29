# このサンプルを実行する

`uv`をインストールすることを推奨しますが、必須ではありません。[手順はこちら](https://docs.astral.sh/uv/#highlights)をご覧ください。

## -1- 依存関係をインストールする

```bash
npm install
```

## -3- サンプルを実行する

```bash
npm run build
```

## -4- サンプルをテストする

サーバーを1つのターミナルで実行した状態で、別のターミナルを開き、以下のコマンドを実行してください:

```bash
npm run inspector
```

これにより、サンプルをテストできるビジュアルインターフェース付きのウェブサーバーが起動します。

サーバーが接続されたら以下を試してください:

- ツールをリストし、`add`を実行してください。引数に2と4を指定すると、結果に6が表示されるはずです。
- リソースとリソーステンプレートに移動し、「greeting」を呼び出してください。名前を入力すると、入力した名前を含む挨拶が表示されるはずです。

### CLIモードでのテスト

実行したインスペクターは実際にはNode.jsアプリであり、`mcp dev`はそのラッパーです。

以下のコマンドを実行することで、CLIモードで直接起動できます:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

これにより、サーバーで利用可能なすべてのツールがリストされます。以下のような出力が表示されるはずです:

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

ツールを呼び出すには以下を入力してください:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

以下のような出力が表示されるはずです:

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
> 通常、ブラウザで実行するよりもCLIモードでインスペクターを実行する方がはるかに高速です。
> インスペクターについての詳細は[こちら](https://github.com/modelcontextprotocol/inspector)をご覧ください。

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。