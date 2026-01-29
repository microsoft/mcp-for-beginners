# HTTPS 스트리밍과 모델 컨텍스트 프로토콜 (MCP)

이 장에서는 HTTPS를 사용하여 안전하고 확장 가능하며 실시간 스트리밍을 구현하는 방법에 대한 포괄적인 가이드를 제공합니다. 스트리밍의 동기, 사용 가능한 전송 메커니즘, MCP에서 스트리밍 가능한 HTTP 구현 방법, 보안 모범 사례, SSE에서의 마이그레이션, 그리고 MCP 스트리밍 애플리케이션을 구축하기 위한 실용적인 지침을 다룹니다.

## MCP의 전송 메커니즘과 스트리밍

이 섹션에서는 MCP에서 사용할 수 있는 다양한 전송 메커니즘과 클라이언트와 서버 간 실시간 통신을 가능하게 하는 스트리밍 기능의 역할을 탐구합니다.

### 전송 메커니즘이란?

전송 메커니즘은 클라이언트와 서버 간 데이터 교환 방식을 정의합니다. MCP는 다양한 환경과 요구 사항에 맞는 여러 전송 유형을 지원합니다:

- **stdio**: 표준 입력/출력으로, 로컬 및 CLI 기반 도구에 적합합니다. 간단하지만 웹이나 클라우드에는 적합하지 않습니다.
- **SSE (서버-발송 이벤트)**: 서버가 HTTP를 통해 클라이언트에 실시간 업데이트를 푸시할 수 있도록 합니다. 웹 UI에 적합하지만 확장성과 유연성이 제한적입니다.
- **스트리밍 가능한 HTTP**: 알림과 더 나은 확장성을 지원하는 최신 HTTP 기반 스트리밍 전송. 대부분의 프로덕션 및 클라우드 시나리오에 권장됩니다.

### 비교 표

아래 비교 표를 통해 이러한 전송 메커니즘 간의 차이를 이해할 수 있습니다:

| 전송 방식         | 실시간 업데이트 | 스트리밍 | 확장성 | 사용 사례                |
|-------------------|----------------|-----------|---------|-------------------------|
| stdio             | 아니요         | 아니요    | 낮음    | 로컬 CLI 도구           |
| SSE               | 예             | 예        | 중간    | 웹, 실시간 업데이트      |
| 스트리밍 가능한 HTTP | 예             | 예        | 높음    | 클라우드, 다중 클라이언트 |

> **팁:** 적절한 전송 방식을 선택하는 것은 성능, 확장성, 사용자 경험에 영향을 미칩니다. **스트리밍 가능한 HTTP**는 현대적이고 확장 가능하며 클라우드에 적합한 애플리케이션에 권장됩니다.

이전 장에서 다룬 stdio와 SSE 전송 방식과, 이번 장에서 다룰 스트리밍 가능한 HTTP 전송 방식을 비교해 보세요.

## 스트리밍: 개념과 동기

스트리밍의 기본 개념과 동기를 이해하는 것은 효과적인 실시간 통신 시스템을 구현하는 데 필수적입니다.

**스트리밍**은 네트워크 프로그래밍에서 데이터를 한 번에 전체 응답을 기다리지 않고 작은 청크나 이벤트 시퀀스로 전송하고 수신할 수 있도록 하는 기술입니다. 이는 특히 다음과 같은 경우에 유용합니다:

- 대용량 파일 또는 데이터셋.
- 실시간 업데이트(예: 채팅, 진행률 표시줄).
- 사용자에게 정보를 지속적으로 제공해야 하는 장기 실행 작업.

스트리밍에 대해 알아야 할 주요 사항은 다음과 같습니다:

- 데이터는 한 번에 모두가 아닌 점진적으로 전달됩니다.
- 클라이언트는 데이터가 도착하는 즉시 처리할 수 있습니다.
- 지연 시간을 줄이고 사용자 경험을 향상시킵니다.

### 왜 스트리밍을 사용할까요?

스트리밍을 사용하는 이유는 다음과 같습니다:

- 사용자는 작업이 끝날 때까지 기다리지 않고 즉각적인 피드백을 받을 수 있습니다.
- 실시간 애플리케이션과 반응형 UI를 가능하게 합니다.
- 네트워크 및 컴퓨팅 자원을 더 효율적으로 사용할 수 있습니다.

### 간단한 예: HTTP 스트리밍 서버 및 클라이언트

다음은 스트리밍을 구현하는 간단한 예입니다:

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

