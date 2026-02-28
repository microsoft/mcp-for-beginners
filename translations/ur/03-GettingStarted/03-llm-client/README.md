# LLM کے ساتھ کلائنٹ بنانا

اب تک، آپ نے دیکھا ہے کہ کس طرح سرور اور کلائنٹ بنائیں۔ کلائنٹ سرور کو واضح طور پر کال کر کے اس کے ٹولز، وسائل، اور پرامپٹس کی فہرست حاصل کر سکتا تھا۔ تاہم، یہ طریقہ بہت عملی نہیں ہے۔ آپ کے صارفین ایجنٹک دور میں رہتے ہیں اور توقع کرتے ہیں کہ وہ پرامپٹس کا استعمال کریں اور ایک LLM کے ساتھ بات چیت کریں۔ انہیں اس بات کی پرواہ نہیں کہ آپ MCP کا استعمال اپنے صلاحیتوں کو ذخیرہ کرنے کے لیے کرتے ہیں؛ وہ صرف قدرتی زبان کے ذریعے بات چیت کی توقع رکھتے ہیں۔ تو ہم اسے کیسے حل کریں؟ حل یہ ہے کہ کلائنٹ میں ایک LLM شامل کیا جائے۔

## جائزہ

اس سبق میں ہم اپنے کلائنٹ میں LLM شامل کرنے پر توجہ دیں گے اور دکھائیں گے کہ یہ صارف کے لیے بہتر تجربہ کیسے فراہم کرتا ہے۔

## تعلیمی مقاصد

اس سبق کے آخر تک، آپ قابل ہوں گے:

- ایک LLM کے ساتھ کلائنٹ بنانا۔
- MCP سرور کے ساتھ LLM استعمال کر کے بغیر کسی رکاوٹ کے تعامل کرنا۔
- کلائنٹ سائڈ پر بہتر اختتامی صارف تجربہ فراہم کرنا۔

## طریقہ کار

آئیے سمجھنے کی کوشش کریں کہ ہمیں کون سا طریقہ اختیار کرنا چاہیے۔ LLM شامل کرنا آسان لگتا ہے، لیکن کیا آپ واقعی ایسا کریں گے؟

یہاں بتایا گیا ہے کہ کلائنٹ سرور کے ساتھ کیسے تعامل کرے گا:

1. سرور سے کنکشن قائم کریں۔

1. صلاحیتیں، پرامپٹس، وسائل اور ٹولز کی فہرست بنائیں، اور ان کا اسکیمہ محفوظ کریں۔

1. ایک LLM شامل کریں اور محفوظ شدہ صلاحیتیں اور ان کا اسکیمہ LLM کو سمجھ آنے والے فارمیٹ میں پاس کریں۔

1. صارف کے پرامپٹ کو ہینڈل کریں اور اسے کلائنٹ کی جانب سے فہرست کردہ ٹولز کے ساتھ LLM کو پاس کریں۔

بہت خوب، اب جب کہ ہم نے اعلی سطح پر سمجھ لیا کہ یہ کیسے کیا جا سکتا ہے، آئیے ذیل کے مشق میں اسے آزما کر دیکھتے ہیں۔

## مشق: LLM کے ساتھ کلائنٹ بنانا

اس مشق میں، ہم اپنے کلائنٹ میں ایک LLM شامل کرنا سیکھیں گے۔

### گٹ ہب پرسنل ایکسیس ٹوکن کے ذریعے تصدیق

گٹ ہب ٹوکن بنانا ایک آسان عمل ہے۔ یہاں بتایا گیا ہے کہ آپ یہ کیسے کر سکتے ہیں:

- GitHub Settings پر جائیں – اپنے پروفائل تصویر پر اوپر دائیں کونے میں کلک کریں اور Settings منتخب کریں۔
- Developer Settings پر جائیں – نیچے سکرول کریں اور Developer Settings پر کلک کریں۔
- Personal Access Tokens منتخب کریں – Fine-grained tokens پر کلک کریں اور پھر Generate new token پر کلک کریں۔
- اپنا ٹوکن ترتیب دیں – حوالہ کے لیے نوٹ شامل کریں، ایک معیاد تاریخ مقرر کریں، اور ضروری scopes (اجازتیں) منتخب کریں۔ اس کیس میں Models کی اجازت ضرور شامل کریں۔
- ٹوکن بنائیں اور کاپی کریں – Generate token پر کلک کریں اور اسے فوراً کاپی کر لیں، کیونکہ آپ اسے دوبارہ نہیں دیکھ سکیں گے۔

