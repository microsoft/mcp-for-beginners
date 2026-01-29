# MCP سرورز کی تعیناتی

اپنے MCP سرور کو تعینات کرنے سے دوسرے لوگ اس کے ٹولز اور وسائل تک آپ کے مقامی ماحول سے باہر بھی رسائی حاصل کر سکتے ہیں۔ تعیناتی کی مختلف حکمت عملیاں ہیں جن پر غور کرنا ضروری ہے، جو آپ کی توسیع پذیری، اعتمادیت، اور انتظام کی آسانی کی ضروریات پر منحصر ہیں۔ نیچے آپ کو MCP سرورز کو مقامی، کنٹینرز میں، اور کلاؤڈ پر تعینات کرنے کے لیے رہنمائی ملے گی۔

## جائزہ

یہ سبق آپ کو MCP Server ایپ کو تعینات کرنے کا طریقہ سکھاتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ قابل ہوں گے:

- مختلف تعیناتی کے طریقوں کا جائزہ لینا۔
- اپنی ایپ کو تعینات کرنا۔

## مقامی ترقی اور تعیناتی

اگر آپ کا سرور صارفین کی مشین پر چلانے کے لیے ہے، تو آپ درج ذیل مراحل پر عمل کر سکتے ہیں:

1. **سرور ڈاؤن لوڈ کریں**۔ اگر آپ نے سرور خود نہیں لکھا، تو پہلے اسے اپنی مشین پر ڈاؤن لوڈ کریں۔  
1. **سرور کا عمل شروع کریں**: اپنی MCP سرور ایپلیکیشن چلائیں۔

SSE کے لیے (stdio قسم کے سرور کے لیے ضروری نہیں)

1. **نیٹ ورکنگ ترتیب دیں**: یقینی بنائیں کہ سرور متوقع پورٹ پر قابل رسائی ہے۔  
1. **کلائنٹس کو جوڑیں**: مقامی کنکشن URLs جیسے `http://localhost:3000` استعمال کریں۔

## کلاؤڈ تعیناتی

MCP سرورز مختلف کلاؤڈ پلیٹ فارمز پر تعینات کیے جا سکتے ہیں:

- **سرورلیس فنکشنز**: ہلکے پھلکے MCP سرورز کو سرورلیس فنکشنز کے طور پر تعینات کریں۔  
- **کنٹینر سروسز**: Azure Container Apps، AWS ECS، یا Google Cloud Run جیسی سروسز استعمال کریں۔  
- **کبرنیٹیز**: MCP سرورز کو کبرنیٹیز کلسٹرز میں تعینات اور منظم کریں تاکہ اعلی دستیابی حاصل ہو۔

### مثال: Azure Container Apps

Azure Container Apps MCP سرورز کی تعیناتی کی حمایت کرتے ہیں۔ یہ ابھی ترقی کے مراحل میں ہے اور فی الحال SSE سرورز کی حمایت کرتا ہے۔

آپ اس طرح آگے بڑھ سکتے ہیں:

1. ایک ریپو کلون کریں:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. مقامی طور پر اسے چلائیں تاکہ چیزوں کا تجربہ کریں:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. مقامی تجربے کے لیے، *.vscode* ڈائریکٹری میں *mcp.json* فائل بنائیں اور درج ذیل مواد شامل کریں:

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

  جب SSE سرور شروع ہو جائے، تو آپ JSON فائل میں پلے آئیکن پر کلک کر سکتے ہیں، اب آپ کو سرور پر ٹولز GitHub Copilot کے ذریعے پکڑے جانے نظر آئیں گے، Tool آئیکن دیکھیں۔

1. تعیناتی کے لیے، درج ذیل کمانڈ چلائیں:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

بس یہی ہے، اسے مقامی طور پر تعینات کریں، یا ان مراحل کے ذریعے Azure پر تعینات کریں۔

## اضافی وسائل

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps آرٹیکل](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP ریپو](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## آگے کیا ہے

- اگلا: [عملی نفاذ](../../04-PracticalImplementation/README.md)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