이 예제는 서버가 모든 메시지가 준비될 때까지 기다리지 않고, 준비되는 대로 메시지를 클라이언트에 전송하는 방식을 보여줍니다.

**작동 방식:**

- 서버는 각 메시지가 준비될 때마다 이를 생성합니다.
- 클라이언트는 도착하는 각 청크를 수신하고 출력합니다.

**요구 사항:**

- 서버는 스트리밍 응답(e.g., FastAPI의 `StreamingResponse`)을 사용해야 합니다.
- 클라이언트는 응답을 스트림으로 처리해야 합니다(`stream=True` in requests).
- Content-Type은 일반적으로 `text/event-stream` 또는 `application/octet-stream`입니다.

#### Java

**서버 (Java, Spring Boot와 Server-Sent Events 사용):**

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

- Spring Boot의 반응형 스택과 `Flux`를 사용하여 스트리밍을 구현합니다.
- `ServerSentEvent`는 이벤트 유형이 있는 구조화된 이벤트 스트리밍을 제공합니다.
- `WebClient`의 `bodyToFlux()`는 반응형 스트리밍 소비를 가능하게 합니다.
- `delayElements()`는 이벤트 간 처리 시간을 시뮬레이션합니다.
- 이벤트는 클라이언트 처리를 개선하기 위해 유형(`info`, `result`)을 가질 수 있습니다.

### 비교: 고전적 스트리밍 vs MCP 스트리밍

고전적인 방식의 스트리밍과 MCP에서의 스트리밍 방식의 차이는 다음과 같이 요약할 수 있습니다:

| 특징                  | 고전적 HTTP 스트리밍         | MCP 스트리밍 (알림)            |
|------------------------|-----------------------------|--------------------------------|
| 주요 응답             | 청크로 전송                 | 끝에서 단일 응답               |
| 진행 업데이트         | 데이터 청크로 전송          | 알림으로 전송                  |
| 클라이언트 요구 사항  | 스트림 처리 필요            | 메시지 핸들러 구현 필요         |
| 사용 사례             | 대용량 파일, AI 토큰 스트림 | 진행 상황, 로그, 실시간 피드백 |

### 관찰된 주요 차이점

추가적으로, 다음과 같은 주요 차이점이 있습니다:

- **통신 패턴:**
  - 고전적 HTTP 스트리밍: 단순한 청크 전송 인코딩을 사용하여 데이터를 청크로 전송
  - MCP 스트리밍: JSON-RPC 프로토콜을 사용하는 구조화된 알림 시스템 사용

- **메시지 형식:**
  - 고전적 HTTP: 개행 문자로 구분된 일반 텍스트 청크
  - MCP: 메타데이터가 포함된 구조화된 LoggingMessageNotification 객체

- **클라이언트 구현:**
  - 고전적 HTTP: 스트리밍 응답을 처리하는 간단한 클라이언트
  - MCP: 다양한 유형의 메시지를 처리하기 위한 메시지 핸들러를 갖춘 더 정교한 클라이언트

- **진행 업데이트:**
  - 고전적 HTTP: 진행 상황이 주요 응답 스트림의 일부로 포함됨
  - MCP: 진행 상황이 별도의 알림 메시지를 통해 전송되며 주요 응답은 끝에서 제공됨

### 권장 사항

고전적 스트리밍(위에서 보여준 `/stream` 엔드포인트 사용)과 MCP를 통한 스트리밍 중에서 선택할 때 다음을 권장합니다:

- **간단한 스트리밍 요구 사항:** 고전적 HTTP 스트리밍은 구현이 간단하며 기본적인 스트리밍 요구 사항에 충분합니다.
- **복잡하고 상호작용적인 애플리케이션:** MCP 스트리밍은 더 구조화된 접근 방식을 제공하며, 메타데이터와 알림 및 최종 결과를 분리할 수 있습니다.
- **AI 애플리케이션:** MCP의 알림 시스템은 진행 상황을 사용자에게 알리고자 하는 장기 실행 AI 작업에 특히 유용합니다.

## MCP에서의 스트리밍

지금까지 고전적 스트리밍과 MCP 스트리밍의 차이점과 권장 사항을 살펴보았습니다. 이제 MCP에서 스트리밍을 활용하는 방법을 자세히 알아보겠습니다.

MCP 프레임워크 내에서 스트리밍이 작동하는 방식을 이해하는 것은 장기 실행 작업 중 사용자에게 실시간 피드백을 제공하는 반응형 애플리케이션을 구축하는 데 필수적입니다.

