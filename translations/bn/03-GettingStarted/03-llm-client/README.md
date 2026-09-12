# LLM সহ একটি ক্লায়েন্ট তৈরি করা

> [!NOTE]
> জাভা ক্লায়েন্ট উদাহরণগুলি লিগ্যাসি HTTP+SSE পরিবহন মাধ্যমে সংযুক্ত হয় এবং
> MCP `2025-11-25` SDK API লক্ষ্য করে। নতুন রিমোট ক্লায়েন্টের জন্য `2026-07-28`-সঙ্গত SDK এবং
> স্ট্রিমেবল HTTP ব্যবহার করুন।

এখন পর্যন্ত, আপনি কিভাবে একটি সার্ভার এবং একটি ক্লায়েন্ট তৈরি করতে হয় তা দেখেছেন। ক্লায়েন্ট প্রদর্শিতভাবে সার্ভারকে কল করতে পেরেছে তার টুলস, রিসোর্স এবং প্রম্পটগুলি তালিকাভুক্ত করার জন্য। তবে, এটি খুবই ব্যবহারিক পদ্ধতি নয়। আপনার ব্যবহারকারীরা এজেন্টিক যুগে বাস করেন এবং তারা প্রম্পট ব্যবহার এবং একটি LLM-এর সাথে যোগাযোগের প্রত্যাশা করেন। তারা MCP ব্যবহার করে আপনার সক্ষমতাগুলি সংরক্ষণ করছেন কিনা তা নিয়ে সুন্দর করেন না; তারা শুধুমাত্র প্রাকৃতিক ভাষা ব্যবহার করে যোগাযোগ করার আশা করেন। তাহলে আমরা কিভাবে এটি সমাধান করব? সমাধান হল ক্লায়েন্টে একটি LLM যোগ করা।

## ওভারভিউ

এই পাঠে আমরা আমাদের ক্লায়েন্টে একটি LLM যোগ করার উপর ফোকাস করব এবং দেখাব কিভাবে এটি আপনার ব্যবহারকারীর জন্য অনেক ভাল অভিজ্ঞতা প্রদান করে।

## শেখার উদ্দেশ্য

এই পাঠ শেষ করার পরে, আপনি সক্ষম হবেন:

- একটি LLM সহ একটি ক্লায়েন্ট তৈরি করতে।
- একটি LLM ব্যবহার করে নিরবচ্ছিন্নভাবে একটি MCP সার্ভারের সাথে যোগাযোগ করতে।
- ক্লায়েন্ট পার্শ্বে একটি ভাল এন্ড ইউজার অভিজ্ঞতা প্রদান করতে।

## পদ্ধতি

চলুন আমরা বুঝতে চেষ্টা করি আমাদের কিভাবে এগোতে হবে। একটি LLM যোগ করা সহজ শোনায়, তবে আমরা কি সত্যিই এটি করব?

এখানে কিভাবে ক্লায়েন্ট সার্ভারের সাথে যোগাযোগ করবে:

1. সার্ভারের সাথে সংযোগ স্থাপন করুন।

1. সক্ষমতা, প্রম্পট, রিসোর্স এবং টুলগুলি তালিকাভুক্ত করুন এবং তাদের স্কিমা সংরক্ষণ করুন।

1. একটি LLM যোগ করুন এবং সংরক্ষিত সক্ষমতা এবং তাদের স্কিমা এমন ফরম্যাটে পাস করুন যা LLM বুঝতে পারে।

1. ব্যবহারকারীর প্রম্পট হ্যান্ডেল করুন, এটি LLM-এ পাস করুন ক্লায়েন্ট দ্বারা তালিকাভুক্ত টুলগুলির সাথে।

চমৎকার, এখন আমরা বুঝতে পারলাম উচ্চ স্তরে আমরা কিভাবে এটি করতে পারি, আসুন নিচের অনুশীলনে এটি চেষ্টা করি।

## অনুশীলন: একটি LLM সহ ক্লায়েন্ট তৈরি করা

