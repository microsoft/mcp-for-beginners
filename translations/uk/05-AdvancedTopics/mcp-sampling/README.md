> [!WARNING]
> Семплінг застарілий у MCP `2026-07-28`. Цей урок збережено для
> спадкових реалізацій. Нові сервери повинні інтегруватися безпосередньо з API
> постачальника LLM.

# Семплінг у Протоколі Контексту Моделі

> Семплінг залишається у специфікації `2026-07-28` для сумісності і може
> бути видалений у першому оновленні, випущеному 28 липня 2027 року чи пізніше.
> Приклади в цьому уроці можуть використовувати SDK API, які реалізують `2025-11-25`.
> Дивіться [Що змінилося у MCP: Специфікація 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

У спадкових реалізаціях MCP семплінг дозволяє серверам запитувати завершення LLM
через клієнта. Цей урок пояснює цей застарілий протокольний
потік для сумісності та роботи з міграцією.

## Вступ

У цьому уроці ми розглянемо, як налаштувати параметри семплінгу в запитах MCP і зрозуміти основні механіки протоколу семплінгу.

## Цілі навчання

До кінця цього уроку ви зможете:

- Розуміти ключові параметри семплінгу, доступні в MCP.
- Налаштовувати параметри семплінгу для різних випадків використання.
- Реалізувати детермінований семплінг для відтворюваних результатів.
- Динамічно регулювати параметри семплінгу залежно від контексту та уподобань користувача.
- Застосовувати стратегії семплінгу для покращення продуктивності моделі в різних сценаріях.
- Розуміти, як працює семплінг у клієнт-серверному потоці MCP.

## Як працює семплінг у MCP

Потік семплінгу в MCP включає такі кроки:

1. Сервер надсилає запит `sampling/createMessage` клієнту
2. Клієнт перевіряє запит і може його змінити
3. Клієнт робить семплінг з LLM
4. Клієнт переглядає отримане завершення
5. Клієнт повертає результат серверу

Цей дизайн із людиною в циклі забезпечує користувачам контроль над тим, що LLM бачить і генерує.

## Огляд параметрів семплінгу

MCP визначає такі параметри семплінгу, які можна налаштовувати в клієнтських запитах:

| Параметр | Опис | Типовий діапазон |
|-----------|-------------|---------------|
| `temperature` | Контролює випадковість вибору токенів | 0.0 - 1.0 |
| `maxTokens` | Максимальна кількість токенів для генерації | Ціле число |
| `stopSequences` | Користувацькі послідовності, які зупиняють генерацію при зустрічі | Масив рядків |
| `metadata` | Додаткові параметри, специфічні для провайдера | JSON-об’єкт |

Багато провайдерів LLM підтримують додаткові параметри через поле `metadata`, які можуть включати:

| Загальний розширений параметр | Опис | Типовий діапазон |
|-----------|-------------|---------------|
| `top_p` | Семплінг "ядра" - обмежує токени до топ-кумулятивної ймовірності | 0.0 - 1.0 |
| `top_k` | Обмежує вибір токенів до топ K варіантів | 1 - 100 |
| `presence_penalty` | Карає токени залежно від їх наявності в тексті | -2.0 - 2.0 |
| `frequency_penalty` | Карає токени залежно від їх частоти в тексті | -2.0 - 2.0 |
| `seed` | Конкретне випадкове зерно для відтворюваних результатів | Ціле число |

## Формат прикладу запиту

Ось приклад запиту семплінгу від клієнта в MCP:

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

## Контроль людиною в циклі

Семплінг MCP розроблено з урахуванням людського нагляду:

- **Для підказок**:
  - Клієнти повинні показувати користувачам запропоновану підказку
  - Користувачі повинні мати змогу змінювати або відхиляти підказки
  - Системні підказки можуть фільтруватися або змінюватися
  - Включення контексту контролюється клієнтом

- **Для завершень**:
  - Клієнти повинні показувати користувачам завершення
  - Користувачі повинні мати змогу змінювати або відхиляти завершення
  - Клієнти можуть фільтрувати або змінювати завершення
  - Користувачі контролюють, яка модель використовується

З урахуванням цих принципів, розглянемо, як реалізувати семплінг у різних мовах програмування з акцентом на параметри, які зазвичай підтримуються провайдерами LLM.

## Заходи безпеки

При реалізації семплінгу в MCP враховуйте такі найкращі практики безпеки:

- **Перевіряйте весь вміст повідомлення** перед відправкою клієнту
- **Очищуйте конфіденційну інформацію** із підказок і завершень
- **Впроваджуйте обмеження частоти запитів** для запобігання зловживанням
- **Моніторьте використання семплінгу** для виявлення аномалій
- **Шифруйте дані в транзиті** за допомогою захищених протоколів
- **Дотримуйтеся політики конфіденційності користувачів** відповідно до нормативних вимог
- **Аудитуйте запити семплінгу** для відповідності та безпеки
- **Контролюйте витрати** через відповідні ліміти
- **Впроваджуйте тайм-аути** для запитів семплінгу
- **Обробляйте помилки моделі коректно** із відповідними резервними сценаріями

Параметри семплінгу дозволяють тонко налаштувати поведінку мовних моделей для досягнення бажаного балансу між детермінованими та творчими результатами.

Розглянемо, як налаштувати ці параметри в різних мовах програмування.

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

У наведеному коді ми:

- Створили MCP клієнта з конкретним URL сервера.
- Налаштували запит із параметрами семплінгу, такими як `temperature`, `top_p` та `top_k`.
- Відправили запит і вивели згенерований текст.
- Використали:
    - `allowedTools` для вказівки, які інструменти модель може використовувати під час генерації. У цьому випадку ми дозволили інструменти `ideaGenerator` і `marketAnalyzer` для допомоги у створенні креативних ідей додатків.
    - `frequencyPenalty` та `presencePenalty` для контролю повторень і різноманітності в результатах.
    - `temperature` для контролю випадковості результату, де вищі значення призводять до більш творчих відповідей.
    - `top_p` для обмеження вибору токенів тими, що складають топ кумулятивної ймовірності, що підвищує якість тексту.
    - `top_k` для обмеження моделі топ K найбільш імовірних токенів, що допомагає генерувати більш послідовні відповіді.
    - `frequencyPenalty` та `presencePenalty` для зменшення повторень і заохочення різноманітності в тексті.

# [JavaScript](#tab/javascript)

```javascript
// Приклад JavaScript: налаштування температури та вибірки Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Ініціалізувати клієнт MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Налаштувати запит з різними параметрами вибірки
  const creativeSampling = {
    temperature: 0.9,    // Вища температура = більша випадковість/креативність
    topP: 0.92,          // Розглядати токени з топ 92% ймовірнісної маси
    frequencyPenalty: 0.6, // Зменшити повторення послідовностей токенів
    presencePenalty: 0.4   // Карати токени, що вже з’являлися в тексті
  };
  
  const factualSampling = {
    temperature: 0.2,    // Нижча температура = більш детермінований/фактичний
    topP: 0.85,          // Трохи більше сфокусований вибір токенів
    frequencyPenalty: 0.2, // Мінімальне покарання за повторення
    presencePenalty: 0.1   // Мінімальне покарання за присутність
  };
  
  try {
    // Надіслати два запити з різними налаштуваннями вибірки
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
- Налаштували два набори параметрів семплінгу: один для творчих завдань і один для фактичних.
- Надіслали запити з цими конфігураціями, дозволивши моделі використовувати специфічні інструменти для кожного завдання.
- Вивели згенеровані відповіді, щоб продемонструвати вплив різних параметрів семплінгу.
- Використали `allowedTools` для вказівки, які інструменти модель може використовувати під час генерації. У цьому випадку ми дозволили `ideaGenerator` та `environmentalImpactTool` для творчих завдань, і `factChecker` та `dataAnalysisTool` для фактичних завдань.
- Використали `temperature` для контролю випадковості результату, де вищі значення призводять до більш творчих відповідей.

- Використано `top_p`, щоб обмежити вибір токенів тими, що складають верхню кумулятивну ймовірність, підвищуючи якість згенерованого тексту.
- Використано `frequencyPenalty` та `presencePenalty`, щоб зменшити повторення та заохотити різноманітність у результатах.
- Використано `top_k`, щоб обмежити модель лише топ K найбільш ймовірних токенів, що може допомогти у генерації більш послідовних відповідей.

---

## Детерміноване семплювання

Для застосунків, які потребують стабільних результатів, детерміноване семплювання забезпечує відтворюваність. Це робиться за допомогою фіксованого випадкового насіння та встановлення температури в нуль.

Розглянемо приклад реалізації, щоб продемонструвати детерміноване семплювання на різних мовах програмування.

# [Java](#tab/java)

```java
// Приклад Java: Детерміновані відповіді з фіксованим початковим значенням
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Використання фіксованого початкового значення для детермінованих результатів
        
        // Перший запит з фіксованим початковим значенням
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Нульова температура для максимальної детермінованості
            .build();
            
        // Другий запит з тим самим початковим значенням
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Виконати обидва запити
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Відповіді мають бути ідентичними через те саме початкове значення та температуру=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

У наведеному коді ми:

- Створили клієнта MCP із заданою URL сервера.
- Налаштували два запити з однаковим запитом, фіксованим насінням і температурою нуль.
- Відправили обидва запити та вивели згенерований текст.
- Показали, що відповіді ідентичні через детерміновану природу конфігурації семплювання (те саме насіння і температура).
- Використали `setSeed` для вказівки фіксованого випадкового насіння, що гарантує однаковий результат генерації для однакового вводу щоразу.
- Встановили `temperature` в нуль для максимальної детермінованості, означаючи, що модель завжди вибиратиме найбільш ймовірний наступний токен без випадковості.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Приклад JavaScript: детерміновані відповіді з контролем зерна випадковості
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Перший запит з фіксованим зерном
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Нульова температура для максимальної детермінованості
    });
    
    // Другий запит з тим самим зерном і температурою
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Третій запит з іншим зерном, але з тією ж температурою
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

