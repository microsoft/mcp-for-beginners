<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "af6cee6052e751674c1d9022a4b204e6",
  "translation_date": "2025-06-03T14:53:41+00:00",
  "source_file": "03-GettingStarted/06-aitk/README.md",
  "language_code": "sl"
}
-->
# Consuming a server from the AI Toolkit extension for Visual Studio Code

When building an AI agent, it’s not just about generating smart replies; it’s also about enabling your agent to take action. That’s where the Model Context Protocol (MCP) comes in. MCP makes it simple for agents to access external tools and services in a consistent way. Think of it as plugging your agent into a toolbox it can *actually* use.

Imagine connecting an agent to your calculator MCP server. Suddenly, your agent can do math operations just by receiving a prompt like “What’s 47 times 89?”—no need to hardcode logic or build custom APIs.

## Overview

This lesson explains how to connect a calculator MCP server to an agent using the [AI Toolkit](https://aka.ms/AIToolkit) extension in Visual Studio Code, allowing your agent to perform math operations such as addition, subtraction, multiplication, and division through natural language.

AI Toolkit is a powerful extension for Visual Studio Code that streamlines agent development. AI Engineers can easily build AI applications by creating and testing generative AI models—locally or in the cloud. The extension supports most major generative models available today.

*Note*: The AI Toolkit currently supports Python and TypeScript.

## Learning Objectives

By the end of this lesson, you will be able to:

- Consume an MCP server via the AI Toolkit.
- Configure an agent setup to let it discover and use tools provided by the MCP server.
- Use MCP tools through natural language.

## Approach

Here’s the high-level approach:

- Create an agent and define its system prompt.
- Create a MCP server with calculator tools.
- Connect the Agent Builder to the MCP server.
- Test the agent’s tool usage via natural language.

Great, now that we know the flow, let’s configure an AI agent to leverage external tools through MCP, boosting its capabilities!

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [AI Toolkit for Visual Studio Code](https://aka.ms/AIToolkit)

## Exercise: Consuming a server

In this exercise, you will build, run, and improve an AI agent with tools from a MCP server inside Visual Studio Code using the AI Toolkit.

### -0- Prestep, add the OpenAI GPT-4o model to My Models

The exercise uses the **GPT-4o** model. Add this model to **My Models** before creating the agent.

![Screenshot of a model selection interface in Visual Studio Code's AI Toolkit extension. The heading reads "Find the right model for your AI Solution" with a subtitle encouraging users to discover, test, and deploy AI models. Below, under “Popular Models,” six model cards are displayed: DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), and DeepSeek-R1 (Ollama-hosted). Each card includes options to “Add” the model or “Try in Playground](../../../../translated_images/aitk-model-catalog.c0c66f0d9ac0ee73c1d21b9207db99e914ef9dd52fced6f226c2b1f537e2c447.sl.png)

1. Open the **AI Toolkit** extension from the **Activity Bar**.
2. In the **Catalog** section, select **Models** to open the **Model Catalog**. This opens the **Model Catalog** in a new editor tab.
3. In the **Model Catalog** search bar, type **OpenAI GPT-4o**.
4. Click **+ Add** to add the model to your **My Models** list. Make sure you pick the model **Hosted by GitHub**.
5. In the **Activity Bar**, verify that the **OpenAI GPT-4o** model appears in your list.

### -1- Create an agent

The **Agent (Prompt) Builder** lets you create and customize your own AI-powered agents. Here, you’ll create a new agent and assign a model to power the conversation.

![Screenshot of the "Calculator Agent" builder interface in the AI Toolkit extension for Visual Studio Code. On the left panel, the model selected is "OpenAI GPT-4o (via GitHub)." A system prompt reads "You are a professor in university teaching math," and the user prompt says, "Explain to me the Fourier equation in simple terms." Additional options include buttons for adding tools, enabling MCP Server, and selecting structured output. A blue “Run” button is at the bottom. On the right panel, under "Get Started with Examples," three sample agents are listed: Web Developer (with MCP Server, Second-Grade Simplifier, and Dream Interpreter, each with brief descriptions of their functions.](../../../../translated_images/aitk-agent-builder.fb7df60f7923b4d8ba839662bf6d7647e843c01b57256e1e9adecb46a64d3408.sl.png)

1. Open the **AI Toolkit** extension from the **Activity Bar**.
2. In the **Tools** section, select **Agent (Prompt) Builder**. This opens the **Agent (Prompt) Builder** in a new editor tab.
3. Click the **+ New Agent** button. The extension will launch a setup wizard via the **Command Palette**.
4. Enter the name **Calculator Agent** and press **Enter**.
5. In the **Agent (Prompt) Builder**, for the **Model** field, select the **OpenAI GPT-4o (via GitHub)** model.

### -2- Create a system prompt for the agent

With the agent created, it’s time to define its personality and purpose. Here, you’ll use the **Generate system prompt** feature to describe the agent’s intended behavior—in this case, a calculator agent—and have the model write the system prompt for you.

![Screenshot of the "Calculator Agent" interface in the AI Toolkit for Visual Studio Code with a modal window open titled "Generate a prompt." The modal explains that a prompt template can be generated by sharing basic details and includes a text box with the sample system prompt: "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." Below the text box are "Close" and "Generate" buttons. In the background, part of the agent configuration is visible, including the selected model "OpenAI GPT-4o (via GitHub)" and fields for system and user prompts.](../../../../translated_images/aitk-generate-prompt.0d4292407c15282bf714e327f5d3d833389324004135727ef28adc22dbbb4e8f.sl.png)

1. In the **Prompts** section, click the **Generate system prompt** button. This opens the prompt builder which uses AI to create a system prompt for the agent.
2. In the **Generate a prompt** window, enter the following: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
3. Click **Generate**. A notification will appear confirming the system prompt is being generated. When done, the prompt will appear in the **System prompt** field of the **Agent (Prompt) Builder**.
4. Review the **System prompt** and adjust it if needed.

### -3- Create a MCP server

Now that you’ve set your agent’s system prompt—guiding its behavior—it’s time to equip the agent with practical abilities. Here, you’ll create a calculator MCP server with tools to perform addition, subtraction, multiplication, and division. This server lets your agent do real-time math operations in response to natural language prompts.

!["Screenshot of the lower section of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. It shows expandable menus for “Tools” and “Structure output,” along with a dropdown menu labeled “Choose output format” set to “text.” To the right, there is a button labeled “+ MCP Server” for adding a Model Context Protocol server. An image icon placeholder is shown above the Tools section.](../../../../translated_images/aitk-add-mcp-server.9b158809336d87e8076eb5954846040a7370c88046639a09e766398c8855c3d3.sl.png)

AI Toolkit provides templates to simplify creating your own MCP server. We’ll use the Python template to create the calculator MCP server.

*Note*: The AI Toolkit currently supports Python and TypeScript.

1. In the **Tools** section of the **Agent (Prompt) Builder**, click the **+ MCP Server** button. The extension will launch a setup wizard via the **Command Palette**.
2. Select **+ Add Server**.
3. Select **Create a New MCP Server**.
4. Choose **python-weather** as the template.
5. Select **Default folder** to save the MCP server template.
6. Name the server: **Calculator**
7. A new Visual Studio Code window will open. Click **Yes, I trust the authors**.
8. In the terminal (**Terminal** > **New Terminal**), create a virtual environment: `python -m venv .venv`
9. Activate the virtual environment:
    - Windows - `.venv\Scripts\activate`
    - macOS/Linux - `source venv/bin/activate`
10. Install the dependencies: `pip install -e .[dev]`
11. In the **Explorer** view of the **Activity Bar**, expand the **src** folder and open **server.py**.
12. Replace the code in **server.py** with the following and save:

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

Now that your agent has tools, it’s time to use them! Here, you’ll submit prompts to test if the agent uses the right tool from the calculator MCP server.

![Screenshot of the Calculator Agent interface in the AI Toolkit extension for Visual Studio Code. On the left panel, under “Tools,” an MCP server named local-server-calculator_server is added, showing four available tools: add, subtract, multiply, and divide. A badge shows that four tools are active. Below is a collapsed “Structure output” section and a blue “Run” button. On the right panel, under “Model Response,” the agent invokes the multiply and subtract tools with inputs {"a": 3, "b": 25} and {"a": 75, "b": 20} respectively. The final “Tool Response” is shown as 75.0. A “View Code” button appears at the bottom.](../../../../translated_images/aitk-agent-response-with-tools.0f0da2c6eef5eb3f5b7592d6d056449aa8aaa42a3ab0b0c2f14269b3049cfdb5.sl.png)

You will run the calculator MCP server locally using the **Agent Builder** as the MCP client.

1. Press `F5` to start debugging the MCP server. The **Agent (Prompt) Builder** will open in a new editor tab. The status of the server is visible in the terminal.
1. In the **User prompt** field of the **Agent (Prompt) Builder**, enter the following prompt: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. Click the **Run** button to generate the agent's response.
1. Review the agent output. The model should conclude that you paid **$55**.
1. Here's a breakdown of what should occur:
    - The agent selects the **multiply** and **substract** tools to aid in the calculation.
    - The respective `a` and `b` values are assigned for the **multiply** tool.
    - The respective `a` and `b` values are assigned for the **subtract** tool.
    - Each tool’s response appears in the **Tool Response** section.
    - The final output from the model is shown in the **Model Response**.
2. Submit more prompts to further test the agent. Modify the existing prompt in the **User prompt** field by clicking it and replacing the text.
3. When finished testing, stop the server in the **terminal** by pressing **CTRL/CMD+C**.

## Assignment

Try adding a new tool entry to your **server.py** file (for example: return the square root of a number). Submit prompts that require the agent to use your new tool (or existing ones). Remember to restart the server to load the new tools.

## Solution

[Solution](./solution/README.md)

## Key Takeaways

Here are the main points from this chapter:

- The AI Toolkit extension is a great client for consuming MCP Servers and their tools.
- You can add new tools to MCP servers, expanding your agent’s abilities as needs evolve.
- The AI Toolkit includes templates (like Python MCP server templates) that make creating custom tools easier.

## Additional Resources

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## What's Next

Next: [Lesson 4 Practical Implementation](/04-PracticalImplementation/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.