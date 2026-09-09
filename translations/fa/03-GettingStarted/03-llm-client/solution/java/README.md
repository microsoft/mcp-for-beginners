# کلاینت ماشین حساب LLM

یک برنامه جاوا که نشان می‌دهد چگونه از LangChain4j برای اتصال به سرویس ماشین حساب MCP (پروتکل بستر مدل) از طریق API سازگار با MiniMax OpenAI استفاده کنیم.

## پیش‌نیازها

- جاوا ۲۱ یا بالاتر
- Maven نسخه ۳.۶ یا بالاتر (یا استفاده از Maven wrapper همراه)
- یک کلید API از MiniMax
- سرویس ماشین حساب MCP که روی `http://localhost:8080` در حال اجرا باشد

## دریافت کلید API

این برنامه از API سازگار با MiniMax OpenAI استفاده می‌کند. مراحل زیر را برای دریافت کلید و نقطه پایانی دنبال کنید:

### ۱. انتخاب نقطه پایانی
۱. برای نقطه پایانی جهانی از `https://api.minimax.io/v1` استفاده کنید
۲. برای نقطه پایانی چین از `https://api.minimaxi.com/v1` استفاده کنید

### ۲. ایجاد کلید API
۱. یک کلید MiniMax API از حساب کاربری MiniMax خود بسازید
۲. کلید را در جای امن نگه دارید

### ۳. تنظیم متغیرهای محیطی

#### در ویندوز (خط فرمان):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### در ویندوز (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### در مک/لینوکس:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## راه‌اندازی و نصب

۱. **کلون یا رفتن به پوشه پروژه**

۲. **نصب وابستگی‌ها**:
   ```cmd
   mvnw clean install
   ```
   یا اگر Maven را به‌صورت سراسری نصب کرده‌اید:
   ```cmd
   mvn clean install
   ```

۳. **تنظیم متغیرهای محیطی** (بخش "دریافت کلید API" بالا را ببینید)

۴. **راه‌اندازی سرویس ماشین حساب MCP**:
   مطمئن شوید سرویس ماشین حساب MCP فصل اول روی `http://localhost:8080/sse` در حال اجرا است. قبل از شروع کلاینت این سرویس باید فعال باشد.

## اجرای برنامه

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## عملکرد برنامه

برنامه سه تعامل اصلی با سرویس ماشین حساب را نشان می‌دهد:

۱. **جمع**: حاصل جمع ۲۴.۵ و ۱۷.۳ را محاسبه می‌کند
۲. **جذر**: جذر عدد ۱۴۴ را محاسبه می‌کند
۳. **راهنما**: عملکردهای موجود ماشین حساب را نشان می‌دهد

## خروجی مورد انتظار

هنگام اجرای موفق، باید خروجی مشابه زیر را ببینید:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## عیب‌یابی

### مشکلات رایج

۱. **"متغیر محیطی OPENAI_API_KEY تنظیم نشده است"**
   - مطمئن شوید که متغیر محیطی `OPENAI_API_KEY` را تنظیم کرده‌اید
   - پس از تنظیم متغیر، ترمینال یا خط فرمان خود را مجدداً راه‌اندازی کنید

۲. **"اتصال به localhost:8080 رد شد"**
   - اطمینان حاصل کنید که سرویس ماشین حساب MCP روی پورت ۸۰۸۰ فعال است
   - بررسی کنید که سرویس دیگری پورت ۸۰۸۰ را اشغال نکرده باشد

۳. **"احراز هویت ناموفق بود"**
   - صحت کلید API خود را بررسی کنید
   - مطمئن شوید که `OPENAI_BASE_URL` با نقطه پایانی که قصد استفاده از آن را دارید مطابقت دارد

۴. **خطاهای ساخت Maven**
   - اطمینان حاصل کنید که از جاوا ۲۱ یا بالاتر استفاده می‌کنید: `java -version`
   - سعی کنید ساخت را تمیز کنید: `mvnw clean`

### اشکال‌زدایی

برای فعال کردن لاگ‌گذاری اشکال‌زدایی، هنگام اجرا، آرگومان JVM زیر را اضافه کنید:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## پیکربندی

برنامه به‌صورت زیر پیکربندی شده است:
- به‌طور پیش‌فرض از MiniMax-M3 استفاده می‌کند؛ برای انتخاب بین `MiniMax-M3` یا `MiniMax-M2.7` متغیر `MINIMAX_MODEL_ID` را تنظیم کنید
- وقتی `OPENAI_BASE_URL` تنظیم شده به آن متصل می‌شود؛ در غیر این صورت وقتی `MINIMAX_REGION=cn_zh` است از `https://api.minimaxi.com/v1` استفاده می‌کند، وگرنه به طور پیش‌فرض از `https://api.minimax.io/v1`
- به سرویس MCP در `http://localhost:8080/sse` متصل می‌شود
- برای درخواست‌ها از تایم‌اوت ۶۰ ثانیه استفاده می‌کند

## وابستگی‌ها

وابستگی‌های کلیدی استفاده شده در این پروژه:
- **LangChain4j**: برای یکپارچه‌سازی هوش مصنوعی و مدیریت ابزارها
- **LangChain4j MCP**: برای حمایت از پروتکل بستر مدل (MCP)
- **LangChain4j OpenAI رسمی**: برای یکپارچه‌سازی API سازگار با MiniMax OpenAI
- **Spring Boot**: برای چارچوب برنامه و تزریق وابستگی‌ها

## مجوز

این پروژه تحت مجوز Apache License 2.0 قرار دارد - برای جزئیات بیشتر فایل [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) را ببینید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->