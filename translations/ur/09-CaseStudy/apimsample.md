# کیس اسٹڈی: API مینجمنٹ میں REST API کو MCP سرور کے طور پر ظاہر کریں

Azure API Management ایک سروس ہے جو آپ کے API اینڈ پوائنٹس کے اوپر ایک گیٹ وے فراہم کرتی ہے۔ یہ اس طرح کام کرتی ہے کہ Azure API Management آپ کے APIs کے سامنے ایک پراکسی کے طور پر کام کرتی ہے اور آنے والی درخواستوں کے ساتھ کیا کرنا ہے، اس کا فیصلہ کرتی ہے۔

اسے استعمال کرنے سے آپ کو درج ذیل خصوصیات ملتی ہیں:

- **سیکیورٹی**، آپ API کیز، JWT، یا مینیجڈ آئیڈینٹیٹی جیسے تمام آپشنز استعمال کر سکتے ہیں۔
- **ریٹ لمیٹنگ**، ایک زبردست فیچر جو یہ فیصلہ کرنے کی اجازت دیتا ہے کہ ایک خاص وقت میں کتنی کالز گزر سکتی ہیں۔ یہ یقینی بناتا ہے کہ تمام صارفین کو بہترین تجربہ ملے اور آپ کی سروس درخواستوں سے مغلوب نہ ہو۔
- **اسکیلنگ اور لوڈ بیلنسنگ**۔ آپ لوڈ کو متوازن کرنے کے لیے متعدد اینڈ پوائنٹس سیٹ کر سکتے ہیں اور یہ بھی فیصلہ کر سکتے ہیں کہ "لوڈ بیلنسنگ" کیسے کی جائے۔
- **AI خصوصیات جیسے سیمینٹک کیشنگ**، ٹوکن لمٹ اور ٹوکن مانیٹرنگ وغیرہ۔ یہ زبردست خصوصیات ہیں جو رسپانس کو بہتر بناتی ہیں اور آپ کو ٹوکن کے استعمال پر نظر رکھنے میں مدد دیتی ہیں۔ [مزید پڑھیں](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)۔

## MCP + Azure API Management کیوں؟

ماڈل کانٹیکسٹ پروٹوکول تیزی سے ایجنٹک AI ایپس کے لیے ایک معیار بن رہا ہے اور ٹولز اور ڈیٹا کو ایک مستقل طریقے سے ظاہر کرنے کا ایک طریقہ ہے۔ Azure API Management ایک قدرتی انتخاب ہے جب آپ کو APIs کو "مینج" کرنے کی ضرورت ہو۔ MCP سرورز اکثر دیگر APIs کے ساتھ انٹیگریٹ ہوتے ہیں تاکہ کسی ٹول کی درخواست کو حل کیا جا سکے۔ لہٰذا Azure API Management اور MCP کو یکجا کرنا ایک منطقی فیصلہ ہے۔

## جائزہ

اس خاص کیس اسٹڈی میں ہم سیکھیں گے کہ API اینڈ پوائنٹس کو MCP سرور کے طور پر کیسے ظاہر کیا جائے۔ ایسا کرنے سے، ہم آسانی سے ان اینڈ پوائنٹس کو ایک ایجنٹک ایپ کا حصہ بنا سکتے ہیں اور ساتھ ہی Azure API Management کی خصوصیات سے فائدہ اٹھا سکتے ہیں۔

## کلیدی خصوصیات

- آپ ان اینڈ پوائنٹس کے میتھڈز منتخب کرتے ہیں جنہیں ٹولز کے طور پر ظاہر کرنا ہے۔
- اضافی خصوصیات کا انحصار اس پر ہے کہ آپ نے اپنی API کے لیے پالیسی سیکشن میں کیا کنفیگر کیا ہے۔ لیکن یہاں ہم آپ کو دکھائیں گے کہ ریٹ لمیٹنگ کیسے شامل کی جا سکتی ہے۔

## ابتدائی مرحلہ: API درآمد کریں

اگر آپ کے پاس Azure API Management میں پہلے سے ایک API موجود ہے تو یہ زبردست ہے، آپ اس مرحلے کو چھوڑ سکتے ہیں۔ اگر نہیں، تو اس لنک کو دیکھیں: [Azure API Management میں API درآمد اور شائع کریں](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)۔

## API کو MCP سرور کے طور پر ظاہر کریں

API اینڈ پوائنٹس کو ظاہر کرنے کے لیے، درج ذیل مراحل پر عمل کریں:

1. Azure پورٹل پر جائیں اور اس ایڈریس پر جائیں: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   اپنی API Management انسٹینس پر جائیں۔

