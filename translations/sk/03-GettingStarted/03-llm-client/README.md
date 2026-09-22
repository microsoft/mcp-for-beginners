# Vytvorenie klienta s LLM

> [!NOTE]
> Príklady Java klienta sa pripájajú prostredníctvom starého HTTP+SSE transportu a
> cielia na MCP SDK API `2025-11-25`. Pre nových vzdialených klientov použite
> kompatibilnú verziu SDK `2026-07-28` a streamovateľné HTTP.

Doteraz ste videli, ako vytvoriť server a klienta. Klient bol schopný explicitne volať server, aby získal zoznam jeho nástrojov, zdrojov a promptov. Avšak toto nie je veľmi praktický prístup. Vaši používatelia žijú v agentickej ére a očakávajú používanie promptov a komunikáciu s LLM. Nezaujíma ich, či používate MCP na ukladanie vašich schopností, jednoducho očakávajú interakciu pomocou prirodzeného jazyka. Ako to teda vyriešime? Riešením je pridať LLM do klienta.

## Prehľad

V tejto lekcii sa zameriame na pridanie LLM ku klientovi a ukážeme, ako to poskytuje oveľa lepší zážitok pre používateľa.

## Ciele učenia

Na konci tejto lekcie budete:

- Vytvoriť klienta s LLM.
- Bezproblémovo komunikovať so serverom MCP pomocou LLM.
- Poskytnúť lepší používateľský zážitok na strane klienta.

## Prístup

Pokúsme sa pochopiť prístup, ktorý potrebujeme zvoliť. Pridanie LLM znie jednoducho, ale naozaj to urobíme?

Tu je, ako klient bude komunikovať so serverom:

1. Nadviazať spojenie so serverom.

1. Zoznam schopností, promptov, zdrojov a nástrojov a uložiť ich schému.

1. Pridať LLM a odovzdať uložené schopnosti a ich schému v formáte, ktorý LLM rozumie.

1. Spracovať používateľský prompt odovzdaním LLM spolu s nástrojmi zoznamu klienta.

Výborne, teraz keď chápeme, ako to môžeme urobiť na vysokej úrovni, vyskúšajme to v nasledujúcej úlohe.

## Cvičenie: Vytvorenie klienta s LLM

V tomto cvičení sa naučíme pridať LLM ku nášmu klientovi.

### Autentifikácia pomocou GitHub Personal Access Token

Vytvorenie GitHub tokenu je jednoduchý proces. Tu je návod, ako to urobiť:

- Prejdite do GitHub Nastavení – Kliknite na svoj profilový obrázok v pravom hornom rohu a vyberte Nastavenia.
- Prejdite na Vývojárske nastavenia – Posuňte zobrazenie nižšie a kliknite na Vývojárske nastavenia.
- Vyberte Personal Access Tokens – Kliknite na Jemnozrné tokeny a potom Generovať nový token.
- Nakonfigurujte svoj token – Pridajte poznámku na referenciu, nastavte dátum vypršania platnosti a vyberte potrebné rozsahy (oprávnenia). V tomto prípade nezabudnite pridať povolenie Models.
- Vygenerujte a skopírujte token – Kliknite na Generovať token a okamžite ho skopírujte, pretože ho už viac neuvidíte.

### -1- Pripojenie na server

