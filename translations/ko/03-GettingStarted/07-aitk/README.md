<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6fb74f952ab79ed4b4a33fda5fa04ecb",
  "translation_date": "2025-07-31T01:16:19+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "ko"
}
-->
# Visual Studio Code의 AI Toolkit 확장에서 서버 활용하기

AI 에이전트를 구축할 때, 단순히 스마트한 응답을 생성하는 것만이 전부가 아닙니다. 에이전트가 실제로 행동을 취할 수 있는 능력을 부여하는 것도 중요합니다. 여기서 **Model Context Protocol (MCP)**이 등장합니다. MCP는 에이전트가 외부 도구와 서비스를 일관된 방식으로 쉽게 접근할 수 있도록 해줍니다. 마치 에이전트를 실제로 사용할 수 있는 도구 상자에 연결하는 것과 같습니다.

예를 들어, 에이전트를 계산기 MCP 서버에 연결한다고 가정해봅시다. 그러면 에이전트는 "47 곱하기 89는 얼마야?"와 같은 프롬프트를 받는 것만으로 수학 연산을 수행할 수 있습니다. 로직을 하드코딩하거나 커스텀 API를 구축할 필요가 없습니다.

## 개요

이 강의에서는 Visual Studio Code의 [AI Toolkit](https://aka.ms/AIToolkit) 확장을 사용하여 계산기 MCP 서버를 에이전트에 연결하는 방법을 다룹니다. 이를 통해 에이전트가 덧셈, 뺄셈, 곱셈, 나눗셈과 같은 수학 연산을 자연어로 수행할 수 있게 됩니다.

AI Toolkit은 Visual Studio Code에서 에이전트 개발을 간소화하는 강력한 확장 프로그램입니다. AI 엔지니어는 이 도구를 사용하여 생성형 AI 모델을 로컬 또는 클라우드에서 개발하고 테스트할 수 있습니다. 이 확장은 현재 사용 가능한 주요 생성형 모델 대부분을 지원합니다.

*참고*: AI Toolkit은 현재 Python과 TypeScript를 지원합니다.

## 학습 목표

이 강의를 마치면 다음을 수행할 수 있습니다:

- AI Toolkit을 통해 MCP 서버를 활용하기
- MCP 서버가 제공하는 도구를 발견하고 사용할 수 있도록 에이전트 설정 구성하기
- 자연어를 통해 MCP 도구 활용하기

## 접근 방식

다음은 고수준에서의 접근 방식입니다:

- 에이전트를 생성하고 시스템 프롬프트를 정의합니다.
- 계산기 도구를 포함한 MCP 서버를 생성합니다.
- Agent Builder를 MCP 서버에 연결합니다.
- 자연어를 통해 에이전트의 도구 호출을 테스트합니다.

좋습니다. 이제 흐름을 이해했으니, MCP를 통해 외부 도구를 활용하여 에이전트의 기능을 확장해봅시다!

## 사전 준비

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code용 AI Toolkit](https://aka.ms/AIToolkit)

## 실습: 서버 활용하기

> [!WARNING]
> **macOS 사용자 주의**. 현재 macOS에서 종속성 설치에 영향을 미치는 문제를 조사 중입니다. 이로 인해 macOS 사용자는 현재 이 튜토리얼을 완료할 수 없습니다. 문제가 해결되는 대로 지침을 업데이트하겠습니다. 기다려주셔서 감사합니다!

이 실습에서는 Visual Studio Code의 AI Toolkit을 사용하여 MCP 서버의 도구를 활용하는 AI 에이전트를 구축, 실행 및 개선합니다.

### -0- 사전 단계: OpenAI GPT-4o 모델을 My Models에 추가하기

이 실습에서는 **GPT-4o** 모델을 사용합니다. 에이전트를 생성하기 전에 이 모델을 **My Models**에 추가해야 합니다.

![Visual Studio Code의 AI Toolkit 확장에서 모델 선택 인터페이스 스크린샷. 제목은 "Find the right model for your AI Solution"이며, 부제목은 사용자가 AI 모델을 발견, 테스트, 배포하도록 권장합니다. 아래에는 "Popular Models" 섹션에 여섯 개의 모델 카드가 표시됩니다: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), DeepSeek-R1 (Ollama-hosted). 각 카드에는 "Add" 또는 "Try in Playground" 옵션이 포함되어 있습니다.](../../../../translated_images/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.ko.png)

1. **Activity Bar**에서 **AI Toolkit** 확장을 엽니다.
1. **Catalog** 섹션에서 **Models**를 선택하여 **Model Catalog**를 엽니다. **Models**를 선택하면 **Model Catalog**가 새 편집기 탭에서 열립니다.
1. **Model Catalog** 검색창에 **OpenAI GPT-4o**를 입력합니다.
1. **+ Add**를 클릭하여 모델을 **My Models** 목록에 추가합니다. **GitHub에서 호스팅된** 모델을 선택했는지 확인하세요.
1. **Activity Bar**에서 **OpenAI GPT-4o** 모델이 목록에 나타나는지 확인합니다.

### -1- 에이전트 생성하기

