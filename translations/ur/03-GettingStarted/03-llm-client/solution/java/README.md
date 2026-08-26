# کیلکولیٹر LLM کلائنٹ

ایک جاوا ایپلیکیشن جو دکھاتی ہے کہ کس طرح LangChain4j کو MiniMax OpenAI-مطابق API کے ذریعے MCP (ماڈل کانٹیکسٹ پروٹوکول) کیلکولیٹر سروس سے جڑنے کے لیے استعمال کیا جاتا ہے۔

## ضروریات

- جاوا 21 یا اس سے اوپر
- Maven 3.6+ (یا شامل Maven ریپر استعمال کریں)
- ایک MiniMax API کلید
- ایک MCP کیلکولیٹر سروس جو `http://localhost:8080` پر چل رہی ہو

## API کلید حاصل کرنا

یہ ایپلیکیشن MiniMax OpenAI-مطابق API کا استعمال کرتی ہے۔ اپنی کلید اور اینڈپوائنٹ حاصل کرنے کے لیے یہ اقدامات کریں:

### 1. ایک اینڈپوائنٹ کا انتخاب کریں
1. عالمی اینڈپوائنٹ کے لیے `https://api.minimax.io/v1` استعمال کریں
2. چین کے اینڈپوائنٹ کے لیے `https://api.minimaxi.com/v1` استعمال کریں

### 2. ایک API کلید بنائیں
1. اپنی MiniMax اکاؤنٹ سے MiniMax API کلید بنائیں
2. کلید کو کہیں محفوظ رکھیں

### 3. ماحول کے متغیرات سیٹ کریں

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

1. **پروجیکٹ ڈائریکٹری کلون کریں یا وہاں جائیں**

2. **انحصارات انسٹال کریں**:
   ```cmd
   mvnw clean install
   ```
   یا اگر Maven عالمی طور پر انسٹال ہے تو:
   ```cmd
   mvn clean install
   ```

3. **ماحول کے متغیرات سیٹ کریں** (مذکورہ "API کلید حاصل کرنا" سیکشن دیکھیں)

4. **MCP کیلکولیٹر سروس شروع کریں**:
   یقینی بنائیں کہ باب 1 کی MCP کیلکولیٹر سروس `http://localhost:8080/sse` پر چل رہی ہو۔ کلائنٹ شروع کرنے سے پہلے یہ چل رہی ہونی چاہیے۔

## ایپلیکیشن چلانا

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ایپلیکیشن کیا کرتی ہے

ایپلیکیشن کیلکولیٹر سروس کے ساتھ تین اہم تعاملات دکھاتی ہے:

1. **جمع**: 24.5 اور 17.3 کا مجموعہ نکالتی ہے
2. **اسکوائر روٹ**: 144 کا مربع جذر نکالتی ہے
3. **مدد**: دستیاب کیلکولیٹر فنکشنز دکھاتی ہے

## متوقع آؤٹ پٹ

کامیابی سے چلانے پر آپ کو درج ذیل جیسا آؤٹ پٹ دیکھنا چاہیے:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## مسئلے حل کرنا

### عام مسائل

1. **"OPENAI_API_KEY ماحول کا متغیر سیٹ نہیں ہے"**
   - یقینی بنائیں کہ `OPENAI_API_KEY` ماحول کا متغیر سیٹ کیا گیا ہے
   - متغیر سیٹ کرنے کے بعد اپنا ٹرمینل/کمانڈ پرامپٹ ری اسٹارٹ کریں

2. **"localhost:8080 سے کنکشن رد کر دیا گیا"**
   - یقینی بنائیں کہ MCP کیلکولیٹر سروس پورٹ 8080 پر چل رہی ہے
   - چیک کریں کہ کوئی اور سروس پورٹ 8080 استعمال نہیں کر رہی

3. **"تصدیق ناکام"**
   - اپنی API کلید کی درستگی کی جانچ کریں
   - چیک کریں کہ `OPENAI_BASE_URL` وہ اینڈپوائنٹ ہے جو آپ نے استعمال کرنا تھا

4. **Maven بلڈ کی غلطیاں**
   - یقینی بنائیں کہ آپ جاوا 21 یا اس سے اوپر استعمال کر رہے ہیں: `java -version`
   - بلڈ صاف کرنے کی کوشش کریں: `mvnw clean`

### ڈیبگنگ

ڈیبگ لاگنگ فعال کرنے کے لیے، چلانے کے وقت درج ذیل JVM آرگیومنٹ شامل کریں:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## ترتیب

ایپلیکیشن کی ترتیب یہ ہے:
- ڈیفالٹ کے طور پر MiniMax-M3 استعمال کریں، یا جب `MINIMAX_MODEL_ID` سیٹ ہو تو MiniMax-M2.7 استعمال کریں
- `OPENAI_BASE_URL` سے جڑیں جب یہ سیٹ ہو؛ ورنہ `MINIMAX_REGION=cn_zh` ہونے پر `https://api.minimaxi.com/v1` استعمال کریں، یا ڈیفالٹ کے طور پر `https://api.minimax.io/v1`
- MCP سروس سے جڑیں `http://localhost:8080/sse` پر
- درخواستوں کے لیے 60 سیکنڈ کا ٹائم آؤٹ استعمال کریں

## انحصارات

اس پروجیکٹ میں استعمال ہونے والے کلیدی انحصارات:
- **LangChain4j**: AI انضمام اور ٹول مینجمنٹ کے لیے
- **LangChain4j MCP**: ماڈل کانٹیکسٹ پروٹوکول کی حمایت کے لیے
- **LangChain4j OpenAI آفیشل**: MiniMax OpenAI-مطابق API انضمام کے لیے
- **Spring Boot**: ایپلیکیشن فریم ورک اور انحصار انجیکشن کے لیے

## لائسنس

یہ پروجیکٹ Apache License 2.0 کے تحت لائسنس یافتہ ہے - تفصیلات کے لیے [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) فائل دیکھیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->