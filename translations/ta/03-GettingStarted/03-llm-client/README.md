# LLM உடன் ஒரு கிளையண்ட் உருவாக்குதல்

இதுவரை, நீங்கள் ஒரு சார்வர் மற்றும் ஒரு கிளையண்ட் உருவாக்குவது எப்படி என்பதை நோக்கியுள்ளீர்கள். கிளையண்ட் சார்வரின் கருவிகள், வளங்கள் மற்றும் உந்துதல்களை பட்டியலிட சர்வரை நேரடியாக அழைக்க முடிந்தது. எனினும், இது மிகவும் நடைமுறைமிக்க அணுகுமுறை அல்ல. உங்கள் பயனர்கள் முகவரிய যুগத்தில் வாழ்வதால், அவர்கள் உந்துதல்கள் மற்றும் ஒரு LLM உடன் தொடர்பு கொள்வதை எதிர்பார்க்கின்றனர். அவர்கள் MCP தங்களது திறன்களை சேமிக்கவில்லை என்பதை கவலையில்லை; அவர்கள் இயற்கை மொழியைப் பயன்படுத்தி தொடர்பு கொள்ள எதிர்பார்க்கின்றனர். எனவே நாம் இதை எப்படி தீர்க்கப்போகிறோம்? தீர்வு என்பது கிளையண்டில் ஒரு LLM நுழைக்க வேண்டும்.

## கண்ணோட்டம்

இந்த பாடத்தில், உங்கள் கிளையண்டில் ஒரு LLM சேர்க்கும் முறையில் கவனம் செலுத்துகிறோம் மற்றும் இது உங்கள் பயனருக்கு அதிக தரமான அனுபவத்தை எப்படி வழங்குகிறது என்பதை காண்பிப்போம்.

## கற்றல் குறிக்கோள்கள்

இந்த பாடம் முடிந்தவுடன், நீங்கள் செயல்படுத்த முடியும்:

- LLM உடன் ஒரு கிளையண்டை உருவாக்குதல்.
- LLM பயன்படுத்தி MCP சர்வருடன் இடையிலான முறையான தொடர்பு.
- கிளையண்ட் பக்கத்தில் ஒரு சிறந்த பயனர் அனுபவத்தை வழங்குதல்.

## அணுகுமுறை

நாம் ஏற்கனவே எவ்வாறு செய்யவேண்டும் என்பதை புரிந்துகொள்வோம். LLM சேர்ப்பது எளிதானதாக தோன்றினாலும், அதை நம்மால் எப்படி செய்வது என்பதை பார்க்கலாம்.

கிளையண்ட் சர்வருடன் எப்படி தொடர்பு கொள்கிறது என்பதை இங்கே பார்க்கலாம்:

1. சர்வருடன் இணைப்பை ஏற்படுத்துக.

1. திறன்கள், உந்துதல்கள், வளங்கள் மற்றும் கருவிகளை பட்டியலிடுக மற்றும் அவற்றின் ஸ்கீமாவை சேமிக்கவும்.

1. ஒரு LLM ஐ சேர்த்து சேமிக்கப்பட்ட திறன்கள் மற்றும் அவற்றின் ஸ்கீமாவை LLM புரிந்துக் கொள்ளும் வடிவத்தில் வழங்கவும்.

1. பயனர் உந்துதலை LLM க்கு கிளையண்ட் பட்டியலிட்ட கருவிகளுடன் ஒன்றாக அனுப்பி கையாளவும்.

அருமை, இதனால் நாம் மேல் நிலை அணுகுமுறையைப் புரிந்துகொண்டோம், கீழே உள்ள பயிற்சியில் இதை முயற்சிப்போம்.

## பயிற்சி: LLM உடன் ஒரு கிளையண்ட் உருவாக்குதல்

இந்த பயிற்சியில், நாமும் எவ்வாறு ஒரு LLM ஐ நமது கிளையண்டில் சேர்ப்பது என்பதை கற்றுக்கொள்வோம்.

### GitHub தனிப்பட்ட அணுகல் குறியீடு மூலம் அங்கீகரித்தல்

