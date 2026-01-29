# أخذ العينات في بروتوكول سياق النموذج (MCP)

أخذ العينات هو ميزة قوية في MCP تتيح للخوادم طلب إكمالات LLM عبر العميل، مما يمكّن سلوكيات وكيل متقدمة مع الحفاظ على الأمان والخصوصية. يمكن لتكوين أخذ العينات الصحيح أن يحسن بشكل كبير جودة الاستجابة والأداء. يوفر MCP طريقة موحدة للتحكم في كيفية توليد النماذج للنص مع معلمات محددة تؤثر على العشوائية والإبداع والتماسك.

## المقدمة

في هذا الدرس، سنستعرض كيفية تكوين معلمات أخذ العينات في طلبات MCP وفهم آليات البروتوكول الأساسية لأخذ العينات.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:

- فهم المعلمات الرئيسية لأخذ العينات المتاحة في MCP.
- تكوين معلمات أخذ العينات لحالات استخدام مختلفة.
- تنفيذ أخذ عينات حتمي للحصول على نتائج قابلة للتكرار.
- تعديل معلمات أخذ العينات ديناميكيًا بناءً على السياق وتفضيلات المستخدم.
- تطبيق استراتيجيات أخذ العينات لتعزيز أداء النموذج في سيناريوهات متنوعة.
- فهم كيفية عمل أخذ العينات في تدفق العميل-الخادم في MCP.

## كيف يعمل أخذ العينات في MCP

يتبع تدفق أخذ العينات في MCP الخطوات التالية:

1. يرسل الخادم طلب `sampling/createMessage` إلى العميل  
2. يراجع العميل الطلب ويمكنه تعديله  
3. يأخذ العميل عينة من LLM  
4. يراجع العميل الإكمال  
5. يعيد العميل النتيجة إلى الخادم  

يضمن هذا التصميم الذي يشمل الإنسان في الحلقة بقاء المستخدمين مسيطرين على ما يراه النموذج وما يولده.

## نظرة عامة على معلمات أخذ العينات

يحدد MCP معلمات أخذ العينات التالية التي يمكن تكوينها في طلبات العميل:

| المعلمة | الوصف | النطاق النموذجي |
|---------|--------|-----------------|
| `temperature` | يتحكم في العشوائية في اختيار الرموز | 0.0 - 1.0 |
| `maxTokens` | الحد الأقصى لعدد الرموز التي يتم توليدها | قيمة صحيحة |
| `stopSequences` | تسلسلات مخصصة توقف التوليد عند مواجهتها | مصفوفة من السلاسل النصية |
| `metadata` | معلمات إضافية خاصة بمزود الخدمة | كائن JSON |

يدعم العديد من مزودي LLM معلمات إضافية عبر حقل `metadata`، والتي قد تشمل:

| معلمة التوسعة الشائعة | الوصف | النطاق النموذجي |
|-----------------------|--------|-----------------|
| `top_p` | أخذ عينات النواة - يحدد الرموز ضمن أعلى احتمال تراكمي | 0.0 - 1.0 |
| `top_k` | يحدد اختيار الرموز ضمن أفضل K خيارات | 1 - 100 |
| `presence_penalty` | يعاقب الرموز بناءً على وجودها في النص حتى الآن | -2.0 - 2.0 |
| `frequency_penalty` | يعاقب الرموز بناءً على تكرارها في النص حتى الآن | -2.0 - 2.0 |
| `seed` | بذرة عشوائية محددة لنتائج قابلة للتكرار | قيمة صحيحة |

## مثال على صيغة الطلب

إليك مثال على طلب أخذ عينات من عميل في MCP:

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

## صيغة الاستجابة

يعيد العميل نتيجة الإكمال:

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

## ضوابط الإنسان في الحلقة

تم تصميم أخذ العينات في MCP مع وضع إشراف الإنسان في الاعتبار:

- **بالنسبة للمطالبات**:  
  - يجب على العملاء عرض المطالبة المقترحة للمستخدمين  
  - يجب أن يكون المستخدمون قادرين على تعديل أو رفض المطالبات  
  - يمكن تصفية أو تعديل مطالبات النظام  
  - يتحكم العميل في تضمين السياق  

