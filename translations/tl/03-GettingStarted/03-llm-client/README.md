# Paglikha ng isang kliyente gamit ang LLM

> [!NOTE]
> Ang mga halimbawa ng Java client ay kumokonekta sa pamamagitan ng legacy HTTP+SSE transport at
> tumutukoy sa MCP `2025-11-25` SDK APIs. Gumamit ng `2026-07-28`-compatible SDK at
> Streamable HTTP para sa mga bagong remote client.

Sa ngayon, nakita mo na kung paano gumawa ng isang server at isang kliyente. Ang kliyente ay nakakagawa ng tawag sa server nang tahasan upang ilista ang mga tool, resources, at mga prompt nito. Gayunpaman, ito ay hindi isang napaka-praktikal na pamamaraan. Ang iyong mga gumagamit ay nabubuhay sa agentic na panahon at inaasahan na gagamit ng mga prompt at makipag-usap gamit ang isang LLM. Hindi nila iniintindi kung gumagamit ka ng MCP para i-imbak ang iyong mga kakayahan; inaasahan lang nila na makipag-ugnayan gamit ang natural na wika. Paano natin ito sosolusyonan? Ang solusyon ay magdagdag ng LLM sa kliyente.

## Pangkalahatang-ideya

Sa araling ito, tututok tayo sa pagdaragdag ng isang LLM sa iyong kliyente at ipapakita kung paano ito nagbibigay ng mas magandang karanasan para sa iyong mga gumagamit.

## Mga Layunin ng Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Gumawa ng kliyente na may LLM.
- Makipag-ugnayan nang tuloy-tuloy sa isang MCP server gamit ang isang LLM.
- Magbigay ng mas mahusay na karanasan sa end user sa kliyente.

## Paraan

Subukan nating unawain ang paraan na dapat nating gawin. Ang pagdaragdag ng isang LLM ay tila simple, ngunit gagawin ba talaga natin ito?

Ganito ang pakikipag-ugnayan ng kliyente sa server:

1. Magtatag ng koneksyon sa server.

1. Ilista ang mga kakayahan, mga prompt, mga resources at mga tool, at i-save ang kanilang schema.

1. Magdagdag ng isang LLM at ipasa ang na-save na mga kakayahan at ang kanilang schema sa format na nauunawaan ng LLM.

1. Pangalagaan ang prompt ng gumagamit sa pamamagitan ng pagpapasa nito sa LLM kasama ang mga tool na inilista ng kliyente.

Mahusay, ngayon nauunawaan natin kung paano natin ito magagawa sa mataas na lebel, subukan natin ito sa ibaba na ehersisyo.

## Ehersisyo: Paglikha ng kliyente na may LLM

Sa ehersisyong ito, matututo tayo magdagdag ng LLM sa ating kliyente.

### Pagpapatunay gamit ang GitHub Personal Access Token

Ang paglikha ng GitHub token ay isang madaliang proseso. Ganito ang paraan:

- Pumunta sa GitHub Settings – I-click ang iyong profile picture sa kanang itaas na bahagi at piliin ang Settings.
- Mag-navigate sa Developer Settings – Mag-scroll pababa at i-click ang Developer Settings.
- Piliin ang Personal Access Tokens – I-click ang Fine-grained tokens at pagkatapos ay Generate new token.
- Isaayos ang Iyong Token – Magdagdag ng tala para sa reference, magtakda ng petsa ng pag-expire, at piliin ang kinakailangang scopes (pahintulot). Sa pagkakataong ito siguraduhing idagdag ang Models permission.
- Gumawa at Kopyahin ang Token – I-click ang Generate token, at siguraduhing kopyahin ito agad dahil hindi mo na ito makikita muli.

### -1- Kumonekta sa server

Gawin muna nating kliyente:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // I-import ang zod para sa pagsubok ng iskema

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

Sa code na nauna nating ginawa:

- In-import ang mga kinakailangang library
- Gumawa ng klase na may dalawang miyembro, `client` at `openai` na tutulong sa atin pamahalaan ang isang kliyente at makipag-ugnayan sa LLM nang sunud-sunod.
- Inayos ang ating LLM instance para gamitin ang GitHub Models sa pamamagitan ng pagtatakda ng `baseUrl` na tumutukoy sa inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Gumawa ng mga parameter ng server para sa stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Maaring patakbuhin
    args=["run", "server.py"],  # Opsyonal na mga argumento sa command line
    env=None,  # Opsyonal na mga variable ng kapaligiran
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # I-initialize ang koneksyon
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Sa code na nauna nating ginawa:

- In-import ang mga kinakailangang library para sa MCP
- Gumawa ng kliyente

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

Una, kailangan mong idagdag ang LangChain4j dependencies sa iyong `pom.xml` file. Idagdag ang mga dependencies na ito para payagan ang integrasyon ng MCP at ang OpenAI-compatible MiniMax API:

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

Itakda ang iyong MiniMax API key at, kung gusto, ang endpoint at modelo.
Sinusuportahan ng `MINIMAX_MODEL_ID` ang `MiniMax-M3` at `MiniMax-M2.7`. Kung
hindi naka-set ang `OPENAI_BASE_URL`, sinusuportahan ng `MINIMAX_REGION` ang `global_en` at `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Para pumili ng endpoint ayon sa rehiyon, huwag itakda ang `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Pagkatapos gumawa ng iyong Java client class:

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

        // Gumawa ng MCP transport para kumonekta sa server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Gumawa ng MCP client
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

Sa code na nauna nating ginawa:

- **Nagdagdag ng LangChain4j dependencies**: Kailangan para sa MCP integrasyon at OpenAI-compatible MiniMax API
- **In-import ang LangChain4j libraries**: Para sa MCP integrasyon at OpenAI chat model functionality
- **Gumawa ng `ChatLanguageModel`**: Inayos para gamitin ang MiniMax gamit ang iyong MiniMax API key, endpoint, at suportadong model ID
- **Naka-set up ang HTTP transport**: Gamit ang Server-Sent Events (SSE) para kumonekta sa MCP server
- **Gumawa ng MCP client**: Na siyang mag-aasikaso ng komunikasyon sa server
- **Ginamit ang built-in MCP support ng LangChain4j**: Na nagpapadali sa integrasyon sa pagitan ng LLMs at MCP servers

#### Rust

Ang halimbawang ito ay nagpapalagay na mayroon kang Rust-based na MCP server na tumatakbo. Kung wala ka pa, balikan ang aralin sa [01-first-server](../01-first-server/README.md) upang gumawa ng server.

Kapag mayroon ka nang Rust MCP server, buksan ang isang terminal at pumunta sa parehong direktoryo ng server. Pagkatapos patakbuhin ang sumusunod na utos para gumawa ng bagong LLM client project:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Idagdag ang mga sumusunod na dependencies sa iyong `Cargo.toml` file:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Walang opisyal na Rust library para sa OpenAI, ngunit ang `async-openai` crate ay isang [community maintained library](https://platform.openai.com/docs/libraries/rust#rust) na karaniwang ginagamit.

Buksan ang `src/main.rs` file at palitan ang nilalaman nito ng sumusunod na code:

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
    // Paunang mensahe
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // I-setup ang OpenAI client
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // I-setup ang MCP client
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

    // TODO: Kunin ang listahan ng MCP tool

    // TODO: Pag-uusap ng LLM gamit ang mga tawag sa tool

    Ok(())
}
```

Ang code na ito ay nagse-setup ng isang basic na Rust application na kumokonekta sa isang MCP server at GitHub Models para sa LLM na interaksyon.

> [!IMPORTANT]
> Siguraduhing itakda ang `OPENAI_API_KEY` environment variable gamit ang iyong GitHub token bago patakbuhin ang application.

Mahusay, sa susunod nating hakbang, ilista natin ang mga kakayahan sa server.

### -2- Ilan ng mga kakayahan ng server

Ngayon ay kokonekta tayo sa server at hihilingin ang mga kakayahan nito:

#### Typescript

Sa parehong klase, idagdag ang sumusunod na mga pamamaraan:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // paglista ng mga kasangkapan
    const toolsResult = await this.client.listTools();
}
```

Sa code na nauna nating ginawa:

- Nagdagdag ng code para kumonekta sa server, `connectToServer`.
- Gumawa ng `run` method na responsable sa paghawak ng daloy ng aplikasyon. Sa ngayon, ito ay naglilista lamang ng mga tool, ngunit dadagdagan natin ito sa susunod.

#### Python

