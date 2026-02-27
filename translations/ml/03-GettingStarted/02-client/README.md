# ഒരു ക്ലയന്റ് സൃഷ്‌ടിക്കൽ

ക്ലയന്റുകൾ MCP സെർവറുമായി നേരിട്ട് സംസാരിക്കുന്ന കസ്റ്റം ആപ്ലിക്കേഷനുകളോ സ്ക്രിപ്റ്റുകളോ ആണ്, അവ വിഭവങ്ങൾ, ഉപകരണങ്ങൾ, പ്രോംപ്റ്റുകൾ അഭ്യർത്ഥിക്കുന്നു. സെർവറുമായി സംവദിക്കുന്നതിനുള്ള ഗ്രാഫിക്കൽ ഇന്റർഫേസ് നൽകുന്ന ഇൻസ്‌പക്ടർ ഉപകരണം ഉപയോഗിക്കുന്നതിനേക്കാൾ വ്യത്യസ്തമായി, നിങ്ങളുടെ സ്വന്തം ക്ലയന്റ് എഴുതുന്നത് പ്രോഗ്രാമാറ്റിക്, സ്വയംസഞ്ചരിക്കുന്ന ഇടപെടലുകൾക്ക് സാഹചര്യം സൃഷ്‌ടിക്കുന്നു. ഇതുവഴി ഡെവലപ്പർമാർക്ക് MCP ശേഷികളെ അവരുടെ സ്വന്തം പ്രവർത്തനപ്രവാഹങ്ങളിലേക്ക് ഏകോപിപ്പിക്കാനും, കൃത്യമായ ആവശ്യങ്ങൾക്കായി കസ്റ്റം പരിഹാരങ്ങൾ നിർമ്മിക്കാനും കഴിയും.

## അവലോകനം

ഈ പാഠം MCP ഇക്കോസിസ്റ്റത്തിൽ ക്ലയന്റുകളുടെ ആശയം പരിചയപ്പെടുത്തുന്നു. നിങ്ങൾ സ്വയം ഒരു ക്ലയന്റ് എഴുതാനും അത് ഒരു MCP സെർവറുമായി ബന്ധിപ്പിക്കുന്നതും പഠിക്കും.

## പഠനലക്ഷ്യങ്ങൾ

ഈ പാഠം കഴിഞ്ഞാൽ, നിങ്ങൾ ചെയ്യാൻ കഴിയുന്നതാണ്:

- ഒരു ക്ലയന്റ് എന്ത് ചെയ്യാമെന്ന് മനസിലാക്കുക.
- നിങ്ങളുടെ സ്വന്തം ക്ലയന്റ് എഴുതുക.
- MCP സെർവറുമായി ക്ലയന്റ് ബന്ധിപ്പിച്ച് ടെസ്റ്റ് ചെയ്ത് ആവശ്യാനുസരണം പ്രവർത്തിക്കുന്നുവെന്ന് ഉറപ്പാക്കുക.

## ഒരു ക്ലയന്റ് എഴുതുമ്പോൾ എന്തെല്ലാം ചെയ്യണം?

ഒരു ക്ലയന്റ് എഴുതാൻ നിങ്ങൾ ചെയ്യേണ്ടത്:

- **ശരിയായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്യുക.** മുമ്പ് ഉപയോഗിച്ച ലൈബ്രറിയെ പോലെ തന്നെ, പക്ഷേ വ്യത്യസ്ത ഘടകങ്ങൾ ഉപയോഗിക്കും.
- **ഒരു ക്ലയന്റ് ഇൻസ്റ്റാൻസ് സൃഷ്ടിക്കുക.** ഇത് ഒരു ക്ലയന്റ് ഒബ്ജക്ട് ഉണ്ടാക്കുകയും അത് തിരഞ്ഞെടുക്കപ്പെട്ട ട്രാൻസ്പോർട്ട് രീതിയുമായി ബന്ധിപ്പിക്കുകയും ചെയ്യുന്നതാണ്.
- **ഏത് വിഭവങ്ങൾ പട്ടികപ്പെടുത്തണമെന്ന് തീരുമാനിക്കുക.** നിങ്ങളുടെ MCP സെർവറിനൊപ്പം വിഭവങ്ങൾ, ഉപകരണങ്ങൾ, പ്രോംപ്റ്റുകൾ ഉണ്ടാകും; അവയിൽ ഏതെല്ലാമാണു് പട്ടികപ്പെടുത്തേണ്ടത് എന്നത് നിങ്ങൾ തീരുമാനിക്കണം.
- **ക്ലയന്റിനെ ഹോസ്റ്റ് ആപ്ലിക്കേഷൻസുമായി സംയോജിപ്പിക്കുക.** സെർവറിന്റെ ശേഷികൾ മനസ്സിലായാൽ, ഒരു ഉപയോക്താവ് ഒരു പ്രോംപ്റ്റ് ಅಥವಾ മറ്റു കമാൻഡ് ടൈപ്പ് ചെയ്യുന്നപ്പോൾ അനുബന്ധ സെർവർ ഫീച്ചർ വിളിക്കപ്പെടാൻ ഇത് നിങ്ങളുടെ ഹോസ്റ്റ് ആപ്ലിക്കേഷനുമായി സംയോജിപ്പിക്കണം.

