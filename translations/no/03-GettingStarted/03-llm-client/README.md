# Opprette en klient med LLM

> [!NOTE]
> Java-klienteksemplene kobler til gjennom den eldre HTTP+SSE-transporten og
> bruker MCP `2025-11-25` SDK APIer. Bruk en `2026-07-28`-kompatibel SDK og
> Streamable HTTP for nye fjernklienter.

Så langt har du sett hvordan du oppretter en server og en klient. Klienten har kunnet kalle serveren eksplisitt for å liste opp dens verktøy, ressurser og prompts. Dette er imidlertid ikke en veldig praktisk tilnærming. Brukerne dine lever i den agentiske æraen og forventer å bruke prompts og kommunisere med en LLM i stedet. De bryr seg ikke om du bruker MCP for å lagre dine kapasiteter; de forventer rett og slett å samhandle med naturlig språk. Så hvordan løser vi dette? Løsningen er å legge til en LLM i klienten.

## Oversikt

I denne leksjonen fokuserer vi på å legge til en LLM i klienten din og viser hvordan dette gir en mye bedre opplevelse for brukeren din.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Opprette en klient med en LLM.
- Sømløst samhandle med en MCP-server ved hjelp av en LLM.
- Gi en bedre sluttbrukeropplevelse på klientsiden.

## Tilnærming

La oss prøve å forstå tilnærmingen vi må ta. Å legge til en LLM høres enkelt ut, men skal vi faktisk gjøre det?

Slik vil klienten samhandle med serveren:

1. Etablere forbindelse med serveren.

1. Liste opp kapasiteter, prompts, ressurser og verktøy, og lagre skjemaene deres.

1. Legge til en LLM og sende de lagrede kapasiteter og deres skjema i et format som LLM forstår.

1. Håndtere en brukerprompt ved å sende den til LLM sammen med verktøyene listet opp av klienten.

Flott, nå som vi forstår hvordan vi kan gjøre dette på et overordnet nivå, la oss prøve det ut i øvelsen nedenfor.

## Øvelse: Opprette en klient med en LLM

I denne øvelsen skal vi lære å legge til en LLM i vår klient.

### Autentisering med GitHub Personal Access Token

Å opprette et GitHub-token er en enkel prosess. Slik gjør du det:

- Gå til GitHub-innstillinger – Klikk på profilbildet ditt øverst til høyre og velg Innstillinger.
- Naviger til Utviklerinnstillinger – Bla ned og klikk på Utviklerinnstillinger.
- Velg Personlige tilgangstokener – Klikk på Finmasket tokens og deretter Generer nytt token.
- Konfigurer tokenet ditt – Legg til en merknad for referanse, sett en utløpsdato, og velg nødvendige tillatelser (scopes). I dette tilfellet må du sørge for å legge til Modeller-tillatelsen.
- Generer og kopier tokenet – Klikk Generer token, og sørg for å kopiere det med en gang, da du ikke vil kunne se det igjen.

### -1- Koble til server

La oss opprette klienten vår først:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importer zod for skjema validering

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

I koden ovenfor har vi:

- Importert nødvendige biblioteker
- Opprettet en klasse med to medlemmer, `client` og `openai`, som vil hjelpe oss med å håndtere en klient og samhandle med en LLM henholdsvis.
- Konfigurert LLM-forekomsten vår til å bruke GitHub Models ved å sette `baseUrl` til å peke til inference-API-et.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Opprett serverparametere for stdio-tilkobling
server_params = StdioServerParameters(
    command="mcp",  # Kjørbar fil
    args=["run", "server.py"],  # Valgfrie kommandolinjeargumenter
    env=None,  # Valgfrie miljøvariabler
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialiser tilkoblingen
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

I koden ovenfor har vi:

- Importert nødvendige biblioteker for MCP
- Opprettet en klient

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

Først må du legge til LangChain4j-avhengighetene i `pom.xml`-filen din. Legg til disse avhengighetene for å aktivere MCP-integrasjon og OpenAI-kompatibel MiniMax API:

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

Sett din MiniMax API-nøkkel og eventuelt endepunkt og modell.
`MINIMAX_MODEL_ID` støtter `MiniMax-M3` og `MiniMax-M2.7`. Hvis
`OPENAI_BASE_URL` ikke er satt, støtter `MINIMAX_REGION` `global_en` og `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

For å velge endepunkt basert på region i stedet, utelat `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Deretter oppretter du din Java-klientklasse:

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

        // Opprett MCP-transport for tilkobling til server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Opprett MCP-klient
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

I koden ovenfor har vi:

- **Lagt til LangChain4j-avhengigheter**: Nødvendig for MCP-integrasjon og OpenAI-kompatibel MiniMax API
- **Importert LangChain4j-biblioteker**: For MCP-integrasjon og OpenAI chat-modellfunksjonalitet
- **Opprettet en `ChatLanguageModel`**: Konfigurert til å bruke MiniMax med din MiniMax API-nøkkel, endepunkt, og støttet modell-ID
- **Satt opp HTTP-transport**: Bruker Server-Sent Events (SSE) for å koble til MCP-serveren
- **Opprettet en MCP-klient**: Som vil håndtere kommunikasjonen med serveren
- **Brukt LangChain4j sin innebygde MCP-støtte**: Som forenkler integrasjonen mellom LLM-er og MCP-servere

#### Rust

Dette eksemplet forutsetter at du har en Rust-basert MCP-server kjørende. Hvis du ikke har en, se tilbake til [01-first-server](../01-first-server/README.md) leksjonen for å opprette serveren.

Når du har din Rust MCP-server, åpne et terminalvindu og naviger til samme mappe som serveren. Kjør deretter følgende kommando for å opprette et nytt LLM-klientprosjekt:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Legg til følgende avhengigheter i `Cargo.toml`-filen din:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Det finnes ikke et offisielt Rust-bibliotek for OpenAI, men `async-openai`-pakken er et [samfunnsvedlikeholdt bibliotek](https://platform.openai.com/docs/libraries/rust#rust) som ofte brukes.

Åpne `src/main.rs`-filen og erstatt innholdet med følgende kode:

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
    // Startmelding
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Sett opp OpenAI-klient
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Sett opp MCP-klient
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

    // TODO: Få MCP verktøyliste

    // TODO: LLM-samtale med verktøyanrop

    Ok(())
}
```

Denne koden setter opp en enkel Rust-applikasjon som kobler til en MCP-server og GitHub Models for LLM-interaksjoner.

> [!IMPORTANT]
> Sørg for å sette `OPENAI_API_KEY` miljøvariabelen med GitHub-tokenet ditt før du kjører applikasjonen.

Flott, for vårt neste steg, la oss liste opp kapasiteter på serveren.

### -2- Liste opp serverkapasiteter

Nå kobler vi til serveren og spør om dens kapasiteter:

#### Typescript

I samme klasse legger du til følgende metoder:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // verktøyliste
    const toolsResult = await this.client.listTools();
}
```

I koden ovenfor har vi:

- Lagt til kode for å koble til serveren, `connectToServer`.
- Opprettet en `run`-metode som er ansvarlig for å håndtere appens flyt. Så langt lister den bare verktøyene, men vi vil snart legge til mer.

#### Python

```python
# List opp tilgjengelige ressurser
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List opp tilgjengelige verktøy
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Dette la vi til:

- Liste opp ressurser og verktøy og skrevet dem ut. For verktøy lister vi også `inputSchema` som vi bruker senere.

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


I koden ovenfor har vi:

- Listet opp verktøyene tilgjengelig på MCP-serveren
- For hvert verktøy, listet opp navn, beskrivelse og skjemaet deres. Det sistnevnte er noe vi snart vil bruke for å kalle verktøyene.

#### Java

```java
// Opprett en verktøyleverandør som automatisk oppdager MCP-verktøy
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP-verktøyleverandøren håndterer automatisk:
// - Liste opp tilgjengelige verktøy fra MCP-serveren
// - Konvertere MCP-verktøy-skjemaer til LangChain4j-format
// - Håndtere verktøykjøring og svar
```

I koden ovenfor har vi:

- Opprettet en `McpToolProvider` som automatisk oppdager og registrerer alle verktøy fra MCP-serveren
- Verktøytilbyderen håndterer konverteringen mellom MCP-verktøy-skjemaer og LangChain4j sitt verktøyformat internt
- Denne tilnærmingen abstrakterer bort den manuelle verktøyliste- og konverteringsprosessen

#### Rust

Henting av verktøy fra MCP-serveren gjøres ved å bruke `list_tools`-metoden. I din `main`-funksjon, etter å ha satt opp MCP-klienten, legg til følgende kode:

```rust
// Hent MCP verktøyliste
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Konverter serverfunksjoner til LLM-verktøy

Neste steg etter å ha listet serverfunksjonene er å konvertere dem til et format som LLM forstår. Når vi gjør det, kan vi tilby disse funksjonene som verktøy til vår LLM.

#### TypeScript

1. Legg til følgende kode for å konvertere svar fra MCP-serveren til et verktøyformat som LLM kan bruke:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Lag et zod-skjema basert på input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Sett type eksplisitt til "funksjon"
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

    Koden over tar et svar fra MCP-serveren og konverterer det til et verktøydefinisjonsformat som LLM kan forstå.

2. La oss oppdatere `run`-metoden neste for å liste serverfunksjoner:

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

    I koden ovenfor har vi oppdatert `run`-metoden til å mappe gjennom resultatet og for hvert element kalle `openAiToolAdapter`.

#### Python

1. Først, la oss lage følgende konverteringsfunksjon

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

    I funksjonen ovenfor `convert_to_llm_tools` tar vi et MCP-verktøysvar og konverterer det til et format som LLM kan forstå.

2. Neste, la oss oppdatere klientkoden vår for å bruke denne funksjonen slik:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Her legger vi til et kall til `convert_to_llm_tool` for å konvertere MCP-verktøysvaret til noe vi senere kan sende til LLM.

#### .NET

1. La oss legge til kode for å konvertere MCP-verktøysvaret til noe LLM kan forstå

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

I koden ovenfor har vi:

- Opprettet en funksjon `ConvertFrom` som tar navn, beskrivelse og inndatakskjema.
- Definert funksjonalitet som oppretter en FunctionDefinition som sendes til en ChatCompletionsDefinition. Sistnevnte er noe LLM kan forstå.

2. La oss se hvordan vi kan oppdatere noe eksisterende kode for å dra nytte av funksjonen over:

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
// Lag et bot-grensesnitt for naturlig språkinteraksjon
public interface Bot {
    String chat(String prompt);
}

// Konfigurer AI-tjenesten med LLM- og MCP-verktøy
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

I koden ovenfor har vi:

- Definert et enkelt `Bot`-grensesnitt for naturlig språk-interaksjoner
- Brukt LangChain4j sin `AiServices` for automatisk å binde LLM med MCP verktøytilbyder
- Rammeverket håndterer automatisk verktøyskjema-konvertering og funksjonskall i bakgrunnen
- Denne tilnærmingen eliminerer manuell verktøyskonvertering - LangChain4j håndterer all kompleksitet ved å konvertere MCP-verktøy til LLM-kompatibelt format

#### Rust

For å konvertere MCP-verktøysvaret til et format som LLM kan forstå, legger vi til en hjelpefunksjon som formaterer verktøyliste. Legg til følgende kode i `main.rs`-filen din under `main`-funksjonen. Dette vil bli kalt når vi gjør forespørsler til LLM:

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

Flott, vi er klare til å håndtere brukerforespørsler, så la oss ta tak i det neste.

### -4- Håndtere brukerforespørsel

I denne delen av koden vil vi håndtere brukerforespørsler.

#### TypeScript

1. Legg til en metode som skal brukes til å kalle vår LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Kall serverens verktøy
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gjør noe med resultatet
        // Å gjøre

        }
    }
    ```

    I koden ovenfor har vi:

    - Lagt til en metode `callTools`.
    - Metoden tar et LLM-svar og sjekker hvilke verktøy som eventuelt har blitt kalt:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // kall verktøy
        }
        ```

    - Kaller et verktøy, hvis LLM indikerer at det skal kalles:

        ```typescript
        // 2. Kall serverens verktøy
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gjør noe med resultatet
        // TODO
        ```