ஒரு GitHub குறியீட்டை உருவாக்குவது மிக எளிதான செயல்முறை. இதைப் பின்வருபவை போல செய்யலாம்:

- GitHub அமைப்புக்கு செல்லவும் – மேலே வலது மூலையில் உங்கள் சுயவிவரப்படத்தை கிளிக் செய்து அமைப்புகளைத் தேர்வுசெய்க.
- டெவலப்பர் அமைப்புகள் – கீழே இறங்கி Developer Settings ஐ கிளிக் செய்யவும்.
- தனிப்பட்ட அணுகல் குறியீடுகள் – Fine-grained tokens ஐ தேர்வு செய்து புதிய குறியீடு உருவாக்கவும்.
- உங்கள் குறியீட்டை அமைக்கவும் – குறிப்பைச் சேர்க்கவும், காலாவதியான தேதியைக் குறிப்பிடவும், மற்றும் தேவையான அனுமதிகளைத் தேர்ந்தெடுக்கவும். இந்த வழியில் Models அனுமதியைவும் சேர்க்க வேண்டும்.
- குறியீடு உருவாக்கி நகலெடுக்கவும் – Generate token ஐ கிளிக் செய்து உடனடியாக நகலெடுக்கவும், மீண்டும் பார்க்க முடியாது.

### -1- சர்வருடன் இணைக்கவும்

