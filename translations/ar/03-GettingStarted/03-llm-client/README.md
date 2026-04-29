# إنشاء عميل مع LLM

حتى الآن، رأيت كيف تنشئ خادمًا وعميلًا. كان العميل قادرًا على استدعاء الخادم صراحةً لقائمة أدواته وموارده والمحرضات. ومع ذلك، هذه ليست طريقة عملية جدًا. يعيش مستخدموك في عصر الوكلاء ويتوقعون استخدام المحرضات والتواصل مع LLM بدلاً من ذلك. لا يهتمون بما إذا كنت تستخدم MCP لتخزين قدراتك؛ فهم فقط يتوقعون التفاعل باستخدام اللغة الطبيعية. فكيف نحل هذا؟ الحل هو إضافة LLM إلى العميل.

## نظرة عامة

في هذا الدرس نركز على إضافة LLM ليقوم بعميلك ونوضح كيف يوفر هذا تجربة أفضل بكثير لمستخدمك.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- إنشاء عميل مع LLM.
- التفاعل بسلاسة مع خادم MCP باستخدام LLM.
- توفير تجربة مستخدم نهائية أفضل على جانب العميل.

## النهج

دعونا نحاول فهم النهج الذي نحتاج لاتخاذه. يبدو أن إضافة LLM أمر بسيط، لكن هل سنقوم بذلك بالفعل؟

إليك كيف سيتفاعل العميل مع الخادم:

1. إنشاء اتصال بالخادم.

1. سرد القدرات، والمحرضات، والموارد، والأدوات، وحفظ مخططها.

1. إضافة LLM وتمرير القدرات المحفوظة ومخططها بطريقة يفهمها LLM.

1. التعامل مع محرض المستخدم بتمريره إلى LLM مع الأدوات المدرجة من قبل العميل.

رائع، الآن فهمنا كيف يمكننا القيام بذلك على مستوى عالٍ، دعونا نجرب هذا في التمرين أدناه.

## تمرين: إنشاء عميل مع LLM

في هذا التمرين، سنتعلم كيف نضيف LLM إلى عميلنا.

### المصادقة باستخدام رمز الوصول الشخصي لـ GitHub

إنشاء رمز GitHub هو عملية مباشرة. إليك كيف يمكنك القيام بذلك:

- اذهب إلى إعدادات GitHub – انقر على صورة ملفك الشخصي في الركن الأيمن العلوي واختر الإعدادات.
- انتقل إلى إعدادات المطور – قم بالتمرير لأسفل وانقر على إعدادات المطور.
- اختر رموز الوصول الشخصية – انقر على رموز مقيدة الدقة ثم إنشاء رمز جديد.
- قم بتكوين رمزك – أضف ملاحظة للرجوع إليها، وحدد تاريخ انتهاء صلاحية، واختر الأذونات اللازمة. في هذه الحالة تأكد من إضافة إذن النماذج.
- أنشئ وانسخ الرمز – انقر على إنشاء رمز، وتأكد من نسخه على الفور، لأنك لن تتمكن من رؤيته مرة أخرى.

### -1- الاتصال بالخادم

لننشئ عميلنا أولاً:

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

في الكود السابق لقد:

- استوردنا المكتبات اللازمة
- أنشأنا صف يحتوي على عضوين، `client` و `openai` سيساعداننا على إدارة العميل والتفاعل مع LLM على التوالي.
- قامنا بضبط مثيل LLM لاستخدام نماذج GitHub عن طريق تعيين `baseUrl` للإشارة إلى واجهة برمجة التطبيقات الخاصة بالاستدلال.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# إنشاء معلمات الخادم لاتصال stdio
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

في الكود السابق لقد:

- استوردنا المكتبات اللازمة لـ MCP
- أنشأنا عميلًا

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

أولاً، تحتاج إلى إضافة التبعيات الخاصة بـ LangChain4j إلى ملف `pom.xml` الخاص بك. أضف هذه التبعيات لتمكين تكامل MCP ودعم نماذج GitHub:

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

