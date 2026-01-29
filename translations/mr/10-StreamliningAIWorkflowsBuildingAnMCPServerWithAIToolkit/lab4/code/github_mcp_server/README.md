# Weather MCP Server

हा Python मध्ये तयार केलेला एक नमुना MCP Server आहे जो हवामान साधनांसह mock प्रतिसाद प्रदान करतो. तुम्ही तुमच्या स्वतःच्या MCP Server साठी याचा वापर करू शकता. यात खालील वैशिष्ट्ये समाविष्ट आहेत:

- **Weather Tool**: दिलेल्या स्थानावर आधारित mock हवामान माहिती प्रदान करणारे साधन.
- **Git Clone Tool**: git रिपॉझिटरी एका निर्दिष्ट फोल्डरमध्ये क्लोन करणारे साधन.
- **VS Code Open Tool**: VS Code किंवा VS Code Insiders मध्ये फोल्डर उघडणारे साधन.
- **Agent Builder शी कनेक्ट करा**: MCP Server ला Agent Builder शी जोडण्यासाठी चाचणी आणि डीबगिंगसाठी एक वैशिष्ट्य.
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector) मध्ये डीबग करा**: MCP Inspector वापरून MCP Server डीबग करण्याचे एक वैशिष्ट्य.

## Weather MCP Server टेम्पलेटसह सुरुवात करा

