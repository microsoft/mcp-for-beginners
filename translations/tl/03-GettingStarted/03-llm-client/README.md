# Paglikha ng kliyente gamit ang LLM

Sa ngayon, nakita mo na kung paano gumawa ng server at isang kliyente. Ang kliyente ay nakakapag-tawag sa server nang hayagan upang ilista ang mga tools, resources, at prompts nito. Gayunpaman, hindi ito isang praktikal na paraan. Ang iyong mga user ay nabubuhay sa panahon ng agentic at inaasahan nilang gumamit ng mga prompt at makipag-ugnayan sa isang LLM sa halip. Hindi nila iniintindi kung ginagamit mo ang MCP upang iimbak ang iyong mga kakayahan; inaasahan lang nila na makipag-ugnayan gamit ang natural na wika. Paano natin ito sosolusyunan? Ang solusyon ay magdagdag ng LLM sa kliyente.

## Pangkalahatang-ideya

Sa araling ito ay tututok tayo sa pagdaragdag ng LLM para sa iyong kliyente at ipapakita kung paano ito nagbibigay ng mas magandang karanasan para sa iyong user.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Gumawa ng isang kliyente na may LLM.
- Makipag-ugnayan nang tuloy-tuloy sa isang MCP server gamit ang LLM.
- Magbigay ng mas mahusay na karanasan sa end user sa panig ng kliyente.

## Paraan

Subukan nating intindihin ang kailangang gawin. Ang pagdagdag ng LLM ay tila simple, ngunit gagawin ba talaga natin ito?

Ganito makikipag-ugnayan ang kliyente sa server:

1. Magtatag ng koneksyon sa server.

1. Ililista ang mga kakayahan, prompt, resources, at tools, at isi-save ang kanilang schema.

1. Magdadagdag ng LLM at ipapasa ang mga na-save na kakayahan at ang kanilang schema sa format na naiintindihan ng LLM.

1. Pangasiwaan ang user prompt sa pamamagitan ng pagpapasa nito sa LLM kasama ang mga tools na inilista ng kliyente.

Maganda, ngayon na naiintindihan natin kung paano ito gagawin sa mataas na antas, subukan natin ito sa sumusunod na ehersisyo.

## Ehersisyo: Paglikha ng kliyente na may LLM

Sa ehersisyong ito, matututuhan nating magdagdag ng LLM sa ating kliyente.

### Authentication gamit ang GitHub Personal Access Token

Ang paggawa ng GitHub token ay isang diretso na proseso. Ganito mo ito magagawa:

- Pumunta sa GitHub Settings – I-click ang iyong larawan sa profile sa kanang itaas na sulok at piliin ang Settings.
- Pumunta sa Developer Settings – Mag-scroll pababa at i-click ang Developer Settings.
- Piliin ang Personal Access Tokens – I-click ang Fine-grained tokens at pagkatapos ay Generate new token.
- I-configure ang Iyong Token – Magdagdag ng tala para reference, itakda ang expiration date, at piliin ang mga kinakailangang scopes (permissions). Sa kasong ito, siguraduhing idagdag ang Models permission.
- I-generate at kopyahin ang Token – I-click ang Generate token, at siguraduhing kopyahin ito agad, dahil hindi mo na ito makikita muli.

### -1- Kumonekta sa server

Gawin muna nating client natin:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // I-import ang zod para sa pagpapatunay ng schema

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

Sa naunang code ay:

- Nag-import ng mga kailangan na libraries
- Gumawa ng isang klase na may dalawang miyembro, `client` at `openai` na tutulong sa amin pamahalaan ang kliyente at makipag-ugnayan sa isang LLM nang naaayon.
- In-configure ang aming LLM instance upang gamitin ang GitHub Models sa pamamagitan ng pagtatakda ng `baseUrl` upang ituro sa inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Lumikha ng mga parametro ng server para sa koneksyon ng stdio
server_params = StdioServerParameters(
    command="mcp",  # Naaandar
    args=["run", "server.py"],  # Mga opsyonal na argumento ng command line
    env=None,  # Mga opsyonal na variable ng kapaligiran
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Simulan ang koneksyon
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Sa naunang code ay:

- Nag-import ng mga kinakailangang libraries para sa MCP
- Nilikha ang isang kliyente

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

Una, kailangan mong idagdag ang LangChain4j dependencies sa iyong `pom.xml` file. Idagdag ang mga dependencies na ito para paganahin ang MCP integration at suporta sa GitHub Models:

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

Pagkatapos, gawin ang iyong Java client class:

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
    
    public static void main(String[] args) throws Exception {        // I-configure ang LLM upang gamitin ang mga Modelo ng GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
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
}
```

Sa naunang code:

- **Nagdagdag ng LangChain4j dependencies**: Kinakailangan para sa MCP integration, opisyal na OpenAI client, at suporta sa GitHub Models
- **Nag-import ng LangChain4j libraries**: Para sa MCP integration at OpenAI chat model functionality
- **Nilikha ang isang `ChatLanguageModel`**: Na naka-configure upang gumamit ng GitHub Models gamit ang iyong GitHub token
- **Nagatakda ng HTTP transport**: Gamit ang Server-Sent Events (SSE) para kumonekta sa MCP server
- **Nilikha ang MCP client**: Na maghahandle ng komunikasyon sa server
- **Gumamit ng LangChain4j's built-in MCP support**: Na nagpapadali ng integrasyon sa pagitan ng LLMs at MCP servers

#### Rust

Ipinapalagay na mayroon kang Rust-based MCP server na tumatakbo. Kung wala pa, tumingin sa [01-first-server](../01-first-server/README.md) na aralin para gumawa ng server.

Kapag mayroon ka nang Rust MCP server, buksan ang terminal at mag-navigate sa parehong direktoryo ng server. Pagkatapos ay patakbuhin ang sumusunod na utos upang gumawa ng bagong LLM client project:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Idagdag ang sumusunod na dependencies sa iyong `Cargo.toml` file:

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
    // Panimulang mensahe
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

    // TODO: Kunin ang listahan ng MCP tool

    // TODO: Pag-uusap ng LLM gamit ang mga tawag sa tool

    Ok(())
}
```

Ang code na ito ay nagse-set up ng basic na Rust application na kumokonekta sa MCP server at GitHub Models para sa pakikipag-ugnayan sa LLM.

> [!IMPORTANT]
> Siguraduhing naitakda mo na ang `OPENAI_API_KEY` environment variable gamit ang iyong GitHub token bago patakbuhin ang aplikasyon.

Maganda, para sa susunod na hakbang, ilista natin ang mga kakayahan ng server.

### -2- Ilista ang mga kakayahan ng server

Ngayon ay kumonekta tayo sa server at hilingin ang kanyang mga kakayahan:

#### Typescript

Sa parehong klase, idagdag ang mga sumusunod na method:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // naglilista ng mga kasangkapan
    const toolsResult = await this.client.listTools();
}
```

Sa naunang code ay:

- Nagdagdag ng code para kumonekta sa server, `connectToServer`.
- Nilikha ang method na `run` na responsable sa pagpapatakbo ng ating app flow. Sa ngayon, ito ay naglilista lang ng tools ngunit magdadagdag tayo ng iba pa rito.

#### Python

```python
# Ilahad ang mga magagamit na resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Ilahad ang mga magagamit na tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Narito ang mga idinagdag natin:

- Naglista ng resources at tools at pina-print ito. Para sa tools, nilista rin natin ang `inputSchema` na gagamitin natin sa susunod.

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

Sa naunang code ay:

- Nilista ang mga tools na available sa MCP Server
- Para sa bawat tool, nilista ang pangalan, paglalarawan, at ang schema nito. Ang huli ay gagamitin natin para tawagin ang tools sa susunod.

#### Java

