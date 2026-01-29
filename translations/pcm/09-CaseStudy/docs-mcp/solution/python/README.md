# Study Plan Generator wit Chainlit & Microsoft Learn Docs MCP

## Wetin You Go Need

- Python 3.8 or higher
- pip (Python package manager)
- Internet wey go connect to di Microsoft Learn Docs MCP server

## How to Install Am

1. Clone dis repository or download di project files.
2. Install di things wey di app need:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use Am

### Scenario 1: Simple Query to Docs MCP
Dis na command-line client wey go connect to di Docs MCP server, send query, and show di result.

1. Run di script:
   ```bash
   python scenario1.py
   ```
2. Type di question wey you get for di documentation for di prompt.

### Scenario 2: Study Plan Generator (Chainlit Web App)
Dis na web-based interface (wey dey use Chainlit) wey go allow you create personal week-by-week study plan for any technical topic.

1. Start di Chainlit app:
   ```bash
   chainlit run scenario2.py
   ```
2. Open di local URL wey go show for your terminal (e.g., http://localhost:8000) for your browser.
3. For di chat window, type di study topic and how many weeks you wan take study am (e.g., "AI-900 certification, 8 weeks").
4. Di app go reply you wit week-by-week study plan, wit links to di Microsoft Learn documentation wey relate to di topic.

**Environment Variables We You Go Need:**

To use Scenario 2 (di Chainlit web app wit Azure OpenAI), you go need set di following environment variables for `.env` file inside di `python` directory:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Put di values wey match your Azure OpenAI resource details before you run di app.

> [!TIP]
> E easy to deploy your own models wit [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: In-Editor Docs wit MCP Server for VS Code

Instead of dey switch browser tabs to find documentation, you fit bring Microsoft Learn Docs enter VS Code directly wit di MCP server. Dis go allow you:
- Search and read docs inside VS Code without comot from your coding environment.
- Add documentation links directly to your README or course files.
- Use GitHub Copilot and MCP together for smooth, AI-powered documentation workflow.

**Example Use Cases:**
- Quickly add reference links to README while you dey write course or project documentation.
- Use Copilot to generate code and MCP to find and add relevant docs fast.
- Stay focused for your editor and increase productivity.

> [!IMPORTANT]
> Make sure say you get valid [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration for your workspace (di location na `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit na modern open-source framework wey dem design to build conversational web applications. E make am easy to create chat-based user interfaces wey dey connect to backend services like di Microsoft Learn Docs MCP server. Dis project dey use Chainlit to provide simple, interactive way to create personal study plans for real time. Wit Chainlit, you fit quickly build and deploy chat-based tools wey go help productivity and learning.

## Wetin Dis App Dey Do

Dis app dey allow users create personal study plan by just typing di topic and di time wey dem wan take. Di app go read wetin you type, query di Microsoft Learn Docs MCP server for di content wey relate to am, and arrange di results into structured, week-by-week plan. Each week recommendation go show for di chat, so e go dey easy to follow and track your progress. Di integration go make sure say you dey always get di latest and most relevant learning resources.

## Sample Queries

Try dis queries for di chat window to see how di app go respond:

- `AI-900 certification, 8 weeks`
- `Learn Azure Functions, 4 weeks`
- `Azure DevOps, 6 weeks`
- `Data engineering on Azure, 10 weeks`
- `Microsoft security fundamentals, 5 weeks`
- `Power Platform, 7 weeks`
- `Azure AI services, 12 weeks`
- `Cloud architecture, 9 weeks`

Dis examples dey show how flexible di app be for different learning goals and timeframes.

## References

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important mata, na beta make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->