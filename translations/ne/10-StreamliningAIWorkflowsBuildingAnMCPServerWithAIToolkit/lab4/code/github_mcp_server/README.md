# मौसम MCP सर्भर

यो Python मा लेखिएको एक नमूना MCP सर्भर हो जसले मौसम उपकरणहरूलाई नकली प्रतिक्रिया सहित कार्यान्वयन गर्दछ। यसलाई तपाईंको आफ्नै MCP सर्भरको लागि आधारको रूपमा प्रयोग गर्न सकिन्छ। यसमा निम्न सुविधाहरू समावेश छन्:

- **मौसम उपकरण**: दिइएको स्थानको आधारमा नकली मौसम जानकारी प्रदान गर्ने उपकरण।
- **Git Clone उपकरण**: एक उपकरण जसले git रिपोजिटरीलाई निर्दिष्ट फोल्डरमा क्लोन गर्दछ।
- **VS Code Open उपकरण**: एक उपकरण जसले फोल्डरलाई VS Code वा VS Code Insiders मा खोल्छ।
- **एजेन्ट बिल्डरसँग जडान गर्नुहोस्**: MCP सर्भरलाई परीक्षण र डिबग गर्न Agent Builder सँग जडान गर्ने सुविधा।
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector) मा डिबग गर्नुहोस्**: MCP Inspector प्रयोग गरेर MCP सर्भरलाई डिबग गर्ने सुविधा।

## मौसम MCP सर्भर टेम्प्लेटसँग सुरु गर्नुहोस्

