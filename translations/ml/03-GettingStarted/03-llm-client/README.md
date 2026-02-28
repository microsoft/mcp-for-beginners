# LLM ഉപയോഗിച്ച് ഒരു ക്ലയന്റ് സൃഷ്ടിക്കൽ

ഇപ്പോൾ വരെ, നിങ്ങൾ ഒരു സെർവർയും ഒരു ക്ലയന്റും എങ്ങനെ സൃഷ്ടിക്കാമെന്ന് കാണിച്ചു. ക്ലയന്റ് വ്യക്തമായി സെർവറിനെ വിളിച്ച് അതിന്റെ ടൂളുകൾ, റിസോഴ്‌സുകൾ, പ്രോമ്റ്റുകൾ പട്ടികപ്പെടുത്തിയിരുന്നു. എന്നിരുന്നാലും, ഇത് വളരെ പ്രായോഗികമായ സമീപനം അല്ല. നിങ്ങളുടെ ഉപയോക്താക്കൾ ഏജൻസിക്കാലത്ത് ജീവിക്കുന്നു, പ്രോമ്റ്റുകൾ ഉപയോഗിക്കുകയും LLM-ഉം ആശയവിനിമയം നടത്തുകയും ചെയ്യാനാണ് അവർ പ്രതീക്ഷിക്കുന്നത്. നിങ്ങളുടെ കഴിവുകൾ സൂക്ഷിക്കാൻ MCP ഉപയോഗിക്കുന്നുവോ എന്നത് അവർക്ക് കാര്യമില്ല; അവർ പ്രകൃതിസഹജമായ ഭാഷ ഉപയോഗിച്ച് ആശയവിനിമയം മാത്രമാണ് പ്രതീക്ഷിക്കുന്നത്. അത്ഹേകിൽ, ഇത് എങ്ങിനെ പരിഹരിക്കാം? പരിഹാരം, ക്ലയന്റിലേക്ക് ഒരു LLM ചേർക്കുന്നതാണ്.

## അവലോകനം

ഈ പാഠത്തിൽ, ഞങ്ങൾ നിങ്ങളുടെ ക്ലയന്റിൽ ഒരു LLM എങ്ങനെ ചേർക്കുമെന്ന് ശ്രദ്ധിക്കുകയും ഇത് ഉപയോക്താവിന് എങ്ങനെ മെച്ചപ്പെട്ട അനുഭവം നൽകുന്നുവെന്ന് കാണിക്കുകയും ചെയ്യുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കുമ്പോൾ, നിങ്ങൾ ഇതെല്ലാം ചെയ്യും:

- ഒരു LLM ഉള്ള ക്ലയന്റ് സൃഷ്ടിക്കുക.
- LLM ഉപയോഗിച്ച് MCP സെർവറിനോട് നിസ്സംബന്ധമായി പ്രവർത്തിക്കുക.
- ക്ലയന്റ് വശത്ത് മെച്ചപ്പെട്ട ഉപയോക്തൃ അനുഭവം നൽകുക.

## സമീപനം

ഞങ്ങൾ എടുക്കേണ്ട സമീപനം മനസ്സിലാക്കാം. LLM ചേർക്കുന്നത് ലളിതമായി തോന്നുന്നു, എന്നാൽ നാം വാസ്തവത്തിൽ ഇത് ചെയ്യും?

ഇവിടെ ക്ലയന്റ് സെർവറിനോടെയും എങ്ങനെ ഇടപെടുമെന്ന് കാണാം:

1. സെർവറുമായി ബന്ധം സ്ഥാപിക്കുക.

2. കഴിവുകൾ, പ്രോമ്റ്റുകൾ, റിസോഴ്‌സുകൾ, ടൂളുകൾ പട്ടികപ്പെടുത്തുക, അവയുടെ സ്കീമാ ചിട്ടപ്പെടുത്തുക.

3. ഒരു LLM ചേർത്ത്, സൂക്ഷിച്ചിരിക്കുന്ന കഴിവുകളും അവയുടെ സ്കീമയും LLM മനസ്സിലാക്കുന്ന പടിയായി നൽകുക.

4. ഉപയോക്താവിന്റെ പ്രോമ്റ്റ് കൈകാര്യം ചെയ്യുമ്പോൾ, അതിനെ LLM-യ്ക്ക് കൈമാറുക ഒപ്പം ക്ലയന്റ് പട്ടികപ്പെടുത്തിയ ടൂളുകളും.

നല്ലത്, ഇപ്പോൾ നാം ഉയർന്ന തലത്തിൽ എങ്ങനെ ചെയ്യാമെന്ന് മനസ്സിലായിരിക്കുന്നു, താഴെ വെച്ചിരിക്കുന്ന അഭ്യാസത്തിൽ ഇത് പരീക്ഷിക്കാം.

## അഭ്യാസം: LLM ഉള്ള ക്ലയന്റ് സൃഷ്ടിക്കൽ

ഈ അഭ്യാസത്തിൽ, ഞങ്ങൾ നമ്മുടെ ക്ലയന്റിലേക്ക് ഒരു LLM ചേർക്കാൻ പഠിക്കും.

### GitHub Personal Access Token ഉപയോഗിച്ച് അംഗീകാരം

GitHub ടോക്കൺ സൃഷ്ടിക്കുന്നത് നേരിട്ടുള്ള പ്രക്രിയയാണ്. ഇങ്ങനെ ചെയ്യാം:

- GitHub സെറ്റിംഗ്സിലേക്ക് പോവുക – മുകളിൽ വലതുഭാഗത്തെ നിങ്ങളുടെ പ്രൊഫൈൽ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്ത് Settings തിരഞ്ഞെടുക്കുക.
- Developer Settings ലേക്ക് നാവിഗേറ്റ് ചെയ്യുക – താഴേക്ക് സ്ക്രോൾ ചെയ്ത് Developer Settings ക്ലിക്ക് ചെയ്യുക.
- Personal Access Tokens തിരഞ്ഞെടുക്കുക – Fine-grained tokens ക്ലിക്ക് ചെയ്ത് Generate new token തിരഞ്ഞെടുക്കുക.
- നിങ്ങളുടെ ടോക്കൺ ക്രമീകരിക്കുക – റഫറൻസ് കുറിപ്പ് ചേർക്കുക, കാലഹരണ തീയതി സജ്ജമാക്കുക, ആവശ്യമായ സ്കോപ്പുകൾ (അനുമതികൾ) തിരഞ്ഞെടുക്കുക. ഈ സാഹചര്യത്തിൽ Models അനുമതികൾ ചേർക്കുക.
- ടോക്കൺ ജനറേറ്റ് ചെയ്ത് കോപ്പി ചെയ്യുക – Generate token ക്ലിക്ക് ചെയ്യുക, ഉടനടി കോപ്പി ചെയ്യണം, പിന്നീട് അത് കാണാനാകില്ല.

