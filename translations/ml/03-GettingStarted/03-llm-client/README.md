<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d846ebb88fbb0f00549e2ff8cc3f746",
  "translation_date": "2025-12-11T11:46:13+00:00",
  "source_file": "03-GettingStarted/03-llm-client/README.md",
  "language_code": "ml"
}
-->
# LLM ഉപയോഗിച്ച് ക്ലയന്റ് സൃഷ്ടിക്കൽ

ഇതുവരെ, നിങ്ങൾ ഒരു സെർവർയും ഒരു ക്ലയന്റും എങ്ങനെ സൃഷ്ടിക്കാമെന്ന് കണ്ടിട്ടുണ്ട്. ക്ലയന്റ് സെർവറെ വ്യക്തമായി വിളിച്ച് അതിന്റെ ടൂളുകൾ, റിസോഴ്‌സുകൾ, പ്രോംപ്റ്റുകൾ എന്നിവ ലിസ്റ്റ് ചെയ്യാൻ കഴിഞ്ഞിട്ടുണ്ട്. എന്നാൽ, ഇത് വളരെ പ്രായോഗികമായ സമീപനം അല്ല. നിങ്ങളുടെ ഉപയോക്താവ് ഏജന്റിക് കാലഘട്ടത്തിൽ ജീവിക്കുന്നു, പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് LLM-നുമായി ആശയവിനിമയം നടത്താൻ പ്രതീക്ഷിക്കുന്നു. നിങ്ങളുടെ ഉപയോക്താവിന് MCP ഉപയോഗിച്ച് നിങ്ങളുടെ കഴിവുകൾ സംഭരിക്കുന്നതിൽ താൽപര്യമില്ല, പക്ഷേ അവർ സ്വാഭാവിക ഭാഷ ഉപയോഗിച്ച് ഇടപഴകാൻ പ്രതീക്ഷിക്കുന്നു. അതിനാൽ ഇത് എങ്ങനെ പരിഹരിക്കാം? പരിഹാരം ക്ലയന്റിൽ ഒരു LLM ചേർക്കുന്നതിലാണ്.

## അവലോകനം

ഈ പാഠത്തിൽ, നിങ്ങളുടെ ക്ലയന്റിൽ ഒരു LLM ചേർക്കുന്നതിൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കുകയും ഇത് നിങ്ങളുടെ ഉപയോക്താവിന് എങ്ങനെ മികച്ച അനുഭവം നൽകുന്നുവെന്ന് കാണിക്കുകയും ചെയ്യും.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം അവസാനിക്കുന്നതോടെ, നിങ്ങൾക്ക് കഴിയും:

- LLM ഉപയോഗിച്ച് ഒരു ക്ലയന്റ് സൃഷ്ടിക്കുക.
- LLM ഉപയോഗിച്ച് MCP സെർവറുമായി സുതാര്യമായി ഇടപഴകുക.
- ക്ലയന്റ് വശത്ത് മികച്ച ഉപയോക്തൃ അനുഭവം നൽകുക.

## സമീപനം

നമുക്ക് എടുക്കേണ്ട സമീപനം മനസ്സിലാക്കാം. LLM ചേർക്കുന്നത് ലളിതമാണ് എന്ന് തോന്നാം, പക്ഷേ നാം ഇത് യഥാർത്ഥത്തിൽ ചെയ്യുമോ?

ക്ലയന്റ് സെർവറുമായി ഇങ്ങനെ ഇടപഴകും:

1. സെർവറുമായി കണക്ഷൻ സ്ഥാപിക്കുക.

1. കഴിവുകൾ, പ്രോംപ്റ്റുകൾ, റിസോഴ്‌സുകൾ, ടൂളുകൾ ലിസ്റ്റ് ചെയ്ത് അവയുടെ സ്കീമ സേവ് ചെയ്യുക.

1. ഒരു LLM ചേർക്കുക, സേവ് ചെയ്ത കഴിവുകളും അവയുടെ സ്കീമയും LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിൽ പാസ്സ് ചെയ്യുക.

1. ഉപയോക്തൃ പ്രോംപ്റ്റ് LLM-നു പാസ്സ് ചെയ്ത്, ക്ലയന്റ് ലിസ്റ്റ് ചെയ്ത ടൂളുകളോടൊപ്പം കൈകാര്യം ചെയ്യുക.

ശ്രേഷ്ഠം, ഇപ്പോൾ നാം ഉയർന്ന തലത്തിൽ ഇത് എങ്ങനെ ചെയ്യാമെന്ന് മനസ്സിലാക്കി, താഴെ ഉള്ള അഭ്യാസത്തിൽ ഇത് പരീക്ഷിക്കാം.

## അഭ്യാസം: LLM ഉപയോഗിച്ച് ക്ലയന്റ് സൃഷ്ടിക്കൽ

