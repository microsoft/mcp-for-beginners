# MCP 서버와 stdio 전송 방식

> **⚠️ 중요 업데이트**: MCP 사양 2025-06-18 기준으로, 독립형 SSE(Server-Sent Events) 전송 방식은 **더 이상 사용되지 않으며** "Streamable HTTP" 전송 방식으로 대체되었습니다. 현재 MCP 사양은 두 가지 주요 전송 메커니즘을 정의합니다:
> 1. **stdio** - 표준 입력/출력 (로컬 서버에 권장)
> 2. **Streamable HTTP** - 내부적으로 SSE를 사용할 수 있는 원격 서버용
>
> 이 강의는 대부분의 MCP 서버 구현에 권장되는 **stdio 전송 방식**에 초점을 맞추도록 업데이트되었습니다.

stdio 전송 방식은 MCP 서버가 표준 입력 및 출력 스트림을 통해 클라이언트와 통신할 수 있도록 합니다. 이는 현재 MCP 사양에서 가장 일반적으로 사용되고 권장되는 전송 메커니즘으로, 다양한 클라이언트 애플리케이션과 쉽게 통합할 수 있는 간단하고 효율적인 방법을 제공합니다.

## 개요

이 강의에서는 stdio 전송 방식을 사용하여 MCP 서버를 구축하고 사용하는 방법을 다룹니다.

## 학습 목표

이 강의를 마치면 다음을 수행할 수 있습니다:

- stdio 전송 방식을 사용하여 MCP 서버를 구축하기
- Inspector를 사용하여 MCP 서버 디버깅하기
- Visual Studio Code를 사용하여 MCP 서버 소비하기
- 현재 MCP 전송 메커니즘과 stdio가 권장되는 이유 이해하기

## stdio 전송 방식 - 작동 원리

stdio 전송 방식은 현재 MCP 사양(2025-06-18)에서 지원되는 두 가지 전송 유형 중 하나입니다. 작동 방식은 다음과 같습니다:

- **간단한 통신**: 서버는 표준 입력(`stdin`)에서 JSON-RPC 메시지를 읽고 표준 출력(`stdout`)으로 메시지를 보냅니다.
- **프로세스 기반**: 클라이언트는 MCP 서버를 하위 프로세스로 실행합니다.
- **메시지 형식**: 메시지는 개별 JSON-RPC 요청, 알림 또는 응답으로, 줄바꿈으로 구분됩니다.
- **로깅**: 서버는 로깅 목적으로 표준 오류(`stderr`)에 UTF-8 문자열을 기록할 수 있습니다.

### 주요 요구 사항:
- 메시지는 반드시 줄바꿈으로 구분되어야 하며, 포함된 줄바꿈을 포함해서는 안 됩니다.
- 서버는 `stdout`에 유효한 MCP 메시지가 아닌 내용을 기록해서는 안 됩니다.
- 클라이언트는 서버의 `stdin`에 유효한 MCP 메시지가 아닌 내용을 기록해서는 안 됩니다.

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

위 코드에서:

- MCP SDK에서 `Server` 클래스와 `StdioServerTransport`를 가져옵니다.
- 기본 구성과 기능을 가진 서버 인스턴스를 생성합니다.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

위 코드에서:

- MCP SDK를 사용하여 서버 인스턴스를 생성합니다.
- 데코레이터를 사용하여 도구를 정의합니다.
- stdio_server 컨텍스트 관리자를 사용하여 전송을 처리합니다.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

SSE와의 주요 차이점은 stdio 서버가:

- 웹 서버 설정이나 HTTP 엔드포인트를 필요로 하지 않습니다.
- 클라이언트에 의해 하위 프로세스로 실행됩니다.
- stdin/stdout 스트림을 통해 통신합니다.
- 구현 및 디버깅이 더 간단합니다.

## 연습: stdio 서버 생성하기

서버를 생성하려면 두 가지를 염두에 두어야 합니다:

- 연결 및 메시지를 위한 엔드포인트를 노출하기 위해 웹 서버를 사용해야 합니다.

## 실습: 간단한 MCP stdio 서버 생성하기

이 실습에서는 권장되는 stdio 전송 방식을 사용하여 간단한 MCP 서버를 생성합니다. 이 서버는 클라이언트가 표준 Model Context Protocol을 사용하여 호출할 수 있는 도구를 노출합니다.

### 사전 준비

- Python 3.8 이상
- MCP Python SDK: `pip install mcp`
- 비동기 프로그래밍에 대한 기본 이해

첫 번째 MCP stdio 서버를 생성해 봅시다:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## 기존 SSE 접근 방식과의 주요 차이점

