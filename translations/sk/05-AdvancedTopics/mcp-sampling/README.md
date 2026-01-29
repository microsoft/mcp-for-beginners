# Sampling v protokole Model Context Protocol

Sampling je výkonná funkcia MCP, ktorá umožňuje serverom žiadať o dokončenia LLM prostredníctvom klienta, čím umožňuje sofistikované agentné správanie pri zachovaní bezpečnosti a súkromia. Správna konfigurácia samplingu môže výrazne zlepšiť kvalitu odpovedí a výkon. MCP poskytuje štandardizovaný spôsob, ako riadiť generovanie textu modelmi pomocou špecifických parametrov, ktoré ovplyvňujú náhodnosť, kreativitu a koherenciu.

## Úvod

V tejto lekcii preskúmame, ako nakonfigurovať sampling parametre v MCP požiadavkách a pochopíme základné mechanizmy protokolu samplingu.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Pochopiť kľúčové sampling parametre dostupné v MCP.
- Nakonfigurovať sampling parametre pre rôzne použitia.
- Implementovať deterministický sampling pre reprodukovateľné výsledky.
- Dynamicky upravovať sampling parametre na základe kontextu a preferencií používateľa.
- Použiť sampling stratégie na zlepšenie výkonu modelu v rôznych scenároch.
- Pochopiť, ako sampling funguje v klient-server toku MCP.

## Ako sampling funguje v MCP

Samplingový tok v MCP prebieha nasledovne:

1. Server pošle klientovi požiadavku `sampling/createMessage`
2. Klient požiadavku skontroluje a môže ju upraviť
3. Klient vykoná sampling z LLM
4. Klient skontroluje dokončenie
5. Klient vráti výsledok serveru

Tento dizajn s človekom v slučke zabezpečuje, že používatelia majú kontrolu nad tým, čo LLM vidí a generuje.

## Prehľad sampling parametrov

MCP definuje nasledujúce sampling parametre, ktoré je možné konfigurovať v požiadavkách klienta:

| Parameter | Popis | Typický rozsah |
|-----------|-------------|---------------|
| `temperature` | Riadi náhodnosť pri výbere tokenov | 0.0 - 1.0 |
| `maxTokens` | Maximálny počet tokenov na generovanie | Celé číslo |
| `stopSequences` | Vlastné sekvencie, ktoré zastavia generovanie pri ich výskyte | Pole reťazcov |
| `metadata` | Ďalšie parametre špecifické pre poskytovateľa | JSON objekt |

Mnoho poskytovateľov LLM podporuje ďalšie parametre cez pole `metadata`, ktoré môžu obsahovať:

| Bežný rozšírený parameter | Popis | Typický rozsah |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - obmedzuje tokeny na najvyššiu kumulatívnu pravdepodobnosť | 0.0 - 1.0 |
| `top_k` | Obmedzuje výber tokenov na top K možností | 1 - 100 |
| `presence_penalty` | Penalizuje tokeny na základe ich prítomnosti v texte doteraz | -2.0 - 2.0 |
| `frequency_penalty` | Penalizuje tokeny na základe ich frekvencie v texte doteraz | -2.0 - 2.0 |
| `seed` | Špecifické náhodné semeno pre reprodukovateľné výsledky | Celé číslo |

## Príklad formátu požiadavky

Tu je príklad požiadavky na sampling od klienta v MCP:

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

## Formát odpovede

Klient vráti výsledok dokončenia:

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

## Ovládanie človekom v slučke

Sampling v MCP je navrhnutý s ohľadom na ľudský dohľad:

- **Pre prompt-y**:
  - Klienti by mali používateľom zobraziť navrhovaný prompt
  - Používatelia by mali mať možnosť prompt upraviť alebo odmietnuť
  - Systémové prompt-y môžu byť filtrované alebo upravované
  - Zahrnutie kontextu riadi klient

