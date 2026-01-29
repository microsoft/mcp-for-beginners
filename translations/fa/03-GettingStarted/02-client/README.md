# ایجاد یک کلاینت

کلاینت‌ها برنامه‌ها یا اسکریپت‌های سفارشی هستند که به طور مستقیم با سرور MCP ارتباط برقرار می‌کنند تا منابع، ابزارها و درخواست‌ها را دریافت کنند. برخلاف استفاده از ابزار بازرس که یک رابط گرافیکی برای تعامل با سرور فراهم می‌کند، نوشتن کلاینت خودتان امکان تعامل برنامه‌ریزی‌شده و خودکار را فراهم می‌کند. این قابلیت به توسعه‌دهندگان اجازه می‌دهد تا توانایی‌های MCP را در جریان کاری خود ادغام کنند، وظایف را خودکار کنند و راه‌حل‌های سفارشی متناسب با نیازهای خاص ایجاد کنند.

## مرور کلی

این درس مفهوم کلاینت‌ها را در اکوسیستم Model Context Protocol (MCP) معرفی می‌کند. شما یاد می‌گیرید که چگونه کلاینت خود را بنویسید و آن را به یک سرور MCP متصل کنید.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- درک کنید که یک کلاینت چه کاری می‌تواند انجام دهد.
- کلاینت خود را بنویسید.
- کلاینت را به سرور MCP متصل کرده و آن را تست کنید تا مطمئن شوید که سرور به درستی کار می‌کند.

## چه چیزی برای نوشتن یک کلاینت لازم است؟

برای نوشتن یک کلاینت، باید مراحل زیر را انجام دهید:

- **کتابخانه‌های مناسب را وارد کنید.** شما از همان کتابخانه قبلی استفاده خواهید کرد، فقط ساختارهای متفاوتی را به کار می‌گیرید.
- **یک کلاینت ایجاد کنید.** این شامل ایجاد یک نمونه کلاینت و اتصال آن به روش انتقال انتخابی است.
- **تصمیم بگیرید که کدام منابع را لیست کنید.** سرور MCP شما دارای منابع، ابزارها و درخواست‌ها است، شما باید تصمیم بگیرید کدام یک را لیست کنید.
- **کلاینت را در یک برنامه میزبان ادغام کنید.** پس از آگاهی از قابلیت‌های سرور، باید آن را در برنامه میزبان خود ادغام کنید تا اگر کاربر یک درخواست یا دستور دیگر وارد کرد، ویژگی مربوطه سرور فراخوانی شود.

حالا که به طور کلی متوجه شدیم چه کاری قرار است انجام دهیم، بیایید به یک مثال نگاه کنیم.

### یک مثال از کلاینت

بیایید به این مثال از یک کلاینت نگاه کنیم:

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

در کد بالا ما:

- کتابخانه‌ها را وارد کردیم.
- یک نمونه از کلاینت ایجاد کردیم و آن را با استفاده از stdio برای انتقال متصل کردیم.
- درخواست‌ها، منابع و ابزارها را لیست کرده و همه آن‌ها را فراخوانی کردیم.

این هم از یک کلاینت که می‌تواند با سرور MCP صحبت کند.

بیایید در بخش تمرین بعدی، هر قطعه کد را به دقت بررسی کنیم و توضیح دهیم که چه اتفاقی می‌افتد.

## تمرین: نوشتن یک کلاینت

همان‌طور که گفته شد، بیایید وقت بگذاریم و کد را توضیح دهیم، و اگر می‌خواهید، می‌توانید همزمان کدنویسی کنید.

### -1- وارد کردن کتابخانه‌ها

