# Kliento kūrimas su LLM

Iki šiol matėte, kaip sukurti serverį ir klientą. Klientas galėjo aiškiai kreiptis į serverį, kad išvardintų jo įrankius, išteklius ir užklausas. Tačiau tai nėra labai praktiškas požiūris. Jūsų vartotojas gyvena agentiškoje eroje ir tikisi naudoti užklausas bei bendrauti su LLM tam. Jūsų vartotojui nesvarbu, ar naudojate MCP savo galimybėms saugoti, tačiau jie tikisi naudoti natūralią kalbą sąveikai. Kaip tai išspręsti? Sprendimas yra pridėti LLM prie kliento.

## Apžvalga

Šioje pamokoje sutelksime dėmesį į LLM pridėjimą prie kliento ir parodysime, kaip tai suteikia daug geresnę patirtį jūsų vartotojui.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Sukurti klientą su LLM.
- Sklandžiai bendrauti su MCP serveriu naudojant LLM.
- Užtikrinti geresnę galutinio vartotojo patirtį kliento pusėje.

## Požiūris

Pabandykime suprasti, kokį požiūrį turime taikyti. LLM pridėjimas skamba paprastai, bet ar tikrai tai padarysime?

Štai kaip klientas bendraus su serveriu:

1. Užmegzti ryšį su serveriu.

1. Išvardinti galimybes, užklausas, išteklius ir įrankius bei išsaugoti jų schemą.

1. Pridėti LLM ir perduoti išsaugotas galimybes bei jų schemą formatu, kurį LLM supranta.

1. Apdoroti vartotojo užklausą perduodant ją LLM kartu su kliento išvardytais įrankiais.

Puiku, dabar suprantame, kaip tai padaryti aukštu lygiu, pabandykime tai išbandyti žemiau pateiktame pratime.

## Pratimas: Kliento kūrimas su LLM

Šiame pratime išmoksime pridėti LLM prie mūsų kliento.

### Autentifikacija naudojant GitHub asmeninį prieigos raktą

GitHub rakto sukūrimas yra paprastas procesas. Štai kaip tai padaryti:

- Eikite į GitHub nustatymus – spustelėkite savo profilio nuotrauką viršutiniame dešiniajame kampe ir pasirinkite Nustatymai.
- Eikite į kūrėjų nustatymus – slinkite žemyn ir spustelėkite Kūrėjų nustatymai.
- Pasirinkite Asmeninius prieigos raktus – spustelėkite Smulkiai sukonfigūruoti raktai ir tada Generuoti naują raktą.
- Konfigūruokite savo raktą – pridėkite pastabą, nustatykite galiojimo datą ir pasirinkite reikalingas sritis (leidimus). Šiuo atveju būtinai pridėkite Models leidimą.
- Generuokite ir nukopijuokite raktą – spustelėkite Generuoti raktą ir būtinai iškart jį nukopijuokite, nes vėliau jo nematysite.

### -1- Prisijungimas prie serverio

Pirmiausia sukurkime savo klientą:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importuokite zod schemos validavimui

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

Ankstesniame kode mes:

- Importavome reikalingas bibliotekas
- Sukūrėme klasę su dviem nariais, `client` ir `openai`, kurie padės valdyti klientą ir bendrauti su LLM atitinkamai.
- Sukonfigūravome mūsų LLM egzempliorių naudoti GitHub Models, nustatydami `baseUrl`, kad jis rodytų į inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Sukurkite serverio parametrus stdio ryšiui
server_params = StdioServerParameters(
    command="mcp",  # Vykdomasis failas
    args=["run", "server.py"],  # Pasirinktiniai komandų eilutės argumentai
    env=None,  # Pasirinktiniai aplinkos kintamieji
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializuokite ryšį
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Ankstesniame kode mes:

- Importavome reikalingas MCP bibliotekas
- Sukūrėme klientą

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

Pirmiausia turėsite pridėti LangChain4j priklausomybes į savo `pom.xml` failą. Pridėkite šias priklausomybes, kad įgalintumėte MCP integraciją ir GitHub Models palaikymą:

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

Tada sukurkite savo Java kliento klasę:

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
    
    public static void main(String[] args) throws Exception {        // Konfigūruokite LLM naudoti GitHub modelius
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Sukurkite MCP transportą serverio prisijungimui
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Sukurkite MCP klientą
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Ankstesniame kode mes:

- **Pridėjome LangChain4j priklausomybes**: reikalingas MCP integracijai, oficialiam OpenAI klientui ir GitHub Models palaikymui
- **Importavome LangChain4j bibliotekas**: MCP integracijai ir OpenAI pokalbių modelio funkcionalumui
- **Sukūrėme `ChatLanguageModel`**: sukonfigūruotą naudoti GitHub Models su jūsų GitHub raktu
- **Nustatėme HTTP transportą**: naudojant Server-Sent Events (SSE) prisijungimui prie MCP serverio
- **Sukūrėme MCP klientą**: kuris tvarkys komunikaciją su serveriu
- **Naudojome LangChain4j įmontuotą MCP palaikymą**: kuris supaprastina integraciją tarp LLM ir MCP serverių

#### Rust

Šis pavyzdys daro prielaidą, kad turite Rust pagrindu veikiantį MCP serverį. Jei neturite, grįžkite prie [01-first-server](../01-first-server/README.md) pamokos, kad sukurtumėte serverį.

Kai turėsite savo Rust MCP serverį, atidarykite terminalą ir eikite į tą patį katalogą kaip serveris. Tada paleiskite šią komandą, kad sukurtumėte naują LLM kliento projektą:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Pridėkite šias priklausomybes į savo `Cargo.toml` failą:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Nėra oficialios Rust bibliotekos OpenAI, tačiau `async-openai` crate yra [bendruomenės palaikoma biblioteka](https://platform.openai.com/docs/libraries/rust#rust), kuri dažnai naudojama.

Atidarykite `src/main.rs` failą ir pakeiskite jo turinį šiuo kodu:

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
    // Pradinis pranešimas
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Nustatyti OpenAI klientą
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Nustatyti MCP klientą
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

    // TODO: Gauti MCP įrankių sąrašą

    // TODO: LLM pokalbis su įrankių kvietimais

    Ok(())
}
```

Šis kodas nustato pagrindinę Rust programą, kuri prisijungs prie MCP serverio ir GitHub Models LLM sąveikai.

> [!IMPORTANT]
> Prieš paleisdami programą būtinai nustatykite `OPENAI_API_KEY` aplinkos kintamąjį su savo GitHub raktu.

Puiku, kitas žingsnis – išvardinti serverio galimybes.

### -2- Išvardinti serverio galimybes

Dabar prisijungsime prie serverio ir paprašysime jo galimybių:

#### Typescript

Toje pačioje klasėje pridėkite šiuos metodus:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // įrankių sąrašas
    const toolsResult = await this.client.listTools();
}
```

Ankstesniame kode mes:

- Pridėjome kodą prisijungimui prie serverio, `connectToServer`.
- Sukūrėme `run` metodą, atsakingą už mūsų programos srautą. Iki šiol jis tik išvardina įrankius, bet netrukus pridėsime daugiau.

#### Python

```python
# Išvardinti turimus išteklius
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Išvardinti turimus įrankius
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Štai ką pridėjome:

- Išvardinome išteklius ir įrankius bei juos atspausdinome. Įrankiams taip pat išvardinome `inputSchema`, kurį naudosime vėliau.

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

Ankstesniame kode mes:

- Išvardinome įrankius, esančius MCP serveryje
- Kiekvienam įrankiui išvardinome pavadinimą, aprašymą ir jo schemą. Pastaroji bus naudojama netrukus kviečiant įrankius.

#### Java

```java
// Sukurkite įrankių tiekėją, kuris automatiškai aptinka MCP įrankius
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP įrankių tiekėjas automatiškai tvarko:
// - Galimų įrankių iš MCP serverio sąrašą
// - MCP įrankių schemų konvertavimą į LangChain4j formatą
// - Įrankių vykdymo ir atsakymų valdymą
```

Ankstesniame kode mes:

- Sukūrėme `McpToolProvider`, kuris automatiškai aptinka ir registruoja visus įrankius iš MCP serverio
- Įrankių tiekėjas viduje tvarko konvertavimą tarp MCP įrankių schemų ir LangChain4j įrankių formato
- Šis požiūris abstrahuoja rankinį įrankių išvardinimą ir konvertavimą

#### Rust

Įrankių gavimas iš MCP serverio atliekamas naudojant `list_tools` metodą. Savo `main` funkcijoje, po MCP kliento nustatymo, pridėkite šį kodą:

```rust
// Gauti MCP įrankių sąrašą
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Konvertuoti serverio galimybes į LLM įrankius

Kitas žingsnis po serverio galimybių išvardinimo yra jų konvertavimas į formatą, kurį LLM supranta. Kai tai padarysime, galėsime šias galimybes pateikti kaip įrankius mūsų LLM.

#### TypeScript

1. Pridėkite šį kodą, kad konvertuotumėte MCP serverio atsakymą į įrankio formatą, kurį LLM gali naudoti:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Sukurkite zod schemą pagal input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Aiškiai nustatykite tipą kaip "function"
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

    Aukščiau pateiktas kodas paima MCP serverio atsakymą ir konvertuoja jį į įrankio apibrėžimo formatą, kurį LLM gali suprasti.

1. Tada atnaujinkime `run` metodą, kad išvardintume serverio galimybes:

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

    Ankstesniame kode atnaujinome `run` metodą, kad jis pereitų per rezultatą ir kiekvienam įrašui iškvietė `openAiToolAdapter`.

#### Python

1. Pirmiausia sukurkime šią konvertavimo funkciją

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

    Aukščiau esančioje funkcijoje `convert_to_llm_tools` paimame MCP įrankio atsakymą ir konvertuojame jį į formatą, kurį LLM gali suprasti.

1. Tada atnaujinkime savo kliento kodą, kad naudotume šią funkciją taip:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Čia pridedame kvietimą `convert_to_llm_tool`, kad konvertuotume MCP įrankio atsakymą į kažką, ką vėliau galime perduoti LLM.

#### .NET

1. Pridėkime kodą, kuris konvertuos MCP įrankio atsakymą į formatą, kurį LLM gali suprasti

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

Ankstesniame kode mes:

- Sukūrėme funkciją `ConvertFrom`, kuri priima pavadinimą, aprašymą ir įvesties schemą.
- Apibrėžėme funkcionalumą, kuris sukuria `FunctionDefinition`, perduodamą `ChatCompletionsDefinition`. Pastarasis yra tai, ką LLM gali suprasti.

1. Pažiūrėkime, kaip galime atnaujinti esamą kodą, kad pasinaudotume šia funkcija:

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
// Sukurkite Bot sąsają natūralios kalbos sąveikai
public interface Bot {
    String chat(String prompt);
}

// Konfigūruokite AI paslaugą su LLM ir MCP įrankiais
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Ankstesniame kode mes:

- Apibrėžėme paprastą `Bot` sąsają natūralios kalbos sąveikai
- Naudojome LangChain4j `AiServices`, kad automatiškai susietume LLM su MCP įrankių tiekėju
- Ši sistema automatiškai tvarko įrankių schemų konvertavimą ir funkcijų kvietimą užkulisiuose
- Šis požiūris pašalina rankinį įrankių konvertavimą – LangChain4j tvarko visą MCP įrankių konvertavimo į LLM suderinamą formatą sudėtingumą

#### Rust

Norėdami konvertuoti MCP įrankio atsakymą į formatą, kurį LLM gali suprasti, pridėsime pagalbinę funkciją, kuri suformatuos įrankių sąrašą. Pridėkite šį kodą į savo `main.rs` failą po `main` funkcijos. Tai bus kviečiama siunčiant užklausas LLM:

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

Puiku, dabar esame pasiruošę apdoroti vartotojo užklausas, tad imkimės to.

### -4- Apdoroti vartotojo užklausą

Šioje kodo dalyje apdorosime vartotojo užklausas.

#### TypeScript

1. Pridėkite metodą, kuris bus naudojamas kviečiant mūsų LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Iškvieskite serverio įrankį
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Atlikite ką nors su rezultatu
        // DAR REIKIA PADARYTI

        }
    }
    ```

    Ankstesniame kode mes:

    - Pridėjome metodą `callTools`.
    - Šis metodas priima LLM atsakymą ir tikrina, ar buvo kviečiami įrankiai, jei taip:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // iškvietimo įrankis
        }
        ```

    - Kvies įrankį, jei LLM nurodė, kad jis turi būti kviečiamas:

        ```typescript
        // 2. Iškvieskite serverio įrankį
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Atlikite ką nors su rezultatu
        // TODO
        ```

