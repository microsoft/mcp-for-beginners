# AGENTS.md

## 프로젝트 개요

**MCP for Beginners**는 AI 모델과 클라이언트 애플리케이션 간의 상호작용을 위한 표준화된 프레임워크인 Model Context Protocol (MCP)을 배우기 위한 오픈소스 교육 커리큘럼입니다. 이 저장소는 여러 프로그래밍 언어로 실습 코드 예제를 포함한 포괄적인 학습 자료를 제공합니다.

### 주요 기술

- **프로그래밍 언어**: C#, Java, JavaScript, TypeScript, Python, Rust
- **프레임워크 및 SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **데이터베이스**: PostgreSQL 및 pgvector 확장
- **클라우드 플랫폼**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **빌드 도구**: npm, Maven, pip, Cargo
- **문서화**: 자동 다국어 번역이 포함된 Markdown (48개 이상의 언어 지원)

### 아키텍처

- **11개의 핵심 모듈 (00-11)**: 기초부터 고급 주제까지 순차적인 학습 경로
- **실습 랩**: 여러 언어로 완전한 솔루션 코드를 포함한 실습 과제
- **샘플 프로젝트**: MCP 서버 및 클라이언트 구현 예제
- **번역 시스템**: 다국어 지원을 위한 자동화된 GitHub Actions 워크플로우
- **이미지 자산**: 번역된 버전을 포함한 중앙 집중식 이미지 디렉토리

## 설정 명령

이 저장소는 문서 중심입니다. 대부분의 설정은 개별 샘플 프로젝트와 랩 내에서 이루어집니다.

### 저장소 설정

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### 샘플 프로젝트 작업

샘플 프로젝트는 다음 위치에 있습니다:
- `03-GettingStarted/samples/` - 언어별 예제
- `03-GettingStarted/01-first-server/solution/` - 첫 번째 서버 구현
- `03-GettingStarted/02-client/solution/` - 클라이언트 구현
- `11-MCPServerHandsOnLabs/` - 포괄적인 데이터베이스 통합 랩

각 샘플 프로젝트는 자체 설정 지침을 포함합니다:

#### TypeScript/JavaScript 프로젝트
```bash
cd <project-directory>
npm install
npm start
```

#### Python 프로젝트
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java 프로젝트
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## 개발 워크플로우

### 문서 구조

