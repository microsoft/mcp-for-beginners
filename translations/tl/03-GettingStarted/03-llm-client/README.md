# Paglikha ng kliyente gamit ang LLM

Hanggang ngayon, nakita mo na kung paano gumawa ng server at kliyente. Nagawang tawagan ng kliyente ang server nang hayagan upang ilista ang mga tools, resources, at prompts nito. Gayunpaman, hindi ito isang praktikal na paraan. Ang iyong mga gumagamit ay nabubuhay sa agentic era at inaasahan na gamitin ang mga prompt at makipag-usap sa isang LLM na lamang. Hindi sila interesado kung ginagamit mo ang MCP para iimbak ang iyong mga kakayahan; inaasahan lang nila na makipag-ugnayan gamit ang natural na wika. Paano natin ito sosolusyunan? Ang solusyon ay magdagdag ng isang LLM sa kliyente.

## Pangkalahatang-ideya

Sa araling ito ay nakatuon tayo sa pagdaragdag ng isang LLM sa iyong kliyente at ipapakita kung paano ito nagbibigay ng mas magandang karanasan para sa iyong gumagamit.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Gumawa ng kliyente na may LLM.
- Makipag-ugnayan nang maayos sa isang MCP server gamit ang isang LLM.
- Magbigay ng mas mahusay na karanasan sa end user sa bahagi ng kliyente.

## Paraan

Subukan natin unawain ang paraan na kailangan nating gawin. Ang pagdaragdag ng isang LLM ay tila simple, ngunit talagang gagawin ba natin ito?

Ganito ang pakikipag-ugnayan ng kliyente sa server:

1. Magtatag ng koneksyon sa server.

1. Ililista ang mga kakayahan, mga prompt, mga resources at mga tools, at i-save ang kanilang schema.

1. Magdagdag ng isang LLM at ipasa ang mga na-save na kakayahan at kanilang schema sa isang format na naiintindihan ng LLM.

1. Pangalagaan ang prompt ng user sa pamamagitan ng pagpapasa nito sa LLM kasama ang mga tool na nakalista ng kliyente.

Magaling, ngayon ay naintindihan na natin kung paano gawin ito sa mataas na antas, subukan natin ito sa ibaba na ehersisyo.

## Ehersisyo: Paglikha ng kliyente na may LLM

Sa ehersisyong ito, matututo tayo na magdagdag ng LLM sa ating kliyente.

### Pagpapatunay gamit ang GitHub Personal Access Token

Ang paggawa ng GitHub token ay isang simple at diretso na proseso. Ganito mo ito magagawa:

- Pumunta sa GitHub Settings – I-click ang iyong larawan ng profile sa itaas na kanang sulok at piliin ang Settings.
- Mag-navigate sa Developer Settings – Mag-scroll pababa at i-click ang Developer Settings.
- Piliin ang Personal Access Tokens – I-click ang Fine-grained tokens at pagkatapos ay Generate new token.
- I-configure ang Iyong Token – Magdagdag ng tala para sa sanggunian, magtakda ng expiration date, at piliin ang kinakailangang scopes (mga pahintulot). Sa pagkakataong ito tiyakin na idagdag ang Models permission.
- I-generate at Kopyahin ang Token – I-click ang Generate token, at siguraduhing kopyahin ito agad dahil hindi mo na ito muling makikita.

### -1- Kumonekta sa server

Gawin muna natin ang ating kliyente:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // I-import ang zod para sa pag-validate ng schema

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

Sa mga naunang code ay:

- Inimport ang mga kinakailangang library
- Gumawa ng klase na may dalawang miyembro, `client` at `openai` na tutulong sa atin pamahalaan ang kliyente at makipag-ugnayan sa isang LLM.
- Inayos ang ating LLM instance para gamitin ang GitHub Models sa pamamagitan ng pagtatakda ng `baseUrl` na tumutukoy sa inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Lumikha ng mga parameter ng server para sa stdio koneksyon
server_params = StdioServerParameters(
    command="mcp",  # Maaaring patakbuhin
    args=["run", "server.py"],  # Mga opsyonal na argumento ng command line
    env=None,  # Mga opsyonal na variable ng kapaligiran
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

Sa mga naunang code ay:

- Inimport ang mga kinakailangang library para sa MCP
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

Una, kailangan mong idagdag ang LangChain4j dependencies sa iyong `pom.xml` file. Idagdag ang mga dependency na ito upang paganahin ang MCP integration at ang OpenAI-compatible MiniMax API:

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

Itakda ang iyong MiniMax API key at, opsyonal, ang endpoint at modelo.
Sinusuportahan ng `MINIMAX_MODEL_ID` ang `MiniMax-M3` at `MiniMax-M2.7`. Kung hindi itinakda ang
`OPENAI_BASE_URL`, sinusuportahan ng `MINIMAX_REGION` ang `global_en` at `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Para pumili ng endpoint ayon sa rehiyon, huwag isama ang `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Pagkatapos lumikha ng iyong Java client class:

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

        // Lumikha ng MCP transport para kumonekta sa server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Lumikha ng MCP client
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

Sa mga naunang code ay:

- **Nagdagdag ng LangChain4j dependencies**: Kinakailangan para sa MCP integration at OpenAI-compatible MiniMax API
- **Inimport ang mga LangChain4j libraries**: Para sa MCP integration at functionality ng OpenAI chat model
- **Gumawa ng `ChatLanguageModel`**: Inayos para gamitin ang MiniMax gamit ang iyong MiniMax API key, endpoint, at suportadong model ID
- **Nagtakda ng HTTP transport**: Gamit ang Server-Sent Events (SSE) para kumonekta sa MCP server
- **Gumawa ng MCP client**: Na siyang hahawak ng komunikasyon sa server
- **Ginamit ang built-in na suporta ng LangChain4j MCP**: Na nagpapadali ng integrasyon sa pagitan ng LLMs at MCP servers

#### Rust

Ang halimbawang ito ay nangangailangan na mayroong Rust-based MCP server ka na tumatakbo. Kung wala ka pa, balikan ang [01-first-server](../01-first-server/README.md) na aralin para gumawa ng server.

Kapag meron ka nang Rust MCP server, buksan ang terminal at pumunta sa parehong direktoryo ng server. Pagkatapos ay patakbuhin ang sumusunod na utos para gumawa ng bagong LLM client project:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Idagdag ang mga sumusunod na dependency sa iyong `Cargo.toml` file:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Walang opisyal na Rust library para sa OpenAI, gayunpaman, ang `async-openai` crate ay isang [community maintained library](https://platform.openai.com/docs/libraries/rust#rust) na karaniwang ginagamit.

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

    // I-set up ang OpenAI client
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // I-set up ang MCP client
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

    // TODO: Kunin ang listahan ng tool ng MCP

    // TODO: Pag-uusap ng LLM gamit ang mga tawag sa tool

    Ok(())
}
```

Itinakda ng code na ito ang isang basic Rust application na kokonekta sa MCP server at GitHub Models para sa pakikipag-ugnayan sa LLM.

> [!IMPORTANT]
> Siguraduhing itakda ang `OPENAI_API_KEY` environment variable gamit ang iyong GitHub token bago patakbuhin ang application.

Magaling, para sa susunod na hakbang, ilista natin ang mga kakayahan ng server.

### -2- Ilista ang mga kakayahan ng server

Ngayon ay kokonekta tayo sa server at hihingin ang mga kakayahan nito:

#### Typescript

Sa parehong klase, idagdag ang mga sumusunod na metodo:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // paglista ng mga kagamitan
    const toolsResult = await this.client.listTools();
}
```

Sa mga naunang code ay:

- Nagdagdag ng code para kumonekta sa server, `connectToServer`.
- Gumawa ng `run` method na responsable para pamahalaan ang takbo ng ating app. Hanggang ngayon, ito ay naglilista lang ng mga tool ngunit magdadagdag tayo ng higit pa dito.

#### Python

```python
# Ilahad ang mga magagamit na mapagkukunan
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Ilahad ang mga magagamit na kasangkapan
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Ganito ang idinagdag natin:

- Naglista ng mga resources at tools at prinint ang mga ito. Para sa mga tools, nilista rin natin ang `inputSchema` na gagamitin natin mamaya.

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

Sa mga naunang code ay:

- Naka-lista ang mga tool na available sa MCP Server
- Para sa bawat tool, nilista ang pangalan, paglalarawan at ang schema nito. Ito ang gagamitin natin para tawagan ang mga tool mamaya.

#### Java

```java
// Gumawa ng tagapagbigay ng tool na awtomatikong nagtatuklas ng mga MCP tool
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Awtomatikong pinamamahalaan ng tagapagbigay ng MCP tool ang:
// - Paglilista ng mga magagamit na tool mula sa server ng MCP
// - Pag-convert ng mga schema ng MCP tool sa format ng LangChain4j
// - Pamamahala ng pagpapatupad ng tool at mga tugon
```

Sa mga naunang code ay:

- Gumawa ng `McpToolProvider` na kusang natutuklasan at nire-register lahat ng tools mula sa MCP server
- Pinangangasiwaan ng tool provider ang conversion sa pagitan ng MCP tool schemas at LangChain4j's tool format nang internal
- Pinapaliit nito ang manu-manong prosesong paglista ng tool at conversion

#### Rust

Ang pagkuha ng mga tools mula sa MCP server ay ginagawa gamit ang `list_tools` method. Sa iyong `main` function, pagkatapos i-set up ang MCP client, idagdag ang sumusunod na code:

```rust
// Kunin ang listahan ng MCP tool
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- I-convert ang mga kakayahan ng server sa LLM tools

Susunod na hakbang pagkatapos mailista ang mga kakayahan ng server ay i-convert ang mga ito sa isang format na naiintindihan ng LLM. Kapag nagawa na natin iyon, maibibigay natin ang mga kakayahang ito bilang mga tools sa ating LLM.

#### TypeScript

1. Idagdag ang sumusunod na code para i-convert ang response mula sa MCP Server sa tool format na magagamit ng LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Gumawa ng zod schema batay sa input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Eksplisitong itakda ang uri sa "function"
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

Ang code sa itaas ay kumukuha ng response mula sa MCP Server at kino-convert ito sa tool definition format na naiintindihan ng LLM.

2. I-update naman natin ang `run` method para ilista ang mga kakayahan ng server:

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

Sa naunang code, in-update natin ang `run` method na mag-map sa resulta at para sa bawat entry tawagan ang `openAiToolAdapter`.

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

Sa function na `convert_to_llm_tools` ay kinokonvert natin ang MCP tool response sa format na maiintindihan ng LLM.

2. Sunod, i-update natin ang ating client code upang magamit ang function na ito ganito:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

Dito, nagdaragdag tayo ng tawag sa `convert_to_llm_tool` para i-convert ang MCP tool response sa isang bagay na mailalabas natin sa LLM mamaya.

#### .NET

1. Magdagdag tayo ng code para i-convert ang MCP tool response sa isang format na maiintindihan ng LLM

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

Sa mga naunang code ay:

- Gumawa ng function `ConvertFrom` na tumatanggap ng pangalan, paglalarawan at input schema.
- Nag-defina ng functionality na lumilikha ng FunctionDefinition na ipinapasa sa ChatCompletionsDefinition. Ang huli ay naiintindihan ng LLM.

2. Tingnan natin kung paano i-update ang ilang umiiral na code para makinabang sa function na ito:

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
// Lumikha ng isang Bot interface para sa natural na pakikipag-ugnayan gamit ang wika
public interface Bot {
    String chat(String prompt);
}

// I-configure ang serbisyo ng AI gamit ang LLM at MCP na mga kasangkapan
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Sa mga naunang code ay:

- Nag-defina ng simpleng `Bot` interface para sa mga natural language interactions
- Ginamit ang LangChain4j's `AiServices` para awtomatikong i-bind ang LLM sa MCP tool provider
- Awtomatikong pinangangasiwaan ng framework ang tool schema conversion at function calling sa likod ng eksena
- Inaalis nito ang manu-manong conversion ng tool - pinangangasiwaan ng LangChain4j ang lahat ng komplikasyon ng conversion mula MCP tools papuntang LLM-compatible format

#### Rust

Para i-convert ang MCP tool response sa format na naiintindihan ng LLM, magdadagdag tayo ng helper function na nagfo-format ng listing ng mga tools. Idagdag ang sumusunod na code sa iyong `main.rs` file sa ilalim ng `main` function. Tatawagin ito kapag gumagawa ng mga request sa LLM:

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

Magaling, nakahanda na tayo na pangasiwaan ang mga request ng user, kaya't tackle natin iyon sa susunod.

### -4- Pangasiwaan ang user prompt request

Sa bahaging ito ng code, pangasiwaan natin ang mga request ng user.

#### TypeScript

1. Magdagdag ng isang metodo na gagamitin para tawagan ang ating LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Tawagin ang kasangkapan ng server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gawin ang isang bagay gamit ang resulta
        // GAWIN PA

        }
    }
    ```

Sa naunang code ay:

- Nagdagdag ng method `callTools`.
- Tinitingnan ng method ang response ng LLM at sinusuri kung anong mga tools ang tinawag, kung meron man:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // tawagan ang tool
        }
        ```

