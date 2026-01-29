# Paglikha ng kliyente gamit ang LLM

Sa ngayon, nakita mo na kung paano gumawa ng server at kliyente. Nakapag-call na ang kliyente sa server nang tahasan upang ilista ang mga tools, resources, at prompts nito. Gayunpaman, hindi ito masyadong praktikal na paraan. Ang iyong user ay nabubuhay sa agentic era at inaasahan na gagamit ng prompts at makikipag-ugnayan sa isang LLM para gawin ito. Para sa iyong user, hindi mahalaga kung gagamit ka ng MCP o hindi para iimbak ang iyong mga kakayahan ngunit inaasahan nilang gagamit ng natural na wika sa pakikipag-ugnayan. Paano natin ito sosolusyunan? Ang solusyon ay ang pagdagdag ng LLM sa kliyente.

## Pangkalahatang-ideya

Sa araling ito, tututok tayo sa pagdagdag ng LLM sa iyong kliyente at ipapakita kung paano ito nagbibigay ng mas magandang karanasan para sa iyong user.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Gumawa ng kliyente na may LLM.
- Makipag-ugnayan nang tuloy-tuloy sa MCP server gamit ang LLM.
- Magbigay ng mas magandang karanasan sa end user sa panig ng kliyente.

## Paraan

Subukan nating unawain ang paraan na kailangan nating gawin. Ang pagdagdag ng LLM ay tila simple, pero gagawin ba talaga natin ito?

Ganito makikipag-ugnayan ang kliyente sa server:

1. Magtatag ng koneksyon sa server.

1. Ililista ang mga kakayahan, prompts, resources, at tools, at ise-save ang kanilang schema.

1. Magdadagdag ng LLM at ipapasa ang mga na-save na kakayahan at schema sa format na naiintindihan ng LLM.

1. Haharapin ang prompt ng user sa pamamagitan ng pagpapasa nito sa LLM kasama ang mga tools na nilista ng kliyente.

Magaling, ngayon naintindihan natin kung paano ito gagawin sa mataas na antas, subukan natin ito sa sumusunod na ehersisyo.

## Ehersisyo: Paglikha ng kliyente na may LLM

Sa ehersisyong ito, matututuhan natin kung paano magdagdag ng LLM sa ating kliyente.

### Pag-authenticate gamit ang GitHub Personal Access Token

Ang paggawa ng GitHub token ay isang diretso na proseso. Ganito ang paraan:

- Pumunta sa GitHub Settings – I-click ang iyong larawan sa profile sa kanang itaas na sulok at piliin ang Settings.
- Pumunta sa Developer Settings – Mag-scroll pababa at i-click ang Developer Settings.
- Piliin ang Personal Access Tokens – I-click ang Fine-grained tokens at pagkatapos ay Generate new token.
- I-configure ang Iyong Token – Magdagdag ng tala para sa reference, magtakda ng expiration date, at piliin ang mga kinakailangang scopes (permissions). Sa kasong ito, siguraduhing idagdag ang Models permission.
- I-generate at Kopyahin ang Token – I-click ang Generate token, at siguraduhing kopyahin ito agad dahil hindi mo na ito makikita muli.

### -1- Kumonekta sa server

Gumawa muna tayo ng ating kliyente:

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

Sa naunang code ay:

- Inimport ang mga kinakailangang libraries
- Gumawa ng klase na may dalawang miyembro, `client` at `openai` na tutulong sa atin na pamahalaan ang kliyente at makipag-ugnayan sa LLM nang magkahiwalay.
- Kinonpigura ang ating LLM instance upang gamitin ang GitHub Models sa pamamagitan ng pagtatakda ng `baseUrl` na tumutukoy sa inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Gumawa ng mga parameter ng server para sa koneksyon ng stdio
server_params = StdioServerParameters(
    command="mcp",  # Maaaring patakbuhin
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

Sa naunang code ay:

- Inimport ang mga kinakailangang libraries para sa MCP
- Gumawa ng kliyente

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

Una, kailangan mong idagdag ang LangChain4j dependencies sa iyong `pom.xml` file. Idagdag ang mga dependencies na ito upang paganahin ang MCP integration at suporta sa GitHub Models:

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

Pagkatapos ay gumawa ng iyong Java client class:

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
}
```

Sa naunang code ay:

- **Idinagdag ang LangChain4j dependencies**: Kinakailangan para sa MCP integration, opisyal na OpenAI client, at suporta sa GitHub Models
- **Inimport ang LangChain4j libraries**: Para sa MCP integration at OpenAI chat model functionality
- **Gumawa ng `ChatLanguageModel`**: Kinonpigura upang gamitin ang GitHub Models gamit ang iyong GitHub token
- **Nagtakda ng HTTP transport**: Gamit ang Server-Sent Events (SSE) para kumonekta sa MCP server
- **Gumawa ng MCP client**: Na siyang hahawak ng komunikasyon sa server
- **Gumamit ng built-in MCP support ng LangChain4j**: Na nagpapadali ng integrasyon sa pagitan ng LLMs at MCP servers

#### Rust

Ang halimbawang ito ay nagpapalagay na mayroon kang Rust-based MCP server na tumatakbo. Kung wala ka pa, balikan ang [01-first-server](../01-first-server/README.md) na aralin upang gumawa ng server.

Kapag mayroon ka nang Rust MCP server, buksan ang terminal at pumunta sa parehong direktoryo ng server. Pagkatapos patakbuhin ang sumusunod na utos upang gumawa ng bagong LLM client project:

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

    // TODO: Usapan ng LLM gamit ang mga tawag sa tool

    Ok(())
}
```

