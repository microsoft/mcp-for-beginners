# Kuunda mteja na LLM

Hadi sasa, umeona jinsi ya kuunda seva na mteja. Mteja amekuwa na uwezo wa kuita seva moja kwa moja ili kuorodhesha zana zake, rasilimali na maelekezo. Hata hivyo, siyo njia yenye ufanisi sana. Mtumiaji wako anaishi katika enzi ya mawakala na anatarajia kutumia maelekezo na kuwasiliana na LLM kufanya hivyo. Kwa mtumiaji wako, haijalishi kama unatumia MCP au la kuhifadhi uwezo wako lakini wanatarajia kutumia lugha ya asili kuingiliana. Basi tunatatuaje hili? Suluhisho ni kuhusu kuongeza LLM kwa mteja.

## Muhtasari

Katika somo hili tunazingatia kuongeza LLM kufanya kazi kwa mteja wako na kuonyesha jinsi hii inavyotoa uzoefu bora zaidi kwa mtumiaji wako.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuunda mteja mwenye LLM.
- Kuingiliana kwa urahisi na seva ya MCP kwa kutumia LLM.
- Kutoa uzoefu bora kwa mtumiaji wa mwisho upande wa mteja.

## Njia

Hebu tujifunze njia tunayohitaji kuchukua. Kuongeza LLM inaonekana rahisi, lakini je, tutafanya hivyo kweli?

Hivi ndivyo mteja atavyowasiliana na seva:

1. Kuanzisha muunganisho na seva.

1. Kuorodhesha uwezo, maelekezo, rasilimali na zana, na kuhifadhi muundo wao.

1. Ongeza LLM na pita uwezo ulihifadhiwa na muundo wake kwa muundo unaoeleweka na LLM.

1. Shughulikia maelekezo ya mtumiaji kwa kuyapita kwa LLM pamoja na zana zilizoorodheshwa na mteja.

Nzuri, sasa tunaelewa jinsi tunavyoweza kufanya hivi kwa kiwango cha juu, hebu tujaribu hili katika zoezi lililofuata.

## Zoezi: Kuunda mteja mwenye LLM

Katika zoezi hili, tutajifunza kuongeza LLM kwa mteja wetu.

### Uthibitishaji kwa kutumia Tokeni ya Ufikiaji wa Binafsi ya GitHub

Kuunda tokeni ya GitHub ni mchakato rahisi. Hapa ni jinsi unavyoweza kufanya hivyo:

- Nenda kwenye Mipangilio ya GitHub – Bonyeza picha yako ya wasifu upande wa juu kulia na chagua Mipangilio.
- Elekea kwenye Mipangilio ya Mwanaendelezaji – Skrolli chini na bonyeza Mipangilio ya Mwanaendelezaji.
- Chagua Tokeni za Ufikiaji wa Binafsi – Bonyeza tokeni za Fine-grained kisha Tengeneza tokeni mpya.
- Sanidi Tokeni Yako – Ongeza maelezo kwa kumbukumbu, weka tarehe ya kumalizika, na chagua wigo unaohitajika (idhini). Katika kesi hii hakikisha unaongeza idhini ya Models.
- Tengeneza na Nakili Tokeni – Bonyeza Tengeneza tokeni, na hakikisha unakili mara moja, kwani hautaweza kuiona tena.

### -1- Unganisha na seva

Hebu tuanze kwa kuunda mteja wetu:

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

Katika msimbo uliotangulia tume:

- Kuleta maktaba zinazohitajika
- Kuunda darasa lenye wanachama wawili, `client` na `openai` ambao watatusaidia kusimamia mteja na kuingiliana na LLM mtawaliwa.
- Kusanidi mfano wetu wa LLM kutumia GitHub Models kwa kuweka `baseUrl` kuelekeza kwenye API ya inference.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Unda vigezo vya seva kwa muunganisho wa stdio
server_params = StdioServerParameters(
    command="mcp",  # Inayotekelezeka
    args=["run", "server.py"],  # Hoja za hiari za mstari wa amri
    env=None,  # Vigezo vya mazingira vya hiari
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

Katika msimbo uliotangulia tume:

- Kuleta maktaba zinazohitajika kwa MCP
- Kuunda mteja

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

Kwanza, utahitaji kuongeza utegemezi wa LangChain4j kwenye faili yako ya `pom.xml`. Ongeza utegemezi huu kuwezesha ushirikiano wa MCP na msaada wa GitHub Models:

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
    
    public static void main(String[] args) throws Exception {        // Sanidi LLM kutumia Modeli za GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Unda usafirishaji wa MCP kwa kuunganishwa na seva
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Unda mteja wa MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Katika msimbo uliotangulia tume:

- **Kuongeza utegemezi wa LangChain4j**: Unaohitajika kwa ushirikiano wa MCP, mteja rasmi wa OpenAI, na msaada wa GitHub Models
- **Kuleta maktaba za LangChain4j**: Kwa ushirikiano wa MCP na utendaji wa mfano wa mazungumzo wa OpenAI
- **Kuunda `ChatLanguageModel`**: Iliyosanidiwa kutumia GitHub Models na tokeni yako ya GitHub
- **Kuweka usafirishaji wa HTTP**: Kutumia Server-Sent Events (SSE) kuungana na seva ya MCP
- **Kuunda mteja wa MCP**: Atashughulikia mawasiliano na seva
- **Kutumia msaada wa MCP uliopo ndani ya LangChain4j**: Ambayo inarahisisha ushirikiano kati ya LLMs na seva za MCP

#### Rust

Mfano huu unadhani kuwa una seva ya MCP inayotumia Rust inayoendesha. Ikiwa huna moja, rejelea somo la [01-first-server](../01-first-server/README.md) kuunda seva.

Mara baada ya kuwa na seva yako ya MCP ya Rust, fungua terminal na elekea kwenye saraka ile ile kama seva. Kisha endesha amri ifuatayo kuunda mradi mpya wa mteja wa LLM:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Ongeza utegemezi ufuatao kwenye faili yako ya `Cargo.toml`:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Hakuna maktaba rasmi ya Rust kwa OpenAI, hata hivyo, `async-openai` ni [maktaba inayodumishwa na jamii](https://platform.openai.com/docs/libraries/rust#rust) inayotumika sana.

Fungua faili `src/main.rs` na badilisha yaliyomo na msimbo ufuatao:

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
    // Ujumbe wa awali
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Sanidi mteja wa OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Sanidi mteja wa MCP
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

Msimbo huu unaandaa programu ya msingi ya Rust ambayo itaungana na seva ya MCP na GitHub Models kwa maingiliano ya LLM.

> [!IMPORTANT]
> Hakikisha umeweka thamani ya mazingira `OPENAI_API_KEY` na tokeni yako ya GitHub kabla ya kuendesha programu.

Nzuri, kwa hatua yetu inayofuata, hebu tuorodheshe uwezo wa seva.

### -2- Orodhesha uwezo wa seva

Sasa tutaungana na seva na kuomba uwezo wake:

#### Typescript

Katika darasa lile lile, ongeza njia zifuatazo:

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

Katika msimbo uliotangulia tume:

- Kuongeza msimbo wa kuungana na seva, `connectToServer`.
- Kuunda njia `run` inayohusika na kusimamia mtiririko wa programu yetu. Hadi sasa inaorodhesha zana tu lakini tutaziongeza zaidi hivi karibuni.

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

Hapa tuliongeza:

- Kuorodhesha rasilimali na zana na kuzichapisha. Kwa zana pia tumeorodhesha `inputSchema` ambayo tutaitumia baadaye.

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

Katika msimbo uliotangulia tume:

- Kuweka orodha ya zana zinazopatikana kwenye seva ya MCP
- Kwa kila zana, kuorodhesha jina, maelezo na muundo wake. Hili ni jambo ambalo tutalitumia kuitisha zana hivi karibuni.

#### Java

```java
// Unda mtoa zana anayegundua zana za MCP kiotomatiki
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Mtoa zana wa MCP hushughulikia kiotomatiki:
// - Orodhesha zana zinazopatikana kutoka kwa seva ya MCP
// - Kubadilisha miundo ya zana za MCP kuwa muundo wa LangChain4j
// - Kusimamia utekelezaji wa zana na majibu
```

Katika msimbo uliotangulia tume:

- Kuunda `McpToolProvider` inayogundua na kusajili moja kwa moja zana zote kutoka kwa seva ya MCP
- Mtoa zana anashughulikia uongofu kati ya miundo ya zana za MCP na muundo wa zana wa LangChain4j ndani yake
- Njia hii inaficha mchakato wa kuorodhesha zana na uongofu wa mikono

#### Rust

Kupata zana kutoka kwa seva ya MCP hufanywa kwa kutumia njia `list_tools`. Katika kazi yako ya `main`, baada ya kuandaa mteja wa MCP, ongeza msimbo ufuatao:

```rust
// Pata orodha ya zana za MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Badilisha uwezo wa seva kuwa zana za LLM

Hatua inayofuata baada ya kuorodhesha uwezo wa seva ni kuubadilisha kuwa muundo unaoeleweka na LLM. Mara tu tutakapofanya hivyo, tunaweza kutoa uwezo huu kama zana kwa LLM yetu.

#### TypeScript

1. Ongeza msimbo ufuatao kubadilisha majibu kutoka MCP Server kuwa muundo wa zana unaotumika na LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Unda schema ya zod kulingana na input_schema
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

    ```

    Msimbo hapo juu unachukua jibu kutoka MCP Server na kuubadilisha kuwa muundo wa ufafanuzi wa zana unaoeleweka na LLM.

1. Hebu sasisha njia ya `run` ifuatayo kuorodhesha uwezo wa seva:

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

    Katika msimbo uliotangulia, tumesasisha njia ya `run` kupita matokeo na kwa kila kipengee kuitisha `openAiToolAdapter`.

#### Python

1. Kwanza, hebu tuunde kazi ifuatayo ya kubadilisha

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

    Katika kazi hapo juu `convert_to_llm_tools` tunachukua jibu la zana ya MCP na kuibadilisha kuwa muundo unaoeleweka na LLM.

1. Ifuatayo, hebu sasisha msimbo wetu wa mteja kutumia kazi hii kama ifuatavyo:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Hapa, tunaongeza wito kwa `convert_to_llm_tool` kubadilisha jibu la zana ya MCP kuwa kitu ambacho tunaweza kumpa LLM baadaye.

#### .NET

1. Hebu ongeza msimbo kubadilisha jibu la zana ya MCP kuwa kitu ambacho LLM inaweza kuelewa

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

Katika msimbo uliotangulia tume:

- Kuunda kazi `ConvertFrom` inayochukua jina, maelezo na muundo wa ingizo.
- Kueleza utendaji unaounda `FunctionDefinition` inayopitishwa kwa `ChatCompletionsDefinition`. Hili ni jambo ambalo LLM inaweza kuelewa.

1. Hebu tazame jinsi tunavyoweza kusasisha baadhi ya msimbo uliopo kutumia kazi hii hapo juu:

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
// Unda kiolesura cha Bot kwa mawasiliano ya lugha asilia
public interface Bot {
    String chat(String prompt);
}

// Sanidi huduma ya AI kwa zana za LLM na MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Katika msimbo uliotangulia tume:

- Kueleza kiolesura rahisi cha `Bot` kwa maingiliano ya lugha ya asili
- Kutumia `AiServices` ya LangChain4j kufunga moja kwa moja LLM na mtoa zana wa MCP
- Mfumo huu unashughulikia moja kwa moja uongofu wa muundo wa zana na kuitisha kazi nyuma ya pazia
- Njia hii inaondoa uongofu wa mikono wa zana - LangChain4j hushughulikia ugumu wote wa kubadilisha zana za MCP kuwa muundo unaolingana na LLM

#### Rust

Kubadilisha jibu la zana ya MCP kuwa muundo unaoeleweka na LLM, tutaongeza kazi ya msaada inayopanga orodha ya zana. Ongeza msimbo ufuatao kwenye faili yako ya `main.rs` chini ya kazi ya `main`. Hii itaitwa wakati wa kufanya maombi kwa LLM:

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

Nzuri, sasa tumeandaa kushughulikia maombi yoyote ya mtumiaji, basi hebu tushughulikie hilo ifuatayo.

### -4- Shughulikia ombi la maelekezo ya mtumiaji

Katika sehemu hii ya msimbo, tutashughulikia maombi ya mtumiaji.

#### TypeScript

1. Ongeza njia itakayotumika kuitisha LLM yetu:

    ```typescript
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
    ```

    Katika msimbo uliotangulia tume:

    - Kuongeza njia `callTools`.
    - Njia hii inachukua jibu la LLM na kuangalia ni zana gani zimeitwa, ikiwa zipo:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // piga simu chombo
        }
        ```

    - Kuitisha zana, ikiwa LLM inaonyesha inapaswa kuitwa:

        ```typescript
        // 2. Piga zana ya seva
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fanya kitu na matokeo
        // KUFANYA
        ```

1. Sasisha njia ya `run` kujumuisha wito kwa LLM na kuitisha `callTools`:

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

    // 2. Piga simu kwa LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
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

Nzuri, hebu tuorodheshe msimbo mzima:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Ingiza zod kwa uthibitishaji wa muundo

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // huenda ikahitajika kubadilisha hadi URL hii siku za usoni: https://models.github.ai/inference
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
          // Unda muundo wa zod kulingana na input_schema
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
    
    
          // 2. Piga simu kwa chombo cha seva
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Pitia jibu la LLM, kwa kila chaguo, angalia kama lina simu za zana
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

1. Hebu ongeza baadhi ya uingizaji unaohitajika kuitisha LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Ifuatayo, ongeza kazi itakayoitisha LLM:

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

    Katika msimbo uliotangulia tume:

    - Kupitisha kazi zetu, tulizozipata kwenye seva ya MCP na kuzibadilisha, kwa LLM.
    - Kisha tukaomba LLM kwa kazi hizo.
    - Kisha, tunachunguza matokeo kuona ni kazi gani tunapaswa kuitisha, ikiwa zipo.
    - Mwishowe, tunapita safu ya kazi za kuitisha.

1. Hatua ya mwisho, hebu sasisha msimbo wetu mkuu:

    ```python
    prompt = "Add 2 to 20"

    # muulize LLM zana gani kwa wote, ikiwa zipo
    functions_to_call = call_llm(prompt, functions)

    # piga simu kwa kazi zilizopendekezwa
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Hapo, hiyo ilikuwa hatua ya mwisho, katika msimbo hapo juu tuko:

    - Kuitisha zana ya MCP kupitia `call_tool` kwa kutumia kazi ambayo LLM iliona inapaswa kuitwa kulingana na maelekezo yetu.
    - Kuchapisha matokeo ya wito wa zana kwa seva ya MCP.

#### .NET

1. Hebu tueleze msimbo wa kufanya ombi la maelekezo kwa LLM:

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

    Katika msimbo uliotangulia tume:

    - Kupata zana kutoka kwa seva ya MCP, `var tools = await GetMcpTools()`.
    - Kueleza maelekezo ya mtumiaji `userMessage`.
    - Kuunda kitu cha chaguo kinachoelezea mfano na zana.
    - Kufanya ombi kwa LLM.

1. Hatua ya mwisho, hebu tazame kama LLM inadhani tunapaswa kuitisha kazi:

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

    Katika msimbo uliotangulia tume:

    - Kupitia orodha ya wito wa kazi.
    - Kwa kila wito wa zana, changanua jina na hoja na uitishe zana kwenye seva ya MCP kwa kutumia mteja wa MCP. Mwisho tunachapisha matokeo.

Hapa ni msimbo mzima:

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
    // Tekeleza maombi ya lugha ya asili yanayotumia zana za MCP moja kwa moja
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

Katika msimbo uliotangulia tume:

- Kutumia maelekezo rahisi ya lugha ya asili kuingiliana na zana za seva ya MCP
- Mfumo wa LangChain4j unashughulikia moja kwa moja:
  - Kubadilisha maelekezo ya mtumiaji kuwa wito wa zana inapohitajika
  - Kuitisha zana za MCP zinazofaa kulingana na uamuzi wa LLM
  - Kusimamia mtiririko wa mazungumzo kati ya LLM na seva ya MCP
- Njia ya `bot.chat()` inarudisha majibu ya lugha ya asili ambayo yanaweza kujumuisha matokeo kutoka kwa utekelezaji wa zana za MCP
- Njia hii hutoa uzoefu usio na mshono kwa mtumiaji ambapo hawahitaji kujua kuhusu utekelezaji wa MCP chini ya uso

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

Hapa ndipo kazi nyingi zinapofanyika. Tutaita LLM na maelekezo ya awali ya mtumiaji, kisha tushughulikie jibu kuona kama kuna zana zozote zinazohitaji kuitwa. Ikiwa zipo, tutaaita zana hizo na kuendelea na mazungumzo na LLM hadi hakuna wito zaidi wa zana na tunapata jibu la mwisho.

Tutafanya miito mingi kwa LLM, basi hebu tueleze kazi itakayoshughulikia wito wa LLM. Ongeza kazi ifuatayo kwenye faili yako ya `main.rs`:

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

Kazi hii inachukua mteja wa LLM, orodha ya ujumbe (ikiwa ni pamoja na maelekezo ya mtumiaji), zana kutoka kwa seva ya MCP, na kutuma ombi kwa LLM, ikirudisha jibu.
Jibu kutoka kwa LLM litakuwa na safu ya `choices`. Tutahitaji kuchakata matokeo kuona kama kuna `tool_calls` yoyote. Hii inatufahamisha kuwa LLM inahitaji zana maalum iitwe na hoja. Ongeza msimbo ufuatao chini ya faili yako ya `main.rs` ili kufafanua kazi ya kushughulikia jibu la LLM:

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

    // Shughulikia simu za zana
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Ongeza ujumbe wa msaidizi

        // Tekeleza kila simu ya zana
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

Kama `tool_calls` zipo, hutambua taarifa za zana, huwaita seva ya MCP na ombi la zana, na huongeza matokeo kwenye ujumbe wa mazungumzo. Kisha inaendelea na mazungumzo na LLM na ujumbe huboreshwa kwa jibu la msaidizi na matokeo ya wito wa zana.

Ili kutoa taarifa za wito wa zana ambazo LLM inarudisha kwa wito za MCP, tutaongeza kazi nyingine ya msaada kutoa kila kitu kinachohitajika kufanya wito. Ongeza msimbo ufuatao chini ya faili yako ya `main.rs`:

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

Hii itauliza LLM kwa ombi la mwanzo la mtumiaji linaloomba jumla ya nambari mbili, na itachakata jibu kushughulikia kwa nguvu wito wa zana.

Nzuri, umefanya kazi!

## Kazi

Chukua msimbo kutoka kwenye zoezi na ujenge seva na zana zaidi. Kisha tengeneza mteja mwenye LLM, kama ilivyo kwenye zoezi, na ujitihadi na maombi tofauti kuhakikisha zana zote za seva yako zinaitwa kwa nguvu. Njia hii ya kujenga mteja inamaanisha mtumiaji wa mwisho atapata uzoefu mzuri wa mtumiaji kwa kuwa anaweza kutumia maombi, badala ya amri kamili za mteja, na haatambui MCP server yoyote inayoitwa.

## Suluhisho

[Suluhisho](/03-GettingStarted/03-llm-client/solution/README.md)

## Muhimu Kumbuka

- Kuongeza LLM kwenye mteja wako kunatoa njia bora kwa watumiaji kuingiliana na Seva za MCP.
- Unahitaji kubadilisha jibu la Seva ya MCP kuwa kitu ambacho LLM inaweza kuelewa.

## Sampuli

- [Kalkuleta ya Java](../samples/java/calculator/README.md)
- [Kalkuleta ya .Net](../../../../03-GettingStarted/samples/csharp)
- [Kalkuleta ya JavaScript](../samples/javascript/README.md)
- [Kalkuleta ya TypeScript](../samples/typescript/README.md)
- [Kalkuleta ya Python](../../../../03-GettingStarted/samples/python)
- [Kalkuleta ya Rust](../../../../03-GettingStarted/samples/rust)

## Rasilimali Zaidi

## Ifuatayo

- Ifuatayo: [Kutumia seva kwa kutumia Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifa cha Kukataa**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->