# LLM ഉപയോഗിച്ച് ക്ലയന്റ് സൃഷ്‌ടിക്കൽ

ഇതുവരെ, നിങ്ങൾ ഒരു സേർവർയും ക്ലയന്റും എങ്ങനെ സൃഷ്‌ടിക്കാമെന്ന് കണ്ടിട്ടുണ്ട്. ക്ലയന്റ് സേർവറെ വ്യക്തമായി വിളിച്ച് അതിന്റെ ടൂളുകൾ, റിസോഴ്‌സുകൾ, പ്രോംപ്റ്റുകൾ എന്നിവ ലിസ്റ്റുചെയ്യാൻ കഴിഞ്ഞിരുന്നു. എന്നാൽ, ഇത് വളരെ പ്രായോഗികമായ സമീപനം അല്ല. നിങ്ങളുടെ ഉപയോക്താക്കൾ ഏജൻസിക് കാലഘട്ടത്തിലാണ് ജീവിക്കുന്നത്, അവർ പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് LLM-ഉടൊപ്പം ആശയവിനിമയം നടത്താൻ പ്രതീക്ഷിക്കുന്നു. അവർ നിങ്ങളുടെ കഴിവുകൾ MCP-യിൽ സ്റ്റോർ ചെയ്യുന്നതിൽ ശ്രദ്ധിച്ചുപോകരുത്; അവർ സ്വാഭാവിക ഭാഷ ഉപയോഗിച്ച് ആശയവിനിമയം പുലർത്തണമെന്ന് മാത്രമാണ് പ്രതീക്ഷിക്കുന്നത്. അപ്പോൾ നാം ഇത് എങ്ങനെ പരിഹരിക്കണം? പരിഹാരം ക്ലയന്റിനൊപ്പം LLM ചേർക്കുകയാണ്.

## അവലോകനം

ഈ പാഠത്തിൽ, ക്ലയന്റിൽ LLM ചേർക്കുന്നതിന് കേന്ദ്രീകരിക്കുകയും, ഇത് നിങ്ങളുടെ ഉപയോക്താക്കൾക്ക് എങ്ങനെ മെച്ചപ്പെട്ട അനുഭവം നൽകുന്നു എന്ന് കാണിക്കും.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം അവസാനിക്കുമ്പോൾ, നിങ്ങൾക്ക് കഴിയും:

- LLM ഉള്ള ഒരു ക്ലയന്റ് സൃഷ്‌ടിക്കൽ.
- MCP സേർവറുമായി LLM ഉപയോഗിച്ച് സുൽഭമായി ഇടപഴകൽ.
- ക്ലയന്റ് ദിശയിൽ മെച്ചപ്പെട്ട സമാപന ഉപയോക്തൃ അനുഭവം നൽകുക.

## സമീപനം

നാം എടുക്കേണ്ട സമീപനം മനസ്സിലാക്കാം. LLM ചേർക്കുന്നത് സാധാരണമാണ്, എന്നാൽ നന്നായി ഇത് നടത്തുമോ?

ക്ലയന്റ് സേർവറുമായി ഇങ്ങനെ ഇടപഴകും:

1. സേർവറുമായി കണക്ഷൻ സ്ഥാപിക്കുക.

1. കഴിവുകൾ, പ്രോംപ്റ്റുകൾ, റിസോഴ്‌സുകൾ, ടൂളുകൾ ലിസ്റ്റുചെയ്യുകയും അവരുടെ സ്കീമ സെവ് ചെയ്യുകയും ചെയ്യുക.

1. LLM ചേർത്ത്, ലിംഗമായി നിന്നും ലഭിച്ച കഴിവുകളും സ്കീമയും LLM-ന് മനസ്സിലാകുന്ന ഫോർമാറ്റിൽ പാസ്സ് ചെയ്യുക.

1. ഉപയോക്തൃ പ്രോംപ്റ്റ് കൈകാര്യം ചെയ്യുക, അതിനെ LLM-നോട് കൂടാതെ ക്ലയന്റ് ലിസ്റ്റുചെയ്ത ടൂളുകളും നല്‍കി.

നല്ലത്, നാം കൂടെ ഹൈ ലെവലിൽ ഇത് എങ്ങനെ ചെയ്യാമെന്ന് മനസ്സിലാക്കി, ഇപ്പോൾ താഴെയുള്ള പ്രവർത്തനത്തിൽ ഇത് പരീക്ഷിക്കാം.

## അഭ്യാസം: LLM ഉള്ള ക്ലയന്റ് സൃഷ്‌ടിക്കൽ

ഈ അഭ്യാസത്തിൽ, നമ്മൾ നമ്മുടെ ക്ലയന്റിൽ LLM ചേർക്കുന്നത് പഠിക്കും.

### GitHub Personal Access Token ഉപയോഗിച്ച് പ്രാമാണീകരണം

GitHub ടോക്കൺ സൃഷ്‌ടിക്കൽ എളുപ്പമാണ്. ഇതാ എങ്ങനെ ചെയ്യാം:

- GitHub സെറ്റിംഗ്സിലേക്ക് പോയി – ടോപ്പ് വലതുഭാഗത്തെ നിങ്ങളുടെ പ്രൊഫൈൽ ചിത്രത്തിൽ ക്ലിക്കുചെയ്യുക, Settings തിരഞ്ഞെടുക്കുക.
- Developer Settings നാവിഗേറ്റ് ചെയ്യുക – താഴേക്ക്_SCROLL ചെയ്ത് Developer Settings തിരഞ്ഞെടുക്കുക.
- Personal Access Tokens തിരഞ്ഞെടുക്കുക – Fine-grained tokens ക്ലിക്കുചെയ്യുക, പിന്നീട് Generate new token.
- നിങ്ങളുടെ ടോകൺ കോൺഫിഗർ ചെയ്യുക – റഫറൻസിന് ഒരു കുറിപ്പ് ചേർക്കുക, കാലഹരണ തീയതി സജ്ജമാക്കുക, ആവശ്യമായ സ്കോപ്പുകൾ (പരമിഷനുകൾ) തിരഞ്ഞെടുക്കുക. ഈ കേസിൽ Models അനുവാദം ചേർക്കാൻ ഉറപ്പുവരുത്തുക.
- Generated ടോക്കൺ കോപ്പി ചെയ്ത് സൂക്ഷിക്കുക – Generate token ക്ലിക്ക് ചെയ്യുക, ഉടനടി കോപ്പി ചെയ്യുക, പിന്നീട് കാണാനാകില്ല.

### -1- സേർവറിനോട് കണക്ട് ചെയ്യുക

നാം ആദ്യം നമ്മുടെ ക്ലയന്റ് സൃഷ്‌ടിക്കാം:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // സ്കീമ സ്ഥിരീകരണത്തിനായി zod ഇറക്കുമതി ചെയ്യുക

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
  
മുന്‍പുള്ള കോഡിൽ നാം:

- ആവശ്യമുള്ള ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു
- രണ്ട് അംഗങ്ങൾ ഉള്ള ക്ളാസ് സൃഷ്‌ടിച്ചു, `client` ഉം `openai` ഉം, ക്ലയന്റ് കൈകാര്യം ചെയ്യാനും LLM-ുമായി ഇടപെടാനും സഹായിക്കും.
- നമ്മുടെ LLM ഉദാഹരണം GitHub Models ഉപയോഗിക്കാൻ കോൺഫിഗർ ചെയ്തു, `baseUrl` inference API-യിലേക്കായി സജ്ജീകരിച്ചു.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio കണക്ഷനു വേണ്ടി സെര്‍വര്‍ പാരാമീറ്ററുകള്‍ സൃഷ്ടിക്കുക
server_params = StdioServerParameters(
    command="mcp",  # നിർവ്വഹണസാദ്ധ്യമാകുന്ന
    args=["run", "server.py"],  # ജീവസാഹായ കമാന്‍ഡ് ലൈന്‍ വാദങ്ങള്‍
    env=None,  # ജീവസാഹായ പരിസ്ഥിതി വ്യത്യാസങ്ങള്‍
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # കണക്ഷന്‍ തുടക്കം കുറിക്കുക
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```
  
മുന്‍പുള്ള കോഡിൽ നാം:

- MCP ന് ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു
- ക്ലയന്റ് സൃഷ്‌ടിച്ചു

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
  
#### Java

ആദ്യമേ, നിങ്ങളുടെ `pom.xml` ഫയലിൽ LangChain4j ഡിപെൻഡൻസികൾ ചേർക്കണം. MCP ഇന്റഗ്രേഷൻ, GitHub Models പിന്തുണയ്ക്കാൻ ആവശ്യമായ ഡിപെൻഡൻസികൾ ചേർക്കുക:

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
  
ശേഷം നിങ്ങളുടെ ജാവ ക്ലയന്റ് ക്ലാസ് സൃഷ്‌ടിക്കുക:

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
    
    public static void main(String[] args) throws Exception {        // GitHub മോഡലുകൾ ഉപയോഗിക്കുന്നതിന് LLM കോൺഫിഗർ ചെയ്യുക
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // സെർവറുമായി കണക്ട് ചെയ്യുന്നതിനുള്ള MCP ട്രാൻസ്പോർട്ട് സൃഷ്ടിക്കുക
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
  
മുന്‍പുള്ള കോഡിൽ നാം:

- **LangChain4j ഡിപെൻഡൻസികൾ ചേർത്തു**: MCP ഇന്റഗ്രേഷൻ, OpenAI ഔദ്യോഗിക ക്ലയന്റ്, GitHub Models പിന്തുണ
- **LangChain4j ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു**: MCP ഇന്റഗ്രേഷൻ, OpenAI ചാറ്റ് മോഡൽ ഫങ്ഷണാലിറ്റി
- **`ChatLanguageModel` സൃഷ്‌ടിച്ചു**: GitHub Models ഉപയോഗിച്ച് നിങ്ങളുടെ GitHub ടോക്കണുമായി കോൺഫിഗർ ചെയ്തു
- **HTTP ട്രാൻസ്പോർട്ട് സജ്ജമാക്കി**: MCP സേർവറുമായി കണക്ട് ചെയ്യാൻ Server-Sent Events (SSE) ഉപയോഗിച്ചു
- **MCP ക്ലയന്റ് സൃഷ്‌ടിച്ചു**: സേർവറുമായി ആശയവിനിമയം കൈകാര്യം ചെയ്യാൻ
- **LangChain4j-ന്റെ ഇൻബിൽറ്റ് MCP പിന്തുണ ഉപയോഗിച്ചു**: LLM-നും MCP സേർവറിനും ഇടയിൽ ഇന്റഗ്രേഷൻ ലളിതമാക്കി

#### Rust

ഈ ഉദാഹരണം Rust അടിസ്ഥാനമാക്കിയ MCP സേർവർ പ്രവർത്തനക്ഷമമാണെന്ന് فرضിച്ചു. ഇല്ലെങ്കിൽ, [01-first-server](../01-first-server/README.md) പാഠത്തിന് മടക്കം പോയി സേർവർ സൃഷ്‌ടിക്കുക.

Rust MCP സേർവ്വർ ഉണ്ടെങ്കിൽ, ടെർമിനൽ തുറന്ന് സേർവർ ഉള്ള ഡയറക്ടറിയിലേക്ക് പോകുക. പിന്നെ പുതിയ LLM ക്ലയന്റ് പ്രോജക്ട് സൃഷ്‌ടിക്കാൻ താഴെയുള്ള കമാൻഡ് എക്സിക്യൂട്ട് ചെയ്യുക:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```
  
നിങ്ങളുടെ `Cargo.toml` ഫയലിൽ താഴെ കാണുന്ന ഡിപെൻഡൻസികൾ ചേർക്കുക:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```
  
> [!NOTE]  
> OpenAI-യ്ക്കുള്ള ഔദ്യോഗിക Rust ലൈബ്രറി ഇല്ല. എന്നാൽ, `async-openai` crate ഒരു [കമ്യൂണിറ്റി നയിക്കുന്ന ലൈബ്രറി](https://platform.openai.com/docs/libraries/rust#rust) ആണ്, വ്യാപകമായി ഉപയോഗിക്കുന്നതും.

`src/main.rs` ഫയൽ തുറന്ന് താളത്തിന്റെ ഉള്ളടക്കം താഴെക്കൊടുക്കുന്ന കോഡുമായി മാറ്റുക:

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

    // TODO: MCP ടൂൾ ലിസ്റ്റിങ് നേടുക

    // TODO: ഉപകരണ കോൾസോടൊപ്പം LLM സംഭാഷണം

    Ok(())
}
```
  
ഈ കോഡ് ഒരു അടിസ്ഥാന Rust ആപ്പ് സജ്ജമാക്കുന്നു, MCP സേർവറുമായി GitHub Models համար LLM ഇടപാട് നടത്താൻ.

> [!IMPORTANT]  
> GitHub ടോക്കൺ ഉപയോഗിച്ച് `OPENAI_API_KEY` എൻവർൺമെന്റ് 변수 സജ്ജമാക്കുന്നത് ഉറപ്പ് വരുത്തുക.

നല്ലത്, അടുത്ത ഘട്ടം സെർവറിലെ കഴിവുകൾ ലിസ്റ്റുചെയ്യുക.

### -2- സേർവർ കഴിവുകൾ ലിസ്റ്റുചെയ്യുക

ഇപ്പോൾ നാം സേർവറുമായി കണക്ട് ചെയ്ത് അതിന്റെ കഴിവുകൾ ചോദിക്കും:

#### Typescript

അഭിപ്രായ ക്ലാസിൽ താഴെയുള്ള മെത്തഡുകൾ ഉൾപ്പെടുത്തുക:

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
  
മുൻ കോഡിൽ നാം:

- സേർവറുമായി കണക്ട് ചെയ്യാനുള്ള `connectToServer` കോഡ് ചേർത്തു.
- ഒരു `run` മെത്തഡ് സൃഷ്‌ടിച്ചു, അത് ആപ്പ് ഫ്ലോ കൈകാര്യം ചെയ്യും. ഇതുവരെ ടൂളുകൾ മാത്രം ലിസ്റ്റ് ചെയ്യുന്നു, പിന്നീട് കൂടുതൽ ചേർക്കും.

#### Python

```python
# ലഭ്യമായ വിഭവങ്ങൾ പട്ടികചെയ്യുക
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ലഭ്യമായ ഉപകരണങ്ങൾ പട്ടികചെയ്യുക
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```
  
ചേർത്തത്ഹाइएकोത്:

- റിസോഴ്‌സുകളും ടൂളുകളും ലിസ്റ്റ് ചെയ്ത് പ്രിന്റ് ചെയ്തു. ടൂളുകൾക്കായി `inputSchema` കൂടി ലിസ്റ്റ് ചെയ്തു, ഇത് പിന്നീട് ഉപയോഗിക്കും.

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
  
മുൻ കോഡിൽ:

- MCP സേർവറിൽ ലഭ്യമായ ടൂളുകൾ ലിസ്റ്റ് ചെയ്‌തു
- ഓരോ ടൂളിനും അതിന്റെ പേര്, വിവരണം, സ്കീമ എന്നിവ ലിസ്റ്റ് ചെയ്തു. സ്കീമ പിന്നീട് ഈ ടൂളുകൾ വിളിക്കുവാൻ ഉപയോഗിക്കും.

#### Java

```java
// സ്വയം MCP ഉപകരണങ്ങൾ കണ്ടെത്തുന്ന ഒരു ടൂൾ പ്രൊവൈഡർ സൃഷ്ടിക്കുക
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ടൂൾ പ്രൊവൈഡർ സ്വയം കൈകാര്യം ചെയ്യുന്നത്:
// - MCP സർവറിൽ നിന്ന് ലഭ്യമായ ഉപകരണങ്ങളുടെ ലിസ്റ്റിംഗ്
// - MCP ടൂൾ സ്കീമകളെ LangChain4j ഫോർമാറ്റിലേക്ക് മാറ്റൽ
// - ഉപകരണം പ്രവർത്തനം மற்றும் പ്രതികരണങ്ങൾ കൈകാര്യം ചെയ്യൽ
```
  
മുൻ കോഡിൽ നാം:

- MCP സേർവറിൽ നിന്നുള്ള എല്ലാ ടൂളുകളും സ്വയം കണ്ടെത്തി രജിസ്റ്റർ ചെയ്യുന്ന `McpToolProvider` സൃഷ്‌ടിച്ചു
- ടൂൾ പ്രൊവൈഡർ MCP ടൂൾ സ്കീമകളും LangChain4j ടൂൾ ഫോർമാറ്റും അന്വയിച്ച് കൈകാര്യം ചെയ്യുന്നു
- ഇത് ടൂൾ ലിസ്റ്റിംഗ്, കൺവർഷൻ നിർബന്ധിതമാക്കുന്ന പ്രക്രിയ ഒഴിവാക്കുന്നു

#### Rust

MCP സേർവറിൽ നിന്നും ടൂൾസ് `list_tools` മെത്തഡ് ഉപയോഗിച്ച് ലഭിക്കും. `main` ഫംഗ്ഷനിൽ MCP ക്ലയന്റ് സജ്ജീകരിച്ച ശേഷം താഴെ കാണുന്ന കോഡ് ചേർക്കുക:

```rust
// MCP ടൂൾ ലിസ്റ്റിംഗ് നേടുക
let tools = mcp_client.list_tools(Default::default()).await?;
```
  
### -3- സേർവർ കഴിവുകൾ LLM ടൂളുകളായി പരിവർത്തനം ചെയ്യുക

സേർവർ കഴിവുകൾ ലിസ്റ്റാക്കിയതിനു ശേഷം അത് LLM മനസ്സിലാകുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റണം. തുടർന്ന് ഈ കഴിവുകൾ LLM-നെ ടൂളുകളായി നൽകാം.

#### TypeScript

1. MCP സേർവർ റിസ്പോൺസിന് LLM ഉപയോഗിക്കാൻ ടൂൾ ഫോർമാറ്റിലേക്ക് പരിവർത്തനം ചെയ്യാൻ താഴെ കാണുന്ന കോഡ് ചേർക്കുക:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ഇൻപുട്ട്_സ്കീമയുടെ അടിസ്ഥാനത്തില്‍ ഒരു സോഡ് സ്കീമ സൃഷ്ടിക്കുക
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // തരം "ഫംഗ്ഷൻ" ആയി വ്യക്തമായി സജ്ജമാക്കുക
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
  
    മുകളിൽ കാണുന്ന കോഡ് MCP സേർവറിന്റെ റിസ്പോൺസ് LLM മനസ്സിലാക്കുന്ന ടൂൾ ഡെഫിനിഷൻ ഫോർമാറ്റിലേക്ക് മാറ്റുന്നു.

1. പിന്നീട് `run` മെത്തഡ് ഇങ്ങനെ അപ്‌ഡേറ്റ് ചെയ്യാം, സെർവർ കഴിവുകൾ ലിസ്റ്റ് ചെയ്യാൻ:

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
  
    മുൻ കോഡിൽ, `run` മെത്തഡ് ഫലത്തിലൂടെ മാപ്പ് ചെയ്തു, ഓരോ എൻട്രിക്കും `openAiToolAdapter` വിളിക്കുന്നു.

#### Python

1. ആദ്യം, താഴെ കാണുന്ന കൺവെർട്ടർ ഫംഗ്ഷൻ സൃഷ്‌ടിക്കുക

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
  
    `convert_to_llm_tools` ഫംഗ്ഷൻ MCP ടൂൾ റിസ്പോൺസ് LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റുന്നു.

1. പിന്നീട്, ഈ ഫംഗ്ഷൻ ഉപയോഗിച്ച് ക്ലയന്റ് കോഡ് ഇങ്ങനെ അപ്‌ഡേറ്റ് ചെയ്യാം:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```
  
    ഇവിടെ, MCP ടൂൾ റിസ്പോൺസ് LLM-നായി പരിവർത്തനം ചെയ്യാൻ `convert_to_llm_tool` വിളിക്കുന്നു.

#### .NET

1. MCP ടൂൾ റിസ്പോൺസ് LLM മനസ്സിലാക്കുന്ന രൂപത്തിലേക്ക് പരിവർത്തനം ചെയ്യാൻ താഴെ കാണുന്ന കോഡ് ചേർക്കുക:

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
  
മുൻ കോഡിൽ:

- നാമം, വിവരം, ഇൻപുട്ട് സ്കീമ ഉപഗ്രഹിച്ച് `ConvertFrom` ഫംഗ്ഷൻ സൃഷ്‌ടിച്ചു.
- ഇത് FunctionDefinition സൃഷ്‌ടിക്കുന്നു, ChatCompletionsDefinition-നു പാസ് ചെയ്യുന്നു. LLM ഈ ഫോർമാറ്റ് മനസ്സിലാക്കും.

1. ഈ ഫംഗ്ഷൻ ഉപയോഗിക്കാൻ കയറിയിരിക്കുന്ന കോഡ് ഇങ്ങനെ അപ്‌ഡേറ്റ് ചെയ്യാം:

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
// സ്വാഭാവിക ഭാഷാ ഇടപെടലിനുള്ള ബോട്ട് ഇന്റർഫേസ് സൃഷ്ടിക്കുക
public interface Bot {
    String chat(String prompt);
}

// LLM এবং MCP ഉപകരണങ്ങളുള്ള AI സേവനം ക്രമീകരിക്കുക
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```
  
മുൻ കോഡിൽ:

- സ്വാഭാവിക ഭാഷാ ഇടപാടുകൾക്കുള്ള ലളിതമായ `Bot` ഇന്റർഫേസ് ഡിഫൈൻ ചെയ്തു
- LangChain4j-ന്റെ `AiServices` ഉപയോഗിച്ച് LLM MCP ടൂൾ പ്രൊവൈഡറുമായി ഓട്ടോമാറ്റിക്കായി ബന്ധപ്പെടുത്തി
- ഫ്രെയിമ്വർക്കിൽ ടൂൾ സ്കീമ പരിവർത്തനം, ഫംഗ്ഷൻ കോളുകൾ സജീവമായി കൈകാര്യം ചെയ്യും
- ഈ സമീപനം മാനുവൽ ടൂൾ പരിവർത്തനം ഒഴിവാക്കും, LangChain4j MCP ടൂളുകൾ LLM-ഓടേക്ക് കെട്ടിപ്പടുക്കുന്നു

#### Rust

MCP ടൂൾ റിസ്പോൺസ് LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റാൻ സഹായകമായ ഒരു ഹെൽപ്പർ ഫംഗ്ഷൻ ചേർക്കാം. `main` ഫംഗ്ഷൻ താഴെ ഈ കോഡ് ചേർക്കുക. ഇത് LLM-നോട് അഭ്യർത്ഥനകൾ നൽകുമ്പോൾ ഉപയോഗിക്കും:

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
  
നല്ലത്, ഇനി ഉപയോക്തൃ അഭ്യർത്ഥന കൈകാര്യം ചെയ്യാൻ സജ്ജമാണ്.

### -4- ഉപയോക്തൃ പ്രോംപ്റ്റ് അഭ്യർത്ഥന കൈകാര്യം ചെയ്യുക

ഇതിൽ, ഉപയോക്തൃ അഭ്യർത്ഥന കൈകാര്യം ചെയ്യും.

#### TypeScript

1. LLM-നെ വിളിക്കാൻ ഉപയോഗിക്കുന്ന ഒരു മെത്തഡ് ചേർക്കുക:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. സർവറിന്റെ ടൂൾ വിളിക്കുക
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ഫലവുമായി എന്തും ചെയ്യുക
        // TODO

        }
    }
    ```
  
    മുൻ കോഡിൽ:

    - `callTools` എന്ന ഒരു മെത്തഡ് ചേർത്തു.
    - ഈ മെത്തഡ് LLM ഫലത്തെ പരിശോധിച്ച് ഏത് ടൂളുകൾ വിളിക്കണമെന്ന് തീരുമാനിക്കുന്നു:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ടൂൾ വിളിക്കുക
        }
        ```
  
    - LLM ടൂൾ കോളിംഗ് നിർദേശിക്കുന്നുവെങ്കിൽ ടൂൾ വിളിക്കുന്നു:

        ```typescript
        // 2. സെര്‍വറിന്റെ ഉപകരണം വിളിക്കുക
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ഫലത്തെക്കൊണ്ട് എന്തെങ്കിലും ചെയ്യുക
        // ചെയ്യേണ്ടത്
        ```
  
