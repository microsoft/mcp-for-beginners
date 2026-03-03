# கிளையண்ட் உருவாக்குதல்

கிளையண்ட்கள் சுயமொரு பயன்பாடுகள் அல்லது ஸ்கிரிப்ட்டுகள் ஆகும், அவை MCP சர்வருடன் நேரடியாக தொடர்பு கொண்டு வளங்கள், கருவிகள் மற்றும் உவமைகளைக் கேட்பதற்காக செயல்படுகின்றன. சர்வருடன் தொடர்பு கொள்ள ஒரு காட்சியமைப்பு கிடைக்கும் இன்ஸ்பெக்டர் கருவியைப் பயன்படுத்துவதைவிட, உங்களின் சொந்த கிளையண்ட் எழுதுவது நிரலாக்கப்படக்கூடிய மற்றும் தானாக செயல்படும் தொடர்புக்களை அனுமதிக்கிறது. இது அபிவிருத்தியாளர்களுக்கு MCP திறன்களை தங்களது சொந்த பணிமுறைகளுக்கு இணைக்க, பணிகளை தானாக செய்ய மற்றும் குறிப்பிட்ட தேவைகளுக்கு ஏற்ற தனிப்பயன் தீர்வுகளை உருவாக்க உதவுகிறது.

## மேற்பார்வை

இந்த பாடத்தில் Model Context Protocol (MCP) சுற்றுச்சூழலில் உள்ள கிளையண்டுகள் என்ற கருத்தை அறிமுகம் செய்கிறது. நீங்கள் உங்கள் சொந்த கிளையண்டை எப்படி எழுதுவது மற்றும் அதை MCP சர்வருடன் எப்படி இணைப்பது என்பதைக் கற்றுக்கொள்வீர்கள்.

## கற்றல் குறிக்கோள்கள்

இந்த பாடம் முடிவுக்கு வந்தவுடன், நீங்கள்:

- கிளையண்ட் என்ன செய்ய முடியும் என்பதை புரிந்துகொள்ள முடியும்.
- உங்கள் சொந்த கிளையண்டை எழுத முடியும்.
- MCP சர்வருடன் கிளையண்டை இணைத்து பரிசோதித்து சர்வர் எதிர்பார்த்தபடி செயல்படுகிறதா என்று உறுதி செய்ய முடியும்.

## ஒரு கிளையண்ட் எழுத என்ன செய்ய வேண்டும்?

ஒரு கிளையண்டை எழுத, நீங்கள் பின்வரும் நடவடிக்கைகள் தேவை:

- **சரியான நூலகங்களை இறக்குமதி செய்யவும்**. நீங்கள் இதுவரை பயன்படுத்திய நூலகத்தையே பயன்படுத்துவீர்கள், வெவ்வேறு கட்டமைப்புகளுடன்.
- **ஒரு கிளையண்ட் உருவாக்கவும்**. இது கிளையண்ட் நகலை உருவாக்கி, தேர்ந்தெடுக்கப்பட்ட போக்குவரத்து முறையில் (transport method) அதனை இணைப்பதை உட்படுத்தும்.
- **எவற்றை பட்டியலிடுவது என்று முடிவு செய்யவும்**. உங்கள் MCP சர்வர் வளங்கள், கருவிகள் மற்றும் உவமைகளை கொண்டுள்ளது, எதை பட்டியலிட வேண்டும் என்று நீங்கள் தேர்ந்தெடுக்க வேண்டும்.
- **கிளையண்டை ஒரு ஹோஸ்ட் பயன்பாட்டுடன் ஒருங்கிணைக்கவும்**. சர்வரின் திறன்களை அறிந்தவுடன், உங்கள் ஹோஸ்ட் பயன்பாட்டுடன் இனைக்க வேண்டும், பயனர் உவமை அல்லது பிற கட்டளைகள் தட்டினால் சரியான சர்வர் செயல்பாடு அழைக்கப்பட வேண்டும்.

