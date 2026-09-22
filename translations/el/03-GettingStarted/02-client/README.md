# Δημιουργία πελάτη

Οι πελάτες είναι προσαρμοσμένες εφαρμογές ή σενάρια που επικοινωνούν απευθείας με έναν MCP Server για να ζητήσουν πόρους, εργαλεία και προτροπές. Σε αντίθεση με τη χρήση του εργαλείου επιθεώρησης, που παρέχει γραφική διεπαφή για την αλληλεπίδραση με τον διακομιστή, η συγγραφή του δικού σας πελάτη επιτρέπει προγραμματισμένες και αυτοματοποιημένες αλληλεπιδράσεις. Αυτό επιτρέπει στους προγραμματιστές να ενσωματώνουν τις δυνατότητες του MCP στις δικές τους ροές εργασίας, να αυτοματοποιούν εργασίες και να δημιουργούν προσαρμοσμένες λύσεις προσαρμοσμένες σε συγκεκριμένες ανάγκες.

## Επισκόπηση

Αυτό το μάθημα εισάγει την έννοια των πελατών στο οικοσύστημα του Model Context Protocol (MCP). Θα μάθετε πώς να γράφετε τον δικό σας πελάτη και να τον συνδέετε με έναν MCP Server.

## Στόχοι μάθησης

Στο τέλος αυτού του μαθήματος, θα είστε σε θέση να:

- Κατανοείτε τι μπορεί να κάνει ένας πελάτης.
- Να γράφετε τον δικό σας πελάτη.
- Να συνδέετε και να δοκιμάζετε τον πελάτη με έναν MCP server για να διασφαλίσετε ότι λειτουργεί όπως αναμένεται.

## Τι περιλαμβάνει η συγγραφή ενός πελάτη;

Για να γράψετε έναν πελάτη, πρέπει να κάνετε τα εξής:

- **Εισαγωγή των σωστών βιβλιοθηκών**. Θα χρησιμοποιήσετε την ίδια βιβλιοθήκη όπως πριν, απλώς με διαφορετικές κατασκευές.
- **Δημιουργία ενός πελάτη**. Αυτό θα περιλαμβάνει τη δημιουργία μιας παρουσίας πελάτη και τη σύνδεσή της με την επιλεγμένη μέθοδο μεταφοράς.
- **Απόφαση σχετικά με τους πόρους που θα αναφέρουμε**. Ο MCP server σας διαθέτει πόρους, εργαλεία και προτροπές, πρέπει να αποφασίσετε ποιον να αναφέρετε.
- **Ενσωμάτωση του πελάτη σε μια εφαρμογή φιλοξενίας**. Μόλις μάθετε τις δυνατότητες του διακομιστή, πρέπει να ενσωματώσετε αυτό στην εφαρμογή φιλοξενίας σας έτσι ώστε αν ένας χρήστης πληκτρολογήσει μια προτροπή ή άλλη εντολή, να ενεργοποιηθεί η αντίστοιχη λειτουργία του διακομιστή.

Τώρα που κατανοούμε σε γενικές γραμμές τι πρόκειται να κάνουμε, ας δούμε ένα παράδειγμα παρακάτω.

### Ένα παράδειγμα πελάτη

Ας δούμε αυτό το παράδειγμα πελάτη:

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

// Λίστα με προτροπές
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

// Κλήση εργαλείου
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Στον παραπάνω κώδικα:

- Εισάγουμε τις βιβλιοθήκες
- Δημιουργούμε μια παρουσία πελάτη και τη συνδέουμε χρησιμοποιώντας stdio για μεταφορά.
- Αναφέρουμε προτροπές, πόρους και εργαλεία και τα εκτελούμε όλα.

Ορίστε, ένας πελάτης που μπορεί να μιλήσει με έναν MCP Server.

Ας αφιερώσουμε χρόνο στην επόμενη ενότητα άσκησης για να αναλύσουμε κάθε τμήμα κώδικα και να εξηγήσουμε τι συμβαίνει.