- **Pre dokončenia**:
  - Klienti by mali používateľom zobraziť dokončenie
  - Používatelia by mali mať možnosť dokončenie upraviť alebo odmietnuť
  - Klienti môžu filtrovať alebo upravovať dokončenia
  - Používatelia kontrolujú, ktorý model sa použije

S týmito princípmi na pamäti sa pozrime, ako implementovať sampling v rôznych programovacích jazykoch, so zameraním na parametre, ktoré sú bežne podporované naprieč poskytovateľmi LLM.

## Bezpečnostné úvahy

Pri implementácii samplingu v MCP zvážte tieto bezpečnostné odporúčania:

- **Overte celý obsah správy** pred jej odoslaním klientovi
- **Sanitizujte citlivé informácie** z promptov a dokončení
- **Implementujte limity rýchlosti** na zabránenie zneužitia
- **Monitorujte používanie samplingu** pre nezvyčajné vzory
- **Šifrujte dáta počas prenosu** pomocou bezpečných protokolov
- **Zaobchádzajte s ochranou osobných údajov používateľov** podľa príslušných predpisov
- **Auditujte sampling požiadavky** pre súlad a bezpečnosť
- **Kontrolujte náklady** pomocou vhodných limitov
- **Implementujte timeouty** pre sampling požiadavky
- **Zvládajte chyby modelu** s vhodnými záložnými mechanizmami

Sampling parametre umožňujú jemné doladenie správania jazykových modelov na dosiahnutie požadovanej rovnováhy medzi deterministickými a kreatívnymi výstupmi.

Pozrime sa, ako nakonfigurovať tieto parametre v rôznych programovacích jazykoch.

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

V predchádzajúcom kóde sme:

- Vytvorili MCP klienta so špecifickou URL servera.
- Nakonfigurovali požiadavku so sampling parametrami ako `temperature`, `top_p` a `top_k`.
- Odoslali požiadavku a vytlačili vygenerovaný text.
- Použili:
    - `allowedTools` na špecifikovanie nástrojov, ktoré môže model počas generovania použiť. V tomto prípade sme povolili nástroje `ideaGenerator` a `marketAnalyzer` na pomoc pri generovaní kreatívnych nápadov na aplikácie.
    - `frequencyPenalty` a `presencePenalty` na kontrolu opakovania a rozmanitosti výstupu.
    - `temperature` na riadenie náhodnosti výstupu, kde vyššie hodnoty vedú k kreatívnejším odpovediam.
    - `top_p` na obmedzenie výberu tokenov na tie, ktoré prispievajú k najvyššej kumulatívnej pravdepodobnosti, čím sa zvyšuje kvalita generovaného textu.
    - `top_k` na obmedzenie modelu na top K najpravdepodobnejších tokenov, čo môže pomôcť pri generovaní koherentnejších odpovedí.
    - `frequencyPenalty` a `presencePenalty` na zníženie opakovania a podporu rozmanitosti v generovanom texte.

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

V predchádzajúcom kóde sme:

- Inicializovali MCP klienta s URL servera a API kľúčom.
- Nakonfigurovali dve sady sampling parametrov: jednu pre kreatívne úlohy a druhú pre faktické úlohy.
- Odoslali požiadavky s týmito konfiguráciami, umožňujúc modelu používať špecifické nástroje pre každú úlohu.
- Vytlačili vygenerované odpovede na demonštráciu efektov rôznych sampling parametrov.
- Použili `allowedTools` na špecifikovanie nástrojov, ktoré môže model počas generovania použiť. V tomto prípade sme povolili `ideaGenerator` a `environmentalImpactTool` pre kreatívne úlohy a `factChecker` a `dataAnalysisTool` pre faktické úlohy.
- Použili `temperature` na riadenie náhodnosti výstupu, kde vyššie hodnoty vedú k kreatívnejším odpovediam.
- Použili `top_p` na obmedzenie výberu tokenov na tie, ktoré prispievajú k najvyššej kumulatívnej pravdepodobnosti, čím sa zvyšuje kvalita generovaného textu.
- Použili `frequencyPenalty` a `presencePenalty` na zníženie opakovania a podporu rozmanitosti vo výstupe.
- Použili `top_k` na obmedzenie modelu na top K najpravdepodobnejších tokenov, čo môže pomôcť pri generovaní koherentnejších odpovedí.

