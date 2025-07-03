<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d1980763f2a545ca6648363bf5757b5a",
  "translation_date": "2025-06-12T22:27:34+00:00",
  "source_file": "03-GettingStarted/07-aitk/README.md",
  "language_code": "ko"
}
-->
# Visual Studio Code용 AI Toolkit 확장 프로그램에서 서버 사용하기

AI 에이전트를 만들 때, 단순히 똑똑한 답변을 생성하는 것뿐만 아니라 에이전트가 실제로 행동할 수 있는 능력을 부여하는 것도 중요합니다. 여기서 Model Context Protocol(MCP)이 역할을 합니다. MCP는 에이전트가 외부 도구와 서비스를 일관된 방식으로 쉽게 접근할 수 있도록 해줍니다. 마치 에이전트를 실제로 쓸 수 있는 도구 상자에 연결하는 것과 같습니다.

예를 들어, 에이전트를 계산기 MCP 서버에 연결하면 “47 곱하기 89는 얼마야?” 같은 프롬프트만 받아도 수학 연산을 수행할 수 있습니다. 별도로 로직을 하드코딩하거나 API를 직접 만들 필요가 없습니다.

## 개요

이 강의에서는 Visual Studio Code의 [AI Toolkit](https://aka.ms/AIToolkit) 확장 프로그램을 사용해 계산기 MCP 서버를 에이전트에 연결하는 방법을 다룹니다. 이를 통해 덧셈, 뺄셈, 곱셈, 나눗셈 같은 수학 연산을 자연어로 수행할 수 있게 됩니다.

AI Toolkit은 Visual Studio Code용 강력한 확장 프로그램으로, 에이전트 개발을 간소화합니다. AI 엔지니어는 생성형 AI 모델을 로컬이나 클라우드에서 쉽게 개발하고 테스트하여 AI 애플리케이션을 만들 수 있습니다. 현재 대부분의 주요 생성형 모델을 지원합니다.

*참고*: AI Toolkit은 현재 Python과 TypeScript를 지원합니다.

## 학습 목표

이 강의를 마치면 다음을 할 수 있습니다:

- AI Toolkit을 통해 MCP 서버를 사용하는 방법
- 에이전트 구성을 설정해 MCP 서버가 제공하는 도구를 발견하고 활용할 수 있도록 하기
- 자연어를 통해 MCP 도구를 활용하기

## 접근 방법

전체적인 접근 방식은 다음과 같습니다:

- 에이전트를 만들고 시스템 프롬프트를 정의하기
- 계산기 도구가 포함된 MCP 서버 생성하기
- Agent Builder를 MCP 서버에 연결하기
- 자연어로 에이전트의 도구 호출 테스트하기

이제 흐름을 이해했으니, MCP를 통해 외부 도구를 활용하는 AI 에이전트를 설정해 기능을 확장해봅시다!

## 사전 준비물

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code용 AI Toolkit](https://aka.ms/AIToolkit)

## 실습: 서버 사용하기

이번 실습에서는 Visual Studio Code 내 AI Toolkit을 사용해 MCP 서버의 도구를 가진 AI 에이전트를 만들고 실행하며 개선해봅니다.

### -0- 사전 단계: My Models에 OpenAI GPT-4o 모델 추가하기

이번 실습에서는 **GPT-4o** 모델을 사용합니다. 에이전트를 만들기 전에 **My Models**에 해당 모델을 추가해야 합니다.

![Visual Studio Code AI Toolkit 확장의 모델 선택 화면. "Find the right model for your AI Solution"라는 제목과 AI 모델을 발견, 테스트, 배포하라는 부제목이 보입니다. 인기 모델 목록에는 DeepSeek-R1 (GitHub 호스팅), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - 소형, 빠름), DeepSeek-R1 (Ollama 호스팅) 등이 카드 형태로 나열되어 있습니다. 각 카드에는 모델 추가 버튼과 플레이그라운드에서 테스트 버튼이 있습니다.](../../../../translated_images/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.ko.png)

1. **Activity Bar**에서 **AI Toolkit** 확장을 엽니다.
2. **Catalog** 섹션에서 **Models**를 선택해 **Model Catalog**를 엽니다. Models를 선택하면 새 편집기 탭에서 Model Catalog가 열립니다.
3. Model Catalog 검색창에 **OpenAI GPT-4o**를 입력합니다.
4. **+ Add**를 클릭해 모델을 **My Models** 목록에 추가합니다. 반드시 **GitHub에서 호스팅되는** 모델을 선택했는지 확인하세요.
5. Activity Bar에서 **OpenAI GPT-4o** 모델이 목록에 나타나는지 확인합니다.

