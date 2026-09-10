# 변경 로그: MCP 초급 커리큘럼

이 문서는 Model Context Protocol (MCP) 초급 커리큘럼에 이루어진 모든 주요 변경 사항의 기록입니다. 변경 사항은 최신 변경이 먼저 오도록 역순으로 문서화되어 있습니다.

## 2026년 7월 29일

### 신규 모듈 08 동반 수업: 신뢰성 사이드카 및 안전한 재시도

실제 세계 효과를 생성하는 MCP 도구용 공급업체 중립 동반 수업이 추가되었으며,
최종 `2026-07-28` 명세와 일치합니다.

- <strong>신규</strong>: [신뢰성 사이드카 동반 수업][reliability-sidecar]
  하나의 지원 티켓 스토리, 두 개의 Mermaid 다이어그램, 그리고 재시도 결정
  흐름을 사용하여 안정적 운영 키, 원자적 중복 입장,
  조정, 증거, 그리고 Tasks 확장 경계를 설명합니다.
- <strong>신규</strong>: 표준 라이브러리 Python 및 SQLite 장애 주입 연습이 추가되어
  별도의 운영 및 티켓 저장소를 이용해 외부 효과가 커밋된 후
  응답의 손실을 보여줍니다. 6가지 결정적 테스트는 단순
  중복, 보호된 재시작 복구, 페이로드 충돌, 캐시된 결과,
  활성 청구 및 동시 중복 입장을 다룹니다.
- <strong>업데이트</strong>: 모듈 08은 이제 동반 수업 링크를 포함하고,
  최종 `2026-07-28` 상태 없는 요청 모델을 식별하며,
  OpenTelemetry 관측성과 더 이상 사용되지 않는 MCP 로깅 기능을 구분하고,
  일반 재시도 예제를 읽기 전용 작업으로 제한합니다.
- **선택 사항**: 수업은 휴대 가능한 개념을 하나의 태그된 커뮤니티
  구현에 매핑하지만, 호스팅 서비스나 네트워크 호출을
  연습의 일부로 포함하지 않습니다.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2026년 7월 2일

### 신규 수업: 2026-07-28 MCP 명세 릴리스 후보

다가오는 `2026-07-28` MCP 명세 릴리스 후보를 다루는 수업이 추가되었습니다 (2026년 5월 21일 발표; 최종 릴리스 예정 7월 28일). [공식 발표 블로그 포스트](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)에서 요약했습니다. 커리큘럼의 기준은 새로운 버전 배포까지 <strong>MCP 명세 2025-11-25</strong>로 유지되므로, 기존 수업을 다시 작성하기보다 미래 지향적 지침으로 제공됩니다.

- <strong>신규</strong>: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — 상태 없는 프로토콜 핵심 (initialize 핸드셰이크 및 `Mcp-Session-Id` 제거), 새로운 `Mcp-Method`/`Mcp-Name` 라우팅 헤더, `ttlMs`/`cacheScope` 캐싱 메타데이터, `_meta` 내 W3C Trace Context, 공식 확장 프레임워크 (MCP 앱 및 새 Tasks 확장), 여섯 개의 권한 강화 SEP, Roots/Sampling/Logging 폐지, 전체 JSON Schema 2020-12로 도구 스키마 전환을 다룬 전체 수업입니다.
- <strong>업데이트</strong>: 새 수업과 연동하는 미래 지향 콜아웃 추가:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): 프로토콜 버전 안내, Sampling/Roots/Logging/Tasks 섹션, 및 "다음 단계"
  - [02-Security/README.md](./02-Security/README.md): 권한 강화 콜아웃
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): 상태 없는 전송 콜아웃
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Sampling 폐지 콜아웃
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Logging 폐지 및 Tasks 확장 콜아웃
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): 상태 없음/세션 라우팅 콜아웃
  - [README.md](./README.md): 명세 섹션 내 "앞을 내다보며" 노트 및 커리큘럼 모듈 테이블에 `1.1` 신규 항목 추가
  - [study_guide.md](./study_guide.md): 핵심 개념 개요 하단의 미래 지향 점과 날짜가 적힌 부록 노트
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): 상태 없는 요청 모델 전에 `mcp-session-id` 전송 맵 콜아웃
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): 루트 컨텍스트/Sampling 폐지 및 Tasks 확장에 대한 모듈 개요 콜아웃
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): 권한 강화 콜아웃

## 2026년 6월 24일

### 신규 수업: Copilot 앱에서 MCP 사용하기

- [도구 섹션](./12-tooling/README.md) 추가.
- [Copilot 앱 내 MCP](./12-tooling/01-copilot-app/README.md)

## 2026년 6월 16일

### MCP 명세 정렬 및 샘플 검증

커리큘럼을 현재 **MCP 명세 2025-11-25** 및 최신 공식 SDK와 대조하여 검증하고, 여전히 남아있던 오래된 명세 참조를 수정했으며 주요 샘플들이 여전히 빌드되고 실행됨을 확인했습니다.

#### 명세 버전 수정 (2025-06-18 / 2025-03-26 → 2025-11-25)

이전 명세 개정판을 *현재/최신* 표준이라고 명시한 영어 내용 업데이트 및 주요 링크를 공식 `modelcontextprotocol.io` 명세 경로로 변경:
- **05-AdvancedTopics/mcp-security/README.md**: "현재 표준" 배너, 소개, 핵심 보안 원칙 제목, 필수 요구 사항 제목, Microsoft Entra ID 섹션, 참조 및 자료 링크, 보안 종료 공지 (8개 참조)를 2025-11-25로 업데이트
- **05-AdvancedTopics/mcp-transport/README.md**: 추가 자료 명세 링크 및 "현재 표준" 배너를 2025-11-25로 업데이트
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: 오래된 `2025-03-26` 보안 및 신뢰 링크를 최신 2025-11-25 보안 모범 사례 페이지로 교체
- **03-GettingStarted/14-sampling/README.md**: 공식 샘플링 문서 링크를 2025-11-25로 업데이트

- **03-GettingStarted/05-stdio-server/README.md**: 현재형 "현 MCP 사양" 참조 및 추가 리소스 사양 링크를 2025-11-25로 업데이트함 (정확성을 위해 과거 SSE 폐기 노트는 그대로 둠)

