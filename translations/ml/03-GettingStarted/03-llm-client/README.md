# LLM ഉപയോഗിച്ച് ക്ലയന്റ് സൃഷ്ടിക്കുന്നത്

> [!NOTE]
> ജാവ ക്ലയന്റ് ഉദാഹരണങ്ങൾ പാരമ്പര്യ HTTP+SSE ട്രാൻസ്പോർട്ടിലൂടെ കണക്ട് ചെയ്യുന്നു, 
> MCP `2025-11-25` SDK API-കളെ ലക്ഷ്യം വച്ചതാണ്. പുതിയ റിമോട്ട് ക്ലയന്റുകൾക്ക് 
> `2026-07-28`-അനുയോജ്യമായ SDKയും Streamable HTTPയും ഉപയോഗിക്കുക.

ഇതുവരെ, നിങ്ങൾ ഒരു സർവർയും ക്ലയന്റും സൃഷ്ടിക്കുന്നത് കണ്ടിട്ടുണ്ട്. താങ്കളുടെ ക്ലയന്റ് സർവറിനെ വ്യക്തമായി വിളിച്ച് അതിന്റെ ടൂളുകൾ, ഉറവിടങ്ങൾ, പ്രോംപ്റ്റുകൾ പട്ടികപ്പെടുത്താൻ സിദ്ധമായിട്ടുണ്ട്. എന്നാൽ, ഇത് വളരെ യാഥാർത്ഥ്യമുള്ള സമീപനം അല്ല. നിങ്ങളുടെ ഉപയോക്താക്കൾ ഏജന്റിക് കാലഘട്ടത്തിലാണ് ജീവിക്കുന്നത്, അവർ പ്രോംപ്റ്റുകളെയും LLM-യുമായും ആശയവിനിമയം നടത്താൻ പ്രതീക്ഷിക്കുന്നു. അവർ MCP നിങ്ങളുടെ ശേഷികൾ സൂക്ഷിക്കാൻ ഉപയോഗിക്കുന്നുണ്ടോ എന്നു പരിഗണിക്കുന്നില്ല; അവർ സ്വാഭാവിക ഭാഷ ഉപയോഗിച്ച് ആശയവിനിമയം നടത്തുമെന്ന് പ്രതീക്ഷിക്കുന്നു. അതിനാൽ, നമുക്ക് ഇത് എങ്ങനെ പരിഹരിക്കാം? പരിഹാരമായത് ക്ലയന്റിന് ഒരു LLM ചേർക്കുന്നതാണ്.

## അവലോകനം

ഈ പാഠത്തിൽ, നാം നിങ്ങളുടെ ക്ലയന്റിൽ LLM ചേർക്കുന്നതിൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കുകയും ഇത് നിങ്ങളുടെ ഉപയോക്താക്കൾക്ക് എങ്ങനെ മികച്ച അനുഭവം നൽകുന്നുവെന്ന് കാണിക്കുകയും ചെയ്യും.

## പഠനലക്ഷ്യങ്ങൾ

ഈ പാഠത്തിന്റെ അവസാനത്തേക്ക്, നിങ്ങൾക്ക് കഴിയുന്നതാണ്:

- LLM ഉള്ള ഒരു ക്ലയന്റ് സൃഷ്ടിക്കുക.
- LLM ഉപയോഗിച്ച് MCP സർവറുമായി സുതാര്യമായ ആശയവിനിമയം നടത്തുക.
- ക്ലയന്റ് വശത്ത് മികച്ച അന്തിമ ഉപയോക്തൃ അനുഭവം നൽകുക.

## സമീപനം

നമുക്ക് നടത്തേണ്ട സമീപനം മനസ്സിലാക്കാം. LLM ചേർക്കുന്നത് എളുപ്പമെന്ന് തോന്നാം, എന്നാൽ നമ്മൾ ഇത് യഥാർത്ഥത്തിൽ നടത്തുമോ?

ഈ രീതിയിൽ ക്ലയന്റ് സർവറുമായി ആശയവിനിമയം നടത്തും:

1. സർവറുമായി കണക്ഷൻ സ്ഥാപിക്കുക.

1. ശേഷികൾ, പ്രോംപ്റ്റുകൾ, ഉറവിടങ്ങളും ടൂളുകളും പട്ടികപ്പെടുത്തുകയും അവയുടെ സ്കീമ സംഭരിച്ചു വെക്കുകയും ചെയ്യുക.

1. LLM ചേർത്ത്, LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിൽ സംഭരിച്ച ശേഷികളും സ്കീമയും കൈമാറുക.

1. ഉപയോക്തൃ പ്രോംപ്റ്റ് കൈകാര്യം ചെയ്യുക, അത് LLM-ലേക്ക് ക്ലയന്റ് പട്ടികപ്പെടുത്തിയ ടൂളുകളുമായി കൈമാറികൊണ്ട്.

ശരിയാണ്, നാം ഇതു മിനിമം ലെവലിൽ എങ്ങനെ ചെയ്യുന്നതാണെന്ന് മനസ്സിലായി, താഴെയുള്ള അഭ്യാസത്തിൽ ഇത് പ്രായോഗികം ചെയ്യാം.

## അഭ്യാസം: LLM ഉള്ള ക്ലയന്റ് സൃഷ്ടിക്കുക

ഈ അഭ്യാസത്തിൽ, നാം നമ്മുടെ ക്ലയന്റിൽ LLM ചേർക്കാൻ പഠിക്കും.

