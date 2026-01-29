# Consuming a server from the AI Toolkit extension for Visual Studio Code

When building an AI agent, it’s not just about generating intelligent responses; it’s also about enabling your agent to take action. That’s where the Model Context Protocol (MCP) comes in. MCP allows agents to access external tools and services in a consistent way. Think of it as plugging your agent into a toolbox it can *actually* use.

For example, if you connect an agent to your calculator MCP server, your agent can perform math operations simply by receiving a prompt like “What’s 47 times 89?”—no need to hardcode logic or create custom APIs.

## Overview

This lesson explains how to connect a calculator MCP server to an agent using the [AI Toolkit](https://aka.ms/AIToolkit) extension in Visual Studio Code. This connection enables your agent to perform math operations like addition, subtraction, multiplication, and division through natural language.

AI Toolkit is a powerful extension for Visual Studio Code that simplifies agent development. AI Engineers can easily build AI applications by developing and testing generative AI models—locally or in the cloud. The extension supports most major generative models available today.

*Note*: The AI Toolkit currently supports Python and TypeScript.

## Learning Objectives

By the end of this lesson, you will be able to:

- Use an MCP server with the AI Toolkit.
- Configure an agent to discover and use tools provided by the MCP server.
- Interact with MCP tools using natural language.

## Approach

Here’s the high-level approach:

- Create an agent and define its system prompt.
- Set up an MCP server with calculator tools.
- Connect the Agent Builder to the MCP server.
- Test the agent’s ability to use tools via natural language.

Now that we understand the process, let’s configure an AI agent to use external tools through MCP, enhancing its capabilities!

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Exercise: Consuming a server

> [!WARNING]
> Note for macOS Users: We are currently investigating an issue affecting dependency installation on macOS. As a result, macOS users won’t be able to complete this tutorial at this time. We’ll update the instructions as soon as a fix is available. Thank you for your patience and understanding!

In this exercise, you will build, run, and enhance an AI agent with tools from an MCP server inside Visual Studio Code using the AI Toolkit.

### -0- Prestep: Add the OpenAI GPT-4o model to My Models

This exercise uses the **GPT-4o** model. Make sure to add it to **My Models** before creating the agent.

![Screenshot of a model selection interface in Visual Studio Code's AI Toolkit extension. The heading reads "Find the right model for your AI Solution" with a subtitle encouraging users to discover, test, and deploy AI models. Below, under “Popular Models,” six model cards are displayed: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), and DeepSeek-R1 (Ollama-hosted). Each card includes options to “Add” the model or “Try in Playground](../../../../translated_images/en/aitk-model-catalog.2acd38953bb9c119.webp)

1. Open the **AI Toolkit** extension from the **Activity Bar**.
2. In the **Catalog** section, select **Models** to open the **Model Catalog**. This opens the **Model Catalog** in a new editor tab.
3. In the **Model Catalog** search bar, enter **OpenAI GPT-4o**.
4. Click **+ Add** to add the model to your **My Models** list. Ensure that you select the model **Hosted by GitHub**.
5. In the **Activity Bar**, confirm that the **OpenAI GPT-4o** model appears in the list.

### -1- Create an agent

The **Agent (Prompt) Builder** allows you to create and customize your own AI-powered agents. In this section, you’ll create a new agent and assign a model to power the conversation.

![Screenshot of the "Calculator Agent" builder interface in the AI Toolkit extension for Visual Studio Code. On the left panel, the model selected is "OpenAI GPT-4o (via GitHub)." A system prompt reads "You are a professor in university teaching math," and the user prompt says, "Explain to me the Fourier equation in simple terms." Additional options include buttons for adding tools, enabling MCP Server, and selecting structured output. A blue “Run” button is at the bottom. On the right panel, under "Get Started with Examples," three sample agents are listed: Web Developer (with MCP Server, Second-Grade Simplifier, and Dream Interpreter, each with brief descriptions of their functions.](../../../../translated_images/en/aitk-agent-builder.901e3a2960c3e477.webp)

1. Open the **AI Toolkit** extension from the **Activity Bar**.
2. In the **Tools** section, select **Agent (Prompt) Builder**. This opens the **Agent (Prompt) Builder** in a new editor tab.
3. Click the **+ New Agent** button. The extension will launch a setup wizard via the **Command Palette**.
4. Enter the name **Calculator Agent** and press **Enter**.
5. In the **Agent (Prompt) Builder**, for the **Model** field, select the **OpenAI GPT-4o (via GitHub)** model.

### -2- Create a system prompt for the agent

With the agent scaffolded, it’s time to define its personality and purpose. In this section, you’ll use the **Generate system prompt** feature to describe the agent’s intended behavior—in this case, a calculator agent—and have the model write the system prompt for you.

![Screenshot of the "Calculator Agent" interface in the AI Toolkit for Visual Studio Code with a modal window open titled "Generate a prompt." The modal explains that a prompt template can be generated by sharing basic details and includes a text box with the sample system prompt: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Below the text box are "Close" and "Generate" buttons. In the background, part of the agent configuration is visible, including the selected model "OpenAI GPT-4o (via GitHub)" and fields for system and user prompts.](../../../../translated_images/en/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. In the **Prompts** section, click the **Generate system prompt** button. This opens the prompt builder, which uses AI to generate a system prompt for the agent.
2. In the **Generate a prompt** window, enter the following: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
3. Click the **Generate** button. A notification will appear in the bottom-right corner confirming that the system prompt is being generated. Once the prompt generation is complete, the prompt will appear in the **System prompt** field of the **Agent (Prompt) Builder**.
4. Review the **System prompt** and modify it if necessary.

### -3- Create an MCP server

Now that you’ve defined your agent’s system prompt—guiding its behavior and responses—it’s time to equip the agent with practical capabilities. In this section, you’ll create a calculator MCP server with tools to perform addition, subtraction, multiplication, and division. This server will enable your agent to handle real-time math operations in response to natural language prompts.

!["Screenshot of the lower section of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. It shows expandable menus for “Tools” and “Structure output,” along with a dropdown menu labeled “Choose output format” set to “text.” To the right, there is a button labeled “+ MCP Server” for adding a Model Context Protocol server. An image icon placeholder is shown above the Tools section.](../../../../translated_images/en/aitk-add-mcp-server.9742cfddfe808353.webp)

The AI Toolkit includes templates to simplify creating your own MCP server. We’ll use the Python template to create the calculator MCP server.

*Note*: The AI Toolkit currently supports Python and TypeScript.

1. In the **Tools** section of the **Agent (Prompt) Builder**, click the **+ MCP Server** button. The extension will launch a setup wizard via the **Command Palette**.
2. Select **+ Add Server**.
3. Select **Create a New MCP Server**.
4. Select **python-weather** as the template.
5. Select **Default folder** to save the MCP server template.
6. Enter the following name for the server: **Calculator**.
7. A new Visual Studio Code window will open. Select **Yes, I trust the authors**.
8. Using the terminal (**Terminal** > **New Terminal**), create a virtual environment: `python -m venv .venv`.
9. Using the terminal, activate the virtual environment:
    - Windows: `.venv\Scripts\activate`
    - macOS/Linux: `source .venv/bin/activate`
10. Using the terminal, install the dependencies: `pip install -e .[dev]`.
11. In the **Explorer** view of the **Activity Bar**, expand the **src** directory and select **server.py** to open the file in the editor.
12. Replace the code in the **server.py** file with the following and save:

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

### -4- Run the agent with the calculator MCP server

Now that your agent has tools, it’s time to use them! In this section, you’ll submit prompts to the agent to test and validate whether the agent uses the appropriate tool from the calculator MCP server.

![Screenshot of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. On the left panel, under “Tools,” an MCP server named local-server-calculator_server is added, showing four available tools: add, subtract, multiply, and divide. A badge shows that four tools are active. Below is a collapsed “Structure output” section and a blue “Run” button. On the right panel, under “Model Response,” the agent invokes the multiply and subtract tools with inputs {"a": 3, "b": 25} and {"a": 75, "b": 20} respectively. The final “Tool Response” is shown as 75.0. A “View Code” button appears at the bottom.](../../../../translated_images/en/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

You will run the calculator MCP server on your local development machine via the **Agent Builder** as the MCP client.

1. Press `F5` to start debugging the MCP server. The **Agent (Prompt) Builder** will open in a new editor tab. The server status is visible in the terminal.
2. In the **User prompt** field of the **Agent (Prompt) Builder**, enter the following prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
3. Click the **Run** button to generate the agent’s response.
4. Review the agent output. The model should conclude that you paid **$55**.
5. Here’s what should happen:
    - The agent selects the **multiply** and **subtract** tools to perform the calculation.
    - The respective `a` and `b` values are assigned for the **multiply** tool.
    - The respective `a` and `b` values are assigned for the **subtract** tool.
    - The response from each tool is provided in the respective **Tool Response**.
    - The final output from the model is provided in the **Model Response**.
6. Submit additional prompts to further test the agent. You can modify the existing prompt in the **User prompt** field by clicking into the field and replacing the existing prompt.
7. Once you’re done testing the agent, stop the server via the **terminal** by entering **CTRL/CMD+C** to quit.

## Assignment

Try adding an additional tool entry to your **server.py** file (e.g., return the square root of a number). Submit additional prompts that require the agent to use your new tool (or existing tools). Be sure to restart the server to load the newly added tools.

## Solution

[Solution](./solution/README.md)

## Key Takeaways

The key takeaways from this chapter are:

- The AI Toolkit extension is an excellent client for consuming MCP Servers and their tools.
- You can add new tools to MCP servers, expanding the agent’s capabilities to meet evolving requirements.
- The AI Toolkit includes templates (e.g., Python MCP server templates) to simplify the creation of custom tools.

## Additional Resources

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## What's Next
- Next: [Testing & Debugging](../08-testing/README.md)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.