1. `run` മെത്തഡ് ഇങ്ങനെ അപ്‌ഡേറ്റ് ചെയ്യുക, LLM വിളിക്കുകയും `callTools` ഉപയോഗിക്കുകയും ചെയ്യാൻ:

    ```typescript

    // 1. LLMന്‌ ഇൻপുട്ട് ആയി സന്ദേശങ്ങൾ സൃഷ്ടിക്കുക
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM നെ വിളിക്കുക
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM പ്രതികരണം പരിശോധിക്കുക, ഓരോ തിരഞ്ഞെടുപ്പിനും ടൂൾ കോളുകൾ ഉള്ളതാണോ എന്ന് പരിശോധിക്കുക
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```
  
നല്ലത്, പൂർണ്ണ കോഡ് താഴെ കാണുക:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // സ്കീമാ സ്ഥിരീകരണത്തിന് zod ഇമ്പോർട്ട് ചെയ്യുക

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ഭാവിയിൽ ഈ URL മാറ്റേണ്ടി വരാം: https://models.github.ai/inference
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
            type: "function" as const, // type "function" ആയി വ്യക്തമാക്കുക
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
    
          // 3. ഫലവുമായി എന്തെങ്കിലും ചെയ്യുക
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM പ്രതികരണം വഴി പോകുക, ഓരോ തിരഞ്ഞെടുപ്പിനും ടൂൾ കോളുകൾ ഉണ്ടോ എന്ന് പരിശോധിക്കുക
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

