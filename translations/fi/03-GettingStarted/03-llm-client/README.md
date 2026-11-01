# Asiakas, jossa on LLM

> [!NOTE]
> Java-asiakasesimerkit käyttävät yhteyteen vanhaa HTTP+SSE-protokollaa ja
> kohdistuvat MCP `2025-11-25` SDK -rajapintoihin. Käytä `2026-07-28`-yhteensopivaa SDK:ta ja
> Streamable HTTP:tä uusissa etäasiakkaissa.

Tähän asti olet nähnyt, kuinka luodaan palvelin ja asiakas. Asiakas on voinut kutsua palvelinta erikseen listatakseen sen työkalut, resurssit ja kehotteet. Tämä ei kuitenkaan ole kovin käytännöllinen lähestymistapa. Käyttäjäsi elävät agenttiperäisessä aikakaudessa ja odottavat käyttävänsä kehotteita ja kommunikoivansa LLM:n kanssa. Heitä ei kiinnosta, käytätkö MCP:tä kykyjen tallentamiseen; he yksinkertaisesti odottavat vuorovaikutusta luonnollisella kielellä. Joten miten tätä ratkaistaan? Ratkaisu on lisätä LLM asiakkaaseen.

## Yleiskatsaus

Tässä oppitunnissa keskitymme lisäämään LLM:n asiakkaaseen ja näytämme, kuinka tämä tarjoaa paljon paremman käyttäjäkokemuksen.

## Oppimistavoitteet

Oppitunnin lopuksi osaat:

- Luoda asiakkaan, jossa on LLM.
- Vuorovaikuttaa saumattomasti MCP-palvelimen kanssa käyttäen LLM:ää.
- Tarjota parempi loppukäyttäjäkokemus asiakaspäässä.

## Lähestymistapa

Yritetään ymmärtää lähestymistapa, jota meidän täytyy käyttää. LLM:n lisääminen kuulostaa yksinkertaiselta, mutta aiommeko todella tehdä sen?

Näin asiakas suhtautuu palvelimeen:

1. Perusta yhteys palvelimeen.

1. Listaa kyvyt, kehotteet, resurssit ja työkalut ja tallenna niiden skeema.

1. Lisää LLM ja anna tallennetut kyvyt ja niiden skeema muodossa, jonka LLM ymmärtää.

1. Käsittele käyttäjän kehotetta välittämällä se LLM:lle yhdessä asiakkaan listaamien työkalujen kanssa.

Hienoa, nyt ymmärrämme miten tämä tehdään yleisellä tasolla. Kokeillaan tätä seuraavassa harjoituksessa alla.

## Harjoitus: Asiakkaan luominen LLM:llä

Tässä harjoituksessa opimme lisäämään LLM:n asiakkaaseen.

### Microsoft Foundryn konfigurointi

GitHub Models lopetettiin 30. heinäkuuta 2026. Luo Microsoft Foundry -resurssi,
ota käyttöön aktiivinen malli, kuten `gpt-5.1`, ja aseta nämä ympäristömuuttujat:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

