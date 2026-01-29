# クライアントの作成

クライアントは、MCPサーバーと直接通信してリソース、ツール、プロンプトを要求するカスタムアプリケーションやスクリプトです。サーバーと対話するためのグラフィカルインターフェースを提供するインスペクターツールを使用する場合とは異なり、自分自身でクライアントを作成することで、プログラム的かつ自動化された対話が可能になります。これにより、開発者はMCPの機能を自分のワークフローに統合し、タスクを自動化し、特定のニーズに合わせたカスタムソリューションを構築することができます。

## 概要

このレッスンでは、Model Context Protocol (MCP) エコシステム内でのクライアントの概念を紹介します。自分自身のクライアントを作成し、それをMCPサーバーに接続する方法を学びます。

## 学習目標

このレッスンの終わりまでに、以下ができるようになります：

- クライアントが何をできるかを理解する。
- 自分自身のクライアントを作成する。
- MCPサーバーに接続し、期待通りに動作するかテストする。

## クライアント作成の手順

クライアントを作成するには、以下の手順が必要です：

- **適切なライブラリをインポートする**。以前使用したライブラリと同じですが、異なる構造を使用します。
- **クライアントをインスタンス化する**。クライアントインスタンスを作成し、選択したトランスポートメソッドに接続します。
- **リストするリソースを決定する**。MCPサーバーにはリソース、ツール、プロンプトが用意されているため、どれをリストするかを決定します。
- **クライアントをホストアプリケーションに統合する**。サーバーの機能を理解したら、ホストアプリケーションに統合し、ユーザーがプロンプトやコマンドを入力した際に対応するサーバー機能が呼び出されるようにします。

これで、全体的な流れを理解しましたので、次に例を見てみましょう。

### クライアントの例

以下はクライアントの例です：

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

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

上記のコードでは以下を行っています：

- ライブラリをインポートする。
- クライアントのインスタンスを作成し、stdioを使用してトランスポートに接続する。
- プロンプト、リソース、ツールをリストし、それらをすべて呼び出す。

これで、MCPサーバーと通信できるクライアントが完成しました。

次の演習セクションでは、コードを分解して各部分を説明していきます。

## 演習：クライアントの作成

前述の通り、コードを説明しながら進めていきます。コードを書きながら進めても構いません。

### -1- ライブラリのインポート

必要なライブラリをインポートします。クライアントと選択したトランスポートプロトコル（今回はstdio）への参照が必要です。stdioはローカルマシンで実行されるもの向けのプロトコルです。SSEは別のトランスポートプロトコルで、今後の章で紹介しますが、もう一つの選択肢です。今回はstdioを使って進めましょう。

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
using ModelContextProtocol.Protocol.Transport;
```

#### Java

Javaの場合、前の演習で作成したMCPサーバーに接続するクライアントを作成します。[Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) のJava Spring Bootプロジェクト構造を使用して、`SDKClient`という新しいJavaクラスを`src/main/java/com/microsoft/mcp/sample/client/`フォルダーに作成し、以下のインポートを追加します：

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

`Cargo.toml`ファイルに以下の依存関係を追加する必要があります。

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

その後、クライアントコードで必要なライブラリをインポートします。

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

次に、インスタンス化に進みましょう。

### -2- クライアントとトランスポートのインスタンス化

トランスポートのインスタンスとクライアントのインスタンスを作成する必要があります：

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

上記のコードでは以下を行っています：

- stdioトランスポートインスタンスを作成。サーバーを見つけて起動するためのコマンドと引数を指定する必要があることに注意してください。

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

- 選択したトランスポートにクライアントを接続。

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

上記のコードでは以下を行っています：

- 必要なライブラリをインポート。
- サーバーパラメータオブジェクトをインスタンス化。これを使用してサーバーを実行し、クライアントで接続できるようにします。
- `run`メソッドを定義。このメソッドは`stdio_client`を呼び出し、クライアントセッションを開始します。
- エントリーポイントを作成し、`asyncio.run`に`run`メソッドを提供。

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

上記のコードでは以下を行っています：

- 必要なライブラリをインポート。
- stdioトランスポートを作成し、クライアント`mcpClient`を作成。このクライアントを使用してMCPサーバーの機能をリストおよび呼び出します。

注意："Arguments"では、*.csproj*または実行可能ファイルを指定できます。

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
        
        // Your client logic goes here
    }
}
```

上記のコードでは以下を行っています：

