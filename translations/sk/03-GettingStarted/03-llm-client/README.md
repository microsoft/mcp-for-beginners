# Vytvorenie klienta s LLM

Doteraz ste videli, ako vytvoriť server a klienta. Klient mohol explicitne volať server, aby zobrazil jeho nástroje, zdroje a výzvy. Avšak, nie je to veľmi praktický prístup. Váš používateľ žije v agentickej ére a očakáva, že bude používať výzvy a komunikovať s LLM, aby to dosiahol. Pre vášho používateľa nezáleží na tom, či používate MCP na ukladanie svojich schopností, ale očakáva, že bude používať prirodzený jazyk na interakciu. Ako to teda vyriešime? Riešením je pridať LLM ku klientovi.

## Prehľad

V tejto lekcii sa zameriame na pridanie LLM do vášho klienta a ukážeme, ako to poskytuje oveľa lepší zážitok pre vášho používateľa.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Vytvoriť klienta s LLM.
- Bezproblémovo komunikovať so serverom MCP pomocou LLM.
- Poskytnúť lepší zážitok koncovému používateľovi na strane klienta.

## Prístup

Poďme sa pokúsiť pochopiť prístup, ktorý musíme zvoliť. Pridanie LLM znie jednoducho, ale naozaj to tak urobíme?

Takto bude klient komunikovať so serverom:

1. Nadviazať spojenie so serverom.

1. Zoznam schopností, výziev, zdrojov a nástrojov a uložiť ich schému.

1. Pridať LLM a odovzdať uložené schopnosti a ich schému v formáte, ktorý LLM rozumie.

1. Spracovať používateľskú výzvu odovzdaním LLM spolu s nástrojmi, ktoré klient zobrazil.

Skvelé, teraz keď chápeme, ako to môžeme urobiť na vysokej úrovni, poďme to vyskúšať v nasledujúcom cvičení.

## Cvičenie: Vytvorenie klienta s LLM

V tomto cvičení sa naučíme pridať LLM do nášho klienta.

### Overenie pomocou GitHub Personal Access Token

Vytvorenie GitHub tokenu je jednoduchý proces. Tu je návod, ako to urobiť:

- Prejdite do nastavení GitHub – Kliknite na svoj profilový obrázok v pravom hornom rohu a vyberte Nastavenia.
- Prejdite do Developer Settings – Posuňte sa nadol a kliknite na Developer Settings.
- Vyberte Personal Access Tokens – Kliknite na Fine-grained tokens a potom na Generate new token.
- Nakonfigurujte svoj token – Pridajte poznámku pre referenciu, nastavte dátum vypršania platnosti a vyberte potrebné oprávnenia (scopes). V tomto prípade nezabudnite pridať oprávnenie Models.
- Vygenerujte a skopírujte token – Kliknite na Generate token a nezabudnite ho okamžite skopírovať, pretože ho už znova neuvidíte.

### -1- Pripojenie k serveru

Najprv si vytvorme klienta:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importujte zod pre validáciu schémy

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

V predchádzajúcom kóde sme:

- Importovali potrebné knižnice
- Vytvorili triedu s dvoma členmi, `client` a `openai`, ktoré nám pomôžu spravovať klienta a komunikovať s LLM.
- Nakonfigurovali inštanciu LLM na použitie GitHub Models nastavením `baseUrl` na inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Vytvorte parametre servera pre stdio pripojenie
server_params = StdioServerParameters(
    command="mcp",  # Spustiteľný súbor
    args=["run", "server.py"],  # Voliteľné argumenty príkazového riadku
    env=None,  # Voliteľné premenné prostredia
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializujte pripojenie
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

V predchádzajúcom kóde sme:

- Importovali potrebné knižnice pre MCP
- Vytvorili klienta

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

Najprv musíte pridať závislosti LangChain4j do vášho súboru `pom.xml`. Pridajte tieto závislosti, aby ste umožnili integráciu MCP a podporu GitHub Models:

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

Potom vytvorte svoju Java klientskú triedu:

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
    
    public static void main(String[] args) throws Exception {        // Nakonfigurujte LLM na použitie modelov GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Vytvorte MCP transport pre pripojenie k serveru
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Vytvorte MCP klienta
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

V predchádzajúcom kóde sme:

- **Pridali závislosti LangChain4j**: Potrebné pre integráciu MCP, oficiálneho OpenAI klienta a podporu GitHub Models
- **Importovali knižnice LangChain4j**: Pre integráciu MCP a funkčnosť OpenAI chat modelu
- **Vytvorili `ChatLanguageModel`**: Nakonfigurovaný na použitie GitHub Models s vaším GitHub tokenom
- **Nastavili HTTP transport**: Použitím Server-Sent Events (SSE) na pripojenie k MCP serveru
- **Vytvorili MCP klienta**: Ktorý bude spravovať komunikáciu so serverom
- **Použili vstavanú podporu MCP v LangChain4j**: Čo zjednodušuje integráciu medzi LLM a MCP servermi

#### Rust

Tento príklad predpokladá, že máte spustený MCP server založený na Rust. Ak ho nemáte, vráťte sa k lekcii [01-first-server](../01-first-server/README.md) a vytvorte server.

Keď máte svoj Rust MCP server, otvorte terminál a prejdite do rovnakého adresára ako server. Potom spustite nasledujúci príkaz na vytvorenie nového projektu LLM klienta:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Pridajte nasledujúce závislosti do súboru `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Neexistuje oficiálna Rust knižnica pre OpenAI, avšak `async-openai` crate je [knižnica udržiavaná komunitou](https://platform.openai.com/docs/libraries/rust#rust), ktorá sa bežne používa.

Otvorte súbor `src/main.rs` a nahraďte jeho obsah nasledujúcim kódom:

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
    // Počiatočná správa
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Nastavenie OpenAI klienta
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Nastavenie MCP klienta
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

    // TODO: Získať zoznam nástrojov MCP

    // TODO: Konverzácia LLM s volaniami nástrojov

    Ok(())
}
```

Tento kód nastavuje základnú Rust aplikáciu, ktorá sa pripojí k MCP serveru a GitHub Models pre interakcie s LLM.

> [!IMPORTANT]
> Pred spustením aplikácie nezabudnite nastaviť premennú prostredia `OPENAI_API_KEY` s vaším GitHub tokenom.

Skvelé, v ďalšom kroku si zobrazíme schopnosti servera.

### -2- Zobrazenie schopností servera

Teraz sa pripojíme k serveru a požiadame o jeho schopnosti:

#### Typescript

V tej istej triede pridajte nasledujúce metódy:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // zoznam nástrojov
    const toolsResult = await this.client.listTools();
}
```

V predchádzajúcom kóde sme:

- Pridali kód na pripojenie k serveru, `connectToServer`.
- Vytvorili metódu `run`, ktorá je zodpovedná za riadenie toku aplikácie. Zatiaľ iba zobrazuje nástroje, ale čoskoro pridáme viac.

#### Python

```python
# Zoznam dostupných zdrojov
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Zoznam dostupných nástrojov
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Tu je, čo sme pridali:

- Zobrazovanie zdrojov a nástrojov a ich výpis. Pre nástroje sme tiež zobrazili `inputSchema`, ktorý použijeme neskôr.

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

V predchádzajúcom kóde sme:

- Zobrazili nástroje dostupné na MCP serveri
- Pre každý nástroj sme zobrazili názov, popis a jeho schému. Túto schému použijeme na volanie nástrojov čoskoro.

#### Java

```java
// Vytvorte poskytovateľa nástrojov, ktorý automaticky objavuje MCP nástroje
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Poskytovateľ MCP nástrojov automaticky spracováva:
// - Zoznam dostupných nástrojov zo servera MCP
// - Konverziu schém MCP nástrojov do formátu LangChain4j
// - Správu vykonávania nástrojov a odpovedí
```

V predchádzajúcom kóde sme:

- Vytvorili `McpToolProvider`, ktorý automaticky objavuje a registruje všetky nástroje z MCP servera
- Poskytovateľ nástrojov interné spracováva konverziu medzi MCP schémami nástrojov a formátom nástrojov LangChain4j
- Tento prístup abstrahuje manuálne zobrazovanie a konverziu nástrojov

#### Rust

Získavanie nástrojov z MCP servera sa vykonáva pomocou metódy `list_tools`. Vo vašej funkcii `main`, po nastavení MCP klienta, pridajte nasledujúci kód:

```rust
// Získať zoznam nástrojov MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Konverzia schopností servera na LLM nástroje

Ďalším krokom po zobrazení schopností servera je ich konverzia do formátu, ktorému LLM rozumie. Keď to urobíme, môžeme tieto schopnosti poskytnúť ako nástroje nášmu LLM.

#### TypeScript

1. Pridajte nasledujúci kód na konverziu odpovede z MCP servera do formátu nástroja, ktorý LLM môže použiť:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Vytvorte zod schému na základe input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Explicitne nastavte typ na "function"
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

    Vyššie uvedený kód vezme odpoveď z MCP servera a konvertuje ju do definície nástroja, ktorú LLM rozumie.

1. Aktualizujme teraz metódu `run`, aby sme zobrazili schopnosti servera:

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

    V predchádzajúcom kóde sme aktualizovali metódu `run`, aby sme prešli výsledkom a pre každý záznam zavolali `openAiToolAdapter`.

#### Python

1. Najprv vytvorme nasledujúcu konverznú funkciu

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

    Vo funkcii `convert_to_llm_tools` prevádzame odpoveď MCP nástroja do formátu, ktorému LLM rozumie.

1. Potom aktualizujme náš klientsky kód, aby využíval túto funkciu takto:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Tu pridávame volanie `convert_to_llm_tool` na konverziu odpovede MCP nástroja na formát, ktorý môžeme neskôr poskytnúť LLM.

#### .NET

1. Pridajme kód na konverziu odpovede MCP nástroja do formátu, ktorému LLM rozumie

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

V predchádzajúcom kóde sme:

- Vytvorili funkciu `ConvertFrom`, ktorá prijíma názov, popis a vstupnú schému.
- Definovali funkcionalitu, ktorá vytvára `FunctionDefinition`, ktorý sa odovzdáva do `ChatCompletionsDefinition`. Toto je formát, ktorému LLM rozumie.

1. Pozrime sa, ako môžeme aktualizovať existujúci kód, aby využil túto funkciu:

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
// Vytvorte rozhranie bota pre interakciu v prirodzenom jazyku
public interface Bot {
    String chat(String prompt);
}

// Nakonfigurujte AI službu s nástrojmi LLM a MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

V predchádzajúcom kóde sme:

- Definovali jednoduché rozhranie `Bot` pre interakcie v prirodzenom jazyku
- Použili LangChain4j `AiServices` na automatické prepojenie LLM s poskytovateľom MCP nástrojov
- Framework automaticky spracováva konverziu schém nástrojov a volanie funkcií na pozadí
- Tento prístup eliminuje manuálnu konverziu nástrojov – LangChain4j rieši všetku zložitosť konverzie MCP nástrojov do formátu kompatibilného s LLM

#### Rust

Na konverziu odpovede MCP nástroja do formátu, ktorému LLM rozumie, pridáme pomocnú funkciu, ktorá naformátuje zoznam nástrojov. Pridajte nasledujúci kód do súboru `main.rs` pod funkciu `main`. Táto funkcia bude volaná pri požiadavkách na LLM:

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

Skvelé, sme pripravení spracovať používateľské požiadavky, poďme na to.

### -4- Spracovanie používateľskej výzvy

V tejto časti kódu budeme spracovávať požiadavky používateľa.

#### TypeScript

1. Pridajte metódu, ktorá bude používaná na volanie nášho LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Zavolajte nástroj servera
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Urobte niečo s výsledkom
        // TODO

        }
    }
    ```

    V predchádzajúcom kóde sme:

    - Pridali metódu `callTools`.
    - Metóda prijíma odpoveď LLM a kontroluje, ktoré nástroje boli volané, ak vôbec:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // zavolať nástroj
        }
        ```

    - Volá nástroj, ak LLM naznačí, že by mal byť volaný:

        ```typescript
        // 2. Zavolajte nástroj servera
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Urobte niečo s výsledkom
        // TODO
        ```

1. Aktualizujte metódu `run`, aby zahŕňala volania LLM a volanie `callTools`:

    ```typescript

    // 1. Vytvorte správy, ktoré sú vstupom pre LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Volanie LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Prejdite odpoveď LLM, pre každú možnosť skontrolujte, či obsahuje volania nástrojov
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Skvelé, tu je celý kód:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importujte zod pre validáciu schémy

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // možno bude potrebné v budúcnosti zmeniť na túto URL: https://models.github.ai/inference
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
          // Vytvorte zod schému na základe input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Explicitne nastavte typ na "function"
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
    
    
          // 2. Zavolajte nástroj servera
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Urobte niečo s výsledkom
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Prejdite odpoveď LLM, pre každú možnosť skontrolujte, či obsahuje volania nástrojov
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

