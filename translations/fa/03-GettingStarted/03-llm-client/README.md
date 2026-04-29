# ایجاد یک کلاینت با LLM

تا کنون، شما دیده‌اید که چگونه یک سرور و یک کلاینت ایجاد کنید. کلاینت توانسته است به طور صریح سرور را برای فهرست کردن ابزارها، منابع و پرامپت‌ها صدا بزند. با این حال، این رویکرد چندان کاربردی نیست. کاربران شما در عصر هوشمندی عامل‌دار زندگی می‌کنند و انتظار دارند از پرامپت‌ها استفاده کنند و با یک LLM ارتباط برقرار کنند. آنها اهمیتی نمی‌دهند که شما از MCP برای ذخیره قابلیت‌های خود استفاده می‌کنید یا خیر؛ آنها صرفاً انتظار دارند با زبان طبیعی تعامل داشته باشند. پس چگونه این مشکل را حل کنیم؟ راه‌حل این است که یک LLM به کلاینت اضافه کنیم.

## نمای کلی

در این درس ما روی افزودن یک LLM به کلاینت تمرکز می‌کنیم و نشان می‌دهیم چگونه این موضوع تجربه بسیار بهتری برای کاربر شما فراهم می‌آورد.

## اهداف یادگیری

تا پایان این درس، شما قادر خواهید بود:

- ایجاد یک کلاینت با یک LLM.
- تعامل بدون درز با یک سرور MCP با استفاده از یک LLM.
- فراهم آوردن تجربه بهتر برای کاربر نهایی در سمت کلاینت.

## رویکرد

بیایید تلاش کنیم رویکردی که باید اتخاذ کنیم را بفهمیم. افزودن یک LLM ساده به نظر می‌رسد، اما آیا واقعاً این کار را انجام خواهیم داد؟

در اینجا نحوه تعامل کلاینت با سرور است:

1. برقرار کردن اتصال با سرور.

1. فهرست کردن قابلیت‌ها، پرامپت‌ها، منابع و ابزارها و ذخیره کردن ساختار آنها.

1. افزودن یک LLM و ارسال قابلیت‌ها و ساختار ذخیره شده به فرمت قابل فهم برای LLM.

1. رسیدگی به پرامپت کاربر با ارسال آن به LLM همراه با ابزارهای فهرست‌شده توسط کلاینت.

عالی، حالا که در سطح کلی فهمیدیم چگونه این کار را انجام دهیم، بیایید در تمرین زیر آن را امتحان کنیم.

## تمرین: ایجاد یک کلاینت با یک LLM

در این تمرین، یاد می‌گیریم چگونه یک LLM به کلاینت خود اضافه کنیم.

### احراز هویت با توکن دسترسی شخصی GitHub

ساخت توکن GitHub فرایند ساده‌ای است. این‌گونه عمل می‌کنید:

- به تنظیمات GitHub بروید – روی عکس پروفایل خود در گوشه بالا سمت راست کلیک کرده و Settings را انتخاب کنید.
- به بخش تنظیمات توسعه‌دهنده بروید – پایین صفحه اسکرول کرده و روی Developer Settings کلیک کنید.
- انتخاب توکن‌های دسترسی شخصی – روی Fine-grained tokens کلیک کرده و سپس Generate new token را انتخاب کنید.
- پیکربندی توکن شما – یک یادداشت برای مرجع اضافه کنید، تاریخ انقضا تنظیم کنید و مجوزهای لازم (Scopes) را انتخاب کنید. در این حالت حتماً مجوز Models را اضافه کنید.
- توکن را ایجاد و کپی کنید – روی Generate token کلیک کنید و حتماً فوراً آن را کپی کنید، چون دوباره قادر به دیدن آن نخواهید بود.

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

