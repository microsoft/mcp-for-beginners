# クライアントの作成

クライアントは、MCPサーバーと直接通信してリソース、ツール、プロンプトをリクエストするカスタムアプリケーションまたはスクリプトです。サーバーと対話するためのグラフィカルインターフェースを提供するインスペクターツールとは異なり、自分でクライアントを書くことで、プログラム的かつ自動化された操作が可能になります。これにより、開発者はMCPの機能を自分のワークフローに統合し、タスクを自動化し、特定のニーズに合わせたカスタムソリューションを構築できます。

## 概要

このレッスンでは、Model Context Protocol (MCP) エコシステム内のクライアントの概念を紹介します。自身のクライアントを書き、それをMCPサーバーに接続する方法を学びます。

## 学習目標

このレッスンの終了時には、次のことができるようになります：

- クライアントが何をできるか理解する
- 自分のクライアントを書く
- MCPサーバーに接続しクライアントをテストして、サーバーが期待通りに動作していることを確認する

## クライアントを書くには何が必要か？

クライアントを書くために次のことを行う必要があります：

- <strong>正しいライブラリをインポートする</strong>。前回と同じライブラリを使いますが、使う構成は異なります。
- <strong>クライアントのインスタンスを生成する</strong>。クライアントインスタンスを作成し、選択したトランスポート方法に接続します。
- <strong>どのリソースをリストアップするか決める</strong>。MCPサーバーにはリソース、ツール、プロンプトが用意されています。どれをリストアップするかを決める必要があります。
- <strong>クライアントをホストアプリケーションに統合する</strong>。サーバーの機能を理解したら、ユーザーがプロンプトや他のコマンドを入力した際に該当するサーバー機能が呼び出されるように、このクライアントをホストアプリケーションに組み込みます。

高レベルでやるべきことを理解したので、次に例を見てみましょう。

### 例となるクライアント

この例のクライアントを見てみましょう：

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// プロンプトの一覧
const prompts = await client.listPrompts();

// プロンプトを取得
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// リソースの一覧
const resources = await client.listResources();

// リソースを読む
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ツールを呼び出す
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

上記のコードで私たちは：

- ライブラリをインポートし
- クライアントのインスタンスを作成し、stdioトランスポートで接続しました
- プロンプト、リソース、ツールをリストアップしてすべて呼び出します

これで、MCPサーバーと通信可能なクライアントができました。

次の演習セクションではコードの断片をじっくり説明し、どのように動作しているかを解説します。

## 演習：クライアントを書く

ここまでの説明の通り、コードの説明に時間をかけて、必要なら一緒にコードを書いてみてください。

### -1- ライブラリのインポート

必要なライブラリをインポートしましょう。クライアントと選択したトランスポートプロトコル（ここではstdio）への参照が必要です。stdioはローカルマシン上で動作することを想定したプロトコルです。SSEは将来章で紹介する別のトランスポートプロトコルですが、現時点ではstdioを使います。

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### Java

Javaでは、前の演習で使ったMCPサーバーに接続するクライアントを作成します。[Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) のJava Spring Bootプロジェクト構造を使い、`src/main/java/com/microsoft/mcp/sample/client/` フォルダーに `SDKClient` という新しいJavaクラスを作成して、次のインポートを追加してください。

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

`Cargo.toml` ファイルに次の依存関係を追加する必要があります。

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

そこから、クライアントコード内で必要なライブラリをインポート可能です。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

次はインスタンス作成に進みましょう。

### -2- クライアントとトランスポートのインスタンス作成

トランスポートとクライアントのインスタンスを作成する必要があります：

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

上記のコードで私たちは：

- stdioトランスポートのインスタンスを作成しました。サーバーの起動方法を示す `command` と `args` が指定されているのがポイントで、これはクライアント作成時に必要となります。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- クライアントを名前とバージョンを与えてインスタンス化しました。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- クライアントを選択したトランスポートに接続しました。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio接続のためのサーバーパラメータを作成する
server_params = StdioServerParameters(
    command="mcp",  # 実行可能ファイル
    args=["run", "server.py"],  # 任意のコマンドライン引数
    env=None,  # 任意の環境変数
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # 接続を初期化する
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

上記のコードでは：

- 必要なライブラリをインポートし
- サーバーパラメータオブジェクトをインスタンス化しました。これを利用してサーバーを起動し、クライアントから接続します。
- `run` メソッドを定義し、`stdio_client` を呼び出してクライアントセッションを開始します。
- エントリーポイントを作成し、`asyncio.run` に `run` メソッドを渡しています。

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

上記のコードでは：

- 必要なライブラリをインポートし
- stdioトランスポートを作成し、クライアント `mcpClient` を作成しています。そのクライアントを使ってMCPサーバーの機能をリストアップし呼び出します。

「Arguments」には *.csproj* または実行可能ファイルのどちらかを指定できます。

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // あなたのクライアントロジックはここに記述します
    }
}
```

上記のコードでは：

- MCPサーバーが `http://localhost:8080` で動作する想定でSSEトランスポートを設定するmainメソッドを作成しました。
- トランスポートをコンストラクタパラメータとして受け取るクライアントクラスを作成しています。
- `run` メソッド内でトランスポートを使い同期的なMCPクライアントを作成し接続を初期化します。
- Java Spring Boot MCPサーバーとのHTTPベース通信に適したSSE (Server-Sent Events) トランスポートを使用しています。

