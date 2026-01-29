# יצירת לקוח עם LLM

עד כה, ראית כיצד ליצור שרת ולקוח. הלקוח היה מסוגל לקרוא לשרת במפורש כדי לרשום את הכלים, המשאבים וההנחיות שלו. עם זאת, זו לא גישה מאוד פרקטית. המשתמש שלך חי בעידן הסוכני ומצפה להשתמש בהנחיות ולתקשר עם LLM כדי לעשות זאת. עבור המשתמש שלך, לא משנה אם אתה משתמש ב-MCP או לא לאחסן את היכולות שלך, אבל הם כן מצפים להשתמש בשפה טבעית כדי לתקשר. אז איך פותרים את זה? הפתרון הוא להוסיף LLM ללקוח.

## סקירה כללית

בשיעור זה נתמקד בהוספת LLM ללקוח שלך ונראה כיצד זה מספק חוויית משתמש טובה יותר.

## מטרות הלמידה

בסוף שיעור זה, תוכל:

- ליצור לקוח עם LLM.
- לתקשר בצורה חלקה עם שרת MCP באמצעות LLM.
- לספק חוויית משתמש טובה יותר בצד הלקוח.

## גישה

בוא ננסה להבין את הגישה שעלינו לנקוט. הוספת LLM נשמעת פשוטה, אבל האם באמת נעשה זאת?

כך הלקוח יתקשר עם השרת:

1. יצירת חיבור עם השרת.

1. רשימת היכולות, ההנחיות, המשאבים והכלים, ושמירת הסכמה שלהם.

1. הוספת LLM והעברת היכולות השמורות והסכמה שלהם בפורמט שה-LLM מבין.

1. טיפול בהנחיית משתמש על ידי העברתה ל-LLM יחד עם הכלים שרשומים על ידי הלקוח.

מעולה, עכשיו כשאנחנו מבינים איך לעשות זאת ברמה גבוהה, בוא ננסה זאת בתרגיל למטה.

## תרגיל: יצירת לקוח עם LLM

בתרגיל זה, נלמד להוסיף LLM ללקוח שלנו.

### אימות באמצעות אסימון גישה אישי של GitHub

יצירת אסימון GitHub היא תהליך פשוט. כך תוכל לעשות זאת:

- עבור להגדרות GitHub – לחץ על תמונת הפרופיל שלך בפינה הימנית העליונה ובחר בהגדרות.
- נווט להגדרות מפתח – גלול למטה ולחץ על הגדרות מפתח.
- בחר באסימוני גישה אישית – לחץ על אסימונים מדויקים ואז צור אסימון חדש.
- הגדר את האסימון שלך – הוסף הערה להתייחסות, הגדר תאריך תפוגה, ובחר את ההרשאות הנדרשות. במקרה זה, ודא להוסיף את הרשאת Models.
- צור והעתק את האסימון – לחץ על צור אסימון, וודא להעתיק אותו מיד, כיוון שלא תוכל לראות אותו שוב.

### -1- התחבר לשרת

בוא ניצור את הלקוח שלנו תחילה:

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
- הגדרנו את מופע ה-LLM שלנו להשתמש ב-GitHub Models על ידי הגדרת `baseUrl` שמצביע ל-API של האינפרנס.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# צור פרמטרים של שרת לחיבור stdio
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
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

#### Java

ראשית, תצטרך להוסיף את התלויות של LangChain4j לקובץ `pom.xml` שלך. הוסף את התלויות האלה כדי לאפשר אינטגרציה עם MCP ותמיכה ב-GitHub Models:

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

