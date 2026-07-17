# AGENTS.md

## 프로젝트 개요

<strong>초보자를 위한 MCP</strong>는 AI 모델과 클라이언트 애플리케이션 간의 상호작용을 위한 표준화된 프레임워크인 Model Context Protocol(MCP)을 학습하기 위한 오픈소스 교육 커리큘럼입니다. 이 저장소는 여러 프로그래밍 언어에서 실습 코드 예제를 포함한 종합적인 학습 자료를 제공합니다.

### 핵심 기술

- **프로그래밍 언어**: C#, Java, JavaScript, TypeScript, Python, Rust
- **프레임워크 및 SDK**:
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- <strong>데이터베이스</strong>: pgvector 확장 기능이 포함된 PostgreSQL
- **클라우드 플랫폼**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **빌드 도구**: npm, Maven, pip, Cargo
- <strong>문서화</strong>: 자동 다국어 번역이 지원되는 Markdown (48개 이상 언어)

### 아키텍처

- **11개 핵심 모듈 (00-11)**: 기초부터 고급 주제까지 순차적 학습 경로
- **실습 실험실**: 여러 언어로 완성된 솔루션 코드가 포함된 실용적 연습
- **샘플 프로젝트**: 동작하는 MCP 서버 및 클라이언트 구현
- **번역 시스템**: 다국어 지원을 위한 자동 GitHub Actions 워크플로우
- **이미지 자산**: 번역된 버전이 포함된 중앙 이미지 디렉토리

## 설정 명령어

이 저장소는 문서 중심입니다. 대부분의 설정은 개별 샘플 프로젝트와 실험실 내에서 발생합니다.

### 저장소 설정

```bash
# 저장소를 복제하세요
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### 샘플 프로젝트 작업하기

샘플 프로젝트 위치:
- `03-GettingStarted/samples/` - 언어별 예제
- `03-GettingStarted/01-first-server/solution/` - 첫 번째 서버 구현
- `03-GettingStarted/02-client/solution/` - 클라이언트 구현
- `11-MCPServerHandsOnLabs/` - 종합 데이터베이스 통합 실습실

각 샘플 프로젝트에는 자체 설정 지침이 포함되어 있습니다:

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
# 또는
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

### MCP 7-28 준비사항

#### 저장소 준비 체크리스트

- [x] **신규 기여자 이해도**: 이 파일은 저장소 목적,
  구조, 기여 규칙, 샘플 설정 경로를 정의합니다.
- [x] **정확한 플래그가 포함된 빌드/테스트/린트 명령어**:
  - 저장소 문서 린트:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - 저장소 문서 링크 패턴 감사:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript 샘플 검증:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python 샘플 검증:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java 샘플 검증:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **MCP 도구가 될 수 있는 하나의 현실적인 워크플로우**:
  `validate_curriculum_change`
- [x] **입력/출력이 명확함** (아래 명세 참조).
- [x] **권한 및 실패 모드 문서화됨** (아래 명세 참조).
- [x] **CI 테스트 가능성 명확함** (결정적 명령, 명확한
  종료 코드, 기계가 읽을 수 있는 출력).

#### 후보 MCP 도구 워크플로우: `validate_curriculum_change`

##### 목표

병합 전 커리큘럼 문서 변경사항과 대표 샘플 코드의 
건전성을 검증합니다.

##### 입력값

- `changed_paths: string[]` (필수) - PR에서 변경된 상대 경로.
- `run_docs_lint: boolean` (기본값 `true`)
- `run_links_audit: boolean` (기본값 `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (기본값 모두 `false`)

##### 출력값

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### 권한

- 작업공간 파일 읽기 및 도구 생성 산출물 기록만 허용 (예: 린트
  보고서, 테스트 로그); `translations/` 또는
  `translated_images/`에 대한 기록 금지.
- 로컬 셸 명령 실행 허용.
- 패키지 복원(`npm ci`,
  `python -m pip install`, `mvn` 의존성 해결) 용 네트워크 접근은 선택적 허용.
- `translations/` 또는
  `translated_images/`에 푸시, 병합, 수정 권한 없음.

##### 실패 모드

- `E_NO_INPUT_PATHS`: `changed_paths`가 비어 있음.
- `E_INVALID_PATH`: 입력 경로가 저장소 루트를 벗어남.
- `E_LINT_FAILED`: 마크다운 린트가 0이 아닌 코드로 종료됨.
- `E_LINK_AUDIT_FAILED`: 링크 감사 명령이 0이 아닌 코드로 종료됨.
- `E_SAMPLE_TEST_FAILED`: 샘플 테스트/빌드가 0이 아닌 코드로 종료됨.
- `E_TIMEOUT`: 명령이 설정된 시간 초과함.