ഇപ്പോൾ ഞങ്ങൾ ഉയർന്ന നിലയിൽ ചെയ്യുന്ന കാര്യങ്ങൾ മനസ്സിലാക്കിയിട്ടുണ്ടെങ്കിൽ, അടുത്തതായി ഒരു ഉദാഹരണം നോക്കാം.

### ഒരു ഉദാഹരണ ക്ലയന്റ്

ഈ ഉദാഹരണ ക്ലയന്റ് നോക്കാം:

### ടൈപ്‌സ്‌ക്രിപ്റ്റ്

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

// പ്രോംപ്റ്റുകൾ ലിസ്റ്റ് ചെയ്യുക
const prompts = await client.listPrompts();

// ഒരു പ്രോംപ്റ്റ് നേടുക
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// വിഭവങ്ങൾ ലിസ്റ്റ് ചെയ്യുക
const resources = await client.listResources();

// ഒരു വിഭവം വായിക്കുക
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


മുൻкодിൽ ഞങ്ങൾ:

- ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തിട്ടുണ്ട്
- ഒരു ക്ലയന്റ് ഇൻസ്റ്റാൻസ് സൃഷ്ടിച്ച് stdio ട്രാൻസ്പോർട്ടായി ഉപയോഗിച്ച് ബന്ധിപ്പിച്ചിട്ടുണ്ട്
- പ്രോംപ്റ്റുകളും വിഭവങ്ങളും ഉപകരണങ്ങളും പട്ടികപ്പെടുത്തി അവയെല്ലാം വിളിച്ചാണ് പ്രവർത്തിപ്പിച്ചത്

അങ്ങനെ ഒരു MCP സെർവറുമായി സംസാരിക്കാൻ കഴിയുന്ന ക്ലയന്റ് നിങ്ങൾക്ക് ലഭിച്ചു.

അടുത്ത വ്യായാമത്തിൽ ഓരോ കോഡ് സ്നിപ്പെറ്റും ഞങ്ങൾ വിശദമായി പരിശോധിച്ച് വിശദീകരിക്കാം.

## വ്യായാമം: ക്ലയന്റ് എഴുതുക

മുമ്പ് പറഞ്ഞതു പോലെ, കോഡ് വിശദമായി വിശദീകരിക്കാൻ നമ്മൾ സമയം എടുക്കാം, ആവശ്യമെങ്കിൽ കൂടെ കോഡ് ചെയ്യാനും കഴിയും.

### -1- ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്യുക

നമുക്ക് ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്യാം. ക്ലയന്റിനും നാം തിരഞ്ഞെടുത്ത ട്രാൻസ്പോർട്ട് പ്രോട്ടോക്കോളായ stdioയ്ക്കും റഫറൻസുകൾ വേണ്ടിവരും. stdio നിങ്ങളുടെ ലോക്കൽ മെഷീൻൽ പ്രവർത്തിക്കുന്നതിനുള്ള പ്രോട്ടോക്കോൾ ആണ്. SSE മറ്റൊരു ട്രാൻസ്പോർട്ട് പ്രോട്ടോക്കോളാണ്, അത് ഭാവി അധ്യായങ്ങളിൽ കാണിക്കും. ഇപ്പോൾ stdioത്തോടെയറിയാം മുന്നോട്ട് പോകുക.

#### ടൈപ്‌സ്‌ക്രിപ്റ്റ്

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

ജാവയിൽ, മുമ്പത്തെ വ്യായാമത്തിൽ നിന്നും MCP സെർവറുമായി ബന്ധിപ്പിക്കുന്ന ക്ലയന്റ് സൃഷ്ടിക്കും. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) പോപ്പ്‌വലിയിലുള്ള ജാവ സ്പ്രിംഗ് ബൂട്ട് പ്രോജക്ട് ഘടന ഉപയോഗിച്ച്, `src/main/java/com/microsoft/mcp/sample/client/` ഫോൾഡറിൽ `SDKClient` നാമമുള്ള പുതിയ ജാവ ക്ലാസ് സൃഷ്ടിച്ച് താഴെക്കൊടുത്ത ഇറക്കുമതികൾ ചേർക്കുക:

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

`Cargo.toml` ഫയലിൽ താഴെ പറഞ്ഞ ഡിപ്പെൻഡൻസികൾ ചേർക്കണം.

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

അവിടെ നിന്നു, ക്ലയന്റ് കോഡിൽ ആവശ്യമായ ലൈബ്രറികളും ഇറക്കുമതി ചെയ്യാം.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ഇപ്പോൾ ഇൻസ്റ്റാൻഷ്യേഷൻ കാണാം.

### -2- ക്ലയന്റ്, ട്രാൻസ്പോർട്ട് ഇൻസ്റ്റാൻഷ്യേറ്റ് ചെയ്യുക