```java
// Lumikha ng isang tagapagbigay ng tool na awtomatikong nakakakita ng mga MCP na tool
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Ang tagapagbigay ng MCP tool ay awtomatikong humahawak ng:
// - Paglilista ng mga magagamit na tool mula sa MCP server
// - Pagko-convert ng mga schema ng MCP tool sa format ng LangChain4j
// - Pamamahala sa pagpapatupad ng tool at mga tugon
```

Sa naunang code ay:

- Nilikha ang `McpToolProvider` na awtomatikong naghahanap at nagrerehistro ng lahat ng tools mula sa MCP server
- Ang tool provider ang naghahandle ng conversion sa pagitan ng MCP tool schemas at LangChain4j's tool format nang internal
- Pinapadali nito ang manual na paglista ng tools at conversion

#### Rust

Ang pagkuha ng tools mula sa MCP server ay ginagawa gamit ang `list_tools` method. Sa iyong `main` function, pagkatapos itakda ang MCP client, idagdag ang sumusunod na code:

```rust
// Kunin ang listahan ng MCP tool
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- I-convert ang mga kakayahan ng server sa mga LLM tools

Susunod na hakbang pagkatapos ilista ang mga kakayahan ng server ay i-convert ang mga ito sa format na nauunawaan ng LLM. Kapag nagawa na iyon, maibibigay natin ang mga kakayahan bilang mga tool sa LLM.

#### TypeScript

1. Idagdag ang sumusunod na code para i-convert ang response mula MCP Server sa tool format na magagamit ng LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Gumawa ng zod schema batay sa input_schema
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

    Ang code sa itaas ay kumukuha ng response mula sa MCP Server at kino-convert ito sa tool definition format na naiintindihan ng LLM.

1. I-update natin ang `run` method para ilista ang kakayahan ng server:

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

    Sa naunang code, in-update natin ang `run` method upang i-map ang result at sa bawat entry ay tawagin ang `openAiToolAdapter`.

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

1. Susunod, i-update natin ang kliyente upang gamitin ang function na ito tulad nito:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Dito, nagdagdag tayo ng tawag sa `convert_to_llm_tool` para i-convert ang MCP tool response sa format na pwede nating ipasa sa LLM sa hinaharap.

#### .NET

1. Magdagdag tayo ng code para i-convert ang MCP tool response sa format na naiintindihan ng LLM

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

Sa naunang code ay:

- Nilikha ang function na `ConvertFrom` na tumatanggap ng pangalan, paglalarawan, at input schema.
- Nagtakda ng funcionality na lumilikha ng FunctionDefinition na ipapasa sa ChatCompletionsDefinition. Ang huli ay naiintindihan ng LLM.

1. Tingnan naman natin kung paano i-update ang existing na code para gamitin ang function na ito:

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
// Lumikha ng isang Bot interface para sa interaksyong likas na wika
public interface Bot {
    String chat(String prompt);
}

// I-configure ang AI serbisyo gamit ang LLM at MCP na mga kasangkapan
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Sa naunang code ay:

- Nagtakda ng simpleng `Bot` interface para sa natural language interactions
- Ginamit ang LangChain4j's `AiServices` upang awtomatikong i-bind ang LLM sa MCP tool provider
- Ang framework ay awtomatikong naghahandle ng tool schema conversion at function calling sa likod ng eksena
- Pinapawi nito ang manual tool conversion - inaalagaan ng LangChain4j ang lahat ng komplikasyon sa pag-convert ng MCP tools sa LLM-compatible format

#### Rust

Para i-convert ang MCP tool response sa format na naiintindihan ng LLM, magdadagdag tayo ng helper function na nagfo-format ng tools listing. Idagdag ang sumusunod na code sa `main.rs` file mo sa ilalim ng `main` function. Tatawagin ito kapag gumagawa ng request sa LLM:

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

Maganda, handa na tayo para pangasiwaan ang mga user request, kaya gawin natin iyon sa susunod.

### -4- Pangasiwaan ang user prompt request

Sa bahaging ito ng code, pangasiwaan natin ang mga user request.

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


        // 2. Tawagan ang tool ng server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gawin ang isang bagay gamit ang resulta
        // GAGAWIN

        }
    }
    ```

    Sa naunang code ay:

    - Nagdagdag tayo ng method na `callTools`.
    - Tinitingnan ng method ang LLM response at sinusuri kung anong mga tools ang tinawag, kung meron man:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // tawagan ang kasangkapan
        }
        ```

    - Tumatawag ng tool, kung ipinaalam ng LLM na dapat ito tawagin:

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

1. I-update ang `run` method para isama ang mga tawag sa LLM at pagtawag ng `callTools`:

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

    // 3. Suriin ang tugon ng LLM, para sa bawat pagpipilian, tingnan kung mayroong pagtawag ng tool
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Maganda, narito ang buong code:

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
            baseURL: "https://models.inference.ai.azure.com", // maaaring kailanganing palitan ang url na ito sa hinaharap: https://models.github.ai/inference
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
            type: "function" as const, // Malinaw na itakda ang uri sa "function"
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
    
          // 3. Gawan ng aksyon ang resulta
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
    
        // 1. Suriin ang tugon ng LLM, para sa bawat pagpipilian, tingnan kung may tool calls ito
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

1. Magdagdag tayo ng mga import na kailangan para tumawag ng LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Susunod, idagdag ang function na tatawag sa LLM:

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

    Sa naunang code ay:

    - Ipinasa natin ang ating mga function, na nakuha mula sa MCP server at na-convert, sa LLM.
    - Tinawag natin ang LLM gamit ang mga nabanggit na function.
    - Sinuri natin ang resulta upang malaman kung anong mga function ang dapat tawagin, kung meron man.
    - Sa wakas, ipinapasa natin ang array ng mga function na tatawagin.

1. Huling hakbang, i-update ang pangunahing code:

    ```python
    prompt = "Add 2 to 20"

    # tanungin ang LLM kung anong mga kasangkapan ang kailangang gamitin, kung mayroon man
    functions_to_call = call_llm(prompt, functions)

    # tawagan ang mga mungkahing function
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Ayan, iyon ang huling hakbang, sa code sa itaas ay:

    - Tumatawag ng MCP tool gamit ang `call_tool` sa isang function na inirekomenda ng LLM base sa prompt.
    - Ini-print ang resulta ng tool call sa MCP Server.

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

    Sa naunang code ay:

    - Kumuha ng tools mula sa MCP server, `var tools = await GetMcpTools()`.
    - Nagtakda ng user prompt `userMessage`.
    - Gumawa ng options object na nagsasaad ng model at tools.
    - Nagpadala ng request sa LLM.

