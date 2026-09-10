# Δημιουργία πελάτη με LLM

Μέχρι τώρα, έχετε δει πώς να δημιουργήσετε έναν διακομιστή και έναν πελάτη. Ο πελάτης είχε τη δυνατότητα να καλεί ρητά τον διακομιστή για να καταγράψει τα εργαλεία, τους πόρους και τα prompt του. Ωστόσο, αυτή δεν είναι μια πολύ πρακτική προσέγγιση. Οι χρήστες σας ζουν στην εποχή των πρακτόρων και περιμένουν να χρησιμοποιούν prompts και να επικοινωνούν με ένα LLM. Δεν τους ενδιαφέρει αν χρησιμοποιείτε MCP για να αποθηκεύσετε τις δυνατότητές σας· απλά περιμένουν να αλληλεπιδράσουν χρησιμοποιώντας φυσική γλώσσα. Πώς λύνουμε λοιπόν αυτό το θέμα; Η λύση είναι να προσθέσουμε ένα LLM στον πελάτη.

## Επισκόπηση

Σε αυτό το μάθημα, εστιάζουμε στην προσθήκη ενός LLM για τον πελάτη σας και δείχνουμε πώς αυτό προσφέρει μια πολύ καλύτερη εμπειρία για τον χρήστη σας.

## Στόχοι Μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Δημιουργήσετε έναν πελάτη με ένα LLM.
- Αλληλεπιδράσετε απρόσκοπτα με έναν διακομιστή MCP χρησιμοποιώντας ένα LLM.
- Παρέχετε καλύτερη εμπειρία τελικού χρήστη στην πλευρά του πελάτη.

## Προσέγγιση

Ας προσπαθήσουμε να κατανοήσουμε την προσέγγιση που πρέπει να ακολουθήσουμε. Η προσθήκη ενός LLM φαίνεται απλή, αλλά θα το κάνουμε πραγματικά;

Να πώς θα αλληλεπιδρά ο πελάτης με τον διακομιστή:

1. Καθιέρωση σύνδεσης με τον διακομιστή.

1. Καταγραφή δυνατοτήτων, prompts, πόρων και εργαλείων, και αποθήκευση του σχήματός τους.

1. Προσθήκη ενός LLM και μεταβίβαση των αποθηκευμένων δυνατοτήτων και του σχήματός τους σε μορφή που κατανοεί το LLM.

1. Διαχείριση ενός user prompt μεταβιβάζοντάς το στο LLM μαζί με τα εργαλεία που έχει καταγράψει ο πελάτης.

Τέλεια, τώρα που καταλαβαίνουμε πώς μπορούμε να το κάνουμε σε υψηλό επίπεδο, ας δοκιμάσουμε στην παρακάτω άσκηση.

## Άσκηση: Δημιουργία πελάτη με έναν LLM

Σε αυτή την άσκηση, θα μάθουμε να προσθέτουμε ένα LLM στον πελάτη μας.

### Πιστοποίηση με χρήση GitHub Personal Access Token

Η δημιουργία ενός token στο GitHub είναι μια απλή διαδικασία. Δείτε πώς μπορείτε να το κάνετε:

- Μεταβείτε στις Ρυθμίσεις του GitHub – Κάντε κλικ στην εικόνα προφίλ σας πάνω δεξιά και επιλέξτε Ρυθμίσεις.
- Πλοηγηθείτε στις Ρυθμίσεις Προγραμματιστή – Κάτω, κάντε κλικ στις Ρυθμίσεις Προγραμματιστή.
- Επιλέξτε Personal Access Tokens – Κάντε κλικ στα “Fine-grained tokens” και μετά “Generate new token”.
- Διαμορφώστε το Token σας – Προσθέστε ένα σημείωμα για αναφορά, ορίστε ημερομηνία λήξης και επιλέξτε τα απαιτούμενα δικαιώματα (permissions). Σε αυτή την περίπτωση βεβαιωθείτε ότι έχετε προσθέσει το δικαίωμα Models.
- Δημιουργήστε και Αντιγράψτε το Token – Κάντε κλικ στο Generate token, και φροντίστε να το αντιγράψετε αμέσως, καθώς δεν θα ξαναδειτε το token.

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

