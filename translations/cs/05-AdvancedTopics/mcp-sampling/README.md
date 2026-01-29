# Sampling v Model Context Protocolu

Sampling je výkonná funkce MCP, která umožňuje serverům požadovat dokončení od LLM přes klienta, čímž umožňuje sofistikované agentní chování při zachování bezpečnosti a soukromí. Správná konfigurace sampling výrazně zlepší kvalitu odpovědí a výkon. MCP poskytuje standardizovaný způsob, jak řídit generování textu modelem pomocí specifických parametrů ovlivňujících náhodnost, kreativitu a soudržnost.

## Úvod

V této lekci si ukážeme, jak nastavit parametry sampling v požadavcích MCP a pochopíme základní principy protokolu sampling.

## Cíle učení

Na konci této lekce budete umět:

- Porozumět klíčovým parametrům sampling dostupným v MCP.
- Nastavit parametry sampling pro různé scénáře použití.
- Implementovat deterministický sampling pro reprodukovatelné výsledky.
- Dynamicky upravovat parametry sampling podle kontextu a preferencí uživatele.
- Použít strategie sampling ke zlepšení výkonu modelu v různých situacích.
- Pochopit, jak sampling funguje v klient-server toku MCP.

## Jak sampling funguje v MCP

Sampling v MCP probíhá podle těchto kroků:

1. Server pošle klientovi požadavek `sampling/createMessage`
2. Klient požadavek zkontroluje a může jej upravit
3. Klient provede sampling z LLM
4. Klient zkontroluje dokončení
5. Klient vrátí výsledek serveru

Tento design s člověkem v procesu zajišťuje, že uživatelé mají kontrolu nad tím, co LLM vidí a generuje.

## Přehled parametrů sampling

MCP definuje následující parametry sampling, které lze nastavit v požadavcích klienta:

| Parametr | Popis | Typický rozsah |
|----------|--------|----------------|
| `temperature` | Řídí náhodnost výběru tokenů | 0.0 - 1.0 |
| `maxTokens` | Maximální počet generovaných tokenů | Celé číslo |
| `stopSequences` | Vlastní sekvence, které zastaví generování při jejich výskytu | Pole řetězců |
| `metadata` | Další parametry specifické pro poskytovatele | JSON objekt |

Mnoho poskytovatelů LLM podporuje další parametry přes pole `metadata`, které mohou zahrnovat:

| Běžný rozšiřující parametr | Popis | Typický rozsah |
|----------------------------|--------|----------------|
| `top_p` | Nucleus sampling - omezuje tokeny na nejvyšší kumulativní pravděpodobnost | 0.0 - 1.0 |
| `top_k` | Omezuje výběr tokenů na top K možností | 1 - 100 |
| `presence_penalty` | Penalizuje tokeny podle jejich přítomnosti v textu | -2.0 - 2.0 |
| `frequency_penalty` | Penalizuje tokeny podle jejich četnosti v textu | -2.0 - 2.0 |
| `seed` | Specifické náhodné semeno pro reprodukovatelné výsledky | Celé číslo |

## Příklad formátu požadavku

Zde je příklad požadavku na sampling od klienta v MCP:

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

## Formát odpovědi

Klient vrací výsledek dokončení:

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

## Kontrola člověkem v procesu

Sampling v MCP je navržen s ohledem na lidský dohled:

- **U promptů**:
  - Klienti by měli uživatelům zobrazit navržený prompt
  - Uživatelé by měli mít možnost prompt upravit nebo odmítnout
  - Systémové prompty lze filtrovat nebo upravovat
  - Zařazení kontextu řídí klient

- **U dokončení**:
  - Klienti by měli uživatelům zobrazit dokončení
  - Uživatelé by měli mít možnost dokončení upravit nebo odmítnout
  - Klienti mohou dokončení filtrovat nebo upravovat
  - Uživatelé mají kontrolu nad tím, který model se použije

S těmito principy si nyní ukážeme, jak sampling implementovat v různých programovacích jazycích, se zaměřením na parametry běžně podporované napříč poskytovateli LLM.

## Bezpečnostní aspekty

Při implementaci sampling v MCP zvažte tyto bezpečnostní zásady:

- **Validujte veškerý obsah zpráv** před odesláním klientovi
- **Sanitizujte citlivé informace** z promptů a dokončení
- **Implementujte limity rychlosti** pro prevenci zneužití
- **Sledujte využití sampling** kvůli neobvyklým vzorcům
- **Šifrujte data při přenosu** pomocí bezpečných protokolů
- **Zacházejte s uživatelskými daty** v souladu s příslušnými předpisy
- **Auditujte požadavky na sampling** pro dodržování pravidel a bezpečnost
- **Řiďte náklady** pomocí vhodných limitů
- **Implementujte timeouty** pro požadavky sampling
- **Zvládejte chyby modelu** s vhodnými záložními mechanismy

