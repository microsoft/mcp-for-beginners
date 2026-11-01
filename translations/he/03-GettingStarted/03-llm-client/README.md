# יצירת לקוח עם LLM

> [!NOTE]
> דוגמאות לקוח בג'אווה מתחברות דרך תחבורה ישנה מסוג HTTP+SSE ומכוונות ל-API של MCP `2025-11-25` SDK. השתמש ב-SDK תואם `2026-07-28`
> ו-Streamable HTTP ללקוחות מרוחקים חדשים.




## סקירה כללית

בשיעור זה נתמקד בהוספת LLM ללקוח שלך ונראה כיצד זה מספק חוויה טובה בהרבה למשתמש שלך.

## מטרות הלמידה

בסוף השיעור הזה תוכל:

- ליצור לקוח עם LLM.
- ליצור אינטראקציה חלקה עם שרת MCP באמצעות LLM.
- להעניק חוויית משתמש טובה יותר בצד הלקוח.

## הגישה

בוא ננסה להבין את הגישה שעלינו לקחת. הוספת LLM נשמעת פשוטה, אבל האם נעשה זאת בפועל?

כך הלקוח יתקשר עם השרת:

1. יצירת חיבור עם השרת.

1. רישום היכולות, הנחיות, משאבים וכלים, ושמירת הסכימה שלהם.

1. הוספת LLM והעברת היכולות השמורות והסכימה שלהן בפורמט שה-LLM מבין.

1. טיפול בהנחיית משתמש על ידי העברתה ל-LLM יחד עם הכלים שהלקוח רשם.

מצוין, עכשיו כשאנחנו מבינים איך לעשות זאת ברמה הגבוהה, בוא ננסה זאת באימון הבא.

## תרגיל: יצירת לקוח עם LLM

בתרגיל זה נלמד להוסיף LLM ללקוח שלנו.

### הגדרת Microsoft Foundry

GitHub Models הוסרו ב-30 ביולי 2026. צור משאב Microsoft Foundry,
פרוס מודל פעיל כגון `gpt-5.1`, והגדר את משתני הסביבה הבאים:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

