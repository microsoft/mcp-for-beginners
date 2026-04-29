# Ustvarjanje odjemalca z LLM

Do zdaj ste videli, kako ustvariti strežnik in odjemalca. Odjemalec je lahko izrecno poklical strežnik, da na seznamu pokaže njegova orodja, vire in pozive. Vendar to ni zelo praktičen pristop. Vaši uporabniki živijo v agentnem času in pričakujejo, da bodo uporabljali pozive in komunicirali z LLM. Ni jim mar, ali uporabljate MCP za shranjevanje svojih zmožnosti; preprosto želijo komunicirati z uporabo naravnega jezika. Kako torej to rešimo? Rešitev je, da dodamo LLM odjemalcu.

## Pregled

V tej lekciji se osredotočamo na dodajanje LLM k vašemu odjemalcu in pokažemo, kako to uporabniku nudi veliko boljšo izkušnjo.

## Cilji učenja

Ob koncu te lekcije boste znali:

- Ustvariti odjemalca z LLM.
- Brezšivno komunicirati z MCP strežnikom z uporabo LLM.
- Zagotoviti boljšo izkušnjo končnega uporabnika na strani odjemalca.

## Pristop

Poskusimo razumeti pristop, ki ga moramo sprejeti. Dodajanje LLM zveni preprosto, a bomo to dejansko naredili?

Tako bo odjemalec komuniciral s strežnikom:

1. Vzpostavitev povezave s strežnikom.

1. Na seznamu prikaže zmožnosti, pozive, vire in orodja ter shrani njihov shematski opis.

1. Dodaj LLM in posreduj shranjene zmožnosti in njihov shematski opis v formatu, ki ga LLM razume.

1. Obdelaj uporabniški poziv tako, da ga posreduješ LLM skupaj z orodji, ki jih je odjemalec navedel.

Super, zdaj ko razumemo, kako to lahko naredimo na visoki ravni, poskusimo to v spodnji vadbi.

## Vadba: Ustvarjanje odjemalca z LLM

V tej vadbi se bomo naučili, kako dodati LLM našemu odjemalcu.

### Avtentikacija z GitHub osebnim dostopnim žetonom

Ustvarjanje GitHub žetona je preprost postopek. Tako ga lahko naredite:

- Pojdite v nastavitve GitHub – Kliknite na svojo profilno sliko v zgornjem desnem kotu in izberite Nastavitve.
- Pomaknite se do razdelka Developer Settings – Pomaknite se navzdol in kliknite na Developer Settings.
- Izberite Personal Access Tokens – Kliknite na Fine-grained tokens in nato Generate new token.
- Konfigurirajte svoj žeton – Dodajte opombo za referenco, nastavite datum poteka in izberite potrebne obsege (dovoljenja). V tem primeru ne pozabite dodati dovoljenja Models.
- Ustvarite in kopirajte žeton – Kliknite Generate token in ga takoj kopirajte, saj ga ne boste mogli ponovno videti.

### -1- Povezava s strežnikom

Najprej ustvarimo našega odjemalca:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Uvozi zod za preverjanje sheme

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

V zgornji kodi smo:

