# LLM সহ একটি ক্লায়েন্ট তৈরি করা

এখন পর্যন্ত, আপনি দেখেছেন কীভাবে একটি সার্ভার এবং একটি ক্লায়েন্ট তৈরি করতে হয়। ক্লায়েন্ট স্পষ্টভাবে সার্ভারকে কল করতে পেরেছে তার টুলস, রিসোর্স এবং প্রম্পটগুলি তালিকাভুক্ত করার জন্য। তবে, এটি খুবই ব্যবহারিক পদ্ধতি নয়। আপনার ব্যবহারকারী এজেন্টিক যুগে বাস করে এবং প্রম্পট ব্যবহার করতে এবং একটি LLM এর সাথে যোগাযোগ করতে আশা করে। আপনার ব্যবহারকারীর জন্য, তারা MCP ব্যবহার করছেন কিনা তা নিয়ে তেমন যত্ন করে না, তবে তারা প্রাকৃতিক ভাষা ব্যবহার করে ইন্টারঅ্যাক্ট করতে আশা করে। তাহলে আমরা কীভাবে এটি সমাধান করব? সমাধান হল ক্লায়েন্টে একটি LLM যোগ করা।

## ওভারভিউ

এই পাঠে আমরা ক্লায়েন্টে একটি LLM যোগ করার উপর ফোকাস করব এবং দেখাব কীভাবে এটি আপনার ব্যবহারকারীর জন্য একটি অনেক ভাল অভিজ্ঞতা প্রদান করে।

## শেখার উদ্দেশ্য

এই পাঠের শেষে, আপনি সক্ষম হবেন:

- একটি LLM সহ একটি ক্লায়েন্ট তৈরি করতে।
- একটি MCP সার্ভারের সাথে LLM ব্যবহার করে নির্বিঘ্নে ইন্টারঅ্যাক্ট করতে।
- ক্লায়েন্ট সাইডে একটি উন্নত শেষ ব্যবহারকারী অভিজ্ঞতা প্রদান করতে।

## পদ্ধতি

চলুন বুঝতে চেষ্টা করি আমাদের কোন পদ্ধতি গ্রহণ করতে হবে। একটি LLM যোগ করা সহজ শোনায়, কিন্তু আমরা কি সত্যিই এটি করব?

ক্লায়েন্ট কীভাবে সার্ভারের সাথে ইন্টারঅ্যাক্ট করবে তা এখানে:

1. সার্ভারের সাথে সংযোগ স্থাপন করুন।

1. ক্ষমতা, প্রম্পট, রিসোর্স এবং টুলস তালিকাভুক্ত করুন এবং তাদের স্কিমা সংরক্ষণ করুন।

1. একটি LLM যোগ করুন এবং সংরক্ষিত ক্ষমতা এবং তাদের স্কিমা এমন একটি ফরম্যাটে পাঠান যা LLM বুঝতে পারে।

1. একটি ব্যবহারকারী প্রম্পট হ্যান্ডেল করুন, এটি LLM-এ পাঠিয়ে দিন ক্লায়েন্ট দ্বারা তালিকাভুক্ত টুলস সহ।

দারুণ, এখন আমরা উচ্চ স্তরে বুঝতে পেরেছি কীভাবে এটি করা যায়, নিচের অনুশীলনে এটি চেষ্টা করি।

## অনুশীলন: একটি LLM সহ ক্লায়েন্ট তৈরি করা

এই অনুশীলনে, আমরা আমাদের ক্লায়েন্টে একটি LLM যোগ করতে শিখব।

### GitHub পার্সোনাল অ্যাক্সেস টোকেন ব্যবহার করে প্রমাণীকরণ

GitHub টোকেন তৈরি করা একটি সরল প্রক্রিয়া। এখানে কীভাবে করবেন:

- GitHub সেটিংসে যান – উপরের ডান কোণে আপনার প্রোফাইল ছবিতে ক্লিক করুন এবং সেটিংস নির্বাচন করুন।
- ডেভেলপার সেটিংসে যান – নিচে স্ক্রল করুন এবং ডেভেলপার সেটিংসে ক্লিক করুন।
- পার্সোনাল অ্যাক্সেস টোকেন নির্বাচন করুন – ফাইন-গ্রেইনড টোকেনস-এ ক্লিক করুন এবং তারপর নতুন টোকেন তৈরি করুন।
- আপনার টোকেন কনফিগার করুন – রেফারেন্সের জন্য একটি নোট যোগ করুন, মেয়াদ শেষের তারিখ সেট করুন, এবং প্রয়োজনীয় স্কোপ (অনুমতি) নির্বাচন করুন। এই ক্ষেত্রে অবশ্যই Models অনুমতি যোগ করুন।
- টোকেন তৈরি করুন এবং কপি করুন – Generate token-এ ক্লিক করুন, এবং তাৎক্ষণিক কপি করুন, কারণ আপনি এটি আর দেখতে পারবেন না।

### -1- সার্ভারের সাথে সংযোগ স্থাপন করুন

চলুন প্রথমে আমাদের ক্লায়েন্ট তৈরি করি:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // স্কিমা যাচাইয়ের জন্য zod ইম্পোর্ট করুন

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

