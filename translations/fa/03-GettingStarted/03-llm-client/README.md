# ایجاد یک کلاینت با LLM

تا کنون، نحوه ایجاد یک سرور و یک کلاینت را دیده‌اید. کلاینت توانسته صریحاً سرور را برای لیست ابزارها، منابع و پرامپت‌های آن فرا بخواند. با این حال، این رویکرد چندان عملی نیست. کاربران شما در عصر عامل‌محور زندگی می‌کنند و انتظار دارند از پرامپت‌ها استفاده کنند و با یک LLM ارتباط برقرار نمایند. آنها اهمیتی نمی‌دهند که شما از MCP برای ذخیره قابلیت‌های خود استفاده می‌کنید یا نه؛ آنها صرفاً انتظار تعامل با زبان طبیعی دارند. پس چگونه این مسئله را حل کنیم؟ راه حل اضافه کردن یک LLM به کلاینت است.

## مرور کلی

در این درس تمرکز ما بر افزودن یک LLM به کلاینت شماست و نشان می‌دهیم چگونه این تجربه به مراتب بهتر برای کاربر نهایی فراهم می‌کند.

## اهداف یادگیری

تا پایان این درس، شما قادر خواهید بود:

- ایجاد یک کلاینت با یک LLM.
- تعامل بی‌درنگ با یک سرور MCP با استفاده از LLM.
- ارائه تجربه بهتر برای کاربر نهایی در سمت کلاینت.

## رویکرد

بیایید رویکردی را که باید اتخاذ کنیم درک کنیم. افزودن یک LLM ساده به نظر می‌رسد، اما آیا واقعاً این کار را انجام خواهیم داد؟

نحوه تعامل کلاینت با سرور به شرح زیر است:

1. برقراری اتصال با سرور.

1. لیست کردن قابلیت‌ها، پرامپت‌ها، منابع و ابزارها، و ذخیره‌ی اسکیمای آنها.

1. افزودن یک LLM و ارسال قابلیت‌های ذخیره‌شده همراه با اسکیمای آن‌ها به فرمتی که LLM می‌فهمد.

1. مدیریت یک پرامپت کاربر با ارسال آن به LLM همراه با ابزارهای فهرست‌شده توسط کلاینت.

عالی است، اکنون که فهمیدیم چطور می‌توانیم این کار را در سطح بالا انجام دهیم، بیایید این را در تمرین زیر اجرا کنیم.

## تمرین: ایجاد یک کلاینت با یک LLM

در این تمرین، یاد می‌گیریم چگونه یک LLM را به کلاینت خود اضافه کنیم.

### احراز هویت با استفاده از توکن دسترسی شخصی GitHub

ایجاد یک توکن GitHub فرآیندی ساده است. این‌گونه می‌توانید این کار را انجام دهید:

- رفتن به تنظیمات GitHub – روی عکس پروفایل خود در گوشه بالا سمت راست کلیک کرده و Settings را انتخاب کنید.
- رفتن به تنظیمات توسعه‌دهنده – صفحه را به پایین اسکرول کرده و روی Developer Settings کلیک کنید.
- انتخاب توکن‌های دسترسی شخصی – روی Fine-grained tokens کلیک کرده و سپس Generate new token را انتخاب کنید.
- پیکربندی توکن خود – یک یادداشت برای مرجع اضافه کنید، تاریخ انقضا تنظیم کنید و مجوزهای لازم را انتخاب نمایید. در این مورد مطمئن شوید مجوز Models را اضافه کرده‌اید.
- تولید و کپی توکن – روی Generate token کلیک کنید و حتماً فوراً آن را کپی نمایید زیرا دیگر قادر به مشاهده دوباره آن نخواهید بود.

### -1- اتصال به سرور

