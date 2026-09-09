# יצירת לקוח עם LLM

עד כה, ראית כיצד ליצור שרת ולקוח. הלקוח היה מסוגל לקרוא לשרת במפורש כדי לרשום את הכלים, המשאבים וההנחיות שלו. עם זאת, זו לא גישה מאוד מעשית. המשתמשים שלך חיים בעידן הסוכני ומצפים להשתמש בהנחיות ולתקשר עם LLM במקום זאת. הם לא אכפת להם אם אתה משתמש ב-MCP כדי לאחסן את היכולות שלך; הם פשוט מצפים לתקשר בשפה טבעית. אז איך אנחנו פותרים את זה? הפתרון הוא להוסיף LLM ללקוח.

## סקירה כללית

בשיעור זה אנו מתמקדים בהוספת LLM ללקוח שלנו ומראים כיצד זה מספק חווייה טובה יותר למשתמש שלך.

## מטרות הלמידה

בסוף שיעור זה, תהיה מסוגל:

- ליצור לקוח עם LLM.
- לתקשר בצורה חלקה עם שרת MCP באמצעות LLM.
- לספק חוויית משתמש טובה יותר בצד הלקוח.

## גישה

בוא ננסה להבין את הגישה שעלינו לנקוט. הוספת LLM נשמעת פשוטה, אך האם באמת נעשה זאת?

כך הלקוח יתקשר עם השרת:

1. יצירת חיבור עם השרת.

1. רשימת היכולות, ההנחיות, המשאבים והכלים, ושמירת הסכימה שלהם.

1. הוספת LLM והעברת היכולות השמורות והסכימה שלהם בפורמט שה-LLM מבין.

1. טיפול בהנחיית משתמש על ידי העברתה ל-LLM יחד עם הכלים שרשם הלקוח.

מצוין, עכשיו כשאנחנו מבינים איך לעשות זאת ברמה גבוהה, בואו ננסה את זה בתרגיל למטה.

## תרגיל: יצירת לקוח עם LLM

בתרגיל זה נלמד להוסיף LLM ללקוח שלנו.

### אימות באמצעות אסימון גישה אישי של GitHub

יצירת אסימון GitHub היא תהליך פשוט. כך תוכל לעשות זאת:

- עבור להגדרות GitHub – לחץ על תמונת הפרופיל שבפינה הימנית העליונה ובחר ב'הגדרות'.
- עבור להגדרות מפתחים – גלול למטה ולחץ על 'הגדרות מפתחים'.
- בחר באסימוני גישה אישית – לחץ על אסימונים בעלי רמת פירוט ואז צרף אסימון חדש.
- הגדר את האסימון שלך – הוסף הערה לציון, הגדר תאריך תפוגה, ובחר את ההרשאות הנדרשות (סopes). במקרה זה, ודא שהוספת את ההרשאה של Models.
- צור והעתק את האסימון – לחץ על צור אסימון, וודא להעתיק אותו מיד, שכן לא תוכל לראות אותו שוב.

### -1- התחבר לשרת

בוא ניצור קודם את הלקוח שלנו:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ייבוא zod לאימות סכימה

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

בקוד שלמעלה עשינו:

- ייבאנו את הספריות הנדרשות
- יצרנו מחלקה עם שני חברים, `client` ו-`openai` שיעזרו לנו לנהל לקוח ולתקשר עם LLM בהתאמה.
- קונפיגרנו את מופע ה-LLM שלנו להשתמש ב-GitHub Models על ידי הגדרת `baseUrl` שמצביע ל-API של inference.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# צור פרמטרים לשרת עבור חיבור stdio
server_params = StdioServerParameters(
    command="mcp",  # קובץ הרצה
    args=["run", "server.py"],  # ארגומנטים אופציונליים בשורת הפקודה
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

בקוד שלמעלה עשינו:

- ייבאנו את הספריות הנדרשות ל-MCP
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

ראשית, יהיה עליך להוסיף את התלויות של LangChain4j לקובץ `pom.xml` שלך. הוסף תלויות אלו כדי לאפשר אינטגרציה עם MCP ועם MiniMax API התואם ל-OpenAI:

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

הגדר את מפתח ה-MiniMax API שלך, ואופציונלית את נקודת הקצה והמודל.
`MINIMAX_MODEL_ID` תומך ב-`MiniMax-M3` ו-`MiniMax-M2.7`. אם
`OPENAI_BASE_URL` לא מוגדר, `MINIMAX_REGION` תומך ב-`global_en` ו-`cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

כדי לבחור את נקודת הקצה לפי אזור, השמט את `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

אחר כך צור את מחלקת הלקוח שלך ב-Java:

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

        // צור תחבורה MCP לחיבור לשרת
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

בקוד שלמעלה עשינו:

- **הוספנו תלויות LangChain4j**: דרושות לאינטגרציה עם MCP ו-OpenAI-compatible MiniMax API
- **ייבאנו את הספריות של LangChain4j**: לאינטגרציה עם MCP ולפונקציונליות צ'אט מודלי OpenAI
- **יצרנו `ChatLanguageModel`**: הוגדר להשתמש ב-MiniMax עם מפתח ה-MiniMax API שלך, נקודת הקצה ומזהה המודל הנתמך
- **הגדרנו טרטנספורט HTTP**: באמצעות Server-Sent Events (SSE) להתחברות לשרת MCP
- **יצרנו לקוח MCP**: שיטפל בתקשורת עם השרת
- **השתמשנו בתמיכה מובנית של LangChain4j ב-MCP**: שמפשטת את האינטגרציה בין LLM לשרתי MCP

#### Rust

דוגמה זו מניחה שיש לך שרת MCP מבוסס Rust שרץ. אם אין לך כזה, גש חזרה לשיעור [01-first-server](../01-first-server/README.md) כדי ליצור את השרת.

לאחר שיש לך את שרת ה-MCP מבוסס Rust, פתח מסוף ונווט לאותה תיקייה בה נמצא השרת. ואז הרץ את הפקודה הבאה כדי ליצור פרויקט לקוח LLM חדש:

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
> אין ספריית Rust רשמית ל-OpenAI, עם זאת, ה-crate `async-openai` היא [ספרייה שמתוחזקת על ידי הקהילה](https://platform.openai.com/docs/libraries/rust#rust) שנמצאת בשימוש נרחב.

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
    // הודעה ראשונית
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

    // TODO: קבל רשימת כלים של MCP

    // TODO: שיחה של LLM עם קריאות לכלים

    Ok(())
}
```

קוד זה מכין אפליקציית Rust בסיסית שתתחבר לשרת MCP ו-GitHub Models לאינטראקציות עם LLM.

> [!IMPORTANT]
> ודא שהגדרת את משתנה הסביבה `OPENAI_API_KEY` עם אסימון GitHub שלך לפני הרצת האפליקציה.

מצוין, לשלב הבא, נרשום את היכולות בשרת.

### -2- רשימת יכולות של השרת

עכשיו נחבר לשרת ונבקש את היכולות שלו:

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

בקוד שלמעלה עשינו:

- הוספנו קוד להתחברות לשרת, `connectToServer`.
- יצרנו את המתודה `run` שאחראית לזרימת האפליקציה שלנו. עד כה היא רק מציגה את הכלים, אך נוסיף לה עוד בקרוב.

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

אלו הדברים שהוספנו:

- הצגנו משאבים וכלים והדפסנו אותם. עבור כלים רשמנו גם את `inputSchema` ששימש אותנו אחר כך.

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

בקוד שלמעלה עשינו:

- רשמנו את הכלים הזמינים בשרת MCP
- עבור כל כלי, רשמנו שם, תיאור והסכימה שלו. האחרון הוא משהו שנשתמש עליו כדי לקרוא לכלים בקרוב.

#### Java

```java
// ליצור ספק כלי שמגלה באופן אוטומטי כלים של MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ספק הכלים של MCP מטפל אוטומטית ב:
// - רישום כלים זמינים משרת MCP
// - המרת סכימות כלים של MCP לפורמט LangChain4j
// - ניהול ביצוע הכלים והתגובות
```

בקוד שלמעלה עשינו:

- יצירת `McpToolProvider` שמגלה באופן אוטומטי ורושם את כל הכלים משרת MCP
- ספק הכלים מטפל בהמרה בין סכימות הכלים של MCP לפורמט הכלים של LangChain4j באופן פנימי
- גישה זו מסתירה את תהליך רשימת ההכלים וההמרה הידנית

#### Rust

שליפת הכלים משרת MCP מתבצעת באמצעות המתודה `list_tools`. בפונקציית `main` שלך, לאחר שהגדרת את לקוח MCP, הוסף את הקוד הבא:

```rust
// קבל רשימת כלי MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- המרת יכולות השרת לכלי LLM

השלב הבא לאחר רישום היכולות של השרת הוא להמירן לפורמט שה-LLM מבין. ברגע שנעשה זאת, נוכל לספק את היכולות הללו ככלים ל-LLM שלנו.

#### TypeScript

1. הוסף את הקוד הבא להמרת תגובת שרת MCP לפורמט כלי שה-LLM יכול להשתמש בו:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // צור סכמת זוד בהתבסס על ה-input_schema
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

    הקוד שלמעלה לוקח תגובה משרת MCP וממיר אותה לפורמט הגדרת כלי שה-LLM יכול להבין.

2. נעדכן את המתודה `run` כדי לרשום את היכולות של השרת:

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

    בקוד שלמעלה, עדכנו את המתודה `run` כדי למפות את התוצאה ולקרוא ל-`openAiToolAdapter` עבור כל רשומה.

#### Python

1. תחילה, ניצור את פונקציית ההמרה הבאה

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

    בפונקציה `convert_to_llm_tools` שלמעלה, אנו מקבלים תגובת כלי MCP וממירים אותה לפורמט שה-LLM יכול להבין.

2. לאחר מכן נעשה עדכון בקוד הלקוח כדי להשתמש בפונקציה זו כך:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    כאן, אנו מוסיפים קריאה ל-`convert_to_llm_tool` כדי להמיר את תגובת כלי ה-MCP למשהו שנוכל להזין ל-LLM מאוחר יותר.

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

בקוד שלמעלה עשינו:

- יצרנו פונקציה `ConvertFrom` שמקבלת שם, תיאור וסכימת קלט.
- הגדרנו פונקציונליות שיוצרת `FunctionDefinition` שמועברת ל-`ChatCompletionsDefinition`. האחרון הוא משהו שה-LLM יכול להבין.

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

בקוד שלמעלה עשינו:

- הגדרנו ממשק פשוט `Bot` לאינטראקציות בשפה טבעית
- השתמשנו ב-`AiServices` של LangChain4j כדי לקשר באופן אוטומטי את ה-LLM עם ספק הכלים של MCP
- המסגרת מטפלת אוטומטית בהמרת סכימות הכלים והקריאות לפונקציות מאחורי הקלעים
- גישה זו מבטלת המרה ידנית של כלים - LangChain4j מטפל בכל המורכבות של המרת כלים MCP לפורמט שתואם ל-LLM

#### Rust

כדי להמיר את תגובת הכלי של MCP לפורמט שה-LLM יכול להבין, נוסיף פונקציה עזר שמעצבת את רשימת הכלים. הוסף את הקוד הבא לקובץ `main.rs` שלך מתחת לפונקציית `main`. זה יקרא בעת ביצוע בקשות ל-LLM:

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

מצוין, אנחנו מוכנים לטפל בבקשות המשתמש, אז בואו נטפל בזה עכשיו.

### -4- טיפול בבקשת הנחיית משתמש

בחלק הקוד הזה נטפל בבקשות משתמש.

#### TypeScript

1. הוסף מתודה שתשמש לקריאה ל-LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. התקשר לכלי השרת
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. עשה משהו עם התוצאה
        // לביצוע

        }
    }
    ```

    בקוד שלמעלה עשינו:

    - הוספנו מתודה בשם `callTools`.
    - המתודה מקבלת תגובה מ-LLM ובודקת איזה כלים נקראו, אם בכלל:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // לקרוא לכלי
        }
        ```

    - קוראת לכלי, אם ה-LLM מציין שיש לקרוא לו:

        ```typescript
        // 2. לקרוא לכלי של השרת
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. לעשות משהו עם התוצאה
        // יש להשלים
        ```

