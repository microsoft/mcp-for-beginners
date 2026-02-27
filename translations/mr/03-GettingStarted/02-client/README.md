# क्लायंट तयार करणे

क्लायंट हे सानुकूल अनुप्रयोग किंवा स्क्रिप्ट असतात जे थेट MCP सर्व्हरशी संवाद साधतात संसाधने, साधने, आणि प्रॉम्प्ट मागण्यासाठी. इन्स्पेक्टर टूल वापरण्यापेक्षा, जे सर्व्हरशी संवाद साधण्यासाठी ग्राफिकल इंटरफेस देते, स्वतःचा क्लायंट लिहिणे प्रोग्रामॅटिक व स्वयंचलित संवाद सक्षम करते. यामुळे विकासकांना त्यांच्या स्वत:च्या कार्यप्रवाहात MCP क्षमतांचा समावेश करण्याची, कार्ये स्वयंचलित करण्याची, आणि विशिष्ट गरजेनुसार सानुकूल सोल्यूशन्स निर्माण करण्याची मुभा मिळते.

## आढावा

हा धडा Model Context Protocol (MCP) वातावरणातील क्लायंट संकल्पनेची ओळख करून देतो. आपण आपल्या स्वतःचा क्लायंट कसा लिहायचा आणि तो MCP सर्व्हरशी कसा कनेक्ट होतो ते शिकाल.

## शिकण्याचे उद्दिष्ट

या धड्याच्या शेवटी आपण सक्षम असाल:

- क्लायंट काय करू शकतो हे समजून घेणे.
- आपला स्वतःचा क्लायंट लिहिणे.
- MCP सर्व्हरसह क्लायंट कनेक्ट करणे आणि तपासणे की तो अपेक्षेनुसार कार्य करतो की नाही.

## क्लायंट लिहिताना काय करावे लागते?

क्लायंट लिहिण्यासाठी, आपल्याला पुढील गोष्टी कराव्या लागतील:

- **योग्य लायब्ररी आयात करा**. आपण आधी सारख्या लायब्ररीचा वापर करणार आहोत, फक्त वेगळ्या निर्माणधारकांसह.
- **क्लायंट तयार करा**. यात क्लायंटची उदाहरण तयार करणे आणि निवडलेल्या ट्रान्सपरट पद्धतीशी कनेक्ट करणे समाविष्ट आहे.
- **कोणती संसाधने सूचीबद्ध करायची ते ठरवा**. आपल्या MCP सर्व्हरमध्ये संसाधने, साधने आणि प्रॉम्प्ट असतात, त्यापैकी कोणती सूचीबद्ध करायची ते ठरवा.
- **क्लायंट होस्ट अनुप्रयोगात एकत्र करा**. एकदा सर्व्हरच्या क्षमतांची माहिती झाल्यावर, हे आपल्या होस्ट अनुप्रयोगात एकत्र करा जेणेकरून वापरकर्ता प्रॉम्प्ट किंवा इतर आदेश टाइप केल्यावर त्यानुसार सर्व्हरची वैशिष्ट्ये सक्रिय होईल.

आता आपण उच्च स्तरावर काय करणार ते समजल्यामुळे, पुढे एक उदाहरण पाहूया.

### एक उदाहरण क्लायंट

या उदाहरण क्लायंटकडे पाहूया:

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

// प्रॉम्प्टची यादी करा
const prompts = await client.listPrompts();

// एक प्रॉम्प्ट मिळवा
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// साधनांची यादी करा
const resources = await client.listResources();

// एक साधन वाचा
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

वरील कोडमध्ये आपण:

- लायब्ररीज आयात केल्या
- क्लायंटचे एक उदाहरण तयार केले आणि stdio द्वारे ट्रान्सपरटसाठी कनेक्ट केले.
- प्रॉम्प्ट्स, संसाधने आणि साधने सूचीबद्ध केली आणि सर्वांनाच कॉल केले.

तर झाले, एक क्लायंट जो MCP सर्व्हरशी बोलू शकतो.