### -1- 에이전트 생성하기

**Agent (Prompt) Builder**를 사용하면 자신만의 AI 에이전트를 만들고 맞춤화할 수 있습니다. 이 단계에서는 새 에이전트를 만들고 대화를 담당할 모델을 지정합니다.

![Visual Studio Code AI Toolkit 확장의 "Calculator Agent" 빌더 화면. 왼쪽 패널에 "OpenAI GPT-4o (via GitHub)" 모델이 선택되어 있습니다. 시스템 프롬프트에는 "You are a professor in university teaching math"라고 적혀 있고, 사용자 프롬프트에는 "Explain to me the Fourier equation in simple terms."라고 되어 있습니다. 도구 추가, MCP 서버 활성화, 구조화된 출력 선택 버튼이 보이며, 아래쪽에 파란색 "Run" 버튼이 있습니다. 오른쪽 패널에는 예제 시작하기 섹션에 Web Developer (MCP Server 포함), Second-Grade Simplifier, Dream Interpreter 같은 샘플 에이전트가 나열되어 있습니다.](../../../../translated_images/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.ko.png)

1. **Activity Bar**에서 **AI Toolkit** 확장을 엽니다.
2. **Tools** 섹션에서 **Agent (Prompt) Builder**를 선택합니다. 선택하면 새 편집기 탭에서 Agent (Prompt) Builder가 열립니다.
3. **+ New Agent** 버튼을 클릭합니다. 그러면 **Command Palette**를 통해 설정 마법사가 시작됩니다.
4. 이름을 **Calculator Agent**로 입력하고 **Enter**를 누릅니다.
5. Agent (Prompt) Builder에서 **Model** 필드에 **OpenAI GPT-4o (via GitHub)** 모델을 선택합니다.

### -2- 에이전트용 시스템 프롬프트 생성하기

에이전트 기본 틀이 준비되었으니, 이제 에이전트의 성격과 목적을 정의할 차례입니다. 이 단계에서는 **Generate system prompt** 기능을 사용해 계산기 에이전트로서의 행동 방침을 모델에게 작성하도록 합니다.

![Visual Studio Code AI Toolkit의 "Calculator Agent" 화면. "Generate a prompt"라는 제목의 모달 창이 열려 있습니다. 모달은 기본 정보를 입력하면 프롬프트 템플릿을 생성할 수 있다고 설명하며, "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result."라는 예시 시스템 프롬프트가 텍스트 박스에 있습니다. 아래에 "Close"와 "Generate" 버튼이 있습니다. 배경에는 선택된 모델 "OpenAI GPT-4o (via GitHub)"와 시스템 및 사용자 프롬프트 필드 일부가 보입니다.](../../../../translated_images/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.ko.png)

1. **Prompts** 섹션에서 **Generate system prompt** 버튼을 클릭합니다. 이 버튼을 누르면 AI를 활용해 시스템 프롬프트를 생성하는 프롬프트 빌더가 열립니다.
2. **Generate a prompt** 창에 다음 내용을 입력합니다: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
3. **Generate** 버튼을 클릭합니다. 오른쪽 아래에 시스템 프롬프트 생성 중이라는 알림이 나타납니다. 생성이 완료되면 프롬프트가 **Agent (Prompt) Builder**의 **System prompt** 필드에 표시됩니다.
4. 생성된 **System prompt**를 검토하고 필요하면 수정합니다.

### -3- MCP 서버 생성하기

에이전트의 시스템 프롬프트를 정의해 행동과 응답을 안내했으니, 이제 실질적인 기능을 추가할 차례입니다. 이번 섹션에서는 덧셈, 뺄셈, 곱셈, 나눗셈 연산을 수행할 수 있는 계산기 MCP 서버를 만듭니다. 이 서버 덕분에 에이전트는 자연어 프롬프트에 실시간으로 수학 연산을 수행할 수 있습니다.

![Visual Studio Code AI Toolkit 확장의 Calculator Agent 하단 화면. "Tools"와 "Structure output" 확장 가능한 메뉴가 보이고, "Choose output format" 드롭다운은 "text"로 설정되어 있습니다. 오른쪽에 "+ MCP Server" 버튼이 있어 Model Context Protocol 서버를 추가할 수 있습니다. 도구 섹션 위에는 이미지 아이콘 자리 표시자가 있습니다.](../../../../translated_images/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.ko.png)

AI Toolkit은 MCP 서버 생성을 쉽게 해주는 템플릿을 제공합니다. 이번에는 Python 템플릿을 사용해 계산기 MCP 서버를 만듭니다.

*참고*: AI Toolkit은 현재 Python과 TypeScript를 지원합니다.

