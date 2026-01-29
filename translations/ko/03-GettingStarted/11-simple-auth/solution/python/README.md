# 샘플 실행

## 환경 생성

```sh
python -m venv venv
source ./venv/bin/activate
```

## 의존성 설치

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## 토큰 생성

클라이언트가 서버와 통신하기 위해 사용할 토큰을 생성해야 합니다.

다음 호출을 실행하세요:

```sh
python util.py
```

## 코드 실행

코드를 실행하려면 다음을 입력하세요:

```sh
python server.py
```

별도의 터미널에서 다음을 입력하세요:

```sh
python client.py
```

서버 터미널에서는 다음과 같은 메시지가 표시될 것입니다:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

클라이언트 창에서는 다음과 유사한 텍스트가 표시될 것입니다:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

이 메시지가 표시되면 모든 것이 정상적으로 작동하는 것입니다.

### 정보를 변경하여 실패를 확인하기

*server.py* 파일에서 다음 코드를 찾으세요:

```python
 if not has_scope(has_header, "Admin.Write"):
```

이를 "User.Write"로 변경하세요. 현재 토큰은 해당 권한 수준을 가지고 있지 않으므로 서버를 다시 시작하고 클라이언트를 다시 실행하려고 하면 서버 터미널에서 다음과 유사한 오류 메시지가 표시될 것입니다:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

서버 코드를 원래대로 되돌리거나 추가 범위를 포함하는 새 토큰을 생성할 수 있습니다. 선택은 여러분에게 달려 있습니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.