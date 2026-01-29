# 🚀 개발자 생산성을 혁신하는 10가지 Microsoft MCP 서버

## 🎯 이 가이드에서 배우게 될 내용

이 실용적인 가이드는 AI 어시스턴트와 함께 개발자들이 일하는 방식을 적극적으로 변화시키고 있는 10가지 Microsoft MCP 서버를 소개합니다. MCP 서버가 *할 수 있는* 기능을 단순히 설명하는 대신, Microsoft와 그 외 여러 곳에서 실제 개발 워크플로우에 변화를 가져오고 있는 서버들을 보여드립니다.

이 가이드에 소개된 각 서버는 실제 사용 사례와 개발자 피드백을 바탕으로 선정되었습니다. 각 서버가 무엇을 하는지뿐만 아니라, 왜 중요한지, 그리고 여러분의 프로젝트에서 최대한 활용하는 방법까지 알게 될 것입니다. MCP가 처음이든 기존 환경을 확장하려는 중이든, 이 서버들은 Microsoft 생태계에서 가장 실용적이고 영향력 있는 도구들입니다.

> **💡 빠른 시작 팁**
> 
> MCP가 처음인가요? 걱정 마세요! 이 가이드는 초보자도 쉽게 따라올 수 있도록 설계되었습니다. 개념을 하나씩 설명하며 진행하니, 언제든지 [MCP 소개](../00-Introduction/README.md)와 [핵심 개념](../01-CoreConcepts/README.md) 모듈을 참고해 더 깊이 있는 배경지식을 얻을 수 있습니다.

## 개요

이 포괄적인 가이드는 AI 어시스턴트와 외부 도구 간 상호작용 방식을 혁신하는 10가지 Microsoft MCP 서버를 탐구합니다. Azure 리소스 관리부터 문서 처리까지, 이 서버들은 Model Context Protocol이 매끄럽고 생산적인 개발 워크플로우를 만드는 데 얼마나 강력한지 보여줍니다.

## 학습 목표

이 가이드를 마치면 다음을 할 수 있습니다:
- MCP 서버가 개발자 생산성을 어떻게 향상시키는지 이해하기
- Microsoft의 가장 영향력 있는 MCP 서버 구현 사례 배우기
- 각 서버의 실용적인 사용 사례 발견하기
- VS Code와 Visual Studio에서 서버 설정 및 구성 방법 알기
- 더 넓은 MCP 생태계와 미래 방향 탐색하기

## 🔧 MCP 서버 이해하기: 초보자 가이드

### MCP 서버란 무엇인가요?

Model Context Protocol(MCP)에 익숙하지 않은 분이라면 “MCP 서버가 정확히 무엇이고 왜 중요한가?”라는 질문이 떠오를 수 있습니다. 간단한 비유로 시작해 보겠습니다.

MCP 서버는 AI 코딩 동반자(예: GitHub Copilot)가 외부 도구 및 서비스와 연결할 수 있도록 돕는 전문화된 어시스턴트라고 생각하세요. 마치 스마트폰에서 날씨 앱, 내비게이션 앱, 은행 앱을 각각 사용하는 것처럼, MCP 서버는 AI 어시스턴트가 다양한 개발 도구 및 서비스와 상호작용할 수 있게 해줍니다.

### MCP 서버가 해결하는 문제

MCP 서버가 등장하기 전에는 다음과 같은 작업을 하려면:
- Azure 리소스 확인
- GitHub 이슈 생성
- 데이터베이스 쿼리
- 문서 검색

코딩을 멈추고 브라우저를 열어 해당 웹사이트로 이동해 수동으로 작업해야 했습니다. 이런 잦은 컨텍스트 전환은 작업 흐름을 끊고 생산성을 떨어뜨립니다.

### MCP 서버가 개발 경험을 바꾸는 방법

MCP 서버를 사용하면 VS Code, Visual Studio 등 개발 환경을 벗어나지 않고 AI 어시스턴트에게 작업을 맡길 수 있습니다. 예를 들어:

**기존 작업 흐름:**
1. 코딩 중단
2. 브라우저 열기
3. Azure 포털 접속
4. 스토리지 계정 정보 확인
5. VS Code로 돌아오기
6. 코딩 재개

**이제는 이렇게 할 수 있습니다:**
1. AI에게 묻기: "내 Azure 스토리지 계정 상태가 어때?"
2. 받은 정보를 바탕으로 코딩 계속하기

### 초보자를 위한 주요 이점

#### 1. 🔄 **작업 흐름 유지**
- 여러 앱을 오가며 전환할 필요 없음
- 코딩에 집중력 유지
- 도구 관리에 따른 정신적 부담 감소

#### 2. 🤖 **복잡한 명령 대신 자연어 사용**
- SQL 문법을 외우지 않고 필요한 데이터를 설명
- Azure CLI 명령어 대신 원하는 작업을 자연어로 전달
- AI가 기술적 세부사항을 처리하도록 맡기고 논리에 집중

#### 3. 🔗 **여러 도구 연결**
- 다양한 서비스를 조합해 강력한 워크플로우 생성
- 예: "최근 GitHub 이슈 모두 가져와서 Azure DevOps 작업 항목 생성"
- 복잡한 스크립트 없이 자동화 구축

