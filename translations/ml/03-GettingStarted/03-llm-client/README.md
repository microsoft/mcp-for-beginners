# LLM ഉപയോഗിച്ച് ക്ലയന്റ് സൃഷ്ടിക്കുകയാണ്

ഇതുവരെ, നിങ്ങൾ എങ്ങനെ ഒരു സെർവറും ഒരു ക്ലയന്റും സൃഷ്ടിക്കാമെന്ന് കണ്ടിട്ടുണ്ട്. ക്ലയന്റ് തങ്ങളുടെ ഉപകരണങ്ങൾ, സ്രോതസ്സുകൾ, പ്രോംപ്റുകൾ ലിസ്റ്റ് ചെയ്യാൻ സെർവറെ വ്യക്തമായി വിളിക്കുമായിരുന്നു. എന്നിരുന്നാലും, ഇത് വളരെ പ്രായോഗികമായ സമീപനം അല്ല. നിങ്ങളുടെ ഉപയോക്താക്കൾ ഏജന്റിക് യുഗത്തിൽ ജീവിക്കുന്നു, പ്രോംപ്റുകൾ ഉപയോഗിച്ച് LLM (ലാർജ് ലാംഗ്വേജ് മോഡൽ) ഒപ്പം ആശയവിനിമയം നടത്താൻ പ്രതീക്ഷിക്കുന്നു. നിങ്ങളുടെ കഴിവുകൾ MCPയിൽ സംഭരിക്കുന്നുവോ അല്ലയോ എന്നത് അവർക്ക് പ്രാധാന്യമില്ല; അവർ സ്വാഭാവിക ഭാഷ ഉപയോഗിച്ച് ഇടപഴകാനാണ് പ്രതീക്ഷിക്കുന്നത്. ഈ പ്രശ്നം എങ്ങനെ പരിഹരിക്കാം? പരിഹാരം ക്ലയന്റിൽ ഒരു LLM ചേർക്കുകയാണു.

## അവലോകനം

ഈ പാഠത്തിൽ, LLM ക്ലയന്റിന് ചേർക്കുന്നതിൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കുകയും ഇത് ഉപയോക്താവിന് എങ്ങനെ വളരെയധികം മെച്ചപ്പെട്ട അനുഭവം നൽകുന്നതിൻറെ പ്രദർശനവും നടത്തുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം അവസാനിച്ചതോടെ, നിങ്ങൾക്ക് കഴിയുന്നതാണ്:

- LLM ഉള്ള ഒരു ക്ലയന്റ് സൃഷ്ടിക്കുക.
- MCP സെർവർ LLM ഉപയോഗിച്ച് സുലഭമായി ഇടപഴകുക.
- ക്ലയന്റ് ഭാഗത്ത് മെച്ചപ്പെട്ട ഉപഭോക്തൃ അനുഭവം നൽകുക.

## സമീപനം

നമ്മൾ എടുക്കേണ്ട സമീപനം മനസ്സിലാക്കാൻ ശ്രമിക്കാം. LLM ചേർക്കുന്നത് ലളിതമെന്നു തോന്നാം, പക്ഷേ നാം അത് യാഥാര്‍ഥ്യം ആക്കുമെന്ന് ഓർക്കേണ്ടതുണ്ടോ?

ക്ലയന്റ് സെർവറുമായി ഇങ്ങനെ ഇടപഴകും:

1. സെർവറുമായി കണക്ഷൻ സ്ഥാപിക്കുക.

1. കഴിവുകൾ, പ്രോംപ്റുകൾ, സ്രോതസ്സുകൾ, ഉപകരണങ്ങൾ ലിസ്റ്റ് ചെയ്ത് അവരുടെ സ്കീമ സംഭരിച്ചു വെക്കുക.

1. ഒരു LLM ചേർത്തു, സംഭരിച്ച കഴിവുകളും സ്കീമയും LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിൽ കൈമാറുക.

1. ഉപയോക്താവിന്റെ പ്രോംപ്റ്റ് കൈകാര്യം ചെയ്ത്, അത് ഉപകരണങ്ങളുമായി ചേർന്ന് LLM-ന് കൈമാറുക.

മികവുറ്റത്, ഇപ്പോൾ നാം ഇതു ഉയർന്ന തലത്തിൽ എങ്ങനെ ചെയ്യാമെന്ന് മനസ്സിലാക്കിയിട്ടുണ്ട്, താഴെയുള്ള വ്യായാമത്തിൽ ഇത് പരീക്ഷിക്കാം.

## വ്യായാം: LLM ഉപയോഗിച്ച് ക്ലയന്റ് സൃഷ്ടിക്കൽ

ഈ വ്യായാമത്തിൽ, ഞങ്ങൾ എങ്ങനെ LLM നമ്മുടെ ക്ലയന്റിൽ ചേർക്കാമെന്ന് പഠിക്കും.

### GitHub പേഴ്സണൽ ആക്സസ് ടോക്കൺ ഉപയോഗിച്ച് പ്രാമാണീകരണം

GitHub ടോക്കൺ സൃഷ്ടിക്കൽ ഒരു ലളിതമായ പ്രക്രിയയാണ്. ഇതു ചെയ്യാൻ കഴിയുന്ന വിധം:

- GitHub സെറ്റിംഗ്സിലേക്ക് പോവുക – മുകളിൽ വലതുവശത്തെ പ്രൊഫൈൽ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്ത് സെറ്റിംഗ്സ് തിരഞ്ഞെടുക്കുക.
- ഡെവലപ്പർ സെറ്റിംഗ്സിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക – താഴേക്ക് സ്ക്രോൾ ചെയ്ത് ഡെവലപ്പർ സെറ്റിംഗ്സ് ക്ലിക്ക് ചെയ്യുക.
- പേഴ്സണൽ ആക്സസ് ടോക്കൺസ് തിരഞ്ഞെടുക്കുക – ഫൈൻ-ഗ്രെയ്ന്ഡ് ടോക്കൺസ് ക്ലിക്ക് ചെയ്ത് പുതിയ ടോക്കൺ ജനറേറ്റ് ചെയ്യുക.
- ടോക്കൺ കോൺഫിഗർ ചെയ്യുക – റഫറൻസിനായി ഒരു കുറിപ്പ് ചേർക്കുക, കാലാവധി ക്രമീകരിക്കുക, ആവശ്യമായ സ്കോപ്പുകൾ തിരഞ്ഞെടുക്കുക (പരമിഷനുകൾ). ഈ കേസിൽ മോഡൽസ് പർമിഷൻ ചേർക്കാൻ ശ്രദ്ധിക്കുക.
- ടോക്കൺ ജനറേറ്റ് ചെയ്ത് കോപ്പി ചെയ്യുക – ടോക്കൺ ജനറേറ്റ് ചെയ്ത് ഉടൻ കോപ്പി ചെയ്യുക, ഒരു തവണ മാത്രമാണ് കാണാനാകുക.

### -1- സെർവറുമായി കണ.connect ചെയ്യുക

നാം ആദ്യം നമ്മുടെ ക്ലയന്റ് സൃഷ്ടിക്കാം:

#### ടൈപ്പ്സ്ക്രിപ്റ്റ്

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // സ്കീമ പരിശോധനക്ക് വേണ്ടി zod ഇംപോർട്ട് ചെയ്യുക

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

എന്ന പുല്ലിലെ കോഡിൽ ഞങ്ങൾ:

- ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു
- `client` എന്നും `openai` എന്നും രണ്ട് അംഗങ്ങളുള്ള ക്ലാസ് സൃഷ്‌ടിച്ചു, ഇത് ഓരോന്നും ക്ലയന്റ് മാനേജ്മെന്റിനും LLM-ഉം ഇടപഴകുന്നതിനും സഹായിക്കുന്നു.
- GitHub Models ഉപയോഗിക്കാൻ LLM ഇൻസ്റ്റൻസ് `baseUrl` ഇൻഫറൻസ് API-യിലേക്ക് പോയിന്റ് ചെയ്യുന്നത് ക്രമീകരിച്ചു.

