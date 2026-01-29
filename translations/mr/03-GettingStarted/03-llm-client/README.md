# LLM सह क्लायंट तयार करणे

आत्तापर्यंत, तुम्ही पाहिले आहे की सर्व्हर आणि क्लायंट कसे तयार करायचे. क्लायंटने स्पष्टपणे सर्व्हरला कॉल करून त्याचे टूल्स, संसाधने आणि प्रॉम्प्ट्स यादीबद्ध केली आहे. मात्र, हा दृष्टिकोन फारसा व्यावहारिक नाही. तुमचा वापरकर्ता एजंटिक युगात राहतो आणि प्रॉम्प्ट्स वापरून LLM शी संवाद साधण्याची अपेक्षा करतो. तुमच्या वापरकर्त्यास याची पर्वा नाही की तुम्ही तुमच्या क्षमता साठवण्यासाठी MCP वापरता की नाही, पण ते नैसर्गिक भाषेत संवाद साधण्याची अपेक्षा करतात. तर आपण हे कसे सोडवू? यासाठी क्लायंटमध्ये LLM जोडणे आवश्यक आहे.

## आढावा

या धड्यात आपण क्लायंटमध्ये LLM कसे जोडायचे यावर लक्ष केंद्रित करू आणि हे तुमच्या वापरकर्त्यास कसे चांगले अनुभव देते हे दाखवू.

## शिकण्याचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- LLM सह क्लायंट तयार करणे.
- LLM वापरून MCP सर्व्हरशी सहज संवाद साधणे.
- क्लायंट बाजूने चांगला अंतिम वापरकर्ता अनुभव प्रदान करणे.

## दृष्टिकोन

आपण कोणता दृष्टिकोन घ्यायचा आहे ते समजून घेऊया. LLM जोडणे सोपे वाटते, पण आपण प्रत्यक्षात हे कसे करणार?

क्लायंट सर्व्हरशी कसे संवाद साधेल ते खालीलप्रमाणे:

1. सर्व्हरशी कनेक्शन स्थापित करा.

1. क्षमता, प्रॉम्प्ट्स, संसाधने आणि टूल्स यादीबद्ध करा आणि त्यांचा स्कीमा जतन करा.

1. LLM जोडा आणि जतन केलेल्या क्षमता आणि त्यांचा स्कीमा LLM समजेल अशा स्वरूपात द्या.

1. वापरकर्त्याचा प्रॉम्प्ट LLM कडे टूल्ससह पाठवा जे क्लायंटने यादीबद्ध केले आहेत.

छान, आता आपण उच्च स्तरावर हे कसे करायचे ते समजले, खालील व्यायामात हे प्रयत्न करूया.

## व्यायाम: LLM सह क्लायंट तयार करणे

या व्यायामात, आपण क्लायंटमध्ये LLM कसे जोडायचे ते शिकू.

### GitHub वैयक्तिक प्रवेश टोकन वापरून प्रमाणीकरण

GitHub टोकन तयार करणे सोपे आहे. हे कसे करायचे:

- GitHub सेटिंग्जवर जा – वरच्या उजव्या कोपऱ्यात तुमच्या प्रोफाइल चित्रावर क्लिक करा आणि सेटिंग्ज निवडा.
- डेव्हलपर सेटिंग्जकडे जा – खाली स्क्रोल करा आणि डेव्हलपर सेटिंग्जवर क्लिक करा.
- वैयक्तिक प्रवेश टोकन्स निवडा – फाईन-ग्रेनड टोकन्सवर क्लिक करा आणि नवा टोकन तयार करा.
- तुमचा टोकन कॉन्फिगर करा – संदर्भासाठी नोट जोडा, समाप्ती तारीख सेट करा, आणि आवश्यक स्कोप्स (परवानग्या) निवडा. या प्रकरणात Models परवानगी नक्की जोडा.
- टोकन तयार करा आणि कॉपी करा – Generate token वर क्लिक करा आणि लगेच कॉपी करा, कारण नंतर ते पुन्हा पाहता येणार नाही.

