# Creazione di un client con LLM

Finora, hai visto come creare un server e un client. Il client è stato in grado di chiamare esplicitamente il server per elencare i suoi strumenti, risorse e prompt. Tuttavia, questo non è un approccio molto pratico. I tuoi utenti vivono nell'era agentica e si aspettano di usare prompt e comunicare con un LLM. A loro non interessa se usi MCP per memorizzare le tue capacità; si aspettano semplicemente di interagire usando il linguaggio naturale. Quindi, come risolviamo questo problema? La soluzione è aggiungere un LLM al client.

## Panoramica

In questa lezione ci concentriamo sull’aggiunta di un LLM al client e mostriamo come questo fornisce un’esperienza molto migliore per l’utente.

## Obiettivi di apprendimento

Al termine di questa lezione, sarai in grado di:

- Creare un client con un LLM.
- Interagire senza soluzione di continuità con un server MCP utilizzando un LLM.
- Fornire una migliore esperienza utente finale sul lato client.

## Approccio

Cerchiamo di capire l’approccio da adottare. Aggiungere un LLM sembra semplice, ma come lo faremo davvero?

Ecco come il client interagirà con il server:

1. Stabilire la connessione con il server.

1. Elencare capacità, prompt, risorse e strumenti e salvare il loro schema.

1. Aggiungere un LLM e passare le capacità salvate e i loro schemi in un formato che l’LLM comprende.

1. Gestire un prompt utente passandolo all’LLM insieme agli strumenti elencati dal client.

Ottimo, ora che abbiamo capito come possiamo farlo a livello alto, proviamo con l’esercizio qui sotto.

## Esercizio: Creare un client con un LLM

In questo esercizio impareremo ad aggiungere un LLM al nostro client.

### Autenticazione usando GitHub Personal Access Token

Creare un token GitHub è un processo semplice. Ecco come puoi farlo:

- Vai alle Impostazioni di GitHub – Clicca sulla tua immagine del profilo in alto a destra e seleziona Impostazioni.
- Naviga su Impostazioni sviluppatore – Scorri verso il basso e clicca su Impostazioni sviluppatore.
- Seleziona Personal Access Tokens – Clicca su Fine-grained tokens e quindi su Genera nuovo token.
- Configura il tuo token – Aggiungi una nota di riferimento, imposta una data di scadenza e seleziona gli ambiti necessari (permessi). In questo caso assicurati di aggiungere il permesso Models.
- Genera e copia il token – Clicca su Genera token e assicurati di copiarlo immediatamente, perché non potrai rivederlo.

