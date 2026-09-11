# Een client maken met LLM

> [!NOTE]
> De Java clientvoorbeelden maken verbinding via de legacy HTTP+SSE transport en
> richten zich op MCP `2025-11-25` SDK API's. Gebruik een `2026-07-28`-compatibele SDK en
> Streamable HTTP voor nieuwe externe clients.

Tot nu toe heb je gezien hoe je een server en een client kunt maken. De client kon expliciet de server aanroepen om zijn tools, resources en prompts op te sommen. Dit is echter geen erg praktische aanpak. Je gebruikers leven in het agentische tijdperk en verwachten prompts te gebruiken en met een LLM te communiceren. Het maakt hen niet uit of je MCP gebruikt om je mogelijkheden op te slaan; ze verwachten simpelweg interactie in natuurlijke taal. Dus hoe lossen we dit op? De oplossing is om een LLM toe te voegen aan de client.

## Overzicht

In deze les richten we ons op het toevoegen van een LLM aan je client en laten we zien hoe dit een veel betere ervaring biedt voor je gebruiker.

## Leerdoelen

Aan het einde van deze les zul je in staat zijn om:

- Een client te maken met een LLM.
- Naadloos te communiceren met een MCP-server met behulp van een LLM.
- Een betere eindgebruikerservaring aan de clientzijde te bieden.

## Aanpak

Laten we proberen te begrijpen welke aanpak we moeten nemen. Een LLM toevoegen klinkt simpel, maar gaan we dit echt doen?

Zo zal de client met de server communiceren:

1. Verbinding maken met de server.

1. Mogelijkheden, prompts, resources en tools opsommen en het schema ervan opslaan.

1. Een LLM toevoegen en de opgeslagen mogelijkheden en hun schema doorgeven in een formaat dat de LLM begrijpt.

1. Een gebruikersprompt afhandelen door deze aan de LLM door te geven samen met de door de client opgesomde tools.

Geweldig, nu we begrijpen hoe we dit op hoofdlijnen kunnen doen, laten we dit proberen in de onderstaande oefening.

## Oefening: Een client maken met een LLM

In deze oefening leren we een LLM toe te voegen aan onze client.

### Authenticatie met GitHub Personal Access Token

Het maken van een GitHub-token is een eenvoudig proces. Zo doe je dat:

- Ga naar GitHub Instellingen – Klik op je profielfoto rechtsboven en selecteer Instellingen.
- Navigeer naar Developer Settings – Scroll naar beneden en klik op Developer Settings.
- Selecteer Personal Access Tokens – Klik op Fine-grained tokens en dan Generate new token.
- Configureer je token – Voeg een notitie toe ter referentie, stel een vervaldatum in en selecteer de benodigde scopes (machtigingen). Zorg er in dit geval voor dat je de Models-machtiging toevoegt.
- Genereer en kopieer het token – Klik op Generate token, en zorg dat je het direct kopieert, want je ziet het daarna niet meer terug.

### -1- Verbinden met de server

Laten we eerst onze client maken:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importeer zod voor schema-validatie

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

In bovenstaande code hebben we:

- De benodigde bibliotheken geïmporteerd
- Een klasse gemaakt met twee leden, `client` en `openai` die ons helpen een client te beheren en te communiceren met een LLM.
- Onze LLM-instantie geconfigureerd om GitHub Models te gebruiken door `baseUrl` in te stellen op de inferentie-API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Maak serverparameters voor stdio-verbinding
server_params = StdioServerParameters(
    command="mcp",  # Uitvoerbaar bestand
    args=["run", "server.py"],  # Optionele opdrachtregelargumenten
    env=None,  # Optionele omgevingsvariabelen
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialiseer de verbinding
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

In bovenstaande code hebben we:

- De benodigde bibliotheken voor MCP geïmporteerd
- Een client gemaakt

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

Eerst moet je de LangChain4j-afhankelijkheden toevoegen aan je `pom.xml` bestand. Voeg deze afhankelijkheden toe om MCP-integratie en de OpenAI-compatibele MiniMax API mogelijk te maken:

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

Stel je MiniMax API-sleutel en, optioneel, de endpoint en het model in.
`MINIMAX_MODEL_ID` ondersteunt `MiniMax-M3` en `MiniMax-M2.7`. Als
`OPENAI_BASE_URL` niet is ingesteld, ondersteunt `MINIMAX_REGION` `global_en` en `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Om de endpoint in te stellen op basis van regio, laat `OPENAI_BASE_URL` weg:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Maak daarna je Java clientklasse aan:

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

        // Maak MCP-transport aan voor verbinding met de server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Maak MCP-client aan
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

In bovenstaande code hebben we:

- **LangChain4j-afhankelijkheden toegevoegd**: Nodig voor MCP-integratie en de OpenAI-compatibele MiniMax API
- **De LangChain4j bibliotheken geïmporteerd**: Voor MCP-integratie en OpenAI chatmodel functionaliteit
- **Een `ChatLanguageModel` gemaakt**: Geconfigureerd om MiniMax te gebruiken met je MiniMax API-sleutel, endpoint en ondersteund model-ID
- **HTTP-transport opgezet**: Met Server-Sent Events (SSE) verbonden met de MCP-server
- **Een MCP-client gemaakt**: Die communicatie met de server afhandelt
- **LangChain4j's ingebouwde MCP-ondersteuning gebruikt**: Wat de integratie tussen LLMs en MCP-servers vereenvoudigt

#### Rust

Dit voorbeeld gaat ervan uit dat je een Rust-gebaseerde MCP-server hebt draaien. Als je die nog niet hebt, zie dan de [01-first-server](../01-first-server/README.md) les om de server te maken.

Zodra je je Rust MCP-server hebt, open je een terminal en navigeer je naar dezelfde map als de server. Voer dan de volgende opdracht uit om een nieuw LLM-clientproject te maken:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Voeg de volgende afhankelijkheden toe aan je `Cargo.toml` bestand:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Er is geen officiële Rust-bibliotheek voor OpenAI, maar de `async-openai` crate is een [gemeenschapsonderhouden bibliotheek](https://platform.openai.com/docs/libraries/rust#rust) die veel gebruikt wordt.

Open het `src/main.rs` bestand en vervang de inhoud door de volgende code:

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
    // Initieel bericht
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI-client instellen
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP-client instellen
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

    // TODO: Verkrijg MCP gereedschapslijst

    // TODO: LLM-gesprek met gereedschapsaanroepen

    Ok(())
}
```

Deze code zet een basis Rust-applicatie op die verbinding maakt met een MCP-server en GitHub Models voor LLM-interacties.

> [!IMPORTANT]
> Zorg dat je de `OPENAI_API_KEY` omgevingsvariabele instelt met je GitHub-token voordat je de applicatie uitvoert.

Geweldig, onze volgende stap is om de mogelijkheden op de server op te sommen.

### -2- Server mogelijkheden opsommen

Nu verbinden we met de server en vragen we om zijn mogelijkheden:

#### Typescript

Voeg in dezelfde klasse de volgende methodes toe:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // gereedschappen opsommen
    const toolsResult = await this.client.listTools();
}
```

In bovenstaande code hebben we:

- Code toegevoegd voor verbinding maken met de server, `connectToServer`.
- Een `run` methode gemaakt die verantwoordelijk is voor het afhandelen van de app-stroom. Tot nu toe somt deze alleen de tools op, maar we voegen er binnenkort meer aan toe.

#### Python

```python
# Lijst beschikbare bronnen
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Lijst beschikbare hulpmiddelen
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Dit hebben we toegevoegd:

- Resources en tools opgesomd en afgedrukt. Voor tools hebben we ook `inputSchema` opgesomd, wat we later gebruiken.

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

In bovenstaande code hebben we:

- De beschikbare tools op de MCP Server opgesomd
- Voor elke tool naam, beschrijving en schema opgesomd. Dit schema gebruiken we straks om de tools aan te roepen.

