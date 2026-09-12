# క్లయింట్ సృష్టించడం

క్లయింట్లు అనేవి MCP సర్వర్‌తో నేరుగా కమ్యూనికేట్ చేసే ప్రత్యేక అనువర్తనాలు లేదా స్క్రిప్ట్‌లు, ఇవి వనరులు, టూల్స్ మరియు ప్రాంప్ట్‌లను అభ్యర్థిస్తాయి. సర్వర్‌తో ముచ్చటించడానికి గ్రాఫికల్ ఇంటర్ఫేస్ అందించే ఇన్స్పెక్టర్ టూల్ ఉపయోగించడంనుంచి భిన్నంగా, స్వీయ క్లయింట్ రాయడం ప్రోగ్రామేటిక్ మరియు ఆటోమేటెడ్ ఇంటరాక్షన్లను అనుమతిస్తుంది. ఇది డెవలపర్లకి తమ స్వంత వర్క్‌ఫ్లోలలో MCP సామర్థ్యాలను ఏకీకరించడానికి, పనులను ఆటోమేట్ చేసుకోవడానికి మరియు ప్రత్యేక అవసరాలకు అనుగుణంగా అనుకూల పరిష్కారాలను నిర్మించడానికి సహాయపడుతుంది.

## సమీక్ష

ఈ పాఠం Model Context Protocol (MCP) వ్యవస్థలో క్లయింట్ల అనే కన్సెప్ట్‌ను పరిచయం చేస్తుంది. మీరు మీ స్వంత క్లయింట్‌ను ఎలా రాయాలో, దానిని MCP సర్వర్‌కు ఎలా కనెక్ట్ చేయాలో నేర్చుకుంటారు.

## నేర్చుకోవాల్సిన లక్ష్యాలు

ఈ పాఠం ముగిసే సమయానికి, మీరు సాధించగలుగుతారు:

- ఒక క్లయింట్ ఏం చేయగలదో అర్ధం చేసుకోవడం.
- మీ స్వంత క్లయింట్‌ను రాయడం.
- క్లయింట్‌ను MCP సర్వర్‌తో కనెక్ట్ చేసి పరీక్షించడం, తద్వారా సర్వర్ ప్రతీక్షించినట్లుగా పనిచేస్తున్నదని నిర్ధారించడం.

## క్లయింట్ రాయడంలో ఏమి అవసరం?

క్లయింట్ రాయడానికి మీరు ఈ క్రింది పనులు చేయాలి:

- **సరైన లైబ్రరీలను దిగుమతి చేయండి**. మీరు ముందే ఉపయోగించిన లైబ్రరీతో పాటు వేర్వేరు నిర్మాణాలు ఉపయోగిస్తారు.
- **క్లయింట్‌ను ఉదాహరించండి**. దీంట్లో క్లయింట్ ఇన్‌స్టాన్స్ సృష్టించడం మరియు ఎంచుకున్న ట్రాన్స్‌పోర్ట్ పద్ధతితో కనెక్ట్ చేయడం ఉంటాయి.
- **ఏ వనరులు జాబితా చేయాలో నిర్ణయించండి**. మీ MCP సర్వర్ వనరులు, టూల్స్ మరియు ప్రాంప్ట్‌లు కలిగి ఉంటాయి, మీరు వాటిలో ఏది జాబితా చేయాలో నిర్ణయించాలి.
- **క్లయింట్‌ను హోస్ట్ అనువర్తనంతో ఏకీకృతం చేయండి**. సర్వర్ యొక్క సామర్థ్యాలను తెలిసిన తర్వాత, మీరు మీ హోస్ట్ అనువర్తనంలో దీనిని ఏకీకృతం చేయాలి, తద్వారా యూజర్ ప్రాంప్ట్ లేదా ఇతర ఆదేశాలు టైపు చేసినప్పుడు సంబంధిత సర్వర్ ఫీచర్ పిలవబడుతుంది.