### -1- സെർവറുമായി കണക്ട്‌ചെയ്യുക

ആദ്യം, നമ്മുടെ ക്ലയന്റ് സൃഷ്ടിക്കാം:

#### ടൈപ്പ്‌സ്‌ക്രിപ്റ്റ്

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // സ്കീമാ സാധുത പരിശോധനയ്ക്കായി zod ഇറക്കുമതി ചെയ്യുക

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", 
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }
}
```

മുൻകാല കോഡിൽ നാം:

- ആവശ്യമായ ലൈബ്രറികൾ ഇമ്പോർട്ട് ചെയ്തു
- `client` എന്നതും `openai` എന്നതും ഉള്ള ക്ലാസ് സൃഷ്ടിച്ചു, ഇതുവഴി ക്ലയന്റ് മാനേജ് ചെയ്യാനും LLM-ുമായി ആശയവിനിമയം നടത്താനും സഹായിക്കും.
- GitHub Models ഉപയോഗിക്കാൻ `baseUrl` സെറ്റ് ചെയ്ത് LLM ഇൻസ്റ്റൻസ് ക്രമീകരിച്ചു.

#### പൈതൺ

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# സ്റ്റ്ഡിയോ കണക്ഷനിനുള്ള സർവാർ പാരാമീറ്ററുകൾ സൃഷ്‌ടിക്കുക
server_params = StdioServerParameters(
    command="mcp",  # എക്സിക്യുട്ടബിൾ
    args=["run", "server.py"],  # ഓപ്ഷണൽ കമാൻഡ് ലൈൻ_ARGUMENTS
    env=None,  # ഓപ്ഷണൽ പരിസ്ഥിതി ചേരുവകൾ
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # കണക്ഷൻ പ്രാരംഭീകരിക്കുക
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

മുൻകാല കോഡിൽ നാം:

- MCP-യ്ക്ക് ആവശ്യമായ ലൈബ്രറികൾ ഇമ്പോർട്ട് ചെയ്തു
- ഒരു ക്ലയന്റ് സൃഷ്ടിച്ചു

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### ജാവ 

ആദ്യമായി, നിങ്ങളുടെ `pom.xml` ഫയലിൽ LangChain4j ആശ്രിതങ്ങൾ ചേർക്കണം. MCP ഇന്റഗ്രേഷൻ GitHub Models പിന്തുണEnabled്ക്കാൻ ഈ ആശ്രിതങ്ങൾ ചേർക്കുക:

```xml
<properties>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
</properties>

<dependencies>
    <!-- LangChain4j MCP Integration -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-mcp</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- OpenAI Official API Client -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-open-ai-official</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- GitHub Models Support -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-github-models</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

അടുത്തതായി, നിങ്ങളുടെ ജാവ ക്ലയന്റ് ക്ലാസ് സൃഷ്ടിക്കുക:

```java
import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // GitHub മോഡലുകൾ ഉപയോഗിക്കാൻ LLM കോൺഫിഗർ ചെയ്യുക
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // സർവറുമായി ബന്ധിപ്പിക്കാൻ MCP ട്രാൻസ്പോർട്ട് സൃഷ്‌ടിക്കുക
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ക്ലയന്റ് സൃഷ്‌ടിക്കുക
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

മുൻകാല കോഡിൽ നാം:

- **LangChain4j ആശ്രിതങ്ങൾ ചേർത്തു**: MCP ഇന്റഗ്രേഷൻ, OpenAI ഔദ്യോഗിക ക്ലയന്റ്, GitHub Models പിന്തുണയ്ക്കും
- **LangChain4j ലൈബ്രറികൾ ഇമ്പോർട്ട് ചെയ്തു**: MCP ഇന്റഗ്രേഷൻ, OpenAI ചാറ്റ് മോഡൽ ഫംഗ്ഷണാലിറ്റിക്ക്
- **`ChatLanguageModel` സൃഷ്ടിച്ചു**: GitHub Models-നൊപ്പം നിങ്ങളുടെ GitHub ടോക്കൺ ഉപയോഗിച്ച് ക്രമീകരിച്ചു
- **HTTP ട്രാൻസ്പോർട്ട് സേവർ-സെൻറ് ഇവന്റുകൾ (SSE) ഉപയോഗിച്ച് ക്രമീകരിച്ചു** MCP സെർവറുമായി കണക്ട് ചെയ്യാൻ
- **MCP ക്ലയന്റ് സൃഷ്ടിച്ചു**: സെർവർ ആശയവിനിമയം കൈകാര്യം ചെയ്യുന്നതിന്
- **LangChain4j-ന്റെ ബിൽറ്റ്-ഇൻ MCP പിന്തുണ ഉപയോഗിച്ചു**: LLM-കളും MCP സെർവറുകളും ഇന്റഗ്രേറ്റ് ചെയ്യുന്നത് ലളിതമാക്കുന്നു

#### റസ്റ്റ്

ഈ ഉദാഹരണം Rust അടിസ്ഥാനമാക്കിയ MCP സെർവർ പ്രവർത്തനസജ്ജമാണെന്ന് പരിഗണിക്കുന്നു. ഇല്ലെങ്കിൽ, [01-first-server](../01-first-server/README.md) പാഠം വായിച്ച് സെർവർ സൃഷ്ടിക്കുക.

Rust MCP സെർവർ ലഭ്യമായാൽ, ടെർമിനൽ തുറന്നു സെർവറിന്റെ ഡയറെക്ടറിയിലേക്ക് പോകുക. തുടർന്ന് പുതിയ LLM ക്ലയന്റ് പ്രോജെക്ട് സൃഷ്ടിക്കാൻ താഴെ കൊടുത്ത കമാൻഡ് പ്രവർത്തിപ്പിക്കുക:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` ഫയലിൽ താഴെ ആശ്രിതങ്ങൾ ചേർക്കുക:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> ഔദ്യോഗിക Rust OpenAI ലൈബ്രറി ഇല്ലാത്തതിനാൽ, `async-openai` ക്രേറ്റ് ഒരു [സമൂഹപ്രതിരക്ഷിത ലൈബ്രറി](https://platform.openai.com/docs/libraries/rust#rust) ആണ്, സാധാരണയായി ഉപയോഗിക്കുന്നത്.

`src/main.rs` ഫയൽ തുറക്കു, ഉള്ളടക്കം താഴെ കൊടുത്ത കോഡിൽ മാറ്റുക:

```rust
use async_openai::{Client, config::OpenAIConfig};
use rmcp::{
    RmcpError,
    model::{CallToolRequestParam, ListToolsResult},
    service::{RoleClient, RunningService, ServiceExt},
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use serde_json::{Value, json};
use std::error::Error;
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // ആദിത്യ സന്ദേശം
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ക്ലയന്റ് ക്രമീകരിക്കുക
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ക്ലയന്റ് ക്രമീകരിക്കുക
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("calculator-server");

    let mcp_client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: MCP ടൂൾ ലിസ്റ്റിംഗ് നേടുക

    // TODO: ടൂളുകളുടെ വിളികളുമായി LLM സംവാദം

    Ok(())
}
```

ഈ കോഡ് ഒരു അടിസ്ഥാന Rust അപ്ലിക്കേഷൻ ക്രമീകരിക്കുന്നു, MCP സെർവറും GitHub Models ഉപയോഗിച്ച് LLM ഇടപെടലും നടത്താൻ.

> [!IMPORTANT]
> അപേക്ഷ പ്രവർത്തിപ്പിക്കാൻ മുമ്പ് `OPENAI_API_KEY` എന്വയിറൺമെന്റ്VARIABLE-ൽ നിങ്ങളുടെ GitHub ടോക്കൺ സജ്ജമാക്കുക.

നല്ലത്, അടുത്ത ഘട്ടം, സെർവറിന്റെ കഴിവുകൾ പട്ടികപ്പെടുത്തുക.

### -2- സെർവർ കഴിവുകൾ പട്ടികപ്പെടുത്തുക

ഇപ്പോൾ സെർവറുമായി കണക്റ്റ് ചെയ്ത് അതിന്റെ കഴിവുകൾ ചോദിക്കാം:

#### ടൈപ്പ്‌സ്‌ക്രിപ്റ്റ്

അരെ ക്ലാസിൽ താഴെ കൊടുത്ത മെത്തഡുകൾ ചേർക്കുക:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ഉപകരണങ്ങൾ ലിസ്റ്റുചെയ്യുന്നു
    const toolsResult = await this.client.listTools();
}
```

മുൻകാല കോഡിൽ നാം:

- സെർവറുമായി കണക്റ്റ് ചെയ്യാനുള്ള `connectToServer` കോഡ് ചേർത്തു.
- `run` മെത്തഡ് സൃഷ്ടിച്ചു, ആപ്പ് ഫ്ലോ കൈകാര്യം ചെയ്യുന്നതിന്. ഇദ്ദേഹം ഇപ്പോൾ ടൂളുകൾ only പട്ടികപ്പെടുത്തുന്നു, ചുരുക്കത്തിൽ ഇതിൽ കൂടുതൽ ചേർക്കും.

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
    print("Tool", tool.inputSchema["properties"])
```

ഞങ്ങൾ ചേർത്തത്:

- റിസോഴ്‌സുകളും ടൂളുകളും പട്ടികപ്പെടുത്തി, പ്രിന്റ് ചെയ്തു. ടൂളുകൾക്കായി നാം പിന്നീട് ഉപയോഗിക്കുന്ന `inputSchema`യും പട്ടികപ്പെടുത്തി.

#### .NET

```csharp
async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        // TODO: convert tool definition from MCP tool to LLm tool     
    }

    return toolDefinitions;
}
```

മുദ്രിച്ചുക:

- MCP സെർവറിലുള്ള ടൂളുകളെ പട്ടികപ്പെടുത്തി
- ഓരോ ടൂൾക്കും പേര്, വിവരണം, അവയുടെ സ്കീമ ഇത് തുടര്‍ന്ന് ഉപയോഗിക്കാനായി

#### ജാവ

```java
// MCP ടൂളുകൾ സ്വയമേവ കണ്ടെത്തുന്ന ഒരു ടൂൾ പ്രൊവൈഡർ ഉണ്ടാക്കുക
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ടൂൾ പ്രൊവൈഡർ സ്വയമേവ കൈകാര്യം ചെയ്യുന്നത്:
// - MCP സർവറായി ലഭ്യമായ ടൂളുകളുടെ പട്ടിക ഒരുക്കൽ
// - MCP ടൂൾ സ്കീമികളെ LangChain4j ഫോർമാറ്റിലേക്ക് മാറ്റൽ
// - ടൂൾ പ്രവർത്തനവും പ്രതികരണങ്ങളും നിയന്ത്രിക്കൽ
```

മുൻകാല കോഡിൽ:

- MCP ടൂളുകൾ സാധാരണയായി കണ്ടെത്തിയും രജിസ്റ്ററുചെയ്യുമായി `McpToolProvider` സൃഷ്ടിച്ചു
- MCP ടൂൾ സ്കീമകളും LangChain4j ടൂൾ ഫോർമാറ്റും ഇന്റേണലായി പരിവർത്തനം ചെയ്യുന്നു
- മാനുവൽ ടൂൾ പട്ടികാനവും പരിവർത്തനവും മറച്ച് ഈ സമീപനം സ്വയം ചെയ്യുന്നു

#### റസ്റ്റ്

