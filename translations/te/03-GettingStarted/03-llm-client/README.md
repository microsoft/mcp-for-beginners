<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d846ebb88fbb0f00549e2ff8cc3f746",
  "translation_date": "2025-12-11T11:44:24+00:00",
  "source_file": "03-GettingStarted/03-llm-client/README.md",
  "language_code": "te"
}
-->
# LLMతో క్లయింట్ సృష్టించడం

ఇప్పటి వరకు, మీరు సర్వర్ మరియు క్లయింట్‌ను ఎలా సృష్టించాలో చూశారు. క్లయింట్ స్పష్టంగా సర్వర్‌ను పిలిచి దాని టూల్స్, వనరులు మరియు ప్రాంప్ట్‌లను జాబితా చేయగలిగింది. అయితే, ఇది చాలా ప్రాక్టికల్ విధానం కాదు. మీ యూజర్ ఏజెంటిక్ యుగంలో జీవిస్తున్నారు మరియు ప్రాంప్ట్‌లను ఉపయోగించి LLMతో కమ్యూనికేట్ చేయాలని ఆశిస్తున్నారు. మీ యూజర్‌కు మీరు MCP ఉపయోగిస్తున్నారా లేదా అనేది ముఖ్యం కాదు, కానీ వారు సహజ భాషను ఉపయోగించి ఇంటరాక్ట్ చేయాలని ఆశిస్తున్నారు. కాబట్టి దీన్ని ఎలా పరిష్కరిస్తాం? పరిష్కారం క్లయింట్‌కు LLMను జోడించడం గురించి.

## అవలోకనం

ఈ పాఠంలో మేము క్లయింట్‌కు LLMను జోడించడం మరియు ఇది మీ యూజర్‌కు ఎలా మెరుగైన అనుభవాన్ని అందిస్తుందో చూపించడంపై దృష్టి సారిస్తాము.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- LLMతో క్లయింట్ సృష్టించండి.
- LLM ఉపయోగించి MCP సర్వర్‌తో సజావుగా ఇంటరాక్ట్ చేయండి.
- క్లయింట్ వైపు మెరుగైన ఎండ్ యూజర్ అనుభవాన్ని అందించండి.

## విధానం

మనం తీసుకోవలసిన విధానాన్ని అర్థం చేసుకుందాం. LLMను జోడించడం సులభంగా అనిపించవచ్చు, కానీ నిజంగా మేము దీన్ని ఎలా చేస్తాము?

క్లయింట్ సర్వర్‌తో ఎలా ఇంటరాక్ట్ చేస్తుందో ఇక్కడ ఉంది:

1. సర్వర్‌తో కనెక్షన్ స్థాపించండి.

1. సామర్థ్యాలు, ప్రాంప్ట్‌లు, వనరులు మరియు టూల్స్ జాబితా చేయండి, మరియు వాటి స్కీమాను సేవ్ చేయండి.

1. LLMను జోడించి సేవ్ చేసిన సామర్థ్యాలు మరియు వాటి స్కీమాను LLM అర్థం చేసుకునే ఫార్మాట్‌లో పంపండి.

1. యూజర్ ప్రాంప్ట్‌ను LLMకు పంపించి, క్లయింట్ జాబితా చేసిన టూల్స్‌తో కలిసి హ్యాండిల్ చేయండి.

అద్భుతం, ఇప్పుడు మేము ఈ విధానాన్ని ఉన్నత స్థాయిలో అర్థం చేసుకున్నాము, కింద ఇచ్చిన వ్యాయామంలో దీన్ని ప్రయత్నిద్దాం.

## వ్యాయామం: LLMతో క్లయింట్ సృష్టించడం

ఈ వ్యాయామంలో, మేము మా క్లయింట్‌కు LLMను జోడించడం నేర్చుకుంటాము.

### GitHub వ్యక్తిగత యాక్సెస్ టోకెన్ ఉపయోగించి ధృవీకరణ

GitHub టోకెన్ సృష్టించడం సులభమైన ప్రక్రియ. ఇది ఎలా చేయాలో ఇక్కడ ఉంది:

- GitHub సెట్టింగ్స్‌కు వెళ్లండి – పై కుడి మూలలో మీ ప్రొఫైల్ చిత్రాన్ని క్లిక్ చేసి సెట్టింగ్స్ ఎంచుకోండి.
- డెవలపర్ సెట్టింగ్స్‌కు నావిగేట్ చేయండి – క్రిందికి స్క్రోల్ చేసి డెవలపర్ సెట్టింగ్స్ క్లిక్ చేయండి.
- వ్యక్తిగత యాక్సెస్ టోకెన్లను ఎంచుకోండి – ఫైన్-గ్రెయిన్ టోకెన్లను క్లిక్ చేసి కొత్త టోకెన్ సృష్టించండి.
- మీ టోకెన్‌ను కాన్ఫిగర్ చేయండి – సూచన కోసం ఒక నోట్ జోడించండి, గడువు తేదీ సెట్ చేయండి, మరియు అవసరమైన స్కోప్స్ (అనుమతులు) ఎంచుకోండి. ఈ సందర్భంలో Models అనుమతిని తప్పనిసరిగా జోడించండి.
- టోకెన్‌ను సృష్టించి కాపీ చేసుకోండి – Generate token క్లిక్ చేసి వెంటనే కాపీ చేసుకోండి, ఎందుకంటే మీరు మళ్లీ చూడలేరు.

### -1- సర్వర్‌కు కనెక్ట్ అవ్వండి

ముందుగా మన క్లయింట్‌ను సృష్టిద్దాం:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా ధృవీకరణ కోసం zod ను దిగుమతి చేసుకోండి

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

