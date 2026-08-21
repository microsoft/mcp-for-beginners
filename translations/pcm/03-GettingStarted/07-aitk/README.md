# How to use server from AI Toolkit extension for Visual Studio Code

Wen yu dey build AI agent, e no be only to generate correct answer; e still mean say yu gots make ur agent fit do action. Na so Model Context Protocol (MCP) come dey important. MCP make am easy for agents to access tools and services outside in one sure way. Think am like na if yu jux plug ur agent inside toolbox Wey e fit really use well.

Make we say yu connect agent to ur calculator MCP server. Suddenly, ur agent fit do maths work by just seeing prompt like “Wetin be 47 multiply 89?”—no need to code tori or build custom API dem.

## Overview

This lesson go show how to connect calculator MCP server to agent with [AI Toolkit](https://aka.ms/AIToolkit) extension for Visual Studio Code, make ur agent fit do maths work like addition, subtraction, multiplication, and division with plain everyday talk.

AI Toolkit na strong extension for Visual Studio Code Wey dey help agent development well well. AI engineers fit build AI apps easily by testing and developing generative AI models—fit work locally or for cloud. Extension dey support most popular generative models wey dey today.

*Note*: AI Toolkit now dey support Python and TypeScript.

## Wetin You Go Learn

By di end of dis lesson, yu go sabi:

- How to consume MCP server through AI Toolkit.
- How to setup agent config make e fit find and use tools wey MCP server provide.
- How to use MCP tools with normal language talk.

## How We Go Take Do Am

Na so we go take do am for high level:

- Create agent and set im system prompt.
- Create MCP server wey get calculator tools.
- Connect Agent Builder to MCP server.
- Test how agent wan use tools through normal language.

Correct, now we sabi di way, make we configure AI agent make e use tools outside through MCP, make e fit sabi knock better work!

## Wetin You Need Before

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Exercise: How to Consume Server

> [!WARNING]
> Note for macOS Users. Right now we dey look into problem Wey dey affect how dependencies dey install for macOS. So macOS users no go fit finish dis tutorial yet. We go update di instructions once we fix am. Thank you for your patience and understanding!

For dis exercise, you go build, run, and sharpen AI agent wit tools from MCP server inside Visual Studio Code using AI Toolkit.

### -0- Prestep, add OpenAI GPT-4o model to My Models

Dis exercise dey use **GPT-4o** model. You gots add am for **My Models** before you fit create agent.

![Screenshot of a model selection interface in Visual Studio Code's AI Toolkit extension. The heading reads "Find the right model for your AI Solution" with a subtitle encouraging users to discover, test, and deploy AI models. Below, under “Popular Models,” six model cards are displayed: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), and DeepSeek-R1 (Ollama-hosted). Each card includes options to “Add” the model or “Try in Playground](../../../../translated_images/pcm/aitk-model-catalog.2acd38953bb9c119.webp)

1. Open **AI Toolkit** extension for **Activity Bar**.
1. Inside **Catalog** section, pick **Models** to open **Model Catalog**. Selecting **Models** go open **Model Catalog** for new editor tab.
1. Inside **Model Catalog** search bar, type **OpenAI GPT-4o**.
1. Click **+ Add** to add model go **My Models** list. Make sure say na model Wey **GitHub dey host** you select.
1. For **Activity Bar**, check say **OpenAI GPT-4o** model dey list.

### -1- Create Agent

**Agent (Prompt) Builder** dey let you create and customize your own AI-powered agents. For here, you go create new agent and assign model to power conversation.

![Screenshot of the "Calculator Agent" builder interface in the AI Toolkit extension for Visual Studio Code. On the left panel, the model selected is "OpenAI GPT-4o (via GitHub)." A system prompt reads "You are a professor in university teaching math," and the user prompt says, "Explain to me the Fourier equation in simple terms." Additional options include buttons for adding tools, enabling MCP Server, and selecting structured output. A blue “Run” button is at the bottom. On the right panel, under "Get Started with Examples," three sample agents are listed: Web Developer (with MCP Server, Second-Grade Simplifier, and Dream Interpreter, each with brief descriptions of their functions.](../../../../translated_images/pcm/aitk-agent-builder.901e3a2960c3e477.webp)

1. Open **AI Toolkit** extension from **Activity Bar**.
1. For **Tools** section, choose **Agent (Prompt) Builder**. E go open for new editor tab.
1. Click **+ New Agent** button. Extension go launch setup wizard through **Command Palette**.
1. Enter **Calculator Agent** as name and press **Enter**.
1. For **Agent (Prompt) Builder**, under **Model** field, pick **OpenAI GPT-4o (via GitHub)** model.

### -2- Create System Prompt for Agent

After you scaffold agent, time don reach to define personality and purpose. For here, you go use **Generate system prompt** feature to talk about how agent suppose behave—this case na calculator agent—and make model write system prompt for you.

![Screenshot of the "Calculator Agent" interface in the AI Toolkit for Visual Studio Code with a modal window open titled "Generate a prompt." The modal explains that a prompt template can be generated by sharing basic details and includes a text box with the sample system prompt: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Below the text box are "Close" and "Generate" buttons. In the background, part of the agent configuration is visible, including the selected model "OpenAI GPT-4o (via GitHub)" and fields for system and user prompts.](../../../../translated_images/pcm/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. For **Prompts** section, click **Generate system prompt**. E go open prompt builder Wey use AI to create system prompt for agent.
1. For **Generate a prompt** window, enter: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Click **Generate**. Notification go show for bottom-right confirm say system prompt dey generate. When e finish, the prompt go show for **System prompt** field of **Agent (Prompt) Builder**.
1. Check **System prompt** and change am if need be.

### -3- Create MCP Server

Now we define agent system prompt—wey go clear im behavior and responses—time don dey to give agent real power. For here, you go create calculator MCP server with tools Wey fit do addition, subtraction, multiplication, and division calculations. This server go allow agent do maths calculation for real time based on normal speech prompts.

!["Screenshot of the lower section of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. It shows expandable menus for “Tools” and “Structure output,” along with a dropdown menu labeled “Choose output format” set to “text.” To the right, there is a button labeled “+ MCP Server” for adding a Model Context Protocol server. An image icon placeholder is shown above the Tools section.](../../../../translated_images/pcm/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit get templates to help you quickly create MCP server. We go use Python template to create calculator MCP server.

*Note*: AI Toolkit now dey support Python and TypeScript.

1. For **Tools** section of **Agent (Prompt) Builder**, click **+ MCP Server**. Extension go launch setup wizard through **Command Palette**.
1. Pick **+ Add Server**.
1. Pick **Create a New MCP Server**.
1. Pick **python-weather** as template.
1. Pick **Default folder** to save MCP server template.
1. Enter server name: **Calculator**
1. New Visual Studio Code window go open. Click **Yes, I trust the authors**.
1. For terminal (**Terminal** > **New Terminal**), create virtual environment: `python -m venv .venv`
1. For terminal, activate virtual environment:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. For terminal, install dependencies: `pip install -e .[dev]`
1. For **Explorer** view inside **Activity Bar**, open **src** directory and pick **server.py** to open for editor.
1. Replace code for **server.py** with follow code and save am:

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

### -4- Run Agent with Calculator MCP Server

Now we get tools for agent, na so time don reach to use dem! For here, you go send prompts to agent to test if e go use correct tool from calculator MCP server.

![Screenshot of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. On the left panel, under “Tools,” an MCP server named local-server-calculator_server is added, showing four available tools: add, subtract, multiply, and divide. A badge shows that four tools are active. Below is a collapsed “Structure output” section and a blue “Run” button. On the right panel, under “Model Response,” the agent invokes the multiply and subtract tools with inputs {"a": 3, "b": 25} and {"a": 75, "b": 20} respectively. The final “Tool Response” is shown as 75.0. A “View Code” button appears at the bottom.](../../../../translated_images/pcm/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

You go run calculator MCP server for your local dev machine using **Agent Builder** as MCP client.

1. Press `F5` to start debugging MCP server. **Agent (Prompt) Builder** go open for new editor tab. Server status go show for terminal.
1. For **User prompt** field of **Agent (Prompt) Builder**, put this prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Click **Run** button to generate agent response.
1. Check agent output. Model suppose talk say you pay **$55**.
1. Dis na how e suppose happen:
    - Agent select **multiply** and **subtract** tools to help do calculation.
    - The correct `a` and `b` values go dey assign for **multiply** tool.
    - The correct `a` and `b` values go dey assign for **subtract** tool.
    - Response from every tool go show for **Tool Response**.
    - Final answer from model go show for **Model Response**.
1. Make you fit try other prompts to test agent more. You fit change prompt for **User prompt** field by clicking and replacing the prompt.
1. When you finish, you fit stop server for **terminal** by pressing **CTRL/CMD+C** to quit.

## Assignment

Try add another tool for your **server.py** file (like make e return square root of number). Submit more prompts Wey go require agent to use your new tool or the tools wey already dey. Make sure say you restart server to load new tools.

## Solution

[Solution](./solution/README.md)

## Main Points to Remember

Main things wey you go carry go from dis chapter na:

- AI Toolkit extension na good client wey allow you consume MCP Servers and their tools.
- You fit add new tools to MCP servers, make agent fit do more things as e need grow.
- AI Toolkit get templates (like Python MCP server templates) to make creating custom tools easy.

## More Resources

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## Wetin Next
- Next: [Testing & Debugging](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->