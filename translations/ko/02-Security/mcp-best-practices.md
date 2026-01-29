# MCP 보안 모범 사례 2025

이 종합 가이드는 최신 **MCP 사양 2025-11-25** 및 현재 업계 표준을 기반으로 Model Context Protocol (MCP) 시스템 구현을 위한 필수 보안 모범 사례를 설명합니다. 이 모범 사례는 전통적인 보안 문제와 MCP 배포에 고유한 AI 관련 위협을 모두 다룹니다.

## 중요한 보안 요구 사항

### 필수 보안 제어 (MUST 요구 사항)

1. **토큰 검증**: MCP 서버는 명시적으로 MCP 서버 자체에 발급된 토큰만을 수락해야 하며, 그렇지 않은 토큰은 **절대 수락해서는 안 됩니다**
2. **권한 확인**: 권한 부여를 구현하는 MCP 서버는 모든 수신 요청을 검증해야 하며, 인증에 세션을 사용해서는 안 됩니다  
3. **사용자 동의**: 정적 클라이언트 ID를 사용하는 MCP 프록시 서버는 각 동적 등록 클라이언트에 대해 명시적인 사용자 동의를 받아야 합니다
4. **안전한 세션 ID**: MCP 서버는 암호학적으로 안전하고 비결정적인 세션 ID를 안전한 난수 생성기로 생성해야 합니다

## 핵심 보안 관행

### 1. 입력 검증 및 정화
- **포괄적 입력 검증**: 모든 입력을 검증하고 정화하여 인젝션 공격, 혼란 대리 문제, 프롬프트 인젝션 취약점을 방지합니다
- **매개변수 스키마 적용**: 모든 도구 매개변수 및 API 입력에 대해 엄격한 JSON 스키마 검증을 구현합니다
- **콘텐츠 필터링**: Microsoft Prompt Shields 및 Azure Content Safety를 사용하여 프롬프트와 응답의 악성 콘텐츠를 필터링합니다
- **출력 정화**: 사용자 또는 하위 시스템에 제공하기 전에 모든 모델 출력을 검증하고 정화합니다

### 2. 인증 및 권한 부여 우수성  
- **외부 ID 공급자**: 맞춤형 인증 구현 대신 Microsoft Entra ID, OAuth 2.1 공급자 등 검증된 ID 공급자에 인증을 위임합니다
- **세분화된 권한**: 최소 권한 원칙에 따라 도구별 세분화된 권한을 구현합니다
- **토큰 수명 주기 관리**: 짧은 수명의 액세스 토큰을 사용하고 안전한 회전 및 적절한 대상 검증을 수행합니다
- **다중 요소 인증**: 모든 관리자 접근 및 민감한 작업에 대해 MFA를 요구합니다

### 3. 안전한 통신 프로토콜
- **전송 계층 보안**: 모든 MCP 통신에 대해 HTTPS/TLS 1.3을 사용하고 적절한 인증서 검증을 수행합니다
- **종단 간 암호화**: 전송 중 및 저장 중인 고도로 민감한 데이터에 대해 추가 암호화 계층을 구현합니다
- **인증서 관리**: 자동 갱신 프로세스를 포함한 적절한 인증서 수명 주기 관리를 유지합니다
- **프로토콜 버전 적용**: 최신 MCP 프로토콜 버전(2025-11-25)을 사용하고 적절한 버전 협상을 수행합니다

### 4. 고급 속도 제한 및 자원 보호
- **다계층 속도 제한**: 사용자, 세션, 도구, 자원 수준에서 속도 제한을 구현하여 남용을 방지합니다
- **적응형 속도 제한**: 사용 패턴 및 위협 지표에 적응하는 머신러닝 기반 속도 제한을 사용합니다
- **자원 할당 관리**: 계산 자원, 메모리 사용량, 실행 시간에 적절한 제한을 설정합니다
- **DDoS 방어**: 포괄적인 DDoS 방어 및 트래픽 분석 시스템을 배포합니다

