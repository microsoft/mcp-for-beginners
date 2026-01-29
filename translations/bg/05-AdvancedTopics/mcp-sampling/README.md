# Sampling в протокола Model Context

Sampling е мощна функция на MCP, която позволява на сървърите да заявяват LLM завършвания чрез клиента, като така се осъществяват сложни агентни поведения, запазвайки сигурността и поверителността. Правилната конфигурация на sampling може значително да подобри качеството и производителността на отговорите. MCP предоставя стандартизиран начин за контролиране на начина, по който моделите генерират текст с конкретни параметри, които влияят върху случайността, креативността и свързаността.

## Въведение

В този урок ще разгледаме как да конфигурираме sampling параметрите в MCP заявки и ще разберем основните механизми на протокола за sampling.

## Учебни цели

След края на този урок ще можете да:

- Разбирате ключовите sampling параметри, налични в MCP.
- Конфигурирате sampling параметри за различни случаи на употреба.
- Прилагате детерминиран sampling за възпроизводими резултати.
- Динамично настройвате sampling параметрите според контекста и предпочитанията на потребителя.
- Използвате sampling стратегии за подобряване на производителността на модела в различни сценарии.
- Разбирате как работи sampling в клиент-сървърния поток на MCP.

## Как работи Sampling в MCP

Потокът на sampling в MCP следва следните стъпки:

1. Сървърът изпраща заявка `sampling/createMessage` към клиента
2. Клиентът преглежда заявката и може да я модифицира
3. Клиентът извършва sampling от LLM
4. Клиентът преглежда получения резултат
5. Клиентът връща резултата на сървъра

Този дизайн с човека в цикъла гарантира, че потребителите запазват контрол върху това, което LLM вижда и генерира.

## Преглед на Sampling параметрите

MCP дефинира следните sampling параметри, които могат да се конфигурират в клиентските заявки:

| Параметър | Описание | Типичен диапазон |
|-----------|----------|------------------|
| `temperature` | Контролира случайността при избора на токени | 0.0 - 1.0 |
| `maxTokens` | Максимален брой токени за генериране | Цяло число |
| `stopSequences` | Потребителски последователности, които спират генерирането при срещане | Масив от низове |
| `metadata` | Допълнителни параметри, специфични за доставчика | JSON обект |

Много доставчици на LLM поддържат допълнителни параметри чрез полето `metadata`, които могат да включват:

| Често използван параметър | Описание | Типичен диапазон |
|---------------------------|----------|------------------|
| `top_p` | Nucleus sampling - ограничава токените до най-вероятните с кумулативна вероятност | 0.0 - 1.0 |
| `top_k` | Ограничение на избора до топ K опции | 1 - 100 |
| `presence_penalty` | Налага наказание на токени според тяхното присъствие в текста досега | -2.0 - 2.0 |
| `frequency_penalty` | Налага наказание на токени според честотата им в текста досега | -2.0 - 2.0 |
| `seed` | Конкретно случайно начало за възпроизводими резултати | Цяло число |

## Примерен формат на заявка

Ето пример за заявка за sampling от клиент в MCP:

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

## Формат на отговор

Клиентът връща резултат от завършване:

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

## Контрол с човека в цикъла

Sampling в MCP е проектиран с оглед на човешкия контрол:

- **За подсказки (prompts)**:
  - Клиентите трябва да показват на потребителите предложената подсказка
  - Потребителите трябва да могат да модифицират или отхвърлят подсказките
  - Системните подсказки могат да бъдат филтрирани или модифицирани
  - Включването на контекст се контролира от клиента

- **За завършвания (completions)**:
  - Клиентите трябва да показват на потребителите завършването
  - Потребителите трябва да могат да модифицират или отхвърлят завършванията
  - Клиентите могат да филтрират или модифицират завършванията
  - Потребителите контролират кой модел се използва

С тези принципи наум, нека разгледаме как да имплементираме sampling на различни програмни езици, като се фокусираме върху параметрите, които са широко поддържани от доставчиците на LLM.

## Съображения за сигурност

При имплементиране на sampling в MCP, имайте предвид следните добри практики за сигурност:

- **Валидирайте цялото съдържание на съобщенията** преди да ги изпратите към клиента
- **Почиствайте чувствителна информация** от подсказки и завършвания
- **Прилагайте ограничения на честотата** за предотвратяване на злоупотреби
- **Наблюдавайте използването на sampling** за необичайни модели
- **Криптирайте данните при пренос** с помощта на сигурни протоколи
- **Обработвайте поверителността на потребителските данни** според съответните регулации
- **Аудитирайте заявките за sampling** за съответствие и сигурност
- **Контролирайте разходите** с подходящи лимити
- **Прилагайте таймаути** за заявки за sampling
- **Обработвайте грешки на модела** по подходящ начин с резервни варианти

Sampling параметрите позволяват фина настройка на поведението на езиковите модели, за да се постигне желан баланс между детерминирани и креативни изходи.

Нека разгледаме как да конфигурираме тези параметри на различни програмни езици.

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

В горния код сме:

- Създали MCP клиент с конкретен URL на сървъра.
- Конфигурирали заявка със sampling параметри като `temperature`, `top_p` и `top_k`.
- Изпратили заявката и отпечатали генерирания текст.
- Използвали:
    - `allowedTools`, за да посочим кои инструменти моделът може да използва по време на генериране. В този случай разрешихме инструментите `ideaGenerator` и `marketAnalyzer`, за да подпомогнат генерирането на креативни идеи за приложения.
    - `frequencyPenalty` и `presencePenalty`, за да контролираме повторенията и разнообразието в изхода.
    - `temperature`, за да контролираме случайността на изхода, като по-високите стойности водят до по-креативни отговори.
    - `top_p`, за да ограничим избора на токени до тези, които допринасят за най-голямата кумулативна вероятност, подобрявайки качеството на генерирания текст.
    - `top_k`, за да ограничим модела до топ K най-вероятни токени, което може да помогне за по-свързани отговори.
    - `frequencyPenalty` и `presencePenalty`, за да намалим повторенията и да насърчим разнообразието в генерирания текст.

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

В горния код сме:

- Инициализирали MCP клиент с URL на сървъра и API ключ.
- Конфигурирали два комплекта sampling параметри: един за креативни задачи и друг за фактически задачи.
- Изпратили заявки с тези конфигурации, позволявайки на модела да използва специфични инструменти за всяка задача.
- Отпечатали генерираните отговори, за да демонстрираме ефектите от различните sampling параметри.
- Използвали `allowedTools`, за да посочим кои инструменти моделът може да използва по време на генериране. В този случай разрешихме `ideaGenerator` и `environmentalImpactTool` за креативни задачи, и `factChecker` и `dataAnalysisTool` за фактически задачи.
- Използвали `temperature`, за да контролираме случайността на изхода, като по-високите стойности водят до по-креативни отговори.
- Използвали `top_p`, за да ограничим избора на токени до тези, които допринасят за най-голямата кумулативна вероятност, подобрявайки качеството на генерирания текст.
- Използвали `frequencyPenalty` и `presencePenalty`, за да намалим повторенията и да насърчим разнообразието в изхода.
- Използвали `top_k`, за да ограничим модела до топ K най-вероятни токени, което може да помогне за по-свързани отговори.

---

## Детерминиран Sampling

За приложения, изискващи последователни изходи, детерминираният sampling гарантира възпроизводими резултати. Това се постига чрез използване на фиксирано случайно начало (seed) и задаване на температурата на нула.

Нека разгледаме примерна имплементация, която демонстрира детерминиран sampling на различни програмни езици.

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

В горния код сме:

- Създали MCP клиент с посочен URL на сървъра.
- Конфигурирали две заявки със същата подсказка, фиксиран seed и температура нула.
- Изпратили и двете заявки и отпечатали генерирания текст.
- Демонстрирали, че отговорите са идентични поради детерминирания характер на sampling конфигурацията (същият seed и температура).
- Използвали `setSeed`, за да зададем фиксирано случайно начало, което гарантира, че моделът винаги генерира същия изход за една и съща входна стойност.
- Зададохме `temperature` на нула, за да осигурим максимална детерминираност, което означава, че моделът винаги ще избира най-вероятния следващ токен без случайност.

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

В горния код сме:

- Инициализирали MCP клиент с URL на сървъра.
- Конфигурирали две заявки със същата подсказка, фиксиран seed и температура нула.
- Изпратили и двете заявки и отпечатали генерирания текст.
- Демонстрирали, че отговорите са идентични поради детерминирания характер на sampling конфигурацията (същият seed и температура).
- Използвали `seed`, за да зададем фиксирано случайно начало, което гарантира, че моделът винаги генерира същия изход за една и съща входна стойност.
- Зададохме `temperature` на нула, за да осигурим максимална детерминираност, което означава, че моделът винаги ще избира най-вероятния следващ токен без случайност.
- Използвали различен seed за третата заявка, за да покажем, че промяната на seed води до различни изходи, дори при същата подсказка и температура.

