# MCP 보안 모범 사례 - 2026년 9월 업데이트

이 포괄적인 가이드는 **MCP 사양 2026-07-28** 및 현재 산업 표준을 기반으로 모델 컨텍스트 프로토콜 (MCP) 시스템 구현을 위한 필수 보안 모범 사례를 설명합니다.
이러한 관행은 전통적인 보안 문제와 MCP 배포에 특유한 AI 관련 위협 모두를 다룹니다.




## 중요한 보안 요구 사항

### 필수 보안 제어 (MUST 요구 사항)

1. **토큰 검증**: MCP 서버는 명시적으로 MCP 서버 자체에 대해 발급된 토큰만을 수락해야 하며, 그 외의 토큰은 **절대 수락하지 않아야 합니다**
2. **권한 확인**: 권한 부여를 구현하는 MCP 서버는 모든 인바운드 요청을 검증해야 하며, 인증에 세션을 사용해서는 안 됩니다  
3. **사용자 동의**: 정적 제3자 클라이언트 ID를 사용하는 MCP 프록시 서버는 권한 부여 흐름을 전달하기 전에 각 MCP 클라이언트에 대한 명시적인 동의를 얻어야 합니다
4. **상태 핸들 보안**: MCP 서버는 애플리케이션 상태 핸들 소지를 인증으로 간주하지 말아야 하며, 상태 핸들을 사용하는 모든 요청을 권한 부여해야 합니다



## 핵심 보안 실천사항

### 1. 입력 검증 및 정제
- **포괄적인 입력 검증**: 모든 입력을 검증 및 정제하여 인젝션 공격, 혼란스러운 대리인 문제, 프롬프트 인젝션 취약점을 방지합니다
- **파라미터 스키마 적용**: 모든 도구 파라미터 및 API 입력에 대해 엄격한 JSON 스키마 검증을 구현합니다
- **콘텐츠 필터링**: Microsoft Prompt Shields 및 Azure Content Safety를 사용하여 프롬프트 및 응답 내의 악성 콘텐츠를 필터링합니다
- **출력 정제**: 사용자 또는 하위 시스템에 제공하기 전에 모든 모델 출력을 검증하고 정제합니다

### 2. 인증 및 권한 부여 우수 사례  
- **외부 ID 제공자**: 사용자 지정 인증보다 신뢰된 ID 제공자(Microsoft Entra ID, OAuth 2.1 제공자)에 인증을 위임합니다
- **클라이언트 등록**: 클라이언트 ID 메타데이터 문서 또는 사전 등록을 우선 사용하며, 호환성을 위해서만 더 이상 사용되지 않는 동적 클라이언트 등록을 사용합니다
- **세밀한 권한 관리**: 최소 권한 원칙에 따라 도구별로 세분화된 권한을 구현합니다
- **토큰 수명 주기 관리**: 짧은 수명의 액세스 토큰을 사용하고 안전한 순환과 적절한 청중 검증을 수행합니다
- **다중 요소 인증**: 모든 관리 액세스 및 민감한 작업에 MFA를 요구합니다

### 3. 안전한 통신 프로토콜
- **전송 계층 보안**: 원격 HTTP MCP 통신에 대해 적절한 인증서 검증이 적용된 HTTPS를 사용합니다
	로컬 stdio 서버에는 프로세스 격리 및 환경 자격 증명을 사용합니다

- **종단 간 암호화**: 전송 중 및 저장 중의 고도로 민감한 데이터에 대해 추가 암호화 계층을 구현합니다
- **인증서 관리**: 자동 갱신 프로세스를 포함한 적절한 인증서 수명 주기 관리를 유지합니다
- **프로토콜 버전 적용**: MCP `2026-07-28` 버전을 사용하고 모든 요청에 필수 버전 메타데이터를 포함하며, 지원하지 않는 버전은 거부합니다


### 4. 고급 속도 제한 및 자원 보호
- **다계층 속도 제한**: 사용자, 자격 증명, 작업, 도구 및 자원별로 속도 제한을 구현하여 남용을 방지합니다

- **적응형 속도 제한**: 사용 패턴 및 위협 지표에 적응하는 머신러닝 기반 속도 제한을 사용합니다
- **자원 할당 관리**: 컴퓨팅 자원, 메모리 사용량, 실행 시간에 적절한 제한을 설정합니다
- **DDoS 방어**: 포괄적인 DDoS 방어 및 트래픽 분석 시스템을 배포합니다

### 5. 포괄적 로깅 및 모니터링
- **구조화된 감사 로깅**: 모든 MCP 작업, 도구 실행 및 보안 이벤트에 대해 상세하고 검색 가능한 로그를 구현합니다
- **실시간 보안 모니터링**: MCP 작업에 대해 AI 기반 이상 탐지 기능을 갖춘 SIEM 시스템을 배포합니다
- **개인정보 보호 준수 로그**: 데이터 개인정보 보호 요구사항 및 규정을 준수하며 보안 이벤트를 기록합니다
- **사고 대응 통합**: 로깅 시스템을 자동화된 사고 대응 워크플로우에 연결합니다