ഈ അഭ്യാസത്തിൽ, നാം നമ്മുടെ ക്ലയന്റിൽ ഒരു LLM ചേർക്കാൻ പഠിക്കും.

### GitHub Personal Access Token ഉപയോഗിച്ച് പ്രാമാണീകരണം

GitHub ടോക്കൺ സൃഷ്ടിക്കുന്നത് ലളിതമായ പ്രക്രിയയാണ്. ഇതാ എങ്ങനെ ചെയ്യാം:

- GitHub സെറ്റിംഗ്സിലേക്ക് പോവുക – മുകളിൽ വലത് കോണിൽ നിങ്ങളുടെ പ്രൊഫൈൽ ചിത്രം ക്ലിക്ക് ചെയ്ത് സെറ്റിംഗ്സ് തിരഞ്ഞെടുക്കുക.
- Developer Settings-ലേക്ക് നാവിഗേറ്റ് ചെയ്യുക – താഴേക്ക് സ്ക്രോൾ ചെയ്ത് Developer Settings ക്ലിക്ക് ചെയ്യുക.
- Personal Access Tokens തിരഞ്ഞെടുക്കുക – Fine-grained tokens ക്ലിക്ക് ചെയ്ത് Generate new token തിരഞ്ഞെടുക്കുക.
- നിങ്ങളുടെ ടോക്കൺ കോൺഫിഗർ ചെയ്യുക – റഫറൻസിനായി ഒരു നോട്ടു ചേർക്കുക, കാലഹരണ തീയതി സജ്ജമാക്കുക, ആവശ്യമായ സ്കോപ്പുകൾ (അനുമതികൾ) തിരഞ്ഞെടുക്കുക. ഈ കേസിൽ Models അനുമതി ചേർക്കാൻ ഉറപ്പാക്കുക.
- ടോക്കൺ ജനറേറ്റ് ചെയ്ത് കോപ്പി ചെയ്യുക – Generate token ക്ലിക്ക് ചെയ്ത് ഉടൻ കോപ്പി ചെയ്യുക, പിന്നീട് കാണാൻ സാധിക്കില്ല.

### -1- സെർവറുമായി കണക്ട് ചെയ്യുക

നമുക്ക് ആദ്യം നമ്മുടെ ക്ലയന്റ് സൃഷ്ടിക്കാം:

#### TypeScript

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

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു
- `client`യും `openai`യും എന്ന രണ്ട് അംഗങ്ങളുള്ള ഒരു ക്ലാസ് സൃഷ്ടിച്ചു, ഇത് ക്ലയന്റ് മാനേജുചെയ്യാനും LLM-നുമായി ഇടപഴകാനും സഹായിക്കും.
- `baseUrl` GitHub Models-നു സൂചിപ്പിക്കുന്ന വിധം സെറ്റ് ചെയ്ത് LLM ഇൻസ്റ്റൻസ് കോൺഫിഗർ ചെയ്തു.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio കണക്ഷനായി സെർവർ പാരാമീറ്ററുകൾ സൃഷ്ടിക്കുക
server_params = StdioServerParameters(
    command="mcp",  # പ്രവർത്തനക്ഷമമായ ഫയൽ
    args=["run", "server.py"],  # ഐച്ഛിക കമാൻഡ് ലൈൻ_ARGUMENTS
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

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- MCP-ക്കായി ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു
- ഒരു ക്ലയന്റ് സൃഷ്ടിച്ചു

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

#### Java

ആദ്യം, നിങ്ങളുടെ `pom.xml` ഫയലിൽ LangChain4j ഡിപ്പൻഡൻസികൾ ചേർക്കണം. MCP ഇന്റഗ്രേഷൻക്കും GitHub Models പിന്തുണയ്ക്കും ഈ ഡിപ്പൻഡൻസികൾ ചേർക്കുക:

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

പിന്നീട് നിങ്ങളുടെ ജാവ ക്ലയന്റ് ക്ലാസ് സൃഷ്ടിക്കുക:

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
    
    public static void main(String[] args) throws Exception {        // GitHub മോഡലുകൾ ഉപയോഗിക്കാൻ LLM ക്രമീകരിക്കുക
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // സെർവറുമായി ബന്ധപ്പെടാൻ MCP ട്രാൻസ്പോർട്ട് സൃഷ്ടിക്കുക
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ക്ലയന്റ് സൃഷ്ടിക്കുക
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- **LangChain4j ഡിപ്പൻഡൻസികൾ ചേർത്തു**: MCP ഇന്റഗ്രേഷൻ, OpenAI ഔദ്യോഗിക ക്ലയന്റ്, GitHub Models പിന്തുണയ്ക്കായി
- **LangChain4j ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു**: MCP ഇന്റഗ്രേഷൻക്കും OpenAI ചാറ്റ് മോഡൽ ഫംഗ്ഷണാലിറ്റിക്കും
- **`ChatLanguageModel` സൃഷ്ടിച്ചു**: GitHub Models ഉപയോഗിച്ച് നിങ്ങളുടെ GitHub ടോക്കൺ ഉപയോഗിച്ച് കോൺഫിഗർ ചെയ്തു
- **HTTP ട്രാൻസ്പോർട്ട് സജ്ജമാക്കി**: MCP സെർവറുമായി കണക്ട് ചെയ്യാൻ Server-Sent Events (SSE) ഉപയോഗിച്ചു
- **MCP ക്ലയന്റ് സൃഷ്ടിച്ചു**: സെർവറുമായി ആശയവിനിമയം കൈകാര്യം ചെയ്യാൻ
- **LangChain4j-യുടെ MCP പിന്തുണ ഉപയോഗിച്ചു**: LLM-കളും MCP സെർവറുകളും തമ്മിലുള്ള ഇന്റഗ്രേഷൻ ലളിതമാക്കുന്നു

#### Rust

ഈ ഉദാഹരണം Rust അടിസ്ഥാനമാക്കിയ MCP സെർവർ പ്രവർത്തനക്ഷമമാണെന്ന് فرضിക്കുന്നു. ഇല്ലെങ്കിൽ, [01-first-server](../01-first-server/README.md) പാഠത്തിലേക്ക് തിരിച്ച് സെർവർ സൃഷ്ടിക്കുക.

Rust MCP സെർവർ ഉണ്ടെങ്കിൽ, ടെർമിനൽ തുറന്ന് സെർവറിന്റെ ഡയറക്ടറിയിലേക്ക് പോകുക. തുടർന്ന് പുതിയ LLM ക്ലയന്റ് പ്രോജക്ട് സൃഷ്ടിക്കാൻ താഴെ കാണുന്ന കമാൻഡ് റൺ ചെയ്യുക:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` ഫയലിൽ താഴെ കാണുന്ന ഡിപ്പൻഡൻസികൾ ചേർക്കുക:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI-ക്കായി ഔദ്യോഗിക Rust ലൈബ്രറി ഇല്ല, പക്ഷേ `async-openai` ക്രേറ്റ് ഒരു [കമ്മ്യൂണിറ്റി പരിപാലിത ലൈബ്രറി](https://platform.openai.com/docs/libraries/rust#rust) ആണ്, സാധാരണയായി ഉപയോഗിക്കുന്നു.

`src/main.rs` ഫയൽ തുറന്ന് ഉള്ളടക്കം താഴെ കാണുന്ന കോഡിൽ മാറ്റുക:

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
    // പ്രാരംഭ സന്ദേശം
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ക്ലയന്റ് സജ്ജമാക്കുക
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ക്ലയന്റ് സജ്ജമാക്കുക
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

    // TODO: ടൂൾ കോൾസുമായി LLM സംഭാഷണം

    Ok(())
}
```

ഈ കോഡ് ഒരു അടിസ്ഥാന Rust അപ്ലിക്കേഷൻ സജ്ജമാക്കുന്നു, MCP സെർവറിനും GitHub Models-നുമായി LLM ഇടപഴകുന്നതിനും.

> [!IMPORTANT]
> ആപ്ലിക്കേഷൻ റൺ ചെയ്യുന്നതിന് മുമ്പ് `OPENAI_API_KEY` പരിസ്ഥിതി വ്യത്യാസം നിങ്ങളുടെ GitHub ടോക്കൺ ഉപയോഗിച്ച് സജ്ജമാക്കുക.

ശ്രേഷ്ഠം, അടുത്ത ഘട്ടം സെർവറിലെ കഴിവുകൾ ലിസ്റ്റ് ചെയ്യുക.

### -2- സെർവർ കഴിവുകൾ ലിസ്റ്റ് ചെയ്യുക

ഇപ്പോൾ സെർവറുമായി കണക്ട് ചെയ്ത് അതിന്റെ കഴിവുകൾ ചോദിക്കാം:

#### Typescript

അടുത്ത ക്ലാസിൽ താഴെ കാണുന്ന മെത്തഡുകൾ ചേർക്കുക:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ഉപകരണങ്ങൾ പട്ടികപ്പെടുത്തുന്നു
    const toolsResult = await this.client.listTools();
}
```

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- സെർവറുമായി കണക്ട് ചെയ്യാനുള്ള `connectToServer` കോഡ് ചേർത്തു.
- ആപ്പ് ഫ്ലോ കൈകാര്യം ചെയ്യുന്ന `run` മെത്തഡ് സൃഷ്ടിച്ചു. ഇതുവരെ ടൂളുകൾ മാത്രം ലിസ്റ്റ് ചെയ്യുന്നു, പിന്നീട് കൂടുതൽ ചേർക്കും.

#### Python

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

നാം ചേർത്തത്:

- റിസോഴ്‌സുകളും ടൂളുകളും ലിസ്റ്റ് ചെയ്ത് പ്രിന്റ് ചെയ്തു. ടൂളുകൾക്കായി `inputSchema`യും ലിസ്റ്റ് ചെയ്തു, പിന്നീട് ഉപയോഗിക്കും.

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

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- MCP സെർവറിൽ ലഭ്യമായ ടൂളുകൾ ലിസ്റ്റ് ചെയ്തു
- ഓരോ ടൂളിനും പേര്, വിവരണം, സ്കീമ എന്നിവ ലിസ്റ്റ് ചെയ്തു. സ്കീമ പിന്നീട് ടൂൾ വിളിക്കാനായി ഉപയോഗിക്കും.

#### Java

```java
// MCP ടൂളുകൾ സ്വയം കണ്ടെത്തുന്ന ഒരു ടൂൾ പ്രൊവൈഡർ സൃഷ്ടിക്കുക
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ടൂൾ പ്രൊവൈഡർ സ്വയം കൈകാര്യം ചെയ്യുന്നത്:
// - MCP സെർവറിൽ നിന്ന് ലഭ്യമായ ടൂളുകൾ ലിസ്റ്റ് ചെയ്യൽ
// - MCP ടൂൾ സ്കീമകൾ LangChain4j ഫോർമാറ്റിലേക്ക് മാറ്റൽ
// - ടൂൾ പ്രവർത്തനം மற்றும் പ്രതികരണങ്ങൾ നിയന്ത്രിക്കൽ
```

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- MCP സെർവറിൽ നിന്നുള്ള എല്ലാ ടൂളുകളും സ്വയം കണ്ടെത്തി രജിസ്റ്റർ ചെയ്യുന്ന `McpToolProvider` സൃഷ്ടിച്ചു
- ടൂൾ പ്രൊവൈഡർ MCP ടൂൾ സ്കീമകളും LangChain4j ടൂൾ ഫോർമാറ്റും തമ്മിലുള്ള പരിവർത്തനം കൈകാര്യം ചെയ്യുന്നു
- ഈ സമീപനം മാനുവൽ ടൂൾ ലിസ്റ്റിംഗ്, പരിവർത്തനം ഒഴിവാക്കുന്നു

#### Rust

MCP സെർവറിൽ നിന്നുള്ള ടൂളുകൾ `list_tools` മെത്തഡ് ഉപയോഗിച്ച് ലഭിക്കും. `main` ഫംഗ്ഷനിൽ MCP ക്ലയന്റ് സജ്ജമാക്കിയ ശേഷം താഴെ കാണുന്ന കോഡ് ചേർക്കുക:

```rust
// MCP ടൂൾ ലിസ്റ്റിംഗ് നേടുക
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- സെർവർ കഴിവുകൾ LLM ടൂളുകളായി പരിവർത്തനം ചെയ്യുക

സെർവർ കഴിവുകൾ ലിസ്റ്റ് ചെയ്ത ശേഷം, അവ LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റണം. അതിനുശേഷം ഈ കഴിവുകൾ LLM-നു ടൂളുകളായി നൽകാം.

#### TypeScript

1. MCP സെർവറിന്റെ പ്രതികരണം LLM ഉപയോഗിക്കാൻ കഴിയുന്ന ടൂൾ ഫോർമാറ്റിലേക്ക് മാറ്റാൻ താഴെ കാണുന്ന കോഡ് ചേർക്കുക:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ഇൻപുട്ട്_സ്കീമയുടെ അടിസ്ഥാനത്തിൽ ഒരു സോഡ് സ്കീമ സൃഷ്ടിക്കുക
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ടൈപ്പ് "ഫംഗ്ഷൻ" ആയി വ്യക്തമായി സജ്ജമാക്കുക
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

    മുകളിൽ കാണുന്ന കോഡ് MCP സെർവറിന്റെ പ്രതികരണം എടുത്ത് LLM മനസ്സിലാക്കുന്ന ടൂൾ നിർവചന ഫോർമാറ്റിലേക്ക് മാറ്റുന്നു.

1. തുടർന്ന് `run` മെത്തഡ് അപ്ഡേറ്റ് ചെയ്ത് സെർവർ കഴിവുകൾ ലിസ്റ്റ് ചെയ്യാം:

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

    മുൻകൂട്ടി നൽകിയ കോഡിൽ, `run` മെത്തഡ് ഫലം മാപ്പ് ചെയ്ത് ഓരോ എൻട്രിക്കും `openAiToolAdapter` വിളിക്കുന്നു.

#### Python

1. ആദ്യം, താഴെ കാണുന്ന കൺവെർട്ടർ ഫംഗ്ഷൻ സൃഷ്ടിക്കാം:

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

    `convert_to_llm_tools` ഫംഗ്ഷനിൽ MCP ടൂൾ പ്രതികരണം LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റുന്നു.

1. തുടർന്ന് ക്ലയന്റ് കോഡ് അപ്ഡേറ്റ് ചെയ്ത് ഈ ഫംഗ്ഷൻ ഉപയോഗിക്കാം:

    ```python
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ഇവിടെ MCP ടൂൾ പ്രതികരണം LLM-നു നൽകാൻ `convert_to_llm_tool` വിളിക്കുന്നു.

#### .NET

1. MCP ടൂൾ പ്രതികരണം LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റാൻ കോഡ് ചേർക്കാം:

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

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- പേര്, വിവരണം, ഇൻപുട്ട് സ്കീമ സ്വീകരിക്കുന്ന `ConvertFrom` ഫംഗ്ഷൻ സൃഷ്ടിച്ചു.
- ഇത് `FunctionDefinition` സൃഷ്ടിച്ച് `ChatCompletionsDefinition`-ലേക്ക് പാസ്സ് ചെയ്യുന്നു, LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റ്.

1. നിലവിലുള്ള കോഡ് അപ്ഡേറ്റ് ചെയ്യാം:

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

#### Java

```java
// സ്വാഭാവിക ഭാഷാ ഇടപെടലിനായി ഒരു ബോട്ട് ഇന്റർഫേസ് സൃഷ്ടിക്കുക
public interface Bot {
    String chat(String prompt);
}

// LLM மற்றும் MCP ഉപകരണങ്ങളോടുകൂടി AI സേവനം ക്രമീകരിക്കുക
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- സ്വാഭാവിക ഭാഷാ ഇടപെടലിനായി ലളിതമായ `Bot` ഇന്റർഫേസ് നിർവചിച്ചു
- LangChain4j-യുടെ `AiServices` ഉപയോഗിച്ച് LLM MCP ടൂൾ പ്രൊവൈഡറുമായി സ്വയം ബന്ധിപ്പിച്ചു
- ഫ്രെയിംവർക്ക് ടൂൾ സ്കീമ പരിവർത്തനവും ഫംഗ്ഷൻ കോളിംഗും സ്വയം കൈകാര്യം ചെയ്യുന്നു
- മാനുവൽ ടൂൾ പരിവർത്തനം ഒഴിവാക്കി - LangChain4j MCP ടൂളുകൾ LLM-സഹജമായ ഫോർമാറ്റിലേക്ക് മാറ്റുന്നതിന്റെ സങ്കീർണ്ണത കൈകാര്യം ചെയ്യുന്നു

#### Rust

MCP ടൂൾ പ്രതികരണം LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റാൻ, ടൂൾ ലിസ്റ്റിംഗ് ഫോർമാറ്റ് ചെയ്യുന്ന ഹെൽപ്പർ ഫംഗ്ഷൻ ചേർക്കാം. `main` ഫംഗ്ഷനിന് താഴെ താഴെ കാണുന്ന കോഡ് ചേർക്കുക. ഇത് LLM-നു അഭ്യർത്ഥനകൾ അയയ്ക്കുമ്പോൾ വിളിക്കും:

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

ശ്രേഷ്ഠം, ഉപയോക്തൃ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യാൻ നമുക്ക് സജ്ജമാണ്, അടുത്തത് അത് നോക്കാം.

### -4- ഉപയോക്തൃ പ്രോംപ്റ്റ് അഭ്യർത്ഥന കൈകാര്യം ചെയ്യുക

ഈ ഭാഗത്ത്, ഉപയോക്തൃ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യും.

#### TypeScript

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


        // 2. സെർവറിന്റെ ടൂൾ വിളിക്കുക
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ഫലത്തോടെ എന്തെങ്കിലും ചെയ്യുക
        // ചെയ്യേണ്ടത്

        }
    }
    ```

    മുൻകൂട്ടി നൽകിയ കോഡിൽ:

    - `callTools` എന്ന മെത്തഡ് ചേർത്തു.
    - LLM പ്രതികരണം പരിശോധിച്ച് ഏത് ടൂളുകൾ വിളിക്കപ്പെട്ടുവെന്ന് പരിശോധിക്കുന്നു:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ടൂൾ വിളിക്കുക
        }
        ```

    - LLM ടൂൾ വിളിക്കണമെന്ന് സൂചിപ്പിച്ചാൽ ടൂൾ വിളിക്കുന്നു:

        ```typescript
        // 2. സെർവറിന്റെ ടൂൾ വിളിക്കുക
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ഫലത്തോടെ എന്തെങ്കിലും ചെയ്യുക
        // ചെയ്യേണ്ടത്
        ```

