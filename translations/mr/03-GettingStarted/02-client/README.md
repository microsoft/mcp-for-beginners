# क्लायंट तयार करणे

क्लायंट म्हणजे सानुकूल अनुप्रयोग किंवा स्क्रिप्ट जे थेट MCP सर्व्हरशी संवाद साधून संसाधने, साधने आणि प्रम्प्टची विनंती करतात. निरीक्षक साधन (inspector tool) वापरण्याच्या उलट, जे सर्व्हरशी संवाद साधण्यासाठी ग्राफिकल इंटरफेस प्रदान करते, स्वतःचा क्लायंट लिहिणे प्रोग्रॅमॅटिक आणि स्वयंचलित परस्परसंबंधांना परवानगी देते. हे विकसकांना त्यांच्या स्वतःच्या कार्यप्रवाहांमध्ये MCP क्षमता समाकलित करण्यास, कामे स्वयंचलित करण्यास आणि विशिष्ट गरजांसाठी सानुकूल उपाय तयार करण्यास सक्षम करते.

## आराखडा

या धड्यात Model Context Protocol (MCP) पर्यावरणातील क्लायंट्सची संकल्पना सादर केली आहे. तुम्हाला तुमचा स्वतःचा क्लायंट लिहिणे आणि तो MCP सर्व्हरशी कसा जोडायचा हे शिकवले जाईल.

## शिकण्याचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्हाला ते करता येईल:

- क्लायंट काय करू शकतो हे समजून घेणे.
- तुमचा स्वतःचा क्लायंट लिहिणे.
- क्लायंटला MCP सर्व्हरशी जोडणे आणि तपासणे जेणेकरून शेवटचा अपेक्षेनुसार कार्य करेल याची खात्री होईल.

## क्लायंट लिहिताना काय करायला हवे?

क्लायंट लिहिण्यासाठी, पुढील गोष्टी कराव्या लागतात:

- **योग्य लायब्ररी आयात करा**. तुम्ही अगोदर वापरलेल्या त्याच लायब्ररीचा वापर करणार आहात, फक्त वेगवेगळे कन्सट्रक्ट्स वापरायचे आहेत.
- **क्लायंट तयार करा**. यामध्ये क्लायंटची एक उदाहरण तयार करणे आणि निवडलेल्या ट्रान्सपोर्ट पद्धतीशी जोडणे समाविष्ट आहे.
- **कोणती संसाधने यादी करायची ते ठरवा**. तुमच्या MCP सर्व्हरमध्ये संसाधने, साधने आणि प्रम्प्ट असतात, तुम्हाला कोणती यादी करायची ते ठरवावे लागेल.
- **क्लायंटला होस्ट अनुप्रयोगाशी एकत्र करा**. जेव्हा तुम्हाला सर्व्हरच्या क्षमतांची कल्पना असेल तेव्हा तुम्हाला तुमच्या होस्ट अनुप्रयोगाशी एकत्रीकरण करणे आवश्यक आहे, जेणेकरून वापरकर्ता जेव्हा प्रम्प्ट किंवा इतर आदेश टाइप करेल तेव्हा संबंधित सर्व्हर फंक्शन कॉल होईल.

आता आपण वरवर पाहिले काय करायचे आहे, मग पुढील उदाहरण पाहूया.

### एक उदाहरण क्लायंट

या उदाहरण क्लायंटकडे एक नजर टाकूया:

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

// प्रॉम्प्ट्सची यादी करा
const prompts = await client.listPrompts();

// एक प्रॉम्प्ट मिळवा
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// संसाधनांची यादी करा
const resources = await client.listResources();

// एक संसाधन वाचा
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// एक साधन कॉल करा
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

वर दिलेल्या कोडमध्ये आपण:

- लायब्ररीज आयात केल्या
- क्लायंटची उदाहरण तयार केली आणि stdio वापरून ट्रान्सपोर्टसोबत जोडले.
- प्रम्प्ट, संसाधने आणि साधने यादी केली आणि सर्वांना कॉल केले.

एवढंच, एक क्लायंट जो MCP सर्व्हरशी बोलू शकतो.

