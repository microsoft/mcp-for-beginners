# Model Context Protocol (MCP) Python 구현

이 저장소에는 Model Context Protocol (MCP)의 Python 구현이 포함되어 있으며, MCP 표준을 사용하여 통신하는 서버와 클라이언트 애플리케이션을 만드는 방법을 보여줍니다.

## 개요

MCP 구현은 두 가지 주요 구성 요소로 이루어져 있습니다:

1. **MCP 서버 (`server.py`)** - 다음을 제공하는 서버:
   - **Tools**: 원격으로 호출할 수 있는 함수들
   - **Resources**: 가져올 수 있는 데이터
   - **Prompts**: 언어 모델용 프롬프트 템플릿

2. **MCP 클라이언트 (`client.py`)** - 서버에 연결하여 기능을 사용하는 클라이언트 애플리케이션

## 기능

이 구현은 여러 주요 MCP 기능을 보여줍니다:

### Tools
- `completion` - AI 모델로부터 텍스트 완성을 생성 (시뮬레이션)
- `add` - 두 숫자를 더하는 간단한 계산기

### Resources
- `models://` - 사용 가능한 AI 모델에 대한 정보 반환
- `greeting://{name}` - 주어진 이름에 대한 맞춤 인사 반환

### Prompts
- `review_code` - 코드 리뷰용 프롬프트 생성

## 설치

이 MCP 구현을 사용하려면 필요한 패키지를 설치하세요:

```powershell
pip install mcp-server mcp-client
```

## 서버 및 클라이언트 실행

### 서버 시작

한 터미널 창에서 서버를 실행하세요:

```powershell
python server.py
```

서버는 MCP CLI를 사용하여 개발 모드로도 실행할 수 있습니다:

```powershell
mcp dev server.py
```

또는 Claude Desktop에 설치하여 실행할 수도 있습니다 (사용 가능한 경우):

```powershell
mcp install server.py
```

### 클라이언트 실행

다른 터미널 창에서 클라이언트를 실행하세요:

```powershell
python client.py
```

이렇게 하면 서버에 연결되어 모든 기능을 시연합니다.

### 클라이언트 사용법

클라이언트(`client.py`)는 MCP의 모든 기능을 보여줍니다:

```powershell
python client.py
```

서버에 연결하여 tools, resources, prompts를 포함한 모든 기능을 사용합니다. 출력 결과는 다음을 보여줍니다:

1. 계산기 도구 결과 (5 + 7 = 12)
2. "What is the meaning of life?"에 대한 completion 도구 응답
3. 사용 가능한 AI 모델 목록
4. "MCP Explorer"에 대한 맞춤 인사
5. 코드 리뷰 프롬프트 템플릿

## 구현 세부사항

서버는 MCP 서비스를 정의하기 위한 고수준 추상화를 제공하는 `FastMCP` API를 사용하여 구현되었습니다. 다음은 도구가 정의되는 간단한 예시입니다:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

클라이언트는 MCP 클라이언트 라이브러리를 사용하여 서버에 연결하고 호출합니다:

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## 더 알아보기

MCP에 대한 자세한 정보는 다음을 방문하세요: https://modelcontextprotocol.io/

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.