# MCP計算機サーバー (Python)

Pythonで実装されたシンプルなModel Context Protocol (MCP)サーバーで、基本的な計算機能を提供します。

## インストール

必要な依存関係をインストールしてください:

```bash
pip install -r requirements.txt
```

または、MCP Python SDKを直接インストールしてください:

```bash
pip install mcp>=1.18.0
```

## 使用方法

### サーバーの起動

このサーバーはMCPクライアント（例: Claude Desktop）によって使用されるよう設計されています。サーバーを起動するには以下を実行してください:

```bash
python mcp_calculator_server.py
```

**注意**: ターミナルで直接実行すると、JSON-RPCの検証エラーが表示されます。これは正常な動作です。サーバーは適切にフォーマットされたMCPクライアントメッセージを待機しています。

### 機能のテスト

計算機能が正しく動作するかテストするには:

```bash
python test_calculator.py
```

## トラブルシューティング

### インポートエラー

`ModuleNotFoundError: No module named 'mcp'`というエラーが表示された場合は、MCP Python SDKをインストールしてください:

```bash
pip install mcp>=1.18.0
```

### サーバーを直接実行した際のJSON-RPCエラー

サーバーを直接実行した際に「Invalid JSON: EOF while parsing a value」といったエラーが表示される場合があります。これは予期された動作であり、サーバーは直接のターミナル入力ではなく、MCPクライアントメッセージを必要としています。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。