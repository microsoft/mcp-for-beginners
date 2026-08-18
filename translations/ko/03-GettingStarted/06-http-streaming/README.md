# 모델 컨텍스트 프로토콜(MCP)을 이용한 HTTPS 스트리밍

이 장에서는 HTTPS를 사용하여 모델 컨텍스트 프로토콜(MCP)로 보안성, 확장성, 실시간 스트리밍을 구현하는 포괄적인 가이드를 제공합니다. 이 장에서는 스트리밍의 동기, 사용 가능한 전송 메커니즘, MCP에서 스트리밍 가능한 HTTP 구현 방법, 보안 모범 사례, SSE에서의 마이그레이션, 그리고 자체 스트리밍 MCP 애플리케이션 구축에 대한 실용적인 지침을 다룹니다.

> **미리보기:** 이 수업은 `initialize` 중 세션을 설정하고 `Mcp-Session-Id` 헤더로 고정하는 <strong>MCP 사양 2025-11-25</strong>의 스트리밍 가능한 HTTP를 설명합니다. `2026-07-28` 릴리스 후보에서는 핸드셰이크와 세션 ID가 완전히 제거되어 모든 요청이 자체 포함되어 있고 접착 세션 없이도 모든 서버 인스턴스로 라우팅 가능합니다. 자세한 내용은 [MCP에서 변경 사항: 2026-07-28 릴리스 후보](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)를 참조하세요.

## MCP의 전송 메커니즘과 스트리밍

이 절에서는 MCP에서 사용할 수 있는 다양한 전송 메커니즘과 이들이 클라이언트와 서버 간 실시간 통신을 위한 스트리밍 기능 구현에 어떻게 기여하는지 탐구합니다.

### 전송 메커니즘이란?

전송 메커니즘은 클라이언트와 서버 간 데이터 교환 방식을 정의합니다. MCP는 다양한 환경과 요구 사항에 맞는 여러 전송 유형을 지원합니다:

- **stdio**: 표준 입출력으로, 로컬 및 CLI 기반 도구에 적합합니다. 간단하지만 웹이나 클라우드에는 적합하지 않습니다.
- **SSE (서버-전송 이벤트)**: 서버가 HTTP를 통해 클라이언트로 실시간 업데이트를 푸시할 수 있습니다. 웹 UI에 좋지만 확장성 및 유연성이 제한적입니다. MCP 사양 2025-06-18부터 독립적인 SSE (서버-전송 이벤트) 전송은 더 이상 사용하지 않으며 "스트리밍 가능한 HTTP" 전송으로 대체되었습니다.
- **스트리밍 가능한 HTTP**: 알림 및 향상된 확장성을 지원하는 최신 HTTP 기반 스트리밍 전송입니다. 대부분 프로덕션 및 클라우드 시나리오에 권장됩니다.

### 비교표

다음 비교표를 통해 이들 전송 메커니즘 간 차이점을 이해하세요:

| 전송             | 실시간 업데이트 | 스트리밍 | 확장성    | 용도                   |
|-------------------|-----------------|-----------|----------|------------------------|
| stdio             | 아니요          | 아니요    | 낮음     | 로컬 CLI 도구          |
| SSE               | 예              | 예        | 중간     | 웹, 실시간 업데이트    |
| 스트리밍 가능한 HTTP | 예              | 예        | 높음     | 클라우드, 다중 클라이언트 |

> **팁:** 적절한 전송 방식 선택은 성능, 확장성, 사용자 경험에 영향을 줍니다. <strong>스트리밍 가능한 HTTP</strong>가 현대적이고 확장 가능하며 클라우드에 적합한 애플리케이션에 권장됩니다.

이전 장에서 보여준 stdio와 SSE 전송에 주목하고, 이번 장에서 다루는 스트리밍 가능한 HTTP 전송이 어떤 것인지 확인하세요.

## 스트리밍: 개념 및 동기

스트리밍 뒤에 있는 기본 개념과 동기를 이해하는 것은 효과적인 실시간 통신 시스템을 구현하는 데 필수적입니다.

<strong>스트리밍</strong>은 네트워크 프로그래밍에서 데이터를 응답 전체가 준비되기를 기다리는 대신 작고 관리하기 쉬운 조각이나 이벤트의 연속으로 보내고 받는 기술입니다. 특히 다음과 같은 경우에 유용합니다:

- 대용량 파일 또는 데이터셋.
- 실시간 업데이트(예: 채팅, 진행 표시줄).
- 사용자를 지속적으로 정보를 제공해야 하는 장기 연산.

