# Consuming a server with Microsoft Foundry Toolkit for Visual Studio Code

When you’re building an AI agent, it’s not just about generating smart responses; it’s also about giving your agent the ability to take action. That’s where the Model Context Protocol (MCP) comes in. MCP makes it easy for agents to access external tools and services in a consistent way. Think of it like plugging your agent into a toolbox it can *actually* use.

Let’s say you connect an agent to your calculator MCP server. Suddenly, your agent can perform math operations just by receiving a prompt like “What’s 47 times 89?”—no need to hardcode logic or build custom APIs.

## Overview

This lesson covers how to connect a calculator MCP server to an agent with
[Microsoft Foundry Toolkit for Visual Studio Code](https://aka.ms/AIToolkit),
enabling your agent to perform math operations through natural language.

Microsoft Foundry Toolkit streamlines the development and testing of generative
AI applications with local and cloud-hosted models.

*Note*: The Toolkit currently supports Python and TypeScript MCP templates.

## Learning Objectives

By the end of this lesson, you will be able to:

- Consume an MCP server with Microsoft Foundry Toolkit.
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
- [Microsoft Foundry Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Exercise: Consuming a server

> [!WARNING]
> Note for macOS Users. We're currently investigating an issue affecting dependency installation on macOS. As a result, macOS users won’t be able to complete this tutorial at this time. We’ll update the instructions as soon as a fix is available. Thank you for your patience and understanding!

In this exercise, you will build, run, and enhance an AI agent with tools from
an MCP server inside Visual Studio Code using Microsoft Foundry Toolkit.

### -0- Prestep, add a Microsoft Foundry GPT-5.1 deployment

Create a Microsoft Foundry resource, deploy **GPT-5.1**, and add the deployment
to **My Models**. Review the
[model retirement schedule](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule)
when choosing a deployment.

1. Open **Microsoft Foundry Toolkit** from the **Activity Bar**.
1. In the **Catalog** section, select **Models** to open the **Model Catalog**. Selecting **Models** opens the **Model Catalog** in a new editor tab.
1. Connect your Microsoft Foundry project and select your **GPT-5.1** deployment.
1. Click **+ Add** to add the deployment to your **My Models** list.
1. In the **Activity Bar**, confirm that the deployment appears in the list.

### -1- Create an agent

The **Agent (Prompt) Builder** enables you to create and customize your own AI-powered agents. In this section, you’ll create a new agent and assign a model to power the conversation.

1. Open **Microsoft Foundry Toolkit** from the **Activity Bar**.
1. In the **Tools** section, select **Agent (Prompt) Builder**. Selecting **Agent (Prompt) Builder** opens the **Agent (Prompt) Builder** in a new editor tab.
1. Click the **+ New Agent** button. The extension will launch a setup wizard via the **Command Palette**.
1. Enter the name **Calculator Agent** and press **Enter**.
1. In the **Agent (Prompt) Builder**, select your **GPT-5.1** Foundry deployment.

### -2- Create a system prompt for the agent

With the agent scaffolded, it’s time to define its personality and purpose. In this section, you’ll use the **Generate system prompt** feature to describe the agent’s intended behavior—in this case, a calculator agent—and have the model write the system prompt for you.

1. For the **Prompts** section, click the **Generate system prompt** button. This button opens in the prompt builder which leverages AI to generate a system prompt for the agent.
1. In the **Generate a prompt** window, enter the following: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. Click the **Generate** button. A notification will appear in the bottom-right corner confirming that the system prompt is being generated. Once the prompt generation is complete, the prompt will appear in the **System prompt** field of the **Agent (Prompt) Builder**.
1. Review the **System prompt** and modify if necessary.

### -3- Create a MCP server

Now that you've defined your agent's system prompt—guiding its behavior and responses—it's time to equip the agent with practical capabilities. In this section, you’ll create a calculator MCP server with tools to execute addition, subtraction, multiplication, and division calculations. This server will enable your agent to perform real-time math operations in response to natural language prompts.

![Screenshot of the lower section of the Calculator Agent interface in Microsoft Foundry Toolkit for Visual Studio Code.](./assets/aitk-add-mcp-server.png)

Microsoft Foundry Toolkit includes templates for creating MCP servers. We'll
use the Python template for the calculator MCP server.

*Note*: The Toolkit currently supports Python and TypeScript MCP templates.

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

![Screenshot of the Calculator Agent invoking MCP calculator tools in Microsoft Foundry Toolkit.](./assets/aitk-agent-response-with-tools.png)

You will run the calculator MCP server on your local dev machine via the **Agent Builder** as the MCP client.

1. Press `F5` to start debugging the MCP server. The **Agent (Prompt) Builder** will open in a new editor tab. The status of the server is visible in the terminal.
1. In the **User prompt** field of the **Agent (Prompt) Builder**, enter the following prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Click the **Run** button to generate the agent's response.
1. Review the agent output. The model should conclude that you paid **$55**.
1. Here's a breakdown of what should occur:
    - The agent selects the **multiply** and **subtract** tools to aid in the calculation.
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

- Microsoft Foundry Toolkit can consume MCP servers and their tools.
- You can add new tools to MCP servers, expanding the agent's capabilities to meet evolving requirements.
- Microsoft Foundry Toolkit includes MCP server templates for creating custom tools.

## Additional Resources

- [Microsoft Foundry Toolkit documentation](https://aka.ms/AIToolkit/doc)

## What's Next
- Next: [Testing & Debugging](../08-testing/README.md)
