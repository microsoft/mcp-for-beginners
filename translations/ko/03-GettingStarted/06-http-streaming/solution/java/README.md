# Calculator HTTP Streaming Demo

이 프로젝트는 Spring Boot WebFlux를 사용하여 Server-Sent Events(SSE)를 통한 HTTP 스트리밍을 보여줍니다. 두 개의 애플리케이션으로 구성되어 있습니다:

- **Calculator Server**: 계산을 수행하고 SSE를 통해 결과를 스트리밍하는 리액티브 웹 서비스
- **Calculator Client**: 스트리밍 엔드포인트를 소비하는 클라이언트 애플리케이션

## Prerequisites

- Java 17 이상
- Maven 3.6 이상

## Project Structure

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## How It Works

1. **Calculator Server**는 `/calculate` 엔드포인트를 제공합니다:
   - 쿼리 파라미터: `a` (숫자), `b` (숫자), `op` (연산)
   - 지원하는 연산: `add`, `sub`, `mul`, `div`
   - 계산 진행 상황과 결과를 Server-Sent Events로 반환

2. **Calculator Client**는 서버에 연결하여:
   - `7 * 5` 계산 요청을 보냄
   - 스트리밍 응답을 소비
   - 각 이벤트를 콘솔에 출력

## Running the Applications

### Option 1: Using Maven (Recommended)

#### 1. Calculator Server 시작하기

터미널을 열고 서버 디렉터리로 이동:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

서버는 `http://localhost:8080`에서 시작됩니다.

다음과 같은 출력이 보일 것입니다:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Calculator Client 실행하기

**새 터미널**을 열고 클라이언트 디렉터리로 이동:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

클라이언트가 서버에 연결하여 계산을 수행하고 스트리밍 결과를 표시합니다.

### Option 2: Using Java directly

#### 1. 서버 컴파일 및 실행:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. 클라이언트 컴파일 및 실행:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Testing the Server Manually

웹 브라우저나 curl을 사용하여 서버를 테스트할 수도 있습니다:

### 웹 브라우저 사용:
다음 주소 방문: `http://localhost:8080/calculate?a=10&b=5&op=add`

### curl 사용:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Expected Output

클라이언트를 실행하면 다음과 유사한 스트리밍 출력이 나타납니다:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Supported Operations

- `add` - 덧셈 (a + b)
- `sub` - 뺄셈 (a - b)
- `mul` - 곱셈 (a * b)
- `div` - 나눗셈 (a / b, b가 0일 경우 NaN 반환)

## API Reference

### GET /calculate

**파라미터:**
- `a` (필수): 첫 번째 숫자 (double)
- `b` (필수): 두 번째 숫자 (double)
- `op` (필수): 연산 (`add`, `sub`, `mul`, `div`)

**응답:**
- Content-Type: `text/event-stream`
- 계산 진행 상황과 결과를 Server-Sent Events로 반환

**요청 예시:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**응답 예시:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Troubleshooting

### Common Issues

1. **포트 8080이 이미 사용 중인 경우**
   - 포트 8080을 사용하는 다른 애플리케이션을 종료하세요
   - 또는 `calculator-server/src/main/resources/application.yml`에서 서버 포트를 변경하세요

2. **연결 거부 오류**
   - 클라이언트를 시작하기 전에 서버가 실행 중인지 확인하세요
   - 서버가 포트 8080에서 정상적으로 시작되었는지 확인하세요

3. **파라미터 이름 문제**
   - 이 프로젝트는 `-parameters` 플래그가 포함된 Maven 컴파일러 설정을 사용합니다
   - 파라미터 바인딩 문제 발생 시, 해당 설정으로 프로젝트가 빌드되었는지 확인하세요

### 애플리케이션 종료 방법

- 각 애플리케이션이 실행 중인 터미널에서 `Ctrl+C`를 누르세요
- 또는 백그라운드 프로세스로 실행 중일 경우 `mvn spring-boot:stop` 명령을 사용하세요

## Technology Stack

- **Spring Boot 3.3.1** - 애플리케이션 프레임워크
- **Spring WebFlux** - 리액티브 웹 프레임워크
- **Project Reactor** - 리액티브 스트림 라이브러리
- **Netty** - 논블로킹 I/O 서버
- **Maven** - 빌드 도구
- **Java 17+** - 프로그래밍 언어

## Next Steps

코드를 수정해 보세요:
- 더 많은 수학 연산 추가
- 잘못된 연산에 대한 에러 처리 포함
- 요청/응답 로깅 추가
- 인증 기능 구현
- 단위 테스트 추가

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.