# stdio トランスポートによる MCP サーバー

> **⚠️ 重要なお知らせ**: MCP仕様 2025-06-18 現在では、独立した SSE（Server-Sent Events）トランスポートは**非推奨**となり、「Streamable HTTP」トランスポートに置き換えられています。現在の MCP 仕様では主なトランスポート機構が２つ定義されています:
> 1. **stdio** - 標準入出力（ローカルサーバーで推奨）
> 2. **Streamable HTTP** - 内部で SSE を利用するリモートサーバー向け
>
> 本レッスンは、ほとんどの MCP サーバー実装で推奨される **stdio トランスポート** に焦点をあてて更新されています。

stdio トランスポートは MCP サーバーが標準入出力ストリームを通じてクライアントと通信できるようにします。これは現在の MCP 仕様で最もよく使われ推奨されるトランスポート機構で、様々なクライアントアプリケーションと簡単に統合できるシンプルかつ効率的な方法です。

## 概要

本レッスンでは stdio トランスポートを使って MCP サーバーを構築し利用する方法を解説します。

## 学習目標

本レッスンの終了時には以下ができるようになります：

- stdio トランスポートを使って MCP サーバーを構築する
- Inspector を使って MCP サーバーのデバッグを行う
- Visual Studio Code を使って MCP サーバーを利用する
- 現在の MCP トランスポート機構の理解と stdio が推奨される理由を把握する

## stdio トランスポート - 動作の仕組み

stdio トランスポートは現在（2025-06-18）の MCP 仕様でサポートされる２つのトランスポートタイプの一つです。動作の概要は以下の通り：

- **シンプルな通信**: サーバーは標準入力（`stdin`）から JSON-RPC メッセージを読み取り、標準出力（`stdout`）にメッセージを送信する。
- **プロセスベース**: クライアントが MCP サーバーをサブプロセスとして起動する。
- **メッセージ形式**: メッセージは JSON-RPC のリクエスト、通知、応答で、それぞれ改行で区切られる。
- **ログ記録**: サーバーは UTF-8 文字列を標準エラー（`stderr`）に書き出してログに利用してもよい。

### 主な要件:
- メッセージは改行で区切られ、メッセージ内に改行を含んではいけない
- サーバーは有効な MCP メッセージ以外を `stdout` に書き込んではいけない
- クライアントは有効な MCP メッセージ以外をサーバーの `stdin` に書き込んではいけない

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

上記のコードでは：

- MCP SDK から `Server` クラスと `StdioServerTransport` をインポートしている
- 基本的な設定と機能を持つサーバーインスタンスを生成している

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# サーバーインスタンスを作成する
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

上記のコードでは：

- MCP SDK を使ってサーバーインスタンスを作成している
- デコレータでツールを定義している
- stdio_server コンテキストマネージャーでトランスポートを処理している

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

SSE との主な違いは stdio サーバーは：

- Web サーバーの設定や HTTP エンドポイントを必要としない
- クライアントによってサブプロセスとして起動される
- stdin/stdout ストリーム経由で通信する
- 実装やデバッグがより簡単である

## 演習：stdio サーバーを作成する

サーバーを作成する際には２点を留意します：

- 接続やメッセージ用のエンドポイントを公開するための Web サーバーは不要である。

## ラボ：シンプルな MCP stdio サーバーを作ろう

このラボでは推奨される stdio トランスポートを使ってシンプルな MCP サーバーを作成します。このサーバーはクライアントが標準の Model Context Protocol を使って呼び出せるツールを公開します。

### 前提条件

- Python 3.8 以上
- MCP Python SDK：`pip install mcp`
- 非同期プログラミングの基本知識

まずは最初の MCP stdio サーバーを作成しましょう：

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# ロギングを設定する
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# サーバーを作成する
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # stdioトランスポートを使用する
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## 非推奨の SSE 方式との主な違い

**Stdio トランスポート（現在の標準）:**
- シンプルなサブプロセスモデル - クライアントがサーバーを子プロセスとして起動
- stdin/stdout 経由での JSON-RPC メッセージ通信
- HTTP サーバーのセットアップ不要
- 高いパフォーマンスとセキュリティ
- デバッグと開発が容易

**SSE トランスポート（2025-06-18 で非推奨）:**
- SSE エンドポイントを持つ HTTP サーバーが必要
- Web サーバーインフラ構築が複雑
- HTTP エンドポイントのセキュリティ対応が追加で必要
- Web ベースシナリオでは現在 Streamable HTTP に置き換え済み

### stdio トランスポートでのサーバー作成手順

stdio サーバーを作成するには：

1. **必要なライブラリをインポート** - MCP サーバーコンポーネントと stdio トランスポート
2. **サーバーインスタンスを作成** - 機能（capabilities）を定義
3. **ツールを定義** - 公開する機能を追加
4. **トランスポート設定** - stdio 通信の設定
5. **サーバー実行** - サーバーを起動しメッセージ処理

順を追って構築しましょう。

### ステップ1: 基本的な stdio サーバーの作成

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ロギングを設定する
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# サーバーを作成する
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### ステップ2: ツールを追加する

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### ステップ3: サーバーを実行する

コードを `server.py` として保存し、コマンドラインで実行します：

```bash
python server.py
```

サーバーは起動して stdin からの入力を待ちます。stdio トランスポートを使い JSON-RPC メッセージで通信します。

### ステップ4: Inspector でテストする

MCP Inspector を使ってサーバーをテストできます：

1. Inspector をインストール: `npx @modelcontextprotocol/inspector`
2. Inspector を起動しサーバーを指定
3. 作成したツールをテストする

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## stdio サーバーのデバッグ

### MCP Inspector の使用方法

