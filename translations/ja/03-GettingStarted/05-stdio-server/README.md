# stdio トランスポートを使った MCP サーバー

> **⚠️ 重要なアップデート**: MCP仕様 2025-06-18 の時点で、単独の SSE (Server-Sent Events) トランスポートは <strong>非推奨</strong> となり、「Streamable HTTP」トランスポートに置き換えられました。現行の MCP 仕様では、主要な２つのトランスポートメカニズムが定義されています:
> 1. **stdio** - 標準入力／出力（ローカルサーバーに推奨）
> 2. **Streamable HTTP** - SSE を内部的に使う可能性のあるリモートサーバー向け
>
> 本レッスンは、ほとんどの MCP サーバー実装に推奨される **stdio トランスポート** に焦点を当てて更新されています。

stdio トランスポートを使用することで、MCP サーバーは標準入力および標準出力ストリームを通じてクライアントと通信できます。これは MCP 仕様で最も一般的かつ推奨されるトランスポートであり、様々なクライアントアプリケーションと簡単に統合可能なシンプルかつ効率的な MCP サーバー構築手法です。

## 概要

このレッスンでは、stdio トランスポートを用いて MCP サーバーを構築し、利用する方法を解説します。

## 学習目標

このレッスンを終える頃には、以下ができるようになります:

- stdio トランスポートを使って MCP サーバーを構築する。
- Inspector を使って MCP サーバーのデバッグを行う。
- Visual Studio Code から MCP サーバーを利用する。
- 現行 MCP のトランスポートメカニズムと stdio 推奨の理由を理解する。


## stdio トランスポート - 動作原理

stdio トランスポートは MCP 仕様
`2026-07-28` における 2 つの標準トランスポートの一つです。動作は以下の通りです:

- <strong>シンプルな通信</strong>: サーバーは標準入力(`stdin`)から JSON-RPC メッセージを読み取り、標準出力(`stdout`)へメッセージを送信します。
- <strong>プロセスベース</strong>: クライアントが MCP サーバーをサブプロセスとして起動します。
- <strong>メッセージ形式</strong>: メッセージは個別の JSON-RPC リクエスト、通知、またはレスポンスであり、改行で区切られます。
- <strong>ログ出力</strong>: サーバーはログのために標準エラー(`stderr`)へ UTF-8 文字列を出力してもよいです。

### 主要要件:
- メッセージは必ず改行で区切られ、埋め込み改行を含んではいけません
- サーバーは有効な MCP メッセージ以外を `stdout` に書き込んではいけません
- クライアントは有効な MCP メッセージ以外をサーバーの `stdin` に書き込んではいけません

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

前述のコードでは:

- MCP SDK から `Server` クラスと `StdioServerTransport` をインポートしています
- 基本設定と機能を持ったサーバーインスタンスを作成しています
- `StdioServerTransport` インスタンスを作成し、サーバーを標準入出力で通信可能に接続しています

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

上記コードでは:

- MCP SDK を使ってサーバーインスタンスを作成しています
- デコレーターでツールを定義しています
- stdio_server コンテキストマネージャーを使ってトランスポートを管理しています

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

SSE との主な違いは stdio サーバーは:

- ウェブサーバー設定や HTTP エンドポイントを必要としません
- クライアントによりサブプロセスとして起動されます
- 標準入力・出力ストリームで通信します
- 実装やデバッグが簡単です

## 演習: stdio サーバーの作成

サーバー作成にあたり以下を念頭に置きます:

- 接続やメッセージ用のエンドポイントを公開するにはウェブサーバーを使う必要があります。
## ラボ: 簡単な MCP stdio サーバーの作成

このラボでは、推奨される stdio トランスポートを用いてシンプルな MCP サーバーを作成します。クライアントが標準の Model Context Protocol を使って呼び出せるツールを公開します。

### 前提条件

- Python 3.8 以上
- MCP Python SDK: `pip install mcp`
- 非同期プログラミングの基礎知識

まずは初めての MCP stdio サーバーを作ってみましょう:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# ロギングを構成する
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

**Stdio トランスポート（現在の標準）:**
- シンプルなサブプロセスモデル - クライアントがサーバーを子プロセスとして起動
- JSON-RPC メッセージを標準入出力で通信
- HTTP サーバー設定不要
- パフォーマンスとセキュリティが向上
- デバッグと開発が容易

**SSE トランスポート（MCP 2025-06-18 で非推奨）:**
- SSE エンドポイント付き HTTP サーバーが必要
- ウェブサーバーインフラの複雑なセットアップ
- HTTP エンドポイントの追加セキュリティ考慮
- 現在はウェブベース用途のため Streamable HTTP に置き換え済み

### stdio トランスポートのサーバー作成

stdio サーバーを作成するには:

1. <strong>必要なライブラリをインポート</strong> - MCP サーバー部品と stdio トランスポートを使用
2. <strong>サーバーインスタンスを作成</strong> - 機能を定義
3. <strong>ツールを定義</strong> - 公開したい機能を追加
4. <strong>トランスポートを設定</strong> - stdio 通信を構成
5. <strong>サーバーを起動</strong> - メッセージを処理しながらサーバーを実行

一つずつ順番に進めていきましょう:

### ステップ 1: 基本的な stdio サーバーを作成

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

### ステップ 2: さらにツールを追加

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

### ステップ 3: サーバーの起動

コードを `server.py` として保存し、コマンドラインから実行してください:

```bash
python server.py
```

サーバーは起動して標準入力からの入力を待機します。stdio トランスポートを通じて JSON-RPC メッセージで通信します。

### ステップ 4: Inspector でのテスト

MCP Inspector を使ってサーバーをテストできます:

1. Inspector をインストール: `npx @modelcontextprotocol/inspector`
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

