# 사례 연구: API Management에서 MCP 서버로 REST API 노출하기

Azure API Management는 API 엔드포인트 위에 게이트웨이를 제공하는 서비스입니다. 작동 방식은 Azure API Management가 API 앞에서 프록시 역할을 하며 들어오는 요청에 대해 어떻게 처리할지 결정할 수 있습니다.

이를 사용함으로써 다음과 같은 다양한 기능을 추가할 수 있습니다:

- <strong>보안</strong>: API 키, JWT부터 관리되는 ID까지 모든 것을 사용할 수 있습니다.
- **요율 제한(Rate limiting)**: 특정 시간 단위당 몇 번의 호출이 허용될지 결정할 수 있는 훌륭한 기능입니다. 이는 모든 사용자가 훌륭한 경험을 할 수 있도록 보장하고 서비스가 과도한 요청으로 과부하 되는 것을 방지합니다.
- **스케일링 및 로드 밸런싱**: 여러 엔드포인트를 설정하여 부하를 분산할 수 있고, "로드 밸런싱" 방식을 결정할 수도 있습니다.
- **시맨틱 캐싱, 토큰 제한 및 토큰 모니터링과 같은 AI 기능**: 응답성을 향상시키고 토큰 사용량을 관리하는 데 큰 도움이 되는 훌륭한 기능입니다. [자세한 내용 읽기](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## 왜 MCP + Azure API Management인가?

모델 컨텍스트 프로토콜은 에이전트형 AI 앱과 도구 및 데이터를 일관된 방식으로 노출하는 방법에 대한 표준으로 급부상하고 있습니다. API를 "관리"해야 할 때 Azure API Management는 자연스러운 선택입니다. MCP 서버는 종종 도구에 대한 요청을 해결하기 위해 다른 API와 통합됩니다. 따라서 Azure API Management와 MCP를 결합하는 것이 매우 합리적입니다.

## 개요

이 특정 사용 사례에서는 API 엔드포인트를 MCP 서버로 노출하는 방법을 배웁니다. 이를 통해 이러한 엔드포인트를 쉽고 에이전트형 앱의 일부로 만들면서 Azure API Management의 기능을 활용할 수 있습니다.

## 주요 기능

- 노출할 도구로 사용할 엔드포인트 메서드를 선택합니다.
- 추가 기능은 API의 정책 섹션에서 구성한 내용에 따라 달라집니다. 여기서는 요율 제한 설정 방법을 보여드립니다.

## 사전 단계: API 가져오기

Azure API Management에 이미 API가 있다면 좋지만, 없다면 이 링크를 참고하세요, [Azure API Management에 API 가져오기](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API를 MCP 서버로 노출하기

API 엔드포인트를 노출하기 위해 다음 단계를 따라갑니다:

1. Azure 포털에 접속하여 다음 주소로 이동합니다 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
API Management 인스턴스로 이동합니다.

1. 왼쪽 메뉴에서 APIs > MCP Servers > + 새 MCP 서버 만들기를 선택합니다.

1. API에서 REST API를 선택하여 MCP 서버로 노출합니다.

1. 도구로 노출할 하나 이상의 API 작업을 선택합니다. 모든 작업을 선택할 수도 있고 특정 작업만 선택할 수도 있습니다.

    ![도구로 노출할 메서드 선택](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. <strong>만들기</strong>를 선택합니다.

1. 메뉴 옵션 <strong>APIs</strong>와 <strong>MCP Servers</strong>로 이동하면 다음과 같은 화면을 볼 수 있습니다:

    ![메인 창에서 MCP 서버 보기](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 서버가 생성되었고 API 작업이 도구로 노출되었습니다. MCP 서버가 MCP Servers 패널에 나열됩니다. URL 열에는 테스트용 또는 클라이언트 애플리케이션 내에서 호출할 수 있는 MCP 서버의 엔드포인트가 표시됩니다.

## 선택사항: 정책 구성

Azure API Management에는 엔드포인트에 대해 요율 제한 또는 시맨틱 캐싱과 같은 다양한 규칙을 설정하는 핵심 개념인 정책이 있습니다. 이 정책들은 XML로 작성됩니다.

MCP 서버의 요율 제한 정책을 설정하는 방법은 다음과 같습니다:

1. 포털에서 APIs 아래의 <strong>MCP Servers</strong>를 선택합니다.

1. 생성한 MCP 서버를 선택합니다.

1. 왼쪽 메뉴에서 MCP 아래의 <strong>Policies</strong>를 선택합니다.

1. 정책 편집기에서 MCP 서버의 도구에 적용할 정책을 추가하거나 편집합니다. 정책은 XML 형식으로 정의됩니다. 예를 들어, MCP 서버의 도구에 대한 호출을 클라이언트 IP별로 30초당 5회로 제한하는 정책을 추가할 수 있습니다. 다음은 해당 요율 제한을 구현하는 XML입니다:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    정책 편집기 화면은 다음과 같습니다:

    ![정책 편집기](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## 사용해 보기

MCP 서버가 의도대로 작동하는지 확인해봅시다.

> [!NOTE]
> Azure API Management는 현재 이 서버를 스트리머블 HTTP `/mcp` 엔드포인트를 통해 노출합니다.
> 이전의 HTTP+SSE `/sse` 전송 방식은 더 이상 권장되지 않으며
> 레거시 클라이언트에서만 사용해야 합니다.

이를 위해 Visual Studio Code와 GitHub Copilot의 에이전트 모드를 사용합니다. MCP 서버를 <em>mcp.json</em>에 추가할 것입니다. 이렇게 하면 Visual Studio Code가 에이전트 기능을 가진 클라이언트 역할을 하며 최종 사용자가 프롬프트를 입력하여 해당 서버와 상호작용할 수 있습니다.

Visual Studio Code에서 MCP 서버를 추가하는 방법은 다음과 같습니다:

1. 명령 팔레트에서 MCP: <strong>서버 추가 명령을 사용</strong>합니다.

1. 프롬프트가 뜨면 서버 유형을 선택합니다: **HTTP (HTTP 또는 서버 전송 이벤트)**.

1. API Management에서 MCP 서버에 대해 표시된 스트리머블 HTTP URL을 입력합니다.
    예를 들면:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. 원하는 서버 ID를 입력합니다. 이는 중요한 값은 아니지만 이 서버 인스턴스를 기억하는데 도움이 됩니다.

1. 구성을 작업 공간 설정 또는 사용자 설정에 저장할지 선택합니다.

  - **작업 공간 설정** - 서버 구성이 .vscode/mcp.json 파일에 저장되어 현재 작업 공간에서만 사용할 수 있습니다.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **사용자 설정** - 서버 구성이 전역 *settings.json* 파일에 추가되어 모든 작업 공간에서 사용할 수 있습니다. 구성은 다음과 유사합니다:

    ![사용자 설정](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Azure API Management에 올바르게 인증되는지 확인하기 위해 헤더를 추가하여 구성해야 합니다. 헤더 이름은 **Ocp-Apim-Subscription-Key** 입니다.

    - 설정에 추가하는 방법은 다음과 같습니다:

    ![인증용 헤더 추가](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), 이로 인해 프롬프트가 표시되어 Azure 포털에서 Azure API Management 인스턴스의 API 키 값을 입력하도록 합니다.

   - 대신 <em>mcp.json</em>에 추가하려면 다음과 같이 할 수 있습니다:

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

### 에이전트 모드 사용하기

이제 설정에 구성하거나 <em>.vscode/mcp.json</em>에 모두 설정을 완료했습니다. 사용해 봅시다.

도구 아이콘이 나타나고, 여기에서 서버에서 노출한 도구 목록을 볼 수 있어야 합니다:

![서버의 도구들](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 도구 아이콘을 클릭하면 다음과 같은 도구 목록을 볼 수 있습니다:

    ![도구 목록](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. 채팅에 프롬프트를 입력하여 도구를 호출합니다. 예를 들어 주문 관련 정보를 얻는 도구를 선택했다면, 에이전트에게 주문에 대해 물어볼 수 있습니다. 예시 프롬프트는 다음과 같습니다:

    ```text
    get information from order 2
    ```

    이제 도구 아이콘이 나타나 도구 호출을 계속할지 묻습니다. 계속 실행을 선택하면 다음과 같은 결과를 볼 수 있습니다:

    ![프롬프트 결과](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **위 이미지에서 보는 내용은 설정한 도구에 따라 다르지만, 기본적으로 위와 같은 텍스트 응답을 받게 됩니다**


## 참고 자료

더 자세히 알고 싶다면 다음을 참고하세요:

- [Azure API Management와 MCP 튜토리얼](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 샘플: Azure API Management를 사용한 안전한 원격 MCP 서버(실험적)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 클라이언트 인증 실습](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code용 Azure API Management 확장 기능으로 API 가져오기 및 관리하기](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center에서 원격 MCP 서버 등록 및 검색](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management와 함께 여러 AI 기능을 보여주는 훌륭한 저장소
- [AI Gateway 워크숍](https://azure-samples.github.io/AI-Gateway/) Azure 포털을 활용한 워크숍 포함, AI 기능 평가를 시작하기 좋은 방법

## 다음 단계

- 이전으로: [사례 연구 개요](./README.md)
- 다음으로: [Azure AI 여행 에이전트](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->