#### പൈത്തൺ

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio കണക്ഷനായി സർവർaaringാളുകൾ സൃഷ്‌ടിക്കുക
server_params = StdioServerParameters(
    command="mcp",  # നിർവഹണ യോഗ്യമായത്
    args=["run", "server.py"],  # ഐച്ഛിക കമാൻഡ് ലൈനിലെ arguments
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

മുന്നിലുള്ള കോഡിൽ ഞങ്ങൾ:

- MCPക്ക് ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു
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

ആദ്യം, നിങ്ങളുടെ `pom.xml` ഫയലിൽ LangChain4j ആശ്രിതങ്ങൾ ചേർക്കണം. MCP ഇന്റഗ്രേഷനും OpenAI-ഉം പൊരുത്തപ്പെടുന്ന MiniMax API സഹായിക്കുന്നതിനും ഈ ആശ്രിതങ്ങൾ ചേർക്കുക:

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

നിങ്ങളുടെ MiniMax API കീ, ഓപ്ഷണൽ ആയി എൻഡ്‌പോയിന്റ്, മോഡൽ ക്രമീകരിക്കുക.
`MINIMAX_MODEL_ID` `'MiniMax-M3'`നും `'MiniMax-M2.7'`നും പിന്തുണ വക്കുന്നു. 
`OPENAI_BASE_URL` ക്രമീകരിക്കാത്ത പക്ഷം `MINIMAX_REGION` `'global_en'`നും `'cn_zh'`നും പിന്തുണ വക്കുന്നു.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

പ്രദേശം പ്രകാരം എൻഡ്‌പോയിന്റ് തിരഞ്ഞെടുക്കാൻ, `OPENAI_BASE_URL` ഒഴിവാക്കുക:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
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

        // സെർവറുമായി ബന്ധങ്ങൾ കെട്ടിപ്പടുക്കാൻ MCP ട്രാൻസ്പോർട്ട് നിർമ്മിക്കുക
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

മുന്നിലുള്ള കോഡിൽ ഞങ്ങൾ:

- **LangChain4j ആശ്രിതങ്ങൾ ചേർത്തു**: MCP ഇന്റഗ്രേഷനും OpenAI പൊരുത്തപ്പെടുന്ന MiniMax API-ക്കും ആവശ്യമായത്
- **LangChain4j ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്തു**: MCP ഇന്റഗ്രേഷനും OpenAI ചാറ്റ് മോഡൽ പ്രവർത്തനത്തിനും
- **`ChatLanguageModel` സൃഷ്ടിച്ചു**: നിങ്ങളുടെ MiniMax API കീ, എൻഡ്‌പോയിന്റ്, പിന്തുണയുള്ള മോഡൽ ഐഡി ഉപയോഗിച്ച് MiniMax-നെ ക്രമീകരിച്ചു
- **HTTP ട്രാൻസ്പോർട്ട് ക്രമീകരിച്ചു**: MCP സെർവറുമായി ബന്ധിപ്പിക്കാൻ Server-Sent Events (SSE) ഉപയോഗിച്ചു
- **MCP ക്ലയന്റ് സൃഷ്ടിച്ചു**: സെർവറുമായി ആശയവിനിമയം കൈകാര്യം ചെയ്യുന്നതിന്
- **LangChain4jയുടെ MCP സപ്പോർട്ട് ഉപയോഗിച്ചു**: LLM-കളും MCP സെർവറുകളും തമ്മിലുള്ള ഇന്റഗ്രേഷൻ ലളിതമാക്കുന്നു

#### റസ്റ്റ്

ഈ ഉദാഹരണം ഒരു റസ്റ്റ് അധിഷ്ഠിത MCP സെർവർ പ്രവർത്തനത്തിലാണെന്ന് فرضിച്ചുള്ളതാണ്. നിങ്ങൾക്ക് ഇല്ലെങ്കിൽ, [01-first-server](../01-first-server/README.md) പാഠത്തിലേക്ക് മടങ്ങി സെർവർ സൃഷ്ടിക്കുക.

റസ്റ്റ് MCP സെർവർ നിങ്ങൾക്കുണ്ടായെങ്കിൽ, ടെർമിനൽ തുറന്ന് സെർവറിന്റെ തത്സമയ ഡയറക്ടറിയിലേക്ക് പോവുക. പിന്നെ, പുതിയ LLM ക്ലയന്റ് പ്രോജക്റ്റ് സൃഷ്ടിക്കാൻ താഴെ കൊടുത്ത കമാൻഡ് പ്രവർത്തിപ്പിക്കുക:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

നിങ്ങളുടെ `Cargo.toml` ഫയലിൽ താഴെ കാണുന്ന ആശ്രിതങ്ങൾ ചേർക്കുക:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> ഔദ്യോഗികമായ OpenAI റസ്റ്റ് ലൈബ്രറി ഇല്ല, പക്ഷേ `'async-openai'` ക്രേറ്റ് ഒരു [കമ്മ്യൂണിറ്റി പരിപാലിത ലൈബ്രറിയാണ്](https://platform.openai.com/docs/libraries/rust#rust) സാധാരണയായി ഉപയോഗിക്കുന്നത്.

`src/main.rs` ഫയൽ തുറന്ന് അതിന്റെ ഉള്ളടക്കം താഴെ കാണിക്കുന്ന കോഡിലേക്ക് മാറ്റുക:

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

    // OpenAI ക്ലയന്റ് സജ്ജീകരിക്കുക
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ക്ലയന്റ് സജ്ജീകരിക്കുക
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

    // TODO: ടൂൾ കോൾസിനൊപ്പം LLM സംഭാഷണം

    Ok(())
}
```

ഈ കോഡ് ഒരു അടിസ്ഥാന റസ്റ്റ് അപ്ലിക്കേഷൻ സജ്ജമാക്കുന്നു, അത് MCP സെർവറിനും GitHub Models-ഉം LLM ഇടപഴകലിനുമായി ബന്ധിപ്പിക്കും.

> [!IMPORTANT]
> അപ്ലിക്കേഷൻ പ്രവർത്തിപ്പിക്കുന്നതിന് മുമ്പ് നിങ്ങളുടെ GitHub ടോക്കൺ ഉൾപ്പെടുത്തി `OPENAI_API_KEY` എൻവയേൺമെന്റ് വേരിയബിൾ ക്രമീകരിക്കാൻ ശ്രദ്ധിക്കണം.

സാരമായി, ഇനി നാം സെർവറിന്റെ കഴിവുകൾ ലിസ്റ്റ് ചെയ്യുക.

### -2- സെർവർ കഴിവുകൾ ലിസ്റ്റ് ചെയ്യുക

ഇനി ഞങ്ങൾ സെർവറുമായി കണക്ട് ചെയ്ത് അതിന്റെ കഴിവുകൾ ചോദിക്കും:

#### ടൈപ്പ്സ്ക്രിപ്റ്റ്

അവിടെ ഉണ്ടാകുന്ന ക്ലാസിൽ താഴെ വരികൾ ചേർക്കുക:

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

മുന്നിലുള്ള കോഡിൽ ഞങ്ങൾ:

- സെർവറുമായി കണക്ട് ചെയ്യാനുള്ള കോഡ് ചേർത്തു, `connectToServer`.
- നമ്മുടെ ആപ്പ് ഫ്ലോ കൈകാര്യം ചെയ്യാനുള്ള ഒരു `run` മെത്തഡ് സൃഷ്ടിച്ചു. ഇതുവരെ ഉപകരണങ്ങൾ മാത്രം ലിസ്റ്റ് ചെയ്യുന്നു, പക്ഷേ പിന്നീട് കൂട്ടിച്ചേർക്കും.

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

ഞങ്ങൾ ചേർത്തതെന്ന്:

- സ്രോതസ്സുകളും ഉപകരണങ്ങളും ലിസ്റ്റ് ചെയ്ത് പ്രിന്റ് ചെയ്തു. ഉപകരണങ്ങൾക്കായി, നാം പിന്നീട് ഉപയോഗിക്കുന്ന `inputSchema`-യും ലിസ്റ്റ് ചെയ്തു.

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

മുന്നിലുള്ള കോഡിൽ ഞങ്ങൾ:

- MCP സെർവറിൽ ലഭ്യമായ ഉപകരണങ്ങൾ ലിസ്റ്റ് ചെയ്തു
- ഓരോ ഉപകരണത്തിനും നാമം, വിവരണം, സ്കീമ എന്നിവ ലിസ്റ്റ് ചെയ്തു. സ്കീമ പിന്നീട് ഉപകരണങ്ങൾ വിളിക്കാൻ ഉപയോഗിക്കും.

#### ജാവ

```java
// MCP ടൂളുകൾ സ്വയം കണ്ടെത്തുന്ന ഒരു ടൂൾ പ്രൊവൈഡർ സൃഷ്ടിക്കുക
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ടൂൾ പ്രൊവൈഡർ സ്വയം കൈകാര്യം ചെയ്യുന്നത്:
// - MCP സെർവറിൽ നിന്ന് ലഭ്യമായ ടൂളുകളുടെ പട്ടിക
// - MCP ടൂൾ സ്‌കീമകളെ LangChain4j ഫോർമാറ്റിലേക്ക് മാറ്റുക
// - ടൂൾ നിർവഹണവും പ്രതികരണങ്ങളും നിയന്ത്രിക്കുക
```

മുന്നിലുള്ള കോഡിൽ ഞങ്ങൾ:


- MCP സെർവറിൽ നിന്നും എല്ലാ ടൂളുകളും സ്വയമേ ഉപയോഗിച്ച് കണ്ടെത്തുകയും രജിസ്റ്റർ ചെയ്‌ത്തും ഒരു `McpToolProvider` സൃഷ്ടിച്ചു
- ടൂൾ പ്രൊവൈഡർ MCP ടൂൾ സ്കീമുകളിലെയും LangChain4jയുടെ ടൂൾ ഫോർമാറ്റിലേക്കുള്ള പരിവർത്തനം ഉൾക്കൊണ്ട് കൈകാര്യം ചെയ്യുന്നു
- ഈ സമീപനം മാനുവൽ ടൂൾ ലിസ്റ്റിംഗ്‌വും പരിവർത്തന പ്രക്രിയയും പരിഹരിക്കുന്നു

#### റസ്റ്റി

MCP സെർവറിൽ നിന്നും ടൂളുകൾ തിരികെ തരുമാൻ `list_tools` മെത്തഡിനെ ഉപയോഗിക്കുന്നു. നിങ്ങളുടെ `main` ഫംഗ്ഷനിൽ MCP ക്ലയന്റ് സെറ്റ് ചെയ്യുന്നതിന് ശേഷം താഴെ കൊടുത്ത കോഡ് ചേർക്കുക:

```rust
// MCP ഉപകരണ ലിസ്റ്റിംഗ് നേടുക
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- സെർവർ ശേഷികളെ LLM ടൂളുകളിലേക്കും മാറ്റുക

സെർവർ ശേഷികൾ ലിസ്റ്റ് ചെയ്ത ശേഷം LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് അവ മാറ്റുക അതാണ് അടുത്ത ഘട്ടം. പിന്നീട് ആ ശേഷികൾ ടൂളുകളായി ഞങ്ങളുടെ LLMനെ നൽകാം.

#### ടൈപ്പ്സ്ക്രിപ്റ്റ്

1. MCP സെർവർ നിന്നുള്ള പ്രതികരണത്തെ LLM ഉപയോഗിക്കാൻ കഴിയുന്ന ടൂൾ ഫോർമാറ്റിൽ മാറ്റാൻ താഴെ കൊടുത്ത കോഡ് ചേർക്കുക:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ഇൻപുട്ട് സ്കീമയുടെ അടിസ്ഥാനത്തിൽ സോഡ് സ്കീമ സൃഷ്ടിക്കുക
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ടൈപ്പ് "function" ആയി വ്യക്തമായി ക്രമീകരിക്കുക
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

    മുകളിൽ നൽകിയ കോഡ് MCP സെർവറിൽ നിന്നുള്ള പ്രതികരണം എടുത്ത് LLM മനസ്സിലാക്കുന്ന ടൂൾ നിർവചന ഫോർമാറ്റിലേക്ക് മാറ്റുന്നു.

2. അടുത്തതായി `run` മെത്തഡ് അപ്ഡേറ്റ് ചെയ്ത് സെർവർ ശേഷികൾ ലിസ്റ്റ് ചെയ്യുക:

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

    മുകളിലുള്ള കോഡിൽ `run` മെത്തഡ് അപ്ഡേറ്റ് ചെയ്തു ഫലം പ്ലസിലൂടെ മാപ്പ് ചെയ്ത് ഓരോ എൻട്രിക്കും `openAiToolAdapter` വിളിക്കുന്നു.

#### പൈറ്റൺ

1. ആദ്യം താഴെ കൊടുത്ത ഒരു കൺവെർട്ടർ ഫംഗ്ഷൻ സൃഷ്ടിക്കാം

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

    മുകളിൽ നൽകിയ `convert_to_llm_tools` ഫംഗ്ഷനിൽ MCP ടൂൾ പ്രതികരണം എടുത്ത് LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്ക് മാറ്റുന്നു.

2. തുടർന്ന്, ഈ ഫംഗ്ഷൻ ഉപയോഗിക്കാൻ ഞങ്ങളുടെ ക്ലയന്റ് കോഡ് അപ്ഡേറ്റ് ചെയ്യാം:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ഇവിടെ MCP ടൂൾ പ്രതികരണത്തെ LLMക്ക് നൽകാൻ കഴിയുന്ന രൂപത്തിലേക്ക് `convert_to_llm_tool` വിളിക്കുന്നു.

#### .NET

1. MCP ടൂൾ പ്രതികരണത്തെ LLM മനസ്സിലാക്കുന്ന രൂപത്തിലേക്ക് മാറ്റാൻ കോഡ് ചേർക്കാം

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

മുകളിലുള്ള കോഡിൽ:

- name, description, input schema തുടങ്ങിയവ സ്വീകരിക്കുന്ന `ConvertFrom` ഫംഗ്ഷൻ സൃഷ്ടിച്ചു
- FunctionDefinition സൃഷ്ടിക്കുന്ന പ്രവർത്തനം നിർവചിച്ചു, അത് ChatCompletionsDefinition-ന് നൽകി LLMക്ക് മനസ്സിലാക്കാവുന്നതാക്കുന്നു

2. ഇതിനുശേഷം, മുകളിൽ നൽകിയ ഫംഗ്ഷൻ ഉപയോഗിക്കാൻ നിലവിലെ കോഡ് എങ്ങനെ അപ്ഡേറ്റ് ചെയ്യാമെന്ന് നോക്കാം:

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
// സ്വാഭാവിക ഭാഷ ഇന്റർഅക്ഷനിനു വേണ്ടി ബോട്ട് ഇന്റർഫേസ് സൃഷ്ടിക്കുക
public interface Bot {
    String chat(String prompt);
}

// LLM കൂടാതെ MCP ടൂളുകളോടൊപ്പം AI സേവനം ക്രമീകരിക്കുക
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

മുകളിലുള്ള കോഡിൽ:

- സ്വാഭാവിക ഭാഷാ ഇടപെടലുകൾക്ക് ഒരു ലളിത `Bot` ഇന്റർഫേസ് നിർവചിച്ചു
- LangChain4j-യുടെ `AiServices` ഉപയോഗിച്ച് MCP ടൂൾ പ്രൊവൈഡറുമായി LLM സ്വയം ബന്ധിപ്പിക്കുന്നു
- ടൂൾ സ്കീമ പരിവർത്തനം, ഫംഗ്ഷൻ വിളിക്കല്‍ എന്നിവ പിന്‍‌ഗാമികളായി ഫ്രെയിംവർക്ക് കൈകാര്യം ചെയ്യുന്നു
- മാനുവൽ ടൂൾ പരിവർത്തനം ഒഴിവാകും - MCP ടൂളുകൾ LLM-സഹജ ഫോർമാറ്റിലേക്കു മാറ്റുന്നതിന്റെ സങ്കീർണത LangChain4j കൈകാര്യമാക്കുന്നു

#### റസ്റ്റി

MCP ടൂൾ പ്രതിരോധം LLM മനസ്സിലാക്കുന്ന ഫോർമാറ്റിലേക്കു മാറ്റാൻ സഹായകമായ ഒരു സഹായ ഫംഗ്ഷൻ ചേർക്കും, അത് ടൂൾ ലിസ്റ്റിംഗ് ഫോർമാറ്റ് ചെയ്യുന്നു. നിങ്ങളുടെ `main.rs` ഫയലിലെ `main` ഫംഗ്ഷൻ താഴെ താളിൽ താഴെ കൊടുത്ത കോഡ് ചേർക്കുക. ഇത് LLM-க்கு അഭ്യർത്ഥനകൾ ചെയ്യുമ്പോൾ വിളിക്കും:

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

നല്ലതാണ്, ഇപ്പോൾ ഉപയോക്തൃ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യാൻ തയ്യാറാകാം, അത് അടുത്തതായി കൈകാര്യം ചെയ്യുക.

### -4- ഉപയോക്തൃ പ്രോംപ്റ്റ് അഭ്യർത്ഥന കൈകാര്യം ചെയ്യുക

കോഡിന്റെ ഈ ഘട്ടത്തിൽ, ഉപയോക്തൃ അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യും.

#### ടൈപ്പ്സ്ക്രിപ്റ്റ്

1. ഞങ്ങളുടെ LLM വിളിക്ക് ഉപയോഗിക്കുന്ന ഒരു മെത്തഡ് ചേർക്കുക:

    ```typescript
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

        // 3. ഫലത്തോട് എന്തെങ്കിലുമാക്കുക
        // ചെയ്യേണ്ടത്

        }
    }
    ```

    മുകളിൽ നൽകിയ കോഡിൽ:

    - `callTools` എന്ന മെത്തഡ് ചേർത്തു.
    - ഈ മെത്തഡ് ഒരു LLM പ്രതികരണം സ്വീകരിച്ച് എന്തെല്ലാ ടൂളുകൾ വിളിക്കപ്പെട്ടോ അതു പരിശോധിക്കുന്നു:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ടൂൾ کال ചെയ്യുക
        }
        ```

    - LLM ആവശ്യപ്പെടുന്നെങ്കിൽ ടൂൾ വിളിക്കുന്നു:

        ```typescript
        // 2. സರ್ವറിന്റെ ഉപകരണം വിളിക്കുക
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ഫലത്തോടൊപ്പം എന്തോ ചെയ്യുക
        // ചെയ്യാനുള്ളതിൻ്റെ ലിസ്റ്റ് (TODO)
        ```

2. LLM-നു കോൾ നടത്തുന്നതിനും `callTools` വിളിക്കാൻ `run` മെത്തഡ് അപ്ഡേറ്റ് ചെയ്യുക:

    ```typescript

    // 1. LLM ന് ഇൻപുട്ടായി ഉപയോഗിക്കുന്ന സന്ദേശങ്ങൾ സൃഷ്ടിക്കുക
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

    // 3. ഓരോ തിരഞ്ഞെടുപ്പിനും LLM പ്രതികരണം പരിശോധിക്കുകയായി ടൂൾ കോൾ ഉണ്ട് എങ്കിൽ കണ്ടെത്തുക
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

