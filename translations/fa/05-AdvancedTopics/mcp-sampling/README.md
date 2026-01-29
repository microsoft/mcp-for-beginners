# نمونه‌گیری در پروتکل مدل کانتکست

نمونه‌گیری یکی از قابلیت‌های قدرتمند MCP است که به سرورها اجازه می‌دهد از طریق کلاینت درخواست تکمیل‌های LLM را ارسال کنند و رفتارهای پیچیده و عامل‌محور را در عین حفظ امنیت و حریم خصوصی ممکن سازد. پیکربندی درست نمونه‌گیری می‌تواند کیفیت و عملکرد پاسخ‌ها را به طور چشمگیری بهبود بخشد. MCP روشی استاندارد برای کنترل نحوه تولید متن توسط مدل‌ها با پارامترهای خاصی ارائه می‌دهد که بر تصادفی بودن، خلاقیت و انسجام تأثیر می‌گذارند.

## مقدمه

در این درس، نحوه پیکربندی پارامترهای نمونه‌گیری در درخواست‌های MCP را بررسی کرده و مکانیزم‌های پروتکل نمونه‌گیری را درک خواهیم کرد.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- پارامترهای کلیدی نمونه‌گیری موجود در MCP را بشناسید.
- پارامترهای نمونه‌گیری را برای کاربردهای مختلف پیکربندی کنید.
- نمونه‌گیری قطعی برای نتایج قابل تکرار پیاده‌سازی کنید.
- پارامترهای نمونه‌گیری را به صورت پویا بر اساس کانتکست و ترجیحات کاربر تنظیم کنید.
- استراتژی‌های نمونه‌گیری را برای بهبود عملکرد مدل در سناریوهای مختلف به کار ببرید.
- نحوه عملکرد نمونه‌گیری در جریان کلاینت-سرور MCP را درک کنید.

## نحوه عملکرد نمونه‌گیری در MCP

روند نمونه‌گیری در MCP به این صورت است:

1. سرور درخواست `sampling/createMessage` را به کلاینت ارسال می‌کند  
2. کلاینت درخواست را بررسی کرده و می‌تواند آن را تغییر دهد  
3. کلاینت از LLM نمونه‌گیری می‌کند  
4. کلاینت تکمیل را بازبینی می‌کند  
5. کلاینت نتیجه را به سرور بازمی‌گرداند  

این طراحی با حضور انسان در حلقه، اطمینان می‌دهد که کاربران کنترل آنچه مدل می‌بیند و تولید می‌کند را حفظ می‌کنند.

## مرور پارامترهای نمونه‌گیری

MCP پارامترهای نمونه‌گیری زیر را تعریف می‌کند که می‌توان در درخواست‌های کلاینت تنظیم کرد:

| پارامتر | توضیح | بازه معمول |
|---------|--------|-------------|
| `temperature` | کنترل میزان تصادفی بودن در انتخاب توکن‌ها | 0.0 - 1.0 |
| `maxTokens` | حداکثر تعداد توکن‌های تولید شده | مقدار عدد صحیح |
| `stopSequences` | دنباله‌های سفارشی که هنگام مواجهه تولید را متوقف می‌کنند | آرایه‌ای از رشته‌ها |
| `metadata` | پارامترهای اضافی خاص ارائه‌دهنده | شیء JSON |

بسیاری از ارائه‌دهندگان LLM پارامترهای اضافی را از طریق فیلد `metadata` پشتیبانی می‌کنند که ممکن است شامل موارد زیر باشد:

| پارامتر توسعه رایج | توضیح | بازه معمول |
|--------------------|--------|-------------|
| `top_p` | نمونه‌گیری هسته‌ای - محدود کردن توکن‌ها به بالاترین احتمال تجمعی | 0.0 - 1.0 |
| `top_k` | محدود کردن انتخاب توکن‌ها به K گزینه برتر | 1 - 100 |
| `presence_penalty` | جریمه توکن‌ها بر اساس حضورشان در متن تا کنون | -2.0 - 2.0 |
| `frequency_penalty` | جریمه توکن‌ها بر اساس تکرارشان در متن تا کنون | -2.0 - 2.0 |
| `seed` | بذر تصادفی مشخص برای نتایج قابل تکرار | مقدار عدد صحیح |