இப்போது நாம் மேல் நிலை நோக்கில் என்ன செய்யப்போகிறோம் என்பதை புரிந்து கொண்டோம், அடுத்ததாக ஒரு எடுத்துக்காட்டைப் பார்ப்போம்.

### ஒரு எடுத்துக்காட்டு கிளையண்ட்

இந்த எடுத்துக்காட்டு கிளையண்டை பார்ப்போம்:

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

// ப்ராம்ப்டுகளை பட்டியலிடு
const prompts = await client.listPrompts();

// ஒரு ப்ராம்ப்டை பெறு
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// வளங்களை பட்டியலிடு
const resources = await client.listResources();

// ஒரு வளத்தை படிக்கவும்
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ஒரு கருவியை அழைக்கவும்
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

மேலேயுள்ள குறியீட்டில் நாங்கள்:

- நூலகங்களை இறக்குமதி செய்தோம்
- கிளையண்ட் நகலை உருவாக்கி stdio போக்குவரத்தில் இணைத்தோம்.
- உவமைகள், வளங்கள் மற்றும் கருவிகளை பட்டியலிட்டு அவற்றை அனைத்து எடுப்பும்.

இதோ, MCP சர்வருடன் பேசக்கூடிய கிளையண்ட் உள்ளது.

அடுத்த பயிற்சி பகுதியில் ஒவ்வொரு குறியீட்டு துண்டுகளையும் விரிவாக விளக்குவோம்.

## பயிற்சி: கிளையண்ட் எழுதுதல்

மேலே சொன்னதுபோல், குறியீட்டை விளக்க நேரம் எடுத்துக் கொள்வோம், மற்றும் நீங்கள் விரும்பினால் குறியீட்டோடு இணைந்து செயல்படுங்கள்.

### -1- நூலகங்கள் இறக்குமதி செய்

நாம் தேவைப்படுவது நூலகங்களை இறக்குமதி செய்வதே, கிளையண்ட் மற்றும் தேர்ந்தெடுக்கப்பட்ட போக்குவரத்து முறையினை (stdio)த் தேவையாகக் கொள்கின்றோம். stdio உங்கள் உள்ளூர் கணினியில் இயக்கப்படுவதை நோக்கி விருப்பமுடைய பதிவு. SSE என்பது இன்னொரு போக்குவரத்து פרொட்டோக்கோல் ஆகும், அதை எதிர்கால அத்தியாயங்களில் காண்போம் ஆனால் தற்போது stdio-ன் வழியில் தொடர்கிறோம்.

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

Javaக்கானது, நீங்கள் முன் பயிற்சியில் இருந்து MCP சர்வருடன் இணைக்கும் கிளையண்டை உருவாக்க்வீர்கள். [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) இடைமுக Java Spring Boot திட்ட கட்டமைப்பைப் பயன்படுத்தி, `src/main/java/com/microsoft/mcp/sample/client/` கோப்பகத்தில் `SDKClient` என்ற புதிய கிளாஸ் உருவாக்கி கீழ்க்காணும் இறக்குமதிகளைச் சேர்க்கவும்:

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

`Cargo.toml` கோப்பில் பின்வரும் சார்புகளைச் சேர்க்க வேண்டும்.

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

அதன்பின், உங்கள் கிளையண்ட் குறியீட்டில் தேவையான நூலகங்களை இறக்குமதி செய்யலாம்.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

இப்போது உருவாக்குவோம்.

### -2- கிளையண்ட் மற்றும் போக்குவரத்தை உருவாக்கல்

போக்குவரத்து மற்றும் கிளையண்டின் நகலை உருவாக்க வேண்டும்:

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

மேலிருந்த குறியீட்டில்:

- stdio போக்குவரத்து நகலை உருவாக்கினோம். இதில் சர்வரை எப்படிப் பெறுவதும் துவக்குவதும் என்பதை உருவாக்கும் கட்டளைகள் தெரிவிக்கப்படுகின்றன, இது கிளையண்ட் உருவாக்கும்போது தேவைப்படும்.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- கிளையண்டை பெயர் மற்றும் பதிப்புடன் உருவாக்கினோம்.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- கிளையண்டை தேர்ந்தெடுக்கப்பட்ட போக்குவரத்தில் இணைத்தோம்.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio இணைப்புக்கான சர்வர் அளவுருக்களை உருவாக்கவும்
server_params = StdioServerParameters(
    command="mcp",  # இயக்கக்கூடியது
    args=["run", "server.py"],  # விருப்பமான கட்டளை வரி வாதங்கள்
    env=None,  # விருப்பமான சூழல் மாறிலிகள்
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # இணைப்பை ஆரம்பிக்கவும்
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

மேலிருந்து:

- தேவையான நூலகங்களை இறக்குமதி செய்தோம்
- சர்வர் அளவுரு பொருளை உருவாக்கினோம், எதனால் சர்வரை இயக்கு கிளையண்டுடன் இணைவோம்.
- `run` என்பது ஒரு முறை, அது `stdio_client`ஐ அழைத்து கிளையண்ட் அமர்வை துவங்கும்.
- `asyncio.run`க்கு `run` முறையை வழங்கும் நுழைவாயில் உருவாக்கினோம்.

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

மேலிருந்து:

- தேவையான நூலகங்கள் இறக்குமதி ஆனன.
- stdio போக்குவரத்தை உருவாக்கி `mcpClient` கிளையண்டை உருவாக்கினோம். இதனை MCP சர்வரில் அம்சங்களை பட்டியலிடவும் அழைக்கவும் பயன்படுத்துவோம்.

“Arguments” பகுதியில், *.csproj* அல்லது இயங்கும் கோப்பை குறிக்கலாம்.

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
        
        // உங்கள் கிளையன்ட் லாஜிக் இங்கே வரும்
    }
}
```

மேலிருந்து:

- MCP சர்வர் இயங்கும் `http://localhost:8080` இடத்தில் SSE போக்குவரத்தை அமைக்கும் முக்கிய முறை உருவாக்கப்பட்டது.
- போக்குவரத்தை கட்டுமான பின்புலமாக எடுத்துக்கொள்ளும் கிளையண்ட் வகுப்பை உருவாக்கினோம்.
- `run` முறையில் synchronous MCP கிளையண்டை போக்குவரத்தின் உதவியுடன் உருவாக்கி இணைத்தோம்.
- Java Spring Boot MCP சர்வர்களுடன் HTTP அடிப்படையான தொடர்புக்கு ஏற்ற SSE போக்குவரத்தைப் பயன்படுத்தினோம்.

#### Rust

இந்த Rust கிளையண்ட் சர்வர் "calculator-server" என்ற பக்கத் திட்டமாக இருக்கும் என நம்புகிறது, அதே கோப்பகத்தில். கீழே குறியீடு சர்வரை துவங்கி அதனுடன் இணைகிறது.

```rust
async fn main() -> Result<(), RmcpError> {
    // சர்வர் "calculator-server" என்ற சகோதர திட்டமாக அதே கோப்புறையில் உள்ளது என்று கருதி செயல் படுத்துக
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

    // செய்யவேண்டியது: துவக்கம் செய்யவும்

    // செய்யவேண்டியது: கருவிகளை பட்டியலிடுக

    // செய்யவேண்டியது: {"a": 3, "b": 2} என்ற аргுமான்ட்களுடன் add கருவியை அழைக்கவும்

    client.cancel().await?;
    Ok(())
}
```

### -3- சர்வர் அம்சங்களை பட்டியலிடுதல்

இப்போது கிளையண்ட் அணைக்கப்படக்கூடியது, ஆனால் அதன் அம்சங்களை பட்டியலிடவில்லை, அதை செய்யலாம்:

#### TypeScript

```typescript
// பட்டியல் கோரிக்கைகள்
const prompts = await client.listPrompts();

// பட்டியல் வளங்கள்
const resources = await client.listResources();

// பட்டியல் கருவிகள்
const tools = await client.listTools();
```

#### Python