### -1- सर्व्हरशी कनेक्ट करा

आता आपला क्लायंट तयार करूया:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा प्रमाणीकरणासाठी zod आयात करा

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

- आवश्यक लायब्ररी आयात केल्या आहेत
- दोन सदस्यांसह एक क्लास तयार केला आहे, `client` आणि `openai`, जे अनुक्रमे क्लायंट व्यवस्थापित करण्यासाठी आणि LLM शी संवाद साधण्यासाठी मदत करतील.
- GitHub Models वापरण्यासाठी `baseUrl` सेट करून LLM उदाहरण कॉन्फिगर केले आहे.

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

वरील कोडमध्ये आपण:

- MCP साठी आवश्यक लायब्ररी आयात केल्या आहेत
- क्लायंट तयार केला आहे

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

सर्वप्रथम, तुम्हाला तुमच्या `pom.xml` फाईलमध्ये LangChain4j अवलंबित्वे जोडावी लागतील. MCP एकत्रीकरण आणि GitHub Models समर्थन सक्षम करण्यासाठी ही अवलंबित्वे जोडा:

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

नंतर तुमचा Java क्लायंट क्लास तयार करा:

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
    
    public static void main(String[] args) throws Exception {        // LLM ला GitHub मॉडेल्स वापरण्यासाठी कॉन्फिगर करा
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
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
}
```

वरील कोडमध्ये आपण:

- **LangChain4j अवलंबित्वे जोडली**: MCP एकत्रीकरण, OpenAI अधिकृत क्लायंट, आणि GitHub Models समर्थनासाठी आवश्यक
- **LangChain4j लायब्ररी आयात केल्या**: MCP एकत्रीकरण आणि OpenAI चॅट मॉडेल कार्यक्षमता साठी
- **`ChatLanguageModel` तयार केला**: GitHub Models वापरण्यासाठी तुमचा GitHub टोकन वापरून कॉन्फिगर केला
- **HTTP ट्रान्सपोर्ट सेट केला**: Server-Sent Events (SSE) वापरून MCP सर्व्हरशी कनेक्ट करण्यासाठी
- **MCP क्लायंट तयार केला**: जो सर्व्हरशी संवाद साधेल
- **LangChain4j चा अंगभूत MCP समर्थन वापरला**: जे LLM आणि MCP सर्व्हरमधील एकत्रीकरण सुलभ करते

#### Rust

हा उदाहरण समजते की तुमच्याकडे Rust आधारित MCP सर्व्हर चालू आहे. जर नसेल, तर [01-first-server](../01-first-server/README.md) धडा पाहून सर्व्हर तयार करा.

तुमचा Rust MCP सर्व्हर तयार झाल्यावर, टर्मिनल उघडा आणि सर्व्हरच्या निर्देशिकेत जा. नंतर खालील आदेश चालवा नवीन LLM क्लायंट प्रोजेक्ट तयार करण्यासाठी:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

तुमच्या `Cargo.toml` फाईलमध्ये खालील अवलंबित्वे जोडा:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI साठी अधिकृत Rust लायब्ररी नाही, मात्र `async-openai` क्रेट ही एक [समुदायाने देखभाल केलेली लायब्ररी](https://platform.openai.com/docs/libraries/rust#rust) आहे जी सामान्यतः वापरली जाते.

`src/main.rs` फाईल उघडा आणि त्याचा मजकूर खालील कोडने बदला:

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
    // प्रारंभिक संदेश
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

    // TODO: टूल कॉलसह LLM संभाषण

    Ok(())
}
```

हा कोड एक मूलभूत Rust अॅप्लिकेशन सेट करतो जे MCP सर्व्हर आणि GitHub Models शी LLM संवादासाठी कनेक्ट होईल.

> [!IMPORTANT]
> अॅप्लिकेशन चालवण्यापूर्वी `OPENAI_API_KEY` पर्यावरण चल तुमच्या GitHub टोकनसह सेट करा.

