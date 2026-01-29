# LLM کے ساتھ کلائنٹ بنانا

اب تک، آپ نے دیکھا ہے کہ سرور اور کلائنٹ کیسے بنائے جاتے ہیں۔ کلائنٹ سرور کو واضح طور پر کال کر کے اس کے ٹولز، وسائل اور پرامپٹس کی فہرست حاصل کر سکتا ہے۔ تاہم، یہ طریقہ کار بہت عملی نہیں ہے۔ آپ کا صارف ایجنٹک دور میں رہتا ہے اور توقع کرتا ہے کہ وہ پرامپٹس استعمال کرے اور LLM کے ساتھ بات چیت کرے۔ آپ کے صارف کے لیے یہ اہم نہیں کہ آپ اپنی صلاحیتوں کو ذخیرہ کرنے کے لیے MCP استعمال کرتے ہیں یا نہیں، لیکن وہ قدرتی زبان میں بات چیت کی توقع رکھتے ہیں۔ تو ہم اس مسئلے کو کیسے حل کریں؟ حل یہ ہے کہ کلائنٹ میں ایک LLM شامل کیا جائے۔

## جائزہ

اس سبق میں ہم کلائنٹ میں LLM شامل کرنے پر توجہ مرکوز کریں گے اور دکھائیں گے کہ یہ آپ کے صارف کے لیے کس طرح بہتر تجربہ فراہم کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ قابل ہوں گے:

- LLM کے ساتھ ایک کلائنٹ بنائیں۔
- LLM کا استعمال کرتے ہوئے MCP سرور کے ساتھ بغیر رکاوٹ بات چیت کریں۔
- کلائنٹ سائڈ پر بہتر صارف تجربہ فراہم کریں۔

## طریقہ کار

آئیے سمجھنے کی کوشش کرتے ہیں کہ ہمیں کون سا طریقہ اختیار کرنا ہے۔ LLM شامل کرنا آسان لگتا ہے، لیکن کیا ہم واقعی ایسا کریں گے؟

یہاں بتایا گیا ہے کہ کلائنٹ سرور کے ساتھ کیسے بات چیت کرے گا:

1. سرور کے ساتھ کنکشن قائم کریں۔

1. صلاحیتوں، پرامپٹس، وسائل اور ٹولز کی فہرست بنائیں، اور ان کا اسکیمہ محفوظ کریں۔

1. ایک LLM شامل کریں اور محفوظ شدہ صلاحیتوں اور ان کے اسکیمے کو ایسے فارمیٹ میں پاس کریں جو LLM سمجھتا ہو۔

1. صارف کے پرامپٹ کو LLM کو پاس کریں، ساتھ ہی کلائنٹ کی طرف سے فہرست کردہ ٹولز بھی دیں۔

زبردست، اب جب ہم اعلی سطح پر سمجھ گئے ہیں کہ ہم یہ کیسے کر سکتے ہیں، تو آئیے نیچے دیے گئے مشق میں اسے آزما کر دیکھتے ہیں۔

## مشق: LLM کے ساتھ کلائنٹ بنانا

اس مشق میں، ہم اپنے کلائنٹ میں LLM شامل کرنا سیکھیں گے۔

### GitHub پرسنل ایکسیس ٹوکن کے ذریعے توثیق

GitHub ٹوکن بنانا ایک سیدھا سادہ عمل ہے۔ یہاں بتایا گیا ہے کہ آپ یہ کیسے کر سکتے ہیں:

- GitHub سیٹنگز پر جائیں – اوپر دائیں کونے میں اپنی پروفائل تصویر پر کلک کریں اور سیٹنگز منتخب کریں۔
- ڈیولپر سیٹنگز پر جائیں – نیچے سکرول کریں اور ڈیولپر سیٹنگز پر کلک کریں۔
- پرسنل ایکسیس ٹوکن منتخب کریں – Fine-grained tokens پر کلک کریں اور پھر Generate new token پر کلک کریں۔
- اپنا ٹوکن ترتیب دیں – حوالہ کے لیے نوٹ شامل کریں، ایکسپائری کی تاریخ مقرر کریں، اور ضروری اسکوپس (اجازتیں) منتخب کریں۔ اس معاملے میں Models کی اجازت شامل کرنا یقینی بنائیں۔
- ٹوکن بنائیں اور کاپی کریں – Generate token پر کلک کریں، اور فوراً اسے کاپی کر لیں کیونکہ آپ اسے دوبارہ نہیں دیکھ سکیں گے۔

