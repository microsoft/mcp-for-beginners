# Kliendi loomine LLM-iga

Siiani olete näinud, kuidas luua serverit ja klienti. Klient on suutnud serverit otseselt kutsuda, et loetleda selle tööriistu, ressursse ja prompt'e. Kuid see pole väga praktiline lähenemine. Teie kasutaja elab agendi ajastul ja ootab, et saaks kasutada prompt'e ja suhelda LLM-iga. Teie kasutajale ei ole oluline, kas te kasutate MCP-d oma võimete salvestamiseks või mitte, kuid nad ootavad loomuliku keele kasutamist suhtlemiseks. Kuidas me seda lahendame? Lahendus seisneb LLM-i lisamises kliendile.

## Ülevaade

Selles õppetükis keskendume LLM-i lisamisele teie kliendile ja näitame, kuidas see pakub teie kasutajale palju paremat kogemust.

## Õpieesmärgid

Selle õppetüki lõpuks oskate:

- Luua kliendi koos LLM-iga.
- Sujuvalt suhelda MCP serveriga, kasutades LLM-i.
- Pakkuda kliendi poolel paremat lõppkasutajakogemust.

## Lähenemine

Proovime mõista, millist lähenemist peame kasutama. LLM-i lisamine tundub lihtne, kuid kas me tegelikult teeme seda?

Siin on, kuidas klient suhtleb serveriga:

1. Loob ühenduse serveriga.

1. Loetleb võimed, prompt'id, ressursid ja tööriistad ning salvestab nende skeemi.

1. Lisab LLM-i ja edastab salvestatud võimed ja nende skeemi vormingus, mida LLM mõistab.

1. Töötleb kasutaja prompt'i, edastades selle koos kliendi poolt loetletud tööriistadega LLM-ile.

Suurepärane, nüüd kui mõistame, kuidas seda kõrgtasemel teha, proovime seda alljärgnevas harjutuses.

## Harjutus: Kliendi loomine LLM-iga

Selles harjutuses õpime lisama LLM-i oma kliendile.

### Autentimine GitHubi isikliku juurdepääsutokeniga

GitHubi tokeni loomine on lihtne protsess. Siin on, kuidas seda teha:

- Minge GitHubi seadistustesse – klõpsake paremas ülanurgas oma profiilipildil ja valige Seaded.
- Navigeerige arendaja seadistustesse – kerige alla ja klõpsake Arendaja seaded.
- Valige Isikliku juurdepääsu tokenid – klõpsake Peenhäälestatud tokenid ja seejärel Loo uus token.
- Konfigureerige oma token – lisage viide, määrake aegumiskuupäev ja valige vajalikud õigused (load). Sel juhul lisage kindlasti Models õigused.
- Looge ja kopeerige token – klõpsake Loo token ja veenduge, et kopeerite selle kohe, sest hiljem seda enam näha ei saa.

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
- Loonud klassi kahe liikmega, `client` ja `openai`, mis aitavad meil hallata klienti ja suhelda LLM-iga vastavalt.
- Konfigureerinud oma LLM-i instantsi kasutama GitHubi mudeleid, määrates `baseUrl` viitama inference API-le.

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

- Impordinud MCP jaoks vajalikud teegid
- Loonud kliendi

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

Esmalt peate lisama LangChain4j sõltuvused oma `pom.xml` faili. Lisage need sõltuvused, et lubada MCP integratsioon ja GitHubi mudelite tugi:

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

- **Lisanud LangChain4j sõltuvused**: vajalikud MCP integratsiooniks, OpenAI ametlikuks kliendiks ja GitHubi mudelite toeks
- **Impordinud LangChain4j teegid**: MCP integratsiooni ja OpenAI vestlusmudeli funktsionaalsuse jaoks
- **Loonud `ChatLanguageModel`**: konfigureeritud kasutama GitHubi mudeleid koos teie GitHubi tokeniga
- **Seadistanud HTTP transpordi**: kasutades Server-Sent Events (SSE) ühenduse loomiseks MCP serveriga
- **Loonud MCP kliendi**: mis haldab suhtlust serveriga
- **Kasutanud LangChain4j sisseehitatud MCP tuge**: mis lihtsustab LLM-ide ja MCP serverite integratsiooni

#### Rust

