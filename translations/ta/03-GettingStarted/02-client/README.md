# ஒரு கிளையன்டை உருவாக்குதல்

கிளையன்டுகள் தனிப்பயன் பயன்பாட்டுகளோ அல்லது ஸ்கிரிப்டுகளோ ஆகும், அவை நேரடியாக MCP சேவையகத்துடன் தொடர்புகொண்டு வளங்கள், கருவிகள் மற்றும் முன்னோட்டங்களைக் கோருகின்றன. சேவையகத்துடன் தொடர்பு கொண்டிருக்கும் இன்ஸ்பெக்டர் கருவியை பயன்படுத்துவதற்கு மாறாக, அது ஒரு காட்சி இடைமுகத்தை வழங்குகிறது; உங்கள் சொந்த கிளையண்டை எழுதுதல் மூலம் நிரலாக்கமான மற்றும் தானாகத் தொடர்புகள் ஏற்படுத்த முடியும். இது மேம்படுத்துனர்களுக்கு தங்கள் சொந்த பணியிடங்களில் MCP திறன்களை இணைக்க, பணிகளை தானாக செயல்படுத்த மற்றும் குறிப்பிட்ட தேவைகளுக்கு ஏற்ப தனிப்பயன் தீர்வுகளை கட்டமைக்க அனுமதிக்கிறது.

## மேற்பார்வை

இந்த பாடத்தில், நீங்கள் Model Context Protocol (MCP) சூழலில் உள்ள கிளையன்டுகளின் கருத்தை அறிந்துகொள்வீர்கள். உங்கள் சொந்த கிளையண்டை எழுதுவது எப்படி என்பது மற்றும் அதை MCP சேவையகத்திற்கு இணைப்பது எப்படி என்று கற்றுக்கொள்வீர்கள்.

## கற்றல் நோக்கங்கள்

இந்த பாடம் முடிந்ததும், நீங்கள் செய்யக்கூடியவை:

- கிளையண்ட் என்ன செய்யக்கூடியது என்பதை புரிந்து கொள்வது.
- உங்கள் சொந்த கிளையண்டை எழுதுவது.
- கிளையண்டை MCP சேவையகத்துடன் இணைத்து சோதனை செய்து, அது எதிர்பார்த்தபடி செயல்படுகிறதா என்பதை உறுதிப்படுத்துவது.

## கிளையண்ட் எழுத என்ன வேண்டும்?

கிளையண்ட் எழுதுவதற்காக, நீங்கள் பின்வரும் செயல்களை செய்ய வேண்டும்:

- **தக்க நூலகங்களை இறக்கு**. நீங்கள் முன்பு பயன்படுத்திய அதே நூலகத்தை பயன்படுத்துவீர்கள், ஆனால் வெவ்வேறு கட்டமைப்புகளுடன்.
- **ஒரு கிளையண்டை உருவாக்கு**. இது கிளையண்ட் ஒரு உதாரணத்தை உருவாக்கி, தேர்ந்தெடுக்கப்பட்ட போக்குவரத்து முறைக்கு (transport method) இணைப்பதை உள்ளடக்கியது.
- **எந்த வளங்களை பட்டியலிட வேண்டும் என்று தீர்மானி**. உங்கள் MCP சேவையகம் வளங்கள், கருவிகள் மற்றும் முன்னோட்டங்களை வழங்குகிறது, அவை எந்தவையென தேர்வு செய்ய வேண்டும்.
- **கிளையண்டை ஒரு ஹோஸ்ட் பயன்பாட்டுடன் ஒருங்கிணை**. சேவையகத்தின் திறன்களை அறிந்த பின்பு, உங்கள் ஹோஸ்ட் பயன்பாட்டுக்கு இதை ஒருங்கிணைக்க வேண்டும், பயனர் முன்னோட்டம் அல்லது கட்டளையை தட்டச்சு செய்தால், தொடர்புடைய சேவையக அம்சம் செயல்படும்.

இப்போது நாங்கள் மேலோட்டமாக என்ன செய்யப்போகிறோம் என்று புரிந்துகொண்டோம், அடுத்து ஒரு எடுத்துக்காட்டைப் பார்ப்போம்.

### ஒரு எடுத்துக்காட்டு கிளையண்ட்