2. עדכן את המתודה `run` שתכלול קריאות ל-LLM וקריאה ל-`callTools`:

    ```typescript

    // 1. צור הודעות שהן קלט עבור המודל השפתי הגדול
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. קריאה למודל השפתי הגדול
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. סרוק את תגובת המודל השפתי הגדול, עבור כל בחירה, בדוק אם יש קריאות לכלים
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

מצוין, בוא נציג את הקוד במלואו:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ייבא את zod לאימות סכימות

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
          // צור סכימת zod מבוססת על input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // הגדר במפורש את הסוג כ"פונקציה"
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
    
        // 3. עבור על תגובת LLM, עבור כל בחירה, בדוק אם יש קריאות לכלים
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

1. נוסיף כמה ייבוא שדרושים לקריאה ל-LLM

    ```python
    # מודל שפה גדול
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. לאחר מכן נוסיף את הפונקציה שתקריא ל-LLM:

    ```python
    # מודל שפה גדול

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

בקוד שלמעלה עשינו:

- העברנו את הפונקציות שמצאנו בשרת MCP והמרנו ל-LLM.
- לאחר מכן קראנו ל-LLM עם הפונקציות הללו.
- אחר כך בדקנו את התוצאה לראות אילו פונקציות עלינו לקרוא, אם בכלל.
- לבסוף העברנו מערך של פונקציות לקריאה.

3. שלב אחרון, נעדכן את הקוד הראשי שלנו:

    ```python
    prompt = "Add 2 to 20"

    # לשאול את מודל השפה האולטימטיבי אילו כלים יש להשתמש, אם בכלל
    functions_to_call = call_llm(prompt, functions)

    # לקרוא לפונקציות המוצעות
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

