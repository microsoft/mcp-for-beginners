# 샘플 실행

이 샘플은 유효한 Authorization 헤더를 확인하는 미들웨어와 함께 MCP 서버를 시작합니다.

## 의존성 설치

```bash
pip install "mcp[cli]" 
```

## 서버 시작

```bash
python server.py
```

다른 터미널에서 클라이언트를 시작하세요.

```bash
python client.py
```

다음과 유사한 결과를 볼 수 있습니다:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

이는 전송된 자격 증명이 허용되었음을 의미합니다.

`client.py`에서 자격 증명을 "secret-token2"로 변경해 보세요. 그러면 응답의 일부로 다음 텍스트를 볼 수 있습니다:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

이는 인증되었지만 (자격 증명을 가지고 있었음) 자격 증명이 유효하지 않았음을 의미합니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.