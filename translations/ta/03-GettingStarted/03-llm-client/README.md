# LLM உடன் ஒரு கிளையண்டை உருவாக்குதல்

இன்னும் வரை, நீங்கள் ஒரு சர்வர் மற்றும் ஒரு கிளையண்டை உருவாக்குவது எப்படி என்பதைப் பார்த்துள்ளீர்கள். கிளையண்ட் சர்வரை தெளிவாக அழைத்து அதன் கருவிகள், வளங்கள் மற்றும் ப்ராம்ப்ட்களை பட்டியலிட முடிந்தது. இருப்பினும், இது மிகவும் நடைமுறைமற்ற அணுகுமுறை. உங்கள் பயனர் முகவரியியல் காலத்தில் வாழ்கிறார் மற்றும் ப்ராம்ப்ட்களைப் பயன்படுத்தி LLM உடன் தொடர்பு கொள்ள எதிர்பார்க்கிறார். உங்கள் பயனருக்கு, நீங்கள் MCP ஐ பயன்படுத்துகிறீர்களா இல்லையா என்பது முக்கியமல்ல, ஆனால் அவர்கள் இயற்கை மொழியைப் பயன்படுத்தி தொடர்பு கொள்ள எதிர்பார்க்கிறார்கள். இதை எப்படி தீர்க்கலாம்? தீர்வு கிளையண்டில் ஒரு LLM ஐ சேர்ப்பதே ஆகும்.

## கண்ணோட்டம்

இந்த பாடத்தில், உங்கள் கிளையண்டில் ஒரு LLM ஐச் சேர்ப்பதில் கவனம் செலுத்தி, இது உங்கள் பயனருக்கு எவ்வாறு சிறந்த அனுபவத்தை வழங்குகிறது என்பதை காண்போம்.

## கற்றல் நோக்கங்கள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- ஒரு LLM உடன் கிளையண்டை உருவாக்க முடியும்.
- LLM ஐப் பயன்படுத்தி MCP சர்வருடன் தானாக தொடர்பு கொள்ள முடியும்.
- கிளையண்ட் பக்கத்தில் சிறந்த இறுதி பயனர் அனுபவத்தை வழங்க முடியும்.

## அணுகுமுறை

நாம் எடுக்க வேண்டிய அணுகுமுறையை புரிந்துகொள்ள முயலுவோம். ஒரு LLM ஐச் சேர்ப்பது எளிதாகத் தோன்றினாலும், நாங்கள் உண்மையில் இதை செய்வோமா?

கிளையண்ட் சர்வருடன் தொடர்பு கொள்ளும் விதம் இதுவாக இருக்கும்:

1. சர்வருடன் இணைப்பு ஏற்படுத்துக.

1. திறன்கள், ப்ராம்ப்ட்கள், வளங்கள் மற்றும் கருவிகளை பட்டியலிட்டு அவற்றின் ஸ்கீமாவை சேமிக்கவும்.

1. ஒரு LLM ஐச் சேர்த்து, சேமிக்கப்பட்ட திறன்கள் மற்றும் அவற்றின் ஸ்கீமாவை LLM புரிந்துகொள்ளும் வடிவத்தில் அனுப்பவும்.

1. பயனர் ப்ராம்ப்டை LLM க்கு அனுப்பி, கிளையண்ட் பட்டியலிட்ட கருவிகளுடன் சேர்த்து கையாளவும்.

சிறந்தது, இப்போது நாம் இதை உயர் மட்டத்தில் எப்படி செய்வது என்பதை புரிந்துகொண்டோம், கீழே உள்ள பயிற்சியில் இதை முயற்சிப்போம்.

## பயிற்சி: LLM உடன் ஒரு கிளையண்டை உருவாக்குதல்

இந்த பயிற்சியில், நாங்கள் எவ்வாறு ஒரு LLM ஐ நமது கிளையண்டில் சேர்ப்பது என்பதை கற்றுக்கொள்வோம்.

### GitHub தனிப்பட்ட அணுகல் டோக்கன் மூலம் அங்கீகாரம்

GitHub டோக்கன் உருவாக்குவது நேர்த்தியான செயல்முறை. இதோ எப்படி செய்வது:

- GitHub அமைப்புகளுக்கு செல்லவும் – மேல் வலது மூலையில் உங்கள் சுயவிவர படத்தை கிளிக் செய்து Settings ஐத் தேர்ந்தெடுக்கவும்.
- Developer Settings க்கு செல்லவும் – கீழே ஸ்க்ரோல் செய்து Developer Settings ஐ கிளிக் செய்யவும்.
- Personal Access Tokens ஐத் தேர்ந்தெடுக்கவும் – Fine-grained tokens ஐ கிளிக் செய்து Generate new token ஐத் தேர்ந்தெடுக்கவும்.
- உங்கள் டோக்கனை அமைக்கவும் – குறிப்பு சேர்க்கவும், காலாவதியான தேதி அமைக்கவும், தேவையான அனுமதிகளை (scopes) தேர்ந்தெடுக்கவும். இதில் Models அனுமதியை சேர்க்க வேண்டும்.
- டோக்கனை உருவாக்கி நகலெடுக்கவும் – Generate token ஐ கிளிக் செய்து உடனடியாக நகலெடுக்கவும், ஏனெனில் மீண்டும் பார்க்க முடியாது.

### -1- சர்வருடன் இணைப்பு

முதலில் நமது கிளையண்டை உருவாக்குவோம்:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ஸ்கீமா சரிபார்ப்புக்காக zod ஐ இறக்குமதி செய்க

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

மேலே உள்ள குறியீட்டில்:

- தேவையான நூலகங்களை இறக்குமதி செய்துள்ளோம்
- `client` மற்றும் `openai` என்ற இரண்டு உறுப்பினர்களுடன் ஒரு வகுப்பை உருவாக்கி, கிளையண்டை நிர்வகிக்கவும் LLM உடன் தொடர்பு கொள்ளவும் உதவுகிறது.
- `baseUrl` ஐ inference API க்கு குறிக்க GitHub Models ஐ பயன்படுத்த LLM உதாரணத்தை அமைத்துள்ளோம்.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio இணைப்புக்கான சர்வர் அளவுருக்களை உருவாக்கவும்
server_params = StdioServerParameters(
    command="mcp",  # இயக்கக்கூடியது
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

மேலே உள்ள குறியீட்டில்:

- MCP க்கான தேவையான நூலகங்களை இறக்குமதி செய்துள்ளோம்
- ஒரு கிளையண்டை உருவாக்கியுள்ளோம்

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

முதலில், உங்கள் `pom.xml` கோப்பில் LangChain4j சார்புகளைச் சேர்க்க வேண்டும். MCP ஒருங்கிணைப்பு மற்றும் GitHub Models ஆதரவை இயக்க இந்த சார்புகளைச் சேர்க்கவும்:

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

பிறகு உங்கள் Java கிளையண்ட் வகுப்பை உருவாக்கவும்:

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
    
    public static void main(String[] args) throws Exception {        // LLM ஐ GitHub மாதிரிகளை பயன்படுத்த அமைக்கவும்
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // சர்வருடன் இணைக்க MCP போக்குவரத்தை உருவாக்கவும்
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
}
```

மேலே உள்ள குறியீட்டில்:

- **LangChain4j சார்புகளைச் சேர்த்துள்ளோம்**: MCP ஒருங்கிணைப்பு, OpenAI அதிகாரப்பூர்வ கிளையண்ட் மற்றும் GitHub Models ஆதரவு
- **LangChain4j நூலகங்களை இறக்குமதி செய்துள்ளோம்**: MCP ஒருங்கிணைப்பு மற்றும் OpenAI உரையாடல் மாதிரி செயல்பாடு
- **`ChatLanguageModel` உருவாக்கியுள்ளோம்**: GitHub Models ஐ உங்கள் GitHub டோக்கனுடன் பயன்படுத்த அமைக்கப்பட்டுள்ளது
- **HTTP போக்குவரத்தை அமைத்துள்ளோம்**: MCP சர்வருடன் இணைக்க Server-Sent Events (SSE) பயன்படுத்தி
- **MCP கிளையண்டை உருவாக்கியுள்ளோம்**: சர்வருடன் தொடர்பை கையாளும்
- **LangChain4j இன் உள்ளமைக்கப்பட்ட MCP ஆதரவை பயன்படுத்தியுள்ளோம்**: LLM மற்றும் MCP சர்வர்களுக்கு இடையேயான ஒருங்கிணைப்பை எளிதாக்குகிறது

#### Rust

இந்த உதாரணம் Rust அடிப்படையிலான MCP சர்வர் இயங்குவதாக கருதுகிறது. இல்லையெனில், சர்வரை உருவாக்க [01-first-server](../01-first-server/README.md) பாடத்துக்கு திரும்பவும்.

Rust MCP சர்வர் இருந்தால், ஒரு டெர்மினலை திறந்து சர்வர் கோப்பகத்துக்கு செல்லவும். பிறகு புதிய LLM கிளையண்ட் திட்டத்தை உருவாக்க கீழ்காணும் கட்டளையை இயக்கவும்:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` கோப்பில் கீழ்காணும் சார்புகளைச் சேர்க்கவும்:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI க்கான அதிகாரப்பூர்வ Rust நூலகம் இல்லை, இருப்பினும் `async-openai` கிரேட் ஒரு [சமூக பராமரிக்கப்பட்ட நூலகம்](https://platform.openai.com/docs/libraries/rust#rust) ஆகும்.

`src/main.rs` கோப்பை திறந்து உள்ளடக்கத்தை கீழ்காணும் குறியீட்டால் மாற்றவும்:

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

    // OpenAI கிளையண்டை அமைக்கவும்
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP கிளையண்டை அமைக்கவும்
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

    // செய்யவேண்டியது: MCP கருவி பட்டியலைப் பெறவும்

    // செய்யவேண்டியது: கருவி அழைப்புகளுடன் LLM உரையாடல்

    Ok(())
}
```

இந்த குறியீடு MCP சர்வர் மற்றும் GitHub Models உடன் LLM தொடர்புக்கு அடிப்படையான Rust செயலியை அமைக்கிறது.

> [!IMPORTANT]
> செயலியை இயக்குவதற்கு முன் உங்கள் GitHub டோக்கனுடன் `OPENAI_API_KEY` சுற்றுச்சூழல் மாறியை அமைக்கவும்.

சிறந்தது, அடுத்த படியாக சர்வரின் திறன்களை பட்டியலிடுவோம்.

### -2- சர்வர் திறன்களை பட்டியலிடுதல்

இப்போது சர்வருடன் இணைந்து அதன் திறன்களை கேட்கலாம்:

#### Typescript

அதே வகுப்பில் கீழ்காணும் முறைகளைச் சேர்க்கவும்:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // கருவிகளை பட்டியலிடுதல்
    const toolsResult = await this.client.listTools();
}
```

மேலே உள்ள குறியீட்டில்:

- சர்வருடன் இணைக்க `connectToServer` என்ற குறியீட்டைச் சேர்த்துள்ளோம்.
- `run` என்ற செயல்முறையை உருவாக்கி, தற்போதைக்கு கருவிகளை மட்டுமே பட்டியலிடுகிறது, விரைவில் இதை விரிவாக்குவோம்.

#### Python

```python
# கிடைக்கும் வளங்களை பட்டியலிடு
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# கிடைக்கும் கருவிகளை பட்டியலிடு
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

நாங்கள் சேர்த்தது:

- வளங்கள் மற்றும் கருவிகளை பட்டியலிட்டு அச்சிடுதல். கருவிகளுக்கு `inputSchema` ஐவும் பட்டியலிட்டோம், இது பின்னர் பயன்படுத்தப்படும்.

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

மேலே உள்ள குறியீட்டில்:

- MCP சர்வரில் உள்ள கருவிகளை பட்டியலிட்டோம்
- ஒவ்வொரு கருவிக்கும் பெயர், விளக்கம் மற்றும் அதன் ஸ்கீமாவை பட்டியலிட்டோம். இதை விரைவில் கருவிகளை அழைக்க பயன்படுத்துவோம்.

#### Java

```java
// MCP கருவிகளை தானாக கண்டுபிடிக்கும் ஒரு கருவி வழங்குநரை உருவாக்கவும்
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP கருவி வழங்குநர் தானாக கையாள்கிறது:
// - MCP சேவையகத்திலிருந்து கிடைக்கும் கருவிகளை பட்டியலிடுதல்
// - MCP கருவி ஸ்கீமாக்களை LangChain4j வடிவத்திற்கு மாற்றுதல்
// - கருவி செயல்பாடு மற்றும் பதில்களை நிர்வகித்தல்
```

மேலே உள்ள குறியீட்டில்:

- MCP சர்வரிலிருந்து அனைத்து கருவிகளையும் தானாக கண்டறிந்து பதிவு செய்யும் `McpToolProvider` உருவாக்கியுள்ளோம்
- கருவி வழங்குநர் MCP கருவி ஸ்கீமாவையும் LangChain4j கருவி வடிவத்தையும் உள்ளகமாக மாற்றுகிறது
- இந்த அணுகுமுறை கருவிகளை கையேடு பட்டியலிடல் மற்றும் மாற்றலை மறைத்து விடுகிறது

#### Rust

MCP சர்வரிலிருந்து கருவிகளை பெற `list_tools` முறையைப் பயன்படுத்துகிறோம். `main` செயல்பாட்டில் MCP கிளையண்டை அமைத்த பிறகு கீழ்காணும் குறியீட்டைச் சேர்க்கவும்:

```rust
// MCP கருவி பட்டியலைப் பெறுக
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- சர்வர் திறன்களை LLM கருவிகளாக மாற்றுதல்

சர்வர் திறன்களை பட்டியலிட்ட பிறகு அடுத்த படி அவற்றை LLM புரிந்துகொள்ளும் வடிவமாக மாற்றுவதே ஆகும். இதை செய்தவுடன், இந்த திறன்களை LLM க்கு கருவிகளாக வழங்கலாம்.

#### TypeScript

1. MCP சர்வர் பதிலை LLM பயன்படுத்தக்கூடிய கருவி வடிவமாக மாற்ற கீழ்காணும் குறியீட்டைச் சேர்க்கவும்:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // உள்ளீடு_schema அடிப்படையில் ஒரு zod திட்டத்தை உருவாக்கவும்
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

    மேலே உள்ள குறியீடு MCP சர்வர் பதிலை எடுத்துக் கொண்டு LLM புரிந்துகொள்ளும் கருவி வரையறை வடிவமாக மாற்றுகிறது.

1. அடுத்து `run` முறையை சர்வர் திறன்களை பட்டியலிட மாற்றுவோம்:

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

    மேலே உள்ள குறியீட்டில், `run` முறையை மாற்றி முடிவில் உள்ள ஒவ்வொரு பதிவுக்கும் `openAiToolAdapter` ஐ அழைக்கின்றோம்.

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

    `convert_to_llm_tools` என்ற செயல்பாட்டில் MCP கருவி பதிலை எடுத்துக் கொண்டு LLM புரிந்துகொள்ளும் வடிவமாக மாற்றுகிறோம்.

1. அடுத்து, கிளையண்ட் குறியீட்டில் இதைப் பயன்படுத்த மாற்றுவோம்:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    இங்கு MCP கருவி பதிலை LLM க்கு வழங்க `convert_to_llm_tool` அழைப்பைச் சேர்த்துள்ளோம்.

#### .NET

1. MCP கருவி பதிலை LLM புரிந்துகொள்ளும் வடிவமாக மாற்ற குறியீட்டைச் சேர்க்கலாம்

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

மேலே உள்ள குறியீட்டில்:

- பெயர், விளக்கம் மற்றும் உள்ளீட்டு ஸ்கீமாவை எடுத்துக் கொண்டு `ConvertFrom` என்ற செயல்பாட்டை உருவாக்கியுள்ளோம்.
- இது `FunctionDefinition` உருவாக்கி அதை `ChatCompletionsDefinition` க்கு அனுப்புகிறது. இது LLM புரிந்துகொள்ளும் வடிவம்.

1. மேலே உள்ள செயல்பாட்டைப் பயன்படுத்த `run` போன்ற குறியீட்டை மாற்றுவோம்:

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
// இயற்கை மொழி தொடர்புக்கான ஒரு பாட்டை உருவாக்கவும்
public interface Bot {
    String chat(String prompt);
}

// LLM மற்றும் MCP கருவிகளுடன் AI சேவையை அமைக்கவும்
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

மேலே உள்ள குறியீட்டில்:

- இயற்கை மொழி தொடர்புகளுக்கு எளிய `Bot` இடைமுகத்தை வரையறுத்துள்ளோம்
- LangChain4j இன் `AiServices` ஐ பயன்படுத்தி LLM ஐ MCP கருவி வழங்குநருடன் தானாக இணைத்துள்ளோம்
- இந்த கட்டமைப்பு கருவி ஸ்கீமா மாற்றம் மற்றும் செயல்பாடு அழைப்பை பின்னணியில் தானாக கையாள்கிறது
- இதனால் கையேடு கருவி மாற்றல் தேவையில்லை - LangChain4j MCP கருவிகளை LLM பொருந்தக்கூடிய வடிவமாக மாற்றும் சிக்கல்களை எல்லாம் கையாள்கிறது

#### Rust

MCP கருவி பதிலை LLM புரிந்துகொள்ளும் வடிவமாக மாற்ற, கருவி பட்டியலை வடிவமைக்கும் உதவியாளர் செயல்பாட்டை `main.rs` கோப்பில் `main` செயல்பாட்டுக்குப் பின்பு சேர்க்கவும். இது LLM க்கு கோரிக்கை செய்யும்போது அழைக்கப்படும்:

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

சிறந்தது, பயனர் கோரிக்கைகளை கையாள தயாராகவில்லை, அதனை அடுத்து செய்யலாம்.

### -4- பயனர் ப்ராம்ப்ட் கோரிக்கையை கையாளுதல்

இந்த குறியீட்டில், பயனர் கோரிக்கைகளை கையாளுவோம்.

#### TypeScript

1. LLM ஐ அழைக்க பயன்படுத்தப்படும் முறையைச் சேர்க்கவும்:

    ```typescript
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

        // 3. முடிவுடன் ஏதாவது செய்க
        // செய்ய வேண்டியது

        }
    }
    ```

    மேலே உள்ள குறியீட்டில்:

    - `callTools` என்ற முறையைச் சேர்த்துள்ளோம்.
    - LLM பதிலைப் பெற்று எந்த கருவிகள் அழைக்கப்பட்டுள்ளன என்பதைச் சரிபார்க்கிறது:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // கருவியை அழைக்கவும்
        }
        ```

    - LLM கருவி அழைக்க வேண்டும் எனக் கூறினால், கருவியை அழைக்கிறது:

        ```typescript
        // 2. சர்வரின் கருவியை அழைக்கவும்
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. முடிவுடன் ஏதாவது செய்க
        // செய்ய வேண்டியது
        ```

1. `run` முறையை LLM அழைப்புகளுடன் மற்றும் `callTools` அழைப்புடன் புதுப்பிக்கவும்:

    ```typescript

    // 1. LLM க்கான உள்ளீடாக இருக்கும் செய்திகளை உருவாக்கவும்
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ஐ அழைக்கவும்
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM பதிலைப் பார்வையிடவும், ஒவ்வொரு தேர்விற்கும், அது கருவி அழைப்புகளை கொண்டுள்ளதா என்று சரிபார்க்கவும்
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
          // input_schema அடிப்படையில் ஒரு zod ஸ்கீமா உருவாக்குக
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // வகையை "function" என தெளிவாக அமைக்கவும்
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
    
          // 3. முடிவுடன் ஏதாவது செய்க
          // செய்ய வேண்டியது
    
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
    
        // 1. LLM பதிலை வழியாக செல்லவும், ஒவ்வொரு தேர்வுக்கும், அது கருவி அழைப்புகளை கொண்டுள்ளதா என்று சரிபார்க்கவும்
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
    # எல்.எல்.எம்
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. அடுத்து, LLM ஐ அழைக்கும் செயல்பாட்டைச் சேர்க்கவும்:

    ```python
    # எல்.எல்.எம்

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

    மேலே உள்ள குறியீட்டில்:

    - MCP சர்வரில் கண்டுபிடித்த மற்றும் மாற்றிய செயல்பாடுகளை LLM க்கு வழங்கியுள்ளோம்.
    - பின்னர் அந்த செயல்பாடுகளுடன் LLM ஐ அழைத்துள்ளோம்.
    - முடிவை ஆய்வு செய்து எந்த செயல்பாடுகளை அழைக்க வேண்டும் என்பதை கண்டறிகிறோம்.
    - இறுதியில் அழைக்க வேண்டிய செயல்பாடுகளின் வரிசையை அனுப்புகிறோம்.

1. கடைசி படி, முக்கிய குறியீட்டை புதுப்பிக்கவும்:

    ```python
    prompt = "Add 2 to 20"

    # LLM-க்கு எந்த கருவிகள் அனைத்தும் தேவையா என்று கேளுங்கள், இருந்தால்
    functions_to_call = call_llm(prompt, functions)

    # பரிந்துரைக்கப்பட்ட செயல்பாடுகளை அழைக்கவும்
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    மேலே உள்ள குறியீட்டில்:

    - LLM ப்ராம்ப்ட் அடிப்படையில் அழைக்க வேண்டிய MCP கருவியை `call_tool` மூலம் அழைக்கிறோம்.
    - கருவி அழைப்பின் முடிவை MCP சர்வரில் அச்சிடுகிறோம்.

