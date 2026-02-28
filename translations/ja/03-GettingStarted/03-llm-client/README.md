# LLMを使ったクライアントの作成

これまでに、サーバーとクライアントの作り方を見てきました。クライアントはサーバーを明示的に呼び出してツール、リソース、プロンプトの一覧を取得できました。しかし、これはあまり実用的な方法ではありません。ユーザーはエージェンシックな時代に生きており、プロンプトを使いLLMと対話することを期待しています。ユーザーはMCPで機能を管理しているかどうかには関心がなく、自然言語での対話を単純に求めているのです。では、どうすればこれを解決できるでしょうか？ 解決策は、クライアントにLLMを追加することです。

## 概要

このレッスンでは、クライアントにLLMを追加することに焦点を当て、ユーザーにとってより良い体験をどのように提供できるかを示します。

## 学習目標

このレッスンの終了時には、以下ができるようになります。

- LLMを備えたクライアントを作成する。
- LLMを用いてMCPサーバーとシームレスにやり取りする。
- クライアント側でより良いエンドユーザー体験を提供する。

## アプローチ

どのようなアプローチが必要か理解してみましょう。LLMを追加するのは簡単に聞こえますが、実際にどうやるのでしょうか？

クライアントはサーバーと以下のようにやり取りします：

1. サーバーとの接続を確立する。

1. 機能、プロンプト、リソース、ツールを一覧し、それらのスキーマを保存する。

1. LLMを追加し、保存した機能とスキーマをLLMが理解できる形式で渡す。

1. ユーザープロンプトを、クライアントがリストしたツールと共にLLMに渡して処理する。

素晴らしい、これで高レベルでの流れがわかりました。では以下の演習で試してみましょう。

## 演習：LLMを使ったクライアントの作成

この演習では、クライアントにLLMを追加する方法を学びます。

### GitHubパーソナルアクセストークンを使った認証

GitHubトークンの作成は簡単です。以下のように行います：

- GitHubの設定画面へ – 右上のプロフィールアイコンをクリックして設定を選択。
- 開発者設定へ移動 – 下にスクロールして「Developer Settings」をクリック。
- パーソナルアクセストークンを選択 – 「Fine-grained tokens」をクリックし、「Generate new token」を選択。
- トークンの設定 – 参照用のメモを追加し、有効期限を設定し、必要な権限（スコープ）を選択します。今回のケースではModels権限を必ず追加してください。
- トークンの生成とコピー – 「Generate token」をクリックし、表示されるトークンを必ずすぐコピーしてください。後で再表示はできません。

### -1- サーバーに接続

まずはクライアントを作成しましょう。

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // スキーマ検証のためにzodをインポートする

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", 
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }
}
```

前のコードでは以下を行いました：

- 必要なライブラリをインポート
- `client` と `openai` という2つのメンバーを持つクラスを作成し、それぞれクライアント管理とLLMとのやり取りに使用
- `baseUrl`を推論APIに設定してGitHub Modelsを使うようにLLMインスタンスを設定

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

前のコードでは以下を行いました：

- MCP用の必要なライブラリをインポート
- クライアントを作成

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

まず、`pom.xml`にLangChain4jの依存関係を追加します。これによりMCP連携とGitHub Modelsのサポートが有効になります。

```xml
<properties>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
</properties>

<dependencies>
    <!-- LangChain4j MCP Integration -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-mcp</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- OpenAI Official API Client -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-open-ai-official</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- GitHub Models Support -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-github-models</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

次にJavaクライアントクラスを作成します：

