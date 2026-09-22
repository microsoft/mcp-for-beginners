> [!WARNING]
> نمونه‌برداری در MCP نسخه `2026-07-28` منسوخ شده است. این درس برای
> پیاده‌سازی‌های قدیمی نگهداری شده است. سرورهای جدید باید به طور مستقیم با API ارائه‌دهنده LLM ادغام شوند.


# نمونه‌برداری در پروتکل زمینه مدل

> نمونه‌برداری در مشخصه `2026-07-28` همچنان برای سازگاری باقی مانده و
> ممکن است در اولین بازنگری که در یا پس از 28 ژوئیه 2027 منتشر می‌شود حذف شود.
> مثال‌های این درس ممکن است از APIهای SDK استفاده کنند که `2025-11-25` را پیاده‌سازی می‌کنند.
> برای اطلاعات بیشتر به [تغییرات در MCP: مشخصه 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md) مراجعه کنید.

در پیاده‌سازی‌های قدیمی MCP، نمونه‌برداری به سرورها اجازه می‌دهد تا از طریق کلاینت درخواست تکمیل‌های LLM کنند.
این درس جریان پروتکل منسوخ شده را برای سازگاری و کار مهاجرت توضیح می‌دهد.


## معرفی

در این درس، به بررسی نحوه تنظیم پارامترهای نمونه‌برداری در درخواست‌های MCP و درک مکانیک‌های پایه پروتکل نمونه‌برداری خواهیم پرداخت.

## اهداف یادگیری

تا پایان این درس، شما قادر خواهید بود:

- پارامترهای کلیدی نمونه‌برداری در MCP را درک کنید.
- پارامترهای نمونه‌برداری را برای موارد استفاده مختلف پیکربندی کنید.
- نمونه‌برداری تعیین‌شده برای نتایج قابل تکرار پیاده‌سازی کنید.
- پارامترهای نمونه‌برداری را بر اساس زمینه و ترجیحات کاربر به صورت داینامیک تنظیم کنید.
- استراتژی‌های نمونه‌برداری را برای بهبود عملکرد مدل در سناریوهای گوناگون اعمال کنید.
- نحوه کار نمونه‌برداری در جریان کلاینت-سرور MCP را درک کنید.

## چگونه نمونه‌برداری در MCP کار می‌کند

جریان نمونه‌برداری در MCP گام‌های زیر را دنبال می‌کند:

1. سرور یک درخواست `sampling/createMessage` به کلاینت ارسال می‌کند
2. کلاینت درخواست را بررسی و در صورت نیاز اصلاح می‌کند
3. کلاینت از LLM نمونه‌برداری می‌کند
4. کلاینت تکمیل را بررسی می‌کند
5. کلاینت نتیجه را به سرور بازمی‌گرداند

این طراحی با حضور انسان تضمین می‌کند که کاربران کنترل آنچه مدل می‌بیند و تولید می‌کند را حفظ کنند.

## نمای کلی پارامترهای نمونه‌برداری

MCP پارامترهای نمونه‌برداری زیر را تعریف می‌کند که می‌توان در درخواست‌های کلاینت تنظیم کرد:

| پارامتر | توضیحات | بازه معمول |
|-----------|-------------|---------------|
| `temperature` | کنترل تصادفی بودن در انتخاب توکن‌ها | ۰.۰ - ۱.۰ |
| `maxTokens` | حداکثر تعداد توکن برای تولید | مقدار عدد صحیح |
| `stopSequences` | دنباله‌های سفارشی که هنگام مواجهه، تولید را متوقف می‌کنند | آرایه‌ای از رشته‌ها |
| `metadata` | پارامترهای اضافی مخصوص ارائه‌دهنده | شیء JSON |

بسیاری از ارائه‌دهندگان LLM پارامترهای اضافی از طریق فیلد `metadata` پشتیبانی می‌کنند که ممکن است شامل موارد زیر باشد:

| پارامتر افزونه رایج | توضیحات | بازه معمول |
|-----------|-------------|---------------|
| `top_p` | نمونه‌برداری هسته‌ای - توکن‌ها را به احتمال تجمعی برتر محدود می‌کند | ۰.۰ - ۱.۰ |
| `top_k` | انتخاب توکن‌ها را به گزینه‌های برتر K محدود می‌کند | ۱ - ۱۰۰ |
| `presence_penalty` | توکن‌ها را بر اساس حضورشان در متن تا کنون جریمه می‌کند | -۲.۰ - ۲.۰ |
| `frequency_penalty` | توکن‌ها را بر اساس تکرارش در متن تا کنون جریمه می‌کند | -۲.۰ - ۲.۰ |
| `seed` | بذر تصادفی خاص برای نتایج قابل تکرار | مقدار عدد صحیح |