#### 현재 SDK에 대한 샘플 검증

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install`로 `@modelcontextprotocol/sdk@1.29.0` 해결 완료; `tsc --noEmit`에서 타입 오류 없이 통과 — 기존 `McpServer`/`StdioServerTransport` API는 계속 유효함
- **Python (03-GettingStarted/01-first-server/solution/python)**: 격리된 `.venv`에서 `mcp[cli]` (1.27.2) 사용해 검증; `py_compile` 통과 및 `FastMCP.list_tools()`가 `add`와 `subtract` 도구를 올바르게 반환함
- 모든 샘플 `@modelcontextprotocol/sdk` 버전 범위 (`>=1.26.0` / `^1.26.0` / `^1.27.0`)가 현재 `1.29.0`으로 정상 해결되며 API 변경 사항 없음 확인

#### 의존성 고정 정렬 (버전 차이 해소)

오래된 SDK 고정을 올려 각 샘플이 현재 MCP 릴리스를 추적하도록 업데이트하여 저장소 전체 규칙과 일치시킴:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: `@modelcontextprotocol/sdk`를 `^1.8.0`에서 `>=1.26.0`으로 상향 조정하고, 오래된 `"updated for MCP 2025-06-18"` 패키지 설명을 `"aligned with MCP Specification 2025-11-25"`로 변경
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** 및 **lab4/code/github_mcp_server/pyproject.toml**: 정확히 고정된 `mcp==1.23.0`을 `mcp>=1.26.0`으로 변경; 두 `uv.lock` 파일(`uv lock`)을 재생성하여 락파일이 현재 `mcp 1.27.2`를 해결하고 매니페스트와 동기화 유지

#### 교육 과정 격차 분석 — 최신 사양 기능 반영 상태

교육 과정이 MCP 2025-11-25에서 도입/확장된 모든 기본 기능을 이미 포괄하므로 내용 격차 없음 확인됨:
- <strong>샘플링</strong>: 03-GettingStarted/14-sampling 및 05-AdvancedTopics/mcp-sampling 강의
- **끌어내기(URL 모드 포함)**: 01-CoreConcepts 및 05-AdvancedTopics/mcp-protocol-features에 문서화됨
- <strong>루트</strong>: 00-Introduction, 01-CoreConcepts, 및 05-AdvancedTopics/mcp-root-contexts에 문서화됨
- **작업(실험적, 장기 실행 연산)**: 01-CoreConcepts 및 05-AdvancedTopics/mcp-protocol-features에 문서화됨
- **도구 주석** (`readOnlyHint` / `destructiveHint`): 01-CoreConcepts 및 05-AdvancedTopics/mcp-protocol-features에 문서화됨

### 보안 강화 및 의존성 취약점 보완

모든 의존성 매니페스트와 샘플 소스 코드에 대해 전체 보안 점검을 수행하고, 보고된 모든 npm 경고와 코드 수준 문제 하나를 해결함. 보완 후 `npm audit`는 모든 감사 대상 디렉터리에서 <strong>0개의 취약점</strong>을 보고함.

#### npm 의존성 취약점 (전이적) — 수정됨

커밋된 15개 `package-lock.json` 파일 전부 감사함. 취약점은 MCP Inspector 개발 도구, OpenAI 클라이언트, MCP SDK에서 끌어온 전이적 의존성에 한정되어 있었으며, 모두 샘플에 영향 없이 해결됨:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** 및 **lab3/code/weather_mcp/inspector**: `@modelcontextprotocol/inspector`(`0.16.6` / `0.14.1` → `0.22.0`) 상향 조정으로 포함된 `ajv`, `brace-expansion`, `diff`, `path-to-regexp`, `ws` 경고 해소. npm `overrides`에 패치된 `shell-quote@1.8.4` 강제 적용하여 `concurrently`가 남긴 치명적 경고 해소; 양측 락파일 재생성(현재 0 취약점)
- **03-GettingStarted/samples/typescript**: `npm audit fix`로 전이된 `qs` (중간 위험) 패치 버전으로 업데이트
- **03-GettingStarted/samples/javascript**: `npm audit fix`로 전이된 `hono` (중간 위험) 패치 버전으로 업데이트
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix`로 전이된 `form-data` (높은 위험) 패치 버전으로 업데이트
- **03-GettingStarted/11-simple-auth/solution/typescript**: 누락된 `package-lock.json` 생성하여 프로젝트 재현 및 감사 가능하게 함 (취약점 0개)

#### 코드 수준 보안 수정 (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: `open_in_vscode` 도구에서 `shell=True` 제거. 이전 `subprocess.run(["start", "", vscode_path, folder_path], shell=True)`는 폴더 경로의 셸 메타문자를 `cmd.exe`가 해석하게 하여 명령어 주입 벡터였음. 현재는 폴더를 인자로 직접 실행 파일 `Code.exe`를 실행하여 셸 없이 함수적으로 동등하고 안전함

#### Python 의존성 감사

- 모든 Python 요구 사항 세트를 `pip-audit`으로 감사함. `05-AdvancedTopics` 및 `03-GettingStarted/samples/python`은 **알려진 취약점 없음** 보고 (해당 `mcp` / `httpx` / `pydantic` / `python-dotenv` 범위가 현재 패치 릴리스로 해결됨)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit`가 전이적 의존성 **`werkzeug` 3.1.1**에서 세 개의 `safe_join` Windows 디바이스 이름 DoS 경고 (`CVE-2025-66221`, `CVE-2026-21860`, `CVE-2026-27199`, 모두 3.1.6에서 수정됨)를 발견함. 명시적 보안 고정 `werkzeug>=3.1.6` 추가하여 패치 릴리스가 해결되도록 함; `chainlit` / `mcp` / `semantic-kernel` 스택으로 제약 조건이 깔끔하게 해결됨 검증

### 제품 이름 리브랜딩

모든 교육 과정 내용을 Microsoft의 제품 리브랜딩에 맞게 업데이트함:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Discord 커뮤니티 링크 업데이트

- **AGENTS.md**: 디스코드 서버 참조 업데이트
- **README.md**: 기술 생태계 참조 업데이트
- **study_guide.md**: 사례 연구 참조 업데이트
- **05-AdvancedTopics/README.md**: 모듈 5.13 제목 및 설명 업데이트
- **05-AdvancedTopics/mcp-integration/README.md**: 섹션 헤더 및 설명 업데이트
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: 전체 모듈 제목 및 내용 업데이트
- **05-AdvancedTopics/mcp-security-entra/README.md**: 교차 참조 링크 업데이트
- **07-LessonsfromEarlyAdoption/README.md**: 사례 연구 참조 업데이트
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: 섹션 9 헤더, 배지 및 기능 업데이트
- **08-BestPractices/README.md**: 디스코드 커뮤니티 링크 업데이트
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: 디스코드 채널 참조 업데이트
- **09-CaseStudy/docs-mcp/solution/python/README.md**: 모델 배포 참조 업데이트
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: AI 서비스 테이블 업데이트
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: 리소스 참조 업데이트

#### AI Toolkit / AITK → VS Code용 Microsoft Foundry Toolkit Extension
- **README.md**: 주요 교육 과정 참조 업데이트
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: 모듈 제목, 개요 및 모든 모듈 헤더 업데이트
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: 제목, 학습 목표, 설정 지침 및 리소스 업데이트
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: 제목, 학습 목표, MCP 호스트 테이블 및 교차 참조 업데이트
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: 제목, 배지, 전제 조건 및 리소스 업데이트
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: 에이전트 빌더 참조 및 피드백 링크 업데이트
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: 전제 조건 및 확장 참조 업데이트

---

## 2026년 4월 11일

### 새로운 강의, 문서 수정 및 종속성 업데이트

#### 새로운 교육 과정 내용 추가

**모듈 05 - 고급 주제**
- **레슨 5.17: MCP를 활용한 적대적 다중 에이전트 추론** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): 다중 에이전트 시스템을 위한 적대적 토론 패턴에 대한 종합 가이드 신규 추가
  - 머메이드 아키텍처 다이어그램: 두 에이전트 → 공유 MCP 서버 → 토론 기록 → 심판 → 판결
  - 파이썬과 타입스크립트로 구현된 공유 MCP 도구 서버(`web_search` + `run_python`)
  - 명확한 도구 사용 요구사항이 포함된 반대 시스템 프롬프트(FOR / AGAINST / Judge)
  - 라운드 관리 및 주장 라우팅을 담당하는 파이썬, 타입스크립트, C# 토론 감독자
  - 도구 실제 호출을 위한 MCP `ClientSession` 와이어링
  - 활용 사례 표 (환각 감지, 위협 모델링, API 설계 검토, 사실 검증, 기술 선택)
  - 보안 고려사항: 샌드박스 실행, 도구 호출 검증, 속도 제한, 감사 로그
  - 세 가지 실습 시나리오(코드 리뷰, 아키텍처 결정, 콘텐츠 검열)를 포함한 구조화된 연습

#### 문서 수정

**모듈 03 - 시작하기**
- **05-stdio-server/README.md**: 불완전했던 TypeScript stdio 서버 예제 수정 — 누락된 전송 인스턴스 생성(`new StdioServerTransport()`) 및 `server.connect(transport)` 호출 추가, 동일 섹션 내 Python 및 .NET 예제와 맞춤
- **14-sampling/README.md**: 오타 수정 — `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### 교육 과정 업데이트

