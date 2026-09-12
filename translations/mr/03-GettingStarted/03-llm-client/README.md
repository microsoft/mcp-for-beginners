# LLM सह क्लायंट तयार करणे

> [!NOTE]
> Java क्लायंट उदाहरणे परंपरागत HTTP+SSE ट्रान्सपोर्ट वापरून जोडले जातात आणि
> MCP `2025-11-25` SDK API लक्ष्य करतात. नवीन रिमोट क्लायंटसाठी `2026-07-28`-सुसंगत SDK आणि
> स्ट्रीम करण्यायोग्य HTTP वापरा.

आतापर्यंत, तुम्ही पाहिलं आहे की सर्व्हर आणि क्लायंट कसे तयार करायचे. क्लायंटने स्पष्टपणे सर्व्हरला कॉल करून त्याच्या टूल्स, संसाधने, आणि प्रॉम्प्ट्सची यादी केली. तथापि, हा फार व्यवहार्य दृष्टिकोन नाही. तुमचे वापरकर्ते एजंटिक युगात राहत आहेत आणि ते प्रॉम्प्ट्स वापरण्याची आणि LLM सोबत संवाद साधण्याची अपेक्षा करतात. त्यांना काळजी नाही की तुम्ही तुमच्या क्षमता साठवण्यासाठी MCP वापरत आहात की नाही; ते फक्त नैसर्गिक भाषेचा वापर करून संवाद साधण्याची अपेक्षा करतात. तर आम्ही हे कसे सोडवतो? सोडवणूक म्हणजे क्लायंटमध्ये LLM जोडणे.

## आढावा

या धड्यात आपण क्लायंटमध्ये LLM कसे जोडायचे ते पाहू आणि हे तुमच्या वापरकर्त्यांसाठी कसे अजून चांगले अनुभव प्रदान करते ते दाखवू.

## शिक्षण उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम व्हाल:

- LLM सह क्लायंट तयार करा.
- LLM वापरून seamless पद्धतीने MCP सर्व्हरशी संवाद साधा.
- क्लायंट बाजूने वापरकर्त्यांना अधिक चांगला अनुभव द्या.

## दृष्टिकोन

चला पाहूया आम्हाला कोणता दृष्टिकोन घ्यायचा आहे. LLM जोडणे सोपे वाटते, पण आपण खरोखरच हे कसे करू?

क्लायंट सर्व्हरशी कसे संवाद साधेल ते खालीलप्रमाणे:

1. सर्व्हरशी कनेक्शन स्थापित करा.

1. क्षमता, प्रॉम्प्ट्स, संसाधने आणि टूल्स यादी करा आणि त्यांचा schema जतन करा.

1. LLM जोडा आणि जतन केलेल्या क्षमता व त्यांचा schema LLM समजेल अशा स्वरूपात द्या.

1. वापरकर्त्याचा प्रॉम्प्ट हाताळा आणि त्याला LLM कडे टूल्सच्या यादीसह पाठवा.

छान, आता आपण उच्चस्तरीय पद्धतीने हे कसे करायचे ते समजलो, चला खालील सरावात हे करून पाहूया.

## सराव: LLM सह क्लायंट तयार करणे

या सरावात, आम्ही आमच्या क्लायंटमध्ये LLM कसे जोडायचे ते शिकू.

### GitHub वैयक्तिक प्रवेश टोकन वापरून प्रमाणीकरण

GitHub टोकन तयार करणे सोपे आहे. असे करा:

- GitHub सेटिंग्जमध्ये जा – वरच्या उजव्या कोपऱ्यातील तुमच्या प्रोफाइल फोटोवर क्लिक करा आणि सेटिंग्ज निवडा.
- Developer सेटिंग्जकडे जा – खाली स्क्रोल करा आणि Developer सेटिंग्जवर क्लिक करा.
- Personal Access Tokens निवडा – Fine-grained tokens वर क्लिक करा आणि नवा टोकन जनरेट करा.
- तुमचा टोकन कॉन्फिगर करा – संदर्भासाठी नोंद जोडा, समाप्ती तारीख सेट करा, आणि आवश्यक परवानग्या निवडा. या बाबतीत Models परवानगी नक्की जोडा.
- टोकन जनरेट करा आणि कॉपी करा – Generate token वर क्लिक करा, आणि लगेच कॉपी करा, कारण पुन्हा ते पाहता येणार नाही.

### -1- सर्व्हरशी कनेक्ट करा

