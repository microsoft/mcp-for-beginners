# Вибірка в протоколі Model Context Protocol

Вибірка — це потужна функція MCP, яка дозволяє серверам запитувати завершення LLM через клієнта, забезпечуючи складні агентські поведінки при збереженні безпеки та конфіденційності. Правильне налаштування вибірки може суттєво покращити якість та продуктивність відповідей. MCP надає стандартизований спосіб контролю генерації тексту моделями з використанням конкретних параметрів, що впливають на випадковість, креативність і послідовність.

## Вступ

У цьому уроці ми розглянемо, як налаштовувати параметри вибірки в запитах MCP та зрозуміємо основні механізми протоколу вибірки.

## Цілі навчання

До кінця цього уроку ви зможете:

- Розуміти ключові параметри вибірки, доступні в MCP.
- Налаштовувати параметри вибірки для різних випадків використання.
- Реалізовувати детерміновану вибірку для відтворюваних результатів.
- Динамічно регулювати параметри вибірки залежно від контексту та уподобань користувача.
- Застосовувати стратегії вибірки для покращення продуктивності моделей у різних сценаріях.
- Розуміти, як працює вибірка у клієнт-серверному потоці MCP.

## Як працює вибірка в MCP

Потік вибірки в MCP проходить такі кроки:

1. Сервер надсилає запит `sampling/createMessage` клієнту
2. Клієнт переглядає запит і може його змінити
3. Клієнт виконує вибірку з LLM
4. Клієнт переглядає отриманий результат
5. Клієнт повертає результат серверу

Цей дизайн із людиною в циклі гарантує, що користувачі зберігають контроль над тим, що бачить і генерує LLM.

## Огляд параметрів вибірки

MCP визначає такі параметри вибірки, які можна налаштовувати в запитах клієнта:

| Параметр | Опис | Типовий діапазон |
|-----------|-------------|---------------|
| `temperature` | Контролює випадковість вибору токенів | 0.0 - 1.0 |
| `maxTokens` | Максимальна кількість токенів для генерації | Ціле число |
| `stopSequences` | Користувацькі послідовності, які зупиняють генерацію при зустрічі | Масив рядків |
| `metadata` | Додаткові параметри, специфічні для провайдера | JSON-об’єкт |

Багато провайдерів LLM підтримують додаткові параметри через поле `metadata`, які можуть включати:

| Поширений розширений параметр | Опис | Типовий діапазон |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling — обмежує вибір токенів до верхньої кумулятивної ймовірності | 0.0 - 1.0 |
| `top_k` | Обмежує вибір токенів до топ K варіантів | 1 - 100 |
| `presence_penalty` | Карає токени за їхню присутність у тексті до цього моменту | -2.0 - 2.0 |
| `frequency_penalty` | Карає токени за їхню частоту у тексті до цього моменту | -2.0 - 2.0 |
| `seed` | Конкретне випадкове зерно для відтворюваних результатів | Ціле число |

## Приклад формату запиту

Ось приклад запиту вибірки від клієнта в MCP:

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

## Формат відповіді

Клієнт повертає результат завершення:

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

## Контроль людини в циклі

Вибірка MCP розроблена з урахуванням людського контролю:

- **Для підказок**:
  - Клієнти повинні показувати користувачам запропоновану підказку
  - Користувачі повинні мати змогу змінювати або відхиляти підказки
  - Системні підказки можна фільтрувати або змінювати
  - Включення контексту контролюється клієнтом

- **Для завершень**:
  - Клієнти повинні показувати користувачам завершення
  - Користувачі повинні мати змогу змінювати або відхиляти завершення
  - Клієнти можуть фільтрувати або змінювати завершення
  - Користувачі контролюють, яка модель використовується

З урахуванням цих принципів, розглянемо, як реалізувати вибірку на різних мовах програмування, зосереджуючись на параметрах, які зазвичай підтримують провайдери LLM.

## Міркування щодо безпеки

При реалізації вибірки в MCP враховуйте такі найкращі практики безпеки:

- **Перевіряйте весь вміст повідомлень** перед відправленням клієнту
- **Очищуйте конфіденційну інформацію** з підказок і завершень
- **Впроваджуйте обмеження частоти запитів** для запобігання зловживанням
- **Моніторте використання вибірки** на предмет аномалій
- **Шифруйте дані під час передачі** за допомогою безпечних протоколів
- **Дотримуйтесь політики конфіденційності користувачів** відповідно до чинних норм
- **Аудитуйте запити вибірки** для відповідності та безпеки
- **Контролюйте витрати** за допомогою відповідних лімітів
- **Впроваджуйте таймаути** для запитів вибірки
- **Обробляйте помилки моделей** з відповідними запасними варіантами

Параметри вибірки дозволяють тонко налаштовувати поведінку мовних моделей для досягнення бажаного балансу між детермінованими та креативними відповідями.

Розглянемо, як налаштовувати ці параметри на різних мовах програмування.

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

У наведеному коді ми:

- Створили MCP клієнта з конкретною URL-адресою сервера.
- Налаштували запит із параметрами вибірки, такими як `temperature`, `top_p` і `top_k`.
- Відправили запит і вивели згенерований текст.
- Використали:
    - `allowedTools` для вказівки інструментів, які модель може використовувати під час генерації. У цьому випадку ми дозволили інструменти `ideaGenerator` та `marketAnalyzer` для допомоги у створенні креативних ідей додатків.
    - `frequencyPenalty` і `presencePenalty` для контролю повторень і різноманітності у вихідних даних.
    - `temperature` для контролю випадковості відповіді, де вищі значення ведуть до більш креативних результатів.
    - `top_p` для обмеження вибору токенів тими, що входять до верхньої кумулятивної ймовірності, що покращує якість згенерованого тексту.
    - `top_k` для обмеження моделі топ K найбільш ймовірними токенами, що допомагає генерувати більш послідовні відповіді.
    - `frequencyPenalty` і `presencePenalty` для зменшення повторень і заохочення різноманітності у згенерованому тексті.

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

У наведеному коді ми:

- Ініціалізували MCP клієнта з URL сервера та API ключем.
- Налаштували два набори параметрів вибірки: один для креативних завдань, інший — для фактичних.
- Відправили запити з цими конфігураціями, дозволяючи моделі використовувати конкретні інструменти для кожного завдання.
- Вивели згенеровані відповіді, щоб продемонструвати вплив різних параметрів вибірки.
- Використали `allowedTools` для вказівки інструментів, які модель може використовувати під час генерації. У цьому випадку ми дозволили `ideaGenerator` та `environmentalImpactTool` для креативних завдань, а також `factChecker` і `dataAnalysisTool` для фактичних.
- Використали `temperature` для контролю випадковості відповіді, де вищі значення ведуть до більш креативних результатів.
- Використали `top_p` для обмеження вибору токенів тими, що входять до верхньої кумулятивної ймовірності, що покращує якість згенерованого тексту.
- Використали `frequencyPenalty` і `presencePenalty` для зменшення повторень і заохочення різноманітності у вихідних даних.
- Використали `top_k` для обмеження моделі топ K найбільш ймовірними токенами, що допомагає генерувати більш послідовні відповіді.

---

## Детермінована вибірка

Для застосунків, які потребують послідовних результатів, детермінована вибірка забезпечує відтворюваність. Це досягається використанням фіксованого випадкового зерна та встановленням temperature у нуль.

Розглянемо приклад реалізації детермінованої вибірки на різних мовах програмування.

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

У наведеному коді ми:

- Створили MCP клієнта з вказаною URL-адресою сервера.
- Налаштували два запити з однаковою підказкою, фіксованим seed і нульовою temperature.
- Відправили обидва запити і вивели згенерований текст.
- Продемонстрували, що відповіді ідентичні через детермінований характер конфігурації вибірки (однаковий seed і temperature).
- Використали `setSeed` для вказівки фіксованого випадкового зерна, що гарантує однаковий результат для однакового вводу щоразу.
- Встановили `temperature` у нуль для максимальної детермінованості, тобто модель завжди вибиратиме найбільш ймовірний наступний токен без випадковості.

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

У наведеному коді ми:

- Ініціалізували MCP клієнта з URL сервера.
- Налаштували два запити з однаковою підказкою, фіксованим seed і нульовою temperature.
- Відправили обидва запити і вивели згенерований текст.
- Продемонстрували, що відповіді ідентичні через детермінований характер конфігурації вибірки (однаковий seed і temperature).
- Використали `seed` для вказівки фіксованого випадкового зерна, що гарантує однаковий результат для однакового вводу щоразу.
- Встановили `temperature` у нуль для максимальної детермінованості, тобто модель завжди вибиратиме найбільш ймовірний наступний токен без випадковості.
- Використали інше seed для третього запиту, щоб показати, що зміна seed призводить до різних результатів, навіть при однаковій підказці та temperature.

