# إنشاء عميل مع LLM

حتى الآن، رأيت كيف تنشئ خادمًا وعميلًا. تمكن العميل من الاتصال بالخادم بشكل صريح لعرض أدواته وموارده واستفساراته. مع ذلك، هذه ليست طريقة عملية جدًا. يعيش مستخدموك في عصر الوكلاء ويتوقعون استخدام الاستفسارات والتواصل مع نموذج لغوي ضخم بدلاً من ذلك. لا يهمهم ما إذا كنت تستخدم MCP لتخزين إمكانياتك؛ فهم ببساطة يتوقعون التفاعل باستخدام اللغة الطبيعية. فكيف نحل هذه المشكلة؟ الحل هو إضافة نموذج لغوي ضخم إلى العميل.

## نظرة عامة

في هذا الدرس نركز على إضافة نموذج لغوي ضخم ليعمل مع عميلك ونوضح كيف يوفر هذا تجربة أفضل بكثير لمستخدمك.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- إنشاء عميل مع نموذج لغوي ضخم.
- التفاعل بسلاسة مع خادم MCP باستخدام نموذج لغوي ضخم.
- تقديم تجربة مستخدم أفضل على جانب العميل.

## النهج

لنحاول فهم النهج الذي نحتاج إلى اتخاذه. إضافة نموذج لغوي ضخم تبدو بسيطة، لكن هل سنفعل ذلك فعليًا؟

إليك كيف سيتفاعل العميل مع الخادم:

1. إقامة اتصال مع الخادم.

1. عرض الإمكانيات، الاستفسارات، الموارد والأدوات، وحفظ مخططها.

1. إضافة نموذج لغوي ضخم وتمرير الإمكانيات المحفوظة ومخططها بصيغة يفهمها النموذج.

1. التعامل مع استفسار المستخدم بتمريره إلى النموذج مع الأدوات التي قدّمها العميل.

عظيم، الآن نفهم كيف يمكن أن نفعل هذا على مستوى عالي، لنجرّب ذلك في التمرين أدناه.

## تمرين: إنشاء عميل مع نموذج لغوي ضخم

في هذا التمرين، سنتعلم كيف نضيف نموذج لغوي ضخم لعميلنا.

### المصادقة باستخدام رمز الوصول الشخصي لـ GitHub

إنشاء رمز GitHub هو عملية بسيطة. إليك كيف يمكنك القيام بها:

- اذهب إلى إعدادات GitHub – انقر على صورة ملفك الشخصي في الزاوية العليا اليمنى واختر الإعدادات.
- انتقل إلى إعدادات المطور – قم بالتمرير لأسفل وانقر على إعدادات المطور.
- اختر رموز الوصول الشخصية – انقر على الرموز الدقيقة التحديد ثم إنشاء رمز جديد.
- قم بتكوين رمزك – أضف ملاحظة للرجوع إليها، وضع تاريخ انتهاء الصلاحية، وحدد الأذونات الضرورية. في هذه الحالة تأكد من إضافة إذن النماذج.
- أنشئ وانسخ الرمز – انقر على إنشاء الرمز، وتأكد من نسخه فورًا، لأنه لن يكون بإمكانك رؤيته مرة أخرى.

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

في الكود السابق قمنا بـ:

- استيراد المكتبات اللازمة
- إنشاء فئة تحتوي على عضوين، `client` و `openai` لمساعدتنا في إدارة العميل والتفاعل مع نموذج لغوي ضخم على التوالي.
- تهيئة مثيل النموذج اللغوي لاستخدام نماذج GitHub بتعيين `baseUrl` للإشارة إلى واجهة برمجة التطبيقات الخاصة بالاستدلال.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# إنشاء معلمات الخادم لاتصال stdio
server_params = StdioServerParameters(
    command="mcp",  # الملف التنفيذي
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

أولًا، ستحتاج إلى إضافة تبعيات LangChain4j إلى ملف `pom.xml` الخاص بك. أضف هذه التبعيات لتمكين تكامل MCP وواجهة برمجة التطبيقات MiniMax المتوافقة مع OpenAI:

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

اضبط مفتاح واجهة برمجة تطبيقات MiniMax الخاص بك، وبشكل اختياري، نقطة النهاية والنموذج.
يدعم `MINIMAX_MODEL_ID` النموذجين `MiniMax-M3` و `MiniMax-M2.7`. إذا
لم يُضبط `OPENAI_BASE_URL`، يدعم `MINIMAX_REGION` المناطق `global_en` و `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

لاختيار نقطة النهاية بحسب المنطقة بدلاً من ذلك، تجاهل `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
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

في الكود السابق قمنا بـ:

- **إضافة تبعيات LangChain4j**: اللازمة لتكامل MCP وواجهة برمجة التطبيقات MiniMax المتوافقة مع OpenAI
- **استيراد مكتبات LangChain4j**: لتكامل MCP ووظائف موديل المحادثة OpenAI
- **إنشاء نموذج لغة محادثة `ChatLanguageModel`**: مُهيأ لاستخدام MiniMax مع مفتاح API الخاص بك، نقطة النهاية، ومعرف النموذج المدعوم
- **إعداد نقل HTTP**: باستخدام Server-Sent Events (SSE) للاتصال بخادم MCP
- **إنشاء عميل MCP**: للتواصل مع الخادم
- **استخدام دعم MCP المدمج في LangChain4j**: الذي يبسط التكامل بين النماذج اللغوية وخوادم MCP

#### Rust

يفترض هذا المثال أنك تمتلك خادم MCP مبني بلغة Rust يعمل. إن لم يكن لديك، راجع درس [01-first-server](../01-first-server/README.md) لإنشاء الخادم.

بمجرد أن تملك خادم MCP بلغة Rust، افتح الطرفية وانتقل إلى نفس مسار الخادم. ثم نفذ الأمر التالي لإنشاء مشروع عميل نموذج لغوي ضخم جديد:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

أضف التبعيات التالية إلى ملف `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> لا توجد مكتبة رسمية لـ OpenAI بلغة Rust، لكن `async-openai` هي مكتبة يديرها المجتمع تستخدم بشكل شائع.

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
    // رسالة أولية
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

    // TODO: الحصول على قائمة أدوات MCP

    // TODO: محادثة LLM مع استدعاءات الأدوات

    Ok(())
}
```

هذا الكود ينشئ تطبيق Rust أساسي سيتصل بخادم MCP ونماذج GitHub للتفاعل مع النموذج اللغوي.

> [!IMPORTANT]
> تأكد من تعيين متغير البيئة `OPENAI_API_KEY` برمز GitHub الخاص بك قبل تشغيل التطبيق.

عظيم، للخطوة التالية، لنلق نظرة على عرض الإمكانيات على الخادم.

### -2- عرض إمكانيات الخادم

الآن سنوصل الاتصال بالخادم ونسأل عن إمكانياته:

#### Typescript

أضف إلى نفس الفئة الطرق التالية:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // أدوات الإدراج
    const toolsResult = await this.client.listTools();
}
```

في الكود السابق قمنا بـ:

- إضافة كود للاتصال بالخادم، `connectToServer`.
- إنشاء طريقة `run` مسؤولة عن تدفق تطبيقنا. حتى الآن تكتفي بعرض الأدوات لكننا سنضيف المزيد قريبًا.

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

هذا ما أضفناه:

- عرض الموارد والأدوات وطبعها. بالنسبة للأدوات نعرض أيضًا `inputSchema` والذي نستخدمه لاحقًا.

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

- عرض الأدوات المتاحة على خادم MCP
- لكل أداة تم عرض الاسم والوصف ومخططها. الأخير هو ما سنستخدمه لاستدعاء الأدوات قريبًا.

#### Java

```java
// إنشاء موفر أدوات يكتشف أدوات MCP تلقائيًا
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// يتولى موفر أدوات MCP التعامل تلقائيًا مع:
// - سرد الأدوات المتاحة من خادم MCP
// - تحويل مخططات أدوات MCP إلى صيغة LangChain4j
// - إدارة تنفيذ الأدوات والردود
```

في الكود السابق قمنا بـ:

- إنشاء `McpToolProvider` يكتشف ويسجل جميع الأدوات من خادم MCP تلقائيًا
- مزود الأدوات يتعامل مع تحويل مخططات أدوات MCP إلى صيغة أدوات LangChain4j داخليًا
- هذا النهج يلغي الحاجة للقائمة اليدوية وتحويل الأدوات

#### Rust

استرجاع الأدوات من خادم MCP يتم باستخدام دالة `list_tools`. في دالة `main` الخاصة بك، بعد إعداد عميل MCP، أضف الكود التالي:

```rust
// الحصول على قائمة أدوات MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- تحويل إمكانيات الخادم إلى أدوات نموذج لغوي