ട്രാൻസ്പോർട്ടിനും ക്ലയന്റിനും ഇൻസ്റ്റാൻസ് സൃഷ്ടിക്കേണ്ടതുണ്ട്:

#### ടൈപ്‌സ്‌ക്രിപ്റ്റ്

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

മുൻകോഡിൽ ഞങ്ങൾ:

- stdio ട്രാൻസ്പോർട്ട് ഇൻസ്റ്റാൻസ് സൃഷ്ടിച്ചു. സെർവർ എങ്ങനെ കണ്ടെത്തി തുടങ്ങണമെന്ന് കാണിക്കുന്ന കമാൻഡ്, അർഗുമെന്റുകൾ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- ഒരു ക്ലയന്റ് ഇൻസ്റ്റാൻസ് (പേര്, വേർഷൻ നൽകി) സൃഷ്ടിച്ചു.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- തിരഞ്ഞെടുക്കപ്പെട്ട ട്രാൻസ്പോർട്ടുമായി ക്ലയന്റ് ബന്ധിപ്പിച്ചു.

    ```typescript
    await client.connect(transport);
    ```

#### പൈതൺ

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# സ്റ്റ്ഡിയോ കണക്ഷനിന് സെർവർ പാരാമീറ്ററുകൾ സൃഷ്‌ടിക്കുക
server_params = StdioServerParameters(
    command="mcp",  # തുടക്കശേഷമുള്ള പ്രോഗ്രാം
    args=["run", "server.py"],  # ഐച్ఛിക കമാൻഡ് ലൈൻ ആർഗ്യുമെന്റുകൾ
    env=None,  # ഐച്ഛിക പരിസ്ഥിതി വ്യത്യാസങ്ങൾ
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

മുൻകോഡിൽ:

- ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തിട്ടുണ്ട്
- സെർവർ റൺചെയ്യുന്നതിനായി സെർവർ പാരാമീറ്ററുകൾ ഉൾക്കുന്ന ഒബ്ജക്ട് സൃഷ്ടിച്ചു
- `run` എന്ന മെഥഡ്ഫ് നിർവ്വചിച്ചു, അത് `stdio_client` വിളിച്ച് ഒരു ക്ലയന്റ് സെഷൻ തുടങ്ങുന്നു
- `asyncio.run` എന്നതിൽ `run` മെథഡ്ഫ് നൽകിയ എൻട്രി പോയിന്റ് ഉണ്ടാക്കി

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

മുൻകോഡിൽ:

- ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു
- stdio ട്രാൻസ്പോർട്ട് സൃഷ്ടിക്കുകയും `mcpClient` എന്ന ക്ലയന്റ് സൃഷ്ടിക്കുകയും ചെയ്തു, ഇത് MCP സെർവറിലേയ്ക്ക് ഫീച്ചറുകൾ പട്ടികപ്പെടുത്താനും വിളിക്കാനുമുള്ളതാണ്

കമാൻഡിന്റെ Arguments ന് തലക്കെട്ടിൽ *.csproj* അല്ലെങ്കിൽ എക്സിക്യൂട്ടബിൾ പോയിന്റ് നൽകാം.

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
        
        // നിങ്ങളുടെ ക്ലയന്റ് ലജിക്കും ഇവിടെകൾ
    }
}
```

മുൻകോഡിൽ:

- MCP സെർവർ പ്രവർത്തിക്കുന്ന `http://localhost:8080` എന്ന വിലാസത്തിലുള്ള SSE ട്രാൻസ്പോർട്ട് സജ്ജമാക്കിയ പ്രൈമറി മേധാവി മെഥഡ്ഫ് സൃഷ്ടിച്ചു
- ട്രാൻസ്പോർട്ട് കൺസ്ട്രക്ടർ പാരാമീറ്ററായി എടുത്ത ഒരു ക്ലയന്റ് ക്ലാസ് സൃഷ്ടിച്ചു
- `run` മെഥഡിൽ ട്രാൻസ്പോർട്ടുപയോഗിച്ച് synchronous MCP ക്ലയന്റ് നിർമ്മിക്കുകയും കണക്ഷൻ ആരംഭിക്കുകയും ചെയ്തു
- ജാവ സ്പ്രിംഗ് ബൂട്ടിനുള്ള MCP സെർവറുമായി HTTP അടിസ്ഥാനത്തിലുള്ള സംവാദത്തിനു SSE ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ചു

#### റസ്റ്റ്

റസ്റ്റ് ക്ലയന്റ് സെർവർ "calculator-server" എന്ന അനുറൂപ പ്രോജക്ട് തുല്യ ഡയറക്ടറിയിൽ എന്നു കരുതുന്നു. 아래 കോഡ് സെർവർ ആരംഭിക്കുകയും അതുമായി ബന്ധിപ്പിക്കുകയും ചെയ്യും.

