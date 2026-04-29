# Vytvoření klienta s LLM

Doposud jste viděli, jak vytvořit server a klienta. Klient byl schopen explicitně volat server, aby vypsal jeho nástroje, zdroje a výzvy. Nicméně, toto není příliš praktický přístup. Vaši uživatelé žijí v agentní éře a očekávají, že budou používat výzvy a komunikovat s LLM. Nezajímají je detaily, zda používáte MCP ke skladování svých schopností; jednoduše očekávají, že budou komunikovat pomocí přirozeného jazyka. Jak to tedy vyřešíme? Řešením je přidat LLM ke klientovi.

## Přehled

V této lekci se zaměříme na přidání LLM do vašeho klienta a ukážeme, jak to poskytuje mnohem lepší zážitek pro vašeho uživatele.

## Cíle učení

Na konci této lekce budete umět:

- Vytvořit klienta s LLM.
- Bezproblémově komunikovat s MCP serverem pomocí LLM.
- Poskytnout lepší uživatelský zážitek na straně klienta.

## Přístup

Pojďme se pokusit pochopit přístup, který musíme zvolit. Přidání LLM zní jednoduše, ale uděláme to skutečně?

Takto bude klient komunikovat se serverem:

1. Navázat spojení se serverem.

1. Vypsat schopnosti, výzvy, zdroje a nástroje, a uložit jejich schéma.

1. Přidat LLM a předat uložené schopnosti a jejich schéma ve formátu, kterému LLM rozumí.

1. Zpracovat uživatelskou výzvu tak, že ji předáme LLM spolu s nástroji, které klient vypsal.

Skvělé, teď když rozumíme, jak to můžeme udělat na vysoké úrovni, pojďme to vyzkoušet v níže uvedeném cvičení.

## Cvičení: Vytvoření klienta s LLM

V tomto cvičení se naučíme přidat LLM k našemu klientovi.

### Autentizace pomocí GitHub Personal Access Token

Vytvoření GitHub tokenu je jednoduchý proces. Tady je návod, jak na to:

- Jděte do GitHub Settings – Klikněte na svůj profilový obrázek v pravém horním rohu a zvolte Nastavení.
- Přejděte do Developer Settings – Sjeďte dolů a klikněte na Developer Settings.
- Zvolte Personal Access Tokens – Klikněte na Fine-grained tokens a poté Generate new token.
- Nakonfigurujte si svůj token – Přidejte poznámku pro orientaci, nastavte datum vypršení platnosti a vyberte potřebné rozsahy (oprávnění). V tomto případě nezapomeňte přidat oprávnění Models.
- Vygenerujte a zkopírujte token – Klikněte na Generate token a nezapomeňte ho ihned zkopírovat, protože jej později neuvidíte.

### -1- Připojení k serveru

Nejprve vytvoříme našeho klienta:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importujte zod pro validaci schématu

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

V předchozím kódu jsme:

- Importovali potřebné knihovny
- Vytvořili třídu se dvěma členy, `client` a `openai`, kteří nám pomohou spravovat klienta a komunikovat s LLM.
- Nakonfigurovali naši instanci LLM tak, aby používala GitHub Models nastavením `baseUrl` směrujícího na inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Vytvořit parametry serveru pro připojení přes stdio
server_params = StdioServerParameters(
    command="mcp",  # Spustitelný soubor
    args=["run", "server.py"],  # Nepovinné argumenty příkazového řádku
    env=None,  # Nepovinné proměnné prostředí
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inicializovat připojení
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

V předchozím kódu jsme:

- Importovali potřebné knihovny pro MCP
- Vytvořili klienta

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

Nejprve si přidejte závislosti LangChain4j do souboru `pom.xml`. Přidejte tyto závislosti, aby byla povolena integrace s MCP a podpora GitHub Models:

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

Pak vytvořte svou třídu Java klienta:

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
    
    public static void main(String[] args) throws Exception {        // Nakonfigurujte LLM pro použití modelů GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Vytvořte MCP transport pro připojení k serveru
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Vytvořte MCP klienta
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

V předchozím kódu jsme:

- **Přidali závislosti LangChain4j**: Požadované pro integraci MCP, oficiální OpenAI klient a podporu GitHub Models
- **Importovali knihovny LangChain4j**: Pro integraci MCP a funkce OpenAI chat modelu
- **Vytvořili `ChatLanguageModel`**: Nastavený na použití GitHub Models s tokenem z GitHubu
- **Nastavili HTTP přenos**: pomocí Server-Sent Events (SSE) pro připojení k MCP serveru
- **Vytvořili MCP klienta**: který bude spravovat komunikaci se serverem
- **Použili zabudovanou podporu MCP v LangChain4j**: která zjednodušuje integraci mezi LLM a MCP servery

#### Rust

Tento příklad předpokládá, že máte spuštěný Rust-based MCP server. Pokud jej nemáte, vraťte se k lekci [01-first-server](../01-first-server/README.md) pro vytvoření serveru.

Jakmile máte svůj Rust MCP server, otevřete terminál a přejděte do stejného adresáře jako server. Pak spusťte následující příkaz pro vytvoření nového projektu LLM klienta:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Přidejte následující závislosti do souboru `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Neexistuje oficiální Rust knihovna pro OpenAI, nicméně `async-openai` crate je [komunitně udržovaná knihovna](https://platform.openai.com/docs/libraries/rust#rust), která se běžně používá.

Otevřete soubor `src/main.rs` a nahraďte jeho obsah následujícím kódem:

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
    // Počáteční zpráva
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Nastavení klienta OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Nastavení klienta MCP
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

    // TODO: Získat seznam nástrojů MCP

    // TODO: Konverzace LLM s voláním nástrojů

    Ok(())
}
```

Tento kód nastavuje základní Rust aplikaci, která se připojí k MCP serveru a GitHub Models pro interakci s LLM.

> [!IMPORTANT]
> Nezapomeňte nastavit environmentální proměnnou `OPENAI_API_KEY` s vaším GitHub tokenem před spuštěním aplikace.

Skvělé, jako další krok vypsáme schopnosti na serveru.

### -2- Výpis schopností serveru

Teď se připojíme k serveru a požádáme o jeho schopnosti:

#### Typescript

Do stejné třídy přidejte následující metody:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // nástroje pro výpis
    const toolsResult = await this.client.listTools();
}
```

V předchozím kódu jsme:

- Přidali kód pro navázání spojení se serverem, `connectToServer`.
- Vytvořili metodu `run` zodpovědnou za řízení toku naší aplikace. Zatím pouze vypisuje nástroje, ale brzy do ní přidáme další funkce.

#### Python

```python
# Vypsat dostupné zdroje
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Vypsat dostupné nástroje
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Zde jsme přidali:

- Výpis zdrojů a nástrojů a jejich vytištění. U nástrojů také vypisujeme `inputSchema`, které později použijeme.

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

V předchozím kódu jsme:

- Vypsali nástroje dostupné na MCP serveru
- Pro každý nástroj vypsali jeho název, popis a schéma. To budeme brzy používat k volání nástrojů.

#### Java

```java
// Vytvořte poskytovatele nástrojů, který automaticky objevuje nástroje MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Poskytovatel nástrojů MCP automaticky zpracovává:
// - Výpis dostupných nástrojů ze serveru MCP
// - Převod schémat nástrojů MCP do formátu LangChain4j
// - Správu spuštění nástrojů a odpovědí
```

V předchozím kódu jsme:

- Vytvořili `McpToolProvider`, který automaticky objeví a zaregistruje všechny nástroje z MCP serveru
- Poskytovatel nástrojů se interně postará o převod mezi MCP schématy nástrojů a formátem nástrojů LangChain4j
- Tento přístup abstrahuje manuální proces výpisu a převodu nástrojů

#### Rust

Získání nástrojů ze serveru MCP se provádí pomocí metody `list_tools`. Ve vaší funkci `main`, po nastavení MCP klienta, přidejte následující kód:

```rust
// Získat seznam nástrojů MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Převod schopností serveru na nástroje LLM

Dalším krokem po vypsání schopností serveru je jejich převod do formátu, kterému LLM rozumí. Jakmile to uděláme, můžeme tyto schopnosti poskytnout jako nástroje našemu LLM.

#### TypeScript

1. Přidejte následující kód k převodu odpovědi z MCP serveru do formátu nástroje, který LLM dokáže použít:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Vytvořte schéma zod na základě input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Explicitně nastavte typ na "function"
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

    Výše uvedený kód vezme odpověď z MCP serveru a převede ji na formát definice nástroje, kterému LLM rozumí.

1. Aktualizujme následující metodu `run`, aby vypsala schopnosti serveru:

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

    V předchozím kódu jsme aktualizovali metodu `run` tak, že procházející výsledkem a pro každý záznam voláme `openAiToolAdapter`.

#### Python

1. Nejprve vytvořme následující konverzní funkci

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

    V této funkci `convert_to_llm_tools` vezmeme odpověď nástroje MCP a převedeme ji do formátu, kterému LLM rozumí.

1. Dále aktualizujme kód klienta, aby využíval tuto funkci takto:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Zde přidáváme volání `convert_to_llm_tool` k převodu odpovědi MCP nástroje na formát, který následně předáme LLM.

#### .NET

1. Přidejme kód pro převod odpovědi MCP nástroje do formátu, kterému LLM rozumí:

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

V předchozím kódu jsme:

- Vytvořili funkci `ConvertFrom`, která přijímá název, popis a vstupní schéma.
- Definovali funkcionalitu, která vytvoří `FunctionDefinition`, která je předána do `ChatCompletionsDefinition`. To je formát, který LLM dokáže zpracovat.

1. Podívejme se, jak můžeme aktualizovat existující kód k využití této funkce:

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
// Vytvořte rozhraní Bota pro interakci v přirozeném jazyce
public interface Bot {
    String chat(String prompt);
}

// Nakonfigurujte AI službu s nástroji LLM a MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

V předchozím kódu jsme:

- Definovali jednoduché rozhraní `Bot` pro interakce v přirozeném jazyce
- Použili `AiServices` LangChain4j k automatickému spojení LLM s poskytovatelem MCP nástrojů
- Framework automaticky řeší konverzi schémat nástrojů a volání funkcí na pozadí
- Tento přístup eliminuje manuální převod nástrojů – LangChain4j se stará o veškerou složitost převodu MCP nástrojů do formátu kompatibilního s LLM

#### Rust

Pro převod odpovědi MCP nástroje na formát, kterému LLM rozumí, přidáme pomocnou funkci formátující výpis nástrojů. Přidejte následující kód do souboru `main.rs` pod funkci `main`. Bude volán při požadavcích na LLM:

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

Skvělé, jsme nyní připraveni zpracovat uživatelské požadavky, pojďme na to.

### -4- Zpracování uživatelské výzvy

V této části kódu budeme zpracovávat uživatelské požadavky.

#### TypeScript

1. Přidejte metodu, která bude sloužit ke volání našeho LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Zavolejte nástroj serveru
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Udělejte něco s výsledkem
        // TODO

        }
    }
    ```

    V předchozím kódu jsme:

    - Přidali metodu `callTools`.
    - Metoda přijímá odpověď LLM a kontroluje, jaké nástroje byly volány, pokud vůbec:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // zavolat nástroj
        }
        ```

    - Volá nástroj, pokud LLM ukáže, že by měl být zavolán:

        ```typescript
        // 2. Zavolejte nástroj serveru
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Něco udělejte s výsledkem
        // TODO
        ```

1. Aktualizujte metodu `run`, aby zahrnovala volání LLM a následně volání `callTools`:

    ```typescript

    // 1. Vytvořit zprávy, které jsou vstupem pro LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Volání LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Projít odpověď LLM, u každé možnosti zkontrolovat, zda obsahuje volání nástrojů
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Skvělé, vypsat celý kód:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importujte zod pro ověřování schémat

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // v budoucnu může být potřeba změnit na tuto URL: https://models.github.ai/inference
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
          // Vytvořte zod schéma na základě input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Explicitně nastavte typ na "function"
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
    
    
          // 2. Zavolejte nástroj serveru
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Něco udělejte s výsledkem
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
    
        // 1. Projděte odpověď LLM, pro každou volbu zkontrolujte, zda obsahuje volání nástrojů
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

