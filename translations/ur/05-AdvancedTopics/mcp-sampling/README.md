> [!WARNING]
> MCP `2026-07-28` میں سیمپلنگ منسوخ کر دی گئی ہے۔ یہ سبق 
> پرانے نفاذ کے لیے رکھا گیا ہے۔ نئے سرورز کو چاہیے کہ وہ براہ راست ایک LLM
> فراہم کنندہ API کے ساتھ انضمام کریں۔

# ماڈل کانٹیکسٹ پروٹوکول میں سیمپلنگ

> مطابقت کے لیے `2026-07-28` وضاحت میں سیمپلنگ برقرار ہے اور یہ
> 28 جولائی، 2027 کے بعد پہلی نظرثانی میں ہٹائے جانے کے لیے اہل ہے۔
> اس سبق کی مثالیں SDK APIs استعمال کر سکتی ہیں جو `2025-11-25` کو نافذ کرتی ہیں۔
> دیکھیں [MCP میں کیا تبدیل ہوا: 2026-07-28 کی وضاحت](../../01-CoreConcepts/mcp-2026-07-28.md)۔

پرانے MCP نفاذ میں، سیمپلنگ سرورز کو کلائنٹ کے ذریعے LLM
تکمیل کی درخواست کرنے کی اجازت دیتی ہے۔ یہ سبق اس منسوخ شدہ پروٹوکول
کے بہاؤ کی وضاحت کرتا ہے تاکہ مطابقت اور منتقلی کے کام میں مدد ملے۔

## تعارف

اس سبق میں، ہم جانچیں گے کہ MCP درخواستوں میں سیمپلنگ کے پیرامیٹرز کو کیسے ترتیب دیا جائے اور سیمپلنگ کے بنیادی پروٹوکول میکانکس کو سمجھیں۔

## تعلیمی مقاصد

اس سبق کے اختتام تک، آپ قادر ہو جائیں گے کہ:

- MCP میں دستیاب اہم سیمپلنگ پیرامیٹرز کو سمجھیں۔
- مختلف استعمال کے معاملات کے لیے سیمپلنگ پیرامیٹرز کو ترتیب دیں۔
- دوبارہ پیدا ہونے والے نتائج کے لیے یقینی سیمپلنگ کو نافذ کریں۔
- سیاق و سباق اور صارف کی ترجیحات کی بنیاد پر سیمپلنگ پیرامیٹرز کو متحرک طور پر ایڈجسٹ کریں۔
- مختلف حالات میں ماڈل کی کارکردگی کو بہتر بنانے کے لیے سیمپلنگ حکمت عملیوں کا اطلاق کریں۔
- MCP کے کلائنٹ-سرور بہاؤ میں سیمپلنگ کے کام کرنے کا طریقہ سمجھیں۔

## MCP میں سیمپلنگ کیسے کام کرتی ہے

MCP میں سیمپلنگ کا بہاؤ درج ذیل مراحل پر عمل کرتا ہے:

1. سرور کلائنٹ کو `sampling/createMessage` کی درخواست بھیجتا ہے
2. کلائنٹ درخواست کا جائزہ لیتا ہے اور اسے تبدیل کر سکتا ہے
3. کلائنٹ LLM سے سیمپلنگ کرتا ہے
4. کلائنٹ تکمیل کا جائزہ لیتا ہے
5. کلائنٹ نتیجہ سرور کو واپس کرتا ہے

یہ انسان-ان-دی-لوپ ڈیزائن یقینی بناتا ہے کہ صارفین اس بات پر کنٹرول رکھتے ہیں کہ LLM کیا دیکھتا اور جنریٹ کرتا ہے۔

## سیمپلنگ پیرامیٹرز کا جائزہ

MCP مندرجہ ذیل سیمپلنگ پیرامیٹرز کی وضاحت کرتا ہے جنہیں کلائنٹ درخواستوں میں ترتیب دیا جا سکتا ہے:

| پیرامیٹر | تفصیل | معمول کا رینج |
|-----------|-------------|---------------|
| `temperature` | ٹوکن کے انتخاب میں بے ترتیب پن کو کنٹرول کرتا ہے | 0.0 - 1.0 |
| `maxTokens` | پیدا کرنے والے ٹوکنز کی زیادہ سے زیادہ تعداد | عددی قدر |
| `stopSequences` | مخصوص سلسلے جو ملتے ہی جنریشن کو روکتے ہیں | سٹرنگز کی صف |
| `metadata` | اضافی فراہم کنندہ مخصوص پیرامیٹرز | JSON آبجیکٹ |

