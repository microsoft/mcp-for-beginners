# このサンプルを実行する

## -1- 依存関係をインストールする

```bash
dotnet restore
```

## -3- サンプルを実行する

```bash
dotnet run
```

## -4- サンプルをテストする

サーバーを1つのターミナルで実行している状態で、別のターミナルを開き、以下のコマンドを実行してください:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

これにより、サンプルをテストできるビジュアルインターフェース付きのウェブサーバーが起動します。

サーバーが接続されたら以下を試してください:

- ツールをリストし、`add`を実行して、引数に2と4を渡してください。結果に6が表示されるはずです。
- リソースとリソーステンプレートに移動し、「greeting」を呼び出して名前を入力してください。入力した名前を使った挨拶が表示されるはずです。

### CLIモードでのテスト

以下のコマンドを実行することで、直接CLIモードで起動できます:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

これにより、サーバーで利用可能なすべてのツールがリストされます。以下のような出力が表示されるはずです:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

ツールを呼び出すには以下を入力してください:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

以下のような出力が表示されるはずです:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> 通常、CLIモードでインスペクターを実行する方がブラウザで実行するよりもはるかに高速です。
> インスペクターについての詳細は[こちら](https://github.com/modelcontextprotocol/inspector)をご覧ください。

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当方は責任を負いません。