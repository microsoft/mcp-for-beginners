# Ügyfél létrehozása LLM-mel

Eddig láttad, hogyan lehet szervert és ügyfelet létrehozni. Az ügyfél képes volt explicit módon hívni a szervert, hogy listázza az eszközeit, erőforrásait és promptjait. Azonban ez nem túl praktikus megközelítés. A felhasználód az ügynöki korszakban él, és elvárja, hogy promptokat használjon és természetes nyelven kommunikáljon egy LLM-mel. A felhasználód számára nem számít, hogy MCP-t használsz-e a képességek tárolására, de elvárja, hogy természetes nyelven tudjon interakcióba lépni. Hogyan oldjuk meg ezt? A megoldás az, hogy hozzáadunk egy LLM-et az ügyfélhez.

## Áttekintés

Ebben a leckében arra koncentrálunk, hogy hogyan adjunk hozzá egy LLM-et az ügyfélhez, és megmutatjuk, hogyan nyújt ez sokkal jobb élményt a felhasználód számára.

## Tanulási célok

A lecke végére képes leszel:

- LLM-mel rendelkező ügyfelet létrehozni.
- Zökkenőmentesen kommunikálni egy MCP szerverrel LLM segítségével.
- Jobb végfelhasználói élményt nyújtani az ügyfél oldalon.

## Megközelítés

Próbáljuk megérteni, milyen lépéseket kell tennünk. Egy LLM hozzáadása egyszerűnek hangzik, de tényleg meg is fogjuk ezt tenni?

Így fog az ügyfél kommunikálni a szerverrel:

1. Kapcsolat létrehozása a szerverrel.

1. A képességek, promptok, erőforrások és eszközök listázása, majd ezek sémájának elmentése.

1. Egy LLM hozzáadása, és a mentett képességek és sémák átadása olyan formátumban, amit az LLM ért.

1. Egy felhasználói prompt kezelése úgy, hogy azt átadjuk az LLM-nek az ügyfél által listázott eszközökkel együtt.

Remek, most, hogy nagy vonalakban értjük, hogyan csináljuk, próbáljuk ki az alábbi gyakorlatban.

## Gyakorlat: Ügyfél létrehozása LLM-mel

Ebben a gyakorlatban megtanuljuk, hogyan adjunk hozzá egy LLM-et az ügyfelünkhöz.

### Hitelesítés GitHub személyes hozzáférési tokennel

GitHub token létrehozása egyszerű folyamat. Íme, hogyan csinálhatod:

- Menj a GitHub Beállításokhoz – Kattints a profilképedre a jobb felső sarokban, majd válaszd a Beállítások menüpontot.
- Navigálj a Fejlesztői beállításokhoz – Görgess le és kattints a Fejlesztői beállításokra.
- Válaszd a Személyes hozzáférési tokeneket – Kattints a Finomhangolt tokenekre, majd az Új token generálása gombra.
- Konfiguráld a tokened – Adj meg egy megjegyzést, állíts be lejárati dátumot, és válaszd ki a szükséges jogosultságokat. Ebben az esetben mindenképp add hozzá a Models jogosultságot.
- Generáld és másold ki a tokent – Kattints a Token generálása gombra, és azonnal másold ki, mert később már nem fogod látni.

### -1- Kapcsolódás a szerverhez

Először hozzuk létre az ügyfelünket:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Zod importálása séma érvényesítéshez

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

- Importáltuk a szükséges könyvtárakat
- Létrehoztunk egy osztályt két taggal, `client` és `openai`, amelyek segítenek az ügyfél kezelésében és az LLM-mel való interakcióban.
- Beállítottuk az LLM példányunkat, hogy GitHub Modelleket használjon az `baseUrl` beállításával, amely az inference API-ra mutat.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Szerverparaméterek létrehozása stdio kapcsolathoz
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

- Importáltuk az MCP-hez szükséges könyvtárakat
- Létrehoztunk egy ügyfelet

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

Először hozzá kell adnod a LangChain4j függőségeket a `pom.xml` fájlodhoz. Add hozzá ezeket a függőségeket az MCP integráció és a GitHub Modellek támogatásához:

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

