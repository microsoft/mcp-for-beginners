# Δημιουργία πελάτη με LLM

Μέχρι τώρα, έχετε δει πώς να δημιουργήσετε έναν διακομιστή και έναν πελάτη. Ο πελάτης ήταν σε θέση να καλέσει ρητά τον διακομιστή για να απαριθμήσει τα εργαλεία, τους πόρους και τα prompts του. Ωστόσο, δεν είναι πολύ πρακτική προσέγγιση. Ο χρήστης σας ζει στην εποχή των πρακτόρων και αναμένει να χρησιμοποιεί prompts και να επικοινωνεί με ένα LLM για να το κάνει. Για τον χρήστη σας, δεν έχει σημασία αν χρησιμοποιείτε MCP ή όχι για να αποθηκεύσετε τις δυνατότητές σας, αλλά αναμένει να χρησιμοποιεί φυσική γλώσσα για να αλληλεπιδράσει. Πώς το λύνουμε αυτό; Η λύση είναι να προσθέσουμε ένα LLM στον πελάτη.

## Επισκόπηση

Σε αυτό το μάθημα εστιάζουμε στην προσθήκη ενός LLM στον πελάτη σας και δείχνουμε πώς αυτό παρέχει μια πολύ καλύτερη εμπειρία για τον χρήστη σας.

## Στόχοι Μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Δημιουργήσετε έναν πελάτη με ένα LLM.
- Αλληλεπιδράσετε απρόσκοπτα με έναν MCP διακομιστή χρησιμοποιώντας ένα LLM.
- Παρέχετε μια καλύτερη εμπειρία τελικού χρήστη στην πλευρά του πελάτη.

## Προσέγγιση

Ας προσπαθήσουμε να κατανοήσουμε την προσέγγιση που πρέπει να ακολουθήσουμε. Η προσθήκη ενός LLM ακούγεται απλή, αλλά θα το κάνουμε πραγματικά;

Έτσι θα αλληλεπιδρά ο πελάτης με τον διακομιστή:

1. Εγκαθιδρύστε σύνδεση με τον διακομιστή.

1. Απαριθμήστε τις δυνατότητες, τα prompts, τους πόρους και τα εργαλεία, και αποθηκεύστε το σχήμα τους.

1. Προσθέστε ένα LLM και περάστε τις αποθηκευμένες δυνατότητες και το σχήμα τους σε μορφή που κατανοεί το LLM.

1. Διαχειριστείτε ένα prompt χρήστη περνώντας το στο LLM μαζί με τα εργαλεία που απαριθμεί ο πελάτης.

Τέλεια, τώρα που καταλαβαίνουμε πώς μπορούμε να το κάνουμε σε υψηλό επίπεδο, ας το δοκιμάσουμε στην παρακάτω άσκηση.

## Άσκηση: Δημιουργία πελάτη με ένα LLM

Σε αυτή την άσκηση, θα μάθουμε πώς να προσθέσουμε ένα LLM στον πελάτη μας.

### Πιστοποίηση με χρήση GitHub Personal Access Token

Η δημιουργία ενός token GitHub είναι μια απλή διαδικασία. Δείτε πώς μπορείτε να το κάνετε:

- Μεταβείτε στις Ρυθμίσεις GitHub – Κάντε κλικ στην εικόνα προφίλ σας στην πάνω δεξιά γωνία και επιλέξτε Ρυθμίσεις.
- Πλοηγηθείτε στις Ρυθμίσεις Προγραμματιστή – Κάντε κύλιση προς τα κάτω και κάντε κλικ στις Ρυθμίσεις Προγραμματιστή.
- Επιλέξτε Personal Access Tokens – Κάντε κλικ στα Fine-grained tokens και μετά στο Generate new token.
- Διαμορφώστε το Token σας – Προσθέστε μια σημείωση για αναφορά, ορίστε ημερομηνία λήξης και επιλέξτε τα απαραίτητα δικαιώματα (scopes). Σε αυτή την περίπτωση βεβαιωθείτε ότι προσθέτετε το δικαίωμα Models.
- Δημιουργήστε και Αντιγράψτε το Token – Κάντε κλικ στο Generate token και βεβαιωθείτε ότι το αντιγράψατε αμέσως, καθώς δεν θα μπορείτε να το δείτε ξανά.

