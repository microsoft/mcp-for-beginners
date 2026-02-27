# ایجاد یک کلاینت

کلاینت‌ها برنامه‌ها یا اسکریپت‌های سفارشی هستند که مستقیماً با سرور MCP ارتباط برقرار کرده و درخواست منابع، ابزارها و پرامپت‌ها را می‌دهند. بر خلاف استفاده از ابزار inspector که یک رابط گرافیکی برای تعامل با سرور فراهم می‌کند، نوشتن کلاینت خودتان امکان تعامل برنامه‌نویسی و خودکار را میسر می‌سازد. این به توسعه‌دهندگان اجازه می‌دهد قابلیت‌های MCP را در جریان‌های کاری خود یکپارچه کنند، وظایف را خودکار سازند و راه‌حل‌های سفارشی متناسب با نیازهای خاص بسازند.

## مرور کلی

این درس مفهوم کلاینت‌ها در اکوسیستم پروتکل مدل کانتکست (MCP) را معرفی می‌کند. شما خواهید آموخت چگونه کلاینت خود را بنویسید و آن را به یک سرور MCP متصل کنید.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- درک کنید که یک کلاینت چه کارهایی می‌تواند انجام دهد.
- کلاینت خود را بنویسید.
- کلاینت را به سرور MCP متصل کرده و تست کنید تا اطمینان حاصل شود که سرور به درستی کار می‌کند.

## چه مواردی برای نوشتن یک کلاینت لازم است؟

برای نوشتن یک کلاینت، باید موارد زیر را انجام دهید:

- **وارد کردن کتابخانه‌های صحیح**. شما از همان کتابخانه قبلی استفاده خواهید کرد، فقط ساختارهای متفاوت.
- **ایجاد یک نمونه کلاینت**. این شامل ساخت یک نمونه کلاینت و اتصال آن به روش انتقال انتخاب شده خواهد بود.
- **تصمیم‌گیری درباره منابعی که باید فهرست شوند**. سرور MCP شما دارای منابع، ابزارها و پرامپت‌هایی است، باید تصمیم بگیرید کدام را فهرست کنید.
- **یکپارچه‌سازی کلاینت با برنامه میزبان**. وقتی قابلیت‌های سرور را فهمیدید باید کلاینت خود را به برنامه میزبان‌تان متصل کنید تا اگر کاربری پرامپت یا فرمانی وارد کرد، ویژگی مربوط به سرور فراخوانی شود.

حالا که روی خط کلی آنچه باید انجام دهیم فهمیدیم، بیایید به مثالی نگاه کنیم.

### یک کلاینت نمونه

بیایید به این کلاینت نمونه نگاه کنیم:

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

// لیست پرامپت‌ها
const prompts = await client.listPrompts();

// گرفتن یک پرامپت
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// لیست منابع
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
- نمونه‌ای از کلاینت ساختیم و با استفاده از stdio برای انتقال به سرور متصل شدیم.
- پرامپت‌ها، منابع و ابزارها را فهرست کرده و همه را فراخوانی کردیم.

همین است، یک کلاینت که می‌تواند با سرور MCP صحبت کند.

بیایید در بخش تمرین بعدی وقت بگذاریم و هر قطعه کد را بررسی کرده و توضیح دهیم چه اتفاقی می‌افتد.

## تمرین: نوشتن یک کلاینت

همانطور که گفته شد، بیایید وقت بگذاریم تا کد را توضیح دهیم و هر طور که خواستید هم می‌توانید کدنویسی همراه ما انجام دهید.

### -1- وارد کردن کتابخانه‌ها

بیایید کتابخانه‌های مورد نیاز را وارد کنیم، ما به ارجاع‌هایی برای کلاینت و پروتکل انتقال انتخاب شده خود یعنی stdio نیاز داریم. stdio یک پروتکل برای چیزهایی است که قرار است روی ماشین محلی شما اجرا شوند. SSE یک پروتکل انتقال دیگر است که در فصل‌های بعدی نشان خواهیم داد ولی آن گزینه دیگر شماست. فعلاً ادامه می‌دهیم با stdio.

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