بیایید ابتدا کلاینت خود را ایجاد کنیم:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // وارد کردن Zod برای اعتبارسنجی اسکیمای داده‌ها

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
- یک کلاس با دو عضو `client` و `openai` ایجاد کرده‌ایم که به ترتیب به ما در مدیریت کلاینت و تعامل با LLM کمک می‌کنند.  
- نمونه LLM خود را پیکربندی کردیم تا از GitHub Models استفاده کند با تنظیم `baseUrl` به API استنتاج.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# ایجاد پارامترهای سرور برای اتصال استاندارد ورودی و خروجی
server_params = StdioServerParameters(
    command="mcp",  # فایل اجرایی
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

- کتابخانه‌های مورد نیاز برای MCP را وارد کردیم  
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
  
#### Java

ابتدا باید وابستگی‌های LangChain4j را به فایل `pom.xml` خود اضافه کنید. این وابستگی‌ها را اضافه کنید تا یکپارچگی MCP و پشتیبانی از GitHub Models فعال شود:

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

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // پیکربندی LLM برای استفاده از مدل‌های گیت‌هاب
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

- **وابستگی‌های LangChain4j را اضافه کرده‌ایم**: برای یکپارچگی MCP، کلاینت رسمی OpenAI و پشتیبانی GitHub Models  
- **کتابخانه‌های LangChain4j را وارد کرده‌ایم**: برای یکپارچگی MCP و عملکرد مدل چت OpenAI  
- **یک `ChatLanguageModel` ایجاد کرده‌ایم**: که برای استفاده از GitHub Models با توکن GitHub شما پیکربندی شده است  
- **HTTP transport را راه‌اندازی کرده‌ایم**: با استفاده از Server-Sent Events (SSE) برای اتصال به سرور MCP  
- **یک کلاینت MCP ایجاد کرده‌ایم**: که مسئول ارتباط با سرور است  
- **از پشتیبانی داخلی MCP در LangChain4j استفاده کرده‌ایم**: که یکپارچگی بین LLM و سرورهای MCP را ساده می‌کند

#### Rust

این مثال فرض می‌کند شما یک سرور MCP مبتنی بر Rust در حال اجرا دارید. اگر ندارید، به درس [01-first-server](../01-first-server/README.md) بازگردید تا سرور را ایجاد کنید.

پس از اینکه سرور Rust MCP خود را داشتید، یک ترمینال باز کرده و به همان دایرکتوری سرور بروید. سپس فرمان زیر را برای ایجاد یک پروژه کلاینت LLM جدید اجرا کنید:

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
> کتابخانه رسمی Rust برای OpenAI وجود ندارد، اما crate `async-openai` یک [کتابخانه تحت نگهداری جامعه](https://platform.openai.com/docs/libraries/rust#rust) است که معمولاً استفاده می‌شود.

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

    // کارهای انجام‌دادنی: دریافت فهرست ابزار MCP

    // کارهای انجام‌دادنی: مکالمه LLM با فراخوانی ابزارها

    Ok(())
}
```
  
این کد یک برنامه Rust پایه راه‌اندازی می‌کند که به یک سرور MCP و GitHub Models برای تعاملات LLM اتصال می‌یابد.

> [!IMPORTANT]  
> مطمئن شوید قبل از اجرای برنامه متغیر محیطی `OPENAI_API_KEY` را با توکن GitHub خود تنظیم کرده‌اید.

عالی است، برای مرحله بعد بیایید قابلیت‌های سرور را فهرست کنیم.

### -2- فهرست کردن قابلیت‌های سرور

حالا به سرور متصل می‌شویم و قابلیت‌های آن را درخواست می‌کنیم:

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

    // فهرست ابزارها
    const toolsResult = await this.client.listTools();
}
```
  
در کد بالا ما:

- کد اتصال به سرور، `connectToServer` را اضافه کردیم.  
- متد `run` را ایجاد کردیم که مسئول مدیریت جریان برنامه ما است. تاکنون فقط ابزارها را لیست می‌کند اما به زودی موارد بیشتری اضافه می‌کنیم.

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
  
موارد افزوده شده:

- منابع و ابزارها را فهرست کردیم و چاپ کردیم. برای ابزارها همچنین `inputSchema` را که بعداً استفاده می‌کنیم، فهرست کردیم.

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

- ابزارهای موجود روی سرور MCP را لیست کردیم  
- برای هر ابزار، نام، توضیحات و اسکیمای آن را فهرست کردیم. اسکیمای ابزار برای فراخوانی ابزارها به کار می‌رود.

#### Java

```java
// ایجاد یک تامین‌کننده ابزار که به‌طور خودکار ابزارهای MCP را کشف می‌کند
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// تامین‌کننده ابزار MCP به‌طور خودکار موارد زیر را مدیریت می‌کند:
// - فهرست کردن ابزارهای موجود از سرور MCP
// - تبدیل ساختارهای ابزار MCP به فرمت LangChain4j
// - مدیریت اجرای ابزار و پاسخ‌ها
```
  
در کد بالا ما:

- یک `McpToolProvider` ایجاد کردیم که به‌طور خودکار همه ابزارها را از سرور MCP کشف و ثبت می‌کند  
- این ابزار ارائه‌دهنده تبدیل بین اسکیمای ابزار MCP و فرمت ابزار LangChain4j را به صورت داخلی مدیریت می‌کند  
- این رویکرد فرآیند فهرست‌بندی و تبدیل دستی ابزارها را حذف می‌کند

#### Rust

دریافت ابزارها از سرور MCP با استفاده از متد `list_tools` انجام می‌شود. در تابع `main` خود، پس از راه‌اندازی کلاینت MCP، کد زیر را اضافه کنید:

```rust
// دریافت لیست ابزار MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```
  
### -3- تبدیل قابلیت‌های سرور به ابزارهای LLM

مرحله بعدی پس از فهرست قابلیت‌های سرور، تبدیل آنها به فرمتی است که LLM بتواند بفهمد. وقتی این کار را انجام دادیم، می‌توانیم این قابلیت‌ها را به عنوان ابزار به LLM ارائه دهیم.

#### TypeScript

1. کد زیر را برای تبدیل پاسخ از سرور MCP به فرمتی که LLM می‌تواند استفاده کند اضافه کنید:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ایجاد یک اسکیمای زاد بر اساس input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // نوع را صراحتاً روی "function" تنظیم کنید
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
  
کد بالا پاسخ سرور MCP را می‌گیرد و آن را به فرمت تعریف ابزار تبدیل می‌کند که LLM آن را درک می‌کند.

1. حالا متد `run` را برای فهرست کردن قابلیت‌های سرور به‌روزرسانی می‌کنیم:

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
  
در کد بالا متد `run` را برای پیمایش نتایج و فراخوانی `openAiToolAdapter` برای هر مورد به‌روزرسانی کرده‌ایم.

#### Python

1. ابتدا تابع مبدل زیر را ایجاد می‌کنیم:

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
  
در تابع `convert_to_llm_tools`، پاسخ ابزار MCP را گرفته و به فرمت قابل فهم برای LLM تبدیل می‌کنیم.

1. سپس کد کلاینت را برای استفاده از این تابع به شکل زیر به‌روزرسانی می‌کنیم:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```
  
در اینجا، یک فراخوانی به `convert_to_llm_tool` اضافه کرده‌ایم تا پاسخ ابزار MCP را به فرمتی تبدیل کنیم که بعداً به LLM ارسال می‌کنیم.

#### .NET

1. کدی برای تبدیل پاسخ ابزار MCP به فرمتی که LLM می‌تواند بفهمد اضافه کنیم:

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
  
در کد بالا:

- تابع `ConvertFrom` را ساخته‌ایم که نام، توضیح و اسکیمای ورودی را می‌گیرد.  
- عملکردی تعریف کردیم که یک `FunctionDefinition` می‌سازد که به `ChatCompletionsDefinition` منتقل می‌شود. دومی چیزی است که LLM می‌تواند بفهمد.

1. حالا بیایید بعضی از کدهای موجود را به‌روزرسانی کنیم تا از این تابع استفاده کنیم:

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
  
در کد بالا:

- یک اینترفیس ساده `Bot` برای تعاملات زبان طبیعی تعریف کرده‌ایم  
- از `AiServices` LangChain4j استفاده کردیم که به طور خودکار LLM را با ارائه‌دهنده ابزار MCP متصل می‌کند  
- این چارچوب به طور خودکار تبدیل اسکیمای ابزار و فراخوانی توابع را پشت صحنه مدیریت می‌کند  
- این رویکرد تبدیل دستی ابزارها را حذف می‌کند - LangChain4j تمام پیچیدگی تبدیل ابزارهای MCP به فرمت سازگار با LLM را مدیریت می‌کند

#### Rust

برای تبدیل پاسخ ابزار MCP به فرمتی که LLM درک کند، یک تابع کمکی اضافه می‌کنیم که فهرست ابزارها را قالب‌بندی می‌کند. کد زیر را در فایل `main.rs` خود، در زیر تابع `main` اضافه کنید. این تابع هنگام ارسال درخواست به LLM فراخوانی می‌شود:

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
  
عالی، حالا آماده‌ایم درخواست‌های کاربر را مدیریت کنیم.

### -4- مدیریت درخواست پرامپت کاربر

در این بخش کد، درخواست‌های کاربران را مدیریت خواهیم کرد.

#### TypeScript

1. یک متد اضافه کنید که برای فراخوانی LLM استفاده خواهد شد:

    ```typescript
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
        // باید انجام شود

        }
    }
    ```
  
در کد بالا ما:

- متد `callTools` را اضافه کردیم.  
- این متد پاسخ LLM را می‌گیرد و بررسی می‌کند کدام ابزارها فراخوانی شده‌اند، اگر وجود داشته باشند:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // فراخوانی ابزار
        }
        ```
  