**Agent (Prompt) Builder**를 사용하면 AI 기반 에이전트를 생성하고 사용자 정의할 수 있습니다. 이 섹션에서는 새 에이전트를 생성하고 대화를 구동할 모델을 할당합니다.

![Visual Studio Code의 AI Toolkit 확장에서 "Calculator Agent" 빌더 인터페이스 스크린샷. 왼쪽 패널에서 선택된 모델은 "OpenAI GPT-4o (via GitHub)"입니다. 시스템 프롬프트는 "You are a professor in university teaching math"이며, 사용자 프롬프트는 "Explain to me the Fourier equation in simple terms"입니다. 추가 옵션으로 도구 추가, MCP 서버 활성화, 구조화된 출력 선택 버튼이 포함되어 있습니다. 하단에는 파란색 "Run" 버튼이 있습니다. 오른쪽 패널에는 "Get Started with Examples" 아래에 세 가지 샘플 에이전트가 나열되어 있습니다: Web Developer (with MCP Server, Second-Grade Simplifier, Dream Interpreter). 각 에이전트의 기능에 대한 간략한 설명이 포함되어 있습니다.](../../../../translated_images/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.ko.png)

1. **Activity Bar**에서 **AI Toolkit** 확장을 엽니다.
1. **Tools** 섹션에서 **Agent (Prompt) Builder**를 선택합니다. **Agent (Prompt) Builder**를 선택하면 새 편집기 탭에서 열립니다.
1. **+ New Agent** 버튼을 클릭합니다. 확장은 **Command Palette**를 통해 설정 마법사를 실행합니다.
1. 이름으로 **Calculator Agent**를 입력하고 **Enter**를 누릅니다.
1. **Agent (Prompt) Builder**에서 **Model** 필드에 **OpenAI GPT-4o (via GitHub)** 모델을 선택합니다.

### -2- 에이전트의 시스템 프롬프트 생성하기

에이전트의 기본 구조를 생성한 후, 이제 에이전트의 성격과 목적을 정의할 차례입니다. 이 섹션에서는 **Generate system prompt** 기능을 사용하여 계산기 에이전트의 의도된 동작을 설명하고, 모델이 시스템 프롬프트를 작성하도록 합니다.

