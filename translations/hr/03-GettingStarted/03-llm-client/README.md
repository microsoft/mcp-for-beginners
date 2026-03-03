# Kreiranje klijenta s LLM-om

Do sada ste vidjeli kako kreirati server i klijenta. Klijent je mogao izričito pozvati server da nabroji njegove alate, resurse i upite. Međutim, to nije vrlo praktičan pristup. Vaši korisnici žive u agentskoj eri i očekuju koristiti upite i komunicirati s LLM-om. Nije im važno koristite li MCP za pohranu svojih mogućnosti; oni jednostavno očekuju komunicirati koristeći prirodni jezik. Pa kako to rješavamo? Rješenje je dodati LLM klijentu.

## Pregled

U ovoj lekciji fokusiramo se na dodavanje LLM-a vašem klijentu i pokazujemo kako to pruža puno bolje iskustvo za vašeg korisnika.

## Ciljevi učenja

Do kraja ove lekcije moći ćete:

- Kreirati klijenta s LLM-om.
- Bešavno surađivati sa MCP serverom koristeći LLM.
- Pružiti bolje krajnje korisničko iskustvo na strani klijenta.

## Pristup

Pokušajmo razumjeti pristup koji trebamo poduzeti. Dodavanje LLM-a zvuči jednostavno, ali hoćemo li to zapravo napraviti?

Evo kako će klijent komunicirati sa serverom:

1. Uspostavi vezu sa serverom.

1. Nabroji mogućnosti, upite, resurse i alate, te spremi njihov shematski prikaz.

1. Dodaj LLM i proslijedi spremljene mogućnosti i njihov shematski prikaz u formatu koji LLM razumije.

1. Rukuj korisničkim upitom prosljeđujući ga LLM-u zajedno s alatima nabrojanim od strane klijenta.

Odlično, sada kad razumijemo kako to možemo napraviti na visokoj razini, isprobajmo to u sljedećoj vježbi.

## Vježba: Kreiranje klijenta s LLM-om

U ovoj vježbi naučit ćemo kako dodati LLM našem klijentu.

### Autentifikacija pomoću GitHub Personal Access Tokena

Kreiranje GitHub tokena je jednostavan proces. Evo kako to možete napraviti:

- Idite na GitHub Settings – Kliknite na svoju profilnu sliku u gornjem desnom kutu i odaberite Settings.
- Navigirajte na Developer Settings – Skrolajte dolje i kliknite na Developer Settings.
- Odaberite Personal Access Tokens – Kliknite na Fine-grained tokens i zatim Generate new token.
- Konfigurirajte vaš token – Dodajte bilješku radi reference, postavite datum isteka i odaberite potrebne dozvole (scopeove). U ovom slučaju obavezno dodajte Models dozvolu.
- Generirajte i kopirajte token – Kliknite Generate token i odmah ga kopirajte jer ga nećete moći ponovno vidjeti.

### -1- Povežite se sa serverom

Prvo kreirajmo našeg klijenta:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Uvoz zoda za validaciju sheme

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
- Kreirali klasu s dva člana, `client` i `openai` koji će nam pomoći upravljati klijentom i komunicirati s LLM-om.
- Konfigurirali naš LLM primjerak da koristi GitHub Models postavljanjem `baseUrl` na inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Kreiraj parametre servera za stdio vezu
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
            # Inicijaliziraj vezu
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

Prvo trebate dodati LangChain4j ovisnosti u svoj `pom.xml` datoteku. Dodajte ove ovisnosti za omogućavanje MCP integracije i podrške za GitHub Models:

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

Zatim kreirajte svoju Java klijent klasu:

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

- **Dodali LangChain4j ovisnosti**: Potrebne za MCP integraciju, službeni OpenAI klijent i podršku za GitHub Models
- **Uvezli LangChain4j biblioteke**: Za MCP integraciju i OpenAI chat model funkcionalnost
- **Kreirali `ChatLanguageModel`**: Konfiguriran da koristi GitHub Models s vašim GitHub tokenom
- **Postavili HTTP transport**: Koristeći Server-Sent Events (SSE) za povezivanje s MCP serverom
- **Kreirali MCP klijenta**: Koji će upravljati komunikacijom sa serverom
- **Koristili ugrađenu LangChain4j MCP podršku**: Koja pojednostavljuje integraciju između LLM-a i MCP servera

