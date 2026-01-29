# Сэмплирование в протоколе Model Context Protocol

Сэмплирование — это мощная функция MCP, которая позволяет серверам запрашивать завершения LLM через клиента, обеспечивая сложное агентное поведение при сохранении безопасности и конфиденциальности. Правильная настройка сэмплирования может значительно улучшить качество и производительность ответов. MCP предоставляет стандартизированный способ управления генерацией текста моделями с помощью параметров, влияющих на случайность, креативность и связность.

## Введение

В этом уроке мы рассмотрим, как настраивать параметры сэмплирования в запросах MCP и разберём основные механизмы протокола сэмплирования.

## Цели обучения

К концу урока вы сможете:

- Понимать ключевые параметры сэмплирования, доступные в MCP.
- Настраивать параметры сэмплирования для различных сценариев.
- Реализовывать детерминированное сэмплирование для воспроизводимых результатов.
- Динамически изменять параметры сэмплирования в зависимости от контекста и предпочтений пользователя.
- Применять стратегии сэмплирования для улучшения производительности модели в разных ситуациях.
- Понимать, как работает сэмплирование в клиент-серверном взаимодействии MCP.

## Как работает сэмплирование в MCP

Процесс сэмплирования в MCP включает следующие шаги:

1. Сервер отправляет клиенту запрос `sampling/createMessage`
2. Клиент проверяет запрос и может его изменить
3. Клиент выполняет сэмплирование из LLM
4. Клиент проверяет результат завершения
5. Клиент возвращает результат серверу

Такой подход с участием человека обеспечивает контроль пользователей над тем, что видит и генерирует LLM.

## Обзор параметров сэмплирования

MCP определяет следующие параметры сэмплирования, которые можно настроить в запросах клиента:

| Параметр | Описание | Типичный диапазон |
|----------|----------|-------------------|
| `temperature` | Управляет случайностью выбора токенов | 0.0 - 1.0 |
| `maxTokens` | Максимальное количество генерируемых токенов | Целое число |
| `stopSequences` | Пользовательские последовательности, при встрече с которыми генерация останавливается | Массив строк |
| `metadata` | Дополнительные параметры, специфичные для провайдера | JSON-объект |

Многие провайдеры LLM поддерживают дополнительные параметры через поле `metadata`, которые могут включать:

| Распространённый параметр расширения | Описание | Типичный диапазон |
|-------------------------------------|----------|-------------------|
| `top_p` | Nucleus sampling — ограничивает выбор токенов верхней кумулятивной вероятностью | 0.0 - 1.0 |
| `top_k` | Ограничивает выбор токенов топ-K вариантами | 1 - 100 |
| `presence_penalty` | Наказывает токены за их присутствие в тексте до этого момента | -2.0 - 2.0 |
| `frequency_penalty` | Наказывает токены за частоту их появления в тексте | -2.0 - 2.0 |
| `seed` | Конкретное случайное зерно для воспроизводимых результатов | Целое число |

## Пример формата запроса

Пример запроса на сэмплирование от клиента в MCP:

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

## Формат ответа

Клиент возвращает результат завершения:

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

## Управление с участием человека

Сэмплирование в MCP разработано с учётом контроля со стороны человека:

- **Для подсказок**:
  - Клиенты должны показывать пользователям предложенную подсказку
  - Пользователи должны иметь возможность изменять или отклонять подсказки
  - Системные подсказки могут фильтроваться или изменяться
  - Включение контекста контролируется клиентом

- **Для завершений**:
  - Клиенты должны показывать пользователям результат завершения
  - Пользователи должны иметь возможность изменять или отклонять завершения
  - Клиенты могут фильтровать или изменять завершения
  - Пользователи контролируют, какая модель используется

Исходя из этих принципов, рассмотрим, как реализовать сэмплирование на разных языках программирования, сосредоточившись на параметрах, которые обычно поддерживаются провайдерами LLM.

## Вопросы безопасности

При реализации сэмплирования в MCP учитывайте следующие лучшие практики безопасности:

- **Проверяйте всё содержимое сообщений** перед отправкой клиенту
- **Очищайте конфиденциальную информацию** из подсказок и завершений
- **Реализуйте ограничения по частоте запросов** для предотвращения злоупотреблений
- **Отслеживайте использование сэмплирования** на предмет необычной активности
- **Шифруйте данные при передаче** с помощью безопасных протоколов
- **Обеспечивайте конфиденциальность пользовательских данных** в соответствии с применимыми нормами
- **Проводите аудит запросов сэмплирования** для соответствия требованиям безопасности
- **Контролируйте расходы** с помощью соответствующих лимитов
- **Реализуйте тайм-ауты** для запросов сэмплирования
- **Обрабатывайте ошибки модели корректно** с использованием запасных вариантов