##### 권장 CI 계약

자동 검증을 위해 다음을 설정한 CI 작업을 구성합니다:

- `*.md`, 샘플 코드, 또는 이 파일을 포함하는 PR 발생 시 트리거됨.
- 위에 나열된 명령어를 정확히 실행함.
- 로그를 산출물로 보존함.
- 종료 코드가 0이 아닐 경우 작업 실패 처리함.

#### 이 저장소에서 MCP 서버를 배포하는 경우

- [ ] MCP 7-28 초안 변경 로그를 읽어보십시오:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] SDK 베타 버전을 사용하여 서버를 실행해 보십시오:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] 세션 및 핸드셰이크 가정을 제거하고, 각 요청을
  독립적으로 처리하십시오:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] 원시 HTTP 요청에 대해 `Mcp-Method` 및 `Mcp-Name` 헤더를 전송하십시오:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] 하드코딩된 오류 코드 감사를 수행하십시오 (`missing resource` 가 `-32002`에서 `-32602`로 이동).

- [ ] 더 이상 사용하지 않는 루트, 샘플링 및 로깅에 대해 마이그레이션 플래그 및 계획 설정:
  
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] 실험적인 `2025-11-25` Tasks API 마이그레이션:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] OAuth 및 OpenID Connect 보안 강화에 대한 권한 검토:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### 문서 구조

