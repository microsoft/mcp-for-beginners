# ایجاد یک کلاینت با LLM

> [!NOTE]
> مثال‌های کلاینت جاوا از طریق ترنسپورت قدیمی HTTP+SSE متصل می‌شوند و
> به MCP `2025-11-25` SDK APIs هدف‌گذاری شده‌اند. برای کلاینت‌های جدید از SDK سازگار با `2026-07-28` و
> Streamable HTTP استفاده کنید.

تا کنون، دیده‌اید چگونه یک سرور و کلاینت ایجاد کنید. کلاینت توانسته است به‌طور صریح سرور را برای فهرست ابزارها، منابع، و پرامپت‌ها فراخوانی کند. اما این روش چندان عملی نیست. کاربران شما در عصر عامل‌محور زندگی می‌کنند و انتظار دارند به‌جای این کارها، مستقیماً با LLM ارتباط برقرار کنند. آن‌ها اهمیتی نمی‌دهند که شما از MCP برای ذخیره قابلیت‌هایتان استفاده می‌کنید یا خیر؛ صرفاً انتظار دارند با زبان طبیعی ارتباط برقرار کنند. پس چگونه این مشکل را حل کنیم؟ راه‌حل افزودن یک LLM به کلاینت است.

## مرور کلی

در این درس تمرکز ما روی افزودن یک LLM به کلاینت است و نشان می‌دهیم چگونه این تجربه بسیار بهتر و روان‌تری برای کاربر فراهم می‌کند.

## اهداف یادگیری

تا پایان این درس، شما قادر خواهید بود:

- ایجاد یک کلاینت با LLM.
- تعامل بی‌وقفه با سرور MCP با استفاده از یک LLM.
- ارائه تجربه کاربری بهتر در سمت کلاینت.

## رویکرد

بیایید رویکرد را بهتر درک کنیم. افزودن LLM به نظر ساده می‌رسد، اما آیا واقعاً این کار را انجام می‌دهیم؟

این‌گونه کلاینت با سرور تعامل خواهد داشت:

1. برقراری اتصال با سرور.

1. فهرست کردن قابلیت‌ها، پرامپت‌ها، منابع و ابزارها و ذخیره طرح (schema) آن‌ها.

1. افزودن یک LLM و ارسال قابلیت‌ها و طرح ذخیره شده در فرمتی که LLM متوجه می‌شود.

1. مدیریت پرامپت کاربر با ارسال آن به LLM همراه با ابزارهایی که کلاینت فهرست کرده است.

بسیار خوب، حالا که درک کردیم چگونه می‌توانیم این کار را به‌صورت کلی انجام دهیم، بیایید در تمرین زیر امتحان کنیم.

## تمرین: ایجاد یک کلاینت با LLM

در این تمرین، یاد می‌گیریم چگونه یک LLM را به کلاینت خود اضافه کنیم.

### احراز هویت با استفاده از توکن دسترسی شخصی GitHub

ایجاد یک توکن GitHub فرآیند ساده‌ای است. در اینجا چگونگی انجام آن آمده است:

- به تنظیمات GitHub بروید – روی عکس پروفایل خود در بالای سمت راست کلیک کرده و گزینه Settings را انتخاب کنید.
- به تنظیمات توسعه‌دهنده بروید – به پایین صفحه اسکرول کرده و روی Developer Settings کلیک کنید.
- توکن‌های دسترسی شخصی را انتخاب کنید – روی Fine-grained tokens کلیک کرده و سپس Generate new token را انتخاب کنید.
- توکن خود را پیکربندی کنید – یک توضیح اضافه کنید، تاریخ انقضا تنظیم کنید و مجوزهای لازم را انتخاب کنید. در اینجا مطمئن شوید که مجوز Models را اضافه کرده‌اید.
- توکن را ایجاد و کپی کنید – روی Generate token کلیک کنید و مطمئن شوید فوراً آن را کپی کنید چون بعداً قابل مشاهده نخواهد بود.

### -1- اتصال به سرور