1. LLM വിളിക്കാനായി ആവശ്യമായ ഇറക്കുമതികൾ ചേർക്കുക:

    ```python
    # എൽഎൽഎം
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```
  
1. LLM-നെ വിളിക്കുന്ന ഫംഗ്ഷൻ ചേർക്കുക:

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
  
    മുൻ കോഡിൽ:

    - MCP സേർവറിൽ നിന്നുള്ള ടൂളുകൾ LLM-നോപ്പിയ്ക്കായി പാസാണ്.
    - തുടർന്ന്, അവർക്ക് LLM വിളിച്ചു.
    - ഫലത്തെ പരിശോധിച്ച് ഏതെല്ലാം ഫംഗ്ഷനുകൾ വിളിക്കണമെന്ന് നോക്കുന്നു.
    - അവസാനമായി, വിളിക്കേണ്ട ഫംഗ്ഷനുകളുടെ ലിസ്റ്റ് നൽകുന്നു.

1. അവസാന ഘട്ടം, പ്രധാന കോഡ് അപ്‌ഡേറ്റ് ചെയ്യുക:

    ```python
    prompt = "Add 2 to 20"

    # എന്തെങ്കിലും ഉണ്ടെങ്കിൽ, ഉപയോഗിക്കുന്ന ഉപകരണങ്ങൾ ഏവൊന്നാണ് എന്ന് LLM-നോട് ചോദിക്കുക
    functions_to_call = call_llm(prompt, functions)

    # നിർദ്ദേശിച്ച ഫംഗ്ഷനുകൾ വിളിക്കുക
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```
  
    കോഡിൽ:

    - LLM-ന്റെ നിർദ്ദേശം പ്രകാരം MCP ടൂൾ `call_tool` വഴി വിളിക്കുന്നു.
    - ടൂൾ കോളിന്റെ ഫലം MCP സേർവറിൽ പ്രിന്റ് ചെയ്യുന്നു.

