# 🚀 개발자 생산성을 혁신하는 10가지 Microsoft MCP 서버

## 🎯 이 가이드에서 배우게 될 내용

이 실용적인 가이드는 개발자가 AI 어시스턴트와 함께 작업하는 방식을 적극적으로 혁신하고 있는 10가지 Microsoft MCP 서버를 소개합니다. MCP 서버가 *할 수 있는* 기능을 단순히 설명하는 대신, Microsoft 및 그 외 현장에서 매일 개발 워크플로우에 실제로 변화를 만들고 있는 서버들을 보여 드립니다.

이 가이드의 각 서버는 실사용 사례와 개발자 피드백을 바탕으로 선정되었습니다. 각 서버가 무엇을 하는지뿐 아니라, 왜 중요한지, 그리고 여러분의 프로젝트에서 최대한 활용하는 방법도 알게 됩니다. MCP가 처음이든 기존 설정을 확장하려는 분이든, 이들 서버는 Microsoft 생태계에서 가장 실용적이고 영향력 있는 도구 중 일부입니다.

> **💡 빠른 시작 팁**
> 
> MCP가 처음인가요? 걱정 마세요! 이 가이드는 초보자도 쉽게 따라할 수 있도록 설계되었습니다. 개념을 단계별로 설명하고 있으며, 더 깊은 배경은 [MCP 소개](../00-Introduction/README.md)와 [핵심 개념](../01-CoreConcepts/README.md) 모듈을 참고하세요.

## 개요

이 포괄적인 가이드는 AI 어시스턴트 및 외부 도구와 상호작용하는 방식을 혁신하는 10가지 Microsoft MCP 서버를 탐구합니다. Azure 리소스 관리부터 문서 처리에 이르기까지, 이 서버들은 원활하고 생산적인 개발 워크플로우를 만들기 위한 Model Context Protocol의 힘을 보여줍니다.

## 학습 목표

이 가이드를 마치면 다음을 할 수 있습니다:
- MCP 서버가 어떻게 개발자 생산성을 높이는지 이해하기
- Microsoft의 가장 영향력 있는 MCP 서버 구현 사례 알아보기
- 각 서버의 실용적인 사용 사례 발견하기
- VS Code와 Visual Studio에서 이 서버를 설정하고 구성하는 방법 알기
- 더 넓은 MCP 생태계와 미래 방향 탐색하기

## 🔧 MCP 서버 이해하기: 초보자 가이드

### MCP 서버란 무엇인가?

Model Context Protocol(MCP)이 처음이라면, "MCP 서버가 정확히 무엇이고 왜 신경 써야 하지?"라고 궁금할 수 있습니다. 간단한 비유부터 시작해 보겠습니다.

MCP 서버는 AI 코딩 동반자(예: GitHub Copilot)가 외부 도구 및 서비스에 연결할 수 있도록 돕는 전문화된 어시스턴트와 같습니다. 날씨 앱, 내비게이션 앱, 은행 앱 등 각기 다른 작업을 위해 여러 앱을 사용하는 스마트폰처럼, MCP 서버는 AI 어시스턴트가 다양한 개발 도구와 서비스를 사용할 수 있게 합니다.

### MCP 서버가 해결하는 문제

MCP 서버가 없던 시절, 만약 다음 작업을 하려면:
- Azure 리소스 확인
- GitHub 이슈 생성
- 데이터베이스 질의
- 문서 검색

코딩을 멈추고, 브라우저를 열고, 해당 웹사이트로 이동해 수동으로 작업을 해야 했습니다. 이런 잦은 컨텍스트 전환은 흐름을 끊고 생산성을 저하합니다.

### MCP 서버가 개발 경험을 혁신하는 방법

MCP 서버를 사용하면 개발 환경(VS Code, Visual Studio 등) 안에 머물면서 AI 어시스턴트에게 작업을 요청할 수 있습니다. 예를 들어:

**기존 전통적 워크플로우 대신에:**
1. 코딩 중단
2. 브라우저 열기
3. Azure 포털 접속
4. 스토리지 계정 정보 조회
5. VS Code로 돌아오기
6. 코딩 재개

**이제는 이렇게 할 수 있습니다:**
1. AI에게 묻기: "내 Azure 스토리지 계정 상태 알려줘."
2. 받은 정보로 코딩 계속하기

### 초보자를 위한 주요 이점

#### 1. 🔄 **흐름 상태 유지**
- 여러 애플리케이션 간 전환 불필요
- 코딩에 집중 유지
- 다양한 도구 관리에 대한 정신적 부담 감소

#### 2. 🤖 **복잡한 명령 대신 자연어 사용**
- SQL 문법을 외우지 않고 필요한 데이터를 설명
- Azure CLI 명령 대신 원하는 목표 설명
- AI가 기술적 세부사항 처리, 논리에 집중

#### 3. 🔗 **여러 도구 연결하기**
- 다양한 서비스 결합해 강력한 워크플로우 생성
- 예: "최근 GitHub 이슈 가져와서 Azure DevOps 작업 항목 생성"
- 복잡한 스크립트 없이 자동화 구축

