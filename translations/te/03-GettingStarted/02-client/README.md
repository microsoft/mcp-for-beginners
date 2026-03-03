# క్లయింట్ సృష్టించడం

క్లయింట్లు అనేవి కస్టమ్ అప్లికేషన్లు లేదా స్క్రిప్ట్లు, ఇవి MCP సర్వర్‌తో నేరుగా కమ్యూనికేట్ చేసి వనరులు, టూల్స్, మరియు ప్రాంప్ట్‌లను అభ్యర్థిస్తాయి. సర్వర్‌తో ఇన్‌టరాక్ట్ కావడానికి గ్రాఫికల్ ఇంటర్‌ఫేస్‌ని అందించే ఇన్స్పెక్టర్ టూల్‌ను ఉపయోగించడం కాకుండా, మీ సొంత క్లయింట్ రాయడం ప్రోగ్రామాటిక్ మరియు ఆటోమేటిక్ ఇంటరాక్షన్లకు వీలును ఇస్తుంది. ఇది డెవలపర్‌లకు MCP విధానాలను తమ పనిప్రవాహాల్లో అనుసంధానం చేయడానికి, టాస్క్‌లను ఆటోమేట్ చేయడానికి, మరియు నిర్దిష్ట అవసరాలకు తగిన కస్టమ్ పరిష్కారాలను నిర్మించడానికి వీలు కల్పిస్తుంది.

## అవలోకనం

ఈ పాఠం Model Context Protocol (MCP) పరిసరాల్లో క్లయింట్లు అనే కాన్సెప్టును పరిచయం చేస్తుంది. మీ సొంత క్లయింట్‌ను ఎలా రాయాలో మరియు దాన్ని MCP సర్వర్‌తో ఎలా కనెక్ట్ చేయాలో మీరు నేర్చుకుంటారు.

## అభ్యాస లక్ష్యాలు

ఈ పాఠం ముగింపు నాటికి, మీరు చేయగలుగుతారు:

- క్లయింట్ ఏమి చేయగలదో అర్థం చేసుకోవడం.
- మీ సొంత క్లయింట్ రాయడం.
- MCP సర్వర్‌తో క్లయింట్‌ను కనెక్ట్ చేసి పరీక్షించడం, దీంతో సర్వర్ నిబంధన ప్రకారం పనిచేస్తుందో లేదో నిర్ధారించుకోవడం.

## క్లయింట్ రాయడంలో ఏమి వస్తుంది?

క్లయింట్ రాయడానికి, మీరు ఈ క్రింద చెప్పిన ప్రక్రియలను అనుసరించాల్సి ఉంటుంది:

- **సరైన లైబ్రరీలను దిగుమతి (ఇంపోర్ట్) చేసుకోండి**. ముందే ఉపయోగించినంతే లైబ్రరీ, కేవలం వేరే నిర్మాణాలు (constructs).
- **క్లయింట్‌ను ఉదాహరించండి (instantiate)**. ఇది ఒక క్లయింట్ ఉదాహరణను (instance) సృష్టించి, మీరు ఎంచుకున్న ట్రాన్స్‌పోర్ట్ పద్ధతికి కనెక్ట్ చేయడాన్ని కలిగి ఉంటుంది.
- **ఏ వనరులు పట్టిక చేయాలనుకుంటున్నారో నిర్ణయించుకోండి**. మీ MCP సర్వర్ వనరులు, టూల్స్ మరియు ప్రాంప్ట్‌లతో వస్తుంది, ఎటువంటి వాటిని పట్టిక చేయాలో ఎంచుకోవాలి.
- **క్లయింట్‌ను హోస్ట్అప్ అప్లికేషన్‌తో ఏకీకృతం చేయండి**. సర్వర్ యొక్క సామర్థ్యాలను తెలుసుకున్న తర్వాత, ఉపయోగించేవారి వలన ప్రాంప్ట్ లేదా ఇతర కమాండ్‌లు టైప్ చేసినప్పుడు, అవసరమైన సర్వర్ ఫీచర్‌ను సూచించగలిగే విధంగా మీ హోస్ట్ అప్లికేషన్‌లో ఈ క్లయింట్‌ను ఏకీకృతం చేయాలి.

