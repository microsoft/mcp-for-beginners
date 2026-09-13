# إنشاء عميل مع LLM

> [!NOTE]
> أمثلة العملاء في جافا تتصل عبر بروتوكول HTTP+SSE القديم وتستهدف MCP `2025-11-25` واجهات برمجة التطبيقات الخاصة بـ SDK. استخدم SDK متوافق مع `2026-07-28` و HTTP قابل للبث للعملاء البعيدين الجدد.
> 
> 



## نظرة عامة

في هذا الدرس نركز على إضافة LLM لعملائك ونوضح كيف يقدم ذلك تجربة أفضل بكثير للمستخدم الخاص بك.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- إنشاء عميل مع LLM.
- التفاعل بسلاسة مع خادم MCP باستخدام LLM.
- تقديم تجربة مستخدم أفضل على جانب العميل.

## النهج

دعونا نحاول فهم النهج الذي نحتاج لاتخاذه. يبدو إضافة LLM بسيطًا، لكن هل سنفعل ذلك حقًا؟

هذه هي الطريقة التي سيتفاعل بها العميل مع الخادم:

1. إقامة اتصال مع الخادم.

1. سرد الإمكانيات، المطالبات، الموارد والأدوات، وحفظ مخططها.

1. إضافة LLM وتمرير الإمكانيات المحفوظة ومخططها بصيغة يفهمها LLM.

1. معالجة طلب المستخدم بتمريره إلى LLM مع الأدوات المدرجة بواسطة العميل.

عظيم، الآن نفهم كيف يمكننا القيام بذلك على مستوى عال، دعنا نجرب ذلك في التمرين أدناه.

## تمرين: إنشاء عميل مع LLM

في هذا التمرين، سنتعلم كيفية إضافة LLM إلى عميلنا.

### المصادقة باستخدام رمز وصول شخصي من GitHub

إنشاء رمز GitHub عملية بسيطة. إليك كيف يمكنك القيام بذلك:

- انتقل إلى إعدادات GitHub – انقر على صورة ملفك الشخصي في الزاوية اليمنى العليا واختر الإعدادات.
- توجه إلى إعدادات المطور – قم بالتمرير لأسفل وانقر على إعدادات المطور.
- اختر رموز الوصول الشخصي – انقر على الرموز الدقيقة الصلاحية ثم توليد رمز جديد.
- قم بتكوين رمزك – أضف ملاحظة للرجوع إليها، حدد تاريخ انتهاء الصلاحية، واختر الصلاحيات اللازمة (الأذونات). في هذه الحالة، تأكد من إضافة إذن النماذج.
- توليد ونسخ الرمز – أنقر على توليد الرمز، وتأكد من نسخه فورًا، لأنه لن يمكنك رؤيته مرة أخرى.

### -1- الاتصال بالخادم

