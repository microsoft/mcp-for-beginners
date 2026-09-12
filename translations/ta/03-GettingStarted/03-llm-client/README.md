# LLM உடன் கிளையண்ட் உருவாக்குதல்

> [!NOTE]
> ஜாவா கிளையண்ட் எடுத்துக்காட்டுகள் பாரம்பரிய HTTP+SSE போக்குவரத்தைக் கொண்டு இணைக்கின்றன மற்றும்
> MCP `2025-11-25` SDK APIகளை குறிக்கின்றன. புதிய தொலைவான கிளையண்டுகளுக்கான `2026-07-28` பொருந்தக்கூடிய SDK மற்றும்
> ஸ்ட்ரீமபிள் HTTP ஐப் பயன்படுத்தவும்.

இதுவரை, நீங்கள் ஒரு சேவையகத்தையும் கிளையண்டையும் எப்படி உருவாக்குவது என்பதைப் பார்த்துள்ளீர்கள். கிளையண்ட் பின்னர் திறன்கள், வளங்கள் மற்றும் ஊக்க ஊட்டிகளை பட்டியலிட சேவையகத்தை தெளிவாக அழைக்க முடிந்தது. இருப்பினும், இது மிக பயனுள்ள அணுகுமுறை அல்ல. உங்கள் பயனர்கள் முகாமைத்துவ யுகத்தில் வாழ்கிறார்கள் மற்றும் ஊக்க ஊட்டிகளைப் பயன்படுத்தி ஒரு LLM உடன் தொடர்பு கொள்ள எதிர்பார்க்கிறார்கள். அவர்கள் உங்களுடைய திறன்களை MCPஇல் சேமிக்கிறீர்களா என்பதை கவலைப்படவில்லை; அவர்கள் இயற்கை மொழியைப் பயன்படுத்தி தொடர்பு கொள்க expecting். எனவே, இதை எப்படிப் பிரச்சனையற்றதாக்க முடியும்? பதில், கிளையண்டிற்கு ஒரு LLMஐச் சேர்ப்பது.

## மேலோட்டம்

இபாடத்தில் உங்கள் கிளையண்டில் LLMஐச் சேர்ப்பதில் கவனம் செலுத்தி இது உங்கள் பயனருக்கு சிறந்த அனுபவத்தை எப்படி வழங்குகிறது என்பதைக் காண்போம்.

## கற்றல் இலக்குகள்

இபாடத்தின் முடிவில், நீங்கள்:

- LLM உடன் ஒரு கிளையண்ட் உருவாக்க முடியும்.
- ஒரு LLM ஐப் பயன்படுத்தி MCP சேவையகத்துடன் தெளிவாக தொடர்பு கொள்ள முடியும்.
- கிளையண்ட் பக்கத்தில் சிறந்த இறுதி பயனர் அனுபவம் வழங்க முடியும்.

## அணுகுமுறை

நாம் எடுக்க வேண்டிய அணுகுமுறையை புரிந்துகொள்வோம். LLM சேர்ப்பது எளிதாக தெரிகிறது, ஆனால் உண்மையில் நாம் இதனை செய்வோமா?

கிளையண்ட் சேவையகத்துடன் தொடர்பு கொள்வது எப்படி:

1. சேவையகத்துடன் இணைப்பு ஏற்படுத்துதல்.

1. திறன்கள், ஊக்க ஊட்டிகள், வளங்கள் மற்றும் கருவிகள் பட்டியலிடப்பட்டு, அவற்றின் சிக்கலான அமைப்பை சேமித்தல்.

1. ஒரு LLM ஐச் சேர்த்து, சேமிக்கப்பட்ட திறன்கள் மற்றும் அவற்றின் சிக்கலான அமைப்பை LLM புரிந்து கொள்கின்ற வடிவத்தில் வழங்குதல்.

1. பயனர் ஊக்க ஊட்டியை பெற்றுக்கொண்டு அதை கிளையண்ட் பட்டியலிட்ட கருவிகளுடன் LLM க்கு அனுப்பி கையாளுதல்.

கிழ்காணும் பயிற்சியில் இதைச் செய்வதைப் பார்ப்போம்.

## பயிற்சி: LLM உடன் கிளையண்ட் உருவாக்குதல்