#### Java

```java
// Maak een toolprovider die automatisch MCP-tools ontdekt
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// De MCP-toolprovider handelt automatisch af:
// - Het weergeven van beschikbare tools van de MCP-server
// - Het converteren van MCP-toolschemas naar LangChain4j-formaat
// - Het beheren van tooluitvoering en -reacties
```

In bovenstaande code hebben we:

- Een `McpToolProvider` gemaakt die automatisch alle tools van de MCP-server ontdekt en registreert
- De tool provider verzorgt intern de conversie tussen MCP tool schema’s en het LangChain4j toolformaat
- Deze aanpak abstraheert het handmatig opsommen en conversie proces van tools

#### Rust

Tools van de MCP-server ophalen doe je met de `list_tools` methode. Voeg in je `main` functie na het opzetten van de MCP-client de volgende code toe:

```rust
// Haal MCP-gereedschapslijst op
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Server mogelijkheden omzetten naar LLM-tools

De volgende stap nadat de servermogelijkheden zijn opgesomd, is ze omzetten naar een formaat dat de LLM begrijpt. Zodra we dat doen, kunnen we deze mogelijkheden als tools aan onze LLM aanbieden.

#### TypeScript

1. Voeg de volgende code toe om de respons van de MCP Server om te zetten naar een toolformaat dat de LLM kan gebruiken:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Maak een zod-schema op basis van het input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Stel het type expliciet in op "functie"
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

    De bovenstaande code neemt een reactie van de MCP Server en converteert die naar een tooldefinitie in een formaat dat de LLM kan begrijpen.

2. Laten we de `run` methode bijwerken om servermogelijkheden op te sommen:

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

    In bovenstaande code hebben we de `run` methode aangepast om door het resultaat te lopen en voor elke invoer `openAiToolAdapter` aan te roepen.

#### Python

1. Laten we eerst de volgende converter functie maken

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

    In de functie hierboven `convert_to_llm_tools` nemen we een MCP-toolrespons en zetten die om in een formaat dat de LLM begrijpt.

2. Vervolgens passen we onze clientcode aan om van deze functie gebruik te maken:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Hier voegen we een aanroep toe naar `convert_to_llm_tool` om de MCP-toolrespons om te zetten naar iets wat we later aan de LLM kunnen geven.

#### .NET

1. Laten we code toevoegen om de MCP-toolrespons om te zetten naar iets wat de LLM kan begrijpen

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

In bovenstaande code hebben we:

- Een functie `ConvertFrom` gemaakt die naam, beschrijving en inputschema als parameters neemt.
- Functionaliteit gedefinieerd om een FunctionDefinition te maken, die wordt doorgegeven aan een ChatCompletionsDefinition. Dit laatste begrijpt de LLM.

2. Laten we zien hoe we bestaande code kunnen bijwerken om van deze functie gebruik te maken:

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
// Maak een Bot-interface voor natuurlijke taalinteractie
public interface Bot {
    String chat(String prompt);
}

// Configureer de AI-service met LLM- en MCP-tools
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

In bovenstaande code hebben we:

- Een eenvoudige `Bot` interface gedefinieerd voor natuurlijke taalinteracties
- LangChain4j's `AiServices` gebruikt om automatisch de LLM te koppelen met de MCP toolprovider
- Het framework handelt automatisch tool schema conversie en functie-aanroepen achter de schermen af
- Deze aanpak elimineert handmatige toolconversie - LangChain4j regelt alle complexiteit van het omzetten van MCP-tools naar LLM-compatibel formaat

#### Rust

Om de MCP-toolrespons om te zetten naar een formaat dat de LLM kan begrijpen, zullen we een hulpfunctie toevoegen die de toolopgave formatteert. Voeg de volgende code toe aan je `main.rs` bestand onder de `main` functie. Dit wordt aangeroepen bij LLM-verzoeken:

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

Geweldig, we zijn klaar om gebruikersverzoeken te verwerken, laten we dat nu aanpakken.

### -4- Gebruikersprompt verzoek afhandelen

In dit deel van de code zullen we gebruikersverzoeken afhandelen.

#### TypeScript

1. Voeg een methode toe die onze LLM zal aanroepen:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Roep het gereedschap van de server aan
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Doe iets met het resultaat
        // TODO

        }
    }
    ```

    In bovenstaande code hebben we:

    - Een methode `callTools` toegevoegd.
    - De methode neemt een LLM-respons en controleert welke tools er zijn aangeroepen, als die er zijn:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // hulpmiddel aanroepen
        }
        ```

    - Roept een tool aan als de LLM aangeeft dat die moet worden aangeroepen:

        ```typescript
        // 2. Roep de tool van de server aan
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Doe iets met het resultaat
        // NOG TE DOEN
        ```

2. Werk de `run` methode bij om aanroepen naar de LLM en `callTools` te bevatten:

    ```typescript

    // 1. Maak berichten die input zijn voor de LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Het aanroepen van de LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Doorloop de LLM-respons, voor elke keuze, controleer of er tool-oproepen zijn
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Geweldig, hier volgt de volledige code:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importeer zod voor schema validatie

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // Mogelijk in de toekomst overstappen naar deze url: https://models.github.ai/inference
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
          // Maak een zod schema gebaseerd op het input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Stel expliciet het type in op "function"
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
    
    
          // 2. Roep de tool van de server aan
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Doe iets met het resultaat
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
    
        // 3. Doorloop de LLM-respons, controleer bij elke keuze of er tool-aanroepen zijn
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