ఇప్పుడు మనం ఏం చేయబోతున్నామో హై లెవల్‌గా అర్థం చేసుకున్న తరువాత, మేము ఒక ఉదాహరణను చూద్దాం.

### ఒక ఉదాహరణ క్లయింట్

ఈ ఉదాహరణ క్లయింట్ను చూద్దాం:

### టైప్‌స్క్రిప్ట్

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

// ప్రాంప్ట్‌లను జాబితా చేయండి
const prompts = await client.listPrompts();

// ఒక ప్రాంప్ట్ పొందండి
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// వనరులను జాబితా చేయండి
const resources = await client.listResources();

// ఒక వనరును చదవండి
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ఒక సాధనాన్ని కాల్ చేయండి
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

పూర్వపు కోడ్‌లో మేము:

- లైబ్రరీలను దిగుమతి చేసుకుంటాం
- క్లయింట్ ఇన్‌స్టాన్స్ సృష్టించి, stdio ద్వారా ట్రాన్స్‌పోర్ట్ విధానంగా కనెక్ట్ చేస్తాం
- ప్రాంప్ట్‌లు, వనరులు మరియు టూల్స్ జాబితా చేసి వాటిని అందరికీ పిలుస్తాం

ఇక్కడ మీరు చూస్తున్నది, MCP సర్వర్‌తో మాట్లాడగలిగే క్లయింట్.

తదుపరి వ్యాయామ విభాగంలో ప్రతీ కోడ్ స్నిపెట్‌ను విశ్లేషించి వివరిస్తాము.

## వ్యాయామం: క్లయింట్ రాయడం

పైగా చెప్పినట్లుగా, కోడ్‌ని వివరించడంలో మనం సమయం తీసుకుందాం, కావాల్సినంత కోడ్ కూడా రాయండి.

### -1- లైబ్రరీలను దిగుమతి చేయడం

మనకు కావలసిన లైబ్రరీలను దిగుమతి చేద్దాం, మనకు క్లయింట్ మరియు stdio అనే ఉపయుక్త ట్రాన్స్‌పోర్ట్ ప్రోటోకాల్కు రిఫరెన్స్‌లు కావలసి ఉంటుంది. stdio అనేది మీ స్థానిక యంత్రంలో నడిచే పద్ధతుల కోసం ప్రోటోకాల్. SSE మరొక ట్రాన్స్‌పోర్ట్ ప్రోటోకాల్, దీన్ని భవిష్యత్ అధ్యాయాల్లో చూపించబోతున్నాం, అది మీకు మరో ఎంపిక. ప్రస్తుతం stdio తో కొనసాగుదాం.

#### టైప్‌స్క్రిప్ట్

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### పైథాన్

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

#### జావా

జావా కోసం, మీరు గత వ్యాయామం నుండి MCP సర్వర్‌కు కనెక్ట్ చేసే క్లయింట్ సృష్టిస్తారు. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) నుండి అందిన జావా స్ప్రింగ్ బూట్ ప్రాజెక్ట్ నిర్మాణాన్నే ఉపయోగించి, `SDKClient` అనే కొత్త జావా తరగతిని `src/main/java/com/microsoft/mcp/sample/client/` ఫోల్డర్లో సృష్టించి క్రింది దిగుమతులను జోడించండి:

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

#### రస్ట్

మీరు మీ `Cargo.toml` ఫైల్‌కు క్రింది డిపెండెన్సీలను జోడించాలి.

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

ఆ తర్వాత, మీరు మీ క్లయింట్ కోడ్‌లో అవసరమైన లైబ్రరీలను దిగుమతి చేసుకోవచ్చు.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ఇప్పుడు ఇన్‌స్టాన్షియేషన్ దిశగా పోదాం.

### -2- క్లయింట్ మరియు ట్రాన్స్‌పోర్ట్ ఇన్‌స్టాన్షియేషన్

మనం ట్రాన్స్‌పోర్ట్ మరియు క్లయింట్ ఇన్‌స్టాన్స్‌ని సృష్టించాలి:

#### టైప్‌స్క్రిప్ట్

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