पुढील व्यायाम विभागात प्रत्येक कोड भागाचे भाष्य करून त्याचा अर्थ समजून घेऊया.

## व्यायाम: क्लायंट लिहिणे

पुढे सांगितल्याप्रमाणे, चला कोडचे स्पष्टीकरण करत जाऊ आणि शक्य असल्यास तुम्हीही सोबत कोड करा.

### -1- लायब्ररी आयात करणे

आता आवश्यक लायब्ररी आयात करूया, आपल्याला क्लायंट आणि stdio ह्या ट्रान्सपरट प्रोटोकॉलसाठी संदर्भ हवा आहे. stdio ही लोकल मशीनवर चालणाऱ्या गोष्टींसाठी प्रोटोकॉल आहे. SSE हा आणखी एक ट्रान्सपरट प्रोटोकॉल आहे जो आपण आगामी धड्यांमध्ये पाहू. आतासाठी stdio सोबत पुढे जाऊया.

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

Java साठी, मागील व्यायामातील MCP सर्व्हरशी कनेक्ट होणारा क्लायंट तयार करा. समान Java Spring Boot प्रोजेक्ट स्ट्रक्चर वापरून [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) मधील `src/main/java/com/microsoft/mcp/sample/client/` फोल्डरमध्ये `SDKClient` नावाचा नवीन क्लास तयार करा आणि पुढील आयात जोडा:

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

आपल्या `Cargo.toml` फाइलमध्ये पुढील आवश्यकतांसह जोडावे लागेल.

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

यानंतर, आपल्या क्लायंट कोडमध्ये आवश्यक लायब्ररी आयात करा.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

आता उदाहरण तयार करुया.

### -2- क्लायंट आणि ट्रान्सपरटची उदाहरणे तयार करणे

आपल्याला ट्रान्सपरटचे आणि क्लायंटचे उदाहरण तयार करावे लागेल:

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

वरील कोडमध्ये आपण:

- stdio ट्रान्सपरट उदाहरण तयार केले. हे कसे शोधायचे आणि सर्व्हर कसा सुरू करायचा हे `command` आणि `args` द्वारा सांगितले आहे, जे क्लायंट तयार करताना आवश्यक आहे.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- नाव व आवृत्ती देऊन क्लायंट तयार केला.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- निवडलेल्या ट्रान्सपरटशी क्लायंट कनेक्ट केला.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio कनेक्शनसाठी सर्व्हर पॅरामीटर्स तयार करा
server_params = StdioServerParameters(
    command="mcp",  # एक्झिक्युटेबल
    args=["run", "server.py"],  # ऐच्छिक कमांड लाइन आर्ग्युमेंट्स
    env=None,  # ऐच्छिक पर्यावरण चल
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

- आवश्यक लायब्ररी आयात केले.
- सर्व्हर पॅरामीटर्स ऑब्जेक्ट तयार केले जो सर्व्हर चालवण्यासाठी वापरले जाईल आणि त्याद्वारे क्लायंट कनेक्ट होईल.
- `run` नावाची मेथड तयार केली जी `stdio_client` कॉल करेल, ज्यामुळे क्लायंट सेशन सुरू होईल.
- `asyncio.run` ला `run` पद्धत दिली.

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

वरील कोडमध्ये आपण:

- आवश्यक लायब्ररी आयात केला.
- stdio ट्रान्सपरट तयार केला आणि `mcpClient` नावाचा क्लायंट तयार केला. त्याचा वापर MCP सर्व्हरवर वैशिष्ट्ये सूचीबद्ध करण्यासाठी आणि कॉल करण्यासाठी होईल.

टीप: "Arguments" मध्ये आपण *.csproj* किंवा executable कडे निर्देश करू शकता.

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
        
        // तुमचा क्लायंट लॉजिक इथे जातो
    }
}
```

वरील कोडमध्ये आपण:

- मुख्य मेथड तयार केली ज्यात SSE ट्रान्सपरट सेट केली आहे जी `http://localhost:8080` कडे निर्देशित करते, जिथे MCP सर्व्हर चालेल.
- क्लायंट क्लास तयार केला जो कन्स्ट्रक्टरमध्ये ट्रान्सपरट घेते.
- `run` मेथडमध्ये ट्रान्सपरटसह सिंक्रोनस MCP क्लायंट तयार केला आणि कनेक्शन प्रारंभ केले.
- SSE ट्रान्सपरट वापरला जो Java Spring Boot MCP सर्व्हरशी HTTP आधारित संवादासाठी योग्य आहे.