#### .NET

1. LLM ப்ராம்ப்ட் கோரிக்கைக்கான குறியீட்டை காண்போம்:

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

    மேலே உள்ள குறியீட்டில்:

    - MCP சர்வரிலிருந்து கருவிகளை பெற்றுள்ளோம், `var tools = await GetMcpTools()`.
    - பயனர் ப்ராம்ப்ட் `userMessage` ஐ வரையறுத்துள்ளோம்.
    - மாதிரி மற்றும் கருவிகளை குறிப்பிடும் விருப்பங்கள் பொருளை உருவாக்கியுள்ளோம்.
    - LLM க்கு கோரிக்கை செய்துள்ளோம்.

1. கடைசி படி, LLM செயல்பாடு அழைக்க வேண்டுமா என்று பார்க்கலாம்:

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

    மேலே உள்ள குறியீட்டில்:

    - செயல்பாடு அழைப்புகளின் பட்டியலில் சுற்றி,
    - ஒவ்வொரு கருவி அழைப்புக்கும் பெயர் மற்றும் அளவுருக்களை பிரித்து MCP சர்வரில் கருவியை அழைக்க MCP கிளையண்டை பயன்படுத்துகிறோம். முடிவுகளை அச்சிடுகிறோம்.

முழு குறியீடு:

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
    // MCP கருவிகளை தானாக பயன்படுத்தும் இயற்கை மொழி கோரிக்கைகளை செயல்படுத்தவும்
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