1. `run` മെത്തഡ് അപ്ഡേറ്റ് ചെയ്ത് LLM വിളിക്കുകയും `callTools` വിളിക്കുകയും ചെയ്യുക:

    ```typescript

    // 1. LLM-ന് ഇൻപുട്ടായി ഉപയോഗിക്കുന്ന സന്ദേശങ്ങൾ സൃഷ്ടിക്കുക
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM-നെ വിളിക്കുക
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM പ്രതികരണം പരിശോധിക്കുക, ഓരോ തിരഞ്ഞെടുപ്പിനും ടൂൾ കോൾസ് ഉണ്ടോ എന്ന് പരിശോധിക്കുക
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ശ്രേഷ്ഠം, മുഴുവൻ കോഡ് ലിസ്റ്റ് ചെയ്യാം:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // സ്കീമാ സാധുത പരിശോധനയ്ക്കായി zod ഇറക്കുമതി ചെയ്യുക

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ഭാവിയിൽ ഈ URL-ലേക്ക് മാറ്റേണ്ടതുണ്ടാകാം: https://models.github.ai/inference
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
            type: "function" as const, // ടൈപ്പ് "function" ആയി വ്യക്തമായി സജ്ജമാക്കുക
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
    
    
          // 2. സെർവറിന്റെ ടൂൾ വിളിക്കുക
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ഫലത്തോടൊപ്പം എന്തെങ്കിലും ചെയ്യുക
          // ചെയ്യേണ്ടത്
    
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM പ്രതികരണം പരിശോധിക്കുക, ഓരോ തിരഞ്ഞെടുപ്പിനും ടൂൾ കോളുകൾ ഉണ്ടോ എന്ന് പരിശോധിക്കുക
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

#### Python

1. LLM വിളിക്കാൻ ആവശ്യമായ ഇറക്കുമതികൾ ചേർക്കുക:

    ```python
    # എൽഎൽഎം
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. LLM വിളിക്കുന്ന ഫംഗ്ഷൻ ചേർക്കുക:

    ```python
    # എൽഎൽഎം

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
            # ഐച്ഛിക പാരാമീറ്ററുകൾ
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

    മുൻകൂട്ടി നൽകിയ കോഡിൽ:

    - MCP സെർവറിൽ നിന്നുള്ള ഫംഗ്ഷനുകൾ LLM-നു പാസ്സ് ചെയ്തു.
    - LLM ആ ഫംഗ്ഷനുകളുമായി വിളിച്ചു.
    - ഫലം പരിശോധിച്ച് ഏത് ഫംഗ്ഷനുകൾ വിളിക്കണമെന്ന് നോക്കി.
    - വിളിക്കേണ്ട ഫംഗ്ഷനുകളുടെ ലിസ്റ്റ് പാസ്സ് ചെയ്തു.

1. അവസാന ഘട്ടം, പ്രധാന കോഡ് അപ്ഡേറ്റ് ചെയ്യുക:

    ```python
    prompt = "Add 2 to 20"

    # LLM-നെ എന്തെങ്കിലും ഉപകരണങ്ങൾ ഉണ്ടോ എന്ന് ചോദിക്കുക
    functions_to_call = call_llm(prompt, functions)

    # നിർദ്ദേശിച്ച ഫംഗ്ഷനുകൾ വിളിക്കുക
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    മുകളിൽ, MCP ടൂൾ LLM-ന്റെ നിർദ്ദേശപ്രകാരം `call_tool` വഴി വിളിക്കുന്നു.
    - ടൂൾ വിളന ഫലം MCP സെർവറിൽ പ്രിന്റ് ചെയ്യുന്നു.