இந்த எடுத்துக்காட்டு கிளையண்டைப் பார்ப்போம்:

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

// ஏளனைப்பட்டியலிடு
const prompts = await client.listPrompts();

// ஒரு ஏளனை பெறு
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// வளங்களை பட்டியலிடு
const resources = await client.listResources();

// ஒரு வளத்தை வாசி
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

முன்னொரு குறியீட்டில் நாம் செய்தவை:

- நூலகங்களை இறக்கியுள்ளோம்
- கிளையண்ட் உதாரணத்தை உருவாக்கி stdio மூலம் போக்குவரத்தில் இணைத்துள்ளோம்.
- முனைப்புகள், வளங்கள் மற்றும் கருவிகளை பட்டியலிட்டு அனைத்தையும் செயல்படுத்தியுள்ளோம்.

இதோ, MCP சேவையகத்துடன் பேசக்கூடிய ஒரு கிளையண்ட்.

அடுத்த பயிற்சி பகுதியை நோக்கி நாம் எடுத்துக்காட்டில் உள்ள ஒவ்வொரு குறியீட்டு துண்டையும் விளக்கிப் பேசுவோம்.

## பயிற்சி: கிளையண்டை எழுதுதல்

மேலே கூறியது போல், நாம் குறியீட்டை விளக்க நேரம் எடுத்துக்கொள்வோம், விருப்பமானால் நீங்கள் அதே நேரத்தில் குறியீடு செய்யலாம்.

### -1- நூலகங்களை இறக்குதல்

தேவையான நூலகங்களை இறக்குவோம், கிளையண்டுக்கும் நாம் தேர்ந்தெடுத்த போக்குவரத்து நெறிமுறைக்கும்,stdioக்கு. stdio என்பது உங்கள் உள்ளக கணினியில் இயங்கும் செயல்களுக்கு ஏற்ப ஒரு நெறிமுறை. SSE எனும் மற்றொரு போக்குவரத்து நெறிமுறையை எதிர்கால அத்தியாயங்களில் காட்டுவோம், அது மற்றொரு விருப்பம். ஆனால் இப்பொழுது stdio உடன் தொடர்வோம்.

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

ஜாவாவுக்கு, நீங்கள் முந்தய பயிற்சியில் இருந்து MCP சேவையகத்துடன் இணைக்கும் ஒரு கிளையண்டை உருவாக்குவீர்கள். [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) என்ற ஜாவா ஸ்பிரிங் பூட் திட்ட கட்டமைப்பை பயன்படுத்தி, `src/main/java/com/microsoft/mcp/sample/client/` கோப்பகத்தில் `SDKClient` என்ற புதிய ஜாவா வகுப்பு உருவாக்கி பின்வரும் இறக்குமதிகளை சேர்க்கவும்:

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

உங்கள் `Cargo.toml` கோப்பில் பின்வரும் சார்புகளைச் சேர்க்க வேண்டும்.

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

அங்கு இருந்து, உங்கள் கிளையண்ட் குறியீட்டில் தேவையான நூலகங்களை இறக்கலாம்.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

இப்போது உருவாக்குவதை நோக்கி அடுத்தடுத்து செல்வோம்.

### -2- கிளையண்டையும் போக்குவரத்தையும் உருவாக்கல்

போக்குவரத்து மற்றும் கிளையண்டின் உதாரணங்களை உருவாக்க வேண்டும்:

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

முன்னொரு குறியீட்டில் நாம் செய்தவை:

- stdio போக்குவரத்தை உருவாக்கியுள்ளோம். இதன் மூலம் சேவையகத்தை எவ்வாறு கண்டுபிடித்து தொடங்க வேண்டும் என்று கட்டளையும் அர்களையும் குறிப்பிடுகிறது, இது கிளையண்டை உருவாக்கும்போது தேவைப்படும்.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- கிளையண்ட் உருவாக்கி அதற்கு பெயர் மற்றும் பதிப்பு கொடுத்துள்ளோம்.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- கிளையண்ட் தேர்ந்தெடுக்கப்பட்ட போக்குவரத்துடன் இணைக்கப்பட்டுள்ளது.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio இணைப்புக்கான சேவையக இயக்கி параметрங்களை உருவாக்கவும்
server_params = StdioServerParameters(
    command="mcp",  # இயக்கக்கூடிய
    args=["run", "server.py"],  # விருப்ப கட்டளை வரிசை வாதங்கள்
    env=None,  # விருப்ப சூழல் மாறிலிகள்
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # இணைப்பை தொடங்குக
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

முன்னொரு குறியீட்டில் நாம் செய்தவை:

- தேவையான நூலகங்களை இறக்கியுள்ளோம்
- சேவையக பண்பகங்களை உருவாக்கியுள்ளோம், இது சேவையகத்தை இயக்கு என்று கிளையண்டுடன் இணைக்க பயன்படுத்தப்படும்.
- `run` என்ற முறை வரையறுத்துள்ளோம், அது `stdio_client` ஐ அழைக்கும், இது கிளையண்ட் அமர்வைத் தொடங்குகிறது.
- `asyncio.run` இற்கு `run` முறையை வழங்கும் நுழைவு புள்ளியை உருவாக்கியுள்ளோம்.

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

முன்னொரு குறியீட்டில் நாம் செய்தவை:

- தேவையான நூலகங்களை இறக்கியுள்ளோம்.
- stdio போக்குவரத்தை உருவாக்கி `mcpClient` என்ற கிளையண்ட் உருவாக்கியுள்ளோம். இதுவே MCP சேவையகத்தின் அம்சங்களை பட்டியல் செய்து அழைக்க பயன்படுத்தப்படும்.

கவனிக்கவும், "Arguments" இல், *.csproj* அல்லது செயல்படக்கூடிய கோப்பை குறிப்பிடலாம்.

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
        
        // உங்கள் கிளையেন্ট லாஜிக் இங்கே போடவும்
    }
}
```

முன்னொரு குறியீட்டில் நாம் செய்தவை:

- MCP சேவையகம் இயங்க உள்ள `http://localhost:8080` எனும் URL ஐ குறிக்கின்ற SSE போக்குவரத்தை அமைக்கும் முக்கிய முறை உருவாக்கியுள்ளோம்.
- போக்குவரத்தை கட்டுமான மாற்றி (constructor parameter) ஆகக் கொண்டு கிளையண்ட் வகுப்பு உருவாக்கியுள்ளோம்.
- `run` முறையில், போக்குவரத்தைப் பயன்படுத்தி ஒத்திசைவுடைய MCP கிளையண்டை உருவாக்கி இணைப்பைத் தொடங்கியுள்ளோம்.
- Java Spring Boot MCP சேவையகங்களுக்கு பொருத்தமான HTTP-அடிப்படையிலான SSE (Server-Sent Events) போக்குவரத்தை பயன்படுத்தியுள்ளோம்.

#### Rust

இந்த Rust கிளையண்ட் சேவையகம் ஒத்திசைவுப் திட்டமாக உள்ள "calculator-server" என்ற பெயரில் இருக்கிறது என்று கருதுகிறது. கீழ்க்கண்ட குறியீடு சேவையகத்தைத் தொடங்கி இணைக்கிறது.

```rust
async fn main() -> Result<(), RmcpError> {
    // சர்வர் அதே அடைவு உள்ள "calculator-server" எனும் சக கிளை திட்டம் என்று நினைக்கவும்
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

    // செய்யவேண்டியது: ஆரம்பிக்கவும்

    // செய்யவேண்டியது: கருவிகள் பட்டியலிடவும்

    // செய்யவேண்டியது: {"a": 3, "b": 2} என்ற arguments உடன் add கருவியை அழைக்கவும்

    client.cancel().await?;
    Ok(())
}
```

### -3- சேவையக அம்சங்களை பட்டியலிடல்

இப்போது, நாம் ஒரு கிளையண்டை உருவாக்கியுள்ளோம், அதனை இயக்கினால் அது சேவையகத்துடன் இணைகிறது. ஆனால் அது சேவையக அம்சங்களை பட்டியலிடவில்லை, அதை இப்போது செய்வோம்:

#### TypeScript

```typescript
// பாட்வடிவங்களை பட்டியலிடு
const prompts = await client.listPrompts();

// வளங்களை பட்டியலிடு
const resources = await client.listResources();

// கருவிகளைக் பட்டியலிடு
const tools = await client.listTools();
```

#### Python

