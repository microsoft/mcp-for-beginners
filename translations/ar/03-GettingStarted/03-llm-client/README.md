# إنشاء عميل مع LLM

حتى الآن، شاهدت كيفية إنشاء خادم وعميل. كان العميل قادرًا على الاتصال بالخادم بشكل صريح لقائمة أدواته وموارده والمطالبات. ومع ذلك، هذه ليست طريقة عملية جدًا. يعيش مستخدموك في عصر الوكلاء ويتوقعون استخدام المطالبات والتواصل مع LLM بدلاً من ذلك. لا يهتمون إذا كنت تستخدم MCP لتخزين قدراتك؛ بل يتوقعون ببساطة التفاعل باستخدام اللغة الطبيعية. فكيف نحل هذا؟ الحل هو إضافة LLM إلى العميل.

## نظرة عامة

في هذا الدرس نركز على إضافة LLM إلى عميلك ونوضح كيف يوفر هذا تجربة أفضل بكثير لمستخدمك.

## أهداف التعلم

بحلول نهاية هذا الدرس، ستتمكن من:

- إنشاء عميل مع LLM.
- التفاعل بسلاسة مع خادم MCP باستخدام LLM.
- توفير تجربة مستخدم أفضل على جانب العميل.

## النهج

لنحاول فهم النهج الذي نحتاج إلى اتخاذه. إضافة LLM تبدو بسيطة، لكن هل سنفعل ذلك فعلاً؟

إليك كيف سيتفاعل العميل مع الخادم:

1. إقامة اتصال مع الخادم.

1. قائمة القدرات، المطالبات، الموارد والأدوات، وحفظ مخططها.

1. إضافة LLM وتمرير القدرات المحفوظة ومخططها في صيغة يفهمها LLM.

1. معالجة مطالبة المستخدم بتمريرها إلى LLM مع الأدوات التي أدرجها العميل.

رائع، الآن فهمنا كيف يمكننا فعل ذلك على المستوى العالي، دعنا نجرب ذلك في التمرين أدناه.

## تمرين: إنشاء عميل مع LLM

في هذا التمرين، سنتعلم إضافة LLM إلى عميلنا.

### المصادقة باستخدام رمز الوصول الشخصي لـ GitHub

إنشاء رمز GitHub هو عملية بسيطة. إليك كيف تفعل ذلك:

- اذهب إلى إعدادات GitHub – اضغط على صورة ملفك الشخصي في الزاوية العلوية اليمنى واختر الإعدادات.
- انتقل إلى إعدادات المطور – قم بالتمرير لأسفل واضغط على إعدادات المطور.
- اختر رموز الوصول الشخصية – اضغط على الرموز الدقيقة التحكم ثم إنشاء رمز جديد.
- قم بتكوين رمزك – أضف ملاحظة للرجوع إليها، حدد تاريخ انتهاء صلاحية، واختر النطاقات الضرورية (الأذونات). في هذه الحالة تأكد من إضافة إذن النماذج.
- أنشئ ونسخ الرمز – اضغط على إنشاء رمز، وتأكد من نسخه مباشرةً لأنه لن يكون بإمكانك رؤيته مرة أخرى.

### -1- الاتصال بالخادم

لنقم بإنشاء عميلنا أولاً:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // استيراد zod للتحقق من صحة المخطط

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

في الكود السابق قمنا بـ:

- استيراد المكتبات اللازمة
- إنشاء فئة تحتوي على عضوين، `client` و `openai`، لمساعدتنا في إدارة العميل والتفاعل مع LLM على التوالي.
- تكوين مثيل LLM لاستخدام نماذج GitHub عن طريق ضبط `baseUrl` للإشارة إلى واجهة برمجة تطبيقات الاستدلال.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# إنشاء معايير الخادم لاتصال stdio
server_params = StdioServerParameters(
    command="mcp",  # قابل للتنفيذ
    args=["run", "server.py"],  # وسائط سطر الأوامر الاختيارية
    env=None,  # متغيرات البيئة الاختيارية
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

في الكود السابق قمنا بـ:

- استيراد المكتبات اللازمة لـ MCP
- إنشاء عميل

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

أولاً، ستحتاج إلى إضافة تبعيات LangChain4j إلى ملف `pom.xml` الخاص بك. أضف هذه التبعيات لتمكين دمج MCP ودعم نماذج GitHub:

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

ثم أنشئ فئة عميل Java الخاصة بك:

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
    
    public static void main(String[] args) throws Exception {        // تكوين LLM لاستخدام نماذج GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // إنشاء ناقل MCP للاتصال بالخادم
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // إنشاء عميل MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

في الكود السابق قمنا بـ:

- **إضافة تبعيات LangChain4j**: المطلوبة لدمج MCP، عميل OpenAI الرسمي، ودعم نماذج GitHub
- **استيراد مكتبات LangChain4j**: لدمج MCP ووظائف نموذج دردشة OpenAI
- **إنشاء `ChatLanguageModel`**: تم تكوينه لاستخدام نماذج GitHub مع رمز GitHub الخاص بك
- **إعداد النقل عبر HTTP**: باستخدام Server-Sent Events (SSE) للاتصال بخادم MCP
- **إنشاء عميل MCP**: الذي سيتولى الاتصال بالخادم
- **استخدام دعم MCP المدمج في LangChain4j**: مما يبسط التكامل بين LLMs وخوادم MCP

#### Rust

تفترض هذه الأمثلة أن لديك خادم MCP يعتمد على Rust يعمل. إذا لم يكن لديك واحد، ارجع إلى درس [01-first-server](../01-first-server/README.md) لإنشاء الخادم.

بمجرد أن يكون لديك خادم MCP الخاص بـ Rust، افتح الطرفية وانتقل إلى نفس دليل الخادم. ثم نفذ الأمر التالي لإنشاء مشروع عميل LLM جديد:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

أضف التبعيات التالية إلى ملف `Cargo.toml` الخاص بك:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> لا توجد مكتبة رسمية لـ Rust لـ OpenAI، ومع ذلك، `async-openai` هي [مكتبة يحافظ عليها المجتمع](https://platform.openai.com/docs/libraries/rust#rust) وغالبًا ما تُستخدم.

افتح ملف `src/main.rs` واستبدل محتواه بالكود التالي:

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
    // الرسالة الأولية
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // إعداد عميل OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // إعداد عميل MCP
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

    // يجب القيام به: الحصول على قائمة أدوات MCP

    // يجب القيام به: محادثة LLM مع استدعاءات الأدوات

    Ok(())
}
```

يقوم هذا الكود بإعداد تطبيق Rust أساسي سيتصل بخادم MCP ونماذج GitHub لتفاعل LLM.

> [!IMPORTANT]
> تأكد من تعيين متغير البيئة `OPENAI_API_KEY` باستخدام رمز GitHub الخاص بك قبل تشغيل التطبيق.

رائع، للخطوة التالية، دعنا ندرج القدرات على الخادم.

### -2- قائمة قدرات الخادم

الآن سنتصل بالخادم ونطلب منه قدراته:

#### Typescript

في نفس الفئة، أضف الطرق التالية:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // سرد الأدوات
    const toolsResult = await this.client.listTools();
}
```

في الكود السابق قمنا بـ:

- أضفنا كودًا للاتصال بالخادم، `connectToServer`.
- أنشأنا دالة `run` مسؤولة عن التعامل مع تدفق التطبيق. حتى الآن تكتفي ببساطة بإدراج الأدوات ولكننا سنضيف المزيد قريبًا.

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
    print("Tool", tool.inputSchema["properties"])
```

إليك ما أضفناه:

- سرد الموارد والأدوات وطباعتها. بالنسبة للأدوات، نُدرج أيضًا `inputSchema` الذي نستخدمه لاحقًا.

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

في الكود السابق قمنا بـ:

- سرد الأدوات المتاحة على خادم MCP
- لكل أداة، سرد الاسم والوصف والمخطط الخاص بها. الأخير هو شيء سنستخدمه لاستدعاء الأدوات قريبًا.

#### Java

```java
// إنشاء مزود أدوات يكتشف أدوات MCP تلقائيًا
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// يقوم مزود أدوات MCP تلقائيًا بالتعامل مع:
// - سرد الأدوات المتاحة من خادم MCP
// - تحويل مخططات أدوات MCP إلى صيغة LangChain4j
// - إدارة تنفيذ الأدوات والاستجابات
```

في الكود السابق قمنا بـ:

- إنشاء `McpToolProvider` الذي يكتشف ويسجل تلقائيًا جميع الأدوات من خادم MCP
- موفر الأدوات يتعامل داخليًا مع التحويل بين مخططات أدوات MCP وصيغة أدوات LangChain4j
- هذا النهج يلغي الحاجة إلى سرد وتحويل الأدوات يدويًا

#### Rust

يتم استرداد الأدوات من خادم MCP باستخدام دالة `list_tools`. في دالتك `main`، وبعد إعداد عميل MCP، أضف الكود التالي:

```rust
// احصل على قائمة أدوات MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- تحويل قدرات الخادم إلى أدوات LLM

الخطوة التالية بعد سرد قدرات الخادم هي تحويلها إلى صيغة يفهمها LLM. بمجرد القيام بذلك، يمكننا تقديم هذه القدرات كأدوات لـ LLM.

#### TypeScript

1. أضف الكود التالي لتحويل استجابة خادم MCP إلى صيغة تعريف أداة يمكن لـ LLM استخدامها:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // إنشاء مخطط زود بناءً على input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // تعيين النوع صراحة إلى "function"
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

    الكود أعلاه يأخذ استجابة من خادم MCP ويحولها إلى صيغة تعريف أداة يمكن لـ LLM فهمها.

1. لنعمل تحديثًا على دالة `run` بعد ذلك لسرد قدرات الخادم:

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

    في الكود السابق، قمنا بتحديث دالة `run` للتكرار عبر النتيجة ومن ثم لكل إدخال استدعاء `openAiToolAdapter`.

#### Python

1. أولاً، لننشئ دالة التحويل التالية

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

    في الدالة `convert_to_llm_tools` أعلاه نأخذ استجابة أداة MCP ونحولها إلى صيغة يمكن لـ LLM فهمها.

1. بعد ذلك، دعونا نحدث كود العميل لدينا ليستفيد من هذه الدالة كما يلي:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    هنا، نضيف استدعاءً إلى `convert_to_llm_tool` لتحويل استجابة أداة MCP إلى شيء يمكننا تمريره إلى LLM لاحقًا.

#### .NET

1. دعونا نضيف كودًا لتحويل استجابة أداة MCP إلى صيغة يمكن أن يفهمها LLM

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

في الكود السابق قمنا بـ:

- إنشاء دالة `ConvertFrom` التي تأخذ الاسم والوصف ومخطط الإدخال.
- تحديد وظيفة تنشئ `FunctionDefinition` يتم تمريرها إلى `ChatCompletionsDefinition`. الأخير شيء يمكن لـ LLM فهمه.

1. لنر كيف يمكننا تحديث بعض الكود الحالي للاستفادة من هذه الدالة أعلاه:

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
// إنشاء واجهة روبوت للتفاعل باللغة الطبيعية
public interface Bot {
    String chat(String prompt);
}

// تكوين خدمة الذكاء الاصطناعي باستخدام أدوات LLM و MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

في الكود السابق قمنا بـ:

- تعريف واجهة بسيطة `Bot` للتفاعل باستخدام اللغة الطبيعية
- استخدام `AiServices` من LangChain4j لربط LLM تلقائيًا مع موفر أدوات MCP
- الإطار يتعامل تلقائيًا مع تحويل مخطط الأداة واستدعاء الوظائف في الخلفية
- هذا النهج يلغي الحاجة للتحويل اليدوي للأدوات - LangChain4j يتولى كل التعقيد في تحويل أدوات MCP إلى صيغة متوافقة مع LLM

#### Rust

لتحويل استجابة أداة MCP إلى صيغة يمكن لـ LLM فهمها، سنضيف دالة مساعدة تقوم بتنسيق قائمة الأدوات. أضف الكود التالي إلى ملف `main.rs` الخاص بك أسفل دالة `main`. سيتم استدعاؤه عند تقديم طلبات إلى LLM:

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

رائع، نحن الآن جاهزون للتعامل مع أي طلبات مستخدم، لذا دعنا ننتقل إلى ذلك.

### -4- معالجة مطالبة المستخدم

في هذا الجزء من الكود، سنتعامل مع طلبات المستخدم.

#### TypeScript

1. أضف دالة ستُستخدم لاستدعاء LLM الخاص بنا:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // ٢. استدعاء أداة الخادم
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ٣. القيام بشيء مع النتيجة
        // للقيام

        }
    }
    ```

    في الكود السابق:

    - أضفنا دالة `callTools`.
    - الدالة تأخذ استجابة من LLM وتتحقق لمعرفة الأدوات التي تم استدعاؤها، إن وجدت:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // استدعاء الأداة
        }
        ```

    - تستدعي أداة إذا أشارت LLM إلى وجوب استدعائها:

        ```typescript
        // ٢. استدعاء أداة الخادم
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ٣. القيام بشيء ما بالنتيجة
        // TODO
        ```

