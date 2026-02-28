# Kuunda mteja mwenye LLM

Hadi sasa, umeona jinsi ya kuunda seva na mteja. Mteja amekuwa na uwezo wa kuita seva moja kwa moja ili kuorodhesha zana zake, rasilimali, na maelezo ya kuanzisha mazungumzo. Hata hivyo, hii si njia yenye ufanisi sana. Watumiaji wako wanaishi katika zama za mawakala na wanatarajia kutumia maelezo ya kuanzisha mazungumzo na kuwasiliana na LLM badala yake. Hawajali kama unatumia MCP kuhifadhi uwezo wako; wanatarajia tu kuingiliana kwa kutumia lugha asilia. Hivyo basi, tunatatuaje hii? Suluhisho ni kuongeza LLM kwa mteja.

## Muhtasari

Katika somo hili tunazingatia kuongeza LLM kufanya kazi kwa mteja wako na kuonyesha jinsi hii inavyotoa uzoefu bora zaidi kwa mtumiaji wako.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuunda mteja mwenye LLM.
- Kujihusisha kwa urahisi na seva ya MCP kwa kutumia LLM.
- Kutoa uzoefu bora kwa mtumiaji wa mwisho upande wa mteja.

## Mbinu

Hebu tujifunze mbinu tunayohitaji kuchukua. Kuongeza LLM kunaonekana rahisi, lakini je, tutayafanya kweli?

Hapa ndipo mteja atakuwa anawasiliana na seva:

1. Kuanzisha muunganisho na seva.

1. Kuorodhesha uwezo, maelezo ya kuanzisha mazungumzo, rasilimali na zana, na kuhifadhi muundo wake.

1. Kuongeza LLM na kupitisha uwezo ulihifadhiwa na muundo wake kwa muundo unaoeleweka na LLM.

1. Kushughulikia maelezo ya mtumiaji kwa kuyapitia LLM pamoja na zana zilizoorodheshwa na mteja.

Nzuri, sasa tunaelewa jinsi ya kufanya hivi kwa kiwango cha juu, hebu tujaribu kwenye zoezi lililopo chini.

## Zoezi: Kuunda mteja mwenye LLM

Katika zoezi hili, tutajifunza kuongeza LLM kwa mteja wetu.

### Uthibitishaji kwa kutumia Token ya Upatikanaji wa Kibinafsi ya GitHub

Kuunda token ya GitHub ni mchakato rahisi. Hapa kuna jinsi unavyoweza kufanya:

- Nenda kwenye GitHub Settings – Bonyeza picha yako ya wasifu kwenye kona ya juu kulia na chagua Settings.
- Elekea kwenye Developer Settings – Teleza chini na bonyeza Developer Settings.
- Chagua Personal Access Tokens – Bonyeza Fine-grained tokens kisha Generate new token.
- Sanidi Token Yako – Ongeza maelezo kwa kumbukumbu, weka tarehe ya kuisha muda, na chagua vyema wigo unaohitajika (idhini). Katika kesi hii hakikisha unaongeza idhini ya Models.
- Tengeneza na Nakili Token – Bonyeza Generate token, na hakikisha kunakili mara moja, kwani hautaweza kuona tena.

### -1- Unganisha na seva

Hebu tuunde mteja wetu kwanza:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Ingiza zod kwa uthibitishaji wa muundo

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

Katika msimbo uliotangulia tumefanya:

- Kuleta maktaba zinazohitajika
- Kuunda darasa lenye wanajumla wawili, `client` na `openai` ambao watatusaidia kusimamia mteja na kuingiliana na LLM mtawalia.
- Kusanidi mfano wetu wa LLM kutumia GitHub Models kwa kuweka `baseUrl` kuelekeza kwenye API ya uamuzi.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Unda vigezo vya seva kwa muunganisho wa stdio
server_params = StdioServerParameters(
    command="mcp",  # Inayotekelezwa
    args=["run", "server.py"],  # Hoja za hiari za mstari wa amri
    env=None,  # Mabadiliko ya hiari ya mazingira
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Anzisha muunganisho
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

Katika msimbo uliotangulia tumefanya:

- Kuleta maktaba zinazohitajika kwa MCP
- Kuunda mteja

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

Kwanza, utahitaji kuongeza tegemezi za LangChain4j kwenye faili lako `pom.xml`. Ongeza tegemezi hizi kuwezesha ushirikiano wa MCP na msaada wa GitHub Models:

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

Kisha unda darasa lako la mteja wa Java:

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
    
    public static void main(String[] args) throws Exception {        // Sanidi LLM kutumia Mifano ya GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Tengeneza usafirishaji wa MCP kwa kuunganishwa na seva
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Tengeneza mteja wa MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Katika msimbo uliotangulia tumefanya:

- **Kuongeza tegemezi za LangChain4j**: Inahitajika kwa ushirikiano wa MCP, mteja rasmi wa OpenAI, na msaada wa GitHub Models
- **Kuleta maktaba za LangChain4j**: Kwa ushirikiano na MCP na utendaji wa mfano wa mazungumzo wa OpenAI
- **Kuunda `ChatLanguageModel`**: Imewekwa kutumia GitHub Models na token yako ya GitHub
- **Kuseti usafirishaji wa HTTP**: Kutumia Server-Sent Events (SSE) kuungana na seva ya MCP
- **Kuunda mteja wa MCP**: Atakayeshughulikia mawasiliano na seva
- **Kutumia msaada wa MCP uliyojumuishwa wa LangChain4j**: Ambayo hurahisisha ushirikiano kati ya LLMs na seva za MCP

#### Rust

Mfano huu unadhani kwa kuwa na seva ya MCP ya Rust inayoendesha. Kama huna moja, rejelea somo la [01-first-server](../01-first-server/README.md) kuunda seva.

Mara unapokuwa na seva yako ya MCP ya Rust, fungua terminal na elekea kwenye saraka ile ile na seva inayoendesha. Kisha endesha amri ifuatayo kuunda mradi mpya wa mteja LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Ongeza tegemezi zifuatazo kwenye faili lako `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Hakuna maktaba rasmi ya Rust ya OpenAI, lakini `async-openai` ni [maktaba inayotunzwa na jamii](https://platform.openai.com/docs/libraries/rust#rust) ambayo hutumika sana.

Fungua faili `src/main.rs` na badilisha maudhui yake na msimbo ufuatao:

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
    // Ujumbe wa mwanzo
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Weka mteja wa OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Weka mteja wa MCP
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

    // TODO: Pata orodha ya zana za MCP

    // TODO: Mazungumzo ya LLM na simu za zana

    Ok(())
}
```

Msimbo huu unaandaa programu ya Rust ambayo itaungana na seva ya MCP na GitHub Models kwa ajili ya mwingiliano wa LLM.

> [!IMPORTANT]
> Hakikisha umeweka thamani ya mazingira `OPENAI_API_KEY` na token yako ya GitHub kabla ya kuendesha programu.

Nzuri, kwa hatua inayofuata, hebu tuorodheshe uwezo wa seva.

### -2- Orodhesha uwezo wa seva

Sasa tutaungana na seva na kuomba uwezo wake:

#### Typescript

Katika darasa lile lile, ongeza mbinu zifuatazo:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // orodha ya zana
    const toolsResult = await this.client.listTools();
}
```

Katika msimbo uliotangulia tumefanya:

- Kuongeza msimbo wa kuungana na seva, `connectToServer`.
- Kuunda mbinu `run` inayosimamia mkondo wa programu yetu. Hadi sasa inaorodhesha tu zana lakini tutaziongeza zaidi hivi karibuni.

#### Python

```python
# Orodhesha rasilimali zinazopatikana
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Orodhesha zana zinazopatikana
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Hivi ndivyo tulivyoongeza:

- Kurodhesha rasilimali na zana na kuzichapisha. Kwa zana pia tumeorodhesha `inputSchema` tunayotumia baadaye.

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

Katika msimbo uliotangulia tumefanya:

- Kurodhesha zana zilizopo kwenye Seva ya MCP
- Kwa kila zana, kuorodhesha jina, maelezo na muundo wake. Huu wa mwisho ni tunaoutumia kuitisha zana hivi karibuni.

#### Java

```java
// Unda mtoa zana ambaye huwachunguza zana za MCP kiotomatiki
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Mtoa zana wa MCP huendesha moja kwa moja:
// - Kuorodhesha zana zinazopatikana kutoka kwa seva ya MCP
// - Kubadilisha skimu za zana za MCP kuwa muundo wa LangChain4j
// - Kusimamia utekelezaji wa zana na majibu
```

Katika msimbo uliotangulia tumefanya:

- Kuunda `McpToolProvider` inayogundua na kusajili moja kwa moja zana zote kutoka seva ya MCP
- Mtoaji zana hushughulikia uongofu kati ya miundo ya zana za MCP na muundo wa zana za LangChain4j ndani
- Mbinu hii huondoa hitaji la orodha na uongofu wa zana kwa mikono

#### Rust

Kupata zana kutoka kwa seva ya MCP hufanywa kwa kutumia mbinu `list_tools`. Katika kazi yako `main`, baada ya kutengeneza mteja wa MCP, ongeza msimbo ufuatao:

```rust
// Pata orodha ya zana za MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Badilisha uwezo wa seva kuwa zana za LLM

Hatua inayofuata baada ya kuorodhesha uwezo wa seva ni kuyabadilisha kuwa muundo unaoeleweka na LLM. Mara tutakapofanya hivyo, tunaweza kutoa uwezo huu kama zana kwa LLM yetu.

#### TypeScript

1. Ongeza msimbo ufuatao kubadilisha majibu kutoka Seva ya MCP kuwa muundo wa zana LLM inaweza kutumia:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Tengeneza muundo wa zod msingi kwenye input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Weka aina waziwazi kuwa "kazi"
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

    Msimbo uliotangulia unachukua jibu kutoka kwa Seva ya MCP na kuukibadilisha kuwa ufafanuzi wa zana unaoeleweka na LLM.

1. Hebu sasisha mbinu ya `run` kisha ili kuorodhesha uwezo wa seva:

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

    Katika msimbo uliotangulia, tumesasisha mbinu ya `run` ili kupitisha matokeo na kwa kila kipengee kuitisha `openAiToolAdapter`.

#### Python

1. Kwanza, hebu tujenge kipengele cha kubadilisha kama kifuatacho

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

    Katika kazi `convert_to_llm_tools` hapo juu tunachukua jibu la zana ya MCP na kulitafsiri kuwa muundo unaoeleweka na LLM.

1. Kisha, hebu sasisha msimbo wetu wa mteja kutumia kipengele hiki kama ifuatavyo:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Hapa, tunaongeza kuitisha `convert_to_llm_tool` kubadilisha jibu la zana ya MCP kuwa kitu tunaweza kumpa LLM baadaye.

#### .NET

1. Hebu ongeza msimbo kubadilisha jibu la zana ya MCP kuwa kitu LLM inaweza kuelewa

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

Katika msimbo uliotangulia tumefanya:

- Kuunda kazi `ConvertFrom` inayochukua jina, maelezo na muundo wa ingizo.
- Kueleza utendaji unaounda `FunctionDefinition` inayopitishwa kwa `ChatCompletionsDefinition`. Huu wa mwisho ni kitu ambacho LLM inaelewa.

1. Hebu tazame jinsi tunavyoweza kusasisha msimbo uliopo kufaidika na kazi hii hapo juu:

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
// Tengeneza kiolesura cha Bot kwa mwingiliano wa lugha ya asili
public interface Bot {
    String chat(String prompt);
}

// Sanidi huduma ya AI na zana za LLM na MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Katika msimbo uliotangulia tumefanya:

- Kutoa kiolesura rahisi cha `Bot` kwa mwingiliano wa lugha asilia
- Kutumia `AiServices` za LangChain4j kufunga moja kwa moja LLM na mtoaji zana wa MCP
- Mfumo huo huendesha moja kwa moja uongofu wa miundo ya zana na kuitisha kazi
- Mbinu hii huondoa uongofu wa zana kwa mikono – LangChain4j hushughulikia utekelezaji mzito wa kubadilisha zana za MCP kuwa muundo unaotambuliwa na LLM

#### Rust

Ili kubadilisha jibu la zana ya MCP kuwa muundo unaoeleweka na LLM, tutaongeza kazi saidizi inayotengeneza muundo wa orodha ya zana. Ongeza msimbo ufuatao kwenye faili yako `main.rs` chini ya kazi ya `main`. Hii itaitwa wakati wa kutuma maombi kwa LLM:

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

Nzuri, hatujasaidishwa kushughulikia maombi ya mtumiaji, hivyo tuchukulie hilo sasa.

### -4- Shughulikia ombi la maelezo ya mtumiaji

Katika sehemu hii ya msimbo, tutaendesha maombi ya mtumiaji.

#### TypeScript

1. Ongeza mbinu inayotumika kuitisha LLM wetu:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Piga simu zana ya seva
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fanya kitu fulani na matokeo
        // KIFANYIKE

        }
    }
    ```

    Katika msimbo uliotangulia tume:

    - Kuongeza mbinu `callTools`.
    - Mbinu hiyo hupokea jibu la LLM na kuangalia ni zana zipi zimeitwa, kama zipo:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // piga simu chombo
        }
        ```

    - Kuita zana, ikiwa LLM inaonyesha inapaswa kuitwa:

        ```typescript
        // 2. Piga simu zana ya seva
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fanya kitu na matokeo
        // KUFANYA
        ```

1. Sasisha mbinu ya `run` kuhusisha kuitisha LLM na kuitisha `callTools`:

    ```typescript

    // 1. Tengeneza ujumbe ambao ni ingizo kwa LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Kupiga simu kwa LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Pitia jibu la LLM, kwa kila chaguo, angalia kama lina simu za zana
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Nzuri, hapa chini ni msimbo wote:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Ingiza zod kwa ajili ya kuthibitisha muundo

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // pengine tutahitaji kubadilisha URL hii baadaye: https://models.github.ai/inference
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
          // Tengeneza muundo wa zod kulingana na input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Weka aina wazi kuwa "function"
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
    
    
          // 2. Piga zana ya seva
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Fanya kitu na matokeo
          // KUFANYA
    
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
    
        // 1. Pitia majibu ya LLM, kwa kila chaguo, angalia kama ina wito wa zana
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