### GitHub വ്യക്തിഗത ആക്സസ് ടോക്കൺ ഉപയോഗിച്ചാണ് പ്രമാണീകരണം

GitHub ടോക്കൺ സൃഷ്ടിക്കുന്നത് ഒരു ലളിതമായ പ്രക്രിയയാണ്. ഇതുപോലെ ചെയ്യാം:

- GitHub സെറ്റിംഗ്സിലേക്ക് പോവുക – മുകളിൽ വലതുവശത്തെ പ്രൊഫൈൽ ചിത്രം ക്ലിക്ക് ചെയ്ത് സെറ്റിംഗ്സ് തിരഞ്ഞെടുക്കുക.
- ഡെവലപ്പർ സെറ്റിംഗ്സിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക – താഴേക്ക് സ്‌ക്രോൾ ചെയ്ത് ഡെവലപ്പർ സെറ്റിംഗ്സ് ക്ലിക്ക് ചെയ്യുക.
- വ്യക്തിഗത ആക്സസ് ടോക്കണുകൾ തിരഞ്ഞെടുക്കുക – ഫൈൻ-ഗ്രെയിൻഡ് ടോക്കണുകൾ ക്ലിക്ക് ചെയ്ത് പുതിയ ടോക്കൺ ജനरेटു ചെയ്യുക.
- നിങ്ങളുടെ ടോക്കൺ കോൺഫിഗർ ചെയ്യുക – റഫറൻസ് കുറിപ്പ് ചേർക്കുക, കാലാവധി നിർദ്ദേശിക്കുക, ആവശ്യമായ സ്‌കോപ്പുകൾ (അനുമതികൾ) തിരഞ്ഞെടുക്കുക. ഈ സാഹചര്യത്തിൽ Models അനുമതി ചേർക്കുന്നത് ഉറപ്പാക്കുക.
- ടോക്കൺ ജനറേറ്റു ചെയ്ത് കോപ്പി ചെയ്യുക – Generate token ക്ലിക്ക് ചെയ്യുക, പിന്നീട് കാണാനാകില്ല, അതിനാൽ ഉടൻ കോപ്പി ചെയ്യുക.

### -1- സർവറിലേക്ക് കണെക്‌ട് ചെയ്യുക

നമുക്ക് പറ്റിയ ക്ലയന്റ് ആദ്യം സൃഷ്ടിക്കാം:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // സ്‌കീമ വിപരിതീകരണത്തിനായി zod ഇറക്കുമതി ചെയ്യുക

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

മുൻ‌കൂറായി നൽകിയ കോഡിൽ നാം:

- ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു
- `client`നും `openai`നും ഉള്ള രണ്ട് അംഗങ്ങളോടുകൂടെ ഒരു ക്ലാസ് സൃഷ്ടിച്ചു, ഇവ ക്ലയന്റിനെ നിയന്ത്രിക്കാൻ LLM-യുമായി ഇടപെടാൻ സഹായിക്കും.
- GitHub Models ഉപയോഗിക്കാൻ `baseUrl` സജ്ജമാക്കി നമ്മുടെ LLM ഇൻസ്റ്റൻസ് കോൺഫിഗർ ചെയ്തു.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio കണക്ഷനുള്ള സെർവർ പാരാമീറ്ററുകൾ സൃഷ്ടിക്കുക
server_params = StdioServerParameters(
    command="mcp",  # നിർവഹിക്കാൻ കഴിയുന്ന ഫയൽ
    args=["run", "server.py"],  # ഐച്ഛിക കമാൻഡ് ലൈൻ_ARGUMENT_കൾ
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

മുൻ‌കൂറായി നൽകിയ കോഡിൽ നാം:

- MCP-ക്കുള്ള ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു
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


ആദ്യം, നിങ്ങളുടെ `pom.xml` ഫയലിൽ LangChain4j ആശ്രിതത്വങ്ങൾ ചേർക്കേണ്ടതാണ്. MCP ഇന്റഗ്രേഷൻക്കും OpenAI-ഉളള MiniMax API-ക്കും സേവനങ്ങൾ നൽകാൻ ഈ ആശ്രിതത്വങ്ങൾ ചേർക്കുക:

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
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

നിങ്ങളുടെ MiniMax API കീയും, ഐച്ഛികമായി, എન્ડ്പോയിന്റും മോഡലും സജ്ജമാക്കുക.
`MINIMAX_MODEL_ID` `MiniMax-M3`നും `MiniMax-M2.7`നും പിന്തുണ നൽകുന്നു. 
`OPENAI_BASE_URL` സജ്ജമാക്കിയിട്ടില്ലെങ്കിൽ, `MINIMAX_REGION` `global_en`-നും `cn_zh`-നും പിന്തുണ നൽകുന്നു.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

അതിന്റെ പകരം, പ്രാദേശിക അടിസ്ഥാനത്തിൽ എണ്ട്പോയിന്റ് തിരഞ്ഞെടുക്കാൻ `OPENAI_BASE_URL` ഒഴിവാക്കുക:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

പിന്നെ നിങ്ങളുടെ ജാവ ക്ലയന്റ് ക്ലാസ് സൃഷ്ടിക്കുക:

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
                .build();

        // സർവറുമായി ബന്ധപ്പെടാൻ MCP ട്രാൻസ്പോർട്ട് സൃഷ്ടിക്കുക
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

മുൻപുള്ള കോഡിൽ നമ്മൾ:

- **LangChain4j ആശ്രിതത്വങ്ങൾ ചേർത്തു**: MCP ഇന്റഗ്രേഷന് വേണ്ടി, OpenAI-ഉളള MiniMax API-ക്കായി ആവശ്യമാണ്.
- **LangChain4j ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു**: MCP ഇന്റഗ്രേഷനും OpenAI ചാറ്റ് മോഡൽ സുഖതക്കും.
- **`ChatLanguageModel` സൃഷ്ടിച്ചു**: MiniMax ഉപയോഗിച്ച് നിങ്ങളുടെ MiniMax API കീ, എന്റ്പോയിന്റ്, പിന്തുണയുള്ള മോഡൽ ID ഉപയോഗിച്ച് കോൺഫിഗർ ചെയ്തു.
- **HTTP ട്രാൻസ്പോർട്ട് സജ്ജമാക്കിയത്**: MCP സർവറിൽ ബന്ധിപ്പിക്കുന്നതിന് Server-Sent Events (SSE) ഉപയോഗിച്ചു.
- **MCP ക്ലയന്റ് സൃഷ്ടിച്ചു**: സർവറുമായി സംവദിക്കാൻ ആവശ്യമായത്.
- **LangChain4j-ന്റെ അടങ്ങിയ MCP പിന്തുണ ഉപയോഗിച്ചു**: LLM-കളും MCP സർവറുകളും തമ്മിൽ എളുപ്പത്തിൽ ഇന്റഗ്രേറ്റ് ചെയ്യാൻ.

#### റസ്റ്റ്

ഈ ഉദാഹരണം നിങ്ങൾക്ക് റസ്റ്റ് MCP സർവർ പ്രവർത്തിക്കുന്നതായി കരുതുന്നു. നിങ്ങൾക്ക് ഉണ്ടാകാത്ത പക്ഷം, സർവർ സൃഷ്ടിക്കാൻ [01-first-server](../01-first-server/README.md) പാഠത്തേക്ക് മടങ്ങി കാണുക.

നിങ്ങളുടെ റസ്റ്റ് MCP സർവർ ഉണ്ടായപ്പോൾ, ഒരു ടെർമിനൽ തുറന്ന് സർവർ ഉള്ള ഡയറക്ടറിയിലേക്ക് പോകുക. പിന്നെ ഒരു പുതിയ LLM ക്ലയന്റ് പ്രോജക്ട് സൃഷ്ടിക്കാൻ താഴെ പറയുന്ന കമാൻഡ് ഓടിക്കുക:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

നിങ്ങളുടെ `Cargo.toml` ഫയലിൽ താഴെപ്പറയുന്ന ആശ്രിതത്വങ്ങൾ ചേർക്കുക:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI-യ്ക്ക് ഔദ്യോഗിക റസ്റ്റ് ലൈബ്രറി ഇല്ല, എന്നാൽ `async-openai` ക്രേറ്റ് [സമൂഹം പരിപാലിക്കുന്ന ലൈബ്രറിയാണ്](https://platform.openai.com/docs/libraries/rust#rust) സാധാരണ ഉപയോഗിക്കുന്നത്.

`src/main.rs` ഫയൽ തുറന്ന്, അതിന്റെ ഉള്ളടക്കം താഴെയുള്ള കോഡോടെ മാറ്റുക:

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
    // ആദ്യ സന്ദേശം
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ക്ലയന്റ് സെറ്റപ്പ് ചെയ്യുക
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ക്ലയന്റ് സെറ്റപ്പ് ചെയ്യുക
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

    // TODO: ടൂൾ કૉલുകളുള്ള LLM സംഭാഷണം

    Ok(())
}
```

ഈ കോഡ് ഒരു അടിസ്ഥാന റസ്റ്റ് അപ്ലിക്കേഷൻ സജ്ജമാക്കുന്നു, അത് MCP സർവറും GitHub മോഡലുകളും LLM സംവാദത്തിനായി ബന്ധിപ്പിക്കും.

> [!IMPORTANT]
> അപ്ലിക്കേഷൻ ഓടിക്കുന്നതിന് മുമ്പ് നിങ്ങളുടെ GitHub ടോക്കണോടൊപ്പം `OPENAI_API_KEY` എൻവയോൺമെന്റ് വേരിയബിൾ സജ്ജമാക്കുക.

അടിപൊടി, അടുത്തപടിയായി, സർവറിലെ ശേഷികൾ പട്ടികപ്പെടുത്താം.

### -2- സർവർ ശേഷികൾ പട്ടികപ്പെടുത്തുക

ഇനി നാം сервറി യുമായ ബന്ധിപ്പിച്ച് അതിന്റെ ശേഷികൾ ചോദിക്കും:

#### ടൈപ്സ്ക്രിപ്റ്റ്

അതേ ക്ലാസിൽ താഴെ കൊടുത്തിട്ടുള്ള മെതഡുകൾ ചേർക്കുക:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ഉപകരണങ്ങൾ പട്ടിക ചെയ്യുന്നു
    const toolsResult = await this.client.listTools();
}
```

മുൻപ് നൽകിയ കോഡിൽ നാം:

-服务器 ബന്ധിപ്പിക്കുന്നതിന് ആവശ്യമായ കോഡ് ചേർത്തു, `connectToServer`.
- ഞങ്ങളുടെ ആപ്പ് ഫ്ലോ നിയന്ത്രിക്കുന്ന `run` മെതഡ് സൃഷ്ടിച്ചു. ഇതുവരെ ഇത് ടൂളുകളുടെ പട്ടിക കാണിക്കുന്നു, എന്നാൽ പിന്നീട് ഇതിൽ കൂടുതൽ ചേർക്കും.

#### പൈത്തൺ

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

- വിഭവങ്ങളും ഉപകരണങ്ങളും പട്ടികപ്പെടുത്തുകയും അവ പ്രിന്റ് ചെയ്യുകയും ചെയ്തു. ഉപകരണങ്ങൾക്ക് `inputSchema` കൂടി പട്ടികപ്പെടുത്തിയിട്ടുണ്ട്, പിന്നീട് ഉപയോഗിക്കും.

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


മുൻവരെയുള്ള കോഡിൽ നാം ചെയ്തിരിക്കുന്നത്:

- MCP സർവറിലുള്ള ലഭ്യമായ ഉപകരണങ്ങൾ പട്ടികപ്പെടുത്തിയത്
- ഓരോ ഉപകരണത്തിനും പേരു, വിവരണം, അതിന്റെ സ്കീമ എന്നിവ പട്ടികപ്പെടുത്തിയിട്ടുണ്ട്. പിന്നീട് നാം ഉപകരണങ്ങൾ വിളിക്കുമ്പോൾ അതാണ് ഉപയോഗിക്കുന്നത്.

#### ജാവ

```java
// MCP ഉപകരണങ്ങളെ സ്വയം കണ്ടെത്തുന്ന ഒരു ടൂൾ പ്രൊവൈഡർ സൃഷ്ടിക്കുക
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ടൂൾ പ്രൊവൈഡർ സ്വয়മേവ കൈകാര്യം ചെയ്യുന്നു:
// - MCP സർവറിൽ നിന്ന് ലഭ്യമായ ഉപകരണങ്ങളുടെ ലിസ്റ്റിംഗ്
// - MCP ടൂൾ സ്കീമകൾ LangChain4j ഫോർമാറ്റിലേക്ക് മാറ്റുന്നത്
// - ഉപകരണങ്ങളുടെ പ്രവർത്തനം ಮತ್ತು പ്രതികരണങ്ങൾ മാനേജ് ചെയ്യുന്നത്
```

മുൻവരെയുള്ള കോഡിൽ നാം ചെയ്തിരിക്കുന്നത്:

- MCP സർവറിലുള്ള എല്ലാ ഉപകരണങ്ങളും സ്വയം കണ്ടെത്തി രജിസ്റ്റർ ചെയ്യുന്ന `McpToolProvider` സൃഷ്‌ടിച്ചത്
- MCP ടൂൾ സ്കീമുകളുമായി LangChain4jയുടെ ഉപകരണം ഫോർമാറ്റിനുള്ള മാറ്റം ടൂൾ പ്രൊവൈഡർ നയർ‌വഹിക്കുന്നു
- ഇത് മാനുവൽ ടൂൾ പട്ടികപ്പെടുത്തലും മാറ്റവും ഒഴിവാക്കുന്ന രീതിയാണ്

#### റസ്റ്റ്

MCP സർവറിൽനിന്നുുത്ത് ഉപകരണങ്ങൾ ഏറ്റെടുക്കുന്നത് `list_tools` മെത്തഡിന്റെ സഹായത്തോടെയാണ്. നിങ്ങളുടെ `main` ഫങ്ഷനിൽ MCP ക്ലയന്റ് സെറ്റ്‌അപ്പ് ചെയ്ത ശേഷം താഴെയുള്ള കോഡ് ചേർക്കുക:

```rust
// MCP ടൂൾ ലിസ്റ്റിംഗ് നേടുക
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- സർവർ കഴിവുകൾ LLM ടൂളുകളാക്കിയെടുക്കുക

സർവർ കഴിവുകൾ പട്ടികപ്പെടുത്തിയ ശേഷമാണ് അടുത്തഘട്ടം അവയെ LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റുക. അതിനു ശേഷം നാം ഈ കഴിവുകൾ ടൂളുകളായി നമുക്ക് നൽകാം.

#### ടൈപ്പ്‌സ്ക്രിപ്റ്റ്

1. MCP സർവറിൽ നിന്നുള്ള മറുപടി LLM ഉപയോഗിക്കാവുന്ന ടൂൾ ഫോർമാറ്റിലേക്ക് മാറ്റാൻ താഴെ കാഴ്ചപ്പാട് ചേർക്കുക:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ഇൻപുട്ട്_സ്കീമ വികസിപ്പിച്ചെടുത്ത് ഒരു സോഡ് സ്കീമ സൃഷ്‌ടിക്കുക
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

    ```

    മേൽപ്പറഞ്ഞ കോഡ് MCP സർവറിൽ നിന്നുള്ള മറുപടി സ്വീകരിച്ച് LLM മനസ്സിലാക്കുന്ന ടൂൾ നിർവചന ഫോർമാറ്റിലേക്ക് മാറ്റുന്നു.

2. അടുത്ത്, സരവർ കഴിവുകൾ പട്ടികപ്പെടുത്താൻ `run` മെത്തഡ് അപ്ഡേറ്റ് ചെയ്യാം:

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

    മുൻവരെയുള്ള കോഡിൽ, ഫലം വഴി മാപ്പ് ചെയ്ത് ഓരോ എൻട്രിക്കും `openAiToolAdapter` വിളിക്കുന്നു എന്ന രീതിയിൽ `run` മെത്തഡ് അപ്ഡേറ്റ് ചെയ്തിട്ടുണ്ട്.

#### പൈതൺ

1. ആദ്യം, താഴെ കാണുന്ന പരിവർത്തക ഫങ്ഷൻ സൃഷ്‌ടിക്കാം

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

    മേൽപ്പറഞ്ഞ `convert_to_llm_tools` ഫങ്ഷനിൽ MCP ടൂൾ മറുപടി സ്വീകരിച്ച് LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്കായി മാറ്റുന്നു.

2. പിന്നീട്, ക്ലയന്റ് കോഡ് ഈ ഫങ്ഷൻ ഉപയോഗിക്കാൻ അപ്ഡേറ്റ് ചെയ്യാം:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ഇവിടെ, MCP ടൂൾ മറുപടിയെ LLM ക്ക് നൽകുന്നതിനായി `convert_to_llm_tool` വിളിക്കുന്നു.

#### .NET

1. MCP ടൂൾ മറുപടി LLM മനസ്സിലാക്കുന്ന രൂപത്തിലേക്ക് മാറ്റുന്ന കോഡ് ചേർക്കാം

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

മുൻവരെയുള്ള കോഡിൽ നാം ചെയ്തിരിക്കുന്നത്:

- പേരു, വിവരണം, ഇൻപുട്ട് സ്കീമ എന്നിവ സ്വീകരിക്കുന്ന `ConvertFrom` ഫങ്ഷൻ സൃഷ്‌ടിച്ചതും
- അത് FunctionDefinition രൂപത്തിലാക്കുകയും, അത് ChatCompletionsDefinition ൽ പാസാക്കുകയും ചെയ്യുന്ന പ്രവർത്തനം നിർവഹിച്ചു. പിന്നീട് LLM ഇതിനേ മനസ്സിലാക്കും.

2. ഈ ഫങ്ഷൻ പ്രയോജനം കണ്ട് നിലവിലുള്ള കോഡ് അപ്ഡേറ്റ് ചെയ്യാം:

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
// സ്വാഭാവിക ഭാഷ ഇന്ററാക്ഷനுக்கായി ബോട്ട് ഇന്റർഫേസ് സൃഷ്‌ടിക്കുക
public interface Bot {
    String chat(String prompt);
}

// LLM, MCP ഉപകരണങ്ങളുമായി AI സേവനം കൺഫിഗർ ചെയ്യുക
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

മുൻ വർന്ന കോഡിൽ നാം ചെയ്തുണ്ട്:

- സ്വാഭാവിക ഭാഷ ഇടപെടലുകൾക്കായി ലളിതമായ `Bot` ഇന്റർഫേസ് നിർവചിച്ചത്
- MCP ടൂൾ പ്രൊവൈഡറുമായി LLM സ്വയം ബന്ധിപ്പിക്കാൻ LangChain4jന്റെ `AiServices` ഉപയോഗിച്ചത്
- ടെക്കാം സ്കീം മാറ്റവും ഫങ്ഷൻ കോളിംഗ് എല്ലാം ഫ്രെയിംവർക്ക് സ്വയമായി കൈകാര്യം ചെയ്യുന്നു
- ഇത് മാനുവൽ ടൂൾ മാറ്റം ഒഴിവാക്കി - MCP ടൂളുകളെ LLM-സാധുവായ ഫോർമാറ്റിലേക്ക് മാറ്റുന്നത് LangChain4j തന്നെ ചെയ്യുന്നു

#### റസ്റ്റ്

MCP ടൂൾ മറുപടി LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റാൻ ഉപകരണ പട്ടിക ഫോർമാറ്റ് ചെയ്യുന്ന ഹelper ഫങ്ഷൻ ചേർക്കും. നിങ്ങളുടെ `main.rs` ഫയലിൽ `main` ഫങ്ഷൻ താഴെ താഴെ കൊടുക്കുന്ന കോഡ് ചേർക്കുക. ഇത് LLM അറിയിപ്പുകൾക്കായി വിളിക്കപ്പെടും:

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


നന്നായി, നാം ഉപയോക്തൃ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യാൻ നിർദ്ദിഷ്ടമല്ല, അതുകൊണ്ട് അടുത്തതായി അത് പരിഹരിക്കാം.

### -4- ഉപയോക്തൃ പ്രോംപ്റ്റ് അഭ്യർത്ഥന കൈകാര്യം ചെയ്യുക

കോഡിന്റെ ഈ ഭാഗത്തിൽ, നാം ഉപയോക്തൃ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യും.

#### ടൈപ്പ്‌സ്‌ക്രിപ്റ്റ്

1. നമ്മുടെ LLM-നെ വിളിക്കാൻ ഉപയോഗിക്കപ്പെടുന്ന ഒരു മെത്തഡ് ചേർക്കുക:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. സെര്‍വറിന്റെ ടൂൾ വിളിക്കുക
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ഫലത്തോടെ എന്തെങ്കിലും ചെയ്യുക
        // ചെയ്യാൻ ഉണ്ട്

        }
    }
    ```

    മുൻപത്തെ കോഡിൽ നാം:

    - `callTools` എന്ന മെത്തഡ് ചേർത്തു.
    - മെത്തഡ് ഒരു LLM പ്രതികരണം എടുക്കുന്നു, ഏത് ഉപകരണങ്ങൾ വിളിക്കപ്പെട്ടിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുന്നു, ഉണ്ടെങ്കിൽ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ടൂൾ വിളിക്കുക
        }
        ```

    - LLM വിളിക്കണമെന്ന് സൂചിപ്പിച്ചാൽ ഒരു ഉപകരണം വിളിക്കുന്നു:

        ```typescript
        // 2. സർവറിന്റെ ഉപകരണം വിളിക്കുക
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ഫലത്തോടൊപ്പം എന്തങ്കിലുമൊരു പ്രവൃത്തി ചെയ്യുക
        // ചെയ്യേണ്ടതാണ്
        ```