الخطوة التالية بعد عرض إمكانيات الخادم هي تحويلها إلى صيغة يفهمها النموذج اللغوي. بعد ذلك يمكننا تقديم هذه الإمكانيات كأدوات لنموذجنا.

#### TypeScript

1. أضف الكود التالي لتحويل استجابة خادم MCP إلى صيغة أداة يمكن للنموذج استخدامها:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // إنشاء مخطط زود بناءً على input_schema
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

    ```

    الكود أعلاه يأخذ استجابة من خادم MCP ويحولها إلى تعريف أداة يفهمه النموذج اللغوي.

2. دعنا نحدث طريقة `run` بعد ذلك لعرض إمكانيات الخادم:

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

    في الكود السابق، قمنا بتحديث طريقة `run` لتوسيط النتيجة ولكل إدخال يتم استدعاء `openAiToolAdapter`.

#### Python

1. أولًا، لننشئ دالة تحويل كما يلي

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

    في الدالة أعلاه `convert_to_llm_tools` نأخذ استجابة أداة MCP ونحولها إلى صيغة يفهمها النموذج اللغوي.

2. بعد ذلك، لنحدث كود عميلنا للاستفادة من هذه الدالة كما يلي:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    هنا، نضيف استدعاء إلى `convert_to_llm_tool` لتحويل استجابة أداة MCP إلى صيغة يمكن تقديمها للنموذج لاحقًا.

#### .NET

1. دعنا نضيف كودًا لتحويل استجابة أداة MCP إلى صيغة يفهمها النموذج اللغوي

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

- إنشاء دالة `ConvertFrom` التي تأخذ الاسم، الوصف، ومخطط الإدخال.
- تعريف دالة تقوم بإنشاء تعريف الدالة `FunctionDefinition` الذي يُمرر إلى تعريف محادثة `ChatCompletionsDefinition`. الأخير صيغة يفهمها النموذج اللغوي.

2. لنرى كيف نحدث بعض الكود الحالي للاستفادة من الدالة أعلاه:

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

// تكوين خدمة الذكاء الاصطناعي باستخدام أدوات LLM و MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

في الكود السابق قمنا بـ:

- تعريف واجهة `Bot` بسيطة للتفاعل باستخدام اللغة الطبيعية
- استخدام `AiServices` من LangChain4j لربط النموذج اللغوي تلقائيًا مع مزود أدوات MCP
- الإطار يتعامل تلقائيًا مع تحويل المخطط الأداتي واستدعاء الوظائف خلف الكواليس
- هذا النهج يلغي الحاجة لتحويل الأدوات يدويًا - LangChain4j يتولى كل تعقيدات تحويل أدوات MCP إلى صيغة متوافقة مع النموذج اللغوي

#### Rust

لتحويل استجابة أداة MCP إلى صيغة يفهمها النموذج اللغوي، سنضيف دالة مساعدة تقوم بتنسيق قائمة الأدوات. أضف الكود التالي إلى ملف `main.rs` تحت دالة `main`. سيتم استدعاؤها عند تقديم طلبات للنموذج اللغوي:

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

عظيم، لقد أعددنا للتعامل مع أي طلبات من المستخدم، لننتقل لهذه الخطوة التالية.

### -4- التعامل مع طلب استفسار المستخدم

في هذا الجزء من الكود، سنتعامل مع طلبات المستخدم.

#### TypeScript

1. أضف طريقة ستُستخدم لاستدعاء النموذج اللغوي:

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
        // للقيام به

        }
    }
    ```

    في الكود السابق قمنا بـ:

    - إضافة الطريقة `callTools`.
    - الطريقة تأخذ استجابة نموذج لغوي وتتحقق من الأدوات التي يجب استدعاؤها إذا وُجدت:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // استدعاء الأداة
        }
        ```

    - استدعاء أداة إذا أشار النموذج اللغوي بوجوب استدعائها:

        ```typescript
        // ٢. استدعاء أداة الخادم
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ٣. القيام بشيء ما مع النتيجة
        // للقيام به
        ```

2. حدث طريقة `run` لتتضمن استدعاءات للنموذج اللغوي واستدعاء `callTools`:

    ```typescript

    // 1. إنشاء رسائل تعتبر مدخلاً لنموذج اللغة الكبير
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. استدعاء نموذج اللغة الكبير
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. مراجعة استجابة نموذج اللغة الكبير، لكل خيار، تحقق مما إذا كان يحتوي على استدعاءات أدوات
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