1. Atnaujinkite `run` metodą, kad įtrauktumėte kvietimus LLM ir `callTools` kvietimą:

    ```typescript

    // 1. Sukurkite žinutes, kurios yra įvestis LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Kvieskite LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Peržiūrėkite LLM atsakymą, kiekvienam pasirinkimui patikrinkite, ar yra įrankių kvietimų
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Puiku, pateikiame visą kodą:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importuoti zod schemai tikrinti

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ateityje gali reikėti pakeisti į šį URL: https://models.github.ai/inference
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
          // Sukurti zod schemą pagal input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Aiškiai nustatyti tipą kaip "function"
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
    
    
          // 2. Iškviesti serverio įrankį
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Atlikti kažką su rezultatu
          // DAR PADARYTI
    
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
    
        // 1. Peržiūrėti LLM atsakymą, kiekvienam pasirinkimui patikrinti, ar yra įrankių kvietimų
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

1. Pridėkime keletą importų, reikalingų LLM kvietimui

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Tada pridėkime funkciją, kuri kvies LLM:

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
            # Pasirenkami parametrai
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

    Ankstesniame kode mes:

    - Perdavėme mūsų funkcijas, rastas MCP serveryje ir konvertuotas, LLM.
    - Tada kvietėme LLM su šiomis funkcijomis.
    - Tada tikriname rezultatą, kad pamatytume, kurias funkcijas turėtume kviesti, jei tokių yra.
    - Galiausiai perduodame funkcijų masyvą kvietimui.

1. Paskutinis žingsnis, atnaujinkime pagrindinį kodą:

    ```python
    prompt = "Add 2 to 20"

    # paklausk LLM, kokie įrankiai yra visi, jei tokių yra
    functions_to_call = call_llm(prompt, functions)

    # iškvieskite siūlomas funkcijas
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Štai ir paskutinis žingsnis, aukščiau esančiame kode mes:

    - Kvietėme MCP įrankį per `call_tool` naudodami funkciją, kurią LLM manė, kad turėtume kviesti pagal mūsų užklausą.
    - Atspausdinome įrankio kvietimo rezultatą MCP serveriui.

