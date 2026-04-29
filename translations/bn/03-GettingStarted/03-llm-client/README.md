# LLM দিয়ে একটি ক্লায়েন্ট তৈরি করা

এখন পর্যন্ত, আপনি দেখেছেন কীভাবে একটি সার্ভার এবং ক্লায়েন্ট তৈরি করতে হয়। ক্লায়েন্ট সার্ভারকে স্পষ্টভাবে কল করে তার সরঞ্জাম, সম্পদ এবং প্রম্পট তালিকাভুক্ত করতে পেরেছে। তবে, এটি খুবই ব্যবহারিক পদ্ধতি নয়। আপনার ব্যবহারকারীরা এজেন্টিক যুগে বাস করে এবং প্রম্পট ব্যবহার করে এবং একটি LLM এর সঙ্গে যোগাযোগ করতে চায়। তারা MCP ব্যবহার করে আপনার ক্ষমতাগুলি সংরক্ষণ করছেন কিনা তা নিয়ে মাথা ঘামায় না; তারা কেবল প্রাকৃতিক ভাষায় ইন্টারঅ্যাক্ট করার প্রত্যাশা করে। তাহলে আমরা কীভাবে এটি সমাধান করব? সমাধান হল ক্লায়েন্টে একটি LLM যুক্ত করা।

## ওভারভিউ

এই পাঠে আমরা ক্লায়েন্টে একটি LLM যোগ করার উপর মনোযোগ কেন্দ্রীভূত করব এবং দেখাব কীভাবে এটি আপনার ব্যবহারকারীর জন্য অনেক ভালো অভিজ্ঞতা প্রদান করে।

## শেখার উদ্দেশ্য

এই পাঠের শেষে, আপনি সক্ষম হবেন:

- একটি LLM সহ ক্লায়েন্ট তৈরি করতে।
- একটি MCP সার্ভারের সঙ্গে LLM ব্যবহার করে নির্বিঘ্নে ইন্টারঅ্যাক্ট করতে।
- ক্লায়েন্ট পাশে ব্যবহারকারীর জন্য একটি উন্নত অভিজ্ঞতা প্রদান করতে।

## পদ্ধতি

আমরা যে পদ্ধতি গ্রহণ করব তা বুঝে নেওয়া যাক। একটি LLM যোগ করা সহজ শোনাতে পারে, তবে আমরা কি আসলেই এটি করব?

ক্লায়েন্ট কীভাবে সার্ভারের সাথে ইন্টারঅ্যাক্ট করবে:

1. সার্ভারের সাথে সংযোগ স্থাপন করুন।

1. ক্ষমতা, প্রম্পট, সম্পদ এবং সরঞ্জাম তালিকাভুক্ত করুন এবং তাদের স্কিমা সংরক্ষণ করুন।

1. একটি LLM যোগ করুন এবং সংরক্ষিত ক্ষমতা এবং তাদের স্কিমা LLM এর বোঝার ফরম্যাটে প্রদান করুন।

1. একটি ব্যবহারকারী প্রম্পট গ্রহণ করুন এবং এটি ক্লায়েন্টের তালিকাভুক্ত সরঞ্জামগুলির সঙ্গে LLM এ পাঠান।

দারুণ, এখন আমরা উচ্চ স্তরে কীভাবে এটি করতে হয় তা বুঝে গেছি, নিচের অনুশীলনে এটি চেষ্টা করি।

## অনুশীলন: একটি LLM সহ ক্লায়েন্ট তৈরি করা

এই অনুশীলনে, আমরা আমাদের ক্লায়েন্টে একটি LLM যোগ করতে শিখব।

### GitHub Personal Access Token দিয়ে প্রমাণীকরণ

GitHub টোকেন তৈরি করা একটি সরল প্রক্রিয়া। আপনি এটি কিভাবে করবেন:

