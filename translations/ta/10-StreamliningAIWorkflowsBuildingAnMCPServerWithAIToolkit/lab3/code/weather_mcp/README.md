# வானிலை MCP சர்வர்

Python-இல் உருவாக்கப்பட்ட ஒரு மாதிரி MCP சர்வர் இது, mock பதில்களுடன் வானிலை கருவிகளை செயல்படுத்துகிறது. உங்கள் சொந்த MCP சர்வருக்கான அடிப்படையாக இதை பயன்படுத்தலாம். இதில் பின்வரும் அம்சங்கள் அடங்கும்:

- **வானிலை கருவி**: கொடுக்கப்பட்ட இடத்தின் அடிப்படையில் mock வானிலை தகவல்களை வழங்கும் ஒரு கருவி.
- **Agent Builder-இன் இணைப்பு**: MCP சர்வரை Agent Builder-க்கு இணைத்து சோதனை மற்றும் பிழைதிருத்தம் செய்ய உதவும் ஒரு அம்சம்.
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)-இல் பிழைதிருத்தம்**: MCP Inspector-ஐ பயன்படுத்தி MCP சர்வரை பிழைதிருத்தம் செய்ய உதவும் ஒரு அம்சம்.

## Weather MCP Server டெம்ப்ளேட்டுடன் தொடங்குங்கள்