MCP Inspector は MCP サーバーのデバッグやテストに有用なツールです。stdio サーバーとどう使うか以下の手順：

1. **Inspector のインストール**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector の起動**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **サーバーのテスト**: Inspector はウェブインターフェースを提供し以下を行えます：
   - サーバーの機能を表示
   - さまざまなパラメータでツールをテスト
   - JSON-RPC メッセージの監視
   - 接続問題のデバッグ

### VS Code を使う

VS Code で MCP サーバーを直接デバッグできます：

1. `.vscode/launch.json` に起動構成を作成：
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. サーバーコードにブレークポイントを設定
3. デバッガを起動し Inspector でテスト

### デバッグの一般的なコツ

- ログには `stderr` を使い、`stdout` には MCP メッセージのみ書き込む
- JSON-RPC メッセージは必ず改行区切りにする
- 最初は単純なツールで動作確認し、複雑な機能はあとで追加する
- Inspector でメッセージ形式を検証する

## VS Code で stdio サーバーを利用する

MCP stdio サーバーを構築したら、VS Code と統合して Claude や他の MCP クライアントで利用できます。

### 設定方法

1. MCP 設定ファイルを `%APPDATA%\Claude\claude_desktop_config.json`（Windows）または `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）に作成：

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. Claude を再起動して新しいサーバー設定を読み込む

3. 接続テスト：Claude と会話を開始し、サーバーのツールを試す：
   - 「greeting ツールで挨拶してくれますか？」
   - 「15 と 27 の合計を計算してください」
   - 「サーバー情報は何ですか？」

### TypeScript stdio サーバー例

参考用に TypeScript の完全な例です：

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// ツールを追加する
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET stdio サーバー例

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## まとめ

本更新レッスンで学んだこと：

- 現在推奨される **stdio トランスポート** を使った MCP サーバー構築方法
- SSE トランスポートが stdio と Streamable HTTP に置き換えられた理由
- MCP クライアントから呼び出せるツールの作成方法
- MCP Inspector によるサーバーデバッグ
- VS Code と Claude への stdio サーバー統合

stdio トランスポートは deprecated となった SSE 方式に比べてシンプルで安全かつ高性能な MCP サーバー構築手段であり、2025-06-18 仕様時点で最も推奨されるトランスポートです。

### .NET

1. まずはツールをいくつか作成します。そのために *Tools.cs* というファイルに以下の内容を記述します：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 演習：stdio サーバーの動作確認

stdio サーバーが完成したら、正しく動作するかテストしましょう。

### 前提条件

1. MCP Inspector がインストールされていること：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. サーバーコードが保存されていること（例：`server.py`）

### Inspector でのテスト

1. **サーバーと共に Inspector を起動**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **ウェブインターフェースを開く**: Inspector はブラウザを開き、サーバーの機能を表示

3. **ツールをテスト**:
   - `get_greeting` ツールを様々な名前で試す
   - `calculate_sum` ツールを色々な数字で試す
   - `get_server_info` ツールを呼び出しサーバーメタデータを確認

4. **通信の監視**: Inspector はクライアントとサーバー間の JSON-RPC メッセージ送受信を表示

### 正常時に見るもの

サーバーが正常に起動すると：

- Inspector にサーバー機能が表示される
- テスト可能なツールがリストアップされる
- JSON-RPC のメッセージ交換が成功する
- インターフェースにツールの応答が表示される

### よくある問題と解決法

**サーバーが起動しない場合:**
- 依存モジュールがすべてインストール済みか確認：`pip install mcp`
- Python の構文とインデントをチェック
- コンソールのエラーメッセージを確認

**ツールが表示されない場合:**
- `@server.tool()` デコレータの存在を確認
- ツール関数が `main()` より前に定義されているか確認
- サーバー設定が正しいか確認

**接続の問題:**
- サーバーが stdio トランスポートを正しく使っているか確認
- 他のプロセスの干渉がないか確認
- Inspector のコマンドの構文を確認

## 課題

更に機能を増やしたサーバーを構築してみましょう。例えば [このページ](https://api.chucknorris.io/) を参照して API を呼び出すツールの作成も可能です。サーバーの形は自由に決めてください。楽しんで！

## 解答例

[解答例](./solution/README.md) には動作するコードの一例があります。

## 重要なポイント

この章の重要なポイントは以下です：

- stdio トランスポートはローカル MCP サーバーに推奨される機構である
- stdio トランスポートにより標準入出力ストリームで MCP サーバーとクライアントがシームレスに通信できる
- Inspector と Visual Studio Code の両方で stdio サーバーを直接利用できるため、デバッグや統合が容易である

## サンプル

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## 追加リソース

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 次に学ぶこと

## 次のステップ

stdio トランスポートを使った MCP サーバー構築を学んだら、次の高度なテーマに進みましょう：

- **次へ**: [MCP による HTTP ストリーミング (Streamable HTTP)](../06-http-streaming/README.md) - リモートサーバー向けの他のトランスポート機構について学ぶ
- **応用**: [MCP セキュリティのベストプラクティス](../../02-Security/README.md) - MCP サーバーのセキュリティ強化
- **本番環境**: [デプロイメント戦略](../09-deployment/README.md) - 本番運用のためのサーバー公開方法

## 追加リソース

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 公式仕様書
- [MCP SDK ドキュメント](https://github.com/modelcontextprotocol/sdk) - 各言語の SDK 参照
- [コミュニティによる例](../../06-CommunityContributions/README.md) - コミュニティによるサーバー例集

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる場合があることをご留意ください。原文はその言語における正式な原典として扱われるべきものです。重要な情報については、専門の人による翻訳を推奨します。本翻訳の使用により生じた誤解や解釈の相違について、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->