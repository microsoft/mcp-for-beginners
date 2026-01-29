# Sampling v protokolu Model Context Protocol

Sampling je zmogljiva funkcija MCP, ki strežnikom omogoča, da prek odjemalca zahtevajo dokončanja LLM, kar omogoča napredna agentna vedenja ob ohranjanju varnosti in zasebnosti. Pravilna konfiguracija samplinga lahko bistveno izboljša kakovost in zmogljivost odgovorov. MCP zagotavlja standardiziran način nadzora, kako modeli generirajo besedilo z določenimi parametri, ki vplivajo na naključnost, ustvarjalnost in koherenco.

## Uvod

V tej lekciji bomo raziskali, kako nastaviti parametre samplinga v MCP zahtevkih in razumeli osnovno mehaniko protokola samplinga.

## Cilji učenja

Na koncu te lekcije boste znali:

- Razumeti ključne parametre samplinga, ki so na voljo v MCP.
- Nastaviti parametre samplinga za različne primere uporabe.
- Izvesti deterministični sampling za ponovljive rezultate.
- Dinamično prilagajati parametre samplinga glede na kontekst in uporabniške preference.
- Uporabiti strategije samplinga za izboljšanje zmogljivosti modela v različnih scenarijih.
- Razumeti, kako sampling deluje v poteku klient-strežnik MCP.

## Kako sampling deluje v MCP

Potek samplinga v MCP sledi tem korakom:

1. Strežnik pošlje `sampling/createMessage` zahtevek odjemalcu
2. Odjemalec pregleda zahtevek in ga lahko spremeni
3. Odjemalec izvede sampling iz LLM
4. Odjemalec pregleda dokončanje
5. Odjemalec vrne rezultat strežniku

Ta zasnova s človekom v zanki zagotavlja, da uporabniki ohranjajo nadzor nad tem, kaj LLM vidi in generira.

## Pregled parametrov samplinga

MCP definira naslednje parametre samplinga, ki jih je mogoče nastaviti v odjemalskih zahtevkih:

| Parameter | Opis | Tipični razpon |
|-----------|-------|----------------|
| `temperature` | Nadzoruje naključnost pri izbiri tokenov | 0.0 - 1.0 |
| `maxTokens` | Največje število tokenov za generiranje | Celo število |
| `stopSequences` | Lastne sekvence, ki ustavijo generiranje, ko so zaznane | Polje nizov |
| `metadata` | Dodatni parametri specifični za ponudnika | JSON objekt |

Veliko ponudnikov LLM podpira dodatne parametre preko polja `metadata`, ki lahko vključujejo:

| Pogost razširitveni parameter | Opis | Tipični razpon |
|-------------------------------|-------|----------------|
| `top_p` | Nucleus sampling - omeji tokene na vrh kumulativne verjetnosti | 0.0 - 1.0 |
| `top_k` | Omeji izbiro tokenov na top K možnosti | 1 - 100 |
| `presence_penalty` | Kaznuje tokene glede na njihovo prisotnost v besedilu do zdaj | -2.0 - 2.0 |
| `frequency_penalty` | Kaznuje tokene glede na njihovo frekvenco v besedilu do zdaj | -2.0 - 2.0 |
| `seed` | Specifično naključno seme za ponovljive rezultate | Celo število |

## Primer formata zahtevka

Tukaj je primer zahtevka za sampling od odjemalca v MCP:

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

## Format odgovora

Odjemalec vrne rezultat dokončanja:

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

## Nadzor s človekom v zanki

Sampling v MCP je zasnovan z mislijo na človeški nadzor:

- **Za pozive (prompts)**:
  - Odjemalci naj uporabnikom prikažejo predlagani poziv
  - Uporabniki naj lahko spremenijo ali zavrnejo pozive
  - Sistemske pozive je mogoče filtrirati ali spremeniti
  - Vključevanje konteksta nadzoruje odjemalec

- **Za dokončanja (completions)**:
  - Odjemalci naj uporabnikom prikažejo dokončanje
  - Uporabniki naj lahko spremenijo ali zavrnejo dokončanja
  - Odjemalci lahko filtrirajo ali spreminjajo dokončanja
  - Uporabniki nadzorujejo, kateri model se uporablja

S temi načeli v mislih si poglejmo, kako implementirati sampling v različnih programskih jezikih, s poudarkom na parametrih, ki jih običajno podpirajo ponudniki LLM.

## Varnostni vidiki

Pri implementaciji samplinga v MCP upoštevajte naslednje varnostne prakse:

- **Preverite vsebino sporočil** pred pošiljanjem odjemalcu
- **Očistite občutljive informacije** iz pozivov in dokončanj
- **Uvedite omejitve hitrosti** za preprečevanje zlorab
- **Nadzorujte uporabo samplinga** za nenavadne vzorce
- **Šifrirajte podatke med prenosom** z varnimi protokoli
- **Upoštevajte zasebnost uporabniških podatkov** v skladu z veljavnimi predpisi
- **Revizirajte zahtevke samplinga** za skladnost in varnost
- **Nadzorujte stroške** z ustreznimi omejitvami
- **Uvedite časovne omejitve** za zahtevke samplinga
- **Obravnavajte napake modela** na eleganten način z ustreznimi rezervnimi rešitvami

