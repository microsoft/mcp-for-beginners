# ക്ലയന്റ് സൃഷ്ടിക്കല്‍

ക്ലയന്റുകള്‍ MCP സേര്‍വറുമായി നേരിട്ട് ആശയവിനിമയം നടത്തുന്നതിനുള്ള കസ്റ്റം അപ്ലിക്കേഷനുകള്‍ അല്ലെങ്കില്‍ സ്‌ക്രിപ്റ്റുകളാണ്, ഇത് റിസോഴ്‌സുകള്‍, ടൂളുകള്‍, പ്രോംപ്റ്റുകള്‍ ആവശ്യപ്പെടുന്നു. സെര്‍വറുമായി ആശയവിനിമയം നടത്തുന്നതിനുള്ള ഗ്രാഫിക്കല്‍ ഇന്റര്‍ഫേസ് നല്‍കുന്ന ഇന്‍സ്പെക്ടര്‍ ടൂള്‍ ഉപയോഗിക്കുന്നതിന് പകരം, നിങ്ങളുടെ സ്വന്തം ക്ലയന്റ് എഴുതുന്നത് പ്രോഗ്രാമാറ്റിക് ആണും ഓട്ടോമേറ്റഡ് ആശയവിനിമയത്തിനും അനുവദിക്കുന്നു. ഇത് ഡെവലപ്പര്‍മാര്‍ക്ക് MCP സവിശേഷതകള്‍ അവരുടെ സ്വന്തം വര്‍ക്‌ഫ്ലോകളിലേക്ക് സംയോജിപ്പിക്കാനും, ടാസ്‌കുകള്‍ ഓട്ടോമേറ്റ് ചെയ്യാനും, പ്രത്യേക ആവശ്യങ്ങള്‍ക്ക് അനുയോജ്യമായ കസ്റ്റം പരിഹാരങ്ങള്‍ നിര്‍മ്മിക്കാനുമുള്ള സാധ്യത നല്‍കുന്നു.

## അവലോകനം

ഈ പാഠത്തില്‍ മോഡല്‍ കോണ്‍ടെക്‌സ്്റ്റ് പ്രോട്ടോക്കോള്‍ (MCP) പരിസ്ഥിതിയിലെ ക്ലയന്റുകളുടെ ആശയം പരിചയപ്പെടാം. നിങ്ങളുടെ സ്വന്തം ക്ലയന്റ് എഴുതാനും അത് MCP സേര്‍വറുമായി ബന്ധിപ്പിക്കാനും നിങ്ങള്‍ എങ്ങനെ സാധിക്കും എന്നതും പഠിക്കും.

## പഠന ലക്ഷ്യങ്ങള്‍

ഈ പാഠം പൂര്‍ത്തിയാക്കുമ്പോൾ, നിങ്ങൾക്കാകും:

- ഒരു ക്ലയന്റ് എന്ത് ചെയ്യാമെന്നു മനസ്സിലാക്കുക.
- നിങ്ങളുടെ സ്വന്തം ക്ലയന്റ് എഴുതുക.
- ക്ലയന്റിനെ MCP സേര്‍വറുമായി ബന്ധിപ്പിച്ച് പരീക്ഷിച്ച്, അവസാനത്തേത് പ്രതീക്ഷിച്ചതുപോലെ പ്രവര്‍ത്തിക്കുന്നുവോയെന്ന് ഉറപ്പാക്കുക.

## ക്ലയന്റ് എഴുതുന്നതിലേക്ക് എന്തെല്ലാം വേണം?

ക്ലയന്റ് എഴുതാന്‍ നിങ്ങള്‍ ചെയ്യേണ്ടത്:

- **തീർച്ചയായ ലൈബ്രറികള്‍ ഇംപോര്‍ട്ട് ചെയ്യുക**. മുമ്പുള്ളതുപോലെ തന്നെ ലൈബ്രറി ഉപയോഗിച്ചുകൊണ്ടിരിക്കും, വെറും വ്യത്യസ്ത ഘടകം.
- **ക്ലയന്റ് ഘടിപ്പിക്കുക**. ഇതില്‍ ക്ലയന്റ് ഉദാഹരണം സൃഷ്ടിച്ച് തെരഞ്ഞെടുക്കപ്പെട്ട ട്രാന്‍സ്‌പോര്‍ട്ട് രീതിയിലേക്ക് ബന്ധിപ്പിക്കുന്നതാണ്.
- **എന്ത് റിസോഴ്‌സുകള്‍ പട്ടികപ്പെടുത്തണമെന്ന് തീരുമാനിക്കുക**. നിങ്ങളുടെ MCP സേര്‍വറിനു റിസോഴ്‌സുകള്‍, ടൂളുകള്‍, പ്രോംപ്റ്റുകള്‍ ഉണ്ട്, ഏതൊക്കെ പട്ടികപ്പെടുത്തുന്നുവെന്ന് തീരുമാനിക്കണം.
- **ക്ലയന്റ് ഹോസ്റ്റ് അപ്ലിക്കേഷനുമായി സംയോജിപ്പിക്കുക**. സേര്‍വറിന്റെ ശേഷികള്‍ അറിഞ്ഞപ്പോള്‍, ഉപയോക്താവ് പ്രോംപ്റ്റ് അല്ലെങ്കില്‍ മറ്റേതെങ്കിലും കമാൻഡ് ടൈപ്പ് ചെയ്‌താല്‍ അനുയോജ്യമായ സേര്‍വര്‍ ഫീച്ചർ ആരംഭിക്കുന്നതിനായി ഹോസ്റ്റ് അപ്ലിക്കേഷനിൽ ഇതെന്താക്കണം.

