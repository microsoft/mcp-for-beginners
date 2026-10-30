# Kliendi loomine LLM-iga

> [!NOTE]
> Java kliendi näited ühenduvad pärandliku HTTP+SSE transpordi kaudu ja
> sihtivad MCP `2025-11-25` SDK API-sid. Kasutage `2026-07-28`-ühilduvat SDK-d ja
> Streamable HTTP-i uute kaugklientide jaoks.

Siiani oled näinud, kuidas luua serverit ja klienti. Klient on suutnud serverit otseselt kutsuda selle tööriistade, ressursside ja promptide loetlemiseks. Siiski pole see väga praktiline lähenemine. Sinu kasutajad elavad agentsel ajastul ning eeldavad, et kasutavad prompt'e ja suhtlevad selle asemel LLM-iga. Neid ei huvita, kas kasutad MCP-d oma võimete salvestamiseks; nad lihtsalt ootavad, et saaksid loomulikus keeles suhelda. Kuidas seda siis lahendada? Lahendus on lisada kliendile LLM.

## Ülevaade

Selles õppetükis keskendume LLM-i lisamisele teie kliendile ja näitame, kuidas see tagab kasutajale palju parema kogemuse.

## Õpitulemused

Selle õppetüki lõpus suudate:

- Luua klient LLM-iga.
- Sujuvalt suhelda MCP-serveriga, kasutades LLM-i.
- Pakkuda kliendipoolsel küljel paremat lõppkasutajakogemust.

## Lähenemine

Püüame mõista, millist lähenemist vajame. LLM-i lisamine tundub lihtne, kuid kas me teeme seda tegelikult?

Siin on, kuidas klient serveriga suhtleb:

1. Looge ühendus serveriga.

1. Loetlege võimed, promptid, ressursid ja tööriistad ning salvestage nende skeem.

1. Lisage LLM ja edastage salvestatud võimed ning nende skeem vormingus, mida LLM mõistab.

1. Töötlege kasutaja prompti, edastades selle LLM-ile koos kliendi loetletud tööriistadega.

Suurepärane, nüüd mõistame, kuidas seda kõrgetasemeliselt teha, proovime seda alljärgnevas harjutuses.

## Harjutus: Kliendi loomine LLM-iga

Selles harjutuses õpime, kuidas lisada LLM oma kliendile.

### Microsoft Foundry seadistamine

GitHub Models lõpetati 30. juulil 2026. Loo Microsoft Foundry ressurss,
paiguta aktiivne mudel, näiteks `gpt-5.1`, ja määra need keskkonnamuutujad:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

