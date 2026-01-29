# LLM으로 클라이언트 만들기

지금까지 서버와 클라이언트를 만드는 방법을 보았습니다. 클라이언트는 서버에 명시적으로 호출하여 도구, 리소스 및 프롬프트를 나열할 수 있었습니다. 하지만 이것은 그리 실용적인 접근법이 아닙니다. 사용자는 에이전트 시대에 살고 있으며, 프롬프트를 사용하고 LLM과 소통하기를 기대합니다. 사용자는 MCP를 사용하여 기능을 저장하는지 여부에는 신경 쓰지 않지만, 자연어를 사용하여 상호작용하기를 기대합니다. 그렇다면 어떻게 해결할까요? 해결책은 클라이언트에 LLM을 추가하는 것입니다.

## 개요

이번 수업에서는 클라이언트에 LLM을 추가하는 방법에 집중하고, 이것이 사용자에게 훨씬 더 나은 경험을 제공하는 방법을 보여줍니다.

## 학습 목표

이 수업이 끝나면 다음을 할 수 있습니다:

- LLM이 포함된 클라이언트를 생성합니다.
- LLM을 사용하여 MCP 서버와 원활하게 상호작용합니다.
- 클라이언트 측에서 더 나은 최종 사용자 경험을 제공합니다.

## 접근법

우리가 취해야 할 접근법을 이해해 봅시다. LLM을 추가하는 것은 간단해 보이지만 실제로 어떻게 할까요?

클라이언트가 서버와 상호작용하는 방법은 다음과 같습니다:

1. 서버와 연결을 설정합니다.

1. 기능, 프롬프트, 리소스 및 도구를 나열하고 해당 스키마를 저장합니다.

1. LLM을 추가하고 저장된 기능과 스키마를 LLM이 이해하는 형식으로 전달합니다.

1. 사용자 프롬프트를 LLM에 전달하고 클라이언트가 나열한 도구와 함께 처리합니다.

좋습니다, 이제 높은 수준에서 어떻게 할 수 있는지 이해했으니 아래 연습 문제에서 시도해 봅시다.

## 연습: LLM이 포함된 클라이언트 만들기

이번 연습에서는 클라이언트에 LLM을 추가하는 방법을 배웁니다.

### GitHub 개인 액세스 토큰을 사용한 인증

GitHub 토큰 생성은 간단한 과정입니다. 방법은 다음과 같습니다:

- GitHub 설정으로 이동 – 오른쪽 상단 프로필 사진을 클릭하고 설정을 선택합니다.
- 개발자 설정으로 이동 – 아래로 스크롤하여 개발자 설정을 클릭합니다.
- 개인 액세스 토큰 선택 – 세분화된 토큰을 클릭한 후 새 토큰 생성을 클릭합니다.
- 토큰 구성 – 참조용 메모를 추가하고 만료 날짜를 설정하며 필요한 범위(권한)를 선택합니다. 이 경우 Models 권한을 반드시 추가하세요.
- 토큰 생성 및 복사 – 토큰 생성을 클릭하고 즉시 복사하세요. 다시 볼 수 없습니다.

### -1- 서버에 연결

먼저 클라이언트를 만들어 봅시다:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 스키마 유효성 검사를 위해 zod를 가져옵니다

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

위 코드에서 우리는:

- 필요한 라이브러리를 가져왔습니다.
- `client`와 `openai`라는 두 멤버를 가진 클래스를 생성하여 각각 클라이언트를 관리하고 LLM과 상호작용하도록 했습니다.
- `baseUrl`을 추론 API를 가리키도록 설정하여 GitHub Models를 사용하도록 LLM 인스턴스를 구성했습니다.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio 연결을 위한 서버 매개변수 생성
server_params = StdioServerParameters(
    command="mcp",  # 실행 파일
    args=["run", "server.py"],  # 선택적 명령줄 인수
    env=None,  # 선택적 환경 변수
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # 연결 초기화
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

위 코드에서 우리는:

- MCP에 필요한 라이브러리를 가져왔습니다.
- 클라이언트를 생성했습니다.

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

먼저, `pom.xml` 파일에 LangChain4j 의존성을 추가해야 합니다. MCP 통합과 GitHub Models 지원을 활성화하려면 다음 의존성을 추가하세요:

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

그런 다음 Java 클라이언트 클래스를 만듭니다:

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
    
    public static void main(String[] args) throws Exception {        // LLM을 GitHub 모델을 사용하도록 구성
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // 서버에 연결하기 위한 MCP 전송 생성
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP 클라이언트 생성
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

위 코드에서 우리는:

- **LangChain4j 의존성 추가**: MCP 통합, OpenAI 공식 클라이언트, GitHub Models 지원에 필요합니다.
- **LangChain4j 라이브러리 가져오기**: MCP 통합과 OpenAI 채팅 모델 기능을 위해.
- **`ChatLanguageModel` 생성**: GitHub 토큰으로 GitHub Models를 사용하도록 구성했습니다.
- **HTTP 전송 설정**: Server-Sent Events(SSE)를 사용하여 MCP 서버에 연결합니다.
- **MCP 클라이언트 생성**: 서버와의 통신을 처리합니다.
- **LangChain4j 내장 MCP 지원 사용**: LLM과 MCP 서버 간 통합을 간소화합니다.

#### Rust

이 예제는 Rust 기반 MCP 서버가 실행 중이라고 가정합니다. 서버가 없다면 [01-first-server](../01-first-server/README.md) 수업을 참고하여 서버를 만드세요.

Rust MCP 서버가 준비되면 터미널을 열고 서버와 동일한 디렉터리로 이동한 후 다음 명령어로 새 LLM 클라이언트 프로젝트를 만듭니다:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` 파일에 다음 의존성을 추가하세요:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> 공식 Rust용 OpenAI 라이브러리는 없지만, `async-openai` 크레이트는 [커뮤니티에서 유지하는 라이브러리](https://platform.openai.com/docs/libraries/rust#rust)로 널리 사용됩니다.

`src/main.rs` 파일을 열고 내용을 다음 코드로 교체하세요:

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
    // 초기 메시지
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI 클라이언트 설정
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP 클라이언트 설정
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

    // TODO: MCP 도구 목록 가져오기

    // TODO: 도구 호출과 함께 LLM 대화

    Ok(())
}
```

이 코드는 MCP 서버와 GitHub Models에 연결하여 LLM 상호작용을 설정하는 기본 Rust 애플리케이션을 만듭니다.

> [!IMPORTANT]
> 애플리케이션 실행 전에 `OPENAI_API_KEY` 환경 변수에 GitHub 토큰을 설정해야 합니다.

좋습니다, 다음 단계로 서버의 기능을 나열해 봅시다.

### -2- 서버 기능 나열

이제 서버에 연결하여 기능을 요청합니다:

#### Typescript

같은 클래스에 다음 메서드를 추가하세요:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // 도구 나열
    const toolsResult = await this.client.listTools();
}
```

위 코드에서 우리는:

- 서버에 연결하는 코드 `connectToServer`를 추가했습니다.
- 앱 흐름을 처리하는 `run` 메서드를 만들었습니다. 현재는 도구만 나열하지만 곧 더 추가할 예정입니다.

#### Python

```python
# 사용 가능한 리소스 목록
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# 사용 가능한 도구 목록
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

추가한 내용은:

- 리소스와 도구를 나열하고 출력했습니다. 도구의 경우 나중에 사용할 `inputSchema`도 나열했습니다.

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

위 코드에서 우리는:

- MCP 서버에서 사용 가능한 도구를 나열했습니다.
- 각 도구에 대해 이름, 설명 및 스키마를 나열했습니다. 후자는 곧 도구 호출에 사용할 것입니다.

#### Java

```java
// MCP 도구를 자동으로 검색하는 도구 공급자를 만듭니다
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP 도구 공급자는 다음을 자동으로 처리합니다:
// - MCP 서버에서 사용 가능한 도구 목록 가져오기
// - MCP 도구 스키마를 LangChain4j 형식으로 변환
// - 도구 실행 및 응답 관리
```

위 코드에서 우리는:

- MCP 서버에서 모든 도구를 자동으로 검색하고 등록하는 `McpToolProvider`를 만들었습니다.
- 도구 공급자는 MCP 도구 스키마와 LangChain4j 도구 형식 간 변환을 내부적으로 처리합니다.
- 이 접근법은 수동 도구 나열 및 변환 과정을 추상화합니다.

#### Rust

MCP 서버에서 도구를 가져오는 것은 `list_tools` 메서드를 사용합니다. `main` 함수에서 MCP 클라이언트를 설정한 후 다음 코드를 추가하세요:

```rust
// MCP 도구 목록 가져오기
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- 서버 기능을 LLM 도구로 변환

서버 기능을 나열한 다음 단계는 이를 LLM이 이해하는 형식으로 변환하는 것입니다. 이렇게 하면 LLM에 도구로 제공할 수 있습니다.

#### TypeScript

1. MCP 서버 응답을 LLM이 사용할 수 있는 도구 형식으로 변환하는 다음 코드를 추가하세요:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema를 기반으로 zod 스키마를 생성합니다
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // 타입을 명시적으로 "function"으로 설정합니다
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

    위 코드는 MCP 서버 응답을 받아 LLM이 이해할 수 있는 도구 정의 형식으로 변환합니다.

1. 다음으로 `run` 메서드를 업데이트하여 서버 기능을 나열해 봅시다:

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

    위 코드에서 `run` 메서드를 업데이트하여 결과를 매핑하고 각 항목에 대해 `openAiToolAdapter`를 호출합니다.

#### Python

1. 먼저 다음 변환 함수부터 만듭니다:

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

    위 함수 `convert_to_llm_tools`는 MCP 도구 응답을 받아 LLM이 이해할 수 있는 형식으로 변환합니다.

1. 다음으로 클라이언트 코드를 업데이트하여 이 함수를 활용합니다:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    여기서는 MCP 도구 응답을 LLM에 전달할 수 있는 형식으로 변환하기 위해 `convert_to_llm_tool` 호출을 추가했습니다.

#### .NET

1. MCP 도구 응답을 LLM이 이해할 수 있는 형식으로 변환하는 코드를 추가합니다:

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

위 코드에서 우리는:

- 이름, 설명, 입력 스키마를 받아 `ConvertFrom` 함수를 만들었습니다.
- 이 함수는 `FunctionDefinition`을 생성하며, 이는 `ChatCompletionsDefinition`에 전달됩니다. 후자는 LLM이 이해할 수 있는 형식입니다.

1. 기존 코드를 업데이트하여 이 함수를 활용하는 방법을 봅시다:

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
// 자연어 상호작용을 위한 봇 인터페이스 생성
public interface Bot {
    String chat(String prompt);
}

// LLM 및 MCP 도구로 AI 서비스 구성
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

위 코드에서 우리는:

- 자연어 상호작용을 위한 간단한 `Bot` 인터페이스를 정의했습니다.
- LangChain4j의 `AiServices`를 사용하여 LLM과 MCP 도구 공급자를 자동으로 바인딩했습니다.
- 프레임워크가 도구 스키마 변환과 함수 호출을 자동으로 처리합니다.
- 이 접근법은 수동 도구 변환을 없애고, LangChain4j가 MCP 도구를 LLM 호환 형식으로 변환하는 복잡성을 모두 처리합니다.

#### Rust

MCP 도구 응답을 LLM이 이해할 수 있는 형식으로 변환하기 위해 도구 목록을 포맷하는 헬퍼 함수를 추가합니다. `main` 함수 아래에 다음 코드를 `main.rs` 파일에 추가하세요. 이 함수는 LLM에 요청할 때 호출됩니다:

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

좋습니다, 이제 사용자 요청을 처리할 준비가 되었으니 다음으로 넘어갑시다.

### -4- 사용자 프롬프트 요청 처리

이 부분에서는 사용자 요청을 처리합니다.

#### TypeScript

1. LLM을 호출하는 데 사용할 메서드를 추가하세요:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. 서버의 도구를 호출합니다
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 결과로 무언가를 합니다
        // 해야 할 일

        }
    }
    ```

    위 코드에서 우리는:

    - `callTools` 메서드를 추가했습니다.
    - 이 메서드는 LLM 응답을 받아 호출된 도구가 있는지 확인합니다:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // 도구 호출
        }
        ```

    - LLM이 호출해야 한다고 표시한 경우 도구를 호출합니다:

        ```typescript
        // 2. 서버의 도구를 호출합니다
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. 결과로 무언가를 수행합니다
        // 해야 할 일
        ```

1. `run` 메서드를 업데이트하여 LLM 호출과 `callTools` 호출을 포함시킵니다:

    ```typescript

    // 1. LLM에 입력할 메시지를 생성합니다
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM 호출하기
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM 응답을 확인하고, 각 선택지에 도구 호출이 있는지 검사합니다
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

