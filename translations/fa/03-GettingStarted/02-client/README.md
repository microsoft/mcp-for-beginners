# ایجاد یک کلاینت

کلاینت‌ها برنامه‌ها یا اسکریپت‌های سفارشی هستند که به طور مستقیم با سرور MCP ارتباط برقرار می‌کنند تا منابع، ابزارها و پرامپت‌ها را درخواست کنند. برخلاف استفاده از ابزار بازرسی که یک رابط گرافیکی برای تعامل با سرور فراهم می‌کند، نوشتن کلاینت خودتان امکان تعامل برنامه‌ریزی شده و خودکار را می‌دهد. این به توسعه‌دهندگان اجازه می‌دهد تا قابلیت‌های MCP را در جریان‌های کاری خود ادغام کنند، کارها را خودکار کنند و راه‌حل‌های سفارشی متناسب با نیازهای خاص بسازند.

## مرور کلی

این درس مفهوم کلاینت‌ها در اکوسیستم پروتکل مدل کانتکست (MCP) را معرفی می‌کند. شما خواهید آموخت که چگونه کلاینت خود را بنویسید و آن را به یک سرور MCP متصل کنید.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- درک کنید کلاینت چه کاری می‌تواند انجام دهد.
- کلاینت خود را بنویسید.
- کلاینت را به سرور MCP متصل کرده و آن را تست کنید تا از عملکرد صحیح سرور اطمینان حاصل کنید.

## چه چیزهایی در نوشتن کلاینت لازم است؟

برای نوشتن یک کلاینت، باید موارد زیر را انجام دهید:

- **وارد کردن کتابخانه‌های صحیح**. شما همان کتابخانه قبلی را استفاده خواهید کرد، فقط ساختارهای متفاوت.
- **ایجاد نمونه‌ای از کلاینت**. این شامل ایجاد یک نمونه کلاینت و اتصال آن به روش انتقال انتخاب شده است.
- **تصمیم‌گیری درباره منابعی که باید لیست شوند**. سرور MCP شما شامل منابع، ابزارها و پرامپت‌ها است، باید تصمیم بگیرید کدام یک را لیست کنید.
- **ادغام کلاینت با برنامه میزبان**. وقتی قابلیت‌های سرور را می‌دانید باید این را در برنامه میزبان خود ادغام کنید تا اگر کاربری پرامپت یا فرمانی تایپ کرد، ویژگی متناظر سرور فراخوانی شود.

حال که یک نمای کلی از کاری که انجام می‌دهیم داریم، بیایید به یک مثال نگاه کنیم.

### یک کلاینت نمونه

بیایید نگاهی به این کلاینت نمونه بیندازیم:

### تایپ‌اسکریپت

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

// فهرست درخواست‌ها
const prompts = await client.listPrompts();

// دریافت یک درخواست
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// فهرست منابع
const resources = await client.listResources();

// خواندن یک منبع
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// فراخوانی یک ابزار
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

در کد بالا ما:

- کتابخانه‌ها را وارد کردیم
- نمونه‌ای از یک کلاینت ساختیم و با استفاده از stdio برای انتقال به آن متصل شدیم.
- پرامپت‌ها، منابع و ابزارها را لیست کرده و همه را فراخوانی کردیم.

این هم شد، کلاینتی که می‌تواند با سرور MCP ارتباط برقرار کند.

بیایید در بخش تمرین بعدی هر قطعه کد را تجزیه و تحلیل کنیم و توضیح دهیم چه می‌گذرد.

## تمرین: نوشتن کلاینت

همانطور که گفته شد، بیایید کد را با دقت شرح دهیم، و اگر خواستید می‌توانید همراه کد پیش بروید.

### -1- وارد کردن کتابخانه‌ها

بیایید کتابخانه‌های مورد نیاز را وارد کنیم، به کلاینت و پروتکل انتقال انتخابی‌مان یعنی stdio نیاز خواهیم داشت. stdio پروتکلی برای مواردی است که قرار است روی ماشین محلی شما اجرا شود. SSE پروتکل انتقال دیگری است که در فصل‌های آینده نشان خواهیم داد اما گزینه دیگر شماست. فعلاً ادامه می‌دهیم با stdio.

