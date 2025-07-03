<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f00aedb7b1d11b7eaacb0618d8791c65",
  "translation_date": "2025-05-29T23:07:39+00:00",
  "source_file": "02-Security/README.md",
  "language_code": "ko"
}
-->
# Security Best Practices

Model Context Protocol(MCP)를 도입하면 AI 기반 애플리케이션에 강력한 기능이 추가되지만, 전통적인 소프트웨어 위험을 넘어서는 고유한 보안 과제도 함께 발생합니다. 안전한 코딩, 최소 권한 원칙, 공급망 보안과 같은 기존 우려 사항 외에도 MCP와 AI 워크로드는 프롬프트 인젝션, 도구 오염, 동적 도구 수정과 같은 새로운 위협에 직면합니다. 이러한 위험을 제대로 관리하지 않으면 데이터 유출, 개인정보 침해, 의도치 않은 시스템 동작이 발생할 수 있습니다.

이 강의에서는 인증, 권한 부여, 과도한 권한, 간접 프롬프트 인젝션, 공급망 취약점 등 MCP와 관련된 주요 보안 위험을 살펴보고 이를 완화하기 위한 실질적인 제어 방법과 모범 사례를 제공합니다. 또한 Microsoft의 Prompt Shields, Azure Content Safety, GitHub Advanced Security와 같은 솔루션을 활용해 MCP 구현을 강화하는 방법도 배웁니다. 이러한 제어를 이해하고 적용하면 보안 침해 가능성을 크게 줄이고 AI 시스템의 안정성과 신뢰성을 확보할 수 있습니다.

# Learning Objectives

이 강의를 마치면 다음을 수행할 수 있습니다:

- Model Context Protocol(MCP)이 도입하는 고유한 보안 위험(프롬프트 인젝션, 도구 오염, 과도한 권한, 공급망 취약점 등)을 식별하고 설명할 수 있습니다.
- 강력한 인증, 최소 권한 원칙, 안전한 토큰 관리, 공급망 검증 등 MCP 보안 위험을 완화하는 효과적인 제어 방법을 설명하고 적용할 수 있습니다.
- Prompt Shields, Azure Content Safety, GitHub Advanced Security와 같은 Microsoft 솔루션을 이해하고 활용하여 MCP와 AI 워크로드를 보호할 수 있습니다.
- 도구 메타데이터 검증, 동적 변경 모니터링, 간접 프롬프트 인젝션 공격 방어의 중요성을 인식할 수 있습니다.
- 안전한 코딩, 서버 강화, 제로 트러스트 아키텍처 등 기존 보안 모범 사례를 MCP 구현에 통합하여 보안 침해 가능성과 영향을 줄일 수 있습니다.

# MCP security controls

중요 자원에 접근하는 모든 시스템은 암묵적인 보안 과제를 안고 있습니다. 이러한 보안 과제는 기본적인 보안 제어와 개념을 올바르게 적용함으로써 일반적으로 해결할 수 있습니다. MCP는 최근에 정의된 프로토콜로, 사양이 매우 빠르게 변화하고 있으며 프로토콜이 발전함에 따라 보안 제어도 점차 성숙해져 기업 환경과 기존 보안 아키텍처 및 모범 사례와 더 잘 통합될 것입니다.

