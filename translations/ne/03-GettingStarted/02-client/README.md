# क्लाइंट सिर्जना गर्दै

क्लाइंटहरू विशेष अनुप्रयोग वा स्क्रिप्टहरू हुन् जुन सिधै MCP सर्भरसँग सञ्चार गरी स्रोत, उपकरण, र प्रॉम्प्टहरूको अनुरोध गर्छन्। इन्स्पेक्टर उपकरण प्रयोग गर्नु भन्दा फरक, जुन सर्भरसँग अन्तरक्रिया गर्न दृश्यात्मक इन्टरफेस प्रदान गर्छ, तपाईंको आफ्नै क्लाइंट लेख्दा प्रोग्रामिङ र स्वचालित अन्तरक्रियाहरू सम्भव हुन्छ। यसले विकासकर्ताहरूलाई MCP क्षमताहरू आफ्नै कार्यप्रवाहमा समावेश गर्न, कार्यहरू स्वचालित गर्न, र विशेष आवश्यकताहरू अनुसार अनुकूलित समाधानहरू निर्माण गर्न सक्षम बनाउँछ।

## अवलोकन

यो पाठले Model Context Protocol (MCP) प्रणालीभित्र क्लाइंटहरूको अवधारणा परिचय गराउँछ। तपाईंले आफ्नै क्लाइंट कसरी लेख्ने र यसलाई MCP सर्भरसँग कसरी जडान गर्ने सिक्नेछ।

## सिकाई उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- क्लाइंटले के गर्न सक्छ बुझ्न।
- आफ्नै क्लाइंट लेख्न।
- क्लाइंटलाई MCP सर्भरसँग जडान गरी परीक्षण गर्न ताकि पछिल्लो आशा अनुसार कार्य गर्दछ भनी सुनिश्चित गर्न।

## क्लाइंट लेख्नमा के आवश्यक हुन्छ?

क्लाइंट लेख्न तपाईंले तलका कुराहरू गर्नुपर्नेछ:

- **सही पुस्तकालयहरू आयात गर्नुहोस्**। तपाईंले पहिले प्रयोग गरेको पुस्तकालय नै प्रयोग गर्नु हुनेछ, तर फरक संरचनाहरू।
- **क्लाइंटको एउटा उदाहरण सिर्जना गर्नुहोस्**। यसले क्लाइंट उदाहरण बनाउने र छनौट गरिएको ट्रान्सपोर्ट विधिसँग जडान गर्ने समावेश हुन्छ।
- **कुन स्रोत सूचीबद्ध गर्ने निर्णय गर्नुहोस्**। तपाईंको MCP सर्भर स्रोत, उपकरण र प्रॉम्प्टहरूसँग आउँछ, तपाईंले कुन सूचीबद्ध गर्ने निर्णय गर्नुपर्नेछ।
- **क्लाइंटलाई होस्ट अनुप्रयोगमा एकीकृत गर्नुहोस्**। सर्भरको क्षमताहरू थाहा पाए पछि, तपाईंले यसलाई होस्ट अनुप्रयोगसँग एकीकृत गर्नुपर्छ ताकि प्रयोगकर्ताले प्रॉम्प्ट वा अन्य कमाण्ड टाइप गर्दा सम्बद्ध सर्भर सुविधाहरू चल्नेछन्।

अब हामीले उच्च तहमा के गर्ने हो बुझ्यौँ, अब एउटा उदाहरण हेर्नेछौं।

### एउटा उदाहरण क्लाइंट

यस उदाहरण क्लाइंटमा हेरौं:

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// सूची प्रॉम्प्टहरू
const prompts = await client.listPrompts();

// एक प्रॉम्प्ट प्राप्त गर्नुहोस्
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// स्रोतहरूको सूची
const resources = await client.listResources();

// स्रोत पढ्नुहोस्
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// उपकरण कल गर्नुहोस्
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