بہت سے LLM فراہم کنندہ اضافی پیرامیٹرز کو `metadata` فیلڈ کے ذریعے سپورٹ کرتے ہیں، جن میں شامل ہو سکتے ہیں:

| عام توسیعی پیرامیٹر | تفصیل | معمول کا رینج |
|-----------|-------------|---------------|
| `top_p` | نیوکلیئس سیمپلنگ - ٹوکنز کو اعلی مجموعی احتمال تک محدود کرتا ہے | 0.0 - 1.0 |
| `top_k` | ٹوکن انتخاب کو اعلی K اختیارات تک محدود کرتا ہے | 1 - 100 |
| `presence_penalty` | ٹیکسٹ میں موجودگی کی بنیاد پر ٹوکنز کو سزا دیتا ہے | -2.0 - 2.0 |
| `frequency_penalty` | متن میں کثرت کی بنیاد پر ٹوکنز کو سزا دیتا ہے | -2.0 - 2.0 |
| `seed` | دوبارہ پیدا ہونے والے نتائج کے لیے مخصوص رینڈم سیڈ | عددی قدر |

## درخواست کی مثال کا فارمیٹ

یہاں MCP میں کلائنٹ سے سیمپلنگ کی درخواست کی ایک مثال ہے:

```json
{
  "method": "sampling/createMessage",
  "params": {
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "What files are in the current directory?"
        }
      }
    ],
    "systemPrompt": "You are a helpful file system assistant.",
    "includeContext": "thisServer",
    "maxTokens": 100,
    "temperature": 0.7
  }
}
```

## جوابی فارمیٹ

کلائنٹ ایک تکمیل کا نتیجہ واپس کرتا ہے:

```json
{
  "model": "string",  // Name of the model used
  "stopReason": "endTurn" | "stopSequence" | "maxTokens" | "string",
  "role": "assistant",
  "content": {
    "type": "text",
    "text": "string"
  }
}
```

## انسان کے کنٹرول میں شامل

MCP سیمپلنگ انسان کی نگرانی کے ساتھ ڈیزائن کی گئی ہے:


- **پرامپٹس کے لیے**:
  - کلائنٹس کو صارفین کو مجوزہ پرامپٹ دکھانا چاہیے
  - صارفین پرامپٹس کو ترمیم یا رد کر سکتے ہیں
  - سسٹم پرامپٹس کو فلٹر یا ترمیم کیا جا سکتا ہے
  - کانٹیکسٹ کی شمولیت کا کنٹرول کلائنٹ کے پاس ہوتا ہے

- **کامیابیوں کے لیے**:
  - کلائنٹس کو صارفین کو مکمل نتیجہ دکھانا چاہیے
  - صارفین کامیابیوں کو ترمیم یا رد کر سکتے ہیں
  - کلائنٹس کامیابیوں کو فلٹر یا ترمیم کر سکتے ہیں
  - صارفین اس ماڈل کو کنٹرول کرتے ہیں جو استعمال کیا جاتا ہے

ان اصولوں کو ذہن میں رکھتے ہوئے، آئیے مختلف پروگرامنگ زبانوں میں سیمپلنگ کو کیسے نافذ کیا جائے، اس پر غور کریں، خاص طور پر ان پیرامیٹرز پر جو عام طور پر LLM فراہم کنندگان کے درمیان حمایت یافتہ ہوتے ہیں۔

## سیکیورٹی کے امور

MCP میں سیمپلنگ نافذ کرتے وقت، ان سیکیورٹی کی بہترین مشقوں پر غور کریں:

- **تمام پیغام کا مواد درست کریں** اس سے پہلے کہ اسے کلائنٹ کو بھیجا جائے
- **حساس معلومات کو صاف کریں** جو پرامپٹس اور کامیابیوں میں شامل ہوں
- **دھوکہ دہی کو روکنے کے لیے ریٹ کی پابندیاں نافذ کریں**
- **سیمپلنگ کے استعمال کی مانیٹرنگ کریں** تاکہ غیر معمولی پیٹرنز کا پتہ چل سکے
- **منتقلی میں ڈیٹا کو انکرپٹ کریں** محفوظ پروٹوکولز کا استعمال کرتے ہوئے
- **صارف کے ڈیٹا کی پرائیویسی کو سنبھالیں** متعلقہ ضوابط کے مطابق
- **سیمپلنگ درخواستوں کا آڈٹ کریں** تعمیل اور سیکیورٹی کے لیے
- **لاگت کے انکشاف کو کنٹرول کریں** مناسب حدود کے ذریعے
- **سیمپلنگ درخواستوں کے لیے ٹائم آؤٹ نافذ کریں**
- **ماڈل کی غلطیوں کو ہنر مندی سے سنبھالیں** مناسب بیک اپ کے ساتھ

