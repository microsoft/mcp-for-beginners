# サンプルの実行方法

`uv`をインストールすることを推奨しますが、必須ではありません。[インストール手順](https://docs.astral.sh/uv/#highlights)をご覧ください。

## -0- 仮想環境を作成する

```bash
python -m venv venv
```

## -1- 仮想環境を有効化する

```bash
venv\Scripts\activate
```

## -2- 依存関係をインストールする

```bash
pip install "mcp[cli]"
```

## -3- サンプルを実行する

```bash
mcp run server.py
```

## -4- サンプルをテストする

サーバーを1つのターミナルで起動した状態で、別のターミナルを開き、以下のコマンドを実行してください:

```bash
mcp dev server.py
```

これにより、視覚的なインターフェースを備えたウェブサーバーが起動し、サンプルをテストできるようになります。

サーバーが接続されたら:

- ツールの一覧を表示し、`add`を実行してください。引数に2と4を指定すると、結果に6が表示されるはずです。

- リソースとリソーステンプレートに移動し、`get_greeting`を呼び出してください。名前を入力すると、入力した名前を含む挨拶が表示されるはずです。

### CLIモードでのテスト

実行したインスペクターは実際にはNode.jsアプリであり、`mcp dev`はそのラッパーです。

以下のコマンドを実行することで、CLIモードで直接起動できます:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

これにより、サーバーで利用可能なすべてのツールが一覧表示されます。以下の出力が表示されるはずです:

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
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

以下の出力が表示されるはずです:

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
> インスペクターをブラウザで実行するよりも、CLIモードで実行する方が通常はかなり高速です。
> インスペクターについての詳細は[こちら](https://github.com/modelcontextprotocol/inspector)をご覧ください。

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。