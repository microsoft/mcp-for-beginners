# ایل ایل ایم کے ساتھ کلائنٹ بنانا

اب تک، آپ نے ایک سرور اور کلائنٹ بنانے کا طریقہ دیکھا ہے۔ کلائنٹ واضح طور پر سرور کو کال کر کے اس کے ٹولز، وسائل اور پرامپٹس کی فہرست حاصل کر سکتا ہے۔ تاہم، یہ ایک زیادہ عملی طریقہ نہیں ہے۔ آپ کے صارفین ایجنٹک دور میں رہتے ہیں اور توقع کرتے ہیں کہ وہ پرامپٹس استعمال کریں اور ایل ایل ایم کے ساتھ بات چیت کریں۔ انہیں یہ پرواہ نہیں کہ آپ اپنی صلاحیتوں کو محفوظ کرنے کے لیے MCP استعمال کرتے ہیں یا نہیں؛ وہ صرف قدرتی زبان میں بات چیت کرنے کی توقع کرتے ہیں۔ تو ہم اسے کیسے حل کریں؟ حل یہ ہے کہ کلائنٹ میں ایل ایل ایم شامل کیا جائے۔

## جائزہ

اس سبق میں ہم کلائنٹ میں ایل ایل ایم شامل کرنے پر توجہ دیتے ہیں اور دکھاتے ہیں کہ یہ آپ کے صارف کے لیے بہتر تجربہ کیسے فراہم کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے آخر تک، آپ ان کاموں کے قابل ہو جائیں گے:

- ایل ایل ایم کے ساتھ کلائنٹ بنائیں۔
- ایل ایل ایم کا استعمال کرتے ہوئے MCP سرور کے ساتھ بغیر رکاوٹ بات چیت کریں۔
- کلائنٹ سائڈ پر بہتر اختتامی صارف تجربہ فراہم کریں۔

## طریقہ کار

آئیے سمجھنے کی کوشش کریں کہ ہمیں کون سا طریقہ اختیار کرنا ہے۔ ایل ایل ایم شامل کرنا آسان لگتا ہے، لیکن کیا ہم واقعی یہ کریں گے؟

یہاں بتایا گیا ہے کہ کلائنٹ سرور کے ساتھ کیسے بات چیت کرے گا:

1. سرور کے ساتھ کنکشن قائم کریں۔

1. صلاحیتوں، پرامپٹس، وسائل اور ٹولز کی فہرست بنائیں، اور ان کی اسکیمہ محفوظ کریں۔

1. ایک ایل ایل ایم شامل کریں اور محفوظ شدہ صلاحیتوں اور ان کی اسکیمہ کو ایل ایل ایم کو ایسے فارمیٹ میں دیں جو وہ سمجھتا ہو۔

1. صارف کے پرامپٹ کو اس ٹولز کے ساتھ ایل ایل ایم کو دیں جس کی کلائنٹ نے فہرست بنائی ہے۔

زبردست، اب ہم اعلی سطح پر سمجھ گئے کہ ہم یہ کیسے کر سکتے ہیں، آئیے نیچے مشق میں اسے آزما کر دیکھتے ہیں۔

## مشق: ایل ایل ایم کے ساتھ کلائنٹ بنانا

اس مشق میں، ہم سیکھیں گے کہ کلائنٹ میں ایل ایل ایم شامل کیسے کیا جائے۔

### GitHub پرسنل ایکسیس ٹوکن کے ذریعے تصدیق

GitHub ٹوکن بنانا ایک آسان عمل ہے۔ یہاں طریقہ ہے:

- GitHub کی ترتیبات پر جائیں – اوپر دائیں کونے میں اپنی پروفائل تصویر پر کلک کریں اور سیٹنگز منتخب کریں۔
- ڈیولپر سیٹنگز پر جائیں – نیچے اسکرول کریں اور Developer Settings پر کلک کریں۔
- پرسنل ایکسیس ٹوکن منتخب کریں – Fine-grained tokens پر کلک کریں اور پھر Generate new token کا انتخاب کریں۔
- اپنا ٹوکن ترتیب دیں – حوالہ کے لیے نوٹ شامل کریں، ایکسپائریشن تاریخ سیٹ کریں، اور ضروری اسکوپس (اجازتیں) منتخب کریں۔ اس صورت میں Models کی اجازت شامل کرنا یقینی بنائیں۔
- ٹوکن بنائیں اور کاپی کریں – Generate token پر کلک کریں، اور فوراً اسے کاپی کر لیں، کیونکہ آپ اسے دوبارہ نہیں دیکھ سکیں گے۔