MCP സെർവറിൽ നിന്നും ടൂളുകൾ സ്വീകരിക്കുന്നത് `list_tools` മെത്തഡ് ഉപയോഗിച്ച്. `main` ഫംഗ്ഷനിൽ MCP ക്ലയന്റ് ക്രമീകരിച്ചതിനു ശേഷം താഴെ കൊടുത്ത കോഡ് ചേർക്കുക:

```rust
// MCP ഉപകരണ ലിസ്റ്റിംഗ് നേടുക
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- സെർവർ കഴിവുകൾ LLM ടൂളുകളായി മാറ്റുക

സെർവർ കഴിവുകൾ പട്ടികപ്പെടുത്തിയതിന് ശേഷം അതിനെ LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്കു മാറ്റാം. ഇത് ചെയ്താൽ കഴിവുകൾ ടൂളുകളായി LLM-ന് നൽകാനാകും.

#### ടൈപ്പ്‌സ്‌ക്രിപ്റ്റ്

1. MCP സെർവർ പ്രതികരണത്തെ LLM ഉപയോഗിക്കുന്ന ടൂൾ ഫോർമാറ്റിലേക്കു മാറ്റാൻ താഴെ കൊടുത്ത കോഡ് ചേർക്കൂ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema അടിസ്ഥാനമാക്കി ഒരു zod സ്കീമ സൃഷ്ടിക്കുക
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ടൈപ്പ് "function" എന്നാക്കി വ്യക്തമായി സജ്ജമാക്കുക
            function: {
            name: tool.name,
            description: tool.description,
            parameters: {
            type: "object",
            properties: tool.input_schema.properties,
            required: tool.input_schema.required,
            },
            },
        };
    }

    ```

    മുകളിൽ കാണുന്ന കോഡ് MCP സെർവർ പ്രതികരണം എടുത്ത് അത് LLM മനസ്സിലാക്കുന്ന ടൂൾ നിർവചന ഫോർമാറ്റിലേക്ക് പരിവർത്തനം ചെയ്യുന്നു.

1. പിന്നീട്, `run` മെത്തഡ് അപ്ഡേറ്റ് ചെയ്ത് സെർവർ കഴിവുകൾ പട്ടികപ്പെടുത്താം:

    ```typescript
    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
            });
        });
    }
    ```

    ഇവിടെ `run` മെത്തഡ് അപ്ഡേറ്റ് ചെയ്തു, ഫലം വഴി മാറി ഓരോ എൻട്രിക്കും `openAiToolAdapter` വിളിക്കുന്നു.

#### പൈതൺ

1. ആദ്യം, താഴെ കൊടുത്ത പരിവർത്തന ഫംഗ്ഷൻ സൃഷ്ടിക്കാം:

    ```python
    def convert_to_llm_tool(tool):
        tool_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "type": "function",
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema["properties"]
                }
            }
        }

        return tool_schema
    ```

    `convert_to_llm_tools` ഫംഗ്ഷനിൽ, MCP ടൂൾ പ്രതികരണം എടുത്ത് അത് LLMക്ക് മനസ്സിലാക്കാവുന്ന ഫോർമാറ്റിൽ മാറ്റുന്നു.

1. തുടർന്ന്, ക്ലയന്റ് കോഡ് അപ്ഡേറ്റ് ചെയ്ത് ഈ ഫംഗ്ഷൻ ഉപയോഗിക്കാം:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ഇവിടെ MCP ടൂൾ പ്രതികരണം LLM-ന് നൽകുന്നതിന് `convert_to_llm_tool` വിളിക്കുന്നു.

#### .NET

1. MCP ടൂൾ പ്രതികരണം LLM മനസ്സിലാക്കുന്നതായി മാറ്റാൻ താഴെ കൊടുത്ത കോഡ് ചേർക്കൂ:

```csharp
ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}
```

മുമ്പ് നാം:

- `ConvertFrom` ഫംഗ്ഷൻ സൃഷ്ടിച്ചു, പേര്, വിവരണം, ഇൻപുട്ട് സ്കീമ സ്വീകരിക്കുന്നു.
- ഫംഗ്ഷനിന്റെ നിർവചനത്തിൽ `FunctionDefinition` സൃഷ്ടിച്ച് അത് `ChatCompletionsDefinition`-ലേക്ക് നൽകുന്നു. ഇത് LLMക്ക് മനസ്സിലാക്കാവുന്നതാണ്.

1. നിലവിലുള്ള കോഡ് ഈ ഫംഗ്ഷൻ ഉപയോഗിക്കാൻ മാറ്റാം:

    ```csharp
    async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            JsonElement propertiesElement;
            tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

            var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);

            Console.WriteLine($"Properties: {propertiesElement}");        
        }

        return toolDefinitions;
    }
    ```    In the preceding code, we've:

    - Update the function to convert the MCP tool response to an LLm tool. Let's highlight the code we added:

        ```csharp
        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
        ```

        The input schema is part of the tool response but on the "properties" attribute, so we need to extract. Furthermore, we now call `ConvertFrom` with the tool details. Now we've done the heavy lifting, let's see how it call comes together as we handle a user prompt next.

#### ജാവ

