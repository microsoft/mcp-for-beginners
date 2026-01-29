# वेदर MCP सर्वर

यह एक नमूना MCP सर्वर है जो Python में मौसम उपकरणों को मॉक प्रतिक्रियाओं के साथ लागू करता है। इसे आपके अपने MCP सर्वर के लिए एक आधार के रूप में उपयोग किया जा सकता है। इसमें निम्नलिखित विशेषताएं शामिल हैं:

- **वेदर टूल**: एक उपकरण जो दिए गए स्थान के आधार पर मॉक मौसम जानकारी प्रदान करता है।
- **Git Clone Tool**: एक उपकरण जो एक गिट रिपॉजिटरी को निर्दिष्ट फ़ोल्डर में क्लोन करता है।
- **VS Code Open Tool**: एक उपकरण जो VS Code या VS Code Insiders में फ़ोल्डर खोलता है।
- **एजेंट बिल्डर से कनेक्ट करें**: एक सुविधा जो MCP सर्वर को परीक्षण और डिबगिंग के लिए एजेंट बिल्डर से जोड़ने की अनुमति देती है।
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector) में डिबग करें**: एक सुविधा जो MCP सर्वर को MCP Inspector का उपयोग करके डिबग करने की अनुमति देती है।

## वेदर MCP सर्वर टेम्पलेट के साथ शुरुआत करें

