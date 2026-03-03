# LLM সহ ক্লায়েন্ট তৈরি করা

এখন পর্যন্ত, আপনি দেখেছেন কীভাবে একটি সার্ভার এবং একটি ক্লায়েন্ট তৈরি করতে হয়। ক্লায়েন্ট স্পষ্টভাবে সার্ভারকে কল করতে পেরেছে তার টুলস, রিসোর্স এবং প্রম্পটগুলি তালিকাভুক্ত করার জন্য। তবে, এটি খুব কার্যকরী পদ্ধতি নয়। আপনার ব্যবহারকারীরা এজেন্টিক যুগে বাস করে এবং তারা প্রম্পট ব্যবহার করতে এবং একটি LLM-এর সাথে যোগাযোগ করতে আশা করে। তারা MCP ব্যবহার করে আপনার সক্ষমতাগুলি সংরক্ষণ করছেন কিনা তাতে আগ্রহী নয়; তারা কেবল প্রাকৃতিক ভাষা ব্যবহার করে ইন্টারঅ্যাক্ট করতে চায়। তাহলে আমরা কীভাবে এটি সমাধান করব? সমাধান হল ক্লায়েন্টে একটি LLM যোগ করা।

## ওভারভিউ

এই পাঠে আমরা ক্লায়েন্টে একটি LLM যোগ করার দিকে দৃষ্টি নিবদ্ধ করব এবং দেখাব কীভাবে এটি আপনার ব্যবহারকারীর জন্য একটি অনেক ভালো অভিজ্ঞতা প্রদান করে।

## শেখার উদ্দেশ্যসমূহ

এই পাঠের শেষে, আপনি সক্ষম হবেন:

- একটি LLM সহ ক্লায়েন্ট তৈরি করতে।
- একটি MCP সার্ভারের সাথে LLM ব্যবহার করে নির্বিঘ্নে ইন্টারঅ্যাক্ট করতে।
- ক্লায়েন্ট পাশের শেষ ব্যবহারকারী অভিজ্ঞতা উন্নত করতে।

## পদ্ধতি

চলুন আমরা বুঝতে চেষ্টা করি কোন পদ্ধতি নিতে হবে। একটি LLM যোগ করা সহজ শোনায়, তবে আমরা কি সত্যিই এটা করব?

এভাবে ক্লায়েন্ট সার্ভারের সাথে ইন্টারঅ্যাক্ট করবে:

1. সার্ভারের সাথে সংযোগ স্থাপন করুন।

1. সক্ষমতা, প্রম্পট, রিসোর্স এবং টুলসগুলি তালিকাভুক্ত করুন, এবং তাদের স্কিমা সংরক্ষণ করুন।

1. একটি LLM যোগ করুন এবং সংরক্ষিত সক্ষমতা এবং তাদের স্কিমা সেই ফর্ম্যাটে পাস করুন যা LLM বোঝে।

1. একটি ব্যবহারকারীর প্রম্পট হ্যান্ডেল করুন এবং এটি LLM-এ পাস করুন ক্লায়েন্ট দ্বারা তালিকাভুক্ত টুলসগুলো সহ।

দারুন, এখন আমরা উচ্চ স্তরে বুঝে গেছি কীভাবে করব, নিচের অনুশীলনে এটি চেষ্টা করা যাক।

## অনুশীলন: LLM সহ ক্লায়েন্ট তৈরি করা

এই অনুশীলনে, আমরা আমাদের ক্লায়েন্টে একটি LLM যোগ করা শিখব।

### গিটহাব পার্সোনাল অ্যাক্সেস টোকেন ব্যবহার করে প্রমাণীকরণ

গিটহাব টোকেন তৈরি করা একটি সরল প্রক্রিয়া। এখানে কীভাবে করবেন:

- গিটহাব সেটিংসে যান – উপরের ডানদিকে আপনার প্রোফাইল ছবিতে ক্লিক করুন এবং Settings নির্বাচন করুন।
- ডেভেলপার সেটিংসে যান – নিচ দিকে স্ক্রল করে Developer Settings-এ ক্লিক করুন।
- পার্সোনাল অ্যাক্সেস টোকেন নির্বাচন করুন – Fine-grained tokens-এ ক্লিক করুন এবং তারপর Generate new token ক্লিক করুন।
- আপনার টোকেন কনফিগার করুন – রেফারেন্সের জন্য একটি নোট যোগ করুন, একটি মেয়াদ শেষের তারিখ নির্ধারণ করুন, এবং প্রয়োজনীয় স্কোপ (অনুমতি) নির্বাচন করুন। এই ক্ষেত্রে নিশ্চিত করুন Models অনুমতি যোগ করেছেন।
- টোকেন তৈরি করুন এবং কপি করুন – Generate token ক্লিক করুন, এবং এটি সঙ্গে সঙ্গেই কপি করুন, কারণ আপনি এটি আবার দেখতে পারবেন না।