Itinatakda ng code na ito ang isang basic na Rust application na kokonekta sa MCP server at GitHub Models para sa pakikipag-ugnayan sa LLM.

> [!IMPORTANT]
> Siguraduhing itakda ang `OPENAI_API_KEY` environment variable gamit ang iyong GitHub token bago patakbuhin ang application.

Magaling, para sa susunod na hakbang, ilista natin ang mga kakayahan sa server.

### -2- Ilista ang mga kakayahan ng server

Ngayon ay kokonekta tayo sa server at hihingin ang mga kakayahan nito:

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

    // paglista ng mga kasangkapan
    const toolsResult = await this.client.listTools();
}
```

Sa naunang code ay:

- Idinagdag ang code para kumonekta sa server, `connectToServer`.
- Gumawa ng `run` method na responsable sa paghawak ng daloy ng app. Sa ngayon, nililista lang nito ang mga tools pero magdadagdag tayo ng iba pa dito sa lalong madaling panahon.

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

Ito ang idinagdag natin:

- Paglilista ng mga resources at tools at pag-print ng mga ito. Para sa tools, nililista rin natin ang `inputSchema` na gagamitin natin mamaya.

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
- Para sa bawat tool, nilista ang pangalan, deskripsyon, at ang schema nito. Ang huli ay gagamitin natin para tawagan ang mga tools sa lalong madaling panahon.

#### Java

```java
// Lumikha ng isang tagapagbigay ng tool na awtomatikong naghahanap ng mga MCP tool
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Ang tagapagbigay ng MCP tool ay awtomatikong humahawak ng:
// - Paglilista ng mga magagamit na tool mula sa MCP server
// - Pag-convert ng mga schema ng MCP tool sa format ng LangChain4j
// - Pamamahala ng pagpapatupad ng tool at mga tugon
```

Sa naunang code ay:

- Gumawa ng `McpToolProvider` na awtomatikong naghahanap at nagrerehistro ng lahat ng tools mula sa MCP server
- Ang tool provider ang humahawak ng conversion sa pagitan ng MCP tool schemas at LangChain4j's tool format nang internal
- Ang paraang ito ay nag-aalis ng manual na proseso ng paglista at conversion ng tools

#### Rust

Ang pagkuha ng mga tools mula sa MCP server ay ginagawa gamit ang `list_tools` method. Sa iyong `main` function, pagkatapos i-setup ang MCP client, idagdag ang sumusunod na code:

```rust
// Kunin ang listahan ng MCP tool
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- I-convert ang mga kakayahan ng server sa mga tool ng LLM

Susunod na hakbang pagkatapos ilista ang mga kakayahan ng server ay i-convert ang mga ito sa format na naiintindihan ng LLM. Kapag nagawa na natin ito, maibibigay natin ang mga kakayahang ito bilang mga tools sa ating LLM.

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

    Kinukuha ng code sa itaas ang response mula sa MCP Server at kino-convert ito sa tool definition format na naiintindihan ng LLM.

1. I-update natin ang `run` method upang ilista ang mga kakayahan ng server:

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

    Sa function na `convert_to_llm_tools` ay kinukuha natin ang MCP tool response at kino-convert ito sa format na naiintindihan ng LLM.