1. Pridajme niektoré importy potrebné na volanie LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Potom pridajme funkciu, ktorá bude volať LLM:

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
            # Nepovinné parametre
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

    V predchádzajúcom kóde sme:

    - Odovzdali naše funkcie, ktoré sme našli na MCP serveri a konvertovali, LLM.
    - Potom sme zavolali LLM s týmito funkciami.
    - Následne kontrolujeme výsledok, aby sme zistili, ktoré funkcie by sme mali volať, ak vôbec.
    - Nakoniec odovzdávame pole funkcií na volanie.

1. Posledný krok, aktualizujme náš hlavný kód:

    ```python
    prompt = "Add 2 to 20"

    # opýtaj sa LLM, aké nástroje použiť, ak vôbec nejaké
    functions_to_call = call_llm(prompt, functions)

    # zavolaj navrhované funkcie
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Toto bol posledný krok, v kóde vyššie:

    - Voláme MCP nástroj cez `call_tool` pomocou funkcie, ktorú LLM vyhodnotil, že by sme mali volať na základe našej výzvy.
    - Vypisujeme výsledok volania nástroja na MCP server.

#### .NET

1. Ukážme kód na vykonanie požiadavky LLM promptu:

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

    V predchádzajúcom kóde sme:

    - Načítali nástroje z MCP servera, `var tools = await GetMcpTools()`.
    - Definovali používateľskú výzvu `userMessage`.
    - Vytvorili objekt možností špecifikujúci model a nástroje.
    - Vykonali požiadavku na LLM.

1. Posledný krok, pozrime sa, či LLM myslí, že by sme mali volať funkciu:

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

    V predchádzajúcom kóde sme:

    - Prešli zoznam volaní funkcií.
    - Pre každé volanie nástroja sme rozparsovali názov a argumenty a zavolali nástroj na MCP serveri pomocou MCP klienta. Nakoniec sme vypísali výsledky.

Tu je celý kód:

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
    // Vykonajte požiadavky v prirodzenom jazyku, ktoré automaticky používajú nástroje MCP
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

V predchádzajúcom kóde sme:

- Použili jednoduché výzvy v prirodzenom jazyku na interakciu s nástrojmi MCP servera
- Framework LangChain4j automaticky spracováva:
  - Konverziu používateľských výziev na volania nástrojov, keď je to potrebné
  - Volanie príslušných MCP nástrojov na základe rozhodnutia LLM
  - Riadenie toku konverzácie medzi LLM a MCP serverom
- Metóda `bot.chat()` vracia odpovede v prirodzenom jazyku, ktoré môžu obsahovať výsledky vykonania MCP nástrojov
- Tento prístup poskytuje plynulý používateľský zážitok, kde používatelia nemusia poznať podkladovú implementáciu MCP

Kompletný príklad kódu:

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

Tu sa odohráva väčšina práce. Zavoláme LLM s počiatočnou používateľskou výzvou, potom spracujeme odpoveď, aby sme zistili, či je potrebné volať nejaké nástroje. Ak áno, zavoláme tieto nástroje a budeme pokračovať v konverzácii s LLM, kým nebudú potrebné ďalšie volania nástrojov a nezískame konečnú odpoveď.

Budeme volať LLM viackrát, preto definujme funkciu, ktorá bude spracovávať volanie LLM. Pridajte nasledujúcu funkciu do súboru `main.rs`:

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

Táto funkcia prijíma LLM klienta, zoznam správ (vrátane používateľskej výzvy), nástroje z MCP servera a odosiela požiadavku LLM, pričom vracia odpoveď.
Odpoveď z LLM bude obsahovať pole `choices`. Budeme potrebovať spracovať výsledok, aby sme zistili, či sú prítomné nejaké `tool_calls`. To nám umožní vedieť, že LLM žiada o zavolanie konkrétneho nástroja s argumentmi. Pridajte nasledujúci kód na koniec vášho súboru `main.rs`, aby ste definovali funkciu na spracovanie odpovede LLM:

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

    // Vytlačiť obsah, ak je k dispozícii
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Spracovať volania nástrojov
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Pridať správu asistenta

        // Vykonať každé volanie nástroja
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Pridať výsledok nástroja do správ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Pokračovať v konverzácii s výsledkami nástrojov
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

Ak sú prítomné `tool_calls`, extrahuje informácie o nástroji, zavolá MCP server s požiadavkou nástroja a pridá výsledky do správ konverzácie. Následne pokračuje v konverzácii s LLM a správy sa aktualizujú s odpoveďou asistenta a výsledkami volania nástroja.

Na extrahovanie informácií o volaní nástroja, ktoré LLM vracia pre MCP volania, pridáme ďalšiu pomocnú funkciu na získanie všetkého potrebného na vykonanie volania. Pridajte nasledujúci kód na koniec vášho súboru `main.rs`:

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

Keď máme všetky časti na mieste, môžeme teraz spracovať počiatočný používateľský prompt a zavolať LLM. Aktualizujte svoju funkciu `main` tak, aby obsahovala nasledujúci kód:

```rust
// Konverzácia LLM s volaniami nástrojov
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