- GitHub সেটিংসে যান – উপরের ডান কোণার আপনার প্রোফাইল ছবি ক্লিক করুন এবং Settings নির্বাচন করুন।
- Developer Settings এ যান – নিচে স্ক্রল করুন এবং Developer Settings ক্লিক করুন।
- Personal Access Tokens নির্বাচন করুন – Fine-grained tokens এ ক্লিক করুন এবং তারপর Generate new token চাপুন।
- আপনার টোকেন কনফিগার করুন – একটি নোট দিন রেফারেন্সের জন্য, মেয়াদ শেষের তারিখ দিন, এবং প্রয়োজনীয় স্কোপ (অনুমতিসমূহ) নির্বাচন করুন। এই ক্ষেত্রে Models অনুমতি নিশ্চিত করুন।
- Generate এবং টোকেন কপি করুন – Generate token ক্লিক করুন, এবং তাৎক্ষণিকভাবে কপি করুন কারণ পরে আর দেখতে পাবেন না।

### -1- সার্ভারে সংযোগ করুন

চলুন প্রথমে আমাদের ক্লায়েন্ট তৈরি করি:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // স্কিমা যাচাইকরণের জন্য জড ইমপোর্ট করুন

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
- দুটি সদস্য সহ একটি ক্লাস তৈরি করেছি, `client` এবং `openai` যা যথাক্রমে ক্লায়েন্ট পরিচালনা এবং LLM এর সঙ্গে ইন্টারঅ্যাক্ট করতে সাহায্য করবে।
- আমাদের LLM ইনস্ট্যান্স কনফিগার করেছি GitHub Models ব্যবহার করার জন্য `baseUrl` কে inference API তে নির্দেশ করে।

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

- MCP জন্য প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করেছি
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