```rust
async fn main() -> Result<(), RmcpError> {
    // സർവർ അവിടെ തന്നെ ഡയറക്റ്ററിയിലുള്ള "calculator-server" എന്ന സഹോദര പ്രോജക്ട് എന്നാണ് കരുതുക
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

    // ചെയ്യേണ്ടത്: ആരംഭിക്കുക

    // ചെയ്യേണ്ടത്: ടൂളുകൾ പട്ടിക ചെയ്യുക

    // ചെയ്യേണ്ടത്: آرگیومെന്റുകൾ = {"a": 3, "b": 2} ആയി add tool കോളുചെയ്യുക

    client.cancel().await?;
    Ok(())
}
```

### -3- സെർവർ ഫീച്ചറുകൾ പട്ടികപ്പെടുത്തൽ

ഇപ്പോൾ, ക്ലയന്റ് സെർവറുമായി ബന്ധിപ്പിക്കാം. എന്നാൽ അതിന്റെ ഫീച്ചറുകൾ പട്ടികപ്പെടുത്തുന്നില്ല. അത് ചെയ്യാം:

#### ടൈപ്‌സ്‌ക്രിപ്റ്റ്

```typescript
// പ്രോംപ്റ്റുകൾ പട്ടിക
const prompts = await client.listPrompts();

// വിഭവങ്ങൾ പട്ടിക
const resources = await client.listResources();

// ഉപകരണങ്ങൾ പട്ടിക
const tools = await client.listTools();
```

#### പൈതൺ

```python
# ലഭ്യമായ വിഭവങ്ങൾ പട്ടിക ചെയ്യുക
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ലഭ്യമായ ഉപകരണങ്ങൾ പട്ടിക ചെയ്യുക
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ഇവിടെ `list_resources()` ഉപയോഗിച്ച് ലഭ്യമായ വിഭവങ്ങളും `list_tools` ഉപയോഗിച്ച് ഉപകരണങ്ങളും പട്ടികപ്പെടുത്തുകയും അവ പ്രിന്റ് ചെയ്യുകയും ചെയ്യുന്നു.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ഇവിടെയുണ്ട് സെർവറിലെ ഉപകരണങ്ങൾ പട്ടികപ്പെടുത്താനുള്ള ഒരു ഉദാഹരണം. ഓരോ ഉപകരണത്തിനും അതിന്റെ പേര് പ്രിന്റ് ചെയ്യുന്നു.

#### ജാവ

```java
// ടൂൾസുകൾ പട്ടികപ്പെടുത്തി കാണിക്കുക
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// ബന്ധം സ്ഥിരീകരിക്കാൻ സേർവർ പിംഗ് ചെയ്യുന്നതും നിങ്ങൾക്ക് സാധിക്കും
client.ping();
```

മുൻകോഡിൽ:

- MCP സെർവറിൽ നിന്നും ലഭ്യമായ ടൂൾസ് ലഭ്യമാക്കാൻ `listTools()` വിളിച്ചു
- കണക്ഷൻ പ്രവർത്തനക്ഷമമാണെന്ന് ഉറപ്പാക്കാൻ `ping()` ഉപയോഗിച്ചു
- `ListToolsResult` ൽ ടൂൾസിന്റെ പേര്, വിവരണം, ഇൻപുട്ട് ഘടനകൾ ഉൾപ്പെടെയുള്ള വിവരങ്ങൾ അടങ്ങിയിട്ടുണ്ട്

അടിസ്ഥാന ഫീച്ചറുകൾ കൈവശം വെച്ചിരിക്കുന്നു. എന്നാൽ ഇവ എപ്പോൾ ഉപയോഗിക്കണം? ഈ ക്ലയന്റ് ലളിതമാണ്; ഫീച്ചറുകൾ ഉപയോഗിക്കാൻ നിങ്ങൾ വ്യക്തമായി വിളിക്കണം. അടുത്ത അധ്യായത്തിൽ, സ്വന്തം വലിയ ഭാഷാമോഡൽ (LLM) ഉള്ള കൂടുതൽ സങ്കീർണ്ണ ക്ലയന്റ് സൃഷ്ടിക്കും. ഇപ്പോൾ സെർവറിലെ ഫീച്ചറുകൾ എങ്ങനെ വിളിക്കുന്നുവെന്നു നോക്കാം:

#### റസ്റ്റ്

പ്രധാന ഫംഗ്ഷനിൽ, ക്ലയന്റ് സജ്ജമാക്കിയതിന് ശേഷം സെർവർ ആരംഭിച്ച് ചില ഫീച്ചറുകൾ പട്ടികപ്പെടുത്താം.

```rust
// ആരംഭിക്കുക
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// ഉപകരണങ്ങളുടെ പട്ടിക
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ഫീച്ചറുകൾ Invoke ചെയ്യുക

ഫീച്ചറുകൾ invoke ചെയ്യാനായി ശരിയായ arguments, ചിലപ്പോൾ വിളിക്കാനുള്ള ഫീച്ചറിന്റെ പേര് നിർദ്ദിഷ്ടമാക്കേണ്ടതുണ്ട്.

#### ടൈപ്‌സ്‌ക്രിപ്റ്റ്

