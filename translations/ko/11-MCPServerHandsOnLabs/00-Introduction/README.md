# MCP 데이터베이스 통합 소개

> [!NOTE]
> 이 학습 경로의 HTTP/SSE 또는 초기화 옵션을 사용하는 다이어그램 또는 코드는 샘플 MCP `2025-11-25` 종속성을 반영합니다. 새로운 구현에는 `2026-07-28` 무상태 요청과 Streamable HTTP를 사용하세요.
> 
>

## 🎯 이 실습에서 다루는 내용

이 소개 실습은 MCP(Model Context Protocol) 서버를 데이터베이스 통합과 함께 구축하는 포괄적인 개요를 제공합니다. https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail의 Zava Retail 분석 사례를 통해 비즈니스 사례, 기술 아키텍처 및 실제 적용 사례를 이해할 수 있습니다.

## 개요

**Model Context Protocol (MCP)** 은 AI 어시스턴트가 외부 데이터 소스에 안전하게 실시간으로 접근하고 상호작용할 수 있도록 합니다. 데이터베이스 통합과 결합 시 MCP는 데이터 기반 AI 애플리케이션에 강력한 기능을 제공합니다.

이 학습 경로에서는 PostgreSQL을 통해 AI 어시스턴트를 소매 판매 데이터에 연결하는 프로덕션 준비된 MCP 서버를 구축하는 방법, Row Level Security, 의미 기반 검색, 다중 테넌트 데이터 접근과 같은 엔터프라이즈 패턴 구현법을 배웁니다.

## 학습 목표

이 실습이 끝나면 다음을 할 수 있습니다:

- **MCP 정의** 및 데이터베이스 통합의 핵심 이점 설명
- **MCP 서버 아키텍처** 내 주요 구성요소 식별
- Zava Retail 사례 및 비즈니스 요구사항 <strong>이해</strong>
- 안전하고 확장 가능한 데이터베이스 액세스를 위한 **엔터프라이즈 패턴 인식**
- 이 학습 경로에 사용되는 도구와 기술 <strong>목록화</strong>

## 🧭 도전 과제: AI와 실제 데이터의 만남

### 전통적인 AI 제한 사항

현대 AI 어시스턴트는 매우 강력하지만 실제 비즈니스 데이터 작업에서는 다음과 같은 주요 한계가 있습니다:

| **도전 과제** | <strong>설명</strong> | **비즈니스 영향** |
|---------------|-----------------|-------------------|
| **정적 지식** | 고정된 데이터셋으로 훈련된 AI 모델은 최신 비즈니스 데이터에 접근할 수 없음 | 구식 통찰력, 놓치는 기회 |
| **데이터 사일로** | 데이터베이스, API, 시스템에 잠긴 정보는 AI가 접근 불가 | 불완전한 분석, 분절된 업무 흐름 |
| **보안 제약** | 직접 데이터베이스 접근에서 보안 및 규정 문제 발생 | 제한된 배포, 수동 데이터 준비 |
| **복잡한 쿼리** | 비즈니스 사용자가 데이터 분석에 기술 지식 필요 | 낮은 채택률, 비효율적 프로세스 |

### MCP 솔루션

Model Context Protocol은 다음을 제공하여 이 문제들을 해결합니다:

- **실시간 데이터 접근**: AI 어시스턴트가 라이브 데이터베이스와 API를 쿼리
- **안전한 통합**: 인증과 권한으로 제어되는 접근
- **자연어 인터페이스**: 비즈니스 사용자가 일상 언어로 질문 가능
- **표준 프로토콜**: 다양한 AI 플랫폼과 도구에서 작동

## 🏪 Zava Retail 소개: 학습 사례 https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

이 학습 경로 전반에 걸쳐, 다수 매장을 운영하는 가상의 DIY 소매 체인 <strong>Zava Retail</strong>을 위한 MCP 서버를 구축합니다. 이 현실감 있는 시나리오는 엔터프라이즈 급 MCP 구현을 보여줍니다.

### 비즈니스 컨텍스트

<strong>Zava Retail</strong>은 다음을 운영합니다:
- 워싱턴 주 내 **8개 오프라인 매장** (시애틀, 벨뷰, 타코마, 스포캔, 에버렛, 레드먼드, 커클랜드)
- 전자상거래를 위한 **1개 온라인 매장**
- 공구, 하드웨어, 정원용품, 건축 자재 등 다양한 **제품 카탈로그**
- 매장 관리자, 지역 관리자, 임원을 포함한 **다단계 관리 체계**

### 비즈니스 요구사항

매장 관리자와 임원은 AI 기반 분석을 필요로 합니다:

1. **판매 실적 분석** (매장별 및 기간별)
2. **재고 수준 추적** 및 리스톡 필요성 파악
3. **고객 행동** 및 구매 패턴 이해
4. 의미 기반 검색을 통한 **제품 인사이트 발견**
5. 자연어 쿼리를 통한 **보고서 생성**
6. 역할 기반 접근 제어로 **데이터 보안 유지**

### 기술 요구사항

MCP 서버는 다음을 제공해야 합니다:

- 매장 관리자는 자신 매장 데이터만 보는 **다중 테넌트 데이터 접근**
- 복잡한 SQL 연산을 지원하는 **유연한 쿼리 기능**
- 제품 발견 및 추천을 위한 **의미 기반 검색**
- 현재 비즈니스 상태를 반영하는 **실시간 데이터**
- 행 수준 보안을 갖춘 **안전한 인증**
- 여러 동시 사용자 지원하는 **확장 가능한 아키텍처**

## 🏗️ MCP 서버 아키텍처 개요

MCP 서버는 데이터베이스 통합 최적화된 계층형 아키텍처를 구현합니다:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### 주요 구성요소

#### **1. MCP 서버 계층**
- **FastMCP 프레임워크**: 최신 Python MCP 서버 구현
- **도구 등록**: 유형 안전성을 보장하는 선언적 도구 정의
- **요청 컨텍스트**: 사용자 아이덴티티 및 세션 관리
- **오류 처리**: 견고한 오류 관리 및 로깅

#### **2. 데이터베이스 통합 계층**
- **커넥션 풀링**: 효율적인 asyncpg 연결 관리
- **스키마 제공자**: 동적 테이블 스키마 탐색
- **쿼리 실행기**: RLS 컨텍스트를 갖춘 안전한 SQL 실행
- **트랜잭션 관리**: ACID 준수 및 롤백 처리

#### **3. 보안 계층**
- **행 수준 보안(RLS)**: 다중 테넌트 데이터 격리를 위한 PostgreSQL RLS
- **사용자 아이덴티티**: 매장 관리자 인증 및 권한 부여
- **접근 제어**: 세밀한 권한과 감사 추적
- **입력 검증**: SQL 인젝션 예방 및 쿼리 검증

#### **4. AI 향상 계층**
- **의미 검색**: 제품 발견을 위한 벡터 임베딩
- **Azure OpenAI 통합**: 텍스트 임베딩 생성
- **유사도 알고리즘**: pgvector 코사인 유사도 검색
- **검색 최적화**: 인덱싱 및 성능 튜닝

## 🔧 기술 스택

### 핵심 기술

| **구성 요소** | <strong>기술</strong> | <strong>목적</strong> |
|---------------|----------------|-------------|
| **MCP 프레임워크** | FastMCP (Python) | 최신 MCP 서버 구현 |
| <strong>데이터베이스</strong> | PostgreSQL 17 + pgvector | 벡터 검색이 가능한 관계형 데이터 |
| **AI 서비스** | Azure OpenAI | 텍스트 임베딩 및 언어 모델 |
| <strong>컨테이너화</strong> | Docker + Docker Compose | 개발 환경 |
| **클라우드 플랫폼** | Microsoft Azure | 프로덕션 배포 |
| **IDE 통합** | VS Code | AI 채팅 및 개발 워크플로우 |

### 개발 도구

| <strong>도구</strong> | <strong>목적</strong> |
|----------|-------------|
| **asyncpg** | 고성능 PostgreSQL 드라이버 |
| **Pydantic** | 데이터 검증 및 직렬화 |
| **Azure SDK** | 클라우드 서비스 통합 |
| **pytest** | 테스트 프레임워크 |
| **Docker** | 컨테이너화 및 배포 |

### 프로덕션 스택

| <strong>서비스</strong> | **Azure 리소스** | <strong>목적</strong> |
|-------------|-------------------|-------------|
| <strong>데이터베이스</strong> | Azure Database for PostgreSQL | 관리형 데이터베이스 서비스 |
| <strong>컨테이너</strong> | Azure Container Apps | 서버리스 컨테이너 호스팅 |
| **AI 서비스** | Microsoft Foundry | OpenAI 모델 및 엔드포인트 |
| <strong>모니터링</strong> | Application Insights | 가시성 및 진단 |
| <strong>보안</strong> | Azure Key Vault | 비밀 및 구성 관리 |

## 🎬 실제 사용 시나리오

다양한 사용자가 MCP 서버와 상호작용하는 방식을 살펴봅시다:

### 시나리오 1: 매장 관리자 성과 리뷰

<strong>사용자</strong>: Sarah, 시애틀 매장 관리자  
<strong>목표</strong>: 2024년 4분기 매출 실적 분석

**자연어 쿼리**:
> "내 매장의 2024년 4분기 매출 상위 10개 제품 보여줘"