### -1- سرور سے کنیکٹ کریں

آئیے پہلے اپنا کلائنٹ بنائیں:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // سکیمہ کی توثیق کے لیے زوڈ درآمد کریں

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

پچھلے کوڈ میں ہم نے:

- ضروری لائبریریاں امپورٹ کیں
- ایک کلاس بنائی جس میں دو ممبرز ہیں، `client` اور `openai` جو بالترتیب کلائنٹ کو منظم کرنے اور LLM کے ساتھ بات چیت کرنے میں مدد دیں گے۔
- اپنے LLM انسٹینس کو GitHub Models استعمال کرنے کے لیے ترتیب دیا، `baseUrl` کو inference API کی طرف اشارہ کرتے ہوئے۔

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# اسٹڈیئو کنکشن کے لیے سرور کے پیرامیٹرز بنائیں
server_params = StdioServerParameters(
    command="mcp",  # قابلِ اجرا
    args=["run", "server.py"],  # اختیاری کمانڈ لائن دلائل
    env=None,  # اختیاری ماحول کے متغیرات
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # کنکشن کو شروع کریں
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

پچھلے کوڈ میں ہم نے:

- MCP کے لیے ضروری لائبریریاں امپورٹ کیں
- ایک کلائنٹ بنایا

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

سب سے پہلے، آپ کو اپنے `pom.xml` فائل میں LangChain4j کی dependencies شامل کرنی ہوں گی۔ MCP انٹیگریشن اور GitHub Models کی سپورٹ کے لیے یہ dependencies شامل کریں:

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

پھر اپنا Java کلائنٹ کلاس بنائیں:

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
    
    public static void main(String[] args) throws Exception {        // ایل ایل ایم کو گٹ ہب ماڈلز استعمال کرنے کے لیے ترتیب دیں
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // سرور سے جڑنے کے لیے ایم سی پی ٹرانسپورٹ بنائیں
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // ایم سی پی کلائنٹ بنائیں
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

پچھلے کوڈ میں ہم نے:

- **LangChain4j dependencies شامل کیں**: MCP انٹیگریشن، OpenAI آفیشل کلائنٹ، اور GitHub Models کی سپورٹ کے لیے
- **LangChain4j لائبریریاں امپورٹ کیں**: MCP انٹیگریشن اور OpenAI چیٹ ماڈل کی فعالیت کے لیے
- **`ChatLanguageModel` بنایا**: GitHub Models کو آپ کے GitHub ٹوکن کے ساتھ استعمال کرنے کے لیے ترتیب دیا
- **HTTP ٹرانسپورٹ سیٹ اپ کیا**: Server-Sent Events (SSE) کا استعمال کرتے ہوئے MCP سرور سے کنیکٹ کرنے کے لیے
- **MCP کلائنٹ بنایا**: جو سرور کے ساتھ بات چیت سنبھالے گا
- **LangChain4j کی بلٹ ان MCP سپورٹ استعمال کی**: جو LLMs اور MCP سرورز کے درمیان انٹیگریشن کو آسان بناتی ہے

#### Rust

یہ مثال فرض کرتی ہے کہ آپ کے پاس Rust پر مبنی MCP سرور چل رہا ہے۔ اگر آپ کے پاس نہیں ہے، تو سرور بنانے کے لیے [01-first-server](../01-first-server/README.md) سبق کو دیکھیں۔

جب آپ کے پاس Rust MCP سرور ہو، تو ایک ٹرمینل کھولیں اور سرور کی ڈائریکٹری میں جائیں۔ پھر نیا LLM کلائنٹ پروجیکٹ بنانے کے لیے درج ذیل کمانڈ چلائیں:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

اپنی `Cargo.toml` فائل میں درج ذیل dependencies شامل کریں:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI کے لیے کوئی آفیشل Rust لائبریری نہیں ہے، تاہم `async-openai` crate ایک [کمیونٹی کی دیکھ بھال والی لائبریری](https://platform.openai.com/docs/libraries/rust#rust) ہے جو عام طور پر استعمال ہوتی ہے۔

`src/main.rs` فائل کھولیں اور اس کا مواد درج ذیل کوڈ سے تبدیل کریں:

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
    // ابتدائی پیغام
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // اوپن اے آئی کلائنٹ سیٹ اپ کریں
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // ایم سی پی کلائنٹ سیٹ اپ کریں
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

    // کرنے کے لیے: ایم سی پی ٹول کی فہرست حاصل کریں

    // کرنے کے لیے: ٹول کالز کے ساتھ ایل ایل ایم گفتگو

    Ok(())
}
```

یہ کوڈ ایک بنیادی Rust ایپلیکیشن سیٹ اپ کرتا ہے جو MCP سرور اور GitHub Models کے ساتھ LLM انٹریکشن کے لیے کنیکٹ کرے گا۔

> [!IMPORTANT]
> ایپلیکیشن چلانے سے پہلے `OPENAI_API_KEY` ماحول متغیر کو اپنے GitHub ٹوکن کے ساتھ سیٹ کرنا یقینی بنائیں۔

زبردست، اگلے مرحلے کے لیے، آئیے سرور کی صلاحیتوں کی فہرست بنائیں۔

### -2- سرور کی صلاحیتوں کی فہرست بنائیں

اب ہم سرور سے کنیکٹ کریں گے اور اس کی صلاحیتوں کے بارے میں پوچھیں گے:

#### Typescript

اسی کلاس میں درج ذیل طریقے شامل کریں:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // آلات کی فہرست بنانا
    const toolsResult = await this.client.listTools();
}
```

پچھلے کوڈ میں ہم نے:

- سرور سے کنیکٹ کرنے کے لیے کوڈ شامل کیا، `connectToServer`۔
- ایک `run` طریقہ بنایا جو ہماری ایپ کے فلو کو سنبھالتا ہے۔ اب تک یہ صرف ٹولز کی فہرست دیتا ہے لیکن ہم جلد ہی اس میں مزید اضافہ کریں گے۔

#### Python

```python
# دستیاب وسائل کی فہرست بنائیں
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# دستیاب آلات کی فہرست بنائیں
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

یہاں ہم نے کیا شامل کیا:

- وسائل اور ٹولز کی فہرست بنائی اور انہیں پرنٹ کیا۔ ٹولز کے لیے ہم `inputSchema` بھی فہرست کرتے ہیں جو بعد میں استعمال ہوگا۔

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

پچھلے کوڈ میں ہم نے:

- MCP سرور پر دستیاب ٹولز کی فہرست بنائی
- ہر ٹول کے لیے نام، وضاحت اور اس کا اسکیمہ فہرست کیا۔ یہ اسکیمہ ہم جلد ہی ٹولز کو کال کرنے کے لیے استعمال کریں گے۔

#### Java

```java
// ایک ٹول فراہم کنندہ بنائیں جو خود بخود MCP ٹولز کو دریافت کرے
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ٹول فراہم کنندہ خود بخود مندرجہ ذیل کام کرتا ہے:
// - MCP سرور سے دستیاب ٹولز کی فہرست بنانا
// - MCP ٹول اسکیموں کو LangChain4j فارمیٹ میں تبدیل کرنا
// - ٹول کے نفاذ اور جوابات کا انتظام کرنا
```

پچھلے کوڈ میں ہم نے:

- ایک `McpToolProvider` بنایا جو خودکار طور پر MCP سرور سے تمام ٹولز دریافت اور رجسٹر کرتا ہے
- ٹول پرووائیڈر MCP ٹول اسکیموں اور LangChain4j کے ٹول فارمیٹ کے درمیان تبدیلی کو اندرونی طور پر سنبھالتا ہے
- یہ طریقہ کار دستی ٹول فہرست سازی اور تبدیلی کے عمل کو ختم کرتا ہے

#### Rust

MCP سرور سے ٹولز حاصل کرنے کے لیے `list_tools` طریقہ استعمال کیا جاتا ہے۔ اپنے `main` فنکشن میں، MCP کلائنٹ سیٹ اپ کرنے کے بعد، درج ذیل کوڈ شامل کریں:

```rust
// MCP ٹول کی فہرست حاصل کریں
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- سرور کی صلاحیتوں کو LLM ٹولز میں تبدیل کریں

سرور کی صلاحیتوں کی فہرست بنانے کے بعد اگلا قدم انہیں ایسے فارمیٹ میں تبدیل کرنا ہے جو LLM سمجھ سکے۔ جب ہم یہ کر لیں، تو ہم ان صلاحیتوں کو اپنے LLM کے لیے ٹولز کے طور پر فراہم کر سکتے ہیں۔

#### TypeScript

1. MCP سرور کے جواب کو ایسے ٹول فارمیٹ میں تبدیل کرنے کے لیے درج ذیل کوڈ شامل کریں جو LLM استعمال کر سکے:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ان پٹ_سکیما کی بنیاد پر زوڈ اسکیمہ بنائیں
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // قسم کو واضح طور پر "فنکشن" پر سیٹ کریں
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

    اوپر دیا گیا کوڈ MCP سرور کے جواب کو لے کر اسے ایسے ٹول کی تعریف کے فارمیٹ میں تبدیل کرتا ہے جو LLM سمجھتا ہے۔

1. اب `run` طریقہ کو اپ ڈیٹ کریں تاکہ سرور کی صلاحیتوں کی فہرست بنائی جا سکے:

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

    پچھلے کوڈ میں، ہم نے `run` طریقہ کو اپ ڈیٹ کیا ہے تاکہ نتیجہ کے ذریعے مپ کیا جا سکے اور ہر اندراج کے لیے `openAiToolAdapter` کال کی جا سکے۔

#### Python

1. پہلے، درج ذیل کنورٹر فنکشن بنائیں

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

    اوپر دیے گئے `convert_to_llm_tools` فنکشن میں ہم MCP ٹول کے جواب کو لے کر اسے ایسے فارمیٹ میں تبدیل کرتے ہیں جو LLM سمجھ سکے۔

1. اگلا، اپنے کلائنٹ کوڈ کو اس فنکشن کا فائدہ اٹھانے کے لیے اپ ڈیٹ کریں:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    یہاں، ہم `convert_to_llm_tool` کال شامل کر رہے ہیں تاکہ MCP ٹول کے جواب کو ایسی شکل میں تبدیل کیا جا سکے جسے ہم بعد میں LLM کو دے سکیں۔

#### .NET

1. MCP ٹول کے جواب کو ایسی شکل میں تبدیل کرنے کے لیے کوڈ شامل کریں جو LLM سمجھ سکے

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

پچھلے کوڈ میں ہم نے:

- `ConvertFrom` فنکشن بنایا جو نام، وضاحت اور ان پٹ اسکیمہ لیتا ہے۔
- ایسی فعالیت متعین کی جو `FunctionDefinition` بناتی ہے جو `ChatCompletionsDefinition` کو پاس کی جاتی ہے۔ یہ وہ چیز ہے جو LLM سمجھتا ہے۔

1. اب دیکھیں کہ ہم موجودہ کوڈ کو اس فنکشن کے فائدے کے لیے کیسے اپ ڈیٹ کر سکتے ہیں:

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
// قدرتی زبان کے تعامل کے لیے بوٹ انٹرفیس بنائیں
public interface Bot {
    String chat(String prompt);
}

// LLM اور MCP ٹولز کے ساتھ AI سروس کو ترتیب دیں
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

پچھلے کوڈ میں ہم نے:

- قدرتی زبان کی بات چیت کے لیے ایک سادہ `Bot` انٹرفیس متعین کیا
- LangChain4j کے `AiServices` استعمال کیے تاکہ LLM کو خودکار طور پر MCP ٹول پرووائیڈر کے ساتھ باندھ دیا جائے
- فریم ورک خودکار طور پر ٹول اسکیمہ کی تبدیلی اور فنکشن کالنگ کو پس منظر میں سنبھالتا ہے
- یہ طریقہ کار دستی ٹول تبدیلی کو ختم کرتا ہے - LangChain4j MCP ٹولز کو LLM کے قابل قبول فارمیٹ میں تبدیل کرنے کی تمام پیچیدگی سنبھالتا ہے

#### Rust

MCP ٹول کے جواب کو LLM کے سمجھنے کے قابل فارمیٹ میں تبدیل کرنے کے لیے، ہم ایک ہیلپر فنکشن شامل کریں گے جو ٹولز کی فہرست کو فارمیٹ کرے گا۔ اپنے `main.rs` فائل میں `main` فنکشن کے نیچے درج ذیل کوڈ شامل کریں۔ یہ LLM کو درخواست بھیجتے وقت کال کیا جائے گا:

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

زبردست، اب ہم صارف کی درخواستوں کو سنبھالنے کے لیے تیار ہیں، تو آئیے اگلے مرحلے پر چلتے ہیں۔

### -4- صارف کے پرامپٹ کی درخواست سنبھالیں

اس کوڈ کے حصے میں، ہم صارف کی درخواستوں کو سنبھالیں گے۔

#### TypeScript

1. ایک طریقہ شامل کریں جو ہمارے LLM کو کال کرنے کے لیے استعمال ہوگا:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // ۲۔ سرور کے ٹول کو کال کریں
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳۔ نتیجہ کے ساتھ کچھ کریں
        // کرنے کے لیے

        }
    }
    ```

    پچھلے کوڈ میں ہم نے:

    - `callTools` نامی طریقہ شامل کیا۔
    - یہ طریقہ LLM کے جواب کو لیتا ہے اور چیک کرتا ہے کہ کون سے ٹولز کال کیے گئے ہیں، اگر کوئی ہیں:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // آلہ کال کریں
        }
        ```

    - اگر LLM نے اشارہ دیا کہ کسی ٹول کو کال کرنا چاہیے تو اسے کال کرتا ہے:

        ```typescript
        // ۲۔ سرور کے ٹول کو کال کریں
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳۔ نتیجہ کے ساتھ کچھ کریں
        // کرنے کے لیے
        ```

