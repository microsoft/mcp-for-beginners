# LLM সহ ক্লায়েন্ট তৈরি করা

এখন পর্যন্ত, আপনি দেখেছেন কীভাবে একটি সার্ভার এবং একটি ক্লায়েন্ট তৈরি করা যায়। ক্লায়েন্ট সার্ভারকে স্পষ্টভাবে কল করতে পেরেছে তার টুলস, রিসোর্স এবং প্রম্পটগুলো তালিকা করার জন্য। তবে, এটি খুব কার্যকরী পদ্ধতি নয়। আপনার ব্যবহারকারীরা এজেন্টিক যুগে বাস করে এবং তারা প্রম্পট ব্যবহার এবং একটি LLM-এর সাথে যোগাযোগ করার প্রত্যাশা করে। তারা MCP ব্যবহার করে আপনার সক্ষমতাগুলো সংরক্ষণ করছেন কি না তা নিয়ে যত্ন করেন না; তারা কেবল প্রাকৃতিক ভাষা ব্যবহার করে যোগাযোগ করতে চায়। তাহলে আমরা এটা কীভাবে সমাধান করব? সমাধান হচ্ছে ক্লায়েন্টে একটি LLM যোগ করা।

## সারসংক্ষেপ

এই পাঠে আমরা আপনার ক্লায়েন্টে একটি LLM যোগ করার উপর মনোনিবেশ করব এবং দেখাব কীভাবে এটি আপনার ব্যবহারকারীর জন্য অনেক উন্নত অভিজ্ঞতা প্রদান করে।

## শেখার উদ্দেশ্য

এই পাঠের শেষে আপনি সক্ষম হবেন:

- একটি LLM সহ ক্লায়েন্ট তৈরি করতে।
- একটি MCP সার্ভারের সাথে একটি LLM ব্যবহার করে বাধাহীনভাবে যোগাযোগ করতে।
- ক্লায়েন্ট পাশে একটি ভালো শেষ ব্যবহারকারী অভিজ্ঞতা প্রদান করতে।

## পদ্ধতি

আসুন আমরা বুঝে নিই আমাদের যে পদ্ধতি নিতে হবে। একটি LLM যোগ করা সহজ শোনালেও, আমরা কি সত্যিই এটি করব?

এখানে দেখানো হলো ক্লায়েন্ট সার্ভারের সাথে কীভাবে যোগাযোগ করবে:

1. সার্ভারের সাথে সংযোগ স্থাপন করুন।

1. সক্ষমতা, প্রম্পট, রিসোর্স এবং টুলস তালিকা করুন এবং তাদের স্কিমা সংরক্ষণ করুন।

1. একটি LLM যোগ করুন এবং সংরক্ষিত সক্ষমতা ও তাদের স্কিমা LLM বোঝার ফরম্যাটে পাস করুন।

1. একটি ব্যবহারকারী প্রম্পট হ্যান্ডেল করুন, ক্লায়েন্ট দ্বারা তালিকাভুক্ত টুলসের সাথে এটি LLM-এ পাস করে।

দুর্দান্ত, এখন আমরা বুঝেছি আমরা এই কাজটি উচ্চ পর্যায়ে কীভাবে করব, আসুন নিচের অনুশীলনে এটি চেষ্টা করি।

## অনুশীলন: LLM সহ ক্লায়েন্ট তৈরি

এই অনুশীলনে, আমরা আমাদের ক্লায়েন্টে একটি LLM যোগ করতে শিখব।

### গিটহাব পার্সোনাল এক্সেস টোকেন ব্যবহার করে প্রমাণীকরণ

একটি গিটহাব টোকেন তৈরি করা একটি সরল প্রক্রিয়া। এখানে আপনি কীভাবে এটি করতে পারেন:

