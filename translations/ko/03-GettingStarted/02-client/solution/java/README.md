# MCP Java Client - 계산기 데모

이 프로젝트는 MCP(Model Context Protocol) 서버에 연결하고 상호작용하는 Java 클라이언트를 만드는 방법을 보여줍니다. 이 예제에서는 1장에 나온 계산기 서버에 연결하여 다양한 수학 연산을 수행합니다.

## 사전 준비 사항

이 클라이언트를 실행하기 전에 다음을 준비해야 합니다:

1. 1장의 계산기 서버를 **시작**합니다:
   - 계산기 서버 디렉터리로 이동: `03-GettingStarted/01-first-server/solution/java/`
   - 계산기 서버를 빌드하고 실행합니다:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - 서버는 `http://localhost:8080`에서 실행 중이어야 합니다

2. 시스템에 **Java 21 이상**이 설치되어 있어야 합니다
3. **Maven** (Maven Wrapper를 통해 포함됨)

## SDKClient란?

`SDKClient`는 다음을 보여주는 Java 애플리케이션입니다:
- Server-Sent Events(SSE) 전송을 사용해 MCP 서버에 연결하는 방법
- 서버에서 사용 가능한 도구 목록을 가져오는 방법
- 원격으로 다양한 계산기 함수를 호출하는 방법
- 응답을 처리하고 결과를 표시하는 방법

## 작동 방식

클라이언트는 Spring AI MCP 프레임워크를 사용하여:

1. **연결 설정**: WebFlux SSE 클라이언트 전송을 생성해 계산기 서버에 연결
2. **클라이언트 초기화**: MCP 클라이언트를 설정하고 연결을 확립
3. **도구 검색**: 사용 가능한 모든 계산기 연산 목록 조회
4. **연산 실행**: 샘플 데이터를 사용해 다양한 수학 함수 호출
5. **결과 표시**: 각 계산 결과를 화면에 출력

## 프로젝트 구조

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## 주요 의존성

프로젝트는 다음 주요 의존성을 사용합니다:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

이 의존성은 다음을 제공합니다:
- `McpClient` - 주요 클라이언트 인터페이스
- `WebFluxSseClientTransport` - 웹 기반 통신을 위한 SSE 전송
- MCP 프로토콜 스키마 및 요청/응답 타입

## 프로젝트 빌드

Maven Wrapper를 사용해 프로젝트를 빌드합니다:

```cmd
.\mvnw clean install
```

## 클라이언트 실행

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**참고**: 명령어를 실행하기 전에 계산기 서버가 `http://localhost:8080`에서 실행 중인지 확인하세요.

## 클라이언트 동작 내용

클라이언트를 실행하면 다음 작업을 수행합니다:

1. `http://localhost:8080`의 계산기 서버에 **연결**
2. **도구 목록 조회** - 사용 가능한 모든 계산기 연산 표시
3. **계산 수행**:
   - 덧셈: 5 + 3 = 8
   - 뺄셈: 10 - 4 = 6
   - 곱셈: 6 × 7 = 42
   - 나눗셈: 20 ÷ 4 = 5
   - 거듭제곱: 2^8 = 256
   - 제곱근: √16 = 4
   - 절댓값: |-5.5| = 5.5
   - 도움말: 사용 가능한 연산 표시

## 예상 출력

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**참고**: 실행 종료 시 Maven에서 남아있는 스레드에 대한 경고가 나타날 수 있는데, 이는 리액티브 애플리케이션에서 정상적인 현상이며 오류가 아닙니다.

## 코드 이해하기

### 1. 전송 설정
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
계산기 서버에 연결하는 SSE(Server-Sent Events) 전송을 생성합니다.

### 2. 클라이언트 생성
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
동기식 MCP 클라이언트를 생성하고 연결을 초기화합니다.

### 3. 도구 호출
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
매개변수 a=5.0, b=3.0으로 "add" 도구를 호출합니다.

## 문제 해결

### 서버가 실행 중이지 않을 때
연결 오류가 발생하면 1장의 계산기 서버가 실행 중인지 확인하세요:
```
Error: Connection refused
```
**해결 방법**: 먼저 계산기 서버를 시작하세요.

### 포트가 이미 사용 중일 때
포트 8080이 사용 중이라면:
```
Error: Address already in use
```
**해결 방법**: 포트 8080을 사용하는 다른 애플리케이션을 종료하거나 서버가 다른 포트를 사용하도록 변경하세요.

### 빌드 오류 발생 시
빌드 오류가 발생하면:
```cmd
.\mvnw clean install -DskipTests
```

## 더 알아보기

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.