இபயிற்சியில், நாங்கள் LLM ஐ எங்கள் கிளையண்டில் சேர்க்கக் கற்றுக்கொள்வோம்.

### GitHub தனிப்பட்ட அணுகல் குறியீடு மூலம் அங்கீகாரம்

GitHub குறியீட்டை உருவாக்குவது எளிதான செயல்முறை. இதை எப்படி செய்வது என்பதைப் பார்க்கலாம்:

- GitHub அமைப்புக்கு செல்லவும் – மேல் வலது மூலையில் உங்கள் சுவரெடுப்பை கிளிக் செய்து அமைப்புகள் தெரிவு செய்யவும்.
- டெவலப்பர் அமைப்புகளுக்குச் செல்லவும் – கீழே சுருங்கி டெவலப்பர் அமைப்புகளை கிளிக் செய்யவும்.
- தனிப்பட்ட அணுகல் குறியீடுகளைத் தெரிவு செய்யவும் – நுண்ணறிவு குறியீடுகளைத் தேர்ந்தெடுத்து புதிய குறியீடு உருவாக்கவும்.
- உங்கள் குறியீட்டை அமைத்தல் – குறிப்புக்காக ஒரு குறிப்பைச் சேர்க்கவும், காலாவதியான தேதி அமைக்கவும் மற்றும் தேவையான அனுமதிகளைத் தேர்ந்தெடுக்கவும் (இதில் Models அனுமதியைச் சேர்க்க வேண்டும்).
- குறியீட்டை உருவாக்கி நகலெடுக்கவும் – குறியீட்டை உருவாக்கவும், பின்னர் உடனடியாக நகலெடுக்கவும்; ஏனெனில் மறுபடியும் காண முடியாது.

### -1- சேவையகத்துடன் இணையவும்

முதலில் எங்கள் கிளையண்டை உருவாக்குவோம்:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ஸ்கீமா பரிசோதனைக்காக zod ஐ இறக்குமதி செய்க

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

மேலே உள்ள குறியீட்டில் நாங்கள்:

- தேவையான நூலகங்களை இறக்குமதி செய்துள்ளோம்
- `client` மற்றும் `openai` என்ற இரண்டு உறுப்பினர்களுடன் ஒரு வகுப்பை உருவாக்கியுள்ளோம், இது எங்கள் கிளையண்டை நிர்வகிக்கவும் ஒரு LLM உடன் தொடர்பு கொள்ளவும் உதவும்.
- GitHub Models ஐப் பயன்படுத்தும் வகையில் LLM நிகழ்ச்சியை `baseUrl` ஐ inference API-க்கு அமைத்து கட்டமைத்துள்ளோம்.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio இணைக்கும் சேவையக அளவுருக்களை உருவாக்குக
server_params = StdioServerParameters(
    command="mcp",  # இயக்கக்கூடிய
    args=["run", "server.py"],  # விருப்பமான கட்டளை வரி குறிகள்
    env=None,  # விருப்பமான சூழல் மாறிகள்
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # இணைப்பை ஆரம்பிக்கவும்
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

மேலே உள்ள குறியீட்டில் நாங்கள்:

- MCP க்கான தேவையான நூலகங்களை இறக்குமதி செய்தோம்
- ஒரு கிளையண்ட் உருவாக்கினோம்

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

முதலில், உங்கள் `pom.xml` கோப்பில் LangChain4j சார்புகளைச் சேர்க்க வேண்டும். MCP ஒருங்கிணைப்பு மற்றும் OpenAI இணக்கமான MiniMax API க்கான இவற்றைச் சேர்:

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

உங்கள் MiniMax API விசை மற்றும் விருப்பத்திற்கேற்ப endpoint மற்றும் மாடலை அமைக்கவும்.
`MINIMAX_MODEL_ID` `MiniMax-M3` மற்றும் `MiniMax-M2.7` களை ஆதரிக்கிறது. 
`OPENAI_BASE_URL` அமைக்கப்படவில்லை என்றால், `MINIMAX_REGION` `global_en` மற்றும் `cn_zh` ஆகியவற்றை ஆதரிக்கிறது.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

பகுதி சராசரியைத் தேர்ந்தெடுக்க `OPENAI_BASE_URL` ஐ தவிர்க்கவும்:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

பிறகு உங்கள் ஜாவா கிளையண்ட் வகுப்பை உருவாக்கவும்:

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

        // சர்வருடன் இணைக்கும் MCP மாற்றுகை உருவாக்கவும்
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP கிளையன்ட் உருவாக்கவும்
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

மேலே உள்ள குறியீட்டில் நாங்கள்:

- **LangChain4j சார்புகளைச் சேர்த்துள்ளோம்**: MCP ஒருங்கிணைப்பிற்கும் OpenAI இணக்கமான MiniMax API க்கும்
- **LangChain4j நூலகங்களை இறக்குமதி செய்துள்ளோம்**: MCP ஒருங்கிணைப்புக்கும் OpenAI பேசும் மாடல் செயல்பாட்டிற்கும்
- **ChatLanguageModel உருவாக்கினோம்**: உங்கள் MiniMax API விசை, endpoint மற்றும் ஆதரிக்கப்படும் மாடல் ஐடியுடன் MiniMax பயன்படுத்த அமைக்கப்பட்டது
- **HTTP போக்குவரத்தை அமைத்துள்ளோம்**: Server-Sent Events (SSE) பயன்படுத்தி MCP சேவையகத்துடன் சேர்க்க
- **MCP கிளையண்ட் உருவாக்கப்பட்டது**: சேவையகத்துடன் தொடர்பை கையாளும்
- **LangChain4j இன் உள்ளமைந்த MCP ஆதரவை பயன்படுத்தினோம்**: இது LLM களுக்கும் MCP சேவையகங்களுக்கும் இடையே ஒருங்கிணைப்பை எளிதாக்குகிறது

#### Rust

இந்த எடுத்துக்காட்டு Rust அடிப்படையிலான MCP சேவையகம் இயங்குவதாக கருதுகிறது. இல்லையெனில், [01-first-server](../01-first-server/README.md) பாடத்திற்குச் செல்லவும்.

உங்கள் Rust MCP சேவையகத்தைப் பெற்றுவிட்டதும், டெர்மினல் திறந்து அதே அடைவுக்கு செல்லவும். பின்வரும் கட்டளையை இயக்கி புதிய LLM கிளையண்ட் திட்டம் உருவாக்கவும்:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

உங்கள் `Cargo.toml` கோப்பில் பின்வரும் சார்புகளைச் சேர்க்கவும்:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAIக்கான அதிகாரபூர்வ Rust நூலகம் இல்லை, ஆனால் `async-openai` விளக்கம் [சமூக பராமரிப்பில் இருக்கும் நூலகம்](https://platform.openai.com/docs/libraries/rust#rust) ஆகும்.

`src/main.rs` கோப்பைத் திறந்து அதில் உள்ளடக்கம் பின்வரும் குறியீடு ஆக மாற்றவும்:

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
    // ஆரம்ப உரை
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI கிளையண்ட் அமைக்கவும்
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP கிளையண்ட் அமைக்கவும்
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

    // செய்ய வேண்டியது: MCP கருவி பட்டியலைப் பெறவும்

    // செய்ய வேண்டியது: கருவி அழைப்புகளுடன் LLM உரையாடல்

    Ok(())
}
```

இந்த குறியீடு ஒரு அடிப்படை Rust செயலியை அமைக்கிறது, இது MCP சேவையகம் மற்றும் GitHub Models உடன் LLM தொடர்புக்கு இணைக்கும்.

> [!IMPORTANT]
> செயலியை இயக்குவதற்கு முன் உங்கள் GitHub குறியீட்டுடன் `OPENAI_API_KEY` சூழல் மாறியை அமைக்கவும்.

நன்றாக உள்ளது, அடுத்த படியாக சேவையகத்திலுள்ள திறன்களை பட்டியலிடுவோம்.

### -2- சேவையக திறன்களை பட்டியலிடுதல்

இப்போது நாம் சேவையகத்துடன் இணைந்து அதன் திறன்களை கேட்கிறோம்:

#### Typescript

அதே வகுப்பில் பின்வரும் முறைகளைச் சேர்க்கவும்:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // கருவிகள் பட்டியலிடல்
    const toolsResult = await this.client.listTools();
}
```

மேலே உள்ள குறியீட்டில் நாங்கள்:

- சேவையகத்துடன் இணைவதற்கான குறியீடு `connectToServer` சேர்த்துள்ளோம்.
- `run` முறையை உருவாக்கியும் அது தற்போதைக்கு கருவிகளின் பட்டியலை மட்டுமே செய்கிறது; விரைவில் அதனை மேம்படுத்தவுள்ளோம்.

#### Python

```python
# கிடைக்கும் வளங்களை பட்டியலிடவும்
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# கிடைக்கும் கருவிகள் பட்டியலிடவும்
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

நாம் சேர்த்தவை:

- வளங்களையும் கருவிகளையும் பட்டியலிட்டு அச்சிடுகிறது. கருவிகளுக்கான `inputSchema`-யையும் பட்டியலிடும், இதை பின்னர் பயன்படுத்துகிறோம்.

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

மேலே உள்ள குறியீட்டில் நாங்கள்:

- MCP சேவையகத்தில் உள்ள கருவிகளை பட்டியலிட்டோம்
- ஒவ்வொரு கருவிக்கும் பெயர், விளக்கம் மற்றும் அதன் சிக்கலான அமைப்பையும் பட்டியலிட்டோம். இதைச் சிறிது நேரத்தில் பயன்படுத்தப் போகிறோம்.

#### Java

```java
// MCP கருவிகளை தானாக கண்டுபிடிக்கும் ஒரு கருவி வழங்கியரை உருவாக செய்க
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP கருவி வழங்கியர் தானாக கையாள்கிறது:
// - MCP சேவையகத்திலிருந்து கிடைக்கும் கருவிகளை பட்டியலிடுதல்
// - MCP கருவி சிக்கல்களை LangChain4j வடிவத்தில் மாற்றுதல்
// - கருவி செயல்பாடு மற்றும் பதில்களை நிர்வகித்தல்
```

மேலே உள்ள குறியீட்டில் நாங்கள்:

- MCP சேவையகத்திலிருந்து அனைத்து கருவிகளையும் தானாக கண்டறிந்து பதிவு செய்யும் `McpToolProvider` உருவாக்கினோம்
- கருவி வழங்குநர் MCP கருவி சிக்கலான அமைப்புகளை LangChain4j கருவி வடிவத்துக்கு உட்புறமாக மாற்றுகிறது
- இது கருவிகளைத் பட்டியலிடுதல் மற்றும் மாற்றும் பணிகளை கைமுறை செய்வதைத் தவிர்க்கின்றது

#### Rust

MCP சேவையகத்திலிருந்து கருவிகளை `list_tools` முறை மூலம் பெறலாம். உங்கள் `main` செயலியில் MCP கிளையண்டை அமைத்த பிறகு பின்வரும் குறியீட்டைச் சேர்க்கவும்:

```rust
// MCP கருவி பட்டியலைப் பெறுக
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- சேவையக திறன்களை LLM கருவிகளாக மாற்றுதல்

சேவையக திறன்களை பட்டியலிட்ட பிறகு அடுத்த படி அவற்றைப் LLM புரிந்துகொள்ளும் வடிவத்திற்கு மாற்றுதல். இதனால் நாம் LLM க்கு கருவிகள் என வழங்க முடியும்.

#### TypeScript

1. MCP சேவையகத்திலிருந்து பெறப்பட்ட பதிலை LLM பயன்படுத்தக்கூடிய கருவி வடிவத்திற்கு மாற்ற பின்வருமாறு குறியீடு சேர்க்கவும்:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // உள்ளீட்டு_schema அடிப்படையில் ஒரு zod சேமா உருவாக்கவும்
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // வகையை "function" ஆக தெளிவாக அமைக்கவும்
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

    மேலே கூறிய குறியீடு MCP சேவையகத்திலிருந்து பதிலை எடுத்து அதை LLM பாவிக்கும் கருவி வரையறை வடிவத்திற்கு மாற்றுகிறது.

2. அடுத்தது `run` முறையை புதுப்பித்து சேவையக திறன்களை பட்டியலிடுவோம்:

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

    மேலே உள்ள குறியீட்டில், நாங்கள் `run` முறையை புதுப்பித்து முடிவை வரைபடமாக மாற்றி ஒவ்வொரு மதிப்பையும் `openAiToolAdapter`க்கு அழைக்கின்றோம்.

#### Python

1. முதலில் பின்வரும் மாற்றுநிலை செயல்பாட்டை உருவாக்குங்கள்

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

    மேலே உள்ள `convert_to_llm_tools` செயல்பாட்டில் MCP கருவி பதிலை எடுத்து அதை LLM புரிந்து கொள்ளக்கூடிய வடிவமாக மாற்றுகிறோம்.

2. பிறகு, எங்கள் கிளையண்ட் குறியீட்டில் இதை பயன்படுத்திட்டு புதுப்பிப்போம்:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    இங்கு, MCP கருவி பதிலை LLM க்கு வழங்குவதற்காக `convert_to_llm_tool` அழைப்பு சேர்க்கப்பட்டுள்ளது.

#### .NET

1. MCP கருவி பதிலை LLM புரிந்து கொள்ளக்கூடிய வடிவிற்கு மாற்ற பின்வருமாறு குறியீடு சேர்க்கவும்

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

மேலே உள்ள குறியீட்டில் நாங்கள்:

- பெயர், விளக்கம் மற்றும் உள்ளீட்டு சிக்கலான அமைப்புகளை எடுத்துக் கொண்டு `ConvertFrom` செயல்பாட்டை உருவாக்கினோம்.
- இந்த செயல்பாடு ஒரு FunctionDefinition உருவாக்கி அதை ChatCompletionsDefinition க்கு வழங்குகிறது. இது LLM புரிந்துகொள்ளும் வடிவாகும்.

2. மேலே உள்ள செயல்பாட்டைப் பயன்படுத்தி இருப்பை புதுப்பிப்பது எப்படி என்பதைக் காண்போம்:

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
// இயல்பான மொழி தொடர்புக்கான ஒரு பாட்டை உருவாக்கவும்
public interface Bot {
    String chat(String prompt);
}

// LLM மற்றும் MCP கருவிகளுடன் AI சேவையை அமைக்கவும்
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

மேலே உள்ள குறியீட்டில் நாங்கள்:

- இயல்பான மொழி ஊக்க ஊட்டிகளுக்கான எளிய `Bot` இடைமுகத்தை வரையறுத்துள்ளோம்
- LangChain4j இன் `AiServices` ஐ பயன்படுத்தி LLM ஐ MCP கருவி வழங்குநருடன் தானாக இணைத்துள்ளோம்
- பின்னணி செயல்பாட்டில் கருவி சிக்கலான அமைப்பு மாற்றம் மற்றும் செயல்பாட்டை அழைக்கும் பணிகளை தானாக கையாள்கிறது
- இதன் மூலம் MCP கருவிகளை LLM பொருந்தக்கூடிய வடிவத்திற்கு மாற்றும் அசராத செயல்பாட்டை LangChain4j கவனிக்கிறது

#### Rust

MCP கருவி பதிலை LLM புரிந்துகொள்ளும் வடிவத்திற்கு மாற்ற, கருவி பட்டியலை வடிவமைக்கும் உதவி செயல்பாட்டை சேர்க்கிறோம். `main` செயலிக்கு கீழே பின்வரும் குறியீட்டை `main.rs` கோப்பில் சேர்க்கவும். இது LLMக்கு கோரிக்கை செய்யும் போது அழைக்கப்படும்:

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

நன்றாக உள்ளது, உங்கள் பயனர் கோரிக்கைகளை கையாள தயாராக இல்லை, அடுத்ததைக் கையாள்வோம்.

### -4- பயனர் ஊக்க ஊட்டிக்கான கோரிக்கையை கையாள்தல்

இப் பகுதியின் குறியீட்டில் பயனர் கோரிக்கைகளை கையாள்வோம்.

#### TypeScript

1. எங்கள் LLM ஐ அழைக்க பயன்படுத்தப்படும் ஒரு செயற்துறையைச் சேர்க்கவும்:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. சேவையகத்தின் கருவியை அழைக்கவும்
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. முடிவுடன் ஒன்றைச் செய்யவும்
        // செய்யவேண்டியது

        }
    }
    ```

மேலே உள்ள குறியீட்டில் நாங்கள்:

- `callTools` என்ற செயல்பாட்டைச் சேர்த்துள்ளோம்.
- இந்த செயற்துறை LLM பதிலை எடுத்துப் அதில் எந்த கருவிகள் அழைக்கப்பட்டுள்ளன என்பதை சரிபார்க்கிறது, இருந்தால்:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // கருவியை அழைப்பு
        }
        ```