## قالب نمونه درخواست

در اینجا نمونه‌ای از درخواست نمونه‌برداری از کلاینت در MCP آمده است:

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

## قالب پاسخ

کلاینت نتیجه تکمیل را بازمی‌گرداند:

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

## کنترل‌های حضور انسان در فرآیند

نمونه‌برداری MCP با نظارت انسانی طراحی شده است:

- **برای پرامپت‌ها**:
  - کلاینت‌ها باید پرامپت پیشنهادی را به کاربران نشان دهند
  - کاربران باید بتوانند پرامپت‌ها را اصلاح یا رد کنند
  - پرامپت‌های سیستم می‌توانند فیلتر یا اصلاح شوند
  - درج زمینه توسط کلاینت کنترل می‌شود

- **برای تکمیل‌ها**:
  - کلاینت‌ها باید تکمیل را به کاربران نشان دهند
  - کاربران باید بتوانند تکمیل‌ها را اصلاح یا رد کنند
  - کلاینت‌ها می‌توانند تکمیل‌ها را فیلتر یا اصلاح کنند
  - کاربران کنترل می‌کنند که کدام مدل استفاده شود

با در نظر گرفتن این اصول، بیایید ببینیم چگونه نمونه‌برداری را در زبان‌های برنامه‌نویسی مختلف پیاده‌سازی کنیم، با تمرکز بر پارامترهایی که در میان ارائه‌دهندگان LLM معمولاً پشتیبانی می‌شوند.

## ملاحظات امنیتی

هنگام پیاده‌سازی نمونه‌برداری در MCP، نکات برتر امنیتی زیر را در نظر بگیرید:

- **تمام محتوای پیام را اعتبارسنجی کنید** قبل از ارسال به کلاینت
- **اطلاعات حساس را از پرامپت‌ها و تکمیل‌ها پاک‌سازی کنید**
- **محدودیت نرخ را برای جلوگیری از سوءاستفاده اعمال کنید**
- **کاربرد نمونه‌برداری را برای الگوهای غیرمعمول نظارت کنید**
- **داده‌ها را در انتقال با پروتکل‌های امن رمزگذاری کنید**
- **حریم خصوصی داده‌های کاربر را مطابق مقررات مربوطه مدیریت کنید**
- **درخواست‌های نمونه‌برداری را برای انطباق و امنیت حسابرسی کنید**
- **کنترل هزینه با محدودیت‌های مناسب**
- **برای درخواست‌های نمونه‌برداری محدودیت زمانی تعیین کنید**
- **خطاهای مدل را با راه‌حل‌های جایگزین مناسب به طور نرم مدیریت کنید**

پارامترهای نمونه‌برداری اجازه می‌دهند رفتار مدل‌های زبانی را به دقت تنظیم کنید تا تعادل مطلوب بین خروجی‌های تعیین‌شده و خلاقانه برقرار شود.

بیایید ببینیم چگونه این پارامترها را در زبان‌های برنامه‌نویسی مختلف پیکربندی کنیم.

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

در کد قبلی ما:

- یک کلاینت MCP با URL سرور مشخص ایجاد کردیم.
- یک درخواست با پارامترهای نمونه‌برداری مانند `temperature`، `top_p`، و `top_k` پیکربندی کردیم.
- درخواست را ارسال کردیم و متن تولید شده را چاپ کردیم.
- از موارد زیر استفاده کردیم:
    - `allowedTools` برای مشخص کردن ابزارهایی که مدل می‌تواند در هنگام تولید استفاده کند. در این حالت، ابزارهای `ideaGenerator` و `marketAnalyzer` برای کمک به تولید ایده‌های خلاقانه اپلیکیشن مجاز شدند.
    - `frequencyPenalty` و `presencePenalty` برای کنترل تکرار و تنوع در خروجی.
    - `temperature` برای کنترل تصادفی بودن خروجی، که مقادیر بالاتر منجر به پاسخ‌های خلاقانه‌تر می‌شود.
    - `top_p` برای محدود کردن انتخاب توکن‌ها به آن‌هایی که به جرم احتمالی تجمعی برتر کمک می‌کنند و کیفیت متن تولید شده را افزایش می‌دهد.
    - `top_k` برای محدود کردن مدل به توکن‌های محتمل‌ترین K، که می‌تواند به تولید پاسخ‌های منسجم‌تر کمک کند.
    - `frequencyPenalty` و `presencePenalty` برای کاهش تکرار و تشویق تنوع در متن تولید شده.

