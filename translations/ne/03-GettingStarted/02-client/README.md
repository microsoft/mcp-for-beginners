# क्लाइन्ट सिर्जना गर्दै

क्लाइन्टहरू कस्टम अनुप्रयोगहरू वा स्क्रिप्टहरू हुन् जसले resources, tools, र prompts अनुरोध गर्न सीधै MCP सर्भर संग सम्पर्क गर्छन्। इन्स्पेक्टर टुल प्रयोग गर्नुभन्दा फरक, जसले सर्भर सँग इन्टरएक्ट गर्न ग्राफिकल इन्टरफेस प्रदान गर्दछ, आफैंको क्लाइन्ट लेख्नु प्रोग्राममैटिक र स्वचालित इन्टरएक्शन गर्न सक्षम बनाउँछ। यसले विकासकर्ताहरूलाई MCP क्षमताहरू आफ्नै workflow मा समावेश गर्न, कार्यहरू स्वचालित गर्न, र विशेष आवश्यकताहरू अनुरूप कस्टम समाधानहरू बनाउन अनुमति दिन्छ।

## अवलोकन

यस पाठले Model Context Protocol (MCP) पारिस्थितिकीमा क्लाइन्टहरूको अवधारणालाई परिचय गराउँछ। तपाईं आफैंको क्लाइन्ट कसरी लेख्ने र त्यो क्लाइन्ट कसरी MCP सर्भर सँग जडान गर्ने भनेर सिक्नुहुनेछ।

## सिकाई उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईं गर्न सक्षम हुनुहुनेछ:

- क्लाइन्ट के गर्न सक्छ बुझ्ने।
- आफैंको क्लाइन्ट लेख्ने।
- क्लाइन्टलाई MCP सर्भर सँग जडान गरी परीक्षण गर्ने ताकि सर्भरले अपेक्षित रूपमा काम गर्छ भनी सुनिश्चित गर्न।

## क्लाइन्ट लेख्न के के आवश्यक हुन्छ?

क्लाइन्ट लेख्न, तपाईंले तलका कुरा गर्नुपर्नेछ:

- **सही लाइब्रेरीहरू आयात गर्नुहोस्**। तपाईंले पहिले जस्तै लाइब्रेरी प्रयोग गर्नुहुनेछ, तर फरक संरचनाहरू हुनेछन्।
- **क्लाइन्टको उदाहरण सिर्जना गर्नुहोस्**। यसले क्लाइन्टको उदाहरण बनाउने र छानिएको ट्रान्सपोर्ट विधि सङ्ग जडान गर्ने समावेश गर्दछ।
- **कुन स्रोतहरू सूचीकृत गर्ने छनोट गर्नुहोस्**। तपाईंको MCP सर्भरमा स्रोतहरू, उपकरणहरू र प्रॉम्प्टहरू हुन्छन्, कुन सूचीकृत गर्ने निर्णय गर्नुहोस्।
- **क्लाइन्टलाई होस्ट अनुप्रयोगमा एकीकृत गर्नुहोस्**। सर्भरका क्षमताहरू थाहा पाएपछि, तपाईंको होस्ट अनुप्रयोगमा यसलाई एकीकृत गर्नुहोस् ताकि प्रयोगकर्ताले प्रॉम्प्ट वा अन्य कमाण्ड टाइप गर्दा सर्भरको सम्बन्धित सुविधा सक्रिय होस्।

अब हामीले उच्च तहमा के गर्ने भनी बुझिसकेका छौं, अब एउटा उदाहरण हेरौं।

### एउटा उदाहरण क्लाइन्ट

यो उदाहरण क्लाइन्ट हेरौँ:

### टाइपस्क्रिप्ट

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

// एउटा प्रॉम्प्ट प्राप्त गर्नुहोस्
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// स्रोतहरू सूचीबद्ध गर्नुहोस्
const resources = await client.listResources();

// एउटा स्रोत पढ्नुहोस्
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// एउटा उपकरण बोलाउनुहोस्
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

माथिको कोडमा हामीले:

- लाइब्रेरीहरू आयात गर्‍यौं
- क्लाइन्टको एक उदाहरण सिर्जना गर्‍यौं र stdio ट्रान्सपोर्ट प्रयोग गरी जडान गर्‍यौं।
- प्रॉम्प्टहरू, स्रोतहरू र उपकरणहरूको सूची बनाएर ती सबै सक्रिय गर्यौं।

