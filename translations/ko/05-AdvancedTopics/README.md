# MCP의 고급 주제

[![고급 MCP: 안전하고 확장 가능하며 다중 모달 AI 에이전트](../../../translated_images/ko/06.42259eaf91fccfc6d06ef1c126c9db04bbff9e5f60a87b782a2ec2616163142f.png)](https://youtu.be/4yjmGvJzYdY)

_(위 이미지를 클릭하면 이 강의의 동영상을 볼 수 있습니다)_

이 장에서는 모델 컨텍스트 프로토콜(MCP) 구현의 고급 주제인 다중 모달 통합, 확장성, 보안 모범 사례, 그리고 엔터프라이즈 통합에 대해 다룹니다. 이러한 주제는 현대 AI 시스템의 요구를 충족할 수 있는 견고하고 실무에 적합한 MCP 애플리케이션을 구축하는 데 필수적입니다.

## 개요

이 강의에서는 모델 컨텍스트 프로토콜 구현의 고급 개념을 탐구하며, 다중 모달 통합, 확장성, 보안 모범 사례, 엔터프라이즈 통합에 중점을 둡니다. 이러한 주제는 복잡한 요구 사항을 처리할 수 있는 실무용 MCP 애플리케이션을 구축하는 데 필수적입니다.

## 학습 목표

이 강의를 마치면 다음을 수행할 수 있습니다:

- MCP 프레임워크 내에서 다중 모달 기능 구현
- 고수요 시나리오를 위한 확장 가능한 MCP 아키텍처 설계
- MCP의 보안 원칙에 맞춘 보안 모범 사례 적용
- MCP를 엔터프라이즈 AI 시스템 및 프레임워크와 통합
- 실무 환경에서 성능과 신뢰성을 최적화

## 강의 및 샘플 프로젝트

| 링크 | 제목 | 설명 |
|------|-------|-------------|
| [5.1 Azure와의 통합](./mcp-integration/README.md) | Azure와 통합 | Azure에서 MCP 서버를 통합하는 방법을 배웁니다 |
| [5.2 다중 모달 샘플](./mcp-multi-modality/README.md) | MCP 다중 모달 샘플 | 오디오, 이미지 및 다중 모달 응답 샘플 |
| [5.3 MCP OAuth2 샘플](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 데모 | OAuth2를 MCP와 함께 사용하는 최소한의 Spring Boot 앱. 인증 및 리소스 서버로서의 역할, 안전한 토큰 발급, 보호된 엔드포인트, Azure Container Apps 배포, API 관리 통합을 보여줍니다. |
| [5.4 루트 컨텍스트](./mcp-root-contexts/README.md) | 루트 컨텍스트 | 루트 컨텍스트에 대해 배우고 이를 구현하는 방법을 학습합니다 |
| [5.5 라우팅](./mcp-routing/README.md) | 라우팅 | 다양한 유형의 라우팅을 학습합니다 |
| [5.6 샘플링](./mcp-sampling/README.md) | 샘플링 | 샘플링 작업 방법을 학습합니다 |
| [5.7 확장성](./mcp-scaling/README.md) | 확장성 | 확장성에 대해 학습합니다 |
| [5.8 보안](./mcp-security/README.md) | 보안 | MCP 서버를 안전하게 보호합니다 |
| [5.9 웹 검색 샘플](./web-search-mcp/README.md) | 웹 검색 MCP | SerpAPI와 통합된 Python MCP 서버 및 클라이언트로, 실시간 웹, 뉴스, 제품 검색 및 Q&A를 제공합니다. 다중 도구 오케스트레이션, 외부 API 통합, 강력한 오류 처리를 보여줍니다. |
| [5.10 실시간 스트리밍](./mcp-realtimestreaming/README.md) | 스트리밍 | 실시간 데이터 스트리밍은 오늘날 데이터 중심 세계에서 즉각적인 정보 접근이 필요한 비즈니스와 애플리케이션에 필수적입니다. |
| [5.11 실시간 웹 검색](./mcp-realtimesearch/README.md) | 웹 검색 | MCP가 실시간 웹 검색을 어떻게 혁신적으로 변화시키는지, AI 모델, 검색 엔진, 애플리케이션 간의 표준화된 컨텍스트 관리 접근 방식을 제공합니다. |
| [5.12 모델 컨텍스트 프로토콜 서버를 위한 Entra ID 인증](./mcp-security-entra/README.md) | Entra ID 인증 | Microsoft Entra ID는 강력한 클라우드 기반 ID 및 액세스 관리 솔루션을 제공하여, MCP 서버와 상호작용할 수 있는 사용자와 애플리케이션을 인증합니다. |
| [5.13 Azure AI Foundry 에이전트 통합](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry 통합 | 모델 컨텍스트 프로토콜 서버를 Azure AI Foundry 에이전트와 통합하여 강력한 도구 오케스트레이션 및 엔터프라이즈 AI 기능을 표준화된 외부 데이터 소스 연결과 함께 제공합니다. |
| [5.14 컨텍스트 엔지니어링](./mcp-contextengineering/README.md) | 컨텍스트 엔지니어링 | MCP 서버를 위한 컨텍스트 최적화, 동적 컨텍스트 관리, 효과적인 프롬프트 엔지니어링 전략을 포함한 컨텍스트 엔지니어링 기술의 미래 기회를 탐구합니다. |

## 추가 참고 자료

최신 MCP 고급 주제에 대한 정보는 다음을 참조하세요:
- [MCP 문서](https://modelcontextprotocol.io/)
- [MCP 사양](https://spec.modelcontextprotocol.io/)
- [GitHub 저장소](https://github.com/modelcontextprotocol)

## 주요 요점

- 다중 모달 MCP 구현은 텍스트 처리 이상의 AI 기능을 확장합니다
- 확장성은 엔터프라이즈 배포에 필수적이며, 수평 및 수직 확장을 통해 해결할 수 있습니다
- 포괄적인 보안 조치는 데이터를 보호하고 적절한 액세스 제어를 보장합니다
- Azure OpenAI 및 Microsoft AI Foundry와 같은 플랫폼과의 엔터프라이즈 통합은 MCP 기능을 강화합니다
- 고급 MCP 구현은 최적화된 아키텍처와 신중한 리소스 관리의 이점을 누릴 수 있습니다

## 연습 문제

특정 사용 사례에 대한 엔터프라이즈급 MCP 구현을 설계하세요:

1. 사용 사례에 필요한 다중 모달 요구 사항을 식별합니다
2. 민감한 데이터를 보호하기 위한 보안 제어를 개략적으로 작성합니다
3. 다양한 부하를 처리할 수 있는 확장 가능한 아키텍처를 설계합니다
4. 엔터프라이즈 AI 시스템과의 통합 지점을 계획합니다
5. 잠재적인 성능 병목 현상과 완화 전략을 문서화합니다

## 추가 자료

- [Azure OpenAI 문서](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Microsoft AI Foundry 문서](https://learn.microsoft.com/en-us/ai-services/)

---

## 다음 단계

- [5.1 MCP 통합](./mcp-integration/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.