छान, पुढील टप्प्यासाठी, सर्व्हरवरील क्षमता यादीबद्ध करूया.

### -2- सर्व्हर क्षमता यादीबद्ध करा

आता आपण सर्व्हरशी कनेक्ट होऊन त्याच्या क्षमता विचारू:

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

    // साधने यादी करीत आहे
    const toolsResult = await this.client.listTools();
}
```

वरील कोडमध्ये आपण:

- सर्व्हरशी कनेक्ट होण्यासाठी `connectToServer` कोड जोडला आहे.
- `run` पद्धत तयार केली आहे जी आमच्या अॅप फ्लोची जबाबदारी सांभाळते. आतापर्यंत ती फक्त टूल्स यादीबद्ध करते पण लवकरच त्यात अधिक जोडू.

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

- संसाधने आणि टूल्स यादीबद्ध केली आणि छापली. टूल्ससाठी `inputSchema` देखील यादीबद्ध केली जी नंतर वापरली जाईल.

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

- MCP सर्व्हरवरील उपलब्ध टूल्स यादीबद्ध केली
- प्रत्येक टूलसाठी नाव, वर्णन आणि त्याचा स्कीमा यादीबद्ध केला. हा स्कीमा आपण लवकरच टूल कॉलसाठी वापरणार आहोत.

#### Java

```java
// एक टूल प्रदाता तयार करा जो स्वयंचलितपणे MCP टूल्स शोधतो
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP टूल प्रदाता स्वयंचलितपणे हाताळतो:
// - MCP सर्व्हरवरून उपलब्ध टूल्सची यादी करणे
// - MCP टूल स्कीमांना LangChain4j स्वरूपात रूपांतरित करणे
// - टूल कार्यान्वयन आणि प्रतिसाद व्यवस्थापित करणे
```

वरील कोडमध्ये आपण:

- `McpToolProvider` तयार केला जो MCP सर्व्हरमधील सर्व टूल्स आपोआप शोधून नोंदणी करतो
- टूल प्रोव्हायडर MCP टूल स्कीम्स आणि LangChain4j च्या टूल फॉरमॅटमधील रूपांतरण अंतर्गत हाताळतो
- हा दृष्टिकोन मॅन्युअल टूल यादीबद्ध करणे आणि रूपांतरण प्रक्रिया लपवतो

#### Rust

MCP सर्व्हरमधून टूल्स मिळवण्यासाठी `list_tools` पद्धत वापरली जाते. तुमच्या `main` फंक्शनमध्ये, MCP क्लायंट सेट केल्यानंतर खालील कोड जोडा:

```rust
// MCP साधन यादी मिळवा
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्व्हर क्षमता LLM टूल्समध्ये रूपांतरित करा

सर्व्हर क्षमता यादीबद्ध केल्यानंतर पुढचा टप्पा म्हणजे त्यांना LLM समजेल अशा स्वरूपात रूपांतरित करणे. एकदा आपण तसे केले की, आपण या क्षमता LLM साठी टूल्स म्हणून प्रदान करू शकतो.

#### TypeScript

1. MCP सर्व्हरच्या प्रतिसादाला LLM वापरू शकणाऱ्या टूल स्वरूपात रूपांतरित करण्यासाठी खालील कोड जोडा:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // इनपुट_स्कीमावर आधारित झोड स्कीमा तयार करा
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // प्रकार स्पष्टपणे "function" म्हणून सेट करा
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

    वरील कोड MCP सर्व्हरचा प्रतिसाद घेऊन तो LLM समजेल अशा टूल व्याख्येच्या स्वरूपात रूपांतरित करतो.

1. नंतर `run` पद्धत अपडेट करूया जेणेकरून सर्व्हर क्षमता यादीबद्ध करता येतील:

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

    वरील कोडमध्ये, `run` पद्धत अपडेट केली आहे ज्यात परिणामावर नकाशा तयार करून प्रत्येक नोंदीसाठी `openAiToolAdapter` कॉल केला आहे.