سیمپلنگ پیرامیٹرز زبان کے ماڈلز کے رویے کو باریکی سے ایڈجسٹ کرنے کی اجازت دیتے ہیں تاکہ متعین اور تخلیقی نتائج کے درمیان مطلوبہ توازن حاصل کیا جا سکے۔

آئیے دیکھتے ہیں کہ ان پیرامیٹرز کو مختلف پروگرامنگ زبانوں میں کیسے ترتیب دیا جائے۔

# [.NET](#tab-dotnet)

```csharp
// .NET Example: Configuring sampling parameters in MCP
public class SamplingExample
{
    public async Task RunWithSamplingAsync()
    {
        // Create MCP client with sampling configuration
        var client = new McpClient("https://mcp-server-url.com");
        
        // Create request with specific sampling parameters
        var request = new McpRequest
        {
            Prompt = "Generate creative ideas for a mobile app",
            SamplingParameters = new SamplingParameters
            {
                Temperature = 0.8f,     // Higher temperature for more creative outputs
                TopP = 0.95f,           // Nucleus sampling parameter
                TopK = 40,              // Limit token selection to top K options
                FrequencyPenalty = 0.5f, // Reduce repetition
                PresencePenalty = 0.2f   // Encourage diversity
            },
            AllowedTools = new[] { "ideaGenerator", "marketAnalyzer" }
        };
        
        // Send request using specific sampling configuration
        var response = await client.SendRequestAsync(request);
        
        // Output results
        Console.WriteLine($"Generated with Temperature={request.SamplingParameters.Temperature}:");
        Console.WriteLine(response.GeneratedText);
    }
}
```

پچھلے کوڈ میں ہم نے:

- مخصوص سرور URL کے ساتھ ایک MCP کلائنٹ بنایا۔
- `temperature`, `top_p`, اور `top_k` جیسے سیمپلنگ پیرامیٹرز کے ساتھ ایک درخواست کو ترتیب دیا۔
- درخواست بھیجی اور تیار کردہ متن کو پرنٹ کیا۔
- استعمال کیا:
    - `allowedTools` جس کے ذریعے یہ تعین کیا کہ ماڈل جنریٹ کرنے کے دوران کون سے ٹولز استعمال کر سکتا ہے۔ اس صورت میں، ہم نے تخلیقی ایپ آئیڈیاز بنانے میں مدد کے لیے `ideaGenerator` اور `marketAnalyzer` ٹولز کی اجازت دی۔
    - `frequencyPenalty` اور `presencePenalty` آؤٹ پٹ میں تکرار اور تنوع کو کنٹرول کرنے کے لیے۔
    - `temperature` آؤٹ پٹ کی بے ترتیبیت کو کنٹرول کرنے کے لیے، جہاں زیادہ قیمتیں زیادہ تخلیقی جوابات کا باعث بنتی ہیں۔
    - `top_p` ٹوکنز کے انتخاب کو ان تک محدود کرنے کے لیے جو کُل احتمالی ماس میں نمایاں حصہ ڈالتے ہیں، جس سے تیار کردہ متن کے معیار میں اضافہ ہوتا ہے۔
    - `top_k` ماڈل کو سب سے زیادہ ممکنہ ٹوکنز میں محدود کرنے کے لیے، جو زیادہ مربوط جوابات پیدا کرنے میں مددگار ہو سکتے ہیں۔
    - `frequencyPenalty` اور `presencePenalty` تیار کردہ متن میں تکرار کو کم کرنے اور تنوع کو فروغ دینے کے لیے۔

# [JavaScript](#tab/javascript)

