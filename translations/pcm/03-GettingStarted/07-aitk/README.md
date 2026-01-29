# How to use server wey dey from AI Toolkit extension for Visual Studio Code

When you dey build AI agent, e no be only to make am dey give smart answer; e go also need sabi how to take action. Na here Model Context Protocol (MCP) go help. MCP dey make am easy for agents to fit use external tools and services in one kind way wey dey consistent. Think am like say you dey connect your agent to toolbox wey e fit *really* use.

Make we say you connect one agent to your calculator MCP server. Just like that, your agent go fit do math operations if e receive prompt like “Wetin be 47 times 89?”—no need to dey write logic or build custom APIs.

## Overview

This lesson go show you how to connect calculator MCP server to agent wey dey use [AI Toolkit](https://aka.ms/AIToolkit) extension for Visual Studio Code. This one go make your agent fit do math operations like addition, subtraction, multiplication, and division through natural language.

AI Toolkit na one strong extension for Visual Studio Code wey dey make agent development easy. AI Engineers fit build AI applications easy by dey develop and test generative AI models—whether na for local machine or for cloud. The extension dey support most of the big generative models wey dey available today.

*Note*: AI Toolkit dey support Python and TypeScript for now.

## Learning Objectives

By the time you finish this lesson, you go sabi:

- How to use MCP server through AI Toolkit.
- How to configure agent settings so e go fit find and use tools wey MCP server provide.
- How to use MCP tools through natural language.

## Approach

Na so we go take approach this matter:

- Create agent and set im system prompt.
- Create MCP server wey get calculator tools.
- Connect Agent Builder to MCP server.
- Test how agent dey use tools through natural language.

Okay, now we don understand the flow, make we configure AI agent wey go fit use external tools through MCP to make am better!

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Exercise: How to use server

> [!WARNING]
> Note for macOS Users. We dey check one issue wey dey affect dependency installation for macOS. Because of this, macOS users no go fit complete this tutorial for now. We go update the instructions as soon as we fix am. Thank you for your patience and understanding!

For this exercise, you go build, run, and improve AI agent wey dey use tools from MCP server inside Visual Studio Code with AI Toolkit.

### -0- Prestep, add OpenAI GPT-4o model to My Models

This exercise dey use **GPT-4o** model. You go need add the model to **My Models** before you create the agent.

![Screenshot of model selection interface for AI Toolkit extension for Visual Studio Code. Heading talk "Find the right model for your AI Solution" with subtitle wey dey encourage users to discover, test, and deploy AI models. Under “Popular Models,” six model cards dey show: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), and DeepSeek-R1 (Ollama-hosted). Each card get options to “Add” the model or “Try in Playground](../../../../translated_images/pcm/aitk-model-catalog.2acd38953bb9c119.webp)

1. Open **AI Toolkit** extension from **Activity Bar**.
1. For **Catalog** section, select **Models** to open **Model Catalog**. When you select **Models**, e go open **Model Catalog** for new editor tab.
1. For **Model Catalog** search bar, type **OpenAI GPT-4o**.
1. Click **+ Add** to add the model to your **My Models** list. Make sure say na the model wey **Hosted by GitHub** you select.
1. For **Activity Bar**, confirm say **OpenAI GPT-4o** model dey appear for the list.

### -1- Create agent

The **Agent (Prompt) Builder** dey help you create and customize your own AI-powered agents. For this section, you go create new agent and assign model wey go power the conversation.

