# Izrada klijenta s LLM-om

Do sada ste vidjeli kako se stvara server i klijent. Klijent je mogao eksplicitno pozivati server kako bi dobio popis njegovih alata, resursa i promptova. Međutim, ovo nije baš praktičan pristup. Vaši korisnici žive u agentnoj eri i očekuju da koriste promptove i komuniciraju s LLM-om umjesto toga. Ne zanima ih koristite li MCP za pohranu svojih sposobnosti; oni jednostavno očekuju interakciju koristeći prirodni jezik. Kako to riješiti? Rješenje je dodati LLM klijentu.

## Pregled

U ovom ćemo poglavlju koristiti dodavanje LLM-a u vaš klijent i pokazati kako to pruža mnogo bolje iskustvo za vašeg korisnika.

## Ciljevi učenja

Do kraja ovog lekcije moći ćete:

- Izraditi klijenta s LLM-om.
- Besprijekorno komunicirati s MCP serverom koristeći LLM.
- Omogućiti bolje korisničko iskustvo na strani klijenta.

## Pristup

Pokušajmo razumjeti pristup koji trebamo poduzeti. Dodavanje LLM-a zvuči jednostavno, ali hoćemo li to doista učiniti?

Evo kako će klijent komunicirati sa serverom:

1. Uspostaviti vezu sa serverom.

1. Izlistati sposobnosti, promptove, resurse i alate te sačuvati njihov shemu.

1. Dodati LLM i proslijediti spremljene sposobnosti i njihove sheme u formatu koji LLM razumije.

1. Obraditi korisnički prompt prosljeđivanjem LLM-u zajedno s alatima koje je klijent izlistao.

Odlično, sada kad razumijemo kako to možemo napraviti na visokoj razini, pokušajmo to u sljedećoj vježbi.

## Vježba: Izrada klijenta s LLM-om

U ovoj vježbi ćemo naučiti kako dodati LLM našem klijentu.

### Autentifikacija pomoću GitHub Personal Access Tokena

Izrada GitHub tokena je jednostavan proces. Evo kako to možete napraviti:

- Idite na GitHub Postavke – Kliknite na svoju profilnu sliku u gornjem desnom kutu i odaberite Postavke.
- Navigirajte do Developer Settings – Skrolajte dolje i kliknite na Developer Settings.
- Odaberite Personal Access Tokens – Kliknite na Fine-grained tokens i zatim Generiraj novi token.
- Konfigurirajte svoj token – Dodajte bilješku za referencu, postavite datum isteka i odaberite potrebne pristupe (dozvole). U ovom slučaju obavezno dodajte Models dopuštenje.
- Generirajte i kopirajte token – Kliknite Generiraj token i odmah ga kopirajte jer ga više nećete moći vidjeti.

### -1- Spojite se na server

Prvo napravimo naš klijent:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Uvezi zod za provjeru valjanosti šeme

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

U prethodnom kodu smo:

- Uvezli potrebne biblioteke
- Kreirali klasu s dva člana, `client` i `openai`, koja nam pomažu upravljati klijentom i komunicirati s LLM-om
- Konfigurirali naš LLM instance da koristi GitHub Models postavljajući `baseUrl` na inferencijski API

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Kreirajte parametre servera za stdio vezu
server_params = StdioServerParameters(
    command="mcp",  # Izvršna datoteka
    args=["run", "server.py"],  # Opcionalni argumenti naredbenog retka
    env=None,  # Opcionalne varijable okoline
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicijalizirajte vezu
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

U prethodnom kodu smo:

- Uvezli potrebne biblioteke za MCP
- Kreirali klijenta

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

Prvo trebate dodati LangChain4j ovisnosti u svoj `pom.xml` file. Dodajte ove ovisnosti za omogućavanje MCP integracije i podrške za GitHub Models:

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

Zatim kreirajte svoju Java klijentsku klasu:

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
    
    public static void main(String[] args) throws Exception {        // Konfigurirajte LLM za korištenje GitHub modela
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Kreirajte MCP transport za povezivanje sa serverom
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Kreirajte MCP klijenta
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

U prethodnom kodu smo:

- **Dodali LangChain4j ovisnosti**: Potrebne za MCP integraciju, službeni OpenAI klijent, i podršku za GitHub Models
- **Uvezli LangChain4j biblioteke**: Za MCP integraciju i funkcionalnost OpenAI chat modela
- **Kreirali `ChatLanguageModel`**: Konfigurirano za korištenje GitHub Models s vašim GitHub tokenom
- **Postavili HTTP transport**: Koristeći Server-Sent Events (SSE) za povezivanje s MCP serverom
- **Kreirali MCP klijenta**: Koji upravlja komunikacijom sa serverom
- **Koristili ugrađenu MCP podršku LangChain4j-a**: Koja pojednostavljuje integraciju između LLM-a i MCP servera

#### Rust

Ovaj primjer pretpostavlja da imate Rust bazirani MCP server pokrenut. Ako nemate, vratite se na lekciju [01-first-server](../01-first-server/README.md) za kreiranje servera.

Nakon što imate Rust MCP server, otvorite terminal i navigirajte do mape u kojoj se nalazi server. Zatim pokrenite sljedeću naredbu da kreirate novi LLM klijentski projekt:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Dodajte sljedeće ovisnosti u svoj `Cargo.toml` file:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Ne postoji službena Rust biblioteka za OpenAI, no `async-openai` crate je [biblioteka održavana od strane zajednice](https://platform.openai.com/docs/libraries/rust#rust) koja se često koristi.

Otvorite `src/main.rs` i zamijenite njegov sadržaj s donjim kodom:

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
    // Početna poruka
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Postavljanje OpenAI klijenta
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Postavljanje MCP klijenta
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

    // TODO: Dohvati popis MCP alata

    // TODO: Razgovor LLM-a s pozivima alata

    Ok(())
}
```

Ovaj kod postavlja osnovnu Rust aplikaciju koja se povezuje na MCP server i GitHub Models za LLM interakcije.

> [!IMPORTANT]
> Prije pokretanja aplikacije obavezno postavite varijablu okoline `OPENAI_API_KEY` s vašim GitHub tokenom.

Odlično, za sljedeći korak, izlistajmo sposobnosti servera.

### -2- Izlistajte sposobnosti servera

Sada ćemo se spojiti na server i zatražiti njegove sposobnosti:

#### Typescript

U istoj klasi dodajte sljedeće metode:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // popis alata
    const toolsResult = await this.client.listTools();
}
```

U prethodnom kodu smo:

- Dodali kod za povezivanje na server, `connectToServer`.
- Kreirali `run` metodu odgovornu za tijek aplikacije. Do sada samo izlistava alate, ali ubrzo ćemo to proširiti.

#### Python

```python
# Popis dostupnih resursa
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Popis dostupnih alata
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Evo što smo dodali:

- Izlistavanje resursa i alata te njihovo ispisivanje. Za alate također izlistavamo `inputSchema` koji ćemo kasnije koristiti.

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

U prethodnom kodu smo:

- Izlistali alate dostupne na MCP serveru
- Za svaki alat izlistali ime, opis i njegovu shemu. Ovo zadnje ćemo koristiti za pozivanje alata uskoro.

#### Java

```java
// Stvorite pružatelja alata koji automatski otkriva MCP alate
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Pružatelj MCP alata automatski upravlja:
// - Popisivanjem dostupnih alata s MCP poslužitelja
// - Pretvaranjem MCP shema alata u LangChain4j format
// - Upravljanjem izvođenjem alata i odgovorima
```

U prethodnom kodu smo:

- Kreirali `McpToolProvider` koji automatski pronalazi i registrira sve alate s MCP servera
- Provider alata interno rukuje konverzijom između MCP alatnih shema i formata alata LangChain4j-a
- Ovaj pristup apstrahira ručno izlistavanje i konverziju alata

#### Rust

Dobivanje alata s MCP servera radi se pomoću metode `list_tools`. U funkciji `main`, nakon postavljanja MCP klijenta, dodajte sljedeći kod:

```rust
// Dohvati popis MCP alata
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Pretvorite sposobnosti servera u LLM alate

Sljedeći korak nakon izlistavanja sposobnosti servera je pretvoriti ih u format koji LLM razumije. Kad to učinimo, možemo te sposobnosti ponuditi kao alate LLM-u.

#### TypeScript

1. Dodajte sljedeći kod za pretvaranje odgovora sa MCP servera u format alata kojeg LLM može koristiti:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Napravite zod shemu na temelju input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Izričito postavite tip na "function"
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

    Gornji kod uzima odgovor s MCP servera i pretvara ga u definiciju alata koju LLM može razumjeti.

1. Sljedeće, ažurirajmo `run` metodu da izlista sposobnosti servera:

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

    U prethodnom kodu ažurirali smo `run` metodu da mapira rezultat i za svaki zapis poziva `openAiToolAdapter`.

#### Python

1. Prvo, napravimo sljedeću funkciju za konverziju

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

    U funkciji `convert_to_llm_tools` uzimamo odgovor MCP alata i pretvaramo ga u format koji LLM može razumjeti.

1. Zatim ažurirajmo naš klijentski kod da koristi ovu funkciju ovako:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Ovdje dodajemo poziv `convert_to_llm_tool` kako bismo pretvorili MCP alatni odgovor u format koji kasnije možemo dati LLM-u.

#### .NET

1. Dodajmo kod za pretvaranje MCP alatnog odgovora u format koji LLM može razumjeti

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

U prethodnom kodu smo:

- Kreirali funkciju `ConvertFrom` koja prima ime, opis i ulaznu shemu
- Definirali funkcionalnost koja kreira `FunctionDefinition` koja se prosljeđuje `ChatCompletionsDefinition`. Ovo zadnje LLM razumije.

1. Pogledajmo kako možemo osuvremeniti postojeći kod koristeći ovu funkciju:

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
// Izradite Bot sučelje za interakciju na prirodnom jeziku
public interface Bot {
    String chat(String prompt);
}

// Konfigurirajte AI uslugu s LLM i MCP alatima
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

U prethodnom kodu smo:

- Definirali jednostavan `Bot` interface za interakcije prirodnim jezikom
- Koristili LangChain4j-ove `AiServices` za automatsko povezivanje LLM-a s MCP providerom alata
- Framework automatski rukuje konverzijom shema alata i pozivanjem funkcija u pozadini
- Ovaj pristup uklanja ručnu konverziju alata — LangChain4j rješava svu složenost pretvaranja MCP alata u LLM-kompatibilan format

#### Rust

Za pretvaranje MCP alatnog odgovora u format koji LLM može razumjeti, dodati ćemo pomoćnu funkciju koja formatira popis alata. Dodajte sljedeći kod u `main.rs` ispod funkcije `main`. Ovo će se zvati prilikom slanja zahtjeva prema LLM-u:

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

Odlično, sada smo spremni obrađivati korisničke zahtjeve, pa krenimo s time.

### -4- Obradite korisnički prompt

U ovom dijelu koda obradit ćemo korisničke zahtjeve.

#### TypeScript

1. Dodajte metodu koju ćemo koristiti da pozovemo naš LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Pozovite alat poslužitelja
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Napravite nešto s rezultatom
        // ZA UČINITI

        }
    }
    ```

    U prethodnom kodu smo:

    - Dodali metodu `callTools`.
    - Metoda prima odgovor LLM-a i provjerava koji su alati, ako ih ima, pozvani:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // pozovi alat
        }
        ```

    - Poziva alat, ako LLM kaže da ga treba pozvati:

        ```typescript
        // 2. Pozovi alat servera
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Učini nešto s rezultatom
        // ZA UČINITI
        ```