#### تایپ‌اسکریپت

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### پایتون

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
```

#### جاوا

برای جاوا، شما یک کلاینت می‌سازید که به سرور MCP در تمرین قبلی متصل شود. با استفاده از ساختار پروژه جاوا اسپرینگ بوت که در [شروع به کار با MCP سرور](../../../../03-GettingStarted/01-first-server/solution/java) داشتیم، یک کلاس جدید جاوا به نام `SDKClient` در پوشه‌ی `src/main/java/com/microsoft/mcp/sample/client/` بسازید و ایمپورت‌های زیر را اضافه کنید:

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

#### راست

باید وابستگی‌های زیر را به فایل `Cargo.toml` خود اضافه کنید.

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

از آنجا می‌توانید کتابخانه‌های لازم را در کد کلاینت‌تان وارد کنید.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

برویم سراغ ایجاد نمونه.

### -2- ایجاد نمونه کلاینت و انتقال

باید یک نمونه از انتقال و یک نمونه از کلاینت ایجاد کنیم:

#### تایپ‌اسکریپت

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

- یک نمونه از انتقال stdio ساختیم. توجه کنید که فرمان (command) و آرگومان‌ها چطور برای پیدا کردن و راه‌اندازی سرور مشخص شده‌اند چون این کاری است که هنگام ایجاد کلاینت باید انجام دهیم.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- یک کلاینت با نام و نسخه مشخص ساختیم.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- کلاینت را به انتقال انتخاب شده متصل کردیم.

    ```typescript
    await client.connect(transport);
    ```

#### پایتون

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

- کتابخانه‌های مورد نیاز را وارد کردیم
- یک شیء پارامترهای سرور ساختیم چون با آن می‌خواهیم سرور را اجرا کنیم تا بتوانیم با کلاینت وصل شویم.
- یک متد `run` تعریف کردیم که `stdio_client` را فراخوانی می‌کند که یک جلسه کلاینت را شروع می‌کند.
- یک نقطه ورود ساختیم که متد `run` را به `asyncio.run` می‌دهد.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

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

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

در کد بالا ما:

- کتابخانه‌های نیازمند را وارد کردیم.
- یک stdio transport ساختیم و یک کلاینت به نام `mcpClient` ساختیم. این برای لیست کردن و فراخوانی ویژگی‌های سرور MCP استفاده می‌شود.

توجه کنید در "Arguments" می‌توانید به فایل *.csproj* یا به فایل اجرایی اشاره کنید.

#### جاوا

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
        
        // منطق مشتری شما اینجا قرار می‌گیرد
    }
}
```

در کد بالا ما:

- یک متد اصلی (main) ساختیم که یک انتقال SSE را تنظیم می‌کند که به `http://localhost:8080` اشاره دارد جایی که سرور MCP ما اجرا خواهد شد.
- یک کلاس کلاینت ساختیم که انتقال را به عنوان پارامتر سازنده می‌گیرد.
- در متد `run`، یک کلاینت MCP همگام سازی شده با استفاده از انتقال ساخته و اتصال را مقداردهی اولیه می‌کند.
- از انتقال SSE (رویدادهای ارسال شده از سرور) استفاده کردیم که برای ارتباط مبتنی بر HTTP با سرورهای جاوا اسپرینگ بوت MCP مناسب است.

#### راست

توجه کنید این کلاینت Rust فرض می‌کند سرور یک پروژه خواهر به نام "calculator-server" در همان دایرکتوری است. کد زیر سرور را شروع می‌کند و به آن متصل می‌شود.

```rust
async fn main() -> Result<(), RmcpError> {
    // فرض کنید سرور یک پروژه خواهر به نام "calculator-server" در همان دایرکتوری است
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

    // انجام شود: مقداردهی اولیه

    // انجام شود: فهرست ابزارها

    // انجام شود: فراخوانی تابع اضافه کردن ابزار با آرگومان‌ها = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- لیست کردن امکانات سرور

حالا ما کلاینتی داریم که وقتی برنامه اجرا شود می‌تواند به سرور متصل شود. با این حال، هنوز امکانات سرور را لیست نمی‌کند، بیایید این کار را انجام دهیم:

#### تایپ‌اسکریپت

```typescript
// فهرست راهنمایی‌ها
const prompts = await client.listPrompts();

