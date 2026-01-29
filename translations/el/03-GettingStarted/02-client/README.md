# Δημιουργία πελάτη

Οι πελάτες είναι προσαρμοσμένες εφαρμογές ή σενάρια που επικοινωνούν απευθείας με έναν MCP Server για να ζητήσουν πόρους, εργαλεία και προτροπές. Σε αντίθεση με τη χρήση του εργαλείου επιθεώρησης, το οποίο παρέχει γραφική διεπαφή για την αλληλεπίδραση με τον διακομιστή, η δημιουργία του δικού σας πελάτη επιτρέπει προγραμματισμένες και αυτοματοποιημένες αλληλεπιδράσεις. Αυτό δίνει τη δυνατότητα στους προγραμματιστές να ενσωματώσουν τις δυνατότητες του MCP στις δικές τους ροές εργασίας, να αυτοματοποιήσουν εργασίες και να δημιουργήσουν προσαρμοσμένες λύσεις προσαρμοσμένες σε συγκεκριμένες ανάγκες.

## Επισκόπηση

Αυτό το μάθημα εισάγει την έννοια των πελατών στο οικοσύστημα του Model Context Protocol (MCP). Θα μάθετε πώς να γράψετε τον δικό σας πελάτη και να τον συνδέσετε με έναν MCP Server.

## Στόχοι μάθησης

Μέχρι το τέλος αυτού του μαθήματος, θα μπορείτε να:

- Κατανοήσετε τι μπορεί να κάνει ένας πελάτης.
- Γράψετε τον δικό σας πελάτη.
- Συνδέσετε και δοκιμάσετε τον πελάτη με έναν MCP Server για να βεβαιωθείτε ότι λειτουργεί όπως αναμένεται.

## Τι περιλαμβάνει η δημιουργία ενός πελάτη;

Για να γράψετε έναν πελάτη, θα χρειαστεί να κάνετε τα εξής:

- **Εισαγωγή των σωστών βιβλιοθηκών**. Θα χρησιμοποιήσετε την ίδια βιβλιοθήκη όπως πριν, απλώς διαφορετικές δομές.
- **Δημιουργία ενός πελάτη**. Αυτό θα περιλαμβάνει τη δημιουργία μιας παρουσίας πελάτη και τη σύνδεσή της με την επιλεγμένη μέθοδο μεταφοράς.
- **Απόφαση για τους πόρους που θα καταχωρηθούν**. Ο MCP Server σας διαθέτει πόρους, εργαλεία και προτροπές, και πρέπει να αποφασίσετε ποια από αυτά θα καταχωρηθούν.
- **Ενσωμάτωση του πελάτη σε μια εφαρμογή υποδοχής**. Μόλις γνωρίσετε τις δυνατότητες του διακομιστή, πρέπει να τον ενσωματώσετε στην εφαρμογή υποδοχής σας, ώστε όταν ένας χρήστης πληκτρολογεί μια προτροπή ή άλλη εντολή, να ενεργοποιείται η αντίστοιχη λειτουργία του διακομιστή.

Τώρα που κατανοούμε σε υψηλό επίπεδο τι πρόκειται να κάνουμε, ας δούμε ένα παράδειγμα.

### Παράδειγμα πελάτη

Ας δούμε ένα παράδειγμα πελάτη:

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

Στον παραπάνω κώδικα:

- Εισάγουμε τις βιβλιοθήκες.
- Δημιουργούμε μια παρουσία πελάτη και τη συνδέουμε χρησιμοποιώντας το stdio για μεταφορά.
- Καταχωρούμε προτροπές, πόρους και εργαλεία και τα ενεργοποιούμε όλα.

Έχουμε λοιπόν έναν πελάτη που μπορεί να επικοινωνεί με έναν MCP Server.

Ας αφιερώσουμε χρόνο στην επόμενη ενότητα άσκησης και να αναλύσουμε κάθε κομμάτι κώδικα εξηγώντας τι συμβαίνει.

## Άσκηση: Δημιουργία πελάτη

Όπως είπαμε παραπάνω, ας αφιερώσουμε χρόνο εξηγώντας τον κώδικα, και φυσικά μπορείτε να γράψετε κώδικα παράλληλα αν θέλετε.

### -1- Εισαγωγή βιβλιοθηκών

