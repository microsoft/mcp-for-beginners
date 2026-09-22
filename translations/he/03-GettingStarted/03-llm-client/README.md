# יצירת לקוח עם LLM

> [!NOTE]
> דוגמאות הלקוח ב-Java מתחברות דרך תחבורה מורשת HTTP+SSE ומכוונות ל-API של MCP `2025-11-25`. השתמשו ב-SDK תואם `2026-07-28` וב-Streamable HTTP ללקוחות מרוחקים חדשים.
> 
> ללקוחות מרוחקים חדשים יש להשתמש ב-SDK תואם `2026-07-28` וב-Streamable HTTP.

עד כה, ראית כיצד ליצור שרת ולקוח. הלקוח היה מסוגל לקרוא לשרת במפורש כדי לרשום את הכלים, המשאבים והפרומפטים שלו. עם זאת, זהו לא גישה פרקטית מאוד. המשתמשים שלך חיים בעידן האגנטי וצופים להשתמש בפרומפטים ולתקשר עם LLM במקום זאת. הם לא דואגים אם אתה משתמש ב-MCP לאחסון היכולות שלך; הם פשוט מצפים לתקשר בשפת טבעית. אז איך נפתור את זה? הפתרון הוא להוסיף LLM ללקוח.

## סקירה כללית

בשיעור זה נתרכז בהוספת LLM לעשיית הלקוח שלך ונראה כיצד זה מספק חוויה טובה יותר למשתמש שלך.

## מטרות לימוד

בסיום שיעור זה תהיה מסוגל:

- ליצור לקוח עם LLM.
- לתקשר בצורה חלקה עם שרת MCP באמצעות LLM.
- לספק חוויית משתמש טובה יותר בצד הלקוח.

## גישה

בוא ננסה להבין את הגישה שצריך לקחת. הוספת LLM נשמעת פשוטה, אבל האם נבצע זאת באמת?

כך הלקוח יתקשר עם השרת:

1. הקמת חיבור עם השרת.

1. רשימת היכולות, הפרומפטים, המשאבים והכלים, ושמירת הסכימה שלהם.

1. הוספת LLM והעברת היכולות ושמירת הסכימה שלהם בפורמט שה-LLM מבין.

1. טיפול בפרומפט משתמש על ידי העברתו ל-LLM יחד עם הכלים שרשום הלקוח.

מצוין, עכשיו כשאנחנו מבינים כיצד ניתן לעשות זאת ברמה גבוהה, בוא ננסה את זה בתרגיל הבא.

## תרגיל: יצירת לקוח עם LLM

בתרגיל זה נלמד כיצד להוסיף LLM ללקוח שלנו.

### אימות באמצעות טוקן גישה אישי של GitHub

יצירת טוקן ב-GitHub היא תהליך פשוט. כך ניתן לעשות זאת:

- עבור ללשונית ההגדרות של GitHub – לחץ על תמונת הפרופיל בפינה הימנית העליונה ובחר בהגדרות.
- נווט להגדרות מפתח – גלול למטה ולחץ על Developer Settings.
- בחר בטוקני גישה אישית – לחץ על Fine-grained tokens ואז צור טוקן חדש.
- הגדר את הטוקן שלך – הוסף הערה לעיון, הגדר תאריך תפוגה ובחר את ההרשאות הנחוצות. במקרה זה ודא להוסיף את ההרשאה Models.
- צור והעתק את הטוקן – לחץ על Generate token, וודא להעתיק אותו מיד, כיוון שלא תוכל לראות אותו שוב.

### -1- התחבר לשרת

בוא ניצור את הלקוח שלנו תחילה:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ייבא zod לאימות סכימה

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

בקוד הקודם עשינו:

- ייבאנו את הספריות הנחוצות
- יצרנו מחלקה עם שני חברים, `client` ו-`openai` שיעזרו לנו לנהל לקוח ולתקשר עם LLM בהתאמה.
- קונפגנו את מופע ה-LLM שלנו להשתמש במודלים של GitHub על ידי הגדרת `baseUrl` כדי להפנות ל-API של האינפרנס.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# צור פרמטרים של שרת לקישור stdio
server_params = StdioServerParameters(
    command="mcp",  # קובץ הרצה
    args=["run", "server.py"],  # פרמטרי שורת פקודה אופציונליים
    env=None,  # משתני סביבה אופציונליים
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # אתחל את החיבור
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

בקוד הקודם עשינו:

- ייבאנו את הספריות הנחוצות ל-MCP
- יצרנו לקוח

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

תחילה, עליך להוסיף את התלויות של LangChain4j לקובץ `pom.xml` שלך. הוסף את התלויות האלו כדי לאפשר אינטגרציה ל-MCP ול-API MiniMax תואם OpenAI:

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

הגדר את מפתח ה-API של MiniMax, ואפשר גם להגדיר נקודת קצה ודגם אופציונליים.
`MINIMAX_MODEL_ID` תומך ב-`MiniMax-M3` ו-`MiniMax-M2.7`. אם
`OPENAI_BASE_URL` לא מוגדר, `MINIMAX_REGION` תומך ב-`global_en` ו-`cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

כדי לבחור נקודת קצה לפי אזור, השמט את `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

אז צור את מחלקת הלקוח שלך ב-Java:

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

        // צור תחבורת MCP להתחברות לשרת
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // צור לקוח MCP
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

- **הוספנו תלויות LangChain4j**: נדרשות לאינטגרציה עם MCP ו-API MiniMax תואם OpenAI
- **ייבאנו את ספריות LangChain4j**: לאינטגרציה עם MCP ולפונקציונליות של דגם צ'אט OpenAI
- **יצרנו `ChatLanguageModel`**: מקונפג להשתמש ב-MiniMax עם מפתח API, נקודת הקצה וזיהוי הדגם
- **הגדרנו תחבורה HTTP**: באמצעות Server-Sent Events (SSE) להתחברות לשרת MCP
- **יצרנו לקוח MCP**: שיטפל בתקשורת עם השרת
- **השתמשנו בתמיכה מובנית של LangChain4j ב-MCP**: שמפשטת אינטגרציה בין LLM לשרתי MCP

#### Rust

דוגמה זו מניחה שיש לך שרת MCP מבוסס Rust פועל. אם אין לך, עיין בשיעור [01-first-server](../01-first-server/README.md) ליצירת השרת.

לאחר שיש לך את שרת MCP Rust, פתח טרמינל ונווט לתיקיית השרת. ואז הפעל את הפקודה הבאה ליצירת פרויקט לקוח LLM חדש:

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
> אין ספריית Rust רשמית ל-OpenAI, אך ה-crate `async-openai` היא [ספרייה שמנוהלת על ידי הקהילה](https://platform.openai.com/docs/libraries/rust#rust) ונפוצה לשימוש.

פתח את הקובץ `src/main.rs` והחלף את תוכנו בקוד הבא:

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
    // הודעה התחלתית
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // הגדרת לקוח OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // הגדרת לקוח MCP
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

    // יש לעשות: לקבל רשימת כלים של MCP

    // יש לעשות: שיחה עם LLM עם קריאות לכלים

    Ok(())
}
```

קוד זה מגדיר אפליקציית Rust בסיסית שתתחבר לשרת MCP ולמודלים של GitHub לאינטראקציה עם LLM.

> [!IMPORTANT]
> וודא להגדיר את משתנה הסביבה `OPENAI_API_KEY` עם הטוקן שלך מ-GitHub לפני הרצת האפליקציה.

מצוין, לשלב הבא, בוא נרשום את היכולות בשרת.

### -2- רשום את היכולות של השרת

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

    // רישום כלים
    const toolsResult = await this.client.listTools();
}
```

בקוד הקודם עשינו:

- הוספנו קוד להתחברות לשרת, `connectToServer`.
- יצרנו מתודה `run` האחראית לניהול זרימת האפליקציה. עד כה היא רק מציגה את הכלים אך נוסיף לה בקרוב.

#### Python

```python
# רשום משאבים זמינים
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# רשום כלים זמינים
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

כך הוספנו:

- רשימת משאבים וכלים והדפסתם. עבור כלים גם רשמנו את `inputSchema` שנשתמש בו אחר כך.

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

בקוד הקודם עשינו:

- רשמנו את הכלים הזמינים בשרת MCP
- עבור כל כלי, רשמנו שם, תיאור וסכימה שלו. הסכימה מטרתה לשימוש בקריאה לכלים בקרוב.

#### Java

```java
// צור ספק כלי שמגלה אוטומטית כלים של MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ספק הכלים של MCP מטפל אוטומטית ב:
// - רשימת כלים זמינים משרת MCP
// - המרת סכמות כלים של MCP לפורמט LangChain4j
// - ניהול ביצוע הכלים והתגובות שלהם
```

בקוד הקודם עשינו:

- יצרנו `McpToolProvider` שמגלה ומרשום אוטומטית את כל הכלים משרת MCP
- ספק הכלים מטפל בהמרה בין סכימות כלי MCP לפורמט הכלים של LangChain4j באופן פנימי
- גישה זו מסתירה את תהליך רישום והמרת הכלים הידני

#### Rust

שליפת כלים משרת MCP נעשית באמצעות המתודה `list_tools`. בפונקציית `main` שלך, לאחר הגדרת לקוח MCP, הוסף את הקוד הבא:

```rust
// קבל רשימת כלי MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- המר היכולות של השרת לכלי LLM

השלב הבא לאחר רישום יכולות השרת הוא להמיר אותן לפורמט שה-LLM מבין. ברגע שנעשה זאת, נוכל לספק את היכולות הללו ככלים ל-LLM שלנו.

#### TypeScript

1. הוסף את הקוד הבא להמרת תגובה משרת MCP לפורמט כלי שה-LLM יכול להשתמש בו:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // צור סכימת זוד מבוססת על input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // הגדר במפורש את הסוג ל-"function"
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

הקוד שלמעלה לוקח תגובה משרת MCP וממיר אותה לפורמט הגדרת כלי שה-LLM מבין.

2. עכשיו נעודכן את מתודת `run` לרשימת יכולות השרת:

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

בקוד שלמעלה, עדכנו את ה-run כדי למפות את התוצאה ולקרוא עבור כל פריט את `openAiToolAdapter`.

#### Python

1. תחילה ניצור את פונקציית ההמרה הבאה

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

בפונקציה שלמעלה `convert_to_llm_tools` אנו לוקחים תגובת כלי MCP וממירים אותה לפורמט שה-LLM מבין.

2. לאחר מכן נעדכן את קוד הלקוח שלנו להשתמש בפונקציה זו כך:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

כאן אנו מוסיפים קריאה ל-`convert_to_llm_tool` להמרת תגובת כלי MCP למשהו שנוכל להזין ל-LLM מאוחר יותר.

#### .NET

1. נוסיף קוד להמרת תגובת כלי MCP למשהו שה-LLM יכול להבין

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

בקוד הקודם עשינו:

- יצרנו פונקציה `ConvertFrom` שלוקחת שם, תיאור וסכמת קלט.
- הגדרנו פונקציונליות שיוצרת FunctionDefinition שמועברת ל-ChatCompletionsDefinition. האחרון הוא פורמט שה-LLM מבין.

2. נראה איך נוכל לעדכן קוד קיים כדי לנצל את הפונקציה הזו:

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
// צור ממשק בוט לאינטראקציה בשפה טבעית
public interface Bot {
    String chat(String prompt);
}

// הגדר את שירות ה-AI עם כלי LLM ו-MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

בקוד הקודם עשינו:

- הגדרנו ממשק פשוט `Bot` לאינטראקציות בשפה טבעית
- השתמשנו ב-`AiServices` של LangChain4j כדי לקשור אוטומטית את ה-LLM עם ספק הכלים MCP
- המסגרת מטפלת אוטומטית בהמרת סכימת הכלי ובקריאות פונקציה מאחורי הקלעים
- גישה זו מבטלת המרת כלים ידנית - LangChain4j מנהל את כל המורכבות של המרת כלים MCP לפורמט תואם LLM

#### Rust

להמרת תגובת כלי MCP לפורמט שה-LLM מבין, נוסיף פונקציית עזר שמעצבת את רשימת הכלים. הוסף את הקוד הבא לקובץ `main.rs` מתחת לפונקציית `main`. פונקציה זו תוקרא בעת ביצוע בקשות ל-LLM:

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

מצוין, אנחנו מוכנים לטפל בבקשות משתמשים, אז בוא נתקדם לכך.

### -4- טיפול בבקשות פרומפט משתמש

בחלק זה של הקוד, נטפל בבקשות המשתמש.

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


        // 2. לקרוא לכלי השרת
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. לעשות משהו עם התוצאה
        // לעשות

        }
    }
    ```

בקוד הקודם עשינו:

- הוספנו מתודה `callTools`.
- המתודה מקבלת תגובה מה-LLM ובודקת אילו כלים נקראו, אם בכלל:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // קריאה לכלי
        }
        ```