- Tumatawag ng tool, kung sinasabi ng LLM na dapat itong tawagan:

        ```typescript
        // 2. Tawagan ang kasangkapan ng server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gawin ang isang bagay gamit ang resulta
        // GAGAWIN
        ```

2. I-update ang `run` method upang maisama ang tawag sa LLM at pagtawag sa `callTools`:

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

    // 3. Suriin ang tugon ng LLM, para sa bawat pagpipilian, tingnan kung may mga tawag sa mga tool
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Magaling, tingnan natin ang buong code:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // I-import ang zod para sa schema validation

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // Maaaring kailanganing palitan sa url na ito sa hinaharap: https://models.github.ai/inference
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
          // Gumawa ng zod schema batay sa input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Hayagang itakda ang type bilang "function"
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
          // GAGAWIN PA
    
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
    
        // 3. Suriin ang sagot mula sa LLM, para sa bawat pagpipilian, tingnan kung may mga tawag sa tool
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

1. Magdagdag tayo ng mga import na kinakailangan para tawagan ang LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Sunod, magdagdag tayo ng function na tatawag sa LLM:

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
            # Mga opsyonal na parameter
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

Sa mga naunang code ay:

- Ipinasa ang mga functions na nahanap natin sa MCP server at na-convert sa LLM.
- Tinawag ang LLM gamit ang mga function na iyon.
- Sini-inspeksyon ang resulta para makita kung anong functions ang dapat tawagin, kung meron man.
- Sa wakas, pinapasa ang array ng mga functions na dapat tawagin.

