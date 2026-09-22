# 이 샘플 실행하기

`uv` 설치를 권장하지만 필수는 아닙니다. 자세한 내용은 [설명](https://docs.astral.sh/uv/#highlights)을 참고하세요.

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
python client.py
```

아래와 유사한 출력이 보여야 합니다:

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->