### -1- Σύνδεση με τον διακομιστή

Ας δημιουργήσουμε πρώτα τον πελάτη μας:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Εισαγωγή του zod για επικύρωση σχήματος

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

Στον προηγούμενο κώδικα έχουμε:

- Εισάγει τις απαραίτητες βιβλιοθήκες
- Δημιουργήσει μια κλάση με δύο μέλη, `client` και `openai` που θα μας βοηθήσουν να διαχειριστούμε έναν πελάτη και να αλληλεπιδράσουμε με ένα LLM αντίστοιχα.
- Διαμορφώσει το στιγμιότυπο LLM μας να χρησιμοποιεί GitHub Models ορίζοντας το `baseUrl` ώστε να δείχνει στο inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Δημιουργία παραμέτρων διακομιστή για σύνδεση stdio
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
            # Αρχικοποίηση της σύνδεσης
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Στον προηγούμενο κώδικα έχουμε:

- Εισάγει τις απαραίτητες βιβλιοθήκες για MCP
- Δημιουργήσει έναν πελάτη

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

Πρώτα, θα χρειαστεί να προσθέσετε τις εξαρτήσεις LangChain4j στο αρχείο `pom.xml` σας. Προσθέστε αυτές τις εξαρτήσεις για να ενεργοποιήσετε την ενσωμάτωση MCP και την υποστήριξη GitHub Models:

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

