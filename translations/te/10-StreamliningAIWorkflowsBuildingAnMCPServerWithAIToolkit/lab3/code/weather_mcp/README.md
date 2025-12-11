<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "999c5e7623c1e2d5e5a07c2feb39eb67",
  "translation_date": "2025-12-11T17:01:49+00:00",
  "source_file": "10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md",
  "language_code": "te"
}
-->
# వాతావరణ MCP సర్వర్

ఇది మాక్ ప్రతిస్పందనలతో వాతావరణ సాధనాలను అమలు చేసే Python లో ఒక నమూనా MCP సర్వర్. ఇది మీ స్వంత MCP సర్వర్ కోసం ఒక మౌలిక నిర్మాణంగా ఉపయోగించవచ్చు. ఇది క్రింది లక్షణాలను కలిగి ఉంది:

- **వాతావరణ సాధనం**: ఇచ్చిన స్థానం ఆధారంగా మాక్ చేసిన వాతావరణ సమాచారాన్ని అందించే సాధనం.
- **ఏజెంట్ బిల్డర్‌కు కనెక్ట్ అవ్వడం**: పరీక్ష మరియు డీబగ్గింగ్ కోసం MCP సర్వర్‌ను ఏజెంట్ బిల్డర్‌కు కనెక్ట్ చేయడానికి ఒక లక్షణం.
- **[MCP ఇన్స్పెక్టర్](https://github.com/modelcontextprotocol/inspector)లో డీబగ్ చేయడం**: MCP ఇన్స్పెక్టర్ ఉపయోగించి MCP సర్వర్‌ను డీబగ్ చేయడానికి ఒక లక్షణం.

## వాతావరణ MCP సర్వర్ టెంప్లేట్‌తో ప్రారంభించండి

> **ముందస్తు అవసరాలు**
>
> మీ స్థానిక డెవ్ మెషీన్‌లో MCP సర్వర్‌ను నడపడానికి, మీరు అవసరం:
>
> - [Python](https://www.python.org/)
> - (*ఐచ్ఛికం - మీరు uv ఇష్టపడితే*) [uv](https://github.com/astral-sh/uv)
> - [Python డీబగ్గర్ ఎక్స్‌టెన్షన్](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## పరిసరాన్ని సిద్ధం చేయండి

ఈ ప్రాజెక్ట్ కోసం పరిసరాన్ని సెట్ చేయడానికి రెండు విధానాలు ఉన్నాయి. మీ ఇష్టానుసారం ఏదైనా ఒకదాన్ని ఎంచుకోవచ్చు.

> గమనిక: వర్చువల్ పరిసరాన్ని సృష్టించిన తర్వాత వర్చువల్ పరిసరపు python ఉపయోగించబడుతున్నదని నిర్ధారించడానికి VSCode లేదా టెర్మినల్‌ను రీలోడ్ చేయండి.

| విధానం | దశలు |
| -------- | ----- |
| `uv` ఉపయోగించడం | 1. వర్చువల్ పరిసరాన్ని సృష్టించండి: `uv venv` <br>2. VSCode కమాండ్ "***Python: Select Interpreter***" నడిపించి సృష్టించిన వర్చువల్ పరిసరపు python ను ఎంచుకోండి <br>3. డిపెండెన్సీలు (డెవ్ డిపెండెన్సీలను కూడా కలుపుకొని) ఇన్‌స్టాల్ చేయండి: `uv pip install -r pyproject.toml --extra dev` |
| `pip` ఉపయోగించడం | 1. వర్చువల్ పరిసరాన్ని సృష్టించండి: `python -m venv .venv` <br>2. VSCode కమాండ్ "***Python: Select Interpreter***" నడిపించి సృష్టించిన వర్చువల్ పరిసరపు python ను ఎంచుకోండి<br>3. డిపెండెన్సీలు (డెవ్ డిపెండెన్సీలను కూడా కలుపుకొని) ఇన్‌స్టాల్ చేయండి: `pip install -e .[dev]` |

పరిసరాన్ని సెట్ చేసిన తర్వాత, మీరు Agent Builder ద్వారా MCP క్లయింట్‌గా మీ స్థానిక డెవ్ మెషీన్‌లో సర్వర్‌ను నడపవచ్చు:
1. VS Code డీబగ్ ప్యానెల్‌ను తెరవండి. `Debug in Agent Builder` ఎంచుకుని లేదా `F5` నొక్కి MCP సర్వర్ డీబగ్గింగ్ ప్రారంభించండి.
2. AI Toolkit Agent Builder ఉపయోగించి [ఈ ప్రాంప్ట్](../../../../../../../../../../../../open_prompt_builder)తో సర్వర్‌ను పరీక్షించండి. సర్వర్ ఆటోమేటిక్‌గా ఏజెంట్ బిల్డర్‌కు కనెక్ట్ అవుతుంది.
3. ప్రాంప్ట్‌తో సర్వర్‌ను పరీక్షించడానికి `Run` క్లిక్ చేయండి.

**అభినందనలు**! మీరు Agent Builder ద్వారా MCP క్లయింట్‌గా మీ స్థానిక డెవ్ మెషీన్‌లో విజయవంతంగా వాతావరణ MCP సర్వర్‌ను నడిపారు.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## టెంప్లేట్‌లో ఏమి ఉంది

| ఫోల్డర్ / ఫైల్| విషయాలు                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | డీబగ్గింగ్ కోసం VSCode ఫైళ్లు                   |
| `.aitk`      | AI Toolkit కోసం కాన్ఫిగరేషన్లు                |
| `src`        | వాతావరణ MCP సర్వర్ కోసం సోర్స్ కోడ్            |

## వాతావరణ MCP సర్వర్‌ను ఎలా డీబగ్ చేయాలి

> గమనికలు:
> - [MCP ఇన్స్పెక్టర్](https://github.com/modelcontextprotocol/inspector) MCP సర్వర్లను పరీక్షించడానికి మరియు డీబగ్గింగ్ చేయడానికి ఒక విజువల్ డెవలపర్ సాధనం.
> - అన్ని డీబగ్గింగ్ మోడ్‌లు బ్రేక్‌పాయింట్లను మద్దతు ఇస్తాయి, కాబట్టి మీరు సాధనం అమలు కోడ్‌లో బ్రేక్‌పాయింట్లు జోడించవచ్చు.

| డీబగ్ మోడ్ | వివరణ | డీబగ్ దశలు |
| ---------- | ----------- | --------------- |
| ఏజెంట్ బిల్డర్ | AI Toolkit ద్వారా ఏజెంట్ బిల్డర్‌లో MCP సర్వర్‌ను డీబగ్ చేయండి. | 1. VS Code డీబగ్ ప్యానెల్‌ను తెరవండి. `Debug in Agent Builder` ఎంచుకుని `F5` నొక్కి MCP సర్వర్ డీబగ్గింగ్ ప్రారంభించండి.<br>2. AI Toolkit Agent Builder ఉపయోగించి [ఈ ప్రాంప్ట్](../../../../../../../../../../../../open_prompt_builder)తో సర్వర్‌ను పరీక్షించండి. సర్వర్ ఆటోమేటిక్‌గా ఏజెంట్ బిల్డర్‌కు కనెక్ట్ అవుతుంది.<br>3. ప్రాంప్ట్‌తో సర్వర్‌ను పరీక్షించడానికి `Run` క్లిక్ చేయండి. |
| MCP ఇన్స్పెక్టర్ | MCP ఇన్స్పెక్టర్ ఉపయోగించి MCP సర్వర్‌ను డీబగ్ చేయండి. | 1. [Node.js](https://nodejs.org/) ఇన్‌స్టాల్ చేయండి<br> 2. ఇన్స్పెక్టర్ సెట్ చేయండి: `cd inspector` && `npm install` <br> 3. VS Code డీబగ్ ప్యానెల్‌ను తెరవండి. `Debug SSE in Inspector (Edge)` లేదా `Debug SSE in Inspector (Chrome)` ఎంచుకోండి. డీబగ్గింగ్ ప్రారంభించడానికి F5 నొక్కండి.<br> 4. MCP ఇన్స్పెక్టర్ బ్రౌజర్‌లో ప్రారంభమైనప్పుడు, ఈ MCP సర్వర్‌ను కనెక్ట్ చేయడానికి `Connect` బటన్ క్లిక్ చేయండి.<br> 5. ఆపై మీరు `List Tools` చేయవచ్చు, ఒక సాధనం ఎంచుకోండి, పారామితులు ఇన్పుట్ చేయండి, మరియు `Run Tool` ద్వారా మీ సర్వర్ కోడ్‌ను డీబగ్ చేయండి.<br> |

## డిఫాల్ట్ పోర్టులు మరియు అనుకూలీకరణలు

| డీబగ్ మోడ్ | పోర్టులు | నిర్వచనాలు | అనుకూలీకరణలు | గమనిక |
| ---------- | ----- | ------------ | -------------- |-------------- |
| ఏజెంట్ బిల్డర్ | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | పై పోర్టులను మార్చడానికి [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) సవరించండి. | వర్తించదు |
| MCP ఇన్స్పెక్టర్ | 3001 (సర్వర్); 5173 మరియు 3000 (ఇన్స్పెక్టర్) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | పై పోర్టులను మార్చడానికి [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) సవరించండి.| వర్తించదు |

## అభిప్రాయం

ఈ టెంప్లేట్ గురించి మీకు ఏవైనా అభిప్రాయాలు లేదా సూచనలు ఉంటే, దయచేసి [AI Toolkit GitHub రిపోజిటరీ](https://github.com/microsoft/vscode-ai-toolkit/issues)లో ఒక ఇష్యూ తెరవండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->