# Ügyfél létrehozása LLM-mel

Eddig láttad, hogyan kell szervert és ügyfelet létrehozni. Az ügyfél képes volt explicit módon hívni a szervert, hogy felsorolja az eszközeit, erőforrásait és promptjait. Azonban ez nem túl praktikus megközelítés. A felhasználóid az ügynöki korszakban élnek, és azt várják el, hogy promptokat használjanak, és egy LLM-mel kommunikáljanak. Nem érdekli őket, hogy MCP-t használsz-e a képességeid tárolására; egyszerűen azt várják el, hogy természetes nyelven kommunikáljanak. Hogyan oldjuk ezt meg? A megoldás, hogy hozzáadunk egy LLM-et az ügyfélhez.

## Áttekintés

Ebben a leckében arra koncentrálunk, hogy hogyan adjunk egy LLM-et az ügyfélhez, és megmutatjuk, hogyan nyújt ez sokkal jobb élményt a felhasználód számára.

## Tanulási célok

A lecke végére képes leszel:

- Ügyfelet létrehozni LLM-mel.
- Zökkenőmentesen kommunikálni egy MCP szerverrel LLM segítségével.
- Jobb végfelhasználói élményt biztosítani az ügyfél oldalán.

## Megközelítés

Próbáljuk megérteni a szükséges megközelítést. Egy LLM hozzáadása egyszerűnek tűnik, de vajon tényleg így fogjuk csinálni?

Így fog az ügyfél kommunikálni a szerverrel:

1. Kapcsolódás a szerverhez.

1. Felsorolni a képességeket, promptokat, erőforrásokat és eszközöket, és elmenteni azok sémáját.

1. Hozzáadni egy LLM-et, és az elmentett képességeket, valamint a sémájukat olyan formátumban továbbítani, amit az LLM ért.

1. Felhasználói prompt kezelésével azt átadni az LLM-nek az ügyfél által felsorolt eszközökkel együtt.

Remek, most, hogy nagy vonalakban megértettük, hogyan csináljuk, próbáljuk ki az alábbi gyakorlatban.

## Gyakorlat: Ügyfél létrehozása egy LLM-mel

Ebben a gyakorlatban megtanuljuk, hogyan adjunk egy LLM-et az ügyfelünkhöz.

### Hitelesítés GitHub személyes hozzáférési tokennel

Egy GitHub token létrehozása egyszerű folyamat. Így csinálhatod:

- Lépj a GitHub Beállításokhoz – Kattints a profilképedre a jobb felső sarokban, és válaszd a Beállításokat.
- Navigálj a Fejlesztői beállításokhoz – Görgess le, és kattints a Fejlesztői beállításokra.
- Válaszd a Személyes hozzáférési tokeneket – Kattints a Finomhangolt tokenekre, majd az Új token generálására.
- Konfiguráld a tokened – Adj hozzá egy megjegyzést, állítsd be a lejárati dátumot, és válaszd ki a szükséges jogosultságokat. Ebben az esetben győződj meg róla, hogy hozzáadtad a Models jogosultságot.
- Generáld és másold ki a tokent – Kattints a Token generálásra, és azonnal másold ki, mert később már nem fogod látni.

### -1- Kapcsolódás a szerverhez

Először hozzuk létre az ügyfelet:

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

Az előző kódban:

- Importáltuk a szükséges könyvtárakat
- Létrehoztunk egy osztályt két taggal, `client` és `openai`, amelyek segítenek az ügyfél kezelésében és az LLM-mel való interakcióban.
- Beállítottuk az LLM példányt, hogy GitHub Modelleket használjon, a `baseUrl` beállításával az inference API-ra mutatva.

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
            # A kapcsolat inicializálása
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Az előző kódban:

- Importáltuk a szükséges MCP könyvtárakat
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

