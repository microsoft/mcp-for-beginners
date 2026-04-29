# 초보자를 위한 모델 컨텍스트 프로토콜(MCP) - 학습 가이드

이 학습 가이드는 "초보자를 위한 모델 컨텍스트 프로토콜(MCP)" 커리큘럼의 리포지토리 구조 및 내용을 개요합니다. 이 가이드를 사용하여 리포지토리를 효율적으로 탐색하고 이용 가능한 리소스를 최대한 활용하세요.

## 리포지토리 개요

모델 컨텍스트 프로토콜(MCP)은 AI 모델과 클라이언트 애플리케이션 간 상호작용을 위한 표준화된 프레임워크입니다. 처음에는 Anthropic에서 만들어졌으며, 현재는 공식 GitHub 조직을 통해 넓은 MCP 커뮤니티가 유지 관리하고 있습니다. 이 리포지토리는 C#, Java, JavaScript, Python, TypeScript의 실습 코드 예제와 함께 AI 개발자, 시스템 아키텍트, 소프트웨어 엔지니어를 위해 설계된 포괄적인 커리큘럼을 제공합니다.

## 시각적 커리큘럼 지도

```mermaid
mindmap
  root((초보자를 위한 MCP))
    00. 소개
      ::icon(fa fa-book)
      (프로토콜 개요)
      (표준화의 장점)
      (실제 사용 사례)
      (AI 통합 기본)
    01. 핵심 개념
      ::icon(fa fa-puzzle-piece)
      (클라이언트-서버 아키텍처)
      (프로토콜 구성 요소)
      (메시징 패턴)
      (전송 메커니즘)
      (작업 - 실험적)
      (도구 주석)
    02. 보안
      ::icon(fa fa-shield)
      (AI 특정 위협)
      (2025 모범 사례)
      (Azure 콘텐츠 안전)
      (인증 및 권한 부여)
      (Microsoft 프롬프트 보호)
      (OWASP MCP 상위 10)
      (Sherpa 보안 워크숍)
    03. 시작하기
      ::icon(fa fa-rocket)
      (첫 번째 서버 구현)
      (클라이언트 개발)
      (LLM 클라이언트 통합)
      (VS 코드 확장)
      (SSE 서버 설정)
      (HTTP 스트리밍)
      (AI 도구 통합)
      (테스트 프레임워크)
      (고급 서버 사용법)
      (간단한 인증)
      (배포 전략)
      (MCP 호스트 설정)
      (MCP 검사기)
    04. 실용 구현
      ::icon(fa fa-code)
      (다중 언어 SDK)
      (테스트 및 디버깅)
      (프롬프트 템플릿)
      (샘플 프로젝트)
      (프로덕션 패턴)
      (페이지네이션 전략)
    05. 고급 주제
      ::icon(fa fa-graduation-cap)
      (컨텍스트 엔지니어링)
      (Foundry 에이전트 통합)
      (다중 모드 AI 워크플로우)
      (OAuth2 인증)
      (실시간 검색)
      (스트리밍 프로토콜)
      (루트 컨텍스트)
      (라우팅 전략)
      (샘플링 기법)
      (확장 솔루션)
      (보안 강화)
      (Entra ID 통합)
      (웹 검색 MCP)
      (프로토콜 기능 심층 분석)
      (적대적 다중 에이전트 추론)
      
    06. 커뮤니티
      ::icon(fa fa-users)
      (코드 기여)
      (문서화)
      (MCP 클라이언트 생태계)
      (MCP 서버 레지스트리)
      (이미지 생성 도구)
      (GitHub 협업)
    07. 초기 채택
      ::icon(fa fa-lightbulb)
      (프로덕션 배포)
      (Microsoft MCP 서버)
      (Azure MCP 서비스)
      (기업 사례 연구)
      (미래 로드맵)
    08. 모범 사례
      ::icon(fa fa-check)
      (성능 최적화)
      (장애 허용)
      (시스템 복원력)
      (모니터링 및 가시성)
    09. 사례 연구
      ::icon(fa fa-file-text)
      (Azure API 관리)
      (AI 여행사)
      (Azure DevOps 통합)
      (문서화 MCP)
      (GitHub MCP 레지스트리)
      (VS 코드 통합)
      (실제 구현)
    10. 실습 워크숍
      ::icon(fa fa-laptop)
      (MCP 서버 기본)
      (고급 개발)
      (AI 도구 통합)
      (프로덕션 배포)
      (4개 실습 구조)
    11. 데이터베이스 통합 실습
      ::icon(fa fa-database)
      (PostgreSQL 통합)
      (리테일 분석 사용 사례)
      (행 수준 보안)
      (시맨틱 검색)
      (프로덕션 배포)
      (13개 실습 구조)
      (실습 학습)
```
## 리포지토리 구조

리포지토리는 MCP의 다양한 측면에 집중하는 열한 개 주요 섹션으로 구성되어 있습니다:

1. **소개 (00-Introduction/)**
   - 모델 컨텍스트 프로토콜 개요
   - AI 파이프라인에서 표준화가 중요한 이유
   - 실용적인 사용 사례와 장점

