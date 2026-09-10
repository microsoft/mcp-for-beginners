# Asiakas LLM:n kanssa

Tähän asti olet nähnyt, miten palvelin ja asiakas luodaan. Asiakas on voinut kutsua palvelinta erikseen listatakseen sen työkalut, resurssit ja kehotteet. Tämä ei kuitenkaan ole kovin käytännöllinen lähestymistapa. Käyttäjäsi elävät agenttisella aikakaudella ja odottavat käyttävänsä kehotteita ja kommunikoivansa LLM:n kanssa sen sijaan. Heitä ei kiinnosta, käytätkö MCP:tä kykyjen tallentamiseen; he vain odottavat vuorovaikuttavansa luonnollisella kielellä. Miten siis ratkaistaan tämä? Ratkaisu on lisätä LLM asiakkaaseen.

## Yleiskatsaus

Tässä oppitunnissa keskitymme lisäämään LLM:n asiakkaaseen ja näytämme, miten tämä tarjoaa paljon paremman käyttökokemuksen käyttäjälle.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Luoda asiakkaan, jossa on LLM.
- Vuorovaikuttaa saumattomasti MCP-palvelimen kanssa LLM:n avulla.
- Tarjota parempi loppukäyttäjäkokemus asiakaspäässä.

## Lähestymistapa

Yritetään ymmärtää tarvittava lähestymistapa. LLM:n lisääminen kuulostaa yksinkertaiselta, mutta tehdäkö se tosiasiassa?

Näin asiakas vuorovaikuttaa palvelimen kanssa:

1. Luo yhteys palvelimeen.

1. Listaa kyvyt, kehotteet, resurssit ja työkalut, ja tallenna niiden skeemat.

1. Lisää LLM ja syötä tallennetut kyvyt ja niiden skeemat muodossa, jonka LLM ymmärtää.

1. Käsittele käyttäjän kehotetta välittämällä se LLM:lle yhdessä asiakkaan listaamien työkalujen kanssa.

Hienoa, nyt ymmärrämme miten tämä toimii yleisellä tasolla, kokeillaan tätä seuraavassa harjoituksessa.

## Harjoitus: Asiakkaan luominen LLM:n kanssa

Tässä harjoituksessa opimme lisäämään LLM:n asiakkaaseemme.

### Autentikointi GitHub Personal Access Tokenilla

GitHub-tokenin luominen on suoraviivainen prosessi. Näin se tehdään:

- Siirry GitHubin asetuksiin – Klikkaa profiilikuvakettasi oikeassa yläkulmassa ja valitse Asetukset.
- Siirry kehittäjäasetuksiin – Vieritä alas ja klikkaa Developer Settings.
- Valitse Personal Access Tokens – Klikkaa Fine-grained tokens ja sitten Generate new token.
- Määritä tokenisi – Lisää muistiinpano, aseta vanhentumispäivä ja valitse tarvittavat oikeudet (scopet). Tässä tapauksessa varmista, että lisäät Models-oikeuden.
- Luo ja kopioi token – Klikkaa Generate token, ja muista kopioida se välittömästi, et voi nähdä sitä uudelleen.

### -1- Yhdistä palvelimeen

Luodaan ensin asiakas:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Tuo zod skeemavarmistusta varten

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

Edellisessä koodissa olemme:

- Tuoneet tarvittavat kirjastot
- Luoneet luokan, jolla on kaksi jäsentä, `client` ja `openai`, jotka auttavat meitä hallitsemaan asiakasta ja vuorovaikuttamaan LLM:n kanssa erikseen.
- Konfiguroineet LLM-instanssimme käyttämään GitHub Modelsia asettamalla `baseUrl` osoittamaan inference API:iin.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Luo palvelimen parametrit stdio-yhteydelle
server_params = StdioServerParameters(
    command="mcp",  # Suoritettava tiedosto
    args=["run", "server.py"],  # Valinnaiset komentorivin argumentit
    env=None,  # Valinnaiset ympäristömuuttujat
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Alusta yhteys
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Edellisessä koodissa olemme:

- Tuoneet MCP:n tarvitsemat kirjastot
- Luoneet asiakkaan

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

Ensin sinun tulee lisätä LangChain4j-riippuvuudet `pom.xml`-tiedostoosi. Lisää nämä riippuvuudet MCP-integraation ja OpenAI-yhteensopivan MiniMax API:n käyttöä varten:

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

Aseta MiniMax API -avaimesi ja tarvittaessa myös päätepiste ja malli.
`MINIMAX_MODEL_ID` tukee `MiniMax-M3` ja `MiniMax-M2.7`. Jos
`OPENAI_BASE_URL` ei ole asetettu, `MINIMAX_REGION` tukee `global_en` ja `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Päätepisteen valitsemiseksi alueen mukaan jätä pois `OPENAI_BASE_URL`:

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

        // Luo MCP-siirto yhteyden muodostamiseksi palvelimeen
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Luo MCP-asiakas
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

- **Lisänneet LangChain4j-riippuvuudet**: Tarvitaan MCP-integraatioon ja OpenAI-yhteensopivan MiniMax API:n käyttöön
- **Tuoneet LangChain4j-kirjastot**: MCP-integraatiota ja OpenAI-chat-mallin toimintoa varten
- **Luoneet `ChatLanguageModel`-instanssin**: Konfiguroitu käyttämään MiniMaxia MiniMax API-avaimella, päätepisteellä ja tuetuilla mallin tunnuksilla
- **Asetettu HTTP-siirto**: Käyttäen Server-Sent Events (SSE) -tekniikkaa MCP-palvelimeen yhdistämiseen
- **Luotu MCP-asiakas**: Joka käsittelee kommunikoinnin palvelimen kanssa
- **Käytetty LangChain4jn sisäänrakennettua MCP-tukea**: Joka yksinkertaistaa LLM:ien ja MCP-palvelinten välistä integraatiota

#### Rust

Tässä esimerkissä oletetaan, että sinulla on Rust-pohjainen MCP-palvelin käynnissä. Jos sinulla ei ole sellaista, katso [01-first-server](../01-first-server/README.md) -oppitunti palvelimen luomiseksi.

Kun sinulla on Rust MCP -palvelin, avaa terminaali ja siirry samaan hakemistoon palvelimen kanssa. Suorita sitten seuraava komento luodaksesi uuden LLM-asiakasprojektin:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Lisää seuraavat riippuvuudet `Cargo.toml` -tiedostoosi:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Virallista Rust-kirjastoa OpenAI:lle ei ole, mutta `async-openai` -paketti on [yhteisön ylläpitämä kirjasto](https://platform.openai.com/docs/libraries/rust#rust), jota yleisesti käytetään.

Avaa `src/main.rs` -tiedosto ja korvaa sen sisältö seuraavalla koodilla:

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
    // Alkuviesti
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Aseta OpenAI-asiakas
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Aseta MCP-asiakas
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

    // TODO: Hanki MCP-työkaluluettelo

    // TODO: LLM-keskustelu työkalukutsuilla

    Ok(())
}
```

Tämä koodi perustaa perus-Rust-sovelluksen, joka yhdistyy MCP-palvelimeen ja GitHub Modelsiin LLM-vuorovaikutuksia varten.

> [!IMPORTANT]
> Muista asettaa ympäristömuuttuja `OPENAI_API_KEY` GitHub-tokenillasi ennen sovelluksen käynnistämistä.

Hienoa, seuraavana askeleena listataan palvelimen kyvyt.

### -2- Listaa palvelimen kyvyt

Nyt yhdistämme palvelimeen ja kysymme sen kyvyt:

#### TypeScript

Lisää samaan luokkaan seuraavat metodit:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // työkalujen luetteloiminen
    const toolsResult = await this.client.listTools();
}
```

Edellisessä koodissa olemme:

- Lisänneet koodin palvelimeen yhdistämiseksi, `connectToServer`.
- Luoneet `run`-metodin, joka hallitsee sovelluksen kulkua. Tällä hetkellä se listaa vain työkalut, mutta lisäämme siihen pian lisää.

#### Python

```python
# Listaa saatavilla olevat resurssit
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Listaa saatavilla olevat työkalut
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Tässä lisäykset:

- Listataan resurssit ja työkalut ja tulostetaan ne. Työkaluista listataan myös `inputSchema`, jota käytämme myöhemmin.

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

Edellisessä koodissa olemme:

- Listanneet MCP-palvelimen työkalut
- Jokaisesta työkalusta listattu nimi, kuvaus ja skeema. Jälkimmäistä käytämme pian työkalukutsuihin.

#### Java

```java
// Luo työkaluntarjoaja, joka löytää MCP-työkalut automaattisesti
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP-työkaluntarjoaja hoitaa automaattisesti:
// - Saatavilla olevien työkalujen listaaminen MCP-palvelimelta
// - MCP-työkalujen skeemojen muuntaminen LangChain4j-muotoon
// - Työkalujen suorituksen ja vastausten hallinta
```