#### Python

1. प्रथम, खालील कन्व्हर्टर फंक्शन तयार करूया

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

    `convert_to_llm_tools` फंक्शनमध्ये आपण MCP टूल प्रतिसाद घेऊन तो LLM समजेल अशा स्वरूपात रूपांतरित करतो.

1. नंतर, क्लायंट कोड अपडेट करूया जेणेकरून हा फंक्शन वापरता येईल:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    येथे, आपण MCP टूल प्रतिसाद LLM ला देण्यायोग्य स्वरूपात रूपांतरित करण्यासाठी `convert_to_llm_tool` कॉल जोडत आहोत.

#### .NET

1. MCP टूल प्रतिसाद LLM समजेल अशा स्वरूपात रूपांतरित करण्यासाठी कोड जोडा

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

- `ConvertFrom` फंक्शन तयार केले जे नाव, वर्णन आणि इनपुट स्कीमा घेतो.
- एक फंक्शन डिफिनिशन तयार करण्याची कार्यक्षमता परिभाषित केली जी ChatCompletionsDefinition मध्ये दिली जाते. हे LLM समजेल अशा स्वरूपात आहे.

1. या फंक्शनचा फायदा घेण्यासाठी काही विद्यमान कोड कसा अपडेट करायचा ते पाहूया:

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

// LLM आणि MCP साधनांसह AI सेवा कॉन्फिगर करा
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

वरील कोडमध्ये आपण:

- नैसर्गिक भाषा संवादासाठी सोपा `Bot` इंटरफेस परिभाषित केला आहे
- LangChain4j च्या `AiServices` वापरून LLM आणि MCP टूल प्रोव्हायडर आपोआप बांधले आहेत
- फ्रेमवर्क टूल स्कीमा रूपांतरण आणि फंक्शन कॉलिंग मागे हाताळतो
- हा दृष्टिकोन मॅन्युअल टूल रूपांतरण टाळतो - LangChain4j MCP टूल्सना LLM-सुसंगत स्वरूपात रूपांतरित करण्याची सर्व गुंतागुंत हाताळतो

#### Rust

MCP टूल प्रतिसाद LLM समजेल अशा स्वरूपात रूपांतरित करण्यासाठी, आपण एक सहाय्यक फंक्शन जोडू जे टूल्सची यादी योग्य स्वरूपात तयार करेल. `main.rs` फाईलमध्ये `main` फंक्शनखाली खालील कोड जोडा. हा LLM कडे विनंत्या करताना कॉल केला जाईल:

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

छान, आता आपण वापरकर्त्याच्या विनंत्या हाताळण्यासाठी तयार आहोत, तर पुढे जाऊया.

### -4- वापरकर्ता प्रॉम्प्ट विनंती हाताळा

या कोड भागात आपण वापरकर्त्याच्या विनंत्या हाताळणार आहोत.

#### TypeScript

1. LLM कॉल करण्यासाठी वापरली जाणारी पद्धत जोडा:

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

    - `callTools` नावाची पद्धत जोडली आहे.
    - ही पद्धत LLM प्रतिसाद घेते आणि कोणती टूल्स कॉल झाली आहेत ते तपासते:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // साधन कॉल करा
        }
        ```

    - LLM सूचित केल्यास टूल कॉल करते:

        ```typescript
        // 2. सर्व्हरच्या टूलला कॉल करा
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. निकालासह काहीतरी करा
        // करायचे आहे
        ```

1. `run` पद्धत अपडेट करा ज्यात LLM कॉल आणि `callTools` कॉल समाविष्ट आहेत:

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

    // 2. LLM कॉल करणे
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM प्रतिसाद तपासा, प्रत्येक पर्यायासाठी, तपासा की त्यात टूल कॉल आहेत का
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
            baseURL: "https://models.inference.ai.azure.com", // भविष्यात कदाचित या URL वर बदल करावा लागेल: https://models.github.ai/inference
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
          // इनपुट_स्कीमावर आधारित zod स्कीमा तयार करा
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
    
        // 1. LLM प्रतिसादातून जा, प्रत्येक निवडीसाठी तपासा की त्यात टूल कॉल आहेत का
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

1. LLM कॉल करण्यासाठी आवश्यक काही आयात जोडा

    ```python
    # ल्लम
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. नंतर, LLM कॉल करणारा फंक्शन जोडा:

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

    वरील कोडमध्ये आपण:

    - MCP सर्व्हरवर सापडलेल्या आणि रूपांतरित केलेल्या फंक्शन्स LLM कडे दिल्या.
    - नंतर त्या फंक्शन्ससह LLM कॉल केला.
    - नंतर निकाल तपासला की कोणते फंक्शन्स कॉल करायचे आहेत.
    - शेवटी कॉल करायच्या फंक्शन्सची यादी दिली.

