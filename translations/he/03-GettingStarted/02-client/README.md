# יצירת קליינט

קליינטים הם אפליקציות מותאמות אישית או סקריפטים שמתקשרים ישירות עם שרת MCP כדי לבקש משאבים, כלים, והנחות התחלה. בשונה מהשימוש בכלי המפקח שמספק ממשק גרפי לאינטראקציה עם השרת, כתיבת קליינט משלך מאפשרת אינטראקציות פרוגרמטיות ואוטומטיות. זה מאפשר למפתחים לשלב את היכולות של MCP בעבודות שלהם, לאוטומט משימות ולבנות פתרונות מותאמים לפי צרכים ספציפיים.

## סקירה כללית

השיעור הזה מציג את רעיון הקליינטים בתוך מערך הפרוטוקול Model Context Protocol (MCP). תלמד כיצד לכתוב קליינט משלך ולחבר אותו לשרת MCP.

## מטרות הלמידה

בסיום השיעור תוכל:

- להבין מה קליינט יכול לעשות.
- לכתוב קליינט משלך.
- להתחבר ולבחון את הקליינט עם שרת MCP כדי לוודא שהשרת פועל כמצופה.

## מה נדרש בכתיבת קליינט?

כדי לכתוב קליינט, תצטרך לבצע את הפעולות הבאות:

- **ייבוא הספריות הנכונות**. תשתמש באותה ספרייה כמו קודם, אך עם מבנים שונים.
- **אתחול קליינט**. זה יכלול יצירת מופע של קליינט וחיבורו לשיטת התקשורת הנבחרת.
- **החלטה על אילו משאבים לרשום**. לשרת MCP שלך יש משאבים, כלים והנחות התחלה, עליך להחליט איזה מהם לרשום.
- **שילוב הקליינט באפליקציית מארח**. ברגע שאתה יודע אילו יכולות יש לשרת, עליך לשלב את זה באפליקציית המארח כך שאם משתמש יקליד הנחה או פקודה אחרת, תופעל התכונה המתאימה של השרת.

עכשיו כשאנחנו מבינים ברמה גבוהה מה עומדים לעשות, בוא נראה דוגמה בהמשך.

### דוגמת קליינט

בוא נראה דוגמת קליינט זו:

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

// רשימת בקשות
const prompts = await client.listPrompts();

// קבל בקשה
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// רשימת משאבים
const resources = await client.listResources();

// קרא משאב
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// קרא כלי
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

בקוד שלמעלה:

- מייבאים את הספריות
- יוצרים מופע של קליינט ומחברים אותו באמצעות stdio לתקשורת.
- מוצאים רשימה של הנחות התחלה, משאבים וכלים ומפעילים אותם כולם.

הנה לך, קליינט שיכול לתקשר עם שרת MCP.

בתרגיל הבא ניקח את הזמן ונפרק כל קטע קוד ונסביר מה קורה.

## תרגיל: כתיבת קליינט

כמו שנאמר למעלה, ניקח את הזמן להסביר את הקוד, ואתה מוזמן לקודד יחד אם תרצה.

### -1- ייבוא הספריות

בוא נייבא את הספריות שנצטרך, נזדקק להפניות לקליינט ולפרוטוקול התקשורת שבחרנו, stdio. stdio הוא פרוטוקול לדברים שמיועדים לרוץ על המחשב המקומי שלך. SSE הוא פרוטוקול תקשורת נוסף שנראה בפרקים הבאים אך זו אופציה נוספת שלך. לעת עתה נמשיך עם stdio.

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

לג׳אווה, תיצור קליינט שמתחבר לשרת MCP מהתרגיל הקודם. תוך שימוש באותה מבנה פרויקט Java Spring Boot מהקובץ [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), צור מחלקת Java חדשה שנקראת `SDKClient` בתיקיית `src/main/java/com/microsoft/mcp/sample/client/` והוסף את הייבואיות הבאות:

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

תצטרך להוסיף את התלויות הבאות לקובץ `Cargo.toml`.

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

לאחר מכן תוכל לייבא את הספריות הנחוצות בקוד הקליינט שלך.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

נעבור לאתחול.

### -2- אתחול קליינט ופרוטוקול תקשורת

נצטרך ליצור מופע של התקשורת ושל הקליינט:

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

בקוד הנ״ל:

- יצרנו מופע של תקשורת stdio. שים לב שהוא מגדיר פקודת הפעלה וארגומנטים לאיך לאתר ולהפעיל את השרת, כי זה משהו שנצטרך לעשות בזמן יצירת הקליינט.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- אתחלנו קליינט עם שם וגירסה.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- חיברנו את הקליינט לפרוטוקול התקשורת שנבחר.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# צור פרמטרים של שרת לחיבור stdio
server_params = StdioServerParameters(
    command="mcp",  # קובץ הרצה
    args=["run", "server.py"],  # פרמטרים אופציונליים בשורת הפקודה
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

בקוד הנ״ל:

- ייבאנו את הספריות הדרושות
- אתחלנו אובייקט פרמטרים לשרת כדי שנשתמש בו להרצת השרת ולחיבור אליו עם הקליינט.
- הגדרנו פונקציה `run` שקוראת לפעולה `stdio_client` שמתחילה סשן קליינט.
- יצרנו נקודת כניסה שבה מספקים את הפונקציה `run` ל־`asyncio.run`.

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

בקוד הנ״ל:

- ייבאנו את הספריות הדרושות.
- יצרנו תקשורת stdio וקליינט `mcpClient`. האחרון הוא מה שנשתמש בו לרשום ולהפעיל תכונות בשרת MCP.

הערה: בפרמטר "Arguments", אפשר להפנות ל־*.csproj* או לקובץ ההרצה.

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
        
        // הלוגיקה של הלקוח שלך הולכת כאן
    }
}
```

בקוד שלמעלה:

- יצרנו מתודת העיקרית שמגדירה תקשורת SSE שמופנית ל־`http://localhost:8080` שבו שרת MCP שלנו ירוץ.
- יצרנו מחלקת קליינט שתקבל את התקשורת כאובייקט בנאי.
- במתודת `run`, יצרנו קליינט MCP סינכרוני עם התקשורת ואתחלנו את החיבור.
- השתמשנו בתקשורת SSE (Server-Sent Events) המתאימה לתקשורת HTTP עם שרתי MCP מבוססי Java Spring Boot.

#### Rust

שים לב שהקליינט Rust מניח שהשרת הוא פרויקט אחוי בשם "calculator-server" באותה תיקייה. הקוד שלמטה יאתחל את השרת ויתחבר אליו.

```rust
async fn main() -> Result<(), RmcpError> {
    // הנח שהשרת הוא פרויקט אח בשם "calculator-server" באותה תיקיה
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

    // יש להשלים: אתחול

    // יש להשלים: רשימת כלים

    // יש להשלים: קריאה לפונקציית הוספת כלי עם ארגומנטים = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- רישום תכונות השרת

כעת יש לנו קליינט שיכול להתחבר כאשר מריצים את התוכנית. עם זאת, הוא לא מציג את התכונות שלו, אז נעשה זאת עכשיו:

#### TypeScript

```typescript
// רשימת בקשות
const prompts = await client.listPrompts();

// רשימת משאבים
const resources = await client.listResources();

// רשימת כלים
const tools = await client.listTools();
```

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
```

כאן אנו מציגים את המשאבים הזמינים עם `list_resources()` והכלים עם `list_tools` ומדפיסים אותם.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

מעלה דוגמה כיצד לרשום את הכלים בשרת. עבור כל כלי, מדפיסים את שמו.

#### Java

```java
// לרשום ולהדגים כלים
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// אתה יכול גם לשלוח פינג לשרת כדי לאמת את החיבור
client.ping();
```

בקוד שלמעלה:

- קראנו את `listTools()` כדי לקבל את כל הכלים הזמינים בשרת MCP.
- השתמשנו ב־`ping()` כדי לוודא שהחיבור לשרת תקין.
- האובייקט `ListToolsResult` מכיל מידע על כל הכלים כולל שמותיהם, תיאוריהם, וסכימות הקלט.

מצוין, עכשיו אנחנו תופסים את כל התכונות. כעת השאלה היא מתי משתמשים בהן? הקליינט הזה די פשוט, כלומר נצטרך לקרוא במפורש לכל תכונה כשרוצים אותה. בפרק הבא ניצור קליינט מתקדם יותר שיש לו גישה למודל שפה גדול משלו, LLM. בינתיים, נראה איך מפעילים את תכונות השרת:

#### Rust

בפונקציית main, לאחר אתחול הקליינט, ניתן לאתחל את השרת ולרשום כמה מהתכונות שלו.

```rust
// אתחל
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// רשימת כלים
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- הפעלת תכונות

כדי להפעיל תכונות נצטרך לוודא שאנחנו מספקים את הפרמטרים הנכונים ובחלק מהמקרים את שם מה שאנחנו רוצים להפעיל.

#### TypeScript

```typescript

// קרא משאב
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// קרא כלי
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// קרא הנחיה
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

בקוד זה:

- קוראים משאב, בשוליים משתמשים ב־`readResource()` ומציינים `uri`. כך זה כנראה נראה על צד השרת:

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

    ערך ה־`uri` שלנו `file://example.txt` מתאים למחרוזת `file://{name}` על השרת. `example.txt` ימופה כ־`name`.

- קוראים לכלי, קוראים לו על ידי ציון `name` ו־`arguments` כך:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- מקבלים הנחה, כדי לקבל הנחה, קוראים ל־`getPrompt()` עם `name` ו־`arguments`. הקוד בשרת נראה כך:

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

    ולכן הקוד הנוצר בקליינט נראה כך כדי להתאים למה שהוגדר בשרת:

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
# לקרוא משאב
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# לקרוא לכלי
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

בקוד הנ״ל:

- קראנו משאב בשם `greeting` באמצעות `read_resource`.
- הפעלנו כלי בשם `add` באמצעות `call_tool`.

#### .NET

1. נוסיף קוד להפעיל כלי:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. כדי להדפיס את התוצאה, הנה קוד לטיפול בזה:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// קרא לכלים שונים של מחשבון
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

בקוד למעלה:

- קראנו לכלי מחשבון רבים באמצעות מתודת `callTool()` עם אובייקטים של `CallToolRequest`.
- כל קריאת כלי מגדירה את שם הכלי ומפה (Map) של פרמטרים הנדרשים לכלי זה.
- הכלים בשרת מצפים לפרמטרים מסוימים (כמו "a", "b" לפעולות מתמטיות).
- התוצאות מוחזרות כאובייקטים `CallToolResult` המכילים את תגובת השרת.

#### Rust

```rust
// קריאה לכלי הוספה עם ארגומנטים = {"a": 3, "b": 2}
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

### -5- הרצת הקליינט

כדי להריץ את הקליינט, הקלד את הפקודה הבאה בטרמינל:

#### TypeScript

הוסף את הערך הבא לסעיף "scripts" בקובץ *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

הפעל את הקליינט עם הפקודה הבאה:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

ראשית, ודא ששרת MCP שלך רץ בכתובת `http://localhost:8080`. לאחר מכן הפעל את הקליינט:

```bash
# לבנות את הפרויקט שלך
./mvnw clean compile

# להריץ את הלקוח
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

כחלופה, תוכל להריץ את פרויקט הקליינט המלא שבספריית הפתרון `03-GettingStarted\02-client\solution\java`:

```bash
# נווט אל תיקיית הפתרון
cd 03-GettingStarted/02-client/solution/java

# בניתי והרץ את קובץ ה-JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## מטלה

במטלה זו, תשתמש במה שלמדת בכתיבת קליינט ותיצור קליינט משלך.

הנה שרת שתוכל להשתמש בו שעליך לקרוא אליו דרך קוד הקליינט שלך, נסה להוסיף תכונות נוספות לשרת כדי להפוך אותו למעניין יותר.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// צור שרת MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// הוסף כלי נוסף
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// הוסף משאב ברכה דינמי
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

// התחל לקבל הודעות ב-stdin ולשלוח הודעות ב-stdout

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

# צור שרת MCP
mcp = FastMCP("Demo")


# הוסף כלי חיבור
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# הוסף משאב ברכה דינמי
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

