# MCP 보안: AI 시스템을 위한 포괄적 보호

[![MCP Security Best Practices](../../../translated_images/ko/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(위 이미지 클릭 시 본 강의 영상 시청)_

보안은 AI 시스템 설계의 기본이며, 그래서 우리는 이를 두 번째 섹션으로 우선시합니다. 이는 마이크로소프트의 [Secure Future Initiative](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/)의 **Secure by Design** 원칙과 일치합니다.

모델 컨텍스트 프로토콜(MCP)은 AI 기반 애플리케이션에 강력한 새 기능을 제공하는 동시에 전통적인 소프트웨어 위험을 넘어선 독특한 보안 과제를 도입합니다. MCP 시스템은 기존 보안 문제(안전한 코딩, 최소 권한, 공급망 보안)뿐 아니라 프롬프트 인젝션, 도구 오염, 세션 탈취, 혼란된 대리인 공격, 토큰 패스스루 취약점, 동적 기능 수정 등 AI 특유의 위협에도 직면합니다.

이 강의에서는 MCP 구현에서 가장 중요한 보안 위험을 다룹니다—인증, 권한 부여, 과도한 권한, 간접 프롬프트 인젝션, 세션 보안, 혼란된 대리인 문제, 토큰 관리, 공급망 취약점 등을 포함합니다. Microsoft의 Prompt Shields, Azure Content Safety, GitHub Advanced Security 같은 솔루션을 활용하여 MCP 배포를 강화하는 실질적 제어 및 모범 사례를 배우게 됩니다.

## 학습 목표

이 강의를 마치면 다음을 수행할 수 있습니다:

- **MCP 특화 위협 식별**: 프롬프트 인젝션, 도구 오염, 과도한 권한, 세션 탈취, 혼란된 대리인 문제, 토큰 패스스루 취약점, 공급망 위험 등 MCP 시스템만의 고유 보안 위험 인식
- **보안 제어 적용**: 강력한 인증, 최소 권한 접근, 안전한 토큰 관리, 세션 보안 제어, 공급망 검증 등 효과적 완화책 구현
- **Microsoft 보안 솔루션 활용**: MCP 작업 부하 보호를 위해 Microsoft Prompt Shields, Azure Content Safety, GitHub Advanced Security 이해 및 배포
- **도구 보안 검증**: 도구 메타데이터 검증 중요성 인식, 동적 변경 모니터링, 간접 프롬프트 인젝션 공격 방어
- **모범 사례 통합**: 기존 보안 기반(안전한 코딩, 서버 강화, 제로 트러스트)과 MCP 전용 제어를 결합해 포괄적 보호 구현

# MCP 보안 아키텍처 및 제어

현대 MCP 구현은 전통적인 소프트웨어 보안과 AI 특유 위협 모두를 다루는 다계층 보안 접근법이 필요합니다. 빠르게 진화하는 MCP 명세는 보안 제어를 계속 개선하여 엔터프라이즈 보안 아키텍처 및 검증된 모범 사례와 더 나은 통합을 가능하게 합니다.

[Microsoft Digital Defense Report](https://aka.ms/mddr)의 연구에 따르면 **보고된 침해 사고의 98%는 강력한 보안 위생으로 예방할 수 있습니다**. 가장 효과적인 보호 전략은 기본 보안 관행과 MCP 특화 제어를 결합하는 것으로, 검증된 기본 보안 조치가 전반적 보안 위험 감소에 가장 큰 영향을 줍니다.

## 현재 보안 환경

> **참고:** 이 장은 기존 MCP 보안 제어와
> 현행 **MCP 명세 2026-07-28** 권한 부여 지침을 결합했습니다. 항상
> 최신 [MCP 명세](https://modelcontextprotocol.io/specification/2026-07-28/),
> [MCP GitHub 저장소](https://github.com/modelcontextprotocol), 그리고
> [보안 모범 사례 문서](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)를
> 참조하여 보안 민감 코드 구현에 활용하세요.

> **권한 부여 업데이트:** MCP `2026-07-28`은 클라이언트가
> 권한 부여 응답의 `iss` 파라미터(RFC 9207)를 검증하며,
> 등록된 인증 정보를 발급 권한 서버에 바인딩하도록 요구합니다.
> 동적 클라이언트 등록 기능은 더 이상 권장되지 않으며,
> 새 구현은 클라이언트 ID 메타데이터 문서를 사용해야 합니다.
> 자세한 권한 부여 변경 사항은 [MCP 최신 변경사항: 2026-07-28 명세](../01-CoreConcepts/mcp-2026-07-28.md)를 확인하세요.

## 🏔️ MCP 보안 정상 회의 워크숍 (Sherpa)

<strong>실습 보안 교육</strong>을 위해, **MCP 보안 정상 회의 워크숍** (Sherpa)을 강력히 추천합니다 — Microsoft Azure에서 MCP 서버 보안을 위한 포괄적 가이드 탐험 과정입니다.

### 워크숍 개요

[MCP 보안 정상 회의 워크숍](https://azure-samples.github.io/sherpa/)은 검증된 "취약점 → 공격 → 수정 → 검증" 방식을 통해 실질적인 보안 교육을 제공합니다. 이 워크숍에서 여러분은:

- **직접 깨며 학습**: 의도적으로 취약한 서버를 공격해 취약점을 직접 경험
- **Azure 기본 보안 활용**: Azure Entra ID, Key Vault, API Management, AI Content Safety를 활용
- **다층 방어 전략 따르기**: 캠프별로 보안 레이어를 쌓아 나감
- **OWASP 표준 준수**: 모든 기술이 [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)와 연계됨
- **프로덕션 코드 획득**: 작동하는, 테스트된 구현 코드를 확보

### 탐험 경로

| 캠프 | 집중 내용 | 다루는 OWASP 위험 |
|------|-------|---------------------|
| **기본 캠프** | MCP 기초 및 인증 취약점 | MCP01, MCP07 |
| **캠프 1: 신원 관리** | OAuth 2.1, Azure 관리형 신원, Key Vault | MCP01, MCP02, MCP07 |
| **캠프 2: 게이트웨이** | API 관리, 프라이빗 엔드포인트, 거버넌스 | MCP02, MCP06, MCP07, MCP09 |
| **캠프 3: 입출력 보안** | 프롬프트 인젝션, PII 보호, 콘텐츠 안전 | MCP03, MCP05, MCP06, MCP10 |
| **캠프 4: 모니터링** | 로그 분석, 대시보드, 위협 탐지 | MCP04, MCP08 |
| **정상 회의** | 레드 팀 / 블루 팀 통합 테스트 | 모두 |

<strong>시작하기</strong>: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## OWASP MCP TOP 10 보안 위험

[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)는 MCP 구현에서 가장 중요한 10가지 보안 위험을 다음과 같이 소개합니다:

| 위험 | 설명 | Azure 완화책 |
|------|-------------|------------------|
| **MCP01** | 토큰 관리 부실 및 비밀 노출 | Azure Key Vault, 관리형 신원 |
| **MCP02** | 권한 범위 확장으로 인한 권한 상승 | RBAC, 조건부 접근 |
| **MCP03** | 도구 오염 | 도구 검증, 무결성 확인 |
| **MCP04** | 소프트웨어 공급망 공격 및 의존성 변조 | GitHub Advanced Security, 의존성 스캔 |
| **MCP05** | 명령어 인젝션 및 실행 | 입력 검증, 샌드박스 |
| **MCP06** | 의도 흐름 전복 | Azure AI 콘텐츠 안전, Prompt Shields |

| **MCP07** | 인증 및 권한 부여 불충분 | Azure Entra ID, PKCE가 포함된 OAuth 2.1 |
| **MCP08** | 감사 및 원격 측정 부족 | Azure Monitor, Application Insights |
| **MCP09** | 섀도우 MCP 서버 | API 센터 거버넌스, 네트워크 격리 |
| **MCP10** | 컨텍스트 주입 및 과다 공유 | 데이터 분류, 최소 노출 |

### MCP 인증의 진화

MCP 명세는 인증 및 권한 부여 접근 방식에서 크게 진화했습니다:

- **초기 접근 방식**: 초기 명세는 개발자가 사용자 인증을 직접 관리하는 OAuth 2.0 인증 서버 역할을 하는 MCP 서버와 맞춤형 인증 서버를 구현하도록 요구했습니다
- **현재 표준 (`2026-07-28`)**: MCP 서버는 인증을 다음과 같이 위임할 수 있습니다
  Microsoft Entra ID와 같은 외부 ID 공급자에게. 클라이언트도
  현재 발행자 검증 및 자격 증명 바인딩 요구 사항을 적용해야 합니다.
- **전송 계층 보안**: 로컬(STDIO) 및 원격(스트리밍 가능한 HTTP) 연결 모두에 적합한 인증 패턴을 갖춘 보안 전송 메커니즘 지원 강화

## 인증 및 권한 부여 보안

### 현재 보안 문제

현대 MCP 구현은 여러 인증 및 권한 부여 문제에 직면해 있습니다:

### 위험 및 위협 벡터

- **잘못 구성된 권한 부여 논리**: MCP 서버의 결함 있는 권한 부여 구현은 민감한 데이터를 노출하고 잘못된 접근 제어를 적용할 수 있습니다
- **OAuth 토큰 노출**: 로컬 MCP 서버 토큰 도난은 공격자가 서버를 가장하여 다운스트림 서비스에 접근할 수 있게 합니다
- **토큰 전달 취약점**: 부적절한 토큰 처리로 보안 제어 우회 및 책임 공백이 발생합니다
- **과도한 권한**: 과도 권한 MCP 서버는 최소 권한 원칙을 위반하고 공격 표면을 확대합니다

#### 토큰 전달: 중대한 반패턴

현재 MCP 권한 부여 명세에서 <strong>토큰 전달은 명시적으로 금지</strong>되어 있습니다. 이는 심각한 보안 영향 때문입니다:

##### 보안 제어 우회
- MCP 서버 및 다운스트림 API는 적절한 토큰 검증에 의존하는 핵심 보안 제어(속도 제한, 요청 검증, 트래픽 모니터링)를 구현합니다
- 클라이언트-API 직접 토큰 사용은 이러한 필수 보호체계를 우회하여 보안 구조를 약화시킵니다

##### 책임 및 감사 문제  
- MCP 서버는 상류 발급 토큰을 사용하는 클라이언트를 구분할 수 없어 감사 추적이 깨집니다
- 다운스트림 리소스 서버 로그는 실제 MCP 서버 대리자 대신 잘못된 요청 출처를 기록합니다
- 사고 조사 및 규정 준수 감사가 크게 어려워집니다

##### 데이터 유출 위험
- 검증되지 않은 토큰 클레임으로 인해 도난당한 토큰을 가진 악의적 행위자가 MCP 서버를 프록시로 사용하여 데이터 유출이 가능해집니다
- 신뢰 경계 위반은 승인되지 않은 접근 패턴을 허용하여 의도된 보안 제어를 우회합니다

##### 다중 서비스 공격 벡터
- 여러 서비스가 수용하는 손상된 토큰으로 연결된 시스템 전반에 횡적 이동이 가능합니다
- 토큰 출처를 검증할 수 없으면 서비스 간 신뢰 가정이 위반될 수 있습니다

### 보안 제어 및 완화책

**중요 보안 요구 사항:**

> <strong>필수</strong>: MCP 서버는 MCP 서버에 명시적으로 발급되지 않은 토큰을 **절대 수용해서는 안 됩니다**

#### 인증 및 권한 부여 제어

- **엄격한 권한 부여 검토**: MCP 서버 권한 부여 논리를 종합적으로 감사하여 의도된 사용자와 클라이언트만 민감 자원에 접근하도록 보장
  - **구현 가이드**: [MCP 서버용 인증 게이트웨이로서 Azure API Management](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **아이덴티티 통합**: [MCP 서버 인증용 Microsoft Entra ID 사용하기](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **보안 토큰 관리**: [Microsoft의 토큰 검증 및 수명 주기 모범 사례](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)를 구현
  - 토큰 대상 청중 클레임이 MCP 서버 ID와 일치하는지 검증
  - 적절한 토큰 순환 및 만료 정책 적용
  - 토큰 재사용 공격 및 무단 사용 방지

- **보호된 토큰 저장**: 저장 및 전송 시 모두 암호화된 보안 토큰 저장 구현
  - **모범 사례**: [보안 토큰 저장 및 암호화 가이드라인](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### 접근 제어 구현

- **최소 권한 원칙**: MCP 서버에 의도된 기능 수행에 필요한 최소 권한만 부여
  - 권한 증가 방지를 위한 정기적인 권한 검토 및 갱신
  - **Microsoft 문서**: [안전한 최소 권한 접근](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **역할 기반 접근 제어(RBAC)**: 세밀한 역할 할당 구현
  - 특정 자원과 동작에 역할을 엄격히 범위 지정
  - 공격 표면을 확대하는 광범위하거나 불필요한 권한 피하기

- **지속적 권한 모니터링**: 접근 감사 및 모니터링 지속적 구현
  - 이상 징후에 대해 권한 사용 패턴 모니터링
  - 과도하거나 사용하지 않는 권한 즉각 시정

## AI 특정 보안 위협

### 프롬프트 주입 및 도구 조작 공격

현대 MCP 구현은 전통적인 보안 조치로 완전히 대응 불가능한 정교한 AI 특정 공격 벡터에 직면해 있습니다:

#### **간접 프롬프트 주입 (교차 도메인 프롬프트 주입)**

<strong>간접 프롬프트 주입</strong>은 MCP 지원 AI 시스템에서 가장 치명적인 취약점 중 하나입니다. 공격자는 악의적 명령을 외부 콘텐츠(문서, 웹 페이지, 이메일, 데이터 소스 등)에 삽입하며 AI 시스템이 이를 정상 명령으로 처리합니다.

**공격 시나리오:**
- **문서 기반 주입**: 처리된 문서에 숨겨진 악의적 명령으로 AI가 의도치 않은 동작 수행
- **웹 콘텐츠 악용**: 스크랩 시 AI 행동을 조작하는 내장 프롬프트가 포함된 타락한 웹 페이지
- **이메일 기반 공격**: AI 보조자가 정보 유출 또는 무단 동작을 하도록 하는 이메일 내 악의적 프롬프트
- **데이터 소스 오염**: 오염된 콘텐츠를 AI 시스템에 제공하는 손상된 데이터베이스 또는 API

**실제 영향**: 이러한 공격은 데이터 유출, 프라이버시 침해, 유해 콘텐츠 생성, 사용자 상호작용 조작을 초래할 수 있습니다. 상세 분석은 [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)를 참조하십시오.

![프롬프트 주입 공격 다이어그램](../../../translated_images/ko/prompt-injection.ed9fbfde297ca877.webp)

#### **도구 중독 공격**

<strong>도구 중독</strong>은 MCP 도구를 정의하는 메타데이터를 겨냥하며, LLM이 도구 설명과 매개변수를 해석해 실행 결정을 내리는 방식을 악용합니다.

**공격 메커니즘:**
- **메타데이터 조작**: 공격자가 도구 설명, 매개변수 정의 또는 사용 예시에 악의적 명령 삽입
- **보이지 않는 명령**: AI 모델이 처리하지만 인간 사용자에게는 보이지 않는 도구 메타데이터 내 숨겨진 프롬프트
- **동적 도구 변경("러그 풀")**: 사용자가 승인한 도구가 나중에 사용자 인지 없이 악의적 동작 수행하도록 변경
- **매개변수 주입**: 모델 행동에 영향을 미치는 악의적 내용이 포함된 도구 매개변수 스키마


**호스팅 서버 위험**: 원격 MCP 서버는 도구 정의가 초기 사용자 승인 후에 업데이트될 수 있어, 이전에 안전했던 도구가 악의적으로 변할 수 있는 상황을 초래하기 때문에 높은 위험을 내포합니다. 포괄적인 분석은 [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)을 참조하세요.

![Tool Injection Attack Diagram](../../../translated_images/ko/tool-injection.3b0b4a6b24de6bef.webp)

#### **추가 AI 공격 벡터**

- **도메인 간 프롬프트 인젝션(XPIA)**: 여러 도메인의 콘텐츠를 활용하여 보안 통제를 우회하는 정교한 공격
- **동적 기능 수정**: 초기 보안 평가를 회피하는 도구 기능의 실시간 변경
- **컨텍스트 윈도우 포이즈닝**: 대규모 컨텍스트 윈도우를 조작하여 악성 지침을 숨기는 공격
- **모델 혼란 공격**: 모델 한계를 악용하여 예측 불가능하거나 안전하지 않은 동작을 유발


### AI 보안 위험 영향

**높은 영향 결과:**
- **데이터 유출**: 인가되지 않은 접근 및 민감한 기업 또는 개인 데이터 도난
- **개인정보 침해**: 개인 식별 정보(PII) 및 기밀 비즈니스 데이터 노출  
- **시스템 조작**: 중요 시스템 및 워크플로우의 의도하지 않은 수정
- **자격증명 도난**: 인증 토큰 및 서비스 자격증명의 손상
- **횡적 이동**: 침해된 AI 시스템을 이용한 광범위한 네트워크 공격의 발판 마련

### 마이크로소프트 AI 보안 솔루션

#### **AI 프롬프트 실드: 인젝션 공격에 대한 고급 방어**

마이크로소프트 <strong>AI 프롬프트 실드</strong>는 다중 보안 계층을 통해 직접 및 간접 프롬프트 인젝션 공격에 대해 포괄적인 방어 기능을 제공합니다:

##### **핵심 보호 메커니즘:**

1. **고급 탐지 및 필터링**
   - 머신러닝 알고리즘과 NLP 기술을 활용하여 외부 콘텐츠 내 악성 지침 탐지
   - 문서, 웹 페이지, 이메일 및 데이터 소스에 포함된 위협을 실시간 분석
   - 합법적 프롬프트 패턴과 악성 패턴의 맥락적 이해

2. **스포트라이팅 기술**  
   - 신뢰할 수 있는 시스템 지침과 잠재적으로 손상된 외부 입력을 구분
   - 악성 콘텐츠를 분리하면서 모델 관련성을 향상시키는 텍스트 변환 방법
   - AI 시스템이 올바른 지침 계층을 유지하며 인젝션 명령을 무시하도록 지원

3. **구분자 및 데이터 마킹 시스템**
   - 신뢰할 수 있는 시스템 메시지와 외부 입력 텍스트 간의 명시적 경계 정의
   - 신뢰/비신뢰 데이터 소스 경계를 강조하는 특수 마커
   - 명확한 구분으로 지침 혼동 및 무단 명령 실행 방지

4. **지속적인 위협 인텔리전스**
   - 마이크로소프트는 새롭게 등장하는 공격 패턴을 지속 모니터링하고 방어를 업데이트
   - 새로운 인젝션 기법 및 공격 벡터에 대한 선제적 위협 사냥 수행
   - 발전하는 위협에 대응하여 정기적인 보안 모델 업데이트 유지

5. **Azure 콘텐츠 안전 통합**
   - 종합적인 Azure AI 콘텐츠 안전 제품군 일부
   - 탈옥 시도, 유해 콘텐츠, 보안 정책 위반에 대한 추가 탐지 제공
   - AI 애플리케이션 구성 요소 전반에 걸친 통합 보안 통제

**도입 자료**: [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/ko/prompt-shield.ff5b95be76e9c78c.webp)


## 고급 MCP 보안 위협

### 세션 가로채기 취약점

<strong>세션 가로채기</strong>는 상태를 유지하는 MCP 구현에서 중요 공격 벡터로서, 무단자가 합법적인 세션 식별자를 획득하고 악용해 클라이언트를 가장하여 무단 행위를 수행할 수 있습니다.

#### **공격 시나리오 및 위험**

- **세션 가로채기 프롬프트 인젝션**: 도난당한 세션 ID로 세션 상태를 공유하는 서버에 악성 이벤트 주입, 잠재적으로 유해 동작 촉발 또는 민감 데이터 접근
- **직접 가장**: 도난된 세션 ID를 이용해 인증을 우회하여 공격자가 합법 사용자로 취급되는 직접 MCP 서버 호출
- **손상된 재개 가능 스트림**: 공격자가 요청을 조기에 종료시켜, 합법 클라이언트가 잠재적으로 악성 콘텐츠로 재개하도록 유도

#### **세션 관리 보안 통제**

**중요 요구사항:**
- **인가 검증**: 인가를 구현한 MCP 서버는 모든 수신 요청을 반드시 검증해야 하며, 인증을 위해 세션에 의존해서는 안 됨
- **보안 세션 생성**: 암호학적으로 안전한 비결정적 세션 ID를 보안 난수 생성기로 생성할 것
- **사용자별 바인딩**: `<user_id>:<session_id>` 형식 등으로 세션 ID를 사용자별 정보에 바인딩하여 교차 사용자 세션 악용 방지
- **세션 수명 주기 관리**: 적절한 만료, 회전 및 무효화 구현으로 취약성 창 제한
- **통신 보안**: 세션 ID 가로채기를 방지하기 위해 모든 통신에 HTTPS 필수

### 혼란스러운 대리 문제

<strong>혼란스러운 대리 문제</strong>는 MCP 서버가 클라이언트와 제3자 서비스 사이에서 인증 프록시 역할을 하면서, 정적 클라이언트 ID 악용을 통한 인가 우회 기회를 만드는 상황입니다.

#### **공격 메커니즘 및 위험**

- **쿠키 기반 동의 우회**: 이전 사용자 인증으로 생성된 동의 쿠키를 공격자가 악의적인 인가 요청과 조작된 리디렉션 URI를 이용해 악용
- **인가 코드 도난**: 기존 동의 쿠키로 인해 인가 서버가 동의 화면을 건너뛰고 코드를 공격자 제어 엔드포인트로 리디렉션  
- **무단 API 접근**: 도난당한 인가 코드를 통해 명시적 승인 없이 토큰 교환 및 사용자 가장

#### **완화 전략**

**필수 통제:**
- **명시적 동의 요구**: 정적 클라이언트 ID를 사용하는 MCP 프록시는 각 동적 등록 클라이언트에 대해 사용자 동의를 반드시 받아야 함
- **OAuth 2.1 보안 구현**: 인가 요청에 대해 PKCE(Proof Key for Code Exchange)를 포함한 최신 OAuth 보안 모범 사례 준수
- **엄격한 클라이언트 검증**: 악용 방지를 위해 리디렉션 URI 및 클라이언트 식별자에 대한 철저한 검증 수행

### 토큰 패스스루 취약점  

<strong>토큰 패스스루</strong>는 MCP 서버가 클라이언트 토큰을 적절한 검증 없이 수락하고 하위 API에 전달하는 명백한 안티패턴으로, MCP 인가 명세를 위반합니다.

#### **보안 영향**

- **통제 우회**: 클라이언트-API 직접 토큰 사용은 중요 속도 제한, 검증 및 모니터링 통제를 우회
- **감사 추적 손상**: 상위 발급 토큰으로 인해 클라이언트 식별 불가능, 사고 조사 기능 붕괴
- **프록시 기반 데이터 유출**: 검증되지 않은 토큰이 서버를 무단 데이터 접근 프록시로 악용 가능
- **신뢰 경계 위반**: 토큰 출처 확인 불가 시 하위 서비스 신뢰 가정 위반 가능
- **다중 서비스 공격 확장**: 여러 서비스에서 수락되는 침해된 토큰이 횡적 이동 지원

#### **필수 보안 통제**

**비협상 요구사항:**
- **토큰 검증**: MCP 서버는 명시적으로 MCP 서버용으로 발급되지 않은 토큰을 수락해서는 안 됨
- **대상 검증**: 항상 토큰 대상 클레임이 MCP 서버 ID와 일치하는지 검증
- **적절한 토큰 수명 주기**: 단기 액세스 토큰 및 안전한 회전 정책 구현


## AI 시스템을 위한 공급망 보안

공급망 보안은 전통적 소프트웨어 종속성을 넘어 AI 생태계 전체를 포함하도록 진화했습니다. 현대 MCP 구현은 시스템 무결성 손상을 초래할 수 있는 잠재적 취약점이 내포된 모든 AI 관련 구성 요소를 철저히 검증 및 모니터링해야 합니다.

### 확장된 AI 공급망 구성 요소

**전통적 소프트웨어 종속성:**
- 오픈 소스 라이브러리 및 프레임워크
- 컨테이너 이미지 및 기본 시스템  
- 개발 도구 및 빌드 파이프라인
- 인프라 구성 요소 및 서비스

**AI 특화 공급망 요소:**
- **기초 모델**: 다양한 제공자로부터 사전 훈련된 모델로 출처 검증 요구
- **임베딩 서비스**: 외부 벡터화 및 의미 검색 서비스
- **컨텍스트 제공자**: 데이터 소스, 지식 베이스 및 문서 저장소  
- **서드파티 API**: 외부 AI 서비스, ML 파이프라인, 데이터 처리 엔드포인트
- **모델 아티팩트**: 가중치, 구성, 미세 조정된 모델 변형
- **훈련 데이터 소스**: 모델 훈련 및 미세 조정에 사용된 데이터셋

### 포괄적 공급망 보안 전략

#### **구성 요소 검증 및 신뢰**
- **출처 검증**: 통합 전 모든 AI 구성 요소의 출처, 라이선스, 무결성 검증
- **보안 평가**: 모델, 데이터 소스 및 AI 서비스에 대한 취약점 스캔 및 보안 검토 수행
- **평판 분석**: AI 서비스 제공자의 보안 이력 및 관행 평가
- **준수 검증**: 모든 구성 요소가 조직의 보안 및 규제 요구사항 충족하는지 확인

#### **안전한 배포 파이프라인**  
- **자동화된 CI/CD 보안**: 자동화된 배포 파이프라인 전반에 보안 스캐닝 통합
- **아티팩트 무결성**: 배포된 모든 아티팩트(코드, 모델, 구성)에 대한 암호학적 검증 구현
- **단계별 배포**: 각 단계별 보안 검증을 포함한 점진적 배포 전략 사용
- **신뢰할 수 있는 아티팩트 저장소**: 검증된 안전한 아티팩트 레지스트리 및 저장소에서만 배포

#### **지속적인 모니터링 및 대응**
- **종속성 스캐닝**: 모든 소프트웨어 및 AI 구성 요소 종속성에 대한 지속적 취약점 모니터링
- **모델 모니터링**: 모델 동작, 성능 변동, 보안 이상 현상 연속 평가
- **서비스 상태 추적**: 외부 AI 서비스의 가용성, 보안 사고, 정책 변경 모니터링
- **위협 인텔리전스 통합**: AI 및 ML 보안 위험에 특화된 위협 피드 통합

#### **접근 통제 및 최소 권한**
- **구성 요소별 권한**: 비즈니스 필요성에 따라 모델, 데이터, 서비스 접근 제한
- **서비스 계정 관리**: 최소 권한이 부여된 전용 서비스 계정 구현
- **네트워크 분할**: AI 구성 요소를 격리하고 서비스 간 네트워크 접근 제한
- **API 게이트웨이 통제**: 중앙 집중식 API 게이트웨이로 외부 AI 서비스 접근 통제 및 모니터링

#### **사고 대응 및 복구**
- **신속 대응 절차**: 침해된 AI 구성 요소 패치 또는 교체를 위한 확립된 프로세스
- **자격증명 회전**: 비밀, API 키, 서비스 자격증명의 자동 회전 시스템
- **롤백 기능**: 이전의 알려진 정상 버전으로 신속 복구 가능
- **공급망 침해 복구**: 상위 AI 서비스 침해에 대응하기 위한 구체적 절차

### 마이크로소프트 보안 도구 및 통합

<strong>GitHub 고급 보안</strong>은 다음을 포함한 포괄적인 공급망 보호 기능을 제공합니다:
- **비밀 스캔**: 저장소 내 자격증명, API 키, 토큰 자동 탐지
- **종속성 스캔**: 오픈 소스 종속성 및 라이브러리에 대한 취약점 평가
- **CodeQL 분석**: 보안 취약점 및 코딩 문제에 대한 정적 코드 분석
- **공급망 인사이트**: 종속성 상태 및 보안 현황 가시성 제공

**Azure DevOps 및 Azure Repos 통합:**
- Microsoft 개발 플랫폼 전반에 걸친 원활한 보안 스캔 통합
- AI 워크로드에 대한 Azure 파이프라인의 자동 보안 검사
- 안전한 AI 구성 요소 배포를 위한 정책 시행

**마이크로소프트 내부 관행:**
마이크로소프트는 모든 제품에 걸쳐 광범위한 공급망 보안 관행을 구현합니다. [Microsoft에서 소프트웨어 공급망 보안을 향한 여정](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)에서 입증된 접근법을 확인하세요.


## 기본 보안 모범 사례

MCP 구현은 조직의 기존 보안 태세를 계승하고 강화합니다. 기본 보안 관행을 강화하면 AI 시스템 및 MCP 배포의 전반적인 보안이 크게 향상됩니다.

### 핵심 보안 기본 요소

#### **안전한 개발 관행**
- **OWASP 준수**: [OWASP Top 10](https://owasp.org/www-project-top-ten/) 웹 애플리케이션 취약점 방어
- **AI 특화 보호**: [LLM용 OWASP Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559)에 대한 제어 구현
- **안전한 비밀 관리**: 토큰, API 키 및 민감 구성 데이터 전용 금고 사용
- **종단 간 암호화**: 모든 애플리케이션 구성 요소 및 데이터 흐름에 대한 안전한 통신 구현
- **입력 검증**: 모든 사용자 입력, API 매개변수 및 데이터 소스에 대한 엄격한 검증

#### **인프라 강화**
- **다중 요소 인증**: 모든 관리자 및 서비스 계정에 대해 MFA 필수
- **패치 관리**: 운영체제, 프레임워크, 종속성에 대한 자동화된 적시 패치 적용  
- **ID 공급자 통합**: 엔터프라이즈 ID 공급자(Microsoft Entra ID, Active Directory)를 통한 중앙 집중식 ID 관리
- **네트워크 분할**: 횡적 이동 가능성을 줄이기 위해 MCP 구성 요소 논리적 격리
- **최소 권한 원칙**: 모든 시스템 구성 요소 및 계정에 대해 최소 필요 권한 부여

#### **보안 모니터링 및 탐지**
- **포괄적 로깅**: MCP 클라이언트-서버 상호작용을 포함한 AI 애플리케이션 활동 상세 기록
- **SIEM 통합**: 이상 탐지를 위한 중앙 집중식 보안 정보 및 이벤트 관리
- **행동 분석**: 시스템 및 사용자 행동의 비정상 패턴 탐지를 위한 AI 기반 모니터링
- **위협 인텔리전스**: 외부 위협 피드 및 침해 지표(IOC) 통합
- **사고 대응**: 보안 사고 탐지, 대응 및 복구를 위한 명확한 절차

#### **제로 트러스트 아키텍처**
- **절대 신뢰하지 말고, 항상 검증할 것**: 사용자, 장치, 네트워크 연결에 대한 지속적 검증
- **마이크로 세분화**: 개별 워크로드 및 서비스를 격리하는 세분화된 네트워크 통제
- **ID 중심 보안**: 네트워크 위치보다 검증된 신원을 기반으로 한 보안 정책
- **지속적인 위험 평가**: 현재 상황 및 행동을 기반으로 한 동적 보안 태세 평가
- **조건부 접근**: 위험 요소, 위치, 장치 신뢰도를 기반으로 적응하는 접근 통제

### 엔터프라이즈 통합 패턴

#### **마이크로소프트 보안 생태계 통합**
- **Microsoft Defender for Cloud**: 포괄적 클라우드 보안 태세 관리
- **Azure Sentinel**: AI 워크로드 보호를 위한 클라우드 네이티브 SIEM 및 SOAR 기능
- **Microsoft Entra ID**: 조건부 접근 정책을 포함한 엔터프라이즈 ID 및 접근 관리
- **Azure Key Vault**: 하드웨어 보안 모듈(HSM) 지원 중앙 집중식 비밀 관리
- **Microsoft Purview**: AI 데이터 소스 및 워크플로우에 대한 데이터 거버넌스 및 컴플라이언스

#### **컴플라이언스 및 거버넌스**
- **규제 준수**: MCP 구현이 산업별 컴플라이언스 요구사항(GDPR, HIPAA, SOC 2) 충족하도록 보장

- **데이터 분류**: AI 시스템에서 처리되는 민감한 데이터의 적절한 분류 및 처리
- **감사 기록**: 규제 준수 및 법의학 조사를 위한 포괄적 기록 로그
- **개인정보 보호 통제**: AI 시스템 아키텍처에 개인정보 보호 설계 원칙 구현
- **변경 관리**: AI 시스템 수정에 대한 공식적인 보안 검토 절차

이러한 기본 관행들은 강력한 보안 기준을 구축하여 MCP 전용 보안 통제의 효과를 높이고 AI 기반 애플리케이션에 종합적인 보호를 제공합니다.

## 주요 보안 요점

- **계층화된 보안 접근법**: 기본 보안 관행(안전한 코딩, 최소 권한, 공급망 검증, 지속 모니터링)과 AI 전용 통제를 결합하여 완전한 보호 구현

- **AI 특화 위협 환경**: MCP 시스템은 프롬프트 인젝션, 도구 중독, 세션 하이재킹, 혼란된 대리인 문제, 토큰 패스스루 취약점, 과도한 권한 등 특수 위험에 직면하며 전문 대응책 필요

- **인증 및 권한 부여 우수성**: 외부 ID 공급자(Microsoft Entra ID)를 활용한 강력한 인증 구현, 올바른 토큰 검증 강제, 명시적 발행 토큰만 MCP 서버에서 수용

- **AI 공격 방지**: Microsoft Prompt Shields 및 Azure Content Safety를 배포하여 간접적 프롬프트 인젝션 및 도구 중독 공격 방어, 도구 메타데이터 검증 및 동적 변경 모니터링 수행

- **세션 및 전송 보안**: 암호학적으로 안전하고 비결정적인 세션 ID를 사용자 ID와 연동하여 사용, 세션 수명주기 적절 관리, 인증용 세션 사용 금지

- **OAuth 보안 모범 사례**: 동적으로 등록된 클라이언트에 대해 명시적 사용자 동의 요구, PKCE가 포함된 올바른 OAuth 2.1 구현, 엄격한 리디렉션 URI 검증으로 혼란된 대리인 공격 방지  

- **토큰 보안 원칙**: 토큰 패스스루 반패턴 회피, 토큰 대상 청구 검증, 짧은 주기의 토큰 및 안전한 회전 구현, 명확한 신뢰 경계 유지

- **포괄적 공급망 보안**: AI 생태계의 모든 구성 요소(모델, 임베딩, 컨텍스트 제공자, 외부 API)를 전통적 소프트웨어 종속성과 동일한 보안 엄격성으로 취급

- **지속적 진화**: 급변하는 MCP 사양 최신화 유지, 보안 커뮤니티 표준에 기여, 프로토콜 성숙에 따른 적응적 보안 자세 유지

- **Microsoft 보안 통합**: Microsoft의 포괄적 보안 생태계(Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID)를 활용하여 MCP 배포 보안 강화

## 종합 리소스

### **공식 MCP 보안 문서**
- [MCP 사양 (현재: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP 보안 모범 사례](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP 권한 부여 사양](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub 저장소](https://github.com/modelcontextprotocol)

### **OWASP MCP 보안 리소스**
- [OWASP MCP Azure 보안 가이드](https://microsoft.github.io/mcp-azure-security-guide/) - Azure 구현 지침을 포함한 OWASP MCP Top 10 종합 안내
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - 공식 OWASP MCP 보안 위험
- [MCP 보안 서밋 워크숍 (Sherpa)](https://azure-samples.github.io/sherpa/) - Azure에서 MCP 보안 실습 교육

### **보안 표준 및 모범 사례**
- [OAuth 2.0 보안 모범 사례 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 웹 애플리케이션 보안](https://owasp.org/www-project-top-ten/)
- [대형 언어 모델용 OWASP Top 10](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft 디지털 방어 보고서](https://aka.ms/mddr)

### **AI 보안 연구 및 분석**
- [MCP 내 프롬프트 인젝션 (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [도구 중독 공격 (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP 보안 연구 브리핑 (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Microsoft 보안 솔루션**
- [Microsoft Prompt Shields 문서](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety 서비스](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID 보안](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure 토큰 관리 모범 사례](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **구현 가이드 및 튜토리얼**
- [Azure API Management를 MCP 인증 게이트웨이로 활용](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [MCP 서버와 Microsoft Entra ID 인증](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [안전한 토큰 저장 및 암호화 (영상)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps 및 공급망 보안**
- [Azure DevOps 보안](https://azure.microsoft.com/products/devops)
- [Azure Repos 보안](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft 공급망 보안 여정](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **추가 보안 문서**

종합적인 보안 지침은 이 섹션의 전문 문서를 참조하십시오:

- **[CIMD 및 DCR 권한 부여 샘플](./samples/cimd-dcr-auth/README.md)** - 선호 Client ID 메타데이터 문서와 폐기된 동적 클라이언트 등록 대체를 비교하는 실행 가능한 TypeScript MCP `2026-07-28` 리소스 서버
- **[MCP 보안 모범 사례](./mcp-security-best-practices.md)** - MCP 구현을 위한 완전한 보안 모범 사례
- **[Azure Content Safety 구현](./azure-content-safety-implementation.md)** - Azure Content Safety 통합의 실용적 구현 예제  
- **[MCP 보안 통제](./mcp-security-controls.md)** - MCP 배포를 위한 최신 보안 통제 및 기술
- **[MCP 모범 사례 빠른 참조](./mcp-best-practices.md)** - 필수 MCP 보안 관행 빠른 참조 가이드
- **[BlueHat 2026: AI의 미래 보안: 심층 방어 패턴을 통한 MCP 보안](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Microsoft 보안 대응 센터(MSRC)의 심층 방어 패턴

### **실습 보안 교육**

- **[MCP 보안 서밋 워크숍 (Sherpa)](https://azure-samples.github.io/sherpa/)** - Base Camp에서 Summit까지 단계별로 Azure에서 MCP 서버 보안을 위한 종합 실습 워크숍
- **[OWASP MCP Azure 보안 가이드](https://microsoft.github.io/mcp-azure-security-guide/)** - 모든 OWASP MCP Top 10 위험에 대한 참고 아키텍처 및 구현 지침

---

## 다음 단계

다음: [3장: 시작하기](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->