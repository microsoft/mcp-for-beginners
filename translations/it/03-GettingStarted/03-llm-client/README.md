# Creazione di un client con LLM

Finora, hai visto come creare un server e un client. Il client è stato in grado di chiamare esplicitamente il server per elencare i suoi strumenti, risorse e prompt. Tuttavia, questo non è un approccio molto pratico. I tuoi utenti vivono nell'era agentica e si aspettano di utilizzare prompt e comunicare con un LLM. Non importa se usi MCP per memorizzare le tue capacità; si aspettano semplicemente di interagire utilizzando il linguaggio naturale. Quindi, come risolviamo questo problema? La soluzione è aggiungere un LLM al client.

## Panoramica

In questa lezione ci concentriamo sull'aggiunta di un LLM al tuo client e mostriamo come questo offra un'esperienza molto migliore per il tuo utente.

## Obiettivi di apprendimento

Al termine di questa lezione, sarai in grado di:

- Creare un client con un LLM.
- Interagire senza problemi con un server MCP usando un LLM.
- Fornire una migliore esperienza utente finale sul lato client.

## Approccio

Cerchiamo di capire l'approccio che dobbiamo adottare. Aggiungere un LLM sembra semplice, ma lo faremo davvero?

Ecco come il client interagirà con il server:

1. Stabilire la connessione con il server.

1. Elencare capacità, prompt, risorse e strumenti, e salvare il loro schema.

1. Aggiungere un LLM e passare le capacità salvate e il loro schema in un formato che il LLM comprende.

1. Gestire un prompt dell'utente passandolo al LLM insieme agli strumenti elencati dal client.

Ottimo, ora che abbiamo capito come fare questo ad alto livello, proviamo nell'esercizio qui sotto.

## Esercizio: Creare un client con un LLM

In questo esercizio impareremo ad aggiungere un LLM al nostro client.

### Autenticazione usando GitHub Personal Access Token

Creare un token GitHub è un processo semplice. Ecco come puoi farlo:

- Vai su GitHub Settings – Clicca sulla tua immagine profilo in alto a destra e seleziona Settings.
- Naviga su Developer Settings – Scorri verso il basso e clicca su Developer Settings.
- Seleziona Personal Access Tokens – Clicca su Fine-grained tokens e poi su Generate new token.
- Configura il tuo token – Aggiungi una nota per riferimento, imposta una data di scadenza e seleziona gli ambiti necessari (permessi). In questo caso assicurati di aggiungere il permesso Models.
- Genera e copia il token – Clicca su Generate token, e assicurati di copiarlo immediatamente, perché non potrai più vederlo.

### -1- Collegarsi al server

Creiamo prima il nostro client:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importa zod per la validazione dello schema

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

Nel codice precedente abbiamo:

- Importato le librerie necessarie
- Creato una classe con due membri, `client` e `openai` che ci aiuteranno rispettivamente a gestire un client e interagire con un LLM.
- Configurato la nostra istanza LLM per usare GitHub Models impostando `baseUrl` per puntare all'API di inferenza.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Crea parametri del server per la connessione stdio
server_params = StdioServerParameters(
    command="mcp",  # Eseguibile
    args=["run", "server.py"],  # Argomenti opzionali della riga di comando
    env=None,  # Variabili d'ambiente opzionali
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inizializza la connessione
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Nel codice precedente abbiamo:

- Importato le librerie necessarie per MCP
- Creato un client

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

Prima, dovrai aggiungere le dipendenze LangChain4j al tuo file `pom.xml`. Aggiungi queste dipendenze per abilitare l'integrazione MCP e il supporto per GitHub Models:

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

Poi crea la tua classe client Java:

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
    
    public static void main(String[] args) throws Exception {        // Configura il LLM per utilizzare i modelli di GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Crea il trasporto MCP per la connessione al server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Crea il client MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Nel codice precedente abbiamo:

- **Aggiunto dipendenze LangChain4j**: necessarie per l'integrazione MCP, client ufficiale OpenAI e supporto GitHub Models
- **Importato le librerie LangChain4j**: per integrazione MCP e funzionalità chat model OpenAI
- **Creato un `ChatLanguageModel`**: configurato per usare GitHub Models con il tuo token GitHub
- **Configurato il trasporto HTTP**: usando Server-Sent Events (SSE) per connettersi al server MCP
- **Creato un client MCP**: che gestirà la comunicazione con il server
- **Utilizzato il supporto MCP integrato di LangChain4j**: che semplifica l'integrazione tra LLM e server MCP

#### Rust

Questo esempio presuppone che tu abbia un server MCP basato su Rust in esecuzione. Se non ne hai uno, torna alla lezione [01-first-server](../01-first-server/README.md) per creare il server.

Una volta che hai il tuo server MCP Rust, apri un terminale e naviga nella stessa directory del server. Poi esegui il seguente comando per creare un nuovo progetto client LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Aggiungi le seguenti dipendenze al tuo file `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Non esiste una libreria ufficiale Rust per OpenAI, tuttavia il crate `async-openai` è una [libreria mantenuta dalla comunità](https://platform.openai.com/docs/libraries/rust#rust) comunemente usata.

Apri il file `src/main.rs` e sostituisci il contenuto con il seguente codice:

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
    // Messaggio iniziale
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Configura il client OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Configura il client MCP
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

    // DA FARE: Ottieni l'elenco degli strumenti MCP

    // DA FARE: Conversazione LLM con chiamate agli strumenti

    Ok(())
}
```

Questo codice configura una semplice applicazione Rust che si connetterà a un server MCP e GitHub Models per interazioni LLM.

> [!IMPORTANT]
> Assicurati di impostare la variabile d’ambiente `OPENAI_API_KEY` con il tuo token GitHub prima di avviare l’applicazione.

Ottimo, per il prossimo passo, elenchiamo le capacità presenti sul server.

### -2- Elencare le capacità del server

Ora ci connetteremo al server e chiederemo le sue capacità:

#### Typescript

Nella stessa classe, aggiungi i seguenti metodi:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // elenco degli strumenti
    const toolsResult = await this.client.listTools();
}
```

Nel codice precedente abbiamo:

- Aggiunto codice per la connessione al server, `connectToServer`.
- Creato un metodo `run` responsabile di gestire il flusso della nostra app. Finora elenca solo gli strumenti ma a breve aggiungeremo altro.

#### Python

```python
# Elenca le risorse disponibili
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Elenca gli strumenti disponibili
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ecco cosa abbiamo aggiunto:

- Elencato risorse e strumenti e stampati. Per gli strumenti abbiamo anche elencato `inputSchema` che useremo più avanti.

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

Nel codice precedente abbiamo:

- Elencato gli strumenti disponibili sul server MCP
- Per ogni strumento, elencato nome, descrizione e il suo schema. Quest’ultimo è qualcosa che useremo presto per chiamare gli strumenti.

#### Java

```java
// Crea un provider di strumenti che scopre automaticamente gli strumenti MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Il provider di strumenti MCP gestisce automaticamente:
// - L'elenco degli strumenti disponibili dal server MCP
// - La conversione degli schemi degli strumenti MCP nel formato LangChain4j
// - La gestione dell'esecuzione degli strumenti e delle risposte
```

Nel codice precedente abbiamo:

- Creato un `McpToolProvider` che scopre automaticamente e registra tutti gli strumenti dal server MCP
- Il provider gestisce internamente la conversione tra gli schemi degli strumenti MCP e il formato strumenti di LangChain4j
- Questo approccio astrae il processo manuale di elenco e conversione degli strumenti

#### Rust

Il recupero degli strumenti dal server MCP si fa usando il metodo `list_tools`. Nella tua funzione `main`, dopo aver impostato il client MCP, aggiungi il seguente codice:

```rust
// Ottieni l'elenco degli strumenti MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Convertire le capacità del server in strumenti LLM

Il passo successivo dopo aver elencato le capacità del server è convertirle in un formato che il LLM comprende. Una volta fatto ciò, possiamo fornire queste capacità come strumenti al nostro LLM.

#### TypeScript

1. Aggiungi il seguente codice per convertire la risposta dal server MCP in un formato strumento che il LLM può usare:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Crea uno schema zod basato sull'input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Imposta esplicitamente il tipo su "funzione"
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

    Il codice sopra prende una risposta dal server MCP e la converte in un formato di definizione strumento che il LLM può comprendere.

1. Ora aggiorniamo il metodo `run` per elencare le capacità del server:

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

    Nel codice precedente abbiamo aggiornato il metodo `run` per mappare il risultato e per ogni voce chiamare `openAiToolAdapter`.

#### Python

1. Prima, creiamo la seguente funzione convertitrice

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

    Nella funzione sopra `convert_to_llm_tools` prendiamo una risposta strumento MCP e la convertiamo in un formato che il LLM può comprendere.

1. Poi aggiorniamo il codice client per usare questa funzione così:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Qui aggiungiamo una chiamata a `convert_to_llm_tool` per convertire la risposta strumento MCP in qualcosa che possiamo passare al LLM.

#### .NET

1. Aggiungiamo codice per convertire la risposta strumento MCP in qualcosa che il LLM può comprendere

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

Nel codice precedente abbiamo:

- Creato una funzione `ConvertFrom` che prende nome, descrizione e schema di input.
- Definito la funzionalità che crea una FunctionDefinition passata a una ChatCompletionsDefinition. Quest’ultima è qualcosa che il LLM può comprendere.

1. Vediamo come aggiornare un po’ di codice esistente per sfruttare questa funzione:

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
// Crea un'interfaccia Bot per l'interazione in linguaggio naturale
public interface Bot {
    String chat(String prompt);
}

// Configura il servizio AI con strumenti LLM e MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Nel codice precedente abbiamo:

- Definito una semplice interfaccia `Bot` per interazioni in linguaggio naturale
- Usato `AiServices` di LangChain4j per legare automaticamente il LLM con il provider di strumenti MCP
- Il framework gestisce automaticamente conversione degli schemi degli strumenti e chiamate di funzione dietro le quinte
- Questo approccio elimina la conversione manuale degli strumenti - LangChain4j si occupa di tutta la complessità

#### Rust

Per convertire la risposta strumento MCP in un formato comprensibile dal LLM, aggiungeremo una funzione helper che formatta l’elenco degli strumenti. Aggiungi il seguente codice al file `main.rs` sotto la funzione `main`. Verrà chiamata quando si fanno richieste al LLM:

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

Ottimo, ora siamo pronti a gestire richieste utente, quindi affrontiamo questo passo.

### -4- Gestire la richiesta di prompt utente

In questa parte del codice gestiremo le richieste degli utenti.

#### TypeScript

1. Aggiungi un metodo che sarà usato per chiamare il nostro LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Chiamare lo strumento del server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fare qualcosa con il risultato
        // DA FARE

        }
    }
    ```

    Nel codice precedente abbiamo:

    - Aggiunto un metodo `callTools`.
    - Il metodo prende una risposta LLM e controlla quali strumenti sono stati chiamati, se presenti:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // chiamare lo strumento
        }
        ```

    - Chiama uno strumento, se il LLM indica che deve essere chiamato:

        ```typescript
        // 2. Chiamare lo strumento del server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fare qualcosa con il risultato
        // DA FARE
        ```

1. Aggiorna il metodo `run` per includere chiamate al LLM e chiamare `callTools`:

    ```typescript

    // 1. Crea messaggi che sono input per il LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Chiamata al LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Analizza la risposta del LLM, per ogni scelta, verifica se ci sono chiamate a strumenti
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Ottimo, ecco il codice completo:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importa zod per la validazione dello schema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // potrebbe essere necessario cambiare in questo URL in futuro: https://models.github.ai/inference
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
          // Crea uno schema zod basato su input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Imposta esplicitamente il tipo su "function"
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
    
    
          // 2. Chiama lo strumento del server
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Fai qualcosa con il risultato
          // DA FARE
    
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
    
        // 1. Esamina la risposta LLM, per ogni scelta, verifica se contiene chiamate a strumenti
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

