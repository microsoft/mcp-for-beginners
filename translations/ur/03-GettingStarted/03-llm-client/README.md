# LLM کے ساتھ کلائنٹ بنانا

> [!NOTE]
> جاوا کلائنٹ کی مثالیں پرانا HTTP+SSE ٹرانسپورٹ استعمال کرتے ہوئے جڑتی ہیں اور
> MCP `2025-11-25` SDK APIs کو ہدف بناتی ہیں۔ نئے ریموٹ کلائنٹس کے لیے `2026-07-28`-مطابق SDK اور
> Streamable HTTP استعمال کریں۔

اب تک، آپ نے دیکھا کہ کس طرح ایک سرور اور ایک کلائنٹ بنائیں۔ کلائنٹ نے واضح طور پر سرور کو کال کر کے اس کے ٹولز، وسائل، اور پرامپٹس کی فہرست نکالنے کی صلاحیت رکھی ہے۔ تاہم، یہ طریقہ زیادہ عملی نہیں ہے۔ آپ کے صارفین ایجنٹک دور میں رہتے ہیں اور امید رکھتے ہیں کہ وہ پرامپٹس کا استعمال کرکے اور ایک LLM کے ساتھ بات چیت کر سکیں۔ انہیں اس بات کی پرواہ نہیں ہے کہ آپ اپنی صلاحیتوں کو اسٹور کرنے کے لئے MCP استعمال کرتے ہیں یا نہیں؛ وہ صرف قدرتی زبان کا استعمال کرتے ہوئے بات چیت کی توقع رکھتے ہیں۔ تو ہم اسے کیسے حل کریں؟ حل یہ ہے کہ کلائنٹ میں ایک LLM شامل کیا جائے۔

## جائزہ

اس سبق میں ہم اپنے کلائنٹ میں LLM شامل کرنے پر توجہ دیتے ہیں اور دکھاتے ہیں کہ یہ آپ کے صارف کے لئے بہت بہتر تجربہ فراہم کرتا ہے۔

## سیکھنے کے اہداف

اس سبق کے اختتام تک، آپ قابل ہوں گے:

- LLM کے ساتھ کلائنٹ بنانا۔
- LLM کا استعمال کرتے ہوئے MCP سرور کے ساتھ بے جوڑ بات چیت کرنا۔
- کلائنٹ سائڈ پر بہتر اینڈ یوزر تجربہ فراہم کرنا۔

## طریقہ کار

آئیں سمجھنے کی کوشش کریں کہ ہمیں کون سا طریقہ اختیار کرنا چاہیے۔ ایک LLM شامل کرنا آسان لگتا ہے، لیکن کیا ہم واقعی ایسا کریں گے؟

کلائنٹ کس طرح سرور کے ساتھ بات چیت کرے گا اس کا طریقہ درج ذیل ہے:

1. سرور کے ساتھ کنکشن قائم کریں۔

1. صلاحیتیں، پرامپٹس، وسائل اور ٹولز کی فہرست نکالیں، اور ان کے اسکیمہ کو محفوظ کریں۔

1. ایک LLM شامل کریں اور محفوظ شدہ صلاحیتوں اور ان کے اسکیمہ کو ایسے فارمیٹ میں پاس کریں جسے LLM سمجھتا ہو۔

1. صارف کے پرامپٹ کو سنبھالیں اور اسے LLM کو کلائنٹ کی فہرست کردہ ٹولز کے ساتھ پاس کریں۔

اچھا، اب ہم سمجھ چکے ہیں کہ ہم اعلی سطح پر یہ کیسے کر سکتے ہیں، آئیں ذیل میں اس مشق میں یہ آزما کر دیکھیں۔

## مشق: LLM کے ساتھ کلائنٹ بنانا

اس مشق میں، ہم سیکھیں گے کہ اپنے کلائنٹ میں ایک LLM کیسے شامل کریں۔