#### دات‌نت

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### جاوا

برای جاوا، یک کلاینت بسازید که به سرور MCP از تمرین قبلی متصل شود. با استفاده از ساختار پروژه Java Spring Boot مشابه [شروع کار با MCP Server](../../../../03-GettingStarted/01-first-server/solution/java)، یک کلاس جدید به نام `SDKClient` در پوشه `src/main/java/com/microsoft/mcp/sample/client/` ایجاد کنید و ایمپورت‌های زیر را اضافه نمایید:

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

باید وابستگی‌های زیر را به فایل `Cargo.toml` اضافه کنید.

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

از آنجا، می‌توانید کتابخانه‌های لازم را در کد کلاینت خود وارد کنید.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

حالا به مرحله نمونه‌سازی می‌رویم.

### -2- نمونه‌سازی کلاینت و انتقال

باید یک نمونه از انتقال و یک نمونه از کلاینت بسازیم:

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

- یک نمونه انتقال stdio ایجاد کردیم. توجه کنید که چگونه فرمان و آرگومان‌ها را مشخص می‌کند برای اینکه چگونه سرور را پیدا کرده و راه‌اندازی کند، چون این کاری است که باید هنگام ایجاد کلاینت انجام دهیم.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- با دادن نام و نسخه، یک کلاینت نمونه‌سازی کردیم.

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

- کتابخانه‌های مورد نیاز را وارد کردیم.
- یک شیء پارامترهای سرور نمونه‌سازی کردیم چون می‌خواهیم با آن سرور را اجرا کنیم تا با کلاینت به آن متصل شویم.
- متدی به نام `run` تعریف کردیم که به نوبه خود `stdio_client` را فراخوانی می‌کند که جلسه کلاینت را شروع می‌کند.
- یک نقطه ورودی ساختیم که متد `run` را به `asyncio.run` می‌دهد.

#### دات‌نت

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

- کتابخانه‌های لازم را وارد کردیم.
- یک انتقال stdio ایجاد کردیم و یک کلاینت به نام `mcpClient` ساختیم. این کلاینت برای فهرست کردن و فراخوانی قابلیت‌های سرور MCP استفاده خواهد شد.

توجه داشته باشید در قسمت "Arguments" می‌توانید به فایل *.csproj* یا به فایل اجرایی اشاره کنید.

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
        
        // منطق کلاینت شما اینجا قرار می‌گیرد
    }
}
```

در کد بالا ما:

- یک متد اصلی ساختیم که یک انتقال SSE به آدرس `http://localhost:8080` که سرور MCP ما روی آن اجرا می‌شود تنظیم می‌کند.
- یک کلاس کلاینت ساختیم که انتقال را به عنوان پارامتر سازنده می‌گیرد.
- در متد `run`، یک کلاینت MCP همزمان با استفاده از انتقال ایجاد کردیم و اتصال را مقداردهی اولیه کردیم.
- از انتقال SSE (رویدادهای ارسالی سرور) استفاده کردیم که برای ارتباط مبتنی بر HTTP با سرورهای Java Spring Boot MCP مناسب است.

#### راست

توجه داشته باشید این کلاینت راست فرض می‌کند سرور پروژه‌ای هم‌سطح به نام "calculator-server" در همان دایرکتوری است. کد زیر سرور را راه‌اندازی کرده و به آن متصل می‌شود.

```rust
async fn main() -> Result<(), RmcpError> {
    // فرض کنید سرور پروژه خواهر به نام "calculator-server" در همان دایرکتوری است
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

    // انجام شدنی: مقداردهی اولیه

    // انجام شدنی: فهرست ابزارها

    // انجام شدنی: فراخوانی ابزار افزودن با آرگومان‌ها = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- فهرست کردن قابلیت‌های سرور

حالا، ما کلاینتی داریم که اگر برنامه اجرا شود به سرور متصل می‌شود. اما در واقع قابلیت‌هایش را فهرست نمی‌کند، پس اکنون این کار را انجام می‌دهیم:

#### تایپ‌اسکریپت

```typescript
// فهرست درخواست‌ها
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