```typescript

// ഒരു റിസോഴ്‌സ് വായിക്കുക
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ഒരു ടൂൾ കോൾ ചെയ്യുക
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// പ്രാമ്പ്റ്റ് കോൾ ചെയ്യുക
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

മുൻകോഡിൽ:

- `readResource()` വിളിച്ച് ഒരു resource വായിച്ചു, അത് uri കൊടുത്ത് വിളിക്കുന്നു. സെർവർ സൈഡിലെ കോഡ് ഇങ്ങനെ കാണാം:

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

    ഞങ്ങളുടെ `uri` മൂല്യം `file://example.txt` സെർവറിൽ `file://{name}` ആയി పోలിക്കുന്നു. `example.txt` നാമമായി മാപ്പിംഗ് ചെയ്തു.

- ഒരു ടൂൾ വിളിക്കുന്നു, അതിന്റെ പേര്, അർഗുമെന്റുകൾ നൽകിയാണ് വിളിക്കുന്നത്:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- പ്രോംപ്റ്റ് ലഭിക്കാൻ `getPrompt()` സർവറിനു വേണ്ട പ്രോംപ്റ്റിന്റെ പേര്, അർഗുമെന്റുകൾ നൽകി വിളിക്കുന്നു. സെർവർ കോഡ് ഇങ്ങനെ:

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

    അതിനനുസരിച്ച് ക്ലയന്റ് കോഡ് ഇങ്ങനെ കാണിക്കും:

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
# ഒരു ഉറവിടം വായിക്കുക
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ഒരു ഉപകരണം വിളിക്കുക
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

മുൻകോഡിൽ:

- `greeting` എന്ന resource `read_resource` ഉപയോഗിച്ച് വിളിച്ചു
- `add` എന്ന ടൂൾ `call_tool` ഉപയോഗിച്ച് invoke ചെയ്തു

#### .NET

1. ടൂൾ വിളിക്കാൻ ഇത്തരം കോഡ് ചേർക്കാം:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. ഫലം പ്രിന്റ് ചെയ്യാൻ ഈ കോഡ് ഉപയോഗിക്കാം:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### ജാവ

```java
// വിവിധ കാൽക്കുലേറ്റർ ഉപകരണങ്ങൾ വിളിക്കുക
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

മുൻകോഡിൽ:

- `callTool()` പദത്തിൽ `CallToolRequest` ഓബ്ജക്റ്റുകളുമായി വിവിധ കള്കുലേറ്റർ ടൂളുകൾ invoked ചെയ്തു
- ഓരോ ടൂൾ വിളിയും ടൂൾ നാമവും ടൂൾ ആവശ്യമായ അർഗുമെന്റുകൾ `Map` രൂപത്തിലാണ് നൽകിയത്
- ടൂൾസിന് നിർദ്ദേശിക്കപ്പെട്ട നാമത്തിലുള്ള പാരാമീറ്ററുകൾ ആണ് നിരീക്ഷിക്കേണ്ടത് (ഉദാ, "a", "b")
- ഫലങ്ങൾ `CallToolResult` ഒബ്ജക്റ്റുകളായി സെർവറിൽ നിന്നുള്ള പ്രതികരണങ്ങൾ അടങ്ങിയാണ് ലഭിക്കുന്നത്

#### റസ്റ്റ്

```rust
// _ARGUMENTS = {"a": 3, "b": 2} ആയി add ഉപകരണം വിളിക്കുക
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

### -5- ക്ലയന്റ് റൺ ചെയ്യുക

ക്ലയന്റ് റൺ ചെയ്യാൻ, ടർമിനലിൽ താഴെ കമാൻഡ് ടൈപ്പ് ചെയ്യുക:

#### ടൈപ്‌സ്‌ക്രിപ്റ്റ്

*package.json*-ൽ "scripts" സെക്ഷനിൽ താഴെ ചേർക്കുക:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### പൈതൺ

താഴെ കൊടുത്ത കമാൻഡ് ഉപയോഗിച്ച് ക്ലയന്റ് വിളിക്കുക:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### ജാവ

ആദ്യമേ MCP സെർവർ `http://localhost:8080`ൽ പ്രവർത്തിക്കുന്നതായി ഉറപ്പാക്കുക. തുടർന്ന് ക്ലയന്റ് ഓടിക്കുക:

```bash
# നിങ്ങളുടെ പ്രോജക്റ്റ് നിർമ്മിക്കുക
./mvnw clean compile

# ക്ലയന്റിനെ ഓടിക്കുക
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

അല്ലെങ്കിൽ, സൊല്യൂഷൻ ഫോൾഡറിലുള്ള `03-GettingStarted\02-client\solution\java` പ്രോജക്ട് എല്ലാം ഓടിച്ചു കാണാം:

```bash
# പരിഹാര ഡയറക്ടറിയിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക
cd 03-GettingStarted/02-client/solution/java

# JAR നിർമ്മിക്കുകയും പ്രവർത്തിപ്പിക്കയും ചെയ്യുക
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### റസ്റ്റ്

```bash
cargo fmt
cargo run
```

## അസൈന്മെന്റ്

ഈ അസൈൻമെന്റിൽ, ഇപ്പോൾ പഠിച്ചിരിക്കുന്ന കാര്യങ്ങൾ ഉപയോഗിച്ച് നിങ്ങളുടെ സ്വന്തം ക്ലയന്റ് സൃഷ്ടിക്കേണ്ടതാണ്.