1. Huling hakbang, tingnan kung sa tingin ng LLM ay dapat itong tumawag ng isang function:

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

    Sa naunang code ay:

    - Nag-loop sa listahan ng function calls.
    - Para sa bawat tool call, pina-parse ang pangalan at arguments at tinawag ang tool sa MCP server gamit ang MCP client. Sa dulo, prinint ang mga resulta.

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

// 5. Print the generic response
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

Sa naunang code ay:

- Gumamit ng simpleng natural language prompts para makipag-ugnayan sa MCP server tools
- Awtomatikong hinahandle ng LangChain4j framework ang:
  - Pag-convert ng user prompts sa tool calls kapag kinakailangan
  - Pagtawag ng mga naaangkop na MCP tools base sa desisyon ng LLM
  - Pamamahala ng flow ng pag-uusap sa pagitan ng LLM at MCP server
- Nagbabalik ang `bot.chat()` method ng mga natural language responses na maaaring maglaman ng resulta mula sa pag-execute ng MCP tools
- Nagbibigay ito ng seamless user experience kung saan hindi na kailangang malaman ng user ang nakatagong implementasyon ng MCP

Kompletong halimbawa ng code:

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

Dito nangyayari ang karamihan ng trabaho. Tatawagin natin ang LLM gamit ang panimulang user prompt, pagkatapos ay ipoproseso ang sagot upang makita kung may mga tool na kailangang tawagin. Kung meron, tatawagin natin ang mga ito at ipagpapatuloy ang pag-uusap sa LLM hanggang wala nang kailangang tawaging tool at mayroon na tayong panghuling sagot.

