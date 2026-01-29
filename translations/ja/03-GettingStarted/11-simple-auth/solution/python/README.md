# サンプルを実行する

## 環境を作成する

```sh
python -m venv venv
source ./venv/bin/activate
```

## 依存関係をインストールする

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## トークンを生成する

クライアントがサーバーと通信するために使用するトークンを生成する必要があります。

以下を呼び出します:

```sh
python util.py
```

## コードを実行する

以下のコマンドでコードを実行します:

```sh
python server.py
```

別のターミナルで以下を入力します:

```sh
python client.py
```

サーバーのターミナルには以下のような内容が表示されるはずです:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

クライアントのウィンドウには以下のようなテキストが表示されるはずです:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

これで全てが正常に動作していることを意味します。

### 情報を変更して失敗する様子を確認する

*server.py* 内の以下のコードを探します:

```python
 if not has_scope(has_header, "Admin.Write"):
```

これを "User.Write" と表示されるように変更してください。現在のトークンにはその権限レベルが含まれていないため、サーバーを再起動してクライアントをもう一度実行しようとすると、サーバーのターミナルに以下のようなエラーが表示されるはずです:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

サーバーコードを元に戻すか、この追加のスコープを含む新しいトークンを生成するか、どちらかを選んでください。

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。