```javascript
// جاوا اسکرپٹ کی مثال: درجہ حرارت اور ٹاپ-پی سیمپلنگ کی ترتیبات
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // MCP کلائنٹ کو شروع کریں
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // مختلف سیمپلنگ پیرا میٹرز کے ساتھ درخواست تشکیل دیں
  const creativeSampling = {
    temperature: 0.9,    // زیادہ درجہ حرارت = زیادہ بے ترتیبی/تخلیقی صلاحیت
    topP: 0.92,          // ٹوکنز کو ۹۲٪ ممکنہ ماس کے ساتھ مد نظر رکھیں
    frequencyPenalty: 0.6, // ٹوکن سلسلوں کی تکرار کو کم کریں
    presencePenalty: 0.4   // ٹوکنز کو سزا دیں جو اب تک متن میں آ چکے ہیں
  };
  
  const factualSampling = {
    temperature: 0.2,    // کم درجہ حرارت = زیادہ متعین/حقیقت پسندانہ
    topP: 0.85,          // تھوڑا زیادہ مرکوز ٹوکن انتخاب
    frequencyPenalty: 0.2, // کم از کم تکرار کی سزا
    presencePenalty: 0.1   // کم از کم موجودگی کی سزا
  };
  
  try {
    // مختلف سیمپلنگ کنفیگریشنز کے ساتھ دو درخواستیں بھیجیں
    const creativeResponse = await client.sendPrompt(
      "Generate innovative ideas for sustainable urban transportation",
      {
        allowedTools: ['ideaGenerator', 'environmentalImpactTool'],
        ...creativeSampling
      }
    );
    
    const factualResponse = await client.sendPrompt(
      "Explain how electric vehicles impact carbon emissions",
      {
        allowedTools: ['factChecker', 'dataAnalysisTool'],
        ...factualSampling
      }
    );
    
    console.log('Creative Response (temperature=0.9):');
    console.log(creativeResponse.generatedText);
    
    console.log('\nFactual Response (temperature=0.2):');
    console.log(factualResponse.generatedText);
    
  } catch (error) {
    console.error('Error demonstrating sampling:', error);
  }
}

demonstrateSampling();
```

پچھلے کوڈ میں ہم نے:

- ایک سرور URL اور API کلید کے ساتھ MCP کلائنٹ کو انیشئیلائز کیا۔
- دو مختلف سیمپلنگ پیرامیٹرز کے سیٹ ترتیب دیے: ایک تخلیقی کاموں کے لیے اور دوسرا حقائق پر مبنی کاموں کے لیے۔
- ان ترتیبوں کے ساتھ درخواستیں بھیجی گئیں، ماڈل کو ہر کام کے لیے مخصوص ٹولز استعمال کرنے کی اجازت دی گئی۔
- تیار کردہ جوابات کو پرنٹ کیا تاکہ سیمپلنگ پیرامیٹرز کے مختلف اثرات کو ظاہر کیا جا سکے۔
- `allowedTools` استعمال کیا تاکہ ماڈل جنریشن کے دوران کون سے ٹولز استعمال کر سکتا ہے، یہ تعین کیا جا سکے۔ اس صورت میں ہم نے تخلیقی کاموں کے لیے `ideaGenerator` اور `environmentalImpactTool` کی اجازت دی، جبکہ حقائق پر مبنی کاموں کے لیے `factChecker` اور `dataAnalysisTool`۔
- `temperature` استعمال کیا تاکہ آؤٹ پٹ کی بے ترتیبیت کو کنٹرول کیا جا سکے، جہاں زیادہ قیمتیں زیادہ تخلیقی جوابات کا باعث بنتی ہیں۔

- `top_p` کا استعمال کیا گیا تاکہ ٹوکنز کے انتخاب کو اس حد تک محدود کیا جا سکے جو سب سے زیادہ مجموعی ممکنہ مقدار میں حصہ ڈالتے ہیں، جس سے تیار کردہ متن کا معیار بہتر ہوتا ہے۔
- `frequencyPenalty` اور `presencePenalty` کا استعمال کیا گیا تاکہ تکرار کم کی جا سکے اور آؤٹ پٹ میں تنوع کو فروغ دیا جا سکے۔
- `top_k` کا استعمال کیا گیا تاکہ ماڈل کو سب سے زیادہ ممکنہ K ٹوکنز تک محدود کیا جا سکے، جو زیادہ مربوط جوابات پیدا کرنے میں مددگار ہو سکتا ہے۔

---

## تعیناتی نمونہ سازی

ایسے درخواستوں کے لیے جن میں مستقل آؤٹ پٹ کی ضرورت ہو، تعیناتی نمونہ سازی قابل تکرار نتائج کو یقینی بناتی ہے۔ یہ کام اس طرح ہوتا ہے کہ ایک مقررہ رینڈم سیڈ استعمال کی جاتی ہے اور درجہ حرارت صفر پر سیٹ کیا جاتا ہے۔

آئیے مختلف پروگرامنگ زبانوں میں تعیناتی نمونہ سازی کو دکھانے کے لیے نیچے ایک نمونہ کا جائزہ لیتے ہیں۔

# [Java](#tab/java)