Týmto sa vykoná dotaz na LLM s počiatočným používateľským promptom, ktorý žiada o súčet dvoch čísel, a spracuje sa odpoveď na dynamické spracovanie volaní nástrojov.

Skvelé, podarilo sa vám to!

## Zadanie

Vezmite kód z cvičenia a rozšírte server o ďalšie nástroje. Potom vytvorte klienta s LLM, ako v cvičení, a otestujte ho s rôznymi promptmi, aby ste sa uistili, že všetky vaše serverové nástroje sa volajú dynamicky. Tento spôsob vytvárania klienta znamená, že koncový používateľ bude mať skvelý používateľský zážitok, pretože môže používať prompty namiesto presných klientskych príkazov a nebude si uvedomovať, že sa volá MCP server.

## Riešenie

[Riešenie](/03-GettingStarted/03-llm-client/solution/README.md)

## Kľúčové poznatky

- Pridanie LLM do vášho klienta poskytuje lepší spôsob, ako môžu používatelia komunikovať s MCP servermi.
- Je potrebné previesť odpoveď MCP servera na niečo, čomu LLM rozumie.

## Ukážky

- [Java kalkulačka](../samples/java/calculator/README.md)
- [.Net kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulačka](../samples/javascript/README.md)
- [TypeScript kalkulačka](../samples/typescript/README.md)
- [Python kalkulačka](../../../../03-GettingStarted/samples/python)
- [Rust kalkulačka](../../../../03-GettingStarted/samples/rust)

## Ďalšie zdroje

## Čo ďalej

- Ďalej: [Použitie servera vo Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->