এই অনুশীলনে, আমরা শিখব কিভাবে একটি LLM আমাদের ক্লায়েন্টে যোগ করতে হয়।

### GitHub পার্সোনাল অ্যাক্সেস টোকেন ব্যবহার করে প্রমাণীকরণ

একটি GitHub টোকেন তৈরি করা সরল প্রক্রিয়া। এখানে কিভাবে করবেন:

- GitHub সেটিংসে যান – উপরের ডান কোণায় আপনার প্রোফাইল ছবিতে ক্লিক করুন এবং সেটিংস নির্বাচন করুন।
- ডেভেলপার সেটিংসে যান – নিচে স্ক্রোল করুন এবং ডেভেলপার সেটিংস ক্লিক করুন।
- পার্সোনাল অ্যাক্সেস টোকেন নির্বাচন করুন – ফাইন-গ্রেইনড টোকেন ক্লিক করুন এবং তারপর নতুন টোকেন তৈরি করুন।
- আপনার টোকেন কনফিগার করুন – রেফারেন্সের জন্য একটি নোট যোগ করুন, একটি শেষ তারিখ সেট করুন এবং প্রয়োজনীয় স্কোপ (অনুমতি) নির্বাচন করুন। এই ক্ষেত্রে Models অনুমতি অবশ্যই যোগ করুন।
- টোকেন তৈরি করুন এবং কপি করুন – Generate token ক্লিক করুন, এবং এটি তাত্ক্ষণিক কপি করতে ভুলবেন না, কারণ এটি পুনরায় দেখতে পারবেন না।

### -1- সার্ভারের সাথে সংযোগ করুন

আসুন প্রথমে আমাদের ক্লায়েন্ট তৈরি করি:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // স্কিমা যাচাইয়ের জন্য zod ইমপোর্ট করুন

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

পূর্ববর্তী কোডে আমরা:

- প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করেছি
- একটি ক্লাস তৈরি করেছি যার দুটি সদস্য, `client` এবং `openai` যারা আমাদের ক্লায়েন্ট পরিচালনা এবং LLM-এ যোগাযোগ করতে সাহায্য করবে।
- আমাদের LLM ইনস্ট্যান্স কনফিগার করেছি GitHub মডেল ব্যবহার করার জন্য `baseUrl` সেট করে যা ইনফারেন্স API নির্দেশ করে।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio সংযোগের জন্য সার্ভার প্যারামিটার তৈরি করুন
server_params = StdioServerParameters(
    command="mcp",  # নির্বাহযোগ্য
    args=["run", "server.py"],  # ঐচ্ছিক কমান্ড লাইন আর্গুমেন্ট
    env=None,  # ঐচ্ছিক পরিবেশ পরিবর্তনশীল
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

পূর্ববর্তী কোডে আমরা:

- MCP এর জন্য প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করেছি
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

প্রথমে, আপনাকে আপনার `pom.xml` ফাইলে LangChain4j নির্ভরশীলতা যোগ করতে হবে। MCP ইন্টিগ্রেশন এবং OpenAI-সঙ্গত MiniMax API সক্ষম করতে এই নির্ভরশীলতাগুলি যোগ করুন:

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

আপনার MiniMax API কী এবং প্রয়োজনে এন্ডপয়েন্ট এবং মডেল সেট করুন।
`MINIMAX_MODEL_ID` `MiniMax-M3` এবং `MiniMax-M2.7` সমর্থন করে। যদি
`OPENAI_BASE_URL` সেট না থাকে, `MINIMAX_REGION` `global_en` এবং `cn_zh` সমর্থন করে।

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

পরিবর্তে অঞ্চল দ্বারা এন্ডপয়েন্ট নির্বাচন করতে, `OPENAI_BASE_URL` বাদ দিন:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

তারপর আপনার জাভা ক্লায়েন্ট ক্লাস তৈরি করুন:

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

পূর্ববর্তী কোডে আমরা:

- **LangChain4j নির্ভরশীলতা যোগ করেছি**: MCP ইন্টিগ্রেশন এবং OpenAI-সঙ্গত MiniMax API এর জন্য প্রয়োজনীয়
- **LangChain4j লাইব্রেরি ইমপোর্ট করেছি**: MCP ইন্টিগ্রেশন এবং OpenAI চ্যাট মডেল কার্যকারিতার জন্য
- **একটি `ChatLanguageModel` তৈরি করেছি**: MiniMax ব্যবহার করে কনফিগার করা আপনার MiniMax API কী, এন্ডপয়েন্ট এবং সমর্থিত মডেল আইডি সহ
- **HTTP পরিবহন সেটআপ করেছি**: সার্ভার-সেন্ট ইভেন্টস (SSE) ব্যবহার করে MCP সার্ভারের সাথে সংযোগের জন্য
- **একটি MCP ক্লায়েন্ট তৈরি করেছি**: যা সার্ভারের সাথে যোগাযোগ হ্যান্ডেল করবে
- **LangChain4j এর অন্তর্নির্মিত MCP সমর্থন ব্যবহার করেছি**: যা LLM এবং MCP সার্ভারের মধ্যে ইন্টিগ্রেশন সহজ করে তোলে

#### Rust

এই উদাহরণটি ধরে নেয় যে আপনার কাছে একটি Rust ভিত্তিক MCP সার্ভার চলছে। যদি থাকে না, [01-first-server](../01-first-server/README.md) পাঠে ফিরে যান সার্ভার তৈরি করার জন্য।

একবার আপনার Rust MCP সার্ভার থাকলে, একটি টার্মিনাল খুলুন এবং সার্ভারের একই ডিরেক্টরিতে যান। তারপর নিম্নলিখিত কমান্ড রান করুন একটি নতুন LLM ক্লায়েন্ট প্রজেক্ট তৈরি করতে:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

আপনার `Cargo.toml` ফাইলে নিম্নলিখিত নির্ভরশীলতাগুলি যোগ করুন:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI-এর জন্য একটি অফিসিয়াল Rust লাইব্রেরি নেই, তবে `async-openai` ক্রেট একটি [কমিউনিটি পরিচালিত লাইব্রেরি](https://platform.openai.com/docs/libraries/rust#rust) যা সাধারণত ব্যবহৃত হয়।

`src/main.rs` ফাইলটি খুলুন এবং এর বিষয়বস্তু নিম্নলিখিত কোড দ্বারা প্রতিস্থাপন করুন:

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

    // TODO: MCP টুল তালিকা সংগ্রহ করুন

    // TODO: টুল কল সহ LLM কথোপকথন

    Ok(())
}
```

এই কোড একটি বেসিক Rust অ্যাপ্লিকেশন সেটআপ করে যা MCP সার্ভার এবং GitHub মডেলগুলির সাথে LLM ইন্টারঅ্যাকশনের জন্য সংযুক্ত হবে।

> [!IMPORTANT]
> অ্যাপ্লিকেশন চালানোর আগে আপনার GitHub টোকেন সহ `OPENAI_API_KEY` পরিবেশ পরিবর্তনশীল সেট করার কথা ভুলবেন না।

চমৎকার, আমাদের পরবর্তী ধাপে, আসুন সার্ভারের সক্ষমতাগুলি তালিকাভুক্ত করি।

### -2- সার্ভারের সক্ষমতা তালিকাভুক্ত করুন

এখন আমরা সার্ভারের সাথে সংযোগ করব এবং এর সক্ষমতাগুলি জিজ্ঞেস করব:

#### টাইপস্ক্রিপ্ট

একই ক্লাসে নিম্নলিখিত মেথডগুলি যোগ করুন:

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

পূর্ববর্তী কোডে আমরা:

- সার্ভারের সাথে সংযোগ করার কোড যোগ করেছি, `connectToServer`।
- একটি `run` মেথড তৈরি করেছি যা আমাদের অ্যাপ ফ্লো হ্যান্ডল করবে। আপাতত এটি শুধুমাত্র টুলগুলিকে তালিকাভুক্ত করে, তবে আমরা শীঘ্রই আরো যোগ করব।

#### পাইথন

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

- রিসোর্স এবং টুলগুলি তালিকাভুক্ত করেছি এবং মুদ্রণ করেছি। টুলগুলির জন্য আমরা `inputSchema` ও তালিকাভুক্ত করেছি যা পরে ব্যবহার করব।

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


পূর্ববর্তী কোডে আমরা:

- MCP সার্ভারে উপলব্ধ সরঞ্জামগুলি তালিকাভুক্ত করেছি
- প্রতিটি সরঞ্জামের জন্য, নাম, বর্ণনা এবং এর স্কীমা তালিকাভুক্ত করেছি। পরের অংশে আমরা এই স্কীমাকে সরঞ্জামগুলি কল করার জন্য ব্যবহার করব।

#### Java

```java
// একটি টুল প্রদানকারী তৈরি করুন যা স্বয়ংক্রিয়ভাবে MCP টুলগুলি আবিষ্কার করে
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP টুল প্রদানকারী স্বয়ংক্রিয়ভাবে পরিচালনা করে:
// - MCP সার্ভার থেকে উপলব্ধ টুলের তালিকা তৈরি করা
// - MCP টুল স্কিমাগুলি LangChain4j ফরম্যাটে রূপান্তর করা
// - টুল কার্যকরকরণ এবং প্রতিক্রিয়া পরিচালনা করা
```

পূর্ববর্তী কোডে আমরা:

- একটি `McpToolProvider` তৈরি করেছি যা স্বয়ংক্রিয়ভাবে MCP সার্ভার থেকে সব সরঞ্জাম আবিষ্কার এবং নিবন্ধন করে
- টুল প্রোভাইডার MCP সরঞ্জাম স্কীমাগুলির মধ্যে এবং LangChain4j এর সরঞ্জাম ফরম্যাটের মধ্যে রূপান্তর অভ্যন্তরীণভাবে পরিচালনা করে
- এই পদ্ধতি ম্যানুয়াল সরঞ্জাম তালিকা এবং রূপান্তর প্রক্রিয়া থেকে মুক্তি দেয়

#### Rust

MCP সার্ভার থেকে সরঞ্জামগুলি আনার জন্য `list_tools` পদ্ধতি ব্যবহার করা হয়। আপনার `main` ফাংশনে MCP ক্লায়েন্ট সেটআপ করার পরে নিম্নলিখিত কোড যোগ করুন:

```rust
// MCP টুল তালিকা পান
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- সার্ভার ক্ষমতাগুলিকে LLM সরঞ্জামে রূপান্তর করা

সার্ভারের ক্ষমতা তালিকা করার পরের ধাপ হলো সেগুলো এমন ফরম্যাটে রূপান্তর করা যা LLM বুঝতে পারে। একবার আমরা এটা করলে, আমরা এই ক্ষমতাগুলোকে আমাদের LLM এর জন্য সরঞ্জাম হিসেবে সরবরাহ করতে পারব।

#### TypeScript

1. MCP সার্ভারের উত্তরকে LLM ব্যবহার করতে পারবে এমন সরঞ্জামের ফরম্যাটে রূপান্তর করতে নিম্নলিখিত কোড যোগ করুন:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ইনপুট_স্কিমা ভিত্তিক একটি জড স্কিমা তৈরি করুন
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // স্পষ্টভাবে টাইপটি "function" সেট করুন
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

    উপরের কোডটি MCP সার্ভারের একটি উত্তর নিয়ে সেটিকে LLM বুঝতে পারার মত একটি সরঞ্জাম সংজ্ঞায় রূপান্তর করে।

2. পরবর্তী ধাপে `run` মেথড আপডেট করি যা সার্ভারের ক্ষমতাগুলো তালিকা করে:

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

    পূর্ববর্তী কোডে, আমরা `run` পদ্ধতিটি আপডেট করেছি যাতে রেজাল্টের মধ্য দিয়ে ম্যাপ করে প্রতিটি এন্ট্রি জন্য `openAiToolAdapter` কল করা হয়।

#### Python

1. প্রথমে, নিম্নলিখিত রূপান্তরক ফাংশন তৈরি করি:

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

    উপরের `convert_to_llm_tools` ফাংশনে, আমরা MCP একটি টুলের প্রতিক্রিয়া নিয়ে সেটিকে LLM বুঝতে পারার ফরম্যাটে রূপান্তর করি।

2. এরপর, আমাদের ক্লায়েন্ট কোড আপডেট করি যাতে এটি এই ফাংশনটি ব্যবহার করে:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    এখানে, আমরা `convert_to_llm_tool` কল যোগ করছি যাতে MCP সরঞ্জামের প্রতিক্রিয়াকে এমন কিছুতে রূপান্তর করা যায় যা আমরা পরে LLM-এ দিতে পারি।

#### .NET

1. MCP সরঞ্জামের প্রতিক্রিয়াকে LLM বুঝতে পারার মত কিছুতে রূপান্তর করার কোড যোগ করি:

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

পূর্ববর্তী কোডে আমরা:

- একটি `ConvertFrom` ফাংশন তৈরি করেছি যা নাম, বর্ণনা এবং ইনপুট স্কীমা নেয়।
- এমন কার্যকারিতা সংজ্ঞায়িত করেছি যা একটি FunctionDefinition তৈরি করে যা পরবর্তীতে ChatCompletionsDefinition এ প্রেরণ করা হয়। এটি LLM বুঝতে পারে।

2. চলুন দেখি কীভাবে আমরা বিদ্যমান কোড কিছু আপডেট করতে পারি যাতে উপরের ফাংশনের সুবিধা নিতে পারি:

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
// প্রাকৃতিক ভাষা সংলাপের জন্য একটি বট ইন্টারফেস তৈরি করুন
public interface Bot {
    String chat(String prompt);
}

// LLM এবং MCP টুল সহ AI পরিষেবা কনফিগার করুন
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

পূর্ববর্তী কোডে আমরা:

- সহজ একটি `Bot` ইন্টারফেস সংজ্ঞায়িত করেছি প্রাকৃতিক ভাষা কথোপকথনের জন্য
- LangChain4j এর `AiServices` ব্যবহার করেছি যার মাধ্যমে স্বয়ংক্রিয়ভাবে LLM MCP টুল প্রোভাইডারের সাথে যুক্ত হয়
- ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে টুল স্কীমা রূপান্তর এবং ফাংশন কলিং আড়ালে পরিচালনা করে
- এই পদ্ধতিতে, ম্যানুয়াল সরঞ্জাম রূপান্তর প্রয়োজন হয় না - LangChain4j সব MCP সরঞ্জামকে LLM-সঙ্গত ফরম্যাটে রূপান্তর করার জটিলতা সামলে নেয়

#### Rust

MCP সরঞ্জামের প্রতিক্রিয়াকে এমন ফরম্যাটে রূপান্তর করতে যা LLM বুঝতে পারে, আমরা একটি হেল্পার ফাংশন যোগ করব যা সরঞ্জামের তালিকাকে ফরম্যাট করে। এটি `main.rs` ফাইলে `main` ফাংশনের নিচে যোগ করুন। এটি LLM এ রিকোয়েস্ট করার সময় কল করা হবে:

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

অসাধারণ, এখন আমরা ব্যবহারকারীর রিকোয়েস্ট পরিচালনা করার জন্য প্রস্তুত, তাই পরের অংশ দেখা যাক।

### -4- ব্যবহারকারীর প্রম্পট রিকোয়েস্ট পরিচালনা করা

এই কোড অংশে, আমরা ব্যবহারকারীর রিকোয়েস্টগুলো পরিচালনা করব।

#### TypeScript

1. একটি মেথড যোগ করুন যা আমাদের LLM কল করতে ব্যবহৃত হবে:

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
        // TODO

        }
    }
    ```

    পূর্ববর্তী কোডে আমরা:

    - `callTools` নামের মেথড যোগ করেছি।
    - মেথডটি একটি LLM প্রতিক্রিয়া নেয় এবং দেখে কোন সরঞ্জামগুলি কল হয়েছে, থাকলে:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // কল টুল
        }
        ```

    - সরঞ্জাম কল করে, যদি LLM ইঙ্গিত করে যে কল করা উচিত:

        ```typescript
        // ২. সার্ভারের টুল কল করুন
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ৩. ফলাফল দিয়ে কিছু করুন
        // TODO
        ```