### -1- سرور سے کنکٹ ہونا

آئیے پہلے اپنا کلائنٹ بنائیں:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // سکیمہ کی تصدیق کے لیے zod کو درآمد کریں

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
- ایک کلاس بنائی جس میں دو ممبرز `client` اور `openai` ہیں جو کلائنٹ کو منظم کرنے اور LLM کے ساتھ بات چیت کرنے میں مدد دیں گے۔
- اپنے LLM انسٹانس کو GitHub Models استعمال کرنے کے لیے کنفیگر کیا، `baseUrl` کو inference API کی طرف اشارہ کرتے ہوئے۔

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# اسٹڈیو کنکشن کے لیے سرور کے پیرا میٹر بنائیں
server_params = StdioServerParameters(
    command="mcp",  # قابلِ اجرایہ
    args=["run", "server.py"],  # اختیاری کمانڈ لائن دلائل
    env=None,  # اختیاری ماحولیاتی متغیرات
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

سب سے پہلے، آپ کو اپنی `pom.xml` فائل میں LangChain4j کے dependencies شامل کرنے ہوں گے۔ MCP انٹیگریشن اور GitHub Models کی سپورٹ کے لیے یہ dependencies شامل کریں:

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

پھر اپنی Java کلائنٹ کلاس بنائیں:

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

        // سرور سے جڑنے کے لیے MCP ٹرانسپورٹ بنائیں
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP کلائنٹ بنائیں
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

پچھلے کوڈ میں ہم نے:

- **LangChain4j dependencies شامل کیں**: MCP انٹیگریشن، OpenAI آفیشل کلائنٹ، اور GitHub Models کی سپورٹ کے لیے
- **LangChain4j لائبریریاں امپورٹ کیں**: MCP انٹیگریشن اور OpenAI چیٹ ماڈل افعال کے لیے
- **`ChatLanguageModel` بنایا**: GitHub Models استعمال کرنے کے لیے آپ کے GitHub ٹوکن کے ساتھ کنفیگر کیا گیا
- **HTTP ٹرانسپورٹ سیٹ کیا**: Server-Sent Events (SSE) استعمال کرتے ہوئے MCP سرور سے کنیکٹ کرنے کے لیے
- **MCP کلائنٹ بنایا**: جو سرور کے ساتھ بات چیت سنبھالے گا
- **LangChain4j کی بلٹ ان MCP سپورٹ استعمال کی**: جو LLMs اور MCP سرورز کے درمیان انٹیگریشن کو آسان بناتی ہے

#### Rust

یہ مثال فرض کرتی ہے کہ آپ کے پاس ایک Rust پر مبنی MCP سرور چل رہا ہے۔ اگر آپ کے پاس نہیں ہے، تو سرور بنانے کے لیے [01-first-server](../01-first-server/README.md) سبق دیکھیں۔

جب آپ کے پاس اپنا Rust MCP سرور ہو، تو ٹرمینل کھولیں اور سرور والی ڈائریکٹری میں جائیں۔ پھر نیچے دیا گیا کمانڈ چلائیں تاکہ نیا LLM کلائنٹ پروجیکٹ بنایا جا سکے:

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
> OpenAI کے لیے Rust کی کوئی آفیشل لائبریری نہیں ہے، تاہم `async-openai` کریٹ ایک [کمیونٹی کی جانب سے برقرار رکھی گئی لائبریری](https://platform.openai.com/docs/libraries/rust#rust) ہے جو عام طور پر استعمال ہوتی ہے۔

`src/main.rs` فائل کھولیں اور اس کا مواد درج ذیل کوڈ سے بدلیں:

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

    // اوپن اے آئی کلائنٹ کا سیٹ اپ کریں
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // ایم سی پی کلائنٹ کا سیٹ اپ کریں
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

    // کرنا ہے: ایم سی پی ٹول کی فہرست حاصل کریں

    // کرنا ہے: ٹول کالز کے ساتھ ایل ایل ایم گفتگو

    Ok(())
}
```

یہ کوڈ ایک بنیادی Rust ایپلیکیشن سیٹ اپ کرتا ہے جو MCP سرور اور GitHub Models سے LLM بات چیت کرے گا۔

> [!IMPORTANT]
> ایپلیکیشن چلانے سے پہلے `OPENAI_API_KEY` انوائرنمنٹ ویریبل کو اپنے GitHub ٹوکن سے سیٹ کرنا یقینی بنائیں۔

بہت خوب، اگلا مرحلہ یہ ہے کہ سرور کی صلاحیتیں فہرست کریں۔

### -2- سرور کی صلاحیتوں کی فہرست بنائیں

اب ہم سرور سے کنیکٹ ہوں گے اور اس کی صلاحیتیں دریافت کریں گے:

#### Typescript

اسی کلاس میں درج ذیل میتھڈز شامل کریں:

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

- سرور سے کنکٹ ہونے کا کوڈ شامل کیا، `connectToServer`۔
- `run` میتھڈ بنایا جو ہمارے ایپ فلو کو سنبھالتا ہے۔ اب تک یہ صرف ٹولز کی فہرست دکھاتا ہے لیکن ہم جلد ہی اس میں مزید شامل کریں گے۔

#### Python

```python
# دستیاب وسائل کی فہرست بنائیں
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# دستیاب اوزار کی فہرست بنائیں
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

یہاں ہم نے کیا کیا:

- وسائل اور ٹولز کی فہرست بنائی اور پرنٹ کیا۔ ٹولز کے لیے ہم نے `inputSchema` بھی شامل کیا جو بعد میں استعمال کریں گے۔

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
- ہر ٹول کے لیے نام، تفصیل اور اس کا اسکیمہ شامل کیا۔ یہ اسکیمہ ہم بعد میں ٹولز کال کرنے کے لیے استعمال کریں گے۔

#### Java

```java
// ایک ٹول فراہم کنندہ تیار کریں جو خود بخود MCP ٹولز کو دریافت کرے
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ٹول فراہم کنندہ خود بخود مندرجہ ذیل کام انجام دیتا ہے:
// - MCP سرور سے دستیاب ٹولز کی فہرست بنانا
// - MCP ٹول اسکیموں کو LangChain4j فارمیٹ میں تبدیل کرنا
// - ٹول کی اجرایٔ اور جوابات کا انتظام کرنا
```

پچھلے کوڈ میں ہم نے:

- ایک `McpToolProvider` بنایا جو خودبخود MCP سرور سے تمام ٹولز دریافت اور رجسٹر کرتا ہے
- ٹول پرووائیڈر MCP ٹول اسکیموں کو اندرونی طور پر LangChain4j کے ٹول فارمیٹ میں تبدیل کرتا ہے
- یہ طریقہ کار دستی ٹول لسٹنگ اور تبدیلی کے عمل کو غیر ضروری بنا دیتا ہے

#### Rust

MCP سرور سے ٹولز حاصل کرنے کے لیے `list_tools` میتھڈ استعمال کی جاتی ہے۔ اپنے `main` فنکشن میں، MCP کلائنٹ سیٹ اپ کرنے کے بعد، یہ کوڈ شامل کریں:

```rust
// ایم سی پی ٹول کی فہرست حاصل کریں
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- سرور صلاحیتوں کو LLM ٹولز میں تبدیل کریں

سرور صلاحیتوں کی فہرست بنانے کے بعد اگلا قدم یہ ہے کہ انہیں ایسے فارمیٹ میں تبدیل کیا جائے جو LLM سمجھ سکے۔ جب ہم یہ کر لیں، تو ہم یہ صلاحیتیں اپنے LLM کو ٹولز کے طور پر فراہم کر سکتے ہیں۔

#### TypeScript

1. درج ذیل کوڈ شامل کریں جو MCP سرور کے ریسپانس کو ایسی فارمیٹ میں تبدیل کرے جو LLM استعمال کر سکے:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ان پٹ_سکیما کی بنیاد پر زوڈ اسکیمہ بنائیں
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // قسم کو واضح طور پر "function" پر سیٹ کریں
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

    یہ کوڈ MCP سرور کے ریسپانس کو لے کر LLM کے لیے قابل فہم ٹول ڈیفینیشن فارمیٹ میں تبدیل کرتا ہے۔

1. اب `run` میتھڈ کو اپ ڈیٹ کریں تاکہ سرور کی صلاحیتوں کی فہرست دکھا سکے:

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

    پچھلے کوڈ میں ہم نے `run` میتھڈ کو اپ ڈیٹ کیا ہے تاکہ نتیجے میں سے ہر انٹری کے لیے `openAiToolAdapter` کال ہو۔

#### Python

1. پہلے، درج ذیل کنورٹر فنکشن بنائیں:

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

    `convert_to_llm_tools` فنکشن میں ہم MCP ٹول ریسپانس کو ایسے فارمیٹ میں تبدیل کرتے ہیں جو LLM سمجھ سکتا ہے۔

1. اگلے، کلائنٹ کوڈ کو اپ ڈیٹ کریں تاکہ یہ فنکشن استعمال ہو:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    یہاں ہم `convert_to_llm_tool` کال شامل کر رہے ہیں تاکہ MCP ٹول ریسپانس کو ایک ایسی چیز میں تبدیل کیا جا سکے جو بعد میں LLM کو دی جا سکے۔

#### .NET

1. MCP ٹول ریسپانس کو LLM کے قابل فہم شکل میں تبدیل کرنے کا کوڈ شامل کریں:

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

- `ConvertFrom` فنکشن بنایا جو نام، تفصیل، اور ان پٹ اسکیمہ لیتا ہے۔
- فنکشن کی تعریف کی جو `FunctionDefinition` بناتی ہے جو `ChatCompletionsDefinition` کو پاس ہوتی ہے۔ یہ وہ چیز ہے جو LLM سمجھتا ہے۔

1. اب موجودہ کوڈ کو اپ ڈیٹ کرنے کا طریقہ دیکھتے ہیں تاکہ اس فنکشن سے فائدہ اٹھایا جا سکے:

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

// LLM اور MCP آلات کے ساتھ AI سروس کو تشکیل دیں
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

پچھلے کوڈ میں ہم نے:

- قدرتی زبان کے تبادلے کے لیے ایک سادہ `Bot` انٹرفیس ڈیفائن کی
- LangChain4j کے `AiServices` استعمال کیے تاکہ خودبخود LLM کو MCP ٹول پرووائیڈر کے ساتھ منسلک کیا جا سکے
- فریم ورک خود بخود ٹول اسکیمہ تبدیلی اور فنکشن کالنگ کو پس منظر میں سنبھالتا ہے
- یہ طریقہ کار دستی ٹول تبدیلی کو ختم کر دیتا ہے – LangChain4j MCP ٹولز کو LLM-مطابق فارمیٹ میں تبدیل کرنے کی تمام پیچیدگی سنبھالتا ہے

#### Rust

MCP ٹول ریسپانس کو ایسی شکل میں تبدیل کرنے کے لیے جو LLM سمجھ سکے، ہم ایک ہیلپر فنکشن شامل کریں گے جو ٹولز کی فہرست فارمیٹ کرے گا۔ یہ کوڈ اپنی `main.rs` فائل میں `main` فنکشن کے نیچے شامل کریں۔ یہ فنکشن LLM کو درخواست بھیجتے وقت کال کیا جائے گا:

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

بہت خوب، اب ہم صارف کی درخواستوں کو ہینڈل کرنے کے لیے تیار ہیں، تو آئیے اگلے مرحلے کو دیکھتے ہیں۔

### -4- صارف کے پرامپٹ کی درخواست ہینڈل کریں

اس کوڈ کے حصے میں، ہم صارف کی درخواستوں کو سنبھالیں گے۔

#### TypeScript

1. ایک میتھڈ شامل کریں جو ہمارے LLM کو کال کرے گا:

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

        // ۳۔ نتیجے کے ساتھ کچھ کریں
        // کرنے کے لیے

        }
    }
    ```

    پچھلے کوڈ میں ہم نے:

    - `callTools` میتھڈ شامل کیا۔
    - اس میتھڈ میں LLM کے ریسپانس کو لیا جاتا ہے اور دیکھا جاتا ہے کہ کون سے ٹولز کال ہوئے ہیں، اگر کوئی ہیں:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // آلہ کال کریں
        }
        ```

    - اگر LLM نے کسی ٹول کو کال کرنا بتایا تو اسے کال کریں:

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

1. `run` میتھڈ کو اپ ڈیٹ کریں تاکہ LLM کو کال کرے اور `callTools` کو کال کرے:

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
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM کے جواب کا جائزہ لیں، ہر انتخاب کے لیے چیک کریں کہ اس میں ٹول کالز ہیں یا نہیں
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

زبردست، اب مکمل کوڈ دیکھیں:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // اسکیمہ کی توثیق کے لیے zod درآمد کریں

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // مستقبل میں شاید اس URL کو تبدیل کرنے کی ضرورت ہو: https://models.github.ai/inference
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
          // input_schema کی بنیاد پر zod اسکیمہ بنائیں
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // قسم کو واضح طور پر "function" پر سیٹ کریں
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
    
    
          // 2. سرور کے ٹول کو کال کریں
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. نتیجہ کے ساتھ کچھ کریں
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM کے جواب کو دیکھیں، ہر انتخاب کے لیے چیک کریں کہ آیا اس میں ٹول کالز ہیں
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

1. LLM کو کال کرنے کے لیے ضروری امپورٹس شامل کریں:

    ```python
    # ایل ایل ایم
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. اب وہ فنکشن شامل کریں جو LLM کو کال کرے گا:

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

    - اپنے فنکشنز جو MCP سرور سے ملے اور تبدیل کیے گئے، LLM کو دیے۔
    - پھر LLM کو کال کیا۔
    - نتیجہ چیک کیا کہ کون سے فنکشنز کال کرنے چاہییں۔
    - آخر میں کال کرنے والے فنکشنز کی آرے پاس کی گئی۔