MCP에서 스트리밍은 주요 응답을 청크로 전송하는 것이 아니라, 도구가 요청을 처리하는 동안 클라이언트에 **알림**을 전송하는 것입니다. 이러한 알림에는 진행 상황 업데이트, 로그 또는 기타 이벤트가 포함될 수 있습니다.

### 작동 방식

주요 결과는 여전히 단일 응답으로 전송됩니다. 그러나 알림은 처리 중 별도의 메시지로 전송되어 클라이언트를 실시간으로 업데이트할 수 있습니다. 클라이언트는 이러한 알림을 처리하고 표시할 수 있어야 합니다.

## 알림이란 무엇인가?

MCP에서 "알림"이란 무엇을 의미할까요?

알림은 장기 실행 작업 중 진행 상황, 상태 또는 기타 이벤트를 알리기 위해 서버에서 클라이언트로 전송되는 메시지입니다. 알림은 투명성과 사용자 경험을 향상시킵니다.

예를 들어, 클라이언트는 서버와 초기 핸드셰이크를 완료한 후 알림을 전송해야 합니다.

알림은 다음과 같은 JSON 메시지 형태를 가집니다:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

알림은 MCP에서 ["로깅"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging)이라는 주제에 속합니다.

로깅을 작동시키려면 서버가 다음과 같이 기능/기능을 활성화해야 합니다:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 사용하는 SDK에 따라 로깅이 기본적으로 활성화되어 있을 수도 있고, 서버 설정에서 명시적으로 활성화해야 할 수도 있습니다.

알림에는 다양한 유형이 있습니다:

| 수준       | 설명                          | 예제 사용 사례                 |
|------------|-------------------------------|---------------------------------|
| debug      | 상세한 디버깅 정보            | 함수 진입/종료 지점            |
| info       | 일반 정보 메시지              | 작업 진행 상황 업데이트         |
| notice     | 정상적이지만 중요한 이벤트    | 구성 변경                      |
| warning    | 경고 조건                     | 사용 중단된 기능 사용           |
| error      | 오류 조건                     | 작업 실패                      |
| critical   | 치명적 조건                   | 시스템 구성 요소 실패           |
| alert      | 즉각적인 조치 필요            | 데이터 손상 감지               |
| emergency  | 시스템 사용 불가              | 전체 시스템 실패               |

## MCP에서 알림 구현

MCP에서 알림을 구현하려면 실시간 업데이트를 처리할 수 있도록 서버와 클라이언트 양쪽을 설정해야 합니다. 이를 통해 애플리케이션이 장기 실행 작업 중 사용자에게 즉각적인 피드백을 제공할 수 있습니다.

### 서버 측: 알림 전송

서버 측부터 시작해 보겠습니다. MCP에서는 요청을 처리하는 동안 알림을 전송할 수 있는 도구를 정의합니다. 서버는 컨텍스트 객체(일반적으로 `ctx`)를 사용하여 클라이언트에 메시지를 전송합니다.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

위 예제에서 `process_files` 도구는 각 파일을 처리할 때 클라이언트에 세 개의 알림을 전송합니다. `ctx.info()` 메서드는 정보 메시지를 전송하는 데 사용됩니다.

추가적으로, 알림을 활성화하려면 서버가 스트리밍 전송(예: `streamable-http`)을 사용하고 클라이언트가 알림을 처리할 메시지 핸들러를 구현해야 합니다. 서버를 `streamable-http` 전송을 사용하도록 설정하는 방법은 다음과 같습니다:

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

위 .NET 예제에서 `ProcessFiles` 도구는 `Tool` 특성으로 데코레이트되며, 각 파일을 처리할 때 클라이언트에 세 개의 알림을 전송합니다. `ctx.Info()` 메서드는 정보 메시지를 전송하는 데 사용됩니다.

.NET MCP 서버에서 알림을 활성화하려면 스트리밍 전송을 사용하고 있는지 확인하세요:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### 클라이언트 측: 알림 수신

클라이언트는 도착하는 알림을 처리하고 표시하기 위해 메시지 핸들러를 구현해야 합니다.

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

위 코드에서 `message_handler` 함수는 들어오는 메시지가 알림인지 확인합니다. 알림인 경우 이를 출력하고, 그렇지 않으면 일반 서버 메시지로 처리합니다. 또한 `ClientSession`이 알림을 처리하기 위해 `message_handler`로 초기화된 것을 확인하세요.

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