ఇప్పుడు మేము ఉన్నత స్థాయిలో ఏమి చేయబోతున్నామో అర్థం చేసుకున్నాము, తదుపరి ఉదాహరణను చూద్దాం.

### ఒక ఉదాహరణ క్లయింట్

ఈ ఉదాహరణ క్లయింట్‌కి ఓ చూపు వేయండి:

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

// ప్రాంప్ట్‌ల జాబితా
const prompts = await client.listPrompts();

// ఒక ప్రాంప్ట్ పొందండి
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// వనరుల జాబితా
const resources = await client.listResources();

// ఒక వనరు చదవడం
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ఒక టూల్ కాల్ చేయండి
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

పైన ఇచ్చిన కోడ్‌లో మేము:

- లైబ్రరీలను ఇంపోర్ట్ చేసాము
- ఒక క్లయింట్ యొక్క ఉదాహరణను సృష్టించి, stdio ట్రాన్స్‌పోర్ట్ ద్వారా కనెక్ట్ చేసాము.
- ప్రాంప్ట్‌లు, వనరులు మరియు టూల్స్‌ని జాబితా చేసి వాటన్నింటినీ ఆహ్వానించాము.

ఇలా చేయడం ద్వారా, మీరు MCP సర్వర్‌తో మాట్లాడగలిగే ఒక క్లయింట్‌ను పొందారు.

తదుపరి వ్యాయామ విభాగంలో ప్రతి కోడ్ స్నిపెట్‌ను కళామాటగా విడగొట్టి ఏం జరుగుతుందో వివరించుకుందాం.

## వ్యాయామం: క్లయింట్ రాయడం

పైగా చెప్పినట్లుగా, కోడ్‌ను సమగ్రంగా వివరించేందుకు మరియు కావలసిన వారు కోడ్ చేయడానికి సమయం వేయండి.

### -1- లైబ్రరీలను దిగుమతి చేసుకోవడం

అవసరమైన లైబ్రరీలను దిగుమతి చేసుకుందాం, దీనికి మనకు క్లయింట్ మరియు గా ఎంచుకున్న ట్రాన్స్‌పోర్ట్ ప్రోటోకాల్, stdio కి సూచనలు అవసరం. stdio అనేది మీ స్థానిక మెషీన్‌లో నడపబడి ఉండే అప్లికేషన్ల కోసం రూపొందించిన ప్రోటోకాల్. SSE అనేది భవిష్యత్ అధ్యాయాల్లో చూపించనున్న మరో ట్రాన్స్‌పోర్ట్ ప్రోటోకాల్, ఇది ప్రతిపాదించుకుంటే మీకు మరో ఎంపిక.

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

జావా లో, మీరు ముందటి వ్యాయామం నుండి MCP సర్వర్‌కు కనెక్ట్ అవ్వడానికి ఒక క్లయింట్ సృష్టించాలి. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) నుండి Java Spring Boot ప్రాజెక్ట్ నిర్మాణాన్ని ఉపయోగించి, `src/main/java/com/microsoft/mcp/sample/client/` ఫోల్డర్‌లో `SDKClient` అనే కొత్త Java క్లాస్ సృష్టించి ఈ దిగుమతులు చేర్చండి:

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

మీ `Cargo.toml` ఫైల్‌లో ఈ డిపెండెన్సీలను చేర్చండి:

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

ఆ తర్వాత, అవసరమైన లైబ్రరీలను క్లయింట్ కోడ్‌లో ఇంపోర్ట్ చేసుకోండి.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ఇంకా ముందుకు వెళ్తూ ఉదాహరణ సృష్టిద్దాం.