در اینجا منابع موجود را با `list_resources()` و ابزارها را با `list_tools` فهرست کرده و چاپ می‌کنیم.

#### دات‌نت

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

در بالا نمونه‌ای از نحوه فهرست کردن ابزارهای سرور دیده می‌شود. برای هر ابزار، نام آن را چاپ می‌کنیم.

#### جاوا

```java
// فهرست و نمایش ابزارها
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// همچنین می‌توانید به سرور پینگ بزنید تا اتصال را بررسی کنید
client.ping();
```

در کد بالا ما:

- با فراخوانی `listTools()` همه ابزارهای موجود در سرور MCP را گرفتیم.
- با `ping()` صحت اتصال به سرور را بررسی کردیم.
- `ListToolsResult` شامل اطلاعات همه ابزارها شامل نام، توضیحات و طرح‌بندی ورودی است.

عالی، حالا همه قابلیت‌ها را گرفتیم. سوال این است که چه زمانی از آنها استفاده کنیم؟ خوب، این کلاینت ساده است، یعنی برای استفاده باید به طور صریح ویژگی‌ها را فراخوانی کنیم. در فصل بعد، کلاینت پیشرفته‌تری می‌سازیم که به مدل زبان بزرگ (LLM) خودش دسترسی دارد. فعلاً بیایید ببینیم چگونه می‌توان قابلیت‌های سرور را فراخوانی کرد:

#### راست

در تابع main، پس از مقداردهی اولیه کلاینت، می‌توانیم سرور را راه‌اندازی کرده و برخی از قابلیت‌های آن را فهرست کنیم.

```rust
// مقداردهی اولیه
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// فهرست ابزارها
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- فراخوانی قابلیت‌ها

برای فراخوانی قابلیت‌ها باید مطمئن شویم آرگومان‌های درست را مشخص می‌کنیم و در برخی موارد نام چیزی که می‌خواهیم فراخوانی کنیم.

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

// فراخوانی درخواست
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

در کد بالا ما:

- یک منبع را خواندیم، منبع را با فراخوانی `readResource()` و تعیین `uri` صدا زدیم. این احتمالاً در سمت سرور به این شکل است:

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

- یک ابزار را فراخوانی کردیم، آن را با تعیین نام و آرگومان‌ها اینگونه صدا زدیم:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- پرامپت گرفتیم، برای گرفتن پرامپت، `getPrompt()` را با نام و آرگومان‌ها فراخوانی کردیم. کد سرور به این شکل است:

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

    و کد کلاینت شما در نتیجه به این شکل خواهد بود تا با کد سرور مطابقت داشته باشد:

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

- منبعی به نام `greeting` را با `read_resource` صدا زدیم.
- ابزاری به نام `add` را با `call_tool` فراخوانی کردیم.

#### دات‌نت

1. برای فراخوانی یک ابزار، کد زیر را اضافه کنید:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. برای چاپ نتیجه، کد زیر را اضافه کنید:

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

- چند ابزار ماشین حساب را با استفاده از متد `callTool()` و اشیاء `CallToolRequest` فراخوانی کردیم.
- هر فراخوانی ابزار، نام ابزار و یک `Map` از آرگومان‌های لازم را مشخص می‌کند.
- ابزارهای سرور انتظار دارند پارامترهای خاصی مانند "a"، "b" برای عملیات ریاضی داشته باشند.
- نتایج به صورت اشیاء `CallToolResult` شامل پاسخ از سرور بازگردانده می‌شوند.

#### راست

```rust
// فراخوانی ابزار جمع با آرگومان‌ها = {"a": 3، "b": 2}
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

برای اجرای کلاینت، فرمان زیر را در ترمینال تایپ کنید:

#### تایپ‌اسکریپت

آیتم زیر را به بخش "scripts" در *package.json* اضافه کنید:

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

