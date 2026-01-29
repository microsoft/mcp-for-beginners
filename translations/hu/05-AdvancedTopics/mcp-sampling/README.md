# Sampling a Model Context Protocolban

A sampling egy erőteljes MCP funkció, amely lehetővé teszi a szerverek számára, hogy LLM kiegészítéseket kérjenek a kliensen keresztül, így kifinomult, ügynöki viselkedéseket valósíthatnak meg, miközben megőrzik a biztonságot és a magánszférát. A megfelelő sampling beállítás jelentősen javíthatja a válaszok minőségét és teljesítményét. Az MCP szabványos módot kínál arra, hogy meghatározzuk, hogyan generáljanak a modellek szöveget, olyan paraméterekkel, amelyek befolyásolják a véletlenszerűséget, kreativitást és koherenciát.

## Bevezetés

Ebben a leckében megvizsgáljuk, hogyan lehet konfigurálni a sampling paramétereket MCP kérésekben, és megértjük a sampling mögötti protokollmechanizmust.

## Tanulási célok

A lecke végére képes leszel:

- Megérteni az MCP-ben elérhető kulcsfontosságú sampling paramétereket.
- Különböző felhasználási esetekhez konfigurálni a sampling paramétereket.
- Determinisztikus samplinget megvalósítani reprodukálható eredményekhez.
- Dinamikusan állítani a sampling paramétereket a kontextus és a felhasználói preferenciák alapján.
- Sampling stratégiákat alkalmazni a modell teljesítményének javítására különböző helyzetekben.
- Megérteni, hogyan működik a sampling a kliens-szerver MCP folyamatban.

## Hogyan működik a sampling az MCP-ben

A sampling folyamata az MCP-ben a következő lépésekből áll:

1. A szerver elküld egy `sampling/createMessage` kérést a kliensnek
2. A kliens átnézi a kérést, és módosíthatja azt
3. A kliens mintát vesz egy LLM-ből
4. A kliens átnézi a kiegészítést
5. A kliens visszaküldi az eredményt a szervernek

Ez az emberi felügyeletet biztosító kialakítás garantálja, hogy a felhasználók irányításuk alatt tarthatják, mit lát és generál az LLM.

## Sampling paraméterek áttekintése

Az MCP a következő sampling paramétereket definiálja, amelyeket a kliens kérésekben lehet konfigurálni:

| Paraméter | Leírás | Tipikus tartomány |
|-----------|--------|-------------------|
| `temperature` | Szabályozza a token kiválasztás véletlenszerűségét | 0.0 - 1.0 |
| `maxTokens` | A generálandó tokenek maximális száma | Egész szám |
| `stopSequences` | Egyedi szekvenciák, amelyek megállítják a generálást, ha előfordulnak | Karakterláncok tömbje |
| `metadata` | További, szolgáltató-specifikus paraméterek | JSON objektum |

Sok LLM szolgáltató további paramétereket támogat a `metadata` mezőn keresztül, amelyek például:

| Gyakori kiterjesztés paraméter | Leírás | Tipikus tartomány |
|-------------------------------|--------|-------------------|
| `top_p` | Nucleus sampling – korlátozza a tokeneket a legmagasabb kumulatív valószínűségre | 0.0 - 1.0 |
| `top_k` | Korlátozza a token kiválasztást a legjobb K opcióra | 1 - 100 |
| `presence_penalty` | Bünteti a tokeneket a szövegben való előfordulásuk alapján | -2.0 - 2.0 |
| `frequency_penalty` | Bünteti a tokeneket a szövegben való gyakoriságuk alapján | -2.0 - 2.0 |
| `seed` | Meghatározott véletlenszám-generátor mag a reprodukálható eredményekhez | Egész szám |

## Példa kérés formátum

Íme egy példa arra, hogyan kérhetünk samplinget egy kliensnél MCP-ben:

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

## Válasz formátum

A kliens egy kiegészítési eredményt ad vissza:

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

## Ember a folyamatban vezérlők

Az MCP sampling kialakítása emberi felügyeletet tart szem előtt:

- **Promptok esetén**:
  - A klienseknek meg kell mutatniuk a felhasználóknak a javasolt promptot
  - A felhasználók módosíthatják vagy elutasíthatják a promptokat
  - A rendszer promptokat szűrni vagy módosítani lehet
  - A kontextus bevonását a kliens szabályozza

- **Kiegészítések esetén**:
  - A klienseknek meg kell mutatniuk a felhasználóknak a kiegészítést
  - A felhasználók módosíthatják vagy elutasíthatják a kiegészítéseket
  - A kliensek szűrhetik vagy módosíthatják a kiegészítéseket
  - A felhasználók szabályozzák, melyik modellt használják

Ezekkel az alapelvekkel nézzük meg, hogyan valósítható meg a sampling különböző programozási nyelveken, különös tekintettel azokra a paraméterekre, amelyeket a legtöbb LLM szolgáltató támogat.

