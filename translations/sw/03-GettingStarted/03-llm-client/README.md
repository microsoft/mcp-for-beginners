# Kutoa mteja kwa LLM

> [!NOTE]
> Mifano ya mteja wa Java inaunganishwa kupitia usafirishaji wa HTTP+SSE wa urithi na
> inalenga MCP `2025-11-25` APIs za SDK. Tumia SDK inayolingana na `2026-07-28` na
> Streamable HTTP kwa wateja wapya wa mbali.

Hadi sasa, umeona jinsi ya kuunda seva na mteja. Mteja amekuwa akiuweza kuitisha seva moja kwa moja ili kuorodhesha zana zake, rasilimali, na maelekezo. Hata hivyo, hii sio njia halisi sana. Watumiaji wako wanaishi katika enzi ya mawakala na wanatarajia kutumia maelekezo na kuwasiliana na LLM badala yake. Hawajali kama unatumia MCP kuhifadhi uwezo wako; wanatarajia tu kuwasiliana kwa kutumia lugha ya asili. Basi tunawezaje kutatua hili? Suluhisho ni kuongeza LLM kwenye mteja.

## Muhtasari

Katika somo hili tunazingatia kuongeza LLM ili kufanya kazi kwenye mteja wako na kuonyesha jinsi hii inavyotoa uzoefu bora kwa mtumiaji wako.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuunda mteja pamoja na LLM.
- Kuweza kuwasiliana kwa urahisi na seva ya MCP kwa kutumia LLM.
- Kutoa uzoefu bora kwa mtumiaji mwisho upande wa mteja.

## Njia

Hebu tujaribu kuelewa njia tunayohitaji kuchukua. Kuongeza LLM inasikika rahisi, lakini je tunafanya hivyo kweli?

Hapa ndio jinsi mteja ataungana na seva:

1. Kuanzisha muunganisho na seva.

1. Kuorodhesha uwezo, maelekezo, rasilimali na zana, na kuhifadhi muundo wake.

1. Ongeza LLM na pitia uwezo ulihifadhiwa na muundo wake kwa njia LLM inaelewa.

1. Shughulikia ombi la mtumiaji kwa kulipitisha kwa LLM pamoja na zana zilizoorodheshwa na mteja.

Vizuri, sasa tumeelewa jinsi tunavyoweza kufanya hivi kwa kiwango cha juu, hebu tujaribu katika mazoezi hapa chini.

## Zoeezi: Kuunda mteja kwa LLM

Katika zoezi hili, tutajifunza kuongeza LLM kwenye mteja wetu.

### Uthibitishaji kwa kutumia Token ya Upatikanaji wa Binafsi ya GitHub

Kuunda tokeni ya GitHub ni mchakato rahisi. Hapa ni jinsi unaweza kufanya hivyo:

- Nenda kwenye Mipangilio ya GitHub – Bonyeza picha yako ya wasifu upande wa juu kulia na chagua Mipangilio.
- Elekea Mipangilio ya Mendelezaji – Skroll chini na bonyeza Mipangilio ya Mendelezaji.
- Chagua Tokeni za Ufikiaji wa Binafsi – Bonyeza tokeni zenye udhibiti wa kina kisha Unda tokeni mpya.
- Sanidi Tokeni Yako – Ongeza maelezo kwa kumbukumbusho, weka tarehe ya kuisha, na chagua mawasiliano muhimu (idhini). Katika kesi hii hakikisha unaongeza idhini ya Models.
- Tengeneza na Nakili Tokeni – Bonyeza Tengeneza tokeni, na hakikisha kunakili mara moja, kwani hutaweza kuiona tena.

### -1- Unganisha na seva