1. `run` طریقہ کو اپ ڈیٹ کریں تاکہ LLM کو کال کیا جا سکے اور `callTools` کو کال کیا جا سکے:

    ```typescript

    // 1. پیغامات بنائیں جو LLM کے لیے ان پٹ ہوں
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM کو کال کرنا
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM کے جواب کا جائزہ لیں، ہر انتخاب کے لیے چیک کریں کہ آیا اس میں ٹول کالز ہیں یا نہیں
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

زبردست، مکمل کوڈ درج ذیل ہے:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // سکیمہ کی توثیق کے لیے زوڈ درآمد کریں

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // مستقبل میں اس یو آر ایل کو تبدیل کرنے کی ضرورت ہو سکتی ہے: https://models.github.ai/inference
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
          // ان پٹ_سکیمہ کی بنیاد پر زوڈ سکیمہ بنائیں
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // قسم کو واضح طور پر "فنکشن" پر سیٹ کریں
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
    
    
          // 2۔ سرور کے ٹول کو کال کریں
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3۔ نتیجہ کے ساتھ کچھ کریں
          // کرنے کے لیے
    
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
    
        // 1۔ ایل ایل ایم کے جواب کو دیکھیں، ہر انتخاب کے لیے چیک کریں کہ آیا اس میں ٹول کالز ہیں
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

1. LLM کو کال کرنے کے لیے کچھ ضروری امپورٹس شامل کریں

    ```python
    # ایل ایل ایم
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. پھر، وہ فنکشن شامل کریں جو LLM کو کال کرے گا:

    ```python
    # ایل ایل ایم

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
            # اختیاری پیرامیٹرز
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

    پچھلے کوڈ میں ہم نے:

    - اپنے فنکشنز جو MCP سرور پر ملے اور تبدیل کیے گئے، انہیں LLM کو پاس کیا۔
    - پھر LLM کو ان فنکشنز کے ساتھ کال کیا۔
    - پھر نتیجہ کا معائنہ کیا کہ کون سے فنکشنز کال کرنے چاہئیں، اگر کوئی ہوں۔
    - آخر میں، کال کرنے کے لیے فنکشنز کی ایک فہرست پاس کی۔

1. آخری مرحلہ، اپنے مرکزی کوڈ کو اپ ڈیٹ کریں:

    ```python
    prompt = "Add 2 to 20"

    # LLM سے پوچھیں کہ کون سے ٹولز سب کو، اگر کوئی ہوں
    functions_to_call = call_llm(prompt, functions)

    # تجویز کردہ فنکشنز کو کال کریں
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    یہ آخری مرحلہ تھا، اوپر دیے گئے کوڈ میں ہم:

    - `call_tool` کے ذریعے MCP ٹول کو کال کر رہے ہیں، وہ فنکشن جو LLM نے ہمارے پرامپٹ کی بنیاد پر کال کرنے کا سوچا تھا۔
    - MCP سرور پر ٹول کال کے نتیجے کو پرنٹ کر رہے ہیں۔

