<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8831b194cb5ece750355e99434b7154",
  "translation_date": "2025-07-17T17:59:08+00:00",
  "source_file": "03-GettingStarted/05-sse-server/README.md",
  "language_code": "ja"
}
-->
# SSEサーバー

SSE（Server Sent Events）は、サーバーからクライアントへのストリーミングの標準であり、サーバーがHTTPを通じてリアルタイムの更新をクライアントにプッシュすることを可能にします。これはチャットアプリケーション、通知、リアルタイムデータフィードなど、ライブアップデートが必要なアプリケーションに特に有用です。また、サーバーはクラウドなどのどこかで実行されるサーバー上に存在するため、複数のクライアントが同時に利用できます。

## 概要

このレッスンでは、SSEサーバーの構築と利用方法について説明します。

## 学習目標

このレッスンの終わりまでに、以下ができるようになります：

- SSEサーバーを構築する。
- Inspectorを使ってSSEサーバーをデバッグする。
- Visual Studio Codeを使ってSSEサーバーを利用する。

## SSEの仕組み

SSEはサポートされている2つのトランスポートタイプのうちの一つです。前のレッスンで使ったstdioが最初のタイプでした。違いは以下の通りです：

- SSEでは接続とメッセージの2つを扱う必要があります。
- このサーバーはどこにでも存在できるため、InspectorやVisual Studio Codeのようなツールの使い方にもそれが反映されます。つまり、サーバーの起動方法を指定する代わりに、接続を確立できるエンドポイントを指定します。以下の例コードを参照してください。

### TypeScript

```typescript
app.get("/sse", async (_: Request, res: Response) => {
    const transport = new SSEServerTransport('/messages', res);
    transports[transport.sessionId] = transport;
    res.on("close", () => {
        delete transports[transport.sessionId];
    });
    await server.connect(transport);
});

app.post("/messages", async (req: Request, res: Response) => {
    const sessionId = req.query.sessionId as string;
    const transport = transports[sessionId];
    if (transport) {
        await transport.handlePostMessage(req, res);
    } else {
        res.status(400).send('No transport found for sessionId');
    }
});
```

上記のコードでは：

- `/sse`がルートとして設定されています。このルートにリクエストが来ると、新しいトランスポートインスタンスが作成され、サーバーはこのトランスポートを使って*接続*します。
- `/messages`は受信メッセージを処理するルートです。

### Python

```python
mcp = FastMCP("My App")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

```

上記のコードでは：

- ASGIサーバーのインスタンス（特にStarletteを使用）を作成し、デフォルトルート`/`にマウントしています。

  裏側では、`/sse`と`/messages`のルートがそれぞれ接続とメッセージの処理に設定されています。その他の機能追加はstdioサーバーと同様に行われます。

### .NET    

```csharp
    var builder = WebApplication.CreateBuilder(args);
    builder.Services
        .AddMcpServer()
        .WithTools<Tools>();


    builder.Services.AddHttpClient();

    var app = builder.Build();

    app.MapMcp();
    ```

    WebサーバーからSSE対応のWebサーバーに移行するのに役立つ2つのメソッドがあります：

    - `AddMcpServer`：機能を追加します。
    - `MapMcp`：`/SSE`や`/messages`のようなルートを追加します。
```

SSE についてもう少し理解できたので、次は SSE サーバーを構築してみましょう。

## 演習: SSE サーバーの作成

To create our server, we need to keep two things in mind:

- We need to use a web server to expose endpoints for connection and messages.
- stdio を使用していたときに通常行うのと同じように、ツール、リソース、プロンプトを使用してサーバーを構築します。

### -1- Create a server instance

To create our server, we use the same types as with stdio. However, for the transport, we need to choose SSE.

### TypeScript

```typescript
import { Request, Response } from "express";
import express from "express";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";

const server = new McpServer({
  name: "example-server",
  version: "1.0.0"
});

const app = express();

