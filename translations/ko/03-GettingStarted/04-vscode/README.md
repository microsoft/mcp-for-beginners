<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0eb9557780cd0a2551cdb8a16c886b51",
  "translation_date": "2025-06-17T15:27:43+00:00",
  "source_file": "03-GettingStarted/04-vscode/README.md",
  "language_code": "ko"
}
-->
다음 섹션에서는 시각적 인터페이스를 어떻게 사용하는지 더 자세히 이야기해 보겠습니다.

## 접근 방법

고수준에서 다음과 같이 접근해야 합니다:

- MCP 서버를 찾기 위한 설정 파일을 구성합니다.
- 해당 서버를 시작하거나 연결하여 서버가 제공하는 기능 목록을 가져옵니다.
- GitHub Copilot Chat 인터페이스를 통해 해당 기능들을 사용합니다.

좋습니다, 이제 흐름을 이해했으니 Visual Studio Code를 통해 MCP 서버를 사용하는 연습을 해봅시다.

## 연습: 서버 사용하기

이번 연습에서는 Visual Studio Code가 MCP 서버를 찾을 수 있도록 설정하여 GitHub Copilot Chat 인터페이스에서 사용할 수 있도록 구성합니다.

### -0- 사전 단계, MCP 서버 검색 활성화

MCP 서버 검색을 활성화해야 할 수도 있습니다.

1. `File -> Preferences -> Settings`로 이동한 후 settings.json 파일에서 ` in Visual Studio Code.

1. Search for "MCP" and enable `chat.mcp.discovery.enabled 값을 확인하세요.

### -1- 설정 파일 생성

프로젝트 루트에 설정 파일을 만드세요. MCP.json이라는 파일을 .vscode 폴더 안에 넣어야 합니다. 파일은 다음과 같이 생겼어야 합니다:

```text
.vscode
|-- mcp.json
```

다음으로 서버 항목을 추가하는 방법을 살펴봅시다.

### -2- 서버 구성

*mcp.json*에 다음 내용을 추가하세요:

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

위 예시는 Node.js로 작성된 서버를 시작하는 간단한 예입니다. 다른 런타임의 경우 `command` and `args`를 사용하여 서버 시작 명령을 정확히 지정하세요.

### -3- 서버 시작하기

항목을 추가했으니 이제 서버를 시작해 봅시다:

1. *mcp.json*에서 본인의 항목을 찾아 "재생" 아이콘을 확인하세요:

  ![Visual Studio Code에서 서버 시작](../../../../translated_images/vscode-start-server.8e3c986612e3555de47e5b1e37b2f3020457eeb6a206568570fd74a17e3796ad.ko.png)  

1. "재생" 아이콘을 클릭하면 GitHub Copilot Chat의 도구 아이콘에 사용 가능한 도구 수가 늘어난 것을 볼 수 있습니다. 도구 아이콘을 클릭하면 등록된 도구 목록이 표시됩니다. 각 도구를 선택하거나 해제하여 GitHub Copilot이 도구를 컨텍스트로 사용할지 결정할 수 있습니다:

  ![Visual Studio Code에서 도구 확인](../../../../translated_images/vscode-tool.0b3bbea2fb7d8c26ddf573cad15ef654e55302a323267d8ee6bd742fe7df7fed.ko.png)

1. 도구를 실행하려면, 도구 설명과 일치하는 프롬프트를 입력하세요. 예를 들어 "add 22 to 1" 같은 프롬프트입니다:

  ![GitHub Copilot에서 도구 실행](../../../../translated_images/vscode-agent.d5a0e0b897331060518fe3f13907677ef52b879db98c64d68a38338608f3751e.ko.png)

  그러면 23이라는 응답을 볼 수 있을 것입니다.

## 과제

*mcp.json* 파일에 서버 항목을 추가하고 서버를 시작/중지할 수 있는지 확인하세요. 또한 GitHub Copilot Chat 인터페이스를 통해 서버 도구들과 통신할 수 있는지 확인하세요.

## 해결책

[해결책](./solution/README.md)

## 주요 내용 정리

이번 장의 주요 내용은 다음과 같습니다:

- Visual Studio Code는 여러 MCP 서버와 그 도구들을 사용할 수 있게 해주는 훌륭한 클라이언트입니다.
- GitHub Copilot Chat 인터페이스가 서버와 상호작용하는 방법입니다.
- 사용자에게 API 키 같은 입력값을 프롬프트로 받아 *mcp.json* 파일에서 서버 항목을 구성할 때 MCP 서버로 전달할 수 있습니다.

## 샘플

- [Java 계산기](../samples/java/calculator/README.md)
- [.Net 계산기](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 계산기](../samples/javascript/README.md)
- [TypeScript 계산기](../samples/typescript/README.md)
- [Python 계산기](../../../../03-GettingStarted/samples/python)

## 추가 자료

- [Visual Studio 문서](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

## 다음 단계

- 다음: [SSE 서버 만들기](../05-sse-server/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서는 해당 언어의 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