스트리밍에 대해 알아야 할 주요 사항:

- 데이터가 한꺼번에가 아니라 점진적으로 전달됩니다.
- 클라이언트가 도착하는 데이터를 즉시 처리할 수 있습니다.
- 지연 인식을 줄이고 사용자 경험을 개선합니다.

### 스트리밍을 사용하는 이유는?

스트리밍 사용 이유는 다음과 같습니다:

- 사용자는 작업 완료 시점이 아닌 즉시 피드백을 받습니다.
- 실시간 애플리케이션 및 반응형 UI를 구현합니다.
- 네트워크와 컴퓨팅 자원의 효율적 활용.

### 간단한 예: HTTP 스트리밍 서버 & 클라이언트

스트리밍이 어떻게 구현될 수 있는지 간단한 예를 살펴봅시다:

#### Python

**서버 (Python, FastAPI와 StreamingResponse 사용):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**클라이언트 (Python, requests 사용):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

이 예시는 모든 메시지가 준비될 때까지 기다리지 않고 사용할 수 있는 대로 서버가 메시지 시리즈를 클라이언트로 보내는 것을 보여줍니다.

**작동 원리:**

- 서버는 각 메시지가 준비되는 대로 순차적으로 전송합니다.
- 클라이언트는 도착하는 각 조각을 받아 출력합니다.

**요구사항:**

- 서버는 스트리밍 응답(예: FastAPI의 `StreamingResponse`)을 사용해야 합니다.
- 클라이언트는 스트림으로 응답을 처리해야 합니다(`requests`의 `stream=True`).
- Content-Type은 보통 `text/event-stream` 또는 `application/octet-stream`입니다.

#### Java

**서버 (Java, Spring Boot 및 Server-Sent Events 사용):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**클라이언트 (Java, Spring WebFlux WebClient 사용):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Java 구현 참고 사항:**

- Spring Boot의 reactive 스택과 `Flux`를 사용한 스트리밍
- `ServerSentEvent`는 이벤트 타입을 가진 구조화된 이벤트 스트리밍 제공
- `WebClient`의 `bodyToFlux()`를 통해 reactive 스트리밍 소비 가능
- `delayElements()`는 이벤트간 처리 지연을 시뮬레이션
- 이벤트에 `info`, `result`와 같은 타입 지정 가능으로 클라이언트 처리 용이

### 비교: 클래식 스트리밍 vs MCP 스트리밍

고전적 방식의 스트리밍과 MCP 방식의 스트리밍 작동 차이는 다음과 같이 정리할 수 있습니다:

| 특징                | 클래식 HTTP 스트리밍          | MCP 스트리밍 (알림)              |
|---------------------|------------------------------|----------------------------------|
| 주요 응답           | 청크 단위                    | 단일 응답, 마지막에 전송         |
| 진행 업데이트       | 데이터 청크로 전송           | 알림으로 전송                    |
| 클라이언트 요구사항 | 스트림을 처리해야 함          | 메시지 핸들러 구현 필요           |
| 사용 사례           | 대용량 파일, AI 토큰 스트림   | 진행 상황, 로그, 실시간 피드백    |

### 관찰된 주요 차이점

추가로, 주요 차이점은 다음과 같습니다:

- **통신 패턴:**
  - 클래식 HTTP 스트리밍: 단순 청크 전송 인코딩 사용
  - MCP 스트리밍: JSON-RPC 프로토콜을 활용한 구조화된 알림 시스템 사용

- **메시지 형식:**
  - 클래식 HTTP: 줄바꿈이 포함된 일반 텍스트 청크
  - MCP: 메타데이터를 포함한 구조화된 LoggingMessageNotification 객체

- **클라이언트 구현:**
  - 클래식 HTTP: 스트리밍 응답을 처리하는 간단한 클라이언트
  - MCP: 다양한 메시지 유형을 처리하는 메시지 핸들러가 있는 복잡한 클라이언트

- **진행 업데이트:**
  - 클래식 HTTP: 진행 상황이 주요 응답 스트림의 일부
  - MCP: 진행 상황은 별도의 알림 메시지로 전송되고, 주요 결과는 마지막에 전달

### 권장 사항

고전적 스트리밍(`/stream` 엔드포인트 사용)과 MCP 스트리밍 중 선택할 때 권장 사항은 다음과 같습니다.

- **간단한 스트리밍 필요 시:** 클래식 HTTP 스트리밍이 구현이 간단하며 기본 스트리밍에 충분합니다.