### -1- سرور سے کنیکٹ ہونا

سب سے پہلے اپنا کلائنٹ بنائیں:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // اسکیمہ کی توثیق کے لیے zod درآمد کریں

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

مندرجہ بالا کوڈ میں ہم نے:

- ضروری لائبریریز درآمد کیں
- ایک کلاس بنائی جس میں دو ارکان، `client` اور `openai` ہیں جو ہمیں کلائنٹ اور ایل ایل ایم سے بات چیت کرنے میں مدد کریں گے۔
- اپنے ایل ایل ایم انسٹینس کو GitHub Models استعمال کرنے کے لیے ترتیب دیا، `baseUrl` کو inference API کی طرف پوائنٹ کرتے ہوئے۔

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# اسٹینڈ ان پٹ/آؤٹ پٹ کنکشن کے لیے سرور کے پیرامیٹرز بنائیں
server_params = StdioServerParameters(
    command="mcp",  # قابل عمل
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

مندرجہ بالا کوڈ میں ہم نے:

- MCP کے لیے درکار لائبریریز درآمد کیں
- ایک کلائنٹ تخلیق کیا

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

مندرجہ بالا کوڈ میں ہم نے:

- **LangChain4j dependencies شامل کیں**: MCP انٹیگریشن، OpenAI آفیشل کلائنٹ، اور GitHub Models کی سپورٹ کے لیے
- **LangChain4j لائبریریز درآمد کیں**: MCP انٹیگریشن اور OpenAI چیٹ ماڈل فنکشنالٹی کے لیے
- **`ChatLanguageModel` بنایا**: جسے آپ کے GitHub ٹوکن کے ساتھ GitHub Models استعمال کرنے کے لیے ترتیب دیا گیا
- **HTTP ٹرانسپورٹ سیٹ اپ کیا**: Server-Sent Events (SSE) استعمال کرتے ہوئے MCP سرور سے کنکشن کے لیے
- **MCP کلائنٹ بنایا**: جو سرور کے ساتھ مواصلت سنبھالے گا
- **LangChain4j کی بلٹ ان MCP سپورٹ استعمال کی**: جو LLMs اور MCP سرورز کے درمیان انٹیگریشن آسان بناتی ہے

#### Rust

اس مثال میں فرض کیا گیا ہے کہ آپ کے پاس Rust پر مبنی MCP سرور چل رہا ہے۔ اگر آپ کے پاس نہیں ہے، تو سرور بنانے کے لیے [01-first-server](../01-first-server/README.md) سبق دیکھیں۔

جب آپ کا Rust MCP سرور تیار ہو جائے، تو ٹرمینل کھولیں اور سرور کی ڈائریکٹری میں جائیں۔ پھر نیا LLM کلائنٹ پروجیکٹ بنانے کے لیے درج ذیل کمانڈ چلائیں:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

اپنی `Cargo.toml` فائل میں یہ dependencies شامل کریں:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI کے لیے کوئی رسمی Rust لائبریری نہیں ہے، تاہم `async-openai` کریٹ ایک [کمیونٹی کی دیکھ بھال والی لائبریری](https://platform.openai.com/docs/libraries/rust#rust) ہے جو عام طور پر استعمال ہوتی ہے۔

`src/main.rs` فائل کھولیں اور اس کا مواد درج ذیل کوڈ سے بدل دیں:

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

    // OpenAI کلائنٹ سیٹ اپ کریں
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP کلائنٹ سیٹ اپ کریں
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

    // TODO: MCP ٹول کی فہرست حاصل کریں

    // TODO: ٹول کالز کے ساتھ LLM گفتگو

    Ok(())
}
```

یہ کوڈ ایک بنیادی Rust ایپلیکیشن سیٹ اپ کرتا ہے جو MCP سرور اور GitHub Models سے LLM بات چیت کے لیے کنکٹ ہوتی ہے۔

> [!IMPORTANT]
> ایپلیکیشن چلانے سے پہلے `OPENAI_API_KEY` ماحول متغیر کو اپنے GitHub ٹوکن سے سیٹ کرنا یقینی بنائیں۔

زبردست، اگلے مرحلے کے لیے، آئیے سرور کی صلاحیتوں کی فہرست نکالتے ہیں۔

### -2- سرور کی صلاحیتوں کی فہرست بنائیں

اب ہم سرور سے کنیکٹ کریں گے اور اس کی صلاحیتیں پوچھیں گے:

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

    // اوزاروں کی فہرست بندی
    const toolsResult = await this.client.listTools();
}
```

مندرجہ بالا کوڈ میں ہم نے:

- سرور سے کنیکٹ کرنے کے لیے `connectToServer` کا کوڈ شامل کیا۔
- `run` طریقہ بنایا جو ایپلیکیشن کے فلو کو سنبھالتا ہے۔ اب تک یہ صرف ٹولز کی فہرست بناتا ہے لیکن مزید کام جلد شامل کریں گے۔

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

یہ ہم نے کیا:

- وسائل اور ٹولز کی فہرست بنائی اور پرنٹ کی۔ ٹولز کے لیے ہم `inputSchema` بھی لسٹ کرتے ہیں جسے بعد میں استعمال کریں گے۔

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

مندرجہ بالا کوڈ میں ہم نے:

- MCP سرور پر دستیاب ٹولز کی فہرست بنائی
- ہر ٹول کے لیے نام، تفصیل، اور اس کی اسکیمہ لسٹ کی، جسے ہم جلدی ٹولز کال کرنے کے لیے استعمال کریں گے۔

#### Java

```java
// ایک ٹول پرووائیڈر بنائیں جو خودکار طریقے سے MCP ٹولز کو دریافت کرے
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ٹول پرووائیڈر خودکار طریقے سے یہ کام کرتا ہے:
// - MCP سرور سے دستیاب ٹولز کی فہرست بنانا
// - MCP ٹول اسکیموں کو LangChain4j فارمیٹ میں تبدیل کرنا
// - ٹول کی عمل کاری اور جوابات کا انتظام کرنا
```

مندرجہ بالا کوڈ میں ہم نے:

- `McpToolProvider` بنایا جو خودکار طور پر MCP سرور سے تمام ٹولز دریافت اور رجسٹر کردیتا ہے
- ٹول پرووائڈر MCP ٹول اسکیمہ کو LangChain4j کے ٹول فارمیٹ میں خودکار طور پر تبدیل کرتا ہے
- اس طریقہ کار سے دستی ٹول لسٹنگ اور کنورژن کا کام ختم ہو جاتا ہے

#### Rust

MCP سرور سے ٹولز حاصل کرنے کے لیے `list_tools` طریقہ استعمال کریں۔ `main` فنکشن میں MCP کلائنٹ کے سیٹ اپ کے بعد یہ کوڈ شامل کریں:

```rust
// MCP ٹول کی فہرست حاصل کریں
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- سرور کی صلاحیتوں کو ایل ایل ایم کے ٹولز میں تبدیل کریں

سرور کی صلاحیتوں کی فہرست بنانے کے بعد اگلا قدم انہیں ایل ایل ایم کے سمجھنے والے فارمیٹ میں تبدیل کرنا ہے۔ جب یہ کر لیں تو ہم انہیں اپنے LLM کو ٹولز کے طور پر دے سکتے ہیں۔

#### TypeScript

1. MCP سرور سے جواب کو ایسے ٹول فارمیٹ میں تبدیل کرنے کے لیے درج ذیل کوڈ شامل کریں جو LLM سمجھ سکے:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ان پٹ_سکیما کی بنیاد پر زوڈ اسکیمہ بنائیں
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // قسم کو واضح طور پر "فنکشن" مقرر کریں
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

    اوپر دیا گیا کوڈ MCP سرور سے حاصل جوابی ڈیٹا لیتا ہے اور اسے ایسے ٹول تعریف فارمیٹ میں بدلتا ہے جو ایل ایل ایم سمجھ سکتا ہے۔

1. اب `run` طریقہ کو اپ ڈیٹ کریں تاکہ سرور کی صلاحیتوں کی فہرست بنائی جائے:

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

    اوپر دی گئی مثال میں ہم نے `run` طریقہ کو اپ ڈیٹ کیا ہے تاکہ نتائج کے لیے `openAiToolAdapter` کال کی جائے۔

#### Python

1. سب سے پہلے، یہ کنورٹر فنکشن بنائیں:

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

    `convert_to_llm_tools` فنکشن MCP ٹول کے جواب کو لیتا ہے اور اسے ایل ایل ایم کے لیے قابل فہم فارمیٹ میں تبدیل کرتا ہے۔

1. پھر کلائنٹ کوڈ میں اس فنکشن کو استعمال کریں:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    یہاں ہم MCP ٹول ردعمل کو ایل ایل ایم کو فراہم کرنے کے قابل بنانے کے لیے `convert_to_llm_tool` کال کر رہے ہیں۔

#### .NET

1. MCP ٹول جواب کو ایل ایل ایم کے قابل فہم بنانے کے لیے کوڈ شامل کریں:

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

مندرجہ بالا کوڈ میں ہم نے:

- `ConvertFrom` فنکشن بنایا جو نام، تفصیل اور ان پٹ اسکیمہ لیتا ہے۔
- ایک فنکشنلٹی بنائی جو `FunctionDefinition` تخلیق کرتی ہے جو `ChatCompletionsDefinition` کو پاس ہوتی ہے، جو ایل ایل ایم سمجھ سکتا ہے۔

1. اب موجودہ کوڈ کو اس فنکشن کے فائدے کے لیے اپ ڈیٹ کریں:

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

// AI سروس کو LLM اور MCP ٹولز کے ساتھ ترتیب دیں
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

مندرجہ بالا کوڈ میں ہم نے:

- قدرتی زبان میں بات چیت کے لیے ایک سادہ `Bot` انٹرفیس بنایا
- LangChain4j کے `AiServices` کا استعمال کیا تاکہ ایل ایل ایم کو MCP ٹول پرووائڈر کے ساتھ خودکار طور پر باندھا جا سکے
- فریم ورک خود بخود ٹول اسکیمہ کی تبدیلی اور فنکشن کال کے پیچیدہ عمل کو ہینڈل کرتا ہے
- اس طریقہ سے دستی ٹول کنورژن کا عمل ختم ہو جاتا ہے - LangChain4j تمام پیچیدگی سنبھال لیتا ہے

#### Rust

MCP ٹول جواب کو ایل ایل ایم کے سمجھنے والے فارمیٹ میں تبدیل کرنے کے لیے ہم ایک ہیلپر فنکشن شامل کریں گے جو ٹولز کی فہرست کو فارمیٹ کرے گا۔ `main.rs` فائل میں `main` فنکشن کے نیچے یہ کوڈ شامل کریں۔ یہ ایل ایل ایم کو درخواست کرتے وقت کال کیا جائے گا:

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

زبردست، اب ہم صارف کی درخواستیں سنبھالنے کے لیے تیار ہیں، تو آئیے اگلے مرحلے کی طرف بڑھیں۔

### -4- صارف کے پرامپٹ کی درخواست سنبھالیں

اس حصے میں، ہم صارف کی درخواستوں کو ہینڈل کریں گے۔

#### TypeScript

1. ایک طریقہ شامل کریں جو ایل ایل ایم کو کال کرے گا:

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
        // کرنا ہے

        }
    }
    ```

    اوپر کے کوڈ میں ہم نے:

    - `callTools` نامی طریقہ شامل کیا۔
    - یہ طریقہ ایل ایل ایم کے جواب کو دیکھتا ہے اور چیک کرتا ہے کہ کون سے ٹولز کال ہوئے ہیں، اگر کوئی ہوں:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // آلہ کو کال کریں
        }
        ```

    - اگر ایل ایل ایم کہے کہ کسی ٹول کو کال کیا جائے تو اسے کال کریں:

        ```typescript
        // 2۔ سرور کے ٹول کو کال کریں
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3۔ نتیجہ کے ساتھ کچھ کریں
        // جاری ہے
        ```

1. `run` طریقہ کو اپ ڈیٹ کریں تاکہ ایل ایل ایم کالز اور `callTools` شامل ہوں:

    ```typescript

    // 1۔ LLM کے لیے ان پٹ میسجز بنائیں
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2۔ LLM کو کال کرنا
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3۔ LLM کے جواب کا جائزہ لیں، ہر انتخاب کے لیے چیک کریں کہ آیا اس میں ٹول کالز ہیں
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