প্রথমে, আপনার `pom.xml` ফাইলে LangChain4j ডিপেনডেন্সিস যুক্ত করতে হবে। MCP ইন্টিগ্রেশন এবং GitHub Models সাপোর্ট সক্ষম করার জন্য এগুলো যুক্ত করুন:

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
    
    public static void main(String[] args) throws Exception {        // LLM কে GitHub মডেল ব্যবহারের জন্য কনফিগার করুন
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // সার্ভারের সাথে সংযোগ স্থাপনের জন্য MCP ট্রান্সপোর্ট তৈরি করুন
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

- **LangChain4j ডিপেনডেন্সিস যুক্ত করেছি**: MCP ইন্টিগ্রেশন, OpenAI অফিসিয়াল ক্লায়েন্ট এবং GitHub Models সাপোর্টের জন্য
- **LangChain4j লাইব্রেরি ইমপোর্ট করেছি**: MCP ইন্টিগ্রেশন এবং OpenAI চ্যাট মডেলের কার্যকারিতার জন্য
- **একটি `ChatLanguageModel` তৈরি করেছি**: GitHub Models ব্যবহার করে আপনার GitHub টোকেন সহ কনফিগার করা
- **HTTP ট্রান্সপোর্ট সেটআপ করেছি**: Server-Sent Events (SSE) ব্যবহার করে MCP সার্ভারের সাথে সংযোগের জন্য
- **একটি MCP ক্লায়েন্ট তৈরি করেছি**: যা সার্ভারের সঙ্গে যোগাযোগ পরিচালনা করবে
- **LangChain4j এর বিল্ট-ইন MCP সাপোর্ট ব্যবহার করেছি**: যা LLM এবং MCP সার্ভারের মধ্যে ইন্টিগ্রেশন সহজ করে

#### Rust

এই উদাহরণটি ধরে নেয় যে আপনার একটি Rust ভিত্তিক MCP সার্ভার চলছে। যদি না থাকে, তাহলে সার্ভার তৈরি করার জন্য [01-first-server](../01-first-server/README.md) পাঠটি দেখুন।

আপনার Rust MCP সার্ভার চালু থাকলে, একটি টার্মিনাল খুলুন এবং সার্ভারের সমান ডিরেক্টরিতে যান। তারপর নিম্নলিখিত কমান্ড চালিয়ে একটি নতুন LLM ক্লায়েন্ট প্রকল্প তৈরি করুন:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

আপনার `Cargo.toml` ফাইলে নিম্নলিখিত ডিপেনডেন্সিস যুক্ত করুন:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI এর জন্য কোনও অফিশিয়াল Rust লাইব্রেরি নেই, তবে `async-openai` ক্রেট একটি [কমিউনিটি মেইন্টেইনড লাইব্রেরি](https://platform.openai.com/docs/libraries/rust#rust) যা সাধারণত ব্যবহৃত হয়।

`src/main.rs` ফাইল খুলুন এবং এর বিষয়বস্তু নিম্নলিখিত কোড দিয়ে প্রতিস্থাপিত করুন:

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

এই কোড একটি মৌলিক Rust অ্যাপ্লিকেশন সেটআপ করে যা MCP সার্ভার এবং GitHub Models এর সঙ্গে LLM ইন্টারঅ্যাকশন করবে।

> [!IMPORTANT]
> অ্যাপ্লিকেশন চালানোর আগে অবশ্যই `OPENAI_API_KEY` এনভায়রনমেন্ট ভেরিয়েবলে আপনার GitHub টোকেন সেট করুন।

দারুণ, আমাদের পরবর্তী ধাপে, চলুন সার্ভারের ক্ষমতাগুলি তালিকাভুক্ত করি।

### -2- সার্ভারের ক্ষমতাগুলি তালিকাভুক্ত করুন

এখন আমরা সার্ভারের সাথে সংযোগ করব এবং তার ক্ষমতাগুলি জানতে চাইব:

#### Typescript

একই ক্লাসে নীচের মেথডগুলি যুক্ত করুন:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // সরঞ্জাম তালিকা
    const toolsResult = await this.client.listTools();
}
```

উপরের কোডে আমরা:

- সার্ভারের সঙ্গে সংযোগ করার কোড যুক্ত করেছি, `connectToServer`।
- একটি `run` মেথড তৈরি করেছি যা আমাদের অ্যাপ ফ্লো পরিচালনা করবে। এখন পর্যন্ত এটি শুধুমাত্র সরঞ্জামগুলো তালিকাভুক্ত করে কিন্তু আমরা শীঘ্রই আরও যোগ করব।

#### Python

```python
# পাওয়া যাওয়া সম্পদসমূহ তালিকা করুন
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# পাওয়া যাওয়া সরঞ্জামসমূহ তালিকা করুন
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

আমরা যা যুক্ত করেছি:

- সম্পদ এবং সরঞ্জাম তালিকাভুক্ত এবং মুদ্রিত হয়েছে। সরঞ্জামগুলোর জন্য আমরা `inputSchema` তালিকাভুক্ত করেছি যা পরে ব্যবহার করব।

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

- MCP সার্ভারের সরঞ্জামগুলো তালিকাভুক্ত করেছি
- প্রতিটি সরঞ্জামের জন্য নাম, বিবরণ এবং তার স্কিমা তালিকাভুক্ত করেছি। পরবর্তীতে এটি ব্যবহার করব।

#### Java

```java
// একটি টুল প্রোভাইডার তৈরি করুন যা স্বয়ংক্রিয়ভাবে MCP টুল আবিষ্কার করে
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP টুল প্রোভাইডার স্বয়ংক্রিয়ভাবে নিম্নলিখিতগুলি পরিচালনা করে:
// - MCP সার্ভার থেকে উপলব্ধ টুলের তালিকা প্রদান
// - MCP টুল স্কিমাগুলিকে LangChain4j ফরম্যাটে রূপান্তর করা
// - টুলের কার্য সম্পাদন এবং প্রতিক্রিয়া পরিচালনা করা
```

উপরের কোডে আমরা:

- একটি `McpToolProvider` তৈরি করেছি যা স্বয়ংক্রিয়ভাবে MCP সার্ভার থেকে সব সরঞ্জাম আবিষ্কার এবং নিবন্ধন করে
- টুল প্রোভাইডার MCP সরঞ্জাম স্কিমাগুলো LanChain4j এর টুল ফরম্যাটে অভ্যন্তরীণভাবে রূপান্তর করে
- এটি ম্যানুয়াল টুল তালিকা এবং রূপান্তর প্রক্রিয়ার থেকে অব্যাহতি দেয়

#### Rust

MCP সার্ভার থেকে সরঞ্জাম সংগ্রহ করা হয় `list_tools` মেথড ব্যবহার করে। আপনার `main` ফাংশনে MCP ক্লায়েন্ট সেটআপ করার পর নিম্নলিখিত কোড যুক্ত করুন:

```rust
// MCP টুল তালিকা পান
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- সার্ভারের ক্ষমতাগুলি LLM টুলে রূপান্তর করুন

সার্ভারের ক্ষমতাগুলি তালিকাভুক্ত করার পর এর পরের ধাপ হলো সেগুলিকে এমন ফরম্যাটে রূপান্তর করা যা LLM বুঝতে পারে। একবার এটি করলে, আমরা এই ক্ষমতাগুলোকে আমাদের LLM এর জন্য টুল হিসেবে দিতে পারব।

#### TypeScript

1. MCP সার্ভারের রেসপন্সকে LLM ব্যবহারযোগ্য টুল ফরম্যাটে রূপান্তর করতে নিম্নলিখিত কোড যুক্ত করুন:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ইনপুট_স্কিমার উপর ভিত্তি করে একটি জড স্কিমা তৈরি করুন
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // স্পষ্টভাবে টাইপ "ফাংশন" সেট করুন
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

উপরের কোডটি MCP সার্ভারের রেসপন্স গ্রহণ করে সেটি LLM বোঝার টুল ডেফিনিশন ফরম্যাটে রূপান্তর করে।

1. `run` মেথড আপডেট করে সার্ভারের ক্ষমতাগুলো তালিকাভুক্ত করা যাক:

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

উপরের কোডে, আমরা `run` মেথড আপডেট করেছি যাতে রেসপন্সের প্রতিটি এন্ট্রির জন্য `openAiToolAdapter` কল করা হয়।

#### Python

1. প্রথমে নিচের রূপান্তর ফাংশনটি তৈরি করুন

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

উপরের `convert_to_llm_tools` ফাংশনে MCP টুল রেসপন্সকে এমন ফরম্যাটে রূপান্তর করা হয়েছে যা LLM বুঝতে পারে।

1. এরপর আমাদের ক্লায়েন্ট কোড আপডেট করি এই ফাংশন ব্যবহার করে:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

এখানে, আমরা MCP টুল রেসপন্সকে LLM কে দেওয়ার জন্য রূপান্তর করতে `convert_to_llm_tool` ফাংশন ব্যবহার করেছি।

#### .NET

1. MCP টুল রেসপন্সকে LLM বোঝার ফরম্যাটে রূপান্তরের কোড যোগ করি

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

- একটি `ConvertFrom` ফাংশন তৈরি করেছি যা নাম, বিবরণ এবং ইনপুট স্কিমা গ্রহণ করে।
- একটি `FunctionDefinition` তৈরি করার কার্যকারিতা সংজ্ঞায়িত করেছি যা `ChatCompletionsDefinition` এ পাস হয়। যে latter টি LLM বুঝতে পারে।

1. চলুন দেখি কিভাবে আগের কোড আপডেট করা যায় এই ফাংশনের সুবিধা নিতে:

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

// এলএলএম এবং এমসিপি টুলস দিয়ে এআই পরিষেবা কনফিগার করুন
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

উপরের কোডে আমরা:

- প্রাকৃতিক ভাষা ইন্টারঅ্যাকশনের জন্য একটি সাধারণ `Bot` ইন্টারফেস সংজ্ঞায়িত করেছি
- LangChain4j এর `AiServices` ব্যবহার করে স্বয়ংক্রিয়ভাবে LLM কে MCP টুল প্রোভাইডারের সঙ্গে যুক্ত করেছি
- ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে টুল স্কিমা রূপান্তর এবং ফাংশন কলিং হ্যান্ডেল করে
- ম্যানুয়াল টুল রূপান্তর প্রয়োজন নেই — LangChain4j MCP টুলগুলোকে LLM-সঙ্গত ফরম্যাটে রূপান্তর করার সমস্ত জটিলতা হ্যান্ডেল করে

#### Rust

MCP টুল রেসপন্সকে LLM বুঝতে পারার মতো ফরম্যাটে রূপান্তর করার জন্য একটি হেল্পার ফাংশন যোগ করব যা টুল তালিকা ফরম্যাট করবে। আপনার `main.rs` ফাইলে `main` ফাংশনের নিচে নিচের কোড যোগ করুন। এটি LLM অনুরোধ করার সময় কল করা হবে:

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

দারুণ, এখন আমরা ব্যবহারকারীর অনুরোধ পরিচালনা করার জন্য প্রস্তুত, তাহলে সেটা করি।

### -4- ব্যবহারকারীর প্রম্পট অনুরোধ পরিচালনা

এই অংশে আমরা ব্যবহারকারীর অনুরোধ হ্যান্ডেল করব।

#### TypeScript

1. একটি মেথড যুক্ত করুন যা আমাদের LLM কল করতে ব্যবহার হবে:

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

        // ৩. ফলাফল নিয়ে কিছু করুন
        // করার আছে

        }
    }
    ```

উপরের কোডে আমরা:

- `callTools` নামের একটি মেথড যুক্ত করেছি।
- এই মেথড LLM রেসপন্স গ্রহণ করে দেখে কোন টুলগুলো কল হয়েছে, যদি থাকে:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // টুল কল করুন
        }
        ```

- যদি LLM নির্দেশ দেয় কোন টুল কল করতে, তা কল করা হয়:

        ```typescript
        // ২. সার্ভারের টুল কল করুন
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ৩. ফলাফলের সাথে কিছু করুন
        // করার আছে
        ```

1. `run` মেথড আপডেট করুন যাতে LLM কল এবং `callTools` কল থাকে:

    ```typescript

    // ১. এমন বার্তা তৈরি করুন যা LLM-এর ইনপুট হিসেবে ব্যবহৃত হয়
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ২. LLM কল করা হচ্ছে
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ৩. LLM-এর প্রতিক্রিয়া পরীক্ষা করুন, প্রতিটি পছন্দের জন্য যাচাই করুন এটি কিনা টুল কল রয়েছে
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

