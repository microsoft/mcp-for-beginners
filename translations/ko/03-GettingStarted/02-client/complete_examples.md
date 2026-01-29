# 완전한 MCP 클라이언트 예제

이 디렉토리에는 다양한 프로그래밍 언어로 작성된 MCP 클라이언트의 완전하고 작동 가능한 예제가 포함되어 있습니다. 각 클라이언트는 메인 README.md 튜토리얼에서 설명된 모든 기능을 보여줍니다.

## 사용 가능한 클라이언트

### 1. Java 클라이언트 (`client_example_java.java`)

- **전송 방식**: HTTP를 통한 SSE (서버 전송 이벤트)
- **대상 서버**: `http://localhost:8080`
- **기능**:
  - 연결 설정 및 핑
  - 도구 목록 조회
  - 계산기 작업 (더하기, 빼기, 곱하기, 나누기, 도움말)
  - 오류 처리 및 결과 추출

**실행 방법:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# 클라이언트 (`client_example_csharp.cs`)

- **전송 방식**: Stdio (표준 입력/출력)
- **대상 서버**: dotnet run을 통해 실행되는 로컬 .NET MCP 서버
- **기능**:
  - Stdio 전송을 통한 자동 서버 시작
  - 도구 및 리소스 목록 조회
  - 계산기 작업
  - JSON 결과 파싱
  - 포괄적인 오류 처리

**실행 방법:**

```bash
dotnet run
```

### 3. TypeScript 클라이언트 (`client_example_typescript.ts`)

- **전송 방식**: Stdio (표준 입력/출력)
- **대상 서버**: 로컬 Node.js MCP 서버
- **기능**:
  - MCP 프로토콜 완전 지원
  - 도구, 리소스 및 프롬프트 작업
  - 계산기 작업
  - 리소스 읽기 및 프롬프트 실행
  - 강력한 오류 처리

**실행 방법:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python 클라이언트 (`client_example_python.py`)

- **전송 방식**: Stdio (표준 입력/출력)  
- **대상 서버**: 로컬 Python MCP 서버
- **기능**:
  - 작업을 위한 Async/await 패턴
  - 도구 및 리소스 검색
  - 계산기 작업 테스트
  - 리소스 내용 읽기
  - 클래스 기반 구성

**실행 방법:**

```bash
python client_example_python.py
```

## 모든 클라이언트의 공통 기능

각 클라이언트 구현은 다음을 보여줍니다:

1. **연결 관리**
   - MCP 서버에 연결 설정
   - 연결 오류 처리
   - 적절한 정리 및 리소스 관리

2. **서버 검색**
   - 사용 가능한 도구 목록 조회
   - 사용 가능한 리소스 목록 조회 (지원되는 경우)
   - 사용 가능한 프롬프트 목록 조회 (지원되는 경우)

3. **도구 호출**
   - 기본 계산기 작업 (더하기, 빼기, 곱하기, 나누기)
   - 서버 정보를 위한 도움말 명령
   - 적절한 인수 전달 및 결과 처리

4. **오류 처리**
   - 연결 오류
   - 도구 실행 오류
   - 우아한 실패 및 사용자 피드백

5. **결과 처리**
   - 응답에서 텍스트 콘텐츠 추출
   - 가독성을 위한 출력 형식화
   - 다양한 응답 형식 처리

## 사전 준비 사항

이 클라이언트를 실행하기 전에 다음을 확인하세요:

1. **해당 MCP 서버 실행 중** (`../01-first-server/`에서 제공)
2. **선택한 언어에 필요한 종속성 설치**
3. **적절한 네트워크 연결** (HTTP 기반 전송의 경우)

## 구현 간 주요 차이점

| 언어       | 전송 방식 | 서버 시작 방식 | 비동기 모델 | 주요 라이브러리       |
|------------|-----------|----------------|-------------|---------------------|
| Java       | SSE/HTTP  | 외부           | 동기        | WebFlux, MCP SDK    |
| C#         | Stdio     | 자동           | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | 자동           | Async/Await | Node MCP SDK        |
| Python     | Stdio     | 자동           | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | 자동           | Async/Await | Rust MCP SDK, Tokio |

## 다음 단계

이 클라이언트 예제를 탐색한 후:

1. **클라이언트를 수정하여** 새로운 기능이나 작업 추가
2. **자신만의 서버를 생성하여** 이 클라이언트로 테스트
3. **다양한 전송 방식 실험** (SSE vs. Stdio)
4. **MCP 기능을 통합한 더 복잡한 애플리케이션 구축**

## 문제 해결

### 일반적인 문제

1. **연결 거부됨**: MCP 서버가 예상 포트/경로에서 실행 중인지 확인
2. **모듈을 찾을 수 없음**: 선택한 언어에 필요한 MCP SDK 설치
3. **권한 거부됨**: Stdio 전송을 위한 파일 권한 확인
4. **도구를 찾을 수 없음**: 서버가 예상 도구를 구현했는지 확인

### 디버그 팁

1. **MCP SDK에서 상세 로깅 활성화**
2. **서버 로그 확인**하여 오류 메시지 탐색
3. **클라이언트와 서버 간 도구 이름 및 서명 확인**
4. **MCP Inspector로 먼저 테스트**하여 서버 기능 검증

## 관련 문서

- [메인 클라이언트 튜토리얼](./README.md)
- [MCP 서버 예제](../../../../03-GettingStarted/01-first-server)
- [LLM 통합과 함께하는 MCP](../../../../03-GettingStarted/03-llm-client)
- [공식 MCP 문서](https://modelcontextprotocol.io/)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.