زبردست، پوری کوڈ کی فہرست دیکھیں:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // سکیمہ کی توثیق کے لیے زوڈ کو درآمد کریں

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
            type: "function" as const, // قسم کو صریحاً "function" پر سیٹ کریں
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
    
        // 1. ایل ایل ایم جواب کا جائزہ لیں، ہر انتخاب کے لیے چیک کریں کہ کیا اس میں ٹول کالز ہیں
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

1. ایل ایل ایم کال کرنے کے لیے کچھ ضروری امپورٹس شامل کریں:

    ```python
    # لم
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. پھر وہ فنکشن شامل کریں جو ایل ایل ایم کو کال کرے گا:

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

    اوپر کے کوڈ میں ہم نے:

    - MCP سرور سے ملنے والے فنکشنز کو ایل ایل ایم کو پاس کیا۔
    - پھر ایل ایل ایم کو کال کیا۔
    - نتیجہ دیکھا کہ کون سے فنکشنز کال کیے جانے چاہئیں۔
    - آخر میں بُلائے جانے والے فنکشنز کی فہرست پاس کی۔

1. آخری مرحلہ، اپنے مرکزی کوڈ کو اپ ڈیٹ کریں:

    ```python
    prompt = "Add 2 to 20"

    # اگر کوئی ہو تو، LLM سے پوچھیں کہ کون سے ٹولز استعمال کرنے ہیں
    functions_to_call = call_llm(prompt, functions)

    # تجویز کردہ افعال کو کال کریں
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    یہ آخری قدم تھا؛ مذکورہ بالا کوڈ میں ہم:

    - `call_tool` کے ذریعے MCP ٹول کال کر رہے ہیں جسے ایل ایل ایم نے تجویز کیا۔
    - سرور سے حاصل نتیجہ پرنٹ کر رہے ہیں۔

