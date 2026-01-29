# إنشاء عميل

العملاء هم تطبيقات أو سكربتات مخصصة تتواصل مباشرة مع خادم MCP لطلب الموارد، الأدوات، والمحفزات. على عكس استخدام أداة الفحص التي توفر واجهة رسومية للتفاعل مع الخادم، فإن كتابة عميل خاص بك يتيح التفاعل البرمجي والتلقائي. هذا يمكّن المطورين من دمج قدرات MCP في سير العمل الخاص بهم، أتمتة المهام، وبناء حلول مخصصة تلبي احتياجات محددة.

## نظرة عامة

تقدم هذه الدرس مفهوم العملاء ضمن نظام Model Context Protocol (MCP). ستتعلم كيفية كتابة عميل خاص بك وربطه بخادم MCP.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- فهم ما يمكن للعميل القيام به.
- كتابة عميل خاص بك.
- ربط العميل واختباره مع خادم MCP للتأكد من عمله كما هو متوقع.

## ما الذي يتطلبه كتابة عميل؟

لكتابة عميل، ستحتاج إلى القيام بما يلي:

- **استيراد المكتبات الصحيحة**. ستستخدم نفس المكتبة كما في السابق، ولكن مع استخدام تراكيب مختلفة.
- **إنشاء عميل**. يتضمن ذلك إنشاء مثيل للعميل وربطه بطريقة النقل المختارة.
- **تحديد الموارد التي تريد عرضها**. يأتي خادم MCP مع موارد، أدوات، ومحفزات، ويجب عليك تحديد ما تريد عرضه.
- **دمج العميل مع تطبيق مضيف**. بمجرد معرفة قدرات الخادم، تحتاج إلى دمج ذلك مع تطبيقك المضيف بحيث يتم استدعاء الميزة المناسبة على الخادم عند إدخال المستخدم أمرًا أو محفزًا.

الآن بعد أن فهمنا على مستوى عالٍ ما نحن بصدد القيام به، دعونا نلقي نظرة على مثال.

### مثال على عميل

لنلقِ نظرة على هذا المثال للعميل:

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

في الكود السابق قمنا بـ:

- استيراد المكتبات.
- إنشاء مثيل للعميل وربطه باستخدام stdio كوسيلة للنقل.
- عرض المحفزات، الموارد، والأدوات واستدعائها جميعًا.

ها قد حصلت على عميل يمكنه التحدث مع خادم MCP.

لنأخذ وقتنا في القسم التالي من التمارين ونفصل كل جزء من الكود ونشرح ما يحدث.

## تمرين: كتابة عميل

كما ذكرنا أعلاه، لنأخذ وقتنا في شرح الكود، وبكل تأكيد يمكنك كتابة الكود أثناء المتابعة إذا أردت.

### -1- استيراد المكتبات

لنقم باستيراد المكتبات التي نحتاجها، سنحتاج إلى مراجع لعميلنا وبروتوكول النقل الذي اخترناه، stdio. بروتوكول stdio مخصص للأشياء التي تعمل على جهازك المحلي. SSE هو بروتوكول نقل آخر سنعرضه في الفصول القادمة ولكنه خيارك الآخر. ولكن الآن، دعنا نستمر مع stdio.

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

بالنسبة لـ Java، ستقوم بإنشاء عميل يتصل بخادم MCP من التمرين السابق. باستخدام نفس بنية مشروع Java Spring Boot من [البدء مع خادم MCP](../../../../03-GettingStarted/01-first-server/solution/java)، قم بإنشاء فئة Java جديدة تسمى `SDKClient` في المجلد `src/main/java/com/microsoft/mcp/sample/client/` وأضف الاستيرادات التالية:

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

ستحتاج إلى إضافة التبعيات التالية إلى ملف `Cargo.toml`.

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

من هناك، يمكنك استيراد المكتبات اللازمة في كود العميل الخاص بك.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

دعنا ننتقل إلى إنشاء العميل.

### -2- إنشاء العميل ووسيلة النقل