### GitHub پرسنل ایکسیس ٹوکن کے ذریعے توثیق

GitHub ٹوکن بنانا ایک آسان عمل ہے۔ یہاں ہے کہ آپ یہ کیسے کر سکتے ہیں:

- GitHub سیٹنگز پر جائیں – اوپری دائیں کونے میں اپنی پروفائل تصویر پر کلک کریں اور سیٹنگز منتخب کریں۔
- ڈیولپر سیٹنگز پر جائیں – نیچے سکرول کریں اور ڈیولپر سیٹنگز پر کلک کریں۔
- پرسنل ایکسیس ٹوکن منتخب کریں – فائن-گریند ٹوکنز پر کلک کریں اور پھر نیا ٹوکن بنائیں۔
- اپنا ٹوکن کنفیگر کریں – حوالہ کے لیے نوٹ شامل کریں، ایکسپائری ڈیٹ مقرر کریں، اور ضروری اسکوب منتخب کریں۔ اس معاملے میں ماڈلز کی اجازت شامل کرنا یقینی بنائیں۔
- ٹوکن جنریٹ کریں اور اسے کاپی کریں – جنریٹ ٹوکن پر کلک کریں، اور فوراً کاپی کریں کیونکہ آپ دوبارہ اسے نہیں دیکھ پائیں گے۔

### -1- سرور سے کنیکٹ کریں

پہلے ہمارے کلائنٹ کو بنائیں:

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

