# 클라이언트 생성하기

클라이언트는 MCP 서버와 직접 통신하여 리소스, 도구, 프롬프트를 요청하는 맞춤형 애플리케이션 또는 스크립트입니다. 서버와 상호작용하기 위해 그래픽 인터페이스를 제공하는 검사 도구를 사용하는 것과 달리, 클라이언트를 직접 작성하면 프로그래밍 방식으로 자동화된 상호작용이 가능합니다. 이를 통해 개발자는 MCP 기능을 자신의 워크플로우에 통합하고, 작업을 자동화하며, 특정 요구에 맞춘 맞춤형 솔루션을 구축할 수 있습니다.

## 개요

이 강의에서는 Model Context Protocol (MCP) 생태계 내에서 클라이언트의 개념을 소개합니다. 여러분은 직접 클라이언트를 작성하고 MCP 서버에 연결하는 방법을 배우게 됩니다.

## 학습 목표

이 강의를 마치면 다음을 할 수 있습니다:

- 클라이언트가 할 수 있는 일을 이해하기
- 직접 클라이언트 작성하기
- MCP 서버와 클라이언트를 연결하고 테스트하여 서버가 예상대로 작동하는지 확인하기

## 클라이언트를 작성하려면 무엇이 필요할까요?

클라이언트를 작성하려면 다음을 수행해야 합니다:

- **적절한 라이브러리 가져오기**. 이전에 사용했던 동일한 라이브러리를 사용하지만 다른 구성 요소를 사용합니다.
- **클라이언트 인스턴스화**. 클라이언트 인스턴스를 생성하고 선택한 전송 방식에 연결합니다.
- **리소스를 나열할지 결정하기**. MCP 서버는 리소스, 도구, 프롬프트를 제공하며, 나열할 항목을 결정해야 합니다.
- **클라이언트를 호스트 애플리케이션에 통합하기**. 서버의 기능을 파악한 후, 이를 호스트 애플리케이션에 통합하여 사용자가 프롬프트나 다른 명령을 입력하면 해당 서버 기능이 호출되도록 합니다.

이제 우리가 무엇을 할 것인지 높은 수준에서 이해했으니, 다음으로 예제를 살펴보겠습니다.

### 예제 클라이언트

다음은 예제 클라이언트입니다:

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

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

위 코드에서 우리는:

- 라이브러리를 가져옵니다.
- 클라이언트 인스턴스를 생성하고 stdio를 사용하여 연결합니다.
- 프롬프트, 리소스, 도구를 나열하고 모두 호출합니다.

이제 MCP 서버와 통신할 수 있는 클라이언트가 완성되었습니다.

다음 연습 섹션에서 각 코드 스니펫을 자세히 살펴보고 어떤 일이 일어나는지 설명해 보겠습니다.

## 연습: 클라이언트 작성하기

앞서 말했듯이, 코드를 설명하는 데 시간을 들이고, 원한다면 직접 코드를 작성하며 따라 해보세요.

### -1- 라이브러리 가져오기

필요한 라이브러리를 가져옵니다. 클라이언트와 선택한 전송 프로토콜(stdio)에 대한 참조가 필요합니다. stdio는 로컬 머신에서 실행되는 것에 적합한 프로토콜입니다. SSE는 다른 전송 프로토콜로, 이후 챕터에서 보여드릴 예정입니다. 지금은 stdio로 계속 진행하겠습니다.

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
using ModelContextProtocol.Protocol.Transport;
```

#### Java

Java에서는 이전 연습에서 사용한 MCP 서버에 연결하는 클라이언트를 생성합니다. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java)에서 사용한 Java Spring Boot 프로젝트 구조를 사용하여 `src/main/java/com/microsoft/mcp/sample/client/` 폴더에 `SDKClient`라는 새 Java 클래스를 생성하고 다음과 같은 라이브러리를 가져옵니다:

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

`Cargo.toml` 파일에 다음 종속성을 추가해야 합니다.

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

이제 인스턴스화를 진행해 보겠습니다.

### -2- 클라이언트와 전송 인스턴스화

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

- stdio 전송 인스턴스를 생성했습니다. 서버를 찾고 시작하는 방법을 지정하는 명령과 인수를 포함하는 것을 확인하세요. 이는 클라이언트를 생성할 때 필요합니다.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- 이름과 버전을 지정하여 클라이언트를 인스턴스화했습니다.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- 선택한 전송 방식에 클라이언트를 연결했습니다.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

위 코드에서 우리는:

- 필요한 라이브러리를 가져왔습니다.
- 서버 매개변수 객체를 인스턴스화했습니다. 이를 사용하여 서버를 실행하고 클라이언트와 연결할 수 있습니다.
- `run` 메서드를 정의하여 `stdio_client`를 호출하고 클라이언트 세션을 시작합니다.
- `asyncio.run`에 `run` 메서드를 제공하는 진입점을 생성했습니다.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

위 코드에서 우리는:

- 필요한 라이브러리를 가져왔습니다.
- stdio 전송을 생성하고 클라이언트 `mcpClient`를 생성했습니다. 이는 MCP 서버에서 기능을 나열하고 호출하는 데 사용할 것입니다.

참고로 "Arguments"에서는 *.csproj* 또는 실행 파일을 지정할 수 있습니다.

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
        
        // Your client logic goes here
    }
}
```