- Uvozili potrebne knjižnice
- Ustvarili razred z dvema članoma, `client` in `openai`, ki nam pomagata upravljati odjemalca in komunicirati z LLM vsakega posebej.
- Konfigurirali naš primer LLM, da uporablja GitHub Models, tako da nastavimo `baseUrl`, ki kaže na inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Ustvari strežniške parametre za stdio povezavo
server_params = StdioServerParameters(
    command="mcp",  # Izvedljiva datoteka
    args=["run", "server.py"],  # Neobvezni argumenti ukazne vrstice
    env=None,  # Neobvezne okoljske spremenljivke
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializiraj povezavo
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

V zgornji kodi smo:

- Uvozili potrebne knjižnice za MCP
- Ustvarili odjemalca

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

Najprej morate dodati odvisnosti LangChain4j v vašo datoteko `pom.xml`. Dodajte te odvisnosti za omogočanje MCP integracije in podporo GitHub Modelom:

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

Nato ustvarite svojo Java razred odjemalca:

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
    
    public static void main(String[] args) throws Exception {        // Konfigurirajte LLM za uporabo GitHub modelov
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Ustvarite MCP prenos za povezavo s strežnikom
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Ustvarite MCP odjemalca
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

V zgornji kodi smo:

- **Dodali odvisnosti LangChain4j**: Potrebne za MCP integracijo, uradnega odjemalca OpenAI in podporo GitHub Modelom
- **Uvozili knjižnice LangChain4j**: Za MCP integracijo in funkcionalnost chat modela OpenAI
- **Ustvarili `ChatLanguageModel`**: Konfiguriran za uporabo GitHub Modelov z vašim GitHub žetonom
- **Nastavili HTTP transport**: Z uporabo Server-Sent Events (SSE) za povezavo s MCP strežnikom
- **Ustvarili MCP odjemalca**: Ki bo upravljal komunikacijo s strežnikom
- **Uporabili vgrajeno podporo MCP v LangChain4j**: Kar poenostavi integracijo med LLM in MCP strežniki

#### Rust

Ta primer predpostavlja, da imate zagon MCP strežnika, ki je napisan v Rustu. Če ga še nimate, si oglejte lekcijo [01-first-server](../01-first-server/README.md), da ustvarite strežnik.

Ko imate Rust MCP strežnik, odprite terminal in se pomaknite do iste mape kot strežnik. Nato zaženite naslednji ukaz za ustvarjanje novega LLM odjemalskega projekta:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Dodajte naslednje odvisnosti v vašo datoteko `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Uradne Rust knjižnice za OpenAI ni, vendar je `async-openai` crate [skupnostno vzdrževana knjižnica](https://platform.openai.com/docs/libraries/rust#rust), ki se pogosto uporablja.

Odprite datoteko `src/main.rs` in zamenjajte njeno vsebino s spodnjo kodo:

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
    // Začetno sporočilo
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Nastavi OpenAI odjemalca
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Nastavi MCP odjemalca
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

    // NAREDITI: Pridobi seznam orodij MCP

    // NAREDITI: Pogovor LLM z uporabo klicev orodij

    Ok(())
}
```

Ta koda nastavi osnovno Rust aplikacijo, ki se bo povezala z MCP strežnikom in GitHub Modeli za interakcijo z LLM.

> [!IMPORTANT]
> Pred zagonom aplikacije poskrbite, da nastavite okoljsko spremenljivko `OPENAI_API_KEY` z vašim GitHub žetonom.

Odlično, za naslednji korak pa bomo našteli zmožnosti strežnika.

### -2- Naštevanje zmožnosti strežnika

Zdaj se bomo povezali s strežnikom in zahtevali njegove zmožnosti:

#### Typescript

V istem razredu dodajte naslednje metode:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // orodja za seznam
    const toolsResult = await this.client.listTools();
}
```

V zgornji kodi smo:

- Dodali kodo za povezovanje s strežnikom, `connectToServer`.
- Ustvarili metodo `run`, ki je odgovorna za upravljanje z aplikacijskim tokom. Do zdaj zgolj našteva orodja, kmalu pa bomo dodali še več.

#### Python

```python
# Naštej razpoložljive vire
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Naštej razpoložljiva orodja
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Tukaj pa smo dodali:

- Naštevanje virov in orodij in njihovo izpisovanje. Pri orodjih smo prav tako našteli `inputSchema`, katerega bomo kasneje uporabili.

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

V zgornji kodi smo:

- Našteli orodja, ki so na voljo na MCP strežniku
- Za vsako orodje našteli ime, opis in njen shematski opis. Ta slednji je nekaj, kar bomo kmalu uporabili za klic orodij.

#### Java

```java
// Ustvari ponudnika orodij, ki samodejno odkrije MCP orodja
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ponudnik orodij samodejno upravlja:
// - Prikaz razpoložljivih orodij z MCP strežnika
// - Pretvorbo shem MCP orodij v format LangChain4j
// - Upravljanje izvajanja orodij in odgovorov
```

V zgornji kodi smo:

- Ustvarili `McpToolProvider`, ki samodejno odkrije in registrira vsa orodja s MCP strežnika
- Ponudnik orodij interno upravlja pretvorbo med šemami MCP orodij in formatom orodij LangChain4j
- Ta pristop odpravlja ročno naštevanje in pretvorbo orodij

#### Rust

Pridobivanje orodij s MCP strežnika se opravi z metodo `list_tools`. V vaši funkciji `main`, po nastavitvi MCP odjemalca, dodajte naslednjo kodo:

```rust
// Pridobi seznam orodij MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Pretvorba zmožnosti strežnika v LLM orodja

Naslednji korak po naštetju zmožnosti strežnika je pretvorba le-teh v format, ki ga LLM razume. Ko to naredimo, lahko te zmožnosti ponudimo kot orodja našemu LLM.

#### TypeScript

1. Dodajte naslednjo kodo za pretvorbo odgovora MCP strežnika v orodja, ki jih LLM lahko uporabi:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Ustvari zod shemo na podlagi vhodne sheme
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Izrecno nastavi tip na "funkcija"
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

    Zgornja koda vzame odgovor MCP strežnika in ga pretvori v definicijo orodja, ki jo LLM razume.

1. Posodobimo sedaj metodo `run`, da naštete zmožnosti strežnika:

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

    V zgornji kodi smo posodobili metodo `run` tako, da preslikamo rezultat in za vsako vnos pokličemo `openAiToolAdapter`.

#### Python

1. Najprej ustvarimo naslednjo funkcijo za pretvorbo

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

    V funkciji `convert_to_llm_tools` sprejmemo MCP odziv orodja in ga pretvorimo v format, ki ga LLM lahko razume.

1. Naslednje posodobimo kodo našega odjemalca, da uporabi to funkcijo takole:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Tukaj kličemo `convert_to_llm_tool` za pretvorbo odgovora MCP orodja v nekaj, kar lahko kasneje posredujemo LLM.

#### .NET

1. Dodajmo kodo za pretvorbo MCP odgovora orodja v nekaj, kar LLM razume

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

V zgornji kodi smo:

- Ustvarili funkcijo `ConvertFrom`, ki sprejme ime, opis in vhodno shemo.
- Definirali funkcionalnost, ki ustvari FunctionDefinition, ki ga posreduje ChatCompletionsDefinition. Ta slednji del je nekaj, kar LLM razume.

1. Posodobimo sedaj nekaj obstoječe kode, da izkoristi to funkcijo:

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
// Ustvarite vmesnik robota za interakcijo v naravnem jeziku
public interface Bot {
    String chat(String prompt);
}

// Konfigurirajte AI storitev z orodji LLM in MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

V zgornji kodi smo:

- Definirali enostaven vmesnik `Bot` za naravne jezikovne interakcije
- Uporabili LangChain4j `AiServices`, da samodejno povežemo LLM s ponudnikom MCP orodij
- Okvir samodejno upravlja pretvorbo orodjnih shem in klic funkcij v ozadju
- Ta pristop odpravlja ročno pretvorbo orodij – LangChain4j upravlja vse podrobnosti pretvorbe MCP orodij v LLM združljiv format

#### Rust

Za pretvorbo MCP orodij v format, ki ga LLM razume, bomo dodali pomožno funkcijo, ki oblikuje seznam orodij. Dodajte naslednjo kodo v vašo datoteko `main.rs` pod funkcijo `main`. To funkcijo bomo klicali pri zahtevah po LLM:

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

Super, zdaj smo pripravljeni obdelati uporabniške zahteve, zato se lotimo še tega.

### -4- Obdelava uporabniških pozivov

V tem delu kode bomo obdelovali uporabniške zahteve.

#### TypeScript

1. Dodajte metodo, ki bo uporabljena za klic našega LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Pokliči strežnikov pripomoček
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Naredi nekaj z rezultatom
        // NAREDITI

        }
    }
    ```

    V zgornji kodi smo:

    - Dodali metodo `callTools`.
    - Metoda prejme odgovor LLM in preveri, katera orodja so bila poklicana, če sploh katera:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // pokliči orodje
        }
        ```

    - Pokliče orodje, če LLM nakaže, da je treba orodje poklicati:

        ```typescript
        // 2. Pokliči orodje strežnika
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Naredi nekaj z rezultatom
        // TODO
        ```

1. Posodobite metodo `run`, da vključuje klice LLM in `callTools`:

    ```typescript

    // 1. Ustvarite sporočila, ki so vnos za LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Klicanje LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Preverite odgovor LLM, za vsako možnost preverite, ali vsebuje klice orodij
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Odlično, tukaj je koda v celoti:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Uvozi zod za validacijo sheme

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // morda bo treba v prihodnosti spremeniti na ta URL: https://models.github.ai/inference
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
          // Ustvari zod shemo na podlagi input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Izrecno nastavi tip na "function"
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
    
    
          // 2. Pokliči orodje strežnika
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Naredi nekaj z rezultatom
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Preišči LLM odgovor, za vsak izbor preveri, če ima klice orodij
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