सुरुवातीला आपला क्लायंट तयार करूया:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा प्रमाणनासाठी झोड आयात करा

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

मागील कोडमध्ये आम्ही:

- आवश्यक लायब्ररी आयात केल्या
- एक वर्ग तयार केला ज्यामध्ये `client` आणि `openai` हे दोन सदस्य आहेत जे क्लायंट आणि LLM इंटरेक्शन व्यवस्थापित करण्यास मदत करतील.
- GitHub Models वापरण्यासाठी LLM इन्स्टन्स कॉन्फिगर केले, `baseUrl` ला inference API कडे सेट करून.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio कनेक्शनसाठी सर्व्हर पॅरामीटर्स तयार करा
server_params = StdioServerParameters(
    command="mcp",  # कार्यान्वित करण्यायोग्य
    args=["run", "server.py"],  # ऐच्छिक कमांड लाइन आर्ग्युमेंट्स
    env=None,  # ऐच्छिक पर्यावरणीय चल
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # कनेक्शन प्रारंभ करा
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

मागील कोडमध्ये आम्ही:

- MCP साठी आवश्यक लायब्ररी आयात केल्या
- क्लायंट तयार केला

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

प्रथम, तुम्हाला तुमच्या `pom.xml` फाइलमध्ये LangChain4j dependencies जोडाव्या लागतील. MCP इंटिग्रेशन आणि OpenAI-समर्थित MiniMax APIसाठी या डिपेंडन्सीज जोडा:

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

तुमचा MiniMax API की आणि, पर्यायीपणे, endpoint आणि मॉडेल सेट करा.
`MINIMAX_MODEL_ID` मध्ये `MiniMax-M3` आणि `MiniMax-M2.7` ची मागणी आहे. जर
`OPENAI_BASE_URL` सेट नसेल, तर `MINIMAX_REGION` `global_en` आणि `cn_zh` ला समर्थन देते.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

बदलीने region नुसार endpoint निवडण्यासाठी, `OPENAI_BASE_URL` काढा:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

नंतर तुमचा Java क्लायंट वर्ग तयार करा:

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

        // सर्व्हरशी कनेक्ट होण्यासाठी MCP ट्रान्सपोर्ट तयार करा
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP क्लायंट तयार करा
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

मागील कोडमध्ये आम्ही:

- **LangChain4j dependencies जोडल्या**: MCP इंटिग्रेशन आणि OpenAI-समर्थित MiniMax APIसाठी आवश्यक
- **LangChain4j लायब्ररी आयात केल्या**: MCP इंटिग्रेशन आणि OpenAI चॅट मॉडेल कार्यक्षमता साठी
- **`ChatLanguageModel` तयार केला**: MiniMax वापरण्यासाठी कॉन्फिगर केले, तुमचा MiniMax API की, endpoint, आणि समर्थित मॉडेल आयडीसह
- **HTTP ट्रान्सपोर्ट सेट केला**: Server-Sent Events (SSE) वापरून MCP सर्व्हरशी कनेक्ट होण्यासाठी
- **MCP क्लायंट तयार केला**: जो सर्व्हरशी संवाद हाताळेल
- **LangChain4j ची अंतर्निहित MCP सपोर्ट वापरली**: जी LLM आणि MCP सर्व्हर दरम्यान इंटिग्रेशन सुलभ करते

#### Rust

हे उदाहरण गृहित धरते की तुमच्याकडे Rust आधारित MCP सर्व्हर चालू आहे. जर नसल्यास, सर्व्हर तयार करण्यासाठी [01-first-server](../01-first-server/README.md) धडा पहा.

तुमच्याकडे Rust MCP सर्व्हर असल्यावर, टर्मिनल उघडा आणि सर्व्हरच्या तीच फोल्डरमध्ये जा. नंतर खालील कमांड वापरून नवीन LLM क्लायंट प्रोजेक्ट तयार करा:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

तुमच्या `Cargo.toml` फाइलमध्ये खालीलdependencies जोडा:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI साठी अधिकृत Rust लायब्ररी नाही, पण `async-openai` क्रेट हा [समुदाय-देखरेखीत लायब्ररी](https://platform.openai.com/docs/libraries/rust#rust) आहे जो सामान्यतः वापरला जातो.

`src/main.rs` फाइल उघडा आणि त्याचा मजकूर पुढील कोडने बदला:

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
    // प्राथमिक संदेश
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI क्लायंट सेटअप करा
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP क्लायंट सेटअप करा
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

    // TODO: MCP साधन यादी मिळवा

    // TODO: LLM संभाषण साधन कॉलसह

    Ok(())
}
```

हा कोड बेसिक Rust अनुप्रयोग सेट करतो जो MCP सर्व्हर आणि GitHub Models शी LLM संवादासाठी कनेक्ट होईल.

> [!IMPORTANT]
> अनुप्रयोग चालवण्यापूर्वी `OPENAI_API_KEY` पर्यावरण चल GitHub टोकन सह सेट करा.

छान, पुढील पायरीसाठी चला सर्व्हरवरील क्षमता यादी करूया.

### -2- सर्व्हरच्या क्षमता यादी करा

आता आपण सर्व्हरशी कनेक्ट होऊ आणि त्याच्या क्षमता मागवू:

#### Typescript

त्याच वर्गात खालील मेथड्स जोडा:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // साधने यादी करणे
    const toolsResult = await this.client.listTools();
}
```

मागील कोडमध्ये आम्ही:

- सर्व्हरशी कनेक्शन करण्यासाठी कोड जोडला, `connectToServer`.
- `run` नावाचा एक मेथड तयार केला जो आमच्या अॅप फ्लोची जबाबदारी घेतो. आतापर्यंत तो फक्त टूल्सची यादी करतो पण आम्ही लवकरच यात आणखी काही जोडू.

#### Python

```python
# उपलब्ध साधने यादी करा
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# उपलब्ध उपकरणे यादी करा
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

आम्ही काय जोडले याची यादी:

- संसाधने आणि टूल्सची यादी केली आणि छापले. टूल्ससाठी आम्ही `inputSchema` देखील यादी केली जी नंतर वापरली जाईल.

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

मागील कोडमध्ये आम्ही:

- MCP सर्व्हरवर उपलब्ध टूल्सची यादी केली
- प्रत्येक टूलसाठी नाव, वर्णन आणि त्याचा schema दिला. हे आम्ही लवकरच टूल्स कॉल करण्यासाठी वापरणार आहोत.

#### Java

```java
// एक टूल प्रदाता तयार करा जो आपोआप MCP टूल्स शोधतो
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP टूल प्रदाता आपोआप व्यवस्थापित करतो:
// - MCP सर्व्हरकडून उपलब्ध टूल्सची यादी करणे
// - MCP टूल स्कीमा LangChain4j स्वरूपात रूपांतरित करणे
// - टूलच्या अंमलबजावणी आणि प्रतिक्रियांचे व्यवस्थापन करणे
```

मागील कोडमध्ये आम्ही:

- एक `McpToolProvider` तयार केला जो MCP सर्व्हरवरून सर्व टूल्स स्वयंचलितपणे शोधून नोंदवतो
- टूल प्रदाता अंतर्गत MCP टूल स्कीम्स आणि LangChain4j च्या टूल स्वरूपामधील रूपांतरण हाताळतो
- हा दृष्टिकोन मॅन्युअल टूल यादी आणि रूपांतरण प्रक्रियेला वगळतो

#### Rust

MCP सर्व्हरवरून टूल्स मिळवण्यासाठी `list_tools` मेथडचा वापर करा. तुमच्या `main` फंक्शनमध्ये MCP क्लायंट सेट केल्यानंतर खालील कोड जोडा:

```rust
// MCP टूल सूची मिळवा
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्व्हरची क्षमता LLM टूल्समध्ये रूपांतरित करा

सर्व्हरच्या क्षमता यादी केल्यानंतर पुढचा टप्पा म्हणजे त्यांना LLM समजेल अशा स्वरूपात रूपांतरित करणे. तसे केल्यास आम्ही या क्षमतांना आमच्या LLM साठी टूल्स म्हणून पुरवू शकतो.

#### TypeScript

1. खालील कोड जोडा जे MCP सर्व्हरच्या प्रतिसादाची रूपांतरणे LLM वापरू शकणाऱ्या टूल स्वरूपात करते:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // इनपुट_स्कीमा वर आधारित झोड स्कीमा तयार करा
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // प्रकार स्पष्टपणे "फंक्शन" म्हणून सेट करा
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

    वर दिलेला कोड MCP सर्व्हरच्या प्रतिसादाला LLM समजेल अशा टूल परिभाषेच्या स्वरूपात रूपांतरित करतो.

2. पुढे `run` मेथड अपडेट करू जेणेकरून सर्व्हरच्या क्षमतांची यादी होईल:

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

    मागील कोडमध्ये, आम्ही `run` मेथड अपडेट केली आहे जी परिणामातून प्रत्येक एन्ट्रीसाठी `openAiToolAdapter` कॉल करते.

#### Python

1. प्रथम, खालील कन्व्हर्टर फंक्शन तयार करू:

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

    वर दिलेल्या `convert_to_llm_tools` फंक्शनमध्ये MCP टूल प्रतिसाद घेतला जातो आणि तो LLM समजेल अशा स्वरूपात रूपांतरित होतो.

2. नंतर, आमच्या क्लायंट कोडमध्ये हा फंक्शन वापरायला पुढीलप्रमाणे अपडेट करूया:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    येथे आम्ही `convert_to_llm_tool` कॉल जोडला आहे ज्याने MCP टूल प्रतिसाद LLM ला दिला जाणाऱ्या स्वरूपात बदलतो.

#### .NET

1. MCP टूल प्रतिसाद LLM समजेल अशा स्वरूपात रूपांतरित करणारा कोड जोडा:

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

मागील कोडमध्ये आम्ही:

- `ConvertFrom` नावाचा फंक्शन तयार केला जो नाव, वर्णन आणि इनपुट स्कीमा घेतो.
- ही फंक्शन `FunctionDefinition` तयार करते जी ChatCompletionsDefinition मध्ये जाते. नंतर ही LLM समजेल.

2. नंतर, खालीलप्रमाणे कोड अपडेट करू:

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
// नैसर्गिक भाषा संवादासाठी बॉट इंटरफेस तयार करा
public interface Bot {
    String chat(String prompt);
}

// LLM आणि MCP साधने सह AI सेवा कॉन्फिगर करा
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

मागील कोडमध्ये आम्ही:

- नैसर्गिक भाषेतील संवादासाठी सोपे `Bot` इंटरफेस डिफाइन केला
- LangChain4j च्या `AiServices` वापरून LLM आणि MCP टूल प्रदात्याला आपोआप जोडले
- फ्रेमवर्क स्वयंचलितपणे टूल स्कीमा रूपांतर आणि फंक्शन कॉल हाताळतो
- हा दृष्टिकोन मॅन्युअल टूल रूपांतरण बंद करतो - LangChain4j सर्व क्लिष्टता हाताळतो

#### Rust

MCP टूल प्रतिसाद LLM समजेल अशा स्वरूपात रूपांतरित करण्यासाठी एक सहाय्यक फंक्शन तयार करू. `main.rs` मध्ये `main` फंक्शनखाली खालील कोड जोडा. हा LLM कडे विनंत्या करताना कॉल केला जाईल:

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

छान, आता आपल्याकडे वापरकर्त्याच्या विनंत्या हाताळण्याची तयारी नाही, तर त्यावर काम करूया.

### -4- वापरकर्त्याचा प्रॉम्प्ट विनंती हाताळा

या भागात आपण वापरकर्त्याच्या विनंत्या हाताळणार आहोत.

#### TypeScript

1. LLM कॉल करण्यासाठी एक मेथड जोडा:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. सर्व्हरच्या टूलला कॉल करा
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. निकालासह काहीतरी करा
        // करायचे आहे

        }
    }
    ```

    मागील कोडमध्ये:

    - `callTools` नावाची मेथड जोडली.
    - ही मेथड LLM प्रतिसाद घेते आणि तपासते की कोणते टूल कॉल झालीत का:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // साधन कॉल करा
        }
        ```

    - जर LLM सूचित करत असेल तर टूल कॉल करते:

        ```typescript
        // 2. सर्व्हरच्या साधनाला कॉल करा
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. निकालासह काहीतरी करा
        // करायचे बाकी आहे
        ```