Parametri samplinga omogočajo natančno prilagajanje vedenja jezikovnih modelov za dosego želene ravnotežja med determinističnimi in ustvarjalnimi izhodi.

Poglejmo, kako nastaviti te parametre v različnih programskih jezikih.

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

V zgornji kodi smo:

- Ustvarili MCP odjemalca z določenim URL strežnika.
- Nastavili zahtevek s parametri samplinga, kot so `temperature`, `top_p` in `top_k`.
- Poslali zahtevek in izpisali generirano besedilo.
- Uporabili:
    - `allowedTools` za določitev orodij, ki jih model lahko uporablja med generiranjem. V tem primeru smo dovolili orodji `ideaGenerator` in `marketAnalyzer`, da pomagata pri ustvarjanju kreativnih idej za aplikacije.
    - `frequencyPenalty` in `presencePenalty` za nadzor ponavljanja in raznolikosti v izhodu.
    - `temperature` za nadzor naključnosti izhoda, kjer višje vrednosti vodijo do bolj ustvarjalnih odgovorov.
    - `top_p` za omejitev izbire tokenov na tiste, ki prispevajo k vrhu kumulativne verjetnostne mase, kar izboljša kakovost generiranega besedila.
    - `top_k` za omejitev modela na top K najbolj verjetnih tokenov, kar lahko pomaga pri generiranju bolj koherentnih odgovorov.
    - `frequencyPenalty` in `presencePenalty` za zmanjšanje ponavljanja in spodbujanje raznolikosti v generiranem besedilu.

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

V zgornji kodi smo:

- Inicializirali MCP odjemalca z URL strežnika in API ključem.
- Nastavili dva nabora parametrov samplinga: enega za ustvarjalne naloge in drugega za dejanske naloge.
- Poslali zahtevke s temi nastavitvami, pri čemer smo modelu dovolili uporabo določenih orodij za vsako nalogo.
- Izpisali generirane odgovore, da pokažemo učinke različnih parametrov samplinga.
- Uporabili `allowedTools` za določitev orodij, ki jih model lahko uporablja med generiranjem. V tem primeru smo za ustvarjalne naloge dovolili `ideaGenerator` in `environmentalImpactTool`, za dejanske naloge pa `factChecker` in `dataAnalysisTool`.
- Uporabili `temperature` za nadzor naključnosti izhoda, kjer višje vrednosti vodijo do bolj ustvarjalnih odgovorov.
- Uporabili `top_p` za omejitev izbire tokenov na tiste, ki prispevajo k vrhu kumulativne verjetnostne mase, kar izboljša kakovost generiranega besedila.
- Uporabili `frequencyPenalty` in `presencePenalty` za zmanjšanje ponavljanja in spodbujanje raznolikosti v izhodu.
- Uporabili `top_k` za omejitev modela na top K najbolj verjetnih tokenov, kar lahko pomaga pri generiranju bolj koherentnih odgovorov.

---

## Deterministični sampling

Za aplikacije, ki zahtevajo dosledne izhode, deterministični sampling zagotavlja ponovljive rezultate. To doseže z uporabo fiksnega naključnega semena in nastavitvijo temperature na nič.

Poglejmo spodnji primer implementacije, ki prikazuje deterministični sampling v različnih programskih jezikih.

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

V zgornji kodi smo:

- Ustvarili MCP odjemalca z določenim URL strežnika.
- Nastavili dva zahtevka z istim pozivom, fiksnim semenom in temperaturo nič.
- Poslali oba zahtevka in izpisali generirano besedilo.
- Pokazali, da so odgovori enaki zaradi deterministične narave konfiguracije samplinga (isto seme in temperatura).
- Uporabili `setSeed` za določitev fiksnega naključnega semena, kar zagotavlja, da model vedno generira isti izhod za isti vhod.
- Nastavili `temperature` na nič, da zagotovimo maksimalno determinističnost, kar pomeni, da bo model vedno izbral najbolj verjeten naslednji token brez naključnosti.

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

V zgornji kodi smo:

- Inicializirali MCP odjemalca z URL strežnika.
- Nastavili dva zahtevka z istim pozivom, fiksnim semenom in temperaturo nič.
- Poslali oba zahtevka in izpisali generirano besedilo.
- Pokazali, da so odgovori enaki zaradi deterministične narave konfiguracije samplinga (isto seme in temperatura).
- Uporabili `seed` za določitev fiksnega naključnega semena, kar zagotavlja, da model vedno generira isti izhod za isti vhod.
- Nastavili `temperature` na nič, da zagotovimo maksimalno determinističnost, kar pomeni, da bo model vedno izbral najbolj verjeten naslednji token brez naključnosti.
- Za tretji zahtevek uporabili drugačno seme, da pokažemo, da sprememba semena povzroči različne izhode, tudi z istim pozivom in temperaturo.

---

## Dinamična konfiguracija samplinga

