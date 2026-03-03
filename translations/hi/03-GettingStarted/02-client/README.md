# एक क्लाइंट बनाना

क्लाइंट कस्टम एप्लिकेशन या स्क्रिप्ट होते हैं जो सीधे MCP सर्वर से संसाधन, टूल और प्रांप्ट अनुरोध करने के लिए संवाद करते हैं। निरीक्षक उपकरण का उपयोग करने के विपरीत, जो सर्वर के साथ संवाद करने के लिए एक ग्राफिकल इंटरफ़ेस प्रदान करता है, अपना स्वयं का क्लाइंट लिखने से प्रोग्रामेटिक और स्वचालित इंटरैक्शन संभव होता है। इससे डेवलपर्स MCP क्षमताओं को अपने कार्यप्रवाह में एकीकृत कर सकते हैं, कार्यों को स्वचालित कर सकते हैं, और विशेष आवश्यकताओं के अनुसार कस्टम समाधान बना सकते हैं।

## अवलोकन

यह पाठ MCP इकोसिस्टम के अंदर क्लाइंट्स की अवधारणा परिचय कराता है। आप सीखेंगे कि अपना स्वयं का क्लाइंट कैसे लिखा जाए और उसे MCP सर्वर से जोड़ा जाए।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- समझना कि क्लाइंट क्या कर सकता है।
- अपना खुद का क्लाइंट लिखना।
- MCP सर्वर के साथ क्लाइंट को कनेक्ट और टेस्ट करना ताकि सुनिश्चित किया जा सके कि सर्वर अपेक्षित रूप से कार्य करता है।

## क्लाइंट लिखने में क्या आता है?

क्लाइंट लिखने के लिए, आपको निम्न करना होगा:

- **सही लाइब्रेरीज आयात करें।** आप वही लाइब्रेरी उपयोग कर रहे होंगे जो पहले उपयोग की गई थी, बस निर्माण थोड़े अलग होंगे।
- **एक क्लाइंट इंस्टैंस बनाएँ।** इसमें एक क्लाइंट उदाहरण बनाना और इसे चुने हुए ट्रांसपोर्ट मेथड से कनेक्ट करना शामिल होगा।
- **निर्णय लें कि किन संसाधनों को सूचीबद्ध करना है।** आपका MCP सर्वर संसाधन, टूल्स और प्रांप्ट के साथ आता है, आपको निर्णय लेना है कि किसे सूचीबद्ध करना है।
- **क्लाइंट को होस्ट एप्लिकेशन के साथ एकीकृत करें।** एक बार जब आप सर्वर की क्षमताओं को जान लेते हैं, तो आपको इसे अपने होस्ट एप्लिकेशन में एकीकृत करना होगा ताकि यदि कोई उपयोगकर्ता प्रांप्ट या अन्य कमांड टाइप करता है तो सर्वर की संबंधित सुविधा को कॉल किया जाए।

अब जब हमने उच्च स्तर पर समझ लिया कि हमें क्या करना है, तो आइए अगला एक उदाहरण देखें।

### एक उदाहरण क्लाइंट

आइए इस उदाहरण क्लाइंट को देखें:

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

// सूची सार्णियाँ
const prompts = await client.listPrompts();

// एक सार्णी प्राप्त करें
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// संसाधन सूचीबद्ध करें
const resources = await client.listResources();

// एक संसाधन पढ़ें
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// एक उपकरण कॉल करें
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

पिछले कोड में हमने:

- लाइब्रेरीज आयात की
- क्लाइंट का एक उदाहरण बनाया और stdio ट्रांसपोर्ट के साथ कनेक्ट किया।
- प्रांप्ट्स, संसाधन और टूल सूचीबद्ध किए और उन्हें सभी को कॉल किया।

यहां आपके पास एक क्लाइंट है जो MCP सर्वर से संवाद कर सकता है।

आइए अगले अभ्यास खंड में समय लेकर प्रत्येक कोड स्निपेट को समझें और व्याख्या करें कि क्या हो रहा है।

## अभ्यास: क्लाइंट लिखना