#### دات‌نت

```sh
dotnet run
```

#### جاوا

اول، مطمئن شوید سرور MCP شما روی `http://localhost:8080` در حال اجرا است. سپس کلاینت را اجرا کنید:

```bash
# پروژه خود را بسازید
./mvnw clean compile

# کلاینت را اجرا کنید
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

همچنین، می‌توانید پروژه کامل کلاینت را که در پوشه راه‌حل `03-GettingStarted\02-client\solution\java` موجود است اجرا کنید:

```bash
# به دایرکتوری راه‌حل بروید
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

## تمرین

در این تمرین، آنچه را در ساخت یک کلاینت آموخته‌اید استفاده می‌کنید اما یک کلاینت خودتان بسازید.

در اینجا یک سروری هست که می‌توانید از آن استفاده کنید و باید از طریق کد کلاینت خود به آن فراخوانی دهید، ببینید آیا می‌توانید ویژگی‌های بیشتری به سرور اضافه کنید تا جالب‌تر شود.

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

// افزودن منبع خوش‌آمدگویی پویا
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

// شروع دریافت پیام‌ها از ورودی استاندارد و ارسال پیام‌ها به خروجی استاندارد

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

### دات‌نت

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

برای نحوه [افزودن پرامپت‌ها و منابع](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) این پروژه را ببینید.

همچنین این لینک را برای چگونگی [فراخوانی پرامپت‌ها و منابع](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) بررسی کنید.

### راست