לאחר מכן צור את מחלקת הלקוח שלך ב-Java:

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
    
    public static void main(String[] args) throws Exception {        // הגדר את ה-LLM לשימוש במודלים של GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
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
}
```

בקוד שלמעלה עשינו:

- **הוספנו את תלויות LangChain4j**: נדרשות לאינטגרציה עם MCP, לקוח רשמי של OpenAI, ותמיכה ב-GitHub Models
- **ייבאנו את ספריות LangChain4j**: לאינטגרציה עם MCP ולפונקציונליות של מודל שיחה OpenAI
- **יצרנו `ChatLanguageModel`**: מוגדר להשתמש ב-GitHub Models עם אסימון ה-GitHub שלך
- **הגדרנו תחבורה HTTP**: באמצעות Server-Sent Events (SSE) להתחבר לשרת MCP
- **יצרנו לקוח MCP**: שיטפל בתקשורת עם השרת
- **השתמשנו בתמיכה המובנית של LangChain4j ב-MCP**: שמפשטת את האינטגרציה בין LLM לשרתי MCP

#### Rust

דוגמה זו מניחה שיש לך שרת MCP מבוסס Rust פועל. אם אין לך אחד, עיין שוב בשיעור [01-first-server](../01-first-server/README.md) כדי ליצור את השרת.

לאחר שיש לך את שרת ה-MCP מבוסס Rust, פתח טרמינל ונווט לתיקייה שבה נמצא השרת. לאחר מכן הרץ את הפקודה הבאה כדי ליצור פרויקט לקוח LLM חדש:

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
> אין ספריית Rust רשמית ל-OpenAI, עם זאת, ה-crate `async-openai` היא [ספרייה שמנוהלת על ידי הקהילה](https://platform.openai.com/docs/libraries/rust#rust) שנמצאת בשימוש נפוץ.

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

    // TODO: קבלת רשימת כלים של MCP

    // TODO: שיחה עם LLM עם קריאות לכלים

    Ok(())
}
```

קוד זה מגדיר אפליקציית Rust בסיסית שתתחבר לשרת MCP ול-GitHub Models לאינטראקציות עם LLM.

> [!IMPORTANT]
> ודא להגדיר את משתנה הסביבה `OPENAI_API_KEY` עם אסימון ה-GitHub שלך לפני הרצת האפליקציה.

מעולה, לשלב הבא, בוא נרשום את היכולות בשרת.

### -2- רשום את היכולות של השרת

כעת נתחבר לשרת ונבקש את היכולות שלו:

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
- יצרנו מתודה `run` שאחראית על ניהול זרימת האפליקציה שלנו. עד כה היא רק רושמת את הכלים אך נוסיף לה עוד בקרוב.

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

הנה מה שהוספנו:

- רשימת משאבים וכלים והדפסתם. עבור כלים גם רשמנו את `inputSchema` שנשתמש בו מאוחר יותר.

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
- עבור כל כלי, רשמנו שם, תיאור והסכמה שלו. האחרון הוא משהו שנשתמש בו כדי לקרוא לכלים בקרוב.

#### Java

```java
// צור ספק כלים שמגלה אוטומטית כלים של MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// ספק הכלים של MCP מטפל אוטומטית ב:
// - רישום כלים זמינים משרת MCP
// - המרת סכימות כלים של MCP לפורמט LangChain4j
// - ניהול ביצוע הכלים והתגובות
```

בקוד שלמעלה עשינו:

- יצרנו `McpToolProvider` שמגלה ומרשם אוטומטית את כל הכלים משרת MCP
- ספק הכלים מטפל בהמרה בין סכמות הכלים של MCP לפורמט הכלים של LangChain4j באופן פנימי
- גישה זו מסתירה את תהליך רישום הכלים וההמרה הידנית

#### Rust

שליפת כלים משרת MCP נעשית באמצעות המתודה `list_tools`. בפונקציית `main` שלך, לאחר שהגדרת את לקוח ה-MCP, הוסף את הקוד הבא:

```rust
// קבל רשימת כלי MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- המרת היכולות של השרת לכלי LLM

השלב הבא לאחר רישום היכולות של השרת הוא להמיר אותן לפורמט שה-LLM מבין. ברגע שנעשה זאת, נוכל לספק את היכולות האלה ככלים ל-LLM שלנו.

#### TypeScript

1. הוסף את הקוד הבא להמרת תגובת שרת MCP לפורמט כלי שה-LLM יכול להשתמש בו:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // צור סכמת זוד המבוססת על input_schema
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

    הקוד שלמעלה לוקח תגובה משרת MCP וממיר אותה להגדרת כלי שה-LLM יכול להבין.

1. בוא נעדכן את המתודה `run` כדי לרשום את היכולות של השרת:

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

    בקוד שלמעלה, עדכנו את המתודה `run` כדי למפות את התוצאה ולקרוא עבור כל פריט ל-`openAiToolAdapter`.

#### Python

1. ראשית, ניצור את פונקציית ההמרה הבאה

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

    בפונקציה `convert_to_llm_tools` שלמעלה אנו לוקחים תגובת כלי MCP וממירים אותה לפורמט שה-LLM יכול להבין.

1. לאחר מכן, נעדכן את קוד הלקוח שלנו כדי להשתמש בפונקציה זו כך:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    כאן, אנו מוסיפים קריאה ל-`convert_to_llm_tool` כדי להמיר את תגובת כלי MCP למשהו שנוכל להזין ל-LLM מאוחר יותר.

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

- יצרנו פונקציה `ConvertFrom` שלוקחת שם, תיאור וסכמת קלט.
- הגדרנו פונקציונליות שיוצרת `FunctionDefinition` שמועברת ל-`ChatCompletionsDefinition`. האחרון הוא משהו שה-LLM יכול להבין.

1. בוא נראה איך נעדכן קוד קיים כדי לנצל את הפונקציה הזו:

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

// הגדר את שירות ה-AI עם כלים LLM ו-MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

בקוד שלמעלה עשינו:

- הגדרנו ממשק פשוט `Bot` לאינטראקציות בשפה טבעית
- השתמשנו ב-`AiServices` של LangChain4j כדי לקשר אוטומטית את ה-LLM עם ספק הכלים של MCP
- המסגרת מטפלת אוטומטית בהמרת סכמות הכלים וקריאת פונקציות מאחורי הקלעים
- גישה זו מבטלת את הצורך בהמרת כלים ידנית - LangChain4j מטפל בכל המורכבות של המרת כלים מ-MCP לפורמט תואם LLM

#### Rust

כדי להמיר את תגובת כלי MCP לפורמט שה-LLM יכול להבין, נוסיף פונקציית עזר שמעצבנת את רשימת הכלים. הוסף את הקוד הבא לקובץ `main.rs` שלך מתחת לפונקציית `main`. פונקציה זו תיקרא בעת ביצוע בקשות ל-LLM:

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

מעולה, אנחנו מוכנים לטפל בבקשות משתמש, אז בוא נטפל בזה עכשיו.

### -4- טיפול בבקשת הנחיית משתמש

בחלק זה של הקוד נטפל בבקשות משתמש.

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


        // 2. לקרוא לכלי של השרת
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. לעשות משהו עם התוצאה
        // יש לעשות

        }
    }
    ```

    בקוד שלמעלה:

    - הוספנו מתודה `callTools`.
    - המתודה מקבלת תגובת LLM ובודקת אילו כלים נקראו, אם בכלל:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // קריאת כלי
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
        // יש לעשות
        ```

1. עדכן את המתודה `run` לכלול קריאות ל-LLM וקריאה ל-`callTools`:

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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. עבור על תגובת ה-LLM, עבור כל אפשרות, בדוק אם יש קריאות לכלים
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

מעולה, בוא נציג את הקוד במלואו:

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
          // צור סכימת zod המבוססת על input_schema
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. עבור על תגובת ה-LLM, עבור כל אפשרות, בדוק אם יש קריאות לכלים
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

1. לאחר מכן, נוסיף את הפונקציה שתקריא ל-LLM:

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
    - לאחר מכן, בודקים את התוצאה כדי לראות אילו פונקציות יש לקרוא, אם בכלל.
    - לבסוף, מעבירים מערך של פונקציות לקריאה.

1. שלב סופי, נעדכן את הקוד הראשי שלנו:

    ```python
    prompt = "Add 2 to 20"

    # לשאול את ה-LLM אילו כלים להשתמש, אם בכלל
    functions_to_call = call_llm(prompt, functions)

    # לקרוא לפונקציות המוצעות
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    זהו, זה היה השלב הסופי, בקוד שלמעלה אנו:

    - קוראים לכלי MCP דרך `call_tool` באמצעות פונקציה שה-LLM חשב שצריך לקרוא לה בהתבסס על ההנחיה שלנו.
    - מדפיסים את תוצאת הקריאה לכלי לשרת MCP.

#### .NET

1. נציג קוד לביצוע בקשת הנחיה ל-LLM:

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
        Model = "gpt-4o-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    בקוד שלמעלה עשינו:

    - שלפנו כלים משרת MCP, `var tools = await GetMcpTools()`.
    - הגדרנו הנחיית משתמש `userMessage`.
    - בנינו אובייקט אפשרויות שמציין מודל וכלים.
    - ביצענו בקשה ל-LLM.

1. שלב אחרון, נראה אם ה-LLM חושב שצריך לקרוא לפונקציה:

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

    - עברנו בלולאה על רשימת קריאות פונקציות.
    - עבור כל קריאת כלי, פרשנו שם וארגומנטים וקראנו לכלי בשרת MCP באמצעות לקוח MCP. לבסוף הדפסנו את התוצאות.

