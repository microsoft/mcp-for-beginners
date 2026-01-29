# Asiakkaan luominen LLM:llä

Tähän asti olet nähnyt, miten luodaan palvelin ja asiakas. Asiakas on pystynyt kutsumaan palvelinta eksplisiittisesti listatakseen sen työkalut, resurssit ja kehotteet. Tämä ei kuitenkaan ole kovin käytännöllinen lähestymistapa. Käyttäjäsi elää agenttisessa aikakaudessa ja odottaa käyttävänsä kehotteita ja kommunikoivansa LLM:n kanssa. Käyttäjäsi ei välitä siitä, käytätkö MCP:tä kykyjesi tallentamiseen, mutta he odottavat käyttävänsä luonnollista kieltä vuorovaikutukseen. Miten ratkaistaan tämä? Ratkaisu on lisätä LLM asiakkaaseen.

## Yleiskatsaus

Tässä oppitunnissa keskitymme LLM:n lisäämiseen asiakkaaseen ja näytämme, miten tämä tarjoaa paljon paremman käyttökokemuksen käyttäjällesi.

## Oppimistavoitteet

Oppitunnin lopussa osaat:

- Luoda asiakkaan, jossa on LLM.
- Vuorovaikuttaa saumattomasti MCP-palvelimen kanssa LLM:n avulla.
- Tarjota parempi loppukäyttäjäkokemus asiakaspuolella.

## Lähestymistapa

Yritetään ymmärtää, millainen lähestymistapa meidän täytyy ottaa. LLM:n lisääminen kuulostaa yksinkertaiselta, mutta teemmekö sen oikeasti?

Näin asiakas vuorovaikuttaa palvelimen kanssa:

1. Yhdistä palvelimeen.

1. Listaa kyvyt, kehotteet, resurssit ja työkalut, ja tallenna niiden skeema.

1. Lisää LLM ja anna tallennetut kyvyt ja niiden skeema muodossa, jonka LLM ymmärtää.

1. Käsittele käyttäjän kehotetta välittämällä se LLM:lle yhdessä asiakkaan listaamien työkalujen kanssa.

Hienoa, nyt kun ymmärrämme tämän korkean tason, kokeillaan alla olevassa harjoituksessa.

## Harjoitus: Asiakkaan luominen LLM:llä

Tässä harjoituksessa opimme lisäämään LLM:n asiakkaaseemme.

### Todennus GitHub Personal Access Tokenilla

GitHub-tokenin luominen on suoraviivainen prosessi. Näin teet sen:

- Mene GitHubin asetuksiin – Klikkaa profiilikuvaasi oikeassa yläkulmassa ja valitse Settings.
- Siirry Developer Settings -kohtaan – Selaa alas ja klikkaa Developer Settings.
- Valitse Personal Access Tokens – Klikkaa Fine-grained tokens ja sitten Generate new token.
- Määritä tokenisi – Lisää muistiinpano viitteeksi, aseta vanhenemispäivä ja valitse tarvittavat oikeudet (scopes). Tässä tapauksessa varmista, että lisäät Models-oikeuden.
- Luo ja kopioi token – Klikkaa Generate token ja kopioi se heti, sillä et näe sitä uudelleen.

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

Edellisessä koodissa olemme:

- Tuoneet tarvittavat kirjastot
- Luoneet luokan, jossa on kaksi jäsentä, `client` ja `openai`, jotka auttavat hallitsemaan asiakasta ja vuorovaikuttamaan LLM:n kanssa.
- Konfiguroineet LLM-instanssin käyttämään GitHub-malleja asettamalla `baseUrl` osoittamaan inference API:iin.

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

Ensiksi sinun täytyy lisätä LangChain4j-riippuvuudet `pom.xml`-tiedostoosi. Lisää nämä riippuvuudet MCP-integraation ja GitHub-mallien tuen mahdollistamiseksi:

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

Edellisessä koodissa olemme:

- **Lisänneet LangChain4j-riippuvuudet**: Tarvitaan MCP-integraatioon, OpenAI:n viralliseen asiakkaaseen ja GitHub-mallien tukeen
- **Tuoneet LangChain4j-kirjastot**: MCP-integraatiota ja OpenAI-chat-mallin toiminnallisuutta varten
- **Luoneet `ChatLanguageModel`-instanssin**: Konfiguroitu käyttämään GitHub-malleja GitHub-tokenillasi
- **Asettaneet HTTP-siirron**: Käyttäen Server-Sent Events (SSE) MCP-palvelimeen yhdistämiseen
- **Luoneet MCP-asiakkaan**: Joka hoitaa kommunikoinnin palvelimen kanssa
- **Käyttäneet LangChain4j:n sisäänrakennettua MCP-tukea**: Joka yksinkertaistaa LLM:ien ja MCP-palvelimien integraatiota

#### Rust

Tämä esimerkki olettaa, että sinulla on Rust-pohjainen MCP-palvelin käynnissä. Jos sinulla ei ole sellaista, palaa [01-first-server](../01-first-server/README.md) -oppitunnille palvelimen luomiseksi.

Kun sinulla on Rust MCP -palvelin, avaa terminaali ja siirry samaan hakemistoon palvelimen kanssa. Suorita sitten seuraava komento luodaksesi uuden LLM-asiakasprojektin:

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
> Virallista Rust-kirjastoa OpenAI:lle ei ole, mutta `async-openai`-paketti on [yhteisön ylläpitämä kirjasto](https://platform.openai.com/docs/libraries/rust#rust), jota käytetään yleisesti.

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

    // TODO: LLM-keskustelu työkalukutsujen kanssa

    Ok(())
}
```

Tämä koodi luo perus Rust-sovelluksen, joka yhdistyy MCP-palvelimeen ja GitHub-malleihin LLM-vuorovaikutuksia varten.

> [!IMPORTANT]
> Muista asettaa `OPENAI_API_KEY`-ympäristömuuttuja GitHub-tokenillasi ennen sovelluksen suorittamista.

Hienoa, seuraavaksi listataan palvelimen kyvyt.

### -2- Listaa palvelimen kyvyt

Yhdistetään nyt palvelimeen ja kysytään sen kyvyt:

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

Edellisessä koodissa olemme:

- Lisänneet koodin palvelimeen yhdistämiseen, `connectToServer`.
- Luoneet `run`-metodin, joka vastaa sovelluksen kulun hallinnasta. Tähän asti se listaa vain työkalut, mutta lisäämme siihen pian lisää.

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

- Listasimme resurssit ja työkalut ja tulostimme ne. Työkaluista listaamme myös `inputSchema`-tiedot, joita käytämme myöhemmin.

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

- Listanneet MCP-palvelimen käytettävissä olevat työkalut
- Jokaiselle työkalulle listanneet nimen, kuvauksen ja sen skeeman. Tätä skeemaa käytämme pian työkalujen kutsumiseen.

#### Java

```java
// Luo työkaluntarjoaja, joka löytää MCP-työkalut automaattisesti
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP-työkaluntarjoaja hoitaa automaattisesti:
// - Saatavilla olevien työkalujen listaamisen MCP-palvelimelta
// - MCP-työkalujen skeemojen muuntamisen LangChain4j-muotoon
// - Työkalujen suorittamisen ja vastausten hallinnan
```

Edellisessä koodissa olemme:

- Luoneet `McpToolProvider`-luokan, joka automaattisesti löytää ja rekisteröi kaikki MCP-palvelimen työkalut
- Työkaluntarjoaja hoitaa MCP-työkalujen skeemojen ja LangChain4j:n työkalumuodon välisen muunnoksen sisäisesti
- Tämä lähestymistapa abstrahoi manuaalisen työkalulistauksen ja muunnoksen prosessin

#### Rust

Työkalujen hakeminen MCP-palvelimelta tehdään `list_tools`-metodilla. Lisää `main`-funktiosi jälkeen seuraava koodi:

```rust
// Hae MCP-työkaluluettelo
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Muunna palvelimen kyvyt LLM-työkaluiksi

Seuraava askel palvelimen kykyjen listaamisen jälkeen on muuntaa ne LLM:n ymmärtämään muotoon. Kun teemme tämän, voimme tarjota nämä kyvyt työkaluina LLM:lle.

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
            type: "function" as const, // Aseta tyyppi nimenomaisesti "function"iksi
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