పూర్వపు కోడ్‌లో మనం:

- stdio ట్రాన్స్‌పోర్ట్ ఇన్‌స్టాన్స్ సృష్టించాము. ఇది సర్వర్‌ను ఎలా కనుగొని ప్రారంభించాలో వివరించడానికి కమాండ్ మరియు ఆర్గ్యుమెంట్స్ పేర్కొంటుంది, దానిని క్లయింట్ తయారు చేసేటప్పుడు అవసరం.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- క్లయింట్ ను ఒక పేరుతో మరియు వెర్షన్ తో ఇన్‌స్టాన్షియేట్ చేయడంతో పూర్తయ్యింది.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- క్లయింట్ ను ఎంచుకున్న ట్రాన్స్‌పోర్ట్ కి కనెక్ట్ చేయబడింది.

    ```typescript
    await client.connect(transport);
    ```

#### పైథాన్

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio కనెక్షన్ కోసం సర్వర్ పారామితులను సృష్టించండి
server_params = StdioServerParameters(
    command="mcp",  # అమలు చేయదగినది
    args=["run", "server.py"],  # ఐచ్ఛిక ఆదేశ రేఖా ఆర్గ్యుమెంట్లు
    env=None,  # ఐచ్ఛిక పర్యావరణ చరాలు
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # కనెక్షన్‌ను Inicialize చేయండి
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

పూర్వపు కోడ్‌లో మనం:

- కావాల్సిన లైబ్రరీలను దిగుమతి చేసుకున్నాం
- సర్వర్ పరిమితుల ఆబ్జెక్ట్ సృష్టించాం, దీన్ని మనం సర్వర్ నడపడానికి ఉపయోగించబోతున్నాం తద్వారా మన క్లయింట్ అందుకి కనెక్ట్ కావచ్చు
- `run` అనే పద్ధతిని నిర్వచించాం, ఇది `stdio_client`ని పిలుస్తుంది, ఇది క్లయింట్ సెషన్ ప్రారంభిస్తుంది
- `asyncio.run`కు `run` మెథడ్‌ను అందించే ఎంట్రీ పాయింట్ సృష్టించాం

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

పూర్వపు కోడ్‌లో మనం:

- కావాల్సిన లైబ్రరీలను దిగుమతి చేసుకున్నాం.
- stdio ట్రాన్స్‌పోర్ట్ సృష్టించి `mcpClient` అనే క్లయింట్ క్రియేట్ చేసాము. ఇది MCP సర్వర్‌పై ఫీచర్ల జాబితా చేయడానికి మరియు పిలవడానికి ఉపయోగిస్తారు.

గమనిక: "Arguments"లో మీరు *.csproj* లేదా ఎజిక్యూటబుల్‌కి పాయింట్ చేయవచ్చు.

#### జావా

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
        
        // మీ క్లయింట్ లాజిక్ ఇక్కడ ఉంటుంది
    }
}
```

పూర్వపు కోడ్‌లో మనం:

- `http://localhost:8080`కు పాయింట్ చేసే SSE ట్రాన్స్‌పోర్ట్ సృష్టించే మెయిన్ మెథడ్ తయారు చేసాము, అక్కడ మన MCP సర్వర్ నడుస్తుంది.
- ట్రాన్స్‌పోర్ట్‌ను కన్స్ట్రక్టర్ పారామీటర్‌గా తీసుకునే క్లయింట్ క్లాస్ సృష్టించాం.
- `run` మెథడ్‌లో, మనము ట్రాన్స్‌పోర్ట్ ఉపయోగించి సింక్రోనస్ MCP క్లయింట్ తయారు చేసి కనెక్షన్ ప్రారంభించాము.
- Java Spring Boot MCP సర్వర్‌లకు అనువైన HTTP ఆధారిత కమ్యూనికేషన్ కోసం SSE (సర్వర్-సెంట్ ఈవెంట్స్) ట్రాన్స్‌పోర్ట్ ఉపయోగించాము.

#### రస్ట్