**주요 README.md**
- 새로운 강의에 대한 직접 링크와 함께 커리큘럼 표에 항목 5.17 (MCP를 활용한 적대적 다중 에이전트 추론) 추가

**05-AdvancedTopics/README.md**
- 강의 테이블에 레슨 5.17 행 추가

**study_guide.md**
- 마인드맵 및 고급 주제 설명에 적대적 다중 에이전트 추론 주제 추가

#### 코드 및 보안 수정

**모듈 05 - 적대적 에이전트 (`mcp-adversarial-agents`)**
- **보안 수정 — 명령어 인젝션**: TypeScript `run_python` 도구의 `execSync` 셸 보간을 `execFile` + `promisify`로 교체하여 명령어 인젝션 취약점 제거 (LLM 제어 코드는 셸 개입 없이 리터럴 argv 요소로 전달)
- **MCP 도구 루프 와이어링**: Python 토론 감독자를 `AsyncAnthropic` 클라이언트로 업데이트(블로킹 동기 `Anthropic` 대체), 각 에이전트 턴에 실시간 `ClientSession` 직접 전달, 각 턴마다 `session.list_tools()`로 도구 정의 조회, 모델이 최종 텍스트 응답을 낼 때까지 루프 내에서 `session.call_tool()`로 `tool_use` 블록 디스패치

#### 종속성 업데이트

- 여러 패키지(03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)에서 `hono`를 4.12.12 버전으로 업데이트
- 타입스크립트 패키지에서 `@hono/node-server`를 1.19.11에서 1.19.13으로 업데이트
- 파이썬 패키지(10-StreamliningAIWorkflows 랩 3 및 4)에서 `cryptography`를 46.0.5에서 46.0.7로 업데이트
- 10-StreamliningAIWorkflows 검사 도구에서 `lodash`를 4.17.23에서 4.18.1로 업데이트

#### 번역

- 최신 소스 변경사항에 맞춰 48개 이상 언어의 번역 동기화(i18n 업데이트)

---

## 2026년 2월 5일

### 저장소 전체 검증 및 내비게이션 개선

#### 새로운 교육 과정 내용 추가

**모듈 03 - 시작하기**
- **12-mcp-hosts/README.md**: MCP 호스트 설정에 관한 종합 안내서 신규 추가
  - Claude Desktop, VS Code, Cursor, Cline, Windsurf 구성 예제
  - 주요 호스트 모두에 대한 JSON 구성 템플릿
  - 전송 유형 비교 표 (stdio, SSE/HTTP, WebSocket)
  - 자주 발생하는 연결 문제 해결 방법
  - 호스트 구성에 대한 보안 모범 사례

- **13-mcp-inspector/README.md**: MCP 검사 도구 디버깅 가이드 신규 추가
  - 설치 방법 (npx, 전역 npm, 소스에서)
  - stdio 및 HTTP/SSE를 통한 서버 연결
  - 테스트 도구, 리소스, 프롬프트 워크플로
  - VS Code와 MCP 검사 도구 통합
  - 일반적인 디버깅 시나리오와 해결법

**모듈 04 - 실무 구현**
- **pagination/README.md**: 새로운 페이지 네이션 구현 가이드
  - Python, TypeScript, Java의 커서 기반 페이지 네이션 패턴
  - 클라이언트 쪽 페이지 네이션 처리
  - 커서 설계 전략 (불투명 vs 구조화)
  - 성능 최적화 권장 사항

**모듈 05 - 고급 주제**
- **mcp-protocol-features/README.md**: 새로운 프로토콜 기능 심층 분석
  - 진행 상황 알림 구현
  - 요청 취소 패턴
  - URI 패턴이 포함된 리소스 템플릿
  - 서버 생애 주기 관리
  - 로깅 수준 제어
  - JSON-RPC 코드가 포함된 오류 처리 패턴

#### 내비게이션 수정 (24개 이상 파일 업데이트)

**주요 모듈 README들**
 첫 강의와 다음 모듈 모두로의 링크 추가

**02-보안 하위 파일들**
- 5개 보조 보안 문서 모두 "다음 단계" 내비게이션 추가:

**09-사례 연구 파일들**
- 모든 사례 연구 파일에 순차 내비게이션 추가:

**10-StreamliningAI 랩**
모듈 10 개요와 모듈 11에 다음 단계 섹션 추가

#### 코드 및 콘텐츠 수정

**SDK 및 종속성 업데이트**
빈 openai 버전을 `^4.95.0`으로 수정
SDK를 `^1.8.0`에서 `>=1.26.0`으로 업데이트
MCP 버전 핀을 `>=1.26.0`으로 업데이트

**코드 수정**
유효하지 않은 모델 `gpt-4o-mini`를 `gpt-4.1-mini`로 수정

**콘텐츠 수정**
부서진 링크 `READMEmd` → `README.md`, 커리큘럼 헤더 `Module 1-3` → `Module 0-3` 수정, 대소문자 경로 수정
손상된 중복 사례 연구 5 콘텐츠 제거

**초보자 안내 개선**
초보자를 위한 적절한 소개, 학습 목표 및 전제 조건 추가

#### 교육 과정 업데이트

**주요 README.md**
- 교육 과정 표에 항목 3.12 (MCP 호스트), 3.13 (MCP 검사 도구), 4.1 (페이지 네이션), 5.16 (프로토콜 기능) 추가

**모듈 README들**
강의 목록에 레슨 12와 13 추가
페이지 네이션 링크와 함께 실무 안내 섹션 추가
레슨 5.15 (사용자 정의 전송) 및 5.16 (프로토콜 기능) 추가

