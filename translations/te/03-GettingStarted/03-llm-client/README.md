# LLMతో క్లయింట్ సృష్టించడం

ఇప్పటివరకు మీరు సర్వర్ మరియు క్లయింట్ ఎలా సృష్టించాలో చూశారు. క్లయింట్ స్పష్టంగా సర్వర్‌ను కాల్ చేసి దాని టూల్స్, వనరులు మరియు ప్రాంప్ట్స్ జాబితా చేయగలిగింది. అయినప్పటికీ, ఇది చాలా ప్రాక్టికల్ దృక్పథం కాదు. మీ వినియోగదారులు ఏజెంటిక్ యుగంలో నివసిస్తున్నారు మరియు ప్రాంప్ట్స్ ఉపయోగించి LLMతో కమ్యూనికేట్ చేయాలని ఆశిస్తున్నారు. వారు మీ సామర్థ్యాలను నిల్వ చేయడానికి MCPను ఉపయోగిస్తారా లేదా అంటే మాదిరిగా చూడరు; వారు సహజ భాషను ఉపయోగించి పరస్పరం చర్యలు జరపాలని మాత్రమే ఆశిస్తున్నారు. అందువలన దీన్ని ఎలా పరిష్కరిస్తారు? పరిష్కారం క్లయింట్‌కు LLMను చేర్చడంలో ఉంది.

## అవలోకనం

ఈ పాఠంలో, మీ క్లయింట్‌లో LLMను చేర్చడం మరియు దీని ద్వారా మీ వినియోగదారులకు మరింత మెరుగైన అనుభవం అందించడం పై దృష్టి సారిస్తాము.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ముగింపునకు, మీరు చేయగలుగుతారు:

- LLMతో కూడిన క్లయింట్ సృష్టించడం.
- LLMను ఉపయోగించి MCP సర్వర్‌తో సులభంగా పరస్పర చర్యలు చేయడం.
- క్లయింట్ వైపు మెరుగైన చివరి వినియోగదారు అనుభవాన్ని అందించడం.

## దృష్టాంతం

మనం తీసుకోవలసిన దృష్టాంతాన్ని అర్థం చేసుకుందాం. LLMను చేర్చడం సులభంగా అనిపించినా ఇది సరైన విధంగా చేస్తామా?

క్లయింట్ సర్వర్‌తో ఎలా పరస్పరం చేస్తుందో ఇలా ఉంది:

1. సర్వర్‌తో కనెక్షన్ ఏర్పరచడం.

1. సామర్థ్యాలు, ప్రాంప్ట్స్, వనరులు మరియు టూల్స్ జాబితా చేయడం, మరియు వాటి స్కీమాను సేవ్ చేయడం.

1. LLMను చేర్చడం మరియు సేవ్ చేసుకున్న సామర్థ్యాలు మరియు వాటి స్కీమాను LLM అర్థం చేసుకునే ఫార్మాట్‌లో అందించడం.

1. వాటి జాబితా చేసిన టూల్స్‌తో యూజర్ ప్రాంప్ట్‌ను LLMకు పంపించడం.

బాగుంది, ఇప్పుడు మనం ఈ దృష్టాంతం పై అవగాహన సాధించాము, కింద ఉన్న వ్యాయామంలో దీన్ని ప్రయత్నిద్దాం.

## వ్యాయామం: LLMతో క్లయింట్ సృష్టించడం

ఈ వ్యాయామంలో, మేము మా క్లయింట్‌కు LLMను చేర్చడం నేర్చుకుంటాము.

### GitHub Personal Access Token ఉపయోగించి удостоверение

GitHub టోకెన్ సృష్టించడం సులభమైన ప్రక్రియ. మీరు ఇలా చేయవచ్చు:

- GitHub సెట్టింగ్స్‌కు వెళ్లండి – మీ ప్రొఫైల్ చిత్రం పై భాగం కుడివైపున క్లిక్ చేసి సెట్టింగ్స్ ఎంచుకోండి.
- డెవలపర్ సెట్టింగ్స్‌కు వెళ్లండి – స్క్రోలు చేసి డెవలపర్ సెట్టింగ్స్‌పై క్లిక్ చేయండి.
- Personal Access Tokens ఎంచుకోండి – Fine-grained tokens పై క్లిక్ చేసి Generate new token క్లిక్ చేయండి.
- మీ టోకెన్‌ను కాన్ఫిగర్ చేయండి – రిఫరెన్స్ కోసం ఒక నోట్ జత చేయండి, సమాప్తి తేదీని సెట్ చేయండి మరియు అవసరమైన స్కోప్స్ (హక్కులు) ఎంచుకోండి. ఈ సందర్భంలో Models అనుమతిని తప్పనిసరిగా జత చేయండి.
- టోకెన్‌ను జనరేట్ చేసి కాపీ చేసుకోండి – Generate token పై క్లిక్ చేసి వెంటనే దాన్ని కాపీ చేసుకోండి, ఎందుకంటే మీరు దాన్ని తిరిగి చూడలేరు.

### -1- సర్వర్‌కు కనెక్ట్ అవ్వండి

ముందుగా మన క్లయింట్‌ను సృష్టిద్దాం:

#### టైప్‌స్క్రిప్ట్

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా ప్రయామాణికత కోసం zod ని దిగుమతి చేయండి

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

పూర్వపు కోడ్‌లో మేము:

- అవసరమైన లైబ్రరీలను దిగుమతించాము
- `client` మరియు `openai` అనే రెండు సభ్యులతో ఒక క్లాస్ సృష్టించాము, ఇది మనకు క్లయింట్ నిర్వహణ మరియు LLMతో పరస్పరం చేయడానికి సహాయం చేస్తుంది.
- GitHub Models ఉపయోగించడానికి మన LLM ఇన్‌స్టాన్స్‌ను `baseUrl` సెట్టింగ్ ద్వారా కన్ఫిగర్ చేసాము, ఇది ఇన్ఫరెన్స్ APIని సూచిస్తుంది.

