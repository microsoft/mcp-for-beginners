# 샘플 실행하기

> [!WARNING]
> 이 샘플은 더 이상 사용되지 않는 Sampling과 구식 HTTP+SSE 엔드포인트를 사용합니다. 이는
> MCP `2025-11-25` 호환성을 위해 유지됩니다. 새 구현에서는 LLM 공급자를 직접 호출하고
> 원격 MCP 트래픽에 Streamable HTTP를 사용해야 합니다.

## 가상 환경 생성하기

```sh
python -m venv venv
source ./venv/bin/activate
```

## 의존성 설치하기

```sh
pip install "mcp[cli]"
```

## 서버 실행하기

```sh
uvicorn server:app --port 8000
```

## GitHub Copilot 및 VS Code로 서버 테스트하기

다음과 같이 mcp.json에 항목을 추가하세요:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

서버에서 "start"를 클릭했는지 확인하세요.

GitHub Copilot에 다음 프롬프트를 붙여넣으세요:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

처음에는 Sampling 작업을 수락할지 묻고, 그 다음에는 "create_blog"를 실행할 도구 수락을 요청받게 됩니다. 다음과 비슷한 응답을 볼 수 있습니다:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->