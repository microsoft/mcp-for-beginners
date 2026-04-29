# クライアントの作成

クライアントは、MCPサーバーと直接通信してリソース、ツール、およびプロンプトを要求するカスタムアプリケーションまたはスクリプトです。サーバーとの対話のためのグラフィカルインターフェイスを提供するインスペクターツールとは異なり、自分でクライアントを書くことでプログラムによる自動化された操作が可能になります。これにより、開発者はMCPの機能を自分のワークフローに統合し、タスクを自動化し、特定のニーズに合わせたカスタムソリューションを構築できます。

## 概要

このレッスンでは、Model Context Protocol (MCP) エコシステム内のクライアントの概念を紹介します。自分のクライアントを書く方法とMCPサーバーに接続する方法を学びます。

## 学習目標

このレッスンの終わりには、以下ができるようになります：

- クライアントができることを理解する。
- 自分自身でクライアントを書く。
- MCPサーバーに接続してテストし、サーバーが期待通りに動作することを確認する。

## クライアントを書くには何が必要？

クライアントを書くために必要なことは以下の通りです：

- **適切なライブラリのインポート**。前回と同じライブラリを使いますが、使う構造体が異なります。
- **クライアントのインスタンス化**。クライアントインスタンスを作成し、選択したトランスポート方法に接続します。
- **どのリソースを一覧表示するか決定**。MCPサーバーにはリソース、ツール、プロンプトがありますが、どれを一覧表示するか選択します。
- **クライアントをホストアプリに統合**。サーバーの機能が分かったら、ユーザーがプロンプトやコマンドを入力したときに対応するサーバーの機能が呼び出されるようホストアプリケーションに組み込みます。

大まかな流れがわかったところで、次は例を見ていきましょう。

### クライアントの例

以下に例となるクライアントを見てみましょう：

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

// プロンプトを一覧表示
const prompts = await client.listPrompts();

// プロンプトを取得
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// リソースを一覧表示
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

上記コードでは：

- ライブラリをインポート。
- クライアントのインスタンスを作成し、stdioをトランスポートとして接続。
- プロンプト、リソース、ツールを一覧表示し、すべて呼び出し。

これでMCPサーバーと通信できるクライアントができました。

次の演習セクションでじっくりコードを分解し、内容を説明します。

## 演習：クライアントを書く

前述の通り、コードの説明をじっくり行います。もしよければ一緒にコードを書きながら進めてください。

### -1- ライブラリをインポートする

必要なライブラリをインポートします。クライアント本体と、選択したトランスポートプロトコルであるstdioの参照が必要です。stdioはローカルマシンで実行するもの向けのプロトコルです。SSEは別のトランスポートプロトコルで、後の章で紹介しますが、今回はstdioを使います。

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

Javaでは、前の演習で使ったMCPサーバーに接続するクライアントを作成します。[Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java)のJava Spring Bootプロジェクト構造を利用し、`src/main/java/com/microsoft/mcp/sample/client/`フォルダーに`SDKClient`クラスを作成し、以下のインポートを追加してください：

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

`Cargo.toml`ファイルに以下の依存関係を追加してください。

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

クライアントコード内で必要なライブラリをインポートします。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

次にインスタンス化に移ります。

### -2- クライアントとトランスポートのインスタンス化

トランスポートのインスタンスとクライアントのインスタンスを作成します。

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

上記コードで：

- stdioトランスポートのインスタンスを作成。サーバーを起動するコマンドと引数を指定している点に注目してください。クライアント作成時に必要な処理です。

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 名前とバージョンを指定してクライアントをインスタンス化。

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- クライアントを選択したトランスポートに接続。

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
    args=["run", "server.py"],  # オプションのコマンドライン引数
    env=None,  # オプションの環境変数
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

上記コードで：

- 必要なライブラリをインポート。
- サーバーパラメータオブジェクトを作成。これを使ってサーバーを起動し、クライアントから接続します。
- `run`メソッドを定義し、内部から`stdio_client`を呼び出してクライアントセッションを開始。
- エントリポイントで`asyncio.run`に`run`メソッドを渡す。

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

上記コードで：

- ライブラリをインポート。
- stdioトランスポートを作成し、クライアント`mcpClient`を作成。これはMCPサーバーの機能を一覧表示・呼び出しに使います。

なお、"Arguments"では*.csproj*ファイルか実行ファイルのどちらかを指定できます。

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
        
        // クライアントのロジックはここに記述します
    }
}
```

上記コードで：

- `http://localhost:8080`を指すSSEトランスポートを設定するmainメソッドを作成。ここでMCPサーバーが動作。
- トランスポートをコンストラクタ引数にとるクライアントクラスを作成。
- `run`メソッドでトランスポート経由の同期MCPクライアントを作成し、接続を初期化。
- Java Spring Boot MCPサーバーとのHTTPベース通信に適したSSE (Server-Sent Events) トランスポートを使用。