**study_guide.md**
- 모든 신규 주제 포함하여 마인드맵 업데이트: MCP 호스트 설정, MCP 검사 도구, 페이지 네이션 전략, 프로토콜 기능 심층 분석

## 2026년 1월 28일

### MCP 사양 2025-11-25 준수 검토

#### 핵심 개념 강화 (01-CoreConcepts/)
- **새 클라이언트 원시 항목 - Roots**: 서버가 파일 시스템 경계와 접근 권한을 이해할 수 있도록 하는 Roots 클라이언트 원시 항목에 대한 종합 문서 추가
- **도구 주석**: 도구 실행 결정 개선을 위한 `readOnlyHint`, `destructiveHint` 행동 주석 문서 추가
- **샘플링 중 도구 호출**: 샘플링 요청 시 모델 기반 도구 호출을 위한 `tools` 및 `toolChoice` 매개변수 포함하도록 샘플링 문서 업데이트
- **URL 모드 유도**: 서버 주도 외부 웹 상호작용을 위한 URL 기반 유도 문서 추가
- **작업(실험적)**: 내구 실행 래퍼 및 지연 결과 검색을 위한 실험적 작업 기능 문서 추가
- **아이콘 지원**: 도구, 리소스, 리소스 템플릿 및 프롬프트가 이제 추가 메타데이터로 아이콘 포함 가능 명시

#### 문서 업데이트
- **README.md**: MCP 사양 2025-11-25 버전 참조 및 날짜 기반 버전 관리 설명 추가
- **study_guide.md**: 핵심 개념 섹션에 작업 및 도구 주석 포함하도록 교육 과정 지도 업데이트; 문서 타임스탬프 업데이트

#### 사양 준수 검증
- **프로토콜 버전**: 모든 문서가 현재 MCP 사양 2025-11-25 참조를 확인
- **아키텍처 정렬**: 2계층 아키텍처(데이터 계층 + 전송 계층) 문서 정확성 확인
- **원시 항목 문서**: 서버 원시 항목(리소스, 프롬프트, 도구) 및 클라이언트 원시 항목(샘플링, 유도, 로깅, Roots) 검증
- **전송 메커니즘**: STDIO 및 스트림 가능한 HTTP 전송 문서 정확성 확인
- **보안 지침**: 현재 MCP 보안 모범 사례 문서와 일치 확인

#### 주요 MCP 2025-11-25 기능 문서화
- **OpenID Connect 탐색**: OIDC를 통한 인증 서버 탐색
- **OAuth 클라이언트 ID 메타데이터 문서**: 클라이언트 등록 방법 권장
- **JSON 스키마 2020-12**: MCP 스키마 정의의 기본 방언
- **SDK 계층 시스템**: SDK 기능 지원 및 유지 보수 요구사항 공식화
- **거버넌스 구조**: MCP 거버넌스 내 작업 그룹 및 관심 그룹 공식화

### 보안 문서 주요 업데이트 (02-Security/)