1. Ongeza baadhi ya kuingiza vinavyohitajika kuitisha LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Kisha, ongeza kazi itakayoitisha LLM:

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
            # Vigezo vya hiari
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

    Katika msimbo uliotangulia tumefanya:

    - Kupitisha kazi zetu, tulizopata kwenye seva ya MCP na kuzibadilisha, kwa LLM.
    - Katiwa basi LLM na kazi hizo.
    - Kagua matokeo kuona ni kazi gani tunapaswa kuitisha, ikiwa ipo.
    - Mwisho, tunapitisha safu ya kazi za kuitisha.

1. Hatua ya mwisho, tusasishe msimbo wetu mkuu:

    ```python
    prompt = "Add 2 to 20"

    # muulize LLM zana gani zote, ikiwa zipo
    functions_to_call = call_llm(prompt, functions)

    # ita fungsi zilizopendekezwa
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Hapo, hiyo ilikuwa hatua ya mwisho, katika msimbo hapo juu tunafanya:

    - Kuita zana ya MCP kupitia `call_tool` kwa kutumia kazi ambayo LLM iliona inapaswa kuitwa kulingana na maelezo yetu.
    - Kuchapisha matokeo ya kuitisha zana kwenye Seva ya MCP.

#### .NET

1. Tuwatumie msimbo wa kuomba maelezo ya LLM:

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

    Katika msimbo uliotangulia tumefanya:

    - Kupata zana kutoka seva ya MCP, `var tools = await GetMcpTools()`.
    - Kuainisha maelezo ya mtumiaji `userMessage`.
    - Kuandaa kipengele cha chaguzi kinachoeleza mfano na zana.
    - Kutuma ombi kwa LLM.

1. Hatua ya mwisho, tazama kama LLM inadhani tunapaswa kuitisha kazi:

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

    Katika msimbo uliotangulia tumefanya:

    - Kuangalia orodha ya simu za kazi.
    - Kwa kila simu ya zana, taja jina na hoja kisha ita zana kwenye seva ya MCP kwa kutumia mteja wa MCP. Mwisho tunachapisha matokeo.

Haya ni maelezo ya msimbo kamili:

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
    // Tekeleza maombi ya lugha ya asili ambayo hutumia zana za MCP kiotomatiki
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

Katika msimbo uliotangulia tumefanya:

- Kutumia maelezo rahisi ya lugha asilia kuzungumza na zana za seva ya MCP
- Mfumo wa LangChain4j huendesha moja kwa moja:
  - Kubadilisha maelezo ya mtumiaji kuwa simu za zana inapohitajika
  - Kuitisha zana za MCP zinazofaa kulingana na uamuzi wa LLM
  - Kusimamia mtiririko wa mazungumzo kati ya LLM na seva ya MCP
- Mbinu hii hutoa uzoefu mzuri kwa mtumiaji ambapo watumiaji hawahitaji kujua kuhusu utekelezaji wa MCP nyuma ya pazia

Mfano kamili wa msimbo:

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

Hapa ndipo kazi kuu hufanyika. Tuitisha LLM na maelezo ya mtumiaji ya awali, kisha tuchambue majibu kuona kama zana yoyote inapaswa kuitwa. Ikiwa ndiyo, tutaaita zana hizo na kuendelea na mazungumzo na LLM hadi sitakapo hitaji zaidi ya simu za zana na kuwa na jibu la mwisho.

Tutafanya simu nyingi kwa LLM, hivyo hebu tufuate na kuunda kazi ambayo itashughulikia simu za LLM. Ongeza kazi ifuatayo kwenye faili `main.rs`:

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

Kazi hii hupokea mteja wa LLM, orodha ya ujumbe (ikiwa ni pamoja na maelezo ya mtumiaji), zana kutoka seva ya MCP, na kutuma ombi kwa LLM, ikirejesha jibu.
Jibu kutoka kwa LLM litakuwa na safu ya `choices`. Tutahitaji kuchakata matokeo kuona kama kuna `tool_calls` zozote. Hii inatuamsha kuwa LLM inahitaji zana maalum iitwe na hoja. Ongeza msimbo ufuatao chini ya faili yako ya `main.rs` ili kufafanua kazi ya kushughulikia jibu la LLM:

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

    // Chapisha maudhui ikiwa yanapatikana
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Shughulikia wito za zana
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Ongeza ujumbe wa msaidizi

        // Tekeleza kila wito wa zana
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Ongeza matokeo ya zana kwenye ujumbe
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Endelea mazungumzo na matokeo ya zana
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

Ikiwa `tool_calls` zipo, inachukua taarifa za zana, inaita server ya MCP kwa ombi la zana, na inaongeza matokeo kwenye ujumbe wa mazungumzo. Kisha inaendelea na mazungumzo na LLM na ujumbe unasasishwa na jibu la msaidizi na matokeo ya simu za zana.

Ili kutoa taarifa za simu za zana ambazo LLM inarudisha kwa simu za MCP, tutaongeza kazi nyingine ya msaada kutoa kila kinachohitajika ili kufanya simu hiyo. Ongeza msimbo ufuatao chini ya faili yako ya `main.rs`:

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

Kwa vipande vyote vikiwa mahali pake, sasa tunaweza kushughulikia ombi la mwanzo la mtumiaji na kuita LLM. Sasisha kazi yako ya `main` kujumuisha msimbo ufuatao:

```rust
// Mazungumzo ya LLM na simu za zana
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