See näide eeldab, et teil töötab Rust-põhine MCP server. Kui teil seda pole, vaadake tagasi [01-first-server](../01-first-server/README.md) õppetükki, et server luua.

Kui teil on Rust MCP server, avage terminal ja liikuge samasse kataloogi, kus server asub. Seejärel käivitage järgmine käsk, et luua uus LLM kliendi projekt:

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
> Rustile pole ametlikku OpenAI teeki, kuid `async-openai` crate on [kogukonna hooldatav teek](https://platform.openai.com/docs/libraries/rust#rust), mida sageli kasutatakse.

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

    // TODO: LLM vestlus tööriistakutsete abil

    Ok(())
}
```

See kood seab üles lihtsa Rusti rakenduse, mis ühendub MCP serveri ja GitHubi mudelitega LLM suhtluseks.

> [!IMPORTANT]
> Veenduge, et enne rakenduse käivitamist oleks seatud keskkonnamuutuja `OPENAI_API_KEY` teie GitHubi tokeniga.

Suurepärane, järgmise sammuna loetleme serveri võimed.

### -2- Serveri võimete loetelu

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

- Lisanud koodi serveriga ühenduse loomiseks, `connectToServer`.
- Loonud `run` meetodi, mis vastutab meie rakenduse voo haldamise eest. Seni loetleb see ainult tööriistu, kuid lisame varsti rohkem.

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

Siin on, mida lisasime:

- Loetlesime ressursid ja tööriistad ning printisime need välja. Tööriistade puhul loetleme ka `inputSchema`, mida kasutame hiljem.

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

- Loetlenud MCP serveri saadaval olevad tööriistad
- Iga tööriista kohta loetlenud nime, kirjelduse ja selle skeemi. Viimane on midagi, mida kasutame tööriistade kutsumiseks varsti.

#### Java

```java
// Loo tööriistapakkuja, mis avastab automaatselt MCP tööriistad
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP tööriistapakkuja haldab automaatselt:
// - MCP serverist saadaolevate tööriistade nimekirja koostamine
// - MCP tööriistade skeemide teisendamine LangChain4j formaati
// - Tööriistade täitmise ja vastuste haldamine
```

Eelnevas koodis oleme:

- Loonud `McpToolProvider`, mis automaatselt avastab ja registreerib kõik MCP serveri tööriistad
- Tööriistapakkuja haldab MCP tööriistade skeemide ja LangChain4j tööriistavormingu konverteerimist sisemiselt
- See lähenemine varjab käsitsi tööriistade loetlemise ja konverteerimise protsessi

#### Rust

MCP serverist tööriistade pärimine toimub meetodiga `list_tools`. Oma `main` funktsioonis, pärast MCP kliendi seadistamist, lisage järgmine kood:

```rust
// Hangi MCP tööriistade nimekiri
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Serveri võimete konverteerimine LLM tööriistadeks

Järgmine samm pärast serveri võimete loetlemist on nende konverteerimine vormingusse, mida LLM mõistab. Kui me seda teeme, saame need võimed pakkuda LLM-ile tööriistadena.

#### TypeScript

1. Lisage järgmine kood, et konverteerida MCP serveri vastus tööriista vormingusse, mida LLM saab kasutada:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Loo zod skeem sisendiskeemi põhjal
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Määra tüübiks selgesõnaliselt "function"
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

    Ülaltoodud kood võtab MCP serveri vastuse ja konverteerib selle tööriista definitsiooni vormingusse, mida LLM mõistab.

1. Uuendame nüüd `run` meetodit, et loetleda serveri võimed:

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

    Eelnevas koodis uuendasime `run` meetodit, et läbida tulemus ja iga kirje puhul kutsuda `openAiToolAdapter`.

#### Python

1. Loome esmalt järgmise konverteri funktsiooni

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

    Funktsioonis `convert_to_llm_tools` võtame MCP tööriista vastuse ja konverteerime selle vormingusse, mida LLM mõistab.

1. Järgmiseks uuendame oma kliendi koodi, et kasutada seda funktsiooni nii:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Siin lisame kutse `convert_to_llm_tool`-ile, et konverteerida MCP tööriista vastus millekski, mida saame hiljem LLM-ile anda.

#### .NET

1. Lisame koodi, mis konverteerib MCP tööriista vastuse millekski, mida LLM mõistab

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
- Määratlenud funktsionaalsuse, mis loob `FunctionDefinition`-i, mis antakse edasi `ChatCompletionsDefinition`-ile. Viimane on midagi, mida LLM mõistab.