- کتابخانه‌های مورد نیاز را وارد کردیم
- کلاسی با دو عضو `client` و `openai` ساختیم که به ما در مدیریت کلاینت و تعامل با LLM کمک می‌کنند.
- نمونه LLM خود را برای استفاده از GitHub Models پیکربندی کردیم با تنظیم `baseUrl` برای اشاره به API استنتاج.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# ایجاد پارامترهای سرور برای اتصال stdio
server_params = StdioServerParameters(
    command="mcp",  # اجرایی
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

در کد بالا ما:

- کتابخانه‌های مورد نیاز برای MCP را وارد کردیم
- یک کلاینت ساختیم

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

ابتدا باید وابستگی‌های LangChain4j را به فایل `pom.xml` خود اضافه کنید. این وابستگی‌ها را برای فعال‌سازی ادغام MCP و پشتیبانی از GitHub Models اضافه کنید:

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

سپس کلاس کلاینت Java خود را ایجاد کنید:

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
    
    public static void main(String[] args) throws Exception {        // پیکربندی LLM برای استفاده از مدل‌های GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
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
}
```

در کد بالا ما:

- **وابستگی‌های LangChain4j را اضافه کردیم**: مورد نیاز برای ادغام MCP، کلاینت رسمی OpenAI و پشتیبانی از GitHub Models
- **کتابخانه‌های LangChain4j را وارد کردیم**: برای ادغام MCP و قابلیت چت مدل OpenAI
- **یک `ChatLanguageModel` ساختیم**: که برای استفاده از GitHub Models با توکن GitHub شما پیکربندی شده است
- **انتقال HTTP را تنظیم کردیم**: با استفاده از Server-Sent Events (SSE) برای اتصال به سرور MCP
- **یک کلاینت MCP ایجاد کردیم**: که ارتباط با سرور را مدیریت می‌کند
- **از پشتیبانی داخلی LangChain4j برای MCP استفاده کردیم**: که ادغام بین LLM ها و سرورهای MCP را ساده می‌کند

#### Rust

این مثال فرض می‌کند که شما یک سرور MCP بر پایه Rust دارید. اگر ندارید، به درس [01-first-server](../01-first-server/README.md) مراجعه کنید تا سرور را بسازید.

وقتی سرور MCP Rust خود را دارید، یک ترمینال باز کنید و به همان پوشه سرور بروید. سپس دستور زیر را برای ایجاد یک پروژه کلاینت LLM جدید اجرا کنید:

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
> کتابخانه رسمی Rust برای OpenAI وجود ندارد، اما crate `async-openai` یک [کتابخانه نگهداری‌شده توسط جامعه](https://platform.openai.com/docs/libraries/rust#rust) است که معمولاً استفاده می‌شود.

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

    // انجام شود: دریافت فهرست ابزارهای MCP

    // انجام شود: گفت‌وگوی LLM با فراخوانی ابزارها

    Ok(())
}
```

این کد یک برنامه پایه Rust را راه‌اندازی می‌کند که به سرور MCP و GitHub Models برای تعاملات LLM متصل می‌شود.

> [!IMPORTANT]
> قبل از اجرای برنامه، مطمئن شوید متغیر محیطی `OPENAI_API_KEY` را با توکن GitHub خود تنظیم کرده‌اید.

عالی، برای مرحله بعد، اجازه دهید قابلیت‌های روی سرور را فهرست کنیم.

### -2- فهرست کردن قابلیت‌های سرور

حالا به سرور متصل می‌شویم و از آن قابلیت‌ها را درخواست می‌کنیم:

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

- کد اتصال به سرور، `connectToServer` را اضافه کردیم.
- متد `run` را ایجاد کردیم که مسئول مدیریت جریان برنامه ماست. تا کنون فقط ابزارها را فهرست می‌کند ولی به زودی وظایف بیشتری به آن اضافه خواهیم کرد.

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

اینجا آنچه اضافه کردیم:

- فهرست کردن منابع و ابزارها و چاپ آنها. برای ابزارها همچنین `inputSchema` که بعدا استفاده خواهیم کرد را فهرست کردیم.

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

در کد بالا ما:

- ابزارهای موجود روی سرور MCP را فهرست کردیم
- برای هر ابزار، نام، توضیح و ساختار آن را فهرست کردیم. مورد آخر چیزی است که به زودی برای فراخوانی ابزارها استفاده خواهیم کرد.

#### Java

```java
// ایجاد یک ارائه‌دهنده ابزار که به‌طور خودکار ابزارهای MCP را کشف می‌کند
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ارائه‌دهنده ابزار MCP به‌طور خودکار موارد زیر را مدیریت می‌کند:
// - فهرست کردن ابزارهای موجود از سرور MCP
// - تبدیل شمای ابزار MCP به فرمت LangChain4j
// - مدیریت اجرای ابزار و پاسخ‌ها
```

در کد بالا ما:

- یک `McpToolProvider` ساختیم که به طور خودکار همه ابزارهای سرور MCP را کشف و ثبت می‌کند
- این تامین‌کننده ابزار تبدیل ساختارهای ابزار MCP به فرمت ابزار LangChain4j را به صورت داخلی مدیریت می‌کند
- این رویکرد فرایند فهرست‌بندی و تبدیل ابزارهای دستی را حذف می‌کند

#### Rust

دریافت ابزارها از سرور MCP با استفاده از متد `list_tools` انجام می‌شود. در تابع `main` خود، پس از تنظیم کلاینت MCP، کد زیر را اضافه کنید:

```rust
// گرفتن فهرست ابزار MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- تبدیل قابلیت‌های سرور به ابزارهای LLM

مرحله بعدی پس از فهرست کردن قابلیت‌های سرور، تبدیل آنها به فرمتی است که LLM می‌فهمد. وقتی این کار را انجام دادیم، می‌توانیم این قابلیت‌ها را به عنوان ابزار به LLM خود ارائه کنیم.

#### TypeScript

1. کد زیر را اضافه کنید تا پاسخ از سرور MCP به فرمت ابزاری تبدیل شود که LLM می‌تواند استفاده کند:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // یک اسکیمای زاد بر اساس ورودی اسکیمای ایجاد کنید
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // نوع را به صراحت به "function" تنظیم کنید
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

    کد بالا پاسخ از سرور MCP را می‌گیرد و آن را به فرمت تعریف ابزار تبدیل می‌کند که LLM می‌تواند بفهمد.

1. حالا متد `run` را برای فهرست کردن قابلیت‌های سرور به روز کنیم:

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

    در کد بالا، متد `run` را بروز کردیم تا روی نتیجه پیمایش کند و برای هر ورودی `openAiToolAdapter` را فراخوانی نماید.

#### Python

1. اول، تابع تبدیل زیر را بسازیم

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

    در تابع `convert_to_llm_tools` پاسخ ابزار MCP را می‌گیریم و آن را به فرمتی تبدیل می‌کنیم که LLM متوجه شود.

1. سپس کد کلاینت خود را به گونه‌ای به‌روزرسانی کنیم که از این تابع بهره ببرد:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    اینجا ما فراخوانی به `convert_to_llm_tool` اضافه کرده‌ایم تا پاسخ ابزار MCP را به چیزی تبدیل کنیم که بعداً به LLM ارائه می‌دهیم.

#### .NET

1. اضافه کنیم کدی برای تبدیل پاسخ ابزار MCP به چیزی که LLM درک کند

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

- تابع `ConvertFrom` را ساختیم که نام، توضیح و ساختار ورودی می‌گیرد.
- عملکردی تعریف کردیم که یک `FunctionDefinition` ایجاد می‌کند که به `ChatCompletionsDefinition` ارسال می‌شود. مورد اخیر را LLM می‌فهمد.

1. ببینیم چگونه می‌توانیم برخی کدهای موجود را برای بهره بردن از این تابع به‌روزرسانی کنیم:

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

- یک اینترفیس ساده `Bot` برای تعاملات زبان طبیعی تعریف کرده‌ایم
- از `AiServices` LangChain4j استفاده کردیم تا به طور خودکار LLM را با تامین‌کننده ابزار MCP پیوند دهد
- این چارچوب به طور خودکار تبدیل ساختار ابزار و فراخوانی توابع را پشت صحنه مدیریت می‌کند
- این رویکرد تبدیل دستی ابزار را حذف می‌کند - LangChain4j تمام پیچیدگی‌های تبدیل ابزار MCP به فرمت سازگار با LLM را مدیریت می‌کند

#### Rust

برای تبدیل پاسخ ابزار MCP به فرمتی که LLM بفهمد، تابع کمکی اضافه می‌کنیم که فهرست ابزارها را قالب‌بندی کند. کد زیر را در فایل `main.rs` در زیر تابع `main` اضافه کنید. این زمانی فراخوانی می‌شود که به LLM درخواست می‌دهیم:

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

خوب، حالا ما آماده‌ایم درخواست‌های کاربر را مدیریت کنیم، پس این بخش را دنبال می‌کنیم.

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


        // ۲. ابزار سرور را فراخوانی کنید
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳. کاری با نتیجه انجام دهید
        // انجام دادن

        }
    }
    ```

    در کد بالا ما:

    - متد `callTools` را اضافه کردیم.
    - این متد پاسخ LLM را می‌گیرد و بررسی می‌کند چه ابزاری باید فراخوانی شود، اگر باشد:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // فراخوانی ابزار
        }
        ```

    - اگر LLM اعلام کند باید فراخوانی شود، یک ابزار را صدا می‌زند:

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

1. متد `run` را بروز کنیم تا شامل فراخوانی‌های LLM و `callTools` شود:

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

    // ۳. بررسی پاسخ مدل زبان بزرگ، برای هر گزینه، چک کنید که آیا فراخوانی ابزار دارد یا نه
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

عالی، حالا کد کامل را فهرست کنیم:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // وارد کردن zod برای اعتبارسنجی طرح‌واره

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
          // ایجاد یک طرح‌واره zod بر اساس input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // به‌صراحت نوع را روی "function" تنظیم کنید
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
          // انجام شود
    
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
    
        // ۱. بررسی پاسخ LLM، برای هر گزینه، چک کنید آیا فراخوانی ابزار دارد
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

1. برخی ایمپورت‌های مورد نیاز برای فراخوانی LLM را اضافه کنیم

    ```python
    # مدل زبان بزرگ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. سپس تابعی که LLM را فراخوانی می‌کند اضافه کنیم:

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

    در کد بالا ما:

    - توابعی که روی سرور MCP یافتیم و تبدیل کردیم را به LLM پاس دادیم.
    - سپس LLM را با این توابع فراخوانی کردیم.
    - نتیجه را بررسی می‌کنیم تا ببینیم کدام توابع باید فراخوانی شوند، اگر باشد.
    - نهایتاً فهرستی از توابع برای فراخوانی می‌فرستیم.