- প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করেছি
- একটি ক্লাস তৈরি করেছি যার দুটি সদস্য, `client` এবং `openai`, যা আমাদের ক্লায়েন্ট পরিচালনা করতে এবং LLM এর সাথে ইন্টারঅ্যাক্ট করতে সাহায্য করবে।
- আমাদের LLM ইনস্ট্যান্স কনফিগার করেছি GitHub Models ব্যবহার করার জন্য `baseUrl` সেট করে যা ইনফারেন্স API নির্দেশ করে।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio সংযোগের জন্য সার্ভার প্যারামিটার তৈরি করুন
server_params = StdioServerParameters(
    command="mcp",  # এক্সিকিউটেবল
    args=["run", "server.py"],  # ঐচ্ছিক কমান্ড লাইন আর্গুমেন্ট
    env=None,  # ঐচ্ছিক পরিবেশ ভেরিয়েবল
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # সংযোগ আরম্ভ করুন
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

উপরের কোডে আমরা:

- MCP এর জন্য প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করেছি
- একটি ক্লায়েন্ট তৈরি করেছি

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

#### Java

প্রথমে, আপনাকে আপনার `pom.xml` ফাইলে LangChain4j ডিপেন্ডেন্সি যোগ করতে হবে। MCP ইন্টিগ্রেশন এবং GitHub Models সাপোর্ট সক্ষম করতে এই ডিপেন্ডেন্সিগুলি যোগ করুন:

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

তারপর আপনার Java ক্লায়েন্ট ক্লাস তৈরি করুন:

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
    
    public static void main(String[] args) throws Exception {        // LLM-কে GitHub মডেল ব্যবহার করার জন্য কনফিগার করুন
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

- **LangChain4j ডিপেন্ডেন্সি যোগ করেছি**: MCP ইন্টিগ্রেশন, OpenAI অফিসিয়াল ক্লায়েন্ট, এবং GitHub Models সাপোর্টের জন্য
- **LangChain4j লাইব্রেরি ইমপোর্ট করেছি**: MCP ইন্টিগ্রেশন এবং OpenAI চ্যাট মডেল ফাংশনালিটির জন্য
- **`ChatLanguageModel` তৈরি করেছি**: GitHub Models ব্যবহার করার জন্য আপনার GitHub টোকেন সহ কনফিগার করা হয়েছে
- **HTTP ট্রান্সপোর্ট সেটআপ করেছি**: Server-Sent Events (SSE) ব্যবহার করে MCP সার্ভারের সাথে সংযোগের জন্য
- **MCP ক্লায়েন্ট তৈরি করেছি**: যা সার্ভারের সাথে যোগাযোগ পরিচালনা করবে
- **LangChain4j এর বিল্ট-ইন MCP সাপোর্ট ব্যবহার করেছি**: যা LLM এবং MCP সার্ভারের মধ্যে ইন্টিগ্রেশন সহজ করে

#### Rust

এই উদাহরণটি ধরে নিচ্ছে আপনার একটি Rust ভিত্তিক MCP সার্ভার চলছে। যদি না থাকে, তাহলে [01-first-server](../01-first-server/README.md) পাঠে ফিরে যান সার্ভার তৈরি করতে।

আপনার Rust MCP সার্ভার থাকলে, একটি টার্মিনাল খুলুন এবং সার্ভারের একই ডিরেক্টরিতে যান। তারপর নিচের কমান্ডটি চালিয়ে একটি নতুন LLM ক্লায়েন্ট প্রজেক্ট তৈরি করুন:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

আপনার `Cargo.toml` ফাইলে নিম্নলিখিত ডিপেন্ডেন্সিগুলি যোগ করুন:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI এর জন্য একটি অফিসিয়াল Rust লাইব্রেরি নেই, তবে `async-openai` ক্রেটটি একটি [কমিউনিটি রক্ষণাবেক্ষিত লাইব্রেরি](https://platform.openai.com/docs/libraries/rust#rust) যা সাধারণত ব্যবহৃত হয়।

`src/main.rs` ফাইলটি খুলুন এবং এর বিষয়বস্তু নিম্নলিখিত কোড দিয়ে প্রতিস্থাপন করুন:

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

    // TODO: MCP টুল তালিকা পান

    // TODO: টুল কল সহ LLM কথোপকথন

    Ok(())
}
```

এই কোড একটি বেসিক Rust অ্যাপ্লিকেশন সেটআপ করে যা MCP সার্ভার এবং GitHub Models এর সাথে LLM ইন্টারঅ্যাকশনের জন্য সংযোগ স্থাপন করবে।

> [!IMPORTANT]
> অ্যাপ্লিকেশন চালানোর আগে অবশ্যই `OPENAI_API_KEY` পরিবেশ ভেরিয়েবলে আপনার GitHub টোকেন সেট করুন।

দারুণ, পরবর্তী ধাপে, চলুন সার্ভারের ক্ষমতাগুলি তালিকাভুক্ত করি।

### -2- সার্ভারের ক্ষমতাগুলি তালিকাভুক্ত করুন

এখন আমরা সার্ভারের সাথে সংযোগ করব এবং তার ক্ষমতাগুলি চাইব:

#### Typescript

একই ক্লাসে, নিম্নলিখিত মেথডগুলি যোগ করুন:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // সরঞ্জাম তালিকা করা
    const toolsResult = await this.client.listTools();
}
```

উপরের কোডে আমরা:

- সার্ভারের সাথে সংযোগ করার জন্য কোড যোগ করেছি, `connectToServer`।
- একটি `run` মেথড তৈরি করেছি যা আমাদের অ্যাপ ফ্লো পরিচালনা করবে। এখন পর্যন্ত এটি শুধুমাত্র টুলস তালিকাভুক্ত করে, তবে আমরা শীঘ্রই আরও যোগ করব।

#### Python

```python
# উপলব্ধ সম্পদগুলি তালিকা করুন
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# উপলব্ধ সরঞ্জামগুলি তালিকা করুন
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

আমরা যা যোগ করেছি:

- রিসোর্স এবং টুলস তালিকাভুক্ত করেছি এবং প্রিন্ট করেছি। টুলসের জন্য আমরা `inputSchema` ও তালিকাভুক্ত করেছি যা পরে ব্যবহার করব।

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

- MCP সার্ভারে উপলব্ধ টুলস তালিকাভুক্ত করেছি
- প্রতিটি টুলের জন্য নাম, বর্ণনা এবং তার স্কিমা তালিকাভুক্ত করেছি। পরবর্তীতে আমরা এই স্কিমা ব্যবহার করব টুলস কল করার জন্য।

#### Java

```java
// একটি টুল প্রদানকারী তৈরি করুন যা স্বয়ংক্রিয়ভাবে MCP টুলগুলি আবিষ্কার করে
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP টুল প্রদানকারী স্বয়ংক্রিয়ভাবে পরিচালনা করে:
// - MCP সার্ভার থেকে উপলব্ধ টুলগুলির তালিকা তৈরি করা
// - MCP টুল স্কিমাগুলিকে LangChain4j ফরম্যাটে রূপান্তর করা
// - টুলের কার্যকরীতা এবং প্রতিক্রিয়া পরিচালনা করা
```

উপরের কোডে আমরা:

- একটি `McpToolProvider` তৈরি করেছি যা স্বয়ংক্রিয়ভাবে MCP সার্ভার থেকে সব টুল আবিষ্কার এবং নিবন্ধন করে
- টুল প্রোভাইডার MCP টুল স্কিমা এবং LangChain4j এর টুল ফরম্যাটের মধ্যে রূপান্তর অভ্যন্তরীণভাবে পরিচালনা করে
- এই পদ্ধতি ম্যানুয়াল টুল তালিকা এবং রূপান্তর প্রক্রিয়া থেকে মুক্তি দেয়

#### Rust

MCP সার্ভার থেকে টুলস পুনরুদ্ধার করা হয় `list_tools` মেথড ব্যবহার করে। আপনার `main` ফাংশনে, MCP ক্লায়েন্ট সেটআপ করার পরে, নিম্নলিখিত কোড যোগ করুন:

```rust
// MCP টুল তালিকা পান
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- সার্ভারের ক্ষমতাগুলি LLM টুলসে রূপান্তর করুন

সার্ভারের ক্ষমতাগুলি তালিকাভুক্ত করার পরের ধাপ হল সেগুলোকে এমন একটি ফরম্যাটে রূপান্তর করা যা LLM বুঝতে পারে। একবার আমরা এটি করলে, আমরা এই ক্ষমতাগুলোকে আমাদের LLM এর জন্য টুলস হিসেবে প্রদান করতে পারব।

#### TypeScript

1. MCP সার্ভারের প্রতিক্রিয়া থেকে LLM ব্যবহারযোগ্য টুল ফরম্যাটে রূপান্তর করার জন্য নিম্নলিখিত কোড যোগ করুন:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ইনপুট_স্কিমার উপর ভিত্তি করে একটি জড স্কিমা তৈরি করুন
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

    উপরের কোড MCP সার্ভারের প্রতিক্রিয়া নিয়ে সেটিকে এমন একটি টুল ডেফিনিশন ফরম্যাটে রূপান্তর করে যা LLM বুঝতে পারে।

1. পরবর্তী ধাপে `run` মেথড আপডেট করুন সার্ভারের ক্ষমতাগুলি তালিকাভুক্ত করার জন্য:

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

    উপরের কোডে, আমরা `run` মেথড আপডেট করেছি যাতে ফলাফলের প্রতিটি এন্ট্রির জন্য `openAiToolAdapter` কল করা হয়।

#### Python

1. প্রথমে, নিম্নলিখিত কনভার্টার ফাংশন তৈরি করুন

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

    উপরের `convert_to_llm_tools` ফাংশনে আমরা MCP টুল প্রতিক্রিয়া নিয়ে সেটিকে এমন একটি ফরম্যাটে রূপান্তর করি যা LLM বুঝতে পারে।

1. পরবর্তী ধাপে, আমাদের ক্লায়েন্ট কোড আপডেট করি এই ফাংশন ব্যবহার করার জন্য:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    এখানে, আমরা MCP টুল প্রতিক্রিয়া রূপান্তর করার জন্য `convert_to_llm_tool` কল যোগ করছি যাতে পরে LLM-এ ফিড করতে পারি।

#### .NET

1. MCP টুল প্রতিক্রিয়া থেকে LLM বুঝতে পারার মতো ফরম্যাটে রূপান্তর করার কোড যোগ করি

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

- একটি `ConvertFrom` ফাংশন তৈরি করেছি যা নাম, বর্ণনা এবং ইনপুট স্কিমা নেয়।
- একটি ফাংশনালিটি সংজ্ঞায়িত করেছি যা একটি `FunctionDefinition` তৈরি করে যা `ChatCompletionsDefinition` এ পাস হয়। পরবর্তীতে এটি LLM বুঝতে পারে।

1. চলুন দেখি কীভাবে বিদ্যমান কোড আপডেট করা যায় এই ফাংশন ব্যবহার করার জন্য:

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
// প্রাকৃতিক ভাষার ইন্টারঅ্যাকশনের জন্য একটি বট ইন্টারফেস তৈরি করুন
public interface Bot {
    String chat(String prompt);
}

// LLM এবং MCP টুলস দিয়ে AI সার্ভিস কনফিগার করুন
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

উপরের কোডে আমরা:

- প্রাকৃতিক ভাষার ইন্টারঅ্যাকশনের জন্য একটি সহজ `Bot` ইন্টারফেস সংজ্ঞায়িত করেছি
- LangChain4j এর `AiServices` ব্যবহার করেছি যা স্বয়ংক্রিয়ভাবে LLM কে MCP টুল প্রোভাইডারের সাথে বেঁধে দেয়
- ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে টুল স্কিমা রূপান্তর এবং ফাংশন কলিং পরিচালনা করে
- এই পদ্ধতি ম্যানুয়াল টুল রূপান্তর দূর করে - LangChain4j MCP টুলসকে LLM-সঙ্গত ফরম্যাটে রূপান্তরের সব জটিলতা পরিচালনা করে

#### Rust

MCP টুল প্রতিক্রিয়া থেকে LLM বুঝতে পারার মতো ফরম্যাটে রূপান্তর করার জন্য, আমরা একটি হেল্পার ফাংশন যোগ করব যা টুলস তালিকাভুক্তি ফরম্যাট করবে। আপনার `main.rs` ফাইলে `main` ফাংশনের নিচে নিম্নলিখিত কোড যোগ করুন। এটি LLM-এ অনুরোধ করার সময় কল করা হবে:

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

দারুণ, এখন আমরা ব্যবহারকারীর অনুরোধ হ্যান্ডেল করার জন্য প্রস্তুত, তাই চলুন সেটি করি।

### -4- ব্যবহারকারী প্রম্পট অনুরোধ হ্যান্ডেল করুন

এই অংশে, আমরা ব্যবহারকারীর অনুরোধ হ্যান্ডেল করব।

#### TypeScript

1. একটি মেথড যোগ করুন যা আমাদের LLM কল করতে ব্যবহার হবে:

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

        // ৩. ফলাফলের সাথে কিছু করুন
        // TODO

        }
    }
    ```

    উপরের কোডে আমরা:

    - একটি `callTools` মেথড যোগ করেছি।
    - মেথডটি LLM প্রতিক্রিয়া নিয়ে দেখে কোন টুলস কল হয়েছে, যদি থাকে:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // টুল কল করুন
        }
        ```

    - একটি টুল কল করে, যদি LLM নির্দেশ দেয় কল করতে:

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

    // 1. LLM এর ইনপুট হিসেবে মেসেজ তৈরি করুন
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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM এর প্রতিক্রিয়া পরীক্ষা করুন, প্রতিটি বিকল্পের জন্য দেখুন এতে টুল কল আছে কিনা
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

