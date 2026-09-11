# کیس اسٹڈی: API مینجمنٹ میں REST API کو MCP سرور کے طور پر ظاہر کریں

Azure API Management، ایک سروس ہے جو آپ کے API Endpoints کے اوپر ایک گیٹ وے فراہم کرتی ہے۔ اس کا طریقہ کار یہ ہے کہ Azure API Management آپ کے APIs کے سامنے ایک پراکسی کی طرح کام کرتی ہے اور داخل ہونے والی درخواستوں کے ساتھ کیا کرنا ہے اس کا فیصلہ کر سکتی ہے۔

اس کا استعمال کرتے ہوئے، آپ بہت سی خصوصیات شامل کرتے ہیں جیسے:

- **سیکیورٹی**، آپ API keys, JWT سے لیکر Managed Identity تک سب کچھ استعمال کر سکتے ہیں۔
- **ریٹ لمٹنگ**، ایک بہترین خصوصیت یہ ہے کہ آپ فیصلہ کر سکتے ہیں کہ ایک مخصوص وقت کی اکائی میں کتنی کالز گزر سکتی ہیں۔ یہ یقینی بناتا ہے کہ تمام صارفین کا تجربہ بہترین ہو اور آپ کی سروس درخواستوں کے بوجھ سے مغلوب نہ ہو۔
- **اسکیلنگ اور لوڈ بیلنسنگ**۔ آپ کئی endpoints سیٹ اپ کر سکتے ہیں تاکہ لوڈ کو متوازن کیا جا سکے اور آپ یہ بھی فیصلہ کر سکتے ہیں کہ "لوڈ بیلنس" کیسے کیا جائے۔
- **AI خصوصیات جیسے Semantic Caching، Token Limit اور Token Monitoring وغیرہ**۔ یہ بہترین خصوصیات ہیں جو ردعمل کو بہتر بناتی ہیں اور آپ کو اپنے ٹوکن کے خرچ پر کنٹرول میں رکھنے میں مدد دیتی ہیں۔ [مزید پڑھیں یہاں](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)۔

## MCP + Azure API Management کیوں؟

ماڈل کانٹیکسٹ پروٹوکول تیزی سے ایجنٹک AI ایپس کے لیے ایک معیار بنتا جا رہا ہے اور ٹولز اور ڈیٹا کو ایک مستقل طریقے سے ظاہر کرنے کا ذریعہ ہے۔ Azure API Management ایک قدرتی انتخاب ہے جب آپ کو APIs کو "مینج" کرنا ہو۔ MCP سرورز اکثر دوسرے APIs کے ساتھ انٹیگریٹ ہوتے ہیں تاکہ مثال کے طور پر ایک ٹول کے لیے درخواستوں کو حل کیا جا سکے۔ اس لیے Azure API Management اور MCP کو ملا کر بہت مطلب پیدا ہوتا ہے۔

## جائزہ

اس مخصوص کیس میں ہم سیکھیں گے کہ API Endpoints کو MCP سرور کے طور پر کیسے ظاہر کریں۔ ایسا کرنے سے، ہم آسانی سے ان endpoints کو ایجنٹک ایپ کا حصہ بنا سکتے ہیں اور ساتھ ہی Azure API Management کی خصوصیات سے فائدہ اٹھا سکتے ہیں۔

## کلیدی خصوصیات

- آپ وہ endpoint طریقے منتخب کرتے ہیں جنہیں ٹولز کے طور پر ظاہر کرنا چاہتے ہیں۔
- اضافی خصوصیات آپ کی API کے پالیسی سیکشن میں کنفیگر کیے جانے پر منحصر ہیں۔ لیکن یہاں ہم آپ کو دکھائیں گے کہ آپ ریٹ لمٹنگ کیسے شامل کر سکتے ہیں۔

## پیشگی قدم: ایک API درآمد کریں

اگر آپ کے پاس پہلے سے Azure API Management میں API موجود ہے تو بہت اچھا، آپ اس قدم کو چھوڑ سکتے ہیں۔ اگر نہیں، تو اس لنک کو دیکھیں، [Azure API Management میں API درآمد کرنا](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)۔

## API کو MCP سرور کے طور پر ظاہر کریں

API endpoints کو ظاہر کرنے کے لیے، درج ذیل مراحل پر عمل کریں:

1. Azure پورٹل پر جائیں اور اس پتہ پر جائیں <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>
اپنے API Management کا انسٹینس منتخب کریں۔

1. بائیں مینو میں، APIs > MCP Servers > + Create new MCP Server منتخب کریں۔

1. API میں، ایک REST API منتخب کریں جسے MCP سرور کے طور پر ظاہر کرنا ہو۔

1. ایک یا زیادہ API عملیات منتخب کریں جنہیں ٹولز کے طور پر ظاہر کرنا ہو۔ آپ تمام عملیات یا صرف مخصوص آپریشن منتخب کر سکتے ہیں۔

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Create** منتخب کریں۔

1. مینو میں **APIs** اور **MCP Servers** پر جائیں، آپ کو درج ذیل نظر آنا چاہیے:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP سرور بنا دیا گیا ہے اور API عملیات کو بطور ٹولز ظاہر کیا گیا ہے۔ MCP سرور MCP Servers پین میں درج ہے۔ URL کالم MCP سرور کے endpoint کو دکھاتا ہے جسے آپ ٹیسٹنگ کے لیے یا کلائنٹ ایپلیکیشن میں کال کر سکتے ہیں۔

## اختیاری: پالیسیز ترتیب دیں

Azure API Management میں پالیسیز کا بنیادی تصور موجود ہے جہاں آپ اپنے Endpoints کے لیے مختلف قواعد مرتب کرتے ہیں جیسے ریٹ لمٹنگ یا Semantic Caching۔ یہ پالیسیاں XML میں مرتب کی جاتی ہیں۔

یہاں بتایا گیا ہے کہ آپ اپنے MCP سرور کے لیے ریٹ لمٹ کرنے کی پالیسی کیسے مرتب کر سکتے ہیں:

1. پورٹل میں، APIs کے تحت، **MCP Servers** منتخب کریں۔

1. اپنا بنایا ہوا MCP سرور منتخب کریں۔

1. بائیں مینو میں، MCP کے تحت، **Policies** منتخب کریں۔

1. پالیسی ایڈیٹر میں، وہ پالیسیاں شامل کریں یا تدوین کریں جو آپ MCP سرور کے ٹولز پر لاگو کرنا چاہتے ہیں۔ پالیسیاں XML فارمیٹ میں بیان کی جاتی ہیں۔ مثال کے طور پر، آپ ایک پالیسی شامل کر سکتے ہیں جو MCP سرور کے ٹولز کے لیے کالز کی حد مقرر کرے (اس مثال میں، کلائنٹ IP ایڈریس کے حساب سے ہر 30 سیکنڈ میں 5 کالز)۔ یہ XML ریٹ لمٹ کرے گا:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    یہاں پالیسی ایڈیٹر کی تصویر ہے:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## آزمائیں

چلیے یقینی بناتے ہیں کہ ہمارا MCP سرور صحیح طریقے سے کام کر رہا ہے۔

> [!NOTE]
> Azure API Management اس وقت اس سرور کو Streamable
> HTTP `/mcp` endpoint کے ذریعے ظاہر کرتا ہے۔ پرانا HTTP+SSE `/sse` ٹرانسپورٹ غیر مستعمل ہے اور
> صرف پرانے کلائنٹس کے ساتھ استعمال کیا جانا چاہیے۔

اس کے لیے، ہم Visual Studio Code اور GitHub Copilot اور اس کے Agent موڈ کا استعمال کریں گے۔ ہم MCP سرور کو *mcp.json* میں شامل کریں گے۔ اس طرح Visual Studio Code ایک کلائنٹ کے طور پر ایجنٹک صلاحیتوں کے ساتھ کام کرے گا اور آخری صارف ایک پرامپٹ ٹائپ کر کے اس سرور کے ساتھ تعامل کر سکے گا۔

دیکھتے ہیں کہ Visual Studio Code میں MCP سرور کو کیسے شامل کیا جائے:

1. Command Palette سے MCP: **Add Server کمانڈ** استعمال کریں۔

1. جب پوچھا جائے، سرور کی قسم منتخب کریں: **HTTP (HTTP یا Server Sent Events)**۔

