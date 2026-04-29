# Vytvorenie klienta s LLM

Doteraz ste videli, ako vytvoriť server a klienta. Klient mohol explicitne volať server, aby zobrazil jeho nástroje, zdroje a prompt-y. Toto však nie je veľmi praktický prístup. Vaši používatelia žijú v agentickej dobe a očakávajú používanie promptov a komunikáciu s LLM. Nezaujíma ich, či používate MCP na uloženie svojich schopností; jednoducho očakávajú interakciu v prirodzenom jazyku. Ako teda túto situáciu vyriešime? Riešením je pridať LLM ku klientovi.

## Prehľad

V tejto lekcii sa zameriame na pridanie LLM ku klientovi a ukážeme, ako to poskytuje oveľa lepšiu používateľskú skúsenosť.

## Ciele učenia

Na konci tejto lekcie budete vedieť:

- Vytvoriť klienta s LLM.
- Bezproblémovo komunikovať so serverom MCP pomocou LLM.
- Poskytnúť lepšiu používateľskú skúsenosť na strane klienta.

## Prístup

Skúsme pochopiť prístup, ktorý musíme použiť. Pridať LLM znie jednoducho, ale naozaj to tak urobíme?

Takto bude klient komunikovať so serverom:

1. Nadviaže spojenie so serverom.

1. Zobrazí zoznam schopností, promptov, zdrojov a nástrojov a uloží ich schému.

1. Pridá LLM a predá uložené schopnosti a ich schému v formáte, ktorý LLM rozumie.

1. Spracuje používateľský prompt tak, že ho predá LLM spolu s nástrojmi uvedenými klientom.

Skvelé, teraz keď chápeme, ako to môžeme urobiť na vysokej úrovni, vyskúšajme to v nasledujúcej úlohe.

## Cvičenie: Vytvorenie klienta s LLM

V tomto cvičení sa naučíme pridať LLM ku nášmu klientovi.

### Overenie prostredníctvom GitHub Personal Access Tokenu

Vytvorenie GitHub tokenu je jednoduchý proces. Tu je, ako to urobíte:

- Prejdite na GitHub Nastavenia – Kliknite na svoj profilový obrázok v pravom hornom rohu a vyberte Nastavenia.
- Prejdite do Vývojárskych nastavení – Posuňte sa nadol a kliknite na Vývojárske nastavenia.
- Vyberte Personal Access Tokens – Kliknite na Fine-grained tokeny a potom Generujte nový token.
- Nastavte svoj token – Pridajte poznámku pre referenciu, nastavte dátum vypršania a vyberte potrebné rozsahy (oprávnenia). V tomto prípade nezabudnite pridať oprávnenie Models.
- Vygenerujte a skopírujte token – Kliknite na Generovať token a nezabudnite ho hneď skopírovať, pretože ho už znova neuvidíte.

### -1- Pripojenie k serveru

Najskôr vytvorme nášho klienta:

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
- Nakonfigurovali inštanciu LLM, aby používala GitHub Models nastavením `baseUrl` na inference API.

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

Najskôr pridajte závislosti LangChain4j do vášho súboru `pom.xml`. Pridajte tieto závislosti, aby ste umožnili integráciu MCP a podporu GitHub Models:

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

Potom vytvorte svoju Java klientsku triedu:

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
- **Vytvorili `ChatLanguageModel`**: Nakonfigurovaný na použitie GitHub Models s vašim GitHub tokenom
- **Nastavili HTTP transport**: Použitím Server-Sent Events (SSE) na pripojenie k MCP serveru
- **Vytvorili MCP klienta**: Ktorý sa bude starať o komunikáciu so serverom
- **Použili vstavanú podporu MCP v LangChain4j**: Čo zjednodušuje integráciu medzi LLM a MCP servermi

#### Rust

Tento príklad predpokladá, že máte spustený MCP server založený na Rust. Ak ho nemáte, vráťte sa späť k lekcii [01-first-server](../01-first-server/README.md), kde sa server vytvára.