#### .NET

1. LLM പ്രോംപ്റ്റ് അഭ്യർത്ഥനയ്ക്കുള്ള കോഡ് കാണിക്കുക:

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
        Model = "gpt-4o-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    മുൻകൂട്ടി നൽകിയ കോഡിൽ:

    - MCP സെർവറിൽ നിന്നുള്ള ടൂളുകൾ എടുത്തു, `var tools = await GetMcpTools()`.
    - ഉപയോക്തൃ പ്രോംപ്റ്റ് നിർവചിച്ചു `userMessage`.
    - മോഡൽ, ടൂളുകൾ എന്നിവ വ്യക്തമാക്കുന്ന ഓപ്ഷൻസ് ഒബ്ജക്റ്റ് സൃഷ്ടിച്ചു.
    - LLM-നു അഭ്യർത്ഥന അയച്ചു.

1. ഒടുവിൽ, LLM ഫംഗ്ഷൻ കോളുകൾ പരിശോധിക്കുക:

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

    മുൻകൂട്ടി നൽകിയ കോഡിൽ:

    - ഫംഗ്ഷൻ കോളുകളുടെ ലിസ്റ്റ് ലൂപ്പ് ചെയ്തു.
    - ഓരോ ടൂൾ കോളിനും പേര്, ആർഗുമെന്റുകൾ പാഴ്സ് ചെയ്ത് MCP ക്ലയന്റ് ഉപയോഗിച്ച് ടൂൾ വിളിച്ചു. ഫലം പ്രിന്റ് ചെയ്തു.