#### .NET

1. LLM പ്രോംപ്റ്റ് അഭ്യർത്ഥനക്കുള്ള കോഡ് ചേർക്കുക:

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
  
    മുൻ കോഡിൽ:

    - MCP സേർവറിൽ നിന്ന് ടൂളുകൾ നേടി, `var tools = await GetMcpTools()`   
    - ഉപയോക്തൃ പ്രോംപ്റ്റ് നിർവ്വചിച്ചു `userMessage`  
    - മോഡൽ, ടൂളുകൾ ഉൾപ്പടെ ഓപ്ഷൻസ് ഒബ്ജക്റ്റ് സൃഷ്‌ടിച്ചു  
    - LLM-നെ അഭ്യർത്ഥന അയച്ചു

1. LLM ഫംഗ്ഷൻ കോളുകൾ നിർദ്ദേശിക്കുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക:

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
  
    മുൻ കോഡിൽ:

    - ഫംഗ്ഷൻ കോളുകളുടെ ലിസ്റ്റിൽ ലൂപ്പ് ചെയ്തു.
    - ഓരോ ടൂൾ കോളിലും പേര്, ആർഗ്യുമെന്റുകൾ പാർസ് ചെയ്തു MCP ക്ലയന്റ് വഴി ടൂൾ വിളിച്ചു.
    - ഫലം പ്രിന്റ് ചെയ്തു.

