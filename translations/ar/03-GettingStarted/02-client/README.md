# إنشاء عميل

العملاء هم تطبيقات مخصصة أو سكربتات تتواصل مباشرة مع خادم MCP لطلب الموارد، الأدوات، والمطالبات. بخلاف استخدام أداة المفتش التي توفر واجهة رسومية للتفاعل مع الخادم، كتابة عميل خاص بك تتيح تفاعلات مبرمجة وآلية. هذا يمكّن المطورين من دمج قدرات MCP في سير العمل الخاص بهم، أتمتة المهام، وبناء حلول مخصصة تلبي احتياجات محددة.

## نظرة عامة

تقدم هذه الدرس مفهوم العملاء داخل نظام بروتوكول سياق النموذج (MCP). ستتعلم كيفية كتابة عميل خاص بك وجعله يتصل بخادم MCP.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- فهم ما يمكن للعميل القيام به.
- كتابة عميل خاص بك.
- الاتصال واختبار العميل مع خادم MCP لضمان عمل الأخير كما هو متوقع.

## ما الذي يتطلبه كتابة عميل؟

لكتابة عميل، ستحتاج إلى القيام بما يلي:

- **استيراد المكتبات الصحيحة**. ستستخدم نفس المكتبة كما في السابق، فقط مع تراكيب مختلفة.
- **إنشاء نسخة من العميل**. هذا سيتضمن إنشاء مثيل للعميل وربطه بطريقة النقل المختارة.
- **تحديد الموارد التي سيتم سردها**. يأتي خادم MCP الخاص بك مع موارد، أدوات ومطالبات، تحتاج إلى تحديد أيها سيتم سردها.
- **دمج العميل مع تطبيق مضيف**. بمجرد معرفتك بقدرات الخادم، تحتاج إلى دمج هذا مع تطبيق المضيف بحيث إذا كتب المستخدم مطالبة أو أمرًا آخر يتم استدعاء الميزة المقابلة على الخادم.

الآن بعد أن فهمنا على مستوى عالٍ ما نحن على وشك القيام به، دعنا نلقي نظرة على مثال في القسم التالي.

### مثال على عميل

لنلق نظرة على هذا العميل النموذجي:

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

// قائمة الطلبات
const prompts = await client.listPrompts();

// الحصول على طلب
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// قائمة الموارد
const resources = await client.listResources();

// قراءة مورد
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// استدعاء أداة
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

في الشفرة السابقة قمنا بـ:

- استيراد المكتبات
- إنشاء نسخة من العميل وربطها باستخدام stdio للنقل.
- سرد المطالبات، الموارد، والأدوات واستدعاءها جميعًا.

هذا هو، عميل يمكنه التحدث إلى خادم MCP.

دعنا نأخذ وقتنا في قسم التمرين القادم ونفصل كل مقتطف كود ونشرح ما يجري.

## التمرين: كتابة عميل

كما ذُكر أعلاه، دعنا نأخذ وقتنا نشرح الكود، وبكل الوسائل قم بالبرمجة جنبًا إلى جنب إذا رغبت.

### -1- استيراد المكتبات

دعنا نستورد المكتبات التي نحتاجها، سنحتاج مراجع إلى العميل وبروتوكول النقل المختار، stdio. stdio هو بروتوكول للأشياء التي من المفترض أن تعمل على جهازك المحلي. SSE هو بروتوكول نقل آخر سنعرضه في الفصول القادمة لكنه خيارك الآخر. الآن، لنكمل مع stdio.

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
```

#### Java

بالنسبة للجافا، ستنشئ عميلًا يتصل بخادم MCP من التمرين السابق. باستخدام نفس هيكل مشروع Java Spring Boot من [البدء مع خادم MCP](../../../../03-GettingStarted/01-first-server/solution/java)، أنشئ فئة جافا جديدة باسم `SDKClient` في المجلد `src/main/java/com/microsoft/mcp/sample/client/` وأضف الاستيرادات التالية:

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

ستحتاج إلى إضافة الاعتمادات التالية إلى ملف `Cargo.toml` الخاص بك.

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

دعنا ننتقل إلى عملية التهيئة.

### -2- إنشاء العميل ووسيلة النقل

سنحتاج إلى إنشاء مثيل لوسيلة النقل وواحد للعميل:

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

- إنشاء مثيل لوسيلة النقل stdio. لاحظ كيف أنه يحدد الأمر والوسائط لكيفية العثور على الخادم وتشغيله لأن ذلك شيء سنحتاج للقيام به عند إنشاء العميل.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- إنشاء عميل بإعطائه اسمًا وإصدارًا.

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

# إنشاء معلمات الخادم لاتصال stdio
server_params = StdioServerParameters(
    command="mcp",  # قابل للتنفيذ
    args=["run", "server.py"],  # وسيطات اختيارية لسطر الأوامر
    env=None,  # متغيرات بيئة اختيارية
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # تهيئة الاتصال
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

في الكود السابق قمنا بما يلي:

- استيراد المكتبات اللازمة
- إنشاء كائن معلمات الخادم لأننا سنستخدمه لتشغيل الخادم حتى نتمكن من الاتصال به من خلال العميل.
- تعريف دالة `run` التي بدورها تستدعي `stdio_client` التي تبدأ جلسة العميل.
- إنشاء نقطة دخول حيث نوفر الدالة `run` إلى `asyncio.run`.

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

في الكود السابق قمنا بما يلي:

- استيراد المكتبات اللازمة.
- إنشاء وسيلة نقل stdio وإنشاء عميل `mcpClient`. هذا الأخير هو الذي سنستخدمه لسرد واستدعاء ميزات على خادم MCP.

ملاحظة، في "Arguments"، يمكنك الإشارة إما إلى *.csproj* أو إلى الملف التنفيذي.

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
        
        // هنا تذهب منطق العميل الخاص بك
    }
}
```