#### 4. 🌐 **커지는 생태계 접근**
- Microsoft, GitHub 등 회사에서 만든 서버 혜택
- 다양한 공급업체 도구를 자연스럽게 조합
- 여러 AI 어시스턴트 간 작동하는 표준화된 생태계 참여

#### 5. 🛠️ **실습을 통한 학습**
- 기본 제공 서버로 개념 이해 시작
- 익숙해지면 직접 서버 구축
- SDK와 문서 활용해 학습 지원

### 초보자를 위한 실제 예시

웹 개발이 처음이고 첫 프로젝트를 하고 있다고 가정합시다. MCP 서버가 어떻게 도움이 될까요?

**전통적 방법:**
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**MCP 서버 사용 시:**
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### 엔터프라이즈 표준의 이점

MCP는 업계 표준이 되어가고 있으며, 이는:
- <strong>일관성</strong>: 다양한 도구와 회사에서 유사한 경험 제공
- **상호 운용성**: 서로 다른 공급업체의 서버가 함께 작동
- **미래 대비**: 다양한 AI 어시스턴트 간 기술과 설정 이전 가능
- <strong>커뮤니티</strong>: 방대한 공유 지식과 리소스 생태계

### 시작하기: 배우게 될 내용

이 가이드에서는 모든 수준의 개발자에게 특히 유용한 10가지 Microsoft MCP 서버를 살펴봅니다. 각 서버는:
- 일반적인 개발 문제 해결
- 반복 작업 감소
- 코드 품질 향상
- 학습 기회 증대

> **💡 학습 팁**
> 
> MCP가 처음이라면, 먼저 [MCP 소개](../00-Introduction/README.md)와 [핵심 개념](../01-CoreConcepts/README.md) 모듈을 시작하세요. 그 다음 이곳으로 돌아와 실제 Microsoft 도구에서 이 개념들을 확인하세요.
>
> MCP 중요성에 대한 추가 배경은 Maria Naggaga의 게시물 [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps)를 참고하세요.

## VS Code와 Visual Studio에서 MCP 시작하기 🚀

Visual Studio Code나 Visual Studio 2022에서 GitHub Copilot과 함께 이 MCP 서버를 설정하는 것은 간단합니다.

### VS Code 설정

VS Code 기본 과정은 다음과 같습니다:

1. **에이전트 모드 활성화**: VS Code에서 Copilot Chat 창을 에이전트 모드로 전환
2. **MCP 서버 구성**: VS Code settings.json 파일에 서버 구성 추가
3. **서버 시작**: 사용하려는 서버마다 "시작" 버튼 클릭
4. **도구 선택**: 현재 세션에서 활성화할 MCP 서버 선택