1. Ažurirajmo `run` metodu da uključi pozive LLM-u i pozivanje `callTools`:

    ```typescript

    // 1. Kreiraj poruke koje su ulaz za LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Pozivanje LLM-a
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Prođi kroz odgovor LLM-a, za svaki izbor provjeri ima li pozive alata
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Odlično, evo kompletnog koda:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Uvoz zoda za validaciju sheme

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // možda će biti potrebno promijeniti na ovaj URL u budućnosti: https://models.github.ai/inference
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
          // Kreiraj zod shemu temeljenu na input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Izričito postavi tip na "function"
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
    
    
          // 2. Pozovi alat servera
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Uradi nešto s rezultatom
          // ZA NAPRAVITI
    
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
    
        // 1. Prođi kroz odgovor LLM-a, za svaki izbor provjeri ima li poziva alata
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

1. Dodajmo potrebne importove za pozivanje LLM-a

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Zatim, dodajmo funkciju koja će pozivati LLM:

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
            # Opcionalni parametri
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

    U prethodnom kodu smo:

    - Proslijedili funkcije koje smo pronašli na MCP serveru i pretvorili LLM-u.
    - Zatim smo pozvali LLM s tim funkcijama.
    - Pregledavamo rezultat da vidimo koje funkcije treba pozvati, ako ih ima.
    - Na kraju prosljeđujemo niz funkcija koje treba pozvati.

1. Završni korak, ažurirajmo glavni kod:

    ```python
    prompt = "Add 2 to 20"

    # pitaj LLM koje alate, ako ih ima
    functions_to_call = call_llm(prompt, functions)

    # pozovi predložene funkcije
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    To je bio završni korak, u gornjem kodu:

    - Pozivamo MCP alat preko `call_tool` koristeći funkciju koju je LLM odlučio pozvati prema našem promptu.
    - Ispisujemo rezultat poziva alata prema MCP serveru.

#### .NET

1. Evo koda za slanje LLM prompt zahtjeva:

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

    U prethodnom kodu smo:

    - Dohvatili alate s MCP servera, `var tools = await GetMcpTools()`.
    - Definirali korisnički prompt `userMessage`.
    - Konstruktor options objekta s modelom i alatima.
    - Poslali zahtjev prema LLM-u.