2. `run` পদ্ধতি আপডেট করুন যাতে LLM কল এবং `callTools` কল অন্তর্ভুক্ত থাকে:

    ```typescript

    // ১. LLM এর ইনপুট হিসেবে মেসেজ তৈরি করা
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ২. LLM কল করা
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ৩. LLM এর উত্তর পরীক্ষা করা, প্রতিটি অপশনের জন্য চেক করুন এটি টুল কল রয়েছে কিনা
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

অসাধারণ, পুরো কোড তালিকাভুক্ত করি:

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
          // ইনপুট_স্কিমার ভিত্তিতে একটি zod স্কিমা তৈরি করুন
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
          // করার আছে
    
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
    
        // ৩. LLM প্রতিক্রিয়াটি দেখুন, প্রতিটি বিকল্পের জন্য চেক করুন এটি টুল কল আছে কিনা
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

1. LLM কল করার জন্য প্রয়োজনীয় কিছু ইম্পোর্ট যোগ করি

    ```python
    # এলএলএম
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. এরপর, LLM কল করার ফাংশন যোগ করি:

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

    পূর্ববর্তী কোডে আমরা:

    - MCP সার্ভারে পাওয়া এবং রূপান্তরित আমাদের ফাংশনগুলো LLM-এ পাস করেছি।
    - তারপর ঐ ফাংশনগুলো ব্যবহার করে LLM কল করেছি।
    - এরপর আমরা ফলাফল পরীক্ষা করছি কোন ফাংশন কল করা উচিত কিনা।
    - সর্বশেষে কল করার জন্য ফাংশনগুলোর একটি অ্যারে পাস করছি।