ഇപ്പോൾ എന്തു ചെയ്യാനുവെന്നാണ് ഉയർന്ന നിലയില്‍ മനസ്സിലാക്കിയത്, അടുത്തതായി ഒരു ഉദാഹരണം നോക്കാം.

### ഒരു ഉദാഹരണ ക്ലയന്റ്

ഈ ഉദാഹരണ ക്ലയന്റ് നോക്കാം:

### ടൈപ്പ്സ്ക്രിപ്റ്റ്

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

// പ്രോംപ്റ്റുകൾ പട്ടികപ്പെടുത്തുക
const prompts = await client.listPrompts();

// ഒരു പ്രോംപ്റ്റ് ലഭിക്കുക
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// സ്രോതസ്സുകൾ പട്ടികപ്പെടുത്തുക
const resources = await client.listResources();

// ഒരു സ്രോത് വായിക്കുക
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ഒരു ഉപകരണം വിളിക്കുക
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

മുമ്പുള്ള കോഡിൽ ഞങ്ങൾ:

- ലൈബ്രറികള്‍ ഇംപോര്‍ട്ട് ചെയ്തു
- ക്ലയന്റ് ഒരു ഉദാഹരണം സൃഷ്ടിച്ച് stdio ട്രാൻസ്പോര്‍ട്ട് ഉപയോഗിച്ച് ബന്ധിപ്പിച്ചു.
- പ്രോംപ്റ്റുകൾ, റിസോഴ്‌സുകൾ, ടൂളുകൾ പട്ടികപ്പെടുത്തി അവ എല്ലാം വിളിച്ചു.

ഇതാ, MCP സേര്‍വറുമായി സംസാരിക്കാവുന്ന ഒരു ക്ലയന്റ്.

അടുത്ത വ്യായാമ വിഭാഗത്തിൽ ഓരോ കോഡ് വിഭജികയും വിശദീകരിക്കപ്പെടും.

## വ്യായാമം: ഒരു ക്ലയന്റ് എഴുതല്‍

മുകളിൽ പറഞ്ഞത് പോലെ, കോഡ് വിശദീകരിക്കാനാണ് സമയം എടുത്തുകൊണ്ടിരിക്കുക, കൂടാതെ നിങ്ങൾക്ക് ആഗ്രഹമുണ്ടെങ്കിൽ കൂടെ കോഡ് ചെയ്യുക.

### -1- ലൈബ്രറികള്‍ ഇംപോർട്ട് ചെയ്യുക

നമുക്ക് വേണ്ട ലൈബ്രറികൾ ഇമ്പോര്‍ട്ട് ചെയ്യാം, ഒരു ക്ലയന്റിനും തിരഞ്ഞെടുത്ത ട്രാൻസ്പോര്‍ട്ട് പ്രോട്ടോക്കോള്‍ stdio നും റഫറന്‍സുകള്‍ വേണം. stdio നിങ്ങളുടെ ലൊക്കല്‍ മെഷീനില്‍ ഓടുന്നവയ്ക്കുള്ള പ്രോട്ടോക്കോള്‍ ആണ്. SSE മറ്റൊരു ട്രാൻസ്പോർട്ട് പ്രോട്ടോക്കോള്‍ ആയി ഭാവിയില്‍ നമ്മൽ കാണിക്കും, പക്ഷേ ഇപ്പോള്‍ stdio കൊണ്ടുതുടരാം.

#### ടൈപ്പ്സ്ക്രിപ്റ്റ്

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### പൈതൺ

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

#### ജാവ

ജാവയില്‍, മുമ്പ് ഉപയോഗിച്ച MCP സേര്‍വറുമായി ബന്ധിപ്പിക്കുന്ന ഒരു ക്ലയന്റ് സൃഷ്ടിക്കും. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) എന്ന ജാവ സ്പ്രിംഗ് ബൂട്ട് പ്രോജക്ട് ഘടന ഉപയോഗിച്ച് `src/main/java/com/microsoft/mcp/sample/client/` ഫോൾഡറിൽ `SDKClient` എന്ന പുതിയ ക്ലാസ്സ് സൃഷ്ടിച്ച് താഴെ കാണുന്ന ഇമ്പോർട്ടുകള്‍ ചേർക്കുക:

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

#### റസ്റ്റ്

നിങ്ങളുടെ `Cargo.toml` ഫയലിൽ താഴെ കാണുന്ന ഡിപ്പെൻഡൻസികൾ ചേർക്കണം.

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