```java
import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // LLM を GitHub モデルを使用するように設定する
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // サーバーに接続するための MCP トランスポートを作成する
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP クライアントを作成する
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

前のコードでは以下を行いました：

- **LangChain4j依存関係の追加**：MCP連携、OpenAI公式クライアント、GitHub Modelsサポートを含む
- **LangChain4jライブラリのインポート**：MCP連携とOpenAIチャットモデル機能のため
- **ChatLanguageModelの作成**：GitHubトークンでGitHub Modelsを使うよう設定
- **HTTPトランスポートのセットアップ**：Server-Sent Events (SSE) を使いMCPサーバーと接続
- **MCPクライアントの作成**：サーバーとの通信を担当
- **LangChain4jのMCPサポート活用**：LLMとMCPサーバーの統合を簡素化

#### Rust

この例ではRust製のMCPサーバーを動かしていることが前提です。お持ちでない場合は[01-first-server](../01-first-server/README.md)レッスンを参照してサーバーを作成してください。

Rust MCPサーバーを用意したら、ターミナルを開きサーバーと同じディレクトリに移動し、以下のコマンドで新しいLLMクライアントプロジェクトを作成します。

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml`ファイルに以下の依存関係を追加してください：

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Rust向けの公式OpenAIライブラリはありませんが、`async-openai`クレートは[コミュニティ維持のライブラリ](https://platform.openai.com/docs/libraries/rust#rust)としてよく使われています。

`src/main.rs`を開き、内容を次のコードに置き換えます：

```rust
use async_openai::{Client, config::OpenAIConfig};
use rmcp::{
    RmcpError,
    model::{CallToolRequestParam, ListToolsResult},
    service::{RoleClient, RunningService, ServiceExt},
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use serde_json::{Value, json};
use std::error::Error;
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // 初期メッセージ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAIクライアントを設定
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCPクライアントを設定
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("calculator-server");

    let mcp_client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: MCPツールのリストを取得

    // TODO: ツール呼び出しを伴うLLM会話

    Ok(())
}
```

このコードは基本的なRustアプリケーションをセットアップし、MCPサーバーおよびGitHub Modelsと連携してLLMインタラクションを可能にします。

> [!IMPORTANT]
> 実行前に必ず`OPENAI_API_KEY`環境変数にGitHubトークンを設定してください。

良いですね。次のステップとしてサーバーの機能を一覧表示しましょう。

### -2- サーバー機能の一覧表示

サーバーに接続して機能を問い合わせます。

#### TypeScript

同じクラスに以下のメソッドを追加します：

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ツールの一覧表示
    const toolsResult = await this.client.listTools();
}
```

前のコードでは以下を行いました：

- サーバー接続用メソッド`connectToServer`を追加
- `run`メソッドを作成し、アプリのフローを管理。現在はツール一覧表示のみだが後で拡張予定

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
    print("Tool", tool.inputSchema["properties"])
```

追加した内容：

- リソースとツールを一覧し、出力。ツールについては後で使うため`inputSchema`も表示している

#### .NET

```csharp
async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        // TODO: convert tool definition from MCP tool to LLm tool     
    }

    return toolDefinitions;
}
```

前のコードでは以下を行いました：

- MCPサーバー上の利用可能なツールの一覧表示
- 各ツールについて名前、説明、スキーマを取得。スキーマは後でツール呼び出しに使う予定

#### Java

```java
// MCPツールを自動的に検出するツールプロバイダーを作成します
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCPツールプロバイダーは以下を自動的に処理します：
// - MCPサーバーから利用可能なツールの一覧取得
// - MCPツールのスキーマをLangChain4j形式に変換
// - ツールの実行とレスポンスの管理
```

前のコードでは以下を行いました：

- MCPサーバーから自動的にツールを発見し登録する`McpToolProvider`を作成
- ツールプロバイダーはMCPのツールスキーマとLangChain4jのツール形式を内部で変換
- これによりツールの手動列挙と変換処理が抽象化される

#### Rust

MCPサーバーからツールを取得するには`list_tools`メソッドを使います。`main`関数内でMCPクライアントをセットアップした後、以下のコードを追加してください：

```rust
// MCPツールのリストを取得する
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- サーバー機能をLLMツールに変換

次はサーバーの機能一覧をLLMが理解できるツール形式に変換します。こうしてLLMにツールとして提供できるようにします。

#### TypeScript

1. MCPサーバーからの応答をLLMが利用可能なツール形式に変換するコードを追加：

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // 入力スキーマに基づいてzodスキーマを作成する
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // 明示的にタイプを「function」に設定する
            function: {
            name: tool.name,
            description: tool.description,
            parameters: {
            type: "object",
            properties: tool.input_schema.properties,
            required: tool.input_schema.required,
            },
            },
        };
    }

    ```

    上記コードはMCPサーバーからの応答を受け取り、LLMが理解可能なツール定義に変換するものです。

