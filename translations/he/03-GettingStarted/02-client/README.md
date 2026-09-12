# יצירת לקוח

לקוחות הם אפליקציות או סקריפטים מותאמים אישית התקשורת ישירות עם שרת MCP כדי לבקש משאבים, כלים והנחיות. בניגוד לשימוש בכלי הבודק, המספק ממשק גרפי לאינטראקציה עם השרת, כתיבת לקוח משלך מאפשרת אינטראקציות מתוכנתות ואוטומטיות. זה מאפשר למפתחים לשלב את יכולות MCP בתהליכי העבודה שלהם, לאוטומט משימות ולבנות פתרונות מותאמים אישית לצרכים ספציפיים.

## סקירה כללית

שיעור זה מציג את מושג הלקוחות בתוך מערכת פרוטוקול הקונטקסט למודל (MCP). תלמדו כיצד לכתוב לקוח משלכם ולחברו לשרת MCP.

## מטרות הלמידה

בסיום שיעור זה, תדעו:

- להבין מה יכול לעשות לקוח.
- לכתוב לקוח משלכם.
- להתחבר ולבדוק את הלקוח עם שרת MCP כדי לוודא שהאחרון פועל כמצופה.

## מה נדרש בכתיבת לקוח?

לצורך כתיבת לקוח, תצטרכו לעשות את הפעולות הבאות:

- **ייבא את הספריות הנכונות**. תשתמשו באותה ספריה כמו קודם, רק מבנים שונים.
- **אתחל לקוח**. זה יכלול יצירת מופע לקוח וחיבורו לשיטת ההעברה הנבחרת.
- **החליטו אילו משאבים לרשום**. בשרת MCP שלכם יש משאבים, כלים והנחיות, אתם צריכים להחליט אילו מהם לרשום.
- **שלבו את הלקוח באפליקציית מארחת**. ברגע שאתם יודעים את יכולות השרת, עליכם לשלב זאת באפליקציית המארח שלכם כדי שאם משתמש מקליד הנחיה או פקודה אחרת, תוקרא התכונה המתאימה בשרת.

כעת כשאנחנו מבינים ברמה גבוהה מה עומדים לעשות, בואו נסתכל על דוגמה בהמשך.

### דוגמת לקוח

בואו נבחן דוגמת לקוח זו:

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

// השג בקשה
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

// הפעל כלי
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

בקוד שלפני כן:

- ייבאנו את הספריות
- יצרנו מופע של לקוח וחיברנו אותו באמצעות stdio כהעברה.
- רשמנו הנחיות, משאבים וכלים והפעלנו את כולם.

הנה לכם, לקוח שיכול לדבר עם שרת MCP.

בואו נקדיש זמן בחלק התרגיל הבא ונפרק כל קטע קוד ונסביר מה מתרחש.

## תרגיל: כתיבת לקוח

כפי שנאמר למעלה, בואו נקדיש זמן להסבר הקוד, ותחושת חופשי לכתוב לצדנו אם תרצו.

### -1- ייבוא הספריות

נייבא את הספריות הנחוצות, נצטרך הפניות ללקוח ולפרוטוקול ההעברה שבחרנו, stdio. stdio הוא פרוטוקול לדברים שנועדו לרוץ על המחשב המקומי שלכם. SSE הוא פרוטוקול העברה אחר שנציג בפרקים הבאים אך זו האופציה השנייה שלכם. לעת עתה, נמשיך עם stdio.

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

עבור Java, תיצרו לקוח שמתחבר לשרת MCP מהתרגיל הקודם. השתמשו במבנה פרויקט Java Spring Boot זהה להוראות [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), צרו כיתה חדשה בשם `SDKClient` בתיקייה `src/main/java/com/microsoft/mcp/sample/client/` והוסיפו את הייבוא הבא:

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

תצטרכו להוסיף את התלויות הבאות בקובץ `Cargo.toml` שלכם.

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

משם תוכלו לייבא את הספריות הנחוצות לקוד הלקוח שלכם.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

נמשיך לאתחול.

### -2- אתחול לקוח והעברה

נצטרך ליצור מופע של ההעברה ושל הלקוח שלנו:

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

בקוד שלפני כן:

- יצרנו מופע של stdio transport. שימו לב כיצד הוא מגדיר פקודה וארגומנטים כדי לאתר ולהפעיל את השרת כי זה משהו שנצטרך לעשות כשניצור את הלקוח.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- אתחלנו לקוח בכך שנתנו לו שם וגרסה.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- חיברנו את הלקוח למעבר הנבחר.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# צור פרמטרים של שרת עבור חיבור stdio
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