- Εισάγει τις απαιτούμενες βιβλιοθήκες
- Δημιουργεί μια κλάση με δύο μέλη, `client` και `openai` που θα μας βοηθήσουν να διαχειριστούμε έναν πελάτη και να αλληλεπιδράσουμε με ένα LLM αντίστοιχα.
- Διαμορφώσαμε την παρουσία του LLM μας ώστε να χρησιμοποιεί τα GitHub Models, ορίζοντας το `baseUrl` ώστε να δείχνει στο inference API.

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

- Εισάγει τις απαραίτητες βιβλιοθήκες για MCP
- Δημιούργησε έναν πελάτη

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

Πρώτα, θα χρειαστεί να προσθέσετε τις εξαρτήσεις LangChain4j στο αρχείο `pom.xml`. Προσθέστε αυτές τις εξαρτήσεις για να ενεργοποιήσετε την ενσωμάτωση MCP και το OpenAI-συμβατό MiniMax API:

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

Ορίστε το κλειδί API του MiniMax και, προαιρετικά, το endpoint και το μοντέλο.
Το `MINIMAX_MODEL_ID` υποστηρίζει `MiniMax-M3` και `MiniMax-M2.7`. Αν
το `OPENAI_BASE_URL` δεν είναι ορισμένο, το `MINIMAX_REGION` υποστηρίζει `global_en` και `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Για να επιλέξετε το endpoint ανά περιοχή, παραλείψτε το `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Στη συνέχεια, δημιουργήστε την κλάση πελάτη Java:

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

        // Δημιουργήστε μεταφορά MCP για σύνδεση με διακομιστή
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

Στον προηγούμενο κώδικα έχουμε:

- **Προσθέσαμε τις εξαρτήσεις LangChain4j**: Απαραίτητες για την ενσωμάτωση MCP και το OpenAI-συμβατό MiniMax API
- **Εισάγαμε τις βιβλιοθήκες LangChain4j**: Για ενσωμάτωση MCP και λειτουργικότητα μοντέλου συνομιλίας OpenAI
- **Δημιουργήσαμε ένα `ChatLanguageModel`**: Διαμορφωμένο να χρησιμοποιεί MiniMax με το κλειδί API, endpoint και υποστηριζόμενο ID μοντέλου MiniMax
- **Ρυθμίσαμε τη μεταφορά HTTP**: Χρησιμοποιώντας Server-Sent Events (SSE) για σύνδεση με τον διακομιστή MCP
- **Δημιουργήσαμε έναν πελάτη MCP**: Ο οποίος θα χειρίζεται την επικοινωνία με τον διακομιστή
- **Χρησιμοποιήσαμε την ενσωματωμένη υποστήριξη MCP του LangChain4j**: Που απλοποιεί την ενσωμάτωση μεταξύ LLMs και MCP servers

#### Rust

Αυτό το παράδειγμα υποθέτει ότι έχετε έναν MCP διακομιστή που βασίζεται σε Rust σε λειτουργία. Αν δεν έχετε, ανατρέξτε ξανά στο μάθημα [01-first-server](../01-first-server/README.md) για να δημιουργήσετε τον διακομιστή.

Μόλις έχετε τον Rust MCP διακομιστή σας, ανοίξτε ένα τερματικό και μεταβείτε στον ίδιο φάκελο με τον διακομιστή. Στη συνέχεια τρέξτε την παρακάτω εντολή για να δημιουργήσετε ένα νέο project πελάτη LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Προσθέστε τις ακόλουθες εξαρτήσεις στο αρχείο `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Δεν υπάρχει επίσημη βιβλιοθήκη Rust για το OpenAI, ωστόσο, το crate `async-openai` είναι μια [βιβλιοθήκη που διατηρείται από την κοινότητα](https://platform.openai.com/docs/libraries/rust#rust) που χρησιμοποιείται συχνά.

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

    // Διαμόρφωση πελάτη OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Διαμόρφωση πελάτη MCP
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

    // ΠΡΕΠΕΙ ΝΑ ΓΙΝΕΙ: Λήψη λίστας εργαλείων MCP

    // ΠΡΕΠΕΙ ΝΑ ΓΙΝΕΙ: Συνομιλία LLM με κλήσεις εργαλείων

    Ok(())
}
```

