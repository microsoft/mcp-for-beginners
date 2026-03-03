# Paglikha ng kliyente gamit ang LLM

Sa ngayon, nakita mo kung paano gumawa ng server at isang kliyente. Ang kliyente ay nakapag-atawag nang tuwiran sa server para ilista ang mga tool, resources, at mga prompt nito. Gayunpaman, hindi ito isang praktikal na paraan. Ang iyong mga gumagamit ay nabubuhay sa panahon ng agentic at inaasahan nilang gamitin ang mga prompt at makipag-usap sa isang LLM. Hindi nila pinapansin kung ginamit mo ang MCP para iimbak ang iyong mga kakayahan; inaasahan nilang makipag-ugnayan gamit ang natural na wika. Paano natin ito sosolusyunan? Ang solusyon ay magdagdag ng isang LLM sa kliyente.

## Pangkalahatang-ideya

Sa araling ito, tututok tayo sa pagdaragdag ng isang LLM para sa iyong kliyente at ipapakita kung paano ito nagbibigay ng mas magandang karanasan para sa iyong gumagamit.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magiging kaya mong:

- Gumawa ng kliyente na may LLM.
- Magsagawa ng tuloy-tuloy na interaksyon sa isang MCP server gamit ang LLM.
- Magbigay ng mas magandang karanasan sa end user sa bahagi ng kliyente.

## Pamamaraan

Subukan nating unawain ang pamamaraan na kailangan nating gawin. Ang pagdaragdag ng isang LLM ay tila simple, pero talaga ba natin ito gagawin?

Ganito ang pakikipag-ugnayan ng kliyente sa server:

1. Magtayo ng koneksyon sa server.

1. Ilista ang mga kakayahan, mga prompt, mga resources, at mga tool, at i-save ang kanilang schema.

1. Magdagdag ng isang LLM at ipasa ang mga naka-save na kakayahan pati na ang kanilang schema sa format na naiintindihan ng LLM.

1. Pamahalaan ang prompt ng gumagamit sa pamamagitan ng pagpapasa nito sa LLM kasabay ng mga tool na naka-lista ng kliyente.

Magaling, ngayon naiintindihan natin kung paano natin ito gagawin sa mataas na antas, subukan natin ito sa sumusunod na pagsasanay.

## Pagsasanay: Paglikha ng kliyente na may LLM

Sa pagsasanay na ito, matututuhan nating magdagdag ng LLM sa ating kliyente.

### Pag-authenticate gamit ang GitHub Personal Access Token

Ang paggawa ng GitHub token ay isang diretso na proseso. Ganito mo ito magagawa:

- Pumunta sa GitHub Settings – I-click ang iyong larawan ng profile sa kanang itaas na sulok at piliin ang Settings.
- Pumunta sa Developer Settings – Mag-scroll pababa at i-click ang Developer Settings.
- Piliin ang Personal Access Tokens – I-click ang Fine-grained tokens at pagkatapos ay Generate new token.
- I-configure ang Iyong Token – Magdagdag ng tala para reference, itakda ang expiration date, at piliin ang kinakailangang mga scope (mga permiso). Sa kasong ito ay siguraduhing idagdag ang Models permission.
- I-generate at Kopyahin ang Token – I-click ang Generate token, at siguraduhing kopyahin ito agad dahil hindi mo na ito makikita ulit.

### -1- Kumonekta sa server

Gumawa muna tayo ng ating kliyente:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // I-import ang zod para sa schema validation

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

Sa nakaraang code ay:

- In-import ang mga kinakailangang librarya
- Gumawa ng klase na may dalawang miyembro, `client` at `openai` na tutulong sa atin na pamahalaan ang isang kliyente at makipag-ugnayan sa isang LLM ayon sa pagkakabanggit.
- Ikinonpigura ang ating LLM instance upang gamitin ang GitHub Models sa pamamagitan ng pagtatakda ng `baseUrl` para tumuro sa inference API.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Gumawa ng mga parameter ng server para sa koneksyon ng stdio
server_params = StdioServerParameters(
    command="mcp",  # Maisasakatuparan
    args=["run", "server.py"],  # Opsyonal na mga argumento sa linya ng utos
    env=None,  # Opsyonal na mga variable ng kapaligiran
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

Sa nakaraang code ay:

- In-import ang mga kinakailangang librarya para sa MCP
- Lumilikha ng kliyente

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

Una, kailangan mong idagdag ang mga LangChain4j dependencies sa iyong `pom.xml` file. Idagdag ang mga dependencies na ito para payagan ang MCP integration at GitHub Models support:

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

Pagkatapos, gumawa ng iyong Java client class:

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
    
    public static void main(String[] args) throws Exception {        // I-configure ang LLM upang gamitin ang mga Modelong GitHub
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

Sa nakaraang code ay:

- **Idinagdag ang mga LangChain4j dependencies**: Kinakailangan para sa integrasyon ng MCP, opisyal na OpenAI client, at GitHub Models support
- **In-import ang mga LangChain4j librarya**: Para sa MCP integration at OpenAI chat model functionality
- **Gumawa ng `ChatLanguageModel`**: Nakikonpigura upang gamitin ang GitHub Models gamit ang iyong GitHub token
- **Naitakda ang HTTP transport**: Gamit ang Server-Sent Events (SSE) para kumonekta sa MCP server
- **Nagawa ang MCP client**: Na siyang humahawak ng komunikasyon sa server
- **Ginamit ang built-in MCP support ng LangChain4j**: Na nagpapadali ng integrasyon sa pagitan ng LLMs at MCP servers

#### Rust

Ang halimbawang ito ay nangangailangan na mayroon kang Rust based MCP server na tumatakbo. Kung wala pa, balikan ang leksyon na [01-first-server](../01-first-server/README.md) para gumawa ng server.

Kapag nakuha mo na ang Rust MCP server, buksan ang terminal at pumunta sa parehong directory kung nasaan ang server. Pagkatapos patakbuhin ang sumusunod na utos para gumawa ng bagong LLM client project:

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

Ang code na ito ay nagse-set up ng isang pangunahing Rust application na magkokonekta sa MCP server at GitHub Models para sa LLM interactions.

> [!IMPORTANT]
> Siguraduhing itakda ang `OPENAI_API_KEY` na environment variable gamit ang iyong GitHub token bago patakbuhin ang application.

Magaling, para sa ating susunod na hakbang, listahan ang mga kakayahan sa server.

### -2- Listahan ng kakayahan ng server

Ngayon ay kokonekta tayo sa server at hihilingin ang mga kakayahan nito:

#### Typescript

Sa parehong klase, idagdag ang sumusunod na mga method:

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

Sa nakaraang code ay:

- Idinagdag ang code para kumonekta sa server, `connectToServer`.
- Gumawa ng `run` na method na responsable sa paghawak ng daloy ng ating app. Sa ngayon inililista lamang nito ang mga tool ngunit magdaragdag tayo pa rito.

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

Narito ang idinagdag namin:

- Paglilista ng mga resources at tools at ipinrint ang mga ito. Para sa mga tool, nilista rin ang `inputSchema` na gagamitin natin mamaya.

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

Sa nakaraang code ay:

- Nilista ang mga tool na available sa MCP Server
- Para sa bawat tool, nilista ang pangalan, deskripsyon at ang schema nito. Ang huli ay gagamitin natin para tumawag sa mga tool sa lalong madaling panahon.

#### Java

```java
// Gumawa ng tagapagbigay ng tool na awtomatikong nakakakita ng mga MCP tool
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Ang tagapagbigay ng MCP tool ay awtomatikong humahawak ng:
// - Paglilista ng mga magagamit na tool mula sa MCP server
// - Pag-convert ng mga schema ng MCP tool sa format ng LangChain4j
// - Pamamahala ng pagpapatupad ng tool at mga sagot
```

Sa nakaraang code ay:

- Gumawa ng isang `McpToolProvider` na awtomatikong nagdi-discover at nagrerehistro ng lahat ng tool mula sa MCP server
- Ang tool provider ang humahawak ng conversion sa pagitan ng MCP tool schemas at tool format ng LangChain4j nang internal
- Binabawasan ng pamamaraang ito ang manual na paglilista at conversion ng tool

#### Rust

Ang pagkuha ng tool mula sa MCP server ay ginagawa gamit ang `list_tools` na method. Sa iyong `main` function, pagkatapos i-setup ang MCP client, idagdag ang sumusunod na code:

```rust
// Kunin ang listahan ng MCP tool
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- I-convert ang kakayahan ng server sa mga tool para sa LLM

Susunod na hakbang pagkatapos ilista ang kakayahan ng server ay i-convert ang mga ito sa format na naiintindihan ng LLM. Kapag nagawa na ito, maipapasa natin ang mga kakayahang ito bilang mga tool sa ating LLM.

#### TypeScript

1. Idagdag ang sumusunod na code para i-convert ang response mula sa MCP Server sa tool format na puwedeng gamitin ng LLM:

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

    Ang code sa itaas ay kumukuha ng tugon mula sa MCP Server at kino-convert ito sa isang tool definition format na naiintindihan ng LLM.

1. I-update naman natin ang `run` method upang ilista ang kakayahan ng server:

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

    Sa nakaraang code, in-update natin ang `run` method upang dumaan sa resulta at para sa bawat entry ay tawagin ang `openAiToolAdapter`.

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

1. Susunod, i-update natin ang kodigo ng kliyente gamit ang function na ito:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Dito, nagdagdag tayo ng tawag sa `convert_to_llm_tool` para i-convert ang response ng MCP tool sa isang bagay na maipapakain natin sa LLM mamaya.

#### .NET

1. Magdagdag tayo ng code upang i-convert ang response ng MCP tool sa isang bagay na naiintindihan ng LLM

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

Sa nakaraang code ay:

- Gumawa tayo ng function na `ConvertFrom` na tumatanggap ng pangalan, deskripsyon, at input schema.
- Itinakda ang functionality na lumilikha ng FunctionDefinition na ipapasa sa ChatCompletionsDefinition. Ang huli ay naiintindihan ng LLM.

1. Tingnan natin kung paano i-update ang ilang bahagi ng code upang samantalahin ang function na ito:

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

// I-configure ang AI serbisyo gamit ang LLM at MCP na mga kasangkapan
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Sa nakaraang code ay:

- Nagdefine ng simpleng `Bot` interface para sa natural language interactions
- Ginamit ang LangChain4j's `AiServices` upang awtomatikong i-bind ang LLM sa MCP tool provider
- Ang framework ay awtomatikong humahawak sa conversion ng tool schema at pagtawag ng function sa likod ng eksena
- Pinapawi nito ang manual tool conversion — hinahandle ng LangChain4j ang lahat ng komplikasyon ng pag-convert ng MCP tools sa LLM-compatible na format

#### Rust

Para i-convert ang MCP tool response sa isang format na naiintindihan ng LLM, magdadagdag tayo ng helper function na nagfo-format ng listahan ng mga tool. Idagdag ang sumusunod na code sa iyong `main.rs` file sa ibaba ng `main` function. Ito ay tatawagin kapag gumagawa ng mga request sa LLM:

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

Magaling, handa na tayo para hawakan ang anumang request mula sa user, kaya gawin natin iyon sa susunod.

### -4- Hawakan ang prompt request ng gumagamit

Sa bahaging ito ng code, hahawakan natin ang mga request ng gumagamit.

#### TypeScript

1. Magdagdag ng metodo na gagamitin para tawagan ang ating LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Tawagin ang tool ng server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gawin ang isang bagay gamit ang resulta
        // TODO

        }
    }
    ```

    Sa nakaraang code ay:

    - Idinagdag ang method na `callTools`.
    - Tinitingnan ng method na ito ang response mula sa LLM kung anong mga tool ang tinawag, kung mayroon man:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // tawagin ang tool
        }
        ```

    - Tinatawag ang isang tool, kung sinasabi ng LLM na dapat iyon ang tawagin:

        ```typescript
        // 2. Tawagan ang kasangkapang server
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gawin ang isang bagay gamit ang resulta
        // TODO
        ```

1. I-update ang `run` method upang isama ang tawag sa LLM at pagtawag sa `callTools`:

    ```typescript

    // 1. Gumawa ng mga mensaheng input para sa LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Tawagan ang LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
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

Magaling, narito ang buong code:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Mag-import ng zod para sa pag-validate ng schema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // maaaring kailanganin baguhin ang url na ito sa hinaharap: https://models.github.ai/inference
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
            type: "function" as const, // Tiyaking itakda ang uri bilang "function"
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
    
    
          // 2. Tawagin ang tool ng server
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
    
        // 1. Suriin ang sagot ng LLM, para sa bawat pagpipilian, tingnan kung may tawag sa tool
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

1. Magdagdag tayo ng ilang import na kailangan para tumawag ng LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Ngayon naman, idagdag ang function na tatawag sa LLM:

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

    Sa nakaraang code ay:

    - Ipinasa natin ang mga functions na nahanap sa MCP server at na-convert natin sa LLM.
    - Tinawag natin ang LLM gamit ang mga nasabing function.
    - Sinusuri naman natin ang resulta para makita kung ano ang mga function na dapat tawagin, kung meron man.
    - Sa wakas, nagpasa tayo ng array ng mga function na tatawagin.

1. Panghuling hakbang, i-update ang ating pangunahing kodigo:

    ```python
    prompt = "Add 2 to 20"

    # tanungin ang LLM kung may mga gamit na dapat gamitin, kung meron man
    functions_to_call = call_llm(prompt, functions)

    # tawagan ang mga mungkahing function
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Yan ang huling hakbang, sa code sa itaas ay:

    - Tinawag ang MCP tool gamit ang `call_tool` gamit ang function na inisip ng LLM na dapat tawagin base sa prompt.
    - Ipiniprint ang resulta ng tool call sa MCP Server.

#### .NET

1. Ipakita natin ang ilang code para sa pag-request ng prompt ng LLM:

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

    Sa nakaraang code ay:

    - Kinuha ang mga tool mula sa MCP server, `var tools = await GetMcpTools()`.
    - Dinisenyo ang user prompt `userMessage`.
    - Gumawa ng options object na nagtatalaga ng modelo at mga tool.
    - Nagpadala ng kahilingan sa LLM.

1. Panghuling hakbang, tingnan kung sa palagay ng LLM ay dapat tayong tumawag ng isang function:

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

    Sa nakaraang code ay:

    - Nou-loop ang listahan ng function calls.
    - Para sa bawat tool call, pinuparse ang pangalan at argumento at tinawag ang tool sa MCP server gamit ang MCP client. Sa huli, priniprint ang mga resulta.

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
    // Isagawa ang mga kahilingan sa natural na wika na awtomatikong gumagamit ng mga kasangkapang MCP
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

Sa nakaraang code ay:

- Gumamit ng simpleng natural language prompts para makipag-ugnayan sa mga tool ng MCP server
- Awtomatikong humahawak ang LangChain4j framework ng:
  - Pag-convert ng user prompts sa tool calls kapag kinakailangan
  - Pagtawag sa tamang MCP tool base sa desisyon ng LLM
  - Pamamahala ng daloy ng pag-uusap sa pagitan ng LLM at MCP server
- Ang `bot.chat()` method ay nagbabalik ng natural language responses na maaaring may kasamang resulta mula sa pagpapatakbo ng mga MCP tool
- Nagbibigay ito ng tuloy-tuloy na karanasan sa gumagamit kung saan hindi kailangang malaman ng mga user ang tungkol sa likod-ng-tagpo na MCP implementation

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

Dito nangyayari ang karamihan sa trabaho. Tatawagin natin ang LLM gamit ang unang prompt mula sa user, pagkatapos ay ipoproseso ang sagot upang tingnan kung may kailangan bang tawagin na mga tool. Kung mayroon, tatawagin natin ang mga tool na iyon at ipagpapatuloy ang pag-uusap sa LLM hanggang sa wala nang ibang tool na kailangang tawagin at mayroon na tayong pangwakas na sagot.

Gagawa tayo ng maraming tawag sa LLM, kaya gumawa tayo ng function na hahawak sa tawag sa LLM. Idagdag ang sumusunod na function sa iyong `main.rs` file:

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

Ang function na ito ay tumatanggap ng LLM client, isang listahan ng mga mensahe (kasama ang prompt ng user), mga tool mula sa MCP server, at nagpapadala ng kahilingan sa LLM, pagkatapos ay ibinabalik ang sagot.
Ang tugon mula sa LLM ay maglalaman ng isang array ng `choices`. Kailangan nating iproseso ang resulta upang makita kung mayroon bang anumang `tool_calls`. Ipinapahiwatig nito na ang LLM ay humihiling na isang partikular na tool ay tatawagin kasama ang mga argumento. Idagdag ang sumusunod na code sa ilalim ng iyong `main.rs` file upang tukuyin ang isang function na hahawakan ang tugon ng LLM:

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

    // Huwag mag-handle ng mga tawag sa tool
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

Kung mayroong `tool_calls`, kinukuha nito ang impormasyon ng tool, tinatawagan ang MCP server gamit ang kahilingan ng tool, at idinadagdag ang mga resulta sa mga mensahe ng pag-uusap. Pagkatapos nito ay ipinagpapatuloy ang pag-uusap sa LLM at ang mga mensahe ay ina-update gamit ang tugon ng assistant at mga resulta ng pagtawag sa tool.

Upang makuha ang impormasyon ng pagtawag sa tool na ibinabalik ng LLM para sa mga MCP call, magdadagdag tayo ng isa pang helper function upang makuha ang lahat ng kailangan para gawin ang tawag. Idagdag ang sumusunod na code sa ilalim ng iyong `main.rs` file:

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

Sa lahat ng bahagi na nasa lugar na, maaari na nating hawakan ang unang prompt ng user at tawagan ang LLM. I-update ang iyong `main` function upang isama ang sumusunod na code:

```rust
// Usapan ng LLM na may mga tawag sa kagamitan
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

Ito ay magtatanong sa LLM gamit ang unang prompt ng user na humihiling ng kabuuan ng dalawang numero, at ipoproseso nito ang tugon upang dynamic na hawakan ang mga tawag sa tool.

Magaling, nagawa mo ito!

## Takdang Aralin

Kunin ang code mula sa ehersisyo at palawakin ang server gamit ang ilang iba pang mga tool. Pagkatapos gumawa ng isang client na may LLM, tulad ng sa ehersisyo, at subukan ito gamit ang iba't ibang mga prompt upang matiyak na lahat ng mga tool ng iyong server ay tinatawagan nang dynamic. Ang paraan ng paggawa ng isang client na ito ay nangangahulugan na magkakaroon ng mahusay na karanasan ang end user dahil magagamit nila ang mga prompt, sa halip na mga eksaktong command ng client, at hindi nila mapapansin ang anumang MCP server na tinatawag.

## Solusyon

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## Pangunahing Mga Natutuhan

- Ang pagdagdag ng LLM sa iyong client ay nagbibigay ng mas mahusay na paraan para makipag-ugnayan ang mga user sa MCP Servers.
- Kailangan mong i-convert ang tugon ng MCP Server sa isang bagay na maiintindihan ng LLM.

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Karagdagang Mga Mapagkukunan

## Ano ang Susunod

- Susunod: [Pagkonsumo ng server gamit ang Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami na maging tumpak, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring magmula sa paggamit ng salin na ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->