בקוד שלפני כן:

- ייבאנו את הספריות הנחוצות.
- אתחלנו אובייקט פרמטרים של שרת כי נשתמש בו להפעלת השרת כך שנוכל להתחבר אליו עם הלקוח שלנו.
- הגדרנו מתודה `run` שקוראת `stdio_client` שמפעילה מושב לקוח.
- יצרנו נקודת כניסה שבה אנו מספקים את המתודה `run` ל-`asyncio.run`.

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

בקוד שלפני כן:

- ייבאנו את הספריות הנחוצות.
- יצרנו stdio transport ויצרנו לקוח `mcpClient`. האחרון הוא משהו שנשתמש בו כדי לרשום ולהפעיל תכונות על שרת MCP.

שימו לב, ב-"Arguments", ניתן לציין את קובץ ה-*.csproj* או את הקובץ הניתן להרצה.

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

בקוד שלפני כן:

- יצרנו מתודה ראשית שמכינה SSE transport המכוון ל-`http://localhost:8080` שבו שרת MCP שלנו ירוץ.
- יצרנו מחלקת לקוח שלוקחת את ההעברה כפרמטר בבנאי.
- במתודה `run`, יצרנו לקוח MCP סינכרוני באמצעות ההעברה ואתחלנו את החיבור.
- השתמשנו ב-SSE (Server-Sent Events) כפרוטוקול תקשורת מבוסס HTTP המתאים לשרתי MCP של Java Spring Boot.

#### Rust

שימו לב כי לקוח Rust זה מניח שהשרת הוא פרויקט אח של בשם "calculator-server" באותה ספרייה. הקוד למטה יאתחל את השרת ויתחבר אליו.

```rust
async fn main() -> Result<(), RmcpError> {
    // הנח שהשרת הוא פרויקט אחים בשם "calculator-server" באותה תיקייה
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

    // עוד לבצע: אתחול

    // עוד לבצע: רישום כלים

    // עוד לבצע: קריאה לפונקציית הוספת כלים עם ארגומנטים = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- רשימת תכונות השרת

עכשיו יש לנו לקוח שיכול להתחבר אם התוכנית תרוץ. עם זאת, הוא לא באמת מציג את התכונות שלו, אז בואו נעשה זאת עכשיו:

#### TypeScript

```typescript
// רשום הנחיות
const prompts = await client.listPrompts();

// רשום משאבים
const resources = await client.listResources();

// רשום כלים
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

כאן אנו מרשימים את המשאבים הזמינים, `list_resources()` והכלים, `list_tools` ומדפיסים אותם.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

למעלה דוגמה כיצד ניתן לרשום את הכלים בשרת. עבור כל כלי, אנו מדפיסים את שמו.

#### Java

```java
// רשום והדגם כלים
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// ניתן גם לשלוח פינג לשרת כדי לאמת את החיבור
client.ping();
```

בקוד שלפני כן:

- קראנו ל-`listTools()` כדי לקבל את כל הכלים הזמינים מהשרת MCP.
- השתמשנו ב-`ping()` כדי לוודא שהחיבור לשרת פועל.
- ה-`ListToolsResult` מכיל מידע על כל הכלים כולל שמותיהם, תיאורים, וסכימות קלט.

מצוין, כעת רשמנו את כל התכונות. עכשיו השאלה מתי משתמשים בהן? טוב, לקוח זה פשוט למדי, פשוט במובן שנצטרך לקרוא במפורש לתכונות כשנרצה אותן. בפרק הבא, ניצור לקוח מתוחכם יותר שיש לו גישה למודל שפה גדול משלו, LLM. לעת עתה, נראה כיצד להפעיל את התכונות על השרת:

#### Rust

בפונקציית הראשית, לאחר אתחול הלקוח, נוכל לאתחל את השרת ולרשום חלק מהתכונות שלו.

```rust
// לאתחל
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// למיין כלים
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- הפעלת תכונות

כדי להפעيل את התכונות, עלינו לוודא שאנו מגדירים את הארגומנטים הנכונים ובחלק מהמקרים את השם של מה שאנו מנסים להפעיל.

#### TypeScript

```typescript

// קרא משאב
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// פנה לכלי
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// פנה להנחיה
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

בקוד שלפני כן:

- קראנו משאב, אנו קוראים למשאב על ידי קריאה ל-`readResource()` ומגדירים `uri`. כך זה כנראה נראה בצד השרת:

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

    הערך שלנו `uri` הוא `file://example.txt` תואם ל-`file://{name}` בשרת. `example.txt` יתאים ל-`name`.

- קריאה לכלי, אנו קוראים לו על ידי הגדרת שמו וארגומנטיו כך:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- קבלת הנחיה, כדי לקבל הנחיה, קוראים ל-`getPrompt()` עם `name` ו-`arguments`. קוד השרת נראה כך:

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

    לכן קוד הלקוח שנוצר נראה כך להתאמה למה שהוצהר בשרת:

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

בקוד שלפני כן:

- קראנו למשאב בשם `greeting` באמצעות `read_resource`.
- הפעלנו כלי בשם `add` באמצעות `call_tool`.

#### .NET

1. נוסיף קוד לקריאה לכלי:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. כדי להדפיס את התוצאה, הנה קוד לעשות זאת:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// קרא לכלי מחשבון שונים
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

בקוד שלפני כן:

- קראנו לכלי מחשבון מרובים באמצעות מתודת `callTool()` עם אובייקטים מסוג `CallToolRequest`.
- כל קריאה לכלי מגדירה את שם הכלי ומפה (Map) של ארגומנטים הנדרשים לכלי זה.
- כלים בשרת מצפים לשמות פרמטרים ספציפיים (כגון "a", "b" לפעולות מתמטיות).
- התוצאות מוחזרות כאובייקטים מסוג `CallToolResult` המכילים את התגובה מהשרת.

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

### -5- הרצת הלקוח

כדי להריץ את הלקוח, הקלד את הפקודה הבאה בטרמינל:

#### TypeScript

הוסף את הכניסה הבאה לקטע "scripts" ב-*package.json* שלך:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

קרא ללקוח עם הפקודה הבאה:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

קודם וודא ששרת MCP שלך רץ ב-`http://localhost:8080`. לאחר מכן הרץ את הלקוח:

```bash
# בנה את הפרויקט שלך
./mvnw clean compile

# הפעל את הלקוח
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

بدיל כך, תוכל להריץ את פרויקט הלקוח המלא המסופק בתיקיית הפתרון `03-GettingStarted\02-client\solution\java`:

```bash
# עבור לתיקיית הפתרון
cd 03-GettingStarted/02-client/solution/java

# בנה והרץ את הקובץ JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## מטלה

במטלה זו, תשתמשו במה שלמדתם ביצירת לקוח אך תיצרו לקוח משלכם.

הנה שרת שבו ניתן להשתמש שעליכם לקרוא אליו בקוד הלקוח שלכם, נסו להוסיף לשרת תכונות נוספות כדי להפוך אותו למעניין יותר.

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

// התחל לקבל הודעות מהקלט הסטנדרטי ולשלוח הודעות לפלט הסטנדרטי

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

# יצירת שרת MCP
mcp = FastMCP("Demo")


# הוסף כלי חיבור
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# הוסף משאב ברכה דינמית
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