const transports: {[sessionId: string]: SSEServerTransport} = {};
```

In the preceding code we've:

- Created a server instance.
- Defined an app using the web framework express.
- Created a transports variable that we will use to store incoming connections.

### Python

```python
from starlette.applications import Starlette
from starlette.routing import Mount, Host
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("My App")
```

In the preceding code we've:

- Imported the libraries we're going to need with Starlette (an ASGI framework) being pulled in.
- Created an MCP server instance `mcp`.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();


builder.Services.AddHttpClient();

var app = builder.Build();

// TODO: add routes 
```

At this point, we've:

- Created a web app
- Added support for MCP features through `AddMcpServer`.

Let's add the needed routes next.

### -2- Add routes

Let's add routes next that handle the connection and incoming messages:

### TypeScript

```typescript
app.get("/sse", async (_: Request, res: Response) => {
  const transport = new SSEServerTransport('/messages', res);
  transports[transport.sessionId] = transport;
  res.on("close", () => {
    delete transports[transport.sessionId];
  });
  await server.connect(transport);
});

app.post("/messages", async (req: Request, res: Response) => {
  const sessionId = req.query.sessionId as string;
  const transport = transports[sessionId];
  if (transport) {
    await transport.handlePostMessage(req, res);
  } else {
    res.status(400).send('No transport found for sessionId');
  }
});

app.listen(3001);
```

In the preceding code we've defined:

- An `/sse` route that instantiates a transport of type SSE and ends up calling `connect` on the MCP server.
- A `/messages` route that takes care of incoming messages.

### Python

```python
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)
```

In the preceding code we've:

- Created an ASGI app instance using the Starlette framework. As part of that we passes `mcp.sse_app()` to it's list of routes. That ends up mounting an `/sse` and `/messages` route on the app instance.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();

builder.Services.AddHttpClient();

var app = builder.Build();

app.MapMcp();
```

We've added one line of code at the end `add.MapMcp()` this means we now have routes `/SSE` and `/messages`. 

Let's add capabilties to the server next.

### -3- Adding server capabilities

Now that we've got everything SSE specific defined, let's add server capabilities like tools, prompts and resources.

### TypeScript

```typescript
server.tool("random-joke", "A joke returned by the chuck norris api", {},
  async () => {
    const response = await fetch("https://api.chucknorris.io/jokes/random");
    const data = await response.json();

    return {
      content: [
        {
          type: "text",
          text: data.value
        }
      ]
    };
  }
);
```

Here's how you can add a tool for example. This specific tool creates a tool call "random-joke" that calls a Chuck Norris API and returns a JSON response.

### Python

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

Now your server has one tool.

### TypeScript

```typescript
// server-sse.ts
import { Request, Response } from "express";
import express from "express";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { SSEServerTransport } from "@modelcontextprotocol/sdk/server/sse.js";

// MCPサーバーを作成
const server = new McpServer({
  name: "example-server",
  version: "1.0.0",
});

const app = express();

const transports: { [sessionId: string]: SSEServerTransport } = {};

app.get("/sse", async (_: Request, res: Response) => {
  const transport = new SSEServerTransport("/messages", res);
  transports[transport.sessionId] = transport;
  res.on("close", () => {
    delete transports[transport.sessionId];
  });
  await server.connect(transport);
});

app.post("/messages", async (req: Request, res: Response) => {
  const sessionId = req.query.sessionId as string;
  const transport = transports[sessionId];
  if (transport) {
    await transport.handlePostMessage(req, res);
  } else {
    res.status(400).send("sessionIdに対応するトランスポートが見つかりません");
  }
});

server.tool("random-joke", "chuck norris APIから取得したジョーク", {}, async () => {
  const response = await fetch("https://api.chucknorris.io/jokes/random");
  const data = await response.json();

  return {
    content: [
      {
        type: "text",
        text: data.value,
      },
    ],
  };
});

app.listen(3001);
```

### Python

```python
from starlette.applications import Starlette
from starlette.routing import Mount, Host
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("My App")

@mcp.tool()
def add(a: int, b: int) -> int:
    """2つの数字を足す"""
    return a + b