Αυτός ο κώδικας δημιουργεί μια βασική εφαρμογή Rust που θα συνδεθεί με έναν MCP διακομιστή και τα GitHub Models για αλληλεπιδράσεις LLM.

> [!IMPORTANT]
> Βεβαιωθείτε ότι έχετε ορίσει την μεταβλητή περιβάλλοντος `OPENAI_API_KEY` με το token GitHub σας πριν τρέξετε την εφαρμογή.

Τέλεια, για το επόμενο βήμα, ας καταγράψουμε τις δυνατότητες του διακομιστή.

### -2- Καταγραφή δυνατοτήτων διακομιστή

Τώρα θα συνδεθούμε στον διακομιστή και θα ζητήσουμε τις δυνατότητές του:

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

    // καταχώριση εργαλείων
    const toolsResult = await this.client.listTools();
}
```

Στον προηγούμενο κώδικα έχουμε:

- Προσθέσει κώδικα για σύνδεση με τον διακομιστή, `connectToServer`.
- Δημιουργήσει μια μέθοδο `run` υπεύθυνη για τη ροή της εφαρμογής μας. Μέχρι τώρα καταγράφει μόνο τα εργαλεία, αλλά σύντομα θα προσθέσουμε περισσότερα.

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

Να τι προσθέσαμε:

- Καταγραφή πόρων και εργαλείων και εκτύπωσή τους. Για τα εργαλεία καταγράφουμε επίσης την `inputSchema` που θα χρησιμοποιήσουμε αργότερα.

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

- Καταγράψει τα εργαλεία που είναι διαθέσιμα στον MCP Server
- Για κάθε εργαλείο, καταγράψει όνομα, περιγραφή και το σχήμα του. Το τελευταίο θα χρησιμοποιήσουμε για να καλέσουμε τα εργαλεία σύντομα.

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

- Δημιουργήσει ένα `McpToolProvider` που αυτόματα ανιχνεύει και καταχωρεί όλα τα εργαλεία από τον MCP server
- Ο πάροχος εργαλείων χειρίζεται εσωτερικά τη μετατροπή μεταξύ των σχημάτων εργαλείων MCP και της μορφής εργαλείων του LangChain4j
- Αυτή η προσέγγιση αφαιρεί την ανάγκη χειροκίνητης καταγραφής και μετατροπής εργαλείων

#### Rust

Η ανάκτηση εργαλείων από τον MCP server γίνεται με τη μέθοδο `list_tools`. Στη συνάρτηση `main` σας, μετά τη δημιουργία του MCP client, προσθέστε τον ακόλουθο κώδικα:

```rust
// Λάβετε τη λίστα εργαλείων MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Μετατροπή δυνατοτήτων διακομιστή σε εργαλεία LLM

Το επόμενο βήμα μετά την καταγραφή των δυνατοτήτων του διακομιστή είναι να τις μετατρέψουμε σε μορφή που κατανοεί το LLM. Μόλις το κάνουμε, μπορούμε να παρέχουμε αυτές τις δυνατότητες ως εργαλεία στο LLM μας.

#### TypeScript

1. Προσθέστε τον ακόλουθο κώδικα για να μετατρέψετε την απόκριση από τον MCP Server σε μορφή εργαλείου που μπορεί να χρησιμοποιήσει το LLM:

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

    Ο παραπάνω κώδικας παίρνει μια απόκριση από τον MCP Server και τη μετατρέπει σε μορφή ορισμού εργαλείου που κατανοεί το LLM.

2. Ας ενημερώσουμε επόμενα τη μέθοδο `run` για να καταγράψει τις δυνατότητες του διακομιστή:

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

    Στον προηγούμενο κώδικα, έχουμε ενημερώσει τη μέθοδο `run` ώστε να διατρέχει το αποτέλεσμα και για κάθε εγγραφή να καλεί το `openAiToolAdapter`.

#### Python

1. Πρώτα, ας δημιουργήσουμε την ακόλουθη συνάρτηση μετατροπής:

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

    Στη συνάρτηση `convert_to_llm_tools` παίρνουμε μια απόκριση εργαλείου MCP και τη μετατρέπουμε σε μορφή που κατανοεί το LLM.