Parametry sampling umožňují jemné doladění chování jazykových modelů tak, aby bylo dosaženo požadované rovnováhy mezi deterministickými a kreativními výstupy.

Podívejme se, jak tyto parametry nastavit v různých programovacích jazycích.

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

V předchozím kódu jsme:

- Vytvořili MCP klienta s konkrétní URL serveru.
- Nakonfigurovali požadavek s parametry sampling jako `temperature`, `top_p` a `top_k`.
- Odeslali požadavek a vypsali generovaný text.
- Použili:
    - `allowedTools` k určení, které nástroje může model během generování používat. V tomto případě jsme povolili nástroje `ideaGenerator` a `marketAnalyzer` pro pomoc při generování kreativních nápadů na aplikace.
    - `frequencyPenalty` a `presencePenalty` k omezení opakování a podpoře rozmanitosti výstupu.
    - `temperature` k řízení náhodnosti výstupu, kde vyšší hodnoty vedou k kreativnějším odpovědím.
    - `top_p` k omezení výběru tokenů na ty, které přispívají k nejvyšší kumulativní pravděpodobnosti, což zlepšuje kvalitu generovaného textu.
    - `top_k` k omezení modelu na top K nejpravděpodobnějších tokenů, což pomáhá generovat soudržnější odpovědi.
    - `frequencyPenalty` a `presencePenalty` k redukci opakování a podpoře rozmanitosti v generovaném textu.

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

V předchozím kódu jsme:

- Inicializovali MCP klienta s URL serveru a API klíčem.
- Nakonfigurovali dvě sady parametrů sampling: jednu pro kreativní úkoly a druhou pro faktické úkoly.
- Odeslali požadavky s těmito konfiguracemi, přičemž modelu jsme umožnili používat specifické nástroje pro každý úkol.
- Vypsali generované odpovědi, abychom ukázali vliv různých parametrů sampling.
- Použili `allowedTools` k určení, které nástroje může model během generování používat. V tomto případě jsme povolili `ideaGenerator` a `environmentalImpactTool` pro kreativní úkoly a `factChecker` a `dataAnalysisTool` pro faktické úkoly.
- Použili `temperature` k řízení náhodnosti výstupu, kde vyšší hodnoty vedou k kreativnějším odpovědím.
- Použili `top_p` k omezení výběru tokenů na ty, které přispívají k nejvyšší kumulativní pravděpodobnosti, což zlepšuje kvalitu generovaného textu.
- Použili `frequencyPenalty` a `presencePenalty` k redukci opakování a podpoře rozmanitosti ve výstupu.
- Použili `top_k` k omezení modelu na top K nejpravděpodobnějších tokenů, což pomáhá generovat soudržnější odpovědi.

---

## Deterministický sampling

Pro aplikace vyžadující konzistentní výstupy zajišťuje deterministický sampling reprodukovatelné výsledky. Dosahuje se to použitím pevného náhodného semene a nastavením teploty na nulu.

Níže je ukázková implementace deterministického sampling v různých programovacích jazycích.

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

V předchozím kódu jsme:

- Vytvořili MCP klienta s určenou URL serveru.
- Nakonfigurovali dva požadavky se stejným promptem, pevným seedem a nulovou teplotou.
- Odeslali oba požadavky a vypsali generovaný text.
- Ukázali, že odpovědi jsou identické díky deterministické povaze konfigurace sampling (stejné seed a teplota).
- Použili `setSeed` k určení pevného náhodného semene, což zajišťuje, že model vždy generuje stejný výstup pro stejný vstup.
- Nastavili `temperature` na nulu pro maximální determinismus, což znamená, že model vždy vybere nejpravděpodobnější následující token bez náhodnosti.

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

V předchozím kódu jsme:

- Inicializovali MCP klienta s URL serveru.
- Nakonfigurovali dva požadavky se stejným promptem, pevným seedem a nulovou teplotou.
- Odeslali oba požadavky a vypsali generovaný text.
- Ukázali, že odpovědi jsou identické díky deterministické povaze konfigurace sampling (stejné seed a teplota).
- Použili `seed` k určení pevného náhodného semene, což zajišťuje, že model vždy generuje stejný výstup pro stejný vstup.
- Nastavili `temperature` na nulu pro maximální determinismus, což znamená, že model vždy vybere nejpravděpodobnější následující token bez náhodnosti.
- Použili jiné seed pro třetí požadavek, abychom ukázali, že změna semene vede k odlišným výstupům, i když prompt a teplota zůstávají stejné.

---

## Dynamická konfigurace sampling