- Ініціалізували клієнта MCP з URL сервера.
- Налаштували два запити з однаковим запитом, фіксованим насінням і температурою нуль.
- Відправили обидва запити та вивели згенерований текст.
- Показали, що відповіді ідентичні через детерміновану природу конфігурації семплювання (те саме насіння і температура).
- Використали `seed` для вказівки фіксованого випадкового насіння, що гарантує однаковий результат генерації для однакового вводу щоразу.
- Встановили `temperature` в нуль для максимальної детермінованості, означаючи, що модель завжди вибиратиме найбільш ймовірний наступний токен без випадковості.
- Використали інше насіння для третього запиту, щоб показати, що зміна насіння призводить до різних результатів, навіть при тому ж запиті і температурі.

---

## Динамічна конфігурація семплювання

Інтелектуальне семплювання адаптує параметри залежно від контексту й вимог кожного запиту. Це означає динамічну зміну параметрів, таких як temperature, top_p та штрафи, залежно від типу завдання, уподобань користувача або історичної продуктивності.

Розглянемо, як реалізувати динамічне семплювання на різних мовах програмування.

# [Python](#tab/python)

```python
# Приклад на Python: Динамічне вибіркове опитування на основі контексту запиту
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Визначте пресети вибірки для різних типів завдань
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Виберіть базовий пресет
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Налаштуйте залежно від уподобань користувача, якщо вони надані
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Масштабуйте температуру залежно від переваги креативності (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Налаштуйте top_p залежно від бажаної різноманітності відповідей
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Створіть і надішліть запит з користувацькими параметрами вибіркової вибірки
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Поверніть відповідь з метаданими вибірки для прозорості
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

У наведеному коді ми:

- Створили клас `DynamicSamplingService`, який керує адаптивним семплюванням.
- Визначили пресети семплювання для різних типів завдань (креативні, фактичні, коди, аналітичні).
- Обрали базовий пресет семплювання залежно від типу завдання.
- Відкоригували параметри семплювання залежно від уподобань користувача, таких як рівень креативності та різноманітність.
- Відправили запит із динамічно налаштованими параметрами семплювання.
- Повернули згенерований текст разом із застосованими параметрами семплювання та типом завдання для прозорості.
- Використали `temperature` для контролю випадковості результату, де вищі значення ведуть до більш креативних відповідей.
- Використали `top_p`, щоб обмежити вибір токенів тими, що складають верхню кумулятивну ймовірність, підвищуючи якість згенерованого тексту.
- Використали `frequency_penalty`, щоб зменшити повторення і заохотити різноманітність у виводі.
- Використали `user_preferences` для дозволу налаштування параметрів семплювання на основі визначених користувачем рівнів креативності та різноманітності.
- Використали `task_type` для визначення відповідної стратегії семплювання для запиту, що дозволяє отримувати більш адресні відповіді залежно від природи завдання.
- Використали метод `send_request` для відправки запиту з налаштованими параметрами семплювання, переконуючись, що модель генерує текст відповідно до заданих вимог.
- Використали `generated_text`, щоб отримати відповідь моделі, яка потім повертається разом із параметрами семплювання та типом завдання для подальшого аналізу чи відображення.
- Використали функції `min` та `max`, щоб переконатися, що уподобання користувача утримуються в межах допустимих значень, запобігаючи недійсним конфігураціям семплювання.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// Приклад JavaScript: динамічна конфігурація вибірки на основі контексту користувача
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Визначення базових профілів вибірки
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Відстеження історичної продуктивності
    this.performanceHistory = [];
  }
  
  // Визначення типу завдання за підказкою
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Проста евристична детекція - може бути покращена за допомогою класифікації ML
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
    
    // За замовчуванням - розмова, якщо чіткий тип не визначено
    return 'conversational';
  }
  
  // Обчислення параметрів вибірки на основі контексту та уподобань користувача
  getSamplingParameters(prompt, context = {}) {
    // Визначення типу завдання
    const taskType = this.detectTaskType(prompt, context);
    
    // Отримання базового профілю
    let params = {...this.samplingProfiles[taskType]};
    
    // Коригування на основі уподобань користувача
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Масштабування від 1 до 10 до відповідного діапазону температури
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Вища точність означає нижчий topP (більш сфокусований вибір)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Вища послідовність означає менші штрафи
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Застосування навчальних коригувань з історії продуктивності
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Проста адаптивна логіка - може бути покращена складнішими алгоритмами
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Розглядати лише недавню історію
    
    if (relevantHistory.length > 0) {
      // Обчислення середніх оцінок продуктивності
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Якщо продуктивність нижча за поріг, коригувати параметри
      if (avgScore < 0.7) {
        // Невелике коригування у бік безпечніших значень
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Запис продуктивності для майбутніх коригувань
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Оцінка якості відповіді від 0 до 1
    });
    
    // Обмеження розміру історії
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Отримання оптимізованих параметрів вибірки
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Надсилання запиту з оптимізованими параметрами
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Якщо користувач надає відгук, записувати його для майбутньої оптимізації
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

// Приклад використання
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Креативне завдання з користувацькими вподобаннями
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Висока креативність (1-10)
          consistency: 3  // Низька послідовність (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Завдання з генерації коду
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Низька креативність
          precision: 8,   // Висока точність
          consistency: 9  // Висока послідовність
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

- Створили клас `AdaptiveSamplingManager`, який керує динамічним семплюванням залежно від типу завдання та уподобань користувача.
- Визначили профілі семплювання для різних типів завдань (креативні, фактичні, код, розмовні).
- Реалізували метод для визначення типу завдання за запитом з використанням простих евристик.
- Розрахували параметри семплювання на основі визначеного типу завдання та уподобань користувача.
- Застосували вивчені корекції на основі історичної продуктивності для оптимізації параметрів семплювання.
- Зареєстрували продуктивність для майбутніх коригувань, що дозволяє системі навчатися на основі минулих взаємодій.
- Відправили запити з динамічно налаштованими параметрами семплювання та повернули згенерований текст разом із застосованими параметрами та визначеним типом завдання.
- Використали:
    - `userPreferences` для налаштування параметрів семплювання на основі визначених користувачем рівнів креативності, точності та послідовності.
    - `detectTaskType` для визначення характеру завдання за запитом, що дозволяє отримувати більш адресні відповіді.
    - `recordPerformance` для ведення журналу продуктивності згенерованих відповідей, що дає змогу системі адаптуватися і вдосконалюватися з часом.
    - `applyLearnedAdjustments` для модифікації параметрів семплювання на основі історичної продуктивності, покращуючи здатність моделі генерувати високоякісні відповіді.
    - `generateResponse` для інкапсуляції всього процесу генерації відповіді з адаптивним семплюванням, що спрощує виклики з різними запитами та контекстами.
    - `allowedTools` для вказівки, які інструменти може використовувати модель під час генерації, дозволяючи отримати більш контекстно-залежні відповіді.
    - `feedbackScore` для дозволу користувачам надавати відгук про якість згенерованої відповіді, що може бути використано для подальшого покращення продуктивності моделі з часом.
    - `performanceHistory` для ведення записів минулих взаємодій, що дозволяє системі навчатися на основі попередніх успіхів і невдач.
    - `getSamplingParameters` для динамічного налаштування параметрів семплювання залежно від контексту запиту, дозволяючи гнучкішу та чутливішу поведінку моделі.
    - `detectTaskType` для класифікації завдання за запитом, що дає змогу системі застосовувати відповідні стратегії семплювання для різних типів запитів.
    - `samplingProfiles` для визначення базових конфігурацій семплювання для різних типів завдань, що дозволяє швидко коригуватися залежно від природи запиту.

---

## Що далі

- [5.7 Масштабування](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->