Hii itauliza LLM kwa ombi la mwanzo la mtumiaji linalouliza jumla ya nambari mbili, na itachakata jibu ili kushughulikia simu za zana kwa mabadiliko.

Vizuri, umefanya kazi!

## Kazi

Chukua msimbo kutoka zoezi na ujenge server na zana zaidi. Kisha tengeneza mteja mwenye LLM, kama ilivyozoezwa kwenye zoezi, na ujaribu kwa maombi tofauti kuhakikisha zana zote za server yako zinaitwa kwa mabadiliko. Njia hii ya kujenga mteja inamaanisha mtumiaji wa mwisho atapata uzoefu mzuri kwa kuwa anaweza kutumia maombi badala ya amri kamilifu za mteja, na hawatajua hata MCP server inapoitwa.

## Suluhisho

[Suluhisho](/03-GettingStarted/03-llm-client/solution/README.md)

## Muhimu Kuchukuliwa

- Kuongeza LLM kwenye mteja wako kunatoa njia bora kwa watumiaji kuingiliana na MCP Servers.
- Unahitaji kubadilisha majibu ya MCP Server kuwa kitu ambacho LLM inaweza kuelewa.

## Sampuli

- [Kihesabu cha Java](../samples/java/calculator/README.md)
- [Kihesabu cha .Net](../../../../03-GettingStarted/samples/csharp)
- [Kihesabu cha JavaScript](../samples/javascript/README.md)
- [Kihesabu cha TypeScript](../samples/typescript/README.md)
- [Kihesabu cha Python](../../../../03-GettingStarted/samples/python)
- [Kihesabu cha Rust](../../../../03-GettingStarted/samples/rust)

## Rasilimali Zaidi

## Kinachofuata

- Ifuatayo: [Kutumia server kwa Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tangazo la Kukataa**:  
Nyaraka hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au kutokamilika. Nyaraka asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->