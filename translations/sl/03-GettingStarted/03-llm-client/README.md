# Ustvarjanje odjemalca z LLM

Do zdaj ste videli, kako ustvariti strežnik in odjemalca. Odjemalec je lahko neposredno poklical strežnik, da izpiše njegove orodja, vire in pozive. Vendar to ni zelo praktičen pristop. Vaši uporabniki živijo v agentnem obdobju in pričakujejo uporabo pozivov ter komunikacijo z LLM. Ne zanima jih, ali uporabljate MCP za shranjevanje svojih zmogljivosti; preprosto pričakujejo, da bodo lahko komunicirali z naravnim jezikom. Kako torej to rešimo? Rešitev je dodati LLM odjemalcu.

## Pregled

V tej lekciji se osredotočimo na dodajanje LLM vašemu odjemalcu in pokažemo, kako to uporabniku zagotavlja veliko boljšo izkušnjo.

## Cilji učenja

Ob koncu te lekcije boste znali:

- Ustvariti odjemalca z LLM.
- Brezhibno komunicirati z MCP strežnikom prek LLM.
- Zagotoviti boljšo uporabniško izkušnjo na strani odjemalca.

## Pristop

Poskusimo razumeti pristop, ki ga moramo uporabiti. Dodajanje LLM se sliši preprosto, a ali ga bomo res implementirali?

Tako bo odjemalec komuniciral s strežnikom:

1. Vzpostavi povezavo s strežnikom.

1. Izpiše zmogljivosti, pozive, vire in orodja ter shrani njihov shematski opis.

1. Doda LLM in podaja shranjene zmogljivosti ter njihovo shemo v obliki, ki jo LLM razume.

1. Obravnava uporabniški poziv tako, da ga posreduje LLM skupaj z orodji, ki jih je našel odjemalec.

Super, zdaj ko razumemo visok nivo, kako to doseči, poskusimo spodnjo vajo.

## Vaja: Ustvarjanje odjemalca z LLM

V tej vaji se bomo naučili dodati LLM našemu odjemalcu.

### Avtentikacija z GitHub osebni dostopni žeton

Ustvarjanje GitHub žetona je preprost postopek. Tako ga lahko naredite:

- Pojdite v Nastavitve GitHub – Kliknite na svojo profilno sliko zgoraj desno in izberite Nastavitve.
- Pomaknite se do Nastavitev razvijalca – Pomaknite se navzdol in kliknite Nastavitve razvijalca.
- Izberite osebne dostopne žetone – Kliknite na Žetoni z določenimi dovoljenji in nato Ustvari nov žeton.
- Konfigurirajte svoj žeton – Dodajte opombo za referenco, nastavite datum poteka in izberite potrebne obsege (dovoljenja). V tem primeru poskrbite, da dodate dovoljenje Models.
- Ustvarite in kopirajte žeton – Kliknite Ustvari žeton in ga takoj kopirajte, ker ga kasneje ne boste mogli več videti.

### -1- Povezava s strežnikom

Najprej ustvarimo našega odjemalca:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Uvozi zod za validacijo sheme

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
- Ustvarili razred z dvema članoma, `client` in `openai`, ki nam pomagata upravljati odjemalca in komunicirati z LLM.
- Konfigurirali naš LLM primerek, da uporablja GitHub Models z nastavitvijo `baseUrl` na inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Ustvarite parametre strežnika za stdio povezavo
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
            # Inicializirajte povezavo
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

Najprej morate v `pom.xml` datoteko dodati odvisnosti LangChain4j. Dodajte te odvisnosti, da omogočite integracijo MCP in podporo za GitHub Models:

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

Nato ustvarite razred Java odjemalca:

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

- **Dodali odvisnosti LangChain4j**: potrebne za integracijo MCP, uradnega OpenAI odjemalca in podporo GitHub Models
- **Uvozili knjižnice LangChain4j**: za integracijo MCP in funkcionalnost OpenAI klepetalnega modela
- **Ustvarili `ChatLanguageModel`**: konfiguriran za uporabo GitHub Models z vašim GitHub žetonom
- **Nastavili HTTP prenos**: z uporabo Server-Sent Events (SSE) za povezavo s MCP strežnikom
- **Ustvarili MCP odjemalca**: ki bo upravljal komunikacijo s strežnikom
- **Uporabili vgrajeno podporo MCP v LangChain4j**: kar poenostavlja integracijo med LLM in MCP strežniki