### 5. 포괄적 로깅 및 모니터링
- **구조화된 감사 로깅**: 모든 MCP 작업, 도구 실행, 보안 이벤트에 대해 상세하고 검색 가능한 로그를 구현합니다
- **실시간 보안 모니터링**: AI 기반 이상 탐지 기능이 포함된 SIEM 시스템을 MCP 워크로드에 배포합니다
- **개인정보 보호 준수 로깅**: 데이터 개인정보 보호 요구사항 및 규정을 준수하며 보안 이벤트를 기록합니다
- **사고 대응 통합**: 로깅 시스템을 자동화된 사고 대응 워크플로우에 연결합니다

### 6. 강화된 안전한 저장 관행
- **하드웨어 보안 모듈**: 중요한 암호화 작업에 대해 HSM 기반 키 저장소(Azure Key Vault, AWS CloudHSM)를 사용합니다
- **암호화 키 관리**: 키 회전, 분리, 접근 제어를 적절히 구현합니다
- **비밀 관리**: 모든 API 키, 토큰, 자격 증명을 전용 비밀 관리 시스템에 저장합니다
- **데이터 분류**: 민감도 수준에 따라 데이터를 분류하고 적절한 보호 조치를 적용합니다

### 7. 고급 토큰 관리
- **토큰 패스스루 방지**: 보안 제어를 우회하는 토큰 패스스루 패턴을 명시적으로 금지합니다
- **대상 검증**: 토큰 대상 클레임이 의도된 MCP 서버 ID와 일치하는지 항상 검증합니다
- **클레임 기반 권한 부여**: 토큰 클레임 및 사용자 속성에 기반한 세분화된 권한 부여를 구현합니다
- **토큰 바인딩**: 적절한 경우 토큰을 특정 세션, 사용자 또는 장치에 바인딩합니다

### 8. 안전한 세션 관리
- **암호학적 세션 ID**: 예측 불가능한 암호학적으로 안전한 난수 생성기로 세션 ID를 생성합니다
- **사용자별 바인딩**: `<user_id>:<session_id>`와 같은 안전한 형식을 사용하여 세션 ID를 사용자별 정보에 바인딩합니다
- **세션 수명 주기 제어**: 적절한 세션 만료, 회전, 무효화 메커니즘을 구현합니다
- **세션 보안 헤더**: 세션 보호를 위한 적절한 HTTP 보안 헤더를 사용합니다

### 9. AI 특화 보안 제어
- **프롬프트 인젝션 방어**: Microsoft Prompt Shields를 스포트라이트, 구분자, 데이터마킹 기법과 함께 배포합니다
- **도구 중독 방지**: 도구 메타데이터를 검증하고 동적 변경을 모니터링하며 도구 무결성을 확인합니다
- **모델 출력 검증**: 데이터 유출, 유해 콘텐츠, 보안 정책 위반 가능성을 모델 출력에서 검사합니다
- **컨텍스트 윈도우 보호**: 컨텍스트 윈도우 중독 및 조작 공격을 방지하는 제어를 구현합니다

### 10. 도구 실행 보안
- **실행 샌드박싱**: 도구 실행을 컨테이너화된 격리 환경에서 자원 제한과 함께 수행합니다
- **권한 분리**: 최소 권한으로 도구를 실행하고 서비스 계정을 분리합니다
- **네트워크 격리**: 도구 실행 환경에 네트워크 분할을 구현합니다
- **실행 모니터링**: 도구 실행 중 이상 행동, 자원 사용, 보안 위반을 모니터링합니다

### 11. 지속적인 보안 검증
- **자동화된 보안 테스트**: GitHub Advanced Security와 같은 도구를 사용하여 CI/CD 파이프라인에 보안 테스트를 통합합니다
- **취약점 관리**: AI 모델 및 외부 서비스를 포함한 모든 종속성을 정기적으로 스캔합니다
- **침투 테스트**: MCP 구현을 대상으로 정기적인 보안 평가를 수행합니다
- **보안 코드 리뷰**: 모든 MCP 관련 코드 변경에 대해 필수 보안 검토를 수행합니다

