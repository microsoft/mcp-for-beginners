# LLM తో క్లయింట్ సృష్టించడం

> [!NOTE]
> జావా క్లయింట్ ఉదాహరణలు పూర్వ వైపు HTTP+SSE రవాణా ద్వారా కనెక్షన్ కా౦పించి
> MCP `2025-11-25` SDK APIs ని లక్ష్యంగా ఉంచతాయి. కొత్త రిమోట్ క్లయింట్ల కోసం `2026-07-28`-అనుకూల SDK మరియు
> స్ట్రీమబుల్ HTTP ఉపయోగించండి.

ఇప్పటివరకు, మీరు సర్వర్ మరియు క్లయింట్ ఎలా సృష్టించాలో చూశారు. క్లయింట్ స్పష్టంగా సర్వర్‌ను పిలిచి దాని టూల్స్, వనరులు మరియు ప్రాంప్ట్‌లను జాబితా చేయగలుగుతుంది. అయినప్పటికీ, ఇది చాలా ప్రాక్టికల్ దృక్కోణం కాదు. మీ వినియోగదారులు ఏజెంటిక్ యుగంలో నివసిస్తున్నారు మరియు ప్రాంప్ట్‌లు ఉపయోగించి మరియు LLM తో సంభాషించడానికి కోరుకుంటున్నారు. వారు మీరు MCP ను మీ సామర్ధ్యాలను నిల్వ చేయడానికి ఉపయోగించినా ఉపయోగించకపోయినా పట్టించుకోరు; వారు సహజ భాష ఉపయోగించి పరస్పర చర్యల్ని అంచనా వేస్తారు. అలాగె మనం దీన్ని ఎలా పరిష్కరించాలి? పరిష్కారం మీ క్లయింట్‌కు LLM ను జోడించడం.

## అవలోకనం

ఈ పాఠంలో మనం మీ క్లయింట్‌కు LLM ను జోడించడం పై దృష్టి పెడతాము మరియు ఇది మీ వినియోగదారుకు బహుళంగా మెరుగైన అనుభవం ఎలా అందిస్తుందో చూపిస్తాము.

## అభ్యాస లక్ష్యాలు

ఈ పాఠం ముగింపులో మీరు చేయగలుగుతారు:

- LLM తో క్లయింట్ సృష్టించండి.
- LLM ఉపయోగించి MCP సర్వర్‌తో సావధానంగా పరస్పర చర్య చేయండి.
- క్లయింట్ పక్కన మెరుగైన చివరి వినియోగదారు అనుభవాన్ని అందించండి.

## విధానం

మనం తీసుకోవలసిన విధానాన్ని అర్థం చేసుకుందాం. LLM ను జోడించడం సాధారణంగా అనిపిస్తే, మనం నిజంగా దీన్ని ఎలా చేయాలి?

క్లయింట్ సర్వర్‌తో ఎలా పరస్పర చర్య చేస్తుంది:

1. సర్వర్‌తో కనెక్షన్ ఏర్పాటు చేయండి.

1. సామర్ధ్యాలు, ప్రాంప్ట్‌లు, వనరులు మరియు టూల్స్ జాబితా చేయండి మరియు వారి స్కీమా నిల్వ చేయండి.

1. LLM ను జోడించి, నిల్వ చేసిన సామర్ధ్యాలు మరియు వారి స్కీమాను LLM అర్థం చేసుకునే ఫార్మాట్‌లో పాస్ చేయండి.

1. ఒక యూజర్ ప్రాంప్ట్‌ని క్లయింట్ ద్వారా జాబితా చేసిన టూల్స్‌తో పాటు LLM కు పాస్ చేయండి.

బాగుంది, ఇప్పుడు మనం ఎన్ని అధిక స్థాయిలో చేయగలమో అర్థం చేసుకున్నామని, వెంటనే క్రింది వ్యాయామంలో ప్రయత్నిద్దాం.

## వ్యాయామం: LLMతో క్లయింట్ సృష్టించడం

ఈ వ్యాయామంలో, మనం LLM ను మన క్లయింట్ కు జోడించడం నేర్చుకుంటాము.

### GitHub వ్యక్తిగత యాక్సెస్ టోకెన్ ద్వారా ధృవీకరణ

GitHub టోకెన్ సృష్టించడం ఒక సులభమైన ప్రక్రియ. ఇలా చేయొచ్చు:

- GitHub సెట్టింగులకు వెళ్ళండి – ఎడమ పై మూలలోని మీ ప్రొఫైల్ చిత్రంపై క్లిక్ చేసి సెట్టింగులను ఎంచుకోండి.
- డెవలపర్ సెట్టింగులకు వెళ్లండి – క్రిందికి స్క్రోల్ చేసి డెవలపర్ సెట్టింగులను క్లిక్ చేయండి.
- వ్యక్తిగత యాక్సెస్ టోకెన్లను ఎంచుకోండి – ఫైన్-గ్రెయిన్ టోకెన్లను క్లిక్ చేసి, తరువాత కొత్త టోకెన్ సృష్టించండి.
- మీ టోకెన్ కాన్ఫిగర్ చేయండి – రిఫరెన్స్ కోసం ఒక టిప్పణీ చేర్చండి, గడువు తేదీ సెట్ చేయండి, మరియు అవసరమైన స్కోపులను ఎంచుకోండి. ఈ సందర్భంలో ప్రత్యేకంగా మోడల్స్ అనుమతిని జోడించాలి.
- టోకెన్ సృష్టించి కాపీ చేయండి – జనరేట్ టోకెన్ పై క్లిక్ చేసి, వెంటనే దాన్ని కాపీ చేసుకోండి, చెహ వేళ అది మళ్లీ చూడలేరు.

### -1- సర్వర్‌కు కనెక్ట్ అవ్వండి

ముందుగా మనం మన క్లయింట్ సృష్టిద్దాం:

#### టైప్‌స్క్రిప్ట్

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా ధృవీకరణ కోసం zod ని దిగుమతి చేసుకోండి

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

కొద్ది ముందు కోడ్‌లో మనం:

- కావలసిన లైబ్రరీలను దిగుమతి చేసుకున్నాము
- ఒక క్లాస్ సృష్టించాం, ఇందులో రెండు సభ్యులు, `client` మరియు `openai` ఉన్నాయి, ఇది మనకు క్లయింట్ నిర్వహణ మరియు LLM తో పరస్పర చర్యలో సహాయం చేస్తాయి.
- గిట్హబ్ మోడల్స్ ఉపయోగించడానికి మన LLM ఉదాహరణను `baseUrl` ను ఇన్ఫరెన్స్ API దిశగా సెట్ చేసి కాన్ఫిగర్ చేసాం.

