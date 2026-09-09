# LLM کے ساتھ کلائنٹ بنانا

اب تک، آپ نے دیکھا ہے کہ سرور اور کلائنٹ کیسے بنانا ہے۔ کلائنٹ سرور کو واضح طور پر کال کر کے اس کے ٹولز، وسائل، اور پرامپٹس کی فہرست حاصل کرنے کے قابل رہا ہے۔ تاہم، یہ ایک بہت عملی طریقہ نہیں ہے۔ آپ کے صارفین ایجنٹک دور میں رہتے ہیں اور توقع کرتے ہیں کہ وہ پرامپٹس استعمال کریں اور ایک LLM کے ساتھ بات چیت کریں۔ وہ اس بات کی پرواہ نہیں کرتے کہ آپ اپنی صلاحیتوں کو اسٹور کرنے کے لیے MCP استعمال کرتے ہیں یا نہیں؛ وہ بس فطری زبان میں بات چیت کی توقع رکھتے ہیں۔ تو ہم اسے کیسے حل کریں؟ حل یہ ہے کہ کلائنٹ میں ایک LLM شامل کیا جائے۔

## جائزہ

اس سبق میں ہم اپنے کلائنٹ میں LLM شامل کرنے پر توجہ دیتے ہیں اور دکھاتے ہیں کہ یہ آپ کے صارف کے لیے کس طرح ایک بہتر تجربہ فراہم کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے آخر تک، آپ قابل ہوں گے کہ:

- LLM کے ساتھ ایک کلائنٹ بنائیں۔
- LLM استعمال کرتے ہوئے بغیر کسی رکاوٹ کے MCP سرور کے ساتھ بات چیت کریں۔
- کلائنٹ کی جانب سے ایک بہتر اختتامی صارف کا تجربہ فراہم کریں۔

## طریقہ کار

آئیے وہ طریقہ سمجھنے کی کوشش کریں جو ہمیں اختیار کرنا ہے۔ LLM شامل کرنا آسان لگتا ہے، لیکن کیا ہم واقعی ایسا کریں گے؟

کلائنٹ سرور کے ساتھ اس طرح بات چیت کرے گا:

1. سرور کے ساتھ کنکشن قائم کریں۔

1. صلاحیتوں، پرامپٹس، وسائل، اور ٹولز کی فہرست بنائیں، اور ان کا سکیمہ محفوظ کریں۔

1. ایک LLM شامل کریں اور محفوظ شدہ صلاحیتیں اور ان کا سکیمہ ایسی شکل میں LLM کو دیں جو وہ سمجھ سکے۔

1. صارف کے پرامپٹ کو سنبھالیں اور اسے کلائنٹ کی فہرست کردہ ٹولز کے ساتھ LLM کو بھیجیں۔

بہت اچھا، اب ہم سمجھ گئے کہ ہم اس کو اعلی سطح پر کیسے کر سکتے ہیں، آئیے نیچے مشق میں اسے آزمائیں۔

## مشق: LLM کے ساتھ کلائنٹ بنانا

اس مشق میں، ہم اپنے کلائنٹ میں ایک LLM شامل کرنا سیکھیں گے۔

### GitHub پرسنل ایکسیس ٹوکن کے ذریعے توثیق

GitHub ٹوکن بنانا ایک آسان عمل ہے۔ یہاں ہے کہ آپ کیسے کر سکتے ہیں:

- GitHub سیٹنگز پر جائیں – اوپر دائیں کونے میں اپنے پروفائل تصویر پر کلک کریں اور سیٹنگز منتخب کریں۔
- ڈویلپر سیٹنگز پر جائیں – نیچے اسکرول کریں اور ڈویلپر سیٹنگز پر کلک کریں۔
- پرسنل ایکسیس ٹوکنز منتخب کریں – فائن گرینڈ ٹوکنز پر کلک کریں اور پھر نیا ٹوکن جنریٹ کریں۔
- اپنے ٹوکن کی کنفیگریشن کریں – حوالہ کے لیے نوٹ شامل کریں، ایکسپائری تاریخ منتخب کریں، اور ضروری دائرہ کار (پرمیشنز) منتخب کریں۔ اس معاملے میں ماڈلز کی اجازت کو ضرور شامل کریں۔
- ٹوکن جنریٹ کریں اور کاپی کریں – جنریٹ ٹوکن پر کلک کریں، اور فوراً اسے کاپی کر لیں کیونکہ آپ اسے دوبارہ نہیں دیکھ پائیں گے۔

### -1- سرور سے جڑیں

آئیے پہلے اپنا کلائنٹ بنائیں:

#### ٹائپ اسکرپٹ

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // اسکیمہ کی توثیق کے لیے زوڈ درآمد کریں

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

- ضروری لائبریریز درآمد کیں
- ایک کلاس بنائی جس کے دو ممبر `client` اور `openai` ہیں جو بالترتیب کلائنٹ کو منظم کرنے اور LLM کے ساتھ بات چیت کے لیے مدد دیں گے۔
- اپنی LLM انسٹنس کی کنفیگریشن کی تاکہ GitHub ماڈلز استعمال ہو سکیں، `baseUrl` کو inference API کی طرف سیٹ کر کے۔

