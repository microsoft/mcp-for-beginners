# Kliendi loomine LLM-iga

> [!NOTE]
> Java kliendi näited ühenduvad pärandi HTTP+SSE transpordi kaudu ja
> sihivad MCP `2025-11-25` SDK API-sid. Uute kaugsuhtluskliendi jaoks kasutage `2026-07-28` ühilduvat SDK-d ja
> voogedastatavat HTTP-d.

Seni olete näinud, kuidas luua server ja klient. Klient on suutnud serverit eksplitsiitselt kutsuda, et kuvada selle tööriistu, ressursse ja päringuid. Kuid see ei ole väga praktiline lähenemine. Teie kasutajad elavad agendiajastul ja ootavad, et saaksid kasutada päringuid ja suhelda LLM-iga. Neid ei huvita, kas kasutate MCP-d oma võimekuste salvestamiseks; nad lihtsalt ootavad suhtlust loomulikus keeles. Kuidas seda siis lahendada? Lahenduseks on lisada LLM kliendile.

## Ülevaade

Selles õppetükis keskendume kliendi täiendamisele LLM-iga ja näitame, kuidas see kasutajakogemust oluliselt parandab.

## Õpieesmärgid

Selle õppetüki lõpuks oskate:

- Luua klient LLM-iga.
- Sujuvalt suhelda MCP serveriga LLM-i kaudu.
- Pakkuda kliendi poolel paremat lõppkasutajakogemust.

## Lähenemine

Proovime mõista, millist lähenemist me peaksime kasutama. LLM-i lisamine tundub lihtne, aga kas me seda ka teeme?

Kuidas klient serveriga suhtleb:

1. Loob ühenduse serveriga.

1. Loendab võimekused, päringud, ressursid ja tööriistad ning salvestab nende skeemi.

1. Lisab LLM-i ja edastab salvestatud võimekused ja nende skeemi formaadis, mida LLM mõistab.

1. Töötleb kasutajapäringu, edastades selle LLM-ile koos kliendi poolt loetletud tööriistadega.

Suurepärane, nüüd kui mõistame seda kõrgel tasemel, proovime järgmist harjutust.

## Harjutus: kliendi loomine LLM-iga

Selles harjutuses õpime lisama meie kliendile LLM-i.

### Autentimine GitHub isikliku juurdepääsu tokeniga

GitHubi tokeni loomine on lihtne protsess. Siin on, kuidas seda teha:

- Minge GitHubi seadistustesse – klõpsake paremas ülanurgas oma profiilipildil ja valige Settings.
- Navigeerige arendajate seadistustesse – kerige alla ja klõpsake Developer Settings.
- Valige isiklikud juurdepääsu tokenid – klõpsake Fine-grained tokens ja seejärel Generate new token.
- Konfigureerige token – lisage märkusi, määrake aegumiskuupäev ja valige vajalikud õigused. Veenduge, et lisate Models loa.
- Looge ja kopeerige token – klõpsake Generate token ning kopeerige see kohe, kuna hiljem seda enam näha ei saa.

### -1- Ühenduse loomine serveriga

Loome esmalt oma kliendi:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Impordi zod skeemi valideerimiseks

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

Eelnevas koodis me:

- Impordisime vajalikud teegid
- Loodud klassi kahe liikmega, `client` ja `openai`, mis aitavad meil hallata klienti ja suhelda LLM-iga.
- Konfigureerisime oma LLM-i instantsi kasutama GitHubi mudeleid, määrates `baseUrl` osutamaks inference API-le.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Loo serveri parameetrid stdio ühenduseks
server_params = StdioServerParameters(
    command="mcp",  # Käivitatav fail
    args=["run", "server.py"],  # Valikulised käsurea argumendid
    env=None,  # Valikulised keskkonnamuutujad
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Alusta ühendust
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Eelnevas koodis me:

- Impordisime MCP jaoks vajalikke teeke
- Lõime kliendi

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

Esmalt peate lisama LangChain4j sõltuvused oma `pom.xml` faili. Lisage need sõltuvused MCP integratsiooni ja OpenAI-ga ühilduva MiniMax API võimaldamiseks:

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

Määrake oma MiniMax API võti ja valikuliselt lõpp-punkt ja mudel.
`MINIMAX_MODEL_ID` toetab `MiniMax-M3` ja `MiniMax-M2.7`. Kui
`OPENAI_BASE_URL` pole seadistatud, toetab `MINIMAX_REGION` regioone `global_en` ja `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Kui soovite valida lõpp-punkti piirkonna järgi, jätke `OPENAI_BASE_URL` välja:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Seejärel looge oma Java kliendiklasse:

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

        // Loo MCP transport serveriga ühendamiseks
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Loo MCP klient
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

Eelnevas koodis me:

- **Lisasime LangChain4j sõltuvused**: vajalik MCP integratsiooniks ja OpenAI-ga ühilduva MiniMax API jaoks
- **Impordisime LangChain4j teegid**: MCP integratsiooniks ja OpenAI chat-mudeli funktsionaalsuseks
- **Lõime `ChatLanguageModel`**: konfigureeritud MiniMax kasutamiseks teie MiniMax API võtme, lõpp-punkti ja toetatud mudeli ID-ga
- **Seadistasime HTTP transpordi**: kasutades Server-Sent Events (SSE) MCP serveriga ühenduse loomiseks
- **Lõime MCP kliendi**: mis haldab suhtlust serveriga
- **Kasutasime LangChain4j sisseehitatud MCP tuge**: mis lihtsustab LLM-ide ja MCP serverite integratsiooni

#### Rust

See näide eeldab, et teil töötab Rust-põhine MCP server. Kui seda pole, vaadake tagasi [01-esimene-server](../01-first-server/README.md) õppetüki, et server luua.

Kui teil on Rust MCP server, avage terminal ja minge samasse kataloogi, kus server asub. Seejärel käivitage järgmine käsk, et luua uus LLM kliendiprojekt:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Lisage oma `Cargo.toml` faili järgmised sõltuvused:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Rusti jaoks pole ametlikku OpenAI teeki, kuid `async-openai` crate on [kogukonna hooldatav teek](https://platform.openai.com/docs/libraries/rust#rust), mida sageli kasutatakse.

Avage fail `src/main.rs` ja asendage selle sisu järgmise koodiga:

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
    // Algne sõnum
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI kliendi seadistamine
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP kliendi seadistamine
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

    // TODO: Hangi MCP tööriistade nimekiri

    // TODO: LLM vestlus tööriistakõnede abil

    Ok(())
}
```

See kood seadistab lihtsa Rusti rakenduse, mis loob ühenduse MCP serveri ja GitHubi mudelitega LLM-i suhtluseks.

> [!IMPORTANT]
> Enne rakenduse käivitamist seadke kindlasti keskkonnamuutujaks `OPENAI_API_KEY` oma GitHubi token.

Suurepärane, järgmise sammuna loetleme serveri võimekused.

### -2- Serveri võimekuste loetelu

Nüüd ühendume serveriga ja küsime selle võimekusi:

#### Typescript

Sama klassi lisage järgmised meetodid:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // tööriistade nimekiri
    const toolsResult = await this.client.listTools();
}
```

Eelnevas koodis me:

- Lisatud serveriga ühenduse loomise kood, `connectToServer`.
- Loodud `run` meetod, mis haldab rakenduse voogu. Tähendab praegu tööriistade loetelu, kuid lisame sellega peagi rohkem.

#### Python

```python
# Loetle saadaolevad ressursid
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Loetle saadaolevad tööriistad
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Lisasime:

- Ressursside ja tööriistade loetelu ning nende printimise. Tööriistade puhul loetleme ka `inputSchema`, mida kasutame hiljem.

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


Eelnevas koodis oleme:

- Loetlenud MCP serveris saadavalolevad tööriistad
- Iga tööriista kohta loetlenud nime, kirjelduse ja selle skeemi. Viimane on midagi, mida me peagi tööriistade kutsumiseks kasutame.

#### Java