#### పైథాన్

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio కనెక్షన్ కోసం సర్వర్ పరామితులను సృష్టించండి
server_params = StdioServerParameters(
    command="mcp",  # అమలు చేసేందుకు
    args=["run", "server.py"],  # ఐచ్ఛిక కమాండ్ లైన్ ఆర్గుమెంట్స్
    env=None,  # ఐచ్ఛిక పర్యావరణ మార్పిదారులు
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # కనెక్షన్‌ను ప్రారంభించండి
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

పూర్వపు కోడ్‌లో మేము:

- MCPకి అవసరమైన లైబ్రరీలను దిగుమతించాము
- క్లయింట్‌ను సృష్టించాము

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

#### జావా

ముందుగా, మీరు మీ `pom.xml` ఫైల్‌లో LangChain4j డిపెండెన్సీలు జత చేయాలి. MCP ఇంటిగ్రేషన్ మరియు OpenAI-కి అనుకూలమైన MiniMax APIని యాక్టివేట్ చేయడానికి ఈ డిపెండెన్సీలు జోడించండి:

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

మీ MiniMax API కీని సెటుచేసుకోండి మరియు ఆప్షనల్‌గా ఎండ్‌పాయింట్ మరియు మోడల్‌ను కూడా సెట్ చేయండి.
`MINIMAX_MODEL_ID` కోసం `MiniMax-M3` మరియు `MiniMax-M2.7` మద్దతు ఉంది. 
`OPENAI_BASE_URL` సెటుచేయబడలేదు అయితే, `MINIMAX_REGION`కి `global_en` మరియు `cn_zh` మద్దతు ఉంది.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

ఏ రీజియన్ ఆధారంగా ఎండ్‌పాయింట్‌ని ఎంచుకోవాలంటే, `OPENAI_BASE_URL`ని వదిలివేయండి:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

తరువాత మీ జావా క్లయింట్ క్లాస్‌ని సృష్టించండి:

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

        // సర్వర్‌కు కనెక్ట్ కావడానికి MCP రవాణాను సృష్టించండి
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP క్లయింట్‌ను సృష్టించండి
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

పూర్వపు కోడ్‌లో మేము:

- **LangChain4j డిపెండెన్సీలు జత చేసినవి**: MCP ఇంటిగ్రేషన్ మరియు OpenAI-అనుకూల MiniMax APIకి అవసరం
- **LangChain4j లైబ్రరీలను దిగుమతించాము**: MCP ఇంటిగ్రేషన్ మరియు OpenAI చాట్ మోడల్ ఫంక్షనాలిటీ కోసం
- **`ChatLanguageModel` సృష్టించాము**: MiniMax API కీ, ఎండ్‌పాయింట్ మరియు మద్దతు ఉన్న మోడల్ IDతో MiniMax ఉపయోగించడానికి కన్ఫిగర్ చేసినది
- **HTTP ట్రాన్స్‌పోర్ట్ సెటప్ చేసాము**: Server-Sent Events (SSE) ఉపయోగించి MCP సర్వర్‌తో కనెక్ట్ అవ్వడానికి
- **MCP క్లయింట్ సృష్టించాము**: సర్వరుతో కమ్యూనికేషన్ నిర్వహించడానికి
- **LangChain4j లో బిల్ట్-ఇన్ MCP సపోర్ట్ ఉపయోగించాము**: ఇది LLM మరియు MCP సర్వర్లు మధ్య ఇంటిగ్రేషన్ సులభతరం చేస్తుంది

#### రస్ట్

ఈ ఉదాహరణకు, మీరు ఒక రస్ట్ ఆధారిత MCP సర్వర్ నడుపుతున్నారు అని భావించబడుతుంది. మీకి సర్వర్ లేదు అయితే, [01-first-server](../01-first-server/README.md) పాఠానికి తిరిగి వెళ్లి సర్వర్ సృష్టించండి.

మీరు మీ రస్ట్ MCP సర్వర్ సిద్ధంగా ఉన్న తర్వాత, ఒక టెర్మినల్ తెరిచి సర్వర్ ఉన్న డైరెక్టరీకి పోయి క్రింది ఆదేశాన్ని చూపించి కొత్త LLM క్లయింట్ ప్రాజెక్ట్ సృష్టించండి:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

మీ `Cargo.toml` ఫైల్‌లో క్రింది డిపెండెన్సీలు జోడించండి:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAIకి అధికారిక రస్ట్ లైబ్రరీ లేదు, అయితే `async-openai` క్రేట్ ఒక [కమ్యూనిటీ నిర్వహించబడే లైబ్రరీ](https://platform.openai.com/docs/libraries/rust#rust) గా విస్తృతంగా ఉపయోగించబడుతోంది.

`src/main.rs` ఫైల్ తెరిచి దాని కంటెంట్‌ని క్రింది కోడ్‌తో మార్చండి:

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
    // ప్రారంభ సందేశం
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI క్లయింట్‌ని సెట్ చేయండి
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP క్లయింట్‌ని సెట్ చేయండి
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

    // TODO: MCP టూల్ జాబితాను పొందండి

    // TODO: టూల్ కాల్‌లతో LLM సంభాషణ్

    Ok(())
}
```

ఈ కోడ్ బేసిక్ రస్ట్ అప్లికేషన్‌ని సెట్ చేస్తుంది, ఇది MCP సర్వర్ మరియు GitHub Modelsతో LLM పరస్పర చర్యలకు కనెక్ట్ అవుతుంది.

> [!IMPORTANT]
> అప్లికేషన్ ను నడపడాన్ని ముందుగా `OPENAI_API_KEY` ఎన్విరోన్మెంట్ వేరియబుల్ లో మీ GitHub టోకెన్ ని సెట్ చేయండి.

బాగుంది, తదుపరి దశకు త్వరగా వెళ్లి సర్వర్ సామర్థ్యాలను జాబితా చేద్దాం.

### -2- సర్వర్ సామర్థ్యాలను జాబితా చేయండి

ఇప్పుడు మనం సర్వర్‌కి కనెక్ట్ అవ్వడానికి మరియు దాని సామర్థ్యాలను అడగబోతున్నాము:

#### టైప్‌స్క్రిప్ట్

అదే క్లాస్‌లో క్రింది విధానాలను జోడించండి:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // పరికరాలను జాబితా చేయడం
    const toolsResult = await this.client.listTools();
}
```

పూర్వపు కోడ్‌లో మేము:

- సర్వర్‌కు కనెక్ట్ చేయడం కోసం కోడ్ జోడించాము, `connectToServer`.
- మా యాప్ ఫ్లో నిర్వహించడం కోసం `run` మెథడ్ను సృష్టించాము. ఇప్పటివరకు ఇది టూల్స్ మాత్రమే జాబితా చేస్తోంది కానీ త్వరలో మరిన్ని ఫీచర్లు జోడిస్తాము.

#### పైథాన్

```python
# అందుబాటు ఉన్న వనరులను జాబితా చేయండి
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# అందుబాటు ఉన్న పరికరాలను జాబితా చేయండి
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

మేము జోడించినవి:

- వనరులు మరియు టూల్స్ జాబితా చేసి వాటిని ప్రింట్ చేశారు. టూల్స్‌కి `inputSchema` కూడా జాబితా చేసాము, దీన్ని తర్వాత ఉపయోగిస్తాము.

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

పూర్వపు కోడ్‌లో మేము:

- MCP సర్వర్‌లో అందుబాటులో ఉన్న టూల్స్ జాబితా చేసినాము
- ప్రతి టూల్కు పేరు, వివరాలు మరియు దాని స్కీమా జాబితా చేశారు. తరువాత ఈ స్కీమాను టూల్స్ కాల్ చేయడానికి ఉపయోగిస్తాము.

#### జావా

```java
// ఆటోమేటిక్‌గా MCP టూల్స్‌ని గుర్తించే టూల్ ప్రొవైడర్‌ను సృష్టించండి
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP టూల్ ప్రొవైడర్ ఆటోమేటిక్‌గా నిర్వహిస్తుంది:
// - MCP సర్వర్ నుండి అందుబాటులో ఉన్న టూల్స్ ని జాబితా చేయడం
// - MCP టూల్ స్కీమాలను LangChain4j ఫార్మాట్‌కు మార్చడం
// - టూల్ నిర్వహణ మరియు స్పందనలను నిర్వహించడం
```

పూర్వపు కోడ్‌లో మేము:

- MCP సర్వర్ నుండి అన్ని టూల్స్‌ను ఆటోమేటిక్‌గా కనుగొని నమోదు చేసే `McpToolProvider` సృష్టించాము
- MCP టూల్ స్కీమాలు మరియు LangChain4j టూల్ ఫార్మాట్ మధ్య మడిచే మార్పిడి ఒకటిగా టూల్ ప్రొవైడర్ నిర్వహిస్తోంది
- ఈ విధానం మనవంటి చేతిపనిలా టూల్స్ జాబితా మరియు మార్పిడి ప్రాసెస్‌ను లైను అవుతుంది

#### రస్ట్

MCP సర్వర్ నుండి టూల్స్‌ను పొందడం కోసం `list_tools` మెథడ్ వాడబడుతుంది. మీ `main` ఫంక్షన్‌లో MCP క్లయింట్‌ను సెట్ చేసుకున్న తరువాత, క్రింది కోడ్ జోడించండి:

```rust
// MCP టూల్ జాబితాను పొందండి
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- సర్వర్ సామర్థ్యాలను LLM టూల్స్‌గా మార్చండి

సర్వర్ సామర్థ్యాలను జాబితా చేశాక, వాటిని LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చండి. అప్పుడు ఆ సామర్థ్యాలను LLMకు టూల్స్‌గా అందించవచ్చు.

#### టైప్‌స్క్రిప్ట్

1. MCP సర్వర్ నుండి వచ్చిన ప్రతిస్పందనని LLM ఉపయోగించే టూల్ ఫార్మాట్‌లోకి మార్చే క్రింది కోడ్‌ను జోడించండి:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ఇన్‌పుట్_స్కీమా ఆధారంగా ఒక జోడ్ స్కీమాను సృష్టించండి
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // తరహాను "ఫంక్షన్" గా స్పష్టంగా సెట్ చేయండి
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

    పై కోడ్ MCP సర్వర్ నుండి వచ్చిన ప్రతిస్పందనని LLM అర్థం చేసుకునే టూల్ నిర్వచన ఫార్మాట్‌గా మార్చుతుంది.

2. తరువాత `run` మెథడ్‌ను క్రింది విధంగా సవరించండి, సర్వర్ సామర్థ్యాలను జాబితా చేయడానికి:

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

    పూర్వపు కోడ్‌లో `run` మెథడ్‌ను ఫలితంలో జాబితా చేయడానికి మరియు ప్రతి ఎంట్రీకి `openAiToolAdapter` పిలవడానికి నవీకరించాము.

#### పైథాన్

1. మొదట, క్రింది కన్వర్టర్ ఫంక్షన్ సృష్టిద్దాం

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

    పై ఫంక్షన్ `convert_to_llm_tools` లో MCP టూల్ ప్రతిస్పందనని LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చతాం.

2. తరువాత మా క్లయింట్ కోడ్‌ను ఈ విధంగా నవీకరించండి:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ఇక్కడ, మనం MCP టూల్ ప్రతిస్పందనను LLMకి తినిపించదగిన ఫార్మాట్‌గా మార్చడానికి `convert_to_llm_tool` పిలవడం జోడిస్తున్నాము.

#### .NET

1. MCP టూల్ ప్రతిస్పందనను LLM అర్థం చేసుకునే రూపంలోకి మార్పిడి చేసే కోడ్‌ను జోడిద్దాం

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

పూర్వపు కోడ్‌లో మేము:

- `ConvertFrom` అనే ఫంక్షన్ సృష్టించాము, ఇది పేరు, వివరణ, మరియు ఇన్‌పుట్ స్కీమాను తీసుకుంటుంది.
- ఈ ఫంక్షన్ చాట్ కంప్లీషన్ డిఫినిషన్‌కు పంపే ఫంక్షన్ డిఫినిషన్ సృష్టించడాన్ని నిర్వచిస్తుంది, ఇది LLM అర్థం చేసుకుంటుంది.

2. తరువాత మనం ఈ ఫంక్షన్ ఉపయోగించడానికి కొద్దిగా మునుపటి కోడ్ ఎలా నవీకరించవచ్చో చూద్దాం:

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

#### జావా

```java
// సహజ భాషా మోకాలికి బోట్ ఇంటర్‌ఫేస్‌ని సృష్టించండి
public interface Bot {
    String chat(String prompt);
}

// LLM మరియు MCP సాధనాలతో AI సేవను ఏర్పాటు చేయండి
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

పూర్వపు కోడ్‌లో మేము:

- సహజ భాషా పరస్పర చర్యలకు సరళమైన `Bot` ఇంటర్‌ఫేజ్ నిర్వచించాము
- MCP టూల్ ప్రొవైడర్‌తో ఆటోమేటిక్‌గా LLMని బైండ్ చేయడానికి LangChain4j యొక్క `AiServices` ఉపయోగించాము
- ఫ్రేమ్‌వర్క్ టూల్ స్కీమా మార్పిడి మరియు ఫంక్షన్ కాల్లింగ్‌ను వెనుక స్టేజీలో స్వయంచాలకంగా నిర్వహిస్తుంది
- ఈ పద్ధతి చేతితో టూల్ మార్పిడి అవసరాన్ని తొలగిస్తుంది - LangChain4j MCP టూల్స్‌ను LLM అనుకూల ఫార్మాట్‌గా మార్పిడి చేసే క్లిష్టతను పూరిస్తుంది

#### రస్ట్

MCP టూల్ ప్రతిస్పందనని LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చడానికి, మేము టూల్స్ జాబితాను ఫార్మాట్ చేసే సహాయక ఫంక్షన్‌ను జోడిస్తాం. `main.rs` ఫైల్‌లో `main` ఫంక్షన్ కింద క్రింది కోడ్ జోడించండి. ఇది LLMకు అభ్యర్థనలు చేసేటప్పుడు పిలవబడుతుంది:

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

బాగుంది, ఇప్పుడు మనం యూజర్ అభ్యర్థనలు నిర్వహించడానికి సిద్దంగా ఉన్నాము, కాబట్టి దీన్ని తరువాత చూద్దాం.

### -4- యూజర్ ప్రాంప్ట్ అభ్యర్థనను నిర్వహించండి

ఈ భాగంలో, మేము యూజర్ నడి అభ్యర్థనలను నిర్వహిస్తాము.

#### టైప్‌స్క్రిప్ట్

1. మన LLMను కాల్ చేయడానికి ఉపయోగించే ఒక మెథడ్ జోడించండి:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. సర్వర్ టూల్‌ను కాల్ చేయండి
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ఫలితంతో ఏదైనా చేయండి
        // చేయాల్సి ఉంది

        }
    }
    ```

    పూర్వపు కోడ్‌లో మేము:

    - `callTools` అనే మెథడ్ జోడించాము.
    - ఈ మెథడ్ LLM ప్రతిస్పందన తీసుకొని ఏ టూల్స్ కాల్ చేయబడినాయని తనిఖీ చేస్తుంది, ఉంటే:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // టూల్‌ని కాల్ చేయండి
        }
        ```

    - LLM సూచన ప్రకారం ఒక టూల్‌ను కాల్ చేస్తుంది:

        ```typescript
        // 2. సర్వర్ యొక్క సాధనం కాల్ చేయండి
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ఫలితంతో ఏదైనా చేయండి
        // చేయవలసింది
        ```

2. `run` మెథడ్‌ను LLMకు కాల్‌లు మరియు `callTools` పిలవడం భాగంగా నవీకరించండి:

    ```typescript

    // 1. LLM కోసం ఇన్‌పుట్ అయిన సందేశాలను సృష్టించండి
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ను పిలవడం
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ప్రతిస్పందనను గమనించండి, ప్రతి ఎంపికకు, దాని టూల్ కాల్స్ ఉన్నాయా అని తనిఖీ చేయండి
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