Έπειτα δημιουργήστε την κλάση πελάτη Java:

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
    
    public static void main(String[] args) throws Exception {        // Διαμορφώστε το LLM για να χρησιμοποιεί τα Μοντέλα GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Δημιουργήστε μεταφορά MCP για σύνδεση με τον διακομιστή
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Δημιουργήστε πελάτη MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Στον προηγούμενο κώδικα έχουμε:

- **Προσθέσει τις εξαρτήσεις LangChain4j**: Απαραίτητες για ενσωμάτωση MCP, επίσημο πελάτη OpenAI και υποστήριξη GitHub Models
- **Εισάγει τις βιβλιοθήκες LangChain4j**: Για ενσωμάτωση MCP και λειτουργικότητα μοντέλου συνομιλίας OpenAI
- **Δημιουργήσει ένα `ChatLanguageModel`**: Διαμορφωμένο να χρησιμοποιεί GitHub Models με το GitHub token σας
- **Ρυθμίσει HTTP μεταφορά**: Χρησιμοποιώντας Server-Sent Events (SSE) για σύνδεση με τον MCP διακομιστή
- **Δημιουργήσει έναν MCP πελάτη**: Που θα χειρίζεται την επικοινωνία με τον διακομιστή
- **Χρησιμοποιήσει την ενσωματωμένη υποστήριξη MCP του LangChain4j**: Που απλοποιεί την ενσωμάτωση μεταξύ LLMs και MCP διακομιστών

#### Rust

Αυτό το παράδειγμα υποθέτει ότι έχετε έναν MCP διακομιστή βασισμένο σε Rust σε λειτουργία. Αν δεν έχετε, ανατρέξτε στο μάθημα [01-first-server](../01-first-server/README.md) για να δημιουργήσετε τον διακομιστή.

Μόλις έχετε τον Rust MCP διακομιστή σας, ανοίξτε ένα τερματικό και πλοηγηθείτε στον ίδιο φάκελο με τον διακομιστή. Έπειτα εκτελέστε την ακόλουθη εντολή για να δημιουργήσετε ένα νέο έργο πελάτη LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Προσθέστε τις ακόλουθες εξαρτήσεις στο αρχείο `Cargo.toml` σας:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Δεν υπάρχει επίσημη βιβλιοθήκη Rust για OpenAI, ωστόσο, το crate `async-openai` είναι μια [βιβλιοθήκη που διατηρείται από την κοινότητα](https://platform.openai.com/docs/libraries/rust#rust) και χρησιμοποιείται ευρέως.

Ανοίξτε το αρχείο `src/main.rs` και αντικαταστήστε το περιεχόμενό του με τον ακόλουθο κώδικα:

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
    // Αρχικό μήνυμα
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Ρύθμιση πελάτη OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Ρύθμιση πελάτη MCP
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

    // TODO: Λήψη καταλόγου εργαλείων MCP

    // TODO: Συνομιλία LLM με κλήσεις εργαλείων

    Ok(())
}
```

Αυτός ο κώδικας ρυθμίζει μια βασική εφαρμογή Rust που θα συνδεθεί με έναν MCP διακομιστή και GitHub Models για αλληλεπιδράσεις LLM.

> [!IMPORTANT]
> Βεβαιωθείτε ότι έχετε ορίσει τη μεταβλητή περιβάλλοντος `OPENAI_API_KEY` με το GitHub token σας πριν τρέξετε την εφαρμογή.

Τέλεια, για το επόμενο βήμα, ας απαριθμήσουμε τις δυνατότητες στον διακομιστή.

### -2- Απαρίθμηση δυνατοτήτων διακομιστή

Τώρα θα συνδεθούμε με τον διακομιστή και θα ζητήσουμε τις δυνατότητές του:

#### Typescript

Στην ίδια κλάση, προσθέστε τις ακόλουθες μεθόδους:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // λίστα εργαλείων
    const toolsResult = await this.client.listTools();
}
```

Στον προηγούμενο κώδικα έχουμε:

- Προσθέσει κώδικα για σύνδεση με τον διακομιστή, `connectToServer`.
- Δημιουργήσει μια μέθοδο `run` υπεύθυνη για τη ροή της εφαρμογής μας. Μέχρι στιγμής απαριθμεί μόνο τα εργαλεία αλλά σύντομα θα προσθέσουμε περισσότερα.

#### Python

```python
# Καταχώριση διαθέσιμων πόρων
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Καταχώριση διαθέσιμων εργαλείων
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Αυτό προσθέσαμε:

- Απαρίθμηση πόρων και εργαλείων και εκτύπωσή τους. Για τα εργαλεία απαριθμούμε επίσης το `inputSchema` που θα χρησιμοποιήσουμε αργότερα.

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

Στον προηγούμενο κώδικα έχουμε:

- Απαριθμήσει τα εργαλεία που είναι διαθέσιμα στον MCP διακομιστή
- Για κάθε εργαλείο, απαριθμήσει το όνομα, την περιγραφή και το σχήμα του. Το τελευταίο είναι κάτι που θα χρησιμοποιήσουμε για να καλέσουμε τα εργαλεία σύντομα.

#### Java

```java
// Δημιουργήστε έναν πάροχο εργαλείων που ανακαλύπτει αυτόματα τα εργαλεία MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Ο πάροχος εργαλείων MCP χειρίζεται αυτόματα:
// - Τη λίστα διαθέσιμων εργαλείων από τον διακομιστή MCP
// - Τη μετατροπή των σχημάτων εργαλείων MCP σε μορφή LangChain4j
// - Τη διαχείριση εκτέλεσης εργαλείων και απαντήσεων
```

Στον προηγούμενο κώδικα έχουμε:

- Δημιουργήσει έναν `McpToolProvider` που ανακαλύπτει και καταχωρεί αυτόματα όλα τα εργαλεία από τον MCP διακομιστή
- Ο πάροχος εργαλείων χειρίζεται εσωτερικά τη μετατροπή μεταξύ των σχημάτων εργαλείων MCP και της μορφής εργαλείων του LangChain4j
- Αυτή η προσέγγιση αφαιρεί την ανάγκη χειροκίνητης απαρίθμησης και μετατροπής εργαλείων

#### Rust

Η ανάκτηση εργαλείων από τον MCP διακομιστή γίνεται με τη μέθοδο `list_tools`. Στη συνάρτηση `main`, μετά τη ρύθμιση του MCP πελάτη, προσθέστε τον ακόλουθο κώδικα:

```rust
// Λήψη λίστας εργαλείων MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Μετατροπή δυνατοτήτων διακομιστή σε εργαλεία LLM

Το επόμενο βήμα μετά την απαρίθμηση των δυνατοτήτων του διακομιστή είναι να τις μετατρέψουμε σε μορφή που κατανοεί το LLM. Μόλις το κάνουμε αυτό, μπορούμε να παρέχουμε αυτές τις δυνατότητες ως εργαλεία στο LLM μας.

#### TypeScript

1. Προσθέστε τον ακόλουθο κώδικα για να μετατρέψετε την απάντηση από τον MCP διακομιστή σε μορφή εργαλείου που μπορεί να χρησιμοποιήσει το LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Δημιουργήστε ένα σχήμα zod βασισμένο στο input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Ορίστε ρητά τον τύπο σε "function"
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

    Ο παραπάνω κώδικας παίρνει μια απάντηση από τον MCP διακομιστή και την μετατρέπει σε μορφή ορισμού εργαλείου που κατανοεί το LLM.

1. Ας ενημερώσουμε τη μέθοδο `run` για να απαριθμήσουμε τις δυνατότητες του διακομιστή:

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

    Στον προηγούμενο κώδικα, ενημερώσαμε τη μέθοδο `run` ώστε να διατρέχει το αποτέλεσμα και για κάθε εγγραφή να καλεί το `openAiToolAdapter`.

#### Python

1. Πρώτα, ας δημιουργήσουμε την ακόλουθη συνάρτηση μετατροπής

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

    Στη συνάρτηση `convert_to_llm_tools` παίρνουμε μια απάντηση εργαλείου MCP και την μετατρέπουμε σε μορφή που κατανοεί το LLM.

1. Έπειτα, ας ενημερώσουμε τον κώδικα του πελάτη μας για να χρησιμοποιήσει αυτή τη συνάρτηση ως εξής:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Εδώ, προσθέτουμε μια κλήση στο `convert_to_llm_tool` για να μετατρέψουμε την απάντηση εργαλείου MCP σε κάτι που μπορούμε να δώσουμε στο LLM αργότερα.

#### .NET

1. Ας προσθέσουμε κώδικα για να μετατρέψουμε την απάντηση εργαλείου MCP σε κάτι που κατανοεί το LLM

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

Στον προηγούμενο κώδικα έχουμε:

- Δημιουργήσει μια συνάρτηση `ConvertFrom` που παίρνει όνομα, περιγραφή και σχήμα εισόδου.
- Ορίσει λειτουργικότητα που δημιουργεί ένα `FunctionDefinition` που περνά σε ένα `ChatCompletionsDefinition`. Το τελευταίο είναι κάτι που κατανοεί το LLM.

1. Ας δούμε πώς μπορούμε να ενημερώσουμε υπάρχοντα κώδικα για να εκμεταλλευτούμε αυτή τη συνάρτηση:

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
// Δημιουργήστε μια διεπαφή Bot για αλληλεπίδραση φυσικής γλώσσας
public interface Bot {
    String chat(String prompt);
}

// Διαμορφώστε την υπηρεσία AI με εργαλεία LLM και MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Στον προηγούμενο κώδικα έχουμε:

- Ορίσει ένα απλό interface `Bot` για αλληλεπιδράσεις φυσικής γλώσσας
- Χρησιμοποιήσει το `AiServices` του LangChain4j για αυτόματη σύνδεση του LLM με τον πάροχο εργαλείων MCP
- Το πλαίσιο χειρίζεται αυτόματα τη μετατροπή σχημάτων εργαλείων και τις κλήσεις συναρτήσεων στο παρασκήνιο
- Αυτή η προσέγγιση εξαλείφει τη χειροκίνητη μετατροπή εργαλείων - το LangChain4j χειρίζεται όλη την πολυπλοκότητα της μετατροπής εργαλείων MCP σε μορφή συμβατή με LLM

#### Rust

Για να μετατρέψουμε την απάντηση εργαλείου MCP σε μορφή που κατανοεί το LLM, θα προσθέσουμε μια βοηθητική συνάρτηση που μορφοποιεί την απαρίθμηση εργαλείων. Προσθέστε τον ακόλουθο κώδικα στο αρχείο `main.rs` κάτω από τη συνάρτηση `main`. Αυτό θα καλείται όταν γίνονται αιτήματα προς το LLM:

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

Τέλεια, είμαστε έτοιμοι να χειριστούμε αιτήματα χρηστών, ας το κάνουμε τώρα.

### -4- Χειρισμός αιτήματος prompt χρήστη

Σε αυτό το μέρος του κώδικα, θα χειριστούμε αιτήματα χρηστών.

#### TypeScript

1. Προσθέστε μια μέθοδο που θα χρησιμοποιηθεί για να καλέσουμε το LLM μας:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Καλέστε το εργαλείο του διακομιστή
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Κάντε κάτι με το αποτέλεσμα
        // ΠΡΕΠΕΙ ΝΑ ΓΙΝΕΙ

        }
    }
    ```

    Στον προηγούμενο κώδικα:

    - Προσθέσαμε τη μέθοδο `callTools`.
    - Η μέθοδος παίρνει μια απάντηση LLM και ελέγχει ποια εργαλεία έχουν κληθεί, αν υπάρχουν:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // κλήση εργαλείου
        }
        ```

    - Καλεί ένα εργαλείο, αν το LLM υποδεικνύει ότι πρέπει να κληθεί:

        ```typescript
        // 2. Καλέστε το εργαλείο του διακομιστή
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Κάντε κάτι με το αποτέλεσμα
        // ΠΡΕΠΕΙ ΝΑ ΓΙΝΕΙ
        ```

