# このサンプルを実行する

以下は、Pythonを使用してクラシックなHTTPストリーミングサーバーとクライアント、そしてMCPストリーミングサーバーとクライアントを実行する方法です。

### 概要

- MCPサーバーをセットアップし、アイテムを処理する際に進捗通知をクライアントにストリーム配信します。
- クライアントは各通知をリアルタイムで表示します。
- このガイドでは、前提条件、セットアップ、実行、トラブルシューティングについて説明します。

### 前提条件

- Python 3.9以上
- `mcp` Pythonパッケージ（`pip install mcp`でインストール）

### インストールとセットアップ

1. リポジトリをクローンするか、ソリューションファイルをダウンロードします。

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **仮想環境を作成して有効化します（推奨）：**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **必要な依存関係をインストールします：**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### ファイル

- **サーバー:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **クライアント:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### クラシックHTTPストリーミングサーバーの実行

1. ソリューションディレクトリに移動します：

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. クラシックHTTPストリーミングサーバーを起動します：

   ```pwsh
   python server.py
   ```

3. サーバーが起動し、以下が表示されます：

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### クラシックHTTPストリーミングクライアントの実行

1. 新しいターミナルを開きます（同じ仮想環境とディレクトリを有効化）：

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. ストリームされたメッセージが順次表示されるのを確認できます：

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### MCPストリーミングサーバーの実行

1. ソリューションディレクトリに移動します：
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. MCPサーバーをstreamable-httpトランスポートで起動します：
   ```pwsh
   python server.py mcp
   ```
3. サーバーが起動し、以下が表示されます：
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCPストリーミングクライアントの実行

1. 新しいターミナルを開きます（同じ仮想環境とディレクトリを有効化）：
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. サーバーが各アイテムを処理する際に通知がリアルタイムで表示されるのを確認できます：
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### 主な実装ステップ

1. **FastMCPを使用してMCPサーバーを作成します。**
2. **リストを処理し、`ctx.info()`または`ctx.log()`を使用して通知を送信するツールを定義します。**
3. **`transport="streamable-http"`でサーバーを実行します。**
4. **通知を受信時に表示するメッセージハンドラーを持つクライアントを実装します。**

### コードの解説
- サーバーは非同期関数とMCPコンテキストを使用して進捗更新を送信します。
- クライアントは非同期メッセージハンドラーを実装し、通知と最終結果を表示します。

### ヒントとトラブルシューティング

- 非同期操作には`async/await`を使用してください。
- サーバーとクライアントの両方で例外を適切に処理し、堅牢性を確保してください。
- 複数のクライアントでテストを行い、リアルタイム更新を確認してください。
- エラーが発生した場合は、Pythonのバージョンを確認し、すべての依存関係がインストールされていることを確認してください。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当社は一切の責任を負いません。