## قالب نمونه درخواست

در اینجا نمونه‌ای از درخواست نمونه‌گیری از کلاینت در MCP آمده است:

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

## کنترل‌های حضور انسان در حلقه

نمونه‌گیری MCP با نظارت انسانی طراحی شده است:

- **برای پرامپت‌ها**:  
  - کلاینت‌ها باید پرامپت پیشنهادی را به کاربران نشان دهند  
  - کاربران باید بتوانند پرامپت‌ها را تغییر داده یا رد کنند  
  - پرامپت‌های سیستمی می‌توانند فیلتر یا تغییر داده شوند  
  - گنجاندن کانتکست توسط کلاینت کنترل می‌شود  

- **برای تکمیل‌ها**:  
  - کلاینت‌ها باید تکمیل را به کاربران نشان دهند  
  - کاربران باید بتوانند تکمیل‌ها را تغییر داده یا رد کنند  
  - کلاینت‌ها می‌توانند تکمیل‌ها را فیلتر یا تغییر دهند  
  - کاربران کنترل انتخاب مدل را دارند  

با در نظر گرفتن این اصول، بیایید ببینیم چگونه نمونه‌گیری را در زبان‌های برنامه‌نویسی مختلف پیاده‌سازی کنیم، با تمرکز بر پارامترهایی که معمولاً توسط ارائه‌دهندگان LLM پشتیبانی می‌شوند.

## ملاحظات امنیتی

هنگام پیاده‌سازی نمونه‌گیری در MCP، این بهترین شیوه‌های امنیتی را در نظر بگیرید:

- **اعتبارسنجی تمام محتوای پیام** قبل از ارسال به کلاینت  
- **پاک‌سازی اطلاعات حساس** از پرامپت‌ها و تکمیل‌ها  
- **اجرای محدودیت نرخ** برای جلوگیری از سوءاستفاده  
- **نظارت بر استفاده نمونه‌گیری** برای الگوهای غیرمعمول  
- **رمزنگاری داده‌ها در انتقال** با استفاده از پروتکل‌های امن  
- **رعایت حریم خصوصی داده‌های کاربر** مطابق با مقررات مربوطه  
- **ممیزی درخواست‌های نمونه‌گیری** برای انطباق و امنیت  
- **کنترل هزینه‌ها** با محدودیت‌های مناسب  
- **اجرای تایم‌اوت برای درخواست‌های نمونه‌گیری**  
- **مدیریت خطاهای مدل به صورت مناسب** با راهکارهای جایگزین  

پارامترهای نمونه‌گیری امکان تنظیم دقیق رفتار مدل‌های زبانی را فراهم می‌کنند تا تعادل مطلوب بین خروجی‌های قطعی و خلاقانه برقرار شود.

بیایید ببینیم چگونه این پارامترها را در زبان‌های برنامه‌نویسی مختلف پیکربندی کنیم.

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

در کد بالا ما:

- یک کلاینت MCP با URL سرور مشخص ایجاد کردیم.  
- درخواست را با پارامترهای نمونه‌گیری مانند `temperature`، `top_p` و `top_k` پیکربندی کردیم.  
- درخواست را ارسال کرده و متن تولید شده را چاپ کردیم.  
- از:  
    - `allowedTools` برای مشخص کردن ابزارهایی که مدل می‌تواند در طول تولید استفاده کند بهره بردیم. در این مورد، ابزارهای `ideaGenerator` و `marketAnalyzer` برای کمک به تولید ایده‌های خلاقانه اپلیکیشن مجاز شدند.  
    - `frequencyPenalty` و `presencePenalty` برای کنترل تکرار و تنوع در خروجی استفاده کردیم.  
    - `temperature` برای کنترل تصادفی بودن خروجی، که مقادیر بالاتر پاسخ‌های خلاقانه‌تری ایجاد می‌کند.  
    - `top_p` برای محدود کردن انتخاب توکن‌ها به آن‌هایی که به بالاترین احتمال تجمعی کمک می‌کنند، به منظور بهبود کیفیت متن تولید شده.  
    - `top_k` برای محدود کردن مدل به K توکن محتمل‌ترین، که می‌تواند به تولید پاسخ‌های منسجم‌تر کمک کند.  
    - `frequencyPenalty` و `presencePenalty` برای کاهش تکرار و تشویق تنوع در متن تولید شده استفاده کردیم.

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

در کد بالا ما:

- یک کلاینت MCP با URL سرور و کلید API مقداردهی اولیه کردیم.  
- دو مجموعه پارامتر نمونه‌گیری پیکربندی کردیم: یکی برای وظایف خلاقانه و دیگری برای وظایف واقعی.  
- درخواست‌ها را با این پیکربندی‌ها ارسال کردیم و اجازه دادیم مدل برای هر وظیفه از ابزارهای خاصی استفاده کند.  
- پاسخ‌های تولید شده را چاپ کردیم تا تأثیر پارامترهای مختلف نمونه‌گیری را نشان دهیم.  
- از `allowedTools` برای مشخص کردن ابزارهایی که مدل می‌تواند در طول تولید استفاده کند بهره بردیم. در این مورد، برای وظایف خلاقانه ابزارهای `ideaGenerator` و `environmentalImpactTool` و برای وظایف واقعی ابزارهای `factChecker` و `dataAnalysisTool` مجاز شدند.  
- از `temperature` برای کنترل تصادفی بودن خروجی استفاده کردیم، که مقادیر بالاتر پاسخ‌های خلاقانه‌تری ایجاد می‌کند.  
- از `top_p` برای محدود کردن انتخاب توکن‌ها به آن‌هایی که به بالاترین احتمال تجمعی کمک می‌کنند، به منظور بهبود کیفیت متن تولید شده استفاده کردیم.  
- از `frequencyPenalty` و `presencePenalty` برای کاهش تکرار و تشویق تنوع در خروجی بهره بردیم.  
- از `top_k` برای محدود کردن مدل به K توکن محتمل‌ترین، که می‌تواند به تولید پاسخ‌های منسجم‌تر کمک کند استفاده کردیم.

---

## نمونه‌گیری قطعی

برای برنامه‌هایی که نیاز به خروجی‌های ثابت دارند، نمونه‌گیری قطعی نتایج قابل تکرار را تضمین می‌کند. این کار با استفاده از بذر تصادفی ثابت و تنظیم دما روی صفر انجام می‌شود.

بیایید نمونه پیاده‌سازی زیر را برای نشان دادن نمونه‌گیری قطعی در زبان‌های برنامه‌نویسی مختلف ببینیم.

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

در کد بالا ما:

- یک کلاینت MCP با URL سرور مشخص ایجاد کردیم.  
- دو درخواست با همان پرامپت، بذر ثابت و دمای صفر پیکربندی کردیم.  
- هر دو درخواست را ارسال کرده و متن تولید شده را چاپ کردیم.  
- نشان دادیم که پاسخ‌ها به دلیل ماهیت قطعی پیکربندی نمونه‌گیری (بذر و دمای یکسان) یکسان هستند.  
- از `setSeed` برای تعیین بذر تصادفی ثابت استفاده کردیم تا مدل هر بار برای ورودی یکسان خروجی یکسان تولید کند.  
- `temperature` را روی صفر تنظیم کردیم تا حداکثر قطعی بودن حاصل شود، یعنی مدل همیشه محتمل‌ترین توکن بعدی را بدون تصادفی بودن انتخاب کند.

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

در کد بالا ما:

- یک کلاینت MCP با URL سرور مقداردهی اولیه کردیم.  
- دو درخواست با همان پرامپت، بذر ثابت و دمای صفر پیکربندی کردیم.  
- هر دو درخواست را ارسال کرده و متن تولید شده را چاپ کردیم.  
- نشان دادیم که پاسخ‌ها به دلیل ماهیت قطعی پیکربندی نمونه‌گیری (بذر و دمای یکسان) یکسان هستند.  
- از `seed` برای تعیین بذر تصادفی ثابت استفاده کردیم تا مدل هر بار برای ورودی یکسان خروجی یکسان تولید کند.  
- `temperature` را روی صفر تنظیم کردیم تا حداکثر قطعی بودن حاصل شود، یعنی مدل همیشه محتمل‌ترین توکن بعدی را بدون تصادفی بودن انتخاب کند.  
- برای درخواست سوم از بذر متفاوتی استفاده کردیم تا نشان دهیم تغییر بذر منجر به خروجی‌های متفاوت می‌شود، حتی با پرامپت و دمای یکسان.

---

## پیکربندی پویا نمونه‌گیری

نمونه‌گیری هوشمند پارامترها را بر اساس کانتکست و نیازهای هر درخواست تنظیم می‌کند. این یعنی تنظیم پویا پارامترهایی مانند temperature، top_p و جریمه‌ها بر اساس نوع وظیفه، ترجیحات کاربر یا عملکرد تاریخی.

بیایید ببینیم چگونه نمونه‌گیری پویا را در زبان‌های برنامه‌نویسی مختلف پیاده‌سازی کنیم.

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

در کد بالا ما:

- کلاسی به نام `DynamicSamplingService` ایجاد کردیم که مدیریت نمونه‌گیری تطبیقی را بر عهده دارد.  
- پیش‌تنظیم‌های نمونه‌گیری برای انواع مختلف وظایف (خلاقانه، واقعی، کد، تحلیلی) تعریف کردیم.  
- پیش‌تنظیم پایه نمونه‌گیری را بر اساس نوع وظیفه انتخاب کردیم.  
- پارامترهای نمونه‌گیری را بر اساس ترجیحات کاربر مانند سطح خلاقیت و تنوع تنظیم کردیم.  
- درخواست را با پارامترهای نمونه‌گیری پیکربندی شده به صورت پویا ارسال کردیم.  
- متن تولید شده را همراه با پارامترهای نمونه‌گیری اعمال شده و نوع وظیفه برای شفافیت بازگرداندیم.  
- از `temperature` برای کنترل تصادفی بودن خروجی استفاده کردیم، که مقادیر بالاتر پاسخ‌های خلاقانه‌تری ایجاد می‌کند.  
- از `top_p` برای محدود کردن انتخاب توکن‌ها به آن‌هایی که به بالاترین احتمال تجمعی کمک می‌کنند، به منظور بهبود کیفیت متن تولید شده بهره بردیم.  
- از `frequency_penalty` برای کاهش تکرار و تشویق تنوع در خروجی استفاده کردیم.  
- از `user_preferences` برای امکان سفارشی‌سازی پارامترهای نمونه‌گیری بر اساس سطح خلاقیت و تنوع تعریف شده توسط کاربر بهره بردیم.  
- از `task_type` برای تعیین استراتژی نمونه‌گیری مناسب برای درخواست استفاده کردیم تا پاسخ‌ها بر اساس ماهیت وظیفه بهتر تنظیم شوند.  
- از متد `send_request` برای ارسال پرامپت با پارامترهای نمونه‌گیری پیکربندی شده استفاده کردیم تا مدل متن را مطابق با نیازهای مشخص شده تولید کند.  
- از `generated_text` برای دریافت پاسخ مدل استفاده کردیم که همراه با پارامترهای نمونه‌گیری و نوع وظیفه برای تحلیل یا نمایش بازگردانده می‌شود.  
- از توابع `min` و `max` برای اطمینان از اینکه ترجیحات کاربر در بازه‌های معتبر قرار دارند استفاده کردیم تا پیکربندی نمونه‌گیری نامعتبر جلوگیری شود.

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

