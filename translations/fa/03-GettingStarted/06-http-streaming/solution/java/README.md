# دمو استریمینگ HTTP ماشین‌حساب

این پروژه استریمینگ HTTP را با استفاده از Server-Sent Events (SSE) و Spring Boot WebFlux نشان می‌دهد. این پروژه شامل دو برنامه است:

- **سرور ماشین‌حساب**: یک سرویس وب واکنشی که محاسبات را انجام داده و نتایج را با SSE استریم می‌کند
- **کلاینت ماشین‌حساب**: برنامه‌ای که نقطه انتهایی استریم را مصرف می‌کند

## پیش‌نیازها

- جاوا ۱۷ یا بالاتر
- Maven نسخه ۳.۶ یا بالاتر

## ساختار پروژه

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## نحوه کار

1. **سرور ماشین‌حساب** یک نقطه انتهایی `/calculate` ارائه می‌دهد که:
   - پارامترهای کوئری را می‌پذیرد: `a` (عدد)، `b` (عدد)، `op` (عملیات)
   - عملیات‌های پشتیبانی شده: `add`، `sub`، `mul`، `div`
   - رویدادهای Server-Sent Events را با پیشرفت محاسبه و نتیجه بازمی‌گرداند

2. **کلاینت ماشین‌حساب** به سرور متصل می‌شود و:
   - درخواست محاسبه `7 * 5` را ارسال می‌کند
   - پاسخ استریم شده را مصرف می‌کند
   - هر رویداد را در کنسول چاپ می‌کند

## اجرای برنامه‌ها

### گزینه ۱: استفاده از Maven (توصیه شده)

#### ۱. راه‌اندازی سرور ماشین‌حساب

یک ترمینال باز کنید و به دایرکتوری سرور بروید:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

سرور روی `http://localhost:8080` اجرا خواهد شد

باید خروجی مشابه زیر را ببینید:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### ۲. اجرای کلاینت ماشین‌حساب

یک **ترمینال جدید** باز کنید و به دایرکتوری کلاینت بروید:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

کلاینت به سرور متصل شده، محاسبه را انجام داده و نتایج استریم شده را نمایش می‌دهد.

### گزینه ۲: اجرای مستقیم با جاوا

#### ۱. کامپایل و اجرای سرور:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### ۲. کامپایل و اجرای کلاینت:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## تست دستی سرور

می‌توانید سرور را با مرورگر وب یا curl نیز تست کنید:

### استفاده از مرورگر وب:
به آدرس زیر مراجعه کنید: `http://localhost:8080/calculate?a=10&b=5&op=add`

### استفاده از curl:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## خروجی مورد انتظار

هنگام اجرای کلاینت، باید خروجی استریم شده مشابه زیر را ببینید:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## عملیات‌های پشتیبانی شده

- `add` - جمع (a + b)
- `sub` - تفریق (a - b)
- `mul` - ضرب (a * b)
- `div` - تقسیم (a / b، اگر b = 0 باشد مقدار NaN برمی‌گرداند)

## مرجع API

### GET /calculate

**پارامترها:**
- `a` (الزامی): عدد اول (double)
- `b` (الزامی): عدد دوم (double)
- `op` (الزامی): عملیات (`add`، `sub`، `mul`، `div`)

**پاسخ:**
- Content-Type: `text/event-stream`
- رویدادهای Server-Sent Events با پیشرفت محاسبه و نتیجه را بازمی‌گرداند

**نمونه درخواست:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**نمونه پاسخ:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## رفع اشکال

### مشکلات رایج

1. **پورت ۸۰۸۰ در حال استفاده است**
   - برنامه‌های دیگر که از پورت ۸۰۸۰ استفاده می‌کنند را متوقف کنید
   - یا پورت سرور را در `calculator-server/src/main/resources/application.yml` تغییر دهید

2. **اتصال رد شد**
   - مطمئن شوید سرور قبل از اجرای کلاینت در حال اجرا است
   - بررسی کنید که سرور با موفقیت روی پورت ۸۰۸۰ اجرا شده باشد

3. **مشکل در نام پارامترها**
   - این پروژه شامل پیکربندی کامپایلر Maven با فلگ `-parameters` است
   - اگر با مشکلات اتصال پارامتر مواجه شدید، مطمئن شوید پروژه با این پیکربندی ساخته شده است

### متوقف کردن برنامه‌ها

- در ترمینال هر برنامه، کلیدهای `Ctrl+C` را فشار دهید
- یا اگر برنامه به صورت پس‌زمینه اجرا می‌شود، از دستور `mvn spring-boot:stop` استفاده کنید

## فناوری‌های استفاده شده

- **Spring Boot 3.3.1** - فریم‌ورک برنامه
- **Spring WebFlux** - فریم‌ورک وب واکنشی
- **Project Reactor** - کتابخانه استریم‌های واکنشی
- **Netty** - سرور I/O غیرمسدودکننده
- **Maven** - ابزار ساخت
- **Java 17+** - زبان برنامه‌نویسی

## مراحل بعدی

کد را تغییر دهید تا:
- عملیات‌های ریاضی بیشتری اضافه کنید
- مدیریت خطا برای عملیات نامعتبر را پیاده‌سازی کنید
- لاگ‌گیری درخواست/پاسخ را اضافه کنید
- احراز هویت را پیاده‌سازی کنید
- تست‌های واحد اضافه کنید

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.