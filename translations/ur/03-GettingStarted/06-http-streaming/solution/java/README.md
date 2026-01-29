# Calculator HTTP Streaming Demo

یہ پروجیکٹ Server-Sent Events (SSE) کے ذریعے HTTP streaming کو Spring Boot WebFlux کے ساتھ ظاہر کرتا ہے۔ اس میں دو ایپلیکیشنز شامل ہیں:

- **Calculator Server**: ایک reactive ویب سروس جو حساب کتاب کرتی ہے اور SSE کے ذریعے نتائج کو stream کرتی ہے  
- **Calculator Client**: ایک کلائنٹ ایپلیکیشن جو streaming endpoint کو استعمال کرتی ہے

## Prerequisites

- Java 17 یا اس سے اوپر  
- Maven 3.6 یا اس سے اوپر  

## Project Structure

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

## How It Works

1. **Calculator Server** ایک `/calculate` endpoint فراہم کرتا ہے جو:  
   - query parameters قبول کرتا ہے: `a` (نمبر)، `b` (نمبر)، `op` (آپریشن)  
   - سپورٹ شدہ آپریشنز: `add`, `sub`, `mul`, `div`  
   - Server-Sent Events کے ذریعے حساب کی پیش رفت اور نتیجہ واپس کرتا ہے  

2. **Calculator Client** سرور سے جڑتا ہے اور:  
   - `7 * 5` کا حساب کرنے کی درخواست بھیجتا ہے  
   - streaming response کو استعمال کرتا ہے  
   - ہر ایونٹ کو کنسول پر پرنٹ کرتا ہے  

## Running the Applications

### Option 1: Using Maven (Recommended)

#### 1. Calculator Server شروع کریں

ٹرمینل کھولیں اور سرور ڈائریکٹری میں جائیں:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

سرور `http://localhost:8080` پر شروع ہو جائے گا

آپ کو اس طرح کا آؤٹ پٹ نظر آئے گا:  
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Calculator Client چلائیں

ایک **نیا ٹرمینل** کھولیں اور کلائنٹ ڈائریکٹری میں جائیں:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

کلائنٹ سرور سے جڑ کر حساب کرے گا اور streaming نتائج دکھائے گا۔

### Option 2: Using Java directly

#### 1. سرور کو کمپائل اور چلائیں:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. کلائنٹ کو کمپائل اور چلائیں:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Testing the Server Manually

آپ سرور کو ویب براؤزر یا curl کے ذریعے بھی ٹیسٹ کر سکتے ہیں:

### ویب براؤزر استعمال کرتے ہوئے:  
ملاحظہ کریں: `http://localhost:8080/calculate?a=10&b=5&op=add`

### curl استعمال کرتے ہوئے:  
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Expected Output

جب کلائنٹ چلائیں گے تو آپ کو اس طرح کا streaming آؤٹ پٹ نظر آئے گا:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Supported Operations

- `add` - جمع (a + b)  
- `sub` - تفریق (a - b)  
- `mul` - ضرب (a * b)  
- `div` - تقسیم (a / b، اگر b = 0 ہو تو NaN واپس کرتا ہے)  

## API Reference

### GET /calculate

**Parameters:**  
- `a` (ضروری): پہلا نمبر (double)  
- `b` (ضروری): دوسرا نمبر (double)  
- `op` (ضروری): آپریشن (`add`, `sub`, `mul`, `div`)  

**Response:**  
- Content-Type: `text/event-stream`  
- Server-Sent Events کے ذریعے حساب کی پیش رفت اور نتیجہ واپس کرتا ہے  

**Example Request:**  
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Example Response:**  
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Troubleshooting

### Common Issues

1. **Port 8080 پہلے سے استعمال میں ہے**  
   - کوئی اور ایپلیکیشن جو پورٹ 8080 استعمال کر رہی ہو اسے بند کریں  
   - یا `calculator-server/src/main/resources/application.yml` میں سرور پورٹ تبدیل کریں  

2. **Connection refused**  
   - کلائنٹ شروع کرنے سے پہلے یقینی بنائیں کہ سرور چل رہا ہے  
   - چیک کریں کہ سرور پورٹ 8080 پر کامیابی سے شروع ہوا ہے  

3. **Parameter name issues**  
   - یہ پروجیکٹ Maven compiler configuration کے ساتھ `-parameters` فلیگ استعمال کرتا ہے  
   - اگر parameter binding میں مسئلہ ہو تو یقینی بنائیں کہ پروجیکٹ اس کنفیگریشن کے ساتھ بنایا گیا ہے  

### Stopping the Applications

- ہر ایپلیکیشن کے چلنے والے ٹرمینل میں `Ctrl+C` دبائیں  
- یا اگر بیک گراؤنڈ میں چل رہا ہو تو `mvn spring-boot:stop` استعمال کریں  

## Technology Stack

- **Spring Boot 3.3.1** - ایپلیکیشن فریم ورک  
- **Spring WebFlux** - Reactive ویب فریم ورک  
- **Project Reactor** - Reactive streams لائبریری  
- **Netty** - Non-blocking I/O سرور  
- **Maven** - Build ٹول  
- **Java 17+** - پروگرامنگ زبان  

## Next Steps

کوڈ میں تبدیلی کر کے کوشش کریں:  
- مزید ریاضیاتی آپریشنز شامل کریں  
- غلط آپریشنز کے لیے error handling شامل کریں  
- request/response logging شامل کریں  
- authentication نافذ کریں  
- unit tests شامل کریں

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