```python
# பயன்பாட்டில் உள்ள வளங்களை பட்டியலிடுக
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# பயன்பாட்டில் உள்ள கருவிகளை பட்டியலிடுக
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

இங்கு கிடைக்கும் வளங்கள் `list_resources()` மற்றும் கருவிகள் `list_tools()` களை பட்டியலிடி அச்சிடுகிறோம்.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

மேலே, சர்வரில் உள்ள கருவிகளை எப்படி பட்டியலிடுவது எடுத்துக்காட்டு. ஒவ்வொரு கருவிக்கும் அதன் பெயரை அச்சிடுகிறோம்.

#### Java

```java
// கருவிகளை பட்டியலிடவும் மற்றும் காட்சி செய்யவும்
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// இணைப்பை உறுதிப்படுத்த சர்வரை பிங் செய்யலாம்
client.ping();
```

மேலிருந்து:

- MCP சர்வரிலிருந்து எல்லா கருவிகளையும் பெற `listTools()` அழைத்தோம்.
- சர்வருடன் இணைப்பு சரியானதா என `ping()` மூலம் உறுதிப்படுத்தினோம்.
- `ListToolsResult` என்பது அனைத்து கருவிகளின் பெயர், விளக்கம், மற்றும் உள்ளீட்டு கட்டமைப்புகளைக் கொண்டது.

சரி, இப்போது அனைத்து அம்சங்களையும் பெற்றுவிட்டோம். இவற்றைப் எப்போது பயன்படுத்துவது? இந்த கிளையண்ட் எளிமையானது, நீங்கள் தேவையானபோது அம்சங்களை தெளிவாக அழைக்க வேண்டும். அடுத்த அத்தியாயத்தில், தனித்துவமான பெரிய மொழி மாதிரி கொண்ட மேம்பட்ட கிளையண்டை உருவாக்குவோம். இப்போது சர்வர் அம்சங்களை அழைப்பது எப்படி என்பதை பார்ப்போம்:

#### Rust

முக்கிய வகுப்பில் கிளையண்டை தொடங்கி சர்வர் அம்சங்களை பட்டியலிடலாம்.

```rust
// துவக்கம் செய்யவும்
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// கருவிகள் பட்டியல்
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- அம்சங்களை அழைப்பு

அம்சங்களை அழைக்க சரியான கட்டளைகள் மற்றும் சில நேரங்களில் என்ன அழைக்கப்போகிறோம் என்பதை குறிப்பிட வேண்டும்.

#### TypeScript

```typescript

// ஒரு வளத்தைப் படி
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ஒரு கருவியை அழைக்கவும்
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// அழைப்பு பதில்
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

மேலிருந்து:

- ஒரு வளத்தை வாசிக்க `readResource()` மூலம் `uri` வழங்கி அழைக்கின்றோம். சர்வர் பக்கம் இதோ போல் இருக்கலாம்:

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

    `uri` மதிப்பு `file://example.txt` சர்வரிலுள்ள `file://{name}` உடன் பொருந்தும். `example.txt` `name` ஆக மாறும்.

- கருவியை அழைக்க, அதனுடைய `name` மற்றும் `arguments` கொண்டு:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- உவமை பெற, `getPrompt()` அழைத்து `name` மற்றும் `arguments` கொடுக்கிறது. சர்வர் குறியீடு:

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

    அதன்பின் உங்கள் கிளையண்ட் குறியீடு அதே மாதிரி இருக்கும்:

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
# ஒரு வளத்தை வாசிக்கவும்
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ஒரு கருவியை அழைக்கவும்
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

மேலிருந்து:

- `greeting` என்ற வளத்தை `read_resource` மூலம் அழைத்தோம்.
- `add` என்ற கருவியை `call_tool` மூலம் அழைத்தோம்.

#### .NET

1. கருவியை அழைக்க குறியீடு சேர்க்கலாம்:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. முடிவுகளை அச்சிட:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// பல கணக்கீட்டு கருவிகளை அழைக்கவும்
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

மேலிருந்து:

- பல கணக்கீட்டு கருவிகளை `callTool()` மூலம் `CallToolRequest` உடன் அழைத்தோம்.
- ஒவ்வொரு கருவி அழைப்பும் கருவியின் பெயர் மற்றும் அவசியமான அறிமுக டேட்டாவைக் கொண்டது.
- சர்வர் கருவிகள் குறிப்பிட்ட செயல்பாட்டு பெயர்களை எதிர்பார்க்கின்றன.
- முடிவுகள் `CallToolResult` வடிவில் வழங்கப்படுகின்றன.

#### Rust

```rust
// {"a": 3, "b": 2} என்ற காரணிகளுடன் add கருவியை அழைக்கவும்
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

### -5- கிளையண்டை இயக்குக

கிளையண்டை இயக்க கட்டளை:

#### TypeScript

*package.json* இல் "scripts" பகுதியில் சேர்க்கவும்:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

கிளையண்டை கீழ்கண்ட கட்டளையால் இயக்கவும்:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

முதல் MCP சர்வர் `http://localhost:8080` இல் இயங்குவதை உறுதி செய்து கிளையண்டை இயக்கவும்:

```bash
# உங்கள் திட்டத்தை கட்டமைக்கவும்
./mvnw clean compile

# கிளையண்டை இயக்கவும்
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

அல்லது, முழுமையான கிளையண்ட் திட்டத்தை `03-GettingStarted\02-client\solution\java` ஆய்வு கோப்பகத்தில் இயக்கவும்:

```bash
# தீர்வு கோப்புறைக்குச் செல்லுங்கள்
cd 03-GettingStarted/02-client/solution/java

# JAR கட்டமைத்து இயக்குங்கள்
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## பணியமைப்பு

இந்த பணியில், நீங்கள் கற்ற கிளையண்ட் உருவாக்கலில் உங்கள் சொந்த கிளையண்டை உருவாக்குவீர்கள்.

கீழே ஒரு சர்வர் உள்ளது, உங்கள் கிளையண்ட் மூலம் அழைக்க வேண்டும், அதில் சிறிது கூடுதல் அம்சங்களைச் சேர்க்க முயற்சிக்கவும்.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ஒரு MCP சேவையகத்தை உருவாக்கவும்
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ஒரு கூட்டல் கருவியைச் சேர்க்கவும்
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ஒரு இயக்கமுள்ள வரவேற்பு வளத்தைச் சேர்க்கவும்
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

// stdin இல் இருந்து செய்திகளைக் பெறத் தொடங்கி stdout இல் செய்திகளை அனுப்புங்கள்

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

# ஒரு MCP சேவையகத்தை உருவாக்கவும்
mcp = FastMCP("Demo")


# ஒரு கூட்டல் சாதனத்தைச் சேர்க்கவும்
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ஒரு இயக்கமயமான வாழ்த்து வளத்தைச் சேர்க்கவும்
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

இப்பிரોજெக்டில் [prompts மற்றும் resources சேர்க்க எப்படி என்பது](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) காணவும்.

மேலும் [prompts மற்றும் resources எப்படி அழைக்கப்படுவது](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) என்பதையும் பாருங்கள்.

### Rust

