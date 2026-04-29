# stdioトランスポートを使用したMCPサーバー

> **⚠️ 重要なお知らせ**: MCP仕様2025-06-18現在、スタンドアロンのSSE（Server-Sent Events）トランスポートは<strong>非推奨</strong>となり、「Streamable HTTP」トランスポートに置き換えられました。現在のMCP仕様は主に2つのトランスポートメカニズムを定義しています:
> 1. **stdio** - 標準入出力（ローカルサーバー推奨）
> 2. **Streamable HTTP** - 内部でSSEを使用する可能性のあるリモートサーバー向け
>
> このレッスンは、ほとんどのMCPサーバー実装で推奨される<strong>stdioトランスポート</strong>に焦点を当てて更新されています。

stdioトランスポートは、MCPサーバーが標準入力および出力ストリームを通じてクライアントと通信することを可能にします。これは現在のMCP仕様の中で最も一般的かつ推奨されるトランスポートメカニズムであり、さまざまなクライアントアプリケーションと容易に統合できるシンプルで効率的なMCPサーバー構築手法を提供します。

## 概要

このレッスンでは、stdioトランスポートを使ってMCPサーバーを構築・利用する方法を解説します。

## 学習目標

このレッスンの終了時には、以下ができるようになります:

- stdioトランスポートを使用したMCPサーバーの構築
- Inspectorを使ったMCPサーバーのデバッグ
- Visual Studio Codeを使ったMCPサーバーの利用
- 現在のMCPトランスポートメカニズムの理解とstdioが推奨される理由の理解


## stdioトランスポートの仕組み

stdioトランスポートは、現在のMCP仕様（2025-06-18）でサポートされている2つのトランスポートタイプのうちの1つです。仕組みは以下の通りです：

- <strong>シンプルな通信</strong>：サーバーは標準入力（`stdin`）からJSON-RPCメッセージを読み取り、標準出力（`stdout`）にメッセージを送信します。
- <strong>プロセスベース</strong>：クライアントがMCPサーバーをサブプロセスとして起動します。
- <strong>メッセージ形式</strong>：メッセージは個別のJSON-RPCリクエスト、通知、またはレスポンスであり、改行で区切られています。
- <strong>ログ出力</strong>：サーバーはログ目的で標準エラー（`stderr`）にUTF-8文字列を書き込むことができます。

### 重要な要件:
- メッセージは改行で区切られ、改行を含んではいけません
- サーバーは`stdout`に有効なMCPメッセージ以外のものを書き込んではいけません
- クライアントはサーバーの`stdin`に有効なMCPメッセージ以外のものを書き込んではいけません

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

上記のコードでは:

- MCP SDKから`Server`クラスと`StdioServerTransport`をインポートしています
- 基本設定と機能を備えたサーバーインスタンスを作成しています
- `StdioServerTransport`のインスタンスを作成し、サーバーを接続してstdin/stdout経由の通信を可能にしています

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

上記のコードでは:

- MCP SDKを使ってサーバーインスタンスを作成しています
- デコレーターでツールを定義しています
- stdio_serverコンテキストマネージャーを使ってトランスポートを扱っています

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

SSEとの主な違いは、stdioサーバーは:

- WebサーバーのセットアップやHTTPエンドポイントを必要としません
- クライアントがサブプロセスとして起動します
- stdin/stdoutストリームを通じて通信します
- 実装とデバッグがより簡単です

## 演習：stdioサーバーの作成

サーバー作成にあたっては次の2点に注意する必要があります：

- 接続やメッセージのためのエンドポイント公開にWebサーバーを使用する必要がある。

## ラボ：シンプルなMCP stdioサーバーの作成

このラボでは、推奨されるstdioトランスポートを使ってシンプルなMCPサーバーを作成します。このサーバーはクライアントが標準のModel Context Protocolを使って呼び出せるツールを公開します。

### 前提条件

- Python 3.8以降
- MCP Python SDK: `pip install mcp`
- 非同期プログラミングの基本知識