അപ്പോൾ നിങ്ങളുടെ ക്ലയന്റ് കോഡിൽ ആവശ്യമായ ലൈബ്രറികൾ ഇമ്പോര്‍ട്ട് ചെയ്യാം.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ക്ലയന്റ് ഘടിപ്പിക്കാൻ മുന്നേറാം.

### -2- ക്ലയന്റും ട്രാൻസ്പോർട്ടും ഘടിപ്പിക്കൽ

നമുക്ക് ട്രാൻസ്പോർട്ടിന്റെ ഒരു ഉദാഹരണവും ക്ലയന്റിന്റെയും സൃഷ്ടിക്കേണ്ടതാണ്:

#### ടൈപ്പ്സ്ക്രിപ്റ്റ്

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

கீழെ കാണുന്ന കോഡിൽ:

- stdio ട്രാൻസ്പോർട്ട് ഒരു উদാഹരണം സൃഷ്ടിച്ചു. സെർവർ കണ്ടെത്താനും സ്റ്റാർട്ട് ചെയ്‌തും എങ്ങനെ എന്ന് കമാൻഡ്, ആർക്കുമെന്റുകൾ കാണിക്കുന്നു, ക്ലയന്റ് സൃഷ്ടിക്കുമ്പോൾ ചെയ്യേണ്ടത്.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- ഒരു പേര്, പതിപ്പ് നൽകി ഒരു ക്ലയന്റ് ഘടിപ്പിച്ചു.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- ക്ലയന്റ് തിരഞ്ഞെടുക്കപ്പെട്ട ട്രാൻസ്പോർട്ടുമായി ബന്ധിപ്പിച്ചു.

    ```typescript
    await client.connect(transport);
    ```

#### പൈതൺ

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# സ്റ്റിഡിയോ കണക്ഷനിനുള്ള സെർവർ പരാമീറ്ററുകൾ സൃഷ്ടിക്കുക
server_params = StdioServerParameters(
    command="mcp",  # പ്രവർത്തനക്ഷമമായ ഫയൽ
    args=["run", "server.py"],  # ഐച്ഛിക കമാൻഡ് ലൈനിലെ ആർഗ്യുമെന്റുകൾ
    env=None,  # ഐച്ഛിക പരിസ്ഥിതി വേരിയബിളുകൾ
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # കണക്ഷൻ ആരംഭിക്കുക
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

താഴെ കാണുന്ന കോഡിൽ:

- ആവശ്യമായ ലൈബ്രറികൾ ഇംപോര്‍ട്ട് ചെയ്‌തു
- സേവറിനു ചേരാൻ ഉപയോഗിക്കുന്ന സെർവർ പരാമീറ്ററുകൾ അനുഭവപ്പെട്ടു
- `run` എന്ന് ഒരു മെത്തഡ് നിർവ്വചിച്ചു, അത് `stdio_client` വിളിക്കുമ്പോൾ ഒരു ക്ലയന്റ് സെഷൻ ആരംഭിക്കുന്നു.
- `asyncio.run`-നു `run` മെത്തഡ് നൽകുന്ന പ്രവേശന ബിന്ദു സൃഷ്ടിച്ചു.

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

താഴെ കാണുന്ന കോഡിൽ:

- ആവശ്യമായ ലൈബ്രറികള്‍ ഇമ്പോര്‍ട്ട് ചെയ്‌തു.
- stdio transport ഒരു ക്ലയന്റ് `mcpClient` സൃഷ്ടിച്ചു, ഇത് MCP സേർവറിലെ ഫീച്ചറുകൾ പട്ടികപ്പെടുത്താനും വിളിക്കാനുമായി ഉപയോഗിക്കും.

ശ്രദ്ധിക്കുക, "Arguments" ൽ *.csproj* അല്ലെങ്കിൽ എക്സിക്യൂട്ടിബിളിലേക്ക് സൂചിപ്പിക്കാം.

#### ജാവ

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
        
        // നിങ്ങളുടെ ക്ലയന്റ് ലോജിക് ഇവിടെ പോകും
    }
}
```

താഴെ കാണുന്ന കോഡിൽ:

- `http://localhost:8080`-ը കണ്ടുള്ള SSE ട്രാൻസ്പോർട്ട് സജ്ജമാക്കുന്ന പ്രധാന മെത്തഡ് സൃഷ്ടിച്ചു, ഇവിടെ MCP സേർവർ പ്രവർത്തിക്കും.
- ട്രാൻസ്പോർട്ട് കോൺസ്ട്രക്ടറായി സ്വീകരിക്കുന്ന ക്ലയന്റ് ക്ലാസ്സ് സൃഷ്ടിച്ചു.
- `run` മെഥഡിൽ ട്രാൻസ്പോർട് ഉപയോഗിച്ച് സിംക്രോണസ് MCP ക്ലയന്റ് സൃഷ്ടിച്ച് ബന്ധം ആരംഭിച്ചു.
- ജാവ സ്പ്രിംഗ് ബൂട്ട് MCP സേർവറുകളുമായി HTTP അടിസ്ഥാന ബന്ധത്തിന് അനുയോജ്യമായ SSE (Server-Sent Events) ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ചു.

#### റസ്റ്റ്

