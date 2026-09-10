# Vytvoření klienta s LLM

Doposud jste viděli, jak vytvořit server a klienta. Klient mohl explicitně volat server za účelem výpisu jeho nástrojů, zdrojů a promptů. Toto však není příliš praktický přístup. Vaši uživatelé žijí v agentické éře a očekávají, že budou používat prompt a komunikovat s LLM. Nezajímá je, jestli používáte MCP pro uložení svých schopností; jednoduše očekávají, že budou komunikovat přirozeným jazykem. Jak to tedy vyřešíme? Řešením je přidat LLM ke klientovi.

## Přehled

V této lekci se zaměříme na přidání LLM do vašeho klienta a ukážeme, jak to poskytuje mnohem lepší zážitek pro vašeho uživatele.

## Cíle učení

Na konci této lekce budete schopni:

- Vytvořit klienta s LLM.
- Bezproblémově komunikovat se serverem MCP pomocí LLM.
- Poskytnout lepší uživatelský zážitek na straně klienta.

## Přístup

Pojďme se pokusit pochopit přístup, který je potřeba použít. Přidání LLM zní jednoduše, ale opravdu to tak uděláme?

Zde je, jak bude klient komunikovat se serverem:

1. Navázání spojení se serverem.

1. Výpis schopností, promptů, zdrojů a nástrojů a uložení jejich schématu.

1. Přidání LLM a předání uložených schopností a jejich schématu ve formátu, který LLM rozumí.

1. Zpracování uživatelského promptu předáním LLM společně s nástroji, které klient vypsal.

Skvěle, teď když chápeme, jak to udělat na vysoké úrovni, pojďme to vyzkoušet v následujícím cvičení.

## Cvičení: Vytvoření klienta s LLM

V tomto cvičení se naučíme přidat LLM do našeho klienta.

### Autentizace pomocí osobního přístupového tokenu GitHubu

Vytvoření tokenu na GitHubu je přímý proces. Zde je návod, jak to můžete udělat:

- Jděte do Nastavení GitHubu – Klikněte na svůj profilový obrázek v pravém horním rohu a vyberte Nastavení.
- Přejděte do Nastavení vývojáře – Sjeďte dolů a klikněte na Nastavení vývojáře.
- Vyberte osobní přístupové tokeny – Klikněte na Fine-grained tokens a poté Generovat nový token.
- Nakonfigurujte svůj token – Přidejte poznámku pro referenci, nastavte datum vypršení platnosti a vyberte potřebné rozsahy (oprávnění). V tomto případě nezapomeňte přidat oprávnění Models.
- Vygenerujte a zkopírujte token – Klikněte na Generovat token a ihned si ho zkopírujte, protože ho už znovu neuvidíte.

### -1- Připojení k serveru

Nejprve vytvořme našeho klienta:

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