### -1- সার্ভারের সাথে সংযোগ করুন

চলুন প্রথমে আমাদের ক্লায়েন্ট তৈরি করি:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // স্কিমা যাচাইকরণের জন্য zod আমদানি করুন

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

উপরের কোডে আমরা:

- প্রয়োজনীয় লাইব্রেরি আমদানি করেছি
- একটি ক্লাস তৈরি করেছি যার মধ্যে দুটি সদস্য, `client` এবং `openai`, যা আমাদের ক্লায়েন্ট পরিচালনা এবং LLM-এর সাথে ইন্টারঅ্যাক্ট করতে সাহায্য করবে।
- আমাদের LLM ইন্সট্যান্স কনফিগার করেছি GitHub Models ব্যবহারের জন্য, `baseUrl` সেট করে inference API-র দিকে নির্দেশনা দিয়েছি।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio সংযোগের জন্য সার্ভার প্যারামিটার তৈরি করুন
server_params = StdioServerParameters(
    command="mcp",  # কার্যনির্বাহী
    args=["run", "server.py"],  # ঐচ্ছিক কমান্ড লাইন যুক্তি
    env=None,  # ঐচ্ছিক পরিবেশ ভেরিয়েবল
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # সংযোগ শুরু করুন
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

উপরের কোডে আমরা:

- MCP এর জন্য প্রয়োজনীয় লাইব্রেরি আমদানি করেছি
- একটি ক্লায়েন্ট তৈরি করেছি

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

প্রথমে, আপনাকে আপনার `pom.xml` ফাইলে LangChain4j নির্ভরশীলতা (dependencies) যোগ করতে হবে। MCP ইন্টিগ্রেশন এবং GitHub Models সাপোর্টের জন্য এই নির্ভরশীলতাগুলি যোগ করুন:

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

এরপর, আপনার Java ক্লায়েন্ট ক্লাস তৈরি করুন:

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
    
    public static void main(String[] args) throws Exception {        // GitHub মডেলগুলি ব্যবহারের জন্য LLM কনফিগার করুন
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // সার্ভারের সাথে সংযোগ করার জন্য MCP ট্রান্সপোর্ট তৈরি করুন
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ক্লায়েন্ট তৈরি করুন
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

উপরের কোডে আমরা:

- **LangChain4j নির্ভরশীলতা যোগ করেছি**: MCP ইন্টিগ্রেশন, OpenAI অফিসিয়াল ক্লায়েন্ট, এবং GitHub Models সাপোর্টের জন্য
- **LangChain4j লাইব্রেরি আমদানি করেছি**: MCP ইন্টিগ্রেশন এবং OpenAI চ্যাট মডেল ফাংশনালিটির জন্য
- **`ChatLanguageModel` তৈরি করেছি**: GitHub Models ব্যবহার করার জন্য আপনার গিটহাব টোকেন দিয়ে কনফিগার করা
- **HTTP ট্রান্সপোর্ট সেটআপ করেছি**: MCP সার্ভারের সাথে সংযোগের জন্য Server-Sent Events (SSE) ব্যবহার করে
- **MCP ক্লায়েন্ট তৈরি করেছি**: যা সার্ভারের সাথে যোগাযোগ পরিচালনা করবে
- **LangChain4j-এর বিল্ট-ইন MCP সাপোর্ট ব্যবহার করেছি**: যা LLM এবং MCP সার্ভারের মধ্যকার ইন্টিগ্রেশন সহজ করে তোলে

#### Rust

এই উদাহরণটি ধরে নিচ্ছে যে আপনার একটি Rust ভিত্তিক MCP সার্ভার রান করছে। যদি না থাকে, তবে [01-first-server](../01-first-server/README.md) লেসনে ফিরে গিয়ে সার্ভার তৈরি করুন।

আপনার Rust MCP সার্ভার থাকলে, একটি টার্মিনাল খুলুন এবং সার্ভারের ডিরেক্টরিতে যান। এরপর নতুন একটি LLM ক্লায়েন্ট প্রোজেক্ট তৈরি করতে নিম্নলিখিত কমান্ড চালান:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` ফাইলে নিম্নলিখিত নির্ভরশীলতাগুলি যোগ করুন:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI-এর জন্য কোনো অফিসিয়াল Rust লাইব্রেরি নেই, তবে `async-openai` ক্রেটটি একটি [কমিউনিটি রক্ষণাবেক্ষিত লাইব্রেরি](https://platform.openai.com/docs/libraries/rust#rust) যা সাধারণত ব্যবহৃত হয়।

`src/main.rs` ফাইলটি খুলে তার বিষয়বস্তু নিচের কোড দিয়ে প্রতিস্থাপন করুন:

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
    // প্রাথমিক বার্তা
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ক্লায়েন্ট সেটআপ করুন
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ক্লায়েন্ট সেটআপ করুন
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

    // TODO: MCP টুল লিস্টিং পান

    // TODO: টুল কল সহ LLM কথোপকথন

    Ok(())
}
```

এই কোড একটি মৌলিক Rust অ্যাপ্লিকেশন সেটআপ করে যা MCP সার্ভার এবং GitHub Models-এর সঙ্গে LLM ইন্টারঅ্যাকশনের জন্য সংযোগ করবে।

> [!IMPORTANT]
> অ্যাপ্লিকেশন চালানোর আগে অবশ্যই `OPENAI_API_KEY` পরিবেশ ভেরিয়েবলটি আপনার GitHub টোকেন দিয়ে সেট করুন।

দারুন, পরবর্তী ধাপে আমরা সার্ভারের সক্ষমতাগুলি তালিকাভুক্ত করব।

### -2- সার্ভারের সক্ষমতাগুলি তালিকাভুক্ত করুন

এখন আমরা সার্ভারের সাথে সংযোগ করব এবং তার সক্ষমতাগুলি জানতে চাইব:

#### TypeScript

একই ক্লাসে নিম্নলিখিত মেথডগুলি যোগ করুন:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // টুলগুলো তালিকাভুক্ত করা হচ্ছে
    const toolsResult = await this.client.listTools();
}
```

উপরের কোডে আমরা:

- সার্ভারের সাথে সংযোগ করার জন্য `connectToServer` কোড যোগ করেছি।
- একটি `run` মেথড তৈরি করেছি যা আমাদের অ্যাপ ফ্লো পরিচালনা করবে। এখন পর্যন্ত এটি কেবল টুলস তালিকাভুক্ত করে, পরবর্তীতে আরও কিছু যোগ করব।

#### Python

```python
# উপলব্ধ সম্পদের তালিকা দিন
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# উপলব্ধ সরঞ্জামগুলির তালিকা দিন
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

আমরা যা যোগ করেছি:

- রিসোর্স এবং টুলস তালিকাভুক্ত এবং প্রিন্ট করেছি। টুলের ক্ষেত্রে `inputSchema` তালিকাভুক্ত করেছি, যা পরে ব্যবহার করব।

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

উপরের কোডে আমরা:

- MCP সার্ভারের উপলব্ধ টুলস তালিকাভুক্ত করেছি
- প্রতিটি টুলের নাম, বর্ণনা এবং স্কিমা তালিকাভুক্ত করেছি। এই স্কিমাটি আমরা শীঘ্রই টুল কল করার জন্য ব্যবহার করব।

#### Java

```java
// এমন একটি টুল প্রদানকারী তৈরি করুন যা স্বয়ংক্রিয়ভাবে MCP টুলগুলি আবিষ্কার করে
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP টুল প্রদানকারী স্বয়ংক্রিয়ভাবে পরিচালনা করে:
// - MCP সার্ভার থেকে উপলব্ধ টুলগুলি তালিকাভুক্ত করা
// - MCP টুল স্কিমাগুলি LangChain4j ফরম্যাটে রূপান্তর করা
// - টুল কার্যকরকরণ এবং প্রতিক্রিয়াগুলি পরিচালনা করা
```

উপরের কোডে আমরা:

- একটি `McpToolProvider` তৈরি করেছি যা স্বয়ংক্রিয়ভাবে MCP সার্ভার থেকে সব টুল আবিষ্কার এবং নিবন্ধন করে
- টুল প্রোভাইডার MCP টুল স্কিমা এবং LangChain4j-এর টুল ফরম্যাটের মধ্যে রূপান্তর অভ্যন্তরীণভাবে পরিচালনা করে
- এই পদ্ধতি ম্যানুয়াল টুল তালিকা এবং রূপান্তর প্রক্রিয়াটি লুকিয়ে রাখে

#### Rust

MCP সার্ভার থেকে টুলস পুনরুদ্ধার করা `list_tools` মেথড ব্যবহার করে করা হয়। আপনার `main` ফাংশনে MCP ক্লায়েন্ট সেটআপ করার পর নিচের কোডটি যোগ করুন:

```rust
// MCP টুল তালিকা পান
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- সার্ভারের সক্ষমতাকে LLM টুলসে রূপান্তর করুন

পরবর্তী ধাপ হল সার্ভারের সক্ষমতাকে এমন ফরম্যাটে রূপান্তর করা যা LLM বুঝতে পারে। একবার আমরা এটি করলে, আমরা এই সক্ষমতাগুলো টুলস হিসেবে আমাদের LLM-এ দিতে পারব।

#### TypeScript

1. MCP সার্ভারের রেসপন্সকে LLM ব্যবহারযোগ্য একটা টুল ফরম্যাটে রূপান্তরের জন্য নিচের কোড যুক্ত করুন:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ইনপুট_স্কিমা উপর ভিত্তি করে একটি জোড স্কিমা তৈরি করুন
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // স্পষ্টভাবে টাইপ "function" সেট করুন
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

    উপরের কোড MCP সার্ভারের একটি রেসপন্স নিয়ে তা এমন টুল ডেফিনিশনে রূপান্তর করে যা LLM বুঝতে পারে।

1. এবার `run` মেথডটি আপডেট করি সার্ভারের সক্ষমতা তালিকাভুক্ত করতে:

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

    আগের কোডে, আমরা `run` মেথড আপডেট করে ফলাফল গুলোতে ম্যাপ করেছি এবং প্রতিটি এন্ট্রিতে `openAiToolAdapter` কল করেছি।

#### Python

1. প্রথমে, নিচের রূপান্তর ফাংশন তৈরি করুন

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

    `convert_to_llm_tools` ফাংশনে মাহত্তব, আমরা MCP টুল রেসপন্স নিয়ে তা এমন একটি ফর্ম্যাটে রূপান্তর করছি যা LLM বুঝতে পারে।

1. এবার আমাদের ক্লায়েন্ট কোড আপডেট করে এই ফাংশন ব্যবহার করি:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    এখানে আমরা MCP টুল রেসপন্সকে LLM-এ ফিড করার জন্য রূপান্তর করতে `convert_to_llm_tool` ফাংশন কল করছি।

#### .NET

1. MCP টুল রেসপন্সকে LLM বোঝার মতো রূপান্তর করার কোড যোগ করি:

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

উপরের কোডে আমরা:

- `ConvertFrom` নামে একটি ফাংশন তৈরি করেছি যা নাম, বর্ণনা এবং ইনপুট স্কিমা নেয়।
- একটি ফাংশন যা `FunctionDefinition` তৈরি করে যা `ChatCompletionsDefinition` এ পাস হয়। পরবর্তীটি LLM বোঝে।

1. পরবর্তীতে এই ফাংশনের সুবিধা নিতে বিদ্যমান কোড আপডেট করি:

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
// প্রাকৃতিক ভাষায় ইন্টারঅ্যাকশনের জন্য একটি বট ইন্টারফেস তৈরি করুন
public interface Bot {
    String chat(String prompt);
}

// LLM এবং MCP সরঞ্জাম সহ AI সেবা কনফিগার করুন
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

উপরের কোডে আমরা:

- প্রাকৃতিক ভাষায় ইন্টারঅ্যাকশনের জন্য একটি সিম্পল `Bot` ইন্টারফেস ডিফাইন করেছি
- LangChain4j-এর `AiServices` ব্যবহার করে LLM এবং MCP টুল প্রোভাইডার স্বয়ংক্রিয়ভাবে বেঁধেছি
- ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে টুল স্কিমা রূপান্তর এবং ফাংশন কলিং পরিচালনা করে
- এই পদ্ধতি ম্যানুয়াল টুল রূপান্তর বাতিল করে — LangChain4j MCP টুলগুলোকে LLM-সঙ্গত ফরম্যাটে রূপান্তর করার পুরা জটিলতা হ্যান্ডেল করে

#### Rust

MCP টুল রেসপন্সকে LLM বোঝার মতো রূপান্তর করতে আমরা একটি হেল্পার ফাংশন যোগ করব যা টুলস তালিকাকে ফরম্যাট করে। আপনার `main.rs` ফাইলে `main` ফাংশনের নিচে নিম্নলিখিত কোড যোগ করুন। এটি LLM এর জন্য অনুরোধ করার সময় কল করা হবে:

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

দারুন, এখন আমরা ব্যবহারকারীর অনুরোধগুলো হ্যান্ডেল করার জন্য প্রস্তুত, এবার সেটাই করি।

### -4- ব্যবহারকারীর প্রম্পট হ্যান্ডেল করা

এই অংশে আমরা ব্যবহারকারীর অনুরোধসমূহ হ্যান্ডেল করব।

#### TypeScript

1. একটি মেথড যোগ করুন যা আমাদের LLM কল করার জন্য ব্যবহৃত হবে:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // ২. সার্ভারের টুল কল করুন
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ৩. ফলাফল দিয়ে কিছু করুন
        // করতে হবে

        }
    }
    ```

    উপরের কোডে আমরা:

    - `callTools` নামে একটি মেথড যোগ করেছি।
    - মেথডটি একটি LLM রেসপন্স নেয় এবং দেখে কোন টুলস কল হয়েছে কি না:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // টুল কল করুন
        }
        ```

    - যদি LLM নির্দেশ দেয়, তাহলে একটি টুল কল করা হয়:

        ```typescript
        // ২. সার্ভারের টুল কল করুন
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ৩. ফলাফলের সাথে কিছু করুন
        // TODO
        ```

1. `run` মেথড আপডেট করুন যাতে LLM কল এবং `callTools` কল অন্তর্ভুক্ত থাকে:

    ```typescript

    // 1. LLM-এর ইনপুট হিসেবে মেসেজ তৈরি করুন
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM কল করা হচ্ছে
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM প্রতিক্রিয়া পর্যালোচনা করুন, প্রতিটি বিকল্পের জন্য দেখুন এটি টুল কল আছে কিনা
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

