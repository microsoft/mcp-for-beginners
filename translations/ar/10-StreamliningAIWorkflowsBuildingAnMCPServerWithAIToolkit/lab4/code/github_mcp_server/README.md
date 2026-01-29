# خادم الطقس MCP

هذا نموذج لخادم MCP مكتوب بلغة بايثون، يطبق أدوات الطقس مع ردود وهمية. يمكن استخدامه كقاعدة لبناء خادم MCP الخاص بك. يتضمن الميزات التالية:

- **أداة الطقس**: أداة تقدم معلومات الطقس الوهمية بناءً على الموقع المحدد.
- **أداة استنساخ Git**: أداة تستنسخ مستودع Git إلى مجلد محدد.
- **أداة فتح VS Code**: أداة تفتح مجلدًا في VS Code أو VS Code Insiders.
- **الاتصال بـ Agent Builder**: ميزة تتيح لك ربط خادم MCP بـ Agent Builder للاختبار وتصحيح الأخطاء.
- **تصحيح الأخطاء باستخدام [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: ميزة تتيح لك تصحيح أخطاء خادم MCP باستخدام MCP Inspector.

## البدء باستخدام قالب خادم الطقس MCP

> **المتطلبات الأساسية**
>
> لتشغيل خادم MCP على جهاز التطوير المحلي الخاص بك، ستحتاج إلى:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (مطلوب لأداة git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) أو [VS Code Insiders](https://code.visualstudio.com/insiders/) (مطلوب لأداة open_in_vscode)
> - (*اختياري - إذا كنت تفضل uv*) [uv](https://github.com/astral-sh/uv)
> - [إضافة تصحيح الأخطاء لبايثون](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## إعداد البيئة

هناك طريقتان لإعداد البيئة لهذا المشروع. يمكنك اختيار أي منهما بناءً على تفضيلاتك.

> ملاحظة: قم بإعادة تحميل VSCode أو الطرفية للتأكد من استخدام بايثون الخاص بالبيئة الافتراضية بعد إنشائها.

| الطريقة | الخطوات |
| -------- | ----- |
| باستخدام `uv` | 1. إنشاء بيئة افتراضية: `uv venv` <br>2. تشغيل أمر VSCode "***Python: Select Interpreter***" واختيار بايثون من البيئة الافتراضية التي تم إنشاؤها <br>3. تثبيت التبعيات (بما في ذلك تبعيات التطوير): `uv pip install -r pyproject.toml --extra dev` |
| باستخدام `pip` | 1. إنشاء بيئة افتراضية: `python -m venv .venv` <br>2. تشغيل أمر VSCode "***Python: Select Interpreter***" واختيار بايثون من البيئة الافتراضية التي تم إنشاؤها <br>3. تثبيت التبعيات (بما في ذلك تبعيات التطوير): `pip install -e .[dev]` |

بعد إعداد البيئة، يمكنك تشغيل الخادم على جهاز التطوير المحلي الخاص بك عبر Agent Builder كمستخدم MCP للبدء:
1. افتح لوحة تصحيح الأخطاء في VS Code. اختر `Debug in Agent Builder` أو اضغط على `F5` لبدء تصحيح أخطاء خادم MCP.
2. استخدم AI Toolkit Agent Builder لاختبار الخادم باستخدام [هذا النص](../../../../../../../../../../../open_prompt_builder). سيتم ربط الخادم تلقائيًا بـ Agent Builder.
3. اضغط على `Run` لاختبار الخادم باستخدام النص.

**تهانينا**! لقد نجحت في تشغيل خادم الطقس MCP على جهاز التطوير المحلي الخاص بك عبر Agent Builder كمستخدم MCP.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## ما الذي يتضمنه القالب

| المجلد / الملف | المحتويات                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | ملفات VSCode لتصحيح الأخطاء                   |
| `.aitk`      | إعدادات AI Toolkit                            |
| `src`        | الشيفرة المصدرية لخادم الطقس MCP              |

## كيفية تصحيح أخطاء خادم الطقس MCP

> ملاحظات:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) هو أداة تطوير مرئية لاختبار وتصحيح أخطاء خوادم MCP.
> - جميع أوضاع التصحيح تدعم نقاط التوقف، لذا يمكنك إضافة نقاط توقف إلى شيفرة تنفيذ الأدوات.

## الأدوات المتاحة

### أداة الطقس
أداة `get_weather` تقدم معلومات الطقس الوهمية لموقع محدد.

| المعامل | النوع | الوصف |
| --------- | ---- | ----------- |
| `location` | string | الموقع للحصول على الطقس (مثل اسم المدينة، الولاية، أو الإحداثيات) |

### أداة استنساخ Git
أداة `git_clone_repo` تستنسخ مستودع Git إلى مجلد محدد.

| المعامل | النوع | الوصف |
| --------- | ---- | ----------- |
| `repo_url` | string | رابط مستودع Git للاستنساخ |
| `target_folder` | string | المسار إلى المجلد الذي يجب أن يتم استنساخ المستودع فيه |

تعيد الأداة كائن JSON يحتوي على:
- `success`: قيمة منطقية تشير إلى نجاح العملية
- `target_folder` أو `error`: مسار المستودع المستنسخ أو رسالة خطأ

### أداة فتح VS Code
أداة `open_in_vscode` تفتح مجلدًا في تطبيق VS Code أو VS Code Insiders.

| المعامل | النوع | الوصف |
| --------- | ---- | ----------- |
| `folder_path` | string | المسار إلى المجلد الذي سيتم فتحه |
| `use_insiders` | boolean (اختياري) | ما إذا كان سيتم استخدام VS Code Insiders بدلاً من VS Code العادي |

تعيد الأداة كائن JSON يحتوي على:
- `success`: قيمة منطقية تشير إلى نجاح العملية
- `message` أو `error`: رسالة تأكيد أو رسالة خطأ

| وضع التصحيح | الوصف | خطوات التصحيح |
| ---------- | ----------- | --------------- |
| Agent Builder | تصحيح أخطاء خادم MCP في Agent Builder عبر AI Toolkit. | 1. افتح لوحة تصحيح الأخطاء في VS Code. اختر `Debug in Agent Builder` واضغط على `F5` لبدء تصحيح أخطاء خادم MCP.<br>2. استخدم AI Toolkit Agent Builder لاختبار الخادم باستخدام [هذا النص](../../../../../../../../../../../open_prompt_builder). سيتم ربط الخادم تلقائيًا بـ Agent Builder.<br>3. اضغط على `Run` لاختبار الخادم باستخدام النص. |
| MCP Inspector | تصحيح أخطاء خادم MCP باستخدام MCP Inspector. | 1. تثبيت [Node.js](https://nodejs.org/)<br> 2. إعداد Inspector: `cd inspector` && `npm install` <br> 3. افتح لوحة تصحيح الأخطاء في VS Code. اختر `Debug SSE in Inspector (Edge)` أو `Debug SSE in Inspector (Chrome)`. اضغط F5 لبدء التصحيح.<br> 4. عندما يتم تشغيل MCP Inspector في المتصفح، اضغط على زر `Connect` لربط هذا الخادم MCP.<br> 5. بعد ذلك يمكنك `List Tools`، اختيار أداة، إدخال المعاملات، و`Run Tool` لتصحيح شيفرة الخادم. |

## المنافذ الافتراضية والتخصيصات

| وضع التصحيح | المنافذ | التعريفات | التخصيصات | ملاحظة |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | تعديل [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)، [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)، [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)، [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) لتغيير المنافذ المذكورة أعلاه. | N/A |
| MCP Inspector | 3001 (الخادم); 5173 و3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | تعديل [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)، [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)، [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)، [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) لتغيير المنافذ المذكورة أعلاه. | N/A |

## الملاحظات

إذا كان لديك أي ملاحظات أو اقتراحات لهذا القالب، يرجى فتح قضية على [مستودع GitHub الخاص بـ AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.