### 12. AI 공급망 보안
- **구성 요소 검증**: 모든 AI 구성 요소(모델, 임베딩, API)의 출처, 무결성, 보안을 검증합니다
- **종속성 관리**: 취약점 추적과 함께 모든 소프트웨어 및 AI 종속성의 최신 목록을 유지합니다
- **신뢰할 수 있는 저장소**: 모든 AI 모델, 라이브러리, 도구에 대해 검증된 신뢰할 수 있는 소스를 사용합니다
- **공급망 모니터링**: AI 서비스 제공자 및 모델 저장소의 침해 여부를 지속적으로 모니터링합니다

## 고급 보안 패턴

### MCP를 위한 제로 트러스트 아키텍처
- **절대 신뢰하지 말고 항상 검증하라**: 모든 MCP 참여자에 대해 지속적인 검증을 구현합니다
- **마이크로 세분화**: 세분화된 네트워크 및 ID 제어로 MCP 구성 요소를 격리합니다
- **조건부 접근**: 상황과 행동에 적응하는 위험 기반 접근 제어를 구현합니다
- **지속적 위험 평가**: 현재 위협 지표를 기반으로 보안 태세를 동적으로 평가합니다

### 개인정보 보호 AI 구현
- **데이터 최소화**: 각 MCP 작업에 필요한 최소한의 데이터만 노출합니다
- **차등 개인정보 보호**: 민감한 데이터 처리에 개인정보 보호 기법을 구현합니다
- **동형 암호화**: 암호화된 데이터에 대한 안전한 계산을 위한 고급 암호화 기법을 사용합니다
- **연합 학습**: 데이터 지역성과 개인정보를 보존하는 분산 학습 방식을 구현합니다

### AI 시스템을 위한 사고 대응
- **AI 특화 사고 절차**: AI 및 MCP 특화 위협에 맞춘 사고 대응 절차를 개발합니다
- **자동화된 대응**: 일반적인 AI 보안 사고에 대해 자동 격리 및 복구를 구현합니다  
- **포렌식 역량**: AI 시스템 침해 및 데이터 유출에 대비한 포렌식 준비 태세를 유지합니다
- **복구 절차**: AI 모델 중독, 프롬프트 인젝션 공격, 서비스 침해로부터 복구하는 절차를 수립합니다

## 구현 리소스 및 표준