மேலே உள்ள குறியீட்டில்:

- எளிய இயற்கை மொழி ப்ராம்ப்ட்களைப் பயன்படுத்தி MCP சர்வர் கருவிகளுடன் தொடர்பு கொண்டுள்ளோம்
- LangChain4j கட்டமைப்பு தானாக கையாள்கிறது:
  - தேவையான போது பயனர் ப்ராம்ப்ட்களை கருவி அழைப்புகளாக மாற்றுதல்
  - LLM முடிவின் அடிப்படையில் சரியான MCP கருவிகளை அழைத்தல்
  - LLM மற்றும் MCP சர்வருக்கு இடையேயான உரையாடல் ஓட்டத்தை நிர்வகித்தல்
- `bot.chat()` முறை இயற்கை மொழி பதில்களை வழங்குகிறது, இதில் MCP கருவி செயல்பாடுகளின் முடிவுகள் இருக்கலாம்
- இது பயனர்களுக்கு MCP அடிப்படையை அறிய தேவையில்லாமல் தொடர்ச்சியான அனுபவத்தை வழங்குகிறது

முழு குறியீடு உதாரணம்:

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

இங்கு பெரும்பாலான வேலை நடக்கிறது. முதலில் ஆரம்ப பயனர் ப்ராம்ப்டுடன் LLM ஐ அழைக்கிறோம், பின்னர் பதிலை ஆய்வு செய்து எந்த கருவிகள் அழைக்கப்பட வேண்டும் என்பதை பார்க்கிறோம். தேவையெனில் அந்த கருவிகளை அழைத்து, LLM உடன் உரையாடலை தொடர்கிறோம், மேலும் கருவி அழைப்புகள் தேவையில்லை மற்றும் இறுதி பதில் கிடைக்கும் வரை.