ابتدا کلاینت خود را ایجاد کنیم:

#### TypeScript

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

در کد بالا ما:

- کتابخانه‌های مورد نیاز را وارد کرده‌ایم
- کلاسی با دو عضو `client` و `openai` ساخته‌ایم که به ما در مدیریت کلاینت و تعامل با LLM کمک می‌کنند.
- نمونه LLM را برای استفاده از GitHub Models با تنظیم `baseUrl` به API استنتاج تنظیم کرده‌ایم.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# ایجاد پارامترهای سرور برای اتصال stdio
server_params = StdioServerParameters(
    command="mcp",  # اجرایی
    args=["run", "server.py"],  # آرگومان‌های اختیاری خط فرمان
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

در کد بالا ما:

- کتابخانه‌های مورد نیاز MCP را وارد کرده‌ایم
- یک کلاینت ایجاد کرده‌ایم

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

ابتدا باید وابستگی‌های LangChain4j را به فایل `pom.xml` پروژه خود اضافه کنید. این وابستگی‌ها ادغام MCP و API MiniMax سازگار با OpenAI را فعال می‌کنند:

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

کلید API MiniMax خود و در صورت نیاز نقطه پایانی و مدل را تنظیم کنید.
`MINIMAX_MODEL_ID` از `MiniMax-M3` و `MiniMax-M2.7` پشتیبانی می‌کند. اگر
`OPENAI_BASE_URL` تنظیم نشده باشد، `MINIMAX_REGION` از `global_en` و `cn_zh` پشتیبانی می‌کند.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

برای انتخاب نقطه پایانی بر اساس منطقه، `OPENAI_BASE_URL` را حذف کنید:

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

در کد بالا ما:

- **وابستگی‌های LangChain4j** را اضافه کرده‌ایم: مورد نیاز برای ادغام MCP و API MiniMax سازگار با OpenAI
- **کتابخانه‌های LangChain4j** را وارد کرده‌ایم: برای ادغام MCP و عملکرد مدل چت OpenAI
- **یک `ChatLanguageModel` ایجاد کرده‌ایم**: کانفیگ شده برای استفاده از MiniMax با کلید API MiniMax، نقطه پایانی و مدل پشتیبانی شده شما
- **ترنسپورت HTTP را تنظیم کرده‌ایم**: با استفاده از رویدادهای ارسال شده توسط سرور (SSE) برای اتصال به سرور MCP
- **یک کلاینت MCP ساخته‌ایم**: که ارتباط با سرور را مدیریت می‌کند
- **از پشتیبانی درون چارچوب LangChain4j برای MCP بهره برده‌ایم**: که ادغام بین LLMها و سرورهای MCP را ساده می‌کند

#### Rust

این مثال فرض می‌کند یک سرور MCP مبتنی بر Rust دارید. اگر ندارید، به درس [01-first-server](../01-first-server/README.md) مراجعه کنید تا سرور را بسازید.

وقتی سرور Rust MCP خود را دارید، ترمینال را باز کرده و به همان دایرکتوری سرور بروید. سپس فرمان زیر را برای ایجاد یک پروژه کلاینت LLM جدید اجرا کنید:

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
> کتابخانه رسمی Rust برای OpenAI وجود ندارد، اما crates.io `async-openai` یک [کتابخانه تحت نگهداری جامعه](https://platform.openai.com/docs/libraries/rust#rust) است که معمولاً استفاده می‌شود.

فایل `src/main.rs` را باز کرده و محتوای آن را با کد زیر جایگزین کنید:

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

    // تنظیم کلاینت OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // تنظیم کلاینت MCP
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

    // کاری که باید انجام شود: دریافت فهرست ابزارهای MCP

    // کاری که باید انجام شود: مکالمه LLM با فراخوانی ابزارها

    Ok(())
}
```

این کد یک برنامه پایه Rust تنظیم می‌کند که به سرور MCP و GitHub Models متصل می‌شود برای تعاملات LLM.

> [!IMPORTANT]
> حتماً قبل از اجرای برنامه متغیر محیطی `OPENAI_API_KEY` را با توکن GitHub خود تنظیم کنید.

عالی، برای مرحله بعد، بیایید قابلیت‌های سرور را فهرست کنیم.

### -2- فهرست قابلیت‌های سرور

اکنون به سرور متصل شده و درخواست قابلیت‌ها می‌کنیم:

#### Typescript

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

در کد بالا ما:

- کد اتصال به سرور با نام `connectToServer` اضافه کرده‌ایم.
- متد `run` را ایجاد کردیم که مسئول مدیریت جریان برنامه است. تاکنون فقط ابزارها را فهرست می‌کند ولی به زودی موارد بیشتری اضافه خواهیم کرد.

#### Python

```python
# فهرست منابع موجود
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# فهرست ابزارهای موجود
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

موارد اضافه شده:

- فهرست منابع و ابزارها را چاپ کرده‌ایم. برای ابزارها همچنین `inputSchema` را فهرست کرده‌ایم که بعداً استفاده می‌کنیم.

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

در کد بالا:

- ابزارهای موجود در سرور MCP را فهرست کرده‌ایم
- برای هر ابزار، نام، توضیح و طرح آن را فهرست کرده‌ایم. این موارد بعدا برای فراخوانی ابزارها استفاده خواهد شد.

#### Java

```java
// ایجاد یک ارائه‌دهنده ابزار که به‌طور خودکار ابزارهای MCP را کشف می‌کند
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ارائه‌دهنده ابزار MCP به‌طور خودکار موارد زیر را مدیریت می‌کند:
// - فهرست کردن ابزارهای موجود از سرور MCP
// - تبدیل طرح‌های ابزار MCP به فرمت LangChain4j
// - مدیریت اجرای ابزار و پاسخ‌ها
```

در کد بالا:

- یک `McpToolProvider` ایجاد کرده‌ایم که به‌صورت خودکار همه ابزارهای سرور MCP را کشف و ثبت می‌کند
- فراهم‌کننده ابزار تبدیل بین طرح MCP و قالب ابزار LangChain4j را به‌صورت داخلی انجام می‌دهد
- این رویکرد فرآیند فهرست سازی و تبدیل دستی ابزارها را حذف می‌کند

#### Rust

بازیابی ابزارها از سرور MCP با متد `list_tools` انجام می‌شود. در تابع `main` خود، پس از تنظیم کلاینت MCP، کد زیر را اضافه کنید:

```rust
// دریافت فهرست ابزار MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- تبدیل قابلیت‌های سرور به ابزارهای LLM

گام بعدی پس از فهرست کردن قابلیت‌های سرور، تبدیل آن‌ها به فرمتی است که LLM متوجه شود. وقتی این کار را انجام دادیم، می‌توانیم این قابلیت‌ها را به‌عنوان ابزار به LLM ارائه کنیم.

#### TypeScript

1. کد زیر را برای تبدیل پاسخ از سرور MCP به فرمت ابزار قابل استفاده توسط LLM اضافه کنید:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ایجاد یک طرح زود بر اساس input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // نوع را صریحاً به "function" تنظیم کنید
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

    کد بالا پاسخ سرور MCP را گرفته و به فرمت تعریفی ابزار که LLM می‌تواند بفهمد تبدیل می‌کند.

2. حالا متد `run` را برای فهرست کردن قابلیت‌های سرور به‌روزرسانی کنیم:

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

    در کد فوق، متد `run` را به‌روزرسانی کرده‌ایم تا روی نتیجه پیمایش کند و برای هر ورودی `openAiToolAdapter` را فراخوانی نماید.

#### Python

1. ابتدا تابع تبدیل زیر را بسازیم:

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

    در تابع `convert_to_llm_tools` که بالا آمده، پاسخ ابزار MCP گرفته شده و به فرمتی تبدیل می‌شود که LLM بتواند بفهمد.

2. سپس کد کلاینت را به‌روزرسانی کنیم تا از این تابع استفاده کند:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    در اینجا، فراخوانی `convert_to_llm_tool` را اضافه کرده‌ایم تا پاسخ ابزار MCP به فرمی تبدیل شود که بعدها به LLM داده شود.

#### .NET

1. کد تبدیل پاسخ ابزار MCP به فرمتی که LLM می‌فهمد را اضافه کنیم:

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

در کد بالا ما:

- تابعی به نام `ConvertFrom` ایجاد کرده‌ایم که نام، توضیح و طرح ورودی را می‌گیرد.
- عملکردی تعریف کرده‌ایم که یک `FunctionDefinition` ایجاد می‌کند و به `ChatCompletionsDefinition` ارسال می‌نماید که برای LLM قابل فهم است.

2. حالا می‌بینیم چطور می‌توانیم کد موجود را به‌روزرسانی کنیم تا از این تابع استفاده کند:

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
// ایجاد یک رابط بات برای تعامل زبان طبیعی
public interface Bot {
    String chat(String prompt);
}

// پیکربندی سرویس هوش مصنوعی با ابزارهای LLM و MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

در کد بالا ما:

- یک رابط ساده `Bot` برای تعاملات زبان طبیعی تعریف کرده‌ایم
- از `AiServices` LangChain4j استفاده کرده‌ایم تا به‌صورت خودکار LLM را با فراهم‌کننده ابزار MCP پیوند دهد
- چارچوب به‌صورت خودکار تبدیل طرح ابزار و فراخوانی توابع را مدیریت می‌کند
- این رویکرد تبدیل دستی ابزارها را حذف می‌کند و LangChain4j تمام پیچیدگی‌های تبدیل ابزارهای MCP به فرمت سازگار با LLM را مدیریت می‌کند

#### Rust

برای تبدیل پاسخ ابزار MCP به فرمت قابل فهم برای LLM، یک تابع کمکی اضافه می‌کنیم که فهرست ابزارها را فرمت می‌کند. کد زیر را زیر تابع `main` در فایل `main.rs` اضافه کنید. این کد هنگام ارسال درخواست به LLM فراخوانی می‌شود:

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

عالی، اکنون برای مدیریت درخواست‌های کاربر آماده نیستیم، بنابراین بیایید این مورد را بعدی انجام دهیم.

### -4- مدیریت درخواست پرامپت کاربر

در این بخش از کد، درخواست‌های کاربر را مدیریت می‌کنیم.

#### TypeScript

1. متدی اضافه کنید که برای فراخوانی LLM استفاده می‌شود:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // ۲. ابزار سرور را فراخوانی کن
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳. کاری با نتیجه انجام بده
        // انجام شد

        }
    }
    ```

    در کد بالا ما:

    - متد `callTools` را اضافه کرده‌ایم.
    - این متد پاسخ LLM را گرفته و بررسی می‌کند که آیا ابزاری باید فراخوانی شود یا خیر:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // فراخوانی ابزار
        }
        ```

    - در صورت لزوم، یک ابزار را فرا می‌خواند:

        ```typescript
        // ۲. فراخوانی ابزار سرور
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳. انجام کاری با نتیجه
        // انجام شود
        ```

2. متد `run` را به‌روزرسانی کنید تا تماس با LLM و فراخوانی `callTools` را شامل شود:

    ```typescript

    // ۱. ایجاد پیام‌هایی که ورودی برای مدل زبان بزرگ (LLM) هستند
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ۲. فراخوانی مدل زبان بزرگ (LLM)
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ۳. بررسی پاسخ مدل زبان بزرگ، برای هر گزینه، بررسی کنید که آیا فراخوانی ابزار دارد یا خیر
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