```java
// جیوہ مثال: مقررہ بیج کے ساتھ متعین جوابات
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // متعین نتائج کے لئے مقررہ بیج کا استعمال
        
        // پہلے درخواست مقررہ بیج کے ساتھ
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // زیادہ سے زیادہ تعینیت کے لئے صفر درجہ حرارت
            .build();
            
        // دوسری درخواست ایک ہی بیج کے ساتھ
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // دونوں درخواستیں چلائیں
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // جوابات ایک جیسے ہونے چاہئیں کیونکہ بیج اور درجہ حرارت = 0 ایک ہی ہے
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

پچھلے کوڈ میں ہم نے:

- مخصوص سرور URL کے ساتھ ایک MCP کلائنٹ بنایا۔
- دو درخواستیں ویسی ہی پرامپٹ، مقررہ سیڈ، اور صفر درجہ حرارت کے ساتھ ترتیب دیں۔
- دونوں درخواستیں بھیجیں اور تیار شدہ متن کو پرنٹ کیا۔
- دکھایا کہ جوابات ایک جیسے ہیں کیونکہ نمونہ سازی کی ترتیب تعیناتی نوعیت کی ہے (ویسا ہی سیڈ اور درجہ حرارت)۔
- `setSeed` کا استعمال کیا گیا تاکہ مقررہ رینڈم سیڈ بتائی جا سکے، یہ یقینی بناتے ہوئے کہ ماڈل ہر بار ایک جیسے ان پٹ کے لیے ایک جیسا آؤٹ پٹ تیار کرے۔
- `temperature` کو صفر پر سیٹ کیا گیا تاکہ زیادہ سے زیادہ تعیناتی کی ضمانت دی جا سکے، یعنی ماڈل ہمیشہ سب سے زیادہ ممکنہ اگلے ٹوکن کا انتخاب کرے گا بغیر رینڈم پن کے۔

# [JavaScript](#tab/javascript-deterministic)

```javascript
// جاوا اسکرپٹ کی مثال: سیڈ کنٹرول کے ساتھ تعین کن جوابات
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // پہلا درخواست فکسڈ سیڈ کے ساتھ
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // زیادہ سے زیادہ تعین کے لیے صفر درجہ حرارت
    });
    
    // دوسرا درخواست ایک ہی سیڈ اور درجہ حرارت کے ساتھ
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // تیسرا درخواست مختلف سیڈ لیکن ایک ہی درجہ حرارت کے ساتھ
    const response3 = await client.sendPrompt(prompt, {
      seed: 67890,
      temperature: 0.0
    });
    
    console.log('Response 1:', response1.generatedText);
    console.log('Response 2:', response2.generatedText);
    console.log('Response 3:', response3.generatedText);
    console.log('Responses 1 and 2 match:', response1.generatedText === response2.generatedText);
    console.log('Responses 1 and 3 match:', response1.generatedText === response3.generatedText);
    
  } catch (error) {
    console.error('Error in deterministic sampling demo:', error);
  }
}

deterministicSampling();
```

پچھلے کوڈ میں ہم نے:

- ایک MCP کلائنٹ ایک سرور URL کے ساتھ شروع کیا۔
- دو درخواستیں ویسی ہی پرامپٹ، مقررہ سیڈ، اور صفر درجہ حرارت کے ساتھ ترتیب دیں۔
- دونوں درخواستیں بھیجیں اور تیار شدہ متن کو پرنٹ کیا۔
- دکھایا کہ جوابات ایک جیسے ہیں کیونکہ نمونہ سازی کی ترتیب تعیناتی نوعیت کی ہے (ویسا ہی سیڈ اور درجہ حرارت)۔
- `seed` کا استعمال کیا گیا تاکہ مقررہ رینڈم سیڈ بتایا جا سکے، یہ یقینی بناتے ہوئے کہ ماڈل ہر بار ایک جیسے ان پٹ کے لیے ایک جیسا آؤٹ پٹ تیار کرے۔
- `temperature` کو صفر پر سیٹ کیا گیا تاکہ زیادہ سے زیادہ تعیناتی کی ضمانت دی جا سکے، یعنی ماڈل ہمیشہ سب سے زیادہ ممکنہ اگلے ٹوکن کا انتخاب کرے گا بغیر رینڈم پن کے۔
- تیسرے درخواست کے لیے مختلف سیڈ استعمال کیا گیا تاکہ دکھایا جا سکے کہ سیڈ کو بدلنے سے مختلف آؤٹ پٹس پیدا ہوتے ہیں، چاہے پرامپٹ اور درجہ حرارت ویسے ہی ہوں۔

---

## متحرک نمونہ ساز ترتیب

ذہین نمونہ سازی ہر درخواست کے معیار اور سیاق و سباق کے مطابق پیرامیٹرز کو موافق بناتی ہے۔ اس کا مطلب ہے درجہ حرارت، top_p، اور سزاؤں کو متحرک طور پر ایڈجسٹ کرنا، جو کام کی نوعیت، صارف کی ترجیحات، یا ماضی کی کارکردگی پر مبنی ہو۔

آئیے دیکھتے ہیں کہ متحرک نمونہ سازی کو مختلف پروگرامنگ زبانوں میں کیسے نافذ کیا جائے۔

# [Python](#tab/python)

```python
# پائتھن مثال: درخواست کے سیاق و سباق پر مبنی متحرک نمونہ
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # مختلف قسم کے کاموں کے لیے نمونہ پری سیٹ کی تعریف کریں
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # بنیادی پری سیٹ منتخب کریں
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # اگر فراہم کیا گیا ہو تو صارف کی ترجیحات کی بنیاد پر ایڈجسٹ کریں
        if user_preferences:
            if "creativity_level" in user_preferences:
                # تخلیقی صلاحیت کی ترجیح کی بنیاد پر درجہ حرارت کو اسکيل کریں (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # مطلوبہ جواب کی تنوع کی بنیاد پر top_p ایڈجسٹ کریں
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # حسب ضرورت نمونہ کے پیرامیٹرز کے ساتھ درخواست بنائیں اور بھیجیں
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # شفافیت کے لیے نمونہ میٹا ڈیٹا کے ساتھ جواب واپس کریں
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