#### Rust

Ta primer predvideva, da imate zagnan MCP strežnik na Rustu. Če ga nimate, se vrnite na lekcijo [01-first-server](../01-first-server/README.md) za ustvarjanje strežnika.

Ko imate Rust MCP strežnik, odprite terminal in pojdite v isto mapo kot strežnik. Nato zaženite naslednji ukaz za ustvarjanje novega LLM odjemalskega projekta:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Dodajte naslednje odvisnosti v vašo `Cargo.toml` datoteko:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Za Rust ni uradne knjižnice za OpenAI, vendar je `async-openai` crate [skupnostno vzdrževana knjižnica](https://platform.openai.com/docs/libraries/rust#rust), ki se pogosto uporablja.

Odprite datoteko `src/main.rs` in zamenjajte njeno vsebino z naslednjo kodo:

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

    // TODO: Pridobi seznam orodij MCP

    // TODO: Pogovor LLM z klici orodij

    Ok(())
}
```

Ta koda nastavi osnovno Rust aplikacijo, ki se bo povezana s MCP strežnikom in GitHub Models za interakcijo z LLM.

> [!IMPORTANT]
> Pred zagonom aplikacije poskrbite, da nastavite okoljsko spremenljivko `OPENAI_API_KEY` z vašim GitHub žetonom.

Super, za naslednji korak pa poglejmo zmogljivosti strežnika.

### -2- Izpis zmogljivosti strežnika

Zdaj se bomo povezali s strežnikom in zahtevali njegove zmogljivosti:

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

- Dodali kodo za povezovanje s strežnikom `connectToServer`.
- Ustvarili metodo `run`, ki skrbi za tok vaše aplikacije. Za zdaj izpiše samo orodja, a kmalu ji bomo dodali več.

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

Tukaj je, kar smo dodali:

- Izpis virov in orodij ter izpisali rezultate. Pri orodjih izpišemo tudi `inputSchema`, ki ga bomo kasneje uporabili.

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

- Izpisali orodja, ki so na voljo na MCP strežniku
- Za vsako orodje izpisali ime, opis in njegovo shemo. Ta shema bo kasneje uporabljena za klice orodij.

#### Java

```java
// Ustvarite ponudnika orodij, ki samodejno odkrije MCP orodja
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Ponudnik MCP orodij samodejno upravlja:
// - Seznam razpoložljivih orodij s strežnika MCP
// - Pretvarjanje shem MCP orodij v LangChain4j format
// - Upravljanje izvajanja orodij in odgovorov
```

V zgornji kodi smo:

- Ustvarili `McpToolProvider`, ki samodejno odkrije in registrira vsa orodja iz MCP strežnika.
- Ponudnik orodij interno obdela pretvorbo med shemami MCP orodij in LangChain4j orodji.
- Ta pristop odstrani potrebo po ročnem izpisu in pretvorbi orodij.

#### Rust

Pridobivanje orodij z MCP strežnika je mogoče z metodo `list_tools`. V `main` funkciji, potem ko nastavite MCP odjemalca, dodajte naslednjo kodo:

```rust
// Pridobite seznam orodij MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Pretvorba zmogljivosti strežnika v LLM orodja

Naslednji korak po izpisu zmogljivosti strežnika je, da jih pretvorimo v format, ki ga LLM razume. Ko to dosežemo, jim lahko kot orodjem omogočimo dostop do našega LLM.

#### TypeScript

1. Dodajte naslednjo kodo, ki pretvori odgovor MCP strežnika v format orodja, ki ga lahko uporablja LLM:

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

    Zgornja koda sprejme odgovor iz MCP strežnika in ga pretvori v definicijo orodja, ki jo LLM razume.

1. Naslednji korak je posodobitev metode `run`, da izpiše zmogljivosti strežnika:

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

    V zgornji kodi smo posodobili metodo `run`, da prehodi skozi rezultat in za vsak vnos kliče `openAiToolAdapter`.

#### Python