2. `run` മെത്തഡ് LLM-നെ വിളിക്കുകയും `callTools` വിളിക്കുകയും ഉൾപ്പെടുന്നപടിയായി അപ്ഡേറ്റ് ചെയ്യുക:

    ```typescript

    // 1. LLM-ന്റെ ഇൻപുട്ടായി ഉള്ള സന്ദേശങ്ങൾ സൃഷ്ടിക്കുക
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

    // 3. LLM-ന്റെ പ്രതികരണം കാണുക, ഓരോ തിരഞ്ഞെടുപ്പിനും, അതിൽ ടൂൾ കോൾസ് ഉണ്ടോ എന്ന് പരിശോധിക്കുക
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

നിങ്ങൾക്ക്, പൂർണ്ണ കോഡ് പട്ടികപ്പെടുത്താം:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // സ്കീമ പരിശോധനയ്ക്ക് zod ഇറക്കുമതി ചെയ്യുക

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ഭാവിയില്‍ ഈ url മാറ്റേണ്ടിവരാമാകും: https://models.github.ai/inference
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
          // input_schema ആധാരമാക്കി ഒരു zod സ്കീമ സൃഷ്ടിക്കുക
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // വ്യക്തമായി ടൈപ്പ് "function" ആക്കി സജ്ജമാക്കുക
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
    
    
          // 2. സെര്‍വറിന്റെ ഉപകരണം വിളിക്കുക
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
    
        // 3. LLM പ്രതികരണത്തിലിലൂടെ പോകുക, ഓരോ തെരഞ്ഞെടുത്തതിനും ഉപകരണം വിളികൾ ഉണ്ടോ എന്ന് പരിശോധിക്കുക
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

#### പൈത്തൺ

1. LLM-നെ വിളിക്കാൻ ആവശ്യമായ ചില ഇറക്കുമതികൾ ചേർക്കാം

    ```python
    # എൽഎൽഎം
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. തുടർന്ന്, LLM-നെ വിളിക്കുന്ന ഫംഗ്ഷൻ ചേർക്കാം:

    ```python
    # എൽ‌എൽഎം

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

    മുൻപത്തെ കോഡിൽ നാം:

    - MCP സർവറിൽ കണ്ടെത്തിയ, മാറ്റം ചെയ്ത ഫംഗ്ഷനുകൾ LLM-ന് പാസ്സ് ചെയ്തു.
    - ഇപ്പോൾ ആ ഫംഗ്ഷനുകളാൽ LLM-നെ വിളിച്ചു.
    - തുടർന്ന് ഫലം പരിശോധിച്ച്, ഏത് ഫംഗ്ഷനുകൾ വിളിക്കണമെന്ന് തീരുമാനിക്കുന്നു, ഉണ്ടെങ്കിൽ.
    - അവസാനം വിളിക്കേണ്ട ഫംഗ്ഷനുകളുടെ അറേ പാസ്സ് ചെയ്യുന്നു.

3. അവസാന ഘട്ടം, പ്രധാന കോഡ് അപ്ഡേറ്റ് ചെയ്യാം:

    ```python
    prompt = "Add 2 to 20"

    # ഏതെങ്കിലും ടൂളുകൾ ഉണ്ടെങ്കിൽ LLM-ന് ചോദിക്കുക
    functions_to_call = call_llm(prompt, functions)

    # നിർദ്ദേശിച്ച ഫംഗ്ഷനുകൾ വിളിക്കുക
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    അവിടെ, മുകളിൽ നൽകിയ കോഡിന്റെ അവസാന ഘട്ടത്തിൽ:

    - `call_tool` വഴി MCP ഉപകരണം വിളിക്കുന്നു, LLM നമുക്ക് വിളിക്കേണ്ടെന്ന് തോന്നിയ ഫംഗ്ഷൻ അടിസ്ഥാനമാക്കി.
    - ഉപകരണം വിളിച്ചതിന്റെ ഫലം MCP സർവറിലേക്ക് പ്രിന്റ് ചെയ്യുന്നു.