```java
// സ്വാഭാവിക ഭാഷാ ഇടപാട്ടിനായി ബോട്ട് ഇന്റർഫേസ് സൃഷ്ടിക്കുക
public interface Bot {
    String chat(String prompt);
}

// LLMയും MCP ടൂളുകളും ഉപയോഗിച്ച് AI സേവനം ക്രമീകരിക്കുക
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

മുമ്പ് നാം:

- സ്വാഭാവിക ഭാഷാ സംസാരം നടത്താൻ ഒരു ലളിതമായ `Bot` ഇന്റർഫേസ് നിർവചിച്ചു
- LangChain4jന്‍റെ `AiServices` ഉപയോഗിച്ച് LLM MCP ടൂൾ പ്രൊവൈഡറോട് ആ അറ്റോമാറ്റിക് ബൈൻഡിംഗ് നടത്തി
- ടൂൾ സ്കീമ പരിവർത്തനവും ഫംഗ്ഷൻ കോളിംഗും ഫ്രെയിംവർക്ക് എടുത്തുകൊണ്ടുവന്നതു
- മാനുവൽ ടൂൾ പരിവർത്തനം ഒഴിവാക്കി, MCP ടൂളുകൾ LLM-க்கு അനുയോജ്യമായ ഫോർമാറ്റ് ലാംഗ്ചെയിൻ4ജ്ജ് കൈകാര്യം ചെയ്യുന്നു.

#### റസ്റ്റ്

MCP ടൂൾ പ്രതികരണം LLM മനസ്സിലാക്കാവുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റാൻ സഹായകമായ ഒരു ഫംഗ്ഷൻ ചേർക്കാം, ടൂളുകളുടെ പട്ടികഫോർമാറ്റു നിർവചിക്കുന്നു. `main` ഫംഗ്ഷനു താഴെ താഴെ കൊടുത്ത കോഡ് ചേർക്കുക, ഇത് LLM-ന് അഭ്യർഥനകൾ അയയ്ക്കുമ്പോൾ വിളിക്കും:

```rust
async fn format_tools(tools: &ListToolsResult) -> Result<Vec<Value>, Box<dyn Error>> {
    let tools_json = serde_json::to_value(tools)?;
    let Some(tools_array) = tools_json.get("tools").and_then(|t| t.as_array()) else {
        return Ok(vec![]);
    };

    let formatted_tools = tools_array
        .iter()
        .filter_map(|tool| {
            let name = tool.get("name")?.as_str()?;
            let description = tool.get("description")?.as_str()?;
            let schema = tool.get("inputSchema")?;

            Some(json!({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": {
                        "type": "object",
                        "properties": schema.get("properties").unwrap_or(&json!({})),
                        "required": schema.get("required").unwrap_or(&json!([]))
                    }
                }
            }))
        })
        .collect();

    Ok(formatted_tools)
}
```

നന്നായി, ഉപയോക്തൃ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യാനായി നമുക്ക് മുന്നോട്ട് പോകാം.

### -4- ഉപയോക്തൃ പ്രോമ്റ്റ് അഭ്യർത്ഥന കൈകാര്യം ചെയ്യുക

ഇവിടെ ഉപയോക്താവിന്റെ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യാം.

#### ടൈപ്പ്‌സ്‌ക്രിപ്റ്റ്

1. LLM വിളിക്കാൻ ഉപയോഗിക്കുന്ന ഒരു മെത്തഡ് ചേർക്കുക:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. സേർവറിന്റെ ടൂളിനെ വിളിക്കുക
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ഫലത്തോടൊപ്പം എന്തെങ്കിലും ചെയ്യുക
        // TODO

        }
    }
    ```

    മുൻകാലത്തിൽ നാം:

    - `callTools` എന്ന മെത്തഡ് ചേർത്തു.
    - മെത്തഡ് LLM പ്രതികരണം പരിശോധിച്ച് എത്രയും ടൂളുകൾ വിളിച്ചിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുന്നു:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ഉപകരണം വിളിക്കല്‍
        }
        ```

    - LLM ടൂൾ വിളിക്കണം എന്ന് സൂചിപ്പിച്ചാൽ ടൂൾ വിളിക്കുന്നു:

        ```typescript
        // 2. സെർവർ ടൂളിനെ കോളുചെയ്യുക
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ഫലത്തിൽ നിന്നുള്ള ഏതെങ്കിലും പ്രവർത്തനം ചെയ്യുക
        // ചെയ്യേണ്ടതുണ്ട്
        ```

1. `run` മെത്തഡ് LLM വിളി ഉൾപ്പെടുത്തുന്നതിന് അപ്ഡേറ്റ് ചെയ്യാം:

    ```typescript

    // 1. LLM-ന് ഇൻപുട്ട് ആയി ഉള്ള സന്ദേശങ്ങൾ സൃഷ്ടിക്കുക
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM-നെ വിളിക്കൽ
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM പ്രതികരണം പരിശോധിക്കുക, ഓരോ തിരഞ്ഞെടുപ്പും ടൂൾ കോളുകൾ ഉണ്ടോയെന്ന് പരിശോധിക്കുക
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

നല്ലത്, മുഴുവൻ കോഡ് താഴെ കാണൂ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // സ്കീമ വാലിഡേഷൻക്കായി zod ഇറക്കുമതി ചെയ്യുക

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ഭാവിയിൽ ഈ URL-ൽ മാറ്റേണ്ടി വരാമ്: https://models.github.ai/inference
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }

    async connectToServer(transport: Transport) {
        await this.client.connect(transport);
        this.run();
        console.error("MCPClient started on stdin/stdout");
    }

    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
          }) {
          // input_schema അടിസ്ഥാനമാക്കി ഒരു zod സ്കീമ സൃഷ്ടിക്കുക
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ടൈപ്പ് സുതാര്യമായി "function" ആക്കുക
            function: {
              name: tool.name,
              description: tool.description,
              parameters: {
              type: "object",
              properties: tool.input_schema.properties,
              required: tool.input_schema.required,
              },
            },
          };
    }
    
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
      ) {
        for (const tool_call of tool_calls) {
          const toolName = tool_call.function.name;
          const args = tool_call.function.arguments;
    
          console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);
    
    
          // 2. സർവറിന്റെ ഉപകരണം വിളിക്കുക
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ഫലത്തെപ്പറ്റി എന്തെങ്കിലും ചെയ്യുക
          // TODO
    
         }
    }

    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
              name: tool.name,
              description: tool.description,
              input_schema: tool.inputSchema,
            });
        });

        const prompt = "What is the sum of 2 and 3?";
    
        const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

        console.log("Querying LLM: ", messages[0].content);
        let response = this.openai.chat.completions.create({
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM പ്രതികരണം വായിക്കുക, ഓരോ തിരഞ്ഞെടുപ്പിനും ഉപകരണം വിളികൾ ഉണ്ടോയെന്ന് പരിശോധിക്കുക
        (await response).choices.map(async (choice: { message: any; }) => {
          const message = choice.message;
          if (message.tool_calls) {
              console.log("Making tool call")
              await this.callTools(message.tool_calls, results);
          }
        });
    }
    
}

let client = new MyClient();
 const transport = new StdioClientTransport({
            command: "node",
            args: ["./build/index.js"]
        });