השתמש בשם הפריסה בשיחות API. הוא עשוי להיות שונה משם המודל הבסיסי.
עיין בלוח הזמנים לפרישת המודלים של
[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
לפני בחירת מודל.

### -1- התחבר לשרת

בוא ניצור את הלקוח שלנו תחילה:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod for schema validation

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
            }
            );    
    }
}
```

בקוד הקודם עשינו:

- ייבאנו את הספריות הנדרשות
- יצרנו מחלקה עם שני משתנים, `client` ו-`openai` שיעזרו לנו לנהל לקוח ולהתקשר עם LLM בהתאמה.
- הגדרנו את לקוח OpenAI להשתמש בנקודת הקצה של Microsoft Foundry v1 ומפתח ה-API.

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

בקוד הקודם עשינו:

- ייבאנו את הספריות הנדרשות עבור MCP
- יצרנו לקוח

#### .NET

```csharp
using ModelContextProtocol.Client;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
var client = new ChatClient(
    deployment,
    new ApiKeyCredential(apiKey),
    new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

ראשית, תצטרך להוסיף את התלויות של LangChain4j לקובץ `pom.xml` שלך. הוסף את התלויות האלה כדי לאפשר אינטגרציה עם MCP ו-API MiniMax התואם ל-OpenAI:

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

הגדר את מפתח ה-API של MiniMax שלך, ואופציונלית גם את נקודת הקצה והמודל.
`MINIMAX_MODEL_ID` תומך ב-`MiniMax-M3` ו-`MiniMax-M2.7`. אם
`OPENAI_BASE_URL` לא מוגדר, `MINIMAX_REGION` תומך ב-`global_en` ו-`cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

כדי לבחור את נקודת הקצה לפי אזור במקום זאת, השמט את `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

לאחר מכן צור את מחלקת הלקוח בג'אווה שלך:

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

        // Create MCP transport for connecting to server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Create MCP client
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

בקוד הקודם עשינו:

- **הוספנו את תלויות LangChain4j**: דרושות לאינטגרציה עם MCP ו-API MiniMax התואם ל-OpenAI
- **ייבאנו את ספריות LangChain4j**: לאינטגרציה עם MCP ולפונקציונליות מודל הצ'אט של OpenAI
- **יצרנו `ChatLanguageModel`**: הוגדר להשתמש ב-MiniMax עם מפתח ה-API, נקודת הקצה ו-מודל ID התומך
- **קבענו תחבורה HTTP**: באמצעות Server-Sent Events (SSE) להתחברות לשרת MCP
- **יצרנו לקוח MCP**: שיטפל בתקשורת עם השרת
- **השתמשנו בתמיכה המובנית של LangChain4j ב-MCP**: שמפשטת אינטגרציה בין LLM לשרתי MCP

#### Rust

דוגמה זו מניחה שיש לך שרת MCP מבוסס Rust פועל. אם אין לך אחד, עיין שוב ב-[01-first-server](../01-first-server/README.md) ליצירת השרת.

לאחר שיש לך שרת MCP של Rust, פתח טרמינל ונווט לתיקייה שבה נמצא השרת. לאחר מכן הרץ את הפקודה הבאה ליצירת פרויקט לקוח LLM חדש:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

הוסף את התלויות הבאות לקובץ `Cargo.toml` שלך:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> אין ספריית Rust רשמית ל-OpenAI, אולם ה-crate `async-openai` היא [ספרייה שמתחזקת בקהילה](https://platform.openai.com/docs/libraries/rust#rust) ונפוצה לשימוש.

פתח את קובץ `src/main.rs` והחלף את תוכנו בקוד הבא:

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
    // Initial message
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Setup Microsoft Foundry client
    let endpoint = std::env::var("AZURE_OPENAI_ENDPOINT")?;
    let api_key = std::env::var("AZURE_OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base(format!("{}/openai/v1", endpoint.trim_end_matches('/')))
            .with_api_key(api_key),
    );

    // Setup MCP client
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

    // TODO: Get MCP tool listing 

    // TODO: LLM conversation with tool calls

    Ok(())
}
```

הקוד הזה מגדיר אפליקציית Rust שמתחברת לשרת MCP ו
לפריסת מודל Microsoft Foundry עבור אינטראקציות LLM.

> [!IMPORTANT]
> הגדר את `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, ו-
> `AZURE_OPENAI_DEPLOYMENT` לפני הרצת האפליקציה.

מצוין, בשלב הבא, בוא נרשום את היכולות בשרת.

### -2- רישום יכולות השרת

עכשיו נתחבר לשרת ונבקש את היכולות שלו:

#### Typescript

באותה מחלקה, הוסף את הפונקציות הבאות:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // listing tools
    const toolsResult = await this.client.listTools();
}
```

בקוד הקודם אנו:

- הוספנו קוד להתחברות לשרת, `connectToServer`.
- יצרנו מתודה `run` האחראית לניהול הזרימה של האפליקציה שלנו. עד כה היא רק מפרטת את הכלים אך בקרוב נוסיף לה עוד.

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
    print("Tool", tool.inputSchema["properties"])
```

הנה מה שהוספנו:

- רשימת משאבים וכלים והדפסתם. עבור כלים אנו גם מפרטים `inputSchema` שנשתמש בהם בהמשך.

#### .NET

```csharp
async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

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

בקוד הקודם אנו:

- ריכזנו את הכלים הזמינים בשרת MCP
- לכל כלי ריכזנו את השם, התיאור והסכמה שלו. האחרונה היא משהו שנשתמש בו בקרוב לקריאת הכלים.

#### Java

```java
// Create a tool provider that automatically discovers MCP tools
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// The MCP tool provider automatically handles:
// - Listing available tools from the MCP server
// - Converting MCP tool schemas to LangChain4j format
// - Managing tool execution and responses
```

בקוד הקודם אנו:

- יצרנו `McpToolProvider` שמגלה ומרשום אוטומטית את כל הכלים משרת MCP
- ספק הכלים מטפל בהמרה בין סכמות הכלים של MCP לפורמט הכלים של LangChain4j פנימית
- גישה זו מסתירה את התהליך הידני של רישום הכלים והמרתם

#### Rust

אחזור הכלים משרת MCP מתבצע באמצעות מתודת `list_tools`. בפונקציה שלך `main`, לאחר שהגדרת את לקוח MCP, הוסף את הקוד הבא:

```rust
// Get MCP tool listing 
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- המרת יכולות השרת לכלי LLM

השלב הבא לאחר רישום יכולות השרת הוא להמיר אותן לפורמט שה-LLM מבין. ברגע שנעשה זאת, נוכל לספק יכולות אלה ככלים ל-LLM שלנו.

#### TypeScript

1. הוסף את הקוד הבא להמרת תגובת שרת MCP לפורמט כלים שה-LLM יכול להשתמש בו:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Create a zod schema based on the input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Explicitly set type to "function"
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

    הקוד שלמעלה מקבל תגובה משרת MCP וממיר אותה לפורמט הגדרת כלים שה-LLM יכול להבין.

