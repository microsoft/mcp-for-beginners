# 클라이언트 생성하기

클라이언트는 MCP 서버와 직접 통신하여 리소스, 도구 및 프롬프트를 요청하는 사용자 정의 애플리케이션 또는 스크립트입니다. 서버와 상호작용하는 그래픽 인터페이스를 제공하는 인스펙터 도구를 사용하는 것과 달리, 자체 클라이언트를 작성하면 프로그래밍 방식 및 자동화된 상호작용이 가능합니다. 이를 통해 개발자는 MCP 기능을 자신의 워크플로에 통합하고 작업을 자동화하며 특정 요구에 맞춘 맞춤형 솔루션을 구축할 수 있습니다.

## 개요

이 강의에서는 Model Context Protocol(MCP) 생태계 내 클라이언트 개념을 소개합니다. 직접 클라이언트를 작성하고 MCP 서버에 연결하는 방법을 배우게 됩니다.

## 학습 목표

이 강의가 끝나면 다음을 수행할 수 있습니다:

- 클라이언트가 할 수 있는 일을 이해합니다.
- 직접 클라이언트를 작성합니다.
- MCP 서버에 클라이언트를 연결하고 테스트하여 정상 작동하는지 확인합니다.

## 클라이언트 작성에 필요한 것들

클라이언트를 작성하려면 다음 작업이 필요합니다:

- **올바른 라이브러리 가져오기**. 이전과 동일한 라이브러리를 사용하지만 구조체는 다릅니다.
- **클라이언트 인스턴스 생성하기**. 클라이언트 인스턴스를 만들고 선택한 전송 방식에 연결합니다.
- **나열할 리소스 결정하기**. MCP 서버에는 리소스, 도구, 프롬프트가 제공되며, 무엇을 나열할지 결정해야 합니다.
- **클라이언트를 호스트 애플리케이션에 통합하기**. 서버 기능을 파악한 후 사용자가 프롬프트나 명령을 입력하면 해당 서버 기능이 실행되도록 호스트 애플리케이션에 통합합니다.

이제 큰 그림에서 우리가 무엇을 할지 알았으니, 다음으로 예제를 살펴보겠습니다.

### 예제 클라이언트

다음 예제 클라이언트를 살펴봅시다:

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

// 프롬프트 목록
const prompts = await client.listPrompts();

// 프롬프트 가져오기
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// 리소스 목록
const resources = await client.listResources();

// 리소스 읽기
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// 도구 호출
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

위 코드에서 우리는 다음을 수행했습니다:

- 라이브러리 가져오기
- 클라이언트 인스턴스 생성 후 stdio 전송을 사용하여 연결하기
- 프롬프트, 리소스, 도구를 나열하고 모두 호출하기

자, 이제 MCP 서버와 통신 가능한 클라이언트를 만들었습니다.

다음 연습 섹션에서 각 코드 조각을 자세히 살펴보고 동작 방식을 설명해 보겠습니다.

## 연습: 클라이언트 작성하기

위에서 말했듯이, 코드를 자세히 설명하며 진행하고 원한다면 함께 코딩해보세요.

### -1- 라이브러리 가져오기

필요한 라이브러리를 가져옵니다. 클라이언트와 선택한 전송 프로토콜인 stdio 참조가 필요합니다. stdio는 로컬 머신에서 실행되는 용도의 프로토콜입니다. SSE는 앞으로 보여줄 다른 전송 프로토콜이지만, 우선은 stdio로 계속 진행합니다.

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

Java의 경우, 이전 연습에서 만든 MCP 서버에 연결되는 클라이언트를 생성합니다. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java)에서 사용한 동일한 Java Spring Boot 프로젝트 구조를 사용하여 `src/main/java/com/microsoft/mcp/sample/client/` 폴더에 `SDKClient`라는 새 Java 클래스를 만들고 다음과 같은 import를 추가하세요:

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

`Cargo.toml` 파일에 다음 의존성을 추가해야 합니다.

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

그런 다음 클라이언트 코드에서 필요한 라이브러리를 가져올 수 있습니다.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

인스턴스 생성을 진행해 봅시다.

### -2- 클라이언트 및 전송 인스턴스 생성

전송 인스턴스와 클라이언트 인스턴스를 생성해야 합니다:

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

위 코드에서 우리는:

- stdio 전송 인스턴스를 생성했습니다. 명령과 인수를 지정하여 서버를 찾아 시작하는 방법을 정의했는데, 이는 클라이언트를 만들 때 필요한 부분입니다.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 이름과 버전을 주어 클라이언트를 인스턴스화했습니다.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 클라이언트를 선택한 전송에 연결했습니다.

    ```typescript
    await client.connect(transport);
    ```

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

- 필요한 라이브러리를 가져왔습니다.
- 서버를 실행하기 위한 매개변수 객체를 생성했으며, 이를 이용해 클라이언트가 연결할 서버를 실행합니다.
- `stdio_client`를 호출하는 `run` 메서드를 정의했습니다. 이 함수가 클라이언트 세션을 시작합니다.
- `asyncio.run`에 `run` 메서드를 제공하는 진입점을 만들었습니다.

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

위 코드에서 우리는:

- 필요한 라이브러리를 가져왔습니다.
- stdio 전송을 만들고 `mcpClient` 클라이언트를 생성했습니다. 이는 MCP 서버의 기능을 나열하고 호출하는 데 사용됩니다.

"Arguments"에는 *.csproj* 파일이나 실행 파일을 지정할 수 있습니다.

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
        
        // 여기에 클라이언트 로직이 들어갑니다
    }
}
```

위 코드에서 우리는:

- `http://localhost:8080`을 가리키는 SSE 전송을 설정하는 메인 메서드를 만들었습니다. 여기에 MCP 서버가 실행 중입니다.
- 전송을 생성자 매개변수로 받는 클라이언트 클래스를 만들었습니다.
- `run` 메서드에서는 전송을 사용해 동기 MCP 클라이언트를 생성하고 연결을 초기화합니다.
- SSE(Server-Sent Events) 전송을 사용했고, 이는 Java Spring Boot MCP 서버와의 HTTP 기반 통신에 적합합니다.

#### Rust

이 Rust 클라이언트는 서버가 같은 디렉터리 내에 "calculator-server"라는 이름의 형제 프로젝트라고 가정합니다. 아래 코드는 서버를 시작하고 연결합니다.

```rust
async fn main() -> Result<(), RmcpError> {
    // 서버가 같은 디렉토리 내의 "calculator-server"라는 형제 프로젝트라고 가정합니다
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

    // TODO: 초기화

    // TODO: 도구 목록 작성

    // TODO: 인수={"a": 3, "b": 2}로 추가 도구 호출

    client.cancel().await?;
    Ok(())
}
```

### -3- 서버 기능 나열하기

이제 프로그램이 실행될 때 연결할 클라이언트가 생겼습니다. 하지만 기능을 실제로 나열하진 않으므로, 나열해 봅시다:

#### TypeScript

```typescript
// 프롬프트 목록
const prompts = await client.listPrompts();

// 리소스 목록
const resources = await client.listResources();

// 도구 목록
const tools = await client.listTools();
```

#### Python

```python
# 사용 가능한 리소스 나열
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# 사용 가능한 도구 나열
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

여기서는 사용 가능한 리소스(`list_resources()`)와 도구(`list_tools`)를 나열하고 출력합니다.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

위 예시는 서버의 도구를 나열하는 방법입니다. 각 도구 이름을 출력합니다.

#### Java

```java
// 도구를 나열하고 시연합니다
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// 연결을 확인하려면 서버에 핑을 보낼 수도 있습니다
client.ping();
```

위 코드에서 우리는:

- MCP 서버에서 제공하는 모든 도구를 가져오기 위해 `listTools()`를 호출했습니다.
- 서버와 연결이 정상인지 확인하기 위해 `ping()`을 사용했습니다.
- `ListToolsResult`는 도구들의 이름, 설명, 입력 스키마 정보를 포함합니다.

좋습니다, 이제 모든 기능을 캡처했습니다. 그렇다면 언제 사용합니까? 이 클라이언트는 매우 단순해서 기능을 원할 때 명시적으로 호출해야 합니다. 다음 장에서는 자체 대형 언어 모델(LLM)을 가진 더 고급 클라이언트를 만들 예정입니다. 우선 서버 기능을 호출하는 방법을 살펴봅시다:

#### Rust

main 함수 내에서 클라이언트를 초기화한 후 서버를 초기화하고 일부 기능을 나열할 수 있습니다.

```rust
// 초기화
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// 도구 목록
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 기능 호출하기

기능을 호출하려면 정확한 인수와 경우에 따라 호출하려는 이름을 지정해야 합니다.

#### TypeScript