- **بالنسبة للإكمالات**:  
  - يجب على العملاء عرض الإكمال للمستخدمين  
  - يجب أن يكون المستخدمون قادرين على تعديل أو رفض الإكمالات  
  - يمكن للعملاء تصفية أو تعديل الإكمالات  
  - يتحكم المستخدم في اختيار النموذج المستخدم  

مع وضع هذه المبادئ في الاعتبار، دعونا نلقي نظرة على كيفية تنفيذ أخذ العينات في لغات برمجة مختلفة، مع التركيز على المعلمات المدعومة عادة عبر مزودي LLM.

## اعتبارات الأمان

عند تنفيذ أخذ العينات في MCP، ضع في اعتبارك أفضل ممارسات الأمان التالية:

- **التحقق من صحة محتوى الرسالة بالكامل** قبل إرسالها إلى العميل  
- **تنقية المعلومات الحساسة** من المطالبات والإكمالات  
- **تنفيذ حدود معدل** لمنع سوء الاستخدام  
- **مراقبة استخدام أخذ العينات** للكشف عن أنماط غير معتادة  
- **تشفير البيانات أثناء النقل** باستخدام بروتوكولات آمنة  
- **معالجة خصوصية بيانات المستخدم** وفقًا للأنظمة ذات الصلة  
- **تدقيق طلبات أخذ العينات** للامتثال والأمان  
- **التحكم في التعرض للتكاليف** من خلال حدود مناسبة  
- **تنفيذ مهلات زمنية** لطلبات أخذ العينات  
- **التعامل مع أخطاء النموذج بسلاسة** مع حلول بديلة مناسبة  

تسمح معلمات أخذ العينات بضبط سلوك نماذج اللغة لتحقيق التوازن المطلوب بين المخرجات الحتمية والإبداعية.

دعونا نرى كيفية تكوين هذه المعلمات في لغات برمجة مختلفة.

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

في الكود السابق قمنا بـ:

- إنشاء عميل MCP مع عنوان URL محدد للخادم.  
- تكوين طلب بمعلمات أخذ العينات مثل `temperature`، `top_p`، و`top_k`.  
- إرسال الطلب وطباعة النص المولد.  
- استخدام:  
    - `allowedTools` لتحديد الأدوات التي يمكن للنموذج استخدامها أثناء التوليد. في هذه الحالة، سمحنا لأدوات `ideaGenerator` و`marketAnalyzer` بالمساعدة في توليد أفكار تطبيقات إبداعية.  
    - `frequencyPenalty` و`presencePenalty` للتحكم في التكرار والتنوع في المخرجات.  
    - `temperature` للتحكم في عشوائية المخرجات، حيث تؤدي القيم الأعلى إلى استجابات أكثر إبداعًا.  
    - `top_p` لتحديد اختيار الرموز ضمن أعلى كتلة احتمال تراكمي، مما يعزز جودة النص المولد.  
    - `top_k` لتقييد النموذج بأفضل K رموز محتملة، مما يساعد في توليد استجابات أكثر تماسكًا.  
    - `frequencyPenalty` و`presencePenalty` لتقليل التكرار وتشجيع التنوع في النص المولد.

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

في الكود السابق قمنا بـ:

- تهيئة عميل MCP مع عنوان URL للخادم ومفتاح API.  
- تكوين مجموعتين من معلمات أخذ العينات: واحدة للمهام الإبداعية وأخرى للمهام الواقعية.  
- إرسال طلبات بهذه التكوينات، مما يسمح للنموذج باستخدام أدوات محددة لكل مهمة.  
- طباعة الاستجابات المولدة لعرض تأثيرات معلمات أخذ العينات المختلفة.  
- استخدام `allowedTools` لتحديد الأدوات التي يمكن للنموذج استخدامها أثناء التوليد. في هذه الحالة، سمحنا لأدوات `ideaGenerator` و`environmentalImpactTool` للمهام الإبداعية، و`factChecker` و`dataAnalysisTool` للمهام الواقعية.  
- استخدام `temperature` للتحكم في عشوائية المخرجات، حيث تؤدي القيم الأعلى إلى استجابات أكثر إبداعًا.  
- استخدام `top_p` لتحديد اختيار الرموز ضمن أعلى كتلة احتمال تراكمي، مما يعزز جودة النص المولد.  
- استخدام `frequencyPenalty` و`presencePenalty` لتقليل التكرار وتشجيع التنوع في المخرجات.  
- استخدام `top_k` لتقييد النموذج بأفضل K رموز محتملة، مما يساعد في توليد استجابات أكثر تماسكًا.

