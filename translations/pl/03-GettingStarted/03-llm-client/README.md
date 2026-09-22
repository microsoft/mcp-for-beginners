# Tworzenie klienta z LLM

> [!NOTE]
> Przykłady klienta Java łączą się przez tradycyjny transport HTTP+SSE i
> wykorzystują API SDK MCP `2025-11-25`. Używaj SDK kompatybilnego z `2026-07-28` oraz
> Streamable HTTP dla nowych zdalnych klientów.

Do tej pory widziałeś, jak utworzyć serwer i klienta. Klient mógł wywoływać serwer eksplicytnie, aby wylistować jego narzędzia, zasoby i prompt'y. Jednak nie jest to bardzo praktyczne podejście. Twoi użytkownicy żyją w erze agentów i oczekują używania promptów oraz komunikacji z LLM. Nie interesuje ich, czy do przechowywania możliwości używasz MCP; po prostu oczekują interakcji za pomocą języka naturalnego. Jak więc rozwiązać ten problem? Rozwiązaniem jest dodanie LLM do klienta.

## Przegląd

W tej lekcji skupimy się na dodaniu LLM do klienta i pokażemy, jak to zapewnia znacznie lepsze doświadczenie użytkownika.

## Cele nauki

Po zakończeniu tej lekcji będziesz w stanie:

- Utworzyć klienta z LLM.
- Bezproblemowo komunikować się z serwerem MCP używając LLM.
- Zapewnić lepsze doświadczenie końcowemu użytkownikowi po stronie klienta.

## Podejście

Spróbujmy zrozumieć podejście, które musimy przyjąć. Dodanie LLM wydaje się proste, ale czy faktycznie tak zrobimy?

Oto jak klient będzie współdziałać z serwerem:

1. Nawiązać połączenie z serwerem.

1. Wylistować możliwości, prompt'y, zasoby i narzędzia oraz zapisać ich schemat.

1. Dodać LLM i przekazać zapisane możliwości oraz ich schemat w formacie, który LLM rozumie.

1. Obsłużyć prompt użytkownika, przekazując go do LLM wraz z narzędziami wylistowanymi przez klienta.

Świetnie, teraz gdy rozumiemy jak to zrobić na wysokim poziomie, spróbujmy tego w poniższym ćwiczeniu.

## Ćwiczenie: Tworzenie klienta z LLM

W tym ćwiczeniu nauczymy się dodawać LLM do naszego klienta.

### Uwierzytelnianie za pomocą Personal Access Token GitHub

Utworzenie tokena GitHub to prosty proces. Oto jak to zrobić:

- Przejdź do ustawień GitHub – Kliknij na swój zdjęcie profilowe w prawym górnym rogu i wybierz Ustawienia.
- Przejdź do Ustawień deweloperskich – Przewiń w dół i kliknij Ustawienia deweloperskie.
- Wybierz Personal Access Tokens – Kliknij na Tokeny o szczegółowych uprawnieniach, a następnie Wygeneruj nowy token.
- Skonfiguruj swój token – Dodaj notatkę dla odniesienia, ustaw datę wygaśnięcia i wybierz niezbędne zakresy (uprawnienia). W tym przypadku pamiętaj, aby dodać uprawnienie Models.
- Wygeneruj i skopiuj token – Kliknij Wygeneruj token i upewnij się, że skopiujesz go od razu, ponieważ nie będziesz mógł go ponownie zobaczyć.

### -1- Połącz się z serwerem

Najpierw utwórzmy naszego klienta:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importuj zod do walidacji schematu

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

W powyższym kodzie:

- Zaimportowaliśmy potrzebne biblioteki
- Utworzyliśmy klasę z dwoma członkami, `client` i `openai`, które pomogą nam zarządzać klientem i interakcją z LLM odpowiednio.
- Skonfigurowaliśmy instancję LLM, aby korzystała z GitHub Models, ustawiając `baseUrl` na API inferencji.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Utwórz parametry serwera dla połączenia stdio
server_params = StdioServerParameters(
    command="mcp",  # Wykonywalny plik
    args=["run", "server.py"],  # Opcjonalne argumenty wiersza poleceń
    env=None,  # Opcjonalne zmienne środowiskowe
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Zainicjuj połączenie
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

W powyższym kodzie:

- Zaimportowaliśmy potrzebne biblioteki dla MCP
- Utworzyliśmy klienta

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

Najpierw musisz dodać zależności LangChain4j do swojego pliku `pom.xml`. Dodaj te zależności, aby umożliwić integrację MCP oraz API kompatybilne z OpenAI MiniMax:

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

Ustaw swój klucz API MiniMax oraz opcjonalnie punkt końcowy i model.
`MINIMAX_MODEL_ID` obsługuje `MiniMax-M3` i `MiniMax-M2.7`. Jeśli
`OPENAI_BASE_URL` nie jest ustawiony, `MINIMAX_REGION` obsługuje `global_en` i `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Aby wybrać punkt końcowy według regionu, pomiń `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Następnie utwórz swoją klasę klienta Java:

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

        // Utwórz transport MCP do łączenia z serwerem
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Utwórz klienta MCP
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

W powyższym kodzie:

- **Dodano zależności LangChain4j**: Wymagane dla integracji MCP oraz API kompatybilnego z OpenAI MiniMax
- **Zaimportowano biblioteki LangChain4j**: Do integracji MCP oraz funkcji modelu czatu OpenAI
- **Utworzono `ChatLanguageModel`**: Skonfigurowane do korzystania z MiniMax z twoim kluczem API MiniMax, punktem końcowym i obsługiwanym modelem
- **Skonfigurowano transport HTTP**: Używając Server-Sent Events (SSE) do połączenia z serwerem MCP
- **Utworzono klienta MCP**: Który obsłuży komunikację z serwerem
- **Użyto wbudowanej obsługi MCP w LangChain4j**: Co upraszcza integrację między LLM i serwerami MCP

#### Rust

Ten przykład zakłada, że masz uruchomiony serwer MCP oparty na Rust. Jeśli go nie masz, wróć do lekcji [01-first-server](../01-first-server/README.md), aby utworzyć serwer.

Gdy masz już serwer MCP w Rust, otwórz terminal i przejdź do tego samego katalogu, co serwer. Następnie uruchom poniższe polecenie, aby utworzyć nowy projekt klienta LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Dodaj następujące zależności do pliku `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Nie ma oficjalnej biblioteki Rust dla OpenAI, jednak `async-openai` to [biblioteka utrzymywana przez społeczność](https://platform.openai.com/docs/libraries/rust#rust), która jest powszechnie używana.

Otwórz plik `src/main.rs` i zamień jego zawartość na poniższy kod:

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
    // Wiadomość początkowa
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Konfiguracja klienta OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Konfiguracja klienta MCP
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

    // DO ZROBIENIA: Pobierz listę narzędzi MCP

    // DO ZROBIENIA: Konwersacja LLM z wywołaniami narzędzi

    Ok(())
}
```

Ten kod ustawia podstawową aplikację w Rust, która łączy się z serwerem MCP oraz GitHub Models do interakcji LLM.

> [!IMPORTANT]
> Upewnij się, że ustawiłeś zmienną środowiskową `OPENAI_API_KEY` na swój token GitHub przed uruchomieniem aplikacji.

Świetnie, kolejnym krokiem wylistujmy możliwości serwera.

### -2- Wylistuj możliwości serwera

Teraz połączymy się z serwerem i zapytamy o jego możliwości:

#### TypeScript

W tej samej klasie dodaj następujące metody:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // narzędzia do wyświetlania listy
    const toolsResult = await this.client.listTools();
}
```

W powyższym kodzie:

- Dodano kod do połączenia z serwerem, `connectToServer`.
- Utworzono metodę `run`, która odpowiada za obsługę przepływu aplikacji. Na razie tylko wylistowuje narzędzia, ale niebawem dodamy więcej funkcji.

#### Python

```python
# Wyświetl dostępne zasoby
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Wyświetl dostępne narzędzia
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Oto co dodaliśmy:

- Wylistowaliśmy zasoby i narzędzia oraz je wyświetliliśmy. Dla narzędzi wylistowaliśmy także `inputSchema`, którego użyjemy później.

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

W powyższym kodzie:

- Wylistowano dostępne narzędzia na serwerze MCP
- Dla każdego narzędzia wylistowano nazwę, opis oraz jego schemat. Ten ostatni wykorzystamy do wywołań narzędzi niedługo.

#### Java

```java
// Utwórz dostawcę narzędzi, który automatycznie wykrywa narzędzia MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Dostawca narzędzi MCP automatycznie obsługuje:
// - Wypisywanie dostępnych narzędzi z serwera MCP
// - Konwersję schematów narzędzi MCP do formatu LangChain4j
// - Zarządzanie wykonaniem narzędzi i odpowiedziami
```

W powyższym kodzie:

- Utworzono `McpToolProvider`, który automatycznie wykrywa i rejestruje wszystkie narzędzia z serwera MCP
- Provider narzędzi obsługuje konwersję między schematami narzędzi MCP a formatem narzędzi LangChain4j wewnętrznie
- To podejście abstrahuje ręczne listowanie i konwersję narzędzi

#### Rust

Pobieranie narzędzi z serwera MCP odbywa się metodą `list_tools`. W funkcji `main`, po skonfigurowaniu klienta MCP, dodaj następujący kod:

```rust
// Pobierz listę narzędzi MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Konwersja możliwości serwera na narzędzia LLM

Kolejnym krokiem po wylistowaniu możliwości serwera jest przekształcenie ich do formatu rozumianego przez LLM. Gdy to zrobimy, możemy dostarczyć te możliwości jako narzędzia do naszego LLM.

#### TypeScript

1. Dodaj następujący kod, aby konwertować odpowiedź z serwera MCP do formatu narzędziowego, którego LLM może użyć:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Utwórz schemat zod na podstawie input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Wyraźnie ustaw typ na "function"
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

    Powyższy kod bierze odpowiedź z serwera MCP i konwertuje ją na definicję narzędzia w formacie zrozumiałym dla LLM.

2. Teraz zaktualizuj metodę `run`, aby wylistować możliwości serwera:

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

    W powyższym kodzie zaktualizowaliśmy metodę `run`, aby mapować wyniki i dla każdego wpisu wywołać `openAiToolAdapter`.

#### Python

1. Najpierw utwórz następującą funkcję konwertującą

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

    W powyższej funkcji `convert_to_llm_tools` bierzemy odpowiedź narzędzia MCP i konwertujemy ją do formatu, który LLM może zrozumieć.

2. Następnie zaktualizuj kod klienta, aby wykorzystać tę funkcję w ten sposób:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Tutaj dodajemy wywołanie `convert_to_llm_tool`, aby przetransformować odpowiedź narzędzia MCP na coś, co później przekażemy LLM.

#### .NET

1. Dodajmy kod konwertujący odpowiedź narzędzia MCP na coś, co LLM może zrozumieć

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

W powyższym kodzie:

- Utworzono funkcję `ConvertFrom`, która przyjmuje nazwę, opis i schemat wejściowy.
- Zdefiniowano funkcjonalność tworzącą `FunctionDefinition`, która jest przekazywana do `ChatCompletionsDefinition`. To ostatnie jest formatem, który LLM rozumie.

2. Zobaczmy, jak możemy zaktualizować istniejący kod, aby wykorzystać powyższą funkcję:

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
// Utwórz interfejs Bota do interakcji w języku naturalnym
public interface Bot {
    String chat(String prompt);
}

// Skonfiguruj usługę AI z narzędziami LLM i MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

W powyższym kodzie:

- Zdefiniowano prosty interfejs `Bot` do interakcji w języku naturalnym
- Użyto `AiServices` z LangChain4j do automatycznego powiązania LLM z dostawcą narzędzi MCP
- Framework automatycznie obsługuje konwersję schematów narzędzi i wywołania funkcji w tle
- To podejście eliminuje ręczną konwersję narzędzi - LangChain4j zajmuje się całym złożonym procesem konwersji narzędzi MCP na format kompatybilny z LLM

#### Rust

Aby przekształcić odpowiedź narzędzia MCP do formatu zrozumiałego przez LLM, dodamy funkcję pomocniczą, która sformatuje listę narzędzi. Dodaj następujący kod do pliku `main.rs` poniżej funkcji `main`. Będzie on wywoływany podczas żądań do LLM:

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

Świetnie, jesteśmy gotowi obsługiwać zapytania użytkownika, więc zajmijmy się tym teraz.

### -4- Obsługa zapytań użytkownika

W tej części kodu będziemy obsługiwać zapytania użytkownika.

#### TypeScript

1. Dodaj metodę, która będzie używana do wywoływania naszego LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Wywołaj narzędzie serwera
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Zrób coś z wynikiem
        // DO ZROBIENIA

        }
    }
    ```

    W powyższym kodzie:

    - Dodano metodę `callTools`.
    - Metoda przyjmuje odpowiedź LLM i sprawdza, które narzędzia zostały wywołane, jeśli w ogóle:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // wywołaj narzędzie
        }
        ```

    - Wywołuje narzędzie, jeśli LLM wskazało, że powinno być wywołane:

        ```typescript
        // 2. Wywołaj narzędzie serwera
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Zrób coś z wynikiem
        // DO ZROBIENIA
        ```

2. Zaktualizuj metodę `run`, aby zawierała wywołania LLM i `callTools`:

    ```typescript

    // 1. Utwórz wiadomości będące wejściem dla LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Wywołanie LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Przejdź przez odpowiedź LLM, dla każdej opcji sprawdź, czy zawiera wywołania narzędzi
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Świetnie, pokażmy cały kod razem:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importuj zod do walidacji schematu

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // może trzeba będzie w przyszłości zmienić na ten adres URL: https://models.github.ai/inference
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
          // Utwórz schemat zod na podstawie input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Wyraźnie ustaw typ na "function"
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
    
    
          // 2. Wywołaj narzędzie serwera
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Zrób coś z wynikiem
          // DO ZROBIENIA
    
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
    
        // 3. Przejdź przez odpowiedź LLM, dla każdej opcji sprawdź, czy zawiera wywołania narzędzi
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