Ας εισάγουμε τις βιβλιοθήκες που χρειαζόμαστε. Θα χρειαστούμε αναφορές σε έναν πελάτη και στο επιλεγμένο πρωτόκολλο μεταφοράς, stdio. Το stdio είναι ένα πρωτόκολλο για πράγματα που προορίζονται να εκτελούνται στον τοπικό σας υπολογιστή. Το SSE είναι ένα άλλο πρωτόκολλο μεταφοράς που θα δείξουμε σε μελλοντικά κεφάλαια, αλλά είναι η άλλη σας επιλογή. Προς το παρόν, όμως, ας συνεχίσουμε με το stdio.

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

Για την Java, θα δημιουργήσετε έναν πελάτη που συνδέεται με τον MCP Server από την προηγούμενη άσκηση. Χρησιμοποιώντας την ίδια δομή έργου Java Spring Boot από [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), δημιουργήστε μια νέα κλάση Java που ονομάζεται `SDKClient` στον φάκελο `src/main/java/com/microsoft/mcp/sample/client/` και προσθέστε τις ακόλουθες εισαγωγές:

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

Θα χρειαστεί να προσθέσετε τις ακόλουθες εξαρτήσεις στο αρχείο `Cargo.toml`.

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

Από εκεί, μπορείτε να εισάγετε τις απαραίτητες βιβλιοθήκες στον κώδικα του πελάτη σας.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Ας προχωρήσουμε στη δημιουργία παρουσίας.

### -2- Δημιουργία πελάτη και μεταφοράς

Θα χρειαστεί να δημιουργήσουμε μια παρουσία της μεταφοράς και του πελάτη μας:

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

Στον παραπάνω κώδικα:

- Δημιουργούμε μια παρουσία μεταφοράς stdio. Σημειώστε πώς καθορίζει την εντολή και τα επιχειρήματα για το πώς να βρει και να ξεκινήσει τον διακομιστή, καθώς αυτό είναι κάτι που θα χρειαστεί να κάνουμε καθώς δημιουργούμε τον πελάτη.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Δημιουργούμε μια παρουσία πελάτη δίνοντάς της ένα όνομα και έκδοση.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Συνδέουμε τον πελάτη με την επιλεγμένη μεταφορά.

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

Στον παραπάνω κώδικα:

- Εισάγουμε τις απαραίτητες βιβλιοθήκες.
- Δημιουργούμε ένα αντικείμενο παραμέτρων διακομιστή, καθώς θα το χρησιμοποιήσουμε για να εκτελέσουμε τον διακομιστή ώστε να μπορέσουμε να συνδεθούμε με αυτόν μέσω του πελάτη μας.
- Ορίζουμε μια μέθοδο `run` που με τη σειρά της καλεί το `stdio_client`, το οποίο ξεκινά μια συνεδρία πελάτη.
- Δημιουργούμε ένα σημείο εισόδου όπου παρέχουμε τη μέθοδο `run` στο `asyncio.run`.

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

Στον παραπάνω κώδικα:

- Εισάγουμε τις απαραίτητες βιβλιοθήκες.
- Δημιουργούμε μια μεταφορά stdio και έναν πελάτη `mcpClient`. Ο τελευταίος είναι κάτι που θα χρησιμοποιήσουμε για να καταχωρήσουμε και να ενεργοποιήσουμε λειτουργίες στον MCP Server.

Σημείωση: Στα "Arguments", μπορείτε είτε να δείξετε στο *.csproj* είτε στο εκτελέσιμο.

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

Στον παραπάνω κώδικα:

- Δημιουργούμε μια κύρια μέθοδο που ρυθμίζει μια μεταφορά SSE που δείχνει στο `http://localhost:8080`, όπου θα εκτελείται ο MCP Server μας.
- Δημιουργούμε μια κλάση πελάτη που λαμβάνει τη μεταφορά ως παράμετρο κατασκευαστή.
- Στη μέθοδο `run`, δημιουργούμε έναν συγχρονισμένο MCP πελάτη χρησιμοποιώντας τη μεταφορά και αρχικοποιούμε τη σύνδεση.
- Χρησιμοποιούμε τη μεταφορά SSE (Server-Sent Events), η οποία είναι κατάλληλη για επικοινωνία μέσω HTTP με MCP Servers Java Spring Boot.

#### Rust

