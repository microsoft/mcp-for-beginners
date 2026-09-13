# MCP 인스펙터로 디버깅하기

> [!NOTE]
> `--sse` 옵션과 `/sse`로 끝나는 URL을 사용하는 명령어는 기존 HTTP+SSE
> 전송 방식을 테스트합니다. 새로운 MCP `2026-07-28` 서버의 경우,
> 스트리머블 HTTP를 지원하는 인스펙터 버전을 사용하고 해당 전송 방식을 선택하세요.

<strong>MCP 인스펙터</strong>는 완전한 AI 호스트 애플리케이션 없이도 MCP 서버를 대화식으로 테스트하고 문제를 해결할 수 있게 해주는 필수 디버깅 도구입니다. 일종의 "MCP용 Postman"으로 생각할 수 있으며, 요청을 보내고, 응답을 확인하며, 서버 동작 방식을 이해할 수 있는 시각적 인터페이스를 제공합니다.

## 왜 MCP 인스펙터를 사용할까?

MCP 서버를 구축할 때 다음과 같은 문제에 자주 직면합니다:

- **"내 서버가 제대로 실행되고 있나요?"** - 인스펙터가 연결 상태를 보여줍니다
- **"도구가 올바르게 등록되었나요?"** - 인스펙터가 사용 가능한 모든 도구를 나열합니다
- **"응답 형식은 어떻게 되나요?"** - 인스펙터가 전체 JSON 응답을 표시합니다
- **"왜 이 도구가 작동하지 않나요?"** - 인스펙터가 자세한 오류 메시지를 보여줍니다

## 사전 준비물

- Node.js 18 이상 설치
- npm (Node.js에 포함)
- 테스트할 MCP 서버 ([모듈 3.1 - 첫 번째 서버](../01-first-server/README.md) 참조)

## 설치 방법

### 옵션 1: npx로 실행하기 (빠른 테스트 추천)

```bash
npx @modelcontextprotocol/inspector
```

### 옵션 2: 전역 설치

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### 옵션 3: 프로젝트에 추가하기

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

`package.json`에 추가:
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## 서버에 연결하기

### stdio 서버 (로컬 프로세스)

표준 입력/출력으로 통신하는 서버의 경우:

```bash
# 파이썬 서버
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js 서버
npx @modelcontextprotocol/inspector node ./build/index.js

# 환경 변수와 함께
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP 서버 (네트워크)

HTTP 서비스로 실행 중인 서버의 경우:

1. 먼저 서버를 시작하세요:
   ```bash
   python server.py  # 서버가 http://localhost:8080 에서 실행 중입니다
   ```

2. 인스펙터를 실행하고 연결하세요:
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## 인스펙터 인터페이스 개요

인스펙터가 실행되면 보통 `http://localhost:5173`에서 웹 인터페이스를 보게 됩니다:

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 도구 테스트

### 사용 가능한 도구 나열하기

1. **도구(Tools)** 탭을 클릭합니다
2. 인스펙터가 자동으로 `tools/list`를 호출합니다
3. 등록된 모든 도구가 다음과 함께 표시됩니다:
   - 도구 이름
   - 설명
   - 입력 스키마(매개변수)

### 도구 실행하기

1. 목록에서 도구를 선택합니다
2. 폼에 필요한 매개변수를 입력합니다
3. **도구 실행(Run Tool)** 버튼을 클릭합니다
4. 결과 패널에서 응답을 확인합니다

**예시: 계산기 도구 테스트**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### 도구 오류 디버깅

도구가 실패할 경우, 인스펙터는 다음을 보여줍니다:

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

일반적인 오류 코드:
| 코드 | 의미 |
|------|---------|
| -32700 | 파싱 오류 (잘못된 JSON) |
| -32600 | 잘못된 요청 |
| -32601 | 메서드 없음 |
| -32602 | 잘못된 매개변수 |
| -32603 | 내부 오류 |

---

## 리소스 테스트

### 리소스 목록 보기

1. **리소스(Resources)** 탭을 클릭합니다
2. 인스펙터가 `resources/list`를 호출합니다
3. 다음이 표시됩니다:
   - 리소스 URI
   - 이름과 설명
   - MIME 유형

### 리소스 읽기


1. 리소스 선택
2. **리소스 읽기** 클릭
3. 반환된 내용 보기

**예시 출력:**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## 프롬프트 테스트

### 프롬프트 목록

1. <strong>프롬프트</strong> 탭 클릭
2. 인스펙터가 `prompts/list` 호출
3. 사용 가능한 프롬프트 템플릿 보기

### 프롬프트 가져오기

