# Kliento sukūrimas su LLM

Iki šiol matėte, kaip sukurti serverį ir klientą. Klientas galėjo tiesiogiai kviesti serverį, kad būtų pateiktas įrankių, išteklių ir paragrafų sąrašas. Tačiau tai nėra labai praktiškas požiūris. Jūsų vartotojai gyvena agentų amžiuje ir tikisi naudoti paragrafus bei bendrauti su LLM. Jiems nesvarbu, ar naudojate MCP savo galimybėms saugoti; jie tiesiog nori bendrauti natūralia kalba. Kaip tai išspręsti? Sprendimas yra pridėti LLM prie kliento.

## Apžvalga

Šioje pamokoje dėmesys skiriamas LLM pridėjimui kliento pusėje ir parodymui, kaip tai suteikia daug geresnę vartotojo patirtį.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Sukurti klientą su LLM.
- Sklandžiai bendrauti su MCP serveriu naudojant LLM.
- Užtikrinti geresnę galutinio vartotojo patirtį kliento pusėje.

## Požiūris

Pabandykime suprasti, kokį požiūrį turime pasirinkti. LLM pridėjimas skamba paprastai, bet ar iš tikrųjų tai padarysime?

Štai kaip klientas bendraus su serveriu:

1. Užmegzti ryšį su serveriu.

1. Išvardinti galimybes, paragrafus, išteklius ir įrankius bei išsaugoti jų schemą.

1. Pridėti LLM ir perduoti išsaugotas galimybes bei jų schemą formatu, kurį LLM supranta.

1. Apdoroti vartotojo paragrafą, perduodant jį LLM kartu su klientu išvardytais įrankiais.

Puiku, dabar, kai suprantame tai aukštu lygiu, pabandykime tai pritaikyti žemiau esančioje užduotyje.

## Užduotis: Kliento kūrimas su LLM

Šioje užduotyje mokysimės pridėti LLM prie mūsų kliento.

### Autentifikacija naudojant GitHub asmeninį prieigos raktą

GitHub rakto sukūrimas yra paprastas procesas. Štai kaip tai padaryti:

- Eikite į GitHub nustatymus – spustelėkite savo profilio paveikslėlį viršutiniame dešiniajame kampe ir pasirinkite Nustatymai.
- Pereikite prie Developer Settings – nuslinkite žemyn ir spustelėkite Developer Settings.
- Pasirinkite Personal Access Tokens – spustelėkite Fine-grained tokens ir tada Generate new token.
- Suformuokite raktą – pridėkite pastabą, nustatykite galiojimo terminą ir pasirinkite reikalingus leidimus (scopes). Šiuo atveju būtinai pridėkite Models leidimą.
- Sukurkite ir nukopijuokite raktą – spustelėkite Generate token, ir būtinai jį iškart nukopijuokite, nes vėliau jo nebeišvysite.

### -1- Prisijungimas prie serverio

Pirmiausia sukurkime mūsų klientą:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importuoti zod schemos patikrinimui

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

Aukščiau pateiktame kode mes:

- Importavome reikiamas bibliotekas
- Sukūrėme klasę su dviem nariais, `client` ir `openai`, kurie padės valdyti klientą ir bendrauti su LLM atitinkamai.
- Konfigūravome LLM egzempliorių naudoti GitHub Models, nustatydami `baseUrl` į inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Sukurkite serverio parametrus stdio ryšiui
server_params = StdioServerParameters(
    command="mcp",  # Vykdomasis failas
    args=["run", "server.py"],  # Pasirinktiniai komandinės eilutės argumentai
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

Aukščiau pateiktame kode mes:

- Importavome reikiamas MCP bibliotekas
- Sukūrėme klientą

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

Pirma, reikės pridėti LangChain4j priklausomybes į savo `pom.xml` failą. Pridėkite šias priklausomybes, kad įgalintumėte MCP integraciją ir GitHub Models palaikymą:

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

Aukščiau pateiktame kode mes:

- **Pridėjome LangChain4j priklausomybes**: reikalingas MCP integracijai, oficialiam OpenAI klientui ir GitHub Models palaikymui
- **Importavome LangChain4j bibliotekas**: MCP integracijai ir OpenAI pokalbių modeliui
- **Sukūrėme `ChatLanguageModel`**: konfigūruotą naudoti GitHub Models su jūsų GitHub raktu
- **Nustatėme HTTP transportą**: naudojant Server-Sent Events (SSE), kad prisijungtume prie MCP serverio
- **Sukūrėme MCP klientą**: kuris tvarkys ryšį su serveriu
- **Naudojome LangChain4j įdiegtą MCP palaikymą**: kuris supaprastina LLM ir MCP serverių integraciją

#### Rust

Šis pavyzdys daro prielaidą, kad turite veikiančią Rust MCP serverio programą. Jei neturite, grįžkite į pamoką [01-first-server](../01-first-server/README.md) ir sukurkite serverį.

Kai turite Rust MCP serverį, atidarykite terminalą ir pereikite į tą patį katalogą, kur yra serveris. Tada paleiskite šią komandą, kad sukurtumėte naują LLM kliento projektą:

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
> Oficialios Rust bibliotekos OpenAI nėra, tačiau `async-openai` brangakmenis yra [bendruomenės palaikoma biblioteka](https://platform.openai.com/docs/libraries/rust#rust), kuri dažnai naudojama.

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
    // Pradinė žinutė
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

Šis kodas sukuria paprastą Rust programą, kuri jungiasi prie MCP serverio ir GitHub Models, skirtų LLM sąveikai.

> [!IMPORTANT]
> Įsitikinkite, kad prieš paleisdami programą nustatėte aplinkos kintamąjį `OPENAI_API_KEY` su savo GitHub raktu.

Puiku, kitame žingsnyje išvardinsime galimybes serveryje.

### -2- Serverio galimybių išvardinimas

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

Aukščiau pateiktame kode mes:

- Pridėjome kodą jungimuisi prie serverio, `connectToServer`.
- Sukūrėme `run` metodą, atsakingą už programos eigą. Kol kas jis tik išvardina įrankius, tačiau netrukus pridėsime daugiau.

#### Python

```python
# Išvardinti prieinamus išteklius
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Išvardinti prieinamus įrankius
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

Aukščiau pateiktame kode mes:

- Išvardinome MCP serverio įrankius
- Kiekvienam įrankiui išvardinome pavadinimą, aprašymą ir jo schemą. Pastarąją naudosime norėdami netrukus kviesti įrankius.

#### Java

```java
// Sukurkite įrankių teikėją, kuris automatiškai aptinka MCP įrankius
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP įrankių teikėjas automatiškai tvarko:
// - Galimų įrankių iš MCP serverio sąrašą
// - MCP įrankių schemų konvertavimą į LangChain4j formatą
// - Įrankių vykdymo ir atsakymų valdymą
```

Aukščiau pateiktame kode mes:

- Sukūrėme `McpToolProvider`, kuris automatiškai aptinka ir registruoja visus MCP serverio įrankius
- Įrankių tiekėjas viduje tvarko MCP įrankių schemų konvertavimą į LangChain4j įrankių formatą
- Šis požiūris abstrahuoja rankinį įrankių išvardinimą ir konvertavimą

#### Rust

MCP serverio įrankiai gaunami naudojant `list_tools` metodą. Savo `main` funkcijoje, po MCP kliento nustatymo, pridėkite šį kodą:

```rust
// Gauti MCP įrankių sąrašą
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Serverio galimybių konvertavimas į LLM įrankius

Kitas žingsnis po galimybių sąrašo gavimo yra konvertuoti jas į formatą, kurį supranta LLM. Kai tai padarysime, galėsime šias galimybes pateikti kaip įrankius mūsų LLM.

#### TypeScript

1. Pridėkite šį kodą, kuris konvertuoja MCP serverio atsakymą į įrankių formatą, kurį gali naudoti LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Sukurkite zod schemą remiantis input_schema
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

    Aukščiau pateiktas kodas ima MCP serverio atsakymą ir konvertuoja jį į įrankio apibrėžimo formatą, kurį LLM gali suprasti.

1. Atnaujinkime `run` metodą, kad būtų išvardytos serverio galimybės:

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

    Aukščiau pateiktame kode atnaujiname `run` metodą, kad jis pereitų per rezultatą ir kiekvienam įrašui iškvietų `openAiToolAdapter`.

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

    Aukščiau esančioje funkcijoje `convert_to_llm_tools` priimame MCP įrankio atsakymą ir konvertuojame jį į formatą, kurį LLM gali suprasti.

1. Tada atnaujinkime klientų kodą, kad naudotume šią funkciją:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Čia pridedame kvietimą `convert_to_llm_tool`, kad MCP įrankio atsakymą paverstume į ką nors, ką galime perduoti LLM.

#### .NET

1. Pridėkime kodą, kuris konvertuoja MCP įrankio atsakymą į LLM suprantamą formatą

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

Aukščiau pateiktame kode mes:

- Sukūrėme funkciją `ConvertFrom`, kuri priima pavadinimą, aprašymą ir įvesties schemą.
- Apibrėžėme funkcionalumą, kuris sukuria `FunctionDefinition`, perduodamą `ChatCompletionsDefinition`. Pastarasis yra suprantamas LLM.

1. Pažiūrėkime, kaip atnaujinti esamą kodą, kad pasinaudotume šia funkcija:

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
// Sukurkite botų sąsają natūralios kalbos sąveikai
public interface Bot {
    String chat(String prompt);
}

// Konfigūruokite AI paslaugą su LLM ir MCP įrankiais
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Aukščiau pateiktame kode mes:

- Apibrėžėme paprastą `Bot` sąsają natūralios kalbos sąveikai
- Naudojome LangChain4j `AiServices` automatiškai susieti LLM su MCP įrankių tiekėju
- Įrankių schema konvertavimas ir funkcijų kvietimas tvarkomas automatiškai
- Šis požiūris panaikina rankinio įrankių konvertavimo poreikį – LangChain4j tvarko visą sudėtingumą konvertuojant MCP įrankius į LLM suderinamą formatą

#### Rust

Norėdami konvertuoti MCP įrankio atsakymą į formatą, kurį LLM supranta, pridėsime pagalbinę funkciją, kuri suformatuos įrankių sąrašą. Pridėkite šį kodą į savo `main.rs` failą žemiau `main` funkcijos. Ši funkcija bus kviečiama siunčiant užklausas LLM:

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

Puiku, dabar esame pasiruošę apdoroti vartotojų užklausas, tad spręskime tai toliau.

### -4- Vartotojo paragrafo apdorojimas

Šiame kodo dalyje apdorosime vartotojo užklausas.

#### TypeScript

1. Pridėkite metodą, kuris bus naudojamas kviečiant LLM:

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

        // 3. Padarykite ką nors su rezultatu
        // ATLIKTI

        }
    }
    ```

    Aukščiau pateiktame kode mes:

    - Pridėjome metodą `callTools`.
    - Metodas priima LLM atsakymą ir tikrina, ar buvo kviečiami kokie nors įrankiai:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // iškvietimo įrankis
        }
        ```

    - Kviečia įrankį, jei LLM nurodo jį kviesti:

        ```typescript
        // 2. Iškvieskite serverio įrankį
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Padarykite ką nors su rezultatu
        // TODO
        ```