চমৎকার, সম্পূর্ণ কোডটি দেখি:

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
            type: "function" as const, // টাইপ স্পষ্টভাবে "function" সেট করুন
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
    
    
          // ২। সার্ভারের টুল কল করুন
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // ৩। ফলাফলের সাথে কিছু করুন
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
    
        // ১। LLM উত্তর দেখে প্রতিটি চয়েসের জন্য যাচাই করুন এটি টুল কল আছে কিনা
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

1. LLM কল করার জন্য প্রয়োজনীয় কিছু ইমপোর্ট যুক্ত করি:

    ```python
    # এলএলএম
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. এরপর, LLM কল করার ফাংশনটি যোগ করি:

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
            # ঐচ্ছিক পরামিতি
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

- MCP সার্ভারে পাওয়া ফাংশনগুলো LLM-কে পাঠিয়েছি
- LLM কল করেছি উক্ত ফাংশনসহ
- ফলাফল পরীক্ষা করেছি কোন ফাংশন কল করা প্রয়োজন কিনা
- সেই ফাংশনগুলো কল করার জন্য অ্যারে পাস করেছি

1. শেষ ধাপে মূল কোড আপডেট করি:

    ```python
    prompt = "Add 2 to 20"

    # LLM কে জিজ্ঞাসা করুন কোন কোন টুলস প্রয়োজন, যদি থাকে
    functions_to_call = call_llm(prompt, functions)

    # প্রস্তাবিত ফাংশনগুলি কল করুন
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

