# MCP 계산기 서버 (Python)

Python으로 구현된 간단한 Model Context Protocol (MCP) 서버로, 기본적인 계산기 기능을 제공합니다.

## 설치

필요한 종속성을 설치하세요:

```bash
pip install -r requirements.txt
```

또는 MCP Python SDK를 직접 설치하세요:

```bash
pip install mcp>=1.18.0
```

## 사용법

### 서버 실행

이 서버는 MCP 클라이언트(예: Claude Desktop)에서 사용하도록 설계되었습니다. 서버를 시작하려면:

```bash
python mcp_calculator_server.py
```

**참고**: 터미널에서 직접 실행할 경우 JSON-RPC 유효성 검사 오류가 표시될 수 있습니다. 이는 정상적인 동작이며, 서버는 올바르게 형식화된 MCP 클라이언트 메시지를 기다리고 있는 상태입니다.

### 함수 테스트

계산기 함수가 올바르게 작동하는지 테스트하려면:

```bash
python test_calculator.py
```

## 문제 해결

### Import 오류

`ModuleNotFoundError: No module named 'mcp'` 오류가 발생하면 MCP Python SDK를 설치하세요:

```bash
pip install mcp>=1.18.0
```

### 직접 실행 시 JSON-RPC 오류

서버를 직접 실행할 때 "Invalid JSON: EOF while parsing a value"와 같은 오류가 발생하는 것은 정상입니다. 서버는 MCP 클라이언트 메시지를 필요로 하며, 직접 터미널 입력을 처리하지 않습니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.