Параметры сэмплирования позволяют тонко настраивать поведение языковых моделей, достигая нужного баланса между детерминированностью и креативностью.

Далее рассмотрим, как настраивать эти параметры на разных языках программирования.

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

В приведённом коде мы:

- Создали MCP-клиент с указанным URL сервера.
- Настроили запрос с параметрами сэмплирования, такими как `temperature`, `top_p` и `top_k`.
- Отправили запрос и вывели сгенерированный текст.
- Использовали:
    - `allowedTools` для указания инструментов, которые модель может использовать во время генерации. В данном случае разрешены инструменты `ideaGenerator` и `marketAnalyzer` для помощи в создании креативных идей приложений.
    - `frequencyPenalty` и `presencePenalty` для контроля повторов и разнообразия в выводе.
    - `temperature` для управления случайностью вывода, где более высокие значения приводят к более креативным ответам.
    - `top_p` для ограничения выбора токенов теми, которые входят в верхнюю кумулятивную вероятность, улучшая качество текста.
    - `top_k` для ограничения модели топ-K наиболее вероятными токенами, что помогает создавать более связные ответы.
    - `frequencyPenalty` и `presencePenalty` для снижения повторов и поощрения разнообразия в сгенерированном тексте.

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

В приведённом коде мы:

- Инициализировали MCP-клиент с URL сервера и API-ключом.
- Настроили два набора параметров сэмплирования: для творческих задач и для фактических.
- Отправили запросы с этими конфигурациями, позволяя модели использовать определённые инструменты для каждой задачи.
- Вывели сгенерированные ответы, чтобы продемонстрировать влияние разных параметров сэмплирования.
- Использовали `allowedTools` для указания инструментов, которые модель может применять во время генерации. В данном случае разрешены `ideaGenerator` и `environmentalImpactTool` для творческих задач, а также `factChecker` и `dataAnalysisTool` для фактических.
- Использовали `temperature` для управления случайностью вывода, где более высокие значения приводят к более креативным ответам.
- Использовали `top_p` для ограничения выбора токенов теми, которые входят в верхнюю кумулятивную вероятность, улучшая качество текста.
- Использовали `frequencyPenalty` и `presencePenalty` для снижения повторов и поощрения разнообразия в выводе.
- Использовали `top_k` для ограничения модели топ-K наиболее вероятными токенами, что помогает создавать более связные ответы.

---

## Детерминированное сэмплирование

Для приложений, требующих стабильных результатов, детерминированное сэмплирование обеспечивает воспроизводимость. Это достигается использованием фиксированного случайного зерна и установкой температуры в ноль.

Рассмотрим пример реализации детерминированного сэмплирования на разных языках программирования.

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

В приведённом коде мы:

- Создали MCP-клиент с указанным URL сервера.
- Настроили два запроса с одинаковой подсказкой, фиксированным зерном и нулевой температурой.
- Отправили оба запроса и вывели сгенерированный текст.
- Продемонстрировали, что ответы идентичны благодаря детерминированной настройке сэмплирования (одинаковое зерно и температура).
- Использовали `setSeed` для указания фиксированного случайного зерна, что гарантирует одинаковый вывод модели для одного и того же ввода.
- Установили `temperature` в ноль для максимальной детерминированности, чтобы модель всегда выбирала наиболее вероятный следующий токен без случайности.

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

В приведённом коде мы:

- Инициализировали MCP-клиент с URL сервера.
- Настроили два запроса с одинаковой подсказкой, фиксированным зерном и нулевой температурой.
- Отправили оба запроса и вывели сгенерированный текст.
- Продемонстрировали, что ответы идентичны благодаря детерминированной настройке сэмплирования (одинаковое зерно и температура).
- Использовали `seed` для указания фиксированного случайного зерна, что гарантирует одинаковый вывод модели для одного и того же ввода.
- Установили `temperature` в ноль для максимальной детерминированности, чтобы модель всегда выбирала наиболее вероятный следующий токен без случайности.
- Использовали другое зерно для третьего запроса, чтобы показать, что изменение зерна приводит к разным результатам, даже при одинаковой подсказке и температуре.

---