عالی، بیایید کل کد را به‌طور کامل ببینیم:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // وارد کردن zod برای اعتبارسنجی طرح

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ممکن است در آینده نیاز به تغییر به این آدرس باشد: https://models.github.ai/inference
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
          // ایجاد یک طرح zod بر اساس input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // به طور صریح نوع را "function" تنظیم کنید
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
    
    
          // ۲. تماس با ابزار سرور
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // ۳. انجام کاری با نتیجه
          // باید انجام شود
    
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
    
        // ۳. پاسخ LLM را بررسی کنید، برای هر گزینه، بررسی کنید آیا تماس با ابزار دارد یا خیر
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

1. چند ایمپورت لازم برای فراخوانی LLM اضافه کنیم

    ```python
    # مدل زبان بزرگ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. سپس تابعی که LLM را فرا می‌خواند اضافه کنیم:

    ```python
    # مدل زبانی بزرگ

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

    در کد بالا ما:

    - توابعی که در سرور MCP یافتیم و تبدیل کردیم را به LLM داده‌ایم.
    - سپس LLM را با آن توابع فراخوانی کرده‌ایم.
    - سپس نتیجه را بررسی می‌کنیم تا ببینیم کدام توابع باید فراخوانی شوند.
    - در نهایت آرایه‌ای از توابع برای فراخوانی ارسال می‌کنیم.