Najskôr vytvorme nášho klienta:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importovať zod pre validáciu schémy

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
- Nakonfigurovali inštanciu LLM na používanie GitHub Models nastavením `baseUrl` tak, aby smeroval na inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Vytvorte parametre servera pre pripojenie stdio
server_params = StdioServerParameters(
    command="mcp",  # Spustiteľný súbor
    args=["run", "server.py"],  # Nepovinné argumenty príkazového riadku
    env=None,  # Nepovinné premenné prostredia
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

Najskôr musíte pridať závislosti LangChain4j do súboru `pom.xml`. Pridajte tieto závislosti, aby ste umožnili integráciu MCP a OpenAI-kompatibilné MiniMax API:

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

Nastavte svoj MiniMax API kľúč a voliteľne aj endpoint a model.
`MINIMAX_MODEL_ID` podporuje `MiniMax-M3` a `MiniMax-M2.7`. Ak
`OPENAI_BASE_URL` nie je nastavený, `MINIMAX_REGION` podporuje `global_en` a `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Ak chcete vybrať endpoint podľa regiónu, vynechajte `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
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

V predchádzajúcom kóde sme:

- **Pridali závislosti LangChain4j**: Potrebné pre integráciu MCP a OpenAI-kompatibilné MiniMax API
- **Importovali knižnice LangChain4j**: Pre integráciu MCP a funkčnosť OpenAI chat modelu
- **Vytvorili `ChatLanguageModel`**: Nakonfigurovaný na použitie MiniMax s vašim MiniMax API kľúčom, endpointom a podporovaným modelom
- **Nastavili HTTP transport**: Pomocou Server-Sent Events (SSE) na pripojenie k MCP serveru
- **Vytvorili MCP klienta**: Ktorý bude obsluhovať komunikáciu so serverom
- **Použili zabudovanú podporu MCP v LangChain4j**: Čím sa zjednodušuje integrácia medzi LLM a MCP servermi

#### Rust

Tento príklad predpokladá, že máte spustený MCP server založený na Rust. Ak ho nemáte, vráťte sa k lekcii [01-first-server](../01-first-server/README.md), kde si server vytvoríte.

Keď máte svoj Rust MCP server, otvorte terminál a prejdite do rovnakého adresára ako server. Potom spustite nasledujúci príkaz na vytvorenie nového LLM klientského projektu:

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
> Neexistuje oficiálna Rust knižnica pre OpenAI, avšak `async-openai` crate je [spoločenstvom udržiavaná knižnica](https://platform.openai.com/docs/libraries/rust#rust), ktorá je bežne používaná.

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

    // Nastavenie klienta OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Nastavenie klienta MCP
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

    // TODO: Získajte zoznam nástrojov MCP

    // TODO: Konverzácia LLM s volaniami nástrojov

    Ok(())
}
```

Tento kód nastavuje základnú Rust aplikáciu, ktorá sa pripojí k MCP serveru a GitHub Models pre interakciu s LLM.

> [!IMPORTANT]
> Pred spustením aplikácie sa uistite, že ste nastavili premennú prostredia `OPENAI_API_KEY` s vaším GitHub tokenom.

Výborne, v ďalšom kroku si zobrazíme schopnosti na serveri.

### -2- Zoznam schopností servera

Teraz sa pripojíme k serveru a vyžiadame jeho schopnosti:

#### Typescript

Do tej istej triedy pridajte nasledujúce metódy:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // nástroje zoznamu
    const toolsResult = await this.client.listTools();
}
```

V predchádzajúcom kóde sme:

- Pridali kód na pripojenie sa k serveru, `connectToServer`.
- Vytvorili metódu `run`, ktorá je zodpovedná za spracovanie nášho aplikačného toku. Zatiaľ iba zobrazuje nástroje, ale čoskoro ju rozšírime.

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

Čo sme pridali:

- Zoznam zdrojov a nástrojov a ich výpis. Pre nástroje sme tiež zobrazili `inputSchema`, ktorý použijeme neskôr.

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

- Vypísali nástroje dostupné na MCP serveri
- Pre každý nástroj vypísali meno, popis a jeho schému. To druhé použijeme na volanie nástrojov o chvíľu.

#### Java

```java
// Vytvorte poskytovateľa nástrojov, ktorý automaticky zisťuje MCP nástroje
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Poskytovateľ MCP nástrojov automaticky spracováva:
// - Zoznam dostupných nástrojov zo servera MCP
// - Konverziu schém MCP nástrojov do formátu LangChain4j
// - Správu vykonávania nástrojov a odpovedí
```

V predchádzajúcom kóde sme:

- Vytvorili `McpToolProvider`, ktorý automaticky zistí a zaregistruje všetky nástroje zo servera MCP
- Poskytovateľ nástrojov interne prekladá medzi schémou nástrojov MCP a LangChain4j formátom nástrojov
- Tento prístup abstrahuje manuálne zisťovanie a prevod nástrojov

#### Rust

Získavanie nástrojov zo servera MCP sa vykonáva metódou `list_tools`. Vo vašej funkcii `main`, po nastavení MCP klienta, pridajte nasledujúci kód:

```rust
// Získať zoznam nástrojov MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Konverzia schopností servera na nástroje LLM

Ďalším krokom po zozname schopností servera je prevod do formátu, ktorému LLM rozumie. Keď to urobíme, môžeme tieto schopnosti poskytnúť ako nástroje nasmu LLM.

#### TypeScript

1. Pridajte nasledujúci kód pre konverziu odpovede z MCP servera do formátu nástroja, ktorý LLM môže používať:

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

    Vyššie uvedený kód zoberie odpoveď z MCP servera a prevedie ju do definície nástroja, ktorej LLM rozumie.

2. Aktualizujme následne metódu `run`, aby sme v nej zobrazili schopnosti servera:

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

    V predchádzajúcom kóde sme aktualizovali metódu `run`, aby prešla cez výsledok a pre každú položku zavolala `openAiToolAdapter`.

#### Python

1. Najprv si vytvorme nasledujúcu prevodnú funkciu

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

    Vo funkcii `convert_to_llm_tools` vyššie berieme MCP nástrojovú odpoveď a konvertujeme ju do formátu, ktorému LLM rozumie.

2. Potom aktualizujme náš klientsky kód, aby túto funkciu využil takto:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Tu pridávame volanie `convert_to_llm_tool` na konverziu MCP nástrojovej odpovede na niečo, čo neskôr poskytneme LLM.

#### .NET

1. Pridajme kód na konverziu MCP nástrojovej odpovede na niečo, čomu LLM rozumie

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
- Definovali funkčnosť, ktorá vytvára `FunctionDefinition`, ktorá je odovzdaná do `ChatCompletionsDefinition`. To druhé LLM rozumie.

2. Pozrime sa, ako môžeme aktualizovať existujúci kód, aby využíval túto funkciu:

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

- Definovali jednoduché rozhranie `Bot` pre interakciu v prirodzenom jazyku
- Použili LangChain4j `AiServices` na automatické prepojenie LLM s MCP poskytovateľom nástrojov
- Framework automaticky spravuje prevod schém nástrojov a volania funkcií na pozadí
- Tento prístup eliminuje manuálnu konverziu nástrojov - LangChain4j rieši všetku zložitosť konverzie MCP nástrojov do kompatibilného formátu LLM

#### Rust

Pre konverziu MCP nástrojovej odpovede do formátu, ktorému LLM rozumie, pridáme pomocnú funkciu, ktorá naformátuje zoznam nástrojov. Pridajte nasledujúci kód do súboru `main.rs` pod funkciu `main`. Tento kód sa zavolá pri požiadavkách smerovaných na LLM:

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

Výborne, sme pripravení spracovávať aj používateľské požiadavky, poďme sa na to pozrieť ďalší krok.

### -4- Spracuj požiadavku používateľa

V tejto časti kódu budeme spracúvať požiadavky používateľov.

#### TypeScript

1. Pridajte metódu, ktorá bude volať náš LLM:

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
    - Metóda prijíma odpoveď LLM a kontroluje, ktoré nástroje boli volané, ak vôbec nejaké:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // využiť nástroj
        }
        ```

    - Volá nástroj, ak LLM indikuje, že by mal byť zavolaný:

        ```typescript
        // 2. Zavolajte nástroj servera
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Niečo urobte s výsledkom
        // TODO
        ```

2. Aktualizujte metódu `run`, aby volala LLM a `callTools`:

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

Výborne, tu je kompletný kód:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importovať zod pre validáciu schémy

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // môže byť potrebné v budúcnosti zmeniť na túto URL: https://models.github.ai/inference
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
          // Vytvoriť zod schému na základe input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Explicitne nastaviť typ na "function"
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
    
    
          // 2. Zavolať nástroj servera
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Niečo urobiť s výsledkom
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
    
        // 3. Prejsť odpoveď LLM, pre každý výber skontrolovať, či obsahuje volania nástrojov
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

1. Pridajme potrebné importy na volanie LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Potom pridajme funkciu, ktorá zavolá LLM:

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
    - Kontrolujeme výsledok, ktoré funkcie by sme mali volať, ak vôbec.
    - Nakoniec odovzdávame pole funkcií na volanie.

3. Posledný krok, aktualizujme náš hlavný kód:

    ```python
    prompt = "Add 2 to 20"

    # opýtaj sa LLM, aké nástroje použiť, ak vôbec nejaké
    functions_to_call = call_llm(prompt, functions)

    # zavolaj navrhované funkcie
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Hotovo, toto bol posledný krok, v kóde vyššie:

    - Voláme MCP nástroj pomocou `call_tool` s funkciou, ktorú LLM určil na základe nášho promptu.
    - Vypisujeme výsledok volania nástroja na MCP server.

#### .NET

1. Ukážme si kód na vykonanie požiadavky na LLM prompt:

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
    - Definovali prompt používateľa `userMessage`.
    - Vytvorili objekt s možnosťami určujúcimi model a nástroje.
    - Vykonali požiadavku na LLM.

2. Jeden posledný krok, zistíme, či si LLM myslí, že by sme mali zavolať funkciu:

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
    - Pre každé volanie nástroja získali meno a argumenty a zavolali nástroj na MCP serveri pomocou MCP klienta. Nakoniec vypíšeme výsledky.

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

// 6. Print the generic response
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

- Použili jednoduché prírodné jazykové promptívy na interakciu s nástrojmi MCP servera
- Framework LangChain4j automaticky spravuje:
  - Prevod používateľských promptov na volania nástrojov podľa potreby
  - Volanie vhodných MCP nástrojov na základe rozhodnutia LLM
  - Riadenie toku konverzácie medzi LLM a MCP serverom
- Metóda `bot.chat()` vracia odpovede v prirodzenom jazyku, ktoré môžu obsahovať výsledky vykonaní MCP nástrojov
- Tento prístup poskytuje plynulý používateľský zážitok, kde používatelia nemusia poznať podkladovú implementáciu MCP

Kompletný príklad kódu:

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


Tu sa odohráva väčšina práce. Zavoláme LLM s počiatočným používateľským promptom, potom spracujeme odpoveď, aby sme zistili, či je potrebné zavolať nejaké nástroje. Ak áno, zavoláme tieto nástroje a budeme pokračovať v konverzácii s LLM, až kým nebude potrebné volať ďalšie nástroje a nebude máme konečnú odpoveď.

Bude potrebné volať LLM viackrát, takže si definujeme funkciu, ktorá bude volanie LLM riešiť. Pridajte nasledujúcu funkciu do vášho súboru `main.rs`:

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

Táto funkcia prijíma LLM klienta, zoznam správ (vrátane používateľského promptu), nástroje zo servera MCP a odošle požiadavku na LLM, pričom vráti odpoveď.

Odpoveď z LLM bude obsahovať pole `choices`. Budeme musieť spracovať výsledok, aby sme zistili, či sú prítomné nejaké `tool_calls`. To nám dáva vedieť, že LLM požaduje zavolať konkrétny nástroj s argumentmi. Pridajte nasledujúci kód na koniec vášho `main.rs` súboru, aby ste definovali funkciu na spracovanie odpovede LLM:

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

    // Vytlačiť obsah, ak je dostupný
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Riešiť volania nástrojov
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

Ak sú prítomné `tool_calls`, extrahuje informácie o nástroji, zavolá MCP server so žiadosťou o nástroj a pridá výsledky do správ konverzácie. Potom pokračuje v konverzácii s LLM a správy sa aktualizujú odpoveďou asistenta a výsledkami volania nástroja.

Na extrahovanie informácií o volaní nástroja, ktoré LLM vracia pre volania MCP, pridáme ďalšiu pomocnú funkciu, ktorá vyberie všetko potrebné na uskutočnenie volania. Pridajte nasledujúci kód na koniec vášho `main.rs` súboru:

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

Keď máme všetky časti na mieste, teraz môžeme spracovať počiatočný používateľský prompt a zavolať LLM. Aktualizujte vašu funkciu `main`, aby obsahovala nasledujúci kód:

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

Toto nastaví dotaz na LLM s počiatočným používateľským promptom žiadajúcim o súčet dvoch čísel a spracuje odpoveď, aby dynamicky riešil volania nástrojov.

Skvelé, podarilo sa vám to!

## Zadanie

Vezmite kód z cvičenia a rozšírte server o ďalšie nástroje. Potom vytvorte klienta s LLM, ako v cvičení, a otestujte ho s rôznymi promptami, aby ste sa uistili, že všetky vaše serverové nástroje sa volajú dynamicky. Tento spôsob budovania klienta znamená, že koncový používateľ bude mať skvelý používateľský zážitok, keďže môže použiť prompt namiesto presných klientských príkazov a nebude si uvedomovať, že sa volá niektorý MCP server.

## Riešenie

[Riešenie](./solution/README.md)

## Hlavné body

- Pridanie LLM do vášho klienta poskytuje lepší spôsob interakcie používateľov so servermi MCP.
- Je potrebné previesť odpoveď servera MCP na niečo, čomu LLM rozumie.

## Príklady

- [Java Kalkulačka](../samples/java/calculator/README.md)
- [.Net Kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](../samples/javascript/README.md)
- [TypeScript Kalkulačka](../samples/typescript/README.md)
- [Python Kalkulačka](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulačka](../../../../03-GettingStarted/samples/rust)

## Ďalšie zdroje

## Čo ďalej

- Ďalej: [Používanie servera vo Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->