1. Još jedan korak, pogledajmo ako LLM smatra da treba pozvati funkciju:

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

    U prethodnom kodu smo:

    - Petljali kroz listu poziva funkcija.
    - Za svaki poziv alata parsirali ime i argumente te pozvali alat na MCP serveru koristeći MCP klijenta. Na kraju ispisujemo rezultate.

Evo kompletnog koda:

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
    // Izvršite zahtjeve na prirodnom jeziku koji automatski koriste MCP alate
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

U prethodnom kodu smo:

- Koristili jednostavne promptove prirodnog jezika za interakciju s MCP alatima
- LangChain4j framework automatski:
  - Pretvara korisničke promptove u pozive alata kada treba
  - Poziva odgovarajuće MCP alate temeljem odluke LLM-a
  - Upravljanja tijekom razgovora između LLM-a i MCP servera
- Metoda `bot.chat()` vraća odgovore u prirodnom jeziku koji mogu uključivati rezultate izvođenja MCP alata
- Ovaj pristup pruža besprijekorno korisničko iskustvo gdje korisnici ne trebaju znati o MCP implementaciji u pozadini

Kompletan primjer koda:

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

Ovdje se odvija većina posla. Pozvat ćemo LLM s početnim korisničkim promptom, zatim obraditi odgovor da vidimo treba li pozvati neke alate. Ako treba, pozvat ćemo te alate i nastaviti razgovor s LLM-om dok ne budu potrebni daljnji pozivi alata i dok ne dobijemo konačni odgovor.

Napravit ćemo više poziva prema LLM-u, stoga definirajmo funkciju koja će upravljati pozivima LLM-a. Dodajte sljedeću funkciju u svoj `main.rs`:

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

Ova funkcija prima LLM klijenta, listu poruka (uključujući korisnički prompt), alate s MCP servera i šalje zahtjev prema LLM-u, vraćajući odgovor.
Odgovor iz LLM-a sadržavat će niz `choices`. Trebat ćemo obraditi rezultat kako bismo vidjeli postoje li `tool_calls`. To nam omogućuje saznati traži li LLM da se pozove određeni alat s argumentima. Dodajte sljedeći kod na dno vaše datoteke `main.rs` kako biste definirali funkciju za rukovanje odgovorom LLM-a:

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

    // Ispiši sadržaj ako je dostupan
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Obradi pozive alata
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Dodaj poruku asistenta

        // Izvrši svaki poziv alata
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Dodaj rezultat alata u poruke
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Nastavi razgovor s rezultatima alata
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

Ako postoje `tool_calls`, izvuče informacije o alatu, pozove MCP poslužitelj s zahtjevom za alat i doda rezultate u poruke razgovora. Zatim nastavlja razgovor s LLM-om, a poruke se ažuriraju odgovorom pomoćnika i rezultatima poziva alata.

Da bismo izvukli informacije o pozivu alata koje LLM vraća za MCP pozive, dodati ćemo još jednu pomoćnu funkciju za izdvajanje svega što je potrebno za napraviti poziv. Dodajte sljedeći kod na dno svoje datoteke `main.rs`:

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

Svim dijelovima na mjestu, sada možemo obraditi početni korisnički upit i pozvati LLM. Ažurirajte svoju funkciju `main` da uključuje sljedeći kod:

```rust
// LLM razgovor s pozivima alata
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

Ovo će poslati upit LLM-u s početnim korisničkim upitom tražeći zbroj dva broja i obradit će odgovor kako bi dinamički upravljao pozivima alata.

Odlično, uspjeli ste!

## Zadatak

Uzmite kod iz vježbe i razvijte poslužitelj s još nekoliko alata. Zatim stvorite klijenta s LLM-om, kao u vježbi, i testirajte ga s različitim upitima kako biste se uvjerili da se svi alati vašeg poslužitelja pozivaju dinamički. Ovakav način izrade klijenta znači da će krajnji korisnik imati izvrsno korisničko iskustvo jer može koristiti upite umjesto točnih naredbi klijenta i ne mora biti svjestan da se poziva neki MCP poslužitelj.

## Rješenje

[Rješenje](./solution/README.md)

## Ključne spoznaje

- Dodavanje LLM-a u vaš klijent pruža bolji način za korisnike da komuniciraju s MCP poslužiteljima.
- Potrebno je pretvoriti odgovor MCP poslužitelja u nešto što LLM može razumjeti.

## Primjeri

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulator](../../../../03-GettingStarted/samples/rust)

## Dodatni resursi

## Što slijedi

- Sljedeće: [Korištenje poslužitelja u Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge prijevoda [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo vas da imate na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati službenim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili pogrešna tumačenja proizašla iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->