ഈ റസ്റ്റ് ക്ലയന്റ് അടുത്തൂര്‍ "calculator-server" എന്ന സഹോദര പ്രോജക്ടാണെന്ന് പരിഗണിക്കുന്നു. താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് സേർവർ ആരംഭിച്ച് അതുമായി ബന്ധിപ്പിക്കും.

```rust
async fn main() -> Result<(), RmcpError> {
    // സെർവർ ഒരു സഹോദര പ്രോജക്ട് "calculator-server" എന്ന പേരിലുള്ളതാണെന്ന് കരുതുക, അത് സമാന ഡയറക്ടറിയിലാണ്
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

    // TODO: ഇൻനിഷ്യലൈസ് ചെയ്യുക

    // TODO: ടൂളുകൾ ലിസ്റ്റ് ചെയ്യുക

    // TODO: add tool എന്ന ഫംഗ്ഷൻ {"a": 3, "b": 2} എന്ന സംവരണങ്ങളോടെ വിളിക്കുക

    client.cancel().await?;
    Ok(())
}
```

### -3- സേർവർ ഫീച്ചറുകൾ പട്ടികപ്പെടുത്തല്‍

ഇപ്പോൾ, പ്രോഗ്രാം ഓടിച്ചാൽ ബന്ധിപ്പിക്കാൻ കഴിയുന്ന ഒരു ക്ലയന്റ് നമുക്ക് ഉണ്ട്. എന്നാൽ അത് അതിന്റെ ഫീച്ചറുകൾ പട്ടികപ്പെടുത്തുകയുള്ളൂ, അതിനാൽ തുടർന്ന് അതു ചെയ്യാം:

#### ടൈപ്പ്സ്ക്രിപ്റ്റ്

```typescript
// പ്രോംപ്റ്റുകൾ പട്ടിക
const prompts = await client.listPrompts();

// وسائل പട്ടിക
const resources = await client.listResources();

// ഉപകരണങ്ങൾ പട്ടിക
const tools = await client.listTools();
```

#### പൈതൺ

```python
# ലഭ്യമായ വിഭവങ്ങൾ പട്ടികപ്പെടുത്തുക
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ലഭ്യമായ ഉപകരണങ്ങൾ പട്ടികപ്പെടുത്തുക
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ഇവിടെ ലഭ്യമായ റിസോഴ്‌സുകൾ, `list_resources()` ובה כלים, `list_tools` പട്ടികപ്പെടുത്തി അവ പ്രിന്റ് ചെയ്യുന്നു.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

മുകളിൽ സേർവറിലെ ടൂളുകൾ പട്ടികപ്പെടുത്തുന്നതിനുള്ള ഉദാഹരണം. ഓരോ ടൂളിനും അവയുടെ പേര് പ്രിന്റ് ചെയ്യുന്നു.

#### ജാവ

```java
// ഉപകരണങ്ങളെ ലിസ്റ്റ് ചെയ്ത് പ്രദർശിപ്പിക്കുക
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// കണക്ഷൻ സ്ഥിരീകരിക്കാൻ സർവർ പിംഗ് ചെയ്യാനും കഴിയും
client.ping();
```

താഴെ പോയ ഒരിക്കൽ:

- MCP സെർവറിലെ എല്ലാ ടൂളുകളും നേടുന്നതിനായി `listTools()` വിളിച്ചു.
- സർവറുമായി ബന്ധം സാധുവാണോയെന്ന് പരിശോധിക്കാൻ `ping()` ഉപയോഗിച്ചു.
- `ListToolsResult` ടൂളുകളുടെ പേര്, വിവരണം, ഇൻപുട്ട് സ്കീമകൾ എന്നിവ ഉൾക്കൊള്ളുന്നു.

വളരെ നന്ന്, ഇപ്പോൾ ഏറ്റവും വലിയ ചോദ്യം അത് എപ്പോൾ ഉപയോഗിക്കണം? ഈ ക്ലയന്റ് വളരെ ലളിതമാണ്, പ്രത്യേകിച്ച് നമ്മുക്ക് ഫീച്ചറുകൾ ആവശ്യപ്പെടുമ്പോഴാണ് വിളിക്കേണ്ടത്. അടുത്ത അധ്യായത്തിൽ സ്വയം വലിയ ഭാഷാ മോഡൽ (LLM) ഉള്ള കൂടുതൽ സങ്കീർണ ക്ലയന്റ് സൃഷ്ടിക്കും. ഇന്നതിന്, സേർവറിൽ ഫീച്ചറുകൾ എങ്ങനെ വിളിക്കാമെന്ന് നോക്കാം:

#### റസ്റ്റ്

മെയിൻ ഫംഗ്ഷനിൽ, ക്ലയന്റ് ആരംഭിച്ചതിന് ശേഷം, സേര്‍വറിനെയും ആരംഭിക്കുകയും ചില ഫീച്ചറുകൾ പട്ടികപ്പെടുത്തുകയും ചെയ്യാം.

```rust
// ആരംഭിക്കുക
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// ഉപകരണങ്ങളുടെ പട്ടിക
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ഫീച്ചറുകൾ വിളിക്കുക

