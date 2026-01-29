# MCP Java Client - کیلکولیٹر ڈیمو

یہ پروجیکٹ دکھاتا ہے کہ کیسے ایک جاوا کلائنٹ بنایا جائے جو MCP (Model Context Protocol) سرور سے جڑتا ہے اور اس کے ساتھ تعامل کرتا ہے۔ اس مثال میں، ہم چپٹر 01 کے کیلکولیٹر سرور سے کنیکٹ ہوں گے اور مختلف ریاضیاتی عملیات انجام دیں گے۔

## ضروریات

اس کلائنٹ کو چلانے سے پہلے آپ کو یہ کرنا ہوگا:

1. **چپٹر 01 سے کیلکولیٹر سرور شروع کریں**:
   - کیلکولیٹر سرور ڈائریکٹری پر جائیں: `03-GettingStarted/01-first-server/solution/java/`
   - کیلکولیٹر سرور کو بنائیں اور چلائیں:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - سرور `http://localhost:8080` پر چل رہا ہونا چاہیے

2. آپ کے سسٹم پر **Java 21 یا اس سے جدید** انسٹال ہو
3. **Maven** (Maven Wrapper کے ذریعے شامل)

## SDKClient کیا ہے؟

`SDKClient` ایک جاوا ایپلیکیشن ہے جو یہ دکھاتی ہے کہ کیسے:
- MCP سرور سے Server-Sent Events (SSE) ٹرانسپورٹ کے ذریعے کنیکٹ کیا جائے
- سرور سے دستیاب ٹولز کی فہرست حاصل کی جائے
- کیلکولیٹر کے مختلف فنکشنز کو ریموٹلی کال کیا جائے
- جوابات کو ہینڈل کیا جائے اور نتائج دکھائے جائیں

## یہ کیسے کام کرتا ہے

کلائنٹ Spring AI MCP فریم ورک استعمال کرتا ہے تاکہ:

1. **کنکشن قائم کرے**: کیلکولیٹر سرور سے جڑنے کے لیے WebFlux SSE کلائنٹ ٹرانسپورٹ بنائے
2. **کلائنٹ کو انیشیئلائز کرے**: MCP کلائنٹ سیٹ اپ کرے اور کنکشن قائم کرے
3. **ٹولز دریافت کرے**: تمام دستیاب کیلکولیٹر آپریشنز کی فہرست بنائے
4. **آپریشنز انجام دے**: مختلف ریاضیاتی فنکشنز کو سیمپل ڈیٹا کے ساتھ کال کرے
5. **نتائج دکھائے**: ہر حساب کا نتیجہ ظاہر کرے

## پروجیکٹ کی ساخت

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

## اہم انحصار

پروجیکٹ میں درج ذیل اہم انحصار استعمال ہوتے ہیں:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

یہ انحصار فراہم کرتا ہے:
- `McpClient` - مرکزی کلائنٹ انٹرفیس
- `WebFluxSseClientTransport` - ویب بیسڈ کمیونیکیشن کے لیے SSE ٹرانسپورٹ
- MCP پروٹوکول کے اسکیمے اور درخواست/جواب کی اقسام

## پروجیکٹ بنانا

Maven wrapper کے ذریعے پروجیکٹ بنائیں:

```cmd
.\mvnw clean install
```

## کلائنٹ چلانا

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**نوٹ**: ان کمانڈز کو چلانے سے پہلے یقینی بنائیں کہ کیلکولیٹر سرور `http://localhost:8080` پر چل رہا ہو۔

## کلائنٹ کیا کرتا ہے

جب آپ کلائنٹ چلائیں گے، تو یہ:

1. `http://localhost:8080` پر کیلکولیٹر سرور سے **کنیکٹ** کرے گا
2. **ٹولز کی فہرست** دکھائے گا - تمام دستیاب کیلکولیٹر آپریشنز
3. **حسابات انجام دے گا**:
   - جمع: 5 + 3 = 8
   - تفریق: 10 - 4 = 6
   - ضرب: 6 × 7 = 42
   - تقسیم: 20 ÷ 4 = 5
   - طاقت: 2^8 = 256
   - مربع جذر: √16 = 4
   - مطلق قیمت: |-5.5| = 5.5
   - مدد: دستیاب آپریشنز دکھائے گا

## متوقع نتیجہ

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

**نوٹ**: آپ کو Maven کی وارننگز نظر آ سکتی ہیں جو تھریڈز کے باقی رہنے کے بارے میں ہوں - یہ reactive ایپلیکیشنز کے لیے معمول کی بات ہے اور کسی غلطی کی نشاندہی نہیں کرتا۔

## کوڈ کو سمجھنا

### 1. ٹرانسپورٹ سیٹ اپ
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
یہ ایک SSE (Server-Sent Events) ٹرانسپورٹ بناتا ہے جو کیلکولیٹر سرور سے جڑتا ہے۔

### 2. کلائنٹ بنانا
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
ایک synchronous MCP کلائنٹ بناتا ہے اور کنکشن کو انیشیئلائز کرتا ہے۔

### 3. ٹولز کال کرنا
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
"add" ٹول کو پیرامیٹرز a=5.0 اور b=3.0 کے ساتھ کال کرتا ہے۔

## مسائل کا حل

### سرور چل نہیں رہا
اگر کنکشن کی غلطیاں آئیں، تو یقینی بنائیں کہ چپٹر 01 کا کیلکولیٹر سرور چل رہا ہے:
```
Error: Connection refused
```
**حل**: پہلے کیلکولیٹر سرور شروع کریں۔

### پورٹ پہلے سے استعمال میں ہے
اگر پورٹ 8080 مصروف ہے:
```
Error: Address already in use
```
**حل**: پورٹ 8080 استعمال کرنے والی دوسری ایپلیکیشنز کو بند کریں یا سرور کو مختلف پورٹ پر چلائیں۔

### بلڈ کی غلطیاں
اگر بلڈ میں غلطیاں آئیں:
```cmd
.\mvnw clean install -DskipTests
```

## مزید جانیں

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