2. Oppdater `run`-metoden til å inkludere kall til LLM og kalle `callTools`:

    ```typescript

    // 1. Lag meldinger som er input for LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Kaller LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Gå gjennom LLM-responsen, sjekk for hvert valg om det har verktøysanrop
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Flott, la oss liste koden komplett:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importer zod for skjema validering

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // kan måtte endres til denne URL-en i fremtiden: https://models.github.ai/inference
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
          // Lag et zod skjema basert på input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Sett eksplisitt type til "function"
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
    
    
          // 2. Kall serverens verktøy
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Gjør noe med resultatet
          // MÅ GJØRES
    
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
    
        // 3. Gå gjennom LLM-svaret, for hvert valg, sjekk om det har verktøy-kall
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

1. La oss legge til noen imports som trengs for å kalle en LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Neste, la oss legge til funksjonen som skal kalle LLM:

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
            # Valgfrie parametere
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

    I koden ovenfor har vi:

    - Overført våre funksjoner som vi fant på MCP-serveren og konverterte, til LLM.
    - Deretter kalte vi LLM med disse funksjonene.
    - Deretter inspiserer vi resultatet for å se hvilke funksjoner vi bør kalle, om noen.
    - Til slutt sender vi en liste med funksjoner som skal kalles.

3. Siste steg, la oss oppdatere hovedkoden vår:

    ```python
    prompt = "Add 2 to 20"

    # spør LLM hvilke verktøy å bruke, hvis noen
    functions_to_call = call_llm(prompt, functions)

    # kall foreslåtte funksjoner
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Der, det var siste steg, i koden over gjør vi:

    - Kaller et MCP-verktøy via `call_tool` ved å bruke en funksjon som LLM mente vi skulle kalle basert på vårt prompt.
    - Skriver ut resultatet av verktøykallet til MCP-serveren.

