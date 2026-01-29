# MCP stdio 서버 솔루션

> **⚠️ 중요**: 이 솔루션은 MCP 사양 2025-06-18에 따라 권장되는 **stdio 전송**을 사용하도록 업데이트되었습니다. 기존의 SSE (Server-Sent Events) 전송은 더 이상 사용되지 않습니다.

다음은 각 런타임에서 stdio 전송을 사용하여 MCP 서버를 구축하기 위한 완전한 솔루션입니다:

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - 완전한 stdio 서버 구현
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - asyncio를 사용하는 Python stdio 서버
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - 의존성 주입을 사용하는 .NET stdio 서버

각 솔루션은 다음을 보여줍니다:
- stdio 전송 설정
- 서버 도구 정의
- 올바른 JSON-RPC 메시지 처리
- Claude와 같은 MCP 클라이언트와의 통합

모든 솔루션은 현재 MCP 사양을 따르며 최적의 성능과 보안을 위해 권장되는 stdio 전송을 사용합니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.