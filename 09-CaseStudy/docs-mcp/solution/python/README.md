# Study Plan Generator with Chainlit & Microsoft Learn Docs MCP

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Internet access to connect to the Microsoft Learn Docs MCP server

## Installation

1. Clone this repository or download the project files.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** `chainlit` and `semantic-kernel` don't support the MCP Python SDK 2.x yet (both require `mcp<2`), so this case study pins `mcp>=1.30.0,<2` and uses the 1.x client API. In 1.x, `streamable_http_client` yields three values (`read_stream, write_stream, get_session_id`); in 2.x it yields only two.

## Usage

### Scenario 1: Simple Query to Docs MCP
A command-line client that connects to the Docs MCP server, sends a query, and prints the result.

1. Run the script:
   ```bash
   python scenario1.py
   ```
2. Enter your documentation question at the prompt.

### Scenario 2: Study Plan Generator (Chainlit Web App)
A web-based interface (using Chainlit) that allows users to generate a personalized, week-by-week study plan for any technical topic.

1. Start the Chainlit app:
   ```bash
   chainlit run scenario2.py
   ```
2. Open the local URL provided in your terminal (e.g., http://localhost:8000) in your browser.
3. In the chat window, enter your study topic and the number of weeks you want to study (e.g., "AI-900 certification, 8 weeks").
4. The app will respond with a week-by-week study plan, including links to relevant Microsoft Learn documentation.

**Environment Variables Required:**

To use Scenario 2 (the Chainlit web app with Azure OpenAI), you must set the following environment variables in a `.env` file in the `python` directory:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Fill in these values with your Azure OpenAI resource details before running the app.

> [!TIP]
> You can easily deploy your own models using [Microsoft Foundry](https://ai.azure.com/).

### Scenario 3: In-Editor Docs with MCP Server in VS Code

Instead of switching browser tabs to search documentation, you can bring Microsoft Learn Docs directly into your VS Code using the MCP server. This enables you to:
- Search and read docs inside VS Code without leaving your coding environment.
- Reference documentation and insert links directly into your README or course files.
- Use GitHub Copilot and MCP together for a seamless, AI-powered documentation workflow.

**Example Use Cases:**
- Quickly add reference links to a README while writing a course or project documentation.
- Use Copilot to generate code and MCP to instantly find and cite relevant docs.
- Stay focused in your editor and boost productivity.

> [!IMPORTANT]
> Ensure you have a valid [`mcp.json`](../scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit is a modern open-source framework for building conversational web applications. It makes it easy to create chat-based user interfaces that connect to backend services like the Microsoft Learn Docs MCP server. This project uses Chainlit to provide a simple, interactive way to generate personalized study plans in real time. By leveraging Chainlit, you can quickly build and deploy chat-based tools that enhance productivity and learning.

## What This Does

This app allows users to create a personalized study plan by simply entering a topic and a duration. The app parses your input, queries the Microsoft Learn Docs MCP server for relevant content, and organizes the results into a structured, week-by-week plan. Each week’s recommendations are displayed in the chat, making it easy to follow and track your progress. The integration ensures you always get the latest, most relevant learning resources.

## Sample Queries

Try these queries in the chat window to see how the app responds:

- `AI-900 certification, 8 weeks`
- `Learn Azure Functions, 4 weeks`
- `Azure DevOps, 6 weeks`
- `Data engineering on Azure, 10 weeks`
- `Microsoft security fundamentals, 5 weeks`
- `Power Platform, 7 weeks`
- `Azure AI services, 12 weeks`
- `Cloud architecture, 9 weeks`

These examples demonstrate the flexibility of the app for different learning goals and timeframes.

## References

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)