2. Στη συνέχεια, ας ενημερώσουμε τον κώδικα του πελάτη μας ώστε να χρησιμοποιεί αυτή τη συνάρτηση:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Εδώ προσθέτουμε μια κλήση στη `convert_to_llm_tool` για να μετατρέψουμε την απόκριση εργαλείου MCP σε κάτι που μπορούμε να δώσουμε αργότερα στο LLM.

#### .NET

1. Ας προσθέσουμε κώδικα για να μετατρέψουμε την απόκριση εργαλείου MCP σε μορφή που κατανοεί το LLM

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
- Ορίσει λειτουργικότητα που δημιουργεί ένα `FunctionDefinition` που περνάει σε ένα `ChatCompletionsDefinition`. Το τελευταίο είναι κάτι που κατανοεί το LLM.

2. Ας δούμε πώς μπορούμε να ενημερώσουμε υπάρχοντα κώδικα για να αξιοποιήσουμε αυτή τη συνάρτηση:

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

// Ρυθμίστε την υπηρεσία AI με εργαλεία LLM και MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Στον προηγούμενο κώδικα έχουμε:

- Ορίσει ένα απλό interface `Bot` για αλληλεπιδράσεις με φυσική γλώσσα
- Χρησιμοποιήσει το `AiServices` του LangChain4j για να δέσει αυτόματα το LLM με τον πάροχο εργαλείων MCP
- Το πλαίσιο χειρίζεται αυτόματα τη μετατροπή του σχήματος και τις κλήσεις συναρτήσεων στο παρασκήνιο
- Αυτή η προσέγγιση καταργεί την χειροκίνητη μετατροπή εργαλείων - το LangChain4j χειρίζεται όλη την πολυπλοκότητα της μετατροπής εργαλείων MCP σε μορφή συμβατή με τα LLM

#### Rust

Για να μετατρέψουμε την απόκριση εργαλείου MCP σε μορφή που κατανοεί το LLM, θα προσθέσουμε μια βοηθητική συνάρτηση που μορφοποιεί την καταγραφή εργαλείων. Προσθέστε τον ακόλουθο κώδικα στο αρχείο `main.rs` κάτω από τη συνάρτηση `main`. Αυτή θα καλείται κατά τα αιτήματα προς το LLM:

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

Τέλεια, είμαστε έτοιμοι να χειριστούμε αιτήματα από τον χρήστη, οπότε ας προχωρήσουμε σε αυτό.

### -4- Διαχείριση αιτήματος χρήστη (prompt)

Σε αυτό το μέρος του κώδικα, θα διαχειριστούμε τα αιτήματα των χρηστών.

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


        // 2. Κλήση στο εργαλείο του διακομιστή
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Κάντε κάτι με το αποτέλεσμα
        // ΕΚΚΑΘΑΡΙΣΗ

        }
    }
    ```

    Στον προηγούμενο κώδικα:

    - Προσθέσαμε μια μέθοδο `callTools`.
    - Η μέθοδος παίρνει μια απόκριση LLM και ελέγχει ποια εργαλεία έχουν κληθεί, αν υπάρχουν:

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

2. Ενημερώστε τη μέθοδο `run` ώστε να περιλαμβάνει κλήσεις προς το LLM και κλήση της `callTools`:

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
        model: "gpt-4.1-mini",
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
import { z } from "zod"; // Εισαγωγή του zod για επικύρωση σχημάτων

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
          // ΕΚΚΡΕΜΕΣ ΕΝΕΡΓΕΙΕΣ
    
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
    
        // 3. Εξετάστε την απάντηση του LLM, για κάθε επιλογή, ελέγξτε αν έχει κλήσεις εργαλείων
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

1. Ας προσθέσουμε μερικές εισαγωγές που απαιτούνται για κλήση σε LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Στη συνέχεια, ας προσθέσουμε τη συνάρτηση που θα καλέσει το LLM:

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

    - Περάσει τις συναρτήσεις μας που βρήκαμε στον MCP server και μετατρέψαμε, στο LLM.
    - Στη συνέχεια καλέσαμε το LLM με αυτές τις συναρτήσεις.
    - Μετά, εξετάζουμε το αποτέλεσμα για να δούμε ποιες συναρτήσεις πρέπει να καλέσουμε, αν υπάρχουν.
    - Τέλος, περνάμε έναν πίνακα συναρτήσεων που πρέπει να κληθούν.

3. Τελικό βήμα, ας ενημερώσουμε τον βασικό μας κώδικα:

    ```python
    prompt = "Add 2 to 20"

    # ρώτα το LLM ποια εργαλεία να χρησιμοποιήσει, αν υπάρχουν
    functions_to_call = call_llm(prompt, functions)

    # κάλεσε τις προτεινόμενες λειτουργίες
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Εκεί, αυτό ήταν το τελευταίο βήμα, στον παραπάνω κώδικα:

    - Καλούμε ένα εργαλείο MCP μέσω της `call_tool` χρησιμοποιώντας μια συνάρτηση που το LLM θεώρησε ότι πρέπει να κληθεί βάσει του prompt μας.
    - Εκτυπώνουμε το αποτέλεσμα της κλήσης εργαλείου στον MCP Server.

