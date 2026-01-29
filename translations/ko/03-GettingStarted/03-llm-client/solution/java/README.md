# Calculator LLM Client

LangChain4j를 사용해 MCP(Model Context Protocol) 계산기 서비스에 GitHub Models 통합으로 연결하는 방법을 보여주는 Java 애플리케이션입니다.

## 사전 준비 사항

- Java 21 이상
- Maven 3.6+ (또는 포함된 Maven 래퍼 사용)
- GitHub Models에 접근 권한이 있는 GitHub 계정
- `http://localhost:8080`에서 실행 중인 MCP 계산기 서비스

## GitHub 토큰 받기

이 애플리케이션은 GitHub Models를 사용하므로 GitHub 개인 액세스 토큰이 필요합니다. 토큰을 받으려면 다음 단계를 따르세요:

### 1. GitHub Models 접속
1. [GitHub Models](https://github.com/marketplace/models)로 이동
2. GitHub 계정으로 로그인
3. 아직 요청하지 않았다면 GitHub Models 접근 권한 요청

### 2. 개인 액세스 토큰 생성
1. [GitHub 설정 → 개발자 설정 → 개인 액세스 토큰 → 토큰(클래식)](https://github.com/settings/tokens)으로 이동
2. "새 토큰 생성" → "새 토큰 생성(클래식)" 클릭
3. 토큰에 설명이 잘 되는 이름 지정 (예: "MCP Calculator Client")
4. 필요에 따라 만료 기간 설정
5. 다음 권한 선택:
   - `repo` (비공개 저장소 접근 시)
   - `user:email`
6. "토큰 생성" 클릭
7. **중요**: 토큰은 한 번만 보여지므로 바로 복사하세요!

### 3. 환경 변수 설정

#### Windows (명령 프롬프트):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## 설치 및 설정

1. **프로젝트 디렉터리 복제 또는 이동**

2. **의존성 설치**:
   ```cmd
   mvnw clean install
   ```
   또는 Maven이 전역에 설치되어 있다면:
   ```cmd
   mvn clean install
   ```

3. **환경 변수 설정** ("GitHub 토큰 받기" 섹션 참고)

4. **MCP 계산기 서비스 시작**:
   1장의 MCP 계산기 서비스가 `http://localhost:8080/sse`에서 실행 중인지 확인하세요. 클라이언트를 시작하기 전에 서비스가 실행 중이어야 합니다.

## 애플리케이션 실행

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 애플리케이션 기능

이 애플리케이션은 계산기 서비스와 다음 세 가지 주요 상호작용을 보여줍니다:

1. **덧셈**: 24.5와 17.3의 합 계산
2. **제곱근**: 144의 제곱근 계산
3. **도움말**: 사용 가능한 계산기 함수 목록 표시

## 예상 출력

성공적으로 실행되면 다음과 유사한 출력이 나타납니다:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 문제 해결

### 자주 발생하는 문제

1. **"GITHUB_TOKEN 환경 변수가 설정되지 않음"**
   - `GITHUB_TOKEN` 환경 변수를 설정했는지 확인하세요
   - 변수 설정 후 터미널/명령 프롬프트를 재시작하세요

2. **"localhost:8080 연결 거부"**
   - MCP 계산기 서비스가 8080 포트에서 실행 중인지 확인
   - 다른 서비스가 8080 포트를 사용 중인지 확인

3. **"인증 실패"**
   - GitHub 토큰이 유효하고 권한이 올바른지 확인
   - GitHub Models 접근 권한이 있는지 확인

4. **Maven 빌드 오류**
   - Java 21 이상 사용 중인지 확인: `java -version`
   - 빌드 클린 시도: `mvnw clean`

### 디버깅

디버그 로깅을 활성화하려면 실행 시 다음 JVM 인자를 추가하세요:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 구성

애플리케이션 구성 내용:
- GitHub Models에서 `gpt-4.1-nano` 모델 사용
- MCP 서비스에 `http://localhost:8080/sse`로 연결
- 요청 타임아웃 60초 설정
- 디버깅을 위한 요청/응답 로깅 활성화

## 의존성

이 프로젝트에서 사용된 주요 의존성:
- **LangChain4j**: AI 통합 및 도구 관리
- **LangChain4j MCP**: Model Context Protocol 지원
- **LangChain4j GitHub Models**: GitHub Models 통합
- **Spring Boot**: 애플리케이션 프레임워크 및 의존성 주입

## 라이선스

이 프로젝트는 Apache License 2.0 하에 라이선스가 부여되어 있습니다. 자세한 내용은 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 파일을 참고하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.