Gagawa tayo ng maraming tawag sa LLM, kaya gumawa tayo ng function na maghahandle ng tawag sa LLM. Idagdag ang sumusunod na function sa `main.rs` file mo:

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

Ang function na ito ay tumatanggap ng LLM client, listahan ng mga mensahe (kasama ang user prompt), mga tools mula sa MCP server, at nagpapadala ng request sa LLM, at ibinabalik ang response.
Ang tugon mula sa LLM ay maglalaman ng isang array ng `choices`. Kailangan nating iproseso ang resulta upang makita kung mayroong anumang `tool_calls` na naroroon. Ipinapahiwatig nito na ang LLM ay humihiling na isang partikular na tool ay tatawagin na may mga argumento. Idagdag ang sumusunod na code sa ilalim ng iyong `main.rs` file upang tukuyin ang isang function para hawakan ang LLM response:

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

    // I-print ang nilalaman kung mayroon
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Pangasiwaan ang mga tawag sa tool
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Magdagdag ng mensahe ng assistant

        // Isa-isang isagawa ang bawat tawag sa tool
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

Kung mayroong `tool_calls`, kinukuha nito ang impormasyon ng tool, tinatawagan ang MCP server gamit ang kahilingan para sa tool, at idinadagdag ang mga resulta sa mga mensahe ng usapan. Pagkatapos ay nagpapatuloy ang usapan sa LLM at ang mga mensahe ay ina-update gamit ang tugon ng assistant at mga resulta ng tool call.

Para makuha ang impormasyon ng tool call na ibinabalik ng LLM para sa mga MCP call, magdadagdag tayo ng isa pang helper function upang makuha lahat ng kailangan para gawin ang tawag. Idagdag ang sumusunod na code sa ilalim ng iyong `main.rs` file:

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

Sa pagkakaroon ng lahat ng bahagi, maaari na nating hawakan ang unang prompt ng user at tawagin ang LLM. I-update ang iyong `main` function upang isama ang sumusunod na code:

```rust
// Usapan ng LLM na may tawag sa mga kasangkapan
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

Ito ay magtatanong sa LLM gamit ang unang prompt ng user na humihiling ng kabuuan ng dalawang numero, at ipoproseso nito ang tugon upang dinamiko na hawakan ang mga tawag sa tool.

Mahusay, nagawa mo na!

## Takdang-Aralin

Kunin ang code mula sa pagsasanay at palawakin ang server gamit pa ang iba pang mga tool. Pagkatapos gumawa ng client na may LLM, tulad ng sa pagsasanay, at subukan ito gamit ang iba't ibang prompt upang masiguro na lahat ng iyong mga tool sa server ay tawagin nang dinamiko. Ang ganitong paraan ng paggawa ng client ay nangangahulugan na ang end user ay magkakaroon ng mahusay na karanasan dahil maaari silang gumamit ng mga prompt, sa halip na eksaktong mga utos ng client, at hindi malalaman na may anumang MCP server na tinatawag.

## Solusyon

[Solusyon](./solution/README.md)

## Pangunahing Mga Aral

- Ang pagdagdag ng LLM sa iyong client ay nagbibigay ng mas mahusay na paraan para makipag-ugnayan ang mga gumagamit sa MCP Servers.
- Kailangan mong i-convert ang tugon mula sa MCP Server sa isang bagay na maiintindihan ng LLM.

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Karagdagang Mga Mapagkukunan

## Ano Ang Susunod

- Susunod: [Pagkonsumo ng server gamit ang Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggal ng Pananagutan**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing pinagmumulan. Para sa mga mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->