- গিটহাব সেটিংসে যান – ডান উপরের কর্নারে আপনার প্রোফাইল ছবিতে ক্লিক করুন এবং Settings নির্বাচন করুন।
- ডেভেলপার সেটিংসে যান – নিচে স্ক্রোল করুন এবং Developer Settings-এ ক্লিক করুন।
- পার্সোনাল এক্সেস টোকেন্স নির্বাচন করুন – Fine-grained tokens-এ ক্লিক করুন এবং তারপর Generate new token বেছে নিন।
- আপনার টোকেন কনফিগার করুন – রেফারেন্সের জন্য একটি নোট যোগ করুন, মেয়াদ নির্ধারণ করুন, এবং প্রয়োজনীয় স্কোপ (অনুমতি) নির্বাচন করুন। এই ক্ষেত্রে Models অনুমতি যোগ করতে ভুলবেন না।
- টোকেন তৈরি করুন এবং কপি করুন – Generate token-এ ক্লিক করুন এবং সঙ্গে সঙ্গেই এটি কপি করুন, কারণ আপনি এটি আর দেখতে পারবেন না।

### -1- সার্ভারের সাথে সংযোগ স্থাপন করুন

চলুন প্রথমে আমাদের ক্লায়েন্ট তৈরি করি:

#### টাইপস্ক্রিপ্ট

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

পূর্বের কোডে আমরা:

- প্রয়োজনীয় লাইব্রেরি আমদানি করেছি
- একটি ক্লাস তৈরি করেছি যার দুইটি সদস্য, `client` এবং `openai`, যা যথাক্রমে ক্লায়েন্ট পরিচালনা এবং LLM-এ যোগাযোগে সাহায্য করবে।
- আমাদের LLM ইনস্ট্যান্স কনফিগার করেছি GitHub Models ব্যবহার করার জন্য `baseUrl` inference API-র দিকে নির্দেশ করে।

