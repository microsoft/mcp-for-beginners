# ایجاد یک کلاینت با LLM

تاکنون دیده‌اید چگونه یک سرور و یک کلاینت ایجاد کنید. کلاینت توانسته به‌طور صریح سرور را برای لیست کردن ابزارها، منابع و پرامپت‌هایش فراخوانی کند. با این حال، این روش چندان عملی نیست. کاربران شما در عصر عامل‌محور زندگی می‌کنند و انتظار دارند از پرامپت‌ها استفاده کنند و با یک LLM ارتباط برقرار کنند. آنها اهمیتی نمی‌دهند که شما برای ذخیره قابلیت‌ها از MCP استفاده می‌کنید یا نه؛ آنها صرفاً انتظار دارند با زبان طبیعی ارتباط برقرار کنند. پس چگونه این مشکل را حل می‌کنیم؟ راه‌حل این است که یک LLM به کلاینت اضافه کنیم.

## مرور کلی

در این درس ما بر افزودن یک LLM به کلاینت تمرکز می‌کنیم و نشان می‌دهیم چگونه این کار تجربه بهتری برای کاربر شما فراهم می‌کند.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- ایجاد یک کلاینت با یک LLM.
- تعامل بی‌وقفه با سرور MCP با استفاده از یک LLM.
- ارائه تجربه بهتر به کاربر نهایی در سمت کلاینت.

## رویکرد

بیایید سعی کنیم رویکرد لازم را بفهمیم. افزودن یک LLM ساده به‌نظر می‌رسد، اما آیا واقعاً این کار را انجام خواهیم داد؟

این‌گونه کلاینت با سرور تعامل خواهد داشت:

1. برقراری اتصال با سرور.

1. لیست کردن قابلیت‌ها، پرامپت‌ها، منابع و ابزارها و ذخیره اسکیمای آنها.

1. افزودن یک LLM و ارسال قابلیت‌های ذخیره شده همراه با اسکیمای آنها به فرمتی که LLM بفهمد.

1. مدیریت پرامپت کاربر با ارسال آن به LLM به همراه ابزارهای لیست شده توسط کلاینت.

عالی است، حالا که درک کردیم چگونه می‌توانیم این کار را در سطح بالا انجام دهیم، بیایید این کار را در تمرین زیر امتحان کنیم.

## تمرین: ایجاد یک کلاینت با یک LLM

در این تمرین، یاد می‌گیریم چگونه یک LLM به کلاینت خود اضافه کنیم.

### احراز هویت با توکن دسترسی شخصی گیت‌هاب

ایجاد توکن گیت‌هاب فرایندی ساده است. در اینجا نحوه انجام آن آمده است:

- به تنظیمات گیت‌هاب بروید – روی عکس پروفایل خود در گوشه بالا سمت راست کلیک کنید و Settings را انتخاب کنید.
- به تنظیمات توسعه‌دهنده بروید – اسکرول کنید و روی Developer Settings کلیک کنید.
- توکن‌های دسترسی شخصی را انتخاب کنید – روی Fine-grained tokens کلیک کنید و سپس Generate new token را انتخاب کنید.
- توکن خود را تنظیم کنید – یک یادداشت برای مرجع وارد کنید، تاریخ انقضا را تنظیم کنید و دامنه‌های لازم (دسترسی‌ها) را انتخاب کنید. در این مورد مطمئن شوید مجوز Models را اضافه کنید.
- توکن را ایجاد و کپی کنید – روی Generate token کلیک کنید و بلافاصله آن را کپی کنید، چون دیگر قادر به دیدن آن نخواهید بود.

### -1- اتصال به سرور

ابتدا کلاینت خود را ایجاد کنیم:

#### تایپ‌اسکریپت

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // وارد کردن zod برای اعتبارسنجی طرح‌واره

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

در کد قبلی ما:

- کتابخانه‌های لازم را وارد کردیم
- یک کلاس با دو عضو، `client` و `openai` ایجاد کردیم که به ما در مدیریت کلاینت و تعامل با یک LLM کمک می‌کند.
- نمونه LLM خود را برای استفاده از مدل‌های GitHub با تنظیم `baseUrl` به سمت API استنتاج پیکربندی کردیم.