---

## Динамична конфигурация на Sampling

Интелигентният sampling адаптира параметрите според контекста и изискванията на всяка заявка. Това означава динамично настройване на параметри като temperature, top_p и наказания според типа задача, предпочитанията на потребителя или историческата производителност.

Нека разгледаме как да имплементираме динамичен sampling на различни програмни езици.

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

В горния код сме:

- Създали клас `DynamicSamplingService`, който управлява адаптивния sampling.
- Дефинирали sampling пресети за различни типове задачи (креативни, фактически, код, аналитични).
- Избрали базов sampling preset според типа задача.
- Настроили sampling параметрите според потребителските предпочитания, като ниво на креативност и разнообразие.
- Изпратили заявката с динамично конфигурираните sampling параметри.
- Върнали генерирания текст заедно с приложените sampling параметри и типа задача за прозрачност.
- Използвали `temperature`, за да контролираме случайността на изхода, като по-високите стойности водят до по-креативни отговори.
- Използвали `top_p`, за да ограничим избора на токени до тези, които допринасят за най-голямата кумулативна вероятност, подобрявайки качеството на генерирания текст.
- Използвали `frequency_penalty`, за да намалим повторенията и да насърчим разнообразието в изхода.
- Използвали `user_preferences`, за да позволим персонализация на sampling параметрите според дефинирани от потребителя нива на креативност и разнообразие.
- Използвали `task_type`, за да определим подходящата sampling стратегия за заявката, позволявайки по-персонализирани отговори според естеството на задачата.
- Използвали метода `send_request`, за да изпратим подсказката с конфигурираните sampling параметри, гарантирайки, че моделът генерира текст според зададените изисквания.
- Използвали `generated_text`, за да получим отговора на модела, който след това се връща заедно с sampling параметрите и типа задача за по-нататъшен анализ или показване.
- Използвали функции `min` и `max`, за да гарантираме, че потребителските предпочитания са в допустимите граници, предотвратявайки невалидни конфигурации.

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

В горния код сме:

- Създали клас `AdaptiveSamplingManager`, който управлява динамичния sampling според типа задача и потребителските предпочитания.
- Дефинирали sampling профили за различни типове задачи (креативни, фактически, код, разговорни).
- Имплементирали метод за откриване на типа задача от подсказката чрез прости евристики.
- Изчислили sampling параметрите според открития тип задача и потребителските предпочитания.
- Приложили научени корекции на базата на историческа производителност за оптимизиране на sampling параметрите.
- Записали производителността за бъдещи корекции, позволявайки на системата да се учи от минали взаимодействия.
- Изпратили заявки с динамично конфигурирани sampling параметри и върнали генерирания текст заедно с приложените параметри и открития тип задача.
- Използвали:
    - `userPreferences`, за да позволим персонализация на sampling параметрите според дефинирани от потребителя нива на креативност, прецизност и последователност.
    - `detectTaskType`, за да определим естеството на задачата според подсказката, позволявайки по-персонализирани отговори.
    - `recordPerformance`, за да регистрираме производителността на генерираните отговори, което позволява системата да се адаптира и подобрява с времето.
    - `applyLearnedAdjustments`, за да модифицираме sampling параметрите на базата на историческа производителност, подобрявайки способността на модела да генерира качествени отговори.
    - `generateResponse`, за да обхванем целия процес на генериране на отговор с адаптивен sampling, улеснявайки извикването с различни подсказки и контексти.
    - `allowedTools`, за да посочим кои инструменти моделът може да използва по време на генериране, позволявайки по-контекстуални отговори.
    - `feedbackScore`, за да позволим на потребителите да дават обратна връзка за качеството на генерирания отговор, която може да се използва за допълнително усъвършенстване на модела с времето.
    - `performanceHistory`, за да поддържаме запис на минали взаимодействия, позволявайки системата да се учи от предишни успехи и неуспехи.
    - `getSamplingParameters`, за да динамично настройваме sampling параметрите според контекста на заявката, позволявайки по-гъвкаво и отзивчиво поведение на модела.
    - `detectTaskType`, за да класифицираме задачата според подсказката, позволявайки системата да прилага подходящи sampling стратегии за различни типове заявки.
    - `samplingProfiles`, за да дефинираме базови sampling конфигурации за различни типове

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.