1. Najprej ustvarimo naslednjo funkcijo za pretvorbo:

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

    Funkcija `convert_to_llm_tools` sprejme odgovor MCP orodja in ga pretvori v format, ki ga razume LLM.

1. Nato posodobimo našo odjemalsko kodo, da uporabi to funkcijo tako:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Tukaj dodajamo klic `convert_to_llm_tool`, ki pretvori MCP odgovor orodja v nekaj, kar lahko kasneje predamo LLM.

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

- Ustvarili funkcijo `ConvertFrom`, ki prejme ime, opis in vhodno shemo.
- Definirali funkcionalnost, ki ustvari `FunctionDefinition`, ki je nato predan `ChatCompletionsDefinition`. Slednje razume LLM.

1. Poglejmo, kako lahko posodobimo obstoječo kodo, da izkoristimo zgornjo funkcijo:

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
// Ustvarite vmesnik za bota za interakcijo v naravnem jeziku
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

- Definirali preprost vmesnik `Bot` za interakcijo z naravnim jezikom
- Uporabili LangChain4j `AiServices`, ki samodejno poveže LLM z MCP ponudnikom orodij
- Okvir avtomatsko upravlja pretvorbo shem orodij in klic funkcij v ozadju
- Ta pristop odstrani ročno pretvorbo orodij – LangChain4j poskrbi za vso kompleksnost konverzije MCP orodij v LLM združljiv format

#### Rust

Da bomo pretvorili MCP odgovor orodja v format, ki ga LLM razume, bomo dodali pomožno funkcijo, ki formatira seznam orodij. Dodajte naslednjo kodo v vašo datoteko `main.rs` pod funkcijo `main`. To bo poklicano ob zahtevah LLM:

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

Super, zdaj smo pripravljeni za obravnavo uporabniških zahtev.

### -4- Obravnava uporabniških pozivov

V tem delu kode bomo obravnavali uporabniške zahteve.

#### TypeScript

1. Dodajte metodo, ki bo klicala naš LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Pokliči strežniško orodje
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Naredi nekaj z rezultatom
        // NAREDI

        }
    }
    ```

    V zgornji kodi smo:

    - Dodali metodo `callTools`.
    - Metoda sprejme odgovor LLM in preveri, katera orodja so bila zahtevana, če sploh:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // pokliči orodje
        }
        ```

    - Pokliče orodje, če LLM predlaga njegov klic:

        ```typescript
        // 2. Pokliči strežniško orodje
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

    // 1. Ustvari sporočila, ki so vhod za LLM
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

    // 3. Preglej odgovor LLM, za vsako izbiro preveri, če vsebuje klice orodij
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Super, oglejmo si kodo celotno:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Uvozi zod za preverjanje sheme

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // morda bo v prihodnosti treba spremeniti na to URL: https://models.github.ai/inference
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
    
        // 1. Preglej odgovor LLM, za vsako izbiro preveri, če vsebuje klice orodja
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

1. Dodajmo potrebne uvoze za klic LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Nato dodajmo funkcijo, ki kliče LLM:

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
            # Izbirni parametri
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

    - Poslali funkcije, ki smo jih našli na MCP strežniku in pretvorili, LLM.
    - Potem poklicali LLM z omenjenimi funkcijami.
    - Nato preučujemo rezultat, da vidimo, katere funkcije naj pokličemo, če sploh.
    - Nazadnje posredujemo niz funkcij za klic.

1. Zadnji korak, posodobimo glavno kodo:

    ```python
    prompt = "Add 2 to 20"

    # vprašaj LLM, katere orodja uporabiti, če sploh kakšna
    functions_to_call = call_llm(prompt, functions)

    # kliči predlagane funkcije
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Tukaj, v zgornji kodi, smo:

    - Poklicali MCP orodje prek `call_tool` z uporabo funkcije, ki jo je LLM predlagal glede na poziv.
    - Izpisali rezultat klica orodja na MCP strežnik.

#### .NET

1. Pokažimo kodo za poizvedbo LLM poziva:

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

    - Pridobili orodja z MCP strežnika, `var tools = await GetMcpTools()`.
    - Določili uporabniški poziv `userMessage`.
    - Konstrukcijski objekt z modelom in orodji.
    - Poslali zahtevek LLM.

