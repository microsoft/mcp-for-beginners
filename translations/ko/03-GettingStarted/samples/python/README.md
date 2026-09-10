# MCP 계산기 서버 (Python)



기본적인 계산기 기능을 제공하는 Python으로 구현된 간단한 모델 컨텍스트 프로토콜(MCP) 서버입니다.


## 설치

필요한 의존성을 설치하세요:

```bash
pip install -r requirements.txt
```

또는 MCP Python SDK를 직접 설치하세요:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

## 사용법

### 서버 실행하기

이 서버는 MCP 클라이언트(예: Claude Desktop)에서 사용되도록 설계되었습니다. 서버를 시작하려면:

```bash
python mcp_calculator_server.py
```

<strong>참고</strong>: 터미널에서 직접 실행하면 JSON-RPC 검증 오류가 나타납니다. 이는 정상 동작이며 서버가 올바르게 형식화된 MCP 클라이언트 메시지를 기다리고 있기 때문입니다.

### 기능 테스트하기

계산기 기능이 올바르게 작동하는지 테스트하려면:

```bash
python test_calculator.py
```

## 문제 해결

### 임포트 오류

`ModuleNotFoundError: No module named 'mcp'` 오류가 발생하면 MCP Python SDK를 설치하세요:

```bash
pip install "mcp>=2.1.1,<3.0.0"
```

### 직접 실행 시 JSON-RPC 오류

서버를 직접 실행할 때 "Invalid JSON: EOF while parsing a value" 같은 오류는 예상된 것입니다. 서버는 직접 터미널 입력이 아닌 MCP 클라이언트 메시지를 필요로 합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->