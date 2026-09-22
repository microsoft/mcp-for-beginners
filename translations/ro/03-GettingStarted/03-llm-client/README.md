# Crearea unui client cu LLM

> [!NOTE]
> Exemplele de client Java se conectează prin transportul legacy HTTP+SSE și
> vizează API-urile SDK MCP `2025-11-25`. Folosește un SDK compatibil `2026-07-28` și
> Streamable HTTP pentru noii clienți remote.

Până acum, ai văzut cum să creezi un server și un client. Clientul a putut apela serverul în mod explicit pentru a lista uneltele, resursele și prompturile sale. Totuși, aceasta nu este o abordare foarte practică. Utilizatorii tăi trăiesc în era agentică și se așteaptă să utilizeze prompturi și să comunice cu un LLM în schimb. Nu le pasă dacă folosești MCP pentru a stoca capabilitățile tale; ei se așteaptă pur și simplu să interacționeze folosind limbaj natural. Deci, cum rezolvăm asta? Soluția este să adăugăm un LLM la client.

## Prezentare generală

În această lecție ne concentrăm pe adăugarea unui LLM pentru clientul tău și arătăm cum acest lucru oferă o experiență mult mai bună pentru utilizatorul tău.

## Obiective de învățare

La finalul acestei lecții, vei fi capabil să:

- Creezi un client cu un LLM.
- Interacționezi fără întreruperi cu un server MCP folosind un LLM.
- Oferi o experiență mai bună utilizatorului final pe partea clientului.

## Abordare

Să încercăm să înțelegem abordarea pe care trebuie să o luăm. Adăugarea unui LLM pare simplă, dar chiar o vom face?

Iată cum clientul va interacționa cu serverul:

1. Stabilește conexiunea cu serverul.

1. Listează capabilitățile, prompturile, resursele și uneltele, și salvează schema lor.

1. Adaugă un LLM și transmite capabilitățile și schema salvată într-un format înțeles de LLM.

1. Gestionează un prompt al utilizatorului, trecându-l la LLM împreună cu uneltele listate de client.

Grozav, acum că am înțeles cum putem face asta la nivel înalt, să încercăm în exercițiul de mai jos.

## Exercițiu: Crearea unui client cu un LLM

În acest exercițiu, vom învăța să adăugăm un LLM clientului nostru.

### Autentificare folosind token personal GitHub

Crearea unui token GitHub este un proces simplu. Iată cum poți face asta:

- Mergi la GitHub Settings – Dă click pe poza ta de profil din colțul din dreapta sus și selectează Settings.
- Navighează la Developer Settings – Derulează în jos și dă click pe Developer Settings.
- Selectează Personal Access Tokens – Dă click pe Fine-grained tokens și apoi Generate new token.
- Configurează token-ul – Adaugă o notă pentru referință, setează o dată de expirare și selectează permisiunile necesare (scopes). În acest caz, asigură-te că adaugi permisiunea Models.
- Generează și copiază token-ul – Dă click pe Generate token și asigură-te că îl copiezi imediat, deoarece nu vei mai putea să îl vezi din nou.

### -1- Conectarea la server

Hai să creăm mai întâi clientul nostru:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importă zod pentru validarea schemelor

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

În codul precedent am:

- Importat librăriile necesare
- Creat o clasă cu doi membri, `client` și `openai`, care ne vor ajuta să gestionăm un client și să interacționăm cu un LLM, respectiv.
- Configurat instanța noastră de LLM să folosească modelele GitHub setând `baseUrl` să indice către API-ul de inferență.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Creează parametrii serverului pentru conexiunea stdio
server_params = StdioServerParameters(
    command="mcp",  # Executabil
    args=["run", "server.py"],  # Argumente opționale din linia de comandă
    env=None,  # Variabile de mediu opționale
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inițializează conexiunea
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

În codul precedent am:

- Importat librăriile necesare pentru MCP
- Creat un client

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

Mai întâi, va trebui să adaugi dependențele LangChain4j în fișierul tău `pom.xml`. Adaugă aceste dependențe pentru a activa integrarea MCP și API-ul MiniMax compatibil OpenAI:

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

Setează cheia ta API MiniMax și, opțional, endpoint-ul și modelul.
`MINIMAX_MODEL_ID` suportă `MiniMax-M3` și `MiniMax-M2.7`. Dacă
`OPENAI_BASE_URL` nu este setat, `MINIMAX_REGION` suportă `global_en` și `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Pentru a selecta endpoint-ul după regiune în schimb, omit `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Apoi creează clasa ta Java client:

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

        // Creează transport MCP pentru conectarea la server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Creează client MCP
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

În codul precedent am:

- **Adăugat dependențele LangChain4j**: Necesare pentru integrarea MCP și API-ul MiniMax compatibil OpenAI
- **Importat librăriile LangChain4j**: Pentru integrarea MCP și funcționalitatea modelului chat OpenAI
- **Creat un `ChatLanguageModel`**: Configurat să folosească MiniMax cu cheia ta API MiniMax, endpoint-ul și ID-ul modelului suportat
- **Setat transportul HTTP**: Folosind Server-Sent Events (SSE) pentru conectarea la serverul MCP
- **Creat un client MCP**: Care va gestiona comunicarea cu serverul
- **Folosit suportul încorporat LangChain4j pentru MCP**: Care simplifică integrarea între LLM și serverele MCP

#### Rust

Acest exemplu presupune că ai un server MCP bazat pe Rust în funcțiune. Dacă nu ai unul, consultă lecția [01-first-server](../01-first-server/README.md) pentru a crea serverul.

După ce ai serverul Rust MCP, deschide un terminal și navighează în același director cu serverul. Apoi rulează următoarea comandă pentru a crea un nou proiect client LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Adaugă următoarele dependențe în fișierul tău `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Nu există o bibliotecă Rust oficială pentru OpenAI, însă crate-ul `async-openai` este o [bibliotecă întreținută de comunitate](https://platform.openai.com/docs/libraries/rust#rust) care este folosită frecvent.

Deschide fișierul `src/main.rs` și înlocuiește-i conținutul cu următorul cod:

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
    // Mesaj inițial
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Configurare client OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Configurare client MCP
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

    // TODO: Obțineți lista de unelte MCP

    // TODO: Conversație LLM cu apeluri la unelte

    Ok(())
}
```

Acest cod configurează o aplicație Rust de bază care se va conecta la un server MCP și modelele GitHub pentru interacțiuni LLM.

> [!IMPORTANT]
> Asigură-te că setezi variabila de mediu `OPENAI_API_KEY` cu token-ul tău GitHub înainte de a rula aplicația.

Grozav, pentru următorul pas, să listăm capabilitățile serverului.

### -2- Listează capabilitățile serverului

Acum ne vom conecta la server și vom cere capabilitățile sale:

#### Typescript

În aceeași clasă, adaugă următoarele metode:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // listarea uneltelor
    const toolsResult = await this.client.listTools();
}
```

În codul precedent am:

- Adăugat cod pentru conectarea la server, `connectToServer`.
- Creat o metodă `run` responsabilă pentru gestionarea fluxului aplicației noastre. Până acum listează doar uneltele, dar vom mai adăuga curând.

#### Python

```python
# Listează resursele disponibile
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Listează uneltele disponibile
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Iată ce am adăugat:

- Listarea resurselor și uneltelor și afișarea lor. Pentru unelte am listat și `inputSchema` pe care îl vom folosi mai târziu.

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

În codul precedent am:

- Listat uneltele disponibile pe serverul MCP
- Pentru fiecare unealtă, listat numele, descrierea și schema ei. Ultima este ceva ce vom folosi pentru a apela uneltele în curând.

#### Java

