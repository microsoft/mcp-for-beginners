# Asiakas LLM:llä

Niin kauan olet nähnyt, miten palvelin ja asiakas luodaan. Asiakas on pystynyt kutsumaan palvelinta eksplisiittisesti listatakseen sen työkalut, resurssit ja kehotteet. Tämä ei kuitenkaan ole kovin käytännöllinen lähestymistapa. Käyttäjäsi elävät toimijuuden aikakaudessa ja odottavat käyttävänsä kehotteita ja kommunikoivansa LLM:n kanssa. He eivät välitä siitä, käytätkö MCP:tä kyvykkyyksiesi tallentamiseen; he odottavat vain luonnollisen kielen kautta tapahtuvaa vuorovaikutusta. Miten ratkaistaan tämä? Ratkaisu on lisätä LLM asiakkaaseen.

## Yleiskatsaus

Tässä oppitunnissa keskitymme LLM:n lisäämiseen asiakkaaseen ja näytämme, miten tämä tarjoaa paljon paremman käyttäjäkokemuksen.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Luoda asiakkaan LLM:n kanssa.
- Kommunikoida saumattomasti MCP-palvelimen kanssa LLM:n avulla.
- Tarjota parempi loppukäyttäjäkokemus asiakaspäässä.

## Lähestymistapa

Yritetään ymmärtää, mitä lähestymistapaa meidän tulee käyttää. LLM:n lisääminen kuulostaa yksinkertaiselta, mutta teemmekö sen tosiasiassa?

Näin asiakas kommunikoi palvelimen kanssa:

1. Muodosta yhteys palvelimeen.

1. Listaa kyvykkyydet, kehotteet, resurssit ja työkalut ja tallenna niiden skeema.

1. Lisää LLM ja välitä tallennetut kyvykkyydet ja niiden skeema muodossa, jonka LLM ymmärtää.

1. Käsittele käyttäjän kehotetta lähettämällä se LLM:lle yhdessä asiakkaan listaamien työkalujen kanssa.

Hienoa, nyt meillä on yleiskuva siitä, miten teemme tämän, kokeillaan tätä seuraavassa harjoituksessa.

## Harjoitus: Asiakas LLM:llä

Tässä harjoituksessa opimme lisäämään LLM:n asiakkaaseemme.

### Todentaminen GitHub Personal Access Tokenilla

GitHub-tokenin luominen on suoraviivainen prosessi. Näin se tehdään:

- Siirry GitHub-asetuksiin – Klikkaa profiilikuvaasi oikeassa yläkulmassa ja valitse Asetukset.
- Siirry kehittäjäasetuksiin – Selaa alas ja klikkaa Kehittäjäasetukset.
- Valitse henkilökohtaiset käyttöoikeustokenit – Klikkaa hienosäädetyt tokenit ja sitten Luo uusi token.
- Määritä token – Lisää viitenote, aseta vanhentumispäivä ja valitse tarvittavat luvat (oikeudet). Tässä tapauksessa varmista, että lisäät Models-oikeuden.
- Luo ja kopioi token – Klikkaa Luo token, ja muista kopioida se välittömästi, koska et näe sitä uudelleen.

### -1- Yhdistä palvelimeen

Luodaan ensin asiakas:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Tuo zod skeeman validointia varten

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
  
Edellä olevassa koodissa olemme:

- Tuoneet tarvittavat kirjastot
- Luoneet luokan, jolla on kaksi jäsentä, `client` ja `openai`, jotka auttavat meitä hallitsemaan asiakasta ja kommunikoimaan LLM:n kanssa.
- Määrittäneet LLM-instanssin käyttämään GitHub-malleja asettamalla `baseUrl` osoittamaan inference-rajapintaan.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Luo palvelimen parametrit stdio-yhteydelle
server_params = StdioServerParameters(
    command="mcp",  # Suoritettava tiedosto
    args=["run", "server.py"],  # Valinnaiset komentoriviparametrit
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
  
Edellä olevassa koodissa olemme:

- Tuoneet tarvittavat MCP-kirjastot
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

Ensiksi sinun tulee lisätä LangChain4j-riippuvuudet `pom.xml`-tiedostoosi. Lisää nämä riippuvuudet MCP-integraation ja GitHub-mallien tuen mahdollistamiseksi:

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
  
Sitten luo Java-asiakasluokkasi:

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
    
    public static void main(String[] args) throws Exception {        // Määritä LLM käyttämään GitHub-malleja
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Luo MCP-siirto palvelimeen yhdistämistä varten
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
}
```
  
Edellä olevassa koodissa olemme:

- **Lisänneet LangChain4j-riippuvuudet**: Vaaditut MCP-integraatiolle, OpenAI:n viralliselle asiakkaalle ja GitHub-mallien tuelle
- **Tuoneet LangChain4j-kirjastot**: MCP-integraatiolle ja OpenAI-chat-mallin toiminnallisuudelle
- **Luoneet `ChatLanguageModel`**: Määritelty käyttämään GitHub-malleja GitHub-tokenillasi
- **Määrittäneet HTTP-siirron**: Käyttäen Server-Sent Events (SSE) MCP-palvelimeen yhdistämiseen
- **Luoneet MCP-asiakkaan**: Joka hoitaa kommunikoinnin palvelimen kanssa
- **Käyttäneet LangChain4j:n sisäänrakennettua MCP-tukea**: Joka yksinkertaistaa LLM:n ja MCP-palvelinten integraatiota

#### Rust

Tässä esimerkissä oletetaan, että sinulla on Rust-pohjainen MCP-palvelin käynnissä. Jos sinulla ei ole sellaista, palaa oppituntiin [01-first-server](../01-first-server/README.md) palvelimen luomiseksi.

Kun Rust MCP -palvelimesi on valmis, avaa terminaali ja siirry samalla hakemistoon kuin palvelin. Suorita sitten seuraava komento uuden LLM-asiakasprojektin luomiseksi:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```
  
Lisää seuraavat riippuvuudet `Cargo.toml` tiedostoosi:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```
  
> [!NOTE]
> Virallista Rust-kirjastoa OpenAI:lle ei ole, mutta `async-openai`-paketti on [yhteisön ylläpitämä kirjasto](https://platform.openai.com/docs/libraries/rust#rust), jota käytetään yleisesti.

Avaa `src/main.rs` tiedosto ja korvaa sen sisältö seuraavalla koodilla:

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

    // TEHTÄVÄ: Hanki MCP-työkaluluettelo

    // TEHTÄVÄ: LLM-keskustelu työkalukutsuilla

    Ok(())
}
```
  
Tämä koodi määrittää perustason Rust-sovelluksen, joka yhdistää MCP-palvelimeen ja GitHub-malleihin LLM-vuorovaikutusta varten.

> [!IMPORTANT]
> Muista asettaa ympäristömuuttuja `OPENAI_API_KEY` GitHub-tokenillasi ennen sovelluksen ajamista.

Hienoa, seuraavaksi listataan palvelimen kyvykkyydet.

### -2- Listaa palvelimen kyvykkyydet

Yhdistetään nyt palvelimeen ja pyydetään sen kyvykkyydet:

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

    // työkalujen listaaminen
    const toolsResult = await this.client.listTools();
}
```
  
Edellä olevassa koodissa olemme:

- Lisänneet koodin yhteyden luomiseksi palvelimeen, `connectToServer`.
- Luoneet `run`-metodin, joka vastaa sovellusvirran hallinnasta. Tähän asti se listaa vain työkalut, mutta pian lisäämme siihen muuta.

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
  
Tässä mitä lisäsimme:

- Listaus resursseista ja työkaluista ja niiden tulostus. Työkaluista myös listataan `inputSchema`, jota käytämme myöhemmin.

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
  
Edellä olevassa koodissa olemme:

- Listanneet työkalut, jotka ovat saatavilla MCP-palvelimella
- Kullekin työkalulle listattu nimi, kuvaus ja sen skeema. Viimeksi mainittu on jotain, jota käytämme työkalujen kutsussa pian.

#### Java

```java
// Luo työkaluntarjoaja, joka löytää MCP-työkalut automaattisesti
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP-työkaluntarjoaja käsittelee automaattisesti:
// - Saatavilla olevien työkalujen listaus MCP-palvelimelta
// - MCP-työkalujen skeemojen muuntaminen LangChain4j-muotoon
// - Työkalun suorituksen ja vastausten hallinta
```
  
Edellä olemme:

- Luoneet `McpToolProvider`in, joka automaattisesti löytää ja rekisteröi kaikki työkalut MCP-palvelimelta
- Työkalutarjoaja hoitaa muunnoksen MCP-työkalujen skeemojen ja LangChain4j:n työkalumuodon välillä sisäisesti
- Tämä lähestymistapa poistaa manuaalisen työkalulistauksen ja muunnosprosessin tarpeen

#### Rust

Työkalujen hakeminen MCP-palvelimelta tehdään `list_tools` -metodilla. Lisää `main`-funktiosi jälkeen, MCP-asiakkaan asetuksen jälkeen, seuraava koodi:

```rust
// Hae MCP-työkaluluettelo
let tools = mcp_client.list_tools(Default::default()).await?;
```
  
### -3- Muunna palvelimen kyvykkyydet LLM-työkaluiksi

Seuraava vaihe palvelimen kyvykkyyksien listaamisen jälkeen on muuntaa ne LLM:n ymmärtämään muotoon. Kun teemme tämän, voimme tarjota nämä kyvykkyydet LLM:n työkaluina.

#### TypeScript

1. Lisää seuraava koodi muuntamaan MCP-palvelimen vastaus työkalumuotoon, jota LLM voi käyttää:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Luo zod-skeema perustuen input_schemaan
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Aseta tyyppi erikseen "function"iksi
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
  
    Ylläoleva koodi ottaa MCP-palvelimen vastauksen ja muuntaa sen työkalumäärittelyksi, jonka LLM ymmärtää.

1. Päivitetään seuraavaksi `run`-metodia, jotta se listaa palvelimen kyvykkyydet:

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
  
    Edellä olemme päivittäneet `run`-metodia käymään tuloksen läpi ja kutsumaan `openAiToolAdapter`:ia jokaiselle merkinnälle.

#### Python

1. Luodaan ensin seuraava muuntajafunktio

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
  
    Funktiossa `convert_to_llm_tools` otamme MCP-työkaluvastauksen ja muunnetaan sen muotoon, jonka LLM ymmärtää.

1. Päivitetään seuraavaksi asiakkaan koodi hyödyntämään tätä funktiota näin:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```
  
    Tässä lisäämme kutsun `convert_to_llm_tool` -funktiolle muuntaaksemme MCP-työkaluvastauksen LLM:lle sopivaksi.

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
  