2. `run` मेथड मध्ये LLM कॉल्स आणि `callTools` कॉल समाविष्ट करा:

    ```typescript

    // 1. LLM साठी इनपुट असलेले संदेश तयार करा
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM कॉल करत आहे
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM च्या प्रतिसादातून प्रत्येक पर्याय तपासा, त्यात टूल कॉल आहेत का हे पहा
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

छान, पूर्ण कोड पाहूया:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा व्हॅलिडेशनसाठी zod आयात करा

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // भविष्यात कदाचित ही URL बदलावी लागेल: https://models.github.ai/inference
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
          // इनपुट_स्कीमा वर आधारित zod स्कीमा तयार करा
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // प्रकार स्पष्टपणे "function" सेट करा
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
    
    
          // 2. सर्व्हरचे टूल कॉल करा
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. परिणामासह काहीतरी करा
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
    
        // 3. LLM प्रतिसादादरम्यान जा, प्रत्येक निवडीसाठी, तपासा की त्यात टूल कॉल आहेत का
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

1. LLM कॉल करण्यासाठी आवश्यक काही इम्पोर्ट्स जोडा:

    ```python
    # एलएलएम
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. नंतर, LLM कॉल करण्याची फंक्शन जोडा:

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
            # ऐच्छिक पॅरामीटर्स
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

    मागील कोडमध्ये आम्ही:

    - MCP सर्व्हरवर आढळलेल्या आणि रूपांतरित फंक्शन्स LLM कडे दिल्या.
    - नंतर LLM ला त्या फंक्शन्ससह कॉल केला.
    - परिणाम तपासला की कोणत्या फंक्शन्स कॉल करायच्या आहेत.
    - शेवटी कॉल करायच्या फंक्शन्सची यादी दिली.