### 6. 강화된 안전한 저장 실천사항
- **하드웨어 보안 모듈**: 중요한 암호화 작업에 대해 HSM 기반 키 저장소(Azure Key Vault, AWS CloudHSM)를 사용합니다
- **암호화 키 관리**: 암호화 키에 대해 적절한 키 순환, 분리 및 접근 제어를 구현합니다
- **비밀 관리**: 모든 API 키, 토큰, 자격 증명을 전용 비밀 관리 시스템에 저장합니다
- **데이터 분류**: 민감도 수준에 따라 데이터를 분류하고 적절한 보호 조치를 적용합니다

### 7. 고급 토큰 관리
- **토큰 전달 방지**: 보안 제어를 우회하는 토큰 전달 패턴을 명시적으로 금지합니다
- **청중 검증**: 항상 토큰의 청중 클레임이 의도한 MCP 서버 ID와 일치하는지 검증합니다
- **클레임 기반 권한 부여**: 토큰 클레임 및 사용자 속성에 기반한 세밀한 권한 부여를 구현합니다
- **토큰 바인딩**: 토큰이 의도된 MCP 리소스를 대상으로 하는지 검증하고, 애플리케이션 상태 핸들을 서버 측에서 인증된 주체에 바인딩합니다


### 8. 안전한 애플리케이션 상태 관리

- **암호화 상태 핸들**: 요청 간 걸쳐지는 상태에 대해 불투명하고 비결정적인 핸들을 생성합니다

- **사용자별 바인딩**: 각 핸들을 서버 측에서 인증된 주체에 바인딩하며, 클라이언트가 제공하는 사용자 ID는 신뢰하지 않습니다

- **수명 주기 제어**: 핸들을 만료 및 폐기하며, 호출자가 오래된 상태에서 복구하는 방법을 정의합니다

- **요청별 권한 재확인**: 핸들이 제출될 때마다 권한을 재검토합니다; 핸들은 이름일 뿐 자격 증명이 아닙니다


### 9. AI 특화 보안 제어
- **프롬프트 인젝션 방어**: Microsoft Prompt Shields를 배포하고 스포트라이팅, 구분자, 데이터 마킹 기법을 적용합니다
- **도구 오염 방지**: 도구 메타데이터를 검증하고 동적 변경 사항을 모니터링하며 도구 무결성을 확인합니다
- **모델 출력 검증**: 모델 출력에서 데이터 유출, 유해 콘텐츠 또는 보안 정책 위반 가능성을 검사합니다
- **컨텍스트 창 보호**: 컨텍스트 창 오염 및 조작 공격을 방지하기 위한 제어를 구현합니다

### 10. 도구 실행 보안
- **실행 샌드박스**: 도구 실행을 컨테이너화된 격리된 환경에서 자원 제한과 함께 수행합니다
- **권한 분리**: 최소 권한으로 도구를 실행하고 별도의 서비스 계정을 사용합니다
- **네트워크 격리**: 도구 실행 환경에 네트워크 분할을 구현합니다
- **실행 모니터링**: 도구 실행 중 이상 행위, 자원 사용 및 보안 위반을 모니터링합니다

### 11. 지속적인 보안 검증
- **자동화된 보안 테스트**: GitHub Advanced Security와 같은 도구를 사용해 CI/CD 파이프라인에 보안 테스트를 통합합니다
- **취약점 관리**: AI 모델 및 외부 서비스를 포함한 모든 종속성에 대해 정기적으로 검사합니다
- **침투 테스트**: MCP 구현을 목표로 정기적인 보안 평가를 수행합니다
- **보안 코드 리뷰**: MCP 관련 모든 코드 변경에 대해 필수 보안 리뷰를 시행합니다

### 12. AI 공급망 보안
- **구성요소 검증**: 모든 AI 구성요소(모델, 임베딩, API)의 출처, 무결성 및 보안을 검증합니다
- **종속성 관리**: 취약점 추적과 함께 모든 소프트웨어 및 AI 종속성의 최신 목록을 유지합니다
- **신뢰할 수 있는 저장소**: 모든 AI 모델, 라이브러리 및 도구에 대해 검증된 신뢰할 수 있는 출처를 사용합니다
- **공급망 모니터링**: AI 서비스 제공자 및 모델 저장소의 침해 여부를 지속적으로 모니터링합니다


## 고급 보안 패턴

### MCP를 위한 제로 트러스트 아키텍처
- **절대 신뢰하지 말고 항상 검증하라**: 모든 MCP 참가자에 대해 지속적인 검증을 구현하십시오
- **마이크로 세그멘테이션**: 세분화된 네트워크 및 신원 통제로 MCP 구성요소를 격리하십시오
- **조건부 액세스**: 컨텍스트와 행동에 적응하는 위험 기반 액세스 제어를 구현하십시오
- **지속적인 위험 평가**: 현재 위협 지표를 기반으로 보안 태세를 동적으로 평가하십시오