Ak máte Rust MCP server, otvorte terminál a prejdite do toho istého adresára ako server. Potom spustite nasledujúci príkaz na vytvorenie nového projektu LLM klienta:

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
> Neexistuje oficiálna Rust knižnica pre OpenAI, avšak balíček `async-openai` je [knižnica udržiavaná komunitou](https://platform.openai.com/docs/libraries/rust#rust), ktorá sa bežne používa.

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

    // Nastaviť klienta OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Nastaviť klienta MCP
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

Tento kód nastavuje základnú Rust aplikáciu, ktorá sa pripojí ku MCP serveru a GitHub Models pre interakcie s LLM.

> [!IMPORTANT]
> Nezabudnite nastaviť premennú prostredia `OPENAI_API_KEY` so svojím GitHub tokenom pred spustením aplikácie.

Skvelé, v ďalšom kroku zobrazíme zoznam schopností na serveri.

### -2- Zobrazenie schopností servera

Teraz sa pripojíme k serveru a požiadame o jeho schopnosti:

#### Typescript

Do rovnakej triedy pridajte nasledujúce metódy:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // výpis nástrojov
    const toolsResult = await this.client.listTools();
}
```

V predchádzajúcom kóde sme:

- Pridali kód na pripojenie k serveru, `connectToServer`.
- Vytvorili metódu `run`, ktorá riadi tok našej aplikácie. Zatiaľ iba zobrazuje nástroje, ale čoskoro ju rozšírime.

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

Pridali sme:

- Zobrazenie zdrojov a nástrojov s ich výpisom. Pre nástroje tiež zobrazujeme `inputSchema`, ktorý neskôr použijeme.

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
- Pre každý nástroj zobrazili meno, popis a jeho schému. Túto schému použijeme na volanie nástrojov čoskoro.

#### Java

```java
// Vytvorte poskytovateľa nástrojov, ktorý automaticky objavuje MCP nástroje
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Poskytovateľ MCP nástrojov automaticky spracováva:
// - Zoznam dostupných nástrojov z MCP servera
// - Konverziu schém MCP nástrojov do formátu LangChain4j
// - Správu vykonávania nástrojov a odpovedí
```

V predchádzajúcom kóde sme:

- Vytvorili `McpToolProvider`, ktorý automaticky objavuje a registruje všetky nástroje z MCP servera
- Poskytovateľ nástrojov spracováva konverziu medzi MCP schémami nástrojov a formátom nástrojov LangChain4j interným spôsobom
- Tento prístup abstraktne odstraňuje manuálny proces zisťovania a konverzie nástrojov

#### Rust

Získanie nástrojov z MCP servera sa vykonáva pomocou metódy `list_tools`. Vo svojej funkcii `main`, po nastavení MCP klienta, pridajte nasledovný kód:

```rust
// Získajte zoznam nástrojov MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Konverzia schopností servera na nástroje pre LLM

Ďalším krokom po zobrazení schopností servera je ich konverzia do formátu, ktorému rozumie LLM. Keď to urobíme, môžeme tieto schopnosti poskytnúť ako nástroje nášmu LLM.

#### TypeScript

1. Pridajte nasledujúci kód, ktorý konvertuje odpoveď z MCP servera na formát nástroja, ktorý LLM dokáže použiť:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Vytvorte zod schému na základe vstupnej_schémy
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

    Vyššie uvedený kód vezme odpoveď z MCP servera a konvertuje ju do formátu definície nástroja, ktorému LLM rozumie.

1. Aktualizujme teraz metódu `run`, ktorá bude zobrazovať schopnosti servera:

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

    V predchádzajúcom kóde sme aktualizovali metódu `run`, aby prechádzala výsledkom a pre každý záznam volala `openAiToolAdapter`.

#### Python

1. Najskôr vytvorme nasledujúcu konverznú funkciu

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

1. Potom aktualizujeme náš klientsky kód takto:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Tu pridávame volanie `convert_to_llm_tool`, aby sme konvertovali MCP odpoveď na nástroj do formátu vhodného pre LLM.

#### .NET

1. Pridajme kód, ktorý konvertuje MCP odpoveď na formát vhodný pre LLM:

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

- Vytvorili funkciu `ConvertFrom`, ktorá prijíma meno, popis a vstupnú schému.
- Definovali funkcionalitu, ktorá vytvára `FunctionDefinition`, ktorá sa používa v `ChatCompletionsDefinition`. To je formát, ktorému LLM rozumie.

