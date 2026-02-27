# Δημιουργία πελάτη

Οι πελάτες είναι προσαρμοσμένες εφαρμογές ή σενάρια που επικοινωνούν απευθείας με έναν MCP Server για να ζητήσουν πόρους, εργαλεία και προτροπές. Σε αντίθεση με τη χρήση του εργαλείου επιθεώρησης, που παρέχει γραφικό περιβάλλον για αλληλεπίδραση με τον διακομιστή, η γραφή του δικού σας πελάτη επιτρέπει προγραμματιστική και αυτοματοποιημένη αλληλεπίδραση. Αυτό επιτρέπει στους προγραμματιστές να ενσωματώσουν δυνατότητες MCP στις δικές τους ροές εργασίας, να αυτοματοποιήσουν εργασίες και να δημιουργήσουν προσαρμοσμένες λύσεις προσαρμοσμένες σε συγκεκριμένες ανάγκες.

## Επισκόπηση

Αυτό το μάθημα εισάγει την έννοια των πελατών στο οικοσύστημα του Model Context Protocol (MCP). Θα μάθετε πώς να γράφετε τον δικό σας πελάτη και να τον συνδέετε σε έναν MCP Server.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτού του μαθήματος, θα είστε σε θέση να:

- Κατανοήσετε τι μπορεί να κάνει ένας πελάτης.
- Γράψετε τον δικό σας πελάτη.
- Συνδέσετε και δοκιμάσετε τον πελάτη με έναν MCP server για να βεβαιωθείτε ότι ο τελευταίος λειτουργεί όπως αναμένεται.

## Τι χρειάζεται για να γράψετε έναν πελάτη;

Για να γράψετε έναν πελάτη, πρέπει να κάνετε τα εξής:

- **Εισαγάγετε τις σωστές βιβλιοθήκες**. Θα χρησιμοποιήσετε την ίδια βιβλιοθήκη όπως πριν, μόνο διαφορετικές δομές.
- **Δημιουργήστε έναν πελάτη**. Αυτό θα περιλαμβάνει τη δημιουργία μιας παρουσίας πελάτη και τη σύνδεσή του με την επιλεγμένη μέθοδο μεταφοράς.
- **Αποφασίστε ποιους πόρους θα καταχωρήσετε**. Ο MCP server σας διαθέτει πόρους, εργαλεία και προτροπές, πρέπει να αποφασίσετε ποιος θα καταχωρηθεί.
- **Ενσωματώστε τον πελάτη σε μια εφαρμογή φιλοξενίας**. Αφού γνωρίζετε τις δυνατότητες του διακομιστή, πρέπει να ενσωματώσετε αυτό στην εφαρμογή φιλοξενίας σας ώστε αν ένας χρήστης πληκτρολογήσει μια προτροπή ή άλλη εντολή να καλείται η αντίστοιχη λειτουργία του διακομιστή.

Τώρα που κατανοούμε σε γενικές γραμμές τι πρόκειται να κάνουμε, ας δούμε ένα παράδειγμα παρακάτω.

### Παράδειγμα πελάτη

Ας ρίξουμε μια ματιά σε αυτό το παράδειγμα πελάτη:

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

// Λίστα προτροπών
const prompts = await client.listPrompts();

// Λήψη προτροπής
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Λίστα πόρων
const resources = await client.listResources();

// Ανάγνωση πόρου
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Χρήση εργαλείου
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Στον προηγούμενο κώδικα:

- Εισάγουμε τις βιβλιοθήκες
- Δημιουργούμε μια παρουσία πελάτη και τη συνδέουμε χρησιμοποιώντας stdio για τη μεταφορά.
- Καταγράφουμε προτροπές, πόρους και εργαλεία και τα καλούμε όλα.

Έχετε λοιπόν έναν πελάτη που μπορεί να επικοινωνεί με έναν MCP Server.

Ας αφιερώσουμε χρόνο στην επόμενη ενότητα άσκησης και να αναλύσουμε κάθε απόσπασμα κώδικα και να εξηγήσουμε τι συμβαίνει.

## Άσκηση: Γράφοντας έναν πελάτη

