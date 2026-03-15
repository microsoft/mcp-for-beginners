# 실용적인 구현

[![How to Build, Test, and Deploy MCP Apps with Real Tools and Workflows](../../../translated_images/ko/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(위 이미지를 클릭하여 본 강의 영상을 보세요)_

실용적인 구현은 모델 컨텍스트 프로토콜(MCP)의 힘을 구체화하는 부분입니다. MCP의 이론과 아키텍처를 이해하는 것도 중요하지만, 실제로 이러한 개념을 적용해 실제 문제를 해결하는 솔루션을 구축, 테스트, 배포할 때가 진짜 가치가 드러납니다. 이 장은 개념적 지식과 실전 개발 간의 격차를 메우며 MCP 기반 애플리케이션을 구현하는 과정을 안내합니다.

지능형 어시스턴트를 개발하든, 비즈니스 워크플로우에 AI를 통합하든, 데이터 처리용 맞춤형 도구를 구축하든 MCP는 유연한 기반을 제공합니다. 언어에 구애받지 않는 설계와 인기 있는 프로그래밍 언어용 공식 SDK 덕분에 다양한 개발자들이 접근할 수 있습니다. 이들 SDK를 활용하면 다양한 플랫폼과 환경에서 솔루션을 빠르게 프로토타입하고 반복 발전시키며 확장할 수 있습니다.

다음 섹션에서는 C#, Java(Spring 포함), TypeScript, JavaScript, Python에서 MCP를 구현하는 실용적인 예제, 샘플 코드, 배포 전략을 살펴봅니다. MCP 서버를 디버깅하고 테스트하는 법, API를 관리하는 법, 그리고 Azure를 이용해 솔루션을 클라우드에 배포하는 법도 배울 수 있습니다. 이러한 실습 자료는 학습을 가속화하고 견고하고 프로덕션에 적합한 MCP 애플리케이션을 자신 있게 구축할 수 있도록 설계되었습니다.

## 개요

본 강의는 다양한 프로그래밍 언어에서 MCP 구현에 관한 실용적인 측면에 중점을 둡니다. C#, Java(Spring), TypeScript, JavaScript, Python용 MCP SDK를 활용해 견고한 애플리케이션을 구축하고, MCP 서버를 디버깅 및 테스트하며, 재사용 가능한 리소스, 프롬프트, 도구를 만드는 방법을 다룹니다.

## 학습 목표

이 강의를 완료하면 다음을 수행할 수 있습니다:

- 다양한 프로그래밍 언어의 공식 SDK를 사용해 MCP 솔루션 구현
- MCP 서버를 체계적으로 디버깅하고 테스트
- 서버 기능(리소스, 프롬프트, 도구) 생성 및 활용
- 복잡한 작업을 위한 효과적인 MCP 워크플로우 설계
- 성능과 신뢰성을 최적화한 MCP 구현

## 공식 SDK 리소스

모델 컨텍스트 프로토콜은 여러 언어용 공식 SDK를 제공합니다 ([MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)에 맞춤):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java with Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **참고:** [Project Reactor](https://projectreactor.io) 의존성 필요. ([토론 이슈 246 참고](https://github.com/orgs/modelcontextprotocol/discussions/246))
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## MCP SDK 사용하기

이 섹션에는 여러 프로그래밍 언어별 MCP 구현 실용 예제가 있습니다. `samples` 디렉터리에서 언어별 샘플 코드를 찾을 수 있습니다.

### 제공되는 샘플

다음 언어로 된 [샘플 구현](../../../04-PracticalImplementation/samples)이 저장소에 포함되어 있습니다:

- [C#](./samples/csharp/README.md)
- [Java with Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

각 샘플은 특정 언어 및 생태계에 맞춘 주요 MCP 개념과 구현 패턴을 보여줍니다.

### 실용 가이드

추가 MCP 실용 구현 가이드:

- [페이지네이션과 큰 결과 집합](./pagination/README.md) - 도구, 리소스 및 대용량 데이터셋에 대한 커서 기반 페이지네이션 처리

## 핵심 서버 기능

MCP 서버는 다음 기능들을 조합해 구현할 수 있습니다:

### 리소스

리소스는 사용자 또는 AI 모델이 활용할 수 있는 컨텍스트와 데이터를 제공합니다:

- 문서 저장소
- 지식 베이스
- 구조화된 데이터 소스
- 파일 시스템

### 프롬프트

프롬프트는 사용자용 템플릿 메시지 및 워크플로우입니다:

- 미리 정의된 대화 템플릿
- 안내형 상호 작용 패턴
- 특화된 대화 구조

### 도구

도구는 AI 모델이 실행할 함수들입니다:

- 데이터 처리 유틸리티
- 외부 API 통합
- 계산 기능
- 검색 기능

## 샘플 구현: C# 구현

공식 C# SDK 저장소에는 MCP의 다양한 측면을 보여주는 여러 샘플 구현이 있습니다:

- **기본 MCP 클라이언트**: MCP 클라이언트를 생성하고 도구 호출하는 간단 예제
- **기본 MCP 서버**: 기본 도구 등록이 포함된 최소 서버 구현
- **고급 MCP 서버**: 도구 등록, 인증, 오류 처리를 포함한 완전한 기능 서버
- **ASP.NET 통합**: ASP.NET Core와의 통합 예제
- **도구 구현 패턴**: 다양한 복잡도의 도구 구현 패턴

MCP C# SDK는 현재 프리뷰 단계이며 API는 변경될 수 있습니다. SDK 변화에 따라 본 블로그를 계속 업데이트할 예정입니다.

### 주요 기능

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- [첫 MCP 서버 구축하기](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

전체 C# 구현 샘플은 [공식 C# SDK 샘플 저장소](https://github.com/modelcontextprotocol/csharp-sdk)에서 확인하세요.

## 샘플 구현: Java with Spring 구현

Java with Spring SDK는 엔터프라이즈급 기능을 갖춘 견고한 MCP 구현 옵션을 제공합니다.

### 주요 기능

- Spring Framework 통합
- 강력한 타입 안정성
- 리액티브 프로그래밍 지원
- 포괄적 오류 처리

전체 Java with Spring 구현 샘플은 `samples` 디렉터리의 [Java with Spring 샘플](samples/java/containerapp/README.md)에서 확인할 수 있습니다.

## 샘플 구현: JavaScript 구현

JavaScript SDK는 가볍고 유연한 MCP 구현 방식을 제공합니다.

### 주요 기능

- Node.js 및 브라우저 지원
- 프로미스 기반 API
- Express 및 기타 프레임워크와의 쉬운 통합
- 스트리밍용 WebSocket 지원

전체 JavaScript 구현 샘플은 `samples` 디렉터리의 [JavaScript 샘플](samples/javascript/README.md)에서 확인하세요.

## 샘플 구현: Python 구현

Python SDK는 훌륭한 ML 프레임워크 통합과 함께 Python다운 MCP 구현 방식을 제공합니다.

### 주요 기능

- asyncio를 활용한 비동기/await 지원
- FastAPI 통합
- 간편한 도구 등록
- 인기 ML 라이브러리와 네이티브 통합

전체 Python 구현 샘플은 `samples` 디렉터리의 [Python 샘플](samples/python/README.md)에서 확인할 수 있습니다.

## API 관리

Azure API 관리 서비스는 MCP 서버를 안전하게 보호할 수 있는 훌륭한 솔루션입니다. 아이디어는 MCP 서버 앞에 Azure API Management 인스턴스를 배치하고, 다음과 같은 기능들을 처리하게 하는 것입니다:

- 속도 제한
- 토큰 관리
- 모니터링
- 로드 밸런싱
- 보안

### Azure 샘플

다음은 바로 그 작업을 수행하는 Azure 샘플, 즉 [MCP 서버 생성 및 Azure API Management로 보안 적용](https://github.com/Azure-Samples/remote-mcp-apim-functions-python) 예제입니다.

아래 이미지에서 인증 흐름이 어떻게 진행되는지 확인하세요:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

위 이미지에서 다음과 같은 과정이 일어납니다:

- Microsoft Entra를 이용한 인증/인가가 수행됩니다.
- Azure API Management가 게이트웨이로 작동하며 정책을 사용해 트래픽을 관리하고 제어합니다.
- Azure Monitor가 모든 요청을 기록하여 추가 분석에 활용합니다.

#### 인증 흐름

인증 흐름을 더 자세히 살펴보겠습니다:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 인증 사양

[MCP 인증 사양](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)에 대해 더 알아보세요.

## 원격 MCP 서버를 Azure에 배포하기

앞서 언급한 샘플을 배포해 봅시다:

1. 저장소 복제

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. `Microsoft.App` 리소스 제공자 등록

   - Azure CLI를 사용하는 경우 `az provider register --namespace Microsoft.App --wait` 명령 실행
   - Azure PowerShell을 사용하는 경우 `Register-AzResourceProvider -ProviderNamespace Microsoft.App` 명령 실행. 등록 완료 여부는 `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` 명령으로 확인

1. 다음 [azd](https://aka.ms/azd) 명령어를 실행하여 API 관리 서비스, 코드 포함 함수 앱, 기타 필요한 Azure 리소스를 프로비저닝

    ```shell
    azd up
    ```

    이 명령어는 모든 클라우드 리소스를 Azure에 배포합니다.

### MCP Inspector로 서버 테스트하기

1. **새 터미널 창**에서 MCP Inspector 설치 및 실행

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    다음과 같은 인터페이스가 표시됩니다:

    ![Connect to Node inspector](../../../translated_images/ko/connect.141db0b2bd05f096.webp)

1. 앱에 표시된 URL (예: [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))에서 MCP Inspector 웹 앱을 CTRL 클릭하여 로드
1. 전송 유형을 `SSE`로 설정
1. `azd up` 후 표시된 실행 중인 API Management SSE 엔드포인트 URL을 입력하고 **연결**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **도구 목록 보기**. 도구를 클릭하고 **도구 실행**.

모든 단계가 성공했다면 MCP 서버에 연결되었으며 도구를 호출할 수 있었을 것입니다.

## Azure용 MCP 서버

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): 이 저장소 세트는 Azure Functions를 사용하여 Python, C# .NET 또는 Node/TypeScript로 원격 MCP (Model Context Protocol) 서버를 빠르게 시작하고 배포할 수 있는 템플릿입니다.

샘플은 개발자가 다음을 할 수 있는 완전한 솔루션을 제공합니다:

- 로컬에서 빌드 및 실행: 로컬 머신에서 MCP 서버 개발 및 디버깅
- Azure에 배포: 간단한 azd up 명령어를 통한 클라우드 배포
- 클라이언트 연결: VS Code의 Copilot 에이전트 모드와 MCP Inspector 툴 등 다양한 클라이언트에서 MCP 서버 연결

### 주요 기능

- 설계 단계부터 보안: MCP 서버는 키와 HTTPS로 보호됨
- 인증 옵션: 내장 인증 및/또는 API 관리 기반 OAuth 지원
- 네트워크 분리: Azure Virtual Networks(VNET)를 사용한 네트워크 격리 가능
- 서버리스 아키텍처: Azure Functions를 활용한 확장 가능하고 이벤트 중심 실행
- 로컬 개발 지원: 포괄적인 로컬 개발 및 디버깅 지원
- 간편한 배포: Azure로의 간소화된 배포 프로세스

이 저장소에는 프로덕션 환경에 적합한 MCP 서버 구현을 빠르게 시작하는 데 필요한 모든 구성 파일, 소스 코드, 인프라 정의가 포함되어 있습니다.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Python용 Azure Functions를 활용한 MCP 샘플 구현

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - C# .NET용 Azure Functions를 활용한 MCP 샘플 구현

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Node/TypeScript용 Azure Functions를 활용한 MCP 샘플 구현

## 주요 요점

- MCP SDK는 견고한 MCP 솔루션 구현을 위한 언어별 도구를 제공합니다
- 디버깅 및 테스트 과정은 신뢰할 수 있는 MCP 애플리케이션을 위한 핵심 단계입니다
- 재사용 가능한 프롬프트 템플릿으로 일관된 AI 상호 작용 가능
- 잘 설계된 워크플로우는 여러 도구를 사용해 복잡한 작업을 조율할 수 있습니다
- MCP 솔루션 구현 시 보안, 성능, 오류 처리를 고려해야 합니다

## 연습 문제

자신의 분야에서 실제 문제를 다루는 실용적인 MCP 워크플로우를 설계해 보세요:

1. 문제 해결에 유용할 3-4개의 도구 선정
2. 이 도구들이 어떻게 상호 작용하는지 보여주는 워크플로우 다이어그램 작성
3. 선호하는 언어로 도구 중 하나의 기본 버전 구현
4. 모델이 도구를 효과적으로 사용할 수 있게 돕는 프롬프트 템플릿 작성

## 추가 리소스

---

## 다음 단계

다음: [고급 주제](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역은 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원본 문서의 원어는 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 본 번역본 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->