2. **핵심 개념 (01-CoreConcepts/)**
   - 클라이언트-서버 아키텍처
   - 주요 프로토콜 구성 요소
   - MCP의 메시징 패턴

3. **보안 (02-Security/)**
   - MCP 기반 시스템의 보안 위협
   - 구현 보안 모범 사례
   - 인증 및 권한 부여 전략
   - **포괄적인 보안 문서**:
     - MCP 보안 모범 사례 2025
     - Azure 콘텐츠 안전 구현 가이드
     - MCP 보안 제어 및 기법
     - MCP 모범 사례 빠른 참조
   - **주요 보안 주제**:
     - 프롬프트 주입 및 도구 중독 공격
     - 세션 탈취와 혼란스러운 대리인 문제
     - 토큰 전달 취약점
     - 과도한 권한 및 접근 제어
     - AI 구성요소 공급망 보안
     - Microsoft 프롬프트 실드 통합

4. **시작하기 (03-GettingStarted/)**
   - 환경 설정 및 구성
   - 기본 MCP 서버 및 클라이언트 생성
   - 기존 애플리케이션과 통합
   - 다음 섹션 포함:
     - 첫 서버 구현
     - 클라이언트 개발
     - LLM 클라이언트 통합
     - VS Code 연동
     - 서버-발신 이벤트(SSE) 서버
     - 고급 서버 사용법
     - HTTP 스트리밍
     - AI 툴킷 통합
     - 테스트 전략
     - 배포 가이드라인

5. **실전 구현 (04-PracticalImplementation/)**
   - 다양한 프로그래밍 언어용 SDK 사용법
   - 디버깅, 테스트, 검증 기법
   - 재사용 가능한 프롬프트 템플릿 및 워크플로우 제작
   - 구현 예제와 샘플 프로젝트

6. **심화 주제 (05-AdvancedTopics/)**
   - 컨텍스트 엔지니어링 기법
   - Foundry 에이전트 통합
   - 멀티모달 AI 워크플로우
   - OAuth2 인증 데모
   - 실시간 검색 기능
   - 실시간 스트리밍
   - 루트 컨텍스트 구현
   - 라우팅 전략
   - 샘플링 기법
   - 확장 방법론
   - 보안 고려사항
   - Entra ID 보안 통합
   - 웹 검색 통합
   - 공격적 멀티 에이전트 추론 (토론 패턴)

7. **커뮤니티 기여 (06-CommunityContributions/)**
   - 코드 및 문서 기여 방법
   - GitHub를 통한 협업
   - 커뮤니티 주도 개선 및 피드백
   - 다양한 MCP 클라이언트 사용법 (Claude Desktop, Cline, VSCode)
   - 이미지 생성 포함 인기 MCP 서버 작업법

8. **초기 도입 사례 (07-LessonsfromEarlyAdoption/)**
   - 실제 구현과 성공 사례
   - MCP 기반 솔루션 구축 및 배포
   - 트렌드 및 향후 로드맵
   - **Microsoft MCP 서버 가이드**: 10개 이상의 생산 준비된 Microsoft MCP 서버 종합 안내:
     - Microsoft Learn Docs MCP 서버
     - Azure MCP 서버 (15개 이상 전문 커넥터)
     - GitHub MCP 서버
     - Azure DevOps MCP 서버
     - MarkItDown MCP 서버
     - SQL Server MCP 서버
     - Playwright MCP 서버
     - Dev Box MCP 서버
     - Azure AI Foundry MCP 서버
     - Microsoft 365 Agents Toolkit MCP 서버

9. **모범 사례 (08-BestPractices/)**
   - 성능 튜닝 및 최적화
   - 내결함성 MCP 시스템 설계
   - 테스트 및 복원력 전략

10. **사례 연구 (09-CaseStudy/)**
    - <strong>7가지 포괄적인 사례 연구</strong>를 통해 MCP의 다재다능성 시연:
    - **Azure AI 여행 에이전트**: Azure OpenAI 및 AI 검색을 활용한 다중 에이전트 오케스트레이션
    - **Azure DevOps 통합**: YouTube 데이터 자동 업데이트 워크플로우 자동화
    - **실시간 문서 검색**: Python 콘솔 클라이언트와 HTTP 스트리밍
    - **인터랙티브 학습 계획 생성기**: Chainlit 웹 앱과 대화형 AI
    - **편집기 내 문서화**: VS Code와 GitHub Copilot 워크플로우 통합
    - **Azure API 관리**: 기업 API 통합과 MCP 서버 생성
    - **GitHub MCP 레지스트리**: 생태계 개발 및 에이전트 통합 플랫폼
    - 기업 통합, 개발자 생산성, 생태계 개발을 아우르는 구현 사례