- **모듈 00-11**: 순차적인 핵심 커리큘럼 콘텐츠
- **translations/**: 언어별 버전 (자동 생성, 직접 편집 금지)
- **translated_images/**: 지역화된 이미지 버전 (자동 생성)
- **images/**: 원본 이미지 및 다이어그램

### 문서 변경 작업

1. 루트 모듈 디렉토리(00-11)의 영어 Markdown 파일만 편집
2. 필요한 경우 `images/` 디렉토리에서 이미지를 업데이트
3. co-op-translator GitHub Action이 번역을 자동으로 생성
4. 번역은 메인 브랜치로 푸시 시 재생성됨

### 번역 작업

- **자동 번역**: GitHub Actions 워크플로우가 모든 번역을 처리
- **직접 편집 금지**: `translations/` 디렉토리 내 파일
- 번역 메타데이터는 각 번역 파일에 포함됨
- 지원 언어: 아랍어, 중국어, 프랑스어, 독일어, 힌디어, 일본어, 한국어, 포르투갈어, 러시아어, 스페인어 등 48개 이상의 언어

## 테스트 지침

### 문서 검증

이 저장소는 주로 문서 중심이므로 테스트는 다음에 중점을 둡니다:

1. **링크 검증**: 모든 내부 링크가 작동하는지 확인
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **코드 샘플 검증**: 코드 예제가 컴파일/실행되는지 테스트
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown 린팅**: 형식 일관성 확인
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### 샘플 프로젝트 테스트

각 언어별 샘플은 자체 테스트 접근 방식을 포함합니다:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## 코드 스타일 가이드라인

### 문서 스타일

- 명확하고 초보자 친화적인 언어 사용
- 가능한 경우 여러 언어로 코드 예제 포함
- Markdown 모범 사례 준수:
  - ATX 스타일 헤더 사용 (`#` 문법)
  - 언어 식별자를 포함한 fenced 코드 블록 사용
  - 이미지에 설명적인 alt 텍스트 포함
  - 합리적인 줄 길이 유지 (엄격한 제한은 없지만 상식적으로)

### 코드 샘플 스타일

#### TypeScript/JavaScript
- ES 모듈 사용 (`import`/`export`)
- TypeScript 엄격 모드 규칙 준수
- 타입 주석 포함
- ES2022 대상

#### Python
- PEP 8 스타일 가이드라인 준수
- 적절한 경우 타입 힌트 사용
- 함수 및 클래스에 docstring 포함
- 최신 Python 기능 사용 (3.8+)

#### Java
- Spring Boot 규칙 준수
- Java 21 기능 사용
- 표준 Maven 프로젝트 구조 준수
- Javadoc 주석 포함

### 파일 구성

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## 빌드 및 배포

### 문서 배포

이 저장소는 GitHub Pages 또는 유사한 플랫폼을 사용하여 문서를 호스팅합니다(적용 가능한 경우). 메인 브랜치로 변경 사항이 푸시되면 다음이 트리거됩니다:

1. 번역 워크플로우 (`.github/workflows/co-op-translator.yml`)
2. 모든 영어 Markdown 파일의 자동 번역
3. 필요한 경우 이미지 지역화

### 빌드 프로세스 불필요

이 저장소는 주로 Markdown 문서를 포함합니다. 핵심 커리큘럼 콘텐츠에 대해 컴파일 또는 빌드 단계가 필요하지 않습니다.

### 샘플 프로젝트 배포

개별 샘플 프로젝트는 배포 지침을 포함할 수 있습니다:
- MCP 서버 배포 지침은 `03-GettingStarted/09-deployment/`에서 확인
- Azure Container Apps 배포 예제는 `11-MCPServerHandsOnLabs/`에서 확인

## 기여 가이드라인

### Pull Request 프로세스

1. **Fork 및 Clone**: 저장소를 Fork하고 로컬에 Clone
2. **브랜치 생성**: 설명이 포함된 브랜치 이름 사용 (예: `fix/typo-module-3`, `add/python-example`)
3. **변경 작업**: 영어 Markdown 파일만 편집 (번역 파일은 제외)
4. **로컬 테스트**: Markdown이 올바르게 렌더링되는지 확인
5. **PR 제출**: 명확한 PR 제목과 설명 사용
6. **CLA**: Microsoft Contributor License Agreement 서명 필요

### PR 제목 형식

명확하고 설명적인 제목 사용:
- `[Module XX] 간단한 설명` - 모듈별 변경 사항
- `[Samples] 설명` - 샘플 코드 변경 사항
- `[Docs] 설명` - 일반 문서 업데이트

### 기여할 내용

- 문서 또는 코드 샘플의 버그 수정
- 추가 언어로 새로운 코드 예제
- 기존 콘텐츠의 명확화 및 개선
- 새로운 사례 연구 또는 실용적인 예제
- 불명확하거나 잘못된 콘텐츠에 대한 문제 보고

### 하지 말아야 할 일

- `translations/` 디렉토리 내 파일 직접 편집 금지
- `translated_images/` 디렉토리 편집 금지
- 논의 없이 대형 바이너리 파일 추가 금지
- 번역 워크플로우 파일 변경 금지 (조율 필요)

## 추가 참고 사항

### 저장소 유지 관리

- **변경 로그**: 모든 주요 변경 사항은 `changelog.md`에 기록
- **학습 가이드**: 커리큘럼 탐색 개요는 `study_guide.md` 사용
- **이슈 템플릿**: 버그 보고 및 기능 요청은 GitHub 이슈 템플릿 사용
- **행동 강령**: 모든 기여자는 Microsoft 오픈소스 행동 강령을 준수해야 함

### 학습 경로

최적의 학습을 위해 모듈을 순차적으로 따라가기:
1. **00-02**: 기초 (소개, 핵심 개념, 보안)
2. **03**: 실습 구현 시작
3. **04-05**: 실용적 구현 및 고급 주제
4. **06-10**: 커뮤니티, 모범 사례 및 실제 응용
5. **11**: 포괄적인 데이터베이스 통합 랩 (13개의 순차적 랩)

### 지원 리소스

- **문서**: https://modelcontextprotocol.io/
- **명세서**: https://spec.modelcontextprotocol.io/
- **커뮤니티**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord 서버
- **관련 과정**: README.md에서 다른 Microsoft 학습 경로 확인

### 일반적인 문제 해결

**Q: PR이 번역 검사에서 실패합니다**
A: 루트 모듈 디렉토리의 영어 Markdown 파일만 편집했는지 확인하세요. 번역된 버전은 편집하지 마세요.

**Q: 새로운 언어를 추가하려면 어떻게 해야 하나요?**
A: 언어 지원은 co-op-translator 워크플로우를 통해 관리됩니다. 새로운 언어 추가를 논의하려면 이슈를 열어주세요.

**Q: 코드 샘플이 작동하지 않습니다**
A: 특정 샘플의 README에 있는 설정 지침을 따랐는지 확인하세요. 올바른 버전의 종속성이 설치되었는지 확인하세요.

**Q: 이미지가 표시되지 않습니다**
A: 이미지 경로가 상대적이고 슬래시를 사용했는지 확인하세요. 이미지는 `images/` 디렉토리 또는 지역화된 버전은 `translated_images/`에 있어야 합니다.

### 성능 고려 사항

- 번역 워크플로우는 완료까지 몇 분이 걸릴 수 있음
- 대형 이미지는 커밋 전에 최적화 필요
- 개별 Markdown 파일은 집중적이고 적절한 크기를 유지
- 더 나은 이동성을 위해 상대 링크 사용

### 프로젝트 관리

이 프로젝트는 Microsoft 오픈소스 관행을 따릅니다:
- 코드 및 문서에 대한 MIT 라이선스
- Microsoft 오픈소스 행동 강령
- 기여를 위한 CLA 필요
- 보안 문제: SECURITY.md 지침 준수
- 지원: SUPPORT.md에서 도움 리소스 확인

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.