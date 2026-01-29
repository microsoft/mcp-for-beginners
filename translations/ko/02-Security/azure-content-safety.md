# Azure Content Safety를 활용한 고급 MCP 보안

Azure Content Safety는 MCP 구현의 보안을 강화할 수 있는 여러 강력한 도구를 제공합니다.

## Prompt Shields

Microsoft의 AI Prompt Shields는 직접적 및 간접적인 프롬프트 인젝션 공격으로부터 강력한 보호를 제공합니다:

1. **고급 탐지**: 머신러닝을 활용해 콘텐츠에 숨겨진 악의적인 명령을 식별합니다.
2. **스포트라이팅**: 입력 텍스트를 변환하여 AI 시스템이 유효한 명령과 외부 입력을 구분할 수 있도록 돕습니다.
3. **구분자 및 데이터 마킹**: 신뢰할 수 있는 데이터와 신뢰할 수 없는 데이터의 경계를 표시합니다.
4. **Content Safety 통합**: Azure AI Content Safety와 연동하여 탈옥 시도 및 유해 콘텐츠를 탐지합니다.
5. **지속적인 업데이트**: Microsoft는 새로운 위협에 대응하기 위해 보호 메커니즘을 정기적으로 업데이트합니다.

## MCP와 함께 Azure Content Safety 구현하기

이 방법은 다층적인 보호를 제공합니다:
- 처리 전에 입력을 스캔
- 반환 전에 출력 검증
- 알려진 유해 패턴에 대한 차단 목록 사용
- Azure의 지속적으로 업데이트되는 Content Safety 모델 활용

## Azure Content Safety 리소스

MCP 서버에 Azure Content Safety를 구현하는 방법에 대해 더 알고 싶다면, 다음 공식 리소스를 참고하세요:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety 공식 문서입니다.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - 프롬프트 인젝션 공격 방지 방법을 배울 수 있습니다.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety 구현을 위한 상세 API 참조입니다.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C#을 사용한 빠른 구현 가이드입니다.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - 다양한 프로그래밍 언어용 클라이언트 라이브러리입니다.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 탈옥 시도 탐지 및 방지에 관한 구체적인 안내입니다.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - 효과적인 Content Safety 구현을 위한 모범 사례입니다.

더 심도 있는 구현 방법은 [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md)를 참고하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.