3. Huling hakbang, i-update natin ang ating pangunahing code:

    ```python
    prompt = "Add 2 to 20"

    # tanungin ang LLM kung anong mga kasangkapan ang mayroon, kung mayroon man
    functions_to_call = call_llm(prompt, functions)

    # tawagan ang mga mungkahing function
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

Iyon na, iyon ang huling hakbang, sa code sa itaas ay:

- Tinatawag ang MCP tool via `call_tool` gamit ang function na iniisip ng LLM na dapat tawagin base sa ating prompt.
- Pinapakita ang resulta ng pagtawag sa tool sa MCP Server.

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

Sa mga naunang code ay:

- Nakuha ang mga tools mula sa MCP server, `var tools = await GetMcpTools()`.
- Nag-defina ng user prompt `userMessage`.
- Gumawa ng options object na nagtatalaga ng modelo at tools.
- Gumawa ng request patungo sa LLM.

2. Isa pang hakbang, tingnan kung iniisip ng LLM na dapat tawagin ang isang function:

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

Sa mga naunang code ay:

- Inikot ang listahan ng mga function calls.
- Para sa bawat tool call, kinukuha ang pangalan at mga argumento at tinatawag ang tool sa MCP server gamit ang MCP client. Sa wakas, ipinapakita ang mga resulta.

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
    // Isagawa ang mga kahilingan sa natural na wika na awtomatikong gumagamit ng mga MCP na kasangkapan
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

Sa mga naunang code ay:

- Ginamit ang simpleng natural language prompts para makipag-ugnayan sa mga tool ng MCP server
- Awtomatikong pinangangasiwaan ng LangChain4j framework:
  - Pag-convert ng user prompts sa tool calls kapag kinakailangan
  - Pagtawag sa mga tamang MCP tools base sa desisyon ng LLM
  - Pamamahala sa daloy ng pag-uusap sa pagitan ng LLM at MCP server
- Ang `bot.chat()` method ay nagbabalik ng mga sagot sa natural na wika na maaaring kasama ang mga resulta mula sa pagpapatupad ng mga MCP tool
- Ang paraan na ito ay nagbibigay ng seamless na karanasan para sa gumagamit kung saan hindi nila kailangang malaman ang tungkol sa likod ng MCP implementation

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

Dito nagaganap ang karamihan ng trabaho. Tatawagin natin ang LLM gamit ang unang prompt ng user, pagkatapos ay ipoproseso ang sagot upang makita kung kailangan bang tawagin ang mga tool. Kung oo, tatawagin natin ang mga tool na iyon at ipagpapatuloy ang pag-uusap sa LLM hanggang sa wala nang kailangang pagtawag sa tool at makuha na ang pinal na sagot.


Gagawa tayo ng maraming tawag sa LLM, kaya magde-define muna tayo ng isang function na magha-handle ng tawag sa LLM. Idagdag ang sumusunod na function sa iyong `main.rs` na file:

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

Ang function na ito ay tumatanggap ng LLM client, isang listahan ng mga mensahe (kasama na ang user prompt), mga tools mula sa MCP server, at nagpapadala ng request sa LLM, at ibinabalik ang tugon.

Ang tugon mula sa LLM ay magkakaroon ng array ng `choices`. Kailangan nating prosesuhin ang resulta upang makita kung may mga `tool_calls` na naroroon. Ipinapahiwatig nito na ang LLM ay humihiling na tawagin ang isang partikular na tool gamit ang mga argumento. Idagdag ang sumusunod na code sa ibaba ng iyong `main.rs` file upang ide-define ang isang function na magha-handle ng tugon ng LLM:

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

    // I-print ang nilalaman kung available
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Pangasiwaan ang mga tawag sa tool
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Magdagdag ng mensahe mula sa assistant

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

Kung mayroong `tool_calls`, kukunin nito ang impormasyon ng tool, tatawagin ang MCP server gamit ang request ng tool, at idadagdag ang mga resulta sa mga mensahe ng pag-uusap. Pagkatapos ay ipinagpapatuloy ang pag-uusap sa LLM at naa-update ang mga mensahe gamit ang tugon ng assistant at resulta ng tool call.

Para kunin ang impormasyon ng tool call na ibinabalik ng LLM para sa mga MCP call, magdadagdag tayo ng isa pang helper function upang makuha ang lahat ng kailangang datos para gawin ang call. Idagdag ang sumusunod na code sa ibaba ng iyong `main.rs` file:

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

Sa pagkakaroon ng lahat ng bahagi, maaari na nating i-handle ang initial na user prompt at tawagan ang LLM. I-update ang iyong `main` function upang isama ang sumusunod na code:

```rust
// Usapan ng LLM na may tawag sa tool
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