ఈ రస్ట్ క్లయింట్ సర్వర్‌ను అదే డైరెక్టరీలో ఉన్న "calculator-server" అనే సిబ్లింగ్ ప్రాజెక్ట్‌గా భావిస్తుంది. క్రింది కోడ్ సర్వర్‌ను వీడియో చేసి దానికి కనెక్ట్ అవుతుంది.

```rust
async fn main() -> Result<(), RmcpError> {
    // సర్వర్ అదే డైరెక్టరీలో "calculator-server" అనే సిబ్లింగ్ ప్రాజెక్ట్ అని అనుకోండి
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

    // చేయాల్సింది: ప్రారంభించండి

    // చేయాల్సింది: సాధనాలను జాబితా చేయండి

    // చేయాల్సింది: ఆర్గ్యుమెంట్స్ = {"a": 3, "b": 2}తో add సాధనాన్ని పిలవండి

    client.cancel().await?;
    Ok(())
}
```

### -3- సర్వర్ ఫీచర్ల జాబితా

ఇప్పుడు మనకు ఒక క్లయింట్ ఉంది, దీన్ని ప్రోగ్రామ్ ఓడినప్పుడు కనెక్ట్ అయిపోతుంది. అయితే, ఇది దాని ఫీచర్లను జాబితా చేయదు, కాబట్టి తదుపరి మనం అది చేయాలి:

#### టైప్‌స్క్రిప్ట్

```typescript
// ప్రాంప్ట్‌ల జాబితా
const prompts = await client.listPrompts();

// వనరుల జాబితా
const resources = await client.listResources();

// పరికరాల జాబితా
const tools = await client.listTools();
```

#### పైథాన్

```python
# అందుబాటులో ఉన్న వనరులను జాబితా చేయండి
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# అందుబాటులో ఉన్న సాధనాలను జాబితా చేయండి
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ఇక్కడ మనం అందుబాటులో ఉన్న వనరులు, `list_resources()` మరియు టూల్స్, `list_tools`ను జాబితా చేసి, వాటిని ప్రింట్ చేస్తున్నాము.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

పై ఉదాహరణలో మనం సర్వర్ టూల్స్ జాబితా చేసే విధానం చూపించారు. ప్రతి టూల్ కోసం, దాని పేరు ప్రింట్ చేయబడుతుంది.

#### జావా

```java
// ఆపరేటింగ్ టూల్స్ మరియు డెమోన్ట్రేట్ జాబితా
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// మీరు కనెక్షన్‌ని నిర్ధారించడానికి సర్వర్‌ను పింగ్ కూడా చేయవచ్చు
client.ping();
```

పూర్వపు కోడ్‌లో మనం:

- MCP సర్వర్ నుండి అందుబాటులో ఉన్న అన్ని టూల్స్‌ను పొందడానికి `listTools()` పిలిచాము.
- కనెక్షన్ పని చేస్తున్నదని ధృవీకరించడానికి `ping()` వాడాము.
- `ListToolsResult`లో అన్ని టూల్స్ పేరు, వివరణలు మరియు ఇన్పుట్ స్కీమాలు ఉన్నాయి.

చక్కగా, ఇప్పుడు మనం అన్ని ఫీచర్లను క్యాప్చర్ చేసాము. ఇప్పుడు ప్రశ్న ఏమిటంటే వాటిని ఎప్పుడు ఉపయోగించాలి? ఈ క్లయింట్ చాలా సింపల్‌గా ఉంది, అంటే మనం వాటిని స్పష్టంగా పిలవాల్సి ఉంటుంది. తరువాత అధ్యాయం లో, మనం ఒక అధునాతన క్లయింట్ సృష్టించబోతున్నాం, దీనికి స్వంత LLM ఉంది. ప్రస్తుతం, సర్వర్ ఫీచర్లను ఎలా పిలవాలో చూద్దాం:

#### రస్ట్

మైన్ ఫంక్షన్ లో, క్లయింట్‌ను ఇనిషియలైజ్ చేసిన తర్వాత, మనం సర్వర్‌ను ఇనిషియలైజ్ చేసి కొంత ఫీచర్లను జాబితా చేయవచ్చు.

```rust
// ప్రారంభించండి
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// టూల్స్ జాబితా
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ఫీచర్లను పిలవడం

