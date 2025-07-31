# Consuming a server from the AI Toolkit extension for Visual Studio Code

When you’re building an AI agent, it’s not just about generating smart responses; it’s also about giving your agent the ability to take action. That’s where the Model Context Protocol (MCP) comes in. MCP makes it easy for agents to access external tools and services in a consistent way. Think of it like plugging your agent into a toolbox it can *actually* use.

Let’s say you connect an agent to your calculator MCP server. Suddenly, your agent can perform math operations just by receiving a prompt like “What’s 47 times 89?”—no need to hardcode logic or build custom APIs.

## Overview

This lesson covers how to connect a calculator MCP server to an agent with the [AI Toolkit](https://aka.ms/AIToolkit) extension in Visual Studio Code, enabling your agent to perform math operations such as addition, subtraction, multiplication, and division through natural language.

AI Toolkit is a powerful extension for Visual Studio Code that streamlines agent development. AI Engineers can easily build AI applications by developing and testing generative AI models—locally or in the cloud. The extension supports most major generative models available today.

*Note*: The AI Toolkit currently supports Python and TypeScript.

## Learning Objectives

By the end of this lesson, you will be able to:

- Consume an MCP server via the AI Toolkit.
- Configure an agent configuration to enable it to discover and utilize tools provided by the MCP server.
- Utilize MCP tools via natural language.

## Approach

Here's how we need to approach this at a high level:

- Create an agent and define its system prompt.
- Create a MCP server with calculator tools.
- Connect the Agent Builder to the MCP server.
- Test the agent's tool invocation via natural language.

Great, now that we understand the flow, let's configure an AI agent to leverage external tools through MCP, enhancing its capabilities!

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Exercise: Consuming a server

> [!WARNING]
> Note for macOS Users. We're currently investigating an issue affecting dependency installation on macOS. As a result, macOS users won’t be able to complete this tutorial at this time. We’ll update the instructions as soon as a fix is available. Thank you for your patience and understanding!

In this exercise, you will build, run, and enhance an AI agent with tools from a MCP server inside Visual Studio Code using the AI Toolkit.

### -0- Prestep, add the OpenAI GPT-4o model to My Models

The exercise leverages the **GPT-4o** model. The model should be added to **My Models** before creating the agent.

![Screenshot of a model selection interface in Visual Studio Code's AI Toolkit extension. The heading reads "Find the right model for your AI Solution" with a subtitle encouraging users to discover, test, and deploy AI models. Below, under “Popular Models,” six model cards are displayed: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), and DeepSeek-R1 (Ollama-hosted). Each card includes options to “Add” the model or “Try in Playground](./assets/aitk-model-catalog.png)

1. Open the **AI Toolkit** extension from the **Activity Bar**.
1. In the **Catalog** section, select **Models** to open the **Model Catalog**. Selecting **Models** opens the **Model Catalog** in a new editor tab.
1. In the **Model Catalog** search bar, enter **OpenAI GPT-4o**.
1. Click **+ Add** to add the model to your **My Models** list. Ensure that you've selected the model that's **Hosted by GitHub**.
1. In the **Activity Bar**, confirm that the **OpenAI GPT-4o** model appears in the list.

### -1- Create an agent

The **Agent (Prompt) Builder** enables you to create and customize your own AI-powered agents. In this section, you’ll create a new agent and assign a model to power the conversation.

![Screenshot of the "Calculator Agent" builder interface in the AI Toolkit extension for Visual Studio Code. On the left panel, the model selected is "OpenAI GPT-4o (via GitHub)." A system prompt reads "You are a professor in university teaching math," and the user prompt says, "Explain to me the Fourier equation in simple terms." Additional options include buttons for adding tools, enabling MCP Server, and selecting structured output. A blue “Run” button is at the bottom. On the right panel, under "Get Started with Examples," three sample agents are listed: Web Developer (with MCP Server, Second-Grade Simplifier, and Dream Interpreter, each with brief descriptions of their functions.](./assets/aitk-agent-builder.png)

1. Open the **AI Toolkit** extension from the **Activity Bar**.
1. In the **Tools** section, select **Agent (Prompt) Builder**. Selecting **Agent (Prompt) Builder** opens the **Agent (Prompt) Builder** in a new editor tab.
1. Click the **+ New Agent** button. The extension will launch a setup wizard via the **Command Palette**.
1. Enter the name **Calculator Agent** and press **Enter**.
1. In the **Agent (Prompt) Builder**, for the **Model** field, select the **OpenAI GPT-4o (via GitHub)** model.

### -2- Create a system prompt for the agent

With the agent scaffolded, it’s time to define its personality and purpose. In this section, you’ll use the **Generate system prompt** feature to describe the agent’s intended behavior—in this case, a calculator agent—and have the model write the system prompt for you.

![Screenshot of the "Calculator Agent" interface in the AI Toolkit for Visual Studio Code with a modal window open titled "Generate a prompt." The modal explains that a prompt template can be generated by sharing basic details and includes a text box with the sample system prompt: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Below the text box are "Close" and "Generate" buttons. In the background, part of the agent configuration is visible, including the selected model "OpenAI GPT-4o (via GitHub)" and fields for system and user prompts.](./assets/aitk-generate-prompt.png)

1. For the **Prompts** section, click the **Generate system prompt** button. This button opens in the prompt builder which leverages AI to generate a system prompt for the agent.
1. In the **Generate a prompt** window, enter the following: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Click the **Generate** button. A notification will appear in the bottom-right corner confirming that the system prompt is being generated. Once the prompt generation is complete, the prompt will appear in the **System prompt** field of the **Agent (Prompt) Builder**.
1. Review the **System prompt** and modify if necessary.

### -3- Create a MCP server

Now that you've defined your agent's system prompt—guiding its behavior and responses—it's time to equip the agent with practical capabilities. In this section, you’ll create a calculator MCP server with tools to execute addition, subtraction, multiplication, and division calculations. This server will enable your agent to perform real-time math operations in response to natural language prompts.

!["Screenshot of the lower section of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. It shows expandable menus for “Tools” and “Structure output,” along with a dropdown menu labeled “Choose output format” set to “text.” To the right, there is a button labeled “+ MCP Server” for adding a Model Context Protocol server. An image icon placeholder is shown above the Tools section.](./assets/aitk-add-mcp-server.png)

AI Toolkit is equipped with templates for ease of creating your own MCP server. We'll use the Python template for creating the calculator MCP server.

*Note*: The AI Toolkit currently supports Python and TypeScript.

1. In the **Tools** section of the **Agent (Prompt) Builder**, click the **+ MCP Server** button. The extension will launch a setup wizard via the **Command Palette**.
1. Select **+ Add Server**.
1. Select **Create a New MCP Server**.
1. Select **python-weather** as the template.
1. Select **Default folder** to save the MCP server template.
1. Enter the following name for the server: **Calculator**
1. A new Visual Studio Code window will open. Select **Yes, I trust the authors**.
1. Using the terminal (**Terminal** > **New Terminal**), create a virtual environment: `python -m venv .venv`
1. Using the terminal, activate the virtual environment:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. Using the terminal, install the dependencies: `pip install -e .[dev]`
1. In the **Explorer** view of the **Activity Bar**, expand the **src** directory and select **server.py** to open the file in the editor.
1. Replace the code in the **server.py** file with the following and save:

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

Now that your agent has tools, it's time to use them! In this section, you'll submit prompts to the agent to test and validate whether the agent leverages the appropriate tool from the calculator MCP server.

![Screenshot of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. On the left panel, under “Tools,” an MCP server named local-server-calculator_server is added, showing four available tools: add, subtract, multiply, and divide. A badge shows that four tools are active. Below is a collapsed “Structure output” section and a blue “Run” button. On the right panel, under “Model Response,” the agent invokes the multiply and subtract tools with inputs {"a": 3, "b": 25} and {"a": 75, "b": 20} respectively. The final “Tool Response” is shown as 75.0. A “View Code” button appears at the bottom.](./assets/aitk-agent-response-with-tools.png)

You will run the calculator MCP server on your local dev machine via the **Agent Builder** as the MCP client.

1. Press `F5` to start debugging the MCP server. The **Agent (Prompt) Builder** will open in a new editor tab. The status of the server is visible in the terminal.
1. In the **User prompt** field of the **Agent (Prompt) Builder**, enter the following prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Click the **Run** button to generate the agent's response.
1. Review the agent output. The model should conclude that you paid **$55**.
1. Here's a breakdown of what should occur:
    - The agent selects the **multiply** and **substract** tools to aid in the calculation.
    - The respective `a` and `b` values are assigned for the **multiply** tool.
    - The respective `a` and `b` values are assigned for the **subtract** tool.
    - The response from each tool is provided in the respective **Tool Response**.
    - The final output from the model is provided in the final **Model Response**.
1. Submit additional prompts to further test the agent. You can modify the existing prompt in the **User prompt** field by clicking into the field and replacing the existing prompt.
1. Once you're done testing the agent, you can stop the server via the **terminal** by entering **CTRL/CMD+C** to quit.

## Assignment

Try adding an additional tool entry to your **server.py** file (ex: return the square root of a number). Submit additional prompts that would require the agent to leverage your new tool (or existing tools). Be sure to restart the server to load newly added tools.

## Solution

[Solution](./solution/README.md)

## Key Takeaways

The takeaways from this chapter is the following:

- The AI Toolkit extension is a great client that lets you consume MCP Servers and their tools.
- You can add new tools to MCP servers, expanding the agent's capabilities to meet evolving requirements.
- The AI Toolkit includes templates (e.g., Python MCP server templates) to simplify the creation of custom tools.

## Additional Resources

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## What's Next
- Next: [Testing & Debugging](../08-testing/README.md)