MCP Inspector は MCP サーバーのデバッグとテストに役立つツールです。stdio サーバーでの使い方は以下の通りです:

1. **Inspector をインストール**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector を起動**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. <strong>サーバーをテスト</strong>: Inspector のウェブインターフェースで以下ができます:
   - サーバーの機能表示
   - さまざまなパラメーターでツールをテスト
   - JSON-RPC メッセージの監視
   - 接続の問題をデバッグ

### VS Code の使用

VS Code 内でも MCP サーバーのデバッグが可能です:

1. `.vscode/launch.json` に起動設定を作成:
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
3. デバッガーを実行し、Inspector と併用してテスト

### 一般的なデバッグのコツ

- ログには `stderr` を使う - `stdout` は MCP メッセージ専用で絶対に使わない
- 全ての JSON-RPC メッセージが改行区切りであることを確認
- 複雑な機能追加前にまずシンプルなツールでテスト
- Inspector でメッセージ形式を検証

## VS Code での stdio サーバー利用

MCP stdio サーバーを構築したら、Claude や他の MCP 対応クライアントとの連携のため VS Code に統合できます。

### 設定方法

1. MCP 設定ファイルを `%APPDATA%\Claude\claude_desktop_config.json`（Windows）または `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）に作成:

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

2. Claude を再起動し、新サーバー設定を読み込みます。

3. 接続テスト: Claude との会話を開始し、サーバーのツールを試します:
   - 「greeting ツールで挨拶してくれますか？」
   - 「15 と 27 の合計を計算して」
   - 「サーバー情報は？」

### TypeScript stdio サーバーの例

参考用の TypeScript 完全例です:

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

### .NET stdio サーバーの例

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

この更新レッスンで学んだこと:

- 現行の **stdio トランスポート**（推奨手法）を用いた MCP サーバーの構築
- SSE トランスポートが stdio と Streamable HTTP に置き換えられた理由の理解
- MCP クライアントが呼び出せるツールの作成
- MCP Inspector を使ったサーバーのデバッグ
- VS Code と Claude との統合による stdio サーバーの活用

stdio トランスポートは、非推奨となった SSE アプローチに比べてシンプルでセキュアかつ高性能な MCP サーバー構築方法を提供し、2025-06-18 仕様以降ほとんどの MCP サーバー実装に推奨されています。


### .NET

1. まずはツールをいくつか作成しましょう。*Tools.cs* ファイルに以下の内容を記述します:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 演習: stdio サーバーのテスト

stdio サーバーを構築したので、正常に動作するかテストしましょう。

### 前提条件

1. MCP Inspector がインストールされていることを確認:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. サーバーコードが保存されていること（例: `server.py`）

### Inspector でのテスト

1. **Inspector をサーバー付きで起動**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. <strong>ウェブインターフェースを開く</strong>: Inspector がブラウザを開き、サーバーの機能を表示します。

3. <strong>ツールをテスト</strong>:
   - `get_greeting` ツールを様々な名前で試す
   - `calculate_sum` ツールを色々な数値でテスト
   - `get_server_info` ツールを呼び出し、サーバーのメタデータを確認

4. <strong>通信を監視</strong>: Inspector はクライアントとサーバー間の JSON-RPC メッセージを表示します。

### 見られるべきもの

正常に起動した場合、以下が確認できます:
- Inspector 内でサーバーの機能一覧
- テスト可能なツール
- 成功した JSON-RPC メッセージの交換
- インターフェースに返されたツールのレスポンス

### よくある問題と解決策

**サーバーが起動しない:**
- 依存関係が全てインストールされているか確認: `pip install mcp`
- Python の文法エラーやインデントを確認
- コンソールのエラーメッセージを確認

**ツールが表示されない:**
- `@server.tool()` デコレーターの有無を確認
- `main()` より前にツール関数が定義されているか確認
- サーバーが正しく設定されているか確認

**接続問題:**
- サーバーが stdio トランスポートを正しく使っているか確認
- 他のプロセスが干渉していないか確認
- Inspector のコマンド構文を確認

## 課題

さらに機能を充実させたサーバーを構築してみてください。[こちらのページ](https://api.chucknorris.io/)などを参考に、API を呼び出すツールを追加するのも良いでしょう。サーバーの仕様はあなた次第です。楽しんでください :)
## 解答例

[解答例](./solution/README.md) 動作するコードを含む一例です。

## 重要なポイント

本章の重要なポイントは以下です:

- stdio トランスポートはローカル MCP サーバーに推奨される仕組みです。
- 標準入力・出力ストリームを使い MCP サーバーとクライアント間でシームレスに通信できます。
- Inspector と Visual Studio Code の両方を使って stdio サーバーを直接利用でき、デバッグや統合が簡単です。

## サンプル 

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python) 

## 追加リソース

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 次に進むべきこと

## 次のステップ

stdio トランスポートを使った MCP サーバー構築を学んだら、より高度なトピックに進みましょう:

- <strong>次へ</strong>: [MCP の HTTP ストリーミング (Streamable HTTP)](../06-http-streaming/README.md) - リモートサーバー向けの他のトランスポートメカニズムを学ぶ
- <strong>上級</strong>: [MCP セキュリティのベストプラクティス](../../02-Security/README.md) - MCP サーバーにセキュリティを実装
- <strong>本番</strong>: [デプロイ戦略](../09-deployment/README.md) - サーバーを本番環境へ展開

## 追加リソース

- [MCP 仕様 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - 現行仕様
- [MCP SDK ドキュメント](https://github.com/modelcontextprotocol/sdk) - 全言語向け SDK リファレンス
- [コミュニティ例](../../06-CommunityContributions/README.md) - コミュニティによるさらに多くのサーバー例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
