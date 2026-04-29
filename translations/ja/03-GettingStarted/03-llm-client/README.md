# LLMを使ったクライアントの作成

ここまでで、サーバーとクライアントの作成方法を見てきました。クライアントは明示的にサーバーを呼び出してツール、リソース、プロンプトの一覧を取得できていました。しかし、これはあまり実用的なアプローチではありません。ユーザーはエージェント時代に生きており、プロンプトを使用しLLMとやりとりすることを望んでいます。ユーザーはMCPを使って機能を管理しているかどうかには関心がなく、自然言語でやりとりできることを期待しています。では、これをどう解決するのでしょうか？解決策はクライアントにLLMを追加することです。

## 概要

このレッスンではクライアントにLLMを追加することに焦点を当て、これがユーザーにとってずっと良い体験を提供することを示します。

## 学習目標

このレッスンを終える頃には、以下ができるようになります：

- LLMを使ったクライアントの作成
- LLMを使ってMCPサーバーとスムーズにやりとりする方法
- クライアント側でより良いエンドユーザー体験を提供する方法

## アプローチ

どのようなアプローチが必要か理解してみましょう。LLMを追加するのは簡単そうに聞こえますが、実際にどう実装するのでしょうか？

クライアントがサーバーとやりとりする流れは以下の通りです：

1. サーバーと接続を確立する。

1. 機能（capabilities）、プロンプト、リソース、ツールを一覧し、そのスキーマを保存する。

1. LLMを追加し、保存した機能とスキーマをLLMが理解できる形式で渡す。

1. ユーザープロンプトをLLMにツールと共に渡して処理する。

よし、これで上位レベルでどのように実装できるかが分かりました。では、以下の演習で試してみましょう。

## 演習：LLMを使ったクライアントの作成

この演習では、クライアントにLLMを追加する方法を学びます。

### GitHubパーソナルアクセストークンによる認証

GitHubトークンの作成は簡単です。作成手順は以下の通りです：

- GitHub設定にアクセス – 右上のプロフィール画像をクリックし、設定を選択。
- 開発者設定に移動 – 下にスクロールして「開発者設定」をクリック。
- パーソナルアクセストークンを選択 – 「細かいスコープのトークン」をクリックし、「新しいトークンを生成」。
- トークンを設定 – 参照用のノート、期限日、必要な権限（スコープ）を設定。ここでは必ず「Models」権限を追加してください。
- トークンを生成しコピー – 「トークンを生成」をクリックし、その後すぐにコピーしてください。後で再表示できません。

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
- `client` と `openai` の2つのメンバーを持つクラスを作成しました。これらはそれぞれクライアント管理とLLMとのやりとりに使います。
- `baseUrl`を推論APIに設定してGitHub Modelsを使うようLLMインスタンスを設定しました。

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

- MCP用の必要なライブラリをインポートしました
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