Ito ay magtatanong sa LLM gamit ang initial user prompt na humihiling ng sum ng dalawang numero, at ipoproseso ang tugon upang dynamic na mahawakan ang tool calls.

Magaling, nagawa mo ito!

## Takdang-Aralin

Gamitin ang code mula sa exercise at buuin ang server na may mas maraming tools. Pagkatapos gumawa ng client na may LLM, gaya ng sa exercise, at subukan ito gamit ang iba't ibang prompts upang matiyak na lahat ng iyong server tools ay dynamic na natatawagan. Ang ganitong paraan ng paggawa ng client ay nangangahulugang magkakaroon ang end user ng mahusay na karanasan sa paggamit dahil makakapag-prompt sila imbes na eksaktong client commands, at hindi nila malalaman ang MCP server na tinatawag.

## Solusyon

[Solusyon](./solution/README.md)

## Mahahalagang Punto

- Ang pagdagdag ng LLM sa iyong client ay nagbibigay ng mas magandang paraan para makipag-interact ang mga user sa MCP Servers.
- Kailangan mong i-convert ang tugon ng MCP Server sa format na maiintindihan ng LLM.

## Mga Sample

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Karagdagang Mga Sanggunian

## Ano ang Susunod

- Susunod: [Paggamit ng server gamit ang Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->