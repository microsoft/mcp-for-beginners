# 샘플 실행

## 의존성 설치

```sh
npm install
```

## 빌드

```sh
npm run build
```

## 토큰 생성

```sh
npm run generate
```

이 작업은 *.env* 파일에 토큰을 생성합니다. 클라이언트는 이 파일에서 읽어옵니다.

## 코드 실행

서버를 시작하려면 다음을 실행하세요:

```sh
npm start
```

클라이언트를 실행하려면, 별도의 터미널에서 다음을 실행하세요:

```sh
npm run client
```

서버 터미널에서는 다음과 유사한 출력이 표시됩니다:

```text
User exists
User has required scopes
Middleware executed
```

클라이언트 터미널에서는 다음과 유사한 출력이 표시됩니다:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### 변경 사항 적용

스코프를 이해해 봅시다. *server.ts* 파일을 찾아 다음 코드를 확인하세요:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

이 코드는 전달된 토큰에 "User.Read" 스코프가 필요하다고 명시합니다. 이를 "User.Write"로 변경해 봅시다. 이제 `npm run build`를 실행하고 서버를 다시 시작하세요 (`npm start`). 이제 인증이 실패하는 것을 볼 수 있습니다. 이는 우리가 해당 스코프를 가지고 있지 않기 때문입니다 (현재는 User.Read와 Admin.Write만 있습니다):

클라이언트는 이제 다음과 같이 표시합니다:

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

그리고 서버 터미널에서는 다음과 같이 표시됩니다:

```text
User exists
```

이 지점을 넘어가지 않는 것을 확인할 수 있습니다.

"User.Write" 스코프를 추가하고 `npm run generate`를 실행한 후 클라이언트를 다시 실행하거나, 서버 코드를 원래대로 되돌리세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.