#### 4. 🌐 **확장되는 생태계 접근**
- Microsoft, GitHub 등 다양한 기업이 만든 서버 활용
- 여러 공급업체 도구를 자유롭게 조합
- 다양한 AI 어시스턴트에서 작동하는 표준화된 생태계 참여

#### 5. 🛠️ **실습을 통한 학습**
- 미리 만들어진 서버로 개념 이해 시작
- 익숙해지면 직접 서버 구축 도전
- SDK와 문서 활용해 학습 지원

### 초보자를 위한 실제 예시

웹 개발이 처음이고 첫 프로젝트를 진행 중이라고 가정해 봅시다. MCP 서버가 어떻게 도움이 되는지 살펴보겠습니다:

**기존 방식:**
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

### 기업 표준의 이점

MCP는 업계 표준으로 자리잡고 있어:
- **일관성**: 다양한 도구와 기업 간 유사한 경험 제공
- **상호운용성**: 서로 다른 공급업체 서버 간 협업 가능
- **미래 대비**: 기술과 설정이 여러 AI 어시스턴트 간에 이전 가능
- **커뮤니티**: 방대한 지식과 리소스 공유 생태계

### 시작하기: 이 가이드에서 배우는 내용

이 가이드에서는 모든 수준의 개발자에게 유용한 10가지 Microsoft MCP 서버를 다룹니다. 각 서버는 다음을 목표로 설계되었습니다:
- 일반적인 개발 문제 해결
- 반복 작업 감소
- 코드 품질 향상
- 학습 기회 확대

> **💡 학습 팁**
> 
> MCP가 완전 처음이라면, 먼저 [MCP 소개](../00-Introduction/README.md)와 [핵심 개념](../01-CoreConcepts/README.md) 모듈을 학습하세요. 그런 다음 이곳으로 돌아와 Microsoft 도구와 함께 개념을 실습해 보세요.
>
> MCP의 중요성에 대한 추가 배경은 Maria Naggaga의 글 [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps)를 참고하세요.

## VS Code와 Visual Studio에서 MCP 시작하기 🚀

GitHub Copilot과 함께 Visual Studio Code 또는 Visual Studio 2022를 사용한다면 MCP 서버 설정은 간단합니다.

### VS Code 설정

VS Code에서 기본 설정 절차는 다음과 같습니다:

1. **에이전트 모드 활성화**: Copilot Chat 창에서 에이전트 모드로 전환
2. **MCP 서버 구성**: VS Code의 settings.json 파일에 서버 설정 추가
3. **서버 시작**: 사용하려는 각 서버 옆의 "시작" 버튼 클릭
4. **도구 선택**: 현재 세션에서 활성화할 MCP 서버 선택