Ezután hozd létre a Java ügyfél osztályodat:

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
    
    public static void main(String[] args) throws Exception {        // Állítsa be az LLM-et a GitHub modellek használatára
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Hozzon létre MCP átvitelt a szerverhez való csatlakozáshoz
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Hozzon létre MCP klienst
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

A fenti kódban:

- **Hozzáadtuk a LangChain4j függőségeket**: Szükségesek az MCP integrációhoz, az OpenAI hivatalos klienshez és a GitHub Modellek támogatásához
- **Importáltuk a LangChain4j könyvtárakat**: Az MCP integrációhoz és az OpenAI chat modell funkciókhoz
- **Létrehoztunk egy `ChatLanguageModel`-t**: Beállítva, hogy GitHub Modelleket használjon a GitHub tokeneddel
- **Beállítottuk az HTTP szállítást**: Server-Sent Events (SSE) használatával az MCP szerverhez való kapcsolódáshoz
- **Létrehoztunk egy MCP ügyfelet**: Ami kezeli a kommunikációt a szerverrel
- **Használtuk a LangChain4j beépített MCP támogatását**: Ami leegyszerűsíti az LLM-ek és MCP szerverek közötti integrációt

#### Rust

Ez a példa feltételezi, hogy van egy Rust alapú MCP szervered futtatva. Ha nincs, nézd meg az [01-first-server](../01-first-server/README.md) leckét a szerver létrehozásához.

Miután megvan a Rust MCP szervered, nyiss egy terminált, és navigálj ugyanabba a könyvtárba, ahol a szerver található. Futtasd a következő parancsot egy új LLM ügyfél projekt létrehozásához:

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
> Nincs hivatalos Rust könyvtár az OpenAI-hoz, azonban az `async-openai` crate egy [közösség által karbantartott könyvtár](https://platform.openai.com/docs/libraries/rust#rust), amelyet gyakran használnak.

Nyisd meg a `src/main.rs` fájlt, és cseréld le a tartalmát a következő kódra:

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

    // TODO: MCP eszközlista lekérése

    // TODO: LLM beszélgetés eszközhívásokkal

    Ok(())
}
```

Ez a kód egy alap Rust alkalmazást állít be, amely kapcsolódik egy MCP szerverhez és GitHub Modellekhez az LLM interakciókhoz.

> [!IMPORTANT]
> Győződj meg róla, hogy az `OPENAI_API_KEY` környezeti változó a GitHub tokenedre van állítva, mielőtt futtatod az alkalmazást.

Remek, a következő lépésként listázzuk a szerver képességeit.

### -2- A szerver képességeinek listázása

Most kapcsolódunk a szerverhez, és lekérdezzük a képességeit:

#### TypeScript

Ugyanebben az osztályban add hozzá a következő metódusokat:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // eszközök felsorolása
    const toolsResult = await this.client.listTools();
}
```

A fenti kódban:

- Hozzáadtunk egy kódot a szerverhez való kapcsolódáshoz, `connectToServer`.
- Létrehoztunk egy `run` metódust, amely kezeli az alkalmazásunk folyamatát. Egyelőre csak az eszközöket listázza, de hamarosan bővítjük.

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

- Listázzuk az erőforrásokat és eszközöket, és kiírtuk őket. Az eszközöknél az `inputSchema`-t is listázzuk, amit később használunk.

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
- Minden eszköznél listáztuk a nevét, leírását és a sémáját. Ez utóbbit hamarosan használni fogjuk az eszközök hívásához.

#### Java

```java
// Hozzon létre egy eszközszolgáltatót, amely automatikusan felfedezi az MCP eszközöket
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Az MCP eszközszolgáltató automatikusan kezeli:
// - Az MCP szerverről elérhető eszközök listázását
// - Az MCP eszközsémák LangChain4j formátumba történő átalakítását
// - Az eszközök végrehajtásának és válaszainak kezelését
```

A fenti kódban:

- Létrehoztunk egy `McpToolProvider`-t, amely automatikusan felfedezi és regisztrálja az összes eszközt az MCP szerverről
- Az eszköz szolgáltató belsőleg kezeli az MCP eszköz sémák és a LangChain4j eszköz formátum közötti átalakítást
- Ez a megközelítés elrejti az eszközök manuális listázását és átalakítását

#### Rust

Az MCP szerverről az eszközök lekérése a `list_tools` metódussal történik. A `main` függvényedben, az MCP kliens beállítása után add hozzá a következő kódot:

```rust
// MCP eszközlista lekérése
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- A szerver képességeinek átalakítása LLM eszközökké

A következő lépés a szerver képességeinek olyan formátumba konvertálása, amit az LLM megért. Miután ezt megtesszük, ezeket a képességeket eszközként tudjuk átadni az LLM-nek.

#### TypeScript

1. Add hozzá a következő kódot, amely az MCP szerver válaszát olyan eszköz formátumba alakítja, amit az LLM használni tud:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Hozzon létre egy zod sémát az input_schema alapján
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Állítsa be kifejezetten a típust "function"-re
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

    A fenti kód az MCP szerver válaszát veszi, és olyan eszköz definíciós formátumba alakítja, amit az LLM megért.

1. Frissítsük a `run` metódust, hogy listázza a szerver képességeit:

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

    A fenti kódban frissítettük a `run` metódust, hogy végigmenjen az eredményen, és minden elemre meghívja az `openAiToolAdapter`-t.

#### Python

1. Először hozzuk létre a következő konvertáló függvényt:

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

    A `convert_to_llm_tools` függvényben az MCP eszköz válaszát olyan formátumba alakítjuk, amit az LLM megért.

1. Ezután frissítsük az ügyfél kódját, hogy használja ezt a függvényt:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Itt hozzáadtunk egy hívást a `convert_to_llm_tool`-ra, hogy az MCP eszköz válaszát olyan formátumba alakítsuk, amit később az LLM-nek átadhatunk.

#### .NET

1. Adjunk hozzá kódot, amely az MCP eszköz válaszát olyan formátumba alakítja, amit az LLM megért:

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

- Létrehoztunk egy `ConvertFrom` függvényt, amely nevet, leírást és bemeneti sémát fogad.
- Definiáltunk egy funkciót, amely létrehoz egy `FunctionDefinition`-t, amit egy `ChatCompletionsDefinition`-nek adunk át. Ez utóbbit az LLM megérti.

1. Nézzük meg, hogyan frissíthetjük a meglévő kódot, hogy kihasználja ezt a függvényt:

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

// Állítsa be az AI szolgáltatást LLM és MCP eszközökkel
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

A fenti kódban:

- Egyszerű `Bot` interfészt definiáltunk a természetes nyelvű interakciókhoz
- Használtuk a LangChain4j `AiServices`-ét, hogy automatikusan összekösse az LLM-et az MCP eszköz szolgáltatóval
- A keretrendszer automatikusan kezeli az eszköz séma átalakítást és a funkcióhívásokat a háttérben
- Ez a megközelítés megszünteti a manuális eszköz átalakítást – a LangChain4j kezeli az MCP eszközök LLM-kompatibilis formátumba konvertálásának összetettségét

#### Rust

Az MCP eszköz válaszának olyan formátumba alakításához, amit az LLM megért, hozzáadunk egy segédfüggvényt, amely formázza az eszközök listáját. Add hozzá a következő kódot a `main.rs` fájlodhoz a `main` függvény alatt. Ezt fogjuk hívni, amikor kéréseket küldünk az LLM-nek:

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

Remek, most már készen állunk a felhasználói kérések kezelésére, nézzük ezt meg a következő lépésben.

### -4- Felhasználói prompt kérés kezelése

Ebben a kódrészben a felhasználói kéréseket fogjuk kezelni.

#### TypeScript

1. Adj hozzá egy metódust, amely az LLM hívására szolgál:

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
        // TEENDŐ

        }
    }
    ```

    A fenti kódban:

    - Hozzáadtunk egy `callTools` metódust.
    - A metódus megvizsgálja az LLM válaszát, hogy mely eszközöket hívták meg, ha egyáltalán:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // eszköz hívása
        }
        ```

    - Meghív egy eszközt, ha az LLM jelzi, hogy meg kell hívni:

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

1. Frissítsd a `run` metódust, hogy tartalmazza az LLM hívását és a `callTools` meghívását:

    ```typescript

    // 1. Üzenetek létrehozása, amelyek bemenetként szolgálnak az LLM-nek
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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Átnézni az LLM válaszát, minden választásnál ellenőrizni, hogy tartalmaz-e eszközhívásokat
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
import { z } from "zod"; // Importáld a zod-ot sémavalidációhoz

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
            type: "function" as const, // Állítsd be explicit módon a típust "function"-re
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
    
          // 3. Tegyél valamit az eredménnyel
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Menj végig az LLM válaszon, minden választásnál ellenőrizd, hogy vannak-e eszközhívások
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

