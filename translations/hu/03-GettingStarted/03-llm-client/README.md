# Ügyfél létrehozása LLM-mel

Eddig láthattad, hogyan kell szervert és ügyfelet létrehozni. Az ügyfél explicit módon tudta hívni a szervert, hogy listázza az eszközeit, erőforrásait és promptjait. Ez azonban nem túl praktikus megközelítés. A felhasználóid az ügynöki korszakban élnek, és elvárják, hogy promptokat használjanak és egy LLM-mel kommunikáljanak helyette. Őket nem érdekli, hogy MCP-t használsz-e képességeid tárolására; egyszerűen elvárják, hogy természetes nyelven kommunikálhassanak. Hogyan oldjuk meg ezt? A megoldás, hogy egy LLM-et adunk hozzá az ügyfélhez.

## Áttekintés

Ebben a leckében arra koncentrálunk, hogyan adhatunk hozzá LLM-et az ügyfélhez, és megmutatjuk, hogyan nyújt ez sokkal jobb élményt a felhasználó számára.

## Tanulási célok

A lecke végére képes leszel:

- Létrehozni egy ügyfelet LLM-mel.
- Zökkenőmentesen kommunikálni egy MCP szerverrel LLM segítségével.
- Jobb végfelhasználói élményt nyújtani az ügyfél oldalon.

## Megközelítés

Próbáljuk megérteni a szükséges megközelítést. LLM hozzáadása egyszerűnek tűnik, de tényleg meg is fogjuk ezt tenni?

Így fog az ügyfél kommunikálni a szerverrel:

1. Kapcsolat létrehozása a szerverrel.

1. A képességek, promptok, erőforrások és eszközök listázása, majd azok sémájának mentése.

1. Egy LLM hozzáadása, és a mentett képességek és sémák átadása olyan formátumban, amit az LLM ért.

1. Felhasználói prompt kezelése az LLM felé továbbítva, az ügyfél által listázott eszközökkel együtt.

Remek, most hogy nagy vonalakban értjük, hogyan csináljuk, próbáljuk ki a következő gyakorlatban.

## Gyakorlat: Ügyfél létrehozása LLM-mel

Ebben a gyakorlatban megtanuljuk, hogyan adjunk hozzá LLM-et az ügyfelünkhöz.

### Hitelesítés GitHub személyes hozzáférési tokennel

GitHub token létrehozása egyszerű folyamat. Így teheted meg:

- Menj a GitHub Beállításokhoz – Kattints a profilképeden a jobb felső sarokban, majd válaszd a Beállításokat.
- Navigálj a Fejlesztői Beállításokhoz – Görgess le és kattints a Fejlesztői Beállításokra.
- Válaszd a Személyes Hozzáférési Tokeneket – Kattints a Finomhangolt tokenekre, majd az Új token generálására.
- Konfiguráld a tokened – Adj meg egy megjegyzést, állíts be lejárati időt, és válaszd ki a szükséges jogosultságokat (scope-okat). Ebben az esetben mindenképp add hozzá a Models jogosultságot.
- Generáld és másold ki a tokent – Kattints a Token generálása gombra, és azonnal másold ki, mert később már nem fogod látni.

### -1- Csatlakozás a szerverhez

Létrehozzuk először az ügyfelünket:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Zod importálása sémavizsgálathoz

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

Az előző kódban:

- Importáltuk a szükséges könyvtárakat
- Létrehoztunk egy osztályt két taggal, `client` és `openai`, amelyek segítenek az ügyfél és az LLM kezelésében.
- Beállítottuk az LLM példányunkat, hogy GitHub modelleket használjon az `baseUrl`-t az inference API-ra állítva.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Szerver paraméterek létrehozása stdio kapcsolathoz
server_params = StdioServerParameters(
    command="mcp",  # Futtatható
    args=["run", "server.py"],  # Opcionális parancssori argumentumok
    env=None,  # Opcionális környezeti változók
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Kapcsolat inicializálása
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Az előző kódban:

- Importáltuk az MCP-hez szükséges könyvtárakat
- Létrehoztunk egy ügyfelet

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

Először is hozzá kell adnod a LangChain4j függőségeket a `pom.xml` fájlodhoz. Ez lehetővé teszi az MCP integrációt és az OpenAI-kompatibilis MiniMax API használatát:

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

Állítsd be a MiniMax API kulcsodat, opcionálisan az endpointot és modellt.
A `MINIMAX_MODEL_ID` támogatja a `MiniMax-M3` és `MiniMax-M2.7` modelleket. Ha
nincs beállítva az `OPENAI_BASE_URL`, a `MINIMAX_REGION` támogatja a `global_en` és `cn_zh` régiókat.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

A régió alapú endpoint választáshoz hagyd el az `OPENAI_BASE_URL`-t:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Ezután hozd létre a Java kliens osztályodat:

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

        // MCP kapcsolat létrehozása a szerverhez való csatlakozáshoz
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP kliens létrehozása
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

Az előző kódban:

- **Hozzáadtuk a LangChain4j függőségeket**: amelyek szükségesek az MCP integrációhoz és az OpenAI-kompatibilis MiniMax API-hoz
- **Importáltuk a LangChain4j könyvtárakat**: az MCP integrációhoz és az OpenAI chat modell funkciókhoz
- **Létrehoztunk egy `ChatLanguageModel`-t**: konfigurálva MiniMax használatára a MiniMax API kulccsal, végponttal és támogatott modellel
- **Beállítottuk az HTTP szállítást**: Server-Sent Events (SSE) használata az MCP szerverhez való kapcsolódáshoz
- **Létrehoztunk egy MCP ügyfelet**: amely kezeli a kommunikációt a szerverrel
- **Felhasználtuk a LangChain4j beépített MCP támogatását**: amely egyszerűsíti az LLM-ek és MCP szerverek közti integrációt

#### Rust

Ez a példa feltételezi, hogy egy Rust-alapú MCP szerver fut. Ha nincs még, nézd meg az [01-first-server](../01-first-server/README.md) leckét a szerver létrehozásához.

Ha megvan a Rust MCP szervered, nyiss egy terminált, és navigálj ugyanabba a mappába, ahol a szerver van. Futattd a következő parancsot új LLM kliens projekt létrehozásához:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Add hozzá a következő függőségeket a `Cargo.toml` fájlodhoz:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Nincs hivatalos Rust könyvtár az OpenAI-hoz, de az `async-openai` crate egy [közösség által karbantartott könyvtár](https://platform.openai.com/docs/libraries/rust#rust), amelyet gyakran használnak.

Nyisd meg a `src/main.rs` fájlt és cseréld ki a tartalmát a következő kódra:

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
    // Kezdeti üzenet
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI kliens beállítása
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP kliens beállítása
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

    // TEENDŐ: MCP eszközlista lekérése

    // TEENDŐ: LLM párbeszéd eszközhívásokkal

    Ok(())
}
```

Ez a kód beállít egy alap Rust alkalmazást, amely csatlakozik egy MCP szerverhez és GitHub modellekhez az LLM interakciókhoz.

> [!IMPORTANT]
> Figyelj arra, hogy az alkalmazás futtatása előtt állítsd be az `OPENAI_API_KEY` környezeti változót a GitHub tokeneddel.

Remek, a következő lépésben listázzuk a szerver képességeit.

### -2- A szerver képességeinek listázása

Most csatlakozunk a szerverhez, és lekérjük a képességeit:

#### Typescript

Ugyanabban az osztályban add hozzá a következő metódusokat:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // eszközök listázása
    const toolsResult = await this.client.listTools();
}
```

Az előző kódban:

- Hozzáadtuk a szerverhez kapcsolódás kódját, `connectToServer` metódust.
- Létrehoztunk egy `run` metódust, amely kezeli az alkalmazás folyamatát. Eddig csak az eszközöket listázza, de hamarosan többet is hozzáadunk.

#### Python

```python
# Elérhető erőforrások listázása
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Elérhető eszközök listázása
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Amit hozzáadtunk:

- Listáztuk az erőforrásokat és eszközöket, és kiírtuk azokat. Az eszközöknél az `inputSchema`-t is listázzuk, amit később használunk.

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

Az előző kódban:

- Listáztuk az MCP szerveren elérhető eszközöket
- Minden eszköznél listáztuk a nevet, leírást és a sémát, amit később használunk eszköz-híváshoz.

#### Java

```java
// Hozzon létre egy eszközszolgáltatót, amely automatikusan felfedezi az MCP eszközöket
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Az MCP eszközszolgáltató automatikusan kezeli:
// - Az MCP szerverről elérhető eszközök listázását
// - Az MCP eszközsémák LangChain4j formátumba történő átalakítását
// - Az eszközvégrehajtás és válaszok kezelését
```

Az előző kódban:

- Létrehoztunk egy `McpToolProvider`-t, ami automatikusan felfedezi és regisztrálja az összes eszközt az MCP szerverről
- Az eszköz szolgáltató kezeli az MCP eszköz sémák és LangChain4j eszköz formátum közti átalakítást
- Ez a megközelítés eltakarja a manuális eszköz listázás és átalakítás folyamatát

#### Rust

Az eszközök lekérése az MCP szerverről az intézet `list_tools` metódussal történik. A `main` függvényben, az MCP kliens beállítása után, add hozzá a következő kódot:

```rust
// MCP eszközlista lekérése
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- A szerver képességeinek átalakítása LLM eszközökké

A szerver képességeinek listázása után a következő lépés az átalakítás olyan formátumba, amit az LLM ért. Miután megvan, ezeket az eszközöket biztosíthatjuk az LLM-ünk számára.

#### TypeScript

1. Add hozzá a következő kódot, hogy átalakítsd az MCP szerver válaszát eszköz formátummá az LLM számára:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Hozz létre egy zod sémát az input_schema alapján
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Állítsd be kifejezetten a típust "function"-re
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

    A fenti kód átalakítja az MCP szerver válaszát egy LLM által értelmezhető eszköz definícióvá.

2. Frissítsük a `run` metódust, hogy listázza a szerver képességeit:

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

    Az előző kódban a `run` metódus végigmegy az eredményen és minden elemre meghívja az `openAiToolAdapter`-t.

#### Python

1. Először hozzuk létre a következő konverter funkciót

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

    A fenti `convert_to_llm_tools` függvény átalakítja az MCP eszköz választ LLM számára érthető formára.

2. Ezután frissítsük a kódot, hogy ehhez a függvényhez forduljon:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Itt meghívjuk a `convert_to_llm_tool` függvényt, hogy az MCP eszköz választ olyan formára alakítsuk, amit az LLM később tud használni.

#### .NET

1. Adjunk kódot az MCP eszköz válaszának konvertálására LLM által érthető formára:

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

Az előző kódban:

- Létrehoztunk egy `ConvertFrom` függvényt, ami nevet, leírást és bemeneti sémát vesz át.
- Definiáltunk egy funkciót, amely egy `FunctionDefinition`-t hoz létre, amely átadásra kerül egy `ChatCompletionsDefinition`-nek. Ez az utóbbi az, amit az LLM ért.

2. Nézzük meg, hogyan frissíthetjük az eddigi kódot, hogy kihasználjuk ezt a függvényt:

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
// Hozzon létre egy Bot interfészt a természetes nyelvi interakcióhoz
public interface Bot {
    String chat(String prompt);
}

// Állítsa be az AI szolgáltatást LLM és MCP eszközökkel
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Az előző kódban:

- Egyszerű `Bot` interfészt definiáltunk természetes nyelvű interakciókhoz
- Használtuk a LangChain4j `AiServices`-t, hogy automatikusan összekösse az LLM-et az MCP eszköz szolgáltatóval
- A keretrendszer automatikusan kezeli az eszköz séma átalakítást és a függvényhívásokat a háttérben
- Ez a megközelítés megszünteti a manuális eszköz-átalakítást - a LangChain4j kezeli az MCP eszközök LLM-kompatibilis formátumba konvertálását

#### Rust

Az MCP eszköz válasz LLM által értett formába konvertálásához hozzáadunk egy segédfunkciót, ami formázza az eszközök listáját. Add a következő kódot a `main.rs` fájlodba, a `main` függvény alá. Ezt fogja hívni az LLM-hez történő kéréseknél:

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

Remek, most beállítottuk a felhasználói kérések kezelését, foglalkozzunk ezzel a következő lépésben.

### -4- Felhasználói prompt kezelés

Ebben a részen kezeljük a felhasználói kéréseket.

#### TypeScript

1. Adj hozzá egy metódust, amit az LLM hívására fogunk használni:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Hívd meg a szerver eszközét
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tegyél valamit az eredménnyel
        // TEENDŐ

        }
    }
    ```

    Az előző kódban:

    - Hozzáadtunk egy `callTools` nevű metódust.
    - A metódus vesz egy LLM választ, és megnézi, hogy mely eszközöket hívta meg, ha egyáltalán:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // eszköz hívása
        }
        ```

    - Meghív egy eszközt, ha az LLM jelezte, hogy hívni kell:

        ```typescript
        // 2. Hívja meg a szerver eszközét
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tegyen valamit az eredménnyel
        // TODO
        ```