#### పైథాన్

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio కనెక్షన్ కోసం సర్వర్ పారామితులు సృష్టించండి
server_params = StdioServerParameters(
    command="mcp",  # పనితీరు
    args=["run", "server.py"],  # ఐచ్చిక కమాండ్ లైన్ ఆర్గుమెంట్లు
    env=None,  # ఐచ్చిక వాతావరణ చరాలు
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

కొద్ది ముందు కోడ్‌లో మనం:

- MCP కోసం కావలసిన లైబ్రరీలను దిగుమతి చేసుకున్నాము
- ఒక క్లయింట్ సృష్టించాము

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

మొదట, మీరు LangChain4j డిపెండెన్సీలను మీ `pom.xml` ఫైల్లో జోడించాలి. MCP ఇంటిగ్రేషన్ మరియు OpenAI అనుకూలమైన MiniMax API ను సక్రియం చేసేందుకు ఈ డిపెండెన్సీలను జత చేయండి:

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

మీ MiniMax API కీ, ఐచ్ఛికంగా ఎండ్‌పాయింట్ మరియు మోడల్‌ను సెట్ చేయండి.
`MINIMAX_MODEL_ID` `MiniMax-M3` మరియు `MiniMax-M2.7` ను మద్దతు ఇస్తుంది. 
`OPENAI_BASE_URL` సెట్ చేయకపోతే, `MINIMAX_REGION` `global_en` మరియు `cn_zh` మద్దతు ఇస్తుంది.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

ప్రాంతం ప్రకారం ఎండ్‌పాయింట్ ఎంచుకోవడానికి, `OPENAI_BASE_URL` ని తప్పింప జేయండి:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

తరువాత మీ జావా క్లయింట్ క్లాస్‌ను సృష్టించండి:

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

        // సర్వర్‌కు కనెక్ట్ కావడానికి MCP ట్రాన్స్‌పోర్ట్‌ను సృష్టించండి
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

కొద్ది ముందు కోడ్‌లో మనం:

- **LangChain4j డిపెండెన్సీలు జోడించాను**: MCP ఇంటిగ్రేషన్ మరియు OpenAI అనుకూల MiniMax API కోసం అవసరం
- **LangChain4j లైబ్రరీలను దిగుమతి చేసుకున్నాము**: MCP ఇంటిగ్రేషన్ మరియు OpenAI చాట్ మోడల్ ఫంక్షనాలిటీ కోసం
- **`ChatLanguageModel` సృష్టించాము**: MiniMax తో మీ MiniMax API కీ, ఎండ్‌పాయింట్, మరియు మద్దతిస్తున్న మోడల్ ID ఉపయోగించి కాన్ఫిగర్ చేయబడింది
- **HTTP రవాణాను సెటప్ చేసాం**: సర్వర్-సెంటు ఈవెంట్స్ (SSE) ఉపయోగించి MCP సర్వర్‌కు కనెక్ట్ అవుతున్నారు
- **MCP క్లయింట్ సృష్టించాం**: ఇది సర్వర్‌తో కమ్యూనికేషన్ నిర్వహిస్తుంది
- **LangChain4j యొక్క బిల్ట్-ఇన్ MCP సపోర్ట్ ఉపయోగించాము**: ఇది LLMs మరియు MCP సర్వర్‌ల మధ్య ఇంటిగ్రేషన్ సులభతరం చేస్తుంది

#### రస్ట్

ఈ ఉదాహరణ మీకు రస్ట్-ఆధారిత MCP సర్వర్ నడుస్తోంది అనుకుంటుంది. మీరు ఒకటి లేకపోతే, సర్వర్ సృష్టించడానికి [01-first-server](../01-first-server/README.md) పాఠాన్ని అనుసరించండి.

ఒకసారి మీకు రస్ట్ MCP సర్వర్ చెలామణీలో ఉంది, ఓ టెర్మినల్ ఓపెన్ చేసి సర్వర్ ఉన్న అదే డైరెక్టరీకి వెళ్లండి. తరువాత క్రింది ఆజ్ఞను నడపండి కొత్త LLM క్లయింట్ ప్రాజెక్టును సృష్టించేందుకు:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

మీ `Cargo.toml` ఫైల్‌కు కింది డిపెండెన్సీలను జోడించండి:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI కోసం అధికారిక రస్ట్ లైబ్రరీ లేదు, కానీ `async-openai` క్రేట్ ఒక [కమ్యూనిటీ నిర్వహించే లైబ్రరీ](https://platform.openai.com/docs/libraries/rust#rust) గా సాధారణంగా ఉపయోగిస్తారు.

`src/main.rs` ఫైల్‌ను తెరిచి దాని కంటెంట్‌ను క్రింది కోడ్‌తో మార్చండి:

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

    // OpenAI క్లయింట్ సెటప్ చేయండి
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP క్లయింట్ సెటప్ చేయండి
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

    // TODO: MCP టూల్ లిస్టింగ్ పొందండి

    // TODO: టూల్ కాల్స్‌తో LLM సంభాషణ

    Ok(())
}
```

ఈ కోడ్ ఒక ప్రాథమిక రస్ట్ అప్లికేషన్‌ను సృష్టిస్తుంది, ఇది MCP సర్వర్ మరియు GitHub మోడల్స్‌కి LLM పరస్పర చర్యలకు కనెక్ట్ అవుతుంది.

> [!IMPORTANT]
> అప్లికేషన్ నడపక ముందు `OPENAI_API_KEY` పర్యావరణ చరమైన విలువతో మీ GitHub టోకెన్ సెటు చేస్తారో లేదో ఖచ్చితంగా చూసుకోండి.

బాగుంది, తదుపరి దశకు మనము సర్వర్ నుంచి సామర్ధ్యాలను జాబితా చేద్దాం.

### -2- సర్వర్ సామర్ధ్యాలను జాబితా చేయండి

ఇప్పుడు మనం సర్వర్‌కు కనెక్ట్ అయ్యి దాని సామర్ధ్యాలను అడుగుతాము:

#### టైప్స్క్రిప్ట్

అదే క్లాస్‌లో క్రింది మెథడ్లను జోడించండి:

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

కొద్ది ముందు కోడ్‌లో మనం:

- సర్వర్‌కి కనెక్ట్ అయ్యే కోడ్ జోడించాం, `connectToServer`.
- మన అప్లికేషన్ ప్రవాహాన్ని నిర్వహించడానికి `run` మెథడ్ సృష్టించాం. ప్రస్తుతం ఇది కేవలం టూల్స్ జాబితాను మాత్రమే చూపిస్తుంది కానీ త్వరలో మరిన్ని జోడిస్తాము.

#### పైథాన్

```python
# అందుబాటులో ఉన్న వనరులను జాబితా చేయండి
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# అందుబాటులో ఉన్న సాధనాలను జాబితా చేయండి
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

మనం జోడించినవి:

- వనరులు మరియు టూల్స్ జాబితా చేయడం మరియు వాటిని ప్రింట్ చేయడం. టూల్స్ కోసం `inputSchema` ను కూడా జాబితా చేస్తాం, ఇది తర్వాత ఉపయోగిస్తాం.

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


ముందు కోడ్‌లో మేము:

- MCP సర్వర్ మీద అందుబాటులో ఉన్న టూల్స్‌లను జాబితా చేశాము
- ప్రతి టూల్ కోసం, పేరు, వివరణ మరియు దాని స్కీమాను జాబితా చేసాము. తర్వాతి భాగంలో, టూల్స్‌ను కాల్ చేయడానికి ఈ స్కీమాను ఉపయోగిస్తాము.

#### జావా

```java
// MCP సౌకర్యాలను స్వయంచాలకంగా కనుగొనే టూల్ ప్రొవైడర్ సృష్టించండి
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP టూల్ ప్రొవైడర్ స్వయంచాలకంగా నిర్వహిస్తుంది:
// - MCP సర్వర్ నుండి అందుబాటులో ఉన్న టూల్స్ యొక్క జాబితా తయారు చేయడం
// - MCP టూల్ స్కీమాలను LangChain4j ఫార్మాట్‌కు మార్పిడి చేయడం
// - టూల్ నడిపింపు మరియు ప్రతిస్పందనలను నిర్వహించడం
```

ముందు కోడ్‌లో మేము:

- MCP సర్వర్ నుండి అన్ని టూల్స్‌ను ఆటోమేటిక్‌గా కనుగొని నమోదు చేసే `McpToolProvider` ను సృష్టించాము
- టూల్ ప్రొవైడర్ MCP టూల్స్ స్కీమా మరియు LangChain4j టూల్ ఫార్మాట్ మధ్య కాన్వర్షన్‌ను అంతర్గతంగా నిర్వహిస్తుంది
- ఈ విధానం మాన్యువల్ టూల్ జాబితా మరియు కాన్వర్షన్ ప్రక్రియను దాచిపెడుతుంది

#### రస్ట్

MCP సర్వర్ నుండి టూల్స్‌ని పొందడాన్ని `list_tools` మెథడ్ ఉపయోగించి చేస్తారు. మీ `main` ఫంక్షన్‌లో MCP క్లయింట్ సెటప్ చేసిన తర్వాత, క్రింది కోడ్‌ను జోడించండి:

```rust
// MCP టూల్ జాబితాను పొందండి
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- సర్వర్ సామర్థ్యాలను LLM టూల్స్‌గా మార్చడం

సర్వర్ సామర్థ్యాలను జాబితా చేసిన తర్వాతి దశ అవి LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చడం. ఒకసారి మేము అలా చేస్తాము, ఈ సామర్థ్యాలను మా LLMకి టూల్స్‌గా అందించవచ్చు.

#### టైప్స్క్రిప్ట్

1. MCP సర్వర్ నుండి రిస్పాన్స్‌ను LLM ఉపయోగించగల టూల్ ఫార్మాట్లోకి మార్చడానికి క్రింది కోడ్‌ను జోడించండి:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ఇన్‌పుట్ స్కీమాపై ఆధారపడి ఒక జాడ్ స్కీమాను సృష్టించండి
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // టైపు‌ను "function"గా స్పష్టంగా సెట్ చేయండి
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

    పై కోడ్ MCP సర్వర్ నుండి వచ్చిన రిస్పాన్స్‌ను LLM అర్థం చేసుకునే టూల్ నిర్వచన ఫార్మాట్‌గా మార్చుతుంది.

2. తర్వాత, సర్వర్ సామర్థ్యాలను జాబితా చేయడానికి `run` మెథడ్‌ను నవీకరしましょう:

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

    ముందు కోడ్‌లో, మేము `run` మెథడ్‌ను ఫలితాన్ని మ్యాప్ చేయడానికి నవీకరించి, ప్రతి ఎంట్రీకి `openAiToolAdapter` ను పిలిచాము.

#### పైథాన్

1. ముందుగా, క్రింది కన్వర్టర్ ఫంక్షన్‌ను సృష్టిద్దాం

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

    పై ఫంక్షన్ `convert_to_llm_tools` లో మేము MCP టూల్ రిస్పాన్స్ తీసుకొని LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చాము.

2. తర్వాత, ఈ ఫంక్షన్ ఉపయోగించడానికి మా క్లయింట్ కోడ్‌ను ఇలా నవీకరిద్దాం:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ఇక్కడ, మేము `convert_to_llm_tool` ను పిలిచి MCP టూల్ రిస్పాన్స్‌ను తర్వాత LLMకి అందించగల ఫార్మాట్‌కు మార్చుతుండాము.

#### .NET

1. MCP టూల్ రిస్పాన్స్‌ను LLM అర్థం చేసుకునేలా మార్చడానికి కోడ్ జోడిద్దాం

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

ముందరి కోడ్‌లో మేము:

- పేరు, వివరణ మరియు ఇన్పుట్ స్కీమాను తీసుకునే `ConvertFrom` అనే ఫంక్షన్ సృష్టించాము.
- ఇది ఒక FunctionDefinition సృష్టించే విధానాన్ని నిర్వచించుతుంది, ఇది ChatCompletionsDefinition కి పాస్ అవుతుంది. తరువాతి భాగం LLM అర్థం చేసుకునేది.

2. ఇప్పుడు పై ఫంక్షన్‌ని ఉపయోగించడానికి ఉన్న కోడ్‌ను ఎలా నవీకరించాలో చూద్దాం:

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
// సహజ భాషా సంభాషణకు బోట్ ఇంటర్‌ఫేస్ సృష్టించండి
public interface Bot {
    String chat(String prompt);
}

// LLM మరియు MCP టూల్స్‌తో AI సేవను కాన్ఫిగర్ చేయండి
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ముందు కోడ్‌లో మేము:

- సహజ భాషా సంభాషణ కోసం సులభమైన `Bot` ఇంటర్‌ఫేస్‌ను నిర్వచించాము
- LangChain4j యొక్క `AiServices` ఉపయోగించి LLMని MCP టూల్ ప్రొవైడర్‌తో ఆటోమేటిక్‌గా బైండ్ చేశాము
- ఫ్రేమ్‌వర్క్ బ్యాక్‌గ్రౌండ్‌లో టూల్ స్కీమా కాన్వర్షన్ మరియు ఫంక్షన్ కాలింగ్‌ను ఆటోమేటిక్‌గా నిర్వహిస్తుంది
- ఈ విధానం మాన్యువల్ టూల్ కాన్వర్షన్ అవసరాన్ని తొలగిస్తుంది - LangChain4j MCP టూల్స్‌ను LLM అనుకూల ఫార్మాట్‌గా మార్చడంలో అన్ని సంక్లిష్టతలను నిర్వహిస్తుంది

#### రస్ట్

MCP టూల్ రిస్పాన్స్‌ని LLM అర్థం చేసుకునే ఫార్మాట్‌కు మార్చటానికి, టూల్స్ జాబితాను ఫార్మాట్ చేసే సహాయక ఫంక్షన్‌ను చేర్చుతాము. దీన్ని మీ `main.rs` ఫైల్‌లో `main` ఫంక్షన్ క్రింద క్రిందైనా జోడించండి. ఇది LLM కి అభ్యర్థనలు చేసే సమయంలో పిలవబడుతుంది:

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


అద్భుతం, మేము ఏ ఒక్క వినియోగదారు అభ్యర్థనలను కూడా నిర్వహించడానికి సెట్ చేయబడలేదు, కాబట్టి దీన్ని తర్వాత పరిష్కరించుకుందాం.

### -4- వినియోగదారు ప్రాంప్ట్ అభ్యర్థనను నిర్వహించండి

కోడ్ యొక్క ఈ భాగంలో, మేము వినియోగదారు అభ్యర్థనలను నిర్వహించనున్నాము.

#### టైప్‌స్క్రిప్ట్

1. మా LLMను పిలవడానికి ఉపయోగించే ఒక విధానాన్ని జోడించండి:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. సర్వర్ టూల్‌ను పిలవండి
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ఫలితంతో ఏదో చేయండి
        // చేయవలసింది

        }
    }
    ```

    ముందు ఉన్న కోడ్లో మేము:

    - ఒక `callTools` అనే విధానాన్ని జోడించారా.
    - ఆ విధానం LLM స్పందనను తీసుకొని, ఏ సాధనాలు పిలవబడ్డాయో చూడటానికి చెక్ చేస్తుంది, ఉంటే:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // టూల్‌ను పిలవండి
        }
        ```

    - LLM పిలవాల్సిందని సూచిస్తే ఒక సాధనాన్ని పిలుస్తుంది:

        ```typescript
        // 2. సర్వర్ టూల్‌ను పిలవండి
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ఫలితంతో ఏదైనా చేయండి
        // చేయాల్సింది
        ```

2. `run` విధానాన్ని LLM కాల్స్ మరియు `callTools` పిలవడాన్ని చేర్చడానికి అప్‌డేట్ చేయండి:

    ```typescript

    // 1. LLMకి ఇన్‌పుట్ గా ఉండే సందేశాలను సృష్టించండి
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLMను కాల్ చేయడం
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ప్రతిస్పందనలో ప్రతి ఎంపికను చూడండి, దాని టూల్ కాల్స్ ఉన్నాయా కాదా అని తనిఖీ చేయండి
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