#### পাইথন

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# স্টডিও সংযোগের জন্য সার্ভার প্যারামিটার তৈরি করুন
server_params = StdioServerParameters(
    command="mcp",  # নির্বাহযোগ্য
    args=["run", "server.py"],  # ঐচ্ছিক কমান্ড লাইন আর্গুমেন্ট
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

পূর্বের কোডে আমরা:

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

#### জাভা

প্রথমে, আপনাকে আপনার `pom.xml` ফাইলে LangChain4j ডিপেন্ডেন্সিগুলো যোগ করতে হবে। MCP ইন্টিগ্রেশন এবং OpenAI-সহযোগী MiniMax API সক্ষম করতে এই ডিপেন্ডেন্সিগুলো যোগ করুন:

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

আপনার MiniMax API কী সেট করুন এবং ইচ্ছাকৃতভাবে শেষ বিন্দু ও মডেল নির্ধারণ করুন।
`MINIMAX_MODEL_ID` সমর্থন করে `MiniMax-M3` এবং `MiniMax-M2.7`। যদি
`OPENAI_BASE_URL` নির্ধারণ না করা থাকে, `MINIMAX_REGION` সমর্থন করে `global_en` এবং `cn_zh`।

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

পরিবর্তে, অঞ্চল দ্বারা শেষ বিন্দু নির্বাচন করতে চাইলে `OPENAI_BASE_URL` বাদ দিন:

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

        // সার্ভারের সাথে সংযোগ করার জন্য MCP পরিবহন তৈরি করুন
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

পূর্বের কোডে আমরা:

- **LangChain4j ডিপেন্ডেন্সি যুক্ত করেছি**: MCP ইন্টিগ্রেশন এবং OpenAI-সহযোগী MiniMax API এর জন্য প্রয়োজনীয়
- **LangChain4j লাইব্রেরি আমদানি করেছি**: MCP ইন্টিগ্রেশন এবং OpenAI চ্যাট মডেল ফাংশনালিটির জন্য
- **একটি `ChatLanguageModel` তৈরি করেছি**: MiniMax ব্যবহার করে কনফিগার করা, আপনার MiniMax API কী, শেষ বিন্দু এবং সমর্থিত মডেল আইডি সহ
- **HTTP ট্রান্সপোর্ট সেটআপ করেছি**: সার্ভার-সেন্ট ইভেন্টস (SSE) ব্যবহার করে MCP সার্ভারের সাথে সংযোগ করার জন্য
- **একটি MCP ক্লায়েন্ট তৈরি করেছি**: সার্ভারের সাথে যোগাযোগ পরিচালনার জন্য
- **LangChain4j এর বিল্ট-ইন MCP সাপোর্ট ব্যবহার করেছি**: যা LLM এবং MCP সার্ভারের মধ্যে ইন্টিগ্রেশন সরল করে

#### রাস্ট

এই উদাহরণে ধরেছি যে আপনি একটি রাস্ট ভিত্তিক MCP সার্ভার চালু করেছেন। আপনার যদি না থাকে, তাহলে [01-first-server](../01-first-server/README.md) পাঠে ফিরে যান সার্ভার তৈরি করতে।

একবার আপনার রাস্ট MCP সার্ভার থাকলে, একটি টার্মিনাল খুলুন এবং সার্ভারের মতো একই ডিরেক্টরিতে যান। তারপর নিম্নলিখিত কমান্ড চালিয়ে একটি নতুন LLM ক্লায়েন্ট প্রকল্প তৈরি করুন:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

আপনার `Cargo.toml` ফাইলে নিম্নলিখিত ডিপেন্ডেন্সিগুলো যোগ করুন:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI এর জন্য অফিসিয়াল রাস্ট লাইব্রেরি না থাকলেও, `async-openai` ক্রেট একটি [সম্প্রদায় সংরক্ষিত লাইব্রেরি](https://platform.openai.com/docs/libraries/rust#rust) যা সাধারণত ব্যবহৃত হয়।

`src/main.rs` ফাইলটি খুলুন এবং এর বিষয়বস্তু নিচের কোড দিয়ে প্রতিস্থাপন করুন:

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

    // করতে হবে: MCP টুল তালিকা সংগ্রহ করুন

    // করতে হবে: টুল কল সহ LLM সংলাপ

    Ok(())
}
```

এই কোড একটি মৌলিক রাস্ট অ্যাপ্লিকেশন সেটআপ করে যা MCP সার্ভার এবং গিটহাব মডেলসের সাথে LLM ইন্টারঅ্যাকশনের জন্য সংযুক্ত হবে।

> [!IMPORTANT]
> অ্যাপ্লিকেশন চালানোর আগে নিশ্চিত করুন যে `OPENAI_API_KEY` পরিবেশ ভ্যারিয়েবল আপনার গিটহাব টোকেন দিয়ে সেট করা আছে।

দুর্দান্ত, আমাদের পরবর্তী ধাপ হলো সার্ভারের সক্ষমতাগুলো তালিকা করা।

### -2- সার্ভারের সক্ষমতাগুলো তালিকা করুন

এখন আমরা সার্ভারের সাথে সংযোগ করব এবং এর সক্ষমতা জানতে চাব:

#### টাইপস্ক্রিপ্ট

একই ক্লাসে, নিম্নলিখিত মেথডগুলো যোগ করুন:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // সরঞ্জামগুলি তালিকা করা
    const toolsResult = await this.client.listTools();
}
```

পূর্বের কোডে আমরা:

- সার্ভারের সাথে সংযোগের কোড যোগ করেছি, `connectToServer`।
- একটি `run` মেথড তৈরি করেছি যা আমাদের অ্যাপ ফ্লো হ্যান্ডেল করে। এখন পর্যন্ত এটি শুধু টুলস তালিকা করে, কিন্তু আমরা শীঘ্রই এতে আরও যোগ করব।

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

আমরা যা যুক্ত করেছি:

- রিসোর্স এবং টুল তালিকা করেছি এবং প্রিন্ট করেছি। টুলের জন্য আমরা `inputSchema`ও তালিকা করেছি যা পরে ব্যবহার করব।

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

পূর্বের কোডে আমরা:

- MCP সার্ভারে উপলব্ধ টুলস তালিকা করেছি
- প্রতিটি টুলের জন্য নাম, বিবরণ এবং স্কিমা তালিকা করেছি। শেষেরটি আমরা শীঘ্রই টুলস কল করার জন্য ব্যবহার করব।

#### জাভা

```java
// এমন একটি টুল প্রোভাইডার তৈরি করুন যা স্বয়ংক্রিয়ভাবে MCP টুলগুলি আবিষ্কার করে
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP টুল প্রোভাইডার স্বয়ংক্রিয়ভাবে নিম্নলিখিতগুলি হ্যান্ডেল করে:
// - MCP সার্ভার থেকে উপলব্ধ টুলগুলির তালিকা প্রস্তুত করা
// - MCP টুল স্কিমাগুলি LangChain4j ফরম্যাটে রূপান্তর করা
// - টুল কার্যকরী পরিচালনা এবং প্রতিক্রিয়া ব্যবস্থাপনা করা
```

পূর্বের কোডে আমরা:

- একটি `McpToolProvider` তৈরি করেছি যা স্বয়ংক্রিয়ভাবে MCP সার্ভার থেকে সব টুল আবিষ্কার ও রেজিস্টার করে
- টুল প্রোভাইডার MCP টুল স্কিমার এবং LangChain4j টুল ফরম্যাটের মধ্যে রূপান্তর নিজে থেকে পরিচালনা করে
- এই পদ্ধতি ম্যানুয়াল টুল তালিকা ও রূপান্তর প্রক্রিয়া থেকে মুক্তি দেয়

#### রাস্ট

MCP সার্ভার থেকে টুলস আনা `list_tools` মেথড ব্যবহার করে করা হয়। `main` ফাংশনে MCP ক্লায়েন্ট সেটআপ করার পর নিচের কোড যোগ করুন:

```rust
// MCP টুল লিস্টিং পান
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- সার্ভার সক্ষমতাকে LLM টুলস এ রূপান্তর করুন

সার্ভারের সক্ষমতা তালিকা করার পরের ধাপ হলো সেগুলো এমন ফরম্যাটে রূপান্তর করা যা LLM বুঝতে পারে। একবার আমরা এটা করলে, আমরা এই সক্ষমতাগুলো টুলস হিসেবে আমাদের LLM-এ দিতে পারব।

#### টাইপস্ক্রিপ্ট

1. MCP সার্ভার থেকে পাওয়া রেসপন্স রূপান্তর করার জন্য নিম্নলিখিত কোড যোগ করুন, যাতে এটি LLM ব্যবহারযোগ্য টুল ফরম্যাটে আসবে:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ইনপুট_schema এর উপর ভিত্তি করে একটি জড স্কিমা তৈরি করুন
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

    উপরের কোড MCP সার্ভার থেকে পাওয়া রেসপন্সকে এমন একটি টুল ডেফিনিশন ফরম্যাটে রূপান্তর করে যা LLM বুঝতে পারে।

2. এখন `run` মেথড আপডেট করুন সার্ভারের সক্ষমতা তালিকা করার জন্য:

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

    পূর্বের কোডে, আমরা `run` মেথড আপডেট করেছি যাতে এটি রেজাল্টের মধ্য দিয়ে যায় এবং প্রতিটি এন্ট্রির জন্য `openAiToolAdapter` কল করে।

#### পাইথন

1. প্রথমে, নিম্নলিখিত কনভার্টার ফাংশন তৈরি করি

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

    উপরের `convert_to_llm_tools` ফাংশন MCP টুল রেসপন্স নিয়ে এটিকে এমন ফরম্যাটে রূপান্তর করে যা LLM বুঝতে পারে।

2. এরপর, আমাদের ক্লায়েন্ট কোড আপডেট করি যাতে এটি ফাংশনটি ব্যবহার করে:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    এখানে, আমরা `convert_to_llm_tool` কল যোগ করছি যা MCP টুল রেসপন্সকে এমন কিছুতে রূপান্তর করে যা আমরা পরে LLM-এ দিতে পারব।

#### .NET

1. MCP টুল রেসপন্সকে এমন কিছুতে রূপান্তর করার কোড যোগ করি যা LLM বুঝতে পারে

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

পূর্বের কোডে আমরা:

- একটি `ConvertFrom` ফাংশন তৈরি করেছি যা নাম, বিবরণ এবং ইনপুট স্কিমা নেয়।
- এমন এক ফাংশনালিটি ডিফাইন করেছি যা একটি FunctionDefinition তৈরি করে এবং এটি ChatCompletionsDefinition-এ পাস করে। শেষেরটি LLM বুঝতে পারে।

2. এই ফাংশন ব্যবহার করে কীভাবে বিদ্যমান কোড আপডেট করা যায় তা দেখি:

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

#### জাভা

```java
// প্রাকৃতিক ভাষা ইন্টারঅ্যাকশনের জন্য একটি বট ইন্টারফেস তৈরি করুন
public interface Bot {
    String chat(String prompt);
}

// LLM এবং MCP টুলস সহ AI সার্ভিস কনফিগার করুন
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

পূর্বের কোডে আমরা:

- সহজ `Bot` ইন্টারফেস ডিফাইন করেছি প্রাকৃতিক ভাষার ইন্টারঅ্যাকশনের জন্য
- LangChain4j এর `AiServices` ব্যবহার করেছি যা স্বয়ংক্রিয়ভাবে LLM কে MCP টুল প্রোভাইডারের সাথে বেঁধে দেয়
- ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে টুল স্কিমা রূপান্তর এবং ফাংশন কলিং পেছনের দিক থেকে পরিচালনা করে
- এই পদ্ধতি ম্যানুয়াল টুল রূপান্তর নির্মূল করে - LangChain4j সব MCP টুলকে LLM-সঙ্গত ফরম্যাটে রূপান্তর করার জটিলতা সামলায়

#### রাস্ট

MCP টুল রেসপন্সকে এমন ফরম্যাটে রূপান্তর করার জন্য যা LLM বুঝতে পারে, আমরা একটি হেল্পার ফাংশন যোগ করব যা টুলস তালিকাকে ফরম্যাট করবে। `main.rs` ফাইলে `main` ফাংশনের নিচে নিম্নলিখিত কোড যোগ করুন। এটি LLM-এ অনুরোধ করার সময় কল করা হবে:

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

দুর্দান্ত, এখন আমরা ব্যবহারকারীর যে কোনো অনুরোধ হ্যান্ডল করতে প্রস্তুত, তাই চলুন সেটি করব।

### -4- ব্যবহারকারীর প্রম্পট অনুরোধ হ্যান্ডেল করুন

এই অংশে, আমরা ব্যবহারকারীর অনুরোধগুলো হ্যান্ডল করব।

#### টাইপস্ক্রিপ্ট

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

        // ৩. ফলাফলের সাথে কিছু করুন
        // TODO

        }
    }
    ```

    পূর্বের কোডে আমরা:

    - একটি মেথড `callTools` যোগ করেছি।
    - মেথডটি LLM রেসপন্স নিয়ে দেখে কি কি টুলস কল হয়েছে, যদি থাকে:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // কল টুল
        }
        ```

    - একটি টুল কল করে, যদি LLM নির্দেশ দেয় কল করা উচিত:

        ```typescript
        // ২. সার্ভারের টুল কল করুন
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ৩. ফলাফল নিয়ে কিছু করুন
        // করণীয়
        ```