### -1- Connettersi al server

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
- Creato una classe con due membri, `client` e `openai`, che ci aiuteranno a gestire un client e a interagire rispettivamente con un LLM.
- Configurato la nostra istanza LLM per usare i modelli GitHub impostando `baseUrl` per puntare all’API di inferenza.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Crea parametri del server per la connessione stdio
server_params = StdioServerParameters(
    command="mcp",  # Eseguibile
    args=["run", "server.py"],  # Argomenti della riga di comando opzionali
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

Per prima cosa, devi aggiungere le dipendenze LangChain4j al tuo file `pom.xml`. Aggiungi queste dipendenze per abilitare l’integrazione MCP e il supporto per i modelli GitHub:

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

Quindi crea la tua classe client Java:

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
    
    public static void main(String[] args) throws Exception {        // Configura il LLM per utilizzare i modelli GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Crea un trasporto MCP per connettersi al server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Crea un client MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Nel codice precedente abbiamo:

- **Aggiunto dipendenze LangChain4j**: necessarie per l'integrazione MCP, client ufficiale OpenAI e supporto modelli GitHub
- **Importato le librerie LangChain4j**: per integrazione MCP e funzionalità chat modello OpenAI
- **Creato un `ChatLanguageModel`**: configurato per usare modelli GitHub con il tuo token GitHub
- **Configurato il trasporto HTTP**: usando Server-Sent Events (SSE) per connettersi al server MCP
- **Creato un client MCP**: che gestirà la comunicazione col server
- **Utilizzato il supporto MCP integrato di LangChain4j**: che semplifica l’integrazione tra LLM e server MCP

#### Rust

Questo esempio presume che tu abbia un server MCP basato su Rust in esecuzione. Se non ne hai uno, consulta la lezione [01-first-server](../01-first-server/README.md) per creare il server.

Una volta che hai il server MCP Rust, apri un terminale e naviga nella stessa directory del server. Quindi esegui il seguente comando per creare un nuovo progetto client LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Aggiungi le seguenti dipendenze al file `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Non esiste una libreria ufficiale Rust per OpenAI, tuttavia la crate `async-openai` è una [libreria mantenuta dalla community](https://platform.openai.com/docs/libraries/rust#rust) comunemente utilizzata.

Apri il file `src/main.rs` e sostituisci il suo contenuto con il seguente codice:

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

    // DA FARE: Ottenere l'elenco degli strumenti MCP

    // DA FARE: Conversazione LLM con chiamate agli strumenti

    Ok(())
}
```

Questo codice configura una semplice applicazione Rust che si connetterà a un server MCP e ai modelli GitHub per interazioni LLM.

> [!IMPORTANT]
> Assicurati di impostare la variabile ambiente `OPENAI_API_KEY` con il tuo token GitHub prima di eseguire l’applicazione.

Ottimo, per il prossimo passo, elenchiamo le capacità del server.

### -2- Elencare le capacità del server

Ora ci connettiamo al server e chiediamo le sue capacità:

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

- Aggiunto il codice per connettersi al server, `connectToServer`.
- Creato un metodo `run` responsabile di gestire il flusso dell’app. Finora elenca solo gli strumenti, ma presto aggiungeremo altro.

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

- Elenco di risorse e strumenti stampati. Per gli strumenti elenchiamo anche lo `inputSchema` che useremo in seguito.

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
- Per ogni strumento, elencato nome, descrizione e schema. Quest’ultimo è qualcosa che useremo in seguito per chiamare gli strumenti.

#### Java

```java
// Crea un provider di strumenti che scopre automaticamente gli strumenti MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Il provider di strumenti MCP gestisce automaticamente:
// - Elencare gli strumenti disponibili dal server MCP
// - Convertire gli schemi degli strumenti MCP nel formato LangChain4j
// - Gestire l’esecuzione degli strumenti e le risposte
```

Nel codice precedente abbiamo:

- Creato un `McpToolProvider` che scopre e registra automaticamente tutti gli strumenti dal server MCP
- Il provider gestisce internamente la conversione tra schemi strumenti MCP e il formato strumenti di LangChain4j
- Questo approccio astrarre il processo manuale di elenco e conversione degli strumenti

#### Rust

Il recupero degli strumenti dal server MCP avviene usando il metodo `list_tools`. Nella tua funzione `main`, dopo aver configurato il client MCP, aggiungi il seguente codice:

```rust
// Ottieni l'elenco degli strumenti MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Convertire le capacità del server in strumenti LLM

Il passo successivo dopo aver elencato le capacità del server è convertirle in un formato che l’LLM comprende. Una volta fatto, possiamo fornire queste capacità come strumenti al nostro LLM.

#### TypeScript

1. Aggiungi il seguente codice per convertire la risposta del server MCP in un formato di strumento utilizzabile dall’LLM:

    ```typescript
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

    ```

    Il codice sopra prende una risposta dal server MCP e la converte in un formato di definizione di strumento che l’LLM può capire.

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

    Nel codice precedente, abbiamo aggiornato il metodo `run` per mappare i risultati e chiamare `openAiToolAdapter` per ogni elemento.

#### Python

1. Per prima cosa, creiamo la seguente funzione di conversione

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

    Nella funzione sopra `convert_to_llm_tools` prendiamo una risposta strumento MCP e la convertiamo in un formato comprensibile all’LLM.

1. Poi aggiorniamo il codice client per utilizzare questa funzione così:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Qui stiamo aggiungendo una chiamata a `convert_to_llm_tool` per convertire la risposta strumento MCP in qualcosa che possiamo fornire all’LLM più avanti.

#### .NET

1. Aggiungiamo codice per convertire la risposta strumento MCP in qualcosa che l’LLM può comprendere

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

- Creato una funzione `ConvertFrom` che prende nome, descrizione e schema d’ingresso.
- Definito funzionalità che crea una FunctionDefinition che viene passata a ChatCompletionsDefinition. Quest’ultimo è qualcosa che l’LLM può comprendere.

1. Vediamo come aggiornare del codice esistente per usufruire di questa funzione sopra:

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
- Usato LangChain4j `AiServices` per collegare automaticamente l’LLM con il provider strumenti MCP
- Il framework gestisce automaticamente la conversione degli schemi strumenti e le chiamate di funzione dietro le quinte
- Questo approccio elimina la conversione manuale degli strumenti — LangChain4j gestisce tutta la complessità di conversione degli strumenti MCP in formato compatibile con LLM

#### Rust

Per convertire la risposta strumento MCP in un formato che l’LLM può comprendere, aggiungeremo una funzione helper che formatta l’elenco degli strumenti. Aggiungi il seguente codice al file `main.rs` sotto la funzione `main`. Questa verrà chiamata quando si effettuano richieste all’LLM:

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

Ottimo, siamo pronti a gestire eventuali richieste utente, quindi affrontiamo quel punto ora.

### -4- Gestire una richiesta prompt utente

In questa parte del codice, gestiremo le richieste degli utenti.

#### TypeScript

1. Aggiungi un metodo che chiamerà il nostro LLM:

    ```typescript
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
    ```

    Nel codice precedente abbiamo:

    - Aggiunto un metodo `callTools`.
    - Il metodo prende la risposta LLM e verifica quali strumenti sono stati chiamati, se ce ne sono:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // chiamare strumento
        }
        ```

    - Chiama uno strumento, se l’LLM indica che deve essere chiamato:

        ```typescript
        // 2. Chiama lo strumento del server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fai qualcosa con il risultato
        // DA FARE
        ```

1. Aggiorna il metodo `run` per includere chiamate all’LLM e a `callTools`:

    ```typescript

    // 1. Creare messaggi che sono input per l'LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Chiamare l'LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Esaminare la risposta dell'LLM, per ogni scelta, verificare se contiene chiamate a strumenti
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Ottimo, elenchiamo il codice completo:

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
            baseURL: "https://models.inference.ai.azure.com", // potrebbe essere necessario cambiare in questo url in futuro: https://models.github.ai/inference
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
    
        // 1. Analizza la risposta LLM, per ogni scelta, verifica se ha chiamate a strumenti
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

1. Aggiungiamo alcuni import necessari per chiamare un LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Ora aggiungiamo la funzione che chiamerà l’LLM:

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

    - Passato le nostre funzioni, trovate sul server MCP e convertite, all’LLM.
    - Poi abbiamo chiamato l’LLM con queste funzioni.
    - Successivamente, ispezioniamo il risultato per vedere quali funzioni chiamare, se ce ne sono.
    - Infine passiamo un array di funzioni da chiamare.

1. Passo finale, aggiorniamo il nostro codice principale:

    ```python
    prompt = "Add 2 to 20"

    # chiedi al LLM quali strumenti usare, se ce ne sono
    functions_to_call = call_llm(prompt, functions)

    # chiama le funzioni suggerite
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ecco, questo è stato l’ultimo passo: nel codice sopra stiamo:

    - Chiamando uno strumento MCP tramite `call_tool` usando una funzione che l’LLM ha ritenuto di dover chiamare sulla base del nostro prompt.
    - Stampando il risultato della chiamata strumento al server MCP.

#### .NET

1. Ecco un codice che mostra come fare una richiesta prompt LLM:

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

    - Prelevato strumenti dal server MCP, `var tools = await GetMcpTools()`.
    - Definito un prompt utente `userMessage`.
    - Costruito un oggetto opzioni specificando modello e strumenti.
    - Fatto una richiesta verso l’LLM.

1. Un ultimo passo, vediamo se l’LLM pensa che dobbiamo chiamare una funzione:

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

    - Iterato su una lista di chiamate funzione.
    - Per ogni chiamata strumento, estratto nome e argomenti e chiamato lo strumento sul server MCP usando il client MCP. Infine stampiamo i risultati.

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
    // Esegui richieste in linguaggio naturale che utilizzano automaticamente gli strumenti MCP
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

- Usato semplici prompt in linguaggio naturale per interagire con gli strumenti del server MCP
- Il framework LangChain4j gestisce automaticamente:
  - La conversione di prompt utente in chiamate a strumenti quando necessario
  - La chiamata agli strumenti MCP appropriati basata sulla decisione dell’LLM
  - La gestione del flusso della conversazione tra LLM e server MCP
- Il metodo `bot.chat()` ritorna risposte in linguaggio naturale che possono includere risultati da esecuzioni di strumenti MCP
- Questo approccio fornisce un’esperienza utente senza interruzioni dove gli utenti non devono sapere dell’implementazione MCP sottostante

Esempio di codice completo:

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

Qui avviene la maggior parte del lavoro. Chiameremo l’LLM con il prompt iniziale dell’utente, quindi processeremo la risposta per vedere se è necessario chiamare strumenti. In tal caso, chiameremo quegli strumenti e continueremo la conversazione con l’LLM finché non saranno necessarie più chiamate a strumenti e avremo una risposta finale.

Effettueremo più chiamate all’LLM, quindi definiamo una funzione che gestirà la chiamata all’LLM. Aggiungi la seguente funzione al tuo file `main.rs`:

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

Questa funzione prende il client LLM, una lista di messaggi (compreso il prompt utente), gli strumenti dal server MCP e invia una richiesta all’LLM, restituendo la risposta.
La risposta dal LLM conterrà un array di `choices`. Dovremo elaborare il risultato per vedere se sono presenti `tool_calls`. Questo ci fa capire che il LLM sta richiedendo che uno specifico strumento venga chiamato con degli argomenti. Aggiungi il seguente codice in fondo al tuo file `main.rs` per definire una funzione che gestisca la risposta del LLM:

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

        // Esegui ogni chiamata dello strumento
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

        // Continua la conversazione con i risultati dello strumento
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

Se sono presenti `tool_calls`, estrae le informazioni sullo strumento, chiama il server MCP con la richiesta dello strumento, e aggiunge i risultati ai messaggi della conversazione. Procede quindi con la conversazione con il LLM e i messaggi vengono aggiornati con la risposta dell’assistente e i risultati della chiamata allo strumento.

Per estrarre le informazioni della chiamata allo strumento che il LLM restituisce per le chiamate MCP, aggiungeremo un’altra funzione helper per estrarre tutto il necessario per effettuare la chiamata. Aggiungi il seguente codice in fondo al tuo file `main.rs`:

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

Con tutti i pezzi al loro posto, ora possiamo gestire il prompt iniziale dell’utente e chiamare il LLM. Aggiorna la tua funzione `main` includendo il seguente codice:

```rust
// Conversazione LLM con chiamate a strumenti
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

Questo interroguerà il LLM con il prompt iniziale dell’utente che chiede la somma di due numeri, ed elaborerà la risposta per gestire dinamicamente le chiamate agli strumenti.

Ottimo, ce l’hai fatta!

## Compito

Prendi il codice dell’esercizio e costruisci il server con altri strumenti. Poi crea un client con un LLM, come nell’esercizio, e testalo con diversi prompt per assicurarti che tutti gli strumenti del server vengano chiamati dinamicamente. Questo modo di costruire un client significa che l’utente finale avrà un’ottima esperienza perché può usare prompt, invece di comandi client esatti, e non si accorgerà di alcuna chiamata a un server MCP.

## Soluzione

[Soluzione](./solution/README.md)

## Punti Chiave

- Aggiungere un LLM al tuo client fornisce un modo migliore per gli utenti di interagire con i server MCP.
- Devi convertire la risposta del server MCP in qualcosa che il LLM possa capire.

## Esempi

- [Calcolatrice Java](../samples/java/calculator/README.md)
- [Calcolatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calcolatrice JavaScript](../samples/javascript/README.md)
- [Calcolatrice TypeScript](../samples/typescript/README.md)
- [Calcolatrice Python](../../../../03-GettingStarted/samples/python)
- [Calcolatrice Rust](../../../../03-GettingStarted/samples/rust)

## Risorse Aggiuntive

## Cosa c’è dopo

- Successivo: [Consumare un server usando Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l'accuratezza, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->