11. **실습 워크숍 (10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/)**
    - MCP와 AI 툴킷을 결합한 포괄적 실습 워크숍
    - AI 모델과 실제 도구를 연결하는 지능형 애플리케이션 구축
    - 기초, 맞춤 서버 개발, 생산 배포 전략을 다루는 실용 모듈
    - **랩 구성**:
      - 랩 1: MCP 서버 기본
      - 랩 2: 고급 MCP 서버 개발
      - 랩 3: AI 툴킷 통합
      - 랩 4: 생산 환경 배포 및 확장
    - 단계별 지침이 포함된 랩 기반 학습

12. **MCP 서버 데이터베이스 통합 랩 (11-MCPServerHandsOnLabs/)**
    - PostgreSQL 통합으로 생산 환경 준비 MCP 서버 구축을 위한 **총 13개의 랩 학습 경로**
    - Zava Retail 사례를 사용한 실제 소매 분석 구현
    - 행 수준 보안(RLS), 의미 기반 검색, 다중 테넌트 데이터 접근 등 엔터프라이즈 패턴 포함
    - **완전한 랩 구성**:
      - **랩 00-03: 기초** - 소개, 아키텍처, 보안, 환경 설정
      - **랩 04-06: MCP 서버 구축** - 데이터베이스 설계, MCP 서버 구현, 도구 개발
      - **랩 07-09: 고급 기능** - 의미 검색, 테스트 및 디버깅, VS Code 통합
      - **랩 10-12: 생산 및 모범 사례** - 배포, 모니터링, 최적화
    - **사용 기술**: FastMCP 프레임워크, PostgreSQL, Azure OpenAI, Azure 컨테이너 앱, 애플리케이션 인사이트
    - **학습 성과**: 생산 준비된 MCP 서버, 데이터베이스 통합 패턴, AI 기반 분석, 기업 보안

## 추가 리소스

리포지토리에는 다음의 지원 리소스가 포함되어 있습니다:

- **이미지 폴더**: 커리큘럼 전반에 사용된 다이어그램 및 일러스트
- <strong>번역</strong>: 문서의 다중 언어 자동 번역 지원
- **공식 MCP 리소스**:
  - [MCP 문서](https://modelcontextprotocol.io/)
  - [MCP 사양](https://spec.modelcontextprotocol.io/)
  - [MCP GitHub 리포지토리](https://github.com/modelcontextprotocol)

## 이 리포지토리 사용 방법

1. **순차적 학습**: 구조화된 학습을 위해 00부터 11장까지 순서대로 진행하세요.
2. **언어별 집중**: 원하는 프로그래밍 언어의 샘플 디렉토리를 탐색하세요.
3. **실전 구현**: "시작하기" 섹션에서 환경을 구축하고 첫 MCP 서버 및 클라이언트를 만들어보세요.
4. **심화 탐구**: 기본기를 익힌 후 심화 주제로 넘어가 지식을 확장하세요.
5. **커뮤니티 참여**: GitHub 토론과 Discord 채널에서 MCP 커뮤니티에 참여해 전문가 및 동료 개발자와 교류하세요.

## MCP 클라이언트 및 도구

커리큘럼은 다양한 MCP 클라이언트 및 도구를 다룹니다:

1. **공식 클라이언트**:
   - Visual Studio Code
   - Visual Studio Code 내 MCP
   - Claude Desktop
   - VSCode 내 Claude
   - Claude API

2. **커뮤니티 클라이언트**:
   - Cline (터미널 기반)
   - Cursor (코드 에디터)
   - ChatMCP
   - Windsurf

3. **MCP 관리 도구**:
   - MCP CLI
   - MCP Manager
   - MCP Linker
   - MCP Router

## 인기 MCP 서버

리포지토리는 다양한 MCP 서버를 소개합니다:

1. **공식 Microsoft MCP 서버**:
   - Microsoft Learn Docs MCP 서버
   - Azure MCP 서버 (15개 이상 전문 커넥터)
   - GitHub MCP 서버
   - Azure DevOps MCP 서버
   - MarkItDown MCP 서버
   - SQL Server MCP 서버
   - Playwright MCP 서버
   - Dev Box MCP 서버
   - Azure AI Foundry MCP 서버
   - Microsoft 365 Agents Toolkit MCP 서버

2. **공식 참조 서버**:
   - 파일 시스템
   - Fetch
   - 메모리
   - 순차적 사고

3. **이미지 생성**:
   - Azure OpenAI DALL-E 3
   - Stable Diffusion WebUI
   - Replicate

4. **개발 도구**:
   - Git MCP
   - 터미널 제어
   - 코드 어시스턴트

5. **특화 서버**:
   - Salesforce
   - Microsoft Teams
   - Jira & Confluence

## 기여하기

이 리포지토리는 커뮤니티 기여를 환영합니다. MCP 생태계에 효과적으로 기여하는 방법은 커뮤니티 기여 섹션을 참조하세요.

----

*이 학습 가이드는 2026년 2월 5일 마지막 업데이트되었으며 최신 MCP 사양 2025-11-25를 반영하고 있습니다. 리포지토리 내용은 이 날짜 이후에 업데이트될 수 있습니다.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원본 문서는 해당 언어로 된 원문이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 당사가 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->