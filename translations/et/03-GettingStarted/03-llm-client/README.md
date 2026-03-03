# Kliendi loomine koos LLM-iga

Nii kaugele on näidatud, kuidas luua serverit ja klienti. Klient on suutnud serverit otseselt kutsuda, et loetleda selle tööriistu, ressursse ja käivitusi. Kuid see pole väga praktiline lähenemine. Teie kasutajad elavad agendi ajastul ja ootavad, et nad saaksid kasutada käivitusi ja suhelda LLM-iga. Neid ei huvita, kas te kasutate MCP-d oma võimete hoidmiseks; nad lihtsalt ootavad loomulikus keeles suhtlemist. Kuidas me seda lahendame? Lahendus on lisada kliendile LLM.

## Ülevaade

Selles õppetükis keskendume LLM-i lisamisele kliendile ja näitame, kuidas see pakub kasutajale palju paremat kogemust.

## Õpieesmärgid

Selle õppetüki lõpuks oskate:

- Luua kliendi, kellel on LLM.
- Sujuvalt suhelda MCP serveriga LLM-i abil.
- Pakkuda kliendi poolel paremat lõppkasutaja kogemust.

## Lähenemine

Proovime mõista, millist lähenemist peame järgima. LLM-i lisamine kõlab lihtsalt, kuid kas me tõepoolest nii teeme?

Näide sellest, kuidas klient suhtleb serveriga:

1. Luuakse ühendus serveriga.

1. Loetletakse võimed, käivitused, ressursid ja tööriistad ning salvestatakse nende skeem.

1. Lisatakse LLM ja antakse salvestatud võimed ja skeem vormingus üle, mida LLM mõistab.

1. Käsitletakse kasutaja käivitust, edastades selle LLM-ile koos kliendi poolt loetletud tööriistadega.

Suurepärane, nüüd kui mõistame, kuidas seda üldiselt teha, proovime seda alljärgnevas ülesandes.

## Ülesanne: Kliendi loomine koos LLM-iga

Selles ülesandes õpime lisama meie kliendile LLM-i.

### Autentimine GitHubi isikliku juurdepääsutunnusega

GitHubi tunnuse loomine on lihtne protsess. Siin on, kuidas seda teha:

- Minge GitHubi sätetesse – klõpsake üleval paremas nurgas oma profiilipilti ja valige Settings.
- Navigeerige arendaja sätetesse – kerige alla ja klõpsake Developer Settings.
- Valige isiklikud juurdepääsutunnused – klõpsake Fine-grained tokens ja seejärel Generate new token.
- Konfigureerige oma tunnus – lisage viide, määrake aegumiskuupäev ja valige vajalikud õigused (loalused). Sel juhul lisage kindlasti Models-luba.
- Genereerige ja kopeerige tunnus – klõpsake Generate token ja kopeerige see kohe, kuna hiljem seda enam ei näe.

### -1- Ühenduse loomine serveriga

Loome esmalt kliendi:

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
- Loonud klassi kahe liikmega, `client` ja `openai`, mis aitavad meil hallata klienti ja suhelda LLM-iga vastavalt
- Konfigureerinud oma LLM-eksemplari kasutama GitHub Models-e, seatud `baseUrl` suunama inference API-le

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
            # Algata ühendus
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Eelnevas koodis oleme:

- Importinud MCP vajalikke teeke
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

Kõigepealt peate lisama LangChain4j sõltuvused oma `pom.xml` faili. Lisage need sõltuvused, et võimaldada MCP integratsiooni ja GitHub Models toe kasutamist:

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

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // Konfigureeri LLM kasutama GitHubi mudeleid
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
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
}
```

Eelnevas koodis oleme:

- **Lisanud LangChain4j sõltuvused**: MCP integratsiooni, OpenAI ametliku kliendi ja GitHub Models toe jaoks
- **Importinud LangChain4j teegid**: MCP integratsiooni ja OpenAI vestlusmootori funktsionaalsuse jaoks
- **Loonud `ChatLanguageModel`**: Konfigureeritud kasutama GitHub Models-i teie GitHubi tunnusega
- **Seadistanud HTTP transpordi**: Server-Sent Events (SSE) kasutades MCP serveriga ühenduse loomiseks
- **Loonud MCP kliendi**: Mis haldab suhtlust serveriga
- **Kasutanud LangChain4j sisseehitatud MCP tuge**: Mis lihtsustab LLM-ide ja MCP serverite integratsiooni

#### Rust

See näide eeldab, et teil jookseb Rust-põhine MCP server. Kui teil pole, vaadake tagasi [01-first-server](../01-first-server/README.md) õppetükki, et server luua.

Kui teil on Rust MCP server, avage terminal ja navigeerige serveri kausta. Käivitage järgmine käsk uue LLM kliendi projekti loomiseks:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Lisage oma `Cargo.toml` failile järgmised sõltuvused:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Rustil pole ametlikku OpenAI teeki, kuid `async-openai` hermi on [kogukonna hallatav teek](https://platform.openai.com/docs/libraries/rust#rust), mida kasutatakse laialdaselt.

Avage faili `src/main.rs` ja asendage selle sisu järgmise koodiga:

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
    // Esialgne sõnum
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

    // TEHA: Hangi MCP tööriistade nimekiri

    // TEHA: LLM vestlus tööriistakutsetega

    Ok(())
}
```

