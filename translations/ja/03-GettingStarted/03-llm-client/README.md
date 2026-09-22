# LLMを使ってクライアントを作成する

> [!NOTE]
> Javaクライアントの例はレガシーなHTTP+SSEトランスポートを通じて接続し、
> MCP `2025-11-25` SDK APIをターゲットとしています。新しいリモートクライアントには
> `2026-07-28`対応のSDKとStreamable HTTPを使用してください。

ここまでで、サーバーとクライアントの作成方法を見てきました。クライアントは明示的にサーバーを呼び出して、そのツールやリソース、プロンプトの一覧を取得できました。ただし、これはあまり実用的なアプローチではありません。ユーザーはエージェント時代に生きており、プロンプトを使ってLLMと対話することを期待しています。彼らはあなたがMCPを使って能力を保存しているかどうかには関心がなく、自然言語でのやり取りを求めています。では、それをどのように解決するのでしょうか？解決策はクライアントにLLMを追加することです。

## 概要

このレッスンでは、クライアントにLLMを追加することに焦点を当て、これがユーザー体験をどのように大きく向上させるかを示します。

## 学習目標

このレッスンの終わりまでに、あなたは次のことができるようになります：

- LLMを使ってクライアントを作成する。
- LLMを使ってシームレスにMCPサーバーと対話する。
- クライアント側でより良いエンドユーザー体験を提供する。

## アプローチ

必要なアプローチを理解してみましょう。LLMを追加するのは簡単そうに聞こえますが、実際にこれを行えるでしょうか？

クライアントがサーバーとやり取りする方法は以下の通りです：

1. サーバーとの接続を確立する。

1. 能力、プロンプト、リソース、ツールの一覧を取得し、そのスキーマを保存する。

1. LLMを追加し、保存した能力とスキーマをLLMが理解できる形式で渡す。

1. ユーザープロンプトをLLMに渡し、クライアントが一覧したツールと一緒に処理する。

素晴らしいですね。高レベルでの流れを理解したので、次は以下の演習で実際に試してみましょう。

## 演習：LLMを使ったクライアントの作成

この演習では、クライアントにLLMを追加する方法を学びます。

### GitHubパーソナルアクセストークンによる認証

GitHubトークンの作成は簡単です。手順は以下の通りです：

- GitHub設定にアクセスする – 右上のプロフィール画像をクリックして「Settings」を選択。
- 「Developer Settings」に進む – スクロールして「Developer Settings」をクリック。
- 「Personal Access Tokens」を選択 – 「Fine-grained tokens」をクリックし、新しいトークンを生成。
- トークンを設定 – 参照用のメモを追加し、有効期限を設定、必要なスコープ（権限）を選択。この場合は「Models」権限を必ず追加してください。
- トークンを生成してコピー – 「Generate token」をクリックし、表示されたトークンをすぐにコピーしてください。後で再度見ることはできません。

### -1- サーバーへ接続する

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

上記のコードでは次のことを行いました：

- 必要なライブラリをインポート
- `client`と`openai`の二つのメンバーを持つクラスを作成し、それぞれクライアント管理とLLMとの対話に使う
- `baseUrl`を推論APIにセットしてGitHub Modelsを使用するようLLMインスタンスを設定

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

上記のコードでは次のことを行いました：

- MCP用の必要ライブラリをインポート
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

まず、LangChain4jの依存パッケージを`pom.xml`に追加する必要があります。これによりMCP統合とOpenAI互換のMiniMax APIが利用可能になります：

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
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

MiniMax APIキーと、必要に応じてエンドポイントやモデルを設定してください。
`MINIMAX_MODEL_ID`は`MiniMax-M3`と`MiniMax-M2.7`をサポートします。
`OPENAI_BASE_URL`が設定されていない場合は、`MINIMAX_REGION`に`global_en`と`cn_zh`が使えます。

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

地域によるエンドポイントの選択には`OPENAI_BASE_URL`を省略してください：

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

