# Kliendi loomine LLM-iga

Seni olete näinud, kuidas luua serverit ja klienti. Klient on suutnud serverit otseselt kutsuda, et loetleda selle tööriistu, ressursse ja põhimõtteid. Kuid see pole väga praktiline lähenemine. Teie kasutajad elavad agendi ajastul ja ootavad, et kasutaksid põhimõtteid ning suhtleksid LLM-iga. Neid ei huvita, kas kasutate oma võimekuse salvestamiseks MCP-d; nad lihtsalt ootavad loomulikus keeles suhtlemist. Kuidas me seda lahendame? Lahendus on lisada kliendile LLM.

## Ülevaade

Selles õppetükis keskendume LLM-i lisamisele teie kliendile ja näitame, kuidas see pakub kasutajale palju paremat kogemust.

## Õpieesmärgid

Selle õppetüki lõpuks oskate:

- Luua klient LLM-iga.
- Sujuvalt suhelda MCP serveriga LLM-i abil.
- Pakkuda kliendi poolel paremat lõppkasutaja kogemust.

## Lähenemine

Proovime mõista, millist lähenemist peame kasutama. LLM-i lisamine tundub lihtne, kuid kas me seda tegelikult teeme?

Nii suhtleb klient serveriga:

1. Loob ühenduse serveriga.

1. Loetleb võimekused, põhimõtted, ressursid ja tööriistad ning salvestab nende skeemi.

1. Lisab LLM-i ja edastab salvestatud võimekused ja nende skeemi vormingus, mida LLM mõistab.

1. Töötleb kasutaja põhimõtet, edastades selle LLM-ile koos kliendi poolt loetletud tööriistadega.

Suurepärane, nüüd mõistame, kuidas seda kõrgemal tasemel teha, proovime seda alltoodud ülesandes.

## Harjutus: Kliendi loomine LLM-iga

Selles harjutuses õpime lisama LLM-i oma kliendile.

### Autentimine GitHubi isikliku juurdepääsuvõtmega

GitHubi võtme loomine on lihtne protsess. Siin on, kuidas seda teha:

- Minge GitHubi seadistusse – klõpsake oma profiilipildil paremas ülanurgas ja valige Seaded.
- Navigeerige arendaja sätete alla – kerige alla ja klõpsake Arendaja sätted.
- Valige isiklikud juurdepääsuvõtmed – klõpsake peenhäälestatud võtmed ja seejärel Genereeri uus võti.
- Seadistage oma võti – lisage viite märkus, määrake aegumiskuupäev ja valige vajalikud õigused. Selles juhul kindlasti lisage Mudelite õigus.
- Genereerige ja kopeerige võti – klõpsake Genereeri võti ja veenduge, et kopeerite selle kohe, sest hiljem seda enam näha ei saa.

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

Eelnevas koodis oleme:

- Impordinud vajalikud teegid
- Loonud klassi kahel liikmel `client` ja `openai`, mis aitavad meil hallata klienti ja suhelda LLM-iga.
- Konfigureerinud meie LLM-i eksemplari kasutama GitHubi mudeleid, määrates `baseUrl` inferentsi API suunas.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Loo serveri parameetrid stdio ühenduseks
server_params = StdioServerParameters(
    command="mcp",  # Täidetav fail
    args=["run", "server.py"],  # Valikulised käsurea argumendid
    env=None,  # Valikulised keskkonnamuutujad
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Algata ühendus
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Eelnevas koodis oleme:

- Importinud vajalikud teegid MCP jaoks
- Loonud kliendi

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

Esiteks peate lisama LangChain4j sõltuvused oma `pom.xml` faili. Lisage need sõltuvused MCP integratsiooni ja OpenAI-ga ühilduva MiniMax API lubamiseks:

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

Määrake oma MiniMax API võti ja vajadusel lõpp-punkt ning mudel.
`MINIMAX_MODEL_ID` toetab `MiniMax-M3` ja `MiniMax-M2.7`.
Kui `OPENAI_BASE_URL` pole määratud, toetab `MINIMAX_REGION` väärtusi `global_en` ja `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Lõpp-punkti tõrgete saamiseks piirkonna järgi jätke `OPENAI_BASE_URL` välja:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Seejärel looge oma Java kliendiklass:

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

Eelnevas koodis oleme:

- **Lisanud LangChain4j sõltuvused**: vajalikud MCP integratsiooniks ja OpenAI-ga ühilduvaks MiniMax API-ks
- **Impordinud LangChain4j teegid**: MCP integratsiooni ja OpenAI vestlusmudeli funktsioonide jaoks
- **Loonud `ChatLanguageModel`**: konfigureeritud kasutama MiniMax-i koos teie MiniMax API võtme, lõpp-punkti ja toetatud mudeli ID-ga
- **Seadistanud HTTP transpordi**: kasutades Server-Sent Events (SSE) MCP serveriga ühendamiseks
- **Loonud MCP kliendi**: mis haldab suhtlust serveriga
- **Kasutab LangChain4j sisseehitatud MCP tugi**: mis lihtsustab LLM-ide ja MCP serverite integreerimist

#### Rust

See näide eeldab, et teil on Rust-põhine MCP server käimas. Kui teil seda pole, vaadake uuesti [01-first-server](../01-first-server/README.md) õppetükk, et server luua.

Kui teil on Rust MCP server, avage terminal ja liikuge kausta, kus server asub. Seejärel käivitage järgmine käsk, et luua uus LLM kliendiprojekt:

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
> Rusti ametlikku OpenAI teeki pole, kuid `async-openai` crate on [kogukonna poolt hooldatav teek](https://platform.openai.com/docs/libraries/rust#rust), mida sageli kasutatakse.

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

    // TODO: LLM vestlus tööriista kõnedega

    Ok(())
}
```

See kood seab üles lihtsa Rusti rakenduse, mis ühendub MCP serveri ja GitHub Mudelitega LLM suhtlusteks.

> [!IMPORTANT]
> Veenduge, et määrate keskkonnamuutujale `OPENAI_API_KEY` oma GitHubi võtme enne rakenduse käivitamist.

Suurepärane, järgmises etapis loetleme serveri võimekused.

### -2- Serveri võimekuste loetlemine

Nüüd ühendame serveriga ja küsime selle võimekusi:

#### Typescript

Lisage samasse klassi järgmised meetodid:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // tööriistade nimekirja koostamine
    const toolsResult = await this.client.listTools();
}
```

Eelnevas koodis oleme:

- Lisanud ühenduse loomise koodi serveriga, `connectToServer`.
- Loonud meetodi `run`, mis vastutab rakenduse voolu juhtimise eest. Seni loetleb see tööriistad, kuid lisame varsti juurde rohkem.

#### Python

```python
# Loetle saadaolevad ressursid
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Loetle olemasolevad tööriistad
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Siin on, mida me lisasime:

- Ressursid ja tööriistad ning prinditud. Tööriistade jaoks loetleme ka `inputSchema`, mida hiljem kasutame.

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

- Loetlenud MCP serveris saadaolevad tööriistad
- Iga tööriista jaoks loetlenud nime, kirjelduse ja skeemi. Viimane on midagi, mida kasutame peagi tööriistade kutsumiseks.

#### Java

```java
// Loo tööriista pakkuja, mis avastab automaatselt MCP tööriistad
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP tööriista pakkuja haldab automaatselt:
// - MCP serverist saadaolevate tööriistade nimekirja koostamine
// - MCP tööriistade skeemide teisendamine LangChain4j formaati
// - Tööriista täitmise ja vastuste haldamine
```

Eelnevas koodis oleme:

- Loonud `McpToolProvider`, mis automaatselt avastab ja registreerib kõik MCP serveri tööriistad
- Tööriista pakkuja haldab MCP tööriista skeemi ja LangChain4j tööriista vormingu vahelist teisendust sisemiselt
- See lähenemine varjab käsitsi tööriistade loetelu ja teisendamise protsessi

#### Rust

Tööriistade hankimine MCP serverist toimub `list_tools` meetodiga. Oma `main` funktsioonis, pärast MCP kliendi seadistamist, lisage järgmine kood:

```rust
// Hangi MCP tööriistade nimekiri
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Serveri võimekuste teisendamine LLM tööriistadeks

Pärast serveri võimekuste loetlemist teisendame need vormingusse, mida LLM mõistab. Kui me seda teeme, saame neid võimekusi anda oma LLM-ile tööriistadena.

#### TypeScript

1. Lisage järgmine kood, et teisendada MCP serveri vastus tööriista vormingusse, mida LLM saab kasutada:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Loo zod skeem, mis põhineb input_schema-l
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Sea tüüp selgelt "function"iks
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

    Ülaltoodud kood võtab MCP serveri vastuse ja teisendab selle tööriista definitsiooni vormingusse, mida LLM mõistab.

2. Uuendame nüüd meetodit `run`, et lisada serveri võimekuste loetelu:

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

    Eelnevas koodis uuendasime meetodit `run`, et kaardistada tulemuse kaudu ja iga kirje puhul kutsuda `openAiToolAdapter`.

#### Python

1. Loome esmalt järgmise teisendusfunktsiooni

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

    Funktsioonis `convert_to_llm_tools` võtame MCP tööriista vastuse ja teisendame selle vormingusse, mida LLM saab mõista.

2. Seejärel uuendame oma kliendi koodi, et kasutada seda funktsiooni järgmiselt:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Siin lisame kutse `convert_to_llm_tool`, et teisendada MCP tööriista vastus millekski, mida saame hiljem LLM-ile anda.

#### .NET

1. Lisame koodi, mis teisendab MCP tööriista vastuse millekski, mida LLM saab mõista

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

- Loonud funktsiooni `ConvertFrom`, mis võtab nime, kirjelduse ja sisendskeemi.
- Määratlenud funktsionaalsuse, mis loob funktsioonide definitsiooni, mis antakse edasi ChatCompletionsDefinition-ile. Viimane on midagi, mida LLM mõistab.

2. Vaatame, kuidas saame olemasolevat koodi uuendada, et kasutada seda funktsiooni:

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
// Loo boti liides loomuliku keele suhtluseks
public interface Bot {
    String chat(String prompt);
}

// Konfigureeri tehisintellekti teenus LLM ja MCP tööriistadega
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Eelnevas koodis oleme:

- Määratlenud lihtsa `Bot` liidese loomuliku keele interaktsioonide jaoks
- Kasutanud LangChain4j `AiServices`-t, et automaatselt siduda LLM MCP tööriistapakkujaga
- Raamistik haldab automaatselt tööriista skeemi teisendust ja funktsioonide kutsumist taustal
- See lähenemine elimineerib käsitsi tööriistade teisendamise – LangChain4j haldab kõiki keerukusi MCP tööriistade teisendamisel LLM-i ühilduvasse formaati

#### Rust

MCP tööriista vastuse teisendamiseks vormingusse, mida LLM mõistab, lisame abifunktsiooni, mis vormindab tööriistade loendi. Lisage järgmine kood oma `main.rs` faili `main` funktsiooni alla. Seda kutsutakse LLM-ile päringute tegemisel:

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

Suurepärane, oleme valmis haldama kasutaja päringuid, nüüd alustame sellest.

### -4- Kasutaja põhimõtte päringu haldamine

Selles koodiosas käsitleme kasutaja päringuid.

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


        // 2. Kutsu serveri tööriista
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tee midagi tulemusega
        // TEHA

        }
    }
    ```

    Eelnevas koodis oleme:

    - Lisanud meetodi `callTools`.
    - Meetod võtab LLM-i vastuse ja kontrollib, millised tööriistad on kutsutud, kui üldse:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // kutsu tööriist
        }
        ```

    - Kutsub tööriista, kui LLM näitab, et see tuleb kutsuda:

        ```typescript
        // 2. Kutsu serveri tööriist
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tee midagi tulemusega
        // TEGEMIST VAJA
        ```

2. Uuendage meetodit `run`, et lisada kutsed LLM-le ja `callTools`-i kutsumine:

    ```typescript

    // 1. Loo sõnumid, mis on LLM sisendiks
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

    // 3. Läbi LLM vastuse, kontrolli iga valiku puhul, kas seal on tööriista kutseid
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
            baseURL: "https://models.inference.ai.azure.com", // Võib tulevikus vaja minna muuta selleks URL-iks: https://models.github.ai/inference
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
          // Loo zod skeem sisendskeemi põhjal
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Sea tüübiks selgesõnaliselt "function"
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
    
          // 3. Tee tulemusega midagi
          // TEGEMATA
    
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
    
        // 3. Läbi LLM vastuse, iga valiku puhul kontrolli, kas selles on tööriista kutseid
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

1. Lisame mõningased impordid, mis on vajalikud LLM-i kutsumiseks

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Seejärel lisame funktsiooni, mis kutsub LLM-i:

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

    - Edastanud funktsioonid, mis leiti MCP serverist ja teisendati, LLM-ile.
    - Seejärel kutsusime LLM-i neist funktsioonidest.
    - Seejärel kontrollime tulemust, et näha, milliseid funktsioone tuleb kutsuda, kui üldse.
    - Lõpuks edastasime massiivi funktsioonidest, mida kutsuda.

