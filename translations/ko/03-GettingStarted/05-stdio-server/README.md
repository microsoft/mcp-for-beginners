# stdio 전송을 사용하는 MCP 서버

> **⚠️ 중요한 업데이트**: MCP 사양 2025-06-18부터 독립형 SSE(Server-Sent Events) 전송은 **더 이상 사용되지 않으며** "스트리밍 HTTP" 전송으로 대체되었습니다. 현재 MCP 사양은 두 가지 주요 전송 메커니즘을 정의합니다:
> 1. **stdio** - 표준 입력/출력 (로컬 서버에 권장)
> 2. **스트리밍 HTTP** - 내부적으로 SSE를 사용할 수 있는 원격 서버용
>
> 이 강의는 대부분 MCP 서버 구현에 권장되는 <strong>stdio 전송</strong>에 중점을 두도록 업데이트되었습니다.

stdio 전송은 MCP 서버가 표준 입력과 출력 스트림을 통해 클라이언트와 통신할 수 있게 합니다. 이는 현재 MCP 사양에서 가장 많이 사용되고 권장되는 전송 메커니즘으로, 다양한 클라이언트 애플리케이션과 쉽게 통합할 수 있는 간단하고 효율적인 MCP 서버 구축 방식을 제공합니다.

## 개요

이 강의에서는 stdio 전송을 사용하여 MCP 서버를 구축하고 사용하는 방법을 다룹니다.

## 학습 목표

이 강의를 마치면 다음을 할 수 있습니다:

- stdio 전송을 사용해 MCP 서버를 구축하기
- Inspector를 사용해 MCP 서버 디버깅하기
- Visual Studio Code에서 MCP 서버를 사용하기
- 현재 MCP 전송 메커니즘과 stdio가 권장되는 이유 이해하기


## stdio 전송 - 작동 방식

stdio 전송은 현재 MCP 사양(2025-06-18)에서 지원하는 두 가지 전송 유형 중 하나입니다. 작동 방식은 다음과 같습니다:

- **간단한 통신**: 서버는 표준 입력(`stdin`)으로부터 JSON-RPC 메시지를 읽고 표준 출력(`stdout`)으로 메시지를 보냄
- **프로세스 기반**: 클라이언트가 MCP 서버를 서브프로세스로 실행
- **메시지 형식**: 메시지는 개별 JSON-RPC 요청, 알림 또는 응답이며 줄바꿈 문자로 구분됨
- <strong>로깅</strong>: 서버는 표준 에러(`stderr`)에 UTF-8 문자열을 기록할 수 있음

### 주요 요구사항:
- 메시지는 줄바꿈 문자로 구분되어야 하며 줄내림 문자 포함 불가
- 서버는 유효한 MCP 메시지가 아닌 어떤 것도 `stdout`에 출력해선 안 됨
- 클라이언트는 유효하지 않은 MCP 메시지를 서버의 `stdin`에 보내선 안 됨

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

앞 코드에서는:

- MCP SDK에서 `Server` 클래스와 `StdioServerTransport`를 가져옴
- 기본 구성과 기능을 갖춘 서버 인스턴스를 생성
- `StdioServerTransport` 인스턴스를 생성하고 서버를 연결하여 stdin/stdout을 통한 통신 활성화

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# 서버 인스턴스 생성
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

앞 코드에서는:

- MCP SDK를 사용해 서버 인스턴스 생성
- 데코레이터로 도구 정의
- stdio_server 컨텍스트 매니저로 전송 처리

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

SSE와 다른 핵심 차이점은 stdio 서버는:

- 웹 서버 설정이나 HTTP 엔드포인트가 필요 없음
- 클라이언트가 서브프로세스로 실행
- stdin/stdout 스트림을 통해 통신
- 구현과 디버깅이 더 간단함

## 연습: stdio 서버 생성

서버를 만들 때 두 가지를 염두에 둬야 합니다:

- 연결과 메시지를 위한 엔드포인트를 노출하려면 웹 서버를 사용해야 합니다.
## 실습: 간단한 MCP stdio 서버 만들기

이 실습에서는 권장되는 stdio 전송을 사용해 간단한 MCP 서버를 만듭니다. 이 서버는 표준 Model Context Protocol을 사용해 클라이언트가 호출할 수 있는 도구를 노출합니다.

### 사전 준비 사항

- Python 3.8 이상
- MCP Python SDK: `pip install mcp`
- 비동기 프로그래밍 기본 이해