자세한 설정 지침은 [VS Code MCP 문서](https://code.visualstudio.com/docs/copilot/copilot-mcp)를 참조하세요.

> **💡 전문가 팁: MCP 서버를 프로처럼 관리하세요!**
> 
> VS Code 확장 보기에는 [설치된 MCP 서버 관리를 위한 새로운 UI](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)가 포함되어 있습니다! 간단하고 명확한 인터페이스로 설치된 MCP 서버를 신속히 시작, 중지, 관리할 수 있습니다. 한번 써보세요!

### Visual Studio 2022 설정

Visual Studio 2022 (버전 17.14 이상)의 경우:

1. **에이전트 모드 활성화**: GitHub Copilot Chat 창에서 "Ask" 드롭다운을 클릭하고 "Agent" 선택
2. **구성 파일 생성**: 솔루션 디렉터리에 `.mcp.json` 파일 생성 (권장 위치: `<SOLUTIONDIR>\.mcp.json`)
3. **서버 구성**: 표준 MCP 형식으로 MCP 서버 구성 추가
4. **도구 승인**: 요청 시 적절한 범위 권한으로 사용할 도구 승인

자세한 Visual Studio 설정 지침은 [Visual Studio MCP 문서](https://learn.microsoft.com/visualstudio/ide/mcp-servers)를 참고하세요.

각 MCP 서버는 자체 구성 요구 사항(연결 문자열, 인증 등)이 있지만, 두 IDE 모두에서 설정 패턴은 일관됩니다.

## Microsoft MCP 서버에서 배운 교훈 🛠️

### 1. 📚 Microsoft Learn Docs MCP 서버

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

<strong>기능</strong>: Microsoft Learn Docs MCP 서버는 Model Context Protocol을 통해 AI 어시스턴트에 공식 Microsoft 문서에 대한 실시간 접근을 제공하는 클라우드 호스팅 서비스입니다. `https://learn.microsoft.com/api/mcp`에 연결하며 Microsoft Learn, Azure 문서, Microsoft 365 문서 등 공식 Microsoft 자료를 의미 기반 검색할 수 있습니다.

**유용한 이유**: 단순히 "문서" 같아 보여도, 이 서버는 Microsoft 기술을 사용하는 모든 개발자에게 매우 중요합니다. .NET 개발자들이 AI 코딩 어시스턴트가 최신 .NET 및 C# 릴리스에 뒤쳐진다는 불만이 많았는데, Microsoft Learn Docs MCP 서버는 최신 문서, API 참조, 모범 사례를 실시간으로 제공해 이 문제를 해결합니다. 최신 Azure SDK, C# 13 신규 기능, 선진 Aspire 패턴 작업 시 AI 어시스턴트가 정확하고 최신 정보를 토대로 코드를 생성하도록 돕습니다.

**실제 사용 사례**: "공식 Microsoft Learn 문서에 따른 Azure 컨테이너 앱 생성 az cli 명령어가 뭐야?" 또는 "ASP.NET Core에서 의존성 주입으로 Entity Framework를 어떻게 구성해?" "이 코드가 Microsoft Learn 문서의 성능 권장 사항에 맞는지 검토해줘." 이 서버는 고급 의미 기반 검색으로 Microsoft Learn, Azure 문서, Microsoft 365 문서 내 맥락상 가장 관련성 높은 정보를 최대 10개 고품질 콘텐츠 조각(제목과 URL 포함)으로 제공합니다. 최신 문서가 출판되는 즉시 접근 가능합니다.

**주요 예시**: 서버는 Microsoft 공식 기술 문서에 대해 의미 기반 검색을 수행하는 `microsoft_docs_search` 도구를 제공합니다. 구성 후에는 "ASP.NET Core에서 JWT 인증을 어떻게 구현하지?" 같은 질문에 공식 출처 링크와 함께 상세한 답변을 받을 수 있습니다. 이 검색 품질은 컨텍스트를 이해하여 Azure 관련 "컨테이너"는 Azure Container Instances 문서를, .NET 컨텍스트에서는 관련 C# 컬렉션 정보를 반환하는 등 탁월합니다.

이 기능은 빠르게 변화하거나 최근에 업데이트된 라이브러리 및 사용 사례에 특히 유용합니다. 최근 프로젝트에서 Aspire와 Microsoft.Extensions.AI 최신 릴리스 기능을 활용할 때 Microsoft Learn Docs MCP 서버를 포함하여 API 문서뿐 아니라 막 게시된 안내서와 가이드를 효과적으로 활용할 수 있었습니다.

> **💡 전문가 팁**
> 
> 도구 친화적 모델도 MCP 도구 사용 독려가 필요합니다! 예를 들어 시스템 프롬프트나 [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot)를 추가해, "microsoft.docs.mcp에 접근할 수 있습니다 – C#, Azure, ASP.NET Core, Entity Framework 같은 Microsoft 기술 관련 질문 처리 시 최신 공식 문서를 검색하는 데 이 도구를 사용하세요."라고 안내하세요.
>
> 실제 활용 훌륭한 예로는 Awesome GitHub Copilot 저장소의 [C# .NET Janitor 채팅 모드](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md)를 살펴보세요. 이 모드는 최신 패턴과 모범 사례를 이용해 C# 코드를 정리하고 현대화하는 데 Microsoft Learn Docs MCP 서버를 적극 활용합니다.
### 2. ☁️ Azure MCP 서버


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

<strong>기능</strong>: Azure MCP 서버는 전체 Azure 생태계를 AI 워크플로우에 통합하는 15개 이상의 전문화된 Azure 서비스 커넥터의 종합 세트입니다. 단일 서버가 아니라 리소스 관리, 데이터베이스 연결(PostgreSQL, SQL Server), KQL을 활용한 Azure Monitor 로그 분석, Cosmos DB 통합 등 강력한 기능들을 포함한 컬렉션입니다.

**유용한 이유**: Azure 리소스 관리뿐만 아니라, 이 서버는 Azure SDK 작업 시 코드 품질을 크게 향상시킵니다. 에이전트 모드에서 Azure MCP를 사용하면 단순히 코드를 작성하는 것을 넘어 최신 인증 패턴, 오류 처리 모범 사례를 따르고 최신 SDK 기능을 활용하는 *더 나은* Azure 코드를 작성할 수 있습니다. 단순히 동작하는 일반 코드를 받는 대신, Azure가 권장하는 패턴을 따르는 프로덕션용 코드를 얻을 수 있습니다.

**주요 모듈**:
- **🗄️ 데이터베이스 커넥터**: Azure Database for PostgreSQL 및 SQL Server에 자연어 직접 접근
- **📊 Azure Monitor**: KQL 기반 로그 분석 및 운영 인사이트
- **🌐 리소스 관리**: 완전한 Azure 리소스 라이프사이클 관리
- **🔐 인증**: DefaultAzureCredential 및 관리형 ID 패턴
- **📦 스토리지 서비스**: Blob Storage, Queue Storage, Table Storage 작업
- **🚀 컨테이너 서비스**: Azure Container Apps, Container Instances, AKS 관리
- **기타 여러 전문 커넥터 포함**

**실제 사용 예**: "내 Azure 저장소 계정 목록 보여줘", "지난 시간 내 내 Log Analytics 작업공간의 오류 쿼리해줘", "Node.js로 적절한 인증을 사용하는 Azure 애플리케이션 작성 도와줘"

**전체 데모 시나리오**: Azure MCP와 VS Code의 GitHub Copilot for Azure 확장 기능을 결합한 강력한 예시입니다. 둘 다 설치된 상태에서 다음을 입력하면:

> "DefaultAzureCredential 인증을 사용해 Azure Blob Storage에 파일을 업로드하는 Python 스크립트를 만들어줘. 스크립트는 'mycompanystorage'라는 내 Azure 저장소 계정에 연결하고, 'documents' 컨테이너에 업로드하며, 현재 타임스탬프가 포함된 테스트 파일을 생성해 업로드하고, 오류를 우아하게 처리하며 유익한 출력을 제공해야 해. 인증 및 오류 처리에 대해 Azure 모범 사례를 따르고, DefaultAzureCredential 인증이 작동하는 방법에 대한 주석을 포함하며, 함수를 적절히 구조화하고 문서화해서 스크립트를 잘 작성해줘."

Azure MCP 서버가 생성하는 완전한 프로덕션 준비 Python 스크립트는 다음과 같습니다:
- 최신 Azure Blob Storage SDK를 사용하며 적절한 비동기 패턴 적용
- DefaultAzureCredential의 포괄적인 폴백 체인 설명 포함 구현
- 특정 Azure 예외 유형을 활용하는 견고한 오류 처리 포함
- 리소스 관리와 연결 처리에 대한 Azure SDK 모범 사례 준수
- 상세한 로깅과 유익한 콘솔 출력 제공
- 함수, 문서화, 타입 힌트가 포함된 적절히 구조화된 스크립트 작성

주목할 점은 Azure MCP가 없으면 최신 Azure 패턴을 따르지 않는 일반 블롭 스토리지 코드가 생성될 수 있다는 것입니다. Azure MCP를 사용하면 최신 인증 방식 활용, Azure 특정 오류 시나리오 처리, Microsoft 권장 프로덕션 애플리케이션 관행 준수 코드를 받게 됩니다.

**특징적인 예**: `az` 및 `azd` CLI 명령어를 기억하는 게 어려워 항상 먼저 문법을 찾아보고 명령을 실행하는 두 단계 과정을 거칩니다. CLI 문법을 기억하지 못한다고 인정하기 싫어 포털에 접속해 여기저기 클릭해서 작업을 하곤 했습니다. 원하는 걸 그냥 설명할 수 있다는 게 놀랍고, IDE를 떠나지 않고도 할 수 있다는 게 더 좋습니다!

시작하는 데 도움이 될 [Azure MCP 저장소](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server)의 훌륭한 사용 사례 목록이 있습니다. 종합적인 설정 가이드와 고급 구성 옵션은 [공식 Azure MCP 문서](https://learn.microsoft.com/azure/developer/azure-mcp-server/)를 참고하세요.

### 3. 🐙 GitHub MCP 서버

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

<strong>기능</strong>: 공식 GitHub MCP 서버는 호스팅된 원격 접근 및 로컬 Docker 배포 옵션을 제공하여 GitHub 전체 생태계와 원활하게 통합합니다. 단순한 저장소 작업이 아니라 GitHub Actions 관리, 풀 리퀘스트 워크플로우, 이슈 추적, 보안 스캔, 알림, 고급 자동화 기능을 포함하는 종합 도구입니다.

**유용한 이유**: VS Code와 GitHub.com을 오가며 프로젝트 관리, 코드 리뷰, CI/CD 모니터링을 하는 대신 자연어 명령으로 모든 작업을 수행하며 개발에 집중할 수 있게 GitHub와 상호작용하는 방식을 바꿉니다.

> **ℹ️ 참고: 다양한 '에이전트' 유형**
> 
> GitHub MCP 서버를 GitHub의 코딩 에이전트(자동화된 코딩 작업을 위한 이슈 지정 AI 에이전트)와 혼동하지 마세요. GitHub MCP 서버는 VS Code 에이전트 모드 내에서 GitHub API 통합을 제공하며, 코딩 에이전트는 지정받은 GitHub 이슈에 대해 풀 리퀘스트를 생성하는 별도 기능입니다.

**주요 기능**:
- **⚙️ GitHub Actions**: 완전한 CI/CD 파이프라인 관리, 워크플로우 모니터링, 아티팩트 관리
- **🔀 풀 리퀘스트**: PR 생성, 리뷰, 병합 및 상태 추적 전반 관리
- **🐛 이슈**: 이슈 라이프사이클 관리, 댓글, 라벨링, 담당자 지정
- **🔒 보안**: 코드 스캔 경고, 비밀 탐지, Dependabot 통합
- **🔔 알림**: 스마트 알림 관리 및 저장소 구독 제어
- **📁 저장소 관리**: 파일 작업, 브랜치 관리, 저장소 행정
- **👥 협업**: 사용자 및 조직 검색, 팀 관리, 접근 제어

**실제 사용 예**: "내 기능 브랜치에서 풀 리퀘스트 생성해줘", "이번 주 실패한 CI 실행 모두 보여줘", "내 저장소의 열려 있는 보안 경고 알려줘", "내가 담당인 모든 조직별 이슈 찾아줘"

**전체 데모 시나리오**: GitHub MCP 서버 기능을 보여주는 강력한 워크플로우 예시입니다:

> "스프린트 리뷰 준비가 필요해. 이번 주 내가 생성한 모든 풀 리퀘스트 보여주고, CI/CD 파이프라인 상태 확인하며, 해결해야 할 보안 경고 요약 만들어 줘. ‘feature’ 라벨이 붙은 병합된 PR 기반으로 릴리스 노트 초안 작성도 도와줘."

GitHub MCP 서버는 다음을 수행합니다:
- 최근 풀 리퀘스트의 상세 상태 정보 조회
- 워크플로우 실행 분석 및 실패나 성능 문제 하이라이트
- 보안 스캔 결과 수집 및 중요 경고 우선순위 지정
- 병합된 PR에서 정보 추출한 종합 릴리스 노트 생성
- 스프린트 계획과 릴리스 준비를 위한 실행 가능한 다음 단계 제공

**특징적인 예**: 코드 리뷰 워크플로우에 이 기능을 좋아합니다. VS Code, GitHub 알림, PR 페이지 사이를 오가지 않고 "내 검토를 기다리는 모든 PR 보여줘"라고 말한 뒤 "PR #123에 인증 메서드 오류 처리에 관한 댓글 달아줘"라고 요청합니다. 서버가 GitHub API 호출을 다루고 대화 맥락을 유지하며 더 건설적인 리뷰 댓글 작성까지 도와줍니다.

**인증 옵션**: OAuth(VS Code 내 원활함) 및 개인 액세스 토큰 모두 지원하며 필요한 GitHub 기능만 활성화할 수 있는 구성 가능한 도구 세트를 제공합니다. 즉시 설정 가능한 원격 호스팅 서비스로 실행하거나 완전한 제어를 위한 로컬 Docker 실행도 가능합니다.

> **💡 전문가 팁**
> 
> MCP 서버 설정에서 `--toolsets` 매개변수를 구성해 필요한 도구 세트만 활성화하면 컨텍스트 크기를 줄이고 AI 도구 선택을 향상할 수 있습니다. 예를 들어 코어 개발 워크플로우에는 `"--toolsets", "repos,issues,pull_requests,actions"`를, 주로 GitHub 모니터링 기능 원할 때는 `"--toolsets", "notifications, security"`를 추가하세요.
### 4. 🔄 Azure DevOps MCP 서버

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

<strong>기능</strong>: Azure DevOps 서비스에 연결하여 종합 프로젝트 관리, 작업 항목 추적, 빌드 파이프라인 관리, 저장소 작업을 지원합니다.

**유용한 이유**: 팀이 Azure DevOps를 주요 DevOps 플랫폼으로 사용할 경우, 이 MCP 서버는 개발 환경과 Azure DevOps 웹 인터페이스 간의 끊임없는 탭 전환을 없애줍니다. AI 어시스턴트를 통해 작업 항목 관리, 빌드 상태 확인, 저장소 쿼리, 프로젝트 관리 업무를 직접 처리할 수 있습니다.

**실제 사용 예**: "WebApp 프로젝트의 현재 스프린트 내 활성 작업 항목 모두 보여줘", "방금 찾은 로그인 문제에 대한 버그 리포트 생성해줘", "빌드 파이프라인 상태 확인하고 최근 실패 사례 보여줘"

**특징적인 예**: 개발 환경을 떠나지 않고 간단한 쿼리로 팀의 현재 스프린트 상태를 쉽게 확인할 수 있습니다. 예를 들어 "WebApp 프로젝트 현재 스프린트의 활성 작업 항목 모두 보여줘" 또는 "방금 찾은 로그인 문제 버그 리포트 생성해줘" 같은 식입니다.

### 5. 📝 MarkItDown MCP 서버


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**기능 설명**: MarkItDown은 다양한 파일 형식을 고품질 Markdown으로 변환하는 종합 문서 변환 서버로, LLM 소모 및 텍스트 분석 워크플로우에 최적화되어 있습니다.

**유용한 이유**: 현대 문서 작업에 필수적입니다! MarkItDown은 헤딩, 목록, 표, 링크 같은 중요한 문서 구조를 보존하면서 광범위한 파일 형식을 처리합니다. 단순 텍스트 추출 도구와 달리 AI 처리와 사람이 읽기 모두에 유용한 의미 체계와 서식을 유지하는 데 중점을 둡니다.

**지원하는 파일 형식**:
- **오피스 문서**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **미디어 파일**: 이미지 (EXIF 메타데이터 및 OCR 포함), 오디오 (EXIF 메타데이터 및 음성 전사 포함)
- **웹 콘텐츠**: HTML, RSS 피드, YouTube URL, 위키피디아 페이지
- **데이터 형식**: CSV, JSON, XML, ZIP 파일 (재귀적으로 내용 처리)
- **출판 형식**: EPub, 주피터 노트북 (.ipynb)
- <strong>이메일</strong>: Outlook 메시지 (.msg)
- <strong>고급</strong>: 향상된 PDF 처리를 위한 Azure Document Intelligence 통합

**고급 기능**: MarkItDown은 OpenAI 클라이언트가 제공될 경우 LLM 기반 이미지 설명, 향상된 PDF 처리를 위한 Azure Document Intelligence, 음성 콘텐츠 전사를 지원하며, 추가 파일 형식 확장을 위한 플러그인 시스템도 갖추고 있습니다.

**실제 사용 사례**: "이 PowerPoint 프레젠테이션을 문서 사이트용 Markdown으로 변환", "적절한 헤딩 구조를 가진 PDF에서 텍스트 추출", "이 Excel 스프레드시트를 읽기 쉬운 표 형식으로 변환"

**대표 예시**: [MarkItDown 문서](https://github.com/microsoft/markitdown#why-markdown)에서 인용:

> Markdown은 최소한의 마크업이나 서식으로 평문에 매우 가깝지만 중요한 문서 구조를 표현할 수 있습니다. OpenAI의 GPT-4o 같은 주류 LLM은 본질적으로 Markdown을 “이해”하며 흔히 무의식적으로 응답에 Markdown을 포함합니다. 이는 방대한 Markdown 형식의 텍스트 교육을 받았음을 시사하며, 부수적인 이점으로 Markdown 규약은 토큰 효율성도 매우 높습니다.

MarkItDown은 문서 구조를 잘 보존하는 데 탁월하며, 이는 AI 워크플로우에 중요합니다. 예를 들어 파워포인트 변환 시 슬라이드 구성에 맞는 헤딩을 유지하고, 표를 Markdown 표로 추출하며, 이미지에 대체 텍스트를 포함하고, 발표자 노트도 처리합니다. 차트는 읽기 쉬운 데이터 표로 변환되고, 결과 Markdown은 원본 프레젠테이션의 논리적 흐름을 유지합니다. 이는 프레젠테이션 콘텐츠를 AI 시스템에 전달하거나 기존 슬라이드로 문서화할 때 완벽합니다.
### 6. 🗃️ SQL Server MCP 서버

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**기능 설명**: SQL Server 데이터베이스(온프레미스, Azure SQL, 또는 Fabric)에 대한 대화형 접근 제공

**유용한 이유**: PostgreSQL 서버와 유사하지만 Microsoft SQL 생태계용입니다. 간단한 연결 문자열로 연결하여 자연어로 쿼리할 수 있어 문맥 전환이 필요 없습니다!

**실제 사용 사례**: "최근 30일 내에 이행되지 않은 모든 주문을 찾기"가 적절한 SQL 쿼리로 번역되어 형식화된 결과를 반환합니다

**대표 예시**: 데이터베이스 연결 설정 후 즉시 데이터와 대화할 수 있습니다. 블로그 글에서는 간단한 질문 "어떤 데이터베이스에 연결되어 있나요?"를 통해 보여줍니다. MCP 서버는 적합한 데이터베이스 도구를 호출해 SQL Server 인스턴스와 연결하고 현재 데이터베이스 연결 세부정보를 반환합니다—SQL 한 줄도 작성하지 않고요. 서버는 스키마 관리부터 데이터 조작까지 자연어 프롬프트를 통한 포괄적인 데이터베이스 작업을 지원합니다. VS Code와 Claude Desktop을 사용한 완전한 설정 지침 및 구성 예제는 [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/)를 참조하세요.


### 7. 🎭 Playwright MCP 서버

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**기능 설명**: AI 에이전트가 웹 페이지와 상호작용하여 테스트 및 자동화를 수행할 수 있게 함

> **ℹ️ GitHub Copilot 구동**
> 
> Playwright MCP 서버는 GitHub Copilot의 코딩 에이전트를 구동하여 웹 브라우징 기능을 제공합니다! [이 기능에 대해 더 알아보기](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**유용한 이유**: 자연어 설명에 기반한 자동화 테스트에 완벽합니다. AI가 웹사이트를 탐색하고, 폼을 작성하며, 구조화된 접근성 스냅샷을 통해 데이터를 추출할 수 있어 매우 강력합니다!

**실제 사용 사례**: "로그인 흐름 테스트하고 대시보드가 올바르게 로드되는지 확인" 또는 "제품 검색 테스트를 생성하고 결과 페이지를 검증"—모두 애플리케이션 소스 코드 없이 가능

**대표 예시**: 제 동료 Debbie O'Brien은 Playwright MCP 서버로 놀라운 작업을 하고 있습니다! 예를 들어, 그녀는 애플리케이션 소스 코드 접근 없이도 완전한 Playwright 테스트를 생성하는 방법을 최근 보여줬습니다. 그녀의 시나리오에서 Copilot에게 영화 검색 앱에 대한 테스트를 생성하라고 요청했는데: 사이트 방문, "Garfield" 검색, 결과에서 영화 존재 확인. MCP는 브라우저 세션을 시작하고 DOM 스냅샷으로 페이지 구조를 탐색하며 올바른 선택자를 찾아 첫 실행에서 통과하는 완전 작동하는 TypeScript 테스트를 생성했습니다.

이 기능의 강력한 점은 자연어 지시와 실행 가능한 테스트 코드 간의 간극을 메워준다는 점입니다. 전통적인 방식은 수동 테스트 작성이나 코드베이스 접근이 필요하지만, Playwright MCP를 사용하면 코드 접근 불가한 외부 사이트, 클라이언트 앱, 또는 블랙박스 테스트 시나리오까지 테스트할 수 있습니다.


### 8. 💻 Dev Box MCP 서버

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**기능 설명**: 자연어를 통해 Microsoft Dev Box 환경을 관리

**유용한 이유**: 개발 환경 관리를 크게 단순화합니다! 구체적인 명령을 기억하지 않고도 개발 환경을 생성, 구성, 관리할 수 있습니다.

**실제 사용 사례**: "최신 .NET SDK로 새 Dev Box를 설정하고 프로젝트에 맞게 구성", "내 개발 환경 전체 상태 확인", "팀 발표용 표준화된 데모 환경 생성"

**대표 예시**: 저는 개인 개발에 Dev Box를 많이 사용합니다. 제게 인사이트를 준 순간은 James Montemagno가 Dev Box가 회의 데모에 얼마나 좋은지 설명해주었을 때입니다. 회의나 호텔, 비행기 와이파이 상황에 상관없이 빠른 이더넷 연결을 제공하기 때문입니다. 실제로 저는 최근 브뤼헤에서 앤트워프로 버스를 타고 이동하며 전화 핫스팟에 노트북을 연결해 회의 데모 연습을 했습니다! 앞으로는 여러 개발 환경 관리 및 표준화된 데모 환경 구축에 좀 더 집중할 예정입니다. 고객 및 동료들로부터 많이 듣는 다른 사용 사례는 미리 구성된 개발 환경용 Dev Box 사용입니다. 두 경우 모두 MCP를 사용해 Dev Box를 구성 및 관리함으로써 자연어 상호작용을 하면서 개발 환경을 유지할 수 있습니다.

### 9. 🤖 Microsoft Foundry MCP 서버


[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**기능 소개**: Microsoft Foundry MCP 서버는 모델 카탈로그, 배포 관리, Azure AI Search를 이용한 지식 색인 및 평가 도구 등 Azure의 AI 생태계에 대한 포괄적인 접근을 개발자에게 제공합니다. 이 실험적 서버는 AI 개발과 Azure의 강력한 AI 인프라 간의 격차를 연결하여 AI 애플리케이션을 더 쉽게 구축, 배포 및 평가할 수 있도록 합니다.

**유용한 이유**: 이 서버는 엔터프라이즈급 AI 기능을 개발 워크플로에 직접 통합하여 Azure AI 서비스 사용 방식을 혁신합니다. Azure 포털, 문서, IDE 간을 전환하는 대신 자연어 명령으로 모델 탐색, 서비스 배포, 지식 베이스 관리 및 AI 성능 평가가 가능합니다. 특히 RAG(검색 보강 생성) 애플리케이션을 구축하거나 다중 모델 배포를 관리하거나 종합적인 AI 평가 파이프라인을 구현하는 개발자에게 매우 유용합니다.

**주요 개발자 기능**:
- **🔍 모델 탐색 및 배포**: Microsoft Foundry의 모델 카탈로그를 탐색하고 코드 샘플과 함께 자세한 모델 정보를 얻은 후 Azure AI 서비스에 모델 배포
- **📚 지식 관리**: Azure AI Search 인덱스 생성 및 관리, 문서 추가, 인덱서 구성, 정교한 RAG 시스템 구축
- **⚡ AI 에이전트 통합**: Azure AI 에이전트와 연결, 기존 에이전트 쿼리, 운영 환경에서 에이전트 성능 평가
- **📊 평가 프레임워크**: 종합적인 텍스트 및 에이전트 평가 실행, 마크다운 보고서 생성, AI 애플리케이션 품질 보증 구현
- **🚀 프로토타이핑 도구**: GitHub 기반 프로토타이핑 설정 안내 및 Microsoft Foundry Labs에서 최신 연구 모델 접근

**실제 개발자 활용 사례**: "내 애플리케이션에 Phi-4 모델을 Azure AI 서비스에 배포", "문서 기반 RAG 시스템용 새 검색 인덱스 생성", "내 에이전트 응답을 품질 지표에 따라 평가", "복잡한 분석 작업에 최적의 추론 모델 찾기"

**전체 데모 시나리오**: 강력한 AI 개발 워크플로 예시:

> "고객 지원 에이전트를 구축 중입니다. 카탈로그에서 좋은 추론 모델을 찾아 Azure AI 서비스에 배포하고, 문서에서 지식 베이스를 만들며, 응답 품질을 테스트할 평가 프레임워크를 설정한 후, 테스트용 GitHub 토큰을 이용한 통합 프로토타입을 도와주세요."

Microsoft Foundry MCP 서버는 다음을 수행합니다:
- 요구사항에 맞는 최적의 추론 모델을 추천하기 위해 모델 카탈로그 쿼리
- 선호하는 Azure 지역에 맞는 배포 명령 및 할당량 정보 제공
- 문서용 적절한 스키마를 갖춘 Azure AI Search 인덱스 설정
- 품질 지표 및 안전 검사로 평가 파이프라인 구성
- 즉시 테스트 가능한 GitHub 인증 프로토타이핑 코드 생성
- 특정 기술 스택에 맞춘 종합 설치 가이드 제공

**특별 사례**: 개발자로서 다양한 LLM 모델을 따라잡기 어려웠습니다. 몇 가지 주요 모델만 알고 있었지만 생산성 및 효율성 향상을 놓치고 있다는 느낌이 들었고, 토큰과 할당량 관리는 스트레스와 어려움이 많았습니다. 적합한 작업에 맞는 모델을 선택하는지, 예산을 비효율적으로 쓰고 있는지 늘 걱정했습니다. 이 MCP 서버를 팀원들과 MCP 서버 추천 관련 이야기를 하다가 James Montemagno로부터 처음 듣고 사용해 보게 되어 기대됩니다! 모델 탐색 기능은 평소 접하지 못했던 최적화된 모델을 찾고 싶은 저 같은 사람에게 특히 인상적입니다. 평가 프레임워크는 단순히 새로 시도하는 것이 아니라 실제로 더 나은 결과를 얻고 있는지 검증하는 데 도움이 될 것입니다.

> **ℹ️ 실험적 상태**
> 
> 이 MCP 서버는 실험 단계이며 활발히 개발 중입니다. 기능과 API가 변경될 수 있습니다. Azure AI 기능 탐색과 프로토타입 제작에 적합하지만, 운영 환경에서는 안정성 요구 사항을 검증해야 합니다.
### 10. 🏢 Microsoft 365 Agents Toolkit MCP 서버

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**기능 소개**: Microsoft 365 및 Microsoft 365 Copilot과 통합된 AI 에이전트 및 애플리케이션을 구축하기 위한 필수 도구를 개발자에게 제공합니다. 여기에는 스키마 검증, 샘플 코드 검색, 문제 해결 지원이 포함됩니다.

**유용한 이유**: Microsoft 365 및 Copilot 개발은 복잡한 매니페스트 스키마와 특정 개발 패턴을 요구합니다. 이 MCP 서버는 필수 개발 리소스를 코드 환경에 직접 가져와 스키마를 검증하고, 샘플 코드를 찾으며, 자주 겪는 문제를 문서를 참고하지 않고도 해결할 수 있도록 도와줍니다.

**실제 활용 사례**: "내 선언적 에이전트 매니페스트를 검증하고 스키마 오류를 수정해 주세요", "Microsoft Graph API 플러그인 구현 샘플 코드를 보여 주세요", "Teams 앱 인증 문제를 해결하는 데 도움을 주세요"

**특별 사례**: Build 행사에서 M365 Agents 이야기를 하다가 친구 John Miller에게 연락했는데 이 MCP를 추천받았습니다. M365 Agents 초보 개발자에게 유용할 것 같습니다. 이는 문서에 파묻히지 않고 바로 시작할 수 있는 템플릿, 샘플 코드, 스캐폴딩을 제공하기 때문입니다. 특히 매니페스트 구조 오류를 방지하는 스키마 검증 기능이 몇 시간의 디버깅 시간을 줄여 줄 것 같습니다.

> **💡 팁**
> 
> 이 서버를 Microsoft Learn Docs MCP 서버와 함께 사용하여 M365 개발을 종합적으로 지원하세요 – 공식 문서를 제공하는 서버와 실제 개발 도구 및 문제 해결 지원을 제공하는 서버가 함께 작동합니다.


## 다음 단계는? 🔮

## 📋 결론

모델 컨텍스트 프로토콜(MCP)은 개발자가 AI 어시스턴트 및 외부 도구와 상호작용하는 방식을 변화시키고 있습니다. 이 10개의 Microsoft MCP 서버는 표준화된 AI 통합의 힘을 보여주며, 개발자가 강력한 외부 기능에 접근하면서도 흐름을 유지할 수 있는 원활한 워크플로를 가능하게 합니다.

Azure 생태계의 광범위한 통합부터 브라우저 자동화를 위한 Playwright, 문서 처리를 위한 MarkItDown과 같은 특화 도구에 이르기까지, 이 서버들은 다양한 개발 시나리오에서 MCP가 생산성을 향상시킬 수 있음을 보여줍니다. 표준화된 프로토콜은 이 도구들이 원활하게 함께 작동하여 통합된 개발 경험을 제공합니다.

MCP 생태계가 계속 발전함에 따라, 커뮤니티에 참여하고 새로운 서버를 탐색하며 맞춤형 솔루션을 구축하는 것이 개발 생산성을 극대화하는 데 중요합니다. MCP의 개방형 표준 특성 덕분에 여러 공급업체의 도구를 혼합하여 특정 요구에 완벽한 워크플로를 만들 수 있습니다.

## 🔗 추가 리소스

- [공식 Microsoft MCP 저장소](https://github.com/microsoft/mcp)
- [MCP 커뮤니티 및 문서](https://modelcontextprotocol.io/introduction)
- [VS Code MCP 문서](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP 문서](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP 문서](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP 이벤트](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot 커스터마이제이션](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days 라이브 7월 29일/30일 또는 온디맨드 시청](https://aka.ms/mcpdevdays)

## 🎯 연습 문제

1. **설치 및 구성**: VS Code 환경에 MCP 서버 중 하나를 설치하고 기본 기능을 테스트하세요.
2. **워크플로 통합**: 세 가지 이상의 MCP 서버를 결합한 개발 워크플로를 설계하세요.
3. **맞춤형 서버 기획**: 일상 개발 작업 중 맞춤형 MCP 서버가 도움이 될 작업을 식별하고 사양을 만드세요.
4. **성능 분석**: MCP 서버 사용 시와 전통적 방법으로 일반 개발 작업 수행 시의 효율성을 비교하세요.
5. **보안 평가**: MCP 서버 사용 시 개발 환경에서의 보안 영향을 평가하고 최선의 실천 방안을 제안하세요.


다음: [Best Practices](../08-BestPractices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->