നല്ലതാണ്, പൂർണ്ണ കോഡ് ലിസ്റ്റ് ചെയ്യാം:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // സ്കീമാ പരിശോധനയ്ക്കായി zod ഇറക്കുമതി ചെയ്യുക

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // വരാനിരിക്കുന്ന കാലത്ത് ഈ url-ൽ മാറ്റേണ്ടിവരും: https://models.github.ai/inference
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
          // input_schema-നെ അടിസ്ഥാനമാക്കി ഒരു zod സ്കീമ സൃഷ്ടിക്കുക
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
    
          // 3. ഫലത്തിനൊപ്പം എന്തെങ്കിലും ചെയ്യുക
          // ചെയ്യേണ്ടതുണ്ട്
    
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
    
        // 3. LLM പ്രതികരണത്തിലൂടെയാണ് പോകുക, ഓരോ തിരഞ്ഞെടുപ്പിനും ടൂൾ കോൾസ് ഉണ്ടോ എന്ന് പരിശോധിക്കുക
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

#### പൈറ്റൺ

1. LLM വിളിക്കാൻ ആവശ്യമായ ചില ഇമ്പോർട്ടുകൾ ചേർക്കുക

    ```python
    # എൽഎൽഎം
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. പിന്നീട്, LLM വിളിക്കുന്ന ഫംഗ്ഷൻ ചേർക്കുക:

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
            # ഐച്ഛിക പരാമര്ശങ്ങൾ
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

    മുകളിൽ നൽകിയ കോഡിൽ:

    - MCP സെർവറിൽ കണ്ടെത്തി മാറ്റിയ ഫംഗ്ഷനുകൾ LLM-യിലെക്ക് നൽകി.
    - തുടർന്ന് ആ ഫംഗ്ഷനുകളുമായി LLM വിളിച്ചു.
    - ഫലം പരിശോധിച്ച് ഏത് ഫംഗ്ഷനുകൾ വിളിക്കേണ്ടതുണ്ടെന്ന് കണ്ടെത്തുന്നു.
    - അവസാനം വിളിക്കാനുള്ള ഫംഗ്ഷനുകളുടെ പട്ടിക നൽകി.

3. അവസാന ഘട്ടം, പ്രധാന കോഡ് അപ്ഡേറ്റ് ചെയ്യുക:

    ```python
    prompt = "Add 2 to 20"

    # എല്ലാ ഉപകരണങ്ങളും എന്താണെന്ന്, ഉണ്ടെങ്കിൽ, LLM-നോട് ചോദിക്കൂ
    functions_to_call = call_llm(prompt, functions)

    # നിർദേശിച്ച ഫംഗ്ഷനുകൾ വിളിക്കുക
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    മുകളിൽ നൽകിയ കോഡിൽ അവസാനം ഘട്ടം:

    - LLM കരുതിയ ഫംഗ്ഷൻ അടിസ്ഥാനമാക്കി `call_tool` വഴി MCP ടൂൾ വിളിക്കുന്നു.
    - MCP സെർവറിലേക്ക് ടൂൾ വിളിയുടെ ഫലം പ്രിന്റ് ചെയ്യുന്നു.

