# LLM के साथ क्लाइंट बनाना

अब तक, आपने देखा है कि सर्वर और क्लाइंट कैसे बनाते हैं। क्लाइंट सर्वर को स्पष्ट रूप से कॉल करके उसके टूल, संसाधन और प्रॉम्प्ट सूचीबद्ध कर सकता था। हालांकि, यह एक व्यावहारिक तरीका नहीं है। आपके उपयोगकर्ता एजेंटिक युग में रहते हैं और प्रॉम्प्ट का उपयोग करने और LLM के साथ संवाद करने की उम्मीद करते हैं। वे इस बात की परवाह नहीं करते कि आप अपनी क्षमताओं को संग्रहीत करने के लिए MCP का उपयोग करते हैं या नहीं; वे केवल स्वाभाविक भाषा का उपयोग करके बातचीत की उम्मीद करते हैं। तो हम इसे कैसे हल करें? समाधान है क्लाइंट में एक LLM जोड़ना।

## अवलोकन

इस पाठ में हम क्लाइंट में एक LLM जोड़ने पर फोकस करेंगे और दिखाएंगे कि यह आपके उपयोगकर्ता के लिए एक बेहतर अनुभव कैसे प्रदान करता है।

## शिक्षण उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- एक LLM के साथ क्लाइंट बनाना।
- MCP सर्वर के साथ एक LLM का उपयोग करके सहजता से संवाद करना।
- क्लाइंट पक्ष पर बेहतर अंतिम उपयोगकर्ता अनुभव प्रदान करना।

## दृष्टिकोण

आइए उस दृष्टिकोण को समझने की कोशिश करें जो हमें अपनाना है। LLM जोड़ना सरल लगता है, लेकिन क्या हम वास्तव में ऐसा करेंगे?

यहाँ बताया गया है कि क्लाइंट सर्वर के साथ कैसे संवाद करेगा:

1. सर्वर के साथ कनेक्शन स्थापित करें।

1. क्षमताओं, प्रॉम्प्ट, संसाधनों और टूल्स की सूची बनाएं, और उनके स्कीमा को सहेजें।

1. एक LLM जोड़ें और सहेजी गई क्षमताओं और उनके स्कीमा को LLM के समझने वाले प्रारूप में पास करें।

1. उपयोगकर्ता प्रॉम्प्ट को क्लाइंट द्वारा सूचीबद्ध टूल्स के साथ LLM को पास करके संभालें।

बहुत अच्छा, अब हम समझ गए कि इसे उच्च स्तर पर कैसे किया जा सकता है, चलिए नीचे दिए गए अभ्यास में इसे आज़माते हैं।

## अभ्यास: LLM के साथ क्लाइंट बनाना

इस अभ्यास में, हम अपने क्लाइंट में एक LLM जोड़ना सीखेंगे।

### GitHub पर्सनल एक्सेस टोकन का उपयोग करके प्रमाणीकरण

GitHub टोकन बनाना एक सरल प्रक्रिया है। यह है कि आप इसे कैसे कर सकते हैं:

- GitHub सेटिंग्स पर जाएं – अपने प्रोफ़ाइल चित्र पर ऊपर दाईं ओर क्लिक करें और सेटिंग्स चुनें।
- डेवलपर सेटिंग्स पर नेविगेट करें – नीचे स्क्रॉल करें और डेवलपर सेटिंग्स पर क्लिक करें।
- पर्सनल एक्सेस टोकन चुनें – फाइन-ग्रेनड टोकन पर क्लिक करें और फिर नया टोकन जनरेट करें।
- अपने टोकन को कॉन्फ़िगर करें – संदर्भ के लिए एक नोट जोड़ें, समाप्ति तिथि सेट करें, और आवश्यक स्कोप्स (अनुमतियाँ) चुनें। इस मामले में सुनिश्चित करें कि मॉडल्स अनुमति जोड़ी गई हो।
- टोकन जनरेट करें और कॉपी करें – जनरेट टोकन पर क्लिक करें, और इसे तुरंत कॉपी करना न भूलें, क्योंकि आप इसे बाद में नहीं देख पाएंगे।

### -1- सर्वर से कनेक्ट करें

आइए पहले अपना क्लाइंट बनाएं:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा मान्यता के लिए zod आयात करें

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

पिछले कोड में हमने:

- आवश्यक लाइब्रेरीज को इंपोर्ट किया
- एक क्लास बनाया जिसमें दो सदस्य हैं, `client` और `openai`, जो क्रमशः क्लाइंट प्रबंधन और LLM के साथ इंटरैक्शन में मदद करेंगे।
- अपने LLM इंस्टेंस को GitHub Models का उपयोग करने के लिए कॉन्फ़िगर किया, `baseUrl` को inference API की ओर सेट करके।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio कनेक्शन के लिए सर्वर पैरामीटर बनाएं
server_params = StdioServerParameters(
    command="mcp",  # निष्पादन योग्य
    args=["run", "server.py"],  # वैकल्पिक कमांड लाइन तर्क
    env=None,  # वैकल्पिक पर्यावरण चर
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # कनेक्शन प्रारंभ करें
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

पिछले कोड में हमने:

- MCP के लिए आवश्यक लाइब्रेरीज को इंपोर्ट किया
- एक क्लाइंट बनाया

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

सबसे पहले, आपको अपनी `pom.xml` फाइल में LangChain4j डिपेंडेंसी जोड़नी होगी। MCP इंटीग्रेशन और GitHub Models सपोर्ट को सक्षम करने के लिए ये डिपेंडेंसियां जोड़ें:

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

फिर अपनी Java क्लाइंट क्लास बनाएं:

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
    
    public static void main(String[] args) throws Exception {        // LLM को GitHub मॉडल्स का उपयोग करने के लिए कॉन्फ़िगर करें
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // सर्वर से कनेक्ट करने के लिए MCP ट्रांसपोर्ट बनाएं
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP क्लाइंट बनाएं
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

पिछले कोड में हमने:

- **LangChain4j डिपेंडेंसियां जोड़ीं**: MCP इंटीग्रेशन, OpenAI आधिकारिक क्लाइंट और GitHub Models सपोर्ट के लिए आवश्यक
- **LangChain4j लाइब्रेरीज इंपोर्ट कीं**: MCP इंटीग्रेशन और OpenAI चैट मॉडल के लिए
- **`ChatLanguageModel` बनाया**: GitHub मॉडल्स का उपयोग करने के लिए GitHub टोकन के साथ कॉन्फ़िगर किया
- **HTTP ट्रांसपोर्ट सेटअप किया**: MCP सर्वर से कनेक्ट करने के लिए Server-Sent Events (SSE) का उपयोग करते हुए
- **MCP क्लाइंट बनाया**: जो सर्वर के साथ संवाद को संभालेगा
- **LangChain4j के अंतर्निर्मित MCP सपोर्ट का उपयोग किया**: जो LLM और MCP सर्वर के बीच इंटीग्रेशन को सरल बनाता है

#### Rust

यह उदाहरण मानता है कि आपके पास Rust आधारित MCP सर्वर चल रहा है। यदि आपके पास नहीं है, तो सर्वर बनाने के लिए [01-first-server](../01-first-server/README.md) पाठ देखें।

जब आपका Rust MCP सर्वर तैयार हो, तो टर्मिनल खोलें और उसी निर्देशिका में जाएं जहाँ सर्वर है। फिर निम्न कमांड चलाकर नया LLM क्लाइंट प्रोजेक्ट बनाएं:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

अपने `Cargo.toml` फाइल में निम्नलिखित डिपेंडेंसियां जोड़ें:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI के लिए आधिकारिक Rust लाइब्रेरी नहीं है, लेकिन `async-openai` क्रेट एक [समुदाय द्वारा रखी गई लाइब्रेरी](https://platform.openai.com/docs/libraries/rust#rust) है जिसे आमतौर पर उपयोग किया जाता है।

`src/main.rs` फाइल खोलें और इसके कंटेंट को निम्नलिखित कोड से बदलें:

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

    // OpenAI क्लाइंट सेटअप करें
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP क्लाइंट सेटअप करें
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

    // TODO: MCP टूल सूची प्राप्त करें

    // TODO: टूल कॉल्स के साथ LLM बातचीत

    Ok(())
}
```

यह कोड एक बेसिक Rust एप्लिकेशन सेटअप करता है जो MCP सर्वर और GitHub Models से LLM इंटरैक्शन के लिए कनेक्ट होगा।

> [!IMPORTANT]
> एप्लिकेशन चलाने से पहले, कृपया `OPENAI_API_KEY` पर्यावरण वेरिएबल को अपने GitHub टोकन के साथ सेट करें।

बहुत अच्छा, अगला कदम है MCP सर्वर पर उपलब्ध क्षमताओं को सूचीबद्ध करना।

### -2- सर्वर क्षमताओं की सूची बनाना

अब हम सर्वर से कनेक्ट करेंगे और उसकी क्षमताओं के लिए पूछेंगे:

#### Typescript

उसी क्लास में, निम्नलिखित मेथड जोड़ें:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // उपकरण सूचीबद्ध करना
    const toolsResult = await this.client.listTools();
}
```

पिछले कोड में हमने:

- सर्वर से कनेक्ट करने के लिए कोड जोड़ा, `connectToServer`।
- एक `run` मेथड बनाया जो हमारी ऐप फ्लो को हैंडल करता है। अभी तक यह केवल टूल्स की सूची बनाता है, लेकिन हम इसमें जल्द ही और जोड़ेंगे।

#### Python

```python
# उपलब्ध संसाधनों की सूची बनाएं
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# उपलब्ध उपकरणों की सूची बनाएं
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

इसे हमने जोड़ा है:

- संसाधनों और टूल्स की सूची बनाई और उनका प्रिंट किया। टूल्स के लिए हम `inputSchema` भी सूचीबद्ध करते हैं, जिसे बाद में उपयोग करेंगे।

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

पिछले कोड में हमने:

- MCP सर्वर पर उपलब्ध टूल्स की लिस्टिंग की
- प्रत्येक टूल का नाम, विवरण और उसका स्कीमा सूचीबद्ध किया। बाद में हम इसका उपयोग टूल्स कॉल करने के लिए करेंगे।

#### Java

```java
// एक टूल प्रोवाइडर बनाएँ जो स्वतः MCP टूल्स की खोज करता है
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP टूल प्रोवाइडर स्वतः निम्नलिखित संभालता है:
// - MCP सर्वर से उपलब्ध टूल्स की सूची बनाना
// - MCP टूल स्कीमाओं को LangChain4j फॉर्मेट में परिवर्तित करना
// - टूल निष्पादन और प्रतिक्रियाओं का प्रबंधन करना
```

पिछले कोड में हमने:

- एक `McpToolProvider` बनाया जो स्वचालित रूप से MCP सर्वर से सभी टूल्स को खोजता और रजिस्टर करता है
- टूल प्रोवाइडर MCP टूल स्कीमा और LangChain4j के टूल फॉर्मेट के बीच कन्वर्ज़न को अंदर से संभालता है
- यह तरीका मैनुअल टूल लिस्टिंग और कन्वर्ज़न प्रक्रिया को छिपा देता है

#### Rust

MCP सर्वर से टूल्स प्राप्त करना `list_tools` मेथड का उपयोग करके किया जाता है। अपने `main` फ़ंक्शन में, MCP क्लाइंट सेटअप करने के बाद, निम्न कोड जोड़ें:

```rust
// MCP टूल सूची प्राप्त करें
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्वर क्षमताओं को LLM टूल्स में कन्वर्ट करना

अगला कदम सर्वर क्षमताओं को ऐसे प्रारूप में कन्वर्ट करना है जिसे LLM समझ सके। एक बार जब हम ऐसा कर लेते हैं, तो हम इन क्षमताओं को अपने LLM को टूल्स के रूप में प्रदान कर सकते हैं।

#### TypeScript

1. MCP सर्वर से प्रतिक्रिया को कन्वर्ट करने के लिए निम्नलिखित कोड जोड़ें ताकि LLM यह टूल फॉर्मेट समझ सके:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // इनपुट_स्कीमा के आधार पर एक Zod स्कीमा बनाएं
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // प्रकार को स्पष्ट रूप से "function" सेट करें
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

    उपरोक्त कोड MCP सर्वर से प्रतिक्रिया लेकर उसे एक टूल डेफिनिशन फॉर्मेट में कन्वर्ट करता है जिसे LLM समझ सके।

1. अब `run` मेथड को अपडेट करें ताकि सर्वर क्षमताओं की सूची बन सके:

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

    पिछले कोड में, हमने `run` मेथड को अपडेट किया ताकि यह परिणाम के माध्यम से मैप करे और प्रत्येक प्रवेश के लिए `openAiToolAdapter` को कॉल करे।

#### Python

1. सबसे पहले, निम्न कन्वर्टर फ़ंक्शन बनाएं

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

    ऊपर दिए गए `convert_to_llm_tools` फ़ंक्शन में, हम MCP टूल रिस्पॉन्स लेते हैं और इसे एक ऐसा फॉर्मेट में कन्वर्ट करते हैं जिसे LLM समझ सके।

1. अगला कदम, अपने क्लाइंट को इस फ़ंक्शन का उपयोग करने के लिए अपडेट करें:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    यहाँ हम MCP टूल रिस्पॉन्स को LLM को फीड करने के लिए कन्वर्ट करने हेतु `convert_to_llm_tool` कॉल जोड़ रहे हैं।

#### .NET

1. MCP टूल रिस्पॉन्स को LLM के समझने लायक बनाने के लिए कोड जोड़ें:

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

पिछले कोड में हमने:

- एक `ConvertFrom` फ़ंक्शन बनाया जो नाम, विवरण और इनपुट स्कीमा लेता है।
- एक फंक्शन बनाया जो `FunctionDefinition` बनाता है जिसे `ChatCompletionsDefinition` को पास किया जाता है। ये वही होता है जिसे LLM समझ सकता है।

1. अब देखें कि हम कैसे मौजूदा कोड को इस फ़ंक्शन के उपयोग के लिए अपडेट कर सकते हैं:

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
// स्वाभाविक भाषा के इंटरैक्शन के लिए एक बॉट इंटरफेस बनाएं
public interface Bot {
    String chat(String prompt);
}

// LLM और MCP उपकरणों के साथ AI सेवा को कॉन्फ़िगर करें
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

पिछले कोड में हमने:

- प्राकृतिक भाषा इंटरैक्शन के लिए एक सरल `Bot` इंटरफ़ेस परिभाषित किया
- LangChain4j के `AiServices` का उपयोग किया जो LLM को MCP टूल प्रोवाइडर के साथ स्वचालित रूप से बाँधता है
- फ्रेमवर्क टूल स्कीमा कन्वर्ज़न और फंक्शन कॉल को स्वचालित तरीके से हैंडल करता है
- यह तरीका मैनुअल टूल कन्वर्ज़न का काम खत्म करता है - LangChain4j MCP टूल्स को LLM-अनुकूल प्रारूप में कन्वर्ट करने की सारी जटिलता संभालता है

#### Rust

MCP टूल रिस्पॉन्स को LLM के समझने वाले फॉर्मेट में कन्वर्ट करने के लिए, हम एक हेल्पर फ़ंक्शन जोड़ेंगे जो टूल्स की लिस्टिंग का फॉर्मेट बनाएगा। `main` फ़ंक्शन के नीचे अपनी `main.rs` फ़ाइल में निम्न कोड जोड़ें। यह LLM को अनुरोध करते समय कॉल किया जाएगा:

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

बहुत अच्छा, अब हम किसी उपयोगकर्ता अनुरोध को संभालने के लिए तैयार हैं, चलिए अगला भाग देखते हैं।

### -4- उपयोगकर्ता प्रॉम्प्ट अनुरोध को संभालना

इस कोड भाग में, हम उपयोगकर्ता अनुरोधों को संभालेंगे।

#### TypeScript

1. एक मेथड जोड़ें जो हमारे LLM को कॉल करने के लिए उपयोग होगा:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. सर्वर के टूल को कॉल करें
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. परिणाम के साथ कुछ करें
        // करने के लिए

        }
    }
    ```

    पिछले कोड में हमने:

    - एक `callTools` मेथड जोड़ा।
    - यह मेथड LLM प्रतिक्रिया लेता है और जांचता है कि कौन से टूल्स कॉल किए गए हैं, यदि कोई हो:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // उपकरण कॉल करें
        }
        ```

    - यदि LLM ने संकेत दिया कि कोई टूल कॉल किया जाना चाहिए, तो उसे कॉल करता है:

        ```typescript
        // 2. सर्वर के टूल को कॉल करें
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. परिणाम के साथ कुछ करें
        // करने के लिए
        ```