### -2- క్లయింట్ మరియు ట్రాన్స్‌పోర్ట్ ఉదాహరణ తీసుకోవడం (Instantiation)

ట్రాన్స్‌పోర్ట్ మరియు క్లయింట్ ఉదాహరణలు సృష్టించాల్సి ఉంటుంది:

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

పైన ఇచ్చిన కోడ్‌లో:

- stdio ట్రాన్స్‌పోర్ట్ ఉదాహరణను సృష్టించాము. ఇది సర్వర్‌ను ఎలా కనుగొని ప్రారంభించాలో సూచించే కమాండ్ మరియు ఆర్గుమెంట్లను సూచిస్తుంది, ఇది క్లయింట్ సృష్టించే సమయంలో అవసరం అవుతుంది.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- క్లయింట్‌ను పేరు మరియు వెర్షన్ ఇచ్చి ఉదాహరించాము.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- క్లయింట్‌ను ఎంచుకున్న ట్రాన్స్‌పోర్ట్‌కు కనెక్ట్ చేసాము.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio కనెక్షన్ కోసం సర్వర్ పరామితులు సృష్టించండి
server_params = StdioServerParameters(
    command="mcp",  # నడపగల ఫైల్
    args=["run", "server.py"],  # ఐచ్ఛిక కమాండ్ లైన్ ఆర్గ్యూమెంట్లు
    env=None,  # ఐచ్ఛిక వాతావరణ మార్పిఠాలు
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # కనెక్షన్ ప్రారంభించండి
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

పైన ఇచ్చిన కోడ్‌లో:

- అవసరమైన లైబ్రరీలను దిగుమతి చేసుకున్నాము
- సర్వర్ పారామీటర్ల ఆబ్జెక్టును ఉదాహరించాము, దీన్నిఉపయోగించి సర్వర్ నడిపి క్లయింట్‌కు కనెక్ట్ అవుతాము
- `stdio_client` అనే క్లయింట్ సెషన్ ప్రారంభించే `run` అనే మేతడ్ నిర్వచించాము.
- `asyncio.run` కు `run` పద్ధతిని అందించే ఎంట్రీ పాయింట్ సృష్టించాము.

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

పైన ఇచ్చిన కోడ్‌లో:

- అవసరమైన లైబ్రరీలను ఇంపోర్ట్ చేసాము.
- stdio ట్రాన్స్‌పోర్ట్ సృష్టించి, `mcpClient` క్లయింట్‌ను సృష్టించాము. దీన్ని MCP సర్వర్‌పై ఫీచర్లను జాబితా చేయడానికి మరియు ఆహ్వానించడానికి ఉపయోగిస్తాము.

గమనిక: "Arguments" లో మీరు *.csproj* ఫైల్ లేదా ఎగ్జిక్యూటబుల్‌కు సూచించవచ్చు.

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
        
        // మీ క్లైంట్ లాజిక్ ఇక్కడికి వస్తుంది
    }
}
```

పైన ఇచ్చిన కోడ్‌లో:

- `http://localhost:8080` వద్ద నడిచే MCP సర్వర్‌కు సనం సూచించిన SSE ట్రాన్స్‌పోర్ట్ ని సెట్ చేసే మెయిన్ మేతడ్ సృష్టించాము.
- ట్రాన్స్‌పోర్ట్‌ను కన్స్ట్రక్టర్ పరామీటర్‌గా తీసుకునే క్లయింట్ క్లాస్ సృష్టించాము.
- `run` మెల్తోడ్లో ట్రాన్స్‌పోర్ట్‌ను ఉపయోగించి సింక్రోనస్ MCP క్లయింట్ సృష్టించి కనెక్షన్ ను ప్రారంభించాము.
- Java Spring Boot MCP సర్వర్లతో HTTP-ఆధారిత కమ్యూనికేషన్‌కు తగిన SSE (సర్వర్-సెంట్ ఈవెంట్స్) ట్రాన్స్‌పోర్ట్‌ను ఉపయోగించాము.

