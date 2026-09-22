# Ügyfél létrehozása LLM-mel

> [!NOTE]
> A Java kliens példák a régi HTTP+SSE transzporton keresztül csatlakoznak és
> az MCP `2025-11-25` SDK API-kat célozzák. Új távoli kliensekhez használjon `2026-07-28`-kompatibilis SDK-t és
> Streamable HTTP-t.

Eddig láttuk, hogyan lehet szervert és klienst létrehozni. A kliens képes volt explicit módon hívni a szervert, hogy listázza az eszközeit, erőforrásait és promptjait. Ez azonban nem túl praktikus megközelítés. Felhasználóid az ügynöki korszakban élnek, és azt várják el, hogy promtokkal interakcióba léphessenek egy LLM-mel. Nem érdekli őket, hogy az MCP-t használod-e a képességek tárolására; egyszerűen azt várják, hogy természetes nyelvet használva kommunikálhassanak. Hogyan oldjuk meg ezt? A megoldás egy LLM hozzáadása az ügyfélhez.

## Áttekintés

Ebben a leckében arra fókuszálunk, hogy LLM-et adjunk az ügyfélhez, és megmutatjuk, hogyan biztosít ez jobb élményt a felhasználónak.

## Tanulási célok

A lecke végére képes leszel:

- LLM-mel rendelkező ügyfelet létrehozni.
- Zökkenőmentesen interakcióba lépni az MCP szerverrel LLM segítségével.
- Jobb végfelhasználói élményt nyújtani az ügyfél oldalon.

## Megközelítés

Próbáljuk megérteni a szükséges megközelítést. LLM hozzáadása egyszerűnek hangzik, de valóban így fogunk eljárni?

Így fog az ügyfél interakcióba lépni a szerverrel:

1. Kapcsolat létrehozása a szerverrel.

1. A képességek, promptok, erőforrások és eszközök listázása, valamint séma mentése.

1. LLM hozzáadása és a mentett képességek, azok sémáinak átadása a LLM által értelmezhető formátumban.

1. Felhasználói prompt kezelése úgy, hogy azt az LLM-nek átadjuk a kliens által listázott eszközökkel együtt.

Remek, most, hogy nagy vonalakban értjük, hogyan csinálhatjuk, próbáljuk ki az alábbi gyakorlatban.

## Gyakorlat: Ügyfél létrehozása LLM-mel

Ebben a gyakorlatban megtanuljuk, hogyan adjunk LLM-et az ügyfelünkhöz.

### Hitelesítés GitHub személyes hozzáférési tokennel

GitHub token létrehozása egyszerű folyamat. Íme, hogyan teheted meg:

- Lépj a GitHub Beállításokra – Kattints a profilképedre a jobb felső sarokban, majd válaszd a Beállításokat.
- Navigálj a Fejlesztői Beállításokhoz – Görgess le és válaszd a Fejlesztői Beállításokat.
- Válaszd a Személyes Hozzáférési Tokeneket – Kattints a Finomhangolt tokenekre, majd az Új token generálása gombra.
- Konfiguráld a tokened – Adj meg egy megjegyzést, állíts be lejárati dátumot, és válaszd ki a szükséges engedélyeket. Ebben az esetben mindenképp add hozzá a Models engedélyt.
- Generáld és másold le a tokent – Kattints a Token generálása gombra, és másold le azonnal, mert később nem lesz látható újra.

### -1- Csatlakozás a szerverhez

Először hozzuk létre az ügyfelünket:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Zod importálása séma validáláshoz

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

A fenti kódban:

- Beimportáltuk a szükséges könyvtárakat
- Létrehoztunk egy osztályt két mezővel, `client` és `openai`, melyek segítenek az ügyfél és az LLM kezelésében.
- Beállítottuk az LLM példányunkat, hogy a GitHub Models-t használja az `baseUrl` beállításával, ami az inferencia API-ra mutat.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Szerver paraméterek létrehozása stdio kapcsolathoz
server_params = StdioServerParameters(
    command="mcp",  # Futtatható állomány
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

A fenti kódban:

- Beimportáltuk a MCP-hez szükséges könyvtárakat
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

Először is hozzá kell adnod a LangChain4j függőségeket a `pom.xml` fájlodhoz. Add hozzá ezeket a függőségeket az MCP integráció és az OpenAI-kompatibilis MiniMax API engedélyezéséhez:

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

Állítsd be a MiniMax API kulcsodat és opcionálisan az endpointot és modellt.
A `MINIMAX_MODEL_ID` támogatja a `MiniMax-M3` és `MiniMax-M2.7` modelleket. Ha
nincs beállítva `OPENAI_BASE_URL`, akkor a `MINIMAX_REGION` támogatja a `global_en` és `cn_zh` régiókat.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Régiók szerinti endpoint választáshoz hagyd el az `OPENAI_BASE_URL` beállítást:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Ezután hozd létre a Java kliens osztályt:

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

        // MCP kapcsolat létrehozása a szerverhez
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

A fenti kódban:

- **Hozzáadtuk a LangChain4j függőségeket**: Szükséges az MCP integrációhoz és az OpenAI-kompatibilis MiniMax API-hoz.
- **Importáltuk a LangChain4j könyvtárakat**: MCP integrációhoz és OpenAI chat modell működéshez.
- **Létrehoztunk egy `ChatLanguageModel`-t**: Beállítva MiniMax használatra, a megfelelő API kulccsal, endpointtal és modellazonosítóval.
- **Beállítottuk az HTTP transzportot**: Server-Sent Events (SSE) használatával az MCP szerverhez való kapcsolódáshoz.
- **Létrehoztunk egy MCP klienst**: Ami kezeli a kommunikációt a szerverrel.
- **Használtuk a LangChain4j beépített MCP támogatását**: Ami leegyszerűsíti az LLM és MCP szerver közötti integrációt.

#### Rust

Ez a példa azt feltételezi, hogy rendelkezel egy Rust alapú MCP szerverrel. Ha nincs még, tekintsd meg az [01-first-server](../01-first-server/README.md) leckét a szerver létrehozásához.

Ha megvan a Rust MCP szervered, nyiss meg egy terminált és navigálj ugyanabba a könyvtárba, ahol a szerver található. Ezután futtasd a következő parancsot, hogy új LLM kliens projektet hozz létre:

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
> Nincs hivatalos Rust könyvtár az OpenAI-hoz, azonban az `async-openai` crate egy [közösség által támogatott könyvtár](https://platform.openai.com/docs/libraries/rust#rust), amit gyakran használnak.

Nyisd meg a `src/main.rs` fájlt, és cseréld ki a tartalmát az alábbi kódra:

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
    // Kezdő üzenet
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

    // TEENDŐ: LLM beszélgetés eszközhívásokkal

    Ok(())
}
```

Ez a kód beállít egy alapvető Rust alkalmazást, amely csatlakozik MCP szerverhez és GitHub Models-hez LLM műveletekhez.

> [!IMPORTANT]
> Győződj meg róla, hogy az `OPENAI_API_KEY` környezeti változó be legyen állítva a GitHub tokeneddel, mielőtt futtatod az alkalmazást.

Remek, a következő lépésben listázzuk a képességeket a szerveren.

### -2- A szerver képességeinek listázása

Most csatlakozunk a szerverhez, és lekérjük a képességeit:

#### TypeScript

Ugyanabban az osztályban adjuk hozzá a következő metódusokat:

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

A fenti kódban:

- Hozzáadtuk a szerverhez való csatlakozás kódját, `connectToServer`.
- Létrehoztunk egy `run` metódust, ami kezeli az alkalmazás folyamatát. Eddig csak az eszközök listázását végzi, de hamarosan bővítjük.

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

- Erőforrásokat és eszközöket listázunk és kiíratjuk. Az eszközöknél listázzuk az `inputSchema`-t is, amit később használunk.

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

A fenti kódban:

- Listáztuk az MCP szerveren elérhető eszközöket
- Minden eszközhöz listáztuk a nevét, leírását és sémáját, amit később az eszközök meghívásához használunk.

#### Java

```java
// Hozzon létre egy eszközszolgáltatót, amely automatikusan felfedezi az MCP eszközöket
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Az MCP eszközszolgáltató automatikusan kezeli:
// - Az MCP szerverről elérhető eszközök listázását
// - Az MCP eszközsémák átalakítását LangChain4j formátumra
// - Az eszköz végrehajtásának és válaszainak kezelését
```

A fenti kódban:

- Létrehoztunk egy `McpToolProvider`-t, amely automatikusan felfedezi és regisztrálja az összes eszközt az MCP szerverről
- Az eszköz szolgáltató kezeli az átalakítást MCP eszköz séma és LangChain4j eszköz formátum között belsőleg
- Ez a megközelítés elrejti a manuális eszközlistázás és átalakítás folyamatát

#### Rust

Az eszközök lekérése az MCP szerverről a `list_tools` metódussal történik. A `main` függvényedben, az MCP kliens beállítása után, add hozzá a következő kódot:

```rust
// MCP eszköz lista lekérése
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- A szerver képességek átalakítása LLM-eszközökké

A következő lépés a szerver képességeinek átalakítása olyan formátumba, amit az LLM megért. Miután ezt megtettük, ezek a képességek eszközként rendelkezésünkre állnak az LLM számára.

#### TypeScript

1. Add hozzá a következő kódot, hogy az MCP szerver válaszát olyan eszköz formátumba konvertáld, amit az LLM tud használni:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Hozzon létre egy zod sémát az input_schema alapján
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Kifejezetten állítsa be a típust "function"-re
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

    A fenti kód egy MCP szerver válaszát alakítja át olyan eszköz definíciós formátumba, amit az LLM ért.

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

    A fenti kódban frissítettük a `run` metódust, hogy végigmenjen az eredményen és minden elemre meghívja az `openAiToolAdapter`-t.

#### Python

1. Először hozzuk létre a következő konverter függvényt

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

    A `convert_to_llm_tools` függvényben az MCP eszköz válaszát olyan formátummá alakítjuk át, amit az LLM megért.

2. Ezután frissítsük a kliens kódot, hogy használja ezt a függvényt így:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Itt meghívjuk a `convert_to_llm_tool`-t, ami az MCP eszköz választ átalakítja LLM számára értelmezhető formátumba.

#### .NET

1. Adjunk hozzá kódot, ami az MCP eszköz választ LLM által érthető formátumba alakítja

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

A fenti kódban:

- Létrehoztunk egy `ConvertFrom` függvényt, ami nevet, leírást és input sémát kap.
- Meghatároztunk egy funkciót, ami létrehoz egy FunctionDefinition-t, amit átadunk egy ChatCompletionsDefinition-nek. Ez az utóbbi az LLM számára érthető.

2. Nézzük meg, hogyan frissítsünk meglévő kódot, hogy használja ezt a függvényt:

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
// Hozzon létre egy Bot interfészt természetes nyelvű interakcióhoz
public interface Bot {
    String chat(String prompt);
}

// Konfigurálja az AI szolgáltatást LLM és MCP eszközökkel
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

A fenti kódban:

- Meghatároztunk egy egyszerű `Bot` interfészt természetes nyelvi interakciókhoz
- Használtuk a LangChain4j `AiServices`-ét, hogy automatikusan összekapcsolja az LLM-et az MCP eszköz szolgáltatóval
- A keretrendszer automatikusan kezeli az eszköz séma konverzióját és a függvényhívásokat a háttérben
- Ez a megközelítés megszünteti a manuális eszköz konverziót – a LangChain4j kezeli az MCP eszközök LLM-kompatibilis formátumba konvertálásának összetettségét

#### Rust

Az MCP eszköz válaszának olyan formátumba alakításához, amit az LLM érthető, hozzáadunk egy segédfunkciót, ami formázza az eszközlista tartalmát. Add hozzá a következő kódot a `main.rs` fájlodba a `main` függvény alatt. Ezt hívjuk meg, amikor az LLM-hez kérés érkezik:

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

Remek, most előkészítettük a felhasználói kérések kezelését, nézzük meg ezt a következő lépésben.

### -4- Felhasználói prompt kérés kezelése

Ebben a kódrészben kezeljük a felhasználói kéréseket.

#### TypeScript

1. Adj hozzá egy metódust, amit az LLM meghívásához használunk:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Hívja meg a szerver eszközét
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tegyen valamit az eredménnyel
        // TODO

        }
    }
    ```

    A fenti kódban:

    - Hozzáadtunk egy `callTools` metódust.
    - A metódus megvizsgálja az LLM választ, hogy mely eszközöket hívta meg, ha vannak:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // eszköz hívása
        }
        ```

    - Meghív egy eszközt, ha az LLM jelezte, hogy meghívandó:

        ```typescript
        // 2. Hívja meg a szerver eszközét
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Tegyen valamit az eredménnyel
        // TEENDŐ
        ```