1. حدّث دالة `run` لتشمل مكالمات إلى LLM واستدعاء `callTools`:

    ```typescript

    // 1. إنشاء رسائل تكون مدخلاً لـ LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. استدعاء LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. استعراض رد LLM، والتحقق من كل اختيار إذا كان يحتوي على استدعاءات أدوات
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

رائع، لنضع الكود كاملًا:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // استيراد zod للتحقق من صحة المخطط

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // قد تحتاج إلى التغيير إلى هذا العنوان في المستقبل: https://models.github.ai/inference
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
          // إنشاء مخطط zod بناءً على input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // تعيين النوع صراحة إلى "دالة"
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
    
    
          // 2. استدعاء أداة الخادم
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. القيام بشيء بالنتيجة
          // للقيام به
    
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
    
        // 1. المرور عبر استجابة LLM، لكل خيار، التحقق مما إذا كان يحتوي على استدعاءات أدوات
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

1. دعنا نضيف بعض الاستيرادات اللازمة لاستدعاء LLM

    ```python
    # نموذج لغة كبير
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. بعد ذلك، دعنا نضيف الدالة التي ستستدعي LLM:

    ```python
    # نموذج لغوي كبير

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
            # معلمات اختيارية
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

    في الكود السابق قمنا بـ:

    - تمرير دالاتنا، التي وجدناها على خادم MCP وحولناها، إلى LLM.
    - ثم استدعينا LLM باستخدام هذه الدالات.
    - ثم نقوم بتفحص النتيجة لمعرفة الدالات التي يجب استدعاؤها، إن وجدت.
    - أخيرًا، نمرر مجموعة من الدالات للاستدعاء.

1. الخطوة النهائية، دعونا نحدث الكود الرئيسي:

    ```python
    prompt = "Add 2 to 20"

    # اسأل نموذج اللغة الكبير عن الأدوات المتاحة، إن وجدت
    functions_to_call = call_llm(prompt, functions)

    # استدعِ الدوال المقترحة
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    هناك، كانت الخطوة الأخيرة، في الكود أعلاه نحن:

    - نستدعي أداة MCP عبر `call_tool` باستخدام دالة اعتقد LLM أنه ينبغي علينا استدعاؤها بناءً على مطالبتنا.
    - نطبع نتيجة استدعاء الأداة إلى خادم MCP.