بیایید کتابخانه‌هایی که نیاز داریم را وارد کنیم. ما به ارجاعاتی به کلاینت و پروتکل انتقال انتخابی خود، stdio، نیاز خواهیم داشت. stdio یک پروتکل برای مواردی است که قرار است روی دستگاه محلی شما اجرا شوند. SSE یک پروتکل انتقال دیگر است که در فصل‌های آینده نشان خواهیم داد، اما فعلاً با stdio ادامه می‌دهیم.

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
```

#### Java

برای جاوا، شما یک کلاینت ایجاد خواهید کرد که به سرور MCP از تمرین قبلی متصل می‌شود. با استفاده از همان ساختار پروژه Java Spring Boot از [شروع کار با سرور MCP](../../../../03-GettingStarted/01-first-server/solution/java)، یک کلاس جاوای جدید به نام `SDKClient` در پوشه `src/main/java/com/microsoft/mcp/sample/client/` ایجاد کنید و واردات زیر را اضافه کنید:

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

شما باید وابستگی‌های زیر را به فایل `Cargo.toml` خود اضافه کنید.

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

سپس می‌توانید کتابخانه‌های لازم را در کد کلاینت خود وارد کنید.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

بیایید به مرحله ایجاد کلاینت برویم.

### -2- ایجاد کلاینت و انتقال

ما باید یک نمونه از انتقال و یک نمونه از کلاینت خود ایجاد کنیم:

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

در کد بالا ما:

- یک نمونه انتقال stdio ایجاد کردیم. توجه کنید که چگونه فرمان و آرگومان‌ها را برای پیدا کردن و راه‌اندازی سرور مشخص می‌کند، زیرا این چیزی است که هنگام ایجاد کلاینت به آن نیاز خواهیم داشت.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- یک کلاینت با نام و نسخه مشخص ایجاد کردیم.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- کلاینت را به انتقال انتخابی متصل کردیم.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

در کد بالا ما:

- کتابخانه‌های مورد نیاز را وارد کردیم.
- یک شیء پارامترهای سرور ایجاد کردیم زیرا از آن برای اجرای سرور استفاده خواهیم کرد تا بتوانیم با کلاینت خود به آن متصل شویم.
- یک متد `run` تعریف کردیم که به نوبه خود `stdio_client` را فراخوانی می‌کند و یک جلسه کلاینت را شروع می‌کند.
- یک نقطه ورود ایجاد کردیم که در آن متد `run` را به `asyncio.run` ارائه می‌دهیم.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

در کد بالا ما:

- کتابخانه‌های مورد نیاز را وارد کردیم.
- یک انتقال stdio و یک کلاینت `mcpClient` ایجاد کردیم. از دومی برای لیست کردن و فراخوانی ویژگی‌های سرور MCP استفاده خواهیم کرد.

توجه داشته باشید که در "Arguments"، می‌توانید به *.csproj* یا فایل اجرایی اشاره کنید.

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // Your client logic goes here
    }
}
```

در کد بالا ما:

- یک متد اصلی ایجاد کردیم که یک انتقال SSE را تنظیم می‌کند که به `http://localhost:8080` اشاره دارد، جایی که سرور MCP ما اجرا خواهد شد.
- یک کلاس کلاینت ایجاد کردیم که انتقال را به عنوان یک پارامتر سازنده می‌گیرد.
- در متد `run`، یک کلاینت MCP همگام با استفاده از انتقال ایجاد کردیم و اتصال را مقداردهی اولیه کردیم.
- از انتقال SSE (رویدادهای ارسال‌شده از سرور) استفاده کردیم که برای ارتباط مبتنی بر HTTP با سرورهای MCP جاوا Spring Boot مناسب است.

#### Rust

این کلاینت Rust فرض می‌کند که سرور یک پروژه هم‌سطح به نام "calculator-server" در همان دایرکتوری است. کد زیر سرور را راه‌اندازی کرده و به آن متصل می‌شود.

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- لیست کردن ویژگی‌های سرور

حالا، ما یک کلاینت داریم که می‌تواند متصل شود، اگر برنامه اجرا شود. با این حال، هنوز ویژگی‌های آن را لیست نمی‌کند، پس بیایید این کار را انجام دهیم:

#### TypeScript

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

#### Python

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

در اینجا ما منابع موجود را با `list_resources()` و ابزارها را با `list_tools` لیست کرده و چاپ می‌کنیم.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

در بالا مثالی از نحوه لیست کردن ابزارهای سرور آورده شده است. برای هر ابزار، سپس نام آن را چاپ می‌کنیم.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

در کد بالا ما:

- با استفاده از `listTools()` تمام ابزارهای موجود در سرور MCP را دریافت کردیم.
- از `ping()` برای تأیید اینکه اتصال به سرور کار می‌کند استفاده کردیم.
- `ListToolsResult` شامل اطلاعاتی درباره تمام ابزارها از جمله نام‌ها، توضیحات و طرح‌های ورودی است.

عالی، حالا تمام ویژگی‌ها را ثبت کردیم. حالا سوال این است که چه زمانی از آن‌ها استفاده کنیم؟ خوب، این کلاینت بسیار ساده است، به این معنا که ما باید به طور صریح ویژگی‌ها را زمانی که به آن‌ها نیاز داریم فراخوانی کنیم. در فصل بعد، یک کلاینت پیشرفته‌تر ایجاد خواهیم کرد که به مدل زبان بزرگ خود (LLM) دسترسی دارد. فعلاً، بیایید ببینیم چگونه می‌توانیم ویژگی‌ها را روی سرور فراخوانی کنیم:

#### Rust

در تابع اصلی، پس از مقداردهی اولیه کلاینت، می‌توانیم سرور را مقداردهی اولیه کرده و برخی از ویژگی‌های آن را لیست کنیم.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- فراخوانی ویژگی‌ها

برای فراخوانی ویژگی‌ها، باید مطمئن شویم که آرگومان‌های صحیح و در برخی موارد نام چیزی که می‌خواهیم فراخوانی کنیم را مشخص کرده‌ایم.