1. Adjunk hozzá néhány importot az LLM hívásához:

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Ezután adjuk hozzá a függvényt, amely az LLM-et hívja:

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

    - Átadtuk az LLM-nek az MCP szerveren talált és konvertált függvényeinket.
    - Meghívtuk az LLM-et ezekkel a függvényekkel.
    - Megvizsgáltuk az eredményt, hogy mely függvényeket kell meghívni, ha vannak ilyenek.
    - Végül átadtunk egy függvények tömbjét a híváshoz.

1. Végül frissítsük a fő kódot:

    ```python
    prompt = "Add 2 to 20"

    # kérdezd meg az LLM-et, milyen eszközöket használjon, ha egyáltalán
    functions_to_call = call_llm(prompt, functions)

    # hívd meg a javasolt függvényeket
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ez volt az utolsó lépés, a fenti kódban:

    - Meghívunk egy MCP eszközt a `call_tool` segítségével, egy olyan függvénnyel, amit az LLM javasolt a prompt alapján.
    - Kiírjuk az eszköz hívás eredményét az MCP szerverről.

#### .NET

1. Mutassunk kódot egy LLM prompt kéréshez:

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

    A fenti kódban:

    - Lekértük az eszközöket az MCP szerverről, `var tools = await GetMcpTools()`.
    - Definiáltunk egy felhasználói promptot `userMessage`.
    - Létrehoztunk egy opció objektumot, amely megadja a modellt és az eszközöket.
    - Kérést küldtünk az LLM-nek.

1. Egy utolsó lépés, nézzük meg, hogy az LLM szerint kell-e függvényt hívni:

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

    - Végigmentünk a függvényhívások listáján.
    - Minden eszköz hívásnál kinyertük a nevet és az argumentumokat, majd meghívtuk az eszközt az MCP szerveren az MCP kliens segítségével. Végül kiírtuk az eredményeket.

Íme a teljes kód:

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

A fenti kódban:

- Egyszerű természetes nyelvű promptokat használtunk az MCP szerver eszközeivel való interakcióhoz
- A LangChain4j keretrendszer automatikusan kezeli:
  - A felhasználói promptok eszköz hívásokká alakítását, ha szükséges
  - A megfelelő MCP eszközök meghívását az LLM döntése alapján
  - A beszélgetés folyamatának kezelését az LLM és az MCP szerver között
- A `bot.chat()` metódus természetes nyelvű válaszokat ad vissza, amelyek tartalmazhatnak eredményeket az MCP eszközök végrehajtásából
- Ez a megközelítés zökkenőmentes felhasználói élményt nyújt, ahol a felhasználóknak nem kell ismerniük az MCP mögöttes megvalósítását

Teljes kód példa:

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

Itt történik a munka nagy része. Meghívjuk az LLM-et a kezdeti felhasználói prompttal, majd feldolgozzuk a választ, hogy lássuk, kell-e eszközöket hívni. Ha igen, meghívjuk azokat az eszközöket, és folytatjuk a beszélgetést az LLM-mel, amíg már nincs több eszköz hívás és végleges válaszunk van.

Többször fogunk hívni az LLM-et, ezért definiáljunk egy függvényt, amely kezeli az LLM hívást. Add hozzá a következő függvényt a `main.rs` fájlodhoz:

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

Ez a függvény megkapja az LLM klienst, az üzenetek listáját (beleértve a felhasználói promptot), az MCP szerver eszközeit, és elküld egy kérést az LLM-nek, majd visszaadja a választ.
Az LLM válasza egy `choices` tömböt fog tartalmazni. Feldolgoznunk kell az eredményt, hogy megnézzük, vannak-e `tool_calls` jelen. Ez megmutatja, hogy az LLM egy adott eszköz meghívását kéri-e argumentumokkal. Add hozzá a következő kódot a `main.rs` fájlod aljához, hogy definiálj egy függvényt az LLM válasz kezelésére:

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

            // Eszköz eredményének hozzáadása az üzenetekhez
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

Ha vannak `tool_calls`, akkor kinyeri az eszköz információkat, meghívja az MCP szervert az eszköz kérésével, és hozzáadja az eredményeket a beszélgetés üzeneteihez. Ezután folytatja a beszélgetést az LLM-mel, és az üzenetek frissülnek az asszisztens válaszával és az eszköz hívás eredményeivel.

Az MCP hívásokhoz az LLM által visszaadott eszköz hívás információk kinyeréséhez hozzáadunk egy másik segédfüggvényt, amely mindent kinyer, ami a híváshoz szükséges. Add hozzá a következő kódot a `main.rs` fájlod aljához:

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

Minden darab a helyén van, most már kezelhetjük a kezdeti felhasználói promptot és meghívhatjuk az LLM-et. Frissítsd a `main` függvényedet a következő kóddal:

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

Ez lekérdezi az LLM-et a kezdeti felhasználói prompttal, amely két szám összegét kéri, és feldolgozza a választ, hogy dinamikusan kezelje az eszköz hívásokat.

Nagyszerű, sikerült!

## Feladat

Vedd át a gyakorlatból a kódot, és építsd ki a szervert több eszközzel. Ezután hozz létre egy klienst egy LLM-mel, mint a gyakorlatban, és teszteld különböző promptokkal, hogy megbizonyosodj arról, hogy az összes szerver eszközöd dinamikusan meghívásra kerül. Ez a kliens építési mód azt jelenti, hogy a végfelhasználó nagyszerű felhasználói élményt kap, mivel promptokat használhat pontos kliens parancsok helyett, és nem kell tudnia arról, hogy bármilyen MCP szerver hívás történik.

## Megoldás

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## Főbb tanulságok

- Egy LLM hozzáadása a kliensedhez jobb módot biztosít a felhasználók számára az MCP szerverekkel való interakcióra.
- Az MCP szerver válaszát át kell alakítani valami olyanná, amit az LLM meg tud érteni.

## Minták

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## További források

## Mi következik

- Következő: [Szerver használata Visual Studio Code-dal](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->