**Stdio 전송 방식(현재 표준):**
- 간단한 하위 프로세스 모델 - 클라이언트가 서버를 자식 프로세스로 실행
- JSON-RPC 메시지를 사용하여 stdin/stdout을 통해 통신
- HTTP 서버 설정 불필요
- 더 나은 성능과 보안
- 디버깅 및 개발이 더 쉬움

**SSE 전송 방식(MCP 2025-06-18 기준으로 더 이상 사용되지 않음):**
- SSE 엔드포인트가 있는 HTTP 서버 필요
- 웹 서버 인프라를 포함한 더 복잡한 설정
- HTTP 엔드포인트에 대한 추가 보안 고려 사항
- 웹 기반 시나리오를 위한 Streamable HTTP로 대체됨

### stdio 전송 방식으로 서버 생성하기

stdio 서버를 생성하려면 다음을 수행해야 합니다:

1. **필요한 라이브러리 가져오기** - MCP 서버 구성 요소와 stdio 전송을 가져옵니다.
2. **서버 인스턴스 생성** - 서버를 정의하고 기능을 설정합니다.
3. **도구 정의** - 노출하려는 기능 추가
4. **전송 설정** - stdio 통신 구성
5. **서버 실행** - 서버를 시작하고 메시지 처리

단계별로 진행해 봅시다:

### 단계 1: 기본 stdio 서버 생성

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### 단계 2: 더 많은 도구 추가

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### 단계 3: 서버 실행

코드를 `server.py`로 저장하고 명령줄에서 실행합니다:

```bash
python server.py
```

서버는 시작되어 stdin에서 입력을 기다립니다. JSON-RPC 메시지를 stdio 전송 방식으로 통신합니다.

### 단계 4: Inspector로 테스트하기

MCP Inspector를 사용하여 서버를 테스트할 수 있습니다:

1. Inspector 설치: `npx @modelcontextprotocol/inspector`
2. Inspector를 실행하고 서버를 지정합니다.
3. 생성한 도구를 테스트합니다.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## stdio 서버 디버깅하기

### MCP Inspector 사용하기

MCP Inspector는 MCP 서버를 디버깅하고 테스트하는 데 유용한 도구입니다. stdio 서버와 함께 사용하는 방법은 다음과 같습니다:

1. **Inspector 설치**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector 실행**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **서버 테스트**: Inspector는 웹 인터페이스를 제공하며, 여기서 다음을 수행할 수 있습니다:
   - 서버 기능 보기
   - 다양한 매개변수로 도구 테스트
   - JSON-RPC 메시지 모니터링
   - 연결 문제 디버깅

### VS Code 사용하기

VS Code에서 MCP 서버를 직접 디버깅할 수도 있습니다:

1. `.vscode/launch.json`에 실행 구성 생성:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. 서버 코드에 중단점을 설정합니다.
3. 디버거를 실행하고 Inspector로 테스트합니다.

### 일반적인 디버깅 팁

- `stderr`를 로깅에 사용하세요 - `stdout`은 MCP 메시지에 예약되어 있습니다.
- 모든 JSON-RPC 메시지가 줄바꿈으로 구분되었는지 확인하세요.
- 복잡한 기능을 추가하기 전에 간단한 도구로 테스트하세요.
- Inspector를 사용하여 메시지 형식을 확인하세요.

## VS Code에서 stdio 서버 소비하기

MCP stdio 서버를 구축한 후 Claude 또는 다른 MCP 호환 클라이언트와 함께 사용하기 위해 VS Code에 통합할 수 있습니다.

### 구성

1. **MCP 구성 파일 생성**: Windows에서는 `%APPDATA%\Claude\claude_desktop_config.json`, Mac에서는 `~/Library/Application Support/Claude/claude_desktop_config.json`에 생성합니다:

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Claude 재시작**: Claude를 닫았다가 다시 열어 새 서버 구성을 로드합니다.

3. **연결 테스트**: Claude와 대화를 시작하고 서버의 도구를 사용해 보세요:
   - "greeting 도구를 사용해 나를 환영해 줄 수 있나요?"
   - "15와 27의 합을 계산해 주세요."
   - "서버 정보를 알려주세요."

### TypeScript stdio 서버 예제

다음은 참고용으로 완전한 TypeScript 예제입니다:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET stdio 서버 예제

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## 요약

이 업데이트된 강의에서 다음을 배웠습니다:

- 현재 권장되는 **stdio 전송 방식**을 사용하여 MCP 서버 구축하기
- SSE 전송 방식이 stdio 및 Streamable HTTP로 대체된 이유 이해하기
- MCP 클라이언트가 호출할 수 있는 도구 생성하기
- MCP Inspector를 사용하여 서버 디버깅하기
- VS Code 및 Claude와 stdio 서버 통합하기

stdio 전송 방식은 더 간단하고, 더 안전하며, 더 성능이 뛰어난 방법으로, 2025-06-18 사양 기준으로 대부분의 MCP 서버 구현에 권장됩니다.

### .NET

1. 먼저 몇 가지 도구를 생성합니다. 이를 위해 *Tools.cs* 파일을 다음 내용으로 생성합니다:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 연습: stdio 서버 테스트하기

stdio 서버를 구축한 후, 올바르게 작동하는지 테스트해 봅시다.

### 사전 준비

1. MCP Inspector가 설치되어 있는지 확인하세요:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 서버 코드를 저장하세요(예: `server.py`).

### Inspector로 테스트하기

1. **Inspector를 서버와 함께 시작**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **웹 인터페이스 열기**: Inspector는 브라우저 창을 열어 서버의 기능을 보여줍니다.

3. **도구 테스트**: 
   - `get_greeting` 도구를 사용하여 다양한 이름으로 테스트
   - `calculate_sum` 도구를 사용하여 다양한 숫자로 테스트
   - `get_server_info` 도구를 호출하여 서버 메타데이터 확인

4. **통신 모니터링**: Inspector는 클라이언트와 서버 간에 교환되는 JSON-RPC 메시지를 보여줍니다.

### 예상 결과

서버가 올바르게 시작되면 다음을 볼 수 있습니다:
- Inspector에 서버 기능이 나열됨
- 테스트 가능한 도구 표시
- 성공적인 JSON-RPC 메시지 교환
- 인터페이스에 도구 응답 표시

### 일반적인 문제와 해결 방법

**서버가 시작되지 않음:**
- 모든 종속성이 설치되었는지 확인: `pip install mcp`
- Python 구문 및 들여쓰기 확인
- 콘솔의 오류 메시지 확인

**도구가 나타나지 않음:**
- `@server.tool()` 데코레이터가 있는지 확인
- 도구 함수가 `main()` 이전에 정의되었는지 확인
- 서버가 올바르게 구성되었는지 확인

**연결 문제:**
- 서버가 stdio 전송 방식을 올바르게 사용하고 있는지 확인
- 다른 프로세스가 방해하고 있지 않은지 확인
- Inspector 명령 구문 확인

## 과제

서버에 더 많은 기능을 추가해 보세요. 예를 들어, [이 페이지](https://api.chucknorris.io/)를 참조하여 API를 호출하는 도구를 추가해 보세요. 서버를 어떻게 구성할지는 여러분의 선택입니다. 재미있게 해보세요 :)

## 해결 방법

[해결 방법](./solution/README.md) 작동하는 코드가 포함된 가능한 해결 방법입니다.

## 주요 내용

이 장의 주요 내용은 다음과 같습니다:

- stdio 전송 방식은 로컬 MCP 서버에 권장되는 메커니즘입니다.
- stdio 전송 방식은 표준 입력 및 출력 스트림을 사용하여 MCP 서버와 클라이언트 간에 원활한 통신을 제공합니다.
- Inspector와 Visual Studio Code를 사용하여 stdio 서버를 직접 소비할 수 있어 디버깅과 통합이 간단합니다.

## 샘플 

- [Java 계산기](../samples/java/calculator/README.md)
- [.Net 계산기](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 계산기](../samples/javascript/README.md)
- [TypeScript 계산기](../samples/typescript/README.md)
- [Python 계산기](../../../../03-GettingStarted/samples/python) 

## 추가 자료

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 다음 단계

## 다음 단계

stdio 전송 방식을 사용하여 MCP 서버를 구축하는 방법을 배웠으니, 더 고급 주제를 탐구해 보세요:

- **다음**: [MCP의 HTTP 스트리밍(Streamable HTTP)](../06-http-streaming/README.md) - 원격 서버를 위한 다른 지원 전송 메커니즘 배우기
- **고급**: [MCP 보안 모범 사례](../../02-Security/README.md) - MCP 서버에 보안을 구현하기
- **운영**: [배포 전략](../09-deployment/README.md) - 운영 환경에서 서버 배포하기

## 추가 자료

- [MCP 사양 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 공식 사양
- [MCP SDK 문서](https://github.com/modelcontextprotocol/sdk) - 모든 언어에 대한 SDK 참조
- [커뮤니티 예제](../../06-CommunityContributions/README.md) - 커뮤니티에서 제공하는 더 많은 서버 예제

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.