1. Päivitetään seuraavaksi `run`-metodi listaamaan palvelimen kyvyt:

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

    Edellisessä koodissa päivitimme `run`-metodin käymään läpi tuloksen ja kutsumaan `openAiToolAdapter`-funktiota jokaiselle merkinnälle.

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

    Funktiossa `convert_to_llm_tools` otamme MCP-työkaluvastauksen ja muunnamme sen LLM:n ymmärtämään muotoon.

1. Päivitetään sitten asiakaskoodimme käyttämään tätä funktiota näin:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Tässä lisäämme kutsun `convert_to_llm_tool`-funktioon muuntaaksemme MCP-työkaluvastauksen muotoon, jonka voimme syöttää LLM:lle myöhemmin.

#### .NET

1. Lisätään koodi, joka muuntaa MCP-työkaluvastauksen LLM:n ymmärtämään muotoon

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

- Luoneet funktion `ConvertFrom`, joka ottaa nimen, kuvauksen ja syötteen skeeman.
- Määritelleet toiminnallisuuden, joka luo FunctionDefinitionin, joka välitetään ChatCompletionsDefinitionille. Tämä jälkimmäinen on LLM:n ymmärtämä.

1. Päivitetään olemassa olevaa koodia hyödyntämään tätä funktiota:

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
// Luo bottirajapinta luonnollisen kielen vuorovaikutukseen
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
- Käyttäneet LangChain4j:n `AiServices`-luokkaa sitomaan LLM automaattisesti MCP-työkaluntarjoajaan
- Kehys hoitaa automaattisesti työkaluskeeman muunnoksen ja funktiokutsut taustalla
- Tämä lähestymistapa poistaa manuaalisen työkalumuunnoksen tarpeen – LangChain4j hoitaa kaiken MCP-työkalujen muuntamisen LLM-yhteensopivaan muotoon

#### Rust

Muuntaaksemme MCP-työkaluvastauksen LLM:n ymmärtämään muotoon lisäämme apufunktion, joka muotoilee työkalulistan. Lisää seuraava koodi `main.rs`-tiedostoosi `main`-funktion alapuolelle. Tätä kutsutaan, kun tehdään pyyntöjä LLM:lle:

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

Hienoa, olemme valmiita käsittelemään käyttäjän pyyntöjä, joten siirrytään siihen.

### -4- Käsittele käyttäjän kehotepyyntö

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

    - Kutsuu työkalua, jos LLM osoittaa, että sitä pitäisi kutsua:

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

1. Päivitä `run`-metodi sisällyttämään LLM:n kutsut ja `callTools`-metodin kutsut:

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

    // 2. Kutsu LLM:ää
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
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
            baseURL: "https://models.inference.ai.azure.com", // saatetaan tarvita muuttaa tähän URL-osoitteeseen tulevaisuudessa: https://models.github.ai/inference
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
            type: "function" as const, // Aseta tyyppi eksplisiittisesti "function"
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Käy läpi LLM-vastaus, tarkista jokaisesta valinnasta, onko siinä työkalukutsuja
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
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Lisätään funktio, joka kutsuu LLM:n:

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
    - Kutsuneet LLM:ää näillä funktioilla.
    - Tarkastelleet tulosta nähdäksesi, mitä funktioita pitäisi kutsua, jos yhtään.
    - Lopuksi välitämme listan kutsuttavista funktioista.