#### Rust

हे Rust क्लायंट असं अपेक्षित करतो की सर्व्हर एक "calculator-server" नावाचं सिबलिंग प्रोजेक्ट आहे त्याच डिरेक्टरीमध्ये. खालील कोड सर्व्हर सुरू करेल आणि त्याला कनेक्ट होईल.

```rust
async fn main() -> Result<(), RmcpError> {
    // सर्व्हर हा त्याच निर्देशिकेत "calculator-server" नावाचा भाऊभाऊ प्रकल्प आहे असे गृहित धरा
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

    // करणायचे: प्रारंभ करा

    // करणायचे: साधने यादी करा

    // करणायचे: add tool शी कॉल करा, आर्ग्युमेंट्स = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- सर्व्हरचे वैशिष्ट्ये सूचीबद्ध करणे

आता आमच्याकडे क्लायंट आहे जो कनेक्ट होतो परंतु तो त्याची वैशिष्ट्ये सूचीबद्ध करत नाही, ते आता करूया:

#### TypeScript

```typescript
// सूचनांची यादी करा
const prompts = await client.listPrompts();

// संसाधनांची यादी करा
const resources = await client.listResources();

// साधनांची यादी करा
const tools = await client.listTools();
```

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
```

इथे आपण उपलब्ध संसाधने `list_resources()` आणि साधने `list_tools()` सूचीबद्ध करतो आणि त्यांना प्रिंट करतो.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

वरील उदाहरणात आपण सर्व्हरवरील साधने सूचीबद्ध केली आणि प्रत्येक साधनाचे नाव मुद्रित केले.

#### Java

```java
// उपकरणांची यादी करा आणि दाखवा
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// कनेक्शन तपासण्यासाठी तुम्ही सर्व्हरवर पिंग देखील करू शकता
client.ping();
```

वरील कोडमध्ये आपण:

- `listTools()` कॉल केले जे MCP सर्व्हरकडून सर्व उपलब्ध साधने मिळवते.
- `ping()` वापरून सर्व्हरशी कनेक्शन काम करत आहे का तपासले.
- `ListToolsResult` मध्ये सर्व साधनांची नावे, वर्णने, आणि इनपुट स्कीम्स असतात.

चांगलं, आता आपण सर्व वैशिष्ट्ये समायोजित केली. आता प्रश्न आहे, आपण ते कधी वापरू? हा क्लायंट साधा आहे, म्हणजे आपल्याला जेव्हा हवे तेव्हा वैशिष्ट्ये स्पष्टपणे कॉल करावी लागतील. पुढील धड्यात, आपण अधिक प्रगत क्लायंट तयार करू जो स्वतःचा मोठ्या भाषेचा मॉडेल (LLM) वापरेल. आतासाठी, चला पाहूया सर्व्हरवरील वैशिष्ट्ये कशी कॉल करतात:

#### Rust

मुख्य फंक्शनमध्ये, क्लायंट इनिशियलाइज केल्यावर आपण सर्व्हरही इनिशियलाइज करू शकतो आणि त्याच्या काही वैशिष्ट्यांचे सूची तयार करू शकतो.

```rust
// प्रारंभ करा
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// साधने यादी करा
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- वैशिष्ट्ये कॉल करणे

वैशिष्ट्ये कॉल करण्यासाठी योग्य आर्ग्युमेंट्स आणि काही प्रकरणात आपण कॉल करत असलेल्या वस्तूचे नाव अचूक द्यावे लागते.

#### TypeScript

```typescript