అద్భుతం, పూర్తి కోడ్‌ను జాబితా చేద్దాం:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా ధ్రువీకరణ కోసం zodని దిగుమతి చేసుకోండి

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // భవిష్యత్తులో ఈ URLకి మార్చాలి కావచ్చు: https://models.github.ai/inference
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
          // ఇన్‌పుట్_స్కీమా ఆధారంగా ఒక zod స్కీమాను సృష్టించండి
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // "function" గా టైప్ను స్పష్టంగా సెట్ చేయండి
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
    
    
          // 2. సర్వర్ టూల్‌ను కాల్ చేయండి
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ఫలితంతో ఏదైనా చేయండి
          // చేయాల్సింది
    
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
    
        // 3. LLM ప్రత్యుత్తరం ద్వారా వెళ్లండి, ప్రతి ఎంపికకు టూల్ కాల్స్ ఉన్నాయా అని తనిఖీ చేయండి
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

1. LLMను పిలవడానికి అవసరమైన కొన్ని ఇంపోర్ట్స్‌ను జోడిద్దాం

    ```python
    # ఎల్‌ఎల్‌ఎం
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. తర్వాత, LLMను పిలవడానికి ఒక ఫంక్షన్‌ను జోడిద్దాం:

    ```python
    # ఎల్ఎల్ఎమ్

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

    ముందు ఉన్న కోਡ్లో మేము:

    - MCP సర్వర్‌లో కనుగొన్న మరియు మార్చిన మా ఫంక్షన్లను LLMకు పంపించారు.
    - ఆ ఫంక్షన్లతో LLMను పిలిచాము.
    - తరువాత, ఫలితాన్ని పరిశీలించి ఏ ఫంక్షన్లు పిలవాలో చూస్తున్నాము, ఉంటే.
    - చివరగా, పిలవాల్సిన ఫంక్షన్ల అర్రేను పంపుతున్నాము.