[முந்தைய பகுதியில்](../../../../03-GettingStarted/01-first-server), நீங்கள் எளிய MCP சர்வரை Rust-ல் உருவாக்க அறிவு பெற்றீர்கள். அதில் தொடரவோ அல்லது இதை அணுகவோ முடியும்: [MCP Server உதாரணங்கள்](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## தீர்வு

**தீர்வு கோப்பகம்** முழுமையான, தயாராக இயங்கக்கூடிய கிளையண்ட் அமலாக்கங்களை கொண்டுள்ளது, இத்தரக்கட்டுரையில் உள்ள அனைத்து கருத்துக்களையும் காட்டுகிறது. ஒவ்வொரு தீர்வும் தனிப்பட்ட கிளையண்ட் மற்றும் சர்வர் குறியீட்டைக் கொண்ட sway-இல் அமைந்துள்ளது.

### 📁 தீர்வு அமைப்பு

தீர்வு கோப்பகம் நிரல் மொழிக் கட்டமைப்புகளுக்கேற்ப பிரிக்கப்பட்டுள்ளது:

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

### 🚀 ஒவ்வொரு தீர்வும் கொண்டது

ஒவ்வொரு மொழிக்குமான தீர்வும் கொண்டவை:

- **முழுமையான கிளையண்ட் அமலாக்கம்** அனைத்துத் திறன்களுடன்
- **செயல்படும் திட்ட அமைப்பு**, சார்புகள் மற்றும் கட்டமைப்புகளுடன்
- **செயலாக்கும் ஸ்கிரிப்ட்டுகள்** எளிய அமைப்பு மற்றும் இயக்கத்திற்கு
- **விரிவான README** மொழிக்கான குறிப்புகளுடன்
- **பிழை கையாளுதல்** மற்றும் முடிவுகளை செயலாக்க உதாரணங்கள்

### 📖 தீர்வுகளைப் பயன்படுத்துதல்

1. **உங்கள் விருப்பமான மொழிக் கோப்பகத்தை திறக்கவும்**:

   ```bash
   cd solution/typescript/    # TypeScript க்காக
   cd solution/java/          # Java க்காக
   cd solution/python/        # Python க்காக
   cd solution/dotnet/        # .NET க்காக
   ```

2. **ஒவ்வொரு கோப்பகத்திலும் README வழிமுறைகளை பின்பற்றவும்**:
   - சார்புகளை நிறுவுதல்
   - திட்டத்தை கட்டமைத்தல்
   - கிளையண்டை இயக்குதல்

3. **உடைக்கப்படும் உதாரண வெளியீடு**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

முழுமையான ஆவணங்கள் மற்றும் படி படியாக உன்னதக் குறிப்புகளைப் பார்க்க: **[📖 தீர்வு ஆவணம்](./solution/README.md)**

## 🎯 முழுமையான உதாரணங்கள்

இந்தக் கற்றல் வழிகாட்டியில் உள்ள அனைத்து நிரல் மொழிகளுக்குமான முழுமையான செயல்படும் கிளையண்ட் அமலாக்கங்களைக் கொடுத்துள்ளோம். இவை முழுமையான செயல்பாடுகளை காட்டுகின்றன மற்றும் உங்கள் சொந்த திட்டங்களுக்கு தொடக்கமாகவும் உதவியாகவும் கொள்ளலாம்.

### கிடைக்கக்கூடிய முழு உதாரணங்கள்

| மொழி | கோப்பு | விளக்கம் |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE போக்குவரத்தைப் பயன்படுத்தி பிழை கையாளுதலுடன் முழுமையான Java கிளையண்ட் |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio போக்குவரத்துடன் தானாக சர்வர் துவக்கும் முழுமையான C# கிளையண்ட் |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | முழு MCP புரோட்டோக்கோல் ஆதரவு கொண்ட TypeScript கிளையண்ட் |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await வடிவமைப்புடன் Python கிளையண்ட் |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio பயன்படுத்தி async செயற்பாடுகளுடன் Rust கிளையண்ட் |

ஒவ்வொரு முழு உதாரணமும் கொண்டவை:
- ✅ **இணைப்பு நிறுவல்** மற்றும் பிழை கையாளல்  
- ✅ **சர்வர் கண்டறிதல்** (கருவிகள், வளங்கள், தேவையான இடங்களில் பதிவுகள்)  
- ✅ **கணக்கீட்டு செயல்பாடுகள்** (கூட்டல், கழித்தல், गुणிப்பு, வகுத்தல், உதவி)  
- ✅ **முடிவுகள் செயலாக்கம்** மற்றும் வடிவமைக்கப்பட்ட வெளியீடு  
- ✅ **பெருமளவு பிழை கையாளல்**  
- ✅ **சுத்தமான, ஆவணப்படுத்தப்பட்ட குறியீடு** மூலம் படி படி கருத்துக்கள்  

### முழுமையான உதாரணங்களுடன் துவக்கம்

1. மேலே உள்ள அட்டவணையில் இருந்து **உங்கள் விருப்பமான மொழியை** தேர்ந்தெடுக்கவும்  
2. முழுமையான அமலாக்கத்தை புரிந்துகொள்ள **முழுமையான உதாரண கோப்பை** பார்வையிடவும்  
3. [`complete_examples.md`](./complete_examples.md) ல் உள்ள அறிவுரைகளை பின்பற்றி **உதாரணத்தை இயக்கவும்**  
4. உங்கள் குறிப்பிட்ட பயன்பாட்டுக்கு **உதாரணத்தை மாற்றவும், விரிவாக்கவும்**  

இதில் உள்ள உதாரணங்களை இயக்குவது மற்றும் தனிப்பயனாக்குதல் குறித்த விரிவான ஆவணங்களுக்கு: **[📖 முழுமையான உதாரணங்கள் ஆவணங்கள்](./complete_examples.md)** பார்க்கவும்  

### 💡 தீர்வு மற்றும் முழுமையான உதாரணங்கள்

| **தீர்வு கோப்புறை** | **முழுமையான உதாரணங்கள்** |
|--------------------|--------------------- |
| கட்டுமான கோப்புகளுடன் கூடிய முழு திட்ட அமைப்பு | ஒரே கோப்பு செயல்பாடுகள் |  
| சார்புகள் உடன் உடனடி இயக்கத்துக்கு தயாராக உள்ளது | கவனிக்கப்பட்ட குறியீடு உதாரணங்கள் |  
| தயாரிப்பு போல அமைப்பு | கல்வி குறிப்பு |  
| மொழி சார்ந்த கருவிகள் | மொழி கடந்த ஒப்பீடு |  

இரு அணுகுமுறைகளும் மதிப்புமிக்கவை - முழுமையான திட்டத்திற்கு **தீர்வு கோப்புறையை** பயன்படுத்தவும், கற்றல் மற்றும் குறிப்பு நோக்கத்திற்கு **முழுமையான உதாரணங்களை** பயன்படுத்தவும்.  

## முக்கிய எடுத்துக்காட்டுகள்

இந்த அத்தியாயத்தின் முக்கிய எடுத்துக்காட்டுகள் வாடிக்கையாளர்களைப் பற்றி பின்வருவன:

- சர்வரில் உள்ள அம்சங்களை கண்டறிந்து, அழைக்க இரண்டிலும் பயன்படுத்த முடியும்.  
- இது தானே துவங்கும்போது ஒரு சர்வரைத் துவக்கலாம் (இந்த அத்தியாயத்தில் போன்று) ஆனால் வாடிக்கையாளர்கள் இயங்கும் சர்வர்களுடன் இணைக்க முடியும்.  
- இதில் சர்வர் திறன்களை பரிசோதிப்பதற்கான சிறந்த வழி ஆகும், முன்பு விளக்கப்பட்ட இன்பெக்டருக்கான மாற்றுகளுடன் ஒப்பிடுகையில்.  

## கூடுதல் வளங்கள்

- [MCP-இல் வாடிக்கையாளரை உருவாக்குதல்](https://modelcontextprotocol.io/quickstart/client)  

## மாதிரிகள்

- [Java கணக்கை](../samples/java/calculator/README.md)  
- [.Net கணக்கை](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript கணக்கை](../samples/javascript/README.md)  
- [TypeScript கணக்கை](../samples/typescript/README.md)  
- [Python கணக்கை](../../../../03-GettingStarted/samples/python)  
- [Rust கணக்கை](../../../../03-GettingStarted/samples/rust)  

## அடுத்தது  

- அடுத்தது: [LLM உடன் வாடிக்கையாளரை உருவாக்குதல்](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**பொறுப்புத்தாக்கல்**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையான [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயலும் போது, தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் சொந்த மொழியில் இருந்தே அதிகாரப்பூர்வ ஆதாரம் ஆகும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பை பயன்படுத்துவதில் ஏற்படும் புரிதல் தவறுகள் அல்லது தவறான விளக்கங்களுக்கு எங்களால் எந்த பொறுப்பும் ஏற்றுக்கொள்ளப்படாது.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->