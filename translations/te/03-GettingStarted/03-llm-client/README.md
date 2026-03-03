# LLMతో క్లయింట్ సృష్టించడం

ఇప్పటివరకు, మీరు సర్వర్ మరియు క్లయింట్ ఎలా సృష్టించాలో చూశారు. క్లయింట్ స్పష్టంగా సర్వర్‌ను పిలిచి దాని టూల్స్, వనరులు మరియు ప్రాంప్ట్స్ లిస్ట్ చేయగలిగింది. అయితే, ఇది చాలా అనుకూలమైన విధానం కాదు. మీ ఉపయోగించుకునేవారు ఏజెంటిక్ యుగంలో ఉంటారు మరియు ప్రాంప్ట్‌లు ఉపయోగించి మరియు LLMతో సంభాషించాలనుకుంటారు. వారు మీరు మీ సామర్థ్యాలను నిల్వ చేసేందుకు MCP ఉపయోగిస్తున్నారా కాదా అనేది పట్టించుకోరు; వారు సహజ భాషను ఉపయోగించి పరస్పరం కమ్యూనికేట్ చేయాలని ఆశిస్తారు. అలా అయితే దీన్ని ఎలా పరిష్కరించాలి? పరిష్కారం క్లయింట్‌లో LLMను జోడించడం.

## అవలోకనం

ఈ పాఠంలో మేము మీ క్లయింట్‌లో LLMను జోడించడం పై దృష్టి పెట్టి, ఇది మీ వినియోగదారికి చాలా మెరుగైన అనుభవం ఎలా అందిస్తుందో చూపిస్తాము.

## శిక్షణ లక్ష్యాలు

ఈ పాఠం పూర్తయ్యేటప్పుడు, మీరు వీటిని చేయగలుగుతారు:

- LLMతో ఒక క్లయింట్ సృష్టించటం.
- LLM ఉపయోగించి ఎమ్‌సీపీ సర్వర్‌తో సుసంధానంగా పరస్పరం చేయటం.
- క్లయింట్ వైపున మెరుగైన చివరి వినియోగదారు అనుభవం అందించడం.

## విధానము

మనం తీసుకోవలసిన విధానాన్ని అర్థం చేసుకుందాం. LLM‌ను జోడించడం సులభం అనిపించవచ్చు, కానీ నిజంగా మేము దీనిని ఎలా చేయగలము?

క్లయింట్ సర్వర్‌తో పరస్పరం చేయగల విధానం:

1. సర్వర్‌తో కనెక్షన్ స్థాపించండి.

1. సామర్థ్యాలు, ప్రాంప్ట్లు, వనరులు మరియు టూల్స్‌ను లిస్ట్ చేసి, వాటి స్కీమాను సేవ్ చేయండి.

1. LLMను జోడించి సేవ్ చేసిన సామర్థ్యాలు మరియు వాటి స్కీమాను LLM అర్థం చేసుకునే ఫార్మాట్‌లో పాస్ చేయండి.

1. ఒక యూజర్ ప్రాంప్ట్‌ను తీసుకుని దానిని క్లయింట్ లిస్ట్ చేసిన టూల్స్‌తో కలిసి LLMకు పంపండి.

బాగుంది, ఇప్పుడు మేము ఈ విధంగా ఎలా చేయాలో అర్థం చేసుకున్నాము, కింద ఉన్న వ్యాయామంలో దీన్ని ప్రయత్నిద్దాం.

## వ్యాయామం: LLMతో క్లయింట్ సృష్టించడం

ఈ వ్యాయామంలో, మనం LLMను మన క్లయింట్‌కు జోడించటం నేర్చుకోబోతున్నాం.

### GitHub వ్యక్తిగత యాక్సెస్ టోకెన్ ఉపయోగించి ధృవీకరణ

GitHub టోకెన్ సృష్టించడం సరళమైన ప్రక్రియ. ఇట్లా చేయండి:

- GitHub సెట్టింగ్స్‌కి వెళ్లండి – పైన ఎడమవైపు ఉన్న ప్రొఫైల్ చిత్రం క్లిక్ చేసి Settings ఎంచుకోండి.
- Developer Settingsకు వెళ్లండి – దిగువకు స్క్రోల్ చేసి Developer Settings క్లిక్ చేయండి.
- Personal Access Tokens ఎంచుకోండి – Fine-grained tokens పై క్లిక్ చేసి Generate new token ఎంచుకోండి.
- మీ టోకెన్‌ను కాన్ఫిగర్ చేయండి – రిఫరెన్స్కోసం ఒక నోట్ జోడించండి, గడువు తేదీ సెట్ చేయండి మరియు అవసరమైన స్కోప్స్ (అధికారాలు) ఎంచుకోండి. ఈ సందర్భంలో Models అనువాదాన్ని జోడించాలి.
- Generate చేసి టోకెన్‌ను కాపి చేసుకోండి – Generate token క్లిక్ చేయండి, వెంటనే కాపి చేయండి, మీరు మళ్లీ చూడలేరు.

### -1- సర్వర్‌కు కనెక్ట్ కావడం

ముందుగా మనం మన క్లయింట్‌ను సృష్టిద్దాం:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా సరిచూసుకోవడానికి zod ను దిగుమతి చేసుకోండి

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

ఇంతకుముందు కాడ్‌లో మేము:

- అవసరమైన లైబ్రరీలను దిగుమతి చేసుకున్నాము
- క్లయింట్ మరియు LLMతో పరస్పరం చేయడానికి సహాయపడే రెండు సభ్యులు కలిగిన ఒక క్లాస్ సృష్టించాము: `client` మరియు `openai`.
- మన LLM ఉదాహరణను GitHub Models ఉపయోగించడానికి `baseUrl`ని inference APIకి సూచించే విధంగా కాన్ఫిగర్ చేసాము.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio కనెక్షన్ కోసం సర్వర్ పరామితులను తయారుచేయండి
server_params = StdioServerParameters(
    command="mcp",  # నడిపించదగిన ఫైలు
    args=["run", "server.py"],  # ఐచ్ఛిక కమాండ్ లైన్ ఆర్గ్యుమెంట్లు
    env=None,  # ఐచ్ఛిక పర్యావరణ త్రుటింగులు
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # కనెక్షన్ ప్రారంభించండి
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

ఇంతకుముందు కాడ్‌లో మేము:

- MCP కోసం అవసరమైన లైబ్రరీలను దిగుమతి చేసుకున్నాము
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

#### Java

ముందుగా, మీరు మీ `pom.xml` ఫైల్‌లో LangChain4j ఆధారాలను జోడించాలి. MCP ఇంటిగ్రేషన్ మరియు GitHub Models మద్దతు కోసం ఈ ఆధారాలను జోడించండి:

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

తరువాత మీ Java క్లయింట్ క్లాస్ సృష్టించండి:

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
    
    public static void main(String[] args) throws Exception {        // LLM ను GitHub మోడల్స్ ఉపయోగించేందుకు కాన్ఫిగర్ చేయండి
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // సర్వర్‌కు కనెక్ట్ అవ్వడానికి MCP ట్రాన్స్‌పోర్ట్ సృష్టించండి
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

ఇంతకుముందు కోడ్‌లో మేము:

- **LangChain4j ఆధారాలను జోడించాము**: MCP ఇంటిగ్రేషన్, OpenAI అధికారిక క్లయింట్, మరియు GitHub Models మద్దతు కోసం
- **LangChain4j లైబ్రరీలను దిగుమతి చేసుకున్నాము**: MCP కలిపి మరియు OpenAI చాట్ మోడల్ ఫంక్షనాలిటి కోసం
- **`ChatLanguageModel` సృష్టించాము**: మీ GitHub టోకెనుతో GitHub Models ఉపయోగించాలని కాన్ఫిగర్ చేయబడి
- **HTTP ట్రాన్స్‌పోర్ట్ ఏర్పాటు చేసాము**: Server-Sent Events (SSE) ఉపయోగించి MCP సర్వర్‌తో కనెక్ట్ అవడం కోసం
- **MCP క్లయింట్ సృష్టించాము**: ఇది సర్వర్‌తో కమ్యూనికేషన్ నిర్వహిస్తుంది
- **LangChain4jలో నిర్మిత MCP మద్దతు వాడాము**: ఇది LLMs మరియు MCP సర్వర్ల మధ్య ఇంటిగ్రేషన్ సులభతరం చేస్తుంది

#### Rust

ఈ ఉదాహరణలో మీరు Rust ఆధారిత MCP సర్వర్ ని నడుపుతూనే ఉన్నారని భావిస్తుంది. ఒకటి లేకపోతే, సర్వర్ సృష్టించడానికి [01-first-server](../01-first-server/README.md) పాఠాన్ని చూడండి.

మీకు Rust MCP సర్వర్ ఉన్నప్పుడు, ఒక టెర్మినల్ తెరచి సర్వర్ ఉన్న డైరెక్టరీకి వెళ్ళండి. తరువాత క్రింది కమాండ్ ఉపయోగించి కొత్త LLM క్లయింట్ ప్రాజెక్ట్ సృష్టించండి:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

మీ `Cargo.toml` ఫైల్‌కు కింది ఆధారాలు జోడించండి:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI కోసం అధికారిక Rust లైబ్రరీ లేదు, అయితే `async-openai` క్రేట్ ఒక [కమ్యూనిటీ నిర్వహిస్తున్న లైబ్రరీ](https://platform.openai.com/docs/libraries/rust#rust)గా సాధారణంగా ఉపయోగిస్తారు.

`src/main.rs` ఫైల్ తెరచి దాని కంటెంట్‌ను కింది కోడ్‌తో మార్చండి:

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

    // OpenAI క్లయింట్ సెٹప్ చేయండి
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

    // చేయవలసింది: MCP టూల్ జాబితా పొందండి

    // చేయవలసింది: టూల్ కాల్స్ తో LLM సంభాషణ

    Ok(())
}
```

ఈ కోడ్ ఒక ప్రాథమిక Rust అప్లికేషన్‌ను సెట్ చేస్తుంది, ఇది MCP సర్వర్ మరియు GitHub Modelsతో LLM పరస్పరం కోసం కనెక్ట్ అవుతుంది.

> [!IMPORTANT]
> యాప్‌ను నడపడానికి ముందు `OPENAI_API_KEY` ఎన్విరాన్‌మెంట్ వేరియబుల్‌ను మీ GitHub టోకెనుతో సెట్ చేయడం మర్చిపోకండి.

బాగుంది, మన తదుపరి దశకు, సర్వర్‌పై సామర్థ్యాలను లిస్ట్ చేద్దాం.

### -2- సర్వర్ సామర్థ్యాలు లిస్ట్ చేయడం

ఇప్పుడు మనం సర్వర్‌ను కనెక్ట్ చేసి దాని సామర్థ్యాలను కోరుకోబోతున్నాము:

#### Typescript

అనే క్లాస్‌లో కింది మెథడ్స్ జోడించండి:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // టూల్స్ జాబితా రూపొందించడం
    const toolsResult = await this.client.listTools();
}
```

ఇంతకుముందు కోడ్‌లో మేము:

- సర్వర్‌తో కనెక్ట్ కావడం కోసం కోడ్ జోడించాము, `connectToServer`.
- మన యాప్ ప్రవాహం నిర్వహణ కోసం `run` మెథడ్ సృష్టించాము. ఇప్పటివరకూ ఇది కేవలం టూల్స్ లిస్ట్ చేస్తుంది, కానీ త్వరలో దీనిలో మరిన్ని జోడిస్తాము.

#### Python

```python
# అందుబాటులో ఉన్న వనరులను జాబితా చెయ్యండి
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# అందుబాటులో ఉన్న సాధనాలను జాబితా చెయ్యండి
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ఇక్కడ మేము జోడించినవి:

- వనరులు మరియు టూల్స్ లిస్ట్ చేసి, వాటిని ప్రింట్ చేశాము. టూల్స్ కోసం `inputSchema` కూడా లిస్ట్ చేశాము, దీన్ని తర్వాత ఉపయోగిస్తాము.

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

ఇంతకుముందు కోడ్‌లో మేము:

- MCP సర్వర్‌లో అందుబాటులో ఉన్న టూల్స్‌ను లిస్ట్ చేశాము
- ప్రతి టూల్ కోసం పేరు, వివరణ మరియు స్కీమా లిస్ట్ చేశాము. స్కీమా అనేది టూల్‌లు పిలవడానికి ఉపయోగించేది.

#### Java

```java
// MCP టూల్స్‌ను ఆటోమేటిక్‌గా కనుగొనే టూల్ ప్రొవైడర్‌ను సృష్టించడం
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP టూల్ ప్రొవైడర్ ఆటోమేటిక్‌గా నిర్వహిస్తుంది:
// - MCP సర్వర్ నుండి అందుబాటులో ఉన్న టూల్స్ జాబితా చేయడం
// - MCP టూల్ స్కీమాలను LangChain4j ఫార్మాట్‌కు మార్చడం
// - టూల్ నిర్వహణ మరియు ప్రతిస్పందనలను నిర్వహించడం
```

ఇంతకుముందు కోడ్‌లో మేము:

- MCP సర్వర్ నుండి అన్ని టూల్స్‌ని ఆటోమేటిగ్గా కనుగొని నమోదు చేసే `McpToolProvider` సృష్టించాము
- టూల్ ప్రొవైడర్ MCP టూల్ స్కీమాలను LangChain4j టూల్ ఫార్మాట్కి అంతర్గతంగా మార్చడం నిర్వహిస్తుంది
- ఈ విధానం మాన్యువల్ టూల్ లిస్టింగ్ మరియు మార్పిడి ప్రక్రియను సరళీకృతం చేస్తుంది

#### Rust

MCP సర్వర్ నుండి టూల్స్ పొందడానికీ `list_tools` మెథడ్ వాడాలి. మీ `main` ఫంక్షన్‌లో MCP క్లయింట్ సెటప్ తర్వాత కింది కోడ్ జోడించండి:

```rust
// MCP టూల్ జాబితాను పొందండి
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- సర్వర్ సామర్థ్యాలను LLM టూల్స్‌గా మార్చడం

సర్వర్ సామర్థ్యాలు లిస్ట్ చేసిన తర్వాత వాటిని LLM అర్థం చేసుకునే ఫార్మాట్ కి మార్చాలి. అప్పుడు ఈ సామర్థ్యాలను LLMకు టూల్స్‌గా అందించుకోవచ్చు.

#### TypeScript

1. MCP సర్వర్ నుండి వచ్చిన రెస్పాన్స్‌ను LLM ఉపయోగించగల టూల్ ఫార్మాట్‌గా మార్చేందుకు కింది కోడ్ జోడించండి:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ఇన్పుట్_స్కీమా ఆధారంగా ఒక జాడ్ స్కీమా సృష్టించండి
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // రకం ను స్పష్టంగా "ఫంక్షన్" గా సెట్ చేయండి
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

    పైన కోడ్ MCP సర్వర్ నుండి వచ్చిన రెస్పాన్స్‌ను LLM అర్థం చేసుకునే టూల్ నిర్వచన ఫార్మాట్‌గా మార్చుతుంది.

1. తరువాత, `run` మెథడ్‌ను అప్డేట్ చేసి సర్వర్ సామర్థ్యాలను లిస్ట్ చేద్దాం:

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

    ఇంతకుముందు కోడ్‌లో, ఫలితంపై మ్యాప్ చేసి ప్రతి ఎంట్రీకి `openAiToolAdapter` పిలవడం ద్వారా `run` మెథడ్‌ను అప్డేట్ చేశాము.

#### Python

1. ముందు ఈ కన్వర్టర్ ఫంక్షన్ సృష్టిద్దాం

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

    పై ఫంక్షన్ `convert_to_llm_tools`లో మేము MCP టూల్ రెస్పాన్స్ తీసుకుని LLM అర్థం చేసుకునే ఫార్మాట్‌లోకి మార్చుతున్నాము.

1. తర్వాత, ఈ ఫంక్షన్‌ని పిలవడానికి క్లయింట్ కోడ్‌ను ఇలా అప్డేట్ చేద్దాం:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ఇక్కడ, MCP టూల్ రెస్పాన్స్‌ని LLMకి ఫీడ్ చేయగలిగే ఫార్మాట్‌కు మార్చడానికి `convert_to_llm_tool` పిలుస్తున్నాము.

#### .NET

1. MCP టూల్ రెస్పాన్స్‌ని LLM అర్థం చేసుకునే ఫార్మాట్‌కు మార్చడానికై కోడ్ జోడిద్దాం

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

ఇంతకుముందు కోడ్‌లో మేము:

- పేరు, వివరణ మరియు ఇన్‌పుట్ స్కీమాతో ఆర్గ్యుమెంట్స్ తీసుకుని `ConvertFrom` ఫంక్షన్ సృష్టించినాము.
- ఫంక్షన్ `FunctionDefinition` తయారుచేసి ఇది తర్వాత `ChatCompletionsDefinition`కి పాస్ చేస్తుంది. ఇది LLM అర్థం చేసుకునేది.

1. ఈ ఫంక్షన్ ఉపయోగించడానికి ఉన్న కోడ్ ఎలా మార్చాలో చూద్దాం:

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
// సహజ భాషా ఇంటరాక్షన్ కోసం బాట్ ఇంటర్ఫేస్‌ను సృష్టించడం
public interface Bot {
    String chat(String prompt);
}

// LLM మరియు MCP టూల్స్‌తో AI సేవ స్పష్టీకరించడం
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ఇంతకుముందు కోడ్‌లో మేము:

- సహజ భాష పరిచయాల కోసం సింపుల్ `Bot` ఇంటర్‌ఫేస్ నిర్వచించాము
- LangChain4j యొక్క `AiServices` ద్వారా LLMను MCP టూల్ ప్రొవైడర్‌తో ఆటోమేటిగ్గా బైండ్ చేశాము
- ఫ్రేమ్‌వర్క్ టూల్ స్కీమా మార్పిడి మరియు ఫంక్షన్ కాల్స్ ఆటోమేటిగ్గా హ్యాండిల్ చేస్తుంది
- ఈ విధానం మాన్యువల్ టూల్ మార్పిడి అవసరాన్ని తొలగించి, MCP టూల్స్‌ను LLM అనుకున్న ఫార్మాట్‌కు మార్చడంలో సులభతనం చేస్తుంది

#### Rust

MCP టూల్ రెస్పాన్స్‌ను LLM అర్థం చేసుకునే ఫార్మాట్‌గా మార్చడానికి, టూల్ లిస్టింగ్ ఫార్మాట్ చేసే సహాయక ఫంక్షన్ జోడిద్దాం. `main.rs`లో `main` ఫంక్షన్ కింద కింద కింది కోడ్ జోడించండి. ఇది LLMకి అభ్యర్థనలు చేసే సమయంలో పిలవబడుతుంది:

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

సరే, ఇప్పుడు మనకు యూజర్ అభ్యర్థనలు నిర్వహించే కోడ్ అవసరం, దాన్ని క్రింద చూద్దాం.

### -4- యూజర్ ప్రాంప్ట్ అభ్యర్థనను నిర్వహించడం

ఈ భాగంలో, మనం యూజర్ అభ్యర్థనలను हाताळించబోతున్నాం.

#### TypeScript

1. మన LLMను పిలవటానికి ఉపయోగించే మెథడ్ జోడిద్దాం:

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
        // చేయవలసింది

        }
    }
    ```

    ఇంతకుముందు కోడ్‌లో మేము:

    - `callTools` అనే మెథడ్ జోడించాము.
    - ఈ మెథడ్ LLM రెస్పాన్స్ తీసుకుని ఎలాంటి టూల్స్ పిలవబడ్డాయో చూసి అటువంటి టూల్స్‌ను పిలుస్తుంది:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // టూల్ కాల్ చేయండి
        }
        ```

    - LLM సూచించినట్లైతేనైనా టూల్‌ను పిలుస్తుంది:

        ```typescript
        // 2. సర్వర్ యొక్క టూల్‌ను కాల్ చేయండి
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ఫలితంతో ఏదో చేయండి
        // చేయవలసింది
        ```

