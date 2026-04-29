# Kuunda mteja na LLM

Mpaka sasa, umeona jinsi ya kuunda seva na mteja. Mteja amekuwa akiwahi kuita seva moja kwa moja ili kuorodhesha zana zake, rasilimali, na misukumo. Hata hivyo, hii si njia bora sana ya vitendo. Watumiaji wako wanaishi katika enzi ya mawakala na wanatarajia kutumia misukumo na kuwasiliana na LLM badala yake. Hawajali kama unatumia MCP kuhifadhi uwezo wako; wanatarajia tu kuwasiliana kwa kutumia lugha ya asili. Basi tunatatuaje hili? Suluhisho ni kuongeza LLM kwa mteja.

## Muhtasari

Katika somo hili tunazingatia kuongeza LLM kufanya mteja wako na kuonyesha jinsi hii inavyotoa uzoefu bora kwa mtumiaji wako.

## Malengo ya Kujifunza

Mwisho wa somo hili, utakuwa na uwezo wa:

- Kuunda mteja na LLM.
- Kujumuisha kwa urahisi na seva ya MCP kutumia LLM.
- Kutoa uzoefu bora wa mtumiaji wa mwisho upande wa mteja.

## Mbinu

Tujaribu kuelewa njia tunayohitaji kuchukua. Kuongeza LLM inaonekana rahisi, lakini je, kweli tutafanya hivi?

Hivi ndivyo mteja atakavyoshirikiana na seva:

1. Kuweka muunganisho na seva.

1. Orodhesha uwezo, misukumo, rasilimali na zana, na hifadhi muundo wake.

1. Ongeza LLM na pita uwezo uliohifadhiwa na muundo wake kwa njia ambayo LLM inaelewa.

1. Shughulikia ombi la mtumiaji kwa kulipitisha kwa LLM pamoja na zana zilizoorodheshwa na mteja.

Nzuri, sasa tunaelewa jinsi tunavyoweza kufanya hivi kwa kiwango cha juu, tujaribu kwenye zoezi hapa chini.

## Zozi: Kuunda mteja na LLM

Katika zoezi hili, tutajifunza kuongeza LLM kwa mteja wetu.

### Uthibitishaji kwa kutumia Tokeni ya Ufikiaji wa Kibinafsi ya GitHub

Kuunda tokeni ya GitHub ni mchakato rahisi. Hivi ndivyo unaweza kufanya:

- Nenda kwenye Mipangilio ya GitHub – Bonyeza picha ya wasifu wako upande wa juu kulia na chagua Mipangilio.
- Elekea kwenye Mipangilio ya Mmoja wa Kuendeleza – Rendesha chini na bonyeza Mipangilio ya Mmoja wa Kuendeleza.
- Chagua Tokeni za Ufikiaji wa Kibinafsi – Bonyeza tokeni zilizopanuliwa kwa undani kisha Unda tokeni mpya.
- Sanidi Tokeni Yako – Ongeza maelezo kwa kumbukumbu, weka tarehe ya kumalizika, na chagua maeneo muhimu (idhini). Katika kesi hii hakikisha unaongeza idhini ya Models.
- Tengeneza na Nakili Tokeni – Bonyeza Tengeneza tokeni, na hakikisha kuikopa mara moja, kwa sababu hautaiona tena.

### -1- Unganisha na seva

Tuanze kwa kuunda mteja wetu kwanza:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Ingiza zod kwa uthibitishaji wa mchakato

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