1. آخری مرحلہ، اپنا مرکزی کوڈ اپ ڈیٹ کریں:

    ```python
    prompt = "Add 2 to 20"

    # اگر کوئی ہوں تو تمام کے لیے آلات کے بارے میں LLM سے پوچھیں
    functions_to_call = call_llm(prompt, functions)

    # تجویز کردہ فنکشنز کو کال کریں
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    یہ آخری قدم تھا، اوپر کوڈ میں ہم:

    - LLM کے پرامپٹ پر عمل کرتے ہوئے `call_tool` کے ذریعے MCP ٹول کو کال کر رہے ہیں۔
    - ٹول کال کا نتیجہ MCP سرور پر پرنٹ کر رہے ہیں۔

#### .NET

1. LLM پرامپٹ درخواست کا کوڈ:

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

    پچھلے کوڈ میں ہم نے:

    - MCP سرور سے ٹولز حاصل کیے، `var tools = await GetMcpTools()`۔
    - صارف کا پرامپٹ `userMessage` ڈیفائن کیا۔
    - ماڈل اور ٹولز کے ساتھ آپشن آبجیکٹ بنایا۔
    - LLM کو درخواست بھیجی۔

1. آخری مرحلہ، چیک کریں کہ کیا LLM نے فنکشن کال کی تجویز دی ہے:

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

    - فنکشن کالز کی فہرست پر لوپ لگائی۔
    - ہر ٹول کال کے لیے نام اور دلیل نکالی اور MCP کلائنٹ استعمال کرتے ہوئے ٹول کال کی، پھر نتیجہ پرنٹ کیا۔

مکمل کوڈ دیکھیں:

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

- MCP سرور کے ٹولز سے بات چیت کے لیے سادہ قدرتی زبان کے پرامپٹس استعمال کیے
- LangChain4j فریم ورک خود بخود ہینڈل کرتا ہے:
  - جہاں ضرورت ہو، صارف کے پرامپٹس کو ٹول کالز میں تبدیل کرنا
  - LLM کے فیصلے کی بنیاد پر مناسب MCP ٹول کالز کرنا
  - LLM اور MCP سرور کے درمیان بات چیت کا انتظام
- `bot.chat()` میتھڈ قدرتی زبان میں جواب دیتا ہے جس میں MCP ٹولز کے نتائج شامل ہو سکتے ہیں
- یہ طریقہ کار ایک مربوط صارف تجربہ فراہم کرتا ہے جہاں صارفین کو MCP کی تفصیلات معلوم کرنے کی ضرورت نہیں ہوتی

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

یہ وہ حصہ ہے جہاں زیادہ تر کام ہوتا ہے۔ ہم ابتدائی صارف کے پرامپٹ کے ساتھ LLM کو کال کریں گے، پھر جواب کا جائزہ لیں گے کہ کیا کسی ٹول کو کال کرنے کی ضرورت ہے۔ اگر ہاں، تو ہم وہ ٹولز کال کریں گے اور LLM کے ساتھ بات چیت جاری رکھیں گے جب تک مزید ٹول کال کی ضرورت نہ رہے اور ہمیں حتمی جواب نہ مل جائے۔

ہم متعدد بار LLM کو کال کریں گے، لہٰذا آئیے ایک ایسا فنکشن ڈیفائن کرتے ہیں جو LLM کال کو سنبھالے۔ درج ذیل فنکشن اپنی `main.rs` فائل میں شامل کریں:

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

یہ فنکشن LLM کلائنٹ، پیغامات کی فہرست (جس میں صارف کا پرامپٹ بھی شامل ہے)، MCP سرور کے ٹولز لیتا ہے اور LLM کو درخواست بھیجتا ہے، پھر جواب واپس کرتا ہے۔
LLM کا جواب `choices` کے ایک صف پر مشتمل ہوگا۔ ہمیں نتیجہ پراسیس کرنا ہوگا تاکہ یہ دیکھا جا سکے کہ کیا کوئی `tool_calls` موجود ہیں۔ یہ ہمیں بتاتا ہے کہ LLM کسی مخصوص ٹول کو دلائل کے ساتھ کال کرنے کی درخواست کر رہا ہے۔ LLM کے جواب کو ہینڈل کرنے کے لیے اپنے `main.rs` فائل کے آخر میں درج ذیل کوڈ شامل کریں:

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

    // مواد پرنٹ کریں اگر دستیاب ہو
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ٹول کالز کو سنبھالیں
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // اسسٹنٹ کا پیغام شامل کریں

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

        // ٹول کے نتائج کے ساتھ بات چیت جاری رکھیں
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


اگر `tool_calls` موجود ہیں، تو یہ ٹول کی معلومات اخذ کرتا ہے، ٹول کی درخواست کے ساتھ MCP سرور کو کال کرتا ہے، اور نتائج کو گفتگو کے پیغامات میں شامل کرتا ہے۔ پھر یہ LLM کے ساتھ گفتگو جاری رکھتا ہے اور پیغامات کو اسسٹنٹ کے جواب اور ٹول کال کے نتائج کے ساتھ اپ ڈیٹ کر دیتا ہے۔

MCP کالز کے لیے LLM کی طرف سے واپس کیے گئے ٹول کال کی معلومات کو استخراج کرنے کے لیے، ہم ایک اور ہیلپر فنکشن شامل کریں گے جو کال کرنے کے لیے درکار تمام چیزیں نکال لے گا۔ اپنے `main.rs` فائل کے آخر میں درج ذیل کوڈ شامل کریں:

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


تمام حصے جگہ پر آ جانے کے بعد، ہم اب ابتدائی یوزر پرامپٹ کو ہینڈل کر سکتے ہیں اور LLM کو کال کر سکتے ہیں۔ اپنے `main` فنکشن کو اپ ڈیٹ کریں تاکہ درج ذیل کوڈ شامل ہو:

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


یہ ابتدائی یوزر پرامپٹ کے ساتھ LLM کو استفسار کرے گا، کہ دو نمبروں کا مجموعہ بتائے، اور جواب کو پراسیس کرے گا تاکہ ٹول کالز کو متحرک طریقے سے ہینڈل کیا جا سکے۔

زبردست، آپ نے کر دکھایا!

## اسائنمنٹ

مشقی کوڈ لے کر سرور میں مزید ٹولز شامل کریں۔ پھر ایک کلائنٹ بنائیں جس میں LLM ہو، جیسے مشق میں، اور مختلف پرامپٹس کے ساتھ اسے ٹیسٹ کریں تاکہ یہ یقینی بنایا جا سکے کہ آپ کے تمام سرور ٹولز متحرک طور پر کال ہو رہے ہیں۔ کلائنٹ بنانے کا یہ طریقہ کار اختتامی صارف کو ایک بہترین تجربہ فراہم کرتا ہے کیونکہ وہ کلائنٹ کمانڈز کے بجائے پرامپٹس استعمال کر سکتے ہیں اور انہیں MCP سرور کی کالنگ کا احساس نہیں ہوتا۔

## حل

[حل](/03-GettingStarted/03-llm-client/solution/README.md)

## اہم نکات

- اپنے کلائنٹ میں LLM شامل کرنے سے صارفین کو MCP سرورز کے ساتھ بہتر انٹریکشن کا طریقہ ملتا ہے۔
- آپ کو MCP سرور کے جواب کو ایسی شکل میں تبدیل کرنا پڑتا ہے جو LLM سمجھ سکے۔

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.نیٹ کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائتھن کیلکولیٹر](../../../../03-GettingStarted/samples/python)
- [رسٹ کیلکولیٹر](../../../../03-GettingStarted/samples/rust)

## اضافی وسائل

## آگے کیا ہے

- اگلا: [ویژوئل اسٹوڈیو کوڈ استعمال کرتے ہوئے سرور سے کنزیوم کرنا](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**انتباہ**:  
یہ دستاویز AI ترجمہ خدمت [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا نابہتیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->