さあ、最初のMCP stdioサーバーを作成しましょう：

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

## 非推奨のSSE方式との主な違い

**Stdioトランスポート（現行標準）:**
- シンプルなサブプロセスモデル - クライアントがサーバーを子プロセスとして起動
- stdin/stdoutを使ったJSON-RPCメッセージでの通信
- HTTPサーバーのセットアップ不要
- 高性能かつ安全性が向上
- デバッグと開発がしやすい

**SSEトランスポート（MCP 2025-06-18で非推奨）:**
- SSEエンドポイントを持つHTTPサーバーが必要
- Webサーバーインフラによる複雑なセットアップ
- HTTPエンドポイントのための追加セキュリティ考慮
- Webベースのシナリオ向けにStreamable HTTPに置換済み

### stdioトランスポートによるサーバーの作成

stdioサーバーを作成するには:

1. <strong>必要なライブラリをインポートする</strong> - MCPサーバーコンポーネントとstdioトランスポートを準備
2. <strong>サーバーインスタンスを作る</strong> - 機能を定義しサーバーを作成
3. <strong>ツールを定義する</strong> - 公開したい機能を追加
4. <strong>トランスポートを設定する</strong> - stdio通信の構成
5. <strong>サーバーを実行する</strong> - サーバーを開始しメッセージを処理

ステップごとに構築していきましょう:

### ステップ1：基本的なstdioサーバーの作成

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

### ステップ2：ツールの追加

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

### ステップ3：サーバーの起動

コードを`server.py`として保存し、コマンドラインから実行します:

```bash
python server.py
```

サーバーは起動してstdinからの入力を待機します。stdioトランスポートを通じてJSON-RPCメッセージで通信します。

### ステップ4：Inspectorによるテスト

MCP Inspectorを使ってサーバーをテストできます：

1. Inspectorをインストール: `npx @modelcontextprotocol/inspector`
2. Inspectorを起動しサーバーを指定
3. 作成したツールをテスト

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## stdioサーバーのデバッグ

### MCP Inspectorの利用

MCP InspectorはMCPサーバーのデバッグとテストに有用なツールです。stdioサーバーでの利用方法は以下の通りです：

1. **Inspectorのインストール**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspectorの起動**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. <strong>サーバーのテスト</strong>: InspectorのWebインターフェースで次のことが可能です：
   - サーバー機能の表示
   - さまざまなパラメータでツールのテスト
   - JSON-RPCメッセージの監視
   - 接続問題のデバッグ

### VS Codeの利用

VS Code上でMCPサーバーのデバッグも可能です：

1. `.vscode/launch.json`にランチ構成を作成:
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
3. デバッガを起動しInspectorでテスト

### デバッグのコツ

- ログは`stderr`に書き込む - `stdout`はMCPメッセージ用なので書き込まない
- JSON-RPCメッセージは必ず改行で区切ること
- 複雑な機能追加前にシンプルなツールでテストする
- Inspectorでメッセージフォーマットを検証する

## VS Codeでstdioサーバーを利用する

MCP stdioサーバーを構築したら、VS Codeと連携してClaudeや他のMCP対応クライアントで使用できます。

### 設定

1. MCP設定ファイルを以下に作成します：  
%APPDATA%\Claude\claude_desktop_config.json（Windows）  
または  
~/Library/Application Support/Claude/claude_desktop_config.json（Mac）

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

2. Claudeを再起動し、新しいサーバー設定を読み込みます。

3. 接続をテスト: Claudeと対話しサーバーのツールを使ってみてください：
   - 「greetingツールを使ってあいさつしてくれる？」
   - 「15と27の合計を計算して」
   - 「サーバー情報は？」

### TypeScript stdioサーバーの例

参考のための完全なTypeScript例を示します：

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

この更新されたレッスンで学んだこと：

