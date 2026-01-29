# レッスン: Web検索MCPサーバーの構築

この章では、外部APIと連携し、多様なデータタイプを扱い、エラー管理を行い、複数のツールをオーケストレーションする、実践的なAIエージェントの構築方法を紹介します。以下の内容が学べます：

- **認証が必要な外部APIとの統合**
- **複数のエンドポイントからの多様なデータタイプの処理**
- **堅牢なエラーハンドリングとログ戦略**
- **単一サーバー内でのマルチツールオーケストレーション**

このレッスンの終わりには、高度なAIやLLMを活用したアプリケーションに不可欠なパターンとベストプラクティスを実践的に習得できます。

## はじめに

このレッスンでは、SerpAPIを使ってリアルタイムのウェブデータでLLMの能力を拡張する高度なMCPサーバーとクライアントの構築方法を学びます。これは、最新情報にアクセスできる動的なAIエージェントを開発する上で重要なスキルです。

## 学習目標

このレッスンの終了時には、以下ができるようになります：

- SerpAPIのような外部APIを安全にMCPサーバーに統合する
- ウェブ検索、ニュース検索、商品検索、Q&Aの複数ツールを実装する
- LLMが扱いやすいように構造化データを解析・整形する
- エラー処理とAPIのレート制限管理を効果的に行う
- 自動化テストと対話型のMCPクライアントの構築とテスト

## Web検索MCPサーバー

このセクションでは、Web検索MCPサーバーのアーキテクチャと機能を紹介します。FastMCPとSerpAPIを組み合わせて、リアルタイムのウェブデータでLLMの能力を拡張する方法を解説します。

### 概要

この実装では、MCPが多様な外部API駆動のタスクを安全かつ効率的に処理できることを示す4つのツールを備えています：

- **general_search**：幅広いウェブ検索用
- **news_search**：最新のニュース見出し用
- **product_search**：eコマースデータ用
- **qna**：質問応答スニペット用

### 特徴
- **コード例**：Python用の言語別コードブロックを含み、他言語への拡張も容易。コードピボットで分かりやすく解説

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

クライアントを実行する前に、サーバーが何をしているか理解しておくと便利です。[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py)ファイルはMCPサーバーを実装しており、SerpAPIと連携してウェブ、ニュース、商品検索、Q&Aのツールを公開しています。リクエストの受け取り、API呼び出しの管理、レスポンスの解析、構造化された結果のクライアントへの返却を行います。

[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py)の完全な実装を確認できます。

以下はサーバーがツールを定義し登録する簡単な例です：

### Pythonサーバー

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **外部API統合**：APIキーや外部リクエストの安全な取り扱いを示す
- **構造化データ解析**：APIレスポンスをLLMに適した形式に変換する方法を解説
- **エラーハンドリング**：適切なログ出力を伴う堅牢なエラー処理
- **対話型クライアント**：自動テストと対話モードの両方を含む
- **コンテキスト管理**：MCP Contextを活用したログ記録とリクエスト追跡

## 前提条件

始める前に、以下の手順で環境を正しくセットアップしてください。これにより、依存関係がすべてインストールされ、APIキーが正しく設定されてスムーズに開発・テストが行えます。