1. آخرین مرحله، کد اصلی خود را بروز کنیم:

    ```python
    prompt = "Add 2 to 20"

    # از LLM بپرسید که چه ابزارهایی به همه اعمال شود، اگر وجود داشته باشد
    functions_to_call = call_llm(prompt, functions)

    # فراخوانی توابع پیشنهادی
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    آنجا بود، مرحله آخر، در کد بالا ما:

    - یک ابزار MCP را از طریق `call_tool` فراخوانی می‌کنیم با استفاده از تابعی که LLM فکر کرد بر اساس پرامپت باید فراخوانی شود.
    - نتیجه فراخوانی ابزار به سرور MCP را چاپ می‌کنیم.

#### .NET

1. کدی برای درخواست پرامپت LLM نمایش دهیم:

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
    - پرامپت کاربر `userMessage` را تعریف کرده‌ایم.
    - شی گزینه‌ای تعریف کردیم با مدل و ابزارها.
    - درخواست به سمت LLM ساخته‌ایم.

1. یک قدم آخر، ببینیم آیا LLM فکر می‌کند باید تابعی را فراخوانی کنیم:

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

    - برای لیستی از فراخوانی‌های توابع حلقه زدیم.
    - برای هر فراخوانی ابزار، نام و آرگومان‌ها را تجزیه کرده و ابزار را روی سرور MCP با استفاده از کلاینت MCP فراخوانی می‌کنیم. در نهایت نتایج را چاپ می‌کنیم.

کد کامل اینجا است:

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
    // درخواست‌های زبان طبیعی را اجرا کنید که به طور خودکار از ابزارهای MCP استفاده می‌کنند
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

- از پرامپت‌های ساده زبان طبیعی برای تعامل با ابزارهای سرور MCP استفاده کرده‌ایم
- چارچوب LangChain4j به طور خودکار مدیریت می‌کند:
  - تبدیل پرامپت‌های کاربر به فراخوانی ابزار در صورت نیاز
  - فراخوانی ابزارهای MCP مناسب بر اساس تصمیم LLM
  - مدیریت جریان گفت‌وگو بین LLM و سرور MCP
- متد `bot.chat()` پاسخ‌های زبان طبیعی باز می‌گرداند که ممکن است شامل نتایج اجرای ابزارهای MCP باشد
- این رویکرد تجربه‌ای روان برای کاربر فراهم می‌کند که نیاز نیست کاربران با پیاده‌سازی زیرساختی MCP آشنا باشند

مثال کد کامل:

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

اینجا بیشتر کار انجام می‌شود. ما با پرامپت اولیه کاربر به LLM فراخوانی می‌زنیم، سپس پاسخ را بررسی می‌کنیم تا ببینیم آیا باید ابزاری را صدا بزنیم یا نه. اگر چنین بود، آن ابزارها را صدا می‌زنیم و گفت‌وگو را با LLM ادامه می‌دهیم تا دیگر نیازی به فراخوانی ابزار نباشد و پاسخ نهایی داشته باشیم.

چندین بار به LLM فراخوانی می‌زنیم، پس بیایید تابعی تعریف کنیم که فراخوانی LLM را مدیریت می‌کند. کد زیر را به فایل `main.rs` خود اضافه کنید:

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

این تابع کلاینت LLM، فهرستی از پیام‌ها (از جمله پرامپت کاربر) و ابزارهای سرور MCP را می‌گیرد و درخواست را به LLM می‌فرستد و پاسخ را بازمی‌گرداند.
پاسخ از LLM شامل آرایه‌ای از `choices` خواهد بود. ما باید نتیجه را پردازش کنیم تا ببینیم آیا هیچ `tool_calls` وجود دارد یا خیر. این به ما اطلاع می‌دهد که LLM درخواست می‌کند ابزار مشخصی با آرگومان‌ها فراخوانی شود. کد زیر را به انتهای فایل `main.rs` خود اضافه کنید تا تابعی برای مدیریت پاسخ LLM تعریف شود:

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

    // مدیریت فراخوانی‌های ابزار
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

        // ادامه مکالمه با نتایج ابزار
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
  
اگر `tool_calls` وجود داشته باشد، اطلاعات ابزار استخراج شده، درخواست ابزار به سرور MCP فرستاده می‌شود و نتایج به پیام‌های مکالمه اضافه می‌گردد. سپس مکالمه با LLM ادامه پیدا می‌کند و پیام‌ها با پاسخ دستیار و نتایج فراخوانی ابزار به‌روزرسانی می‌شوند.

برای استخراج اطلاعات فراخوانی ابزار که LLM برای تماس‌های MCP برمی‌گرداند، یک تابع کمکی دیگر اضافه می‌کنیم تا همه موارد لازم برای انجام فراخوانی را استخراج کند. کد زیر را به انتهای فایل `main.rs` خود اضافه کنید:

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
  
با تمام قطعات در جای خود، اکنون می‌توانیم درخواست اولیه کاربر را مدیریت کرده و LLM را فراخوانی کنیم. تابع `main` خود را به شکل زیر به‌روزرسانی کنید:

```rust
// گفتگوی LLM با فراخوانی ابزارها
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
  