```java
// Creează un furnizor de unelte care descoperă automat uneltele MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Furnizorul de unelte MCP gestionează automat:
// - Listarea uneltelor disponibile de pe serverul MCP
// - Convertirea schemelor uneltelor MCP în format LangChain4j
// - Gestionarea executării uneltelor și a răspunsurilor
```

În codul precedent am:

- Creat un `McpToolProvider` care descoperă și înregistrează automat toate uneltele de pe serverul MCP
- Furnizorul de unelte gestionează conversia între schemele uneltelor MCP și formatul LangChain4j intern
- Această abordare abstractizează procesul manual de listare și conversie al uneltelor

#### Rust

Obținerea uneltelor de pe serverul MCP se face prin metoda `list_tools`. În funcția ta `main`, după configurarea clientului MCP, adaugă următorul cod:

```rust
// Obține lista de unelte MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Convertirea capabilităților serverului în unelte LLM

Pasul următor după listarea capabilităților serverului este să le convertim într-un format înțeles de LLM. Odată ce facem asta, putem oferi aceste capabilități ca unelte LLM.

#### TypeScript

1. Adaugă următorul cod pentru a converti răspunsul de la serverul MCP într-un format de unealtă pe care LLM îl poate folosi:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Creează un schema zod bazat pe input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Setează explicit tipul la "funcție"
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

    Codul de mai sus ia un răspuns de la serverul MCP și îl convertește într-un format de definiție a unei unelte pe care LLM o poate înțelege.

2. Să actualizăm acum metoda `run` pentru a lista capabilitățile serverului:

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

    În codul precedent, am actualizat metoda `run` să parcurgă rezultatul și pentru fiecare intrare să apeleze `openAiToolAdapter`.

#### Python

1. Mai întâi, să creăm funcția convertor de mai jos

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

    În funcția de mai sus `convert_to_llm_tools` luăm un răspuns de unealtă MCP și îl convertim într-un format pe care LLM îl poate înțelege.

2. Apoi, să actualizăm codul clientului pentru a folosi această funcție așa:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Aici, adăugăm un apel către `convert_to_llm_tool` pentru a converti răspunsul uneltei MCP într-un format pe care îl putem transmite LLM-ului ulterior.

#### .NET

1. Să adăugăm cod pentru a converti răspunsul uneltei MCP într-un format înțeles de LLM:

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

În codul precedent am:

- Creat o funcție `ConvertFrom` care ia numele, descrierea și schema de input.
- Definit o funcționalitate care creează o FunctionDefinition ce este transmisă unui ChatCompletionsDefinition. Aceasta din urmă este ceva ce LLM-ul poate înțelege.

2. Să vedem cum putem actualiza codul existent pentru a folosi această funcție:

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
// Creează o interfață Bot pentru interacțiune în limbaj natural
public interface Bot {
    String chat(String prompt);
}

// Configurează serviciul AI cu instrumentele LLM și MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

În codul precedent am:

- Definit o interfață simplă `Bot` pentru interacțiuni în limbaj natural
- Folosit `AiServices` din LangChain4j pentru a lega automat LLM-ul cu furnizorul de unelte MCP
- Framework-ul gestionează automat conversia schemelor uneltelor și apelarea funcțiilor în fundal
- Această abordare elimină conversia manuală a uneltelor - LangChain4j se ocupă de toată complexitatea convertirii uneltelor MCP în format compatibil LLM

#### Rust

Pentru a converti răspunsul uneltei MCP într-un format pe care LLM îl poate înțelege, vom adăuga o funcție auxiliară care formatează lista uneltelor. Adaugă următorul cod în fișierul tău `main.rs` sub funcția `main`. Acesta va fi apelat când faci cereri către LLM:

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

Grozav, suntem pregătiți să gestionăm orice cerere a utilizatorului, așa că să trecem la asta.

### -4- Gestionarea cererilor de prompt ale utilizatorului

În această parte a codului vom gestiona cererile utilizatorilor.

#### TypeScript

1. Adaugă o metodă care va fi folosită pentru a apela LLM-ul nostru:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Apelează instrumentul serverului
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fă ceva cu rezultatul
        // DE FACUT

        }
    }
    ```

    În codul precedent am:

    - Adăugat o metodă `callTools`.
    - Metoda primește un răspuns LLM și verifică ce unelte au fost apelate, dacă există:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // apelare unealtă
        }
        ```

    - Apelează o unealtă, dacă LLM indică că ar trebui apelată:

        ```typescript
        // 2. Apelează instrumentul serverului
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fă ceva cu rezultatul
        // DE FACUT
        ```

2. Actualizează metoda `run` să includă apeluri la LLM și apelarea lui `callTools`:

    ```typescript

    // 1. Creează mesaje care sunt input pentru LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Apelarea LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Parcurge răspunsul LLM, pentru fiecare opțiune, verifică dacă are apeluri de unelte
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Grozav, iată codul complet:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importă zod pentru validarea schemei

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // poate va trebui să schimbăm la acest URL în viitor: https://models.github.ai/inference
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
          // Creează o schemă zod bazată pe input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Setează explicit tipul la "function"
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
    
    
          // 2. Apelează instrumentul serverului
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Fă ceva cu rezultatul
          // DE FACUT
    
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
    
        // 3. Parcurge răspunsul LLM, pentru fiecare opțiune, verifică dacă are apeluri către instrumente
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