ثم أنشئ صف عميل Java الخاص بك:

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
    
    public static void main(String[] args) throws Exception {        // تكوين نموذج اللغة الكبير لاستخدام نماذج GitHub
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

في الكود السابق لقد:

- **أضفنا تبعيات LangChain4j**: المطلوبة لتكامل MCP، العميل الرسمي لـ OpenAI، ودعم نماذج GitHub
- **استوردنا مكتبات LangChain4j**: لتكامل MCP ووظائف نموذج المحادثة OpenAI
- **أنشأنا `ChatLanguageModel`**: مهيأ لاستخدام نماذج GitHub مع رمز GitHub الخاص بك
- **أعددنا النقل عبر HTTP**: باستخدام أحداث الخادم المرسلة (SSE) للاتصال بخادم MCP
- **أنشأنا عميل MCP**: الذي سيتولى التعامل مع الاتصال بالخادم
- **استخدمنا دعم MCP المدمج في LangChain4j**: الذي يبسط التكامل بين LLM وخوادم MCP

#### Rust

يفترض هذا المثال أن لديك خادم MCP قائم على Rust قيد التشغيل. إذا لم يكن لديك واحد، ارجع إلى درس [01-first-server](../01-first-server/README.md) لإنشاء الخادم.

بمجرد أن يكون لديك خادم MCP Rust الخاص بك، افتح طرفية وانتقل إلى نفس مجلد الخادم. ثم نفذ الأمر التالي لإنشاء مشروع عميل LLM جديد:

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
> لا توجد مكتبة Rust رسمية لـ OpenAI، ومع ذلك فإن مكتبة `async-openai` هي [مكتبة تديرها المجتمع](https://platform.openai.com/docs/libraries/rust#rust) وتُستخدم شائعًا.

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

    // مهمة: الحصول على قائمة أدوات MCP

    // مهمة: محادثة LLM مع استدعاءات الأدوات

    Ok(())
}
```

هذا الكود يضبط تطبيق Rust أساسي سيتصل بخادم MCP ونماذج GitHub للتفاعل مع LLM.

> [!IMPORTANT]
> تأكد من تعيين متغير البيئة `OPENAI_API_KEY` برمز GitHub الخاص بك قبل تشغيل التطبيق.

رائع، للخطوة التالية، دعونا نسرد القدرات على الخادم.

### -2- سرد قدرات الخادم

الآن سنقوم بالاتصال بالخادم وطلب قدراته:

#### Typescript

في نفس الصف، أضف الطرق التالية:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // عرض الأدوات
    const toolsResult = await this.client.listTools();
}
```

في الكود السابق لقد:

- أضفنا كودًا للاتصال بالخادم، `connectToServer`.
- أنشأنا طريقة `run` مسؤولة عن إدارة تدفق تطبيقنا. حتى الآن تقوم فقط بسرد الأدوات ولكن سنضيف المزيد قريبًا.

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

- سرد الموارد والأدوات وطباعتها. بالنسبة للأدوات قمنا أيضًا بسرد `inputSchema` الذي سنستخدمه لاحقًا.

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

في الكود السابق لقد:

- سرد الأدوات المتاحة على خادم MCP
- لكل أداة، سرد الاسم والوصف ومخططها. هذا الأخير شيء سنستخدمه لاستدعاء الأدوات قريبًا.

#### Java

```java
// إنشاء مزود أدوات يكتشف أدوات MCP تلقائيًا
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// يقوم مزود أدوات MCP تلقائيًا بالتعامل مع:
// - سرد الأدوات المتاحة من خادم MCP
// - تحويل مخططات أدوات MCP إلى تنسيق LangChain4j
// - إدارة تنفيذ الأدوات والردود
```

في الكود السابق لقد:

- أنشأنا `McpToolProvider` الذي يكتشف ويسجل تلقائيًا كل الأدوات من خادم MCP
- مزود الأدوات يتولى التحويل بين مخططات أدوات MCP وصيغة أدوات LangChain4j داخليًا
- هذا النهج يلغي الحاجة لقائمة الأدوات والتحويل اليدوي

#### Rust

استرداد الأدوات من خادم MCP يتم باستخدام الطريقة `list_tools`. في دالة `main` الخاصة بك، بعد إعداد عميل MCP، أضف الكود التالي:

```rust
// الحصول على قائمة أدوات MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- تحويل قدرات الخادم إلى أدوات لفهم LLM

الخطوة التالية بعد سرد قدرات الخادم هي تحويلها إلى صيغة يفهمها LLM. وما إن نفعل ذلك، يمكننا تقديم هذه القدرات كأدوات لـ LLM.

#### TypeScript

1. أضف الكود التالي لتحويل استجابة من خادم MCP إلى صيغة أداة يمكن لـ LLM استخدامها:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // إنشاء مخطط زود بناءً على input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // تعيين النوع بشكل صريح إلى "function"
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

    الكود أعلاه يأخذ استجابة من خادم MCP ويحوله إلى صيغة تعريف أداة يفهمها LLM.

1. لنُحدث طريقة `run` لاحقًا لسرد قدرات الخادم:

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

    في الكود السابق، قمنا بتحديث طريقة `run` لتخريج النتيجة ولكل عنصر استدعاء `openAiToolAdapter`.

#### Python

1. أولاً، لنُنشئ دالة التحويل التالية

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

    في الدالة أعلاه `convert_to_llm_tools` نأخذ استجابة أداة MCP ونحولها إلى صيغة يمكن لـ LLM فهمها.

1. بعد ذلك، لنُحدث كود العميل للاستفادة من هذه الدالة كما يلي:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    هنا، نضيف استدعاء إلى `convert_to_llm_tool` لتحويل استجابة أداة MCP إلى شيء يمكننا تغذيته لاحقًا إلى LLM.

#### .NET

1. لنُضف كودًا لتحويل استجابة أداة MCP إلى شيء يمكن لـ LLM فهمه

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

في الكود السابق لقد:

- أنشأنا دالة `ConvertFrom` التي تأخذ الاسم، والوصف، ومخطط الإدخال.
- عرّفنا وظيفة تُنشئ `FunctionDefinition` يتم تمريرها إلى `ChatCompletionsDefinition`. هذا الأخير هو شيء يفهمه LLM.

1. لنر كيف يمكن تحديث بعض الكود الحالي للاستفادة من الدالة أعلاه:

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
// إنشاء واجهة بوت للتفاعل باللغة الطبيعية
public interface Bot {
    String chat(String prompt);
}

// تهيئة خدمة الذكاء الاصطناعي باستخدام أدوات LLM وMCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

في الكود السابق لقد:

- عرفنا واجهة بسيطة `Bot` للتفاعل باستخدام اللغة الطبيعية
- استخدمنا `AiServices` من LangChain4j لربط LLM تلقائيًا مع مزود أدوات MCP
- الإطار يدير تلقائيًا تحويل مخطط الأدوات واستدعاء الوظائف خلف الكواليس
- هذا النهج يلغي التحويل اليدوي للأدوات - حيث يتولى LangChain4j تعقيد تحويل أدوات MCP إلى صيغة متوافقة مع LLM

#### Rust

لتحويل استجابة أداة MCP إلى صيغة يمكن لـ LLM فهمها، سنضيف دالة مساعدة تُنسق قائمة الأدوات. أضف الكود التالي إلى ملف `main.rs` تحت دالة `main`. ستُستدعى هذه عند إجراء الطلبات إلى LLM:

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

رائع، نحن الآن مستعدون للتعامل مع أي طلب من المستخدم، فلنتعامل مع ذلك بعد قليل.

### -4- التعامل مع طلب محرض المستخدم

في هذا الجزء من الكود، سنتعامل مع طلبات المستخدم.

#### TypeScript

1. أضف دالة ستُستخدم لاستدعاء LLM لدينا:

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

        // ٣. القيام بشيء ما مع النتيجة
        // يجب القيام بذلك

        }
    }
    ```

    في الكود السابق نحن:

    - أضفنا دالة `callTools`.
    - الدالة تأخذ استجابة LLM وتتحقق مما إذا كانت هناك أدوات قد تم استدعاؤها، إن وجدت:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // استدعاء الأداة
        }
        ```

    - تستدعي أداة، إذا أشار LLM إلى وجوب استدعائها:

        ```typescript
        // ٢. استدعاء أداة الخادم
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ٣. قم بشيء ما مع النتيجة
        // يجب القيام به
        ```

1. حدّث طريقة `run` لتشمل استدعاءات إلى LLM واستدعاء `callTools`:

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

    // 3. مراجعة استجابة LLM، لكل خيار، تحقق مما إذا كان يحتوي على استدعاءات أدوات
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

رائع، لنستعرض الكود بالكامل:

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
            baseURL: "https://models.inference.ai.azure.com", // قد تحتاج لتغيير هذا العنوان في المستقبل: https://models.github.ai/inference
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
            type: "function" as const, // تعيين النوع بشكل صريح إلى "دالة"
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
    
          // 3. القيام بشيء ما بالنتيجة
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
    
        // 1. مراجعة استجابة LLM، لكل خيار، التحقق إذا كان يحتوي على استدعاءات أدوات
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

1. دعونا نضيف بعض الاستيرادات اللازمة لاستدعاء LLM

    ```python
    # نموذج تعلم آلي كبير
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. بعد ذلك، أضف الدالة التي ستستدعي LLM:

    ```python
    # نموذج اللغة الكبير

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

    في الكود السابق لقد:

    - مرّرنا الدوال التي وجدناها على خادم MCP وحولناها إلى LLM.
    - ثم استدعينا LLM مع تلك الدوال.
    - بعد ذلك، نقوم بفحص النتيجة لنرى الدوال التي يجب استدعاؤها، إن وجدت.
    - أخيرًا، نمرر مصفوفة الدوال التي يجب استدعاؤها.

1. الخطوة النهائية، لنُحدّث الكود الرئيسي:

    ```python
    prompt = "Add 2 to 20"

    # اسأل النموذج اللغوي الكبير عن الأدوات التي يجب استخدامها، إن وُجدت
    functions_to_call = call_llm(prompt, functions)

    # استدعِ الوظائف المقترحة
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    هذا هو الخطوة النهائية، في الكود أعلاه نحن:

    - نستدعي أداة MCP عبر `call_tool` باستخدام الدالة التي حسب LLM وجب استدعاؤها بناءً على المحرض.
    - نطبع نتيجة استدعاء الأداة إلى خادم MCP.