1. `run` మెథడ్‌లో LLMకి కాల్స్ మరియు `callTools` పిలవడాన్ని కలుపుద్దాం:

    ```typescript

    // 1. LLM కోసం ఇన్‌పుట్‌గా సందేశాలను సృష్టించండి
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ను కాల్ చేయడం
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM స్పందనను పరిశీలించండి, ప్రతి ఎంపిక కోసం, దానిలో టూల్ కాల్స్ ఉన్నాయా అని తనిఖీ చేయండి
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

మంచిది, పూర్తి కోడ్ చూస్తే:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // స్కీమా ధృవీకరణకు zod ని దిగుమతి చేసుకోండి

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // భవిష్యత్తులో ఈ URL మార్చుకోవలసి రావొచ్చు: https://models.github.ai/inference
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
          // ఇన్‌పుట్ స్కీమాపై ఆధారంగా ఒక zod స్కీమాను సృష్టించండి
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // టైప్‌ను "function" గా స్పష్టంగా సెట్ చేయండి
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
    
    
          // 2. సర్వర్ టూల్ ని పిలవండి
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ఫలితంతో ఏదైనా చేయండి
          // చేయవలసిన పని
    
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
    
        // 1. LLM ప్రతిస్పందనలో ప్రతి ఎంపిక ద్వారా వెళ్లి, అది టూల్ కాల్స్ ని కలిగి ఉన్నదో లేదో తనిఖీ చేయండి
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

1. LLM పిలవటానికి కావలసిన దిగుమతులు జోడిద్దాం

    ```python
    # ఎల్‌ఎల్ఎం
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. తర్వాత, LLMను పిలవడానికీ ఫంక్షన్ జోడిద్దాం:

    ```python
    # ల్లమ్

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

    ఇంతకుముందు కోడ్‌లో మేము:

    - MCP సర్వర్‌లో కనిపించిన మా ఫంక్షన్లను LLMకి పాస్ చేశాము.
    - ఆ తర్వాత LLMను ఆ ఫంక్షన్స్‌తో పిలిచాము.
    - ఫలితాన్ని పరిశీలించి ఏ ఫంక్షన్స్ పిలవవలసున్నాయో కనిపెట్టాము.
    - చివరగా పిలవాల్సిన ఫంక్షన్స్ జాబితాను పంపాము.

1. చివరి దశ, ప్రధాన కోడ్‌ను నవీకరించుద్దాం:

    ```python
    prompt = "Add 2 to 20"

    # LLM ను అడగండి అందరికీ ఏమైనా ఉపకరణాలు ఉంటే
    functions_to_call = call_llm(prompt, functions)

    # సూచించిన ఫంక్షన్లు పిలవండి
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    అక్కడ, పై కోడ్‌లో మేము:

    - LLM ఏ ఫంక్షన్ పిలవాలనుకుంటుందో అర్థం చేసుకుని `call_tool` ద్వారా MCP టూల్ పిలవడం.
    - టూల్ కాల్ ఫలితాన్ని MCP సర్వర్‌కు ప్రింట్ చేయటం.