দারুন, পুরো কোডটি নিচে দেওয়া হলো:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // স্কিমা যাচাইয়ের জন্য zod আমদানি করুন

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ভবিষ্যতে হয়তো এই URL-এ পরিবর্তন করতে হতে পারে: https://models.github.ai/inference
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
          // ইনপুট_স্কিমার উপর ভিত্তি করে একটি zod স্কিমা তৈরি করুন
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // স্পষ্টভাবে টাইপ "function" হিসেবে সেট করুন
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
    
    
          // 2. সার্ভারের টুল কল করুন
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ফলাফলের সাথে কিছু করুন
          // টুডু
    
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
    
        // 1. LLM উত্তরের মাধ্যমে যান, প্রতিটি বিকল্পের জন্য, দেখুন এটি টুল কল রয়েছে কিনা
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

1. LLM কল করার জন্য প্রয়োজনীয় কিছু ইমপোর্ট যোগ করুন

    ```python
    # এলএলএম
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. এরপর, এমন একটি ফাংশন যোগ করুন যা LLM কল করবে:

    ```python
    # এলএলএম

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
            # ঐচ্ছিক প্যারামিটারসমূহ
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

উপরের কোডে আমরা:

- আমাদের ফাংশনগুলো, যেগুলো MCP সার্ভার থেকে পেয়েছি এবং রূপান্তর করেছি, LLM-এ পাস করেছি।
- তারপর আমরা LLM-এ কল করেছি ওই ফাংশনগুলো সহ।
- রেজাল্ট পর্যালোচনা করেছি কোন ফাংশন কল করতে হবে কি না দেখতে।
- অবশেষে কল করার জন্য ফাংশনগুলোর অ্যারে পাস করেছি।