- Kuleta maktaba zinazohitajiwa
- Kuunda darasa lenye wanachama wawili, `client` na `openai` ambao watatusaidia kusimamia mteja na kuingiliana na LLM mtawaliwa.
- Kusanidi mfano wetu wa LLM kutumia GitHub Models kwa kuweka `baseUrl` kuonyesha API ya inference.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Unda vigezo vya seva kwa muunganisho wa stdio
server_params = StdioServerParameters(
    command="mcp",  # Inayotekelezwa
    args=["run", "server.py"],  # Hoja za laini ya amri zinazoweza kuchaguliwa
    env=None,  # Vigezo vya mazingira zinazoweza kuchaguliwa
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

Katika msimbo uliopita tumefanya:

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

Kwanza, utahitaji kuongeza utegemezi wa LangChain4j kwenye faili yako ya `pom.xml`. Ongeza utegemezi huu kuwezesha mchanganyiko wa MCP na msaada wa GitHub Models:

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

Kisha unda darasa lako la mteja la Java:

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
    
    public static void main(String[] args) throws Exception {        // Sanidi LLM kutumia Miundo ya GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Unda usafirishaji wa MCP wa kuunganishwa na seva
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

Katika msimbo uliopita tumefanya:

- **Kuongeza utegemezi wa LangChain4j**: Unaohitajika kwa mchanganyiko wa MCP, mteja rasmi wa OpenAI, na msaada wa GitHub Models
- **Kuleta maktaba za LangChain4j**: Kwa mchanganyiko wa MCP na utendaji wa modeli ya mazungumzo ya OpenAI
- **Kuunda `ChatLanguageModel`**: Iliyosanidiwa kutumia GitHub Models na tokeni yako ya GitHub
- **Kusanidi usafirishaji wa HTTP**: Kutumia Server-Sent Events (SSE) kuungana na seva ya MCP
- **Kuunda mteja wa MCP**: Ambaye atashughulikia mawasiliano na seva
- **Kutumia msaada wa MCP uliomo ndani ya LangChain4j**: Ambayo hurahisisha mchanganyiko kati ya LLM na seva za MCP

#### Rust

Mfano huu unadhani una seva ya MCP inayotumia Rust inayoendeshwa. Ikiwa huna seva, rejelea somo la [01-first-server](../01-first-server/README.md) kuunda seva.

Mara unapo kuwa na seva yako ya MCP ya Rust, fungua terminal na elekea kwenye folda ile ile kama seva. Kisha endesha amri ifuatayo kuunda mradi mpya wa mteja wa LLM:

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
> Hakuna maktaba rasmi ya Rust kwa OpenAI, hata hivyo, `async-openai` ni [maktaba inayotunzwa na jamii](https://platform.openai.com/docs/libraries/rust#rust) inayotumiwa mara nyingi.

Fungua faili ya `src/main.rs` na ubadilishe yaliyomo kwa msimbo ufuatao:

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

    // TODO: Mazungumzo ya LLM na wito wa zana

    Ok(())
}
```

Msimbo huu unasanidi programu ya msingi ya Rust ambayo itaungana na seva ya MCP na GitHub Models kwa maingiliano ya LLM.

> [!IMPORTANT]
> Hakikisha kuanzisha mabadiliko ya mazingira `OPENAI_API_KEY` na tokeni yako ya GitHub kabla ya kuendesha programu.

Nzuri, kwa hatua yetu inayofuata, tutaorodhesha uwezo kwenye seva.

### -2- Orodhesha uwezo wa seva

Sasa tutaanza kuungana na seva na kuuliza uwezo wake:

#### Typescript

Ndani ya darasa lile lile, ongeza njia zifuatazo:

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

Katika msimbo uliopita tumefanya:

- Kuongeza msimbo wa kuungana na seva, `connectToServer`.
- Kuunda njia `run` inayoshughulikia mtiririko wa programu yetu. Hadi sasa inaorodhesha tu zana lakini tutaanzisha zaidi hivi karibuni.

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

- Kuurahisisha orodha ya rasilimali na zana na kuzichapisha. Kwa zana pia tumeorodhesha `inputSchema` ambayo tutaitumia baadaye.

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

Katika msimbo uliopita tumefanya:

- Kuorodhesha zana zilizopo kwenye seva ya MCP
- Kwa kila zana, kuorodhesha jina, maelezo na muundo wake. Huu ni kitu ambacho tutatumia kuita zana hivi karibuni.

#### Java

```java
// Tengeneza mtoa chombo ambaye huigundua vifaa vya MCP kiotomatiki
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Mtoa chombo wa MCP huhakikisha kiotomatiki:
// - Kutoa orodha ya vifaa vinavyopatikana kutoka kwa seva ya MCP
// - Kubadilisha miundo ya zana za MCP kuwa muundo wa LangChain4j
// - Kusimamia utekelezaji wa zana na majibu
```

Katika msimbo uliopita tumefanya:

- Kuunda `McpToolProvider` ambayo inagundua na kusajili zana zote kutoka seva ya MCP moja kwa moja
- Mtoa zana anashughulikia uongofu kati ya miundo ya zana za MCP na mfumo wa zana wa LangChain4j kwa ndani
- Mbinu hii inaweza kuficha orodha ya zana na mchakato wa uongofu kwa kuondoa uendeshaji wa mikono

#### Rust

Kupata zana kutoka seva ya MCP hufanyika kwa kutumia njia `list_tools`. Katika kazi yako `main`, baada ya kusanidi mteja wa MCP, ongeza msimbo ufuatao:

```rust
// Pata orodha ya zana za MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Badilisha uwezo wa seva kuwa zana za LLM

Hatua inayofuata baada ya kuorodhesha uwezo wa seva ni kuubadilisha kuwa muundo ambao LLM inaweza kuelewa. Mara tu tutakapofanya hivyo, tunaweza kutoa uwezo huu kama zana kwa LLM yetu.

#### TypeScript

1. Ongeza msimbo ufuatao kubadilisha majibu kutoka MCP Server kuwa muundo wa zana zinazoweza kutumiwa na LLM:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Unda schema ya zod kwa mujibu wa input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Weka aina kuwa "function" kwa uwazi
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

    Msimbo huu unaochukua jibu kutoka MCP Server na kuubadilisha kuwa muundo wa zana ambayo LLM inaweza kuelewa.

1. Sasa tutaendeleza njia `run` kuorodhesha uwezo wa seva:

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

    Katika msimbo uliopita, tumezaa njia `run` kupitia matokeo na kwa kila kipengee kuita `openAiToolAdapter`.

#### Python

1. Kwanza, tuunde kazi ya kubadilisha ifuatayo

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

    Katika kazi `convert_to_llm_tools` hapo juu tunachukua majibu ya zana ya MCP na kuyaibadilisha kwa muundo LLM inaweza kuelewa.

1. Kisha, tusaidie mteja wetu kutumia kazi hii kama ifuatavyo:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Hapa, tunaongeza wito kwa `convert_to_llm_tool` kubadilisha majibu ya zana ya MCP kuwa kitu tunachoweza kumnyima LLM baadaye.

#### .NET

1. Ongeza msimbo kubadilisha majibu ya zana ya MCP kuwa kitu LLM inaweza kuelewa

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

Katika msimbo uliopita tumefanya:

- Kuunda kazi `ConvertFrom` inayoonyesha, jina, maelezo na muundo wa kuingiza.
- Kuanzisha utendaji unaounda `FunctionDefinition` inayotumiwa na `ChatCompletionsDefinition`. Hii ni kitu ambacho LLM inaweza kuelewa.

1. Tazama jinsi tunavyoweza kusasisha msimbo uliopo kuchukua faida ya kazi hii:

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
// Tengeneza kiolesura cha Bot kwa mwingiliano wa lugha asilia
public interface Bot {
    String chat(String prompt);
}

// Sanidi huduma ya AI na zana za LLM na MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Katika msimbo uliopita tumefanya:

- Kueleza interface rahisi ya `Bot` kwa maingiliano ya lugha ya asili
- Kutumia `AiServices` ya LangChain4j kufunga LLM na mtoa zana wa MCP moja kwa moja
- Mfumo unashughulikia kwa njia ya moja kwa moja uongofu wa muundo wa zana na wito wa kazi nyuma ya pazia
- Mbinu hii inaboresha kuondoa uongofu wa zana za mkono - LangChain4j hudhibiti ugumu wote wa kubadilisha zana za MCP kuwa muundo unaoendana na LLM

#### Rust

Ili kubadilisha majibu ya zana ya MCP kuwa muundo ambao LLM inaweza kuelewa, tutaongeza kazi ya kusaidia inayopanga orodha ya zana. Ongeza msimbo huu kwenye faili yako ya `main.rs` chini ya kazi `main`. Hii itaitwa wakati wa kufanya maombi kwa LLM:

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

Nzuri, sasa tumesanidi kushughulikia maombi ya mtumiaji, basi tuchukulie hilo hatua inayofuata.

### -4- Shughulikia ombi la misukumo ya mtumiaji

Katika sehemu hii ya msimbo, tutashughulikia maombi ya watumiaji.

#### TypeScript

1. Ongeza njia itakayotumika kuita LLM yetu:

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

    Katika msimbo uliopita tulifanya:

    - Kuongeza njia `callTools`.
    - Njia hiyo inachukua jibu la LLM na kuangalia ni zana zipi zilizoitwa, ikiwa zipo:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // piga simu zana
        }
        ```

    - Kuita zana, ikiwa LLM inaonyesha inapaswa kuitwa:

        ```typescript
        // 2. Piga simu kwa chombo cha seva
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Fanya jambo na matokeo
        // KUFANYA
        ```

1. Sasisha njia `run` kujumuisha miito kwa LLM na kuitwa kwa `callTools`:

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

Nzuri, tutaorodhesha msimbo wote:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Ingiza zod kwa uthibitisho wa mpangilio

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // huenda ikabidi kubadilisha URL hii siku za usoni: https://models.github.ai/inference
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
          // Unda mpangilio wa zod kulingana na input_schema
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
    
    
          // 2. Piga simu kwa zana ya seva
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Fanya jambo fulani na matokeo
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

1. Tuongeze baadhi ya uagizaji unaohitajika kuitia LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Kisha, ongeza kazi itakayotoa wito kwa LLM:

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

    Katika msimbo uliopita tumefanya:

    - Kupita kazi zetu, zilizopatikana kwenye seva ya MCP na kubadilishwa, kwa LLM.
    - Kisha tuliita LLM kwa kazi hizo.
    - Halafu, tunachunguza matokeo kuona ni kazi gani tunapaswa kuita, ikiwa zipo.
    - Hatimaye, tunapita safu ya kazi za kuita.

1. Hatua ya mwisho, sasisha msimbo wetu mkuu:

    ```python
    prompt = "Add 2 to 20"

    # muulize LLM ni zana gani zote, kama zipo
    functions_to_call = call_llm(prompt, functions)

    # ita simu kazi zinazopendekezwa
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Hapo, hiyo ilikuwa hatua ya mwisho, katika msimbo huu tunasema:

    - Kuita zana ya MCP kwa njia `call_tool` kwa kutumia kazi ambayo LLM iliona inapaswa kuitwa kulingana na misukumo yetu.
    - Kuchapisha matokeo ya wito wa zana kwenda seva ya MCP.

#### .NET

1. Tutoa mfano wa msimbo wa kufanya ombi la misukumo kwa LLM:

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

    Katika msimbo huu tumefanya:

    - Kupata zana kutoka seva ya MCP, `var tools = await GetMcpTools()`.
    - Kuelezwa misukumo ya mtumiaji `userMessage`.
    - Kujenga chaguo specifying modeli na zana.
    - Kufanya ombi kwa LLM.

1. Hatua ya mwisho, tazama ikiwa LLM inaona tunapaswa kuita kazi:

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

    Katika msimbo huu tumefanya:

    - Kupitia orodha ya wito wa kazi.
    - Kwa kila wito wa zana, kuchuja jina na hoja na kuitisha zana kwenye seva ya MCP kwa kutumia mteja wa MCP. Mwisho tunachapisha matokeo.

Huu hapa msimbo kamili:

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
    // Tekeleza maombi ya lugha asilia yanayotumia zana za MCP moja kwa moja
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

Katika msimbo huu tumefanya:

- Kutumia misukumo rahisi ya lugha ya asili kuingiliana na zana za seva ya MCP
- Mfumo wa LangChain4j huendesha moja kwa moja:
  - Kubadilisha misukumo ya mtumiaji kuwa miito ya zana inapohitajika
  - Kuita zana za MCP zinazofaa kulingana na uamuzi wa LLM
  - Kusimamia mtiririko wa mazungumzo kati ya LLM na seva ya MCP
- Njia ya `bot.chat()` inarudisha majibu ya lugha ya asili ambayo yanaweza kujumuisha matokeo kutoka kwa utekelezaji wa zana za MCP
- Mbinu hii hutoa uzoefu laini kwa mtumiaji ambapo watumiaji hawahitaji kujua kuhusu utekelezaji wa MCP unaofanywa ndani

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

Hapa ndipo kazi nyingi zinafanyika. Tutaita LLM na misukumo ya mwanzo ya mtumiaji, kisha kuchambua jibu kuona kama kuna zana zozote zinazosababisha kuitwa. Ikiwa zipo, tutaendelea kuitisha zana hizo na kuendelea na mazungumzo na LLM hadi hakuna miito zaidi ya zana na tutapata jibu la mwisho.

Tutafanya miito mingi kwa LLM, hivyo tutaeleza kazi itakayosimamia wito wa LLM. Ongeza kazi ifuatayo kwenye faili yako ya `main.rs`:

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

Kazi hii inachukua mteja wa LLM, orodha ya ujumbe (pamoja na misukumo ya mtumiaji), zana kutoka seva ya MCP, na kutuma ombi kwa LLM, kurudisha jibu.
Jibu kutoka kwa LLM litakuwa na safu ya `choices`. Tutahitaji kuchakata matokeo kuona kama kuna `tool_calls` yoyote ipo. Hii inatufahamisha kuwa LLM inahitaji chombo fulani kuitwa na hoja. Ongeza msimbo ufuatao mwisho wa faili yako ya `main.rs` ili kufafanua kazi ya kushughulikia jibu la LLM:

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

    // Shughulikia miito ya zana
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Ongeza ujumbe wa msaidizi

        // Tekeleza kila mwito wa zana
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Ongeza matokeo ya zana kwa ujumbe
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Endelea na mazungumzo kwa matokeo ya zana
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

Kama `tool_calls` zipo, huteka taarifa za chombo, huwaita seva ya MCP na ombi la chombo, na huongeza matokeo kwenye ujumbe wa mazungumzo. Kisha inaendelea na mazungumzo na LLM na ujumbe huboreshwa kwa jibu la msaidizi na matokeo ya wito wa chombo.

Ili kutoa taarifa za wito wa chombo ambazo LLM hurejelea kwa wito za MCP, tutaongeza kazi nyingine ya msaada ya kutoa kila kitu kinachohitajika kufanya wito huo. Ongeza msimbo ufuatao mwisho wa faili yako ya `main.rs`:

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

Kwa vipande vyote vilivyo mahali pake, sasa tunaweza kushughulikia onyo la mwanzo la mtumiaji na kuita LLM. Sasisha kazi yako ya `main` kujumuisha msimbo ufuatao:

```rust
// Mazungumzo ya LLM na kuitwa kwa zana
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

Hii itamjulisha LLM kwa onyo la mwanzo la mtumiaji akiomba jumla ya nambari mbili, na itachakata jibu kushughulikia kikamilifu kwa njia ya wito wa zana.

Nzuri, umefanya!

## Kazi ya Nyumbani

Chukua msimbo kutoka mazoezi na ujenge tena seva yako na zana zaidi. Kisha tengeneza mteja na LLM, kama ilivyo mazoezini, na ujaribu kwa onyo mbalimbali kuhakikisha zana zote za seva hubidiwa kwa nguvu. Njia hii ya kujenga mteja inamaanisha mtumiaji wa mwisho atapata uzoefu bora wa mtumiaji kwa kuwa anaweza kutumia onyo, badala ya amri halisi za mteja, na asijue kama seva ya MCP inaitwa.

## Suluhisho

[Suluhisho](./solution/README.md)

## Muhimu Kujua

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

## Kifuatacho

- Ifuatayo: [Kutumia seva kwa kutumia Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Makubaliano ya Kutotakiwa**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake hukubalika kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya mtaalamu wa binadamu. Hatubebwi dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->