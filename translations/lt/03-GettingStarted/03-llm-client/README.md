# Kliento kūrimas su LLM

Iki šiol matėte, kaip sukurti serverį ir klientą. Klientas galėjo tiesiogiai kreiptis į serverį, kad gautų jo įrankių, išteklių ir užklausų sąrašą. Tačiau tai nėra labai praktiškas metodas. Jūsų vartotojai gyvena agentiniu amžiuje ir tikisi naudoti užklausas bei bendrauti su LLM vietoje to. Jiems nesvarbu, ar jūs naudojate MCP savo galimybėms saugoti; jie tiesiog tikisi bendrauti natūralia kalba. Kaip tai išspręsti? Sprendimas yra pridėti LLM prie kliento.

## Apžvalga

Šioje pamokoje sutelksime dėmesį į LLM pridėjimą prie kliento ir parodysime, kaip tai gerokai pagerina vartotojo patirtį.

## Mokymosi tikslai

Baigę šią pamoką galėsite:

- Sukurti klientą su LLM.
- Sklandžiai sąveikauti su MCP serveriu naudojant LLM.
- Suteikti geresnę galutinio vartotojo patirtį kliento pusėje.

## Požiūris

Pabandykime suprasti, kokį požiūrį turime taikyti. LLM pridėjimas skamba paprastai, bet ar iš tiesų tai padarysime?

Štai kaip klientas bendraus su serveriu:

1. Užmegzti ryšį su serveriu.

1. Gauti galimybių, užklausų, išteklių ir įrankių sąrašą bei išsaugoti jų schemą.

1. Pridėti LLM ir perduoti išsaugotas galimybes ir jų schemą formatu, kurį LLM supranta.

1. Apdoroti vartotojo užklausą perduodant ją LLM kartu su kliento išvardytais įrankiais.

Puiku, dabar kai supratome, kaip tai padaryti aukštu lygiu, pabandykime žemiau esančiame pratime.

## Pratimas: kliento kūrimas su LLM

Šiame pratime išmokysime pridėti LLM prie mūsų kliento.

### Autentifikacija naudojant GitHub Asmeninį Prieigos Raktą

Sukurti GitHub raktą yra paprastas procesas. Štai kaip tai galite padaryti:

- Eikite į GitHub Nustatymus – Spauskite savo profilio paveikslėlį viršutiniame dešiniajame kampe ir pasirinkite Nustatymai.
- Eikite į Kūrėjo nustatymus – Slinkite žemyn ir spauskite Kūrėjo nustatymai.
- Pasirinkite Asmeninius Prieigos Raktus – Spauskite Smulkiai nustatytus raktus ir tada Sukurti naują raktą.
- Konfigūruokite savo raktą – Pridėkite pastabą referencijai, nustatykite galiojimo laiką ir pasirinkite reikalingas teises. Šiuo atveju būtinai pridėkite Models leidimą.
- Sukurkite ir nukopijuokite raktą – Spauskite Sukurti raktą ir įsitikinkite, kad jį iš karto nukopijuojate, nes vėliau jo nebepamatysite.

### -1- Prisijungimas prie serverio

Sukurkime pirmiausia savo klientą:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importuokite zod schemai patikrinti

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
- Sukonfigūrėme savo LLM egzempliorių naudoti GitHub modelius nustatydami `baseUrl` rodyti į inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Sukurti serverio parametrus stdio ryšiui
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
            # Inicializuoti ryšį
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

Pirmiausia turite pridėti LangChain4j priklausomybes į savo `pom.xml` failą. Pridėkite šias priklausomybes, kad įgalintumėte MCP integraciją ir OpenAI suderinamą MiniMax API:

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

Nustatykite savo MiniMax API raktą ir, jei reikia, galinį tašką bei modelį.
`MINIMAX_MODEL_ID` palaiko `MiniMax-M3` ir `MiniMax-M2.7`. Jei
`OPENAI_BASE_URL` nėra nustatytas, `MINIMAX_REGION` palaiko `global_en` ir `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Jei norite pasirinkti galinį tašką pagal regioną, praleiskite `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
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

        // Sukurkite MCP transportą prisijungimui prie serverio
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

Ankstesniame kode mes:

- **Pridėjome LangChain4j priklausomybes**: Reikalinga MCP integracijai ir OpenAI suderinamam MiniMax API
- **Importavome LangChain4j bibliotekas**: MCP integracijai ir OpenAI pokalbių modelio funkcijoms
- **Sukūrėme `ChatLanguageModel`**: Sukonfigūruotas naudoti MiniMax su jūsų MiniMax API raktu, galiniu tašku ir palaikomu modelio ID
- **Nustatėme HTTP transportą**: Naudojant Server-Sent Events (SSE) prisijungti prie MCP serverio
- **Sukūrėme MCP klientą**: Kuris tvarkys komunikaciją su serveriu
- **Naudojome LangChain4j integruotą MCP palaikymą**: Kuris paprastina integalizaciją tarp LLM ir MCP serverių