2. Frissítsd a `run` metódust, hogy tartalmazza az LLM meghívását és a `callTools` hívást:

    ```typescript

    // 1. Üzenetek létrehozása, amelyek bemenetei az LLM-nek
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Az LLM meghívása
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Átvizsgálni az LLM választ, minden választásnál ellenőrizni, hogy vannak-e eszközhívások
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Remek, listázzuk most a teljes kódot:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importáld a zod-ot sémaellenőrzéshez

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
          // Hozz létre egy zod sémát a bemenet_séma alapján
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
    
          // 3. Csinálj valamit az eredménnyel
          // TEENDŐ
    
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
    
        // 3. Nézd át az LLM választ, minden választásnál ellenőrizd, hogy van-e eszköz hívás
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

1. Adjunk hozzá néhány importot, ami az LLM híváshoz kell

    ```python
    # nyelvi modell
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Ezután adjuk hozzá az LLM-et hívó függvényt:

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

    A fenti kódban:

    - Átadtuk az MCP szerverről kapott és átalakított függvényeinket az LLM-nek.
    - Meghívtuk az LLM-et a megadott függvényekkel.
    - Megvizsgáltuk az eredményt, hogy mely függvényeket kell meghívni, ha vannak.
    - Végül tömbként átadtuk a hívandó függvényeket.