عظيم، لنستعرض الكود كاملًا:

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
    
          // 3. قم بعمل شيء بالنتيجة
          // يجب القيام به
    
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
    
        // 3. المرور على استجابة LLM، لكل اختيار، تحقق مما إذا كان يحتوي على استدعاءات أداة
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

1. دعنا نضيف بعض الاستيرادات اللازمة لاستدعاء النموذج اللغوي

    ```python
    # نموذج اللغة الكبير
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. بعد ذلك، لنضيف الدالة التي ستستدعي النموذج اللغوي:

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

    في الكود السابق قمنا بـ:

    - تمرير الوظائف التي وجدناها على خادم MCP وقمنا بتحويلها إلى النموذج اللغوي.
    - بعدها قمنا باستدعاء النموذج اللغوي بهذه الوظائف.
    - ثم نفحص النتيجة لنرى الوظائف التي ينبغي استدعاؤها إذا وُجدت.
    - أخيرًا، نمرر مصفوفة الوظائف التي يجب استدعاؤها.

3. الخطوة الأخيرة، لنحدث الكود الرئيسي لدينا:

    ```python
    prompt = "Add 2 to 20"

    # اسأل LLM عن الأدوات التي يجب استخدامها، إن وجدت
    functions_to_call = call_llm(prompt, functions)

    # استدعاء الوظائف المقترحة
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ها هي الخطوة النهائية، في الكود أعلاه نحن:

    - نستدعي أداة MCP عبر `call_tool` باستخدام دالة اعتقد النموذج اللغوي أننا بحاجة لاستدعائها بناءً على استفسارنا.
    - نطبع نتيجة استدعاء الأداة على خادم MCP.

#### .NET

1. دعنا نعرض بعض الكود لطلب استفسار من النموذج اللغوي:

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
    - تعريف استفسار المستخدم `userMessage`.
    - إنشاء كائن خيارات يحدد النموذج والأدوات.
    - تقديم طلب للنموذج اللغوي.

2. آخر خطوة، لنرى إذا اعتقد النموذج اللغوي أننا بحاجة لاستدعاء دالة:

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

    - اجتزنا قائمة استدعاءات الدوال.
    - لكل استدعاء أداة، حللنا الاسم والوسائط واستدعينا الأداة على خادم MCP باستخدام عميل MCP. وأخيرًا طبعنا النتائج.

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

// 6. Print the generic response
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

- استخدام استفسارات طبيعية بسيطة للتفاعل مع أدوات خادم MCP
- إطار LangChain4j يتولى تلقائيًا:
  - تحويل استفسارات المستخدم إلى استدعاءات أدوات عند اللزوم
  - استدعاء أدوات MCP المناسبة بناءً على قرار النموذج اللغوي
  - إدارة تدفق المحادثة بين النموذج اللغوي وخادم MCP
- طريقة `bot.chat()` تُرجع استجابات لغة طبيعية قد تتضمن نتائج تنفيذ أدوات MCP
- هذا النهج يقدم تجربة مستخدم سلسة حيث لا يحتاج المستخدمون لمعرفة تفاصيل تنفيذ MCP الأساسية