#### MCP 보안 서밋 워크숍 (Sherpa) 통합
- **새로운 실습 교육 자료**: 모든 보안 문서에 [MCP 보안 서밋 워크숍 (Sherpa)](https://azure-samples.github.io/sherpa/)와의 종합 통합 추가
- **원정 경로 커버리지**: 베이스 캠프부터 정상까지의 완전한 캠프 간 진행 경로 문서화
- **OWASP 정렬**: 모든 보안 지침이 OWASP MCP Azure 보안 가이드 위험과 매핑됨

#### OWASP MCP 상위 10위 통합
- **새 섹션**: Azure 완화책이 포함된 OWASP MCP 상위 10위 보안 위험 표를 주요 보안 README에 추가
- **위험 기반 문서**: 각 보안 도메인에 대한 OWASP MCP 위험 참조가 포함된 mcp-security-controls-2025.md 업데이트
- **참조 아키텍처**: OWASP MCP Azure 보안 가이드 참조 아키텍처 및 구현 패턴 링크 추가

#### 보안 파일 업데이트
- **README.md**: Sherpa 워크숍 개요, 원정 경로 표, OWASP MCP 상위 10위 위험 요약 및 실습 교육 섹션 추가
- **mcp-security-controls-2025.md**: 2026년 2월 헤더 업데이트, OWASP 위험 참조 (MCP01-MCP08) 추가, 사양 버전 불일치 수정
- **mcp-security-best-practices-2025.md**: Sherpa 및 OWASP 리소스 섹션 추가, 타임스탬프 업데이트
- **mcp-best-practices.md**: Sherpa 및 OWASP 링크가 포함된 실습 교육 섹션 추가
- **azure-content-safety-implementation.md**: OWASP MCP06 참조, Sherpa 캠프 3 정렬 및 추가 리소스 섹션 추가

#### 새로운 리소스 링크 추가
- [MCP 보안 서밋 워크숍 (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure 보안 가이드](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- 개별 OWASP MCP 위험 페이지 (MCP01-MCP10)

### 커리큘럼 전반 MCP 명세 2025-11-25 정렬

#### 모듈 03 - 시작하기
- **SDK 문서**: 공식 SDK 목록에 Go SDK 추가; MCP 명세 2025-11-25에 맞게 모든 SDK 참조 업데이트
- **전송 명확화**: STDIO 및 HTTP 스트리밍 전송 설명에 명확한 명세 참조 업데이트

#### 모듈 04 - 실용 구현
- **SDK 업데이트**: Go SDK 추가; 명세 버전 참조와 함께 SDK 목록 업데이트
- **권한 부여 명세**: MCP 권한 부여 명세 링크를 최신 2025-11-25 버전으로 업데이트

#### 모듈 05 - 고급 주제
- **새 기능**: MCP 명세 2025-11-25의 새로운 기능(작업, 도구 주석, URL 모드 이끌어내기, 루트)에 관한 메모 추가
- **보안 리소스**: OWASP MCP Top 10 및 Sherpa 워크숍 링크를 추가 참조로 추가

#### 모듈 06 - 커뮤니티 기여
- **SDK 목록**: Swift 및 Rust SDK 추가; 명세 링크를 2025-11-25로 업데이트
- **명세 참조**: MCP 명세 링크를 직접 명세 URL로 업데이트

#### 모듈 07 - 초기 도입에서의 교훈
- **리소스 업데이트**: MCP 명세 2025-11-25 링크와 OWASP MCP Top 10을 추가 리소스에 추가

#### 모듈 08 - 모범 사례
- **명세 버전**: MCP 명세 참조를 2025-11-25로 업데이트
- **보안 리소스**: OWASP MCP Top 10 및 Sherpa 워크숍을 추가 참조로 추가

#### 모듈 10 - AI 워크플로우 간소화
- **배지 업데이트**: MCP 버전 배지를 SDK 버전(1.9.3)에서 명세 버전(2025-11-25)으로 변경
- **리소스 링크**: MCP 명세 링크 업데이트; OWASP MCP Top 10 추가

#### 모듈 11 - MCP 서버 실습 랩
- **명세 참조**: MCP 명세 링크를 2025-11-25 버전으로 업데이트
- **보안 리소스**: 공식 리소스에 OWASP MCP Top 10 추가

## 2025년 12월 18일

### 보안 문서 업데이트 - MCP 명세 2025-11-25

#### MCP 보안 모범 사례 (02-Security/mcp-best-practices.md) - 명세 버전 업데이트
- **프로토콜 버전 업데이트**: 최신 MCP 명세 2025-11-25 (2025년 11월 25일 출시) 참조로 업데이트
  - 모든 명세 버전 참조를 2025-06-18에서 2025-11-25로 업데이트
  - 문서 날짜 참조를 2025년 8월 18일에서 2025년 12월 18일로 업데이트
  - 모든 명세 URL이 현재 문서를 가리키는지 확인
- **내용 검증**: 최신 표준에 따른 보안 모범 사례의 포괄적 검증
  - **Microsoft 보안 솔루션**: Prompt Shields(이전 "Jailbreak 위험 탐지"), Azure 콘텐츠 안전, Microsoft Entra ID, Azure Key Vault의 현재 용어 및 링크 확인
  - **OAuth 2.1 보안**: 최신 OAuth 보안 모범 사례와의 정렬 확인
  - **OWASP 표준**: LLM용 OWASP Top 10 참조가 최신 상태인지 검증
  - **Azure 서비스**: 모든 Microsoft Azure 문서 링크 및 모범 사례 확인
- **표준 정렬**: 참조된 모든 보안 표준이 최신임을 확인
  - NIST AI 위험 관리 프레임워크
  - ISO 27001:2022
  - OAuth 2.1 보안 모범 사례
  - Azure 보안 및 컴플라이언스 프레임워크
- **구현 리소스**: 모든 구현 가이드 링크 및 리소스 검증
  - Azure API 관리 인증 패턴
  - Microsoft Entra ID 통합 가이드
  - Azure Key Vault 비밀 관리
  - DevSecOps 파이프라인 및 모니터링 솔루션

### 문서 품질 보증
- **명세 준수**: 모든 필수 MCP 보안 요구사항(MUST/MUST NOT)이 최신 명세와 일치하는지 확인
- **리소스 최신성**: Microsoft 문서, 보안 표준 및 구현 가이드에 대한 모든 외부 링크 검증
- **모범 사례 범위**: 인증, 권한 부여, AI 특화 위협, 공급망 보안 및 엔터프라이즈 패턴에 대한 포괄적 커버리지 확인

## 2025년 10월 6일

### 시작하기 섹션 확장 – 고급 서버 사용법 및 간단한 인증

#### 고급 서버 사용법 (03-GettingStarted/10-advanced)
- **새 장 추가**: 정규 및 저수준 서버 아키텍처를 모두 다루는 포괄적인 고급 MCP 서버 사용법 가이드 도입
  - **정규 서버 vs 저수준 서버**: 두 접근법에 대한 상세 비교 및 Python, TypeScript 코드 예제 포함
  - **핸들러 기반 설계**: 확장 가능하고 유연한 서버 구현을 위한 도구/리소스/프롬프트 관리 방식 설명
  - **실용적 패턴**: 고급 기능과 아키텍처에 유리한 저수준 서버 패턴의 실제 사례

#### 간단한 인증 (03-GettingStarted/11-simple-auth)
- **새 장 추가**: MCP 서버에 간단한 인증을 구현하는 단계별 가이드
  - **인증 개념**: 인증과 권한 부여, 자격 증명 처리에 대한 명확한 설명
  - **기본 인증 구현**: Python(Starlette) 및 TypeScript(Express) 기반 미들웨어 인증 패턴과 코드 샘플 제공
  - **고급 보안 진입 안내**: 간단한 인증에서 시작해 OAuth 2.1 및 RBAC로 진전하는 방법과 고급 보안 모듈 참조 안내

이러한 추가 내용은 기초 개념과 고급 생산 패턴을 연결하여 더욱 견고하고 안전하며 유연한 MCP 서버 구현을 위한 실질적이고 실용적인 지침을 제공합니다.

## 2025년 9월 29일

### MCP 서버 데이터베이스 통합 랩 - 포괄적인 실습 학습 경로

#### 11-MCPServerHandsOnLabs - 완전한 데이터베이스 통합 커리큘럼 신규 추가
- **전체 13랩 학습 경로**: PostgreSQL 데이터베이스 통합을 통한 생산 준비 MCP 서버 구축을 위한 포괄적 실습 커리큘럼 추가
  - **실제 구현사례**: Zava Retail 분석 사례를 통한 엔터프라이즈급 패턴 시연
  - **구조화된 학습 진행**:
    - **랩 00-03: 기초** - 소개, 핵심 아키텍처, 보안 및 다중 테넌시, 환경 설정
    - **랩 04-06: MCP 서버 구축** - 데이터베이스 설계 및 스키마, MCP 서버 구현, 도구 개발  
    - **랩 07-09: 고급 기능** - 의미론적 검색 통합, 테스트 및 디버깅, VS Code 통합
    - **랩 10-12: 생산 및 모범 사례** - 배포 전략, 모니터링과 관측, 모범 사례 및 최적화
  - **엔터프라이즈 기술**: FastMCP 프레임워크, pgvector가 적용된 PostgreSQL, Azure OpenAI 임베딩, Azure 컨테이너 앱, Application Insights
  - **고급 기능들**: 행 수준 보안(RLS), 의미론적 검색, 다중 테넌트 데이터 접근, 벡터 임베딩, 실시간 모니터링

#### 용어 표준화 - 모듈에서 랩으로 전환
- **포괄적 문서 업데이트**: 11-MCPServerHandsOnLabs의 모든 README 파일에서 "모듈" 대신 "랩" 용어 체계로 체계적으로 업데이트
  - **섹션 헤더**: 모든 13개 랩에서 "이 모듈의 내용"을 "이 랩의 내용"으로 변경
  - **내용 설명**: 문서 전반에 걸쳐 "이 모듈은 ..."을 "이 랩은 ..."으로 변경
  - **학습 목표**: "이 모듈을 마치면 ..."을 "이 랩을 마치면 ..."으로 업데이트
  - **내비게이션 링크**: 교차 참조 및 내비게이션에서 모든 "Module XX:"를 "Lab XX:"로 변환
  - **완료 추적**: "이 모듈 완료 후 ..."를 "이 랩 완료 후 ..."로 업데이트
  - **기술적 참조 유지**: 구성 파일 내 Python 모듈 참조는 그대로 유지 (예: `"module": "mcp_server.main"`)

#### 학습 가이드 향상 (study_guide.md)
- **시각적 커리큘럼 맵**: "11. 데이터베이스 통합 랩" 섹션과 포괄적 랩 구조 시각화 추가
- **저장소 구조**: 열 개의 주요 섹션에서 열한 개로 업데이트하며 11-MCPServerHandsOnLabs 세부 설명 추가
- **학습 경로 안내**: 00-11 섹션을 포함하는 내비게이션 지침 강화
- **기술 범위**: FastMCP, PostgreSQL, Azure 서비스 통합 세부정보 추가
- **학습 성과**: 생산 준비 서버 개발, 데이터베이스 통합 패턴, 엔터프라이즈 보안 강조

#### 메인 README 구조 향상
- **랩 기반 용어 통일**: 11-MCPServerHandsOnLabs 메인 README.md를 "랩" 체계에 일관되게 맞춤
- **학습 경로 조직**: 기초 개념부터 고급 구현, 생산 배포에 이르는 명확한 진행
- **실용성 중점**: 엔터프라이즈급 패턴과 기술을 통한 실습 기반 학습 강조

### 문서 품질 및 일관성 개선
- **실습 학습 강조**: 문서 전반에 걸친 실용적, 랩 기반 접근법 강화
- **엔터프라이즈 패턴 중점**: 생산 준비 구현 및 엔터프라이즈 보안 고려사항 강조
- **기술 통합**: 최신 Azure 서비스 및 AI 통합 패턴에 대한 포괄적 커버리지
- **학습 진행**: 기초 개념부터 생산 배포까지 명확하고 구조화된 경로

## 2025년 9월 26일

### 사례 연구 향상 - GitHub MCP 레지스트리 통합

#### 사례 연구 (09-CaseStudy/) - 생태계 개발 중점
- **README.md**: 포괄적 GitHub MCP 레지스트리 사례 연구로 대폭 확장
  - **GitHub MCP 레지스트리 사례 연구**: 2025년 9월 GitHub MCP 레지스트리 출시에 대한 포괄적 사례 연구 신규 추가
    - **문제 분석**: 분산된 MCP 서버 탐색 및 배포 문제 상세 분석
    - **해결책 아키텍처**: GitHub의 중앙화된 레지스트리 접근법과 원클릭 VS Code 설치
    - **비즈니스 영향**: 개발자 온보딩 및 생산성 향상 측정 가능
    - **전략적 가치**: 모듈식 에이전트 배포 및 도구 간 상호운용성 중점
    - **생태계 개발**: 에이전트 통합을 위한 기초 플랫폼으로 위치 매김
  - **사례 연구 구조 개선**: 모든 일곱 개 사례 연구를 일관된 형식과 포괄적 설명으로 업데이트
    - Azure AI 여행 에이전트: 다중 에이전트 오케스트레이션 중점
    - Azure DevOps 통합: 워크플로 자동화 중점
    - 실시간 문서 검색: Python 콘솔 클라이언트 구현
    - 대화형 학습 계획 생성기: Chainlit 대화형 웹 앱
    - 편집기 내 문서: VS Code 및 GitHub Copilot 통합
    - Azure API 관리: 엔터프라이즈 API 통합 패턴
    - GitHub MCP 레지스트리: 생태계 개발 및 커뮤니티 플랫폼
  - **포괄적 결론**: 여러 MCP 구현 차원을 포괄하는 일곱 사례 연구를 강조하는 결론 부분 재작성
    - 엔터프라이즈 통합, 다중 에이전트 오케스트레이션, 개발자 생산성
    - 생태계 개발, 교육 애플리케이션 분류
    - 아키텍처 패턴, 구현 전략, 모범 사례에 대한 향상된 통찰
    - MCP를 성숙하고 생산 준비된 프로토콜로 강조

#### 학습 가이드 업데이트 (study_guide.md)
- **시각적 커리큘럼 맵**: 사례 연구 섹션에 GitHub MCP 레지스트리 포함하도록 마인드맵 업데이트
- **사례 연구 설명 강화**: 일반 설명에서 일곱 개 포괄적 사례 연구의 세부 분석으로 강화
- **저장소 구조**: 10번 섹션을 구체적 구현 세부 정보로 사례 연구 포괄적 커버리지 반영해 업데이트
- **변경 로그 통합**: 2025년 9월 26일 항목에 GitHub MCP 레지스트리 및 사례 연구 강화 문서 추가
- **날짜 업데이트**: 최신 수정일(2025년 9월 26일)로 바닥글 타임스탬프 업데이트

### 문서 품질 개선
- **일관성 강화**: 모든 일곱 사례 연구의 형식 및 구조 표준화
- **포괄적 커버리지**: 엔터프라이즈, 개발자 생산성, 생태계 개발 시나리오를 포함하도록 확장
- **전략적 위치 지정**: 에이전트 시스템 배포의 기초 플랫폼으로서 MCP에 대한 강조 강화
- **리소스 통합**: 추가 리소스에 GitHub MCP 레지스트리 링크 업데이트

## 2025년 9월 15일

### 고급 주제 확장 - 맞춤형 전송 및 컨텍스트 엔지니어링

#### MCP 맞춤형 전송 (05-AdvancedTopics/mcp-transport/) - 새로운 고급 구현 가이드
- **README.md**: 맞춤 MCP 전송 메커니즘에 대한 완전한 구현 가이드
  - **Azure Event Grid 전송**: 서버리스 이벤트 구동 전송 구현 포괄
    - C#, TypeScript, Python 예제 및 Azure Functions 통합
    - 확장 가능한 MCP 솔루션을 위한 이벤트 기반 아키텍처 패턴
    - 웹훅 수신기 및 푸시 기반 메시지 처리
  - **Azure Event Hubs 전송**: 고처리량 스트리밍 전송 구현
    - 저지연 시나리오용 실시간 스트리밍 기능
    - 파티셔닝 전략 및 체크포인트 관리
    - 메시지 배치 및 성능 최적화
  - **엔터프라이즈 통합 패턴**: 생산 준비 아키텍처 예제
    - 여러 Azure Functions에 걸친 분산 MCP 처리
    - 다중 전송 유형 결합 하이브리드 전송 아키텍처
    - 메시지 내구성, 신뢰성, 오류 처리 전략
  - **보안 및 모니터링**: Azure Key Vault 통합 및 관측 패턴
    - 관리형 ID 인증 및 최소 권한 접근
    - Application Insights 원격 측정 및 성능 모니터링
    - 회로 차단기 및 장애 허용 패턴
  - **테스트 프레임워크**: 맞춤 전송에 대한 포괄적 테스트 전략
    - 테스트 더블 및 모킹 프레임워크를 활용한 단위 테스트
    - Azure 테스트 컨테이너를 활용한 통합 테스트
    - 성능 및 부하 테스트 고려사항

#### 컨텍스트 엔지니어링 (05-AdvancedTopics/mcp-contextengineering/) - 새로 떠오르는 AI 분야
- **README.md**: 떠오르는 분야로서 컨텍스트 엔지니어링에 대한 포괄적 탐구
  - **핵심 원리**: 완전한 컨텍스트 공유, 액션 결정 인식, 컨텍스트 윈도우 관리

  - **MCP 프로토콜 정렬**: MCP 설계가 컨텍스트 엔지니어링 과제를 어떻게 해결하는지
    - 컨텍스트 윈도우 제한 및 점진적 로딩 전략
    - 관련성 판단 및 동적 컨텍스트 검색
    - 다중 모달 컨텍스트 처리 및 보안 고려사항
  - **구현 접근법**: 단일 스레드 대 다중 에이전트 아키텍처
    - 컨텍스트 청킹 및 우선순위 지정 기법
    - 점진적 컨텍스트 로딩 및 압축 전략
    - 계층형 컨텍스트 접근법 및 검색 최적화
  - **측정 프레임워크**: 컨텍스트 효율성 평가를 위한 새로운 메트릭
    - 입력 효율성, 성능, 품질 및 사용자 경험 고려사항
    - 컨텍스트 최적화를 위한 실험적 접근법
    - 실패 분석 및 개선 방법론

#### 커리큘럼 내비게이션 업데이트 (README.md)
- **향상된 모듈 구조**: 새 고급 주제를 포함하도록 커리큘럼 표 업데이트
  - 컨텍스트 엔지니어링 (5.14) 및 맞춤형 전송 (5.15) 항목 추가
  - 모든 모듈에서 일관된 형식 및 내비게이션 링크 유지
  - 현재 콘텐츠 범위를 반영하도록 설명 업데이트

### 디렉터리 구조 개선
- **명명 표준화**: 일관성을 위해 "mcp transport"를 "mcp-transport"로 이름 변경
- **콘텐츠 구성**: 모든 05-AdvancedTopics 폴더가 일관된 명명 패턴(mcp-[주제])을 따름

### 문서 품질 향상
- **MCP 사양 정렬**: 모든 새 콘텐츠가 최신 MCP 사양 2025-06-18 참조
- **다중 언어 예제**: C#, TypeScript, Python의 포괄적 코드 예제
- **기업용 포커스**: 프로덕션 준비 완료 패턴과 Azure 클라우드 통합 전반에 걸쳐
- **시각적 문서화**: 아키텍처 및 흐름 시각화를 위한 Mermaid 다이어그램

## 2025년 8월 18일

### 문서 전면 업데이트 - MCP 2025-06-18 표준

#### MCP 보안 모범 사례 (02-Security/) - 완전 개편
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: MCP 사양 2025-06-18에 맞춘 완전 재작성
  - **필수 요구사항**: 공식 사양의 명확한 MUST/MUST NOT 요구사항 추가, 명확한 시각적 표시 포함
  - **12가지 핵심 보안 실천항목**: 15개 항목 목록에서 포괄적 보안 도메인으로 재구성
    - 외부 ID 제공자 통합을 포함한 토큰 보안 및 인증
    - 암호화 요구사항이 포함된 세션 관리 및 전송 보안
    - Microsoft Prompt Shields 통합을 통한 AI 특화 위협 방어
    - 최소 권한 원칙에 따른 액세스 제어 및 권한
    - Azure Content Safety 통합을 통한 콘텐츠 안전성 및 모니터링
    - 포괄적 구성요소 검증을 포함한 공급망 보안
    - PKCE 구현을 통한 OAuth 보안 및 혼란 대리인 방지
    - 자동화 기능을 갖춘 사고 대응 및 복구
    - 규제 준수를 위한 컴플라이언스 및 거버넌스
    - 제로 트러스트 아키텍처를 활용한 고급 보안 통제
    - 포괄적 솔루션을 포함한 Microsoft 보안 생태계 통합
    - 적응형 실천을 통한 지속적인 보안 진화
  - **Microsoft 보안 솔루션**: Prompt Shields, Azure Content Safety, Entra ID, GitHub Advanced Security 통합 가이드 강화
  - **구현 리소스**: 공식 MCP 문서, Microsoft 보안 솔루션, 보안 표준, 구현 가이드별 포괄적 리소스 링크 분류

#### 고급 보안 통제 (02-Security/) - 기업용 구현
- **MCP-SECURITY-CONTROLS-2025.md**: 기업급 보안 프레임워크로 완전 개편
  - **9개 포괄적 보안 도메인**: 기본 통제에서 상세한 기업 프레임워크로 확장
    - Microsoft Entra ID 통합을 포함한 고급 인증 및 권한 부여
    - 포괄적 검증을 포함한 토큰 보안 및 패스스루 방지 통제
    - 하이재킹 방지를 위한 세션 보안 통제
    - 프롬프트 인젝션 및 툴 중독 방지를 포함한 AI 특화 보안 통제
    - OAuth 프록시 보안을 포함한 혼란 대리인 공격 방지
    - 샌드박싱 및 격리를 통한 툴 실행 보안
    - 의존성 검증을 포함한 공급망 보안 통제
    - SIEM 통합을 통한 모니터링 및 탐지 통제
    - 자동화 기능을 갖춘 사고 대응 및 복구
  - **구현 예제**: 상세한 YAML 구성 블록 및 코드 예제 추가
  - **Microsoft 솔루션 통합**: Azure 보안 서비스, GitHub Advanced Security, 기업 신원 관리에 대한 포괄적 커버리지

#### 고급 주제 보안 (05-AdvancedTopics/mcp-security/) - 프로덕션 준비 구현
- **README.md**: 기업용 보안 구현에 맞춰 완전 재작성
  - **현재 사양 정렬**: MCP 사양 2025-06-18, 필수 보안 요구사항 반영
  - **향상된 인증**: Microsoft Entra ID 통합 및 포괄적인 .NET 및 Java Spring Security 예제
  - **AI 보안 통합**: Microsoft Prompt Shields 및 Azure Content Safety 구현, 상세 Python 예제 포함
  - **고급 위협 완화**: 다음에 대한 포괄적 구현 예제
    - PKCE 및 사용자 동의 검증을 통한 혼란 대리인 공격 방지
    - 대상 검증 및 안전한 토큰 관리로 토큰 패스스루 방지
    - 암호화 바인딩 및 행동 분석 기반 세션 하이재킹 방지
  - **기업 보안 통합**: Azure Application Insights 모니터링, 위협 탐지 파이프라인, 공급망 보안
  - **구현 체크리스트**: 필수 및 권장 보안 통제 구분과 Microsoft 보안 생태계 이점 명확히 표시

### 문서 품질 및 표준 정렬
- **사양 참조**: 모든 참조를 최신 MCP 사양 2025-06-18로 업데이트
- **Microsoft 보안 생태계**: 전 보안 문서에 걸친 통합 가이드 강화
- **실용적 구현**: .NET, Java, Python의 상세 코드 예제 및 기업용 패턴 추가
- **리소스 구성**: 공식 문서, 보안 표준, 구현 가이드의 포괄적 분류
- **시각적 표시**: 필수 요구사항과 권장 실천 표시 명확화


#### 핵심 개념 (01-CoreConcepts/) - 완전 개편
- **프로토콜 버전 업데이트**: 최신 MCP 사양 2025-06-18 참조로 날짜 기반 버전 관리(YYYY-MM-DD 형식) 적용
- **아키텍처 정제**: Hosts, Clients, Servers 설명 업데이트로 최신 MCP 아키텍처 패턴 반영
  - Hosts는 이제 여러 MCP 클라이언트 연결을 조율하는 AI 애플리케이션으로 명확히 정의
  - Clients는 1:1 서버 관계를 유지하는 프로토콜 커넥터로 설명
  - Servers는 로컬 및 원격 배포 시나리오로 강화
- **프리미티브 재구성**: 서버와 클라이언트 프리미티브 전면 개편
  - 서버 프리미티브: 리소스(데이터 소스), 프롬프트(템플릿), 툴(실행 함수) 상세 설명 및 예제 포함
  - 클라이언트 프리미티브: 샘플링(LLM 완성), 추출(사용자 입력), 로깅(디버깅/모니터링)
  - 현재의 검색(`*/list`), 획득(`*/get`), 실행(`*/call`) 메서드 패턴 반영 업데이트
- **프로토콜 아키텍처**: 2계층 아키텍처 모델 도입
  - 데이터 계층: JSON-RPC 2.0 기반, 생명주기 관리 및 프리미티브 포함
  - 전송 계층: STDIO(로컬) 및 스트리머블 HTTP와 SSE(원격) 전송 메커니즘
- **보안 프레임워크**: 명시적 사용자 동의, 데이터 개인정보 보호, 툴 실행 안전, 전송 계층 보안 포함 포괄적 보안 원칙
- **통신 패턴**: 초기화, 검색, 실행 및 알림 흐름을 보여주는 프로토콜 메시지 업데이트
- **코드 예제**: 최신 MCP SDK 패턴 반영한 다중 언어(.NET, Java, Python, JavaScript) 예제 갱신

#### 보안 (02-Security/) - 전면적 보안 개편  
- **표준 정렬**: MCP 사양 2025-06-18 보안 요구사항과 완벽 정렬
- **인증 진화**: 맞춤 OAuth 서버에서 외부 ID 제공자 위임(Microsoft Entra ID)로 발전 문서화
- **AI 특화 위협 분석**: 최신 AI 공격 벡터에 대한 심층적 다룸
  - 실제 사례를 포함한 상세한 프롬프트 인젝션 공격 시나리오
  - 툴 중독 메커니즘 및 "러그 풀(rug pull)" 공격 패턴
  - 컨텍스트 윈도우 중독 및 모델 혼란 공격
- **Microsoft AI 보안 솔루션**: Microsoft 보안 생태계 포괄적 커버리지
  - 고급 탐지, 스포트라이트, 구분자 기술 포함 AI Prompt Shields
  - Azure Content Safety 통합 패턴
  - 공급망 보호를 위한 GitHub Advanced Security
- **고급 위협 완화**: 다음에 대한 상세 보안 통제
  - MCP 특유 공격 시나리오 및 암호학적 세션 ID 요구사항을 가진 세션 하이재킹
  - 명시적 동의 요구를 포함한 MCP 프록시 시나리오 혼란 대리인 문제
  - 필수 검증 통제가 포함된 토큰 패스스루 취약점
- **공급망 보안**: 기초 모델, 임베딩 서비스, 컨텍스트 제공자, 타사 API를 포함한 AI 공급망 범위 확장
- **기초 보안**: 제로 트러스트 아키텍처 및 Microsoft 보안 생태계 포함 기업 보안 패턴 강화 통합
- **리소스 구성**: 유형별(공식 문서, 표준, 연구, Microsoft 솔루션, 구현 가이드) 포괄적 리소스 링크 분류

### 문서 품질 개선
- **구조화된 학습 목표**: 구체적이고 실행 가능한 결과를 포함한 학습 목표 강화
- **상호 참조**: 보안 및 핵심 개념 주제 간 링크 추가
- **최신 정보**: 모든 날짜 참조 및 사양 링크를 최신 표준으로 업데이트
- **구현 가이드**: 두 섹션 전반에 걸쳐 구체적이고 실행 가능한 구현 지침 추가

## 2025년 7월 16일

### README 및 내비게이션 개선
- README.md에서 커리큘럼 내비게이션 완전 재설계
- `<details>` 태그 대신 접근성이 좋은 테이블 기반 포맷으로 교체
- 새로운 "alternative_layouts" 폴더에 대체 레이아웃 옵션 추가
- 카드 기반, 탭 스타일, 아코디언 스타일 내비게이션 예제 추가
- 최신 파일 모두 포함하도록 저장소 구조 섹션 업데이트
- 명확한 권장사항을 포함한 "이 커리큘럼 사용법" 섹션 강화
- MCP 사양 링크가 정확한 URL을 가리키도록 업데이트
- 커리큘럼 구조에 컨텍스트 엔지니어링 섹션(5.14) 추가

### 학습 가이드 업데이트
- 현재 저장소 구조에 맞게 학습 가이드 완전 개정
- MCP 클라이언트와 툴, 인기 MCP 서버에 대한 새로운 섹션 추가
- 모든 주제를 정확히 반영하도록 시각적 커리큘럼 맵 업데이트
- 전문 영역 전반을 다루도록 고급 주제 설명 강화
- 실제 예제를 반영하도록 사례 연구 섹션 업데이트
- 이 포괄적 변경 로그 추가

### 커뮤니티 기여 (06-CommunityContributions/)
- 이미지 생성용 MCP 서버에 관한 상세 정보 추가
- VSCode 내에서 Claude 사용법에 관한 포괄적 섹션 추가
- Cline 터미널 클라이언트 설정 및 사용 지침 추가
- 모든 인기 클라이언트 옵션을 포함하도록 MCP 클라이언트 섹션 업데이트
- 더 정확한 코드 샘플로 기여 예제 강화

### 고급 주제 (05-AdvancedTopics/)
- 일관된 명명으로 모든 전문 주제 폴더 구성
- 컨텍스트 엔지니어링 자료 및 예제 추가
- Foundry 에이전트 통합 문서 추가
- Entra ID 보안 통합 문서 강화

## 2025년 6월 11일

### 초기 생성
- MCP 초보자용 커리큘럼 첫 버전 출시
- 10개 주요 섹션의 기본 구조 생성
- 내비게이션을 위한 시각적 커리큘럼 맵 구현
- 다중 프로그래밍 언어의 초기 샘플 프로젝트 추가

### 시작하기 (03-GettingStarted/)
- 첫 서버 구현 예제 작성
- 클라이언트 개발 가이드 추가
- LLM 클라이언트 통합 지침 포함
- VS Code 통합 문서화 추가
- 서버-센트 이벤트(SSE) 서버 예제 구현

### 핵심 개념 (01-CoreConcepts/)
- 클라이언트-서버 아키텍처 상세 설명 추가
- 핵심 프로토콜 구성 요소 문서화
- MCP의 메시지 패턴 문서화

## 2025년 5월 23일

### 저장소 구조
- 기본 폴더 구조로 저장소 초기화
- 주요 섹션별 README 파일 생성
- 번역 인프라 설정
- 이미지 자산 및 다이어그램 추가

### 문서화
- 커리큘럼 개요를 포함한 초기 README.md 작성
- CODE_OF_CONDUCT.md 및 SECURITY.md 추가
- 지원 가이드가 포함된 SUPPORT.md 설정
- 예비 학습 가이드 구조 작성

## 2025년 4월 15일

### 계획 및 프레임워크
- MCP 초보자용 커리큘럼 초기 계획
- 학습 목표 및 대상 청중 정의
- 커리큘럼 10개 섹션 구조 개요
- 사례 연구 및 예제를 위한 개념적 프레임워크 개발
- 핵심 개념을 위한 초기 프로토타입 예제 작성

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->