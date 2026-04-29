# LLM உடன் ஒரு கிளையண்ட் உருவாக்குதல்

இதுவரை, நீங்கள் ஒரு சர்வரை மற்றும் ஒரு கிளையண்டை எப்படி உருவாக்குவது என்பதைப் பார்த்துள்ளீர்கள். கிளையண்ட் அதன் கருவிகள், வளங்கள் மற்றும் பிராம்ப்ட்களை பட்டியலிடுவதற்கு சர்வரை திறம்பட அழைக்க முடிந்தது. இது மிகவும் நடைமுறை நடைமுறையாகவில்லை. உங்கள் பயனர்கள் செயற்படுத்தும் காலத்தில் உயிரினமான முன்மொழிவுகளை (prompts) பயன்படுத்தி LLM உடன் தொடர்பு கொள்ள எதிர்பார்க்கின்றனர். நீங்கள் MCP பயன்படுத்தி உங்கள் திறன்களை சேமிக்கிறீர்களா என்பதை அவர்கள் கவலைப்பட மாட்டார்கள்; அவர்கள் இயற்கை மொழியைப் பயன்படுத்தி தொடர்பு கொள்ள எதிர்பார்க்கின்றனர். இதனை எப்படி தீர்வுகாணப்போகிறோம்? அதற்கான தீர்வு கிளையண்டில் LLM ஒன்றை சேர்ப்பது ஆகும்.

## கண்ணோட்டம்

இந்த பாடத்தில், உங்கள் கிளையண்டுக்கு LLM ஒன்றை சேர்ப்பதில் கவனம் செலுத்துகிறோம் மற்றும் இது உங்கள் பயனருக்கு 훨씬 சிறந்த அனுபவத்தை எவ்வாறு வழங்குகிறது என்பதைக் காண்பிக்கிறோம்.

## கற்றல் இலக்குகள்

இந்த பாடத்தின் முடிவில், நீங்கள்:

- LLM உடன் ஒரு கிளையண்டை உருவாக்க முடியும்.
- LLM பயன்படுத்தி MCP சர்வருடன் தடை இல்லாமல் தொடர்பு கொள்ள முடியும்.
- கிளையண்ட் பக்கத்தில் சிறந்த பயனர் அனுபவத்தை வழங்க முடியும்.

## அணுகுமுறை

நாம் எடுக்க வேண்டிய அணுகுமுறையை புரிந்து கொள்ள முயலுவோம். LLM ஒன்றை சேர்ப்பது எளிதாக தோன்றுகிறது, ஆனால் நிஜமாக இதை நாம் செய்துகொள்வோமா?

கிளையண்ட் சர்வருடன் தொடர்பு கொள்வது இப்படிச் செய்யப்படும்:

1. சர்வருடன் இணைப்பு ஏற்படுத்துக.

1. திறன்கள், பிராம்ப்ட்கள், வளங்கள் மற்றும் கருவிகள் பட்டியலிடுக, மற்றும் அவற்றின் திட்டவட்ட வடிவமைப்பினை சேமிக்கவும்.

1. ஒரு LLM ஐச் சேர்த்து சேமிக்கப்பட்ட திறன்களையும் அவற்றின் திட்டவட்ட வடிவமைப்பையும் LLM புரிந்துகொள்ளும் வடிவில் அனுப்புக.

1. பயனர் பிராம்ப்டை, கிளையண்ட் பட்டியலிட்ட கருவிகளுடன் சேர்த்து LLM க்கு அனுப்பி கையாள்க.

சிறந்தது, இப்போது நாம் இவை மொத்தமாக எப்படி செய்வது என்பதைப் புரிந்துகொண்டோம்; கீழுள்ள பயிற்சியில் இதை முயற்சிப்போம்.

## பயிற்சி: LLM உடன் ஒரு கிளையண்ட் உருவாக்குதல்

இந்த பயிற்சியில், நாம் எங்கள் கிளையண்டிற்கு ஒரு LLM சேர்ப்பதை கற்றுக்கொள்ளப்போகிறோம்.

### GitHub தனிப்பட்ட அணுகல் குறியாக் கொடுக்கல் மூலம் அங்கீகாரம் பெறுதல்

GitHub குறியை உருவாக்குவது எளிதான முறையாகும். இதோ எப்படி செய்வது:

- GitHub அமைப்புகளுக்குச் செல்லவும் – மேல் வலப்பக்கத்தில் உங்கள் பயனர் படம் மீது கிளிக் செய்து Settings ஐத் தேர்ந்தெடுக்கவும்.
- Developer Settings ஆக செல்லவும் – கீழ்தோக் செய்து Developer Settings என்பதை சொடுக்கவும்.
- Personal Access Tokens ஐத் தேர்ந்தெடுக்கவும் – Fine-grained tokens ஐ கிளிக் செய்து புதிய குறி உருவாக்கவும்.
- உங்கள் குறியை அமைக்கவும் – குறிப்பைச் சேர்க்கவும், காலாவதி தேதியை அமைக்கவும், அவசியமான அனுமதிகளை தேர்ந்தெடுக்கவும் (இக்கேஸில் Models அனுமதியை உறுதிப்படுத்தவும்).
- குறியை உருவாக்கி உடனடியாக நகலெடுக்கவும் – Generate token ஐ அழுத்தி உருவாக்கிய உடன் குறியை நகலெடுக்கவும், மீண்டும் பார்க்க முடியாது.

### -1- சர்வருடன் இணைப்பு ஏற்படுத்துதல்

முதலில் நமது கிளையண்டை உருவாக்குவோம்:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // திட்ட வடிவ சரிபார்ப்புக்காக zod ஐ இறக்குமதி செய்க

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

மேலுள்ள குறியீட்டில் நாம்:

- தேவையான நூலகங்களை இறக்குமதி செய்தோம்
- `client` மற்றும் `openai` என்ற இரண்டு உறுப்பினர்கள் கொண்ட ஒரு வகுப்பை உருவாக்கினோம், இது கிளையண்டை நிர்வகித்து LLM உடன் தொடர்பு கொள்ள உதவும்.
- GitHub Models ஐ பயன்படுத்த எங்கள் LLM உருப்படியை `baseUrl` ஐ inference API க்கு நோக்கிச் செம்கப்படுத்தியது.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio இணைப்பிற்கான சர்வர் அளவுருக்களை உருவாக்கவும்
server_params = StdioServerParameters(
    command="mcp",  # இயங்கக்கூடிய கோப்பு
    args=["run", "server.py"],  # விருப்ப கட்டளை வரி அளவுருக்கள்
    env=None,  # விருப்ப சூழல் மாறிகள்
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # இணைப்பைத் துவக்கவும்
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

மேலுள்ள குறியீட்டில் நாம்:

- MCP க்கான தேவையான நூலகங்களை இறக்குமதி செய்தோம்
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

முதலில், உங்கள் `pom.xml` கோப்பில் LangChain4j சார்புகள் சேர்க்க வேண்டும். MCP ஒருங்கிணைப்பு மற்றும் GitHub Models ஆதரவுக்கு கீழ்காணும் சார்புகளைச் சேர்க்கவும்:

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

பின் உங்கள் ஜாவா கிளையண்ட் வகுப்பை உருவாக்கவும்:

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
    
    public static void main(String[] args) throws Exception {        // GitHub மாதிரிகளை பயன்படுத்த LLM ஐ அமைக்கவும்
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // சர்வருடன் இணைக்க MCP பரிமாற்றத்தை உருவாக்கவும்
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

மேலுள்ள குறியீட்டில் நாம்:

- **LangChain4j சார்புகள் சேர்த்துள்ளோம்**: MCP ஒருங்கிணைப்புக்கு, OpenAI அதிகாரப்பூர்வ கிளையண்டுக்கு மற்றும் GitHub Models ஆதரவுக்கு
- **LangChain4j நூலகங்களை இறக்குமதி செய்தோம்**: MCP ஒருங்கிணைப்பு மற்றும் OpenAI சாட் மாடல் செயல்பாட்டிற்கு
- **`ChatLanguageModel` உருவாக்கினோம்**: GitHub Models மற்றும் உங்கள் GitHub டோக்கனுடன் அமைவழங்கியது
- **HTTP போக்குவரத்தை நிறுவினோம்**: MCP சர்வருடன் Server-Sent Events (SSE) மூலம் இணைக்க
- **MCP கிளையண்டை உருவாக்கினோம்**: சர்வருடன் தொடர்பை கையாள
- **LangChain4j இன் உள்ளமைக்கும் MCP ஆதரவைப் பயன்படுத்தினோம்**: LLM கள் மற்றும் MCP சர்வர்களுக்கிடையேயான ஒருங்கிணைப்பை எளிமையாக்குகிறது

#### Rust

இந்த உதாரணம் நீங்கள் ஒரு Rust அடிப்படையிலான MCP சர்வர் இயக்கிவிட்டு இருக்கீர்கள் எனக் கருதுகிறது. இல்லையெனில், சர்வரை உருவாக்க [01-first-server](../01-first-server/README.md) பாடத்தை பாருங்கள்.

Rust MCP சர்வர் அமைந்ததும், ஒரு டெர்மினல் திறந்து அதே அடைவு நோக்கிச் செல்லவும். பின்னர் புதிய LLM கிளையண்ட் திட்டம் உருவாக்க கீழ்கண்ட கட்டளையை இயக்கவும்:

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
> OpenAI க்கு அதிகாரப்பூர்வமான Rust நூலகம் இல்லை, இருப்பினும் `async-openai` கிரேட் என்பது [சமூகத்தினர் பராமரிக்கும் நூலகம்](https://platform.openai.com/docs/libraries/rust#rust) ஆகும்.

`src/main.rs` கோப்பை திறந்து உள்ளடக்கத்தை பின்வரும் குறியீட்டால் மாற்றவும்:

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

    // OpenAI கிளையன்டை அமைக்கவும்
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP கிளையன்டை அமைக்கவும்
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

இந்த குறியீடு ஒரு அடிப்படையான Rust செயலியை அமைக்கிறது, இது MCP சர்வருடன் மற்றும் GitHub Models உடன் LLM தொடர்புகளுக்கு இணைக்கிறது.

> [!IMPORTANT]
> செயலியை இயக்குவதற்கு முன் உங்கள் GitHub டோக்கனுடன் `OPENAI_API_KEY` சுற்றுச்சூழல் மாறியை அமைக்க மறக்கவேண்டாம்.

சரி, அடுத்து சர்வரின் திறன்களை பட்டியலிடுவோம்.

### -2- சர்வர் திறன்களை பட்டியலிடல்

இப்போது நாம் சர்வருடன் இணைத்து அதன் திறன்களை கேட்கப்போகிறோம்:

#### TypeScript

அதே வகுப்பு உள்ளே கீழ்காணும் முறைகளை சேர்க்கவும்:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // கருவிகள் பட்டியலிடுதல்
    const toolsResult = await this.client.listTools();
}
```

மேலுள்ள குறியீட்டில் நாம்:

- சர்வருடன் இணைப்பதற்கான `connectToServer` குறியீட்டைச் சேர்த்துள்ளோம்.
- பயன்பாட்டு இயக்கத்தை கையாளும் `run` முறையை உருவாக்கினோம். இப்போது அது கருவிகளை மட்டுமே பட்டியலிடுகிறது, விரைவில் இதை விரிவுபடுத்தப்போகிறோம்.

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

நாம் சேர்த்ததாவது:

- வளங்கள் மற்றும் கருவிகளை பட்டியலிட்டு, அச்சிடினோம். கருவிகளுக்கு `inputSchema` ஐக் கூட பட்டியலிட்டோம், இதை பிறகு பயன்படுத்துவோம்.

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

மேலுள்ள குறியீட்டில் நாம்:

- MCP சர்வரில் கிடைக்கும் கருவிகளை பட்டியலிட்டோம்
- ஒவ்வொரு கருவிக்கும் பெயர், விளக்கம் மற்றும் அதன் திட்டவட்ட வடிவமைப்பையும் பட்டியலிட்டோம். இதை பின்னர் கருவிகளை அழைக்க பயன்படுவோம்.

#### Java

```java
// தானாக MCP கருவிகளை கண்டறியும் கருவி வழங்கியதை உருவாக்கவும்
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP கருவி வழங்கியாளர் தானாக கையாளும்:
// - MCP சர்வர் இலிருந்து கிடைக்கும் கருவிகளை பட்டியலிடுதல்
// - MCP கருவி படிவங்களை LangChain4j வடிவத்திற்கு மாற்றுதல்
// - கருவி செயல்பாடு மற்றும் பதில்களை நிர்வகித்தல்
```

மேலுள்ள குறியீட்டில் நாம்:

- MCP சர்வரிலிருந்து அனைத்து கருவிகளையும் தானாகக் கண்டுபிடித்து பதிவு செய்யும் `McpToolProvider` உருவாக்கினோம்
- கருவி வழங்குநர் MCP கருவிகள் திட்டவட்டம் மற்றும் LangChain4j கருவி வடிவத்திற்கு இடையே மாற்றத்தை உள்வாங்கி கையாள்கிறது
- இதன் மூலம் கைமுறை கருவி பட்டியலிடல் மற்றும் மாற்றம் தேவையில்லை

#### Rust

MCP சர்வரிலிருந்து கருவிகளை பெற `list_tools` முறையைப் பயன்படுத்துகிறோம். உங்கள் `main` செயல்பாட்டின் உள்ளே MCP கிளையண்டை அமைத்ததும் கீழ்காணும் குறியீட்டைச் சேர்க்கவும்:

```rust
// MCP சாதன பட்டியலைப் பெறு
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- சர்வர் திறன்களை LLM கருவிகளாக மாற்றல்

அடுத்து சர்வர் திறன்களை பட்டியலிடிய பிறகு, அவற்றை LLM புரிந்து கொள்ளும் வடிவமாக மாற்ற வேண்டும். அந்த திரும்பப்படும் திறன்களை LLM க்கு கருவிகள் போல வழங்க முடியும்.

#### TypeScript

1. MCP சர்வர் பதிலை LLM பயன்படுத்தக்கூடிய கருவி வடிவமாக மாற்ற கீழ்காணும் குறியீட்டைச் சேர்க்கவும்:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // உள்ளீட்டு_ஸ்கீமாவின் அடிப்படையில் ஒரு ஜாட் ஸ்கீமாவை உருவாக்கவும்
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

    ```

    இந்த குறியீடு MCP சர்வர் பதிலை பெற்று அதனை LLM புரிந்து கொள்ளும் கருவி வரையறை வடிவமாக மாற்றுகிறது.

1. அடுத்து `run` முறையை சர்வர் திறன்களை பட்டியலிட மாற்றலாம்:

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

    மேலுள்ள குறியீட்டில், `run` முறை முடிவில் ஒவ்வொரு பெயரிலும் `openAiToolAdapter` ஐ அழைக்க மேபிங் செய்கிறோம்.

#### Python

1. முதலில் கீழ்காணும் மாற்றுபவர் செயல்பாட்டை உருவாக்குவோம்

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

    `convert_to_llm_tools`   என்பது MCP கருவி பதிலை பெற்று LLM புரிந்து கொள்ளும் வடிவமாக மாற்றுகிறது.

1. அடுத்து எங்கள் கிளையண்ட் குறியீட்டை இதைப் பயன்படுத்த மாற்றுவோம்:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    MCP கருவி பதிலை LLM க்கு அளிக்க `convert_to_llm_tool` அழைப்பை சேர்த்தோம்.

#### .NET

1. MCP கருவி பதிலை LLM புரிந்துகொள்ளும் வடிவமாக மாற்றுவதற்கான குறியீடுதான் இதோ:

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

மேலுள்ள குறியீட்டில்:

- `ConvertFrom` என்ற செயல்பாடு உருவாக்கப்பட்டுள்ளது, இது பெயர், விளக்கம் மற்றும் உள்ளீடு திட்டவட்டத்தை எடுத்துக்கொள்கிறது.
- `FunctionDefinition` உருவாக்கி அதை `ChatCompletionsDefinition`க்கு வழங்குகிறது. இது LLM புரிந்துகொள்ளக்கூடிய வடிவம்.

1. இதை பயனுள்ளதாக மாற்ற `run` போன்ற கொடிகளை மாற்றுவோம்:

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
// இயற்கை மொழி தொடர்பிற்கான ஒரு பாட் இடைமுகத்தை உருவாக்கவும்
public interface Bot {
    String chat(String prompt);
}

// LLM மற்றும் MCP கருவிகளுடன் AI சேவையை கட்டமைக்கவும்
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

மேலுள்ள குறியீட்டில்:

- இயற்கை மொழி தொடர்புகளுக்கு சுலபமான `Bot` இடைமுகம் வரையறுக்கப்பட்டுள்ளது
- LangChain4j இன் `AiServices` மூலம் LLM மற்றும் MCP கருவி வழங்குநரை தானாக இணைக்கிறது
- கட்டமைப்பு கருவி திட்டவட்ட மாற்றம் மற்றும் செயல்பாடுகள் அழைப்பை பின்னணியில் கவனித்துக்கொள்கிறது
- இந்த அணுகுமுறை கைமுறை கருவி மாற்றத்தை நிறுத்தி MCP கருவிகளை LLM-ஆக மாற்றுவதில் உள்ள சிக்கலை LangChain4j கையாள்கிறது

#### Rust

MCP கருவி பதிலை LLM புரிந்துகொள்ளும் வடிவாக மாற்ற உதவும் உதவிகார செயல்பாடை `main.rs` இல் `main` செயலுக்கு கீழே சேர்க்கவும். இது LLM க்கு கோரிக்கை செய்யும் போது அழைக்கப்படும்:

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

சிறந்தது, பயனர் கோரிக்கைகளை கையாள தயாராகோம், அதற்கு அடுத்து முனையலாம்.

### -4- பயனர் பிராம்ப்ட் கோரிக்கையை கையாளல்

இந்த பகுதியில், பயனர் கோரிக்கைகளை கையாளுவோம்.

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

    மேலுள்ள குறியீட்டில்:

    - `callTools` என்ற முறை சேர்க்கப்பட்டுள்ளது.
    - LLM பதிலைக் கொண்டு எந்த கருவிகள் அழைக்கப்பட்டுள்ளன என்பதை சரிபார்க்கும்.

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // கருவியை அழைக்கவும்
        }
        ```

    - LLM கருவி அழைக்க வேண்டும் என்றால் அதை அழைக்கும்:

        ```typescript
        // 2. சர்வரின் கருவியை அழைக்கவும்
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. முடிவுடன் ஏதாவது செய்க
        // செய்யவேண்டியது
        ```

1. `run` முறையை LLM அழைப்பும் `callTools` அழைப்பும் சேர்க்கும் முறையில் புதுப்பிக்கவும்:

    ```typescript

    // 1. LLM க்கான உள்ளீடாக இருக்கும் செய்திகள் உருவாக்கவும்
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
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM பதிலை ஊர்முகமாகப் பார்த்து, ஒவ்வொரு தேர்விலும் டூல் அழைப்புகள் உள்ளதா என்று சரிபார்க்கவும்
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

சிறந்தது, முழு குறியீட்டை இங்கேப் பார்க்கலாம்:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // குறிச்சொல் சரிபார்ப்பாக zod ஐ இறக்குமதி செய்க

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // எதிர்காலத்தில் இ-url மாற்றக்கூடும்: https://models.github.ai/inference
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
          // உள்ளீட்டுக் கோவையின் அடிப்படையில் ஒரு zod குறிச்சொல்லை உருவாக்குக
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // தெளிவாக வகையை "function" ஆக அமைக்கு
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
    
    
          // 2. சேவையின் கருவியை அழைக்கவும்
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. பெறுபேற்றுடன் ஏதாவது செய்க
          // செய்யப்பட வேண்டும்
    
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
    
        // 1. LLM பதிலையெல்லா கவனித்துப் பார்க்கவும், ஒவ்வொரு தேர்விலும் கருவி அழைப்புகள் உள்ளதா என்று சோதிக்கவும்
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

1. LLM அழைக்கும் செயல்பாட்டை சேர்க்கவும்:

    ```python
    # LLM

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

    இதில்:

    - MCP சர்வரில் கண்டுபிடித்த செயல்பாடுகளை LLM க்கு வழங்கினோம்.
    - LLM ஐ அந்த செயல்பாடுகளோடு அழைத்தோம்.
    - பதிலைத் தீவிரமாகப் பற்றி தேவையான செயல்பாடுகளை அழைக்க முடிவு செய்தோம்.
    - கடைசியில் அழைக்கவேண்டிய செயல்பாடுகளின் பட்டியலை வழங்கினோம்.

1. இறுதி படி, பிரதானக் குறியீட்டை புதுப்பிக்கவும்:

    ```python
    prompt = "Add 2 to 20"

    # LLM-க்கு எந்த கருவிகள் எல்லாம் வேண்டும் என்று கேளுங்கள், இருந்தால்
    functions_to_call = call_llm(prompt, functions)

    # பரிந்துரைக்கப்பட்ட செயல்பாடுகளை அழைக்கவும்
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    இங்கு நாங்கள்:

    - MCP கருவியை `call_tool` மூலம் LLM நினைத்த செயல்பாட்டை பயன்படுத்தி அழைக்கிறோம்.
    - கருவி அழைப்பின் முடிவை MCP சர்வருக்கு அச்சிடுகிறோம்.

#### .NET

1. LLM பிராம்ப்ட் கோரிக்கை செய்வதற்கான குறியீடு:

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

    இதில்:

    - MCP சர்வரிலிருந்து கருவிகளை பெற்றோம், `var tools = await GetMcpTools()`.
    - பயனர் பிராம்ப்ட் `userMessage` ஐ வரையறுத்தோம்.
    - மாடல் மற்றும் கருவிகளை குறிப்பிடும் விருப்பங்கள் உருவாக்கப்பட்டன.
    - LLM க்கு கோரிக்கை அனுப்பினோம்.

1. கடைசி படி, LLM செயல்பாட்டை அழைக்க வேண்டுமா என்று பார்க்கலாம்:

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

    இதில்:

    - செயல்பாடு அழைப்புகளின் பட்டியலை சுற்றி வந்தோம்.
    - ஒவ்வொரு கருவி அழைப்பிலும் பெயர் மற்றும் அளவுருக்களை எடுத்து MCP கிளையண்டைப் பயன்படுத்தி அதனை அழைத்தோம், முடிவை அச்சிட்டோம்.

முழு குறியீட்டைப் பாருங்கள்:

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
    // இயல்பான மொழி கோரிக்கைகளை இயங்க செய்யவும், அது தானாகவே MCP கருவிகளை பயன்படுத்தும்
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

இதில்:

- MCP சர்வர் கருவிகளுடன் இயற்கை மொழி பிராம்ப்ட்களை பயன்படுத்தி தொடர்பு கொண்டோம்
- LangChain4j கட்டமைப்பு தானாக கையாள்கிறது:
  - தேவையாயின் பயனர் பிராம்ப்ட்களை கருவி அழைப்பாக மாற்றுதல்
  - LLM முடிவின் அடிப்படையில் சரியான MCP கருவிகளை அழைத்தல்
  - LLM மற்றும் MCP சர்வர் இடையேயான உரையாடல் ஓட்டத்தை நிர்வகித்தல்
- `bot.chat()` இயற்கை மொழி பதில்களை வழங்குகிறது, அவற்றில் MCP கருவிகள் இயக்கிய முடிவுகள் இருக்கலாம்
- இது பயனர்களுக்கு MCP பின்புலத்தை அறிந்திருக்க தேவையில்லாமல் சீரான அனுபவத்தை வழங்குகிறது

முழுமையான குறியீட்டு உதாரணம்:

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

இங்கேப் பெரும்பாலான வேலை நடக்கிறது. முதலில் பயனர் பிராம்ப்டுடன் LLM அழைப்போம், பின்னர் பதிலைப் பார்த்து எந்த கருவிகள் அழைக்க வேண்டும் என்பதை கணிதமிடுவோம். அப்படியானால் அவற்றை அழைத்து, பின்னர் LLM உடன் உரையாடலை தொடர்வோம், அவசியமில்லாமல் கருவிகள் அழைப்புகள் முடிந்ததும் இறுதி பதிலைப் பெறுவோம்.

நாங்கள் பலமுறை LLM ஐ அழைப்போம், ஆகவே LLM அழைப்பை கையாளும் செயல்பாட்டை வரையறுப்போம். கீழ்காணும் செயல்பாட்டை உங்கள் `main.rs` கோப்பில் சேர்க்கவும்:

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

இந்த செயல்பாடு LLM கிளையண்ட், செய்திகளின் பட்டியல் (பயனர் பிராம்ப்டுடன்), MCP சர்வர் கருவிகள் எடுத்துக்கொண்டு LLM க்கு கோரிக்கை அனுப்பி பதிலை திருப்பி தருகிறது.
LLM இருந்து வரும் பதில் `choices` எனும் தொகுப்பை கொண்டிருக்கும். எந்தவொரு `tool_calls` உள்ளதா எனற் பார்க்க அந்த முடிவை செயலாக்க வேண்டியிருக்கிறது. LLM ஒரு குறிப்பிட்ட கருவி அழைக்கவும் அதன் arguments உடன் வேண்டுமென்று வேண்டி இருக்கிறதும் இதனால் தெரியும். LLM பதிலை கையாள ஒரு function ஐ வரையறுக்க கீழே உள்ள குறியீட்டை உங்கள் `main.rs` கோப்பில் இப்படிச் சேர்க்கவும்:

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

    // உள்ளடக்கம் கிடைக்குமானால் அச்சிடு
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // கருவி அழைப்புகளை கையாளவும்
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // உதவியாளர் செய்தியை இணைக்கவும்

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

            // கருவி முடிவுகளை செய்திகள் ஒன்றுகூடச் செய்யவும்
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // கருவி முடிவுகளுடன் உரையாடலை தொடரவும்
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

`tool_calls` இருந்தால், அது கருவி தகவலை எடுத்து, MCP சேவைக்கு கருவி கோரிக்கையுடன் அழைக்கிறது, பின்னர் அதன் முடிவுகளை உரையாடல் செய்திகளுடன் சேர்க்கிறது. அதன் பின் LLM உடன் உரையாடல் தொடர்ந்து இருக்கும் மற்றும் உதவியாளர் பதில் மற்றும் கருவி அழைப்பு முடிவுகளுடன் செய்திகள் புதுப்பிக்கப்படும்.

MCP அழைப்புகளுக்கு LLM வழங்கும் கருவி அழைப்பு தகவலை எடுக்க, அழைப்பை செய்ய தேவையான அனைத்தையும் எடுக்க மற்றொரு உதவி function ஐ சேர்க்க வேண்டும். அதை உங்கள் `main.rs` கோப்பின் அடிப்பகுதியில் கீழ்காணும் குறியீட்டைச் சேர்க்கவும்:

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

அனைத்து பகுதிகளும் ஒருங்கிணைக்கப்பட்டவுடன், முதலில் பயனர் கேள்வியை கையாளி LLM அழைக்கலாம். இதற்காக உங்கள் `main` function ஐ கீழ்காணும் குறியீடுக்களுடன் புதுப்பிக்கவும்:

```rust
// கருவி அழைப்புகளுடன் LLM பேச்சு
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

இது முதன்முதலில் பயனர் கேள்வியைப் படிக்கும் போது இரு எண்களின் கூட்டை கேட்டுக் LLM ஐ அழைக்கிறது மற்றும் பதிலை செயலாக்கி கருவி அழைப்புகளை தானாக கையாளும்.

சிறப்பாக உள்ளது, நீங்கள் முடித்துவிட்டீர்கள்!

## பணிகள்

உதய விரிவாக்கத்திலிருந்து குறியீட்டை எடுத்து சேவையகத்தை மேலான கருவிகள் உடன் உருவாக்கவும். பின்னர் அது போல் ஒரு LLM உடை கிளையன்டை உருவாக்கி, பல்வேறு கேள்விகளுடன் சோதனை செய்து உங்கள் சேவையக கருவிகள் அனைத்தும் தானாகவே அழைக்கப்படுவதை உறுதிப்படுத்தவும். இப்படியான கிளையன்ட் கட்டமைப்பு இறுதி பயனாளிக்கு சிறந்த பயனர் அனுபவத்தை தரும்; அவர்கள் துல்லியமான கிளையன்ட் கட்டளைகளை பயன்படுத்தாமல் கேள்விகளுடன் பயன்படுத்திற்றுக் கொள்ள முடியும் மற்றும் எந்த MCP சேவையை அழைக்கப்படுகிறதோ அது தெரியாது.

## தீர்வு

[Solution](./solution/README.md)

## முக்கியக் குறிப்புகள்

- உங்கள் கிளையன்டில் LLM ஐச் சேர்ப்பது MCP சேவையாளர்களுடன் பயனர்களுக்கு சிறந்த தொடர்பு முறையை வழங்கும்.
- MCP சேவையகத்தின் பதிலை LLM புரிந்துகொள்ளக்கூடிய வடிவில் மாற்ற வேண்டும்.

## உதாரணங்கள்

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## மேலதிக வளங்கள்

## அடுத்தது என்ன?

- அடுத்தது: [Visual Studio Code பயன்படுத்தி ஒரு சேவையகத்தைப் பயன்படுத்துதல்](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**தவறான தெரிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டது. நموږால் துல்லியத்தை உறுதி செய்ய முயற்சித்துள்ளோம், இருப்பினும், இயந்திர மொழிபெயர்ப்புகளில் பிழைகள் அல்லது துல்லியக்குறைவுகள் இருக்க வாய்ப்பு உள்ளது. சொந்த மொழியில் உள்ள அசல் ஆவணம் அதிகாரப்பூர்வ வளமாக கருதப்பட வேண்டும். மிக முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டினால் ஏற்படும் எந்த தவறான புரிதலோ அல்லது தவறோ க்காக நாங்கள் பொறுப்பாளர்கள் அல்ல.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->