دعنا ننشئ عميلنا أولاً:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // استورد zod للتحقق من صحة المخطط

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
- إنشاء فئة تحتوي على عضوين، `client` و `openai` اللذين سيساعدانا في إدارة العميل والتفاعل مع LLM على التوالي.
- تكوين مثيل LLM لدينا لاستخدام نماذج GitHub عبر تعيين `baseUrl` إلى واجهة API للاستنتاج.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# إنشاء معلمات الخادم لاتصال stdio
server_params = StdioServerParameters(
    command="mcp",  # قابل للتنفيذ
    args=["run", "server.py"],  # وسيطات اختيارية لسطر الأوامر
    env=None,  # متغيرات بيئية اختيارية
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

- استيراد مكتبات MCP اللازمة
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

أولاً، ستحتاج إلى إضافة تبعيات LangChain4j إلى ملف `pom.xml` الخاص بك. أضف هذه التبعيات لتمكين تكامل MCP وواجهة MiniMax المتوافقة مع OpenAI:

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

قم بتعيين مفتاح API الخاص بـ MiniMax الخاص بك، واختيارياً نقطة النهاية والنموذج.
يدعم `MINIMAX_MODEL_ID` النماذج `MiniMax-M3` و `MiniMax-M2.7`. إذا
لم يتم تعيين `OPENAI_BASE_URL`، يدعم `MINIMAX_REGION` القيم `global_en` و `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

لاختيار نقطة النهاية حسب المنطقة، قم بحذف `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

ثم أنشئ فئة عميل جافا الخاصة بك:

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

        // إنشاء وسيلة نقل MCP للاتصال بالخادم
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

- **أضفنا تبعيات LangChain4j**: مطلوبة لتكامل MCP وواجهة MiniMax المتوافقة مع OpenAI
- **استوردنا مكتبات LangChain4j**: لتكامل MCP ووظائف نموذج دردشة OpenAI
- **أنشأنا `ChatLanguageModel`**: تم تكوينها لاستخدام MiniMax مع مفتاح API الخاص بك، نقطة النهاية، ومعرف النموذج المدعوم
- **أعددنا النقل عبر HTTP**: باستخدام أحداث الخادم المرسلة (SSE) للاتصال بخادم MCP
- **أنشأنا عميل MCP**: الذي سيتولى إدارة الاتصال مع الخادم
- **استخدمنا دعم MCP المدمج في LangChain4j**: لتسهيل التكامل بين LLM وخوادم MCP

#### Rust

يفترض هذا المثال أن لديك خادم MCP مبني على Rust يعمل. إذا لم يكن لديك واحد، ارجع إلى درس [01-first-server](../01-first-server/README.md) لإنشاء الخادم.

بمجرد وجود خادم MCP الخاص بك، افتح الطرفية وانتقل إلى نفس الدليل الذي يحتوي على الخادم. ثم شغل الأمر التالي لإنشاء مشروع عميل LLM جديد:

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
> لا توجد مكتبة Rust رسمية لـ OpenAI، ومع ذلك، مكتبة `async-openai` هي [مكتبة تتم صيانتها من قبل المجتمع](https://platform.openai.com/docs/libraries/rust#rust) وتستخدم بشكل شائع.

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
    // الرسالة الأولى
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

هذا الكود ينشئ تطبيق Rust أساسي يتصل بخادم MCP ونماذج GitHub للتفاعل مع LLM.

> [!IMPORTANT]
> تأكد من تعيين متغير البيئة `OPENAI_API_KEY` برمز GitHub الخاص بك قبل تشغيل التطبيق.

عظيم، للخطوة التالية، دعنا ندرج الإمكانيات على الخادم.

### -2- سرد إمكانيات الخادم

الآن سنقوم بالاتصال بالخادم وطلب إمكانياته:

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

    // قائمة الأدوات
    const toolsResult = await this.client.listTools();
}
```

في الكود السابق قمنا بـ:

- أضفنا رمز للاتصال بالخادم، `connectToServer`.
- أنشأنا طريقة `run` المسؤولة عن إدارة تدفق التطبيق. حتى الآن تقوم فقط بسرد الأدوات لكننا سنضيف المزيد لها قريباً.

#### Python

```python
# قائمة الموارد المتاحة
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# قائمة الأدوات المتاحة
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

هذا ما أضفناه:

- سرد الموارد والأدوات وطباعتها. بالنسبة للأدوات أيضا قمنا بسرد `inputSchema` الذي سنستخدمه لاحقًا.

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


في الكود السابق لقد قمنا بـ:

- سرد الأدوات المتاحة على خادم MCP
- لكل أداة، سرد الاسم والوصف ومخططها. الأخير هو شيء سنستخدمه لاستدعاء الأدوات قريبًا.

#### جافا

```java
// إنشاء موفر أدوات يكتشف أدوات MCP تلقائيًا
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// موفر أدوات MCP يتعامل تلقائيًا مع:
// - سرد الأدوات المتاحة من خادم MCP
// - تحويل مخططات أدوات MCP إلى صيغة LangChain4j
// - إدارة تنفيذ الأدوات والاستجابات
```

في الكود السابق لقد قمنا بـ:

- إنشاء `McpToolProvider` الذي يكتشف ويسجل تلقائيًا جميع الأدوات من خادم MCP
- مزود الأداة يتولى التحويل بين مخططات أدوات MCP وتنسيق أدوات LangChain4j داخليًا
- هذا النهج يلغي الحاجة لسرد الأدوات يدويًا وعملية التحويل

#### راست

جلب الأدوات من خادم MCP يتم باستخدام طريقة `list_tools`. في دالة `main` الخاصة بك، بعد إعداد عميل MCP، أضف الكود التالي:

```rust
// احصل على قائمة أدوات MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- تحويل قدرات الخادم إلى أدوات LLM

الخطوة التالية بعد سرد قدرات الخادم هي تحويلها إلى صيغة يفهمها LLM. بمجرد القيام بذلك، يمكننا توفير هذه القدرات كأدوات ل LLM.

#### تايب سكريبت

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
            type: "function" as const, // تعيين النوع صراحةً إلى "دالة"
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

    الكود أعلاه يأخذ استجابة من خادم MCP ويحولها إلى صيغة تعريف أداة يفهمها LLM.

2. لنقم بتحديث دالة `run` التالية لسرد قدرات الخادم:

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

    في الكود السابق، قمنا بتحديث دالة `run` لترسم من خلال النتيجة ولكل مدخل استدعاء `openAiToolAdapter`.

#### بايثون

1. أولاً، لننشئ دالة محول التالية

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

    في الدالة أعلاه `convert_to_llm_tools` نأخذ استجابة أداة MCP ونحولها إلى شكل يمكن لـ LLM فهمه.

2. بعد ذلك، لنقم بتحديث كود عميلنا للاستفادة من هذه الدالة كما يلي:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    هنا، نضيف استدعاء لـ `convert_to_llm_tool` لتحويل استجابة أداة MCP إلى شيء يمكننا تقديمه ل LLM لاحقًا.

#### .NET

1. لنضيف كود لتحويل استجابة أداة MCP إلى شيء يمكن لـ LLM فهمه

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

في الكود السابق لقد قمنا بـ:

- إنشاء دالة `ConvertFrom` التي تأخذ الاسم والوصف ومخطط الإدخال.
- تعريف وظيفة تنشئ FunctionDefinition يتم تمريرها إلى ChatCompletionsDefinition. الأخير هو شيء يمكن لـ LLM فهمه.

2. دعونا نرى كيف يمكننا تحديث بعض الكود الموجود للاستفادة من هذه الدالة أعلاه:

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

#### جافا

```java
// إنشاء واجهة بوت للتفاعل مع اللغة الطبيعية
public interface Bot {
    String chat(String prompt);
}

// تكوين خدمة الذكاء الاصطناعي باستخدام أدوات LLM و MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

في الكود السابق لقد قمنا بـ:

- تعريف واجهة بسيطة `Bot` للتفاعل باللغة الطبيعية
- استخدام LangChain4j's `AiServices` لربط LLM تلقائيًا مع مزود أدوات MCP
- الإطار يدير تلقائيًا تحويل مخطط الأداة واستدعاء الوظيفة في الخلفية
- هذا النهج يلغي الحاجة لتحويل الأدوات يدويًا - LangChain4j يتولى كل تعقيد تحويل أدوات MCP إلى صيغة متوافقة مع LLM

#### راست

لتحويل استجابة أداة MCP إلى صيغة يمكن لـ LLM فهمها، سنضيف دالة مساعدة تنسق قائمة الأدوات. أضف الكود التالي إلى ملف `main.rs` الخاص بك تحت دالة `main`. سيُستدعى هذا عند إجراء طلبات إلى LLM:

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

رائع، نحن معدون الآن للتعامل مع أي طلبات من المستخدم، لذا دعونا نتناول ذلك بعد ذلك.

### -4- التعامل مع طلبات المستخدم

في هذا الجزء من الكود، سنتعامل مع طلبات المستخدم.

#### تايب سكريبت

1. أضف طريقة ستُستخدم لاستدعاء LLM:

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

        // ٣. قم بشيء ما مع النتيجة
        // يجب القيام به

        }
    }
    ```

    في الكود السابق لقد قمنا بـ:

    - أضفنا طريقة `callTools`.
    - الطريقة تأخذ استجابة LLM وتتحقق من الأدوات التي تم استدعاؤها، إن وجدت:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // استدعاء الأداة
        }
        ```

    - تستدعي أداة إذا كان LLM يشير إلى أنه ينبغي استدعاؤها:

        ```typescript
        // ٢. استدعاء أداة الخادم
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ٣. القيام بشيء ما مع النتيجة
        // يجب القيام به
        ```

