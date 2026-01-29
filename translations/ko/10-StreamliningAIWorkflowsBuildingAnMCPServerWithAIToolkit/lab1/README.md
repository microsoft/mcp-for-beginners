# 🚀 모듈 1: AI Toolkit 기초

[![Duration](https://img.shields.io/badge/Duration-15%20minutes-blue.svg)]()
[![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-green.svg)]()
[![Prerequisites](https://img.shields.io/badge/Prerequisites-VS%20Code-orange.svg)]()

## 📋 학습 목표

이 모듈을 마치면 다음을 할 수 있습니다:
- ✅ Visual Studio Code용 AI Toolkit 설치 및 설정
- ✅ 모델 카탈로그 탐색 및 다양한 모델 소스 이해
- ✅ Playground를 사용한 모델 테스트 및 실험
- ✅ Agent Builder를 이용한 맞춤형 AI 에이전트 생성
- ✅ 다양한 제공업체의 모델 성능 비교
- ✅ 프롬프트 엔지니어링 모범 사례 적용

## 🧠 AI Toolkit (AITK) 소개

**Visual Studio Code용 AI Toolkit**은 마이크로소프트의 대표 확장 기능으로, VS Code를 종합적인 AI 개발 환경으로 바꿔줍니다. AI 연구와 실제 애플리케이션 개발 간의 간극을 메우며, 모든 수준의 개발자가 생성형 AI를 쉽게 활용할 수 있도록 돕습니다.

### 🌟 주요 기능

| 기능 | 설명 | 활용 사례 |
|---------|-------------|----------|
| **🗂️ 모델 카탈로그** | GitHub, ONNX, OpenAI, Anthropic, Google 등 100개 이상의 모델 접근 | 모델 탐색 및 선택 |
| **🔌 BYOM 지원** | 자체 모델(로컬/원격) 통합 | 맞춤형 모델 배포 |
| **🎮 인터랙티브 플레이그라운드** | 채팅 인터페이스를 통한 실시간 모델 테스트 | 빠른 프로토타이핑 및 테스트 |
| **📎 멀티모달 지원** | 텍스트, 이미지, 첨부파일 처리 | 복합 AI 애플리케이션 |
| **⚡ 배치 처리** | 여러 프롬프트 동시 실행 | 효율적인 테스트 워크플로우 |
| **📊 모델 평가** | 내장 지표(F1, 관련성, 유사성, 일관성) | 성능 평가 |

### 🎯 AI Toolkit이 중요한 이유

- **🚀 개발 가속화**: 아이디어에서 프로토타입까지 몇 분 만에
- **🔄 통합 워크플로우**: 여러 AI 제공업체를 한 인터페이스에서
- **🧪 간편한 실험**: 복잡한 설정 없이 모델 비교 가능
- **📈 프로덕션 준비 완료**: 프로토타입에서 배포까지 원활한 전환

## 🛠️ 사전 준비 및 설정

### 📦 AI Toolkit 확장 설치

**1단계: 확장 마켓플레이스 접속**
1. Visual Studio Code 실행
2. 확장 뷰 열기 (`Ctrl+Shift+X` 또는 `Cmd+Shift+X`)
3. "AI Toolkit" 검색

**2단계: 버전 선택**
- **🟢 정식 버전**: 프로덕션 사용 권장
- **🔶 프리릴리스**: 최신 기능 조기 체험 가능

**3단계: 설치 및 활성화**

![AI Toolkit Extension](../../../../translated_images/ko/aitkext.d28945a03eed003c39fc39bc96ae655af9b64b9b922e78e88b07214420ed7985.png)

### ✅ 확인 체크리스트
- [ ] VS Code 사이드바에 AI Toolkit 아이콘 표시
- [ ] 확장 기능이 활성화되어 있음
- [ ] 출력 패널에 설치 오류 없음

## 🧪 실습 1: GitHub 모델 탐색

**🎯 목표**: 모델 카탈로그를 익히고 첫 AI 모델 테스트하기

### 📊 1단계: 모델 카탈로그 탐색

모델 카탈로그는 AI 생태계로 가는 관문입니다. 여러 제공업체의 모델을 한데 모아 쉽게 탐색하고 비교할 수 있습니다.

**🔍 탐색 가이드:**

AI Toolkit 사이드바에서 **MODELS - Catalog** 클릭

![Model Catalog](../../../../translated_images/ko/aimodel.263ed2be013d8fb0e2265c4f742cfe490f6f00eca5e132ec50438c8e826e34ed.png)

**💡 팁**: 코드 생성, 창의적 글쓰기, 분석 등 사용 사례에 맞는 특정 기능을 가진 모델을 찾아보세요.

**⚠️ 주의**: GitHub에 호스팅된 모델(GitHub Models)은 무료로 사용할 수 있지만 요청 및 토큰에 제한이 있습니다. Azure AI나 다른 엔드포인트를 통해 호스팅된 비-GitHub 모델에 접근하려면 적절한 API 키나 인증이 필요합니다.

### 🚀 2단계: 첫 모델 추가 및 설정

**모델 선택 전략:**
- **GPT-4.1**: 복잡한 추론과 분석에 최적
- **Phi-4-mini**: 가벼우며 간단한 작업에 빠른 응답 제공

**🔧 설정 절차:**
1. 카탈로그에서 **OpenAI GPT-4.1** 선택
2. **Add to My Models** 클릭하여 모델 등록
3. **Try in Playground** 선택해 테스트 환경 실행
4. 모델 초기화 대기 (첫 실행 시 시간이 걸릴 수 있음)

![Playground Setup](../../../../translated_images/ko/playground.dd6f5141344878ca4d4f3de819775da7b113518941accf37c291117c602f85db.png)

**⚙️ 모델 파라미터 이해하기:**
- **Temperature**: 창의성 조절 (0 = 결정적, 1 = 창의적)
- **Max Tokens**: 최대 응답 길이
- **Top-p**: 응답 다양성을 위한 핵심 샘플링

### 🎯 3단계: 플레이그라운드 인터페이스 마스터하기

플레이그라운드는 AI 실험실입니다. 최대한 활용하는 방법은 다음과 같습니다:

**🎨 프롬프트 엔지니어링 모범 사례:**
1. **구체적으로 작성**: 명확하고 자세한 지시가 더 좋은 결과를 만듭니다
2. **맥락 제공**: 관련 배경 정보를 포함하세요
3. **예시 사용**: 원하는 바를 예시로 보여주세요
4. **반복 개선**: 초기 결과를 바탕으로 프롬프트를 다듬으세요

**🧪 테스트 시나리오:**
```markdown
# Example 1: Code Generation
"Write a Python function that calculates the factorial of a number using recursion. Include error handling and docstrings."

# Example 2: Creative Writing
"Write a professional email to a client explaining a project delay, maintaining a positive tone while being transparent about challenges."

# Example 3: Data Analysis
"Analyze this sales data and provide insights: [paste your data]. Focus on trends, anomalies, and actionable recommendations."
```

![Testing Results](../../../../translated_images/ko/result.1dfcf211fb359cf65902b09db191d3bfc65713ca15e279c1a30be213bb526949.png)

### 🏆 도전 과제: 모델 성능 비교

**🎯 목표**: 동일한 프롬프트로 여러 모델을 비교해 강점을 파악하기

**📋 지침:**
1. 작업 공간에 **Phi-4-mini** 추가
2. GPT-4.1과 Phi-4-mini에 동일한 프롬프트 사용

![set](../../../../translated_images/ko/set.88132df189ecde2cbbda256c1841db5aac8e9bdeba1a4e343dfa031b9545d6c9.png)

3. 응답 품질, 속도, 정확도 비교
4. 결과 섹션에 발견 내용 기록

![Model Comparison](../../../../translated_images/ko/compare.97746cd0f907495503c1fc217739f3890dc76ea5f6fd92379a6db0cc331feb58.png)

**💡 알아야 할 핵심 인사이트:**
- LLM과 SLM 사용 시기
- 비용과 성능 간 균형
- 모델별 특화 기능

## 🤖 실습 2: Agent Builder로 맞춤형 에이전트 만들기

**🎯 목표**: 특정 작업과 워크플로우에 맞춘 전문 AI 에이전트 생성

### 🏗️ 1단계: Agent Builder 이해하기

Agent Builder는 AI Toolkit의 핵심 기능입니다. 대형 언어 모델의 힘을 맞춤형 지시, 특정 파라미터, 전문 지식과 결합해 목적에 맞는 AI 비서를 만들 수 있습니다.

**🧠 에이전트 아키텍처 구성요소:**
- **Core Model**: 기본 LLM (GPT-4, Groks, Phi 등)
- **System Prompt**: 에이전트 성격과 행동 정의
- **Parameters**: 최적 성능을 위한 세부 설정
- **Tools Integration**: 외부 API 및 MCP 서비스 연결
- **Memory**: 대화 맥락과 세션 유지

![Agent Builder Interface](../../../../translated_images/ko/agentbuilder.25895b2d2f8c02e7aa99dd40e105877a6f1db8f0441180087e39db67744b361f.png)

### ⚙️ 2단계: 에이전트 설정 심화

**🎨 효과적인 시스템 프롬프트 작성:**
```markdown
# Template Structure:
## Role Definition
You are a [specific role] with expertise in [domain].

## Capabilities
- List specific abilities
- Define scope of knowledge
- Clarify limitations

## Behavior Guidelines
- Response style (formal, casual, technical)
- Output format preferences
- Error handling approach

## Examples
Provide 2-3 examples of ideal interactions
```

*물론 Generate System Prompt 기능을 사용해 AI가 프롬프트 생성과 최적화를 도와줄 수도 있습니다*

**🔧 파라미터 최적화:**
| 파라미터 | 권장 범위 | 활용 사례 |
|-----------|------------------|----------|
| **Temperature** | 0.1-0.3 | 기술적/사실적 응답 |
| **Temperature** | 0.7-0.9 | 창의적/브레인스토밍 작업 |
| **Max Tokens** | 500-1000 | 간결한 응답 |
| **Max Tokens** | 2000-4000 | 상세한 설명 |

### 🐍 3단계: 실습 - 파이썬 프로그래밍 에이전트

**🎯 미션**: 전문적인 파이썬 코딩 어시스턴트 만들기

**📋 설정 단계:**

1. **모델 선택**: **Claude 3.5 Sonnet** 선택 (코드 작업에 탁월)

2. **시스템 프롬프트 설계**:
```markdown
# Python Programming Expert Agent

## Role
You are a senior Python developer with 10+ years of experience. You excel at writing clean, efficient, and well-documented Python code.

## Capabilities
- Write production-ready Python code
- Debug complex issues
- Explain code concepts clearly
- Suggest best practices and optimizations
- Provide complete working examples

## Response Format
- Always include docstrings
- Add inline comments for complex logic
- Suggest testing approaches
- Mention relevant libraries when applicable

## Code Quality Standards
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Handle exceptions gracefully
- Write readable, maintainable code
```

3. **파라미터 설정**:
   - Temperature: 0.2 (일관되고 신뢰할 수 있는 코드)
   - Max Tokens: 2000 (상세한 설명)
   - Top-p: 0.9 (균형 잡힌 창의성)

![Python Agent Configuration](../../../../translated_images/ko/pythonagent.5e51b406401c165fcabfd66f2d943c27f46b5fed0f9fb73abefc9e91ca3489d4.png)

### 🧪 4단계: 파이썬 에이전트 테스트

**테스트 시나리오:**
1. **기본 기능**: "소수 찾기 함수 작성"
2. **복잡한 알고리즘**: "삽입, 삭제, 검색 메서드를 포함한 이진 탐색 트리 구현"
3. **실제 문제**: "요청 제한과 재시도를 처리하는 웹 스크래퍼 만들기"
4. **디버깅**: "이 코드를 수정해 주세요 [버그 있는 코드 붙여넣기]"

**🏆 성공 기준:**
- ✅ 오류 없이 코드 실행
- ✅ 적절한 문서화 포함
- ✅ 파이썬 모범 사례 준수
- ✅ 명확한 설명 제공
- ✅ 개선 사항 제안

## 🎓 모듈 1 정리 및 다음 단계

### 📊 지식 점검

이해도를 확인해 보세요:
- [ ] 카탈로그 내 모델 간 차이를 설명할 수 있나요?
- [ ] 맞춤형 에이전트를 성공적으로 생성하고 테스트했나요?
- [ ] 다양한 사용 사례에 맞게 파라미터를 최적화할 수 있나요?
- [ ] 효과적인 시스템 프롬프트를 설계할 수 있나요?

### 📚 추가 자료

- **AI Toolkit 문서**: [공식 Microsoft Docs](https://github.com/microsoft/vscode-ai-toolkit)
- **프롬프트 엔지니어링 가이드**: [모범 사례](https://platform.openai.com/docs/guides/prompt-engineering)
- **AI Toolkit 내 모델**: [개발 중인 모델](https://github.com/microsoft/vscode-ai-toolkit/blob/main/doc/models.md)

**🎉 축하합니다!** AI Toolkit의 기본기를 마스터했으며, 더 고급 AI 애플리케이션을 만들 준비가 되었습니다!

### 🔜 다음 모듈로 계속하기

더 고급 기능을 배우고 싶다면 **[모듈 2: MCP with AI Toolkit Fundamentals](../lab2/README.md)** 로 이동하세요. 여기서 다음을 배우게 됩니다:
- Model Context Protocol (MCP)을 사용해 에이전트를 외부 도구에 연결하는 방법
- Playwright로 브라우저 자동화 에이전트 구축
- AI Toolkit 에이전트와 MCP 서버 통합
- 외부 데이터와 기능으로 에이전트 강화하기

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.