#### .NET

1. Ας δούμε λίγο κώδικα για ένα αίτημα prompt προς το LLM:

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

    Στον προηγούμενο κώδικα έχουμε:

    - Ανάκτηση εργαλείων από τον MCP server, `var tools = await GetMcpTools()`.
    - Ορισμό του prompt χρήστη `userMessage`.
    - Δημιουργία ενός αντικειμένου options καθορίζοντας μοντέλο και εργαλεία.
    - Εγγραφή ενός αιτήματος προς το LLM.

2. Ένα τελευταίο βήμα, ας δούμε αν το LLM νομίζει ότι πρέπει να καλέσουμε μια συνάρτηση:

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

    - Περάσει επανάληψη σε μια λίστα κλήσεων συναρτήσεων.
    - Για κάθε κλήση εργαλείου, ανάλυση ονόματος και ορισμάτων και κλήση εργαλείου στον MCP server χρησιμοποιώντας τον MCP client. Τελικά, εκτυπώνουμε τα αποτελέσματα.

Να ο κώδικας πλήρως:

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
    // Εκτέλεση αιτημάτων φυσικής γλώσσας που χρησιμοποιούν αυτόματα τα εργαλεία MCP
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

- Χρήση απλών prompt φυσικής γλώσσας για αλληλεπίδραση με τα εργαλεία του MCP server
- Το πλαίσιο LangChain4j χειρίζεται αυτόματα:
  - Τη μετατροπή prompts χρηστών σε κλήσεις εργαλείων όταν χρειάζεται
  - Την κλήση των κατάλληλων εργαλείων MCP βάσει απόφασης του LLM
  - Τη διαχείριση της ροής της συνομιλίας ανάμεσα στο LLM και στον MCP server
- Η μέθοδος `bot.chat()` επιστρέφει απαντήσεις σε φυσική γλώσσα που μπορεί να περιλαμβάνουν αποτελέσματα από την εκτέλεση εργαλείων MCP
- Αυτή η προσέγγιση παρέχει μια απρόσκοπτη εμπειρία χρήστη όπου οι χρήστες δεν χρειάζεται να γνωρίζουν για την υποκείμενη υλοποίηση MCP

Πλήρες παράδειγμα κώδικα:

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

Εδώ γίνεται το μεγαλύτερο μέρος της δουλειάς. Θα καλέσουμε το LLM με το αρχικό prompt χρήστη, θα επεξεργαστούμε την απόκριση για να δούμε αν χρειάζεται να κληθούν εργαλεία. Αν ναι, θα καλέσουμε αυτά τα εργαλεία και θα συνεχίσουμε τη συνομιλία με το LLM μέχρι να μην είναι πλέον απαραίτητες κλήσεις εργαλείων και να έχουμε μια τελική απόκριση.


Θα πραγματοποιήσουμε πολλαπλές κλήσεις προς το LLM, οπότε ας ορίσουμε μια συνάρτηση που θα χειρίζεται την κλήση στο LLM. Προσθέστε την παρακάτω συνάρτηση στο αρχείο σας `main.rs`:

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