Először hozzá kell adnod a LangChain4j függőségeket a `pom.xml` fájlhoz. Add hozzá ezeket a függőségeket az MCP integráció és a GitHub Modellek támogatásához:

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
    
    public static void main(String[] args) throws Exception {        // Az LLM beállítása a GitHub modellek használatára
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // MCP átvitel létrehozása a szerverhez való csatlakozáshoz
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
}
```

Az előző kódban:

- **Hozzáadtuk a LangChain4j függőségeket**: Az MCP integrációhoz, az OpenAI hivatalos klienshez és a GitHub Modellek támogatásához
- **Importáltuk a LangChain4j könyvtárakat**: MCP integráció és OpenAI chat modell funkciókhoz
- **Létrehoztunk egy `ChatLanguageModel` példányt**: Beállítva, hogy GitHub Modelleket használjon a GitHub tokeneddel
- **Beállítottuk az HTTP szállítást**: Server-Sent Events (SSE) használatával a MCP szerverhez való kapcsolódáshoz
- **Létrehoztunk egy MCP ügyfelet**: Amit a szerverrel való kommunikáció kezelésére használunk
- **Használtuk a LangChain4j beépített MCP támogatását**: Ami leegyszerűsíti az LLM-ek és MCP szerverek integrációját

#### Rust

Ez a példa feltételezi, hogy van egy Rust alapú MCP szervered. Ha nincs, nézd meg az [01-first-server](../01-first-server/README.md) leckét a szerver létrehozásához.

Miután megvan a Rust MCP szervered, nyiss meg egy terminált, és navigálj abba a könyvtárba, ahol a szerver található. Ezután futtasd a következő parancsot, hogy létrehozd az új LLM kliens projektet:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Add hozzá a következő függőségeket a `Cargo.toml` fájlhoz:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Nincs hivatalos Rust könyvtár az OpenAI-hoz, de az `async-openai` crate egy [közösség által karbantartott könyvtár](https://platform.openai.com/docs/libraries/rust#rust), amelyet gyakran használnak.

Nyisd meg a `src/main.rs` fájlt, és cseréld le a tartalmát az alábbi kódra:

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

Ez a kód alapvető Rust alkalmazást állít be, amely csatlakozik egy MCP szerverhez és GitHub Modellekhez az LLM interakciókhoz.

> [!IMPORTANT]
> Futás előtt győződj meg róla, hogy beállítottad az `OPENAI_API_KEY` környezeti változót a GitHub tokeneddel.

Remek, a következő lépésként soroljuk fel a szerver képességeit.

### -2- Szerver képességek listázása

Most kapcsolódunk a szerverhez és lekérdezzük a képességeit:

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

    // eszközök listázása
    const toolsResult = await this.client.listTools();
}
```

Az előző kódban:

- Hozzáadtuk a szerverhez való kapcsolódást megvalósító kódot, `connectToServer`.
- Létrehoztunk egy `run` metódust, amely az alkalmazás folyamatáért felel. Egyelőre csak az eszközöket listázza, de hamarosan bővítjük.

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

Itt amit hozzáadtunk:

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

Az előző kódban:

- Felsoroltuk a MCP szerveren elérhető eszközöket
- Minden eszköznél felsoroltuk a nevét, leírását és sémáját, amit később az eszközök hívásához fogunk használni.

#### Java

```java
// Hozzon létre egy eszközszolgáltatót, amely automatikusan felfedezi az MCP eszközöket
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Az MCP eszközszolgáltató automatikusan kezeli:
// - Az MCP szerverről elérhető eszközök listázását
// - Az MCP eszközsémák LangChain4j formátumba való átalakítását
// - Az eszközök végrehajtásának és válaszainak kezelését
```

Az előző kódban:

- Létrehoztunk egy `McpToolProvider`-t, amely automatikusan felfedezi és regisztrálja az összes eszközt az MCP szerverről
- Az eszközszolgáltató belsőleg kezeli az MCP eszköz sémák és a LangChain4j eszköz formátuma közötti átalakítást
- Ez a megközelítés elrejti az eszközök manuális listázását és átalakítását

#### Rust

Az MCP szerverről az eszközöket a `list_tools` metódussal kérheted le. A `main` függvényedben, az MCP kliens beállítása után add hozzá az alábbi kódot:

```rust
// MCP eszköz lista lekérése
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Szerver képességek átalakítása LLM eszközökké

A következő lépés az, hogy a szerver képességeit olyan formátumba konvertáljuk, amit az LLM ért. Miután ezt megtettük, ezeket a képességeket eszközként biztosíthatjuk az LLM-nek.

#### TypeScript

1. Add hozzá a következő kódot az MCP szerver válaszának olyan eszköz formátumba konvertálására, amit az LLM használhat:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Készíts egy zod sémát az input_schema alapján
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

    A fenti kód az MCP szerver válaszát vesz és eszköz definíciós formátumba alakítja, amit az LLM érteni tud.

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

    Az előző kódban frissítettük a `run` metódust, hogy végigmenjen az eredményeken, és mindegyikhez meghívja az `openAiToolAdapter`-t.

#### Python

1. Először hozzuk létre a következő konverter függvényt:

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

    A fenti `convert_to_llm_tools` függvény bemenetként MCP eszköz válaszát veszi, és az LLM által értett formátumra konvertálja.

1. Ezután frissítsük az ügyfél kódját, hogy használja ezt a függvényt így:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Itt egy hívást adunk hozzá a `convert_to_llm_tool`-hoz, hogy az MCP eszköz választ olyan formátummá alakítsuk, amit később az LLM-nek adhatunk.

#### .NET

1. Adjunk kódot az MCP eszköz válasz LLM által érthető formátumba konvertálásához

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

- Létrehoztunk egy `ConvertFrom` függvényt, ami nevet, leírást és bementi sémát vesz
- Definiáltunk egy funkciót, ami létrehoz egy FunctionDefinition-t, amit egy ChatCompletionsDefinition-nak ad át. Ez utóbbi az, amit az LLM ért.

1. Frissítsük a meglévő kódokat, hogy használja a fenti függvényt:

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
// Készítsen Bot felületet a természetes nyelvű interakcióhoz
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

- Egyszerű `Bot` interfészt definiáltunk a természetes nyelvű interakciókhoz
- Használtuk a LangChain4j `AiServices`-ét, hogy automatikusan összekösse az LLM-et az MCP eszköz szolgáltatóval
- A keretrendszer automatikusan kezeli az eszköz séma átalakítást és a funkcióhívásokat a háttérben
- Ez a megközelítés megszünteti a kézi eszköz átalakítást – a LangChain4j kezel minden MCP eszköz és LLM kompatibilis formátum közötti átalakítást

#### Rust

Az MCP eszköz válasz LLM által értett formátumba konvertálásához hozzáadunk egy segédfüggvényt, amely formázza az eszközök listáját. Add hozzá az alábbi kódot a `main.rs` fájlhoz a `main` függvény alá. Ezt fogjuk hívni az LLM kéréskor:

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

Remek, most, hogy készen állunk a felhasználói kérések kezelésére, foglalkozzunk azzal.

### -4- Felhasználói prompt kérés kezelése

Ebben a kódrészben a felhasználói kérdéseket kezeljük.

#### TypeScript

1. Adj hozzá egy metódust, amivel hívni tudjuk az LLM-et:

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

    Az előző kódban:

    - Hozzáadtunk egy `callTools` metódust.
    - A metódus megvizsgálja az LLM válaszát, hogy lássa, mely eszközöket hívták meg, ha egyáltalán:

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

        // 3. Csináljon valamit az eredménnyel
        // TEENDŐ
        ```

1. Frissítsd a `run` metódust, hogy tartalmazza az LLM hívását és a `callTools` meghívását:

    ```typescript

    // 1. Üzenetek létrehozása, amelyek bemenetként szolgálnak az LLM-hez
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

    // 3. Végigmenni az LLM válaszán, minden választásnál ellenőrizni, hogy van-e eszközhívás
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Remek, íme a teljes kód:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Zod importálása sémavizsgálathoz

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // Lehet, hogy később ezt az URL-t kell használni: https://models.github.ai/inference
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
          // Zod séma létrehozása az input_schema alapján
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Típus egyértelmű beállítása "function"-re
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
    
    
          // 2. A szerver eszközének meghívása
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Valamit kezdeni az eredménnyel
          // ELVÉGZENDŐ
    
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
    
        // 1. Átnézni az LLM választ, minden választási lehetőségnél ellenőrizni, hogy vannak-e eszközhívások
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

1. Adjunk hozzá néhány importot, amik kellenek az LLM hívásához

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Ezután adjuk hozzá azt a függvényt, ami hívni fogja az LLM-et:

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

- Átadtuk az LLM-nek azokat a függvényeket, amiket az MCP szerverről kaptunk és átalakítottunk.
- Ezután meghívtuk az LLM-et ezekkel a funkciókkal.
- Megvizsgáljuk az eredményt, hogy mely funkciókat kell hívni, ha kell.
- Végül egy tömböt adunk át a hívandó funkciókkal.

1. Az utolsó lépés, frissítsük a fő kódot:

    ```python
    prompt = "Add 2 to 20"

    # kérdezd meg az LLM-et, milyen eszközök állnak rendelkezésre, ha vannak
    functions_to_call = call_llm(prompt, functions)

    # hívd meg a javasolt funkciókat
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

Ott volt a végső lépés, a fenti kódban:

- Meghívunk egy MCP eszközt a `call_tool`-lal, a funkciót az LLM által javasolt hívások alapján.
- Kiírjuk az eszköz hívás eredményét az MCP szervertől.

#### .NET

1. Mutatunk kódot az LLM prompt kéréshez:

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
- Meghatároztuk a felhasználói promptot `userMessage`.
- Összeállítottunk egy options objektumot a modell és eszközök megadásával.
- Kérést tettünk az LLM felé.

1. Egy utolsó lépés, nézzük, hogy az LLM szerint kell-e függvényt hívni:

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

- Végigmentünk a funkcióhívások listáján.
- Minden eszköz hívásnál kiolvastuk a nevet és paramétereket, és meghívtuk az MCP szerver eszközt a MCP kliens segítségével. Végül kiírtuk az eredményeket.