- קורא לכלי, אם ה-LLM מציין שעליו להיקרא:

        ```typescript
        // 2. לקרוא לכלי של השרת
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. לעשות משהו עם התוצאה
        // לעשות
        ```

2. עדכן את מתודת `run` שתכלול קריאות ל-LLM ולקריאה ל-`callTools`:

    ```typescript

    // 1. צור הודעות שהן קלט עבור ה-LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. קריאה ל-LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. עבור על תגובת ה-LLM, לכל בחירה, בדוק אם יש קריאות לכלים
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

מצוין, בוא נראה את הקוד כולו:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ייבא את zod לאימות סכימה

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ייתכן שיהיה צורך לשנות לכתובת URL זו בעתיד: https://models.github.ai/inference
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
          // צור סכמת zod על בסיס ה-input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // הגדר במפורש את הטיפוס כ"function"
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
    
    
          // 2. קרא לכלי של השרת
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. עשה משהו עם התוצאה
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 3. עבור על תגובת ה-LLM, עבור כל בחירה, בדוק אם יש קריאות לכלים
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

1. נוסיף ייבוא נחוצים לקריאה ל-LLM

    ```python
    # למ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. לאחר מכן, נוסיף את הפונקציה שקוראת ל-LLM:

    ```python
    # למ"מ

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
            # פרמטרים אופציונליים
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

בקוד הקודם עשינו:

- העברנו פונקציות שמצאנו על שרת MCP והמרנו אותם ל-LLM.
- לאחר מכן קראנו ל-LLM עם פונקציות אלו.
- לאחר מכן בדקנו את התוצאה לראות אילו פונקציות צריך לקרוא, אם בכלל.
- ולבסוף העברנו מערך פונקציות שיש לקרוא.

3. שלב סופי, נעדכן את הקוד הראשי שלנו:

    ```python
    prompt = "Add 2 to 20"

    # שאל את מודל השפה איזה כלים להשתמש בהם, אם בכלל
    functions_to_call = call_llm(prompt, functions)

    # קריאה לפונקציות המוצעות
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