1. Dodajmy potrzebne importy do wywoływania LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Następnie dodajmy funkcję, która wykona wywołanie LLM:

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
            # Parametry opcjonalne
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

    W powyższym kodzie:

    - Przekazaliśmy funkcje, które znaleźliśmy na serwerze MCP i przekształciliśmy, do LLM.
    - Następnie wywołaliśmy LLM z tymi funkcjami.
    - Sprawdzamy wynik, aby zobaczyć, które funkcje powinniśmy wywołać, jeśli są jakieś.
    - Ostatecznie przekazujemy tablicę funkcji do wywołania.

3. Ostatni krok, zaktualizujmy nasz główny kod:

    ```python
    prompt = "Add 2 to 20"

    # zapytaj LLM, jakie narzędzia, jeśli w ogóle, są dostępne
    functions_to_call = call_llm(prompt, functions)

    # wywołaj zasugerowane funkcje
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    To był ostatni krok, w powyższym kodzie:

    - Wywołujemy narzędzie MCP przez `call_tool` korzystając z funkcji, której LLM uznało, że powinno zostać wywołane na podstawie promptu.
    - Wypisujemy wynik wywołania narzędzia na serwer MCP.

#### .NET

1. Oto kod do wykonania żądania promptu LLM:

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

    W powyższym kodzie:

    - Pobieramy narzędzia z serwera MCP, `var tools = await GetMcpTools()`.
    - Definiujemy prompt użytkownika w `userMessage`.
    - Tworzymy obiekt opcji określający model i narzędzia.
    - Wysyłamy żądanie do LLM.

2. Ostatni krok, sprawdźmy, czy LLM sądzi, że powinniśmy wywołać funkcję:

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

    W powyższym kodzie:

    - Iterujemy po liście wywołań funkcji.
    - Dla każdego wywołania narzędzia parsujemy nazwę i argumenty oraz wywołujemy na serwerze MCP używając klienta MCP. Na końcu wypisujemy wyniki.

Oto pełny kod:

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
    // Wykonaj zapytania w naturalnym języku, które automatycznie korzystają z narzędzi MCP
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

W powyższym kodzie:

- Używamy prostych promptów w języku naturalnym do interakcji z narzędziami serwera MCP
- Framework LangChain4j automatycznie obsługuje:
  - Konwersję promptów użytkownika na wywołania narzędzi w razie potrzeby
  - Wywoływanie odpowiednich narzędzi MCP na podstawie decyzji LLM
  - Zarządzanie przepływem rozmowy pomiędzy LLM a serwerem MCP
- Metoda `bot.chat()` zwraca odpowiedzi w języku naturalnym, które mogą zawierać wyniki wywołań narzędzi MCP
- To podejście zapewnia płynne doświadczenie użytkownika, gdzie użytkownicy nie muszą znać szczegółów implementacji MCP

Kompletny przykładowy kod:

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


Tutaj odbywa się większość pracy. Wywołamy LLM z początkowym zapytaniem użytkownika, a następnie przetworzymy odpowiedź, aby sprawdzić, czy trzeba wywołać jakieś narzędzia. Jeśli tak, wywołamy te narzędzia i będziemy kontynuować rozmowę z LLM, aż nie będą już potrzebne kolejne wywołania narzędzi i otrzymamy ostateczną odpowiedź.

Będziemy wykonywać wiele wywołań do LLM, więc zdefiniujmy funkcję, która będzie obsługiwać wywołania LLM. Dodaj następującą funkcję do swojego pliku `main.rs`:

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

Ta funkcja przyjmuje klienta LLM, listę wiadomości (w tym zapytanie użytkownika), narzędzia z serwera MCP i wysyła zapytanie do LLM, zwracając odpowiedź.

Odpowiedź z LLM będzie zawierać tablicę `choices`. Musimy przetworzyć wynik, aby sprawdzić, czy występują jakieś `tool_calls`. To daje nam znać, że LLM żąda wywołania konkretnego narzędzia z argumentami. Dodaj następujący kod na dole swojego pliku `main.rs`, aby zdefiniować funkcję obsługującą odpowiedź LLM:

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

    // Wydrukuj zawartość, jeśli dostępna
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Obsłuż wywołania narzędzi
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Dodaj wiadomość asystenta

        // Wykonaj każde wywołanie narzędzia
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Dodaj wynik narzędzia do wiadomości
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Kontynuuj rozmowę z wynikami narzędzi
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

Jeśli `tool_calls` są obecne, funkcja wyodrębnia informacje o narzędziu, wywołuje serwer MCP z żądaniem narzędzia i dodaje wyniki do wiadomości rozmowy. Następnie kontynuuje rozmowę z LLM, a wiadomości są aktualizowane o odpowiedź asystenta oraz wyniki wywołania narzędzia.

Aby wyodrębnić informacje o wywołaniu narzędzia, które LLM zwraca do wywołań MCP, dodamy kolejną funkcję pomocniczą, która wyciągnie wszystko, co potrzebne do wykonania wywołania. Dodaj następujący kod na dole swojego pliku `main.rs`:

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

Gdy wszystkie elementy są gotowe, możemy teraz obsłużyć początkowe zapytanie użytkownika i wywołać LLM. Zaktualizuj swoją funkcję `main`, aby zawierała następujący kod:

```rust
// Rozmowa LLM z wywołaniami narzędzi
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

To zapyta LLM o sumę dwóch liczb i przetworzy odpowiedź, aby dynamicznie obsługiwać wywołania narzędzi.

Świetnie, udało się!

## Zadanie

Weź kod z ćwiczenia i rozbuduj serwer o więcej narzędzi. Następnie stwórz klienta z LLM, jak w ćwiczeniu, i przetestuj go różnymi zapytaniami, aby upewnić się, że wszystkie narzędzia serwera są wywoływane dynamicznie. Takie budowanie klienta zapewnia użytkownikowi końcowemu świetne doświadczenie, gdyż może korzystać z zapytań, zamiast dokładnych poleceń klienta, i nie zdaje sobie sprawy z wywoływanego serwera MCP.

## Rozwiązanie

[Rozwiązanie](./solution/README.md)

## Kluczowe wnioski

- Dodanie LLM do klienta zapewnia lepszy sposób interakcji użytkowników z serwerami MCP.
- Musisz przekształcić odpowiedź serwera MCP do formy zrozumiałej dla LLM.

## Przykłady

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Dodatkowe zasoby

## Co dalej

- Dalej: [Korzystanie z serwera za pomocą Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->