#### Rust

ఈ Rust క్లయింట్ సర్వర్‌ను అదే డైరెక్టరీలో "calculator-server" అనే సిబ్లింగ్ ప్రాజెక్టుగా ఉంచుకునేందుకు ఆధారపడి ఉంటుంది. క్రింది కోడ్ సర్వర్‌ను ప్రారంభించి దానికి కనెక్ట్ అవుతుంది.

```rust
async fn main() -> Result<(), RmcpError> {
    // సర్వర్‌ను అదే డైరెక్టరీలో "calculator-server" అని పేరు కలిగిన సోదర ప్రాజెక్ట్‌గా భావించండి
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

    // చేయవలసిన పని: ప్రారంభి చేయండి

    // చేయవలసిన పని: టూల్స్ జాబితా చేయండి

    // చేయవలసిన పని: ఆర్గ్యుమెంట్లతో add tool కాల్ చేయండి = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- సర్వర్ ఫీచర్ల జాబితా

ఇప్పుడు, మీరు ప్రోగ్రామ్ నడిస్తే కనెక్ట్ అయ్యే ఒక క్లయింట్ ఉన్నHelpers. అయితే అది తన ఫీచర్లను జాబితా చేయదు, కాబట్టి దాన్ని చేద్దాం:

#### TypeScript

```typescript
// ప్రాంప్ట్స్ జాబితా
const prompts = await client.listPrompts();

// వనరుల జాబితా
const resources = await client.listResources();

// సాధనాల జాబితా
const tools = await client.listTools();
```

#### Python

```python
# లభ్యమైన వనరులను జాబితా చేయండి
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# లభ్యమైన సాధనాలను జాబితా చేయండి
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ఇక్కడ అందుబాటులో ఉన్న వనరులు `list_resources()` మరియు టూల్స్ `list_tools`ని జాబితా చేసి తామూ అందిస్తున్నాము.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

పైన ఒక ఉదాహరణగా సర్వర్ పై టూల్స్ ఎలా జాబితా చేయాలో ఇచ్చాము. ప్రతీ టూల్ పేరును మనం ప్రింట్ చేస్తున్నాము.

#### Java

```java
// పరికరాలను జాబితా చేయండి మరియు ప్రదర్శించండి
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// కనెక్షన్‌ను నిర్ధారించడానికి మీరు సర్వర్‌ను పింగ్ చేయవచ్చు
client.ping();
```

పైన ఇచ్చిన కోడ్‌లో:

- MCP సర్వర్ నుండి అందుబాటులో ఉన్న అన్ని టూల్స్‌ను `listTools()` తో పిలవడం.
- సర్వర్ కనెక్షన్ పని చేస్తుందో లేదో నిర్ధారించడానికి `ping()` పిలవడం.
- `ListToolsResult` లో అన్ని టూల్స్ గురించి పేర్లు, వివరణలు, ఇన్‌పుట్ స్కీమాలు ఉంటాయి.

బాగుంది, ఇప్పుడు మేము అన్ని ఫీచర్లను పొందగలిగాం. ఇప్పుడు వీటిని ఎప్పుడు వాడుతాం? ఈ క్లయింట్ చాలా సింపుల్ అయినది, అంటే మీరు కావలసినప్పుడు ఫీచర్లను స్పష్టంగా కాల్ చేయాలి. తదుపరి అధ్యాయంలో, దీని స్వంత పెద్ద భాషా మోడల్, LLM కలిగి ఉన్న అభివృద్ధి చెందిన క్లయింట్‌ను సృష్టిస్తాము. ఇప్పటికీ, సర్వర్‌పై ఫీచర్లను ఎలా ఆహ్వానించాలో చూద్దాం:

#### Rust

ప్రధాన ఫంక్షన్‌లో, క్లయింట్‌ను ప్రారంభించిన తర్వాత, సర్వర్‌ను ప్రారంభించి కొన్ని ఫీచర్లను జాబితా చేయవచ్చు.