त्यहाँ छ, एक क्लाइन्ट जसले MCP सर्भर सँग कुरा गर्न सक्छ।

आगामी अभ्यास खण्डमा हामी हरेक कोड टुक्रालाई विस्तारमा व्याख्या गर्नेछौं।

## अभ्यास: क्लाइन्ट लेख्दै

माथि जस्तै, अब हामी कोड स्पष्ट पार्दै पढ्नेछौं, र हतार नगरी कोडसँगै लैजानेछौं।

### -1- लाइब्रेरीहरू आयात गर्दै

आवश्यक लाइब्रेरीहरू आयात गरौं, हामीलाई क्लाइन्ट र छानिएको ट्रान्सपोर्ट प्रोटोकल stdio को संदर्भ चाहिन्छ। stdio यो प्रोटोकल हो जुन तपाइँको स्थानीय मेसिनमा चलाउन डिजाइन गरिएको छ। SSE अर्को ट्रान्सपोर्ट प्रोटोकल हो जुन हामी भविष्यका अध्यायहरूमा देखाउनेछौं तर अहिले stdio नै जारी राखौँ।

#### टाइपस्क्रिप्ट

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### पाइथन

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

#### जाभा

जाभा लागि, तपाईंले पहिलेको अभ्यासबाट MCP सर्भरमा जडान गर्ने क्लाइन्ट तयार गर्नु हुनेछ। [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) बाट उही Java Spring Boot प्रोजेक्ट संरचना प्रयोग गर्दै, `src/main/java/com/microsoft/mcp/sample/client/` फोल्डरमा `SDKClient` नामको नयाँ जाभा क्लास सिर्जना गर्नुहोस् र निम्न आयातहरू थप्नुहोस्:

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

#### रस्टी

निम्न निर्भरताहरू तपाईंको `Cargo.toml` फाइलमा थप्नुपर्नेछ।

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

त्यसपछि, तपाईं क्लाइन्ट कोडमा आवश्यक लाइब्रेरीहरू आयात गर्न सक्नुहुनेछ।

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

अब हामी उदाहरण सिर्जना तर्फ बढौं।

### -2- क्लाइन्ट र ट्रान्सपोर्टको उदाहरण सिर्जना गर्दै

हामी ट्रान्सपोर्टको र क्लाइन्टको उदाहरण बनाउनुपर्नेछ:

#### टाइपस्क्रिप्ट

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

माथिको कोडमा हामीले:

- stdio ट्रान्सपोर्टको उदाहरण सिर्जना गर्यौं। यसले कसरी सर्भर भेट्न र सुरु गर्न कमाण्ड र तर्कहरू निर्दिष्ट गर्छ, जुन क्लाइन्ट बनाउँदा आवश्यक हुन्छ।

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- क्लाइन्टलाई नाम र संस्करण दिई सिर्जना गर्यौं।

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- क्लाइन्टलाई छानिएको ट्रान्सपोर्टसँग जडान गर्यौं।

    ```typescript
    await client.connect(transport);
    ```