1. API Management میں MCP سرور کے لیے دکھائی گئی Streamable HTTP URL درج کریں۔
    مثال کے طور پر:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`۔

1. اپنی پسند کا سرور ID درج کریں۔ یہ اہم ویلیو نہیں ہے لیکن آپ کو یہ یاد رکھنے میں مدد دے گی کہ یہ سرور انسٹینس کیا ہے۔

1. منتخب کریں کہ کنفیگریشن کو ورک اسپیس سیٹنگز میں محفوظ کرنا ہے یا یوزر سیٹنگز میں۔

  - **ورک اسپیس سیٹنگز** - سرور کی کنفیگریشن صرف موجودہ ورک اسپیس میں دستیاب .vscode/mcp.json فائل میں محفوظ ہو گی۔

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **یوزر سیٹنگز** - سرور کی کنفیگریشن آپ کے گلوبل *settings.json* فائل میں شامل ہو گی اور تمام ورک اسپیسز میں دستیاب ہو گی۔ کنفیگریشن کچھ اس طرح نظر آتی ہے:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. آپ کو کنفیگریشن میں ایک ہیڈر بھی شامل کرنا ہوگا تاکہ وہ Azure API Management کے لیے صحیح طریقے سے تصدیق کرے۔ یہ ہیڈر **Ocp-Apim-Subscription-Key* کہلاتا ہے۔

    - یہ آپ یوں شامل کر سکتے ہیں:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)، اس سے ایک پرامپٹ ظاہر ہوگا جو API key کی ویلیو پوچھے گا جو آپ Azure پورٹل میں اپنے Azure API Management انسٹینس میں پا سکتے ہیں۔

   - اگر آپ اسے *mcp.json* میں شامل کرنا چاہتے ہیں، تو آپ اسے اس طرح شامل کر سکتے ہیں:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### ایجنٹ موڈ استعمال کریں

اب ہم سیٹنگز یا *.vscode/mcp.json* میں مکمل سیٹ اپ ہو چکے ہیں۔ آئیے آزماتے ہیں۔

ایک ٹولز آئیکن ہونا چاہیے، جہاں آپ کے سرور کے ظاہر شدہ ٹولز کی فہرست ہو:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ٹولز آئیکن پر کلک کریں اور آپ کو اس طرح ٹولز کی فہرست نظر آئے گی:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. ٹول کو کال کرنے کے لیے چیٹ میں پرامپٹ درج کریں۔ مثال کے طور پر، اگر آپ نے ایک ٹول منتخب کیا ہو جو آرڈر کے بارے میں معلومات دیتا ہے، تو آپ ایجنٹ سے کسی آرڈر کے بارے میں پوچھ سکتے ہیں۔ یہ ایک مثال پرامپٹ ہے:

    ```text
    get information from order 2
    ```

    اب آپ کو ایک ٹولز آئیکن دکھایا جائے گا جو آپ سے ٹول چلانے کی تصدیق کرے گا۔ جاری رکھنے کے لیے منتخب کریں، آپ کو اب ایسا آؤٹ پٹ دیکھنا چاہیے:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **جو آپ اوپر دیکھ رہے ہیں وہ اس بات پر منحصر ہے کہ آپ نے کون سے ٹولز سیٹ کیے ہیں، لیکن مقصد یہ ہے کہ آپ کو ایک متنی جواب ملے جیسا کہ اوپر ہے**


## حوالے

یہاں آپ مزید سیکھ سکتے ہیں:

- [Azure API Management اور MCP پر ٹیوٹوریل](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python نمونہ: Azure API Management کا استعمال کرتے ہوئے محفوظ ریموٹ MCP سرورز (تجرباتی)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP کلائنٹ اجازت نامہ لیب](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Visual Studio Code کے لیے Azure API Management ایکسٹینشن کی مدد سے APIs درآمد کریں اور مینج کریں](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center میں ریموٹ MCP سرورز رجسٹر اور دریافت کریں](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI گیٹ وے](https://github.com/Azure-Samples/AI-Gateway) ایک بہترین ریپوزٹری جو Azure API Management کے ساتھ بہت سی AI خصوصیات دکھاتی ہے
- [AI گیٹ وے ورکشاپس](https://azure-samples.github.io/AI-Gateway/) Azure پورٹل کے استعمال سے ورکشاپس پر مشتمل ہے، جو AI صلاحیتوں کی جانچ شروع کرنے کا بہترین طریقہ ہے۔

## اگلا مرحلہ کیا ہے

- واپس جائیں: [کیس اسٹڈیز کا جائزہ](./README.md)
- آگے بڑھیں: [Azure AI ٹریول ایجنٹس](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->