முதலில் நம் கிளையண்டை உருவாக்குவோம்:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ஸ்கீமா சரிபார்ப்புக்கு zod ஐ இறக்குமதி செய்க

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
- `client` மற்றும் `openai` என்ற இரண்டு உறுப்பினர்களுடன் ஒரு வகுப்பு உருவாக்கி, கிளையண்டையும் LLM உடன் தொடர்புகொள்ள தீர்வு பெற்றுள்ளோம்.
- GitHub Models ஐ பயன்படுத்த LLMஎன்ஸ்டன்ஸ் அமைத்து, `baseUrl` ஐ inference API க்குச் சொந்தமாக மாற்றினோம்.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio இணைப்புக்கு சேவையகம் параметрிகளை உருவாக்கவும்
server_params = StdioServerParameters(
    command="mcp",  # இயங்கக்கூடிய
    args=["run", "server.py"],  # விருப்பமான கட்டளை வரி வாதங்கள்
    env=None,  # விருப்பமான சூழல் மாறிகள்
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # இணைப்பை துவக்கவும்
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

மேலே உள்ள குறியீட்டில் நாங்கள்:

- MCP புகுபதிகைக்கான நூலகங்களை இறக்குமதி செய்துள்ளோம்
- ஒரு கிளையண்டை உருவாக்கினோம்

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

முதலில், `pom.xml` கோப்புக்குள் LangChain4j சார்புகளைச் சேர்க்க வேண்டும். MCP ஒருங்கிணைப்பு மற்றும் OpenAI பொருந்தும் MiniMax APIஐ இயக்க இவை தேவையாக உள்ளன:

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

MiniMax API விசையை மற்றும் விருப்பமாய் முனையம் மற்றும் மாதிரியை அமைக்கவும்.
`MINIMAX_MODEL_ID` `MiniMax-M3` மற்றும் `MiniMax-M2.7` ஐ ஆதரிக்கிறது. 
`OPENAI_BASE_URL` அமைக்கப்படாவிட்டால், `MINIMAX_REGION` `global_en` மற்றும் `cn_zh` ஐ ஆதரிக்கிறது.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

மண்டலத்தின் அடிப்படையில் முனையம் தேர்வு செய்ய `OPENAI_BASE_URL` நீக்கவும்:

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

        // சேவையகத்தை இணைக்க MCP போக்குவரத்தை உருவாக்கவும்
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP கிளையண்டை உருவாக்கவும்
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

- **LangChain4j சார்புகளைச் சேர்த்தோம்**: MCP ஒருங்கிணைப்பு மற்றும் OpenAI பொருந்தும் MiniMax APIக்காக தேவை.
- **LangChain4j நூலகங்களை இறக்குமதி செய்தோம்**: MCP ஒருங்கிணைப்பு மற்றும் OpenAI உரையாடல் மாதிரி செயல்பாட்டுக்காக.
- **`ChatLanguageModel` உருவாக்கப்பட்டது**: MiniMax மற்றும் உங்கள் MiniMax API விசையுடன், முனையம் மற்றும் ஆதரிக்கப்பட்ட மாதிரி IDயுடன் உள்ளமைவு செய்யப்பட்டது.
- **HTTP போக்குவரத்து அமைப்பு**: MCP சர்வருடன் சேர சர்்வர் அனுப்பும் நிகழ்வுகள் (SSE) பயன்படுத்தப்பட்டது.
- **MCP கிளையண்ட் உருவாக்கப்பட்டது**: சர்வருடன் தொடர்பு கையாள.
- **LangChain4j இன் அடிப்படை MCP ஆதரவு பயன்படுத்தப்பட்டது**: இது LLM மற்றும் MCP சர்வர்களுக்கு இடையிலான ஒருங்கிணைப்பை எளிமைப்படுத்தும்.

#### Rust

இந்த உதாரணம் ஒரு Rust அடிப்படையிலான MCP சர்வர் இயங்குவதாக கருதுகிறது. இல்லையெனில், [01-first-server](../01-first-server/README.md) பாடத்தைப் பாருங்கள் சர்வர் உருவாக்க.

உங்களுக்கு Rust MCP சர்வர் இருந்தால், ஒரு டெர்மினல் திறந்து சர்வர் கோப்பகத்திற்கு செல்லவும். பிறகு கீழ்காணும் கட்டளையை ஓட்டி ஒரு புதிய LLM கிளையண்ட் திட்டத்தை உருவாக்கவும்:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` கோப்பில் பின்வரும் சார்புகளைச் சேர்க்கவும்:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAIக்கான அதிகாரபூர்வ Rust நூலகம் இல்லை, இருப்பினும், `async-openai` கூடை ஒரு [சமூக பராமரிப்பு நூலகமாக](https://platform.openai.com/docs/libraries/rust#rust) பொதுவாக பயன்படுத்தப்படுகிறது.

`src/main.rs` கோப்பை திறந்து அதை கீழ்க்காணும் குறியீட்டால் மாற்றவும்:

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
    // ஆரம்ப செய்தி
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI கிளையன்ட் அமைக்கவும்
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP கிளையன்ட் அமைக்கவும்
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

    // செய்ய வேண்டியது: MCP கருவி பட்டியலைப் பெறுக

    // செய்ய வேண்டியது: கருவி அழைப்புகளுடன் LLM உரையாடல்

    Ok(())
}
```

இந்த குறியீடு ஒரு அடிப்படையான Rust செயலியை ஏற்படுத்துகிறது, இது MCP சர்வருக்கும் GitHub Models க்கும் கானெக்ஷன் செய்ய பயன்படும்.

> [!IMPORTANT]
> செயலியை இயக்கும் முன் உங்கள் GitHub குறியீட்டை `OPENAI_API_KEY` சுற்றுச்சூழல் மாறியில் அமைக்க உறுதி செய்யவும்.

அருமை, அடுத்த கட்டமாக, சர்வரின் திறன்களை பட்டியலிடுவோம்.

### -2- சர்வர் திறன்களை பட்டியலிடுதல்

இப்போது நாம் சர்வருடன் இணைந்து அதன் திறன்களை கேட்கப் போகிறோம்:

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

- சர்வருடன் இணைக்கக் குறியீடு சேர்த்துள்ளோம், `connectToServer`.
- நமது செயலி வேலைப்பாட்டை கையாளும் `run` முறையை உருவாக்கினோம். தற்போது அது கருவிகளை மட்டுமே பட்டியலிடுகிறது என்று, விரைவில் அதனை மேம்படுத்துவோம்.

#### Python

```python
# கிடைக்கும் வளங்களை பட்டியலிடுக
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# கிடைக்கும் கருவிகளை பட்டியலிடுக
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

நாங்கள் என்ன செய்தோம்:

- வளங்கள் மற்றும் கருவிகளை பட்டியலிட்டு, அச்சிடும் செயல்பாட்டைப் பெற்றுள்ளோம். கருவிகளுக்கான `inputSchema` ஐவும் பட்டியலிடுகிறோம்; இதனை பின்னர் பயன்படுத்துவோம்.

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

- MCP சர்வரில் கிடைக்கும் கருவிகளை பட்டியலிட்டோம்
- ஒவ்வொரு கருவிக்கும் பெயர், விளக்கம் மற்றும் அதன் ஸ்கீமாவை பட்டியலிட்டோம். இதனை விரைவில் கருவிகளை அழைக்க பயன்படுத்துவோம்.

#### Java

```java
// MCP கருவிகளை தானாக கண்டுபிடிக்கும் கருவி வழங்குவதை உருவாக்கவும்
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP கருவி வழங்குபவர் தானாக சமாளிக்கிறது:
// - MCP சேவையகத்திலிருந்து கிடைக்கும் கருவிகளை பட்டியலிடுதல்
// - MCP கருவி மாதிரிகளை LangChain4j வடிவத்திற்கு மாற்றுதல்
// - கருவி இயங்குவதையும் பதில்களையும் நிர்வகித்தல்
```

மேலே உள்ள குறியீட்டில் நாங்கள்:


- `McpToolProvider` ஐ உருவாக்கியுள்ளோம், இது MCP சேவையகத்தில் இருந்து அனைத்து கருவிகளையும் தானாக கண்டுபிடித்து பதிவு செய்கிறது
- கருவி வழங்குநர் MCP கருவி படிமங்களை மற்றும் LangChain4j இன் கருவி வடிவமைப்புக்கு இடையிலான மாற்றத்தை உள்ளகமாக கையாள்கிறது
- இந்த அணுகுமுறை மனுவல் கருவி பட்டியலாக்கலும் மாற்றும் செயல்முறையையும் மறைக்கும்

#### ரஸ்ட்

MCP சேவையகத்திலிருந்து கருவிகளை பெற `list_tools`முறை பயன்படுத்தப்படுகிறது. உங்கள் `main` செயல்பாட்டில், MCP கிளையண்ட் அமைக்கும் பிறகு, கீழ்க்கண்ட குறியீட்டை சேர்க்கவும்:

```rust
// MCP கருவி பட்டியலைப் பெறுக
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- சேவையக திறன்களை LLM கருவிகளாக மாற்றுதல்

சேவையக திறன்களை பட்டியலிட்ட பிறகு அடுத்த படி அவற்றை LLM புரிந்துகொள்ளக்கூடிய வடிவத்திற்கு மாற்றுவது. அதன்பிறகு, இந்த திறன்களை நமது LLMக்கு கருவிகளாக வழங்கலாம்.

#### TypeScript

1. MCP சேவையகத்திடமிருந்து வந்த பதிலை LLM பயன்படுத்தக்கூடிய கருவி வடிவமாக மாற்ற கீழ்க்கண்ட குறியீட்டைச் சேர்க்கவும்:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // உள்ளீடு_schema based ஒரு zod ஸ்கீமாவை உருவாக்கவும்
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

    ```

    மேல் கூறிய குறியீடு MCP சேவையகத்திலிருந்து பதிலை எடுத்து அதை LLM புரிந்துகொள்ளக்கூடிய கருவி นิரறႈயியை மாற்றுகிறது.

2. அடுத்து `run` முறைப்பாட்டை மேம்படுத்தி சேவையக திறன்களை பட்டியலிடுவோம்:

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

    மேலதிக குறியீட்டில் நாங்கள் `run` முறைப்பாட்டை மேம்படுத்தி பெறப்பட்ட முடிவில் ஒவ்வொரு நுழைவுக்குமான `openAiToolAdapter` கும் அழைக்கின்றோம்.

#### Python

1. முதலில், கீழ்காணும் மாற்றி செயல்பாட்டை உருவாக்குவோம்

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

    மேலுள்ள `convert_to_llm_tools` செயல்பாட்டில் MCP கருவி பதிலை எடுத்து அதனை LLM புரிந்துகொள்ளக்கூடிய வடிவத்திற்கு மாற்றுகிறோம்.

2. அடுத்து, கீழ்த் தொகுப்பில் இந்த செயல்பாட்டைப் பயன்படுத்தும் வகையில் நமது கிளையண்ட் குறியீட்டை மேம்படுத்துவோம்:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    இங்கு, MCP கருவி பதிலை LLM க்கு நீடித்து வழங்கும் வகையில் `convert_to_llm_tool` அழைப்பை சேர்க்கிறோம்.

#### .NET

1. MCP கருவி பதிலை LLM புரிந்துகொள்ளக்கூடிய வடிவத்திற்கு மாற்றும் குறியீடு சேர்க்கலாம்

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

மேலதிக குறியீட்டில் நாம்:

- பெயர், விளக்கம் மற்றும் உள்ளீட்டு படிமத்தை ஏற்கும் `ConvertFrom` என்ற செயல்பாட்டை உருவாக்கியுள்ளோம்.
- அடுத்து, ஒரு FunctionDefinition உருவாக்கி அதை ChatCompletionsDefinition இற்கு வழங்கும் செயல்பாட்டை வரையறுத்துள்ளோம். இது LLM புரிந்துகொள்ளக்கூடியது.

2. மேலுள்ள செயல்பாட்டைப் பயன்படுத்தி ஏற்கனவே உள்ள குறியீட்டை மேம்படுத்துவோம்:

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

#### ஜாவா

```java
// இயற்கை மொழி தொடர்புக்கான ஒரு பாட்டுக் இடைமுகத்தை உருவாக்கவும்
public interface Bot {
    String chat(String prompt);
}

// LLM மற்றும் MCP கருவிகளுடன் AI சேவையை அமைக்கவும்
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

மேலதிக குறியீட்டில் நாம்:

- இயல்பான மொழி தொடர்புகளுக்கான எளிய `Bot` இடைமுகத்தை வரையறுத்துள்ளோம்
- LangChain4j இன் `AiServices` மூலம் LLM ஐ MCP கருவி வழங்குநருடன் தானாக இணைத்துள்ளோம்
- இந்த கட்டமைப்பு பின்னணியில் கருவி படிம மாற்றமும் செயல்பாட்டை அழைப்பதும் தானாக செய்கிறது
- மனுவல் கருவி மாற்றத்தை நீக்கியுள்ளோம் - MCP கருவிகளை LLM-உரிய வடிவத்திற்கு மாற்றுவதில் LangChain4j அனைத்து சிக்கல்களையும் கையாள்கிறது

#### ரஸ்ட்

MCP கருவி பதிலை LLM புரிந்துகொள்ளக்கூடிய வடிவத்தில் மாற்ற, கருவி பட்டியலை வடிவமைக்கும் உதவிக் செயல்பாட்டை சேர்ப்போம். உங்கள் `main.rs` கோப்பில் `main` செயல்பாட்டுக்குப் பின் கீழ்காணும் குறியீட்டை சேர்க்கவும். இது LLMக்கு கோரிக்கை அனுப்பும் போது அழைக்கப்படும்:

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

சிறந்தது, தற்போது எவ்வித பயனர் கோரிக்கைகளையும் கையாள எதுவும் அமைக்கப்படவில்லை, அடுத்ததாக அதைக் கையாள்வோம்.

### -4- பயனர் கேள்வி கோரிக்கையை கையாளுதல்

குறியீட்டின் இந்த பகுதி பயனர் கேள்வி கோரிக்கைகளை கையாளும்.

#### TypeScript

1. நமது LLM அழைப்புக்கு பயன்படுத்தப்படும் ஒரு முறை சேர்க்கவும்:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. சர்வரின் கருவியை அழைத்துக்கொள்
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. முடிவுடன் ஏதாவது செய்
        // செய்யவேண்டியது

        }
    }
    ```

    மேல்கூறிய குறியீட்டில் நாம்:

    - `callTools` என்ற முறையை சேர்த்துள்ளோம்.
    - இந்த முறை LLM பதிலிலிருந்து எந்த கருவிகள் அழைக்கப்பட்டுள்ளன என்று சோதிக்கிறது, இருந்தால் அவற்றை இயக்குகிறது:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // கருவியை அழைக்கவும்
        }
        ```

    - LLM ஒன்று கருவி ஒருங்கிணைப்பை அழைக்க வேண்டும் எனக் கூறினால் அழைக்கிறார்:

        ```typescript
        // 2. சேவையகத்தின் கருவியை அழைக்கவும்
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. முடிவுடன் ஏதாவது செய்
        // செய்யப்பட வேண்டும்
        ```