బాగుంది, పూర్తిగా కోడ్‌ను జాబితా చేద్దాం:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా సరి చూసుకోవడానికి zod ను దిగుమతి చేసుకోండి

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // భవిష్యత్తులో ఈ URL కి మార్చాలి కావచ్చు: https://models.github.ai/inference
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
          // ఇన్పుట్_స్కీమా ఆధారంగా zod స్కీమా సృష్టించండి
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // టైప్ ను స్పష్టంగా "function" గా సెట్ చేయండి
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
    
    
          // 2. సర్వర్ యొక్క టూల్ ను కాల్ చేయండి
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ఫలితంతో ఏదైనా చేయండి
          // చేయవలసినవి
    
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
    
        // 3. LLM స్పందన ద్వారా పోయి, ప్రతి ఎంపికకు టూల్ కాల్స్ ఉన్నాయా చెక్ చేయండి
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

#### పైథాన్

1. LLMను కాల్ చేయడానికి అవసరమైన కొన్ని దిగుమతులను జోడిద్దాం

    ```python
    # ఎల్ఎల్ఎం
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. తరువాత, LLMను పిలవడానికి క్రింది ఫంక్షన్‌ను జోడిద్దాం:

    ```python
    # ఎల్ఎల్‌ఎం

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
            # ఐచ్ఛిక పారామితులు
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

    పూర్వపు కోడ్‌లో మేము:

    - MCP సర్వర్‌లో కనుగొన్న మరియు మార్చిన ఫంక్షన్‌లను LLMకి ఇచ్చాము.
    - ఆపై ఆ ఫంక్షన్‌లతో LLMను పిలిచాం.
    - తరువాత ఫలితాన్ని పరిశీలించడంలో ఏฟంక్షన్‌లు కాల్ చేయాలో చూశాం.
    - చివరగా కాల్ చేయవలసిన ఫంక్షన్‌ల అర్రేను అందించాం.