Edellä olevassa koodissa olemme:

- Luoneet funktion `ConvertFrom`, joka ottaa nimen, kuvauksen ja syötteen skeeman.
- Määritelleet toiminnallisuuden, joka luo `FunctionDefinition`in, joka välitetään `ChatCompletionsDefinition`:lle, ja jälkimmäinen on jotain, mitä LLM ymmärtää.

1. Päivitetään jotakin olemassaolevaa koodia hyödyntämään tätä funktiota:

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
  
Edellä olemme:

- Määritelleet yksinkertaisen `Bot`-rajapinnan luonnollisen kielen vuorovaikutukselle
- Käyttäneet LangChain4j:n `AiServices`-luokkaa sitomaan LLM ja MCP-työkalutarjoaja automaattisesti yhteen
- Kehys hoitaa automaattisesti työkaluskeeman muunnoksen ja toiminnan kutsut kulissien takana
- Tämä lähestymistapa poistaa manuaalisen työkalumuunnoksen - LangChain4j hoitaa kaiken monimutkaisuuden MCP-työkalujen muuntamisessa LLM-yhteensopivaan muotoon

#### Rust

Muutamme MCP-työkaluvastauksen LLM:n ymmärtämään muotoon lisäämällä apufunktion, joka muotoilee työkalulistan. Lisää seuraava koodi `main.rs` -tiedostoon `main`-funktion alle. Tätä kutsutaan, kun teemme pyyntöjä LLM:lle:

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
  