#### .NET

1. لنُظهر بعض الكود لطلب محرض LLM:

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

    في الكود السابق لقد:

    - جلبنا الأدوات من خادم MCP، `var tools = await GetMcpTools()`.
    - عرفنا محرض المستخدم `userMessage`.
    - أنشأنا كائن خيارات يحدد النموذج والأدوات.
    - أجرينا طلبًا نحو LLM.

1. خطوة أخيرة، لنر إذا كان LLM يظن أننا يجب أن نستدعي دالة:

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

    في الكود السابق لقد:

    - تم التكرار عبر قائمة استدعاءات الوظائف.
    - لكل استدعاء أداة، نقوم بتحليل الاسم والوسائط ونستدعي الأداة على خادم MCP باستخدام عميل MCP. وأخيرًا نطبع النتائج.

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

في الكود السابق لقد:

- استخدمنا محرضات بسيطة بلغة طبيعية للتفاعل مع أدوات خادم MCP
- إطار LangChain4j يدير تلقائيًا:
  - تحويل محرضات المستخدم إلى استدعاءات أدوات عند الحاجة
  - استدعاء أدوات MCP المناسبة بناءً على قرار LLM
  - إدارة تدفق المحادثة بين LLM وخادم MCP
- تعيد طريقة `bot.chat()` ردودًا بلغة طبيعية قد تشمل نتائج تنفيذ أدوات MCP
- هذا النهج يوفر تجربة مستخدم سلسة حيث لا يحتاج المستخدمون لمعرفة التفاصيل التقنية لخادم MCP

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

