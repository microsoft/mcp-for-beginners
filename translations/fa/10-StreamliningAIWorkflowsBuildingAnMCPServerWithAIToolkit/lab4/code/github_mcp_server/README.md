# سرور MCP هواشناسی

این یک نمونه سرور MCP در پایتون است که ابزارهای هواشناسی را با پاسخ‌های شبیه‌سازی شده پیاده‌سازی می‌کند. می‌توانید از آن به عنوان پایه‌ای برای سرور MCP خود استفاده کنید. این سرور شامل ویژگی‌های زیر است:

- **ابزار هواشناسی**: ابزاری که اطلاعات شبیه‌سازی شده هواشناسی را بر اساس مکان مشخص شده ارائه می‌دهد.
- **ابزار کلون گیت**: ابزاری که یک مخزن گیت را به یک پوشه مشخص کلون می‌کند.
- **ابزار باز کردن VS Code**: ابزاری که یک پوشه را در VS Code یا VS Code Insiders باز می‌کند.
- **اتصال به Agent Builder**: ویژگی‌ای که به شما امکان می‌دهد سرور MCP را برای تست و دیباگ به Agent Builder متصل کنید.
- **دیباگ در [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: ویژگی‌ای که به شما امکان می‌دهد سرور MCP را با استفاده از MCP Inspector دیباگ کنید.

## شروع به کار با قالب سرور MCP هواشناسی

> **پیش‌نیازها**
>
> برای اجرای سرور MCP در ماشین توسعه محلی خود، به موارد زیر نیاز دارید:
>
> - [پایتون](https://www.python.org/)
> - [گیت](https://git-scm.com/) (مورد نیاز برای ابزار git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) یا [VS Code Insiders](https://code.visualstudio.com/insiders/) (مورد نیاز برای ابزار open_in_vscode)
> - (*اختیاری - اگر uv را ترجیح می‌دهید*) [uv](https://github.com/astral-sh/uv)
> - [افزونه دیباگر پایتون](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## آماده‌سازی محیط

دو روش برای تنظیم محیط این پروژه وجود دارد. می‌توانید بر اساس ترجیح خود یکی را انتخاب کنید.

> توجه: پس از ایجاد محیط مجازی، VSCode یا ترمینال را مجدداً بارگذاری کنید تا مطمئن شوید که پایتون محیط مجازی استفاده می‌شود.

| روش | مراحل |
| ---- | ----- |
| استفاده از `uv` | 1. ایجاد محیط مجازی: `uv venv` <br>2. اجرای فرمان VSCode "***Python: Select Interpreter***" و انتخاب پایتون از محیط مجازی ایجاد شده <br>3. نصب وابستگی‌ها (شامل وابستگی‌های توسعه): `uv pip install -r pyproject.toml --extra dev` |
| استفاده از `pip` | 1. ایجاد محیط مجازی: `python -m venv .venv` <br>2. اجرای فرمان VSCode "***Python: Select Interpreter***" و انتخاب پایتون از محیط مجازی ایجاد شده <br>3. نصب وابستگی‌ها (شامل وابستگی‌های توسعه): `pip install -e .[dev]` | 

پس از تنظیم محیط، می‌توانید سرور را در ماشین توسعه محلی خود از طریق Agent Builder به عنوان MCP Client اجرا کنید تا شروع به کار کنید:
1. پنل دیباگ VS Code را باز کنید. گزینه `Debug in Agent Builder` را انتخاب کنید یا کلید `F5` را فشار دهید تا دیباگ سرور MCP آغاز شود.
2. از AI Toolkit Agent Builder برای تست سرور با [این درخواست](../../../../../../../../../../../open_prompt_builder) استفاده کنید. سرور به طور خودکار به Agent Builder متصل خواهد شد.
3. روی `Run` کلیک کنید تا سرور را با درخواست تست کنید.

**تبریک می‌گوییم**! شما با موفقیت سرور MCP هواشناسی را در ماشین توسعه محلی خود از طریق Agent Builder به عنوان MCP Client اجرا کردید.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## چه چیزی در قالب گنجانده شده است

| پوشه / فایل | محتویات                                     |
| ----------- | ------------------------------------------ |
| `.vscode`   | فایل‌های VSCode برای دیباگ                 |
| `.aitk`     | تنظیمات مربوط به AI Toolkit                |
| `src`       | کد منبع سرور MCP هواشناسی                  |

## چگونه سرور MCP هواشناسی را دیباگ کنیم

> نکات:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) یک ابزار توسعه بصری برای تست و دیباگ سرورهای MCP است.
> - همه حالت‌های دیباگ از نقاط توقف پشتیبانی می‌کنند، بنابراین می‌توانید نقاط توقف را به کد پیاده‌سازی ابزار اضافه کنید.

## ابزارهای موجود

### ابزار هواشناسی
ابزار `get_weather` اطلاعات شبیه‌سازی شده هواشناسی را برای مکان مشخص شده ارائه می‌دهد.

| پارامتر | نوع | توضیحات |
| -------- | ---- | ------- |
| `location` | رشته | مکانی که باید اطلاعات هواشناسی برای آن دریافت شود (مانند نام شهر، ایالت یا مختصات) |

### ابزار کلون گیت
ابزار `git_clone_repo` یک مخزن گیت را به یک پوشه مشخص کلون می‌کند.

| پارامتر | نوع | توضیحات |
| -------- | ---- | ------- |
| `repo_url` | رشته | URL مخزن گیت برای کلون کردن |
| `target_folder` | رشته | مسیر پوشه‌ای که مخزن باید در آن کلون شود |

این ابزار یک شی JSON بازمی‌گرداند که شامل موارد زیر است:
- `success`: مقدار بولین که نشان می‌دهد عملیات موفقیت‌آمیز بوده است یا خیر
- `target_folder` یا `error`: مسیر مخزن کلون شده یا پیام خطا

### ابزار باز کردن VS Code
ابزار `open_in_vscode` یک پوشه را در برنامه VS Code یا VS Code Insiders باز می‌کند.

| پارامتر | نوع | توضیحات |
| -------- | ---- | ------- |
| `folder_path` | رشته | مسیر پوشه‌ای که باید باز شود |
| `use_insiders` | بولین (اختیاری) | آیا باید از VS Code Insiders به جای VS Code معمولی استفاده شود یا خیر |

این ابزار یک شی JSON بازمی‌گرداند که شامل موارد زیر است:
- `success`: مقدار بولین که نشان می‌دهد عملیات موفقیت‌آمیز بوده است یا خیر
- `message` یا `error`: پیام تأیید یا پیام خطا

| حالت دیباگ | توضیحات | مراحل دیباگ |
| ---------- | -------- | ----------- |
| Agent Builder | دیباگ سرور MCP در Agent Builder از طریق AI Toolkit. | 1. پنل دیباگ VS Code را باز کنید. گزینه `Debug in Agent Builder` را انتخاب کنید و کلید `F5` را فشار دهید تا دیباگ سرور MCP آغاز شود.<br>2. از AI Toolkit Agent Builder برای تست سرور با [این درخواست](../../../../../../../../../../../open_prompt_builder) استفاده کنید. سرور به طور خودکار به Agent Builder متصل خواهد شد.<br>3. روی `Run` کلیک کنید تا سرور را با درخواست تست کنید. |
| MCP Inspector | دیباگ سرور MCP با استفاده از MCP Inspector. | 1. نصب [Node.js](https://nodejs.org/)<br> 2. تنظیم Inspector: `cd inspector` && `npm install` <br> 3. پنل دیباگ VS Code را باز کنید. گزینه `Debug SSE in Inspector (Edge)` یا `Debug SSE in Inspector (Chrome)` را انتخاب کنید. کلید F5 را فشار دهید تا دیباگ آغاز شود.<br> 4. وقتی MCP Inspector در مرورگر راه‌اندازی شد، روی دکمه `Connect` کلیک کنید تا این سرور MCP متصل شود.<br> 5. سپس می‌توانید `List Tools` را انتخاب کنید، پارامترها را وارد کنید و `Run Tool` را برای دیباگ کد سرور اجرا کنید.<br> |

## پورت‌های پیش‌فرض و سفارشی‌سازی‌ها

| حالت دیباگ | پورت‌ها | تعاریف | سفارشی‌سازی‌ها | توضیحات |
| ---------- | ------- | -------- | -------------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | ویرایش [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)، [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)، [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)، [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) برای تغییر پورت‌های بالا. | N/A |
| MCP Inspector | 3001 (سرور); 5173 و 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | ویرایش [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)، [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)، [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)، [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) برای تغییر پورت‌های بالا. | N/A |

## بازخورد

اگر بازخورد یا پیشنهادی برای این قالب دارید، لطفاً یک مشکل در [مخزن GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues) باز کنید.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.