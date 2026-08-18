# GitHub Copilot 에이전트 모드에서 서버 사용하기

Visual Studio Code와 GitHub Copilot은 클라이언트 역할을 하여 MCP 서버를 소비할 수 있습니다. 왜 이렇게 하려 할까요? MCP 서버가 제공하는 모든 기능을 IDE 내에서 사용할 수 있기 때문입니다. 예를 들어 GitHub의 MCP 서버를 추가하면 터미널에서 특정 명령어를 입력하는 대신 프롬프트를 통해 GitHub를 제어할 수 있습니다. 또는 자연어로 제어할 수 있는 개발자 경험을 향상시키는 모든 것을 상상해 보세요. 이제 그 장점을 이해하기 시작하셨죠?

## 개요

이 강의에서는 Visual Studio Code와 GitHub Copilot 에이전트 모드를 MCP 서버의 클라이언트로 사용하는 방법을 다룹니다.

## 학습 목표

이 강의가 끝나면 다음을 할 수 있습니다:

- Visual Studio Code를 통해 MCP 서버를 소비합니다.
- GitHub Copilot을 통해 도구 같은 기능을 실행합니다.
- Visual Studio Code를 설정하여 MCP 서버를 찾고 관리합니다.

## 사용법

MCP 서버를 제어하는 두 가지 방법이 있습니다:

- 사용자 인터페이스(이 챕터 후반에 방법을 설명합니다).
- 터미널, `code` 실행 파일을 사용하여 터미널에서 제어할 수 있습니다:

  사용자 프로필에 MCP 서버를 추가하려면 --add-mcp 명령줄 옵션을 사용하고 JSON 서버 구성을 {\"name\":\"server-name\",\"command\":...} 형태로 제공하세요.

  ```
  code --add-mcp "{\"name\":\"my-server\",\"command\": \"uvx\",\"args\": [\"mcp-server-fetch\"]}"
  ```

### 스크린샷

![Visual Studio Code에서 안내되는 MCP 서버 구성](../../../../translated_images/ko/chat-mode-agent.729a22473f822216.webp)
![에이전트 세션별 도구 선택](../../../../translated_images/ko/agent-mode-select-tools.522c7ba5df0848f8.webp)
![MCP 개발 중 오류 쉽게 디버깅](../../../../translated_images/ko/mcp-list-servers.fce89eefe3f30032.webp)

다음 섹션에서 시각적 인터페이스 사용법을 더 자세히 살펴보겠습니다.

## 접근 방법

전반적으로 다음과 같이 접근해야 합니다:

- MCP 서버를 찾을 구성 파일을 설정합니다.
- 서버를 시작/연결하여 기능 목록을 가져옵니다.
- GitHub Copilot 채팅 인터페이스를 통해 해당 기능을 사용합니다.

흐름을 이해했으니, 이제 연습 문제를 통해 Visual Studio Code에서 MCP 서버를 사용하는 방법을 살펴봅시다.

## 연습: 서버 사용하기

이 연습에서는 Visual Studio Code를 구성하여 MCP 서버를 찾아 GitHub Copilot 채팅 인터페이스에서 사용할 수 있도록 합니다.

### -0- 사전 단계, MCP 서버 검색 활성화하기

MCP 서버 검색을 활성화해야 할 수도 있습니다.

1. Visual Studio Code에서 `파일 -> 기본 설정 -> 설정`으로 이동합니다.

1. "MCP"를 검색하고 settings.json 파일에서 `chat.mcp.discovery.enabled`를 활성화하세요.

### -1- 구성 파일 만들기

프로젝트 루트에 구성 파일을 만듭니다. MCP.json이라는 파일이 필요하고, .vscode 폴더에 위치시켜야 합니다. 다음과 같은 형식이어야 합니다:

```text
.vscode
|-- mcp.json
```

다음으로, 서버 항목을 추가하는 방법을 살펴보겠습니다.

### -2- 서버 구성하기

<em>mcp.json</em>에 다음 내용을 추가하세요:

```json
{
    "inputs": [],
    "servers": {
       "hello-mcp": {
           "command": "node",
           "args": [
               "build/index.js"
           ]
       }
    }
}
```

위는 Node.js로 작성된 서버를 시작하는 간단한 예입니다. 다른 런타임의 경우 `command`와 `args`를 사용해 서버 시작에 적절한 명령어를 지정하세요.

### -3- 서버 시작하기

이제 항목을 추가했으니, 서버를 시작해 봅시다:

1. <em>mcp.json</em>에서 항목을 찾고 "재생" 아이콘이 있는지 확인하세요:

  ![Visual Studio Code에서 서버 시작하기](../../../../translated_images/ko/vscode-start-server.8e3c986612e3555d.webp)  

1. "재생" 아이콘을 클릭하면 GitHub Copilot 채팅의 도구 아이콘이 사용할 수 있는 도구 수를 늘려줍니다. 해당 도구 아이콘을 클릭하면 등록된 도구 목록이 표시됩니다. GitHub Copilot이 도구를 컨텍스트로 사용할지 도구별로 선택할 수 있습니다:

  ![Visual Studio Code에서 도구 보기](../../../../translated_images/ko/vscode-tool.0b3bbea2fb7d8c26.webp)

1. 도구를 실행하려면 도구 설명에 맞는 프롬프트를 입력하세요. 예를 들어 "1에 22 더하기" 같은 프롬프트를 입력합니다:

  ![GitHub Copilot에서 도구 실행하기](../../../../translated_images/ko/vscode-agent.d5a0e0b897331060.webp)

  23이라는 응답을 확인할 수 있을 것입니다.

## 과제

*mcp.json* 파일에 서버 항목을 추가하고 서버를 시작/중지할 수 있는지 확인하세요. 또한 GitHub Copilot 채팅 인터페이스를 통해 서버 도구와 통신할 수 있는지 확인하세요.

## 해결책

[해결책](./solution/README.md)

## 주요 내용 정리

이 장의 주요 내용은 다음과 같습니다:

- Visual Studio Code는 여러 MCP 서버와 도구를 소비할 수 있는 훌륭한 클라이언트입니다.
- GitHub Copilot 채팅 인터페이스가 서버와 상호작용하는 방법입니다.
- API 키 같은 사용자 입력을 프롬프트로 받아 *mcp.json* 파일에서 서버 구성 시 MCP 서버에 전달할 수 있습니다.

## 샘플

- [Java 계산기](../samples/java/calculator/README.md)
- [.Net 계산기](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 계산기](../samples/javascript/README.md)
- [TypeScript 계산기](../samples/typescript/README.md)
- [Python 계산기](../../../../03-GettingStarted/samples/python)

## 추가 자료

- [Visual Studio 문서](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## 다음 단계

- 다음: [stdio 서버 만들기](../05-stdio-server/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->