// एक संसाधन वाचा
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// साधनाला कॉल करा
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// प्रांप्ट कॉल करा
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

वरील कोडमध्ये आपण:

- संसाधन वाचले, `readResource()` कॉल करून `uri` निर्दिष्ट केला. सर्व्हरवर हे कसे दिसते:

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

    आपला `uri` मूल्य `file://example.txt` सर्व्हरवरील `file://{name}` शी जुळते. `example.txt` `name` शी नकाशा केले जाईल.

- साधन कॉल केले, त्यासाठी `name` आणि `arguments` निर्दिष्ट करतो:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- प्रॉम्प्ट मिळविला, `getPrompt()` कॉल करून `name` आणि `arguments` दिले. सर्व्हर कोड:

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

    आणि त्यामुळे तुमचा क्लायंट कोड असा दिसेल:

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
# एक स्त्रोत वाचा
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# एक साधन कॉल करा
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

वरील कोडमध्ये आपण:

- `greeting` नावाचा संसाधन `read_resource` वापरून कॉल केला.
- `add` नावाचे साधन `call_tool` वापरून कॉल केले.

#### .NET

1. साधन कॉल करण्यासाठी कोड:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. निकाल मुद्रित करण्यासाठी कोड:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// विविध गणक साधने कॉल करा
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

वरील कोडमध्ये आपण:

- `callTool()` पद्धत वापरून अनेक कॅल्क्युलेटर साधने कॉल केली, ज्यात `CallToolRequest` वस्तू दिल्या.
- प्रत्येक साधन कॉलमध्ये साधनाचे नाव आणि आवश्यक आर्ग्युमेंट्स असलेला `Map` दिला.
- सर्व्हर साधनांसाठी विशिष्ट पॅरामिटर नावे अपेक्षित आहेत (जसे "a", "b" गणितीय ऑपरेशन्ससाठी).
- निकाल `CallToolResult` ऑब्जेक्ट्समध्ये परत मिळतो ज्यात सर्व्हरची प्रतिक्रिया असते.

#### Rust

```rust
// add टूल कॉल करा युक्तिवादांसह = {"a": 3, "b": 2}
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

### -5- क्लायंट चालवा

क्लायंट चालवण्यासाठी टर्मिनलमध्ये खालील आदेश टाका:

#### TypeScript

*package.json* फाइलमधील "scripts" विभागात पुढील एंट्री जोडा:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

क्लायंट खालील आदेशाने कॉल करा:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

प्रथम, MCP सर्व्हर `http://localhost:8080` वर चालू आहे याची खात्री करा. नंतर क्लायंट चालवा:

```bash
# आपला प्रकल्प तयार करा
./mvnw clean compile

# क्लायंट चालवा
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

पर्यायी, आपण संपूर्ण क्लायंट प्रोजेक्ट `03-GettingStarted\02-client\solution\java` फोल्डरमध्ये उपलब्ध असलेला चालवू शकता:

```bash
# सोल्यूशन निर्देशिकेकडे जा
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

या असाइनमेंटमध्ये, आपण शिकलेले वापरून स्वतःचा क्लायंट तयार कराल.

इथे आपल्याला वापरण्यासाठी एक सर्व्हर आहे ज्याला आपला क्लायंट कोड कॉल करतो, पाहा आपण त्यात अधिक वैशिष्ट्ये कशी जोडू शकता ज्यामुळे तो अधिक मनोरंजक बनेल.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एक MCP सर्व्हर तयार करा
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// एक भर टूल जोडा
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक गतिशील अभिवादन संसाधन जोडा
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

// stdin वर संदेश प्राप्त करणे आणि stdout वर संदेश पाठविणे सुरू करा

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


# एक गतिशील अभिवादन संसाधन जोडा
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