#### .NET

1. LLM പ്രോംപ്റ്റ് അഭ്യർത്ഥന പ്രവർത്തനം കാണിച്ച് കൊടുക്കാം:

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

    മുകളിൽ നൽകിയ കോഡിൽ:

    - MCP സെർവറിൽ നിന്ന് ടൂളുകൾ കൊണ്ടുവന്നു, `var tools = await GetMcpTools()` എന്നതുപോലെ.
    - ഒരു ഉപയോക്തൃ പ്രോംപ്റ്റ് നിർവചിച്ചു `userMessage`.
    - മോഡൽ, ടൂളുകൾ എന്നിവ നിർദ്ദേശിച്ച് ഓപ്ഷൻസ് ബജക്ട് സൃഷ്ടിച്ചു.
    - LLM അഭ്യർത്ഥന അയച്ചു.

2. ഒരു അവസാന ഘട്ടം: LLM ഒരു ഫംഗ്ഷൻ വിളിക്കണമെന്ന് കരുതുന്നുണ്ടോയെന്ന് പരിശോധിക്കാം:

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

    മുകളിൽ നൽകിയ കോഡിൽ:

    - ഫംഗ്ഷൻ വിളികളുടെ പട്ടികയിൽ ചുറ്റി.
    - ഓരോ ടൂൾ വിളിക്കും പേരും_ARGUMENTS_ഉം വിശദീകരിക്കുകയും MCP ക്ലയന്റ് ഉപയോഗിച്ച് ടൂൾ MCP സെർവറിൽ വിളിക്കുകയും ചെയ്തു. ഏറ്റവും അവസാനം ഫലം പ്രിന്റ് ചെയ്തു.