ഫീച്ചറുകൾ വിളിക്കാൻ ശരിയായ ആര്‍ഗുമെന്റുകൾ വ്യക്തമാക്കണം, ചിലപ്പോൾ വിളിക്കുന്നത് എന്തെന്ന് പേരും വ്യക്തമാക്കണം.

#### ടൈപ്പ്സ്ക്രിപ്റ്റ്

```typescript

// ഒരു റിസോർസ് വായിക്കുക
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ഒരു ഉപകരണം വിളിക്കുക
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// പ്രംപ്റ്റ് വിളിക്കുക
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

താഴെപ്പറയുന്ന കോഡിൽ:

- ഒരു റിസോഴ്‌സ് വായിക്കുവാൻ, `readResource()` വിളിച്ചുകൊണ്ട് `uri` കൊടുക്കുന്നു. സേർവർ ഭാഗത്ത് ഇത് ഇതുപോലെയാണ്.

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

    നമ്മുടെ `uri` മൂല്യം `file://example.txt` സേർവറിൽ `file://{name}`-ന് പൊരുത്തപ്പെടുന്നു. `example.txt` `name`-ന് മാപ്പ് ചെയ്യപ്പെടും.

- ഒരു ടൂൾ വിളிக்கുവാൻ, `name` യും `arguments` ഉം നൽകുന്നു:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- ഒരു പ്രോംപ്റ്റ് ലഭിക്കാൻ, `getPrompt()` `name` ഉം `arguments` ഉം നല്‍കി വിളിക്കുന്നു. സേർവർ കോഡ് ഇപ്രകാരമാണ്:

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

    അതിനാൽ നിങ്ങൾക്ക് ലഭ്യമായ ക്ലയന്റ് കോഡ് സേർവറിൽ പത്രാരേഖപ്പെടുത്തിയതോട് പൊരുത്തപ്പെടേണ്ടതാണ്:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### പൈതൺ

```python
# ഒരു വിഭവം വായിക്കുക
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ഒരു ഉപകരണം വിളിക്കുക
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

താഴെപ്പറയുന്ന കോഡിൽ:

- `greeting` നാമത്തിലുള്ള ഒരു റിസോഴ്‌സിനെ `read_resource` ഉപയോഗിച്ച് വിളിച്ചു.
- `add` നാമത്തിലുള്ള ഒരു ടൂൾ `call_tool` ഉപയോഗിച്ച് വിളിച്ചു.

#### .NET

1. ഒരു ടൂൾ വിളിക്കാന്‍ കോഡ് ചേർക്കുക:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ഫലം പ്രിന്റ് ചെയ്യാൻ താഴെ കാണുന്ന കോഡ് ഉപയോഗിക്കുക:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### ജാവ

```java
// പല കാൽക്കുലേറ്റർ ഉപകരണങ്ങൾ വിളിക്കുക
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

താഴെപ്പറയുന്ന കോഡിൽ:

- `callTool()` മെത്തഡ് ഉപയോഗിച്ച് നിരവധി കല്കുലേറ്റർ ടൂൾുകൾ `CallToolRequest` ഒബ്ജക്റ്റുകളുവഴി വിളിച്ചു.
- ഓരോ ടൂൾ വിളിയും ടൂൾ നാമവും ആ ടൂളിന് ആവശ്യമായ ആર્ગുമെന്റുകളുടെ `Map` ഉം വ്യക്തമാക്കുന്നു.
- സേർവർ ടൂളുകൾ മാത്തമാറ്റിക്കൽ ഓപ്പറേഷനുകൾക്കായി പ്രത്യേക പാരാമീറ്റർ നാമങ്ങൾ (ഉദാ: "a", "b") പ്രതീക്ഷിക്കുന്നു.
- ഫലങ്ങൾ `CallToolResult` ഒബ്ജക്റ്റുകളായി സേർവറിൽ നിന്നുള്ള പ്രതികരണവുമായി തിരികെ ലഭിക്കുന്നു.

#### റസ്റ്റ്

```rust
// "a": 3, "b": 2} എന്ന_ARGUMENT_കളോടെ add_ടൂൾ 호출ിക്കുക
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

### -5- ക്ലയന്റ് ഓടിക്കുക

ക്ലയന്റ് ഓടിക്കാന്‍, ടർമിനലിൽ താഴെ കാണുന്ന കമാൻഡ് ടൈപ്പ് ചെയ്യുക:

#### ടൈപ്പ്സ്ക്രിപ്റ്റ്

*package.json*-ലെ "scripts" വിഭാഗത്തില്‍ താഴെ കൊടുത്തത് ചേർക്കുക:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### പൈതൺ

താഴെയുള്ള കമാന്‍ഡ് ഉപയോഗിച്ച് ക്ലയന്റ് വിളിക്കുക:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### ജാവ

ആദ്യം നിങ്ങളുടെ MCP സേര്‍വര്‍ `http://localhost:8080`-ൽ പ്രവർത്തിക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക. തുടർന്ന് ക്ലയന്റ് ഓടിക്കുക:

```bash
# നിങ്ങളുടെ പ്രോജക്ട് നിർമ്മിക്കുക
./mvnw clean compile

# ക്ലയന്റ് പ്രവർത്തിപ്പിക്കുക
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

അല്ലെങ്കിൽ പരിഹാര ഫോള്ഡര്‍ `03-GettingStarted\02-client\solution\java`ല്‍ നൽകിയ പൂര്‍ണ ക്ലയന്റ് പ്രോജക്ട് ഓടിക്കാങ്ങള്‍:

```bash
# പരിഹാര ഡയറക്ടറിയിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക
cd 03-GettingStarted/02-client/solution/java

# ജാർറെ നിർമാണം ചെയ്ത് പ്രവർത്തിപ്പിക്കുക
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### റസ്റ്റ്

```bash
cargo fmt
cargo run
```

## നിയമനം

ഈ നിയമനത്തില്‍, നിങ്ങള്‍ക്ക് പഠിച്ച കാര്യങ്ങള്‍ ഉപയോഗിച്ച് ഒരു ക്ലയന്റ് സൃഷ്ടിക്കണം.

ഈ എന്നാൽ നിങ്ങൾ വിളിക്കേണ്ട MCP സേർവർ ഇവിടെ കാണുന്നു, നിങ്ങൾക്ക് അത് ഉപയോഗിച്ച് കൂടുതൽ ഫീച്ചറുകൾ ചേർത്ത് അതിനെ കൂടുതൽ രസകരമാക്കാം.

### ടൈപ്പ്സ്ക്രിപ്റ്റ്

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP സെർവർ സൃഷ്‌ടിക്കുക
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ഒരു കൂട്ടിച്ചേർക്കൽ ഉപകരണം ചേർക്കുക
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ഒരു ഡൈനാമിക് ഗ്രീറ്റിംഗ് റിസോഴ്‌സ് ചേർക്കുക
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

// stdin-ൽ സന്ദേശങ്ങൾ സ്വീകരിച്ചു, stdout-ൽ സന്ദേശങ്ങൾ അയക്കാൻ ആരംഭിക്കുക

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

### പൈതൺ

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ഒരു MCP സെർവർ സൃഷ്ടിക്കുക
mcp = FastMCP("Demo")


# ഒരു കൂടൽ ഉപകരണം ചേർക്കുക
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ഒരു ഡൈനാമിക് ഗ്രീറ്റിംഗ് റിസോഴ്സ് ചേർക്കുക
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

ഈ പ്രോജക്ട് കാണുക [പ്രോംപ്റ്റുകളും റിസോഴ്‌സസ് കൂട്ടിച്ചേർക്കുന്നതും](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) എങ്ങനെ എന്നറിയാൻ.

