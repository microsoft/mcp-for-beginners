<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f01d4263fc6eec331615fef42429b720",
  "translation_date": "2025-06-18T18:17:20+00:00",
  "source_file": "03-GettingStarted/01-first-server/README.md",
  "language_code": "ko"
}
-->
### -2- 프로젝트 생성

이제 SDK를 설치했으니, 다음으로 프로젝트를 생성해 봅시다.

### -3- 프로젝트 파일 생성

### -4- 서버 코드 작성

### -5- 도구와 리소스 추가

다음 코드를 추가하여 도구와 리소스를 추가하세요.

### -6- 최종 코드

서버를 시작할 수 있도록 마지막 코드를 추가해 봅시다.

### -7- 서버 테스트

다음 명령어로 서버를 시작하세요.

### -8- 인스펙터로 실행하기

인스펙터는 서버를 시작하고 상호작용할 수 있게 해주는 훌륭한 도구입니다. 서버가 제대로 작동하는지 테스트해 보세요.

> [!NOTE]
> "command" 필드에 나오는 명령어는 특정 런타임에 맞춰 서버를 실행하는 명령어라 다르게 보일 수 있습니다.

다음과 같은 사용자 인터페이스가 표시될 것입니다:

![Connect](../../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ko.png)

1. "Connect" 버튼을 눌러 서버에 연결하세요.
   연결이 완료되면 다음 화면을 볼 수 있습니다:

   ![Connected](../../../../translated_images/connected.73d1e042c24075d386cacdd4ee7cd748c16364c277d814e646ff2f7b5eefde85.ko.png)

2. "Tools"에서 "listTools"를 선택하면 "Add"가 나타납니다. "Add"를 선택하고 매개변수 값을 입력하세요.

   그러면 다음과 같은 응답을 받게 됩니다. 즉, "add" 도구의 결과입니다:

   ![Result of running add](../../../../translated_images/ran-tool.a5a6ee878c1369ec1e379b81053395252a441799dbf23416c36ddf288faf8249.ko.png)

축하합니다! 첫 번째 서버를 성공적으로 만들고 실행했습니다!

### 공식 SDK

MCP는 여러 언어에 대한 공식 SDK를 제공합니다:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft와 협력하여 유지 관리
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI와 협력하여 유지 관리
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - 공식 TypeScript 구현체
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 공식 Python 구현체
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - 공식 Kotlin 구현체
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI와 협력하여 유지 관리
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - 공식 Rust 구현체

## 주요 내용 요약

- MCP 개발 환경 설정은 언어별 SDK 덕분에 간단합니다.
- MCP 서버를 구축할 때는 명확한 스키마를 가진 도구를 생성하고 등록합니다.
- 테스트와 디버깅은 신뢰할 수 있는 MCP 구현을 위해 필수적입니다.

## 샘플

- [Java 계산기](../samples/java/calculator/README.md)
- [.Net 계산기](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 계산기](../samples/javascript/README.md)
- [TypeScript 계산기](../samples/typescript/README.md)
- [Python 계산기](../../../../03-GettingStarted/samples/python)

## 과제

원하는 도구를 포함한 간단한 MCP 서버를 만들어 보세요:

1. 선호하는 언어(.NET, Java, Python, JavaScript)로 도구를 구현하세요.
2. 입력 매개변수와 반환 값을 정의하세요.
3. 인스펙터 도구를 실행해 서버가 의도대로 작동하는지 확인하세요.
4. 다양한 입력으로 구현을 테스트하세요.

## 솔루션

[솔루션](./solution/README.md)

## 추가 자료

- [Azure에서 Model Context Protocol로 에이전트 빌드하기](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps에서 원격 MCP (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP 에이전트](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## 다음 단계

다음: [MCP 클라이언트 시작하기](../02-client/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다했으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어의 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