위 코드에서 우리는:

- MCP 서버가 실행될 `http://localhost:8080`을 가리키는 SSE 전송을 설정하는 메인 메서드를 생성했습니다.
- 전송을 생성자 매개변수로 받는 클라이언트 클래스를 생성했습니다.
- `run` 메서드에서 전송을 사용하여 동기 MCP 클라이언트를 생성하고 연결을 초기화했습니다.
- Java Spring Boot MCP 서버와 HTTP 기반 통신에 적합한 SSE(Server-Sent Events) 전송을 사용했습니다.

#### Rust

이 Rust 클라이언트는 동일한 디렉터리에 있는 "calculator-server"라는 서버 프로젝트를 가정합니다. 아래 코드는 서버를 시작하고 연결합니다.

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
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

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- 서버 기능 나열하기

이제 프로그램을 실행하면 연결할 수 있는 클라이언트가 생겼습니다. 하지만 실제로 기능을 나열하지는 않으므로 이를 다음 단계에서 추가해 보겠습니다:

#### TypeScript

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

#### Python

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

여기서 사용 가능한 리소스 `list_resources()`와 도구 `list_tools`를 나열하고 출력합니다.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

위는 서버의 도구를 나열하는 방법의 예입니다. 각 도구에 대해 이름을 출력합니다.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

위 코드에서 우리는:

- MCP 서버에서 사용 가능한 모든 도구를 가져오기 위해 `listTools()`를 호출했습니다.
- 서버와의 연결이 작동하는지 확인하기 위해 `ping()`을 사용했습니다.
- `ListToolsResult`는 도구의 이름, 설명, 입력 스키마를 포함한 정보를 제공합니다.

좋습니다. 이제 모든 기능을 캡처했습니다. 그렇다면 언제 이를 사용할까요? 이 클라이언트는 매우 간단하며, 우리가 원하는 기능을 명시적으로 호출해야 합니다. 다음 챕터에서는 자체 대형 언어 모델(LLM)을 갖춘 더 고급 클라이언트를 생성할 것입니다. 지금은 서버의 기능을 호출하는 방법을 살펴보겠습니다:

#### Rust

메인 함수에서 클라이언트를 초기화한 후 서버를 초기화하고 일부 기능을 나열할 수 있습니다.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- 기능 호출하기

기능을 호출하려면 올바른 인수와 경우에 따라 호출하려는 이름을 지정해야 합니다.

#### TypeScript

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

위 코드에서 우리는:

- 리소스를 읽습니다. `readResource()`를 호출하여 `uri`를 지정합니다. 서버 측에서 다음과 같이 보일 것입니다:

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

    우리의 `uri` 값 `file://example.txt`는 서버의 `file://{name}`과 일치합니다. `example.txt`는 `name`으로 매핑됩니다.

- 도구를 호출합니다. `name`과 `arguments`를 지정하여 호출합니다:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- 프롬프트를 가져옵니다. `getPrompt()`를 호출하여 `name`과 `arguments`를 지정합니다. 서버 코드는 다음과 같습니다:

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

    따라서 클라이언트 코드는 서버에 선언된 내용을 일치시키기 위해 다음과 같이 보일 것입니다:

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
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

위 코드에서 우리는:

- `read_resource`를 사용하여 `greeting`이라는 리소스를 호출했습니다.
- `call_tool`을 사용하여 `add`라는 도구를 호출했습니다.

#### .NET

1. 도구를 호출하는 코드를 추가합니다:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. 결과를 출력하기 위한 코드는 다음과 같습니다:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call various calculator tools
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

- `CallToolRequest` 객체를 사용하여 여러 계산기 도구를 호출했습니다.
- 각 도구 호출은 도구 이름과 해당 도구에 필요한 인수의 `Map`을 지정합니다.
- 서버 도구는 특정 매개변수 이름(예: "a", "b"와 같은 수학적 연산)을 기대합니다.
- 결과는 서버에서 반환된 응답을 포함하는 `CallToolResult` 객체로 반환됩니다.

#### Rust

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
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

*package.json*의 "scripts" 섹션에 다음 항목을 추가합니다:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

다음 명령으로 클라이언트를 호출합니다:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

먼저 MCP 서버가 `http://localhost:8080`에서 실행 중인지 확인합니다. 그런 다음 클라이언트를 실행합니다:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

또는 `03-GettingStarted\02-client\solution\java` 솔루션 폴더에 제공된 전체 클라이언트 프로젝트를 실행할 수 있습니다:

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## 과제

이번 과제에서는 배운 내용을 활용하여 직접 클라이언트를 생성합니다.

다음은 클라이언트 코드로 호출해야 할 서버입니다. 서버에 더 많은 기능을 추가하여 더 흥미롭게 만들어 보세요.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout

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

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
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

이 프로젝트를 확인하여 [프롬프트와 리소스 추가](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) 방법을 알아보세요.

또한 [프롬프트와 리소스 호출](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) 방법에 대한 링크를 확인하세요.