1. `run`メソッドを次のようにアップデートしてサーバー機能を一覧表示します：

    ```typescript
    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
            });
        });
    }
    ```

    このコードでは`run`メソッドで結果をマッピングし、それぞれに`openAiToolAdapter`を呼んでいます。

#### Python

1. まず変換関数を作成します：

    ```python
    def convert_to_llm_tool(tool):
        tool_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "type": "function",
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema["properties"]
                }
            }
        }

        return tool_schema
    ```

    `convert_to_llm_tools`関数はMCPツールの応答をLLMが理解できる形式に変換します。

1. 次にクライアントコードを更新してこの関数を活用します：

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    MCPツールの応答をLLMに渡せる形に変換するため`convert_to_llm_tool`を呼んでいます。

#### .NET

1. MCPツール応答をLLMが理解可能な形式に変換するコードを追加：

```csharp
ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}
```

前のコードでは以下を行いました：

- 名前、説明、入力スキーマを受け取り、`ConvertFrom`関数を作成
- `FunctionDefinition`を作成し、それを`ChatCompletionsDefinition`に渡す機能を定義。後者はLLMが理解可能

1. この関数を使うために既存コードをどうアップデートするか見てみましょう：

    ```csharp
    async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            JsonElement propertiesElement;
            tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

            var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);

            Console.WriteLine($"Properties: {propertiesElement}");        
        }

        return toolDefinitions;
    }
    ```    In the preceding code, we've:

    - Update the function to convert the MCP tool response to an LLm tool. Let's highlight the code we added:

        ```csharp
        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
        ```

        The input schema is part of the tool response but on the "properties" attribute, so we need to extract. Furthermore, we now call `ConvertFrom` with the tool details. Now we've done the heavy lifting, let's see how it call comes together as we handle a user prompt next.

#### Java

```java
// 自然言語での対話用のBotインターフェースを作成する
public interface Bot {
    String chat(String prompt);
}

// LLMおよびMCPツールを使用してAIサービスを設定する
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

前のコードでは以下を行いました：

- 自然言語対話用のシンプルな`Bot`インターフェイスを定義
- LangChain4jの`AiServices`を用いてLLMとMCPツールプロバイダーを自動でバインド
- フレームワークがツールスキーマの変換と関数呼び出しを自動で処理
- 手動でのツール変換が不要で、複雑な変換処理をLangChain4jが吸収

#### Rust

MCPツール応答をLLMが理解できる形式に変換する補助関数を追加します。`main`関数の下に以下を追加してください。これはLLMへのリクエスト時に呼び出されます：

```rust
async fn format_tools(tools: &ListToolsResult) -> Result<Vec<Value>, Box<dyn Error>> {
    let tools_json = serde_json::to_value(tools)?;
    let Some(tools_array) = tools_json.get("tools").and_then(|t| t.as_array()) else {
        return Ok(vec![]);
    };

    let formatted_tools = tools_array
        .iter()
        .filter_map(|tool| {
            let name = tool.get("name")?.as_str()?;
            let description = tool.get("description")?.as_str()?;
            let schema = tool.get("inputSchema")?;

            Some(json!({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": {
                        "type": "object",
                        "properties": schema.get("properties").unwrap_or(&json!({})),
                        "required": schema.get("required").unwrap_or(&json!([]))
                    }
                }
            }))
        })
        .collect();

    Ok(formatted_tools)
}
```

よし、ユーザーリクエストを扱う準備ができました。次はそれに取り組みましょう。

### -4- ユーザープロンプトの処理

この部分のコードでユーザーリクエストを処理します。

#### TypeScript

1. LLM呼び出し用のメソッドを追加：

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. サーバーのツールを呼び出す
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 結果を使って何かをする
        // TODO

        }
    }
    ```

    前のコードでは：

    - `callTools`メソッドを追加
    - LLMの応答を受け取り、呼び出すべきツールがあるかチェック

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ツールを呼び出す
        }
        ```

    - 呼び出すべきツールがあれば実行：

        ```typescript
        // 2. サーバーのツールを呼び出す
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 結果を使って何かを行う
        // TODO
        ```

1. `run`メソッドを更新してLLM呼び出しと`callTools`の利用を含めます：

    ```typescript

    // 1. LLM の入力となるメッセージを作成する
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM を呼び出す
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM の応答を確認し、各選択肢にツール呼び出しがあるかチェックする
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