#### .NET

1. La oss vise noe kode for å gjøre en LLM-prompt-forespørsel:

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

    I koden ovenfor har vi:

    - Hentet verktøy fra MCP-serveren, `var tools = await GetMcpTools()`.
    - Definert en bruker-prompt `userMessage`.
    - Konstruert et opsjonsobjekt som spesifiserer modell og verktøy.
    - Sendt en forespørsel til LLM.

2. Ett siste steg, la oss se om LLM mener vi bør kalle en funksjon:

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

    I koden ovenfor har vi:

    - Løpt gjennom en liste med funksjonskall.
    - For hvert verktøykall, hent ut navn og argumenter og kall verktøyet på MCP-serveren ved hjelp av MCP-klienten. Til slutt skriver vi ut resultatene.

Her er koden komplett:

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
    // Utfør forespørsler på naturlig språk som automatisk bruker MCP-verktøy
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

I koden ovenfor har vi:

- Brukt enkle naturlige språk-prompt for å interagere med MCP-serververktøyene
- LangChain4j-rammeverket håndterer automatisk:
  - Konvertering av bruker-prompt til verktøykall når det trengs
  - Kalling av aktuelle MCP-verktøy basert på LLM sin avgjørelse
  - Håndtering av samtaleflyten mellom LLM og MCP-serveren
- Metoden `bot.chat()` returnerer naturlige språksvar som kan inkludere resultater fra kjøring av MCP-verktøy
- Denne tilnærmingen gir en sømløs brukeropplevelse hvor brukere ikke trenger å kjenne til den underliggende MCP-implementasjonen

Komplett kodeeksempel:

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


Her skjer hoveddelen av arbeidet. Vi vil kalle LLM med den innledende brukerprompten, deretter behandle svaret for å se om noen verktøy må kalles. Hvis det er tilfelle, vil vi kalle disse verktøyene og fortsette samtalen med LLM til ingen flere verktøyskall trengs og vi har et endelig svar.

Vi kommer til å gjøre flere kall til LLM, så la oss definere en funksjon som håndterer LLM-kallet. Legg til følgende funksjon i filen din `main.rs`:

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

Denne funksjonen tar LLM-klienten, en liste med meldinger (inkludert brukerprompten), verktøy fra MCP-serveren, og sender en forespørsel til LLM, og returnerer svaret.

Svaret fra LLM vil inneholde en array med `choices`. Vi må behandle resultatet for å se om noen `tool_calls` er til stede. Dette lar oss vite at LLM etterspør at et spesifikt verktøy skal kalles med argumenter. Legg til følgende kode nederst i filen `main.rs` for å definere en funksjon som håndterer LLM-svaret:

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

    // Skriv ut innhold hvis tilgjengelig
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Håndter verktøysanrop
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Legg til assistentmelding

        // Utfør hvert verktøysanrop
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Legg til verktøyresultat i meldinger
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Fortsett samtalen med verktøyresultater
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

Hvis `tool_calls` er til stede, henter den ut verktøysinformasjonen, kaller MCP-serveren med verktøyforespørselen, og legger resultatene til samtalemeldingene. Den fortsetter deretter samtalen med LLM og meldingene oppdateres med assistentens svar og resultater fra verktøyskall.

For å hente ut informasjon om verktøyskall som LLM returnerer for MCP-kall, vil vi legge til en hjelpefunksjon som henter ut alt som trengs for å utføre kallet. Legg til følgende kode nederst i filen din `main.rs`:

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

Med alle delene på plass kan vi nå håndtere den innledende brukerprompten og kalle LLM. Oppdater funksjonen din `main` for å inkludere følgende kode:

```rust
// LLM-samtale med verktøyanrop
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

Dette vil spørre LLM med den innledende brukerprompten som ber om summen av to tall, og det vil behandle svaret for dynamisk å håndtere verktøyskall.

Flott, du klarte det!

## Oppgave

Ta koden fra øvelsen og bygg ut serveren med flere verktøy. Lag deretter en klient med en LLM, som i øvelsen, og test det ut med forskjellige prompts for å sikre at alle serververktøyene dine blir kalt dynamisk. Måten å bygge en klient på slik gir sluttbrukeren en flott brukeropplevelse da de kan bruke prompts i stedet for eksakte klientkommandoer, og være uvitende om at noen MCP-server kalles.

## Løsning

[Løsning](./solution/README.md)

## Viktige punkter

- Å legge til en LLM i klienten gir en bedre måte for brukere å samhandle med MCP-servere.
- Du må konvertere MCP-serverens svar til noe LLM kan forstå.

## Eksempler

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulator](../../../../03-GettingStarted/samples/rust)

## Ytterligere ressurser

## Hva er det neste

- Neste: [Konsumer en server ved hjelp av Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->