client.connectToServer(transport);
```

#### പൈതൺ

1. LLM വിളിക്കാൻ ആവശ്യമായ ഇമ്പോർട്ടുകൾ ചേർക്കാം:

    ```python
    # എല്‍എല്‍എം
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. LLM വിളിക്കുന്ന ഫംഗ്ഷൻ ചേർക്കുക:

    ```python
    # ല്ലം

    def call_llm(prompt, functions):
        token = os.environ["GITHUB_TOKEN"]
        endpoint = "https://models.inference.ai.azure.com"

        model_name = "gpt-4o"

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        print("CALLING LLM")
        response = client.complete(
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant.",
                },
                {
                "role": "user",
                "content": prompt,
                },
            ],
            model=model_name,
            tools = functions,
            # എളുപ്പത്തിലുള്ള പരാമീറ്ററുകൾ
            temperature=1.,
            max_tokens=1000,
            top_p=1.    
        )

        response_message = response.choices[0].message
        
        functions_to_call = []

        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                print("TOOL: ", tool_call)
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                functions_to_call.append({ "name": name, "args": args })

        return functions_to_call
    ```

ഇവിടെ നമ്മൾ:

- MCP സെർവറിലെ ഫംഗ്ഷനുകൾ LLM-ക്ക് നൽകി.
- പിന്നീട് LLM ആ ഫംഗ്ഷനുകളോടെയും വിളിച്ചു.
- ഫലവും പരിശോധിച്ച് എങ്കിൽ ഏത് ഫംഗ്ഷനുകൾ വിളിക്കണം എന്ന് കണ്ടു.
- ഒടുവിൽ വിളിക്കേണ്ട ഫംഗ്ഷനുകളുടെ ലിസ്റ്റ് പാസ്സു ചെയ്തു.

