# Lesson: 웹 검색 MCP 서버 구축

이 장에서는 외부 API와 통합하고, 다양한 데이터 유형을 처리하며, 오류를 관리하고, 여러 도구를 조율하는 실제 AI 에이전트를 만드는 방법을 보여줍니다. 모두 프로덕션 환경에 적합한 형태로 구현합니다. 다음 내용을 다룹니다:

- **인증이 필요한 외부 API 통합**
- **여러 엔드포인트에서 다양한 데이터 유형 처리**
- **견고한 오류 처리 및 로깅 전략**
- **단일 서버에서 다중 도구 조율**

마지막에는 고급 AI 및 LLM 기반 애플리케이션에 필수적인 패턴과 모범 사례를 실습할 수 있습니다.

## 소개

이번 수업에서는 SerpAPI를 사용해 실시간 웹 데이터를 통해 LLM 기능을 확장하는 고급 MCP 서버와 클라이언트를 만드는 방법을 배웁니다. 이는 최신 정보를 웹에서 실시간으로 가져오는 동적 AI 에이전트를 개발하는 데 중요한 기술입니다.

## 학습 목표

이 수업을 마치면 다음을 할 수 있습니다:

- SerpAPI 같은 외부 API를 안전하게 MCP 서버에 통합하기
- 웹, 뉴스, 상품 검색, Q&A를 위한 여러 도구 구현하기
- LLM이 활용할 수 있도록 구조화된 데이터 파싱 및 포맷팅하기
- 오류 처리 및 API 호출 제한 관리 효과적으로 수행하기
- 자동화 및 대화형 MCP 클라이언트 구축 및 테스트하기

## 웹 검색 MCP 서버

이 섹션에서는 웹 검색 MCP 서버의 아키텍처와 기능을 소개합니다. FastMCP와 SerpAPI를 함께 사용해 실시간 웹 데이터로 LLM 기능을 확장하는 방법을 살펴봅니다.

### 개요

이 구현은 MCP가 다양한 외부 API 기반 작업을 안전하고 효율적으로 처리할 수 있음을 보여주는 네 가지 도구를 포함합니다:

- **general_search**: 광범위한 웹 검색용
- **news_search**: 최신 뉴스 헤드라인용
- **product_search**: 전자상거래 데이터용
- **qna**: 질문과 답변 스니펫용

### 특징
- **코드 예제**: Python용 언어별 코드 블록 포함 (다른 언어로도 쉽게 확장 가능), 명확한 이해를 위한 코드 피벗 사용

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

클라이언트를 실행하기 전에 서버가 하는 일을 이해하는 것이 도움이 됩니다. [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) 파일은 MCP 서버를 구현하며, SerpAPI와 통합해 웹, 뉴스, 상품 검색, Q&A 도구를 제공합니다. 들어오는 요청을 처리하고, API 호출을 관리하며, 응답을 파싱해 구조화된 결과를 클라이언트에 반환합니다.

전체 구현은 [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py)에서 확인할 수 있습니다.

아래는 서버가 도구를 정의하고 등록하는 간단한 예시입니다:

### Python 서버

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **외부 API 통합**: API 키와 외부 요청을 안전하게 처리하는 방법 시연
- **구조화된 데이터 파싱**: API 응답을 LLM 친화적인 형식으로 변환하는 방법
- **오류 처리**: 적절한 로깅과 함께 견고한 오류 처리 구현
- **대화형 클라이언트**: 자동화 테스트와 대화형 모드 모두 포함
- **컨텍스트 관리**: MCP Context를 활용해 로깅 및 요청 추적 수행

## 사전 준비 사항

시작하기 전에 환경이 올바르게 설정되었는지 확인하세요. 이 단계는 모든 의존성이 설치되고 API 키가 올바르게 구성되어 원활한 개발과 테스트가 가능하도록 합니다.