هنا يحدث الجزء الأكبر من العمل. سنستدعي LLM مع المحرض الأولي للمستخدم، ثم نعالج الاستجابة لنرى إن كان هناك حاجة لاستدعاء أية أدوات. إذا كان الأمر كذلك، سنستدعي تلك الأدوات ونستمر في الحوار مع LLM حتى لا تحتاج المزيد من الاستدعاءات ولديك استجابة نهائية.

سنقوم بإجراء عدة استدعاءات إلى LLM، لذا دعنا نعرّف دالة ستتعامل مع استدعاء LLM. أضف الدالة التالية إلى ملف `main.rs` الخاص بك:

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

تأخذ هذه الدالة عميل LLM، قائمة من الرسائل (بما في ذلك محرض المستخدم)، أدوات من خادم MCP، وترسل طلبًا إلى LLM، عائدة الاستجابة.
يحتوي الرد من نموذج اللغة الكبير (LLM) على مصفوفة من `choices`. سنحتاج إلى معالجة النتيجة لمعرفة ما إذا كانت هناك أي `tool_calls` موجودة. هذا يخبرنا بأن نموذج اللغة الكبير يطلب استدعاء أداة معينة مع المعطيات. أضف الكود التالي إلى أسفل ملف `main.rs` لتحديد دالة لمعالجة رد نموذج اللغة الكبير:

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

    // طباعة المحتوى إذا كان متاحًا
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // معالجة استدعاءات الأدوات
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

        // متابعة المحادثة مع نتائج الأداة
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
  