سنحتاج إلى إنشاء مثيل لوسيلة النقل ومثيل للعميل الخاص بنا:

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

في الكود السابق قمنا بـ:

- إنشاء مثيل stdio كوسيلة للنقل. لاحظ كيف يحدد الأمر والمعاملات لكيفية العثور على الخادم وتشغيله، حيث سنحتاج إلى ذلك أثناء إنشاء العميل.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- إنشاء مثيل للعميل بإعطائه اسمًا وإصدارًا.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- ربط العميل بوسيلة النقل المختارة.

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

في الكود السابق قمنا بـ:

- استيراد المكتبات اللازمة.
- إنشاء كائن معلمات الخادم حيث سنستخدمه لتشغيل الخادم حتى نتمكن من الاتصال به باستخدام العميل.
- تعريف طريقة `run` التي تستدعي بدورها `stdio_client` لبدء جلسة العميل.
- إنشاء نقطة دخول حيث نوفر طريقة `run` إلى `asyncio.run`.

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

في الكود السابق قمنا بـ:

- استيراد المكتبات اللازمة.
- إنشاء وسيلة نقل stdio وإنشاء عميل `mcpClient`. الأخير هو ما سنستخدمه لعرض واستدعاء الميزات على خادم MCP.

ملاحظة: في "Arguments"، يمكنك الإشارة إما إلى ملف *.csproj* أو إلى الملف التنفيذي.

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

في الكود السابق قمنا بـ:

- إنشاء طريقة رئيسية تقوم بإعداد وسيلة نقل SSE تشير إلى `http://localhost:8080` حيث سيعمل خادم MCP الخاص بنا.
- إنشاء فئة عميل تأخذ وسيلة النقل كمعامل في المنشئ.
- في طريقة `run`، نقوم بإنشاء عميل MCP متزامن باستخدام وسيلة النقل ونبدأ الاتصال.
- استخدام وسيلة نقل SSE (Server-Sent Events) المناسبة للتواصل المستند إلى HTTP مع خوادم Java Spring Boot MCP.

#### Rust

هذا العميل المكتوب بلغة Rust يفترض أن الخادم هو مشروع شقيق يسمى "calculator-server" في نفس الدليل. الكود أدناه سيبدأ الخادم ويتصل به.

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

### -3- عرض ميزات الخادم

الآن، لدينا عميل يمكنه الاتصال إذا تم تشغيل البرنامج. ومع ذلك، فإنه لا يعرض ميزاته، لذا دعنا نفعل ذلك الآن:

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

هنا نقوم بعرض الموارد المتاحة باستخدام `list_resources()` والأدوات باستخدام `list_tools` وطباعتها.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

أعلاه مثال على كيفية عرض الأدوات على الخادم. لكل أداة، نقوم بعد ذلك بطباعة اسمها.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

في الكود السابق قمنا بـ:

- استدعاء `listTools()` للحصول على جميع الأدوات المتاحة من خادم MCP.
- استخدام `ping()` للتحقق من أن الاتصال بالخادم يعمل.
- يحتوي `ListToolsResult` على معلومات حول جميع الأدوات بما في ذلك أسمائها، أوصافها، ومخططات الإدخال الخاصة بها.

رائع، الآن قمنا بجمع جميع الميزات. السؤال الآن هو متى نستخدمها؟ حسنًا، هذا العميل بسيط جدًا، بمعنى أنه سيتعين علينا استدعاء الميزات صراحةً عند الحاجة. في الفصل التالي، سنقوم بإنشاء عميل أكثر تقدمًا لديه إمكانية الوصول إلى نموذج لغوي كبير خاص به (LLM). ولكن الآن، دعنا نرى كيف يمكننا استدعاء الميزات على الخادم:

#### Rust

في الدالة الرئيسية، بعد تهيئة العميل، يمكننا تهيئة الخادم وعرض بعض ميزاته.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- استدعاء الميزات

لاستدعاء الميزات، نحتاج إلى التأكد من تحديد المعاملات الصحيحة وفي بعض الحالات اسم ما نحاول استدعاءه.

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