3. Végül frissítsük a fő kódot:

    ```python
    prompt = "Add 2 to 20"

    # kérdezd meg az LLM-et, hogy milyen eszközöket használjon, ha van ilyen
    functions_to_call = call_llm(prompt, functions)

    # hívd meg a javasolt függvényeket
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ez volt az utolsó lépés, a fenti kódban:

    - Meghívunk egy MCP eszközt a `call_tool`-lal, egy olyan függvényt, amit az LLM javasolt a prompt alapján.
    - Kiírjuk az eszközhívás eredményét az MCP szerverről.

#### .NET

1. Mutassunk kódot LLM prompt kérésre:

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

    A fentiekben:

    - Lekértük az eszközöket az MCP szerverről, `var tools = await GetMcpTools()`.
    - Meghatároztunk egy felhasználói promptot, `userMessage`.
    - Létrehoztunk egy opciós objektumot modell és eszközök specifikálásával.
    - Küldtünk egy kérést az LLM-nek.

2. Végül nézzük meg, ha az LLM szerint függvényt kell hívni:

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

    A fenti kódban:

    - Végigiteráltunk a függvényhívások listáján.
    - Minden eszköz hívásnál kiemeltük a nevet és argumentumokat, majd meghívtuk az MCP eszközt az MCP ügyfél segítségével. Végül kiírtuk az eredményeket.

Íme a teljes kód:

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
    // Végezzen el természetes nyelvű kéréseket, amelyek automatikusan használják az MCP eszközöket
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

A fenti kódban:

- Egyszerű természetes nyelvi promptokat használtunk az MCP szerver eszközeinek hívásához
- LangChain4j keretrendszer automatikusan kezeli:
  - A felhasználói promptok eszköz hívásokká alakítását, ha szükséges
  - A megfelelő MCP eszközök meghívását az LLM döntése alapján
  - Az LLM és az MCP szerver közötti beszélgetési folyamat kezelését
- A `bot.chat()` metódus természetes nyelvi választ ad vissza, amely tartalmazhat eredményeket az MCP eszközök végrehajtásából
- Ez a megközelítés zökkenőmentes felhasználói élményt biztosít, ahol a felhasználóknak nem kell tudniuk az MCP mögöttes megvalósításáról

Teljes kódpélda:

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


Itt történik a munka nagy része. Az LLM-et a kezdeti felhasználói kéréssel hívjuk meg, majd feldolgozzuk a választ, hogy megnézzük, szükség van-e eszközök meghívására. Ha igen, meghívjuk ezeket az eszközöket, és folytatjuk a beszélgetést az LLM-mel, amíg több eszközhívásra nincs szükség, és meg nem kapjuk a végleges választ.

Többször fogjuk hívni az LLM-et, ezért definiáljunk egy függvényt, amely kezeli az LLM hívást. Add hozzá a következő függvényt a `main.rs` fájlodhoz:

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

Ez a függvény megkapja az LLM klienset, az üzenetek listáját (beleértve a felhasználói promptot), az MCP szerver eszközeit, és elküldi a kérést az LLM-nek, majd visszatér a válasszal.

Az LLM válasza egy `choices` tömböt tartalmaz majd. Feldolgoznunk kell az eredményt, hogy lássuk, vannak-e `tool_calls`-ok. Ez jelzi, hogy az LLM egy adott eszköz meghívását kéri argumentumokkal. Add a következő kódot a `main.rs` fájlod aljához egy függvény definiálásához, amely kezeli az LLM választ:

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

    // Tartalom kiírása rendelkezésre áll esetén
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

        // Beszélgetés folytatása az eszköz eredményeivel
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

Ha vannak `tool_calls`-ok, akkor kinyeri az eszköz adatokat, meghívja az MCP szervert az eszköz kérésével, majd hozzáadja az eredményeket a beszélgetés üzeneteihez. Ezután folytatja a beszélgetést az LLM-mel, és az üzenetek frissülnek az asszisztens válaszával és az eszköz hívás eredményeivel.

Ahhoz, hogy kinyerjük az eszköz hívási információkat, amelyeket az LLM ad vissza az MCP hívásokhoz, egy további segédfüggvényt adunk hozzá, amely mindent kinyer, ami a híváshoz kell. Add hozzá a következő kódot a `main.rs` fájlod aljához:

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

Minden részlet rendelkezésre áll, most kezelni tudjuk a kezdeti felhasználói promptot és meghívhatjuk az LLM-et. Frissítsd a `main` függvényed a következő kóddal:

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

Ez lekérdezi az LLM-et a kezdeti felhasználói prompttal, amely a két szám összegét kéri, és feldolgozza a választ, hogy dinamikusan kezelje az eszköz hívásokat.

Remek, sikerült!

## Feladat

Vedd át a példakódból és építsd ki a szervert több eszközzel. Ezután hozz létre egy klienst LLM-mel, mint a példában, és teszteld különböző promptokkal, hogy minden szerver eszközöd dinamikusan meghívódjon. Ez az ügyfélépítési mód azt jelenti, hogy a végfelhasználó remek élményt kap, mert promptokat használhat a pontos kliensparancsok helyett, és nem is tudja, hogy az MCP szerver hívódik meg.

## Megoldás

[Megoldás](./solution/README.md)

## Fontos tanulságok

- Egy LLM hozzáadása az ügyfélhez jobb interakciós módot nyújt a MCP szerverekkel.
- Az MCP szerver válaszát át kell alakítani valamilyen formátummá, amit az LLM megért.

## Minták

- [Java Kalkulátor](../samples/java/calculator/README.md)
- [.Net Kalkulátor](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulátor](../samples/javascript/README.md)
- [TypeScript Kalkulátor](../samples/typescript/README.md)
- [Python Kalkulátor](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulátor](../../../../03-GettingStarted/samples/rust)

## További források

## Mi következik

- Következő: [Szerver használata Visual Studio Code-dal](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->