위 .NET 예제에서 `MessageHandler` 함수는 들어오는 메시지가 알림인지 확인합니다. 알림인 경우 이를 출력하고, 그렇지 않으면 일반 서버 메시지로 처리합니다. `ClientSession`은 `ClientSessionOptions`를 통해 메시지 핸들러와 함께 초기화됩니다.

알림을 활성화하려면 서버가 스트리밍 전송(예: `streamable-http`)을 사용하고 클라이언트가 알림을 처리할 메시지 핸들러를 구현해야 합니다.

## 진행 알림 및 시나리오

이 섹션에서는 MCP에서 진행 알림의 개념, 중요성, Streamable HTTP를 사용한 구현 방법을 설명합니다. 또한 이해를 강화하기 위한 실습 과제를 제공합니다.

진행 알림은 장기 실행 작업 중 서버에서 클라이언트로 전송되는 실시간 메시지입니다. 전체 프로세스가 완료될 때까지 기다리는 대신, 서버는 현재 상태에 대한 업데이트를 클라이언트에 제공합니다. 이는 투명성을 높이고 사용자 경험을 개선하며 디버깅을 용이하게 합니다.

**예제:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### 왜 진행 알림을 사용할까요?

진행 알림은 다음과 같은 이유로 필수적입니다:

- **더 나은 사용자 경험:** 작업이 진행됨에 따라 업데이트를 제공하여 애플리케이션이 반응형으로 느껴지게 합니다.
- **실시간 피드백:** 클라이언트가 진행률 표시줄이나 로그를 표시할 수 있습니다.
- **디버깅 및 모니터링 용이:** 프로세스가 느리거나 멈춘 부분을 확인할 수 있습니다.

### 진행 알림 구현 방법

MCP에서 진행 알림을 구현하는 방법은 다음과 같습니다:

- **서버 측:** 각 항목이 처리될 때 `ctx.info()` 또는 `ctx.log()`를 사용하여 알림을 전송합니다. 이는 주요 결과가 준비되기 전에 클라이언트에 메시지를 전송합니다.
- **클라이언트 측:** 도착하는 알림을 수신하고 표시하는 메시지 핸들러를 구현합니다. 이 핸들러는 알림과 최종 결과를 구분합니다.

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

## 보안 고려 사항

HTTP 기반 전송을 사용하는 MCP 서버를 구현할 때, 보안은 여러 공격 벡터와 보호 메커니즘에 대해 신중히 고려해야 하는 중요한 문제입니다.

### 개요

HTTP를 통해 MCP 서버를 노출할 때 보안은 매우 중요합니다. 스트리밍 가능한 HTTP는 새로운 공격 표면을 도입하며 신중한 구성이 필요합니다.

### 주요 사항

- **Origin 헤더 검증:** DNS 재바인딩 공격을 방지하기 위해 항상 `Origin` 헤더를 검증하세요.
- **로컬호스트 바인딩:** 로컬 개발의 경우, 서버를 `localhost`에 바인딩하여 공용 인터넷에 노출되지 않도록 하세요.
- **인증:** 프로덕션 배포를 위해 인증(e.g., API 키, OAuth)을 구현하세요.
- **CORS:** 교차 출처 리소스 공유(CORS) 정책을 구성하여 접근을 제한하세요.
- **HTTPS:** 트래픽을 암호화하기 위해 프로덕션 환경에서 HTTPS를 사용하세요.

### 모범 사례

- 유효성 검증 없이 들어오는 요청을 신뢰하지 마세요.
- 모든 접근 및 오류를 로깅하고 모니터링하세요.
- 보안 취약점을 패치하기 위해 종속성을 정기적으로 업데이트하세요.

### 도전 과제

- 개발 용이성과 보안 간 균형 유지
- 다양한 클라이언트 환경과의 호환성 보장

## SSE에서 스트리밍 가능한 HTTP로 업그레이드

현재 Server-Sent Events(SSE)를 사용하는 애플리케이션의 경우, 스트리밍 가능한 HTTP로 마이그레이션하면 MCP 구현에 대한 향상된 기능과 더 나은 장기적 지속 가능성을 제공합니다.

### 왜 업그레이드해야 할까요?
SSE에서 Streamable HTTP로 업그레이드해야 하는 두 가지 주요 이유는 다음과 같습니다:

- Streamable HTTP는 SSE보다 더 나은 확장성, 호환성, 풍부한 알림 지원을 제공합니다.
- 새로운 MCP 애플리케이션에 권장되는 전송 방식입니다.

### 마이그레이션 단계

MCP 애플리케이션에서 SSE를 Streamable HTTP로 마이그레이션하는 방법은 다음과 같습니다:

- **서버 코드 업데이트**: `mcp.run()`에서 `transport="streamable-http"`를 사용하도록 수정합니다.
- **클라이언트 코드 업데이트**: SSE 클라이언트 대신 `streamablehttp_client`를 사용하도록 변경합니다.
- **메시지 핸들러 구현**: 클라이언트에서 알림을 처리하는 메시지 핸들러를 구현합니다.
- **기존 도구 및 워크플로와의 호환성 테스트**를 수행합니다.

### 호환성 유지

마이그레이션 과정에서 기존 SSE 클라이언트와의 호환성을 유지하는 것이 좋습니다. 다음과 같은 전략을 사용할 수 있습니다:

- 서로 다른 엔드포인트에서 SSE와 Streamable HTTP를 모두 지원할 수 있습니다.
- 클라이언트를 새로운 전송 방식으로 점진적으로 마이그레이션합니다.

### 과제

마이그레이션 중 다음과 같은 과제를 해결해야 합니다:

- 모든 클라이언트를 업데이트하는 작업
- 알림 전달 방식의 차이 처리

## 보안 고려사항

Streamable HTTP와 같은 HTTP 기반 전송 방식을 사용할 때, 서버 구현 시 보안을 최우선으로 고려해야 합니다.

HTTP 기반 전송 방식을 사용하는 MCP 서버를 구현할 때는 여러 공격 벡터와 보호 메커니즘에 대해 신중히 검토해야 합니다.

### 개요

MCP 서버를 HTTP를 통해 노출할 때 보안은 매우 중요합니다. Streamable HTTP는 새로운 공격 표면을 도입하며, 신중한 구성이 필요합니다.

다음은 주요 보안 고려사항입니다:

- **Origin 헤더 검증**: DNS 리바인딩 공격을 방지하기 위해 항상 `Origin` 헤더를 검증하세요.
- **로컬호스트 바인딩**: 로컬 개발 시 서버를 `localhost`에 바인딩하여 공용 인터넷에 노출되지 않도록 합니다.
- **인증**: 프로덕션 배포 시 API 키, OAuth 등의 인증을 구현하세요.
- **CORS**: 교차 출처 리소스 공유(CORS) 정책을 구성하여 접근을 제한하세요.
- **HTTPS**: 프로덕션 환경에서는 HTTPS를 사용하여 트래픽을 암호화하세요.

### 모범 사례

MCP 스트리밍 서버 구현 시 다음 모범 사례를 따르는 것이 좋습니다:

- 검증되지 않은 요청을 신뢰하지 마세요.
- 모든 접근 및 오류를 로깅하고 모니터링하세요.
- 보안 취약점을 패치하기 위해 종속성을 정기적으로 업데이트하세요.

### 과제

MCP 스트리밍 서버에서 보안을 구현할 때 다음과 같은 과제에 직면할 수 있습니다:

- 개발의 용이성과 보안 간의 균형 유지
- 다양한 클라이언트 환경과의 호환성 보장

### 과제: 나만의 스트리밍 MCP 애플리케이션 구축

**시나리오:**
서버가 항목(예: 파일 또는 문서) 목록을 처리하고 처리된 각 항목에 대해 알림을 보내는 MCP 서버와 클라이언트를 구축하세요. 클라이언트는 도착하는 각 알림을 실시간으로 표시해야 합니다.

**단계:**

1. 목록을 처리하고 각 항목에 대해 알림을 보내는 서버 도구를 구현합니다.
2. 알림을 실시간으로 표시하는 메시지 핸들러를 포함한 클라이언트를 구현합니다.
3. 서버와 클라이언트를 실행하여 알림을 관찰하며 구현을 테스트합니다.

[Solution](./solution/README.md)

## 추가 학습 및 다음 단계

MCP 스트리밍에 대한 지식을 확장하고 더 고급 애플리케이션을 구축하기 위한 추가 리소스와 제안된 다음 단계를 제공합니다.

### 추가 학습

- [Microsoft: HTTP 스트리밍 소개](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET Core의 CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: 스트리밍 요청](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 다음 단계

- 실시간 분석, 채팅, 협업 편집을 위한 스트리밍을 사용하는 더 고급 MCP 도구를 만들어 보세요.
- MCP 스트리밍을 프론트엔드 프레임워크(React, Vue 등)와 통합하여 실시간 UI 업데이트를 탐구하세요.
- 다음: [VSCode용 AI 툴킷 활용](../07-aitk/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.