1. শেষ ধাপ, আমাদের মূল কোড আপডেট করি:

    ```python
    prompt = "Add 2 to 20"

    # LLM কে জিজ্ঞাসা করুন সব টুলস সম্পর্কে, যদি থাকে কোনো
    functions_to_call = call_llm(prompt, functions)

    # প্রস্তাবিত ফাংশনগুলো কল করুন
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

এটিই ছিল চূড়ান্ত ধাপ, উপরের কোডে আমরা:

- LLM প্রম্পট থেকে সিদ্ধান্ত অনুযায়ী `call_tool` পদ্ধতি দিয়ে MCP টুল কল করছি।
- MCP সার্ভারের টুল কলের ফলাফল প্রিন্ট করছি।

#### .NET

1. LLM প্রম্পট অনুরোধ করার কোড দেখানো হলো:

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

উপরের কোডে আমরা:

- MCP সার্ভার থেকে টুলস পেয়েছি, `var tools = await GetMcpTools()`.
- একটি ব্যবহারকারীর প্রম্পট বর্ণনা করেছি `userMessage`.
- মডেল এবং টুলস উল্লেখ করে একটি অপশন অবজেক্ট তৈরি করেছি।
- LLM-এ একটি অনুরোধ পাঠিয়েছি।

1. আরেকটি শেষ ধাপ, দেখুন LLM কি মনে করে কোন ফাংশন কল করা উচিত:

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

উপরের কোডে আমরা:

- ফাংশন কলের তালিকায় লুপ করেছি।
- প্রতিটি টুল কলের জন্য নাম এবং আর্গুমেন্ট পার্স করে MCP সার্ভারে টুল কল করেছি MCP ক্লায়েন্ট ব্যবহার করে এবং ফলাফল প্রিন্ট করেছি।

সম্পূর্ণ কোড নিচে:

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
    // স্বয়ংক্রিয়ভাবে MCP টুলগুলি ব্যবহার করে প্রাকৃতিক ভাষার অনুরোধগুলি সম্পাদন করুন
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

উপরের কোডে আমরা:

- সহজ প্রাকৃতিক ভাষার প্রম্পট ব্যবহার করে MCP সার্ভারের টুলগুলোর সাথে ইন্টারঅ্যাকশন করেছি
- LangChain4j ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে:
  - প্রয়োজন হলে ব্যবহারকারীর প্রম্পট থেকে টুল কল রূপান্তর করে
  - LLM সিদ্ধান্ত অনুযায়ী MCP টুলগুলি কল করে
  - LLM এবং MCP সার্ভারের মধ্যে কথোপকথন প্রবাহ পরিচালনা করে
- `bot.chat()` মেথড প্রাকৃতিক ভাষার উত্তর রিটার্ন করে যার মধ্যে MCP টুল কার্যক্রমের ফলাফল থাকতে পারে
- এই পদ্ধতি ব্যবহারকারীর জন্য একটি নির্বিঘ্ন অভিজ্ঞতা দেয় যেখানে তারা MCP বাস্তবায়ন সম্পর্কে জানার দরকার পড়ে না

পূর্ণ কোড উদাহরণ:

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

এখানেই মূল কাজটি হয়। আমরা প্রথমে ব্যবহারকারীর প্রারম্ভিক প্রম্পট নিয়ে LLM কল করব, তারপর রেসপন্স যাচাই করব কোন টুল কল করা দরকার কিনা। যদি দরকার হয়, তাহলে সেই টুলগুলো কল করব এবং LLM-এর সঙ্গে কথোপকথন চালিয়ে যাব যতক্ষণ আর কোনও টুল কল দরকার না হয় এবং আমাদের একটি চূড়ান্ত উত্তর না আসে।

আমরা LLM-এ একাধিক কল করব, সেক্ষেত্রে একটি ফাংশন তৈরি করি যা LLM কল হ্যান্ডেল করবে। নিচের ফাংশনটি আপনার `main.rs` ফাইলে যোগ করুন:

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

এই ফাংশনটি LLM ক্লায়েন্ট, মেসেজের একটি তালিকা (ব্যবহারকারীর প্রম্পটসহ), MCP সার্ভারের টুলস নেয়, LLM-এ অনুরোধ পাঠায় এবং রেসপন্স রিটার্ন করে।
LLM থেকে উত্তর একটি `choices` অ্যারে থাকবে। আমরা ফলাফল প্রক্রিয়া করতে হবে দেখতে যদি কোন `tool_calls` উপস্থিত আছে। এটি আমাদের জানায় যে LLM একটি নির্দিষ্ট সরঞ্জামকে আর্গুমেন্ট সহ কল করার অনুরোধ করছে। LLM উত্তর হ্যান্ডেল করার জন্য একটি ফাংশন সংজ্ঞায়িত করতে আপনার `main.rs` ফাইলের নিচের দিকে নিম্নলিখিত কোড যুক্ত করুন:

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

    // যদি উপলব্ধ থাকে তবেই কনটেন্ট প্রিন্ট করুন
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // টুল কলগুলি পরিচালনা করুন
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // সহকারী বার্তা যোগ করুন

        // প্রতিটি টুল কল সম্পাদন করুন
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // বার্তাতে টুলের ফলাফল যোগ করুন
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // টুল ফলাফলের সাথে কথোপকথন চালিয়ে যান
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

যদি `tool_calls` উপস্থিত থাকে, এটি টুল তথ্য বের করে, MCP সার্ভারে টুল অনুরোধ সহ কল করে, এবং কথোপকথন বার্তাগুলিতে ফলাফল যোগ করে। এরপর এটি LLM এর সাথে কথোপকথন চালিয়ে যায় এবং বার্তাগুলো সহকারী প্রতিক্রিয়া এবং টুল কল ফলাফল সহ আপডেট হয়।

LLM যেসব MCP কলের জন্য টুল কল তথ্য প্রদান করে সেগুলো বের করতে, আমরা আরেকটি সহায়ক ফাংশন যোগ করবো যাতে কল করার জন্য প্রয়োজনীয় সবকিছু বের করা যায়। আপনার `main.rs` ফাইলের নিচের দিকে নিম্নলিখিত কোড যুক্ত করুন:

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

সব উপাদান প্রস্তুত থাকার পরে, এখন আমরা প্রাথমিক ব্যবহারকারীর প্রম্পট হ্যান্ডেল করতে এবং LLM কল করতে পারি। আপনার `main` ফাংশন আপডেট করুন নিম্নলিখিত কোডটি যুক্ত করে:

```rust
// টুল কল সহ এলএলএম সংলাপন
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