Käytä käyttöönottajan nimeä API-kutsuissa. Se voi poiketa mallin
nimestä. Tarkista
[Microsoft Foundryn mallien lopetusohjelma](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
ennen mallin valintaa.

### -1- Yhdistä palvelimeen

Luodaan ensin asiakkaamme:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod for schema validation

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
            }
            );    
    }
}
```

Edellisessä koodissa olemme:

- Tuoneet tarvittavat kirjastot
- Luoneet luokan, jossa on kaksi jäsenmuuttujaa, `client` ja `openai`, jotka auttavat hallinnoimaan asiakasta ja vuorovaikutusta LLM:n kanssa.
- Määrittäneet OpenAI-asiakkaan käyttämään Microsoft Foundryn v1-päätepistettä ja API-avainta.

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

Edellisessä koodissa olemme:

- Tuoneet MCP-kirjastot
- Luoneet asiakkaan

#### .NET

```csharp
using ModelContextProtocol.Client;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
var client = new ChatClient(
    deployment,
    new ApiKeyCredential(apiKey),
    new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

Ensiksi sinun täytyy lisätä LangChain4j-riippuvuudet `pom.xml`-tiedostoosi. Lisää nämä riippuvuudet mahdollistamaan MCP-integraatio ja OpenAI-yhteensopiva MiniMax API:

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

Aseta MiniMax API-avain ja halutessasi päätepiste ja malli.
`MINIMAX_MODEL_ID` tukee `MiniMax-M3` ja `MiniMax-M2.7`. Jos
`OPENAI_BASE_URL` ei ole asetettu, `MINIMAX_REGION` tukee `global_en` ja `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Valitaksesi päätepisteen alueen mukaan, jätä pois `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Luo sitten Java-asiakasluokkasi:

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

        // Create MCP transport for connecting to server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Create MCP client
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

Edellisessä koodissa olemme:

- **Lisänneet LangChain4j-riippuvuudet**: tarpeellisia MCP-integraatiolle ja OpenAI-yhteensopivalle MiniMax API:lle
- **Tuoneet LangChain4j-kirjastot**: MCP-integraatiota ja OpenAI-chat-mallin toiminnallisuutta varten
- **Luoneet `ChatLanguageModel`**: asetettu käyttämään MiniMaxia MiniMax API-avaimesi, päätepisteesi ja tuetun malli-ID:n kanssa
- **Määrittäneet HTTP-siirron**: käyttäen Server-Sent Events (SSE) yhteyden muodostamiseen MCP-palvelimeen
- **Luoneet MCP-asiakkaan**: joka hoitaa kommunikoinnin palvelimen kanssa
- **Käyttäneet LangChain4j:n sisäänrakennettua MCP-tukea**: joka yksinkertaistaa integraatiota LLM:n ja MCP-palvelimien välillä

#### Rust

Tämä esimerkki olettaa, että sinulla on Rust-pohjainen MCP-palvelin käynnissä. Jos sinulla ei ole, katso takaisin [01-first-server](../01-first-server/README.md) -oppituntiin luodaksesi palvelimen.

Kun sinulla on Rust MCP-palvelin, avaa terminaali ja siirry samaan hakemistoon palvelimen kanssa. Suorita sitten seuraava komento luodaksesi uuden LLM-asiakasprojektin:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Lisää seuraavat riippuvuudet `Cargo.toml`-tiedostoosi:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Rustille ei ole virallista OpenAI-kirjastoa, mutta `async-openai` crate on [yhteisön ylläpitämä kirjasto](https://platform.openai.com/docs/libraries/rust#rust), jota yleisesti käytetään.

Avaa `src/main.rs`-tiedosto ja korvaa sen sisältö seuraavalla koodilla:

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
    // Initial message
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Setup Microsoft Foundry client
    let endpoint = std::env::var("AZURE_OPENAI_ENDPOINT")?;
    let api_key = std::env::var("AZURE_OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base(format!("{}/openai/v1", endpoint.trim_end_matches('/')))
            .with_api_key(api_key),
    );

    // Setup MCP client
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

    // TODO: Get MCP tool listing 

    // TODO: LLM conversation with tool calls

    Ok(())
}
```

Tämä koodi konfiguroi Rust-sovelluksen, joka yhdistää MCP-palvelimeen ja
Microsoft Foundryn malliin LLM-vuorovaikutuksia varten.

> [!IMPORTANT]
> Aseta `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY` ja
> `AZURE_OPENAI_DEPLOYMENT` ennen sovelluksen ajoa.

Hienoa, seuraavassa vaiheessa listaamme palvelimen kyvyt.

### -2- Listaa palvelimen kyvyt

Nyt yhdistämme palvelimeen ja pyydämme sen kykyjä:

#### Typescript

Lisää samaan luokkaan seuraavat metodit:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // listing tools
    const toolsResult = await this.client.listTools();
}
```

Edellisessä koodissa olemme:

- Lisänneet koodin palvelimeen yhdistämiseksi, `connectToServer`.
- Luoneet `run`-metodin, joka vastaa sovelluksen työnkulun hallinnasta. Tähän asti se listaa vain työkalut, mutta lisäämme siihen pian lisää.

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
    print("Tool", tool.inputSchema["properties"])
```

Lisäsimme seuraavaa:

- Listattiin resurssit ja työkalut ja tulostettiin ne. Työkaluista listaamme myös `inputSchema`, jota käytämme myöhemmin.

#### .NET

```csharp
async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

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

Edellisessä koodissa olemme:

- Listanneet MCP-palvelimen käytettävissä olevat työkalut
- Jokaiselle työkalulle listanneet nimen, kuvauksen ja sen skeeman. Viimeksi mainittua käytämme kutsuissa pian.

#### Java

```java
// Create a tool provider that automatically discovers MCP tools
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// The MCP tool provider automatically handles:
// - Listing available tools from the MCP server
// - Converting MCP tool schemas to LangChain4j format
// - Managing tool execution and responses
```

Edellisessä koodissa olemme:

- Luoneet `McpToolProvider`, joka automaattisesti havaitaan ja rekisteröi kaikki työkalut MCP-palvelimelta
- Työkalutoimittaja huolehtii MCP-työkalujen skeemoiden ja LangChain4jin työkalumuodon muuntamisesta sisäisesti
- Tämä lähestymistapa abstrahoi manuaalisen työkalulistauksen ja muuntoprosessin

#### Rust

Työkalujen hakeminen MCP-palvelimelta tapahtuu `list_tools`-metodilla. Lisää `main`-funktiosi, MCP-asiakasasetusten jälkeen, seuraava koodi:

```rust
// Get MCP tool listing 
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Muunna palvelimen kyvyt LLM-työkaluiksi

Seuraava vaihe kykyjen listaamisen jälkeen on muuntaa ne LLM:n ymmärtämään muotoon. Näin voimme tarjota nämä kyvyt työkaluna LLM:lle.

#### TypeScript

1. Lisää seuraava koodi muuntamaan MCP-palvelimen vastaus työkalumuotoon, jota LLM voi käyttää:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Create a zod schema based on the input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Explicitly set type to "function"
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

    Yllä oleva koodi ottaa MCP-palvelimen vastauksen ja muuntaa sen työkalumäärittelyksi, jonka LLM ymmärtää.

2. Päivitetään seuraavaksi `run`-metodi listaamaan palvelimen kyvyt:

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

    Edellisessä koodissa päivitämme `run`-metodin käymään tuloksen läpi ja kutsumaan jokaiselle merkinnälle `openAiToolAdapter`.

#### Python

1. Luodaan ensin seuraava muunnosfunktio

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

    Yllä olevassa `convert_to_llm_tools`-funktiossa otamme MCP-työkaluvastauksen ja muunnamme sen muotoon, jonka LLM ymmärtää.

2. Päivitetään sitten koodimme käyttämään tätä funktiota näin:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Tässä lisäämme kutsun `convert_to_llm_tool`, jolla muunnetaan MCP-työkaluvastaus myöhempää LLM:n syöttöä varten.

#### .NET

1. Lisätään koodi, joka muuntaa MCP-työkaluvastauksen LLM:n ymmärtämään muotoon

```csharp
ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}
```

Edellisessä koodissa olemme:

- Luoneet funktion `ConvertFrom`, joka ottaa nimen, kuvauksen ja syötteen skeeman.
- Luoneet OpenAI `ChatTool` MCP-työkalun JSON-skeemasta.

2. Päivitetään joitain olemassa olevia koodinpätkiä hyödyntämään yllä olevaa funktiota:

    ```csharp
    async Task<List<ChatTool>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatTool> toolDefinitions = [];

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);
        }

        return toolDefinitions;
    }
    ```
    
Edellisessä koodissa olemme:

- Päivittäneet funktion muuntamaan MCP-työkaluvastauksen LLM-työkaluksi. Korostetaan lisätty koodi:

   ```csharp
   JsonElement propertiesElement;
   tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

   var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
   Console.WriteLine($"Tool definition: {def}");
   toolDefinitions.Add(def);
   ```

Syötteen skeema on osa työkalun vastausta, mutta "properties"-attribuutissa, joten se täytyy ottaa talteen. Lisäksi kutsumme nyt `ConvertFrom` työkaludetaljeilla. Nyt kun raskain työ on tehty, katsotaan seuraavaksi miten kutsu käyttäjän kehotteeseen hoidetaan.

#### Java

```java
// Create a Bot interface for natural language interaction
public interface Bot {
    String chat(String prompt);
}