2. `run` মেথড আপডেট করুন যাতে LLM কল এবং `callTools` কল অন্তর্ভুক্ত থাকে:

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

    // 3. LLM এর প্রতিক্রিয়া পরীক্ষা করুন, প্রতিটি পছন্দের জন্য, দেখুন এতে টুল কল আছে কিনা
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

দুর্দান্ত, সম্পূর্ণ কোড তালিকা করি:

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
            baseURL: "https://models.inference.ai.azure.com", // ভবিষ্যতে এই URL এ পরিবর্তন করা লাগতে পারে: https://models.github.ai/inference
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
    
        // ৩। LLM প্রতিক্রিয়ার মাধ্যমে যান, প্রতিটি চয়েসের জন্য পরীক্ষা করুন এটি টুল কল আছে কিনা
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

#### পাইথন

1. কিছু ইম্পোর্ট যোগ করি যা LLM কল করতে লাগব

    ```python
    # এলএলএম
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. পরবর্তীতে, এমন একটি ফাংশন যোগ করি যা LLM কল করবে:

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
            # ঐচ্ছিক প্যারামিটারগুলি
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

    পূর্বের কোডে আমরা:

    - MCP সার্ভারে পাওয়া এবং রূপান্তরিত ফাংশনগুলো LLM এ পাস করেছি।
    - এরপর LLM সেই ফাংশনগুলো দিয়ে কল করেছি।
    - তারপর রেজাল্ট পরীক্ষা করছি কোন কোন ফাংশন কল করা উচিত।
    - অবশেষে কল করার জন্য ফাংশনের একটি অ্যারে পাস করেছি।

3. চূড়ান্ত ধাপ, আমাদের প্রধান কোড আপডেট করি:

    ```python
    prompt = "Add 2 to 20"

    # LLM কে জিজ্ঞাসা করুন কোন টুলগুলি ব্যবহার করা উচিত, যদি থাকে
    functions_to_call = call_llm(prompt, functions)

    # প্রস্তাবিত ফাংশনগুলি কল করুন
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    দেখুন, এটি শেষ ধাপ; উপরের কোডে আমরা:

    - একটি MCP টুলকে `call_tool` এর মাধ্যমে কল করেছি যার ফাংশন LLM আমাদের প্রম্পটের ভিত্তিতে কল করতে বলেছিল।
    - MCP সার্ভারের টুল কলের রেজাল্ট প্রিন্ট করেছি।