```python
# பயன்படுத்தக்கூடிய வளங்களை பட்டியலிடு
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# பயன்படுத்தக்கூடிய கருவிகளை பட்டியலிடு
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

இங்கு, நாங்கள் கிடைக்கக் கூடிய வளங்கள் `list_resources()` மற்றும் கருவிகள் `list_tools` என பட்டியலிட்டு, அவற்றை அச்சிடுகிறோம்.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

மேற்கண்டதில், சேவையகத்தில் உள்ள கருவிகளை இவ்வாறு பட்டியலிடலாம். ஒவ்வொரு கருவிக்கும் அதன் பெயர் அச்சிடப்படுகிறது.

#### Java

```java
// கருவிகளை பட்டியலிட்டு காட்சிப்படுத்து
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// தொடர்பை சரிபார்க்கவும், நீங்கள் சேவையகத்தை பிங் செய்யலாம்
client.ping();
```

முன்னொரு குறியீட்டில் நாம் செய்தவை:

- MCP சேவையகத்தில் உள்ள அனைத்து கருவிகளையும் பெற `listTools()` அழைத்தோம்.
- சேவையக இணைப்பு சரிபார்ப்பதற்காக `ping()` பயன்படுத்தியது.
- `ListToolsResult` உள் கருவி பெயர்கள், விளக்கங்கள் மற்றும் உள்ளீடு வடிவங்கள் ஆகியவை உள்ளடங்கிய தகவலை கொண்டுள்ளது.

மிகச் சிறந்தது, இப்போது நாம் அனைத்து அம்சங்களையும் பெற்றுள்ளோம். இப்போது எப்போது அவற்றைப் பயன்படுத்துவது? இந்த கிளையண்டு மிக எளிதாகும், அதாவது தேவையான போது நாம் விளக்கமாகவே அந்த அம்சங்களை அழைக்கவேண்டும். அடுத்த அத்தியாயத்தில், செம்மையானதொரு செம்மையிலான வடிவமைக்கப்பட்ட LLM (பெரிய மொழி மாதிரி) உடன் கூடிய கிளையண்டை உருவாக்கப்போகிறோம். இப்போது, சேவையகத்தில் அம்சங்களை எப்படி அழைக்கலாம் என்பதைப் பார்ப்போம்:

#### Rust

முதன்மை முறையில், கிளையண்ட் தொடங்கியபின், சேவையகத்தை ஆரம்பித்து சில அம்சங்களை பட்டியலிடலாம்.

```rust
// துவக்கம் செய்க
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// கருவிகள் பட்டியலிடு
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- அம்சங்களை அழைத்தல்

அம்சங்களை அழைக்க, சரியான வாதங்களை குறிப்பிடுதல் மற்றும் சில நேரங்களில் பெயரையும் குறிப்பிடுதல் அவசியம்.

#### TypeScript

```typescript

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

// உத்திரவாதத்தை அழைக்கவும்
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

முன்னொரு குறியீட்டில் நாம் செய்தவை:

- ஒரு வளத்தைப் படிக்க, `readResource()` ஐ `uri` கொடுத்து அழைக்கும். சேவையக வழியில் இது இதுபோல இருக்கும்:

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

    எங்கள் `uri` மதிப்பு `file://example.txt` சேவையகத்தில் உள்ள `file://{name}` உடன் பொருந்துகிறது. `example.txt` `name` ஆக மாறும்.

- கருவியை அழைக்க, அதன் `name` மற்றும் `arguments` ஆகியவற்றைக் குறிப்பிட்டு அழைக்கிறோம்:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- முன்னோட்டம் பெற, `getPrompt()` ஐ `name` மற்றும் `arguments` கொண்டு அழைக்கிறோம். சேவையக குறியீடு இவ்வாறாக இருக்கும்:

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

    எனவே உங்கள் கிளையண்ட் குறியீடு சேவையகத்தில் அறிவிக்கப்பட்டதைப் பொருந்தும் போல்:

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

முன்னொரு குறியீட்டில் நாம் செய்தவை:

- `greeting` என்ற வளத்தை `read_resource` மூலம் அழைத்தோம்.
- `add` என்ற கருவியை `call_tool` மூலம் அழைத்தோம்.

#### .NET

1. கருவி அழைக்கும் குறியீடு சேர்க்கலாம்:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. முடிவை அச்சிட குறியீடு இங்கே உள்ளது:

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