- Python 3.8以上
- SerpAPI APIキー（[SerpAPI](https://serpapi.com/)でサインアップ - 無料プランあり）

## インストール

環境をセットアップするには、以下の手順に従ってください：

1. uv（推奨）またはpipで依存関係をインストール：

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. プロジェクトルートに`.env`ファイルを作成し、SerpAPIキーを記述：

```
SERPAPI_KEY=your_serpapi_key_here
```

## 使い方

Web検索MCPサーバーは、SerpAPIと連携してウェブ、ニュース、商品検索、Q&Aのツールを公開するコアコンポーネントです。リクエストの受け取り、API呼び出しの管理、レスポンスの解析、構造化された結果のクライアントへの返却を行います。

[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py)の完全な実装を確認できます。

### サーバーの起動

MCPサーバーを起動するには、以下のコマンドを使用します：

```bash
python server.py
```

このサーバーはstdioベースのMCPサーバーとして動作し、クライアントが直接接続できます。

### クライアントモード

クライアント（`client.py`）は、MCPサーバーとやり取りするために2つのモードをサポートしています：

- **通常モード**：すべてのツールを実行し、その応答を検証する自動テストを実行します。サーバーとツールが期待通りに動作しているか素早く確認するのに便利です。
- **対話モード**：メニュー形式のインターフェースを起動し、手動でツールを選択して呼び出し、カスタムクエリを入力し、リアルタイムで結果を確認できます。サーバーの機能を探索し、さまざまな入力で試すのに最適です。

[`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py)の完全な実装を確認できます。

### クライアントの実行

自動テストを実行するには（これによりサーバーも自動起動されます）：

```bash
python client.py
```

または対話モードで実行：

```bash
python client.py --interactive
```

### さまざまな方法でのテスト

ニーズやワークフローに応じて、サーバーが提供するツールをテスト・操作する方法はいくつかあります。

#### MCP Python SDKを使ったカスタムテストスクリプトの作成
MCP Python SDKを使って独自のテストスクリプトを作成することも可能です：

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

ここでいう「テストスクリプト」とは、MCPサーバーのクライアントとして動作するカスタムPythonプログラムのことです。正式なユニットテストではなく、プログラム的にサーバーに接続し、任意のツールを任意のパラメータで呼び出し、結果を検査できます。この方法は以下に役立ちます：

- ツール呼び出しのプロトタイピングや実験
- サーバーの異なる入力に対する応答の検証
- 繰り返しツール呼び出しの自動化
- MCPサーバー上で独自のワークフローや統合を構築

テストスクリプトを使えば、新しいクエリを素早く試したり、ツールの挙動をデバッグしたり、より高度な自動化の出発点としても活用できます。以下はMCP Python SDKを使ったスクリプト例です：

## ツールの説明

サーバーが提供する以下のツールを使って、さまざまな検索やクエリを実行できます。各ツールのパラメータと使用例を以下に示します。

このセクションでは、利用可能な各ツールの詳細とパラメータを説明します。

### general_search

一般的なウェブ検索を行い、整形された結果を返します。

**このツールの呼び出し方：**

MCP Python SDKを使ったスクリプトから、またはInspectorや対話型クライアントモードで対話的に`general_search`を呼び出せます。以下はSDKを使ったコード例です：

# [Python例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

または対話モードでは、メニューから`general_search`を選択し、プロンプトに従ってクエリを入力してください。

**パラメータ：**
- `query`（文字列）：検索クエリ

**リクエスト例：**

```json
{
  "query": "latest AI trends"
}
```

### news_search

クエリに関連する最新のニュース記事を検索します。

**このツールの呼び出し方：**

MCP Python SDKを使ったスクリプトから、またはInspectorや対話型クライアントモードで対話的に`news_search`を呼び出せます。以下はSDKを使ったコード例です：

# [Python例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

または対話モードでは、メニューから`news_search`を選択し、プロンプトに従ってクエリを入力してください。

**パラメータ：**
- `query`（文字列）：検索クエリ

**リクエスト例：**

```json
{
  "query": "AI policy updates"
}
```

### product_search

クエリに合致する商品を検索します。

**このツールの呼び出し方：**

MCP Python SDKを使ったスクリプトから、またはInspectorや対話型クライアントモードで対話的に`product_search`を呼び出せます。以下はSDKを使ったコード例です：

# [Python例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

または対話モードでは、メニューから`product_search`を選択し、プロンプトに従ってクエリを入力してください。

**パラメータ：**
- `query`（文字列）：商品検索クエリ

**リクエスト例：**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

検索エンジンから質問に対する直接的な回答を取得します。

**このツールの呼び出し方：**

MCP Python SDKを使ったスクリプトから、またはInspectorや対話型クライアントモードで対話的に`qna`を呼び出せます。以下はSDKを使ったコード例です：

# [Python例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

または対話モードでは、メニューから`qna`を選択し、プロンプトに従って質問を入力してください。

**パラメータ：**
- `question`（文字列）：回答を求める質問

**リクエスト例：**

```json
{
  "question": "what is artificial intelligence"
}
```

## コード詳細

このセクションでは、サーバーとクライアントの実装に関するコードスニペットと参照を提供します。

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

完全な実装は[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py)と[`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py)を参照してください。

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## このレッスンの高度な概念

構築を始める前に、この章で頻出する重要な高度な概念を紹介します。これらを理解しておくと、初めての方でもスムーズに学習を進められます：

- **マルチツールオーケストレーション**：ウェブ検索、ニュース検索、商品検索、Q&Aなど複数のツールを単一のMCPサーバーで動かすこと。多様なタスクを一つのサーバーで処理可能にします。
- **APIレート制限の管理**：多くの外部API（SerpAPIなど）は一定時間内のリクエスト数を制限しています。良いコードはこれを検知し、制限に達した場合もアプリが壊れないように適切に対処します。
- **構造化データ解析**：APIレスポンスは複雑でネストされていることが多いです。これをLLMや他のプログラムが扱いやすいクリーンな形式に変換する技術です。
- **エラー回復**：ネットワーク障害やAPIの予期しない応答など、問題が起きた際にコードが適切に対処し、有用なフィードバックを返すこと。クラッシュを防ぎます。
- **パラメータ検証**：ツールへの入力が正しく安全であるかをチェックすること。デフォルト値の設定や型の確認を含み、バグや混乱を防ぎます。

このセクションは、Web検索MCPサーバーを使う際に遭遇しやすい問題の診断と解決に役立ちます。エラーや予期しない動作があった場合は、まずこのトラブルシューティングを確認してください。多くの問題はここで解決できます。

## トラブルシューティング

Web検索MCPサーバーを使う際に、時折問題が発生することがあります。これは外部APIや新しいツールを使う開発ではよくあることです。このセクションでは、よくある問題とその解決策を紹介し、迅速に作業を再開できるようサポートします。エラーが発生したら、まずここを確認してください。以下のヒントは多くのユーザーが直面する問題をカバーしており、追加のサポートを求める前に解決できることが多いです。

### よくある問題

以下はユーザーがよく遭遇する問題と、その説明および解決手順です：

1. **.envファイルにSERPAPI_KEYがない**
   - `SERPAPI_KEY environment variable not found`というエラーが出た場合、アプリがSerpAPIにアクセスするためのAPIキーを見つけられていません。これを解決するには、プロジェクトルートに`.env`ファイルを作成し、`SERPAPI_KEY=your_serpapi_key_here`のように記述してください。`your_serpapi_key_here`はSerpAPIのウェブサイトで取得した実際のキーに置き換えてください。

2. **モジュールが見つからないエラー**
   - `ModuleNotFoundError: No module named 'httpx'`のようなエラーは、必要なPythonパッケージがインストールされていないことを示します。依存関係がすべてインストールされているか確認してください。解決策として、ターミナルで`pip install -r requirements.txt`を実行し、必要なパッケージをインストールしてください。

3. **接続の問題**
   - `Error during client execution`のようなエラーは、クライアントがサーバーに接続できないか、サーバーが期待通りに動作していないことを示します。クライアントとサーバーのバージョンが互換性があるか、`server.py`が正しいディレクトリで実行されているかを確認してください。サーバーとクライアントの両方を再起動することも効果的です。

4. **SerpAPIのエラー**
   - `Search API returned error status: 401`は、SerpAPIキーがない、間違っている、または期限切れであることを示します。SerpAPIのダッシュボードでキーを確認し、必要に応じて`.env`ファイルを更新してください。キーが正しいのにエラーが続く場合は、無料プランのクォータが使い切られていないか確認してください。

### デバッグモード

デフォルトでは、アプリは重要な情報のみをログに出力します。問題の詳細を確認したい場合（例えば、難しい問題の診断時など）は、DEBUGモードを有効にすると、処理の各ステップの詳細が表示されます。

**例：通常出力**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**例：DEBUG出力**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

DEBUGモードでは、HTTPリクエストやレスポンス、その他内部処理の詳細が追加で表示されます。トラブルシューティングに非常に役立ちます。
DEBUGモードを有効にするには、`client.py` または `server.py` の先頭でログレベルを DEBUG に設定してください。

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## 次に進む

- [5.10 リアルタイムストリーミング](../mcp-realtimestreaming/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。