#### .NET

1. ایل ایل ایم پرامپٹ درخواست کے لیے کوڈ دیکھیں:

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

    اوپر کے کوڈ میں ہم نے:

    - MCP سرور سے ٹولز حاصل کیے، `var tools = await GetMcpTools()`.
    - صارف کا پرامپٹ `userMessage` بنایا۔
    - ماڈل اور ٹولز کی وضاحت کرتے ہوئے آپشنز آبجیکٹ تشکیل دیا۔
    - ایل ایل ایم کو درخواست کی۔

1. ایک آخری قدم، دیکھیں کہ کیا ایل ایل ایم سمجھتا ہے کہ فنکشن کال کرنی چاہیے:

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

    اوپر کے کوڈ میں ہم نے:

    - فنکشن کالز کی فہرست پر لوپ لگایا۔
    - ہر ٹول کال کے لیے نام اور دلائل نکالے اور MCP کلائنٹ کے ذریعے ٹول کال کیا۔ پھر نتیجہ پرنٹ کیا۔

یہ مکمل کوڈ ہے:

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

مندرجہ بالا میں ہم نے:

- سادہ قدرتی زبان کے پرامپٹس استعمال کر کے MCP سرور کے ٹولز کے ساتھ بات چیت کی
- LangChain4j فریم ورک خودکار طور پر سنبھالتا ہے:
  - صارف کے پرامپٹس کو ضرورت کے مطابق ٹول کالز میں تبدیل کرنا
  - ایل ایل ایم کے فیصلے کی بنیاد پر مناسب MCP ٹولز کال کرنا
  - ایل ایل ایم اور MCP سرور کے درمیان بات چیت کے بہاؤ کو منظم کرنا