#### .NET

1. LLM പ്രോംപ്റ്റ് അഭ്യർ‍ത്ഥന ചെയ്യാനുള്ള കോഡ് കാണിക്കാം:

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

    മുൻപ് നൽകിയ കോഡിൽ നാം:

    - MCP സർവറിൽ നിന്നുള്ള ഉപകരണങ്ങൾ ലഭിച്ചു, `var tools = await GetMcpTools()` എന്നു.
    - ഒരു ഉപയോക്തൃ പ്രോംപ്റ്റ് `userMessage` നിർവചിച്ചു.
    - മോഡൽ, ഉപകരണങ്ങൾ ചേർത്ത ഓപ്ഷൻസ് объект് നിർമ്മിച്ചു.
    - LLM-ലേക്ക് അഭ്യർത്ഥന അയച്ചു.

2. അവസാന ഘട്ടം, LLM ഫംഗ്ഷൻ വിളിക്കേണ്ടതായി കരുതി എന്നോഅ തോമസ് പരിശോധിക്കാം:

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

    മുൻപത്തെ കോഡിൽ നാം:

    - ഫംഗ്ഷൻ കോൾകളുടെ ലിസ്റ്റ് ലൂപ്പ് ചെയ്തു.
    - ഓരോ ഉപകരണം കോൾക്കും, പേര്, ആഗ്യൂമെന്റുകൾ പാഴ്സ് ചെയ്ത് MCP ക്ലയന്റ് വഴി MCP സർവറിൽ ഉപകരണം വിളിച്ചു. അവസാനം ഫലങ്ങൾ പ്രിന്റ് ചെയ്തു.

