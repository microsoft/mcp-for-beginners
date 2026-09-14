# stdio トランスポートを使った MCP サーバー

> **⚠️ 重要な更新**: MCP仕様書 2025-06-18 により、スタンドアロンの SSE (Server-Sent Events) トランスポートは<strong>非推奨</strong>となり、「Streamable HTTP」トランスポートに置き換えられました。現在の MCP 仕様では主に次の2つのトランスポート機構が定義されています：
> 1. **stdio** - 標準入出力（ローカルサーバーに推奨）
> 2. **Streamable HTTP** - SSEを内部的に使用する可能性があるリモートサーバー向け
>
> 本レッスンは、ほとんどの MCP サーバー実装に推奨される<strong>stdio トランスポート</strong>に焦点を当てて更新されています。

stdio トランスポートは、MCP サーバーが標準入力と標準出力のストリームを介してクライアントと通信するためのものです。これは、現在の MCP 仕様で最も一般的かつ推奨されるトランスポート方式であり、さまざまなクライアントアプリケーションと簡単に統合できるシンプルで効率的な方法を提供します。

## 概要

このレッスンでは、stdio トランスポートを使った MCP サーバーの構築と利用方法を解説します。

## 学習目標

このレッスン終了時には以下が可能になります：

- stdio トランスポートを使った MCP サーバーの構築
- Inspector を使った MCP サーバーのデバッグ
- Visual Studio Code での MCP サーバーの利用
- 現行 MCP トランスポート機構と stdio が推奨される理由の理解

## stdio トランスポートの仕組み

stdio トランスポートは、現行 MCP 仕様（2025-11-25）でサポートされている2つのトランスポートタイプのうちの1つです。仕組みは以下の通りです：

- <strong>シンプルな通信</strong>：サーバーは標準入力(stdin)から JSON-RPC メッセージを読み込み、標準出力(stdout)にメッセージを送信します。
- <strong>プロセスベース</strong>：クライアントが MCP サーバーをサブプロセスとして起動します。
- <strong>メッセージ形式</strong>：メッセージは個々の JSON-RPC リクエスト、通知、またはレスポンスで、改行で区切られています。
- <strong>ログ出力</strong>：サーバーは必要に応じて標準エラー(stderr)に UTF-8 文字列を書き込むことがあります。

### 重要な要件：
- メッセージは必ず改行で区切られ、埋め込み改行を含んではいけません
- サーバーは有効な MCP メッセージでないものを stdout に書き込んではいけません
- クライアントは有効な MCP メッセージでないものをサーバーの stdin に書き込んではいけません

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

上のコードでは：

- MCP SDK から `Server` クラスと `StdioServerTransport` をインポートしています
- 基本的な設定と能力を持つサーバーインスタンスを作成しています
- `StdioServerTransport` インスタンスを作成し、stdin/stdout 経由の通信を有効にするためサーバーに接続しています

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

上のコードでは：

- MCP SDK を使ってサーバーインスタンスを作成しています
- デコレーターを使ってツールを定義しています
- stdio_server コンテキストマネージャーを使用してトランスポートを処理しています

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

SSE と違う主な点は stdio サーバーが：

- Webサーバー設定や HTTP エンドポイントを必要としないこと
- クライアントがサブプロセスとして起動すること
- stdin/stdout ストリームで通信すること
- 実装とデバッグがより簡単であること

## 演習: stdio サーバーの作成

サーバーを作成するにあたり、以下のことを念頭に置きます：

- 接続とメッセージ用にエンドポイントを公開するために Web サーバーを使用する必要があります。

## 実習: 簡単な MCP stdio サーバーの作成

この実習では、推奨される stdio トランスポートを使って単純な MCP サーバーを作成します。このサーバーはクライアントが標準の Model Context Protocol を使って呼び出せるツールを公開します。

### 前提条件

- Python 3.8 以上
- MCP Python SDK：`pip install mcp`
- 非同期プログラミングの基本知識

さっそく最初の MCP stdio サーバーを作成してみましょう：

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

## 非推奨の SSE アプローチとの主な違い

**Stdio トランスポート（現在の標準）：**
- シンプルなサブプロセスモデル - クライアントがサーバーを子プロセスとして起動
- JSON-RPC メッセージを使った stdin/stdout 通信
- HTTP サーバー設定は不要
- 性能とセキュリティが向上
- デバッグと開発が容易

**SSE トランスポート（MCP 2025-06-18 以降非推奨）：**
- SSE エンドポイントを持つ HTTP サーバーが必要
- Webサーバーインフラによる複雑なセットアップ
- HTTP エンドポイントの追加セキュリティ考慮事項
- Webベースのシナリオでは Streamable HTTP に置き換えられた

### stdio トランスポートでサーバーを作る

stdio サーバー作成の基本手順は以下の通りです：

1. <strong>必要なライブラリをインポート</strong> - MCP サーバーコンポーネントと stdio トランスポート
2. <strong>サーバーインスタンスを作成</strong> - サーバーとその機能を定義
3. <strong>ツールを定義</strong> - 公開したい機能を追加
4. <strong>トランスポートをセットアップ</strong> - stdio 通信を設定
5. <strong>サーバーを起動</strong> - サーバーを開始しメッセージを処理

ステップごとに作っていきましょう：

### ステップ1: 基本的な stdio サーバーを作成

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

### ステップ2: ツールを追加

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

### ステップ3: サーバーの起動

コードを `server.py` として保存し、コマンドラインで実行します：

```bash
python server.py
```

サーバーが起動し、stdin からの入力を待機します。stdio トランスポート経由で JSON-RPC メッセージで通信します。

### ステップ4: Inspector でのテスト

MCP Inspector を使ってサーバーをテストできます：