- ضروری لائبریریز امپورٹ کیں
- ایک کلاس بنائی جس میں دو ممبرز `client` اور `openai` ہیں جو ہمیں کلائنٹ کو مینج کرنے اور LLM کے ساتھ بات چیت کرنے میں مدد دیں گے۔
- ہمارا LLM انسٹینس GitHub ماڈلز استعمال کرنے کے لیے کنفیگر کیا گیا ہے، جس میں `baseUrl` انفرینس API پوائنٹ کر رہا ہے۔

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# اسٹڈیئو کنکشن کے لیے سرور کے پیرامیٹرز بنائیں
server_params = StdioServerParameters(
    command="mcp",  # قابلِ اجرا
    args=["run", "server.py"],  # اختیاری کمانڈ لائن کے دلائل
    env=None,  # اختیاری ماحول کے متغیرات
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # کنکشن کی شروعات کریں
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

پچھلے کوڈ میں ہم نے:

- MCP کے لیے درکار لائبریریز امپورٹ کیں
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

سب سے پہلے، آپ کو اپنے `pom.xml` فائل میں LangChain4j انحصار شامل کرنے ہوں گے۔ ان انحصاروں کو شامل کریں تاکہ MCP انٹیگریشن اور OpenAI-مطابق MiniMax API فعال ہو سکے:

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

اپنے MiniMax API کی کو سیٹ کریں اور، اختیاری طور پر، اینڈپوائنٹ اور ماڈل بھی۔
`MINIMAX_MODEL_ID` `MiniMax-M3` اور `MiniMax-M2.7` کو سپورٹ کرتا ہے۔ اگر
`OPENAI_BASE_URL` سیٹ نہیں ہے، تو `MINIMAX_REGION` `global_en` اور `cn_zh` کو سپورٹ کرتا ہے۔

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

علاقہ کے مطابق اینڈپوائنٹ منتخب کرنے کے لیے، `OPENAI_BASE_URL` چھوڑ دیں:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

پھر اپنے جاوا کلائنٹ کلاس بنائیں:

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

        // سرور سے رابطہ قائم کرنے کے لیے MCP ٹرانسپورٹ بنائیں
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

- **LangChain4j انحصار شامل کیے**: MCP انٹیگریشن اور OpenAI-مطابق MiniMax API کے لیے ضروری
- **LangChain4j لائبریریز امپورٹ کیں**: MCP انٹیگریشن اور OpenAI چیٹ ماڈل فعالیت کے لیے
- **`ChatLanguageModel` بنایا**: MiniMax کو آپ کے MiniMax API کی، اینڈپوائنٹ، اور سپورٹڈ ماڈل ID کے ساتھ کنفیگر کیا گیا
- **HTTP ٹرانسپورٹ ترتیب دی**: سرور سینٹ ایونٹس (SSE) استعمال کرتے ہوئے MCP سرور سے کنیکٹ کرنے کے لیے
- **MCP کلائنٹ بنایا**: جو سرور کے ساتھ بات چیت کا انتظام کرے گا
- **LangChain4j کی بلٹ ان MCP سپورٹ استعمال کی**: جو LLMs اور MCP سرورز کے درمیان انٹیگریشن کو آسان بناتی ہے

#### Rust

یہ مثال فرض کرتی ہے کہ آپ کا ایک Rust پر مبنی MCP سرور چل رہا ہے۔ اگر نہیں ہے، تو سرور بنانے کے لیے [01-first-server](../01-first-server/README.md) سبق ملاحظہ کریں۔

جب آپ کا Rust MCP سرور تیار ہو، تو ایک ٹرمینل کھولیں اور سرور جیسا ہی فولڈر میں جائیں۔ پھر نیا LLM کلائنٹ پروجیکٹ بنانے کے لیے مندرجہ ذیل کمانڈ چلائیں:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

اپنی `Cargo.toml` فائل میں درج ذیل انحصار شامل کریں:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI کے لیے کوئی سرکاری Rust لائبریری نہیں، لیکن `async-openai` کریٹ ایک [کمیونٹی کی دیکھ بھال والی لائبریری](https://platform.openai.com/docs/libraries/rust#rust) ہے جو عام طور پر استعمال ہوتی ہے۔

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

    // اوپن اے آئی کلائنٹ کی ترتیب
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // ایم سی پی کلائنٹ کی ترتیب
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

    // کرنے کے لئے: ایم سی پی ٹول کی فہرست حاصل کریں

    // کرنے کے لئے: ٹول کالز کے ساتھ ایل ایل ایم گفتگو

    Ok(())
}
```

یہ کوڈ ایک بنیادی Rust ایپلیکیشن سیٹ اپ کرتا ہے جو MCP سرور اور GitHub ماڈلز کے ساتھ LLM انٹریکشن کے لیے کنیکٹ کرے گا۔

> [!IMPORTANT]
> ایپلیکیشن چلانے سے پہلے اپنے GitHub ٹوکن کے ساتھ `OPENAI_API_KEY` ماحولیاتی متغیر کو سیٹ کرنا یقینی بنائیں۔

اچھا، اگلے مرحلے کے لیے، آئیں سرور کی صلاحیتوں کی فہرست نکالیں۔

### -2- سرور کی صلاحیتیں فہرست کریں

اب ہم سرور سے کنیکٹ کریں گے اور اس کی صلاحیتیں پوچھیں گے:

#### Typescript

اسی کلاس میں، درج ذیل طریقے شامل کریں:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // اوزار کی فہرست بنانا
    const toolsResult = await this.client.listTools();
}
```

پچھلے کوڈ میں ہم نے:

- سرور سے کنیکٹ کرنے کے لیے کوڈ شامل کیا، `connectToServer`۔
- `run` طریقہ بنایا جو ہماری ایپ کی فلو کا انتظام کرے گا۔ ابھی تک یہ صرف ٹولز کی فہرست دیتا ہے لیکن ہم جلد اس میں مزید چیزیں شامل کریں گے۔

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

ہم نے شامل کیا:

- وسائل اور ٹولز کی فہرست نکالی اور پرنٹ کی۔ ٹولز کے لیے ہم `inputSchema` بھی لسٹ کرتے ہیں جو بعد میں استعمال ہوگا۔

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

- MCP سرور پر دستیاب ٹولز کی فہرست نکالی
- ہر ٹول کے لیے، نام، تفصیل اور اس کا اسکیمہ نکالا۔ یہ اسکیمہ بعد میں ٹولز کال کرنے کے لیے استعمال ہوگا۔

#### Java

```java
// ایک ایسا ٹول فراہم کنندہ بنائیں جو خود بخود MCP ٹولز کو دریافت کرے
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ٹول فراہم کنندہ خود بخود مندرجہ ذیل کو سنبھالتا ہے:
// - MCP سرور سے دستیاب ٹولز کی فہرست بنانا
// - MCP ٹول اسکیمہ کو LangChain4j فارمیٹ میں تبدیل کرنا
// - ٹول کی عملدرآمد اور جوابات کا انتظام کرنا
```

پچھلے کوڈ میں ہم نے:

- ایک `McpToolProvider` بنایا جو خودکار طور پر MCP سرور سے تمام ٹولز دریافت اور رجسٹر کرتا ہے
- ٹول پرووائیڈر MCP ٹول اسکیموں اور LangChain4j کے ٹول فارمیٹ کے درمیان تبادلہ داخلی طور پر سنبھالتا ہے
- یہ طریقہ دستی ٹول فہرست نکالنے اور تبادلۂ کار عمل کو ہٹا دیتا ہے

#### Rust

MCP سرور سے ٹولز حاصل کرنا `list_tools` طریقہ استعمال کرکے کیا جاتا ہے۔ اپنی `main` فنکشن میں، MCP کلائنٹ سیٹ اپ کرنے کے بعد، درج ذیل کوڈ شامل کریں:

```rust
// MCP ٹول لسٹنگ حاصل کریں
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- سرور کی صلاحیتوں کو LLM ٹولز میں تبدیل کریں

سرور کی صلاحیتوں کی فہرست نکالنے کے بعد اگلا قدم ہے انہیں ایسے فارمیٹ میں تبدیل کرنا جو LLM سمجھ سکے۔ ایک بار ایسا کرنے کے بعد، ہم ان صلاحیتوں کو اپنے LLM کے ٹولز کے طور پر فراہم کر سکتے ہیں۔

#### TypeScript

1. MCP سرور سے جواب کو ایسے ٹول فارمیٹ میں تبدیل کرنے کے لیے درج ذیل کوڈ شامل کریں جو LLM استعمال کر سکتا ہو:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ان پٹ_اسکیما کی بنیاد پر زوڈ اسکیمہ بنائیں
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

    اوپر کوڈ MCP سرور سے جواب لیتا ہے اور اسے ایک ٹول ڈیفینیشن فارمیٹ میں تبدیل کرتا ہے جو LLM سمجھ سکتا ہے۔

2. اب `run` طریقہ کو اپ ڈیٹ کریں تاکہ سرور کی صلاحیتوں کی فہرست نکالے:

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

    پچھلے کوڈ میں، ہم نے `run` طریقہ کو اپ ڈیٹ کیا تاکہ وہ نتیجہ میں دورے کرے اور ہر انٹری کے لیے `openAiToolAdapter` کال کرے۔

#### Python

1. سب سے پہلے، درج ذیل کنورٹر فنکشن بنائیں

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

    اوپر فنکشن `convert_to_llm_tools` MCP ٹول کے جواب کو لیتا ہے اور اسے ایسے فارمیٹ میں تبدیل کرتا ہے جسے LLM سمجھ سکتا ہے۔

2. پھر اپنے کلائنٹ کوڈ کو اپ ڈیٹ کریں تاکہ یہ فنکشن استعمال کر سکے:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    یہاں، ہم `convert_to_llm_tool` کو کال کر رہے ہیں تاکہ MCP ٹول کا جواب تبدیل کرکے بعد میں LLM کو دیا جا سکے۔

#### .NET

1. MCP ٹول کے جواب کو LLM سمجھ سکنے والا فارمیٹ میں تبدیل کرنے کے لیے کوڈ شامل کریں

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

- `ConvertFrom` فنکشن بنایا جو نام، وضاحت، اور ان پٹ اسکیمہ لیتا ہے۔
- ایسی فعالیت ڈیفائن کی جو ایک `FunctionDefinition` بناتی ہے جو `ChatCompletionsDefinition` کو پاس کی جاتی ہے۔ یہ آخری چیز LLM سمجھ سکتا ہے۔

2. اب دیکھتے ہیں کس طرح موجودہ کوڈ کو اپ ڈیٹ کیا جا سکتا ہے تاکہ اس فنکشن کا فائدہ اٹھایا جا سکے:

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
// فطری زبان کے تعامل کے لیے ایک بوٹ انٹرفیس بنائیں
public interface Bot {
    String chat(String prompt);
}

// ایل ایل ایم اور ایم سی پی ٹولز کے ساتھ اے آئی سروس کو ترتیب دیں
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

پچھلے کوڈ میں ہم نے:

- خودکار زبان کے تعاملات کے لیے ایک سادہ `Bot` انٹرفیس ڈیفائن کیا
- LangChain4j کے `AiServices` کا استعمال کیا تاکہ LLM کو خودکار طور پر MCP ٹول پرووائیڈر کے ساتھ باندھ سکیں
- فریم ورک خود بخود ٹول اسکیمہ تبادلہ اور فنکشن کالنگ کو پیچھے سے سنبھالتا ہے
- یہ طریقہ کار دستی ٹول تبادلہ ختم کرتا ہے - LangChain4j MCP ٹولز کو LLM-مطابق فارمیٹ میں تبدیل کرنے کی تمام پیچیدگی سنبھالتا ہے

#### Rust

MCP ٹول کے جواب کو ایسے فارمیٹ میں تبدیل کرنے کے لیے جو LLM سمجھ سکے، ہم ایک معاون فنکشن شامل کریں گے جو ٹولز کی فہرست کو فارمیٹ کرے گا۔ اپنے `main.rs` فائل میں `main` فنکشن کے نیچے درج ذیل کوڈ شامل کریں۔ یہ LLM کے لیے ریکویسٹ کرتے وقت کال کیا جائے گا:

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

اچھا، ہم نے کسی بھی صارف کی درخواست کو ہینڈل کرنے کے لیے تیار ہیں، تو آئیں اگلے حصہ سے شروع کرتے ہیں۔

### -4- صارف کے پرامپٹ کی درخواست ہینڈل کریں

اس حصے میں، ہم صارف کی درخواست کو ہینڈل کریں گے۔

#### TypeScript

1. ایک طریقہ شامل کریں جو ہمارا LLM کال کرے گا:

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
        // کرنا ہے

        }
    }
    ```

    پچھلے کوڈ میں ہم نے:

    - `callTools` طریقہ شامل کیا۔
    - یہ طریقہ LLM کے جواب کو لیتا ہے اور دیکھتا ہے کہ کون سے ٹولز کال کیے گئے ہیں، اگر کوئی ہوں:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // آلہ کال کریں
        }
        ```

    - اگر LLM نے اشارہ کیا ہو تو ٹول کو کال کرتا ہے:

        ```typescript
        // 2۔ سرور کے ٹول کو کال کریں
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3۔ نتیجہ کے ساتھ کچھ کریں
        // کرنے کے لئے
        ```

2. `run` طریقہ کو اپ ڈیٹ کریں تاکہ LLM کو کال اور `callTools` کو کال شامل کرے:

    ```typescript

    // 1۔ پیغامات تخلیق کریں جو LLM کے لیے ان پٹ ہوں
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