#### .NET

1. Parodysime kodą, kaip atlikti LLM užklausą:

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

    Ankstesniame kode mes:

    - Gavome įrankius iš MCP serverio, `var tools = await GetMcpTools()`.
    - Apibrėžėme vartotojo užklausą `userMessage`.
    - Sukūrėme parinkčių objektą, nurodantį modelį ir įrankius.
    - Atlikome užklausą LLM.

1. Paskutinis žingsnis, pažiūrėkime, ar LLM mano, kad turėtume kviesti funkciją:

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

    Ankstesniame kode mes:

    - Pereinėjome per funkcijų kvietimų sąrašą.
    - Kiekvienam įrankio kvietimui išskyrėme pavadinimą ir argumentus bei kvietėme įrankį MCP serveryje naudodami MCP klientą. Galiausiai atspausdinome rezultatus.

Štai visas kodas:

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
    // Vykdykite natūralios kalbos užklausas, kurios automatiškai naudoja MCP įrankius
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

Ankstesniame kode mes:

- Naudojome paprastas natūralios kalbos užklausas sąveikai su MCP serverio įrankiais
- LangChain4j sistema automatiškai tvarko:
  - Vartotojo užklausų konvertavimą į įrankių kvietimus, kai reikia
  - Tinkamų MCP įrankių kvietimą pagal LLM sprendimą
  - Pokalbio srauto valdymą tarp LLM ir MCP serverio
- `bot.chat()` metodas grąžina natūralios kalbos atsakymus, kurie gali apimti MCP įrankių vykdymo rezultatus
- Šis požiūris suteikia sklandžią vartotojo patirtį, kai vartotojams nereikia žinoti apie MCP įgyvendinimą