Αυτός ο πελάτης Rust υποθέτει ότι ο διακομιστής είναι ένα αδελφό έργο με όνομα "calculator-server" στον ίδιο κατάλογο. Ο παρακάτω κώδικας θα ξεκινήσει τον διακομιστή και θα συνδεθεί με αυτόν.

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

### -3- Καταχώρηση λειτουργιών του διακομιστή

Τώρα έχουμε έναν πελάτη που μπορεί να συνδεθεί αν εκτελεστεί το πρόγραμμα. Ωστόσο, δεν καταχωρεί τις λειτουργίες του, οπότε ας το κάνουμε αυτό στη συνέχεια:

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

Εδώ καταχωρούμε τους διαθέσιμους πόρους, `list_resources()` και εργαλεία, `list_tools`, και τους εκτυπώνουμε.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Παραπάνω είναι ένα παράδειγμα για το πώς μπορούμε να καταχωρήσουμε τα εργαλεία στον διακομιστή. Για κάθε εργαλείο, εκτυπώνουμε το όνομά του.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Στον παραπάνω κώδικα:

- Καλούμε το `listTools()` για να λάβουμε όλα τα διαθέσιμα εργαλεία από τον MCP Server.
- Χρησιμοποιούμε το `ping()` για να επαληθεύσουμε ότι η σύνδεση με τον διακομιστή λειτουργεί.
- Το `ListToolsResult` περιέχει πληροφορίες για όλα τα εργαλεία, συμπεριλαμβανομένων των ονομάτων, περιγραφών και σχημάτων εισόδου.

Ωραία, τώρα έχουμε καταγράψει όλες τις λειτουργίες. Τώρα το ερώτημα είναι πότε τις χρησιμοποιούμε; Λοιπόν, αυτός ο πελάτης είναι αρκετά απλός, απλός με την έννοια ότι θα χρειαστεί να καλέσουμε ρητά τις λειτουργίες όταν τις θέλουμε. Στο επόμενο κεφάλαιο, θα δημιουργήσουμε έναν πιο προηγμένο πελάτη που έχει πρόσβαση στο δικό του μεγάλο γλωσσικό μοντέλο (LLM). Προς το παρόν, όμως, ας δούμε πώς μπορούμε να ενεργοποιήσουμε τις λειτουργίες στον διακομιστή:

#### Rust

Στη κύρια συνάρτηση, μετά την αρχικοποίηση του πελάτη, μπορούμε να αρχικοποιήσουμε τον διακομιστή και να καταχωρήσουμε μερικές από τις λειτουργίες του.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Ενεργοποίηση λειτουργιών

Για να ενεργοποιήσουμε τις λειτουργίες, πρέπει να βεβαιωθούμε ότι καθορίζουμε τα σωστά επιχειρήματα και, σε ορισμένες περιπτώσεις, το όνομα αυτού που προσπαθούμε να ενεργοποιήσουμε.

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

Στον παραπάνω κώδικα:

- Διαβάζουμε έναν πόρο, τον καλούμε χρησιμοποιώντας το `readResource()` καθορίζοντας το `uri`. Να πώς πιθανότατα φαίνεται από την πλευρά του διακομιστή:

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

    Η τιμή `uri` μας `file://example.txt` αντιστοιχεί στο `file://{name}` στον διακομιστή. Το `example.txt` θα αντιστοιχιστεί στο `name`.

- Καλούμε ένα εργαλείο, το καλούμε καθορίζοντας το `name` και τα `arguments` όπως παρακάτω:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Λαμβάνουμε προτροπή, για να λάβουμε μια προτροπή, καλούμε το `getPrompt()` με `name` και `arguments`. Ο κώδικας του διακομιστή φαίνεται ως εξής:

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

    και ο αντίστοιχος κώδικας πελάτη σας φαίνεται ως εξής για να ταιριάζει με αυτό που δηλώνεται στον διακομιστή:

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

Στον παραπάνω κώδικα:

- Καλούμε έναν πόρο που ονομάζεται `greeting` χρησιμοποιώντας το `read_resource`.
- Ενεργοποιούμε ένα εργαλείο που ονομάζεται `add` χρησιμοποιώντας το `call_tool`.

#### .NET

1. Ας προσθέσουμε λίγο κώδικα για να καλέσουμε ένα εργαλείο:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Για να εκτυπώσουμε το αποτέλεσμα, εδώ είναι κάποιος κώδικας για να το χειριστούμε:

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