続いてJavaのクライアントクラスを作成します：

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
                .build();

        // サーバーに接続するためのMCPトランスポートを作成
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCPクライアントを作成
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

上記コードでは以下のことを行いました：

- **LangChain4j依存パッケージを追加**：MCP統合とOpenAI互換MiniMax API用
- **LangChain4jライブラリをインポート**：MCP統合とOpenAIチャットモデル機能用
- **`ChatLanguageModel`を作成**：MiniMax APIキー、エンドポイント、対応モデルIDを設定
- **HTTPトランスポートを設定**：Server-Sent Events (SSE) を使用してMCPサーバーに接続
- **MCPクライアントを作成**：サーバーとの通信処理を担当
- **LangChain4jのMCPサポートを利用**：LLMとMCPサーバー間の統合を簡素化

#### Rust

この例はRustベースのMCPサーバーが動作していることを前提とします。まだ作成していない場合は[01-first-server](../01-first-server/README.md)のレッスンを参照してください。

Rust MCPサーバーが準備できたら、ターミナルを開きサーバーと同じディレクトリに移動して、以下のコマンドを実行して新しいLLMクライアントプロジェクトを作成します：

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml`ファイルに以下の依存関係を追加します：

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAIの公式Rustライブラリはありませんが、`async-openai`クレートは[コミュニティがメンテナンスしているライブラリ](https://platform.openai.com/docs/libraries/rust#rust)で広く使われています。

`src/main.rs`ファイルを開き、中身を以下のコードに置き換えます：

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

    // OpenAIクライアントのセットアップ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCPクライアントのセットアップ
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

    // TODO: MCPツールのリストを取得する

    // TODO: ツール呼び出しを伴うLLM会話

    Ok(())
}
```

このコードはMCPサーバーとGitHub Modelsに接続してLLMとの対話を行う基本的なRustアプリケーションを設定します。

> [!IMPORTANT]
> 実行前に必ず`OPENAI_API_KEY`環境変数にGitHubトークンをセットしてください。

次はサーバーの能力一覧を取得しましょう。

### -2- サーバーの能力一覧の取得

サーバーに接続して能力を取得します：

#### TypeScript

同じクラスに次のメソッドを追加します：

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

上記コードでは次のことを追加しました：

- サーバー接続用のコード`connectToServer`を追加
- アプリのフローを管理する`run`メソッドを作成。現時点ではツールの一覧取得のみだが、後で機能追加予定

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

- リソースとツールを一覧表示しプリント。ツールには後で使う`inputSchema`も含めている

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

上記コードでは次のことを行いました：

- MCPサーバー上で利用可能なツールを一覧表示
- 各ツールについて名前、説明、スキーマをリスト。スキーマは後でツール呼び出しに利用予定

#### Java

```java
// MCPツールを自動的に検出するツールプロバイダーを作成します
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCPツールプロバイダーは自動的に以下を処理します:
// - MCPサーバーから利用可能なツールの一覧取得
// - MCPツールスキーマをLangChain4jフォーマットに変換
// - ツールの実行と応答の管理
```

上記コードでは次のことを行いました：

- MCPサーバーから全ツールを自動検出し登録する`McpToolProvider`を作成
- このプロバイダーがMCPツールスキーマとLangChain4jツール形式の変換処理を内部で行う
- この手法によりツールの一覧・変換作業を抽象化

#### Rust

MCPサーバーからツールを取得するには`list_tools`メソッドを使用します。`main`関数内でMCPクライアントセットアップ後に次のコードを追加してください：