> **முன்னேற்பாடுகள்**
>
> உங்கள் உள்ளூர் டெவலப்பிங் இயந்திரத்தில் MCP சர்வரை இயக்க, உங்களுக்கு தேவையானவை:
>
> - [Python](https://www.python.org/)
> - (*விருப்பம் - uv பயன்படுத்த விரும்பினால்*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## சூழலை தயாரிக்கவும்

இந்த திட்டத்திற்கான சூழலை அமைக்க இரண்டு முறைகள் உள்ளன. உங்கள் விருப்பத்தின் அடிப்படையில் ஒன்றைத் தேர்ந்தெடுக்கலாம்.

> குறிப்பு: மெய்நிகர் சூழல் Python பயன்படுத்தப்படுவதை உறுதிப்படுத்த VSCode அல்லது terminal-ஐ மீண்டும் ஏற்றவும்.

| முறை | படிகள் |
| -------- | ----- |
| `uv` பயன்படுத்துதல் | 1. மெய்நிகர் சூழலை உருவாக்கவும்: `uv venv` <br>2. VSCode கட்டளையை இயக்கவும் "***Python: Select Interpreter***" மற்றும் உருவாக்கப்பட்ட மெய்நிகர் சூழலிலிருந்து Python-ஐ தேர்ந்தெடுக்கவும் <br>3. சார்புகளை நிறுவவும் (டெவலப்பிங் சார்புகளை உட்பட): `uv pip install -r pyproject.toml --extra dev` |
| `pip` பயன்படுத்துதல் | 1. மெய்நிகர் சூழலை உருவாக்கவும்: `python -m venv .venv` <br>2. VSCode கட்டளையை இயக்கவும் "***Python: Select Interpreter***" மற்றும் உருவாக்கப்பட்ட மெய்நிகர் சூழலிலிருந்து Python-ஐ தேர்ந்தெடுக்கவும்<br>3. சார்புகளை நிறுவவும் (டெவலப்பிங் சார்புகளை உட்பட): `pip install -e .[dev]` | 

சூழலை அமைத்த பிறகு, MCP Client ஆக Agent Builder மூலம் உங்கள் உள்ளூர் டெவலப்பிங் இயந்திரத்தில் சர்வரை இயக்கலாம்:
1. VS Code Debug panel-ஐ திறக்கவும். `Debug in Agent Builder`-ஐ தேர்ந்தெடுக்கவும் அல்லது `F5` அழுத்தி MCP சர்வரை பிழைதிருத்தம் செய்ய தொடங்கவும்.
2. AI Toolkit Agent Builder-ஐ பயன்படுத்தி [இந்த prompt](../../../../../../../../../../../open_prompt_builder)-ஐ MCP சர்வரை சோதிக்க பயன்படுத்தவும். சர்வர் தானாக Agent Builder-க்கு இணைக்கப்படும்.
3. `Run` அழுத்தி prompt-ஐ பயன்படுத்தி சர்வரை சோதிக்கவும்.

**வாழ்த்துக்கள்**! Agent Builder மூலம் MCP Client ஆக உங்கள் உள்ளூர் டெவலப்பிங் இயந்திரத்தில் Weather MCP Server-ஐ வெற்றிகரமாக இயக்கியுள்ளீர்கள்.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## டெம்ப்ளேட்டில் என்ன அடங்கியுள்ளது

| கோப்புறை / கோப்பு | உள்ளடக்கம்                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | பிழைதிருத்தத்திற்கான VSCode கோப்புகள்                   |
| `.aitk`      | AI Toolkit-க்கான கட்டமைப்புகள்                |
| `src`        | Weather MCP Server-க்கான மூலக் குறியீடு   |

## Weather MCP Server-ஐ பிழைதிருத்துவது எப்படி

> குறிப்புகள்:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) என்பது MCP சர்வர்களை சோதிக்க மற்றும் பிழைதிருத்தம் செய்ய உதவும் ஒரு காட்சி டெவலப்பர் கருவி.
> - அனைத்து பிழைதிருத்த முறைகளும் breakpoints-ஐ ஆதரிக்கின்றன, எனவே கருவி செயல்பாட்டு குறியீட்டில் breakpoints சேர்க்கலாம்.

| பிழைதிருத்த முறை | விளக்கம் | பிழைதிருத்த படிகள் |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkit மூலம் MCP சர்வரை Agent Builder-இல் பிழைதிருத்தம் செய்யவும். | 1. VS Code Debug panel-ஐ திறக்கவும். `Debug in Agent Builder`-ஐ தேர்ந்தெடுக்கவும் மற்றும் `F5` அழுத்தி MCP சர்வரை பிழைதிருத்தம் செய்ய தொடங்கவும்.<br>2. AI Toolkit Agent Builder-ஐ பயன்படுத்தி [இந்த prompt](../../../../../../../../../../../open_prompt_builder)-ஐ MCP சர்வரை சோதிக்க பயன்படுத்தவும். சர்வர் தானாக Agent Builder-க்கு இணைக்கப்படும்.<br>3. `Run` அழுத்தி prompt-ஐ பயன்படுத்தி சர்வரை சோதிக்கவும். |
| MCP Inspector | MCP Inspector-ஐ பயன்படுத்தி MCP சர்வரை பிழைதிருத்தம் செய்யவும். | 1. [Node.js](https://nodejs.org/) நிறுவவும்<br> 2. Inspector-ஐ அமைக்கவும்: `cd inspector` && `npm install` <br> 3. VS Code Debug panel-ஐ திறக்கவும். `Debug SSE in Inspector (Edge)` அல்லது `Debug SSE in Inspector (Chrome)`-ஐ தேர்ந்தெடுக்கவும். `F5` அழுத்தி பிழைதிருத்தம் செய்ய தொடங்கவும்.<br> 4. MCP Inspector உலாவியில் தொடங்கும்போது, இந்த MCP சர்வரை இணைக்க `Connect` பொத்தானை அழுத்தவும்.<br> 5. பின்னர் `List Tools`-ஐ தேர்ந்தெடுக்கவும், ஒரு கருவியை தேர்ந்தெடுக்கவும், அளவுருக்களை உள்ளிடவும், மற்றும் `Run Tool`-ஐ அழுத்தி உங்கள் சர்வர் குறியீட்டை பிழைதிருத்தவும்.<br> |

## இயல்புநிலை Ports மற்றும் தனிப்பயனாக்கங்கள்

| பிழைதிருத்த முறை | Ports | வரையறைகள் | தனிப்பயனாக்கங்கள் | குறிப்பு |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json)-ஐ திருத்தி மேலே உள்ள ports-ஐ மாற்றவும். | N/A |
| MCP Inspector | 3001 (Server); 5173 மற்றும் 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json)-ஐ திருத்தி மேலே உள்ள ports-ஐ மாற்றவும்.| N/A |

## கருத்துகள்

இந்த டெம்ப்ளேட்டிற்கான உங்கள் கருத்துகள் அல்லது பரிந்துரைகள் இருந்தால், [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)-இல் ஒரு issue-ஐ திறக்கவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.