പൂർണ്ണമായ കോഡ് ഇതാ:

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
    // MCP ടൂളുകൾ സ്വയം ഉപയോഗിക്കുന്ന സ്വാഭാവിക ഭാഷാ അഭ്യർത്ഥനകൾ നിർവ്വഹിക്കുക
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

മുകളിൽ നൽകിയ കോഡിൽ:

- MCP സെർവർ ടൂളുകളുമായുള്ള ലളിത സ്വാഭാവിക ഭാഷ പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ചു
- LangChain4j ഫ്രെയിംവർക്കിൽ സ്വയം നിയന്ത്രണം:
  - ഉപയോക്തൃ പ്രോംപ്റ്റുകൾ ടൂൾ കോൾമായി മാറ്റുന്നു ആവശ്യമായപ്പോൾ
  - LLM ന്‍റെ തീരുമാനം അനുസരിച്ച് MCP വിശദമായ ടൂളുകൾ വിളിക്കുന്നു
  - LLM-നും MCP സെർവറിന്റെ സംഭാഷണ പ്രവാഹം നിയന്ത്രിക്കുന്നു
- `bot.chat()` മെത്തഡ് MCP ടൂൾ നിർവ്വഹണ ഫലങ്ങൾ ഉൾപ്പെടുന്ന പ്രകൃതിഭാഷാ പ്രതികരണങ്ങൾ തിരികെ നൽകുന്നു
- ഈ സമീപനം ഉപയോക്താക്കളെ MCP അണ്ടർലൈയിംഗ് നടപ്പാക്കലുകൾ അറിയേണ്ടതില്ലാത്ത സുഗമ അനുഭവം നൽകുന്നു