Όπως ειπώθηκε παραπάνω, ας αφιερώσουμε χρόνο για να εξηγήσουμε τον κώδικα και φυσικά, αν θέλετε, γράψτε και εσείς τον κώδικα παράλληλα.

### -1- Εισαγωγή βιβλιοθηκών

Ας εισάγουμε τις βιβλιοθήκες που χρειαζόμαστε, θα χρειαστούμε αναφορές σε έναν πελάτη και στο προτιμώμενο μεταφορικό πρωτόκολλο, stdio. Το stdio είναι ένα πρωτόκολλο για πράγματα που προορίζονται να τρέχουν στη δική σας τοπική μηχανή. Το SSE είναι ένα άλλο πρωτόκολλο μεταφοράς που θα δείξουμε σε μελλοντικά κεφάλαια αλλά αυτή είναι η άλλη επιλογή σας. Προς το παρόν όμως, ας προχωρήσουμε με το stdio.

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

Για Java, θα δημιουργήσετε έναν πελάτη που συνδέεται στον MCP server από την προηγούμενη άσκηση. Χρησιμοποιώντας την ίδια δομή έργου Java Spring Boot από το [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), δημιουργήστε μια νέα κλάση Java με όνομα `SDKClient` στο φάκελο `src/main/java/com/microsoft/mcp/sample/client/` και προσθέστε τις ακόλουθες εισαγωγές:

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

### -2- Δημιουργία παρουσίας πελάτη και μεταφοράς

Θα χρειαστεί να δημιουργήσουμε μια παρουσία της μεταφοράς και μια της παρουσίας του πελάτη:

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

Στον προηγούμενο κώδικα έχουμε:

- Δημιουργήσει μια παρουσία μεταφοράς stdio. Σημειώστε πώς καθορίζει την εντολή και τα επιχειρήματα για το πώς να βρει και να εκκινήσει τον διακομιστή καθώς αυτό είναι κάτι που θα πρέπει να κάνουμε καθώς δημιουργούμε τον πελάτη.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Δημιουργήσαμε έναν πελάτη δίνοντας του όνομα και έκδοση.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Συνδέσαμε τον πελάτη με την επιλεγμένη μεταφορά.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Δημιουργία παραμέτρων διακομιστή για σύνδεση stdio
server_params = StdioServerParameters(
    command="mcp",  # Εκτελέσιμο
    args=["run", "server.py"],  # Προαιρετικά επιχειρήματα γραμμής εντολών
    env=None,  # Προαιρετικές μεταβλητές περιβάλλοντος
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Αρχικοποίηση της σύνδεσης
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Στον προηγούμενο κώδικα έχουμε:

- Εισαγάγει τις απαραίτητες βιβλιοθήκες.
- Δημιουργήσει ένα αντικείμενο παραμέτρων διακομιστή καθώς το χρησιμοποιούμε για να τρέξουμε τον διακομιστή ώστε να συνδεθούμε με τον πελάτη μας.
- Ορίσει μια μέθοδο `run` που καλεί με τη σειρά της `stdio_client` η οποία ξεκινά μια συνεδρία πελάτη.
- Δημιουργήσει ένα σημείο εισόδου όπου παρέχουμε τη μέθοδο `run` στο `asyncio.run`.

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

Στον προηγούμενο κώδικα έχουμε:

- Εισαγάγει τις απαραίτητες βιβλιοθήκες.
- Δημιουργήσει μια μεταφορά stdio και έναν πελάτη `mcpClient`. Το τελευταίο είναι κάτι που θα χρησιμοποιήσουμε για να καταγράψουμε και να καλέσουμε λειτουργίες στον MCP Server.

Σημειώστε, στα "Arguments", μπορείτε είτε να δείξετε στο *.csproj* είτε στο εκτελέσιμο.

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
        
        // Η λογική του πελάτη σας πηγαίνει εδώ
    }
}
```

Στον προηγούμενο κώδικα έχουμε:

- Δημιουργήσει τη μέθοδο main που ορίζει μια μεταφορά SSE που δείχνει στο `http://localhost:8080` όπου θα τρέχει ο MCP server μας.
- Δημιουργήσει μια κλάση πελάτη που παίρνει τη μεταφορά ως παράμετρο κατασκευής.
- Στη μέθοδο `run`, δημιουργούμε έναν σύγχρονο πελάτη MCP χρησιμοποιώντας τη μεταφορά και αρχικοποιούμε τη σύνδεση.
- Χρησιμοποιήσαμε τη μεταφορά SSE (Server-Sent Events) που είναι κατάλληλη για επικοινωνία HTTP με Java Spring Boot MCP servers.