പൂർണ്ണ കോഡ് ഇങ്ങനെ:

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

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### ജാവ

```java
try {
    // MCP ടൂളുകൾ സ്വയം ഉപയോഗിച്ച് പ്രകൃതി ഭാഷാനുരോധങ്ങൾ നടപ്പിലാക്കുക
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

മുൻപ് നൽകിയ കോഡിൽ നാം:

- MCP സർവർ ഉപകരണങ്ങളുമായി സ്വഭാവസഹജ ഭാഷ പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ചു സംവദിച്ചു
- LangChain4j ഫ്രെയിംവർക്ക് സ്വയംസൂക്ഷ്മമായി:
  - ആവശ്യമായപ്പോൾ ഉപയോക്തൃ പ്രോംപ്റ്റുകൾ ഉപകരണങ്ങൾ വിളിക്കലായി മാറ്റുന്നു
  - LLM ന്റെ തീരുമാനത്തിന്റെ അടിസ്ഥാനത്തിലാണ് MCP യന്ത്രങ്ങൾ വിളിക്കുന്നത്
  - LLM-നും MCP സർവറും ഇടയിലുള്ള സംഭാഷണ പ്രവാഹം കൈകാര്യം ചെയ്യുന്നു
- `bot.chat()` മെത്തഡ് സ്വഭാവസഹജ ഭാഷ മറുപടികൾ നൽകുന്നു, അതിൽ MCP ഉപകരണങ്ങൾ നിർവഹിച്ച ഫലങ്ങളും ഉണ്ടാകാം
- ഉപയോക്താക്കൾക്ക് MCP അടിസ്ഥാന ഘടനയെ പറ്റി അറിയേണ്ടതില്ലാത്ത, എളുപ്പവുമായ അനുഭവം ഈ റീതി നൽകുന്നു

പൂർണ്ണ കോഡ് ഉദാഹരണം:

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

#### റസ്റ്റ്


ഇടപെടൽ工作的 പ്രധാനഭാഗം ഇവിടെ നടക്കുന്നു. നാം പ്രാരംഭ ഉപയോക്തൃ പ്രോംപ്റ്റുമായി LLM നെ വിളിക്കും, ശേഷം മറുപടിയെ പ്രോസസ് ചെയ്ത് ഏതെങ്കിലും ഉപകരണങ്ങൾ വിളിക്കേണ്ടതുണ്ടോ എന്ന് പരിശോധിക്കും. ആവശ്യമുണ്ടെങ്കിൽ, ആ ഉപകരണങ്ങൾ വിളിച്ച് LLM-നൊപ്പം സംഭാഷണം തുടരും, കൂടുതൽ ഉപകരണ വിളിപ്പുകൾ ആവശ്യമില്ലാതാകുന്നത് വരെ, പിന്നെ നാം ചূണ്ടിക്കാട്ടുന്ന അവസാന പ്രതികരണമുണ്ടാകും.

നാം LLM-നോട് പലവിധ വിളിപ്പുകൾ നടത്തും, അതിനാൽ LLM വിളി കൈകാര്യം ചെയ്യുന്ന ഒരു ഫംഗ്ഷൻ നിർവചിക്കാം. താഴെ കൊടുത്തിരിക്കുന്ന ഫംഗ്ഷന് നിങ്ങളുടെ `main.rs` ഫയലിൽ ചേർക്കുക:

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

ഈ ഫംഗ്ഷൻ LLM ക്ലയന്റ്, സന്ദേശങ്ങളുടെ സജ്ജികാം (ഉപയോക്തൃ പ്രോംപ്റ്റ് ഉൾപ്പെടെ), MCP സർവറിലുള്ള ഉപകരണങ്ങൾ സ്വീകരിച്ച്, LLM-നോട് രജിസ്റ്റർ ചെയ്ത് മറുപടി നൽകുന്നു.

LLM-യിലെ മറുപടി ഒരു `choices` എന്ന ആറെ ആയിരിക്കും ഉൾക്കൊള്ളുന്നത്. നാം ഫലത്തെ പ്രോസസ് ചെയ്ത് ലഭിക്കുന്ന `tool_calls` ഉണ്ടോ എന്ന് പരിശോധിക്കേണ്ടതാണ്. ഇത് LLM ഒരു പ്രത്യേക ഉപകരണം ആവശ്യപ്പെടുന്നുവെന്ന് കാണിക്കും, അനുയോജ്യമായ എargumentsുകൾ കൂടെ നൽകിയിരിക്കുന്നു. താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് നിങ്ങളുടെ `main.rs` ഫയലിന്റെ അടിഭാഗത്തിൽ ചേർത്ത് LLM പ്രതികരണം കൈകാര്യം ചെയ്യാനുള്ള ഫംഗ്ഷൻ നിർവചിക്കുക:

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

    // ഉപകരണം വിളികൾ കൈകാര്യം ചെയ്യുക
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // സഹായകന്റെ സന്ദേശം ചേർക്കുക

        // ഓരോ ഉപകരണം വിളിയും നടപ്പിലാക്കുക
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ഉപകരണം ഫലങ്ങൾ സന്ദേശങ്ങളിൽ ചേർക്കുക
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ഉപകരണ ഫലങ്ങളോടെ സംഭാഷണം തുടരണം
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

`tool_calls` ഉള്ളപ്പോൾ, അത് ഉപകരണ വിവരങ്ങൾ പുറന്തള്ളുന്നു, MCP സർവർ ഉപകരണ അഭ്യർത്ഥനയോടെ വിളിക്കുന്നു, ഫലങ്ങൾ സംഭാഷണ സന്ദേശങ്ങളിൽ ചേർക്കുന്നു. തുടർന്ന് LLM-നോട് സംവാദം തുടരും, സന്ദേശങ്ങൾ അസിസ്റ്റന്റിന്റെ പ്രതികരണവും ഉപകരണം വിളിച്ച ഫലങ്ങളും ഉൾപ്പെടുത്തി പുതുക്കപ്പെടുന്നു.

MCP വിളിപ്പുകൾക്കായി LLM മടക്കത്തിൽ ഉണ്ടാക്കുന്ന ഉപകരണ വിളിപ്പിന്റെ വിവരങ്ങൾ എടുക്കാൻ ഒരു സഹായക ഫംഗ്ഷൻ കൂടി ചേർക്കാം. താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് നിങ്ങളുടെ `main.rs` ഫയലിന്റെ അടിഭാഗത്തിൽ ചേർക്കുക:

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

എല്ലാ ഭാഗങ്ങളും സജ്ജമാക്കിയതോടെ, പ്രാരംഭ ഉപയോക്തൃ പ്രോംപ്റ്റ് കൈകാര്യം ചെയ്ത് LLM വിളിക്കാം. നിങ്ങളുടെ `main` ഫംഗ്ഷൻ താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ഉൾപ്പെടുത്തുന്നതായി അപ്ഡേറ്റ് ചെയ്യുക:

```rust
// ടൂൾ കോൾസ് ഉൾപ്പെടുന്ന LLM സംഭാഷണം
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