#### پائتھون

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio کنیکشن کے لیے سرور کے پیرامیٹرز بنائیں
server_params = StdioServerParameters(
    command="mcp",  # چلانے کے قابل
    args=["run", "server.py"],  # غیر لازمی کمانڈ لائن دلائل
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

- MCP کے لیے ضروری لائبریریز درآمد کیں
- کلائنٹ بنایا

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

#### جاوا

سب سے پہلے، آپ کو اپنے `pom.xml` فائل میں LangChain4j ڈیپینڈینسز شامل کرنی ہوں گی۔ MCP انٹیگریشن اور OpenAI-موافق MiniMax API کو فعال کرنے کے لیے یہ ڈیپینڈینسز شامل کریں:

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

اپنا MiniMax API کی اور اگر چاہیں تو اینڈپوائنٹ اور ماڈل سیٹ کریں۔
`MINIMAX_MODEL_ID` `MiniMax-M3` اور `MiniMax-M2.7` کو سپورٹ کرتا ہے۔ اگر
`OPENAI_BASE_URL` سیٹ نہ ہو، تو `MINIMAX_REGION` `global_en` اور `cn_zh` کو سپورٹ کرتا ہے۔

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

اینڈپوائنٹ کو ریجن کے لحاظ سے منتخب کرنے کے لیے، `OPENAI_BASE_URL` کو چھوڑ دیں:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

پھر اپنی جاوا کلائنٹ کلاس بنائیں:

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

        // سرور سے رابطہ کرنے کے لیے MCP ٹرانسپورٹ بنائیں
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

پچھلے کوڈ میں ہم نے:

- **LangChain4j ڈیپینڈینسز شامل کیں**: MCP انٹیگریشن اور OpenAI-موافق MiniMax API کے لیے ضروری
- **LangChain4j لائبریریز درآمد کیں**: MCP انٹیگریشن اور OpenAI چیٹ ماڈل فنکشنلٹی کے لیے
- **`ChatLanguageModel` بنایا**: MiniMax کو آپ کے MiniMax API کی، اینڈپوائنٹ، اور سپورٹڈ ماڈل آئی ڈی کے ساتھ استعمال کرنے کے لیے کنفیگر کیا گیا
- **HTTP ٹرانسپورٹ سیٹ اپ کی**: Server-Sent Events (SSE) کے ذریعے MCP سرور سے کنکٹ کرنے کے لیے
- **MCP کلائنٹ بنایا**: جو سرور سے بات چیت سنبھالے گا
- **LangChain4j کا بلٹ ان MCP سپورٹ استعمال کیا**: جو LLMs اور MCP سرورز کے درمیان انٹیگریشن کو آسان بناتا ہے

#### رسٹ

اس مثال میں فرض کیا گیا ہے کہ آپ کے پاس رسٹ پر مبنی MCP سرور چل رہا ہے۔ اگر آپ کے پاس نہیں ہے، تو سرور بنانے کے لیے [01-first-server](../01-first-server/README.md) سبق دیکھیں۔

اپنے رسٹ MCP سرور کے ساتھ، ایک ٹرمینل کھولیں اور اسی ڈائرکٹری میں جائیں جہاں سرور ہے۔ پھر نیا LLM کلائنٹ پروجیکٹ بنانے کے لیے درج ذیل کمانڈ چلائیں:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

اپنی `Cargo.toml` فائل میں درج ذیل ڈیپینڈینسز شامل کریں:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI کے لیے کوئی سرکاری رسٹ لائبریری نہیں ہے، تاہم `async-openai` crate ایک [کمیونٹی کی دیکھ بھال والی لائبریری](https://platform.openai.com/docs/libraries/rust#rust) ہے جو عام طور پر استعمال ہوتی ہے۔

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

    // کرنے کے لیے: MCP ٹول کی فہرست حاصل کریں

    // کرنے کے لیے: ٹول کالز کے ساتھ LLM گفتگو

    Ok(())
}
```

یہ کوڈ ایک بنیادی رسٹ ایپلیکیشن سیٹ اپ کرتا ہے جو MCP سرور اور GitHub ماڈلز سے LLM بات چیت کے لیے جڑے گا۔

> [!IMPORTANT]
> ایپلیکیشن چلانے سے پہلے `OPENAI_API_KEY` انوائرنمنٹ ویریبل اپنے GitHub ٹوکن کے ساتھ سیٹ کرنا یقینی بنائیں۔

بہت خوب، اگلے قدم کے لیے، آئیے سرور کی صلاحیتوں کی فہرست بنائیں۔

### -2- سرور کی صلاحیتوں کی فہرست بنائیں

اب ہم سرور سے جڑیں گے اور اس کی صلاحیتیں پوچھیں گے:

#### ٹائپ اسکرپٹ

اسی کلاس میں، درج ذیل طریقے شامل کریں:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // اوزاروں کی فہرست بنانا
    const toolsResult = await this.client.listTools();
}
```

پچھلے کوڈ میں ہم نے:

- سرور سے جڑنے کا کوڈ شامل کیا، `connectToServer`.
- `run` میتھڈ بنایا جو ہماری ایپ کے بہاؤ کو سنبھالتا ہے۔ اب تک یہ صرف ٹولز کی فہرست بناتا ہے لیکن ہم جلد ہی اس میں مزید اضافہ کریں گے۔

#### پائتھون

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

یہ ہے جو ہم نے شامل کیا:

- وسائل اور ٹولز کی فہرست بنائی اور انہیں پرنٹ کیا۔ ٹولز کے لیے ہم `inputSchema` بھی فہرست کرتے ہیں جسے بعد میں استعمال کریں گے۔

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
- ہر ٹول کے لیے نام، وضاحت، اور اس کا سکیمہ فہرست کیا۔ بعد میں ہم اسے ٹولز کال کرنے کے لیے استعمال کریں گے۔

#### جاوا

```java
// ایک ٹول فراہم کنندہ بنائیں جو خود بخود MCP ٹولز دریافت کرے
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ٹول فراہم کنندہ خود بخود مندرجہ ذیل کو سنبھالتا ہے:
// - MCP سرور سے دستیاب ٹولز کی فہرست تیار کرنا
// - MCP ٹول اسکیموں کو LangChain4j فارمیٹ میں تبدیل کرنا
// - ٹول کے اجرا اور جوابات کا انتظام کرنا
```

پچھلے کوڈ میں ہم نے:

- `McpToolProvider` بنایا جو خود بخود MCP سرور سے تمام ٹولز دریافت اور رجسٹر کرتا ہے
- ٹول پرووائڈر MCP ٹول سکیمہ کو LangChain4j کے ٹول فارمیٹ میں اندرونی طور پر تبدیل کرتا ہے
- اس طریقہ نے دستی ٹول فہرست سازی اور تبدیلی کے عمل کو پوشیدہ کر دیا

#### رسٹ

MCP سرور سے ٹولز بازیافت کرنے کے لیے `list_tools` طریقہ استعمال کیا جاتا ہے۔ `main` فنکشن میں MCP کلائنٹ سیٹ اپ کرنے کے بعد درج ذیل کوڈ شامل کریں:

```rust
// MCP ٹول کی فہرست حاصل کریں
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- سرور کی صلاحیتوں کو LLM ٹولز میں تبدیل کریں

سرور کی صلاحیتوں کی فہرست بنانے کے بعد اگلا قدم ان کو اس شکل میں تبدیل کرنا ہے جو LLM سمجھ سکے۔ جب ہم یہ کر لیں، ہم ان صلاحیتوں کو اپنے LLM کو ٹولز کے طور پر فراہم کر سکتے ہیں۔

#### ٹائپ اسکرپٹ

1. درج ذیل کوڈ شامل کریں تاکہ MCP سرور کے جواب کو ایک ایسے ٹول فارمیٹ میں تبدیل کیا جا سکے جو LLM استعمال کر سکتا ہے:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ان پٹ_سکیما کی بنیاد پر ایک زوڈ سکیما بنائیں
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // قسم کو واضح طور پر "فنکشن" پر مقرر کریں
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

    اوپر دیے گئے کوڈ میں MCP سرور کے جواب کو ایک ایسے ٹول کی تعریف کی شکل میں تبدیل کیا گیا ہے جو LLM سمجھ سکتا ہے۔

2. اب `run` میتھڈ کو اپ ڈیٹ کرتے ہیں تاکہ سرور کی صلاحیتیں فہرست کرے:

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

    پچھلے کوڈ میں، ہم نے `run` میتھڈ کو اپ ڈیٹ کیا ہے تاکہ نتیجے میں ہر انٹری پر `openAiToolAdapter` کال ہو۔

#### پائتھون

1. سب سے پہلے درج ذیل کنورٹر فنکشن بنائیں

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

    اوپر فنکشن `convert_to_llm_tools` میں MCP ٹول کے جواب کو اس شکل میں تبدیل کیا گیا ہے جو LLM سمجھ سکے۔

2. اب اپنے کلائنٹ کوڈ کو اپ ڈیٹ کریں تاکہ یہ فنکشن استعمال ہو:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    یہاں، ہم `convert_to_llm_tool` کو کال کر کے MCP ٹول کے جواب کو ایسی شکل میں تبدیل کر رہے ہیں جسے بعد میں LLM کو دے سکیں۔

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

- `ConvertFrom` فنکشن بنایا جو نام، وضاحت، اور ان پٹ سکیمہ لیتا ہے۔
- ایسا فنکشن ڈیفائن کیا جو `FunctionDefinition` بناتا ہے جو `ChatCompletionsDefinition` کو پاس ہوتا ہے۔ یہ وہ چیز ہے جو LLM سمجھ سکتا ہے۔

2. اب دیکھتے ہیں کہ ہم اپنے موجودہ کوڈ کو کیسے اپ ڈیٹ کر سکتے ہیں تاکہ اس فنکشن کا فائدہ اٹھا سکیں:

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

#### جاوا

```java
// قدرتی زبان کے تعامل کے لیے ایک بوٹ انٹرفیس بنائیں
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

- قدرتی زبان کے تعاملات کے لیے ایک سادہ `Bot` انٹرفیس ڈیفائن کیا
- LangChain4j کے `AiServices` کو استعمال کیا تاکہ LLM کو MCP ٹول پرووائڈر کے ساتھ خود بخود باندھا جا سکے
- فریم ورک خود بخود ٹول سکیمہ کی تبدیلی اور فنکشن کالیز کو پیچھے سے سنبھالتا ہے
- اس طریقہ کار سے دستی ٹول تبدیلی ختم ہو جاتی ہے - LangChain4j MCP ٹولز کو LLM-موافقت شدہ فارمیٹ میں تبدیل کرنے کی پیچیدگی سنبھالتا ہے

#### رسٹ

MCP ٹول کے جواب کو LLM کو قابل فہم شکل میں تبدیل کرنے کے لیے، ہم ایک معاون فنکشن شامل کریں گے جو ٹولز کی فہرست کو فارمیٹ کرے گا۔ `main.rs` فائل میں `main` فنکشن کے نیچے درج ذیل کوڈ شامل کریں۔ یہ LLM سے درخواست کرتے وقت کال کیا جائے گا:

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

بہت اچھا، اب ہم صارف کی درخواستیں سنبھالنے کے لیے تیار ہیں، تو اسے اگلے مرحلے میں کرتے ہیں۔

### -4- صارف کے پرامپٹ کی درخواست سنبھالیں

اس حصہ میں ہم صارف کی درخواستوں کو سنبھالیں گے۔

#### ٹائپ اسکرپٹ

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


        // ۲۔ سرور کے آلے کو کال کریں
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳۔ نتیجہ کے ساتھ کچھ کریں
        // کرنے کے لئے

        }
    }
    ```

    پچھلے کوڈ میں ہم نے:

    - `callTools` میتھڈ شامل کیا۔
    - یہ میتھڈ LLM کے جواب کو لیتا ہے اور چیک کرتا ہے کہ کون سے ٹولز کال کیے گئے ہیں۔

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // کال ٹول
        }
        ```

    - ٹول کو کال کرتا ہے اگر LLM نے اشارہ دیا ہو کہ اسے کال کیا جانا چاہیے۔

        ```typescript
        // ۲۔ سرور کے ٹول کو کال کریں
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳۔ نتیجہ کے ساتھ کچھ کریں
        // کیا جانا ہے
        ```