पुढील व्यायाम विभागात आपण वेळ घेऊन प्रत्येक कोड स्निपेटचे विश्लेषण करू आणि काय चालले आहे ते समजावून घेऊ.

## व्यायाम: क्लायंट लिहिणे

वर सांगितल्याप्रमाणे, चला वेळ घेऊन कोड समजून घेऊ, आणि इच्छ असल्यास तुम्ही सोबत कोड करू शकता.

### -१- लायब्ररीज आयात करा

आपण आवश्यक लायब्ररी आयात करूया, आपल्याला क्लायंट आणि निवडलेल्या ट्रान्सपोर्ट प्रोटोकॉल stdio संदर्भ हवा आहे. stdio ही डिव्हाइसवर चालण्यासाठी असलेली प्रोटोकॉल आहे. SSE ही दुसरी ट्रान्सपोर्ट प्रोटोकॉल आहे जी पुढील प्रकरणांमध्ये दाखविली जाईल, पण सध्या stdio वापरूया.

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

Java मध्ये, तुम्ही मागील व्यायामातील MCP सर्व्हरशी कनेक्ट होणारा क्लायंट तयार कराल. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) येथून ज्या Java Spring Boot प्रोजेक्ट स्ट्रक्चरचा वापर केला आहे तसाच वापरून `src/main/java/com/microsoft/mcp/sample/client/` फोल्डरमध्ये `SDKClient` नावाचा नवीन Java क्लास तयार करा आणि खालील आयात जोडा:

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

तुमच्या `Cargo.toml` फाईलमध्ये खालील अवलंबित्वे (dependencies) जोडण्याची गरज आहे.

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

त्यानंतर, तुम्ही तुमच्या क्लायंट कोडमध्ये आवश्यक लायब्ररी आयात करू शकता.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

आता इंस्टांटिएशनकडे जाऊया.

### -२- क्लायंट आणि ट्रान्सपोर्ट इंस्टांटिएट करणे

आपल्याला ट्रान्सपोर्टची उदाहरण आणि क्लायंटची उदाहरण तयार करावी लागेल:

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

वरच्या कोडमध्ये आपण:

- stdio ट्रान्सपोर्टची उदाहरण तयार केली. लक्षात ठेवा, ते सर्व्हर कसे शोधायचे व सुरू करायचे यासाठी कमांड आणि args निर्दिष्ट करते, कारण क्लायंट बनवताना ते आवश्यक आहे.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- क्लायंटचे उदाहरण तयार केले नाव आणि आवृत्ती देऊन.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- क्लायंटला निवडलेल्या ट्रान्सपोर्टशी जोडले.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio कनेक्शनसाठी सर्व्हर पॅरामीटर्स तयार करा
server_params = StdioServerParameters(
    command="mcp",  # चालवण्यायोग्य फाईल
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

वरच्या कोडमध्ये आपण:

- आवश्यक लायब्ररी आयात केल्या
- सर्व्हर पॅरामीटर्स ऑब्जेक्ट इंस्टांटिएट केला कारण आम्ही सर्व्हर चालवण्यासाठी आणि क्लायंटला कनेक्ट करण्यासाठी वापरू.
- `run` नावाची मेथड तयार केली ज्यात `stdio_client` कॉल केला, ज्यामुळे क्लायंट सेशन सुरु होते.
- एक प्रवेश बिंदू (entry point) तयार केला जिथे `run` मेथड `asyncio.run` ला दिली.

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

वरच्या कोडमध्ये आपण:

- आवश्यक लायब्ररी आयात केल्या.
- stdio ट्रान्सपोर्ट तयार केला आणि `mcpClient` नावाचा क्लायंट बनविला. नंतरच्या भागात हे MCP सर्व्हरवरील फिचर्स कॉल करण्यासाठी वापरले जाईल.

लक्षात ठेवा, "Arguments" मध्ये तुम्ही *.csproj* किंवा executable फाइलच्या पथांकडे निर्देश करू शकता.

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
        
        // तुमची क्लायंट लॉजिक येथे जाते
    }
}
```

वरच्या कोडमध्ये आपण:

- मुख्य मेथड तयार केली जी `http://localhost:8080` कडे SSE ट्रान्सपोर्ट सेटअप करते, जेथे आमचा MCP सर्व्हर चालू असेल.
- क्लायंट वर्ग तयार केला जो ट्रान्सपोर्टला कन्स्ट्रक्टरमध्ये घेतो.
- `run` मेथडमध्ये, ट्रान्सपोर्ट वापरून सिंक्रोनस MCP क्लायंट तयार केला आणि कनेक्शन सुरू केले.
- SSE (Server-Sent Events) ट्रान्सपोर्ट वापरला जो Java Spring Boot MCP सर्व्हरसाठी HTTP आधारित संवादासाठी योग्य आहे.