עיינו בפרויקט זה כדי לראות כיצד ניתן [להוסיף הנחיות ומשאבים](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

כמו כן, בדקו קישור זה לדרך ההתנהגות של [הנחיות ומשאבים](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

ב-[החלק הקודם](../../../../03-GettingStarted/01-first-server), למדת כיצד ליצור שרת MCP פשוט ב-Rust. ניתן להמשיך לבנות עליו או לבדוק קישור זה לדוגמאות שרת MCP מבוססות Rust נוספות: [דוגמאות שרת MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## פתרון

תיקיית **הפתרון** מכילה מימושים מלאים של לקוחות מוכנים להפעלה המדגימים את כל המושגים שנלמדו במדריך זה. כל פתרון כולל קוד לקוח ושרת, מאורגן בפרויקטים נפרדים ועצמאיים.

### 📁 מבנה הפתרון

הספרייה של הפתרון מאורגנת לפי שפת תכנות:

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

- **מימוש לקוח מלא** עם כל התכונות מהמדריך
- **מבנה פרויקט תקין** עם תלות והגדרות נכונות
- **סקריפטים לבנייה והרצה** להקמה והפעלה פשוטות
- **קובץ README מפורט** עם הוראות ספציפיות לשפה
- **דוגמאות לטיפול בשגיאות** ועיבוד תוצאות

### 📖 שימוש בפתרונות

1. **נווטו לתיקיית השפה המועדפת עליכם**:

   ```bash
   cd solution/typescript/    # עבור TypeScript
   cd solution/java/          # עבור Java
   cd solution/python/        # עבור Python
   cd solution/dotnet/        # עבור .NET
   ```

2. **עקבו אחרי הוראות ה-README** בכל תיקייה עבור:
- התקנת תלויות
- בניית הפרויקט
- הרצת הלקוח

3. **פלט לדוגמה** שצריכים לראות:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

לתיעוד מלא ולהוראות שלב אחר שלב, ראו: **[📖 תיעוד הפתרון](./solution/README.md)**

## 🎯 דוגמאות מלאות

סיפקנו מימושים מלאים ועובדים של לקוחות לכל שפות התכנות שנלמדו במדריך זה. דוגמאות אלו מדגימות את כל הפונקציונליות שהוצגה למעלה וניתן להשתמש בהן כהתייחסות או נקודת התחלה לפרויקטים שלכם.

### דוגמאות מלאות זמינות

| שפה | קובץ | תיאור |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | לקוח Java מלא המשתמש ב-SSE transport עם טיפול שגיאות מקיף |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | לקוח C# מלא המשתמש ב-stdio transport עם הפעלת שרת אוטומטית |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | לקוח TypeScript מלא עם תמיכה מלאה בפרוטוקול MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | לקוח Python מלא המשתמש בדפוסי async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | לקוח Rust מלא המשתמש ב-Tokio לפעולות אסינכרוניות |

כל דוגמה מלאה כוללת:

- ✅ **הקמת חיבור** וטיפול בשגיאות
- ✅ **גילוי שרת** (כלים, משאבים, הנחיות במידת הצורך)
- ✅ **פעולות מחשבון** (חיבור, חיסור, כפל, חילוק, עזרה)
- ✅ **עיבוד תוצאות** ופלט מעוצב
- ✅ **טיפול מקיף בשגיאות**

- ✅ **קוד נקי ומתועד** עם הערות שלב אחר שלב

### התחלה עם דוגמאות שלמות

1. **בחר את השפה המועדפת עליך** מהטבלה למעלה
2. **עיין בקובץ הדוגמה השלם** כדי להבין את היישום המלא
3. **הרץ את הדוגמה** לפי ההוראות ב־[`complete_examples.md`](./complete_examples.md)
4. **שנה והרחב** את הדוגמה למקרה השימוש הספציפי שלך

לתיעוד מפורט על הרצת והתאמת הדוגמאות הללו, ראה: **[📖 תיעוד דוגמאות שלמות](./complete_examples.md)**

### 💡 פתרון לעומת דוגמאות שלמות

| **תיקיית הפתרון** | **דוגמאות שלמות** |
|--------------------|--------------------- |
| מבנה פרויקט מלא עם קבצי בנייה | יישומים בקובץ יחיד |
| מוכן להרצה עם תלות | דוגמאות קוד ממוקדות |
| הגדרה בסגנון ייצור | הפניה חינוכית |
| כלים ספציפיים לשפה | השוואה בין שפות |

שתי הגישות הן בעלות ערך - השתמש ב**תיקיית הפתרון** לפרויקטים שלמים וב**דוגמאות השלמות** ללמידה ולהפניה.

## נקודות עיקריות

הנקודות העיקריות לפרק זה לגבי הלקוחות הן:

- ניתן להשתמש בהם הן כדי לגלות ולהפעיל פונקציות בשרת.
- יכול להפעיל שרת תוך כדי ההפעלה שלו עצמו (כמו בפרק זה) אך לקוחות יכולים להתחבר גם לשרתי ריצה.
- דרך מצוינת לבדוק יכולות שרת לצד חלופות כמו Inspector כפי שתואר בפרק הקודם.

## משאבים נוספים

- [בניית לקוחות ב־MCP](https://modelcontextprotocol.io/quickstart/client)

## דוגמאות

- [מחשבון Java](../samples/java/calculator/README.md)
- [מחשבון .NET](../../../../03-GettingStarted/samples/csharp)
- [מחשבון JavaScript](../samples/javascript/README.md)
- [מחשבון TypeScript](../samples/typescript/README.md)
- [מחשבון Python](../../../../03-GettingStarted/samples/python)
- [מחשבון Rust](../../../../03-GettingStarted/samples/rust)

## מה הלאה

- הבא: [יצירת לקוח עם LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->