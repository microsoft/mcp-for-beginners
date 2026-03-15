# MCP سرورز کی تعیناتی

اپنے MCP سرور کی تعیناتی دوسروں کو اس کے اوزار اور وسائل تک رسائی کی اجازت دیتی ہے جو آپ کے مقامی ماحول سے باہر ہیں۔ آپ کی ضروریات کے مطابق اسکیل ایبلیٹی، اعتمادیت، اور انتظام کی آسانی کے لیے متعدد تعیناتی کی حکمت عملیاں موجود ہیں۔ نیچے آپ کو MCP سرورز کو مقامی، کنٹینرز میں، اور کلاؤڈ میں تعینات کرنے کے لیے رہنمائی ملے گی۔

## جائزہ

یہ سبق آپ کے MCP سرور ایپ کو تعینات کرنے کا طریقہ کار سکھاتا ہے۔

## تعلیمی مقاصد

اس سبق کے آخر تک، آپ قابل ہوں گے:

- مختلف تعیناتی کے طریقہ کار کا جائزہ لینا۔
- اپنی ایپ کی تعیناتی کرنا۔

## مقامی ترقی اور تعیناتی

اگر آپ کا سرور صارفین کی مشین پر چلنے کے لیے بنایا گیا ہے، تو آپ درج ذیل مراحل پر عمل کر سکتے ہیں:

1. **سرور ڈاؤن لوڈ کریں**۔ اگر آپ نے سرور نہیں لکھا ہے تو پہلے اسے اپنی مشین پر ڈاؤن لوڈ کریں۔  
1. **سرور پراسیس شروع کریں**: اپنا MCP سرور ایپلیکیشن چلائیں۔

SSE کے لیے (stdio قسم کے سرور کے لیے نہیں چاہیے)

1. **نیٹ ورکنگ ترتیب دیں**: یقین دہانی کریں کہ سرور متوقع پورٹ پر قابل رسائی ہے۔  
1. **کلائنٹس کنیکٹ کریں**: مقامی کنکشن URLs جیسے `http://localhost:3000` استعمال کریں۔

## کلاؤڈ تعیناتی

MCP سرورز مختلف کلاؤڈ پلیٹ فارمز پر تعینات کیے جا سکتے ہیں:

- **سرورلیس فنکشنز**: ہلکے پھلکے MCP سرورز کو سرورلیس فنکشنز کے طور پر تعینات کریں۔  
- **کنٹینر سروسز**: Azure Container Apps، AWS ECS، یا Google Cloud Run جیسے سروسز استعمال کریں۔  
- **کوبرنیٹس**: زیادہ دستیابی کے لیے MCP سرورز کو کوبرنیٹس کلسٹرز میں تعینات اور منظم کریں۔

### مثال: Azure Container Apps

Azure Container Apps MCP سرورز کی تعیناتی کی حمایت کرتی ہے۔ یہ ابھی بھی ترقی کے مراحل میں ہے اور اس وقت SSE سرورز کی حمایت کرتی ہے۔

یہاں آپ کیسے آگے بڑھ سکتے ہیں:

1. ایک ریپوزٹری کلون کریں:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. اسے مقامی طور پر چلائیں تاکہ چیزوں کا تجربہ کریں:

  ```sh
  uv venv
  uv sync

  # لینکس/میک او ایس
  export API_KEYS=<AN_API_KEY>
  # ونڈوز
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. اسے مقامی طور پر آزمانے کے لیے، *.vscode* ڈائریکٹری میں ایک *mcp.json* فائل بنائیں اور درج ذیل مواد شامل کریں:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  جب SSE سرور شروع ہو جائے، تو آپ JSON فائل میں پلے آئیکن پر کلک کر سکتے ہیں، اب آپ کو سرور پر اوزار GitHub Copilot کے ذریعے پکڑے ہوئے نظر آئیں گے، ٹول آئیکن دیکھیں۔

1. تعینات کرنے کے لیے، درج ذیل کمانڈ چلائیں:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

لیجیے، اسے مقامی طور پر تعینات کریں، یا ان مراحل کے ذریعے Azure پر تعینات کریں۔

## اضافی وسائل

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps مضمون](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP ریپو](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## آگے کیا ہے

- اگلا: [ایڈوانسڈ سرور موضوعات](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**مختصر نوٹس**:  
یہ دستاویز AI ترجمہ خدمت [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات کا خیال رکھیں کہ خودکار ترجمے میں غلطیاں یا کوتاہیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ذریعہ سمجھی جائے گی۔ اہم معلومات کے لیے ماہر انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->