#### Rust

Šis pavyzdys daro prielaidą, kad turite Rust pagrįstą MCP serverį. Jei neturite, žr. atgal į [01-first-server](../01-first-server/README.md) pamoką, kad sukurtumėte serverį.

Kai turėsite Rust MCP serverį, atidarykite terminalą ir pereikite į tą patį aplanką kaip serveris. Tada vykdykite šią komandą sukurti naują LLM kliento projektą:

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
> Oficiali Rust biblioteka OpenAI nėra, tačiau `async-openai` paketas yra [bendruomenės prižiūrima biblioteka](https://platform.openai.com/docs/libraries/rust#rust), kurios dažnai naudojama.

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

Šis kodas sukuria pagrindinę Rust programą, kuri jungiasi prie MCP serverio ir GitHub modelių LLM sąveikai.

> [!IMPORTANT]
> Įsitikinkite, kad nustatėte `OPENAI_API_KEY` aplinkos kintamąjį su savo GitHub raktu prieš paleisdami programą.

Puiku, kitame žingsnyje išvardysime serverio galimybes.

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

Ankstesniame kode mes:

- Pridėjome kodą prisijungimui prie serverio, `connectToServer`.
- Sukūrėme `run` metodą atsakingą už mūsų programos eigą. Iki šiol jis tik išvardina įrankius, bet netrukus pridėsime daugiau.

#### Python

```python
# Išvardinti galimus išteklius
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Išvardinti galimus įrankius
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

- Išvardinome MCP serveryje prieinamus įrankius
- Kiekvienam įrankiui išvardinome pavadinimą, aprašymą ir jo schemą. Pastarąją naudosime netrukus įrankių kvietimui.

#### Java

```java
// Sukurkite įrankių teikėją, kuris automatiškai aptinka MCP įrankius
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP įrankių teikėjas automatiškai tvarko:
// - MCP serverio pateiktų įrankių sąrašą
// - MCP įrankių schemų konvertavimą į LangChain4j formatą
// - Įrankių vykdymo ir atsakymų valdymą
```

Ankstesniame kode mes:

- Sukūrėme `McpToolProvider`, kuri automatiškai atranda ir registruoja visus MCP serverio įrankius
- Įrankių tiekėjas viduje konvertuoja MCP įrankių schemas į LangChain4j įrankių formatą
- Šis požiūris abstraktuoja rankinį įrankių išvardinimą ir konvertavimą

#### Rust

Įrankių išgavimas iš MCP serverio atliekamas naudojant `list_tools` metodą. Savo `main` funkcijoje, sukūrę MCP klientą, pridėkite šį kodą:

```rust
// Gauti MCP įrankių sąrašą
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Serverio galimybių konvertavimas į LLM įrankius

Kitas žingsnis po serverio galimybių išvardinimo yra jų konvertavimas į formatą, kurį supranta LLM. Tai leis pateikti šias galimybes kaip įrankius mūsų LLM.

#### TypeScript

1. Pridėkite šį kodą konvertuoti MCP serverio atsakymą į LLM suprantamą įrankio formatą:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Sukurkite zod schemą pagal įvesties schemą
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Aiškiai nustatykite tipą kaip „function“
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

    Aukščiau pateiktas kodas paima MCP serverio atsakymą ir konvertuoja į įrankio apibrėžimo formatą, kurį LLM supranta.

2. Dabar atnaujinkime `run` metodą, kad išvardintų serverio galimybes:

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

    Ankstesniame kode atnaujinome `run` metodą, kad jis praeitų per rezultatus ir kiekvienam įrašui kviečia `openAiToolAdapter`.

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

    Funkcijoje `convert_to_llm_tools` paimame MCP įrankio atsakymą ir konvertuojame į formatą, kurį LLM gali suprasti.

2. Tada atnaujinkime kliento kodą taip, kad panaudotume šią funkciją:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Čia pridedame kvietimą `convert_to_llm_tool`, kad konvertuotume MCP įrankio atsakymą į ką nors, ką galime tiekti LLM vėliau.

#### .NET

1. Pridėkime kodą konvertuoti MCP įrankio atsakymą į ką nors, ką LLM gali suprasti

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
- Apibrėžėme funkcionalumą, kuris sukuria `FunctionDefinition`, perduodamą `ChatCompletionsDefinition`. Pastarasis yra tai, ką LLM supranta.

2. Pažiūrėkime, kaip galime atnaujinti tam tikrą esamą kodą, kad išnaudotume šią funkciją:

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
// Sukurkite roboto sąsają natūraliam kalbos bendravimui
public interface Bot {
    String chat(String prompt);
}

// Konfigūruokite DI paslaugą su LLM ir MCP įrankiais
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Ankstesniame kode mes:

- Apibrėžėme paprastą `Bot` sąsają natūralaus kalbos bendravimo funkcijoms
- Naudojome LangChain4j `AiServices` automatiškai susieti LLM su MCP įrankių tiekėju
- Ši sistema automatiškai tvarko įrankių schemų konvertavimą ir funkcijų iškvietimą užkulisiuose
- Šis požiūris pašalina rankinį įrankių konvertavimą – LangChain4j tvarko visą MCP įrankių konvertavimo sudėtingumą į LLM suderinamą formatą

#### Rust

Norėdami konvertuoti MCP įrankio atsakymą į formatą, kurį LLM gali suprasti, pridėsime pagalbinę funkciją, kuri suformatuos įrankių sąrašą. Pridėkite šį kodą į savo `main.rs` failą žemiau `main` funkcijos. Tai bus kviečiama atliekant užklausas LLM:

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

Gerai, dabar esame pasiruošę apdoroti naudotojo užklausas, tad imkimės to.

### -4- Naudotojo užklausos apdorojimas

Šioje kodo dalyje apdorosime naudotojų užklausas.

#### TypeScript

1. Pridėkite metodą, kuris bus naudojamas kviesti mūsų LLM:

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
        // DARBAI

        }
    }
    ```

    Ankstesniame kode mes:

    - Pridėjome metodą `callTools`.
    - Metodas gauna LLM atsakymą ir tikrina, kokie įrankiai buvo iškviečiami, jei išvis:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // iškvieskite įrankį
        }
        ```

    - Kviečia įrankį, jei LLM rodo, kad jis turi būti iškviestas:

        ```typescript
        // 2. Iškvieskite serverio įrankį
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Atlikite ką nors su rezultatu
        // DAROMA
        ```