1. `run` मेथड को अपडेट करें ताकि LLM को कॉल किया जा सके और `callTools` को बुलाया जाए:

    ```typescript

    // 1. LLM के लिए इनपुट के रूप में संदेश बनाएं
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM को कॉल करना
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM प्रतिक्रिया को देखें, हर विकल्प के लिए, जांचें कि उसमें टूल कॉल हैं या नहीं
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

बहुत बढ़िया, पूरा कोड देखें:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा प्रमाणीकरण के लिए zod आयात करें

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // भविष्य में इस URL को बदलना पड़ सकता है: https://models.github.ai/inference
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
          // इनपुट_स्कीमा के आधार पर एक zod स्कीमा बनाएं
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // स्पष्ट रूप से प्रकार "function" सेट करें
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
    
    
          // 2. सर्वर के टूल को कॉल करें
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. परिणाम के साथ कुछ करें
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
    
        // 1. LLM प्रतिक्रिया को देखें, प्रत्येक विकल्प के लिए जांचें कि क्या उसमें टूल कॉल हैं
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

1. LLM को कॉल करने के लिए आवश्यक कुछ इंपोर्ट जोड़ें:

    ```python
    # एलएलएम
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. अगला, वह फ़ंक्शन जोड़ें जो LLM को कॉल करेगा:

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
            # वैकल्पिक पैरामीटर
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

    पिछले कोड में हमने:

    - MCP सर्वर पर पाए गए और कन्वर्ट किए गए फ़ंक्शन्स को LLM को पास किया।
    - फिर LLM को कहा गया।
    - रेस्पॉन्स का निरीक्षण किया कि कौन से फंक्शन्स कॉल किए जाना चाहिए।
    - अंत में, कॉल करने के लिए फंक्शन्स की सूची पास की।