まず、`pom.xml`ファイルにLangChain4jの依存関係を追加する必要があります。MCP統合とGitHub Modelsサポートのために次の依存関係を追加してください：

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
    
    public static void main(String[] args) throws Exception {        // LLMがGitHubモデルを使用するように設定する
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

- **LangChain4jの依存関係を追加しました**：MCP統合、OpenAI公式クライアント、GitHub Modelsサポート用の依存関係です
- **LangChain4jライブラリをインポートしました**：MCP統合とOpenAIチャットモデル機能に使用します
- **`ChatLanguageModel`を作成しました**：GitHubトークンを使いGitHub Modelsを利用する設定です
- **HTTPトランスポートを設定しました**：サーバー送信イベント（SSE）を使ってMCPサーバーに接続しています
- **MCPクライアントを作成しました**：サーバーと通信を管理します
- **LangChain4jの組み込みMCPサポートを活用しました**：LLMとMCPサーバーの統合を簡素化します

#### Rust

この例ではRustベースのMCPサーバーが稼働していることを前提としています。まだお持ちでない場合は[01-first-server](../01-first-server/README.md)のレッスンを参照してサーバーを作成してください。

RustのMCPサーバーを用意したら、ターミナルでサーバーと同じディレクトリに移動し、以下のコマンドで新しいLLMクライアントプロジェクトを作成します：

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

次に、`Cargo.toml`ファイルに以下の依存関係を追加します：

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAIの公式Rustライブラリはありませんが、`async-openai`クレートは[コミュニティが管理するライブラリ](https://platform.openai.com/docs/libraries/rust#rust)としてよく使われています。

`src/main.rs`ファイルを開き、内容を次のコードに置き換えます：

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

    // OpenAI クライアントのセットアップ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP クライアントのセットアップ
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

    // TODO: MCP ツール一覧を取得する

    // TODO: ツール呼び出しを伴うLLM会話

    Ok(())
}
```

このコードはRustアプリケーションの基本セットアップで、MCPサーバーとGitHub ModelsによるLLM連携を行います。

> [!IMPORTANT]
> アプリケーションを実行する前に、環境変数 `OPENAI_API_KEY` にGitHubトークンを設定しておいてください。

それでは次のステップとして、サーバーの機能一覧を取得してみましょう。

### -2- サーバーの機能一覧取得

今度はサーバーに接続して機能を尋ねます：

#### Typescript

同じクラスに以下のメソッドを追加してください：

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

- サーバー接続用のコード `connectToServer` を追加しました。
- アプリのフローを管理する `run` メソッドを作成しました。現状はツール一覧を出すだけですが、今後拡張します。

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

追加した内容は：

- リソースとツール一覧を取得しプリントしました。ツールは後で使う `inputSchema` も一覧に含めています。

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

- MCPサーバーから利用可能なツール一覧を取得しました
- 各ツールの名前、説明、スキーマを取得しています。スキーマは今後ツール呼び出しに利用します。

#### Java

```java
// MCPツールを自動的に検出するツールプロバイダーを作成する
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCPツールプロバイダーは以下を自動的に処理します：
// - MCPサーバーから利用可能なツールのリスト取得
// - MCPツールスキーマをLangChain4j形式に変換
// - ツールの実行とレスポンスの管理
```

上記コードでは：

- MCPサーバーからツールを自動で検出・登録する `McpToolProvider` を作成しました
- ツールプロバイダーがMCPのツールスキーマとLangChain4jのツール形式の変換を内部で処理します
- 手動でツール一覧や変換する必要がなくなる抽象化です

#### Rust

MCPサーバーからツールを取得するには、`list_tools` メソッドを使います。`main`関数内でMCPクライアントをセットアップした後に以下を追記してください：

```rust
// MCPツールの一覧を取得する
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- サーバー機能をLLM用ツールに変換

サーバーの機能リストが取得できたら、それをLLMが理解できる形式に変換します。変換が済めばLLMにツールとして提供できます。

#### TypeScript

1. MCPサーバーの応答をLLMが使えるツール形式に変換するため、以下のコードを追加します：

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // 入力スキーマに基づいてzodスキーマを作成する
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // 型を明示的に "function" に設定する
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

    上記コードはMCPサーバーのレスポンスを受け、LLMが理解できるツール定義形式に変換します。

1. 続けて `run` メソッドを更新しサーバー機能を一覧表示するようにします：

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

    上記コードで、`run` メソッドを更新し返された結果をマップして各エントリーに `openAiToolAdapter` を呼び出しています。

#### Python

1. まずは下記の変換関数を作成します：

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

    上記の `convert_to_llm_tools` 関数では、MCPツールのレスポンスを受けLLMが理解できる形式に変換しています。

1. つづいて、クライアントコードを更新しこの関数を利用するようにします：

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ここではMCPツールレスポンスをLLMに渡せる形に変換するため、`convert_to_llm_tool` を呼び出しています。

#### .NET

1. MCPツールレスポンスをLLMが理解できる形式に変換するコードを追加します：

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

- 名前、説明、入力スキーマを受け取り変換する `ConvertFrom` 関数を作成しました。
- これにより、LLMが理解する `FunctionDefinition` が作成され、`ChatCompletionsDefinition` に渡されます。

1. 既存コードをこの関数を使うように更新します：

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
// 自然言語での対話のためのBotインターフェースを作成する
public interface Bot {
    String chat(String prompt);
}

// LLMとMCPツールでAIサービスを設定する
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

上記コードでは：

- 自然言語対話用のシンプルな `Bot` インターフェースを定義しました
- LangChain4jの `AiServices` を使い、LLMとMCPツールプロバイダーを自動的に結びつけました
- フレームワークがツールスキーマの変換と関数呼び出しを自動処理します
- これにより手動でのツール変換は不要となり、MCPツールからLLM互換フォーマットへの変換の煩雑さをLangChain4jが吸収しています

#### Rust

MCPツールレスポンスをLLMが理解できる形式に変換するためのヘルパー関数を作成します。`main`関数下に以下を追加してください。これはLLMにリクエストを送る際に使います：

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

よし、ユーザーからのリクエスト処理がまだなので次に取り組みましょう。

### -4- ユーザーのプロンプトリクエスト処理

このパートではユーザーのリクエストを処理します。

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

        // 3. 結果を使って何かを行う
        // TODO

        }
    }
    ```

    上記コードでは：

    - `callTools` メソッドを追加しました。
    - メソッドはLLMのレスポンスを受け、呼び出すべきツールがあれば判断します：

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ツールを呼び出す
        }
        ```

    - LLMが呼び出し指示をした場合にツールを呼び出します：

        ```typescript
        // 2. サーバーのツールを呼び出す
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 結果に対して何かを行う
        // やること
        ```

1. `run` メソッドを更新し、LLMの呼び出しおよび `callTools` も含めるようにします：

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

    // 3. LLMの応答を確認し、各選択肢にツールコールがあるかをチェックする
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

さて、コード全体をリストしてみましょう：

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // スキーマバリデーションのためにzodをインポートする

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // 将来的にこのURLに変更する必要があるかもしれません: https://models.github.ai/inference
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
    
          // 3. 結果に対して何かを行う
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
    
        // 1. LLMの応答を順に処理し、各選択肢がツール呼び出しを含んでいるか確認する
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