जैसा ऊपर कहा गया है, चलिए कोड समझाने में समय लेते हैं, और आप चाहें तो साथ-साथ कोड भी कर सकते हैं।

### -1- लाइब्रेरीज आयात करना

आइए आवश्यक लाइब्रेरीज आयात करें, हमें क्लाइंट और चुने गए ट्रांसपोर्ट प्रोटोकॉल stdio के संदर्भ चाहिए होंगे। stdio एक प्रोटोकॉल है जो स्थानीय मशीन पर चलने के लिए अनुकूलित है। SSE एक और ट्रांसपोर्ट प्रोटोकॉल है जिसे हम भविष्य के अध्यायों में दिखाएंगे, लेकिन अभी के लिए stdio के साथ जारी रखें।

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

Java के लिए, आप पिछली अभ्यास से MCP सर्वर से कनेक्ट करने वाला क्लाइंट बनाएंगे। [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) में बताए गए उसी Java Spring Boot प्रोजेक्ट संरचना का उपयोग करते हुए, `src/main/java/com/microsoft/mcp/sample/client/` फ़ोल्डर में `SDKClient` नामक एक नया Java क्लास बनाएं और निम्नलिखित आयात जोड़ें:

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

आपको अपने `Cargo.toml` फ़ाइल में निम्न निर्भरताएं जोड़नी होंगी।

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

इसके बाद, आप अपने क्लाइंट कोड में आवश्यक लाइब्रेरीज़ आयात कर सकते हैं।

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

आइए इंस्टेंशिएशन की ओर बढ़ें।

### -2- क्लाइंट और ट्रांसपोर्ट का इंस्टेंशिएशन

हमें ट्रांसपोर्ट का एक उदाहरण और हमारे क्लाइंट का एक उदाहरण बनाना होगा:

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

पिछले कोड में हमने:

- stdio ट्रांसपोर्ट का एक उदाहरण बनाया। ध्यान दें कि यह सर्वर को ढूंढने और शुरू करने के लिए कमांड और तर्क निर्दिष्ट करता है, क्योंकि क्लाइंट बनाते समय यह करना आवश्यक होगा।

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- क्लाइंट का उदाहरण बनाया, उसे नाम और वर्शन दिया।

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- क्लाइंट को चुने गए ट्रांसपोर्ट से कनेक्ट किया।

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio कनेक्शन के लिए सर्वर पैरामीटर बनाएँ
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

- आवश्यक लाइब्रेरीज को आयात किया।
- एक सर्वर पैरामीटर ऑब्जेक्ट बनाया क्योंकि इसका उपयोग हम सर्वर चलाने के लिए करेंगे ताकि हम क्लाइंट से कनेक्ट कर सकें।
- एक `run` मेथड परिभाषित की जो अंततः `stdio_client` कॉल करती है ताकि क्लाइंट सेशन शुरू हो।
- एक प्रवेश बिंदु बनाया जहां हम `asyncio.run` को `run` मेथड प्रदान करते हैं।

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

पिछले कोड में हमने:

- आवश्यक लाइब्रेरीज आयात कीं।
- stdio ट्रांसपोर्ट बनाया और `mcpClient` नामक क्लाइंट बनाया। इसका उपयोग हम MCP सर्वर पर फीचर्स को सूचीबद्ध और कॉल करने के लिए करेंगे।

ध्यान दें, "Arguments" में आप *.csproj* या executable दोनों में से किसी को भी इंगित कर सकते हैं।

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
        
        // आपका क्लाइंट लॉजिक यहां जाता है
    }
}
```

पिछले कोड में हमने:

- एक मेन मेथड बनाया जो `http://localhost:8080` को इंगित करता है, जहां हमारा MCP सर्वर चल रहा होगा, और SSE ट्रांसपोर्ट सेट किया।
- एक क्लाइंट क्लास बनाया जो कन्स्ट्रक्टर के रूप में ट्रांसपोर्ट लेता है।
- `run` मेथड में ट्रांसपोर्ट का उपयोग करके सिंक्रोनस MCP क्लाइंट बनाया और कनेक्शन इनिशियलाइज़ किया।
- SSE (Server-Sent Events) ट्रांसपोर्ट का उपयोग किया, जो Java Spring Boot MCP सर्वरों के लिए HTTP आधारित संवाद के लिए उपयुक्त है।