2. قم بتحديث دالة `run` لتشمل استدعاءات لـ LLM واستدعاء `callTools`:

    ```typescript

    // ١. إنشاء رسائل تكون مدخلاً للنموذج اللغوي الكبير
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ٢. استدعاء النموذج اللغوي الكبير
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ٣. استعراض رد النموذج اللغوي الكبير، لكل خيار تحقق مما إذا كان يحتوي على استدعاءات أدوات
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

رائع، لنقم بسرد الكود كاملًا:

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
            baseURL: "https://models.inference.ai.azure.com", // قد تحتاج إلى تغيير هذا الرابط في المستقبل: https://models.github.ai/inference
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
            type: "function" as const, // تعيين النوع صراحةً إلى "function"
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
    
          // 3. القيام بشيء ما مع النتيجة
          // يجب التنفيذ
    
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
    
        // 3. مراجعة رد LLM، لكل خيار، تحقق مما إذا كان يحتوي على استدعاءات لأدوات
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

#### بايثون

1. لنضف بعض الاستيرادات اللازمة لاستدعاء LLM

    ```python
    # نموذج اللغة الكبير
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. بعد ذلك، لنضف الدالة التي ستستدعي LLM:

    ```python
    # نموذج لغوي ضخم

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

    في الكود السابق لقد قمنا بـ:

    - تمرير وظائفنا، التي وجدناها على خادم MCP وحولناها، إلى LLM.
    - ثم استدعاء LLM مع هذه الوظائف.
    - ثم نفحص النتيجة لنرى ما هي الوظائف التي يجب علينا استدعاؤها، إن وجدت.
    - وأخيرًا، نمرر مصفوفة من الوظائف التي يجب استدعاؤها.

3. الخطوة النهائية، دعونا نحدث الكود الرئيسي:

    ```python
    prompt = "Add 2 to 20"

    # اسأل نموذج اللغة الكبير عن الأدوات التي يجب استخدامها، إن وجدت
    functions_to_call = call_llm(prompt, functions)

    # اتصل بالدوال المقترحة
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    هذه كانت الخطوة النهائية، في الكود أعلاه نحن:

    - نستدعي أداة MCP عبر `call_tool` باستخدام دالة اعتقد LLM أنه ينبغي استدعاؤها بناءً على مطالبتنا.
    - نطبع نتيجة استدعاء الأداة إلى خادم MCP.