முன்னொரு குறியீட்டில் நாம் செய்தவை:

- பல கணக்கிடும் கருவிகளை `callTool()` முறையால் `CallToolRequest` பொருட்களை வைத்து அழைத்தோம்.
- ஒவ்வொரு கருவி அழைப்பும் கருவி பெயரையும், அக்கருவிக்கு தேவையான வாதங்களின் `Map`-ஐ கொண்டுள்ளது.
- சேவையக கருவிகள் குறிப்பிட்ட பரிசோதனை பெயர்களைக் (எ. g. "a", "b") எதிர்பார்க்கின்றன.
- முடிவுகள் `CallToolResult` பொருட்களில் சேவையகத்திலிருந்து கிடைக்கும் பதில்களுடன் இருக்கின்றன.

#### Rust

```rust
// கூலிக்கும் கருவியை காரணிகளுடன் அழைக்கவும் = {"a": 3, "b": 2}
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

### -5- கிளையண்டை இயக்குதல்

கிளையண்டை இயக்க டெர்மினலில் கீழ்க்காணும் கட்டளையை தட்டச்சு செய்யவும்:

#### TypeScript

*package.json* இல் "scripts" பகுதியில் பின்வரும் பதிப்பைச் சேர்க்கவும்:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

கிளையண்டை கீழ்காணும் கட்டளையால் அழைக்கவும்:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

முதலில், உங்கள் MCP சேவையகம் `http://localhost:8080` என்ற முகவரியில் இயங்கி இருப்பதை உறுதி செய்யுங்கள். பிறகு கிளையண்டை இயக்குங்கள்:

```bash
# உங்கள் திட்டத்தை கட்டவும்
./mvnw clean compile

# கிளையண்டை இயக்கவும்
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

அல்லது, தீர்வு கோப்பகமான `03-GettingStarted\02-client\solution\java`-இல் வழங்கப்படும் முழுமையான கிளையண்ட் திட்டத்தை இயக்கலாம்:

```bash
# தீர்வு அடைவிற்கு செல்லவும்
cd 03-GettingStarted/02-client/solution/java

# JAR கட்டமைக்கவும் இயக்கவும்
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## பணிசெய்தி

இந்த பணிசெய்தியில், நீங்கள் கற்றுக்கொண்டவற்றைப் பயன்படுத்தி ஒரு கிளையண்டை உருவாக்குவீர்கள், ஆனால் உங்கள் சொந்த கிளையண்டாக:

நீங்கள் உங்கள் கிளையண்ட் குறியீட்டின் மூலம் அழைக்க வேண்டிய சேவையகம் இதோ; இதை பயன்படுத்தி அதிலுள்ள அம்சங்களை அதிகரிக்க முயற்சிக்கவும்.

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

// ஒரு இயக்கக்கூடிய வரவேற்பு நடவடிக்கைச் சேர்க்கவும்
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

// stdin இல் இருந்து தகவல்களை பெற தொடங்கி stdout இல் தகவல்களை அனுப்பவும்

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


# ஒரு கூட்டல் கருவியைக் கூட்டவும்
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ஒரு கதிரியக்க வரவேற்பு வளத்தைச் சேர்க்கவும்
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

இந்த திட்டத்தைப் பாருங்கள், [முன்னோட்டங்கள் மற்றும் வளங்களைச் சேர்க்க](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) எப்படி என்று.

மேலும், இந்த இணைப்பைக் கண்டு [முன்னோட்டங்கள் மற்றும் வளங்களை அழைப்பது எப்படி](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) என்பதைப் பாருங்கள்.

### Rust

[முந்தய பகுதியில்](../../../../03-GettingStarted/01-first-server), நீங்கள் Rust கொண்டு எளிய MCP சேவையகத்தை உருவாக்குவது கற்றீர்கள். அது மேலேயும் வளர்த்துக் கொள்ளலாம் அல்லது இதோ மற்ற Rust அடிப்படையிலான MCP சேவையக உதாரணங்கள்: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## தீர்வு

