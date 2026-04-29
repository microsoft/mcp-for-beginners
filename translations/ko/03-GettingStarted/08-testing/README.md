## 테스트 및 디버깅

MCP 서버 테스트를 시작하기 전에, 사용 가능한 도구와 디버깅을 위한 모범 사례를 이해하는 것이 중요합니다. 효과적인 테스트는 서버가 예상대로 작동하는지 확인하고 문제를 신속하게 식별하고 해결하는 데 도움을 줍니다. 다음 섹션에서는 MCP 구현을 검증하기 위한 권장 접근 방식을 설명합니다.

## 개요

이 수업에서는 올바른 테스트 접근 방식을 선택하는 방법과 가장 효과적인 테스트 도구를 다룹니다.

## 학습 목표

이 수업을 마치면 다음을 수행할 수 있습니다:

- 다양한 테스트 접근 방식을 설명할 수 있습니다.
- 다양한 도구를 사용하여 코드를 효과적으로 테스트할 수 있습니다.

## MCP 서버 테스트

MCP는 서버 테스트 및 디버깅을 돕는 도구를 제공합니다:

- **MCP Inspector**: CLI 도구와 시각적 도구 모두로 실행할 수 있는 명령행 도구입니다.
- **수동 테스트**: curl과 같은 도구를 사용하여 웹 요청을 실행할 수 있지만 HTTP를 실행할 수 있는 모든 도구를 사용할 수 있습니다.
- **단위 테스트**: 선호하는 테스트 프레임워크를 사용하여 서버와 클라이언트의 기능을 테스트할 수 있습니다.

### MCP Inspector 사용하기

이 도구의 사용법은 이전 수업에서 설명했지만, 여기서는 간략히 말씀드리겠습니다. 이 도구는 Node.js로 만들어졌으며 `npx` 실행 파일을 호출하여 사용할 수 있습니다. `npx`는 도구를 일시적으로 다운로드 및 설치하고, 요청 실행이 완료되면 자동으로 정리합니다.

[MCP Inspector](https://github.com/modelcontextprotocol/inspector)는 다음을 도와줍니다:

- **서버 기능 발견**: 사용 가능한 리소스, 도구, 프롬프트를 자동으로 감지합니다.
- **도구 실행 테스트**: 다양한 매개변수를 시도하고 실시간으로 응답을 확인할 수 있습니다.
- **서버 메타데이터 보기**: 서버 정보, 스키마 및 구성을 검토할 수 있습니다.

도구를 실행하는 일반적인 방법은 다음과 같습니다:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

위 명령어는 MCP 및 시각적 인터페이스를 시작하고 브라우저에서 로컬 웹 인터페이스를 실행합니다. 등록된 MCP 서버, 사용 가능한 도구, 리소스 및 프롬프트가 표시되는 대시보드가 나타납니다. 이 인터페이스를 통해 도구 실행을 대화식으로 테스트하고, 서버 메타데이터를 검사하며, 실시간 응답을 볼 수 있으므로 MCP 서버 구현을 검증하고 디버깅하기가 쉽습니다.

다음은 화면 예시입니다: ![Inspector](../../../../translated_images/ko/connect.141db0b2bd05f096.webp)

또한 `--cli` 속성을 추가하여 CLI 모드로도 이 도구를 실행할 수 있습니다. 다음은 서버의 모든 도구를 나열하는 "CLI" 모드에서 도구를 실행하는 예입니다:

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### 수동 테스트

서버 기능 테스트를 위해 Inspector 도구를 실행하는 것 이외에도, curl과 같이 HTTP를 사용할 수 있는 클라이언트를 실행하는 유사한 방법이 있습니다.

curl을 사용하면 MCP 서버를 HTTP 요청으로 직접 테스트할 수 있습니다:

```bash
# 예: 테스트 서버 메타데이터
curl http://localhost:3000/v1/metadata

# 예: 도구 실행
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

위 curl 사용 예에서 보듯이, 도구 이름과 매개변수로 구성된 페이로드를 사용하여 POST 요청으로 도구를 호출합니다. 자신에게 가장 적합한 방법을 사용하세요. 일반적으로 CLI 도구는 사용 속도가 빠르고 스크립트 작성에 적합하여 CI/CD 환경에서 유용할 수 있습니다.

### 단위 테스트

도구와 리소스가 기대한 대로 작동하는지 확인하기 위해 단위 테스트를 작성하세요. 다음은 일부 테스트 예제 코드입니다.

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# 비동기 테스트를 위해 전체 모듈 표시
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # 몇 가지 테스트 도구 생성
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # 커서 매개변수 없이 테스트 (생략됨)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # cursor=None으로 테스트
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # 문자열로서의 커서로 테스트
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # 빈 문자열 커서로 테스트
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

위 코드는 다음과 같은 작업을 수행합니다:

- 함수로 테스트를 작성하고 assert 문을 사용할 수 있는 pytest 프레임워크를 활용합니다.
- 두 가지 다른 도구를 포함하는 MCP 서버를 만듭니다.
- 특정 조건이 충족되었는지 확인하기 위해 `assert` 문을 사용합니다.

[전체 파일 보기](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

위 파일을 참고하여 자신의 서버가 예상대로 기능을 생성하는지 테스트할 수 있습니다.

모든 주요 SDK는 유사한 테스트 섹션을 가지고 있으므로 선택한 런타임에 맞게 조정할 수 있습니다.

## 샘플

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## 추가 자료

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 다음 단계

- 다음: [배포](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하였으나, 자동 번역은 오류나 부정확성이 있을 수 있음을 알려드립니다. 원본 문서의 원어가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 모든 오해나 오역에 대해 당사는 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->