# 샘플 실행하기

`uv`를 설치하는 것을 권장하지만 필수는 아닙니다. [설명서](https://docs.astral.sh/uv/#highlights)를 참고하세요.

## -0- 가상 환경 생성

```bash
python -m venv venv
```

## -1- 가상 환경 활성화

```bash
venv\Scripts\activate
```

## -2- 의존성 설치

```bash
pip install "mcp[cli]"
```

## -3- 샘플 실행

```bash
mcp run server.py
```

## -4- 샘플 테스트

서버가 한 터미널에서 실행 중일 때, 다른 터미널을 열고 다음 명령어를 실행하세요:

```bash
mcp dev server.py
```

이 명령어는 시각적 인터페이스를 제공하는 웹 서버를 시작하며, 샘플을 테스트할 수 있습니다.

서버가 연결되면:

- 도구 목록을 확인하고 `add`를 실행하세요. 인수로 2와 4를 입력하면 결과로 6이 표시됩니다.

- 리소스와 리소스 템플릿으로 이동하여 `get_greeting`을 호출하세요. 이름을 입력하면 제공한 이름으로 인사말이 표시됩니다.

### CLI 모드에서 테스트하기

실행한 인스펙터는 실제로 Node.js 앱이며 `mcp dev`는 이를 감싸는 래퍼입니다.

다음 명령어를 실행하여 CLI 모드에서 직접 실행할 수 있습니다:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

이 명령어는 서버에서 사용 가능한 모든 도구를 나열합니다. 다음과 같은 출력이 표시될 것입니다:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

도구를 호출하려면 다음을 입력하세요:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

다음과 같은 출력이 표시될 것입니다:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> 브라우저에서 실행하는 것보다 CLI 모드에서 인스펙터를 실행하는 것이 훨씬 빠른 경우가 많습니다.
> 인스펙터에 대한 자세한 내용은 [여기](https://github.com/modelcontextprotocol/inspector)를 참고하세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.