في الكود السابق قمنا بـ:

- قراءة مورد، نستدعي المورد باستخدام `readResource()` مع تحديد `uri`. هذا ما قد يبدو عليه على جانب الخادم:

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

    قيمة `uri` الخاصة بنا `file://example.txt` تتطابق مع `file://{name}` على الخادم. سيتم تعيين `example.txt` إلى `name`.

- استدعاء أداة، نستدعيها بتحديد `name` و`arguments` كما يلي:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- الحصول على محفز، للحصول على محفز، نستدعي `getPrompt()` مع `name` و`arguments`. كود الخادم يبدو كما يلي:

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

    وبالتالي يبدو كود العميل الناتج كما يلي ليتطابق مع ما تم تعريفه على الخادم:

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

في الكود السابق قمنا بـ:

- استدعاء مورد يسمى `greeting` باستخدام `read_resource`.
- استدعاء أداة تسمى `add` باستخدام `call_tool`.

#### .NET

1. لنضف بعض الكود لاستدعاء أداة:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. لطباعة النتيجة، إليك بعض الكود للتعامل مع ذلك:

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

في الكود السابق قمنا بـ:

- استدعاء أدوات حاسبة متعددة باستخدام طريقة `callTool()` مع كائنات `CallToolRequest`.
- يحدد كل استدعاء أداة اسم الأداة و`Map` من المعاملات المطلوبة لتلك الأداة.
- تتوقع أدوات الخادم أسماء معلمات محددة (مثل "a"، "b" للعمليات الرياضية).
- يتم إرجاع النتائج ككائنات `CallToolResult` تحتوي على الاستجابة من الخادم.

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

### -5- تشغيل العميل

لتشغيل العميل، اكتب الأمر التالي في الطرفية:

#### TypeScript

أضف الإدخال التالي إلى قسم "scripts" في *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

استدعِ العميل باستخدام الأمر التالي:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

أولاً، تأكد من تشغيل خادم MCP الخاص بك على `http://localhost:8080`. ثم قم بتشغيل العميل:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

بدلاً من ذلك، يمكنك تشغيل مشروع العميل الكامل المقدم في مجلد الحل `03-GettingStarted\02-client\solution\java`:

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

## المهمة

في هذه المهمة، ستستخدم ما تعلمته في إنشاء عميل ولكن ستقوم بإنشاء عميل خاص بك.

إليك خادم يمكنك استخدامه والذي تحتاج إلى استدعائه عبر كود العميل الخاص بك، حاول إضافة المزيد من الميزات إلى الخادم لجعله أكثر إثارة.

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