പൂർണ്ണ കോഡ് ഇതാണ്:

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
  
#### Java

```java
try {
    // എംസി.പി. ഉപകരണങ്ങൾ സ്വയം ഉപയോഗിച്ച് പ്രകൃതിഭാഷാ അഭ്യർത്ഥനകൾ പ്രവർത്തിപ്പിക്കുക
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
  
മുൻ കോഡിൽ:

- ലളിതമായ സ്വാഭാവിക ഭാഷ പ്രോംപ്റ്റുകൾ MCP ടൂളുകളുമായി ഇടപഴകാൻ ഉപയോഗിച്ചു
- LangChain4j ഫ്രെയിംവർക്ക് ഇതെല്ലാം സ്വയം കൈകാര്യം ചെയ്യുന്നു:
  - ആവശ്യപ്പെട്ടപ്പോൾ ഉപയോക്തൃ പ്രോംപ്റ്റുകൾ ടൂൾ കോളുകളായി മാറ്റൽ
  - LLM നിഷ്‌ചയപ്രകാരം അനുയോജ്യമായ MCP ടൂളുകൾ വിളിക്കൽ
  - LLM-നും MCP സേർവറിനും ഇടയിൽ സംഭാഷണ പ്രവാഹം നിയന്ത്രണം
- `bot.chat()` സ്വാഭാവിക ഭാഷാ പ്രതികരണങ്ങൾ നൽകും, MCP ടൂൾ പ്രവർത്തന ഫലങ്ങൾ ഉൾപ്പെടെ
- ഇതു ഉപയോക്തൃക്കൾക്ക് MCP നടപ്പാക്കൽ അറിയാതെ seamless അനുഭവം നൽകുന്നു

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

പിട്ടായി ഇവിടെയാണ് പ്രധാന പ്രവർത്തി നടക്കുന്നത്. ആദ്യം ഉപയോക്താവ് നൽകിയ പ്രോംപ്റ്റോടെ LLM-നെ വിളിക്കും, പിന്നീട് പ്രതികരണം പരിശോധിച്ച് ടൂളുകൾ വിളിക്കേണ്ടതുണ്ടോ എന്ന് നോക്കും. ഉണ്ടെങ്കിൽ, ആ ടൂളുകൾ വിളിച്ച് LLM-നൊപ്പം സംഭാഷണം തുടരും, റിപ്പോർട്ട് ക്രമംമാറും വരെ തുടരും.

LLM-നെ പല പ്രാവശ്യം വിളിക്കേണ്ടിവരും, അതിനാൽ LLM വിളി കൈകാര്യം ചെയ്യുന്ന ഒരു ഫംഗ്ഷൻ നിർവ്വചിക്കാം. ഈ ഫംഗ്ഷൻ `main.rs` ഫയലിൽ ചേർക്കുക:

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
  
ഈ ഫംഗ്ഷൻ LLM ക്ലയന്റ്, സന്ദേശങ്ങളുടെ ലിസ്റ്റ് (ഉപയോക്തൃ പ്രോംപ്റ്റ് ഉൾപ്പെടെ), MCP സേർവറിലെ ടൂളുകൾ സ്വീകരിച്ച് LLM-ന് അഭ്യർത്ഥന അയക്കുകയും മറുപടി നൽകുകയും ചെയ്യും.
LLM ൽ നിന്നുള്ള പ്രതികരണം `choices` എന്നൊരു നിര ഉൾക്കൊള്ളും. ഏതെങ്കിലും `tool_calls` ഉണ്ടോയെന്ന് പരിശോധിക്കാൻ നമുക്ക് ഫലം പ്രോസസ്സുചെയ്യാൻ വേണം. LLM ഒരു പ്രത്യേക ടൂൾ ഉദ്‌ഘാടിക്കണമെന്ന് അഭ്യർത്ഥിക്കുന്നുവെന്ന് ഈ വഴി നമുക്ക് മനസിലാകും, അത് ആർക്ക്യൂമെന്റുകൾക്കിൾപ്പോ ൽ വിളിക്കേണ്ടതാണ്. LLM പ്രതികരണത്തെ കൈകാര്യം ചെയ്യാൻ താഴെ കൊടുത്ത കോഡ് നിങ്ങളുടെ `main.rs` ഫയലിന്റെ ചുവട്ടിൽ ചേർക്കുക:

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

    // ഉള്ളടക്കം ലഭ്യമെങ്കിൽ അച്ചടിക്കുക
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ടൂളുകളുടെ വിളികൾ കൈകാര്യം ചെയ്യുക
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // അസിസ്റ്റന്റ് സന്ദേശം ചേർക്കുക

        // ഓരോ ടൂൾ വിളിയും നടപ്പിലാക്കുക
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // സന്ദേശങ്ങളിൽ ടൂൾ ഫലം ചേർക്കുക
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ടൂൾ ഫലങ്ങളുമായി സംഭാഷണം തുടരു 
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


`tool_calls` ഉണ്ടെങ്കിൽ, അത് ടൂൾ വിവരങ്ങൾ എടുക്കും, MCP സെർവർ ടൂൾ അഭ്യർത്ഥനയോട് കൂട്ടി വിളിക്കും, ഫലങ്ങൾ സംഭാഷണ സന്ദേശങ്ങളിലേക്ക് ചേർക്കുന്നു. തുടർന്ന് LLM-നൊപ്പം സംഭാഷണം തുടരുകയും സന്ദേശങ്ങൾ അസിസ്റ്റന്റിന്റെ പ്രതികരണവും ടൂൾ കോളിന്റെ ഫലങ്ങളും ഉപയോഗിച്ച് അപ്ഡേറ്റ് ചെയ്യപ്പെടുകയും ചെയ്യും.

LLM MCP കോളുകൾക്കായി നൽകുന്ന ടൂൾ കോളിന്റെ വിവരങ്ങൾ പുറം എടുക്കാൻ നമുക്ക് മറ്റൊരു സഹായക ഫംഗ്ഷൻ ചേർക്കാം. വിളിക്കാനുള്ള എല്ലാ വിവരങ്ങളും എടുക്കാൻ താഴെ കൊടുത്ത കോഡ് നിങ്ങളുടെ `main.rs` ഫയലിന്റെ ചുവട്ടിൽ ചേർക്കുക:

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


എല്ലാ ഘടകങ്ങളും ഒരുമിച്ചപ്പോൾ, പ്രാഥമിക ഉപയോക്തൃ പ്രോംപ്റ്റും LLM-നെ കാൾ ചെയ്യലും കൈകാര്യം ചെയ്യാൻ നമുക്ക് സാദ്ധ്യമാക്കാം. നിങ്ങളുടെ `main` ഫംഗ്ഷൻ താഴെ കൊടുത്ത കോഡ് ഉൾപ്പെടുത്തുക:

```rust
// ടൂൾ കോളുകളോടുള്ള LLM സംഭാഷണം
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