1. अंतिम टप्पा, मुख्य कोड अपडेट करा:

    ```python
    prompt = "Add 2 to 20"

    # LLM ला विचारा की कोणती साधने वापरायची आहेत, असल्यास
    functions_to_call = call_llm(prompt, functions)

    # सुचवलेल्या फंक्शन्सना कॉल करा
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    वरील कोडमध्ये आपण:

    - LLM च्या प्रॉम्प्टवर आधारित `call_tool` वापरून MCP टूल कॉल केला.
    - टूल कॉलचा निकाल MCP सर्व्हरवर छापला.

#### .NET

1. LLM प्रॉम्प्ट विनंतीसाठी कोड दाखवा:

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

    वरील कोडमध्ये आपण:

    - MCP सर्व्हरवरून टूल्स मिळवले, `var tools = await GetMcpTools()`.
    - वापरकर्ता प्रॉम्प्ट `userMessage` तयार केला.
    - मॉडेल आणि टूल्स निर्दिष्ट करणारा पर्याय ऑब्जेक्ट तयार केला.
    - LLM कडे विनंती केली.

1. शेवटचा टप्पा, पाहूया LLM ला फंक्शन कॉल करायचे आहे का:

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

    - फंक्शन कॉल्सच्या यादीतून लूप केले.
    - प्रत्येक टूल कॉलसाठी नाव आणि आर्ग्युमेंट्स पार्स करून MCP क्लायंट वापरून टूल कॉल केले. शेवटी निकाल छापले.

पूर्ण कोड:

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
    // MCP साधने स्वयंचलितपणे वापरणारे नैसर्गिक भाषा विनंत्या अंमलात आणा
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

- सोप्या नैसर्गिक भाषा प्रॉम्प्ट्स वापरून MCP सर्व्हर टूल्सशी संवाद साधला
- LangChain4j फ्रेमवर्क आपोआप हाताळतो:
  - आवश्यकतेनुसार वापरकर्ता प्रॉम्प्ट्सना टूल कॉलमध्ये रूपांतरित करणे
  - LLM च्या निर्णयानुसार योग्य MCP टूल्स कॉल करणे
  - LLM आणि MCP सर्व्हरमधील संभाषण प्रवाह व्यवस्थापित करणे
- `bot.chat()` पद्धत नैसर्गिक भाषा प्रतिसाद देते ज्यात MCP टूल्सच्या निष्पत्तींचा समावेश असू शकतो
- हा दृष्टिकोन वापरकर्त्यास एक अखंड अनुभव देतो जिथे त्यांना MCP अंतर्गत अंमलबजावणीची माहिती असण्याची गरज नाही

पूर्ण कोड उदाहरण:

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

इथे बहुतेक काम होते. आपण सुरुवातीचा वापरकर्ता प्रॉम्प्ट घेऊन LLM कॉल करू, नंतर प्रतिसाद तपासू की कोणते टूल्स कॉल करायचे आहेत का. असल्यास, त्या टूल्स कॉल करू आणि LLM सोबत संभाषण चालू ठेवू जोपर्यंत आणखी टूल कॉल्सची गरज नाही आणि अंतिम प्रतिसाद मिळत नाही.

आपण LLM ला अनेक वेळा कॉल करणार आहोत, म्हणून LLM कॉल हाताळणारा फंक्शन परिभाषित करूया. खालील फंक्शन `main.rs` फाईलमध्ये जोडा:

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

हा फंक्शन LLM क्लायंट, संदेशांची यादी (वापरकर्ता प्रॉम्प्टसह), MCP सर्व्हरमधील टूल्स घेतो आणि LLM कडे विनंती पाठवतो, प्रतिसाद परत करतो.
LLM कडून मिळालेला प्रतिसाद `choices` या अ‍ॅरेचा समावेश करेल. आपल्याला निकाल प्रक्रिया करावी लागेल की कोणतेही `tool_calls` आहेत का ते पाहण्यासाठी. हे आपल्याला कळते की LLM विशिष्ट टूल कॉल करण्यासाठी विनंती करत आहे ज्यामध्ये आर्ग्युमेंट्स असतील. LLM प्रतिसाद हाताळण्यासाठी खालील कोड आपल्या `main.rs` फाइलच्या तळाशी जोडा:

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

    // साधन कॉल हाताळा
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

            // संदेशांमध्ये साधनाचा निकाल जोडा
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // साधन निकालांसह संभाषण सुरू ठेवा
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

जर `tool_calls` उपस्थित असतील, तर ते टूलची माहिती काढते, MCP सर्व्हरला टूल विनंतीसह कॉल करते, आणि निकाल संभाषण संदेशांमध्ये जोडते. नंतर ते LLM सोबत संभाषण सुरू ठेवते आणि संदेश सहाय्यकाच्या प्रतिसाद आणि टूल कॉल निकालांसह अद्ययावत होतात.

MCP कॉलसाठी LLM परत करणाऱ्या टूल कॉल माहिती काढण्यासाठी, आपण आणखी एक सहाय्यक फंक्शन जोडू जे कॉल करण्यासाठी आवश्यक असलेले सर्व काही काढेल. खालील कोड आपल्या `main.rs` फाइलच्या तळाशी जोडा:

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

सर्व भाग ठिकाणी असल्यामुळे, आपण आता प्रारंभिक वापरकर्ता प्रॉम्प्ट हाताळू शकतो आणि LLM कॉल करू शकतो. आपल्या `main` फंक्शनमध्ये खालील कोड समाविष्ट करा:

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

हे प्रारंभिक वापरकर्ता प्रॉम्प्टसह LLM ला क्वेरी करेल ज्यात दोन संख्यांचा बेरीज विचारला आहे, आणि प्रतिसाद प्रक्रिया करेल ज्यामुळे टूल कॉल डायनॅमिकली हाताळले जातील.

छान, तुम्ही ते केले!

## असाइनमेंट

व्यायामातील कोड घेऊन सर्व्हरमध्ये आणखी काही टूल्स तयार करा. नंतर व्यायामाप्रमाणे LLM सह क्लायंट तयार करा आणि वेगवेगळ्या प्रॉम्प्टसह त्याची चाचणी करा जेणेकरून तुमचे सर्व्हर टूल्स डायनॅमिकली कॉल होतात याची खात्री होईल. अशा प्रकारे क्लायंट तयार केल्याने अंतिम वापरकर्त्याला उत्तम वापरकर्ता अनुभव मिळेल कारण ते प्रॉम्प्ट वापरू शकतात, अचूक क्लायंट कमांड्सऐवजी, आणि कोणताही MCP सर्व्हर कॉल होत असल्याचे त्यांना कळणार नाही.

## सोल्यूशन

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## मुख्य मुद्दे

- आपल्या क्लायंटमध्ये LLM जोडल्याने वापरकर्त्यांसाठी MCP सर्व्हरशी संवाद साधण्याचा चांगला मार्ग मिळतो.
- MCP सर्व्हर प्रतिसाद LLM समजेल अशा स्वरूपात रूपांतरित करणे आवश्यक आहे.

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
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->