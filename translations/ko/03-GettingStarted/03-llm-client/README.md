<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "904b689eda5a68cbafe656d53f9787c7",
  "translation_date": "2025-06-17T18:46:33+00:00",
  "source_file": "03-GettingStarted/03-llm-client/README.md",
  "language_code": "ko"
}
-->
좋습니다, 다음 단계로 서버의 기능들을 나열해 봅시다.

### -2 서버 기능 나열하기

이제 서버에 연결하여 기능들을 요청해 보겠습니다:

### -3- 서버 기능을 LLM 도구로 변환하기

서버 기능을 나열한 다음 단계는 이를 LLM이 이해할 수 있는 형식으로 변환하는 것입니다. 이렇게 하면 이 기능들을 LLM에 도구로 제공할 수 있습니다.

좋아요, 이제 사용자 요청을 처리할 준비가 되어 있지 않으니, 다음으로 그것을 해결해 봅시다.

### -4- 사용자 프롬프트 요청 처리하기

이 코드 부분에서는 사용자 요청을 처리할 것입니다.

좋습니다, 해냈네요!

## 과제

연습에서 작성한 코드를 가져와서 서버에 더 많은 도구를 추가해 보세요. 그런 다음 연습처럼 LLM이 포함된 클라이언트를 만들어 다양한 프롬프트로 테스트하여 서버의 모든 도구가 동적으로 호출되는지 확인하세요. 이렇게 클라이언트를 구축하면 최종 사용자는 정확한 클라이언트 명령 대신 프롬프트를 사용하고, MCP 서버가 호출되는 사실을 알지 못해도 훌륭한 사용자 경험을 누릴 수 있습니다.

## 솔루션

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## 주요 내용 정리

- 클라이언트에 LLM을 추가하면 사용자가 MCP 서버와 더 나은 방식으로 상호작용할 수 있습니다.
- MCP 서버의 응답을 LLM이 이해할 수 있는 형태로 변환해야 합니다.

## 샘플

- [Java 계산기](../samples/java/calculator/README.md)
- [.Net 계산기](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 계산기](../samples/javascript/README.md)
- [TypeScript 계산기](../samples/typescript/README.md)
- [Python 계산기](../../../../03-GettingStarted/samples/python)

## 추가 자료

## 다음 단계

- 다음: [Visual Studio Code를 사용하여 서버 소비하기](../04-vscode/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 양지해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