[Microsoft Digital Defense Report](https://aka.ms/mddr)에 따르면 보고된 침해 사례의 98%는 강력한 보안 위생 관리로 예방할 수 있으며, 모든 유형의 침해에 대한 최선의 방어는 기본적인 보안 위생, 안전한 코딩 모범 사례, 공급망 보안을 제대로 갖추는 것입니다. 이미 알려진 검증된 방법들이 여전히 보안 위험 감소에 가장 큰 영향을 미칩니다.

MCP 도입 시 보안 위험을 다루기 시작할 수 있는 몇 가지 방법을 살펴보겠습니다.

> **Note:** 아래 내용은 **2025년 5월 29일** 기준으로 정확합니다. MCP 프로토콜은 계속 진화 중이며, 향후 구현에서는 새로운 인증 패턴과 제어가 도입될 수 있습니다. 최신 업데이트와 지침은 항상 [MCP Specification](https://spec.modelcontextprotocol.io/) 및 공식 [MCP GitHub 저장소](https://github.com/modelcontextprotocol), [보안 모범 사례 페이지](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)를 참고하세요.

### 문제 진술  
초기 MCP 사양은 개발자가 자체 인증 서버를 구축할 것으로 가정했습니다. 이는 OAuth 및 관련 보안 제약에 대한 지식이 필요했습니다. MCP 서버는 OAuth 2.0 인증 서버 역할을 하며, Microsoft Entra ID와 같은 외부 서비스에 위임하지 않고 직접 사용자 인증을 관리했습니다. 2025년 4월 26일자로 MCP 사양이 업데이트되어 MCP 서버가 사용자 인증을 외부 서비스에 위임할 수 있게 되었습니다.

### 위험
- MCP 서버의 권한 부여 로직이 잘못 구성되면 민감한 데이터 노출과 잘못된 접근 제어가 발생할 수 있습니다.
- 로컬 MCP 서버에서 OAuth 토큰이 탈취될 경우, 해당 토큰을 이용해 MCP 서버를 가장하여 토큰 대상 서비스의 리소스와 데이터에 접근할 수 있습니다.

#### Token Passthrough
토큰 패스스루는 권한 부여 사양에서 명시적으로 금지되어 있으며, 다음과 같은 여러 보안 위험을 초래합니다:

#### 보안 제어 우회
MCP 서버나 하위 API는 토큰 대상자나 기타 자격 증명 제약에 의존하는 속도 제한, 요청 검증, 트래픽 모니터링 같은 중요한 보안 제어를 구현할 수 있습니다. 클라이언트가 MCP 서버의 적절한 검증 없이 직접 하위 API에 토큰을 사용하면 이러한 제어를 우회하게 됩니다.

#### 책임 추적 및 감사 문제
클라이언트가 업스트림에서 발급된 접근 토큰으로 호출할 경우 MCP 서버는 MCP 클라이언트를 식별하거나 구분할 수 없습니다.  
하위 리소스 서버의 로그는 실제 토큰을 전달하는 MCP 서버가 아닌 다른 출처나 신원에서 온 요청으로 나타날 수 있습니다.  
이로 인해 사고 조사, 제어, 감사가 어려워집니다.  
MCP 서버가 토큰의 클레임(예: 역할, 권한, 대상자)이나 기타 메타데이터를 검증하지 않고 토큰을 전달하면, 탈취된 토큰을 가진 악의적 행위자가 MCP 서버를 데이터 유출의 프록시로 사용할 수 있습니다.

#### 신뢰 경계 문제
하위 리소스 서버는 특정 엔티티에 신뢰를 부여하며, 이 신뢰는 출처나 클라이언트 행동 패턴에 대한 가정을 포함할 수 있습니다.  
이 신뢰 경계가 깨지면 예기치 않은 문제가 발생할 수 있습니다.  
토큰이 적절한 검증 없이 여러 서비스에서 받아들여지면, 한 서비스가 침해될 경우 공격자가 토큰을 사용해 다른 연결된 서비스에 접근할 수 있습니다.

#### 미래 호환성 위험
현재 MCP 서버가 “순수 프록시” 역할을 하더라도, 나중에 보안 제어를 추가해야 할 수 있습니다.  
적절한 토큰 대상자 분리를 시작하면 보안 모델을 더 쉽게 발전시킬 수 있습니다.

### 완화 제어

**MCP 서버는 명시적으로 MCP 서버용으로 발급되지 않은 토큰을 절대 수락해서는 안 됩니다**

- **권한 부여 로직 검토 및 강화:** MCP 서버의 권한 부여 구현을 꼼꼼히 감사하여 의도된 사용자와 클라이언트만 민감 자원에 접근할 수 있도록 합니다. 실용적인 가이드는 [Azure API Management Your Auth Gateway For MCP Servers | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)와 [Using Microsoft Entra ID To Authenticate With MCP Servers Via Sessions - Den Delimarsky](https://den.dev/blog/mcp-server-auth-entra-id-session/)를 참고하세요.
- **안전한 토큰 관리 강제:** [Microsoft의 토큰 검증 및 수명 관련 모범 사례](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)를 따라 접근 토큰의 오용과 재사용, 탈취 위험을 줄이세요.
- **토큰 저장 보호:** 토큰은 항상 안전하게 저장하고 암호화하여 저장 및 전송 중 보호해야 합니다. 구현 팁은 [Use secure token storage and encrypt tokens](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)를 참고하세요.

# MCP 서버의 과도한 권한

### 문제 진술
MCP 서버가 접근하는 서비스/리소스에 과도한 권한이 부여되었을 수 있습니다. 예를 들어, 기업 데이터 저장소에 연결된 AI 영업 애플리케이션의 MCP 서버는 영업 데이터에만 접근할 수 있어야 하며, 저장소 내 모든 파일에 접근해서는 안 됩니다. 최소 권한 원칙(가장 오래된 보안 원칙 중 하나)에 따라, 어떤 리소스도 수행해야 할 작업에 필요한 권한을 초과해서는 안 됩니다. AI는 유연성을 위해 정확한 권한 범위를 정의하기 어려워 이 분야에서 도전이 더 큽니다.

### 위험  
- 과도한 권한 부여는 MCP 서버가 접근해서는 안 되는 데이터를 유출하거나 수정할 수 있게 하며, 개인정보(PII)가 포함된 경우 프라이버시 문제도 발생할 수 있습니다.

### 완화 제어
- **최소 권한 원칙 적용:** MCP 서버가 필요한 작업을 수행하는 데 최소한의 권한만 부여받도록 하며, 정기적으로 권한을 검토하고 필요 이상으로 확대되지 않도록 업데이트하세요. 자세한 지침은 [Secure least-privileged access](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)를 참고하세요.
- **역할 기반 접근 제어(RBAC) 사용:** MCP 서버에 특정 리소스와 작업에 엄격히 제한된 역할을 할당하여 광범위하거나 불필요한 권한을 피하세요.
- **권한 모니터링 및 감사:** 권한 사용 현황을 지속적으로 모니터링하고 접근 로그를 감사하여 과도하거나 미사용 권한을 신속히 발견하고 조치하세요.

# 간접 프롬프트 인젝션 공격

### 문제 진술

악의적이거나 침해된 MCP 서버는 고객 데이터 노출이나 의도치 않은 동작을 초래하는 중대한 위험을 야기할 수 있습니다. 이는 특히 AI와 MCP 기반 워크로드에서 중요하며, 다음과 같은 공격이 포함됩니다:

- **프롬프트 인젝션 공격**: 공격자가 프롬프트나 외부 콘텐츠에 악의적 명령을 삽입해 AI 시스템이 의도하지 않은 동작을 하거나 민감 데이터를 유출하게 만듭니다. 자세히 보기: [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- **도구 오염**: 공격자가 도구 메타데이터(설명이나 매개변수 등)를 조작해 AI 동작에 영향을 주고, 보안 제어를 우회하거나 데이터를 유출합니다. 자세히 보기: [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- **교차 도메인 프롬프트 인젝션**: 악성 명령이 문서, 웹페이지, 이메일 등에 삽입되어 AI가 이를 처리하면서 데이터 유출이나 조작이 발생합니다.
- **동적 도구 수정(러그 풀)**: 사용자 승인 후 도구 정의가 변경되어 사용자가 모르는 사이에 악성 동작이 추가될 수 있습니다.

이러한 취약점은 MCP 서버와 도구를 환경에 통합할 때 철저한 검증, 모니터링, 보안 제어가 필요함을 강조합니다. 자세한 내용은 위 링크를 참고하세요.

![prompt-injection-lg-2048x1034](../../../translated_images/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.ko.png)

**간접 프롬프트 인젝션**(Indirect Prompt Injection, XPIA라고도 함)은 Model Context Protocol(MCP)을 사용하는 생성 AI 시스템에서 치명적인 취약점입니다. 이 공격은 문서, 웹페이지, 이메일 등 외부 콘텐츠에 악의적 명령이 숨겨져 있습니다. AI 시스템이 이 콘텐츠를 처리할 때, 삽입된 명령을 정상 사용자 명령으로 오해해 데이터 유출, 유해 콘텐츠 생성, 사용자 상호작용 조작과 같은 의도치 않은 동작을 일으킬 수 있습니다. 자세한 설명과 실제 사례는 [Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)에서 확인하세요.

특히 위험한 형태는 **도구 오염**입니다. 공격자는 MCP 도구의 메타데이터(도구 설명, 매개변수 등)에 악의적 명령을 주입합니다. 대형 언어 모델(LLM)은 이 메타데이터를 기반으로 호출할 도구를 결정하기 때문에, 오염된 설명은 모델이 무단 도구 호출이나 보안 제어 우회를 하도록 유도할 수 있습니다. 이러한 조작은 사용자에게는 보이지 않지만 AI 시스템이 해석하고 실행할 수 있습니다. 호스팅된 MCP 서버 환경에서는 도구 정의가 사용자 승인 후에도 변경될 수 있는데, 이를 "[러그 풀](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)"이라고 합니다. 이 경우, 이전에 안전했던 도구가 나중에 몰래 데이터 유출이나 시스템 동작 변경 같은 악성 행위를 하도록 바뀔 수 있습니다. 이 공격 벡터에 관한 자세한 내용은 [Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)을 참고하세요.

![tool-injection-lg-2048x1239 (1)](../../../translated_images/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.ko.png)

## 위험
AI의 의도치 않은 동작은 데이터 유출과 개인정보 침해 등 다양한 보안 위험을 야기합니다.

### 완화 제어
### 간접 프롬프트 인젝션 공격 방어를 위한 Prompt Shields 사용
-----------------------------------------------------------------------------

**AI Prompt Shields**는 Microsoft가 개발한 솔루션으로, 직접 및 간접 프롬프트 인젝션 공격을 방어합니다. 다음과 같은 방식으로 도움을 줍니다:

1.  **탐지 및 필터링**: Prompt Shields는 고급 머신러닝 알고리즘과 자연어 처리 기술을 사용해 문서, 웹페이지, 이메일 등 외부 콘텐츠에 삽입된 악성 명령을 탐지하고 필터링합니다.
    
2.  **스포트라이팅(Spotlighting)**: 이 기법은 AI 시스템이 유효한 시스템 명령과 잠재적 불신 외부 입력을 구분할 수 있도록 돕습니다. 입력 텍스트를 모델에 더 관련성 있게 변환하여 악성 명령을 식별하고 무시할 수 있게 합니다.
    
3.  **구분자 및 데이터마킹(Delimiters and Datamarking)**: 시스템 메시지에 구분자를 포함해 입력 텍스트 위치를 명확히 지정함으로써 AI가 사용자 입력과 잠재적 유해 외부 콘텐츠를 구분하도록 돕습니다. 데이터마킹은 신뢰 데이터와 비신뢰 데이터 경계를 특수 마커로 표시하는 개념을 확장한 것입니다.
    
4.  **지속적 모니터링 및 업데이트**: Microsoft는 새로운 위협과 진화하는 공격 기법에 대응하기 위해 Prompt Shields를 지속적으로 모니터링하고 업데이트합니다.
    
5. **Azure Content Safety와 통합:** Prompt Shields는 Azure AI Content Safety 제품군의 일부로, 탈옥 시도 탐지, 유해 콘텐츠 식별 등 AI 애플리케이션 내 다양한 보안 위험을 추가로 방지합니다.

AI Prompt Shields에 대한 자세한 내용은 [Prompt Shields documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)에서 확인할 수 있습니다.

![prompt-shield-lg-2048x1328](../../../translated_images/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.ko.png)

### 공급망 보안

공급망 보안은 AI 시대에도 여전히 기본이며, 공급망의 범위가 확장되었습니다. 전통적인 코드 패키지 외에도, 기본 모델, 임베딩 서비스, 컨텍스트 제공자, 타사 API 등 모든 AI 관련 구성요소를 엄격히 검증하고 모니터링해야 합니다. 이들 각각은 적절히 관리하지 않으면 취약점이나 위험을 초래할 수 있습니다.

**AI 및 MCP를 위한 주요 공급망 보안 관행:**
- **통합 전 모든 구성요소 검증:** 오픈소스 라이브러리뿐 아니라 AI 모델, 데이터 소스, 외부 API도 출처, 라이선스, 알려진 취약점을 반드시 확인하세요.
- **안전한 배포 파이프라인 유지:** 보안 스캔이 통합된 자동 CI/CD 파이프라인을 사용해 문제를 조기에 발견하고, 신뢰된 산출물만 프로덕션에 배포하세요.
- **지속적 모니터링 및 감사:** 모델과 데이터 서비스 등 모든 의존성을 지속적으로 모니터링하고 공급망 공격이나 신규 취약점을 탐지하세요.
- **최소 권한 및 접근 제어 적용:** MCP 서버가 기능 수행에 필요한 모델, 데이터, 서비스에만 접근할 수 있도록 권한을 제한하세요.
- **위협에 신속 대응:** 침해가 확인되면 손상된 구성요소를 신속히 패치하거나 교체하고, 비밀 정보나 자격 증명도 즉시 교체하는 프로세스를 마련하세요.

[GitHub Advanced Security](https://github.com/security/advanced-security)는 비밀 스캔, 의존성 스캔, CodeQL 분석 등 기능을 제공하며, [Azure DevOps](https://azure.microsoft.com/en-us/products/devops) 및 [Azure Repos](https://azure.microsoft.com/en-us/products/devops/repos/)와 통합되어 코드와 AI 공급망 구성요소 전반의 취약점 식별과 완화를 지원합니다.

Microsoft는 모든 제품에 대해 광범위한 공급망 보안 관행을 내부적으로 적용하고 있습니다. 자세한 내용은 [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)를 참고하세요.

# MCP 구현의 보안 수준을 높이는 기존 보안 모범 사례

모든 MCP 구현은 구축된 조직 환경의 기존 보안 수준을 물려받으므로, MCP를 전체
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [GitHub Advanced Security](https://github.com/security/advanced-security)
- [Azure DevOps](https://azure.microsoft.com/products/devops)
- [Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)
- [Secure Least-Privileged Access (Microsoft)](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Best Practices for Token Validation and Lifetime](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [Use Secure Token Storage and Encrypt Tokens (YouTube)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)
- [Azure API Management as Auth Gateway for MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [MCP Security Best Practice](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [Using Microsoft Entra ID to Authenticate with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)

### 다음

다음: [3장: 시작하기](../03-GettingStarted/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.