### 공식 MCP 문서
- [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) - 최신 MCP 프로토콜 사양
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) - 공식 보안 가이드
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) - 인증 및 권한 부여 패턴
- [MCP Transport Security](https://modelcontextprotocol.io/specification/2025-11-25/transports/) - 전송 계층 보안 요구 사항

### Microsoft 보안 솔루션
- [Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 고급 프롬프트 인젝션 방어
- [Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - 포괄적 AI 콘텐츠 필터링
- [Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/v2-oauth2-auth-code-flow) - 엔터프라이즈 ID 및 접근 관리
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/basic-concepts) - 안전한 비밀 및 자격 증명 관리
- [GitHub Advanced Security](https://github.com/security/advanced-security) - 공급망 및 코드 보안 스캔

### 보안 표준 및 프레임워크
- [OAuth 2.1 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) - 최신 OAuth 보안 지침
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - 웹 애플리케이션 보안 위험
- [OWASP Top 10 for LLMs](https://genai.owasp.org/download/43299/?tmstv=1731900559) - AI 특화 보안 위험
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - 포괄적 AI 위험 관리
- [ISO 27001:2022](https://www.iso.org/standard/27001) - 정보 보안 관리 시스템

### 구현 가이드 및 튜토리얼
- [Azure API Management as MCP Auth Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690) - 엔터프라이즈 인증 패턴
- [Microsoft Entra ID with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/) - ID 공급자 통합
- [Secure Token Storage Implementation](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2) - 토큰 관리 모범 사례
- [End-to-End Encryption for AI](https://learn.microsoft.com/azure/architecture/example-scenario/confidential/end-to-end-encryption) - 고급 암호화 패턴

### 고급 보안 리소스
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/sdl) - 안전한 개발 관행
- [AI Red Team Guidance](https://learn.microsoft.com/security/ai-red-team/) - AI 특화 보안 테스트
- [Threat Modeling for AI Systems](https://learn.microsoft.com/security/adoption/approach/threats-ai) - AI 위협 모델링 방법론
- [Privacy Engineering for AI](https://www.microsoft.com/security/blog/2021/07/13/microsofts-pet-project-privacy-enhancing-technologies-in-action/) - 개인정보 보호 AI 기법

### 컴플라이언스 및 거버넌스
- [GDPR Compliance for AI](https://learn.microsoft.com/compliance/regulatory/gdpr-data-protection-impact-assessments) - AI 시스템 개인정보 보호 준수
- [AI Governance Framework](https://learn.microsoft.com/azure/architecture/guide/responsible-ai/responsible-ai-overview) - 책임 있는 AI 구현
- [SOC 2 for AI Services](https://learn.microsoft.com/compliance/regulatory/offering-soc) - AI 서비스 제공자 보안 제어
- [HIPAA Compliance for AI](https://learn.microsoft.com/compliance/regulatory/offering-hipaa-hitech) - 의료 AI 준수 요구 사항

### DevSecOps 및 자동화
- [DevSecOps Pipeline for AI](https://learn.microsoft.com/azure/devops/migrate/security-validation-cicd-pipeline) - 안전한 AI 개발 파이프라인
- [Automated Security Testing](https://learn.microsoft.com/security/engineering/devsecops) - 지속적 보안 검증
- [Infrastructure as Code Security](https://learn.microsoft.com/security/engineering/infrastructure-security) - 안전한 인프라 배포
- [Container Security for AI](https://learn.microsoft.com/azure/container-instances/container-instances-image-security) - AI 워크로드 컨테이너 보안

### 모니터링 및 사고 대응  
- [Azure Monitor for AI Workloads](https://learn.microsoft.com/azure/azure-monitor/overview) - 포괄적 모니터링 솔루션
- [AI Security Incident Response](https://learn.microsoft.com/security/compass/incident-response-playbooks) - AI 특화 사고 대응 절차
- [SIEM for AI Systems](https://learn.microsoft.com/azure/sentinel/overview) - 보안 정보 및 이벤트 관리
- [Threat Intelligence for AI](https://learn.microsoft.com/security/compass/security-operations-videos-and-decks#threat-intelligence) - AI 위협 인텔리전스 소스

## 🔄 지속적 개선

### 진화하는 표준에 맞춰 최신 상태 유지
- **MCP 사양 업데이트**: 공식 MCP 사양 변경 및 보안 권고를 모니터링합니다
- **위협 인텔리전스**: AI 보안 위협 피드 및 취약점 데이터베이스를 구독합니다  
- **커뮤니티 참여**: MCP 보안 커뮤니티 토론 및 작업 그룹에 참여합니다
- **정기 평가**: 분기별 보안 태세 평가를 수행하고 관행을 업데이트합니다

### MCP 보안에 기여하기
- **보안 연구**: MCP 보안 연구 및 취약점 공개 프로그램에 기여합니다
- **모범 사례 공유**: 보안 구현 및 교훈을 커뮤니티와 공유합니다
- **표준 개발**: MCP 사양 개발 및 보안 표준 작성에 참여
- **도구 개발**: MCP 생태계를 위한 보안 도구 및 라이브러리 개발 및 공유

---

*이 문서는 2025년 12월 18일 기준 MCP 사양 2025-11-25를 기반으로 한 MCP 보안 모범 사례를 반영합니다. 프로토콜과 위협 환경이 변화함에 따라 보안 관행은 정기적으로 검토 및 업데이트되어야 합니다.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->