در کد بالا ما:

- کلاسی به نام `AdaptiveSamplingManager` ایجاد کردیم که نمونه‌گیری پویا را بر اساس نوع وظیفه و ترجیحات کاربر مدیریت می‌کند.  
- پروفایل‌های نمونه‌گیری برای انواع مختلف وظایف (خلاقانه، واقعی، کد، مکالمه‌ای) تعریف کردیم.  
- متدی برای تشخیص نوع وظیفه از روی پرامپت با استفاده از قواعد ساده پیاده‌سازی کردیم.  
- پارامترهای نمونه‌گیری را بر اساس نوع وظیفه تشخیص داده شده و ترجیحات کاربر محاسبه کردیم.  
- تنظیمات یادگرفته شده بر اساس عملکرد تاریخی را برای بهینه‌سازی پارامترهای نمونه‌گیری اعمال کردیم.  
- عملکرد را برای تنظیمات آینده ثبت کردیم تا سیستم از تعاملات گذشته بیاموزد.  
- درخواست‌ها را با پارامترهای نمونه‌گیری پیکربندی شده به صورت پویا ارسال کرده و متن تولید شده را همراه با پارامترهای اعمال شده و نوع وظیفه تشخیص داده شده بازگرداندیم.  
- از:  
    - `userPreferences` برای امکان سفارشی‌سازی پارامترهای نمونه‌گیری بر اساس سطح خلاقیت، دقت و ثبات تعریف شده توسط کاربر استفاده کردیم.  
    - `detectTaskType` برای تعیین ماهیت وظیفه بر اساس پرامپت بهره بردیم تا پاسخ‌ها بهتر متناسب با نوع درخواست تنظیم شوند.  
    - `recordPerformance` برای ثبت عملکرد پاسخ‌های تولید شده استفاده کردیم تا سیستم بتواند خود را تطبیق داده و بهبود بخشد.  
    - `applyLearnedAdjustments` برای تغییر پارامترهای نمونه‌گیری بر اساس عملکرد تاریخی به منظور افزایش کیفیت پاسخ‌ها به کار بردیم.  
    - `generateResponse` برای کپسوله کردن کل فرایند تولید پاسخ با نمونه‌گیری تطبیقی استفاده کردیم تا فراخوانی با پرامپت‌ها و کانتکست‌های مختلف آسان شود.  
    - `allowedTools` برای مشخص کردن ابزارهایی که مدل می‌تواند در طول تولید استفاده کند به کار بردیم تا پاسخ‌ها با توجه به کانتکست بهتر باشند.  
    - `feedbackScore` برای امکان ارائه بازخورد توسط کاربران درباره کیفیت پاسخ تولید شده استفاده کردیم که می‌تواند برای بهبود عملکرد مدل به کار رود.  
    - `performanceHistory` برای نگهداری سوابق تعاملات گذشته به منظور یادگیری از موفقیت‌ها و شکست‌ها استفاده کردیم.  
    - `getSamplingParameters` برای تنظیم پویا پارامترهای نمونه‌گیری بر اساس کانتکست درخواست به کار بردیم تا رفتار مدل انعطاف‌پذیرتر و پاسخگوتر شود.  
    - `detectTaskType` برای طبقه‌بندی وظیفه بر اساس پرامپت استفاده کردیم تا استراتژی نمونه‌گیری مناسب برای انواع مختلف درخواست‌ها اعمال شود.  
    - `samplingProfiles` برای تعریف پیکربندی‌های پایه نمونه‌گیری برای انواع مختلف وظایف به کار بردیم تا تنظیمات سریع‌تر و متناسب‌تر انجام شود.

---

## گام بعدی

- [5.7 مقیاس‌پذیری](../mcp-scaling/README.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.