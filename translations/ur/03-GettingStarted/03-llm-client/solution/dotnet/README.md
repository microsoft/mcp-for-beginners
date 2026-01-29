# اس نمونے کو چلائیں

> [!NOTE]  
> یہ نمونہ فرض کرتا ہے کہ آپ GitHub Codespaces استعمال کر رہے ہیں۔ اگر آپ اسے مقامی طور پر چلانا چاہتے ہیں، تو آپ کو GitHub پر ایک personal access token (PAT) سیٹ اپ کرنا ہوگا۔  
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

## لائبریریاں انسٹال کریں

```sh
dotnet restore
```

مندرجہ ذیل لائبریریاں انسٹال ہونی چاہئیں: Azure AI Inference، Azure Identity، Microsoft.Extension، Model.Hosting، ModelContextProtcol  

## چلائیں

```sh 
dotnet run
```

آپ کو اس طرح کا آؤٹ پٹ نظر آنا چاہیے:

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

زیادہ تر آؤٹ پٹ صرف ڈیبگنگ کے لیے ہے لیکن اہم بات یہ ہے کہ آپ MCP Server سے ٹولز کی فہرست بنا رہے ہیں، انہیں LLM ٹولز میں تبدیل کر رہے ہیں اور آخر میں آپ کو MCP کلائنٹ کا جواب "Sum 6" مل رہا ہے۔

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