1. Atnaujinkite `run` metodą, kad jis įtrauktų LLM kvietimą ir skambutį `callTools`:

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
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Peržiūrėkite LLM atsakymą, kiekvienam pasirinkimui patikrinkite, ar jame yra įrankių kvietimai
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
import { z } from "zod"; // Importuokite zod schemos validavimui

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ateityje gali tekti pakeisti į šį URL: https://models.github.ai/inference
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
    
          // 3. Atlikite veiksmus su rezultatu
          // DARBAI VĖLIAU
    
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
    
        // 1. Pereikite per LLM atsakymą, kiekvienam pasirinkimui patikrinkite, ar yra įrankių iškvietimai
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

1. Pridėkime kai kuriuos importus, reikalingus LLM kvietimui

    ```python
    # didelis kalbos modelis
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Dabar pridėkime funkciją, kuri kvies LLM:

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

    Aukščiau pateiktame kode mes:

    - Perdavėme mūsų funkcijas, rastas MCP serveryje ir konvertuotas, į LLM.
    - Tada kvietėme LLM su šiomis funkcijomis.
    - Po to tikrinome rezultatą, kad sužinotume, kokias funkcijas reikia kviesti, jei tokių yra.
    - Galiausiai perduodame funkcijų masyvą kvietimams.

1. Paskutinis žingsnis, atnaujinkime pagrindinį kodą:

    ```python
    prompt = "Add 2 to 20"

    # paklausk LLM, kokie įrankiai tinkami, jei tokių yra
    functions_to_call = call_llm(prompt, functions)

    # iškviesk siūlomas funkcijas
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Tai buvo paskutinis žingsnis. Aukščiau esančiame kode mes:

    - Kviesime MCP įrankį per `call_tool`, naudodami funkciją, kurią LLM nusprendė kviesti pagal mūsų paragrafą.
    - Atspausdinsime įrankio kvietimo rezultatą MCP serveriui.

#### .NET

1. Parodysime kodą LLM paragrafui užklausai:

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

    Aukščiau pateiktame kode mes:

    - Gauta įrankių iš MCP serverio, `var tools = await GetMcpTools()`.
    - Apibrėžtas vartotojo paragrafas `userMessage`.
    - Sukurtas parinkčių objektas, nurodantis modelį ir įrankius.
    - Padarytas užklausimas LLM.

1. Paskutinis žingsnis, patikrinti, ar LLM mano, kad reikia kviesti funkciją:

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

    Aukščiau pateiktame kode mes:

    - Pereiname per funkcijų kvietimų sąrašą.
    - Kiekvienam įrankio kvietimui išskiriame pavadinimą ir argumentus ir kviečiame įrankį MCP serveryje naudodami MCP klientą. Galiausiai atspausdiname rezultatus.