1. LLM呼び出しに必要なインポートを追加します：

    ```python
    # 大規模言語モデル
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. LLMを呼び出す関数を追加します：

    ```python
    # llm

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

    - MCPサーバーで見つけ変換した関数群をLLMに渡しています。
    - それらの関数をLLMに渡して呼び出しました。
    - 結果を確認し、呼ぶべき関数があれば判別しています。
    - 呼び出す関数の配列を渡しています。

1. 最後にメインコードを更新します：

    ```python
    prompt = "Add 2 to 20"

    # 使用するすべてのツール（もしあれば）についてLLMに尋ねる
    functions_to_call = call_llm(prompt, functions)

    # 推奨される関数を呼び出す
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    以上が最後のステップで、上記コードでは：

    - `call_tool`によってLLMが呼ぼうと判断したMCPツールを呼び出しています。
    - ツール呼び出し結果をMCPサーバーに表示しています。

#### .NET

1. LLMのプロンプトリクエストを行うコード例を示します：

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

    - MCPサーバーからツールを取得しています (`var tools = await GetMcpTools()`)。
    - ユーザープロンプト `userMessage` を定義。
    - モデルとツールを指定したオプションオブジェクトを作成。
    - LLMへリクエストを送信しています。

1. 最後に、LLMが関数呼び出しが必要かどうかを判断している箇所：

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

    - 関数呼び出しリストをループ処理。
    - 各ツール呼び出しについて名前と引数を解析し、MCPクライアントでツールを呼び出し、結果をプリントしています。

コード全文はこちら：

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

- 単純な自然言語のプロンプトでMCPサーバーツールとやりとりしています
- LangChain4jフレームワークが以下を自動処理：
  - 必要なときユーザーのプロンプトをツール呼び出しに変換
  - LLMの判断に基づく適切なMCPツールの呼び出し
  - LLMとMCPサーバー間の対話制御
- `bot.chat()` メソッドはMCPツール実行結果を含む自然言語レスポンスを返します
- ユーザーがMCPの仕組みを知らなくても透過的に使える体験を提供します

完成コード例：

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

ここが主な作業の部分です。初回ユーザープロンプトでLLMを呼び出し、そのレスポンスを処理してツール呼び出しが必要なら実行します。ツール呼び出しを行ったら再度LLMと会話を続け、ツール呼び出しが不要になり最終応答が返るまで繰り返します。

複数回のLLM呼び出しを行うので、LLM呼び出しを担当する関数を定義しましょう。以下の関数を`main.rs`に追加してください：

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

この関数はLLMクライアント、メッセージ（ユーザープロンプト含む）、MCPサーバーツールリストを受け、LLMにリクエストを送りレスポンスを返します。
LLMのレスポンスには`choices`の配列が含まれます。結果を処理して`tool_calls`が存在するかどうかを確認する必要があります。これは、LLMが引数付きで特定のツールを呼び出すことを要求していることを示しています。LLMレスポンスを処理する関数を定義するために、以下のコードを`main.rs`ファイルの末尾に追加してください：

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

    // 利用可能な場合はコンテンツを印刷する
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

`tool_calls`が存在する場合、ツール情報を抽出し、MCPサーバーにツールリクエストを送信し、その結果を会話メッセージに追加します。その後、LLMとともに会話を続け、メッセージはアシスタントの応答とツール呼び出し結果で更新されます。

MCP呼び出し用にLLMが返すツールコール情報を抽出するために、呼び出しに必要なすべてを抽出する別のヘルパー関数を追加します。以下のコードを`main.rs`ファイルの末尾に追加してください：

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

これですべての部品が揃いました。初期のユーザープロンプトを処理し、LLMを呼び出せるように`main`関数を更新します。以下のコードを含めてください：

```rust
// ツールコールを伴うLLM対話
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

これにより、最初のユーザープロンプトから2つの数値の合計を求めるようにLLMに問い合わせをし、レスポンスを処理してツールコールを動的に扱います。

素晴らしい、できましたね！

## 課題

演習のコードをベースに、さらに多くのツールを備えたサーバーを構築してください。それから、演習のようにLLMを使ったクライアントを作り、様々なプロンプトでテストして、サーバーツールが動的に正しく呼び出されることを確認しましょう。このクライアントの構築方法は、エンドユーザーが厳密なクライアントコマンドではなくプロンプトを使って操作でき、背後でMCPサーバーが呼ばれていることに気づかない、優れたユーザー体験を提供します。

## 解答例

[Solution](./solution/README.md)

## 重要なポイント

- クライアントにLLMを追加することで、ユーザーがMCPサーバーとより良く対話できるようになる。
- MCPサーバーのレスポンスをLLMが理解できる形に変換する必要がある。

## サンプル集

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## 追加リソース

## 次に進むには

- 次へ：[Visual Studio Codeを使ったサーバーの利用](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の元の言語での文書が正本と見なされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->