في الكود السابق قمنا بما يلي:

- إنشاء طريقة رئيسية تضبط وسيلة نقل SSE تشير إلى `http://localhost:8080` حيث سيعمل خادم MCP الخاص بنا.
- إنشاء فئة عميل تأخذ وسيلة النقل كمعامل منشئ.
- في طريقة `run`، ننشئ عميل MCP متزامن باستخدام وسيلة النقل ونبدأ الاتصال.
- استخدام وسيلة نقل SSE (Server-Sent Events) والتي تناسب الاتصالات المعتمدة على HTTP مع خوادم MCP باستخدام Java Spring Boot.

#### Rust

لاحظ أن هذا العميل الخاص بـ Rust يفترض أن الخادم هو مشروع شقيق باسم "calculator-server" في نفس الدليل. الكود أدناه سيبدأ الخادم ويتصل به.

```rust
async fn main() -> Result<(), RmcpError> {
    // افترض أن الخادم هو مشروع شقيق باسم "calculator-server" في نفس الدليل
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

    // مهمة: التهيئة

    // مهمة: سرد الأدوات

    // مهمة: استدعاء أداة الإضافة بالوسائط = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- سرد ميزات الخادم

الآن، لدينا عميل يمكنه الاتصال إذا تم تشغيل البرنامج. مع ذلك، لا يسرد ميزاته فعليًا، لذا دعنا نفعل ذلك الآن:

#### TypeScript

```typescript
// قائمة المطالبات
const prompts = await client.listPrompts();

// قائمة الموارد
const resources = await client.listResources();

// قائمة الأدوات
const tools = await client.listTools();
```

#### Python

```python
# سرد الموارد المتاحة
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# سرد الأدوات المتاحة
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

هنا نقوم بسرد الموارد المتاحة، `list_resources()` والأدوات، `list_tools` وطباعتها.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

أعلاه مثال كيف يمكننا سرد الأدوات على الخادم. لكل أداة، نطبع اسمها.

#### Java

```java
// قائمة وعرض الأدوات
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// يمكنك أيضًا إرسال طلب Ping للخادم للتحقق من الاتصال
client.ping();
```

في الكود السابق قمنا بما يلي:

- استدعاء `listTools()` للحصول على جميع الأدوات المتاحة من خادم MCP.
- استخدام `ping()` للتحقق من أن الاتصال بالخادم يعمل.
- يحتوي `ListToolsResult` على معلومات عن كل الأدوات بما في ذلك أسماؤها، أوصافها، ومخططات الإدخال الخاصة بها.

جيد، الآن قمنا بالتقاط كل الميزات. الآن السؤال، متى نستخدمها؟ حسنًا، هذا العميل بسيط جدًا، بسيط بمعنى أننا سنحتاج لاستدعاء الميزات صراحةً عندما نريدها. في الفصل التالي، سننشئ عميلًا أكثر تقدمًا لديه وصول إلى نموذج لغوي كبير خاص به، LLM. لكن الآن، دعنا نرى كيف يمكننا استدعاء الميزات على الخادم:

#### Rust

في الوظيفة الرئيسية، بعد تهيئة العميل، يمكننا تهيئة الخادم وسرد بعض ميزاته.

```rust
// تهيئة
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// قائمة الأدوات
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- استدعاء الميزات

لاستدعاء الميزات، نحتاج إلى التأكد من تحديد الوسائط الصحيحة وفي بعض الحالات اسم ما نحاول استدعاءه.

#### TypeScript

```typescript