این کد با درخواست اولیه کاربر برای جمع دو عدد از LLM پرسش می‌کند و پاسخ را به‌گونه‌ای پردازش می‌کند که فراخوانی ابزارها به صورت پویا مدیریت شود.

آفرین، موفق شدی!

## تمرین

کدی که در تمرین استفاده کردید را بگیرید و سرور را با ابزارهای بیشتری گسترش دهید. سپس یک کلاینت با LLM بسازید، مانند تمرین، و آن را با درخواست‌های مختلف آزمایش کنید تا مطمئن شوید همه ابزارهای سرور شما به‌صورت داینامیک فراخوانی می‌شوند. این شیوه ساخت کلاینت باعث می‌شود تجربه کاربری فوق‌العاده‌ای برای کاربران فراهم شود، زیرا آن‌ها می‌توانند با درخواست‌ها به جای دستورات دقیق کلاینت کار کنند و از فراخوانی هر سرور MCP بی‌خبر باشند.

## راه‌حل

[راه‌حل](./solution/README.md)

## نکات کلیدی

- اضافه کردن LLM به کلاینت شما راه بهتری برای تعامل کاربران با سرورهای MCP فراهم می‌کند.
- شما باید پاسخ سرور MCP را به چیزی تبدیل کنید که LLM بتواند درک کند.

## نمونه‌ها

- [ماشین حساب جاوا](../samples/java/calculator/README.md)  
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)  
- [ماشین حساب جاوااسکریپت](../samples/javascript/README.md)  
- [ماشین حساب تایپ‌اسکریپت](../samples/typescript/README.md)  
- [ماشین حساب پایتون](../../../../03-GettingStarted/samples/python)  
- [ماشین حساب راست](../../../../03-GettingStarted/samples/rust)

## منابع اضافی

## بعدی چیست

- بعدی: [استفاده از سرور با استفاده از Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، استفاده از ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده از این ترجمه به وجود آید، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->