1. Aggiungiamo alcune importazioni necessarie per chiamare un LLM

    ```python
    # lm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Poi aggiungiamo la funzione che chiamerà il LLM:

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
            # Parametri opzionali
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

    Nel codice precedente abbiamo:

    - Passato al LLM le nostre funzioni, trovate sul server MCP e convertite.
    - Poi abbiamo chiamato il LLM con queste funzioni.
    - Poi stiamo ispezionando il risultato per vedere quali funzioni dovremmo chiamare, se ce ne sono.
    - Infine passiamo un array di funzioni da chiamare.

1. Ultimo passo, aggiorniamo il nostro codice principale:

    ```python
    prompt = "Add 2 to 20"

    # chiedi al LLM quali strumenti usare, se ce ne sono
    functions_to_call = call_llm(prompt, functions)

    # chiama le funzioni suggerite
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Quello è stato l’ultimo passo, nel codice sopra:

    - Chiamiamo un tool MCP tramite `call_tool` usando una funzione che il LLM ha deciso di chiamare in base al nostro prompt.
    - Stampiamo il risultato della chiamata strumento al server MCP.

#### .NET

1. Ecco un esempio di codice per fare una richiesta di prompt all’LLM:

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

    Nel codice precedente abbiamo:

    - Recuperato gli strumenti dal server MCP, `var tools = await GetMcpTools()`.
    - Definito un prompt utente `userMessage`.
    - Costruito un oggetto opzioni specificando modello e strumenti.
    - Fatto una richiesta al LLM.