- فراخوانی یک ابزار، اگر LLM نشان دهد باید فراخوانی شود:

        ```typescript
        // ۲. ابزار سرور را صدا بزنید
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ۳. کاری با نتیجه انجام دهید
        // انجام شود
        ```
  
1. متد `run` را به‌روزرسانی کنید تا فراخوانی‌های LLM و `callTools` را شامل شود:

    ```typescript

    // ۱. ایجاد پیام‌هایی که ورودی برای مدل زبان بزرگ هستند
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ۲. فراخوانی مدل زبان بزرگ
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ۳. بررسی پاسخ مدل زبان بزرگ، برای هر گزینه، چک کنید آیا فراخوانی ابزار دارد یا خیر
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```
  
عالی، بیایید کد کامل را فهرست کنیم:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // وارد کردن zod برای اعتبارسنجی اسکما

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
          // ایجاد یک اسکما zod بر اساس input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // نوع را صراحتاً روی "function" تنظیم کنید
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
          // انجام دهید
    
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
    
        // ۱. بررسی پاسخ LLM، برای هر انتخاب، بررسی کنید که آیا فراخوانی ابزار دارد یا نه
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

1. واردات مورد نیاز برای فراخوانی LLM را اضافه کنیم:

    ```python
    # مدل زبان بزرگ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```
  