ראה את הפרויקט הזה כיצד ניתן [להוסיף הנחות ומשאבים](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

כמו כן, בדוק קישור זה לגבי אופן הפעלת [הנחות ומשאבים](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

ב[הקטע הקודם](../../../../03-GettingStarted/01-first-server) למדת איך ליצור שרת MCP פשוט עם Rust. תוכל להמשיך לבנות עליו או לבדוק קישור זה לדוגמאות נוספות של שרתי MCP מבוססי Rust: [דוגמאות לשרת MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## פתרון

**ספריית הפתרון** מכילה יישומי קליינט מלאים ומוכנים להפעלה שמדגימים את כל הקונספטים שנלמדו במדריך זה. כל פתרון כולל גם קוד קליינט וגם שרת שמאורגנים בפרויקטים נפרדים ובלתי תלויים.

### 📁 מבנה הפתרון

ספריית הפתרון מאורגנת לפי שפת התכנות:

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

### 🚀 מה כל פתרון כולל

כל פתרון ספציפי לשפה מספק:

- **יישום קליינט מלא** עם כל התכונות מהמדריך
- **מבנה פרויקט עובד** עם תלויות והגדרות מתאימות
- **סקריפטים לבנייה והפעלה** להגדרה ותחזוקה קלה
- **קובץ README מפורט** עם הוראות ספציפיות לשפה
- **דוגמאות לטיפול בשגיאות** ועיבוד תוצאות

### 📖 שימוש בפתרונות

1. **עבור לתיקיית השפה המועדפת עליך**:

   ```bash
   cd solution/typescript/    # עבור TypeScript
   cd solution/java/          # עבור Java
   cd solution/python/        # עבור Python
   cd solution/dotnet/        # עבור .NET
   ```

2. **עקוב אחרי הוראות README בכל תיקייה לגבי**:
   - התקנת תלויות
   - בניית הפרויקט
   - הרצת הקליינט

3. **פלט לדוגמה שנראה כך**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

לתיעוד מלא והוראות שלב-אחר-שלב, ראה: **[📖 תיעוד הפתרון](./solution/README.md)**

## 🎯 דוגמאות מלאות

העברנו לידי המשתמש יישומי קליינט מלאים ועובדים עבור כל שפות התכנות שנלמדו במדריך זה. דוגמאות אלו מדגימות את כל הפונקציונליות המתוארת לעיל וניתן להשתמש בהן כהפניות או נקודות התחלה לפרויקטים שלך.

### דוגמאות מלאות זמינות

| שפה | קובץ | תיאור |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | קליינט Java מלא המשתמש בתקשורת SSE עם טיפול שגיאות מקיף |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | קליינט C# מלא המשתמש בתקשורת stdio עם הפעלת שרת אוטומטית |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | קליינט TypeScript מלא עם תמיכה מלאה בפרוטוקול MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | קליינט Python מלא המשתמש בתבניות async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | קליינט Rust מלא המשתמש ב-Tokio להפעלות אסינכרוניות |

כל דוגמה מלאה כוללת:
- ✅ **הקמת חיבור** וטיפול בשגיאות  
- ✅ **גילוי שרת** (כלים, משאבים, תזכורות לפי הצורך)  
- ✅ **פעולות מחשבון** (חיבור, חיסור, כפל, חילוק, עזרה)  
- ✅ **עיבוד תוצאות** ופלט מעוצב  
- ✅ **טיפול כולל בשגיאות**  
- ✅ **קוד נקי ומתועד** עם הערות שלב-אחר-שלב  

### התחלה עם דוגמאות מלאות  

1. **בחר את שפתך המועדפת** מתוך הטבלה לעיל  
2. **עיין בקובץ הדוגמה המלאה** כדי להבין את מימוש התכונה במלואה  
3. **הרץ את הדוגמה** לפי ההוראות ב-[`complete_examples.md`](./complete_examples.md)  
4. **שנה והרחב** את הדוגמה לצרכיך הספציפיים  

לתיעוד מפורט על הרצה והתאמה אישית של הדוגמאות הללו, ראה: **[📖 תיעוד דוגמאות מלאות](./complete_examples.md)**  

### 💡 פתרון מול דוגמאות מלאות  

| **תיקיית הפתרון** | **דוגמאות מלאות** |  
|--------------------|--------------------- |  
| מבנה פרויקט מלא עם קבצי בנייה | מימושים בקובץ אחד |  
| מוכן להפעלה עם תלותים | דוגמאות קוד ממוקדות |  
| התקנה בסגנון ייצור | הפניה חינוכית |  
| כלים ספציפיים לשפה | השוואה בין שפות |  

שני הגישות בעלות ערך - השתמש ב**תיקיית הפתרון** לפרויקטים מלאים וב**דוגמאות המלאות** ללמידה ולהפניה.  

## נקודות מפתח  

הנקודות המרכזיות לפרק זה לגבי לקוחות הן:  

- יכולים לשמש גם לגילוי וגם להנעת תכונות בשרת.  
- יכולים להפעיל שרת בעת שהם עצמם מתחילים (כמו בפרק זה) אך גם יכולים להתחבר לשרתים שרצים כבר.  
- דרך מצוינת לבדוק יכולות שרת ליד חלופות כמו Inspector שתואר בפרק הקודם.  

## משאבים נוספים  

- [בניית לקוחות ב-MCP](https://modelcontextprotocol.io/quickstart/client)  

## דוגמאות  

- [מחשבון Java](../samples/java/calculator/README.md)  
- [מחשבון .Net](../../../../03-GettingStarted/samples/csharp)  
- [מחשבון JavaScript](../samples/javascript/README.md)  
- [מחשבון TypeScript](../samples/typescript/README.md)  
- [מחשבון Python](../../../../03-GettingStarted/samples/python)  
- [מחשבון Rust](../../../../03-GettingStarted/samples/rust)  

## מה הלאה  

- הלאה: [יצירת לקוח עם LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור מהווה את המקור הרשמי והמוסמך. למידע קריטי מומלץ לבצע תרגום מקצועי על ידי אדם. אנו לא אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->