#### Rust

Σημειώστε ότι ο Rust πελάτης υποθέτει ότι ο διακομιστής είναι ένα γειτονικό έργο με όνομα "calculator-server" στον ίδιο κατάλογο. Ο παρακάτω κώδικας θα εκκινήσει τον διακομιστή και θα συνδεθεί σε αυτόν.

```rust
async fn main() -> Result<(), RmcpError> {
    // Υποθέστε ότι ο διακομιστής είναι ένα αδελφικό έργο με το όνομα "calculator-server" στον ίδιο φάκελο
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

    // TODO: Αρχικοποίηση

    // TODO: Καταγραφή εργαλείων

    // TODO: Καλέστε το εργαλείο προσθήκης με επιχειρήματα = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Καταγραφή λειτουργιών του διακομιστή

Τώρα, έχουμε έναν πελάτη που μπορεί να συνδεθεί αν εκτελεστεί το πρόγραμμα. Ωστόσο, δεν καταγράφει τις λειτουργίες του οπότε ας το κάνουμε τώρα:

#### TypeScript

```typescript
// Λίστα προτροπών
const prompts = await client.listPrompts();

// Λίστα πόρων
const resources = await client.listResources();

// λίστα εργαλείων
const tools = await client.listTools();
```

#### Python

```python
# Λίστα διαθέσιμων πόρων
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Λίστα διαθέσιμων εργαλείων
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Εδώ καταγράφουμε τους διαθέσιμους πόρους, `list_resources()` και εργαλεία, `list_tools` και τα εκτυπώνουμε.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Παραπάνω είναι ένα παράδειγμα για το πώς μπορούμε να καταγράψουμε τα εργαλεία στο διακομιστή. Για κάθε εργαλείο, έπειτα εκτυπώνουμε το όνομά του.

#### Java

```java
// Καταγράψτε και δείξτε εργαλεία
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Μπορείτε επίσης να κάνετε ping στον διακομιστή για να επαληθεύσετε τη σύνδεση
client.ping();
```

Στον προηγούμενο κώδικα έχουμε:

- Καλέσει το `listTools()` για να λάβουμε όλα τα διαθέσιμα εργαλεία από τον MCP server.
- Χρησιμοποιήσει το `ping()` για να επαληθεύσουμε ότι η σύνδεση με τον διακομιστή λειτουργεί.
- Το `ListToolsResult` περιέχει πληροφορίες για όλα τα εργαλεία, συμπεριλαμβανομένων των ονομάτων, περιγραφών και σχημάτων εισόδου τους.

Τέλεια, τώρα έχουμε καταγράψει όλες τις λειτουργίες. Τώρα το ερώτημα είναι πότε τις χρησιμοποιούμε; Αυτός ο πελάτης είναι αρκετά απλός, απλός με την έννοια ότι θα χρειαστεί να καλούμε ρητά τις λειτουργίες όταν τις θέλουμε. Στο επόμενο κεφάλαιο, θα δημιουργήσουμε έναν πιο προηγμένο πελάτη που θα έχει πρόσβαση στο δικό του μεγάλο γλωσσικό μοντέλο, LLM. Προς το παρόν όμως, ας δούμε πώς καλούμε τις λειτουργίες στον διακομιστή:

#### Rust

Στη συνάρτηση main, μετά την αρχικοποίηση του πελάτη, μπορούμε να αρχικοποιήσουμε τον διακομιστή και να καταγράψουμε κάποιες από τις λειτουργίες του.

```rust
// Αρχικοποίηση
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Εργαλεία λίστας
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Κλήση λειτουργιών

Για να καλέσουμε τις λειτουργίες πρέπει να βεβαιωθούμε ότι καθορίζουμε τα σωστά επιχειρήματα και σε ορισμένες περιπτώσεις το όνομα αυτού που προσπαθούμε να καλέσουμε.

#### TypeScript

```typescript