#### .NET

1. LLM ప్రాంప్ట్ అభ్యర్థన కోసం కొన్ని కోడ్ చూపుద్దాం:

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

    ఇంతకుముందు కోడ్‌లో మేము:

    - MCP సర్వర్ నుండి టూల్స్ పొందాము, `var tools = await GetMcpTools()`.
    - యూజర్ ప్రాంప్ట్ `userMessage` నిర్వచించాము.
    - మోడల్ మరియు టూల్స్ స్పెసిఫై చేసే ఆప్షన్స్ ఒబ్జెక్ట్ నిర్మించాము.
    - LLMకి అభ్యర్థన పంపాము.

1. ఒక చివరి దశ, LLM ఏ ఫంక్షన్ పిలవాలనుకుంటుందో చూద్దాం:

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

    ఇంతకుముందు కోడ్‌లో మేము:

    - ఫంక్షన్ కాల్స్ జాబితాలో లూప్ వేసాము.
    - ప్రతి టూల్ కాల్ కోసం పేరు, ఆర్గ్యుమెంట్స్ వేరుచేసి MCP క్లయింట్ ఉపయోగించి టూల్ ను పిలిచామో, మరియు ఫలితాన్ని ప్రింట్ చేశాము.

పూర్తి కోడె ఇలా ఉంటుంది:

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

