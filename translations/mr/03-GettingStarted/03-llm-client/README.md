# LLM सह क्लायंट तयार करणे

आत्तापर्यंत, तुम्ही पाहिले आहे की तुम्ही सर्व्हर आणि क्लायंट कसे तयार करू शकता. क्लायंटने स्पष्टपणे सर्व्हरला कॉल करून त्याचे टूल्स, संसाधने आणि प्रॉम्प्ट्स यादीबद्ध केले आहे. तथापि, हा एक फारच व्यवहार्य दृष्टिकोन नाही. तुमचे वापरकर्ते एजंटिक युगात राहतात आणि ते प्रॉम्प्ट्स वापरायला आणि LLM शी संवाद साधायला अपेक्षित करतात. त्यांना याची काळजी नाही की तुम्ही तुमच्या क्षमता साठवण्यासाठी MCP वापरता; ते फक्त नैसर्गिक भाषेत संवाद साधण्याची अपेक्षा करतात. मग आपण हे कसे सोडवू? उत्तर म्हणजे क्लायंटमध्ये LLM जोडणे.

## अवलोकन

या धड्यामध्ये आपण आपल्या क्लायंटमध्ये LLM जोडण्यावर लक्ष केंद्रित करू आणि हे कसे तुमच्या वापरकर्त्यासाठी अधिक चांगला अनुभव प्रदान करते हे दाखवू.

## शिक्षण उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- LLM सह क्लायंट तयार करणे.
- LLM वापरून सहजपणे MCP सर्व्हरशी संवाद साधणे.
- क्लायंट बाजूस चांगला अंतिम वापरकर्ता अनुभव प्रदान करणे.

## दृष्टिकोन

आपण घेत असलेला दृष्टिकोन समजून घेऊया. LLM जोडणे सोपे वाटते, पण आपण खरोखरच हे करू का?

क्लायंट सर्व्हरशी कसे संवाद साधेल हे खालीलप्रमाणे आहे:

1. सर्व्हरशी कनेक्शन स्थापन करा.

1. क्षमता, प्रॉम्प्ट्स, संसाधने आणि टूल्स यादीबद्ध करा आणि त्यांच्या स्कीमा जतन करा.

1. एक LLM जोडा आणि जतन केलेल्या क्षमतांसह त्यांचा स्कीमा LLM समजेल अशा स्वरूपात पास करा.

1. वापरकर्त्याचा प्रॉम्प्ट हाताळा, क्लायंटने यादीबद्ध केलेल्या टूल्ससह तो LLM कडे पास करा.

उत्तम, आता आपण कसे करू शकतो हे उच्च पातळीवर समजले, तर खालील व्यायामामध्ये हे प्रयत्न करूया.

## व्यायाम: LLM सह क्लायंट तयार करणे

या व्यायामात, आपण आपल्या क्लायंटमध्ये LLM कसे जोडायचे ते शिकू.

### GitHub Personal Access Token वापरून प्रमाणीकरण

GitHub टोकन तयार करणे एक सोपी प्रक्रिया आहे. हे कसे करायचे:

- GitHub सेटिंग्जमध्ये जा – उजव्या वरच्या कोपऱ्यात आपला प्रोफाइल चित्र क्लिक करा आणि सेटिंग्ज निवडा.
- Developer Settings कडे जा – खाली स्क्रोल करा आणि Developer Settings क्लिक करा.
- Personal Access Tokens निवडा – Fine-grained tokens वर क्लिक करा आणि नंतर Generate new token करा.
- आपले टोकन कॉन्फिगर करा – संदर्भासाठी एक नोट जोडा, कालावधी सेट करा आणि आवश्यक परवानग्या (scopes) निवडा. या प्रकरणात Models परवानगी नक्की जोडा.
- Token तयार करा आणि कॉपी करा – Generate token वर क्लिक करा, आणि लगेच कॉपी करावे कारण नंतर ते पुन्हा पाहू शकणार नाही.

### -1- सर्व्हरशी कनेक्ट करा

आता सुरुवातीला आपला क्लायंट तयार करूया:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा वैधतेसाठी zod आयात करा

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