// Διαβάστε μια πηγή
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Καλέστε ένα εργαλείο
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// καλέστε προτροπή
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Στον προηγούμενο κώδικα:

- Διαβάζουμε έναν πόρο, τον καλούμε με `readResource()` καθορίζοντας το `uri`. Δείτε πώς πιθανότατα φαίνεται αυτό στην πλευρά του διακομιστή:

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

    Η τιμή `uri` μας `file://example.txt` ταιριάζει με `file://{name}` στον διακομιστή. Το `example.txt` θα αντιστοιχηθεί στο `name`.

- Καλούμε ένα εργαλείο, το καλούμε καθορίζοντας το `name` και τα `arguments` του ως εξής:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Λαμβάνουμε μια προτροπή, για να πάρετε μια προτροπή, καλείτε `getPrompt()` με `name` και `arguments`. Ο κώδικας διακομιστή φαίνεται έτσι:

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

    και ο κώδικας του πελάτη που προκύπτει είναι:

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
# Διαβάστε μια πηγή
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Καλέστε ένα εργαλείο
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Στον προηγούμενο κώδικα έχουμε:

- Καλέσει έναν πόρο ονόματι `greeting` χρησιμοποιώντας `read_resource`.
- Ενεργοποιήσει ένα εργαλείο που ονομάζεται `add` χρησιμοποιώντας `call_tool`.

#### .NET

1. Ας προσθέσουμε κώδικα για να καλέσουμε ένα εργαλείο:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Για να εκτυπώσουμε το αποτέλεσμα, εδώ είναι κώδικας για να το χειριστεί:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Καλέστε διάφορα εργαλεία αριθμομηχανής
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

Στον προηγούμενο κώδικα έχουμε:

- Καλέσει πολλαπλά εργαλεία αριθμομηχανής χρησιμοποιώντας τη μέθοδο `callTool()` με αντικείμενα `CallToolRequest`.
- Κάθε κλήση εργαλείου καθορίζει το όνομα του εργαλείου και έναν `Map` με τα επιχειρήματα που απαιτούνται από το εργαλείο.
- Τα εργαλεία του διακομιστή αναμένουν συγκεκριμένα ονόματα παραμέτρων (όπως "a", "b" για μαθηματικές πράξεις).
- Τα αποτελέσματα επιστρέφονται ως αντικείμενα `CallToolResult` που περιέχουν την απάντηση από τον διακομιστή.

#### Rust

```rust
// Καλέστε το εργαλείο πρόσθεσης με επιχειρήματα = {"a": 3, "b": 2}
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

Προσθέστε την ακόλουθη εντολή στην ενότητα "scripts" στο *package.json* σας:

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

Πρώτα βεβαιωθείτε ότι ο MCP server σας τρέχει στο `http://localhost:8080`. Έπειτα εκτελέστε τον πελάτη:

```bash
# Δημιουργήστε το έργο σας
./mvnw clean compile

# Εκτελέστε τον πελάτη
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Εναλλακτικά, μπορείτε να εκτελέσετε το πλήρες έργο πελάτη που παρέχεται στο φάκελο λύσης `03-GettingStarted\02-client\solution\java`:

```bash
# Μεταβείτε στον κατάλογο της λύσης
cd 03-GettingStarted/02-client/solution/java

# Δημιουργήστε και εκτελέστε το JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Άσκηση

Σε αυτή την άσκηση, θα χρησιμοποιήσετε όσα μάθατε για να δημιουργήσετε έναν δικό σας πελάτη.

Εδώ είναι ένας διακομιστής που μπορείτε να χρησιμοποιήσετε και πρέπει να καλέσετε μέσω του κώδικα του πελάτη σας. Δείτε αν μπορείτε να προσθέσετε περισσότερες λειτουργίες στον διακομιστή για να τον κάνετε πιο ενδιαφέροντα.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Δημιουργήστε έναν MCP διακομιστή
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Προσθέστε ένα εργαλείο πρόσθεσης
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Προσθέστε μια δυναμική πηγή χαιρετισμού
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

// Ξεκινήστε να λαμβάνετε μηνύματα στο stdin και να στέλνετε μηνύματα στο stdout

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

