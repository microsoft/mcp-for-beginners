# Weather MCP Server

یہ Python میں ایک نمونہ MCP Server ہے جو موسمی آلات کو جعلی جوابات کے ساتھ نافذ کرتا ہے۔ اسے آپ کے اپنے MCP Server کے لیے ایک بنیاد کے طور پر استعمال کیا جا سکتا ہے۔ اس میں درج ذیل خصوصیات شامل ہیں:

- **Weather Tool**: ایک ایسا آلہ جو دی گئی جگہ کی بنیاد پر جعلی موسمی معلومات فراہم کرتا ہے۔
- **Connect to Agent Builder**: ایک خصوصیت جو آپ کو MCP سرور کو Agent Builder سے جوڑنے کی اجازت دیتی ہے تاکہ آپ ٹیسٹنگ اور ڈیبگنگ کر سکیں۔
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: ایک خصوصیت جو آپ کو MCP Inspector کے ذریعے MCP Server کو ڈیبگ کرنے کی سہولت دیتی ہے۔

## Weather MCP Server ٹیمپلیٹ کے ساتھ شروع کریں

> **Prerequisites**
>
> اپنے مقامی ترقیاتی کمپیوٹر پر MCP Server چلانے کے لیے آپ کو درج ذیل کی ضرورت ہوگی:
>
> - [Python](https://www.python.org/)
> - (*اختیاری - اگر آپ uv کو ترجیح دیتے ہیں*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## ماحول تیار کریں

اس پروجیکٹ کے لیے ماحول تیار کرنے کے دو طریقے ہیں۔ آپ اپنی پسند کے مطابق کوئی بھی طریقہ منتخب کر سکتے ہیں۔

> Note: ورچوئل ماحول بنانے کے بعد VSCode یا ٹرمینل کو ری لوڈ کریں تاکہ ورچوئل ماحول کا Python استعمال ہو۔

| طریقہ | اقدامات |
| -------- | ----- |
| `uv` استعمال کرتے ہوئے | 1. ورچوئل ماحول بنائیں: `uv venv` <br>2. VSCode کمانڈ "***Python: Select Interpreter***" چلائیں اور بنائے گئے ورچوئل ماحول سے Python منتخب کریں <br>3. انحصاریاں انسٹال کریں (ڈویلپمنٹ انحصاریوں سمیت): `uv pip install -r pyproject.toml --extra dev` |
| `pip` استعمال کرتے ہوئے | 1. ورچوئل ماحول بنائیں: `python -m venv .venv` <br>2. VSCode کمانڈ "***Python: Select Interpreter***" چلائیں اور بنائے گئے ورچوئل ماحول سے Python منتخب کریں<br>3. انحصاریاں انسٹال کریں (ڈویلپمنٹ انحصاریوں سمیت): `pip install -e .[dev]` |

ماحول تیار کرنے کے بعد، آپ Agent Builder کے ذریعے MCP Client کے طور پر اپنے مقامی ترقیاتی کمپیوٹر پر سرور چلا سکتے ہیں تاکہ شروع کیا جا سکے:
1. VS Code کے Debug پینل کو کھولیں۔ `Debug in Agent Builder` منتخب کریں یا MCP سرور کو ڈیبگ کرنے کے لیے `F5` دبائیں۔
2. AI Toolkit Agent Builder کا استعمال کرتے ہوئے [اس پرامپٹ](../../../../../../../../../../open_prompt_builder) کے ساتھ سرور کی جانچ کریں۔ سرور خود بخود Agent Builder سے جڑ جائے گا۔
3. پرامپٹ کے ساتھ سرور کی جانچ کے لیے `Run` پر کلک کریں۔

**مبارک ہو**! آپ نے کامیابی کے ساتھ Agent Builder کے ذریعے MCP Client کے طور پر اپنے مقامی ترقیاتی کمپیوٹر پر Weather MCP Server چلایا ہے۔
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## ٹیمپلیٹ میں کیا شامل ہے

| فولڈر / فائل | مواد |
| ------------ | -------------------------------------------- |
| `.vscode`    | ڈیبگنگ کے لیے VSCode فائلز                   |
| `.aitk`      | AI Toolkit کی کنفیگریشنز                     |
| `src`        | weather mcp server کا سورس کوڈ                |

## Weather MCP Server کو کیسے ڈیبگ کریں

> نوٹس:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ایک بصری ڈویلپر ٹول ہے جو MCP سرورز کی جانچ اور ڈیبگنگ کے لیے استعمال ہوتا ہے۔
> - تمام ڈیبگنگ موڈز بریک پوائنٹس کی حمایت کرتے ہیں، لہٰذا آپ ٹول کے نفاذ کے کوڈ میں بریک پوائنٹس شامل کر سکتے ہیں۔

| ڈیبگ موڈ | وضاحت | ڈیبگ کرنے کے اقدامات |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkit کے ذریعے Agent Builder میں MCP سرور کو ڈیبگ کریں۔ | 1. VS Code کے Debug پینل کو کھولیں۔ `Debug in Agent Builder` منتخب کریں اور MCP سرور کو ڈیبگ کرنے کے لیے `F5` دبائیں۔<br>2. AI Toolkit Agent Builder کا استعمال کرتے ہوئے [اس پرامپٹ](../../../../../../../../../../open_prompt_builder) کے ساتھ سرور کی جانچ کریں۔ سرور خود بخود Agent Builder سے جڑ جائے گا۔<br>3. پرامپٹ کے ساتھ سرور کی جانچ کے لیے `Run` پر کلک کریں۔ |
| MCP Inspector | MCP Inspector کا استعمال کرتے ہوئے MCP سرور کو ڈیبگ کریں۔ | 1. [Node.js](https://nodejs.org/) انسٹال کریں۔<br> 2. Inspector سیٹ اپ کریں: `cd inspector` اور `npm install` چلائیں۔<br> 3. VS Code کے Debug پینل کو کھولیں۔ `Debug SSE in Inspector (Edge)` یا `Debug SSE in Inspector (Chrome)` منتخب کریں۔ ڈیبگ شروع کرنے کے لیے `F5` دبائیں۔<br> 4. جب MCP Inspector براؤزر میں کھلے، تو اس MCP سرور کو جوڑنے کے لیے `Connect` بٹن پر کلک کریں۔<br> 5. پھر آپ `List Tools` کر سکتے ہیں، کوئی ٹول منتخب کریں، پیرامیٹرز داخل کریں، اور `Run Tool` کر کے اپنے سرور کے کوڈ کو ڈیبگ کریں۔<br> |

## ڈیفالٹ پورٹس اور تخصیصات

| ڈیبگ موڈ | پورٹس | تعریفات | تخصیصات | نوٹ |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | اوپر دیے گئے پورٹس کو تبدیل کرنے کے لیے [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json)، [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json)، [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py)، [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) میں ترمیم کریں۔ | N/A |
| MCP Inspector | 3001 (سرور); 5173 اور 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | اوپر دیے گئے پورٹس کو تبدیل کرنے کے لیے [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json)، [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json)، [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py)، [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) میں ترمیم کریں۔ | N/A |

## تاثرات

اگر آپ کے پاس اس ٹیمپلیٹ کے بارے میں کوئی رائے یا تجاویز ہیں، تو براہ کرم [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues) پر ایک مسئلہ کھولیں۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