1. Viimeinen askel, päivitetään pääkoodimme:

    ```python
    prompt = "Add 2 to 20"

    # kysy LLM:ltä, mitä työkaluja käyttää, jos lainkaan
    functions_to_call = call_llm(prompt, functions)

    # kutsu ehdotettuja funktioita
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Siinä se, viimeisessä vaiheessa olemme:

    - Kutsuneet MCP-työkalua `call_tool`-funktiolla käyttäen LLM:n ehdottamaa funktiota kehotteemme perusteella.
    - Tulostaneet työkalukutsun tuloksen MCP-palvelimelle.

#### .NET

1. Näytetään koodi LLM-kehotepyynnön tekemiseen:

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

    Edellisessä koodissa olemme:

    - Hainneet työkalut MCP-palvelimelta, `var tools = await GetMcpTools()`.
    - Määritelleet käyttäjän kehotteen `userMessage`.
    - Rakentaneet options-objektin, jossa määritellään malli ja työkalut.
    - Tehty pyyntö LLM:lle.

1. Vielä yksi askel, katsotaan, jos LLM ehdottaa funktiokutsua:

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
    - Jokaiselle työkalukutsulle purkaneet nimen ja argumentit ja kutsuneet työkalua MCP-palvelimella MCP-asiakkaan avulla. Lopuksi tulostamme tulokset.

Tässä koko koodi:

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
  - Oikeiden MCP-työkalujen kutsumisen LLM:n päätöksen perusteella
  - Keskustelun hallinnan LLM:n ja MCP-palvelimen välillä
- `bot.chat()`-metodi palauttaa luonnollisen kielen vastauksia, jotka voivat sisältää MCP-työkalujen suoritustuloksia
- Tämä lähestymistapa tarjoaa saumattoman käyttökokemuksen, jossa käyttäjien ei tarvitse tietää taustalla olevasta MCP-toteutuksesta

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

Tässä tapahtuu suurin osa työstä. Kutsumme LLM:ää alkuperäisellä käyttäjän kehotteella, sitten käsittelemme vastauksen nähdäksesi, tarvitseeko työkaluja kutsua. Jos tarvitsee, kutsumme ne ja jatkamme keskustelua LLM:n kanssa, kunnes työkaluja ei enää tarvitse kutsua ja saamme lopullisen vastauksen.

Teemme useita LLM-kutsuja, joten määritellään funktio, joka hoitaa LLM-kutsun. Lisää seuraava funktio `main.rs`-tiedostoosi:

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

Tämä funktio ottaa LLM-asiakkaan, viestilistan (sisältäen käyttäjän kehotteen), MCP-palvelimen työkalut ja lähettää pyynnön LLM:lle, palauttaen vastauksen.
LLM:n vastaus sisältää taulukon `choices`. Meidän täytyy käsitellä tulos nähdäksesi, onko siellä `tool_calls`-kohteita. Tämä kertoo meille, että LLM pyytää tietyn työkalun kutsumista argumenteilla. Lisää seuraava koodi `main.rs`-tiedostosi loppuun määritelläksesi funktion, joka käsittelee LLM-vastauksen:

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

Jos `tool_calls` ovat läsnä, se poimii työkalutiedot, kutsuu MCP-palvelinta työkalupyyntöjen kanssa ja lisää tulokset keskustelun viesteihin. Sen jälkeen keskustelu jatkuu LLM:n kanssa ja viestit päivitetään avustajan vastauksella ja työkalukutsujen tuloksilla.

Poimiaksemme työkalukutsutiedot, jotka LLM palauttaa MCP-kutsuja varten, lisäämme toisen apufunktion, joka poimii kaiken tarvittavan kutsun tekemiseen. Lisää seuraava koodi `main.rs`-tiedostosi loppuun:

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

Kun kaikki osat ovat paikallaan, voimme nyt käsitellä alkuperäisen käyttäjän kehotteen ja kutsua LLM:ää. Päivitä `main`-funktiosi sisältämään seuraava koodi:

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

Tämä kysyy LLM:ltä alkuperäisen käyttäjän kehotteen, jossa pyydetään kahden luvun summaa, ja käsittelee vastauksen dynaamisesti työkalukutsujen hallitsemiseksi.

Hienoa, onnistuit!

## Tehtävä

Ota harjoituksesta koodi ja rakenna palvelin, jossa on lisää työkaluja. Luo sitten asiakas, jossa on LLM, kuten harjoituksessa, ja testaa sitä eri kehotteilla varmistaaksesi, että kaikki palvelimesi työkalut kutsutaan dynaamisesti. Tällä tavalla rakennettu asiakas tarjoaa loppukäyttäjälle erinomaisen käyttökokemuksen, koska he voivat käyttää kehotteita tarkkojen asiakaskomentojen sijaan eivätkä huomaa MCP-palvelimen kutsuja.

## Ratkaisu

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## Tärkeimmät opit

- LLM:n lisääminen asiakkaaseesi tarjoaa paremman tavan käyttäjien vuorovaikutukseen MCP-palvelimien kanssa.
- Sinun täytyy muuntaa MCP-palvelimen vastaus muotoon, jonka LLM ymmärtää.

## Esimerkit

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Lisäresurssit

## Mitä seuraavaksi

- Seuraava: [Palvelimen käyttäminen Visual Studio Codella](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->