- Naimportovali potřebné knihovny
- Vytvořili třídu se dvěma členy, `client` a `openai`, kteří nám pomohou spravovat klienta a interagovat s LLM.
- Nakonfigurovali instanci LLM tak, aby používala GitHub Models nastavením `baseUrl` na inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Vytvořit parametry serveru pro stdio připojení
server_params = StdioServerParameters(
    command="mcp",  # Spustitelný soubor
    args=["run", "server.py"],  # Volitelné argumenty příkazového řádku
    env=None,  # Volitelné proměnné prostředí
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

- Naimportovali potřebné knihovny pro MCP
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

Nejprve budete muset přidat závislosti LangChain4j do souboru `pom.xml`. Přidejte tyto závislosti pro povolení integrace MCP a OpenAI-kompatibilního MiniMax API:

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

Nastavte svůj MiniMax API klíč a volitelně endpoint a model.
`MINIMAX_MODEL_ID` podporuje `MiniMax-M3` a `MiniMax-M2.7`. Pokud
`OPENAI_BASE_URL` není nastaveno, `MINIMAX_REGION` podporuje `global_en` a `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Pro výběr endpointu podle regionu vynechte `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
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

        // Vytvořit MCP transport pro připojení k serveru
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Vytvořit MCP klienta
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

V předchozím kódu jsme:

- **Přidali závislosti LangChain4j**: Potřebné pro integraci MCP a OpenAI-kompatibilní MiniMax API
- **Naimportovali knihovny LangChain4j**: Pro integraci MCP a funkcionalitu OpenAI chat modelu
- **Vytvořili `ChatLanguageModel`**: Nakonfigurovaný pro použití MiniMax s vaším MiniMax API klíčem, endpointem a podporovaným ID modelu
- **Nastavili HTTP transport**: Pomocí Server-Sent Events (SSE) k připojení k MCP serveru
- **Vytvořili MCP klienta**: Který bude spravovat komunikaci se serverem
- **Použili vestavěnou podporu MCP v LangChain4j**: Což zjednodušuje integraci mezi LLM a MCP servery

#### Rust

Tento příklad předpokládá, že máte spuštěný MCP server napsaný v Rustu. Pokud ho nemáte, vraťte se k lekci [01-first-server](../01-first-server/README.md) a vytvořte server.

Jakmile máte Rust MCP server, otevřete terminál a přejděte do stejné složky jako server. Poté spusťte následující příkaz pro vytvoření nového projektu LLM klienta:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Přidejte následující závislosti do svého souboru `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Oficiální Rust knihovna pro OpenAI neexistuje, nicméně `async-openai` crate je [knihovnou udržovanou komunitou](https://platform.openai.com/docs/libraries/rust#rust), která se běžně používá.

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

    // TODO: Konverzace LLM s voláními nástrojů

    Ok(())
}
```

Tento kód nastavuje základní Rust aplikaci, která se připojí k MCP serveru a GitHub Models pro interakce s LLM.

> [!IMPORTANT]
> Před spuštěním aplikace si nezapomeňte nastavit proměnnou prostředí `OPENAI_API_KEY` s vaším GitHub tokenem.

Skvěle, dalším krokem je vypsat schopnosti na serveru.

### -2- Výpis schopností serveru

Nyní se připojíme k serveru a požádáme o jeho schopnosti:

#### Typescript

Do téže třídy přidejte následující metody:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // výpis nástrojů
    const toolsResult = await this.client.listTools();
}
```

V předchozím kódu jsme:

- Přidali kód pro připojení k serveru, `connectToServer`.
- Vytvořili metodu `run`, která je zodpovědná za zpracování toku aplikace. Zatím jen vypisuje nástroje, ale brzy přidáme další funkce.

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

Přidali jsme toto:

- Výpis zdrojů a nástrojů a jejich vytištění. Pro nástroje také vypisujeme `inputSchema`, který později použijeme.

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
- U každého nástroje vypsali jméno, popis a jeho schéma. To budeme později používat pro volání nástrojů.

#### Java

```java
// Vytvořte poskytovatele nástrojů, který automaticky objeví nástroje MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Poskytovatel nástrojů MCP automaticky zajišťuje:
// - Vyjmenování dostupných nástrojů ze serveru MCP
// - Převod schémat nástrojů MCP do formátu LangChain4j
// - Správu spouštění nástrojů a odpovědí
```

V předchozím kódu jsme:

- Vytvořili `McpToolProvider`, který automaticky vyhledá a zaregistruje všechny nástroje z MCP serveru
- Poskytovatel nástrojů interně řeší převod mezi MCP nástrojovými schématy a formátem nástrojů LangChain4j
- Tento přístup abstrahuje manuální výpis a převod nástrojů

#### Rust

Získání nástrojů z MCP serveru se dělá metodou `list_tools`. Ve vaší funkci `main`, po nastavení MCP klienta, přidejte následující kód:

```rust
// Získat seznam nástrojů MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Převod schopností serveru na LLM nástroje

Dalším krokem po výpisu schopností serveru je převést je do formátu, kterému LLM rozumí. Jakmile to uděláme, můžeme tyto schopnosti poskytnout jako nástroje našemu LLM.

#### TypeScript

1. Přidejte následující kód pro převod odpovědi z MCP serveru do formátu nástrojů, které LLM může použít:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Vytvořte zod schéma na základě vstupního schématu
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

2. Aktualizujme teď metodu `run`, abychom vypsali schopnosti serveru:

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

    V předchozím kódu jsme aktualizovali metodu `run` tak, že procházejí výsledek a pro každý záznam volají `openAiToolAdapter`.

#### Python

1. Nejdříve vytvořme následující převodní funkci

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

    Ve funkci `convert_to_llm_tools` převádíme odpověď MCP nástroje na formát, kterému LLM rozumí.