// قراءة مورد
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// استدعاء أداة
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// استدعاء الموجه
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

في الكود السابق قمنا بـ:

- قراءة مورد، نستدعي المورد عبر استدعاء `readResource()` مع تحديد `uri`. هذا ما سيبدو عليه غالبًا على جانب الخادم:

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

- استدعاء أداة، نستدعيها بتحديد `name` و `arguments` هكذا:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- الحصول على مطالبة، للحصول على مطالبة، تستدعي `getPrompt()` مع `name` و `arguments`. كود الخادم يبدو هكذا:

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

    وكود العميل الناتج لذلك يبدو هكذا ليتطابق مع ما هو معلن على الخادم:

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
# قراءة مورد
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# استدعاء أداة
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

في الكود السابق قمنا بـ:

- استدعاء مورد اسمه `greeting` باستخدام `read_resource`.
- استدعاء أداة اسمها `add` باستخدام `call_tool`.

#### .NET

1. لنضيف بعض الكود لاستدعاء أداة:

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
// استدعاء أدوات حاسبة مختلفة
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

- استدعاء عدة أدوات حاسبة باستخدام طريقة `callTool()` مع كائنات `CallToolRequest`.
- كل استدعاء أداة يحدد اسم الأداة و`Map` من الوسائط المطلوبة بواسطة تلك الأداة.
- تتوقع أدوات الخادم أسماء معلمات محددة (مثل "a"، "b" للعمليات الرياضية).
- تُعاد النتائج ككائنات `CallToolResult` تحتوي على الرد من الخادم.

#### Rust

```rust
// استدعاء أداة الجمع مع الوسيطات = {"a": 3، "b": 2}
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

أضف الإدخال التالي إلى قسم "scripts" في *package.json* الخاص بك:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

استدع العميل بالأمر التالي:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

أولًا، تأكد من أن خادم MCP يعمل على `http://localhost:8080`. ثم شغّل العميل:

```bash
# بناء مشروعك
./mvnw clean compile

# تشغيل العميل
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

بدلاً من ذلك، يمكنك تشغيل مشروع العميل الكامل المقدم في مجلد الحل `03-GettingStarted\02-client\solution\java`:

```bash
# انتقل إلى دليل الحل
cd 03-GettingStarted/02-client/solution/java

# بناء وتشغيل ملف JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## المهمة

في هذه المهمة، ستستخدم ما تعلمته في إنشاء عميل، لكن أنشئ عميلًا خاصًا بك.

إليك خادم يمكنك استخدامه تحتاج لاستدعائه عبر كود العميل الخاص بك، تحقق إذا كنت تستطيع إضافة ميزات أكثر للخادم لجعله أكثر إثارة.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// إنشاء خادم MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// إضافة أداة إضافية
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// إضافة مورد ترحيب ديناميكي
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

// بدء استقبال الرسائل من الإدخال القياسي وإرسال الرسائل عبر الإخراج القياسي

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

# إنشاء خادم MCP
mcp = FastMCP("Demo")


# إضافة أداة جمع
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# إضافة مورد ترحيب ديناميكي
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