ఇందులో మేము:

- సహజ భాష ప్రాంప్ట్‌లను ఉపయోగించి MCP సర్వర్ టూల్స్‌తో పరస్పరం చేశాము
- LangChain4j ఫ్రేమ్‌వర్క్ ఆటోమేటిగ్గా నిర్వహిస్తుంది:
  - అవసరమైనప్పుడు యూజర్ ప్రాంప్ట్‌లను టూల్ కాల్లుగా మార్చటం
  - LLM నిర్ణయంతో సరిగ్గా MCP టూల్స్ పిలవడం
  - LLM మరియు MCP సర్వర్ మధ్య సంభాషణ ప్రవాహం నిర్వహణ
- `bot.chat()` సహజ భాషలో స్పందనలు ఇస్తుంది, అవి MCP టూల్ నిర్వర్తన ఫలితాలు కూడా కలిగి ఉండవచ్చు
- ఇలా వినియోగదారులకు MCP ప్రాథమిక నిర్మాణం గురించి తెలియకుండా ఒక వర్తించే అనుభవం కలిగిస్తుంది

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

ఇక్కడి అనేక పని జరుగుతుంది. మేము ప్రారంభ యూజర్ ప్రాంప్ట్‌తో LLMను పిలిచి, అనంతరం టూల్స్ పిలవాల్సిన అవసరం ఉందో చూద్దాం. అవసరమైతే ఆ టూల్స్ పిలిచి, LLMతో సంభాషణ కొనసాగిస్తాము, మరింత టూల్ కాల్స్ అవసరం లేకుండా చివరి ప్రతిస్పందన పొందేవరకు.