ఫీచర్లను పిలవడానికి సరైన ఆర్గ్యుమెంట్స్ ను మరియు కొన్ని సందర్భాల్లో పిలవాలనుకునే విషయం పేరు ను స్పష్టంగా చెప్పడం అవసరం.

#### టైప్‌స్క్రిప్ట్

```typescript

// ఒక వనరును చదవండి
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ఒక పరికరాన్ని పిలవండి
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// ప్రాంప్ట్‌ను పిలవండి
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

పూర్వపు కోడ్‌లో మనం:

- వనరును చదివాము, `readResource()`ని `uri`తో పిలిచాము. ఇది సర్వర్ పక్కన ఇలా ఉండవచ్చు:

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

    మన `uri` విలువ `file://example.txt` సర్వర్ పక్కన ఉన్న `file://{name}` కి సరిపోతుంది. `example.txt` `name`కి మ్యాప్ అవుతుంది.

- టూల్ పిలవడం, దాని `name` మరియు `arguments`ని ఇలా స్పష్టంచేసి పిలుస్తాం:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- ప్రాంప్ట్ గెట్ చేయడం, మీరు `getPrompt()`ని `name` మరియు `arguments`తో పిలుస్తారు. సర్వర్ కోడ్ ఇలా ఉంటుంది:

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

    మరియు ఫలితంగా మీ క్లయింట్ కోడ్ ఇలా ఉంటుంది, సర్వర్‌లో ప్రకటించినదానికి సరిపోల్చి:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### పైథాన్

```python
# ఒక వనరును చదవండి
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ఒక పరికరాన్ని పిలవండి
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

పూర్వపు కోడ్‌లో మనం:

- `greeting` అనే వనరును `read_resource`తో పిలవడం.
- `add` అనే టూల్‌ను `call_tool`తో పిలవడం.

#### .NET

1. టూల్ పిలవడానికి కొంత కోడ్ జోడిద్దాం:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ఫలితాన్ని ప్రింట్ చేయడానికి దీని కొంత కోడ్:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### జావా

```java
// వివిధ క్యాల్క్యులేటర్ పరికరాలను కాల్ చేయండి
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

పూర్వపు కోడ్‌లో మనం:

- బహుళ క్యాలిక్యులేటర్ టూల్స్‌ను `callTool()` మెథడ్‌తో `CallToolRequest` ఆబ్జెక్ట్స్ సహాయంతో పిలిచాము.
- ప్రతి టూల్ కాల్ టూల్ పేరు మరియు ఆ టూల్ అవసరమైన ఆర్గ్యుమెంట్స్ `Map` specifies చేస్తుంది.
- సర్వర్ టూల్స్ కొన్ని స్పెసిఫిక్ పేరామీటర్లు (ఉదాహరణకు "a", "b" గణిత నిర్వహణలకు) ఆశిస్తాయి.
- ఫలితాలు `CallToolResult` ఆబ్జెక్ట్స్‌గా వస్తాయి, ఇవి సర్వర్ నుండి వచ్చిన రెస్పాన్స్‌ను కలిగి ఉంటాయి.

#### రస్ట్

```rust
// ఆర్గ్యుమెంట్స్ = {"a": 3, "b": 2} తో add టూల్‌ను కాల్ చేయండి
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

### -5- క్లయింట్ నడపడం

క్లయింట్‌ను నడిపేందుకు, టెర్మినల్‌లో క్రింద కనిపించే ఆదేశాన్ని టైప్ చేయండి:

#### టైప్‌స్క్రిప్ట్

మీ *package.json* లో "scripts" సెక్షన్లో క్రింది ఎంట్రీని జోడించండి:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### పైథాన్

క్లయింట్‌ను ఈ ఆదేశంతో పిలవండి:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### జావా

ముందుగా, మీరు MCP సర్వర్ `http://localhost:8080`లో నడుస్తున్నదని నిర్ధారించండి. ఆ తరువాత క్లయింట్ ని నడపండి:

```bash
# మీ ప్రాజెక్ట్‌ను నిర్మించండి
./mvnw clean compile

# క్లయింట్‌ను నడపండి
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

లేదా, మీరు సొల్యూషన్ ఫోల్డర్ `03-GettingStarted\02-client\solution\java`లో అందిన కంప్లీట్ క్లయింట్ ప్రాజెక్ట్‌ను నడపవచ్చు:

```bash
# సొల్యూషన్ డైరెక్టరీకి నావిగేట్ చేయండి
cd 03-GettingStarted/02-client/solution/java

# JARని బిల్డ్ చేయండి మరియు రన్ చేయండి
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### రస్ట్

```bash
cargo fmt
cargo run
```

## అసైన్‌మెంట్

ఈ అసైన్‌మెంట్‌లో, మీరు క్లయింట్ సృష్టించడంలో నేరించిన దాన్ని ఉపయోగించి, మీ స్వంత క్లయింట్‌ను సృష్టించాలి.

మీరు ఉపయోగించగల సర్వర్ ఇది, దీన్ని మీరు మీ క్లయింట్ కోడ్ ద్వారా పిలవాలి, మరిన్ని ఫీచర్లు జోడించి మరింత ఆసక్తికరంగా చేస్తారా చూడండి.

### టైప్‌స్క్రిప్ట్

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ఒక MCP సర్వర్ సృష్టించండి
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

// stdin పై సందేశాలు స్వీకరించడం ప్రారంభించి stdout పై సందేశాలు పంపించడం ప్రారంభించండి

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

### పైథాన్

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ఒక MCP సర్వర్‌ను సృష్టించండి
mcp = FastMCP("Demo")


# ఒక జోడింపు సాధనాన్ని చేర్చండి
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ఒక డైనమిక్ గ్రీటింగ్ రిసోర్స్ను చేర్చండి
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

ఈ ప్రాజెక్ట్‌ను చూసి ఎలా [ప్రాంప్ట్‌లు మరియు వనరులు జోడించాలో](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) తెలుసుకోండి.

అలాగే ఈ లింక్ ద్వారా [ప్రాంప్ట్‌లు మరియు వనరులు పిలవడం](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) ఎలా చేయాలో చూడండి.

### రస్ట్

[ముందటి సెక్షన్](../../../../03-GettingStarted/01-first-server)లో, మీరు రస్ట్‌తో సాదా MCP సర్వర్ ఎలా సృష్టించాలో నేర్చుకున్నారు. మీరు దీన్ని కొనసాగించి నిర్మించవచ్చు లేదా ఈ లింక్ ద్వారా మరిన్ని రస్ట్ ఆధారిత MCP సర్వర్ ఉదాహరణలను చూడండి: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## పరిష్కారం

**సొల్యూషన్ ఫోల్డర్** పూర్తిగా, నడిపే తయారైన క్లయింట్ అమలు విధానాలను కలిగి ఉంటుంది, ఇవి ఈ ట్యుటోరియల్‌లో చదివిన అన్ని కాన్సెప్టులను చూపిస్తాయి. ప్రతి సొల్యూషన్‌లో క్లయింట్ మరియు సర్వర్ కోడ్ వేరే వేరే స్వతంత్ర ప్రాజెక్టులుగా ఏర్పాటు చేసినవి.

### 📁 సొల్యూషన్ నిర్మాణం

సొల్యూషన్ డైరెక్టరీ ప్రోగ్రామింగ్ భాషల ఆధారంగా విభజించబడింది:

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

### 🚀 ప్రతి సొల్యూషన్‌లో ఏమి ఉంటుంది

ప్రతి భాషకు ప్రత్యేక సొల్యూషన్ అందిస్తుంది:

- **పూర్తి క్లయింట్ అమలు** ట్యుటోరియల్‌లోని అన్ని ఫీచర్లతో
- **సక్రమమైన ప్రాజెక్ట్ నిర్మాణం** సరైన డిపెండెన్సీలు మరియు కాన్ఫిగరేషన్‌తో
- **సవరించి నడపడానికి స్ర్కిప్టులు** సులభమైన సెటప్ మరియు అమలుకు
- **వివరణాత్మక README** భాషా-స్పెసిఫిక్ సూచనలతో
- **ఎర్రర్ హ్యాండ్లింగ్** మరియు ఫలితాలు ప్రాసెసింగ్ ఉదాహరణలు

### 📖 సొల్యూషన్ల ఉపయోగము

1. **మీ ఇష్టమైన భాష ఫోల్డరకు నావిగేట్ అవ్వండి**:

   ```bash
   cd solution/typescript/    # టైప్స్క్రిప్ట్ కోసం
   cd solution/java/          # జావా కోసం
   cd solution/python/        # పైథాన్ కోసం
   cd solution/dotnet/        # .NET కోసం
   ```

2. **ప్రతి ఫోల్డర్లో README సూచనల్ని పాటించండి**:
   - డిపెండెన్సీలు ఇన్స్‌టాల్ చేయడం
   - ప్రాజెక్ట్ నిర్మించడం
   - క్లయింట్ నడపడం

3. **మూసలం అవుట్‌పుట్ ఉదాహరణ** ఇది ఉండాలి:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

పూర్తి డాక్యుమెంటేషన్ మరియు దశలవారీ సూచనలకు, చూడండి: **[📖 సొల్యూషన్ డాక్యుమెంటేషన్](./solution/README.md)**

## 🎯 పూర్తి ఉదాహరణలు

ఈ ట్యుటోరియల్‌లో చూచిన అన్ని ప్రోగ్రామింగ్ భాషల కోసం పూర్తి, పనిచేసే క్లయింట్ అమలు విధానాలు అందించబడ్డాయి. ఈ ఉదాహరణలు పై చెప్పిన అన్ని ఫంక్షనాలిటీలను చూపిస్తాయి మరియు మీ స్వంత ప్రాజెక్టుల కోసం రిఫరెన్స్ లేదా ప్రారంభ బిందువులుగా ఉపయోగించవచ్చు.

### అందుబాటులో ఉన్న పూర్తి ఉదాహరణలు

| భాష | ఫైల్ | వివరణ |
|----------|------|-------------|
| **జావా** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ట్రాన్స్‌పోర్ట్‌తో పూర్తి జావా క్లయింట్, విస్తృత ఎర్రర్ హ్యాండ్లింగ్‌తో |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ట్రాన్స్‌పోర్ట్ తో పూర్తి C# క్లయింట్, ఆటోమేటిక్ సర్వర్ స్టార్ట్‌తో |
| **టైప్‌స్క్రిప్ట్** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP ప్రోటోకాల్‌ను పూర్తి మద్దతు చేసే పూర్తి టైప్‌స్క్రిప్ట్ క్లయింట్ |
| **పైథాన్** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await నమూనాలతో పూర్తి పైథాన్ క్లయింట్ |
| **రస్ట్** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | అసంక్రమ కార్యకలాపాల కోసం Tokio ఉపయోగించే పూర్తి రస్ట్ క్లయింట్ |

ప్రతి పూర్తి ఉదాహరణలో ఉంటుంది:

- ✅ **కనెక్షన్ ఏర్పాట్లు** మరియు ఎర్రర్ హ్యాండ్లింగ్
- ✅ **సర్వర్ డిస్కవరీ** (టూల్స్, వనరులు, ప్రాంప్ట్‌లు ఉన్న చోట)
- ✅ **క్యాలిక్యులేటర్ ఆపరేషన్లు** (జోడించు, తీసివేయి, గుణించు, భాగించు, సహాయం)
- ✅ **ఫలితాల ప్రాసెసింగ్** మరియు ఫార్మాట్ చేయబడిన అవుట్‌పుట్
- ✅ **విస్తృతమైన ఎర్రర్ హ్యాండ్లింగ్**