पछिल्ला कोडमा हामीले:

- पुस्तकालय आयात गर्यौं
- क्लाइंटको एउटा उदाहरण सिर्जना गर्यौं र stdio प्रयोग गरेर ट्रान्सपोर्टको रूपमा जडान गर्यौं।
- प्रॉम्प्टहरू, स्रोतहरू र उपकरणहरू सूचीबद्ध गर्यौं र तिनीहरू सबैलाई कल गर्यौं।

त्यसैले तपाईंलाई एउटा क्लाइंट छ जुन MCP सर्भरसँग कुरा गर्न सक्छ।

अर्को अभ्यास खण्डमा हामी प्रत्येक कोड अंशलाई विस्तारमा विश्लेषण गर्नेछौं।

## अभ्यास: क्लाइंट लेख्दै

माथि भनेझैं, हामी विस्तारमा कोड बुझ्ने समय लिऔँ र तपाईं चाहनु भयो भने कोड सँगै गर्न सक्नुहुन्छ।

### -1- पुस्तकालय आयात गर्दै

आवश्यक पुस्तकालयहरू आयात गरौं, हामीलाई क्लाइंट र छनौट गरिएको ट्रान्सपोर्ट प्रोटोकल stdio को रेफरेंस चाहिन्छ। stdio स्थानीय मेसिनमाथि चल्ने कुराहरूका लागि प्रोटोकल हो। SSE अर्को ट्रान्सपोर्ट प्रोटोकल हो जुन भविष्यका अध्यायहरूमा देखाउनेछौं, त्यो तपाईंको अर्को विकल्प हो। अहिले stdio सँग अगाडि बढौं।

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### Java

Java को लागि, तपाईंले अघिल्लो अभ्यासको MCP सर्भरसँग जडान गर्ने क्लाइंट बनाउनु हुनेछ। [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) बाटै सोही Java Spring Boot प्रोजेक्ट संरचना प्रयोग गरी `src/main/java/com/microsoft/mcp/sample/client/` फोल्डरमा `SDKClient` नामको नयाँ Java क्लास बनाउनुहोस् र तलका आयातहरू थप्नुहोस्:

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

तपाईंले आफ्नो `Cargo.toml` फाइलमा तलका निर्भरताहरू थप्नुपर्नेछ।

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

त्यसपछि, तपाईंले क्लाइंट कोडमा आवश्यक पुस्तकालयहरू आयात गर्न सक्नुहुन्छ।

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

अब इन्स्ट्यान्सिएसनतर्फ अगाडि बढौं।

### -2- क्लाइंट र ट्रान्सपोर्ट इन्स्ट्यान्स बनाउँदै

हामीलाई ट्रान्सपोर्ट र क्लाइंट दुवैको उदाहरण सिर्जना गर्न आवश्यक छ:

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

पछिल्ला कोडमा हामीले:

- stdio ट्रान्सपोर्टको एक उदाहरण बनायौं। यसले कसरी सर्भर फेला पार्ने र सुरु गर्ने कमाण्ड र आर्गुमेन्टहरू निर्दिष्ट गर्छ, जुन हामीले क्लाइंट बनाउँदा गर्नुपर्नेछ।

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- क्लाइंटलाई नाम र संस्करण दिई इन्स्ट्यान्स गरिएको छ।

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- क्लाइंटलाई छनौट गरिएको ट्रान्सपोर्टमा जडान गरिएको छ।

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio जडानका लागि सर्भर प्यारामिटरहरू सिर्जना गर्नुहोस्
server_params = StdioServerParameters(
    command="mcp",  # निष्पादन योग्य
    args=["run", "server.py"],  # वैकल्पिक कमाण्ड लाइन तर्कहरू
    env=None,  # वैकल्पिक वातावरण चरहरू
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # जडान सुरु गर्नुहोस्
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

पछिल्ला कोडमा हामीले:

- आवश्यक पुस्तकालयहरू आयात गर्यौं
- सर्भर चलाउन प्रयोग हुने सर्भर प्यारामिटर वस्तु इन्स्ट्यान्स गर्यौं ताकि हामी त्यसमा क्लाइंटमार्फत जडान हुन सकौँ।
- `run` मेथड परिभाषित गर्यौं जसले `stdio_client` कल गर्छ जसले क्लाइंट सत्र शुरु गर्छ।
- एक एंट्री पोइन्ट सिर्जना गर्यौं जहाँ हामी `asyncio.run` लाई `run` मेथड दिन्छौं।

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

पछिल्ला कोडमा हामीले:

- आवश्यक पुस्तकालय आयात गर्यौं।
- stdio ट्रान्सपोर्ट बनायौं र `mcpClient` नामको क्लाइंट सिर्जना गर्यौं। यो यसको प्रयोग गरेर हामी MCP सर्भरका सुविधाहरू सूचीबद्ध र कल गर्नेछौं।

नोट, "Arguments" मा तपाईं *.csproj* वा कार्यान्वयन योग्य फाइल दुवै प्रयोग गर्न सक्नुहुन्छ।

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // तपाईंको ग्राहक तर्क यहाँ जान्छ
    }
}
```

पछिल्ला कोडमा हामीले:

- मुख्य मेथड बनायौं जसले MCP सर्भर चल्ने `http://localhost:8080` मा SSE ट्रान्सपोर्ट सेटअप गर्छ।
- क्लाइंट क्लास बनायौं जुन ट्रान्सपोर्टलाई कन्स्ट्रक्टर प्यारामिटरको रूपमा लिन्छ।
- `run` मेथडमा, हामी ट्रान्सपोर्ट प्रयोग गरेर समकालीन MCP क्लाइंट सिर्जना गर्यौं र कनेक्शन सुरु गर्यौं।
- SSE ट्रान्सपोर्ट प्रयोग गर्यौं जुन Java Spring Boot MCP सर्भरहरूको HTTP आधारित सञ्चारका लागि उपयुक्त हो।

#### Rust

यस Rust क्लाइंटमा मानिन्छ कि सर्भर त्यहि डाइरेक्टोरीमा रहेको "calculator-server" नामको साथी प्रोजेक्ट हो। तलको कोडले सर्भर सुरु गरी जडान गर्छ।

```rust
async fn main() -> Result<(), RmcpError> {
    // सर्भरलाई एउटै डाइरेक्टरीमा रहेको "calculator-server" नामक सहयोद्धा परियोजना भनेर मान्नुहोस्
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // गर्नु पर्ने काम: सुरुवात गर्नुहोस्

    // गर्नु पर्ने काम: उपकरणहरूको सूची बनाउनुहोस्

    // गर्नु पर्ने काम: {"a": 3, "b": 2} तर्कहरूसहित add उपकरण कल गर्नुहोस्

    client.cancel().await?;
    Ok(())
}
```

### -3- सर्भर सुविधाहरू सूचीबद्ध गर्दै

अब हाम्रो क्लाइंट छ जुन जडान हुन सक्छ जब प्रोग्राम चलाइन्छ। यद्यपि, यसले वास्तवमा सुविधाहरू सूचीबद्ध गर्दैन, त्यसैले अब त्यो गरौं:

#### TypeScript

```typescript
// सूची संकेतहरू
const prompts = await client.listPrompts();

// सूची स्रोतहरू
const resources = await client.listResources();

// सूची उपकरणहरू
const tools = await client.listTools();
```

#### Python