Edellisessä koodissa olemme:

- Luoneet `McpToolProvider`-luokan, joka automaattisesti löytää ja rekisteröi kaikki MCP-palvelimen työkalut
- Työkalumoduuli hoitaa MCP-työkalujen skeemojen ja LangChain4jn työkalumuodon muunnokset sisäisesti
- Tämä lähestymistapa vapauttaa manuaalisesta työkalulistauksesta ja muuntamisesta

#### Rust

MCP-palvelimen työkalujen hakeminen tehdään `list_tools`-metodilla. Lisää pääfunktiossa MCP-asiakkaan muodostamisen jälkeen seuraava koodi:

```rust
// Hanki MCP-työkalun listaus
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Muunna palvelimen kyvyt LLM-työkaluiksi

Seuraava askel palvelimen kykyjen listaamisen jälkeen on muuntaa ne muodoksi, jonka LLM ymmärtää. Kun tämä on tehty, voimme tarjota nämä kyvyt LLM:n työkaluina.

#### TypeScript

1. Lisää seuraava koodi muuntamaan MCP-palvelimen vastaus LLM:n käyttämään työkalumuotoon:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Luo zod-skeema input_schema:n perusteella
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Aseta tyyppi eksplisiittisesti "function"iksi
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

    Yllä oleva koodi ottaa MCP-palvelimen vastauksen ja muuntaa sen työkalumääritteen muotoon, jonka LLM ymmärtää.

2. Päivitetään seuraavaksi `run`-metodi listatakseen palvelimen kyvyt:

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

    Edellisessä koodissa olemme päivittäneet `run`-metodin kartoittamaan tuloksen ja kutsumaan jokaisesta merkinnästä `openAiToolAdapter`-funktiota.

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

    Edellisessä `convert_to_llm_tools`-funktiossa otetaan MCP-työkaluvastaus ja muutetaan se LLM:n ymmärtämään muotoon.

2. Päivitetään seuraavaksi asiakaskoodi käyttämään tätä funktiota:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Tässä lisäämme kutsun `convert_to_llm_tool`-funktiolle muuttaaksemme MCP-työkaluvastauksen LLM:lle sopivaksi.

#### .NET

1. Lisätään koodi muuntamaan MCP-työkaluvastaus LLM:n ymmärtämään muotoon

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

Edellisessä koodissa olemme:

- Luoneet funktion `ConvertFrom`, joka ottaa vastaan nimen, kuvauksen ja input-skeeman.
- Määritelleet toiminnallisuuden, joka luo `FunctionDefinition`-olion, joka välitetään `ChatCompletionsDefinition`:ille. Tämä on LLM:n ymmärtämä.

2. Päivitetään seuraavaksi olemassa olevaa koodia hyödyntämään tätä funktiota:

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
// Luo bottirajapinta luonnollisen kielen vuorovaikutusta varten
public interface Bot {
    String chat(String prompt);
}

// Määritä tekoälypalvelu LLM- ja MCP-työkaluilla
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Edellisessä koodissa olemme:

- Määritelleet yksinkertaisen `Bot`-rajapinnan luonnollisen kielen vuorovaikutuksiin
- Käyttäneet LangChain4jn `AiServices`-luokkaa sitomaan LLM automaattisesti MCP-työkaluntarjoajaan
- Kehys hoitaa automaattisesti työkaluskeeman muunnoksen ja funktiokutsut taustalla
- Tämä lähestymistapa poistaa manuaalisen työkalumuunnoksen - LangChain4j huolehtii kaikesta MCP-työkalujen muuntamisen monimutkaisuudesta LLM-yhteensopivaan muotoon

#### Rust

Muuntaaksemme MCP-työkaluvastauksen LLM:n ymmärtämään muotoon lisäämme apufunktion, joka muotoilee työkalulistan. Lisää seuraava koodi `main.rs`-tiedostoosi `main`-funktion alapuolelle. Tätä kutsutaan LLM-pyyntöjen yhteydessä:

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

Hienoa, nyt olemme valmiita käsittelemään käyttäjän pyyntöjä, joten siirrytään siihen seuraavaksi.

### -4- Käyttäjän kehotteen käsittely

Tässä koodin osassa käsittelemme käyttäjän pyyntöjä.

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


        // 2. Kutsu palvelimen työkalua
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tee jotain tuloksella
        // TEHTÄVÄ

        }
    }
    ```

    Edellisessä koodissa olemme:

    - Lisänneet metodin `callTools`.
    - Metodi ottaa LLM:n vastauksen ja tarkistaa, mitä työkaluja on kutsuttu, jos yhtään:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // kutsu työkalu
        }
        ```

    - Kutsuu työkalua, jos LLM ilmaisee, että sitä tulee kutsua:

        ```typescript
        // 2. Kutsu palvelimen työkalua
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tee jotain tuloksella
        // TEHTÄVÄ
        ```

2. Päivitä `run`-metodi sisällyttämään kutsut LLM:lle ja `callTools`-kutsun:

    ```typescript

    // 1. Luo viestit, jotka ovat syötteenä LLM:lle
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Kutsutaan LLM:ää
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Käy läpi LLM:n vastaus, tarkista jokaisesta vaihtoehdosta, onko siinä työkalukutsuja
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
import { z } from "zod"; // Tuo zod skeeman validointia varten

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // saatetaan joutua vaihtamaan tähän url-osoitteeseen tulevaisuudessa: https://models.github.ai/inference
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
          // Luo zod-skeema input_schema:n perusteella
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Aseta tyyppi nimenomaisesti "function"
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
    
    
          // 2. Kutsu palvelimen työkalua
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Tee jotain tuloksella
          // TEHTÄVÄ
    
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
    
        // 3. Käy läpi LLM:n vastaus, tarkista jokaisen vaihtoehdon osalta, sisältääkö se työkalukutsuja
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