#### TypeScript

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

در کد بالا ما:

- یک منبع را خواندیم، منبع را با فراخوانی `readResource()` و مشخص کردن `uri` فراخوانی می‌کنیم. این چیزی است که احتمالاً در سمت سرور به این شکل خواهد بود:

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    مقدار `uri` ما `file://example.txt` با `file://{name}` در سرور مطابقت دارد. `example.txt` به `name` نگاشت می‌شود.

- یک ابزار را فراخوانی کردیم، آن را با مشخص کردن `name` و `arguments` فراخوانی می‌کنیم، به این شکل:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- یک درخواست را دریافت کردیم، برای دریافت یک درخواست، `getPrompt()` را با `name` و `arguments` فراخوانی می‌کنیم. کد سرور به این شکل است:

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    و کد کلاینت شما برای مطابقت با چیزی که در سرور تعریف شده است به این شکل خواهد بود:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

در کد بالا ما:

- یک منبع به نام `greeting` را با استفاده از `read_resource` فراخوانی کردیم.
- یک ابزار به نام `add` را با استفاده از `call_tool` فراخوانی کردیم.

#### .NET

1. بیایید کدی برای فراخوانی یک ابزار اضافه کنیم:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. برای چاپ نتیجه، در اینجا کدی برای مدیریت آن آورده شده است:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call various calculator tools
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

در کد بالا ما:

- چندین ابزار ماشین‌حساب را با استفاده از متد `callTool()` و اشیاء `CallToolRequest` فراخوانی کردیم.
- هر فراخوانی ابزار نام ابزار و یک `Map` از آرگومان‌های مورد نیاز آن ابزار را مشخص می‌کند.
- ابزارهای سرور انتظار دارند نام‌های پارامتر خاصی (مانند "a"، "b" برای عملیات ریاضی) مشخص شود.
- نتایج به صورت اشیاء `CallToolResult` بازگردانده می‌شوند که پاسخ سرور را شامل می‌شوند.

#### Rust

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- اجرای کلاینت

برای اجرای کلاینت، دستور زیر را در ترمینال وارد کنید:

#### TypeScript

ورودی زیر را به بخش "scripts" در *package.json* اضافه کنید:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

کلاینت را با دستور زیر فراخوانی کنید:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

ابتدا مطمئن شوید که سرور MCP شما روی `http://localhost:8080` اجرا می‌شود. سپس کلاینت را اجرا کنید:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

یا می‌توانید پروژه کامل کلاینت ارائه‌شده در پوشه راه‌حل `03-GettingStarted\02-client\solution\java` را اجرا کنید:

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## تکلیف

در این تکلیف، شما از آنچه در ایجاد یک کلاینت یاد گرفته‌اید استفاده خواهید کرد، اما کلاینت خود را ایجاد می‌کنید.

در اینجا یک سرور وجود دارد که می‌توانید از آن استفاده کنید و باید از طریق کد کلاینت خود آن را فراخوانی کنید، ببینید آیا می‌توانید ویژگی‌های بیشتری به سرور اضافه کنید تا جالب‌تر شود.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// Start receiving messages on stdin and sending messages on stdout

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