3. చివరి దశ, మా ప్రధాన కోడ్‌ను అప్‌డేట్ చేద్దాం:

    ```python
    prompt = "Add 2 to 20"

    # LLM కు ఏమైనా ఉంటే అన్ని టూల్స్ ఏమిటి అని అడగండి
    functions_to_call = call_llm(prompt, functions)

    # సూచించిన ఫంక్షన్లను పిలవండి
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    అదే, పైన ఉన్న కోడ్లో చివరి దశగా మేము:

    - LLM మన ప్రాంప్ట్ ఆధారంగా పిలవాల్సిందని భావించిన ఫంక్షన్‌ను ఉపయోగించి `call_tool` ద్వారా MCP సాధనాన్ని పిలుస్తున్నాము.
    - MCP సర్వర్‌కు సాధన పిలుపు ఫలితాన్ని ప్రింట్ చేస్తున్నాము.

#### .NET

1. LLM ప్రాంప్ట్ అభ్యర్థన కోసం కొంత కోడ్ చూపిద్దాం:

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

    ముందు ఉన్న కోడ్లో మేము:

    - MCP సర్వర్ నుండి సాధనాలు తీసుకున్నాము, `var tools = await GetMcpTools()`.
    - ఒక యూజర్ ప్రాంప్ట్ `userMessage` ను నిర్వచించాము.
    - మోడల్ మరియు సాధనాలను పేర్కొనే ఒక ఆప్షన్స్ ఆబ్జెక్ట్ తయారుచేశాము.
    - LLM వైపు అభ్యర్థన పంపాము.

2. చివరి దశ, LLM మాకు కాల్ చేయాలని సూచిస్తుందా అనేదాన్ని చూద్దాం:

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

    ముందస్తు కోడ్లో మేము:

    - ఫంక్షన్ కాల్స్ జాబితా గుండా తిరిగాము.
    - ప్రతి సాధన పిలుపు కోసం, పేరు మరియు ఆర్గ్యుమెంట్లను పార్స్ చేసి MCP క్లయింట్ ఉపయోగించి MCP సర్వర్‌పై సాధనాన్ని పిలిచాము. చివరగా ఫలితాలు ప్రింట్ చేయబడుతున్నాయి.

పూర్తి కోడ్ ఇలా ఉంది:

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
    // MCP టూల్స్‌ను స్వయంచాలకంగా ఉపయోగించే సహజ భాషా అభ్యర్థనలను నిర్వహించండి
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

ముందస్తు కోడ్లో మేము:

- సులభ సహజ భాష ప్రాంప్ట్‌లను ఉపయోగించి MCP సర్వర్ సాధనాలతో ఇంటరాక్ట్ అయ్యాము
- LangChain4j ఫ్రేమ్‌వర్క్ ఆటోమేటిక్ గా నిర్వహిస్తోంది:
  - అవసరమైతే వినియోగదారు ప్రాంప్ట్‌లను సాధన పిలుపులకు మార్చడం
  - LLM నిర్ణయం ఆధారంగా సరైన MCP సాధనాలను పిలవడం
  - LLM మరియు MCP సర్వర్ మధ్య సంభాషణ ప్రవాహం నిర్వహించడం
- `bot.chat()` విధానం సహజ భాషలో స్పందనలను ఇస్తుంది, అవి MCP సాధన అమలు ఫలితాలు కలిగి ఉండవచ్చు
- ఈ ఉపాయంతో వినియోగదారులు MCP అమలు వివరాలు తెలియవలసిన అవసరం లేకుండా సులభ అనుభవం పొందుతారు

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


ఇక్కడే ఎక్కువ పని జరగుతుంది. మేము ప్రారంభ యూజర్ ప్రాంప్ట్‌తో LLM ని పిలుస్తాము, ఆపై ప్రతిస్పందనను ప్రాసెస్ చేసి ఏదైనా టూల్స్ పిలవాల్సిన అవసరం ఉందో లేదో చూస్తాము. అవసరమైతే, ఆ టూల్స్ పిలిచి LLM తో సంభాషణను కొనసాగిస్తాము, మరిన్ని టూల్ పిలుపులు అవసరం లేకపోవు వరకు చివరి ప్రతిస్పందన వచ్చేవరకు.

మేము LLM కు పలు పిలుపులు చేయబోతున్నాము, కాబట్టి LLM పిలుపును నిర్వరణ చేసే ఫంక్షన్‌ను నిర్వచిద్దాం. మీ `main.rs` ఫైల్‌కు క్రింది ఫంక్షన్‌ను జోడించండి:

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

ఈ ఫంక్షన్ LLM కస్టమర్, సందేశాల జాబితా (యూజర్ ప్రాంప్ట్ సహా), MCP సర్వర్ నుండి టూల్స్‌ను తీసుకుని LLM కు درخواستనిచ్చి, ప్రతిస్పందనను తిరిగి ఇవ్వును.

LLM నుండి వచ్చిన ప్రతిస్పందన `choices` అనే అర్రే ఉంటాయి. మేము ఫలితాన్ని ప్రాసెస్ చేసి `tool_calls` ఉండగా ఉన్నాయో పరిశీలించాలి. ఇది LLM నిర్దిష్ట టూల్‌ను పిలవాలని అభ్యర్థిస్తున్నట్లు మాకు తెలుపుతుంది. LLM ప్రతిస్పందనను హ్యాండిల్ చేయడానికి క్రింద ఇచ్చిన కోడ్‌ను మీ `main.rs` ఫైల్ చివరలో జోడించండి:

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

    // అందుబాటులో ఉంటే కంటెంట్ ప్రింట్ చేయండి
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // టూల్ కాల్స్ ని నిర్వహించండి
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // సాయం సందేశం జోడించండి

        // ప్రతి టూల్ కాల్‌ను అమలు చేయండి
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

        // టూల్ ఫలితాలతో సంభాషణ కొనసాగించండి
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

`tool_calls` ఉంటే, అది టూల్ సమాచారాన్ని తీసుకొని MCP సర్వర్‌కి టూల్ అభ్యర్థన పిలుస్తుంది, ఫలితాలను సంభాషణ సందేశాలకు జోడిస్తుంది. ఆపై LLMతో సంభాషణ కొనసాగించి, సందేశాలు అసిస్టెంట్ యొక్క ప్రతిస్పందన మరియు టూల్ పిలుపుల ఫలితాలతో నవీకరించబడతాయి.

LLM MCP పిలుపులకు తిరిగి ఇచ్చే టూల్ పిలుపు సమాచారాన్ని ఎక్స్‌ట్రాక్ట్ చేయడానికి, మేము ఒక సహాయక ఫంక్షన్‌ను జోడిస్తాము. మీ `main.rs` ఫైల్ చివరలో క్రింద ఇచ్చిన కోడ్‌ను చేర్చండి:

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

అన్ని భాగాలు సిద్ధంగా ఉన్నందున, మేము ప్రాథమిక యూజర్ ప్రాంప్ట్ ను హ్యాండిల్ చేసి LLM ను పిలవవచ్చు. మీ `main` ఫంక్షన్‌ను క్రింద చూపిన కోడ్‌తో నవీకరించండి:

```rust
// టూల్ కాల్స్‌తో LLM సంభాషణ
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