پچھلے کوڈ میں ہم نے:

- `DynamicSamplingService` کلاس بنایا جو موافق نمونہ سازی کا انتظام کرتی ہے۔
- مختلف کاموں کی اقسام کے لیے نمونہ ساز پری سیٹس کی تعریف کی (تخلیقی، حقائق، کوڈ، تجزیاتی)۔
- کام کی نوعیت کی بنیاد پر ایک بنیادی نمونہ ساز پری سیٹ منتخب کیا۔
- صارف کی ترجیحات جیسے تخلیقی سطح اور تنوع کی بنیاد پر نمونہ ساز پیرامیٹرز کو ایڈجسٹ کیا۔
- متحرک طور پر ترتیب دیے گئے نمونہ ساز پیرامیٹرز کے ساتھ درخواست بھیجی۔
- تیار کردہ متن کو ساتھ ساتھ استعمال کیے گئے نمونہ ساز پیرامیٹرز اور کام کی نوعیت کے ساتھ شفافیت کے لیے واپس کیا۔
- `temperature` کا استعمال کیا تاکہ آؤٹ پٹ کی بے ترتیبیت کو کنٹرول کیا جا سکے، جہاں زیادہ قدرات زیادہ تخلیقی جوابات کی طرف لے جاتی ہیں۔
- `top_p` کا استعمال کیا تاکہ ٹوکنز کے انتخاب کو اس حد تک محدود کیا جا سکے جو سب سے زیادہ مجموعی ممکنہ مقدار میں حصہ ڈالتے ہیں، جس سے تیار کردہ متن کا معیار بہتر ہوتا ہے۔
- `frequency_penalty` کا استعمال کیا تاکہ تکرار کم کی جا سکے اور آؤٹ پٹ میں تنوع کو فروغ دیا جا سکے۔
- `user_preferences` کا استعمال کیا تاکہ صارف کی تخلیقی اور تنوع کی سطحوں کی بنیاد پر نمونہ ساز پیرامیٹرز کو اپنی مرضی کے مطابق بنانے کی اجازت دی جا سکے۔
- `task_type` کا استعمال کیا تاکہ درخواست کے لیے مناسب نمونہ ساز حکمت عملی کا تعین کیا جا سکے، جس سے کام کی نوعیت کی بنیاد پر زیادہ مناسب جوابات ممکن ہوں۔
- `send_request` طریقہ کار کا استعمال کیا گیا تاکہ ترتیب دیے گئے نمونہ ساز پیرامیٹرز کے ساتھ پرامپٹ بھیجا جائے، یہ یقینی بناتے ہوئے کہ ماڈل مذکورہ ضروریات کے مطابق متن تیار کرے۔
- `generated_text` کا استعمال کیا گیا تاکہ ماڈل کے جواب کو حاصل کیا جائے، جو پھر نمونہ ساز پیرامیٹرز اور کام کی نوعیت کے ساتھ اگلے تجزیے یا نمائش کے لیے واپس کیا جاتا ہے۔
- `min` اور `max` افعال کا استعمال کیا گیا تاکہ یہ یقینی بنایا جا سکے کہ صارف کی ترجیحات درست حدود کے اندر ہوں، غیر معتبر نمونہ ساز ترتیبات سے روکتے ہوئے۔

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// جاوا اسکرپٹ کی مثال: صارف کے سیاق و سباق کی بنیاد پر متحرک سیمپلنگ کنفیگریشن
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // بنیادی سیمپلنگ پروفائلز کی تعریف کریں
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // تاریخی کارکردگی کو ٹریک کریں
    this.performanceHistory = [];
  }
  
  // پرامپٹ سے ٹاسک کی قسم کا پتہ لگائیں
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // سادہ ہیورسٹک کا پتہ لگانا - ایم ایل کلاسفیکیشن کے ساتھ اسے بہتر بنایا جا سکتا ہے
    if (context.taskType) return context.taskType;
    
    if (promptLower.includes('code') || 
        promptLower.includes('function') || 
        promptLower.includes('program')) {
      return 'code';
    }
    
    if (promptLower.includes('explain') || 
        promptLower.includes('what is') || 
        promptLower.includes('how does')) {
      return 'factual';
    }
    
    if (promptLower.includes('creative') || 
        promptLower.includes('imagine') || 
        promptLower.includes('story')) {
      return 'creative';
    }
    
    // اگر کوئی واضح قسم نہیں ملتی تو بات چیت پر ڈیفالٹ کریں
    return 'conversational';
  }
  
  // سیاق و سباق اور صارف کی ترجیحات کی بنیاد پر سیمپلنگ پیرا میٹرز کا حساب لگائیں
  getSamplingParameters(prompt, context = {}) {
    // ٹاسک کی قسم کا پتہ لگائیں
    const taskType = this.detectTaskType(prompt, context);
    
    // بنیادی پروفائل حاصل کریں
    let params = {...this.samplingProfiles[taskType]};
    
    // صارف کی ترجیحات کی بنیاد پر ایڈجسٹ کریں
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // 1-10 سے مناسب درجہ حرارت کی حد تک اسکیل کریں
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // زیادہ درستگی کا مطلب ہے کم topP (زیادہ مرکوز انتخاب)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // زیادہ مستقل مزاجی کا مطلب ہے کم سزائیں
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // کارکردگی کی تاریخ سے سیکھی گئی ترتیبات لاگو کریں
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // سادہ مطابقت پذیری منطق - مزید پیچیدہ الگورتھمز کے ساتھ بہتر بنایا جا سکتا ہے
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // صرف حالیہ تاریخ پر غور کریں
    
    if (relevantHistory.length > 0) {
      // اوسط کارکردگی کے سکور کا حساب لگائیں
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // اگر کارکردگی حد سے کم ہو تو پیرا میٹرز کو ایڈجسٹ کریں
      if (avgScore < 0.7) {
        // محفوظ اقدار کی طرف معمولی ایڈجسٹمنٹ
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // مستقبل کی ترتیبات کے لئے کارکردگی کی ریکارڈنگ کریں
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // جواب کے معیار کی 0-1 درجہ بندی
    });
    
    // تاریخ کا حجم محدود کریں
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // بہتر کردہ سیمپلنگ پیرا میٹرز حاصل کریں
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // بہتر کردہ پیرا میٹرز کے ساتھ درخواست بھیجیں
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // اگر صارف فیڈ بیک فراہم کرتا ہے تو اسے مستقبل کی بہتری کے لئے ریکارڈ کریں
    if (context.recordPerformance) {
      this.recordPerformance(prompt, samplingParams, response, context.feedbackScore || 0.5);
    }
    
    return {
      response,
      appliedSamplingParams: samplingParams,
      detectedTaskType: this.detectTaskType(prompt, context)
    };
  }
}