2. נעדכן את המתודה `run` ברשימת יכולות השרת:

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

    בקוד הקודם, עדכנו את המתודה `run` למפות על התוצאה ולקרוא לכל כניסה את `openAiToolAdapter`.

#### Python

1. קודם כל, ניצור את פונקציית ההמרה הבאה

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

    בפונקציה שלמעלה `convert_to_llm_tools` אנו לוקחים תגובת כלי מ-MCP וממירים אותה לפורמט שה-LLM יכול להבין.

2. לאחר מכן, נעדכן את קוד הלקוח שלנו לנצל פונקציה זו כך:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    כאן, אנו מוסיפים קריאה ל-`convert_to_llm_tool` כדי להמיר את תגובת הכלי של MCP למשהו שנוכל להאכיל ל-LLM בהמשך.

#### .NET

1. נעתיק קוד להמרת תגובת כלי MCP למשהו שה-LLM יכול להבין

```csharp
ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}
```

בקוד הקודם אנו:

- יצרנו פונקציה `ConvertFrom` שלוקחת שם, תיאור וסקמת קלט.
- יצרנו OpenAI `ChatTool` מתוך הסכמה JSON של כלי MCP.

2. נראה כיצד נוכל לעדכן קוד קיים כדי לנצל את הפונקציה שלמעלה:

    ```csharp
    async Task<List<ChatTool>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatTool> toolDefinitions = [];

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);
        }

        return toolDefinitions;
    }
    ```
    
בקוד הקודם אנו:

- עדכנו את הפונקציה להמרת תגובת כלי MCP לכלי LLM. נציג את הקוד שהוספנו:

   ```csharp
   JsonElement propertiesElement;
   tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

   var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
   Console.WriteLine($"Tool definition: {def}");
   toolDefinitions.Add(def);
   ```

סכמה של קלט היא חלק מתגובת הכלי אבל תחת התכונה "properties", לכן עלינו לחלץ אותה. בנוסף, אנו עכשיו קוראים ל-`ConvertFrom` עם פרטי הכלי. לאחר שעשינו את העבודה הקשה, נראה כיצד הקריאה מתבצעת כשאנחנו מטפלים בפרומפט של המשתמש בהמשך.

#### Java