#### .NET

1. LLM پرامپٹ درخواست کرنے کے لیے کچھ کوڈ دکھائیں:

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

    پچھلے کوڈ میں ہم نے:

    - MCP سرور سے ٹولز حاصل کیے، `var tools = await GetMcpTools()`۔
    - صارف کا پرامپٹ `userMessage` متعین کیا۔
    - ماڈل اور ٹولز کی وضاحت کرتے ہوئے ایک options آبجیکٹ بنایا۔
    - LLM کی طرف درخواست بھیجی۔

1. آخری مرحلہ، دیکھیں کہ کیا LLM سمجھتا ہے کہ ہمیں فنکشن کال کرنی چاہیے:

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

    پچھلے کوڈ میں ہم نے:

    - فنکشن کالز کی فہرست میں لوپ لگایا۔
    - ہر ٹول کال کے لیے نام اور دلائل نکالے اور MCP کلائنٹ کا استعمال کرتے ہوئے MCP سرور پر ٹول کال کی۔ آخر میں نتائج پرنٹ کیے۔

مکمل کوڈ درج ذیل ہے:

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
    // قدرتی زبان کی درخواستیں انجام دیں جو خود بخود MCP ٹولز استعمال کرتی ہیں
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

پچھلے کوڈ میں ہم نے:

- MCP سرور کے ٹولز کے ساتھ سادہ قدرتی زبان کے پرامپٹس استعمال کیے
- LangChain4j فریم ورک خودکار طور پر سنبھالتا ہے:
  - جب ضرورت ہو تو صارف کے پرامپٹس کو ٹول کالز میں تبدیل کرنا
  - LLM کے فیصلے کی بنیاد پر مناسب MCP ٹولز کو کال کرنا
  - LLM اور MCP سرور کے درمیان گفتگو کے بہاؤ کا انتظام کرنا
- `bot.chat()` طریقہ قدرتی زبان میں جوابات دیتا ہے جن میں MCP ٹولز کے نتائج شامل ہو سکتے ہیں
- یہ طریقہ کار صارف کو ایک ہموار تجربہ فراہم کرتا ہے جہاں صارفین کو MCP کی اندرونی تفصیلات جاننے کی ضرورت نہیں ہوتی

مکمل کوڈ کی مثال:

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

یہاں زیادہ تر کام ہوتا ہے۔ ہم ابتدائی صارف کے پرامپٹ کے ساتھ LLM کو کال کریں گے، پھر جواب کا تجزیہ کریں گے کہ کیا کسی ٹول کو کال کرنے کی ضرورت ہے۔ اگر ہاں، تو ہم وہ ٹولز کال کریں گے اور LLM کے ساتھ گفتگو جاری رکھیں گے جب تک مزید ٹول کالز کی ضرورت نہ ہو اور ہمیں حتمی جواب نہ مل جائے۔