#### Rust

यह Rust क्लाइंट मानता है कि सर्वर एक समान निर्देशिका में "calculator-server" नामक एक सहयोगी प्रोजेक्ट है। नीचे दिया गया कोड सर्वर को शुरू करेगा और उससे जुड़ जाएगा।

```rust
async fn main() -> Result<(), RmcpError> {
    // मान लीजिए सर्वर उसी डायरेक्टरी में एक सहोदर प्रोजेक्ट जिसका नाम "calculator-server" है
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

    // करने के लिए: प्रारंभ करें

    // करने के लिए: उपकरणों की सूची बनाएं

    // करने के लिए: add टूल को आर्गुमेंट्स = {"a": 3, "b": 2} के साथ कॉल करें

    client.cancel().await?;
    Ok(())
}
```

### -3- सर्वर फीचर्स सूचीबद्ध करना

अब हमारे पास एक क्लाइंट है जो चलने पर कनेक्ट हो सकता है। हालांकि, यह फीचर्स को सूचीबद्ध नहीं करता है, तो आइए इसे आगे करें:

#### TypeScript

```typescript
// सूचि प्रॉम्प्ट्स
const prompts = await client.listPrompts();

// सूचि संसाधन
const resources = await client.listResources();

// सूचि उपकरण
const tools = await client.listTools();
```

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
```

यहां हम उपलब्ध संसाधनों, `list_resources()` और टूल्स, `list_tools` सूचीबद्ध करते हैं और उन्हें प्रिंट करते हैं।

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ऊपर उदाहरण है कि हम सर्वर पर उपकरणों को कैसे सूचीबद्ध कर सकते हैं। प्रत्येक उपकरण के लिए हम उसका नाम प्रिंट करते हैं।

#### Java

```java
// उपकरणों की सूची बनाएं और प्रदर्शन करें
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// आप कनेक्शन सत्यापित करने के लिए सर्वर को पिंग भी कर सकते हैं
client.ping();
```

पिछले कोड में हमने:

- MCP सर्वर से उपलब्ध सभी टूल्स लाने के लिए `listTools()` कॉल किया।
- कनेक्शन काम कर रहा है यह सुनिश्चित करने के लिए `ping()` का उपयोग किया।
- `ListToolsResult` में सभी टूल्स की जानकारी होती है जैसे नाम, विवरण, और इनपुट स्कीमा।

बहुत बढ़िया, अब हमने सभी फीचर्स कैप्चर कर लिए हैं। सवाल है कि हम उन्हें कब उपयोग करें? यह क्लाइंट काफी सरल है, जिसका अर्थ है कि हमें जब फीचर्स चाहिए तो स्पष्ट रूप से कॉल करना होगा। अगले अध्याय में, हम एक अधिक उन्नत क्लाइंट बनाएंगे जिसमें अपनी बड़ी भाषा मॉडल, LLM तक पहुंच होगी। फिलहाल, आइए देखें कि सर्वर पर फीचर्स कैसे कॉल करें:

#### Rust

मेन फ़ंक्शन में, क्लाइंट इनिशियलाइज करने के बाद, हम सर्वर शुरू कर सकते हैं और इसके कुछ फीचर्स सूचीबद्ध कर सकते हैं।

```rust
// आरंभ करें
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// उपकरणों की सूची बनाएं
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- फीचर्स को कॉल करना

फीचर्स को कॉल करने के लिए हमें सही आर्गुमेंट्स निर्दिष्ट करने होंगे और कुछ मामलों में हम जो कॉल कर रहे हैं उसका नाम भी देना होगा।

#### TypeScript