1. Pozrime sa, ako môžeme aktualizovať existujúci kód, aby využíval túto funkciu:

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
// Vytvoriť rozhranie bota pre interakciu v prirodzenom jazyku
public interface Bot {
    String chat(String prompt);
}

// Nakonfigurovať AI službu s nástrojmi LLM a MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

V predchádzajúcom kóde sme:

- Definovali jednoduché rozhranie `Bot` na interakciu v prirodzenom jazyku
- Použili LangChain4j `AiServices`, ktorý automaticky spája LLM s MCP providerom nástrojov
- Framework automaticky spracováva konverziu schémy nástrojov a volanie funkcií na pozadí
- Tento prístup eliminuje manuálnu konverziu nástrojov – LangChain4j zvládne všetku zložitosť prevodu nástrojov MCP do formátu kompatibilného s LLM

#### Rust

Na konverziu odpovede MCP nástroja do formátu, ktorému rozumie LLM, pridáme pomocnú funkciu, ktorá formátuje zoznam nástrojov. Pridajte nasledujúci kód do súboru `main.rs` pod funkciu `main`. Táto funkcia sa bude volať pri požiadavkách na LLM:

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

Skvelé, teraz sme pripravení spracovávať požiadavky používateľa, pozrime sa na to.

### -4- Spracovanie požiadavky používateľa

V tejto časti kódu budeme spracovávať požiadavky používateľa.

#### TypeScript

1. Pridajte metódu, ktorou budeme volať náš LLM:

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
    - Metóda prijíma odpoveď LLM a zisťuje, ktoré nástroje boli prípadne volané:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // zavolať nástroj
        }
        ```

    - Volá nástroj, ak LLM naznačí, že by sa mal nástroj použiť:

        ```typescript
        // 2. Zavolať nástroj servera
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Niečo urobiť s výsledkom
        // TODO
        ```

1. Aktualizujte metódu `run` tak, aby zahŕňala volania LLM a volanie `callTools`:

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
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Prejdite odpoveďou LLM, pre každú možnosť skontrolujte, či obsahuje volania nástrojov
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Skvelé, zobrazme si celý kód:

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
            baseURL: "https://models.inference.ai.azure.com", // V budúcnosti môže byť potrebné zmeniť na túto URL: https://models.github.ai/inference
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
    
          // 3. Niečo urobte s výsledkom
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

1. Pridajme potrebné importy na volanie LLM:

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Pridajme funkciu, ktorá bude volať LLM:

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

    - Poslali naše funkcie, ktoré sme našli na serveri MCP a skonvertovali, do LLM.
    - Potom sme zavolali LLM s týmito funkciami.
    - Následne sme skontrolovali výsledok, aby sme zistili, ktoré funkcie by mali byť zavolané.
    - Nakoniec sme poslali pole funkcií na zavolanie.

1. Posledný krok, aktualizujme hlavný kód:

    ```python
    prompt = "Add 2 to 20"

    # opýtaj sa LLM, aké nástroje používať, ak nejaké
    functions_to_call = call_llm(prompt, functions)

    # zavolať navrhované funkcie
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Bol to posledný krok, v kóde vyššie:

    - Voláme MCP nástroj cez `call_tool` pomocou funkcie, ktorú LLM určil, že by sa mala použiť na základe nášho promptu.
    - Vypisujeme výsledok volania nástroja na MCP server.

#### .NET

1. Ukážeme kód na vykonanie požiadavky na LLM prompt:

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

    V predchádzajúcom kóde sme:

    - Načítali nástroje zo servera MCP, `var tools = await GetMcpTools()`.
    - Definovali používateľský prompt `userMessage`.
    - Vytvorili objekt možností so špecifikovaným modelom a nástrojmi.
    - Vykonali požiadavku voči LLM.

1. Jeden posledný krok, zistíme, či LLM chce volať nejakú funkciu:

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
    - Pre každé volanie nástroja sme extrahovali meno a argumenty a zavolali nástroj na MCP serveri pomocou MCP klienta. Nakoniec sme vypísali výsledky.

Tu je kompletný kód:

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