در بخش [قبلی](../../../../03-GettingStarted/01-first-server) آموختید چگونه یک سرور ساده MCP با Rust بسازید. می‌توانید بر روی آن ادامه دهید یا این لینک را برای نمونه‌های سرور MCP بر پایه Rust ببینید: [نمونه‌های سرور MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## راه‌حل

پوشه **راه‌حل** شامل پیاده‌سازی‌های کامل و آماده اجرا از کلاینت‌ها است که تمام مفاهیم پوشش داده شده در این آموزش را نشان می‌دهد. هر راه‌حل شامل کد کلاینت و سرور است که در پروژه‌های جداگانه و کامل سازماندهی شده‌اند.

### 📁 ساختار راه‌حل

دایرکتوری راه‌حل بر اساس زبان برنامه‌نویسی سازماندهی شده است:

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

هر راه‌حل مخصوص زبان موارد زیر را ارائه می‌کند:

- **پیاده‌سازی کامل کلاینت** با تمام قابلیت‌های آموزش
- **ساختار پروژه کاری** با وابستگی‌ها و پیکربندی مناسب
- **اسکریپت‌های ساخت و اجرا** برای راه‌اندازی و اجرای آسان
- **README دقیق** با دستورالعمل‌های خاص زبان
- **مثال‌های مدیریت خطا** و پردازش نتایج

### 📖 استفاده از راه‌حل‌ها

1. **به پوشه زبان مورد علاقه خود بروید**:

   ```bash
   cd solution/typescript/    # برای تایپ‌اسکریپت
   cd solution/java/          # برای جاوا
   cd solution/python/        # برای پایتون
   cd solution/dotnet/        # برای دات‌نت
   ```

2. **دستورالعمل‌های README در هر پوشه را دنبال کنید** برای:
   - نصب وابستگی‌ها
   - ساخت پروژه
   - اجرای کلاینت

3. **خروجی نمونه** که باید مشاهده کنید:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

برای مستندات کامل و دستورالعمل گام به گام، اینجا را ببینید: **[📖 مستندات راه‌حل](./solution/README.md)**

## 🎯 مثال‌های کامل

ما پیاده‌سازی‌های کامل و کاری کلاینت‌ها را برای تمام زبان‌های برنامه‌نویسی پوشش داده شده در این آموزش فراهم کرده‌ایم. این مثال‌ها عملکرد کامل توضیح داده شده را نشان می‌دهند و می‌توانند به عنوان پیاده‌سازی مرجع یا نقطه شروع برای پروژه‌های خودتان استفاده شوند.

### مثال‌های کامل موجود

| زبان | فایل | توضیح |
|----------|------|-------------|
| **جاوا** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | کلاینت کامل جاوا با استفاده از انتقال SSE و مدیریت کامل خطا |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | کلاینت کامل C# با استفاده از انتقال stdio و راه‌اندازی خودکار سرور |
| **تایپ‌اسکریپت** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | کلاینت کامل تایپ‌اسکریپت با پشتیبانی کامل پروتکل MCP |
| **پایتون** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | کلاینت کامل پایتون با الگوهای async/await |
| **راست** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | کلاینت کامل راست با استفاده از Tokio برای عملیات ناهمزمان |

هر مثال کامل شامل:
- ✅ **برقراری اتصال** و مدیریت خطا
- ✅ **کشف سرور** (ابزارها، منابع، درخواست‌ها در صورت امکان)
- ✅ **عملیات ماشین حساب** (جمع، تفریق، ضرب، تقسیم، راهنما)
- ✅ **پردازش نتیجه** و خروجی قالب‌بندی شده
- ✅ **مدیریت جامع خطا**
- ✅ **کدنویسی پاک و مستند** با توضیحات مرحله به مرحله

### شروع با مثال‌های کامل

1. **زبان مورد علاقه خود را انتخاب کنید** از جدول بالا
2. **فایل مثال کامل را بررسی کنید** تا پیاده‌سازی کامل را درک کنید
3. **مثال را اجرا کنید** با دنبال کردن دستورالعمل‌ها در [`complete_examples.md`](./complete_examples.md)
4. **مثال را برای مورد استفاده خاص خود تغییر داده و گسترش دهید**

برای مستندات دقیق در مورد اجرای این مثال‌ها و سفارشی‌سازی آنها، به **[📖 مستندات مثال‌های کامل](./complete_examples.md)** مراجعه کنید

### 💡 راه حل در مقابل مثال‌های کامل

| **پوشه راه حل** | **مثال‌های کامل** |
|-----------------|-------------------|
| ساختار کامل پروژه با فایل‌های ساخت | پیاده‌سازی‌های تک‌فایل |
| آماده اجرا با وابستگی‌ها | مثال‌های کد متمرکز |
| تنظیمات مشابه تولید | مرجع آموزشی |
| ابزارهای خاص زبان | مقایسه بین زبان‌ها |

هر دو رویکرد ارزشمند هستند - از **پوشه راه حل** برای پروژه‌های کامل و از **مثال‌های کامل** برای یادگیری و مرجع استفاده کنید.

## نکات کلیدی

نکات کلیدی این فصل درباره کلاینت‌ها عبارتند از:

- می‌توان از آنها برای کشف و فراخوانی ویژگی‌ها روی سرور استفاده کرد.
- می‌توانند سرور را همزمان با راه‌اندازی خود آغاز کنند (مثل این فصل) اما کلاینت‌ها می‌توانند به سرورهای در حال اجرا هم متصل شوند.
- روش بسیار خوبی برای آزمودن قابلیت‌های سرور در کنار گزینه‌هایی مثل Inspector است که در فصل قبل شرح داده شد.

## منابع اضافی

- [ساخت کلاینت‌ها در MCP](https://modelcontextprotocol.io/quickstart/client)

## نمونه‌ها

- [ماشین حساب جاوا](../samples/java/calculator/README.md)
- [ماشین حساب .Net](../../../../03-GettingStarted/samples/csharp)
- [ماشین حساب جاوااسکریپت](../samples/javascript/README.md)
- [ماشین حساب تایپ‌اسکریپت](../samples/typescript/README.md)
- [ماشین حساب پایتون](../../../../03-GettingStarted/samples/python)
- [ماشین حساب راست](../../../../03-GettingStarted/samples/rust)

## مرحله بعد

- مرحله بعد: [ساخت کلاینت با LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**توضیحات مهم**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود، منبع معتبر و قطعی محسوب می‌شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما در قبال هرگونه سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->