#### पाइथन

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio जडानको लागि सर्भर प्यारामिटरहरू बनाउनुहोस्
server_params = StdioServerParameters(
    command="mcp",  # कार्यान्वयन योग्य
    args=["run", "server.py"],  # वैकल्पिक कमाण्ड लाइन तर्कहरू
    env=None,  # वैकल्पिक वातावरण भेरिएबलहरू
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

माथिको कोडमा हामीले:

- आवश्यक लाइब्रेरीहरू आयात गर्यौं।
- सर्भर प्यारामिटरको वस्तु सिर्जना गर्यौं जसले सर्भर चलाउन प्रयोग हुन्छ।
- `run` मेथड परिभाषित गर्यौं जुन `stdio_client` बोलाउँछ र ग्राहक सत्र सुरु गर्छ।
- `asyncio.run` मा `run` मेथडलाई प्रदान गर्ने इंट्री पोइन्ट बनायौं।

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

माथिको कोडमा हामीले:

- आवश्यक लाइब्रेरीहरू आयात गर्यौं।
- stdio ट्रान्सपोर्ट बनाई `mcpClient` नामक क्लाइन्ट बनाएर MCP सर्भरका फीचरहरू सूचीबद्ध र कल गर्न तयारी गर्यौं।

तल "Arguments" मा, तपाईंले *.csproj* वा executable दुवै उल्लेख गर्न सक्नुहुन्छ।

#### जाभा

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

माथिको कोडमा हामीले:

- मुख्य मेथड सिर्जना गर्यौं जसले `http://localhost:8080` मा SSE ट्रान्सपोर्ट सेटअप गर्छ, जहाँ MCP सर्भर चलिरहेको छ।
- कन्स्ट्रक्टरमा ट्रान्सपोर्ट लिने क्लाइन्ट क्लास बनायौं।
- `run` मेथडमा ट्रान्सपोर्टको साथ सिंक्रोनस MCP क्लाइन्ट सिर्जना र कनेक्शन सुरु गर्यौं।
- Java Spring Boot MCP सर्भरको लागि HTTP आधारित संवादमा SSE ट्रान्सपोर्ट प्रयोग गर्यौं।

#### रस्टी

यो रस्टी क्लाइन्ट सर्भरलाई "calculator-server" नामको सान्निध्य प्रोजेक्ट मान्दछ। तलको कोडले सर्भर सुरु गरेर जडान गर्छ।

```rust
async fn main() -> Result<(), RmcpError> {
    // सर्भरलाई एउटै डाइरेक्टरीमा रहेको "calculator-server" नामको सहोदर परियोजना मान्नुहोस्
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

    // TODO: सुरु गर्नुहोस्

    // TODO: उपकरणहरूको सूची बनाउनुहोस्

    // TODO: add उपकरणलाई तर्कहरू {"a": 3, "b": 2} सहित कल गर्नुहोस्

    client.cancel().await?;
    Ok(())
}
```

### -3- सर्भर सुविधाहरू सूचीबद्ध गर्दै

अब, हामीसँग क्लाइन्ट छ जुन प्रोग्राम चलाउँदा जडान हुन्छ। तर, यसले आफ्ना सुविधाहरू सूचीबद्ध गर्दैन, त्यसो हेरौं:

#### टाइपस्क्रिप्ट

```typescript
// सूची प्रॉम्प्टहरू
const prompts = await client.listPrompts();

// सूची स्रोतहरू
const resources = await client.listResources();

// सूची उपकरणहरू
const tools = await client.listTools();
```

#### पाइथन

```python
# उपलब्ध स्रोतहरू सूचीबद्ध गर्नुहोस्
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# उपलब्ध उपकरणहरू सूचीबद्ध गर्नुहोस्
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

यहाँ हामीले उपलब्ध स्रोतहरू `list_resources()` र उपकरणहरू `list_tools()` सूचीबद्ध गरी मुद्रण गर्यौं।

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

माथि सर्भरका उपकरणहरू कसरी सूचीबद्ध गर्ने देखाइएको छ। प्रत्येक उपकरणको नाम हामी मुद्रण गर्छौं।

#### जाभा

```java
// उपकरणहरूको सूची बनाएर प्रदर्शन गर्नुहोस्
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// तपाईं कनेक्सन प्रमाणित गर्न सर्भरलाई पिङ पनि गर्न सक्नुहुन्छ
client.ping();
```

माथिको कोडमा हामीले:

- `listTools()` कल गरेर सर्भरका सबै उपकरणहरू पायौं।
- `ping()` कल गरेर सर्भरसँगको जडान काम गरिरहेको सत्यापित गर्यौं।
- `ListToolsResult` मा सबै उपकरणहरूको नाम, विवरण र इनपुट स्किमाहरू समावेश छन्।

अब हामीले सबै सुविधा सूचीबद्ध गर्यौं। प्रश्न के हुन्छ, कहिले यी प्रयोग गर्ने? यो क्लाइन्ट सरल छ, यसमा सुविधा प्रयोग गर्न स्पस्ट रूपमा कल गर्नुपर्छ। अर्को अध्यायमा हामी अझ उन्नत क्लाइन्ट बनाउनेछौं जसले आफैंको ठूलो भाषा मोडेल (LLM) एक्सेस गर्न सक्छ। अहिलेलाई, सर्भर सुविधा कसरी कल गर्ने हेर्नुहोस्:

#### रस्टी

मुख्य फङ्सनमा, क्लाइन्ट इन्स्टेन्ससहित सर्भर सुरु गरेर केहि सुविधा सूचीबद्ध गरिन्छ।

```rust
// आरम्भ गर्नुहोस्
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// उपकरणहरूको सूची गर्नुहोस्
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- सुविधा कल गर्दै

सुविधा कल गर्न, सही तर्कहरू र कहिलेकाहीँ कल गर्ने नाम निर्दिष्ट गर्नु आवश्यक हुन्छ।

#### टाइपस्क्रिप्ट

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

माथिको कोडमा हामीले:

- स्रोत पढ्यौं, `readResource()` कल गर्दै `uri` दिइयो। सर्भरपक्षमा यसरी हुन्छ:

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

    हाम्रो `uri` मान `file://example.txt` सर्भरको `file://{name}` सँग मेल खान्छ। `example.txt` लाई `name` मानिन्छ।

- उपकरण कल गर्यौं, यसको `name` र `arguments` दिइयो:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- प्रॉम्प्ट प्राप्त गर्न, `getPrompt()` कल गरियो `name` र `arguments` सहित। सर्भर कोड:

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

    त्यसैले तपाईँको क्लाइन्ट कोड यसरी देखिन्छ, सर्भरसँग मेल खानको लागि:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### पाइथन

```python
# स्रोत पढ्नुहोस्
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# उपकरण कल गर्नुहोस्
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

माथिको कोडमा हामीले:

- `greeting` स्रोत `read_resource` प्रयोग गरी कल गर्यौं।
- `add` नामक उपकरण `call_tool` प्रयोग गरी कार्यान्वयन गर्यौं।

#### .NET

1. उपकरण कल गर्न थप कोड:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. नतिजा देखाउन कोड:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### जाभा

```java
// विभिन्न क्याल्कुलेटर उपकरणहरूलाई कल गर्नुहोस्
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

माथिको कोडमा हामीले:

- `callTool()` विधि प्रयोग गरी धेरै क्यालकुलेटर उपकरणहरू कल गर्यौं।
- प्रत्येक उपकरण कल उपकरण नाम र आवश्यक `Map` तर्कहरू दिन्छ।
- सर्भर उपकरणहरू विशिष्ट प्यारामिटर नामहरू (जस्तै "a", "b" गणितीय लागि) अपेक्षित गर्छन्।
- नतिजा `CallToolResult` वस्तुमा फर्काइन्छ जसमा सर्भरको प्रतिक्रिया हुन्छ।

#### रस्टी

```rust
// "a": 3, "b": 2} तर्कहरूका साथ add tool कल गर्नुहोस्
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

### -5- क्लाइन्ट चलाउने

क्लाइन्ट चलाउन, टर्मिनलमा तलको कमाण्ड टाइप गर्नुहोस्:

#### टाइपस्क्रिप्ट

*package.json* को "scripts" सेक्षनमा तलको प्रविष्टि थप्नुहोस्:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### पाइथन

क्लाइन्टलाई यो कमाण्डबाट चलाउनुहोस्:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### जाभा

पहिले तपाईंको MCP सर्भर `http://localhost:8080` मा चलिरहेको छ भनी सुनिश्चित गर्नुहोस्। त्यसपछि क्लाइन्ट चलाउनुहोस्:

```bash
# तपाईंको परियोजना निर्माण गर्नुहोस्
./mvnw clean compile

# क्लाइन्ट चलाउनुहोस्
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

वैकल्पिक रूपमा, `03-GettingStarted\02-client\solution\java` फोल्डरमा दिइएको सम्पूर्ण क्लाइन्ट प्रोजेक्ट चलाउन सक्नुहुन्छ:

```bash
# समाधान डाइरेक्टरीमा जानुहोस्
cd 03-GettingStarted/02-client/solution/java

# JAR निर्माण गर्नुहोस् र चलाउनुहोस्
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### रस्टी

```bash
cargo fmt
cargo run
```

## कार्य

यस कार्यमा, तपाईंले सिकेका कुराहरू प्रयोग गरी आफ्नै क्लाइन्ट बनाउनुपर्नेछ।

यहाँ एउटा सर्भर छ जुन तपाईंले आफ्नो क्लाइन्टबाट कल गर्नु पर्नेछ, राखेर हेर्नुस् के थप सुविधाहरू थप्न सकिन्छ यो सर्भरमा र रमाइलो बनाउन सकिन्छ।

### टाइपस्क्रिप्ट

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एउटा MCP सर्भर सिर्जना गर्नुहोस्
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// एउटा थप उपकरण थप्नुहोस्
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// गतिशील अभिवादन स्रोत थप्नुहोस्
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

// stdin मा सन्देश प्राप्त गर्न र stdout मा सन्देश पठाउन सुरु गर्नुहोस्

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

### पाइथन

```python
# server.py
from mcp.server.fastmcp import FastMCP

# एक MCP सर्भर बनाउनुहोस्
mcp = FastMCP("Demo")


# एक थप उपकरण थप्नुहोस्
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एक गतिशील अभिवादन स्रोत थप्नुहोस्
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

यो प्रोजेक्ट हेर्नुस् कसरी [प्रॉम्प्ट र स्रोत थप्ने](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)।

साथ साथै यो लिंक जाँच्नुस् कसरी [प्रॉम्प्ट र स्रोतहरु कल गर्ने](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)।

### रस्टी

[अघिल्लो खण्डमा](../../../../03-GettingStarted/01-first-server) तपाइँले बारेमा सिक्नुभएको छ कसरी सरल MCP सर्भर रस्टीमा बनाउने। त्यसमाथि निर्माण जारी राख्न सक्नुहुन्छ वा थप MCP रस्टी सर्भर उदाहरणहरू हेर्न यो लिंक प्रयोग गर्नुहोस्: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## समाधान

**समाधान फोल्डर** पूर्ण, तत्पर-प्रयोग क्लाइन्ट कार्यान्वयनहरू समावेश गर्दछ जसले यस ट्युटोरियलमा सिकाइएका सबै अवधारणा देखाउँछ। हरेक समाधानमा क्लाइन्ट र सर्भर कोड अलग-अलग, स्वायत प्रोजेक्टहरूमा व्यवस्थित छन्।

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

हरेक भाषा-विशिष्ट समाधानले प्रदान गर्छ:

- **पूर्ण क्लाइन्ट कार्यान्वयन** ट्यूटोरियलका सबै सुविधाहरू सहित
- **काम गर्ने प्रोजेक्ट संरचना** उपयुक्त निर्भरताहरू र कन्फिगरेसन सहित
- **निर्माण र चलाउने स्क्रिप्टहरू** सजिलो सेटअप र कार्यान्वयनका लागि
- **विस्तृत README** भाषा-विशिष्ट निर्देशनहरू सहित
- **त्रुटि ह्यान्डलिङ** र परिणाम प्रशोधन उदाहरणहरू सहित

### 📖 समाधानहरू प्रयोग गर्दै

1. **आफ्नो रोजेको भाषा फोल्डरमा जानुहोस्**:

   ```bash
   cd solution/typescript/    # TypeScript का लागि
   cd solution/java/          # Java का लागि
   cd solution/python/        # Python का लागि
   cd solution/dotnet/        # .NET का लागि
   ```

2. **प्रत्येक फोल्डरमा README निर्देशनहरू अनुसरण गर्नुहोस्**:
   - निर्भरताहरू स्थापना गर्न
   - प्रोजेक्ट निर्माण गर्न
   - क्लाइन्ट चलाउन

3. **तपाईंले पाउनु हुने उदाहरण आउटपुट**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

पूर्ण कागजात र चरणबद्ध निर्देशनहरूका लागि हेर्नुहोस्: **[📖 समाधान कागजात](./solution/README.md)**

## 🎯 पूर्ण उदाहरणहरू

हामीले सबै सिकाइएको भाषाहरूका लागि पूर्ण, काम गर्ने क्लाइन्ट कार्यान्वयनहरू प्रदान गरेका छौं। यी उदाहरणहरूले माथि वर्णन गरिएका सबै कार्यक्षमताहरू देखाउँछन् र तपाईंको परियोजनाका लागि सन्दर्भ वा सुरुवाती बिन्दुका रूपमा प्रयोग गर्न सकिन्छ।

### उपलब्ध पूर्ण उदाहरणहरू

| भाषा | फाइल | विवरण |
|----------|------|-------------|
| **जाभा** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ट्रान्सपोर्ट प्रयोग गरी पूरै जाभा क्लाइन्ट जसमा विस्तृत त्रुटि ह्यान्डलिङ छ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ट्रान्सपोर्ट प्रयोग गरी C# क्लाइन्ट जसले स्वचालित सर्भर सुरुवात गर्छ |
| **टाइपस्क्रिप्ट** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | पूर्ण MCP प्रोटोकल समर्थन सहित टाइपस्क्रिप्ट क्लाइन्ट |
| **पाइथन** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | असिन्क/अवेट ढाँचामा पूर्ण पाइथन क्लाइन्ट |
| **रस्टी** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | असिन्क अपरेशनका लागि Tokio प्रयोग गरी रस्टी क्लाइन्ट |

प्रत्येक पूर्ण उदाहरणले समावेश गर्छ:

- ✅ **जडान स्थापना** र त्रुटि ह्यान्डलिङ
- ✅ **सर्भर खोज** (जहाँ लागू हुने, उपकरणहरू, स्रोतहरू, प्रॉम्प्टहरू)
- ✅ **क्यालकुलेटर अपरेसनहरू** (जोड्ने, घटाउने, गुना, भाग, सहायता)
- ✅ **परिणाम प्रशोधन** र स्वरूपित आउटपुट
- ✅ **व्यापक त्रुटि ह्यान्डलिङ**

- ✅ **सफा, दस्तावेज गरिएको कोड** चरण-द्वारा-चरण टिप्पणीहरू सहित

### पूर्ण उदाहरणहरूसँग सुरुवात गर्नुहोस्

1. माथिको तालिकाबाट **आफ्नो मनपरेको भाषा चयन गर्नुहोस्**
2. पूर्ण कार्यान्वयन बुझ्नका लागि **पूर्ण उदाहरण फाइल समीक्षा गर्नुहोस्**
3. [`complete_examples.md`](./complete_examples.md) मा रहेका निर्देशनहरू अनुसार **उदाहरण चलाउनुहोस्**
4. आफ्नो विशिष्ट प्रयोगका लागि उदाहरण **परिमार्जन र विस्तार गर्नुहोस्**

यी उदाहरणहरू चलाउन र अनुकूलन गर्नको लागि विस्तृत दस्तावेजीकरण हेर्नुहोस्: **[📖 पूर्ण उदाहरण दस्तावेज](./complete_examples.md)**

### 💡 समाधान vs. पूर्ण उदाहरणहरू

| **समाधान फोल्डर** | **पूर्ण उदाहरणहरू** |
|--------------------|--------------------- |
| निर्माण फाइलहरू सहितको पूर्ण परियोजना संरचना | एकल फाइल कार्यान्वयनहरू |
| निर्भरतालाई समावेश गरेर चलाउन तयार | केन्द्रित कोड उदाहरणहरू |
| उत्पादन-जस्तै सेटअप | शैक्षिक सन्दर्भ |
| भाषा-विशेष उपकरण | बहुभाषी तुलना |

दुवै तरिकाहरू मूल्यवान् छन् - पूर्ण परियोजनाहरूका लागि **समाधान फोल्डर** प्रयोग गर्नुहोस् र सिकाइ तथा सन्दर्भका लागि **पूर्ण उदाहरणहरू** प्रयोग गर्नुहोस्।

## मुख्य निष्कर्षहरू

यस अध्यायका लागि ग्राहकहरू सम्बन्धी मुख्य निष्कर्षहरू यसप्रकार छन्:

- सर्भरका फिचरहरू पत्ता लगाउन र चलाउन दुवैका लागि प्रयोग गर्न सकिन्छ।
- आफैं सुरुवात गर्दा (यस अध्यायमा जस्तै) सर्भर सुरू गर्न सक्छ तर ग्राहकहरूले चलिरहेको सर्भरसँग पनि जडान गर्न सक्छन्।
- सर्भर क्षमताहरूको परीक्षण गर्न राम्रो तरिका हो, जस्तै अघिल्लो अध्यायमा वर्णन गरिएको Inspector जस्ता विकल्पहरूका साथै।

## अतिरिक्त स्रोतहरू

- [MCP मा ग्राहकहरू निर्माण गर्दै](https://modelcontextprotocol.io/quickstart/client)

## नमूनाहरू

- [Java क्याल्कुलेटर](../samples/java/calculator/README.md)
- [.NET क्याल्कुलेटर](../../../../03-GettingStarted/samples/csharp)
- [JavaScript क्याल्कुलेटर](../samples/javascript/README.md)
- [TypeScript क्याल्कुलेटर](../samples/typescript/README.md)
- [Python क्याल्कुलेटर](../../../../03-GettingStarted/samples/python)
- [Rust क्याल्कुलेटर](../../../../03-GettingStarted/samples/rust)

## अब के आउनेछ

- अर्को: [LLM संग ग्राहक सिर्जना गर्दै](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->