این پروژه را ببینید تا ببینید چگونه می‌توانید [درخواست‌ها و منابع اضافه کنید](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

همچنین این لینک را برای نحوه فراخوانی [درخواست‌ها و منابع](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) بررسی کنید.

### Rust

در [بخش قبلی](../../../../03-GettingStarted/01-first-server)، یاد گرفتید که چگونه یک سرور MCP ساده با Rust ایجاد کنید. می‌توانید به ساخت آن ادامه دهید یا این لینک را برای مثال‌های بیشتر سرور MCP مبتنی بر Rust بررسی کنید: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## راه‌حل

پوشه **راه‌حل** شامل پیاده‌سازی‌های کامل و آماده اجرا از کلاینت است که تمام مفاهیم پوشش داده‌شده در این آموزش را نشان می‌دهد. هر راه‌حل شامل کد کلاینت و سرور است که در پروژه‌های جداگانه و مستقل سازمان‌دهی شده‌اند.

### 📁 ساختار راه‌حل

دایرکتوری راه‌حل بر اساس زبان برنامه‌نویسی سازمان‌دهی شده است:

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 هر راه‌حل شامل چه چیزی است؟

هر راه‌حل خاص زبان شامل موارد زیر است:

- **پیاده‌سازی کامل کلاینت** با تمام ویژگی‌های آموزش
- **ساختار پروژه کاری** با وابستگی‌ها و پیکربندی مناسب
- **اسکریپت‌های ساخت و اجرا** برای راه‌اندازی و اجرا آسان
- **README دقیق** با دستورالعمل‌های خاص زبان
- **مثال‌های مدیریت خطا** و پردازش نتایج

### 📖 استفاده از راه‌حل‌ها

1. **به پوشه زبان مورد نظر خود بروید**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **دستورالعمل‌های README** در هر پوشه را برای موارد زیر دنبال کنید:
   - نصب وابستگی‌ها
   - ساخت پروژه
   - اجرای کلاینت

3. **خروجی نمونه** که باید ببینید:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

برای مستندات کامل و دستورالعمل‌های گام‌به‌گام، به این لینک مراجعه کنید: **[📖 مستندات راه‌حل](./solution/README.md)**

## 🎯 مثال‌های کامل

ما پیاده‌سازی‌های کامل و کاری کلاینت را برای تمام زبان‌های برنامه‌نویسی پوشش داده‌شده در این آموزش ارائه کرده‌ایم. این مثال‌ها عملکرد کامل توضیح داده‌شده در بالا را نشان می‌دهند و می‌توانند به عنوان پیاده‌سازی‌های مرجع یا نقطه شروع برای پروژه‌های شما استفاده شوند.

### مثال‌های کامل موجود

| زبان | فایل | توضیحات |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | کلاینت کامل جاوا با استفاده از انتقال SSE با مدیریت خطای جامع |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | کلاینت کامل C# با استفاده از انتقال stdio و راه‌اندازی خودکار سرور |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | کلاینت کامل TypeScript با پشتیبانی کامل از پروتکل MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | کلاینت کامل پایتون با استفاده از الگوهای async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | کلاینت کامل Rust با استفاده از Tokio برای عملیات غیرهمزمان |
هر مثال کامل شامل موارد زیر است:

- ✅ **برقراری اتصال** و مدیریت خطا
- ✅ **کشف سرور** (ابزارها، منابع، درخواست‌ها در صورت نیاز)
- ✅ **عملیات ماشین حساب** (جمع، تفریق، ضرب، تقسیم، کمک)
- ✅ **پردازش نتایج** و خروجی قالب‌بندی شده
- ✅ **مدیریت جامع خطاها**
- ✅ **کد تمیز و مستند** با توضیحات مرحله به مرحله

### شروع به کار با مثال‌های کامل

1. **زبان مورد نظر خود را انتخاب کنید** از جدول بالا
2. **فایل مثال کامل را مرور کنید** تا پیاده‌سازی کامل را درک کنید
3. **مثال را اجرا کنید** با دنبال کردن دستورالعمل‌های موجود در [`complete_examples.md`](./complete_examples.md)
4. **مثال را تغییر دهید و گسترش دهید** برای استفاده خاص خود

برای مستندات دقیق درباره اجرای و سفارشی‌سازی این مثال‌ها، به اینجا مراجعه کنید: **[📖 مستندات مثال‌های کامل](./complete_examples.md)**

### 💡 راه‌حل در مقابل مثال‌های کامل

| **پوشه راه‌حل** | **مثال‌های کامل** |
|--------------------|--------------------- |
| ساختار کامل پروژه با فایل‌های ساخت | پیاده‌سازی‌های تک‌فایلی |
| آماده اجرا با وابستگی‌ها | مثال‌های کد متمرکز |
| تنظیمات مشابه تولید | مرجع آموزشی |
| ابزارهای خاص زبان | مقایسه بین زبان‌ها |

هر دو روش ارزشمند هستند - از **پوشه راه‌حل** برای پروژه‌های کامل و از **مثال‌های کامل** برای یادگیری و مرجع استفاده کنید.

## نکات کلیدی

نکات کلیدی این فصل درباره کلاینت‌ها به شرح زیر است:

- می‌توانند برای کشف و فراخوانی ویژگی‌های سرور استفاده شوند.
- می‌توانند هنگام شروع خود، یک سرور را نیز راه‌اندازی کنند (مانند این فصل)، اما کلاینت‌ها می‌توانند به سرورهای در حال اجرا نیز متصل شوند.
- راهی عالی برای آزمایش قابلیت‌های سرور در کنار گزینه‌هایی مانند Inspector است که در فصل قبل توضیح داده شد.

## منابع اضافی

- [ساخت کلاینت‌ها در MCP](https://modelcontextprotocol.io/quickstart/client)

## نمونه‌ها

- [ماشین حساب جاوا](../samples/java/calculator/README.md)
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)
- [ماشین حساب جاوااسکریپت](../samples/javascript/README.md)
- [ماشین حساب تایپ‌اسکریپت](../samples/typescript/README.md)
- [ماشین حساب پایتون](../../../../03-GettingStarted/samples/python)
- [ماشین حساب راست](../../../../03-GettingStarted/samples/rust)

## مرحله بعدی

- بعدی: [ایجاد کلاینت با LLM](../03-llm-client/README.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشد. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.