# [JavaScript](#tab/javascript)

```javascript
// مثال جاوااسکریپت: پیکربندی دمایی و نمونه‌برداری Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // مقداردهی اولیه کلاینت MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // پیکربندی درخواست با پارامترهای نمونه‌برداری مختلف
  const creativeSampling = {
    temperature: 0.9,    // دمای بالاتر = تصادفی‌تر/خلاقانه‌تر
    topP: 0.92,          // در نظر گرفتن توکن‌ها با جرم احتمال ۹۲٪ برتر
    frequencyPenalty: 0.6, // کاهش تکرار توالی‌های توکن
    presencePenalty: 0.4   // جریمه کردن توکن‌هایی که تاکنون در متن ظاهر شده‌اند
  };
  
  const factualSampling = {
    temperature: 0.2,    // دمای پایین‌تر = تصمیم‌گیری قطعی‌تر/واقعی‌تر
    topP: 0.85,          // انتخاب توکن کمی متمرکزتر
    frequencyPenalty: 0.2, // جریمه تکرار حداقلی
    presencePenalty: 0.1   // جریمه حضور حداقلی
  };
  
  try {
    // ارسال دو درخواست با پیکربندی نمونه‌برداری متفاوت
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

در کد قبلی ما:

- یک کلاینت MCP با URL سرور و کلید API مقداردهی اولیه کردیم.
- دو مجموعه پارامتر نمونه‌برداری پیکربندی کردیم: یکی برای کارهای خلاقانه و دیگری برای کارهای حقیقی.
- درخواست‌هایی با این تنظیمات ارسال کردیم و اجازه دادیم مدل برای هر کار از ابزارهای خاصی استفاده کند.
- پاسخ‌های تولید شده را چاپ کردیم تا اثر پارامترهای مختلف نمونه‌برداری را نشان دهیم.
- از `allowedTools` برای مشخص کردن ابزارهایی که مدل در هنگام تولید می‌تواند استفاده کند بهره بردیم. در این حالت، ابزارهای `ideaGenerator` و `environmentalImpactTool` برای کارهای خلاقانه و `factChecker` و `dataAnalysisTool` برای کارهای حقیقی مجاز بودند.
- از `temperature` برای کنترل تصادفی بودن خروجی، که مقادیر بالاتر منجر به پاسخ‌های خلاقانه‌تر می‌شود، استفاده کردیم.

- از `top_p` برای محدود کردن انتخاب توکن‌ها به آن‌هایی استفاده کردیم که به بیشترین جرم احتمال تجمعی کمک می‌کنند، که کیفیت متن تولید شده را افزایش می‌دهد.
- از `frequencyPenalty` و `presencePenalty` برای کاهش تکرار و تشویق به تنوع در خروجی استفاده کردیم.
- از `top_k` برای محدود کردن مدل به K توکن محتمل‌ترین استفاده کردیم، که می‌تواند در تولید پاسخ‌های منسجم‌تر کمک کند.

---

## نمونه‌گیری تعیین‌شده

برای برنامه‌هایی که خروجی‌های سازگار نیاز دارند، نمونه‌گیری تعیین‌شده نتایج قابل تکرار را تضمین می‌کند. این کار با استفاده از دانه تصادفی ثابت و تنظیم دما روی صفر انجام می‌شود.

بیایید به اجرای نمونه زیر نگاهی بیندازیم تا نمونه‌گیری تعیین‌شده را در زبان‌های برنامه‌نویسی مختلف نشان دهیم.

# [Java](#tab/java)

```java
// نمونه جاوا: پاسخ‌های قطعی با بذر ثابت
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // استفاده از بذر ثابت برای نتایج قطعی
        
        // اولین درخواست با بذر ثابت
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // دمای صفر برای حداکثر قطعیت
            .build();
            
        // دومین درخواست با همان بذر
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // اجرای هر دو درخواست
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // پاسخ‌ها باید به دلیل بذر و دمای برابر صفر یکسان باشند
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