- आवश्यक लायब्ररीज इम्पोर्ट केल्या आहेत
- `client` आणि `openai` या दोन मेंबर्ससह एक वर्ग तयार केला आहे ज्याचा वापर आम्ही क्लायंटसाठी आणि LLM शी संवादासाठी करू.
- GitHub Models वापरण्यासाठी LLM उदाहरण कॉन्फिगर केले आहे, `baseUrl` सेट करून inference API कडे निर्देश केला आहे.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio कनेक्शनसाठी सर्व्हर पॅरामिटर्स तयार करा
server_params = StdioServerParameters(
    command="mcp",  # अमलात आणण्यायोग्य फाइल
    args=["run", "server.py"],  # पर्यायी कमांड लाइन अर्ग्युमेंट्स
    env=None,  # पर्यायी पर्यावरण चल
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

- MCP साठी आवश्यक लायब्ररीज इम्पोर्ट केल्या आहेत
- एक क्लायंट तयार केला आहे

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

प्रथम, तुमच्या `pom.xml` फाइलमध्ये LangChain4j अवलंबित्वे जोडा. MCP इंटीग्रेशन आणि GitHub Models सपोर्ट सक्षम करण्यासाठी खालील अवलंबित्व जोडा:

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

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // LLM ला GitHub मॉडेल वापरण्यासाठी कॉन्फिगर करा
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

- **LangChain4j अवलंबित्वे जोडली**: MCP इंटीग्रेशन, OpenAI अधिकृत क्लायंट, आणि GitHub Models सपोर्टसाठी आवश्यक
- **LangChain4j लायब्ररीज आयात केल्या**: MCP इंटीग्रेशन आणि OpenAI चॅट मॉडेल कार्यक्षमता साठी
- **`ChatLanguageModel` तयार केला**: GitHub Models वापरण्यासाठी तुमचा GitHub टोकन वापरुन कॉन्फिगर केला
- **HTTP ट्रांसपोर्ट सेट केला**: Server-Sent Events (SSE) वापरून MCP सर्व्हरशी कनेक्ट करण्यासाठी
- **MCP क्लायंट तयार केला**: जो सर्व्हरशी संवाद हाताळेल
- **LangChain4j चा अंगभूत MCP सपोर्ट वापरला**: ज्यामुळे LLMs आणि MCP सर्व्हर्समधील इंटीग्रेशन सहज होते

#### Rust

ही उदाहरणे मानते की तुमच्याकडे Rust आधारित MCP सर्व्हर चालू आहे. जर तुमच्याकडे नसेल तर [01-first-server](../01-first-server/README.md) धडा पहा, सर्व्हर तयार करण्यासाठी.

तुमचा Rust MCP सर्व्हर असल्यावर, टर्मिनल उघडा आणि सर्व्हरच्या त्याच निर्देशिकेत जा. नंतर खालील आदेश चालवा नवीन LLM क्लायंट प्रोजेक्ट तयार करण्यासाठी:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

तुमच्या `Cargo.toml` फाइलमध्ये खालील अवलंबित्वे जोडा:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI साठी अधिकृत Rust लायब्ररी नाही, पण `async-openai` क्रेट एका [समुदायाद्वारे सांभाळल्या जाणाऱ्या लायब्ररी](https://platform.openai.com/docs/libraries/rust#rust) आहे जी सामान्यतः वापरली जाते.

`src/main.rs` फाइल उघडा आणि त्याचा अंतर्भाग खालील कोडने बदला:

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

    // TODO: MCP साधन सूची मिळवा

    // TODO: साधन कॉलसह LLM संभाषण

    Ok(())
}
```

हा कोड एक बेसिक Rust अ‍ॅप्लिकेशन सेटअप करतो ज्यामुळे MCP सर्व्हर आणि GitHub Models शी LLM संवाद साधता येईल.

> [!IMPORTANT]
> अ‍ॅप्लिकेशन चालवण्यापूर्वी `OPENAI_API_KEY` पर्यावरण बदलशील GitHub टोकन सेट करणे आवश्यक आहे.

छान, पुढील टप्प्यासाठी, चला सर्व्हरवरील क्षमता यादीबद्ध करूया.

### -2- सर्व्हर क्षमतांची यादी करा

आता आपण सर्व्हरशी कनेक्ट होऊ आणि त्याच्या क्षमतांसाठी विचारू:

#### TypeScript

त्याच वर्गात खालील पद्धती जोडा:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // साधने सूचीबद्ध करीत आहे
    const toolsResult = await this.client.listTools();
}
```

वरील कोडमध्ये आपण:

- सर्व्हरशी कनेक्ट होण्यासाठी `connectToServer` कोड जोडला आहे.
- `run` पद्धत तयार केली आहे जिला आमच्या अ‍ॅप फ्लोची जबाबदारी दिली आहे. आतापर्यंत ती फक्त टूल्स सूचीबद्ध करते, पण आपण लवकरच त्यात अधिक काही जोडू.

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

- संसाधने आणि टूल्सची यादी घेतली आणि ती प्रिंट केली. टूल्ससाठी आम्ही मग वापरणार आहोत असलेले `inputSchema` देखील सूचीबद्ध केली.

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

- MCP सर्व्हरवर उपलब्ध टूल्स यादीबद्ध केली.
- प्रत्येक टूलसाठी नाव, वर्णन आणि त्याचा स्कीमा घेतला. हा नंतर टूल कॉलसाठी वापरला जाईल.

#### Java

```java
// एक साधन प्रदाता तयार करा जो MCP साधने आपोआप शोधतो
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP साधन प्रदाता आपोआप हाताळतो:
// - MCP सर्व्हरमधून उपलब्ध साधने यादी करणे
// - MCP साधन स्कीमांना LangChain4j फॉरमॅटमध्ये रूपांतरित करणे
// - साधन अंमलबजावणी आणि प्रतिसाद व्यवस्थापित करणे
```

वरील कोडमध्ये आपण:

- एक `McpToolProvider` तयार केला जो स्वतःच MCP सर्व्हरमधील सर्व टूल्स शोधतो आणि नोंदणी करतो
- टूल प्रोव्हायडर MCP टूल स्कीमा आणि LangChain4j च्या टूल फॉरमॅटमध्ये रूपांतरण अंतर्गत हाताळतो
- हा दृष्टिकोन मॅन्युअल टूल्सची यादी बनवणे आणि रूपांतरण प्रक्रिया गुप्त करत आहे

#### Rust

MCP सर्व्हरमधील टूल्स प्राप्त करण्यासाठी `list_tools` पद्धत वापरली जाते. `main` फंक्शनमध्ये MCP क्लायंट सेटअप केल्यानंतर खालील कोड जोडा:

```rust
// MCP टूल सूची मिळवा
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्व्हरच्या क्षमतांना LLM टूल्समध्ये रूपांतर करा

सर्व्हर क्षमतांची यादी केल्यानंतर पुढील चरण म्हणजे त्यांना LLM समजेल अशा स्वरूपात रुपांतरित करणे. एकदा ते केल्यावर, आपण या क्षमता आपल्या LLM ना टूल्स म्हणून देऊ शकतो.

#### TypeScript

1. MCP सर्व्हरकडून मिळालेल्या प्रतिसादाला LLM वापरू शकणाऱ्या टूल फॉरमॅटमध्ये रुपांतर करण्यासाठी खालील कोड जोडा:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // इनपुट_स्कीमा वर आधारित झोड स्कीमा तयार करा
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // टाइप स्पष्टपणे "function" म्हणून सेट करा
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

    वरील कोड MCP सर्व्हरमधून आलेल्या प्रतिसादाला LLM समजेल अशा टूल डिफिनिशन फॉरमॅटमध्ये रुपांतरित करतो.

1. नंतर `run` पद्धत अपडेट करू या जेणेकरून सर्व्हरच्या क्षमतांची यादी होईल:

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

    वरील कोडमध्ये `run` पद्धत अद्ययावत केली आहे ज्यात निकालाद्वारे मॅपिंग करतो आणि प्रत्येक नोंदीसाठी `openAiToolAdapter` कॉल करतो.

#### Python

1. प्रथम, खालील रूपांतरण फंक्शन तयार करू या

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

    `convert_to_llm_tools` फंक्शनमध्ये MCP टूल प्रतिसाद घेतल्यावर त्याला LLM समजेल अशा स्वरूपात रुपांतरीत करतो.

1. नंतर, आम्ही हा फंक्शन वापरून क्लायंट कोड अपडेट करूया:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    येथे आम्ही MCP टूल प्रतिसाद `convert_to_llm_tool` फंक्शनमध्ये पास करून LLM ला पाठवण्यायोग्य करत आहोत.

#### .NET

1. MCP टूल प्रतिसाद LLM समजेल अशा स्वरूपात रुपांतर करण्यासाठी कोड जोडू या:

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

- `ConvertFrom` फंक्शन तयार केले जे नाव, वर्णन आणि इनपुट स्कीमा ग्रहण करते.
- कार्यक्षमता विशिष्ट केली जी `FunctionDefinition` तयार करते आणि ते `ChatCompletionsDefinition` मध्ये पास होते. नंतर LLM ते समजतो.

1. आता या फंक्शनचा लाभ घेण्यासाठी काही विद्यमान कोड कसा अपडेट करायचा ते पाहू:

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
// नैसर्गिक भाषा संवादासाठी बोट इंटरफेस तयार करा
public interface Bot {
    String chat(String prompt);
}

// LLM आणि MCP साधने वापरून एआय सेवा कॉन्फिगर करा
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

वरील कोडमध्ये आपण:

- नैसर्गिक भाषेत संवादासाठी एक सोपा `Bot` इंटरफेस परिभाषित केला आहे
- LangChain4j चे `AiServices` वापरून LLM आणि MCP टूल प्रोव्हायडर स्वयंचलितपणे बांधले आहे
- फ्रेमवर्क स्वयंचलितपणे टूल स्कीमा रूपांतरण आणि फंक्शन कॉलिंग हाताळतो
- हा दृष्टिकोन मॅन्युअल टूल रूपांतरण टाळतो - LangChain4j MCP टूल्सना LLM-योग्य फॉरमॅटमध्ये रूपांतर करण्याच्या सर्व क्लिष्टता हाताळतो

#### Rust

MCP टूल प्रतिसाद LLM समजेल अशा स्वरूपात रुपांतर करण्यासाठी, आपण एक सहायक फंक्शन तयार करू जे टूल्सची यादी फॉरमॅट करेल. खालील कोड `main` फंक्शनच्या खाली `main.rs` मध्ये जोडा. हे LLM साठी विनंत्या करताना वापरले जाईल:

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

छान, आता आपण वापरकर्ता विनंत्या हाताळण्यासाठी तयार आहोत, तर पुढे जाऊया.

### -4- वापरकर्त्यांच्या प्रॉम्प्ट विनंती हाताळा

या कोड भागात, आपण वापरकर्त्यांच्या विनंत्या हाताळणार आहोत.

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


        // 2. सर्व्हरच्या साधनाला कॉल करा
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. परिणामासह काहीतरी करा
        // करायचे आहे

        }
    }
    ```

    वरील कोडमध्ये आपण:

    - `callTools` नावाची पद्धत जोडली आहे.
    - पद्धत LLM प्रतिसाद घेते आणि तपासते की कोणती टूल्स कॉल करण्यात आली आहेत का:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // टूल कॉल करा
        }
        ```

    - LLM संकेत दिल्यास टूल कॉल करते:

        ```typescript
        // 2. सर्व्हरच्या टूलला कॉल करा
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. निकालासह काही करा
        // करायचे आहे
        ```

1. आता `run` पद्धत अपडेट करा ज्यात LLM कॉल आणि `callTools` कॉल समाविष्ट असतील:

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

    // 2. LLM कॉल करणे
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM प्रतिसादामधून जा, प्रत्येक निवडीसाठी तपासा की त्यात टूल कॉल्स आहेत का
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

उत्तम, संपूर्ण कोड पाहूया:

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
            baseURL: "https://models.inference.ai.azure.com", // भविष्यात कदाचित या URL वर बदलावा लागेल: https://models.github.ai/inference
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
          // इनपुट_स्कीमाच्या आधारावर zod स्कीमा तयार करा
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // स्पष्टपणे टाइप "function" म्हणून सेट करा
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM प्रतिसादातून जा, प्रत्येक पर्यायासाठी तपासा की त्यात टूल कॉल आहे का
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

1. LLM कॉल करण्यासाठी आवश्यक काही आयात जोडा:

    ```python
    # एलएलएम
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. नंतर, LLM कॉल करण्यासाठी फंक्शन जोडा:

    ```python
    # ल्लम

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

    - MCP सर्व्हरवर सापडलेल्या आणि रूपांतरित केलेल्या फंक्शन्स LLM ला दिल्या.
    - नंतर LLM कॉल केला आणि फंक्शन्स दिल्या.
    - निकाल तपासला की कोणते फंक्शन्स कॉल करायचे आहेत.
    - शेवटी फंक्शन्सच्या अ‍ॅरेवर कॉल केला.

1. अंतिम चरण, मुख्य कोड अपडेट करूया:

    ```python
    prompt = "Add 2 to 20"

    # LLM ला विचारा कोणती साधने वापरायची आहेत, असल्यास
    functions_to_call = call_llm(prompt, functions)

    # सुचवलेल्या फंक्शन्सना कॉल करा
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    येथे, आपण:

    - `call_tool` वापरून MCP टूल कॉल करत आहोत, ज्याला LLM ने सांगितले आहे.
    - टूल कॉलच्या निकालाचा प्रिंट मिळवतो.