3. مرحله آخر، حالا کد اصلی را به‌روزرسانی کنیم:

    ```python
    prompt = "Add 2 to 20"

    # به LLM بپرسید که چه ابزاری را به همه بدهد، در صورت وجود
    functions_to_call = call_llm(prompt, functions)

    # فراخوانی توابع پیشنهادی
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    اینجا آخرین مرحله است، در کد بالا:

    - ابزار MCP را از طریق `call_tool` فراخوانی می‌کنیم با تابعی که LLM فکر کرده باید فراخوانی شود.
    - نتیجه فراخوانی ابزار به سرور MCP چاپ می‌شود.

#### .NET

1. کدی برای درخواست پرامپت به LLM نشان می‌دهیم:

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

    در کد بالا ما:

    - ابزارها را از سرور MCP گرفته‌ایم، `var tools = await GetMcpTools()`.
    - پرامپت کاربر `userMessage` تعریف کرده‌ایم.
    - شیء گزینه‌هایی که مدل و ابزارها را مشخص می‌کند ساخته‌ایم.
    - درخواستی به سمت LLM ارسال کرده‌ایم.

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

    در کد بالا ما:

    - فهرستی از فراخوانی توابع را پیمایش کرده‌ایم.
    - برای هر فراخوانی ابزار، نام و آرگومان‌ها را پارس کرده و ابزار را روی سرور MCP با کلاینت MCP فراخوانی کرده‌ایم. در نهایت نتایج را چاپ کرده‌ایم.

در اینجا کل کد کامل آمده است:

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
    // اجرای درخواست‌های زبان طبیعی که به طور خودکار از ابزارهای MCP استفاده می‌کنند
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

در کد بالا ما:

- برای تعامل با ابزارهای سرور MCP از پرامپت‌های ساده زبان طبیعی استفاده کرده‌ایم
- چارچوب LangChain4j به‌صورت خودکار موارد زیر را مدیریت می‌کند:
  - تبدیل پرامپت‌های کاربر به فراخوانی ابزار در صورت نیاز
  - فراخوانی ابزارهای MCP مناسب با تصمیم LLM
  - مدیریت جریان مکالمه بین LLM و سرور MCP
- متد `bot.chat()` پاسخ‌های زبان طبیعی برمی‌گرداند که ممکن است شامل نتایج اجرای ابزارهای MCP باشد
- این رویکرد تجربه کاربری روانی فراهم می‌کند که کاربران نیازی به دانستن جزئیات پیاده‌سازی MCP ندارند

نمونه کد کامل:

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


در اینجا بخش عمده‌ای از کار انجام می‌شود. ما با پرامپت اولیه کاربر به LLM فراخوانی می‌کنیم، سپس پاسخ را پردازش می‌کنیم تا ببینیم آیا نیاز به فراخوانی هیچ ابزاری هست یا نه. اگر چنین باشد، آن ابزارها را فراخوانی می‌کنیم و گفتگو را با LLM ادامه می‌دهیم تا وقتی دیگر نیازی به فراخوانی ابزار نباشد و یک پاسخ نهایی داشته باشیم.

ما چندین بار به LLM فراخوانی خواهیم کرد، پس بیایید تابعی تعریف کنیم که فراخوانی LLM را مدیریت کند. تابع زیر را به فایل `main.rs` خود اضافه کنید:

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

این تابع کلاینت LLM، فهرستی از پیام‌ها (شامل پرامپت کاربر)، ابزارهای سرور MCP را دریافت می‌کند و درخواست را به LLM ارسال کرده و پاسخ را بازمی‌گرداند.

پاسخ از LLM شامل آرایه‌ای از `choices` خواهد بود. نیاز داریم نتیجه را پردازش کنیم تا ببینیم آیا `tool_calls` وجود دارد یا خیر. این موضوع به ما می‌گوید LLM درخواستی برای فراخوانی ابزاری مشخص با آرگومان‌هایی دارد. کد زیر را در انتهای فایل `main.rs` برای تعریف تابعی جهت مدیریت پاسخ LLM اضافه کنید:

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

    // چاپ محتوا در صورت وجود
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

        // ادامه مکالمه با نتایج ابزارها
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

اگر `tool_calls` وجود داشته باشد، اطلاعات ابزار را استخراج کرده، با درخواست ابزار به سرور MCP فراخوانی می‌کند و نتایج را به پیام‌های گفتگو اضافه می‌کند. پس از آن گفتگو را با LLM ادامه می‌دهد و پیام‌ها با پاسخ دستیار و نتایج فراخوانی ابزار به‌روزرسانی می‌شوند.

برای استخراج اطلاعات فراخوانی ابزار که LLM برای تماس‌های MCP برمی‌گرداند، تابع کمکی دیگری اضافه می‌کنیم تا همه آنچه برای انجام تماس لازم است استخراج شود. کد زیر را در انتهای فایل `main.rs` اضافه کنید:

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

با قرار گرفتن همه قطعات در جای خود، اکنون می‌توانیم پرامپت اولیه کاربر را مدیریت کرده و LLM را فراخوانی کنیم. تابع `main` خود را به شکل زیر به‌روزرسانی کنید:

```rust
// مکالمه‌ی LLM با فراخوانی ابزارها
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