```rust
// MCPツールの一覧を取得する
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- サーバーの能力をLLMツール形式に変換

サーバーの能力一覧取得後は、それらをLLMが理解できるツール形式に変換します。こうして得た能力をツールとしてLLMに提供可能となります。

#### TypeScript

1. MCPサーバーのレスポンスをLLMで使えるツール形式に変換するコードを追加：

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schemaに基づいてzodスキーマを作成する
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // 型を"function"に明示的に設定する
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

    上記コードはMCPサーバーのレスポンスをLLMが理解可能なツール定義形式に変換しています。

2. 続けて`run`メソッドを更新し、サーバー能力一覧をマップして`openAiToolAdapter`を呼ぶようにします：

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

    ここでは`run`メソッドを更新し、結果の各エントリに対し`openAiToolAdapter`を呼び出しています。

#### Python

1. まずは次の変換関数を作成します

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

    上記`convert_to_llm_tools`関数ではMCPツールのレスポンスをLLMが理解できる形式に変換しています。

2. 次にクライアントコードを更新してこの関数を使用します：

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ここでは`convert_to_llm_tool`を呼んでMCPツールレスポンスをLLMに渡せる形に変換しています。

#### .NET

1. MCPツールレスポンスをLLMが理解可能な形式に変換するコードを追加します

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

上記コードでは次のことを行いました：

- 名前、説明、入力スキーマを受け取る`ConvertFrom`関数を作成
- `FunctionDefinition`を生成し、それをLLMが理解する`ChatCompletionsDefinition`に渡す機能を定義

2. 続いて既存コードを更新しこの関数を活用します：

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

    - Update the function to convert the MCP tool response to an LLM tool. Let's highlight the code we added:

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

// LLMおよびMCPツールを使ってAIサービスを構成する
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

上記コードでは次のことを行いました：

- 自然言語対話用のシンプルな`Bot`インターフェースを定義
- LangChain4jの`AiServices`を使用してLLMとMCPツールプロバイダーを自動連結
- フレームワークがツールスキーマ変換と関数呼び出しを自動的に処理
- 手動のツール変換がいらない仕組み - LangChain4jがMCPツールのLLM対応形式変換の複雑さを担う

#### Rust

MCPツールレスポンスをLLMが理解できる形式に変換するため、ツール一覧をフォーマットするヘルパー関数を作成します。`main.rs`の`main`関数の下に以下のコードを追加してください。これはLLMへのリクエスト時に利用されます：

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

さて、ユーザからのリクエスト処理を設定しましょう。

### -4- ユーザープロンプトの処理

このコードパートではユーザーのリクエストを処理します。

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

    上記コードでは以下のことを行いました：

    - `callTools`メソッドを追加
    - LLMのレスポンスを解析して呼び出されたツールがあるか判定

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ツールを呼び出す
        }
        ```

    - LLMがツールを呼び出すよう指示があればそのツールを呼び出す

        ```typescript
        // 2. サーバーのツールを呼び出す
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 結果で何かをする
        // TODO
        ```

2. `run`メソッドを更新し、LLM呼び出しと`callTools`の呼び出しを追加：

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

    // 3. LLMの応答を確認し、各選択肢にツール呼び出しがあるかチェックする
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

素晴らしい、完全なコードは以下です：

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
    
          // 3. 結果を使って何かをする
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
    
        // 3. LLMのレスポンスを確認し、各選択肢にツール呼び出しがあるかどうかチェックする
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

1. LLM呼び出しに必要なインポートを追加します

    ```python
    # 大規模言語モデル
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. 次にLLMを呼び出す関数を追加：

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

    上記コードでは次のことをしました：

    - MCPサーバーの関数を取得し変換したものをLLMに渡す
    - その関数群を用いてLLMを呼び出す
    - 結果を調査し呼び出すべき関数があるか確認
    - 呼び出す関数のリストを渡す

3. 最後にメインコードを更新しましょう：

    ```python
    prompt = "Add 2 to 20"

    # ツールがあれば、すべてのツールについてLLMに尋ねる
    functions_to_call = call_llm(prompt, functions)

    # 推奨された関数を呼び出す
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    これが最後のステップで、上記コードでは：

    - LLMが呼ぶべきと判断した関数を用いて`call_tool`でMCPツールを呼び出す
    - MCPサーバーへのツール呼び出し結果をプリント

#### .NET