#### .NET

1. LLM प्रॉम्प्ट विनंतीसाठी काही कोड दाखवूयाः

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

    - MCP सर्व्हरवरून टूल्स मिळवले, `var tools = await GetMcpTools()`.
    - वापरकर्त्याचा प्रॉम्प्ट `userMessage` तयार केला.
    - मॉडेल आणि टूल्ससह पर्याय ठरवले.
    - LLM कडे विनंती केली.

1. शेवटी, LLM ने फंक्शन कॉल करायचा विचार केला आहे का ते पहा:

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

    - फंक्शन कॉल्स लूप केले.
    - प्रत्येक टूल कॉलसाठी नाव आणि अर्ग्युमेंट पार्स करून MCP सर्व्हरवर टूल कॉल केले. अंतिमतः निकाल प्रिंट केला.

पूर्ण कोड:

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
    // नैसर्गिक भाषा विनंत्या चालवा ज्या आपोआप MCP साधने वापरतात
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

- सोप्या नैसर्गिक भाषा प्रॉम्प्ट्स वापरून MCP सर्व्हर टूलशी संवाद साधला आहे
- LangChain4j फ्रेमवर्क स्वयंचलितपणे पुढील गोष्टी हाताळतो:
  - आवश्यकतेनुसार वापरकर्ता प्रॉम्प्ट्सना टूल कॉलमध्ये रूपांतरीत करणे
  - LLM च्या निर्णयावर आधारित योग्य MCP टूल्स कॉल करणे
  - LLM आणि MCP सर्व्हरमधील संभाषण प्रवाह व्यवस्थापित करणे