#### Rust

このRustクライアントでは、同じディレクトリ内の兄弟プロジェクト名 "calculator-server" をサーバーとして想定しています。以下のコードはサーバーを起動し接続します。

```rust
async fn main() -> Result<(), RmcpError> {
    // サーバーは同じディレクトリ内の兄弟プロジェクトである「calculator-server」と仮定します
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: 初期化

    // TODO: ツールをリストアップする

    // TODO: 引数 = {"a": 3, "b": 2}でaddツールを呼び出す

    client.cancel().await?;
    Ok(())
}
```

### -3- サーバー機能のリストアップ

これでクライアントは接続可能ですが、機能の一覧を取得していません。これを次に行います：

#### TypeScript

```typescript
// プロンプトを一覧表示
const prompts = await client.listPrompts();

// リソースを一覧表示
const resources = await client.listResources();

// ツールを一覧表示
const tools = await client.listTools();
```

#### Python

```python
# 利用可能なリソースをリストアップ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# 利用可能なツールをリストアップ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ここでは利用可能なリソースを `list_resources()` で、ツールを `list_tools` でリストアップし、それを出力しています。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

上記はサーバー上のツールをリストアップし、それぞれの名前を表示する例です。

#### Java

```java
// ツールの一覧とデモを示します
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 接続確認のためにサーバーにpingを送ることもできます
client.ping();
```

上記コードでは：

- MCPサーバーから利用可能なツールをすべて取得するために `listTools()` を呼び出しました。
- サーバー接続が正常か確かめるために `ping()` を使いました。
- `ListToolsResult` には名前、説明、入力スキーマを含むすべてのツールの情報が入っています。

これで全機能をキャプチャしました。問題はいつ使うかです。このクライアントは非常にシンプルで、機能が必要な時に明示的に呼び出す必要があります。次章では自身の大規模言語モデル（LLM）を持つ、より高度なクライアントを作成します。とりあえず今のところ、サーバー上の機能を呼び出す方法を見ましょう：

#### Rust

main関数内でクライアント初期化後にサーバーを初期化し、いくつかの機能一覧を取得しています。

```rust
// 初期化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// ツールをリストアップする
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 機能の呼び出し

機能を呼び出すには、正しい引数、場合によっては呼び出す名前を正確に指定する必要があります。

#### TypeScript

```typescript

// リソースを読み取る
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ツールを呼び出す
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// プロンプトを呼び出す
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

上記コードでは：

- リソースの読み込みとして `readResource()` を `uri` 指定で呼び出しました。サーバー側は大抵次のようになります：

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    我々の `uri` 値 `file://example.txt` はサーバーの `file://{name}` に対応しています。`example.txt` は `name` にマッピングされます。

- ツールの呼び出しは、ツールの `name` と `arguments` を指定します：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- プロンプト取得は、 `getPrompt()` を `name` と `arguments` で呼びます。サーバーコードはこうなっています：

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    それに対応するクライアントコードは以下の通りになります：

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# リソースを読み取る
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ツールを呼び出す
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

上記コードで：

- `greeting` と呼ばれるリソースを `read_resource` を使い呼び出しました。
- `add` ツールを `call_tool` で呼び出しました。

#### .NET

1. ツール呼び出しのコードを追加しましょう：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. 結果出力のためのコード例：

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// さまざまな計算ツールを呼び出します
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

上記のコードで：

- `callTool()` メソッドを使い、`CallToolRequest` オブジェクトで複数の計算ツールを呼び出しました。
- 各ツール呼び出しはツール名と、そのツールに必要な引数の `Map` を指定しています。
- サーバーツールは特定のパラメーター名（例えば数学演算の "a", "b"）を期待しています。
- 結果はサーバーからの応答を含む `CallToolResult` オブジェクトとして返されます。

#### Rust

```rust
// 引数 = {"a": 3, "b": 2} で add ツールを呼び出します
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- クライアントの実行

クライアントを実行するには、ターミナルで次のコマンドを入力します：

#### TypeScript

*package.json* の "scripts" セクションに次を追加してください：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

クライアントを次のコマンドで呼び出します：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

まずMCPサーバーが `http://localhost:8080` で動いていることを確認し、クライアントを実行してください：

```bash
# プロジェクトをビルドする
./mvnw clean compile

# クライアントを実行する
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

もしくは、ソリューションフォルダ `03-GettingStarted\02-client\solution\java` にある完全なクライアントプロジェクトを実行できます：

```bash
# ソリューションディレクトリに移動します
cd 03-GettingStarted/02-client/solution/java

# JARをビルドして実行します
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 課題

この課題では学んだクライアント作成を活用し、オリジナルのクライアントを作成してください。