1. بائیں مینو میں، **APIs > MCP Servers > + Create new MCP Server** منتخب کریں۔

1. API میں، ایک REST API منتخب کریں جسے MCP سرور کے طور پر ظاہر کرنا ہے۔

1. ایک یا زیادہ API آپریشنز منتخب کریں جنہیں ٹولز کے طور پر ظاہر کرنا ہے۔ آپ تمام آپریشنز یا صرف مخصوص آپریشنز منتخب کر سکتے ہیں۔

    ![میتھڈز منتخب کریں](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** منتخب کریں۔

1. مینو آپشن **APIs** اور **MCP Servers** پر جائیں، آپ کو درج ذیل نظر آنا چاہیے:

    ![مین پین میں MCP سرور دیکھیں](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP سرور تخلیق ہو گیا ہے اور API آپریشنز ٹولز کے طور پر ظاہر ہو گئے ہیں۔ MCP سرور MCP Servers پین میں درج ہے۔ URL کالم MCP سرور کے اینڈ پوائنٹ کو دکھاتا ہے جسے آپ ٹیسٹنگ یا کلائنٹ ایپلیکیشن میں کال کر سکتے ہیں۔

## اختیاری: پالیسیز کنفیگر کریں

Azure API Management میں پالیسیز کا بنیادی تصور ہے جہاں آپ اپنے اینڈ پوائنٹس کے لیے مختلف قواعد سیٹ کرتے ہیں جیسے ریٹ لمیٹنگ یا سیمینٹک کیشنگ۔ یہ پالیسیز XML میں لکھی جاتی ہیں۔

یہاں یہ ہے کہ آپ اپنے MCP سرور کے لیے ریٹ لمیٹنگ پالیسی کیسے سیٹ کر سکتے ہیں:

1. پورٹل میں، APIs کے تحت، **MCP Servers** منتخب کریں۔

1. وہ MCP سرور منتخب کریں جو آپ نے تخلیق کیا ہے۔

1. بائیں مینو میں، MCP کے تحت، **Policies** منتخب کریں۔

1. پالیسی ایڈیٹر میں، وہ پالیسیز شامل کریں یا ایڈٹ کریں جو آپ MCP سرور کے ٹولز پر لاگو کرنا چاہتے ہیں۔ پالیسیز XML فارمیٹ میں ڈیفائن کی جاتی ہیں۔ مثال کے طور پر، آپ ایک پالیسی شامل کر سکتے ہیں جو MCP سرور کے ٹولز پر کالز کو محدود کرتی ہے (اس مثال میں، ہر کلائنٹ IP ایڈریس کے لیے 30 سیکنڈ میں 5 کالز)۔ یہاں XML ہے جو ریٹ لمیٹنگ کا سبب بنے گا:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    یہ پالیسی ایڈیٹر کی تصویر ہے:

    ![پالیسی ایڈیٹر](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## آزمائیں

آئیے یہ یقینی بنائیں کہ ہمارا MCP سرور صحیح کام کر رہا ہے۔

اس کے لیے، ہم Visual Studio Code اور GitHub Copilot اور اس کے ایجنٹ موڈ کا استعمال کریں گے۔ ہم MCP سرور کو ایک *mcp.json* فائل میں شامل کریں گے۔ ایسا کرنے سے، Visual Studio Code ایک کلائنٹ کے طور پر کام کرے گا جس میں ایجنٹک صلاحیتیں ہوں گی اور اختتامی صارفین ایک پرامپٹ ٹائپ کر کے سرور کے ساتھ تعامل کر سکیں گے۔

آئیے دیکھتے ہیں کہ Visual Studio Code میں MCP سرور کیسے شامل کریں:

1. کمانڈ پیلیٹ سے **MCP: Add Server** کمانڈ استعمال کریں۔

1. جب پوچھا جائے، سرور کی قسم منتخب کریں: **HTTP (HTTP یا Server Sent Events)**۔

1. Azure API Management میں MCP سرور کا URL درج کریں۔ مثال: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE اینڈ پوائنٹ کے لیے) یا **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP اینڈ پوائنٹ کے لیے)، نوٹ کریں کہ ٹرانسپورٹس کے درمیان فرق `/sse` یا `/mcp` ہے۔

1. اپنی پسند کا ایک سرور ID درج کریں۔ یہ کوئی اہم ویلیو نہیں ہے لیکن یہ آپ کو یاد رکھنے میں مدد دے گا کہ یہ سرور انسٹینس کیا ہے۔

1. منتخب کریں کہ کنفیگریشن کو اپنے ورک اسپیس سیٹنگز یا یوزر سیٹنگز میں محفوظ کرنا ہے۔

  - **ورک اسپیس سیٹنگز** - سرور کنفیگریشن ایک .vscode/mcp.json فائل میں محفوظ کی جاتی ہے جو صرف موجودہ ورک اسپیس میں دستیاب ہوتی ہے۔

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    یا اگر آپ اسٹریمنگ HTTP کو بطور ٹرانسپورٹ منتخب کرتے ہیں تو یہ تھوڑا مختلف ہوگا:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **یوزر سیٹنگز** - سرور کنفیگریشن آپ کی گلوبل *settings.json* فائل میں شامل کی جاتی ہے اور یہ تمام ورک اسپیسز میں دستیاب ہوتی ہے۔ کنفیگریشن درج ذیل کی طرح نظر آتی ہے:

    ![یوزر سیٹنگ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. آپ کو کنفیگریشن میں ایک ہیڈر بھی شامل کرنے کی ضرورت ہے تاکہ Azure API Management کے خلاف صحیح طریقے سے تصدیق ہو سکے۔ یہ ایک ہیڈر استعمال کرتا ہے جسے **Ocp-Apim-Subscription-Key** کہا جاتا ہے۔

    - یہاں یہ ہے کہ آپ اسے سیٹنگز میں کیسے شامل کر سکتے ہیں:

    ![تصدیق کے لیے ہیڈر شامل کریں](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)، یہ ایک پرامپٹ ظاہر کرے گا جو آپ سے API کی کلید کی ویلیو پوچھے گا جو آپ Azure پورٹل میں اپنی Azure API Management انسٹینس کے لیے تلاش کر سکتے ہیں۔

   - اسے *mcp.json* میں شامل کرنے کے لیے، آپ اسے اس طرح شامل کر سکتے ہیں:

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

اب ہم یا تو سیٹنگز یا *.vscode/mcp.json* میں سیٹ اپ کر چکے ہیں۔ آئیے اسے آزمائیں۔

وہاں ایک ٹولز آئیکن ہونا چاہیے، جہاں آپ کے سرور سے ظاہر کردہ ٹولز درج ہوں:

![سرور سے ٹولز](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ٹولز آئیکن پر کلک کریں اور آپ کو ٹولز کی ایک فہرست نظر آنی چاہیے:

    ![ٹولز](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. چیٹ میں ایک پرامپٹ درج کریں تاکہ ٹول کو فعال کیا جا سکے۔ مثال کے طور پر، اگر آپ نے کسی آرڈر کے بارے میں معلومات حاصل کرنے کے لیے ایک ٹول منتخب کیا ہے، تو آپ ایجنٹ سے آرڈر کے بارے میں پوچھ سکتے ہیں۔ یہاں ایک مثال پرامپٹ ہے:

    ```text
    get information from order 2
    ```

    اب آپ کو ایک ٹولز آئیکن نظر آئے گا جو آپ سے ٹول کو کال کرنے کے لیے آگے بڑھنے کو کہے گا۔ ٹول کو چلانے کے لیے جاری رکھنے کا انتخاب کریں، آپ کو اب درج ذیل کی طرح ایک آؤٹ پٹ نظر آنا چاہیے:

    ![پرامپٹ کا نتیجہ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **اوپر جو آپ دیکھتے ہیں وہ اس پر منحصر ہے کہ آپ نے کون سے ٹولز سیٹ اپ کیے ہیں، لیکن خیال یہ ہے کہ آپ کو اوپر کی طرح ایک ٹیکسٹوال رسپانس ملے۔**

## حوالہ جات

یہاں آپ مزید سیکھ سکتے ہیں:

- [Azure API Management اور MCP پر ٹیوٹوریل](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python مثال: Azure API Management کا استعمال کرتے ہوئے ریموٹ MCP سرورز کو محفوظ کریں (تجرباتی)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP کلائنٹ اتھورائزیشن لیب](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Azure API Management ایکسٹینشن کا استعمال کرتے ہوئے APIs کو Visual Studio Code میں درآمد اور مینج کریں](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center میں ریموٹ MCP سرورز کو رجسٹر کریں اور دریافت کریں](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI گیٹ وے](https://github.com/Azure-Samples/AI-Gateway) ایک زبردست ریپو جو Azure API Management کے ساتھ کئی AI صلاحیتیں دکھاتا ہے۔
- [AI گیٹ وے ورکشاپس](https://azure-samples.github.io/AI-Gateway/) Azure پورٹل کا استعمال کرتے ہوئے ورکشاپس پر مشتمل ہے، جو AI صلاحیتوں کا جائزہ لینے کے لیے ایک زبردست طریقہ ہے۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