Štai visas kodas:

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

Aukščiau pateiktame kode mes:

- Naudojome paprastus natūralios kalbos paragrafus MCP serverio įrankiams valdyti
- LangChain4j karkasas automatiškai valdo:
  - Vartotojo paragrafų konvertavimą į įrankių kvietimus, kai to reikia
  - Tinkamų MCP įrankių kvietimą pagal LLM sprendimą
  - Pokalbio eigą tarp LLM ir MCP serverio
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

Čia vyksta daugiausia darbo. Iškviesime LLM su pradiniu vartotojo paragrafu, tada apdorosime atsakymą, kad sužinotume, ar reikia kviesti kokius nors įrankius. Jei taip, kviesime tuos įrankius ir tęsiame pokalbį su LLM tol, kol daugiau įrankių kvietimų nereiks ir turėsime galutinį atsakymą.

Mes atliksime kelis kvietimus LLM, tad apibrėžkime funkciją LLM kvietimui apdoroti. Pridėkite šią funkciją į savo `main.rs` failą:

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

Ši funkcija priima LLM klientą, pranešimų sąrašą (įskaitant vartotojo paragrafą), MCP serverio įrankius, siunčia užklausą LLM ir grąžina atsakymą.
LLM atsakyme bus masyvas `choices`. Reikės apdoroti rezultatą, kad sužinotume, ar yra kokių nors `tool_calls`. Tai leidžia mums žinoti, kad LLM prašo iškviesti konkretų įrankį su argumentais. Pridėkite šį kodą failo `main.rs` pabaigoje, kad apibrėžtumėte funkciją, apdorojančią LLM atsakymą:

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

    // Tvarkyti įrankių užklausas
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Pridėti asistentų žinutę

        // Vykdyti kiekvieną įrankio užklausą
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Pridėti įrankio rezultatą į žinutes
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

Jei yra `tool_calls`, funkcija ištraukia įrankio informaciją, kviečia MCP serverį su įrankio užklausa ir priduria rezultatus prie pokalbio žinučių. Tada pokalbis tęsiasi su LLM, o žinutės atnaujinamos pagal asistento atsakymą ir įrankio iškvietimo rezultatus.

Norėdami išgauti LLM grąžinamą informaciją apie įrankio kvietimą MCP iškvietimams, pridėsime dar vieną pagalbinę funkciją, kuri ištraukia viską, ko reikia kvietimui atlikti. Pridėkite šį kodą failo `main.rs` pabaigoje:

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

Kai turėsime visas dalis, galėsime apdoroti pradinį naudotojo užklausimą ir iškviesti LLM. Atnaujinkite savo funkciją `main`, kad įtrauktumėte šį kodą:

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

Šis kodas užklaus LLM su pradiniu vartotojo užklausa, prašančia sumuoti du skaičius, ir apdoroja atsakymą, dinamiškai tvarkydamas įrankių kvietimus.

Puiku, užbaigėte!

## Užduotis

Paimkite kodo fragmentą iš pratimo ir sukurkite serverį su dar keliais įrankiais. Tada sukurkite klientą su LLM, kaip ir pratime, ir išbandykite su įvairiomis užklausomis, kad įsitikintumėte, jog visi jūsų serverio įrankiai kviečiami dinamiškai. Toks kliento kūrimo būdas suteikia vartotojui puikią patirtį, nes jis gali naudoti užklausas vietoje tikslių kliento komandų ir nesuvokia, kad būtų kviečiamas MCP serveris.

## Sprendimas

[Sprendimas](/03-GettingStarted/03-llm-client/solution/README.md)

## Pagrindinės mintys

- LLM pridėjimas prie kliento suteikia geresnį būdą vartotojams bendrauti su MCP serveriais.
- Reikia konvertuoti MCP serverio atsakymą į formatą, kurį supranta LLM.

## Pavyzdžiai

- [Java skaičiuotuvas](../samples/java/calculator/README.md)
- [.Net skaičiuotuvas](../../../../03-GettingStarted/samples/csharp)
- [JavaScript skaičiuotuvas](../samples/javascript/README.md)
- [TypeScript skaičiuotuvas](../samples/typescript/README.md)
- [Python skaičiuotuvas](../../../../03-GettingStarted/samples/python)
- [Rust skaičiuotuvas](../../../../03-GettingStarted/samples/rust)

## Papildomi ištekliai

## Kas toliau

- Toliau: [Serverio naudojimas Visual Studio Code aplinkoje](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas pasitelkus dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogiškas vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus interpretavimus, kilusius naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->