זה היה השלב האחרון, בקוד שלמעלה אנחנו:

- קוראים לכלי MCP באמצעות `call_tool` על פי פונקציה שה-LLM חשב שצריך לקרוא בהתבסס על הפרומפט שלנו.
- מדפיסים את תוצאת קריאת הכלי לשרת MCP.

#### .NET

1. נראה קוד לבקשת פרומפט LLM:

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

בקוד הקודם עשינו:

- קיבלנו כלים משרת MCP, `var tools = await GetMcpTools()`.
- הגדרנו פרומפט משתמש `userMessage`.
- יצרנו אובייקט אפשרויות שמציין דגם וכלים.
- ביצענו בקשה אל ה-LLM.

2. שלב אחרון, נראה אם ה-LLM חושב שצריך לקרוא לפונקציה:

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

בקוד הקודם עשינו:

- עברנו בלולאה על רשימת קריאות לפונקציות.
- עבור כל קריאת כלי, פירשנו שם וארגומנטים וקרינו לכלי בשרת MCP באמצעות לקוח MCP. בסוף הדפסנו את התוצאות.

הנה הקוד במלואו:

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
    // הפעל בקשות בשפה טבעית המשתמשות באופן אוטומטי בכלי MCP
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

בקוד הקודם עשינו:

- השתמשנו בפרומפטים פשוטים בשפה טבעית לאינטראקציה עם כלי שרת MCP
- מסגרת LangChain4j מטפלת באופן אוטומטי ב:
  - המרת פרומפטים לקריאות כלים כשנדרש
  - קריאת הכלים המתאימים של MCP בהתאם להחלטת ה-LLM
  - ניהול זרימת השיחה בין ה-LLM לשרת MCP