```typescript

// 리소스를 읽습니다
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// 도구를 호출합니다
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// 프롬프트를 호출합니다
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

위 코드에서 우리는:

- 리소스를 읽었습니다. `readResource()`를 호출해 `uri`를 지정했습니다. 서버 측 상태는 다음과 비슷할 것입니다:

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

    우리의 `uri` 값인 `file://example.txt`는 서버의 `file://{name}`과 일치합니다. `example.txt`가 `name`에 매핑됩니다.

- 도구를 호출했습니다. 도구 이름과 인수(`name`, `arguments`)를 지정하여 호출합니다:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 프롬프트를 얻기 위해 `getPrompt()`를 `name`과 `arguments`와 함께 호출했습니다. 서버 코드는 다음과 같습니다:

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

    따라서 클라이언트 코드는 서버에서 선언한 대로 다음과 같이 됩니다:

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
# 리소스를 읽습니다
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# 도구를 호출합니다
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

위 코드에서 우리는:

- `read_resource`를 사용해 `greeting`이라는 리소스를 호출했습니다.
- `call_tool`을 사용해 `add`라는 도구를 호출했습니다.

#### .NET

1. 도구를 호출하는 코드를 추가합니다:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. 결과를 출력하는 코드입니다:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// 다양한 계산기 도구 호출
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

위 코드에서 우리는:

- `callTool()` 메서드와 `CallToolRequest` 객체를 사용해 여러 계산기 도구를 호출했습니다.
- 각 도구 호출은 도구 이름과 그 도구가 필요로 하는 인수 맵(`Map`)을 명시합니다.
- 서버 도구는 수학 연산을 위해 "a", "b" 같은 특정 매개변수 이름을 기대합니다.
- 결과는 서버의 응답을 포함하는 `CallToolResult` 객체로 반환됩니다.

#### Rust

```rust
// 인수 = {"a": 3, "b": 2}로 추가 도구를 호출합니다
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

### -5- 클라이언트 실행하기

클라이언트를 실행하려면 터미널에서 다음 명령을 입력하세요:

#### TypeScript

<em>package.json</em>의 "scripts" 섹션에 다음 항목을 추가합니다:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

다음 명령어로 클라이언트를 호출합니다:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

우선 MCP 서버가 `http://localhost:8080`에서 실행 중인지 확인하세요. 그런 다음 클라이언트를 실행합니다:

```bash
# 프로젝트를 빌드하세요
./mvnw clean compile

# 클라이언트를 실행하세요
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

또는 솔루션 폴더 `03-GettingStarted\02-client\solution\java`에 제공된 전체 클라이언트 프로젝트를 실행할 수 있습니다:

```bash
# 솔루션 디렉토리로 이동
cd 03-GettingStarted/02-client/solution/java

# JAR 파일을 빌드하고 실행
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 과제

이번 과제에서는 클라이언트 작성에서 배운 내용을 활용하여 직접 클라이언트를 만들어 보세요.

다음 서버를 사용할 수 있습니다. 클라이언트 코드를 통해 호출해야 하며, 서버에 더 흥미로운 기능을 추가할 수 있는지 확인해 보세요.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP 서버 생성
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// 덧셈 도구 추가
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// 동적 인사말 리소스 추가
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

// stdin에서 메시지 수신 시작 및 stdout에서 메시지 전송 시작

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

# MCP 서버 생성
mcp = FastMCP("Demo")


# 추가 도구 추가
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 동적 인사말 리소스 추가
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

이 프로젝트를 참고하여 [프롬프트 및 리소스 추가 방법](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)을 확인하세요.

또한, [프롬프트 및 리소스 호출 방법](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)도 참고하세요.

### Rust

이전 섹션([../01-first-server](../../../../03-GettingStarted/01-first-server))에서 Rust로 간단한 MCP 서버를 만드는 방법을 배웠습니다. 이 기반 위에 계속 구축하거나 다음 링크에서 Rust 기반 MCP 서버 예제를 확인할 수 있습니다: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 솔루션

<strong>솔루션 폴더</strong>에는 이 튜토리얼에서 다룬 모든 개념을 시연하는 완성된 클라이언트 구현이 포함되어 있습니다. 각 솔루션은 클라이언트와 서버 코드를 별도의 독립 프로젝트로 구성합니다.

### 📁 솔루션 구조

솔루션 디렉터리는 프로그래밍 언어별로 구성되어 있습니다:

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

### 🚀 각 솔루션에 포함된 내용

각 언어별 솔루션은 다음을 제공합니다:

- 튜토리얼의 모든 기능을 갖춘 **완전한 클라이언트 구현**
- 적절한 의존성 및 설정을 포함한 **작동 프로젝트 구조**
- 간편한 설정과 실행을 위한 **빌드 및 실행 스크립트**
- 언어별 상세 설명이 담긴 **상세 README**
- **에러 처리 및 결과 처리 예제**

### 📖 솔루션 사용법

1. **선호하는 언어 폴더로 이동하세요**:

   ```bash
   cd solution/typescript/    # TypeScript용
   cd solution/java/          # Java용
   cd solution/python/        # Python용
   cd solution/dotnet/        # .NET용
   ```

2. **각 폴더의 README 지침을 따르세요**:
   - 의존성 설치
   - 프로젝트 빌드
   - 클라이언트 실행

3. **다음과 같은 실행 결과를 확인할 수 있습니다**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

전체 문서와 단계별 지침은 다음을 참고하세요: **[📖 솔루션 문서](./solution/README.md)**

## 🎯 완성 예제

이 튜토리얼에서 다룬 모든 프로그래밍 언어에 대해 완전하고 작동하는 클라이언트 구현을 제공했습니다. 이 예제들은 앞서 설명한 전체 기능을 시연하며, 참고 구현이나 자신의 프로젝트 시작점으로 사용할 수 있습니다.

### 제공되는 완성 예제

| 언어 | 파일 | 설명 |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE 전송을 사용한 완전한 Java 클라이언트, 포괄적 에러 처리 포함 |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio 전송을 사용한 완전한 C# 클라이언트, 자동 서버 시작 포함 |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP 프로토콜을 완벽히 지원하는 완전한 TypeScript 클라이언트 |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await 패턴을 활용한 완전한 Python 클라이언트 |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio를 이용한 비동기 작업 지원 완전한 Rust 클라이언트 |

각 완성 예제에는 다음이 포함됩니다:

- ✅ **연결 설정 및 에러 처리**
- ✅ **서버 탐색** (도구, 리소스, 프롬프트 등 해당 시)
- ✅ **계산기 연산** (더하기, 빼기, 곱하기, 나누기, 도움말)
- ✅ **결과 처리 및 서식 출력**
- ✅ **포괄적인 에러 처리**

- ✅ **단계별 주석과 함께하는 깔끔하고 문서화된 코드**

### 완전한 예제로 시작하기

1. 위 표에서 **선호하는 언어를 선택하세요**
2. 전체 구현을 이해하기 위해 **완전한 예제 파일을 검토하세요**
3. [`complete_examples.md`](./complete_examples.md)의 지침을 따라 **예제를 실행하세요**
4. 특정 사용 사례에 맞게 예제를 **수정하고 확장하세요**

이 예제들을 실행하고 사용자화하는 방법에 대한 자세한 문서는 다음을 참조하세요: **[📖 완전한 예제 문서](./complete_examples.md)**

### 💡 솔루션 대 완전한 예제

| **솔루션 폴더** | **완전한 예제** |
|--------------------|--------------------- |
| 빌드 파일이 포함된 전체 프로젝트 구조 | 단일 파일 구현 |
| 종속성 포함 즉시 실행 가능 | 집중된 코드 예제 |
| 프로덕션과 유사한 설정 | 교육용 참고 자료 |
| 언어별 툴링 | 다중 언어 비교 |

두 접근 방식 모두 유용합니다 - 완전한 프로젝트는 <strong>솔루션 폴더</strong>를, 학습 및 참고용은 <strong>완전한 예제</strong>를 사용하세요.

## 주요 내용 정리

이 장에서 클라이언트에 대한 주요 내용은 다음과 같습니다:

- 서버의 기능을 발견하고 호출하는 데 모두 사용할 수 있습니다.
- 자체적으로 시작하면서 서버를 시작할 수 있으며(이 장처럼) 실행 중인 서버에 연결할 수 있습니다.
- 이전 장에서 설명한 검사기와 같은 대안과 함께 서버 기능을 테스트하는 좋은 방법입니다.

## 추가 자료

- [MCP에서 클라이언트 만들기](https://modelcontextprotocol.io/quickstart/client)

## 샘플

- [Java 계산기](../samples/java/calculator/README.md)
- [.NET 계산기](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 계산기](../samples/javascript/README.md)
- [TypeScript 계산기](../samples/typescript/README.md)
- [Python 계산기](../../../../03-GettingStarted/samples/python)
- [Rust 계산기](../../../../03-GettingStarted/samples/rust)

## 다음 단계

- 다음: [LLM으로 클라이언트 만들기](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->