മുഴുവൻ കോഡ്:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

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
    Model = "gpt-4o-mini",
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

    Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // MCP ഉപകരണങ്ങൾ സ്വയം ഉപയോഗിച്ച് സ്വാഭാവിക ഭാഷാ അഭ്യർത്ഥനകൾ നടപ്പിലാക്കുക
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

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- ലളിതമായ സ്വാഭാവിക ഭാഷ പ്രോംപ്റ്റുകൾ MCP സെർവർ ടൂളുകളുമായി ഇടപഴകാൻ ഉപയോഗിച്ചു
- LangChain4j ഫ്രെയിംവർക്ക് സ്വയം കൈകാര്യം ചെയ്യുന്നു:
  - ആവശ്യമായപ്പോൾ ഉപയോക്തൃ പ്രോംപ്റ്റുകൾ ടൂൾ കോളുകളായി മാറ്റുന്നു
  - LLM തീരുമാനപ്രകാരം MCP ടൂളുകൾ വിളിക്കുന്നു
  - LLM-നും MCP സെർവറിനും ഇടയിലെ സംഭാഷണ പ്രവാഹം നിയന്ത്രിക്കുന്നു
- `bot.chat()` സ്വാഭാവിക ഭാഷാ പ്രതികരണങ്ങൾ നൽകുന്നു, MCP ടൂൾ ഫലങ്ങൾ ഉൾപ്പെടാം
- ഉപയോക്താക്കൾക്ക് MCP അടിസ്ഥാന ഘടന അറിയേണ്ടതില്ലാത്ത സുതാര്യ അനുഭവം നൽകുന്നു

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