#### .NET

1. دعنا نعرض بعض الكود لطلب مطالبة LLM:

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

    في الكود السابق قمنا بـ:

    - جلب الأدوات من خادم MCP، `var tools = await GetMcpTools()`.
    - تعريف مطالبة المستخدم `userMessage`.
    - إنشاء كائن خيارات يحدد النموذج والأدوات.
    - إجراء طلب نحو LLM.

1. خطوة أخيرة، دعنا نرى إذا كان LLM يعتقد أنه ينبغي علينا استدعاء دالة:

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

    في الكود السابق قمنا بـ:

    - التكرار خلال قائمة استدعاءات الدوال.
    - لكل استدعاء أداة، تحليل الاسم والوسائط واستدعاء الأداة على خادم MCP باستخدام عميل MCP. وأخيرًا نطبع النتائج.

إليك الكود كاملًا:

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
    // تنفيذ طلبات اللغة الطبيعية التي تستخدم أدوات MCP تلقائيًا
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

في الكود السابق قمنا بـ:

- استخدام مطالبات لغة طبيعية بسيطة للتفاعل مع أدوات خادم MCP
- إطار عمل LangChain4j يتعامل تلقائيًا مع:
  - تحويل مطالبات المستخدم إلى استدعاءات أدوات عند الحاجة
  - استدعاء أدوات MCP المناسبة بناءً على قرار LLM
  - إدارة تدفق المحادثة بين LLM وخادم MCP
- دالة `bot.chat()` تُرجع ردودًا بلغة طبيعية قد تشمل نتائج تنفيذ أدوات MCP
- هذا النهج يوفر تجربة مستخدم سلسة حيث لا يحتاج المستخدمون لمعرفة التنفيذ الأساسي لـ MCP

مثال الكود الكامل:

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