See kood seab üles lihtsa Rusti rakenduse, mis loob ühenduse MCP serveri ja GitHub Models-iga LLM interaktsioonide jaoks.

> [!IMPORTANT]
> Veenduge, et seadistate keskkonnamuutujaks `OPENAI_API_KEY` oma GitHubi tunnuse enne rakenduse käivitamist.

Suurepärane, järgmine samm on loetleda serveri võimed.

### -2- Loetle serveri võimed

Nüüd ühendume serveriga ja küsime selle võimeid:

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

    // tööriistade loetelu
    const toolsResult = await this.client.listTools();
}
```

Eelnevas koodis oleme:

- Lisanud ühenduse loomise koodi serveriga, `connectToServer`.
- Loonud `run` meetodi, mis haldab rakenduse voogu. Praegu loetleb see ainult tööriistu, kuid varsti lisame sinna veel.

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

Siin oleme lisanud:

- Ressursside ja tööriistade loetlemine ja nende väljakirjutamine. Tööriistade puhul loetleme ka `inputSchema`, mida hiljem kasutame.

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

- Loetlenud MCP serveri tööriistad
- Iga tööriista kohta loetlenud nime, kirjelduse ja selle skeemi. Viimatist kasutame varsti tööriistade kutsumiseks.

#### Java

```java
// Loo tööriistade pakkuja, mis avastab automaatselt MCP tööriistad
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP tööriistade pakkuja haldab automaatselt:
// - MCP serverist saadaval olevate tööriistade loetelu
// - MCP tööriistade skeemide teisendamine LangChain4j formaati
// - Tööriistade täitmise ja vastuste haldamine
```

Eelnevas koodis oleme:

- Loonud `McpToolProvider`, mis automaatselt avastab ja registreerib kõik MCP serveri tööriistad
- Tööriistapakkuja tegeleb MCP tööriistade skeemide ja LangChain4j tööriistavormingu vahetamisega sisemiselt
- See lähenemine vabastab meid käsitsi tööriistade loetlemisest ja konverteerimisest

#### Rust

Tööriistade tagastamine MCP serverist toimub `list_tools` meetodiga. Oma `main` funktsiooni MCP kliendi seadistamise järel lisage järgmine kood:

```rust
// Hangi MCP tööriistade nimekiri
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Muutke serveri võimed LLM tööriistadeks

Järgmine samm pärast serveri võimete loetlemist on teisendada need LLM-le arusaadavasse vormingusse. Kui see tehtud, saame pakkuda neid võimeid LLM-i tööriistadena.

#### TypeScript

1. Lisage järgmine kood MCP serveri vastuse teisendamiseks tööriistavorminguks, mida LLM kasutada saab:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Loo zod skeem vastavalt sisendiskeemile
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Määra tüüp selgelt "function"
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

    Ülaltoodud kood võtab MCP serveri vastuse ja teisendab selle tööriistade definitsiooniks, mida LLM mõistab.

1. Uuendame nüüd `run` meetodit, et kuvada serveri võimeid:

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

    Eelnevas koodis uuendasime `run` meetodit nii, et see kaardistab tulemuse ja igale üksusele kutsub `openAiToolAdapter`.

#### Python

1. Kõigepealt loome järgmise teisendusfunktsiooni

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

    Ülaltoodud `convert_to_llm_tools` funktsioon võtab MCP tööriista vastuse ja teisendab selle LLM-i mõistetavasse vormingusse.

1. Järgmisena uuendame koodis klienti nii, et see kasutab seda funktsiooni:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Siin lisame kõne `convert_to_llm_tool`, et teisendada MCP tööriista vastus selliseks, mida hiljem LLM-i saab anda.