2. Frissítsd a `run` metódust, hogy tartalmazza az LLM meghívását és a `callTools` hívását:

    ```typescript

    // 1. Üzenetek létrehozása, amelyek a LLM bemenetei
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. A LLM meghívása
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Végigmenni a LLM válaszán, minden választás esetén ellenőrizni, hogy vannak-e eszközhívások
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Remek, nézzük meg a teljes kódot:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importáld a zod-ot séma érvényesítéshez

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // Lehet, hogy a jövőben ezt az URL-t kell használni: https://models.github.ai/inference
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
          // Hozz létre egy zod sémát az input_schema alapján
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Kifejezetten állítsd be a típust "function"-re
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
    
    
          // 2. Hívjuk meg a szerver eszközét
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Tegyél valamit az eredménnyel
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
    
        // 3. Nézd át az LLM választ, minden opció esetén ellenőrizd, hogy tartalmaz-e eszközhívásokat
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

1. Adj hozzá importokat az LLM híváshoz szükséges modulokhoz

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Ezután add hozzá az LLM hívásához szükséges függvényt:

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
            # Opcionális paraméterek
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

Az előző kódban:

- Átadtuk az általunk az MCP szerveren talált, és konvertált függvényeket az LLM-nek.
- Ezután meghívtuk az LLM-et a megadott függvényekkel.
- Majd megnéztük az eredményt, hogy mely függvényeket kell meghívnunk, ha vannak.
- Végül átadtunk egy tömböt a meghívandó függvényekről.

3. Utolsó lépésként frissítsük a fő kódunkat:

    ```python
    prompt = "Add 2 to 20"

    # kérdezd meg az LLM-et, milyen eszközöket használjon, ha egyáltalán
    functions_to_call = call_llm(prompt, functions)

    # hívd meg a javasolt függvényeket
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