---

## Deterministický sampling

Pre aplikácie vyžadujúce konzistentné výstupy zabezpečuje deterministický sampling reprodukovateľné výsledky. Dosahuje sa to použitím pevného náhodného semena a nastavením teploty na nulu.

Pozrime sa na ukážkovú implementáciu deterministického samplingu v rôznych programovacích jazykoch.

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

V predchádzajúcom kóde sme:

- Vytvorili MCP klienta so špecifikovanou URL servera.
- Nakonfigurovali dve požiadavky s rovnakým promptom, pevným seedom a nulovou teplotou.
- Odoslali obe požiadavky a vytlačili vygenerovaný text.
- Ukázali, že odpovede sú identické vďaka deterministickej povahe sampling konfigurácie (rovnaký seed a teplota).
- Použili `setSeed` na špecifikovanie pevného náhodného semena, čím sa zabezpečí, že model vždy vygeneruje rovnaký výstup pre rovnaký vstup.
- Nastavili `temperature` na nulu, aby sa zabezpečila maximálna deterministickosť, teda model vždy vyberie najpravdepodobnejší nasledujúci token bez náhodnosti.

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

V predchádzajúcom kóde sme:

- Inicializovali MCP klienta s URL servera.
- Nakonfigurovali dve požiadavky s rovnakým promptom, pevným seedom a nulovou teplotou.
- Odoslali obe požiadavky a vytlačili vygenerovaný text.
- Ukázali, že odpovede sú identické vďaka deterministickej povahe sampling konfigurácie (rovnaký seed a teplota).
- Použili `seed` na špecifikovanie pevného náhodného semena, čím sa zabezpečí, že model vždy vygeneruje rovnaký výstup pre rovnaký vstup.
- Nastavili `temperature` na nulu, aby sa zabezpečila maximálna deterministickosť, teda model vždy vyberie najpravdepodobnejší nasledujúci token bez náhodnosti.
- Použili iné semeno pre tretiu požiadavku, aby sme ukázali, že zmena semena vedie k odlišným výstupom, aj keď prompt a teplota zostávajú rovnaké.

---

## Dynamická konfigurácia samplingu

Inteligentný sampling prispôsobuje parametre na základe kontextu a požiadaviek každej požiadavky. To znamená dynamickú úpravu parametrov ako temperature, top_p a penalizácie podľa typu úlohy, preferencií používateľa alebo historického výkonu.

Pozrime sa, ako implementovať dynamický sampling v rôznych programovacích jazykoch.

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

V predchádzajúcom kóde sme:

- Vytvorili triedu `DynamicSamplingService`, ktorá spravuje adaptívny sampling.
- Definovali sampling prednastavenia pre rôzne typy úloh (kreatívne, faktické, kód, analytické).
- Vybrali základné sampling prednastavenie podľa typu úlohy.
- Upravili sampling parametre na základe preferencií používateľa, ako je úroveň kreativity a rozmanitosti.
- Odoslali požiadavku s dynamicky nakonfigurovanými sampling parametrami.
- Vrátili vygenerovaný text spolu s použitými sampling parametrami a typom úlohy pre transparentnosť.
- Použili `temperature` na riadenie náhodnosti výstupu, kde vyššie hodnoty vedú k kreatívnejším odpovediam.
- Použili `top_p` na obmedzenie výberu tokenov na tie, ktoré prispievajú k najvyššej kumulatívnej pravdepodobnosti, čím sa zvyšuje kvalita generovaného textu.
- Použili `frequency_penalty` na zníženie opakovania a podporu rozmanitosti vo výstupe.
- Použili `user_preferences` na umožnenie prispôsobenia sampling parametrov na základe používateľom definovanej úrovne kreativity a rozmanitosti.
- Použili `task_type` na určenie vhodnej sampling stratégie pre požiadavku, čo umožňuje lepšie prispôsobené odpovede podľa povahy úlohy.
- Použili metódu `send_request` na odoslanie promptu s nakonfigurovanými sampling parametrami, čím sa zabezpečí, že model generuje text podľa špecifikovaných požiadaviek.
- Použili `generated_text` na získanie odpovede modelu, ktorá je následne vrátená spolu so sampling parametrami a typom úlohy na ďalšiu analýzu alebo zobrazenie.
- Použili funkcie `min` a `max` na zabezpečenie, že používateľské preferencie sú obmedzené v platných rozsahoch, čím sa zabráni neplatným sampling konfiguráciám.

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

V predchádzajúcom kóde sme:

- Vytvorili triedu `AdaptiveSamplingManager`, ktorá spravuje dynamický sampling na základe typu úlohy a preferencií používateľa.
- Definovali sampling profily pre rôzne typy úloh (kreatívne, faktické, kód, konverzačné).
- Implementovali metódu na detekciu typu úlohy z promptu pomocou jednoduchých heuristík.
- Vypočítali sampling parametre na základe detegovaného typu úlohy a preferencií používateľa.
- Aplikovali naučené úpravy na základe historického výkonu na optimalizáciu sampling parametrov.
- Zaznamenali výkon pre budúce úpravy, čo umožňuje systému učiť sa z minulých interakcií.
- Odoslali požiadavky s dynamicky nakonfigurovanými sampling parametrami a vrátili vygenerovaný text spolu s použitými parametrami a detegovaným typom úlohy.
- Použili:
    - `userPreferences` na umožnenie prispôsobenia sampling parametrov na základe používateľom definovaných úrovní kreativity, presnosti a konzistencie.
    - `detectTaskType` na určenie povahy úlohy podľa promptu, čo umožňuje lepšie prispôsobené odpovede.
    - `recordPerformance` na zaznamenávanie výkonu generovaných odpovedí, čo umožňuje systému adaptovať sa a zlepšovať v čase.
    - `applyLearnedAdjustments` na úpravu sampling parametrov na základe historického výkonu, čím sa zvyšuje schopnosť modelu generovať kvalitné odpovede.
    - `generateResponse` na zabalenie celého procesu generovania odpovede s adaptívnym samplingom, čo uľahčuje volanie s rôznymi promptmi a kontextmi.
    - `allowedTools` na špecifikovanie nástrojov, ktoré môže model počas generovania použiť, čo umožňuje kontextovo uvedomelejšie odpovede.
    - `feedbackScore` na umožnenie používateľom poskytovať spätnú väzbu o kvalite generovanej odpovede, ktorá môže byť použitá na ďalšie zlepšenie výkonu modelu v čase.
    - `performanceHistory` na udržiavanie záznamu minulých interakcií, čo umožňuje systému učiť sa z predchádzajúcich úspechov a neúspechov.
    - `getSamplingParameters` na dynamickú úpravu sampling parametrov na základe kontextu požiadavky, čo umožňuje flexibilnejšie a responzívnejšie správanie modelu.
    - `detectTaskType` na klasifikáciu úlohy podľa promptu, čo umožňuje systému aplikovať vhodné sampling stratégie pre rôzne typy požiadaviek.
    - `samplingProfiles` na definovanie základných sampling konfigurácií pre rôzne typy úloh, čo umožňuje rýchle úpravy podľa povahy požiadavky.

---

## Čo ďalej

- [5.7 Scaling](../mcp-scaling/README.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.