#### .NET

1. Lisame koodi, mis konverteerib MCP tööriista vastuse LLM-i arusaadavaks

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
- Defineerinud funktsionaalsuse, mis loob FunctionDefinition, mida antakse ChatCompletionsDefinitionile. Viimane on mida LLM mõistab.

1. Uuendame olemasolevat koodi, et kasutada seda funktsiooni:

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
// Loo Bot-liides loomuliku keele suhtluseks
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

- Defineerinud lihtsa `Bot` liidese loomuliku keele suhtluseks
- Kasutanud LangChain4j `AiServices`-i, et automaatselt siduda LLM MCP tööriistapakkujaga
- Raamistik haldab tööriistade skeemi teisendust ja funktsioonikõnesid automaatselt
- See lähenemine kõrvaldab käsitsi tööriistade teisendamise – LangChain4j tegeleb kõigi MCP tööriistade LLM-iga ühilduvaks vormindamiseks vajalikuga

#### Rust

MCP tööriista vastuse teisendamiseks LLM-le arusaadavaks vorminguks lisame abifunktsiooni, mis vormindab tööriistade nimekirja. Lisage oma `main.rs` faili järgmine kood allpool `main` funktsiooni. Seda kutsutakse LLM-i päringute tegemisel:

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

Suurepärane, nüüd oleme valmis kasutajapäringuid haldama, sellega tegeleme järgmisena.

### -4- Kasutaja päringu haldamine

Selles koodiosas käsitleme kasutaja päringuid.

#### TypeScript

1. Lisage meetod, mida kasutatakse LLM-i kutsumiseks:

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

    Eelnevas koodis oleme:

    - Lisanud meetodi `callTools`.
    - Meetod võtab LLM vastuse ja kontrollib, kas tööriistu kutsuti, ning kui kutsuti, milliseid:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // tööriista kutsumine
        }
        ```

    - Kutsume tööriista, kui LLM näitab, et seda tuleks kutsuda:

        ```typescript
        // 2. Kutsuge serveri tööriist
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tehke midagi tulemusega
        // TEHA
        ```

1. Uuendame `run` meetodi nii, et see sisaldab LLM-i väljakutseid ja `callTools` kutsumist:

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

    // 3. Läbi vaata LLM vastus, iga valiku puhul kontrolli, kas seal on tööriistakõnesid
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Suurepärane, siin on kogu kood koos:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importige zod skeemi valideerimiseks

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // võib tulevikus vaja minna muuta selleks url-iks: https://models.github.ai/inference
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
          // Looge zod skeem sisend_skeemi põhjal
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Määrake tüübi väärtuseks selgelt "function"
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
    
    
          // 2. Kutsuge serveri tööriista
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Tehke tulemusega midagi
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
    
        // 1. Läbige LLM vastus, kontrollige iga valiku puhul, kas on tööriistakutseid
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

1. Lisame vajalikud importimised, et kasutada LLM-i kutsumist

    ```python
    # keelendusmudel
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Seejärel lisame funktsiooni, mis kutsub LLM-i:

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

    - Anname oma funktsioonid, mille leidsime MCP serverilt ja teisendasime, LLM-i kätte.
    - Kutsub LLM-i nendega.
    - Kontrollime tulemust, et näha, kas ja milliseid funktsioone peaks kutsuma.
    - Lõpuks edastame funktsioonide massiivi kutseteks.