1. Ενημερώστε τη μέθοδο `run` για να συμπεριλάβει κλήσεις στο LLM και την κλήση `callTools`:

    ```typescript

    // 1. Δημιουργήστε μηνύματα που είναι είσοδος για το LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Κλήση του LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Εξετάστε την απάντηση του LLM, για κάθε επιλογή, ελέγξτε αν έχει κλήσεις εργαλείων
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Τέλεια, ας δούμε τον πλήρη κώδικα:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Εισαγωγή του zod για επικύρωση σχήματος

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ίσως χρειαστεί να αλλάξει σε αυτό το url στο μέλλον: https://models.github.ai/inference
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
          // Δημιουργία σχήματος zod βασισμένου στο input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Ορισμός τύπου ρητά σε "function"
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
    
    
          // 2. Κλήση του εργαλείου του διακομιστή
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Κάντε κάτι με το αποτέλεσμα
          // ΠΡΕΠΕΙ ΝΑ ΓΙΝΕΙ
    
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
    
        // 1. Επεξεργασία της απάντησης LLM, για κάθε επιλογή, έλεγχος αν έχει κλήσεις εργαλείων
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

1. Ας προσθέσουμε μερικές εισαγωγές που χρειάζονται για να καλέσουμε ένα LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Έπειτα, ας προσθέσουμε τη συνάρτηση που θα καλέσει το LLM:

    ```python
    # llm

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
            # Προαιρετικές παράμετροι
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

    Στον προηγούμενο κώδικα έχουμε:

    - Περνάμε τις συναρτήσεις μας, που βρήκαμε στον MCP διακομιστή και μετατρέψαμε, στο LLM.
    - Έπειτα καλέσαμε το LLM με αυτές τις συναρτήσεις.
    - Μετά, ελέγχουμε το αποτέλεσμα για να δούμε ποιες συναρτήσεις πρέπει να καλέσουμε, αν υπάρχουν.
    - Τέλος, περνάμε έναν πίνακα συναρτήσεων για κλήση.