2. `run` میتھڈ کو اپ ڈیٹ کریں تاکہ LLM کالز اور `callTools` شامل ہوں:

    ```typescript

    // ۱۔ ایسے پیغامات بنائیں جو LLM کے لیے ان پٹ ہوں
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ۲۔ LLM کو کال کرنا
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ۳۔ LLM کے جواب کا جائزہ لیں، ہر انتخاب کے لیے چیک کریں کہ آیا اس میں ٹول کالز ہیں
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

بہت خوب، پورا کوڈ فہرست کرتے ہیں:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // اسکیمہ کی توثیق کے لیے zod کو درآمد کریں

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // مستقبل میں اس URL کو تبدیل کرنے کی ضرورت ہو سکتی ہے: https://models.github.ai/inference
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
          // input_schema کی بنیاد پر ایک zod اسکیمہ بنائیں
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
    
    
          // 2. سرور کے آلے کو کال کریں
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
    
        // 3. LLM کے جواب کو دیکھیں، ہر انتخاب کے لیے چیک کریں کہ کیا اس میں آلے کی کالز ہیں
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

#### پائتھون

1. LLM کو کال کرنے کے لیے ضروری درآمد شامل کریں

    ```python
    # ایل ایل ایم
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. پھر، وہ فنکشن شامل کریں جو LLM کو کال کرے گا:

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

    - وہ فنکشنز LLM کو دیے جو MCP سرور پر ملے اور تبدیل کیے گئے۔
    - پھر ان فنکشنز کے ساتھ LLM کو کال کیا۔
    - نتیجے کا معائنہ کیا کہ ہمیں کون سے فنکشن کال کرنے ہیں، اگر ہوں۔
    - آخر میں کال کرنے کے لیے فنکشنز کی ایک فہرست پاس کی۔