এটাই শেষ ধাপ, উপরের কোডে আমরা:

- LLM এর নির্দেশ অনুসারে MCP টুল কল `call_tool` ব্যবহার করে করেছি
- টুল কলের ফলাফল MCP সার্ভারে প্রিন্ট করেছি

#### .NET

1. LLM প্রম্পট অনুরোধের জন্য কিছু কোড দেখাই:

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

- MCP সার্ভার থেকে সরঞ্জাম নিয়েছি, `var tools = await GetMcpTools();`
- একটি ব্যবহারকারী প্রম্পট সংজ্ঞায়িত করেছি `userMessage`
- মডেল এবং টুল নির্দিষ্ট করে অপশন অবজেক্ট তৈরি করেছি
- LLM এর দিকে অনুরোধ প্রেরণ করেছি

1. শেষ ধাপে দেখুন LLM কি ফাংশন কল করা উচিত মনে করে:

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

- ফাংশন কলের তালিকা লুপ করেছি
- প্রতিটি টুল কলের জন্য নাম ও আর্গুমেন্ট পার্স করে MCP ক্লায়েন্ট ব্যবহার করে টুল কল করেছি এবং ফলাফল মুদ্রণ করেছি।

পূর্ণ কোড নিচে:

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
    // প্রাকৃতিক ভাষার অনুরোধগুলি সম্পাদন করুন যা স্বয়ংক্রিয়ভাবে MCP সরঞ্জামগুলি ব্যবহার করে
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