// Configure the AI service with LLM and MCP tools
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Edellisessä koodissa olemme:

- Määritelleet yksinkertaisen `Bot`-rajapinnan luonnollisen kielen vuorovaikutuksille
- Käyttäneet LangChain4j:n `AiServices` sitomaan LLM MCP-työkalutoimittajaan automaattisesti
- Kehys hoitaa automaattisesti työkaluskeeman muunnoksen ja funktiokutsut taustalla
- Tämä poistaa manuaalisen työkalumuunnoksen - LangChain4j huolehtii MCP-työkalujen muuntamisesta LLM-yhteensopiviksi

#### Rust

MCP-työkaluvastauksen muuntamiseksi LLM:n ymmärtämään muotoon lisäämme apufunktion, joka muotoilee työkalulistauksen. Lisää seuraava koodi `main.rs`-tiedostoosi `main`-funktion alapuolelle. Tätä kutsutaan, kun teemme pyyntöjä LLM:lle:

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

Hienoa, nyt olemme valmiita käsittelemään käyttäjän pyyntöjä, joten siirrytään siihen.

### -4- Käsittele käyttäjän kehotepyyntö

Tässä osassa koodia käsittelemme käyttäjän pyyntöjä.

#### TypeScript

1. Lisää metodi, jota käytetään LLM:n kutsumiseen:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  

        }
    }
    ```

    Edellisessä koodissa me:

    - Lisäsimme metodin `callTools`.
    - Metodi vastaanottaa LLM:n vastauksen ja tarkistaa, onko työkaluja kutsuttu:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // call tool
        }
        ```

    - Kutsuu työkalua, jos LLM ilmoittaa, että sitä pitää kutsua:

        ```typescript
        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  
        ```