- **복잡하고 상호작용적인 애플리케이션용:** MCP 스트리밍은 더 풍부한 메타데이터와 알림 및 최종 결과 분리를 제공하는 체계적인 접근법입니다.

- **AI 응용 프로그램용:** MCP의 알림 시스템은 장시간 실행되는 AI 작업에서 사용자에게 진행 상황을 알리는 데 특히 유용합니다.

## MCP에서의 스트리밍

지금까지 고전적 스트리밍과 MCP 스트리밍의 비교 및 권장 사항을 보았습니다. 이제 MCP에서 스트리밍을 활용하는 구체적인 방법을 살펴봅니다.

MCP 프레임워크 내에서 스트리밍이 어떻게 작동하는지 이해하는 것은 장기 실행 작업 동안 사용자에게 실시간 피드백을 제공하는 반응형 애플리케이션 구축에 필수적입니다.

MCP에서는 응답 본문을 청크로 나누어 전송하는 것이 아니라 도구가 요청을 처리하는 동안 <strong>알림</strong>을 클라이언트에 보내는 방식입니다. 이 알림은 진행 업데이트, 로그 또는 기타 이벤트를 포함할 수 있습니다.

### 작동 방식

주요 결과는 여전히 단일 응답으로 전달됩니다. 그러나 처리 중 별도의 메시지로 알림이 전송되어 클라이언트를 실시간으로 업데이트할 수 있습니다. 클라이언트는 이러한 알림을 처리하고 표시할 수 있어야 합니다.

## 알림이란 무엇인가?

"알림"이라고 했을 때 MCP 맥락에서 이것이 의미하는 바는 무엇일까요?

알림은 장기간 작업 중 진행 상황, 상태 또는 기타 이벤트에 대해 서버가 클라이언트에게 보내는 메시지입니다. 알림은 투명성과 사용자 경험을 향상시킵니다.

예를 들어, 클라이언트는 초기 핸드셰이크가 서버와 완료되면 알림을 보내야 합니다.

알림은 다음과 같이 JSON 메시지 형태입니다:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

알림은 MCP에서 ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging)이라는 주제에 속합니다.

> **폐기 알림:** `2026-07-28` MCP 사양 릴리스 후보에서는 stdio 전송용 `stderr`와 구조화된 관측성을 위한 OpenTelemetry 사용을 제안하면서 Logging 원시형을 더 이상 사용하지 않습니다. Logging은 `2025-11-25` 및 공식 폐기 후 최소 1년 동안 계속 동작합니다. 자세한 내용은 [MCP에서 변경 사항: 2026-07-28 릴리스 후보](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)를 참조하세요.

로깅을 동작하게 하려면 서버는 다음과 같이 기능/능력으로 활성화해야 합니다:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 사용하는 SDK에 따라 로깅이 기본 활성화되어 있거나 서버 구성을 통해 명시적으로 활성화해야 할 수도 있습니다.

다양한 알림 유형이 있습니다:

| 레벨      | 설명                          | 예시 용도                     |
|-----------|-------------------------------|-------------------------------|
| debug     | 상세 디버깅 정보               | 함수 진입/종료 지점           |
| info      | 일반 정보 메시지              | 작업 진행 업데이트            |
| notice    | 정상적이지만 중요한 이벤트    | 구성 변경                    |
| warning   | 경고 조건                   | 더 이상 사용하지 않는 기능 사용 |
| error     | 오류 조건                   | 작업 실패                    |
| critical  | 치명적 조건                 | 시스템 구성 요소 실패          |
| alert     | 즉각 조치 필요               | 데이터 손상 감지              |
| emergency | 시스템 사용 불가             | 전체 시스템 실패              |

## MCP에서 알림 구현하기

MCP에서 알림을 구현하려면 서버와 클라이언트 양쪽을 실시간 업데이트를 처리하도록 설정해야 합니다. 이를 통해 애플리케이션은 장기 작업 중 사용자에게 즉각 피드백을 제공합니다.

### 서버 측: 알림 전송

먼저 서버 측부터 시작합시다. MCP에서는 요청 처리 중 알림을 보낼 수 있는 도구를 정의합니다. 서버는 일반적으로 `ctx`인 컨텍스트 객체를 사용해 클라이언트에 메시지를 보냅니다.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

이전 예제에서 `process_files` 도구는 각 파일을 처리하면서 클라이언트에 세 개의 알림을 보냅니다. `ctx.info()` 메서드는 정보 메시지를 보내는 데 사용됩니다.