3. চূড়ান্ত ধাপ, আমাদের প্রধান কোড আপডেট করি:

    ```python
    prompt = "Add 2 to 20"

    # LLM-কে জিজ্ঞাসা করুন কোন সরঞ্জামগুলি উপলব্ধ, যদি থাকে
    functions_to_call = call_llm(prompt, functions)

    # প্রস্তাবিত ফাংশনগুলি কল করুন
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ঠিক আছে, উপরের কোড ছিল চূড়ান্ত ধাপ:

    - `call_tool` ব্যবহার করে একটি MCP টুল কল করা হয়েছে একটি ফাংশন দিয়ে যা LLM আমাদের প্রম্পটের ভিত্তিতে কল করতে বলেছে।
    - MCP সার্ভারের টুল কলের ফলাফল প্রিন্ট করা হয়েছে।

#### .NET

1. আসুন দেখাই কীভাবে LLM প্রম্পট রিকোয়েস্ট করা যায়:

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

    পূর্ববর্তী কোডে আমরা:

    - MCP সার্ভার থেকে সরঞ্জামগুলো এনেছি, `var tools = await GetMcpTools()`।
    - একটি ব্যবহারকারীর প্রম্পট `userMessage` নির্ধারণ করেছি।
    - একটি অপশনস অবজেক্ট তৈরি করেছি যা মডেল এবং সরঞ্জাম নির্দিষ্ট করে।
    - LLM এর প্রতি একটি রিকোয়েস্ট করেছি।

2. শেষ ধাপ, দেখি LLM কি মনে করে আমাদের একটি ফাংশন কল করা উচিত:

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

    পূর্ববর্তী কোডে আমরা:

    - ফাংশন কলগুলোর একটি তালিকা লুপ করেছি।
    - প্রতিটি টুল কলের জন্য, নাম এবং আর্গুমেন্ট পার্স করে MCP ক্লায়েন্ট ব্যবহার করে MCP সার্ভারে টুল কল করেছি। শেষে ফলাফলগুলো প্রিন্ট করেছি।

এখানে সম্পূর্ণ কোড:

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
    // স্বয়ংক্রিয়ভাবে MCP টুলস ব্যবহার করে প্রাকৃতিক ভাষার অনুরোধগুলি বাস্তবায়ন করুন
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

পূর্ববর্তী কোডে আমরা:

- MCP সার্ভারের সরঞ্জামগুলোর সাথে সহজ প্রাকৃতিক ভাষার প্রম্পট ব্যবহার করেছি
- LangChain4j ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে পরিচালনা করে:
  - প্রয়োজন হলে ব্যবহারকারীর প্রম্পটগুলো সরঞ্জাম কল এ রূপান্তর করা
  - LLM এর সিদ্ধান্ত অনুযায়ী উপযুক্ত MCP সরঞ্জামগুলি কল করা
  - LLM এবং MCP সার্ভারের মধ্যে কথোপকথনের প্রবাহ চালানো
- `bot.chat()` পদ্ধতি প্রাকৃতিক ভাষা প্রতিক্রিয়া ফেরত দেয় যা MCP টুল এক্সিকিউশনের ফলাফল অন্তর্ভুক্ত করতে পারে
- এই পদ্ধতি ব্যবহারকারীর জন্য একটি সুনির্মিত অভিজ্ঞতা প্রদান করে যেখানে তাদের MCP ইমপ্লিমেন্টেশন সম্পর্কে জানতে হয় না

সম্পূর্ণ কোড উদাহরণ:

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


এখানে প্রধানত কাজের বৃহত্তর অংশ ঘটে। আমরা প্রাথমিক ব্যবহারকারীর প্রম্পট সহ LLM-কে কল করব, তারপরে প্রতিক্রিয়া প্রক্রিয়া করব দেখতে যে কোন টুল কল করতে হবে কিনা। যদি করা প্রয়োজন, আমরা সেই টুলগুলি কল করব এবং LLM এর সাথে আলাপচারিতা চালিয়ে যাব যতক্ষণ আর কোনো টুল কলের প্রয়োজন না হয় এবং আমাদের একটি চূড়ান্ত প্রতিক্রিয়া থাকে।

আমরা LLM-কে একাধিকবার কল করব, তাই আসুন একটি ফাংশন সংজ্ঞায়িত করি যা LLM কল পরিচালনা করবে। আপনার `main.rs` ফাইলে নিম্নলিখিত ফাংশনটি যুক্ত করুন:

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

এই ফাংশনটি LLM ক্লায়েন্ট, একটি বার্তার তালিকা (ব্যবহারকারীর প্রম্পট সহ), MCP সার্ভার থেকে টুলগুলি গ্রহণ করে, এবং LLM-কে একটি অনুরোধ পাঠায়, তারপর প্রতিক্রিয়া ফেরত দেয়।

LLM থেকে আসা প্রতিক্রিয়ায় `choices` নামক একটি অ্যারে থাকে। আমাদের ফলাফল প্রক্রিয়া করতে হবে দেখতে যদি কোনো `tool_calls` উপস্থিত থাকে। এটি আমাদের জানায় যে LLM একটি নির্দিষ্ট টুল কল করার জন্য আর্গুমেন্ট সহ অনুরোধ করছে। আপনার `main.rs` ফাইলের নিচে নিম্নলিখিত কোডটি যোগ করুন একটি ফাংশন সংজ্ঞায়িত করতে যা LLM প্রতিক্রিয়া পরিচালনা করবে:

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

    // যদি উপলব্ধ থাকে תוכן মুদ্রণ করুন
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

            // বার্তাগুলিতে টুলের ফলাফল যোগ করুন
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

যদি `tool_calls` থাকে, এটি টুলের তথ্য বের করে, টুল অনুরোধ সহ MCP সার্ভারকে কল করে, এবং ফলাফলগুলো আলাপচারিতার বার্তাগুলিতে যোগ করে। তারপরে এটি LLM এর সাথে আলাপচারিতা চালিয়ে যায় এবং বার্তাগুলি সহকারী প্রতিক্রিয়া এবং টুল কল ফলাফল দিয়ে আপডেট হয়।

MCP কল করার জন্য LLM যে টুল কল তথ্য ফেরত দেয় তা বের করতে, আমরা আরেকটি সহায়ক ফাংশন যোগ করবো যা কল করার জন্য প্রয়োজনীয় সবকিছু বের করবে। আপনার `main.rs` ফাইলের নিচে নিম্নলিখিত কোডটি যুক্ত করুন:

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

সব অংশ ঠিকঠাক থাকায়, এখন আমরা প্রাথমিক ব্যবহারকারীর প্রম্পট পরিচালনা করতে এবং LLM কল করতে পারবো। আপনার `main` ফাংশন আপডেট করুন নিম্নলিখিত কোড সহ:

```rust
// টুল কল সহ LLM আলাপচারিতা
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