#### .NET

1. এখানে দেখানো হলো LLM প্রম্পট অনুরোধ করার কিছু কোড:

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

    পূর্বের কোডে আমরা:

    - MCP সার্ভার থেকে টুলস নিয়ে আসলাম, `var tools = await GetMcpTools()`।
    - একটি ব্যবহারকারী প্রম্পট ডিফাইন করলাম `userMessage`।
    - মডেল এবং টুলস স্পেসিফাই করে একটি অপশন অবজেক্ট তৈরি করলাম।
    - LLM এর কাছে অনুরোধ পাঠালাম।

2. শেষ ধাপ, দেখি LLM মনে করে কোন ফাংশন কল করা উচিত কি না:

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

    পূর্বের কোডে আমরা:

    - একটি ফাংশন কল তালিকা লুপ করেছি।
    - প্রতিটি টুল কলের নাম এবং আর্গুমেন্ট পার্স করে MCP সার্ভারে টুল কল করেছি MCP ক্লায়েন্ট ব্যবহার করে। শেষে রেজাল্ট প্রিন্ট করেছি।

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

#### জাভা

```java
try {
    // স্বয়ংক্রিয়ভাবে MCP টুলস ব্যবহার করে প্রাকৃতিক ভাষার অনুরোধ কার্যকর করুন
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

পূর্বের কোডে আমরা:

- সহজ প্রাকৃতিক ভাষার প্রম্পট ব্যবহার করে MCP সার্ভারের টুলসের সাথে ইন্টারঅ্যাকশন করেছি
- LangChain4j ফ্রেমওয়ার্ক স্বয়ংক্রিয়ভাবে সামলায়:
  - প্রয়োজন হলে ব্যবহারকারীর প্রম্পট থেকে টুল কল রূপান্তর করা
  - LLM সিদ্ধান্ত অনুসারে প্রাসঙ্গিক MCP টুলস কল করা
  - LLM এবং MCP সার্ভারের মধ্যে কথোপকথনের প্রবাহ পরিচালনা
- `bot.chat()` মেথড প্রাকৃতিক ভাষার উত্তর প্রদান করে যা MCP টুল কার্য বাস্তবায়নের ফলাফল অন্তর্ভুক্ত করতে পারে
- এই পদ্ধতি ব্যবহারকারীদের জন্য একটি নিরবচ্ছিন্ন অভিজ্ঞতা নিশ্চিত করে যেখানে তারা MCP বাস্তবায়নের বিষয়ে জানার প্রয়োজন নেই

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

#### রাস্ট

এখানে অধিকাংশ কাজ সাধিত হয়। আমরা প্রাথমিক ব্যবহারকারী প্রম্পটসহ LLM কল করব, তারপর রেসপন্স প্রক্রিয়া করব দেখতে কোন টুল কল দরকার। যদি দরকার হয়, তাহলে সেই টুলগুলো কল করব এবং LLM এর সাথে কথা চালিয়ে যাব যতক্ষণ আর কোন টুল কলের প্রয়োজন নেই এবং আমরা একটি চূড়ান্ত উত্তর পাই।


আমরা LLM-এ একাধিক কল করব, তাই আসুন একটি ফাংশন সংজ্ঞায়িত করি যা LLM কলটি পরিচালনা করবে। আপনার `main.rs` ফাইলে নিম্নলিখিত ফাংশনটি যোগ করুন:

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

এই ফাংশনটি LLM ক্লায়েন্ট, বার্তাগুলির একটি তালিকা (ব্যবহারকারীর প্রম্পট সহ), MCP সার্ভার থেকে টুলগুলি নেয় এবং LLM-এ একটি অনুরোধ পাঠায়, এবং প্রতিক্রিয়া ফেরত দেয়।

LLM থেকে প্রাপ্ত প্রতিক্রিয়াটি একটি `choices` অ্যারে থাকবে। ফলাফল প্রসেস করতে হবে দেখতে `tool_calls` আছে কিনা। এটি আমাদের জানায় যে LLM একটি নির্দিষ্ট টুল কল করার জন্য আর্গুমেন্টসহ অনুরোধ করছে। LLM প্রতিক্রিয়া পরিচালনার জন্য একটি ফাংশন সংজ্ঞায়িত করতে নিচের কোডটি আপনার `main.rs` ফাইলের নীচে যোগ করুন:

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

    // যদি উপযুক্ত থাকে, কনটেন্ট প্রিন্ট করুন
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // টুল কলসমূহ পরিচালনা করুন
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // সহকারী মেসেজ যোগ করুন

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

            // মেসেজগুলিতে টুল ফলাফল যোগ করুন
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // টুল ফলাফলসমূহ নিয়ে আলোচনাটি চালিয়ে যান
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

যদি `tool_calls` থাকে, এটি টুলের তথ্য বের করে, টুল অনুরোধ নিয়ে MCP সার্ভারকে কল করে, এবং ফলাফলগুলি কথোপকথন মেসেজগুলিতে যোগ করে। এরপর এটি LLM-এ কথোপকথন চালিয়ে যায় এবং মেসেজগুলি সহকারী প্রতিক্রিয়া এবং টুল কলের ফলাফলের সাথে আপডেট হয়।

MCP কলের জন্য LLM যেভাবে টুল কল তথ্য ফেরত দেয় তা বের করতে, আমরা আরও একটি সহায়ক ফাংশন যোগ করব যা কল করার জন্য প্রয়োজনীয় সবকিছু বের করবে। আপনার `main.rs` ফাইলের নীচে নিম্নলিখিত কোড যোগ করুন:

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

সব উপাদান প্রস্তুত হওয়ায়, আমরা এখন প্রাথমিক ব্যবহারকারীর প্রম্পট পরিচালনা করতে এবং LLM কল করতে পারি। আপনার `main` ফাংশন আপডেট করুন নিম্নলিখিত কোডসহ:

```rust
// টুল কলসহ এলএলএম কথোপকথন
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