> **पूर्वापेक्षाहरू**
>
> तपाईंको स्थानीय विकास मेसिनमा MCP सर्भर चलाउनको लागि, तपाईंलाई निम्न आवश्यक हुनेछ:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repo उपकरणको लागि आवश्यक)
> - [VS Code](https://code.visualstudio.com/) वा [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscode उपकरणको लागि आवश्यक)
> - (*वैकल्पिक - यदि तपाईं uv प्रयोग गर्न चाहनुहुन्छ*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## वातावरण तयार गर्नुहोस्

यस परियोजनाको लागि वातावरण सेटअप गर्न दुईवटा विधिहरू छन्। तपाईं आफ्नो प्राथमिकताको आधारमा कुनै पनि एक चयन गर्न सक्नुहुन्छ।

> नोट: भर्चुअल वातावरण सिर्जना गरेपछि भर्चुअल वातावरणको Python प्रयोग सुनिश्चित गर्न VSCode वा टर्मिनल पुनः लोड गर्नुहोस्।

| विधि | चरणहरू |
| -------- | ----- |
| `uv` प्रयोग गर्दै | 1. भर्चुअल वातावरण सिर्जना गर्नुहोस्: `uv venv` <br>2. VSCode कमाण्ड "***Python: Select Interpreter***" चलाउनुहोस् र सिर्जना गरिएको भर्चुअल वातावरणबाट Python चयन गर्नुहोस् <br>3. निर्भरता स्थापना गर्नुहोस् (डेभ निर्भरता समावेश): `uv pip install -r pyproject.toml --extra dev` |
| `pip` प्रयोग गर्दै | 1. भर्चुअल वातावरण सिर्जना गर्नुहोस्: `python -m venv .venv` <br>2. VSCode कमाण्ड "***Python: Select Interpreter***" चलाउनुहोस् र सिर्जना गरिएको भर्चुअल वातावरणबाट Python चयन गर्नुहोस् <br>3. निर्भरता स्थापना गर्नुहोस् (डेभ निर्भरता समावेश): `pip install -e .[dev]` |

वातावरण सेटअप गरेपछि, तपाईं Agent Builder लाई MCP Client को रूपमा प्रयोग गरेर आफ्नो स्थानीय विकास मेसिनमा सर्भर चलाउन सक्नुहुन्छ:
1. VS Code Debug प्यानल खोल्नुहोस्। `Debug in Agent Builder` चयन गर्नुहोस् वा `F5` थिचेर MCP सर्भर डिबग गर्न सुरु गर्नुहोस्।
2. AI Toolkit Agent Builder प्रयोग गरेर [यो प्रम्प्ट](../../../../../../../../../../../open_prompt_builder) सँग सर्भर परीक्षण गर्नुहोस्। सर्भर स्वतः Agent Builder सँग जडान हुनेछ।
3. `Run` क्लिक गरेर प्रम्प्टसँग सर्भर परीक्षण गर्नुहोस्।

**बधाई छ**! तपाईंले सफलतापूर्वक मौसम MCP सर्भरलाई Agent Builder को रूपमा MCP Client प्रयोग गरेर आफ्नो स्थानीय विकास मेसिनमा चलाउनुभएको छ।
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## टेम्प्लेटमा समावेश सामग्री

| फोल्डर / फाइल | सामग्री                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | डिबगिङका लागि VSCode फाइलहरू                   |
| `.aitk`      | AI Toolkit का लागि कन्फिगरेसनहरू                |
| `src`        | मौसम MCP सर्भरको स्रोत कोड                     |

## मौसम MCP सर्भर कसरी डिबग गर्ने

> नोटहरू:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) MCP सर्भरहरू परीक्षण र डिबग गर्नको लागि भिजुअल डेभलपर उपकरण हो।
> - सबै डिबगिङ मोडहरूले ब्रेकप्वाइन्टहरू समर्थन गर्छन्, त्यसैले तपाईं उपकरण कार्यान्वयन कोडमा ब्रेकप्वाइन्टहरू थप्न सक्नुहुन्छ।

## उपलब्ध उपकरणहरू

### मौसम उपकरण
`get_weather` उपकरणले निर्दिष्ट स्थानको लागि नकली मौसम जानकारी प्रदान गर्दछ।

| प्यारामिटर | प्रकार | विवरण |
| --------- | ---- | ----------- |
| `location` | string | मौसम जानकारी प्राप्त गर्नको लागि स्थान (जस्तै, शहरको नाम, राज्य, वा समन्वय) |

### Git Clone उपकरण
`git_clone_repo` उपकरणले git रिपोजिटरीलाई निर्दिष्ट फोल्डरमा क्लोन गर्दछ।

| प्यारामिटर | प्रकार | विवरण |
| --------- | ---- | ----------- |
| `repo_url` | string | क्लोन गर्नको लागि git रिपोजिटरीको URL |
| `target_folder` | string | रिपोजिटरी क्लोन गर्नुपर्ने फोल्डरको पथ |

उपकरणले JSON वस्तु फिर्ता गर्छ:
- `success`: अपरेशन सफल भएको हो कि होइन भन्ने संकेत गर्ने Boolean मान
- `target_folder` वा `error`: क्लोन गरिएको रिपोजिटरीको पथ वा त्रुटि सन्देश

### VS Code Open उपकरण
`open_in_vscode` उपकरणले फोल्डरलाई VS Code वा VS Code Insiders एप्लिकेसनमा खोल्छ।

| प्यारामिटर | प्रकार | विवरण |
| --------- | ---- | ----------- |
| `folder_path` | string | खोल्नुपर्ने फोल्डरको पथ |
| `use_insiders` | boolean (वैकल्पिक) | नियमित VS Code को सट्टा VS Code Insiders प्रयोग गर्ने हो कि होइन |

उपकरणले JSON वस्तु फिर्ता गर्छ:
- `success`: अपरेशन सफल भएको हो कि होइन भन्ने संकेत गर्ने Boolean मान
- `message` वा `error`: पुष्टि सन्देश वा त्रुटि सन्देश

| डिबग मोड | विवरण | डिबग गर्ने चरणहरू |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkit मार्फत Agent Builder मा MCP सर्भर डिबग गर्नुहोस्। | 1. VS Code Debug प्यानल खोल्नुहोस्। `Debug in Agent Builder` चयन गर्नुहोस् र `F5` थिचेर MCP सर्भर डिबग गर्न सुरु गर्नुहोस्।<br>2. AI Toolkit Agent Builder प्रयोग गरेर [यो प्रम्प्ट](../../../../../../../../../../../open_prompt_builder) सँग सर्भर परीक्षण गर्नुहोस्। सर्भर स्वतः Agent Builder सँग जडान हुनेछ।<br>3. `Run` क्लिक गरेर प्रम्प्टसँग सर्भर परीक्षण गर्नुहोस्। |
| MCP Inspector | MCP Inspector प्रयोग गरेर MCP सर्भर डिबग गर्नुहोस्। | 1. [Node.js](https://nodejs.org/) स्थापना गर्नुहोस्<br> 2. Inspector सेटअप गर्नुहोस्: `cd inspector` && `npm install` <br> 3. VS Code Debug प्यानल खोल्नुहोस्। `Debug SSE in Inspector (Edge)` वा `Debug SSE in Inspector (Chrome)` चयन गर्नुहोस्। `F5` थिचेर डिबग सुरु गर्नुहोस्।<br> 4. MCP Inspector ब्राउजरमा सुरु भएपछि, `Connect` बटन क्लिक गरेर यो MCP सर्भरसँग जडान गर्नुहोस्।<br> 5. त्यसपछि तपाईं `List Tools` गर्न सक्नुहुन्छ, उपकरण चयन गर्न सक्नुहुन्छ, प्यारामिटरहरू इनपुट गर्न सक्नुहुन्छ, र `Run Tool` क्लिक गरेर सर्भर कोड डिबग गर्न सक्नुहुन्छ।<br> |

## डिफल्ट पोर्टहरू र अनुकूलनहरू

| डिबग मोड | पोर्टहरू | परिभाषाहरू | अनुकूलनहरू | नोट |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) सम्पादन गरेर माथिका पोर्टहरू परिवर्तन गर्नुहोस्। | N/A |
| MCP Inspector | 3001 (सर्भर); 5173 र 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) सम्पादन गरेर माथिका पोर्टहरू परिवर्तन गर्नुहोस्।| N/A |

## प्रतिक्रिया

यदि तपाईंलाई यस टेम्प्लेटको लागि कुनै प्रतिक्रिया वा सुझाव छ भने, कृपया [AI Toolkit GitHub रिपोजिटरी](https://github.com/microsoft/vscode-ai-toolkit/issues) मा एउटा मुद्दा खोल्नुहोस्।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।