- LLM கருவிகளை அழைக்குமென குறிப்பிட்டால் அந்த கருவியை அழைக்கிறது:

        ```typescript
        // 2. சர்வரின் கருவியை அழைக்கவும்
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. முடிவுடன் ஏதாவது செய்
        // செய்ய வேண்டியது
        ```

2. `run` முறையில் LLM அழைக்கப்படுவதையும் `callTools` ஐ அழைக்கும் வகையில் புதுப்பிக்கவும்:

    ```typescript

    // 1. LLM இற்கான உள்ளீட்டாக இருக்கும் செய்திகளை உருவாக்கவும்
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ஐ கால் செய்யிறது
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM பதிலை கொண்டு ஒவ்வொரு தேர்வையும் பார்வையிடுக, அது டூல் கால் உள்ளதா என்று சரிபார்க்கவும்
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

நன்றாக உள்ளது, முழு குறியீட்டை பட்டியலிடுவோம்:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // வடிவமைப்புக் 검증த்திற்கு zod ஐ இறக்குமதி செய்க

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // எதிர்காலத்தில் இந்த URL ஐ மாற்ற வேண்டியிருக்கலாம்: https://models.github.ai/inference
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
          // உள்ளீட்டு_schema அடிப்படையில் zod வடிவமைப்பை உருவாக்குக
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // வகையை தெளிவாக "function" ஆக அமைக்கவும்
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
    
    
          // 2. சர்வர் கருவியை அழைக்கவும்
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. முடிவுடன் ஏதாவது செய்க
          // செய்யவேண்டியது
    
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
    
        // 3. LLM பதிலை ஒவ்வொரு தேர்விற்கும் மூலம் செல்லவும், அது கருவி அழைப்புகளை கொண்டுள்ளதா என்று சரிபார்க்கவும்
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

1. LLM அழைக்க தேவையான இறக்குமதிகளைச் சேர்க்கவும்

    ```python
    # எல்எல்எம்
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. பிறகு, LLM அழைக்கும் செயல்பாட்டைச் சேர்க்கவும்:

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
            # தேர்வுசெய்யப்பட்ட அளவுகோல்கள்
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

