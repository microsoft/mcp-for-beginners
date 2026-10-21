# Paglikha ng kliyente gamit ang LLM

> [!NOTE]
> Ang mga halimbawa ng Java client ay kumokonekta sa pamamagitan ng legacy HTTP+SSE transport at
> tumutukoy sa MCP `2025-11-25` SDK APIs. Gumamit ng `2026-07-28`-compatible na SDK at
> Streamable HTTP para sa mga bagong remote client.

Sa ngayon, nakita mo na kung paano gumawa ng server at client. Nagagawa ng client na tawagan nang tahasan ang server upang ilista ang mga tools, resources, at prompts nito. Gayunpaman, hindi ito napaka-praktikal na paraan. Ang iyong mga user ay nabubuhay sa agentic era at inaasahang gamitin ang prompts at makipag-ugnayan sa isang LLM sa halip. Hindi sila nag-aalala kung ginamit mo ang MCP upang i-store ang iyong mga kakayahan; inaasahan lamang nilang makipag-ugnayan gamit ang natural na wika. Paano natin malulutas ito? Ang solusyon ay magdagdag ng LLM sa client.

## Pangkalahatang-ideya

Sa araling ito, tututok tayo sa pagdaragdag ng LLM sa iyong client at ipapakita kung paano ito nagbibigay ng mas mahusay na karanasan para sa iyong user.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Gumawa ng client na may LLM.
- Maayos na makipag-ugnayan sa MCP server gamit ang LLM.
- Magbigay ng mas magandang karanasan sa end user sa client side.

## Pamamaraan

Subukan nating unawain ang pamamaraan na kailangan nating gawin. Ang pagdaragdag ng LLM ay tila simple, pero talaga ba nating gagawin ito?

Ganito ang magiging interaksyon ng client sa server:

1. Magtatag ng koneksyon sa server.

1. Ililista ang mga kakayahan, prompts, resources at tools, at itatabi ang kanilang schema.

1. Magdaragdag ng LLM at ipapasa ang mga na-save na kakayahan at ang schema nito sa format na naiintindihan ng LLM.

1. Iproseso ang user prompt sa pamamagitan ng pagpapasa nito sa LLM kasabay ng mga tools na inilista ng client.

Mahusay, ngayon na naintindihan natin ang pangkalahatang paraan, subukan natin ito sa sumusunod na ehersisyo.

## Ehersisyo: Paglikha ng client na may LLM

Sa ehersisyong ito, matututunan natin kung paano magdagdag ng LLM sa ating client.

### I-configure ang Microsoft Foundry

Ang GitHub Models ay na-retire noong Hulyo 30, 2026. Gumawa ng Microsoft Foundry resource,
mag-deploy ng aktibong modelo gaya ng `gpt-5.1`, at itakda ang mga sumusunod na environment variables:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