- ✅ **శుభ్రంగా, డాక్యుమెంటులో ఉంచబడిన కోడ్** దశల వారీగా వ్యాఖ్యలతో

### పూర్తి ఉదాహరణలతో ప్రారంభించడం

1. పై పట్టికలో నుండి **మీ ఇష్టమైన భాషను ఎంచుకోండి**
2. **పూర్తి ఉదాహరణ ఫైల్‌ను సమీక్షించండి** పూర్తి అమలును అర్థం చేసుకోడానికి
3. [`complete_examples.md`](./complete_examples.md)లో ఉన్న సూచనలను అనుసరించి **ఉదాహరణను జరపండి**
4. **మీ ప్రత్యేక ఉపయోగ కేస్ కోసం ఉదాహరణను సవరించండి మరియు విస్తరించండి**

ఈ ఉదాహరణలను నడపడం మరియు అనుకూలీకరించడంపై విపులమైన డాక్యుమెంటేషన్ కోసం, చూడండి: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 పరిష్కారం vs. పూర్తి ఉదాహరణలు

| **పరిష్కార ఫోల్డర్** | **పూర్తి ఉదాహరణలు** |
|--------------------|--------------------- |
| బిల్డ్ ఫైల్‌లతో పూర్తి ప్రాజెక్ట్ నిర్మాణం | ఒక్కో ఫైల్ అమలు |
| ఆధారాలతో నడిపేందుకు సిద్ధంగా ఉంటుంది | కేంద్రీకృత కోడ్ ఉదాహరణలు |
| ఉత్పత్తి-లాగే సెటప్ | విద్యాసంరచనా ఉదాహరణ |
| భాషా-ప్రముఖ టూలింగ్ | భాషల మధ్య తులనాత్మక వివరాలూ |

రెండు పద్ధతులు విలువైనవి - పూర్తి ప్రాజెక్టులకి **పరిష్కార ఫోల్డర్**ను, నేర్చుకోవడం మరియు సూచనకి **పూర్తి ఉదాహరణలు**ని ఉపయోగించండి.

## ముఖ్యమైన పాఠాలు

ఈ అధ్యాయానికి సంబంధించిన క్లైయింట్లపై ముఖ్యమైన పాఠాలు:

- సర్వర్‌పై ఫీచర్లను కనుగొనటానికి మరియు పిలవడానికి ఉపయోగించవచ్చు.
- ఇది స్వయంగా ప్రారంభమయ్యే సర్వర్‌ను ప్రారంభించగలదు (ఈ అధ్యాయంలో లాగా), కానీ క్లైయింట్లు ఇప్పటికే నడుస్తున్న సర్వర్‌లకు కూడా కनेक్ట్ అవుతారు.
- ఇది అన్వేషణలో ఉన్న ఇతర ప్రత్యామ్నాయాలతో పాటు సర్దుబాటు ఫంక్షనాలిటీని పరీక్షించడానికి గొప్ప మార్గం, ఇది గత అధ్యాయంలో వివరించబడినట్లు.

## అదనపు వనరులు

- [MCPలో క్లైయింట్లను నిర్మించడం](https://modelcontextprotocol.io/quickstart/client)

## నమూనాలు

- [జావా క్యాలిక్యులేటర్](../samples/java/calculator/README.md)
- [.NET క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/csharp)
- [జావాస్క్రిప్ట్ క్యాలిక్యులేటర్](../samples/javascript/README.md)
- [టైప్స్క్రిప్ట్ క్యాలిక్యులేటర్](../samples/typescript/README.md)
- [పైథాన్ క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/python)
- [రస్ట్ క్యాలిక్యులేటర్](../../../../03-GettingStarted/samples/rust)

## తదుపరి ఏమిటి

- తదుపరి: [LLMతో క్లైయింట్ సృష్టించడం](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->