3. తుది దశగా, మా ప్రధాన కోడ్‌ను నవీకరించుదాం:

    ```python
    prompt = "Add 2 to 20"

    # అవసరమైతే అన్ని టూల్స్ ఎటువంటి ఉన్నాయి అని LLM ని అడగండి
    functions_to_call = call_llm(prompt, functions)

    # సూచించిన ఫంక్షన్లను కాల్ చేయండి
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    అలాగె, పై కోడ్‌లో మేము:

    - LLM సూచించిన ఫంక్షన్ ద్వారా MCP టూల్‌ని `call_tool` గా పిలవడం.
    - MCP సర్వర్ నుంచి టూల్ కాల్ ఫలితాన్ని ప్రింట్ చేయడం.

#### .NET

1. LLM ప్రాంప్ట్ అభ్యర్థన కోసం కొద్దిగా కోడ్ చూపోడాం:

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

    పూర్వపు కోడ్‌లో మేము:

    - MCP సర్వర్ నుండి టూల్స్ తెయిన్, `var tools = await GetMcpTools()`.
    - యూజర్ ప్రాంప్ట్ `userMessage` నిర్వచించాము.
    - మోడల్ మరియు టూల్స్ స్పెసిఫై చేసే ఆప్షన్స్ ఆబ్జెక్ట్ రూపొందించాము.
    - LLMకి అభ్యర్థన పంపాము.

2. చివరి దశగా, LLM ఏ ఫంక్షన్‌లను కాల్ చేయాలో నిర్ణయిస్తే చూడండి:

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

    పూర్వపు కోడ్‌లో మేము:

    - ఫంక్షన్ కాల్‌ల జాబితాను లూప్ చేశాం.
    - ప్రతి టూల్ కాల్ కోసం పేరు మరియు ఆర్గుమెంట్లను పార్స్ చేసి MCP క్లయింట్ ఉపయోగించి టూల్‌ను MCP సర్వర్‌లో కాల్ చేసి ఫలితాలను ప్రింట్ చేశాం.

పూర్తి కోడ్ ఇక్కడ ఉంది:

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

#### జావా

```java
try {
    // స్వయంచాలకంగా MCP టూల్స్ ఉపయోగించే సహజ భాషా అభ్యర్థనలను అమలు చేయండి
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

పూర్వపు కోడ్‌లో మేము:

- MCP సర్వర్ టూల్స్‌తో సహజ భాషా ప్రాంప్ట్స్ ఉపయోగించి పరస్పరం చేశాము
- LangChain4j ఫ్రేమ్‌వర్క్ ఆటోమేటిక్‌గా నిర్వహిస్తుంది:
  - అవసరమైతే యూజర్ ప్రాంప్ట్‌లను టూల్ కాల్స్‌గా మార్చడం
  - LLM యొక్క నిర్ణయం ఆధారంగా సరైన MCP టూల్స్ కాల్ చేయడం
  - LLM మరియు MCP సర్వర్ మధ్య సంభాషణ ప్రవాహాన్ని నిర్వహించడం
- `bot.chat()` సహజ భాషా ప్రత్యుత్తరాలు ఇస్తుంది, అవి MCP టూల్ అమలు ఫలితాలను కూడా కలిగి ఉండవచ్చు
- ఈ దృష్టాంతం వినియోగదారులకు సజావుగా అనుభవాన్ని అందిస్తుంది, వారు MCP వ్యవస్థాపన గురించి తెలియవలసిన అవసరం లేదు

పూర్తి కోడ్ ఉదాహరణ:

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

#### రస్ట్

ఇక్కడ ఎక్కువ భాగం పని జరుగుతుంది. మేము ప్రారంభ యూజర్ ప్రాంప్ట్‌తో LLMను పిలిచువుతాము, తర్వాత స్పందనను పరిశీలించి టూల్స్‌కి కాల్ చేయవలసిన అవసరముందా చూడాలి. అవసరమైతే ఆ టూల్స్‌ని పిలువుతూ సంభాషణ కొనసాగిస్తారు LLMతో ముందుకు, మరింత టూల్ కాల్ అవసరం లేకుండా మరియు తుది స్పందన రావడంతో ముగియుతుంది.


మేము LLMకు అనేక రకాల కాల్స్ చేయబోతున్నాము, కాబట్టి LLM కాల్ ను నిర్వహించే ఫంక్షన్ ను నిర్వచిస్తాము. దిగువ ఫంక్షన్ ను మీ `main.rs` ఫైల్ కు జోడించండి:

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

ఈ ఫంక్షన్ LLM క్లయింట్, సందేశాల జాబితా (వాడుకరి ప్రాంప్ట్ సహా), MCP సర్వర్ నుండి టూల్స్ ను తీసుకుని, LLM కి అభ్యర్థన పంపి, ప్రతిస్పందనను తిరిగి ఇస్తుంది.

LLM నుండి వచ్చిన ప్రతిస్పందన `choices` అన్న అర్రే ను కలిగి ఉంటుంది. ఏ `tool_calls` ఉన్నాయో పరిశీలించడానికి ఫలితాన్ని ప్రాసెస్ చేయాలి. ఇది LLM నిర్దిష్ట టూల్‌ని ఆర్గ్యుమెంట్స్ తో పిలవాలని కోరుకోవడం అని మనకు తెలియజేస్తుంది. LLM ప్రతిస్పందనను నిర్వహించడానికి `main.rs` ఫైల్ unten టోపు కింద ఈ కోడ్ ను జోడించండి:

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

    // కంటెంట్ అందుబాటులో ఉంటే ప్రింట్ చేయండి
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // టూల్ కాల్‌లను నిర్వహించండి
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // అసిస్టెంట్ సందేశం జోడించండి

        // ప్రతి టూల్ کالును అమలు చేయండి
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // సందేశాలకు టూల్ ఫలితాన్ని జోడించండి
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // టూల్ ఫలితాలతో సంభాషణను కొనసాగించండి
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

`tool_calls` ఉంటే, అది టూల్ సమాచారాన్ని తీసుకుని, MCP సర్వర్ కి టూల్ అభ్యర్థనతో కాల్ చేస్తుంది, ఫలితాలను సంభాషణ సందేశాలకు జోడిస్తుంది. తరువాత LLM తో సంభాషణ కొనసాగిస్తూ సహాయకుడి ప్రతిస్పందన మరియు టూల్ కాల్ ఫలితాలతో సందేశాలు నవీకరించబడతాయి.

LLM MCP కాల్స్ కోసం తిరిగి ఇచ్చే టూల్ కాల్ సమాచారాన్ని తీయడానికి మరొక సహాయక ఫంక్షన్ ను జోడిద్దాం. `main.rs` ఫైల్ unten కింద ఈ కోడ్ ను జోడించండి:

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

అన్ని భాగాలు సిద్ధంగా ఉన్నప్పుడు, మేము మొదటి వాడుకరి ప్రాంప్ట్ ను నిర్వహించి LLMని కాల్ చేయగలము. మీ `main` ఫంక్షన్ లో ఈ క్రింది కోడ్ ను నవీకరించండి:

```rust
// టూల్ కాల్స్ తో LLM సంభాషణ
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

ఇది మొదటి వాడుకరి ప్రాంప్ట్ తో LLMని ప్రశ్నిస్తుందని రెండు సంఖ్యల యొక్క మొత్తాన్ని అడిగి, ప్రతిస్పందనను ప్రాసెస్ చేస్తూ టూల్ కాల్స్ ను డైనమిక్ గా నిర్వహిస్తుంది.

అద్భుతం, మీరు చేశారు!

## అసైన్‌మెంట్

వ్యాయామం నుండి కోడ్ తీసుకుని మరిన్ని టూల్స్ తో సర్వర్‌ని నిర్మించండి. తర్వాత వ్యాయామంలో ఉన్నట్లే LLMతో కూడిన క్లయింట్ సృష్టించి, వివిధ ప్రాంప్ట్‌లతో పరీక్షించండి. ఇలా ఒక క్లయింట్‌ను తయారు చేయడం వలన ఎండ్ యూజర్‌కి మంచి అనుభవం ఉంటుంది ఎందుకంటే వారు ఖచ్చితమైన క్లయింట్ ఆదేశాల బదులుగా ప్రాంప్ట్‌లను ఉపయోగించగలుగుతారు మరియు ఏ MCP సర్వర్ పిలవబడుతున్నదో తెలియదు.

## పరిష్కారం

[పరిష్కారం](./solution/README.md)

## ముఖ్యమైన విషయాలు

- మీ క్లయింట్‌లో LLMను జోడించడం వలన MCP సర్వర్లతో యూజర్లు మెరుగైన ఇన్‌టరాక్షన్ పొందగలుగుతారు.
- MCP సర్వర్ ప్రతిస్పందనను LLM అర్థం చేసుకునేలా మార్చాలి.

## నమూనాలు

- [జావా క్యాలిక్యులేటర్](../samples/java/calculator/README.md)
- [.Net క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/csharp)
- [జావాస్క్రిప్ట్ క్యాలిక్యులేటర్](../samples/javascript/README.md)
- [టైప్‌స్క్రిప్ట్ క్యాలిక్యులేటర్](../samples/typescript/README.md)
- [పైథాన్ క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/python)
- [రస్ట్ క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/rust)

## అదనపు వనరులు

## తరువాత ఏమి చేయాలి

- తదుపరి: [Visual Studio Code ఉపయోగించి సర్వర్ వినియోగించడం](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->