// فهرست منابع
const resources = await client.listResources();

// فهرست ابزارها
const tools = await client.listTools();
```

#### پایتون

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
```

اینجا منابع قابل دسترس `list_resources()` و ابزارها `list_tools` را لیست کرده و چاپ می‌کنیم.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

نمونه‌ای از این است که چگونه می‌توان ابزارهای سرور را لیست کرد. برای هر ابزار، نام آن را چاپ می‌کنیم.

#### جاوا

```java
// فهرست و نمایش ابزارها
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// شما همچنین می‌توانید برای بررسی اتصال سرور را پینگ کنید
client.ping();
```

در کد بالا ما:

- با `listTools()` همه ابزارهای موجود از سرور MCP را دریافت کردیم.
- از `ping()` برای تایید اتصال به سرور استفاده کردیم.
- `ListToolsResult` شامل اطلاعات همه ابزارها از جمله نام‌ها، توضیحات و شمای ورودی است.

عالی، حالا تمام قابلیت‌ها را در اختیار داریم. حال سوال این است که چه زمانی از آنها استفاده کنیم؟ خوب، این کلاینت ساده است، یعنی ما باید به طور صریح وقتی می‌خواهیم آن‌ها را فراخوانی کنیم. در فصل بعد یک کلاینت پیشرفته‌تر خواهیم ساخت که به مدل زبانی بزرگ خودش (LLM) دسترسی دارد. فعلاً بیایید ببینیم چگونه می‌توان قابلیت‌های سرور را فراخوانی کرد:

#### راست

در تابع اصلی، پس از مقداردهی اولیه کلاینت، می‌توانیم سرور را مقداردهی کرده و برخی امکانات آن را لیست کنیم.

```rust
// مقداردهی اولیه
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// فهرست ابزارها
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- فراخوانی امکانات

برای فراخوانی امکانات باید اطمینان حاصل کنیم آرگومان‌های صحیح را مشخص کرده‌ایم و در بعضی موارد نام چیزی که می‌خواهیم فراخوانی کنیم را هم ارائه دهیم.

#### تایپ‌اسکریپت

```typescript

// خواندن یک منبع
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// فراخوانی یک ابزار
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// فراخوانی پرامپت
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

در کد بالا ما:

- یک منبع را خواندیم، منبع را با `readResource()` و مشخص کردن `uri` فراخوانی کردیم. این احتمالاً در سرور به این صورت است:

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

    مقدار `uri` ما `file://example.txt` با `file://{name}` روی سرور تطابق دارد. `example.txt` به `name` مکَپ خواهد شد.

- یک ابزار را فراخوانی کردیم، با مشخص کردن `name` و `arguments` ابزار را فراخوانی می‌کنیم:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- دریافت پرامپت، برای دریافت پرامپت، `getPrompt()` را با `name` و `arguments` فراخوانی می‌کنیم. کد سرور به این شکل است:

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

    بنابراین کد کلاینت شما باید مشابه چیزی باشد که در سرور تعریف شده است:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### پایتون

```python
# خواندن یک منبع
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# فراخوانی یک ابزار
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

در کد بالا ما:

- منبعی به نام `greeting` را با `read_resource` فراخوانی کردیم.
- ابزاری به نام `add` را با `call_tool` فراخوانی کردیم.

#### .NET

1. کمی کد اضافه کنیم برای فراخوانی ابزار:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. برای چاپ نتیجه، کد زیر را داریم:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### جاوا

```java
// فراخوانی ابزارهای مختلف ماشین حساب
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

- چند ابزار محاسبه‌گر را با متد `callTool()` با اشیاء `CallToolRequest` فراخوانی کردیم.
- هر فراخوانی ابزار نام ابزار و یک `Map` شامل آرگومان‌های مورد نیاز آن ابزار را مشخص می‌کند.
- ابزارهای سرور نام پارامترهای مشخصی (مثل "a"، "b" برای عملیات ریاضی) انتظار دارند.
- نتایج به صورت اشیاء `CallToolResult` شامل پاسخ سرور برگردانده می‌شود.

#### راست