Ez volt az utolsó lépés, az előző kódban:

- Meghív egy MCP eszközt a `call_tool` függvénnyel, amit az LLM szerint kellett meghívni a prompt alapján.
- Kiírja az eredményt, amit az MCP szervertől kapott.

#### .NET

1. Mutatunk némi kódot egy LLM prompt kérésre:

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

Az előző kódban:

- Lekértük az eszközöket az MCP szerverről, `var tools = await GetMcpTools()`.
- Definiáltuk a felhasználói promptot `userMessage`.
- Létrehoztunk egy opciós objektumot a modell és eszközök megadására.
- Kérést küldtünk az LLM-nek.

2. Egy utolsó lépés, nézzük, ha az LLM szerint hívni kellene egy függvényt:

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

Az előző kódban:

- Végigiteráltunk a függvényhívások listáján.
- Minden eszköz-hívásnál kinyertük a nevet és argumentumokat, majd meghívtuk az eszközt az MCP szerveren az MCP kliens segítségével. Végül kiírtuk az eredményt.

Íme a kód teljes egészében:

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
    // Természetes nyelvű kérések végrehajtása, amelyek automatikusan használják az MCP eszközöket
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

Az előző kódban:

- Egyszerű természetes nyelvű promptokat használtunk az MCP szerver eszközeivel való interakcióhoz
- A LangChain4j keretrendszer automatikusan kezeli:
  - A felhasználói promptok eszköz hívásokká történő konvertálását szükség esetén
  - A megfelelő MCP eszközök hívását az LLM döntése alapján
  - A beszélgetés menetének kezelését az LLM és az MCP szerver közt