또한 알림 기능을 활성화하려면 서버가 스트리밍 전송(`streamable-http` 등)을 사용하고 클라이언트가 알림을 처리할 메시지 핸들러를 구현해야 합니다. 다음은 서버에서 `streamable-http` 전송을 설정하는 예입니다:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

이 .NET 예제에서 `ProcessFiles` 도구는 각 파일 처리 중 클라이언트에 세 개의 알림을 보냅니다. `ctx.Info()` 메서드가 정보 메시지를 전송하는 데 사용됩니다.

.NET MCP 서버에서 알림을 활성화하려면 스트리밍 전송을 사용하고 있는지 확인하세요:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### 클라이언트 측: 알림 수신

클라이언트는 도착하는 알림을 처리하고 표시할 메시지 핸들러를 구현해야 합니다.

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

앞 코드에서 `message_handler` 함수는 들어오는 메시지가 알림인지 확인합니다. 알림이면 출력하고 그렇지 않으면 일반 서버 메시지로 처리합니다. 또한 `ClientSession`이 `message_handler`와 함께 초기화되어 알림을 처리함을 주목하세요.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

이 .NET 예제에서 `MessageHandler` 함수는 수신 메시지가 알림인지 검사합니다. 알림이면 출력하고 아니면 일반 서버 메시지로 처리합니다. `ClientSession`은 `ClientSessionOptions`를 통해 메시지 핸들러와 함께 초기화됩니다.

알림을 활성화하려면 서버에서 스트리밍 전송(`streamable-http` 등)을 사용하고 클라이언트가 알림 처리용 메시지 핸들러를 구현해야 합니다.

## 진행 알림 및 시나리오

이 절에서는 MCP에서 진행 알림의 개념과 중요성, 스트리밍 가능한 HTTP를 사용해 구현하는 방법을 설명합니다. 또한 이해를 돕는 실습 과제가 포함되어 있습니다.

진행 알림은 장기 실행 작업 중 서버가 클라이언트로 보내는 실시간 메시지입니다. 전체 프로세스가 끝날 때까지 기다리지 않고 서버가 현재 상태를 계속 업데이트합니다. 이는 투명성과 사용자 경험을 개선하며 디버깅을 용이하게 합니다.

**예시:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### 진행 알림을 사용하는 이유는?

진행 알림은 여러 이유로 중요합니다:

- **향상된 사용자 경험:** 작업 진행 상황을 사용자가 끝까지 기다리지 않고 바로 확인할 수 있습니다.
- **실시간 피드백:** 클라이언트가 진행률 표시줄이나 로그를 표시해 앱의 반응성을 높입니다.
- **디버깅 및 모니터링 용이:** 개발자와 사용자가 프로세스의 지연 또는 중단 지점을 파악할 수 있습니다.

### 진행 알림 구현 방법

MCP에서 진행 알림을 구현하는 방법은 다음과 같습니다:

- **서버 측:** 각 항목 처리 시 `ctx.info()` 또는 `ctx.log()`를 사용해 알림을 전송합니다. 이는 주요 결과가 준비되기 전에 클라이언트에 메시지를 보냅니다.
- **클라이언트 측:** 도착하는 알림을 수신하고 표시하는 메시지 핸들러를 구현합니다. 핸들러는 알림과 최종 결과를 구분 처리합니다.

**서버 예제:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**클라이언트 예제:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## 보안 고려사항

어떤 서버를 구현할 때든 보안은 최우선 과제여야 하며, 특히 MCP에서 Streamable HTTP와 같은 HTTP 기반 전송을 사용할 때 더욱 그렇습니다.

HTTP 기반 전송을 사용하는 MCP 서버를 구현할 때는 여러 공격 벡터와 보호 메커니즘에 신중하게 주의를 기울여야 하므로 보안이 매우 중요합니다.

### 개요

MCP 서버를 HTTP를 통해 노출할 때 보안은 매우 중요합니다. Streamable HTTP는 새로운 공격면을 만들어 내고 신중한 구성이 필요합니다.

주요 보안 고려 사항은 다음과 같습니다:

- **Origin 헤더 검증**: DNS 재결합 공격을 방지하기 위해 항상 `Origin` 헤더를 검증하세요.
- **로컬호스트 바인딩**: 로컬 개발 시에는 서버를 `localhost`에 바인딩하여 공용 인터넷에 노출되지 않도록 하세요.
- <strong>인증</strong>: 실제 배포 시에는 API 키나 OAuth와 같은 인증을 구현하세요.
- **CORS**: 접근을 제한하기 위해 교차 출처 리소스 공유(CORS) 정책을 구성하세요.
- **HTTPS**: 프로덕션 환경에서는 트래픽 암호화를 위해 HTTPS를 사용하세요.

### 모범 사례

MCP 스트리밍 서버에서 보안을 구현할 때 따르는 것이 좋은 모범 사례는 다음과 같습니다:

- 무조건 검증 없이 요청을 신뢰하지 마세요.
- 모든 접근과 오류를 기록하고 모니터링하세요.
- 보안 취약점을 패치하기 위해 의존성 라이브러리를 정기적으로 업데이트하세요.

### 도전 과제

MCP 스트리밍 서버에서 보안을 구현할 때 직면할 도전 과제는 다음과 같습니다:

- 개발의 용이성과 보안의 균형 유지
- 다양한 클라이언트 환경과의 호환성 확보


## SSE에서 Streamable HTTP로 업그레이드하기

현재 Server-Sent Events(SSE)를 사용 중인 애플리케이션의 경우, Streamable HTTP로 마이그레이션하면 향상된 기능과 더 나은 장기적 확장성을 얻을 수 있습니다.

### 업그레이드가 필요한 이유

SSE에서 Streamable HTTP로 업그레이드해야 할 두 가지 주요 이유는 다음과 같습니다:

- Streamable HTTP는 SSE보다 더 나은 확장성, 호환성 및 풍부한 알림 지원을 제공합니다.
- 새로운 MCP 애플리케이션에 권장되는 전송 방식입니다.

### 마이그레이션 단계

MCP 애플리케이션에서 SSE에서 Streamable HTTP로 마이그레이션하는 방법은 다음과 같습니다:

- <strong>서버 코드를 업데이트</strong>하여 `mcp.run()`에서 `transport="streamable-http"`를 사용하세요.
- <strong>클라이언트 코드를 업데이트</strong>하여 SSE 클라이언트 대신 `streamablehttp_client`를 사용하세요.
- <strong>알림을 처리하는 메시지 핸들러를 클라이언트에 구현</strong>하세요.
- <strong>기존 도구 및 워크플로와의 호환성 테스트</strong>를 수행하세요.

### 호환성 유지

마이그레이션 과정에서 기존 SSE 클라이언트와의 호환성을 유지하는 것이 권장됩니다. 다음과 같은 전략이 있습니다:

- 서로 다른 엔드포인트에서 SSE와 Streamable HTTP 두 가지 전송을 모두 지원할 수 있습니다.
- 클라이언트를 점진적으로 새로운 전송 방식으로 전환하세요.

### 도전 과제

마이그레이션 중에 다음 도전 과제를 해결해야 합니다:

- 모든 클라이언트가 업데이트되도록 보장
- 알림 전달 방식의 차이 처리

### 과제: 나만의 스트리밍 MCP 앱 만들기

**시나리오:**
서버가 항목 목록(예: 파일 또는 문서)을 처리하고 각 항목이 처리될 때마다 알림을 보내도록 MCP 서버와 클라이언트를 구축하세요. 클라이언트는 각 알림을 수신 즉시 표시해야 합니다.

**단계:**

1. 항목 목록을 처리하고 각 항목에 대한 알림을 보내는 서버 도구를 구현하세요.
2. 알림을 실시간으로 표시하는 메시지 핸들러가 있는 클라이언트를 구현하세요.
3. 서버와 클라이언트를 모두 실행하여 구현을 테스트하고 알림을 관찰하세요.

[해결책](./solution/README.md)

## 추가 읽기 자료 및 다음 단계

MCP 스트리밍에 대한 여정을 계속하고 지식을 확장하기 위해 이 섹션에서는 추가 자료와 더 고급 애플리케이션 구축을 위한 권장 다음 단계를 제공합니다.

### 추가 읽기 자료

- [Microsoft: HTTP 스트리밍 소개](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET Core에서의 CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: 스트리밍 요청](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 다음 단계

- 실시간 분석, 채팅 또는 협업 편집을 위해 스트리밍을 사용하는 더 고급 MCP 도구를 구축해 보세요.
- 프런트엔드 프레임워크(React, Vue 등)와 MCP 스트리밍을 통합하여 라이브 UI 업데이트를 탐색하세요.
- 다음: [VSCode용 AI 툴킷 활용하기](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->