```rust
// فراخوانی ابزار جمع با آرگومان‌ها = {"a": 3, "b": 2}
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

برای اجرای کلاینت فرمان زیر را در ترمینال تایپ کنید:

#### تایپ‌اسکریپت

ورودی زیر را به بخش "scripts" در فایل *package.json* خود اضافه کنید:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### پایتون

کلاینت را با فرمان زیر اجرا کنید:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### جاوا

ابتدا از اجرای سرور MCP روی آدرس `http://localhost:8080` اطمینان حاصل کنید. سپس کلاینت را اجرا کنید:

```bash
# پروژه خود را بسازید
./mvnw clean compile

# کلاینت را اجرا کنید
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

یا اینکه می‌توانید پروژه کلاینت کامل ارائه شده در پوشه راه‌حل `03-GettingStarted\02-client\solution\java` را اجرا کنید:

```bash
# به دایرکتوری راه حل بروید
cd 03-GettingStarted/02-client/solution/java

# فایل JAR را بسازید و اجرا کنید
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### راست

```bash
cargo fmt
cargo run
```

## تکلیف

در این تکلیف، آنچه درباره ایجاد کلاینت آموخته‌اید را به کار ببرید و کلاینت خودتان را بسازید.

این یک سرور است که می‌توانید از آن استفاده کنید و باید از طریق کد کلاینت خود آن را صدا بزنید. ببینید آیا می‌توانید ویژگی‌های بیشتری به سرور اضافه کنید تا جالب‌تر شود.

### تایپ‌اسکریپت

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ایجاد یک سرور MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// افزودن یک ابزار جمع
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// افزودن یک منبع خوش‌آمدگویی پویا
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

// شروع دریافت پیام‌ها از stdin و ارسال پیام‌ها به stdout

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

### پایتون

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ایجاد یک سرور MCP
mcp = FastMCP("Demo")


# افزودن یک ابزار جمع
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# افزودن یک منبع خوش‌آمدگویی پویا
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

این پروژه را ببینید تا نحوه [افزودن پرامپت‌ها و منابع](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) را یاد بگیرید.

همچنین این لینک را برای نحوه فراخوانی [پرامپت‌ها و منابع](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) بررسی کنید.

### راست