```rust
// 초기화
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// లిస్టు సాధనాలు
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ఫీచర్లను ఆహ్వానించడం

ఫీచర్లను ఆహ్వానించడానికి సరైన ఆర్గుమెంట్లు ఇవ్వడం మరియు కొన్ని సందర్భాల్లో ఆ ఆహ్వానించదలచిన వనరుల పేరును నిర్ధారించడం అవసరం.

#### TypeScript

```typescript

// రిసోర్స్‌ని చదవండి
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ఒక టూల్‌ను కాల్ చేయండి
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// ప్రాంప్ట్‌ని కాల్ చేయండి
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

పైన ఇచ్చిన కోడ్‌లో:

- వనరును చదవడం, `readResource()` కాల్ చేసి `uri`ని స్పెసిఫై చెయ్యడం. ఇది సర్వర్ వైపు ఇలా ఉంటుంది:

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

    మా `uri` విలువ `file://example.txt` సర్వర్ వైపు `file://{name}` కి సరిపోతుంది. `example.txt` `name`కి మ్యాప్ అవుతుంది.

- టూల్‌ను పిలవడం, `name` మరియు `arguments`ని స్పెసిఫై చేసి పిలవడం:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- ప్రాంప్ట్ పొందడం: `getPrompt()`ని `name` మరియు `arguments`తో పిలవడం. సర్వర్ కోడ్ ఈ విధంగా ఉంది:

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

    దీంతో మీ క్లయింట్ కోడ్ కూడా సర్వర్‌లో ప్రకటించినట్లుగా ఉంటుంది:

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
# ఒక వనరును చదవండి
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ఒక సాధనాన్ని పిలవండి
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

పైన ఇచ్చిన కోడ్‌లో:

- `greeting` అనే వనరును `read_resource` ఉపయోగించి పిలిచాము.
- `add` అనే టూల్‌ను `call_tool` ఉపయోగించి ఆహ్వానించాము.

#### .NET

1. టూల్‌ను పిలవడానికి కొడైంకు:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. ఫలితాన్ని ప్రింట్ చేయడానికి కొడైంకు:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// వివిధ కాలిక్యులేటర్ టూల్స్‌ను పిలవండి
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

పైన ఇచ్చిన కోడ్‌లో:

- పలు కాల్క్యులేటర్ టూల్స్‌ను `callTool()` మరియు `CallToolRequest` ఆబ్జెక్ట్స్ తో పిలిచాము.
- ప్రతి టూల్ కాల్ టూల్ పేరు మరియు అవసరమైన ఆర్గుమెంట్లను `Map` లో ఇస్తుంది.
- సర్వర్ టూల్స్ కొన్ని నిర్దిష్ట పారామీటర్ పేర్లను ఆశిస్తాయి (ఉదా: గణిత కార్యకలాపాలకు "a", "b").
- ఫలితాలు సర్వర్ నుండి వచ్చిన స్పందనతో కూడిన `CallToolResult` వస్తాయి.

#### Rust

```rust
// ఆర్గ్యుమెంట్లతో add టూల్‌కు కాల్ చేయాలి = {"a": 3, "b": 2}
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

### -5- క్లయింట్‌ను నడపడం

క్లయింట్‌ను నడపడానికి, టెర్మినల్‌లో క్రింది ఆజ్ఞను టైప్ చేయండి:

#### TypeScript

మీ "scripts" సెక్షన్‌లో *package.json* లో క్రింది ఎంట్రీని చేర్చండి:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

క్లయింట్‌ను క్రింది ఆజ్ఞతో పిలవండి:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

ముందుగా, మీ MCP సర్వర్ `http://localhost:8080` లో నడుస్తుందో లేదో చూసుకోండి. ఆ తర్వాత క్లయింట్ ను నడపండి:

```bash
# మీ ప్రాజెక్ట్‌ను నిర్మించండి
./mvnw clean compile

# క్లైయింట్‌ను నడపండి
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

వ్యతిరేకంగా, మీరు సొల్యూషన్ ఫోల్డర్ `03-GettingStarted\02-client\solution\java` లో అందించిన పూర్తి క్లయింట్ ప్రాజెక్టన్ని నడపవచ్చు:

```bash
# సొల్యూషన్ డైరెక్టరీకి నావిగేట్ చేయండి
cd 03-GettingStarted/02-client/solution/java

# JAR ను నిర్మించి అమలు చేయండి
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## అసైన్‌మెంట్

ఈ అసైన్‌మెంట్‌లో, మీరు క్లయింట్ సృష్టించడంలో నేర్చుకున్న దేనిని ఉపయోగించి, మీ సొంత క్లయింట్‌ను సృష్టించాలి.

మీరు పిలవవలసిన ఈ సర్వర్ ఉంది; దానిని ఉపయోగించి సర్వర్లో మరిన్ని ఫీచర్లను జోడించి మరింత ఆసక్తిగా మార్చండి.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ఒక MCP సర్వర్ తయారు చేయండి
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ఒక అదనపు సాధనం జోడించండి
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ఒక డైనమిక్ గ్రీటింగ్ వనరు జోడించండి
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

// stdin నుండి సందేశాలు స్వీకరించడం ప్రారంభించి stdout లో సందేశాలు పంపండి

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

# ఒక MCP సర్వర్ సృష్టించండి
mcp = FastMCP("Demo")


# ఒక సాకల్య సాధనం జోడించండి
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ఒక డైనమిక్ శుభాకాంక్ష వనరును జోడించండి
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

ఈ ప్రాజెక్ట్ చూసి మీరు [ప్రాంప్ట్‌లు మరియు వనరులు ఎలా జోడించాలో](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) తెలుసుకోండి.

ఇంకా, ఈ లింక్‌లో [ప్రాంప్ట్‌లు మరియు వనరులను ఎలా ఆహ్వానించాలో](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) తెలుసుకోండి.

### Rust

[ముందటి భాగంలో](../../../../03-GettingStarted/01-first-server), మీరు రస్ట్‌తో సరళమైన MCP సర్వర్‌ను ఎలా సృష్టించాలో నేర్చుకున్నారు. దీని పై కొనసాగించవచ్చు లేదా మరిన్ని రస్ట్ MCP సర్వర్ ఉదాహరణల కోసం ఈ లింక్ చూడండి: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## పరిష్కారం

**సొల్యూషన్ ఫోల్డర్** పూర్తి, నడపడానికి సిద్ధంగా ఉన్న క్లయింట్ అమలు ఉదాహరణలను కలిగి ఉంటుంది, ఈ ట్యూటోరియల్‌లో కవర్ చేసిన అన్ని కాన్సెప్టులను ప్రదర్శిస్తుంది. ప్రతి సొల్యూషన్‌లో రెండు ప్రాజెక్టులు ఉంటాయి: క్లయింట్ మరియు సర్వర్ కోడ్ వేర్వేరు, స్వతంత్ర ప్రాజెక్టులుగా ఉన్నవి.

### 📁 సొల్యూషన్ నిర్మాణం

సొల్యూషన్ డైరెక్టరీ ప్రోగ్రామింగ్ భాష ప్రకారం అలానే అమర్చబడింది:

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

### 🚀 ప్రతి సొల్యూషన్‌లో ఏముంది

ప్రతి భాషా నిర్దిష్ట సొల్యూషన్ అందిస్తుంది:

- ట్యూటోరియల్ లోని అన్ని ఫీచర్లతో మొత్తం క్లయింట్ అమలు
- సరైన డిపెండెన్సీలుతో ప్రాజెక్ట్ నిర్మాణం
- సులభంగా అమలు కోసం బిల్డ్ మరియు నడిపే స్క్రిప్ట్‌లు
- భాషా-నిర్దిష్ట README వివరాలు
- లోపాల నిర్వహణ మరియు ఫలిత ప్రాసెసింగ్ ఉదాహరణలు