- A `bot.chat()` metódus visszaad természetes nyelvű válaszokat, amelyek tartalmazhatnak eredményeket az MCP eszköz végrehajtásokból
- Ez a megközelítés zökkenőmentes felhasználói élményt biztosít, ahol a felhasználóknak nem kell tudniuk az alattuk lévő MCP megvalósításról

Teljes kód példa:

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

Itt történik a munka java része. Meghívjuk az LLM-et a kezdeti felhasználói prompttal, majd feldolgozzuk a választ, hogy lássuk, szükséges-e eszközöket hívni. Ha igen, akkor meghívjuk azokat az eszközöket, és folytatjuk a beszélgetést az LLM-mel, amíg már nincs több eszköz hívásra szükség és végleges választ kapunk.


Többször is fogunk hívni LLM-et, ezért definiáljunk egy függvényt, ami a LLM hívást kezeli. Add hozzá a következő függvényt a `main.rs` fájlodhoz:

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

Ez a függvény megkapja a LLM klienset, egy üzenetlistát (beleértve a felhasználó promptját), az MCP szerver eszközeit, és elküld egy kérést a LLM-nek, visszaadva a választ.

A LLM válasza egy `choices` tömböt tartalmaz. Feldolgoznunk kell az eredményt, hogy megnézzük, vannak-e `tool_calls`-ok. Ez mutatja, hogy a LLM egy konkrét eszköz meghívását kéri argumentumokkal. Add a következő kódot a `main.rs` fájl aljára, hogy definiálj egy függvényt a LLM válasz kezelésére:

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

    // Tartalom nyomtatása, ha elérhető
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Eszközhívások kezelése
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Asszisztens üzenet hozzáadása

        // Minden eszközhívás végrehajtása
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Eszköz eredmény hozzáadása az üzenetekhez
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // A beszélgetés folytatása az eszköz eredményeivel
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

Ha vannak `tool_calls`-ok, kinyeri az eszköz információt, meghívja az MCP szervert az eszköz kérésével, és hozzáadja az eredményeket a beszélgetés üzeneteihez. Ezután folytatja a beszélgetést a LLM-mel, és az üzenetek frissülnek az asszisztens válaszával és az eszköz hívás eredményeivel.

Annak érdekében, hogy kinyerjük az MCP hívásokhoz szükséges eszközhívás információkat, hozzáadunk egy segédfüggvényt, ami mindent kinyer a híváshoz. Add hozzá a következő kódot a `main.rs` fájl aljára:

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

Most, hogy minden összetevő a helyén van, kezelhetjük a kezdeti felhasználói promptot, és meghívhatjuk a LLM-et. Frissítsd a `main` függvényed a következő kóddal:

```rust
// LLM beszélgetés eszközhívásokkal
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

Ez lekérdezi a LLM-et a kezdeti felhasználói promptra, ami két szám összegét kéri, és feldolgozza a választ az eszközhívások dinamikus kezeléséhez.

Nagyszerű, megcsináltad!

## Feladat

Vedd át a gyakorlat kódját, és építsd ki a szervert még több eszközzel. Ezután hozz létre egy klienst egy LLM-mel, ahogy a gyakorlatban, és teszteld különböző promptokkal, hogy megbizonyosodj róla, az összes szerver eszköz dinamikusan meg legyen hívva. Ez a kliens felépítési mód azt jelenti, hogy a végfelhasználó remek felhasználói élményt kap, mert promptokkal tud dolgozni pontos kliens parancsok helyett, és észrevétlen marad, ha bármilyen MCP szerver hívás történik.

## Megoldás

[Megoldás](./solution/README.md)

## Fő tanulságok

- Egy LLM hozzáadása a klienshez jobb módot biztosít a felhasználók számára az MCP szerverekkel való interakcióra.
- A MCP szerver válaszát át kell alakítani valamilyen formára, amit a LLM ért.

## Minták

- [Java Számológép](../samples/java/calculator/README.md)
- [.Net Számológép](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Számológép](../samples/javascript/README.md)
- [TypeScript Számológép](../samples/typescript/README.md)
- [Python Számológép](../../../../03-GettingStarted/samples/python)
- [Rust Számológép](../../../../03-GettingStarted/samples/rust)

## További források

## Mi következik

- Következő: [Szerver fogyasztása Visual Studio Code használatával](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->