1. അവസാനത്തേടി, പ്രധാന കോഡ് അപ്ഡേറ്റ് ചെയ്യാം:

    ```python
    prompt = "Add 2 to 20"

    # എൽഎല്ല്എം അനുമതി നൽകിയ എല്ലാറ്റools കണ്ണിയുള്ളവ, എങ്കിൽ ഏത് ചോദിക്കുക
    functions_to_call = call_llm(prompt, functions)

    # നിർദേശിച്ച ഫംഗ്ഷനുകൾ വിളിക്കുക
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

മുൻകാല കോഡ്:

- LLM-ന്റെ നിർദ്ദേശ പ്രകാരം MCP ടൂൾ `call_tool` വഴി വിളിച്ചു.
- ടൂൾ വിളിയുടെ ഫലം MCP സെർവറിൽ പ്രിന്റ് ചെയ്തു.

#### .NET

1. LLM പ്രോമ്റ്റ് അഭ്യർത്ഥനയ്ക്ക് ഉദാഹരണം:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new ChatRequestUserMessage(userMessage));

    // 1. Define tools
    ChatCompletionsToolDefinition def = CreateToolDefinition();


    // 2. Define options, including the tools
    var options = new ChatCompletionsOptions(chatHistory)
    {
        Model = "gpt-4.1-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

ഇവിടെ:

- MCP സെർവറിൽ നിന്നുള്ള ടൂളുകൾ നേടി, `var tools = await GetMcpTools()`.
- ഉപയോക്തൃ പ്രോമ്റ്റ് `userMessage` നിർവഹിച്ചു.
- മോഡൽ, ടൂളുകൾ അടങ്ങിയ ഓപ്ഷൻസ് ഒബ്‌ജെക്റ്റ് ഉണ്ടാക്കി.
- LLM-ന് അഭ്യർത്ഥന അയച്ചതു.

1. ഒന്ന് കൂടി, LLM വിളിക്കേണ്ട ഫംഗ്ഷൻ ആണോ എന്ന് പരിശോധിക്കുക:

    ```csharp
    // 4. Check if the response contains a function call
    ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
        var result = await mcpClient.CallToolAsync(
            call.Name,
            dict!,
            cancellationToken: CancellationToken.None
        );

        Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

    }
    ```

ഇവിടെ:

- ഫംഗ്ഷൻ കോളുകളുടെ ലിസ്റ്റിലൂടെ ലൂപ്പ്.
- ഓരോ ടൂൾ കോളിനും പേര്, ആഗ്രിഗ്യുമെന്റുകൾ പാഴ്‌സ് ചെയ്ത് MCP സെർവറിലെ ടൂൾ കോളും MCP ക്ലയന്റ് ഉപയോഗിച്ച്. ഫലം പ്രിന്റ് ചെയ്തു.

മുഴുവൻ കോഡിന്:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;

var endpoint = "https://models.inference.ai.azure.com";
var token = Environment.GetEnvironmentVariable("GITHUB_TOKEN"); // Your GitHub Access Token
var client = new ChatCompletionsClient(new Uri(endpoint), new AzureKeyCredential(token));
var chatHistory = new List<ChatRequestMessage>
{
    new ChatRequestSystemMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}



async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);

        Console.WriteLine($"Properties: {propertiesElement}");        
    }

    return toolDefinitions;
}

// 1. List tools on mcp server

var tools = await GetMcpTools();
for (int i = 0; i < tools.Count; i++)
{
    var tool = tools[i];
    Console.WriteLine($"MCP Tools def: {i}: {tool}");
}

// 2. Define the chat history and the user message
var userMessage = "add 2 and 4";

chatHistory.Add(new ChatRequestUserMessage(userMessage));


// 3. Define options, including the tools
var options = new ChatCompletionsOptions(chatHistory)
{
    Model = "gpt-4.1-mini",
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletions? response = await client.CompleteAsync(options);
var content = response.Content;

// 5. Check if the response contains a function call
ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
    var result = await mcpClient.CallToolAsync(
        call.Name,
        dict!,
        cancellationToken: CancellationToken.None
    );

    Console.WriteLine(result.Content.OfType<TextContentBlock>().First().Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### ജാവ

```java
try {
    // MCP ഉപകരണങ്ങൾ സ്വയം ഉപയോഗിക്കുന്ന സ്വാഭാവിക ഭാഷ അഭ്യർത്ഥനകൾ നിർവഹിക്കുക
    String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
    System.out.println(response);

    response = bot.chat("What's the square root of 144?");
    System.out.println(response);

    response = bot.chat("Show me the help for the calculator service");
    System.out.println(response);
} finally {
    mcpClient.close();
}
```

ഇവിടെ:

- ലളിതമായ സ്വാഭാവിക ഭാഷാ പ്രോമ്റ്റുകൾ MCP സെർവർ ടൂളുകളുമായി സംവദിക്കാൻ ഉപയോഗിച്ചു
- LangChain4j ഫ്രെയിംവർക്ക് യാതൊരു തകരാറുമില്ലാതെ കൈകാര്യം ചെയ്യുന്നു:
  - ഉപയോക്തൃ പ്രോമ്റ്റ് ആവശ്യമായാൽ ടൂൾ കോളുകളായി മാറ്റൽ
  - LLM-ന്റെ തീരുമാന പ്രകാരം അനുയോജ്യമായ MCP ടൂളുകൾ കോൾ ചെയ്യൽ
  - LLM-യും MCP സെർവറും ഇടയിലുള്ള സംവാദ പ്രവാഹം കൈകാര്യം ചെയ്യൽ
- `bot.chat()` മെത്തഡ് LLM അഭ്യർത്ഥന പിന്തുണയുള്ള സ്വാഭാവിക ഭാഷാ പ്രതികരണങ്ങൾ നൽകുന്നു, അതിൽ MCP ടൂൾ ഫലങ്ങളും ഉൾക്കൊള്ളാം
- ഉപയോക്താക്കൾക്ക് അടിസ്ഥാനം MCP യഥാർത്ഥവിവരം അറിയേണ്ട ആവശ്യമില്ലാതെയുള്ള ഘടന

പൂർണ്ണ കോഡ് ഉദാഹരണം:

```java
public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .timeout(Duration.ofSeconds(60))
                .build();

        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();

        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        Bot bot = AiServices.builder(Bot.class)
                .chatLanguageModel(model)
                .toolProvider(toolProvider)
                .build();

        try {
            String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
            System.out.println(response);

            response = bot.chat("What's the square root of 144?");
            System.out.println(response);

            response = bot.chat("Show me the help for the calculator service");
            System.out.println(response);
        } finally {
            mcpClient.close();
        }
    }
}
```

#### റസ്റ്റ്

ഇവിടെ പ്രധാനപ്പെട്ട കാര്യങ്ങൾ നടക്കുന്നു. ആദ്യം ഉപയോക്തൃ പ്രോമ്റ്റുമായി LLM വിളിച്ച്, പ്രതികരണം റവ്യൂ ചെയ്ത് ടൂളുകൾ ആവശ്യമുണ്ടോ നോക്കും. വേണമെങ്കിൽ അവ ടൂൾകൾ കോളു ചെയ്ത് LLM-ഉടെയുള്ള സംഭാഷണം തുടരുമ്, കൂടുതൽ ടൂൾ കോളുകൾ ആവശ്യമില്ലാത്തവരെ.

പല തവണ LLM കോൾ ചെയ്യും, അതിനാൽ LLM കോൾ കൈകാര്യം ചെയ്യുന്ന ഒരു ഫംഗ്ഷൻ നിർവചിക്കാം. താഴെ കൊടുത്ത ഫംഗ്ഷൻ `main.rs` ൽ ചേർക്കുക:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": "openai/gpt-4.1",
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

ഈ ഫംഗ്ഷൻ LLM ക്ലയന്റ്, സന്ദേശങ്ങളുടെ പട്ടിക (ഉപയോക്തൃ പ്രോമ്റ്റ് ഉൾപ്പെടെ), MCP സെർവറിലെ ടൂളുകൾ സ്വീകരിച്ച് LLM-ന് അഭ്യർത്ഥന അയച്ച് പ്രതികരണം തിരികെ നൽകുന്നു.
LLM-ലെ പ്രതികരണം `choices` എന്നൊരു അറേ അടങ്ങിയിരിക്കും. `tool_calls` ഉണ്ടോ എന്ന് പരിശോധിക്കാൻ നാം ഫലം പ്രോസസ് ചെയ്യേണ്ടത് ആവശ്യമാണ്. ഏതെങ്കിലും ടൂൾ കാൾ ഉപയോക്തൃമായിരിക്കുകയാണെങ്കിൽ, അത് നമ്മെ അറിയിക്കും അവ ടൂൾ ഒരു നിർദ്ദിഷ്ട ടൂൾ ആ(argumentസിനൊപ്പം) കോള്‍ ചെയ്യണമെന്ന് LLM അഭ്യര്‍ത്ഥിക്കുന്നതായി. LLM പ്രതികരണം കൈകാര്യം ചെയ്യാൻ താഴെയുള്ള കോഡ് നിങ്ങളുടെ `main.rs` ഫയലിന്റെ താഴേക്ക് ചേർക്കുക:

```rust
async fn process_llm_response(
    llm_response: &Value,
    mcp_client: &RunningService<RoleClient, ()>,
    openai_client: &Client<OpenAIConfig>,
    mcp_tools: &ListToolsResult,
    messages: &mut Vec<Value>,
) -> Result<(), Box<dyn Error>> {
    let Some(message) = llm_response
        .get("choices")
        .and_then(|c| c.as_array())
        .and_then(|choices| choices.first())
        .and_then(|choice| choice.get("message"))
    else {
        return Ok(());
    };

    // ലഭ്യമായെങ്കിൽ ഉള്ളടക്കം പ്രിന്റ് ചെയ്യുക
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ടൂൾ കോൾസ് കൈകാര്യം ചെയ്യുക
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // അസിസ്റ്റന്റ് സന്ദേശം ചേർക്കുക

        // ഓരോ ടൂൾ കോഴും നിർവഹിക്കുക
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ടൂൾ ഫലം സന്ദേശങ്ങളിലേക്ക് ചേർക്കുക
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ടൂൾ ഫലങ്ങളോടൊപ്പം സംഭാഷണം തുടരുക
        let response = call_llm(openai_client, messages, mcp_tools).await?;
        Box::pin(process_llm_response(
            &response,
            mcp_client,
            openai_client,
            mcp_tools,
            messages,
        ))
        .await?;
    }
    Ok(())
}
```
  
`tool_calls` ഉണ്ടായാൽ, ടൂൾ വിവരങ്ങൾ എടുക്കുന്നു, ടൂൾ അഭ്യർത്ഥനയോടെ MCP സർവറിനെ കോൾ ചെയ്യുന്നു, ഫലങ്ങൾ സംഭാഷണ സന്ദേശങ്ങളിൽ ചേർക്കുന്നു. പിന്നീട് LLM-ഉം സന്ദേശങ്ങളും സഹിതം സംഭാഷണം തുടരുന്നു, സന്ദേശങ്ങൾ അസിസ്റ്റന്റിന്റെ പ്രതികരണവും ടൂൾ കോൾ ഫലങ്ങളും അപ്ഡേറ്റ് ചെയ്യുന്നു.

MCP കോൾസ് വേണ്ടി LLM നൽകിയ ടൂൾ കോൾ വിവരങ്ങൾ എടുക്കാൻ, മുഴുവൻ കോൾ നടത്താൻ ആവശ്യമായ ഡേറ്റയും എടുക്കുന്ന മറ്റൊരു സഹായിക ഫങ്ഷന്‍ ചേർക്കാം. താഴെയുള്ള കോഡ് നിങ്ങളുടെ `main.rs` ഫയലിന്റെ അവസാനത്തിൽ ചേർക്കുക:

```rust
fn extract_tool_call_info(tool_call: &Value) -> Result<(String, String, String), Box<dyn Error>> {
    let tool_id = tool_call
        .get("id")
        .and_then(|id| id.as_str())
        .unwrap_or("")
        .to_string();
    let function = tool_call.get("function").ok_or("Missing function")?;
    let name = function
        .get("name")
        .and_then(|n| n.as_str())
        .unwrap_or("")
        .to_string();
    let args = function
        .get("arguments")
        .and_then(|a| a.as_str())
        .unwrap_or("{}")
        .to_string();
    Ok((tool_id, name, args))
}
```
  
എല്ലാ ഭാഗങ്ങളും ഒരുമിച്ചപ്പോൾ, ആദ്യം ഉപയോക്തൃ പ്രോമ്പ്റ്റ് കൈകാര്യം ചെയ്ത് LLM-നെ കോൾ ചെയ്യാം. നിങ്ങളുടെ `main` ഫങ്ഷന് താഴെ കാണുന്ന കോഡ് ഉൾപ്പെടുത്തുക:

```rust
// ടൂൾ കോളുകളുമായി LLM സംഭാഷണം
let response = call_llm(&openai_client, &messages, &tools).await?;
process_llm_response(
    &response,
    &mcp_client,
    &openai_client,
    &tools,
    &mut messages,
)
.await?;
```
  
ഇത് ആദ്യം ഉപയോക്തൃ പ്രോമ്പ്റ്റ് ഉപയോഗിച്ച് രണ്ട് സംഖ്യകളുടെ സംഖ്യയുടെ് അഭ്യർത്ഥനയുമായി LLM-നെ ചോദിക്കുകയും, ടൂൾ കോൾസ് ഡൈനാമിക്കായി കൈകാര്യം ചെയ്യാൻ പ്രതികരണം പ്രോസസ്സ് ചെയ്യുകയും ചെയ്യും.

വലുത്, നിങ്ങൾ അത് ചെയ്തു!

## അസൈൻമെന്റ്

അഭ്യാസത്തിലെ കോഡ് എടുത്ത് കൂടുതൽ ടൂൾസ് ചേർക്കുന്നതിലൂടെ സർവർ വികസിപ്പിക്കുക. തുടർന്ന് LLM ഉള്ള ഒരു ക്ലയന്റ് സൃഷ്ടിച്ച് വ്യത്യസ്ത പ്രോമ്പ്റ്റുകൾ ഉപയോഗിച്ച് പരീക്ഷിക്കുക, എല്ലാവിധ സർവർ ടൂൾസും ഡൈനാമിക്കായി കോൾ ചെയ്യപ്പെടുന്നതായി ഉറപ്പാക്കുക. ഈ വിധത്തിലുള്ള ക്ലയന്റ് നിർമാണം ഉപയോക്താവിന് ഒരു മികച്ച അനുഭവം നൽകുന്നു, അവർ കൃത്യമായ ക്ലയന്റ് കമാൻഡുകൾക്കുപകരം പ്രോമ്പ്റ്റുകൾ ഉപയോഗിച്ച് MCP സർവർ കോൾ ആണെന്ന് അറിയാതെ സാധിക്കും.

## പരിഹാരം

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## പ്രധാന കാര്യങ്ങൾ

- നിങ്ങളുടെ ക്ലയന്റിൽ LLM ചേർക്കുന്നതായാൽ MCP സർവറുകളുമായി ഇന്ററാക്ട് ചെയ്യാനുള്ള മികച്ച മാർഗ്ഗം ലഭിക്കും.
- MCP സർവർ ഫലം LLMക്ക് മനസ്സിലാകുന്ന രൂപത്തിലേക്ക് മാറ്റേണ്ടതാണ്.

## സാമ്പിൾസ്

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## അധിക വിഭവങ്ങൾ

## അടുത്തത്

- അടുത്തത്: [Visual Studio Code ഉപയോഗിച്ച് സർവർ ഉപഭോഗം](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**റദ്ദാക്കൽ**:  
ഈ ഡോക്യുമെന്റ് AI തർജ്ജമ സേവനം [കോ-ഓപ്പ് ട്രാൻസ്ലേറ്റർ](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് തർജ്ജമ ചെയ്തതാണ്. നാം സുതാര്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമാറ്റിക് തർജ്ജമകളിൽ പിഴവുകളുമോ അസംബന്ധതകളുമോ ഉണ്ടാകാവുന്നതാണ്. അസൽ ഡോക്യുമെന്റിന്റെ മാതൃഭാഷ അടിസ്ഥാനസ്രോതസാമാന്യമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്കായി പ്രഫഷണൽ മനുഷ്യൻ ചെയ്ത തർജ്ജമ ശുപാർശ ചെയ്യുന്നു. ഈ തർജ്ജമ ഉപയോഗിച്ചതിനാൽ ഉണ്ടായ ഏതെങ്കിലും തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ തെറ്റിദ്ധാരണകൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->