### 📖 సొల్యూషన్‌లను ఉపయోగించడం

1. మీ ఇష్టమైన భాషా ఫోల్డర్‌కు వెళ్ళండి:

   ```bash
   cd solution/typescript/    # టైప్‌స్క్రిప్ట్ కోసం
   cd solution/java/          # జావా కోసం
   cd solution/python/        # పైథాన్ కోసం
   cd solution/dotnet/        # డాట్‌నెట్ కోసం
   ```

2. ప్రతి ఫోల్డర్‌లో README అనుసరించండి:
   - డిపెండెన్సీలు ఇన్స్టాల్ చేయడం
   - ప్రాజెక్ట్‌ను బిల్డ్ చేయడం
   - క్లయింట్ నడపడం

3. మీరు చూడవలసిన ఉదాహరణ అవుట్‌పుట్:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

సంపూర్ణ డాక్యుమెంటేషన్ మరియు దశల వారీ సూచనలు కోసం, చూడండి: **[📖 Solution Documentation](./solution/README.md)**

## 🎯 పూర్తి ఉదాహరణలు

మేము ఈ ట్యూటోరియల్‌లో తెలిపిన అన్ని ప్రోగ్రామింగ్ భాషల కోసం పూర్తి, నడిచే క్లయింట్ అమలు ఉదాహరణలను అందించాము. ఈ ఉదాహరణలు పూర్తిగా పై ఫంక్షనలిటీని ప్రదర్శిస్తాయి మరియు మీ స్వంత ప్రాజెక్టుల కోసం సూచనా అమలు లేదా ప్రారంభ పాయింట్లుగా ఉపయోగించవచ్చు.

### అందుబాటులో ఉన్న పూర్తి ఉదాహరణలు

| భాష | ఫైల్ | వివరణ |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ట్రాన్స్‌పోర్ట్ ఉపయోగించి పూర్తి జావా క్లయింట్, సంపూర్ణ లోపాల నిర్వహణతో |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ట్రాన్స్‌పోర్ట్ తో పూర్తి C# క్లయింట్, ఆటో సర్వర్ స్టార్టప్ తో |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | పూర్తి MCP ప్రోటోకాల్ మద్దతుతో TypeScript క్లయింట్ |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await నమూనాలు ఉపయోగించే పూర్తి Python క్లయింట్ |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | టోకియో ఉపయోగించి అసంక్రోనస్ ఆపరేషన్లకు పూర్తి Rust క్లయింట్ |

ప్రతి పూర్తి ఉదాహరణ:


- ✅ **కనెక్షన్ స్థాపన** మరియు లోపాల నిర్వహణ  
- ✅ **సర్వర్ అన్వేషణ** (ఉపకరణాలు, వనరులు, అవసరమైతే ప్రాంప్ట్‌లు)  
- ✅ **క్యాలిక్యులేటర్ ఆపరేషన్లు** (జోడించు, తీసివేయు, గుణించు, భాగించు, సహాయం)  
- ✅ **ఫలితాల ప్రాసెసింగ్** మరియు ఫార్మాటెడ్ అవుట్పుట్  
- ✅ **విషదమైన లోపాల నిర్వహణ**  
- ✅ **శుభ్రమైన, డాక్యుమెంటెడ్ కోడ్** స్థాయి స్థాయిగా వ్యాఖ్యలను కలిగి ఉంటుంది  

### పూర్తి ఉదాహరణలతో ప్రారంభించడం

1. **పై పట్టికలో నుండి మీ ఇష్టమైన భాషను ఎంచుకోండి**  
2. **పూర్తి ఉదాహరణ ఫైల్‌ని సమీక్షించండి** పూర్తి అమలును అర్థం చేసుకోవడానికి  
3. **[`complete_examples.md`](./complete_examples.md) లోని సూచనల ప్రకారం ఉదాహరణను నడపండి**  
4. **మీ నిర్దిష్ట వినియోగానికి ఉదాహరణను మార్చి విస్తరించండి**  

