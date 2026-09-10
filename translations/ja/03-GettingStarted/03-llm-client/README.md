# LLMを使ったクライアントの作成

これまでに、サーバーとクライアントの作成方法を見てきました。クライアントはサーバーを明示的に呼び出して、そのツール、リソース、プロンプトをリストアップできました。しかし、これはあまり実用的な方法ではありません。ユーザーはエージェンシックな時代に生きており、プロンプトを使いLLMとやり取りすることを期待しています。彼らは、あなたがMCPを使って能力を管理しているかどうかは気にしません。単に自然言語を使って対話できることを望んでいます。では、これをどう解決するのでしょうか？解決策は、クライアントにLLMを追加することです。

## 概要

このレッスンでは、クライアントにLLMを追加することに焦点を当て、これがどのようにユーザーにとってより良い体験を提供するかを示します。

## 学習目標

このレッスンを終えると、以下ができるようになります：

- LLMを使ったクライアントを作成する。
- LLMを使ってMCPサーバーとシームレスにやり取りする。
- クライアント側でより良いエンドユーザー体験を提供する。

## アプローチ

必要なアプローチを理解してみましょう。LLMを追加するのは簡単に聞こえますが、実際にどうするのでしょう？

クライアントがサーバーとどのようにやり取りするかは以下の通りです：

1. サーバーとの接続を確立する。

1. 能力、プロンプト、リソース、ツールをリストし、それらのスキーマを保存する。

1. LLMを追加し、保存した能力とそのスキーマをLLMが理解できる形式で渡す。

1. ユーザープロンプトを受け取り、それをクライアントがリストしたツールと共にLLMへ渡す。

素晴らしい、これで大まかに方法は理解できました。では、以下の演習で実際にやってみましょう。

## 演習：LLMを使ったクライアントの作成

この演習では、クライアントにLLMを追加する方法を学びます。

### GitHubパーソナルアクセストークンを使った認証

GitHubトークンの作成は簡単です。手順は以下の通りです：

- GitHub設定へ移動 — 右上のプロフィール画像をクリックし、設定を選択。
- 開発者設定へ移動 — 下にスクロールして「Developer Settings」をクリック。
- パーソナルアクセストークンを選択 — 「Fine-grained tokens」をクリックし、新しいトークンを生成。
- トークンを設定 — 参照用のメモ、期限を設定し、必要な権限（スコープ）を選択。今回は必ずModels権限を追加してください。
- トークンを生成してコピー — 「Generate token」をクリックし、生成されたトークンをすぐにコピーしてください。後から見られません。

### -1- サーバーへの接続

まずはクライアントを作成しましょう：

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
  
上記コードでは：

- 必要なライブラリをインポートしました
- `client` と `openai` の2つのメンバーを持つクラスを作成し、それぞれクライアント管理とLLMとのやり取りを助けます
- LLMインスタンスをGitHub Modelsを使うように設定し、`baseUrl`を推論APIのURLに設定しました

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
  
上記コードでは：

- MCPで必要なライブラリをインポートしました
- クライアントを作成しました

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

まず、`pom.xml` ファイルにLangChain4jの依存関係を追加してください。これによりMCP統合とGitHub Modelsサポートが可能になります：

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
  