### Rust

[이전 섹션](../../../../03-GettingStarted/01-first-server)에서 Rust로 간단한 MCP 서버를 생성하는 방법을 배웠습니다. 이를 계속 확장하거나 Rust 기반 MCP 서버 예제를 확인하려면 다음 링크를 참조하세요: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## 솔루션

**솔루션 폴더**에는 이 튜토리얼에서 다룬 모든 개념을 보여주는 완전한 실행 가능한 클라이언트 구현이 포함되어 있습니다. 각 솔루션에는 클라이언트와 서버 코드가 별도의 독립적인 프로젝트로 구성되어 있습니다.

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

- **완전한 클라이언트 구현**: 튜토리얼의 모든 기능 포함
- **작동하는 프로젝트 구조**: 적절한 종속성과 구성 포함
- **빌드 및 실행 스크립트**: 간편한 설정 및 실행
- **상세한 README**: 언어별 지침 포함
- **에러 처리** 및 결과 처리 예제

### 📖 솔루션 사용 방법

1. **선호하는 언어 폴더로 이동**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **각 폴더의 README 지침을 따르세요**:
   - 종속성 설치
   - 프로젝트 빌드
   - 클라이언트 실행

3. **예상 출력**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

전체 문서와 단계별 지침은 다음을 참조하세요: **[📖 솔루션 문서](./solution/README.md)**

## 🎯 완전한 예제

이 튜토리얼에서 설명한 모든 기능을 보여주는 완전한 실행 가능한 클라이언트 구현을 제공합니다. 이러한 예제는 참조 구현 또는 자체 프로젝트의 시작점으로 사용할 수 있습니다.

### 제공된 완전한 예제

| 언어       | 파일                          | 설명                                                                 |
|------------|-------------------------------|----------------------------------------------------------------------|
| **Java**   | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE 전송을 사용하는 완전한 Java 클라이언트, 포괄적인 에러 처리 포함 |
| **C#**     | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio 전송을 사용하는 완전한 C# 클라이언트, 자동 서버 시작 포함     |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP 프로토콜을 완전히 지원하는 TypeScript 클라이언트                |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await 패턴을 사용하는 완전한 Python 클라이언트                 |
| **Rust**   | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)     | 비동기 작업을 위한 Tokio를 사용하는 완전한 Rust 클라이언트           |
각 완성된 예제는 다음을 포함합니다:

- ✅ **연결 설정** 및 오류 처리
- ✅ **서버 탐색** (도구, 리소스, 프롬프트 등 필요 시)
- ✅ **계산기 작업** (더하기, 빼기, 곱하기, 나누기, 도움말)
- ✅ **결과 처리** 및 포맷된 출력
- ✅ **포괄적인 오류 처리**
- ✅ **깨끗하고 문서화된 코드** (단계별 주석 포함)

### 완성된 예제로 시작하기

1. 위 표에서 **선호하는 언어를 선택**하세요.
2. **완성된 예제 파일을 검토**하여 전체 구현을 이해하세요.
3. [`complete_examples.md`](./complete_examples.md)의 지침을 따라 **예제를 실행**하세요.
4. **예제를 수정 및 확장**하여 특정 사용 사례에 맞게 조정하세요.

이 예제를 실행하고 커스터마이징하는 방법에 대한 자세한 문서는 **[📖 완성된 예제 문서](./complete_examples.md)**를 참조하세요.

### 💡 솔루션 vs. 완성된 예제

| **솔루션 폴더** | **완성된 예제** |
|--------------------|--------------------- |
| 빌드 파일이 포함된 전체 프로젝트 구조 | 단일 파일 구현 |
| 종속성을 포함하여 바로 실행 가능 | 집중된 코드 예제 |
| 프로덕션 환경과 유사한 설정 | 교육용 참고 자료 |
| 언어별 도구 지원 | 언어 간 비교 |

두 접근법 모두 유용합니다 - **솔루션 폴더**는 전체 프로젝트에 적합하며, **완성된 예제**는 학습 및 참고용으로 사용하세요.

## 주요 요점

이 챕터의 주요 요점은 클라이언트에 대한 다음 내용입니다:

- 서버에서 기능을 탐색하고 호출하는 데 사용할 수 있습니다.
- 클라이언트는 자체적으로 시작하면서 서버를 시작할 수 있지만, 실행 중인 서버에 연결할 수도 있습니다.
- 이전 챕터에서 설명한 Inspector와 같은 대안과 함께 서버 기능을 테스트하는 훌륭한 방법입니다.

## 추가 리소스

- [MCP에서 클라이언트 빌드하기](https://modelcontextprotocol.io/quickstart/client)

## 샘플

- [Java 계산기](../samples/java/calculator/README.md)
- [.Net 계산기](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 계산기](../samples/javascript/README.md)
- [TypeScript 계산기](../samples/typescript/README.md)
- [Python 계산기](../../../../03-GettingStarted/samples/python)
- [Rust 계산기](../../../../03-GettingStarted/samples/rust)

## 다음 단계

- 다음: [LLM을 사용한 클라이언트 생성](../03-llm-client/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.