#### Rust

लक्षात ठेवा हा Rust क्लायंट सर्व्हर "calculator-server" नावाच्या एका सिबलिंग प्रोजेक्टवर आधारित आहे, जो त्याच फोल्डरमध्ये आहे. खालील कोड सर्व्हर सुरु करेल आणि जोडेल.

```rust
async fn main() -> Result<(), RmcpError> {
    // सर्व्हर हा एक सिबलिंग प्रोजेक्ट आहे ज्याचे नाव "calculator-server" असून तो त्याच निर्देशिकेत आहे असे गृहीत धरा
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

    // TODO: प्रारंभ करा

    // TODO: टूल्सची यादी करा

    // TODO: arguments = {"a": 3, "b": 2} वापरून add tool कॉल करा

    client.cancel().await?;
    Ok(())
}
```

### -३- सर्व्हर फिचर्सची यादी करणे

आता, आमच्याकडे एक क्लायंट आहे जो प्रोग्राम चालू करताना जोडू शकतो. पण तो त्याचे फिचर्स अजून यादी करत नाही, ते पुढे करूया:

#### TypeScript

```typescript
// प्रॉम्प्ट्सची यादी
const prompts = await client.listPrompts();

// संसाधनांची यादी
const resources = await client.listResources();

// साधनांची यादी
const tools = await client.listTools();
```

#### Python

```python
# उपलब्ध संसाधने यादी करा
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# उपलब्ध उपकरणे यादी करा
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

येथे आपण उपलब्ध संसाधने, `list_resources()` आणि साधने, `list_tools` यादी करतो आणि त्या छापतो.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

वर दिलेले उदाहरण सर्व्हरवरील साधने कशी यादी करायची हे दाखवते. प्रत्येक साधनाचे नाव नंतर छापले जाते.

#### Java

```java
// साधने यादी करा आणि दाखवा
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// कनेक्शन सत्यापित करण्यासाठी आपण सर्व्हरला पिंग देखील करू शकता
client.ping();
```

वरच्या कोडमध्ये आपण:

- MCP सर्व्हरमधील सर्व उपलब्ध साधने मिळविण्यासाठी `listTools()` कॉल केला.
- सर्व्हरशी कनेक्शन कार्यरत आहे याची खात्री करण्यासाठी `ping()` वापरली.
- `ListToolsResult` मध्ये सर्व साधनांची नावे, वर्णने आणि इनपुट स्कीमाचा माहिती आहे.

छान, आता आपण सर्व फिचर्स समाविष्ट केले. प्रश्न असा आहे की त्यांचा वापर कधी करायचा? हा क्लायंट खूप सोपा आहे, म्हणजे आपल्याला हवे तेव्हा फिचर्स स्पष्टपणे कॉल कराव्या लागतील. पुढील प्रकरणात, आपण अधिक प्रगत क्लायंट तयार करू ज्याला स्वतःचा मोठा भाषा मॉडेल, LLM, असेल. सध्या तरी, पाहूया सर्व्हरवरील फिचर्स कसे कॉल करावेत:

#### Rust

मुख्य फंक्शनमध्ये, क्लायंट प्रारंभ केल्यानंतर, आपण सर्व्हर प्रारंभ करू शकतो आणि काही फिचर्स यादी करू शकतो.

```rust
// प्रारंभ करा
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// साधने यादी करा
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -४- फिचर्स कॉल करणे