பல முறை LLM ஐ அழைக்க இருப்பதால், LLM அழைப்பை கையாளும் செயல்பாட்டை வரையறுக்கலாம். கீழ்காணும் செயல்பாட்டை `main.rs` கோப்பில் சேர்க்கவும்:

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

இந்த செயல்பாடு LLM கிளையண்ட், செய்திகளின் பட்டியல் (பயனர் ப்ராம்ப்ட் உட்பட), MCP சர்வர் கருவிகள் ஆகியவற்றை எடுத்துக் கொண்டு LLM க்கு கோரிக்கை அனுப்பி பதிலை திருப்பி அளிக்கிறது.
LLM இன் பதில் `choices` என்ற வரிசையை கொண்டிருக்கும். எந்த `tool_calls` உள்ளதா என்று பார்க்க முடிவு செய்ய நாம் முடிவை செயலாக்க வேண்டும். LLM ஒரு குறிப்பிட்ட கருவி அழைக்கப்பட வேண்டும் என்று கோருகிறது என்பதை இது நமக்கு தெரிவிக்கிறது. LLM பதிலை கையாள ஒரு செயல்பாட்டை வரையறுக்க உங்கள் `main.rs` கோப்பின் கீழே பின்வரும் குறியீட்டை சேர்க்கவும்:

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

    // உள்ளடக்கம் இருந்தால் அச்சிடுக
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // கருவி அழைப்புகளை கையாள்க
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // உதவியாளர் செய்தியை சேர்க்கவும்

        // ஒவ்வொரு கருவி அழைப்பையும் செயல்படுத்துக
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