```java
// Loo tööriistapakkuja, mis automaatselt avastab MCP tööriistad
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP tööriistapakkuja haldab automaatselt:
// - Saadaval olevate tööriistade nimekirja koostamine MCP serverist
// - MCP tööriistade skeemide konverteerimine LangChain4j formaati
// - Tööriistade täitmise ja vastuste haldamine
```

Eelnevas koodis oleme:

- Loonud `McpToolProvider`, mis automaatselt avastab ja registreerib kõik tööriistad MCP serverist
- Tööriistade pakkuja käsitleb MCP tööriistade skeemide ja LangChain4j tööriistavormingu vahelise teisenduse sisemiselt
- See lähenemine abstraktiseerib käsitsi tööriistade nimekirja koostamise ja teisendamise protsessi

#### Rust

MCP serverist tööriistade pärimine toimub meetodi `list_tools` abil. Oma `main` funktsioonis, pärast MCP kliendi seadistamist, lisa järgmine kood:

```rust
// Hangi MCP tööriistade loend
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Muudame serveri võimed LLM tööriistadeks

Järgmine samm pärast serverivõimete loetlemist on nende teisendamine LLM-i arusaadavas vormis. Kui me selle teeme, saame neid võimeid pakkuda tööriistadena oma LLM-ile.

#### TypeScript

1. Lisa järgmine kood MCP serveri vastuse teisendamiseks tööriistavormingusse, mida LLM saab kasutada:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Loo zod skeem sisendskeemi põhjal
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Sea tüüp selgelt "function"
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

    Ülaltoodud kood võtab MCP serveri vastuse ja teisendab selle tööriistade definitsiooni vormingusse, mida LLM suudab mõista.

2. Uuendame järgmise sammuna meetodit `run`, et loetleda serveri võimeid:

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

    Eelnevas koodis oleme uuendanud `run` meetodit, et tulemust läbi käia ja iga kirje jaoks kutsuda `openAiToolAdapter`.

#### Python

1. Alustuseks loome järgmise teisendustöö funktsiooni

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

    Ülaltoodud funktsioonis `convert_to_llm_tools` võtame MCP tööriista vastuse ja teisendame selle LLM-i arusaadavasse vormingusse.

2. Järgmiseks uuendame meie kliendikoodi, et kasutada seda funktsiooni nii:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Siin lisame `convert_to_llm_tool` kõne, mis teisendab MCP tööriista vastuse millekski, mida saame hiljem LLM-ile ette anda.

#### .NET

1. Lisame koodi, mis teisendab MCP tööriista vastuse millekski, mida LLM mõistab

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

Eelnevas koodis oleme:

- Loonud funktsiooni `ConvertFrom`, mis võtab nime, kirjelduse ja sisendi skeemi.
- Määratlenud funktsionaalsuse, mis loob `FunctionDefinition`, mis antakse üle `ChatCompletionsDefinition-ile`. Viimane on see, mida LLM suudab mõista.

2. Vaatame, kuidas saame olemasolevat koodi selle ülalmainitud funktsiooni abil uuendada:

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
// Loo botiliides loomuliku keele interaktsiooniks
public interface Bot {
    String chat(String prompt);
}

// Konfigureeri tehisintellekti teenus LLM-i ja MCP tööriistadega
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Eelnevas koodis oleme:

- Määratlenud lihtsa `Bot` liidese loomuliku keele interaktsioonide jaoks
- Kasutanud LangChain4j `AiServices`, mis automaatselt seob LLM-i MCP tööriistade pakkujaga
- Raamistik haldab automaatselt tööriistade skeemide teisendust ja funktsioonikõnesid taga
- See lähenemine välistab käsitsi tööriistade teisendamise – LangChain4j haldab kogu keerukust MCP tööriistade teisendamisel LLM-i jaoks sobivasse vormingusse

#### Rust

MCP tööriista vastuse teisendamiseks LLM-i arusaadavasse vormingusse lisame abi funktsiooni, mis vormindab tööriistade nimekirja. Lisa järgmine kood `main.rs` faili alla `main` funktsiooni. Seda kutsutakse, kui tehakse päringuid LLM-ile:

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

Suurepärane, oleme valmis kasutajapäringute käsitlemiseks, lähme sellele järgmisena kallale.

### -4- Kasutajapäringute käsitlemine

Selles koodiosas käsitleme kasutajapäringuid.

#### TypeScript

1. Lisa meetod, mida kasutame oma LLM-i kutsumiseks:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Kutsu serveri tööriista
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tee midagi tulemusega
        // TODO

        }
    }
    ```

    Eelnevas koodis me:

    - Lisame meetodi `callTools`.
    - Meetod võtab LLM-i vastuse ja kontrollib, millised tööriistad on kutsutud, kui üldse:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // tööriista kutsumine
        }
        ```

    - Kutsutakse tööriista, kui LLM näitab, et seda peaks kutsuma:

        ```typescript
        // 2. Kutsuge välja serveri tööriist
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tehke midagi tulemusega
        // TODO
        ```

2. Uuendada meetodit `run`, et see sisaldaks LLM-i kõnesid ja `callTools` päringuid:

    ```typescript

    // 1. Loo sõnumid, mis on sisendiks LLM-ile
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Kutsu LLM-i
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Läbi mine LLM-i vastus, iga valiku puhul kontrolli, kas see sisaldab tööriistakutseid
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Suurepärane, vaatame kogu koodi tervikuna:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Impordi zod skeemi valideerimiseks

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // tulevikus võib olla vaja muuta sellele URL-ile: https://models.github.ai/inference
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
          // Loo zod skeem sisend_skeemi põhjal
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Määrake tüübiks selgelt "function"
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
    
    
          // 2. Kutsu serveri tööriist
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Tee midagi tulemusega
          // TÄHENDUSE LISA
    
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
    
        // 3. Läbivaatamine LLM vastusest, iga valiku puhul kontrolli, kas selles on tööriista kutsed
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