# Δημιουργήστε έναν διακομιστή MCP
mcp = FastMCP("Demo")


# Προσθέστε ένα εργαλείο πρόσθεσης
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Προσθέστε μια δυναμική πηγή χαιρετισμού
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

Δείτε αυτό το έργο για να μάθετε πώς μπορείτε να [προσθέσετε προτροπές και πόρους](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Επίσης, ελέγξτε αυτόν τον σύνδεσμο για το πώς να καλείτε [προτροπές και πόρους](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Στην [προηγούμενη ενότητα](../../../../03-GettingStarted/01-first-server) μάθατε πώς να δημιουργήσετε έναν απλό MCP διακομιστή με Rust. Μπορείτε να συνεχίσετε να χτίζετε πάνω σε αυτό ή να δείτε αυτόν τον σύνδεσμο για περισσότερα παραδείγματα MCP διακομιστών βασισμένων σε Rust: [Παραδείγματα MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Λύση

Ο **φάκελος λύσης** περιέχει ολοκληρωμένες υλοποιήσεις πελατών έτοιμες προς εκτέλεση που παρουσιάζουν όλους τους όρους που καλύφθηκαν σε αυτό το μάθημα. Κάθε λύση περιλαμβάνει κώδικα πελάτη και διακομιστή οργανωμένο σε ξεχωριστά, αυτοτελή έργα.

### 📁 Δομή Λύσης

Ο κατάλογος λύσης οργανώνεται ανά γλώσσα προγραμματισμού:

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

### 🚀 Τι Περιλαμβάνει Κάθε Λύση

Κάθε λύση ειδική για τη γλώσσα παρέχει:

- **Πλήρη υλοποίηση πελάτη** με όλες τις λειτουργίες από το μάθημα
- **Εργασιακή δομή έργου** με σωστές εξαρτήσεις και ρυθμίσεις
- **Σενάρια κατασκευής και εκτέλεσης** για εύκολη ρύθμιση και εκτέλεση
- **Αναλυτικό README** με οδηγίες ειδικές για τη γλώσσα
- **Παραδείγματα χειρισμού σφαλμάτων** και επεξεργασίας αποτελεσμάτων

### 📖 Χρήση των Λύσεων

1. **Μεταβείτε στο φάκελο της προτιμώμενης γλώσσας σας**:

   ```bash
   cd solution/typescript/    # Για TypeScript
   cd solution/java/          # Για Java
   cd solution/python/        # Για Python
   cd solution/dotnet/        # Για .NET
   ```

2. **Ακολουθήστε τις οδηγίες README σε κάθε φάκελο για:**
   - Εγκατάσταση εξαρτήσεων
   - Κατασκευή του έργου
   - Εκτέλεση του πελάτη

3. **Παράδειγμα εξόδου που θα δείτε:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Για πλήρη τεκμηρίωση και βήμα-βήμα οδηγίες, δείτε: **[📖 Τεκμηρίωση Λύσης](./solution/README.md)**

## 🎯 Ολοκληρωμένα Παραδείγματα

Παρείχαμε ολοκληρωμένες, λειτουργικές υλοποιήσεις πελάτη για όλες τις γλώσσες προγραμματισμού που καλύπτονται σε αυτό το μάθημα. Αυτά τα παραδείγματα δείχνουν τη πλήρη λειτουργικότητα που περιγράφηκε παραπάνω και μπορούν να χρησιμοποιηθούν ως δείγματα υλοποίησης ή σημεία εκκίνησης για τα δικά σας έργα.

### Διαθέσιμα Ολοκληρωμένα Παραδείγματα

| Γλώσσα | Αρχείο | Περιγραφή |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Πλήρης πελάτης Java με χρήση SSE μεταφοράς και ολοκληρωμένη διαχείριση σφαλμάτων |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Πλήρης πελάτης C# με χρήση stdio μεταφοράς και αυτόματη εκκίνηση διακομιστή |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Πλήρης πελάτης TypeScript με πλήρη υποστήριξη πρωτοκόλλου MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Πλήρης πελάτης Python με χρήση προτύπων async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Πλήρης πελάτης Rust με χρήση Tokio για ασύγχρονες λειτουργίες |

Κάθε ολοκληρωμένο παράδειγμα περιλαμβάνει:
- ✅ **Εγκατάσταση σύνδεσης** και διαχείριση σφαλμάτων  
- ✅ **Ανακάλυψη διακομιστή** (εργαλεία, πόροι, προτροπές όπου εφαρμόζεται)  
- ✅ **Ενέργειες αριθμομηχανής** (πρόσθεση, αφαίρεση, πολλαπλασιασμός, διαίρεση, βοήθεια)  
- ✅ **Επεξεργασία αποτελεσμάτων** και μορφοποιημένη έξοδος  
- ✅ **Εκτενής διαχείριση σφαλμάτων**  
- ✅ **Καθαρός, τεκμηριωμένος κώδικας** με σχολιασμούς βήμα προς βήμα  

### Ξεκινώντας με Πλήρη Παραδείγματα  

1. **Επιλέξτε την προτιμώμενη γλώσσα σας** από τον πίνακα πιο πάνω  
2. **Εξετάστε το αρχείο με το πλήρες παράδειγμα** για να κατανοήσετε την πλήρη υλοποίηση  
3. **Τρέξτε το παράδειγμα** ακολουθώντας τις οδηγίες στο [`complete_examples.md`](./complete_examples.md)  
4. **Τροποποιήστε και επεκτείνετε** το παράδειγμα για τη συγκεκριμένη περίπτωση χρήσης σας  

Για λεπτομερή τεκμηρίωση σχετικά με την εκτέλεση και την προσαρμογή αυτών των παραδειγμάτων, δείτε: **[📖 Τεκμηρίωση Πλήρων Παραδειγμάτων](./complete_examples.md)**  

### 💡 Λύση έναντι Πλήρων Παραδειγμάτων  

| **Φάκελος Λύσης** | **Πλήρη Παραδείγματα** |  
|--------------------|---------------------|  
| Πλήρης δομή έργου με αρχεία κατασκευής | Υλοποιήσεις σε μεμονωμένα αρχεία |  
| Έτοιμο για εκτέλεση με εξαρτήσεις | Εστιασμένα παραδείγματα κώδικα |  
| Ρύθμιση παραγωγής | Εκπαιδευτική αναφορά |  
| Εργαλεία ειδικά για γλώσσα | Σύγκριση ανάμεσα σε γλώσσες |  

Και οι δύο προσεγγίσεις έχουν αξία - χρησιμοποιήστε το **φάκελο λύσης** για πλήρη έργα και τα **πλήρη παραδείγματα** για μάθηση και αναφορά.  

## Κύρια Συμπεράσματα  

Τα κύρια συμπεράσματα για αυτό το κεφάλαιο σχετικά με τους πελάτες είναι τα εξής:  

- Μπορούν να χρησιμοποιηθούν τόσο για ανακάλυψη όσο και για κλήση λειτουργιών στον διακομιστή.  
- Μπορούν να ξεκινήσουν έναν διακομιστή ενώ ταυτόχρονα ξεκινούν οι ίδιοι (όπως σε αυτό το κεφάλαιο) αλλά επίσης οι πελάτες μπορούν να συνδεθούν σε ήδη τρέχοντες διακομιστές.  
- Αποτελεί έναν εξαιρετικό τρόπο για να δοκιμάσετε τις δυνατότητες του διακομιστή δίπλα σε εναλλακτικές όπως ο Inspector που περιγράφηκε στο προηγούμενο κεφάλαιο.  

## Πρόσθετοι Πόροι  

- [Κατασκευή πελατών στο MCP](https://modelcontextprotocol.io/quickstart/client)  

## Δείγματα  

- [Java Αριθμομηχανή](../samples/java/calculator/README.md)  
- [Αριθμομηχανή .Net](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Αριθμομηχανή](../samples/javascript/README.md)  
- [TypeScript Αριθμομηχανή](../samples/typescript/README.md)  
- [Python Αριθμομηχανή](../../../../03-GettingStarted/samples/python)  
- [Rust Αριθμομηχανή](../../../../03-GettingStarted/samples/rust)  

## Τι Ακολουθεί  

- Επόμενο: [Δημιουργία πελάτη με LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτοματοποιημένες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται η επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή παρανοήσεις προκύψουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->