Gamitin ang pangalan ng deployment sa mga API calls. Maaaring ito ay iba sa pangalan ng underlying model.
Suriin ang
[Microsoft Foundry model retirement schedule](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
bago pumili ng modelo.

### -1- Konektahin sa server

Gumawa muna tayo ng client:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Import zod for schema validation

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
            }
            );    
    }
}
```

Sa naunang code kami ay:

- Nag-import ng mga kinakailangang libraries
- Nilikha ang klase na may dalawang miyembro, `client` at `openai` na tutulong sa atin na pamahalaan ang client at makipag-ugnayan sa LLM.
- Na-configure ang OpenAI client para gamitin ang Microsoft Foundry v1 endpoint at API key.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Sa naunang code kami ay:

- Nag-import ng mga kinakailangang libraries para sa MCP
- Nakamita ang client

#### .NET

```csharp
using ModelContextProtocol.Client;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
var client = new ChatClient(
    deployment,
    new ApiKeyCredential(apiKey),
    new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

Una, kailangan mong idagdag ang LangChain4j dependencies sa iyong `pom.xml` file. Idagdag ang mga dependencies na ito upang paganahin ang MCP integration at ang OpenAI-compatible MiniMax API:

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
Sinusuportahan ng `MINIMAX_MODEL_ID` ang `MiniMax-M3` at `MiniMax-M2.7`. Kung
hindi nakaset ang `OPENAI_BASE_URL`, sinusuportahan ng `MINIMAX_REGION` ang `global_en` at `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Para pumili ng endpoint ayon sa rehiyon, iwaksi ang `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Pagkatapos, gumawa ng Java client class:

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

        // Create MCP transport for connecting to server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Create MCP client
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

Sa naunang code kami ay:

- **Nagdagdag ng LangChain4j dependencies**: Kailangan para sa MCP integration at OpenAI-compatible MiniMax API
- **Nag-import ng LangChain4j libraries**: Para sa MCP integration at OpenAI chat model na functionality
- **Nilikha ang `ChatLanguageModel`**: Na-configure upang gamitin ang MiniMax kasama ang iyong MiniMax API key, endpoint, at sinusuportahang model ID
- **Naitakda ang HTTP transport**: Gamit ang Server-Sent Events (SSE) para kumonekta sa MCP server
- **Nalikha ang MCP client**: Na magsisilbing tagapamahala ng komunikasyon sa server
- **Ginamit ang built-in MCP support ng LangChain4j**: Na nagpapadali ng integrasyon sa pagitan ng LLMs at MCP servers

#### Rust

Ina-assume ng halimbawa na ito na mayroon kang Rust-based MCP server na tumatakbo. Kung wala ka pa, bumalik sa aralin [01-first-server](../01-first-server/README.md) para gumawa ng server.

Kapag mayroon ka nang Rust MCP server, buksan ang terminal at pumunta sa parehong direktoryo ng server. Pagkatapos patakbuhin ang sumusunod na utos para gumawa ng bagong LLM client project:

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
> Wala pang opisyal na Rust library para sa OpenAI, ngunit ang `async-openai` crate ay isang [community maintained library](https://platform.openai.com/docs/libraries/rust#rust) na karaniwang ginagamit.

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
    // Initial message
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Setup Microsoft Foundry client
    let endpoint = std::env::var("AZURE_OPENAI_ENDPOINT")?;
    let api_key = std::env::var("AZURE_OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base(format!("{}/openai/v1", endpoint.trim_end_matches('/')))
            .with_api_key(api_key),
    );

    // Setup MCP client
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

    // TODO: Get MCP tool listing 

    // TODO: LLM conversation with tool calls

    Ok(())
}
```

Itinatakda ng code na ito ang Rust application na kumokonekta sa MCP server at sa
Microsoft Foundry model deployment para sa mga interaksyon sa LLM.

> [!IMPORTANT]
> Itakda ang `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, at
> `AZURE_OPENAI_DEPLOYMENT` bago patakbuhin ang application.

Mahusay, sa susunod nating hakbang, ililista natin ang mga kakayahan sa server.

### -2- Ilahad ang mga kakayahan ng server

Ngayon ay kokonekta tayo sa server at hihingin ang mga kakayahan nito:

#### Typescript

Sa parehong klase, idagdag ang mga sumusunod na methods:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // listing tools
    const toolsResult = await this.client.listTools();
}
```

Sa naunang code kami ay:

- Nagdagdag ng code para kumonekta sa server, `connectToServer`.
- Nilikha ang method na `run` na responsable sa paghawak ng daloy ng app. Sa ngayon, naglilista lamang ito ng mga tools ngunit idaragdag pa natin ito.

#### Python

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Narito ang idinagdag natin:

- Paglilista ng mga resources at tools at pag-print sa mga ito. Para sa tools, inilista rin natin ang `inputSchema` na gagamitin natin sa susunod.

#### .NET

```csharp
async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

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

Sa naunang code kami ay:

- Inilista ang mga tools na available sa MCP Server
- Para sa bawat tool, inilista ang pangalan, deskripsyon at schema nito. Ang huli ay gagamitin upang tawagan ang tools sa kalaunan.

#### Java