1. Přidejme některé importy potřebné pro volání LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Dále přidejme funkci, která bude volat LLM:

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
            # Volitelné parametry
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

    V předchozím kódu jsme:

    - Předali funkce, které jsme našli na MCP serveru a převedli, LLM.
    - Následně jsme zavolali LLM s těmito funkcemi.
    - Prohlížíme si výsledek, abychom zjistili, jaké funkce případně zavolat.
    - Nakonec voláme příslušné funkce.

1. Posledním krokem je aktualizace hlavního kódu:

    ```python
    prompt = "Add 2 to 20"

    # zeptej se LLM, jaké nástroje má použít, pokud nějaké
    functions_to_call = call_llm(prompt, functions)

    # zavolej navrhované funkce
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Toto byl poslední krok. V kódu výše jsme:

    - Volali MCP nástroj přes `call_tool` pomocí funkce, o které LLM usoudil, že ji má zavolat na základě výzvy.
    - Vypisujeme výsledek volání nástroje na MCP Server.

#### .NET

1. Představme kód, který vykoná požadavek na LLM:

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

    V předchozím kódu jsme:

    - Načetli nástroje ze serveru MCP, `var tools = await GetMcpTools()`.
    - Definovali uživatelskou výzvu `userMessage`.
    - Vytvořili objekt možností specifikující model a nástroje.
    - Odeslali požadavek na LLM.

1. Jeden poslední krok, podívejme se, zda LLM soudí, že bychom měli zavolat funkci:

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

    V předchozím kódu jsme:

    - Prošli seznam volání funkcí.
    - Pro každé volání nástroje jsme rozebrali název a argumenty a volali nástroj na serveru MCP pomocí MCP klienta. Nakonec vypisujeme výsledky.

Zde je celý kód:

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
    // Vykonávejte požadavky v přirozeném jazyce, které automaticky používají nástroje MCP
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

V předchozím kódu jsme:

- Použili jednoduché přirozené jazykové výzvy k interakci s MCP nástroji serveru
- Framework LangChain4j automaticky zpracovává:
  - Převod uživatelských výzev na volání nástrojů, pokud je to potřeba
  - Volání příslušných MCP nástrojů na základě rozhodnutí LLM
  - Řízení konverzačního toku mezi LLM a MCP serverem
- Metoda `bot.chat()` vrací odpovědi v přirozeném jazyce, které mohou zahrnovat výsledky vykonání MCP nástrojů
- Tento přístup poskytuje plynulý uživatelský zážitek, kde uživatelé nemusí vědět o pozadí implementace MCP

Kompletní příklad kódu:

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

Zde se odehrává většina práce. Nejprve zavoláme LLM s počáteční uživatelskou výzvou, poté zpracujeme odpověď, abychom zjistili, zda je potřeba zavolat nějaké nástroje. Pokud ano, zavoláme tyto nástroje a budeme pokračovat v konverzaci s LLM, dokud nebude potřeba další volání nástrojů a získáme finální odpověď.

Budeme vykonávat více volání LLM, proto definujeme funkci, která se bude o volání LLM starat. Přidejte následující funkci do souboru `main.rs`:

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

Tato funkce přijímá LLM klienta, seznam zpráv (včetně uživatelské výzvy), nástroje z MCP serveru a odešle požadavek LLM, pak vrátí odpověď.
Odezva z LLM bude obsahovat pole `choices`. Budeme muset zpracovat výsledek a zjistit, zda jsou přítomny nějaké `tool_calls`. To nám umožní vědět, že LLM požaduje, aby byl s argumenty zavolán konkrétní nástroj. Přidejte následující kód na konec vašeho souboru `main.rs`, abyste definovali funkci pro zpracování odezvy LLM:

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

    // Vytisknout obsah, pokud je k dispozici
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Zpracovat volání nástrojů
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Přidat zprávu asistenta

        // Proveďte každé volání nástroje
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Přidat výsledek nástroje do zpráv
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Pokračovat v konverzaci s výsledky nástroje
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

Pokud jsou přítomny `tool_calls`, extrahuje informace o nástroji, zavolá MCP server s požadavkem nástroje a přidá výsledky do zpráv konverzace. Poté pokračuje v konverzaci s LLM a zprávy jsou aktualizovány odpovědí asistenta a výsledky volání nástroje.

Pro extrahování informací o volání nástroje, které LLM vrací pro MCP volání, přidáme další pomocnou funkci, která získá vše potřebné pro provedení volání. Přidejte následující kód na konec vašeho souboru `main.rs`:

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

S veškerými díly na místě nyní můžeme zpracovat počáteční uživatelský prompt a zavolat LLM. Aktualizujte svou funkci `main` tak, aby obsahovala následující kód:

```rust
// Konverzace LLM s voláními nástrojů
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

