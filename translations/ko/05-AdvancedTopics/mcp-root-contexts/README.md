# MCP 루트 (레거시 기능)

> [!WARNING]
> 루트는 MCP `2026-07-28`부터 더 이상 사용되지 않습니다. 호환성을 위해 이 개정판에 남아 있으며 2027년 7월 28일 이후에 공개되는 첫 번째 사양 개정에서 제거될 수 있습니다.
> 새로운 구현에서는 도구 매개변수, 리소스 URI 또는 서버 구성으로 디렉터리나 파일을 전달해야 합니다.




## 개요

루트는 MCP 클라이언트가 현재 요청과 관련된 파일 시스템 위치를 서버에 알릴 수 있게 합니다. 루트는 필수 `file://` URI와 선택적 사람이 읽을 수 있는 이름을 포함합니다.







## 학습 목표

이 수업이 끝나면 다음을 할 수 있습니다:

- MCP 루트가 무엇을 나타내고 나타내지 않는지 설명할 수 있습니다.
- 현재의 `roots/list` 다중 왕복 흐름을 인식할 수 있습니다.
- 루트와 별개로 보안 제어를 적용할 수 있습니다.
- 새 구현을 지원되는 대체 방법으로 이전할 수 있습니다.

## 루트 데이터

클라이언트는 선택적 표시 이름과 함께 각 루트를 `file://` URI로 반환합니다:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

클라이언트는 사용자 승인된 위치만 노출해야 합니다. 서버는 결과를 권한 증명이 아닌 관련 파일에 대한 안내로 취급해야 합니다.


## MCP 2026-07-28 흐름

루트를 지원하는 클라이언트는 모든 요청에 기능을 선언합니다:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

클라이언트 요청을 처리하는 동안 서버는 `roots/list` 입력 요청이 포함된 `InputRequiredResult`를 반환할 수 있습니다:


클라이언트는 승인된 루트를 수집하고 원래 요청을 일치하는 `inputResponses`와 변경되지 않은 `requestState`와 함께 재시도합니다. 이 다중 왕복 패턴은 프로토콜을 무상태로 유지하며, `initialize` 핸드셰이크나 프로토콜 수준 세션이 없습니다.





## 레거시 2025-11-25 동작

MCP `2025-11-25`에서 클라이언트는 초기화 시 루트를 광고했습니다. 서버는 직접 `roots/list` 요청을 할 수 있었고, 클라이언트는 루트가 변경될 때 `notifications/roots/list_changed`를 보낼 수 있었습니다.






## 권장 대체 방법

### 도구 매개변수

필수 디렉터리나 파일을 도구 스키마에 명시하세요:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### 리소스 URI

서버가 관련 파일을 안정적인 URI를 통해 노출할 수 있을 때 MCP 리소스를 사용하세요. 이는 검색과 검색을 명시적으로 유지합니다.


### 서버 구성

고정 배포의 경우, 서버 시작 시 허용된 디렉터리를 구성하세요. 이는 도구 호출 중에 검색하는 것보다 명확한 경우가 많습니다.


## 보안 요구사항

어떤 대체 방법을 선택하든:

- 파일 시스템 위치 노출 전 사용자 동의를 받으세요.
- 경로 이동을 방지하도록 경로를 정규화하고 검증하세요.
- 권한 부여와 샌드박싱을 루트 값과 별개로 강제하세요.
- 파일에 접근할 때 권한을 재확인하세요, 단지 나열할 때만이 아니라.
- 로그나 오류 메시지에 민감한 경로를 반환하지 않도록 하세요.

## 주요 내용 요약

- 루트는 관련 파일 시스템 위치를 설명하며 대화 상태를 저장하지 않습니다.

- 루트는 안내이지 접근 제어 경계가 아닙니다.
- MCP `2026-07-28`은 요청마다 기능을 포함하고 `roots/list`에 `InputRequiredResult`를 사용합니다.

- 새로운 구현은 도구 매개변수, 리소스 URI, 또는 서버 구성을 사용해야 합니다.


## 추가 자료

- [MCP 2026-07-28의 루트](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [더 이상 지원하지 않는 기능 등록](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [MCP 변경 사항: 2026-07-28 사양](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->