```python
# उपलब्ध स्रोतहरूको सूची बनाउनुहोस्
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# उपलब्ध उपकरणहरूको सूची बनाउनुहोस्
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

यहाँ हामी उपलब्ध स्रोतहरू `list_resources()` र उपकरणहरू `list_tools` सूचीबद्ध गरी प्रिन्ट गर्छौं।

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

माथि एक उदाहरण छ कसरी सर्भरका उपकरण सूचीबद्ध गर्ने। प्रत्येक उपकरणको नाम हामी पछि प्रिन्ट गर्छौं।

#### Java

```java
// उपकरणहरू सूचीबद्ध गर्नुहोस् र प्रदर्शन गर्नुहोस्
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// तपाईं जडान पुष्टि गर्न सर्भरलाई पिङ पनि गर्न सक्नुहुन्छ
client.ping();
```

पछिल्ला कोडमा हामीले:

- MCP सर्भरबाट सबै उपकरण पाउन `listTools()` कल गर्यौं।
- सर्भरसँग जडान ठीक छ की छैन जाँच्न `ping()` प्रयोग गर्यौं।
- `ListToolsResult` मा सबै उपकरणहरूका नाम, विवरण र इनपुट स्किमाहरू समावेश हुन्छ।

शानदार, अब हामीले सबै सुविधाहरू समात्यौं। अब प्रश्न छ हामी कहिले प्रयोग गर्ने? यो क्लाइंट धेरै सरल छ, यसको अर्थ हामीले सुविधाहरू चाहिँदा मात्र स्पष्ट रूपमा कल गर्नुपर्नेछ। अर्को अध्यायमा, हामीसँग ठूलो भाषा मोडेल (LLM) उपलब्ध क्लाइंट सिर्जना गर्नेछौं। अहिलेका लागि, आऊँ सर्भरमा सुविधाहरू कसरी कल गर्ने हेर्छौं।

#### Rust

मुख्य फंक्शनमा, क्लाइंट सुरु गरेपछि, हामी सर्भर सुरु गरी केही सुविधाहरू सूचीबद्ध गर्न सक्छौं।

```rust
// सुरुवात गर्नुहोस्
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// उपकरणहरूको सूची
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- सुविधाहरू कल गर्दै

सुविधाहरू कल गर्न हामीले सहि आर्गुमेन्टहरू र कतिपय अवस्थामा कल गर्न खोजिएको नाम निर्दिष्ट गर्नुपर्छ।

#### TypeScript

```typescript

// स्रोत पढ्नुहोस्
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// उपकरण कल गर्नुहोस्
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// संकेत कल गर्नुहोस्
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

पछिल्ला कोडमा हामीले:

- एक स्रोत पढ्यौं, `readResource()` कल गरेर `uri` निर्दिष्ट गर्यौं। सर्भर साइडमा यो यसरी देखिन्छ:

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    हाम्रो `uri` मान `file://example.txt` सर्भरमा रहेको `file://{name}` सँग मेल खान्छ। `example.txt` लाई `name` मा मैप गरिन्छ।

- एक उपकरण कल गर्यौं, नाम र आर्गुमेन्टहरू यसरी दिन्छौं:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- प्रॉम्प्ट प्राप्त गर्यौं, `getPrompt()` लाई नाम र आर्गुमेन्टहरू दिएर। सर्भर कोड यस प्रकार छ:

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    र तपाईंको क्लाइंट कोड यसरी देखिन्छ जुन सर्भरमा घोषणा गरिएकोसँग मेल खान्छ:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# स्रोत पढ्नुहोस्
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# एक उपकरण कल गर्नुहोस्
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

पछिल्ला कोडमा हामीले:

- `greeting` नामक स्रोत पढ्यौं `read_resource` प्रयोग गरी।
- `add` नामक उपकरण कल गर्यौं `call_tool` प्रयोग गरी।

#### .NET

1. उपकरण कल गर्न केही कोड थपौं:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. नतिजा प्रिन्ट गर्न यो कोड प्रयोग गरौं:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// विभिन्न गणक उपकरणहरू कल गर्नुहोस्
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

पछिल्ला कोडमा हामीले:

- `callTool()` मेथड मार्फत विभिन्न क्याल्कुलेटर उपकरणहरू `CallToolRequest` वस्तुहरूसहित कल गर्यौं।
- प्रत्येक उपकरण कलले उपकरण नाम र आवश्यक आर्गुमेन्टहरूको `Map` प्रदान गर्छ।
- सर्भर उपकरणहरूले विशिष्ट प्यारामिटर नामहरू (जस्तै "a", "b") अपेक्षा गर्छन्।
- नतिजाहरू `CallToolResult` वस्तुहरूका रूपमा फिर्ता हुन्छन् जुन सर्भरको प्रतिक्रिया समावेश गर्छ।

#### Rust

```rust
// अर्कुमेन्टहरूसहित add उपकरणलाई कल गर्नुहोस् = {"a": 3, "b": 2}
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- क्लाइंट चलाउनुहोस्

क्लाइंट चलाउन, टर्मिनलमा तलको कमाण्ड टाइप गर्नुहोस्:

#### TypeScript

*package.json* को "scripts" सेक्सनमा तल थप्नुहोस्:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

क्लाइंटलाई यसरी कल गर्नुहोस्:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

पहिले, सुनिश्चित गर्नुहोस् तपाईंको MCP सर्भर `http://localhost:8080` मा चलिरहेको छ। त्यसपछि क्लाइंट चलाउनुहोस्:

```bash
# तपाईंको परियोजना बनाउनुहोस्
./mvnw clean compile

# क्लाइन्ट चलाउनुहोस्
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

अथवा, समाधान फोल्डर `03-GettingStarted\02-client\solution\java` मा उपलब्ध सम्पूर्ण क्लाइंट प्रोजेक्ट चलाउन सक्नुहुन्छ:

```bash
# समाधान डाइरेक्टरीमा जानुहोस्
cd 03-GettingStarted/02-client/solution/java

# JAR निर्माण गर्नुहोस् र चलाउनुहोस्
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## असाइनमेन्ट

यस असाइनमेन्टमा, तपाईंले सिकेको प्रयोग गरी आफ्नै क्लाइंट बनाउनुहुनेछ।

तपाईंले प्रयोग गर्न सक्ने यो सर्भर छ जुन क्लाइंट कोड मार्फत कल गर्नेछ, के तपाईं त्यस सर्भरमा थप सुविधाहरू थप्न सक्नुहुन्छ हेर्नुहोस् र यसलाई अझ रोचक बनाउनुहोस्।

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एक MCP सर्भर सिर्जना गर्नुहोस्
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// एक थप उपकरण थप्नुहोस्
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक गतिशील अभिवादन स्रोत थप्नुहोस्
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// stdin मा सन्देशहरू प्राप्त गर्न र stdout मा सन्देशहरू पठाउन सुरु गर्नुहोस्

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# एउटा MCP सर्भर बनाउनुहोस्
mcp = FastMCP("Demo")


# एउटा थप्ने उपकरण थप्नुहोस्
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एउटा गतिशील अभिवादन स्रोत थप्नुहोस्
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

यस प्रोजेक्टलाई हेरौं कसरि [प्रॉम्प्ट र स्रोतहरू थप्ने](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)।

त्यसैगरी, यो लिंकमा कसरि [प्रॉम्प्ट र स्रोतहरू कल गर्ने](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) जान्न सकिन्छ।

### Rust

[अघिल्लो खण्ड](../../../../03-GettingStarted/01-first-server) मा, तपाईंले Rust प्रयोग गरी साधारण MCP सर्भर कसरी बनाउने सिक्नुभयो। तपाईं यसमा थप निर्माण गर्न सक्नुहुन्छ वा थप Rust आधारित MCP सर्भर उदाहरणहरूका लागि यो लिंक जाँच्न सक्नुहुन्छ: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## समाधान