### 개인정보 보호 AI 구현
- **데이터 최소화**: 각 MCP 작업에 필요한 최소한의 데이터만 노출하십시오
- **차등 개인정보 보호**: 민감한 데이터 처리를 위한 개인정보 보호 기술을 구현하십시오
- **동형 암호화**: 암호화된 데이터에 대한 안전한 계산을 위해 고급 암호화 기술을 사용하십시오
- **연합 학습**: 데이터 지역성과 개인 정보를 보호하는 분산 학습 접근법을 구현하십시오

### AI 시스템에 대한 사고 대응
- **AI 특화 사고 절차**: AI 및 MCP 특유 위협에 맞춘 사고 대응 절차를 마련하십시오
- **자동화된 대응**: 일반적인 AI 보안 사고에 대한 자동 격리 및 복구를 구현하십시오  
- **포렌식 역량**: AI 시스템 침해 및 데이터 유출에 대비한 포렌식 준비태세를 유지하십시오
- **복구 절차**: AI 모델 중독, 프롬프트 주입 공격, 서비스 침해에 대응하는 복구 절차를 수립하십시오

## 구현 리소스 및 표준

### 🏔️ 실습 보안 교육
- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Azure에서 MCP 서버 보안을 위한 종합 실습 워크숍
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - 참조 아키텍처 및 OWASP MCP Top 10 구현 지침

### 공식 MCP 문서
- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - 최신 MCP 프로토콜 명세
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) - 공식 보안 지침
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) - HTTP 권한 부여 패턴
- [MCP Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/) - 전송 요구사항

### Microsoft 보안 솔루션
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 고급 프롬프트 주입 방어
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 포괄적인 AI 콘텐츠 필터링
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - 엔터프라이즈 신원 및 접근 관리
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 안전한 비밀 및 자격 증명 관리
- [GitHub Advanced Security](https://github.com/security/advanced-security) - 공급망 및 코드 보안 스캐닝

### 보안 표준 및 프레임워크
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 최신 OAuth 보안 지침
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - 웹 애플리케이션 보안 위험
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI 특화 보안 위험
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - 포괄적 AI 위험 관리
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 정보 보안 경영 시스템

### 구현 가이드 및 튜토리얼
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - 엔터프라이즈 인증 패턴
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - 신원 공급자 통합
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - 토큰 관리 모범 사례
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 고급 암호화 패턴

### 고급 보안 리소스
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - 안전한 개발 관행
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI 특화 보안 테스트
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI 위협 모델링 방법론
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - 개인정보 보호 AI 기술

### 규정 준수 및 거버넌스
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AI 시스템의 개인정보 보호 준수
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 책임 있는 AI 구현
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AI 서비스 제공자를 위한 보안 통제
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 의료 AI 준수 요건

### DevSecOps 및 자동화
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 안전한 AI 개발 파이프라인
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - 지속적인 보안 검증
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - 안전한 인프라 배포
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI 워크로드 컨테이너 보안

### 모니터링 및 사고 대응  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - 포괄적인 모니터링 솔루션
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI 특화 사고 절차
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - 보안 정보 및 이벤트 관리

- [AI를 위한 위협 인텔리전스](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI 위협 인텔리전스 출처

## 🔄 지속적 개선

### 변화하는 표준에 대응하기
- **MCP 사양 업데이트**: 공식 MCP 사양 변경 사항 및 보안 권고 모니터링
- **위협 인텔리전스**: AI 보안 위협 피드 및 취약점 데이터베이스 구독  
- **커뮤니티 참여**: MCP 보안 커뮤니티 토론 및 작업 그룹 참여
- **정기 평가**: 분기별 보안 태세 평가를 수행하고 이에 따라 관행 업데이트

### MCP 보안 기여
- **보안 연구**: MCP 보안 연구 및 취약점 공개 프로그램에 기여
- **최고 관행 공유**: 보안 구현과 교훈을 커뮤니티와 공유
- **표준 개발**: MCP 사양 개발 및 보안 표준 제정 참여
- **도구 개발**: MCP 생태계용 보안 도구 및 라이브러리 개발 및 공유

---

*이 문서는 2026년 9월 9일 기준 MCP 보안 모범 사례를 반영하며,
MCP 사양 `2026-07-28`를 기반으로 합니다. 프로토콜과 위협 환경이 진화함에 따라 보안 관행을 정기적으로
검토해야 합니다.*

## 다음 단계

- 읽기: [MCP 보안 모범 사례](./mcp-security-best-practices.md)
- 돌아가기: [보안 모듈 개요](./README.md)
- 계속하기: [모듈 3: 시작하기](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->