2. Atnaujinkite `run` metodą įtraukdami LLM kvietimus ir `callTools` kvietimą:

    ```typescript

    // 1. Sukurkite žinutes, kurios bus įvestis LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Iškvieskite LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Peržiūrėkite LLM atsakymą, kiekvienam pasirinkimui patikrinkite, ar yra įrankių iškvietimų
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
import { z } from "zod"; // Importuokite zod schemos patikrinimui

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // gali prireikti ateityje pakeisti į šį url: https://models.github.ai/inference
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
            type: "function" as const, // Aiškiai nurodykite tipą "function"
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
    
          // 3. Atlikite kažką su rezultatu
          // DAR PABAIGTI
    
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
    
        // 3. Peržiūrėkite LLM atsakymą, kiekvienam pasirinkimui patikrinkite, ar yra įrankių kvietimų
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

2. Toliau pridėkime funkciją, kuri kvies LLM:

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

    - Perdavėme funkcijas, rastas MCP serveryje ir konvertuotas, LLM.
    - Tada iškvietėme LLM su tomis funkcijomis.
    - Tada tikriname rezultatą, kad sužinotume, kurias funkcijas turime kviesti, jei išvis.
    - Galiausiai perduodame masyvą funkcijų kvietimui.

3. Paskutinis žingsnis, atnaujinkime pagrindinį kodą:

    ```python
    prompt = "Add 2 to 20"

    # paklausk LLM, kokie įrankiai yra pasiekiami, jei tokių yra
    functions_to_call = call_llm(prompt, functions)

    # iškvieskite siūlomas funkcijas
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Štai tai buvo paskutinis žingsnis, aukščiau pateiktame kode mes:

    - Kvietėme MCP įrankį per `call_tool`, naudodami funkciją, kurią LLM manė, kad turėtume kviesti pagal mūsų užklausą.
    - Spausdinome rezultatą, gautą iš MCP serverio įrankio kvietimo.

#### .NET

1. Parodysime šiek tiek kodo LLM užklausai atlikti:

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

    Ankstesniame kode mes:

    - Gavome įrankius iš MCP serverio, `var tools = await GetMcpTools()`.
    - Apibrėžėme naudotojo užklausą `userMessage`.
    - Sudarėme opcijų objektą, nurodantį modelį ir įrankius.
    - Pateikėme užklausą LLM.