- Použili jednoduché prírodzené jazykové prompt-y na interakciu s nástrojmi MCP servera
- Rámec LangChain4j automaticky zvládá:
  - Konverziu používateľských promptov na volania nástrojov podľa potreby
  - Volania správnych MCP nástrojov na základe rozhodnutia LLM
  - Riadenie toku konverzácie medzi LLM a MCP serverom
- Metóda `bot.chat()` vracia odpovede v prirodzenom jazyku, ktoré môžu obsahovať výsledky vykonaných MCP nástrojov
- Tento prístup poskytuje plynulú používateľskú skúsenosť, kde používatelia nemusia vedieť o vnútornej implementácii MCP

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

Tu sa odohráva väčšina práce. Zavoláme LLM s počiatočným promptom používateľa, potom spracujeme odpoveď, aby sme zistili, či je potrebné volať nejaké nástroje. Ak áno, zavoláme tieto nástroje a pokračujeme v konverzácii s LLM, až kým nebudú potrebné žiadne ďalšie volania nástrojov a nezískame finálnu odpoveď.

Budeme volať LLM viackrát, preto definujme funkciu, ktorá bude volať LLM. Pridajte nasledujúcu funkciu do súboru `main.rs`:

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

Táto funkcia prijíma LLM klienta, zoznam správ (vrátane používateľského promptu), nástroje z MCP servera a odosiela požiadavku na LLM, pričom vracia odpoveď.
Odpoveď z LLM bude obsahovať pole `choices`. Budeme potrebovať spracovať výsledok, aby sme zistili, či sú prítomné nejaké `tool_calls`. To nám dá vedieť, že LLM požaduje, aby sa konkrétny nástroj zavolal s argumentmi. Pridajte nasledujúci kód na koniec vášho súboru `main.rs`, aby ste definovali funkciu na spracovanie odpovede LLM:

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


Ak sú prítomné `tool_calls`, extrahuje informácie o nástroji, zavolá MCP server s požiadavkou nástroja a pridá výsledky do správ konverzácie. Potom pokračuje v konverzácii s LLM a správy sa aktualizujú s odpoveďou asistenta a výsledkami volania nástroja.

Na extrahovanie informácií o volaní nástroja, ktoré LLM vracia pre MCP volania, pridáme ďalšiu pomocnú funkciu, ktorá extrahuje všetko potrebné na vykonanie volania. Pridajte nasledujúci kód na koniec vášho súboru `main.rs`:

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


So všetkými časťami na svojom mieste teraz môžeme spracovať počiatočný vstup používateľa a zavolať LLM. Aktualizujte svoju funkciu `main`, aby zahŕňala nasledujúci kód:

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


Týmto sa dotazujete LLM s počiatočným vstupom používateľa žiadajúcim o súčet dvoch čísel a odpoveď sa spracuje tak, aby dynamicky zvládla volania nástrojov.

Skvelé, zvládli ste to!

## Zadanie

Vezmite kód zo cvičenia a rozšírte server o ďalšie nástroje. Potom vytvorte klienta s LLM, ako v cvičení, a otestujte ho s rôznymi vstupmi, aby ste sa uistili, že všetky nástroje vášho servera sa volajú dynamicky. Takýto spôsob budovania klienta znamená, že koncový používateľ bude mať skvelý používateľský zážitok, pretože bude môcť používať vstupy namiesto presných príkazov klienta a nebude si všímať, že sa volá MCP server.

## Riešenie

[Riešenie](./solution/README.md)

## Hlavné poznatky

- Pridanie LLM do vášho klienta poskytuje lepší spôsob, ako môžu používatelia komunikovať s MCP servermi.
- Musíte previesť odpoveď MCP servera na formát, ktorému LLM rozumie.

## Príklady

- [Java Kalkulačka](../samples/java/calculator/README.md)
- [.Net Kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](../samples/javascript/README.md)
- [TypeScript Kalkulačka](../samples/typescript/README.md)
- [Python Kalkulačka](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulačka](../../../../03-GettingStarted/samples/rust)

## Dodatočné zdroje

## Čo ďalej

- Ďalej: [Spotreba servera pomocou Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Negarantujeme žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->