या प्रोजेक्टमध्ये पहा की [प्रॉम्प्ट्स आणि संसाधने कशी जोडावीत](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

तसेच ह्या दुव्यावर पहा [प्रॉम्प्ट्स आणि संसाधने कशी Invoke करावी](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

[मागील विभागात](../../../../03-GettingStarted/01-first-server) आपण Rust सह साधा MCP सर्व्हर कसा तयार करायचा ते शिकलात. आपण त्यावर पुढे काम करू शकता किंवा ह्या दुव्यावर अधिक Rust-आधारित MCP सर्व्हर उदाहरणे पाहू शकता: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## उपाय

**उपाय फोल्डर** मध्ये संपूर्ण, तयार-चालवायला क्लायंट इम्प्लिमेंटेशन्स आहेत जे या ट्यूटोरियलमधील सर्व संकल्पना दाखवतात. प्रत्येक उपायात क्लायंट आणि सर्व्हर कोड स्वतंत्र, एकत्र न झालेल्या प्रोजेक्ट्समध्ये असतो.

### 📁 उपाय रचना

उपाय डायरेक्टरी प्रोग्रामिंग भाषेप्रमाणे व्यवस्थीत आहे:

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

### 🚀 प्रत्येक उपायात काय समाविष्ट आहे

प्रत्येक भाषा-विशिष्ट उपाय देतो:

- **ट्यूटोरियलमधील सर्व वैशिष्ट्यांसह संपूर्ण क्लायंट इम्प्लिमेंटेशन**
- **योग्य अवलंबन आणि कॉन्फिगरेशनसह कार्यरत प्रोजेक्ट स्ट्रक्चर**
- **सुविधाजनक सेटअप व अंमलबजावणीसाठी बिल्ड व रन स्क्रिप्ट्स**
- **भाषा-विशिष्ट सूचनांसहित सविस्तर README**
- **त्रुटी हाताळणी आणि निकाल प्रक्रिया यांचे उदाहरण**

### 📖 उपाय वापरणे

1. **आपल्या पसंतीच्या भाषा फोल्डरमध्ये जा**:

   ```bash
   cd solution/typescript/    # Typescript साठी
   cd solution/java/          # Java साठी
   cd solution/python/        # Python साठी
   cd solution/dotnet/        # .NET साठी
   ```

2. **प्रत्येक फोल्डरमधील README मधील सूचना पाळा:**
   - अवलंबने इन्स्टॉल करणे
   - प्रोजेक्ट बांधणी
   - क्लायंट चालवणे

3. **आपल्याला दिसणारा उदाहरण आउटपुटः**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

पूर्ण दस्तऐवजीकरण आणि पावलोपावली सूचना साठी पहा: **[📖 Solution Documentation](./solution/README.md)**

## 🎯 संपूर्ण उदाहरणे

या ट्यूटोरियलमध्ये सर्व प्रोग्रामिंग भाषांसाठी संपूर्ण आणि कार्यरत क्लायंट इम्प्लिमेंटेशन्स आम्ही दिली आहेत. ही उदाहरणे वर वर्णन केलेल्या पूर्ण कार्यक्षमतेवर आधारित आहेत आणि आपल्याला संदर्भ किंवा प्रारंभ बिंदू म्हणून वापरता येतील.

### उपलब्ध संपूर्ण उदाहरणे

| भाषा | फाइल | वर्णन |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ट्रान्सपरटसह संपूर्ण Java क्लायंट, व्यापक त्रुटी हाताळणीसह |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ट्रान्सपरटसह संपूर्ण C# क्लायंट, स्वयंचलित सर्व्हर स्टार्टअपसह |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | पूर्ण MCP प्रोटोकॉल सपोर्टसह संपूर्ण TypeScript क्लायंट |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | असिंक्रोनस/अवेट पॅटर्नसह संपूर्ण Python क्लायंट |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | टोकियो वापरून असिंक्रोनस ऑपरेशन्ससाठी संपूर्ण Rust क्लायंट |

प्रत्येक संपूर्ण उदाहरणात समाविष्ट आहे:
- ✅ **कनेक्शन स्थापनेसाठी** आणि त्रुटी हाताळणी
- ✅ **सर्व्हर शोधणे** (टूल्स, संसाधने, प्रॉम्प्ट्स जिथे लागू असतील)
- ✅ **कॅल्क्युलेटर ऑपरेशन्स** (योग, वजाबाकी, गुणाकार, भागाकार, मदत)
- ✅ **परिणाम प्रक्रिया** आणि स्वरूपित आउटपुट
- ✅ **संपूर्ण त्रुटी हाताळणी**
- ✅ **स्वच्छ, दस्तऐवजीकृत कोड** टप्प्याटप्प्याने टिप्पण्या सह

### संपूर्ण उदाहरणांसह सुरुवात करणे

1. वरील तक्ता मधून **आपली पसंतीची भाषा निवडा**
2. **संपूर्ण उदाहरण फाइल पाहा** पूर्ण अंमलबजावणी समजून घेण्यासाठी
3. उदाहरण चालवा [`complete_examples.md`](./complete_examples.md) मधील सूचनांचे पालन करून
4. आपला विशिष्ट वापरासाठी उदाहरण **संपादित आणि विस्तृत करा**

हे उदाहरण चालविणे आणि सानुकूल करण्याविषयी तपशीलवार दस्तऐवजीकरणासाठी पहा: **[📖 संपूर्ण उदाहरणे दस्तऐवज](./complete_examples.md)**

### 💡 सोल्यूशन विरुद्ध संपूर्ण उदाहरणे

| **सोल्यूशन फोल्डर** | **संपूर्ण उदाहरणे** |
|--------------------|--------------------- |
| बिल्ड फायलींसह पूर्ण प्रोजेक्ट संरचना | एकाच फाइलमध्ये अंमलबजावणी |
| अवलंबनांसह तत्पर चालू | लक्ष केंद्रीत कोड उदाहरणे |
| उत्पादनसमान सेटअप | शैक्षणिक संदर्भ |
| भाषेनिहाय टूलिंग | भाषांतर तुलना |

दोन्ही दृष्टिकोण मौल्यवान आहेत - संपूर्ण प्रोजेक्टसाठी **सोल्यूशन फोल्डर** वापरा आणि शिकण्यासाठी तसेच संदर्भासाठी **संपूर्ण उदाहरणे** वापरा.

## मुख्य मुद्दे

या अध्यायासाठी मुख्य मुद्दे खालीलप्रमाणे, क्लायंट बद्दल:

- सर्व्हरवरील वैशिष्ट्ये शोधणे आणि वापरण्यासाठी वापरता येतात.
- स्वतः सुरू करते त्याचवेळी (या अध्यायात जसे) सर्व्हरसाठी क्लायंट वापरू शकतो, पण चालू असलेल्या सर्व्हरशी क्लायंट कनेक्ट देखील होऊ शकतो.
- सर्व्हर क्षमतांची चाचणी घेण्यासाठी एक उत्कृष्ट मार्ग आहे, Inspector सारख्या पर्यायांबरोबर, जो मागील अध्यायात वर्णन केला होता.

## अतिरिक्त संसाधने

- [MCP मध्ये क्लायंट तयार करणे](https://modelcontextprotocol.io/quickstart/client)

## नमुने

- [Java कॅल्क्युलेटर](../samples/java/calculator/README.md)
- [.Net कॅल्क्युलेटर](../../../../03-GettingStarted/samples/csharp)
- [JavaScript कॅल्क्युलेटर](../samples/javascript/README.md)
- [TypeScript कॅल्क्युलेटर](../samples/typescript/README.md)
- [Python कॅल्क्युलेटर](../../../../03-GettingStarted/samples/python)
- [Rust कॅल्क्युलेटर](../../../../03-GettingStarted/samples/rust)

## पुढे काय

- पुढे: [LLM सह क्लायंट तयार करणे](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हे दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आले आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, मात्र कृपया लक्षात घ्या की ऑटोमेटेड अनुवादांमध्ये चूक किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्त्रोत म्हणून मानले पाहिजे. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे झालेल्या कोणत्याही गैरसमजात किंवा गैरव्याख्येमध्ये आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->