2. Dále aktualizujme náš klientský kód takto:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Zde přidáváme volání `convert_to_llm_tool` pro převod odpovědi MCP nástroje na formát, který později můžeme předat LLM.

#### .NET

1. Přidejme kód pro převod odpovědi MCP nástroje na formát, kterému LLM rozumí

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
- Definovali funkčnost, jež vytváří `FunctionDefinition`, která se předává `ChatCompletionsDefinition`. To je něco, čemu LLM rozumí.

2. Pojďme se podívat, jak můžeme aktualizovat stávající kód, abychom využili této funkce:

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
- Použili LangChain4j `AiServices` pro automatické spojení LLM s poskytovatelem MCP nástrojů
- Framework automaticky zpracovává převod schémat nástrojů a volání funkcí na pozadí
- Tento přístup eliminuje manuální převod nástrojů - LangChain4j řeší veškerou složitost převádění MCP nástrojů do formátu kompatibilního s LLM

#### Rust

Pro převod odpovědi MCP nástroje do formátu, kterému LLM rozumí, přidáme pomocnou funkci, která naformátuje seznam nástrojů. Přidejte následující kód do souboru `main.rs` pod funkci `main`. Bude volána při požadavcích na LLM:

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

Skvěle, jsme připraveni zpracovat uživatelské požadavky, takže se na to podíváme dále.

### -4- Zpracování uživatelských promptů

V této části kódu budeme zpracovávat požadavky uživatelů.

#### TypeScript

1. Přidejte metodu, která bude použita k volání našeho LLM:

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

        // 3. Něco udělejte s výsledkem
        // TODO

        }
    }
    ```

    V předchozím kódu jsme:

    - Přidali metodu `callTools`.
    - Metoda přijímá odpověď LLM a kontroluje, jaké nástroje byly volány, pokud vůbec.

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // zavolat nástroj
        }
        ```

    - Pokud LLM naznačuje, že má být nástroj volán, metoda ho zavolá.

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

2. Aktualizujte metodu `run` tak, aby zahrnovala volání LLM a volání `callTools`:

    ```typescript

    // 1. Vytvořte zprávy, které jsou vstupem pro LLM
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

    // 3. Projděte odpověď LLM, pro každou volbu zkontrolujte, zda obsahuje volání nástrojů
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Skvěle, vyjmenujme si kód kompletně:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importujte zod pro validaci schématu

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // možná bude v budoucnu potřeba změnit na tuto URL: https://models.github.ai/inference
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
    
          // 3. Udělejte něco s výsledkem
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
    
        // 3. Projděte odpověď LLM, pro každou volbu zkontrolujte, zda obsahuje volání nástrojů
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

1. Přidejme potřebné importy pro volání LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Dále přidáme funkci, která LLM zavolá:

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
            # Nepovinné parametry
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

    - Předali naše funkce, které jsme našli na MCP serveru a převedli, LLM.
    - Pak jsme LLM zavolali s těmito funkcemi.
    - Poté zkoumáme výsledek, abychom zjistili, jaké funkce máme případně volat.
    - Nakonec předáme pole funkcí, které máme volat.

3. Poslední krok, aktualizujme náš hlavní kód:

    ```python
    prompt = "Add 2 to 20"

    # zeptat se LLM, jaké nástroje může použít, pokud vůbec nějaké
    functions_to_call = call_llm(prompt, functions)

    # zavolat navržené funkce
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Tak to byl poslední krok, v kódu výše:

    - Voláme MCP nástroj přes `call_tool` pomocí funkce, kterou LLM zvolilo na základě našeho promptu.
    - Vypisujeme výsledek volání nástroje na MCP server.

#### .NET

1. Ukážeme kód pro provedení požadavku LLM promptu:

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

    - Načetli nástroje z MCP serveru, `var tools = await GetMcpTools()`.
    - Definovali uživatelský prompt `userMessage`.
    - Vytvořili objekt možností specifikující model a nástroje.
    - Provedli požadavek směrem k LLM.

2. Poslední krok, podíváme se, jestli LLM navrhuje zavolat nějakou funkci:

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
    - Pro každé volání nástroje jsme rozebrali jméno a argumenty a zavolali nástroj na MCP serveru přes MCP klienta. Nakonec výsledky vypsali.

