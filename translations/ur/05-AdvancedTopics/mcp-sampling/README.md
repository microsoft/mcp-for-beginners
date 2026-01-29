# ماڈل کانٹیکسٹ پروٹوکول میں سیمپلنگ

سیمپلنگ ایک طاقتور MCP خصوصیت ہے جو سرورز کو کلائنٹ کے ذریعے LLM مکمل کرنے کی درخواست کرنے کی اجازت دیتی ہے، جس سے پیچیدہ ایجنٹک رویے ممکن ہوتے ہیں جبکہ سیکیورٹی اور پرائیویسی برقرار رہتی ہے۔ درست سیمپلنگ کنفیگریشن ردعمل کے معیار اور کارکردگی کو نمایاں طور پر بہتر بنا سکتی ہے۔ MCP ایک معیاری طریقہ فراہم کرتا ہے کہ ماڈلز مخصوص پیرامیٹرز کے ساتھ متن کیسے تیار کرتے ہیں جو بے ترتیبی، تخلیقی صلاحیت، اور ہم آہنگی کو متاثر کرتے ہیں۔

## تعارف

اس سبق میں، ہم MCP درخواستوں میں سیمپلنگ پیرامیٹرز کو ترتیب دینا سیکھیں گے اور سیمپلنگ کے بنیادی پروٹوکول میکانکس کو سمجھیں گے۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ قابل ہوں گے:

- MCP میں دستیاب اہم سیمپلنگ پیرامیٹرز کو سمجھنا۔
- مختلف استعمال کے کیسز کے لیے سیمپلنگ پیرامیٹرز کو ترتیب دینا۔
- قابلِ تکرار نتائج کے لیے ڈیٹرمینسٹک سیمپلنگ کو نافذ کرنا۔
- سیاق و سباق اور صارف کی ترجیحات کی بنیاد پر سیمپلنگ پیرامیٹرز کو متحرک طور پر ایڈجسٹ کرنا۔
- مختلف حالات میں ماڈل کی کارکردگی کو بہتر بنانے کے لیے سیمپلنگ حکمت عملیوں کا اطلاق کرنا۔
- MCP کے کلائنٹ-سرور فلو میں سیمپلنگ کے کام کرنے کے طریقہ کار کو سمجھنا۔

## MCP میں سیمپلنگ کیسے کام کرتی ہے

MCP میں سیمپلنگ کا عمل درج ذیل مراحل پر مشتمل ہے:

1. سرور کلائنٹ کو `sampling/createMessage` درخواست بھیجتا ہے  
2. کلائنٹ درخواست کا جائزہ لیتا ہے اور اسے تبدیل کر سکتا ہے  
3. کلائنٹ LLM سے سیمپلنگ کرتا ہے  
4. کلائنٹ مکمل شدہ مواد کا جائزہ لیتا ہے  
5. کلائنٹ نتیجہ سرور کو واپس بھیجتا ہے  

یہ انسانی مداخلت والا ڈیزائن یقینی بناتا ہے کہ صارفین اس بات پر قابو رکھتے ہیں کہ LLM کیا دیکھتا اور تیار کرتا ہے۔

## سیمپلنگ پیرامیٹرز کا جائزہ

MCP درج ذیل سیمپلنگ پیرامیٹرز کی وضاحت کرتا ہے جنہیں کلائنٹ درخواستوں میں ترتیب دیا جا سکتا ہے:

| پیرامیٹر | وضاحت | عام حد |
|-----------|-------------|---------------|
| `temperature` | ٹوکن کے انتخاب میں بے ترتیبی کو کنٹرول کرتا ہے | 0.0 - 1.0 |
| `maxTokens` | تیار کیے جانے والے زیادہ سے زیادہ ٹوکنز کی تعداد | عددی قدر |
| `stopSequences` | مخصوص سلسلے جو جنریشن کو روک دیتے ہیں جب ملتے ہیں | سٹرنگز کی فہرست |
| `metadata` | اضافی فراہم کنندہ مخصوص پیرامیٹرز | JSON آبجیکٹ |

بہت سے LLM فراہم کنندگان `metadata` فیلڈ کے ذریعے اضافی پیرامیٹرز کی حمایت کرتے ہیں، جن میں شامل ہو سکتے ہیں:

| عام اضافی پیرامیٹر | وضاحت | عام حد |
|-----------|-------------|---------------|
| `top_p` | نیوکلئیس سیمپلنگ - ٹوکنز کو اعلیٰ مجموعی احتمال تک محدود کرتا ہے | 0.0 - 1.0 |
| `top_k` | ٹوکن کے انتخاب کو اعلیٰ K اختیارات تک محدود کرتا ہے | 1 - 100 |
| `presence_penalty` | اب تک متن میں موجود ٹوکنز کی بنیاد پر سزا دیتا ہے | -2.0 - 2.0 |
| `frequency_penalty` | اب تک متن میں ٹوکنز کی تکرار کی بنیاد پر سزا دیتا ہے | -2.0 - 2.0 |
| `seed` | قابلِ تکرار نتائج کے لیے مخصوص رینڈم سیڈ | عددی قدر |

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

## جواب کا فارمیٹ

کلائنٹ ایک مکمل شدہ نتیجہ واپس کرتا ہے:

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

## انسانی مداخلت کے کنٹرولز

MCP سیمپلنگ انسانی نگرانی کے ساتھ ڈیزائن کی گئی ہے:

- **پرومپٹس کے لیے**:  
  - کلائنٹس کو صارفین کو تجویز کردہ پرومپٹ دکھانا چاہیے  
  - صارفین کو پرومپٹس میں ترمیم یا انکار کرنے کی اجازت ہونی چاہیے  
  - سسٹم پرومپٹس کو فلٹر یا تبدیل کیا جا سکتا ہے  
  - سیاق و سباق کی شمولیت کلائنٹ کے کنٹرول میں ہے  

- **مکمل کرنے کے لیے**:  
  - کلائنٹس کو صارفین کو مکمل شدہ مواد دکھانا چاہیے  
  - صارفین کو مکمل کرنے میں ترمیم یا انکار کرنے کی اجازت ہونی چاہیے  
  - کلائنٹس مکمل کرنے کو فلٹر یا تبدیل کر سکتے ہیں  
  - صارفین کنٹرول کرتے ہیں کہ کون سا ماڈل استعمال ہوتا ہے  

ان اصولوں کو ذہن میں رکھتے ہوئے، آئیے مختلف پروگرامنگ زبانوں میں سیمپلنگ کو نافذ کرنے کا طریقہ دیکھتے ہیں، خاص طور پر ان پیرامیٹرز پر توجہ دیتے ہوئے جو عام طور پر LLM فراہم کنندگان کے درمیان حمایت یافتہ ہیں۔

## سیکیورٹی کے پہلو

MCP میں سیمپلنگ کو نافذ کرتے وقت ان سیکیورٹی بہترین طریقوں پر غور کریں:

- **تمام پیغام کے مواد کی تصدیق کریں** اس سے پہلے کہ اسے کلائنٹ کو بھیجا جائے  
- **پرومپٹس اور مکمل کرنے سے حساس معلومات کو صاف کریں**  
- **دھوکہ دہی سے بچنے کے لیے ریٹ لمٹس نافذ کریں**  
- **سیمپلنگ کے استعمال کی غیر معمولی پیٹرنز کی نگرانی کریں**  
- **منتقلی کے دوران ڈیٹا کو محفوظ پروٹوکولز کے ذریعے انکرپٹ کریں**  
- **صارف کے ڈیٹا کی پرائیویسی کو متعلقہ قوانین کے مطابق سنبھالیں**  
- **مطابقت اور سیکیورٹی کے لیے سیمپلنگ درخواستوں کا آڈٹ کریں**  
- **مناسب حدود کے ساتھ لاگت کے اخراجات کو کنٹرول کریں**  
- **سیمپلنگ درخواستوں کے لیے ٹائم آؤٹ نافذ کریں**  
- **ماڈل کی غلطیوں کو مناسب متبادل کے ساتھ سنبھالیں**  

سیمپلنگ پیرامیٹرز زبان کے ماڈلز کے رویے کو باریک بینی سے ترتیب دینے کی اجازت دیتے ہیں تاکہ ڈیٹرمینسٹک اور تخلیقی آؤٹ پٹس کے درمیان مطلوبہ توازن حاصل کیا جا سکے۔

آئیے دیکھتے ہیں کہ مختلف پروگرامنگ زبانوں میں ان پیرامیٹرز کو کیسے ترتیب دیا جائے۔

# [.NET](../../../../05-AdvancedTopics/mcp-sampling)

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