좋습니다, 전체 코드를 나열해 봅시다:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // 스키마 검증을 위해 zod를 가져옵니다

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // 나중에 이 URL로 변경해야 할 수도 있습니다: https://models.github.ai/inference
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
          // input_schema를 기반으로 zod 스키마를 생성합니다
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // 타입을 명시적으로 "function"으로 설정합니다
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
    
    
          // 2. 서버의 도구를 호출합니다
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. 결과로 무언가를 수행합니다
          // 할 일
    
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
    
        // 1. LLM 응답을 검토하고, 각 선택지에 도구 호출이 있는지 확인합니다
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

1. LLM 호출에 필요한 일부 임포트를 추가합니다:

    ```python
    # 대형 언어 모델
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. 다음으로 LLM을 호출하는 함수를 추가합니다:

    ```python
    # llm

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
            # 선택적 매개변수
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

    위 코드에서 우리는:

    - MCP 서버에서 찾고 변환한 함수를 LLM에 전달했습니다.
    - 해당 함수를 사용해 LLM을 호출했습니다.
    - 결과를 검사하여 호출해야 할 함수가 있는지 확인했습니다.
    - 호출할 함수 배열을 전달했습니다.

1. 마지막 단계로 메인 코드를 업데이트합니다:

    ```python
    prompt = "Add 2 to 20"

    # 모든 도구가 있다면 LLM에 어떤 도구인지 물어보세요
    functions_to_call = call_llm(prompt, functions)

    # 제안된 함수를 호출하세요
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    위 코드가 마지막 단계입니다. 여기서는:

    - LLM이 호출해야 한다고 판단한 함수를 사용해 `call_tool`로 MCP 도구를 호출합니다.
    - 도구 호출 결과를 MCP 서버에 출력합니다.

#### .NET

1. LLM 프롬프트 요청을 처리하는 코드를 봅시다:

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

    위 코드에서 우리는:

    - MCP 서버에서 도구를 가져왔습니다, `var tools = await GetMcpTools()`.
    - 사용자 프롬프트 `userMessage`를 정의했습니다.
    - 모델과 도구를 지정하는 옵션 객체를 생성했습니다.
    - LLM에 요청을 보냈습니다.

1. 마지막으로 LLM이 함수 호출을 해야 하는지 확인하는 코드를 봅시다:

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

    위 코드에서 우리는:

    - 함수 호출 목록을 반복했습니다.
    - 각 도구 호출에 대해 이름과 인수를 파싱하고 MCP 클라이언트를 사용해 MCP 서버에서 도구를 호출했습니다. 결과를 출력합니다.

전체 코드는 다음과 같습니다:

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
    // MCP 도구를 자동으로 사용하는 자연어 요청을 실행합니다
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

위 코드에서 우리는:

- 간단한 자연어 프롬프트를 사용해 MCP 서버 도구와 상호작용했습니다.
- LangChain4j 프레임워크가 자동으로 다음을 처리합니다:
  - 필요 시 사용자 프롬프트를 도구 호출로 변환
  - LLM 결정에 따라 적절한 MCP 도구 호출
  - LLM과 MCP 서버 간 대화 흐름 관리
- `bot.chat()` 메서드는 MCP 도구 실행 결과를 포함할 수 있는 자연어 응답을 반환합니다.
- 이 접근법은 사용자가 MCP 구현을 알 필요 없이 원활한 사용자 경험을 제공합니다.

전체 코드 예제:

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

여기서 대부분의 작업이 이루어집니다. 초기 사용자 프롬프트로 LLM을 호출한 후, 응답을 처리하여 호출해야 할 도구가 있는지 확인합니다. 있다면 도구를 호출하고, 더 이상 도구 호출이 필요 없고 최종 응답이 나올 때까지 LLM과 대화를 계속합니다.

LLM을 여러 번 호출할 것이므로, LLM 호출을 처리하는 함수를 정의합시다. `main.rs` 파일에 다음 함수를 추가하세요:

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

이 함수는 LLM 클라이언트, 메시지 목록(사용자 프롬프트 포함), MCP 서버의 도구를 받아 LLM에 요청을 보내고 응답을 반환합니다.
LLM의 응답에는 `choices` 배열이 포함됩니다. 결과를 처리하여 `tool_calls`가 있는지 확인해야 합니다. 이를 통해 LLM이 특정 도구를 인수와 함께 호출하도록 요청하고 있음을 알 수 있습니다. LLM 응답을 처리하는 함수를 정의하기 위해 `main.rs` 파일 하단에 다음 코드를 추가하세요:

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

    // 내용이 있으면 출력
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // 도구 호출 처리
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // 어시스턴트 메시지 추가

        // 각 도구 호출 실행
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // 도구 결과를 메시지에 추가
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // 도구 결과로 대화 계속 진행
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

`tool_calls`가 있으면 도구 정보를 추출하고, 도구 요청과 함께 MCP 서버를 호출하며, 결과를 대화 메시지에 추가합니다. 그런 다음 LLM과 대화를 계속하며 메시지는 어시스턴트의 응답과 도구 호출 결과로 업데이트됩니다.

LLM이 MCP 호출을 위해 반환하는 도구 호출 정보를 추출하기 위해 호출에 필요한 모든 것을 추출하는 또 다른 헬퍼 함수를 추가하겠습니다. `main.rs` 파일 하단에 다음 코드를 추가하세요:

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

모든 부분이 준비되었으니, 초기 사용자 프롬프트를 처리하고 LLM을 호출할 수 있습니다. `main` 함수를 다음 코드로 업데이트하세요:

```rust
// 도구 호출이 포함된 LLM 대화
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

이 코드는 두 숫자의 합을 묻는 초기 사용자 프롬프트로 LLM에 쿼리하고, 응답을 처리하여 도구 호출을 동적으로 처리합니다.

잘 하셨습니다!

## 과제

연습에서 작성한 코드를 가져와 서버에 더 많은 도구를 추가하여 확장하세요. 그런 다음 연습과 같이 LLM을 사용하는 클라이언트를 만들고 다양한 프롬프트로 테스트하여 모든 서버 도구가 동적으로 호출되는지 확인하세요. 이렇게 클라이언트를 구축하면 최종 사용자가 정확한 클라이언트 명령 대신 프롬프트를 사용하여 MCP 서버 호출을 인지하지 못한 채 훌륭한 사용자 경험을 누릴 수 있습니다.

## 솔루션

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## 주요 내용

- 클라이언트에 LLM을 추가하면 사용자가 MCP 서버와 상호작용하는 더 나은 방법을 제공합니다.
- MCP 서버 응답을 LLM이 이해할 수 있는 형태로 변환해야 합니다.

## 샘플

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## 추가 자료

## 다음 단계

- 다음: [Visual Studio Code를 사용하여 서버 소비하기](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->