#### Rust

Ovaj primjer pretpostavlja da imate Rust MCP server u radu. Ako ga nemate, vratite se na lekciju [01-first-server](../01-first-server/README.md) kako biste kreirali server.

Kada imate svoj Rust MCP server, otvorite terminal i navigirajte u isti direktorij kao server. Zatim pokrenite sljedeću naredbu za kreiranje novog LLM klijentskog projekta:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Dodajte sljedeće ovisnosti u datoteku `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Ne postoji službena Rust biblioteka za OpenAI, no `async-openai` je [zajednički održavana biblioteka](https://platform.openai.com/docs/libraries/rust#rust) koja se često koristi.

Otvorite datoteku `src/main.rs` i zamijenite njen sadržaj sljedećim kodom:

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

    // TODO: LLM razgovor s pozivima alata

    Ok(())
}
```

Ovaj kod postavlja osnovnu Rust aplikaciju koja se povezuje s MCP serverom i GitHub Models za LLM interakcije.

> [!IMPORTANT]
> Obavezno postavite `OPENAI_API_KEY` varijablu okoliša sa svojim GitHub tokenom prije pokretanja aplikacije.

Odlično, za sljedeći korak, nabrojimo mogućnosti na serveru.

### -2- Nabrojite mogućnosti servera

Sada ćemo se povezati sa serverom i zatražiti njegove mogućnosti:

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

- Dodali kod za povezivanje sa serverom, `connectToServer`.
- Kreirali metodu `run` koja upravlja našim tijekovima aplikacije. Do sada samo nabraja alate, ali ćemo uskoro dodati više u nju.

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

- Nabrajanje resursa i alata i ispis istih. Za alate također nabrajamo `inputSchema` koji ćemo kasnije koristiti.

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

- Nabrali alate dostupne na MCP serveru
- Za svaki alat nabrali ime, opis i njegov shematski prikaz. Ovo potonje ćemo uskoro koristiti za pozivanje alata.

#### Java

```java
// Kreirajte pružatelja alata koji automatski otkriva MCP alate
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Pružatelj MCP alata automatski obrađuje:
// - Popis dostupnih alata s MCP poslužitelja
// - Pretvaranje MCP shema alata u LangChain4j format
// - Upravljanje izvršavanjem alata i odgovorima
```

U prethodnom kodu smo:

- Kreirali `McpToolProvider` koji automatski pronalazi i registrira sve alate sa MCP servera
- Tool provider interno rukuje konverzijom između MCP schema alata i LangChain4j formata alata
- Ovaj pristup uklanja ručno nabrajanje i konverziju alata

#### Rust

Dohvaćanje alata s MCP servera obavlja se pomoću metode `list_tools`. U svojoj `main` funkciji, nakon postavljanja MCP klijenta, dodajte sljedeći kod:

```rust
// Dohvati popis MCP alata
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Pretvorite mogućnosti servera u LLM alate

Sljedeći korak nakon nabrajanja server mogućnosti je njihova konverzija u format koji LLM razumije. Kad to napravimo, možemo te mogućnosti ponuditi kao alate našem LLM-u.

#### TypeScript

1. Dodajte sljedeći kod za pretvaranje odgovora s MCP servera u format alata koji LLM može koristiti:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Napravite zod shemu temeljenu na input_schema
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

    Gornji kod prima odgovor s MCP servera i pretvara ga u definiciju alata koju LLM razumije.

1. Ažurirajmo sada `run` metodu da nabroji server mogućnosti:

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

    U prethodnom kodu smo ažurirali `run` metodu kako bi preslikala rezultat i za svaki unos pozvala `openAiToolAdapter`.

#### Python

1. Prvo, kreirajmo sljedeću funkciju za konverziju

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

    U funkciji iznad `convert_to_llm_tools` uzimamo MCP tool odgovor i pretvaramo ga u format koji LLM može razumjeti.

1. Zatim ažurirajmo klijentski kod da koristi ovu funkciju ovako:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Ovdje dodajemo poziv `convert_to_llm_tool` koji pretvara MCP tool odgovor u nešto što možemo poslati LLM-u kasnije.

#### .NET

1. Dodajmo kod za konverziju MCP tool odgovora u format koji LLM razumije

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

- Kreirali funkciju `ConvertFrom` koja prima ime, opis i shemu unosa.
- Definirali funkcionalnost koja kreira `FunctionDefinition` koji se prosljeđuje `ChatCompletionsDefinition`. Ovo potonje LLM može razumjeti.

1. Pogledajmo sada kako možemo ažurirati postojeći kod da iskoristi ovu funkciju:

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
// Kreirajte Bot sučelje za interakciju prirodnim jezikom
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
- Koristili LangChain4j `AiServices` da automatski povežemo LLM s MCP tool providerom
- Framework automatski rukuje konverzijom tool shema i pozivanjem funkcija u pozadini
- Ovaj pristup uklanja ručnu konverziju alata – LangChain4j rješava svu složenost pretvaranja MCP alata u LLM kompatibilan format

#### Rust

Da bismo MCP tool odgovor pretvorili u format koji LLM razumije, dodati ćemo pomoćnu funkciju koja formatira popis alata. Dodajte sljedeći kod u `main.rs` datoteku ispod `main` funkcije. Ovo će se pozivati kod zahtjeva prema LLM-u:

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

Odlično, sada smo postavljeni za rukovanje korisničkim zahtjevima, pa to riješimo sljedeće.

### -4- Rukovanje korisničkim upitom

U ovom dijelu koda rukovat ćemo korisničkim zahtjevima.

#### TypeScript

1. Dodajte metodu koja će se koristiti za pozivanje našeg LLM-a:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Pozovi alat poslužitelja
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Napravi nešto s rezultatom
        // ZA URADITI

        }
    }
    ```

    U prethodnom kodu:

    - Dodali smo metodu `callTools`.
    - Metoda prima LLM odgovor i provjerava koji su alati pozvani, ako ih ima:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // poziv alata
        }
        ```

    - Poziva alat, ako LLM indicira da bi se trebao pozvati:

        ```typescript
        // 2. Pozvati alat servera
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Napravite nešto s rezultatom
        // ZA NAPRAVITI
        ```

1. Ažurirajte `run` metodu da uključi pozive LLM-u i pozivanje `callTools`:

    ```typescript

    // 1. Kreirajte poruke koje su ulaz za LLM
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

    // 3. Prođite kroz odgovor LLM-a, za svaki izbor provjerite ima li pozive alata
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
import { z } from "zod"; // Uvezi zod za validaciju sheme

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // možda će u budućnosti trebati promijeniti na ovu URL adresu: https://models.github.ai/inference
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
          // Kreiraj zod shemu baziranu na input_schema
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
    
          // 3. Napravi nešto s rezultatom
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
    
        // 1. Prođi kroz odgovor LLM-a, za svaki izbor provjeri ima li pozive alata
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

1. Dodajmo potrebne uvoze za pozivanje LLM-a

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Zatim dodajmo funkciju koja će pozvati LLM:

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

    - Proslijedili funkcije koje smo pronašli na MCP serveru i konvertirali LLM-u.
    - Pozvali LLM s tim funkcijama.
    - Pregledali rezultat da vidimo koje funkcije treba pozvati, ako ih ima.
    - Na kraju, prosljeđujemo niz funkcija koje će se pozvati.