در کد قبلی ما:

- یک کلاینت MCP با URL سرور مشخص ایجاد کردیم.
- دو درخواست با پرامپت یکسان، دانه ثابت، و دمای صفر پیکربندی کردیم.
- هر دو درخواست را ارسال کردیم و متن تولید شده را چاپ کردیم.
- نشان دادیم که پاسخ‌ها به دلیل ماهیت تعیین‌شده پیکربندی نمونه‌گیری (همان دانه و دما) یکسان هستند.
- از `setSeed` برای مشخص کردن دانه تصادفی ثابت استفاده کردیم، که اطمینان می‌دهد مدل هر بار برای ورودی یکسان خروجی یکسانی تولید می‌کند.
- `temperature` را روی صفر تنظیم کردیم تا حداکثر تعیین‌شدگی تضمین شود، یعنی مدل همیشه محتمل‌ترین توکن بعدی را بدون تصادفی بودن انتخاب می‌کند.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// نمونه جاوااسکریپت: پاسخ‌های تعیین‌شده با کنترل بذر
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // درخواست اول با بذر ثابت
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // دمای صفر برای حداکثر قطعیت
    });
    
    // درخواست دوم با همان بذر و دما
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // درخواست سوم با بذر متفاوت اما همان دما
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

در کد قبلی ما:

- یک کلاینت MCP با URL سرور راه‌اندازی کردیم.
- دو درخواست با پرامپت یکسان، دانه ثابت، و دمای صفر پیکربندی کردیم.
- هر دو درخواست را ارسال کردیم و متن تولید شده را چاپ کردیم.
- نشان دادیم که پاسخ‌ها به دلیل ماهیت تعیین‌شده پیکربندی نمونه‌گیری (همان دانه و دما) یکسان هستند.
- از `seed` برای تعیین دانه تصادفی ثابت استفاده کردیم، که تضمین می‌کند مدل هر بار برای ورودی یکسان خروجی یکسان تولید کند.
- `temperature` را روی صفر تنظیم کردیم تا حداکثر تعیین‌شدگی وجود داشته باشد، یعنی مدل همیشه محتمل‌ترین توکن ممکن را انتخاب می‌کند بدون تصادفی بودن.
- برای درخواست سوم از دانه متفاوتی استفاده کردیم تا نشان دهیم تغییر دانه منجر به خروجی‌های متفاوت می‌شود، حتی با همان پرامپت و دما.

---

## پیکربندی نمونه‌گیری پویا

نمونه‌گیری هوشمند پارامترها را بر اساس زمینه و نیازهای هر درخواست تطبیق می‌دهد. یعنی پارامترهایی مانند دما، top_p، و جریمه‌ها به صورت پویا بر اساس نوع وظیفه، ترجیحات کاربر یا عملکرد تاریخی تنظیم می‌شوند.

بیایید ببینیم چگونه می‌توان نمونه‌گیری پویا را در زبان‌های برنامه‌نویسی مختلف پیاده‌سازی کرد.

# [Python](#tab/python)

