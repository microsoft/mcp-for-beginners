# MCPサーバーとstdioトランスポート

> **⚠️ 重要な更新情報**: MCP仕様2025-06-18より、独立したSSE（Server-Sent Events）トランスポートは**非推奨**となり、「Streamable HTTP」トランスポートに置き換えられました。現在のMCP仕様では、以下の2つの主要なトランスポートメカニズムが定義されています：
> 1. **stdio** - 標準入力/出力（ローカルサーバー向けに推奨）
> 2. **Streamable HTTP** - SSEを内部的に使用する可能性のあるリモートサーバー向け
>
> このレッスンでは、ほとんどのMCPサーバー実装に推奨される**stdioトランスポート**に焦点を当てて更新されています。

stdioトランスポートを使用すると、MCPサーバーは標準入力および出力ストリームを介してクライアントと通信できます。これは現在のMCP仕様で最も一般的かつ推奨されるトランスポートメカニズムであり、さまざまなクライアントアプリケーションと簡単に統合できるシンプルで効率的な方法を提供します。

## 概要

このレッスンでは、stdioトランスポートを使用してMCPサーバーを構築および利用する方法を学びます。

## 学習目標

このレッスンの終わりまでに、以下ができるようになります：

- stdioトランスポートを使用してMCPサーバーを構築する
- MCPサーバーをインスペクターでデバッグする
- Visual Studio Codeを使用してMCPサーバーを利用する
- 現在のMCPトランスポートメカニズムを理解し、なぜstdioが推奨されるのかを把握する

## stdioトランスポートの仕組み

stdioトランスポートは、現在のMCP仕様（2025-06-18）でサポートされている2つのトランスポートタイプの1つです。その仕組みは以下の通りです：

- **シンプルな通信**: サーバーは標準入力（`stdin`）からJSON-RPCメッセージを読み取り、標準出力（`stdout`）にメッセージを送信します。
- **プロセスベース**: クライアントはMCPサーバーをサブプロセスとして起動します。
- **メッセージ形式**: メッセージは、改行で区切られた個々のJSON-RPCリクエスト、通知、またはレスポンスです。
- **ログ記録**: サーバーはログ記録のために標準エラー（`stderr`）にUTF-8文字列を書き込むことができます。

### 主な要件：
- メッセージは改行で区切られ、埋め込み改行を含んではいけません。
- サーバーは、`stdout`に有効なMCPメッセージ以外を書き込んではいけません。
- クライアントは、サーバーの`stdin`に有効なMCPメッセージ以外を書き込んではいけません。

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

- MCP SDKから`Server`クラスと`StdioServerTransport`をインポートしています。
- 基本的な設定と機能を持つサーバーインスタンスを作成しています。

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

- MCP SDKを使用してサーバーインスタンスを作成しています。
- デコレータを使用してツールを定義しています。
- stdio_serverコンテキストマネージャを使用してトランスポートを処理しています。

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

SSEとの主な違いは、stdioサーバーが以下を必要としない点です：

- WebサーバーのセットアップやHTTPエンドポイント
- クライアントによるサーバーのサブプロセスとしての起動
- stdin/stdoutストリームを介した通信
- 実装とデバッグがより簡単

## 演習: stdioサーバーの作成

サーバーを作成するには、以下の2点を念頭に置く必要があります：

- 接続とメッセージ用のエンドポイントを公開するためにWebサーバーを使用する必要があります。

## 実習: シンプルなMCP stdioサーバーの作成

この実習では、推奨されるstdioトランスポートを使用してシンプルなMCPサーバーを作成します。このサーバーは、クライアントが標準のModel Context Protocolを使用して呼び出せるツールを公開します。

### 前提条件

- Python 3.8以上
- MCP Python SDK: `pip install mcp`
- 非同期プログラミングの基本的な理解

最初のMCP stdioサーバーを作成してみましょう：

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## 非推奨となったSSEアプローチとの主な違い