फिचर्स कॉल करण्यासाठी आपण योग्य आर्ग्युमेंट्स आणि काही वेळेस कॉल करायच्या वस्तूचे नाव निर्दिष्ट करणे आवश्यक आहे.

#### TypeScript

```typescript

// स्त्रोत वाचा
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// उपकरण कॉल करा
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// प्रॉम्प्ट कॉल करा
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

वरच्या कोडमध्ये आपण:

- संसाधन वाचले, `readResource()` कॉल करून `uri` दिला. तरी सर्व्हरवर खालीलप्रमाणे दिसते:

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

    आमचा `uri` मूल्य `file://example.txt` सर्व्हरवरील `file://{name}` शी जुळते. `example.txt` `name` म्हणून मॅप होईल.

- साधन कॉल केले, त्याचे `name` आणि `arguments` निर्दिष्ट करून असे कॉल केले:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- प्रम्प्ट घेतला, `getPrompt()` कॉल करून `name` आणि `arguments` दिले. सर्व्हर कोड असा दिसतो:

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

    आणि परिणामी क्लायंट कोड तसा दिसतो जो सर्व्हरवर घोषित केलेल्या गोष्टीशी जुळतो:

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
# एक स्रोत वाचा
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# एक साधन कॉल करा
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

वरच्या कोडमध्ये आपण:

- `greeting` नावाचे संसाधन `read_resource` वापरून कॉल केले.
- `add` नावाचे साधन `call_tool` वापरून वापरले.

#### .NET

1. साधन कॉल करण्यासाठी हा कोड जोडा:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. परिणाम छापण्यासाठी कोड:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// विविध कॅल्क्युलेटर साधने कॉल करा
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

वरच्या कोडमध्ये आपण:

- `callTool()` पद्धत वापरून अनेक कॅल्क्युलेटर साधने कॉल केली.
- प्रत्येक साधन कॉलमध्ये साधनाचे नाव आणि त्या साधनासाठी आवश्यक असलेले `Map` स्वरूपातील आर्ग्युमेंट्स दिले.
- सर्व्हर साधनांना विशिष्ट पॅरामीटर नावे अपेक्षित असतात (जसे "a", "b" गणितीय ऑपरेशन्ससाठी).
- परिणाम `CallToolResult` वस्तूंमध्ये मिळतात ज्यात सर्व्हर कडून प्रतिसाद असतो.

#### Rust

```rust
// add टूलला आर्ग्युमेंट्ससह कॉल करा = {"a": 3, "b": 2}
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

### -५- क्लायंट चालवा

क्लायंट चालविण्यासाठी, टर्मिनलमध्ये खालील आज्ञा द्या:

#### TypeScript

*package.json* मध्ये "scripts" विभागात खालील एंट्री जोडा:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

क्लायंट खालीलप्रमाणे कॉल करा:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

आधी सुनिश्चित करा की तुमचा MCP सर्व्हर `http://localhost:8080` वर चालू आहे. नंतर क्लायंट चालवा:

```bash
# आपला प्रकल्प तयार करा
./mvnw clean compile

# क्लायंट चालवा
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

किंवा, तुम्ही या सोल्युशन फोल्डरमधील पूर्ण क्लायंट प्रोजेक्ट चालवू शकता `03-GettingStarted\02-client\solution\java`:

```bash
# सोल्यूशन निर्देशिकेत जा
cd 03-GettingStarted/02-client/solution/java

# JAR तयार करा आणि चालवा
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## असाइनमेंट

या असाइनमेंटमध्ये, तुम्ही जे शिकलात त्याचा वापर करून स्वतःचा क्लायंट तयार कराल.

येथे तुम्हाला वापरता येईल असा एक सर्व्हर आहे ज्याला तुम्हाला क्लायंट कोडद्वारे कॉल करायचे आहे, पाहा तुम्ही त्यात आणखी वैशिष्ट्ये समाविष्ट करू शकता का, ज्याने तो अधिक रोचक बनेल.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP सर्व्हर तयार करा
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// एक अतिरिक्त साधन जोडा
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक डायनॅमिक अभिवादन संसाधन जोडा
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

// stdin वर संदेश प्राप्त करणे सुरू करा आणि stdout वर संदेश पाठवा

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