പൂർണ കോഡ് ഉദാഹരണം:

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

#### റസ്റ്റി

ഇവിടെ കൂടുതൽ പരിചരണ പ്രവർത്തനങ്ങൾ നടക്കുന്നു. ആദ്യം ഉപയോക്തൃ പ്രോംപ്റ്റുമായി LLM നു വിളിക്കും, തുടർന്ന് പ്രതികരണം പരിശോധിച്ച് ടൂൾ വിളിക്കേണ്ടതുണ്ടോ എന്നറിയാം. ആവശ്യമെങ്കിൽ ആ ടൂളുകൾ വിളിച്ച് LLM-നു ഉപയുക്തമായ സംഭാഷണം തുടരുന്നു, കൂടാതെ കൂടുതൽ ടൂൾ കോൾ ആവശ്യമില്ലാതെ അന്തിമ പ്രതികരണം ലഭിക്കുന്നു.


നാം LLM-ലേക്ക് പലതവണ কলുകൾ നടത്താൻ പോകുന്നു, അതിനാൽ LLM കോളിനെ കൈകാര്യം ചെയ്യുന്ന ഒരു ഫംഗ്ഷൻ നിർവചിക്കാം. നിങ്ങളുടെ `main.rs` ഫയലിലേക്ക് താഴെ കൊടുത്തിരിക്കുന്ന ഫംഗ്ഷൻ ചേർക്കുക:

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

ഈ ഫംഗ്ഷൻ LLM ക്ലയന്റ്, സന്ദേശങ്ങളുടെ ഒരു പട്ടിക (ഉപയോക്തൃ പ്രോംപ്റ്റ് ഉൾപ്പെടെ), MCP സർവറിലെ ടൂൾസുകൾ സ്വീകരിച്ച് LLM-ലേക്ക് ഒരു അഭ്യർത്ഥന അയയ്ക്കുന്നു, പ്രതികരണം തിരികെ നൽകുന്നു.