## Άσκηση: Συγγραφή πελάτη

Όπως είπαμε παραπάνω, ας αφιερώσουμε χρόνο για να εξηγήσουμε τον κώδικα, και σίγουρα γράψτε κώδικα παράλληλα αν θέλετε.

### -1- Εισαγωγή των βιβλιοθηκών

Ας εισαγάγουμε τις βιβλιοθήκες που χρειαζόμαστε, θα χρειαστούμε αναφορές σε έναν πελάτη και στο επιλεγμένο πρωτόκολλο μεταφοράς, το stdio. Το stdio είναι ένα πρωτόκολλο για προγράμματα που προορίζονται να τρέξουν στον τοπικό σας υπολογιστή. Το SSE είναι ένα άλλο πρωτόκολλο μεταφοράς που θα δείξουμε σε μελλοντικά κεφάλαια αλλά αυτή είναι η άλλη σας επιλογή. Για τώρα όμως, ας συνεχίσουμε με stdio.

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

Για Java, θα δημιουργήσετε έναν πελάτη που συνδέεται με τον MCP server από την προηγούμενη άσκηση. Χρησιμοποιώντας την ίδια δομή έργου Java Spring Boot από το [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), δημιουργήστε μια νέα κλάση Java με όνομα `SDKClient` στο φάκελο `src/main/java/com/microsoft/mcp/sample/client/` και προσθέστε τις ακόλουθες εισαγωγές:

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

Θα χρειαστεί να δημιουργήσουμε μια παρουσία της μεταφοράς και μια της παρουσίας του πελάτη μας:

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

