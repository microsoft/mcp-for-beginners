# اجرای این نمونه

> [!NOTE]
> این نمونه فرض می‌کند که شما از یک نمونه GitHub Codespaces استفاده می‌کنید. اگر می‌خواهید این را به صورت محلی اجرا کنید، باید یک توکن دسترسی شخصی (PAT) در GitHub تنظیم کنید.
>
> ```bash
> # zsh/bash
> export GITHUB_TOKEN="{{YOUR_GITHUB_PAT}}"
> ```
>
> ```powershell
> # PowerShell
> $env:GITHUB_TOKEN = "{{YOUR_GITHUB_PAT}}"
> ```

## نصب کتابخانه‌ها

```sh
dotnet restore
```

باید کتابخانه‌های زیر نصب شوند: Azure AI Inference، Azure Identity، Microsoft.Extension، Model.Hosting، ModelContextProtcol

## اجرا

```sh 
dotnet run
```

باید خروجی مشابه زیر را ببینید:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: Azure.AI.Inference.ChatCompletionsToolDefinition
Properties: {"a":{"type":"integer"},"b":{"type":"integer"}}
MCP Tools def: 0: Azure.AI.Inference.ChatCompletionsToolDefinition
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

بخش زیادی از خروجی فقط برای اشکال‌زدایی است اما نکته مهم این است که شما ابزارها را از MCP Server فهرست می‌کنید، آن‌ها را به ابزارهای LLM تبدیل می‌کنید و در نهایت پاسخ کلاینت MCP را با "Sum 6" دریافت می‌کنید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.