**समाधान फोल्डर** मा सम्पूर्ण, चलाउन तयार क्लाइंट कार्यान्वयनहरू छन् जसले यस ट्यूटरियलमा समावेश सबै अवधारणाहरू देखाउँछन्। प्रत्येक समाधानमा छुट्टाछुट्टै क्लाइंट र सर्भर कोड स्वयं-सम्पूर्ण प्रोजेक्टहरूमा व्यवस्थित छन्।

### 📁 समाधान संरचना

समाधान निर्देशिका प्रोग्रामिङ भाषाको आधारमा व्यवस्थित छ:

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 प्रत्येक समाधानले के समावेश गर्छ

प्रत्येक भाषा-विशेष समाधानले प्रदान गर्छ:

- **ट्यूटोरियलका सबै सुविधाहरूसहित पूर्ण क्लाइंट कार्यान्वयन**
- **सही निर्भरता र कन्फिगरेसन सहित कार्यरत प्रोजेक्ट संरचना**
- **सरल सेटअप र कार्यान्वयनका लागि बिल्ड र रन स्क्रिप्टहरू**
- **भाषागत विशिष्ट निर्देशनहरूसहित विस्तृत README**
- **त्रुटि ह्यान्डलिङ र नतिजा प्रशोधनका उदाहरणहरू**

### 📖 समाधानहरू प्रयोग गर्दै

1. **आफ्नो मनपर्ने भाषा फोल्डरमा नेभिगेट गर्नुहोस्**:

   ```bash
   cd solution/typescript/    # टाइपस्क्रिप्टको लागि
   cd solution/java/          # जाभाको लागि
   cd solution/python/        # पायथनको लागि
   cd solution/dotnet/        # .नेटको लागि
   ```

2. **हरेक फोल्डरमा README निर्देशनहरू पालना गर्नुहोस्**:
   - निर्भरता स्थापना
   - प्रोजेक्ट निर्माण
   - क्लाइंट चलाउने

3. **तपाईंले यसरी उदाहरण आउटपुट हेर्नु पर्नेछ**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

पूरा दस्तावेज र चरण-दर-चरण निर्देशनहरूको लागि हेर्नुहोस्: **[📖 समाधान दस्तावेज](./solution/README.md)**

## 🎯 सम्पूर्ण उदाहरणहरू

हामीले यस ट्यूटरियलमा कभर गरिएका सबै प्रोग्रामिङ भाषाहरूका लागि सम्पूर्ण, कार्यरत क्लाइंट कार्यान्वयनहरू प्रदान गरेका छौं। यी उदाहरणहरूले माथि वर्णन गरिएका सबै कार्यक्षमता प्रदर्शन गर्छन् र तपाईंको आफ्नै प्रोजेक्टको लागि सन्दर्भ वा सुरुवाती बिन्दुको रूपमा प्रयोग गर्न सकिन्छ।

### उपलब्ध सम्पूर्ण उदाहरणहरू

| भाषा | फाइल | विवरण |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ट्रान्सपोर्ट प्रयोग गरी पूर्ण Java क्लाइंट जसमा व्यापक त्रुटि ह्यान्डलिङ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ट्रान्सपोर्ट प्रयोग गरी पूर्ण C# क्लाइंट जसले सर्भर स्वचालित सुरु गर्छ |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | पूर्ण MCP प्रोटोकल समर्थन भएको TypeScript क्लाइंट |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await ढाँचाहरू प्रयोग गरी पूर्ण Python क्लाइंट |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio प्रयोग गरी асिंक्रोनस अपरेशन्सका लागि पूर्ण Rust क्लाइंट |

हरेक पूर्ण उदाहरणले समावेश गर्छ:
- ✅ **जोड स्थापित गर्ने** र त्रुटि व्यवस्थापन
- ✅ **सर्भर पत्ता लगाउने** (उपकरणहरू, स्रोतहरू, उपयुक्त ठाउँमा प्रम्प्टहरू)
- ✅ **क्याल्कुलेटर अपरेसनहरू** (जोड, घटाउ, गुणा, भाग, सहायता)
- ✅ **परिणाम प्रशोधन** र स्वरूपित आउटपुट
- ✅ **व्यापक त्रुटि व्यवस्थापन**
- ✅ **सफा, दस्तावेजित कोड** चरण-द्वारा-चरण टिप्पणीहरू सहित

