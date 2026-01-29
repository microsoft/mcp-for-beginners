# יצירת לקוח

לקוחות הם יישומים מותאמים אישית או סקריפטים שמתקשרים ישירות עם שרת MCP כדי לבקש משאבים, כלים והנחיות. בניגוד לשימוש בכלי הבדיקה, שמספק ממשק גרפי לאינטראקציה עם השרת, כתיבת לקוח משלך מאפשרת אינטראקציות תכנותיות ואוטומטיות. זה מאפשר למפתחים לשלב את יכולות MCP בתהליכי העבודה שלהם, לאוטומט משימות ולבנות פתרונות מותאמים לצרכים ספציפיים.

## סקירה כללית

שיעור זה מציג את מושג הלקוחות בתוך מערכת Model Context Protocol (MCP). תלמדו כיצד לכתוב לקוח משלכם ולחבר אותו לשרת MCP.

## מטרות למידה

בסוף השיעור הזה, תוכלו:

- להבין מה לקוח יכול לעשות.
- לכתוב לקוח משלכם.
- לחבר ולבדוק את הלקוח עם שרת MCP כדי לוודא שהוא פועל כמצופה.

## מה נדרש לכתיבת לקוח?

כדי לכתוב לקוח, תצטרכו לבצע את הפעולות הבאות:

- **לייבא את הספריות הנכונות**. תשתמשו באותה ספרייה כמו קודם, רק במבנים שונים.
- **ליצור מופע של לקוח**. זה יכלול יצירת מופע לקוח וחיבורו לשיטת התעבורה שנבחרה.
- **להחליט אילו משאבים לרשום**. שרת MCP שלכם מגיע עם משאבים, כלים והנחיות, תצטרכו להחליט אילו מהם לרשום.
- **לשלב את הלקוח ביישום מארח**. לאחר שתדעו את יכולות השרת, תצטרכו לשלב זאת ביישום המארח שלכם כך שאם משתמש מקליד הנחיה או פקודה אחרת, תכונת השרת המתאימה תופעל.

עכשיו כשאנחנו מבינים ברמה גבוהה מה אנחנו עומדים לעשות, בואו נסתכל על דוגמה.

### דוגמת לקוח

בואו נסתכל על דוגמת לקוח זו:

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

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

בקוד הקודם:

- ייבאנו את הספריות.
- יצרנו מופע של לקוח וחיברנו אותו באמצעות stdio לתעבורה.
- רשמנו הנחיות, משאבים וכלים והפעלנו את כולם.

הנה לכם, לקוח שיכול לתקשר עם שרת MCP.

בואו ניקח את הזמן בחלק הבא של התרגיל ונפרק כל קטע קוד ונסביר מה קורה.

## תרגיל: כתיבת לקוח

כפי שנאמר לעיל, בואו ניקח את הזמן להסביר את הקוד, ואם תרצו, תוכלו לכתוב את הקוד יחד איתנו.

### -1- ייבוא הספריות