மேலே கூறிய குறியீட்டில் நாங்கள்:

- MCP சேவையகத்தில் கண்டுபிடிக்கப்பட்ட மற்றும் மாற்றப்பட்ட செயல்பாடுகளை LLM க்கு அனுப்பினோம்.
- பிறகு அது செயல்பாடுகளுடன் LLMஐ அழைத்தோம்.
- முடிவில் எந்த செயல்பாடுகளை அழைக்க வேண்டும் என்று பார்க்கிறோம்.
- இறுதியில் அழைக்க வேண்டிய செயல்பாடுகளின் வரிசையை வழங்குகிறோம்.

3. கடைசிச் படி, எங்கள் முதன்மை குறியீட்டை புதுப்பிப்போம்:

    ```python
    prompt = "Add 2 to 20"

    # எல்.எல்.எம்.யிடம் எந்த கருவிகள் இருந்தால் அனைத்து, கேளுங்கள்
    functions_to_call = call_llm(prompt, functions)

    # பரிந்துரைக்கப்பட்ட செயல்பாடுகளை அழைக்கவும்
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

மேலே உள்ள குறியீட்டில் நாங்கள்:

- LLM ஊக்க ஊட்டியால் பரிந்துரைக்கப்பட்ட செயல்பாட்டை கொண்டு `call_tool` மூலம் MCP கருவியை அழைக்கிறோம்.
- உலா MCP சேவையக கருவி அழைப்பு முடிவை அச்சிடுகிறோம்.

#### .NET

1. LLM ஊக்க ஊட்டிக்கான கோரிக்கை குறியீடு:

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

மேலே உள்ள குறியீட்டில் நாங்கள்:

- MCP சேவையகத்திலிருந்து கருவிகளை பெற்று (`var tools = await GetMcpTools()`)
- பயனர் ஊக்க ஊட்டியைக் குறிப்பிடி’ userMessage’.
- மாடல் மற்றும் கருவி தேர்ந்தெடுக்கும் தேர்வுகள் கொண்ட பொருளை உருவாக்கி,
- LLM க்குக் கோரிக்கை செய்தோம்.

2. கடைசி படி, LLM செயல்பாட்டை அழைக்கவேண்டுமா என்பதை பார்க்கலாம்:

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

மேலே உள்ள குறியீட்டில் நாங்கள்:

- செயல்பாட்டுக் கோரிக்கைகளின் பட்டியலில் உலா சுற்றி,
- ஒவ்வொரு கருவி அழைப்புக்கும் பெயர் மற்றும் அளவுருக்கள் பிரித்து MCP கிளையண்ட் மூலம் கருவியை செயல்படுத்தி முடிவுகளை அச்சிடுகிறோம்.

முழு குறியீடு:

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
    // MCP கருவிகளை தானாக பயன்படுத்தும் இயற்கை மொழி கோரிக்கைகளை இயக்கு
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

மேலே உள்ள குறியீட்டில் நாங்கள்:

- MCP சேவையக கருவிகளுடன் எளிய இயற்கை மொழி ஊக்க ஊட்டிகளை பயன்படுத்தி தொடர்பு கொண்டோம்
- LangChain4j கட்டமைப்பு தானாக கையாள்கிறது:
  - தேவையான போது பயனர் ஊக்க ஊட்டிகளை கருவி அழைப்புகளாக மாற்றுதல்
  - LLM முடிவின் அடிப்படையில் சரியான MCP கருவிகளை அழைத்தல்
  - LLM மற்றும் MCP சேவையகத்திற்கிடையேயான உரையாடல் காவல்துறையின் மேலாண்மை
- `bot.chat()` முறையானது இயற்கை மொழி பதில்களை வழங்குகிறது, அதில் MCP கருவி இயக்க முடிவுகளும் இருக்கக்கூடும்
- இந்த அணுகுமுறை பயனர்களுக்கு MCP அடிப்படை செயல்பாட்டை அறியத் தேவையில்லாமல் மென்மையான அனுபவத்தை வழங்குகிறது

முழுமையான குறியீடு எடுத்துக்காட்டு:

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


இங்கே பெரும்பாலும் பணிகள் நடைபெறும். முதலில், பயனர் தொடக்கச் செய்தியுடன் LLM ஐ அழைப்போம், பிறகு எந்த உபகரணங்களை அழைக்க வேண்டுமா என்று பதிலை معالجة செய்வோம். அவ்வாறெனில் அந்த உபகரணங்களை அழைத்து, மேலும் உபகரண அழைப்புகள் தேவையில்லாத வரை LLM உடன் உரையாடலை தொடர்வோம் மற்றும் இறுதி பதிலை பெறுவோம்.

நாம் LLM ஐ பலமுறை அழைக்கும் என்பதால், LLM அழைப்பை கையாளும் ஒரு செயல்பாட்டை வரையறுக்கலாம். கீழ்காணும் செயல்பாட்டை உங்கள் `main.rs` கோப்பில் சேர்க்கவும்:

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

இந்த செயல்பாடு LLM கிளையன்ட், செய்திகளின் பட்டியல் (பயனர் தொடக்கச் செய்தி உட்பட), MCP சர்வரிலிருந்து உபகரணங்கள் எடுத்துக்கொண்டும் LLM க்கு கோரிக்கையை அனுப்பி பதிலை வழங்கும்.

LLM இல் இருந்து வந்த பதில் `choices` என்ற வரிசையை கொண்டிருக்கும். எந்த `tool_calls` உள்ளதா என்று 결과를 பாா்வையிட வேண்டும். இதனால் LLM ஒரு குறிப்பிட்ட உபகரணத்தை அழைக்க வேண்டும் என்று கேட்கிறது என்று தெரிகிறது. உங்கள் `main.rs` கோப்பின் அடியில் கீழ்கண்ட குறியீட்டை சேர்த்து LLM பதிலை கையாளும் செயல்பாட்டை வரையறுக்கவும்:

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

    // உள்ளடக்கம் கிடைக்கும் என்றால் அச்சிடுக
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // கருவி அழைப்புக்களை கையாளுக
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // உதவியாளர் செய்தியை சேர்க்கவும்

        // ஒவ்வொரு கருவி அழப்பையும் இயக்குக
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // கருவி முடிவுகளை செய்திகளுக்கு சேர்க்கவும்
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // கருவி முடிவுகளுடன் உரையாடலை தொடர்க
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

`tool_calls` இருந்தால், அது உபகரண தகவலை எடுத்துக்கொள்கிறது, MCP சர்வரை உபகரண கோரிக்கையுடன் அழைக்கிறது, மற்றும் அதன் முடிவுகளை உரையாடல் செய்திகளுடன் இணைக்கிறது. பின்னர் LLM உடன் உரையாடலை தொடருகிறது மற்றும் செய்திகள் உதவியாளர் பதில் மற்றும் உபகரண அழைப்பு முடிவுகளுடன் புதுப்பிக்கப்படும்.

LLM MCP அழைப்புகளுக்காக திரும்பத் தரும் உபகரண அழைப்பு தகவலை எடுக்க, அனேகமான உதவி செயல்பாடு ஒன்றைச் சேர்த்துக்கொள்வோம். உங்கள் `main.rs` கோப்பின் அடியில் கீழ்கண்ட குறியீட்டை சேர்க்கவும்:

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

அனைத்து பகுதிகளும் இருக்கும்போது, ஆரம்ப பயனர் தொடக்கச் செய்தியைக் கையாள்ந்து LLM ஐ அழைக்கலாம். உங்கள் `main` செயல்பாட்டை கீழ்கண்ட குறியீட்டுடன் புதுப்பிக்கவும்:

```rust
// கருவி அழைப்புகளுடன் LLM உரையாடல்
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