1. Să adăugăm importurile necesare pentru a apela un LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Apoi, să adăugăm funcția care va apela LLM-ul:

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
            # Parametri opționali
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

    În codul precedent am:

    - Transmis funcțiile noastre, pe care le-am găsit pe serverul MCP și le-am convertit, către LLM.
    - Apoi am apelat LLM-ul cu aceste funcții.
    - După aceea inspectăm rezultatul să vedem ce funcții trebuie apelate, dacă există.
    - În final, transmitem un array de funcții de apelat.

3. Pasul final, să actualizăm codul nostru principal:

    ```python
    prompt = "Add 2 to 20"

    # întreabă LLM ce instrumente să folosească, dacă este cazul
    functions_to_call = call_llm(prompt, functions)

    # apelează funcțiile sugerate
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Asta a fost pasul final, în codul de mai sus:

    - Apelăm o unealtă MCP prin `call_tool` folosind o funcție pe care LLM-ul a considerat că ar trebui să o apelăm pe baza promptului nostru.
    - Afișăm rezultatul apelului uneltei la serverul MCP.

#### .NET

1. Să arătăm cod pentru a face o cerere prompt LLM:

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

    În codul precedent am:

    - Preluat uneltele de pe serverul MCP, `var tools = await GetMcpTools()`.
    - Definit un prompt utilizator `userMessage`.
    - Constructor un obiect options specificând modelul și uneltele.
    - Făcut o cerere către LLM.

2. Un ultim pas, să vedem dacă LLM consideră că ar trebui să apelăm o funcție:

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

    În codul precedent am:

    - Iterat printr-o listă de apeluri funcții.
    - Pentru fiecare apel unealtă, extragem numele și argumentele și apelăm unealta pe serverul MCP folosind clientul MCP. În final, afișăm rezultatele.

Iată codul complet:

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
    // Execută cereri în limbaj natural care utilizează automat uneltele MCP
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

În codul precedent am:

- Folosit prompturi simple în limbaj natural pentru a interacționa cu uneltele serverului MCP
- Framework-ul LangChain4j gestionează automat:
  - Conversia prompturilor utilizatorului în apeluri unelte când e necesar
  - Apelarea uneltelor MCP adecvate pe baza deciziei LLM
  - Gestionarea fluxului conversațional între LLM și serverul MCP
- Metoda `bot.chat()` returnează răspunsuri în limbaj natural care pot include rezultate din execuția uneltelor MCP
- Această abordare oferă o experiență fluidă utilizatorului, care nu trebuie să cunoască implementarea MCP din spate

Exemplu complet de cod:

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


Aici se întâmplă majoritatea muncii. Vom apela LLM cu promptul inițial al utilizatorului, apoi vom procesa răspunsul pentru a vedea dacă este necesar să apelăm vreun instrument. Dacă da, vom apela acele instrumente și vom continua conversația cu LLM până când nu mai sunt necesare apeluri de instrumente și avem un răspuns final.

Vom face mai multe apeluri către LLM, așa că să definim o funcție care să gestioneze apelul către LLM. Adaugă următoarea funcție în fișierul tău `main.rs`:

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

Această funcție primește clientul LLM, o listă de mesaje (inclusiv promptul utilizatorului), instrumentele de pe serverul MCP și trimite o cerere către LLM, returnând răspunsul.

Răspunsul de la LLM va conține un tablou de `choices`. Va trebui să procesăm rezultatul pentru a vedea dacă sunt prezente `tool_calls`. Acest lucru ne spune că LLM solicită să fie apelat un anumit instrument cu argumente. Adaugă următorul cod la finalul fișierului tău `main.rs` pentru a defini o funcție care să gestioneze răspunsul LLM:

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

    // Afișează conținutul dacă este disponibil
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Gestionează apelurile către instrumente
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Adaugă mesajul asistentului

        // Execută fiecare apel către instrument
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Adaugă rezultatul instrumentului în mesaje
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Continuă conversația cu rezultatele instrumentelor
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

Dacă există `tool_calls`, extrage informațiile despre instrument, apelează serverul MCP cu cererea pentru instrument și adaugă rezultatele în mesajele conversației. Apoi continuă conversația cu LLM, iar mesajele sunt actualizate cu răspunsul asistentului și rezultatele apelului instrumentului.

Pentru a extrage informațiile apelului instrumentului pe care LLM le returnează pentru apelurile MCP, vom adăuga o altă funcție ajutătoare pentru a extrage tot ce este necesar pentru a face apelul. Adaugă următorul cod la finalul fișierului tău `main.rs`:

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

Cu toate componentele la locul lor, acum putem gestiona promptul inițial al utilizatorului și apela LLM. Actualizează funcția ta `main` pentru a include următorul cod:

```rust
// Conversație LLM cu apeluri către unelte
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

