# 계산기 LLM 클라이언트

> [!NOTE]
> 이 솔루션은 강의의 레거시 HTTP+SSE 계산기 서비스에 연결되며 
> MCP `2025-11-25` SDK API를 대상으로 합니다. 이는 `2026-07-28` 스트리머블 HTTP
> 예제가 아닙니다.

LangChain4j를 사용하여 MiniMax OpenAI 호환 API를 통해 MCP(모델 컨텍스트 프로토콜) 계산기 서비스에 연결하는 방법을 시연하는 자바 응용 프로그램입니다.

## 필수 조건

- Java 21 이상
- Maven 3.6+ (또는 포함된 Maven 래퍼 사용)
- MiniMax API 키
- `http://localhost:8080`에서 실행 중인 MCP 계산기 서비스

## API 키 받기

이 응용 프로그램은 MiniMax OpenAI 호환 API를 사용합니다. 키와 엔드포인트를 얻으려면 다음 단계를 따르세요:

### 1. 엔드포인트 선택
1. 글로벌 엔드포인트로는 `https://api.minimax.io/v1` 사용
2. 중국 엔드포인트로는 `https://api.minimaxi.com/v1` 사용

### 2. API 키 생성
1. MiniMax 계정에서 MiniMax API 키 생성
2. 키를 안전한 곳에 보관

### 3. 환경 변수 설정

#### Windows (명령 프롬프트)에서:
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windows (PowerShell)에서:
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux에서:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## 설정 및 설치

1. **프로젝트 디렉터리 클론하거나 이동**

2. **종속성 설치**:
   ```cmd
   mvnw clean install
   ```
   또는 Maven이 전역에 설치되어 있다면:
   ```cmd
   mvn clean install
   ```

3. **환경 변수 설정** ("API 키 받기" 섹션 참고)

4. **MCP 계산기 서비스 시작**:
   1장의 MCP 계산기 서비스가 `http://localhost:8080/sse`에서 실행 중인지 확인하세요. 클라이언트를 시작하기 전에 실행 중이어야 합니다.

## 애플리케이션 실행

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 애플리케이션이 수행하는 작업

애플리케이션은 계산기 서비스와 세 가지 주요 상호작용을 시연합니다:

1. <strong>덧셈</strong>: 24.5와 17.3의 합 계산
2. <strong>제곱근</strong>: 144의 제곱근 계산
3. <strong>도움말</strong>: 사용 가능한 계산기 함수 표시

## 예상 출력

성공적으로 실행되면 다음과 유사한 출력을 볼 수 있습니다:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 문제 해결

### 일반적인 문제

1. **"OPENAI_API_KEY 환경 변수가 설정되지 않음"**
   - `OPENAI_API_KEY` 환경 변수가 설정되었는지 확인하세요
   - 변수 설정 후 터미널/명령 프롬프트를 재시작하세요

2. **"localhost:8080에 연결 거부됨"**
   - MCP 계산기 서비스가 포트 8080에서 실행 중인지 확인하세요
   - 다른 서비스가 포트 8080을 사용 중인지 확인하세요

3. **"인증 실패"**
   - API 키가 유효한지 확인하세요
   - `OPENAI_BASE_URL`이 사용하려는 엔드포인트와 일치하는지 확인하세요

4. **Maven 빌드 오류**
   - Java 21 이상을 사용 중인지 확인하세요: `java -version`
   - 빌드를 깨끗하게 해보세요: `mvnw clean`

### 디버깅

디버그 로깅을 활성화하려면 실행 시 다음 JVM 인수를 추가하세요:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 구성

애플리케이션은 다음과 같이 구성됩니다:
- 기본적으로 MiniMax-M3 사용; `MINIMAX_MODEL_ID`를 설정하여 `MiniMax-M3` 또는 `MiniMax-M2.7` 선택 가능
- `OPENAI_BASE_URL`이 설정된 경우 해당 URL에 연결; 그렇지 않으면 `MINIMAX_REGION=cn_zh`일 때는 `https://api.minimaxi.com/v1`, 기본적으로는 `https://api.minimax.io/v1` 사용
- MCP 서비스는 `http://localhost:8080/sse`에 연결
- 요청에 60초 제한 시간 사용

## 종속성

이 프로젝트에서 사용하는 주요 종속성:
- **LangChain4j**: AI 통합 및 도구 관리용
- **LangChain4j MCP**: 모델 컨텍스트 프로토콜 지원용
- **LangChain4j OpenAI 공식**: MiniMax OpenAI 호환 API 통합용
- **Spring Boot**: 애플리케이션 프레임워크 및 의존성 주입용

## 라이선스

이 프로젝트는 Apache License 2.0 라이선스 하에 있습니다 - 자세한 내용은 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 파일을 참조하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->