1. अंतिम चरण, मुख्य कोड अपडेट करें:

    ```python
    prompt = "Add 2 to 20"

    # LLM से पूछें कि सभी कौन से टूल्स हैं, यदि कोई हो तो
    functions_to_call = call_llm(prompt, functions)

    # सुझाई गई फंक्शंस को कॉल करें
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    उपरोक्त कोड में हमने:

    - MCP टूल को `call_tool` के माध्यम से कॉल किया, वह फंक्शन जो LLM ने हमारे प्रॉम्प्ट के आधार पर कॉल करने के लिए सुझाया था।
    - टूल कॉल का रिजल्ट MCP सर्वर को प्रिंट किया।

#### .NET

1. LLM प्रॉम्प्ट अनुरोध करने के लिए कुछ कोड दिखाते हैं:

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

    पिछले कोड में हमने:

    - MCP सर्वर से टूल्स प्राप्त किए, `var tools = await GetMcpTools()`.
    - एक उपयोगकर्ता प्रॉम्प्ट `userMessage` परिभाषित किया।
    - मॉडल तथा टूल्स निर्दिष्ट करते हुए विकल्प ऑब्जेक्ट बनाया।
    - LLM के लिए अनुरोध किया।

1. अंतिम चरण, देखें कि LLM को क्या लगता है कि हमें कोई फ़ंक्शन कॉल करना चाहिए:

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

    पिछले कोड में हमने:

    - फंक्शन कॉल्स की सूची का लूप बनाया।
    - प्रत्येक टूल कॉल के लिए नाम और तर्क निकाले और MCP क्लाइंट का उपयोग करके MCP सर्वर पर टूल कॉल किया। अंत में परिणाम प्रिंट किया।

पूरा कोड देखें:

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
    // स्वचालित रूप से MCP उपकरणों का उपयोग करने वाले प्राकृतिक भाषा अनुरोधों को निष्पादित करें
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

पिछले कोड में हमने:

- सरल प्राकृतिक भाषा प्रॉम्प्ट का उपयोग करके MCP सर्वर टूल्स के साथ इंटरैक्ट किया
- LangChain4j फ्रेमवर्क स्वचालित रूप से संभालता है:
  - आवश्यक होने पर उपयोगकर्ता प्रॉम्प्ट को टूल कॉल में कन्वर्ट करना
  - LLM के निर्णय के आधार पर उपयुक्त MCP टूल्स कॉल करना
  - LLM और MCP सर्वर के बीच बातचीत का प्रवाह प्रबंधित करना
- `bot.chat()` मेथड प्राकृतिक भाषा में उत्तर लौटाता है जिसमें MCP टूल निष्पादन के परिणाम शामिल हो सकते हैं
- यह तरीका उपयोगकर्ता को एक सहज अनुभव देता है जहाँ उन्हें MCP के अंतर्निहित कार्यान्वयन के बारे में जानने की आवश्यकता नहीं होती

पूरा कोड उदाहरण:

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

यहाँ अधिकांश कार्य होते हैं। हम LLM को प्रारंभिक उपयोगकर्ता प्रॉम्प्ट के साथ कॉल करेंगे, फिर प्रतिक्रिया को प्रोसेस करेंगे यह देखने के लिए कि कोई टूल कॉल करने की जरूरत है या नहीं। यदि है, तो हम उन टूल्स को कॉल करेंगे और LLM के साथ बातचीत को जारी रखेंगे जब तक कि और टूल कॉल की जरूरत न हो और हमारे पास अंतिम उत्तर न हो।

हम कई बार LLM को कॉल करेंगे, इसलिए चलिए एक फ़ंक्शन परिभाषित करते हैं जो LLM कॉल को संभालेगा। इसे अपनी `main.rs` फ़ाइल में जोड़ें:

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

यह फ़ंक्शन LLM क्लाइंट, संदेशों की सूची (जिसमें उपयोगकर्ता प्रॉम्प्ट शामिल है), MCP सर्वर के टूल्स को लेता है, और LLM को अनुरोध भेजता है, फिर प्रतिक्रिया लौटाता है।
LLM से प्रतिक्रिया में `choices` की एक श्रृंखला होगी। हमें यह देखने के लिए परिणाम को संसाधित करना होगा कि क्या कोई `tool_calls` मौजूद हैं। यह हमें बताता है कि LLM विशिष्ट टूल को आर्गुमेंट्स के साथ कॉल करने का अनुरोध कर रहा है। LLM प्रतिक्रिया को संभालने के लिए एक फ़ंक्शन परिभाषित करने के लिए अपने `main.rs` फाइल के नीचे निम्नलिखित कोड जोड़ें:

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

    // सामग्री उपलब्ध होने पर प्रिंट करें
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // उपकरण कॉल को संभालें
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // सहायक संदेश जोड़ें

        // प्रत्येक उपकरण कॉल को निष्पादित करें
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // संदेशों में उपकरण परिणाम जोड़ें
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // उपकरण परिणामों के साथ बातचीत जारी रखें
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


यदि `tool_calls` मौजूद हैं, तो यह टूल की जानकारी निकालता है, MCP सर्वर को टूल अनुरोध के साथ कॉल करता है, और परिणामों को बातचीत के संदेशों में जोड़ता है। इसके बाद यह LLM के साथ बातचीत जारी रखता है और संदेश सहायक की प्रतिक्रिया और टूल कॉल परिणामों के साथ अपडेट हो जाते हैं।

MCP कॉल के लिए LLM द्वारा लौटाई गई टूल कॉल जानकारी निकालने के लिए, हम एक और सहायता फ़ंक्शन जोड़ेंगे जो कॉल करने के लिए आवश्यक सभी चीज़ों को निकालेगा। अपने `main.rs` फाइल के नीचे निम्नलिखित कोड जोड़ें:

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


सभी टुकड़े जगह पर होने के साथ, अब हम प्रारंभिक उपयोगकर्ता प्रॉम्प्ट को संभाल सकते हैं और LLM को कॉल कर सकते हैं। अपने `main` फ़ंक्शन को निम्नलिखित कोड शामिल करने के लिए अपडेट करें:

```rust
// टूल कॉल के साथ LLM बातचीत
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