ఇది ప్రారంభ యూజర్ ప్రాంప్ట్‌తో LLM ను అడిగి రెండు సంఖ్యల గణన యొక్క సమాన్ని కోరుతుంది, మరియు టూల్ పిలుపులను డైనమిక్‌గా నిర్వహిస్తుంది.

అద్భుతం, మీరు సాధించారు!

## అసైన్‌మెంట్

అనుభవం నుంచి కోడ్ తీసుకుని ఇంకా కొన్ని టూల్స్ తో సర్వర్ ను పెంచండి. ఆ తరువాత LLM కలిగిన క్లయింట్ తయారు చేసి పలు ప్రాంప్టులతో పరీక్షించండి, తద్వారా మీ సర్వర్ టూల్స్ అన్ని డైనమిక్‌గా పిలవబడుతున్నాయని నిర్ధారించండి. ఇలాంటి క్లయింట్ నిర్మాణం వలన చివరి యూజ‌ర్‌కు ఒక మంచి అనుభవం కలుగుతుంది, వారు ఖచ్చిత క్లయింట్ ఆదేశాలు కాకుండా ప్రాంప్ట్స్ ఉపయోగించి ఏ MCP సర్వర్ పిలవబడుతున్నదో అనుసరించకుండా ఉపయోగించగలుగుతారు.