ہم LLM کو متعدد بار کال کریں گے، لہٰذا ایک فنکشن متعین کرتے ہیں جو LLM کال کو سنبھالے گا۔ اپنے `main.rs` فائل میں درج ذیل فنکشن شامل کریں:

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

یہ فنکشن LLM کلائنٹ، پیغامات کی فہرست (جس میں صارف کا پرامپٹ شامل ہے)، MCP سرور کے ٹولز لیتا ہے، اور LLM کو درخواست بھیجتا ہے، پھر جواب واپس کرتا ہے۔
LLM کا جواب `choices` کے ایک ارے پر مشتمل ہوگا۔ ہمیں نتیجہ کو اس طرح پروسیس کرنا ہوگا کہ یہ دیکھا جا سکے کہ آیا کوئی `tool_calls` موجود ہیں۔ اس سے ہمیں معلوم ہوتا ہے کہ LLM کسی مخصوص ٹول کو دلائل کے ساتھ کال کرنے کی درخواست کر رہا ہے۔ LLM کے جواب کو ہینڈل کرنے کے لیے ایک فنکشن کی تعریف کرنے کے لیے اپنے `main.rs` فائل کے نیچے مندرجہ ذیل کوڈ شامل کریں:

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

    // اگر دستیاب ہو تو مواد پرنٹ کریں
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ٹول کالز کو سنبھالیں
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // معاون پیغام شامل کریں

        // ہر ٹول کال کو انجام دیں
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // پیغامات میں ٹول کا نتیجہ شامل کریں
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ٹول کے نتائج کے ساتھ گفتگو جاری رکھیں
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