Hienoa, olemme valmiit käsittelemään käyttäjän pyyntöjä, joten otetaan se seuraavaksi.

### -4- Käsittele käyttäjän pyyntö

Tässä osassa käsittelemme käyttäjän pyyntöjä.

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

        // 3. Tee jotain tuloksen kanssa
        // TEHTÄVÄ

        }
    }
    ```
  
    Edellä olemme:

    - Lisänneet metodin `callTools`.
    - Metodi ottaa LLM:n vastauksen ja tarkistaa, mitkä työkalut on kutsuttu, jos yhtään:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // kutsu työkalu
        }
        ```
  
    - Kutsuu työkalua, jos LLM osoittaa, että sitä pitäisi kutsua:

        ```typescript
        // 2. Kutsu palvelimen työkalua
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tee jotain tuloksen kanssa
        // TEE
        ```
  
1. Päivitä `run`-metodi mukaan lukien LLM-kutsut ja `callTools`:

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

    // 3. Käy läpi LLM:n vastaus, tarkista jokaisen valinnan osalta, onko siinä työkalukutsuja
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
import { z } from "zod"; // Tuo zod skeeman validointiin

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // saatamme joutua muuttamaan tähän url:iin tulevaisuudessa: https://models.github.ai/inference
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
          // Luo zod skeema input_schema:n perusteella
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Aseta tyyppi nimenomaan "function"
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
    
          // 3. Tee jotain tuloksen kanssa
          // TEHTÄVÄNÄ
    
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
    
        // 1. Käy läpi LLM vastaus, jokaiselle vaihtoehdolle tarkista onko siinä työkalukutsuja
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