در [بخش قبلی](../../../../03-GettingStarted/01-first-server) یاد گرفتید چگونه یک سرور ساده MCP با Rust بسازید. می‌توانید ادامه دهید یا این لینک را برای نمونه‌های بیشتری از سرورهای MCP مبتنی بر Rust ببینید: [نمونه‌های سرور MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## راه‌حل

پوشه **راه‌حل** شامل پیاده‌سازی‌های کامل و آماده اجرا برای کلاینت‌ها است که تمام مفاهیم این آموزش را نشان می‌دهد. هر راه‌حل شامل کد کلاینت و سرور در پروژه‌های جدا و مستقل است.

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

### 🚀 هر راه‌حل شامل چه چیزهایی است

هر راه‌حل مخصوص زبان شامل:

- **پیاده‌سازی کامل کلاینت** با تمام ویژگی‌های آموزش داده شده
- **ساختار پروژه عملیاتی** با وابستگی‌ها و تنظیمات درست
- **اسکریپت‌های ساخت و اجرا** برای راه‌اندازی و اجرای آسان
- **README جامع** با دستورالعمل‌های مخصوص هر زبان
- نمونه‌هایی از **مدیریت خطا** و پردازش نتایج

### 📖 استفاده از راه‌حل‌ها

1. **به پوشه زبان مورد نظر خود بروید**:

   ```bash
   cd solution/typescript/    # برای تایپ‌اسکریپت
   cd solution/java/          # برای جاوا
   cd solution/python/        # برای پایتون
   cd solution/dotnet/        # برای دات‌‌نت
   ```

2. **دستورالعمل‌های README را در هر پوشه دنبال کنید برای:**
   - نصب وابستگی‌ها
   - ساخت پروژه
   - اجرای کلاینت

3. **نمونه خروجی که باید ببینید:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

برای مستندات کامل و دستورالعمل گام به گام، به: **[📖 مستندات راه‌حل](./solution/README.md)** مراجعه کنید.

## 🎯 مثال‌های کامل

پیاده‌سازی‌های کامل کلاینت برای همه زبان‌های برنامه‌نویسی آموزش داده شده را ارائه کرده‌ایم. این مثال‌ها عملکرد کامل شرح داده شده را نشان می‌دهند و می‌توانند به عنوان پیاده‌سازی‌های مرجع یا نقطه شروع پروژه‌های خودتان استفاده شوند.

### مثال‌های کامل موجود

| زبان | فایل | توضیحات |
|----------|------|-------------|
| **جاوا** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | کلاینت کامل جاوا با انتقال SSE و مدیریت خطای جامع |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | کلاینت کامل C# با انتقال stdio و راه‌اندازی خودکار سرور |
| **تایپ‌اسکریپت** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | کلاینت کامل تایپ‌اسکریپت با پشتیبانی کامل از پروتکل MCP |
| **پایتون** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | کلاینت کامل پایتون با الگوهای async/await |
| **راست** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | کلاینت کامل راست با استفاده از Tokio برای عملیات ناهمزمان |

هر مثال کامل شامل:

- ✅ **ایجاد اتصال و مدیریت خطا**
- ✅ **کشف سرور** (ابزارها، منابع، پرامپت‌ها در صورت وجود)
- ✅ **عملیات ماشین حساب** (جمع، تفریق، ضرب، تقسیم، راهنما)
- ✅ **پردازش نتایج و خروجی قالب‌بندی شده**
- ✅ **مدیریت خطای جامع**

- ✅ **کد تمیز و مستندسازی شده** همراه با توضیحات گام به گام

### شروع با مثال‌های کامل

1. **زبان مورد نظر خود را** از جدول بالا انتخاب کنید
2. **فایل مثال کامل را مرور کنید** تا پیاده‌سازی کامل را درک کنید
3. **مثال را اجرا کنید** با دنبال کردن دستورالعمل‌ها در [`complete_examples.md`](./complete_examples.md)
4. **مثال را متناسب با نیاز خود تغییر داده و توسعه دهید**

برای مستندات دقیق درباره اجرای این مثال‌ها و سفارشی‌سازی آن‌ها، ببینید: **[📖 مستندات مثال‌های کامل](./complete_examples.md)**

### 💡 راه‌حل در مقابل مثال‌های کامل

| **پوشه راه‌حل** | **مثال‌های کامل** |
|--------------------|--------------------- |
| ساختار کامل پروژه همراه با فایل‌های ساخت | پیاده‌سازی‌های تک‌فایلی |
| آماده اجرا با وابستگی‌ها | مثال‌های کد متمرکز |
| تنظیمات مشابه تولید | مرجع آموزشی |
| ابزارهای مخصوص زبان | مقایسه بین زبان‌ها |

هر دو رویکرد ارزشمند هستند - از **پوشه راه‌حل** برای پروژه‌های کامل و از **مثال‌های کامل** برای یادگیری و مرجع استفاده کنید.

## نکات کلیدی

نکات کلیدی این فصل در مورد مشتری‌ها عبارتند از:

- می‌توانند هم برای کشف و هم برای فراخوانی ویژگی‌ها روی سرور استفاده شوند.
- می‌توانند سروری را در هنگام شروع خود راه‌اندازی کنند (مانند در این فصل) اما مشتریان هم می‌توانند به سرورهای در حال اجرا متصل شوند.
- راهی عالی برای آزمایش قابلیت‌های سرور در کنار گزینه‌هایی مانند Inspector است که در فصل قبلی توضیح داده شد.

## منابع اضافی

- [ساخت مشتری‌ها در MCP](https://modelcontextprotocol.io/quickstart/client)

## نمونه‌ها

- [ماشین‌حساب جاوا](../samples/java/calculator/README.md)
- [ماشین‌حساب .NET](../../../../03-GettingStarted/samples/csharp)
- [ماشین‌حساب جاوااسکریپت](../samples/javascript/README.md)
- [ماشین‌حساب تایپ‌اسکریپت](../samples/typescript/README.md)
- [ماشین‌حساب پایتون](../../../../03-GettingStarted/samples/python)
- [ماشین‌حساب راست](../../../../03-GettingStarted/samples/rust)

## قدم بعدی

- بعدی: [ساخت یک مشتری با LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->