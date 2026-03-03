# LLM உடன் கிளையன்டை உருவாக்குதல்

இன்னும் வரை, நீங்கள் ஒரு சர்வர் மற்றும் ஒரு கிளையன்டை எப்படி உருவாக்குவது என்று பார்த்துள்ளீர்கள். கிளையன்ட் சர்வரை நேரடியாக அழைத்து அதன் கருவிகள், வளங்கள் மற்றும் கட்டளைகளை பட்டியலிட முடிந்தது. ஆனால், இது ஒரு சிறந்த வழி அல்ல. உங்கள் பயனர்கள் ஏஜென்டிக் காலத்தில் வாழ்கின்றனர் மற்றும் அவர்கள் கட்டளைகளை பயன்படுத்தி மற்றும் ஒரு LLM உடன் தொடர்பு கொள்ள எதிர்பார்க்கின்றனர். அவர்கள் உங்கள் திறன்களை MCP-ல் சேமிப்பதா இல்லையா என்பதை கவலைப்பட மாட்டார்கள்; அவர்கள் இயல்பான மொழியைப் பயன்படுத்தி மட்டுமே தொடர்பு கொள்ள எதிர்பார்க்கின்றனர். இதை எப்படி தீர்வுசெய்வது? தீர்வு என்பது LLM-ஐ கிளையன்டில் சேர்ப்பதே.

## கண்ணோட்டம்

இந்த பாடத்தில், நாம் உங்கள் கிளையன்டை செய்யும் LLM சேர்க்கும் செயல்முறையை கவனித்து, இது உங்கள் பயனருக்கு எவ்வாறு சிறந்த அனுபவத்தை வழங்குகிறது என்பதை காண்போம்.

## கற்றல் குறிக்கோள்கள்

இந்த பாடம் முடிவில், நீங்கள்:

- LLM கொண்ட கிளையன்டை உருவாக்க முடியும்.
- MCP சர்வர் உடன் LLM பயன்படுத்தி சீரான தொடர்பு கொள்ள முடியும்.
- கிளையன்டின் பக்கத்தில் சிறந்த இறுதி பயனர் அனுபவத்தை வழங்க முடியும்.

## அணுகுமுறை

நாம் எடுக்க வேண்டிய அணுகுமுறையை புரிந்து கொள்ள முயற்சிக்கலாம். LLM சேர்ப்பது எளிது போல இருக்கிறது, ஆனால் நாங்கள் உண்மையில் இதை செய்வோமா?

கீழ்க்காணும் விதத்தில் கிளையன்ட் சர்வருடன் தொடர்பு கொள்வது:

1. சர்வருடன் இணைப்பை ஏற்படுத்துதல்.

1. திறன்கள், கட்டளைகள், வளங்கள் மற்றும் கருவிகளை பட்டியலிட்டு, அவற்றின் ஸ்கீமாவை சேமித்தல்.

1. LLM-ஐச் சேர்த்து, சேமிக்கப்பட்ட திறன்கள் மற்றும் அவற்றின் ஸ்கீமாவை LLM புரிந்துகொள்ளும் வடிவில் வழங்குதல்.

1. பயனர் கட்டளையை LLM-க்கு, மற்றும் கிளையன்ட் பட்டியலிடும் கருவிகளுடன் அனுப்பி கவனித்தல்.

சரி, இப்போது நாம் இது எவ்வாறு மேம்படுத்துவது என்பதைக் கிளியர்களுடன் புரிந்துகொண்டோம், கீழே உள்ள பயிற்சியில் முயற்சிப்போம்.

## பயிற்சி: LLM கொண்ட கிளையன்டை உருவாக்குதல்

இந்த பயிற்சியில், நாங்கள் எவ்வாறு LLM-ஐ கிளையன்டில் சேர்க்கலாம் என்று கற்றுக்கொள்வோம்.

### GitHub Personal Access Token மூலம் அங்கீகாரம்

GitHub டோக்கன் உருவாக்குவது நேரடியான செயல். இதோ எப்படி செய்யலாம்:

- GitHub அமைப்புக்களில் செல்ல – உங்கள்தான படத்தை மேல்துலையில் உள்ள இடது மூலை பகுதியில் கிளிக் செய்து Settings-ஐ தேர்ந்தெடுக்கவும்.
- Developer Settings-க்கு செல்ல – கீழே சரு செய்து Developer Settings-ஐ கிளிக் செய்யவும்.
- Personal Access Tokens-ஐத் தேர்ந்து கொள்ளவும் – Fine-grained tokens-ஐ கிளிக் செய்து Generate new token என்பதைக் கிளிக் செய்யவும்.
- உங்கள் டோக்கனை அமைக்கவும் – குறிப்பு சேர்க்கவும், கால அவகாசத்தை அமைக்கவும் மற்றும் தேவையான அனுமதிகளை (scopes) தேர்ந்தெடுக்கவும். இதில் Models உரிமையை சேர்க்க தவறாதீர்கள்.
- டோக்கனை உருவாக்கி நகலெடுக்கவும் – Generate token ஐ கிளிக் செய்து உடனே டோக்கனை நகலெடுக்கவும், ஏனெனில் மறுபடியும் அதை பார்க்க முடியாது.

### -1- சர்வருடன் இணைவு கொள்ளுதல்

முதலில் நம்மோடு கிளையன்டை உருவாக்குவோம்:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ஸ்கீமா சரிபார்ப்பிற்காக zod ஐ இறக்குமதி செய்க

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

மேலுள்ள குறியீட்டில்:

- தேவையான நூலகங்களை இறக்குமதி செய்துள்ளோம்
- `client` மற்றும் `openai` என்ற இரண்டு உறுப்பினர்கள் கொண்ட ஒரு வகுப்பை உருவாக்கி, கிளையன்டையும் LLM உடன் தொடர்பு கொள்ள உதவுகிறது.
- LLM எடுத்துக்காட்டை GitHub Models பயன்படுத்தக்கூடியவாறு `baseUrl`-ஐ inference API-க்கு அமைத்துள்ளோம்.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio இணைப்புக்கான சர்வர் பராமிதிகளை உருவாக்கு
server_params = StdioServerParameters(
    command="mcp",  # இயங்கு கோப்பு
    args=["run", "server.py"],  # விருப்பமான கட்டளை வரி argumento்கள்
    env=None,  # விருப்பமான சூழல் மாறிகள்
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # இணைப்பைத் துவக்கு
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

மேலுள்ள குறியீட்டில்:

- MCP க்கான தேவையான நூலகங்களை இறக்குமதி செய்துள்ளோம்
- ஒரு கிளையன்டை உருவாக்கியுள்ளோம்

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

முதல், உங்கள் `pom.xml` கோப்பில் LangChain4j சார்ந்த சார்புகளைச் சேர்க்க வேண்டும். MCP ஒருங்கிணைவு மற்றும் GitHub Models ஆதரவுக்கான சார்புகள் இவைகள்:

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

பிறகு உங்கள் ஜாவா கிளையன்ட் வகுப்பை உருவாக்கவும்:

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
    
    public static void main(String[] args) throws Exception {        // LLM ஐ GitHub மாதிரிகள் பயன்படுத்தக் கட்டமைக்கவும்
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // சர்வரில் இணைக்க MCP போக்குவரத்தை உருவாக்கவும்
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

மேலுள்ள குறியீட்டில்:

- MCP ஒருங்கிணைவு, OpenAI அதிகாரப்பூர்வ கிளையன்ட் மற்றும் GitHub Models ஆதரவுக்கான LangChain4j சார்புகள் சேர்க்கப்பட்டுள்ளன
- MCP ஒருங்கிணைவு மற்றும் OpenAI சந்தை மாதிரி செயல்பாட்டிற்கு LangChain4j நூலகங்கள் இறக்குமதி செய்யப்பட்டுள்ளன
- உங்கள் GitHub டோக்கன் கொண்டு GitHub Models பயன்படுத்த `ChatLanguageModel` உருவாக்கப்பட்டுள்ளதுடன், HTTP பிணைய இணைப்புக்கு Server-Sent Events (SSE) பயன்படுத்தப்பட்டுள்ளது
- MCP சர்வருடன் தொடர்புக்கு MCP கிளையன்ட் உருவாக்கப்பட்டுள்ளது
- LLM கள் மற்றும் MCP சர்வர்களுக்கு இடையேயான ஒருங்கிணைப்பை எளிதாக்கும் LangChain4j இன் உருவாக்கப்பட்ட MCP ஆதரவு பயன்படுத்தப்பட்டுள்ளது

#### Rust

இந்த எடுத்துக்காட்டு Rust அடிப்படையிலான MCP சர்வர் இயங்கி இருக்க வேண்டும் என்ற நிபந்தனையுடன் உள்ளது. இல்லையெனில், [01-first-server](../01-first-server/README.md) பாடத்திற்குச் சென்று சர்வரை உருவாக்கவும்.

Rust MCP சர்வர் இருந்தால், டெர்மினல் திறந்து அதன் கோப்புறை நோக்கி செல்லவும். பின்வரும் கட்டளையை இயக்கி புதிய LLM கிளையன்ட் திட்டத்தை உருவாக்கவும்:

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
> OpenAI க்கான அதிகாரப்பூர்வ Rust நூலகமில்லை; இருப்பினும் `async-openai` crate என்பது பொதுமக்கள் பராமரிக்கும் நூலகமாகும் ([மேலும் தகவல்](https://platform.openai.com/docs/libraries/rust#rust)).

`src/main.rs` கோப்பை திறந்து கீழ்க்காணும் குறியீட்டுடன் மாற்றவும்:

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

    // செய்யவேண்டியது: MCP கருவி பட்டியலை பெறுக

    // செய்யவேண்டியது: கருவி அழைப்புகளுடன் LLM உரையாடல்

    Ok(())
}
```

இந்த குறியீடு ஒரு அடிப்படை Rust செயலியை அமைக்கிறது, இது MCP சர்வர் மற்றும் GitHub Models உடன் LLM தொடர்பு கொண்டு செயல்படும்.

> [!IMPORTANT]
> செயலியை இயக்கும் முன், உங்கள் GitHub டோக்கனுடன் `OPENAI_API_KEY` சுற்றுச்சூழல் மாறியைக் கட்டாயமாக அமைக்கவும்.

சரி, அடுத்த படிக்கு, சர்வரின் திறன்களை பட்டியலிடுவோம்.

### -2- சர்வர் திறன்களை பட்டியலிடுதல்

இதோ சர்வருடன் இணைந்து அதன் திறன்களை கேட்கலாம்:

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

    // கருவிகளை பட்டியலிடுதல்
    const toolsResult = await this.client.listTools();
}
```

மேலுள்ள குறியீட்டில்:

- சர்வருடன் இணைப்பதற்கான `connectToServer` குறியீடு சேர்க்கப்பட்டுள்ளது.
- `run` என்ற ஒரு முறையை உருவாக்கியுள்ளோம்; இதுவரை அது கருவிகளை மட்டுமே பட்டியலிடுகிறது, பின்னர் மேலும் செயற்பாடுகளைச் சேர்ப்போம்.

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

இங்கே சேர்த்தது:

- வளங்கள் மற்றும் கருவிகளை பட்டியலிட்டு அச்சிடுதல். கருவிகளுக்கு `inputSchema` பற்றியும் பட்டியலிட்டோம்.

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

மேலுள்ள குறியீட்டில்:

- MCP சர்வரில் உள்ள கருவிகளை பட்டியலிட்டோம்
- ஒவ்வொரு கருவிக்கும் பெயர், விளக்கம் மற்றும் அதனுடைய ஸ்கீமா பட்டியலிடப்பட்டது. இந்த ஸ்கீமா கருவிகளை அழைக்கும் போது பயன்படுத்தப்பட உள்ளது.

#### Java

```java
// MCP கருவிகளைக் தானாக கண்டுபிடிக்கும் ஒரு கருவி வழங்கியமை படைக்கவும்
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP கருவி வழங்கியமை தானாக கையாள்கிறது:
// - MCP சேவையகம் இருந்து கிடைக்கும் கருவிகளின் பட்டியல்
// - MCP கருவி ஸ்கீமாக்களை LangChain4j வடிவிற்கு மாற்றுதல்
// - கருவி செயலாக்கம் மற்றும் பதில்கள் நிர்வகிப்பு
```

மேலுள்ள குறியீட்டில்:

- MCP சர்வரில் இருந்து அனைத்து கருவிகளையும் தானாக கண்டறிந்து பதிவு செய்யும் `McpToolProvider` உருவாக்கப்பட்டது
- கருவி வழங்குநர் MCP கருவி ஸ்கீமாவையும் LangChain4j கருவித் தள வடிவிலும் உள்ளமைப்பை மாற்று செய்கிறது
- கருவிகளை கையேடு பட்டியலிட்டு மாற்றும் பணியை இவ்வாறு தானாக கையாளும்

#### Rust

MCP சர்வரிடமிருந்து கருவிகளை பெற `list_tools` முறையை பயன்படுத்தலாம். `main` செயல்பாட்டில் MCP கிளையன்டை அமைத்த பிறகு, பின்வரும் குறியீட்டை சேர்க்கவும்:

```rust
// MCP கருவி பட்டியலை பெறுக
let tools = mcp_client.list_tools(Default::default()).await?;
```


### -3- சர்வர் திறன்களை LLM கருவிகளாக மாற்றுதல்

திறன்களை பட்டியலிட்ட பிறகு, அவற்றை LLM புரிந்துகொள்ளும் வடிவிற்கு மாற்ற வேண்டும். அப்படிச் செய்த பின், இவை LLM க்கு கருவிகளாக வழங்கப்படலாம்.

#### TypeScript

1. MCP சர்வர் பதிலை LLM க்கு பொருந்தும் கருவி வடிவுக்கு மாற்ற பின்வரும் குறியீட்டை சேர்க்கவும்:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // உள்ளீடு_schema அடிப்படையில் ஒரு zod திட்டத்தை உருவாக்கவும்
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // வகையை தெளிவாக "function" ஆகவும் நிர்ணயிக்கவும்
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

    மேற்கண்ட குறியீடு MCP சர்வர் பதிலை எடுத்துக் கொண்டு LLM புரிந்துகொள்ளும் கருவி வரையறைக்கும் வடிவிற்கு மாற்றுகின்றது.

1. அடுத்து `run` முறையை மாற்றி சர்வர் திறன்களை பட்டியலிடுவோம்:

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

    மேலே நாம் `run` முறையில் MCP பதிலின் ஒவ்வொரு உருப்படியையும் `openAiToolAdapter` மூலம் மாற்றியுள்ளோம்.

#### Python

1. முதலில் கீழ்காணும் மாற்றி செயல்பாட்டை உருவாக:

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

    `convert_to_llm_tools` என்ற செயல்பாடு MCP கருவி பதிலை எடுத்துக் கொண்டு LLM புரிந்துகொள்ளும் வடிவிற்கு மாற்றுகிறது.

1. பின்னர், கிளையன்டில் இதைப் பயன்படுத்தவும்:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    இங்கே MCP கருவி பதிலை LLM க்கு வழங்க LLM கருவிகளாக மாற்றும் செயல்பாட்டை அழைக்கின்றோம்.

#### .NET

1. MCP கருவி பதிலை LLM புரிந்துகொள்ளும் வடிவிற்கு மாற்ற குறியீட்டைக் கீழேச் சேர்க்கவும்:

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

மேலே:

- பெயர், விளக்கம் மற்றும் உள்ளீட்டு ஸ்கீமாவுடன் `ConvertFrom` செயல்பாடு உருவாக்கப்பட்டது.
- `FunctionDefinition` உருவாக்கி `ChatCompletionsDefinition` -க்கு வழங்கும் செயல்பாடு சேர்க்கப்பட்டுள்ளது.

1. இதை பயன்படுத்த `run` போன்ற குறியீட்டை புதுப்பிக்கலாம்:

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
// இயற்கை மொழி பரிமாற்றத்திற்கு ஒரு பாட்டை இடைமுகமாக உருவாக்கவும்
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

- இயல்பான மொழி தொடர்புக்கு எளிய `Bot` இடைமுகத்தை வரையறுத்தோம்
- LangChain4j இன் `AiServices` மூலம் LLM மற்றும் MCP கருவி வழங்குநரை தானாக இணைத்தோம்
- கருவி ஸ்கீமா மாற்று மற்றும் செயல்பாடுகள் அழைப்பை தானாக ஸ்வயமாக்குகிறது
- இதனால் MCP கருவிகளை LLM பொருந்தும் வடிவிற்கு மாற்றப்படுவது கையாளப்படுகிறது

#### Rust

MCP கருவி பதிலை LLM புரிந்துகொள்ளும் வடிவிற்கு மாற்ற உதவும் செயல்பாட்டை `main.rs` இல் `main` செயல்பாட்டிற்கு கீழ் சேர்க்கவும். இது LLMக்கு கோரிக்கை செய்யும்போது பயன்படுத்தப்படும்:

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

சரி, தற்போது நாம் பயனர் கோரிக்கைகளை கையாள சில குறியீடு சேர்க்கவேண்டும்.

### -4- பயனர் கட்டளையை கையாளுதல்

இந்த பகுதியிலும் பயனர் கோரிக்கைகளை நாம் கையாளப்போகின்றோம்.

#### TypeScript

1. LLM அழைப்புக்கு பயன்படுத்தும் முறையைச் சேர்க்கவும்:

    ```typescript
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

        // 3. பெறுபேறுடன் ஒரு வேலை செய்யவும்
        // செய்ய வேண்டியது

        }
    }
    ```

    மேலே:

    - `callTools` என்ற ஒரு முறையைச் சேர்ந்தோம்.
    - LLM பதிலைப் பெற்று, எந்த கருவிகள் அழைக்கப்படாதென்கின்றது என்பதைச் சரிபார்க்கிறது:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // கருவியை அழைக்கவும்
        }
        ```

    - LLM கூறியபடி கருவிகளை அழைக்கிறது:

        ```typescript
        // 2. சர்வரின் கருவியை அழைக்கவும்
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. முடிவுடன் ஏதாவது செய்யவும்
        // செய்ய வேண்டியது
        ```

1. `run` முறையை LLM அழைக்கும், பின்னர் `callTools` அழைக்கும் வகையில் புதுப்பிக்கவும்:

    ```typescript

    // 1. LLMக்கான உள்ளீடாக செய்திகள் உருவாக்கவும்
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLMஐ அழைக்கும் மெத்திக்கல்
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM பதிலை ஊர்ந்து, ஒவ்வொரு தேர்வையும், அதனுடன் உள்ள கருவி அழைப்புக்களைச் சரிபார்க்கவும்
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

முழு குறியீட்டை கீழே பாருங்கள்:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // காட்சிமுறை சரிபார்ப்பிற்கு zodஐ இறக்குமதி செய்க

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // எதிர்காலத்தில் இந்த urlக்கு மாற்ற தேவை இருக்கலாம்: https://models.github.ai/inference
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
          // input_schema அடிப்படையில் zod காட்சிமுறையை உருவாக்குக
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // வகையை "function" என்று தெளிவாக அமைக்கவும்
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
    
    
          // 2. சேவையகத்தின் கருவியை அழைக்கவும்
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. பெறுபடிக்கு ஏதாவது செய்க
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM பதிலின் ஒவ்வொரு தேர்வையும் பார்த்து, அதில் கருவி அழைப்புகள் உள்ளனவா என்று சரிபார்க்கவும்
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

1. LLM அழைப்புக்கு தேவையான இறக்குமதிகளைச் சேர்க்கவும்:

    ```python
    # எல்எல்எம்
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. இப்போது LLM ஐ அழைக்கும் செயல்பாட்டைச் சேர்க்கவும்:

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

மேலுள்ள குறியீட்டில்:

- MCP சர்வரிலிருந்து பெற்ற செயல்பாடுகள் LLM க்கு வழங்கப்பட்டன.
- பின்னர் அந்த செயல்பாடுகளைப் பயன்படுத்தி LLM அழைக்கப்பட்டது.
- முடிவை ஆய்வு செய்து எந்த செயல்பாடுகளை அழைக்க வேண்டும் என்று கண்டறிந்தோம்.
- கடைசியில் அழைக்க வேண்டிய செயல்பாடுகளின் வரிசை அனுப்பப்பட்டது.

1. இறுதி படி, மெயின் குறியீட்டையும் புதுப்பிக்கவும்:

    ```python
    prompt = "Add 2 to 20"

    # LLMக்கு அனைத்து கருவிகளையும் கேளுங்கள், ஏதேனில்
    functions_to_call = call_llm(prompt, functions)

    # பரிந்துரைக்கப்பட்ட செயல்பாடுகளை அழைக்கவும்
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

மேலே:

- LLM கொடுத்த கருவி செயல்பாட்டைப் பயன்படுத்தி MCP கருவியை `call_tool` வழியாக அழைக்கின்றோம்.
- MCP சர்வரை நோக்கி கருவி அழைப்பு முடிவையும் அச்சிடுகின்றோம்.

#### .NET

1. LLM கட்டளை கோரிக்கை குறியீட்டைக் காண்போம்:

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

மேலே:

- MCP சர்வரிலிருந்து கருவிகளை பெற்று உள்ளோம் (`var tools = await GetMcpTools()`).
- பயனர் கட்டளை இறையணிகப்பட்டுள்ளது (`userMessage`).
- மாதிரி மற்றும் கருவிகள் உள்ள விருப்ப எதிரொல்லை ஒன்றை உருவாக்கி LLMக்கு கோரிக்கை அனுப்பப்பட்டுள்ளது.

1. இறுதி படி, LLM நினைத்தால் செயல்பாடு அழைக்கப்படும் குறியீடு:

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

மேலே:

- செயல்பாடு அழைப்புகளை ஒருவரும் முறையே சுழற்சியிட்டோம்.
- ஒவ்வொரு கருவி அழைப்பு பெயர் மற்றும் பொருட்களை பிரித்தெடுத்து MCP சர்வரின் MCP கிளையண்ட் மூலம் அதனை அழைத்தோம். முடிவையும் அச்சிட்டோம்.

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

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // தேர்வு செய்யப்படாத MCP கருவிகளை தானாகவே பயன்படுத்தும் இயற்கை மொழி கோரிக்கைகளை செயற்படுத்துக
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

மேலே:

- எளிய இயல்பான மொழிக் கட்டளைகளை MCP சர்வரின் கருவிகளுடன் தொடர்புக்கு பயன்படுத்தியது
- LangChain4j தானாக:
  - பயனர் கட்டளைகளை கருவி அழைப்புகளாக மாற்றுதல்
  - LLM தீர்மானிப்பின்பேரில் MCP கருவிகளை அழைத்தல்
  - LLM மற்றும் MCP சர்வர் இடையேயான உரையாடல் ஓட்டத்தை நிர்வகித்தல்
- `bot.chat()` இயல்பான மொழியிலான பதில்களை վերադարձி, அதில் MCP கருவி செயல்பாட்டு முடிவும் இருக்கும்
- இதன் மூலம் பயனர்கள் MCP உள்ளமைவை அறிய வேண்டாமென்ற அருவான அனுபவம் ஏற்படும்

முழுமையான குறியீடு எடுத்துக்காட்டு:

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

பல வேலைகள் இங்கே நடக்கும். முதலில் பயனர் கட்டளையுடன் LLM அழைக்கப்படும், பிறகு பதிலை எடுத்துக் கொண்டு கருவிகள் அழைக்க வேண்டுமா என்பதை பரிசோதிக்கப்படும். அவ்வாறு இருந்தால் அந்த கருவிகளை அழைத்து, LLM உடன் உரையாடலை தொடர்வோம். மேலும் கருவி அழைப்புகள் தேவையில்லாமல் இறுதிப் பதில் வருவிக்கும் வரை இது நடக்கும்.

பல முறைகள் LLM அழைத்தால், LLM அழைப்பை செயல்படுத்தும் முறையை வரையறுக்கலாம். கீழ்கண்ட செயல்பாட்டை `main.rs` இல் சேர்க்கவும்:

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

இந்த செயல்பாடு LLM கிளையன்டை, செய்தி வரிசை (பயனர் கட்டளையை உள்பட), MCP சர்வர் கருவிகளைப் பெற்று LLMக்கு கோரிக்கை அனுப்பி பதிலைக் கொடுக்கும்.
LLM இல் இருந்து பெறப்படும் பதில் `choices` என்ற வரிசையைப் περιக்கிறது. எந்த `tool_calls` உள்ளது என்பதைப் பார்க்க நாங்கள் முடிவை செயலாக்கவேண்டும். இது LLM ஒரு குறிப்பிட்ட கருவியை வரையறுக்கப்பட்ட பாராமீட்டர்களுடன் அழைக்க வேண்டும் என்பதைக் காட்டுகிறது. LLM பதிலை கையாள ஒரு செயல்பாட்டை வரையறுப்பதற்கு உங்கள் `main.rs` கோப்பு இறுதியில் கீழ்காணும் குறியீட்டை சேர்க்கவும்:

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

    // உள்ளடக்கம் கிடைத்தால் அச்சிடுக
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // கருவி அழைப்புகளை கையாள்க
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // உதவியாளர் 메시்ஐ சேர்க்கவும்

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

            // கருவி முடிவை செய்திகள் கொள்ள சேர்க்கவும்
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
  
`tool_calls` இருந்தால், அது கருவி தகவலைப் பெற்று, MCP சேவையகத்தை கருவி கோரிக்கையுடன் அழைக்கிறது, பிறகு பெறுபடிகளை உரையாடல் செய்திகளில் சேர்க்கிறது. பின்னர் இது LLM உடன் உரையாடலை தொடர்கிறது, உரையாடல் செய்திகளுடன் உதவியாளரின் பதில் மற்றும் கருவி அழைப்பு முடிவுகள் புதுப்பிக்கப்படுகின்றன.

LLM MCP அழைப்புகளுக்கு திருப்பும் கருவி அழைப்பு தகவல்களைப் பெற இன்னொரு உதவித்துறையைச் சேர்ப்போம். அழைப்புக்கு தேவையான அனைத்தையும் எடுக்க இந்த குறியீட்டை உங்கள் `main.rs` கோப்பின் கீழ் சேர்க்கவும்:

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
  
அனைத்து கூறுகளும் உருவாக்கப்பட்ட பிறகு, முதன்மை பயனர் பிராம்ட்டைப் பெற்றுக் கொள்ளவும் LLM அழைக்கவும் செய்யலாம். உங்கள் `main` செயல்பாட்டை கீழ்காணும் குறியீடுடன் புதுப்பிக்கவும்:

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
  
இது ஆரம்ப பயனர் பிராம்ட்டுடன் LLM ஐ கேள்வி செய்கிறது, இரண்டு எண்களின் கூட்டுத்தொகையை கேட்கிறது, பதிலை செயலாக்கி கருவி அழைப்புகளை இடைமுகப்படுத்திக் கையாளும்.

சிறந்தது, நீங்கள் செய்துவிட்டீர்கள்!

## பணிகள்

பயிற்சியில் உள்ள குறியீடுகளை எடுத்துக் கொண்டு, சில கூடுதல் கருவிகளுடன் சேவையகத்தை உருவாக்கவும். பின்னர் LLM கொண்டு ஒரு கிளையண்ட் உருவாக்கி, பயிற்சியில் போலவே பயன்படுத்தி, வெவ்வேறு பிராம்ட்களைச் சோதித்து, உங்கள் சேவையக கருவிகள் அனைத்தும் தனிப்பயனாக அழைக்கப்படுகிறதா என்பதை உறுதிப்படுத்துங்கள். இப்படிப் புரியக்கூடிய UI-ஐ உருவாக்கி, பயனர்கள் சரியான கிளையண்ட் கட்டளைகளைப் பயன்படுத்தாமல், ப்ராம்ட் மொழியில் இலகுவாக இயங்கலாம் மற்றும் எந்த MCP சேவையக அழைப்பும் தெரியாமல் இருக்கும்.

## தீர்வு

[தீர்வு](/03-GettingStarted/03-llm-client/solution/README.md)

## முக்கிய கருத்துக்கள்

- உங்கள் கிளையண்டில் LLM சேர்ப்பது MCP சேவையகங்களுடன் பயனர்களுக்கு சிறந்த தொடர்பை வழங்குகிறது.
- MCP சேவையக பதிலை LLM புரிந்துகொள்ளக்கூடிய வடிவிலுக்கு மாற்ற வேண்டியிருக்கும்.

## மாதிரிகள்

- [ஜாவா கணக்கர்](../samples/java/calculator/README.md)
- [.Net கணக்கர்](../../../../03-GettingStarted/samples/csharp)
- [ஜாவாஸ்கிரிப்ட் கணக்கர்](../samples/javascript/README.md)
- [டைப் ஸ்கிரிப்ட் கணக்கர்](../samples/typescript/README.md)
- [பைத்தான் கணக்கர்](../../../../03-GettingStarted/samples/python)
- [ராக்ஸ் கணக்கர்](../../../../03-GettingStarted/samples/rust)

## கூடுதல் வளங்கள்

## அடுத்தது

- அடுத்தது: [Visual Studio Code பயன்படுத்தி சேவையகத்தை உபயோகிப்பது](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**அறிவிப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்துக்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்க வாய்ப்பு உள்ளது. இதன் தமிழாக்கத்தை விட, முதன்மையான ஆவணம் அதன் சொந்த மொழியில் தவிர்க்கத்தக்க ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டினால் ஏற்படும் எந்த தவறுகள் அல்லது தவறான புரிதல்களுக்கு நாங்கள் பொறுப்புதவையில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->