`tool_calls` இருந்தால், அது கருவி தகவலை எடுத்து, MCP சர்வரை கருவி கோரிக்கையுடன் அழைக்கிறது, மற்றும் முடிவுகளை உரையாடல் செய்திகளுக்கு சேர்க்கிறது. பின்னர் LLM உடன் உரையாடலை தொடர்கிறது மற்றும் உதவியாளர் பதில் மற்றும் கருவி அழைப்பு முடிவுகளுடன் செய்திகள் புதுப்பிக்கப்படுகின்றன.

LLM MCP அழைப்புகளுக்கு திருப்பும் கருவி அழைப்பு தகவலை எடுக்க, அழைப்பை செய்ய தேவையான அனைத்தையும் எடுக்க மற்றொரு உதவி செயல்பாட்டை சேர்க்கலாம். உங்கள் `main.rs` கோப்பின் கீழே பின்வரும் குறியீட்டை சேர்க்கவும்:

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

அனைத்து பகுதிகளும் இடத்தில் உள்ளதால், ஆரம்ப பயனர் கேள்வியை கையாளவும் LLM ஐ அழைக்கவும் முடியும். உங்கள் `main` செயல்பாட்டை பின்வரும் குறியீட்டுடன் புதுப்பிக்கவும்:

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

இது ஆரம்ப பயனர் கேள்வியுடன் LLM ஐ கேட்கும், இரண்டு எண்களின் கூட்டுத்தொகையை கேட்டு, பதிலை செயலாக்கி கருவி அழைப்புகளை தானாக கையாளும்.

சிறந்தது, நீங்கள் செய்துவிட்டீர்கள்!

## பணிகள்

பயிற்சியில் உள்ள குறியீட்டை எடுத்து சர்வரை மேலும் சில கருவிகளுடன் உருவாக்கவும். பின்னர் பயிற்சியில் உள்ளபோல் LLM உடன் ஒரு கிளையண்டை உருவாக்கி, வெவ்வேறு கேள்விகளுடன் சோதனை செய்யவும், உங்கள் சர்வர் கருவிகள் அனைத்தும் தானாக அழைக்கப்படுவதை உறுதிப்படுத்தவும். இந்த வகை கிளையண்ட் கட்டமைப்பு இறுதி பயனருக்கு சிறந்த அனுபவத்தை வழங்கும், ஏனெனில் அவர்கள் சரியான கிளையண்ட் கட்டளைகள் பதிலாக கேள்விகளை பயன்படுத்த முடியும் மற்றும் எந்த MCP சர்வர் அழைக்கப்படுவதை அறியாமல் இருக்க முடியும்.

## தீர்வு

[தீர்வு](/03-GettingStarted/03-llm-client/solution/README.md)

## முக்கியக் குறிப்புகள்

- உங்கள் கிளையண்டில் LLM சேர்ப்பது MCP சர்வர்களுடன் பயனர்களுக்கு சிறந்த தொடர்பு முறையை வழங்கும்.
- MCP சர்வர் பதிலை LLM புரிந்துகொள்ளக்கூடியதாக மாற்ற வேண்டும்.

## மாதிரிகள்

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## கூடுதல் வளங்கள்

## அடுத்தது என்ன

- அடுத்து: [Visual Studio Code பயன்படுத்தி சர்வரை பயன்படுத்துதல்](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனிக்கவும். அசல் ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ மூலமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பேற்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->