- `bot.chat()` طریقہ ایسے قدرتی زبان کے جوابات دیتا ہے جو MCP ٹولز کے نتائج بھی شامل کر سکتے ہیں
- اس طریقے سے صارف کو ایک ہموار تجربہ ملتا ہے جس میں انہیں MCP کا عمل جاننے کی ضرورت نہیں ہوتی

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

یہاں زیادہ تر کام ہوتا ہے۔ ہم ابتدائی صارف پرامپٹ کے ساتھ ایل ایل ایم کو کال کریں گے، پھر جواب کا جائزہ لیں گے کہ آیا کوئی ٹول کال کرنا ہے یا نہیں۔ اگر ہاں، تو ان ٹولز کو کال کریں گے اور بات چیت ایل ایل ایم کے ساتھ جاری رکھیں گے جب تک مزید ٹول کالز کی ضرورت نہ ہو اور ہمیں ایک حتمی جواب مل جائے۔

ہم ایل ایل ایم کو متعدد بار کال کریں گے، تو آئیے ایک فنکشن ڈیفائن کرتے ہیں جو ایل ایل ایم کال کو ہینڈل کرے گا۔ `main.rs` فائل میں درج ذیل فنکشن شامل کریں:

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

یہ فنکشن ایل ایل ایم کلائنٹ، پیغامات کی فہرست (جس میں صارف کا پرامپٹ شامل ہے)، MCP سرور کے ٹولز لیتا ہے، اور ایل ایل ایم کو درخواست بھیج کر جواب لوٹاتا ہے۔
LLM سے موصول ہونے والا جواب `choices` کے ایک ارے پر مشتمل ہوگا۔ ہمیں نتیجہ پراسیس کرنا ہوگا تاکہ دیکھا جا سکے کہ کوئی `tool_calls` موجود ہیں یا نہیں۔ اس سے ہمیں پتہ چلتا ہے کہ LLM ایک مخصوص ٹول کے کال کرنے کی درخواست کر رہا ہے جس کے ساتھ دلائل ہوتے ہیں۔ اپنے `main.rs` فائل کے نیچے درج ذیل کوڈ شامل کریں تاکہ LLM کے جواب کو ہینڈل کرنے کے لیے ایک فنکشن define کیا جا سکے:

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

            // ٹول کے نتائج کو پیغامات میں شامل کریں
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