```python
# Ilista ang mga magagamit na mapagkukunan
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Ilista ang mga magagamit na kasangkapan
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Narito ang idinagdag natin:

- Nagtala ng mga resources at mga tool at ipinrint ang mga ito. Para sa mga tool, inilista rin natin ang `inputSchema` na gagamitin natin mamaya.

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

Sa code na nauna nating ginawa:

- Inilista ang mga tool na available sa MCP Server
- Para sa bawat tool, inilista ang pangalan, deskripsyon at ang schema nito. Ang huli ay gagamitin natin upang tawagin ang mga tool sandali.

#### Java

```java
// Lumikha ng tool provider na awtomatikong naghahanap ng mga MCP tool
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Ang MCP tool provider ay awtomatikong humahandle ng:
// - Paglilista ng mga available na tool mula sa MCP server
// - Pagko-convert ng mga schema ng MCP tool sa LangChain4j na format
// - Pamamahala ng pagpapatakbo ng tool at mga sagot
```

Sa code na nauna nating ginawa:

- Gumawa ng `McpToolProvider` na awtomatikong naghahanap at nagrerehistro ng lahat ng tool mula sa MCP server
- Inaalagaan ng tool provider ang conversion sa pagitan ng MCP tool schemas at sa LangChain4j's tool format nang internal
- Ang paraan na ito ay nag-aalis ng manual na pag-lista at conversion ng tool

#### Rust

Ang pagkuha ng mga tool mula sa MCP server ay ginagawa gamit ang `list_tools` method. Sa iyong `main` function, pagkatapos mag-set up ng MCP client, idagdag ang sumusunod na code:

```rust
// Kunin ang listahan ng MCP tool
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- I-convert ang kakayahan ng server sa mga LLM tool

Ang susunod na hakbang pagkatapos ilista ang kakayahan ng server ay i-convert ito sa format na nauunawaan ng LLM. Kapag nagawa na natin ito, maibibigay natin ang mga kakayahang ito bilang mga tool para sa ating LLM.

#### TypeScript

1. Idagdag ang sumusunod na code para i-convert ang tugon mula sa MCP Server sa tool format na magagamit ng LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Lumikha ng zod schema batay sa input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Tahasang itakda ang uri sa "function"
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

    Ang code sa itaas ay kumukuha ng tugon mula sa MCP Server at kino-convert iyon sa tool definition format na nauunawaan ng LLM.

2. I-update natin ang `run` method upang ilista ang kakayahan ng server:

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

    Sa naunang code, in-update natin ang `run` method upang i-map ang resulta at para sa bawat entry ay tawagin ang `openAiToolAdapter`.

#### Python

1. Una, gumawa tayo ng sumusunod na converter function

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

    Sa function na `convert_to_llm_tools` ay kinukuha ang MCP tool response at kino-convert sa format na nauunawaan ng LLM.

2. Sunod, i-update natin ang kodigo ng ating kliyente gamit ang function na ito tulad nito:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Dito, nagdagdag tayo ng tawag sa `convert_to_llm_tool` para i-convert ang MCP tool response sa maaaring ipasa sa LLM.

#### .NET

1. Idagdag ang code upang i-convert ang MCP tool response sa format na nauunawaan ng LLM

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

Sa naunang code:

- Gumawa ng function `ConvertFrom` na tumatanggap ng pangalan, deskripsyon, at input schema.
- Nagdefine ng functionality na lumilikha ng FunctionDefinition na ipinapasa sa ChatCompletionsDefinition. Ang huli ay nauunawaan ng LLM.

2. Tignan natin paano i-update ang umiiral na kodigo para gamitin ang function na ito:

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
// Lumikha ng isang Bot interface para sa natural na pakikipag-ugnayan sa wika
public interface Bot {
    String chat(String prompt);
}

// Isaayos ang AI serbisyo gamit ang LLM at MCP na mga kasangkapan
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Sa naunang code:

- Nagdefine ng simpleng `Bot` interface para sa natural language interactions
- Ginamit ang LangChain4j's `AiServices` para awtomatikong i-bind ang LLM sa MCP tool provider
- Ang framework ay awtomatikong nag-aasikaso ng tool schema conversion at pagtawag ng function sa likod ng mga eksena
- Ang pamamaraang ito ay nag-aalis ng manual na conversion - inilalapat ng LangChain4j ang lahat ng komplikasyon ng pag-convert ng MCP tools sa LLM-compatible na format

#### Rust

Para i-convert ang MCP tool response sa format na nauunawaan ng LLM, magdaragdag tayo ng helper function na nagfo-format ng listing ng mga tool. Idagdag ang sumusunod na code sa iyong `main.rs` file sa ibaba ng `main` function. Tatawagin ito kapag gagawa ng hiling sa LLM:

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

Mahusay, handa na tayo para hawakan ang mga user request, kaya't susunod naman iyon.