בואו נייבא את הספריות שאנחנו צריכים. נצטרך הפניות ללקוח ולפרוטוקול התעבורה שנבחר, stdio. stdio הוא פרוטוקול לדברים שמיועדים לפעול על המחשב המקומי שלכם. SSE הוא פרוטוקול תעבורה נוסף שנראה בפרקים הבאים, אבל זו האפשרות האחרת שלכם. לעת עתה, בואו נמשיך עם stdio.

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
using ModelContextProtocol.Protocol.Transport;
```

#### Java

עבור Java, תיצרו לקוח שמתחבר לשרת MCP מהתרגיל הקודם. באמצעות אותה מבנה פרויקט Java Spring Boot מ-[התחלה עם שרת MCP](../../../../03-GettingStarted/01-first-server/solution/java), צרו מחלקה חדשה בשם `SDKClient` בתיקייה `src/main/java/com/microsoft/mcp/sample/client/` והוסיפו את הייבוא הבא:

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

תצטרכו להוסיף את התלויות הבאות לקובץ `Cargo.toml` שלכם.

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

משם, תוכלו לייבא את הספריות הנחוצות בקוד הלקוח שלכם.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

בואו נמשיך ליצירת מופע.

### -2- יצירת מופע לקוח ותעבורה

נצטרך ליצור מופע של התעבורה ושל הלקוח שלנו:

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

בקוד הקודם:

- יצרנו מופע תעבורה stdio. שימו לב כיצד הוא מציין פקודה וארגומנטים כדי למצוא ולהפעיל את השרת, שכן זה משהו שנצטרך לעשות כשניצור את הלקוח.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- יצרנו מופע לקוח על ידי מתן שם וגרסה.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- חיברנו את הלקוח לתעבורה שנבחרה.

    ```typescript
    await client.connect(transport);
    ```

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

בקוד הקודם:

- ייבאנו את הספריות הנחוצות.
- יצרנו אובייקט פרמטרים של שרת שנשתמש בו כדי להפעיל את השרת כך שנוכל להתחבר אליו עם הלקוח שלנו.
- הגדרנו שיטה `run` שמצידה קוראת ל-`stdio_client` שמתחילה סשן לקוח.
- יצרנו נקודת כניסה שבה אנו מספקים את השיטה `run` ל-`asyncio.run`.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

בקוד הקודם:

- ייבאנו את הספריות הנחוצות.
- יצרנו תעבורת stdio ויצרנו לקוח `mcpClient`. האחרון הוא משהו שנשתמש בו כדי לרשום ולהפעיל תכונות בשרת MCP.

שימו לב, ב"Arguments", תוכלו להצביע על *.csproj* או על הקובץ הביצועי.

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
        
        // Your client logic goes here
    }
}
```

בקוד הקודם:

- יצרנו שיטת main שמגדירה תעבורת SSE המצביעה על `http://localhost:8080` שבו שרת MCP שלנו יפעל.
- יצרנו מחלקת לקוח שלוקחת את התעבורה כפרמטר קונסטרוקטור.
- בשיטה `run`, יצרנו לקוח MCP סינכרוני באמצעות התעבורה ואתחלנו את החיבור.
- השתמשנו בתעבורת SSE (Server-Sent Events) שמתאימה לתקשורת מבוססת HTTP עם שרתי MCP של Java Spring Boot.

#### Rust

שימו לב שלקוח Rust זה מניח שהשרת הוא פרויקט אח בשם "calculator-server" באותה תיקייה. הקוד למטה יפעיל את השרת ויתחבר אליו.

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
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

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- רישום תכונות השרת

עכשיו יש לנו לקוח שיכול להתחבר אם התוכנית תופעל. עם זאת, הוא לא באמת רושם את התכונות שלו, אז בואו נעשה זאת עכשיו:

#### TypeScript

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

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
```

כאן אנו רושמים את המשאבים הזמינים, `list_resources()` ואת הכלים, `list_tools` ומדפיסים אותם.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

לעיל דוגמה כיצד ניתן לרשום את הכלים בשרת. עבור כל כלי, אנו מדפיסים את שמו.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

בקוד הקודם:

- קראנו ל-`listTools()` כדי לקבל את כל הכלים הזמינים משרת MCP.
- השתמשנו ב-`ping()` כדי לוודא שהחיבור לשרת עובד.
- ה-`ListToolsResult` מכיל מידע על כל הכלים כולל שמותיהם, תיאורים וסכמות קלט.

מצוין, עכשיו רשמנו את כל התכונות. עכשיו השאלה היא מתי נשתמש בהם? ובכן, הלקוח הזה די פשוט, פשוט במובן שנצטרך לקרוא לתכונות באופן מפורש כשנרצה אותן. בפרק הבא, ניצור לקוח מתקדם יותר שיש לו גישה למודל שפה גדול משלו, LLM. לעת עתה, בואו נראה כיצד ניתן להפעיל את התכונות בשרת:

#### Rust

בפונקציה הראשית, לאחר אתחול הלקוח, נוכל לאתחל את השרת ולרשום כמה מהתכונות שלו.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- הפעלת תכונות

כדי להפעיל את התכונות, עלינו לוודא שאנו מציינים את הארגומנטים הנכונים ובמקרים מסוימים את שם מה שאנחנו מנסים להפעיל.

#### TypeScript

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

בקוד הקודם:

- קראנו למשאב, אנו קוראים למשאב על ידי קריאה ל-`readResource()` וציון `uri`. הנה איך זה נראה ככל הנראה בצד השרת:

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

    ערך ה-`uri` שלנו `file://example.txt` תואם ל-`file://{name}` בשרת. `example.txt` ימופה ל-`name`.