## Динамическая настройка сэмплирования

Интеллектуальное сэмплирование адаптирует параметры в зависимости от контекста и требований каждого запроса. Это означает динамическую настройку таких параметров, как temperature, top_p и штрафы, в зависимости от типа задачи, предпочтений пользователя или исторической эффективности.

Рассмотрим, как реализовать динамическое сэмплирование на разных языках программирования.

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

В приведённом коде мы:

- Создали класс `DynamicSamplingService`, управляющий адаптивным сэмплированием.
- Определили пресеты сэмплирования для разных типов задач (творческие, фактические, код, аналитические).
- Выбрали базовый пресет сэмплирования в зависимости от типа задачи.
- Отрегулировали параметры сэмплирования с учётом предпочтений пользователя, таких как уровень креативности и разнообразия.
- Отправили запрос с динамически настроенными параметрами сэмплирования.
- Вернули сгенерированный текст вместе с применёнными параметрами сэмплирования и типом задачи для прозрачности.
- Использовали `temperature` для управления случайностью вывода, где более высокие значения приводят к более креативным ответам.
- Использовали `top_p` для ограничения выбора токенов теми, которые входят в верхнюю кумулятивную вероятность, улучшая качество текста.
- Использовали `frequency_penalty` для снижения повторов и поощрения разнообразия в выводе.
- Использовали `user_preferences` для настройки параметров сэмплирования на основе заданных пользователем уровней креативности и разнообразия.
- Использовали `task_type` для определения подходящей стратегии сэмплирования, позволяющей более точно адаптировать ответы в зависимости от характера задачи.
- Использовали метод `send_request` для отправки подсказки с настроенными параметрами сэмплирования, обеспечивая генерацию текста согласно заданным требованиям.
- Использовали `generated_text` для получения ответа модели, который затем возвращается вместе с параметрами сэмплирования и типом задачи для дальнейшего анализа или отображения.
- Использовали функции `min` и `max` для ограничения пользовательских предпочтений в допустимых пределах, предотвращая некорректные настройки сэмплирования.

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

В приведённом коде мы:

- Создали класс `AdaptiveSamplingManager`, управляющий динамическим сэмплированием на основе типа задачи и предпочтений пользователя.
- Определили профили сэмплирования для разных типов задач (творческие, фактические, код, разговорные).
- Реализовали метод для определения типа задачи по подсказке с помощью простых эвристик.
- Рассчитали параметры сэмплирования на основе определённого типа задачи и предпочтений пользователя.
- Применили обученные корректировки на основе исторической эффективности для оптимизации параметров сэмплирования.
- Зафиксировали показатели производительности для будущих корректировок, позволяя системе учиться на прошлых взаимодействиях.
- Отправили запросы с динамически настроенными параметрами сэмплирования и вернули сгенерированный текст вместе с применёнными параметрами и определённым типом задачи.
- Использовали:
    - `userPreferences` для настройки параметров сэмплирования на основе заданных пользователем уровней креативности, точности и последовательности.
    - `detectTaskType` для определения характера задачи по подсказке, что позволяет более точно адаптировать ответы.
    - `recordPerformance` для записи эффективности сгенерированных ответов, что помогает системе адаптироваться и улучшаться со временем.
    - `applyLearnedAdjustments` для изменения параметров сэмплирования на основе исторической эффективности, повышая качество ответов модели.
    - `generateResponse` для инкапсуляции всего процесса генерации ответа с адаптивным сэмплированием, упрощая вызов с разными подсказками и контекстами.
    - `allowedTools` для указания инструментов, которые модель может использовать во время генерации, обеспечивая более контекстно-зависимые ответы.
    - `feedbackScore` для сбора отзывов пользователей о качестве сгенерированного ответа, что может использоваться для дальнейшей оптимизации модели.
    - `performanceHistory` для ведения истории прошлых взаимодействий, позволяя системе учиться на успехах и ошибках.
    - `getSamplingParameters` для динамической настройки параметров сэмплирования в зависимости от контекста запроса, обеспечивая более гибкое и отзывчивое поведение модели.
    - `detectTaskType` для классификации задачи по подсказке, позволяя применять соответствующие стратегии сэмплирования для разных типов запросов.
    - `samplingProfiles` для определения базовых конфигураций сэмплирования для разных типов задач, что позволяет быстро адаптировать параметры в зависимости от характера запроса.

---

## Что дальше

- [5.7 Масштабирование](../mcp-scaling/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.