1. Dodajmo uvoze, potrebne za klic LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Nato dodajmo funkcijo, ki bo poklicala LLM:

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
            # Neobvezni parametri
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

    V zgornji kodi smo:

    - Posredovali funkcije, ki smo jih našli na MCP strežniku in jih pretvorili, LLM.
    - Nato poklicali LLM s temi funkcijami.
    - Nato pregledamo rezultat, da ugotovimo, katere funkcije bi morali poklicati, če sploh katere.
    - Nazadnje, posredujemo seznam funkcij za klic.

1. Zadnji korak, posodobimo glavno kodo:

    ```python
    prompt = "Add 2 to 20"

    # vprašaj LLM, katere orodja uporabiti, če sploh katera
    functions_to_call = call_llm(prompt, functions)

    # pokliči predlagane funkcije
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    To je bil zadnji korak, v zgornji kodi smo:

    - Poklicali MCP orodje preko `call_tool` z uporabo funkcije, ki jo je LLM ocenil, da jo je potrebno poklicati glede na poziv.
    - Izpisali rezultat klica orodja MCP strežniku.

#### .NET

1. Prikažimo kodo za izvedbo LLM poziva:

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

    V zgornji kodi smo:

    - Pridobili orodja iz MCP strežnika, `var tools = await GetMcpTools()`.
    - Definirali uporabniški poziv `userMessage`.
    - Sestavili objekt možnosti z modelom in orodji.
    - Poslali zahtevo LLM.

1. Še zadnji korak, preverimo, če LLM meni, da je potrebno poklicati funkcijo:

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

    V zgornji kodi smo:

    - Pregledali seznam klicev funkcij.
    - Za vsak klic orodja razčlenili ime in argumente ter poklicali orodje na MCP strežniku z uporabo MCP odjemalca. Nazadnje izpisali rezultate.

Tukaj je koda v celoti:

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
    // Izvedite zahteve v naravnem jeziku, ki samodejno uporabljajo orodja MCP
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

V zgornji kodi smo:

- Uporabili enostavne naravnojезikovne pozive za interakcijo z MCP orodji
- LangChain4j okvir samodejno upravlja:
  - Pretvorbo uporabniških pozivov v klice orodij, kadar je to potrebno
  - Klic ustreznih MCP orodij na podlagi odločitve LLM
  - Upravljanje poteka pogovora med LLM in MCP strežnikom
- Metoda `bot.chat()` vrne odgovore v naravnem jeziku, ki lahko vključujejo rezultate izvajanja MCP orodij
- Ta pristop nudi neprekinjeno uporabniško izkušnjo, kjer uporabniki ne potrebujejo poznavanja podlage MCP

Celoten primer kode:

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

Tukaj se zgodi večina dela. Poklicali bomo LLM z začetnim uporabniškim pozivom, nato pa bomo obdelali odgovor, da preverimo, ali je potrebno klicati katera orodja. Če je, bomo ta orodja poklicali in nadaljevali pogovor z LLM, dokler ne bo več potreb po klicih orodij in bomo imeli končen odgovor.

Naredili bomo več klicev LLM, zato definirajmo funkcijo, ki bo obravnavala klic LLM. Dodajte naslednjo funkcijo v `main.rs`:

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

Ta funkcija prejme LLM odjemalca, seznam sporočil (vključno z uporabniškim pozivom), orodja MCP strežnika in pošlje zahtevo LLM, ki vrne odgovor.
Odgovor iz LLM bo vseboval polje `choices`. Rezultat bomo morali obdelati, da preverimo, ali so prisotni `tool_calls`. To nam sporoči, da LLM zahteva, naj se določenemu orodju pokliče z argumenti. Dodajte naslednjo kodo na dno vaše datoteke `main.rs`, da definirate funkcijo za obdelavo LLM odgovora:

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

    // Izpiši vsebino, če je na voljo
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Obravnavaj klice orodij
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Dodaj sporočilo asistenta

        // Izvedi vsak klic orodja
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Dodaj rezultat orodja v sporočila
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Nadaljuj pogovor z rezultati orodij
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

Če so prisotni `tool_calls`, funkcija izlušči podatke o orodju, kliče MCP strežnik z zahtevo za orodje in doda rezultate v sporočila pogovora. Nato nadaljuje pogovor z LLM, sporočila pa se posodobijo z LLM-ovim odgovorom in rezultati klica orodja.

Da izvlečemo informacije o klicu orodja, ki jih LLM vrača za MCP klice, dodamo še eno pomožno funkcijo za pridobitev vsega potrebnega za klic. Dodajte naslednjo kodo na dno datoteke `main.rs`:

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

Z vsemi deli na svojem mestu lahko zdaj obdelamo začetni uporabniški poziv in pokličemo LLM. Posodobite vašo funkcijo `main` tako, da vključite naslednjo kodo:

```rust
// Pogovor LLM z orodnimi klici
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

