# サンプルを実行する

このサンプルでは、有効なAuthorizationヘッダーを確認するミドルウェアを使用してMCPサーバーを起動します。

## 依存関係をインストールする

```bash
pip install "mcp[cli]" 
```

## サーバーを起動する

```bash
python server.py
```

別のターミナルでクライアントを起動します

```bash
python client.py
```

次のような結果が表示されるはずです:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

これは、送信された認証情報が許可されていることを意味します。

`client.py`内の認証情報を"secret-token2"に変更してみてください。すると、レスポンスの一部として次のテキストが表示されるはずです:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

これは、認証情報が送信された（認証情報があった）が、それが無効であったことを意味します。

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源とみなしてください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。