## Biztonsági megfontolások

Az MCP sampling megvalósításakor vedd figyelembe az alábbi biztonsági legjobb gyakorlatokat:

- **Ellenőrizd az összes üzenettartalmat** mielőtt elküldenéd a kliensnek
- **Tisztítsd meg az érzékeny információkat** a promptokból és kiegészítésekből
- **Alkalmazz sebességkorlátokat** a visszaélések megelőzésére
- **Figyeld a sampling használatot** szokatlan minták után kutatva
- **Titkosítsd az adatokat átvitel közben** biztonságos protokollokkal
- **Kezeld a felhasználói adatvédelmet** a vonatkozó szabályozások szerint
- **Auditáld a sampling kéréseket** megfelelőség és biztonság érdekében
- **Szabályozd a költségkitettséget** megfelelő korlátokkal
- **Alkalmazz időkorlátokat** a sampling kérésekre
- **Kezeld a modellhibákat** megfelelő tartalék megoldásokkal

A sampling paraméterek lehetővé teszik a nyelvi modellek viselkedésének finomhangolását, hogy elérjük a kívánt egyensúlyt a determinisztikus és kreatív kimenetek között.

Nézzük meg, hogyan konfigurálhatók ezek a paraméterek különböző programozási nyelveken.

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

Az előző kódban:

- Létrehoztunk egy MCP klienst egy adott szerver URL-lel.
- Beállítottunk egy kérést sampling paraméterekkel, mint például `temperature`, `top_p` és `top_k`.
- Elküldtük a kérést, és kiírtuk a generált szöveget.
- Használtuk:
    - `allowedTools`-t, hogy megadjuk, mely eszközöket használhatja a modell a generálás során. Ebben az esetben engedélyeztük az `ideaGenerator` és `marketAnalyzer` eszközöket, hogy segítsenek kreatív alkalmazásötletek generálásában.
    - `frequencyPenalty` és `presencePenalty`-t a kimenet ismétlődésének és változatosságának szabályozására.
    - `temperature`-t a kimenet véletlenszerűségének szabályozására, ahol a magasabb értékek kreatívabb válaszokat eredményeznek.
    - `top_p`-t, hogy korlátozzuk a tokenek kiválasztását a legmagasabb kumulatív valószínűséget képviselő tokenekre, javítva a generált szöveg minőségét.
    - `top_k`-t, hogy a modellt a legvalószínűbb K tokenre korlátozzuk, ami segíthet koherensebb válaszok generálásában.
    - `frequencyPenalty` és `presencePenalty`-t az ismétlődés csökkentésére és a változatosság ösztönzésére a generált szövegben.

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

Az előző kódban:

- Inicializáltunk egy MCP klienst szerver URL-lel és API kulccsal.
- Két különböző sampling paraméterkészletet állítottunk be: egyet kreatív feladatokra, egyet tényalapú feladatokra.
- Elküldtük a kéréseket ezekkel a konfigurációkkal, lehetővé téve, hogy a modell különböző eszközöket használjon az egyes feladatokhoz.
- Kiírtuk a generált válaszokat, hogy bemutassuk a különböző sampling paraméterek hatását.
- Használtuk az `allowedTools`-t, hogy megadjuk, mely eszközöket használhat a modell a generálás során. Ebben az esetben kreatív feladatokhoz engedélyeztük az `ideaGenerator` és `environmentalImpactTool` eszközöket, míg tényalapú feladatokhoz a `factChecker` és `dataAnalysisTool` eszközöket.
- Használtuk a `temperature`-t a kimenet véletlenszerűségének szabályozására, ahol a magasabb értékek kreatívabb válaszokat eredményeznek.
- Használtuk a `top_p`-t, hogy korlátozzuk a tokenek kiválasztását a legmagasabb kumulatív valószínűséget képviselő tokenekre, javítva a generált szöveg minőségét.
- Használtuk a `frequencyPenalty` és `presencePenalty`-t az ismétlődés csökkentésére és a változatosság ösztönzésére a kimenetben.
- Használtuk a `top_k`-t, hogy a modellt a legvalószínűbb K tokenre korlátozzuk, ami segíthet koherensebb válaszok generálásában.

---

## Determinisztikus sampling

Azoknál az alkalmazásoknál, ahol következetes kimenetekre van szükség, a determinisztikus sampling reprodukálható eredményeket biztosít. Ezt úgy éri el, hogy fix véletlenszám-generátor magot használ, és a hőmérsékletet nullára állítja.

Nézzük meg az alábbi mintapéldát, amely bemutatja a determinisztikus sampling megvalósítását különböző programozási nyelveken.

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

Az előző kódban:

- Létrehoztunk egy MCP klienst egy megadott szerver URL-lel.
- Két kérést konfiguráltunk ugyanazzal a prompttal, fix maggal és nulla hőmérséklettel.
- Mindkét kérést elküldtük, és kiírtuk a generált szöveget.
- Bemutattuk, hogy a válaszok azonosak a sampling konfiguráció determinisztikus jellege miatt (ugyanaz a mag és hőmérséklet).
- Használtuk a `setSeed`-et egy fix véletlenszám-generátor mag megadására, biztosítva, hogy a modell mindig ugyanazt a kimenetet generálja ugyanarra a bemenetre.
- A `temperature`-t nullára állítottuk a maximális determinisztikusság érdekében, vagyis a modell mindig a legvalószínűbb következő tokent választja véletlenszerűség nélkül.

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

Az előző kódban:

- Inicializáltunk egy MCP klienst szerver URL-lel.
- Két kérést konfiguráltunk ugyanazzal a prompttal, fix maggal és nulla hőmérséklettel.
- Mindkét kérést elküldtük, és kiírtuk a generált szöveget.
- Bemutattuk, hogy a válaszok azonosak a sampling konfiguráció determinisztikus jellege miatt (ugyanaz a mag és hőmérséklet).
- Használtuk a `seed`-et egy fix véletlenszám-generátor mag megadására, biztosítva, hogy a modell mindig ugyanazt a kimenetet generálja ugyanarra a bemenetre.
- A `temperature`-t nullára állítottuk a maximális determinisztikusság érdekében, vagyis a modell mindig a legvalószínűbb következő tokent választja véletlenszerűség nélkül.
- Egy másik magot használtunk a harmadik kéréshez, hogy megmutassuk, a mag megváltoztatása eltérő kimeneteket eredményez ugyanazzal a prompttal és hőmérséklettel.

---

## Dinamikus sampling konfiguráció

Az intelligens sampling a kontextus és a kérés követelményei alapján állítja be a paramétereket. Ez azt jelenti, hogy dinamikusan módosítja a `temperature`, `top_p` és büntetéseket a feladat típusa, a felhasználói preferenciák vagy a korábbi teljesítmény alapján.

Nézzük meg, hogyan valósítható meg a dinamikus sampling különböző programozási nyelveken.

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

Az előző kódban:

- Létrehoztunk egy `DynamicSamplingService` osztályt, amely az adaptív samplinget kezeli.
- Meghatároztunk sampling előbeállításokat különböző feladattípusokra (kreatív, tényalapú, kód, elemző).
- Kiválasztottuk az alap sampling előbeállítást a feladattípus alapján.
- Módosítottuk a sampling paramétereket a felhasználói preferenciák, például kreativitás és változatosság alapján.
- Elküldtük a kérést a dinamikusan konfigurált sampling paraméterekkel.
- Visszaadtuk a generált szöveget a használt sampling paraméterekkel és a feladattípussal a transzparencia érdekében.
- Használtuk a `temperature`-t a kimenet véletlenszerűségének szabályozására, ahol a magasabb értékek kreatívabb válaszokat eredményeznek.
- Használtuk a `top_p`-t, hogy korlátozzuk a tokenek kiválasztását a legmagasabb kumulatív valószínűséget képviselő tokenekre, javítva a generált szöveg minőségét.
- Használtuk a `frequency_penalty`-t az ismétlődés csökkentésére és a változatosság ösztönzésére a kimenetben.
- Használtuk a `user_preferences`-t, hogy lehetővé tegyük a sampling paraméterek testreszabását a felhasználó által meghatározott kreativitás és változatosság szint alapján.
- Használtuk a `task_type`-ot, hogy meghatározzuk a kéréshez megfelelő sampling stratégiát, lehetővé téve a feladat jellegének megfelelőbb válaszokat.
- A `send_request` metódussal elküldtük a promptot a konfigurált sampling paraméterekkel, biztosítva, hogy a modell a megadott követelmények szerint generáljon szöveget.
- A `generated_text` segítségével lekértük a modell válaszát, amelyet a sampling paraméterekkel és a feladattípussal együtt visszaadtunk további elemzés vagy megjelenítés céljából.
- A `min` és `max` függvényekkel biztosítottuk, hogy a felhasználói preferenciák érvényes tartományban maradjanak, megakadályozva a hibás sampling konfigurációkat.

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

Az előző kódban:

- Létrehoztunk egy `AdaptiveSamplingManager` osztályt, amely dinamikusan kezeli a samplinget a feladattípus és a felhasználói preferenciák alapján.
- Meghatároztunk sampling profilokat különböző feladattípusokra (kreatív, tényalapú, kód, beszélgetés).
- Megvalósítottunk egy metódust a feladattípus felismerésére a prompt alapján egyszerű heurisztikák segítségével.
- Kiszámoltuk a sampling paramétereket a feladattípus és a felhasználói preferenciák alapján.
- Alkalmaztuk a tanult módosításokat a korábbi teljesítmény alapján a sampling paraméterek optimalizálására.
- Rögzítettük a teljes

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.