இது இரண்டு எண்களின் கூட்டுத்தொகையைக் கேட்டு LLM ஐ விசாரிக்கும், மற்றும் உரையாடல் உபகரண அழைப்புகளை இயற்கையாக கையாளும்.

சிறந்தது, நீங்கள் செய்துவிட்டீர்கள்!

## பணிகள்

நடைமுறையில் உள்ள குறியீட்டை எடுத்துக்கொண்டு சர்வரை மேலும் சில உபகரணங்களுடன் உருவாக்கவும். பிறகு ஒரு LLM உடைய கிளையண்டை உருவாக்கி, வேறு வேறு தொடக்கச் செய்திகளுடன் சோதனை செய்து உங்கள் சர்வர் உபகரணங்கள் அனைத்தும் இயல்பாக அழைக்கப்படுகிறதா என்று உறுதிப்படுத்தவும். இந்த முறையில் கிளையண்ட் கட்டுமானம் போதுமான பெறுநர் திருப்புமுனைகளுடன் கூடிய சிறந்த பயனர் அனுபவத்தை வழங்கும் என்பது, பயனர் குறிப்பிட்ட கிளையண்ட் கட்டளைகளைப் பொருட்படுத்தாமல், பரிமாற்றங்களை பயன்படுத்தி  MCP சர்வர் அழைக்கப்படுவதை அறியாமலே செயல்படலாம்.

## தீர்வு

[தீர்வு](./solution/README.md)

## முக்கியக் குறிப்புகள்

- உங்கள் கிளையண்டில் LLM சேர்த்தல் MCP சர்வர்களுடன் தொடர்பு கொள்ளும் சிறந்த வழி.
- MCP சர்வர் பதிலை LLM புரிந்துகொள்ளக்கூடிய வடிவமாக மாற்ற வேண்டும்.

## மாதிரிகள்

- [Java கல்குலேட்டர்](../samples/java/calculator/README.md)
- [.Net கல்குலேட்டர்](../../../../03-GettingStarted/samples/csharp)
- [JavaScript கல்குலேட்டர்](../samples/javascript/README.md)
- [TypeScript கல்குலேட்டர்](../samples/typescript/README.md)
- [Python கல்குலேட்டர்](../../../../03-GettingStarted/samples/python)
- [Rust கல்குலேட்டர்](../../../../03-GettingStarted/samples/rust)

## கூடுதல் வளங்கள்

## அடுத்து என்ன

- அடுத்து: [Visual Studio Code பயன்படுத்தி சர்வரை பயன்படுத்துதல்](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->