2. `run` முறையை புதுப்பித்து LLM அழைப்பும் `callTools` அழைப்பும் சேர்க்கவும்:

    ```typescript

    // 1. LLM இற்கு உள்ளீடாக இருப்பதற்கான செய்திகளை உருவாக்கவும்
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ஐ அழைக்கின்றது
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM பதிலை பரிசீலனை செய்யவும், ஒவ்வொரு தேர்வுக்கும், அதில் கருவி அழைப்புகள் உள்ளதா என்பதைச் சரிபார்க்கவும்
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

சிறந்தது, முழு குறியீட்டை பட்டியலிடுவோம்:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ஸ்கீமா சரிபார்ப்புக்காக zod ஐ இறக்குமதி செய்க

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // எதிர்காலத்தில் இந்த URL ஐ மாற்ற வேண்டியதாயிருக்கும்: https://models.github.ai/inference
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
          // உள்ளீடு_ஸ்கீமாவை அடிப்படையாகக் கொண்டு zod ஸ்கீமா உருவாக்குக
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // வகையை "function" என்றால் தெளிவாக அமைக்கவும்
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
    
    
          // 2. சர்வரின் கருவியை அழைக்கவும்
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. முடிவுடன் எதாவது செய்க
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
    
        // 3. LLM பதிலை வழியாக சென்று, ஒவ்வொரு தேர்வுக்கும் கருவி அழைப்புகள் உள்ளதா என்று പരിശോധிக்கவும்
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

1. LLM அழைப்புக்கு தேவையான சில இறக்குமதிகளை சேர்க்கவும்

    ```python
    # எல்.எல்.எம்
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. அடுத்து, LLM ஐ அழைக்கும் செயல்பாட்டை சேர்க்கவும்:

    ```python
    # எல்எல்எம்

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
            # விருப்பமான அளவுருக்கள்
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

    மேலதிக குறியீட்டில் நாம்:

    - MCP சேவையகத்தில் கண்டுபிடித்த மற்றும் மாற்றிய செயல்பாடுகளை LLMக்கு வழங்கியுள்ளோம்.
    - பின்னர், அந்த செயல்பாடுகளுடன் LLM ஐ அழைத்துள்ளோம்.
    - முடிவுகளை பரிசோதித்துப் பார்த்து எந்த செயல்பாடுகளைப் அழைக்க வேண்டும் என்று கண்டுபிடிக்கிறோம்.
    - இறுதியில், அழைக்க வேண்டிய செயல்பாடுகளின் வரிசையைக் கொடுக்கிறோம்.

3. கடைசி படி, நமது முகக்குறியீட்டை புதுப்பிப்போம்:

    ```python
    prompt = "Add 2 to 20"

    # எல்.எல்.எம்.க்கு எதனால் அல்லது உள்ள எந்த கருவிகள் உள்ளன என்று கேள்
    functions_to_call = call_llm(prompt, functions)

    # பரிந்துரைக்கப்பட்ட செயல்பாடுகளை அழைக்கவும்
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    மேலே கூறிய கடைசி படியில் நாம்:

    - LLM எங்கள் கேள்வி அடிப்படையில் அழைக்க வேண்டும் என நினைத்த MCP கருவியை `call_tool` மூலம் அழைக்கிறோம்.
    - கருவி அழைப்பின் முடிவை MCP சேவையகத்திலிருந்து அச்சிடுகிறோம்.