Στον παραπάνω κώδικα:

- Καλούμε πολλαπλά εργαλεία υπολογιστή χρησιμοποιώντας τη μέθοδο `callTool()` με αντικείμενα `CallToolRequest`.
- Κάθε κλήση εργαλείου καθορίζει το όνομα του εργαλείου και έναν `Map` με τα επιχειρήματα που απαιτούνται από αυτό το εργαλείο.
- Τα εργαλεία του διακομιστή αναμένουν συγκεκριμένα ονόματα παραμέτρων (όπως "a", "b" για μαθηματικές πράξεις).
- Τα αποτελέσματα επιστρέφονται ως αντικείμενα `CallToolResult` που περιέχουν την απάντηση από τον διακομιστή.

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

### -5- Εκτέλεση του πελάτη

Για να εκτελέσετε τον πελάτη, πληκτρολογήστε την ακόλουθη εντολή στο τερματικό:

#### TypeScript

Προσθέστε την ακόλουθη καταχώρηση στην ενότητα "scripts" στο *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Καλέστε τον πελάτη με την ακόλουθη εντολή:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Πρώτα, βεβαιωθείτε ότι ο MCP Server σας εκτελείται στο `http://localhost:8080`. Στη συνέχεια, εκτελέστε τον πελάτη:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Εναλλακτικά, μπορείτε να εκτελέσετε το πλήρες έργο πελάτη που παρέχεται στον φάκελο λύσης `03-GettingStarted\02-client\solution\java`:

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

## Εργασία

Σε αυτή την εργασία, θα χρησιμοποιήσετε όσα μάθατε για τη δημιουργία ενός πελάτη, αλλά θα δημιουργήσετε έναν δικό σας πελάτη.

Ακολουθεί ένας διακομιστής που μπορείτε να χρησιμοποιήσετε και που πρέπει να καλέσετε μέσω του κώδικα του πελάτη σας. Δείτε αν μπορείτε να προσθέσετε περισσότερες λειτουργίες στον διακομιστή για να τον κάνετε πιο ενδιαφέρον.

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