1. Lisätään joitakin importteja LLM:n kutsua varten

    ```python
    # suuri kielimalli
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Seuraavaksi lisätään funktio, joka kutsuu LLM:n:

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
            # Valinnaiset parametrit
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

    Edellisessä koodissa olemme:

    - Välittäneet funktiomme, jotka löysimme MCP-palvelimelta ja muunsimme, LLM:lle.
    - Sitten kutsuneet LLM:ää kyseisillä funktioilla.
    - Tarkastelleet tulosta nähdäksesi, mitä funktioita meidän tulisi kutsua, jos yhtään.
    - Lopuksi välittäneet taulukon funktioista, jotka tulee kutsua.

3. Viimeinen vaihe, päivitetään pääkoodi:

    ```python
    prompt = "Add 2 to 20"

    # kysy LLM:ltä, mitä työkaluja saa käyttää, jos saa
    functions_to_call = call_llm(prompt, functions)

    # kutsu ehdotettuja funktioita
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Siinä se, viimeinen vaihe. Edellisessä koodissa:

    - Kutsumme MCP-työkalua `call_tool`-funktiolla käyttäen LLM:n kehotteen perusteella valitsemaa funktiota.
    - Tulostamme työkalukutsun tuloksen MCP-palvelimelle.

#### .NET

1. Näytetään koodi LLM-kehotepyyntöön:

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

    Edellisessä koodissa olemme:

    - Hakuaneet työkalut MCP-palvelimelta, `var tools = await GetMcpTools()`.
    - Määritelleet käyttäjän kehotteen `userMessage`.
    - Rakentaneet opts-olion, jossa määritetään malli ja työkalut.
    - Tehneet pyynnön LLM:lle.

2. Lopuksi, tarkistetaan, haluaako LLM kutsua funktiota:

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

    Edellisessä koodissa olemme:

    - Käyneet läpi listan funktiokutsuista.
    - Jokaisen työkalukutsun kohdalla purkaneet nimen ja argumentit ja kutsuneet työkalua MCP-palvelimella MCP-asiakkaan kautta. Lopuksi tulostamme tulokset.

Tässä koko koodi:

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
    // Suorita luonnollisen kielen pyyntöjä, jotka käyttävät automaattisesti MCP-työkaluja
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

- Käyttäneet yksinkertaisia luonnollisen kielen kehotteita MCP-palvelimen työkalujen kanssa vuorovaikutukseen
- LangChain4j-kehys hoitaa automaattisesti:
  - Käyttäjän kehotteiden muuntamisen työkalukutsuiksi tarvittaessa
  - Sopivien MCP-työkalujen kutsumisen LLM:n päätöksen perusteella
  - Keskustelun hallinnan LLM:n ja MCP-palvelimen välillä
- `bot.chat()`-metodi palauttaa luonnollisen kielen vastauksia, jotka voivat sisältää MCP-työkalujen tuloksia
- Tämä lähestymistapa tarjoaa saumattoman käyttökokemuksen, jossa käyttäjän ei tarvitse tietää taustalla olevasta MCP-toteutuksesta

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