1. 프롬프트 선택
2. 필요한 인수 입력
3. **프롬프트 가져오기** 클릭
4. 렌더링된 프롬프트 메시지 보기

---

## 메시지 로그 분석

메시지 로그는 모든 MCP 프로토콜 메시지를 보여줍니다. 아래 기록은
이전 `2025-11-25` 서버에서 가져온 것으로, 제거된 `initialize` 핸드셰이크가 포함되어 있습니다. 
`2026-07-28` 서버는 자체 포함된 요청 메타데이터와 `server/discover`를 사용합니다.


```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### 확인할 사항

- **요청/응답 쌍**: 각 `→`에는 대응하는 `←`가 있어야 함
- **오류 메시지**: 응답에서 `"error"` 확인
- <strong>타이밍</strong>: 큰 간격은 성능 문제를 나타낼 수 있음
- **프로토콜 버전**: 서버와 클라이언트가 버전에 동의해야 함

---

## VS Code 통합

VS Code에서 직접 Inspector를 실행할 수 있습니다:

### launch.json 사용하기

`.vscode/launch.json`에 추가:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### 작업(Tasks) 사용하기

`.vscode/tasks.json`에 추가:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## 일반적인 디버깅 시나리오

### 시나리오 1: 서버가 연결되지 않음

**증상:** Inspector에 "연결 끊김" 표시되거나 "연결 중..."에서 멈춤

**점검 목록:**
1. ✅ 서버 명령이 올바른가?
2. ✅ 모든 의존성이 설치되었는가?
3. ✅ 서버 경로가 절대 경로인지 또는 현재 디렉터리 기준 상대 경로인지?
4. ✅ 필요한 환경 변수가 설정되었는가?

**디버그 단계:**
```bash
# 먼저 서버를 수동으로 테스트하세요
python -c "import your_server_module; print('OK')"

# 가져오기 오류를 확인하세요
python -m your_server_module 2>&1 | head -20

# MCP SDK가 설치되었는지 확인하세요
pip show mcp
```

### 시나리오 2: 도구가 나타나지 않음

**증상:** 도구 탭에 빈 목록 표시

**가능한 원인:**
1. 서버 초기화 중 도구 미등록
2. 시작 후 서버 크래시
3. `tools/list` 핸들러가 빈 배열 반환

**디버그 단계:**
1. `tools/list` 응답을 메시지 로그에서 확인
2. 도구 등록 코드에 로깅 추가
3. `@mcp.tool()` 데코레이터가 존재하는지 확인 (Python)

### 시나리오 3: 도구가 오류 반환

**증상:** 도구 호출이 오류 응답 반환

**디버깅 접근법:**
1. 오류 메시지를 주의 깊게 읽기
2. 매개변수 타입이 스키마와 일치하는지 확인
3. 상세 오류 메시지를 포함한 try/catch 추가
4. 서버 로그에서 스택 트레이스 점검

**개선된 오류 처리 예시:**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # 도구 로직 여기
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### 시나리오 4: 리소스 내용이 비어 있음

**증상:** 리소스가 반환되나 내용이 비었거나 null임

**점검 목록:**
1. ✅ 파일 경로 또는 URI가 정확한가?
2. ✅ 서버에 리소스 읽기 권한이 있는가?
3. ✅ 리소스 내용이 올바르게 반환되고 있는가?

---

## 고급 Inspector 기능

### 사용자 지정 헤더 (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### 자세한 로깅

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### 세션 기록

Inspector는 메시지 로그를 내보내 나중에 분석할 수 있습니다:
1. 메시지 패널에서 **로그 내보내기** 클릭
2. JSON 파일 저장
3. 팀과 공유하여 디버깅

---


## 모범 사례

1. **일찍 그리고 자주 테스트하세요** - 문제가 발생할 때뿐만 아니라 개발 중에도 Inspector를 사용하세요
2. **간단하게 시작하세요** - 복잡한 도구 호출 전에 기본 연결성을 테스트하세요
3. **스키마를 확인하세요** - 많은 오류가 매개변수 유형 불일치에서 발생합니다
4. **오류 메시지를 읽으세요** - MCP 오류는 보통 설명이 잘 되어 있습니다
5. **Inspector를 열어 두세요** - 개발 중 문제를 잡는 데 도움이 됩니다

---

## 다음 단계

모듈 3: 시작하기를 완료했습니다! 학습을 계속하세요:

- [모듈 4: 실습 구현](../../04-PracticalImplementation/README.md)

---

## 추가 리소스

- [MCP Inspector GitHub 저장소](https://github.com/modelcontextprotocol/inspector)
- [MCP 명세 - 프로토콜 메시지](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 명세](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->