> [!WARNING]
> Узорковање је застарело у MCP `2026-07-28`. Ова лекција се задржава за
> наслеђене имплементације. Нови сервери би требало да се интегришу директно са LLM
> добављачким API-јем.

# Узорковање у Model Context Protocol

> Узорковање остаје у спецификацији `2026-07-28` ради компатибилности и
> може бити уклоњено у првој ревизији објављеној на или након 28. јула,
> 2027. Примери у овој лекцији могу користити SDK API-је који имплементирају `2025-11-25`.
> Погледајте [Шта је ново у MCP: Спецификација 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

У наслеђеним MCP имплементацијама, узорковање омогућава серверима да захтевају LLM
довршења преко клијента. Ова лекција објашњава тај застарели протокол
ради компатибилности и миграционих радова.

## Увод

У овој лекцији ћемо истражити како конфигурисати параметре узорковања у MCP захтевима и разумети основне протоколске механике узорковања.

## Циљеви учења

По завршетку ове лекције, моћи ћете да:

- Разумете кључне параметре узорковања доступне у MCP.
- Конфигуришете параметре узорковања за различите употребне случајеве.
- Имплементирате детерминистичко узорковање за репродуктивне резултате.
- Динамички прилагођавате параметре узорковања у зависности од контекста и корисничких преференци.
- Примењујете стратегије узорковања за побољшање перформанси модела у различитим сценаријима.
- Разумете како узорковање функционише у клијент-сервер току MCP.

## Како узорковање функционише у MCP

Ток узорковања у MCP следи ове кораке:

1. Сервер шаље захтев `sampling/createMessage` клијенту
2. Клијент прегледа захтев и може га изменити
3. Клијент врши узорковање из LLM
4. Клијент прегледа резултат завршетка
5. Клијент враћа резултат серверу

Овај дизајн са људским надзором обезбеђује да корисници имају контролу над тим шта LLM види и генерише.

## Преглед параметара узорковања

MCP дефинише следеће параметре узорковања који се могу конфигурисати у захтевима клијента:

| Параметар | Опис | Типични распон |
|-----------|-------------|---------------|
| `temperature` | Контролише случајност у избору токена | 0.0 - 1.0 |
| `maxTokens` | Максималан број токена за генерисање | Целобројна вредност |
| `stopSequences` | Прилагођени низови који заустављају генерисање када се појаве | Низ струкова |
| `metadata` | Додатни провајдерски параметри | JSON објекат |

Многи LLM провајдери подржавају додатне параметре преко поља `metadata`, који могу укључивати:

| Уобичајени параметар проширења | Опис | Типични распон |
|-----------|-------------|---------------|
| `top_p` | Нуклеус узорковање - ограничење на токене са највишом кумулативном вероватноћом | 0.0 - 1.0 |
| `top_k` | Ограничава избор токена на првих К опција | 1 - 100 |
| `presence_penalty` | Казна токенима у зависности од њихове присутности у тексту до сада | -2.0 - 2.0 |
| `frequency_penalty` | Казна токенима у зависности од учесталости у тексту до сада | -2.0 - 2.0 |
| `seed` | Специфично насумично семе за репродуктивне резултате | Целобројна вредност |

## Пример формата захтева

Ево примера захтева за узорковање од клијента у MCP:

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

## Формат одговора

Клијент враћа резултат завршетка:

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

## Контрола људског надзора

MCP узорковање је дизајнирано узимајући у обзир људски надзор:

- **За упите**:
  - Клијенти треба да прикажу корисницима предложени упит
  - Корисници треба да могу да измене или одбију упите
  - Системски упити могу бити филтрирани или модификовани
  - Укључивање контекста контролише клијент

- **За завршетке**:
  - Клијенти треба да прикажу корисницима завршетак
  - Корисници треба да могу да измене или одбију завршетке
  - Клијенти могу филтрирати или модификовати завршетке
  - Корисници контролишу који модел се користи

Са овим принципима на уму, погледајмо како имплементирати узорковање у различитим програмским језицима, са фокусом на параметре које најчешће подржавају LLM провајдери.

## Безбедносне напомене

При имплементацији узорковања у MCP, имајте у виду следеће безбедносне добре праксе:

- **Валидација свих садржаја порука** пре слања клијенту
- **Санирање осетљивих информација** из упита и завршетака
- **Имплементација ограничења учесталости** ради спречавања злоупотребе
- **Надгледање употребе узорковања** за необичне обрасце
- **Енкрипција података у преносу** коришћењем безбедних протокола
- **Руковање приватношћу података корисника** у складу са релевантним прописима
- **Ревизија захтева за узорковање** ради усаглашености и безбедности
- **Контрола трошкова** примењујући одговарајућа ограничења
- **Имплементација тајм-аута** за захтеве узорковања
- **Грациозно руковање грешкама модела** коришћењем одговарајућих резервних решења

Параметри узорковања омогућавају фино подешавање понашања језичких модела како би се постигла жељена равнотежа између детерминистичких и креативних резултата.

Погледајмо како да конфигуришемо ове параметре у различитим програмским језицима.

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

У претходном коду смо:

- Креирали MCP клијента са одређеним URL-ом сервера.
- Конфигурисали захтев са параметрима узорковања као што су `temperature`, `top_p`, и `top_k`.
- Послали захтев и исписали генерисани текст.
- Користили смо:
    - `allowedTools` да наведемо које алате модел може користити током генерисања. У овом случају, дозволили смо алате `ideaGenerator` и `marketAnalyzer` да помогну у генерисању креативних идеја за апликације.
    - `frequencyPenalty` и `presencePenalty` за контролу понављања и разноликости у излазу.
    - `temperature` за контролу случајности излаза, где веће вредности воде ка креативнијим одговорима.
    - `top_p` да ограничимо избор токена на оне који доприносе највишој кумулативној вероватноћној маси, побољшавајући квалитет генерисаног текста.
    - `top_k` да ограничимо модел на првих K највероватнијих токена, што може помоћи у генерисању кохерентнијих одговора.
    - `frequencyPenalty` и `presencePenalty` за смањење понављања и подстицање разноликости у генерисаном тексту.

# [JavaScript](#tab/javascript)

```javascript
// Пример у ЈаваСкрипту: Конфигурација температуре и Top-P узорковања
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Иницијализуј MCP клијента
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Конфигуриши захтев са различитим параметрима узорковања
  const creativeSampling = {
    temperature: 0.9,    // Виша температура = више случајности/креативности
    topP: 0.92,          // Узми у обзир токене са најбољих 92% вероватноће
    frequencyPenalty: 0.6, // Смањи понављање секвенци токена
    presencePenalty: 0.4   // Казни токене који су се појавили у тексту до сада
  };
  
  const factualSampling = {
    temperature: 0.2,    // Нижа температура = више детерминистичко/фактичко
    topP: 0.85,          // Неће фокусиранији избор токена
    frequencyPenalty: 0.2, // Минимална казна за понављање
    presencePenalty: 0.1   // Минимална казна за присуство
  };
  
  try {
    // Пошаљи два захтева са различитим конфигурацијама узорковања
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

У претходном коду смо:

- Иницијализовали MCP клијента са URL-ом сервера и API кључем.
- Конфигурисали два скупа параметара узорковања: један за креативне задатке и други за фактичке задатке.
- Послали захтеве са овим конфигурацијама, дозвољавајући моделу да користи одређене алате за сваки задатак.
- Исписали генерисане одговоре како бисмо демонстрирали ефекте различитих параметара узорковања.
- Користили `allowedTools` да наведемо које алате модел може користити током генерисања. У овом случају, дозволили смо алате `ideaGenerator` и `environmentalImpactTool` за креативне задатке, и `factChecker` и `dataAnalysisTool` за фактичке задатке.
- Користили `temperature` за контролу случајности излаза, где веће вредности воде ка креативнијим одговорима.
- Користили `top_p` да ограничимо избор токена на оне који доприносе највишој кумулативној вероватноћној маси, побољшавајући квалитет генерисаног текста.
- Користили `frequencyPenalty` и `presencePenalty` за смањење понављања и подстицање разноликости у излазу.
- Користили `top_k` да ограничимо модел на првих K највероватнијих токена, што може помоћи у генерисању кохерентнијих одговора.

---

## Детерминистичко узорковање

За апликације које захтевају конзистентне излазе, детерминистичко узорковање обезбеђује репродуктивне резултате. То се постиже коришћењем фиксног насумичног семена и подешавањем температуре на нулу.

Погледајмо пример имплементације испод који демонстрира детерминистичко узорковање у различитим програмским језицима.

# [Java](#tab/java)

```java
// Јава пример: Детерминистички одговори са фиксним седом
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Коришћење фиксног седа за детерминистичке резултате
        
        // Први захтев са фиксним седом
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Нула температура за максималну детерминистичност
            .build();
            
        // Други захтев са истим седом
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Изврши оба захтева
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Одговори треба да буду идентични због истог седа и temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

У претходном коду смо:

- Креирали MCP клијента са одређеним URL-ом сервера.
- Конфигурисали два захтева са истим упитом, фиксним семеном и нултом температуром.
- Послали оба захтева и исписали генерисани текст.
- Демонстрирали да су одговори идентични због детерминистичке природе конфигурације узорковања (исто семе и температура).
- Користили `setSeed` да наведемо фиксно насумично семе, обезбеђујући да модел генерише исти излаз за исти улаз сваки пут.
- Поставили `temperature` на нулу да обезбедимо максималну детерминисаност, што значи да ће модел увек изабрати највероватнији следећи токен без случајности.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Пример у JavaScript-у: Детеминисични одговори са контролом сида
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Први захтев са фиксним сидом
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Нула температура за максималну детерминисаност
    });
    
    // Други захтев са истим сидом и температуром
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Трећи захтев са другачијим сидом али истом температуром
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

