# Scenario 3: In-Editor Docs with MCP Server in VS Code

## Overview

In this scenario, you’ll learn how to bring Microsoft Learn Docs directly into your Visual Studio Code environment using the MCP server. Instead of constantly switching browser tabs to look up documentation, you can access, search, and reference official docs right inside your editor. This approach streamlines your workflow, keeps you focused, and enables seamless integration with tools like GitHub Copilot.

- Search and read docs inside VS Code without leaving your coding environment.
- Reference documentation and insert links directly into your README or course files.
- Use GitHub Copilot and MCP together for a smooth, AI-powered documentation workflow.

## Learning Objectives

By the end of this chapter, you’ll know how to set up and use the MCP server within VS Code to enhance your documentation and development workflow. You will be able to:

- Configure your workspace to use the MCP server for documentation lookup.
- Search and insert documentation directly from within VS Code.
- Combine the power of GitHub Copilot and MCP for a more productive, AI-augmented workflow.

These skills will help you stay focused, improve documentation quality, and boost your productivity as a developer or technical writer.

## Solution

To enable in-editor documentation access, you’ll follow a series of steps that integrate the MCP server with VS Code and GitHub Copilot. This solution is ideal for course authors, documentation writers, and developers who want to stay focused in the editor while working with docs and Copilot.

- Quickly add reference links to a README while writing course or project documentation.
- Use Copilot to generate code and MCP to instantly find and cite relevant docs.
- Stay focused in your editor and increase productivity.

### Step-by-Step Guide

To get started, follow these steps. For each step, you can add a screenshot from the assets folder to visually illustrate the process.

1. **Add the MCP configuration:**  
   In your project root, create a `.vscode/mcp.json` file and add the following configuration:  
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```  
   This configuration tells VS Code how to connect to the [`Microsoft Learn Docs MCP server`](https://github.com/MicrosoftDocs/mcp).

   ![Step 1: Add mcp.json to .vscode folder](../../../../../../translated_images/en/step1-mcp-json.c06a007fccc3edfa.webp)
    
2. **Open the GitHub Copilot Chat panel:**  
   If you don’t already have the GitHub Copilot extension installed, go to the Extensions view in VS Code and install it. You can download it directly from the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Then, open the Copilot Chat panel from the sidebar.

   ![Step 2: Open Copilot Chat panel](../../../../../../translated_images/en/step2-copilot-panel.f1cc86e9b9b8cd1a.webp)

3. **Enable agent mode and verify tools:**  
   In the Copilot Chat panel, enable agent mode.

   ![Step 3: Enable agent mode and verify tools](../../../../../../translated_images/en/step3-agent-mode.cdc32520fd7dd1d1.webp)

   After enabling agent mode, check that the MCP server is listed as one of the available tools. This ensures the Copilot agent can access the documentation server to fetch relevant information.

   ![Step 3: Verify MCP server tool](../../../../../../translated_images/en/step3-verify-mcp-tool.76096a6329cbfecd.webp)

4. **Start a new chat and prompt the agent:**  
   Open a new chat in the Copilot Chat panel. You can now ask the agent your documentation questions. The agent will use the MCP server to fetch and display relevant Microsoft Learn documentation directly in your editor.

   - *"I'm trying to write a study plan for topic X. I’m going to study it for 8 weeks; for each week, suggest content I should cover."*

   ![Step 4: Prompt the agent in chat](../../../../../../translated_images/en/step4-prompt-chat.12187bb001605efc.webp)

5. **Live Query:**

   > Let’s look at a live query from the [#get-help](https://discord.gg/D6cRhjHWSC) section in Azure AI Foundry Discord ([view original message](https://discord.com/channels/1113626258182504448/1385498306720829572)):

   *"I’m looking for answers on how to deploy a multi-agent solution with AI agents developed on Azure AI Foundry. I see there’s no direct deployment method like Copilot Studio channels. So, what are the different ways to deploy this so enterprise users can interact and get the job done?  
   There are many articles/blogs suggesting we can use Azure Bot service as a bridge between MS Teams and Azure AI Foundry Agents. Will this work if I set up an Azure bot that connects to the Orchestrator Agent on Azure AI Foundry via Azure Function to handle orchestration? Or do I need to create an Azure Function for each AI agent in the multi-agent solution to manage orchestration at the Bot Framework level? Any other suggestions are welcome."*

   ![Step 5: Live queries](../../../../../../translated_images/en/step5-live-queries.49db3e4a50bea273.webp)

   The agent will respond with relevant documentation links and summaries, which you can then insert directly into your markdown files or use as references in your code.

### Sample Queries

Here are some example queries you can try. These will show how the MCP server and Copilot work together to provide instant, context-aware documentation and references without leaving VS Code:

- "Show me how to use Azure Functions triggers."
- "Insert a link to the official documentation for Azure Key Vault."
- "What are the best practices for securing Azure resources?"
- "Find a quickstart for Azure AI services."

These queries demonstrate how the MCP server and Copilot can work together to provide instant, context-aware documentation and references without leaving VS Code.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.