3. Lõpuks uuendame peamist koodi:

    ```python
    prompt = "Add 2 to 20"

    # küsi LLM-ilt, milliseid tööriistu kasutada, kui üldse
    functions_to_call = call_llm(prompt, functions)

    # kutsu ettepanekute funktsioonid üles
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Nii, see oli viimane samm, ülaltoodud koodis me:

    - Kutsub MCP tööriista `call_tool` abil, kasutades funktsiooni, mida LLM arvas, et peaksime kutsuma vastavalt meie põhimõttele.
    - Prindime tööriista kutse tulemuse MCP serverile.

#### .NET

1. Näitame natuke koodi LLM põhimõtte päringu tegemiseks:

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

    - Tõime tööriistad MCP serverist, `var tools = await GetMcpTools()`.
    - Määratlesime kasutaja põhimõtte `userMessage`.
    - Koostasime valikute objekti, mis määrab mudeli ja tööriistad.
    - Tegime päringu LLM-ile.

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

    - Läbimänginud funktsioonikõnede nimekirja.
    - Iga tööriistakutset korral parsime nime ja argumendid ning kutsume tööriista MCP serveris MCP kliendi abil. Lõpuks prindime tulemused.

Siin on kood tervikuna:

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
    // Täida loomuliku keele päringud, mis automaatselt kasutavad MCP tööriistu
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

- Kasutanud lihtsaid loomulikus keeles põhimõtteid MCP serveri tööriistadega suhtlemiseks
- LangChain4j raamistik haldab automaatselt:
  - Kasutaja põhimõtete tõlkimise tööriista kõnedeks vajaduse korral
  - Õigete MCP tööriistade kutsumise LLM otsuse põhjal
  - Vestluse voolu haldamise LLM ja MCP serveri vahel
- Meetod `bot.chat()` tagastab loomuliku keele vastuseid, mis võivad sisaldada MCP tööriistade täitmise tulemusi
- See lähenemine tagab sujuva kasutajakogemuse, kus kasutajad ei pea teadma MCP rakenduse põhiteavet

Täielik koodinäide:

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

Siin toimub suurem osa tööst. Kutsub LLM-i esialgse kasutaja põhimõttega, seejärel töötleb vastust, et näha, kas mõni tööriist vajab kutsumist. Kui jah, siis kutsub need tööriistad ja jätkab vestlust LLM-iga, kuni tööriistakutsed lõpevad ja on lõplik vastus.


Me teeme mitu päringut LLM-ile, nii et määratleme funktsiooni, mis haldab LLM kutsumist. Lisa oma faili `main.rs` järgmine funktsioon:

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

See funktsioon võtab vastu LLM kliendi, sõnumite loendi (sh kasutaja prompti), tööriistad MCP serverist ja saadab päringu LLM-ile, tagastades vastuse.

LLM-i vastus sisaldab valikute (`choices`) massiivi. Me peame tulemust töötlema, et näha, kas esineb `tool_calls`. See annab meile teada, et LLM soovib konkreetse tööriista kutsumist koos argumentidega. Lisa oma faili `main.rs` faili lõppu järgmine kood, et määratleda funktsioon LLM vastuse töötlemiseks:

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

    // Trüki sisu, kui see on saadaval
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Töötle tööriista kutsumisi
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

        // Jätka vestlust tööriistade tulemustega
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

Kui `tool_calls` on olemas, eraldab see tööriista info, kutsub MCP serverit tööriista päringuga ja lisab tulemused vestluse sõnumitesse. Seejärel jätkub vestlus LLM-iga ning sõnumid uuendatakse assistendi vastuse ja tööriistakutse tulemustega.

Et eraldada tööriistakutse info, mida LLM MCP kutsedeks tagastab, lisame veel ühe abifunktsiooni, mis eraldab kõik vajaliku kõne tegemiseks. Lisa oma faili `main.rs` järgmine kood:

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

Kõik osad paigas olles saame nüüd töödelda esialgset kasutajaprompti ning kutsuda LLM-i. Uuenda oma `main` funktsiooni järgmise koodiga:

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

See pärib LLM-ilt esialgse kasutajaprompti, milles küsitakse kahe arvu summat, ja töötleb vastuse, et dünaamiliselt tööriistakutsusid hallata.

Suurepärane, sa tegid ära!

## Ülesanne

Võta harjutuse kood ja ehita serverisse veel mõningaid tööriistu. Seejärel loo klient LLM-iga nagu harjutuses ning testi seda erinevate promptidega, et veenduda, et kõik serveri tööriistad kutsutakse dünaamiliselt. Selline kliendi ülesehitamine tagab lõppkasutajale suurepärase kogemuse, kuna tema saab kasutada promte täpsete kliendi käskude asemel ning jääda MCP serveri päringutest teadmatuks.

## Lahendus

[Lahendus](./solution/README.md)

## Peamised õppetunnid

- LLM lisamine oma kliendile võimaldab kasutajatel MCP serveritega paremini suhelda.
- Pead teisendama MCP serveri vastuse millekski, mida LLM mõistab.

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulaator](../../../../03-GettingStarted/samples/rust)

## Lisavarustus

## Mis järgmiseks

- Järgmine: [Serveri kasutamine Visual Studio Code'is](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->