দারুণ, সম্পূর্ণ কোডটি নিচে দেওয়া হলো:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // স্কিমা যাচাইয়ের জন্য zod ইম্পোর্ট করুন

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ভবিষ্যতে এই URL-এ পরিবর্তন করতে হতে পারে: https://models.github.ai/inference
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
    
          // ৩. ফলাফলের সাথে কিছু করুন
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // ১. LLM প্রতিক্রিয়া পরীক্ষা করুন, প্রতিটি বিকল্পের জন্য দেখুন এটি টুল কল আছে কিনা
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

1. LLM কল করার জন্য প্রয়োজনীয় কিছু ইমপোর্ট যোগ করি

    ```python
    # এলএলএম
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. পরবর্তী ধাপে, LLM কল করার ফাংশন যোগ করি:

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

    - আমাদের ফাংশনগুলি, যা MCP সার্ভারে পাওয়া এবং রূপান্তর করা হয়েছে, LLM-এ পাস করেছি।
    - তারপর LLM কল করেছি উক্ত ফাংশনগুলির সাথে।
    - ফলাফল পরীক্ষা করেছি কোন ফাংশন কল করা উচিত, যদি থাকে।
    - অবশেষে, কল করার জন্য ফাংশনের একটি অ্যারে পাস করেছি।

1. শেষ ধাপ, আমাদের মূল কোড আপডেট করি:

    ```python
    prompt = "Add 2 to 20"

    # LLM কে জিজ্ঞাসা করুন কোন টুলগুলি ব্যবহার করতে হবে, যদি থাকে
    functions_to_call = call_llm(prompt, functions)

    # প্রস্তাবিত ফাংশনগুলি কল করুন
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    উপরের কোডে আমরা:

    - `call_tool` ব্যবহার করে MCP টুল কল করছি একটি ফাংশন দিয়ে যা LLM আমাদের প্রম্পটের ভিত্তিতে কল করা উচিত মনে করেছে।
    - MCP সার্ভারে টুল কলের ফলাফল প্রিন্ট করছি।