#### .NET

1. لنر بعض الكود لطلب مطالبة LLM:

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

    في الكود السابق لقد قمنا بـ:

    - جلب الأدوات من خادم MCP، `var tools = await GetMcpTools()`.
    - تعريف مطالبة مستخدم `userMessage`.
    - إنشاء كائن خيارات يحدد النموذج والأدوات.
    - إجراء طلب إلى LLM.

2. خطوة أخيرة، لنرى إن كان LLM يعتقد أنه ينبغي استدعاء دالة:

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

    في الكود السابق لقد قمنا بـ:

    - التنقل عبر قائمة استدعاءات الدوال.
    - لكل استدعاء أداة، تحليل الاسم والوسائط واستدعاء الأداة على خادم MCP باستخدام عميل MCP. وأخيرًا نطبع النتائج.

الكود الكامل هنا:

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

#### جافا

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

في الكود السابق لقد قمنا بـ:

- استخدام مطالبات لغوية بسيطة للتفاعل مع أدوات خادم MCP
- إطار عمل LangChain4j يدير تلقائيًا:
  - تحويل مطالبات المستخدم إلى استدعاءات أدوات عند الحاجة
  - استدعاء أدوات MCP المناسبة بناءً على قرار LLM
  - إدارة تدفق المحادثة بين LLM وخادم MCP