# 既存のASGIサーバーにSSEサーバーをマウント
app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)
```

### .NET

1. Let's create some tools first, for this we will create a file *Tools.cs* with the following content:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;

  namespace server;

  [McpServerToolType]
  public sealed class Tools
  {

      public Tools()
      {
      
      }

      [McpServerTool, Description("2つの数字を足し合わせます。")]
      public async Task<string> AddNumbers(
          [Description("最初の数字")] int a,
          [Description("2番目の数字")] int b)
      {
          return (a + b).ToString();
      }

  }
  ```

  Here we've added the following:

  - Created a class `Tools` with the decorator `McpServerToolType`.
  - Defined a tool `AddNumbers` by decorating the method with `McpServerTool`. We've also provided parameters and an implementation.

1. Let's leverage the `Tools` class we just created:

  ```csharp
  var builder = WebApplication.CreateBuilder(args);
  builder.Services
      .AddMcpServer()
      .WithTools<Tools>();


  builder.Services.AddHttpClient();

  var app = builder.Build();

  app.MapMcp();
  ```

  We've added a call to `WithTools` that specifies `Tools` as the class containing the tools. That's it, we're ready.

Great, we have a server using SSE, let's take it for a spin next.

## Exercise: Debugging an SSE Server with Inspector

Inspector is a great tool that we saw in a previous lesson [Creating your first server](/03-GettingStarted/01-first-server/README.md). Let's see if we can use the Inspector even here:

### -1- Running the inspector

To run the inspector, you first must have an SSE server running, so let's do that next:

1. Run the server 

    ### TypeScript

    ```sh
    tsx && node ./build/server-sse.ts
    ```

    ### Python

    ```sh
    uvicorn server:app
    ```

    Note how we use the executable `uvicorn` that's installed when we typed `pip install "mcp[cli]"`. Typing `server:app` means we're trying to run a file `server.py` and for it to have a Starlette instance called `app`. 

    ### .NET

    ```sh
    dotnet run
    ```

    This should start the server. To interface with it you need a new terminal.

1. Run the inspector

    > ![NOTE]
    > Run this in a separate terminal window than the server is running in. Also note, you need to adjust the below command to fit the URL where your server runs.

    ```sh
    npx @modelcontextprotocol/inspector --cli http://localhost:8000/sse --method tools/list
    ```

    Inspectorの実行はすべてのランタイムで同じように見えます。サーバーのパスや起動コマンドを渡す代わりに、サーバーが動作しているURLと`/sse`ルートを指定している点に注目してください。

### -2- ツールの試用

ドロップリストからSSEを選択し、サーバーが動作しているURL（例： http:localhost:4321/sse）を入力してサーバーに接続します。前回と同様にツールの一覧を取得し、ツールを選択して入力値を提供してください。以下のような結果が表示されるはずです：

![Inspectorで動作中のSSEサーバー](../../../../translated_images/sse-inspector.d86628cc597b8fae807a31d3d6837842f5f9ee1bcc6101013fa0c709c96029ad.ja.png)

素晴らしいです。Inspectorでの操作ができました。次にVisual Studio Codeでの操作方法を見てみましょう。

## 課題

サーバーにさらに機能を追加してみてください。例えば、[このページ](https://api.chucknorris.io/)を参考にAPIを呼び出すツールを追加するなど、サーバーの形は自由に決めて構いません。楽しんでください :)

## 解答例

[解答例](./solution/README.md) 動作するコードを含む一例です。

## まとめ

この章の重要なポイントは以下の通りです：

- SSEはstdioに次ぐ2番目のサポートされているトランスポートです。
- SSEをサポートするには、Webフレームワークを使って接続とメッセージの管理が必要です。
- InspectorやVisual Studio Codeを使ってstdioサーバーと同様にSSEサーバーを利用できます。ただしstdioとSSEでは少し違いがあります。SSEではサーバーを別途起動してからInspectorツールを実行します。またInspectorツールではURLを指定する必要があります。

## サンプル

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## 追加リソース

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 次に進む

- 次へ: [MCPによるHTTPストリーミング（Streamable HTTP）](../06-http-streaming/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。