### -4- Hawakan ang request ng user prompt

Sa bahaging ito ng code, hahawakan natin ang mga kahilingan ng gumagamit.

#### TypeScript

1. Idagdag ang method na gagamitin para tawagan ang ating LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Tawagan ang kasangkapan ng server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gumawa ng bagay gamit ang resulta
        // GAGAWIN

        }
    }
    ```

    Sa naunang code ay:

    - Nagdagdag ng method na `callTools`.
    - Tinitingnan ng method kung anong mga tool ang tinawag batay sa sagot ng LLM, kung mayroon man:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // tawagan ang kasangkapan
        }
        ```

    - Tumatawag ng tool kung sinasabi ng LLM na dapat itong tawagin:

        ```typescript
        // 2. Tawagan ang kasangkapang server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gawin ang isang bagay sa resulta
        // TODO
        ```

2. I-update ang `run` method upang magsama ng tawag sa LLM at tawagin ang `callTools`:

    ```typescript

    // 1. Gumawa ng mga mensahe na input para sa LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Tawagin ang LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Suriin ang sagot ng LLM, para sa bawat pagpipilian, tingnan kung mayroon itong mga tawag sa tool
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Mahusay, ilista natin ang buong code:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Mag-import ng zod para sa pagsusuri ng schema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // maaaring kailanganin baguhin ito sa url na ito sa hinaharap: https://models.github.ai/inference
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
          // Gumawa ng zod schema base sa input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Tiyak na itakda ang uri sa "function"
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
    
    
          // 2. Tawagan ang tool ng server
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Gawin ang isang bagay gamit ang resulta
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
    
        // 3. Suriin ang tugon ng LLM, para sa bawat pagpipilian, tingnan kung mayroon itong mga tawag sa tool
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

1. Idagdag natin ang ilang mga import na kailangan para tawagan ang LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Sunod, idagdag natin ang function na tatawag sa LLM:

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
            # Opsyonal na mga parameter
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

    Sa naunang code:

    - Ipinasa natin ang mga function na nahanap natin sa MCP server at na-convert sa LLM.
    - Tinawag natin ang LLM gamit ang mga nasabing function.
    - Sinusuri natin ang resulta para malaman kung anong function ang dapat tawagin, kung mayroon man.
    - Sa huli, ipinapasa ang array ng mga function na tatawagin.

3. Panghuli, i-update natin ang main code:

    ```python
    prompt = "Add 2 to 20"

    # tanungin ang LLM kung anong mga kagamitan ang mayroon, kung meron man
    functions_to_call = call_llm(prompt, functions)

    # tawagan ang mga mungkahing function
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Narito, iyon ang panghuling hakbang sa code sa itaas:

    - Tinawag ang isang MCP tool sa pamamagitan ng `call_tool` gamit ang function na naisip ng LLM na dapat tawagin batay sa prompt.
    - Ipinrint ang resulta ng tawag ng tool sa MCP Server.

#### .NET

1. Ipakita natin ang code para sa paggawa ng LLM prompt request:

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

    Sa naunang code:

    - Kumuha ng mga tool mula sa MCP server, `var tools = await GetMcpTools()`.
    - Nagdefine ng user prompt `userMessage`.
    - Gumawa ng options object na tumutukoy sa model at mga tool.
    - Nagsagawa ng request patungo sa LLM.

2. Isang huling hakbang, tignan kung sa palagay ng LLM ay dapat nating tawagin ang isang function:

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

    Sa naunang code:

    - Nilakad ang listahan ng function calls.
    - Para sa bawat tawag sa tool, inparse ang pangalan at mga argumento at tinawag ang tool sa MCP server gamit ang MCP client. Sa huli, ipinrint ang mga resulta.

Narito ang buong code:

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
    // Isagawa ang mga kahilingan sa natural na wika na awtomatikong gumagamit ng mga tool ng MCP
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

Sa naunang code:

- Gumamit ng simple natural language prompts upang makipag-ugnayan sa MCP server tools
- Ang LangChain4j framework ay awtomatikong nagsasaayos ng:
  - Pag-convert ng user prompts sa tool calls kapag kinakailangan
  - Pagtawag sa mga angkop na MCP tools base sa desisyon ng LLM
  - Pamamahala ng daloy ng pag-uusap sa pagitan ng LLM at MCP server
