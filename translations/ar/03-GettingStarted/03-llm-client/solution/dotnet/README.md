# تشغيل هذا المثال

> [!NOTE]  
> يفترض هذا المثال أنك تستخدم بيئة GitHub Codespaces. إذا كنت ترغب في تشغيله محليًا، فستحتاج إلى إعداد رمز وصول شخصي (PAT) على GitHub.  
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

## تثبيت المكتبات

```sh
dotnet restore
```

يجب تثبيت المكتبات التالية: Azure AI Inference، Azure Identity، Microsoft.Extension، Model.Hosting، ModelContextProtcol

## التشغيل

```sh 
dotnet run
```

يجب أن ترى ناتجًا مشابهًا لـ:

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

الكثير من الناتج هو مجرد تصحيح، لكن المهم هو أنك تقوم بسرد الأدوات من خادم MCP، وتحويلها إلى أدوات LLM، وفي النهاية تحصل على استجابة عميل MCP "Sum 6".

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.