- MCPサーバーが実行される`http://localhost:8080`を指すSSEトランスポートを設定するメインメソッドを作成。
- トランスポートをコンストラクタパラメータとして受け取るクライアントクラスを作成。
- `run`メソッドで、トランスポートを使用して同期MCPクライアントを作成し、接続を初期化。
- Java Spring Boot MCPサーバーとのHTTPベースの通信に適したSSE（Server-Sent Events）トランスポートを使用。

#### Rust

このRustクライアントは、同じディレクトリ内の兄弟プロジェクト「calculator-server」をサーバーとして想定しています。以下のコードはサーバーを起動し、それに接続します。

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
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

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- サーバー機能のリスト

これで、プログラムを実行すればクライアントが接続できるようになりました。ただし、まだ機能をリストしていないので、次にそれを行います：

#### TypeScript

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

#### Python

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ここでは、利用可能なリソース`list_resources()`とツール`list_tools`をリストし、それらを出力します。

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

上記は、サーバー上のツールをリストする方法の例です。各ツールについて、その名前を出力します。

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

上記のコードでは以下を行っています：

- MCPサーバーから利用可能なツールをすべて取得するために`listTools()`を呼び出し。
- サーバーへの接続が機能していることを確認するために`ping()`を使用。
- `ListToolsResult`には、ツールの名前、説明、入力スキーマなどの情報が含まれています。

これで、すべての機能をキャプチャしました。次の問題は、それらをいつ使用するかです。このクライアントは非常にシンプルで、サーバーの機能を明示的に呼び出す必要があります。次の章では、独自の大規模言語モデル（LLM）にアクセスできるより高度なクライアントを作成します。今回は、サーバーの機能を呼び出す方法を見てみましょう：

#### Rust

クライアントを初期化した後、サーバーを初期化し、その機能をいくつかリストできます。

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 機能の呼び出し

機能を呼び出すには、正しい引数と場合によっては呼び出す対象の名前を指定する必要があります。

#### TypeScript

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

上記のコードでは以下を行っています：

- リソースを読み取る。`readResource()`を呼び出し、`uri`を指定します。サーバー側では以下のようになります：

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

    クライアント側の`uri`値`file://example.txt`はサーバー側の`file://{name}`に一致します。`example.txt`は`name`にマッピングされます。

- ツールを呼び出す。`name`と`arguments`を指定して呼び出します：

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- プロンプトを取得する。`getPrompt()`を`name`と`arguments`で呼び出します。サーバーコードは以下のようになります：

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

    そのため、クライアントコードは以下のようになります：

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
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

上記のコードでは以下を行っています：

- `read_resource`を使用して`greeting`というリソースを呼び出し。
- `call_tool`を使用して`add`というツールを呼び出し。

#### .NET

1. ツールを呼び出すコードを追加：

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. 結果を出力するコードを追加：

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call various calculator tools
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

上記のコードでは以下を行っています：

- `CallToolRequest`オブジェクトを使用して`callTool()`メソッドで複数の計算ツールを呼び出し。
- 各ツール呼び出しで、ツール名とそのツールに必要な引数の`Map`を指定。
- サーバーツールは特定のパラメータ名（例："a"、"b"）を期待。
- 結果はサーバーからの応答を含む`CallToolResult`オブジェクトとして返されます。

#### Rust

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
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

クライアントを実行するには、ターミナルで以下のコマンドを入力します：

#### TypeScript

*package.json*の"scripts"セクションに以下のエントリを追加：

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

以下のコマンドでクライアントを呼び出します：

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

まず、MCPサーバーが`http://localhost:8080`で実行されていることを確認します。その後、クライアントを実行します：

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

または、`03-GettingStarted\02-client\solution\java`フォルダーにある完全なクライアントプロジェクトを実行できます：

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 課題

この課題では、学んだ内容を活用して独自のクライアントを作成します。

以下のサーバーを使用して、クライアントコードを介して呼び出します。サーバーに機能を追加して、より興味深いものにしてみてください。

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout

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

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
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

このプロジェクトを参照して[プロンプトとリソースを追加する方法](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)を確認してください。

また、[プロンプトとリソースを呼び出す方法](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)も確認してください。

### Rust