1. Lisame mõned importimised, mis on vajalikud LLM-i kutsumiseks

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Järgmiseks lisame funktsiooni, mis kutsub LLM-i:

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
            # Valikulised parameetrid
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

    Eelnevas koodis oleme:

    - Edastanud oma funktsioonid, mille leidsime MCP serverist ja teisendasime, LLM-ile.
    - Kutsunud LLM-i nimetatud funktsioonidega.
    - Seejärel kontrollime tulemust, et näha, milliseid funktsioone peaksime kutsuma, kui üldse.
    - Lõpuks edastame funktsioonide massiivi kutsete tegemiseks.

3. Viimane samm, uuendame oma põhikoodi:

    ```python
    prompt = "Add 2 to 20"

    # küsi LLM-ilt, milliseid tööriistu üldse kasutada, kui üldse
    functions_to_call = call_llm(prompt, functions)

    # kutsu soovitatud funktsioonid välja
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    See oli viimane samm, ülaltoodud koodis me:

    - Kutsume MCP tööriista `call_tool` kaudu, kasutades funktsiooni, mida LLM arvates peaksime meie päringu põhjal kutsuma.
    - Väljastame tööriistakutse tulemuse MCP serveris.

#### .NET

1. Näitame koodi LLM-päringu tegemiseks:

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

    Eelnevas koodis oleme:

    - Hankinud tööriistad MCP serverist, `var tools = await GetMcpTools()`.
    - Määratlenud kasutajapäringu `userMessage`.
    - Konfigureerinud valikute objekti, määrates mudeli ja tööriistad.
    - Teinud päringu LLM-ile.

2. Viimane samm, vaatame, kas LLM arvab, et peaksime funktsiooni kutsuma:

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

    Eelnevas koodis oleme:

    - Läbinud funktsiooni kutsete nimekirja.
    - Iga tööriistakutse puhul eemaldanud nime ja argumendid ning kutsunud MCP serveris tööriista MCP kliendi abil. Lõpuks trükime tulemused välja.

Siin on kogu kood tervikuna:

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
    // Täida loomuliku keele päringuid, mis kasutavad automaatselt MCP tööriistu
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

Eelnevas koodis oleme:

- Kasutanud lihtsaid looduliku keele päringuid, et suhelda MCP serveri tööriistadega
- LangChain4j raamistik haldab automaatselt:
  - Kasutajapäringute teisendamist tööriistakutseteks vastavalt vajadusele
  - Asjakohaste MCP tööriistade kutsumist LLM otsuste põhjal
  - Vestluse juhtimist LLM-i ja MCP serveri vahel
- Meetod `bot.chat()` tagastab loodulikus keeles vastuseid, mis võivad sisaldada MCP tööriistade täitmiste tulemusi
- See lähenemine tagab sujuva kasutajakogemuse, kus kasutajal ei pea olema teadmisi põhineva MCP rakenduse kohta

Täielik koodi näide:

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


Siin toimub suurem osa tööst. Kutsume LLM-i esmase kasutajapäringuga, seejärel töötleme vastuse, et näha, kas on vaja kutsuda mõnda tööriista. Kui on, kutsume need tööriistad ja jätkame vestlust LLM-iga, kuni tööriistade kutsumine enam vajalik ei ole ja meil on lõplik vastus.

Me teeme mitu LLM-i kutsumist, seega määratleme funktsiooni, mis tegeleb LLM-i kutsumisega. Lisa järgmine funktsioon oma faili `main.rs`:

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

See funktsioon võtab LLM kliendi, sõnumite nimekirja (sh kasutaja päringu), MCP serveri tööriistad ja saadab LLM-ile päringu, tagastades vastuse.

LLM-i vastus sisaldab valikute massiivi `choices`. Peame töötlema tulemust, et näha, kas seal on olemas `tool_calls`. See annab meile teada, et LLM soovib konkreetset tööriista kutsuda koos argumentidega. Lisa järgmine kood oma faili `main.rs` lõppu, et määratleda funktsioon LLM-i vastuse töötlemiseks:

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

    // Prindi sisu, kui see on saadaval
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Käitle tööriista kutseid
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Lisa assistendi sõnum

        // Täida iga tööriista kutse
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Lisa tööriista tulemus sõnumitesse
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Jätka vestlust tööriista tulemustega
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

Kui `tool_calls` on olemas, ekstraheerib see tööriista info, kutsub MCP serveri tööriista päringuga ja lisab tulemused vestluse sõnumitesse. Seejärel jätkab vestlust LLM-i ja sõnumid uuenevad assistendi vastuse ning tööriista kutse tulemustega.

MCP kutsete jaoks LLM-i tagasi antava tööriistakutse info ekstraheerimiseks lisame teise abifunktsiooni, mis võtab kõike vajalikku välja tehtava kutse jaoks. Lisa järgmine kood oma faili `main.rs` lõppu:

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

Kõigi osade olemasolul saame nüüd töödelda esmast kasutajapäringut ja kutsuda LLM-i. Uuenda oma `main` funktsiooni järgmise koodiga:

```rust
// LLM vestlus tööriistakõnedega
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

See esitab LLM-ile esialgse kasutajapäringu kahe arvu summa kohta ning töötleb vastust dünaamiliselt tööriistade kutsumiseks.

Suurepärane, sa tegid selle ära!

## Ülesanne

Võta harjutuse kood ja ehita server koos veel mõningate tööriistadega. Seejärel loo klient koos LLM-iga nagu harjutuses ja testi seda erinevate päringutega, veendumaks, et kõik su serveri tööriistad kutsutakse dünaamiliselt. Selline kliendi loomise viis tagab lõppkasutajale suurepärase kasutajakogemuse, kuna nad saavad kasutada päringuid täpsete kliendikäskluste asemel ega pea teadma MCP serveri kutsumist.

## Lahendus

[Lahendus](./solution/README.md)

## Peamised mõtted

- LLM-i lisamine kliendi hulka annab kasutajatele parema viisi MCP serveritega suhtlemiseks.
- Pead teisendama MCP serveri vastuse millekski, mida LLM mõista saab.

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulaator](../../../../03-GettingStarted/samples/rust)

## Täiendavad ressursid

## Mis järgmiseks

- Järgmiseks: [Serveri kasutamine Visual Studio Code abil](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->