1. Inspector をインストール：`npx @modelcontextprotocol/inspector`
2. Inspector を起動し、サーバーを指定
3. 作成したツールをテスト

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## stdio サーバーのデバッグ

### MCP Inspector の使用

MCP Inspector は MCP サーバーのデバッグとテストに役立つツールです。stdio サーバーでの使い方は以下の通り：

1. **Inspector をインストール**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector を実行**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. <strong>サーバーをテスト</strong>：Inspector のウェブインターフェースで以下が可能です：
   - サーバーの能力を表示
   - パラメーターを変えたツールのテスト
   - JSON-RPC メッセージの監視
   - 接続問題の調査

### VS Code の使用

VS Code でも直接 MCP サーバーをデバッグできます：

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
3. デバッガーを起動し、Inspector でテスト

### よくあるデバッグのヒント

- ログは `stderr` に書き、`stdout` には MCP メッセージのみを出力する
- すべての JSON-RPC メッセージが改行区切りであることを確認
- 最初は単純なツールでテストし、複雑な機能は後から追加
- Inspector を活用してメッセージ形式を検証する

## VS Code での stdio サーバーの利用

MCP stdio サーバーを作成したら、VS Code に統合して Claude などの MCP 対応クライアントで利用できます。

### 設定方法

1. `%APPDATA%\Claude\claude_desktop_config.json` (Windows) または `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) に MCP 設定ファイルを作成：

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

2. **Claude を再起動**：新設定を読み込むため Claude を閉じて再度開く

3. <strong>接続テスト</strong>：Claude と会話し、サーバーツールを試す：
   - 「greeting ツールを使って挨拶してくれる？」
   - 「15 と 27 の合計を計算して」
   - 「サーバー情報を教えて」

### TypeScript stdio サーバー例

参考のための完全な TypeScript 例：

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

本レッスンでは以下を学びました：

- 現行の **stdio トランスポート**（推奨手法）を使った MCP サーバーの構築
- SSE トランスポートが stdio と Streamable HTTP に置き換えられた理由の理解
- MCP クライアントから呼び出せるツールの作成
- MCP Inspector を使ったサーバーデバッグ
- VS Code と Claude との統合方法

stdio トランスポートは、非推奨となった SSE アプローチと比較して、より簡単で安全かつ高性能に MCP サーバーを構築できる方法です。2025-06-18 仕様以降、ほとんどの MCP サーバー実装に推奨されています。

### .NET

1. まずはツールを作成しましょう。*Tools.cs* というファイルに以下の内容を記述します：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 演習: stdio サーバーのテスト

stdio サーバーができたら、正しく動作するかテストしましょう。

### 前提条件

1. MCP Inspector がインストールされていること：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. サーバーコードが保存されていること（例：`server.py`）

### Inspector でのテスト

1. **Inspector をサーバーで起動**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. <strong>ウェブインターフェースを開く</strong>：Inspector はサーバーの能力を表示するブラウザウィンドウを開きます。

3. <strong>ツールをテスト</strong>： 
   - `get_greeting` ツールに様々な名前で呼び出し
   - `calculate_sum` ツールに異なる数値を入力
   - `get_server_info` ツールでサーバーメタデータ確認

4. <strong>通信状況を監視</strong>：Inspector でクライアントとサーバー間の JSON-RPC メッセージを確認

### 正常時に見るべき内容

サーバーが正しく起動していれば以下が見られます：
- Inspector に表示されたサーバーの能力
- テスト可能なツールの一覧
- 成功した JSON-RPC メッセージ交換
- インターフェースに表示されるツールの応答

### よくある問題と対処法

**サーバーが起動しない：**
- 必要な依存関係 (`pip install mcp`) がインストールされているか確認
- Python の構文・インデントをチェック
- コンソールのエラーメッセージを確認

**ツールが表示されない：**
- `@server.tool()` デコレータがあるか確認
- ツール関数が `main()` 実行前に定義されているか
- サーバー設定が正しく行われているか確認

**接続の問題：**
- stdio トランスポートが正しく使われているか
- 他のプロセスとの干渉がないか確認
- Inspector のコマンド構文を見直す

## 課題

自分でサーバーの機能を拡張してみましょう。例えば [このページ](https://api.chucknorris.io/) の API を呼び出すツールを追加したり、サーバーの形を自由に決めてください。楽しんで作ってみてください :)

## 解答例

[解答例](./solution/README.md) 動作するコードを含んだ一例です。

## 重要ポイント

この章での重要ポイントは以下の通りです：

- stdio トランスポートはローカル MCP サーバーに推奨される通信機構である
- stdio トランスポートにより MCP サーバーとクライアント間が標準入出力ストリームでシームレスに通信可能
- Inspector と Visual Studio Code の両方で stdio サーバーを直接利用でき、デバッグや統合が簡単に行える

## サンプル集

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## 追加リソース

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 次に学ぶこと

## 次のステップ

stdio トランスポートで MCP サーバーの作成方法を学んだので、次の応用トピックに進みましょう：

- <strong>次へ</strong>: [MCP の HTTP ストリーミング（Streamable HTTP）](../06-http-streaming/README.md) - リモートサーバー向けのもう一つのサポートトランスポートを学ぶ
- <strong>応用</strong>: [MCP セキュリティベストプラクティス](../../02-Security/README.md) - MCP サーバーのセキュリティ対策を実装
- <strong>本番用</strong>: [デプロイ戦略](../09-deployment/README.md) - 本番環境向けサーバーのデプロイ方法

## 追加リソース

- [MCP 仕様書 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/) - 公式仕様
- [MCP SDK ドキュメント](https://github.com/modelcontextprotocol/sdk) - 全言語向け SDK リファレンス
- [コミュニティサンプル](../../06-CommunityContributions/README.md) - コミュニティによる他のサーバー例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