1. Un ultimo passo, vediamo se il LLM pensa che dovremmo chiamare una funzione:

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

    Nel codice precedente abbiamo:

    - Ciclo su una lista di chiamate di funzioni.
    - Per ogni chiamata strumento, estraiamo nome e argomenti e chiamiamo lo strumento sul server MCP usando il client MCP. Infine stampiamo i risultati.

Ecco il codice completo:

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

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Eseguire richieste in linguaggio naturale che utilizzano automaticamente gli strumenti MCP
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

Nel codice precedente abbiamo:

- Usato prompt in linguaggio naturale semplici per interagire con gli strumenti del server MCP
- Il framework LangChain4j gestisce automaticamente:
  - La conversione dei prompt utente in chiamate a strumenti se necessario
  - La chiamata degli strumenti MCP appropriati basata sulla decisione del LLM
  - La gestione del flusso di conversazione tra LLM e server MCP
- Il metodo `bot.chat()` restituisce risposte in linguaggio naturale che possono includere risultati da esecuzioni di strumenti MCP
- Questo approccio fornisce un'esperienza utente fluida in cui gli utenti non devono conoscere l’implementazione sottostante MCP

Esempio completo di codice:

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

Qui avviene la maggior parte del lavoro. Chiameremo il LLM con il prompt iniziale dell’utente, poi elaboreremo la risposta per vedere se devono essere chiamati strumenti. Se sì, li chiameremo e continueremo la conversazione con il LLM fino a quando non saranno più necessarie chiamate a strumenti e avremo una risposta finale.

Faremo più chiamate al LLM, quindi definiamo una funzione che gestirà la chiamata LLM. Aggiungi la seguente funzione al file `main.rs`:

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

Questa funzione prende il client LLM, una lista di messaggi (incluso il prompt utente), gli strumenti dal server MCP, e invia una richiesta al LLM, restituendo la risposta.
La risposta dall'LLM conterrà un array di `choices`. Dovremo processare il risultato per verificare se sono presenti `tool_calls`. Questo ci fa sapere che l'LLM sta richiedendo che uno specifico strumento venga chiamato con argomenti. Aggiungi il seguente codice alla fine del tuo file `main.rs` per definire una funzione che gestisca la risposta dell'LLM:

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

    // Stampa il contenuto se disponibile
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Gestisci le chiamate degli strumenti
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Aggiungi messaggio dell'assistente

        // Esegui ogni chiamata allo strumento
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Aggiungi il risultato dello strumento ai messaggi
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Continua la conversazione con i risultati degli strumenti
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

Se sono presenti `tool_calls`, estrae le informazioni dello strumento, chiama il server MCP con la richiesta dello strumento e aggiunge i risultati ai messaggi della conversazione. Quindi continua la conversazione con l'LLM e i messaggi vengono aggiornati con la risposta dell'assistente e i risultati della chiamata allo strumento.

Per estrarre le informazioni della chiamata allo strumento che l'LLM restituisce per le chiamate MCP, aggiungeremo un'altra funzione helper per estrarre tutto ciò che serve per effettuare la chiamata. Aggiungi il seguente codice alla fine del tuo file `main.rs`:

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

Con tutti i pezzi al loro posto, ora possiamo gestire il prompt iniziale dell'utente e chiamare l'LLM. Aggiorna la tua funzione `main` per includere il seguente codice:

```rust
// Conversazione LLM con chiamate agli strumenti
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

Questo interrogherà l'LLM con il prompt iniziale dell'utente che chiede la somma di due numeri, e elaborerà la risposta per gestire dinamicamente le chiamate agli strumenti.

Ottimo, ce l'hai fatta!

## Esercizio

Prendi il codice dall'esercizio e sviluppa il server con qualche strumento in più. Poi crea un client con un LLM, come nell'esercizio, e testalo con diversi prompt per assicurarti che tutti gli strumenti del server vengano chiamati dinamicamente. Questo modo di costruire un client garantisce all'utente finale un'ottima esperienza d'uso poiché può usare prompt, invece di comandi client esatti, senza accorgersi che un server MCP viene chiamato.

## Soluzione

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## Punti Chiave

- Aggiungere un LLM al tuo client offre un modo migliore per gli utenti di interagire con i Server MCP.
- Devi convertire la risposta del Server MCP in qualcosa che l'LLM possa comprendere.

## Esempi

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Risorse Aggiuntive

## Cosa c'è dopo

- Prossimo: [Consumare un server usando Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->