اگر `tool_calls` موجود ہوں، تو یہ ٹول کی معلومات نکالتا ہے، MCP سرور کو ٹول کی درخواست کے ساتھ کال کرتا ہے، اور گفتگو کے پیغامات میں نتائج شامل کرتا ہے۔ پھر گفتگو LLM کے ساتھ جاری رہتی ہے اور اسسٹنٹ کے جواب اور ٹول کال کے نتائج کے ساتھ پیغامات اپ ڈیٹ ہو جاتے ہیں۔

MCP کالز کے لیے LLM کی جانب سے واپس کیے گئے ٹول کال کی معلومات نکالنے کے لیے، ہم ایک اور helper فنکشن شامل کریں گے جو کال کرنے کے لیے درکار تمام چیزیں نکالے گا۔ اپنے `main.rs` فائل کے نیچے درج ذیل کوڈ شامل کریں:

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

تمام حصے جگہ پر ہونے کے بعد، ہم اب ابتدائی صارف کے پرامپٹ کو ہینڈل کر کے LLM کو کال کر سکتے ہیں۔ اپنے `main` فنکشن کو درج ذیل کوڈ شامل کرتے ہوئے اپ ڈیٹ کریں:

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

یہ ابتدائی صارف کے پرامپٹ کے ساتھ LLM کو سوال کرے گا کہ دو نمبروں کا مجموعہ کیا ہے، اور جواب کو پراسیس کرے گا تاکہ ٹول کالز کو متحرک طور پر ہینڈل کیا جا سکے۔

زبردست، آپ نے کر لیا!

## اسائنمنٹ

ورزش سے کوڈ لیں اور سرور کو کچھ مزید ٹولز کے ساتھ ڈیولپ کریں۔ پھر ایک LLM کلائنٹ بنائیں، جیسا کہ ورزش میں کیا گیا ہے، اور مختلف پرامپٹس کے ساتھ اسے ٹیسٹ کریں تاکہ یقینی بنایا جا سکے کہ آپ کے تمام سرور ٹولز متحرک طور پر کال ہو رہے ہیں۔ اس طرح کلائنٹ بنانے کا مطلب ہوتا ہے کہ آخری صارف کو بہترین صارف تجربہ ملے گا کیونکہ وہ پرامپٹس استعمال کر سکتے ہیں بجائے اس کے کہ بالکل کلائنٹ کمانڈز استعمال کرے، اور وہ MCP سرور کے کال ہونے سے غافل رہے گا۔

## حل

[Solution](./solution/README.md)

## اہم نکات

- اپنے کلائنٹ میں LLM شامل کرنے سے صارفین کو MCP سرورز کے ساتھ بات چیت کرنے کا بہتر طریقہ ملتا ہے۔
- آپ کو MCP سرور کے جواب کو ایسی شکل میں تبدیل کرنا ہوگی جو LLM سمجھ سکے۔

## نمونے

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## اضافی وسائل

## آگے کیا ہے

- اگلا: [Visual Studio Code کے استعمال سے سرور کو استعمال کرنا](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلانِ ذمہ داری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہِ کرم اس بات کا خیال رکھیں کہ خودکار تراجم میں غلطیاں یا نا درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں قابلِ بھروسہ ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمہ کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تعبیرات کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->