- সরল প্রাকৃতিক ভাষার প্রম্পট ব্যবহার করে MCP সার্ভারের সরঞ্জামগুলোর সঙ্গে ইন্টারঅ্যাক্ট করেছি
- LangChain4j ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে হ্যান্ডেল করে:
  - প্রয়োজন হলে ব্যবহারকারী প্রম্পট থেকে টুল কল রূপান্তর করা
  - LLM সিদ্ধান্ত অনুযায়ী উপযুক্ত MCP সরঞ্জাম কল করা
  - LLM এবং MCP সার্ভারের মধ্যে কথোপকথন প্রবাহ পরিচালনা করা
- `bot.chat()` মেথড প্রাকৃতিক ভাষায় উত্তর প্রদান করে যার মধ্যে MCP সরঞ্জাম ফলে অন্তর্ভুক্ত থাকতে পারে
- এই পদ্ধতি একটি নিরবচ্ছিন্ন ব্যবহারকারীর অভিজ্ঞতা প্রদান করে যেখানে ব্যবহারকারীদের MCP বাস্তবায়ন সম্পর্কে জানতে হয় না

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

এখানেই বেশিরভাগ কাজ ঘটে। আমরা প্রথমে ব্যবহারকারীর প্রারম্ভিক প্রম্পট দিয়ে LLM কল করব, তারপর রেসপন্স প্রক্রিয়া করব দেখে কোন টুল কল করতে হবে কিনা। যদি প্রয়োজন হয়, তখন ওই টুলগুলো কল করব এবং LLM এর সঙ্গে কথোপকথন চালিয়ে যাব যতক্ষণ আর কোনও টুল কলের প্রয়োজন না হয় এবং চূড়ান্ত উত্তর পাই।

আমরা LLM এর কাছে একাধিক কল করব, তাই একটি ফাংশন সংজ্ঞায়িত করি যা LLM কল পরিচালনা করবে। আপনার `main.rs` ফাইলে নিচের ফাংশনটি যুক্ত করুন:

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

এই ফাংশন LLM ক্লায়েন্ট, বার্তার একটি তালিকা (যাতে ব্যবহারকারীর প্রম্পটসহ), MCP সার্ভারের সরঞ্জাম গ্রহণ করে এবং LLM কে অনুরোধ পাঠিয়ে রেসপন্স ফেরত দেয়।
LLM থেকে প্রাপ্ত প্রতিক্রিয়াটি একটি `choices` অ্যারে ধারণ করবে। আমাদের ফলাফল প্রক্রিয়াকরণ করতে হবে দেখার জন্য কোনও `tool_calls` উপস্থিত আছে কিনা। এটি আমাদের জানায় যে LLM একটি নির্দিষ্ট টুল কল করার অনুরোধ করছে যার আর্গুমেন্ট সহ। LLM প্রতিক্রিয়া পরিচালনা করার জন্য একটি ফাংশন সংজ্ঞায়িত করতে আপনার `main.rs` ফাইলের নীচে নিম্নলিখিত কোডটি যুক্ত করুন:

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

    // কনটেন্ট পাওয়া গেলে প্রিন্ট করুন
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // টুল কল গুলো পরিচালনা করুন
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // অ্যাসিস্ট্যান্ট মেসেজ যোগ করুন

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

            // টুল ফলাফল মেসেজে যোগ করুন
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // টুল রেজাল্ট নিয়ে কথোপকথন চালিয়ে যান
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

