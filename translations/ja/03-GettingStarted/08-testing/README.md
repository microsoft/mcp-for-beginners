## テストとデバッグ

MCPサーバーのテストを始める前に、利用可能なツールとデバッグのベストプラクティスを理解することが重要です。効果的なテストはサーバーが期待通りに動作することを保証し、問題の迅速な特定と解決に役立ちます。以下のセクションでは、MCP実装の検証に推奨されるアプローチを説明します。

## 概要

このレッスンでは、適切なテストアプローチと最も効果的なテストツールの選択方法を扱います。

## 学習目標

このレッスンの終了時には、以下ができるようになります：

- さまざまなテストアプローチを説明できる。
- 異なるツールを使用してコードを効果的にテストできる。


## MCPサーバーのテスト

MCPは、サーバーのテストとデバッグを支援するツールを提供しています：

- **MCP Inspector**：CLIツールとしても、ビジュアルツールとしても実行可能なコマンドラインツール。
- <strong>手動テスト</strong>：curl のようなツールを使ってウェブリクエストを実行可能ですが、HTTPを実行できるツールなら何でも構いません。
- <strong>ユニットテスト</strong>：好みのテストフレームワークを使用して、サーバーとクライアントの機能をテストできます。

### MCP Inspectorの使用

このツールの使用法は前のレッスンで説明しましたが、ここでは高レベルで少し説明します。Node.jsで構築されたツールであり、`npx`実行可能ファイルを呼び出して使用します。これによりツール自体を一時的にダウンロードしてインストールし、実行後に自動でクリーンアップされます。

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) は以下を支援します：

- <strong>サーバー機能の検出</strong>：利用可能なリソース、ツール、プロンプトを自動的に検出
- <strong>ツール実行のテスト</strong>：さまざまなパラメータを試し、リアルタイムでレスポンスを確認
- <strong>サーバーメタデータの表示</strong>：サーバー情報、スキーマ、構成の検査

ツールの典型的な実行例は以下のようになります：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

上記のコマンドはMCPとそのビジュアルインターフェースを開始し、ブラウザでローカルのウェブインターフェースを起動します。登録されたMCPサーバー、それらが利用可能なツール、リソース、プロンプトを表示するダッシュボードが表示されます。このインターフェースで、ツールの実行をインタラクティブにテストし、サーバーメタデータを検査し、リアルタイムのレスポンスを確認でき、MCPサーバー実装の検証とデバッグがより容易になります。

見た目はこんな感じです: ![Inspector](../../../../translated_images/ja/connect.141db0b2bd05f096.webp)

このツールはCLIモードでも実行可能で、その場合は `--cli` 属性を追加します。以下はサーバー上のすべてのツールをリスト表示するCLIモードの実行例です：

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### 手動テスト

インスペクターツールを使ってサーバー機能をテストする以外に、curlのようなHTTPを利用できるクライアントを使う方法もあります。

curlを使うと、HTTPリクエストでMCPサーバーを直接テストできます：

```bash
# 例：テストサーバーメタデータ
curl http://localhost:3000/v1/metadata

# 例：ツールを実行する
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

上記のcurlの使用例からわかる通り、ツール名とパラメータを含むペイロードを使ってPOSTリクエストでツールを呼び出しています。最適な方法を選んでください。CLIツールは通常操作が速く、スクリプト化しやすいためCI/CD環境で役立ちます。

### ユニットテスト

ツールやリソースのユニットテストを作成して正しく動作することを保証しましょう。以下はテストコードの例です。

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# モジュール全体を非同期テスト用にマークする
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # いくつかのテストツールを作成する
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # カーソルパラメータなしでテスト（省略）
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # cursor=Noneでテストする
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # 文字列としてのカーソルでテストする
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # 空文字列のカーソルでテストする
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

上記コードは次のことを行っています：

- pytestフレームワークを利用し、関数としてテストを作成してassert文を使う。
- 2つの異なるツールを持つMCPサーバーを作成。
- `assert`文で特定の条件が満たされているかチェック。

[こちらでファイル全体を確認できます](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

上記ファイルを参考にして、ご自身のサーバーをテストし、機能が正しく構築されているかを確認できます。

主要なSDKには同様のテストセクションがあるため、使用しているランタイムに合わせて調整可能です。

## サンプル

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## 追加リソース

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 次に学ぶこと

- 次： [デプロイメント](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の母国語版が権威ある情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->