# एक MCP सर्व्हर तयार करा
mcp = FastMCP("Demo")


# एक बेरीज साधन जोडा
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एक गतिशील अभिवादन स्त्रोत जोडा
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

हा प्रोजेक्ट पाहा ज्यात तुम्हाला कसे [prompts आणि resources जोडायचे](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) ते शिकता येईल.

तसेच, ह्या लिंकवरून [prompts आणि resources कसे invoke करायचे](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) ते पहा.

### Rust

[मागील विभागात](../../../../03-GettingStarted/01-first-server) तुम्ही Rust वापरून एक सोपा MCP सर्व्हर तयार केला. तुम्ही त्या वर पुढे तयार करू शकता अथवा या लिंकवरून आणखी Rust आधारित MCP सर्व्हरचे उदाहरणे पाहू शकता: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## सोल्युशन

**सोल्युशन फोल्डर** मध्ये पूर्ण, तयार चालवायला शक्य क्लायंट अंमलबजावणी आहेत ज्या या ट्यूटोरियलमध्ये दिलेल्या संकल्पनांना प्रदर्शन करतात. प्रत्येक सोल्युशनमध्ये स्वतंत्र, स्वतंत्र प्रोजेक्ट्समध्ये क्लायंट आणि सर्व्हर कोड समाविष्ट आहे.

### 📁 सोल्युशन संरचना

सोल्युशन डायरेक्टरी प्रोग्रामिंग भाषेनुसार व्यवस्थित करण्यात आली आहे:

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

### 🚀 प्रत्येक सोल्युशनमध्ये काय आहे

प्रत्येक भाषा-विशिष्ट सोल्युशनमध्ये आहे:

- **संपूर्ण क्लायंट अंमलबजावणी** ट्यूटोरियलमधील सर्व वैशिष्ट्यांसह
- **काम करणारी प्रोजेक्ट संरचना** योग्य अवलंबित्वांसह आणि कॉन्फिगरेशनसह
- **बिल्ड आणि रन स्क्रिप्ट्स** सोपी सेटअप आणि अंमलबजावणीसाठी
- **सविस्तर README** भाषा-विशिष्ट सूचना सहित
- **त्रुटी हाताळणी** आणि परिणाम प्रक्रिया उदाहरणे

### 📖 सोल्युशन्स वापरणे

1. **तुमचे प्राधान्य असलेले भाषा फोल्डर निवडा**:

   ```bash
   cd solution/typescript/    # टाइपस्क्रिप्टसाठी
   cd solution/java/          # जावासाठी
   cd solution/python/        # पाइथनसाठी
   cd solution/dotnet/        # .नेटसाठी
   ```

2. **प्रत्येक फोल्डरमधील README मध्ये दिलेल्या सूचना अनुसरा**:
   - अवलंबित्वे स्थापित करणे
   - प्रोजेक्ट बिल्ड करणे
   - क्लायंट चालविणे

3. **तुम्हाला दिसणारा संभाव्य आउटपुट**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

संपूर्ण दस्तऐवजीकरण आणि टप्प्याटप्प्याने सूचना करीता पहा: **[📖 सोल्युशन दस्तऐवजीकरण](./solution/README.md)**

## 🎯 संपूर्ण उदाहरणे

आम्ही सर्व प्रोग्रामिंग भाषांसाठी पूर्ण, काम करणाऱ्या क्लायंट अंमलबजावण्या दिल्या आहेत ज्या या ट्यूटोरियलमध्ये वर्णन केलेल्या संपूर्ण कार्यप्रणाली दाखवतात. या उदाहरणांचा संदर्भासाठी किंवा स्वतःच्या प्रोजेक्टसाठी सुरुवातीस म्हणून वापर करू शकता.

### उपलब्ध संपूर्ण उदाहरणे

| भाषा | फाइल | वर्णन |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ट्रान्सपोर्टसह संपूर्ण Java क्लायंट, सर्वसमावेशक त्रुटी हाताळणीसह |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | स्ट्डिओ ट्रान्सपोर्टसह संपूर्ण C# क्लायंट, स्वयंचलित सर्व्हर सुरु करण्यासह |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | संपूर्ण TypeScript क्लायंट, पूर्ण MCP प्रोटोकॉल समर्थनासह |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await पद्धती वापरून संपूर्ण Python क्लायंट |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio वापरून async ऑपरेशन्ससाठी संपूर्ण Rust क्लायंट |