- קראנו לכלי, אנו קוראים לו על ידי ציון `name` ו-`arguments` כמו כך:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- קיבלנו הנחיה, כדי לקבל הנחיה, אנו קוראים ל-`getPrompt()` עם `name` ו-`arguments`. קוד השרת נראה כך:

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

    ולכן קוד הלקוח שלכם נראה כך כדי להתאים למה שמוצהר בשרת:

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
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

בקוד הקודם:

- קראנו למשאב בשם `greeting` באמצעות `read_resource`.
- הפעלנו כלי בשם `add` באמצעות `call_tool`.

#### .NET

1. בואו נוסיף קוד לקרוא לכלי:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. כדי להדפיס את התוצאה, הנה קוד לטיפול בכך:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call various calculator tools
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

בקוד הקודם:

- קראנו למספר כלים של מחשבון באמצעות שיטת `callTool()` עם אובייקטים של `CallToolRequest`.
- כל קריאה לכלי מציינת את שם הכלי ואת `Map` של ארגומנטים הנדרשים על ידי אותו כלי.
- הכלים בשרת מצפים לשמות פרמטרים ספציפיים (כמו "a", "b" לפעולות מתמטיות).
- התוצאות מוחזרות כאובייקטים של `CallToolResult` המכילים את התגובה מהשרת.

#### Rust

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
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

### -5- הפעלת הלקוח

כדי להפעיל את הלקוח, הקלידו את הפקודה הבאה בטרמינל:

#### TypeScript

הוסיפו את הערך הבא לקטע "scripts" ב-*package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

קראו ללקוח עם הפקודה הבאה:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

ראשית, ודאו ששרת MCP שלכם פועל ב-`http://localhost:8080`. לאחר מכן הפעילו את הלקוח:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

לחילופין, תוכלו להפעיל את פרויקט הלקוח המלא המסופק בתיקיית הפתרון `03-GettingStarted\02-client\solution\java`:

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## משימה

במשימה זו, תשתמשו במה שלמדתם ביצירת לקוח אך תיצרו לקוח משלכם.

הנה שרת שתוכלו להשתמש בו ושעליכם לקרוא לו באמצעות קוד הלקוח שלכם. נסו להוסיף עוד תכונות לשרת כדי להפוך אותו למעניין יותר.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout

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

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
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

