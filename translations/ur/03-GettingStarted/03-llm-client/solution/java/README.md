# کیلکولیٹر LLM کلائنٹ

> [!NOTE]
> یہ حل کورس کی وراثتی HTTP+SSE کیلکولیٹر سروس سے جڑتا ہے اور
> MCP `2025-11-25` SDK APIs کو ہدف بناتا ہے۔ یہ `2026-07-28` Streamable HTTP
> کی مثال نہیں ہے۔

ایک جاوا ایپلیکیشن جو LangChain4j کا استعمال کرتے ہوئے MCP (ماڈل کانٹیکسٹ پروٹوکول) کیلکولیٹر سروس سے MiniMax OpenAI-مطابق API کے ذریعے جڑنے کا مظاہرہ کرتی ہے۔

## ضروریات

- جاوا 21 یا اس سے زیادہ
- Maven 3.6+ (یا شامل Maven ریپر کا استعمال کریں)
- ایک MiniMax API کی
- ایک MCP کیلکولیٹر سروس جو `http://localhost:8080` پر چل رہی ہو

## API کی حاصل کرنا

یہ ایپلیکیشن MiniMax OpenAI-مطابق API کا استعمال کرتی ہے۔ اپنی کی اور اینڈ پوائنٹ حاصل کرنے کے لیے یہ اقدامات کریں:

### 1. ایک اینڈ پوائنٹ انتخاب کریں
1. گلوبل اینڈ پوائنٹ کے لیے `https://api.minimax.io/v1` استعمال کریں
2. چین کے اینڈ پوائنٹ کے لیے `https://api.minimaxi.com/v1` استعمال کریں

### 2. ایک API کی بنائیں
1. اپنے MiniMax اکاؤنٹ سے MiniMax API کی بنائیں
2. کی کو کہیں محفوظ رکھیں

### 3. ماحولیاتی متغیرات سیٹ کریں

#### ونڈوز پر (کمانڈ پرامپٹ):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### ونڈوز پر (پاور شیل):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### میک او ایس/لینکس پر:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## سیٹ اپ اور تنصیب

1. **پروجیکٹ ڈائریکٹری کلون یا اس پر جائیں**

2. **درکار پیکجز انسٹال کریں**:
   ```cmd
   mvnw clean install
   ```
    یا اگر Maven عالمی سطح پر انسٹال ہے تو:
   ```cmd
   mvn clean install
   ```

3. **ماحولیاتی متغیرات سیٹ کریں** (اوپر "API کی حاصل کرنا" سیکشن دیکھیں)

4. **MCP کیلکولیٹر سروس شروع کریں**:
   یقینی بنائیں کہ باب 1 کی MCP کیلکولیٹر سروس `http://localhost:8080/sse` پر چل رہی ہو۔ اسے کلائنٹ شروع کرنے سے پہلے چلنا چاہیے۔

## ایپلیکیشن چلائیں

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ایپلیکیشن کیا کرتی ہے

ایپلیکیشن کیلکولیٹر سروس کے ساتھ تین اہم تعاملات کا مظاہرہ کرتی ہے:

1. **جمع**: 24.5 اور 17.3 کا مجموعہ حساب کرتی ہے
2. **اسکوائر روٹ**: 144 کا اسکوائر روٹ حساب کرتی ہے
3. **مدد**: دستیاب کیلکولیٹر فنکشنز دکھاتی ہے

## متوقع نتیجہ

کامیابی سے چلنے پر، آپ کو اس طرح کا نتیجہ دیکھنا چاہیے:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## مسائل کا حل

### عام مسائل

1. **"OPENAI_API_KEY ماحولیاتی متغیر سیٹ نہیں ہے"**
   - یقینی بنائیں کہ آپ نے `OPENAI_API_KEY` ماحولیاتی متغیر سیٹ کیا ہے
   - متغیر سیٹ کرنے کے بعد اپنا ٹرمینل/کمانڈ پرامپٹ دوبارہ شروع کریں

2. **"localhost:8080 سے کنکشن انکار شدہ"**
   - اس بات کو یقینی بنائیں کہ MCP کیلکولیٹر سروس پورٹ 8080 پر چل رہی ہو
   - دیکھیں کہ کوئی اور سروس پورٹ 8080 استعمال تو نہیں کر رہی

3. **"تصدیق ناکام ہوئی"**
   - اپنی API کی کی درستگی کی تصدیق کریں
   - چیک کریں کہ `OPENAI_BASE_URL` آپ کی مطلوبہ اینڈ پوائنٹ کے مطابق ہے

4. **Maven کی بلڈ میں غلطیاں**
   - یقینی بنائیں کہ آپ جاوا 21 یا اس سے اوپر استعمال کر رہے ہیں: `java -version`
   - بلڈ صاف کرنے کی کوشش کریں: `mvnw clean`

### ڈی بگنگ

ڈی بگ لاگنگ کو فعال کرنے کے لیے، چلانے کے وقت درج ذیل JVM دلیل شامل کریں:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## کنفیگریشن

ایپلیکیشن کی کنفیگریشن یہ ہے:
- بذریعہ ڈیفالٹ MiniMax-M3 کا استعمال؛ `MINIMAX_MODEL_ID` سیٹ کر کے `MiniMax-M3` یا `MiniMax-M2.7` منتخب کریں
- جب `OPENAI_BASE_URL` سیٹ ہو تو اس سے جڑیں؛ ورنہ `MINIMAX_REGION=cn_zh` کے لیے `https://api.minimaxi.com/v1`، یا بصورت دیگر ڈیفالٹ میں `https://api.minimax.io/v1`
- MCP سروس `http://localhost:8080/sse` سے جڑیں
- درخواستوں کے لیے 60 سیکنڈ کا ٹائم آؤٹ استعمال کریں

## انحصار

اس پروجیکٹ میں استعمال ہونے والے کلیدی انحصار:
- **LangChain4j**: AI انضمام اور ٹول مینجمنٹ کے لیے
- **LangChain4j MCP**: ماڈل کانٹیکسٹ پروٹوکول سپورٹ کے لیے
- **LangChain4j OpenAI official**: MiniMax OpenAI-مطابق API انضمام کے لیے
- **Spring Boot**: ایپلیکیشن فریم ورک اور انحصار انجیکشن کے لیے

## لائسنس

یہ پروجیکٹ Apache License 2.0 کے تحت لائسنس یافتہ ہے - تفصیلات کے لیے [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) فائل دیکھیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->