اچھا، اب مکمل کوڈ دیکھیں:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // اسکیمہ کی توثیق کے لیے زوڈ امپورٹ کریں

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
          // انپٹ_اسکیمہ کی بنیاد پر ایک زوڈ اسکیمہ بنائیں
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
    
        // 3. ایل ایل ایم کے ردعمل کا جائزہ لیں، ہر انتخاب کے لیے چیک کریں کہ آیا اس میں ٹول کالز ہیں
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

1. LLM کو کال کرنے کے لیے درکار کچھ امپورٹس شامل کریں

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

    - ہماری وہ فنکشنز پاس کیں جو ہم نے MCP سرور پر پائی اور تبدیل کیں۔
    - پھر LLM کو وہ فنکشنز کال کیں۔
    - پھر نتیجہ کو چیک کیا کہ کون سے فنکشنز کال کیے جانے چاہئیں، اگر ہوں۔
    - آخر میں فنکشنز کی ایک ارے کو کال کیا۔

3. آخری قدم، اپنے مین کوڈ کو اپ ڈیٹ کریں:

    ```python
    prompt = "Add 2 to 20"

    # تمام دستیاب آلات کے بارے میں LLM سے پوچھیں، اگر کوئی ہوں
    functions_to_call = call_llm(prompt, functions)

    # تجویز کردہ افعال کو کال کریں
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    آخر، وہ آخری قدم تھا، اوپر کوڈ میں ہم نے:

    - ہمارے پرامپٹ کی بنیاد پر LLM کے خیال میں کال کیے جانے والے فنکشن کے ذریعے MCP ٹول کو `call_tool` کے ذریعے کال کیا۔
    - MCP سرور کو ٹول کال کے نتیجے کو پرنٹ کیا۔

#### .NET

1. LLM پرامپٹ درخواست کے لیے کچھ کوڈ دکھائیں:

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
    - ایک آپشنز آبجیکٹ بنایا جس میں ماڈل اور ٹولز کی وضاحت کی۔
    - LLM کی طرف درخواست کی۔

2. آخری قدم، دیکھتے ہیں کہ کیا LLM سمجھتا ہے کہ ہمیں کوئی فنکشن کال کرنی چاہیے:

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
    - ہر ٹول کال کے لیے نام اور آرگیومنٹس نکالے اور MCP کلائنٹ استعمال کرتے ہوئے MCP سرور پر ٹول کال کی۔ آخر میں نتائج پرنٹ کیے۔

مکمل کوڈ یہ ہے:

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

- MCP سرور کے ٹولز کے ساتھ سادہ قدرتی زبان کے پرامپٹس سے بات چیت کی
- LangChain4j فریم ورک خودکار طور پر مندرجہ ذیل سنبھالتا ہے:
  - جب ضرورت ہو تو صارف کے پرامپٹس کو ٹول کالز میں تبدیل کرنا
  - LLM کے فیصلہ کی بنیاد پر مناسب MCP ٹولز کو کال کرنا
  - LLM اور MCP سرور کے درمیان گفتگو کے بہاؤ کا انتظام کرنا
- `bot.chat()` طریقہ قدرتی زبان کے جوابات دیتا ہے جس میں ممکنہ طور پر MCP ٹولز کے نفاذ کے نتائج شامل ہوتے ہیں
- یہ طریقہ کار ایک ہموار صارف تجربہ فراہم کرتا ہے جہاں صارفین کو MCP کی بنیادی سمجھنے کی ضرورت نہیں ہوتی

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

#### Rust


یہاں زیادہ تر کام ہوتا ہے۔ ہم ابتدائی صارف کے اشارے کے ساتھ LLM کو کال کریں گے، پھر جواب کو پراسیس کریں گے تاکہ دیکھیں کیا کسی ٹول کو کال کرنے کی ضرورت ہے۔ اگر ایسا ہے، تو ہم ان ٹولز کو کال کریں گے اور LLM کے ساتھ گفتگو جاری رکھیں گے جب تک مزید ٹول کالز کی ضرورت نہ ہو اور ہمارے پاس حتمی جواب نہ ہو۔

ہم LLM کو متعدد کالز کریں گے، اس لیے آئیے ایک فنکشن متعین کریں جو LLM کال کو سنبھالے گا۔ اپنے `main.rs` فائل میں درج ذیل فنکشن شامل کریں:

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

یہ فنکشن LLM کلائنٹ، پیغامات کی فہرست (بشمول صارف کا اشارہ)، MCP سرور سے ٹولز لیتا ہے، اور LLM کو درخواست بھیجتا ہے، جواب واپس کرتا ہے۔

LLM سے موصولہ جواب میں `choices` کی ایک صف ہوگی۔ ہمیں نتیجہ پراسیس کرنا ہوگا تاکہ دیکھ سکیں کیا کوئی `tool_calls` موجود ہیں۔ اس سے ہمیں معلوم ہوتا ہے کہ LLM مخصوص ٹول کو دلائل کے ساتھ کال کرنے کی درخواست کر رہا ہے۔ اپنے `main.rs` فائل کے نیچے درج ذیل کوڈ شامل کریں تاکہ LLM جواب کو سنبھالنے کے لیے فنکشن ڈیفائن کیا جا سکے:

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

اگر `tool_calls` موجود ہیں، تو یہ ٹول کی معلومات نکالتا ہے، MCP سرور کو ٹول کی درخواست کے ساتھ کال کرتا ہے، اور نتائج کو گفتگو کے پیغامات میں شامل کرتا ہے۔ پھر یہ LLM کے ساتھ گفتگو جاری رکھتا ہے اور پیغامات معاون کے جواب اور ٹول کال کے نتائج کے ساتھ اپ ڈیٹ ہوتے ہیں۔

MCP کالز کے لیے LLM کی طرف سے واپس کیے گئے ٹول کال معلومات نکالنے کے لیے، ہم ایک اور معاون فنکشن شامل کریں گے تاکہ کال کے لیے درکار تمام چیزیں نکال سکیں۔ اپنے `main.rs` فائل کے نیچے درج ذیل کوڈ شامل کریں:

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

تمام حصے جگہ پر ہونے کے ساتھ، ہم اب ابتدائی صارف کے اشارے کو سنبھال سکتے ہیں اور LLM کو کال کر سکتے ہیں۔ اپنے `main` فنکشن کو درج ذیل کوڈ کے ساتھ اپ ڈیٹ کریں:

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

یہ ابتدائی صارف کے اشارے کے ساتھ LLM سے دو نمبروں کے مجموعے کے لیے سوال کرے گا، اور جواب کو پراسیس کرے گا تاکہ ٹول کالز کو متحرک طریقے سے سنبھالا جا سکے۔

بہت خوب، آپ نے کر لیا!

## اسائنمنٹ

مشق سے کوڈ لیں اور سرور میں مزید ٹولز شامل کریں۔ پھر ایک LLM کلائنٹ بنائیں، جیسا کہ مشق میں ہے، اور مختلف اشاروں کے ساتھ ٹیسٹ کریں تاکہ یقینی بنایا جا سکے کہ آپ کے تمام سرور ٹولز متحرک طور پر کال ہو رہے ہیں۔ کلائنٹ بنانے کا یہ طریقہ آخر صارف کو بہترین تجربہ فراہم کرے گا کیونکہ وہ اشاروں کو استعمال کر سکیں گے، بجائے مخصوص کلائنٹ کمانڈز کے، اور MCP سرور کی کال سے بے خبر رہیں گے۔

## حل

[حل](./solution/README.md)

## اہم نکات

- اپنے کلائنٹ میں LLM شامل کرنے سے صارفین کے لیے MCP سرورز کے ساتھ تعامل کا بہتر طریقہ ملتا ہے۔
- آپ کو MCP سرور کے جواب کو اس طرح تبدیل کرنا ہوگا کہ LLM اسے سمجھ سکے۔

## نمونے

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## اضافی ذرائع

## آگے کیا ہے

- اگلا: [Visual Studio Code استعمال کرتے ہوئے سرور کا استعمال](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->