```java
// Create a tool provider that automatically discovers MCP tools
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// The MCP tool provider automatically handles:
// - Listing available tools from the MCP server
// - Converting MCP tool schemas to LangChain4j format
// - Managing tool execution and responses
```

Sa naunang code kami ay:

- Nilikha ang `McpToolProvider` na awtomatikong naghahanap at nagre-register ng lahat ng tools mula sa MCP server
- Hinahandle ng tool provider ang conversion sa pagitan ng MCP tool schemas at ng format ng LangChain4j tools nang internal
- Ang pamamaraang ito ay nag-aalis ng kinakailangang manual na paglista at conversion ng tools

#### Rust

Ang pagkuha ng mga tools mula sa MCP server ay ginagawa gamit ang method na `list_tools`. Sa iyong function na `main`, pagkatapos i-setup ang MCP client, idagdag ang sumusunod na code:

```rust
// Get MCP tool listing 
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- I-convert ang mga kakayahan ng server sa mga LLM tools

Susunod na hakbang matapos ilista ang mga kakayahan ng server ay i-convert sila sa format na naiintindihan ng LLM. Kapag nagawa na ito, maibibigay natin ang mga kakayahan bilang mga tools sa ating LLM.

#### TypeScript

1. Idagdag ang sumusunod na code upang i-convert ang response mula sa MCP Server patungong tool format na magagamit ng LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Create a zod schema based on the input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Explicitly set type to "function"
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

    Kinukuha ng code sa itaas ang tugon mula sa MCP Server at kino-convert ito sa tool definition format na naiintindihan ng LLM.

2. I-update naman natin ang method na `run` para ilista ang kakayahan ng server:

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

    Sa naunang code, in-update natin ang method na `run` upang i-map ang resulta at sa bawat entry tawagan ang `openAiToolAdapter`.

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

    Sa function na `convert_to_llm_tools` ay kinokonvert natin ang MCP tool response sa format na naiintindihan ng LLM.

2. Pangalawa, i-update ang kodigo ng client upang gamitin ang function na ito tulad nito:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Dito, nagdadagdag tayo ng tawag sa `convert_to_llm_tool` upang i-convert ang MCP tool response sa format na maipapasok natin sa LLM kalaunan.

#### .NET

1. Idagdag ang code upang i-convert ang MCP tool response sa format na naiintindihan ng LLM

```csharp
ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}
```

Sa naunang code kami ay:

- Nakagawa ng function na `ConvertFrom` na tumatanggap ng pangalan, deskripsyon, at input na schema.
- Nakagawa ng OpenAI `ChatTool` mula sa MCP tool na JSON schema.

2. Tingnan natin kung paano natin i-uupdate ang umiiral na code para magamit ang function na ito:

    ```csharp
    async Task<List<ChatTool>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatTool> toolDefinitions = [];

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);
        }

        return toolDefinitions;
    }
    ```
    
Sa naunang code kami ay:

- In-update ang function upang i-convert ang MCP tool response sa LLM tool. Narito ang mga bahagi na idinagdag:

   ```csharp
   JsonElement propertiesElement;
   tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

   var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
   Console.WriteLine($"Tool definition: {def}");
   toolDefinitions.Add(def);
   ```

Ang input schema ay bahagi ng tool response ngunit nasa "properties" attribute, kaya kailangan natin itong i-extract. Dagdag pa, tinatawag natin ang `ConvertFrom` gamit ang detalye ng tool. Natapos na natin ang mabigat na bahagi, tingnan natin kung paano ito tinawag habang pinaproseso ang user prompt.

#### Java

```java
// Create a Bot interface for natural language interaction
public interface Bot {
    String chat(String prompt);
}

// Configure the AI service with LLM and MCP tools
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Sa naunang code kami ay:

- Nagdefine ng simpleng `Bot` interface para sa natural language interaction
- Gumamit ng LangChain4j's `AiServices` upang awtomatikong i-bind ang LLM sa MCP tool provider
- Ang framework ay awtomatikong humahandle ng conversion ng tool schema at function calling sa likod ng eksena
- Inaalis ng pamamaraang ito ang manual tool conversion - hinahandle ng LangChain4j ang lahat ng komplikasyon ng pag-convert ng MCP tools sa LLM-compatible na format