यह प्रारंभिक उपयोगकर्ता प्रॉम्प्ट के साथ LLM से प्रश्न करेगा जो दो संख्याओं का योग पूछता है, और यह प्रतिक्रिया को संसाधित करेगा ताकि टूल कॉल्स को गतिशील रूप से संभाला जा सके।

बहुत बढ़िया, आपने इसे कर लिया!

## असाइनमेंट

अभ्यास से कोड लेकर सर्वर को और अधिक टूल्स के साथ बनाएं। फिर एक LLM के साथ क्लाइंट बनाएं, जैसा कि अभ्यास में है, और विभिन्न प्रॉम्प्ट्स के साथ इसका परीक्षण करें ताकि यह सुनिश्चित हो सके कि आपके सभी सर्वर टूल्स गतिशील रूप से कॉल हो रहे हैं। क्लाइंट बनाने का यह तरीका अंतिम उपयोगकर्ता को बेहतरीन अनुभव देता है क्योंकि वे प्रॉम्प्ट्स का उपयोग कर सकते हैं, सटीक क्लाइंट कमांड्स के बजाय, और किसी भी MCP सर्वर को कॉल किए जाने से अनजाने रहेंगे।

## समाधान

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## मुख्य बातें

- अपने क्लाइंट में LLM जोड़ना उपयोगकर्ताओं को MCP सर्वर के साथ बेहतर इंटरैक्शन का तरीका प्रदान करता है।
- आपको MCP सर्वर की प्रतिक्रिया को कुछ इस तरह परिवर्तित करना होगा जिसे LLM समझ सके।

## नमूने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## अतिरिक्त संसाधन

## आगे क्या

- अगला: [Visual Studio Code का उपयोग करके सर्वर का उपभोग करना](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी भाषा में अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं होंगे।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->