![Screenshot of "Calculator Agent" builder interface for AI Toolkit extension for Visual Studio Code. For left panel, the model wey dem select na "OpenAI GPT-4o (via GitHub)." System prompt talk "You are a professor in university teaching math," and user prompt talk "Explain to me the Fourier equation in simple terms." Other options dey include buttons for adding tools, enabling MCP Server, and selecting structured output. Blue “Run” button dey bottom. For right panel, under "Get Started with Examples," three sample agents dey listed: Web Developer (with MCP Server, Second-Grade Simplifier, and Dream Interpreter, each with short description of wetin dem dey do.](../../../../translated_images/pcm/aitk-agent-builder.901e3a2960c3e477.webp)

1. Open **AI Toolkit** extension from **Activity Bar**.
1. For **Tools** section, select **Agent (Prompt) Builder**. When you select **Agent (Prompt) Builder**, e go open **Agent (Prompt) Builder** for new editor tab.
1. Click **+ New Agent** button. The extension go launch setup wizard through **Command Palette**.
1. Enter name **Calculator Agent** and press **Enter**.
1. For **Agent (Prompt) Builder**, for **Model** field, select **OpenAI GPT-4o (via GitHub)** model.

### -2- Create system prompt for agent

Now wey you don scaffold the agent, e don reach time to define im personality and wetin e go dey do. For this section, you go use **Generate system prompt** feature to describe wetin the agent go dey do—like calculator agent—and make the model write the system prompt for you.

![Screenshot of "Calculator Agent" interface for AI Toolkit for Visual Studio Code with modal window wey open wey get title "Generate a prompt." The modal dey explain say prompt template fit dey generated by sharing basic details and e get text box wey show sample system prompt: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Below the text box, "Close" and "Generate" buttons dey. For background, part of the agent configuration dey visible, including the selected model "OpenAI GPT-4o (via GitHub)" and fields for system and user prompts.](../../../../translated_images/pcm/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. For **Prompts** section, click **Generate system prompt** button. This button go open prompt builder wey dey use AI to generate system prompt for the agent.
1. For **Generate a prompt** window, enter this: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Click **Generate** button. Notification go show for bottom-right corner wey go confirm say system prompt dey generated. When e finish, the prompt go appear for **System prompt** field of **Agent (Prompt) Builder**.
1. Check the **System prompt** and change am if you need.

### -3- Create MCP server

Now wey you don define your agent system prompt—wey dey guide im behavior and response—e don reach time to give the agent practical skills. For this section, you go create calculator MCP server wey get tools to do addition, subtraction, multiplication, and division calculations. This server go make your agent fit do real-time math operations when e get natural language prompts.

!["Screenshot of lower section of Calculator Agent interface for AI Toolkit extension for Visual Studio Code. E show expandable menus for “Tools” and “Structure output,” with dropdown menu wey talk “Choose output format” wey dey set to “text.” For right, e get button wey talk “+ MCP Server” for adding Model Context Protocol server. Placeholder image icon dey above Tools section.](../../../../translated_images/pcm/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit get templates wey dey make am easy to create your own MCP server. We go use Python template to create calculator MCP server.

*Note*: AI Toolkit dey support Python and TypeScript for now.

1. For **Tools** section of **Agent (Prompt) Builder**, click **+ MCP Server** button. The extension go launch setup wizard through **Command Palette**.
1. Select **+ Add Server**.
1. Select **Create a New MCP Server**.
1. Select **python-weather** as template.
1. Select **Default folder** to save MCP server template.
1. Enter this name for server: **Calculator**
1. New Visual Studio Code window go open. Select **Yes, I trust the authors**.
1. Use terminal (**Terminal** > **New Terminal**) to create virtual environment: `python -m venv .venv`
1. Use terminal to activate virtual environment:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Use terminal to install dependencies: `pip install -e .[dev]`
1. For **Explorer** view of **Activity Bar**, expand **src** directory and select **server.py** to open file for editor.
1. Replace the code for **server.py** file with this and save:

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

### -4- Run agent with calculator MCP server

Now wey your agent don get tools, e don reach time to use dem! For this section, you go submit prompts to the agent to test and confirm whether the agent dey use the correct tool from calculator MCP server.

![Screenshot of Calculator Agent interface for AI Toolkit extension for Visual Studio Code. For left panel, under “Tools,” MCP server wey dem name local-server-calculator_server dey added, e show four tools wey dey available: add, subtract, multiply, and divide. Badge dey show say four tools dey active. Below, e get collapsed “Structure output” section and blue “Run” button. For right panel, under “Model Response,” the agent dey use multiply and subtract tools with inputs {"a": 3, "b": 25} and {"a": 75, "b": 20} respectively. Final “Tool Response” dey show as 75.0. “View Code” button dey bottom.](../../../../translated_images/pcm/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

You go run calculator MCP server for your local dev machine through **Agent Builder** as MCP client.

1. Press `F5` to start debugging MCP server. **Agent (Prompt) Builder** go open for new editor tab. The server status go dey visible for terminal.
1. For **User prompt** field of **Agent (Prompt) Builder**, enter this prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Click **Run** button to generate agent response.
1. Check the agent output. The model suppose talk say you pay **$55**.
1. Na so e suppose happen:
    - The agent go choose **multiply** and **subtract** tools to help for the calculation.
    - The `a` and `b` values go dey assigned for **multiply** tool.
    - The `a` and `b` values go dey assigned for **subtract** tool.
    - The response from each tool go dey show for **Tool Response**.
    - The final output from the model go dey show for **Model Response**.
1. Submit more prompts to test the agent well. You fit change the prompt wey dey **User prompt** field by clicking inside the field and replacing the prompt wey dey there.
1. When you don finish testing the agent, you fit stop the server through **terminal** by entering **CTRL/CMD+C** to quit.

## Assignment

Try add another tool entry to your **server.py** file (example: make e fit return square root of number). Submit more prompts wey go make the agent use your new tool (or the tools wey dey already). Make sure say you restart the server to load the new tools wey you add.

## Solution

[Solution](./solution/README.md)

## Key Takeaways

The things wey you go carry from this chapter na:

- AI Toolkit extension na better client wey dey let you use MCP Servers and their tools.
- You fit add new tools to MCP servers to make the agent sabi do more things wey fit meet new needs.
- AI Toolkit get templates (like Python MCP server templates) wey dey make am easy to create custom tools.

## Additional Resources

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## Wetin go happen next
- Next: [Testing & Debugging](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am correct, abeg make you sabi say machine transle-shon fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->