এটি LLM কে প্রাথমিক ব্যবহারকারীর প্রম্পট দিয়ে দুইটি সংখ্যার যোগফল জিজ্ঞাসা করবে, এবং প্রতিক্রিয়া প্রক্রিয়া করবে টুল কলগুলো গতিশীলভাবে পরিচালনা করার জন্য।

দারুণ, আপনি সফল হয়েছেন!

## কাজ

অনুশীলনের কোড থেকে নিয়ে সার্ভারটিকে আরও কিছু টুল দিয়ে তৈরি করুন। তারপর একটি ক্লায়েন্ট তৈরি করুন LLM সহ, অনুশীলনের মতো, এবং বিভিন্ন প্রম্পট দিয়ে পরীক্ষা করুন যাতে আপনার সমস্ত সার্ভার টুল গতিশীলভাবে কল হয়। ক্লায়েন্ট তৈরির এই পদ্ধতিতে শেষ ব্যবহারকারী একটি দুর্দান্ত ব্যবহারকারী অভিজ্ঞতা পাবে কারণ তারা সঠিক ক্লায়েন্ট কমান্ডের পরিবর্তে প্রম্পট ব্যবহার করতে পারবে এবং MCP সার্ভার কল হওয়ার ব্যাপারে অচেতন থাকবে।

## সমাধান

[সমাধান](./solution/README.md)

## মূল টেকঅ্যাওয়ে

- আপনার ক্লায়েন্টে LLM যোগ করা ব্যবহারকারীদের MCP সার্ভারগুলোর সাথে আরও ভালোভাবে যোগাযোগ করার উপায় দেয়।
- MCP সার্ভার প্রতিক্রিয়াটি এমন কিছুতে রূপান্তর করতে হবে যা LLM বুঝতে পারে।

## নমুনা

- [জাভা ক্যালকুলেটর](../samples/java/calculator/README.md)
- [.Net ক্যালকুলেটর](../../../../03-GettingStarted/samples/csharp)
- [জাভাস্ক্রিপ্ট ক্যালকুলেটর](../samples/javascript/README.md)
- [টাইপস্ক্রিপ্ট ক্যালকুলেটর](../samples/typescript/README.md)
- [পাইথন ক্যালকুলেটর](../../../../03-GettingStarted/samples/python)
- [রাস্ট ক্যালকুলেটর](../../../../03-GettingStarted/samples/rust)

## অতিরিক্ত সম্পদ

## পরবর্তী ধাপ

- পরবর্তী: [Visual Studio Code ব্যবহার করে একটি সার্ভার ব্যবহার করা](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->