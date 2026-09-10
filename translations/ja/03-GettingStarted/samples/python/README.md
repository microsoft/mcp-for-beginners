# MCP Calculator Server (Python)



Pythonで実装されたシンプルなModel Context Protocol（MCP）サーバーで、基本的な計算機能を提供します。


## インストール

必要な依存関係をインストールします：

```bash
pip install -r requirements.txt
```

またはMCP Python SDKを直接インストールします：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## 使い方

### サーバーの起動

サーバーはMCPクライアント（Claude Desktopなど）による利用を想定しています。サーバーを起動するには：

```bash
python mcp_calculator_server.py
```

<strong>注意</strong>：ターミナルで直接実行するとJSON-RPCの検証エラーが表示されます。これは正常な動作で、サーバーは正しい形式のMCPクライアントメッセージを待機しています。

### 関数のテスト

計算機能が正しく動作するか確認するには：

```bash
python test_calculator.py
```

## トラブルシューティング

### インポートエラー

`ModuleNotFoundError: No module named 'mcp'`が表示された場合は、MCP Python SDKをインストールしてください：

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### 直接実行時のJSON-RPCエラー

直接サーバー実行時に「Invalid JSON: EOF while parsing a value」のようなエラーが出るのは予期された現象です。サーバーはMCPクライアントのメッセージを必要とし、直接ターミナルからの入力には対応していません。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->