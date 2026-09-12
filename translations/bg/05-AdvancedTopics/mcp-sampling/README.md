> [!WARNING]
> Семплирането е остаряло в MCP `2026-07-28`. Този урок се запазва за
> наследствени реализации. Нови сървъри трябва да интегрират директно с API на доставчик на LLM.


# Семплиране в Протокол за Контекст на Модела

> Семплирането остава в спецификацията `2026-07-28` за съвместимост и е
> допустимо за премахване при първия преглед, пуснат на или след 28 юли,
> 2027. Примерите в този урок може да използват SDK API-та, които имплементират `2025-11-25`.
> Вижте [Какво се е променило в MCP: Спецификация 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

В наследствени реализации на MCP, семплирането позволява на сървърите да искат довършвания от LLM чрез клиента. Този урок обяснява този остарял протоколен поток за съвместимост и миграционна работа.







## Учебни цели

В края на този урок ще можете да:

- Разберете ключовите параметри за семплиране, налични в MCP.
- Конфигурирате параметрите за семплиране за различни случаи на употреба.
- Имплементирате детерминирано семплиране за възпроизводими резултати.
- Динамично настройвате параметрите за семплиране въз основа на контекст и потребителски предпочитания.
- Прилагате стратегии за семплиране за подобряване на представянето на модела в различни сценарии.
- Разберете как работи семплирането в клиент-сървърния поток на MCP.

## Как работи семплирането в MCP

Потокът на семплиране в MCP следва следните стъпки:

1. Сървърът изпраща заявка `sampling/createMessage` към клиента
2. Клиентът разглежда заявката и може да я модифицира
3. Клиентът семплира от LLM
4. Клиентът преглежда довършването
5. Клиентът връща резултата на сървъра

Този дизайн с човек в цикъла гарантира, че потребителите запазват контрол върху това, което LLM вижда и генерира.

## Преглед на параметрите за семплиране

MCP дефинира следните параметри за семплиране, които могат да се конфигурират в клиентските заявки:

| Параметър | Описание | Типичен диапазон |
|-----------|-------------|---------------|
| `temperature` | Контролира случайността при избора на токени | 0.0 - 1.0 |
| `maxTokens` | Максимален брой токени за генериране | Цяло число |
| `stopSequences` | Персонализирани последователности, които спират генерацията при срещане | Масив от низове |
| `metadata` | Допълнителни параметри специфични за доставчика | JSON обект |

Много доставчици на LLM поддържат допълнителни параметри чрез полето `metadata`, които може да включват:

| Често използван параметър за разширение | Описание | Типичен диапазон |
|-----------|-------------|---------------|
| `top_p` | Семплиране по ядро - ограничава токените до най-високата кумулативна вероятност | 0.0 - 1.0 |
| `top_k` | Ограничение на избора на токени до топ K опции | 1 - 100 |
| `presence_penalty` | Наказва токени на базата на тяхното присъствие в текста дотук | -2.0 - 2.0 |
| `frequency_penalty` | Наказва токени на базата на тяхната честота в текста дотук | -2.0 - 2.0 |
| `seed` | Специфично случайно семе за възпроизводими резултати | Цяло число |

## Примерен формат на заявка

Ето пример за заявка за семплиране от клиент в MCP:

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

Клиентът връща резултат от довършване:

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

## Контроли с човек в цикъла

Семплирането в MCP е проектирано с цел човешки надзор:


- **За подканите**:
  - Клиентите трябва да показват на потребителите предложената подканваща реплика
  - Потребителите трябва да могат да модифицират или отхвърлят подканите
  - Системните подканви могат да бъдат филтрирани или модифицирани
  - Включването на контекста се контролира от клиента

- **За завършванията**:
  - Клиентите трябва да показват на потребителите получения резултат
  - Потребителите трябва да могат да модифицират или отхвърлят завършванията
  - Клиентите могат да филтрират или модифицират завършванията
  - Потребителите контролират кой модел се използва

С тези принципи в ума, нека разгледаме как да приложим семплиране в различни програмни езици, съсредоточавайки се върху параметрите, които са общо поддържани от доставчиците на LLM.

## Съображения за сигурността

При прилагането на семплиране в MCP, следвайте тези най-добри практики за сигурност:

- **Валидирайте цялото съдържание на съобщенията** преди да го изпратите на клиента
- **Очиствайте чувствителната информация** от подканите и завършванията
- **Прилагайте ограничения на честотата** за предотвратяване на злоупотреби
- **Следете използването на семплиране** за необичайни модели
- **Криптирайте данните при предаване** с помощта на защитени протоколи
- **Обработвайте поверителността на потребителските данни** според съответните регулации
- **Провеждайте одити на заявките за семплиране** за съответствие и сигурност
- **Контролирайте разходите** с подходящи лимити
- **Прилагайте таймаути** за заявките за семплиране
- **Обработвайте грешките на модела с грижа** и подходящи резервни варианти

Параметрите за семплиране позволяват фина настройка на поведението на езиковите модели, за да се постигне желаното равновесие между детерминирани и креативни отговори.

Нека разгледаме как да конфигурираме тези параметри в различни програмни езици.

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

В предишния код сме:

- Създали MCP клиент със специфичен URL на сървъра.
- Конфигурирали заявка с параметри за семплиране като `temperature`, `top_p` и `top_k`.
- Изпратили заявката и отпечатали генерирания текст.
- Използвали сме:
    - `allowedTools`, за да посочим кои инструменти моделът може да използва по време на генерирането. В този случай разрешихме инструментите `ideaGenerator` и `marketAnalyzer`, за да подпомогнат генерирането на креативни идеи за приложения.
    - `frequencyPenalty` и `presencePenalty`, за да контролираме повторенията и разнообразието в изхода.
    - `temperature`, за да контролираме случайността на изхода, като по-високите стойности водят до по-креативни отговори.
    - `top_p`, за да ограничим избора на токени до тези, които допринасят за водещата кумулативна вероятност, подобрявайки качеството на генерирания текст.
    - `top_k`, за да ограничим модела само до топ K най-вероятни токена, което може да помогне за генериране на по-кохерентни отговори.
    - `frequencyPenalty` и `presencePenalty`, за да намалим повторенията и да насърчим разнообразието в генерирания текст.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript пример: Конфигурация за температура и Top-P семплиране
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Инициализиране на MCP клиента
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Конфигуриране на заявката с различни параметри за семплиране
  const creativeSampling = {
    temperature: 0.9,    // По-висока температура = повече случаен/креативен резултат
    topP: 0.92,          // Вземат се предвид токени с топ 92% вероятностна маса
    frequencyPenalty: 0.6, // Намаляване на повторението на последователности от токени
    presencePenalty: 0.4   // Наказване на токени, които са се появили в текста до момента
  };
  
  const factualSampling = {
    temperature: 0.2,    // По-ниска температура = по-детерминистичен/фактически резултат
    topP: 0.85,          // Малко по-фокусирано избиране на токени
    frequencyPenalty: 0.2, // Минимална санкция за повторение
    presencePenalty: 0.1   // Минимална санкция за присъствие
  };
  
  try {
    // Изпращане на две заявки с различни конфигурации за семплиране
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

В предишния код сме:

- Инициализирали MCP клиент с URL на сървъра и API ключ.
- Конфигурирали два комплекта параметри за семплиране: един за креативни задачи и друг за фактически задачи.
- Изпратили заявки с тези конфигурации, позволявайки на модела да използва специфични инструменти за всяка задача.
- Отпечатали генерираните отговори, за да демонстрираме ефектите от различните параметри за семплиране.
- Използвали `allowedTools`, за да посочим кои инструменти моделът може да използва по време на генерирането. В този случай разрешихме `ideaGenerator` и `environmentalImpactTool` за креативни задачи и `factChecker` и `dataAnalysisTool` за фактически задачи.
- Използвали `temperature`, за да контролираме случайността на изхода, където по-високите стойности водят до по-креативни отговори.

- Използвахме `top_p`, за да ограничим избора на токени до тези, които допринасят за най-горната кумулативна вероятност, подобрявайки качеството на генерирания текст.
- Използвахме `frequencyPenalty` и `presencePenalty`, за да намалим повторенията и да насърчим разнообразието в изхода.
- Използвахме `top_k`, за да ограничим модела до топ K най-вероятни токени, което може да помогне за генерирането на по-кохерентни отговори.

---

## Детерминирано семплиране

За приложения, които изискват последователни резултати, детерминираното семплиране осигурява възпроизводими резултати. Това се постига чрез използване на фиксирано случайно семе и задаване на температурата на нула.

Нека разгледаме по-долу примерна реализация, която демонстрира детерминираното семплиране на различни програмни езици.

# [Java](#tab/java)

```java
// Пример на Java: Детерминирани отговори с фиксирано семе
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Използване на фиксирано семе за детерминирани резултати
        
        // Първа заявка с фиксирано семе
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Нулева температура за максимален детерминизъм
            .build();
            
        // Втора заявка със същото семе
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Изпълнете и двете заявки
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Отговорите трябва да са идентични поради същото семе и температура=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

В предходния код ние:

- Създадохме MCP клиент със зададен URL на сървъра.
- Конфигурирахме две заявки със същия prompt, фиксирано семе и температура нула.
- Изпратихме двете заявки и отпечатахме генерирания текст.
- Демонстрирахме, че отговорите са идентични поради детерминирания характер на конфигурацията за семплиране (същото семе и температура).
- Използвахме `setSeed`, за да зададем фиксирано случайно семе, осигурявайки модела да генерира един и същ изход за един и същ вход всеки път.
- Зададохме `temperature` на нула, за да осигурим максимален детерминизъм, което означава, че моделът винаги ще избира най-вероятния следващ токен без случайност.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript пример: Детерминистични отговори с управление на семето
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Първа заявка със фиксирано семе
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Нулева температура за максимален детерминизъм
    });
    
    // Втора заявка със същото семе и температура
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Трета заявка с различно семе, но същата температура
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

В предходния код ние:

- Инициализирахме MCP клиент със зададен URL на сървъра.
- Конфигурирахме две заявки със същия prompt, фиксирано семе и температура нула.
- Изпратихме двете заявки и отпечатахме генерирания текст.
- Демонстрирахме, че отговорите са идентични поради детерминирания характер на конфигурацията за семплиране (същото семе и температура).
- Използвахме `seed`, за да зададем фиксирано случайно семе, осигурявайки модела да генерира един и същ изход за един и същ вход всеки път.
- Зададохме `temperature` на нула, за да осигурим максимален детерминизъм, което означава, че моделът винаги ще избира най-вероятния следващ токен без случайност.
- Използвахме различно семе за третата заявка, за да покажем, че промяната на семето води до различни изходи, дори със същия prompt и температура.

---

## Динамична конфигурация на семплирането

Интелигентното семплиране адаптира параметрите въз основа на контекста и изискванията на всяка заявка. Това означава динамично настройване на параметри като температура, top_p и наказания според типа задача, предпочитанията на потребителя или историческата производителност.

Нека разгледаме как да реализираме динамично семплиране на различни програмни езици.

# [Python](#tab/python)

```python
# Python пример: Динамично вземане на проби в зависимост от контекста на заявката
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Дефиниране на предварително зададени настройки за вземане на проби за различни типове задачи
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Избор на базова предварителна настройка
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Настройка въз основа на потребителски предпочитания, ако са предоставени
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Мащабиране на температурата въз основа на предпочитанията за креативност (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Настройка на top_p въз основа на желаното разнообразие на отговора
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Създаване и изпращане на заявка с персонализирани параметри за вземане на проби
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Връщане на отговор с метаданни за вземане на проби за прозрачност
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

В предходния код ние:

- Създадохме клас `DynamicSamplingService`, който управлява адаптивното семплиране.
- Дефинирахме пресети за семплиране за различни типове задачи (креативни, фактически, код, аналитични).
- Избрахме базов пресет за семплиране въз основа на типа задача.
- Настроихме параметрите за семплиране според предпочитанията на потребителя, като ниво на креативност и разнообразие.
- Изпратихме заявката с динамично конфигурираните параметри за семплиране.
- Върнахме генерирания текст заедно с приложените параметри за семплиране и типа задача за прозрачност.
- Използвахме `temperature`, за да контролираме случайността на изхода, където по-високи стойности водят до по-креативни отговори.
- Използвахме `top_p`, за да ограничим избора на токени до тези, които допринасят за най-горната кумулативна вероятност, подобрявайки качеството на генерирания текст.
- Използвахме `frequency_penalty`, за да намалим повторенията и да насърчим разнообразието в изхода.
- Използвахме `user_preferences`, за да позволим персонализиране на параметрите за семплиране според дефинираните от потребителя нива на креативност и разнообразие.
- Използвахме `task_type`, за да определим подходящата стратегия за семплиране на заявката, позволявайки по-прецизни отговори според естеството на задачата.
- Използвахме метода `send_request`, за да изпратим prompt с конфигурираните параметри за семплиране, осигурявайки генериране на текст според зададените изисквания.
- Използвахме `generated_text`, за да получим отговора на модела, който после се връща заедно с параметрите за семплиране и типа задача за по-нататъшен анализ или показване.
- Използвахме функциите `min` и `max`, за да гарантираме, че предпочитанията на потребителя са ограничени в валидни диапазони, предотвратявайки невалидни конфигурации на семплиране.

# [JavaScript Динамично](#tab/javascript-dynamic)

```javascript
// Пример на JavaScript: Динамична конфигурация на извадката въз основа на контекста на потребителя
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Определяне на базови профили на извадки
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Проследяване на историческата производителност
    this.performanceHistory = [];
  }
  
  // Откриване на типа задача от подканата
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Прост евристичен детектор - може да бъде подобрен с ML класификация
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
    
    // По подразбиране към разговорен тип, ако не е открит ясен тип
    return 'conversational';
  }
  
  // Изчисляване на параметрите на извадката въз основа на контекста и предпочитанията на потребителя
  getSamplingParameters(prompt, context = {}) {
    // Откриване на типа задача
    const taskType = this.detectTaskType(prompt, context);
    
    // Вземане на базовия профил
    let params = {...this.samplingProfiles[taskType]};
    
    // Регулиране въз основа на предпочитанията на потребителя
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Скалиране от 1 до 10 до подходящия температурен диапазон
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // По-високата прецизност означава по-нисък topP (по-фокусирано избиране)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // По-високата консистентност означава по-ниски наказания
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Прилагане на научени корекции от историята на производителността
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Прост адаптивен логик - може да бъде подобрен с по-сложни алгоритми
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Взимат се предвид само последните данни от историята
    
    if (relevantHistory.length > 0) {
      // Изчисляване на средни оценки за производителността
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Ако производителността е под прага, параметрите се коригират
      if (avgScore < 0.7) {
        // Лека корекция към по-безопасни стойности
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Записване на производителността за бъдещи корекции
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Оценка от 0 до 1 за качеството на отговора
    });
    
    // Ограничаване на размера на историята
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Вземане на оптимизирани параметри на извадката
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Изпращане на заявка с оптимизирани параметри
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Ако потребителят предостави обратна връзка, тя се записва за бъдеща оптимизация
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

// Пример за използване
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Творческа задача с персонализирани потребителски предпочитания
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Висока креативност (1-10)
          consistency: 3  // Ниска консистентност (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Задача за генериране на код
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Ниска креативност
          precision: 8,   // Висока прецизност
          consistency: 9  // Висока консистентност
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

В предходния код ние:

- Създадохме клас `AdaptiveSamplingManager`, който управлява динамичното семплиране въз основа на типа задача и предпочитанията на потребителя.
- Дефинирахме профили за семплиране за различни типове задачи (креативни, фактически, код, разговорни).
- Реализирахме метод за разпознаване на типа задача от prompt с помощта на прости евристики.
- Изчислихме параметрите за семплиране въз основа на открития тип задача и предпочитанията на потребителя.
- Прилагаме научени корекции въз основа на историческата производителност за оптимизиране на параметрите на семплиране.
- Записахме производителността за бъдещи корекции, което позволява на системата да се учи от минали взаимодействия.
- Изпратихме заявки с динамично конфигурирани параметри за семплиране и върнахме генерирания текст заедно с приложените параметри и открития тип задача.
- Използвахме:
    - `userPreferences`, за да позволим персонализиране на параметрите за семплиране според дефинираните от потребителя нива на креативност, прецизност и последователност.
    - `detectTaskType`, за да определим естеството на задачата според prompt, позволявайки по-прецизни отговори.
    - `recordPerformance`, за да логваме представянето на генерираните отговори, като позволяваме на системата да се адаптира и подобрява с времето.
    - `applyLearnedAdjustments`, за да модифицираме параметрите за семплиране въз основа на историческата производителност, подобрявайки способността на модела да генерира отговори с високо качество.
    - `generateResponse`, за да обобщим целия процес на генериране на отговор с адаптивно семплиране, което го прави лесен за извикване с различни prompt-и и контексти.
    - `allowedTools`, за да посочим кои инструменти моделът може да използва по време на генериране, позволявайки по-контекстуално осъзнати отговори.
    - `feedbackScore`, за да позволим на потребителите да предоставят обратна връзка за качеството на генерирания отговор, която може да се използва за по-нататъшно усъвършенстване на представянето на модела с времето.
    - `performanceHistory`, за да поддържаме запис на минали взаимодействия, което позволява на системата да се учи от предишни успехи и неуспехи.
    - `getSamplingParameters`, за да настройваме динамично параметрите за семплиране въз основа на контекста на заявката, което позволява по-гъвкаво и адаптивно поведение на модела.
    - `detectTaskType`, за да класифицираме задачата според prompt, позволявайки на системата да прилага подходящи стратегии за семплиране за различни видове заявки.
    - `samplingProfiles`, за да дефинираме базови конфигурации за семплиране за различни типове задачи, позволявайки бързи настройки според естеството на заявката.

---

## Какво следва

- [5.7 Scaling](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->