1. Vaatame, kuidas saame olemasolevat koodi uuendada, et kasutada seda funktsiooni:

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
- Kasutanud LangChain4j `AiServices`-i, et automaatselt siduda LLM MCP tööriistapakkujaga
- Raamistik haldab automaatselt tööriistade skeemi konverteerimist ja funktsioonide kutsumist taustal
- See lähenemine elimineerib käsitsi tööriistade konverteerimise – LangChain4j haldab kogu MCP tööriistade LLM-iga ühilduvaks muutmise keerukuse

#### Rust

MCP tööriista vastuse konverteerimiseks LLM mõistetavasse vormingusse lisame abifunktsiooni, mis vormindab tööriistade loendi. Lisage järgmine kood oma `main.rs` faili `main` funktsiooni alla. Seda kutsutakse LLM päringute tegemisel:

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

Suurepärane, nüüd oleme valmis kasutajapäringute töötlemiseks, nii et tegeleme sellega järgmisena.

### -4- Kasutaja prompt'i päringu töötlemine

Selles koodiosas töötleme kasutaja päringuid.

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
        // TEGEMATA

        }
    }
    ```

    Eelnevas koodis oleme:

    - Lisanud meetodi `callTools`.
    - Meetod võtab LLM vastuse ja kontrollib, milliseid tööriistu on kutsutud, kui üldse:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // tööriista kutsumine
        }
        ```

    - Kutsub tööriista, kui LLM näitab, et see tuleks kutsuda:

        ```typescript
        // 2. Kutsu serveri tööriista
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tee midagi tulemusega
        // TEGEMATA
        ```

1. Uuendage `run` meetodit, et lisada LLM-i kutsed ja `callTools` kutsumine:

    ```typescript

    // 1. Loo sõnumid, mis on LLM-i sisendiks
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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Läbi vaata LLM-i vastus, iga valiku puhul kontrolli, kas seal on tööriista kutsed
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
            baseURL: "https://models.inference.ai.azure.com", // võib tulevikus vaja minna seda URL-i muuta: https://models.github.ai/inference
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
            type: "function" as const, // Sea tüüp selgesõnaliselt "function"
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
    
    
          // 2. Kutsu serveri tööriista
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Tee midagi tulemusega
          // TEE TEHTAV
    
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
    
        // 1. Läbi LLM vastuse, iga valiku puhul kontrolli, kas seal on tööriista kutsed
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
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Järgmisena lisame funktsiooni, mis kutsub LLM-i:

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

    - Edastanud oma funktsioonid, mille leidsime MCP serverist ja konverteerisime, LLM-ile.
    - Seejärel kutsusime LLM-i nende funktsioonidega.
    - Seejärel kontrollime tulemust, et näha, milliseid funktsioone peaksime kutsuma, kui üldse.
    - Lõpuks edastame funktsioonide massiivi kutsumiseks.

1. Viimane samm, uuendame oma põhikoodi:

    ```python
    prompt = "Add 2 to 20"

    # küsi LLM-ilt, milliseid tööriistu kasutada, kui üldse
    functions_to_call = call_llm(prompt, functions)

    # kutsu soovitatud funktsioonid välja
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Seal see on, see oli viimane samm, ülaltoodud koodis me:

    - Kutsume MCP tööriista läbi `call_tool` kasutades funktsiooni, mida LLM arvas, et peaksime kutsuma vastavalt meie prompt'ile.
    - Trükime tööriista kutse tulemuse MCP serverile.

#### .NET

1. Näitame koodi, mis teeb LLM prompt'i päringu:

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

    Eelnevas koodis oleme:

    - Hangi tööriistad MCP serverist, `var tools = await GetMcpTools()`.
    - Määratlesime kasutaja prompt'i `userMessage`.
    - Konstrukteerisime valikute objekti, mis määrab mudeli ja tööriistad.
    - Tegime päringu LLM-ile.

1. Viimane samm, vaatame, kas LLM arvab, et peaksime funktsiooni kutsuma:

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

    - Läbinud funktsioonikõnede nimekirja.
    - Iga tööriistakutse puhul eraldanud nime ja argumendid ning kutsunud tööriista MCP serveris MCP kliendi abil. Lõpuks trükime tulemused.

