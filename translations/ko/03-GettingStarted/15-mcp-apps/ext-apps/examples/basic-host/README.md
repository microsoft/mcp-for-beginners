# 예제: 기본 호스트

MCP 서버에 연결하고 도구 UI를 보안 샌드박스에서 렌더링하는 MCP 호스트 애플리케이션을 빌드하는 방법을 보여주는 참조 구현입니다.

이 기본 호스트는 로컬 개발 중 MCP 앱을 테스트하는 데에도 사용될 수 있습니다.

## 주요 파일

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - 도구 선택, 매개변수 입력, iframe 관리를 포함한 React UI 호스트
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - 보안 검증 및 양방향 메시지 중계가 포함된 외부 iframe 프록시
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - 핵심 로직: 서버 연결, 도구 호출, AppBridge 설정

## 시작하기

```bash
npm install
npm run start
# http://localhost:8080 을 여십시오
```

기본적으로 호스트 애플리케이션은 `http://localhost:3001/mcp`의 MCP 서버에 연결을 시도합니다. 이 동작은 `SERVERS` 환경 변수를 서버 URL의 JSON 배열로 설정하여 구성할 수 있습니다:

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## 아키텍처

이 예제는 보안 UI 격리를 위해 이중 iframe 샌드박스 패턴을 사용합니다:

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**왜 두 개의 iframe인가요?**

- 외부 iframe은 별도의 출처(포트 8081)에서 실행되어 호스트에의 직접 접근을 방지합니다.
- 내부 iframe은 `srcdoc`을 통해 HTML을 받고 sandbox 속성으로 제한됩니다.
- 메시지는 외부 iframe을 통해 흐르며, 외부 iframe이 이를 검증하고 양방향으로 중계합니다.

이 아키텍처는 도구 UI 코드가 악의적이더라도 호스트 애플리케이션의 DOM, 쿠키 또는 JavaScript 컨텍스트에 접근할 수 없도록 보장합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
본 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하였으나, 자동 번역은 오류나 부정확성이 포함될 수 있음을 알려드립니다. 원본 문서는 해당 언어의 원문을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 인력에 의한 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->