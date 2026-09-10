# LLM सह क्लायंट तयार करणे

आतापर्यंत, तुम्ही पाहिलं आहे की सर्व्हर आणि क्लायंट कसे तयार करायचे. क्लायंटने स्पष्टपणे सर्व्हरला कॉल करुन त्याचे साधने, संसाधने आणि प्रॉम्प्ट यादीबद्ध केली आहे. मात्र, हा एक फारच व्यवहार्य दृष्टिकोन नाही. तुमचे वापरकर्ते एजंटिक युगात राहतात आणि प्रॉम्प्ट वापरण्याची आणि LLM सह संवाद साधण्याची अपेक्षा करतात. त्यांना याची काळजी नाही की तुम्ही MCP वापरून तुमच्या क्षमता संग्रहित करता का; ते फक्त नैसर्गिक भाषेत संवाद साधण्याची अपेक्षा करतात. तर आपण हे कसे सोडवू? उपाय म्हणजे क्लायंटमध्ये LLM जोडणे.

## आढावा

या धड्यात आपण क्लायंटमध्ये LLM कसे जोडायचे यावर लक्ष केंद्रित करू आणि हे कसे तुमच्या वापरकर्त्यासाठी जास्त चांगला अनुभव प्रदान करते हे दाखवू.

## शिक्षणाचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही खालील गोष्टी करू शकता:

- LLM सह क्लायंट तयार करा.
- LLM वापरून एम्बेड केलेल्या MCP सर्व्हरशी सहज संवाद साधा.
- क्लायंट साईडवर चांगला अंतिम वापरकर्ता अनुभव द्या.

## दृष्टिकोन

आपण घेणे आवश्यक असलेला दृष्टिकोन समजून घेऊया. LLM जोडणे सोपे वाटते, पण आपण प्रत्यक्षात हे करू का?

क्लायंट कसे सर्व्हरशी संवाद साधेल ते येथे आहे:

1. सर्व्हरशी कनेक्शन स्थापन करा.

1. क्षमता, प्रॉम्प्ट, संसाधने आणि साधने यादीबद्ध करा आणि त्यांची स्कीमा जतन करा.

1. LLM जोडा आणि जतन केलेल्या क्षमतांचा आणि त्यांच्या स्कीमांचा LLM समजणाऱ्या स्वरूपात पास करा.

1. वापरकर्ता प्रॉम्प्ट हाताळा, तो LLM कडे पास करताना क्लायंट कडून यादीबद्ध केलेल्या साधनांसह.

छान, आता आम्हाला समजले की आम्ही हे उच्च स्तरावर कसे करू शकतो, खालील सरावात ते करून पाहूया.

## सराव: LLM सह क्लायंट तयार करणे

या सरावात, आपण क्लायंटमध्ये LLM जोडायचे शिकू.

### GitHub वैयक्तिक प्रवेश टोकन वापरून प्रमाणीकरण

GitHub टोकन तयार करणे एक सोपी प्रक्रिया आहे. हे कसे करायचे:

- GitHub सेटिंग्जमध्ये जा – वरच्या उजव्या कोपऱ्यातील तुमच्या प्रोफाइल चित्रावर क्लिक करा आणि सेटिंग्ज निवडा.
- डेव्हलपर सेटिंग्जकडे जा – खाली स्क्रोल करा आणि डेव्हलपर सेटिंग्जवर क्लिक करा.
- वैयक्तिक प्रवेश टोकन निवडा – Fine-grained टोकन्सवर क्लिक करा आणि नंतर नवीन टोकन तयार करा.
- तुमचे टोकन कॉन्फिगर करा – संदर्भासाठी एक नोट जोडा, समाप्ती तारीख सेट करा, आणि आवश्यक स्कोप (परवानग्या) निवडा. या प्रकरणात Models परवानगी नक्की जोडा.
- टोकन तयार करा आणि कॉपी करा – Generate token वर क्लिक करा, आणि ते लगेच कॉपी करा, कारण तुम्हाला ते न दुसऱ्यांदा दिसणार नाही.

### -1- सर्व्हरशी कनेक्ट करा

चला प्रथम आमचा क्लायंट तयार करूया:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा मान्यता साठी zod आयात करा

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

वरील कोडमध्ये आपण:

- आवश्यक लायब्ररी आयात केल्या.
- दोन सदस्यांसह एक क्लास तयार केला, `client` आणि `openai` ज्यामुळे आम्हाला क्लायंट व्यवस्थापित करणे आणि LLM सोबत संवाद साधणे शक्य आहे.
- GitHub Models वापरण्यासाठी आमच्या LLM उदाहरणाचे कॉन्फिगरेशन केले, `baseUrl` सेट करून जो इनफेरन्स API कडे निर्देशित करतो.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio कनेक्शनसाठी सर्व्हर पॅरामीटर्स तयार करा
server_params = StdioServerParameters(
    command="mcp",  # कार्यान्वित करण्यायोग्य
    args=["run", "server.py"],  # ऐच्छिक कमांड लाइन अर्ग्युमेंट्स
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

वरील कोडमध्ये आपण:

- MCP साठी आवश्यक लायब्ररी आयात केल्या.
- क्लायंट तयार केला.

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

प्रथम, तुम्हाला तुमच्या `pom.xml` फाइलमध्ये LangChain4j dependency जोडावी लागेल. MCP एकत्रिकरण आणि OpenAI-सुसंगत MiniMax API सक्षम करण्यासाठी ही dependencies जोडा:

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

तुमचा MiniMax API की सेट करा आणि पर्यायीपणे, endpoint आणि मॉडेल सेट करा.
`MINIMAX_MODEL_ID` `MiniMax-M3` आणि `MiniMax-M2.7` साठी समर्थन करतो. जर
`OPENAI_BASE_URL` सेट नसेल, तर `MINIMAX_REGION` `global_en` आणि `cn_zh` साठी समर्थन करतो.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

क्षेत्रानुसार endpoint निवडण्यासाठी, `OPENAI_BASE_URL` टाळा:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

त्यानंतर तुमचा Java क्लायंट क्लास तयार करा:

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

        // सर्व्हरशी कनेक्ट करण्यासाठी MCP ट्रान्सपोर्ट तयार करा
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP क्लाएंट तयार करा
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

वरील कोडमध्ये आपण:

- **LangChain4j dependencies जोडल्या**: MCP एकत्रिकरण आणि OpenAI-सुसंगत MiniMax API साठी आवश्यक.
- **LangChain4j लायब्ररी आयात केल्या**: MCP एकत्रिकरण आणि OpenAI चॅट मॉडेल कार्यक्षमतेसाठी.
- **`ChatLanguageModel` तयार केला**: तुमच्या MiniMax API की, endpoint, आणि समर्थित मॉडेल ID वापरून MiniMax वापरण्यासाठी कॉन्फिगर केले.
- **HTTP ट्रान्सपोर्ट सेटअप केला**: Server-Sent Events (SSE) वापरून MCP सर्व्हरशी कनेक्ट होण्यासाठी.
- **MCP क्लायंट तयार केला**: जो सर्व्हरशी संवाद सांभाळेल.
- **LangChain4j चे अंगभूत MCP समर्थन वापरले**: ज्यामुळे LLM आणि MCP सर्व्हरमधील एकत्रिकरण सुलभ होते.

#### Rust

हा उदाहरण गृहीत धरतो की तुमच्याकडे Rust आधारित MCP सर्व्हर चालू आहे. जर नसेल तर [01-first-server](../01-first-server/README.md) धडा पाहा सर्व्हर तयार करण्यासाठी.

एकदा तुमच्याकडे Rust MCP सर्व्हर असेल, टर्मिनल उघडा आणि सर्व्हरच्या त्याच निर्देशिकेत जा. मग खालील आदेश चालवा नवीन LLM क्लायंट प्रोजेक्ट तयार करण्यासाठी:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

तुमच्या `Cargo.toml` फाइलमध्ये खालील dependencies जोडा:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> अधिकृत Rust लायब्ररी OpenAI साठी नाही, पण `async-openai` crate [समुदायाने देखरेख केलेली लायब्ररी](https://platform.openai.com/docs/libraries/rust#rust) आहे जी सामान्यतः वापरली जाते.

`src/main.rs` फाइल उघडा आणि त्याची सामग्री खालील कोडने बदला:

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
    // प्रारंभ संदेश
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

    // TODO: MCP टूल यादी मिळवा

    // TODO: टूल कॉल्ससह LLM संभाषण

    Ok(())
}
```

हा कोड एक आधारभूत Rust अॅप्लिकेशन तयार करतो जो MCP सर्व्हर आणि GitHub Models शी LLM संवादासाठी कनेक्ट होईल.

> [!IMPORTANT]
> अनुप्रयोग चालवण्यापूर्वी, निश्चित करा की `OPENAI_API_KEY` पर्यावरणीय चलात तुमचा GitHub टोकन सेट केला आहे.

छान, पुढील पायरी म्हणजे सर्व्हरवरील क्षमता यादीबद्ध करणे.

### -2- सर्व्हर क्षमता यादीबद्ध करा

आता आपण सर्व्हरशी कनेक्ट होऊ आणि त्याच्या क्षमतांसाठी विचारणा करू:

#### Typescript

त्याच क्लासमध्ये खालील पद्धती जोडा:

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

वरील कोडमध्ये आपण:

- `connectToServer` नावाचा सर्व्हरशी कनेक्ट होण्यासाठी कोड जोडला.
- `run` नावाची पद्धत तयार केली जी आमच्या अॅपच्या प्रवाहाची जबाबदारी सांभाळते. आतापर्यंत फक्त साधने यादीबद्ध केली आहेत पण आम्ही त्यात लवकरच अधिक काही जोडू.

#### Python

```python
# उपलब्ध संसाधने यादी करा
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# उपलब्ध साधने यादी करा
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

आम्ही काय जोडले:

- संसाधने आणि साधने यादीबद्ध केली आणि त्यांचा मुद्रण केला. साधनांसाठी `inputSchema` सुद्धा यादीबद्ध केले जे आपण नंतर वापरू.

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

वरील कोडमध्ये आपण:

- MCP सर्व्हरवरील उपलब्ध साधने यादीबद्ध केली.
- प्रत्येक साधनासाठी, नाव, वर्णन आणि त्याची स्कीमा यादीबद्ध केली. ही स्कीमा आपण लवकरच साधने कॉल करण्यासाठी वापरणार आहोत.

#### Java

```java
// एक टूल प्रदाता तयार करा जो आपोआप MCP टूल्स शोधतो
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP टूल प्रदाता आपोआप हाताळतो:
// - MCP सर्व्हरकडून उपलब्ध टूल्सची यादी करणे
// - MCP टूल स्कीमा LangChain4j स्वरूपात रूपांतरित करणे
// - टूल कार्यान्वयन आणि प्रतिसादांचे व्यवस्थापन करणे
```

वरील कोडमध्ये आपण:

- एक `McpToolProvider` तयार केला जो MCP सर्व्हरवरून सर्व साधने आपोआप शोधतो आणि नोंदणी करतो.
- टूल प्रोव्हायडर आतून MCP टूल स्कीमा आणि LangChain4j च्या टूल स्वरूपात रूपांतर सांभाळतो.
- हा दृष्टिकोन मॅन्युअल टूल यादीबद्ध आणि रूपांतरण प्रक्रिया दूर करतो.

#### Rust

MCP सर्व्हरकडून साधने मिळवण्याचे काम `list_tools` पद्धत वापरून केले जाते. तुमच्या `main` फंक्शननंतर, MCP क्लायंट सेटअप केल्यानंतर, खालील कोड जोडा:

```rust
// MCP साधन सूची मिळवा
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्व्हर क्षमता LLM साधनांमध्ये रूपांतरित करा

क्षमता यादीबद्ध केल्यानंतर पुढचा भाग आहे त्यांना अशा स्वरूपात रूपांतरित करणे जे LLM समजू शकतो. असे केल्यावर, आपण या क्षमतांना आमच्या LLM साठी साधन म्हणून उपलब्ध करून देऊ शकतो.

#### TypeScript

1. MCP सर्व्हरकडून उत्तर LLM वापरू शकणाऱ्या टूल स्वरूपात रूपांतरित करण्यासाठी खालील कोड जोडा:

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

    वरील कोड MCP सर्व्हरकडून उत्तर घेते आणि ते LLM समजू शकणाऱ्या टूल परिभाषेत रूपांतरित करते.

2. नंतर `run` पद्धत अपडेट करूया जेणेकरून सर्व्हर क्षमता यादीबद्ध करतील:

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

    वरील कोडमध्ये, `run` पद्धत यादीतून प्रत्येक नोंद घेते आणि `openAiToolAdapter` कॉल करते.

#### Python

1. प्रथम, खालील रूपांतरक फंक्शन तयार करा:

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

    वरील `convert_to_llm_tools` फंक्शनमध्ये MCP टूल उत्तर घेतले आहे आणि ते LLM समजू शकणाऱ्या स्वरूपात रूपांतरित केले आहे.

2. पुढे, आमचा क्लायंट कोड अपडेट करूया जेणेकरून हा फंक्शन वापरला जाईल:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    येथे, आम्ही `convert_to_llm_tool` ला कॉल करत आहोत ज्यामुळे MCP टूल उत्तर रूपांतरित होऊन नंतर LLM ला फीड करता येईल.

#### .NET

1. MCP टूल उत्तर LLM समजू शकेल अशा स्वरूपात रूपांतरित करण्यासाठी कोड जोडा:

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

वरील कोडमध्ये आपण:

- `ConvertFrom` नावाचा फंक्शन तयार केला जो नाव, वर्णन आणि इनपुट स्कीमा घेते.
- अशी कार्यक्षमता परिभाषित केली जी FunctionDefinition तयार करते आणि ते ChatCompletionsDefinition ला पास करते. ते LLM समजू शकणारे आहे.

2. आता पाहूया आपला विद्यमान कोड कसा या फंक्शनचा फायदा घेऊ शकतो:

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

// LLM आणि MCP साधने वापरून AI सेवा कॉन्फिगर करा
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

वरील कोडमध्ये आपण:

- नैसर्गिक भाषा संवादासाठी सोपा `Bot` इंटरफेस परिभाषित केला.
- LangChain4j चे `AiServices` वापरले जे LLM ला MCP टूल प्रोव्हायडरशी आपोआप जोडते.
- फ्रेमवर्क आपोआप टूल स्कीमा रूपांतरण आणि फंक्शन कॉलिंग मागदर्शन करते.
- हा दृष्टिकोन मॅन्युअल टूल रूपांतरण दूर करतो - LangChain4j सर्व जटिलता हाताळतो.

#### Rust

MCP टूल उत्तर LLM समजू शकणाऱ्या स्वरूपात रूपांतरित करण्यासाठी, आम्ही एक मदतनीस फंक्शन जोडू जे टूल यादीचे स्वरूपित करेल. तुमच्या `main.rs` फायलबाहेर `main` फंक्शन नंतर खालील कोड जोडा. हे LLM कडून विनंत्या केल्यावर कॉल केले जाईल:

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

छान, आता आपल्याकडे वापरकर्ता विनंत्या हाताळायला सिस्टम तयार आहे, त्यामुळे पुढे ते पाहूया.

### -4- वापरकर्ता प्रॉम्प्ट विनंती हाताळा

या कोडच्या भागात, आपण वापरकर्ता विनंत्या हाताळणार आहोत.

#### TypeScript

1. LLM कॉल करण्यासाठी खालील पद्धत जोडा:

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

    वरील कोडमध्ये आपण:

    - `callTools` नावाची पद्धत जोडली.
    - ही पद्धत LLM उत्तर घेते आणि कोणती साधने कॉल केली गेली आहेत ते तपासते.

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // टूल कॉल करा
        }
        ```

    - जर LLM सूचित करत असेल तर साधन कॉल करते:

        ```typescript
        // 2. सर्व्हरच्या साधनाला कॉल करा
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. निकालासह काहीतरी करा
        // करायचे आहे
        ```

2. `run` पद्धत अपडेट करा जेणेकरून LLM कॉल्स आणि `callTools` कॉल समाविष्ट होतील:

    ```typescript

    // 1. LLM साठी इनपुट म्हणून संदेश तयार करा
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM कॉल करीत आहे
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM प्रतिसाद तपासा, प्रत्येक पर्यायासाठी तपासा की त्यामध्ये टूल कॉल आहेत का
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

छान, पूर्ण कोड यादीबद्ध करूया:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा प्रमाणीकरणासाठी zod आयात करा

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // भविष्यात कदाचित हा URL बदलावा लागेल: https://models.github.ai/inference
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
          // input_schema वर आधारित एक zod स्कीमा तयार करा
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
    
          // 3. परिणामांसोबत काहीतरी करा
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
    
        // 3. LLM प्रतिसाद पाहा, प्रत्येक पर्यायासाठी तपासा की त्यात टूल कॉल आहेत का
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

1. LLM कॉलसाठी आवश्यक काही आयात जोडा:

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. नंतर, LLM कॉल करणारा फंक्शन जोडा:

    ```python
    # एलएलएम

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
            # ऐच्छिक परिमाणे
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

    वरील कोडमध्ये आपण:

    - आमच्या फंक्शन्स वापरल्या, जे MCP सर्व्हरवर मिळाले आणि रूपांतरित केले.
    - मग LLM ला त्या फंक्शन्ससह कॉल केला.
    - नंतर निकाल तपासला की कोणते फंक्शन्स कॉल करायचे आहेत का.
    - शेवटी कॉल करायच्या फंक्शन्सची यादी दिली.

3. अंतिम टप्पा, मुख्य कोड अपडेट करा:

    ```python
    prompt = "Add 2 to 20"

    # LLM ला विचारा की कोणते उपकरणे वापरायची, असल्यास
    functions_to_call = call_llm(prompt, functions)

    # सुचवलेले फंक्शन्स कॉल करा
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    या कोडमध्ये आपण:

    - `call_tool` द्वारे MCP टूल कॉल करत आहोत असे फंक्शन LLM सूचित करते तसे.
    - MCP सर्व्हरवर साधन कॉल निकाल मुद्रित करतो.

#### .NET

1. LLM प्रॉम्प्ट विनंतीसाठी काही कोड दाखवूया:

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

    वरील कोडमध्ये आपण:

    - MCP सर्व्हरवरून साधने मिळवली, `var tools = await GetMcpTools()`.
    - वापरकर्ता प्रॉम्प्ट `userMessage` परिभाषित केला.
    - मॉडेल आणि साधने निर्दिष्ट करणारा पर्याय ऑब्जेक्ट तयार केला.
    - LLM कडे विनंती केली.

2. शेवटचा टप्पा, पाहूया LLM सूचित करतो का फंक्शन कॉल करावे:

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

    वरील कोडमध्ये आपण:

    - फंक्शन कॉल यादीमधून फेरफटका मारला.
    - प्रत्येक साधन कॉलसाठी नाव आणि आर्ग्युमेंट पार्स केले आणि MCP क्लायंट वापरून MCP सर्व्हरवर साधन कॉल केले. अखेरीस निकाल मुद्रित केले.

खालीलप्रमाणे पूर्ण कोड आहे:

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
    // MCP साधने स्वयंचलितपणे वापरून नैसर्गिक भाषा विनंत्या चालवा
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

वरील कोडमध्ये आपण:

- MCP सर्व्हरच्या साधनांसह साधे नैसर्गिक भाषा प्रॉम्प्ट वापरले.
- LangChain4j फ्रेमवर्क आपोआप हाताळतो:
  - गरजेनुसार वापरकर्ता प्रॉम्प्टला टूल कॉलमध्ये रूपांतरित करणे.
  - LLM च्या निर्णयानुसार योग्य MCP टूल कॉल करणे.
  - LLM आणि MCP सर्व्हरमधील संभाषण प्रवाह व्यवस्थापन.
- `bot.chat()` पद्धत नैसर्गिक भाषा प्रतिसाद परत करते ज्यामध्ये MCP टूल कार्यान्वयनांचे निकाल असू शकतात.
- ह्या दृष्टिकोनाने वापरकर्त्यास सुलभ अनुभव मिळतो ज्यात त्यांना अंतर्गत MCP रचना माहित असण्याची गरज नाही.

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

येथून बहुमत कार्य होते. आपण प्रारंभी वापरकर्ता प्रॉम्प्टसह LLM कॉल करू, नंतर उत्तर प्रक्रिया करू की कोणतेही साधन कॉल करणे आवश्यक आहे का. असल्यास, त्या साधनांना कॉल करू आणि LLM सह संभाषण चालू ठेवू जोपर्यंत आणखी साधन कॉल आवश्यक नाही आणि अंतिम उत्तर प्राप्त होत नाही.


आपण LLM कडे एकाहून अधिक कॉल करणार आहोत, म्हणून LLM कॉलसाठी एक फंक्शन परिभाषित करूया जे तो हाताळेल. आपल्या `main.rs` फाइलमध्ये खालील फंक्शन जोडा:

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

हे फंक्शन LLM क्लायंट, संदेशांची यादी (यात वापरकर्त्याचा प्रॉम्प्ट समाविष्ट आहे), MCP सर्व्हरमधील साधने घेतं आणि LLM ला विनंती पाठवते, प्रतिसाद परत करते.

LLM कडून मिळालेला प्रतिसाद `choices` नावाच्या अॅरेचा समावेश करेल. आपल्याला निकाल प्रक्रिया करणे आवश्यक आहे की काही `tool_calls` आहेत का ते बघण्यासाठी. यामुळे आपल्याला कळते की LLM विशिष्ट साधन कॉल करण्यासाठी अर्ज करत आहे. आपली `main.rs` फाइलच्या शेवटी खालील कोड जोडा जेणेकरून LLM प्रतिसाद हाताळणारे फंक्शन परिभाषित करता येईल:

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

    // साधन कॉल्स हाताळा
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // सहाय्यक संदेश जोडा

        // प्रत्येक साधन कॉल अंमलात आणा
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // संदेशांमध्ये साधनाचे परिणाम जोडा
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // साधन परिणामांसह संभाषण सुरू ठेवा
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

जर `tool_calls` उपलब्ध असतील, तर ते साधनांची माहिती काढते, साधन विनंतीसह MCP सर्व्हरला कॉल करते आणि निकाल संभाषण संदेशांमध्ये जोडते. त्यानंतर LLM सोबत संभाषण सुरू ठेवते आणि संदेश सहाय्यकाचा प्रतिसाद आणि साधन कॉल निकषांसह अद्यतनित केले जातात.

MCP कॉलसाठी LLM परत करत असलेल्या साधन कॉल माहिती काढण्यासाठी, आपण आणखी एक सहाय्यक फंक्शन जोडू जे कॉल करण्यासाठी आवश्यक असेल ते सर्व काढेल. आपल्या `main.rs` फाइलच्या शेवटी खालील कोड जोडा:

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

सर्व भाग समाविष्ट केल्यानंतर, आपण आता प्रारंभिक वापरकर्ता प्रॉम्प्ट हाताळू शकतो आणि LLM ला कॉल करू शकतो. आपल्या `main` फंक्शनला खालील कोड समाविष्ट करून अपडेट करा:

```rust
// टूल कॉलसह LLM संभाषण
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

हे LLM ला दोन संख्यांचा योग विचारणारा प्रारंभिक वापरकर्ता प्रॉम्प्ट विचारेल आणि प्रतिसाद प्रक्रिया करून डायनॅमिकली साधन कॉल हाताळेल.

छान, तुम्ही ते केलं!

## कार्य

व्यायामातील कोड घेऊन अधिक साधने असलेला सर्व्हर तयार करा. मग व्यायामाप्रमाणे LLM असलेला क्लायंट तयार करा आणि वेगवेगळ्या प्रॉम्प्टसह त्याची चाचणी करा जेणेकरून सर्व्हरमधील आपल्या सर्व साधनांचा डायनॅमिक कॉल होत आहे याची खात्री करता येईल. अशा प्रकारे क्लायंट तयार केल्याने अंतिम वापरकर्त्याचा अनुभव उत्तम बनतो कारण त्यांना अचूक क्लायंट कमांड्सच्या ऐवजी प्रॉम्प्ट वापरता येतात आणि कोणताही MCP सर्व्हर कॉल होत आहे हे त्यांना कळत नाही.

## सोडवणूक

[सोडवणूक](./solution/README.md)

## मुख्य मुद्दे

- आपल्या क्लायंटमध्ये LLM जोडल्याने वापरकर्त्यांना MCP सर्व्हरसह संवाद साधण्याचा चांगला मार्ग मिळतो.
- MCP सर्व्हरचा प्रतिसाद LLM समजेल अशा स्वरूपात रूपांतरित करणे आवश्यक आहे.

## नमुने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## अतिरिक्त स्रोत

## पुढे काय

- पुढे: [Visual Studio Code वापरून सर्व्हर कसे वापरायचे](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->