3. अंतिम पायरी, मुख्य कोड अपडेट करा:

    ```python
    prompt = "Add 2 to 20"

    # LLM ला विचारा की सर्व साधने कोणती आहेत, असल्यास
    functions_to_call = call_llm(prompt, functions)

    # सुचविलेल्या फंक्शन्सना कॉल करा
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    वरचा कोड शेवटचा टप्पा होता, ज्यामध्ये:

    - LLM ला प्रॉम्प्टनुसार कॉल करण्यासाठी `call_tool` वापरून MCP टूल कॉल केला जातो.
    - टूल कॉलचा परिणाम छापला जातो.

#### .NET

1. LLM प्रॉम्प्ट विनंती करणारा काही कोड दाखवा:

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

    मागील कोडमध्ये आम्ही:

    - MCP सर्व्हरवरून टूल्स मिळवले, `var tools = await GetMcpTools()`.
    - एक वापरकर्ता प्रॉम्प्ट `userMessage` तयार केला.
    - मॉडेल आणि टूल्ससाठी एक options ऑब्जेक्ट तयार केला.
    - LLM कडे विनंती केली.

2. एक शेवटचा टप्पा, पाहूया LLM ला फंक्शन कॉल करायचं वाटतंय का:

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

    मागील कोडमध्ये आम्ही:

    - फंक्शन कॉल यादीतून लूप केलं.
    - प्रत्येक टूल कॉलसाठी नाव आणि अर्ग्युमेंट्स पार्स केले आणि MCP क्लायंट वापरून MCP सर्व्हरवर टूल कॉल केली. त्यानंतर निकाल छापला.

पूर्ण कोड असा आहे:

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
    // नैसर्गिक भाषा विनंत्या अंमलात आणा ज्या आपोआप MCP साधने वापरतात
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

मागील कोडमध्ये आम्ही:

- MCP सर्व्हर टूल्ससाठी सोप्या नैसर्गिक भाषेतील प्रॉम्प्ट्स वापरल्या
- LangChain4j फ्रेमवर्क आपोआप हाताळतो:
  - वापरकर्ता प्रॉम्प्ट्सना टूल कॉल्समध्ये रूपांतर करणे आवश्यक तेव्हा
  - LLM च्या निर्णयानुसार योग्य MCP टूल्स कॉल करणे
  - LLM आणि MCP सर्व्हर मधील संभाषण प्रवाह व्यवस्थापित करणे
- `bot.chat()` मेथड नैसर्गिक भाषेतील प्रतिसाद देते ज्यात MCP टूल्सच्या परिणामांचा समावेश असू शकतो
- या दृष्टिकोनामुळे वापरकर्त्यांना underlying MCP अंमलबजावणी माहित न लागता सहज अनुभव मिळतो

संपूर्ण कोड उदाहरण:

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


येथे बहुतेक काम होते. आपण सुरुवातीचा वापरकर्ता प्रॉम्प्टसह LLM ला कॉल करू, नंतर प्रतिसाद प्रक्रिया करू जेणेकरून कोणतीही साधने कॉल करण्याची आवश्यकता आहे का हे तपासावे. असल्यास, आपण त्या साधनांना कॉल करू आणि LLM सह संभाषण सुरू ठेवू जोपर्यंत आणखी कोणतीही साधनं कॉल करण्याची गरज नसते आणि आपण अंतिम प्रतिसाद मिळवतो.

आपण LLM ला अनेक वेळा कॉल करणार आहोत, त्यामुळे आपण एक फंक्शन परिभाषित करू जे LLM कॉल हाताळेल. आपला `main.rs` फाइलमध्ये खालील फंक्शन जोडा:

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

हे फंक्शन LLM क्लायंट, संदेशांची यादी (वापरकर्ता प्रॉम्प्टसह), MCP सर्व्हरची साधने घेत आहे, आणि LLM ला विनंती पाठवते, प्रतिसाद परत करते.

LLM कडून प्रतिसादात `choices` नावाचा एक अ‍ॅरे असतो. आपल्याला निकाल प्रक्रिया करणे आवश्यक आहे जेणेकरून कोणतेही `tool_calls` आहेत का ते पाहता येईल. हे आपल्याला सांगते की LLM ने विशिष्ट साधन कॉल करण्यासाठी आग्रह केला आहे ज्यात अर्ग्युमेंट्स दिले आहेत. आपल्या `main.rs` फाइलच्या खालील भागात खालील कोड जोडा जेणेकरून LLM प्रतिसाद हाताळणारे फंक्शन तयार होईल:

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

    // सामग्री उपलब्ध असल्यास छापा
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // टूल कॉल हाताळा
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // सहाय्यक संदेश जोडा

        // प्रत्येक टूल कॉल चालवा
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // संदेशांमध्ये टूल परिणाम जोडा
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // टूल परिणामांसह संवाद सुरू ठेवा
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

जर `tool_calls` अस्तित्त्वात असतील, तर ते साधनांची माहिती बाहेर काढते, MCP सर्व्हरला साधन विनंतीसह कॉल करते, आणि निकाल संभाषण संदेशांमध्ये जोडते. नंतर तो LLM सह संभाषण सुरू ठेवतो आणि संदेश असिस्टंटच्या प्रतिसाद आणि साधन कॉल निकालांसह अपडेट होतात.

MCP कॉलसाठी LLM कडून परत येणारी साधन कॉल माहिती काढण्यासाठी, आपण अजून एक उपयुक्त फंक्शन जोडणार आहोत जे कॉलसाठी आवश्यक सर्व गोष्टी काढेल. आपला `main.rs` फाइलच्या खालील भागात खालील कोड जोडा:

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

सर्व तुकडे जागी असल्यामुळे, आता आपण सुरुवातीचा वापरकर्ता प्रॉम्प्ट हाताळू शकतो आणि LLM ला कॉल करू शकतो. आपल्या `main` फंक्शनमध्ये खालील कोड समाविष्ट करा:

```rust
// साधन कॉलांसह LLM संभाषण
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

