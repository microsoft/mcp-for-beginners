# 사례 연구: API Management에서 REST API를 MCP 서버로 노출하기

Azure API Management는 API 엔드포인트 위에 게이트웨이를 제공하는 서비스입니다. 작동 방식은 Azure API Management가 API 앞에서 프록시 역할을 하며 들어오는 요청에 대해 무엇을 할지 결정하는 것입니다.

이를 사용하면 다음과 같은 다양한 기능을 추가할 수 있습니다:

- **보안**: API 키, JWT, 관리 ID 등 다양한 보안 옵션을 사용할 수 있습니다.
- **속도 제한**: 특정 시간 단위당 허용되는 호출 수를 결정할 수 있는 훌륭한 기능입니다. 이를 통해 모든 사용자가 좋은 경험을 얻을 수 있고 서비스가 요청으로 인해 과부하되지 않도록 할 수 있습니다.
- **확장 및 로드 밸런싱**: 여러 엔드포인트를 설정하여 로드를 분산시킬 수 있으며, 로드 밸런싱 방식을 결정할 수도 있습니다.
- **AI 기능**: 예를 들어, 의미론적 캐싱, 토큰 제한 및 토큰 모니터링 등. 이러한 기능은 응답성을 개선하고 토큰 사용을 효율적으로 관리하는 데 도움을 줍니다. [자세히 알아보기](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## 왜 MCP + Azure API Management인가?

Model Context Protocol(MCP)은 에이전트 기반 AI 앱과 도구 및 데이터를 일관된 방식으로 노출하는 표준으로 빠르게 자리 잡고 있습니다. API를 "관리"해야 할 때 Azure API Management는 자연스러운 선택입니다. MCP 서버는 종종 다른 API와 통합하여 도구에 대한 요청을 해결합니다. 따라서 Azure API Management와 MCP를 결합하는 것은 매우 합리적입니다.

## 개요

이 특정 사용 사례에서는 API 엔드포인트를 MCP 서버로 노출하는 방법을 배웁니다. 이를 통해 이 엔드포인트를 에이전트 기반 앱의 일부로 쉽게 만들 수 있으며 Azure API Management의 기능도 활용할 수 있습니다.

## 주요 기능

- 노출하려는 엔드포인트 메서드를 선택할 수 있습니다.
- 추가 기능은 API의 정책 섹션에서 구성한 내용에 따라 달라집니다. 여기서는 속도 제한을 추가하는 방법을 보여줍니다.

## 사전 단계: API 가져오기

Azure API Management에 이미 API가 있다면 이 단계를 건너뛸 수 있습니다. 그렇지 않다면 [Azure API Management에 API 가져오기](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)를 확인하세요.

## API를 MCP 서버로 노출하기

API 엔드포인트를 노출하려면 다음 단계를 따르세요:

1. Azure 포털로 이동하여 다음 주소로 이동합니다: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   API Management 인스턴스로 이동합니다.

1. 왼쪽 메뉴에서 **APIs > MCP Servers > + Create new MCP Server**를 선택합니다.

1. API에서 MCP 서버로 노출할 REST API를 선택합니다.

1. 도구로 노출할 하나 이상의 API 작업을 선택합니다. 모든 작업을 선택하거나 특정 작업만 선택할 수 있습니다.

    ![노출할 메서드 선택](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create**를 선택합니다.

1. 메뉴 옵션 **APIs** 및 **MCP Servers**로 이동하면 다음과 같은 화면이 표시됩니다:

    ![메인 창에서 MCP 서버 보기](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 서버가 생성되고 API 작업이 도구로 노출됩니다. MCP 서버는 MCP Servers 창에 나열됩니다. URL 열에는 테스트하거나 클라이언트 애플리케이션 내에서 호출할 수 있는 MCP 서버의 엔드포인트가 표시됩니다.

## 선택 사항: 정책 구성

Azure API Management에는 정책이라는 핵심 개념이 있으며, 이를 통해 엔드포인트에 대한 다양한 규칙을 설정할 수 있습니다. 예를 들어 속도 제한이나 의미론적 캐싱을 설정할 수 있습니다. 이러한 정책은 XML로 작성됩니다.

MCP 서버에 대한 속도 제한 정책을 설정하는 방법은 다음과 같습니다:

1. 포털에서 **APIs** 아래 **MCP Servers**를 선택합니다.

1. 생성한 MCP 서버를 선택합니다.

1. 왼쪽 메뉴에서 MCP 아래 **Policies**를 선택합니다.

1. 정책 편집기에서 MCP 서버의 도구에 적용할 정책을 추가하거나 편집합니다. 정책은 XML 형식으로 정의됩니다. 예를 들어, MCP 서버의 도구에 대한 호출을 제한하는 정책을 추가할 수 있습니다(이 예에서는 클라이언트 IP 주소당 30초에 5회 호출 제한). 다음은 속도 제한을 설정하는 XML입니다:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    정책 편집기의 이미지:

    ![정책 편집기](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## 테스트하기

MCP 서버가 의도한 대로 작동하는지 확인해 봅시다.

이를 위해 Visual Studio Code와 GitHub Copilot의 에이전트 모드를 사용합니다. MCP 서버를 *mcp.json* 파일에 추가합니다. 이를 통해 Visual Studio Code는 에이전트 기능을 가진 클라이언트로 작동하며, 최종 사용자는 프롬프트를 입력하고 해당 서버와 상호작용할 수 있습니다.

Visual Studio Code에서 MCP 서버를 추가하는 방법은 다음과 같습니다:

1. **Command Palette**에서 MCP: **Add Server** 명령을 사용합니다.

1. 프롬프트가 표시되면 서버 유형을 선택합니다: **HTTP (HTTP 또는 Server Sent Events)**.

1. API Management의 MCP 서버 URL을 입력합니다. 예: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE 엔드포인트) 또는 **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP 엔드포인트). 전송 방식의 차이는 `/sse` 또는 `/mcp`입니다.

1. 선택한 서버 인스턴스를 기억하는 데 도움이 되는 서버 ID를 입력합니다. 이 값은 중요하지 않지만 식별에 유용합니다.

1. 설정을 워크스페이스 설정 또는 사용자 설정에 저장할지 선택합니다.

  - **워크스페이스 설정**: 서버 구성은 현재 워크스페이스에서만 사용할 수 있는 .vscode/mcp.json 파일에 저장됩니다.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    또는 스트리밍 HTTP를 전송 방식으로 선택하면 약간 다릅니다:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **사용자 설정**: 서버 구성은 글로벌 *settings.json* 파일에 추가되며 모든 워크스페이스에서 사용할 수 있습니다. 구성은 다음과 유사합니다:

    ![사용자 설정](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Azure API Management에 적절히 인증되도록 헤더를 추가해야 합니다. **Ocp-Apim-Subscription-Key**라는 헤더를 사용합니다.

    - 설정에 추가하는 방법은 다음과 같습니다:

    ![인증을 위한 헤더 추가](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png). 이 작업은 API 키 값을 묻는 프롬프트를 표시하며, 해당 값은 Azure 포털에서 Azure API Management 인스턴스에서 찾을 수 있습니다.

   - *mcp.json*에 추가하려면 다음과 같이 추가할 수 있습니다:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### 에이전트 모드 사용

이제 설정 또는 *.vscode/mcp.json*에서 모든 준비가 완료되었습니다. 테스트해 봅시다.

서버에서 노출된 도구가 나열된 도구 아이콘이 표시됩니다:

![서버의 도구](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 도구 아이콘을 클릭하면 다음과 같은 도구 목록이 표시됩니다:

    ![도구](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. 채팅에 프롬프트를 입력하여 도구를 호출합니다. 예를 들어, 주문 정보를 가져오는 도구를 선택했다면 에이전트에게 주문에 대해 질문할 수 있습니다. 다음은 예제 프롬프트입니다:

    ```text
    get information from order 2
    ```

    이제 도구를 호출하도록 요청하는 도구 아이콘이 표시됩니다. 도구 실행을 계속 선택하면 다음과 같은 출력이 표시됩니다:

    ![프롬프트 결과](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **위에 표시된 내용은 설정한 도구에 따라 다르지만, 위와 같은 텍스트 응답을 받는 것이 목표입니다.**

## 참고 자료

다음에서 더 많은 정보를 확인할 수 있습니다:

- [Azure API Management와 MCP에 대한 튜토리얼](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 샘플: Azure API Management를 사용하여 원격 MCP 서버 보호하기 (실험적)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 클라이언트 인증 실습](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Visual Studio Code용 Azure API Management 확장을 사용하여 API 가져오기 및 관리](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center에서 원격 MCP 서버 등록 및 검색](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway): Azure API Management를 활용한 다양한 AI 기능을 보여주는 훌륭한 리포지토리
- [AI Gateway 워크숍](https://azure-samples.github.io/AI-Gateway/): Azure 포털을 사용한 워크숍을 포함하여 AI 기능을 평가하는 좋은 시작점

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 번역가에 의한 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.  