처음 MCP stdio 서버를 만들어 봅시다:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# 로깅 구성
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 서버 생성
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
    # stdio 전송 사용
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## 더 이상 지원하지 않는 SSE 방식과의 주요 차이점

**Stdio 전송 (현재 표준):**
- 간단한 서브프로세스 모델 - 클라이언트가 서버를 자식 프로세스로 실행
- stdin/stdout을 이용한 JSON-RPC 메시지 통신
- HTTP 서버 설정 불필요
- 성능과 보안 향상
- 개발 및 디버깅 용이

**SSE 전송 (MCP 2025-06-18부터 더 이상 사용 안 함):**
- SSE 엔드포인트가 있는 HTTP 서버 필요
- 웹 서버 인프라 설정 복잡
- HTTP 엔드포인트 관련 추가 보안 고려 사항 존재
- 웹 기반 시나리오에 대해 이제 스트리밍 HTTP로 대체됨

### stdio 전송으로 서버 생성하기

stdio 서버를 만들려면:

1. **필요한 라이브러리 가져오기** - MCP 서버 구성 요소와 stdio 전송 필요
2. **서버 인스턴스 생성** - 기능과 함께 서버 정의
3. **도구 정의** - 노출할 기능 추가
4. **전송 설정** - stdio 통신 구성
5. **서버 실행** - 서버 시작 및 메시지 처리

단계별로 구축해 봅시다:

### 1단계: 기본 stdio 서버 만들기

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# 로깅 구성
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 서버 생성
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

### 2단계: 도구 추가하기

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

### 3단계: 서버 실행하기

코드를 `server.py`로 저장하고 명령줄에서 실행:

```bash
python server.py
```

서버가 시작되어 stdin으로부터 입력을 기다립니다. stdio 전송을 통해 JSON-RPC 메시지로 통신합니다.

### 4단계: Inspector로 테스트하기

MCP Inspector를 사용해 서버를 테스트할 수 있습니다:

1. Inspector 설치: `npx @modelcontextprotocol/inspector`
2. Inspector 실행 후 서버에 연결
3. 생성한 도구 테스트

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## stdio 서버 디버깅하기

### MCP Inspector 사용하기

MCP Inspector는 MCP 서버를 디버깅하고 테스트하는 유용한 도구입니다. stdio 서버와 함께 사용하는 방법은 다음과 같습니다:

1. **Inspector 설치**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector 실행**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **서버 테스트**: Inspector는 다음 기능을 제공하는 웹 인터페이스를 지원합니다:
   - 서버 기능 보기
   - 다양한 매개변수로 도구 테스트
   - JSON-RPC 메시지 모니터링
   - 연결 문제 디버깅

### VS Code 사용하기

VS Code에서 직접 MCP 서버 디버깅도 가능합니다:

1. `.vscode/launch.json` 파일에 실행 구성 생성:
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

2. 서버 코드에 중단점 설정
3. 디버거 실행 후 Inspector로 테스트

### 일반 디버깅 팁

- 로깅에는 `stderr` 사용 - `stdout`은 MCP 메시지 전용이므로 절대 사용 금지
- 모든 JSON-RPC 메시지는 줄바꿈 문자로 구분되어야 함
- 복잡한 기능 추가 전 간단한 도구부터 테스트
- 메시지 형식 검증에 Inspector 활용

## VS Code에서 stdio 서버 사용하기

stdio MCP 서버를 구축했다면 VS Code와 통합하여 Claude 또는 다른 MCP 호환 클라이언트와 함께 사용할 수 있습니다.

### 설정

1. Windows의 경우 `%APPDATA%\Claude\claude_desktop_config.json`, Mac의 경우 `~/Library/Application Support/Claude/claude_desktop_config.json` 위치에 MCP 구성 파일 생성:

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

2. **Claude 재시작**: Claude를 닫았다가 다시 열어 새 서버 구성을 반영

3. **연결 테스트**: Claude와 대화 시작 후 서버 도구 사용 시도:
   - "인사 도구를 사용해 인사해 줄래?"
   - "15와 27의 합을 계산해 줘"
   - "서버 정보가 뭐야?"

### TypeScript stdio 서버 예제

참고용 TypeScript 완성 예제:

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

// 도구 추가
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
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## 요약

이번 업데이트된 강의에서 배운 점:

- 현재 **stdio 전송**(권장 방식)을 사용해 MCP 서버 구축하기
- SSE 전송이 stdio와 스트리밍 HTTP로 대체된 이유 이해하기
- MCP 클라이언트가 호출할 도구 만들기
- MCP Inspector를 사용해 서버 디버깅하기
- VS Code 및 Claude와 stdio 서버 통합하기