Suurin osa työstä tapahtuu tässä vaiheessa. Kutsumme LLM:ää alkuperäisellä käyttäjän kehotteella, sitten käsittelemme vastauksen selvittääksemme, tarvitseeko kutsua työkaluja. Jos tarvitsee, kutsumme ne, ja jatkamme keskustelua LLM:n kanssa, kunnes työkalukutsuja ei enää tarvita ja saamme lopullisen vastauksen.


Teemme useita kutsuja LLM:lle, joten määritellään funktio, joka hoitaa LLM-kutsun. Lisää seuraava funktio `main.rs`-tiedostoosi:

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

Tämä funktio ottaa LLM-asiakkaan, viestilistan (johon sisältyy käyttäjän kehotus), työkalut MCP-palvelimelta, ja lähettää pyynnön LLM:lle, palauttaen vastauksen.

LLM:n vastaus sisältää taulukon `choices`. Meidän täytyy käsitellä tulosta nähdäksesi, onko siellä `tool_calls`-kohtia. Tämä kertoo meille, että LLM pyytää tietyn työkalun kutsumista argumenteilla. Lisää seuraava koodi `main.rs`-tiedostosi loppuun määritelläksesi funktion joka käsittelee LLM-vastauksen:

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

    // Tulosta sisältö, jos saatavilla
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Käsittele työkalukutsuja
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Lisää avustajan viesti

        // Suorita jokainen työkalukutsu
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Lisää työkalun tulos viesteihin
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Jatka keskustelua työkalun tulosten kanssa
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

Jos `tool_calls`-kohdat ovat läsnä, se poimii työkalutiedot, kutsuu MCP-palvelinta työkalupyynnöllä ja lisää tulokset keskustelun viesteihin. Sen jälkeen keskustelu jatkuu LLM:n kanssa ja viestit päivitetään avustajan vastauksen ja työkalukutsun tulosten mukaan.

Poimiaksesi työkalukutsun tiedot, jotka LLM palauttaa MCP-kutsuja varten, lisäämme toisen apufunktion, joka poimii kaiken tarvittavan kutsua varten. Lisää seuraava koodi `main.rs`-tiedostosi loppuun:

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

Kun kaikki palaset ovat paikoillaan, voimme nyt käsitellä alkuperäisen käyttäjän kehotuksen ja kutsua LLM:ää. Päivitä `main`-funktion sisältämään seuraava koodi:

```rust
// LLM-keskustelu työkalukutsuilla
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

Tämä kysyy LLM:ltä alkukehotuksen, jossa pyydetään kahden luvun summaa, ja käsittelee vastauksen dynaamisesti työkalukutsujen käsittelemiseksi.

Hienoa, onnistuit!

## Tehtävä

Ota harjoituksen koodi ja laajenna palvelinta lisäämällä siihen enemmän työkaluja. Luo sitten asiakas, joka käyttää LLM:ää, kuten harjoituksessa, ja testaa sitä erilaisilla kehotteilla varmistaaksesi, että kaikki palvelimen työkalut kutsutaan dynaamisesti. Tällä tavalla rakennettu asiakas tarjoaa lopulliselle käyttäjälle erinomaisen käyttökokemuksen, kun he voivat käyttää kehotteita tarkkojen asiakaskomentojen sijaan ja pysyä tietämättöminä MCP-palvelimen kutsuista.

## Ratkaisu

[Ratkaisu](./solution/README.md)

## Keskeiset opit

- LLM:n lisääminen asiakkaallesi tarjoaa paremman tavan käyttäjille olla vuorovaikutuksessa MCP-palvelinten kanssa.
- Sinun täytyy muuntaa MCP-palvelimen vastaus muotoon, jonka LLM voi ymmärtää.

## Esimerkit

- [Java-laskin](../samples/java/calculator/README.md)
- [.Net-laskin](../../../../03-GettingStarted/samples/csharp)
- [JavaScript-laskin](../samples/javascript/README.md)
- [TypeScript-laskin](../samples/typescript/README.md)
- [Python-laskin](../../../../03-GettingStarted/samples/python)
- [Rust-laskin](../../../../03-GettingStarted/samples/rust)

## Lisäresurssit

## Mitä seuraavaksi

- Seuraavaksi: [Palvelimen käyttö Visual Studio Code -ohjelmalla](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->