---

## Динамічне налаштування вибірки

Інтелектуальна вибірка адаптує параметри залежно від контексту та вимог кожного запиту. Це означає динамічне регулювання таких параметрів, як temperature, top_p і штрафи, залежно від типу завдання, уподобань користувача або історичної продуктивності.

Розглянемо, як реалізувати динамічну вибірку на різних мовах програмування.

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

У наведеному коді ми:

- Створили клас `DynamicSamplingService`, який керує адаптивною вибіркою.
- Визначили пресети вибірки для різних типів завдань (креативні, фактичні, код, аналітичні).
- Обрали базовий пресет вибірки залежно від типу завдання.
- Відкоригували параметри вибірки залежно від уподобань користувача, таких як рівень креативності та різноманітності.
- Відправили запит із динамічно налаштованими параметрами вибірки.
- Повернули згенерований текст разом із застосованими параметрами вибірки та типом завдання для прозорості.
- Використали `temperature` для контролю випадковості відповіді, де вищі значення ведуть до більш креативних результатів.
- Використали `top_p` для обмеження вибору токенів тими, що входять до верхньої кумулятивної ймовірності, що покращує якість згенерованого тексту.
- Використали `frequency_penalty` для зменшення повторень і заохочення різноманітності у вихідних даних.
- Використали `user_preferences` для налаштування параметрів вибірки на основі визначених користувачем рівнів креативності та різноманітності.
- Використали `task_type` для визначення відповідної стратегії вибірки для запиту, що дозволяє отримувати більш адаптовані відповіді залежно від характеру завдання.
- Використали метод `send_request` для відправлення підказки з налаштованими параметрами вибірки, забезпечуючи генерацію тексту відповідно до заданих вимог.
- Використали `generated_text` для отримання відповіді моделі, яка потім повертається разом із параметрами вибірки та типом завдання для подальшого аналізу або відображення.
- Використали функції `min` і `max` для обмеження уподобань користувача в межах допустимих значень, щоб уникнути некоректних конфігурацій вибірки.

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

У наведеному коді ми:

- Створили клас `AdaptiveSamplingManager`, який керує динамічною вибіркою залежно від типу завдання та уподобань користувача.
- Визначили профілі вибірки для різних типів завдань (креативні, фактичні, код, розмовні).
- Реалізували метод визначення типу завдання з підказки за допомогою простих евристик.
- Обчислили параметри вибірки на основі виявленого типу завдання та уподобань користувача.
- Застосували навчальні коригування на основі історичної продуктивності для оптимізації параметрів вибірки.
- Записали продуктивність для майбутніх коригувань, дозволяючи системі вчитися на минулих взаємодіях.
- Відправили запити з динамічно налаштованими параметрами вибірки та повернули згенерований текст разом із застосованими параметрами та виявленим типом завдання.
- Використали:
    - `userPreferences` для налаштування параметрів вибірки на основі визначених користувачем рівнів креативності, точності та послідовності.
    - `detectTaskType` для визначення характеру завдання на основі підказки, що дозволяє отримувати більш адаптовані відповіді.
    - `recordPerformance` для фіксації продуктивності згенерованих відповідей, що дає змогу системі адаптуватися та покращуватися з часом.
    - `applyLearnedAdjustments` для модифікації параметрів вибірки на основі історичної продуктивності, підвищуючи здатність моделі генерувати якісні відповіді.
    - `generateResponse` для інкапсуляції всього процесу генерації відповіді з адаптивною вибіркою, що полегшує виклик із різними підказками та контекстами.
    - `allowedTools` для вказівки інструментів, які модель може використовувати під час генерації, що дозволяє отримувати більш контекстно-залежні відповіді.
    - `feedbackScore` для надання користувачами зворотного зв’язку щодо якості згенерованої відповіді, що може використовуватися для подальшого вдосконалення продуктивності моделі.
    - `performanceHistory` для збереження записів минулих взаємодій, що дає змогу системі вчитися на попередніх успіхах і помилках.
    - `getSamplingParameters` для динамічного регулювання параметрів вибірки залежно від контексту зап

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.