#### Rust

Rustクライアントは同じディレクトリに兄弟プロジェクト「calculator-server」があることを前提とします。以下のコードはサーバーを起動し接続します。

```rust
async fn main() -> Result<(), RmcpError> {
    // サーバーは同じディレクトリ内にある「calculator-server」という兄弟プロジェクトであると仮定します
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

    // TODO: 初期化する

    // TODO: ツールをリストする

    // TODO: 引数 = {"a": 3, "b": 2} で add ツールを呼び出す

    client.cancel().await?;
    Ok(())
}
```

### -3- サーバーの機能を一覧表示

プログラム実行時に接続できるクライアントができましたが、現状では機能一覧を表示しません。次にそれを行いましょう：

#### TypeScript

```typescript
// プロンプトをリストする
const prompts = await client.listPrompts();

// リソースをリストする
const resources = await client.listResources();

// ツールをリストする
const tools = await client.listTools();
```

#### Python

```python
# 利用可能なリソースを一覧表示する
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# 利用可能なツールを一覧表示する
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

利用可能なリソースを`list_resources()`で、ツールを`list_tools`で一覧表示し、出力しています。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

上記はサーバーのツールを一覧表示する例です。各ツールの名前を出力しています。

#### Java

```java
// ツールの一覧と実演
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 接続確認のためにサーバーにpingを送ることもできます
client.ping();
```

上記コードで：

- MCPサーバーから利用可能なツールを`listTools()`で取得。
- 接続確認のために`ping()`を呼び出し。
- `ListToolsResult`には名前、説明、入力スキーマなどのツール情報が含まれる。

これでサーバーの全機能を取得できました。ではそれらはいつ使うのか？このクライアントはシンプルで、機能を使いたいときに明示的に呼び出す必要があります。次章では、自身の大規模言語モデル(LLM)を持つ高度なクライアントを作りますが、まずはサーバーの機能の呼び出し方を見てみましょう：

#### Rust

メイン関数でクライアント初期化後、サーバーを初期化し機能を一覧表示できます。

```rust
// 初期化
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// ツールの一覧
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 機能を呼び出す

機能を呼び出すには正しい引数と場合によっては呼び出す名前を指定する必要があります。

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

上記コードで：

- リソースを読み取るため、`readResource()`に`uri`を指定して呼び出し。サーバー側は以下のようになっている可能性があります：

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

    `uri`の値`file://example.txt`はサーバーの`file://{name}`とマッチし、`example.txt`が`name`としてマッピングされます。

- ツール呼び出しは、`name`と`arguments`を指定して行います：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- プロンプト取得は、`getPrompt()`に`name`と`arguments`を渡して呼び出します。サーバーコードは以下の通り：

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

    それに合わせてクライアントコードは以下の通りです：

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

- `read_resource`を使い`greeting`というリソースを呼び出し。
- `call_tool`で`add`というツールを呼び出し。

#### .NET

1. ツールを呼び出すコードを追加：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. 結果を出力するコードは以下：

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// さまざまな計算ツールを呼び出す
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

上記コードで：

- `callTool()`メソッドと`CallToolRequest`オブジェクトを使い複数の電卓ツールを呼び出し。
- 各ツール呼び出しはツール名と、必要な引数の`Map`を指定。
- サーバーツールは特定のパラメータ名(例: "a"、"b")を期待する。
- 結果はサーバーからのレスポンスを含む`CallToolResult`オブジェクトとして返される。

#### Rust

```rust
// 引数={"a": 3, "b": 2}で加算ツールを呼び出す
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

### -5- クライアントを実行する

クライアントを実行するには、以下のコマンドをターミナルで入力してください：

#### TypeScript

*package.json*の"scripts"セクションに以下を追加：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

以下のコマンドでクライアントを実行：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

まず、MCPサーバーが`http://localhost:8080`で実行されていることを確認し、クライアントを実行：

```bash
# プロジェクトをビルドする
./mvnw clean compile

# クライアントを実行する
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

あるいは、ソリューションフォルダ`03-GettingStarted\02-client\solution\java`にある完全なクライアントプロジェクトを実行可能：

```bash
# ソリューションディレクトリに移動する
cd 03-GettingStarted/02-client/solution/java

# JARをビルドして実行する
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 課題

この課題では、学んだことを使って自分のクライアントを作成します。

以下のサーバーをクライアントコードから呼び出してください。機能を追加してより面白くできるか挑戦してみてください。

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

// 追加のツールを追加する
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

// stdinでメッセージの受信を開始し、stdoutでメッセージを送信する

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

このプロジェクトでプロンプトやリソースの[追加方法](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)を参照。