```python
# نمونه پایتون: نمونه‌گیری پویا بر اساس زمینه درخواست
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # تعریف پیش‌تنظیم‌های نمونه‌گیری برای انواع وظایف مختلف
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # انتخاب پیش‌تنظیم پایه
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # تنظیم بر اساس ترجیحات کاربر در صورت ارائه
        if user_preferences:
            if "creativity_level" in user_preferences:
                # مقیاس‌بندی دما بر اساس ترجیح خلاقیت (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # تنظیم top_p بر اساس تنوع پاسخ مورد نظر
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # ایجاد و ارسال درخواست با پارامترهای نمونه‌گیری سفارشی
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # بازگرداندن پاسخ با متادیتای نمونه‌گیری برای شفافیت
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

در کد قبلی ما:

- کلاس `DynamicSamplingService` ایجاد کردیم که نمونه‌گیری تطبیقی را مدیریت می‌کند.
- تنظیمات نمونه‌گیری پیش‌فرض برای انواع مختلف وظایف تعریف کردیم (خلاقانه، واقعی، کد، تحلیلی).
- یک پیش‌تنظیم نمونه‌گیری پایه بر اساس نوع وظیفه انتخاب کردیم.
- پارامترهای نمونه‌گیری را بر اساس ترجیحات کاربر، مانند سطح خلاقیت و تنوع، تنظیم کردیم.
- درخواست را با پارامترهای نمونه‌گیری پیکربندی‌شده به طور پویا ارسال کردیم.
- متن تولید شده همراه با پارامترهای نمونه‌گیری اعمال شده و نوع وظیفه را برای شفافیت برگرداندیم.
- از `temperature` برای کنترل تصادفی بودن خروجی استفاده کردیم که مقادیر بالاتر به پاسخ‌های خلاقانه‌تر منجر می‌شوند.
- از `top_p` برای محدود کردن انتخاب توکن‌ها به آن‌هایی استفاده کردیم که به بیشترین جرم احتمال تجمعی کمک می‌کنند، که کیفیت متن تولید شده را افزایش می‌دهد.
- از `frequency_penalty` برای کاهش تکرار و تشویق به تنوع در خروجی استفاده کردیم.
- از `user_preferences` برای اجازه دادن به سفارشی‌سازی پارامترهای نمونه‌گیری بر اساس سطوح خلاقیت و تنوع تعریف‌شده توسط کاربر استفاده کردیم.
- از `task_type` برای تعیین استراتژی نمونه‌گیری مناسب برای درخواست استفاده کردیم، که امکان پاسخ‌های بیشتر متناسب با ماهیت وظیفه را فراهم می‌کند.
- از متد `send_request` برای ارسال پرامپت با پارامترهای نمونه‌گیری پیکربندی‌شده استفاده کردیم، که تضمین می‌کند مدل متن را طبق نیازهای مشخص شده تولید کند.
- از `generated_text` برای بازیابی پاسخ مدل استفاده کردیم، که سپس همراه با پارامترهای نمونه‌گیری و نوع وظیفه برای تحلیل یا نمایش بیشتر برگردانده می‌شود.
- از توابع `min` و `max` استفاده کردیم تا اطمینان حاصل شود که ترجیحات کاربر در محدوده‌های معتبر محدود شده‌اند، که از پیکربندی‌های نامعتبر نمونه‌گیری جلوگیری می‌کند.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// مثال جاوااسکریپت: پیکربندی نمونه‌برداری پویا بر اساس زمینه کاربر
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // تعریف پروفایل‌های پایه نمونه‌برداری
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // پیگیری عملکرد گذشته
    this.performanceHistory = [];
  }
  
  // شناسایی نوع وظیفه از پرامپت
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // تشخیص ساده مبتنی بر قواعد - قابل بهبود با طبقه‌بندی یادگیری ماشین
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
    
    // پیش‌فرض مکالمه اگر نوع مشخصی شناسایی نشود
    return 'conversational';
  }
  
  // محاسبه پارامترهای نمونه‌برداری بر اساس زمینه و ترجیحات کاربر
  getSamplingParameters(prompt, context = {}) {
    // شناسایی نوع وظیفه
    const taskType = this.detectTaskType(prompt, context);
    
    // دریافت پروفایل پایه
    let params = {...this.samplingProfiles[taskType]};
    
    // تنظیم بر اساس ترجیحات کاربر
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // مقیاس‌بندی از 1 تا 10 به محدوده دمای مناسب
        params.temperature = 0.1 + (creativity * 0.09); // ۰.۱-۱.۰
      }
      
      if (precision !== undefined) {
        // دقت بالاتر به معنی topP پایین‌تر (انتخاب متمرکزتر)
        params.topP = 1.0 - (precision * 0.05); // ۰.۵-۱.۰
      }
      
      if (consistency !== undefined) {
        // سازگاری بالاتر به معنای جریمه‌های کمتر
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // ۰.۱-۰.۹
      }
    }
    
    // اعمال تنظیمات یادگرفته شده از تاریخچه عملکرد
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // منطق سازگار ساده - قابل بهبود با الگوریتم‌های پیشرفته‌تر
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // فقط تاریخچه اخیر را در نظر بگیرید
    
    if (relevantHistory.length > 0) {
      // محاسبه میانگین امتیازات عملکرد
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // اگر عملکرد زیر آستانه باشد، پارامترها را تنظیم کن
      if (avgScore < 0.7) {
        // تنظیم جزئی به سمت مقادیر امن‌تر
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // ثبت عملکرد برای تنظیمات آینده
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // امتیاز ۰ تا ۱ کیفیت پاسخ
    });
    
    // محدود کردن اندازه تاریخچه
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // دریافت پارامترهای نمونه‌برداری بهینه شده
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // ارسال درخواست با پارامترهای بهینه‌شده
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // اگر کاربر بازخورد دهد، آن را برای بهینه‌سازی آینده ثبت کن
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

// استفاده نمونه
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // وظیفه خلاقانه با ترجیحات سفارشی کاربر
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // خلاقیت بالا (۱-۱۰)
          consistency: 3  // سازگاری پایین (۱-۱۰)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // وظیفه تولید کد
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // خلاقیت پایین
          precision: 8,   // دقت بالا
          consistency: 9  // سازگاری بالا
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

در کد قبلی ما:

- کلاس `AdaptiveSamplingManager` ایجاد کردیم که نمونه‌گیری پویا را بر اساس نوع وظیفه و ترجیحات کاربر مدیریت می‌کند.
- پروفایل‌های نمونه‌گیری برای انواع مختلف وظایف تعریف کردیم (خلاقانه، واقعی، کد، مکالمه‌ای).
- متدی برای تشخیص نوع وظیفه از روی پرامپت با استفاده از هیوریستیک‌های ساده پیاده‌سازی کردیم.
- پارامترهای نمونه‌گیری را بر اساس نوع وظیفه شناسایی‌شده و ترجیحات کاربر محاسبه کردیم.
- تنظیمات آموخته شده بر اساس عملکرد تاریخی را برای بهینه‌سازی پارامترهای نمونه‌گیری اعمال کردیم.
- عملکرد را برای تنظیمات آینده ثبت کردیم، که به سیستم اجازه می‌دهد از تعاملات گذشته بیاموزد.
- درخواست‌ها را با پارامترهای نمونه‌گیری پیکربندی‌شده به طور پویا ارسال کردیم و متن تولید شده را همراه با پارامترهای اعمال شده و نوع وظیفه شناسایی‌شده برگرداندیم.
- از موارد زیر استفاده کردیم:
    - `userPreferences` برای اجازه دادن به سفارشی‌سازی پارامترهای نمونه‌گیری بر اساس سطوح تعریف‌شده توسط کاربر در خلاقیت، دقت و ثبات.
    - `detectTaskType` برای تعیین ماهیت وظیفه بر اساس پرامپت، که اجازه می‌دهد پاسخ‌ها بیشتر متناسب شوند.
    - `recordPerformance` برای ثبت عملکرد پاسخ‌های تولید شده، که سیستم را قادر می‌سازد تا به مرور خود را تطبیق و بهبود دهد.
    - `applyLearnedAdjustments` برای تغییر پارامترهای نمونه‌گیری بر اساس عملکرد تاریخی، که توانایی مدل در تولید پاسخ‌های با کیفیت بالا را افزایش می‌دهد.
    - `generateResponse` برای بسته‌بندی کل فرآیند تولید پاسخ با نمونه‌گیری تطبیقی، که فراخوانی آن با پرامپت‌ها و زمینه‌های مختلف آسان است.
    - `allowedTools` برای مشخص کردن اینکه مدل در طول تولید می‌تواند از کدام ابزارها استفاده کند، که پاسخ‌ها را با زمینه بیشتر آگاه می‌سازد.
    - `feedbackScore` برای اجازه دادن به کاربران جهت ارائه بازخورد درباره کیفیت پاسخ تولید شده، که می‌تواند برای بهبود عملکرد مدل در طول زمان استفاده شود.
    - `performanceHistory` برای نگهداری سوابق تعاملات گذشته، که سیستم را قادر می‌سازد از موفقیت‌ها و شکست‌های قبلی بیاموزد.
    - `getSamplingParameters` برای تنظیم پویا پارامترهای نمونه‌گیری بر اساس زمینه درخواست، که رفتار مدل را انعطاف‌پذیرتر و پاسخگوتر می‌کند.
    - `detectTaskType` برای طبقه‌بندی وظیفه بر اساس پرامپت، که سیستم را قادر می‌سازد استراتژی‌های نمونه‌گیری مناسب را برای انواع مختلف درخواست‌ها اعمال کند.
    - `samplingProfiles` برای تعریف پیکربندی‌های پایه نمونه‌گیری برای انواع مختلف وظایف، که تنظیمات سریع بر اساس ماهیت درخواست را ممکن می‌سازد.

---

## گام بعدی چیست

- [5.7 مقیاس‌بندی](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->