#### پایتون

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# ایجاد پارامترهای سرور برای اتصال stdio
server_params = StdioServerParameters(
    command="mcp",  # قابل اجرا
    args=["run", "server.py"],  # آرگومان‌های خط فرمان اختیاری
    env=None,  # متغیرهای محیطی اختیاری
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # مقداردهی اولیه اتصال
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

در کد قبلی ما:

- کتابخانه‌های لازم برای MCP را وارد کردیم
- یک کلاینت ایجاد کردیم

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

ابتدا باید وابستگی‌های LangChain4j را به فایل `pom.xml` خود اضافه کنید. این وابستگی‌ها را برای فعال‌سازی یکپارچگی MCP و API MiniMax سازگار با OpenAI اضافه کنید:

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

کلید API MiniMax خود را تنظیم کنید و به طور اختیاری نقطه انتهایی و مدل را تعیین کنید.
`MINIMAX_MODEL_ID` از `MiniMax-M3` و `MiniMax-M2.7` پشتیبانی می‌کند. اگر
`OPENAI_BASE_URL` تنظیم نشده باشد، `MINIMAX_REGION` از `global_en` و `cn_zh` پشتیبانی می‌کند.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

برای انتخاب نقطه انتهایی به وسیله منطقه، به‌جای آن `OPENAI_BASE_URL` را حذف کنید:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

سپس کلاس کلاینت جاوای خود را ایجاد کنید:

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

        // ایجاد انتقال MCP برای اتصال به سرور
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // ایجاد کلاینت MCP
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

در کد قبلی ما:

- **وابستگی‌های LangChain4j را اضافه کردیم**: مورد نیاز برای یکپارچه‌سازی MCP و API MiniMax سازگار با OpenAI
- **کتابخانه‌های LangChain4j را وارد کردیم**: برای یکپارچه‌سازی MCP و عملکرد مدل گفتگو OpenAI
- **یک `ChatLanguageModel` ایجاد کردیم**: پیکربندی شده برای استفاده از MiniMax با کلید API، نقطه انتهایی و شناسه مدل پشتیبانی شده شما
- **حمل و نقل HTTP را تنظیم کردیم**: با استفاده از Server-Sent Events (SSE) برای اتصال به سرور MCP
- **یک کلاینت MCP ایجاد کردیم**: که ارتباط با سرور را مدیریت می‌کند
- **از پشتیبانی داخلی MCP LangChain4j استفاده کردیم**: که ادغام بین LLM و سرورهای MCP را ساده می‌کند

#### راست

این مثال فرض می‌کند که یک سرور MCP بر پایه Rust دارید. اگر ندارید، به درس [01-first-server](../01-first-server/README.md) مراجعه کنید تا سرور را ایجاد کنید.

وقتی سرور Rust MCP خود را داشتید، یک ترمینال باز کنید و به همان دایرکتوری سرور بروید. سپس فرمان زیر را برای ایجاد یک پروژه کلاینت LLM جدید اجرا کنید:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

وابستگی‌های زیر را به فایل `Cargo.toml` خود اضافه کنید:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> کتابخانه رسمی Rust برای OpenAI وجود ندارد، اما crate `async-openai` یک کتابخانه [نگهداری شده توسط جامعه](https://platform.openai.com/docs/libraries/rust#rust) است که معمولاً استفاده می‌شود.

فایل `src/main.rs` را باز کنید و محتوای آن را با کد زیر جایگزین کنید:

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
    // پیام اولیه
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // راه‌اندازی کلاینت OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // راه‌اندازی کلاینت MCP
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

    // کاری که باید انجام شود: دریافت لیست ابزار MCP

    // کاری که باید انجام شود: مکالمه LLM با فراخوانی ابزارها

    Ok(())
}
```

این کد یک برنامه پایه Rust را تنظیم می‌کند که به یک سرور MCP و مدل‌های GitHub برای تعاملات LLM متصل خواهد شد.

> [!IMPORTANT]
> قبل از اجرای برنامه مطمئن شوید متغیر محیطی `OPENAI_API_KEY` را با توکن گیت‌هاب خود تنظیم کرده‌اید.

عالی، برای گام بعدی، بیایید قابلیت‌های سرور را لیست کنیم.

### -2- لیست قابلیت‌های سرور

حالا به سرور اتصال می‌دهیم و قابلیت‌های آن را می‌پرسیم:

#### تایپ‌اسکریپت

در همان کلاس، متدهای زیر را اضافه کنید:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // فهرست کردن ابزارها
    const toolsResult = await this.client.listTools();
}
```

در کد قبلی ما:

- کدی برای اتصال به سرور، `connectToServer` افزودیم.
- متد `run` را ایجاد کردیم که مسئول مدیریت جریان برنامه ما است. تاکنون فقط ابزارها را لیست می‌کند، اما به زودی موارد بیشتری به آن اضافه خواهیم کرد.

#### پایتون

```python
# لیست منابع موجود
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# لیست ابزارهای موجود
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

موارد افزوده شده این‌ها هستند:

- منابع و ابزارها را لیست کردیم و چاپ نمودیم. برای ابزارها همچنین `inputSchema` را لیست کردیم که بعداً استفاده می‌کنیم.

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

در کد قبلی ما:

- ابزارهای موجود روی سرور MCP را لیست کردیم
- برای هر ابزار، نام، توضیح و اسکیمای آن را لیست کردیم. مورد آخر چیزی است که بعدها برای فراخوانی ابزارها استفاده می‌کنیم.

#### جاوا

```java
// ایجاد یک تامین‌کننده ابزار که به‌طور خودکار ابزارهای MCP را کشف می‌کند
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// تامین‌کننده ابزار MCP به‌طور خودکار مدیریت می‌کند:
// - فهرست کردن ابزارهای موجود از سرور MCP
// - تبدیل طرح‌های ابزار MCP به فرمت LangChain4j
// - مدیریت اجرای ابزار و پاسخ‌ها
```

در کد قبلی ما:

- یک `McpToolProvider` ایجاد کردیم که تمام ابزارهای سرور MCP را به صورت خودکار کشف و ثبت می‌کند
- تأمین‌کننده ابزار تبدیل بین اسکیمای ابزارهای MCP و فرمت ابزار LangChain4j را به صورت داخلی مدیریت می‌کند
- این رویکرد عملیات لیست کردن و تبدیل دستی ابزارها را ساده می‌کند

#### راست

دریافت ابزارها از سرور MCP با استفاده از متد `list_tools` انجام می‌شود. در تابع `main` خود، پس از تنظیم کلاینت MCP، کد زیر را اضافه کنید:

```rust
// دریافت فهرست ابزار MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- تبدیل قابلیت‌های سرور به ابزارهای LLM

گام بعدی پس از لیست کردن قابلیت‌های سرور این است که آن‌ها را به فرمتی تبدیل کنیم که LLM بفهمد. بعد از آن، می‌توانیم این قابلیت‌ها را به عنوان ابزار به LLM ارائه کنیم.

#### تایپ‌اسکریپت

1. کد زیر را برای تبدیل پاسخ از سرور MCP به فرمت ابزاری که LLM می‌تواند استفاده کند، اضافه کنید:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ایجاد یک اسکیمای زاد بر اساس input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // به طور صریح نوع را روی "function" تنظیم کنید
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

    کد بالا پاسخی از سرور MCP را می‌گیرد و آن را به فرمت تعریف ابزار تبدیل می‌کند که LLM می‌تواند درک کند.

2. حالا متد `run` را به روز کنیم تا قابلیت‌های سرور را لیست کند:

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

    در کد قبلی، متد `run` را به گونه‌ای به‌روز کرده‌ایم که روی نتیجه پیمایش کند و برای هر ورودی `openAiToolAdapter` را فراخوانی کند.

#### پایتون

1. ابتدا، تابع تبدیل زیر را ایجاد کنیم:

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

    در تابع بالا `convert_to_llm_tools` پاسخ ابزار MCP را گرفته و به فرمت قابل فهم برای LLM تبدیل می‌کند.

2. سپس، کد کلاینت خود را به این صورت به‌روز کنیم تا از این تابع استفاده کند:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    در اینجا، فراخوانی به `convert_to_llm_tool` اضافه شده تا پاسخ ابزار MCP را به چیزی تبدیل کند که بعدها می‌توانیم به LLM بدهیم.

#### .NET

1. کدی برای تبدیل پاسخ ابزار MCP به چیزی که LLM بتواند درک کند، اضافه کنیم:

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

در کد قبلی ما:

- تابعی به نام `ConvertFrom` ایجاد کردیم که نام، توضیح و اسکیمای ورودی را می‌پذیرد.
- عملکردی تعریف کردیم که یک FunctionDefinition ایجاد می‌کند که به ChatCompletionsDefinition منتقل می‌شود. مورد دوم چیزی است که LLM می‌تواند بفهمد.

2. حالا ببینیم چگونه می‌توانیم کد موجود را به گونه‌ای به روز کنیم که از این تابع استفاده کند:

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
// ایجاد یک رابط ربات برای تعامل زبان طبیعی
public interface Bot {
    String chat(String prompt);
}

// پیکربندی سرویس هوش مصنوعی با ابزارهای LLM و MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

در کد قبلی ما:

- یک اینترفیس ساده به نام `Bot` برای تعاملات زبان طبیعی تعریف کردیم
- از `AiServices` در LangChain4j برای اتصال خودکار LLM با تأمین‌کننده ابزار MCP استفاده کردیم
- فریم ورک به صورت خودکار تبدیل اسکیمای ابزار و فراخوانی توابع را مدیریت می‌کند
- این رویکرد تبدیل دستی ابزار را حذف می‌کند - LangChain4j همه پیچیدگی تبدیل ابزارهای MCP به فرمت سازگار با LLM را مدیریت می‌کند

#### راست

برای تبدیل پاسخ ابزار MCP به فرمتی که LLM بفهمد، تابع کمکی اضافه می‌کنیم که لیست ابزارها را قالب‌بندی کند. کد زیر را در فایل `main.rs` خود پایین تابع `main` اضافه کنید. این تابع هنگام ارسال درخواست‌ها به LLM فراخوانی می‌شود:

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

عالی است، حالا آماده‌ایم تا درخواست‌های کاربر را مدیریت کنیم، پس به این بخش می‌پردازیم.

### -4- مدیریت درخواست پرامپت کاربر

در این بخش، درخواست‌های کاربر را مدیریت می‌کنیم.

#### تایپ‌اسکریپت

1. متدی اضافه کنید که برای فراخوانی LLM ما استفاده می‌شود:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // ۲. تماس با ابزار سرور
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳. انجام کاری با نتیجه
        // انجام شود

        }
    }
    ```

    در کد قبلی ما:

    - متد `callTools` را اضافه کردیم.
    - متد ورودی پاسخ LLM را دریافت می‌کند و بررسی می‌کند آیا ابزاری باید فراخوانی شود یا خیر:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // فراخوانی ابزار
        }
        ```

    - اگر LLM نشان دهد ابزاری باید فراخوانی شود، آن را صدا می‌زند.

        ```typescript
        // ۲. ابزار سرور را فراخوانی کنید
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳. کاری با نتیجه انجام دهید
        // انجام شود
        ```

