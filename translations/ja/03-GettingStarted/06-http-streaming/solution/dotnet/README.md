# サンプルの実行

## -1- 依存関係のインストール

```bash
dotnet restore
```

## -2- サンプルの実行

```bash
dotnet run
```

## -3- サンプルのテスト

以下を実行する前に、別のターミナルを開いてください（サーバーがまだ稼働していることを確認してください）。

サーバーが1つのターミナルで稼働している状態で、別のターミナルを開き、以下のコマンドを実行してください:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

これにより、視覚的なインターフェースを備えたウェブサーバーが起動し、サンプルをテストできるようになります。

> **Streamable HTTP** がトランスポートタイプとして選択されていることを確認し、URLが `http://localhost:3001/mcp` であることを確認してください。

サーバーが接続されたら:

- ツールの一覧を表示し、`add` を実行してください。引数に2と4を指定すると、結果に6が表示されるはずです。
- リソースとリソーステンプレートに移動し、「greeting」を呼び出してください。名前を入力すると、入力した名前を含む挨拶が表示されるはずです。

### CLIモードでのテスト

以下のコマンドを実行することで、直接CLIモードで起動できます:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

これにより、サーバーで利用可能なすべてのツールが一覧表示されます。以下の出力が表示されるはずです:

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

ツールを呼び出すには、以下を入力してください:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
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
> 通常、ブラウザでインスペクターを実行するよりもCLIモードで実行する方がはるかに高速です。
> インスペクターについての詳細は [こちら](https://github.com/modelcontextprotocol/inspector) を参照してください。

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。