ഉപയോഗിക്കാവുന്ന ഒരു സെർവർ താഴെ കൊടുത്തിട്ടുണ്ട്, നിങ്ങളുടെ ക്ലയന്റ് കോഡ് ഉപയോഗിച്ച് ഇതിനു വിളിക്കാം. സെർവറിന് കൂടുതൽ സൗകര്യങ്ങൾ ചേർത്ത് അതിനെ കൂടുതൽ രസകരമാക്കാൻ ശ്രമിക്കുക.

### ടൈപ്‌സ്‌ക്രിപ്റ്റ്

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ഒരു MCP സെർവർ സൃഷ്ടിക്കൂ
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ഒരു കൂട്ടിച്ചേർക്കൽ ഉപകരണം ചേർക്കൂ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ഒരു ഗതിയുള്ള അഭിവാദക വിഭവം ചേർക്കൂ
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

// stdin-ൽ സന്ദേശങ്ങൾ സ്വീകരിക്കുകയും stdout-ൽ സന്ദേശങ്ങൾ അയക്കുകയും ആരംഭിക്കുക

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


# ഒരു കൂട്ടിച്ചേർക്കൽ ഉപകരണം ചേർക്കുക
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ഒരു ഡൈനാമിക് ഗ്രീറ്റിങ്ങ് റിസോഴ്സ് ചേർക്കുക
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