// استعمال کی مثال
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // حسب ضرورت صارف کی ترجیحات کے ساتھ تخلیقی ٹاسک
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // زیادہ تخلیقیت (1-10)
          consistency: 3  // کم مستقل مزاجی (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // کوڈ جنریشن کا ٹاسک
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // کم تخلیقیت
          precision: 8,   // زیادہ درستگی
          consistency: 9  // زیادہ مستقل مزاجی
        }
      }
    );
    
    console.log('\nCode Task:');
    console.log(`Detected type: ${codeResult.detectedTaskType}`);
    console.log('Applied sampling:', codeResult.appliedSamplingParams);
    console.log(codeResult.response.generatedText);
    
  } catch (error) {
    console.error('Error in adaptive sampling demo:', error);
  }
}

demonstrateAdaptiveSampling();
```

پچھلے کوڈ میں ہم نے:

- `AdaptiveSamplingManager` کلاس بنایا جو کام کی نوعیت اور صارف کی ترجیحات کی بنیاد پر متحرک نمونہ سازی کا انتظام کرتی ہے۔
- مختلف کام کی اقسام کے لیے نمونہ ساز پروفائلز کی تعریف کی (تخلیقی، حقائق، کوڈ، گفتگو)۔
- سادہ اصولوں کے ذریعے پرامپٹ سے کام کی نوعیت کا پتہ لگانے کا طریقہ کار نافذ کیا۔
- پتہ چلی ہوئی کام کی نوعیت اور صارف کی ترجیحات کی بنیاد پر نمونہ ساز پیرامیٹرز کا حساب لگایا۔
- ماضی کی کارکردگی کی بنیاد پر سیکھی ہوئی ایڈجسٹمنٹ لاگو کی تاکہ نمونہ ساز پیرامیٹرز بہتر ہو سکیں۔
- مستقبل کی ایڈجسٹمنٹ کے لیے کارکردگی کا ریکارڈ رکھا، جس سے نظام ماضی کے تعاملات سے سیکھ سکے۔
- متحرک طور پر ترتیب دیے گئے نمونہ ساز پیرامیٹرز کے ساتھ درخواستیں بھیجیں اور تیار شدہ متن کو اطلاق شدہ پیرامیٹرز اور پتہ چلی ہوئی کام کی نوعیت کے ساتھ واپس کیا۔
- استعمال کیا:
    - `userPreferences` تاکہ صارف کی تخلیقی، درستگی، اور مستقل مزاجی کی سطحوں کی بنیاد پر نمونہ ساز پیرامیٹرز کو اپنی مرضی کے مطابق بنایا جا سکے۔
    - `detectTaskType` تاکہ پرامپٹ کی بنیاد پر کام کی نوعیت کا تعین کیا جا سکے، جس سے زیادہ موزوں جوابات کی اجازت ملے۔
    - `recordPerformance` تاکہ تیار کردہ جوابات کی کارکردگی کو ریکارڈ کیا جا سکے، جس سے نظام وقت کے ساتھ خود کو بہتر بنا سکے۔
    - `applyLearnedAdjustments` تاکہ ماضی کی کارکردگی کی بنیاد پر نمونہ ساز پیرامیٹرز میں ترمیم کی جا سکے، ماڈل کی اعلیٰ معیار کے جوابات پیدا کرنے کی صلاحیت کو بڑھاتے ہوئے۔
    - `generateResponse` تاکہ موافق نمونہ سازی کے مکمل عمل کو انکیپسولیٹ کیا جا سکے، جس سے اسے مختلف پرامپٹس اور سیاق و سباق کے ساتھ آسانی سے کال کیا جا سکے۔
    - `allowedTools` تاکہ اس بات کا تعین کیا جا سکے کہ ماڈل پیداوار کے دوران کون سے اوزار استعمال کر سکتا ہے، جس سے زیادہ سیاق و سباق سے واقف جوابات ممکن ہوں۔
    - `feedbackScore` تاکہ صارفین کو تیار کردہ جواب کے معیار پر فیڈبیک دینے کی اجازت دی جا سکے، جسے وقت کے ساتھ ماڈل کی کارکردگی کو بہتر بنانے کے لیے استعمال کیا جا سکتا ہے۔
    - `performanceHistory` تاکہ ماضی کے تعاملات کا ریکارڈ رکھا جا سکے، جس سے نظام گزشتہ کامیابیوں اور ناکامیوں سے سیکھ سکے۔
    - `getSamplingParameters` تاکہ درخواست کے سیاق و سباق کی بنیاد پر نمونہ ساز پیرامیٹرز کو متحرک طور پر ایڈجسٹ کیا جا سکے، جس سے ماڈل کے رویے میں زیادہ لچکدار اور جوابدہ پن ہو۔
    - `detectTaskType` تاکہ پرامپٹ کی بنیاد پر کام کی درجہ بندی کی جا سکے، جس سے نظام کو مختلف قسم کی درخواستوں کے لیے مناسب نمونہ ساز حکمت عملی لاگو کرنے کی اجازت ملے۔
    - `samplingProfiles` تاکہ مختلف کام کی اقسام کے لیے بنیادی نمونہ ساز ترتیب کی تعریف کی جا سکے، جو درخواست کی نوعیت کی بنیاد پر تیز تر ایڈجسٹمنٹ کی اجازت دیتی ہے۔

---

## آگے کیا ہے

- [5.7 اسکیلنگ](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->