మనం LLMకు అనేక సార్లు కాల్స్ చేయబోతున్నాం, కనుక LLM కాల్ నిర్వహించే ఫంక్షన్ నిర్వచిద్దాం. ఈ క్రింద ఫంక్షన్‌ను మీ `main.rs` ఫైల్లో జోడించండి:

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

ఈ ఫంక్షన్ LLM క్లయింట్, సందేశాల జాబితా (యూజర్ ప్రాంప్ట్ సహా), MCP సర్వర్ నుండి టూల్స్ తీసుకుని LLMకి అభ్యర్థన పంపి, రెస్పాన్స్ ను తిరిగి ఇవ్వును.
LLM నుండి వచ్చిన సమాధానం `choices` అనే ఒక శ్రేణిని కలిగి ఉంటుందని గమనించండి. ఆ `tool_calls` ఏవైనా ఉన్నారా అని పరిశీలించడానికి ఫలితాన్ని ప్రాసెస్ చేయాల్సి ఉంటుంది. ఇది మనకు LLM ఒక నిర్దిష్ట టూల్ ఆర్గ్యుమెంట్లతో పిలవాలని కోరుకుంటున్నదని తెలియజేస్తుంది. LLM సమాధానాన్ని నిర్వహించడానికి క్రింది కోడ్‌ను మీ `main.rs` ఫైల్ చివరకి జోడించండి:

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

    // ഉള്ളట్లు ఉన్నట్లయితే విషయం ముద్రించు
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // టూల్ కాల్స్‌ను నిర్వహించండి
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // సహాయక సందేశం జోడించండి

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

            // సందేశాలకు టూల్ ఫలితం జోడించండి
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