stdio 전송은 더 이상 사용되지 않는 SSE 방식보다 MCP 서버를 더 간단하고, 안전하며, 성능 좋게 구축할 수 있는 방법입니다. 2025-06-18 사양 기준으로 대부분 MCP 서버 구현에 권장되는 전송입니다.


### .NET

1. 먼저 몇 가지 도구를 만들어보겠습니다. 이를 위해 <em>Tools.cs</em>라는 파일을 생성하고 다음 내용을 작성합니다:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 연습: stdio 서버 테스트하기

stdio 서버를 구축했으니 제대로 동작하는지 테스트해 봅시다.

### 사전 준비 사항

1. MCP Inspector 설치 여부 확인:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 서버 코드는 저장되어 있어야 함 (예: `server.py`)

### Inspector를 이용한 테스트

1. **서버와 함께 Inspector 시작**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **웹 인터페이스 열기**: Inspector가 브라우저 창에서 서버의 기능을 표시합니다.

3. **도구 테스트**: 
   - `get_greeting` 도구를 여러 이름으로 시도
   - `calculate_sum` 도구를 다양한 숫자로 테스트
   - `get_server_info` 도구 호출하여 서버 메타데이터 확인

4. **통신 모니터링**: Inspector가 클라이언트와 서버 간 JSON-RPC 메시지를 보여줍니다.

### 기대 결과

서버가 올바르게 시작되면 다음을 볼 수 있습니다:
- Inspector에서 서버 기능 목록 표시
- 테스트 가능한 도구들
- JSON-RPC 메시지의 정상 교환
- 인터페이스에 표시되는 도구 응답

### 자주 발생하는 문제와 해결책

**서버가 시작되지 않을 때:**
- 모든 의존성 설치 확인: `pip install mcp`
- Python 문법 및 들여쓰기 점검
- 콘솔의 오류 메시지 확인

**도구가 나타나지 않을 때:**
- `@server.tool()` 데코레이터가 있는지 확인
- 도구 함수가 `main()` 이전에 정의되어 있는지 확인
- 서버가 올바르게 구성됐는지 점검

**연결 문제:**
- 서버가 stdio 전송을 적절히 사용하는지 확인
- 다른 프로세스가 방해하지 않는지 점검
- Inspector 명령 구문 확인

## 과제

더 많은 기능을 추가하며 서버를 확장해 보세요. 예를 들어 [이 페이지](https://api.chucknorris.io/)를 참고해 API를 호출하는 도구를 추가할 수 있습니다. 서버를 어떻게 만들지는 여러분의 선택입니다. 즐겁게 만드세요 :)
## 해결책

[해결책](./solution/README.md) 정상 작동하는 코드 예시입니다.

## 주요 정리

이 챕터에서 얻은 주요 내용은 다음과 같습니다:

- stdio 전송은 로컬 MCP 서버에 권장되는 메커니즘입니다.
- stdio 전송은 표준 입출력 스트림을 이용해 MCP 서버와 클라이언트 간 원활한 통신을 가능케 합니다.
- Inspector와 Visual Studio Code 둘 다 stdio 서버를 직접 사용해 디버깅과 통합이 용이합니다.

## 샘플

- [Java 계산기](../samples/java/calculator/README.md)
- [.Net 계산기](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 계산기](../samples/javascript/README.md)
- [TypeScript 계산기](../samples/typescript/README.md)
- [Python 계산기](../../../../03-GettingStarted/samples/python) 

## 추가 자료

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 다음은?

## 다음 단계

stdlib 전송으로 MCP 서버를 만드는 법을 배웠으니, 더 심화된 주제를 탐색해보세요:

- <strong>다음</strong>: [MCP HTTP 스트리밍(스트리밍 HTTP)](../06-http-streaming/README.md) - 원격 서버용 다른 지원 전송 메커니즘 학습
- <strong>고급</strong>: [MCP 보안 모범 사례](../../02-Security/README.md) - MCP 서버 보안 구현
- <strong>운영</strong>: [배포 전략](../09-deployment/README.md) - 운영용 서버 배포

## 추가 자료

- [MCP 사양 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 공식 사양서
- [MCP SDK 문서](https://github.com/modelcontextprotocol/sdk) - 모든 언어용 SDK 참고 자료
- [커뮤니티 예제](../../06-CommunityContributions/README.md) - 커뮤니티에서 만든 서버 예제 더 보기

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문가의 인간 번역을 권장합니다. 이 번역의 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->