- **Modules 00-11**: 핵심 교육 내용의 순차적 구성
- **translations/**: 언어별 버전 (자동 생성, 직접 수정 금지)
- **translated_images/**: 지역화된 이미지 버전 (자동 생성)
- **images/**: 원본 이미지 및 도표

### 문서 변경 방법

1. 루트 모듈 디렉터리(00-11) 내 영어 마크다운 파일만 편집
2. 필요한 경우 `images/` 디렉터리 내 이미지 업데이트
3. co-op-translator GitHub 액션이 자동으로 번역 생성
4. 메인 브랜치에 푸시 시 번역 다시 생성

### 번역 작업

- **자동 번역**: GitHub Actions 워크플로가 모든 번역 처리
- `translations/` 디렉터리 내 파일을 수동으로 편집하지 마세요
- 번역 메타데이터가 각 번역 파일에 포함되어 있음
- 지원 언어: 아랍어, 중국어, 프랑스어, 독일어, 힌디어, 일본어, 한국어, 포르투갈어, 러시아어, 스페인어 등 48개 이상

## 테스트 지침

### 문서 검증

이 저장소는 주로 문서 저장소이므로 테스트는 다음에 집중:

1. **링크 패턴 검사**: 검토를 위한 마크다운 링크 목록 작성

   ```bash
   # 마크다운 링크 목록 (패턴 감사)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **코드 샘플 검증**: 코드 예제가 컴파일/실행되는지 테스트

   ```bash
   # 특정 샘플로 이동하여 해당 테스트를 실행합니다
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **마크다운 린팅**: 서식 일관성 검사

   ```bash
   # 필요하면 markdownlint를 사용하세요
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### 샘플 프로젝트 테스트

각 언어별 샘플은 고유한 테스트 방식을 포함:

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
- 가능한 경우 여러 언어로 된 코드 예시 포함
- 마크다운 모범 사례 준수:
  - ATX 스타일 헤더(`#` 구문) 사용
  - 언어 지정자가 포함된 펜스 코드 블록 사용
  - 이미지에는 설명적인 대체 텍스트 포함
  - 줄 길이 적절하게 유지 (엄격하지는 않으나 합리적으로)

### 코드 샘플 스타일

#### TypeScript/JavaScript
- ES 모듈(`import`/`export`) 사용
- TypeScript 엄격 모드 관례 준수
- 타입 주석 포함
- ES2022 대상

#### Python
- PEP 8 스타일 가이드라인 준수
- 적절한 곳에 타입 힌트 사용
- 함수 및 클래스에 docstring 포함
- 최신 Python 기능(3.8 이상) 사용

#### Java
- Spring Boot 관례 준수
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

저장소는 GitHub Pages 또는 유사한 도구를 사용해 문서를 호스팅합니다(적용 시). 메인 브랜치 변경 사항에 대해 다음이 실행됨:

1. 번역 워크플로(`.github/workflows/co-op-translator.yml`)
2. 모든 영어 마크다운 파일의 자동 번역
3. 필요한 경우 이미지 현지화

### 빌드 과정 불필요

이 저장소는 주로 마크다운 문서를 포함하므로 핵심 교육 내용에는 컴파일이나 빌드 단계가 필요 없음.

### 샘플 프로젝트 배포

개별 샘플 프로젝트는 배포 지침이 있을 수 있음:
- MCP 서버 배포 지침은 `03-GettingStarted/09-deployment/` 참고
- Azure Container Apps 배포 예시는 `11-MCPServerHandsOnLabs/` 참조

## 기여 지침

### 풀 리퀘스트 절차

1. **포크 및 클론**: 저장소를 포크하고 로컬에 클론
2. **브랜치 생성**: 설명적인 브랜치 이름 사용 (예: `fix/typo-module-3`, `add/python-example`)
3. **변경 사항 적용**: 영어 마크다운 파일만 편집 (번역본 제외)
4. **로컬 테스트**: 마크다운이 올바르게 렌더링되는지 확인
5. **PR 제출**: 명확한 제목과 설명 사용
6. **CLA**: 요청 시 Microsoft 기여자 라이선스 계약 서명

### PR 제목 형식

명확하고 설명적인 제목 사용:
- 모듈별 변경 사항에는 `[Module XX] 간략 설명`
- 샘플 코드 변경 사항에는 `[Samples] 설명`
- 일반 문서 업데이트에는 `[Docs] 설명`

### 기여 가능한 내용

- 문서나 코드 샘플의 버그 수정
- 추가 언어로 된 새로운 코드 예시
- 기존 내용에 대한 명확화 및 개선
- 새로운 사례 연구나 실습 예제
- 불명확하거나 잘못된 내용에 대한 이슈 보고

### 하지 말아야 할 것

- `translations/` 디렉터리 내 파일 직접 수정 금지
- `translated_images/` 디렉터리 편집 금지
- 사전 논의 없이 큰 바이너리 파일 추가 금지
- 협의 없이 번역 워크플로 파일 변경 금지

## 추가 참고사항

### 저장소 유지관리

- **변경 내역**: 주요 변경 사항은 `changelog.md`에 문서화
- **학습 가이드**: 커리큘럼 내비게이션 개요는 `study_guide.md` 참조
- **이슈 템플릿**: 버그 및 기능 요청용 GitHub 이슈 템플릿 사용
- **행동 강령**: 모든 기여자는 Microsoft 오픈 소스 행동 강령 준수 필수

### 학습 경로

최적 학습을 위해 모듈을 순차적으로(00-11) 따라가세요:
1. **00-02**: 기본 개념 (소개, 핵심 개념, 보안)
2. **03**: 실습 포함 시작하기
3. **04-05**: 실용 구현 및 고급 주제
4. **06-10**: 커뮤니티, 모범 사례, 실세계 적용
5. **11**: 포괄적 데이터베이스 통합 실습 (13개 순차 실습)

### 지원 리소스

- <strong>문서</strong>: https://modelcontextprotocol.io/
- <strong>명세서</strong>: https://spec.modelcontextprotocol.io/
- <strong>커뮤니티</strong>: https://github.com/orgs/modelcontextprotocol/discussions
- <strong>디스코드</strong>: Microsoft Foundry 디스코드 서버
- **관련 강좌**: 기타 Microsoft 학습 경로는 README.md 참조

### 일반 문제 해결

**Q: 제 PR이 번역 검사를 통과하지 못해요**
A: 루트 모듈 디렉터리 내 영어 마크다운 파일만 편집했는지, 번역 파일은 편집하지 않았는지 확인하세요.

**Q: 새로운 언어를 추가하려면 어떻게 하나요?**
A: 언어 지원은 co-op-translator 워크플로를 통해 관리됩니다. 새로운 언어 추가에 대해 논의하려면 이슈를 열어주세요.

**Q: 코드 샘플이 작동하지 않아요**

A: 특정 샘플의 README에 있는 설정 지침을 따라했는지 확인하세요. 올바른 버전의 종속 항목이 설치되어 있는지 확인하세요.

**Q: 이미지가 표시되지 않아요**
A: 이미지 경로가 상대 경로이고 슬래시(/)를 사용하는지 확인하세요. 이미지는 `images/` 디렉터리 또는 현지화된 버전의 경우 `translated_images/`에 있어야 합니다.

### 성능 고려 사항

- 번역 작업 흐름은 완료하는 데 몇 분이 걸릴 수 있습니다
- 큰 이미지는 커밋 전에 최적화해야 합니다
- 개별 마크다운 파일은 집중되고 적절한 크기로 유지하세요
- 더 나은 이식성을 위해 상대 링크를 사용하세요

### 프로젝트 거버넌스

이 프로젝트는 Microsoft 오픈 소스 관행을 따릅니다:
- 코드 및 문서는 MIT 라이선스 적용
- Microsoft 오픈 소스 행동 강령
- 기여 시 CLA 필요
- 보안 문제: SECURITY.md 지침 따르기
- 지원: 도움 리소스는 SUPPORT.md 참조

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->