素晴らしい。完全なコードを表示します：

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // スキーマ検証のためにzodをインポートする

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // 将来的にこのURLに変更する可能性があります: https://models.github.ai/inference
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }

    async connectToServer(transport: Transport) {
        await this.client.connect(transport);
        this.run();
        console.error("MCPClient started on stdin/stdout");
    }

    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
          }) {
          // input_schemaに基づいてzodスキーマを作成する
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // typeを明示的に"function"に設定する
            function: {
              name: tool.name,
              description: tool.description,
              parameters: {
              type: "object",
              properties: tool.input_schema.properties,
              required: tool.input_schema.required,
              },
            },
          };
    }
    
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
      ) {
        for (const tool_call of tool_calls) {
          const toolName = tool_call.function.name;
          const args = tool_call.function.arguments;
    
          console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);
    
    
          // 2. サーバーのツールを呼び出す
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. 結果を使って何かを行う
          // TODO
    
         }
    }

    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
              name: tool.name,
              description: tool.description,
              input_schema: tool.inputSchema,
            });
        });

        const prompt = "What is the sum of 2 and 3?";
    
        const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

        console.log("Querying LLM: ", messages[0].content);
        let response = this.openai.chat.completions.create({
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLMの応答を確認し、各選択肢にツール呼び出しがあるかどうかをチェックする
        (await response).choices.map(async (choice: { message: any; }) => {
          const message = choice.message;
          if (message.tool_calls) {
              console.log("Making tool call")
              await this.callTools(message.tool_calls, results);
          }
        });
    }
    
}

let client = new MyClient();
 const transport = new StdioClientTransport({
            command: "node",
            args: ["./build/index.js"]
        });

client.connectToServer(transport);
```

#### Python

1. LLM呼び出しに必要なインポートを追加：

    ```python
    # 大規模言語モデル
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. 続いてLLMを呼び出す関数を追加：

    ```python
    # 大規模言語モデル

    def call_llm(prompt, functions):
        token = os.environ["GITHUB_TOKEN"]
        endpoint = "https://models.inference.ai.azure.com"

        model_name = "gpt-4o"

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        print("CALLING LLM")
        response = client.complete(
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant.",
                },
                {
                "role": "user",
                "content": prompt,
                },
            ],
            model=model_name,
            tools = functions,
            # オプションのパラメータ
            temperature=1.,
            max_tokens=1000,
            top_p=1.    
        )

        response_message = response.choices[0].message
        
        functions_to_call = []

        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                print("TOOL: ", tool_call)
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                functions_to_call.append({ "name": name, "args": args })

        return functions_to_call
    ```

    前のコードでは：

    - MCPサーバー上の関数をLLMに渡している
    - LLMを関数付きで呼び出し
    - 結果を検査し呼ぶべき関数を判定
    - 呼び出す関数の配列を渡している