1. سپس تابعی برای فراخوانی LLM اضافه کنیم:

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
  
در کد بالا:

- توابعی که قبلاً از سرور MCP دریافت و تبدیل کرده‌ایم، به LLM ارسال می‌شوند.  
- سپس LLM را با این توابع فراخوانی می‌کنیم.  
- نتیجه را بررسی می‌کنیم تا ببینیم کدام توابع باید فراخوانی شوند، اگر وجود داشته باشند.  
- در نهایت آرایه‌ای از توابع برای فراخوانی می‌فرستیم.

1. مرحله نهایی، کد اصلی خود را به‌روزرسانی کنیم:

    ```python
    prompt = "Add 2 to 20"

    # از مدل زبان بزرگ بپرسید که چه ابزارهایی برای همه موجود است، اگر اصلاً وجود داشته باشد
    functions_to_call = call_llm(prompt, functions)

    # توابع پیشنهادی را فراخوانی کنید
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```
  
در کد بالا:

- یک ابزار MCP را از طریق `call_tool` فراخوانی می‌کنیم که بر اساس پرامپت LLM انتخاب شده است.  
- نتیجه فراخوانی ابزار را چاپ می‌کنیم.

#### .NET

1. کد نمونه‌ای برای درخواست پرامپت به LLM را ببینیم:

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
  
در کد بالا:

- ابزارها را از سرور MCP واکشی کرده‌ایم، `var tools = await GetMcpTools()`  
- پرامپت کاربر را `userMessage` تعریف کرده‌ایم  
- شیء گزینه‌ها را با مدل و ابزارها ساخته‌ایم  
- درخواست به LLM ارسال شده است

1. مرحله آخر، بیایید ببینیم آیا LLM فکر می‌کند باید تابعی فراخوانی شود یا خیر:

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
  
در کد بالا:

- روی لیست فراخوانی توابع حلقه زده‌ایم  
- برای هر فراخوانی ابزار، نام و آرگومان‌ها را استخراج کرده‌ایم و ابزار روی سرور MCP را با کلاینت MCP فراخوانی نموده‌ایم. نهایتاً نتایج چاپ می‌شوند.

کد کامل:

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
  
در کد بالا:

- از پرامپت‌های ساده زبان طبیعی برای تعامل با ابزارهای سرور MCP استفاده کرده‌ایم  
- چارچوب LangChain4j به طور خودکار:  
  - تبدیل پرامپت‌های کاربر به فراخوانی ابزارها در صورت نیاز  
  - فراخوانی ابزارهای MCP مناسب بر اساس تصمیم LLM  
  - مدیریت جریان گفتگو بین LLM و سرور MCP  
- متد `bot.chat()` پاسخ‌های زبان طبیعی بازمی‌گرداند که ممکن است شامل نتایج اجرای ابزارهای MCP باشند  
- این رویکرد تجربه کاربری یکپارچه‌ای ارائه می‌دهد که کاربران نیازی به دانستن جزئیات زیرساخت MCP ندارند

مثال کامل کد:

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

