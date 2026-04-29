# LLM తో క్లయింట్ సృష్టించడం

ఇప్పటి వరకు, మీరు сервер మరియు క్లయింట్ ఎలా సృష్టించాలో చూశారు. క్లయింట్ సర్వర్ ను స్పష్టంగా పిలిచి దాని సాధనాలు, వనరులు మరియు ప్రాంప్ట్ లను జాబితా చేయగలిగింది. అయితే, ఇది ఒక చాలా ప్రాక్టికల్ దృష్టికోణం కాదు. మీ వినియోగదారులు ఏజెంటిక్ యుగంలో ఉంటారు మరియు ప్రాంప్ట్ లను ఉపయోగించి మరియు LLMతో కమ్యూనికేట్ చేయగలగాలని ఆశిస్తున్నారు. వారు మీరు MCPని ఉపయోగించి మీ సామర్థ్యాలను నిల్వ చేస్తున్నారా లేదా అని పట్టించుకోరు; వారు సహజ భాషతో పరస్పర చర్యచేయాలని ఆశిస్తున్నారు. కాబట్టి మనం దీన్ని ఎలా పరిష్కరిస్తాము? పరిష్కారం క్లయింట్ కి LLM ని జోడించడం.

## అవలోకనం

ఈ పాఠంలో మేము మీ క్లయింట్ లో LLM ని జోడించడంపై ఫోకస్ చేస్తాము మరియు ఇది మీ వినియోగదారుని కోసం ఎలా మెరుగైన అనుభవాన్ని అందిస్తుందో చూపిస్తాము.

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం ముగిసినప్పుడు, మీరు ఈ క్రింది వాటిని చేయగలుగుతారు:

- LLM తో కలిగి ఉన్న క్లయింట్ సృష్టించడం.
- LLM ను ఉపయోగించి MCP సర్వర్ తో సౌమ్యంగా ఇంటరాక్ట్ చేయడం.
- క్లయింట్ వైపు మెరుగైన చివరి వినియోగదారు అనుభవం అందించడం.

## దృష్టికోణం

మనం తీసుకోవలసిన దృష్టికోణం అర్థం చేసుకుందాము. LLM ని జోడించడం సులభంగా అనిపించినా, అసలు మనం దీన్ని నిజంగా చేయగలమా?

క్లయింట్ సర్వర్ తో ఎలా ఇంటరాక్ట్ చేస్తుందో ఇక్కడ ఉంది:

1. సర్వర్ తో కనెక్షన్ ఏర్పాటు చేయండి.

1. సామర్థ్యాలు, ప్రాంప్ట్‌లు, వనరులు మరియు సాధనాలను జాబితా చేసి, వాటి స్కీమ్‌ను సేవ్ చేయండి.

1. ఒక LLM ని జోడించి సేవ్ చేసిన సామర్థ్యాలు మరియు వాటి స్కీమాను LLM అర్థం చేసుకునే ఫార్మాట్ లో అందించండి.

1. వినియోగదారు ప్రాంప్ట్ ను LLM కు ఇవ్వడం, క్లయింట్ జాబితా చేసిన సాధనాలతో కలిసి.

శ్రేష్ఠం, ఇప్పుడు మనం ఎలాగే దీన్ని ఉన్నత స్థాయిలో చేసుకోవచ్చో అర్థం చేసుకున్నాము, క్రింది వ్యాయామంలో దీన్ని ప్రయత్నిద్దాము.

## వ్యాయామం: LLMతో క్లయింట్ సృష్టించడం

ఈ వ్యాయామంలో, మనం మన క్లయింట్ కు LLM ని ఎలా జోడించాలో నేర్చుకోబోతున్నాము.

### GitHub పర్సనల్ యాక్సెస్ టోకెన్ ఉపయోగించి ప్రామాణీకరణ

GitHub టోకెన్ సృష్టించడం ఒక సులভమైన ప్రక్రియ. ఇక్కడ మీరు దీన్ని ఎలా చేయాలో ఉంది:

- GitHub సెట్టింగ్స్ కి వెళ్లండి – టాప్ రైట్ మూలలో మీ ప్రొఫైల్ చిత్రాన్ని క్లిక్ చేసి సెట్టింగ్స్ ఎంచుకోండి.
- డెవలపర్ సెట్టింగ్స్ కు వెళ్ళండి – స్క్రోల్ చేసి డెవలపర్ సెట్టింగ్స్ పై క్లిక్ చేయండి.
- పర్సనల్ యాక్సెస్ టోకెన్స్ (PAT) ఎంపిక చేసుకోండి – ఫైన్-గ్రెయిన్ టోకెన్స్ క్లిక్ చేసి నూతన టోకెన్ సృష్టించండి.
- మీ టోకెన్ ను సెట్ చేయండి – సూచన కోసం ఒక నోటు జోడించండి, గడువు తేదీ ఎంపిక చేసుకోండి, అవసరమైన స్కోప్స్ (అధికారం) ఎంచుకోండి. ఇక్కడ Models అనుమతిని తప్పనిసరిగా జోడించండి.
- టోకెన్‌ను తయారు చేసి కాపీ చేయండి – Generate token పై క్లిక్ చేసి, ఆ తర్వాత వెంటనే దాన్ని కాపీ చేసుకోండి, ఎందుకంటే మరోసారి చూడలేరు.

### -1- సర్వర్ కి కనెక్ట్ అవ్వడం

ముందుగా మన క్లయింట్‌ను సృష్టిద్దాం:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా చెల్లింపు కోసం zod ని దిగుమతి చేసుకోండి

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

పూర్వపు కోడ్ లో మనం:

- అవసరమైన లైబ్రరీలను దిగుమతి చేసుకున్నాం
- `client` మరియు `openai` అనే రెండు సభ్యులతో క్లాస్ సృష్టించాం, ఇవి క్లయింట్‌ను నిర్వహించడంలో మరియు LLMతో ఇంటరాక్ట్ చేయడంలో సహాయపడతాయి.
- మన LLM ఉదాహరణను GitHub Models ను ఉపయోగించేందుకు `baseUrl` ను ఇన్ఫరెన్స్ API కి పాయింట్ చేసేలా కాన్ఫిగర్ చేసాము.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio కనెక్షన్ కోసం సర్వర్ పరామితులు సృష్టించండి
server_params = StdioServerParameters(
    command="mcp",  # అమలుచేసే
    args=["run", "server.py"],  # ఐచ్ఛిక కమాండ్ లైన్ ఆర్గుమెంట్లు
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

పూర్వపు కోడ్ లో మనం:

- MCPకి కావలసిన లైబ్రరీలను దిగుమతి చేసుకున్నాం
- ఒక క్లయింట్ సృష్టించాం

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

ముందుగా, మీరు మీ `pom.xml` ఫైల్లో LangChain4j డిపెండెన్సీలను జోడించాలి. MCP ఇంటిగ్రేషన్ మరియు GitHub Models మద్దతు కోసం ఈ డిపెండెన్సీలను జోడించండి:

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
    
    public static void main(String[] args) throws Exception {        // GitHub మోడల్స్‌ను ఉపయోగించడానికి LLMని కాన్ఫిగర్ చేయండి
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // సర్వర్‌కు కనెక్ట్ అవడానికి MCP ట్రాన్స్‌పోర్ట్ సృష్టించండి
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP కస్టమర్‌ను సృష్టించండి
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

పూర్వపు కోడ్ లో మనం:

- **LangChain4j డిపెండెన్సీలు జోడించాం**: MCP ఇంటిగ్రేషన్, OpenAI అధికారిక క్లయింట్ మరియు GitHub Models మద్దతు కోసం
- **LangChain4j లైబ్రరీలను దిగుమతి చేసుకున్నాం**: MCP ఇంటిగ్రేషన్ మరియు OpenAI చాట్ మోడల్ ఫంక్షనాలిటీ కోసం
- **`ChatLanguageModel` సృష్టించాం**: GitHub Models ఉపయోగించేందుకు మీ GitHub టోకెన్ తో కాన్ఫిగర్ చేసినది
- **HTTP ట్రాన్స్‌పోర్ట్ సెట్ చేయడం**: MCP సర్వర్ కి కనెక్ట్ అవ్వడానికి Server-Sent Events (SSE) ఉపయోగించడం
- **MCP క్లయింట్ సృష్టించాం**: ఇది సర్వర్ తో కమ్యూనికేషన్ నిర్వహిస్తుంది
- **LangChain4j యొక్క బిల్ట్-ఇన్ MCP మద్దతును ఉపయోగించాం**: ఇది LLM మరియు MCP సర్వర్లు మధ్య ఇంటిగ్రేషన్ ను సులభతరం చేస్తుంది

#### Rust

ఈ ఉదాహరణ మీకు Rust ఆధారిత MCP సర్వర్ ఉన్నట్లు భావిస్తుంది. మీ దగ్గర ఒకటి లేకుంటే, సర్వర్ సృష్టించడానికి [01-first-server](../01-first-server/README.md) పాఠానికి తిరిగి వెళ్లండి.

మీ Rust MCP సర్వర్ తో, ఒక టెర్మినల్ తెరవండి మరియు సర్వర్ ఉన్న అదే డైరెక్టరీకి నావిగేట్ అవ్వండి. తర్వాత క్రింది కమాండ్ ఉపయోగించి కొత్త LLM క్లయింట్ ప్రాజెక్ట్ సృష్టించండి:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

మీ `Cargo.toml` ఫైల్ కు క్రింది డిపెండెన్సీలను జోడించండి:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI కోసం అధికారిక Rust లైబ్రరీ లేదు, అయినప్పటికీ, `async-openai` క్రేట్ ఒక [క‌మ్యూనిటీ నిర్వహించు లైబ్రరీ](https://platform.openai.com/docs/libraries/rust#rust) గా విస్తృతంగా ఉపయోగించబడుతోంది.

`src/main.rs` ఫైల్ ను తెరిచి దాని కంటెంట్ ను క్రింది కోడ్ తో మార్చండి:

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

    // TODO: టూల్ కాల్లులతో LLM సంభాషణ

    Ok(())
}
```

ఈ కోడ్ ఒక ప్రాథమిక Rust అప్లికేషన్ ను సెట్ చేస్తుంది ఇది MCP సర్వర్ మరియు GitHub Models తో LLM ఇంటరాక్షన్లు కోసం కనెక్ట్ అవుతుంది.

> [!IMPORTANT]
> అప్లికేషన్ రన్ చేసే ముందు `OPENAI_API_KEY` ఎంవిరాన్‌మెంట్ వేరియబుల్ ను మీ GitHub టోకెన్ తో సెట్ చేయండి.

శ్రేష్ఠం, తదుపరి దశకు మేము సర్వర్ పై సామర్థ్యాలను జాబితా చేద్దాం.

### -2- సర్వర్ సామర్థ్యాలు జాబితా చేయండి

ఇప్పుడు మేము సర్వర్ కు కనెక్ట్ అవ్వబోతున్నాము మరియు దాని సామర్థ్యాలను అడుగుతాము:

#### Typescript

అదే క్లాస్ లో క్రింది విధానాలను జోడించండి:

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

పూర్వపు కోడ్ లో మనం:

- సర్వర్ కు కనెక్ట్ అయ్యే కోడ్ `connectToServer` ను జోడించాము.
- మా యాప్ ఫ్లో నిర్వహించే `run` మethoడ్ సృష్టించాము. ఇప్పటివరకు ఇది సాధనాలను జాబితా చేస్తుంది, కానీ దాదాపు త్వరలో దాన్ని మరిన్ని అంశాలతో అభివృద్ధి చేస్తాము.

#### Python

```python
# అందుబాటులో ఉన్న వనరులను జాబితా చేయండి
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# అందుబాటులో ఉన్న టూల్స్ జాబితా చేయండి
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

మేము జోడించినవి:

- వనరులు మరియు సాధనాలను జాబితా చేసి ప్రింట్ చేసాము. సాధనాల కోసం మేము `inputSchema` ని కూడా జాబితా చేశాము, తదుపరి ఉపయోగిస్తాము.

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

పూర్వపు కోడ్ లో మనం:

- MCP సర్వర్ లోని అందుబాటులో ఉన్న సాధనాలను జాబితా చేశాము
- ప్రతి సాధనకి పేరు, వివరణ మరియు దాని స్కీమాని జాబితా చేశాము. వీటిని మేము త్వరలో సాధనాలను కాల్ చేయడానికి ఉపయోగిస్తాము.

#### Java

```java
// MCP టూల్స్‌ను స్వయంచాలకంగా కనుగొనే టూల్ ప్రొవైడర్‌ను సృష్టించండి
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP టూల్ ప్రొవైడర్ స్వయంచాలకంగా నిర్వహిస్తుంది:
// - MCP సర్వర్ నుండి అందుబాటులో ఉన్న టూల్స్‌ను జాబితా చేయడం
// - MCP టూల్ స్కీమాలను LangChain4j ఫార్మాట్‌కు మార్చడం
// - టూల్ అమలు మరియు ప్రతిస్పందనలను నిర్వహించడం
```

పూర్వపు కోడ్ లో మనం:

- MCP సర్వర్ నుండి అన్ని సాధనాలను ఆటోమేటిగ్గా కనుగొని నమోదు చేసుకునే `McpToolProvider` సృష్టించాము
- టూల్ ప్రొవైడర్ MCP సాధన స్కీమాలు మరియు LangChain4j టూల్ ఫార్మాట్ మద్య మార్పిడి నిర్వహిస్తుంది
- ఈ విధానం మాన్యువల్ సాధన జాబితా మరియు మార్పిడి ప్రక్రియను ఆవరణ చేస్తుంది

#### Rust

MCP సర్వర్ నుంచి సాధనాలను పొందటం `list_tools` పద్ధతితో జరుగుతుంది. మీ `main` ఫంక్షన్ లో MCP క్లయింట్ సెట్ తరువాత, క్రింది కోడ్ జోడించండి:

```rust
// MCP టూల్ జాబితాను పొందండి
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- సర్వర్ సామర్థ్యాలను LLM సాధనాలుగా మార్చడం

సర్వర్ సామర్థ్యాల జాబితా తర్వాత తదుపరి దశ వాటిని LLM అర్థం చేసుకునే ఫార్మాట్ కు మార్చడం. దీన్ని చేసిన తరువాత, మేము ఈ సామర్థ్యాలను LLMకి సాధనాలుగా అందించగలము.

#### TypeScript

1. MCP సర్వర్ నుండి వచ్చిన స్పందనను LLM ఉపయోగించే సాధన ఫార్మాట్ కు మార్చడానికి క్రింది కోడ్ జోడించండి:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ఇన్‌పుట్_schema ఆధారంగా ఒక సోడ్ స్కీమాను సృష్టించండి
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

    ```

    పై కోడ్ MCP సర్వర్ నుండి వచ్చిన ప్రతిస్పందనను LLM అర్థం చేసుకునే సాధన నిర్వచన ఫార్మాట్ కు మార్చుతుంది.

1. తరువాత `run` మెథడ్ అప్డేట్ చేసి సర్వర్ సామర్థ్యాలను జాబితా చేయండి:

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

    పూర్వపు కోడ్ లో, మేము `run` మెథడ్ అప్డేట్ చేసి ఫలితాలను మ్యాప్ చేయగా ప్రతి ఎంట్రీకి `openAiToolAdapter` పిలిచాము.

#### Python

1. ముందుగా, క్రింది కన్వర్టర్ ఫంక్షన్ సృష్టిద్దాం:

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

    `convert_to_llm_tools` ఫంక్షన్ లో మేము MCP సాధన ప్రతిస్పందనను తీసుకుని LLM అర్థం చేసుకునే ఫార్మాట్ కు మార్చుతాము.

1. తదుపరి, ఈ ఫంక్షన్ ను ఉపయోగించేందుకు క్లయింట్ కోడ్ అప్డేట్ చేద్దాం:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ఇక్కడ, మేము MCP సాధన ప్రతిస్పందనను LLMకి ఇస్తున్నదానికి మార్చేందుకు `convert_to_llm_tool` పిలుపునివ్వుతున్నాము.

#### .NET

1. MCP సాధన ప్రతిస్పందనను LLM అర్థం చేసుకునే విధంగా మార్చేందుకు కోడ్ జోడిద్దాం:

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

పూర్వపు కోడ్ లో మనం:

- పేరు, వివరణ, మరియు ఇన్‌పుట్ స్కీరా తీసుకుని `ConvertFrom` ఫంక్షన్ సృష్టించాము.
- FunctionDefinition ని సృష్టించి అది ChatCompletionsDefinition కు ఇవ్వబడుతుంది. ఇదే LLM అర్థం చేసుకునేది.

1. ముందు ఉన్న కోడ్ ను ఈ ఫంక్షన్ ఉపయోగించేందుకు ఎలా మార్చాలో చూద్దాం:

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
// సహజభాషా పరస్పర చర్య కోసం బాట్ ఇంటర్‌ఫేస్ రూపొందించండి
public interface Bot {
    String chat(String prompt);
}

// LLM మరియు MCP సాధనాలతో AI సేవను కన్ఫిగర్ చేయండి
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

పూర్వపు కోడ్ లో మనం:

- సహజ భాష ఇంటరాక్షన్ల కోసం ఒక సాధారణ `Bot` ఇన్‌టర్‌ఫేస్ నిర్వచించాము
- LangChain4j యొక్క `AiServices` ఉపయోగించి LLM ను MCP టూల్ ప్రొవైడర్ తో ఆటోమేటిగ్గా బైండ్ చేశాము
- ఫ్రేమ్‌వర్క్ ఆటోమేటిగ్గా సాధన స్కీమా మార్పిడి మరియు ఫంక్షన్ కాలింగ్ నిర్వహిస్తుంది
- ఈ విధానం మానవీయ సాధన మార్పిడిని తొలగించ ఉంది - LangChain4j MCP సాధనాలను LLMకు అనుకూలమైన ఫార్మాట్ లో మార్చే సంక్లిష్టతలను నిర్వహిస్తుంది

#### Rust

MCP సాధన ప్రతిస్పందనను LLM అర్థం చేసుకునే ఫార్మాట్ లోకి మార్చేందుకు, సాధనాల జాబితాను ఫార్మాట్ చేసే సహాయక ఫంక్షన్ జోడిస్తాము. మీ `main.rs` లో `main` ఫంక్షన్ దిగువ క్రింది కోడ్ జోడించండి. ఇది LLM కు అభ్యర్థనలు పంపేటప్పుడు పిలవబడుతుంది:

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

శ్రేష్ఠం, ఇప్పుడు వినియోగదారుల అభ్యర్థనలను నిర్వహించుకునేందుకు సిద్ధంగా ఉన్నాము.

### -4- వినియోగదారు ప్రాంప్ట్ అభ్యర్థనను నిర్వహించండి

ఈ భాగం లో మేము వినియోగదారు అభ్యర్థనలను నిర్వహిస్తాము.

#### TypeScript

1. మన LLM ను పిలవడానికి ఉపయోగించేటట్లు ఒక మెథడ్ జోడిద్దాం:

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

    పూర్వపు కోడ్ లో మనం:

    - `callTools` అనే మెథడ్ జోడించాం.
    - ఈ మెథడ్ LLM స్పందన తీసుకొని, ఏ సాధనాలు పిలవబడ్డాయో తనిఖీ చేస్తుంది:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // టూల్‌ను కాల్ చేయండి
        }
        ```

    - LLM సూచించినట్లయితే సాధన పిలవడం:

        ```typescript
        // 2. సర్వర్ టూల్‌ను కాల్ చేయండి
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ఫలితంతో ఏదైనా చేయండి
        // చేయాల్సినది
        ```

1. `run` మెథడ్ లో LLM పిలుపులు మరియు `callTools` పిలుపు చేరుస్తూ అప్డేట్ చేయండి:

    ```typescript

    // 1. LLM కోసం ఇన్పుట్ అయిన సందేశాలను సృష్టించండి
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ను పిలవటం
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM స్పందనను పరిశీలించండి, ప్రతి ఎంపికకు టూల్ కాల్స్ ఉన్నాయా చుడండి
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

శ్రేష్ఠం, మొత్తం కోడ్ జాబితాను చూద్దాం:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా సరిచూడటానికి zod ను దిగుమతి చెయ్యండి

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // భవిష్యత్తులో ఈ URL కు మార్చవలసి ఉండవచ్చు: https://models.github.ai/inference
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
          // ఇన్‌పుట్ స్కీమా ఆధారంగా zod స్కీమాను సృష్టించండి
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
    
          // 3. ఫలితంతో ఏదో చేయండి
          // TODO
    
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
    
        // 1. LLM ప్రతిస్పందనలోకి వెళ్లి, ప్రతి ఎంపిక కోసం, అందులో టూల్ కాల్స్ ఉన్నాయో లేరో చెక్ చేయండి
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

1. LLM పిలవడానికి అవసరమైన దిగుమతులు జోడిద్దాం:

    ```python
    # ఎల్పీఎం
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. తర్వాత, LLM పిలవటానికి ఫంక్షన్ జోడిద్దాం:

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
            # ఐచ్ఛిక కాపరాములు
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

    పూర్వపు కోడ్ లో:

    - MCP సర్వర్ నుండి కనుగొన్న మరియు మార్చిన ఫంక్షన్లను LLM కు అందించడం.
    - ఆ తర్వాత ఆ ఫంక్షన్లతో LLM పిలవడం.
    - ఫలితాన్ని పరిశీలించి ఏ ఫంక్షన్లు పిలవాలో చూడటం.
    - చివరగా పిలవాల్సిన ఫంక్షన్ల జాబితా పంపడం.

1. చివరి దశగా, ప్రధాన కోడ్ అప్డేట్ చేద్దాం:

    ```python
    prompt = "Add 2 to 20"

    # LLM నుండి అందరికీ ఏ పరికరాలు అవసరమో అడగండి, ఉంటే
    functions_to_call = call_llm(prompt, functions)

    # సూచించిన ఫంక్షన్లను పిలచండి
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ఇక్కడ, పైన కోడ్ లో:

    - LLM సూచించిన ఫంక్షన్ ద్వారా MCP సాధనాన్ని `call_tool` తో పిలవడం.
    - సాధన పిలుపు ఫలితాన్ని MCP సర్వర్ కు ప్రింట్ చేయడం.

#### .NET

1. LLM ప్రాంప్ట్ అభ్యర్థన కోసం కోడ్ చూపుదాం:

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

    పూర్వపు కోడ్ లో:

    - MCP సర్వర్ నుండి సాధనాలను తీసుకొచ్చారు, `var tools = await GetMcpTools()`.
    - వినియోగదారు ప్రాంప్ట్ `userMessage` నిర్వచించారు.
    - మోడల్ మరియు సాధనాలు స్పెసిఫై చేసిన ఆప్షన్స్ ఆబ్జెక్ట్ సృష్టించారు.
    - LLM కి అభ్యర్థన చేసారు.

1. చివరి దశగా, LLM సూచించినట్లయితే ఫంక్షన్ పిలవాలా చూడండి:

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

    పూర్వపు కోడ్ లో:

    - ఫంక్షన్ పిలుస్తున్న జాబితా పై పునరావృతం చేశారు.
    - ప్రతి సాధన పిలుపు కోసం పేరు మరియు ఆర్గ్యూమెంట్లను తీసుకొని MCP క్లయింట్ ఉపయోగించి కాల్ చేసి ఫలితాలను ప్రింట్ చేశారు.

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

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // MCP టూల్స్ ను స్వయంచాలకంగా ఉపయోగించే సహజ భాషా అభ్యర్థనలను అమలు చేయండి
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

పూర్వపు కోడ్ లో:

- సహజ భాష ప్రాంప్ట్ లను ఉపయోగించి MCP సర్వర్ సాధనాలతో ఇంటరాక్ట్ చేశాము
- LangChain4j ఫ్రేమ్‌వర్క్ ఆటోమేటిగ్గా నిర్వహిస్తుంది:
  - అవసరమైతే వినియోగదారు ప్రాంప్ట్ లను సాధన కాల్స్ కు మార్చడం
  - LLM నిర్ణయం ఆధారంగా సరైన MCP సాధనాలను కాల్ చేయడం
  - LLM మరియు MCP సర్వర్ మధ్య సంభాషణ ప్రవాహాన్ని నిర్వహించడం
- `bot.chat()` విధానం సహజ భాష ప్రతిస్పందనలు ఇస్తుంది, వాటిలో MCP సాధన ఫలితాలు ఉండవచ్చు
- ఈ దృష్టికోణం వినియోగదారులకు seamless అనుభవాన్ని అందిస్తుంది, వారు MCPలోని వెనక ప్రదేశాన్ని తెలుసుకోవాల్సిన అవసరం ఉండదు

పూర్తి కోడ్ ఉదాహరణ:

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

ఇక్కడ ఎక్కువ భాగం పని జరుగుతుంది. మేము ప్రారంభ వినియోగదారు ప్రాంప్ట్ తో LLM ను పిలిచే మోడ్ లో ఉంటాము, ఆ తర్వాత ఏ సాధనాలు పిలవాలి అంటే చూసి, అవసరమైతే వాటిని పిలిచి, ఇంకొంతం కాల్ అవసరం లేదంటే చర్చను ముగిస్తాం.

LLM కు అనేక పిలుపులు ఇవ్వబోతున్నాము, కాబట్టి LLM పిలుపును నిర్వహించడానికి ఒక ఫంక్షన్ నిర్వచిద్దాం. ఈ క్రింది ఫంక్షన్ ను మీ `main.rs` ఫైల్ కు జోడించండి:

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

ఈ ఫంక్షన్ LLM క్లయింట్, సందేశాల జాబితా (వినియోగదారు ప్రాంప్ట్ సహా), MCP సర్వర్ నుంచి సాధనాలను తీసుకుని LLM కి అభ్యర్థన పంపుతుంది, మరియు ప్రతిస్పందన నిమిత్తం తిరిగి పంపుతుంది.
LLM నుంచి వచ్చిన ప్రతిస్పందన `choices` అనే య array‌ని కలిగి ఉంటుంది. ఏమైనా `tool_calls` ఉన్నాయో లేదో చూసేందుకు ఫలితాన్ని ప్రాసెస్ చేయాల్సి ఉంటుంది. ఇది మాకు LLM ఒక నిర్దిష్ట టూల్‌ను ఆర్గ్యుమెంట్లతో పిలవాలని కోరుతుందనే విషయం తెలియజేస్తుంది. LLM స్పందనను హ్యాండిల్ చేయేందుకు కింది కోడ్‌ని మీ `main.rs` ఫైల్ దిగువకు జత చేయండి:

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

    // వెచ్చించదగిన విషయం ఉంటే ప్రింట్ చేయండి
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // టూల్ కాల్స్ నిర్వహించండి
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // సహాయం సందేశాన్ని జత చేయండి

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

            // సందేశాలకు టూల్ ఫలితాన్ని జత చేయండి
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

`tool_calls` ఉన్నట్లయితే, అది టూల్ సమాచారాన్ని తీసుకొంటుంది, టూల్ రిక్వెస్ట్‌తో MCP సర్వర్‌ను పిలుస్తుంది, మరియు ఫలితాలను సంభాషణ సందేశాలలో జత చేస్తుంది. తరువాత LLMతో సంభాషణ కొనసాగుతుంది మరియు సందేశాలు అసిస్టెంట్ ప్రతిస్పందన మరియు టూల్ కాల్ ఫలితాలతో అప్‌డేట్ అవుతాయి.

LLM MCP కాల్స్ కోసం రిటర్న్ చేసే టూల్ కాల్ సమాచారాన్ని తీయడానికి ఇంకో సహాయక ఫంక్షన్‌ని జోడించబోతున్నాము, కాల్ చేయడానికి అవసరమైన ప్రతిదీ తీయడానికి. మీ `main.rs` ఫైల్ దిగువకు కింద ఇచ్చిన కోడ్‌ను జత చేయండి:

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

అన్ని భాగాలు సిద్ధంగా ఉన్నందున, ప్రారంభ యూజర్ ప్రాంప్ట్‌ను హ్యాండిల్ చేసి LLMని పిలవడానికి మా `main` ఫంక్షన్‌ను క్రింది కోడ్‌తో అప్డేట్ చేయండి:

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

ఇది ప్రారంభ యూజర్ ప్రాంప్ట్‌తో LLMని క్వెరీ చేస్తుంది, రెండు నెంబర్‌ల సమాన్ని అడుగుతుంది, మరియు ప్రతిస్పందనను డైనమిక్గా టూల్ కాల్స్ హ్యాండిల్ చేసేటట్లు ప్రాసెస్ చేస్తుంది.

చాలా బాగుంది, మీరు చేస్తున్నది!

## అసైన్‌మెంట్

వ్యాయామం నుండీ కోడ్‌ని తీసుకుని కొన్ని మరింత టూల్స్‌తో సర్వర్‌ని నిర్మించండి. తర్వాత వ్యాయామంలో ఉన్నట్టు LLMతో క్లయింట్‌ని సృష్టించి వివిధ ప్రాంప్ట్స్‌తో పరీక్షించి మీ సర్వర్ టూల్స్ డైనమిక్గా పిలవబడుతున్నాయో లేదో నిర్ధారించుకోండి. ఈ విధంగా క్లయింట్‌ని నిర్మించడం ద్వారా చివరి యూజర్‌కు ఒక అద్భుతమైన వినియోగదార అనుభవం కలుగుతుంది, ఎందుకంటే వారు ఖచ్చితమైన క్లయింట్ ఆజ్ఞల బదులు ప్రాంప్ట్‌లను ఉపయోగించగలుగుతారు మరియు ఏ MCP సర్వర్ పిలవబడుతున్నదో గ్రహించలేరు.

## పరిష్కారం

[పరిష్కారం](./solution/README.md)

## ముఖ్య అంశాలు

- మీ క్లయింట్‌లో LLMని చేర్చడం MCP సర్వర్‌లతో యూజర్లు సంభాషించే మెరుగైన మార్గాన్ని అందిస్తుంది.
- MCP సర్వర్ ప్రతిస్పందనను LLM అర్థం చేసుకునేలా మార్చుకోవాల్సి ఉంటుంది.

## నమూనాలు

- [జావా క্যাল్క్యులేటర్](../samples/java/calculator/README.md)
- [.Net కెల్యుక్యులేటర్](../../../../03-GettingStarted/samples/csharp)
- [జావాస్క్రిప్ట్ కెల్యుక్యులేటర్](../samples/javascript/README.md)
- [టైప్‌స్క్రిప్ట్ కెల్యుక్యులేటర్](../samples/typescript/README.md)
- [పైథాన్ కెల్యుక్యులేటర్](../../../../03-GettingStarted/samples/python)
- [రస్ట్ కెల్యులేటర్](../../../../03-GettingStarted/samples/rust)

## అదనపు వనరులు

## తర్వాతి అధ్యాయం

- తర్వాత: [విజువల్ స్టూడియో కోడ్ ఉపయోగించి సర్వర్ వినియోగించడం](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**విలువ సూచన**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి కృషి చేస్తున్నా, ఆటోమేటిక్ అనువాదాల్లో పొరపాట్లు లేదా అసమగ్రతలు ఉండవచ్చు. సొంత భాషలో ఉన్న అసలు డాక్యుమెంట్‌ను అధికారం గల మూలంగా తీసుకోవాలి. కీలక సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడింది. ఈ అనువాదం ఉపయోగించే దృష్ట్యా ఏవైనా అనర్థాలు లేదా తప్పుదోషాలకు మేము బాధ్యులు కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->