1. Še zadnji korak, preverimo, če LLM meni, da naj pokličemo funkcijo:

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

    - Zanka čez seznam funkcijskih klicev.
    - Za vsak klic orodja razčlenimo ime in argumente ter kličemo orodje na MCP strežniku z MCP odjemalcem. Na koncu izpisujemo rezultate.

Tu je celotna koda:

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
    // Izvedi naravne jezikovne zahteve, ki samodejno uporabljajo MCP orodja
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

- Uporabili preproste pozive v naravnem jeziku za interakcijo z orodji MCP strežnika
- Okvir LangChain4j samodejno upravlja:
  - Pretvorbo uporabniških pozivov v klice orodij, kadar je potrebno
  - Klic ustreznih MCP orodij glede na odločitev LLM
  - Upravljanje poteka pogovora med LLM in MCP strežnikom
- Metoda `bot.chat()` vrne odgovore v naravnem jeziku, ki lahko vključujejo rezultate opravil MCP orodij
- Ta pristop ponuja brezhibno uporabniško izkušnjo, kjer uporabniki ne potrebujejo vedeti za podlago MCP implementacije

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

Tu se zgodi večina dela. Začeli bomo z začetnim uporabniškim pozivom k LLM, nato pa obdelali odgovor, da preverimo, ali je potrebno katero orodje poklicati. Če je, bomo poklicali orodja in nadaljevali pogovor z LLM, dokler ne bodo potrebni nadaljnji klici orodij in dobimo končni odgovor.

Ker bomo LLM večkrat klicali, definirajmo funkcijo, ki bo obravnavala LLM klic. Dodajte naslednjo funkcijo v datoteko `main.rs`:

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

Funkcija prejme LLM odjemalca, seznam sporočil (vključno z uporabniškim pozivom), orodja z MCP strežnika in pošlje zahtevek LLM ter vrne odgovor.
Odgovor iz LLM bo vseboval polje `choices`. Rezultat bo treba obdelati, da preverimo, ali so prisotni `tool_calls`. To nam pove, da LLM zahteva uporabo določenega orodja z argumenti. Dodajte naslednjo kodo na konec vaše datoteke `main.rs`, da definirate funkcijo za obdelavo odgovora LLM:

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

    // Natisni vsebino, če je na voljo
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Obdelaj klice orodij
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

Če so prisotni `tool_calls`, izlušči informacije o orodju, pokliče MCP strežnik z zahtevo za orodje in doda rezultate sporočilom v pogovoru. Nato nadaljuje pogovor z LLM in sporočila se posodobijo z odgovorom asistenta in rezultati klicev orodja.

Da izvlečemo informacije o klicu orodja, ki jih LLM vrne za MCP klice, bomo dodali še eno pomožno funkcijo, ki izlušči vse potrebno za izvedbo klica. Dodajte naslednjo kodo na konec vaše datoteke `main.rs`:

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

Z vsemi deli na mestu lahko zdaj obdelamo začetni uporabniški poziv in pokličemo LLM. Posodobite svojo funkcijo `main`, da bo vsebovala naslednjo kodo:

```rust
// Pogovor z LLM z orodnimi klici
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

To bo poslalo poizvedbo LLM z začetnim uporabniškim pozivom za seštevek dveh števil in obdelalo odgovor za dinamično upravljanje klicev orodij.

Čestitke, uspelo vam je!

## Naloga

Vzemite kodo iz vaje in razširite strežnik z nekaj dodatnimi orodji. Nato ustvarite klienta z LLM, kot v vaji, in ga preizkusite z različnimi pozivi, da zagotovite, da se vsa orodja strežnika dinamično kličejo. Ta način gradnje klienta pomeni, da bo končni uporabnik imel odlično uporabniško izkušnjo, saj lahko uporablja pozive namesto natančnih ukazov klienta in ne bo opazil klica MCP strežnika.

## Rešitev

[Rešitev](/03-GettingStarted/03-llm-client/solution/README.md)

## Ključne ugotovitve

- Dodajanje LLM v vašega klienta omogoča boljši način interakcije uporabnikov z MCP strežniki.
- Odgovor MCP strežnika je treba pretvoriti v nekaj, kar LLM lahko razume.

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
**Opozorilo**:
Dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za točnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku naj velja za verodostojen vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->