#### .NET

1. LLM প্রম্পট অনুরোধ করার জন্য কিছু কোড দেখাই:

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
        Model = "gpt-4o-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

উপরের কোডে আমরা:

- MCP সার্ভার থেকে টুলস নিয়ে এসেছি, `var tools = await GetMcpTools()`.
- একটি ব্যবহারকারী প্রম্পট সংজ্ঞায়িত করেছি `userMessage`.
- মডেল এবং টুলস নির্দিষ্ট করে একটি অপশন অবজেক্ট তৈরি করেছি।
- LLM এর দিকে একটি অনুরোধ পাঠিয়েছি।

1. শেষ ধাপ, দেখি LLM কি মনে করে আমাদের কোন ফাংশন কল করা উচিত:

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

- ফাংশন কলের তালিকা লুপ করেছি।
- প্রতিটি টুল কলের জন্য নাম এবং আর্গুমেন্ট পার্স করে MCP ক্লায়েন্ট ব্যবহার করে MCP সার্ভারে টুল কল করেছি। অবশেষে ফলাফল প্রিন্ট করেছি।

সম্পূর্ণ কোড এখানে:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

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
    Model = "gpt-4o-mini",
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

    Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // স্বয়ংক্রিয়ভাবে MCP টুলস ব্যবহার করে প্রাকৃতিক ভাষার অনুরোধগুলি সম্পাদন করুন
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