#### Rust

ഇവിടെ പ്രധാനമായും പ്രവർത്തനം നടക്കുന്നു. ആദ്യം ഉപയോക്തൃ പ്രോംപ്റ്റ് LLM-നു വിളിക്കും, തുടർന്ന് പ്രതികരണം പരിശോധിച്ച് ടൂളുകൾ വിളിക്കേണ്ടതുണ്ടോ എന്ന് നോക്കും. ആവശ്യമെങ്കിൽ ടൂളുകൾ വിളിച്ച് LLM-നുമായി സംഭാഷണം തുടരും, കൂടുതൽ ടൂൾ കോളുകൾ ആവശ്യമില്ലാതെ അന്തിമ പ്രതികരണം ലഭിക്കും.

നാം LLM-നു പല തവണ വിളിക്കും, അതിനാൽ LLM കോളുകൾ കൈകാര്യം ചെയ്യുന്ന ഫംഗ്ഷൻ നിർവചിക്കാം. `main.rs` ഫയലിൽ താഴെ കാണുന്ന ഫംഗ്ഷൻ ചേർക്കുക:

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

ഈ ഫംഗ്ഷൻ LLM ക്ലയന്റ്, സന്ദേശങ്ങളുടെ ലിസ്റ്റ് (ഉപയോക്തൃ പ്രോംപ്റ്റ് ഉൾപ്പെടെ), MCP സെർവറിലെ ടൂളുകൾ സ്വീകരിച്ച് LLM-നു അഭ്യർത്ഥന അയച്ച് പ്രതികരണം തിരികെ നൽകുന്നു.
LLM-ൽ നിന്നുള്ള പ്രതികരണം `choices` എന്ന ഒരു അറേ ഉൾക്കൊള്ളും. ഏതെങ്കിലും `tool_calls` ഉണ്ടോ എന്ന് പരിശോധിക്കാൻ നമുക്ക് ഫലം പ്രോസസ് ചെയ്യേണ്ടതുണ്ട്. LLM ഒരു പ്രത്യേക ടൂൾ ആഗ്യുമെന്റുകളോടുകൂടി വിളിക്കണമെന്ന് അഭ്യർത്ഥിക്കുന്നുവെന്ന് ഇത് നമ്മെ അറിയിക്കുന്നു. LLM പ്രതികരണം കൈകാര്യം ചെയ്യാൻ ഒരു ഫംഗ്ഷൻ നിർവചിക്കാൻ താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് നിങ്ങളുടെ `main.rs` ഫയലിന്റെ അടിയിൽ ചേർക്കുക:

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

    // ഉള്ളടക്കം ലഭ്യമായാൽ പ്രിന്റ് ചെയ്യുക
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ടൂൾ കോൾസ് കൈകാര്യം ചെയ്യുക
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // അസിസ്റ്റന്റ് സന്ദേശം ചേർക്കുക

        // ഓരോ ടൂൾ കോൾയും നടപ്പിലാക്കുക
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ടൂൾ ഫലം സന്ദേശങ്ങളിൽ ചേർക്കുക
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ടൂൾ ഫലങ്ങളോടെ സംഭാഷണം തുടരുക
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