3. آخری قدم، اپنے مین کوڈ کو اپ ڈیٹ کریں:

    ```python
    prompt = "Add 2 to 20"

    # LLM سے پوچھیں کہ کون سے آلات سب کے لیے ہیں، اگر کوئی ہیں
    functions_to_call = call_llm(prompt, functions)

    # تجویز کردہ فنکشنز کو کال کریں
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    یہی آخری قدم تھا، اوپر کوڈ میں ہم نے:

    - MCP ٹول کو `call_tool` کے ذریعے کال کیا جو فنکشن LLM نے ہمارے پرامپٹ کے مطابق کال کرنے کا کہا تھا۔
    - MCP سرور پر ٹول کال کے نتیجے کو پرنٹ کیا۔

#### .NET

1. LLM پرامپٹ کی درخواست کا کوڈ دکھائیں:

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

    - MCP سرور سے ٹولز حاصل کیے، `var tools = await GetMcpTools()`.
    - صارف کا پرامپٹ `userMessage` ڈیفائن کیا۔
    - ماڈل اور ٹولز کی وضاحت کرنے والا ایک options آبجیکٹ بنایا۔
    - LLM کی طرف درخواست بھیجی۔

2. آخری قدم دیکھیں کہ کیا LLM سوچتا ہے کہ ہمیں کوئی فنکشن کال کرنا چاہیے:

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

    - فنکشن کالز کی فہرست میں لوپ کیا۔
    - ہر ٹول کال کے لیے نام اور آرگیومنٹس نکالے اور MCP سرور پر کلائنٹ کا استعمال کرتے ہوئے ٹول کو کال کیا۔ پھر نتائج پرنٹ کیے۔

مکمل کوڈ درج ذیل ہے:

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

#### جاوا

```java
try {
    // قدرتی زبان کی درخواستیں چلائیں جو خود بخود MCP ٹولز استعمال کرتی ہیں
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

- MCP سرور ٹولز کے ساتھ بات چیت کے لیے آسان قدرتی زبان کے پرامپٹس استعمال کیے
- LangChain4j فریم ورک خود بخود سنبھالتا ہے:
  - جب ضرورت ہو تو صارف کے پرامپٹس کو ٹول کالز میں تبدیل کرنا
  - LLM کے فیصلے کی بنیاد پر مناسب MCP ٹولز کو کال کرنا
  - LLM اور MCP سرور کے درمیان بات چیت کے بہاؤ کا انتظام کرنا
- `bot.chat()` طریقہ قدرتی زبان میں جوابات دیتا ہے جن میں MCP ٹولز کے عمل کے نتائج شامل ہو سکتے ہیں
- یہ طریقہ ایک ہموار صارف تجربہ فراہم کرتا ہے جہاں صارفین کو MCP کے بنیادی عمل سے آگاہی کی ضرورت نہیں ہوتی

مکمل کوڈ کی مثال:

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

#### رسٹ

یہاں زیادہ تر کام ہوتا ہے۔ ہم ابتدائی صارف پرامپٹ کے ساتھ LLM کو کال کریں گے، پھر جواب کا تجزیہ کریں گے کہ کیا کوئی ٹولز کال کرنے کی ضرورت ہے۔ اگر ہاں، تو ہم وہ ٹولز کال کریں گے اور LLM کے ساتھ بات چیت جاری رکھیں گے جب تک مزید ٹول کالز کی ضرورت نہ ہو اور ہمیں حتمی جواب نہ مل جائے۔


ہم LLM کو متعدد کالز کریں گے، تو آئیے ایک فنکشن بناتے ہیں جو LLM کال کو سنبھالے گا۔ اپنا `main.rs` فائل میں درج ذیل فنکشن شامل کریں:

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

یہ فنکشن LLM کلائنٹ، پیغامات کی فہرست (جس میں یوزر پرامپٹ بھی شامل ہے)، MCP سرور کے ٹولز لیتا ہے، اور LLM کو درخواست بھیجتا ہے، جواب کو واپس کرتا ہے۔

LLM سے موصول ہونے والے جواب میں `choices` کا ایک ارے ہوگا۔ ہمیں نتیجہ کو اس طرح پراسیس کرنا ہوگا کہ دیکھ سکیں آیا کوئی `tool_calls` موجود ہیں یا نہیں۔ یہ ہمیں بتاتا ہے کہ LLM کسی مخصوص ٹول کو دلائل کے ساتھ کال کرنے کی درخواست کر رہا ہے۔ اپنے `main.rs` فائل کے نیچے درج ذیل کوڈ شامل کریں تاکہ LLM کے جواب کو ہینڈل کرنے والا فنکشن بنایا جا سکے:

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

            // پیغامات میں ٹول کے نتائج شامل کریں
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

اگر `tool_calls` موجود ہیں، تو یہ ٹول کی معلومات نکالتا ہے، MCP سرور کو ٹول کی درخواست کے ساتھ کال کرتا ہے، اور نتائج کو گفتگو کے پیغامات میں شامل کرتا ہے۔ پھر یہ LLM کے ساتھ گفتگو جاری رکھتا ہے اور پیغامات اسسٹنٹ کے جواب اور ٹول کال کے نتائج کے ساتھ اپ ڈیٹ ہو جاتے ہیں۔

MCP کالز کے لیے LLM جو ٹول کال معلومات واپس کرتا ہے اسے نکالنے کے لیے، ہم ایک اور مددگار فنکشن شامل کریں گے جو کال کرنے کے لیے ضروری ہر چیز کو نکالے گا۔ اپنے `main.rs` فائل کے نیچے درج ذیل کوڈ شامل کریں:

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

تمام حصے مکمل ہونے کے بعد، ہم اب ابتدائی یوزر پرامپٹ کو ہینڈل کر کے LLM کو کال کر سکتے ہیں۔ اپنے `main` فنکشن کو درج ذیل کوڈ کے ساتھ اپ ڈیٹ کریں:

```rust
// LLM کا آلہ کالز کے ساتھ مکالمہ
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

یہ ابتدائی یوزر پرامپٹ کے ساتھ LLM سے دو نمبروں کے مجموعے کا سوال کرے گا، اور جواب کو پراسیس کرے گا تاکہ ٹول کالز کو متحرک طور پر سنبھالا جا سکے۔

بہت خوب، آپ نے کر لیا!

## اسائنمنٹ

مشق کے کوڈ کو لے کر سرور کو مزید ٹولز کے ساتھ تیار کریں۔ پھر ایک LLM کے ساتھ کلائنٹ بنائیں، جیسا کہ مشق میں ہے، اور مختلف پرامپٹس کے ساتھ اسے آزما کر دیکھیں تاکہ آپ کے سرور کے تمام ٹولز متحرک طور پر کال ہوں۔ اس طرح کلائنٹ بنانے کا مطلب ہے کہ آخری صارف کو بہترین صارف تجربہ حاصل ہوگا کیونکہ وہ مخصوص کلائنٹ کمانڈز کے بجائے پرامپٹس استعمال کر سکیں گے اور MCP سرور کی کالز سے بے خبر رہیں گے۔

## حل

[حل](./solution/README.md)

## اہم نکات

- اپنے کلائنٹ میں LLM شامل کرنا MCP سرورز کے ساتھ بہتر تعامل کا ذریعہ فراہم کرتا ہے۔
- آپ کو MCP سرور کے جواب کو LLM کے سمجھنے کے قابل کچھ میں تبدیل کرنے کی ضرورت ہے۔

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.نیٹ کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائیتھن کیلکولیٹر](../../../../03-GettingStarted/samples/python)
- [رسٹ کیلکولیٹر](../../../../03-GettingStarted/samples/rust)

## اضافی وسائل

## اگلا کیا ہے

- اگلا: [Visual Studio Code استعمال کرتے ہوئے سرور کا مصرف](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->