प्रत्येक संपूर्ण उदाहरणामध्ये आहे:

- ✅ **कनेक्शन स्थापना** आणि त्रुटी हाताळणी
- ✅ **सर्व्हर शोध** (साधने, संसाधने, प्रम्प्ट जिथे लागू)
- ✅ **कॅल्क्युलेटर ऑपरेशन्स** (जोडणे, वजाबाकी, गुणाकार, भागाकार, मदत)
- ✅ **परिणाम प्रक्रिया** आणि स्वरूपित आउटपुट
- ✅ **संपूर्ण त्रुटी हाताळणी**

- ✅ **साफ, कागदबद्ध केलेला कोड** टप्प्याटप्प्याने कमेंटसह

### पूर्ण उदाहरणांसह सुरुवात करणे

1. वरील तक्त्यातून तुमची आवडती भाषा **निवडा**
2. संपूर्ण अंमलबजावणी समजण्यासाठी **पूर्ण उदाहरण फाइल पहा**
3. [`complete_examples.md`](./complete_examples.md) मधील सूचनांनुसार **उदाहरण चालवा**
4. तुमच्या विशिष्ट वापरासाठी उदाहरण **सांधणे आणि विस्तारित करा**

या उदाहरणांचे चालवणे आणि सानुकूल करण्यासाठी सविस्तर दस्तऐवजीकरण पहा: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 सोल्युशन विरुद्ध पूर्ण उदाहरणे

| **सोल्युशन फोल्डर** | **पूर्ण उदाहरणे** |
|--------------------|--------------------- |
| बिल्ड फाइल्ससह पूर्ण प्रोजेक्ट रचना | सिंगल-फाइल अंमलबजावणी |
| अवलंबनांसह तयार चालवण्याजोगे | लक्ष केंद्रित केलेले कोड उदाहरणे |
| उत्पादनासारखी सेटअप | शैक्षणिक संदर्भ |
| भाषा-विशिष्ट टूलिंग | क्रॉस-भाषा तुलना |

दोन्ही दृष्टिकोन महत्त्वाचे आहेत - पूर्ण प्रोजेक्टसाठी **सोल्युशन फोल्डर** आणि शिकण्यासाठी व संदर्भासाठी **पूर्ण उदाहरणे** वापरा.

## मुख्य मुद्दे

या प्रकरणासाठी ग्राहकांविषयी मुख्य मुद्दे पुढीलप्रमाणे आहेत:

- सर्व्हरवरील वैशिष्ट्ये शोधण्यासाठी आणि कॉल करण्यासाठी वापरले जाऊ शकते.
- स्वतः सुरू होताना सेर्व्हर सुरू करू शकते (जसे या प्रकरणात) पण ग्राहक चालू सेर्व्हरशी देखील कनेक्ट होऊ शकतात.
- मागील प्रकरणात वर्णन केल्याप्रमाणे इन्स्पेक्टरसारख्या पर्यायांच्या शेजारी सेर्व्हर क्षमता तपासण्याचा उत्कृष्ट मार्ग आहे.

## अतिरिक्त संसाधने

- [MCP मध्ये ग्राहक तयार करणे](https://modelcontextprotocol.io/quickstart/client)

## नमुने

- [Java कॅल्क्युलेटर](../samples/java/calculator/README.md)
- [.NET कॅल्क्युलेटर](../../../../03-GettingStarted/samples/csharp)
- [JavaScript कॅल्क्युलेटर](../samples/javascript/README.md)
- [TypeScript कॅल्क्युलेटर](../samples/typescript/README.md)
- [Python कॅल्क्युलेटर](../../../../03-GettingStarted/samples/python)
- [Rust कॅल्क्युलेटर](../../../../03-GettingStarted/samples/rust)

## पुढे काय

- पुढे: [LLM सह ग्राहक तयार करणे](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->