Inteligentní sampling přizpůsobuje parametry podle kontextu a požadavků každého požadavku. To znamená dynamickou úpravu parametrů jako temperature, top_p a penalizací na základě typu úkolu, uživatelských preferencí nebo historického výkonu.

Podívejme se, jak implementovat dynamický sampling v různých programovacích jazycích.

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

V předchozím kódu jsme:

- Vytvořili třídu `DynamicSamplingService`, která spravuje adaptivní sampling.
- Definovali přednastavené parametry sampling pro různé typy úkolů (kreativní, faktické, kód, analytické).
- Vybrali základní přednastavení sampling podle typu úkolu.
- Upravil parametry sampling na základě uživatelských preferencí, jako je úroveň kreativity a rozmanitosti.
- Odeslali požadavek s dynamicky nakonfigurovanými parametry sampling.
- Vrátili generovaný text spolu s použitými parametry sampling a typem úkolu pro přehlednost.
- Použili `temperature` k řízení náhodnosti výstupu, kde vyšší hodnoty vedou k kreativnějším odpovědím.
- Použili `top_p` k omezení výběru tokenů na ty, které přispívají k nejvyšší kumulativní pravděpodobnosti, což zlepšuje kvalitu generovaného textu.
- Použili `frequency_penalty` k redukci opakování a podpoře rozmanitosti ve výstupu.
- Použili `user_preferences` k umožnění přizpůsobení parametrů sampling na základě uživatelsky definované úrovně kreativity a rozmanitosti.
- Použili `task_type` k určení vhodné strategie sampling pro požadavek, což umožňuje lépe přizpůsobené odpovědi podle povahy úkolu.
- Použili metodu `send_request` k odeslání promptu s nakonfigurovanými parametry sampling, čímž zajistili, že model generuje text podle specifikovaných požadavků.
- Použili `generated_text` k získání odpovědi modelu, která je následně vrácena spolu s parametry sampling a typem úkolu pro další analýzu nebo zobrazení.
- Použili funkce `min` a `max` k zajištění, že uživatelské preference jsou omezeny na platné rozsahy, čímž se zabrání neplatným konfiguracím sampling.

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

V předchozím kódu jsme:

- Vytvořili třídu `AdaptiveSamplingManager`, která spravuje dynamický sampling na základě typu úkolu a uživatelských preferencí.
- Definovali profily sampling pro různé typy úkolů (kreativní, faktické, kód, konverzační).
- Implementovali metodu pro detekci typu úkolu z promptu pomocí jednoduchých heuristik.
- Vypočítali parametry sampling na základě detekovaného typu úkolu a uživatelských preferencí.
- Aplikovali naučené úpravy na základě historického výkonu pro optimalizaci parametrů sampling.
- Zaznamenali výkon pro budoucí úpravy, což umožňuje systému učit se z minulých interakcí.
- Odeslali požadavky s dynamicky nakonfigurovanými parametry sampling a vrátili generovaný text spolu s použitými parametry a detekovaným typem úkolu.
- Použili:
    - `userPreferences` k umožnění přizpůsobení parametrů sampling na základě uživatelsky definované úrovně kreativity, přesnosti a konzistence.
    - `detectTaskType` k určení povahy úkolu na základě promptu, což umožňuje lépe přizpůsobené odpovědi.
    - `recordPerformance` k zaznamenání výkonu generovaných odpovědí, což umožňuje systému adaptovat se a zlepšovat v čase.
    - `applyLearnedAdjustments` k úpravě parametrů sampling na základě historického výkonu, čímž se zvyšuje schopnost modelu generovat kvalitní odpovědi.
    - `generateResponse` k zapouzdření celého procesu generování odpovědi s adaptivním samplingem, což usnadňuje volání s různými prompty a kontexty.
    - `allowedTools` k určení, které nástroje může model během generování používat, což umožňuje kontextově uvědomělé odpovědi.
    - `feedbackScore` k umožnění uživatelům poskytovat zpětnou vazbu na kvalitu generované odpovědi, která může být použita k dalšímu vylepšení výkonu modelu.
    - `performanceHistory` k udržování záznamu minulých interakcí, což umožňuje systému učit se z předchozích úspěchů a neúspěchů.
    - `getSamplingParameters` k dynamickému přizpůsobení parametrů sampling na základě kontextu požadavku, což umožňuje flexibilnější a citlivější chování modelu.
    - `detectTaskType` k zařazení úkolu na základě promptu, což umožňuje aplikovat vhodné strategie sampling pro různé typy požadavků.
    - `samplingProfiles` k definování základních konfigurací sampling pro různé typy úkolů, což umožňuje rychlé úpravy podle povahy požadavku.

---

## Co dál

- [5.7 Scaling](../mcp-scaling/README.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.