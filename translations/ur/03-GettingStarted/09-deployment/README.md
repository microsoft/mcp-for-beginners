# MCP سرورز کی تعیناتی

> [!NOTE]
> وہ ترتیب کی مثالیں جو `/sse` اینڈ پوائنٹ استعمال کرتی ہیں وہ پرانے HTTP+SSE ٹرانسپورٹ کو ہدف بناتی ہیں۔ MCP `2026-07-28` ریموٹ سرورز Streamable HTTP استعمال کرتے ہیں، جو عام طور پر سرور کی وضاحت کردہ اینڈ پوائنٹ جیسے `/mcp` پر ہوتا ہے۔
> 




## جائزہ

یہ سبق آپ کے MCP سرور ایپ کو تعینات کرنے کے طریقہ کار کو شامل کرتا ہے۔

## سیکھنے کے مقاصد

اس سبق کے آخر تک، آپ قابل ہوں گے:

- مختلف تعیناتی طریقوں کا جائزہ لیں۔
- اپنی ایپ کو تعینات کریں۔

## مقامی ترقی اور تعیناتی

اگر آپ کا سرور صارف کے مشین پر چلنے کے لیے بنایا گیا ہے، تو آپ مندرجہ ذیل مراحل پر عمل کر سکتے ہیں:

1. **سرور ڈاؤن لوڈ کریں**۔ اگر آپ نے سرور نہیں لکھا تو اسے پہلے اپنی مشین پر ڈاؤن لوڈ کریں۔
1. **سرور کا عمل شروع کریں**: اپنی MCP سرور ایپلیکیشن چلائیں

SSE کے لیے (stdio قسم کے سرور کے لیے ضروری نہیں)

1. **نیٹ ورکنگ ترتیب دیں**: یقینی بنائیں کہ سرور متوقع پورٹ پر قابل رسائی ہے
1. **کلائنٹس کو جوڑیں**: `http://localhost:3000` جیسے مقامی کنکشن URLs استعمال کریں

## کلاؤڈ تعیناتی

MCP سرورز کو مختلف کلاؤڈ پلیٹ فارمز پر تعینات کیا جا سکتا ہے:

- **سرورلیس فنکشنز**: ہلکے MCP سرورز کو سرورلیس فنکشنز کے طور پر تعینات کریں
- **کنٹینر سروسز**: Azure Container Apps، AWS ECS، یا Google Cloud Run جیسی سروسز استعمال کریں
- **کبرنیٹس**: اعلی دستیابی کے لیے MCP سرورز کو کبرنیٹس کلسٹرز میں تعینات اور مینج کریں

### مثال: Azure Container Apps

Azure Container Apps MCP سرورز کی تعیناتی کی حمایت کرتا ہے۔ یہ ابھی ترقی کے مراحل میں ہے اور فی الحال SSE سرورز کی حمایت کرتا ہے۔

یہاں ہے کہ آپ اسے کیسے کر سکتے ہیں:

1. ایک رپو کلون کریں:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. اسے مقامی طور پر چلائیں تاکہ چیزوں کی جانچ کر سکیں:

  ```sh
  uv venv
  uv sync

  # لینکس/میگ او ایس
  export API_KEYS=<AN_API_KEY>
  # ونڈوز
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. اسے مقامی طور پر آزمانے کے لیے، *.vscode* فولڈر میں ایک *mcp.json* فائل بنائیں اور درج ذیل مواد شامل کریں:

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

ایک بار SSE سرور شروع ہو جائے، آپ JSON فائل میں پلے آئیکن پر کلک کر سکتے ہیں، آپ کو اب GitHub Copilot کی طرف سے سرور پر ٹولز کا پتہ چلتا نظر آئے گا، ٹول آئیکن دیکھیں۔

1. تعینات کرنے کے لیے، درج ذیل کمانڈ چلائیں:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

لے لیجیے، اسے مقامی طور پر تعینات کریں، ان مراحل کے ذریعے اسے Azure پر تعینات کریں۔

## اضافی وسائل

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps مضمون](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP رپو](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## اگلا کیا ہے

- اگلا: [ایڈوانسڈ سرور موضوعات](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->