2. متد `run` را به‌روز کنید تا شامل فراخوانی LLM و `callTools` باشد:

    ```typescript

    // ۱. ایجاد پیام‌هایی که ورودی برای LLM هستند
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ۲. فراخوانی LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ۳. گذر از پاسخ LLM، برای هر گزینه، بررسی کنید که آیا شامل فراخوانی ابزار است یا خیر
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

عالی است، کد کامل را مشاهده کنید:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ایمپورت کردن zod برای اعتبارسنجی اسکیمای داده‌ها

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ممکن است در آینده نیاز باشد به این آدرس تغییر داده شود: https://models.github.ai/inference
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
          // ایجاد یک اسکیمای zod بر اساس input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // به‌طور صریح نوع را به "function" تنظیم کن
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
    
    
          // ۲. فراخوانی ابزار سرور
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // ۳. انجام کاری با نتیجه
          // کار برای انجام
    
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
    
        // ۳. بررسی پاسخ LLM، برای هر انتخاب، چک کن که آیا فراخوانی ابزار دارد
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

#### پایتون

1. چند import لازم برای فراخوانی LLM اضافه کنیم

    ```python
    # مدل زبان بزرگ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. سپس، تابعی اضافه کنیم که LLM را فراخوانی می‌کند:

    ```python
    # مدل زبان بزرگ

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
            # پارامترهای اختیاری
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

    در کد قبلی ما:

    - توابعی که روی سرور MCP پیدا کردیم و تبدیل شده‌اند را به LLM داده‌ایم.
    - سپس LLM را با آن توابع فراخوانی کردیم.
    - بعد نتیجه را بررسی می‌کنیم تا ببینیم چه توابعی باید فراخوانی شوند، اگر وجود داشته باشند.
    - در نهایت آرایه‌ای از توابع برای فراخوانی را می‌دهیم.

3. گام نهایی، کد اصلی را به‌روزرسانی کنیم:

    ```python
    prompt = "Add 2 to 20"

    # از مدل زبانی بزرگ بپرسید که چه ابزارهایی، اگر وجود داشته باشد، اعمال شوند
    functions_to_call = call_llm(prompt, functions)

    # فراخوانی توابع پیشنهادی
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    این، آخرین گام بود، در کد بالا ما:

    - با استفاده از تابع `call_tool` ابزاری از MCP را فراخوانی می‌کنیم که LLM بر اساس پرامپت ما فکر کرده باید فراخوانی شود.
    - نتیجه فراخوانی آن ابزار را در سرور MCP چاپ می‌کنیم.