Ta koda bo vprašala LLM za začetni uporabniški poziv, ki zahteva vsoto dveh števil, in bo obdelala odgovor, da dinamično upravlja klice orodij.

Odlično, uspelo vam je!

## Naloga

Vzemi kodo iz vaje in razširi strežnik z nekaj dodatnimi orodji. Nato ustvari klienta z LLM, kot v vaji, in ga preizkusi z različnimi pozivi, da zagotoviš, da se vsa orodja strežnika kličejo dinamično. Ta način izdelave klienta omogoča končnemu uporabniku odlično uporabniško izkušnjo, saj lahko uporablja pozive namesto natančnih ukazov klienta in ne opazi, da se kliče katerikoli MCP strežnik.

## Rešitev

[Rešitev](./solution/README.md)

## Ključne ugotovitve

- Dodajanje LLM k vašemu klientu omogoča boljši način interakcije uporabnikov s MCP strežniki.
- Potrebno je pretvoriti odgovor MCP strežnika v nekaj, kar LLM lahko razume.

## Vzorci

- [Java kalkulator](../samples/java/calculator/README.md)
- [.Net kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulator](../samples/javascript/README.md)
- [TypeScript kalkulator](../samples/typescript/README.md)
- [Python kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulator](../../../../03-GettingStarted/samples/rust)

## Dodatni viri

## Kaj sledi

- Naslednje: [Uporaba strežnika v Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->