**தீர்வு கோப்பகம்** முழுமையான, இயக்கக்கூடிய கிளையண்ட் செயல்முறைகளை கொண்டுள்ளது, இந்த பாடத்தில் உள்ள அனைத்து கருத்துக்களையும் விளக்குகிறது. ஒவ்வொரு தீர்வும் கிளையண்ட் மற்றும் சேவையக குறியீடுகளைக் கொண்ட தனித்தனி, தனித்துவமான திட்டங்கள் ஆகும்.

### 📁 தீர்வு கட்டமைப்பு

தீர்வு அடைவு நிரல் மொழி அடிப்படையில் ஒழுங்குபடுத்தப்பட்டுள்ளது:

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

### 🚀 ஒவ்வொரு தீர்வும் உள்ளவை

ஒவ்வொரு மொழி-சொந்த தீர்வும் வழங்குகிறது:

- **முழுமையான கிளையண்ட் செயல்பாடு** பாடத்தில் உள்ள அனைத்து அம்சங்களுடன்
- **செயல்படுத்தப்பட்ட திட்ட கட்டமைப்பு** தேவையான சார்புகளும் கட்டமைப்புகளும் உடன்
- **எளிய நிறுவல் மற்றும் இயக்க சுட்டிகள்** 
- **விரிவான README** மொழிக்கேற்ற பயிற்சி
- **பிழை கையாளுதல் மற்றும் முடிவுகளைக் கையாளும் உதாரணங்கள்**

### 📖 தீர்வுகளைப் பயன்படுத்துதல்

1. **உங்கள் விருப்பமான மொழி கோப்பகத்தைக் திற**:

   ```bash
   cd solution/typescript/    # TypeScript க்கானது
   cd solution/java/          # Java க்கானது
   cd solution/python/        # Python க்கானது
   cd solution/dotnet/        # .NET க்கானது
   ```

2. **ஒவ்வொரு கோப்பகத்திலும் README வழிமுறைகளை பின்பற்று**:
   - சார்புகளை நிறுவுதல்
   - திட்டத்தை கட்டல்
   - கிளையண்டை இயக்குதல்

3. **உங்கள் கண்ணோட்டமாக காண வேண்டிய உதாரண வெளிச்சம்**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

முழுமையான ஆவணங்கள் மற்றும் படிப்படியான வழிமுறைகளுக்கு, இங்கே காணவும்: **[📖 தீர்வு ஆவணம்](./solution/README.md)**

## 🎯 முழுமையான எடுத்துக்காட்டுகள்

இந்த பாடத்தில் உள்ள அனைத்து நிரல் மொழிகளுக்கும் முழுமையான, செயல்படும் கிளையண்ட் செயலாக்கங்களை வழங்கியுள்ளோம். இவை மேலே விளக்கப்பட்ட முழுமையான செயல்பாடுகளைக் காட்டுகின்றன, குறிப்புகள் விளக்கங்களோ அல்லது உங்கள் சொந்த திட்டங்களுக்கு தொடக்க புள்ளிகளோ ஆக பயன்படுத்தலாம்.

### கிடைக்கும் முழுமையான எடுத்துக்காட்டுகள்

| மொழி | கோப்பு | விளக்கம் |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | முழுமையான Java கிளையண்ட் SSE போக்குவரத்துடன் மற்றும் விரிவான பிழை கையாளுதல் உடன் |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | முழுமான C# கிளையண்ட் stdio போக்குவரத்துடன் மற்றும் தானாக சேவையக தொடக்கம் செய்யும் |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | முழுமையான TypeScript கிளையண்ட் MCP நெறிமுறை முழுமையாக ஆதரிக்கும் |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | முழுமையான Python கிளையண்ட் async/await முறைகள் உடன் |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | முழுமையான Rust கிளையண்ட் Tokio உடன் அசிங்க்ரோனஸ் செயல்பாடுகள் |

ஒவ்வொரு முழுமையான எடுத்துக்காட்டிலும்:

- ✅ **இணைப்பு நிறுவுதல் மற்றும் பிழை கையாளுதல்**
- ✅ **சேவையக கண்டுபிடிப்பு** (கருவிகள், வளங்கள், முன்னோட்டங்கள் தேவையான இடங்களில்)
- ✅ **கணக்கீட்டு இயக்கங்கள்** (கூட்டல், கழித்தல், பெருக்கல், வகுத்தல், உதவி)
- ✅ **முடிவு செயலாக்கம் மற்றும் வடிவமைக்கப்பட்ட வெளியீடு**
- ✅ **முழுமையான பிழை கையாளுதல்**