Pameten sampling prilagaja parametre glede na kontekst in zahteve posameznega zahtevka. To pomeni dinamično prilagajanje parametrov, kot so temperature, top_p in kazni, glede na vrsto naloge, uporabniške preference ali zgodovinsko zmogljivost.

Poglejmo, kako implementirati dinamični sampling v različnih programskih jezikih.

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

V zgornji kodi smo:

- Ustvarili razred `DynamicSamplingService`, ki upravlja prilagodljiv sampling.
- Določili prednastavitve samplinga za različne vrste nalog (ustvarjalne, dejanske, kodne, analitične).
- Izbrali osnovno prednastavitev samplinga glede na vrsto naloge.
- Prilagodili parametre samplinga glede na uporabniške preference, kot sta raven ustvarjalnosti in raznolikosti.
- Poslali zahtevek z dinamično konfiguriranimi parametri samplinga.
- Vrnil generirano besedilo skupaj z uporabljenimi parametri samplinga in vrsto naloge za preglednost.
- Uporabili `temperature` za nadzor naključnosti izhoda, kjer višje vrednosti vodijo do bolj ustvarjalnih odgovorov.
- Uporabili `top_p` za omejitev izbire tokenov na tiste, ki prispevajo k vrhu kumulativne verjetnostne mase, kar izboljša kakovost generiranega besedila.
- Uporabili `frequency_penalty` za zmanjšanje ponavljanja in spodbujanje raznolikosti v izhodu.
- Uporabili `user_preferences` za prilagoditev parametrov samplinga glede na uporabniško določene ravni ustvarjalnosti in raznolikosti.
- Uporabili `task_type` za določitev ustrezne strategije samplinga za zahtevek, kar omogoča bolj prilagojene odgovore glede na naravo naloge.
- Uporabili metodo `send_request` za pošiljanje poziva z nastavitvijo parametrov samplinga, kar zagotavlja, da model generira besedilo v skladu z določenimi zahtevami.
- Uporabili `generated_text` za pridobitev odgovora modela, ki se nato vrne skupaj s parametri samplinga in vrsto naloge za nadaljnjo analizo ali prikaz.
- Uporabili funkciji `min` in `max`, da zagotovimo, da so uporabniške preference omejene na veljavne vrednosti, s čimer preprečimo neveljavne konfiguracije samplinga.

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

V zgornji kodi smo:

- Ustvarili razred `AdaptiveSamplingManager`, ki upravlja dinamični sampling glede na vrsto naloge in uporabniške preference.
- Določili profile samplinga za različne vrste nalog (ustvarjalne, dejanske, kodne, pogovorne).
- Implementirali metodo za zaznavanje vrste naloge iz poziva z uporabo preprostih pravil.
- Izračunali parametre samplinga glede na zaznano vrsto naloge in uporabniške preference.
- Uporabili naučene prilagoditve na podlagi zgodovinske zmogljivosti za optimizacijo parametrov samplinga.
- Beležili zmogljivost za prihodnje prilagoditve, kar omogoča sistemu učenje iz preteklih interakcij.
- Poslali zahtevke z dinamično konfiguriranimi parametri samplinga in vrnili generirano besedilo skupaj z uporabljenimi parametri in zaznano vrsto naloge.
- Uporabili:
    - `userPreferences` za prilagoditev parametrov samplinga glede na uporabniško določene ravni ustvarjalnosti, natančnosti in konsistentnosti.
    - `detectTaskType` za določitev narave naloge na podlagi poziva, kar omogoča bolj prilagojene odgovore.
    - `recordPerformance` za beleženje zmogljivosti generiranih odgovorov, kar omogoča sistemu prilagajanje in izboljševanje skozi čas.
    - `applyLearnedAdjustments` za spreminjanje parametrov samplinga na podlagi zgodovinske zmogljivosti, kar izboljšuje sposobnost modela za generiranje kakovostnih odgovorov.
    - `generateResponse` za zajem celotnega procesa generiranja odgovora z adaptivnim samplingom, kar omogoča enostavno klicanje z različnimi pozivi in konteksti.
    - `allowedTools` za določitev orodij, ki jih model lahko uporablja med generiranjem, kar omogoča bolj kontekstualno prilagojene odgovore.
    - `feedbackScore` za omogočanje uporabnikom, da podajo povratne informacije o kakovosti generiranega odgovora, kar se lahko uporabi za nadaljnje izboljšave zmogljivosti modela.
    - `performanceHistory` za vzdrževanje zapisa preteklih interakcij, kar omogoča sistemu učenje iz preteklih uspehov in neuspehov.
    - `getSamplingParameters` za dinamično prilagajanje parametrov samplinga glede na kontekst zahtevka, kar omogoča bolj prilagodljivo in odzivno vedenje modela.
    - `detectTaskType` za klasifikacijo naloge na podlagi poziva, kar omogoča sistemu uporabo ustreznih strategij samplinga za različne vrste zahtevkov.
    - `samplingProfiles` za določitev osnovnih konfiguracij samplinga za različne vrste nalog, kar omogoča hitro prilagajanje glede na naravo zahtevka.

---

## Kaj sledi

- [5.7 Scaling](../mcp-scaling/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.