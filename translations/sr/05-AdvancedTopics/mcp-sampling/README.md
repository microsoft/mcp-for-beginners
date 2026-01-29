# Sampling у Model Context Protocol

Sampling је моћна MCP функција која омогућава серверима да преко клијента захтевају LLM комплетирања, омогућавајући сложене агентске понашања уз одржавање безбедности и приватности. Правилна конфигурација sampling-а може значајно побољшати квалитет и перформансе одговора. MCP пружа стандардизован начин контроле начина на који модели генеришу текст са специфичним параметрима који утичу на случајност, креативност и кохерентност.

## Увод

У овој лекцији ћемо истражити како се конфигуришу sampling параметри у MCP захтевима и разумети основне протоколске механизме sampling-а.

## Циљеви учења

До краја ове лекције моћи ћете да:

- Разумете кључне sampling параметре доступне у MCP.
- Конфигуришете sampling параметре за различите случајеве употребе.
- Имплементирате детерминистички sampling за репродуктивне резултате.
- Динамички прилагођавате sampling параметре у зависности од контекста и корисничких преференција.
- Примените sampling стратегије за побољшање перформанси модела у разним сценаријима.
- Разумете како sampling функционише у клијент-сервер току MCP.

## Како sampling ради у MCP

Sampling ток у MCP прати ове кораке:

1. Сервер шаље `sampling/createMessage` захтев клијенту
2. Клијент прегледа захтев и може га изменити
3. Клијент врши sampling из LLM
4. Клијент прегледа комплетирање
5. Клијент враћа резултат серверу

Овај дизајн са човеком у петљи осигурава да корисници задрже контролу над тим шта LLM види и генерише.

## Преглед sampling параметара

MCP дефинише следеће sampling параметре који се могу конфигурисати у клијентским захтевима:

| Параметар | Опис | Типичан опсег |
|-----------|-------------|---------------|
| `temperature` | Контролише случајност у избору токена | 0.0 - 1.0 |
| `maxTokens` | Максималан број токена за генерисање | Целобројна вредност |
| `stopSequences` | Прилагођени низови који заустављају генерисање када се појаве | Низ стрингова |
| `metadata` | Додатни параметри специфични за провајдера | JSON објекат |

Многи LLM провајдери подржавају додатне параметре кроз поље `metadata`, која могу укључивати:

| Уобичајени додатни параметар | Опис | Типичан опсег |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - ограничава токене на оне са највећом кумулативном вероватноћом | 0.0 - 1.0 |
| `top_k` | Ограничава избор токена на најбољих K опција | 1 - 100 |
| `presence_penalty` | Казна за токене на основу њихове присутности у тексту до сада | -2.0 - 2.0 |
| `frequency_penalty` | Казна за токене на основу учесталости у тексту до сада | -2.0 - 2.0 |
| `seed` | Конкретан случајни семе за репродуктивне резултате | Целобројна вредност |

## Пример формата захтева

Ево примера захтева за sampling од клијента у MCP:

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

Клијент враћа резултат комплетирања:

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

## Контрола са човеком у петљи

MCP sampling је дизајниран са људским надзором на уму:

- **За упите (prompts)**:
  - Клијенти треба да прикажу корисницима предложени упит
  - Корисници треба да могу да измене или одбију упите
  - Системски упити могу бити филтрирани или измењени
  - Укључивање контекста контролише клијент

- **За комплетирања**:
  - Клијенти треба да прикажу корисницима комплетирање
  - Корисници треба да могу да измене или одбију комплетирања
  - Клијенти могу филтрирати или мењати комплетирања
  - Корисници контролишу који модел се користи

Са овим принципима на уму, погледајмо како имплементирати sampling у различитим програмским језицима, фокусирајући се на параметре који су уобичајено подржани код LLM провајдера.

## Безбедносне напомене

При имплементацији sampling-а у MCP, имајте у виду следеће безбедносне препоруке:

- **Валидирајте сав садржај порука** пре слања клијенту
- **Очистите осетљиве информације** из упита и комплетирања
- **Имплементирајте ограничења брзине** да бисте спречили злоупотребу
- **Пратите коришћење sampling-а** ради уочавања необичних образаца
- **Шифрујте податке у преносу** коришћењем безбедних протокола
- **Обрадите приватност корисничких података** у складу са релевантним прописима
- **Аудитујте захтеве за sampling** ради усаглашености и безбедности
- **Контролишите трошкове** постављањем одговарајућих лимита
- **Имплементирајте тајмауте** за захтеве sampling-а
- **Обрадите грешке модела на прикладан начин** са одговарајућим резервним решењима

Sampling параметри омогућавају прецизно подешавање понашања језичких модела како би се постигла жељена равнотежа између детерминистичких и креативних излаза.

Погледајмо како се конфигуришу ови параметри у различитим програмским језицима.

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

У претходном коду смо:

- Креирали MCP клијента са одређеним URL-ом сервера.
- Конфигурисали захтев са sampling параметрима као што су `temperature`, `top_p` и `top_k`.
- Послали захтев и исписали генерисани текст.
- Користили:
    - `allowedTools` да одредимо које алате модел може користити током генерисања. У овом случају, дозволили смо алате `ideaGenerator` и `marketAnalyzer` да помогну у генерисању креативних идеја за апликације.
    - `frequencyPenalty` и `presencePenalty` за контролу понављања и разноликости у излазу.
    - `temperature` за контролу случајности излаза, где веће вредности воде ка креативнијим одговорима.
    - `top_p` да ограничимо избор токена на оне који доприносе највећој кумулативној вероватноћи, побољшавајући квалитет генерисаног текста.
    - `top_k` да ограничимо модел на највероватнијих K токена, што може помоћи у генерисању кохерентнијих одговора.
    - `frequencyPenalty` и `presencePenalty` да смањимо понављање и подстакнемо разноликост у генерисаном тексту.

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

У претходном коду смо:

- Иницијализовали MCP клијента са URL-ом сервера и API кључем.
- Конфигурисали два скупа sampling параметара: један за креативне задатке, други за фактичке.
- Послали захтеве са овим конфигурацијама, дозвољавајући моделу да користи одређене алате за сваки задатак.
- Исписали генерисане одговоре како бисмо демонстрирали ефекте различитих sampling параметара.
- Користили `allowedTools` да одредимо које алате модел може користити током генерисања. У овом случају, дозволили смо `ideaGenerator` и `environmentalImpactTool` за креативне задатке, и `factChecker` и `dataAnalysisTool` за фактичке задатке.
- Користили `temperature` за контролу случајности излаза, где веће вредности воде ка креативнијим одговорима.
- Користили `top_p` да ограничимо избор токена на оне који доприносе највећој кумулативној вероватноћи, побољшавајући квалитет генерисаног текста.
- Користили `frequencyPenalty` и `presencePenalty` да смањимо понављање и подстакнемо разноликост у излазу.
- Користили `top_k` да ограничимо модел на највероватнијих K токена, што може помоћи у генерисању кохерентнијих одговора.

---

## Детерминистички sampling

За апликације које захтевају конзистентне излазе, детерминистички sampling обезбеђује репродуктивне резултате. То се постиже коришћењем фиксног случајног семена и постављањем temperature на нулу.

Погледајмо пример имплементације детерминистичког sampling-а у различитим програмским језицима.

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

У претходном коду смо:

- Креирали MCP клијента са одређеним URL-ом сервера.
- Конфигурисали два захтева са истим упитом, фиксним семеном и нултом температуром.
- Послали оба захтева и исписали генерисани текст.
- Демонстрирали да су одговори идентични због детерминистичке природе sampling конфигурације (исто семе и температура).
- Користили `setSeed` да одредимо фиксно случајно семе, осигуравајући да модел увек генерише исти излаз за исти улаз.
- Поставили `temperature` на нулу како бисмо обезбедили максималну детерминисаност, што значи да модел увек бира највероватнији следећи токен без случајности.

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

У претходном коду смо:

- Иницијализовали MCP клијента са URL-ом сервера.
- Конфигурисали два захтева са истим упитом, фиксним семеном и нултом температуром.
- Послали оба захтева и исписали генерисани текст.
- Демонстрирали да су одговори идентични због детерминистичке природе sampling конфигурације (исто семе и температура).
- Користили `seed` да одредимо фиксно случајно семе, осигуравајући да модел увек генерише исти излаз за исти улаз.
- Поставили `temperature` на нулу како бисмо обезбедили максималну детерминисаност, што значи да модел увек бира највероватнији следећи токен без случајности.
- Користили друго семе за трећи захтев како бисмо показали да промена семена доводи до различитих излаза, чак и са истим упитом и температуром.

---

## Динамичка конфигурација sampling-а

Интелигентни sampling прилагођава параметре у зависности од контекста и захтева сваког захтева. То значи динамичко подешавање параметара као што су temperature, top_p и казне у зависности од типа задатка, корисничких преференција или историјских перформанси.

Погледајмо како имплементирати динамички sampling у различитим програмским језицима.

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

У претходном коду смо:

- Креирали класу `DynamicSamplingService` која управља адаптивним sampling-ом.
- Дефинисали sampling пресете за различите типове задатака (креативни, фактички, код, аналитички).
- Изабрали основни sampling пресет на основу типа задатка.
- Прилагодили sampling параметре у складу са корисничким преференцама, као што су ниво креативности и разноликости.
- Послали захтев са динамички конфигурисаним sampling параметрима.
- Вратили генерисани текст заједно са примењеним sampling параметрима и типом задатка ради транспарентности.
- Користили `temperature` за контролу случајности излаза, где веће вредности воде ка креативнијим одговорима.
- Користили `top_p` да ограничимо избор токена на оне који доприносе највећој кумулативној вероватноћи, побољшавајући квалитет генерисаног текста.
- Користили `frequency_penalty` да смањимо понављање и подстакнемо разноликост у излазу.
- Користили `user_preferences` да омогућимо прилагођавање sampling параметара на основу кориснички дефинисаних нивоа креативности и разноликости.
- Користили `task_type` да одредимо одговарајућу sampling стратегију за захтев, омогућавајући прилагођеније одговоре у зависности од природе задатка.
- Користили метод `send_request` за слање упита са конфигурисаним sampling параметрима, осигуравајући да модел генерише текст у складу са наведеним захтевима.
- Користили `generated_text` да преузмемо одговор модела, који се затим враћа заједно са sampling параметрима и типом задатка ради даље анализе или приказа.
- Користили функције `min` и `max` да осигурамо да су корисничке преференције унутар важећих опсега, спречавајући неважеће sampling конфигурације.

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

У претходном коду смо:

- Креирали класу `AdaptiveSamplingManager` која управља динамичким sampling-ом на основу типа задатка и корисничких преференција.
- Дефинисали sampling профиле за различите типове задатака (креативни, фактички, код, конверзациони).
- Имплементирали метод за детекцију типа задатка из упита користећи једноставне хеуристике.
- Израчунавали sampling параметре на основу детектованог типа задатка и корисничких преференција.
- Примењивали научене прилагођавања на основу историјских перформанси ради оптимизације sampling параметара.
- Евидентирали перформансе за будућа прилагођавања, омогућавајући систему да учи из претходних интеракција.
- Послали захтеве са динамички конфигурисаним sampling параметрима и вратили генерисани текст заједно са примењеним параметрима и детектованим типом задатка.
- Користили:
    - `userPreferences` да омогућимо прилагођавање sampling параметара на основу кориснички дефинисаних нивоа креативности, прецизности и конзистентности.
    - `detectTaskType` да одредимо природу задатка на основу упита, омогућавајући прилагођеније одговоре.
    - `recordPerformance` да евидентирамо перформансе генерисаних одговора, омогућавајући систему да се прилагођава и побољшава током времена.
    - `applyLearnedAdjustments` да модификујемо sampling параметре на основу историјских перформанси, побољшавајући способност модела да генерише квалитетне одговоре.
    - `generateResponse` да обухватимо цео процес генерисања одговора са адаптивним sampling-ом, олакшавајући позив са различитим упитима и контекстима.
    - `allowedTools` да одредимо које алате модел може користити током генерисања, омогу

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.