הנה הקוד במלואו:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

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
    Model = "gpt-4o-mini",
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

    Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // בצע בקשות בשפה טבעית שמשתמשות בכלי MCP באופן אוטומטי
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

- השתמשנו בהנחיות שפה טבעית פשוטות כדי לתקשר עם כלים של שרת MCP
- מסגרת LangChain4j מטפלת אוטומטית ב:
  - המרת הנחיות משתמש לקריאות כלים כשצריך
  - קריאת הכלים המתאימים של MCP על פי החלטת ה-LLM
  - ניהול זרימת השיחה בין ה-LLM לשרת MCP
- המתודה `bot.chat()` מחזירה תגובות בשפה טבעית שעשויות לכלול תוצאות מביצועי כלים של MCP
- גישה זו מספקת חוויית משתמש חלקה שבה המשתמשים אינם צריכים לדעת על המימוש הפנימי של MCP

דוגמת קוד מלאה:

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

כאן מתבצע רוב העבודה. נקרא ל-LLM עם הנחיית המשתמש הראשונית, ואז נעבד את התגובה כדי לראות אם יש צורך לקרוא לכלים. אם כן, נקרא לכלים אלה ונמשיך את השיחה עם ה-LLM עד שלא נדרשות עוד קריאות כלים ויש לנו תגובה סופית.

נבצע קריאות מרובות ל-LLM, אז נגדיר פונקציה שתטפל בקריאת ה-LLM. הוסף את הפונקציה הבאה לקובץ `main.rs` שלך:

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

פונקציה זו מקבלת את לקוח ה-LLM, רשימת הודעות (כולל הנחיית המשתמש), כלים משרת MCP, ושולחת בקשה ל-LLM, ומחזירה את התגובה.
התשובה מה-LLM תכיל מערך של `choices`. נצטרך לעבד את התוצאה כדי לבדוק אם קיימים `tool_calls`. זה מאפשר לנו לדעת שה-LLM מבקש שיקראו לכלי ספציפי עם ארגומנטים. הוסף את הקוד הבא לתחתית הקובץ `main.rs` שלך כדי להגדיר פונקציה לטיפול בתשובת ה-LLM:

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

    // טיפול בקריאות כלים
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // הוסף הודעת עוזר

        // בצע כל קריאת כלי
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

        // המשך שיחה עם תוצאות הכלי
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

אם קיימים `tool_calls`, הפונקציה תחלץ את מידע הכלי, תקרא לשרת MCP עם בקשת הכלי, ותוסיף את התוצאות להודעות השיחה. לאחר מכן היא ממשיכה את השיחה עם ה-LLM וההודעות מתעדכנות עם תגובת העוזר ותוצאות קריאת הכלי.

כדי לחלץ מידע על קריאת כלי שה-LLM מחזיר עבור קריאות MCP, נוסיף פונקציית עזר נוספת שתחלץ את כל מה שצריך כדי לבצע את הקריאה. הוסף את הקוד הבא לתחתית הקובץ `main.rs` שלך:

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

עם כל החלקים במקום, כעת נוכל לטפל בהנחיית המשתמש הראשונית ולקרוא ל-LLM. עדכן את פונקציית `main` שלך לכלול את הקוד הבא:

```rust
// שיחה עם LLM הכוללת קריאות לכלים
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

זה ישאל את ה-LLM עם הנחיית המשתמש הראשונית המבקשת את סכום שני מספרים, ויעבד את התגובה כדי לטפל בצורה דינמית בקריאות לכלים.

מעולה, עשית את זה!

## משימה

קח את הקוד מהתרגיל ובנה את השרת עם עוד כלים. לאחר מכן צור לקוח עם LLM, כמו בתרגיל, ובדוק אותו עם הנחיות שונות כדי לוודא שכל הכלים בשרת שלך נקראים בצורה דינמית. דרך בניית הלקוח הזו מבטיחה למשתמש קצה חוויית משתמש מצוינת, כי הוא יכול להשתמש בהנחיות במקום פקודות מדויקות של הלקוח, ולהיות לא מודע לקריאות כלשהן לשרת MCP.

## פתרון

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## נקודות מפתח

- הוספת LLM ללקוח שלך מספקת דרך טובה יותר למשתמשים לתקשר עם שרתי MCP.
- יש להמיר את תגובת שרת MCP למשהו שה-LLM יכול להבין.

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
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->