এটি প্রাথমিক ব্যবহারকারীর প্রম্পট নিয়ে দুইটি সংখ্যার যোগফল জানতে LLM-এ অনুসন্ধান করবে এবং প্রতিক্রিয়া প্রসেস করে ডায়নামিক টুল কল পরিচালনা করবে।

চমৎকার, আপনি এটি করেছেন!

## অ্যাসাইনমেন্ট

ব্যায়াম থেকে কোড নিয়ে সার্ভারটি আরও কিছু টুল নিয়ে তৈরি করুন। তারপর একটি ক্লায়েন্ট তৈরি করুন LLM সহ, যেমন ব্যায়ামে হয়েছে, এবং বিভিন্ন প্রম্পট দিয়ে পরীক্ষা করুন যাতে নিশ্চিত হতে পারেন আপনার সমস্ত সার্ভার টুল ডায়নামিকভাবে কল হচ্ছে। এই ধরনের ক্লায়েন্ট তৈরি ব্যবহারকারীকে একটি চমৎকার অভিজ্ঞতা দেবে কারণ তারা সঠিক ক্লায়েন্ট কমান্ডের পরিবর্তে প্রম্পট ব্যবহার করতে পারবে এবং MCP সার্ভারে কল হচ্ছে তা টের পাবে না।

## সমাধান

[সমাধান](./solution/README.md)

## মূল শিক্ষা

- ক্লায়েন্টে একটি LLM যোগ করা MCP সার্ভারের সাথে ব্যবহারকারীর ভাল ইন্টারঅ্যাকশন নিশ্চিত করে।
- MCP সার্ভারের প্রতিক্রিয়াটি LLM যাতে বুঝতে পারে তা রূপান্তর করতে হবে।

## নমুনা

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## অতিরিক্ত সম্পদ

## পরবর্তী বিষয়

- পরবর্তী: [Visual Studio Code ব্যবহার করে সার্ভার ব্যবহার](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->