---

## أخذ العينات الحتمي

للتطبيقات التي تتطلب مخرجات متسقة، يضمن أخذ العينات الحتمي نتائج قابلة للتكرار. يتم ذلك باستخدام بذرة عشوائية ثابتة وضبط درجة الحرارة إلى صفر.

لننظر في مثال تنفيذي أدناه يوضح أخذ العينات الحتمي في لغات برمجة مختلفة.

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

في الكود السابق قمنا بـ:

- إنشاء عميل MCP مع عنوان URL محدد للخادم.  
- تكوين طلبين بنفس المطالبة، بذرة ثابتة، ودرجة حرارة صفر.  
- إرسال كلا الطلبين وطباعة النص المولد.  
- إظهار أن الاستجابات متطابقة بسبب الطبيعة الحتمية لتكوين أخذ العينات (نفس البذرة ودرجة الحرارة).  
- استخدام `setSeed` لتحديد بذرة عشوائية ثابتة، مما يضمن أن النموذج يولد نفس المخرجات لنفس الإدخال في كل مرة.  
- ضبط `temperature` إلى صفر لضمان أقصى قدر من الحتمية، مما يعني أن النموذج سيختار دائمًا الرمز التالي الأكثر احتمالًا بدون عشوائية.

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

في الكود السابق قمنا بـ:

- تهيئة عميل MCP مع عنوان URL للخادم.  
- تكوين طلبين بنفس المطالبة، بذرة ثابتة، ودرجة حرارة صفر.  
- إرسال كلا الطلبين وطباعة النص المولد.  
- إظهار أن الاستجابات متطابقة بسبب الطبيعة الحتمية لتكوين أخذ العينات (نفس البذرة ودرجة الحرارة).  
- استخدام `seed` لتحديد بذرة عشوائية ثابتة، مما يضمن أن النموذج يولد نفس المخرجات لنفس الإدخال في كل مرة.  
- ضبط `temperature` إلى صفر لضمان أقصى قدر من الحتمية، مما يعني أن النموذج سيختار دائمًا الرمز التالي الأكثر احتمالًا بدون عشوائية.  
- استخدام بذرة مختلفة للطلب الثالث لإظهار أن تغيير البذرة يؤدي إلى مخرجات مختلفة، حتى مع نفس المطالبة ودرجة الحرارة.

---

## تكوين أخذ العينات الديناميكي

يتكيف أخذ العينات الذكي مع المعلمات بناءً على السياق ومتطلبات كل طلب. هذا يعني تعديل معلمات مثل temperature، top_p، والعقوبات بناءً على نوع المهمة، تفضيلات المستخدم، أو الأداء التاريخي.

لننظر في كيفية تنفيذ أخذ العينات الديناميكي في لغات برمجة مختلفة.

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

في الكود السابق قمنا بـ:

- إنشاء فئة `DynamicSamplingService` التي تدير أخذ العينات التكيفية.  
- تعريف إعدادات مسبقة لأخذ العينات لأنواع مهام مختلفة (إبداعي، واقعي، برمجي، تحليلي).  
- اختيار إعداد أخذ عينات أساسي بناءً على نوع المهمة.  
- تعديل معلمات أخذ العينات بناءً على تفضيلات المستخدم، مثل مستوى الإبداع والتنوع.  
- إرسال الطلب مع معلمات أخذ العينات المكونة ديناميكيًا.  
- إعادة النص المولد مع معلمات أخذ العينات ونوع المهمة للشفافية.  
- استخدام `temperature` للتحكم في عشوائية المخرجات، حيث تؤدي القيم الأعلى إلى استجابات أكثر إبداعًا.  
- استخدام `top_p` لتحديد اختيار الرموز ضمن أعلى كتلة احتمال تراكمي، مما يعزز جودة النص المولد.  
- استخدام `frequency_penalty` لتقليل التكرار وتشجيع التنوع في المخرجات.  
- استخدام `user_preferences` للسماح بتخصيص معلمات أخذ العينات بناءً على مستويات الإبداع والتنوع التي يحددها المستخدم.  
- استخدام `task_type` لتحديد استراتيجية أخذ العينات المناسبة للطلب، مما يسمح باستجابات أكثر تخصيصًا بناءً على طبيعة المهمة.  
- استخدام طريقة `send_request` لإرسال المطالبة مع معلمات أخذ العينات المكونة، مما يضمن توليد النص وفقًا للمتطلبات المحددة.  
- استخدام `generated_text` لاسترجاع استجابة النموذج، والتي تُعاد مع معلمات أخذ العينات ونوع المهمة لمزيد من التحليل أو العرض.  
- استخدام دوال `min` و`max` لضمان بقاء تفضيلات المستخدم ضمن نطاقات صالحة، مما يمنع تكوينات أخذ عينات غير صالحة.

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

في الكود السابق قمنا بـ:

- إنشاء فئة `AdaptiveSamplingManager` التي تدير أخذ العينات الديناميكي بناءً على نوع المهمة وتفضيلات المستخدم.  
- تعريف ملفات تعريف لأخذ العينات لأنواع مهام مختلفة (إبداعي، واقعي، برمجي، محادثة).  
- تنفيذ طريقة لاكتشاف نوع المهمة من المطالبة باستخدام قواعد بسيطة.  
- حساب معلمات أخذ العينات بناءً على نوع المهمة المكتشف وتفضيلات المستخدم.  
- تطبيق تعديلات متعلمة بناءً على الأداء التاريخي لتحسين معلمات أخذ العينات.  
- تسجيل الأداء للتعديلات المستقبلية، مما يسمح للنظام بالتعلم من التفاعلات السابقة.  
- إرسال طلبات بمعلمات أخذ العينات المكونة ديناميكيًا وإرجاع النص المولد مع المعلمات المطبقة ونوع المهمة المكتشف.  
- استخدام:  
    - `userPreferences` للسماح بتخصيص معلمات أخذ العينات بناءً على مستويات الإبداع والدقة والاتساق التي يحددها المستخدم.  
    - `detectTaskType` لتحديد طبيعة المهمة بناءً على المطالبة، مما يسمح باستجابات أكثر تخصيصًا.  
    - `recordPerformance` لتسجيل أداء الاستجابات المولدة، مما يمكن النظام من التكيف والتحسن مع الوقت.  
    - `applyLearnedAdjustments` لتعديل معلمات أخذ العينات بناءً على الأداء التاريخي، مما يعزز قدرة النموذج على توليد استجابات عالية الجودة.  
    - `generateResponse` لتغليف العملية الكاملة لتوليد استجابة بأخذ عينات تكيفي، مما يسهل استدعاءها مع مطالبات وسياقات مختلفة.  
    - `allowedTools` لتحديد الأدوات التي يمكن للنموذج استخدامها أثناء التوليد، مما يسمح باستجابات أكثر وعيًا بالسياق.  
    - `feedbackScore` للسماح للمستخدمين بتقديم ملاحظات على جودة الاستجابة المولدة، والتي يمكن استخدامها لتحسين أداء النموذج مع الوقت.  
    - `performanceHistory` للحفاظ على سجل التفاعلات السابقة، مما يمكن النظام من التعلم من النجاحات والإخفاقات السابقة.  
    - `getSamplingParameters` لضبط معلمات أخذ العينات ديناميكيًا بناءً على سياق الطلب، مما يسمح بسلوك نموذج أكثر مرونة واستجابة.  
    - `detectTaskType` لتصنيف المهمة بناءً على المطالبة، مما يمكن النظام من تطبيق استراتيجيات أخذ عينات مناسبة لأنواع مختلفة من الطلبات.  
    - `samplingProfiles` لتعريف تكوينات أخذ العينات الأساسية لأنواع مهام مختلفة، مما يسمح بتعديلات سريعة بناءً على طبيعة الطلب.

---

## ما التالي

- [5.7 التوسع](../mcp-scaling/README.md)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.