**Stdioトランスポート（現在の標準）:**
- シンプルなサブプロセスモデル - クライアントがサーバーを子プロセスとして起動
- stdin/stdoutを介したJSON-RPCメッセージによる通信
- HTTPサーバーのセットアップ不要
- パフォーマンスとセキュリティの向上
- デバッグと開発が容易

**SSEトランスポート（MCP 2025-06-18以降非推奨）:**
- SSEエンドポイントを持つHTTPサーバーが必要
- Webサーバーインフラのセットアップが複雑
- HTTPエンドポイントの追加のセキュリティ考慮事項
- WebベースのシナリオではStreamable HTTPに置き換えられた

### stdioトランスポートを使用したサーバーの作成

stdioサーバーを作成するには、以下を行う必要があります：

1. **必要なライブラリをインポート** - MCPサーバーコンポーネントとstdioトランスポートが必要
2. **サーバーインスタンスを作成** - サーバーの機能を定義
3. **ツールを定義** - 公開したい機能を追加
4. **トランスポートを設定** - stdio通信を構成
5. **サーバーを実行** - サーバーを起動し、メッセージを処理

ステップごとに構築していきましょう：

### ステップ1: 基本的なstdioサーバーの作成

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

### ステップ3: サーバーの実行

コードを`server.py`として保存し、コマンドラインから実行します：

```bash
python server.py
```

サーバーは起動し、stdinからの入力を待機します。JSON-RPCメッセージをstdioトランスポートで通信します。

### ステップ4: インスペクターを使用したテスト

MCPインスペクターを使用してサーバーをテストできます：

1. インスペクターをインストール: `npx @modelcontextprotocol/inspector`
2. インスペクターを実行し、サーバーを指定
3. 作成したツールをテスト

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## stdioサーバーのデバッグ

### MCPインスペクターの使用

MCPインスペクターは、MCPサーバーのデバッグとテストに役立つツールです。以下の手順で使用します：

1. **インスペクターをインストール**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **インスペクターを実行**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **サーバーをテスト**: インスペクターのWebインターフェースで以下を行います：
   - サーバーの機能を確認
   - 異なるパラメータでツールをテスト
   - JSON-RPCメッセージを監視
   - 接続の問題をデバッグ

### Visual Studio Codeの使用

VS CodeでMCPサーバーを直接デバッグすることもできます：

1. `.vscode/launch.json`に起動構成を作成：
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
3. デバッガーを実行し、インスペクターでテスト

### 一般的なデバッグのヒント

- ログ記録には`stderr`を使用 - `stdout`はMCPメッセージ専用
- すべてのJSON-RPCメッセージが改行で区切られていることを確認
- 複雑な機能を追加する前にシンプルなツールでテスト
- インスペクターを使用してメッセージ形式を検証

## Visual Studio Codeでのstdioサーバーの利用

作成したMCP stdioサーバーをVS Codeに統合し、Claudeや他のMCP対応クライアントで使用できます。

### 設定