```typescript

// एक संसाधन पढ़ें
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// एक उपकरण कॉल करें
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// प्रॉम्प्ट कॉल करें
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

पिछले कोड में हमने:

- एक संसाधन को पढ़ा, हम `readResource()` को `uri` निर्दिष्ट करके कॉल करते हैं। सर्वर साइड पर यह इस तरह दिख सकता है:

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

    हमारा `uri` मान `file://example.txt` सर्वर पर `file://{name}` से मेल खाता है। `example.txt` को `name` मैप किया जाएगा।

- एक टूल कॉल किया, इसे उसके `name` और `arguments` निर्दिष्ट करके कॉल किया:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- प्रांप्ट प्राप्त किया, प्रांप्ट पाने के लिए आप `getPrompt()` को `name` और `arguments` के साथ कॉल करते हैं। सर्वर कोड इस प्रकार होता है:

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

    और परिणामस्वरूप आपका क्लाइंट कोड इस प्रकार दिखेगा जो सर्वर पर घोषित के अनुरूप है:

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
# एक संसाधन पढ़ें
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# एक उपकरण कॉल करें
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

पिछले कोड में हमने:

- `greeting` नामक एक संसाधन को `read_resource` के माध्यम से कॉल किया।
- `add` नामक टूल को `call_tool` के माध्यम से कॉल किया।

#### .NET

1. आइए कुछ कोड जोड़ें जो टूल को कॉल करता है:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. परिणाम प्रिंट करने के लिए, यहां कुछ कोड है जो इसे संभालता है:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// विभिन्न कैलकुलेटर उपकरणों को कॉल करें
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

पिछले कोड में हमने:

- `callTool()` मेथड के साथ कई कैलकुलेटर टूल कॉल किए using `CallToolRequest` ऑब्जेक्ट्स।
- प्रत्येक टूल कॉल में टूल का नाम और उस टूल द्वारा अपेक्षित आर्गुमेंट्स का मैप शामिल है।
- सर्वर टूल्स विशिष्ट पैरामीटर नामों (जैसे गणितीय ऑपरेशन के लिए "a", "b") की अपेक्षा करते हैं।
- परिणाम `CallToolResult` ऑब्जेक्ट्स के रूप में वापस आते हैं जिनमें सर्वर से प्रतिक्रिया होती है।

#### Rust

```rust
// आर्गुमेंट्स के साथ ऐड टूल को कॉल करें = {"a": 3, "b": 2}
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

### -5- क्लाइंट चलाना

क्लाइंट चलाने के लिए, टर्मिनल में निम्न कमांड टाइप करें:

#### TypeScript

अपने *package.json* की "scripts" सेक्शन में निम्न एंट्री जोड़ें:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

क्लाइंट को निम्न कमांड से कॉल करें:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

सबसे पहले, सुनिश्चित करें कि आपका MCP सर्वर `http://localhost:8080` पर चल रहा है। फिर क्लाइंट चलाएं:

```bash
# अपना प्रोजेक्ट बनाएँ
./mvnw clean compile

# क्लाइंट चलाएँ
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

वैकल्पिक रूप से, आप समाधान फ़ोल्डर `03-GettingStarted\02-client\solution\java` में पूर्ण क्लाइंट प्रोजेक्ट चला सकते हैं:

```bash
# सॉल्यूशन डायरेक्टरी पर जाएं
cd 03-GettingStarted/02-client/solution/java

# JAR बनाएं और चलाएं
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## असाइनमेंट

इस असाइनमेंट में, आप जो सीखे हैं उसका उपयोग करते हुए अपना स्वयं का क्लाइंट बनाएंगे।

यहां एक सर्वर है जिसका उपयोग आप कर सकते हैं, आपको इसे अपने क्लाइंट कोड के माध्यम से कॉल करना है, देखें कि क्या आप सर्वर में अधिक फीचर्स जोड़ सकते हैं जिससे वह अधिक रोचक बन सके।

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// एक MCP सर्वर बनाएं
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// एक जोड़ने का उपकरण जोड़ें
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// एक गतिशील अभिवादन संसाधन जोड़ें
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

// stdin पर संदेश प्राप्त करना शुरू करें और stdout पर संदेश भेजना शुरू करें

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

# एक MCP सर्वर बनाएं
mcp = FastMCP("Demo")