ഇത് പ്രാരംഭ ഉപയോക്തൃ പ്രോംപ്റ്റ് ഉപയോഗിച്ച് LLM-നെ ചോദിക്കും, രണ്ടുവിധ സംഖ്യകളുടെ റെഷ്യിസ് ചോദിക്കുകയാണ്, മറുപടി പ്രോസസ് ചെയ്തുകൊണ്ട് ഉപകരണ വിളികളെ സുഗമമായി കൈകാര്യം ചെയ്യും.

നല്ലതു, നിങ്ങൾ അതെ ചെയ്തു!

## അസൈൻമെന്റ്

അഭ്യാസത്തിൽ നിന്നുള്ള കോഡ് എടുത്ത് കൂടുതൽ ഉപകരണങ്ങളുള്ള ഒരു സർവർ നിർമ്മിക്കുക. പിന്നെ അഭ്യാസത്തിലെ പോലെ LLM ഉള്ള ക്ലയന്റ് സൃഷ്ടിച്ച് വ്യത്യസ്തമായ പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് സുഖകരമായി പരീക്ഷിക്കുക, നിങ്ങളുടെ സർവർ ഉപകരണങ്ങൾ ഡൈനാമിക് ആയി വിളിക്കപ്പെടുന്നു എന്ന് ഉറപ്പാക്കുക. ഇത്തരത്തിലുള്ള ക്ലയന്റ് നിർമ്മാണം ഉപയോഗിച്ച് അവസാനം ഉപയോക്താവിന് മികച്ച അനുഭവം നൽകും, കാരണം അവർ കൃത്യമായ ക്ലയന്റ് കമാൻഡുകൾ ഉപയോഗിക്കുന്നതിന് പകരം പ്രോംപ്റ്റുകൾ ഉപയോഗിക്കാം, MCP സർവർ വിളിക്കാൻ അവർ അറിഞ്ഞിരിക്കും പോലും ആവശ്യമില്ല.

