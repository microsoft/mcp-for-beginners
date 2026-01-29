# 샘플 실행하기

다음은 클래식 HTTP 스트리밍 서버와 클라이언트, 그리고 MCP 스트리밍 서버와 클라이언트를 Python으로 실행하는 방법입니다.

### 개요

- MCP 서버를 설정하여 항목을 처리하는 동안 진행 알림을 클라이언트로 스트리밍합니다.
- 클라이언트는 실시간으로 각 알림을 표시합니다.
- 이 가이드는 사전 요구사항, 설정, 실행 및 문제 해결을 다룹니다.

### 사전 요구사항

- Python 3.9 이상
- `mcp` Python 패키지 (`pip install mcp`로 설치)

### 설치 및 설정

1. 저장소를 클론하거나 솔루션 파일을 다운로드합니다.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **가상 환경을 생성하고 활성화합니다 (권장):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **필요한 종속성을 설치합니다:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### 파일

- **서버:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **클라이언트:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### 클래식 HTTP 스트리밍 서버 실행하기

1. 솔루션 디렉토리로 이동합니다:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. 클래식 HTTP 스트리밍 서버를 시작합니다:

   ```pwsh
   python server.py
   ```

3. 서버가 시작되며 다음과 같은 메시지가 표시됩니다:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### 클래식 HTTP 스트리밍 클라이언트 실행하기

1. 새 터미널을 열고 (같은 가상 환경과 디렉토리를 활성화):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. 스트리밍된 메시지가 순차적으로 출력되는 것을 볼 수 있습니다:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### MCP 스트리밍 서버 실행하기

1. 솔루션 디렉토리로 이동합니다:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. streamable-http 전송 방식으로 MCP 서버를 시작합니다:
   ```pwsh
   python server.py mcp
   ```
3. 서버가 시작되며 다음과 같은 메시지가 표시됩니다:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP 스트리밍 클라이언트 실행하기

1. 새 터미널을 열고 (같은 가상 환경과 디렉토리를 활성화):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. 서버가 각 항목을 처리할 때 실시간으로 알림이 출력되는 것을 볼 수 있습니다:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### 주요 구현 단계

1. **FastMCP를 사용하여 MCP 서버를 생성합니다.**
2. **목록을 처리하고 `ctx.info()` 또는 `ctx.log()`를 사용하여 알림을 보내는 도구를 정의합니다.**
3. **`transport="streamable-http"`로 서버를 실행합니다.**
4. **알림이 도착할 때 표시하는 메시지 핸들러를 구현한 클라이언트를 만듭니다.**

### 코드 설명
- 서버는 비동기 함수와 MCP 컨텍스트를 사용하여 진행 업데이트를 보냅니다.
- 클라이언트는 비동기 메시지 핸들러를 구현하여 알림과 최종 결과를 출력합니다.

### 팁 및 문제 해결

- 비동기 작업을 위해 `async/await`를 사용하세요.
- 서버와 클라이언트 모두에서 예외를 처리하여 안정성을 높이세요.
- 여러 클라이언트를 테스트하여 실시간 업데이트를 관찰하세요.
- 오류가 발생하면 Python 버전을 확인하고 모든 종속성이 설치되었는지 확인하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.