1. 最後にメインコードを更新：

    ```python
    prompt = "Add 2 to 20"

    # もしあれば、利用可能なツールをLLMに尋ねる
    functions_to_call = call_llm(prompt, functions)

    # 推奨される関数を呼び出す
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    これで最後のステップとなります。上記コードでは：

    - LLMの判断で呼び出すべき関数を持つツールを`call_tool`で呼び出し
    - ツール呼び出しの結果をMCPサーバーから受け取り表示

#### .NET

1. LLMプロンプトリクエストのコード例：

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new ChatRequestUserMessage(userMessage));

    // 1. Define tools
    ChatCompletionsToolDefinition def = CreateToolDefinition();


    // 2. Define options, including the tools
    var options = new ChatCompletionsOptions(chatHistory)
    {
        Model = "gpt-4.1-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    前のコードでは：

    - MCPサーバーからツールを取得、`var tools = await GetMcpTools()`。
    - ユーザープロンプト`userMessage`を定義。
    - モデルとツールを指定したオプションオブジェクトを作成。
    - LLMへリクエスト送信。

1. 最後に、LLMが関数呼び出しを要求しているか確認：

    ```csharp
    // 4. Check if the response contains a function call
    ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
        var result = await mcpClient.CallToolAsync(
            call.Name,
            dict!,
            cancellationToken: CancellationToken.None
        );

        Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

    }
    ```

    前のコードでは：

    - 関数呼び出しリストをループ
    - 各ツール呼び出しの名前と引数を解析し、MCPクライアントでツール実行。結果を表示。

完全なコードはこちら：

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;

var endpoint = "https://models.inference.ai.azure.com";
var token = Environment.GetEnvironmentVariable("GITHUB_TOKEN"); // Your GitHub Access Token
var client = new ChatCompletionsClient(new Uri(endpoint), new AzureKeyCredential(token));
var chatHistory = new List<ChatRequestMessage>
{
    new ChatRequestSystemMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}



async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);

        Console.WriteLine($"Properties: {propertiesElement}");        
    }

    return toolDefinitions;
}

// 1. List tools on mcp server

var tools = await GetMcpTools();
for (int i = 0; i < tools.Count; i++)
{
    var tool = tools[i];
    Console.WriteLine($"MCP Tools def: {i}: {tool}");
}

// 2. Define the chat history and the user message
var userMessage = "add 2 and 4";

chatHistory.Add(new ChatRequestUserMessage(userMessage));


// 3. Define options, including the tools
var options = new ChatCompletionsOptions(chatHistory)
{
    Model = "gpt-4.1-mini",
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletions? response = await client.CompleteAsync(options);
var content = response.Content;

// 5. Check if the response contains a function call
ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
    var result = await mcpClient.CallToolAsync(
        call.Name,
        dict!,
        cancellationToken: CancellationToken.None
    );

    Console.WriteLine(result.Content.OfType<TextContentBlock>().First().Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // MCPツールを自動的に使用する自然言語のリクエストを実行する
    String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
    System.out.println(response);

    response = bot.chat("What's the square root of 144?");
    System.out.println(response);

    response = bot.chat("Show me the help for the calculator service");
    System.out.println(response);
} finally {
    mcpClient.close();
}
```

前のコードでは：

- シンプルな自然言語プロンプトでMCPサーバーツールと対話
- LangChain4jフレームワークが以下を自動処理：
  - 必要に応じてユーザープロンプトをツール呼び出しに変換
  - LLMの判断に基づき適切なMCPツールを呼び出し
  - LLMとMCPサーバー間の会話フロー管理
- `bot.chat()`メソッドはMCPツールの結果を含む自然言語応答を返す
- ユーザーはMCPの実装を意識せずにシームレスに利用可能

完全なコード例：

```java
public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .timeout(Duration.ofSeconds(60))
                .build();

        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();

        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        Bot bot = AiServices.builder(Bot.class)
                .chatLanguageModel(model)
                .toolProvider(toolProvider)
                .build();

        try {
            String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
            System.out.println(response);

            response = bot.chat("What's the square root of 144?");
            System.out.println(response);

            response = bot.chat("Show me the help for the calculator service");
            System.out.println(response);
        } finally {
            mcpClient.close();
        }
    }
}
```

#### Rust

ここが主な処理の場所です。初回のユーザープロンプトでLLMを呼び、その応答から必要なツール呼び出しを判定します。もしあればツールを呼び出し、さらにLLMとの対話を続け、ツール呼び出しが不要になるまで繰り返します。

数回にわたるLLM呼び出しがあるため、LLM呼び出しを処理する関数を定義しましょう。`main.rs`に以下を追加：

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": "openai/gpt-4.1",
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