## പരിഹാരം

[Solution](./solution/README.md)

## പ്രധാന സിദ്ധാന്തങ്ങൾ

- MCP സർവറുമായി നിങ്ങളുടെ ക്ലയന്റിന് LLM ചേർക്കുന്നത് ഉപയോക്താക്കൾക്കായി നല്ല ഇടപെടലിന്റെ മാർഗമാണ്.
- MCP സർവർ മറുപടികൾ LLM മനസിലാക്കുന്ന രൂപത്തിലേക്ക് പരിവർത്തനം ചെയ്യേണ്ടതാണ്.

## സാമ്പിൾസുകൾ

- [Java കാൽക്കുലേറ്റർ](../samples/java/calculator/README.md)
- [.Net കാൽക്കുലേറ്റർ](../../../../03-GettingStarted/samples/csharp)
- [JavaScript കാൽക്കുലേറ്റർ](../samples/javascript/README.md)
- [TypeScript കാൽക്കുലേറ്റർ](../samples/typescript/README.md)
- [Python കാൽക്കുലേറ്റർ](../../../../03-GettingStarted/samples/python)
- [Rust കാൽക്കുലേറ്റർ](../../../../03-GettingStarted/samples/rust)

## അധിക വൻകിടവഴികൾ

## അടുത്തത് എന്താണ്

- അടുത്തത്: [Visual Studio Code ഉപയോഗിച്ച് സർവർ ഉപഭോക്തൃ ചെയ്യൽ](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->