**일어나는 일**:
1. VS Code AI 채팅이 쿼리를 MCP 서버에 전송
2. MCP 서버가 Sarah의 매장 컨텍스트(시애틀)를 식별
3. RLS 정책이 시애틀 매장 데이터만 필터링
4. SQL 쿼리 생성 및 실행
5. 결과를 형식화해 AI 채팅에 반환
6. AI가 분석과 통찰 제공

### 시나리오 2: 의미 기반 검색을 통한 제품 발견

<strong>사용자</strong>: Mike, 재고 관리자  
<strong>목표</strong>: 고객 요청과 유사한 제품 찾기

**자연어 쿼리**:
> "'야외용 방수 전기 커넥터'와 유사한 제품 무엇이 있나요?"

**일어나는 일**:
1. 쿼리가 의미 기반 검색 도구로 처리됨
2. Azure OpenAI가 임베딩 벡터 생성
3. pgvector가 유사도 검색 수행
4. 관련 제품이 관련도에 따라 순위 매김
5. 결과에 제품 세부정보 및 재고 포함
6. AI가 대안 및 묶음 구매 기회 제안

### 시나리오 3: 매장 간 분석

<strong>사용자</strong>: Jennifer, 지역 관리자  
<strong>목표</strong>: 모든 매장의 성과 비교

**자연어 쿼리**:
> "지난 6개월간 모든 매장의 카테고리별 매출 비교해줘"

**일어나는 일**:
1. 지역 관리자 접근을 위한 RLS 컨텍스트 설정
2. 복잡한 다중 매장 쿼리 생성
3. 매장 위치별 데이터 집계
4. 결과에 추세 및 비교 포함
5. AI가 인사이트와 권장 사항 식별

## 🔒 보안 및 다중 테넌시 심층 분석

우리의 구현은 엔터프라이즈급 보안을 우선합니다:

### 행 수준 보안 (RLS)

PostgreSQL RLS는 데이터 격리를 보장합니다:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### 사용자 아이덴티티 관리

각 MCP 연결은 다음을 포함합니다:
- **매장 관리자 ID**: RLS 컨텍스트용 고유 식별자
- **역할 할당**: 권한 및 접근 수준
- **세션 관리**: 안전한 인증 토큰
- **감사 로깅**: 전체 접근 기록

### 데이터 보호

다중 보안 계층:
- **연결 암호화**: 모든 데이터베이스 연결에 TLS 적용
- **SQL 인젝션 예방**: 매개변수화된 쿼리만 사용
- **입력 검증**: 포괄적인 요청 검증
- **오류 처리**: 오류 메시지에 민감 정보 없음

## 🎯 주요 시사점

소개를 완료하면 다음을 이해할 수 있습니다:

✅ **MCP 가치 제안**: MCP가 AI 어시스턴트와 실제 데이터를 연결하는 방식  
✅ **비즈니스 컨텍스트**: Zava Retail의 요구사항과 도전과제  
✅ **아키텍처 개요**: 주요 구성요소와 이들의 상호작용  
✅ **기술 스택**: 사용된 도구와 프레임워크  
✅ **보안 모델**: 다중 테넌트 데이터 접근 및 보호  
✅ **사용 패턴**: 실제 쿼리 시나리오와 워크플로우  

## 🚀 다음 단계

더 깊이 들어갈 준비가 되셨나요? 다음을 진행하세요:

**[Lab 01: 핵심 아키텍처 개념](../01-Architecture/README.md)**

MCP 서버 아키텍처 패턴, 데이터베이스 설계 원칙, 소매 분석 솔루션을 구동하는 자세한 기술 구현에 대해 배웁니다.

## 📚 추가 자료

### MCP 문서
- [MCP 사양](https://modelcontextprotocol.io/docs/) - 공식 프로토콜 문서
- [초보자를 위한 MCP](https://aka.ms/mcp-for-beginners) - 포괄적 MCP 학습 안내서
- [FastMCP 문서](https://github.com/modelcontextprotocol/python-sdk) - Python SDK 문서

### 데이터베이스 통합
- [PostgreSQL 문서](https://www.postgresql.org/docs/) - 완전한 PostgreSQL 참고 자료
- [pgvector 가이드](https://github.com/pgvector/pgvector) - 벡터 확장 문서
- [행 수준 보안](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS 가이드

### Azure 서비스
- [Azure OpenAI 문서](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI 서비스 통합
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - 관리형 데이터베이스 서비스
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - 서버리스 컨테이너

---

**면책 조항**: 이 학습 자료는 가상의 소매 데이터를 사용한 연습용입니다. 실제 환경에 유사한 솔루션을 구현할 때는 조직의 데이터 거버넌스 및 보안 정책을 항상 준수하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->