Pilnas kodo pavyzdys:

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

Čia vyksta dauguma darbo. Kviesime LLM su pradiniu vartotojo užklausa, tada apdorosime atsakymą, kad pamatytume, ar reikia kviesti kokius nors įrankius. Jei taip, kviesime tuos įrankius ir tęsiame pokalbį su LLM tol, kol nebereikės kvietimų ir turėsime galutinį atsakymą.

Darysime kelis kvietimus LLM, tad apibrėžkime funkciją, kuri tvarkys LLM kvietimą. Pridėkite šią funkciją į savo `main.rs` failą:

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

Ši funkcija priima LLM klientą, žinučių sąrašą (įskaitant vartotojo užklausą), įrankius iš MCP serverio ir siunčia užklausą LLM, grąžindama atsakymą.
LLM atsakyme bus masyvas `choices`. Turėsime apdoroti rezultatą, kad patikrintume, ar yra `tool_calls`. Tai leidžia mums žinoti, kad LLM prašo iškviesti konkretų įrankį su argumentais. Pridėkite šį kodą prie savo `main.rs` failo apačios, kad apibrėžtumėte funkciją, kuri tvarkys LLM atsakymą:

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

    // Spausdinti turinį, jei yra
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Tvarkyti įrankių kvietimus
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Pridėti asistento žinutę

        // Vykdyti kiekvieną įrankio kvietimą
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Pridėti įrankio rezultatą prie žinučių
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Tęsti pokalbį su įrankių rezultatais
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

Jei yra `tool_calls`, funkcija ištraukia įrankio informaciją, iškviečia MCP serverį su įrankio užklausa ir prideda rezultatus prie pokalbio žinučių. Tada tęsiamas pokalbis su LLM, o žinutės atnaujinamos su asistento atsakymu ir įrankio iškvietimo rezultatais.

Norėdami ištraukti įrankio iškvietimo informaciją, kurią LLM grąžina MCP iškvietimams, pridėsime dar vieną pagalbinę funkciją, kuri ištrauks viską, ko reikia iškvietimui atlikti. Pridėkite šį kodą prie savo `main.rs` failo apačios:

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

Turėdami visus komponentus, dabar galime apdoroti pradinį vartotojo užklausimą ir iškviesti LLM. Atnaujinkite savo `main` funkciją, kad įtrauktumėte šį kodą:

```rust
// LLM pokalbis su įrankių kvietimais
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

Tai užklaus LLM su pradiniu vartotojo užklausa, prašančia dviejų skaičių sumos, ir apdoros atsakymą, kad dinamiškai tvarkytų įrankių iškvietimus.

Puiku, jūs tai padarėte!

## Užduotis

Paimkite kodą iš pratimo ir išplėskite serverį su dar keliomis įrankių funkcijomis. Tada sukurkite klientą su LLM, kaip pratime, ir išbandykite jį su skirtingomis užklausomis, kad įsitikintumėte, jog visi jūsų serverio įrankiai kviečiami dinamiškai. Tokiu būdu kuriant klientą galutinis vartotojas turės puikią patirtį, nes galės naudoti užklausas vietoje tikslių kliento komandų ir nesijaus, kad kviečiamas MCP serveris.

## Sprendimas

[Sprendimas](/03-GettingStarted/03-llm-client/solution/README.md)

## Pagrindinės mintys

- LLM pridėjimas prie kliento suteikia geresnį būdą vartotojams bendrauti su MCP serveriais.
- Reikia konvertuoti MCP serverio atsakymą į formatą, kurį LLM gali suprasti.

## Pavyzdžiai

- [Java skaičiuoklė](../samples/java/calculator/README.md)
- [.Net skaičiuoklė](../../../../03-GettingStarted/samples/csharp)
- [JavaScript skaičiuoklė](../samples/javascript/README.md)
- [TypeScript skaičiuoklė](../samples/typescript/README.md)
- [Python skaičiuoklė](../../../../03-GettingStarted/samples/python)
- [Rust skaičiuoklė](../../../../03-GettingStarted/samples/rust)

## Papildomi ištekliai

## Kas toliau

- Toliau: [Serverio naudojimas su Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->