Zde je kompletní kód:

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
    // Proveďte požadavky v přirozeném jazyce, které automaticky používají nástroje MCP
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

- Použili jednoduché prompty v přirozeném jazyce pro interakci s nástroji MCP serveru
- Framework LangChain4j automaticky zpracovává:
  - Převod uživatelských promptů na volání nástrojů, pokud je to potřeba
  - Volání příslušných MCP nástrojů na základě rozhodnutí LLM
  - Řízení toku konverzace mezi LLM a MCP serverem
- Metoda `bot.chat()` vrací odpovědi v přirozeném jazyce, které mohou obsahovat výsledky z vykonání nástrojů MCP
- Tento přístup poskytuje plynulý uživatelský zážitek, kde uživatelé nemusí znát podkladovou implementaci MCP

Kompletní příklad kódu:

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

Zde se odehrává většina práce. Zavoláme LLM s počátečním uživatelským promptem, potom zpracujeme odpověď, abychom zjistili, zda je potřeba nějaké nástroje volat. Pokud ano, zavoláme tyto nástroje a pokračujeme v konverzaci s LLM, dokud nebudou všechny potřebné volání nástrojů dokončeny a máme finální odpověď.


Budeme volat LLM několikrát, proto si definujeme funkci, která bude volání LLM zpracovávat. Přidejte následující funkci do svého souboru `main.rs`:

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

Tato funkce přijímá klienta LLM, seznam zpráv (včetně uživatelského promptu), nástroje ze serveru MCP a odešle požadavek na LLM, přičemž vrátí odpověď.

Odpověď z LLM bude obsahovat pole `choices`. Budeme muset zpracovat výsledek, abychom zjistili, zda jsou přítomny nějaké `tool_calls`. To nám umožní poznat, že LLM vyžaduje vyvolání konkrétního nástroje s argumenty. Přidejte následující kód na konec souboru `main.rs` pro definici funkce, která zpracuje odpověď LLM:

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

    // Tisknout obsah, pokud je k dispozici
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Zpracovat volání nástroje
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

Pokud jsou přítomny `tool_calls`, extrahuje informace o nástroji, zavolá server MCP s požadavkem nástroje a přidá výsledky do zpráv konverzace. Následně pokračuje v konverzaci s LLM a zprávy jsou aktualizovány odpovědí asistenta a výsledky volání nástroje.

Pro extrakci informací o volání nástrojů, které LLM vrací pro volání MCP, přidáme další pomocnou funkci, která vytáhne vše potřebné pro provedení volání. Přidejte následující kód na konec souboru `main.rs`:

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

S veškerými částmi na místě nyní můžeme zpracovat počáteční uživatelský prompt a zavolat LLM. Aktualizujte svou funkci `main`, aby obsahovala následující kód:

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

Toto provede dotazování LLM s počátečním uživatelským promptem požadujícím součet dvou čísel a zpracuje odpověď tak, aby dynamicky zvládala volání nástrojů.

Skvělé, podařilo se vám to!

## Zadání

Vezměte kód z cvičení a rozšiřte server o několik dalších nástrojů. Poté vytvořte klienta s LLM, jako v cvičení, a otestujte ho s různými promptami, abyste se ujistili, že všechny nástroje vašeho serveru jsou volány dynamicky. Tento způsob vytváření klienta znamená, že koncový uživatel bude mít skvělý uživatelský zážitek, protože může používat prompta místo přesných příkazů klienta a nebude si uvědomovat, že je volán nějaký MCP server.

## Řešení

[Řešení](./solution/README.md)

## Hlavní poznatky

- Přidání LLM do klienta poskytuje lepší způsob, jak uživatelé mohou interagovat se servery MCP.
- Je potřeba převést odpověď serveru MCP na něco, čemu LLM rozumí.

## Ukázky

- [Java Kalkulačka](../samples/java/calculator/README.md)
- [.Net Kalkulačka](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulačka](../samples/javascript/README.md)
- [TypeScript Kalkulačka](../samples/typescript/README.md)
- [Python Kalkulačka](../../../../03-GettingStarted/samples/python)
- [Rust Kalkulačka](../../../../03-GettingStarted/samples/rust)

## Další zdroje

## Co dál

- Dále: [Používání serveru ve Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->