2. Päivitä `run`-metodi sisältämään kutsut LLM:lle ja työkalun kutsut `callTools`:

    ```typescript

    // 1. Create messages that's input for the LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Calling the LLM
    let response = this.openai.chat.completions.create({
        model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
        max_completion_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Go through the LLM response,for each choice, check if it has tool calls 
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Hienoa, listataan koko koodi kokonaisuudessaan:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod for schema validation

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
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
          // Create a zod schema based on the input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Explicitly set type to "function"
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
    
    
          // 2. Call the server's tool 
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Do something with the result
          // TODO  
    
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
            model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
            max_completion_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 3. Go through the LLM response, for each choice, check if it has tool calls 
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

1. Lisätään tarvittavat importit LLM:n kutsumiseen

    ```python
    # llm
    import os
    from openai import OpenAI
    import json
    ```

2. Seuraavaksi lisätään funktio, joka kutsuu LLM:ää. Tämä esimerkki käyttää
    aktiivista `gpt-5.1` mallia. Katso
    [Microsoft Foundryn mallien lopetusohjelma](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
    mallia valitessasi.

    ```python
    # llm

    def call_llm(prompt, functions):
        client = OpenAI(
            base_url=(
                f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/"
            ),
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
        )

        print("CALLING LLM")
        response = client.chat.completions.create(
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
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"),
            tools=functions,
            max_completion_tokens=1000,
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

    Edellisessä koodissa olemme:

    - Antaneet LLM:lle funktiomme, jotka löysimme MCP-palvelimelta ja muunsimme.
    - Sitten kutsuimme LLM:ää näillä funktioilla.
    - Tutkimme tulosta nähdäksesi, mitä toimintoja meidän tulisi kutsua, jos mitään.
    - Lopuksi annamme listan funktioista, jotka kutsutaan.

3. Viimeinen vaihe, päivitetään pääkoodimme:

    ```python
    prompt = "Add 2 to 20"

    # ask LLM what tools to all, if any
    functions_to_call = call_llm(prompt, functions)

    # call suggested functions
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Siinä se, viimeinen vaihe, yllä olevassa koodissa me:

    - Kutsumme MCP-työkalua `call_tool` käyttäen toimintoa, jonka LLM arvioi meidän pitävän kutsua kehotteen perusteella.
    - Tulostamme työkalukutsun tuloksen MCP-palvelimelle.

#### .NET

1. Näytetään koodi LLM-kehotepyynnön tekemiseksi:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new UserChatMessage(userMessage));


    // 2. Define options, including the tools
    var options = new ChatCompletionOptions
    {
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
    var content = response.Content.FirstOrDefault()?.Text;

    ```

    Edellisessä koodissa olemme:

    - Noudettiin työkaluja MCP-palvelimelta, `var tools = await GetMcpTools()`.
    - Määriteltiin käyttäjän kehotus `userMessage`.
    - Rakennettiin asetukset sisältävä olio, jossa määriteltiin malli ja työkalut.
    - Tehtiin pyyntö LLM:lle.

2. Vielä yksi askel, katsotaanpa, ajattelee LLM, että meidän pitäisi kutsua funktiota:

    ```csharp
    // 4. Check if the response contains a function call
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
        var result = await mcpClient.CallToolAsync(
            call.FunctionName,
            dict!,
            cancellationToken: CancellationToken.None
        );

        var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
        if (textBlock != null)
        {
            Console.WriteLine(textBlock.Text);
        }

    }
    ```

    Edellisessä koodissa olemme:

    - Käyneet läpi listan funktiokutsuja.
    - Jokaiselle työkalukutsulle purkaneet nimen ja argumentit ja kutsuneet työkalua MCP-palvelimella käyttämällä MCP-asiakasta. Lopuksi tulostamme tulokset.

Tässä on koko koodi:

```csharp
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
if (string.IsNullOrWhiteSpace(endpoint) || string.IsNullOrWhiteSpace(apiKey))
{
    Console.WriteLine("Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY.");
    return;
}

var client = new ChatClient(
    model: deployment,
    credential: new ApiKeyCredential(apiKey),
    options: new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });
var chatHistory = new List<ChatMessage>
{
    new SystemChatMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}

async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
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

chatHistory.Add(new UserChatMessage(userMessage));

// 3. Define options, including the tools
var options = new ChatCompletionOptions
{
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
var content = response.Content.FirstOrDefault()?.Text;

// 5. Check if the response contains a function call
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
    var result = await mcpClient.CallToolAsync(
        call.FunctionName,
        dict!,
        cancellationToken: CancellationToken.None
    );

    var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
    if (textBlock != null)
    {
        Console.WriteLine(textBlock.Text);
    }

}

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Execute natural language requests that automatically use MCP tools
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

Edellisessä koodissa olemme:

- Käyttäneet yksinkertaisia luonnollisen kielen kehotteita vuorovaikutukseen MCP-palvelimen työkalujen kanssa
- LangChain4j-kehys hoitaa automaattisesti:
  - Muuntaa käyttäjän kehotteet työkalukutsuiksi tarvittaessa
  - Kutsua sopivia MCP-työkaluja LLM:n päätöksen perusteella
  - Hallita keskustelun kulkua LLM:n ja MCP-palvelimen välillä
- `bot.chat()` -metodi palauttaa luonnollisen kielen vastauksia, jotka voivat sisältää MCP-työkalujen suoritus­tuloksia
- Tämä lähestymistapa tarjoaa saumattoman käyttäjäkokemuksen, jossa käyttäjien ei tarvitse tietää taustalla olevasta MCP:n toteutuksesta

Täydellinen koodiesimerkki:

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

Tässä tapahtuu suurin osa työstä. Kutsumme LLM:ää alkuperäisellä käyttäjän kehotteella, sitten käsittelemme vastauksen nähdäksemme, tarvitseeko joitain työkaluja kutsua. Jos tarvitsee, kutsumme nämä työkalut ja jatkamme keskustelua LLM:n kanssa, kunnes ei tarvita enää työkalukutsuja ja meillä on lopullinen vastaus.

Teemme useita kutsuja LLM:lle, joten määritellään funktio, joka hoitaa LLM-kutsun. Lisää seuraava funktio tiedostoosi `main.rs`:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let model = std::env::var("AZURE_OPENAI_DEPLOYMENT")
        .unwrap_or_else(|_| "gpt-5.1".to_string());
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": model,
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

Tämä funktio ottaa vastaan LLM-asiakkaan, viestilistan (sisältäen käyttäjän kehotteen), työkalut MCP-palvelimelta ja lähettää pyynnön LLM:lle, palauttaen vastauksen.

LLM:n vastaus sisältää `choices` taulukon. Meidän on käsiteltävä tulos nähdäksesi, onko siellä `tool_calls`. Tämä kertoo meille, että LLM pyytää tietyn työkalun kutsumista argumenttien kanssa. Lisää seuraava koodi tiedostosi `main.rs` loppuun määritelläksesi funktion LLM-vastauksen käsittelyyn:

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

    // Print content if available
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Handle tool calls
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Add assistant message

        // Execute each tool call
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Add tool result to messages
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Continue conversation with tool results
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

Jos `tool_calls` ovat läsnä, se poimii työkalutiedot, kutsuu MCP-palvelinta työkalupyynnöllä ja lisää tulokset keskustelun viesteihin. Se jatkaa sitten keskustelua LLM:n kanssa ja viestit päivitetään avustajan vastauksella ja työkalukutsujen tuloksilla.

Työkalukutsutietojen poimimiseksi, jotka LLM palauttaa MCP-kutsuja varten, lisäämme toisen apufunktion, joka poimii kaiken tarvittavan kutsun tekemiseen. Lisää seuraava koodi tiedostosi `main.rs` loppuun:

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

Kun kaikki palaset ovat paikoillaan, voimme käsitellä alkuperäisen käyttäjän kehotteen ja kutsua LLM:n. Päivitä `main` funktiosi sisältämään seuraava koodi:

```rust
// LLM conversation with tool calls
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

Tämä kysyy LLM:ltä alkuperäisellä käyttäjän kehotteella kahden luvun summan ja käsittelee vastauksen dynaamisesti käsitelläkseen työkalukutsuja.

Hienoa, onnistuit!

## Tehtävä

Ota koodi harjoituksesta ja laajenna palvelinta lisäämällä muutamia työkaluja. Luo sitten asiakas käyttäen LLM:ää, kuten harjoituksessa, ja testaa sitä erilaisilla kehotteilla varmistaaksesi, että kaikki palvelimesi työkalut kutsutaan dynaamisesti. Tällä tavalla rakennettu asiakas tarjoaa loppukäyttäjälle erinomaisen käyttökokemuksen, koska he voivat käyttää kehotteita, eivät tarkkoja asiakaskomentoja, ja he ovat tietämättömiä mistään MCP-palvelimen kutsuista.

## Ratkaisu

[Ratkaisu](./solution/README.md)

## Tärkeimmät opit

- LLM:n lisääminen asiakkaallesi tarjoaa paremman tavan käyttäjien vuorovaikutukseen MCP-palvelimien kanssa.
- Sinun täytyy muuntaa MCP-palvelimen vastaus muotoon, jonka LLM ymmärtää.

## Esimerkit

- [Java Laskin](../samples/java/calculator/README.md)
- [.NET Laskin](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Laskin](../samples/javascript/README.md)
- [TypeScript Laskin](../samples/typescript/README.md)
- [Python Laskin](../../../../03-GettingStarted/samples/python)
- [Rust Laskin](../../../../03-GettingStarted/samples/rust)

## Lisäresurssit

## Mitä seuraavaksi

- Seuraavaksi: [Palvelimen käyttäminen Visual Studio Codella](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->