Kasutage paigalduse nime API-kõnedes. See võib erineda aluseks oleva mudeli
nimest. Vaadake
[Microsoft Foundry mudelite lõpetamise ajakava](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
enne mudeli valimist.

### -1- Ühendu serveriga

Loome esmalt oma kliendi:

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

Eelnevas koodis me:

- Impordisime vajalikud teegid
- Loodud klass kahe liikmega, `client` ja `openai`, mis aitavad meil vastavalt klienti hallata ja suhelda LLM-iga.
- Konfigureerisime OpenAI kliendi kasutamaks Microsoft Foundry v1 lõpp-punkti ja API-võtit.

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

Eelnevas koodis me:

- Impordisime MCP jaoks vajalikud teegid
- Lõime kliendi

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

Esmalt peate lisama LangChain4j sõltuvused oma `pom.xml` faili. Lisage need sõltuvused, et võimaldada MCP integratsioon ja OpenAI-ühilduv MiniMax API:

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

Määrake oma MiniMax API-võti ja vajadusel lõpp-punkt ning mudel.
`MINIMAX_MODEL_ID` toetab `MiniMax-M3` ja `MiniMax-M2.7`. Kui
`OPENAI_BASE_URL` pole määratud, `MINIMAX_REGION` toetab `global_en` ja `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Kui soovite valida lõpp-punkti regiooni järgi, jätke `OPENAI_BASE_URL` välja:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Seejärel looge oma Java kliendi klass:

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

Eelnevas koodis me:

- **Lisatud LangChain4j sõltuvused**: vajalikud MCP integratsiooni ja OpenAI-ühilduva MiniMax API jaoks
- **Imporditud LangChain4j teegid**: MCP integratsiooni ja OpenAI vestlusmudeli funktsionaalsuse jaoks
- **Loodud `ChatLanguageModel`**: Konfigureeritud kasutama MiniMax-i koos teie MiniMax API-võtmega, lõpp-punkti ja toetatud mudeli ID-ga
- **Seadis üles HTTP-transpordi**: kasutades Server-Sent Events (SSE) MCP serveriga ühenduse loomiseks
- **Loodud MCP klient**: mis haldab suhtlust serveriga
- **Kasutatud LangChain4j sisseehitatud MCP tuge**: mis lihtsustab integratsiooni LLM-ide ja MCP serverite vahel

#### Rust

See näide eeldab, et teil töötab Rust-põhine MCP server. Kui teil seda pole, vaadake serveri loomiseks tagasi õppetundi [01-first-server](../01-first-server/README.md).

Kui teil on Rust MCP server, avage terminal ja liikuge serveriga samasse kataloogi. Seejärel käivitage järgmine käsk uue LLM kliendi projekti loomiseks:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Lisage järgmised sõltuvused oma `Cargo.toml` faili:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Ametlikku Rusti teeki OpenAI jaoks ei ole, kuid `async-openai` crate on [kogukonna hooldatav teek](https://platform.openai.com/docs/libraries/rust#rust), mida sageli kasutatakse.

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

See kood seab üles Rusti rakenduse, mis ühendub MCP serveriga ja
Microsoft Foundry mudeli juurutusega LLM-i suhtluse jaoks.

> [!IMPORTANT]
> Määrake `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, ja
> `AZURE_OPENAI_DEPLOYMENT` enne rakenduse käivitamist.

Suurepärane, järgmiseks sammuks loetleme serveri võimed.

### -2- Serveri võimete loetlemine

Nüüd ühendame serveriga ja küsime selle võimeid:

#### Typescript

Selles samas klassis lisage järgmised meetodid:

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

Eelnevas koodis me:

- Lisatud kood serveriga ühenduse loomiseks, `connectToServer`.
- Loodud `run` meetod, mis vastutab meie rakenduse voo haldamise eest. Seni loetleb see ainult tööriistu, kuid lisame sellele varsti veel.

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

Siin on, mida lisasime:

- Loetlesime ressursid ja tööriistad ning printisime need. Tööriistade puhul loetlesime ka `inputSchema`, mida kasutame hiljem.

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

Eelnevas koodis me:

- Loetlesime MCP serveris saadaval olevad tööriistad
- Iga tööriista jaoks loetlesime nime, kirjelduse ja selle skeemi. Viimane on see, mida kasutame varsti tööriistade kutsumiseks.

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

Eelnevas koodis me:

- Loodud `McpToolProvider`, mis automaatselt avastab ja registreerib kõik MCP serveri tööriistad
- Tööriistapakkuja käsitleb MCP tööriistade skeemide ja LangChain4j tööriistavormi vahelise teisenduse siseselt
- See lähenemine peidab käsitsi tööriistade loetlemise ja teisendamise keerukuse

#### Rust

MCP-serverist tööriistade kättesaamiseks kasutatakse meetodit `list_tools`. Oma `main` funktsioonis, pärast MCP kliendi seadistamist, lisage järgmine kood:

```rust
// Get MCP tool listing 
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Serveri võimete teisendamine LLM-tööriistadeks

Järgmiseks, pärast serveri võimete loetlemist, tuleb need teisendada vormingusse, mida LLM mõistab. Kui me seda teeme, saame neid võimeid pakkuda meie LLM-ile tööriistadena.

#### TypeScript

1. Lisage järgmine kood MCP serveri vastuse teisendamiseks tööriista formaati, mida LLM saab kasutada:

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

    Ülaltoodud kood võtab MCP serveri vastuse ja teisendab selle tööriista definitsiooni formaati, mida LLM mõistab.

2. Uuendame järgmisena meetodit `run`, et loetleda serveri võimed:

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

    Eelnevas koodis oleme uuendanud meetodit `run`, et läbi tulemuse liikudes iga kirje puhul kutsuda `openAiToolAdapter`.

#### Python

1. Esiteks loome järgmise teisendusfunktsiooni

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

    Ülaltoodud funktsioonis `convert_to_llm_tools` võtame MCP tööriista vastuse ja teisendame selle vormingusse, mida LLM saab mõista.

2. Järgmisena uuendame oma kliendi koodi, et seda funktsiooni kasutada järgmise näite järgi:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Siin lisame kutsumise `convert_to_llm_tool`, et teisendada MCP tööriista vastus millekski, mida saame hiljem LLM-ile anda.

#### .NET

1. Lisame koodi MCP tööriista vastuse teisendamiseks millekski, mida LLM saab mõista

```csharp
ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}
```

Eelnevas koodis me:

- Loodud funktsioon `ConvertFrom`, mis võtab nime, kirjelduse ja sisendi skeemi.
- Loodud OpenAI `ChatTool` MCP tööriista JSON-skeemist.

2. Vaatame, kuidas saame mõnda olemasolevat koodi uuendada, et kasutada ülaltoodud funktsiooni:

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
    
Eelnevas koodis me:

- Uuendasime funktsiooni, et teisendada MCP tööriista vastus LLM tööriistaks. Tõstame esile lisatud koodi:

   ```csharp
   JsonElement propertiesElement;
   tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

   var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
   Console.WriteLine($"Tool definition: {def}");
   toolDefinitions.Add(def);
   ```

Sisendi skeem on tööriista vastuse osa, kuid asub atribuudil "properties", seega tuleb see välja tõsta. Lisaks kutsume nüüd `ConvertFrom` tööriista detailidega. Nüüd, kui raske töö on tehtud, vaatame, kuidas see kutsumine kokku tuleb, kui järgmisena töötleme kasutaja prompti.

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

Eelnevas koodis me:

- Määratlesime lihtsa `Bot` liidese loomuliku keele interaktsioonide jaoks
- Kasutasime LangChain4j `AiServices`, et automaatselt siduda LLM MCP tööriistapakkujaga
- Raamistik käsitleb tööriistade skeemi teisendust ja funktsioonikõnesid automaatselt taustal
- See lähenemine kõrvaldab käsitsi tööriistade teisendamise - LangChain4j võtab enda kanda kogu keerukuse MCP tööriistade teisendamisel LLM-iga ühilduvaks formaadiks

#### Rust

MCP tööriista vastuse teisendamiseks vormingusse, mida LLM mõistab, lisame abifunktsiooni, mis vormindab tööriistade loendi. Lisage järgmine kood oma faili `main.rs`, alla funktsiooni `main`. Seda kutsutakse, kui tehakse päringuid LLM-ile:

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

Suurepärane, me pole veel seadistanud kasutajapäringute töötlemist, nii et tegeleme sellega järgmisena.

### -4- Kasutaja prompti töötlemine

Selles koodiosas töötleme kasutajapäringuid.

#### TypeScript

1. Lisage meetod, mida kasutatakse meie LLM-i kutsumiseks:

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

    Eelnevas koodis me:

    - Lisati meetod `callTools`.
    - Meetod võtab LLM-i vastuse ja kontrollib, milliseid tööriistu on kutsutud, kui üldse:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // call tool
        }
        ```

    - Kutsub tööriista, kui LLM näitab, et seda tuleks kutsuda:

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