এটি প্রাথমিক ব্যবহারকারীর প্রম্পট সহ LLM কে প্রশ্ন করবে, যা দুই সংখ্যার যোগফল জানতে চায়, এবং এটি প্রতিক্রিয়াটি প্রক্রিয়া করবে টুল কল গুলো গতিশীলভাবে হ্যান্ডেল করার জন্য।

দারুণ, আপনি করতে পেরেছেন!

## অ্যাসাইনমেন্ট

এক্সারসাইজ থেকে কোড নিয়ে সার্ভারটি আরও কিছু টুল সহ তৈরি করুন। তারপরে একটি ক্লায়েন্ট তৈরি করুন যেটিতে একটি LLM থাকবে, যেমন এক্সারসাইজে, এবং বিভিন্ন প্রম্পট দিয়ে পরীক্ষা করুন যাতে নিশ্চিত হওয়া যায় আপনার সব সার্ভার টুল ডায়নামিকভাবে কল হচ্ছে। এই ধরনের ক্লায়েন্ট নির্মাণ মানে শেষ ব্যবহারকারী একটি চমৎকার ব্যবহারকারীর অভিজ্ঞতা পাবে কারণ তারা নির্দিষ্ট ক্লায়েন্ট কমান্ডের পরিবর্তে প্রম্পট ব্যবহার করতে পারবে এবং MCP সার্ভার কল হওয়া নিয়ে অজানা থাকবে।

## সমাধান

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## মূল বিষয়বস্তু

- আপনার ক্লায়েন্টে একটি LLM যোগ করা ব্যবহারকারীদের MCP সার্ভারগুলির সাথে ইন্টারঅ্যাকশনের একটি ভালো উপায় প্রদান করে।
- MCP সার্ভারের প্রতিক্রিয়াকে LLM বুঝতে পারে এমন কিছুতে রূপান্তর করতে হবে।

## নমুনা

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## অতিরিক্ত রিসোর্স

## পরবর্তী কি

- পরবর্তী: [Visual Studio Code ব্যবহার করে একটি সার্ভার ব্যবহার](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি এআই অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসম্ভব সঠিকতার প্রতি গুরুত্ব দিই, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার মুল ভাষায়ই কর্তৃপক্ষসূত্র হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ প্রয়োজন। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ব্যাখ্যামূলক ত্রুটির জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->