この関数はLLMクライアント、メッセージリスト（ユーザープロンプトを含む）、MCPサーバーのツール群を受けて、LLMにリクエストを送り応答を返します。
LLMからの応答には`choices`の配列が含まれています。結果を処理して`tool_calls`が存在するかどうかを確認する必要があります。これにより、LLMが引数付きで特定のツールを呼び出すことを要求していることが分かります。以下のコードを`main.rs`ファイルの末尾に追加して、LLM応答を処理する関数を定義してください。

```rust
async fn process_llm_response(
    llm_response: &Value,
    mcp_client: &RunningService<RoleClient, ()>,
    openai_client: &Client<OpenAIConfig>,
    mcp_tools: &ListToolsResult,
    messages: &mut Vec<Value>,
) -> Result<(), Box<dyn Error>> {
    let Some(message) = llm_response
        .get("choices")
        .and_then(|c| c.as_array())
        .and_then(|choices| choices.first())
        .and_then(|choice| choice.get("message"))
    else {
        return Ok(());
    };

    // コンテンツが利用可能な場合に印刷する
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ツール呼び出しを処理する
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // アシスタントメッセージを追加する

        // 各ツール呼び出しを実行する
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // メッセージにツール結果を追加する
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ツール結果で会話を続ける
        let response = call_llm(openai_client, messages, mcp_tools).await?;
        Box::pin(process_llm_response(
            &response,
            mcp_client,
            openai_client,
            mcp_tools,
            messages,
        ))
        .await?;
    }
    Ok(())
}
```

`tool_calls`が存在する場合は、ツール情報を抽出し、ツールリクエストをMCPサーバーに送信し、その結果を会話メッセージに追加します。その後、LLMとの会話を続け、メッセージはアシスタントの応答とツール呼び出し結果で更新されます。

LLMがMCP呼び出しのために返すツールコール情報を抽出するために、呼び出しに必要なすべてを抽出する別のヘルパー関数を追加します。以下のコードを`main.rs`ファイルの末尾に追加してください。

```rust
fn extract_tool_call_info(tool_call: &Value) -> Result<(String, String, String), Box<dyn Error>> {
    let tool_id = tool_call
        .get("id")
        .and_then(|id| id.as_str())
        .unwrap_or("")
        .to_string();
    let function = tool_call.get("function").ok_or("Missing function")?;
    let name = function
        .get("name")
        .and_then(|n| n.as_str())
        .unwrap_or("")
        .to_string();
    let args = function
        .get("arguments")
        .and_then(|a| a.as_str())
        .unwrap_or("{}")
        .to_string();
    Ok((tool_id, name, args))
}
```

すべてのパーツが揃ったので、最初のユーザープロンプトを処理してLLMを呼び出せるようになりました。`main`関数を以下のコードで更新してください。

```rust
// ツール呼び出しを含むLLM会話
let response = call_llm(&openai_client, &messages, &tools).await?;
process_llm_response(
    &response,
    &mcp_client,
    &openai_client,
    &tools,
    &mut messages,
)
.await?;
```

これにより、2つの数字の合計を求める最初のユーザープロンプトを使ってLLMに問い合わせ、レスポンスを処理して動的にツール呼び出しを処理します。

素晴らしい、できましたね！

## 課題

演習のコードをもとに、さらにいくつかのツールを持つサーバーを構築してください。その後、演習のようにLLMを使ったクライアントを作成し、さまざまなプロンプトでテストして、すべてのサーバーツールが動的に呼び出されることを確認してください。このようなクライアントの構築方法は、最終ユーザーが正確なクライアントコマンドではなくプロンプトで操作でき、MCPサーバーの呼び出しを意識せずに済むため、優れたユーザー体験を提供します。

## ソリューション

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## 重要なポイント

- クライアントにLLMを追加すると、ユーザーがMCPサーバーとより良く対話する方法が提供されます。
- MCPサーバーの応答をLLMが理解できる形式に変換する必要があります。

## サンプル

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## 追加リソース

## 次にやること

- 次へ: [Visual Studio Codeを使ったサーバーの利用](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。原文の言語での文書を正式な情報源としてご参照ください。重要な情報については、専門の翻訳者による翻訳を推奨します。本翻訳の使用によって生じたいかなる誤解や解釈の相違についても、一切責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->