> **पूर्वअटी**
>
> तुमच्या स्थानिक डेव्हलपमेंट मशीनवर MCP Server चालवण्यासाठी तुम्हाला आवश्यक आहे:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repo साधनासाठी आवश्यक)
> - [VS Code](https://code.visualstudio.com/) किंवा [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscode साधनासाठी आवश्यक)
> - (*पर्यायी - जर तुम्हाला uv हवे असेल*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## वातावरण तयार करा

या प्रकल्पासाठी वातावरण सेट करण्यासाठी दोन पद्धती आहेत. तुम्ही तुमच्या पसंतीनुसार कोणतीही निवडू शकता.

> टीप: व्हर्च्युअल वातावरण तयार केल्यानंतर व्हर्च्युअल वातावरणातील Python वापरला जात आहे याची खात्री करण्यासाठी VSCode किंवा टर्मिनल रीलोड करा.

| पद्धत | चरण |
| -------- | ----- |
| `uv` वापरून | 1. व्हर्च्युअल वातावरण तयार करा: `uv venv` <br>2. VSCode कमांड "***Python: Select Interpreter***" चालवा आणि तयार केलेल्या व्हर्च्युअल वातावरणातील Python निवडा <br>3. dependencies (dev dependencies सह) इंस्टॉल करा: `uv pip install -r pyproject.toml --extra dev` |
| `pip` वापरून | 1. व्हर्च्युअल वातावरण तयार करा: `python -m venv .venv` <br>2. VSCode कमांड "***Python: Select Interpreter***" चालवा आणि तयार केलेल्या व्हर्च्युअल वातावरणातील Python निवडा <br>3. dependencies (dev dependencies सह) इंस्टॉल करा: `pip install -e .[dev]` |

वातावरण सेट केल्यानंतर, MCP Client म्हणून Agent Builder वापरून स्थानिक डेव्हलपमेंट मशीनवर सर्व्हर चालवू शकता:
1. VS Code Debug पॅनेल उघडा. `Debug in Agent Builder` निवडा किंवा `F5` दाबा MCP Server डीबगिंग सुरू करण्यासाठी.
2. AI Toolkit Agent Builder वापरून [या प्रॉम्प्टसह](../../../../../../../../../../../open_prompt_builder) सर्व्हर चाचणी करा. सर्व्हर आपोआप Agent Builder शी कनेक्ट होईल.
3. `Run` क्लिक करा प्रॉम्प्टसह सर्व्हर चाचणी करण्यासाठी.

**अभिनंदन**! तुम्ही यशस्वीरित्या Weather MCP Server तुमच्या स्थानिक डेव्हलपमेंट मशीनवर Agent Builder वापरून MCP Client म्हणून चालवला आहे.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## टेम्पलेटमध्ये काय समाविष्ट आहे

| फोल्डर / फाइल | सामग्री                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode डीबगिंगसाठी फाइल्स                   |
| `.aitk`      | AI Toolkit साठी कॉन्फिगरेशन्स                |
| `src`        | Weather MCP Server साठी स्रोत कोड            |

## Weather MCP Server कसा डीबग करावा

> टीप:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) हे MCP Server चाचणी आणि डीबगिंगसाठी व्हिज्युअल डेव्हलपर टूल आहे.
> - सर्व डीबगिंग मोड्स ब्रेकपॉइंट्सला सपोर्ट करतात, त्यामुळे तुम्ही टूल इम्प्लिमेंटेशन कोडमध्ये ब्रेकपॉइंट्स जोडू शकता.

## उपलब्ध साधने

### Weather Tool
`get_weather` टूल दिलेल्या स्थानासाठी mock हवामान माहिती प्रदान करते.

| पॅरामीटर | प्रकार | वर्णन |
| --------- | ---- | ----------- |
| `location` | string | हवामान मिळवण्यासाठी स्थान (उदा. शहराचे नाव, राज्य, किंवा समन्वय) |

### Git Clone Tool
`git_clone_repo` टूल git रिपॉझिटरी एका निर्दिष्ट फोल्डरमध्ये क्लोन करते.

| पॅरामीटर | प्रकार | वर्णन |
| --------- | ---- | ----------- |
| `repo_url` | string | क्लोन करण्यासाठी git रिपॉझिटरीचा URL |
| `target_folder` | string | रिपॉझिटरी क्लोन करण्यासाठी फोल्डरचा पथ |

टूल JSON ऑब्जेक्ट परत करते ज्यामध्ये:
- `success`: ऑपरेशन यशस्वी झाले का हे दर्शवणारा Boolean
- `target_folder` किंवा `error`: क्लोन केलेल्या रिपॉझिटरीचा पथ किंवा एरर मेसेज

### VS Code Open Tool
`open_in_vscode` टूल VS Code किंवा VS Code Insiders अॅप्लिकेशनमध्ये फोल्डर उघडते.

| पॅरामीटर | प्रकार | वर्णन |
| --------- | ---- | ----------- |
| `folder_path` | string | उघडण्यासाठी फोल्डरचा पथ |
| `use_insiders` | boolean (पर्यायी) | नियमित VS Code ऐवजी VS Code Insiders वापरायचे आहे का |

टूल JSON ऑब्जेक्ट परत करते ज्यामध्ये:
- `success`: ऑपरेशन यशस्वी झाले का हे दर्शवणारा Boolean
- `message` किंवा `error`: पुष्टीकरण संदेश किंवा एरर मेसेज

| डीबग मोड | वर्णन | डीबग करण्याचे चरण |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkit वापरून Agent Builder मध्ये MCP Server डीबग करा. | 1. VS Code Debug पॅनेल उघडा. `Debug in Agent Builder` निवडा आणि `F5` दाबा MCP Server डीबगिंग सुरू करण्यासाठी.<br>2. AI Toolkit Agent Builder वापरून [या प्रॉम्प्टसह](../../../../../../../../../../../open_prompt_builder) सर्व्हर चाचणी करा. सर्व्हर आपोआप Agent Builder शी कनेक्ट होईल.<br>3. `Run` क्लिक करा प्रॉम्प्टसह सर्व्हर चाचणी करण्यासाठी. |
| MCP Inspector | MCP Inspector वापरून MCP Server डीबग करा. | 1. [Node.js](https://nodejs.org/) इंस्टॉल करा<br> 2. Inspector सेट करा: `cd inspector` && `npm install` <br> 3. VS Code Debug पॅनेल उघडा. `Debug SSE in Inspector (Edge)` किंवा `Debug SSE in Inspector (Chrome)` निवडा. `F5` दाबा डीबगिंग सुरू करण्यासाठी.<br> 4. MCP Inspector ब्राउझरमध्ये लॉन्च झाल्यावर, MCP Server शी कनेक्ट करण्यासाठी `Connect` बटण क्लिक करा.<br> 5. नंतर तुम्ही `List Tools` करू शकता, टूल निवडा, पॅरामीटर्स इनपुट करा, आणि `Run Tool` क्लिक करून तुमचा सर्व्हर कोड डीबग करा.<br> |

## डिफॉल्ट पोर्ट्स आणि सानुकूलने

| डीबग मोड | पोर्ट्स | व्याख्या | सानुकूलने | टीप |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) संपादित करा वरील पोर्ट्स बदलण्यासाठी. | N/A |
| MCP Inspector | 3001 (Server); 5173 आणि 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) संपादित करा वरील पोर्ट्स बदलण्यासाठी.| N/A |

## अभिप्राय

जर तुम्हाला या टेम्पलेटसाठी काही अभिप्राय किंवा सूचना असतील, तर कृपया [AI Toolkit GitHub रिपॉझिटरी](https://github.com/microsoft/vscode-ai-toolkit/issues) वर एक इश्यू उघडा.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.