1. LLMプロンプトリクエストのコード例を示します：

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

    上記コードでは次のことを行いました：

    - MCPサーバーからツールを取得(`var tools = await GetMcpTools()`)
    - ユーザープロンプト`userMessage`を定義
    - モデルとツールを指定したオプションオブジェクトを作成
    - LLMへリクエストを送信

2. 最後のステップとして、LLMが呼び出すべきか判断した関数を見てみましょう：

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

    上記コードでは以下を行いました：

    - 関数呼び出しリストをループ処理
    - 各ツール呼び出しについて名前と引数を解析し、MCPクライアントで呼び出し、結果を出力

コード全体はこちらです：

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

上記コードでは以下のことを行いました：

- シンプルな自然言語プロンプトを使いMCPサーバーツールと対話
- LangChain4jフレームワークが以下を自動処理：
  - 必要に応じてユーザープロンプトをツール呼び出しに変換
  - LLMの判断により適切なMCPツールを呼び出し
  - LLMとMCPサーバー間の会話フローを管理
- `bot.chat()`メソッドはMCPツールの結果も含んだ自然言語応答を返す
- このアプローチによりユーザーはMCPの実装を意識せずにシームレスな体験を得られる

完全なコード例：

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

#### Rust


ここで大部分の作業が行われます。初期のユーザープロンプトでLLMを呼び出し、その応答を処理してツールを呼び出す必要があるかを確認します。必要であればそのツールを呼び出し、もうツール呼び出しが不要になり最終的な応答が得られるまでLLMとの会話を続けます。

LLMへの呼び出しを複数回行うため、LLM呼び出しを処理する関数を定義しましょう。以下の関数を`main.rs`ファイルに追加してください：

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

この関数はLLMクライアント、メッセージのリスト（ユーザープロンプトを含む）、MCPサーバーのツールを受け取り、LLMへリクエストを送り応答を返します。

LLMからの応答には`choices`の配列が含まれています。その結果を処理して`tool_calls`があるかどうか確認する必要があります。これでLLMが特定のツールを引数付きで呼び出すことを要求していることがわかります。以下のコードを`main.rs`の末尾に追加し、LLMの応答を処理する関数を定義してください：

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

    // 内容が利用可能な場合は表示する
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

`tool_calls`が存在する場合、ツール情報を取り出し、MCPサーバーにツールリクエストを送り、結果を会話のメッセージに追加します。その後、LLMとの会話を続け、メッセージはアシスタントの応答やツール呼び出しの結果で更新されます。

MCP呼び出し用のツールコール情報をLLMが返す形式から抽出するために、さらに呼び出しに必要なすべてを抜き出すヘルパー関数を追加します。以下のコードを`main.rs`の末尾に追加してください：

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

すべてのパーツが揃ったので、初期のユーザープロンプトを処理してLLMを呼び出せます。`main`関数を以下のコードで更新してください：

```rust
// ツール呼び出しを伴うLLM対話
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

これは、二つの数字の合計を求める初期ユーザープロンプトでLLMに問い合わせ、応答を処理して動的にツール呼び出しを扱います。

よくできました！

## 課題

演習コードをもとにサーバーをより多くのツールで拡張してください。そして、演習のようにLLMを使ったクライアントを作成し、さまざまなプロンプトでテストしてサーバーのツールが動的に呼び出されることを確認してください。こうしたクライアント構築により、最終ユーザーは厳密なクライアントコマンドではなくプロンプトを使い、MCPサーバーが呼び出されていることに気づかずに優れたユーザー体験を得られます。

## 解答例

[Solution](./solution/README.md)

## 重要なポイント

- クライアントにLLMを追加することで、ユーザーがMCPサーバーとやり取りするより良い方法が提供されます。
- MCPサーバーの応答をLLMが扱える形に変換する必要があります。

## サンプル

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## 追加リソース

## 次に学ぶこと

- 次へ：[Visual Studio Codeを使ったサーバーの利用](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