ഇത് രണ്ട്കണക്കുകളുടെ മൊത്തം ചോദിച്ചുകൊണ്ട് പ്രാഥമിക ഉപയോക്തൃ പ്രോംപ്റ്റുമായി LLM-നെ ചോദ്യം ചെയ്യും, പ്രതികരണം പ്രോസസ് ചെയ്ത് ടൂൾ കോളുകൾ ചലിപ്പിക്കുന്നു.

നല്ലത്, നിങ്ങൾ വിജയിച്ചു!

## അസൈൻമെന്റ്

വ്യായാമത്തിൽ നിന്നുള്ള കോഡ് എടുത്ത് കൂടുതൽ ടൂളുകളുമായി സെർവർ നിർമ്മിക്കുക. തുടർന്ന് LLM പോലുള്ള ക്ലയന്റ് സൃഷ്ടിച്ച് വ്യത്യസ്ത പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് പരീക്ഷിച്ച് ഉറപ്പാക്കുക നിങ്ങളുടെ എല്ലാ സെർവർ ടൂളുകളും ഡൈനാമിക് ആയി വിളിക്കുന്നത്. ഈ രീതിയിൽ ക്ലയന്റ് നിർമ്മിക്കുന്നത് ഉപയോക്താവിന് മികച്ച അനുഭവം നൽകും, കാരണം അവർ ക്യാംഡ്-സൂചകങ്ങളില്ലാതെ പ്രോംപ്റ്റുകൾ ഉപയോഗിക്കാനും MCP സർവർ വിളിക്കപ്പെടുമ്പോൾ അറിയാതെ കഴിയും.

## പരിഹാരം

[Solution](./solution/README.md)

## പ്രധാന പാഠങ്ങൾ

- MCP സെർവറുകളോട് ഉപയോക്താക്കൾക്ക് മെച്ചപ്പെട്ട സംവാദം നൽകാൻ LLM കൂടി ചേർക്കണം.
- MCP സെർവർ പ്രതികരണം LLM മനസിലാക്കുന്ന രൂപത്തിൽ മാറ്റണം.

## സാമ്പിളുകൾ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## അധിക റിസോഴ്‌സുകൾ

## അടുത്തത് എന്താണ്

- അടുത്തത്: [Visual Studio Code ഉപയോഗിച്ച് സെർവർ ഉപഭോഗം](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**വിവരണം**:  
ഈ ഡോക്യുമെന്റ് AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് പരിശ്രമിച്ചിട്ടുള്ളെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിഴവുകളും അസ്സത്യതകളും ഉണ്ടാകാൻ സാധ്യതയുണ്ട് എന്ന് ദയവായി ശ്രദ്ധിക്കൂ. അസൽ ഭാഷയിലെ ഔദ്യോഗിക ഡോക്യുമെന്റ് മാത്രമേ സർവوث്‌ന വൺമൂലം ആയിരിക്കുകയുള്ളൂ. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മാനവ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകളോ വ്യാഖ്യാനമാറ്റങ്ങളോയ്ക്ക് ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->