また、[プロンプトやリソースの呼び出し方](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)も確認してください。

### Rust

[前のセクション](../../../../03-GettingStarted/01-first-server)でRustによる簡単なMCPサーバーの作成を学びました。続けて開発するか、以下リンクのRustベースのMCPサーバー例もご覧ください：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解答例

**solutionフォルダ**には、このチュートリアルで扱った全概念を示す完全実装済みクライアントが入っています。各ソリューションはクライアント・サーバーコード両方を別々の自己完結型プロジェクトとして含んでいます。

### 📁 解答例構成

ソリューションディレクトリは言語ごとに整理されています：

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

### 🚀 各解答例に含まれるもの

各言語別ソリューションには：

- チュートリアルの全機能を備えた完全なクライアント実装
- 適切な依存関係・設定を含む動作可能なプロジェクト構成
- 簡単にセットアップ・実行できるビルド・実行スクリプト
- 言語特有の詳細なREADME
- エラーハンドリングや結果処理の例

### 📖 解答例の使い方

1. **使いたい言語のフォルダに移動**：

   ```bash
   cd solution/typescript/    # TypeScript用
   cd solution/java/          # Java用
   cd solution/python/        # Python用
   cd solution/dotnet/        # .NET用
   ```

2. **各フォルダのREADMEに従い**：
   - 依存関係のインストール
   - プロジェクトのビルド
   - クライアントの実行

3. **期待される出力例**：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

完全なドキュメントとステップごとの手順は：**[📖 Solution Documentation](./solution/README.md)**

## 🎯 完成例

このチュートリアルで扱った全プログラミング言語の、完全かつ動作するクライアント実装を提供しています。これらの例は上記機能をフルに示し、参照や独自プロジェクトの出発点として使用可能です。

### 利用可能な完成例

| 言語 | ファイル | 説明 |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSEトランスポートを使い包括的なエラーハンドリングを備えた完全なJavaクライアント |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdioトランスポートを使いサーバー自動起動付きの完全なC#クライアント |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCPプロトコル完全対応のTypeScriptクライアント |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/awaitパターンを使った完全なPythonクライアント |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokioによる非同期処理対応の完全なRustクライアント |

各完成例には以下が含まれます：
- ✅ **接続確立** とエラー処理
- ✅ **サーバー発見**（ツール、リソース、適用可能なプロンプト）
- ✅ **計算機操作**（加算、減算、乗算、除算、ヘルプ）
- ✅ **結果処理** とフォーマット済み出力
- ✅ **包括的なエラー処理**
- ✅ **クリーンでコメント付きのコード**（ステップごとのコメント込み）

### 完全な例で始める

1. 上の表から **希望の言語を選択**
2. 完全な実装を理解するために **完全な例のファイルを確認**
3. [`complete_examples.md`](./complete_examples.md) の指示に従って **例を実行**
4. 特定のユースケースに合わせて **例を変更・拡張**

これらの例の実行とカスタマイズに関する詳細なドキュメントは、**[📖 完全な例のドキュメント](./complete_examples.md)** を参照してください。

### 💡 ソリューション vs. 完全な例

| **ソリューションフォルダー** | **完全な例** |
|------------------------------|--------------|
| ビルドファイルを含む完全なプロジェクト構造 | 単一ファイルの実装例 |
| 依存関係を含みすぐに実行可能 | コードに焦点を当てた例 |
| 本番に近いセットアップ | 教育的な参考用 |
| 言語固有のツールチェイン | 複数言語の比較 |

どちらのアプローチも価値があります。完全なプロジェクトには **ソリューションフォルダー** を、学習や参照には **完全な例** を利用してください。

## 重要なポイント

この章におけるクライアントについての重要ポイントは次の通りです。

- サーバー上の機能を発見し呼び出すために使用できる。
- 自身を起動しながらサーバーも開始できる（この章のように）が、実行中のサーバーに接続することも可能。
- 前章で説明したInspectorのような代替手段と並び、サーバー機能をテストするすばらしい手段である。

## 追加リソース

- [MCPでのクライアント構築](https://modelcontextprotocol.io/quickstart/client)

## サンプル

- [Java 計算機](../samples/java/calculator/README.md)
- [.Net 計算機](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 計算機](../samples/javascript/README.md)
- [TypeScript 計算機](../samples/typescript/README.md)
- [Python 計算機](../../../../03-GettingStarted/samples/python)
- [Rust 計算機](../../../../03-GettingStarted/samples/rust)

## 次にすべきこと

- 次へ: [LLMを使ったクライアントの作成](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を用いて翻訳されました。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文の言語による文書が正式な資料としてご参照ください。重要な情報については、専門の翻訳者による翻訳を推奨いたします。本翻訳の使用により生じたいかなる誤解や誤訳に対しても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