1. Laten we enkele import statements toevoegen die nodig zijn om een LLM aan te roepen

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Vervolgens voegen we de functie toe die de LLM aanroept:

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
            # Optionele parameters
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

    In bovenstaande code hebben we:

    - Onze functies, gevonden op de MCP server en geconverteerd, aan de LLM doorgegeven.
    - Daarna de LLM opgeroepen met die functies.
    - Vervolgens het resultaat geïnspecteerd om te zien welke functies we moeten aanroepen, indien van toepassing.
    - Tenslotte een array van functies doorgegeven om aan te roepen.

3. Laatste stap, laten we onze hoofdcode bijwerken:

    ```python
    prompt = "Add 2 to 20"

    # vraag aan LLM welke tools er zijn, indien aanwezig
    functions_to_call = call_llm(prompt, functions)

    # roep voorgestelde functies aan
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Dat was de laatste stap, in bovenstaande code zijn we:

    - Een MCP-tool aan het aanroepen via `call_tool` met een functie waarvan de LLM dacht dat we die moesten aanroepen op basis van onze prompt.
    - Het resultaat van de toolaanroep naar de MCP Server aan het afdrukken.

#### .NET

1. Hier is wat code om een LLM promptverzoek te doen:

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

    In bovenstaande code hebben we:

    - Tools opgehaald van de MCP server, `var tools = await GetMcpTools()`.
    - Een gebruikersprompt gedefinieerd `userMessage`.
    - Een opties-object gemaakt dat model en tools specificeert.
    - Een verzoek gedaan naar de LLM.

2. Eén laatste stap, laten we kijken of de LLM vindt dat we een functie moeten aanroepen:

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

    In bovenstaande code hebben we:

    - Door een lijst van functie-aanroepen geloopt.
    - Voor elke tool-aanroep naam en argumenten uitgehaald en de tool op de MCP server aangeroepen met de MCP client. Uiteindelijk de resultaten afgedrukt.

Hier is de code in zijn geheel:

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
    // Voer natuurlijke taalverzoeken uit die automatisch MCP-hulpmiddelen gebruiken
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

In bovenstaande code hebben we:

- Eenvoudige natuurlijke taal prompts gebruikt om te communiceren met MCP server tools
- Het LangChain4j framework handelt automatisch:
  - Het omzetten van gebruikersprompts naar toolaanroepen waar nodig
  - Het aanroepen van de juiste MCP-tools gebaseerd op de beslissing van de LLM
  - Het beheren van het gesprek tussen de LLM en de MCP-server
- De `bot.chat()` methode retourneert reacties in natuurlijke taal die ook resultaten van MCP tool-uitvoeringen kunnen bevatten
- Deze aanpak biedt een naadloze gebruikerservaring waarbij gebruikers niet hoeven te weten van de onderliggende MCP-implementatie

Volledige codevoorbeeld:

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


Hier vindt het grootste deel van het werk plaats. We zullen de LLM aanroepen met de initiële gebruikersprompt, en vervolgens de reactie verwerken om te zien of er tools aangeroepen moeten worden. Zo ja, dan roepen we die tools aan en zetten het gesprek met de LLM voort totdat er geen tool-aanroepen meer nodig zijn en we een definitieve reactie hebben.

We zullen meerdere oproepen naar de LLM doen, dus laten we een functie definiëren die de LLM-aanroep afhandelt. Voeg de volgende functie toe aan je `main.rs` bestand:

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

Deze functie neemt de LLM-client, een lijst met berichten (inclusief de gebruikersprompt), tools van de MCP-server, en verstuurt een verzoek naar de LLM, en retourneert de reactie.

De reactie van de LLM zal een array van `choices` bevatten. We moeten het resultaat verwerken om te zien of er `tool_calls` aanwezig zijn. Dit laat ons weten dat de LLM vraagt om een specifieke tool aan te roepen met argumenten. Voeg de volgende code toe onder in je `main.rs` bestand om een functie te definiëren die de LLM-reactie afhandelt:

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

    // Inhoud afdrukken indien beschikbaar
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Verwerk toolaanroepen
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Assistentbericht toevoegen

        // Voer elke toolaanroep uit
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Voeg toolresultaat toe aan berichten
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Vervolg gesprek met toolresultaten
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

Als er `tool_calls` aanwezig zijn, haalt het de toolinformatie eruit, roept de MCP-server aan met het toolverzoek, en voegt de resultaten toe aan de conversatieberichten. Vervolgens zet het het gesprek met de LLM voort en worden de berichten bijgewerkt met de reactie van de assistent en de resultaten van de toolaanroep.

Om de toolaanroepinformatie die de LLM teruggeeft voor MCP-aanroepen te extraheren, voegen we een extra hulpfunctie toe om alles te halen wat nodig is om de oproep te doen. Voeg de volgende code toe onder in je `main.rs` bestand:

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

Met alle onderdelen op hun plaats kunnen we nu de initiële gebruikersprompt afhandelen en de LLM aanroepen. Werk je `main` functie bij met de volgende code:

```rust
// LLM-gesprek met gereedschapsoproepen
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

Dit zal de LLM bevragen met de initiële gebruikersprompt waarin gevraagd wordt om de som van twee getallen, en zal de reactie verwerken om dynamisch tool-aanroepen af te handelen.

Geweldig, je hebt het gedaan!

## Opdracht

Gebruik de code van de oefening en bouw de server uit met wat meer tools. Maak daarna een client met een LLM, zoals in de oefening, en test het met verschillende prompts om er zeker van te zijn dat alle servertools dynamisch worden aangeroepen. Deze manier van het bouwen van een client betekent dat de eindgebruiker een geweldige gebruikerservaring heeft omdat zij prompts kunnen gebruiken in plaats van exacte clientcommando's, en zich niet bewust hoeven te zijn van een MCP-server die wordt aangeroepen.

## Oplossing

[Oplossing](./solution/README.md)

## Belangrijke Leerpunten

- Het toevoegen van een LLM aan je client biedt een betere manier voor gebruikers om te communiceren met MCP-servers.
- Je moet de reactie van de MCP-server omzetten naar iets dat de LLM kan begrijpen.

## Voorbeelden

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Extra Bronnen

## Wat Nu

- Volgende: [Gebruik maken van een server met Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->