使えるサーバーが用意してあるので、それにクライアント経由で呼び出し、さらに面白くなるようサーバーに機能を追加できるか試してみてください。

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCPサーバーを作成する
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// 加算ツールを追加する
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// 動的な挨拶リソースを追加する
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// 標準入力でメッセージの受信を開始し、標準出力でメッセージの送信を開始する

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCPサーバーを作成する
mcp = FastMCP("Demo")


# 加算ツールを追加する
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 動的な挨拶リソースを追加する
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

このプロジェクトを参照して、[プロンプトとリソースの追加方法](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)を確認してください。

また、こちらのリンクで [プロンプトとリソースの呼び出し方法](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) をチェックしてください。

### Rust

[前章](../../../../03-GettingStarted/01-first-server) でRustでのシンプルなMCPサーバーの作り方を学びました。そこから発展させるか、こちらのRustベースMCPサーバー例を参照してください：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## ソリューション

**solutionフォルダー** には、このチュートリアルでカバーしたすべての概念を実装した、すぐに実行可能な完全なクライアント実装が含まれています。各ソリューションにはクライアントとサーバーコードが、それぞれ独立したプロジェクトとして整理されています。

### 📁 ソリューション構成

ソリューションディレクトリはプログラミング言語別に整理されています：

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 各ソリューションの内容

各言語特有のソリューションには以下が含まれます：

- チュートリアルの全機能を備えた完全なクライアント実装
- 適切な依存関係と設定を備えた動作するプロジェクト構造
- 簡単にセットアップし実行できるビルドとラン用スクリプト
- 言語別の詳細なREADME
- エラーハンドリングと結果処理の例

### 📖 ソリューションの使い方

1. <strong>使いたい言語のフォルダーに移動します</strong>：

   ```bash
   cd solution/typescript/    # TypeScript用
   cd solution/java/          # Java用
   cd solution/python/        # Python用
   cd solution/dotnet/        # .NET用
   ```

2. **各フォルダーのREADMEに従って**：
   - 依存関係のインストール
   - プロジェクトのビルド
   - クライアントの実行

3. <strong>以下のような出力例が期待できます</strong>：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

詳細なドキュメントとステップバイステップの説明は： **[📖 ソリューションドキュメント](./solution/README.md)** を参照してください

## 🎯 完全な例

本チュートリアルで扱った全プログラミング言語の完全かつ動作するクライアント実装を用意しています。これらの例は上記のすべての機能を示し、リファレンス実装や自身のプロジェクトの出発点として利用できます。

### 利用可能な完全な例

| 言語 | ファイル | 説明 |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSEトランスポートを使った完全なJavaクライアント。充実したエラーハンドリング付き |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdioトランスポートを使った完全なC#クライアント。サーバー自動起動機能付き |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCPプロトコルを完全にサポートした完璧なTypeScriptクライアント |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/awaitパターンを使った完全なPythonクライアント |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokioを使った非同期操作対応の完全Rustクライアント |

各完全な例には：

- ✅ <strong>接続確立</strong> とエラーハンドリング
- ✅ <strong>サーバー検出</strong>（ツール、リソース、プロンプトを含む場合あり）
- ✅ <strong>計算機能操作</strong>（加算、減算、乗算、除算、ヘルプ）
- ✅ <strong>結果処理</strong> と整形出力
- ✅ <strong>徹底したエラーハンドリング</strong>

- ✅ <strong>段階的なコメント付きのクリーンで文書化されたコード</strong>

### 完全な例で始める

1. 上記の表から <strong>好みの言語を選択</strong> してください
2. <strong>完全な例ファイルを確認して</strong> 実装全体を理解してください
3. [`complete_examples.md`](./complete_examples.md) の指示に従って <strong>例を実行</strong> してください
4. 特定のユースケースに合わせて <strong>例を修正し拡張</strong> してください

これらの例の実行およびカスタマイズに関する詳しいドキュメントは、**[📖 Complete Examples Documentation](./complete_examples.md)** をご覧ください

### 💡 Solution と Complete Examples の違い

| **Solution フォルダー** | **Complete Examples** |
|--------------------|--------------------- |
| ビルドファイルを含む完全なプロジェクト構造 | 単一ファイル実装 |
| 依存関係付きで即実行可能 | 集中したコード例 |
| 本番環境に近いセットアップ | 教育用リファレンス |
| 言語固有のツール | 言語間比較 |

どちらのアプローチも価値があります。完全なプロジェクトには **solution フォルダー** を、学習やリファレンスには **complete examples** をご利用ください。

## 重要なポイント

この章でのクライアントに関する重要なポイントは次の通りです:

- サーバーの機能を発見し、呼び出すための両方に使える
- 自身で起動しながらサーバーを開始できる（この章のように）ほか、クライアントはすでに稼働中のサーバーにも接続できる
- 前章で説明した Inspector のような代替手段と並んで、サーバー機能をテストする素晴らしい方法である

## 追加リソース

- [MCPでのクライアント構築](https://modelcontextprotocol.io/quickstart/client)

## サンプル

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## 次に行うこと

- 次: [LLMでクライアントを作成する](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->