- ایک مخصوص سرور URL کے ساتھ MCP کلائنٹ بنایا۔  
- `temperature`, `top_p`, اور `top_k` جیسے سیمپلنگ پیرامیٹرز کے ساتھ درخواست کو ترتیب دیا۔  
- درخواست بھیجی اور تیار شدہ متن کو پرنٹ کیا۔  
- استعمال کیا:  
    - `allowedTools` تاکہ ماڈل کو جنریشن کے دوران استعمال کرنے والے ٹولز کی وضاحت کی جا سکے۔ اس کیس میں، ہم نے تخلیقی ایپ آئیڈیاز تیار کرنے میں مدد کے لیے `ideaGenerator` اور `marketAnalyzer` ٹولز کی اجازت دی۔  
    - `frequencyPenalty` اور `presencePenalty` تاکہ آؤٹ پٹ میں تکرار اور تنوع کو کنٹرول کیا جا سکے۔  
    - `temperature` تاکہ آؤٹ پٹ کی بے ترتیبی کو کنٹرول کیا جا سکے، جہاں زیادہ قیمتیں زیادہ تخلیقی ردعمل کی طرف لے جاتی ہیں۔  
    - `top_p` تاکہ ٹوکن کے انتخاب کو اعلیٰ مجموعی احتمال ماس تک محدود کیا جا سکے، جس سے تیار شدہ متن کا معیار بہتر ہوتا ہے۔  
    - `top_k` تاکہ ماڈل کو سب سے زیادہ ممکنہ K ٹوکنز تک محدود کیا جا سکے، جو زیادہ ہم آہنگ ردعمل پیدا کرنے میں مدد دیتا ہے۔  
    - `frequencyPenalty` اور `presencePenalty` تاکہ تیار شدہ متن میں تکرار کو کم اور تنوع کو بڑھایا جا سکے۔  

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Temperature and Top-P sampling configuration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialize the MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configure request with different sampling parameters
  const creativeSampling = {
    temperature: 0.9,    // Higher temperature = more randomness/creativity
    topP: 0.92,          // Consider tokens with top 92% probability mass
    frequencyPenalty: 0.6, // Reduce repetition of token sequences
    presencePenalty: 0.4   // Penalize tokens that have appeared in the text so far
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lower temperature = more deterministic/factual
    topP: 0.85,          // Slightly more focused token selection
    frequencyPenalty: 0.2, // Minimal repetition penalty
    presencePenalty: 0.1   // Minimal presence penalty
  };
  
  try {
    // Send two requests with different sampling configurations
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

- سرور URL اور API کلید کے ساتھ MCP کلائنٹ کو انیشیئلائز کیا۔  
- دو سیٹ سیمپلنگ پیرامیٹرز ترتیب دیے: ایک تخلیقی کاموں کے لیے اور دوسرا حقائق پر مبنی کاموں کے لیے۔  
- ان کنفیگریشنز کے ساتھ درخواستیں بھیجیں، ماڈل کو ہر کام کے لیے مخصوص ٹولز استعمال کرنے کی اجازت دی۔  
- تیار شدہ جوابات کو پرنٹ کیا تاکہ مختلف سیمپلنگ پیرامیٹرز کے اثرات کو ظاہر کیا جا سکے۔  
- استعمال کیا:  
    - `allowedTools` تاکہ ماڈل کو جنریشن کے دوران استعمال کرنے والے ٹولز کی وضاحت کی جا سکے۔ اس کیس میں، تخلیقی کاموں کے لیے `ideaGenerator` اور `environmentalImpactTool`، اور حقائق پر مبنی کاموں کے لیے `factChecker` اور `dataAnalysisTool` کی اجازت دی گئی۔  
    - `temperature` تاکہ آؤٹ پٹ کی بے ترتیبی کو کنٹرول کیا جا سکے، جہاں زیادہ قیمتیں زیادہ تخلیقی ردعمل کی طرف لے جاتی ہیں۔  
    - `top_p` تاکہ ٹوکن کے انتخاب کو اعلیٰ مجموعی احتمال ماس تک محدود کیا جا سکے، جس سے تیار شدہ متن کا معیار بہتر ہوتا ہے۔  
    - `frequencyPenalty` اور `presencePenalty` تاکہ آؤٹ پٹ میں تکرار کو کم اور تنوع کو بڑھایا جا سکے۔  
    - `top_k` تاکہ ماڈل کو سب سے زیادہ ممکنہ K ٹوکنز تک محدود کیا جا سکے، جو زیادہ ہم آہنگ ردعمل پیدا کرنے میں مدد دیتا ہے۔  

---

## ڈیٹرمینسٹک سیمپلنگ

ایپلیکیشنز کے لیے جو مستقل نتائج چاہتی ہیں، ڈیٹرمینسٹک سیمپلنگ قابلِ تکرار نتائج کو یقینی بناتی ہے۔ یہ کام ایک مقررہ رینڈم سیڈ استعمال کر کے اور temperature کو صفر پر سیٹ کر کے کیا جاتا ہے۔

آئیے نیچے مختلف پروگرامنگ زبانوں میں ڈیٹرمینسٹک سیمپلنگ کی مثال دیکھتے ہیں۔

# [Java](../../../../05-AdvancedTopics/mcp-sampling)

```java
// Java Example: Deterministic responses with fixed seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Using a fixed seed for deterministic results
        
        // First request with fixed seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperature for maximum determinism
            .build();
            
        // Second request with the same seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Execute both requests
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Responses should be identical due to same seed and temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

پچھلے کوڈ میں ہم نے:

- ایک مخصوص سرور URL کے ساتھ MCP کلائنٹ بنایا۔  
- ایک ہی پرومپٹ، مقررہ سیڈ، اور صفر temperature کے ساتھ دو درخواستیں ترتیب دیں۔  
- دونوں درخواستیں بھیجیں اور تیار شدہ متن کو پرنٹ کیا۔  
- دکھایا کہ جوابات سیمپلنگ کنفیگریشن کی ڈیٹرمینسٹک نوعیت (ایک جیسا سیڈ اور temperature) کی وجہ سے ایک جیسے ہیں۔  
- `setSeed` استعمال کیا تاکہ ایک مقررہ رینڈم سیڈ دیا جا سکے، جس سے ماڈل ہر بار ایک ہی ان پٹ کے لیے ایک ہی آؤٹ پٹ تیار کرتا ہے۔  
- `temperature` کو صفر پر سیٹ کیا تاکہ زیادہ سے زیادہ ڈیٹرمینزم یقینی بنایا جا سکے، یعنی ماڈل ہمیشہ سب سے ممکنہ اگلا ٹوکن منتخب کرے گا بغیر کسی بے ترتیبی کے۔  

# [JavaScript](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Deterministic responses with seed control
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // First request with fixed seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero temperature for maximum determinism
    });
    
    // Second request with same seed and temperature
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Third request with different seed but same temperature
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

- ایک سرور URL کے ساتھ MCP کلائنٹ کو انیشیئلائز کیا۔  
- ایک ہی پرومپٹ، مقررہ سیڈ، اور صفر temperature کے ساتھ دو درخواستیں ترتیب دیں۔  
- دونوں درخواستیں بھیجیں اور تیار شدہ متن کو پرنٹ کیا۔  
- دکھایا کہ جوابات سیمپلنگ کنفیگریشن کی ڈیٹرمینسٹک نوعیت (ایک جیسا سیڈ اور temperature) کی وجہ سے ایک جیسے ہیں۔  
- `seed` استعمال کیا تاکہ ایک مقررہ رینڈم سیڈ دیا جا سکے، جس سے ماڈل ہر بار ایک ہی ان پٹ کے لیے ایک ہی آؤٹ پٹ تیار کرتا ہے۔  
- `temperature` کو صفر پر سیٹ کیا تاکہ زیادہ سے زیادہ ڈیٹرمینزم یقینی بنایا جا سکے، یعنی ماڈل ہمیشہ سب سے ممکنہ اگلا ٹوکن منتخب کرے گا بغیر کسی بے ترتیبی کے۔  
- تیسرے درخواست کے لیے مختلف سیڈ استعمال کیا تاکہ دکھایا جا سکے کہ سیڈ بدلنے سے مختلف آؤٹ پٹ آتے ہیں، چاہے پرومپٹ اور temperature ایک جیسے ہوں۔  

---

## متحرک سیمپلنگ کنفیگریشن

ذہین سیمپلنگ ہر درخواست کے سیاق و سباق اور ضروریات کی بنیاد پر پیرامیٹرز کو ایڈجسٹ کرتی ہے۔ اس کا مطلب ہے کہ temperature، top_p، اور penalties جیسے پیرامیٹرز کو کام کی نوعیت، صارف کی ترجیحات، یا تاریخی کارکردگی کی بنیاد پر متحرک طور پر ایڈجسٹ کیا جائے۔

آئیے مختلف پروگرامنگ زبانوں میں متحرک سیمپلنگ کو نافذ کرنے کا طریقہ دیکھتے ہیں۔

# [Python](../../../../05-AdvancedTopics/mcp-sampling)

```python
# Python Example: Dynamic sampling based on request context
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Define sampling presets for different task types
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Select base preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Adjust based on user preferences if provided
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Scale temperature based on creativity preference (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Adjust top_p based on desired response diversity
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Create and send request with custom sampling parameters
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Return response with sampling metadata for transparency
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

پچھلے کوڈ میں ہم نے:

- `DynamicSamplingService` کلاس بنائی جو ایڈاپٹیو سیمپلنگ کو منظم کرتی ہے۔  
- مختلف کام کی اقسام (تخلیقی، حقائق پر مبنی، کوڈ، تجزیاتی) کے لیے سیمپلنگ پری سیٹس کی تعریف کی۔  
- کام کی نوعیت کی بنیاد پر ایک بنیادی سیمپلنگ پری سیٹ منتخب کیا۔  
- صارف کی ترجیحات جیسے تخلیقی صلاحیت اور تنوع کی بنیاد پر سیمپلنگ پیرامیٹرز کو ایڈجسٹ کیا۔  
- متحرک طور پر ترتیب دیے گئے سیمپلنگ پیرامیٹرز کے ساتھ درخواست بھیجی۔  
- تیار شدہ متن کو سیمپلنگ پیرامیٹرز اور کام کی نوعیت کے ساتھ شفافیت کے لیے واپس کیا۔  
- `temperature` استعمال کیا تاکہ آؤٹ پٹ کی بے ترتیبی کو کنٹرول کیا جا سکے، جہاں زیادہ قیمتیں زیادہ تخلیقی ردعمل کی طرف لے جاتی ہیں۔  
- `top_p` استعمال کیا تاکہ ٹوکن کے انتخاب کو اعلیٰ مجموعی احتمال ماس تک محدود کیا جا سکے، جس سے تیار شدہ متن کا معیار بہتر ہوتا ہے۔  
- `frequency_penalty` استعمال کیا تاکہ تکرار کو کم اور تنوع کو بڑھایا جا سکے۔  
- `user_preferences` استعمال کیا تاکہ صارف کی تعریف کردہ تخلیقی صلاحیت اور تنوع کی سطح کی بنیاد پر سیمپلنگ پیرامیٹرز کو حسب ضرورت بنایا جا سکے۔  
- `task_type` استعمال کیا تاکہ درخواست کے لیے مناسب سیمپلنگ حکمت عملی کا تعین کیا جا سکے، جس سے کام کی نوعیت کی بنیاد پر زیادہ موزوں جوابات مل سکیں۔  
- `send_request` میتھڈ استعمال کیا تاکہ ترتیب دیے گئے سیمپلنگ پیرامیٹرز کے ساتھ پرومپٹ بھیجا جا سکے، اس بات کو یقینی بناتے ہوئے کہ ماڈل مخصوص ضروریات کے مطابق متن تیار کرے۔  
- `generated_text` استعمال کیا تاکہ ماڈل کے جواب کو حاصل کیا جا سکے، جو بعد میں سیمپلنگ پیرامیٹرز اور کام کی نوعیت کے ساتھ واپس کیا جاتا ہے تاکہ مزید تجزیہ یا نمائش کی جا سکے۔  
- `min` اور `max` فنکشنز استعمال کیے تاکہ صارف کی ترجیحات کو درست حدود میں محدود کیا جا سکے، تاکہ غلط سیمپلنگ کنفیگریشنز سے بچا جا سکے۔  

# [JavaScript Dynamic](../../../../05-AdvancedTopics/mcp-sampling)

```javascript
// JavaScript Example: Dynamic sampling configuration based on user context
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Define base sampling profiles
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Track historical performance
    this.performanceHistory = [];
  }
  
  // Detect task type from prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Simple heuristic detection - could be enhanced with ML classification
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
    
    // Default to conversational if no clear type is detected
    return 'conversational';
  }
  
  // Calculate sampling parameters based on context and user preferences
  getSamplingParameters(prompt, context = {}) {
    // Detect the type of task
    const taskType = this.detectTaskType(prompt, context);
    
    // Get base profile
    let params = {...this.samplingProfiles[taskType]};
    
    // Adjust based on user preferences
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Scale from 1-10 to appropriate temperature range
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Higher precision means lower topP (more focused selection)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Higher consistency means lower penalties
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Apply learned adjustments from performance history
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Simple adaptive logic - could be enhanced with more sophisticated algorithms
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Only consider recent history
    
    if (relevantHistory.length > 0) {
      // Calculate average performance scores
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // If performance is below threshold, adjust parameters
      if (avgScore < 0.7) {
        // Slight adjustment toward safer values
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Record performance for future adjustments
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 rating of response quality
    });
    
    // Limit history size
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Get optimized sampling parameters
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Send request with optimized parameters
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // If user provides feedback, record it for future optimization
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

// Example usage
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Creative task with custom user preferences
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // High creativity (1-10)
          consistency: 3  // Low consistency (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Code generation task
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Low creativity
          precision: 8,   // High precision
          consistency: 9  // High consistency
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

- `AdaptiveSamplingManager` کلاس بنائی جو کام کی نوعیت اور صارف کی ترجیحات کی بنیاد پر متحرک سیمپلنگ کو منظم کرتی ہے۔  
- مختلف کام کی اقسام (تخلیقی، حقائق پر مبنی، کوڈ، مکالماتی) کے لیے سیمپلنگ پروفائلز کی تعریف کی۔  
- پرومپٹ سے کام کی نوعیت کا پتہ لگانے کے لیے سادہ ہیورسٹکس کا استعمال کیا۔  
- پتہ لگائی گئی کام کی نوعیت اور صارف کی ترجیحات کی بنیاد پر سیمپلنگ پیرامیٹرز کا حساب لگایا۔  
- تاریخی کارکردگی کی بنیاد پر سیکھی گئی ایڈجسٹمنٹس کو لاگو کیا تاکہ سیمپلنگ پیرامیٹرز کو بہتر بنایا جا سکے۔  
- مستقبل کی ایڈجسٹمنٹس کے لیے کارکردگی کو ریکارڈ کیا، جس سے نظام ماضی کے تعاملات سے سیکھ سکے۔  
- متحرک طور پر ترتیب دیے گئے سیمپلنگ پیرامیٹرز کے ساتھ درخواستیں بھیجیں اور تیار شدہ متن کو لاگو پیرامیٹرز اور پتہ لگائی گئی کام کی نوعیت کے ساتھ واپس کیا۔  
- استعمال کیا:  
    - `userPreferences` تاکہ صارف کی تعریف کردہ تخلیقی صلاحیت، درستگی، اور مستقل مزاجی کی سطح کی بنیاد پر سیمپلنگ پیرامیٹرز کو حسب ضرورت بنایا جا سکے۔  
    - `detectTaskType` تاکہ پرومپٹ کی بنیاد پر کام کی نوعیت کا تعین کیا جا سکے، جس سے زیادہ موزوں جوابات مل سکیں۔  
    - `recordPerformance` تاکہ تیار شدہ جوابات کی کارکردگی کو لاگ کیا جا سکے، جس سے نظام وقت کے ساتھ بہتر ہو سکے۔  
    - `applyLearnedAdjustments` تاکہ تاریخی کارکردگی کی بنیاد پر سیمپلنگ پیرامیٹرز میں تبدیلی کی جا سکے، جس سے ماڈل کی اعلیٰ معیار کی جوابات تیار کرنے کی صلاحیت بہتر ہو۔  
    - `generateResponse` تاکہ ایڈاپٹیو سیمپلنگ کے ساتھ جواب تیار کرنے کے پورے عمل کو انکیپسولیٹ کیا جا سکے، جس سے مختلف پرومپٹس اور سیاق و سباق کے ساتھ آسانی سے کال کیا جا سکے۔  
    - `allowedTools` تاکہ ماڈل کو جنریشن کے دوران استعمال کرنے والے ٹولز کی وضاحت کی جا سکے، جس سے زیادہ سیاق و سباق سے آگاہ جوابات ممکن ہوں۔  
    - `feedbackScore

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