Acest cod va interoga LLM cu promptul inițial al utilizatorului cerând suma a două numere și va procesa răspunsul pentru a gestiona dinamic apelurile instrumentelor.

Minunat, ai reușit!

## Tema

Ia codul din exercițiu și dezvoltă serverul cu mai multe instrumente. Apoi creează un client cu un LLM, ca în exercițiu, și testează-l cu prompturi diferite pentru a te asigura că toate instrumentele serverului tău sunt apelate dinamic. Acest mod de a construi un client înseamnă că utilizatorul final va avea o experiență excelentă deoarece poate folosi prompturi, în loc de comenzi exacte ale clientului, și nu va observa apelarea vreunui server MCP.

## Soluție

[Soluție](./solution/README.md)

## Aspecte importante de reținut

- Adăugarea unui LLM în clientul tău oferă o modalitate mai bună pentru utilizatori de a interacționa cu serverele MCP.
- Trebuie să convertești răspunsul serverului MCP într-un format pe care LLM îl poate înțelege.

## Exemple

- [Calculator Java](../samples/java/calculator/README.md)
- [Calculator .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculator JavaScript](../samples/javascript/README.md)
- [Calculator TypeScript](../samples/typescript/README.md)
- [Calculator Python](../../../../03-GettingStarted/samples/python)
- [Calculator Rust](../../../../03-GettingStarted/samples/rust)

## Resurse suplimentare

## Ce urmează

- Următorul pas: [Consumul unui server folosind Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->