1. **MCP設定ファイルを作成**: `%APPDATA%\Claude\claude_desktop_config.json`（Windows）または`~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）に以下を記述：

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

2. **Claudeを再起動**: Claudeを閉じて再度開き、新しいサーバー設定を読み込みます。

3. **接続をテスト**: Claudeとの会話を開始し、サーバーのツールを試します：
   - 「挨拶ツールを使って挨拶してくれますか？」
   - 「15と27の合計を計算してください」
   - 「サーバー情報は何ですか？」

### TypeScript stdioサーバーの例

以下は参考用の完全なTypeScript例です：

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

// Add tools
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

### .NET stdioサーバーの例

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## まとめ

この更新されたレッスンでは、以下を学びました：

- 現在の**stdioトランスポート**（推奨アプローチ）を使用してMCPサーバーを構築する方法
- SSEトランスポートが非推奨となり、stdioおよびStreamable HTTPに置き換えられた理由
- MCPクライアントが呼び出せるツールを作成する方法
- MCPインスペクターを使用してサーバーをデバッグする方法
- stdioサーバーをVS CodeやClaudeに統合する方法

stdioトランスポートは、非推奨となったSSEアプローチと比較して、よりシンプルで安全かつ高性能な方法を提供します。2025-06-18仕様時点で、ほとんどのMCPサーバー実装に推奨されるトランスポートです。

### .NET

1. まずツールを作成します。以下の内容で*Tools.cs*ファイルを作成します：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 演習: stdioサーバーのテスト

作成したstdioサーバーが正しく動作するかテストしてみましょう。

### 前提条件

1. MCPインスペクターがインストールされていることを確認：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. サーバーコードが保存されていること（例：`server.py`）

### インスペクターを使用したテスト

1. **サーバーでインスペクターを起動**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Webインターフェースを開く**: インスペクターがブラウザウィンドウを開き、サーバーの機能を表示します。

3. **ツールをテスト**: 
   - `get_greeting`ツールを異なる名前で試す
   - `calculate_sum`ツールをさまざまな数値でテスト
   - `get_server_info`ツールを呼び出してサーバーメタデータを確認

4. **通信を監視**: インスペクターは、クライアントとサーバー間で交換されるJSON-RPCメッセージを表示します。

### 期待される結果

サーバーが正しく起動すると、以下が確認できます：
- インスペクターにサーバーの機能がリスト表示される
- テスト可能なツールが表示される
- JSON-RPCメッセージの交換が成功する
- ツールのレスポンスがインターフェースに表示される

### よくある問題と解決策

**サーバーが起動しない**:
- すべての依存関係がインストールされているか確認: `pip install mcp`
- Pythonの構文やインデントを確認
- コンソールのエラーメッセージを確認

**ツールが表示されない**:
- `@server.tool()`デコレータが存在することを確認
- ツール関数が`main()`の前に定義されていることを確認
- サーバーが正しく構成されていることを確認

**接続の問題**:
- サーバーがstdioトランスポートを正しく使用していることを確認
- 他のプロセスが干渉していないことを確認
- インスペクターコマンドの構文を確認

## 課題

サーバーにさらに多くの機能を追加してみてください。例えば、[このページ](https://api.chucknorris.io/)を参考にして、APIを呼び出すツールを追加してみましょう。サーバーの設計は自由です。楽しんでください :)

## 解答

[解答](./solution/README.md) 動作するコードの一例を掲載しています。

## 重要なポイント

この章の重要なポイントは以下の通りです：

- stdioトランスポートはローカルMCPサーバーに推奨されるメカニズムです。
- stdioトランスポートは、標準入力および出力ストリームを使用してMCPサーバーとクライアント間のシームレスな通信を可能にします。
- インスペクターとVisual Studio Codeを使用して、stdioサーバーを直接デバッグおよび統合できます。

## サンプル

- [Java電卓](../samples/java/calculator/README.md)
- [.Net電卓](../../../../03-GettingStarted/samples/csharp)
- [JavaScript電卓](../samples/javascript/README.md)
- [TypeScript電卓](../samples/typescript/README.md)
- [Python電卓](../../../../03-GettingStarted/samples/python) 

## 追加リソース

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 次のステップ

現在、stdioトランスポートを使用してMCPサーバーを構築する方法を学びました。次は、より高度なトピックを探求してみましょう：

- **次へ**: [MCPのHTTPストリーミング（Streamable HTTP）](../06-http-streaming/README.md) - リモートサーバー向けのもう1つのサポートされているトランスポートメカニズムを学ぶ
- **高度な内容**: [MCPセキュリティのベストプラクティス](../../02-Security/README.md) - MCPサーバーにセキュリティを実装する
- **本番環境**: [デプロイ戦略](../09-deployment/README.md) - サーバーを本番環境で使用するためのデプロイ方法

## 追加リソース

- [MCP仕様2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 公式仕様
- [MCP SDKドキュメント](https://github.com/modelcontextprotocol/sdk) - すべての言語のSDKリファレンス
- [コミュニティの例](../../06-CommunityContributions/README.md) - コミュニティによるサーバー例

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当方は一切の責任を負いません。