Δείτε αυτό το έργο για να δείτε πώς μπορείτε να [προσθέσετε προτροπές και πόρους](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Επίσης, ελέγξτε αυτόν τον σύνδεσμο για το πώς να ενεργοποιήσετε [προτροπές και πόρους](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Στην [προηγούμενη ενότητα](../../../../03-GettingStarted/01-first-server), μάθατε πώς να δημιουργήσετε έναν απλό MCP Server με Rust. Μπορείτε να συνεχίσετε να χτίζετε πάνω σε αυτό ή να ελέγξετε αυτόν τον σύνδεσμο για περισσότερα παραδείγματα MCP Server με Rust: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Λύση

Ο **φάκελος λύσης** περιέχει πλήρεις, έτοιμες προς εκτέλεση υλοποιήσεις πελατών που επιδεικνύουν όλες τις έννοιες που καλύφθηκαν σε αυτό το μάθημα. Κάθε λύση περιλαμβάνει τόσο κώδικα πελάτη όσο και διακομιστή οργανωμένο σε ξεχωριστά, αυτοτελή έργα.

### 📁 Δομή Λύσης

Ο φάκελος λύσης είναι οργανωμένος ανά γλώσσα προγραμματισμού:

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

### 🚀 Τι περιλαμβάνει κάθε λύση

Κάθε λύση ανά γλώσσα παρέχει:

- **Πλήρης υλοποίηση πελάτη** με όλες τις λειτουργίες από το μάθημα
- **Λειτουργική δομή έργου** με σωστές εξαρτήσεις και διαμόρφωση
- **Σενάρια κατασκευής και εκτέλεσης** για εύκολη εγκατάσταση και εκτέλεση
- **Λεπτομερές README** με οδηγίες ανά γλώσσα
- **Παραδείγματα χειρισμού σφαλμάτων** και επεξεργασίας αποτελεσμάτων

### 📖 Χρήση των λύσεων

1. **Μεταβείτε στον φάκελο της προτιμώμενης γλώσσας σας**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Ακολουθήστε τις οδηγίες του README** σε κάθε φάκελο για:
   - Εγκατάσταση εξαρτήσεων
   - Κατασκευή του έργου
   - Εκτέλεση του πελάτη

3. **Παραδείγματα εξόδου** που θα πρέπει να δείτε:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Για πλήρη τεκμηρίωση και οδηγίες βήμα προς βήμα, δείτε: **[
Κάθε πλήρες παράδειγμα περιλαμβάνει:

- ✅ **Εγκατάσταση σύνδεσης** και διαχείριση σφαλμάτων
- ✅ **Ανακάλυψη διακομιστή** (εργαλεία, πόροι, προτροπές όπου είναι εφαρμόσιμο)
- ✅ **Λειτουργίες αριθμομηχανής** (πρόσθεση, αφαίρεση, πολλαπλασιασμός, διαίρεση, βοήθεια)
- ✅ **Επεξεργασία αποτελεσμάτων** και μορφοποιημένη έξοδος
- ✅ **Πλήρης διαχείριση σφαλμάτων**
- ✅ **Καθαρός, τεκμηριωμένος κώδικας** με σχόλια βήμα προς βήμα

### Ξεκινώντας με Πλήρη Παραδείγματα

1. **Επιλέξτε την προτιμώμενη γλώσσα σας** από τον πίνακα παραπάνω
2. **Ανασκοπήστε το αρχείο πλήρους παραδείγματος** για να κατανοήσετε την πλήρη υλοποίηση
3. **Εκτελέστε το παράδειγμα** ακολουθώντας τις οδηγίες στο [`complete_examples.md`](./complete_examples.md)
4. **Τροποποιήστε και επεκτείνετε** το παράδειγμα για τη συγκεκριμένη περίπτωση χρήσης σας

Για λεπτομερή τεκμηρίωση σχετικά με την εκτέλεση και την προσαρμογή αυτών των παραδειγμάτων, δείτε: **[📖 Τεκμηρίωση Πλήρων Παραδειγμάτων](./complete_examples.md)**

### 💡 Λύση vs. Πλήρη Παραδείγματα

| **Φάκελος Λύσης** | **Πλήρη Παραδείγματα** |
|--------------------|--------------------- |
| Πλήρης δομή έργου με αρχεία build | Υλοποιήσεις σε ένα αρχείο |
| Έτοιμο για εκτέλεση με εξαρτήσεις | Εστιασμένα παραδείγματα κώδικα |
| Ρύθμιση παραγωγής | Εκπαιδευτική αναφορά |
| Εργαλεία συγκεκριμένα για τη γλώσσα | Σύγκριση μεταξύ γλωσσών |

Και οι δύο προσεγγίσεις είναι πολύτιμες - χρησιμοποιήστε τον **φάκελο λύσης** για πλήρη έργα και τα **πλήρη παραδείγματα** για μάθηση και αναφορά.

## Βασικά Σημεία

Τα βασικά σημεία αυτού του κεφαλαίου σχετικά με τους πελάτες είναι τα εξής:

- Μπορούν να χρησιμοποιηθούν τόσο για την ανακάλυψη όσο και για την εκτέλεση λειτουργιών στον διακομιστή.
- Μπορούν να ξεκινήσουν έναν διακομιστή ενώ ξεκινούν οι ίδιοι (όπως σε αυτό το κεφάλαιο), αλλά οι πελάτες μπορούν επίσης να συνδεθούν σε ήδη λειτουργούντες διακομιστές.
- Είναι ένας εξαιρετικός τρόπος για να δοκιμάσετε τις δυνατότητες του διακομιστή δίπλα σε εναλλακτικές όπως ο Επιθεωρητής, όπως περιγράφηκε στο προηγούμενο κεφάλαιο.

## Πρόσθετοι Πόροι

- [Δημιουργία πελατών στο MCP](https://modelcontextprotocol.io/quickstart/client)

## Παραδείγματα

- [Java Αριθμομηχανή](../samples/java/calculator/README.md)
- [.Net Αριθμομηχανή](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Αριθμομηχανή](../samples/javascript/README.md)
- [TypeScript Αριθμομηχανή](../samples/typescript/README.md)
- [Python Αριθμομηχανή](../../../../03-GettingStarted/samples/python)
- [Rust Αριθμομηχανή](../../../../03-GettingStarted/samples/rust)

## Τι Ακολουθεί

- Επόμενο: [Δημιουργία πελάτη με LLM](../03-llm-client/README.md)

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε κάθε προσπάθεια για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.