- `bot.chat()` पद्धत नैसर्गिक भाषेतील प्रतिसाद देते ज्यात MCP टूल्सचे निष्पन्न समाविष्ट असू शकते
- यामुळे वापरकर्त्यांसाठी एक सुलभ अनुभव तयार होतो जेथे त्यांना अंतर्निहित MCP अंमलबजावणी माहित असण्याची गरज नाही

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

इथे सर्वात जास्त काम घडते. आपण सुरुवातीच्या वापरकर्ता प्रॉम्प्टसह LLM कॉल करू, नंतर प्रतिसाद तपासू की काही टूल्स कॉल करायची गरज आहे का. असल्यास, त्या टूल्स कॉल करू आणि निरंतर LLM सोबत संभाषण चालू ठेवू जोपर्यंत आणखी टूल कॉलची गरज नसते आणि अंतिम प्रतिसाद प्राप्त होतो.

आपण LLM कडे अनेक कॉल करणार आहोत, म्हणून एक फंक्शन तयार करू जे LLM कॉल हाताळेल. खालील फंक्शन `main.rs` मध्ये जोडा:

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

हा फंक्शन LLM क्लायंट, संदेशांची यादी (वापरकर्ता प्रॉम्प्टसह), MCP सर्व्हरकडून टूल्स घेतो आणि LLM कडे विनंती पाठवतो, प्रतिसाद परत करतो.
LLM कडून आलेल्या प्रतिसादात `choices` नावाचा एक अ‍ॅरे असतो. आपल्याला निकाल प्रक्रिया करून तपासावे लागेल की कोणतेही `tool_calls` आहेत का. यामुळे आपल्याला समजेल की LLM एखादा विशिष्ट टूल कॉल करण्याची विनंती करत आहे ज्यास दिलेले आर्ग्युमेंट्स असतील. आपले `main.rs` फायलीच्या तळाशी खालील कोड जोडा ज्यायोगे LLM प्रतिसाद हाताळण्यासाठी एक फंक्शन परिभाषित होईल:

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

    // टूल कॉल्स हाताळा
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

            // टूल परिणाम संदेशांमध्ये जोडा
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // टूल परिणामांसह संभाषण सुरू ठेवा
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