1. Susunod, i-update natin ang ating client code upang gamitin ang function na ito tulad nito:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Dito, nagdagdag tayo ng tawag sa `convert_to_llm_tool` upang i-convert ang MCP tool response sa isang bagay na maaari nating ipasa sa LLM mamaya.

#### .NET

1. Idagdag natin ang code para i-convert ang MCP tool response sa isang bagay na naiintindihan ng LLM

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

- Gumawa ng function na `ConvertFrom` na tumatanggap ng pangalan, deskripsyon, at input schema.
- Nagdefine ng functionality na lumilikha ng FunctionDefinition na ipinapasa sa ChatCompletionsDefinition. Ang huli ay naiintindihan ng LLM.

1. Tingnan natin kung paano natin ma-update ang ilang umiiral na code upang magamit ang function na ito:

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

// I-configure ang AI service gamit ang LLM at MCP na mga tool
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Sa naunang code ay:

- Nagdefine ng simpleng `Bot` interface para sa natural language interactions
- Ginamit ang LangChain4j's `AiServices` upang awtomatikong i-bind ang LLM sa MCP tool provider
- Awtomatikong hinahandle ng framework ang tool schema conversion at function calling sa likod ng mga eksena
- Inaalis ng paraang ito ang manual na conversion ng tools - ang LangChain4j ang humahawak sa lahat ng komplikasyon ng pag-convert ng MCP tools sa LLM-compatible na format

#### Rust

Para i-convert ang MCP tool response sa format na naiintindihan ng LLM, magdadagdag tayo ng helper function na nagfo-format ng tools listing. Idagdag ang sumusunod na code sa iyong `main.rs` file sa ilalim ng `main` function. Tatawagin ito kapag gumagawa ng mga request sa LLM:

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

Magaling, handa na tayo para harapin ang mga user request, kaya gawin natin iyon sa susunod.

### -4- Harapin ang user prompt request

Sa bahaging ito ng code, haharapin natin ang mga request ng user.

#### TypeScript

1. Magdagdag ng method na gagamitin para tawagan ang ating LLM:

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

    - Nagdagdag ng method na `callTools`.
    - Tinitingnan ng method ang response ng LLM upang alamin kung anong mga tools ang tinawag, kung mayroon man:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // tawagan ang kasangkapan
        }
        ```

    - Tinatawag ang isang tool, kung sinasabi ng LLM na dapat itong tawagin:

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

1. I-update ang `run` method upang isama ang mga tawag sa LLM at pagtawag sa `callTools`:

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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Suriin ang sagot ng LLM, para sa bawat pagpipilian, tingnan kung may mga tawag sa tool
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Magaling, ilista natin ang buong code:

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
            baseURL: "https://models.inference.ai.azure.com", // maaaring kailanganin baguhin sa url na ito sa hinaharap: https://models.github.ai/inference
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
            type: "function" as const, // Tahasang itakda ang type sa "function"
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Suriin ang sagot ng LLM, para sa bawat pagpipilian, tingnan kung may tool calls
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

1. Magdagdag tayo ng ilang imports na kailangan para tawagan ang LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Susunod, idagdag natin ang function na tatawag sa LLM:

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

    Sa naunang code ay:

    - Ipinasa natin ang mga functions na nahanap natin sa MCP server at na-convert sa LLM.
    - Tinawag natin ang LLM gamit ang mga nasabing functions.
    - Sinusuri natin ang resulta upang makita kung anong functions ang dapat tawagin, kung mayroon man.
    - Sa huli, ipinapasa natin ang array ng mga functions na tatawagin.

1. Panghuling hakbang, i-update natin ang ating main code:

    ```python
    prompt = "Add 2 to 20"

    # tanungin ang LLM kung anong mga kasangkapan ang lahat, kung mayroon man
    functions_to_call = call_llm(prompt, functions)

    # tawagan ang mga iminungkahing function
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Doon, iyon ang panghuling hakbang, sa code sa itaas ay:

    - Tinatawag ang MCP tool via `call_tool` gamit ang function na inisip ng LLM na dapat tawagin base sa ating prompt.
    - Ipiniprint ang resulta ng tool call sa MCP Server.

#### .NET

1. Ipakita natin ang ilang code para sa paggawa ng LLM prompt request:

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

    Sa naunang code ay:

    - Kinuha ang mga tools mula sa MCP server, `var tools = await GetMcpTools()`.
    - Nagdefine ng user prompt `userMessage`.
    - Gumawa ng options object na nagsasaad ng model at tools.
    - Gumawa ng request papunta sa LLM.