مثال الكود الكامل:

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

هنا يحدث معظم العمل. سنستدعي النموذج اللغوي بالاستفسار الأولي للمستخدم، ثم نعالج الاستجابة لنرى إن كان ينبغي استدعاء أدوات. إذا كان الأمر كذلك، سنستدعي هذه الأدوات ونستمر بالمحادثة مع النموذج حتى لا تبقى استدعاءات أدوات أخرى ويصل لدينا رد نهائي.


سنقوم بإجراء عدة مكالمات إلى LLM، لذلك دعنا نعرّف دالة ستتولى استدعاء LLM. أضف الدالة التالية إلى ملف `main.rs` الخاص بك:

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

تأخذ هذه الدالة عميل LLM، قائمة من الرسائل (بما في ذلك مطالبة المستخدم)، الأدوات من خادم MCP، وترسل طلبًا إلى LLM، ثم تُعيد الاستجابة.

ستحتوي الاستجابة من LLM على مصفوفة من `choices`. سنحتاج لمعالجة النتيجة لنرى ما إذا كانت هناك أي `tool_calls` موجودة. هذا يُعلِمنا أن LLM يطلب استدعاء أداة معينة مع الوسائط. أضف الكود التالي إلى أسفل ملف `main.rs` لتعريف دالة لمعالجة استجابة LLM:

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

        // متابعة المحادثة باستخدام نتائج الأداة
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

إذا كانت هناك `tool_calls`، فإنها تستخرج معلومات الأداة، وتستدعي خادم MCP مع طلب الأداة، وتضيف النتائج إلى رسائل المحادثة. ثم تتابع المحادثة مع LLM وتُحدَّث الرسائل باستجابة المساعد ونتائج استدعاء الأداة.

لاستخراج معلومات استدعاء الأداة التي يُعيدها LLM لمكالمات MCP، سنضيف دالة مساعدة أخرى لاستخراج كل ما يلزم لإجراء المكالمة. أضف الكود التالي إلى أسفل ملف `main.rs` الخاص بك:

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

مع وجود كل الأجزاء في مكانها، يمكننا الآن معالجة مطالبة المستخدم الأولية واستدعاء LLM. حدّث دالة `main` الخاصة بك لتشمل الكود التالي:

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

هذا سيستعلم LLM بمطالبة المستخدم الأولية لطلب مجموع رقمين، وسيعالج الاستجابة للتعامل ديناميكيًا مع استدعاءات الأدوات.

رائع، لقد فعلتها!

## الواجب

خذ الكود من التمرين ووسع الخادم ببعض الأدوات الإضافية. ثم أنشئ عميلًا مع LLM، كما في التمرين، واختبره بمطالبات مختلفة لتتأكد من أن جميع أدوات الخادم الخاصة بك تُستدعى ديناميكيًا. هذه الطريقة في بناء العميل تعني أن المستخدم النهائي سيحصل على تجربة مستخدم رائعة حيث يمكنه استخدام المطالبات بدلاً من الأوامر الدقيقة للعميل، ويكون غير مدرك لأي استدعاء لخادم MCP.

## الحل

[الحل](./solution/README.md)

## نقاط رئيسية

- إضافة LLM إلى عميلك يوفر طريقة أفضل للمستخدمين للتفاعل مع خوادم MCP.
- تحتاج إلى تحويل استجابة خادم MCP إلى شيء يمكن لـ LLM فهمه.

## عينات

- [حاسبة جافا](../samples/java/calculator/README.md)
- [حاسبة .Net](../../../../03-GettingStarted/samples/csharp)
- [حاسبة جافا سكريبت](../samples/javascript/README.md)
- [حاسبة تايب سكريبت](../samples/typescript/README.md)
- [حاسبة بايثون](../../../../03-GettingStarted/samples/python)
- [حاسبة رست](../../../../03-GettingStarted/samples/rust)

## موارد إضافية

## التالي

- التالي: [استهلاك خادم باستخدام Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->