У претходном коду смо:

- Иницијализовали MCP клијента са URL-ом сервера.
- Конфигурисали два захтева са истим упитом, фиксним семеном и нултом температуром.
- Послали оба захтева и исписали генерисани текст.
- Демонстрирали да су одговори идентични због детерминистичке природе конфигурације узорковања (исто семе и температура).
- Користили `seed` да наведемо фиксно насумично семе, обезбеђујући да модел генерише исти излаз за исти улаз сваки пут.
- Поставили `temperature` на нулу да обезбедимо максималну детерминисаност, што значи да ће модел увек изабрати највероватнији следећи токен без случајности.
- Користили друго семе за трећи захтев да покажемо да промена семена резултира другачијим излазима, чак и са истим упитом и температуром.

---

## Динамичка конфигурација узорковања

Интелигентно узорковање прилагођава параметре на основу контекста и захтева сваког захтева. То значи динамичко подешавање параметара као што су temperature, top_p и казне на основу типа задатка, корисничких преференци или историјских перформанси.

Погледајмо како имплементирати динамичко узорковање у различитим програмским језицима.

# [Python](#tab/python)

```python
# Питхон пример: Динамичко узорковање засновано на контексту захтева
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Дефиниши преднаподе за узорковање за различите типове задатака
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Изабери основни предподешен параметар
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Прилагоди према корисничким преференцама ако су дате
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Скалирaj температуру у складу са преференцама креативности (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Прилагоди top_p у складу са жељеном разноликошћу одговора
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Креирај и пошаљи захтев са прилагођеним параметрима узорковања
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Врати одговор са метаподацима о узорковању ради транспарентности
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

У претходном коду смо:

- Креирали класу `DynamicSamplingService` која управља адаптивним узорковањем.
- Дефинисали претходне поставке узорковања за различите типове задатака (креативни, фактички, код, аналитички).
- Изабрали основни узорак на основу типа задатка.
- Прилагодили параметре узорковања на основу корисничких преференци, као што су ниво креативности и разноликости.
- Послали захтев са динамички конфигурисаним параметрима узорковања.
- Вратити генерисани текст заједно са примењеним параметрима узорковања и типом задатка ради транспарентности.
- Користили `temperature` за контролу случајности излаза, где веће вредности воде ка креативнијим одговорима.
- Користили `top_p` да ограничимо избор токена на оне који доприносе највишој кумулативној вероватноћној маси, побољшавајући квалитет генерисаног текста.
- Користили `frequency_penalty` за смањење понављања и подстицање разноликости у излазу.
- Користили `user_preferences` да дозволимо прилагођавање параметара узорковања на основу кориснички дефинисаних нивоа креативности и разноликости.
- Користили `task_type` да одредимо одговарајућу стратегију узорковања за захтев, омогућавајући прилагођене одговоре на основу природе задатка.
- Користили метод `send_request` за слање упита са конфигурисаним параметрима узорковања, осигуравајући да модел генерише текст у складу са назначеним захтевима.
- Користили `generated_text` да преузмемо одговор модела, који се потом враћа заједно са параметрима узорковања и типом задатка за додатну анализу или приказ.
- Користили функције `min` и `max` да обезбедимо да корисничке преференције буду унутар валидних опсега, спречавајући неважеће конфигурације узорковања.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript пример: Динамска конфигурација узорковања на основу корисничког контекста
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Дефинишите основне профиле узорковања
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Пратите историјске перформансе
    this.performanceHistory = [];
  }
  
  // Детектујте тип задатка из упита
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Једноставна хеуристичка детекција - може се унапредити ML класификацијом
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
    
    // Подразумевано конверзацијски ако није откривен јасан тип
    return 'conversational';
  }
  
  // Израчунајте параметре узорковања на основу контекста и корисничких преференци
  getSamplingParameters(prompt, context = {}) {
    // Детектујте тип задатка
    const taskType = this.detectTaskType(prompt, context);
    
    // Преузмите основни профил
    let params = {...this.samplingProfiles[taskType]};
    
    // Прилагодите на основу корисничких преференци
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Претворите скалу од 1-10 у одговарајући опсег температуре
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Већа прецизност значи нижи topP (фокусиранији избор)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Већа конзистентност значи ниже казне
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Примените научена прилагођавања из историје перформанси
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Једноставна адаптивна логика - може се унапредити софистициранијим алгоритмима
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Узмите у обзир само недавну историју
    
    if (relevantHistory.length > 0) {
      // Израчунајте просечне оцене перформанси
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Ако су перформансе испод прага, прилагодите параметре
      if (avgScore < 0.7) {
        // Благи помак ка сигурнијим вредностима
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Евидентирајте перформансе за будућа прилагођавања
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Оцена квалитета одговора од 0 до 1
    });
    
    // Ограничите величину историје
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Преузмите оптимизоване параметре узорковања
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Пошаљите захтев са оптимизованим параметрима
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Ако корисник да повратну информацију, евидентирајте је за будућу оптимизацију
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

// Пример коришћења
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Креативан задатак са прилагођеним корисничким преференцама
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Висок ниво креативности (1-10)
          consistency: 3  // Нижа конзистентност (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Задатак генерације кода
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Ниска креативност
          precision: 8,   // Висока прецизност
          consistency: 9  // Висока конзистентност
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

У претходном коду смо:

- Креирали класу `AdaptiveSamplingManager` која управља динамичким узорковањем на основу типа задатка и корисничких преференци.
- Дефинисали профиле узорковања за различите типове задатака (креативни, фактички, код, конверзациони).
- Имплементирали методу за детекцију типа задатка из упита користећи једноставне хеуристике.
- Израчунили параметре узорковања на основу детектованог типа задатка и корисничких преференци.
- Примењивали научена подешавања на основу историјских перформанси за оптимизацију параметара узорковања.
- Бележили перформансе ради будућих прилагођавања, омогућавајући систему да учи из претходних интеракција.
- Слање захтева са динамички конфигурисаним параметрима узорковања и враћање генерисаног текста заједно са примењеним параметрима и детектованим типом задатка.
- Користили:
    - `userPreferences` за прилагођавање параметара узорковања на основу кориснички дефинисаних нивоа креативности, прецизности и конзистентности.
    - `detectTaskType` за утврђивање природе задатка на основу упита, омогућавајући прилагођеније одговоре.
    - `recordPerformance` за евиденцију перформанси генерисаних одговора, омогућавајући систему да се прилагођава и унапређује током времена.
    - `applyLearnedAdjustments` за модификацију параметара узорковања на основу историјских перформанси, побољшавајући способност модела да генерише висококвалитетне одговоре.
    - `generateResponse` за обухватање целокупног процеса генерисања одговора са адаптивним узорковањем, чинећи га једноставним за коришћење са различитим упитима и контекстима.
    - `allowedTools` за наведено које алате модел може користити током генерисања, омогућавајући одговоре који су свеснији контекста.
    - `feedbackScore` за омогућавање корисницима да пруже повратне информације о квалитету генерисаног одговора, што се може користити за даље унапређење перформанси модела.
    - `performanceHistory` за одржавање евиденције прошлогодишњих интеракција, омогућавајући систему да учи из претходних успеха и неуспеха.
    - `getSamplingParameters` за динамичко подешавање параметара узорковања у зависности од контекста захтева, омогућавајући флексибилније и одзивније понашање модела.
    - `detectTaskType` за класификацију задатка на основу упита, омогућавајући систему да примени одговарајуће стратегије узорковања за различите типове захтева.
    - `samplingProfiles` за дефинисање основних конфигурација узорковања за различите типове задатака, омогућавајући брза подешавања на основу природе захтева.

---

## Шта следи

- [5.7 Скалирање](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->