שם, זה היה השלב הסופי, בקוד שלמעלה אנו:

- קוראים לכלי MCP דרך `call_tool` באמצעות פונקציה שה-LLM חשב שעלינו לקרוא לה בהתאם להנחיה שלנו.
- מדפיסים את תוצאת הקריאה לכלי לשרת MCP.

#### .NET

1. נראה קוד לביצוע בקשה להנחיית LLM:

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

בקוד שלמעלה עשינו:

- משכנו כלים משרת MCP, `var tools = await GetMcpTools()`.
- הגדרנו הנחיית משתמש `userMessage`.
- בנינו אובייקט אפשרויות שמפרט מודל וכלים.
- ביצענו בקשה ל-LLM.

2. שלב אחרון, נראה אם ה-LLM חושב שעלינו לקרוא לפונקציה:

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

בקוד שלמעלה עשינו:

- עברנו בלולאה על רשימת קריאות לפונקציות.
- עבור כל קריאה לכלי, פרסרנו שם וארגומנטים וקראנו לכלי על שרת MCP באמצעות לקוח MCP. לבסוף הדפסנו את התוצאות.

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
    // ביצוע בקשות בשפה טבעית שמשתמשות בכלי MCP באופן אוטומטי
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

בקוד שלמעלה עשינו:

- השתמשנו בהנחיות בשפה טבעית פשוטה כדי לתקשר עם כלים של שרת MCP
- מסגרת LangChain4j מטפלת באופן אוטומטי ב:
  - המרת ההנחיות של המשתמש לקריאות כלים בעת הצורך
  - קריאת הכלים המתאימים של MCP לפי החלטת ה-LLM
  - ניהול שיחת הדיבור בין ה-LLM לשרת MCP
- המתודה `bot.chat()` מחזירה תשובות בשפה טבעית שיכולות לכלול תוצאות מביצועי כלי MCP
- גישה זו מספקת חוויית משתמש חלקה שבה המשתמשים אינם צריכים לדעת על היישום הפנימי של MCP

