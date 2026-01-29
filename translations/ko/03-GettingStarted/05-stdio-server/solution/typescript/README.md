# MCP stdio 서버 - TypeScript 솔루션

> **⚠️ 중요**: 이 솔루션은 MCP 사양 2025-06-18에서 권장하는 **stdio 전송**을 사용하도록 업데이트되었습니다. 기존의 SSE 전송은 더 이상 사용되지 않습니다.

## 개요

이 TypeScript 솔루션은 현재 stdio 전송을 사용하여 MCP 서버를 구축하는 방법을 보여줍니다. stdio 전송은 더 간단하고, 더 안전하며, 사용이 중단된 SSE 방식보다 성능이 뛰어납니다.

## 사전 요구 사항

- Node.js 18 이상
- npm 또는 yarn 패키지 관리자

## 설정 지침

### 1단계: 의존성 설치

```bash
npm install
```

### 2단계: 프로젝트 빌드

```bash
npm run build
```

## 서버 실행

stdio 서버는 이전 SSE 서버와 다르게 작동합니다. 웹 서버를 시작하는 대신 stdin/stdout을 통해 통신합니다:

```bash
npm start
```

**중요**: 서버가 멈춘 것처럼 보일 수 있습니다 - 이는 정상입니다! 서버는 stdin에서 JSON-RPC 메시지를 기다리고 있습니다.

## 서버 테스트

### 방법 1: MCP Inspector 사용 (권장)

```bash
npm run inspector
```

이 작업은 다음을 수행합니다:
1. 서버를 하위 프로세스로 실행
2. 테스트를 위한 웹 인터페이스 열기
3. 모든 서버 도구를 상호작용적으로 테스트 가능

### 방법 2: 명령줄에서 직접 테스트

Inspector를 직접 실행하여 테스트할 수도 있습니다:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### 사용 가능한 도구

서버는 다음 도구를 제공합니다:

- **add(a, b)**: 두 숫자를 더합니다
- **multiply(a, b)**: 두 숫자를 곱합니다  
- **get_greeting(name)**: 개인화된 인사말을 생성합니다
- **get_server_info()**: 서버 정보를 가져옵니다

### Claude Desktop으로 테스트

이 서버를 Claude Desktop에서 사용하려면, `claude_desktop_config.json`에 다음 구성을 추가하세요:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## 프로젝트 구조

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## SSE와의 주요 차이점

**stdio 전송 (현재):**
- ✅ 더 간단한 설정 - HTTP 서버가 필요 없음
- ✅ 더 나은 보안 - HTTP 엔드포인트 없음
- ✅ 하위 프로세스 기반 통신
- ✅ stdin/stdout을 통한 JSON-RPC
- ✅ 더 나은 성능

**SSE 전송 (사용 중단):**
- ❌ Express 서버 설정 필요
- ❌ 복잡한 라우팅 및 세션 관리 필요
- ❌ 더 많은 의존성 (Express, HTTP 처리)
- ❌ 추가적인 보안 고려 사항
- ❌ MCP 2025-06-18에서 사용 중단

## 개발 팁

- 로깅에는 `console.error()`를 사용하세요 (`console.log()`는 stdout에 기록되므로 사용하지 마세요)
- 테스트 전에 `npm run build`로 빌드하세요
- Inspector를 사용하여 시각적으로 디버깅하세요
- 모든 JSON 메시지가 올바르게 포맷되었는지 확인하세요
- 서버는 SIGINT/SIGTERM에서 자동으로 정상 종료를 처리합니다

이 솔루션은 현재 MCP 사양을 따르며 TypeScript를 사용한 stdio 전송 구현의 모범 사례를 보여줍니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.  