Αυτή η συνάρτηση δέχεται τον πελάτη LLM, μια λίστα μηνυμάτων (συμπεριλαμβανομένης της ερώτησης χρήστη), εργαλεία από τον διακομιστή MCP, και στέλνει ένα αίτημα στο LLM, επιστρέφοντας την απάντηση.

Η απάντηση από το LLM θα περιέχει έναν πίνακα από `choices`. Θα χρειαστεί να επεξεργαστούμε το αποτέλεσμα για να δούμε αν υπάρχουν `tool_calls`. Αυτό μας ενημερώνει ότι το LLM ζητά να κληθεί ένα συγκεκριμένο εργαλείο με ορίσματα. Προσθέστε τον παρακάτω κώδικα στο κάτω μέρος του αρχείου `main.rs` για να ορίσετε μια συνάρτηση που θα χειρίζεται την απάντηση του LLM:

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

    // Εκτύπωση περιεχομένου αν είναι διαθέσιμο
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Διαχείριση κλήσεων εργαλείων
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Προσθήκη μηνύματος βοηθού

        // Εκτέλεση κάθε κλήσης εργαλείου
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Προσθήκη αποτελέσματος εργαλείου στα μηνύματα
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Συνέχιση συνομιλίας με τα αποτελέσματα εργαλείων
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

Αν υπάρχουν `tool_calls`, εξάγει τις πληροφορίες του εργαλείου, καλεί τον διακομιστή MCP με το αίτημα του εργαλείου και προσθέτει τα αποτελέσματα στα μηνύματα της συζήτησης. Στη συνέχεια συνεχίζει τη συζήτηση με το LLM και τα μηνύματα ενημερώνονται με την απάντηση του βοηθού και τα αποτελέσματα της κλήσης εργαλείου.

Για να εξάγουμε τις πληροφορίες της κλήσης εργαλείου που επιστρέφει το LLM για κλήσεις MCP, θα προσθέσουμε μια ακόμη βοηθητική συνάρτηση για να εξαγάγουμε όλα όσα χρειάζονται για την πραγματοποίηση της κλήσης. Προσθέστε τον παρακάτω κώδικα στο κάτω μέρος του αρχείου `main.rs`:

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

Με όλα τα κομμάτια στη θέση τους, μπορούμε τώρα να χειριστούμε την αρχική ερώτηση του χρήστη και να καλέσουμε το LLM. Ενημερώστε τη συνάρτηση `main` σας ώστε να περιλαμβάνει τον παρακάτω κώδικα:

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

Αυτό θα ερωτήσει το LLM με την αρχική ερώτηση του χρήστη που ζητά το άθροισμα δύο αριθμών, και θα επεξεργαστεί την απάντηση για να χειριστεί δυναμικά τις κλήσεις εργαλείων.

Τέλεια, τα καταφέρατε!

## Ανάθεση

Πάρτε τον κώδικα από την άσκηση και επεκτείνετε τον διακομιστή με μερικά περισσότερα εργαλεία. Στη συνέχεια δημιουργήστε έναν πελάτη με ένα LLM, όπως στην άσκηση, και δοκιμάστε το με διαφορετικές ερωτήσεις για να βεβαιωθείτε ότι όλα τα εργαλεία του διακομιστή καλούνται δυναμικά. Αυτός ο τρόπος κατασκευής πελάτη σημαίνει ότι ο τελικός χρήστης θα έχει μια εξαιρετική εμπειρία, καθώς μπορεί να χρησιμοποιεί ερωτήσεις αντί για ακριβείς εντολές πελάτη και δεν αντιλαμβάνεται ότι καλείται οποιοσδήποτε διακομιστής MCP.

## Λύση

[Solution](./solution/README.md)

## Βασικά Συμπεράσματα

- Η προσθήκη ενός LLM στον πελάτη σας παρέχει έναν καλύτερο τρόπο στους χρήστες να αλληλεπιδρούν με διακομιστές MCP.
- Πρέπει να μετατρέψετε την απάντηση του διακομιστή MCP σε κάτι που το LLM μπορεί να καταλάβει.

## Παραδείγματα

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Επιπλέον Πόροι

## Τι Ακολουθεί

- Επόμενο: [Κατανάλωση διακομιστή χρησιμοποιώντας Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->