2. Uuendage meetodit `run`, et lisada kutsed LLM-ile ja kutsuda `callTools`:

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

Suurepärane, vaatame kogu koodi koos:

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

1. Lisame mõned impordid, mis on vajalikud LLM-i kutsumiseks

    ```python
    # llm
    import os
    from openai import OpenAI
    import json
    ```

2. Järgmiseks lisame funktsiooni, mis kutsub LLM-i. See näide kasutab
    aktiivset `gpt-5.1` mudelit. Kontrollige
    [Microsoft Foundry mudelite lõpetamise ajakava](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
    mudeli valimisel oma rakenduse jaoks.

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

    Eelnevas koodis me:

    - Andsime LLM-ile meie funktsioonid, mille leidsime MCP serverist ja teisendasime.
    - Seejärel kutsusime LLM-i nimetatud funktsioonidega.
    - Seejärel uurime tulemust, et näha, milliseid funktsioone peaksime kutsuma, kui üldse.
    - Lõpuks edastame kutsutavate funktsioonide massiivi.

3. Viimane samm, uuendame oma peamist koodi:

    ```python
    prompt = "Add 2 to 20"

    # ask LLM what tools to all, if any
    functions_to_call = call_llm(prompt, functions)

    # call suggested functions
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Nii, see oli viimane samm, ülaltoodud koodis me:

    - Kutsume MCP tööriista läbi `call_tool`, kasutades funktsiooni, mida LLM arvas, et peaksime kutsuma meie prompti põhjal.
    - Trükime tööriista kutse tulemuse MCP serverisse.

#### .NET

1. Näitame mõningast koodi LLM-prompti päringu tegemiseks:

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

    Eelnevas koodis me:

    - Hankis tööriistu MCP serverist, `var tools = await GetMcpTools()`.
    - Määratleti kasutajapäring `userMessage`.
    - Koostati valikute objekt, mis määratleb mudeli ja tööriistad.
    - Tehti päring LLM-ile.

2. Viimane samm — vaatame, kas LLM arvab, et me peaksime funktsiooni kutsuma:

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

    Eelnevas koodis oleme:

    - Läbisime funktsioonikõnede loendi.
    - Iga tööriista kutsumisel parsime välja nime ja argumendid ning kutsume tööriista MCP serveris, kasutades MCP klienti. Lõpuks prindime tulemused.

Siin on kogu kood:

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

Eelnevas koodis oleme:

- Kasutasime lihtsaid loomuliku keele päringuid MCP serveri tööriistadega suhtlemiseks
- LangChain4j raamistik käsitleb automaatselt:
  - Kasutaja päringute teisendamine tööriistakõnedeks, kui vaja
  - Õigete MCP tööriistade kutsumine vastavalt LLM-i otsusele
  - Vestluse voo haldamine LLM-i ja MCP serveri vahel
- The `bot.chat()` method returns natural language responses that may include results from MCP tool executions
- See lähenemine tagab sujuva kasutajakogemuse, kus kasutajad ei pea teadma aluseks olevat MCP rakendust

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

Siin toimub suurem osa tööst. Me kutsume LLM-i esialgse kasutajapäringuga, seejärel töötleme vastuse, et näha, kas mõnda tööriista tuleb kutsuda. Kui jah, siis kutsume need tööriistad ja jätkame vestlust LLM-iga, kuni täiendavaid tööriistakõnesid ei vaja ning meil on lõplik vastus.

Me teeme LLM-ile mitu kõnet, seega määratleme funktsiooni, mis käsitleb LLM-kõnet. Lisa järgmine funktsioon faili `main.rs`:

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

See funktsioon võtab LLM-kliendi, sõnumite loendi (sealhulgas kasutajapäringu), tööriistad MCP serverist ja saadab LLM-ile päringu, tagastades vastuse.

LLM vastuses on massiiv `choices`. Peame töötlema tulemuse, et näha, kas esinevad `tool_calls`. See ütleb meile, et LLM taotleb konkreetse tööriista kutsumist argumentidega. Lisa järgmine kood faili `main.rs` lõppu, et määratleda funktsioon LLM vastuse töötlemiseks:

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

Kui esinevad `tool_calls`, eraldab see tööriista info, kutsub MCP serverit tööriistapäringuga ning lisab tulemused vestluse sõnumitesse. Seejärel jätkab vestlust LLM-iga ning sõnumid uuendatakse assistendi vastuse ja tööriistakõnede tulemustega.

Selleks, et eraldada tööriistakõne info, mida LLM tagastab MCP kutsude jaoks, lisame veel abifunktsiooni, mis eraldab kõik, mida kõne tegemiseks vaja on. Lisa järgmine kood faili `main.rs` lõppu:

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

Kõik osad paigas, saame nüüd käsitleda esialgset kasutajapäringut ja kutsuda LLM-i. Uuenda oma funktsiooni `main`, et see sisaldaks järgmist koodi:

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

See küsitleb LLM-i esialgse kasutajapäringuga, milles palutakse kahe arvu summa, ning töötleb vastuse, et dünaamiliselt käsitleda tööriistakõnesid.

Suurepärane, said sellega hakkama!

## Ülesanne

Võta harjutusest kood ja lisa serverile rohkem tööriistu. Seejärel loo klient LLM-iga, nagu harjutuses, ja testi seda erinevate päringutega, et veenduda, et kõik sinu serveri tööriistad kutsutakse dünaamiliselt. Selline kliendi ülesehitus tagab lõppkasutajale suurepärase kasutajakogemuse: nad saavad kasutada päringuid täpsete kliendikäskude asemel ja ei pea teadma MCP serveri kutsumisest.

## Lahendus

[Lahendus](./solution/README.md)

## Peamised järeldused

- LLM-i lisamine oma kliendile annab parema viisi kasutajate suhtlemiseks MCP serveritega.
- Pead teisendama MCP serveri vastuse millekski, mida LLM saab mõista.

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.NET kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScripti kalkulaator](../samples/javascript/README.md)
- [TypeScripti kalkulaator](../samples/typescript/README.md)
- [Pythoni kalkulaator](../../../../03-GettingStarted/samples/python)
- [Rusti kalkulaator](../../../../03-GettingStarted/samples/rust)

## Täiendavad ressursid

## Mis järgmiseks

- Järgmiseks: [Serveri kasutamine Visual Studio Code'is](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->