1. Viimane samm, uuendame põhikoodi:

    ```python
    prompt = "Add 2 to 20"

    # küsi LLM-ilt, milliseid tööriistu kõigile, kui üldse
    functions_to_call = call_llm(prompt, functions)

    # kutsu esitatud funktsioone
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Seal, see oli viimane samm, ülal olevas koodis oleme:

    - Kutsunud MCP tööriista `call_tool` kaudu, kasutades LLM-i poolt leitud funktsiooni, mis põhines meie päringul.
    - Väljastanud tööriista kutsutulemus MCP serverile.

#### .NET

1. Näitame koodi LLM-i päringu tegemiseks:

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

    - Hanginud MCP serveri tööriistad, `var tools = await GetMcpTools()`.
    - Defineerinud kasutaja käivituse `userMessage`.
    - Konstrukteerinud optsioonid mudelile ja tööriistadele.
    - Teinud päringu LLM-i suunas.

1. Viimane samm, kontrollime, kas LLM arvab, et peaks funktsiooni kutsuma:

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

    - Läbinud funktsiooni kutsed.
    - Iga tööriista puhul parsinud nime ja argumendid ning kutsunud tööriista MCP serveris kasutades MCP klienti. Lõpuks trükime tulemuse.

Siin on kogu kood:

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
    // Täida loomuliku keele päringuid, mis automaatselt kasutavad MCP tööriistu
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

- Kasutanud lihtsaid loomuliku keele päringuid MCP serveri tööriistadega suhtlemiseks
- LangChain4j raamistik haldab automaatselt:
  - Kasutaja päringute teisendamist tööriistakõnedeks vajadusel
  - Vastavate MCP tööriistade kutsumist LLM-i otsusest lähtuvalt
  - Vestluse voogu LLM-i ja MCP serveri vahel
- `bot.chat()` meetod tagastab loomulikus keeles vastuseid, mis võivad sisaldada MCP tööde tulemusi
- See pakkumõle sujuva kasutajakogemuse, kus kasutajaid ei pea MCP taustsüsteemi kohta teadma

Täielik koodi näide:

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

Siin toimub töö suur osa. Kutsume LLM-i algse kasutajapäringuga, seejärel töötleme vastuse, et näha, kas mõnda tööriista tuleb kutsuda. Kui jah, kutsume need tööriistad ja jätkame vestlust LLM-iga, kuni rohkem tööriistakutseid vaja pole ja meil on lõplik vastus.

Teeme mitmeid LLM-kõnesid, seega defineerime funktsiooni, mis haldab LLM-i kutsumist. Lisage oma `main.rs` faili järgmine funktsioon:

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

See funktsioon võtab LLM kliendi, sõnumite loendi (sealhulgas kasutajapäringu), MCP serveri tööriistad ja saadab LLM-ile päringu, tagastades vastuse.
LLM-i vastus sisaldab massiivi `choices`. Peame tulemust töötlema, et näha, kas esineb `tool_calls`. See ütleb meile, et LLM palub konkreetset tööriista kutsuda koos argumentidega. Lisa järgmine kood oma faili `main.rs` lõppu, et määratleda funktsioon LLM-i vastuse käsitlemiseks:

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

    // Töötle tööriistakõnesid
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Lisa assistendi sõnum

        // Täida iga tööriistakutse
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
  
Kui `tool_calls` esinevad, ekstraheerib see tööriista informatsiooni, kutsub MCP serveri tööriistapäringuga ja lisab tulemused vestluse sõnumitesse. Seejärel jätkab vestlust LLM-iga ning sõnumid uuendatakse assistendi vastuse ja tööriistakutse tulemustega.

Tööriistakutseinfo ekstraheerimiseks, mida LLM tagastab MCP kutsete jaoks, lisame teise abifunktsiooni, mis võtab välja kõik vajaliku kutse tegemiseks. Lisa järgmine kood faili `main.rs` lõppu:

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
  
Kõik osad paigas, saame nüüd hallata esialgset kasutajakäsku ja kutsuda LLM-i. Uuenda oma `main` funktsiooni järgnevaga:

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
  
See küsib LLM-i esialgse kasutajakäsuga, mis palub kahe arvu summa, ja töötab vastuse läbi, et dünaamiliselt tööriistakutseid hallata.

Suurepärane, tegid ära!

## Ülesanne

Võta harjutusest saadud kood ja ehita server välja täiendavate tööriistadega. Seejärel loo klient LLM-iga, nagu harjutuses, ja testi seda erinevate käskudega, et veenduda, et kõik sinu serveri tööriistad kutsutakse dünaamiliselt. Selline kliendi ehitamise viis tagab kasutajale suurepärase kogemuse, kuna nad saavad kasutada käske, mitte täpseid kliendikäsklusi, jäädes samal ajal teadmatusse mistahes MCP serveri kutsete kohta.

## Lahendus

[Lahendus](/03-GettingStarted/03-llm-client/solution/README.md)

## Peamised õppetunnid

- LLM-i lisamine kliendile annab kasutajatele parema võimaluse suhelda MCP serveritega.
- MCP serveri vastus tuleb konverteerida LLM-i mõistetavaks.

## Näidised

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulaator](../../../../03-GettingStarted/samples/rust)

## Täiendavad ressursid

## Mis edasi

- Järgmine: [Serveri kasutamine Visual Studio Code'iga](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle emakeeles tuleks lugeda usaldusväärseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->