#### Rust

Para i-convert ang MCP tool response sa format na naiintindihan ng LLM, magdadagdag tayo ng helper function na nagfo-format ng tools listing. Idagdag ang sumusunod na code sa iyong `main.rs` file sa ilalim ng `main` function. Tatawagin ito kapag gumagawa ng request sa LLM:

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

Mahusay, nakahanda na tayo upang hawakan ang anumang user na request, kaya gawin natin iyon sa susunod.

### -4- Hawakan ang user prompt request

Sa bahaging ito ng code, hahawakan natin ang mga user requests.

#### TypeScript

1. Magdagdag ng method na gagamitin para tawagan ang LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  

        }
    }
    ```

    Sa naunang code kami ay:

    - Nagdagdag ng method na `callTools`.
    - Tine-check ng method ang sagot mula sa LLM upang makita kung anong mga tools ang tinawag, kung meron:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // call tool
        }
        ```

    - Tinatawag ang tool, kung ipinahiwatig ng LLM na dapat itong tawagin:

        ```typescript
        // 2. Call the server's tool 
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Do something with the result
        // TODO  
        ```

2. I-update ang `run` method upang isama ang mga tawag sa LLM at para tawagin ang `callTools`:

    ```typescript

    // 1. Create messages that's input for the LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Calling the LLM
    let response = this.openai.chat.completions.create({
        model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
        max_completion_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Go through the LLM response,for each choice, check if it has tool calls 
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
import { z } from "zod"; // Import zod for schema validation

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        const endpoint = process.env.AZURE_OPENAI_ENDPOINT;
        const apiKey = process.env.AZURE_OPENAI_API_KEY;
        if (!endpoint || !apiKey) {
            throw new Error("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set");
        }

        this.openai = new OpenAI({
            baseURL: `${endpoint.replace(/\/$/, "")}/openai/v1/`,
            apiKey,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {}
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
          // Create a zod schema based on the input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Explicitly set type to "function"
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
    
    
          // 2. Call the server's tool 
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Do something with the result
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
            model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-5.1",
            max_completion_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 3. Go through the LLM response, for each choice, check if it has tool calls 
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

1. Magdagdag tayo ng ilang imports na kailangan upang tawagan ang LLM

    ```python
    # llm
    import os
    from openai import OpenAI
    import json
    ```

2. Susunod, idagdag natin ang function na tatawag sa LLM. Ginagamit ng halimbawang ito ang
    aktibong `gpt-5.1` model. Tingnan ang
    [Microsoft Foundry model retirement schedule](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
    kapag pumipili ng modelo para sa iyong aplikasyon.

    ```python
    # llm

    def call_llm(prompt, functions):
        client = OpenAI(
            base_url=(
                f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/"
            ),
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
        )

        print("CALLING LLM")
        response = client.chat.completions.create(
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
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.1"),
            tools=functions,
            max_completion_tokens=1000,
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

    Sa naunang code kami ay:

    - Ipinasa ang ating mga functions, na nakuha mula sa MCP server at na-convert, sa LLM.
    - Tinawag ang LLM gamit ang mga nasabing functions.
    - Sinusuri ang resulta upang makita kung anong functions ang dapat tawagin, kung meron man.
    - Sa wakas, ipinapasa ang array ng mga function na tatawagin.

3. Panghuling hakbang, i-update natin ang pangunahing code:

    ```python
    prompt = "Add 2 to 20"

    # ask LLM what tools to all, if any
    functions_to_call = call_llm(prompt, functions)

    # call suggested functions
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Narito na, iyon ang panghuling hakbang, sa code sa itaas kami ay:

    - Tumawag sa MCP tool sa pamamagitan ng `call_tool` gamit ang function na naisip ng LLM na dapat nating tawagin base sa prompt.
    - Ipininatala ang resulta ng tawag sa tool sa MCP Server.

#### .NET

1. Ipakita natin ang code para sa paggawa ng request sa LLM prompt:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new UserChatMessage(userMessage));


    // 2. Define options, including the tools
    var options = new ChatCompletionOptions
    {
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
    var content = response.Content.FirstOrDefault()?.Text;

    ```

    Sa naunang code kami ay:

    - Nakuha ang mga kasangkapan mula sa server ng MCP, `var tools = await GetMcpTools()`.
    - Nagtakda ng isang user prompt `userMessage`.
    - Nilikha ang isang options object na naglalarawan ng modelo at mga kasangkapan.
    - Nagsagawa ng kahilingan patungo sa LLM.

2. Isang huling hakbang, tingnan natin kung iniisip ng LLM na dapat tayong tumawag ng isang function:

    ```csharp
    // 4. Check if the response contains a function call
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
        var result = await mcpClient.CallToolAsync(
            call.FunctionName,
            dict!,
            cancellationToken: CancellationToken.None
        );

        var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
        if (textBlock != null)
        {
            Console.WriteLine(textBlock.Text);
        }

    }
    ```

    Sa naunang code ay:

    - Nag-loop sa isang listahan ng mga function calls.
    - Para sa bawat pagtawag ng tool, hinati ang pangalan at mga argumento at tinawag ang tool sa MCP server gamit ang MCP client. Sa huli, ipinapakita namin ang mga resulta.

Narito ang buong code:

```csharp
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;
using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using System.Text.Json;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT");
var apiKey = Environment.GetEnvironmentVariable("AZURE_OPENAI_API_KEY");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5.1";
if (string.IsNullOrWhiteSpace(endpoint) || string.IsNullOrWhiteSpace(apiKey))
{
    Console.WriteLine("Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY.");
    return;
}

var client = new ChatClient(
    model: deployment,
    credential: new ApiKeyCredential(apiKey),
    options: new OpenAIClientOptions
    {
        Endpoint = new Uri($"{endpoint.TrimEnd('/')}/openai/v1/")
    });
var chatHistory = new List<ChatMessage>
{
    new SystemChatMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net9.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatTool ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    return ChatTool.CreateFunctionTool(
        functionName: name,
        functionDescription: description,
        functionParameters: BinaryData.FromString(jsonElement.GetRawText()));
}

async Task<List<ChatTool>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatTool> toolDefinitions = [];

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        var def = ConvertFrom(tool.Name, tool.Description, tool.JsonSchema);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
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

chatHistory.Add(new UserChatMessage(userMessage));

// 3. Define options, including the tools
var options = new ChatCompletionOptions
{
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletion response = await client.CompleteChatAsync(chatHistory, options);
var content = response.Content.FirstOrDefault()?.Text;

// 5. Check if the response contains a function call
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.FunctionName} with arguments {call.FunctionArguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.FunctionArguments);
    var result = await mcpClient.CallToolAsync(
        call.FunctionName,
        dict!,
        cancellationToken: CancellationToken.None
    );

    var textBlock = result.Content.OfType<TextContentBlock>().FirstOrDefault();
    if (textBlock != null)
    {
        Console.WriteLine(textBlock.Text);
    }

}

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Execute natural language requests that automatically use MCP tools
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

Sa naunang code ay:

- Gumamit ng simpleng natural language prompts para makipag-ugnayan sa mga MCP server tools
- Awtomatikong hinahandle ng LangChain4j framework ang:
  - Pag-convert ng mga user prompts sa tool calls kung kinakailangan
  - Pagtawag sa naaangkop na mga MCP tools batay sa desisyon ng LLM
  - Pamamahala ng daloy ng pag-uusap sa pagitan ng LLM at MCP server
- Ang `bot.chat()` na pamamaraan ay nagbabalik ng mga sagot sa natural na wika na maaaring magsama ng mga resulta mula sa MCP tool executions
- Nagbibigay ang ganitong pamamaraan ng seamless user experience kung saan hindi kailangang malaman ng mga gumagamit ang tungkol sa likod ng MCP implementation

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

Dito nangyayari ang karamihan sa trabaho. Tatawagin natin ang LLM gamit ang unang user prompt, pagkatapos ay ipoproseso ang sagot upang makita kung kinakailangan bang tumawag ng anumang mga tool. Kung oo, tatawagin natin ang mga tool na iyon at ipagpapatuloy ang pag-uusap sa LLM hanggang wala nang kailangang tawaging mga tool at mayroon na tayong panghuling sagot.

Gumagawa tayo ng maraming tawag sa LLM, kaya't magde-define tayo ng isang function na hahawak sa tawag ng LLM. Idagdag ang sumusunod na function sa iyong `main.rs` na file:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let model = std::env::var("AZURE_OPENAI_DEPLOYMENT")
        .unwrap_or_else(|_| "gpt-5.1".to_string());
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": model,
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

Tumatanggap ang function na ito ng LLM client, isang listahan ng mga mensahe (kabilang ang user prompt), mga tool mula sa MCP server, at nagpapadala ng kahilingan sa LLM, at nagbabalik ng sagot.

Ang sagot mula sa LLM ay naglalaman ng isang array ng `choices`. Kailangan natin iproseso ang resulta upang makita kung mayroong mga `tool_calls`. Ipinapaalam nito sa atin na humihiling ang LLM na tumawag ng isang partikular na tool na may mga argumento. Idagdag ang sumusunod na code sa ibaba ng iyong `main.rs` na file upang idefine ang isang function na hahawak sa sagot ng LLM:

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

    // Print content if available
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Handle tool calls
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Add assistant message

        // Execute each tool call
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Add tool result to messages
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Continue conversation with tool results
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

Kung may mga `tool_calls`, kinukuha nito ang impormasyon ng tool, tinatawagan ang MCP server gamit ang tool request, at idinadagdag ang mga resulta sa mga mensahe ng pag-uusap. Pagkatapos ay ipinagpapatuloy ang pag-uusap sa LLM at ina-update ang mga mensahe gamit ang sagot ng assistant at mga resulta ng pagtawag sa tool.

Upang makuha ang impormasyon ng pagtawag sa tool na ibinabalik ng LLM para sa mga MCP calls, magdadagdag tayo ng isa pang helper function upang makuha ang lahat ng kinakailangan upang gawin ang tawag. Idagdag ang sumusunod na code sa ibaba ng iyong `main.rs` na file:

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

Sa pagkakaroon ng lahat ng bahagi, maaari na nating hawakan ang unang user prompt at tawagin ang LLM. I-update ang iyong `main` function upang isama ang sumusunod na code:

```rust
// LLM conversation with tool calls
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

Itatanong nito ang LLM gamit ang unang user prompt na naghihingi ng sum ng dalawang numero, at ipoproseso ang sagot upang dinamiko na hawakan ang mga tool calls.

Magaling, nagawa mo ito!

## Assignment

Kunin ang code mula sa exercise at palawakin ang server gamit ang ilan pang mga tool. Pagkatapos gumawa ng client gamit ang isang LLM, tulad sa exercise, at subukan ito gamit ang iba't ibang prompt upang masiguro na ang lahat ng mga tool ng server ay natatawag nang dinamiko. Ang ganitong paraan ng paggawa ng client ay nangangahulugan na magkakaroon ng mahusay na karanasan ang end user dahil maaari silang gumamit ng mga prompt, sa halip na eksaktong mga utos ng client, at hindi malalaman na may tinatawag na MCP server.

## Solution

[Solusyon](./solution/README.md)

## Key Takeaways

- Ang pagdagdag ng LLM sa iyong client ay nagbibigay ng mas magandang paraan para makipag-ugnayan ang mga user sa MCP Servers.
- Kailangan mong i-convert ang tugon ng MCP Server sa isang bagay na maiintindihan ng LLM.

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Karagdagang Mga Mapagkukunan

## Ano Ang Susunod

- Susunod: [Consuming a server using Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->