[前のセクション](../../../../03-GettingStarted/01-first-server)で、Rustを使用して簡単なMCPサーバーを作成する方法を学びました。それを基に構築するか、以下のリンクでRustベースのMCPサーバーの例を確認してください：[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 解答

**解答フォルダー**には、このチュートリアルで説明したすべての概念を示す完全なクライアント実装が含まれています。各解答には、クライアントとサーバーコードが別々の自己完結型プロジェクトとして整理されています。

### 📁 解答構造

解答ディレクトリはプログラミング言語ごとに整理されています：

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

### 🚀 各解答に含まれる内容

各言語固有の解答には以下が含まれます：

- **完全なクライアント実装**（チュートリアルのすべての機能を含む）
- **適切な依存関係と設定を備えたプロジェクト構造**
- **簡単にセットアップして実行できるビルドおよび実行スクリプト**
- **言語固有の指示を含む詳細なREADME**
- **エラーハンドリング**と結果処理の例

### 📖 解答の使用方法

1. **希望する言語フォルダーに移動**：

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **各フォルダーのREADME指示に従う**：
   - 依存関係のインストール
   - プロジェクトのビルド
   - クライアントの実行

3. **期待される出力例**：

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

完全なドキュメントとステップバイステップの指示については、**[📖 解答ドキュメント](./solution/README.md)** を参照してください。

## 🎯 完全な例

このチュートリアルで説明したすべての機能を示す完全なクライアント実装を提供しています。これらの例は、参考実装や独自プロジェクトの出発点として使用できます。

### 利用可能な完全な例

| 言語       | ファイル                          | 説明                                                                 |
|------------|-----------------------------------|----------------------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSEトランスポートを使用した完全なJavaクライアント（包括的なエラーハンドリング付き） |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdioトランスポートを使用した完全なC#クライアント（自動サーバー起動付き）         |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCPプロトコル完全対応のTypeScriptクライアント                           |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/awaitパターンを使用した完全なPythonクライアント                   |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)     | Tokioを使用した非同期操作対応の完全なRustクライアント                   |
各完全な例には以下が含まれます：

- ✅ **接続の確立**とエラーハンドリング  
- ✅ **サーバーの探索**（ツール、リソース、プロンプトが適用可能な場合）  
- ✅ **計算機の操作**（加算、減算、乗算、除算、ヘルプ）  
- ✅ **結果の処理**とフォーマットされた出力  
- ✅ **包括的なエラーハンドリング**  
- ✅ **クリーンで文書化されたコード**（ステップごとのコメント付き）  

### 完全な例で始める

1. 上記の表から**希望する言語を選択**してください  
2. **完全な例ファイルを確認**して、実装全体を理解してください  
3. [`complete_examples.md`](./complete_examples.md)の指示に従って**例を実行**してください  
4. **特定のユースケースに合わせて例を修正・拡張**してください  

これらの例を実行およびカスタマイズする詳細なドキュメントについては、**[📖 完全な例のドキュメント](./complete_examples.md)** をご覧ください。

### 💡 ソリューション vs 完全な例

| **ソリューションフォルダ** | **完全な例** |
|--------------------|--------------------- |
| ビルドファイルを含む完全なプロジェクト構造 | 単一ファイルの実装 |
| 依存関係を含むすぐに実行可能な形式 | コード例に焦点を当てた内容 |
| 実際の運用に近いセットアップ | 教育的な参考資料 |
| 言語固有のツール | 複数言語の比較 |

どちらのアプローチも価値があります。**ソリューションフォルダ**は完全なプロジェクト向けに、**完全な例**は学習と参考資料として活用してください。

## 重要なポイント

この章の重要なポイントは、クライアントに関する以下の内容です：

- サーバー上の機能を発見し、呼び出すために使用できます。  
- 自身が起動する際にサーバーを開始することもできます（この章のように）。ただし、クライアントは既存のサーバーに接続することも可能です。  
- 前章で説明したInspectorのような代替手段と並んで、サーバーの機能をテストする優れた方法です。  

## 追加リソース

- [MCPでのクライアント構築](https://modelcontextprotocol.io/quickstart/client)

## サンプル

- [Java計算機](../samples/java/calculator/README.md)  
- [.Net計算機](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript計算機](../samples/javascript/README.md)  
- [TypeScript計算機](../samples/typescript/README.md)  
- [Python計算機](../../../../03-GettingStarted/samples/python)  
- [Rust計算機](../../../../03-GettingStarted/samples/rust)  

## 次のステップ

- 次へ: [LLMを使用したクライアントの作成](../03-llm-client/README.md)  

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。
