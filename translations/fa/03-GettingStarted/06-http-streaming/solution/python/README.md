# اجرای این نمونه

در اینجا نحوه اجرای سرور و کلاینت استریمینگ HTTP کلاسیک و همچنین سرور و کلاینت استریمینگ MCP با استفاده از پایتون توضیح داده شده است.

### مرور کلی

- شما یک سرور MCP راه‌اندازی می‌کنید که هنگام پردازش آیتم‌ها، اعلان‌های پیشرفت را به کلاینت ارسال می‌کند.
- کلاینت هر اعلان را به صورت لحظه‌ای نمایش می‌دهد.
- این راهنما شامل پیش‌نیازها، تنظیمات، اجرا و رفع اشکال است.

### پیش‌نیازها

- پایتون نسخه 3.9 یا جدیدتر
- بسته پایتون `mcp` (با دستور `pip install mcp` نصب کنید)

### نصب و تنظیمات

1. مخزن را کلون کنید یا فایل‌های راه‌حل را دانلود کنید.

   ```pwsh
   git clone https://github.com/microsoft/mcp-for-beginners
   ```

1. **یک محیط مجازی ایجاد و فعال کنید (توصیه می‌شود):**

   ```pwsh
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # or
   source venv/bin/activate      # On Linux/macOS
   ```

1. **وابستگی‌های مورد نیاز را نصب کنید:**

   ```pwsh
   pip install "mcp[cli]" fastapi requests
   ```

### فایل‌ها

- **سرور:** [server.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/server.py)
- **کلاینت:** [client.py](../../../../../../03-GettingStarted/06-http-streaming/solution/python/client.py)

### اجرای سرور استریمینگ HTTP کلاسیک

1. به دایرکتوری راه‌حل بروید:

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```

2. سرور استریمینگ HTTP کلاسیک را اجرا کنید:

   ```pwsh
   python server.py
   ```

3. سرور شروع به کار کرده و پیام زیر را نمایش می‌دهد:

   ```
   Starting FastAPI server for classic HTTP streaming...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### اجرای کلاینت استریمینگ HTTP کلاسیک

1. یک ترمینال جدید باز کنید (همان محیط مجازی و دایرکتوری را فعال کنید):

   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py
   ```

2. پیام‌های استریم شده باید به ترتیب نمایش داده شوند:

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

### اجرای سرور استریمینگ MCP

1. به دایرکتوری راه‌حل بروید:
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   ```
2. سرور MCP را با انتقال `streamable-http` اجرا کنید:
   ```pwsh
   python server.py mcp
   ```
3. سرور شروع به کار کرده و پیام زیر را نمایش می‌دهد:
   ```
   Starting MCP server with streamable-http transport...
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

### اجرای کلاینت استریمینگ MCP

1. یک ترمینال جدید باز کنید (همان محیط مجازی و دایرکتوری را فعال کنید):
   ```pwsh
   cd 03-GettingStarted/06-http-streaming/solution
   python client.py mcp
   ```
2. اعلان‌ها باید به صورت لحظه‌ای هنگام پردازش هر آیتم توسط سرور نمایش داده شوند:
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

### مراحل کلیدی پیاده‌سازی

1. **سرور MCP را با استفاده از FastMCP ایجاد کنید.**
2. **ابزاری تعریف کنید که یک لیست را پردازش کرده و با استفاده از `ctx.info()` یا `ctx.log()` اعلان‌ها را ارسال کند.**
3. **سرور را با `transport="streamable-http"` اجرا کنید.**
4. **یک کلاینت با یک هندلر پیام پیاده‌سازی کنید تا اعلان‌ها را هنگام دریافت نمایش دهد.**

### مرور کد
- سرور از توابع async و کانتکست MCP برای ارسال به‌روزرسانی‌های پیشرفت استفاده می‌کند.
- کلاینت یک هندلر پیام async پیاده‌سازی می‌کند تا اعلان‌ها و نتیجه نهایی را چاپ کند.

### نکات و رفع اشکال

- از `async/await` برای عملیات‌های غیرمسدودکننده استفاده کنید.
- همیشه استثناها را هم در سرور و هم در کلاینت برای افزایش پایداری مدیریت کنید.
- با چندین کلاینت آزمایش کنید تا به‌روزرسانی‌های لحظه‌ای را مشاهده کنید.
- اگر با خطا مواجه شدید، نسخه پایتون خود را بررسی کرده و مطمئن شوید که تمام وابستگی‌ها نصب شده‌اند.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.