వివరణాత్మక డాక్యుమెంటేషన్ కోసం మరియు ఈ ఉదాహరణలను ఎలా నడపాలో తెలుసుకోడానికి చూడండి: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 పరిష్కారం vs. పూర్తి ఉదాహరణలు

| **పరిష్కారం ఫోల్డర్** | **పూర్తి ఉదాహరణలు** |
|--------------------|--------------------- |
| నిర్మాణ ఫైళ్లు కలిగిన పూర్తి ప్రాజెక్ట్ నిర్మాణం | సింగిల్-ఫైల్ అమలులు |
| డిపెండెన్సీలతో వెంటనే నడిపించడానికి సన్నద్దం | లక్ష్యంగా ఉండే కోడ్ ఉదాహరణలు |
| ఉత్పత్తి-రకమైన సెటప్ | విద్యా సూచన/reference |
| భాషాపై ప్రత్యేకమైన సాధనాలు | భాషల మధ్య సరిపోలిక |

ఈ రెండు విధానాలు విలువైనవి - పూర్తి ప్రాజెక్ట్‌ల కోసం **పరిష్కారం ఫోల్డర్** ను మరియు అభ్యాసం మరియు సూచన కోసం **పూర్తి ఉదాహరణలు** ను ఉపయోగించండి.

## ముఖ్య బిందువులు

ఈ అధ్యాయం యొక్క ముఖ్య బిందువులు క్లయింట్ల గురించి:

- సర్వర్‌లో ఫీచర్లను కనుగొనడంలో మరియు వాటిని పిలవడంలో ఉపయోగించవచ్చు.  
- ఈ అధ్యాయంలో వివరించినట్టు, క్లయింట్లు తమను తాము ప్రారంభించేటప్పుడు సర్వర్‌ను కూడా ప్రారంభించగలవు, అయితే క్లయింట్లు ఇప్పటికే నడుస్తున్న సర్వర్లకు కూడా కనెక్ట్ అవ్వచ్చు.  
- గత అధ్యాయంలో వివరించిన ఇన్స్పెక్టర్ వంటి ప్రత్యామ్నాయాలతో పాటు సర్వర్ సామర్థ్యాలను పరీక్షించడానికి అద్భుతమైన మార్గం.  

## అదనపు వనరులు

- [MCP లో క్లయింట్లు నిర్మాణం](https://modelcontextprotocol.io/quickstart/client)  

## నమూనాలు

- [జావా క్యాలిక్యులేటర్](../samples/java/calculator/README.md)  
- [.Net క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/csharp)  
- [జావాస్రిప్ట్ క్యాలిక్యులేటర్](../samples/javascript/README.md)  
- [టైప్స్క్రిప్ట్ క్యాలిక్యులేటర్](../samples/typescript/README.md)  
- [పైథాన్ క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/python)  
- [రస్ట్ క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/rust)  

## తరువాత ఏముంది

- తరువాత: [LLM తో క్లయింట్ సృష్టి](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**న Zhongతిక యాజ్ఞాపన**:
ఈ డాక్యుమెంట్ [Co-op Translator](https://github.com/Azure/co-op-translator) అనే AI అనువాద సేవ ద్వారా అనువదించబడింది. మనం ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, స్వయంచాలక అనువాదాలలో పొరపాటులు లేదా తప్పులుండే అవకాశం ఉంటుంది. ఒరిజినల్ డాక్యుమెంట్ దాని స్థానిక భాషలో ఉండే ప్రభావవంతమైన మూలంగా పరిగణించాలి. అత్యవసర సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాద సేవ అవసరం. ఈ అనువాదం ఉపయోగంతో కలగనున్న ఏవైనా అపార్థాలు లేదా తప్పుల కోసం మేము బాధ్యురాలు కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->