1. Završni korak, ažurirajmo glavni kod:

    ```python
    prompt = "Add 2 to 20"

    # pitaj LLM koje alate koristiti, ako uopće
    functions_to_call = call_llm(prompt, functions)

    # pozovi predložene funkcije
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Eto, to je bio završni korak, u gornjem kodu:

    - Pozivamo MCP alat preko `call_tool` koristeći funkciju za koju je LLM procijenio da treba biti pozvana na temelju upita.
    - Ispisujemo rezultat poziva alata MCP serveru.

#### .NET

1. Evo nekog koda za izvođenje LLM upita:

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
    - Definirali korisnički upit `userMessage`.
    - Konstruktor objekta s opcijama specificirajući model i alate.
    - Napravili zahtjev prema LLM-u.

1. Posljednji korak, pogledajmo hoće li LLM pozvati neku funkciju:

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

    - Prošli kroz listu poziva funkcija.
    - Za svaki alat parsirali ime i argumente i pozvali taj alat na MCP serveru koristeći MCP klijent. Na kraju ispisujemo rezultate.

Evo koda u cijelosti:

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

- Koristili jednostavne upite prirodnim jezikom za interakciju s MCP server alatima
- LangChain4j framework automatski rukuje:
  - Pretvaranjem korisničkih upita u pozive alata kada je potrebno
  - Pozivanjem odgovarajućih MCP alata na temelju odluke LLM-a
  - Upravljanjem tijekovima razgovora između LLM-a i MCP servera
- Metoda `bot.chat()` vraća odgovore prirodnim jezikom koji mogu uključivati rezultate izvršenja MCP alata
- Ovaj pristup pruža bešavno korisničko iskustvo gdje korisnici ne moraju znati o internom MCP mehanizmu

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

Ovdje se odvija većina posla. Pozvat ćemo LLM s početnim korisničkim upitom, zatim obraditi odgovor da vidimo treba li pozvati neke alate. Ako treba, pozvat ćemo te alate i nastaviti razgovor s LLM-om sve dok ne prestanu potrebni pozivi na alate i dok ne dobijemo završni odgovor.

Imat ćemo višestruke pozive na LLM, pa definirajmo funkciju koja će upravljati pozivom LLM-a. Dodajte sljedeću funkciju u vaš `main.rs` fajl:

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

Ova funkcija prima LLM klijenta, listu poruka (uključujući korisnički upit), alate s MCP servera i šalje zahtjev LLM-u, vraćajući odgovor.
Odgovor od LLM-a sadržavat će niz `choices`. Morat ćemo obraditi rezultat kako bismo provjerili jesu li prisutni `tool_calls`. To nam govori da LLM traži da se određeni alat pozove s argumentima. Dodajte sljedeći kod na dno vaše datoteke `main.rs` kako biste definirali funkciju za rukovanje LLM odgovorom:

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

Ako su prisutni `tool_calls`, izvuče informacije o alatu, pozove MCP server s zahtjevom za alat i doda rezultate porukama u razgovoru. Zatim nastavlja razgovor s LLM-om, a poruke se ažuriraju odgovorom asistenta i rezultatima poziva alata.

Da bismo izvukli informacije o pozivu alata koje LLM vraća za MCP pozive, dodati ćemo još jednu pomoćnu funkciju koja će izvući sve što je potrebno za poziv. Dodajte sljedeći kod na dno vaše datoteke `main.rs`:

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

Sa svim dijelovima na mjestu, sada možemo obraditi početni korisnički upit i pozvati LLM. Ažurirajte funkciju `main` da uključi sljedeći kod:

```rust
// Razgovor s LLM-om uz pozive na alate
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

Ovo će upitati LLM s početnim korisničkim upitom tražeći zbroj dvaju brojeva, te će obraditi odgovor kako bi dinamički upravljao pozivima alata.

Odlično, uspjeli ste!

## Zadatak

Uzeti kod iz vježbe i proširiti server s još alata. Zatim stvoriti klijent s LLM-om, kao u vježbi, i testirati ga s različitim upitima kako biste osigurali da se svi alati vašeg servera dinamički pozivaju. Ovakav način izrade klijenta omogućuje krajnjem korisniku izvrsno korisničko iskustvo jer može koristiti prirodne upite umjesto točnih naredbi klijenta, a pritom ne mora znati za eventualni poziv MCP servera.

## Rješenje

[Rješenje](/03-GettingStarted/03-llm-client/solution/README.md)

## Ključne spoznaje

- Dodavanje LLM-a vašem klijentu pruža bolji način za korisnike da komuniciraju s MCP serverima.
- Treba konvertirati odgovor MCP servera u nešto što LLM može razumjeti.

## Primjeri

- [Java kalkulator](../samples/java/calculator/README.md)
- [.Net kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulator](../samples/javascript/README.md)
- [TypeScript kalkulator](../samples/typescript/README.md)
- [Python kalkulator](../../../../03-GettingStarted/samples/python)
- [Rust kalkulator](../../../../03-GettingStarted/samples/rust)

## Dodatni resursi

## Što slijedi

- Sljedeće: [Konzumiranje servera pomoću Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj je dokument preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati ovlaštenim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->