हे सुरुवातीच्या वापरकर्ता प्रॉम्प्टसह LLM ला प्रश्न विचारेल की दोन अंकांचे बेरीज काय आहे, आणि प्रतिसाद प्रक्रिया करून डायनॅमिकली साधन कॉल्स हाताळेल.

छान, तुम्ही ते केले!

## असाइनमेंट

व्यायामातील कोड घेतल्यावर काही अधिक साधने वापरून सर्व्हर तयार करा. नंतर व्यायामाप्रमाणे LLM सह एक क्लायंट तयार करा आणि वेगवेगळ्या प्रॉम्प्टसह त्याचे परीक्षण करा जेणेकरून सर्व्हरची साधने डायनॅमिकली कॉल होतात याची खात्री होईल. अशा प्रकारे क्लायंट तयार केल्याने अंतिम वापरकर्त्याला उत्तम अनुभव मिळतो कारण ते अचूक क्लायंट कमांड्सऐवजी प्रॉम्प्ट वापरू शकतात आणि कोणतीही MCP सर्व्हर कॉल होत आहे हे त्यांना कळत नाही.

## समाधान

[Solution](./solution/README.md)

## मुख्य मुद्दे

- आपल्या क्लायंटमध्ये LLM जोडल्याने MPC सर्व्हर्सशी वापरकर्ते चांगल्या प्रकारे संवाद साधू शकतात.
- आपण MCP सर्व्हरच्या प्रतिसादाला LLM समजू शकेल अशा स्वरूपात रूपांतरित करणे आवश्यक आहे.

## नमुने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## अतिरिक्त संसाधने

## पुढे काय

- पुढे: [Visual Studio Code वापरून सर्व्हर वापरणे](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->