إذا كانت هناك `tool_calls` موجودة، فإنه يستخرج معلومات الأداة، يستدعي خادم MCP مع طلب الأداة، ويضيف النتائج إلى رسائل المحادثة. ثم يواصل المحادثة مع نموذج اللغة الكبير ويتم تحديث الرسائل برد المساعد ونتائج استدعاء الأداة.

لاستخراج معلومات استدعاء الأداة التي يعيدها نموذج اللغة الكبير لاستدعاءات MCP، سنضيف دالة مساعدة أخرى لاستخراج كل ما يلزم للقيام بالاستدعاء. أضف الكود التالي إلى أسفل ملف `main.rs`:

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
  
مع توفر كل الأجزاء اللازمة، يمكننا الآن معالجة موجه المستخدم الأولي واستدعاء نموذج اللغة الكبير. حدّث دالة `main` لتشمل الكود التالي:

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
  
هذا سيستعلم نموذج اللغة الكبير باستخدام موجه المستخدم الأولي طالبًا مجموع رقمين، وسيعالج الرد للتعامل ديناميكيًا مع استدعاءات الأدوات.

رائع، لقد فعلتها!

## المهمة

خذ الكود من التمرين وطور الخادم مع بعض الأدوات الإضافية. ثم أنشئ عميلًا مع نموذج لغة كبير، كما في التمرين، وجربه مع مطالبات مختلفة للتأكد من استدعاء جميع أدوات الخادم ديناميكيًا. هذه الطريقة في بناء العميل تعني أن المستخدم النهائي سيحصل على تجربة مستخدم رائعة إذ يستطيع استخدام المطالبات بدلاً من أوامر العميل المحددة وسيكون غير مدرك لأي استدعاء لخادم MCP.

## الحل

[الحل](./solution/README.md)

## النقاط الأساسية

- إضافة نموذج لغة كبير إلى عميلك يوفر طريقة أفضل للمستخدمين للتفاعل مع خوادم MCP.  
- تحتاج إلى تحويل رد خادم MCP إلى شيء يمكن لنموذج اللغة الكبير فهمه.

## عينات

- [حاسبة جافا](../samples/java/calculator/README.md)  
- [حاسبة .Net](../../../../03-GettingStarted/samples/csharp)  
- [حاسبة جافا سكريبت](../samples/javascript/README.md)  
- [حاسبة تايب سكريبت](../samples/typescript/README.md)  
- [حاسبة بايثون](../../../../03-GettingStarted/samples/python)  
- [حاسبة راست](../../../../03-GettingStarted/samples/rust)

## موارد إضافية

## التالي

- التالي: [استهلاك خادم باستخدام Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. بالنسبة للمعلومات الحساسة، يُنصح بالترجمة الاحترافية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->