1. Τελικό βήμα, ας ενημερώσουμε τον κύριο κώδικα μας:

    ```python
    prompt = "Add 2 to 20"

    # ρώτησε το LLM ποια εργαλεία να χρησιμοποιήσει, αν υπάρχουν
    functions_to_call = call_llm(prompt, functions)

    # κάλεσε τις προτεινόμενες λειτουργίες
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Εκεί, αυτό ήταν το τελικό βήμα, στον παραπάνω κώδικα:

    - Καλούμε ένα εργαλείο MCP μέσω `call_tool` χρησιμοποιώντας μια συνάρτηση που το LLM θεώρησε ότι πρέπει να καλέσουμε βάσει του prompt μας.
    - Εκτυπώνουμε το αποτέλεσμα της κλήσης εργαλείου στον MCP διακομιστή.

#### .NET

1. Ας δείξουμε λίγο κώδικα για να κάνουμε ένα αίτημα prompt σε LLM:

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

    Στον προηγούμενο κώδικα έχουμε:

    - Φέρει εργαλεία από τον MCP διακομιστή, `var tools = await GetMcpTools()`.
    - Ορίσει ένα prompt χρήστη `userMessage`.
    - Δημιουργήσει ένα αντικείμενο επιλογών που καθορίζει μοντέλο και εργαλεία.
    - Κάνει ένα αίτημα προς το LLM.

1. Ένα τελευταίο βήμα, ας δούμε αν το LLM θεωρεί ότι πρέπει να καλέσουμε μια συνάρτηση:

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

    Στον προηγούμενο κώδικα έχουμε:

    - Κάνει βρόχο μέσα σε μια λίστα κλήσεων συναρτήσεων.
    - Για κάθε κλήση εργαλείου, αναλύει το όνομα και τα ορίσματα και καλεί το εργαλείο στον MCP διακομιστή χρησιμοποιώντας τον MCP πελάτη. Τέλος εκτυπώνει τα αποτελέσματα.

Ορίστε ο πλήρης κώδικας:

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
    // Εκτελέστε αιτήματα φυσικής γλώσσας που χρησιμοποιούν αυτόματα τα εργαλεία MCP
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

Στον προηγούμενο κώδικα έχουμε:

- Χρησιμοποιήσει απλά prompts φυσικής γλώσσας για αλληλεπίδραση με τα εργαλεία του MCP διακομιστή
- Το πλαίσιο LangChain4j χειρίζεται αυτόματα:
  - Τη μετατροπή των prompts χρήστη σε κλήσεις εργαλείων όταν χρειάζεται
  - Την κλήση των κατάλληλων εργαλείων MCP βάσει της απόφασης του LLM
  - Τη διαχείριση της ροής συνομιλίας μεταξύ LLM και MCP διακομιστή
- Η μέθοδος `bot.chat()` επιστρέφει απαντήσεις φυσικής γλώσσας που μπορεί να περιλαμβάνουν αποτελέσματα από εκτελέσεις εργαλείων MCP
- Αυτή η προσέγγιση παρέχει μια απρόσκοπτη εμπειρία χρήστη όπου οι χρήστες δεν χρειάζεται να γνωρίζουν την υποκείμενη υλοποίηση MCP

Πλήρες παράδειγμα κώδικα:

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

Εδώ συμβαίνει το μεγαλύτερο μέρος της δουλειάς. Θα καλέσουμε το LLM με το αρχικό prompt χρήστη, έπειτα θα επεξεργαστούμε την απάντηση για να δούμε αν χρειάζεται να κληθούν εργαλεία. Αν ναι, θα καλέσουμε αυτά τα εργαλεία και θα συνεχίσουμε τη συνομιλία με το LLM μέχρι να μην χρειάζονται άλλες κλήσεις εργαλείων και να έχουμε μια τελική απάντηση.

Θα κάνουμε πολλαπλές κλήσεις στο LLM, οπότε ας ορίσουμε μια συνάρτηση που θα χειρίζεται την κλήση LLM. Προσθέστε την ακόλουθη συνάρτηση στο αρχείο `main.rs`:

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

Αυτή η συνάρτηση παίρνει τον πελάτη LLM, μια λίστα μηνυμάτων (συμπεριλαμβανομένου του prompt χρήστη), εργαλεία από τον MCP διακομιστή, και στέλνει ένα αίτημα στο LLM, επιστρέφοντας την απάντηση.
Η απάντηση από το LLM θα περιέχει έναν πίνακα με `choices`. Θα χρειαστεί να επεξεργαστούμε το αποτέλεσμα για να δούμε αν υπάρχουν `tool_calls`. Αυτό μας ενημερώνει ότι το LLM ζητά να κληθεί ένα συγκεκριμένο εργαλείο με ορίσματα. Προσθέστε τον ακόλουθο κώδικα στο κάτω μέρος του αρχείου `main.rs` σας για να ορίσετε μια συνάρτηση που θα χειρίζεται την απάντηση του LLM:

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

    // Εκτύπωσε το περιεχόμενο αν είναι διαθέσιμο
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Διαχείριση κλήσεων εργαλείων
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Πρόσθεσε μήνυμα βοηθού

        // Εκτέλεσε κάθε κλήση εργαλείου
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Πρόσθεσε το αποτέλεσμα του εργαλείου στα μηνύματα
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Συνέχισε τη συνομιλία με τα αποτελέσματα των εργαλείων
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

Αν υπάρχουν `tool_calls`, εξάγει τις πληροφορίες του εργαλείου, καλεί τον MCP server με το αίτημα του εργαλείου, και προσθέτει τα αποτελέσματα στα μηνύματα της συνομιλίας. Στη συνέχεια συνεχίζει τη συνομιλία με το LLM και τα μηνύματα ενημερώνονται με την απάντηση του βοηθού και τα αποτελέσματα της κλήσης εργαλείου.

Για να εξάγουμε τις πληροφορίες κλήσης εργαλείου που επιστρέφει το LLM για κλήσεις MCP, θα προσθέσουμε μια ακόμα βοηθητική συνάρτηση για να εξάγει όλα όσα χρειάζονται για την κλήση. Προσθέστε τον ακόλουθο κώδικα στο κάτω μέρος του αρχείου `main.rs` σας:

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

Με όλα τα κομμάτια στη θέση τους, μπορούμε τώρα να χειριστούμε το αρχικό prompt του χρήστη και να καλέσουμε το LLM. Ενημερώστε τη συνάρτηση `main` σας ώστε να περιλαμβάνει τον ακόλουθο κώδικα:

```rust
// Συνομιλία LLM με κλήσεις εργαλείων
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

