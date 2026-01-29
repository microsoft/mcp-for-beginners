# اس نمونے کو چلانا

یہاں بتایا گیا ہے کہ کلاسک HTTP اسٹریمنگ سرور اور کلائنٹ، اور MCP اسٹریمنگ سرور اور کلائنٹ کو Python کے ذریعے کیسے چلایا جائے۔

### جائزہ

- آپ ایک MCP سرور سیٹ اپ کریں گے جو آئٹمز کو پروسیس کرتے وقت کلائنٹ کو پروگریس نوٹیفکیشنز بھیجے گا۔
- کلائنٹ ہر نوٹیفکیشن کو حقیقی وقت میں دکھائے گا۔
- یہ گائیڈ پیشگی ضروریات، سیٹ اپ، چلانے اور خرابیوں کو دور کرنے کا احاطہ کرتا ہے۔

### پیشگی ضروریات

- Python 3.9 یا اس سے جدید ورژن
- `mcp` Python پیکیج (انسٹال کریں `pip install mcp` کے ذریعے)

### انسٹالیشن اور سیٹ اپ

1. ریپوزٹری کلون کریں یا سلوشن فائلز ڈاؤنلوڈ کریں۔

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **ایک ورچوئل ماحول بنائیں اور اسے ایکٹیویٹ کریں (تجویز کردہ):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **ضروری ڈپینڈنسیز انسٹال کریں:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### فائلز

- **سرور:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **کلائنٹ:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### کلاسک HTTP اسٹریمنگ سرور چلانا

1. سلوشن ڈائریکٹری پر جائیں:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. کلاسک HTTP اسٹریمنگ سرور شروع کریں:

   ```pwsh
   python server.py
   ```

3. سرور شروع ہوگا اور یہ دکھائے گا:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### کلاسک HTTP اسٹریمنگ کلائنٹ چلانا

1. ایک نیا ٹرمینل کھولیں (اسی ورچوئل ماحول اور ڈائریکٹری کو ایکٹیویٹ کریں):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. آپ کو اسٹریمنگ میسجز ترتیب وار پرنٹ ہوتے نظر آئیں گے:

   ```text
   Running classic HTTP streaming client...
   Connecting to http://localhost:8000/stream with message: hello
   --- Streaming Progress ---
   Processing file 1/3...
   Processing file 2/3...
   Processing file 3/3...
   Here's the file content: hello
   --- Stream Ended ---
   ```

### MCP اسٹریمنگ سرور چلانا

1. سلوشن ڈائریکٹری پر جائیں:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. MCP سرور کو streamable-http ٹرانسپورٹ کے ساتھ شروع کریں:
   ```pwsh
   python server.py mcp
   ```
3. سرور شروع ہوگا اور یہ دکھائے گا:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### MCP اسٹریمنگ کلائنٹ چلانا

1. ایک نیا ٹرمینل کھولیں (اسی ورچوئل ماحول اور ڈائریکٹری کو ایکٹیویٹ کریں):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. آپ کو نوٹیفکیشنز حقیقی وقت میں پرنٹ ہوتے نظر آئیں گے جب سرور ہر آئٹم کو پروسیس کرے گا:
   ```
   Running MCP client...
   Starting client...
   Session ID before init: None
   Session ID after init: a30ab7fca9c84f5fa8f5c54fe56c9612
   Session initialized, ready to call tools.
   Received message: root=LoggingMessageNotification(...)
   NOTIFICATION: root=LoggingMessageNotification(...)
   ...
   Tool result: meta=None content=[TextContent(type='text', text='Processed files: file_1.txt, file_2.txt, file_3.txt | Message: hello from client')]
   ```

### اہم عمل درآمد کے مراحل

1. **FastMCP کا استعمال کرتے ہوئے MCP سرور بنائیں۔**
2. **ایک ایسا ٹول ڈیفائن کریں جو ایک لسٹ کو پروسیس کرے اور `ctx.info()` یا `ctx.log()` کے ذریعے نوٹیفکیشنز بھیجے۔**
3. **سرور کو `transport="streamable-http"` کے ساتھ چلائیں۔**
4. **ایک کلائنٹ نافذ کریں جو میسج ہینڈلر کے ذریعے نوٹیفکیشنز کو دکھائے جب وہ آئیں۔**

### کوڈ کا جائزہ
- سرور async فنکشنز اور MCP کانٹیکسٹ کا استعمال کرتا ہے تاکہ پروگریس اپڈیٹس بھیجے۔
- کلائنٹ ایک async میسج ہینڈلر نافذ کرتا ہے تاکہ نوٹیفکیشنز اور حتمی نتیجہ پرنٹ کرے۔

### تجاویز اور خرابیوں کا ازالہ

- غیر مسدود آپریشنز کے لیے `async/await` کا استعمال کریں۔
- سرور اور کلائنٹ دونوں میں مضبوطی کے لیے ہمیشہ ایکسیپشنز کو ہینڈل کریں۔
- متعدد کلائنٹس کے ساتھ ٹیسٹ کریں تاکہ حقیقی وقت کی اپڈیٹس کا مشاہدہ کریں۔
- اگر آپ کو ایررز کا سامنا ہو تو اپنے Python ورژن کو چیک کریں اور یقینی بنائیں کہ تمام ڈپینڈنسیز انسٹال ہیں۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز، جو اس کی مقامی زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