#### .NET

1. کدی برای درخواست پرامپت LLM نشان دهیم:

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

    در کد قبلی ما:

    - ابزارها از سرور MCP بازیابی شدند، `var tools = await GetMcpTools()`.
    - پرامپت کاربری تعریف شد `userMessage`.
    - شیء گزینه‌ها با تعیین مدل و ابزارها ساخته شد.
    - یک درخواست به سمت LLM ارسال شد.

2. یک مرحله آخر، ببینیم آیا LLM فکر می‌کند باید تابعی فراخوانی شود:

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

    در کد قبلی ما:

    - روی لیست فراخوانی‌های تابع پیمایش کردیم.
    - برای هر فراخوانی ابزار، نام و آرگومان‌ها استخراج و ابزار روی سرور MCP با استفاده از کلاینت MCP فراخوانی شد. در نهایت نتایج چاپ شدند.

کد کامل چنین است:

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
    // اجرای درخواست‌های زبان طبیعی که به‌طور خودکار از ابزارهای MCP استفاده می‌کنند
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

در کد قبلی ما:

- از پرامپت‌های زبان طبیعی ساده برای تعامل با ابزارهای سرور MCP استفاده کردیم
- فریم ورک LangChain4j به طور خودکار:
  - پرامپت‌های کاربر را وقتی لازم است به فراخوانی ابزار تبدیل می‌کند
  - ابزارهای MCP مناسب را بر اساس تصمیم LLM فراخوانی می‌کند
  - جریان گفتگو بین LLM و سرور MCP را مدیریت می‌کند