# एक जोड़ टूल जोड़ें
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# एक गतिशील अभिवादन संसाधन जोड़ें
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

इस प्रोजेक्ट को देखें कि आप [प्रांप्ट्स और संसाधन कैसे जोड़ सकते हैं](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)।

साथ ही, इस लिंक को देखें कि [प्रांप्ट्स और संसाधनों को कैसे कॉल करें](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)।

### Rust

[पिछले खंड](../../../../03-GettingStarted/01-first-server) में, आपने सीखा कि Rust में सरल MCP सर्वर कैसे बनाएं। आप उस पर आगे बढ़ सकते हैं या इस लिंक को देखें जहां और Rust-आधारित MCP सर्वर उदाहरण मिलेंगे: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## समाधान

**समाधान फ़ोल्डर** में पूर्ण, तैयार-चलाने वाले क्लाइंट कार्यान्वयन शामिल हैं जो इस ट्यूटोरियल में कवर की गई सभी अवधारणाओं को प्रदर्शित करते हैं। प्रत्येक समाधान में क्लाइंट और सर्वर कोड अलग-अलग, स्व-निहित प्रोजेक्ट के रूप में व्यवस्थित होते हैं।

### 📁 समाधान संरचना

समाधान डिरेक्टरी प्रोग्रामिंग भाषा के अनुसार व्यवस्थित है:

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

### 🚀 प्रत्येक समाधान में क्या शामिल है

प्रत्येक भाषा-विशिष्ट समाधान प्रदान करता है:

- **पूरा क्लाइंट कार्यान्वयन** जिसमें ट्यूटोरियल के सभी फीचर्स शामिल हैं
- **कार्यशील प्रोजेक्ट संरचना** उचित निर्भरताओं और कॉन्फ़िगरेशन के साथ
- **बिल्ड और रन स्क्रिप्ट्स** आसान सेटअप और निष्पादन के लिए
- **विस्तृत README** भाषा-विशिष्ट निर्देशों के साथ
- **त्रुटि हैंडलिंग** और परिणाम प्रसंस्करण उदाहरण

### 📖 समाधानों का उपयोग कैसे करें

1. **अपनी पसंदीदा भाषा के फ़ोल्डर में जाएँ**:

   ```bash
   cd solution/typescript/    # टाइपस्क्रिप्ट के लिए
   cd solution/java/          # जावा के लिए
   cd solution/python/        # पाइथन के लिए
   cd solution/dotnet/        # .NET के लिए
   ```

2. **प्रत्येक फ़ोल्डर में README निर्देशों का पालन करें**:
   - निर्भरताओं की स्थापना के लिए
   - प्रोजेक्ट बिल्ड करने के लिए
   - क्लाइंट चलाने के लिए

3. **आपको ऐसा आउटपुट दिखेगा**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

पूर्ण दस्तावेज़ और चरण दर चरण निर्देशों के लिए देखें: **[📖 समाधान दस्तावेज़](./solution/README.md)**

## 🎯 पूर्ण उदाहरण

हमने इस ट्यूटोरियल में शामिल सभी प्रोग्रामिंग भाषाओं के लिए पूर्ण, कार्यशील क्लाइंट कार्यान्वयन प्रदान किए हैं। ये उदाहरण उपर्युक्त सभी कार्यात्मकता दिखाते हैं और संदर्भ कार्यान्वयन या अपने प्रोजेक्ट के लिए शुरुआती बिंदु के रूप में उपयोग किए जा सकते हैं।

### उपलब्ध पूर्ण उदाहरण

| भाषा       | फाइल                                   | विवरण                                                    |
|------------|---------------------------------------|----------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java)       | SSE ट्रांसपोर्ट के साथ पूर्ण Java क्लाइंट जिसमें व्यापक त्रुटि प्रबंधन है |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs)       | stdio ट्रांसपोर्ट के साथ पूर्ण C# क्लाइंट जिसमें स्वचालित सर्वर स्टार्टअप है |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | पूर्ण MCP प्रोटोकॉल समर्थन के साथ TypeScript क्लाइंट       |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py)       | async/await पैटर्न का उपयोग करते हुए पूर्ण Python क्लाइंट |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)           | Tokio का उपयोग करते हुए पूर्ण Rust क्लाइंट                  |