```java
// Create a Bot interface for natural language interaction
public interface Bot {
    String chat(String prompt);
}

// Configure the AI service with LLM and MCP tools
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

בקוד הקודם אנו:

- הגדרנו ממשק `Bot` פשוט לאינטראקציות בשפה טבעית
- השתמשנו ב-`AiServices` של LangChain4j כדי לקשר אוטומטית בין ה-LLM לספק כלי MCP
- המסגרת מטפלת אוטומטית בהמרת סכמה של כלים וקריאות לפונקציות ברקע
- גישה זו מבטלת את ההמרה הידנית של כלים - LangChain4j מנהלת את כל המורכבות של המרת כלי MCP לפורמט תואם LLM

#### Rust

כדי להמיר תגובת כלי MCP לפורמט שה-LLM יכול להבין, נוסיף פונקציית עזר שמעצבת את רישום הכלים. הוסף את הקוד הבא לקובץ `main.rs` מתחת לפונקציה `main`. פונקציה זו תיקרא כאשר נעשה בקשה ל-LLM:

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

מצוין, אנחנו מוכנים לטפל בבקשות משתמש, בואו נטפל בזה עכשיו.

### -4- טיפול בבקשת פרומפט משתמש

בחלק זה של הקוד, נטפל בבקשות משתמש.

#### TypeScript

1. הוסף מתודה שתשמש לקריאה ל-LLM שלנו:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  

        }
    }
    ```

    בקוד הקודם:

    - הוספנו מתודה `callTools`.
    - המתודה מקבלת תגובת LLM ובודקת אילו כלים הופעלו, אם בכלל:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // call tool
        }
        ```

    - קוראת לכלי, אם ה-LLM מציין שיש לקרוא לו:

        ```typescript
        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  
        ```

2. עדכן את המתודה `run` לכלול קריאות ל-LLM וקריאה ל-`callTools`:

    ```typescript

    // 1. Create messages that's input for the LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Calling the LLM
    let response = this.openai.chat.completions.create({
        model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
        max_completion_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Go through the LLM response,for each choice, check if it has tool calls 
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

מצוין, נציג את הקוד כולו:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod for schema validation

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
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
          // Create a zod schema based on the input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Explicitly set type to "function"
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
    
    
          // 2. Call the server's tool 
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Do something with the result
          // TODO  
    
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
            model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
            max_completion_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 3. Go through the LLM response, for each choice, check if it has tool calls 
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

1. נוסיף כמה ייבוא שצריך כדי לקרוא ל-LLM

    ```python
    # llm
    import os
    from openai import OpenAI
    import json
    ```

2. לאחר מכן, נוסיף את הפונקציה שתתקשר ל-LLM. דוגמה זו משתמשת במודל
    `gpt-5.1` הפעיל. בדוק את
    [לו"ז הפרישה של מודל Microsoft Foundry](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
    כשאתה בוחר מודל לאפליקציה שלך.

    ```python
    # llm

    def call_llm(prompt, functions):
        client = OpenAI(
            base_url=(
                f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/"
            ),
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
        )

        print("CALLING LLM")
        response = client.chat.completions.create(
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
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"),
            tools=functions,
            max_completion_tokens=1000,
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

    בקוד הקודם:

    - העברנו את הפונקציות שלנו, שמצאנו על שרת MCP והמרנו, ל-LLM.
    - לאחר מכן קראנו ל-LLM עם הפונקציות האמורות.
    - לאחר מכן בודקים את התוצאה כדי לראות אילו פונקציות עלינו לקרוא, אם בכלל.
    - לבסוף, אנו מעבירים מערך פונקציות לקריאה.

3. שלב סופי, נעדכן את הקוד הראשי שלנו:

    ```python
    prompt = "Add 2 to 20"

    # ask LLM what tools to all, if any
    functions_to_call = call_llm(prompt, functions)

    # call suggested functions
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    הנה, זה השלב הסופי, בקוד למעלה אנו:

    - קוראים לכלי MCP דרך `call_tool` באמצעות פונקציה שה-LLM סבר שצריך לקרוא לה לפי הפרומפט שלנו.
    - מדפיסים את תוצאת קריאת הכלי לשרת MCP.

#### .NET

1. נציג קוד לביצוע בקשת פרומפט ל-LLM:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new UserChatMessage(userMessage));


    // 2. Define options, including the tools
    var options = new ChatCompletionOptions
    {
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
    var content = response.Content.FirstOrDefault()?.Text;

    ```

    בקוד הקודם אנו:

    - כלים שנשלפו משרת MCP, `var tools = await GetMcpTools()`.
    - הוגדר הנחיית משתמש `userMessage`.
    - בחר אובייקט אופציות שמפרט דגם וכלים.
    - ביצע בקשה כלפי LLM.

2. צעד אחרון, בואו נראה אם מודל השפה הגדול חושב שעלינו לקרוא לפונקציה:

    ```csharp
    // 4. Check if the response contains a function call
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
        var result = await mcpClient.CallToolAsync(
            call.FunctionName,
            dict!,
            cancellationToken: CancellationToken.None
        );

        var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
        if (textBlock != null)
        {
            Console.WriteLine(textBlock.Text);
        }

    }
    ```

בקוד הקודם שלנו:

- עברנו על רשימת קריאות לפונקציות.
- עבור כל קריאה לכלי, פרסרנו את השם והארגומנטים וקראנו לכלי על שרת ה-MCP באמצעות לקוח ה-MCP. בסוף הדפסנו את התוצאות.

הנה הקוד במלואו:

```csharp
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
if (string.IsNullOrWhiteSpace(endpoint) || string.IsNullOrWhiteSpace(apiKey))
{
    Console.WriteLine("Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY.");
    return;
}

var client = new ChatClient(
    model: deployment,
    credential: new ApiKeyCredential(apiKey),
    options: new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });
var chatHistory = new List<ChatMessage>
{
    new SystemChatMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}

async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
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

chatHistory.Add(new UserChatMessage(userMessage));

// 3. Define options, including the tools
var options = new ChatCompletionOptions
{
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
var content = response.Content.FirstOrDefault()?.Text;

// 5. Check if the response contains a function call
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
    var result = await mcpClient.CallToolAsync(
        call.FunctionName,
        dict!,
        cancellationToken: CancellationToken.None
    );

    var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
    if (textBlock != null)
    {
        Console.WriteLine(textBlock.Text);
    }

}

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Execute natural language requests that automatically use MCP tools
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

בקוד הקודם שלנו:

- השתמשנו בתמרונים בשפה טבעית פשוטה כדי לתקשר עם כלי שרת ה-MCP
- מסגרת LangChain4j מטפלת אוטומטית ב:
  - המרת תמרורי המשתמש לקריאות לכלים בעת הצורך
  - קריאה לכלים המתאימים בשרת ה-MCP על פי החלטת מודל השפה הגדול
  - ניהול זרימת השיחה בין מודל השפה הגדול לשרת ה-MCP
- השיטה `bot.chat()` מחזירה תגובות בשפה טבעית שעלולות לכלול תוצאות מביצועי כלים בשרת ה-MCP
- גישה זו מספקת חוויית משתמש חלקה שבה המשתמשים אינם צריכים לדעת על היישום הפנימי של שרת ה-MCP

דוגמת קוד מלאה:

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

כאן מתרחשת רוב העבודה. נקרא למודל השפה הגדול עם התמרור הראשוני של המשתמש, ואז נעבד את התגובה כדי לראות אם יש צורך לקרוא לכלים כלשהם. אם כן, נקרא לכלים אלה ונמשיך את השיחה עם מודל השפה הגדול עד שלא יהיו עוד קריאות לכלים ונקבל תגובה סופית.

נעשה מספר קריאות למודל השפה הגדול, אז נגדיר פונקציה שתטפל בקריאת מודל השפה הגדול. הוסף את הפונקציה הבאה לקובץ `main.rs` שלך:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let model = std::env::var("AZURE_OPENAI_DEPLOYMENT")
        .unwrap_or_else(|_| "gpt-5.1".to_string());
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": model,
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

פונקציה זו מקבלת את לקוח מודל השפה הגדול, רשימת הודעות (כולל תמרור המשתמש), כלים משרת ה-MCP, ושולחת בקשה למודל השפה הגדול, ומחזירה את התגובה.

התגובה ממרכז הנתונים של מודל השפה הגדול תכיל מערך של `choices`. נצטרך לעבד את התוצאה כדי לראות אם קיימים `tool_calls`. זה מאפשר לנו לדעת שמודל השפה הגדול מבקש שקריאה לכלי מסוים תתבצע עם ארגומנטים. הוסף את הקוד הבא לתחתית קובץ `main.rs` שלך כדי להגדיר פונקציה שתטפל בתגובת מודל השפה הגדול:

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

    // Print content if available
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Handle tool calls
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Add assistant message

        // Execute each tool call
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Add tool result to messages
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Continue conversation with tool results
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

אם קיימים `tool_calls`, הפונקציה שולפת את מידע הכלי, קוראת לשרת ה-MCP עם בקשת הכלי, ומוסיפה את התוצאות להודעות השיחה. לאחר מכן ממשיכה בשיחה עם מודל השפה הגדול וההודעות מתעדכנות עם תגובת העוזר ותוצאות קריאת הכלי.

כדי לשלוף מידע על קריאת הכלי שמודל השפה הגדול מחזיר לקריאות MCP, נוסיף פונקציית עזר נוספת שתשלוף את כל מה שצריך כדי לבצע את הקריאה. הוסף את הקוד הבא לתחתית הקובץ `main.rs` שלך:

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

עכשיו כשכל הרכיבים במקום, נוכל לטפל בתמרור המשתמש הראשוני ולקרא למודל השפה הגדול. עדכן את פונקציית `main` שלך לכלול את הקוד הבא:

```rust
// LLM conversation with tool calls
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

זה ישאל את מודל השפה הגדול עם התמרור הראשוני מבקש את סכום שני מספרים, ויעבד את התגובה כדי לטפל בקריאות לכלים באופן דינמי.

מצוין, עשית את זה!

## משימה

קח את הקוד מהתרגיל ובנה שרת עם עוד כלים. לאחר מכן צור לקוח עם מודל שפה גדול, כמו בתרגיל, ובדוק אותו עם תמרונים שונים כדי לוודא שכל כלי השרת שלך נקרא בצורה דינמית. דרך בניית הלקוח הזו מאפשרת למשתמש הקצה לחוות חוויית משתמש מצוינת כשהוא יכול להשתמש בתמרונים במקום פקודות מדויקות של לקוח, ולהיות חסרי מודעות לכל שרת MCP שמתבצע.

## פתרון

[פתרון](./solution/README.md)

## נקודות מפתח

- הוספת מודל שפה גדול ללקוח שלך מספקת דרך טובה יותר למשתמשים לתקשר עם שרתי MCP.
- יש להמיר את תגובת שרת ה-MCP למשהו שמודל השפה הגדול יכול להבין.

## דוגמאות

- [מחשבון בג'אווה](../samples/java/calculator/README.md)
- [מחשבון ב-.NET](../../../../03-GettingStarted/samples/csharp)
- [מחשבון ב-JavaScript](../samples/javascript/README.md)
- [מחשבון ב-TypeScript](../samples/typescript/README.md)
- [מחשבון בפייתון](../../../../03-GettingStarted/samples/python)
- [מחשבון ברסט](../../../../03-GettingStarted/samples/rust)

## משאבים נוספים

## מה הלאה

- הבא: [שימוש בשרת באמצעות Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->