Hebu tuunde mteja wetu kwanza:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Ingiza zod kwa ajili ya uthibitishaji wa muundo

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
- Kuunda darasa lenye wanachama wawili, `client` na `openai` ambao watatusaidia kusimamia mteja na kuingiliana na LLM kwa mtiririko.
- Kusanidi mfano wa LLM wetu kutumia GitHub Models kwa kuweka `baseUrl` kuashiria API ya inference.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Unda vigezo vya seva kwa muunganisho wa stdio
server_params = StdioServerParameters(
    command="mcp",  # Inayotekelezwa
    args=["run", "server.py"],  # Hojaji za hiari za mstari wa amri
    env=None,  # Mabadiliko ya mazingira ya hiari
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

Kwanza, utahitaji kuongeza utegemezi wa LangChain4j kwenye faili yako ya `pom.xml`. Ongeza utegemezi huu kuwezesha ushirikiano wa MCP na API ya MiniMax inayolingana na OpenAI:

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

Weka ufunguo wako wa MiniMax API, na ikiwa utapenda, pia upe endpoint na modeli.
`MINIMAX_MODEL_ID` inasaidia `MiniMax-M3` na `MiniMax-M2.7`. Ikiwa
`OPENAI_BASE_URL` haijatolewa, `MINIMAX_REGION` inasaidia `global_en` na `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Ili kuchagua endpoint kwa mkoa badala yake, acha `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
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

        // Tengeneza usafirishaji wa MCP wa kuungana na seva
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

Katika msimbo uliotangulia tumefanya:

- **Kuongeza utegemezi wa LangChain4j**: Unaohitajika kwa ushirikiano wa MCP na API ya MiniMax inayolingana na OpenAI
- **Kuleta maktaba za LangChain4j**: Kwa ushirikiano wa MCP na utendaji wa modeli za mazungumzo za OpenAI
- **Kuunda `ChatLanguageModel`**: Kusanidi kutumia MiniMax na ufunguo wako wa API wa MiniMax, endpoint, na ID ya modeli inayounga mkono
- **Kuweka usafirishaji wa HTTP**: Kutumia Matukio Yanayotumwa na Seva (SSE) kuungana na seva ya MCP
- **Kuunda mteja wa MCP**: Atakayesimamia mawasiliano na seva
- **Kutumia msaada wa MCP wa LangChain4j uliopo ndani**: Ambayo huwezesha ushirikiano kati ya LLMs na seva za MCP

#### Rust

Mfano huu unadhani una seva ya MCP inayotumia Rust inayoendesha. Ikiwa huna moja, rejelea somo la [01-first-server](../01-first-server/README.md) kuunda seva.

Mara utakapopata seva yako ya MCP ya Rust, fungua terminal na nenda kwenye saraka ile ile kama seva. Kisha endesha amri ifuatayo kuunda mradi mpya wa mteja LLM:

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
> Hakuna maktaba rasmi ya Rust kwa OpenAI, hata hivyo, `async-openai` ni [maktaba inayotunzwa na jamii](https://platform.openai.com/docs/libraries/rust#rust) inayotumiwa sana.

Fungua faili ya `src/main.rs` na badilisha yaliyomo na msimbo ufuatao:

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

    // TODO: Mazungumzo ya LLM na kuitisha zana

    Ok(())
}
```

Msimbo huu unaandaa programu ya Rust ya msingi ambayo itaungana na seva ya MCP na GitHub Models kwa mwingiliano wa LLM.

> [!IMPORTANT]
> Hakikisha kuweka thabiti ya mazingira `OPENAI_API_KEY` na tokeni yako ya GitHub kabla ya kuendesha programu.

Vizuri, kwa hatua yetu inayofuata, hebu orodhesha uwezo wa seva.

### -2- Orodhesha uwezo wa seva

Sasa tutaunganisha na seva na kuulizia uwezo wake:

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

Katika msimbo uliotangulia tumefanya:

- Kuongeza msimbo wa kuungana na seva, `connectToServer`.
- Kuunda njia ya `run` inayosimamia mtiririko wa programu yetu. Hadi sasa inoorodhesha tu zana lakini tutaziongeza zaidi hivi karibuni.

#### Python

```python
# Orodha ya rasilimali zinazopatikana
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Orodha ya zana zinazopatikana
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Hapa tuliongeza:

- Kuorodhesha rasilimali na zana na kukatiza kwenye skrini. Kwa zana pia tumeorodhesha `inputSchema` ambayo tutaitumia baadaye.

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

- Kuorodhesha zana zilizo kwenye seva ya MCP
- Kwa kila zana, kuorodhesha jina, maelezo na muundo wake. Hili ni jambo tutakalotumia kuitisha zana hizi baadaye.

#### Java

```java
// Tengeneza mtoa zana anayegundua zana za MCP kiotomatiki
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Mtoa zana wa MCP huhudumia kiotomatiki:
// - Orodhesha zana zinazopatikana kutoka kwa seva ya MCP
// - Kubadilisha mifumo ya zana za MCP kuwa muundo wa LangChain4j
// - Kusimamia utekelezaji wa zana na majibu
```

Katika msimbo uliotangulia tumefanya:

- Kuunda `McpToolProvider` inayogundua moja kwa moja na kusajili zana zote kutoka seva ya MCP
- Mtoaji wa zana hushughulikia uongofu kati ya miundo ya zana za MCP na muundo wa zana wa LangChain4j ndani yake
- Njia hii inaanikia mwendo wa orodha ya mikono na mchakato wa uongofu

#### Rust

Kupata zana kutoka kwa seva ya MCP hufanywa kwa kutumia njia ya `list_tools`. Katika `main` yako, baada ya kuweka mteja wa MCP, ongeza msimbo ufuatao:

```rust
// Pata orodha ya zana za MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Geuza uwezo wa seva kuwa zana za LLM

Hatua inayofuata baada ya kuorodhesha uwezo wa seva ni kugeuza kuwa muundo ambao LLM inaelewa. Mara tunapofanya hivyo, tunaweza kutoa uwezo huo kama zana kwa LLM yetu.

#### TypeScript

1. Ongeza msimbo ufuatao kubadilisha majibu kutoka MCP Server kuwa muundo wa zana ambazo LLM inaweza kutumia:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Unda schema ya zod kulingana na input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Weka aina kuwa "function" waziwazi
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

    Msimbo ulio hapo juu unachukua jibu kutoka MCP Server na kuubadilisha kuwa muundo wa zana ambao LLM inaweza kuelewa.

2. Hebu sasa sasisha njia ya `run` kuorodhesha uwezo wa seva:

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

    Katika msimbo uliotangulia, tumesasisha njia ya `run` kupita matokeo na kwa kila kipengee kuita `openAiToolAdapter`.

#### Python

1. Kwanza, hebu tuunde kipengele kinachobadilisha:

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

    Katika kipengele cha `convert_to_llm_tools` tunachukua jibu la zana ya MCP na kulibadilisha kuwa muundo ambao LLM inaweza kuelewa.

2. Kisha, hebu sasisha msimbo wetu wa mteja kutumia kipengele hiki kama ifuatavyo:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Hapa tumeongeza wito wa `convert_to_llm_tool` kubadilisha jibu la zana ya MCP kuwa kitu ambacho tunaweza kumpa LLM baadaye.

#### .NET

1. Hebu ongezea msimbo kubadilisha jibu la zana ya MCP kuwa kitu LLM inaweza kuelewa

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

- Kuunda kazi ya `ConvertFrom` inayochukua jina, maelezo na muundo wa ingizo.
- Kufafanua utendaji unaounda FunctionDefinition inayopita kwa ChatCompletionsDefinition. Hii ni kitu LLM inaweza kuelewa.

2. Hebu tazama jinsi tunavyoweza kusasisha sehemu ya msimbo iliyopo ili kutumia kazi hii hapa juu:

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
// Tengeneza kiolesura cha Bot kwa mawasiliano ya lugha asili
public interface Bot {
    String chat(String prompt);
}

// Sanidi huduma za AI na zana za LLM na MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Katika msimbo uliotangulia tumefanya:

- Tumeunda interface rahisi ya `Bot` kwa mwingiliano wa lugha asilia
- Tumetumia `AiServices` za LangChain4j kufunga moja kwa moja LLM na mtoaji wa zana MCP
- Mfumo huu unaendesha moja kwa moja mchakato wa uongofu wa miundo ya zana na kuitisha kazi kando ya pazia
- Njia hii huondoa uongofu wa mikono wa zana - LangChain4j hushughulikia ugumu wote wa kubadilisha zana za MCP kuwa muundo unaoungwa mkono na LLM

#### Rust

Kubadilisha jibu la zana ya MCP kuwa muundo ambao LLM inaweza kuelewa, tutaongeza kipengele cha msaada kinachopanga orodha ya zana. Ongeza msimbo ufuatao kwenye faili yako ya `main.rs` chini ya kazi ya `main`. Hii itaitwa wakati wa kutuma maombi kwa LLM:

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

Vizuri, hatujaandaa kwa kushughulikia maombi ya mtumiaji, hivyo hebu tushughulikie hilo sasa.

### -4- Shughulikia ombi la maelekezo ya mtumiaji

Katika sehemu hii ya msimbo, tutashughulikia maombi ya watumiaji.

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

    Katika msimbo uliotangulia tumefanya:

    - Kuongeza njia `callTools`.
    - Njia hii inachukua jibu la LLM na kuangalia ni zana gani zilitumika, ikiwa zipo:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // piga zana
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

        // 3. Fanya jambo fulani na matokeo
        // TODO
        ```

2. Sasisha njia ya `run` kujumuisha wito kwa LLM na kuitisha `callTools`:

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

    // 2. Kupiga simu LLM
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

Vizuri, hebu orodhesha msimbo mzima:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Ingiza zod kwa uthibitishaji wa schema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // huenda ukahitaji kubadilisha kwenda url hii siku zijazo: https://models.github.ai/inference
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
    
        // 3. Pitia majibu ya LLM, kwa kila chaguo, angalia kama ina miito ya zana
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

1. Ongeza baadhi ya kuleta maktaba zinazohitajika kuitisha LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Kisha, ongeza kazi itakayoitisha LLM:

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
    - Kisha tumeiita LLM kwa kazi hizo.
    - Kisha, tunachunguza matokeo kuona ni kazi gani tunapaswa kuitisha, ikiwa zipo.
    - Hatimaye, tunapitia safu ya kazi kuitisha.

3. Hatua ya mwisho, hebu sasisha msimbo wetu mkuu:

    ```python
    prompt = "Add 2 to 20"

    # muulize LLM zana gani zote, kama zipo
    functions_to_call = call_llm(prompt, functions)

    # ita simu za kazi zilizopendekezwa
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Hapo, hii ilikuwa hatua ya mwisho, katika msimbo hapo juu tunafanya:

    - Kuitisha zana ya MCP kupitia `call_tool` kwa kutumia kazi ambayo LLM ilidhani inapaswa kuitwa kulingana na maelekezo yetu.
    - Kuchapisha matokeo ya wito wa zana kwa seva ya MCP.

#### .NET

1. Tuonyeshe baadhi ya msimbo wa kufanya ombi la maelekezo ya LLM:

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

    - Kupata zana kutoka kwa seva ya MCP, `var tools = await GetMcpTools()`.
    - Kuweka maelekezo ya mtumiaji `userMessage`.
    - Kuunda chaguo la constructor ambalo linaeleza modeli na zana.
    - Kutuma ombi kwa LLM.

2. Hatua moja ya mwisho, hebu tazame kama LLM inadhani tunapaswa kuitisha kazi:

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

    - Kurudia kupitia orodha ya wito wa kazi.
    - Kwa kila wito wa zana, chambua jina na hoja na uitishe zana kwenye seva ya MCP kwa kutumia mteja wa MCP. Hatimaye tunachapisha matokeo.

Huu ndio msimbo kamili:

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
    // Tekeleza ombi za lugha ya asili zinazotumia zana za MCP kiotomatiki
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

- Kutumia maelekezo rahisi ya lugha asilia kuingiliana na zana za seva ya MCP
- Mfumo wa LangChain4j unaendesha moja kwa moja:
  - Kubadilisha maelekezo ya mtumiaji kuwa wito wa zana wakati zinapohitajika
  - Kuitisha zana za MCP zinazofaa kulingana na uamuzi wa LLM
  - Kusimamia mtiririko wa mazungumzo kati ya LLM na seva ya MCP
- Njia `bot.chat()` hurudisha majibu ya lugha asilia ambayo yanaweza kujumuisha matokeo kutoka kwa utekelezaji wa zana za MCP
- Njia hii inatoa uzoefu usio na mshono kwa mtumiaji ambapo watumiaji hawahitaji kujua kuhusu utekelezaji wa MCP unao nyuma

Mfano kamili wa msimbo:

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


Hapa ndipo kazi nyingi hutokea. Tutaita LLM na ombi la mtumiaji la awali, kisha tukashughulikie majibu kuona kama kuna zana zozote zinazohitaji kuitwa. Ikiwa kuna, tutaita zile zana na kuendelea na mazungumzo na LLM hadi haita hitaji marudio yoyote ya zana na tunapokuwa na jibu la mwisho.

Tutakuwa tukifanya miito mingi kwa LLM, kwa hivyo wacha tueleze kazi itakayo shughulikia kuitwa kwa LLM. Ongeza kazi ifuatayo kwenye faili yako `main.rs`:

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

Kazi hii inachukua mteja wa LLM, orodha ya meseji (ikiwa pamoja na ombi la mtumiaji), zana kutoka kwa seva ya MCP, na kutuma ombi kwa LLM, ikirejesha jibu.

Jibu kutoka kwa LLM litakuwa na safu ya `choices`. Tutahitaji kushughulikia matokeo kuona kama kuna `tool_calls`. Hii inatufahamisha kuwa LLM inataka zana maalum iitwe na hoja zake. Ongeza msimbo ifuatayo chini ya faili yako `main.rs` kuanzisha kazi ya kushughulikia jibu la LLM:

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

    // Shughulikia simu za chombo
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Ongeza ujumbe wa msaidizi

        // Tekeleza kila simu ya chombo
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Ongeza matokeo ya chombo kwenye ujumbe
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Endelea mazungumzo na matokeo ya chombo
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

Ikiwa `tool_calls` zipo, inachukua taarifa za zana, inaita seva ya MCP na ombi la zana, na kuongeza matokeo kwenye meseji za mazungumzo. Kisha inaendelea na mazungumzo na LLM na meseji zinasasishwa na majibu ya msaidizi na matokeo ya kuitwa kwa zana.

Ili kupata taarifa za kuitwa kwa zana ambazo LLM inarudisha kwa miito ya MCP, tutaongeza kazi nyingine ya msaada kupata kila kitu kinachohitajika kufanya kuitwa. Ongeza msimbo ifuatayo chini ya faili yako `main.rs`:

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

Sasa tunapo kuwa na sehemu zote, tunaweza kushughulikia ombi la mtumiaji la awali na kuita LLM. Sasisha kazi yako `main` kujumuisha msimbo ifuatayo:

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

Hii itamwuliza LLM kwa ombi la mtumiaji la awali akitaka jumla ya nambari mbili, na itashughulikia jibu kudhibiti kwa njia ya mabadiliko kuitwa kwa zana.

Nzuri, umefanya kazi!

## Kazi ya Nyumbani

Chukua msimbo kutoka kwa zoezi na ujenge seva zaidi na baadhi zana zaidi. Kisha tengeneza mteja na LLM, kama vile zoezini, na ujitihada na maombi tofauti kuhakikisha zana zako zote za seva zinaitwa kwa mpangilio madhubuti. Njia hii ya kujenga mteja inamaanisha mtumiaji wa mwisho atakuwa na uzoefu mzuri wa mtumiaji kwa kuwa anaweza kutumia maombi badala ya amri kamili za mteja, na hakuwa na ufahamu wowote wa MCP server inapoitwa.

## Suluhisho

[Suluhisho](./solution/README.md)

## Mambo Muhimu Kukumbuka

- Kuongeza LLM kwenye mteja wako hutoa njia nzuri kwa watumiaji kuwasiliana na Seva za MCP.
- Unahitaji kubadilisha jibu la Seva ya MCP kuwa kitu ambacho LLM inaweza kuelewa.

## Sampuli

- [Kalkuleta ya Java](../samples/java/calculator/README.md)
- [Kalkuleta ya .Net](../../../../03-GettingStarted/samples/csharp)
- [Kalkuleta ya JavaScript](../samples/javascript/README.md)
- [Kalkuleta ya TypeScript](../samples/typescript/README.md)
- [Kalkuleta ya Python](../../../../03-GettingStarted/samples/python)
- [Kalkuleta ya Rust](../../../../03-GettingStarted/samples/rust)

## Rasilimali Zaidi

## Nini Kifuatayo

- Kifuatayo: [Kutumia seva kwa Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->