- అవసరమైన లైబ్రరీలను దిగుమతి చేసుకున్నాము
- `client` మరియు `openai` అనే రెండు సభ్యులతో ఒక క్లాస్ సృష్టించాము, ఇవి క్లయింట్‌ను నిర్వహించడంలో మరియు LLMతో ఇంటరాక్ట్ చేయడంలో సహాయపడతాయి.
- మా LLM ఇన్స్టాన్స్‌ను GitHub Models ఉపయోగించడానికి `baseUrl`ని inference APIకి పాయింట్ చేయడం ద్వారా కాన్ఫిగర్ చేసాము.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio కనెక్షన్ కోసం సర్వర్ పరామితులను సృష్టించండి
server_params = StdioServerParameters(
    command="mcp",  # అమలు చేయదగినది
    args=["run", "server.py"],  # ఐచ్ఛిక కమాండ్ లైన్ ఆర్గ్యుమెంట్లు
    env=None,  # ఐచ్ఛిక పర్యావరణ వేరియబుల్స్
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

- MCP కోసం అవసరమైన లైబ్రరీలను దిగుమతి చేసుకున్నాము
- ఒక క్లయింట్ సృష్టించాము

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

ముందుగా, మీరు మీ `pom.xml` ఫైల్‌లో LangChain4j డిపెండెన్సీలను జోడించాలి. MCP ఇంటిగ్రేషన్ మరియు GitHub Models మద్దతు కోసం ఈ డిపెండెన్సీలను జోడించండి:

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

తర్వాత మీ Java క్లయింట్ క్లాస్‌ను సృష్టించండి:

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
    
    public static void main(String[] args) throws Exception {        // LLM ను GitHub మోడల్స్ ఉపయోగించడానికి కాన్ఫిగర్ చేయండి
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // సర్వర్‌కు కనెక్ట్ కావడానికి MCP ట్రాన్స్‌పోర్ట్ సృష్టించండి
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP క్లయింట్ సృష్టించండి
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

పూర్వపు కోడ్‌లో మేము:

- **LangChain4j డిపెండెన్సీలను జోడించాము**: MCP ఇంటిగ్రేషన్, OpenAI అధికారిక క్లయింట్, మరియు GitHub Models మద్దతు కోసం
- **LangChain4j లైబ్రరీలను దిగుమతి చేసుకున్నాము**: MCP ఇంటిగ్రేషన్ మరియు OpenAI చాట్ మోడల్ ఫంక్షనాలిటీ కోసం
- **`ChatLanguageModel` సృష్టించాము**: GitHub Models ఉపయోగించడానికి మీ GitHub టోకెన్‌తో కాన్ఫిగర్ చేయబడింది
- **HTTP ట్రాన్స్‌పోర్ట్ సెటప్ చేసాము**: MCP సర్వర్‌కు కనెక్ట్ కావడానికి Server-Sent Events (SSE) ఉపయోగించి
- **MCP క్లయింట్ సృష్టించాము**: ఇది సర్వర్‌తో కమ్యూనికేషన్ నిర్వహిస్తుంది
- **LangChain4j యొక్క బిల్ట్-ఇన్ MCP మద్దతు ఉపయోగించాము**: ఇది LLMs మరియు MCP సర్వర్ల మధ్య ఇంటిగ్రేషన్‌ను సులభతరం చేస్తుంది

#### Rust

ఈ ఉదాహరణలో మీరు Rust ఆధారిత MCP సర్వర్ నడుపుతున్నారని అనుకుంటుంది. మీ వద్ద ఒకటి లేకపోతే, సర్వర్ సృష్టించడానికి [01-first-server](../01-first-server/README.md) పాఠానికి తిరిగి చూడండి.

మీ Rust MCP సర్వర్ ఉన్న తర్వాత, టెర్మినల్ ఓపెన్ చేసి సర్వర్ ఉన్న అదే డైరెక్టరీకి వెళ్లండి. తరువాత క్రింది కమాండ్‌ను నడపండి కొత్త LLM క్లయింట్ ప్రాజెక్ట్ సృష్టించడానికి:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

మీ `Cargo.toml` ఫైల్‌లో క్రింది డిపెండెన్సీలను జోడించండి:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI కోసం అధికారిక Rust లైబ్రరీ లేదు, అయితే `async-openai` క్రేట్ ఒక [కమ్యూనిటీ నిర్వహించే లైబ్రరీ](https://platform.openai.com/docs/libraries/rust#rust)గా సాధారణంగా ఉపయోగించబడుతుంది.

`src/main.rs` ఫైల్‌ను ఓపెన్ చేసి దాని కంటెంట్‌ను క్రింది కోడ్‌తో మార్చండి:

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

    // TODO: MCP టూల్ జాబితా పొందండి

    // TODO: టూల్ కాల్స్‌తో LLM సంభాషణ

    Ok(())
}
```

ఈ కోడ్ ఒక ప్రాథమిక Rust అప్లికేషన్‌ను సెట్ చేస్తుంది, ఇది MCP సర్వర్ మరియు GitHub Modelsతో LLM ఇంటరాక్షన్ కోసం కనెక్ట్ అవుతుంది.

> [!IMPORTANT]
> అప్లికేషన్ నడపడానికి ముందు మీ GitHub టోకెన్‌తో `OPENAI_API_KEY` ఎన్విరాన్‌మెంట్ వేరియబుల్ సెట్ చేయడం మర్చిపోకండి.

అద్భుతం, తదుపరి దశకు, సర్వర్‌పై సామర్థ్యాలను జాబితా చేద్దాం.

### -2- సర్వర్ సామర్థ్యాలను జాబితా చేయండి

ఇప్పుడు మేము సర్వర్‌కు కనెక్ట్ అవ్వబోతున్నాము మరియు దాని సామర్థ్యాలను అడుగుతాము:

#### Typescript

అదే క్లాస్‌లో క్రింది మెథడ్స్ జోడించండి:

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

- సర్వర్‌కు కనెక్ట్ కావడానికి `connectToServer` కోడ్ జోడించాము.
- మా యాప్ ఫ్లో నిర్వహించడానికి `run` మెథడ్ సృష్టించాము. ఇప్పటివరకు ఇది కేవలం టూల్స్‌ను జాబితా చేస్తుంది, కానీ త్వరలో మరిన్ని జోడిస్తాము.

#### Python

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

మేము జోడించినవి:

- వనరులు మరియు టూల్స్ జాబితా చేసి ప్రింట్ చేశాము. టూల్స్ కోసం `inputSchema` కూడా జాబితా చేశాము, దీన్ని తర్వాత ఉపయోగిస్తాము.

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

- MCP సర్వర్‌లో అందుబాటులో ఉన్న టూల్స్ జాబితా చేశాము
- ప్రతి టూల్ కోసం పేరు, వివరణ మరియు దాని స్కీమాను జాబితా చేశాము. ఇది త్వరలో టూల్స్ పిలవడానికి ఉపయోగిస్తాము.

#### Java

```java
// MCP టూల్స్‌ను ఆటోమేటిక్‌గా కనుగొనే టూల్ ప్రొవైడర్‌ను సృష్టించండి
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP టూల్ ప్రొవైడర్ ఆటోమేటిక్‌గా నిర్వహిస్తుంది:
// - MCP సర్వర్ నుండి అందుబాటులో ఉన్న టూల్స్ జాబితా చేయడం
// - MCP టూల్ స్కీమాలను LangChain4j ఫార్మాట్‌కు మార్చడం
// - టూల్ అమలు మరియు ప్రతిస్పందనలను నిర్వహించడం
```

పూర్వపు కోడ్‌లో మేము:

- MCP సర్వర్ నుండి అన్ని టూల్స్‌ను ఆటోమేటిక్‌గా కనుగొని రిజిస్టర్ చేసే `McpToolProvider` సృష్టించాము
- టూల్ ప్రొవైడర్ MCP టూల్ స్కీమాలు మరియు LangChain4j టూల్ ఫార్మాట్ మధ్య మార్పిడి నిర్వహిస్తుంది
- ఈ విధానం మాన్యువల్ టూల్ జాబితా మరియు మార్పిడి ప్రక్రియను దూరం చేస్తుంది

#### Rust

MCP సర్వర్ నుండి టూల్స్ పొందడం `list_tools` మెథడ్ ద్వారా జరుగుతుంది. మీ `main` ఫంక్షన్‌లో MCP క్లయింట్ సెటప్ చేసిన తర్వాత క్రింది కోడ్ జోడించండి:

```rust
// MCP టూల్ జాబితాను పొందండి
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- సర్వర్ సామర్థ్యాలను LLM టూల్స్‌గా మార్చండి

సర్వర్ సామర్థ్యాలను జాబితా చేసిన తర్వాత తదుపరి దశ వాటిని LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చడం. ఒకసారి మేము చేస్తే, ఈ సామర్థ్యాలను మా LLMకు టూల్స్‌గా అందించవచ్చు.

#### TypeScript

1. MCP సర్వర్ నుండి వచ్చిన ప్రతిస్పందనను LLM ఉపయోగించగల టూల్ ఫార్మాట్‌గా మార్చడానికి క్రింది కోడ్ జోడించండి:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ఇన్‌పుట్_స్కీమా ఆధారంగా జోడ్ స్కీమాను సృష్టించండి
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // టైప్‌ను స్పష్టంగా "ఫంక్షన్" గా సెట్ చేయండి
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

    పై కోడ్ MCP సర్వర్ నుండి వచ్చిన ప్రతిస్పందనను LLM అర్థం చేసుకునే టూల్ నిర్వచన ఫార్మాట్‌గా మార్చుతుంది.

1. తరువాత, సర్వర్ సామర్థ్యాలను జాబితా చేయడానికి `run` మెథడ్‌ను అప్‌డేట్ చేద్దాం:

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

    పూర్వపు కోడ్‌లో, మేము `run` మెథడ్‌ను అప్‌డేట్ చేసి ఫలితాన్ని మ్యాప్ చేసి ప్రతి ఎంట్రీకి `openAiToolAdapter` పిలిచాము.

#### Python

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

    పై ఫంక్షన్ `convert_to_llm_tools` లో మేము MCP టూల్ ప్రతిస్పందనను LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చుతాము.

1. తరువాత, ఈ ఫంక్షన్‌ను ఉపయోగించడానికి మా క్లయింట్ కోడ్‌ను అప్‌డేట్ చేద్దాం:

    ```python
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ఇక్కడ, మేము MCP టూల్ ప్రతిస్పందనను LLMకి ఫీడ్ చేయడానికి `convert_to_llm_tool` పిలుస్తున్నాము.

#### .NET

1. MCP టూల్ ప్రతిస్పందనను LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చడానికి కోడ్ జోడిద్దాం

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

- పేరు, వివరణ మరియు ఇన్‌పుట్ స్కీమాను తీసుకునే `ConvertFrom` ఫంక్షన్ సృష్టించాము.
- ఇది `FunctionDefinition` సృష్టిస్తుంది, ఇది `ChatCompletionsDefinition`కి పంపబడుతుంది. ఇది LLM అర్థం చేసుకునే ఫార్మాట్.

1. ఈ ఫంక్షన్ ఉపయోగించడానికి కొంత కోడ్ ఎలా అప్‌డేట్ చేయాలో చూద్దాం:

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
// సహజ భాషా పరస్పర చర్య కోసం బాట్ ఇంటర్‌ఫేస్ సృష్టించండి
public interface Bot {
    String chat(String prompt);
}

// LLM మరియు MCP టూల్స్‌తో AI సేవను కాన్ఫిగర్ చేయండి
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

పూర్వపు కోడ్‌లో మేము:

- సహజ భాష ఇంటరాక్షన్ కోసం సింపుల్ `Bot` ఇంటర్‌ఫేస్ నిర్వచించాము
- LangChain4j యొక్క `AiServices` ఉపయోగించి LLMను MCP టూల్ ప్రొవైడర్‌తో ఆటోమేటిక్‌గా బైండ్ చేసాము
- ఫ్రేమ్‌వర్క్ ఆటోమేటిక్‌గా టూల్ స్కీమా మార్పిడి మరియు ఫంక్షన్ కాలింగ్ నిర్వహిస్తుంది
- ఈ విధానం మాన్యువల్ టూల్ మార్పిడిని తొలగిస్తుంది - LangChain4j MCP టూల్స్‌ను LLM-అనుకూల ఫార్మాట్‌గా మార్చడంలో అన్ని క్లిష్టతలను నిర్వహిస్తుంది

#### Rust

MCP టూల్ ప్రతిస్పందనను LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చడానికి, మేము టూల్స్ జాబితాను ఫార్మాట్ చేసే సహాయక ఫంక్షన్ జోడిస్తాము. మీ `main.rs` ఫైల్‌లో `main` ఫంక్షన్ కింద క్రింది కోడ్ జోడించండి. ఇది LLMకు అభ్యర్థనలు పంపేటప్పుడు పిలవబడుతుంది:

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

అద్భుతం, ఇప్పుడు మేము యూజర్ అభ్యర్థనలను హ్యాండిల్ చేయడానికి సెట్ అయ్యాము, కాబట్టి తదుపరి దశకు వెళ్లుదాం.

### -4- యూజర్ ప్రాంప్ట్ అభ్యర్థనను హ్యాండిల్ చేయండి

ఈ భాగంలో, మేము యూజర్ అభ్యర్థనలను హ్యాండిల్ చేస్తాము.

#### TypeScript

1. మా LLMను పిలవడానికి ఉపయోగించే మెథడ్ జోడించండి:

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

        // 3. ఫలితంతో ఏదైనా చేయండి
        // చేయవలసినది

        }
    }
    ```

    పూర్వపు కోడ్‌లో మేము:

    - `callTools` అనే మెథడ్ జోడించాము.
    - ఈ మెథడ్ LLM ప్రతిస్పందన తీసుకుని ఏ టూల్స్ పిలవబడ్డాయో తనిఖీ చేస్తుంది:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // టూల్‌ను పిలవండి
        }
        ```

    - LLM సూచించినట్లయితే టూల్‌ను పిలుస్తుంది:

        ```typescript
        // 2. సర్వర్ టూల్‌ను పిలవండి
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ఫలితంతో ఏదైనా చేయండి
        // చేయవలసినది
        ```

1. `run` మెథడ్‌ను అప్‌డేట్ చేసి LLMకు కాల్స్ మరియు `callTools` పిలవడం చేర్చండి:

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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ప్రతిస్పందనను పరిశీలించండి, ప్రతి ఎంపిక కోసం, అది టూల్ కాల్స్ ఉన్నాయా అని తనిఖీ చేయండి
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

అద్భుతం, పూర్తి కోడ్ ఇక్కడ ఉంది:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా ధృవీకరణ కోసం జోడ్‌ను దిగుమతి చేసుకోండి

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // భవిష్యత్తులో ఈ URLకి మార్చాల్సి ఉండవచ్చు: https://models.github.ai/inference
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
          // ఇన్‌పుట్_స్కీమా ఆధారంగా జోడ్ స్కీమాను సృష్టించండి
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // టైప్‌ను స్పష్టంగా "function" గా సెట్ చేయండి
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
          // చేయవలసినది
    
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
    
        // 1. LLM ప్రతిస్పందనలో ప్రతి ఎంపికను పరిశీలించండి, దానిలో టూల్ కాల్స్ ఉన్నాయా అని తనిఖీ చేయండి
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

1. LLM పిలవడానికి అవసరమైన దిగుమతులు జోడిద్దాం

    ```python
    # ఎల్ఎల్ఎమ్
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. తరువాత, LLMను పిలవడానికి ఫంక్షన్ జోడిద్దాం:

    ```python
    # ఎల్ఎల్ఎం

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
            # ఐచ్ఛిక పరామితులు
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

    - MCP సర్వర్‌లో కనుగొన్న మరియు మార్చిన ఫంక్షన్లను LLMకి పంపాము.
    - ఆపై ఆ ఫంక్షన్లతో LLMను పిలిచాము.
    - ఫలితాన్ని పరిశీలించి ఏ ఫంక్షన్లు పిలవాలో చూసాము.
    - చివరగా పిలవాల్సిన ఫంక్షన్ల అర్రేను పంపాము.

1. చివరి దశ, మా ప్రధాన కోడ్‌ను అప్‌డేట్ చేద్దాం:

    ```python
    prompt = "Add 2 to 20"

    # LLM కి ఏ టూల్స్ అవసరమో అడగండి, ఉంటే
    functions_to_call = call_llm(prompt, functions)

    # సూచించిన ఫంక్షన్లను పిలవండి
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    పై కోడ్‌లో మేము:

    - LLM సూచించిన ఫంక్షన్ ఆధారంగా MCP టూల్‌ను `call_tool` ద్వారా పిలుస్తున్నాము.
    - టూల్ కాల్ ఫలితాన్ని MCP సర్వర్‌కు ప్రింట్ చేస్తున్నాము.

#### .NET

1. LLM ప్రాంప్ట్ అభ్యర్థన కోసం కొంత కోడ్ చూపుదాం:

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

    పూర్వపు కోడ్‌లో మేము:

    - MCP సర్వర్ నుండి టూల్స్ పొందాము, `var tools = await GetMcpTools()`.
    - యూజర్ ప్రాంప్ట్ `userMessage` నిర్వచించాము.
    - మోడల్ మరియు టూల్స్ స్పెసిఫై చేసే ఆప్షన్స్ ఆబ్జెక్ట్ సృష్టించాము.
    - LLMకు అభ్యర్థన పంపాము.

1. చివరి దశ, LLM ఫంక్షన్ కాల్ చేయాలనుకుంటే చూద్దాం:

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

    - ఫంక్షన్ కాల్స్ జాబితా ద్వారా లూప్ చేశాము.
    - ప్రతి టూల్ కాల్ కోసం పేరు మరియు ఆర్గ్యుమెంట్లను పార్స్ చేసి MCP క్లయింట్ ఉపయోగించి టూల్‌ను పిలిచాము. చివరగా ఫలితాలను ప్రింట్ చేశాము.

పూర్తి కోడ్ ఇక్కడ ఉంది:

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
    // MCP టూల్స్‌ను స్వయంచాలకంగా ఉపయోగించే సహజ భాషా అభ్యర్థనలను అమలు చేయండి
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

- MCP సర్వర్ టూల్స్‌తో సహజ భాష ప్రాంప్ట్‌లను ఉపయోగించి ఇంటరాక్ట్ చేశాము
- LangChain4j ఫ్రేమ్‌వర్క్ ఆటోమేటిక్‌గా నిర్వహిస్తుంది:
  - అవసరమైతే యూజర్ ప్రాంప్ట్‌లను టూల్ కాల్స్‌గా మార్చడం
  - LLM నిర్ణయం ఆధారంగా సరైన MCP టూల్స్ పిలవడం
  - LLM మరియు MCP సర్వర్ మధ్య సంభాషణ ప్రవాహం నిర్వహించడం
- `bot.chat()` మెథడ్ సహజ భాష ప్రతిస
LLM నుండి వచ్చిన ప్రతిస్పందనలో `choices` అనే అర్రే ఉంటుంది. ఏమైనా `tool_calls` ఉన్నాయా అని ఫలితాన్ని ప్రాసెస్ చేయాలి. ఇది LLM ఒక నిర్దిష్ట టూల్‌ను ఆర్గ్యుమెంట్లతో పిలవాలని కోరుకుంటున్నదని మనకు తెలియజేస్తుంది. LLM ప్రతిస్పందనను హ్యాండిల్ చేయడానికి క్రింది కోడ్‌ను మీ `main.rs` ఫైల్ చివర చేర్చండి:

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

    // అందుబాటులో ఉంటే కంటెంట్‌ను ముద్రించండి
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // టూల్ కాల్స్‌ను నిర్వహించండి
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // సహాయక సందేశాన్ని జోడించండి

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

            // టూల్ ఫలితాన్ని సందేశాలకు జోడించండి
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

`tool_calls` ఉన్నట్లయితే, అది టూల్ సమాచారాన్ని తీసుకుని, MCP సర్వర్‌ను టూల్ అభ్యర్థనతో పిలుస్తుంది, మరియు ఫలితాలను సంభాషణ సందేశాలకు జోడిస్తుంది. ఆపై LLM తో సంభాషణ కొనసాగుతుంది మరియు సందేశాలు అసిస్టెంట్ ప్రతిస్పందన మరియు టూల్ కాల్ ఫలితాలతో నవీకరించబడతాయి.

LLM MCP కాల్స్ కోసం తిరిగి ఇచ్చే టూల్ కాల్ సమాచారాన్ని తీసుకోవడానికి, మేము మరొక సహాయక ఫంక్షన్‌ను చేర్చబోతున్నాము. ఈ కాల్ చేయడానికి అవసరమైన అన్ని వివరాలను తీసుకోవడానికి క్రింది కోడ్‌ను మీ `main.rs` ఫైల్ చివర చేర్చండి:

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

అన్ని భాగాలు సిద్ధంగా ఉన్నందున, మేము ప్రారంభ యూజర్ ప్రాంప్ట్‌ను హ్యాండిల్ చేసి LLM ను పిలవగలము. క్రింది కోడ్‌తో మీ `main` ఫంక్షన్‌ను నవీకరించండి:

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

ఇది ప్రారంభ యూజర్ ప్రాంప్ట్‌తో LLM ను ప్రశ్నిస్తుంది, రెండు సంఖ్యల మొత్తం అడుగుతుంది, మరియు ప్రతిస్పందనను ప్రాసెస్ చేసి టూల్ కాల్స్‌ను డైనమిక్‌గా హ్యాండిల్ చేస్తుంది.

చాలా బాగుంది, మీరు చేసారు!

## అసైన్‌మెంట్

వ్యాయామం నుండి కోడ్ తీసుకుని మరిన్ని టూల్స్‌తో సర్వర్‌ను నిర్మించండి. ఆపై వ్యాయామంలో ఉన్నట్లుగా LLM కలిగిన క్లయింట్‌ను సృష్టించి, వివిధ ప్రాంప్ట్‌లతో పరీక్షించండి, మీ సర్వర్ టూల్స్ డైనమిక్‌గా పిలవబడుతున్నాయా అని నిర్ధారించుకోండి. ఈ విధంగా క్లయింట్ నిర్మించడం ద్వారా చివరి వినియోగదారుకు మంచి అనుభవం కలుగుతుంది, ఎందుకంటే వారు ఖచ్చితమైన క్లయింట్ కమాండ్ల బదులు ప్రాంప్ట్‌లను ఉపయోగించి MCP సర్వర్ పిలవబడుతున్నదని తెలియకుండానే ఉపయోగించగలుగుతారు.

## పరిష్కారం

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## ముఖ్యమైన పాఠాలు

- మీ క్లయింట్‌కు LLM ను జోడించడం MCP సర్వర్లతో వినియోగదారులు మెరుగైన విధంగా ఇంటరాక్ట్ అవ్వడానికి సహాయపడుతుంది.
- MCP సర్వర్ ప్రతిస్పందనను LLM అర్థం చేసుకునే రూపంలోకి మార్చాలి.

## నమూనాలు

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## అదనపు వనరులు

## తదుపరి

- తదుపరి: [Visual Studio Code ఉపయోగించి సర్వర్‌ను వినియోగించడం](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->