जर `tool_calls` उपस्थित असतील, तर तो टूलची माहिती काढतो, MCP सर्व्हरला टूल विनंतीसह कॉल करतो, आणि परिणाम संभाषणाच्या मेसेजेसमध्ये जोडतो. नंतर LLM सह संभाषण चालू ठेवतो आणि मेसेजेसमध्ये सहाय्यकाचे प्रतिसाद व टूल कॉलचे परिणाम अद्ययावत होतात.

MCP कॉलसाठी LLM जे टूल कॉल माहिती परत करतो ती काढण्यासाठी आणखी एक हेल्पर फंक्शन जोडूया ज्याने कॉलसाठी आवश्यक सर्व काढले जाईल. आपले `main.rs` फायलीच्या तळाशी खालील कोड जोडा:

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


सर्व भाग एकत्र आल्यावर, आपण आता सुरुवातीचा युजर प्रॉम्प्ट हाताळू शकतो आणि LLM ला कॉल करू शकतो. आपले `main` फंक्शन खालील कोडसह अपडेट करा:

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


हे दोन आकड्यांचा बेरीज मागणारा सुरुवातीचा युजर प्रॉम्प्ट LLM कडे विचारेल, आणि प्रतिसाद प्रक्रियेसह टूल कॉल्स डायनामिकली हाताळेल.