যদি `tool_calls` উপস্থিত থাকে, এটি টুল তথ্য বের করে, MCP সার্ভারে টুল অনুরোধ পাঠায়, এবং ফলাফলগুলোকে কথোপকথনের মেসেজগুলিতে যোগ করে। তারপর এটি LLM-এর সাথে কথোপকথন চালিয়ে যায় এবং মেসেজগুলি সহকারী প্রতিক্রিয়া ও টুল কলের ফলাফলে আপডেট হয়।

LLM MCP কলের জন্য যা টুল কল তথ্য রিটার্ন করে তা বের করতে, আমরা আরেকটি সহকারী ফাংশন যোগ করব যা কল করার জন্য প্রয়োজনীয় সবকিছু বের করবে। আপনার `main.rs` ফাইলের নীচে নিম্নলিখিত কোডটি যোগ করুন:

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

সব উপাদান স্থাপিত হয়ে গেলে, আমরা এখন প্রাথমিক ব্যবহারকারীর প্রম্পট পরিচালনা করতে এবং LLM কল করতে পারব। আপনার `main` ফাংশনটি নিম্নলিখিত কোডসহ আপডেট করুন:

```rust
// টুল কলগুলির সাথে এলএলএম সংলাপ
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

এই কোডটি প্রাথমিক ব্যবহারকারীর প্রম্পট সহ LLM-কে প্রশ্ন করবে দুইটি সংখ্যার যোগফল চাইতে, এবং এটি টুল কলসমূহ ডাইনামিকালি পরিচালনা করার জন্য প্রতিক্রিয়া প্রক্রিয়া করবে।

দারুণ, আপনি এটি করলেন!

## অ্যাসাইনমেন্ট

ব্যায়াম থেকে কোডটি নিয়ে আরও কিছু টুল যোগ করে সার্ভার তৈরি করুন। তারপর একটি ক্লায়েন্ট তৈরি করুন যার মধ্যে LLM থাকবে, যেমন ব্যায়ামে ছিল, এবং বিভিন্ন প্রম্পট সহ এটি পরীক্ষা করুন যাতে আপনার সমস্ত সার্ভার টুল ডাইনামিকালি কল হচ্ছে কিনা নিশ্চিত হওয়া যায়। ক্লায়েন্ট এইভাবে তৈরি করলে শেষ ব্যবহারকারীর জন্য সুন্দর ইউজার এক্সপেরিয়েন্স হবে কারণ তারা সঠিক ক্লায়েন্ট কমান্ডের পরিবর্তে প্রম্পট ব্যবহার করে কাজ করতে পারবে এবং MCP সার্ভার কল হওয়া নিয়ে সচেতন থাকবেন না।

## সমাধান

[Solution](./solution/README.md)

## প্রধান বিষয়সমূহ

- আপনার ক্লায়েন্টে LLM যোগ করা MCP সার্ভারগুলোর সাথে ব্যবহারকারীদের ইন্টারঅ্যাকশনের উন্নত উপায় প্রদান করে।
- আপনাকে MCP সার্ভার প্রতিক্রিয়াটি এমন কিছুতে রূপান্তর করতে হবে যা LLM বুঝতে পারে।

## উদাহরণসমূহ

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
এই ডকুমেন্টটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যেহেতু আমরা সঠিকতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে। মূল ডকুমেন্টটি তার নিজস্ব ভাষায় কর্তৃত্বপূর্ণ উৎস হিসাবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারের ফলে সৃষ্ট কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী হই না।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->