راجع هذا المشروع لترى كيف يمكنك [إضافة مطالبات وموارد](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

أيضًا، تحقق من هذا الرابط لمعرفة كيفية استدعاء [مطالبات وموارد](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

في [القسم السابق](../../../../03-GettingStarted/01-first-server)، تعلمت كيفية إنشاء خادم MCP بسيط باستخدام Rust. يمكنك الاستمرار في بناء ذلك أو الاطلاع على هذا الرابط لمزيد من أمثلة خوادم MCP المعتمدة على Rust: [أمثلة خادم MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## الحل

يحتوي **مجلد الحل** على تطبيقات عميل كاملة وجاهزة للتشغيل توضح كل المفاهيم المشروحة في هذا الدليل. كل حل يشمل كود العميل والخادم منظم في مشاريع منفصلة ومستقلة.

### 📁 هيكل المجلد الحل

يُنظم مجلد الحل حسب لغة البرمجة:

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

### 🚀 ماذا يتضمن كل حل

كل حل خاص بلغة معينة يوفر:

- **تطبيق عميل كامل** مع كل الميزات من الدليل
- **هيكل مشروع يعمل** مع الاعتمادات والتكوين المناسب
- **سكريبتات بناء وتشغيل** لتسهيل الإعداد والتنفيذ
- **ملف README مفصل** مع تعليمات خاصة باللغة
- **أمثلة معالجة الأخطاء** ومعالجة النتائج

### 📖 استخدام الحلول

1. **انتقل إلى مجلد اللغة المفضلة لديك**:

   ```bash
   cd solution/typescript/    # لـ TypeScript
   cd solution/java/          # لـ Java
   cd solution/python/        # لـ Python
   cd solution/dotnet/        # لـ .NET
   ```

2. **اتبع تعليمات README في كل مجلد ل**:
   - تثبيت الاعتمادات
   - بناء المشروع
   - تشغيل العميل

3. **الناتج المتوقع** الذي ينبغي أن تراه:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

للحصول على وثائق كاملة وتعليمات خطوة بخطوة، راجع: **[📖 وثائق الحل](./solution/README.md)**

## 🎯 أمثلة كاملة

قدمنا تطبيقات عميل كاملة وعاملة لكل لغات البرمجة التي تم تغطيتها في هذا الدليل. توضح هذه الأمثلة كامل الوظائف الموضحة أعلاه ويمكن استخدامها كنماذج مرجعية أو نقاط بداية لمشاريعك الخاصة.

### الأمثلة الكاملة المتاحة

| اللغة | الملف | الوصف |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | عميل جافا كامل يستخدم وسيلة نقل SSE مع معالجة شاملة للأخطاء |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | عميل C# كامل يستخدم وسيلة نقل stdio مع بدء تشغيل تلقائي للخادم |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | عميل TypeScript كامل بدعم كامل لبروتوكول MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | عميل Python كامل يستخدم نمط async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | عميل Rust كامل يستخدم Tokio للعمليات غير المتزامنة |

كل مثال كامل يتضمن:
- ✅ **إنشاء الاتصال** ومعالجة الأخطاء  
- ✅ **اكتشاف الخادم** (الأدوات، الموارد، الموجهات عند الاقتضاء)  
- ✅ **عمليات الآلة الحاسبة** (جمع، طرح، ضرب، قسمة، مساعدة)  
- ✅ **معالجة النتائج** والإخراج المنسق  
- ✅ **معالجة شاملة للأخطاء**  
- ✅ **كود نظيف وموثق** مع تعليقات خطوة بخطوة  

### البدء بأمثلة كاملة

1. **اختر لغتك المفضلة** من الجدول أعلاه  
2. **راجع ملف المثال الكامل** لفهم التنفيذ الكامل  
3. **شغل المثال** باتباع التعليمات في [`complete_examples.md`](./complete_examples.md)  
4. **قم بتعديل وتوسيع** المثال لحالتك الخاصة  

للحصول على توثيق مفصل حول تشغيل وتخصيص هذه الأمثلة، راجع: **[📖 توثيق الأمثلة الكاملة](./complete_examples.md)**  

### 💡 الحل مقابل الأمثلة الكاملة

| **مجلد الحل**       | **الأمثلة الكاملة**      |
|--------------------|-------------------------|
| هيكل مشروع كامل مع ملفات البناء | تنفيذات في ملف واحد       |
| جاهز للتشغيل مع التبعيات          | أمثلة كود مركزة          |
| إعداد يشبه الإنتاج              | مرجع تعليمي               |
| أدوات موجهة للغة معينة         | مقارنة متعددة اللغات       |

كلا النهجين قيم - استخدم **مجلد الحل** للمشاريع الكاملة و**الأمثلة الكاملة** للتعلم والمرجعية.  

## نقاط رئيسية

النقاط الرئيسية لهذا الفصل حول العملاء هي كما يلي:

- يمكن استخدامها لاكتشاف واستدعاء الميزات على الخادم.  
- يمكن أن يبدأ الخادم أثناء بدء تشغيله (كما في هذا الفصل) ولكن يمكن للعملاء الاتصال بالخوادم التي تعمل أيضًا.  
- هي طريقة رائعة لاختبار قدرات الخادم بجانب البدائل مثل المفتش كما وُصف في الفصل السابق.  

## موارد إضافية

- [بناء العملاء في MCP](https://modelcontextprotocol.io/quickstart/client)  

## عينات

- [آلة حاسبة جافا](../samples/java/calculator/README.md)  
- [آلة حاسبة .Net](../../../../03-GettingStarted/samples/csharp)  
- [آلة حاسبة جافا سكريبت](../samples/javascript/README.md)  
- [آلة حاسبة تايب سكريبت](../samples/typescript/README.md)  
- [آلة حاسبة بايثون](../../../../03-GettingStarted/samples/python)  
- [آلة حاسبة روست](../../../../03-GettingStarted/samples/rust)  

## ماذا بعد

- التالي: [إنشاء عميل مع LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للمواد المهمة والحساسة، يُنصح باستخدام ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->