छान, आपण यशस्वीरीत्या पूर्ण केले!

## असाइनमेंट

व्यायामातील कोड घेऊन अधिक टूल्ससह सर्व्हर तयार करा. नंतर व्यायामाप्रमाणे LLM असलेला क्लायंट तयार करा आणि विविध प्रॉम्प्ट्स वापरून तपासा की सर्व्हरचे सर्व टूल्स डायनामिकली कॉल होत आहेत का. असा क्लायंट तयार केल्याने शेवटचा वापरकर्ता चांगला वापरकर्ता अनुभव मिळवेल, ज्यांना अचूक क्लायंट कमांड्स ऐवजी फक्त प्रॉम्प्ट्स वापरता येतील आणि MCP सर्व्हर कॉल होतोय हे त्यांना कळणार नाही.

## सोल्यूशन

[सोल्यूशन](./solution/README.md)

## मुख्य मुद्दे

- आपल्या क्लायंटमध्ये LLM जोडल्याने वापरकर्त्यांना MCP सर्व्हर्सशी संवाद साधण्याचा चांगला मार्ग मिळतो.
- MCP सर्व्हरचा प्रतिसाद LLM समजून घेईल अशा स्वरूपात रूपांतरित करणे आवश्यक असते.

## नमुने

- [Java कॅल्क्युलेटर](../samples/java/calculator/README.md)
- [.Net कॅल्क्युलेटर](../../../../03-GettingStarted/samples/csharp)
- [JavaScript कॅल्क्युलेटर](../samples/javascript/README.md)
- [TypeScript कॅल्क्युलेटर](../samples/typescript/README.md)
- [Python कॅल्क्युलेटर](../../../../03-GettingStarted/samples/python)
- [Rust कॅल्क्युलेटर](../../../../03-GettingStarted/samples/rust)

## अतिरिक्त संसाधने

## पुढे काय

- पुढे: [Visual Studio Code वापरून सर्व्हर वापरणे](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृत्रिम अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते याची कृपया जाणीव ठेवा. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी अनुवाद करणे शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही समजुतीतील किंवा अर्थव्यर्थतेतील गैरसमजांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->