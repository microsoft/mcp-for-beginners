# MCP stdio 서버 - Python 솔루션

> **⚠️ 중요**: 이 솔루션은 MCP 사양 2025-06-18에 따라 권장되는 **stdio 전송**을 사용하도록 업데이트되었습니다. 기존 SSE 전송은 더 이상 사용되지 않습니다.

## 개요

이 Python 솔루션은 현재 stdio 전송을 사용하여 MCP 서버를 구축하는 방법을 보여줍니다. stdio 전송은 더 간단하고, 더 안전하며, 사용되지 않는 SSE 방식보다 성능이 뛰어납니다.

## 사전 요구사항

- Python 3.8 이상
- 패키지 관리를 위해 `uv` 설치를 권장합니다. [설치 방법](https://docs.astral.sh/uv/#highlights)을 참조하세요.

## 설정 지침

### 1단계: 가상 환경 생성

```bash
python -m venv venv
```

### 2단계: 가상 환경 활성화

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3단계: 종속성 설치

```bash
pip install mcp
```

## 서버 실행

stdio 서버는 이전 SSE 서버와 다르게 실행됩니다. 웹 서버를 시작하는 대신 stdin/stdout을 통해 통신합니다:

```bash
python server.py
```

**중요**: 서버가 멈춘 것처럼 보일 수 있습니다 - 정상입니다! 서버는 stdin에서 JSON-RPC 메시지를 기다리고 있습니다.

## 서버 테스트

### 방법 1: MCP Inspector 사용 (권장)

```bash
npx @modelcontextprotocol/inspector python server.py
```

이 작업은 다음을 수행합니다:
1. 서버를 하위 프로세스로 실행
2. 테스트를 위한 웹 인터페이스 열기
3. 모든 서버 도구를 대화형으로 테스트 가능

### 방법 2: 직접 JSON-RPC 테스트

JSON-RPC 메시지를 직접 보내는 방법으로도 테스트할 수 있습니다:

1. 서버 시작: `python server.py`
2. JSON-RPC 메시지 보내기 (예시):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. 서버가 사용 가능한 도구를 응답합니다.

### 사용 가능한 도구

서버는 다음 도구를 제공합니다:

- **add(a, b)**: 두 숫자를 더합니다.
- **multiply(a, b)**: 두 숫자를 곱합니다.  
- **get_greeting(name)**: 개인화된 인사말을 생성합니다.
- **get_server_info()**: 서버 정보를 가져옵니다.

### Claude Desktop과 함께 테스트하기

이 서버를 Claude Desktop에서 사용하려면 `claude_desktop_config.json`에 다음 구성을 추가하세요:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## SSE와의 주요 차이점

**stdio 전송 (현재):**
- ✅ 더 간단한 설정 - 웹 서버 불필요
- ✅ 더 나은 보안 - HTTP 엔드포인트 없음
- ✅ 하위 프로세스 기반 통신
- ✅ stdin/stdout을 통한 JSON-RPC
- ✅ 더 나은 성능

**SSE 전송 (사용 중지됨):**
- ❌ HTTP 서버 설정 필요
- ❌ 웹 프레임워크 (Starlette/FastAPI) 필요
- ❌ 더 복잡한 라우팅 및 세션 관리
- ❌ 추가적인 보안 고려 사항
- ❌ MCP 2025-06-18에서 사용 중지됨

## 디버깅 팁

- 로깅에는 `stderr`를 사용하세요 (`stdout`은 사용하지 마세요).
- Inspector를 사용하여 시각적 디버깅을 수행하세요.
- 모든 JSON 메시지가 줄바꿈으로 구분되어 있는지 확인하세요.
- 서버가 오류 없이 시작되는지 확인하세요.

이 솔루션은 현재 MCP 사양을 따르며 stdio 전송 구현을 위한 모범 사례를 보여줍니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.