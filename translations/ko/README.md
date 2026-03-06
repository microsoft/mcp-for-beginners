![MCP-for-beginners](../../translated_images/ko/mcp-beginners.2ce2b317996369ff.webp) 

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/mcp-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/mcp-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/mcp-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

다음 단계에 따라 이 리소스를 사용하여 시작하세요:
1. **저장소 포크하기**: 클릭 [![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
2. **저장소 클론하기**:   `git clone https://github.com/microsoft/mcp-for-beginners.git`
3. **가입하기** [![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


### 🌐 다국어 지원

#### GitHub Action을 통한 지원 (자동화 및 항상 최신 상태 유지)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](./README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **로컬 클론을 선호하시나요?**
>
> 이 저장소에는 50개 이상의 언어 번역이 포함되어 있어 다운로드 크기가 상당히 커집니다. 번역 없이 클론하려면 sparse checkout을 사용하세요:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 이렇게 하면 훨씬 빠른 다운로드로 코스를 완료하는 데 필요한 모든 것을 얻을 수 있습니다.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

# 🚀 초보자를 위한 Model Context Protocol (MCP) 커리큘럼

## **C#, Java, JavaScript, Rust, Python 및 TypeScript로 실습하는 MCP 학습**

## 🧠 Model Context Protocol 커리큘럼 개요
Model Context Protocol 여정에 오신 것을 환영합니다! AI 애플리케이션이 다양한 도구와 서비스와 어떻게 소통하는지 궁금했다면, 이제 개발자가 지능형 시스템을 구축하는 방식을 변화시키는 우아한 솔루션을 발견할 준비가 되셨습니다.

MCP를 AI 애플리케이션을 위한 범용 번역기라고 생각해 보세요—USB 포트가 모든 기기를 컴퓨터에 연결할 수 있게 하듯, MCP는 AI 모델이 어떤 도구나 서비스와도 표준화된 방식으로 연결되도록 합니다. 처음 챗봇을 만들든 복잡한 AI 워크플로우를 작업하든, MCP를 이해하면 더욱 강력하고 유연한 애플리케이션을 만들 수 있는 힘을 얻게 됩니다.

이 커리큘럼은 여러분의 학습 여정을 위한 인내심과 세심함을 바탕으로 설계되었습니다. 이미 알고 있는 간단한 개념부터 시작해, 좋아하는 프로그래밍 언어로 실습을 통해 점진적으로 전문성을 키워 나갈 것입니다. 모든 단계마다 명확한 설명, 실용적인 예제, 그리고 충분한 응원이 함께합니다.

이 여정을 완료할 때쯤이면 자신만의 MCP 서버를 구축하고, 인기 있는 AI 플랫폼과 통합하며, 이 기술이 AI 개발의 미래를 어떻게 재구성하고 있는지 이해하는 자신감을 갖게 될 것입니다. 함께 이 흥미진진한 모험을 시작해 봅시다!

### 공식 문서 및 명세서

이 커리큘럼은 **MCP Specification 2025-11-25** (최신 안정 버전)에 맞춰져 있습니다. MCP 명세서는 날짜 기반 버전 관리(YYYY-MM-DD 형식)를 사용하여 명확한 프로토콜 버전 추적을 보장합니다.

이 자료들은 여러분의 이해가 깊어질수록 더욱 가치 있어지지만, 모든 내용을 즉시 읽어야 한다는 부담은 가지지 마세요. 가장 관심 가는 부분부터 시작하세요!
- 📘 [MCP 문서](https://modelcontextprotocol.io/) – 단계별 튜토리얼과 사용자 가이드를 제공하는 주요 리소스입니다. 초보자를 위해 작성되어 여러분이 자신의 속도로 쉽게 따라할 수 있는 명확한 예제가 포함되어 있습니다.
- 📜 [MCP 명세서](https://modelcontextprotocol.io/specification/2025-11-25) – 종합적인 참고 매뉴얼로 생각하세요. 커리큘럼을 진행하면서 특정 세부 사항을 확인하고 고급 기능을 탐험하기 위해 자주 참조하게 될 것입니다.
- 📜 [MCP 명세서 버전 관리](https://modelcontextprotocol.io/specification/versioning) – 프로토콜 버전 이력과 MCP가 날짜 기반 버전(YYYY-MM-DD 형식)을 사용하는 방법에 대한 정보를 담고 있습니다.
- 🧑‍💻 [MCP GitHub 저장소](https://github.com/modelcontextprotocol) – 여러 프로그래밍 언어로 된 SDK, 도구 및 코드 샘플을 찾을 수 있습니다. 실용적인 예제와 바로 사용할 수 있는 컴포넌트가 가득한 보물창고와 같습니다.
- 🌐 [MCP 커뮤니티](https://github.com/orgs/modelcontextprotocol/discussions) – 동료 학습자 및 숙련 개발자들과 MCP에 대해 토론하고 질문할 수 있는 지원적인 커뮤니티입니다. 지식이 자유롭게 공유됩니다.
  
## 학습 목표

이 커리큘럼을 마치면 새로운 능력에 대해 자신감과 흥분을 느끼게 될 것입니다. 달성할 내용은 다음과 같습니다:

• **MCP 기본 개념 이해**: Model Context Protocol이 무엇인지, AI 애플리케이션이 함께 작동하는 방식을 혁신하는 이유를 비유와 예제를 통해 이해하게 됩니다.

• **첫 MCP 서버 구축**: 선호하는 프로그래밍 언어로 동작하는 MCP 서버를 만들어 보고, 간단한 예제부터 단계별로 실력을 키워 나갑니다.

• **AI 모델을 실제 도구에 연결**: AI 모델과 실제 서비스를 잇는 방법을 배우며, 애플리케이션에 강력한 새로운 기능을 부여합니다.

• **보안 모범 사례 구현**: MCP 구현을 안전하게 유지하는 방법을 이해하고, 애플리케이션과 사용자를 보호하는 최선의 관행을 배웁니다.

• **자신감 있는 배포**: 개발에서 프로덕션까지 MCP 프로젝트를 안정적으로 진행하는 실제 배포 전략을 익힙니다.

• **MCP 커뮤니티 참여**: AI 애플리케이션 개발의 미래를 만들어 가는 성장하는 개발자 커뮤니티의 일원이 됩니다.

## 필수 배경 지식

MCP의 구체적인 내용을 파고들기 전에 몇 가지 기초 개념에 대해 편안함을 느끼시길 바랍니다. 전문가가 아니어도 걱정 마세요—필요한 모든 것을 설명해 드립니다!

### 프로토콜 이해하기 (기초)

프로토콜은 대화의 규칙과 같습니다. 친구에게 전화할 때 서로 "안녕하세요"라고 인사하고, 차례대로 말하며, 끝나면 "잘 가"라고 하죠. 컴퓨터 프로그램도 효과적으로 소통하려면 비슷한 규칙이 필요합니다.

MCP는 프로토콜입니다—AI 모델과 애플리케이션이 도구 및 서비스와 생산적으로 "대화"하기 위해 합의한 규칙 모음입니다. 인간 소통에서 규칙이 원활함을 만든 것처럼, MCP가 AI 애플리케이션의 소통을 훨씬 신뢰할 수 있고 강력하게 만듭니다.

### 클라이언트-서버 관계 (프로그램 협력 방식)

여러분은 이미 매일 클라이언트-서버 관계를 사용하고 있습니다! 웹 브라우저(클라이언트)를 사용해 웹사이트에 접속할 때, 웹 서버가 페이지 내용을 보내줍니다. 브라우저는 정보를 요청하는 방법을 알고, 서버는 응답하는 방법을 압니다.

MCP에도 비슷한 관계가 있습니다: AI 모델은 정보를 요청하거나 작업을 요청하는 클라이언트 역할을 하고, MCP 서버는 그 기능을 제공합니다. AI가 특정 작업을 수행하도록 요청할 수 있는 조수(서버)와 같습니다.

### 표준화가 중요한 이유 (호환성 확보)

모든 자동차 제조사가 다른 모양의 주유구를 쓴다면 각 차마다 다른 변환기가 필요할 거예요! 표준화는 공통 방식을 정해 원활한 연결을 가능하게 합니다.

MCP는 AI 애플리케이션을 위한 이 표준화를 제공합니다. 모든 AI 모델이 각각의 도구에 특화된 코드를 쓸 필요 없이, MCP가 모두가 소통할 수 있는 보편적 방법을 만듭니다. 덕분에 개발자가 한 번 도구를 만들면 다양한 AI 시스템과 함께 작동할 수 있습니다.

## 🧭 학습 경로 개요

여러분의 MCP 여정은 자신감과 실력을 점진적으로 쌓을 수 있도록 체계적으로 구성되어 있습니다. 각 단계는 새로운 개념을 소개하면서 이미 배운 내용을 강화합니다.

### 🌱 기초 단계: 기본 개념 이해 (모듈 0-2)

모험은 여기서 시작됩니다! 익숙한 비유와 간단한 예제를 통해 MCP 개념을 소개합니다. MCP가 무엇인지, 왜 존재하는지, 그리고 AI 개발 세계에서 어떻게 자리 잡는지 이해하게 될 것입니다.

• **모듈 0 - MCP 소개**: MCP가 무엇이며 현대 AI 애플리케이션에 왜 중요한지 탐구합니다. 실제 MCP 사례를 보고 개발자가 흔히 겪는 문제를 어떻게 해결하는지 알게 됩니다.

• **모듈 1 - 핵심 개념 설명**: MCP의 필수 구성 요소를 배웁니다. 풍부한 비유와 시각적 예제를 사용해 자연스럽고 이해하기 쉬운 개념으로 만듭니다.

• **모듈 2 - MCP 보안**: 보안은 어렵게 느껴질 수 있지만, MCP가 내장된 보안 기능을 어떻게 포함하는지, 애플리케이션을 처음부터 안전하게 보호하는 모범 사례를 알려줍니다.

### 🔨 구축 단계: 첫 구현 만들기 (모듈 3)

이제 진짜 재미가 시작됩니다! 실제 MCP 서버와 클라이언트를 만드는 실습을 하게 됩니다. 걱정하지 마세요—간단한 예제로 시작해 모든 단계를 안내해 드립니다.
이 모듈에는 선호하는 프로그래밍 언어로 연습할 수 있는 여러 실습 가이드가 포함되어 있습니다. 첫 번째 서버를 만들고, 서버에 연결하는 클라이언트를 구축하며, VS Code와 같은 인기 개발 도구와도 통합할 수 있습니다.

각 가이드에는 완전한 코드 예제, 문제 해결 팁, 그리고 특정 설계 선택을 하는 이유에 대한 설명이 포함되어 있습니다. 이 단계를 마치면 자랑스러워할 수 있는 작동하는 MCP 구현체를 갖게 될 것입니다!

### 🚀 성장 단계: 고급 개념 및 실무 적용 (모듈 4-5)

기본을 마스터한 후에는 보다 정교한 MCP 기능을 탐구할 준비가 된 것입니다. 실제 구현 전략, 디버깅 기법, 멀티모달 AI 통합과 같은 고급 주제를 다룰 예정입니다.

또한 MCP 구현체를 프로덕션 용도로 확장하는 방법과 Azure 같은 클라우드 플랫폼과의 통합 방법도 배우게 됩니다. 이 모듈들은 실제 요구 사항을 처리할 수 있는 MCP 솔루션을 구축할 수 있도록 준비시켜 줍니다.

### 🌟 숙련 단계: 커뮤니티 및 전문화 (모듈 6-11)

최종 단계는 MCP 커뮤니티에 참여하고 관심 분야에 전문화하는 데 중점을 둡니다. 오픈 소스 MCP 프로젝트에 기여하는 방법, 고급 인증 패턴 구현, 데이터베이스 통합 솔루션 구축법을 배우게 됩니다.

특히 모듈 11은 PostgreSQL 통합과 함께 프로덕션 준비가 된 MCP 서버를 구축하는 방법을 가르치는 완전한 13개 실습 랩으로 구성된 학습 경로입니다. 지금까지 배운 모든 내용을 종합하는 캡스톤 프로젝트와 같습니다!

### 📚 전체 커리큘럼 구조

| Module | Topic | Description | Link |
|--------|-------|-------------|------|
| **모듈 0-3: 기초** | | | |
| 00 | MCP 소개 | 모델 컨텍스트 프로토콜과 AI 파이프라인에서의 중요성 개요 | [자세히 읽기](./00-Introduction/README.md) |
| 01 | 핵심 개념 설명 | 핵심 MCP 개념 심층 탐구 | [자세히 읽기](./01-CoreConcepts/README.md) |
| 02 | MCP 보안 | 보안 위협 및 모범 사례 | [자세히 읽기](./02-Security/README.md) |
| 03 | MCP 시작하기 | 환경 설정, 기본 서버/클라이언트, 통합 | [자세히 읽기](./03-GettingStarted/README.md) |
| **모듈 3: 첫 서버 및 클라이언트 구축** | | | |
| 3.1 | 첫 서버 | 첫 번째 MCP 서버 생성 | [가이드](./03-GettingStarted/01-first-server/README.md) |
| 3.2 | 첫 클라이언트 | 기본 MCP 클라이언트 개발 | [가이드](./03-GettingStarted/02-client/README.md) |
| 3.3 | LLM 클라이언트 | 대형 언어 모델 통합 | [가이드](./03-GettingStarted/03-llm-client/README.md) |
| 3.4 | VS Code 통합 | VS Code에서 MCP 서버 사용 | [가이드](./03-GettingStarted/04-vscode/README.md) |
| 3.5 | stdio 서버 | stdio 전송 방식 서버 생성 | [가이드](./03-GettingStarted/05-stdio-server/README.md) |
| 3.6 | HTTP 스트리밍 | MCP에서 HTTP 스트리밍 구현 | [가이드](./03-GettingStarted/06-http-streaming/README.md) |
| 3.7 | AI 툴킷 | AI 툴킷을 사용한 MCP | [가이드](./03-GettingStarted/07-aitk/README.md) |
| 3.8 | 테스트 | MCP 서버 구현 테스트 | [가이드](./03-GettingStarted/08-testing/README.md) |
| 3.9 | 배포 | MCP 서버 프로덕션 배포 | [가이드](./03-GettingStarted/09-deployment/README.md) |
| 3.10 | 고급 서버 사용 | 고급 기능 사용 및 아키텍처 개선을 위한 고급 서버 활용 | [가이드](./03-GettingStarted/10-advanced/README.md) |
| 3.11 | 간단한 인증 | 처음부터 인증과 RBAC 보여주기 | [가이드](./03-GettingStarted/11-simple-auth/README.md) |
| 3.12 | MCP 호스트 | Claude Desktop, Cursor, Cline 등 MCP 호스트 구성 | [가이드](./03-GettingStarted/12-mcp-hosts/README.md) |
| 3.13 | MCP 인스펙터 | Inspector 도구로 MCP 서버 디버깅 및 테스트 | [가이드](./03-GettingStarted/13-mcp-inspector/README.md) |
| 3.14 | 샘플링 | 클라이언트와 협업하는 샘플링 사용법 | [가이드](./03-GettingStarted/14-sampling/README.md) |
| 3.15 | MCP 앱 | MCP 앱 구축 | [가이드](./03-GettingStarted/15-mcp-apps/README.md) |
| **모듈 4-5: 실무 및 고급** | | | |
| 04 | 실무 구현 | SDK, 디버깅, 테스트, 재사용 가능한 프롬프트 템플릿 | [자세히 읽기](./04-PracticalImplementation/README.md) |
| 4.1 | 페이지네이션 | 커서 기반 페이지네이션으로 대용량 결과 처리 | [가이드](./04-PracticalImplementation/pagination/README.md) |
| 05 | MCP 고급 주제 | 멀티모달 AI, 확장성, 기업용 사례 | [자세히 읽기](./05-AdvancedTopics/README.md) |
| 5.1 | Azure 통합 | Azure와 MCP 통합 | [가이드](./05-AdvancedTopics/mcp-integration/README.md) |
| 5.2 | 멀티모달 | 여러 모달리티 다루기 | [가이드](./05-AdvancedTopics/mcp-multi-modality/README.md) |
| 5.3 | OAuth2 데모 | OAuth2 인증 구현 | [가이드](./05-AdvancedTopics/mcp-oauth2-demo/README.md) |
| 5.4 | 루트 컨텍스트 | 루트 컨텍스트 이해 및 구현 | [가이드](./05-AdvancedTopics/mcp-root-contexts/README.md) |
| 5.5 | 라우팅 | MCP 라우팅 전략 | [가이드](./05-AdvancedTopics/mcp-routing/README.md) |
| 5.6 | 샘플링 | MCP 샘플링 기법 | [가이드](./05-AdvancedTopics/mcp-sampling/README.md) |
| 5.7 | 확장 | MCP 구현 확장 | [가이드](./05-AdvancedTopics/mcp-scaling/README.md) |
| 5.8 | 보안 | 고급 보안 고려사항 | [가이드](./05-AdvancedTopics/mcp-security/README.md) |
| 5.9 | 웹 검색 | 웹 검색 기능 구현 | [가이드](./05-AdvancedTopics/web-search-mcp/README.md) |
| 5.10 | 실시간 스트리밍 | 실시간 스트리밍 기능 구축 | [가이드](./05-AdvancedTopics/mcp-realtimestreaming/README.md) |
| 5.11 | 실시간 검색 | 실시간 검색 구현 | [가이드](./05-AdvancedTopics/mcp-realtimesearch/README.md) |
| 5.12 | Entra ID 인증 | Microsoft Entra ID를 이용한 인증 | [가이드](./05-AdvancedTopics/mcp-security-entra/README.md) |
| 5.13 | Foundry 통합 | Azure AI Foundry와 통합 | [가이드](./05-AdvancedTopics/mcp-foundry-agent-integration/README.md) |
| 5.14 | 컨텍스트 엔지니어링 | 효과적인 컨텍스트 엔지니어링 기법 | [가이드](./05-AdvancedTopics/mcp-contextengineering/README.md) |
| 5.15 | MCP 맞춤 전송 | 맞춤형 전송 구현 | [가이드](./05-AdvancedTopics/mcp-transport/README.md) |
| 5.16 | 프로토콜 기능 | 진행 알림, 취소, 리소스 템플릿 | [가이드](./05-AdvancedTopics/mcp-protocol-features/README.md) |
| **모듈 6-10: 커뮤니티 및 모범 사례** | | | |
| 06 | 커뮤니티 기여 | MCP 생태계 기여 방법 | [가이드](./06-CommunityContributions/README.md) |
| 07 | 초기 도입기 인사이트 | 실무 구현 사례 | [가이드](./07-LessonsfromEarlyAdoption/README.md) |
| 08 | MCP 모범 사례 | 성능, 내결함성, 복원력 | [가이드](./08-BestPractices/README.md) |
| 09 | MCP 사례 연구 | 실무 구현 예제 | [가이드](./09-CaseStudy/README.md) |
| 10 | 실습 워크숍 | AI 툴킷으로 MCP 서버 구축 | [랩](./10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) |
| **모듈 11: MCP 서버 실습 랩** | | | |
| 11 | MCP 서버 데이터베이스 통합 | PostgreSQL 통합을 위한 13개 랩 완성 학습 경로 | [랩](./11-MCPServerHandsOnLabs/README.md) |
| 11.1 | 소개 | 데이터베이스 통합 및 소매 분석 사례 개요 | [랩 00](./11-MCPServerHandsOnLabs/00-Introduction/README.md) |
| 11.2 | 핵심 아키텍처 | MCP 서버 아키텍처, 데이터베이스 계층, 보안 패턴 이해 | [랩 01](./11-MCPServerHandsOnLabs/01-Architecture/README.md) |
| 11.3 | 보안 및 멀티 테넌시 | 행 수준 보안, 인증, 다중 테넌트 데이터 접근 | [랩 02](./11-MCPServerHandsOnLabs/02-Security/README.md) |
| 11.4 | 환경 설정 | 개발 환경 설정, Docker, Azure 리소스 | [랩 03](./11-MCPServerHandsOnLabs/03-Setup/README.md) |
| 11.5 | 데이터베이스 설계 | PostgreSQL 설정, 소매 스키마 설계 및 샘플 데이터 | [랩 04](./11-MCPServerHandsOnLabs/04-Database/README.md) |
| 11.6 | MCP 서버 구현 | 데이터베이스 통합 FastMCP 서버 구축 | [랩 05](./11-MCPServerHandsOnLabs/05-MCP-Server/README.md) |
| 11.7 | 도구 개발 | 데이터베이스 쿼리 도구 및 스키마 인트로스펙션 생성 | [랩 06](./11-MCPServerHandsOnLabs/06-Tools/README.md) |
| 11.8 | 시맨틱 검색 | Azure OpenAI와 pgvector를 이용한 벡터 임베딩 구현 | [랩 07](./11-MCPServerHandsOnLabs/07-Semantic-Search/README.md) |
| 11.9 | 테스트 및 디버깅 | 테스트 전략, 디버깅 도구, 검증 방법론 | [랩 08](./11-MCPServerHandsOnLabs/08-Testing/README.md) |
| 11.10 | VS Code 통합 | VS Code MCP 통합 및 AI 챗 사용법 구성 | [랩 09](./11-MCPServerHandsOnLabs/09-VS-Code/README.md) |
| 11.11 | 배포 전략 | Docker 배포, Azure 컨테이너 앱, 확장 고려사항 | [랩 10](./11-MCPServerHandsOnLabs/10-Deployment/README.md) |
| 11.12 | 모니터링 | 애플리케이션 인사이트, 로깅, 성능 모니터링 | [랩 11](./11-MCPServerHandsOnLabs/11-Monitoring/README.md) |
| 11.13 | 모범 사례 | 성능 최적화, 보안 강화, 프로덕션 팁 | [랩 12](./11-MCPServerHandsOnLabs/12-Best-Practices/README.md) |

### 💻 샘플 코드 프로젝트

MCP 학습에서 가장 흥미로운 부분 중 하나는 코드 스킬이 점진적으로 발전하는 모습을 보는 것입니다. 우리의 코드 예제는 쉽게 이해할 수 있으면서도 실제 MCP 원칙을 보여주도록 설계되었습니다. 이 코드를 통해 단순히 코드가 무엇을 하는지뿐 아니라 왜 그렇게 구조화되었는지, 그리고 더 큰 MCP 애플리케이션에서 어떻게 맞아떨어지는지 이해할 수 있을 것입니다.

#### 기본 MCP 계산기 샘플

| Language | Description | Link |
|----------|-------------|------|
| C# | MCP 서버 예제 | [코드 보기](./03-GettingStarted/samples/csharp/README.md) |
| Java | MCP 계산기 | [코드 보기](./03-GettingStarted/samples/java/calculator/README.md) |
| JavaScript | MCP 데모 | [코드 보기](./03-GettingStarted/samples/javascript/README.md) |
| Python | MCP 서버 | [코드 보기](../../03-GettingStarted/samples/python/mcp_calculator_server.py) |
| TypeScript | MCP 예제 | [코드 보기](./03-GettingStarted/samples/typescript/README.md) |
| Rust | MCP 예제 | [코드 보기](./03-GettingStarted/samples/rust/README.md) |

#### 고급 MCP 구현

| Language | Description | Link |
|----------|-------------|------|
| C# | 고급 샘플 | [코드 보기](./04-PracticalImplementation/samples/csharp/README.md) |
| Spring을 사용하는 Java | 컨테이너 앱 예제 | [코드 보기](./04-PracticalImplementation/samples/java/containerapp/README.md) |
| JavaScript | 고급 샘플 | [코드 보기](./04-PracticalImplementation/samples/javascript/README.md) |
| Python | 복잡한 구현 | [코드 보기](./04-PracticalImplementation/samples/python/README.md) |
| TypeScript | 컨테이너 샘플 | [코드 보기](./04-PracticalImplementation/samples/typescript/README.md) |


## 🎯 MCP 학습 필수 조건

이 커리큘럼을 최대한 활용하려면 다음이 필요합니다:
- 다음 언어 중 하나 이상에 대한 기본 프로그래밍 지식: C#, Java, JavaScript, Python, 또는 TypeScript
- 클라이언트-서버 모델 및 API에 대한 이해
- REST 및 HTTP 개념에 대한 친숙함
- (선택 사항) AI/ML 개념 배경

- 지원을 위한 커뮤니티 토론 참여

## 📚 학습 가이드 및 자료

이 저장소에는 효과적으로 탐색하고 학습할 수 있도록 여러 자료가 포함되어 있습니다:

### 학습 가이드

포괄적인 [학습 가이드](./study_guide.md)가 제공되어 이 저장소를 효과적으로 탐색할 수 있도록 돕습니다. 이 시각적 커리큘럼 지도는 모든 주제가 어떻게 연결되는지 보여주고 샘플 프로젝트를 효과적으로 사용하는 방법에 대한 지침을 제공합니다. 특히 큰 그림을 보는 것을 좋아하는 시각 학습자에게 유용합니다.

가이드에는 다음이 포함됩니다:
- 다루는 모든 주제를 보여주는 시각적 커리큘럼 지도
- 각 저장소 섹션의 상세 분해
- 샘플 프로젝트 사용 안내
- 다양한 기술 수준별 추천 학습 경로
- 학습 여정을 보완하는 추가 자료

### 변경 내역

우리는 교육 자료의 모든 주요 업데이트를 추적하는 상세한 [변경 내역](./changelog.md)을 유지하여 최신 개선 사항과 추가 사항을 확인할 수 있습니다.
- 새 콘텐츠 추가
- 구조 변경
- 기능 개선
- 문서 업데이트

## 🛠️ 이 커리큘럼을 효과적으로 사용하는 방법

이 가이드의 각 레슨에는 다음이 포함됩니다:

1. MCP 개념에 대한 명확한 설명  
2. 여러 언어로 된 실시간 코드 예제  
3. 실제 MCP 애플리케이션을 구축하는 연습 문제  
4. 고급 학습자를 위한 추가 자료

### C#으로 배우는 MCP - 튜토리얼 시리즈
모델 컨텍스트 프로토콜(MCP)은 AI 모델과 클라이언트 애플리케이션 간의 상호작용을 표준화하도록 설계된 최첨단 프레임워크입니다. 이 초보자 친화 세션을 통해 MCP를 소개하고 첫 번째 MCP 서버를 만드는 방법을 안내합니다.
#### C#: [https://aka.ms/letslearnmcp-csharp](https://aka.ms/letslearnmcp-csharp)
#### Java: [https://aka.ms/letslearnmcp-java](https://aka.ms/letslearnmcp-java)
#### JavaScript: [https://aka.ms/letslearnmcp-javascript](https://aka.ms/letslearnmcp-javascript)
#### Python: [https://aka.ms/letslearnmcp-python](https://aka.ms/letslearnmcp-python)

## 🎓 MCP 여정의 시작

축하합니다! 프로그래밍 능력을 확장하고 AI 개발의 최첨단과 연결되는 흥미진진한 여정의 첫 단계를 밟으셨습니다.

### 지금까지 이뤄낸 것

이 소개를 통해 이미 MCP 지식 기초를 쌓기 시작했습니다. MCP가 무엇인지, 왜 중요한지, 이 커리큘럼이 어떻게 학습 여정을 지원할지 이해했습니다. 이는 중요한 성취이며 이 중요한 기술에 대한 전문성의 시작입니다.

### 앞으로의 모험

모듈을 진행할수록 모든 전문가가 한때 초보자였음을 기억하세요. 지금은 복잡해 보이는 개념도 연습하고 적용하면서 자연스러워질 것입니다. 작은 발걸음 하나하나가 개발 경력 전체에서 도움이 될 강력한 능력으로 이어집니다.

### 당신의 지원 네트워크

MCP에 열정을 가진 학습자 및 전문가 커뮤니티에 합류하셨습니다. 코딩 문제에 막혔을 때나 성과를 공유하고 싶을 때, 커뮤니티가 여러분의 여정을 돕기 위해 있습니다.

AI 앱 구축에 관해 막히거나 질문이 있으면 MCP에 관한 토론에 참여하세요. 질문이 환영받고 지식이 자유롭게 공유되는 지원 커뮤니티입니다.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

제품 피드백이나 빌드 중 오류가 있을 경우 방문:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

### 시작할 준비 되셨나요?

지금 바로 MCP 모험을 시작하세요! Module 0부터 시작해 첫 실습 MCP 경험에 뛰어들거나 샘플 프로젝트를 탐험해 무엇을 빌드할지 확인하세요. 모든 전문가는 바로 지금 당신이 있는 곳에서 시작했으며, 인내와 연습으로 놀라운 성과를 이룰 수 있습니다.

모델 컨텍스트 프로토콜 개발의 세계에 오신 것을 환영합니다. 함께 놀라운 것을 만들어 봅시다!

## 🤝 학습 커뮤니티에 기여하기

이 커리큘럼은 여러분과 같은 학습자의 기여로 더욱 강해집니다! 오타를 수정하든, 더 명확한 설명을 제안하든, 새 예제를 추가하든, 여러분의 기여가 다른 초보자의 성공을 돕습니다.

Microsoft Valued Professional [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) 님께서 코드 샘플을 기여해 주셨습니다.

기여 과정은 환영하고 지원하는 방식으로 설계되었습니다. 대부분 기여에는 Contributor License Agreement(CLA)가 필요하지만 자동화 도구가 과정을 원활하게 안내합니다.

## 📜 오픈 소스 학습

이 모든 커리큘럼은 MIT [LICENSE](../../LICENSE) 하에 제공되어 자유롭게 사용, 수정, 공유할 수 있습니다. 이는 MCP 지식을 전 세계 개발자에게 접근 가능하게 하려는 우리의 사명을 지원합니다.
## 🤝 기여 지침

이 프로젝트는 기여 및 제안을 환영합니다. 대부분의 기여는 귀하가 기여를 사용할 권리가 있음을 선언하는 Contributor License Agreement(CLA)에 동의해야 합니다. 자세한 내용은 <https://cla.opensource.microsoft.com>을 참조하십시오.

풀 리퀘스트를 제출하면 CLA 봇이 자동으로 CLA 필요 여부를 판단하고 PR에 적절한 표시(예: 상태 검사, 댓글)를 추가합니다. 봇이 제공하는 지침을 따르면 됩니다. 모든 저장소에 걸쳐 이 작업은 한 번만 수행하면 됩니다.

이 프로젝트는 [Microsoft 오픈 소스 행동 강령](https://opensource.microsoft.com/codeofconduct/)을 채택했습니다. 자세한 내용은 [행동 강령 FAQ](https://opensource.microsoft.com/codeofconduct/faq/)나 [opencode@microsoft.com](mailto:opencode@microsoft.com)으로 문의하십시오.

---

*당신의 MCP 여정을 시작할 준비가 되셨나요? [Module 00 - MCP 소개](./00-Introduction/README.md)로 시작해 모델 컨텍스트 프로토콜 개발 세계에 첫 발을 내딛으세요!*



## 🎒 기타 코스
우리 팀은 다른 코스도 제작합니다! 확인해 보세요:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / 에이전트
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 생성 AI 시리즈
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 핵심 학습
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 코파일럿 시리즈
[![AI 페어 프로그래밍용 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET용 Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot 어드벤처](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 있을 수 있음을 양지해 주시기 바랍니다. 원문 문서는 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우에는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->