- Δημιουργήθηκε παρουσία μεταφοράς stdio. Σημειώστε πώς καθορίζεται η εντολή και τα ορίσματα για το πώς να βρεθεί και να ξεκινήσει ο διακομιστής, καθώς είναι κάτι που θα χρειαστεί να κάνουμε καθώς δημιουργούμε τον πελάτη.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Δημιουργήθηκε παρουσία πελάτη δίνοντάς του όνομα και έκδοση.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Συνδέθηκε ο πελάτης με την επιλεγμένη μεταφορά.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Δημιουργήστε παραμέτρους διακομιστή για σύνδεση stdio
server_params = StdioServerParameters(
    command="mcp",  # Εκτελέσιμο
    args=["run", "server.py"],  # Προαιρετικά ορίσματα γραμμής εντολών
    env=None,  # Προαιρετικές μεταβλητές περιβάλλοντος
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Αρχικοποιήστε τη σύνδεση
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Στον παραπάνω κώδικα:

- Εισαγωγή των απαραίτητων βιβλιοθηκών
- Δημιουργία ενός αντικειμένου παραμέτρων διακομιστή, καθώς θα το χρησιμοποιήσουμε για να τρέξουμε τον διακομιστή ώστε να μπορούμε να συνδεθούμε με τον πελάτη μας.
- Ορισμός μεθόδου `run` που καλεί με τη σειρά της `stdio_client` η οποία ξεκινά μια συνεδρία πελάτη.
- Δημιουργία σημείου εισόδου όπου παρέχουμε τη μέθοδο `run` στην `asyncio.run`.

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

Στον παραπάνω κώδικα:

- Εισαγωγή των απαραίτητων βιβλιοθηκών.
- Δημιουργία μεταφοράς stdio και ενός πελάτη `mcpClient`. Αυτό θα το χρησιμοποιήσουμε για να καταγράψουμε και να εκτελέσουμε λειτουργίες στον MCP Server.

Σημείωση, στο "Arguments", μπορείτε είτε να δείξετε στο *.csproj* είτε στο εκτελέσιμο αρχείο.

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

Στον παραπάνω κώδικα:

- Δημιουργία βασικής μεθόδου που ρυθμίζει μια μεταφορά SSE που δείχνει στο `http://localhost:8080` όπου θα τρέχει ο MCP server μας.
- Δημιουργία κλάσης πελάτη που δέχεται τη μεταφορά ως παράμετρο στον κατασκευαστή.
- Στη μέθοδο `run`, δημιουργούμε έναν σύγχρονο πελάτη MCP χρησιμοποιώντας τη μεταφορά και ξεκινάμε τη σύνδεση.
- Χρήση της μεταφοράς SSE (Server-Sent Events) που είναι κατάλληλη για επικοινωνία βασισμένη σε HTTP με MCP servers Java Spring Boot.

#### Rust

Σημείωση: αυτός ο πελάτης Rust υποθέτει ότι ο διακομιστής είναι ένα αδερφικό έργο με όνομα "calculator-server" στον ίδιο φάκελο. Ο παρακάτω κώδικας θα ξεκινήσει τον διακομιστή και θα συνδεθεί σε αυτόν.

```rust
async fn main() -> Result<(), RmcpError> {
    // Υποθέστε ότι ο διακομιστής είναι ένα αδελφό έργο με το όνομα "calculator-server" στον ίδιο φάκελο
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

    // TODO: Καταχώρηση εργαλείων

    // TODO: Κλήση του εργαλείου προσθήκης με παραμέτρους = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Καταγραφή των χαρακτηριστικών του διακομιστή

Τώρα, έχουμε έναν πελάτη που μπορεί να συνδεθεί όταν τρέξει το πρόγραμμα. Ωστόσο, δεν καταγράφει τα χαρακτηριστικά του, οπότε ας το κάνουμε αυτό τώρα:

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

Εδώ καταγράφουμε τους διαθέσιμους πόρους, `list_resources()` και τα εργαλεία, `list_tools` και τα τυπώνουμε.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Παραπάνω είναι ένα παράδειγμα για το πώς μπορούμε να καταγράψουμε τα εργαλεία στον διακομιστή. Για κάθε εργαλείο, στη συνέχεια τυπώνουμε το όνομά του.

#### Java

```java
// Λίστα και επίδειξη εργαλείων
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Μπορείτε επίσης να κάνετε ping στον διακομιστή για να επαληθεύσετε τη σύνδεση
client.ping();
```

Στον παραπάνω κώδικα:

- Κλήση της μεθόδου `listTools()` για να πάρουμε όλα τα διαθέσιμα εργαλεία από τον MCP server.
- Χρήση της μεθόδου `ping()` για να επαληθεύσουμε ότι η σύνδεση με τον διακομιστή λειτουργεί.
- Το `ListToolsResult` περιέχει πληροφορίες για όλα τα εργαλεία, συμπεριλαμβανομένων των ονομάτων, των περιγραφών και των σχημάτων εισόδου τους.

Τέλεια, τώρα έχουμε καταγράψει όλες τις λειτουργίες. Τώρα το ερώτημα είναι πότε τις χρησιμοποιούμε; Αυτός ο πελάτης είναι αρκετά απλός, απλός με την έννοια ότι θα χρειαστεί να καλούμε ρητά τις λειτουργίες όταν τις θέλουμε. Στο επόμενο κεφάλαιο, θα δημιουργήσουμε έναν πιο προηγμένο πελάτη που θα έχει πρόσβαση στο δικό του μεγάλο γλωσσικό μοντέλο, LLM. Για τώρα όμως, ας δούμε πώς μπορούμε να εκτελέσουμε τις λειτουργίες στο διακομιστή:

#### Rust

Στη βασική συνάρτηση, μετά την αρχικοποίηση του πελάτη, μπορούμε να αρχικοποιήσουμε τον διακομιστή και να καταγράψουμε μερικά από τα χαρακτηριστικά του.

```rust
// Αρχικοποίηση
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Καταχώριση εργαλείων
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Εκτέλεση λειτουργιών

Για να εκτελέσουμε τις λειτουργίες πρέπει να βεβαιωθούμε ότι καθορίζουμε τα σωστά ορίσματα και σε ορισμένες περιπτώσεις το όνομα του τι προσπαθούμε να εκτελέσουμε.

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

// καλέστε την προτροπή
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Στον παραπάνω κώδικα:

- Διαβάζουμε έναν πόρο, τον καλούμε με `readResource()` καθορίζοντας `uri`. Να πώς πιθανότατα μοιάζει στην πλευρά του διακομιστή:

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

    Η τιμή `uri` μας `file://example.txt` συμφωνεί με το `file://{name}` στο διακομιστή. Το `example.txt` θα αντιστοιχηθεί στο `name`.

- Καλούμε ένα εργαλείο, το καλούμε καθορίζοντας το `name` του και τα `arguments` του ως εξής:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Παίρνουμε μια προτροπή, για να πάρουμε μια προτροπή, καλούμε `getPrompt()` με `name` και `arguments`. Ο κώδικας του διακομιστή μοιάζει ως εξής:

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

    και ο κώδικας του πελάτη σας θα μοιάζει ως εξής για να ταιριάζει με όσα δηλώθηκαν στο διακομιστή:

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

Στον παραπάνω κώδικα:

- Κλήση πόρου με όνομα `greeting` χρησιμοποιώντας `read_resource`.
- Εκτέλεση εργαλείου με όνομα `add` χρησιμοποιώντας `call_tool`.

#### .NET

1. Ας προσθέσουμε κάποιο κώδικα για την κλήση εργαλείου:

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

Στον παραπάνω κώδικα:

- Κλήση πολλαπλών εργαλείων αριθμομηχανής χρησιμοποιώντας τη μέθοδο `callTool()` με αντικείμενα `CallToolRequest`.
- Κάθε κλήση εργαλείου καθορίζει το όνομα του εργαλείου και έναν `Map` επιχειρημάτων που απαιτούνται από το εργαλείο.
- Τα εργαλεία διακομιστή αναμένουν συγκεκριμένα ονόματα παραμέτρων (όπως "a", "b" για μαθηματικές λειτουργίες).
- Τα αποτελέσματα επιστρέφονται ως αντικείμενα `CallToolResult` που περιέχουν την απάντηση από τον διακομιστή.

#### Rust

```rust
// Καλέστε το εργαλείο προσθήκης με επιχειρήματα = {"a": 3, "b": 2}
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

Προσθέστε την ακόλουθη εγγραφή στην ενότητα "scripts" στο *package.json*:

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

Πρώτα, βεβαιωθείτε ότι ο MCP server σας τρέχει στο `http://localhost:8080`. Στη συνέχεια εκτελέστε τον πελάτη:

```bash
# Δημιουργήστε το έργο σας
./mvnw clean compile

# Εκτελέστε τον πελάτη
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Εναλλακτικά, μπορείτε να εκτελέσετε ολόκληρο το έργο πελάτη που παρέχεται στο φάκελο λύσης `03-GettingStarted\02-client\solution\java`:

```bash
# Πλοηγηθείτε στον κατάλογο της λύσης
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

Σε αυτήν την άσκηση, θα χρησιμοποιήσετε όσα μάθατε σχετικά με τη δημιουργία πελάτη αλλά θα δημιουργήσετε έναν πελάτη δικό σας.

Εδώ είναι ένας διακομιστής που μπορείτε να χρησιμοποιήσετε και πρέπει να τον καλέσετε μέσω του κώδικα πελάτη σας, δείτε αν μπορείτε να προσθέσετε περισσότερα χαρακτηριστικά στο διακομιστή για να τον κάνετε πιο ενδιαφέρον.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Δημιουργήστε έναν διακομιστή MCP
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

// Ξεκινήστε τη λήψη μηνυμάτων από το stdin και την αποστολή μηνυμάτων στο stdout

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

# Δημιουργία ενός διακομιστή MCP
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

Δείτε αυτό το έργο για το πώς μπορείτε να [προσθέσετε προτροπές και πόρους](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Επίσης, ελέγξτε αυτόν τον σύνδεσμο για το πώς να εκτελείτε [προτροπές και πόρους](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Στο [προηγούμενο τμήμα](../../../../03-GettingStarted/01-first-server), μάθατε πώς να δημιουργήσετε έναν απλό MCP server με Rust. Μπορείτε να συνεχίσετε να χτίζετε πάνω σε αυτό ή να δείτε αυτόν τον σύνδεσμο για περισσότερα παραδείγματα MCP server βασισμένα σε Rust: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Λύση

Ο **φάκελος λύσης** περιέχει πλήρεις, έτοιμες προς εκτέλεση υλοποιήσεις πελατών που δείχνουν όλες τις έννοιες που καλύφθηκαν σε αυτό το σεμινάριο. Κάθε λύση περιλαμβάνει τόσο κώδικα πελάτη όσο και διακομιστή οργανωμένους σε ξεχωριστά, αυτοτελή έργα.

### 📁 Δομή Λύσης

Το φάκελο λύσης οργανώνεται κατά γλώσσα προγραμματισμού:

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

Κάθε λύση ειδική για γλώσσα παρέχει:

- **Πλήρης υλοποίηση πελάτη** με όλες τις λειτουργίες από το σεμινάριο
- **Λειτουργική δομή έργου** με σωστές εξαρτήσεις και διαμόρφωση
- **Σενάρια κατασκευής και εκτέλεσης** για εύκολη εγκατάσταση και εκτέλεση
- **Λεπτομερές README** με οδηγίες ειδικές για τη γλώσσα
- **Καταγραφή σφαλμάτων** και παραδείγματα επεξεργασίας αποτελεσμάτων

### 📖 Χρήση των λύσεων

1. **Πηγαίνετε στον φάκελο της προτιμώμενης γλώσσας:**

   ```bash
   cd solution/typescript/    # Για TypeScript
   cd solution/java/          # Για Java
   cd solution/python/        # Για Python
   cd solution/dotnet/        # Για .NET
   ```

2. **Ακολουθήστε τις οδηγίες στο README** σε κάθε φάκελο για:
   - Εγκατάσταση εξαρτήσεων
   - Κατασκευή του έργου
   - Εκτέλεση του πελάτη

3. **Παράδειγμα εξόδου** που θα δείτε:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Για πλήρη τεκμηρίωση και βήμα προς βήμα οδηγίες, δείτε: **[📖 Τεκμηρίωση Λύσης](./solution/README.md)**

## 🎯 Πλήρη Παραδείγματα

Έχουμε παρέχει πλήρεις, λειτουργικές υλοποιήσεις πελατών για όλες τις γλώσσες προγραμματισμού που καλύφθηκαν σε αυτό το σεμινάριο. Αυτά τα παραδείγματα δείχνουν όλη τη λειτουργικότητα που περιγράφηκε παραπάνω και μπορούν να χρησιμοποιηθούν ως αναφορές υλοποίησης ή σημεία εκκίνησης για τα δικά σας έργα.

### Διαθέσιμα Πλήρη Παραδείγματα

| Γλώσσα | Αρχείο | Περιγραφή |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Πλήρης πελάτης Java χρησιμοποιώντας μεταφορά SSE με πλήρη διαχείριση σφαλμάτων |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Πλήρης πελάτης C# χρησιμοποιώντας μεταφορά stdio με αυτόματη εκκίνηση διακομιστή |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Πλήρης πελάτης TypeScript με πλήρη υποστήριξη πρωτοκόλλου MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Πλήρης πελάτης Python χρησιμοποιώντας μοτίβα async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Πλήρης πελάτης Rust χρησιμοποιώντας Tokio για ασύγχρονες λειτουργίες |

Κάθε πλήρες παράδειγμα περιλαμβάνει:

- ✅ **Εγκατάσταση σύνδεσης** και διαχείριση σφαλμάτων
- ✅ **Ανακάλυψη διακομιστή** (εργαλεία, πόροι, προτροπές όπου είναι εφαρμόσιμο)
- ✅ **Λειτουργίες αριθμομηχανής** (πρόσθεση, αφαίρεση, πολλαπλασιασμός, διαίρεση, βοήθεια)
- ✅ **Επεξεργασία αποτελεσμάτων** και μορφοποιημένη έξοδος
- ✅ **Πληρης διαχείριση σφαλμάτων**

- ✅ **Καθαρός, τεκμηριωμένος κώδικας** με σχολιασμούς βήμα προς βήμα

### Ξεκινώντας με Πλήρη Παραδείγματα

1. **Επιλέξτε την προτιμώμενη γλώσσα σας** από τον πίνακα πιο πάνω
2. **Εξετάστε το πλήρες αρχείο παραδείγματος** για να κατανοήσετε την πλήρη υλοποίηση
3. **Τρέξτε το παράδειγμα** ακολουθώντας τις οδηγίες στο [`complete_examples.md`](./complete_examples.md)
4. **Τροποποιήστε και επεκτείνετε** το παράδειγμα για τη συγκεκριμένη περίπτωση χρήσης σας

Για αναλυτική τεκμηρίωση σχετικά με την εκτέλεση και παραμετροποίηση αυτών των παραδειγμάτων, δείτε: **[📖 Τεκμηρίωση Πλήρων Παραδειγμάτων](./complete_examples.md)**

### 💡 Λύση vs. Πλήρη Παραδείγματα

| **Φάκελος Λύσης** | **Πλήρη Παραδείγματα** |
|--------------------|--------------------- |
| Πλήρης δομή έργου με αρχεία κατασκευής | Υλοποιήσεις σε ένα αρχείο |
| Έτοιμα προς εκτέλεση με εξαρτήσεις | Εστιασμένα παραδείγματα κώδικα |
| Παραγωγική ρύθμιση | Εκπαιδευτική αναφορά |
| Εργαλεία ειδικά για γλώσσα | Σύγκριση μεταξύ γλωσσών |

Και οι δύο προσεγγίσεις είναι πολύτιμες - χρησιμοποιήστε τον **φάκελο λύσης** για πλήρη έργα και τα **πλήρη παραδείγματα** για μάθηση και αναφορά.

## Βασικά Συμπεράσματα

Τα βασικά συμπεράσματα αυτού του κεφαλαίου σχετικά με τους πελάτες είναι τα εξής:

- Μπορούν να χρησιμοποιηθούν τόσο για την ανακάλυψη όσο και για την κλήση λειτουργιών στον διακομιστή.
- Μπορούν να ξεκινήσουν διακομιστή ενώ ο ίδιος ξεκινά (όπως σε αυτό το κεφάλαιο) αλλά οι πελάτες μπορούν επίσης να συνδεθούν σε ήδη τρέχοντες διακομιστές.
- Είναι ένας εξαιρετικός τρόπος για να δοκιμάσετε τις δυνατότητες του διακομιστή σε σύγκριση με εναλλακτικές όπως ο Inspector όπως περιγράφηκε στο προηγούμενο κεφάλαιο.

## Πρόσθετοι Πόροι

- [Κατασκευή πελατών στο MCP](https://modelcontextprotocol.io/quickstart/client)

## Παραδείγματα

- [Αριθμομηχανή Java](../samples/java/calculator/README.md)
- [Αριθμομηχανή .NET](../../../../03-GettingStarted/samples/csharp)
- [Αριθμομηχανή JavaScript](../samples/javascript/README.md)
- [Αριθμομηχανή TypeScript](../samples/typescript/README.md)
- [Αριθμομηχανή Python](../../../../03-GettingStarted/samples/python)
- [Αριθμομηχανή Rust](../../../../03-GettingStarted/samples/rust)

## Τι Ακολουθεί

- Επόμενο: [Δημιουργία πελάτη με LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->