ראו את הפרויקט הזה כדי לראות כיצד ניתן [להוסיף הנחיות ומשאבים](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

כמו כן, בדקו את הקישור הזה כיצד להפעיל [הנחיות ומשאבים](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

ב-[החלק הקודם](../../../../03-GettingStarted/01-first-server), למדתם כיצד ליצור שרת MCP פשוט עם Rust. תוכלו להמשיך לבנות על זה או לבדוק את הקישור הזה לעוד דוגמאות שרת MCP מבוססות Rust: [דוגמאות שרת MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## פתרון

תיקיית **הפתרון** מכילה יישומי לקוח מלאים ומוכנים להפעלה שמדגימים את כל המושגים שנלמדו במדריך זה. כל פתרון כולל גם קוד לקוח וגם קוד שרת המאורגנים בפרויקטים נפרדים ועצמאיים.

### 📁 מבנה הפתרון

תיקיית הפתרון מאורגנת לפי שפת תכנות:

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

- **יישום לקוח מלא** עם כל התכונות מהמדריך
- **מבנה פרויקט עובד** עם תלות ותצורה נכונה
- **סקריפטים לבנייה והפעלה** להגדרה והפעלה קלה
- **README מפורט** עם הוראות ספציפיות לשפה
- **דוגמאות לטיפול בשגיאות** ועיבוד תוצאות

### 📖 שימוש בפתרונות

1. **נווטו לתיקיית השפה המועדפת עליכם**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **עקבו אחר הוראות README** בכל תיקייה עבור:
   - התקנת תלות
   - בניית הפרויקט
   - הפעלת הלקוח

3. **פלט דוגמה** שאתם אמורים לראות:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

למסמכים מלאים והוראות שלב-אחר-שלב, ראו: **[📖 מסמכי פתרון](./solution/README.md)**

## 🎯 דוגמאות מלאות

סיפקנו יישומי לקוח מלאים ועובדים לכל שפות התכנות שנלמדו במדריך זה. דוגמאות אלו מדגימות את כל הפונקציונליות שתוארה לעיל וניתן להשתמש בהן כהפניות או נקודות התחלה לפרויקטים שלכם.

### דוגמאות מלאות זמינות

| שפה | קובץ | תיאור |
|-----|------|-------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | לקוח Java מלא המשתמש בתעבורת SSE עם טיפול שגיאות מקיף |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | לקוח C# מלא המשתמש בתעבורת stdio עם הפעלה אוטומטית של השרת |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | לקוח TypeScript מלא עם תמיכה מלאה בפרוטוקול MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | לקוח Python מלא המשתמש בתבניות async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | לקוח Rust מלא המשתמש ב-Tokio לפעולות אסינכרוניות |
כל דוגמה מלאה כוללת:

- ✅ **הקמת חיבור** וטיפול בשגיאות  
- ✅ **גילוי שרת** (כלים, משאבים, הנחיות במידת הצורך)  
- ✅ **פעולות מחשבון** (חיבור, חיסור, כפל, חילוק, עזרה)  
- ✅ **עיבוד תוצאות** ופלט מעוצב  
- ✅ **טיפול מקיף בשגיאות**  
- ✅ **קוד נקי ומתועד** עם הערות שלב אחר שלב  

### התחלת עבודה עם דוגמאות מלאות

1. **בחר את השפה המועדפת עליך** מהטבלה למעלה  
2. **סקור את קובץ הדוגמה המלא** כדי להבין את היישום המלא  
3. **הרץ את הדוגמה** לפי ההוראות ב-[`complete_examples.md`](./complete_examples.md)  
4. **התאם והרחב** את הדוגמה לצרכים הספציפיים שלך  

למסמכים מפורטים על הרצה והתאמה של דוגמאות אלו, ראה: **[📖 תיעוד דוגמאות מלאות](./complete_examples.md)**  

### 💡 פתרון מול דוגמאות מלאות

| **תיקיית פתרון** | **דוגמאות מלאות** |
|--------------------|--------------------- |
| מבנה פרויקט מלא עם קבצי בנייה | יישומים בקובץ יחיד |
| מוכן להרצה עם תלות | דוגמאות קוד ממוקדות |
| הגדרות דמויות ייצור | התייחסות חינוכית |
| כלים ספציפיים לשפה | השוואה בין שפות |

שתי הגישות חשובות - השתמש ב**תיקיית הפתרון** לפרויקטים מלאים וב**דוגמאות המלאות** ללמידה והתייחסות.

## נקודות מרכזיות

הנקודות המרכזיות בפרק זה לגבי לקוחות הן:

- ניתן להשתמש בהם הן לגילוי והן להפעלת תכונות על השרת.  
- יכולים להפעיל שרת תוך כדי הפעלתם (כמו בפרק זה), אך לקוחות יכולים גם להתחבר לשרתים פעילים.  
- מהווים דרך מצוינת לבדוק יכולות שרת לצד חלופות כמו ה-Inspector שתואר בפרק הקודם.  

## משאבים נוספים

- [בניית לקוחות ב-MCP](https://modelcontextprotocol.io/quickstart/client)

## דוגמאות

- [מחשבון ב-Java](../samples/java/calculator/README.md)  
- [מחשבון ב-.Net](../../../../03-GettingStarted/samples/csharp)  
- [מחשבון ב-JavaScript](../samples/javascript/README.md)  
- [מחשבון ב-TypeScript](../samples/typescript/README.md)  
- [מחשבון ב-Python](../../../../03-GettingStarted/samples/python)  
- [מחשבון ב-Rust](../../../../03-GettingStarted/samples/rust)  

## מה הלאה

- הבא: [יצירת לקוח עם LLM](../03-llm-client/README.md)  

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.