കൂടാതെ, ഈ ലിങ്ക് പരിശോധിക്കുക‌ [പ്രോംപ്റ്റുകളും റിസോഴ്‌സുകളും വിളിക്കുന്നതിന്](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### റസ്റ്റ്

മുൻ സെക്ഷനിൽ [previous section](../../../../03-GettingStarted/01-first-server) നിങ്ങൾ Rust ഉപയോഗിച്ച് എളുപ്പം MCP സേർവർ സൃഷ്ടിക്കുന്നതറിയാമായിരുന്നു. അതിൽ തുടരെ നിർമ്മിക്കാം, അല്ലെങ്കിൽ ഈ ലിങ്ക് കാണുക കൂടുതൽ Rust അടിസ്ഥാന MCP സെർവർ ഉദാഹരണങ്ങൾക്ക്: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## പരിഹാരം

**പരിഹാരം ഫൊള്‍ഡര്‍** ഈ ടൊട്ടോറിയലില്‍ കൈകാര്യം ചെയ്ത എല്ലാ ആശയങ്ങളും പ്രകടിപ്പിക്കുന്ന പൂര്‍ണവും പ്രവർത്തനക്ഷമവുമായ ക്ലയന്റ് നടപ്പാക്കലുകൾ ഉണ്ട്. ഓരോ പരിഹാരത്തിലും ക്ലയന്റും സെർവറും വേർതിരിച്ചിട്ടുള്ള, സ്വതന്ത്രമായ പ്രോജക്റ്റുകളായാണ് നിലവിലുള്ളത്.

### 📁 പരിഹാരം ഘടന

പരിഹാര ഡയറക്ടറി പ്രോഗ്രാമിംഗ് ഭാഷ അനുസരിച്ച് ക്രമീകരിച്ചിരിക്കുന്നു:

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

### 🚀 ഓരോ പരിഹാരത്തിലും ഉള്ളത്

ഭാഷപ്രകാരം ഓരോ പരിഹാരത്തിലും ലഭ്യമാകുന്നത്:

- **പാഠത്തിലെ എല്ലാ ഫീച്ചറുകളടങ്ങിയ പൂര്‍ണ ക്ലയന്റ് നടപ്പാക്കല്‍**
- **സഭ്യമായ ഡിപ്പെൻഡൻസികളോടും കോൺഫിഗറേഷനോടും ഉള്ള പ്രോജക്റ്റ് ഘടന**
- **ഇടയ്ക്കനുസരിച്ച് സജ്ജീകരണവും ഓടിക്കുന്നതിനുള്ള സ്ക്രിപ്റ്റുകളും**
- **ഭാഷാ അടിസ്ഥാനമാക്കിയുള്ള വിശദമായ README**
- **പിശക് കൈകാര്യം ചെയ്യലും ഫലം പ്രോസസ്സിംഗിന്റെ ഉദാഹരണങ്ങളും**

### 📖 പരിഹാരങ്ങൾ ഉപയോഗിക്കുന്നത്

1. **പ്രിയപ്പെട്ട ഭാഷാ ഫോൾഡറിലേക്ക് പോവുക**:

   ```bash
   cd solution/typescript/    # ടൈപ്‌സ്‌ക്രിപ്റ്റ് വേണ്ടി
   cd solution/java/          # ജാവയ്ക്ക് വേണ്ടി
   cd solution/python/        # പൈത്തൺ വേണ്ടി
   cd solution/dotnet/        # .NET വേണ്ടി
   ```

2. **ഓരോ ഫോൾഡറിലും README നിർദ്ദേശങ്ങൾ പാലിക്കുക**:
   - ആവശ്യമായ ഡിപ്പെൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുക
   - പ്രോജക്ട് കെട്ടിപ്പടുക്കുക
   - ക്ലയന്റ് ഓടിക്കുക

3. **ഉദാഹരണ ഫലമായതായി കാണേണ്ടത്**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

സമഗ്രമായ ഡോക്യുമെന്റേഷനും ഘട്ടം ഘട്ടമായി നിർദ്ദേശങ്ങളും ഇവിടെ കാണാം: **[📖 പരിഹാര ഡോക്യുമെന്റേഷൻ](./solution/README.md)**

## 🎯 പൂര്‍ണ ഉദാഹരണങ്ങള്‍

ഈ ടൊട്ടോറിയലിൽ ഉൾപ്പെടുത്തിയ എല്ലാ പ്രോഗ്രാമിംഗ് ഭാഷകളിലുമായി സംയുക്തവും പ്രവർത്തനക്ഷമവുമായ ക്ലയന്റ് നടപ്പാക്കലുകൾ നൽകി ഉണ്ട്. ഈ ഉദാഹരണങ്ങൾ മുകളിൽ പറഞ്ഞ മുഴുവൻ പ്രവർത്തനസാന്ദര്‍ഭം ആവിഷ്‌ക്കരിച്ചു, നിങ്ങൾക്ക് ഞങ്ങളുടെ സ്വന്തം പ്രോജക്ടുകൾക്കായുള്ള നൈസർഗിക ഉദ്ഘാടനം രേഖകളായും റഫറൻസായി ഉപയോഗിക്കാം.

### ലഭ്യമായ പൂര്‍ണ ഉദാഹരണങ്ങള്‍

| ഭാഷ | ഫയൽ | വിവരണം |
|----------|------|-------------|
| **ജാവ** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് തികച്ചും പൂർണ ജാവ ക്ലയന്റ്, സമഗ്രമായ പിശക് കൈകാര്യം ചെക്കുകൾ സഹിതം |
| **സി#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സെർവർ ഓട്ടോമാറ്റിക് ആരംഭിക്കുന്ന പൂര്‍ണ C# ക്ലയന്റ് |
| **ടൈപ്പ്സ്ക്രിപ്റ്റ്** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP പ്രോട്ടോക്കോള്‍ പൂർണ്ണ പിന്തുണയുള്ള പൂര്‍ണ ടൈപ്പ്സ്ക്രിപ്റ്റ് ക്ലയന്റ് |
| **പൈതൺ** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await പാറ്റേണുകൾ ഉപയോഗിച്ചുള്ള പൂർണ പൈതൺ ക്ലയന്റ് |
| **റസ്റ്റ്** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | അസിങ്ക് പ്രവർത്തനങ്ങൾക്ക് ഒത്ത് ടോകിയോ ഉപയോഗിച്ച് പൂര്‍ണ റസ്റ്റ് ക്ലയന്റ് |

ഓരോ പൂര്‍ണ ഉദാഹരണത്തിലും ഉള്‍പ്പെടുന്നു:

- ✅ **ബന്ധം സ്ഥാപിക്കൽ** കൂടാതെ പിശക് കൈകാര്യം ചെയ്യല്‍
- ✅ **സേർവർ കണ്ടെത്തൽ** (ഉപയോഗയോഗ്യമായ ടൂളുകൾ, റിസോഴ്‌സുകൾ, പ്രോംപ്റ്റുകൾ)
- ✅ **കല്കുലേറ്റർ പ്രവർത്തനങ്ങൾ** (ചേർക്കുക, ഒഴിവാക്കുക, ഗുണിക്കുക, വിഭജിക്കുക, സഹായം)
- ✅ **ഫലം പ്രോസസ്സിംഗും ഘടനാപരമായ ഔട്ട്പുട്ടും**
- ✅ **സമഗ്ര പിശക് കൈകാര്യം ചെയ്യല്‍**

- ✅ **സ്വच्छവും, രേഖപ്പെടുത്തിയ കോഡും** ഘട്ടം ഘട്ടമായി കമന്റുകളോടുകൂടി

### സമ്പൂർണ്ണ ഉദാഹരണങ്ങളുമായി ആരംഭിക്കൽ

1. മുകളിൽ നൽകിയ പട്ടികയിൽ നിന്ന് **നിങ്ങളുടെ ഇഷ്ട ഭാഷ തിരഞ്ഞെടുക്കുക**
2. **സമ്പൂർണ്ണ ഉദാഹരണ ഫയൽ അവലೋಕനം ചെയ്യുക** പൂര്‍ണ്ണമായ നടപ്പിലാക്കലുമായി പരിചയപ്പെടാൻ
3. [`complete_examples.md`](./complete_examples.md)ൽ ഉള്ള നിർദ്ദേശങ്ങൾ പാലിച്ച് **ഉദാഹരണം പ്രവർത്തിപ്പിക്കുക**
4. **നിങ്ങളുടെ പ്രത്യേക ഉപയോഗത്തിനായി** ഉദാഹരണം **പരിഷ്ക്കരിച്ചു വിപുലീകരിക്കുക**

ഈ ഉദാഹരണങ്ങൾ പ്രവർത്തിപ്പിക്കാനും പ്രവൃത്തി നിജീകരിക്കാനുമുള്ള വിശദമായ രേഖകൾക്ക്, നോക്കുക: **[📖 സമ്പൂർണ്ണ ഉദാഹരണങ്ങളുടെ രേഖകൾ](./complete_examples.md)**

### 💡 പരിഹാരവും സമ്പൂർണ്ണ ഉദാഹരണങ്ങളും തമ്മിലുള്ള വ്യത്യാസം

| **പരിഹാര ഫോൾഡർ** | **സമ്പൂർണ്ണ ഉദാഹരണങ്ങൾ** |
|--------------------|--------------------- |
| ബിൽഡ് ഫയലുകൾ ഉൾപ്പെടെയുള്ള പൂർണ്ണ പ്രോജക്റ്റ് ഘടന | ഏക-ഫയൽ നടപ്പാക്കലുകൾ |
| ആശ്രിതത്വങ്ങളോടുകൂടി നടപ്പാക്കാൻ സജ്ജം | ശ്രദ്ധിച്ച കോഡ് ഉദാഹരണങ്ങൾ |
| ഉത്പാദനപോലെ സജ്ജീകരണം | വിദ്യാഭ്യാസ റഫറൻസ് |
| ഭാഷാനുസൃത ഉപകരണങ്ങൾ | പലഭാഷകളിലെയും താരതമ്യം |

ഇരുവരും ഉപകാരപ്രദമാണ് - പൂർണ്ണമായ പ്രോജക്റ്റുകൾക്കായി **പരിഹാര ഫോൾഡർ** ഉപയോഗിക്കുക; പഠനത്തിനും റഫറൻസിനും **സമ്പൂർണ്ണ ഉദാഹരണങ്ങൾ** ഉപയോഗിക്കുക.

## പ്രധാന ആശയങ്ങൾ

ഈ അധ്യായത്തിലെ പ്രധാന ആശയങ്ങൾ ക്ളയന്റുകളെക്കുറിച്ചാണ്:

- സെർവറിൽ സവിശേഷതകൾ കണ്ടെത്താനും 호출ിക്കാനുമായി ഉപയോഗിക്കാനാകും.
- സ്വയം ആരംഭിക്കുമ്പോൾ സെർവർ ആരംഭിക്കാൻ കഴിയും (ഈ അധ്യായത്തിലെ പോലെ), എന്നാൽ ക്ളയന്റുകൾ already പ്രവർത്തിക്കുന്ന സെർവറുകളിൽ גם കണക്ട് ചെയ്യാനാകും.
- മുൻ അധ്യായത്തിൽ വിവരിച്ച ഇൻസ്പെക്ടർ പോലുള്ള അന്തരീക്ഷങ്ങൾക്കൊപ്പമുള്ള സെർവർ കഴിവുകൾ പരിശോധിക്കാൻ മികച്ച മാർഗ്ഗമാണ്.

## അധിക വനരങ്ങളുമായി

- [MCP-യിൽ kliyantrukal നിർമ്മിക്കൽ](https://modelcontextprotocol.io/quickstart/client)

## സാമ്പിളുകൾ

- [ജാവാ കല്കുലേറ്റർ](../samples/java/calculator/README.md)
- [.NET കല്കുലേറ്റർ](../../../../03-GettingStarted/samples/csharp)
- [ജാവാസ്ക്രീപ്റ്റ് കല്കുലേറ്റർ](../samples/javascript/README.md)
- [ടൈപ്പ്‌സ്‌ക്രിപ്റ്റ് കല്കുലേറ്റർ](../samples/typescript/README.md)
- [പൈറ്റണ്‍ കല്കുലേറ്റർ](../../../../03-GettingStarted/samples/python)
- [റസ്റ്റ് കല്കുലേറ്റർ](../../../../03-GettingStarted/samples/rust)

## അടുത്തത് എന്ത്

- അടുത്തത്: [LLM ഉപയോഗിച്ച് ക്ലയന്റ് സൃഷ്ടിക്കൽ](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->