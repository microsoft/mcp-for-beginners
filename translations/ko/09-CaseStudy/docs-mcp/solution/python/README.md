# 체인릿과 Microsoft Learn Docs MCP를 활용한 학습 계획 생성기

## 사전 요구 사항

- Python 3.8 이상
- pip (Python 패키지 관리자)
- Microsoft Learn Docs MCP 서버에 연결할 수 있는 인터넷 접속

## 설치 방법

1. 이 저장소를 클론하거나 프로젝트 파일을 다운로드합니다.
2. 필요한 종속성을 설치합니다:

   ```bash
   pip install -r requirements.txt
   ```

## 사용 방법

### 시나리오 1: Docs MCP에 간단한 쿼리 보내기
Docs MCP 서버에 연결하여 쿼리를 전송하고 결과를 출력하는 커맨드라인 클라이언트입니다.

1. 스크립트를 실행합니다:
   ```bash
   python scenario1.py
   ```
2. 프롬프트에 문서 관련 질문을 입력합니다.

### 시나리오 2: 학습 계획 생성기 (체인릿 웹 앱)
체인릿(Chainlit)을 사용하여 주제에 맞는 맞춤형 주간 학습 계획을 생성할 수 있는 웹 기반 인터페이스입니다.

1. 체인릿 앱을 시작합니다:
   ```bash
   chainlit run scenario2.py
   ```
2. 터미널에 제공된 로컬 URL(예: http://localhost:8000)을 브라우저에서 엽니다.
3. 채팅 창에 학습 주제와 학습 기간(예: "AI-900 자격증, 8주")을 입력합니다.
4. 앱이 주별 학습 계획과 관련 Microsoft Learn 문서 링크를 제공합니다.

**필요한 환경 변수:**

시나리오 2(체인릿 웹 앱과 Azure OpenAI 사용)를 실행하려면 `python` 디렉터리 내 `.env` 파일에 다음 환경 변수를 설정해야 합니다:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

앱 실행 전에 Azure OpenAI 리소스 정보를 입력하세요.

> [!TIP]
> [Azure AI Foundry](https://ai.azure.com/)를 사용하여 손쉽게 모델을 배포할 수 있습니다.

### 시나리오 3: VS Code에서 MCP 서버를 활용한 문서 검색

브라우저 탭을 전환하지 않고 VS Code 내에서 Microsoft Learn Docs를 검색할 수 있습니다. 이를 통해 다음과 같은 작업이 가능합니다:
- 코딩 환경을 벗어나지 않고 VS Code 내에서 문서를 검색하고 읽기
- 문서를 참조하고 README나 강의 파일에 링크 삽입
- GitHub Copilot과 MCP를 함께 사용하여 AI 기반 문서 작업 워크플로우 구현

**예시 사용 사례:**
- 강의나 프로젝트 문서를 작성하면서 README에 참조 링크를 빠르게 추가
- Copilot을 사용해 코드를 생성하고 MCP를 활용해 관련 문서를 즉시 찾아 인용
- 에디터 내에서 작업에 집중하며 생산성 향상

> [!IMPORTANT]
> 작업 공간에 유효한 [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) 설정 파일이 있어야 합니다 (위치: `.vscode/mcp.json`).

## 시나리오 2에서 체인릿을 사용하는 이유

체인릿(Chainlit)은 대화형 웹 애플리케이션을 구축하기 위한 현대적인 오픈소스 프레임워크입니다. Microsoft Learn Docs MCP 서버와 같은 백엔드 서비스에 연결되는 채팅 기반 사용자 인터페이스를 쉽게 만들 수 있습니다. 이 프로젝트는 체인릿을 활용하여 맞춤형 학습 계획을 실시간으로 생성하는 간단하고 직관적인 방법을 제공합니다. 체인릿을 통해 생산성과 학습을 향상시키는 채팅 기반 도구를 빠르게 구축하고 배포할 수 있습니다.

## 이 앱이 하는 일

사용자가 주제와 기간을 입력하면, 이 앱은 입력을 분석하여 Microsoft Learn Docs MCP 서버에서 관련 콘텐츠를 검색하고 이를 주별 계획으로 구성합니다. 각 주의 추천 학습 자료는 채팅 창에 표시되며, 이를 통해 학습 진행 상황을 쉽게 따라갈 수 있습니다. 이 통합 기능은 항상 최신의 관련 학습 리소스를 제공받을 수 있도록 보장합니다.

## 샘플 쿼리

채팅 창에서 다음 쿼리를 시도해 보세요:

- `AI-900 자격증, 8주`
- `Azure Functions 배우기, 4주`
- `Azure DevOps, 6주`
- `Azure 데이터 엔지니어링, 10주`
- `Microsoft 보안 기초, 5주`
- `Power Platform, 7주`
- `Azure AI 서비스, 12주`
- `클라우드 아키텍처, 9주`

이 예제들은 다양한 학습 목표와 기간에 맞춘 앱의 유연성을 보여줍니다.

## 참고 자료

- [체인릿 문서](https://docs.chainlit.io/)
- [MCP 문서](https://github.com/MicrosoftDocs/mcp)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.  