Αυτό θα κάνει ερώτημα στο LLM με το αρχικό prompt του χρήστη ζητώντας το άθροισμα δύο αριθμών, και θα επεξεργαστεί την απάντηση για να χειριστεί δυναμικά τις κλήσεις εργαλείων.

Τέλεια, τα καταφέρατε!

## Ανάθεση

Πάρτε τον κώδικα από την άσκηση και αναπτύξτε τον server με μερικά ακόμα εργαλεία. Έπειτα δημιουργήστε έναν client με ένα LLM, όπως στην άσκηση, και δοκιμάστε τον με διαφορετικά prompts για να βεβαιωθείτε ότι όλα τα εργαλεία του server καλούνται δυναμικά. Αυτός ο τρόπος δημιουργίας ενός client σημαίνει ότι ο τελικός χρήστης θα έχει μια εξαιρετική εμπειρία χρήσης καθώς μπορεί να χρησιμοποιεί prompts αντί για ακριβείς εντολές client, και να μην αντιλαμβάνεται ότι καλείται κάποιος MCP server.

## Λύση

[Λύση](/03-GettingStarted/03-llm-client/solution/README.md)

## Βασικά Σημεία

- Η προσθήκη ενός LLM στον client σας παρέχει έναν καλύτερο τρόπο για τους χρήστες να αλληλεπιδρούν με τους MCP Servers.
- Πρέπει να μετατρέψετε την απάντηση του MCP Server σε κάτι που το LLM μπορεί να κατανοήσει.

## Παραδείγματα

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Πρόσθετοι Πόροι

## Τι Ακολουθεί

- Επόμενο: [Κατανάλωση ενός server χρησιμοποιώντας το Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->