Tento kód bude dotazovat LLM s počátečním uživatelským promptem žádajícím o součet dvou čísel a zpracuje odpověď tak, aby dynamicky zvládl volání nástrojů.

Výborně, zvládli jste to!

## Zadání

Vezměte kód z cvičení a rozšiřte server o další nástroje. Poté vytvořte klienta s LLM, jako v cvičení, a otestujte jej s různými prompty, abyste se ujistili, že všechny vaše serverové nástroje jsou dynamicky volány. Tento způsob vytváření klienta znamená, že koncový uživatel bude mít skvělý uživatelský zážitek, protože může používat prompty namísto přesných příkazů klienta a nebude si všímat žádných volání MCP serveru.

## Řešení

[Řešení](./solution/README.md)

## Klíčová poznání

- Přidání LLM do vašeho klienta poskytuje lepší způsob, jak uživatelé mohou komunikovat se servery MCP.
- Je potřeba převést odpověď MCP serveru na něco, čemu LLM rozumí.

## Vzory

- [Java Kalkulačka](../samples/java/calculator/README.md)
- [.Net Kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](../samples/javascript/README.md)
- [TypeScript Kalkulačka](../samples/typescript/README.md)
- [Python Kalkulačka](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulačka](../../../../03-GettingStarted/samples/rust)

## Další zdroje

## Co bude dál

- Dál: [Používání serveru ve Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje využít profesionální lidský překlad. Nejsme odpovědní za jakákoli nedorozumění nebo mylné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->