次にJavaのクライアントクラスを作成します：

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
    
    public static void main(String[] args) throws Exception {        // LLMをGitHubモデルを使用するように設定する
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // サーバーに接続するためのMCPトランスポートを作成する
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCPクライアントを作成する
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```
  
上記コードでは：

- **LangChain4j依存関係の追加**：MCP統合、OpenAI公式クライアント、GitHub Modelsサポートのため
- **LangChain4jのライブラリをインポート**：MCP統合とOpenAIチャットモデルの機能のため
- **`ChatLanguageModel`を作成**：GitHubトークンを用いGitHub Modelsを使うように設定
- **HTTPトランスポートを設定**：Server-Sent Events (SSE)でMCPサーバーに接続
- **MCPクライアントを作成**：サーバーとの通信を扱います
- **LangChain4jのMCPサポート機能を使用**：LLMとMCPサーバーの統合を簡略化

#### Rust

この例はRustベースのMCPサーバーが動作していることを前提としています。もしまだない場合は、[01-first-server](../01-first-server/README.md) のレッスンを参照してサーバーを作成してください。

Rust MCPサーバーがある状態で、ターミナルを開きサーバーと同じディレクトリに移動し、以下のコマンドを実行して新しいLLMクライアントプロジェクトを作成します：

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```
  
`Cargo.toml` に次の依存関係を追加します：

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```
  
> [!NOTE]
> RustのOpenAI公式ライブラリはありませんが、`async-openai`クレートは一般的に使われている[コミュニティメンテナンスのライブラリ](https://platform.openai.com/docs/libraries/rust#rust)です。

`src/main.rs` を開き、中身を以下のコードに置き換えます：

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
    // 最初のメッセージ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAIクライアントの設定
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCPクライアントの設定
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

    // TODO: MCPツールの一覧を取得

    // TODO: ツール呼び出しを伴うLLM会話

    Ok(())
}
```
  
このコードはRustアプリケーションをセットアップし、MCPサーバーとGitHub ModelsのLLMと接続します。

> [!IMPORTANT]
> アプリケーション実行前に、環境変数 `OPENAI_API_KEY` にGitHubトークンを設定しておいてください。

では次に、サーバーの能力をリストアップしましょう。

### -2- サーバーの能力をリストアップ

サーバーに接続し、能力を尋ねます：

#### Typescript

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
  
上記コードでは：

- サーバー接続用メソッド `connectToServer` を追加しました
- アプリフローを管理する `run` メソッドを作成。現時点ではツールのリストアップのみですが、後で機能を追加します

#### Python

```python
# 利用可能なリソースを一覧表示
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# 利用可能なツールを一覧表示
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```
  
ここで追加した内容は：

- リソースとツールのリストアップおよび出力。ツールについては後で使う `inputSchema` もリストアップしました

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
  
上記コードでは：

- MCPサーバー上の利用可能なツールをリストアップしました
- 各ツールについて、名前、説明、スキーマをリストしました。このスキーマは後のツール呼び出しに使います

#### Java

```java
// MCPツールを自動的に検出するツールプロバイダーを作成します
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCPツールプロバイダーは以下を自動的に処理します:
// - MCPサーバーから利用可能なツールの一覧取得
// - MCPツールスキーマをLangChain4j形式に変換
// - ツールの実行およびレスポンスの管理
```
  
上記コードでは：

- MCPサーバーからすべてのツールを自動検出し登録する `McpToolProvider` を作成しました
- このツールプロバイダーがMCPツールスキーマとLangChain4jツールフォーマットの変換を内部で処理します
- これにより手動でのツールリストアップや変換が不要になります

#### Rust

MCPサーバーからツールを取得するには `list_tools` メソッドを使います。`main` 関数内でMCPクライアントを設定した後、以下のコードを追加してください：

```rust
// MCPツールの一覧を取得する
let tools = mcp_client.list_tools(Default::default()).await?;
```
  
### -3- サーバー能力をLLM対応ツールへ変換

能力をリストアップしたら次はLLMが理解できる形式へ変換します。変換したツールをLLMに渡して使います。

#### TypeScript

1. MCPサーバーの応答をLLMが使えるツール形式に変換するコードを追加します：

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schemaに基づいてzodスキーマを作成する
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // 型を明示的に"function"に設定する
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
  
    上記コードはMCPサーバーからの応答をLLM理解可能なツール定義形式に変換します。

2. 次に `run` メソッドを更新し、サーバー能力をリストするようにします：

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
  
    上記では `run` メソッドで結果をマップ処理し、それぞれに `openAiToolAdapter` を呼び出すようにしました。

#### Python

1. まず変換用の関数を作成します：

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
  
    関数 `convert_to_llm_tools` はMCPツール応答をLLMが理解できる形式に変換します。

2. 次にこの関数を利用するようクライアントコードを更新します：

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```
  
    ここではMCPツール応答を変換し、LLMに渡せるようにしています。

#### .NET

1. MCPツール応答をLLMが理解できる形式に変換するコードを追加します：

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
  
上記コードでは：

- `ConvertFrom` 関数を作成し、名前、説明、入力スキーマを受け取ります
- `FunctionDefinition`を作成し、`ChatCompletionsDefinition`へ渡します。 latter はLLMが理解できる形式です

2. 既存コードをこの関数を使うように更新します：

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
    ```    
    
    In the preceding code, we've:

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
// 自然言語対話のためのBotインターフェースを作成する
public interface Bot {
    String chat(String prompt);
}

// LLMおよびMCPツールでAIサービスを構成する
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```
  
上記コードでは：

- 自然言語対話用のシンプルな `Bot` インターフェースを定義
- LangChain4jの `AiServices` を使い、LLMとMCPツールプロバイダーを自動的にバインド
- フレームワークがツールスキーマの変換と関数呼び出しを自動処理
- 手動でのツール変換不要。LangChain4jがMCPツールをLLM対応形式に変換する複雑さを隠蔽

#### Rust

MCPツール応答をLLM対応形式に変換するには、ツール列表現を整形するヘルパー関数を追加します。`main.rs` の `main` 関数の下に以下のコードを追加してください。これはLLMへのリクエスト時に呼ばれます：

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
  
さあ、次にユーザーリクエストの処理へ進みましょう。

### -4- ユーザープロンプトの処理

このパートではユーザーリクエストを処理します。

#### TypeScript

1. LLMを呼び出すためのメソッドを追加します：

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
  
    上記コードでは：

    - `callTools` メソッドを追加しました
    - LLM応答を受け取り、呼び出すべきツールをチェックします：

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ツールを呼び出す
        }
        ```
  
    - LLMがツール呼び出しを指示した場合、そのツールを呼び出します：

        ```typescript
        // 2. サーバーのツールを呼び出す
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 結果を使って何かをする
        // TODO
        ```
  
2. `run` メソッドを更新し、LLMへの呼び出しと `callTools` の呼び出しを含めます：

    ```typescript

    // 1. LLMへの入力となるメッセージを作成する
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLMを呼び出す
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLMの応答を確認し、各選択肢にツール呼び出しがあるかどうかをチェックする
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```
  
それでは全コードを示します：

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
            baseURL: "https://models.inference.ai.azure.com", // 将来的にこのURLに変更する必要があるかもしれません：https://models.github.ai/inference
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
    
        // 3. LLMの応答を確認し、各選択肢にツール呼び出しがあるかチェックする
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

1. LLMを呼び出すために必要なインポートを追加します：

    ```python
    # 大規模言語モデル
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```
  
2. 次にLLMを呼び出す関数を追加します：

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
  
    上記コードでは：

    - MCPサーバーで発見・変換した関数をLLMに渡しています。
    - 関数を渡してLLMを呼び出し、
    - 結果を見て呼び出すべき関数を判断し、
    - 呼び出す関数の配列を渡しています。

3. 最後にメインコードを更新します：

    ```python
    prompt = "Add 2 to 20"

    # 利用可能なすべてのツールについて、もしあればLLMに尋ねる
    functions_to_call = call_llm(prompt, functions)

    # 推奨された関数を呼び出す
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```
  
    ここが最終ステップです。コードでは：

    - プロンプトに基づきLLMが呼ぶべきと判断したMCPツールを、`call_tool` を通じて呼び、
    - ツール呼び出し結果をMCPサーバーから出力しています。

#### .NET

1. LLMプロンプトリクエストのコード例です：

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
  
    上記コードでは：

    - MCPサーバーからツールを取得、`var tools = await GetMcpTools()` しました
    - ユーザープロンプト `userMessage` を定義
    - モデルとツールを指定するオプションを作成
    - LLMへリクエストを送信しています

2. 最後にLLMが関数呼び出しをどう思うかをチェックします：

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
  
    上記コードでは：

    - 関数呼び出しリストをループし、
    - 各ツール呼び出しで名前と引数をパースし、MCPクライアントでツールを呼び出し結果を出力します。

全コードはこちらです：

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

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```
  
#### Java

```java
try {
    // MCPツールを自動的に使用する自然言語リクエストを実行する
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
  
上記コードでは：

- シンプルな自然言語プロンプトでMCPサーバーツールと対話
- LangChain4jフレームワークが自動的に：
  - 必要に応じてユーザープロンプトをツール呼び出しに変換
  - LLMの判断に基づき適切なMCPツールを呼び出し
  - LLMとMCPサーバー間の対話フローを管理
- `bot.chat()` メソッドは自然言語応答を返し、MCPツールの実行結果含む応答も可能
- ユーザーはMCPの詳細を意識せずに使えるシームレスな体験を実現

完全コードサンプル：

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

ここで実作業の大部分が行われます。初回ユーザープロンプトでLLMを呼び出し、レスポンスを処理して呼び出すべきツールがあるか判定します。あればツール呼び出しを行い、その後もツール呼び出しが不要となり最終応答を得るまでLLMとの対話を続けます。

LLMを何度も呼び出すため、LLM呼び出しを処理する関数を定義します。以下の関数を `main.rs` に追加してください：

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
  
この関数はLLMクライアント、メッセージリスト（ユーザープロンプト含む）、MCPサーバーツールを受け取りLLMへリクエストを送信し、レスポンスを返します。
LLMの応答には `choices` の配列が含まれます。結果を処理して `tool_calls` が存在するかどうかを確認する必要があります。これは、LLMが特定のツールを引数付きで呼び出すことを要求していることを示します。`main.rs` ファイルの一番下に、LLM応答を処理する関数を定義するために以下のコードを追加してください。

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

    // 利用可能な場合は内容を表示する
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ツール呼び出しを処理する
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // アシスタントのメッセージを追加する

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

            // ツールの結果をメッセージに追加する
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ツールの結果で会話を続ける
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

`tool_calls` が存在する場合、ツール情報を抽出してツールリクエストと共にMCPサーバーを呼び出し、結果を会話メッセージに追加します。その後、LLMと会話を続け、メッセージはアシスタントの応答およびツール呼び出し結果で更新されます。

LLMがMCP呼び出しのために返すツール呼び出し情報を抽出するために、呼び出しに必要なすべてを抽出するもう一つのヘルパー関数を追加します。`main.rs` ファイルの一番下に以下のコードを追加してください。

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

すべての準備が整ったので、最初のユーザープロンプトを処理しLLMを呼び出せるようにします。`main` 関数を以下のコードで更新してください。

```rust
// ツール呼び出しを伴うLLM会話
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

これにより、2つの数の合計を尋ねる初期ユーザープロンプトでLLMに問い合わせを行い、ツール呼び出しを動的に処理する応答を処理します。

すばらしい、できましたね！

## 課題

演習のコードをベースに、いくつかのツールを追加してサーバーを構築してください。そして、演習のようにLLMを使ったクライアントを作成し、異なるプロンプトでテストしてサーバーのすべてのツールが動的に呼び出されることを確認してください。この方法でクライアントを構築すると、エンドユーザーは正確なクライアントコマンドではなくプロンプトを使って操作でき、MCPサーバーが呼ばれていることに気づかず優れたユーザー体験を得られます。

## 解答例

[Solution](./solution/README.md)

## 重要なポイント

- クライアントにLLMを追加することで、ユーザーがMCPサーバーとより良くインタラクションできるようになる。
- MCPサーバーの応答をLLMが理解できる形に変換する必要がある。

## サンプル

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## 追加資料

## 次に進む

- 次へ: [Visual Studio Codeを使ってサーバーを利用する](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
