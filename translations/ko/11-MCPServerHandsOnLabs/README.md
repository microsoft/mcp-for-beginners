# 🚀 PostgreSQL과 함께하는 MCP 서버 - 완벽 학습 가이드

## 🧠 MCP 데이터베이스 통합 학습 경로 개요

이 포괄적인 학습 가이드는 실용적인 소매 분석 구현을 통해 데이터베이스와 통합된 **Model Context Protocol (MCP) 서버**를 구축하는 방법을 가르칩니다. **행 수준 보안(RLS)**, **시맨틱 검색**, **Azure AI 통합**, **멀티 테넌트 데이터 액세스**와 같은 엔터프라이즈급 패턴을 배울 수 있습니다.

백엔드 개발자, AI 엔지니어, 데이터 아키텍트 등 누구든지 이 가이드를 통해 구조화된 학습을 진행할 수 있으며, 실무 예제와 실습을 통해 MCP 서버를 단계적으로 배울 수 있습니다. 자세한 내용은 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail를 참조하세요.

## 🔗 공식 MCP 리소스

- 📘 [MCP 문서](https://modelcontextprotocol.io/) – 상세 튜토리얼 및 사용자 가이드
- 📜 [MCP 명세](https://modelcontextprotocol.io/docs/) – 프로토콜 아키텍처 및 기술 참조
- 🧑‍💻 [MCP GitHub 저장소](https://github.com/modelcontextprotocol) – 오픈소스 SDK, 도구 및 코드 샘플
- 🌐 [MCP 커뮤니티](https://github.com/orgs/modelcontextprotocol/discussions) – 토론에 참여하고 커뮤니티에 기여하세요

## 🧭 MCP 데이터베이스 통합 학습 경로

### 📚 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail에 대한 완벽 학습 구조

| 실습 | 주제 | 설명 | 링크 |
|--------|-------|-------------|------|
| **실습 1-3: 기초** | | | |
| 00 | [MCP 데이터베이스 통합 소개](./00-Introduction/README.md) | MCP와 데이터베이스 통합 및 소매 분석 사례 개요 | [시작하기](./00-Introduction/README.md) |
| 01 | [핵심 아키텍처 개념](./01-Architecture/README.md) | MCP 서버 아키텍처, 데이터베이스 계층 및 보안 패턴 이해 | [배우기](./01-Architecture/README.md) |
| 02 | [보안 및 멀티 테넌시](./02-Security/README.md) | 행 수준 보안, 인증 및 멀티 테넌트 데이터 액세스 | [배우기](./02-Security/README.md) |
| 03 | [환경 설정](./03-Setup/README.md) | 개발 환경, Docker, Azure 리소스 설정 | [설정하기](./03-Setup/README.md) |
| **실습 4-6: MCP 서버 구축** | | | |
| 04 | [데이터베이스 설계 및 스키마](./04-Database/README.md) | PostgreSQL 설정, 소매 스키마 설계 및 샘플 데이터 | [구축하기](./04-Database/README.md) |
| 05 | [MCP 서버 구현](./05-MCP-Server/README.md) | 데이터베이스 통합을 포함한 FastMCP 서버 구축 | [구축하기](./05-MCP-Server/README.md) |
| 06 | [도구 개발](./06-Tools/README.md) | 데이터베이스 쿼리 도구 및 스키마 탐색 도구 생성 | [구축하기](./06-Tools/README.md) |
| **실습 7-9: 고급 기능** | | | |
| 07 | [시맨틱 검색 통합](./07-Semantic-Search/README.md) | Azure OpenAI 및 pgvector를 활용한 벡터 임베딩 구현 | [심화하기](./07-Semantic-Search/README.md) |
| 08 | [테스트 및 디버깅](./08-Testing/README.md) | 테스트 전략, 디버깅 도구 및 검증 접근법 | [테스트하기](./08-Testing/README.md) |
| 09 | [VS Code 통합](./09-VS-Code/README.md) | VS Code MCP 통합 및 AI 채팅 사용 설정 | [통합하기](./09-VS-Code/README.md) |
| **실습 10-12: 프로덕션 및 모범 사례** | | | |
| 10 | [배포 전략](./10-Deployment/README.md) | Docker 배포, Azure Container Apps 및 확장 고려 사항 | [배포하기](./10-Deployment/README.md) |
| 11 | [모니터링 및 관찰성](./11-Monitoring/README.md) | Application Insights, 로깅, 성능 모니터링 | [모니터링하기](./11-Monitoring/README.md) |
| 12 | [모범 사례 및 최적화](./12-Best-Practices/README.md) | 성능 최적화, 보안 강화 및 프로덕션 팁 | [최적화하기](./12-Best-Practices/README.md) |

### 💻 여러분이 구축할 것

이 학습 경로를 완료하면 다음과 같은 기능을 갖춘 **Zava 소매 분석 MCP 서버**를 구축하게 됩니다:

- **다중 테이블 소매 데이터베이스**: 고객 주문, 제품, 재고 포함
- **행 수준 보안**: 매장 기반 데이터 분리
- **시맨틱 제품 검색**: Azure OpenAI 임베딩 활용
- **VS Code AI 채팅 통합**: 자연어 쿼리 지원
- **프로덕션 준비 배포**: Docker 및 Azure 활용
- **포괄적 모니터링**: Application Insights 포함

## 🎯 학습을 위한 사전 요구사항

이 학습 경로를 최대한 활용하려면 다음을 알고 있어야 합니다:

- **프로그래밍 경험**: Python(권장) 또는 유사한 언어에 대한 기본 지식
- **데이터베이스 지식**: SQL 및 관계형 데이터베이스에 대한 기본 이해
- **API 개념**: REST API 및 HTTP 개념 이해
- **개발 도구**: 명령줄, Git, 코드 편집기 사용 경험
- **클라우드 기초**: (선택 사항) Azure 또는 유사한 클라우드 플랫폼에 대한 기본 지식
- **Docker 이해**: (선택 사항) 컨테이너화 개념 이해

### 필수 도구

- **Docker Desktop** - PostgreSQL 및 MCP 서버 실행용
- **Azure CLI** - 클라우드 리소스 배포용
- **VS Code** - 개발 및 MCP 통합용
- **Git** - 버전 관리용
- **Python 3.8+** - MCP 서버 개발용

## 📚 학습 가이드 및 리소스

이 학습 경로는 효과적으로 탐색할 수 있도록 포괄적인 리소스를 제공합니다:

### 학습 가이드

각 실습에는 다음이 포함됩니다:
- **명확한 학습 목표** - 달성할 내용
- **단계별 지침** - 상세 구현 가이드
- **코드 예제** - 작동하는 샘플 및 설명
- **연습 문제** - 실습 기회
- **문제 해결 가이드** - 일반적인 문제 및 해결책
- **추가 리소스** - 추가 읽기 및 탐색

### 사전 요구사항 확인

각 실습 시작 전에 다음을 확인할 수 있습니다:
- **필요한 지식** - 사전에 알아야 할 내용
- **설정 검증** - 환경을 확인하는 방법
- **시간 추정** - 예상 완료 시간
- **학습 결과** - 완료 후 알게 될 내용

### 추천 학습 경로

경험 수준에 따라 경로를 선택하세요:

#### 🟢 **초보자 경로** (MCP 초보자)
1. 먼저 [MCP for Beginners](https://aka.ms/mcp-for-beginners)의 0-10을 완료하세요
2. 실습 00-03을 완료하여 기초를 강화하세요
3. 실습 04-06을 따라하며 실습을 진행하세요
4. 실습 07-09를 시도하여 실무 활용을 경험하세요

#### 🟡 **중급 경로** (MCP 경험 있음)
1. 실습 00-01을 검토하여 데이터베이스 관련 개념을 이해하세요
2. 실습 02-06에 집중하여 구현하세요
3. 실습 07-12를 깊이 탐구하여 고급 기능을 익히세요

#### 🔴 **고급 경로** (MCP 경험 풍부)
1. 실습 00-03을 간단히 살펴보세요
2. 실습 04-09에 집중하여 데이터베이스 통합을 익히세요
3. 실습 10-12에 집중하여 프로덕션 배포를 준비하세요

## 🛠️ 이 학습 경로를 효과적으로 사용하는 방법

### 순차적 학습 (권장)

포괄적인 이해를 위해 실습을 순서대로 진행하세요:

1. **개요 읽기** - 학습할 내용을 이해하세요
2. **사전 요구사항 확인** - 필요한 지식을 확인하세요
3. **단계별 가이드 따라하기** - 학습하며 구현하세요
4. **연습 문제 완료** - 이해를 강화하세요
5. **핵심 내용 복습** - 학습 결과를 확고히 하세요

### 목표 학습

특정 기술이 필요하다면:

- **데이터베이스 통합**: 실습 04-06에 집중하세요
- **보안 구현**: 실습 02, 08, 12에 집중하세요
- **AI/시맨틱 검색**: 실습 07을 깊이 탐구하세요
- **프로덕션 배포**: 실습 10-12를 공부하세요

### 실습

각 실습에는 다음이 포함됩니다:
- **작동하는 코드 예제** - 복사, 수정 및 실험
- **실무 시나리오** - 실용적인 소매 분석 사례
- **점진적 복잡성** - 간단한 것부터 고급까지 구축
- **검증 단계** - 구현이 작동하는지 확인

## 🌟 커뮤니티 및 지원

### 도움 받기

- **Azure AI Discord**: [전문가 지원 받기](https://discord.com/invite/ByRwuEEgH4)
- **GitHub 저장소 및 구현 샘플**: [배포 샘플 및 리소스](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP 커뮤니티**: [MCP 관련 토론 참여](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 시작할 준비가 되셨나요?

**[실습 00: MCP 데이터베이스 통합 소개](./00-Introduction/README.md)**로 여정을 시작하세요.

---

*이 포괄적이고 실습 중심의 학습 경험을 통해 데이터베이스 통합을 갖춘 프로덕션 준비 MCP 서버 구축을 마스터하세요.*

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.