`tool_calls` ഉണ്ടെങ്കിൽ, അത് ടൂൾ വിവരങ്ങൾ എടുക്കുന്നു, ടൂൾ അഭ്യർത്ഥനയോടെ MCP സെർവറെ വിളിക്കുന്നു, ഫലങ്ങൾ സംഭാഷണ സന്ദേശങ്ങളിൽ ചേർക്കുന്നു. തുടർന്ന് LLM-ഉം സന്ദേശങ്ങളും സഹിതം സംഭാഷണം തുടരുന്നു, സഹായിയുടെ പ്രതികരണവും ടൂൾ കോൾ ഫലങ്ങളും സന്ദേശങ്ങളിൽ അപ്ഡേറ്റ് ചെയ്യപ്പെടുന്നു.

MCP കോൾസിനായി LLM തിരികെ നൽകുന്ന ടൂൾ കോൾ വിവരങ്ങൾ എടുക്കാൻ, കോൾ നടത്താൻ ആവശ്യമായ എല്ലാം എടുക്കുന്ന മറ്റൊരു സഹായക ഫംഗ്ഷൻ ചേർക്കാം. നിങ്ങളുടെ `main.rs` ഫയലിന്റെ അടിയിൽ താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ചേർക്കുക:

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

എല്ലാ ഭാഗങ്ങളും സജ്ജമാക്കിയതോടെ, പ്രാഥമിക ഉപയോക്തൃ പ്രോംപ്റ്റ് കൈകാര്യം ചെയ്ത് LLM-നെ വിളിക്കാൻ കഴിയും. നിങ്ങളുടെ `main` ഫംഗ്ഷൻ താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ഉൾപ്പെടുത്താൻ അപ്ഡേറ്റ് ചെയ്യുക:

```rust
// ടൂൾ കോൾസുമായി LLM സംഭാഷണം
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

ഇത് രണ്ട് സംഖ്യകളുടെ കൂട്ടം ചോദിക്കുന്ന പ്രാഥമിക ഉപയോക്തൃ പ്രോംപ്റ്റ് ഉപയോഗിച്ച് LLM-നെ ചോദിക്കും, പ്രതികരണം പ്രോസസ് ചെയ്ത് ടൂൾ കോൾസ് ഡൈനാമിക്കായി കൈകാര്യം ചെയ്യും.

ശ്രേഷ്ഠം, നിങ്ങൾ അത് ചെയ്തു!

## അസൈൻമെന്റ്

പരീക്ഷണത്തിൽ നിന്നുള്ള കോഡ് എടുത്ത് കൂടുതൽ ടൂളുകളുമായി സെർവർ നിർമ്മിക്കുക. തുടർന്ന് LLM പോലുള്ള ഒരു ക്ലയന്റ് സൃഷ്ടിച്ച് വ്യത്യസ്ത പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് പരീക്ഷിച്ച് നിങ്ങളുടെ എല്ലാ സെർവർ ടൂളുകളും ഡൈനാമിക്കായി വിളിക്കപ്പെടുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക. ഈ രീതിയിൽ ക്ലയന്റ് നിർമ്മിക്കുന്നത് അവസാന ഉപയോക്താവിന് മികച്ച അനുഭവം നൽകും, കാരണം അവർ കൃത്യമായ ക്ലയന്റ് കമാൻഡുകൾക്ക് പകരം പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് പ്രവർത്തിക്കാനും MCP സെർവർ വിളിക്കപ്പെടുന്നതിനെ അവഗണിക്കാനും കഴിയും.

## പരിഹാരം

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## പ്രധാന കാര്യങ്ങൾ

- നിങ്ങളുടെ ക്ലയന്റിൽ LLM ചേർക്കുന്നത് MCP സെർവറുകളുമായി ഉപയോക്താക്കൾക്ക് മികച്ച ഇടപെടൽ മാർഗം നൽകുന്നു.
- MCP സെർവർ പ്രതികരണം LLM മനസ്സിലാക്കുന്ന രൂപത്തിലേക്ക് മാറ്റേണ്ടതുണ്ട്.

## സാമ്പിളുകൾ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## അധിക വിഭവങ്ങൾ

## അടുത്തത്

- അടുത്തത്: [Visual Studio Code ഉപയോഗിച്ച് സെർവർ ഉപഭോഗം](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->