ഈ പ്രോജക്ട് കാണുക [പ്രോംപ്റ്റുകളും വിഭവങ്ങളും ചേർക്കുന്നതും](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

കൂടാതെ ഈ ലിങ്ക് പരിശോധിച്ച് [പ്രോംപ്റ്റുകളും വിഭവങ്ങളും invoke ചെയ്യുന്നതും](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) കാണാം.

### റസ്റ്റ്

[മുൻപത്തെ സെക്ഷനിൽ](../../../../03-GettingStarted/01-first-server) റസ്റ്റ് ഉപയോഗിച്ച് എളുപ്പം ഒരു MCP സെർവർ കസ്റ്റം സൃഷ്ടിക്കുന്നതും പഠിച്ചിട്ടുണ്ട്. അതിൽ കൂടി വികസിപ്പിക്കാം അല്ലെങ്കിൽ [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers) എന്ന ലിങ്കിൽ കൂടുതൽ റസ്റ്റ്-അടിസ്ഥാന MCP സെർവർ ഉദാഹരണങ്ങൾ കാണാം.

## സൊല്യൂഷൻ

**സൊല്യൂഷൻ ഫോൾഡർ** ഈ ട്യൂട്ടോറിയിൽ ഉൾപ്പെടുത്തിയ എല്ലാ ആശയങ്ങളും കാണിക്കുന്ന പൂർത്തിയായ, പ്രവർത്തനക്ഷമമായ ക്ലയന്റ് നിർവഹണങ്ങൾ അടങ്ങിയതാണ്. ഓരോ സൊല്യൂഷനും ക്ലയന്റ്, സെർവർ കോഡുകൾ സ്വതന്ത്രമായ പ്രോജക്ടുകളായി ക്രമീകരിച്ചിരിക്കുന്നു.

### 📁 സൊല്യൂഷൻ ഘടന

പ്രോഗ്രാമിംഗ് ഭാഷയെ അനുസരിച്ച് സൊല്യൂഷൻ ഡയറക്ടറി ക്രമീകരിച്ചിരിക്കുന്നു:

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

### 🚀 ഓരോ സൊല്യൂഷനിന്റെയും ഉള്ളടക്കം

ഓരോ ഭാഷാനിരീക്ഷണ സൊല്യൂഷനും താഴെ പറയുന്നതുകൾ ഉൾക്കൊള്ളുന്നു:

- ട്യൂട്ടോറിയിലുടെ കവർ ചെയ്ത എല്ലാ ഫീച്ചറുകളും ഉൾക്കൊള്ളുന്ന പൂർത്തിയാക്കിയ ക്ലയന്റ് നിർവഹണം
- ശരിയായ ഡിപ്പെൻഡൻസികളും കോൺഫിഗറേഷനും ഉള്ള പ്രവർത്തനക്ഷമമായ പ്രോജക്ട് ഘടന
- സജ്ജീകരണവും പ്രവർത്തിപ്പിക്കലും ലളിതമാക്കുന്ന നിർമ്മാണം, റൺ സ്ക്രിപ്റ്റുകൾ
- ഭാഷാനുസരിച്ച് വിശദമായ README ഫയലുകൾ
- പിശകുകൾ കൈകാര്യം ചെയ്യൽ, ഫലം പ്രോസസ്സ് ചെയ്യൽ ഉദാഹരണങ്ങൾ

### 📖 സൊല്യൂഷനുകൾ ഉപയോഗിക്കുക

1. നിങ്ങൾ ഇഷ്ടപ്പെടുന്ന ഭാഷ ഫോൾഡറിലേക്ക് പോകുക:

   ```bash
   cd solution/typescript/    # ടൈപ്പ്‌സ്‌ക്രിപ്റ്റ്‌ക്കായി
   cd solution/java/          # ജാവക്കായി
   cd solution/python/        # പൈത്തൺയ്ക്ക്
   cd solution/dotnet/        # .നെറ്റിനായി
   ```

2. ഓരോ ഫോൾഡറിലും README നിർദേശങ്ങൾ പാലിക്കുക:
   - ഡിപ്പെൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുക
   - പ്രോജക്ട് നിർമിക്കുക
   - ക്ലയന്റ് റൺ ചെയ്യുക

3. നിങ്ങൾ ഇത് പോലുള്ള ഔട്ട്പുട്ട് കാണും:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

പൂർണ്ണമായ ഡോക്യുമെന്റേഷനും വിശദമായ നിർദ്ദേശങ്ങളും ലഭിക്കാൻ: **[📖 സൊല്യൂഷൻ ഡോക്യുമെന്റേഷൻ](./solution/README.md)**

## 🎯 പൂർത്തിയാക്കിയ ഉദാഹരണങ്ങൾ

ഈ ട്യൂട്ടോറിയിലെ എല്ലാ പ്രോഗ്രാമിംഗ് ഭാഷകളിലും പൂർണ്ണമായ പ്രവര്‍ത്തനക്ഷമമായ ക്ലയന്റ് നിർവഹണങ്ങൾ ഞങ്ങൾ നൽകിയിട്ടുണ്ട്. ഇവ ഓർക്കാൻ, തങ്ങളുടെ സ്വന്തം പ്രോജക്ടുകൾ തുടങ്ങാൻ റഫറൻസ് ഇമ്പ്ലിമെന്റേഷനുകൾ ആയി ഉപയോഗിക്കാം.

### ലഭ്യമായ പൂർണ്ണ ഉദാഹരണങ്ങൾ

| ഭാഷ | ഫയൽ | വിവരണം |
|----------|------|-------------|
| **ജാവ** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് സമഗ്ര പിശക് കൈകാര്യംപ്പെടുത്തലുള്ള പൂർത്തിയാക്കിയ ജാവ ക്ലയന്റ് |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | സെർവർ സ്വയം സ്റ്റാർട്ട് ചെയ്യുന്ന stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് പൂർത്തിയാക്കിയ C# ക്ലയന്റ് |
| **ടൈപ്‌സ്‌ക്രിപ്റ്റ്** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP പ്രോട്ടോക്കോൾ പൂർണ്ണ പിന്തുണയുളള പൂർത്തിയാക്കിയ ടൈപ്‌സ്‌ക്രിപ്റ്റ് ക്ലയന്റ് |
| **പൈതൺ** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | അസിങ്ക്/അവൈറ്റ് പാറ്റേൺ ഉപയോഗിച്ച് പൂർത്തിയാക്കിയ പൈതൺ ക്ലയന്റ് |
| **റസ്റ്റ്** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | അസിങ്ക് പ്രവർത്തനങ്ങൾക്കായി ടോകിയോ ഉപയോഗിച്ചുള്ള പൂർത്തിയാക്കിയ റസ്റ്റ് ക്ലയന്റ് |

ഓരോ പൂർണ്ണ ഉദാഹരണവും ഉൾക്കൊള്ളുന്നത്:
- ✅ **കണക്ഷൻ സ്ഥാപിക്കൽ** மற்றும் പിശക് കൈകാര്യം ചെയ്യൽ  
- ✅ **സെർവർ കണ്ടെത്തൽ** (ഉപകരണങ്ങൾ, സ്രോതസ്സ്, ആവശ്യമായ പ്രോംപ്റ്റുകൾ)  
- ✅ **കല്കുലേറ്റർ പ്രവർത്തനങ്ങൾ** (കൂട്ടുക, കുറയ്ക്കുക, ഗുണിക്കുക, വിഭജിക്കുക, സഹായം)  
- ✅ **ഫലം പ്രോസസ്സ് ചെയ്യൽ** மற்றும் ഫോർമാറ്റ് ചെയ്യപ്പെട്ട ഔട്ട്പുട്ട്  
- ✅ **സമഗ്രമായ പിശക് കൈകാര്യം ചെയ്യൽ**  
- ✅ **ശുദ്ധമായ, രേഖപ്പെടുത്തിയ കോഡ്** ഘട്ടം ഘട്ടമായി കമന്റുകളോടെ  

### സമ്പൂർണ്ണ ഉദാഹരണങ്ങളുമായി തുടങ്ങിയതിന്

1. മുകളിൽ ടേബിളിൽ നിന്ന് **താങ്കളുടെ ഇഷ്ടഭാഷ തിരഞ്ഞെടുക്കുക**  
2. **സമ്പൂർണ്ണ ഉദാഹരണ ഫയൽ** അവലോകനം ചെയ്ത് പൂർണ്ണ നടപ്പിലാക്കല് മനസിലാക്കുക  
3. [`complete_examples.md`](./complete_examples.md) ൽ നൽകിയ അതിന്റെ നിർദേശങ്ങൾ പാലിച്ച് **ഉദാഹരണം നടത്തുക**  
4. താങ്കളുടെ പ്രത്യേക ഉപയോഗത്തിനു **ഉദാഹരണം തിരുത്തുകയും വികസിപ്പിക്കുകയും ചെയ്യുക**  

ഈ ഉദാഹരണങ്ങൾ പ്രവർത്തിപ്പിക്കാനും സ്വതന്ത്രമാക്കാനുമുള്ള വിശദമായ രേഖയ്ക്കായി കാണുക: **[📖 സമ്പൂർണ്ണ ഉദാഹരണങ്ങളുടെ ഡോക്യൂമെന്റേഷൻ](./complete_examples.md)**  

### 💡 പരിഹാരവും സമ്പൂർണ്ണ ഉദാഹരണങ്ങളും

| **പരിഹാര ഫോൾഡർ** | **സമ്പൂർണ്ണ ഉദാഹരണങ്ങൾ** |
|--------------------|-------------------------|
| നിർമ്മാണ ഫയലുകൾ അടങ്ങിയ പൂർണ്ണ പ്രൊജക്ട് ഘടന | ഏക ഫയൽ നടപ്പാക്കലുകൾ |  
| ആവശ്യകതകളോട് ഒരുങ്ങിയ പ്രവർത്തനപരമായി റണ്ണ് ചെയ്യാം | ലക്ഷ്യമിട്ട കോഡ് ഉദാഹരണങ്ങൾ |  
| പ്രൊഡക്ഷൻ പോലെ വിന്യാസം | വിദ്യാഭ്യാസ വിഷയം |  
| ഭാഷാപ്രധാന ടൂളിംഗ് | ഭിന്നഭാഷ താരതമ്യം |  

രണ്ടും വിലപ്പെട്ടവയാണ് - പൂർണ്ണ പ്രൊജക്ടുകള്കായി **പരിഹാര ഫോൾഡർ** ഉപയോഗിക്കുക, പഠനത്തോടും തിരികെ കാണുന്നതിനുമായി **സമ്പൂർണ്ണ ഉദാഹരണങ്ങൾ** ഉപയോഗിക്കാം.  

## പ്രധാന ഊഹങ്ങൾ  

ഈ അധ്യായത്തിൻറെ പ്രധാന ഊഹങ്ങൾ ക്ലയന്റുകളെ സംബന്ധിച്ച്:  

- സെർവറിൽ ഉള്ള ഫീച്ചറുകൾ കണ്ടെത്താനും വിളിക്കാനും ഉപയോഗിക്കാം.  
- ക്ലയന്റുകൾക്കും സേവനം തുടങ്ങുകയോ നേരത്തെ നടത്തുന്ന സെർവറുകളുമായി കണക്ഷൻ സ്ഥാപിക്കുകയോ സാധിക്കും (ഈ അധ്യായത്തിലെ പോലെ).  
- മുൻ അധ്യായത്തിൽ വിവരണം ചെയ്ത <i>ഇൻസ്പെക്ടർ</i> പോലുള്ള അന്യോപാധികളടക്കം, സെർവർ ശേഷികളും പരീക്ഷിക്കാൻ മികച്ച മാർഗമാണ്.  

## അധിക സ്രോതസ്സ്  

- [MCP-യിൽ ക്ലയന്റുകൾ നിർമ്മിക്കൽ](https://modelcontextprotocol.io/quickstart/client)  

## സാമ്പിൾസ്  

- [ജാവ കല്കുലേറ്റർ](../samples/java/calculator/README.md)  
- [.നെറ്റ് കല്കുലേറ്റർ](../../../../03-GettingStarted/samples/csharp)  
- [ജാവാസ്ക്രിപ്റ്റ് കല്കുലേറ്റർ](../samples/javascript/README.md)  
- [ടൈപ്പ്സ്ക്രിപ്റ്റ് കല്കുലേറ്റർ](../samples/typescript/README.md)  
- [പൈത്തൺ കല്കുലേറ്റർ](../../../../03-GettingStarted/samples/python)  
- [റസ്റ്റ് കല്കുലേറ്റർ](../../../../03-GettingStarted/samples/rust)  

## എതിർവശം  

- അടുത്തത്: [LLM ഉപയോഗിച്ച് ക്ലയന്റ് സൃഷ്ടിക്കൽ](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**വിവരണം**:  
ഈ ഡോക്യുമെന്റായിരുന്നത് AI വിവർത്തനം സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നമുക്ക് കൃത്യതക്കായി ശ്രമിക്കുമ്പോഴും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ ദോഷങ്ങളോ തെറ്റായ വിവരങ്ങളോ ഉണ്ടായേക്കാമെന്ന് ദയവായി മനസിലാക്കുക. മാതൃഭാഷാ ആസലീ ഡോക്യുമെന്റാണ് പ്രാമാണികമായ ഉറവിടം എന്നും കരുതണം. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യാനുവാദം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗം മൂലം ഉണ്ടായേതായ തെറ്റുകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->