### पूर्ण उदाहरणहरूको साथ सुरु गर्दै

1. माथिको तालिकाबाट **तपाईंको रुचाइएको भाषा** रोज्नुहोस्
2. पूर्ण कार्यान्वयन बुझ्न **पूर्ण उदाहरण फाइल** समीक्षा गर्नुहोस्
3. [`complete_examples.md`](./complete_examples.md) मा निर्देशनहरू अनुसार **उदाहरण चलाउनुस्**
4. तपाईंको विशेष प्रयोगका लागि **उदाहरण परिमार्जन र विस्तार गर्नुस्**

यी उदाहरणहरू चलाउन र अनुकूलन गर्न विस्तृत दस्तावेजीकरणको लागि हेर्नुहोस्: **[📖 पूर्ण उदाहरण दस्तावेजीकरण](./complete_examples.md)**

### 💡 समाधान र पूर्ण उदाहरणहरू

| **समाधान फोल्डर** | **पूर्ण उदाहरणहरू** |
|--------------------|--------------------- |
| बिल्ड फाइलसहित पूर्ण परियोजना संरचना | एकल फाइल कार्यान्वयनहरू |
| निर्भरतासहित तत्पर चलाउन तयार | केन्द्रित कोड उदाहरणहरू |
| उत्पादनजस्तै सेटअप | शैक्षिक सन्दर्भ |
| भाषा-विशिष्ट उपकरणहरू | क्रस-भाषा तुलनात्मक |

दुवै दृष्टिकोणहरू उपयोगी छन् - पूर्ण परियोजनाका लागि **समाधान फोल्डर** प्रयोग गर्नुहोस् र सिकाइ तथा सन्दर्भका लागि **पूर्ण उदाहरणहरू**।

## मुख्य सार

यस अध्यायको मुख्य सार क्लाइन्टहरू बारे निम्न छन्:

- सर्भरमा रहेका सुविधाहरू पत्ता लगाउन र बोलाउन दुवैका लागि प्रयोग गर्न सकिन्छ।
- क्लाइन्टले आफैं सुरु हुँदा पनि सर्भर सुरु गर्न सक्छ (जस्तै यस अध्यायमा) तर क्लाइन्टहरूले चलिरहेको सर्भरसँग पनि जडान गर्न सक्छन्।
- यो सर्वर क्षमताहरू परीक्षण गर्ने एउटा उत्कृष्ट माध्यम हो, पूर्व अध्यायमा वर्णन गरिएको Inspector जस्तै वैकल्पिकहरू पछाडि।

## अतिरिक्त स्रोतहरू

- [MCP मा क्लाइन्टहरू निर्माण](https://modelcontextprotocol.io/quickstart/client)

## नमूनाहरू

- [Java क्याल्कुलेटर](../samples/java/calculator/README.md)
- [.Net क्याल्कुलेटर](../../../../03-GettingStarted/samples/csharp)
- [JavaScript क्याल्कुलेटर](../samples/javascript/README.md)
- [TypeScript क्याल्कुलेटर](../samples/typescript/README.md)
- [Python क्याल्कुलेटर](../../../../03-GettingStarted/samples/python)
- [Rust क्याल्कुलेटर](../../../../03-GettingStarted/samples/rust)

## के छ अर्को

- अर्को: [LLM सहित क्लाइन्ट सिर्जना गर्दै](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यस दस्तावेजलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौँ, तर कृपया बुझ्नुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्दछ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनेछ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न भएका कुनै पनि गलतफहमी वा दुष्प्रतिनिध्यता के लागि हामी जिम्मेवार छैनौँ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->