1. **Agent (Prompt) Builder**의 **Tools** 섹션에서 **+ MCP Server** 버튼을 클릭합니다. 그러면 **Command Palette**를 통해 설정 마법사가 시작됩니다.
2. **+ Add Server**를 선택합니다.
3. **Create a New MCP Server**를 선택합니다.
4. 템플릿으로 **python-weather**를 선택합니다.
5. MCP 서버 템플릿을 저장할 **Default folder**를 선택합니다.
6. 서버 이름으로 **Calculator**를 입력합니다.
7. 새 Visual Studio Code 창이 열리면 **Yes, I trust the authors**를 선택합니다.
8. 터미널에서 가상 환경을 생성합니다: `python -m venv .venv`
9. 터미널에서 가상 환경을 활성화합니다:
    1. Windows - `.venv\Scripts\activate`
    2. macOS/Linux - `source venv/bin/activate`
10. 터미널에서 의존성을 설치합니다: `pip install -e .[dev]`
11. **Activity Bar**의 **Explorer** 뷰에서 **src** 디렉터리를 확장하고 **server.py** 파일을 선택해 엽니다.
12. **server.py** 파일의 코드를 다음 내용으로 교체하고 저장합니다:

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

이제 에이전트에 도구가 생겼으니 실제로 사용해봅시다! 이번 섹션에서는 프롬프트를 에이전트에 제출해 계산기 MCP 서버의 적절한 도구를 잘 활용하는지 테스트하고 검증합니다.

![Visual Studio Code AI Toolkit 확장의 Calculator Agent 화면. 왼쪽 패널의 "Tools" 아래에 local-server-calculator_server라는 MCP 서버가 추가되어 있으며, add, subtract, multiply, divide 네 가지 도구가 활성화되어 있습니다. 도구 개수 배지가 4개 활성 상태를 표시합니다. 그 아래에는 접힌 "Structure output" 섹션과 파란색 "Run" 버튼이 있습니다. 오른쪽 패널의 "Model Response"에는 에이전트가 multiply와 subtract 도구를 각각 {"a": 3, "b": 25}와 {"a": 75, "b": 20} 입력값으로 호출한 기록이 보입니다. 최종 "Tool Response"는 75.0이며, 하단에 "View Code" 버튼이 있습니다.](../../../../translated_images/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.ko.png)

계산기 MCP 서버를 로컬 개발 머신에서 **Agent Builder**를 MCP 클라이언트로 실행합니다.

1. `F5` to start debugging the MCP server. The **Agent (Prompt) Builder** will open in a new editor tab. The status of the server is visible in the terminal.
1. In the **User prompt** field of the **Agent (Prompt) Builder**, enter the following prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Click the **Run** button to generate the agent's response.
1. Review the agent output. The model should conclude that you paid **$55**.
1. Here's a breakdown of what should occur:
    - The agent selects the **multiply** and **substract** tools to aid in the calculation.
    - The respective `a` and `b` values are assigned for the **multiply** tool.
    - The respective `a` and `b` 값이 **subtract** 도구에 할당됩니다.
    - 각 도구의 응답은 해당 **Tool Response**에 표시됩니다.
    - 모델의 최종 출력은 **Model Response**에 표시됩니다.
2. 추가 프롬프트를 제출해 에이전트를 더 테스트할 수 있습니다. **User prompt** 필드에 클릭 후 기존 프롬프트를 수정하면 됩니다.
3. 테스트가 끝나면 터미널에서 **CTRL/CMD+C**를 눌러 서버를 종료할 수 있습니다.

## 과제

**server.py** 파일에 새로운 도구 항목을 추가해보세요 (예: 숫자의 제곱근을 반환하는 도구). 새 도구(또는 기존 도구)를 활용하는 추가 프롬프트를 제출해 보세요. 새 도구가 반영되도록 서버를 반드시 재시작해야 합니다.

## 해답

[Solution](./solution/README.md)

## 주요 내용 정리

이번 장에서 배운 핵심 내용은 다음과 같습니다:

- AI Toolkit 확장은 MCP 서버와 그 도구를 손쉽게 사용할 수 있는 훌륭한 클라이언트입니다.
- MCP 서버에 새로운 도구를 추가해 에이전트의 기능을 확장할 수 있습니다.
- AI Toolkit은 Python MCP 서버 템플릿 등 커스텀 도구 생성에 도움을 주는 템플릿을 제공합니다.

## 추가 자료

- [AI Toolkit 문서](https://aka.ms/AIToolkit/doc)

## 다음 단계
- 다음: [테스트 및 디버깅](../08-testing/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원문 문서는 해당 언어의 원본이므로 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