این کد با پرامپت اولیه کاربر که درخواست جمع دو عدد است، LLM را فراخوانی می‌کند و پاسخ را به گونه‌ای پردازش می‌کند که بتواند فراخوانی‌های ابزار را به صورت پویا مدیریت کند.

عالی، انجامش دادی!

## تمرین

کد تمرین را بردارید و سرور را با چند ابزار بیشتر توسعه دهید. سپس مانند تمرین، یک کلاینت با LLM ایجاد کرده و آن را با پرامپت‌های مختلف امتحان کنید تا مطمئن شوید همه ابزارهای سرور شما به صورت پویا فراخوانی می‌شوند. این نوع ساخت کلاینت باعث می‌شود تجربه کاربری نهایی بسیار عالی باشد زیرا کاربران می‌توانند با پرامپت‌ها کار کنند، نه دستورهای دقیق کلاینت، و متوجه فراخوانی هیچ سرور MCP نشوند.

## راه‌حل

[راه‌حل](./solution/README.md)

## نکات کلیدی

- افزودن LLM به کلاینت شما، راه بهتری برای تعامل کاربران با سرورهای MCP فراهم می‌کند.
- شما باید پاسخ سرور MCP را به شکلی تبدیل کنید که LLM بتواند آن را بفهمد.

## نمونه‌ها

- [ماشین حساب Java](../samples/java/calculator/README.md)
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)
- [ماشین حساب JavaScript](../samples/javascript/README.md)
- [ماشین حساب TypeScript](../samples/typescript/README.md)
- [ماشین حساب Python](../../../../03-GettingStarted/samples/python)
- [ماشین حساب Rust](../../../../03-GettingStarted/samples/rust)

## منابع بیشتر

## مرحله بعد

- بعدی: [مصرف یک سرور با استفاده از Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->