- מתודת `bot.chat()` מחזירה תגובות בשפה טבעית שיכולות לכלול תוצאות מביצועי כלי MCP
- גישה זו מספקת חוויית משתמש חלקה שבה המשתמשים לא צריכים לדעת על היישום הפנימי של MCP

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


כאן מתבצע רוב העבודה. נקרא ל-LLM עם הפקודה הראשונית של המשתמש, ולאחר מכן נעבד את התגובה כדי לראות אם יש צורך לקרוא לכלים כלשהם. אם כן, נקרא לכלים אלו ונמשיך את השיחה עם ה-LLM עד שלא יידרשו עוד קריאות לכלים ונקבל תגובה סופית.

נקרא ל-LLM מספר פעמים, אז נגדיר פונקציה שתטפל בקריאות ל-LLM. הוסף את הפונקציה הבאה לקובץ `main.rs` שלך:

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

פונקציה זו מקבלת את לקוח ה-LLM, רשימת הודעות (כולל פקודת המשתמש), כלים משרת ה-MCP, ושולחת בקשה ל-LLM, ומחזירה את התגובה.

התגובה מ-LLM תכיל מערך של `choices`. נצטרך לעבד את התוצאה כדי לבדוק אם קיימות `tool_calls`. זה מאפשר לנו לדעת שה-LLM מבקש שייקרא כלי ספציפי עם ארגומנטים. הוסף את הקוד הבא לתחתית הקובץ `main.rs` שלך כדי להגדיר פונקציה שתטפל בתגובת ה-LLM:

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

    // הדפס תוכן אם זמין
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // טיפול בקריאות כלי
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // הוסף הודעת עוזר

        // ביצוע כל קריאת כלי
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // הוסף תוצאות כלי להודעות
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // המשך שיחה עם תוצאות כלי
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

אם קיימות `tool_calls`, היא מוציאה את מידע הכלי, קוראת לשרת ה-MCP עם בקשת הכלי, ומוסיפה את התוצאות להודעות השיחה. לאחר מכן ממשיכה בשיחה עם ה-LLM, וההודעות מתעדכנות עם תגובת העוזר ותוצאות קריאת הכלי.

כדי להוציא מידע על קריאת כלי שה-LLM מחזיר לקריאות MCP, נוסיף פונקציית עזר נוספת שתוציא את כל הדרוש לביצוע הקריאה. הוסף את הקוד הבא לתחתית הקובץ `main.rs` שלך:

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

עם כל החלקים במקום, כעת נוכל לטפל בפקודת המשתמש הראשונית ולקרא ל-LLM. עדכן את הפונקציה `main` שלך לכלול את הקוד הבא:

```rust
// שיחת LLM עם קריאות לכלים
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

זה ישאל את ה-LLM עם פקודת המשתמש הראשונית המבקשת סכום של שני מספרים, ויעבד את התגובה כדי לטפל בצורה דינמית בקריאות לכלים.

מצוין, הצלחת!

## משימה

קח את הקוד מהתרגיל ובנה את השרת עם עוד כלים. לאחר מכן יצור לקוח עם LLM, כמו בתרגיל, ובדוק אותו עם פקודות שונות כדי לוודא שכל הכלים בשרת נקראים בצורה דינמית. דרך בניית לקוח זו מבטיחה למשתמש קצה חוויית שימוש טובה כי הוא יכול להשתמש בפקודות חופשיות במקום פקודות מדויקות של הלקוח, ויהיה חסר מודעות לקריאות שרת MCP.

## פתרון

[פתרון](./solution/README.md)

## נקודות מפתח

- הוספת LLM ללקוח שלך מספקת דרך טובה יותר למשתמשים לתקשר עם שרתי MCP.
- יש להמיר את תגובת שרת ה-MCP למשהו שה-LLM יכול להבין.

## דוגמאות

- [מחשבון Java](../samples/java/calculator/README.md)
- [מחשבון .Net](../../../../03-GettingStarted/samples/csharp)
- [מחשבון JavaScript](../samples/javascript/README.md)
- [מחשבון TypeScript](../samples/typescript/README.md)
- [מחשבון Python](../../../../03-GettingStarted/samples/python)
- [מחשבון Rust](../../../../03-GettingStarted/samples/rust)

## משאבים נוספים

## מה הלאה

- הבא: [צריכת שרת עם Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->