> **पूर्व आवश्यकताएँ**
>
> अपने स्थानीय डेवलपमेंट मशीन पर MCP सर्वर चलाने के लिए, आपको आवश्यकता होगी:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repo टूल के लिए आवश्यक)
> - [VS Code](https://code.visualstudio.com/) या [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscode टूल के लिए आवश्यक)
> - (*वैकल्पिक - यदि आप uv पसंद करते हैं*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## पर्यावरण तैयार करें

इस प्रोजेक्ट के लिए पर्यावरण सेटअप करने के दो तरीके हैं। आप अपनी पसंद के अनुसार किसी एक को चुन सकते हैं।

> नोट: वर्चुअल पर्यावरण बनाने के बाद सुनिश्चित करें कि वर्चुअल पर्यावरण का Python उपयोग हो रहा है। इसके लिए VS Code या टर्मिनल को रीलोड करें।

| तरीका | चरण |
| -------- | ----- |
| `uv` का उपयोग करते हुए | 1. वर्चुअल पर्यावरण बनाएं: `uv venv` <br>2. VS Code कमांड "***Python: Select Interpreter***" चलाएं और बनाए गए वर्चुअल पर्यावरण से Python चुनें <br>3. डिपेंडेंसी इंस्टॉल करें (डेवलपमेंट डिपेंडेंसी सहित): `uv pip install -r pyproject.toml --extra dev` |
| `pip` का उपयोग करते हुए | 1. वर्चुअल पर्यावरण बनाएं: `python -m venv .venv` <br>2. VS Code कमांड "***Python: Select Interpreter***" चलाएं और बनाए गए वर्चुअल पर्यावरण से Python चुनें <br>3. डिपेंडेंसी इंस्टॉल करें (डेवलपमेंट डिपेंडेंसी सहित): `pip install -e .[dev]` |

पर्यावरण सेटअप करने के बाद, आप MCP क्लाइंट के रूप में एजेंट बिल्डर के माध्यम से अपने स्थानीय डेवलपमेंट मशीन पर सर्वर चला सकते हैं:
1. VS Code डिबग पैनल खोलें। `Debug in Agent Builder` चुनें या `F5` दबाएं ताकि MCP सर्वर को डिबग करना शुरू करें।
2. AI Toolkit Agent Builder का उपयोग करके [इस प्रॉम्प्ट](../../../../../../../../../../../open_prompt_builder) के साथ सर्वर का परीक्षण करें। सर्वर स्वचालित रूप से एजेंट बिल्डर से कनेक्ट हो जाएगा।
3. प्रॉम्प्ट के साथ सर्वर का परीक्षण करने के लिए `Run` पर क्लिक करें।

**बधाई हो**! आपने सफलतापूर्वक अपने स्थानीय डेवलपमेंट मशीन पर MCP क्लाइंट के रूप में एजेंट बिल्डर के माध्यम से वेदर MCP सर्वर चला लिया है।
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## टेम्पलेट में क्या शामिल है

| फ़ोल्डर / फ़ाइल | सामग्री                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | डिबगिंग के लिए VS Code फाइलें                |
| `.aitk`      | AI Toolkit के लिए कॉन्फ़िगरेशन               |
| `src`        | वेदर MCP सर्वर के लिए स्रोत कोड              |

## वेदर MCP सर्वर को कैसे डिबग करें

> नोट्स:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) MCP सर्वर को परीक्षण और डिबग करने के लिए एक विज़ुअल डेवलपर टूल है।
> - सभी डिबगिंग मोड ब्रेकपॉइंट्स का समर्थन करते हैं, इसलिए आप टूल इम्प्लीमेंटेशन कोड में ब्रेकपॉइंट्स जोड़ सकते हैं।

## उपलब्ध टूल्स

### वेदर टूल
`get_weather` टूल एक निर्दिष्ट स्थान के लिए मॉक मौसम जानकारी प्रदान करता है।

| पैरामीटर | प्रकार | विवरण |
| --------- | ---- | ----------- |
| `location` | string | वह स्थान जिसके लिए मौसम जानकारी चाहिए (जैसे, शहर का नाम, राज्य, या निर्देशांक) |

### Git Clone Tool
`git_clone_repo` टूल एक गिट रिपॉजिटरी को निर्दिष्ट फ़ोल्डर में क्लोन करता है।

| पैरामीटर | प्रकार | विवरण |
| --------- | ---- | ----------- |
| `repo_url` | string | क्लोन करने के लिए गिट रिपॉजिटरी का URL |
| `target_folder` | string | वह फ़ोल्डर जहां रिपॉजिटरी क्लोन की जानी चाहिए |

टूल एक JSON ऑब्जेक्ट लौटाता है जिसमें शामिल हैं:
- `success`: ऑपरेशन सफल हुआ या नहीं, यह बताने वाला बूलियन
- `target_folder` या `error`: क्लोन की गई रिपॉजिटरी का पथ या एक त्रुटि संदेश

### VS Code Open Tool
`open_in_vscode` टूल एक फ़ोल्डर को VS Code या VS Code Insiders एप्लिकेशन में खोलता है।

| पैरामीटर | प्रकार | विवरण |
| --------- | ---- | ----------- |
| `folder_path` | string | वह फ़ोल्डर का पथ जिसे खोलना है |
| `use_insiders` | boolean (वैकल्पिक) | नियमित VS Code के बजाय VS Code Insiders का उपयोग करना है या नहीं |

टूल एक JSON ऑब्जेक्ट लौटाता है जिसमें शामिल हैं:
- `success`: ऑपरेशन सफल हुआ या नहीं, यह बताने वाला बूलियन
- `message` या `error`: एक पुष्टि संदेश या एक त्रुटि संदेश

| डिबग मोड | विवरण | डिबग करने के चरण |
| ---------- | ----------- | --------------- |
| एजेंट बिल्डर | MCP सर्वर को AI Toolkit के माध्यम से एजेंट बिल्डर में डिबग करें। | 1. VS Code डिबग पैनल खोलें। `Debug in Agent Builder` चुनें और `F5` दबाएं ताकि MCP सर्वर को डिबग करना शुरू करें।<br>2. AI Toolkit Agent Builder का उपयोग करके [इस प्रॉम्प्ट](../../../../../../../../../../../open_prompt_builder) के साथ सर्वर का परीक्षण करें। सर्वर स्वचालित रूप से एजेंट बिल्डर से कनेक्ट हो जाएगा।<br>3. प्रॉम्प्ट के साथ सर्वर का परीक्षण करने के लिए `Run` पर क्लिक करें। |
| MCP Inspector | MCP Inspector का उपयोग करके MCP सर्वर को डिबग करें। | 1. [Node.js](https://nodejs.org/) इंस्टॉल करें<br> 2. Inspector सेटअप करें: `cd inspector` && `npm install` <br> 3. VS Code डिबग पैनल खोलें। `Debug SSE in Inspector (Edge)` या `Debug SSE in Inspector (Chrome)` चुनें। `F5` दबाएं ताकि डिबगिंग शुरू हो।<br> 4. जब MCP Inspector ब्राउज़र में लॉन्च हो, तो इस MCP सर्वर को कनेक्ट करने के लिए `Connect` बटन पर क्लिक करें।<br> 5. फिर आप `List Tools` कर सकते हैं, टूल चुन सकते हैं, पैरामीटर इनपुट कर सकते हैं, और `Run Tool` पर क्लिक करके अपने सर्वर कोड को डिबग कर सकते हैं। |

## डिफ़ॉल्ट पोर्ट्स और कस्टमाइज़ेशन

| डिबग मोड | पोर्ट्स | परिभाषाएँ | कस्टमाइज़ेशन | नोट |
| ---------- | ----- | ------------ | -------------- |-------------- |
| एजेंट बिल्डर | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) को संपादित करें ताकि ऊपर दिए गए पोर्ट्स को बदल सकें। | N/A |
| MCP Inspector | 3001 (सर्वर); 5173 और 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) को संपादित करें ताकि ऊपर दिए गए पोर्ट्स को बदल सकें।| N/A |

## फीडबैक

यदि आपके पास इस टेम्पलेट के लिए कोई फीडबैक या सुझाव हैं, तो कृपया [AI Toolkit GitHub रिपॉजिटरी](https://github.com/microsoft/vscode-ai-toolkit/issues) पर एक इश्यू खोलें।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।