راجع هذا المشروع لمعرفة كيفية [إضافة المحفزات والموارد](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

أيضًا، تحقق من هذا الرابط لمعرفة كيفية استدعاء [المحفزات والموارد](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

في [القسم السابق](../../../../03-GettingStarted/01-first-server)، تعلمت كيفية إنشاء خادم MCP بسيط باستخدام Rust. يمكنك الاستمرار في البناء على ذلك أو مراجعة هذا الرابط للحصول على المزيد من أمثلة خوادم MCP المستندة إلى Rust: [أمثلة خوادم MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## الحل

يتضمن **مجلد الحل** تطبيقات عملاء كاملة وجاهزة للتشغيل توضح جميع المفاهيم التي تمت تغطيتها في هذا الدرس. يتضمن كل حل كود العميل والخادم منظمًا في مشاريع منفصلة ومستقلة.

### 📁 بنية الحل

يتم تنظيم دليل الحل حسب لغة البرمجة:

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

### 🚀 ما يتضمنه كل حل

يوفر كل حل خاص بلغة البرمجة:

- **تنفيذ كامل للعميل** مع جميع الميزات من الدرس.
- **بنية مشروع جاهزة للعمل** مع التبعيات والتكوين المناسب.
- **برامج بناء وتشغيل** لتسهيل الإعداد والتنفيذ.
- **README مفصل** مع تعليمات خاصة باللغة.
- **أمثلة على معالجة الأخطاء** ومعالجة النتائج.

### 📖 استخدام الحلول

1. **انتقل إلى مجلد اللغة المفضلة لديك**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **اتبع تعليمات README** في كل مجلد لـ:
   - تثبيت التبعيات.
   - بناء المشروع.
   - تشغيل العميل.

3. **المخرجات المتوقعة** التي يجب أن تراها:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

للحصول على وثائق كاملة وتعليمات خطوة بخطوة، راجع: **[📖 وثائق الحل](./solution/README.md)**

## 🎯 أمثلة كاملة

لقد قدمنا تطبيقات عملاء كاملة وعاملة لجميع لغات البرمجة التي تمت تغطيتها في هذا الدرس. توضح هذه الأمثلة الوظائف الكاملة الموضحة أعلاه ويمكن استخدامها كمرجع أو كنقطة انطلاق لمشاريعك الخاصة.

### أمثلة كاملة متوفرة

| اللغة | الملف | الوصف |
|-------|-------|-------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | عميل Java كامل يستخدم وسيلة نقل SSE مع معالجة شاملة للأخطاء |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | عميل C# كامل يستخدم وسيلة نقل stdio مع تشغيل تلقائي للخادم |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | عميل TypeScript كامل مع دعم كامل لبروتوكول MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | عميل Python كامل يستخدم أنماط async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | عميل Rust كامل يستخدم Tokio للعمليات غير المتزامنة |
كل مثال مكتمل يتضمن:

- ✅ **إنشاء الاتصال** ومعالجة الأخطاء  
- ✅ **اكتشاف الخادم** (الأدوات، الموارد، التعليمات عند الاقتضاء)  
- ✅ **عمليات الآلة الحاسبة** (الجمع، الطرح، الضرب، القسمة، المساعدة)  
- ✅ **معالجة النتائج** وإخراجها بشكل منسق  
- ✅ **معالجة شاملة للأخطاء**  
- ✅ **كود نظيف وموثق** مع تعليقات خطوة بخطوة  

### البدء مع الأمثلة الكاملة

1. **اختر لغتك المفضلة** من الجدول أعلاه  
2. **راجع ملف المثال الكامل** لفهم التنفيذ بالكامل  
3. **قم بتشغيل المثال** باتباع التعليمات في [`complete_examples.md`](./complete_examples.md)  
4. **قم بتعديل وتوسيع** المثال ليناسب حالتك الخاصة  

للحصول على توثيق مفصل حول تشغيل وتخصيص هذه الأمثلة، راجع: **[📖 توثيق الأمثلة الكاملة](./complete_examples.md)**  

### 💡 الحل مقابل الأمثلة الكاملة

| **مجلد الحل**         | **الأمثلة الكاملة**         |
|--------------------|---------------------|
| هيكل مشروع كامل مع ملفات البناء | تنفيذات في ملف واحد |
| جاهز للتشغيل مع التبعيات | أمثلة تعليمية مركزة |
| إعداد يشبه الإنتاج | مرجع تعليمي |
| أدوات مخصصة للغة | مقارنة بين اللغات |

كلا النهجين لهما قيمة - استخدم **مجلد الحل** للمشاريع الكاملة و**الأمثلة الكاملة** للتعلم والمرجعية.

## النقاط الرئيسية

النقاط الرئيسية لهذا الفصل تتعلق بالعملاء:

- يمكن استخدامها لاكتشاف الميزات وتنفيذها على الخادم.  
- يمكنها بدء خادم أثناء تشغيلها (كما في هذا الفصل)، ولكن يمكن للعملاء أيضًا الاتصال بالخوادم التي تعمل بالفعل.  
- تُعد وسيلة رائعة لاختبار قدرات الخادم بجانب بدائل مثل "المفتش" كما تم وصفه في الفصل السابق.  

## موارد إضافية

- [بناء العملاء في MCP](https://modelcontextprotocol.io/quickstart/client)  

## أمثلة

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)  

## ما التالي

- التالي: [إنشاء عميل باستخدام LLM](../03-llm-client/README.md)  

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حساسة أو هامة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.