- 現行の<strong>stdioトランスポート</strong>を使ったMCPサーバーの構築（推奨アプローチ）
- SSEトランスポートがなぜ非推奨になりstdioやStreamable HTTPに置き換わったかの理解
- MCPクライアントから呼び出されるツールの作成方法
- MCP Inspectorを利用したサーバーのデバッグ方法
- VS CodeやClaudeと連携したstdioサーバーの統合

stdioトランスポートは、非推奨となったSSE方式と比べて、よりシンプルで安全性が高く、性能も優れたMCPサーバー構築方法です。2025-06-18仕様の現在では、ほとんどのMCPサーバー実装で推奨されるトランスポートです。


### .NET

1. まずツールをいくつか作成しましょう。そのために<em>Tools.cs</em>というファイルを下記内容で作成します:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 演習：stdioサーバーのテスト

stdioサーバーを構築できたら、正しく動作するかテストしてみましょう。

### 前提条件

1. MCP Inspectorがインストールされていることを確認:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. サーバーコードを保存してある（例：`server.py`）

### Inspectorを使ったテスト

1. **Inspectorをサーバーと共に起動**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Webインターフェースを開く**: Inspectorがブラウザでサーバー機能を表示

3. <strong>ツールをテスト</strong>: 
   - `get_greeting`ツールを異なる名前で試す
   - `calculate_sum`ツールで様々な数値をテスト
   - `get_server_info`ツールを呼び出しサーバーメタデータを確認

4. <strong>通信の監視</strong>: Inspectorがクライアントとサーバー間のJSON-RPCメッセージを表示

### 見るべきポイント

サーバーが正しく起動すると以下が表示されます:
- Inspectorにサーバー機能の一覧
- テスト可能なツール
- 成功したJSON-RPCメッセージのやり取り
- インターフェースにツール応答が表示

### よくある問題と対策

**サーバーが起動しない場合:**
- 依存パッケージがインストールされているか: `pip install mcp`
- Pythonの文法やインデントに誤りがないか
- コンソールのエラーメッセージを確認

**ツールが表示されない場合:**
- `@server.tool()`デコレーターが付いているか
- ツール関数が`main()`より前に定義されているか
- サーバーの設定が正しいか

**接続の問題:**
- サーバーがstdioトランスポートを正しく使用しているか
- 他のプロセスの干渉がないか
- Inspectorのコマンド構文を確認

## 課題

サーバーにさらに多くの機能を追加してみましょう。例えば[このページ](https://api.chucknorris.io/)を参照してAPIを呼び出すツールを作成することも可能です。サーバーの内容は自由に設計してください。楽しんでください :)

## 解答例

[解答例](./solution/README.md) こちらに動作するコードの一例があります。

## 重要ポイント

この章の重要なポイントは次の通りです：

- stdioトランスポートはローカルMCPサーバーの推奨メカニズムである。
- stdioトランスポートは標準入出力ストリームを通してMCPサーバーとクライアント間のシームレスな通信を可能にする。
- InspectorとVisual Studio Codeの両方でstdioサーバーを直接利用できるため、デバッグや統合が容易。

## サンプル

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## 追加リソース

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 次のステップ

## 今後の展開

stdioトランスポートでMCPサーバーを構築する方法を学んだので、次のような高度なトピックを探求できます：

- **次に学ぶ:** [MCPのHTTPストリーミング(Streamable HTTP)](../06-http-streaming/README.md) - リモートサーバー向けのもう1つのトランスポートメカニズムについて学ぶ
- **高度:** [MCPセキュリティベストプラクティス](../../02-Security/README.md) - MCPサーバーのセキュリティ実装
- **本番運用:** [デプロイメント戦略](../09-deployment/README.md) - サーバーの本番環境へのデプロイ

## 追加リソース

- [MCP仕様 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 公式仕様
- [MCP SDKドキュメント](https://github.com/modelcontextprotocol/sdk) - すべての言語向けSDKリファレンス
- [コミュニティ例](../../06-CommunityContributions/README.md) - コミュニティによるさらなるサーバー例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることにご留意ください。オリジナルの原文が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や解釈の相違について、当方は一切の責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->