- সহজ প্রাকৃতিক ভাষার প্রম্পট ব্যবহার করে MCP সার্ভারের টুলসের সাথে ইন্টারঅ্যাক্ট করেছি
- LangChain4j ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে পরিচালনা করে:
  - প্রয়োজন হলে ব্যবহারকারী প্রম্পটকে টুল কল এ রূপান্তর করা
  - LLM এর সিদ্ধান্ত অনুযায়ী উপযুক্ত MCP টুলস কল করা
  - LLM এবং MCP সার্ভারের মধ্যে কথোপকথনের প্রবাহ পরিচালনা করা
- `bot.chat()` মেথড প্রাকৃতিক ভাষার প্রতিক্রিয়া প্রদান করে যা MCP টুল এক্সিকিউশনের ফলাফল অন্তর্ভুক্ত করতে পারে
- এই পদ্ধতি একটি নির্বিঘ্ন ব্যবহারকারী অভিজ্ঞতা প্রদান করে যেখানে ব্যবহারকারীদের MCP বাস্তবায়ন সম্পর্কে জানতে হয় না

সম্পূর্ণ কোড উদাহরণ:

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

এখানেই বেশিরভাগ কাজ হয়। আমরা প্রথমে ব্যবহারকারীর প্রাথমিক প্রম্পট নিয়ে LLM কল করব, তারপর প্রতিক্রিয়া প্রক্রিয়া করব দেখতে কোন টুল কল করতে হবে কিনা। যদি প্রয়োজন হয়, আমরা সেই টুলগুলো কল করব এবং LLM এর সাথে কথোপকথন চালিয়ে যাব যতক্ষণ না আর কোন টুল কলের প্রয়োজন হয় এবং আমাদের একটি চূড়ান্ত প্রতিক্রিয়া পাওয়া যায়।

আমরা LLM-এ একাধিক কল করব, তাই একটি ফাংশন সংজ্ঞায়িত করি যা LLM কল হ্যান্ডেল করবে। আপনার `main.rs` ফাইলে নিম্নলিখিত ফাংশন যোগ করুন:

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