`tool_calls` ఉన్నట్లయితే, అది టూల్ సమాచారాన్ని తీసుకుని, MCP సర్వర్‌కు టూల్ అభ్యర్థనతో పిలిచే విధంగా చేస్తుంది మరియు ఫలితాలను సంభాషణ సందేశాలలో చేర్చుతుంది. ఆ తర్వాత LLMతో సంభాషణ కొనసాగుతుంది మరియు సందేశాలు అసిస్టెంట్ సమాధానంతో మరియు టూల్ కాల్ ఫలితాలతో నవీకరించబడతాయి.

LLM MCP కాల్స్ కోసం తిరిగివచ్చే టూల్ కాల్ సమాచారాన్ని తీసుకోవడానికి, మరో సహాయక ఫంక్షన్‌ను జోడిస్తాము, ఇది కాల్‌కు అవసరమైన అన్ని వివరాలను విముక్తం చేస్తుంది. క్రింది కోడ్‌ను మీ `main.rs` ఫైల్ చివరకి జోడించండి:

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

అన్ని భాగాలు సెట్ అయ్యాక, ఆరంబిక యూజర్ ప్రాంప్ట్‌ను హ్యాండిల్ చేసి LLMని పిలవడం కోసం, మీ `main` ఫంక్షన్‌ను ఈ విధంగా అప్డేట్ చేయండి:

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

ఇది యూజర్ ప్రారంభ ప్రాంప్ట్‌తో LLMని క్వెరీ చేసి రెండు సంఖ్యల సమ్మే కోరుతుంది, అలాగే టూల్ కాల్స్‌ను డైనమిక్ గా ప్రాసెస్ చేస్తుంది.

అద్భుతం, మీరు ఈ పని పూర్తి చేయగలిగారు!

## అసైన్‌మెంట్

వ్యాయామం నుంచి కోడ్ తీసుకుని, మరిన్ని టూల్స్‌తో సర్వర్‌ను రూపొందించండి. తర్వాత అరగంట LLM ఉన్న క్లయింట్‌ను సృష్టించి, వివిధ ప్రాంప్ట్‌లతో పరీక్షించండి, తద్వారా మీ సర్వర్ టూల్స్ డైనమిక్గా పిలవబడుతున్నాయో చూసుకోండి. ఈ విధంగా క్లయింట్ నిర్మించడం ఎండ్ యూజర్‌కు గొప్ప అనుభూతిని అందిస్తుంది, వారు ఖచ్చితమైన క్లయింట్ ఆదేశాల బదులుగా ప్రాంప్ట్‌లు ఉపయోగించి, ఎలాంటి MCP సర్వర్ పిలవబడుతోందో తెలియకుండా ఉపయోగించగలరు.

## పరిష్కారం

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## ముఖ్యమైన అంశాలు

- LLMని మీ క్లయింట్‌లో చేర్చడం MCP సర్వర్స్‌తో యూజర్లు మెరుగ్గా మెలమడతారు.
- MCP సర్వర్ స్పందనను LLM అర్థం చేసుకునే రూపంలో మార్చాల్సి ఉంటుంది.

## నమూనాలు

- [Java క్యాలిక్యులేటర్](../samples/java/calculator/README.md)
- [.Net క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/csharp)
- [JavaScript క్యాలిక్యులేటర్](../samples/javascript/README.md)
- [TypeScript క్యాలిక్యులేటర్](../samples/typescript/README.md)
- [Python క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/python)
- [Rust క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/rust)

## అదనపు వనరులు

## తర్వాతి దశ

- తర్వాతి: [Visual Studio Code ఉపయోగించి సర్వర్‌ను వినియోగించడం](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టం**:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు లోపాలు లేదా తప్పులు ఉండవచ్చును. స్థానిక భాషలో ఉన్న అసలు పత్రం అధికారం కలిగిన మూలం గా పరిగణించాలి. కీలక సమాచారానికి, వృత్తిపరమైన మానవ అనువాదాన్ని సూచించబడింది. ఈ అనువాదం ఉపయోగంతో ఏర్పడిన ఏమైనా అపార్థాలు లేదా అవగాహనలో తప్పుల కోసం మేము బాధ్యులు కాను.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->