- طريقة `bot.chat()` تعيد ردودًا باللغة الطبيعية قد تتضمن نتائج من تنفيذ أدوات MCP
- هذا النهج يوفر تجربة مستخدم سلسة حيث لا يحتاج المستخدمون لمعرفة تفاصيل تنفيذ MCP الأساسية

مثال كامل للكود:

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

#### راست


هنا يحدث الجزء الأكبر من العمل. سنقوم باستدعاء LLM مع موجه المستخدم الأولي، ثم نُعالج الاستجابة لنرى إذا كان هناك حاجة لاستدعاء أي أدوات. إذا كان الأمر كذلك، سنستدعي تلك الأدوات ونستمر في المحادثة مع LLM حتى لا تكون هناك حاجة لمزيد من استدعاءات الأدوات ونحصل على استجابة نهائية.

سنقوم بعدة استدعاءات لـ LLM، لذا دعونا نعرف دالة تتولى استدعاء LLM. أضف الدالة التالية إلى ملف `main.rs` الخاص بك:

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

هذه الدالة تستقبل عميل LLM، قائمة من الرسائل (بما في ذلك موجه المستخدم)، أدوات من خادم MCP، وترسل طلبًا إلى LLM، وتعيد الاستجابة.

ستحتوي الاستجابة من LLM على مصفوفة من `الخيارات`. سنحتاج لمعالجة النتيجة لنعرف إذا كانت هناك `استدعاءات أدوات` موجودة. هذا يُخبرنا أن LLM يطلب استدعاء أداة محددة مع الوسائط. أضف الكود التالي إلى أسفل ملف `main.rs` الخاص بك لتعريف دالة لمعالجة استجابة LLM:

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

    // طباعة المحتوى إذا كان متوفرًا
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

إذا كانت موجودة `استدعاءات أدوات`، تستخرج معلومات الأداة، تستدعي خادم MCP بطلب الأداة، وتضيف النتائج إلى رسائل المحادثة. ثم تستمر المحادثة مع LLM وتُحدّث الرسائل باستجابة المساعد ونتائج استدعاء الأداة.

لاستخراج معلومات استدعاء الأداة التي يعيدها LLM لاستدعاءات MCP، سنضيف دالة مساعدة أخرى لاستخراج كل ما يلزم لإجراء الاستدعاء. أضف الكود التالي إلى أسفل ملف `main.rs` الخاص بك:

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

مع وجود كل القطع في مكانها، يمكننا الآن معالجة موجه المستخدم الأولي واستدعاء LLM. حدث دالتك `main` لتشمل الكود التالي:

```rust
// محادثة نموذج اللغة الكبير مع استدعاءات الأدوات
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

هذا سيستعلم LLM بموجه المستخدم الأولي طالبًا مجموع عددين، وسيعالج الاستجابة للتعامل مع استدعاءات الأدوات بشكل ديناميكي.

عظيم، لقد فعلتها!

## المهمة

خذ الكود من التمرين ووسع الخادم ليشمل المزيد من الأدوات. ثم أنشئ عميلًا مع LLM، كما في التمرين، واختبره مع موجهات مختلفة للتأكد من استدعاء جميع أدوات الخادم ديناميكيًا. هذه الطريقة في بناء العميل تتيح للمستخدم النهائي تجربة مستخدم ممتازة لأنه قادر على استخدام الموجهات بدلاً من أوامر العميل الدقيقة، ويظل غير مدرك لأي استدعاء خادم MCP يحدث.

## الحل

[الحل](./solution/README.md)

## النقاط الرئيسية

- إضافة LLM إلى عميلك توفر طريقة أفضل للمستخدمين للتفاعل مع خوادم MCP.
- تحتاج لتحويل استجابة خادم MCP إلى شيء يمكن لـ LLM فهمه.

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
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->