اگر `tool_calls` موجود ہوں، تو یہ ٹول کی معلومات نکالتا ہے، MCP سرور کو ٹول کی درخواست کے ساتھ کال کرتا ہے، اور نتائج کو گفتگو کے پیغامات میں شامل کرتا ہے۔ پھر یہ LLM کے ساتھ گفتگو جاری رکھتا ہے اور پیغامات اسسٹنٹ کے جواب اور ٹول کال کے نتائج کے ساتھ اپ ڈیٹ ہوتے ہیں۔

MCP کالز کے لیے LLM کی طرف سے واپس کیے گئے ٹول کال کی معلومات نکالنے کے لیے، ہم ایک اور ہیلپر فنکشن شامل کریں گے جو کال کرنے کے لیے درکار تمام چیزیں نکالے گا۔ اپنے `main.rs` فائل کے نیچے مندرجہ ذیل کوڈ شامل کریں:

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

تمام حصے جگہ پر ہونے کے بعد، ہم اب ابتدائی یوزر پرامپٹ کو ہینڈل کر سکتے ہیں اور LLM کو کال کر سکتے ہیں۔ اپنے `main` فنکشن کو اپ ڈیٹ کریں تاکہ درج ذیل کوڈ شامل ہو:

```rust
// ٹول کالز کے ساتھ ایل ایل ایم گفتگو
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

یہ ابتدائی یوزر پرامپٹ کے ساتھ LLM سے سوال کرے گا کہ دو نمبروں کا مجموعہ کیا ہے، اور یہ جواب کو پروسیس کرے گا تاکہ ٹول کالز کو متحرک طور پر ہینڈل کیا جا سکے۔

زبردست، آپ نے کر دکھایا!

## اسائنمنٹ

مشقی کوڈ لے کر سرور کو مزید ٹولز کے ساتھ تیار کریں۔ پھر ایک کلائنٹ بنائیں جس میں LLM ہو، جیسا کہ مشق میں تھا، اور مختلف پرامپٹس کے ساتھ اسے ٹیسٹ کریں تاکہ یہ یقینی بنایا جا سکے کہ آپ کے تمام سرور ٹولز متحرک طور پر کال ہو رہے ہیں۔ کلائنٹ بنانے کا یہ طریقہ صارف کو بہترین تجربہ فراہم کرتا ہے کیونکہ وہ مخصوص کلائنٹ کمانڈز کے بجائے پرامپٹس استعمال کر سکتے ہیں اور MCP سرور کی کالز سے بے خبر رہتے ہیں۔

## حل

[حل](/03-GettingStarted/03-llm-client/solution/README.md)

## اہم نکات

- اپنے کلائنٹ میں LLM شامل کرنے سے صارفین کے لیے MCP سرورز کے ساتھ بات چیت کا بہتر طریقہ فراہم ہوتا ہے۔
- آپ کو MCP سرور کے جواب کو ایسی شکل میں تبدیل کرنا ہوگا جو LLM سمجھ سکے۔

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.Net کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائتھن کیلکولیٹر](../../../../03-GettingStarted/samples/python)
- [رسٹ کیلکولیٹر](../../../../03-GettingStarted/samples/rust)

## اضافی وسائل

## آگے کیا ہے

- اگلا: [Visual Studio Code استعمال کرتے ہوئے سرور کا استعمال](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->