자세한 설정 방법은 [VS Code MCP 문서](https://code.visualstudio.com/docs/copilot/copilot-mcp)를 참고하세요.

> **💡 전문가 팁: MCP 서버를 전문가처럼 관리하세요!**
> 
> VS Code 확장 기능 뷰에 [설치된 MCP 서버를 관리할 수 있는 새 UI](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)가 추가되었습니다! 명확하고 간단한 인터페이스로 서버 시작, 중지, 관리가 빠르게 가능합니다. 꼭 사용해 보세요!

### Visual Studio 2022 설정

Visual Studio 2022(버전 17.14 이상)에서는 다음과 같이 설정합니다:

1. **에이전트 모드 활성화**: GitHub Copilot Chat 창의 "Ask" 드롭다운에서 "Agent" 선택
2. **구성 파일 생성**: 솔루션 디렉터리에 `.mcp.json` 파일 생성 (권장 위치: `<SOLUTIONDIR>\.mcp.json`)
3. **서버 구성**: 표준 MCP 형식으로 서버 설정 추가
4. **도구 승인**: 요청 시 적절한 범위 권한으로 도구 사용 승인

자세한 Visual Studio 설정 방법은 [Visual Studio MCP 문서](https://learn.microsoft.com/visualstudio/ide/mcp-servers)를 참고하세요.

각 MCP 서버는 연결 문자열, 인증 등 고유한 구성 요구사항이 있지만, 두 IDE 모두 설정 패턴은 일관적입니다.

## Microsoft MCP 서버에서 얻은 교훈 🛠️

### 1. 📚 Microsoft Learn Docs MCP 서버

[![VS Code에 설치](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![VS Code Insiders에 설치](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**기능**: Microsoft Learn Docs MCP 서버는 클라우드 기반 서비스로, AI 어시스턴트가 Model Context Protocol을 통해 공식 Microsoft 문서에 실시간으로 접근할 수 있게 합니다. `https://learn.microsoft.com/api/mcp`에 연결되어 Microsoft Learn, Azure 문서, Microsoft 365 문서 등 공식 자료를 의미 기반 검색으로 제공합니다.

**유용한 이유**: 단순한 문서처럼 보일 수 있지만, 이 서버는 Microsoft 기술을 사용하는 모든 개발자에게 필수적입니다. .NET 개발자들이 AI 코딩 어시스턴트에 대해 가장 많이 하는 불만 중 하나는 최신 .NET 및 C# 릴리스에 대한 정보가 부족하다는 점입니다. Microsoft Learn Docs MCP 서버는 최신 문서, API 참조, 모범 사례에 실시간으로 접근할 수 있게 하여 이 문제를 해결합니다. 최신 Azure SDK를 사용하거나 C# 13의 새로운 기능을 탐색하거나 최첨단 .NET Aspire 패턴을 구현할 때, 이 서버는 AI 어시스턴트가 정확하고 현대적인 코드를 생성하는 데 필요한 권위 있는 최신 정보를 제공합니다.

**실제 사용 사례**: "공식 Microsoft Learn 문서에 따른 Azure 컨테이너 앱 생성 az cli 명령어는 무엇인가요?" 또는 "ASP.NET Core에서 의존성 주입과 함께 Entity Framework를 어떻게 구성하나요?" 또는 "이 코드를 Microsoft Learn 문서의 성능 권장사항과 일치하는지 검토해 주세요." 이 서버는 Microsoft Learn, Azure 문서, Microsoft 365 문서를 아우르는 포괄적인 커버리지를 제공하며, 고급 의미 기반 검색으로 가장 관련성 높은 정보를 찾아 최대 10개의 고품질 콘텐츠 조각과 기사 제목, URL을 반환합니다. 항상 최신 문서에 접근합니다.

**특징적인 예시**: 이 서버는 `microsoft_docs_search` 도구를 제공하여 Microsoft 공식 기술 문서에 대한 의미 기반 검색을 수행합니다. 설정 후 "ASP.NET Core에서 JWT 인증을 어떻게 구현하나요?" 같은 질문을 하면 상세하고 공식적인 답변과 출처 링크를 받을 수 있습니다. 검색 품질이 뛰어난 이유는 문맥을 이해하기 때문입니다 – 예를 들어 "컨테이너"라는 단어가 Azure 문맥에서는 Azure Container Instances 문서를, .NET 문맥에서는 관련 C# 컬렉션 정보를 반환합니다.

이 기능은 빠르게 변화하거나 최근 업데이트된 라이브러리와 사용 사례에 특히 유용합니다. 예를 들어 최근 코딩 프로젝트에서 최신 .NET Aspire와 Microsoft.Extensions.AI 릴리스의 기능을 활용하고 싶을 때, Microsoft Learn Docs MCP 서버를 포함시켜 API 문서뿐 아니라 방금 발표된 가이드와 워크스루도 활용할 수 있었습니다.
> **💡 전문가 팁**
> 
> 도구 친화적인 모델이라도 MCP 도구를 사용하도록 격려가 필요합니다! 시스템 프롬프트나 [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) 같은 내용을 추가해 보세요: "당신은 `microsoft.docs.mcp`에 접근할 수 있습니다 – C#, Azure, ASP.NET Core, Entity Framework 같은 Microsoft 기술 관련 질문을 처리할 때 Microsoft의 최신 공식 문서를 검색하는 데 이 도구를 사용하세요."
>
> 이를 실제로 적용한 훌륭한 예시는 Awesome GitHub Copilot 저장소의 [C# .NET Janitor 채팅 모드](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md)를 참고하세요. 이 모드는 Microsoft Learn Docs MCP 서버를 활용해 최신 패턴과 모범 사례를 적용하여 C# 코드를 정리하고 현대화하는 데 특화되어 있습니다.
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**기능 소개**: Azure MCP Server는 15개 이상의 전문화된 Azure 서비스 커넥터를 포함하는 종합 패키지로, 전체 Azure 생태계를 AI 워크플로우에 통합합니다. 단일 서버가 아니라 리소스 관리, 데이터베이스 연결(PostgreSQL, SQL Server), KQL을 활용한 Azure Monitor 로그 분석, Cosmos DB 통합 등 다양한 기능을 포함한 강력한 컬렉션입니다.

**유용한 이유**: 단순히 Azure 리소스를 관리하는 것을 넘어, Azure SDK를 사용할 때 코드 품질을 크게 향상시킵니다. Agent 모드에서 Azure MCP를 사용하면 단순히 코드를 작성하는 데 그치지 않고, 최신 인증 패턴, 오류 처리 모범 사례를 따르고 최신 SDK 기능을 활용하는 *더 나은* Azure 코드를 작성할 수 있습니다. 작동할 수 있는 일반적인 코드 대신, 프로덕션 워크로드에 권장되는 Azure 패턴을 따르는 코드를 얻을 수 있습니다.

**주요 모듈**:
- **🗄️ 데이터베이스 커넥터**: Azure Database for PostgreSQL 및 SQL Server에 자연어로 직접 접근
- **📊 Azure Monitor**: KQL 기반 로그 분석 및 운영 인사이트 제공
- **🌐 리소스 관리**: Azure 리소스 전체 수명주기 관리
- **🔐 인증**: DefaultAzureCredential 및 관리형 아이덴티티 패턴 지원
- **📦 스토리지 서비스**: Blob Storage, Queue Storage, Table Storage 작업
- **🚀 컨테이너 서비스**: Azure Container Apps, Container Instances, AKS 관리
- **그 외 다양한 전문 커넥터 포함**

**실제 활용 예**: "내 Azure 스토리지 계정 목록 보여줘", "지난 한 시간 동안 Log Analytics 작업 영역에서 오류 쿼리해줘", "Node.js로 적절한 인증을 사용해 Azure 애플리케이션 만드는 걸 도와줘"

**전체 데모 시나리오**: Azure MCP와 GitHub Copilot for Azure 확장을 VS Code에 함께 설치한 후 다음과 같이 요청해 보세요:

> "DefaultAzureCredential 인증을 사용해 Azure Blob Storage에 파일을 업로드하는 Python 스크립트를 만들어줘. 내 Azure 스토리지 계정 이름은 'mycompanystorage'이고, 'documents'라는 컨테이너에 업로드할 거야. 현재 타임스탬프로 테스트 파일을 생성하고, 오류를 우아하게 처리하며 유용한 출력을 제공하고, Azure 인증 및 오류 처리 모범 사례를 따르고, DefaultAzureCredential 인증 방식에 대한 주석도 포함해줘. 함수와 문서화가 잘 된 구조로 만들어줘."

Azure MCP Server는 다음과 같은 완전한 프로덕션 수준의 Python 스크립트를 생성합니다:
- 최신 Azure Blob Storage SDK와 적절한 비동기 패턴 사용
- DefaultAzureCredential과 포괄적인 폴백 체인 설명 구현
- 구체적인 Azure 예외 타입을 포함한 견고한 오류 처리
- Azure SDK 모범 사례에 따른 리소스 관리 및 연결 처리
- 상세한 로깅과 유용한 콘솔 출력 제공
- 함수, 문서화, 타입 힌트를 포함한 잘 구조화된 스크립트

이 점이 특별한 이유는, Azure MCP가 없으면 작동은 하지만 최신 Azure 패턴을 따르지 않는 일반적인 blob storage 코드가 생성될 수 있기 때문입니다. Azure MCP를 사용하면 최신 인증 방법을 활용하고 Azure 특화 오류 시나리오를 처리하며, 마이크로소프트가 권장하는 프로덕션 애플리케이션 모범 사례를 따르는 코드를 얻을 수 있습니다.

**추천 예시**: 저는 `az`와 `azd` CLI 명령어를 기억하는 데 어려움을 겪었습니다. 항상 두 단계로 진행하죠: 먼저 문법을 찾아보고, 그다음 명령어를 실행합니다. CLI 문법을 기억하지 못한다는 걸 인정하기 싫어서 포털에 들어가 클릭하며 작업하는 경우가 많았습니다. 원하는 작업을 그냥 설명할 수 있다는 점이 놀랍고, IDE를 떠나지 않고도 할 수 있다는 점이 더 좋습니다!

시작하는 데 도움이 되는 다양한 사용 사례는 [Azure MCP 저장소](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server)에서 확인할 수 있습니다. 자세한 설치 가이드와 고급 설정 옵션은 [공식 Azure MCP 문서](https://learn.microsoft.com/azure/developer/azure-mcp-server/)를 참고하세요.

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**기능 소개**: 공식 GitHub MCP Server는 GitHub 생태계와 원활하게 통합되며, 호스팅된 원격 액세스와 로컬 Docker 배포 옵션을 모두 제공합니다. 단순한 저장소 작업을 넘어서 GitHub Actions 관리, 풀 리퀘스트 워크플로우, 이슈 추적, 보안 스캔, 알림, 고급 자동화 기능을 포함한 종합 툴킷입니다.

**유용한 이유**: 이 서버는 개발 환경 내에서 GitHub의 전체 플랫폼 경험을 제공하여, VS Code와 GitHub.com 사이를 계속 오가며 프로젝트 관리, 코드 리뷰, CI/CD 모니터링을 할 필요 없이 자연어 명령으로 모든 작업을 처리할 수 있게 합니다.

> **ℹ️ 참고: 다양한 '에이전트' 유형**
> 
> 이 GitHub MCP Server를 GitHub의 Coding Agent(이슈에 할당해 자동 코딩 작업을 수행하는 AI 에이전트)와 혼동하지 마세요. GitHub MCP Server는 VS Code의 Agent 모드 내에서 GitHub API 통합을 제공하며, Coding Agent는 별도의 기능으로 이슈에 할당되면 풀 리퀘스트를 생성합니다.

**주요 기능**:
- **⚙️ GitHub Actions**: 완전한 CI/CD 파이프라인 관리, 워크플로우 모니터링, 아티팩트 처리
- **🔀 풀 리퀘스트**: 생성, 검토, 병합 및 상태 추적
- **🐛 이슈**: 전체 이슈 수명주기 관리, 댓글, 라벨링, 할당
- **🔒 보안**: 코드 스캔 알림, 비밀 탐지, Dependabot 통합
- **🔔 알림**: 스마트 알림 관리 및 저장소 구독 제어
- **📁 저장소 관리**: 파일 작업, 브랜치 관리, 저장소 운영
- **👥 협업**: 사용자 및 조직 검색, 팀 관리, 접근 제어

**실제 활용 예**: "내 기능 브랜치에서 풀 리퀘스트 생성해줘", "이번 주 실패한 CI 실행 모두 보여줘", "내 저장소의 열린 보안 알림 목록 보여줘", "내가 할당된 모든 이슈를 조직별로 찾아줘"

**전체 데모 시나리오**: GitHub MCP Server의 기능을 보여주는 강력한 워크플로우 예시입니다:

> "스프린트 리뷰 준비가 필요해. 이번 주 내가 생성한 모든 풀 리퀘스트를 보여주고, CI/CD 파이프라인 상태를 확인해줘. 해결해야 할 보안 알림 요약을 만들고, 'feature' 라벨이 붙은 병합된 PR을 기반으로 릴리스 노트를 작성하는 데 도움을 줘."

GitHub MCP Server는 다음을 수행합니다:
- 최근 풀 리퀘스트를 상세 상태 정보와 함께 조회
- 워크플로우 실행을 분석해 실패나 성능 문제 강조
- 보안 스캔 결과를 취합해 중요 알림 우선순위 지정
- 병합된 PR에서 정보를 추출해 포괄적인 릴리스 노트 생성
- 스프린트 계획 및 릴리스 준비를 위한 실행 가능한 다음 단계 제공

**추천 예시**: 저는 코드 리뷰 워크플로우에 이 서버를 자주 사용합니다. VS Code, GitHub 알림, 풀 리퀘스트 페이지를 오가며 작업하는 대신 "내가 검토 대기 중인 모든 PR 보여줘"라고 말하고, 이어서 "PR #123에 인증 메서드의 오류 처리에 대해 질문하는 댓글 달아줘"라고 하면 됩니다. 서버가 GitHub API 호출을 처리하고, 대화 맥락을 유지하며, 더 건설적인 리뷰 댓글 작성도 도와줍니다.

**인증 옵션**: 이 서버는 VS Code에서 원활한 OAuth와 Personal Access Token을 모두 지원하며, 필요한 GitHub 기능만 활성화할 수 있는 도구 세트 구성이 가능합니다. 즉시 설정 가능한 원격 호스팅 서비스로 실행하거나, 완전한 제어를 위해 로컬 Docker로 실행할 수 있습니다.

> **💡 전문가 팁**
> 
> MCP 서버 설정에서 `--toolsets` 매개변수를 사용해 필요한 도구 세트만 활성화하면 컨텍스트 크기를 줄이고 AI 도구 선택을 개선할 수 있습니다. 예를 들어, 핵심 개발 워크플로우용으로 `"--toolsets", "repos,issues,pull_requests,actions"`를 추가하거나, 주로 GitHub 모니터링 기능만 원한다면 `"--toolsets", "notifications, security"`를 사용하세요.

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**기능 소개**: Azure DevOps 서비스와 연결되어 프로젝트 관리, 작업 항목 추적, 빌드 파이프라인 관리, 저장소 작업을 포괄적으로 지원합니다.

**유용한 이유**: Azure DevOps를 주된 DevOps 플랫폼으로 사용하는 팀에게, 이 MCP 서버는 개발 환경과 Azure DevOps 웹 인터페이스 간의 탭 전환을 없애줍니다. 작업 항목 관리, 빌드 상태 확인, 저장소 쿼리, 프로젝트 관리 작업을 AI 어시스턴트를 통해 직접 처리할 수 있습니다.

**실제 활용 예**: "WebApp 프로젝트의 현재 스프린트에서 활성 작업 항목 모두 보여줘", "방금 발견한 로그인 문제에 대한 버그 리포트 생성해줘", "빌드 파이프라인 상태 확인하고 최근 실패한 항목 보여줘"

**추천 예시**: 개발 환경을 떠나지 않고도 "WebApp 프로젝트의 현재 스프린트에서 활성 작업 항목 모두 보여줘" 또는 "방금 발견한 로그인 문제에 대한 버그 리포트 생성해줘" 같은 간단한 쿼리로 팀의 현재 스프린트 상태를 쉽게 확인할 수 있습니다.

### 5. 📝 MarkItDown MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**기능**: MarkItDown은 다양한 파일 형식을 고품질 Markdown으로 변환하는 종합 문서 변환 서버로, LLM(대형 언어 모델) 활용과 텍스트 분석 워크플로우에 최적화되어 있습니다.

**유용한 이유**: 현대 문서 작업에 필수적입니다! MarkItDown은 제목, 목록, 표, 링크 등 중요한 문서 구조를 유지하면서 다양한 파일 형식을 처리합니다. 단순 텍스트 추출 도구와 달리, AI 처리와 사람이 읽기 모두에 유용한 의미론적 내용과 서식을 보존하는 데 중점을 둡니다.

**지원하는 파일 형식**:
- **오피스 문서**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **미디어 파일**: 이미지(EXIF 메타데이터 및 OCR 포함), 오디오(EXIF 메타데이터 및 음성 전사 포함)
- **웹 콘텐츠**: HTML, RSS 피드, YouTube URL, 위키피디아 페이지
- **데이터 형식**: CSV, JSON, XML, ZIP 파일(내용을 재귀적으로 처리)
- **출판 형식**: EPub, Jupyter 노트북(.ipynb)
- **이메일**: Outlook 메시지(.msg)
- **고급 기능**: 향상된 PDF 처리를 위한 Azure Document Intelligence 통합

**고급 기능**: MarkItDown은 OpenAI 클라이언트가 제공될 경우 LLM 기반 이미지 설명, Azure Document Intelligence를 통한 PDF 고급 처리, 음성 콘텐츠 전사, 추가 파일 형식 확장을 위한 플러그인 시스템을 지원합니다.

**실제 활용 예**: "이 PowerPoint 프레젠테이션을 문서 사이트용 Markdown으로 변환해 주세요", "이 PDF에서 올바른 제목 구조로 텍스트를 추출해 주세요", "이 Excel 스프레드시트를 읽기 쉬운 표 형식으로 바꿔 주세요"

**주요 예시**: [MarkItDown 문서](https://github.com/microsoft/markitdown#why-markdown)에서 인용하자면:


> Markdown은 최소한의 마크업과 서식으로 거의 일반 텍스트에 가깝지만, 중요한 문서 구조를 표현할 수 있는 방법을 제공합니다. OpenAI의 GPT-4o 같은 주류 LLM은 기본적으로 Markdown을 "이해"하며, 종종 별도의 지시 없이도 응답에 Markdown을 포함합니다. 이는 방대한 양의 Markdown 형식 텍스트로 학습되었음을 의미하며, Markdown을 잘 이해한다는 뜻입니다. 부가적으로 Markdown 규칙은 토큰 효율성도 매우 높습니다.

MarkItDown은 문서 구조 보존에 뛰어나 AI 워크플로우에 매우 중요합니다. 예를 들어 PowerPoint를 변환할 때 슬라이드 구성을 적절한 제목으로 유지하고, 표는 Markdown 표로 추출하며, 이미지에는 대체 텍스트를 포함하고, 발표자 노트도 처리합니다. 차트는 읽기 쉬운 데이터 표로 변환되며, 결과 Markdown은 원본 프레젠테이션의 논리적 흐름을 유지합니다. 이는 프레젠테이션 내용을 AI 시스템에 입력하거나 기존 슬라이드로 문서를 만들기에 완벽합니다.

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**기능**: SQL Server 데이터베이스(온프레미스, Azure SQL, Fabric)에 대화형 접근 제공

**유용한 이유**: PostgreSQL 서버와 비슷하지만 Microsoft SQL 생태계용입니다. 간단한 연결 문자열로 연결해 자연어로 쿼리할 수 있어, 더 이상 문맥 전환이 필요 없습니다!

**실제 활용 예**: "지난 30일간 처리되지 않은 모든 주문을 찾아줘" 같은 요청이 적절한 SQL 쿼리로 변환되어 포맷된 결과를 반환합니다.

**주요 예시**: 데이터베이스 연결을 설정하면 즉시 데이터와 대화할 수 있습니다. 블로그 게시물에서는 "어떤 데이터베이스에 연결되어 있나요?"라는 간단한 질문으로 시연합니다. MCP 서버는 적절한 데이터베이스 도구를 호출해 SQL Server 인스턴스에 연결하고 현재 데이터베이스 연결 정보를 반환합니다. SQL 쿼리를 한 줄도 작성하지 않고 말이죠. 이 서버는 스키마 관리부터 데이터 조작까지 자연어 프롬프트로 포괄적인 데이터베이스 작업을 지원합니다. VS Code와 Claude Desktop을 이용한 완전한 설정 및 구성 예시는 [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/)를 참고하세요.


### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**기능**: AI 에이전트가 웹 페이지와 상호작용하여 테스트 및 자동화를 수행할 수 있게 합니다.

> **ℹ️ GitHub Copilot 지원**
> 
> Playwright MCP Server는 GitHub Copilot의 코딩 에이전트에 웹 브라우징 기능을 제공합니다! [이 기능에 대해 더 알아보기](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**유용한 이유**: 자연어 설명으로 구동되는 자동화 테스트에 최적입니다. AI가 웹사이트를 탐색하고, 폼을 작성하며, 구조화된 접근성 스냅샷을 통해 데이터를 추출할 수 있어 매우 강력합니다!

**실제 활용 예**: "로그인 흐름을 테스트하고 대시보드가 제대로 로드되는지 확인해 줘" 또는 "제품 검색 테스트를 생성하고 결과 페이지를 검증해 줘" — 애플리케이션 소스 코드 없이도 가능합니다.

**주요 예시**: 제 동료 Debbie O'Brien은 최근 Playwright MCP Server를 활용해 놀라운 작업을 하고 있습니다! 예를 들어, 애플리케이션 소스 코드 접근 없이도 완전한 Playwright 테스트를 생성하는 방법을 보여주었는데요. 그녀는 Copilot에게 영화 검색 앱에 대한 테스트를 요청했습니다: 사이트에 접속해 "Garfield"를 검색하고 결과에 영화가 나타나는지 확인하는 테스트입니다. MCP는 브라우저 세션을 시작하고 DOM 스냅샷으로 페이지 구조를 탐색해 적절한 셀렉터를 찾아내고, 첫 실행에 통과하는 완전한 TypeScript 테스트 코드를 생성했습니다.

이 기능이 강력한 이유는 자연어 지시와 실행 가능한 테스트 코드 사이의 간극을 메워주기 때문입니다. 기존 방식은 수동 테스트 작성이나 코드베이스 접근이 필요했지만, Playwright MCP를 사용하면 외부 사이트, 클라이언트 애플리케이션, 코드 접근이 불가능한 블랙박스 테스트 시나리오도 테스트할 수 있습니다.


### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**기능**: 자연어로 Microsoft Dev Box 환경을 관리합니다.

**유용한 이유**: 개발 환경 관리를 크게 단순화합니다! 특정 명령어를 기억하지 않아도 개발 환경을 생성, 구성, 관리할 수 있습니다.

**실제 활용 예**: "최신 .NET SDK가 설치된 새 Dev Box를 만들고 우리 프로젝트에 맞게 설정해 줘", "내 모든 개발 환경 상태를 확인해 줘", "팀 발표용 표준화된 데모 환경을 만들어 줘"

**주요 예시**: 저는 개인 개발에 Dev Box를 사용하는 것을 매우 좋아합니다. James Montemagno가 Dev Box가 컨퍼런스 데모에 얼마나 좋은지 설명해 준 순간이 특히 인상적이었는데요, 컨퍼런스, 호텔, 비행기 와이파이 환경과 상관없이 초고속 이더넷 연결을 제공하기 때문입니다. 실제로 최근에 브뤼헤에서 앤트워프로 가는 버스에서 노트북을 휴대폰 핫스팟에 연결한 상태로 컨퍼런스 데모 연습을 했습니다! 앞으로는 여러 개발 환경을 팀 단위로 관리하고 표준화된 데모 환경을 구축하는 데 집중할 계획입니다. 고객과 동료들로부터 많이 듣는 또 다른 활용 사례는 사전 구성된 개발 환경으로 Dev Box를 사용하는 것입니다. 두 경우 모두 MCP를 통해 자연어로 Dev Box를 구성하고 관리할 수 있어, 개발 환경을 벗어나지 않고도 작업할 수 있습니다.

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**기능 설명**: Azure AI Foundry MCP Server는 개발자에게 모델 카탈로그, 배포 관리, Azure AI Search를 활용한 지식 인덱싱, 평가 도구 등 Azure AI 생태계에 대한 포괄적인 접근을 제공합니다. 이 실험적 서버는 AI 개발과 Azure의 강력한 AI 인프라 간의 다리를 놓아 AI 애플리케이션을 더 쉽게 구축, 배포, 평가할 수 있도록 돕습니다.

**유용한 이유**: 이 서버는 엔터프라이즈급 AI 기능을 개발 워크플로우에 직접 통합하여 Azure AI 서비스와의 작업 방식을 혁신합니다. Azure 포털, 문서, IDE를 오가며 작업하는 대신 자연어 명령으로 모델 탐색, 서비스 배포, 지식 베이스 관리, AI 성능 평가를 할 수 있습니다. 특히 RAG(검색 보강 생성) 애플리케이션 개발, 다중 모델 배포 관리, 종합적인 AI 평가 파이프라인 구현에 강력한 도구입니다.

**주요 개발자 기능**:
- **🔍 모델 탐색 및 배포**: Azure AI Foundry의 모델 카탈로그를 탐색하고, 코드 샘플과 함께 상세 모델 정보를 확인하며, 모델을 Azure AI 서비스에 배포
- **📚 지식 관리**: Azure AI Search 인덱스 생성 및 관리, 문서 추가, 인덱서 구성, 정교한 RAG 시스템 구축
- **⚡ AI 에이전트 통합**: Azure AI 에이전트와 연결, 기존 에이전트 쿼리, 운영 환경에서 에이전트 성능 평가
- **📊 평가 프레임워크**: 텍스트 및 에이전트 평가 실행, 마크다운 보고서 생성, AI 애플리케이션 품질 보증 구현
- **🚀 프로토타이핑 도구**: GitHub 기반 프로토타이핑 설정 안내 및 최신 연구 모델을 위한 Azure AI Foundry Labs 접근

**실제 개발자 활용 예**: "내 애플리케이션에 Phi-4 모델을 Azure AI 서비스에 배포하기", "내 문서 RAG 시스템을 위한 새로운 검색 인덱스 생성", "내 에이전트 응답을 품질 지표에 따라 평가하기", "복잡한 분석 작업에 최적화된 추론 모델 찾기"

**전체 데모 시나리오**: 강력한 AI 개발 워크플로우 예시:


> "고객 지원 에이전트를 만들고 있어요. 카탈로그에서 좋은 추론 모델을 찾아 Azure AI 서비스에 배포하고, 문서에서 지식 베이스를 만들고, 응답 품질을 테스트할 평가 프레임워크를 설정한 다음, GitHub 토큰을 이용해 통합 프로토타입을 만드는 데 도움을 주세요."

Azure AI Foundry MCP Server는 다음을 수행합니다:
- 요구사항에 맞는 최적의 추론 모델을 추천하기 위해 모델 카탈로그 쿼리
- 선호하는 Azure 지역에 대한 배포 명령과 할당량 정보 제공
- 문서에 적합한 스키마로 Azure AI Search 인덱스 설정
- 품질 지표와 안전성 검사를 포함한 평가 파이프라인 구성
- 즉시 테스트 가능한 GitHub 인증 프로토타이핑 코드 생성
- 특정 기술 스택에 맞춘 종합 설정 가이드 제공

**주요 사례**: 개발자로서 다양한 LLM 모델을 따라잡기 어려웠습니다. 몇 가지 주요 모델은 알지만, 생산성과 효율성을 놓치고 있다는 느낌이 들었죠. 토큰과 할당량 관리도 스트레스였고, 적절한 모델을 선택하는지, 예산을 낭비하는지 항상 불안했습니다. 이번에 팀원들과 MCP 서버 추천을 알아보던 중 James Montemagno에게서 이 MCP 서버를 알게 되었고, 사용해볼 생각에 기대가 큽니다! 모델 탐색 기능은 평소 접하지 못한 모델을 찾아보고 특정 작업에 최적화된 모델을 발견하는 데 특히 인상적입니다. 평가 프레임워크는 단순히 새로운 시도를 넘어서 실제로 더 나은 결과를 얻고 있는지 검증하는 데 도움이 될 것입니다.

> **ℹ️ 실험적 상태**
> 
> 이 MCP 서버는 실험 단계이며 활발히 개발 중입니다. 기능과 API가 변경될 수 있습니다. Azure AI 기능 탐색과 프로토타입 제작에 적합하지만, 프로덕션 사용 시 안정성 요구사항을 반드시 검증하세요.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**기능 설명**: Microsoft 365 및 Microsoft 365 Copilot과 통합되는 AI 에이전트 및 애플리케이션 개발에 필요한 핵심 도구를 제공합니다. 스키마 검증, 샘플 코드 조회, 문제 해결 지원 등이 포함됩니다.

**유용한 이유**: Microsoft 365와 Copilot 개발은 복잡한 매니페스트 스키마와 특정 개발 패턴을 요구합니다. 이 MCP 서버는 개발 환경 내에서 필수 리소스를 제공해 스키마 검증, 샘플 코드 탐색, 일반적인 문제 해결을 문서를 계속 참조하지 않고도 할 수 있게 도와줍니다.

**실제 활용 예**: "내 선언적 에이전트 매니페스트를 검증하고 스키마 오류를 수정하기", "Microsoft Graph API 플러그인 구현 샘플 코드 보여주기", "Teams 앱 인증 문제 해결 도움 받기"

**주요 사례**: Build 행사에서 M365 Agents에 대해 이야기하다가 친구 John Miller에게 연락했는데, 이 MCP를 추천받았습니다. 문서에 파묻히지 않고 시작할 수 있는 템플릿, 샘플 코드, 스캐폴딩을 제공해 M365 Agents 초보 개발자에게 매우 유용할 것 같습니다. 특히 매니페스트 구조 오류를 방지하는 스키마 검증 기능은 수 시간의 디버깅을 줄여줄 것으로 기대됩니다.

> **💡 전문가 팁**
> 
> Microsoft Learn Docs MCP Server와 함께 사용하면 M365 개발 지원이 더욱 완벽해집니다. 하나는 공식 문서를 제공하고, 이 서버는 실용적인 개발 도구와 문제 해결 지원을 제공합니다.

## 다음 단계는? 🔮

## 📋 결론

Model Context Protocol(MCP)은 개발자가 AI 어시스턴트와 외부 도구를 다루는 방식을 혁신하고 있습니다. 이 10개의 Microsoft MCP 서버는 표준화된 AI 통합의 힘을 보여주며, 개발자가 강력한 외부 기능을 활용하면서도 작업 흐름을 끊기지 않고 유지할 수 있게 합니다.

포괄적인 Azure 생태계 통합부터 Playwright 같은 브라우저 자동화, MarkItDown 같은 문서 처리 도구에 이르기까지, 이 서버들은 다양한 개발 시나리오에서 생산성을 높이는 MCP의 가능성을 보여줍니다. 표준화된 프로토콜 덕분에 이 도구들이 원활하게 협력하여 일관된 개발 경험을 만듭니다.

MCP 생태계가 계속 발전함에 따라 커뮤니티와 적극적으로 소통하고, 새로운 서버를 탐색하며, 맞춤형 솔루션을 구축하는 것이 개발 생산성을 극대화하는 열쇠가 될 것입니다. MCP의 오픈 스탠다드 특성 덕분에 다양한 공급업체의 도구를 조합해 자신만의 최적화된 워크플로우를 만들 수 있습니다.

## 🔗 추가 자료

- [공식 Microsoft MCP 저장소](https://github.com/microsoft/mcp)
- [MCP 커뮤니티 및 문서](https://modelcontextprotocol.io/introduction)
- [VS Code MCP 문서](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP 문서](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP 문서](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP 이벤트](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days 라이브 7월 29/30일 또는 온디맨드 시청](https://aka.ms/mcpdevdays)

## 🎯 연습 과제

1. **설치 및 구성**: VS Code 환경에 MCP 서버 중 하나를 설치하고 기본 기능을 테스트하세요.
2. **워크플로우 통합**: 최소 세 개의 MCP 서버를 결합한 개발 워크플로우를 설계하세요.
3. **맞춤 서버 기획**: 일상 개발 작업 중 맞춤 MCP 서버가 도움이 될 만한 작업을 찾아 사양을 작성하세요.
4. **성능 분석**: MCP 서버 사용과 기존 방식의 효율성을 비교 분석하세요.
5. **보안 평가**: 개발 환경에서 MCP 서버 사용 시 보안 영향을 평가하고 모범 사례를 제안하세요.

Next:[Best Practices](../08-BestPractices/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.