#### .NET

1. LLM கேள்வி கோரிக்கைக்கு குறியீட்டை காண்பிக்கவும்:

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

    மேலதிக குறியீட்டில் நாம்:

    - MCP சேவையகத்திலிருந்து கருவிகளை எடுத்துள்ளோம், `var tools = await GetMcpTools()`.
    - பயனர் கேள்வி `userMessage` ஐ வரையறுத்துள்ளோம்.
    - மாதிரி மற்றும் கருவிகளை குறிப்பிடும் விருப்ப பொருளை உருவாக்கியுள்ளோம்.
    - LLMக்கு கோரிக்கை செய்துள்ளோம்.

2. கடைசிப் படி, LLM எமது கூறிய செயல்பாடு அழைக்கப்படுகிறது என்று நினைத்தால் பார்ப்போம்:

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

    மேலதிக குறியீட்டில் நாம்:

    - செயல்பாட்டு அழைப்புகளின் பட்டியலை சோதனை செய்துள்ளோம்.
    - ஒவ்வொரு கருவி அழைப்புக்கு பெயர் மற்றும்_ARGUMENTS_ பிரித்து MCP கிளையண்ட் மூலம் MCP சேவையகத்தில் கருவியை அழைத்துள்ளோம். முடிவுகளை அச்சிடுகிறோம்.