- متد `bot.chat()` پاسخ‌های زبان طبیعی‌ای برمی‌گرداند که ممکن است شامل نتایجی از اجرای ابزارهای MCP باشد
- این رویکرد تجربه‌ای بی‌وقفه برای کاربر فراهم می‌کند که کاربران نیاز ندارند از پیاده‌سازی پایه MCP مطلع باشند

مثال کامل کد:

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

#### راست

اصلی‌ترین کار در اینجا اتفاق می‌افتد. ما ابتدا LLM را با پرامپت اولیه کاربر فراخوانی می‌کنیم، سپس پاسخ را پردازش می‌کنیم تا ببینیم آیا نیاز به فراخوانی ابزارهای خاصی هست یا خیر. در صورت نیاز، آن ابزارها را فراخوانی می‌کنیم و گفتگو را با LLM ادامه می‌دهیم تا دیگر نیازی به فراخوانی ابزارها نباشد و یک پاسخ نهایی دریافت کنیم.


ما چندین بار باید به LLM فراخوانی کنیم، پس بیایید یک تابع تعریف کنیم که این فراخوانی به LLM را مدیریت کند. تابع زیر را به فایل `main.rs` خود اضافه کنید:

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

این تابع، کلاینت LLM، لیستی از پیام‌ها (شامل درخواست کاربر)، ابزارهای سرور MCP را می‌گیرد و یک درخواست به LLM ارسال می‌کند و پاسخ آن را برمی‌گرداند.