LLM-ൽ നിന്നുള്ള പ്രതികരണം `choices` എന്ന ഒരു അസംഖ്യമായ ഘടകം ഉൾക്കൊള്ളും. `tool_calls` ഉള്ളതാണോ എന്ന് പരിശോധിക്കാൻ നമുക്ക് ഫലം പ്രോസസ്സ് ചെയ്യേണ്ടതുണ്ടാകും. ഇതിൽ നിന്ന് LLM ഒരു പ്രത്യേക ടൂൾ വിവരങ്ങളോടുകൂടി കേൾപിക്കണം എന്ന് നൽകുന്നു. LLM പ്രതികരണം കൈകാര്യം ചെയ്യാൻ ഒരു ഫംഗ്ഷൻ നിർവചിക്കാൻ താഴെ കുരുംബിലുള്ള കോഡ് നിങ്ങളുടെ `main.rs` ഫയലിന്റെ അവസാനം ചേർക്കുക:

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

    // ഉള്ളടക്കം ലഭ്യമായെങ്കില്‍ പ്രിന്‍റ് ചെയ്യുക
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ടൂള്‍ കോള്‍ കൈകാര്യം ചെയ്യുക
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // അസിസ്റ്റന്റ് സന്ദേശം ചേര്‍ക്കുക

        // ഓരോ ടൂള്‍ കോള്‍ നിര്‍വഹിക്കുക
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ടൂള്‍ ഫലം സന്ദേശങ്ങളില്‍ ചേര്‍ക്കുക
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ടൂള്‍ ഫലങ്ങളുമായി സംവാദം തുടര്‍ത്തുക
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

`tool_calls` ഉണ്ടെങ്കിൽ, അത് ടൂൾ വിവരങ്ങൾ കൊണ്ടുകഴിച്ച്, MCP സർവറിലേക്ക് ടൂൾ അഭ്യർത്ഥനയുമായി വിളിക്കുന്നു, ഫലങ്ങൾ സംഭാഷണ സന്ദേശങ്ങളിലേക്ക് ചേർക്കുന്നു. ശേഷം LLM-ുമായി സംഭാഷണം തുടരുന്നു, സന്ദേശങ്ങൾ അസിസ്റ്റന്റിന്റെ പ്രതികരണവും ടൂൾ കോൾ ഫലങ്ങളും ഉൾക്കൊണ്ട് അപ്ഡേറ്റ് ചെയ്യപ്പെടുന്നു.

MCP കോളുകൾക്ക് LLM മടങ്ങുന്നു ടൂൾ കോൾ വിവരങ്ങൾ എടുക്കാൻ മറ്റൊരു സഹായക ഫംഗ്ഷൻ ചേർക്കാം. താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് `main.rs` ഫയലിന്റെ അവസാനം ചേർക്കുക:

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

എല്ലാ ഘടകങ്ങളും സജ്ജമാണെന്നതിനാൽ, തുടക്ക ഉപയോക്തൃ പ്രോംപ്റ്റ് കൈകാര്യം ചെയ്ത് LLM-നെ വിളിക്കാൻ കഴിഞ്ഞു. നിങ്ങളുടെ `main` ഫംഗ്ഷൻ താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ഉൾപ്പെടുത്തുക:

```rust
// ടൂൾ കോളുകളുള്ള LLM ചാറ്റ്
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

ഇത് തുടക്ക ഉപയോക്തൃ പ്രോംപ്റ്റായി രണ്ട് സംഖ്യകളുടെ കൂട്ടം ചോദിച്ച് LLM-നെ ചോദിക്കും, അതിന്റെ പ്രതികരണം പ്രോസസ്സ് ചെയ്ത് ടൂൾ കോൾസ് ഡൈനാമിക് ആയി കൈകാര്യം ചെയ്യും.

മികച്ചതാണ്, നിങ്ങൾ അത് ചെയ്തു!

## അസൈൻമെന്റ്

വ്യായാമത്തിൽ നിന്നുള്ള കോഡ് എടുത്ത് MCP സര്‍വറുമായി കൂടുതൽ ടൂൾസുകൾ ചേർത്തെടുത്തു. പിന്നീട് LLM ഉള്ള ക്ലയന്റിനെ നിർമ്മിച്ച് വ്യത്യസ്ത പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് പരീക്ഷിച്ച് സെർവർ ടൂളുകൾ ഡൈനാമിക് ആയി വിളിക്കപ്പെടുന്നുണ്ടോ എന്ന് ഉറപ്പാക്കുക. ഈ രീതിയിൽ ക്ലയന്റ് നിർമ്മിക്കുന്നത് എത്രയും സൗകര്യപ്രദമായ ഉപയോക്തൃ പരിചയമാണ് നൽകുന്നത്, കാരണം അവർ കൃത്യ ക്ലയന്റ് കമാൻഡുകൾക്കുപകരം പ്രോംപ്റ്റുകൾ ഉപയോഗിച്ച് അത് ചെയ്യാനാകും, MCP സര്‍വർക്ക് വിളിച്ചുപോകുന്നതെന്നത് അവർക്കറിയാതെ.

## പരിഹാരം

[Solution](./solution/README.md)

## പ്രധാന കാര്യങ്ങൾ

- നിങ്ങൾക്കുള്ള MCP സർവറുമായി ഉപയോക്താക്കൾ സംവദിക്കാൻ LLM ചേർക്കുന്നത് ഒരു നല്ല മാർഗം ആണ്.
- MCP സർവർ പ്രതികരണം LLMക്ക് മനസ്സിലാകുന്ന തരത്തിലേക്ക് മാറ്റണം.

## സാമ്പിളുകൾ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## അധികം സഹകരണ സ്രോതസ്സുകൾ

## അടുത്തത് എന്ത്

- അടുത്തത്: [Visual Studio Code ഉപയോഗിച്ച് ഒരു സർവർ ഉപഭോക്തൃമാക്കൽ](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->