முழு குறியீடு இதோ:

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

#### ஜாவா

```java
try {
    // MCP கருவிகளை தானாக பயன்படுத்தி இயல்பான மொழி கோரிக்கைகளை செயல்படுத்தவும்
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

மேலதிக குறியீட்டில் நாம்:

- MCP சேவையக கருவிகளுடன் இயல்பான மொழி கேள்வித் தொடர்புகளை பயன்படுத்தியுள்ளோம்
- LangChain4j கட்டமைப்பு தானாக கையாள்கிறது:
  - தேவையான போது பயனர் கேள்விகளை கருவி அழைப்புகளாக மாற்றுதல்
  - LLM முடிவுகளின்படியான சரியான MCP கருவி அழைப்புகள்
  - LLM மற்றும் MCP சேவையகத்துக்கிடையிலான உரையாடல் ஓட்ட நிர்வகிப்பு
- `bot.chat()` முறை MCP கருவி செயல்பாட்டின் முடிவுகளுடன் இயல்பான மொழி பதில்களை வழங்குகிறது
- இந்த அணுகுமுறை பயனர் ஆதாரத்தை மறைத்து ஊக்குவிக்க கூடிய விஷயங்களைக் கொண்டது

முழு குறியீட்டு உதாரணம்:

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

#### ரஸ்ட்

இங்கே பெரும்பாலும் வேலை நடைபெறும். நாங்கள் ஆரம்ப பயனர் கேள்வியை LLMக்கு அழைப்போம், பின்னர் பதிலை விசாரித்து எந்த கருவிகள் அழைக்கப்பட வேண்டுமோ பார்வையிடுவோம். அவற்றின் அடுத்து அவற்றைப் பின்பற்றுவோம் மற்றும் LLM உடன் உரையாடலை தொடர்வோம், மேலும் கருவி அழைப்புகள் தேவை இல்லாத வரை தொடர்ந்தே இருப்போம்.


நாம் LLM-க்கு பல அழைப்புகளைச் செய்வோம், ஆகவே LLM அழைப்பை கையாளும் ஒரு செயல்பாட்டை வரையறுக்கலாம். உங்கள் `main.rs` கோப்பில் பின்வரும் செயல்பாட்டைப் சேர்க்கவும்:

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

இந்த செயல்பாடு LLM கிளையண்ட், செய்திகளின் பட்டியல் (பயனர் கேள்வியுடன் சேர்ந்து), MCP சர்வரிலிருந்து கருவிகள் ஆகியவற்றை எடுத்துக் கொண்டு LLMக்கு ஒரு கோரிக்கையை அனுப்பி பதிலைத் திருப்பி அளிக்கும்.

LLM இன் பதிலை `choices` எனும் வரிசை கொண்டிருக்கும். எதாவது `tool_calls` உள்ளதா என முடிவை செயலாக்க வேண்டும். இது LLM குறிப்பிட்ட கருவி அழைக்கப்பட வேண்டுமென்று வேண்டுகோள் விடுக்கும் என்பதைக் காட்டும். LLM பதிலை கையாள ஒரு செயல்பாட்டை வரையறுக்க, உங்கள் `main.rs` கோப்பின் கீழே பின்வரும் குறியீட்டைச் சேர்க்கவும்:

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

    // உள்ளடக்கம் கிடைத்தால் அச்சிடவும்
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // கருவி அழைப்புகளை கையாளவும்
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // உதவியாளர் സന്ദேஷம் சேர்க்கவும்

        // ஒவ்வொரு கருவி அழிப்பையும் செயல்படுத்தவும்
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // செய்திகளுக்கு கருவி முடிவுகளைச் சேர்க்கவும்
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

`tool_calls` இருந்தால், அது கருவி தகவலை எடுத்து, MCP சர்வரை கருவி கோரிக்கையுடன் அழைக்கும், அதன் முடிவுகளை உரையாடல் செய்திகளுக்கு சேர்க்கும். பின்னர் LLM உடன் உரையாடலை தொடர்கிறது, செய்திகள் உதவியாளர் பதிலுடன் மற்றும் கருவி அழைப்பு விளைவுகளுடன் புதுப்பிக்கப்படுகின்றன.

MCP அழைப்புகளுக்கு LLM திருப்பி அளிக்கும் கருவி அழைப்பு தகவலை எடுக்க மற்றொரு உதவியாளர் செயல்பாட்டை சேர்ப்போம். உங்கள் `main.rs` இல் கீழே பின்வரும் குறியீட்டைச் சேர்க்கவும்:

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

எல்லா பகுதிகளும் பொருந்தும்போது, ஆரம்ப பயனர் கேள்வியை கையாளி LLM-ஐ அழைக்கலாம். உங்கள் `main` செயல்பாட்டை பின்வரும் குறியீட்டுடன் புதுப்பிக்கவும்:

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

இது ஆரம்ப பயனர் கேள்வியுடன் LLM-ஐ விசாரித்து, இரண்டு எண்களின் கூட்டை கேட்கும், மேலும் பதிலை செயலாக்கி கருவி அழைப்புகளை நிலைத்தளத்தில் கையாளும்.

அருமை, நீங்கள் அதை செய்தீர்கள்!

## பணிநிர்ணயம்

பயிற்சியில் உள்ள குறியீட்டை எடுத்து சர்வரை இன்னும் சில கருவிகளுடன் விருத்தி செய்யவும். பிறகு LLM கொண்ட ஒரு கிளையண்ட் உருவாக்கி, பயிற்சிப் போலவே மாற்று கேள்விகளுடன் சோதித்து, அனைத்து சர்வர் கருவிகள் வடிவமைப்பாக அழைக்கப்படுவதை உறுதிப்படுத்தவும். இப்பாடுகொண்ட கிளையண்ட் அமைப்பால் இறுதி பயனர் சரியான கிளையண்ட் கட்டளைகளை பயன்படுத்தாமல் கேள்விகளைப் பயன்படுத்தி மிகச் சிறந்த பயனர் அனுபவத்தை பெறுவார், எந்த MCP சர்வர் அழைக்கப்படுவதை அறியாமலே.

## தீர்வு

[Solution](./solution/README.md)

## முக்கியக் குறிப்பு

- உங்கள் கிளையண்டில் LLM-ஐச் சேர்த்தல் பயனர்களுக்கு MCP சர்வர்களுடன் சிறந்த தொடர்பை வழங்கும்.
- MCP சர்வர் பதிலை LLM புரிந்துகொள்ளக்கூடிய வடிவிற்கு மாற்ற வேண்டும்.

## உதாரணங்கள்

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## கூடுதல் வளங்கள்

## அடுத்தது என்ன

- அடுத்தது: [Visual Studio Code பயன்படுத்தி சர்வரை உபயோகித்தல்](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->