## పరిష్కారం

[పరిష్కారం](./solution/README.md)

## ముఖ్యమైన విషయాలు

- క్లయింట్‌కు LLM జోడించడం MCP సర్వర్స్‌తో యూజర్లకు మెరుగైన ఇంటరాక్షన్‌ను అందిస్తుంది.
- MCP సర్వర్ ప్రతిస్పందనను LLM అర్థం చేసుకునే విధంగా మార్చాలి.

## నమూనాలు

- [జావా క్యాలక్యులేటర్](../samples/java/calculator/README.md)
- [.నెట్ క్యాలక్యులేటర్](../../../../03-GettingStarted/samples/csharp)
- [జావాస్క్రిప్ట్ క్యాలక్యులేటర్](../samples/javascript/README.md)
- [టైప్‌స్క్రిప్ట్ క్యాలక్యులేటర్](../samples/typescript/README.md)
- [పైథాన్ క్యాలక్యులేటర్](../../../../03-GettingStarted/samples/python)
- [రస్ట్ క్యాలక్యులేటర్](../../../../03-GettingStarted/samples/rust)

## అదనపు వనరులు

## తర్వాత ఏమి చేయాలి

- తదుపరి: [విజువల్ స్టూడియో కోడ్ ఉపయోగించి సర్వర్‌ను కన్సూమ్ చేయడం](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->