![Visual Studio Code의 AI Toolkit에서 "Calculator Agent" 인터페이스 스크린샷. "Generate a prompt"라는 제목의 모달 창이 열려 있습니다. 모달은 기본 세부 정보를 공유하여 프롬프트 템플릿을 생성할 수 있다고 설명하며, 샘플 시스템 프롬프트가 포함된 텍스트 상자를 보여줍니다: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." 텍스트 상자 아래에는 "Close"와 "Generate" 버튼이 있습니다. 배경에는 에이전트 구성의 일부가 보이며, 선택된 모델 "OpenAI GPT-4o (via GitHub)"와 시스템 및 사용자 프롬프트 필드가 포함되어 있습니다.](../../../../translated_images/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.ko.png)

1. **Prompts** 섹션에서 **Generate system prompt** 버튼을 클릭합니다. 이 버튼은 에이전트의 시스템 프롬프트를 생성하기 위해 AI를 활용하는 프롬프트 빌더를 엽니다.
1. **Generate a prompt** 창에서 다음을 입력합니다: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. **Generate** 버튼을 클릭합니다. 오른쪽 하단에 시스템 프롬프트가 생성 중임을 알리는 알림이 표시됩니다. 프롬프트 생성이 완료되면 **Agent (Prompt) Builder**의 **System prompt** 필드에 프롬프트가 나타납니다.
1. **System prompt**를 검토하고 필요하면 수정합니다.

### -3- MCP 서버 생성하기

에이전트의 시스템 프롬프트를 정의하여 동작과 응답을 안내한 후, 이제 에이전트에 실질적인 기능을 추가할 차례입니다. 이 섹션에서는 덧셈, 뺄셈, 곱셈, 나눗셈 계산을 실행할 수 있는 도구를 포함한 계산기 MCP 서버를 생성합니다. 이 서버는 에이전트가 자연어 프롬프트에 따라 실시간으로 수학 연산을 수행할 수 있도록 합니다.

![Visual Studio Code의 AI Toolkit 확장에서 "Calculator Agent" 인터페이스 하단 섹션 스크린샷. "Tools"와 "Structure output" 확장 가능한 메뉴와 함께 "Choose output format"이라는 드롭다운 메뉴가 표시됩니다. 드롭다운 메뉴는 "text"로 설정되어 있습니다. 오른쪽에는 Model Context Protocol 서버를 추가하기 위한 "+ MCP Server" 버튼이 있습니다. Tools 섹션 위에는 이미지 아이콘 플레이스홀더가 표시됩니다.](../../../../translated_images/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.ko.png)

AI Toolkit은 자체 MCP 서버를 쉽게 생성할 수 있도록 템플릿을 제공합니다. 우리는 계산기 MCP 서버를 생성하기 위해 Python 템플릿을 사용할 것입니다.

*참고*: AI Toolkit은 현재 Python과 TypeScript를 지원합니다.

1. **Agent (Prompt) Builder**의 **Tools** 섹션에서 **+ MCP Server** 버튼을 클릭합니다. 확장은 **Command Palette**를 통해 설정 마법사를 실행합니다.
1. **+ Add Server**를 선택합니다.
1. **Create a New MCP Server**를 선택합니다.
1. 템플릿으로 **python-weather**를 선택합니다.
1. MCP 서버 템플릿을 저장할 **Default folder**를 선택합니다.
1. 서버 이름으로 **Calculator**를 입력합니다.
1. 새 Visual Studio Code 창이 열립니다. **Yes, I trust the authors**를 선택합니다.
1. **Terminal** 메뉴에서 **New Terminal**을 선택하여 터미널을 엽니다. 가상 환경을 생성합니다: `python -m venv .venv`
1. 터미널에서 가상 환경을 활성화합니다:
    - Windows: `.venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
1. 터미널에서 종속성을 설치합니다: `pip install -e .[dev]`
1. **Activity Bar**의 **Explorer** 보기에서 **src** 디렉토리를 확장하고 **server.py**를 선택하여 파일을 편집기에서 엽니다.
1. **server.py** 파일의 코드를 다음으로 교체하고 저장합니다:

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- 계산기 MCP 서버와 함께 에이전트 실행하기

이제 에이전트에 도구가 추가되었으니, 이를 사용할 차례입니다! 이 섹션에서는 에이전트에 프롬프트를 제출하여 계산기 MCP 서버의 적절한 도구를 활용하는지 테스트하고 검증합니다.

![Visual Studio Code의 AI Toolkit 확장에서 "Calculator Agent" 인터페이스 스크린샷. 왼쪽 패널에서 "Tools" 아래에 local-server-calculator_server라는 MCP 서버가 추가되어 있으며, 네 가지 사용 가능한 도구(add, subtract, multiply, divide)가 표시됩니다. 배지에는 네 가지 도구가 활성화되었음을 나타냅니다. 아래에는 접힌 "Structure output" 섹션과 파란색 "Run" 버튼이 있습니다. 오른쪽 패널에서 "Model Response" 아래에 에이전트가 multiply와 subtract 도구를 호출하며, 각각 {"a": 3, "b": 25}와 {"a": 75, "b": 20} 입력값을 사용합니다. 최종 "Tool Response"는 75.0으로 표시됩니다. 하단에는 "View Code" 버튼이 있습니다.](../../../../translated_images/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.ko.png)

계산기 MCP 서버를 로컬 개발 환경에서 실행하고 **Agent Builder**를 MCP 클라이언트로 사용합니다.

1. `F5`를 눌러 MCP 서버 디버깅을 시작합니다. **Agent (Prompt) Builder**가 새 편집기 탭에서 열립니다. 서버 상태는 터미널에서 확인할 수 있습니다.
1. **Agent (Prompt) Builder**의 **User prompt** 필드에 다음 프롬프트를 입력합니다: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. **Run** 버튼을 클릭하여 에이전트의 응답을 생성합니다.
1. 에이전트 출력을 검토합니다. 모델은 **$55**를 지불했다고 결론을 내려야 합니다.
1. 다음은 발생해야 할 일의 요약입니다:
    - 에이전트가 계산을 돕기 위해 **multiply**와 **subtract** 도구를 선택합니다.
    - **multiply** 도구에 대해 각각 `a`와 `b` 값이 할당됩니다.
    - **subtract** 도구에 대해 각각 `a`와 `b` 값이 할당됩니다.
    - 각 도구의 응답은 각각 **Tool Response**로 제공됩니다.
    - 모델의 최종 출력은 **Model Response**로 제공됩니다.
1. 추가 프롬프트를 제출하여 에이전트를 더 테스트합니다. **User prompt** 필드에서 기존 프롬프트를 클릭하여 수정할 수 있습니다.
1. 테스트가 끝나면 **터미널**에서 **CTRL/CMD+C**를 입력하여 서버를 종료합니다.

## 과제

**server.py** 파일에 추가 도구 항목(예: 숫자의 제곱근 반환)을 추가해보세요. 에이전트가 새 도구(또는 기존 도구)를 활용해야 하는 추가 프롬프트를 제출하세요. 새 도구를 로드하려면 서버를 다시 시작해야 합니다.

## 솔루션

[솔루션](./solution/README.md)

## 주요 요점

이 장의 주요 요점은 다음과 같습니다:

- AI Toolkit 확장은 MCP 서버와 그 도구를 활용할 수 있는 훌륭한 클라이언트입니다.
- MCP 서버에 새 도구를 추가하여 에이전트의 기능을 확장하고 변화하는 요구 사항을 충족할 수 있습니다.
- AI Toolkit은 커스텀 도구 생성을 간소화하기 위해 템플릿(예: Python MCP 서버 템플릿)을 제공합니다.

## 추가 자료

- [AI Toolkit 문서](https://aka.ms/AIToolkit/doc)

## 다음 단계
- 다음: [테스트 및 디버깅](../08-testing/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.