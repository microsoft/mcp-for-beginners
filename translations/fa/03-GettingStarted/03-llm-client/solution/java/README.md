# مشتری ماشین‌حساب LLM

> [!NOTE]
> این راه‌حل به سرویس ماشین‌حساب قدیمی HTTP+SSE دوره متصل می‌شود و
> به APIهای MCP `2025-11-25` هدف‌گذاری شده است. این یک نمونه‌ی HTTP قابل استریم
> `2026-07-28` نیست.

یک برنامه جاوا که نشان می‌دهد چگونه از LangChain4j برای اتصال به سرویس ماشین‌حساب MCP (پروتکل زمینه مدل) از طریق API سازگار با MiniMax OpenAI استفاده کنیم.

## پیش‌نیازها

- جاوا 21 یا بالاتر
- Maven 3.6+ (یا استفاده از Maven wrapper همراه)
- یک کلید API MiniMax
- یک سرویس ماشین‌حساب MCP که روی `http://localhost:8080` اجرا می‌شود

## گرفتن کلید API

این برنامه از API سازگار با MiniMax OpenAI استفاده می‌کند. برای دریافت کلید و نقطه پایان مراحل زیر را دنبال کنید:

### 1. انتخاب نقطه پایان
1. برای نقطه پایان جهانی از `https://api.minimax.io/v1` استفاده کنید
2. برای نقطه پایان چین از `https://api.minimaxi.com/v1` استفاده کنید

### 2. ساخت کلید API
1. یک کلید API MiniMax از حساب MiniMax خود بسازید
2. کلید را در مکانی امن نگه دارید

### 3. تنظیم متغیرهای محیطی

#### در ویندوز (Command Prompt):
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

#### در macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## راه‌اندازی و نصب

1. **کلون یا به پوشه پروژه بروید**

2. **وابستگی‌ها را نصب کنید**:
   ```cmd
   mvnw clean install
   ```
   یا اگر Maven را به صورت سراسری نصب دارید:
   ```cmd
   mvn clean install
   ```

3. **متغیرهای محیطی را تنظیم کنید** (بخش "گرفتن کلید API" را مشاهده کنید)

4. **سرویس ماشین‌حساب MCP را راه‌اندازی کنید**:
   مطمئن شوید سرویس ماشین‌حساب MCP فصل 1 روی `http://localhost:8080/sse` اجرا می‌شود. باید قبل از شروع مشتری اجرا شده باشد.

## اجرای برنامه

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## کاری که برنامه انجام می‌دهد

برنامه سه تعامل اصلی با سرویس ماشین‌حساب را نشان می‌دهد:

1. **جمع**: مجموع 24.5 و 17.3 را محاسبه می‌کند
2. **جذر**: جذر 144 را محاسبه می‌کند
3. **راهنما**: توابع ماشین‌حساب موجود را نشان می‌دهد

## خروجی مورد انتظار

هنگام اجرای موفق، خروجی مشابه زیر باید مشاهده شود:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## عیب‌یابی

### مشکلات رایج

1. **"متغیر محیطی OPENAI_API_KEY تنظیم نشده است"**
   - مطمئن شوید متغیر محیطی `OPENAI_API_KEY` را تنظیم کرده‌اید
   - پس از تنظیم متغیر، ترمینال/کامند پرامپت را مجدداً راه‌اندازی کنید

2. **"اتصال به localhost:8080 رد شد"**
   - اطمینان حاصل کنید سرویس ماشین‌حساب MCP روی پورت 8080 در حال اجرا است
   - بررسی کنید که سرویس دیگری پورت 8080 را اشغال نکرده باشد

3. **"احراز هویت ناموفق بود"**
   - کلید API خود را معتبر چک کنید
   - بررسی کنید که مقدار `OPENAI_BASE_URL` با نقطه پایان مورد نظر شما مطابقت داشته باشد

4. **خطاهای ساخت Maven**
   - اطمینان حاصل کنید از جاوای 21 یا بالاتر استفاده می‌کنید: `java -version`
   - تلاش کنید ساخت را پاک کنید: `mvnw clean`

### اشکال‌زدایی

برای فعال کردن ثبت اشکال‌زدایی، هنگام اجرا آرگومان JVM زیر را اضافه کنید:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## پیکربندی

برنامه به این صورت پیکربندی شده است:
- به‌صورت پیش‌فرض از MiniMax-M3 استفاده می‌کند؛ `MINIMAX_MODEL_ID` را تنظیم کنید تا بین `MiniMax-M3` یا `MiniMax-M2.7` انتخاب کنید
- اگر `OPENAI_BASE_URL` تنظیم شده باشد به آن متصل می‌شود؛ در غیر این صورت زمانی که `MINIMAX_REGION=cn_zh` است از `https://api.minimaxi.com/v1` و در حالت پیش‌فرض از `https://api.minimax.io/v1` استفاده می‌کند
- به سرویس MCP در `http://localhost:8080/sse` متصل می‌شود
- برای درخواست‌ها از تایم‌اوت ۶۰ ثانیه استفاده می‌کند

## وابستگی‌ها

وابستگی‌های کلیدی استفاده شده در این پروژه:
- **LangChain4j**: برای یکپارچه‌سازی هوش مصنوعی و مدیریت ابزارها
- **LangChain4j MCP**: برای پشتیبانی از پروتکل زمینه مدل
- **LangChain4j OpenAI رسمی**: برای یکپارچه‌سازی API سازگار با MiniMax OpenAI
- **Spring Boot**: برای چارچوب برنامه و تزریق وابستگی

## مجوز

این پروژه تحت مجوز Apache License 2.0 منتشر شده است - جزئیات بیشتر در فایل [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) را ببینید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->