1. Lisätään joitakin tuontilausuntoja LLM:n kutsumista varten

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```
  
1. Lisää funktio, joka kutsuu LLM:ää:

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
  
    Edellä olemme:

    - Välittäneet funktiot, jotka löysimme MCP-palvelimelta ja muunsimme, LLM:lle.
    - Kutsuneet LLM:ää kyseisillä funktioilla.
    - Tarkastelleet tulosta nähdäkseni, mitä funktioita pitäisi kutsua, jos yhtään.
    - Lopuksi välitämme luettelon kutsuttavista funktioista.

1. Päivitetään lopuksi pääkoodimme:

    ```python
    prompt = "Add 2 to 20"

    # kysy LLM:ltä, mitä työkaluja käyttää, jos käytettävissä
    functions_to_call = call_llm(prompt, functions)

    # kutsu ehdotettuja toimintoja
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```
  
    Siinä on viimeinen vaihe, missä:

    - Kutsumme MCP-työkalua `call_tool`-metodilla käyttäen funktiota, jonka LLM katsoi kutsuttavan promptimme perusteella.
    - Tulostamme työkalukutsun tuloksen MCP-palvelimelle.

#### .NET

1. Näytetään koodi LLM:n kehotteen käsittelyyn:

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
  
    Edellä olemme:

    - Hain työkalut MCP-palvelimelta, `var tools = await GetMcpTools()`.
    - Määritin käyttäjän kehotteen `userMessage`.
    - Rakensin optio-olion, joka määrittää mallin ja työkalut.
    - Tein pyynnön LLM:lle.

1. Vielä yksi vaihe: katsotaan, jos LLM katsoo meidän kutsuvan funktiota:

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
  
    Edellä olemme:

    - Kiertäneet läpi funktiokutsut.
    - Jokaiselle työkalukutsulle purimme nimen ja argumentit ja kutsuimme työkalua MCP-palvelimella MCP-asiakkaan avulla. Lopuksi tulostimme tulokset.

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

// 5. Print the generic response
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
  
Edellä olemme:

- Käyttäneet yksinkertaisia luonnollisen kielen kehotteita kommunikoidessamme MCP-palvelimen työkalujen kanssa
- LangChain4j-kehys hoitaa automaattisesti:
  - Käyttäjäkehotteiden muunnon työkalukutsuiksi tarvittaessa
  - Oikeiden MCP-työkalujen kutsumisen LLM:n päätöksen mukaan
  - Keskustelun hallinnan LLM:n ja MCP-palvelimen välillä
- `bot.chat()` metodi palauttaa luonnollisen kielen vastauksia, jotka voivat sisältää MCP-työkaluista saatuja tuloksia
- Tämä lähestymistapa tarjoaa saumattoman käyttäjäkokemuksen, jossa käyttäjien ei tarvitse tietää MCP:n taustalla olevasta toteutuksesta

Täydellinen koodiesimerkki:

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

Suurin osa työstä tapahtuu tässä. Kutsumme LLM:ää alkuperäisellä käyttäjäkehotteella, sitten käsittelemme vastauksen katsoaksemme, tarvitseeko kutsua työkaluja. Jos tarvitsee, kutsumme ne työkalut ja jatkamme keskustelua LLM:n kanssa, kunnes muita työkalukutsuja ei tarvita ja saamme lopullisen vastauksen.

Teemme useita LLM-kutsuja, joten määritellään funktio, joka hoitaa LLM-kutsun. Lisää seuraava funktio `main.rs` tiedostoon:

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
  
Tämä funktio ottaa LLM-asiakkaan, viestilistan (sisältäen käyttäjän kehotteen), MCP-palvelimen työkalut, ja lähettää pyynnön LLM:lle palauttaen vastauksen.
LLM:n vastaus sisältää taulukon `choices`. Meidän täytyy käsitellä tulos nähdäksesi, onko `tool_calls`-kohteita. Tämä antaa meille tiedon, että LLM pyytää tietyn työkalun kutsumista argumenttien kanssa. Lisää seuraava koodi `main.rs`-tiedostosi loppuun määritelläksesi funktion, joka käsittelee LLM-vastauksen:

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

    // Käsittele työkalukutsut
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

        // Jatka keskustelua työkalun tuloksilla
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
  
Jos `tool_calls` ovat läsnä, se poimii työkalutiedot, kutsuu MCP-palvelinta työkalupyynnöllä ja lisää tulokset keskustelun viesteihin. Sen jälkeen keskustelu jatkuu LLM:n kanssa, ja viestit päivitetään assistentin vastauksella ja työkalukutsujen tuloksilla.

Työkalukutsun tietojen poimimiseksi, jotka LLM palauttaa MCP-kutsuja varten, lisäämme toisen apufunktion, joka poimii kaiken tarvittavan kutsun tekemiseksi. Lisää seuraava koodi `main.rs`-tiedostosi loppuun:

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
  
Kun kaikki osat ovat paikoillaan, voimme nyt käsitellä alkuperäisen käyttäjän kehotteen ja kutsua LLM:ää. Päivitä `main`-funktiosi sisältämään seuraava koodi:

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
  
Tämä kysyy LLM:ltä alkuperäisen käyttäjän kehotteen, missä pyydetään kahden numeron summaa, ja käsittelee vastauksen dynaamisesti työkalukutsujen hallitsemiseksi.

Hienoa, sait sen tehtyä!

## Tehtävä

Ota harjoituskoodisi ja laajenna palvelin useammilla työkaluilla. Luo sitten asiakas, jossa on LLM, kuten harjoituksessa, ja testaa sitä erilaisilla kehotteilla varmistaaksesi, että kaikki palvelimesi työkalut kutsutaan dynaamisesti. Tällä tavalla asiakas tarjoaa loppukäyttäjälle loistavan käyttökokemuksen, koska he pystyvät käyttämään kehotteita tarkkojen asiakas-komentojen sijaan eikä heidän tarvitse tietää MCP-palvelimen kutsuista.

## Ratkaisu

[Solution](./solution/README.md)

## Tärkeimmät opit

- LLM:n lisääminen asiakkaaseesi tarjoaa paremman tavan käyttäjille olla vuorovaikutuksessa MCP-palvelimien kanssa.  
- Sinun täytyy muuntaa MCP-palvelimen vastaus muotoon, jonka LLM pystyy ymmärtämään.

## Esimerkkejä

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)  

## Lisäresurssit

## Mitä seuraavaksi

- Seuraavaksi: [Palvelimen käyttäminen Visual Studio Codella](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulisi pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ota vastuuta tästä käännöksestä aiheutuvista mahdollisista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->