1. Huling hakbang, tingnan natin kung iniisip ng LLM na dapat tayong tumawag ng function:

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
    - Para sa bawat tool call, kinukuha ang pangalan at mga argumento at tinatawagan ang tool sa MCP server gamit ang MCP client. Sa huli, ipiniprint ang mga resulta.

Narito ang buong code:

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
  - Pagtawag sa angkop na MCP tools base sa desisyon ng LLM
  - Pamamahala ng daloy ng pag-uusap sa pagitan ng LLM at MCP server
- Ang `bot.chat()` method ay nagbabalik ng natural language responses na maaaring kasama ang mga resulta mula sa pagpapatakbo ng MCP tools
- Nagbibigay ang paraang ito ng tuloy-tuloy na karanasan sa user kung saan hindi na nila kailangang malaman ang likod ng MCP implementation

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

Dito nangyayari ang karamihan ng trabaho. Tatawagin natin ang LLM gamit ang unang user prompt, pagkatapos ay ipoproseso ang response upang makita kung may mga tools na kailangang tawagin. Kung mayroon, tatawagin natin ang mga tools na iyon at ipagpapatuloy ang pag-uusap sa LLM hanggang wala nang kailangang tawaging tool at mayroon na tayong panghuling sagot.

Gagawa tayo ng maraming tawag sa LLM, kaya magde-define tayo ng function na hahawak sa tawag sa LLM. Idagdag ang sumusunod na function sa iyong `main.rs` file:

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

Tumatanggap ang function na ito ng LLM client, listahan ng mga mensahe (kasama ang user prompt), mga tools mula sa MCP server, at nagpapadala ng request sa LLM, na nagbabalik ng response.
Ang tugon mula sa LLM ay maglalaman ng isang array ng `choices`. Kailangan nating iproseso ang resulta upang makita kung mayroong anumang `tool_calls`. Ipinapahiwatig nito na ang LLM ay humihiling na tawagan ang isang partikular na tool na may mga argumento. Idagdag ang sumusunod na code sa ibaba ng iyong `main.rs` file upang tukuyin ang isang function na hahawak sa tugon ng LLM:

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
        messages.push(message.clone()); // Magdagdag ng mensahe ng katulong

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

Kung mayroong `tool_calls`, kinukuha nito ang impormasyon ng tool, tinatawagan ang MCP server gamit ang kahilingan ng tool, at idinadagdag ang mga resulta sa mga mensahe ng pag-uusap. Pagkatapos ay ipinagpapatuloy ang pag-uusap sa LLM at ina-update ang mga mensahe gamit ang tugon ng assistant at mga resulta ng tawag sa tool.

Upang kunin ang impormasyon ng tawag sa tool na ibinabalik ng LLM para sa mga tawag sa MCP, magdadagdag tayo ng isa pang helper function upang kunin ang lahat ng kailangan upang gawin ang tawag. Idagdag ang sumusunod na code sa ibaba ng iyong `main.rs` file:

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

Sa pagkakaroon ng lahat ng bahagi, maaari na nating hawakan ang paunang prompt ng user at tawagan ang LLM. I-update ang iyong `main` function upang isama ang sumusunod na code:

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

Ito ay magtatanong sa LLM gamit ang paunang prompt ng user na humihiling ng kabuuan ng dalawang numero, at ipoproseso nito ang tugon upang dinamiko na hawakan ang mga tawag sa tool.

Magaling, nagawa mo na!

## Assignment

Kunin ang code mula sa ehersisyo at palawakin ang server gamit ang ilang karagdagang mga tool. Pagkatapos ay gumawa ng isang client na may LLM, tulad sa ehersisyo, at subukan ito gamit ang iba't ibang mga prompt upang matiyak na lahat ng iyong mga tool sa server ay tinatawag nang dinamiko. Ang ganitong paraan ng paggawa ng client ay nangangahulugan na magkakaroon ng mahusay na karanasan ang end user dahil maaari silang gumamit ng mga prompt, sa halip na eksaktong mga utos ng client, at hindi nila mapapansin ang anumang MCP server na tinatawag.

## Solution

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## Key Takeaways

- Ang pagdagdag ng LLM sa iyong client ay nagbibigay ng mas mahusay na paraan para sa mga user na makipag-ugnayan sa MCP Servers.
- Kailangan mong i-convert ang tugon ng MCP Server sa isang bagay na maiintindihan ng LLM.

## Samples

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Additional Resources

## What's Next

- Next: [Consuming a server using Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->