प्रत्येक पूर्ण उदाहरण में शामिल हैं:
- ✅ **कनेक्शन स्थापित करना** और त्रुटि प्रबंधन
- ✅ **सर्वर खोज** (उपकरण, संसाधन, संकेत जहां लागू हों)
- ✅ **कैलकुलेटर संचालन** (जोड़ना, घटाना, गुणा करना, भाग देना, सहायता)
- ✅ **परिणाम प्रोसेसिंग** और स्वरूपित आउटपुट
- ✅ **व्यापक त्रुटि प्रबंधन**
- ✅ **साफ़, दस्तावेजीकृत कोड** चरण-दर-चरण टिप्पणियों के साथ

### पूर्ण उदाहरणों के साथ शुरू करना

1. ऊपर दी गई तालिका में से **अपनी पसंदीदा भाषा चुनें**
2. पूर्ण कार्यान्वयन को समझने के लिए **पूर्ण उदाहरण फ़ाइल की समीक्षा करें**
3. [`complete_examples.md`](./complete_examples.md) में निर्देशों का पालन करते हुए **उदाहरण चलाएं**
4. अपने विशिष्ट उपयोग के लिए **उदाहरण संशोधित और विस्तारित करें**

इन उदाहरणों को चलाने और अनुकूलित करने के लिए विस्तृत दस्तावेज़ीकरण देखें: **[📖 पूर्ण उदाहरण दस्तावेज़ीकरण](./complete_examples.md)**

### 💡 समाधान बनाम पूर्ण उदाहरण

| **समाधान फ़ोल्डर** | **पूर्ण उदाहरण** |
|--------------------|------------------|
| बिल्ड फ़ाइलों के साथ पूर्ण प्रोजेक्ट संरचना | एकल-फ़ाइल कार्यान्वयन |
| निर्भरता के साथ रन के लिए तैयार | केंद्रित कोड उदाहरण |
| उत्पादन-समान सेटअप | शैक्षिक संदर्भ |
| भाषा-विशिष्ट टूलिंग | क्रॉस-भाषा तुलना |

दोनों दृष्टिकोण मूल्यवान हैं - पूर्ण परियोजनाओं के लिए **समाधान फ़ोल्डर** का उपयोग करें और सीखने तथा संदर्भ के लिए **पूर्ण उदाहरण** का उपयोग करें।

## मुख्य निष्कर्ष

इस अध्याय के लिए मुख्य निष्कर्ष क्लाइंट्स के बारे में निम्नलिखित हैं:

- सर्वर पर फीचर खोजने और कॉल करने दोनों के लिए उपयोग किए जा सकते हैं।
- यह खुद को शुरू करते समय सर्वर भी शुरू कर सकता है (जैसा कि इस अध्याय में था) लेकिन क्लाइंट्स चल रहे सर्वरों से भी जुड़ सकते हैं।
- सर्वर क्षमताओं को जांचने का एक शानदार तरीका है, जैसे कि पिछले अध्याय में वर्णित इंस्पेक्टर के विकल्प के साथ।

## अतिरिक्त संसाधन

- [MCP में क्लाइंट बनाना](https://modelcontextprotocol.io/quickstart/client)

## नमूने

- [जावा कैलकुलेटर](../samples/java/calculator/README.md)
- [.Net कैलकुलेटर](../../../../03-GettingStarted/samples/csharp)
- [जावास्क्रिप्ट कैलकुलेटर](../samples/javascript/README.md)
- [टाइपस्क्रिप्ट कैलकुलेटर](../samples/typescript/README.md)
- [पाइथन कैलकुलेटर](../../../../03-GettingStarted/samples/python)
- [रस्ट कैलकुलेटर](../../../../03-GettingStarted/samples/rust)

## अगला क्या है

- अगला: [LLM के साथ क्लाइंट बनाना](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। हम सटीकता के लिए प्रयासरत हैं, लेकिन कृपया ध्यान रखें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->