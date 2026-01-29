# کلاینت جاوا MCP - دمو ماشین حساب

این پروژه نشان می‌دهد چگونه یک کلاینت جاوا بسازیم که به سرور MCP (پروتکل مدل کانتکست) متصل شده و با آن تعامل داشته باشد. در این مثال، به سرور ماشین حساب از فصل ۰۱ متصل می‌شویم و عملیات مختلف ریاضی را انجام می‌دهیم.

## پیش‌نیازها

قبل از اجرای این کلاینت، باید:

1. **سرور ماشین حساب را از فصل ۰۱ راه‌اندازی کنید**:
   - به دایرکتوری سرور ماشین حساب بروید: `03-GettingStarted/01-first-server/solution/java/`
   - سرور ماشین حساب را بسازید و اجرا کنید:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - سرور باید روی `http://localhost:8080` در حال اجرا باشد

2. **جاوا ۲۱ یا بالاتر** روی سیستم شما نصب باشد
3. **Maven** (از طریق Maven Wrapper شامل شده است)

## SDKClient چیست؟

`SDKClient` یک برنامه جاوا است که نشان می‌دهد چگونه:
- با استفاده از انتقال Server-Sent Events (SSE) به سرور MCP متصل شویم
- ابزارهای موجود روی سرور را فهرست کنیم
- توابع مختلف ماشین حساب را به صورت ریموت فراخوانی کنیم
- پاسخ‌ها را مدیریت کرده و نتایج را نمایش دهیم

## نحوه کار

کلاینت از فریمورک Spring AI MCP استفاده می‌کند تا:

1. **برقراری اتصال**: یک کلاینت WebFlux SSE ایجاد کند تا به سرور ماشین حساب متصل شود
2. **راه‌اندازی کلاینت**: کلاینت MCP را تنظیم کرده و اتصال را برقرار کند
3. **کشف ابزارها**: تمام عملیات‌های موجود ماشین حساب را فهرست کند
4. **اجرای عملیات**: توابع ریاضی مختلف را با داده‌های نمونه فراخوانی کند
5. **نمایش نتایج**: نتایج هر محاسبه را نمایش دهد

## ساختار پروژه

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## وابستگی‌های کلیدی

پروژه از وابستگی‌های کلیدی زیر استفاده می‌کند:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

این وابستگی شامل موارد زیر است:
- `McpClient` - رابط اصلی کلاینت
- `WebFluxSseClientTransport` - انتقال SSE برای ارتباط وب
- اسکیمای پروتکل MCP و انواع درخواست/پاسخ

## ساخت پروژه

پروژه را با استفاده از Maven wrapper بسازید:

```cmd
.\mvnw clean install
```

## اجرای کلاینت

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**توجه**: قبل از اجرای هر یک از این دستورات، مطمئن شوید سرور ماشین حساب روی `http://localhost:8080` در حال اجرا است.

## عملکرد کلاینت

وقتی کلاینت را اجرا می‌کنید، این کارها را انجام می‌دهد:

1. **اتصال** به سرور ماشین حساب در `http://localhost:8080`
2. **فهرست ابزارها** - نمایش تمام عملیات‌های موجود ماشین حساب
3. **انجام محاسبات**:
   - جمع: ۵ + ۳ = ۸
   - تفریق: ۱۰ - ۴ = ۶
   - ضرب: ۶ × ۷ = ۴۲
   - تقسیم: ۲۰ ÷ ۴ = ۵
   - توان: ۲^۸ = ۲۵۶
   - جذر: √۱۶ = ۴
   - قدر مطلق: |-۵.۵| = ۵.۵
   - راهنما: نمایش عملیات‌های موجود

## خروجی مورد انتظار

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**توجه**: ممکن است در پایان هشدارهایی از Maven درباره رشته‌های فعال باقی‌مانده ببینید - این موضوع برای برنامه‌های واکنشی طبیعی است و به معنای خطا نیست.

## درک کد

### ۱. تنظیم انتقال
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
این کد یک انتقال SSE (Server-Sent Events) ایجاد می‌کند که به سرور ماشین حساب متصل می‌شود.

### ۲. ایجاد کلاینت
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
یک کلاینت MCP همزمان ایجاد کرده و اتصال را راه‌اندازی می‌کند.

### ۳. فراخوانی ابزارها
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
ابزار "add" را با پارامترهای a=5.0 و b=3.0 فراخوانی می‌کند.

## رفع اشکال

### سرور اجرا نمی‌شود
اگر خطاهای اتصال دریافت کردید، مطمئن شوید سرور ماشین حساب از فصل ۰۱ در حال اجرا است:
```
Error: Connection refused
```
**راه‌حل**: ابتدا سرور ماشین حساب را راه‌اندازی کنید.

### پورت در حال استفاده است
اگر پورت ۸۰۸۰ مشغول است:
```
Error: Address already in use
```
**راه‌حل**: برنامه‌های دیگر که از پورت ۸۰۸۰ استفاده می‌کنند را متوقف کنید یا سرور را طوری تنظیم کنید که از پورت دیگری استفاده کند.

### خطاهای ساخت
اگر با خطاهای ساخت مواجه شدید:
```cmd
.\mvnw clean install -DskipTests
```

## اطلاعات بیشتر

- [مستندات Spring AI MCP](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [مشخصات پروتکل مدل کانتکست](https://modelcontextprotocol.io/)
- [مستندات Spring WebFlux](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.