- Ang `bot.chat()` method ay nagbabalik ng natural language responses na maaari ring magsama ng mga resulta mula sa pagpapatupad ng MCP tool
- Ang pamamaraang ito ay nagbibigay ng tuloy-tuloy na karanasan sa gumagamit kung saan hindi na kailangang malaman ng mga user ang detalyadong implementasyon ng MCP

Kumpletong halimbawa ng code:

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


Dito nangyayari ang karamihan ng gawain. Tatawagin natin ang LLM gamit ang unang prompt ng gumagamit, pagkatapos ay ipoproseso ang tugon upang makita kung kailangan bang tawagin ang anumang mga tool. Kung oo, tatawagin natin ang mga tool na iyon at ipagpapatuloy ang pag-uusap sa LLM hanggang sa wala nang kailangang tawaging mga tool at mayroon tayong panghuling tugon.

Gagawa tayo ng maraming tawag sa LLM, kaya't magdeklara tayo ng isang function na hahawak sa tawag ng LLM. Idagdag ang sumusunod na function sa iyong `main.rs` na file:

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

Tumatanggap ang function na ito ng LLM client, isang listahan ng mga mensahe (kasama ang prompt ng gumagamit), mga tool mula sa MCP server, at nagpapadala ng isang kahilingan sa LLM, na nagbabalik ng tugon.

Ang tugon mula sa LLM ay maglalaman ng isang array ng `choices`. Kailangan nating iproseso ang resulta upang makita kung mayroong mga `tool_calls`. Ipinapaalam nito sa atin na hinihiling ng LLM na tawagin ang isang partikular na tool na may mga argumento. Idagdag ang sumusunod na code sa ibaba ng iyong `main.rs` na file upang ideklara ang isang function na hahawak sa tugon ng LLM:

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

    // I-print ang nilalaman kung meron
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Pangasiwaan ang mga tawag sa tool
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Magdagdag ng mensahe ng assistant

        // Isagawa ang bawat tawag sa tool
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Idagdag ang resulta ng tool sa mga mensahe
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Ipagpatuloy ang pag-uusap gamit ang mga resulta ng tool
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

Kung may mga `tool_calls`, kinukuha nito ang impormasyon ng tool, tinatawag ang MCP server gamit ang kahilingan sa tool, at idinadagdag ang mga resulta sa mga mensahe ng pag-uusap. Pagkatapos ay ipinagpapatuloy nito ang pag-uusap sa LLM at naia-update ang mga mensahe sa tugon ng assistant at mga resulta ng pagtawag ng tool.

Upang kunin ang impormasyon ng pagtawag ng tool na ibinabalik ng LLM para sa mga tawag sa MCP, magdadagdag tayo ng isa pang helper function upang kunin ang lahat ng kailangan upang gawin ang tawag. Idagdag ang sumusunod na code sa ibaba ng iyong `main.rs` na file:

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

Sa pagkakaroon ng lahat ng mga bahagi, maaari na nating hawakan ang unang prompt ng gumagamit at tawagin ang LLM. I-update ang iyong `main` na function upang isama ang sumusunod na code:

```rust
// Usapan ng LLM na may mga tawag sa kasangkapan
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

Tatanggapin nito ang LLM gamit ang unang prompt ng gumagamit na humihiling para sa kabuuan ng dalawang numero, at ipoproseso nito ang tugon upang dinamikal na hawakan ang pagtawag sa mga tool.

Magaling, nagawa mo ito!

## Assignment

Kunin ang code mula sa ehersisyo at buuin ang server gamit ang ilan pang mga tool. Pagkatapos ay gumawa ng kliyente gamit ang LLM, tulad sa ehersisyo, at subukan ito gamit ang iba't ibang mga prompt upang matiyak na lahat ng mga tool ng iyong server ay natatawag nang dinamiko. Ang ganitong paraan ng paggawa ng kliyente ay nangangahulugang magkakaroon ng mahusay na karanasan ang end user dahil kaya nilang gamitin ang mga prompt, sa halip na eksaktong mga command ng kliyente, at hindi nila malalaman kung may tawag na MCP server.

## Solution

[Solution](./solution/README.md)

## Mga Pangunahing Puntos

- Ang pagdagdag ng LLM sa iyong kliyente ay nagbibigay ng mas mahusay na paraan para sa mga gumagamit na makipag-ugnayan sa MCP Servers.
- Kailangan mong i-convert ang tugon ng MCP Server sa isang bagay na maiintindihan ng LLM.

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Karagdagang mga Mapagkukunan

## Ano ang Susunod

- Susunod: [Paggamit ng isang server gamit ang Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->