هنا يحدث الجزء الأكبر من العمل. سنقوم باستدعاء LLM مع مطالبة المستخدم الأولية، ثم معالجة الاستجابة لمعرفة إذا كانت هناك حاجة لاستدعاء أي أدوات. إذا كان الأمر كذلك، سنستدعي تلك الأدوات ونواصل المحادثة مع LLM حتى لا تصبح هناك حاجة لمزيد من استدعاءات الأدوات ونحصل على استجابة نهائية.

سنقوم بعمل عدة استدعاءات لـ LLM، لذا دعونا نعرف دالة ستتعامل مع استدعاء LLM. أضف الدالة التالية إلى ملف `main.rs`:

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

تأخذ هذه الدالة عميل LLM، قائمة الرسائل (بما في ذلك مطالبة المستخدم)، أدوات من خادم MCP، وترسل طلبًا إلى LLM، معيدة الاستجابة.
ستحتوي الاستجابة من نموذج اللغة الكبير (LLM) على مصفوفة من `choices`. سنحتاج إلى معالجة النتيجة لمعرفة ما إذا كانت هناك أي `tool_calls` موجودة. هذا يتيح لنا معرفة أن نموذج اللغة الكبير يطلب استدعاء أداة معينة مع الوسائط. أضف الكود التالي إلى أسفل ملف `main.rs` لتعريف دالة لمعالجة استجابة نموذج اللغة الكبير:

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

    // طباعة المحتوى إذا كان متوفراً
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // التعامل مع استدعاءات الأدوات
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // إضافة رسالة المساعد

        // تنفيذ كل استدعاء أداة
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // إضافة نتيجة الأداة إلى الرسائل
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // متابعة المحادثة مع نتائج الأدوات
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


إذا كانت `tool_calls` موجودة، فإنه يستخرج معلومات الأداة، يستدعي خادم MCP مع طلب الأداة، ويضيف النتائج إلى رسائل المحادثة. ثم يستمر في المحادثة مع نموذج اللغة الكبير ويتم تحديث الرسائل باستجابة المساعد ونتائج استدعاء الأداة.

لاستخراج معلومات استدعاء الأداة التي يعيدها نموذج اللغة الكبير لاستدعاءات MCP، سنضيف دالة مساعدة أخرى لاستخراج كل ما هو مطلوب لإجراء الاستدعاء. أضف الكود التالي إلى أسفل ملف `main.rs` الخاص بك:

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


مع وجود جميع الأجزاء في مكانها، يمكننا الآن التعامل مع موجه المستخدم الأولي واستدعاء نموذج اللغة الكبير. حدّث دالة `main` لتشمل الكود التالي:

```rust
// محادثة LLM مع استدعاءات الأدوات
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


سيستعلم هذا نموذج اللغة الكبير باستخدام موجه المستخدم الأولي طالبًا مجموع رقمين، وسيعالِج الاستجابة للتعامل الديناميكي مع استدعاءات الأدوات.

رائع، لقد قمت بذلك!

## المهمة

خذ الكود من التمرين وابنِ الخادم مع بعض الأدوات الإضافية. ثم أنشئ عميلًا مع نموذج لغة كبير، كما في التمرين، واختبره مع موجهات مختلفة للتأكد من استدعاء جميع أدوات الخادم لديك ديناميكيًا. هذه الطريقة في بناء عميل تعني أن المستخدم النهائي سيحصل على تجربة مستخدم رائعة حيث يستطيع استخدام الموجهات بدلاً من أوامر العميل الدقيقة، وسيكون غير مدرك لأي استدعاء لخادم MCP.

## الحل

[الحل](/03-GettingStarted/03-llm-client/solution/README.md)

## النقاط الرئيسية المستفادة

- إضافة نموذج لغة كبير إلى عميلك يوفر طريقة أفضل للمستخدمين للتفاعل مع خوادم MCP.
- تحتاج إلى تحويل استجابة خادم MCP إلى شيء يمكن لنموذج اللغة الكبير فهمه.

## عينات

- [آلة حاسبة جافا](../samples/java/calculator/README.md)
- [آلة حاسبة .Net](../../../../03-GettingStarted/samples/csharp)
- [آلة حاسبة جافا سكريبت](../samples/javascript/README.md)
- [آلة حاسبة تايب سكريبت](../samples/typescript/README.md)
- [آلة حاسبة بايثون](../../../../03-GettingStarted/samples/python)
- [آلة حاسبة راست](../../../../03-GettingStarted/samples/rust)

## موارد إضافية

## التالي

- التالي: [استهلاك خادم باستخدام Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والموثوق. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->