- ✅ **சுத்தமான, ஆவணப்படுத்தப்பட்ட குறியீடு** படிநிலையான கருத்துகளுடன்

### முழுமையான எடுத்துக்காட்டுகளுடன் ஆரம்பிப்பது

1. மேலே உள்ள அட்டவணையில் இருந்து **உங்களுக்குப் பொருந்தும் மொழியை தேர்ந்தெடுக்கவும்**
2. **முழுமையான எடுத்துக்காட்டு கோப்பை மதிப்பாய்வு செய்யவும்** முழு அமல்படுத்தலினை புரிந்துகொள்ள
3. [`complete_examples.md`](./complete_examples.md) இல் உள்ள வழிமுறைகளை பின்பற்றி **எடுத்துக்காட்டை இயக்கவும்**
4. உங்கள் குறிப்பிட்ட பயன்பாட்டுக்கு ஏற்ப **எடுத்துக்காட்டை மாற்றவும் மற்றும் விரிவாக்கவும்**

இந்த எடுத்துக்காட்டுகளை இயக்குவதற்கும் தனிப்பயனாக்குவதற்கும் விரிவான ஆவணங்களுக்கு, பாருங்கள்: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 தீர்வு vs. முழுமையான எடுத்துக்காட்டுகள்

| **தீர்வு கோப்பு** | **முழுமையான எடுத்துக்காட்டுகள்** |
|--------------------|--------------------- |
| கட்டமைப்பு கோப்புகள் உள்ள முழு திட்ட கட்டமைப்பு | தனித்த கோப்பு செயலாக்கங்கள் |
| தேவையான சார்ந்த கோப்புகளுடன் இயக்க தயாரானது | கவனம் செலுத்தப்பட்ட குறியீடு எடுத்துக்காட்டுகள் |
| தயாரிப்பு போன்ற அமைப்பு | கல்வி குறிப்பு |
| மொழி-பொதுவான கருவிகள் | முறைப்பாடுகளை ஒப்பிடுதல் |

இவை இரண்டும் விலைமதிப்புள்ளவை - முழு திட்டங்களுக்கு **தீர்வு கோப்பை** பயன்படுத்தவும், கற்றலும் குறிப்பு நோக்கிலும் **முழுமையான எடுத்துக்காட்டுகளை** பயன்படுத்தவும்.

## முக்கிய எடுத்துக்காட்டுகள்

இந்த அத்தியாயத்துக்கான முக்கிய எடுத்துக்காட்டுகள் கிளையன்ட்கள் குறித்தது:

- சேவையகத்தில் உள்ள அம்சங்களை கண்டுபிடிக்கவும் அழைக்கவும் பயன்படுத்தப்படலாம்.
- தன்னை துவக்கும் போது ஒரு சேவையகத்தைத் தொடங்கலாம் (இந்த அத்தியாயப் பொருள் போல) ஆனால் கிளையன்ட்கள் இயங்கும் சேவையகத்துடன் இணைக்கப்பட முடியும்.
- முன் அத்தியாயத்தில் விவரிக்கப்பட்டுள்ள முகவர் போன்ற தேர்வுகளுடன் சேவையக திறன்களை சோதிக்க சிறந்த வழி.

## கூடுதல் ஆதாரங்கள்

- [MCP இல் கிளையன்ட்களை உருவாக்குவது](https://modelcontextprotocol.io/quickstart/client)

## மாதிரிகள்

- [ஜாவா கணக்கீட்டாளர்](../samples/java/calculator/README.md)
- [.NET கணக்கீட்டாளர்](../../../../03-GettingStarted/samples/csharp)
- [ஜாவாச்கிரிப்ட் கணக்கீட்டாளர்](../samples/javascript/README.md)
- [டைப் ஸ்கிரிப்ட் கணக்கீட்டாளர்](../samples/typescript/README.md)
- [பைத்தான் கணக்கீட்டாளர்](../../../../03-GettingStarted/samples/python)
- [ரஸ்ட் கணக்கீட்டாளர்](../../../../03-GettingStarted/samples/rust)

## அடுத்து என்ன

- அடுத்து: [LLM உடன் கிளையன்டை உருவாக்கல்](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->