Siin on kogu kood tervikuna:

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
    // Täida loomuliku keele päringud, mis kasutavad automaatselt MCP tööriistu
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

- Kasutanud lihtsaid loomuliku keele prompt'e MCP serveri tööriistadega suhtlemiseks
- LangChain4j raamistik haldab automaatselt:
  - Kasutajapromptide konverteerimist tööriistakutseteks vajadusel
  - Sobivate MCP tööriistade kutsumist LLM otsuse põhjal
  - Vestluse voogu LLM-i ja MCP serveri vahel
- `bot.chat()` meetod tagastab loomuliku keele vastuseid, mis võivad sisaldada MCP tööriistade täitmise tulemusi
- See lähenemine pakub sujuvat kasutajakogemust, kus kasutajad ei pea teadma MCP aluseks olevat rakendust

Täielik koodinäide:

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

Siin toimub enamik tööd. Kutsume LLM-i algse kasutajaprompt'iga, seejärel töötleme vastust, et näha, kas mõnda tööriista tuleb kutsuda. Kui jah, kutsume need tööriistad ja jätkame vestlust LLM-iga, kuni tööriistakutsed lõpevad ja meil on lõplik vastus.

Teeme mitu LLM-i kutset, nii et määratleme funktsiooni, mis haldab LLM-i kutset. Lisage järgmine funktsioon oma `main.rs` faili:

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

See funktsioon võtab LLM kliendi, sõnumite nimekirja (sh kasutajaprompt), MCP serveri tööriistad ja saadab LLM-ile päringu, tagastades vastuse.
LLM-i vastus sisaldab massiivi `choices`. Peame tulemuse töötlema, et näha, kas esinevad `tool_calls`. See annab meile teada, et LLM soovib, et konkreetne tööriist kutsutakse argumentidega. Lisa järgmine kood oma `main.rs` faili lõppu, et defineerida funktsioon LLM-i vastuse töötlemiseks:

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

    // Töötle tööriista kutsed
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

Kui `tool_calls` on olemas, ekstraheerib see tööriista info, kutsub MCP serverit tööriista päringuga ja lisab tulemused vestluse sõnumitesse. Seejärel jätkub vestlus LLM-iga ning sõnumid uuendatakse assistendi vastuse ja tööriista kutse tulemustega.

Selleks, et ekstraheerida tööriista kutse infot, mida LLM tagastab MCP kutsete jaoks, lisame teise abifunktsiooni, mis võtab välja kõik vajaliku kutse tegemiseks. Lisa järgmine kood oma `main.rs` faili lõppu:

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

Kõik tükid paigas, saame nüüd töödelda esialgset kasutaja prompti ja kutsuda LLM-i. Uuenda oma `main` funktsiooni, et see sisaldaks järgmist koodi:

```rust
// LLM vestlus tööriistakutsete abil
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

See küsib LLM-ilt esialgset kasutaja prompti, kus palutakse kahe arvu summa, ja töötleb vastust, et dünaamiliselt tööriistakutseid hallata.

Suurepärane, sa tegid selle ära!

## Ülesanne

Võta harjutusest kood ja ehita server välja veel mõne tööriistaga. Seejärel loo klient LLM-iga, nagu harjutuses, ja testi seda erinevate promptidega, et veenduda, et kõik sinu serveri tööriistad kutsutakse dünaamiliselt. Selline kliendi ehitamise viis tagab lõppkasutajale suurepärase kasutajakogemuse, kuna nad saavad kasutada prompt'e täpsete kliendikäskude asemel ning ei pea teadma, et MCP serverit kutsutakse.

## Lahendus

[Lahendus](/03-GettingStarted/03-llm-client/solution/README.md)

## Peamised õppetunnid

- LLM-i lisamine oma kliendile annab kasutajatele parema võimaluse suhelda MCP serveritega.
- Pead teisendama MCP serveri vastuse millekski, mida LLM mõistab.

## Näited

- [Java kalkulaator](../samples/java/calculator/README.md)
- [.Net kalkulaator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulaator](../samples/javascript/README.md)
- [TypeScript kalkulaator](../samples/typescript/README.md)
- [Python kalkulaator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulaator](../../../../03-GettingStarted/samples/rust)

## Täiendavad ressursid

## Mis järgmiseks

- Järgmine: [Serveri kasutamine Visual Studio Code abil](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->