Itt a teljes kód:

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
    // Természetes nyelvű kérések végrehajtása, amelyek automatikusan az MCP eszközöket használják
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

- Egyszerű természetes nyelvű promptokat használtunk az MCP szerver eszközeinek hívásához
- A LangChain4j keretrendszer automatikusan kezeli:
  - A felhasználói promptokat eszköz hívássá alakítja szükség szerint
  - Meghívja a megfelelő MCP eszközöket az LLM döntése alapján
  - Kezeli a beszélgetési folyamatot az LLM és az MCP szerver között
- A `bot.chat()` metódus természetes nyelvű válaszokat ad, amelyek tartalmazhatják az MCP eszközök eredményeit
- Ez a megközelítés zökkenőmentes felhasználói élményt nyújt, ahol a felhasználóknak nem kell tudniuk az MCP háttérről

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

Itt történik a munka java része. Meghívjuk az LLM-et a kezdeti felhasználói prompttal, aztán feldolgozzuk a választ, hogy látjuk, kell-e eszközöket hívni. Ha igen, meghívjuk azokat, és folytatjuk a beszélgetést az LLM-mel, amíg nincs több eszköz hívás és megkapjuk a végleges választ.

Többször fogjuk hívni az LLM-et, ezért definiáljunk egy függvényt, ami kezeli az LLM hívást. Add hozzá a következő függvényt a `main.rs` fájlhoz:

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

Ez a függvény megkapja az LLM klienset, üzenetek listáját (beleértve a felhasználói promptot), az MCP szerver eszközeit, elküldi a kérést az LLM-nek, és visszaadja a választ.
Az LLM válasza tartalmazni fog egy `choices` tömböt. Feldolgoznunk kell az eredményt, hogy lássuk, vannak-e benne `tool_calls`. Ez jelzi számunkra, hogy az LLM egy adott eszköz hívását kéri meg argumentumokkal. Add hozzá a következő kódot a `main.rs` fájlod végéhez, hogy definiálj egy függvényt az LLM válaszának kezelésére:

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

    // Tartalom kiírása, ha elérhető
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Eszközhívások kezelése
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Segéd üzenet hozzáadása

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

Ha jelen vannak `tool_calls`, akkor kinyeri az eszköz információkat, meghívja az MCP szervert az eszköz kéréssel, és hozzáadja az eredményeket a beszélgetés üzeneteihez. Ezután folytatja a beszélgetést az LLM-mel, és az üzenetek frissülnek az asszisztens válaszával és az eszköz hívás eredményeivel.

Ahhoz, hogy kinyerjük az eszköz hívás információkat, amelyeket az LLM ad vissza MCP hívásokhoz, hozzáadunk egy másik segédfüggvényt, hogy kinyerjük mindazt, ami a híváshoz szükséges. Add hozzá a következő kódot a `main.rs` fájlod végéhez:

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

Minden darab a helyén van, most már kezelni tudjuk a kezdeti felhasználói utasítást és meghívni az LLM-et. Frissítsd a `main` függvényed, hogy tartalmazza a következő kódot:

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

Ez lekérdezi az LLM-et a kezdeti felhasználói kéréssel, amely két szám összegét kéri, és feldolgozza a választ, hogy dinamikusan kezelje az eszköz hívásokat.

Remek, sikerült!

## Feladat

Vedd az elméleti kódot és építs ki a szervert több eszközzel. Ezután készíts egy klienst LLM-mel, mint az elméletben, és teszteld különböző kérdésekkel, hogy megbizonyosodj róla, hogy az összes szerver eszközt dinamikusan hívja meg. Ez a kliensépítési mód azt jelenti, hogy a végfelhasználónak kiváló felhasználói élménye lesz, mert promptokat használhat pontos kliens parancsok helyett, és nem is tud róla, hogy bármilyen MCP szerver hívás történik.

## Megoldás

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## Főbb tanulságok

- Az LLM hozzáadása a kliensedhez jobb módot biztosít a felhasználók számára, hogy MCP szerverekkel kommunikáljanak.
- Az MCP szerver válaszát át kell alakítani olyanná, amit az LLM megért.

## Minták

- [Java Számológép](../samples/java/calculator/README.md)
- [.Net Számológép](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Számológép](../samples/javascript/README.md)
- [TypeScript Számológép](../samples/typescript/README.md)
- [Python Számológép](../../../../03-GettingStarted/samples/python)
- [Rust Számológép](../../../../03-GettingStarted/samples/rust)

## További források

## Mi következik

- Következő: [Szerver használata Visual Studio Code-ból](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősségkizárás**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Habár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy a gépi fordítás hibákat vagy pontatlanságokat tartalmazhat. Az eredeti, anyanyelvi dokumentum tekintendő hiteles forrásnak. Kritikus információk esetén szakmai humán fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->