اینجا بخش عمده کار انجام می‌شود. ابتدا LLM را با پرامپت اولیه کاربر فراخوانی می‌کنیم، سپس پاسخ را پردازش می‌کنیم تا ببینیم آیا ابزارهایی باید فراخوانی شوند یا نه. اگر چنین بود، آن ابزارها را فراخوانی کرده و مکالمه را با LLM ادامه می‌دهیم تا دیگر فراخوانی ابزار لازم نباشد و پاسخ نهایی داشته باشیم.

چندین بار به LLM فراخوانی خواهیم داشت، پس یک تابع تعریف می‌کنیم که فراخوانی LLM را مدیریت کند. این تابع را به فایل `main.rs` خود اضافه کنید:

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
  
این تابع کلاینت LLM، لیست پیام‌ها (شامل پرامپت کاربر)، ابزارهای سرور MCP را می‌گیرد و درخواست را به LLM می‌فرستد و پاسخ را بازمی‌گرداند.
پاسخ از LLM شامل یک آرایه از `choices` خواهد بود. ما باید نتیجه را پردازش کنیم تا ببینیم آیا هیچ `tool_calls` وجود دارد یا خیر. این به ما اطلاع می‌دهد که LLM درخواست می‌کند یک ابزار خاص با آرگومان‌ها فراخوانی شود. کد زیر را به انتهای فایل `main.rs` خود اضافه کنید تا یک تابع برای رسیدگی به پاسخ LLM تعریف شود:

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

    // در صورت وجود، محتوا را چاپ کنید
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
  
اگر `tool_calls` وجود داشته باشد، اطلاعات ابزار استخراج می‌شود، درخواست ابزار به سرور MCP فرستاده می‌شود، و نتایج به پیام‌های مکالمه اضافه می‌شود. سپس مکالمه با LLM ادامه می‌یابد و پیام‌ها با پاسخ دستیار و نتایج فراخوانی ابزار به‌روزرسانی می‌شوند.

برای استخراج اطلاعات فراخوانی ابزار که LLM برای تماس‌های MCP بازمی‌گرداند، یک تابع کمکی دیگر اضافه خواهیم کرد تا همه چیز مورد نیاز برای انجام تماس استخراج شود. کد زیر را به انتهای فایل `main.rs` خود اضافه کنید:

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
  
اکنون که همه قطعات آماده‌اند، می‌توانیم درخواست اولیه کاربر را مدیریت کرده و LLM را فراخوانی کنیم. تابع `main` خود را با کد زیر به‌روزرسانی کنید:

```rust
// مکالمه LLM با تماس‌های ابزار
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
  
این کد با درخواست اولیه از کاربر برای جمع دو عدد، LLM را پرس‌وجو می‌کند و پاسخ را برای مدیریت دینامیک فراخوانی ابزارها پردازش می‌کند.

عالی است، شما انجام دادید!

## تمرین

کد تمرین را گرفته و سرور را با چند ابزار بیشتر توسعه دهید. سپس یک کلاینت با LLM مشابه تمرین ایجاد کنید و آن را با درخواست‌های مختلف تست کنید تا مطمئن شوید تمام ابزارهای سرور شما به صورت دینامیک فراخوانی می‌شوند. این روش ساخت کلاینت باعث می‌شود تجربه کاربری نهایی عالی باشد چون کاربران می‌توانند از درخواست‌های متنی استفاده کنند، به جای دستورات دقیق کلاینت، و از تماس به سرور MCP کاملاً بی‌خبر باشند.

## راه‌حل

[راه‌حل](/03-GettingStarted/03-llm-client/solution/README.md)

## نکات کلیدی

- اضافه کردن LLM به کلاینت شما راه بهتری برای تعامل کاربران با سرورهای MCP فراهم می‌کند.
- شما باید پاسخ سرور MCP را به شکلی تبدیل کنید که LLM قادر به درک آن باشد.

## نمونه‌ها

- [ماشین حساب جاوا](../samples/java/calculator/README.md)  
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)  
- [ماشین حساب جاوا اسکریپت](../samples/javascript/README.md)  
- [ماشین حساب تایپ‌اسکریپت](../samples/typescript/README.md)  
- [ماشین حساب پایتون](../../../../03-GettingStarted/samples/python)  
- [ماشین حساب راست](../../../../03-GettingStarted/samples/rust)

## منابع بیشتر

## مرحله بعد

- مرحله بعد: [استفاده از سرور با Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**توضیح مهم**:  
این سند با استفاده از خدمات ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است دارای خطا یا نواقصی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->