דוגמה מלאה של קוד:

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

כאן מתבצע רוב העבודה. נקרא ל-LLM עם ההנחיה הראשונית של המשתמש, אז נעבד את התגובה כדי לבדוק אם יש צורך לקרוא לכלים. אם כן, נקרא לכלים אלו ונמשיך את השיחה עם ה-LLM עד שלא יהיו קריאות כלים נוספות ונקבל תגובה סופית.


אנחנו נעשה מספר קריאות ל-LLM, אז נגדיר פונקציה שתטפל בקריאה ל-LLM. הוסף את הפונקציה הבאה לקובץ `main.rs` שלך:

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

פונקציה זו מקבלת את לקוח ה-LLM, רשימת הודעות (כולל הפקודה מהמשתמש), כלים משרת ה-MCP, ושולחת בקשה ל-LLM, ומחזירה את התגובה.

התגובה מה-LLM תכיל מערך של `choices`. נצטרך לעבד את התוצאה כדי לראות אם קיימים `tool_calls`. זה מראה לנו שה-LLM מבקש להשתמש בכלי מסוים עם פרמטרים. הוסף את הקוד הבא לתחתית קובץ `main.rs` שלך כדי להגדיר פונקציה שתטפל בתגובת ה-LLM:

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

            // הוסף תוצאת כלי להודעות
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // המשך שיחה עם תוצאות כלים
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

אם קיימים `tool_calls`, הפונקציה מחלצת את פרטי הכלי, קוראת לשרת ה-MCP עם בקשת הכלי, ומוסיפה את התוצאות להודעות השיחה. לאחר מכן היא ממשיכה את השיחה עם ה-LLM וההודעות מתעדכנות עם תגובת העוזר ותוצאות קריאות הכלי.

כדי לחלץ את פרטי קריאות הכלי שה-LLM מחזיר עבור קריאות MCP, נוסיף פונקציה עזר נוספת שמחלצת את כל מה שצריך כדי לבצע את הקריאה. הוסף את הקוד הבא לתחתית קובץ `main.rs` שלך:

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

עם כל החלקים במקום, כעת נוכל לטפל בפקודת המשתמש הראשונית ולקרוא ל-LLM. עדכן את פונקציית `main` שלך כך שתכלול את הקוד הבא:

```rust
// שיחה עם מודל שפה גדול הכוללת קריאות לכלים
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

זה ישאל את ה-LLM עם פקודת המשתמש הראשונית המבקשת סכום של שני מספרים, ויעבד את התגובה כדי לטפל בדינמיות בקריאות לכלים.

מצוין, עשית את זה!

## משימה

קח את הקוד מהתרגיל ובנה את השרת עם עוד כלים. לאחר מכן צור לקוח עם LLM, כמו בפתרון, ובדוק אותו עם פקודות שונות כדי לוודא שכל כלי השרת נקראים בצורה דינמית. דרך הבנייה הזו של הלקוח מבטיחה למשתמש סופי חווית משתמש מעולה, משום שהוא יכול להשתמש בפקודות בצורה חופשית, במקום פקודות מדויקות של הלקוח, ולהיות בלתי מודע לכל קריאה לשרת MCP.

## פתרון

[פתרון](./solution/README.md)

## נקודות מפתח

- הוספת LLM ללקוח שלך מספקת דרך טובה יותר למשתמשים לתקשר עם שרתי MCP.
- עליך להמיר את תגובת שרת ה-MCP למשהו שה-LLM יכול להבין.

## דוגמאות

- [מחשבון Java](../samples/java/calculator/README.md)
- [מחשבון .Net](../../../../03-GettingStarted/samples/csharp)
- [מחשבון JavaScript](../samples/javascript/README.md)
- [מחשבון TypeScript](../samples/typescript/README.md)
- [מחשבון Python](../../../../03-GettingStarted/samples/python)
- [מחשבון Rust](../../../../03-GettingStarted/samples/rust)

## משאבים נוספים

## מה הלאה

- הבא: [שימוש בשרת באמצעות Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->