2. Paskutinis žingsnis, pažiūrėkime, ar LLM mano, kad reikia kviesti funkciją:

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
    - Kiekvienam įrankio kvietimui išbierėme pavadinimą ir argumentus, pakvietėme įrankį MCP serveryje naudodami MCP klientą. Galiausiai pateikėme rezultatus.

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

// 6. Print the generic response
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
  - Naudotojų užklausų konvertavimą į įrankių kvietimus, kai reikia
  - Tinkamų MCP įrankių kvietimą, remiantis LLM sprendimu
  - Pokalbio valdymą tarp LLM ir MCP serverio
- `bot.chat()` metodas grąžina natūralios kalbos atsakymus, kurie gali apimti MCP įrankių vykdymo rezultatus
- Šis požiūris suteikia sklandžią vartotojo patirtį, kai vartotojams nereikia žinoti apie MCP vidinę įgyvendinimą

Visa kodo pavyzdys:

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

Čia vyksta dauguma darbo. Mes kviesime LLM su pradiniu naudotojo užklausu, tada apdorosime atsakymą, pažiūrėti, ar reikia kvieti įrankius. Jei taip, kviesime tuos įrankius ir tęsiame pokalbį su LLM tol, kol nebeliks daugiau įrankių kvietimų ir turėsime galutinį atsakymą.


Mes darysime keletą skambučių į LLM, todėl apibrėžkime funkciją, kuri tvarkys LLM skambutį. Pridėkite šią funkciją į savo `main.rs` failą:

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

Atsakyme iš LLM bus masyvas `choices`. Turėsime apdoroti rezultatą, kad pamatytume, ar yra `tool_calls`. Tai leidžia mums žinoti, kad LLM prašo iškviesti konkretų įrankį su argumentais. Pridėkite šį kodą į `main.rs` failo pabaigą, kad apibrėžtumėte funkciją, kuri apdoros LLM atsakymą:

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

    // Spausdinti turinį, jei jis yra
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Apdoroti įrankių iškvietimus
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Pridėti asistento pranešimą

        // Vykdyti kiekvieną įrankio iškvietimą
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Pridėti įrankio rezultatą į pranešimus
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

Jei yra `tool_calls`, funkcija ištraukia įrankio informaciją, iškviečia MCP serverį su įrankio užklausa ir prideda rezultatus prie pokalbio žinučių. Tada ji tęsia pokalbį su LLM, o žinutės atnaujinamos su asistento atsakymu ir įrankio skambučio rezultatais.

Norėdami išgauti įrankio skambučio informaciją, kurią LLM grąžina MCP skambučiams, pridėsime dar vieną pagalbinę funkciją, kuri ištrauks viską, ko reikia skambučiui atlikti. Pridėkite šį kodą į `main.rs` failo pabaigą:

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

Turėdami visas dalis, dabar galime apdoroti pradinę vartotojo užklausą ir iškviesti LLM. Atnaujinkite savo `main` funkciją taip, kad ji apimtų šį kodą:

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

Tai užklaus LLM su pradiniu vartotojo užklausa, klausdama dviejų skaičių sumos, ir apdoros atsakymą, kad dinamiškai apdorotų įrankių skambučius.

Puiku, jūs tai padarėte!

## Užduotis

Paimkite kodą iš pratimo ir sukurkite serverį su dar daugiau įrankių. Tada sukurkite klientą su LLM, kaip pratybose, ir išbandykite jį su skirtingomis užklausomis, kad įsitikintumėte, jog visi jūsų serverio įrankiai kviečiami dinamiškai. Tokiu būdu kuriant klientą galutinis vartotojas turės puikią naudotojo patirtį, nes galės naudotis užklausomis vietoje tikslių klientų komandų ir nematys, kad kviečiamas bet koks MCP serveris.

## Sprendimas

[Sprendimas](./solution/README.md)

## Svarbiausios mintys

- LLM pridėjimas į jūsų klientą suteikia geresnį būdą vartotojams bendrauti su MCP serveriais.
- Turite konvertuoti MCP serverio atsakymą į ką nors, ką gali suprasti LLM.

## Pavyzdžiai

- [Java Skaičiuoklė](../samples/java/calculator/README.md)
- [.Net Skaičiuoklė](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Skaičiuoklė](../samples/javascript/README.md)
- [TypeScript Skaičiuoklė](../samples/typescript/README.md)
- [Python Skaičiuoklė](../../../../03-GettingStarted/samples/python)
- [Rust Skaičiuoklė](../../../../03-GettingStarted/samples/rust)

## Papildomi šaltiniai

## Kas toliau

- Toliau: [Serverio naudojimas Visual Studio Code aplinkoje](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->