پاسخ از LLM شامل آرایه‌ای از `choices` خواهد بود. ما باید نتیجه را پردازش کنیم تا ببینیم آیا `tool_calls` وجود دارد یا خیر. این به ما اطلاع می‌دهد که LLM درخواست می‌کند یک ابزار خاص با آرگومان‌ها فراخوانی شود. کد زیر را به انتهای فایل `main.rs` خود اضافه کنید تا تابعی را برای مدیریت پاسخ LLM تعریف کنید:

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

    // چاپ محتوا در صورت موجود بودن
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // مدیریت فراخوانی ابزارها
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // افزودن پیام دستیار

        // اجرای هر فراخوانی ابزار
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // افزودن نتیجه ابزار به پیام‌ها
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ادامه گفتگو با نتایج ابزار
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

اگر `tool_calls` وجود داشته باشد، اطلاعات ابزار را استخراج می‌کند، سرور MCP را با درخواست ابزار فراخوانی می‌کند و نتایج را به پیام‌های گفتگو اضافه می‌کند. سپس گفتگو را با LLM ادامه می‌دهد و پیام‌ها با پاسخ دستیار و نتایج فراخوانی ابزار به‌روزرسانی می‌شوند.

برای استخراج اطلاعات فراخوانی ابزار که LLM برای تماس‌های MCP برمی‌گرداند، یک تابع کمکی دیگر اضافه خواهیم کرد که همه چیز مورد نیاز برای انجام فراخوانی را استخراج کند. کد زیر را به انتهای فایل `main.rs` اضافه کنید:

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

با داشتن تمام قطعات، اکنون می‌توانیم درخواست اولیه کاربر را مدیریت کرده و LLM را فراخوانی کنیم. تابع `main` خود را با کد زیر به‌روزرسانی کنید:

```rust
// مکالمه LLM با فراخوانی ابزارها
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

این کد با درخواست اولیه کاربر برای جمع دو عدد به LLM پرس‌وجو می‌کند و پاسخ را پردازش می‌کند تا به صورت پویا فراخوانی ابزارها را مدیریت کند.

بسیار خوب، شما موفق شدید!

## تمرین

کد تمرین را بگیرید و سرور را با چند ابزار بیشتر توسعه دهید. سپس یک کلاینت با LLM بسازید، مانند تمرین، و آن را با درخواست‌های مختلف تست کنید تا مطمئن شوید همه ابزارهای سرور شما به صورت پویا فراخوانی می‌شوند. این روش ساخت کلاینت به این معنی است که کاربر نهایی تجربه کاربری عالی خواهد داشت، چون می‌تواند از درخواست‌ها استفاده کند، به جای فرمان‌های دقیق کلاینت، و از فراخوانی هر سرور MCP بی‌خبر باشد.

## راه‌حل

[راه‌حل](./solution/README.md)

## نکات کلیدی

- اضافه کردن LLM به کلاینت شما راه بهتری برای تعامل کاربران با سرورهای MCP فراهم می‌کند.
- شما باید پاسخ سرور MCP را به چیزی تبدیل کنید که LLM بتواند بفهمد.

## نمونه‌ها

- [ماشین حساب جاوا](../samples/java/calculator/README.md)
- [ماشین حساب دات‌نت](../../../../03-GettingStarted/samples/csharp)
- [ماشین حساب جاوااسکریپت](../samples/javascript/README.md)
- [ماشین حساب تایپ‌اسکریپت](../samples/typescript/README.md)
- [ماشین حساب پایتون](../../../../03-GettingStarted/samples/python)
- [ماشین حساب راست](../../../../03-GettingStarted/samples/rust)

## منابع اضافی

## مراحل بعدی

- مرحله بعد: [استفاده از سرور با Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->