এই ফাংশনটি LLM ক্লায়েন্ট, মেসেজের একটি তালিকা (ব্যবহারকারী প্রম্পট সহ), MCP সার্ভারের টুলস নেয় এবং LLM-এ একটি অনুরোধ পাঠায়, প্রতিক্রিয়া ফেরত দেয়।
LLM থেকে প্রাপ্ত প্রতিক্রিয়ায় একটি `choices` অ্যারে থাকবে। আমাদের ফলাফল প্রক্রিয়াকরণ করতে হবে দেখতে যে কোনও `tool_calls` উপস্থিত আছে কিনা। এটি আমাদের জানায় যে LLM একটি নির্দিষ্ট টুল কল করার জন্য আর্গুমেন্ট সহ অনুরোধ করছে। LLM প্রতিক্রিয়া পরিচালনার জন্য একটি ফাংশন সংজ্ঞায়িত করতে আপনার `main.rs` ফাইলের নিচে নিম্নলিখিত কোড যোগ করুন:

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

    // যদি উপলব্ধ থাকে তবে বিষয়বস্তু মুদ্রণ করুন
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // টুল কলগুলি পরিচালনা করুন
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // সহকারী বার্তা যোগ করুন

        // প্রতিটি টুল কল কার্যকর করুন
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // বার্তাগুলিতে টুল ফলাফল যোগ করুন
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // টুল ফলাফল সহ কথোপকথন চালিয়ে যান
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

যদি `tool_calls` উপস্থিত থাকে, এটি টুল তথ্য বের করে, MCP সার্ভারে টুল অনুরোধ পাঠায়, এবং ফলাফলগুলি কথোপকথন বার্তাগুলিতে যোগ করে। তারপর এটি LLM এর সাথে কথোপকথন চালিয়ে যায় এবং বার্তাগুলি সহকারী প্রতিক্রিয়া এবং টুল কল ফলাফল দিয়ে আপডেট হয়।

MCP কলের জন্য LLM যে টুল কল তথ্য ফেরত দেয় তা বের করতে, আমরা আরেকটি সহায়ক ফাংশন যোগ করব যা কল করার জন্য প্রয়োজনীয় সবকিছু বের করবে। আপনার `main.rs` ফাইলের নিচে নিম্নলিখিত কোড যোগ করুন:

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

সব অংশ স্থাপিত হওয়ার পরে, আমরা এখন প্রাথমিক ব্যবহারকারীর প্রম্পট পরিচালনা করতে এবং LLM কল করতে পারি। আপনার `main` ফাংশন আপডেট করুন নিম্নলিখিত কোড সহ:

```rust
// টুল কল সহ এলএলএম কথোপকথন
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

এটি প্রাথমিক ব্যবহারকারীর প্রম্পট সহ LLM কে প্রশ্ন করবে দুই সংখ্যার যোগফল জানতে, এবং এটি প্রতিক্রিয়া প্রক্রিয়াকরণ করবে টুল কলগুলি গতিশীলভাবে পরিচালনা করার জন্য।

দারুণ, আপনি এটি করেছেন!

## অ্যাসাইনমেন্ট

ব্যায়াম থেকে কোড নিয়ে সার্ভারটি আরও কিছু টুল দিয়ে তৈরি করুন। তারপর একটি ক্লায়েন্ট তৈরি করুন LLM সহ, যেমন ব্যায়ামে, এবং বিভিন্ন প্রম্পট দিয়ে পরীক্ষা করুন যাতে আপনার সব সার্ভার টুলগুলি গতিশীলভাবে কল হয়। এইভাবে ক্লায়েন্ট তৈরি করলে শেষ ব্যবহারকারীর জন্য একটি চমৎকার ব্যবহারকারীর অভিজ্ঞতা নিশ্চিত হয় কারণ তারা সঠিক ক্লায়েন্ট কমান্ডের পরিবর্তে প্রম্পট ব্যবহার করতে পারে এবং MCP সার্ভার কল হওয়া সম্পর্কে অবগত থাকে না।

## সমাধান

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## মূল বিষয়সমূহ

- আপনার ক্লায়েন্টে LLM যোগ করা MCP সার্ভারের সাথে ব্যবহারকারীদের ইন্টারঅ্যাকশনের একটি উন্নত উপায় প্রদান করে।
- আপনাকে MCP সার্ভারের প্রতিক্রিয়াকে এমন কিছুতে রূপান্তর করতে হবে যা LLM বুঝতে পারে।

## নমুনা

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## অতিরিক্ত সম্পদ

## পরবর্তী কী

- পরবর্তী: [Visual Studio Code ব্যবহার করে একটি সার্ভার ব্যবহার করা](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->