- Python 3.8 이상
- SerpAPI API 키 (가입은 [SerpAPI](https://serpapi.com/)에서 - 무료 플랜 제공)

## 설치

환경 설정을 위해 다음 단계를 따르세요:

1. uv(권장) 또는 pip로 의존성 설치:

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. 프로젝트 루트에 `.env` 파일을 만들고 SerpAPI 키를 추가:

```
SERPAPI_KEY=your_serpapi_key_here
```

## 사용법

웹 검색 MCP 서버는 SerpAPI와 통합해 웹, 뉴스, 상품 검색, Q&A 도구를 제공하는 핵심 컴포넌트입니다. 들어오는 요청을 처리하고, API 호출을 관리하며, 응답을 파싱해 구조화된 결과를 클라이언트에 반환합니다.

전체 구현은 [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py)에서 확인할 수 있습니다.

### 서버 실행

MCP 서버를 시작하려면 다음 명령어를 사용하세요:

```bash
python server.py
```

서버는 stdio 기반 MCP 서버로 실행되며, 클라이언트가 직접 연결할 수 있습니다.

### 클라이언트 모드

클라이언트(`client.py`)는 MCP 서버와 상호작용할 수 있는 두 가지 모드를 지원합니다:

- **일반 모드**: 모든 도구를 자동으로 테스트하고 응답을 검증합니다. 서버와 도구가 정상 작동하는지 빠르게 확인할 때 유용합니다.
- **대화형 모드**: 메뉴 기반 인터페이스를 시작해 도구를 수동으로 선택하고 호출하며, 직접 쿼리를 입력하고 실시간으로 결과를 확인할 수 있습니다. 서버 기능을 탐색하고 다양한 입력을 실험할 때 적합합니다.

전체 구현은 [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py)에서 확인할 수 있습니다.

### 클라이언트 실행

자동화 테스트 실행 (서버도 자동 시작됨):

```bash
python client.py
```

또는 대화형 모드 실행:

```bash
python client.py --interactive
```

### 다양한 방법으로 테스트하기

필요와 작업 흐름에 따라 서버가 제공하는 도구를 테스트하고 상호작용하는 여러 방법이 있습니다.

#### MCP Python SDK로 맞춤 테스트 스크립트 작성하기
MCP Python SDK를 사용해 직접 테스트 스크립트를 만들 수도 있습니다:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

여기서 "테스트 스크립트"란 MCP 서버의 클라이언트 역할을 하는 맞춤 Python 프로그램을 의미합니다. 정식 단위 테스트가 아니라, 프로그래밍 방식으로 서버에 연결해 원하는 도구를 호출하고 결과를 확인할 수 있습니다. 이 방법은 다음에 유용합니다:
- 도구 호출 프로토타입 제작 및 실험
- 서버가 다양한 입력에 어떻게 반응하는지 검증
- 반복적인 도구 호출 자동화
- MCP 서버 위에 자신만의 워크플로우나 통합 구축

테스트 스크립트를 사용해 새 쿼리를 빠르게 시도하거나 도구 동작을 디버깅할 수 있으며, 더 고급 자동화의 출발점으로도 활용할 수 있습니다. 아래는 MCP Python SDK를 사용해 스크립트를 만드는 예시입니다:

## 도구 설명

서버가 제공하는 다음 도구들을 사용해 다양한 검색과 쿼리를 수행할 수 있습니다. 각 도구의 파라미터와 사용 예시는 아래에 설명되어 있습니다.

이 섹션에서는 사용 가능한 각 도구와 그 파라미터에 대해 자세히 다룹니다.

### general_search

일반 웹 검색을 수행하고 포맷된 결과를 반환합니다.

**도구 호출 방법:**

MCP Python SDK를 사용해 직접 스크립트에서 `general_search`를 호출하거나, Inspector 또는 대화형 클라이언트 모드에서 상호작용할 수 있습니다. SDK 사용 예시는 다음과 같습니다:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

또는 대화형 모드에서 메뉴에서 `general_search`를 선택하고 쿼리를 입력하세요.

**파라미터:**
- `query` (문자열): 검색 쿼리

**요청 예시:**

```json
{
  "query": "latest AI trends"
}
```

### news_search

쿼리와 관련된 최신 뉴스 기사를 검색합니다.

**도구 호출 방법:**

MCP Python SDK를 사용해 직접 스크립트에서 `news_search`를 호출하거나, Inspector 또는 대화형 클라이언트 모드에서 상호작용할 수 있습니다. SDK 사용 예시는 다음과 같습니다:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

또는 대화형 모드에서 메뉴에서 `news_search`를 선택하고 쿼리를 입력하세요.

**파라미터:**
- `query` (문자열): 검색 쿼리

**요청 예시:**

```json
{
  "query": "AI policy updates"
}
```

### product_search

쿼리에 맞는 상품을 검색합니다.

**도구 호출 방법:**

MCP Python SDK를 사용해 직접 스크립트에서 `product_search`를 호출하거나, Inspector 또는 대화형 클라이언트 모드에서 상호작용할 수 있습니다. SDK 사용 예시는 다음과 같습니다:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

또는 대화형 모드에서 메뉴에서 `product_search`를 선택하고 쿼리를 입력하세요.

**파라미터:**
- `query` (문자열): 상품 검색 쿼리

**요청 예시:**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

검색 엔진에서 질문에 대한 직접 답변을 가져옵니다.

**도구 호출 방법:**

MCP Python SDK를 사용해 직접 스크립트에서 `qna`를 호출하거나, Inspector 또는 대화형 클라이언트 모드에서 상호작용할 수 있습니다. SDK 사용 예시는 다음과 같습니다:

# [Python Example](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

또는 대화형 모드에서 메뉴에서 `qna`를 선택하고 질문을 입력하세요.

**파라미터:**
- `question` (문자열): 답변을 찾을 질문

**요청 예시:**

```json
{
  "question": "what is artificial intelligence"
}
```

## 코드 상세

이 섹션에서는 서버와 클라이언트 구현에 대한 코드 스니펫과 참조를 제공합니다.

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

전체 구현은 [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py)와 [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py)에서 확인하세요.

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## 이 수업의 고급 개념

구축을 시작하기 전에, 이 장 전반에 걸쳐 등장할 중요한 고급 개념들을 소개합니다. 이들을 이해하면 처음 접하는 분도 내용을 따라가기 쉬울 것입니다:

- **다중 도구 조율**: 웹 검색, 뉴스 검색, 상품 검색, Q&A 등 여러 도구를 단일 MCP 서버에서 실행하는 것을 의미합니다. 서버가 다양한 작업을 처리할 수 있게 합니다.
- **API 호출 제한 관리**: SerpAPI 같은 외부 API는 일정 시간 내 요청 횟수를 제한합니다. 좋은 코드는 이 제한을 감지하고 우아하게 처리해 앱이 중단되지 않도록 합니다.
- **구조화된 데이터 파싱**: API 응답은 종종 복잡하고 중첩되어 있습니다. 이 개념은 응답을 LLM이나 다른 프로그램이 쉽게 사용할 수 있는 깔끔한 형식으로 변환하는 것입니다.
- **오류 복구**: 네트워크 문제나 예상치 못한 API 응답 등 오류가 발생할 때, 코드가 문제를 처리하고 유용한 피드백을 제공하며 중단되지 않도록 하는 것을 의미합니다.
- **파라미터 검증**: 도구에 전달되는 모든 입력이 올바르고 안전한지 확인하는 과정입니다. 기본값 설정과 타입 검증을 포함해 버그와 혼란을 방지합니다.

이 섹션은 웹 검색 MCP 서버 작업 중 마주칠 수 있는 일반적인 문제를 진단하고 해결하는 데 도움을 줍니다. 오류나 예상치 못한 동작이 발생하면 이 문제 해결 섹션을 먼저 확인하세요. 대부분의 문제는 여기서 제시하는 팁으로 빠르게 해결할 수 있습니다.

## 문제 해결

웹 검색 MCP 서버를 사용하다 보면 가끔 문제가 발생할 수 있습니다. 외부 API와 새로운 도구를 다룰 때는 흔한 일입니다. 이 섹션에서는 가장 흔한 문제에 대한 실용적인 해결책을 제공합니다. 문제가 생기면 여기서부터 시작하세요. 아래 팁들은 대부분의 사용자가 겪는 문제를 다루며, 추가 도움 없이도 문제를 해결할 수 있는 경우가 많습니다.

### 자주 발생하는 문제

아래는 사용자들이 자주 겪는 문제와 그에 대한 명확한 설명 및 해결 방법입니다:

1. **.env 파일에 SERPAPI_KEY 누락**
   - `SERPAPI_KEY environment variable not found` 오류가 나타나면, 애플리케이션이 SerpAPI 접근에 필요한 API 키를 찾지 못하는 것입니다. 이를 해결하려면 프로젝트 루트에 `.env` 파일을 만들고 `SERPAPI_KEY=your_serpapi_key_here` 형식으로 키를 추가하세요. `your_serpapi_key_here`는 SerpAPI 웹사이트에서 받은 실제 키로 바꿔야 합니다.

2. **모듈을 찾을 수 없다는 오류**
   - `ModuleNotFoundError: No module named 'httpx'` 같은 오류는 필요한 Python 패키지가 설치되지 않았을 때 발생합니다. 보통 의존성을 모두 설치하지 않았을 때 나타납니다. 터미널에서 `pip install -r requirements.txt`를 실행해 프로젝트에 필요한 모든 패키지를 설치하세요.

3. **연결 문제**
   - `Error during client execution` 같은 오류는 클라이언트가 서버에 연결하지 못하거나 서버가 정상적으로 실행되지 않을 때 발생합니다. 클라이언트와 서버가 호환되는 버전인지, `server.py`가 올바른 디렉터리에 있고 실행 중인지 확인하세요. 서버와 클라이언트를 모두 재시작하는 것도 도움이 됩니다.

4. **SerpAPI 오류**
   - `Search API returned error status: 401` 오류는 SerpAPI 키가 없거나 잘못되었거나 만료되었음을 의미합니다. SerpAPI 대시보드에서 키를 확인하고 `.env` 파일을 업데이트하세요. 키가 올바른데도 오류가 계속되면 무료 플랜의 할당량이 소진되었는지 확인하세요.

### 디버그 모드

기본적으로 앱은 중요한 정보만 로깅합니다. 문제를 진단하거나 자세한 내부 동작을 보고 싶다면 DEBUG 모드를 활성화할 수 있습니다. 이 모드는 앱이 수행하는 각 단계에 대한 더 많은 정보를 보여줍니다.

**예시: 일반 출력**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**예시: DEBUG 출력**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

DEBUG 모드에서는 HTTP 요청, 응답 및 기타 내부 세부 정보가 추가로 출력됩니다. 문제 해결에 매우 유용합니다.
DEBUG 모드를 활성화하려면 `client.py` 또는 `server.py` 상단에서 로깅 레벨을 DEBUG로 설정하세요:

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## 다음 단계

- [5.10 실시간 스트리밍](../mcp-realtimestreaming/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.