# Sampling in Model Context Protocol

Sampling is een krachtige MCP-functie waarmee servers LLM-completions via de client kunnen opvragen, wat geavanceerd agentgedrag mogelijk maakt terwijl veiligheid en privacy gewaarborgd blijven. De juiste samplingconfiguratie kan de kwaliteit en prestaties van reacties aanzienlijk verbeteren. MCP biedt een gestandaardiseerde manier om te bepalen hoe modellen tekst genereren met specifieke parameters die invloed hebben op willekeur, creativiteit en samenhang.

## Introductie

In deze les verkennen we hoe samplingparameters in MCP-verzoeken geconfigureerd kunnen worden en begrijpen we de onderliggende protocolmechanismen van sampling.

## Leerdoelen

Aan het einde van deze les kun je:

- De belangrijkste samplingparameters in MCP begrijpen.
- Samplingparameters configureren voor verschillende toepassingen.
- Deterministische sampling implementeren voor reproduceerbare resultaten.
- Samplingparameters dynamisch aanpassen op basis van context en gebruikersvoorkeuren.
- Samplingstrategieën toepassen om modelprestaties in diverse scenario’s te verbeteren.
- Begrijpen hoe sampling werkt in de client-serverstroom van MCP.

## Hoe Sampling Werkt in MCP

De samplingstroom in MCP verloopt als volgt:

1. Server stuurt een `sampling/createMessage` verzoek naar de client
2. Client bekijkt het verzoek en kan het aanpassen
3. Client voert sampling uit op een LLM
4. Client beoordeelt de completion
5. Client stuurt het resultaat terug naar de server

Dit ontwerp met menselijke tussenkomst zorgt ervoor dat gebruikers controle houden over wat de LLM ziet en genereert.

## Overzicht Samplingparameters

MCP definieert de volgende samplingparameters die in clientverzoeken kunnen worden ingesteld:

| Parameter | Beschrijving | Typisch bereik |
|-----------|--------------|----------------|
| `temperature` | Bepaalt de willekeur bij het selecteren van tokens | 0.0 - 1.0 |
| `maxTokens` | Maximaal aantal te genereren tokens | Geheel getal |
| `stopSequences` | Aangepaste reeksen die de generatie stoppen wanneer ze worden aangetroffen | Array van strings |
| `metadata` | Extra provider-specifieke parameters | JSON-object |

Veel LLM-providers ondersteunen extra parameters via het `metadata`-veld, waaronder:

| Veelvoorkomende Extensieparameter | Beschrijving | Typisch bereik |
|-----------|--------------|----------------|
| `top_p` | Nucleus sampling - beperkt tokens tot de top cumulatieve waarschijnlijkheid | 0.0 - 1.0 |
| `top_k` | Beperkt tokenselectie tot de top K opties | 1 - 100 |
| `presence_penalty` | Straf tokens op basis van hun aanwezigheid in de tekst tot nu toe | -2.0 - 2.0 |
| `frequency_penalty` | Straf tokens op basis van hun frequentie in de tekst tot nu toe | -2.0 - 2.0 |
| `seed` | Specifieke random seed voor reproduceerbare resultaten | Geheel getal |

## Voorbeeld Verzoekformaat

Hier is een voorbeeld van een samplingverzoek vanuit een client in MCP:

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

## Antwoordformaat

De client retourneert een completionresultaat:

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

## Menselijke Tussenkomst

MCP-sampling is ontworpen met menselijke controle in gedachten:

- **Voor prompts**:
  - Clients tonen de voorgestelde prompt aan gebruikers
  - Gebruikers kunnen prompts aanpassen of afwijzen
  - Systeem prompts kunnen worden gefilterd of aangepast
  - Contextinclusie wordt door de client geregeld

- **Voor completions**:
  - Clients tonen de completion aan gebruikers
  - Gebruikers kunnen completions aanpassen of afwijzen
  - Clients kunnen completions filteren of aanpassen
  - Gebruikers bepalen welk model wordt gebruikt

Met deze principes in gedachten bekijken we hoe sampling geïmplementeerd kan worden in verschillende programmeertalen, met focus op parameters die breed ondersteund worden door LLM-providers.

## Beveiligingsoverwegingen

Bij het implementeren van sampling in MCP, houd rekening met deze beveiligingsrichtlijnen:

- **Valideer alle berichtinhoud** voordat deze naar de client wordt gestuurd
- **Sanitize gevoelige informatie** uit prompts en completions
- **Implementeer rate limits** om misbruik te voorkomen
- **Monitor samplinggebruik** op ongebruikelijke patronen
- **Versleutel data tijdens overdracht** met veilige protocollen
- **Behandel gebruikersprivacy** volgens relevante regelgeving
- **Audit samplingverzoeken** voor compliance en veiligheid
- **Beperk kostenblootstelling** met passende limieten
- **Implementeer timeouts** voor samplingverzoeken
- **Ga netjes om met model fouten** met passende fallbackmechanismen

Samplingparameters maken het mogelijk het gedrag van taalmodellen fijn af te stemmen om de gewenste balans te vinden tussen deterministische en creatieve output.

Laten we bekijken hoe deze parameters geconfigureerd kunnen worden in verschillende programmeertalen.

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

In bovenstaande code hebben we:

- Een MCP-client aangemaakt met een specifieke server-URL.
- Een verzoek geconfigureerd met samplingparameters zoals `temperature`, `top_p` en `top_k`.
- Het verzoek verzonden en de gegenereerde tekst afgedrukt.
- Gebruikt:
    - `allowedTools` om aan te geven welke tools het model mag gebruiken tijdens generatie. In dit geval hebben we de tools `ideaGenerator` en `marketAnalyzer` toegestaan om te helpen bij het genereren van creatieve app-ideeën.
    - `frequencyPenalty` en `presencePenalty` om herhaling en diversiteit in de output te sturen.
    - `temperature` om de willekeur van de output te regelen, waarbij hogere waarden leiden tot creatievere reacties.
    - `top_p` om de selectie van tokens te beperken tot die bijdragen aan de top cumulatieve waarschijnlijkheid, wat de kwaliteit van de gegenereerde tekst verbetert.
    - `top_k` om het model te beperken tot de top K meest waarschijnlijke tokens, wat kan helpen bij het genereren van meer samenhangende reacties.
    - `frequencyPenalty` en `presencePenalty` om herhaling te verminderen en diversiteit in de gegenereerde tekst aan te moedigen.

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

In bovenstaande code hebben we:

- Een MCP-client geïnitialiseerd met een server-URL en API-sleutel.
- Twee sets samplingparameters geconfigureerd: één voor creatieve taken en één voor feitelijke taken.
- Verzoeken verzonden met deze configuraties, waarbij het model specifieke tools mocht gebruiken voor elke taak.
- De gegenereerde reacties afgedrukt om de effecten van verschillende samplingparameters te demonstreren.
- Gebruikt `allowedTools` om aan te geven welke tools het model mag gebruiken tijdens generatie. In dit geval hebben we voor creatieve taken de tools `ideaGenerator` en `environmentalImpactTool` toegestaan, en voor feitelijke taken `factChecker` en `dataAnalysisTool`.
- `temperature` gebruikt om de willekeur van de output te regelen, waarbij hogere waarden leiden tot creatievere reacties.
- `top_p` gebruikt om de selectie van tokens te beperken tot die bijdragen aan de top cumulatieve waarschijnlijkheid, wat de kwaliteit van de gegenereerde tekst verbetert.
- `frequencyPenalty` en `presencePenalty` gebruikt om herhaling te verminderen en diversiteit in de output aan te moedigen.
- `top_k` gebruikt om het model te beperken tot de top K meest waarschijnlijke tokens, wat kan helpen bij het genereren van meer samenhangende reacties.

---

## Deterministische Sampling

Voor toepassingen die consistente output vereisen, zorgt deterministische sampling voor reproduceerbare resultaten. Dit wordt bereikt door een vaste random seed te gebruiken en de temperatuur op nul te zetten.

Hieronder een voorbeeldimplementatie die deterministische sampling demonstreert in verschillende programmeertalen.

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

In bovenstaande code hebben we:

- Een MCP-client aangemaakt met een opgegeven server-URL.
- Twee verzoeken geconfigureerd met dezelfde prompt, vaste seed en temperatuur nul.
- Beide verzoeken verzonden en de gegenereerde tekst afgedrukt.
- Aangetoond dat de reacties identiek zijn vanwege de deterministische aard van de samplingconfiguratie (zelfde seed en temperatuur).
- `setSeed` gebruikt om een vaste random seed op te geven, zodat het model elke keer dezelfde output genereert voor dezelfde input.
- `temperature` op nul gezet om maximale determinisme te garanderen, wat betekent dat het model altijd de meest waarschijnlijke volgende token kiest zonder willekeur.

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

In bovenstaande code hebben we:

- Een MCP-client geïnitialiseerd met een server-URL.
- Twee verzoeken geconfigureerd met dezelfde prompt, vaste seed en temperatuur nul.
- Beide verzoeken verzonden en de gegenereerde tekst afgedrukt.
- Aangetoond dat de reacties identiek zijn vanwege de deterministische aard van de samplingconfiguratie (zelfde seed en temperatuur).
- `seed` gebruikt om een vaste random seed op te geven, zodat het model elke keer dezelfde output genereert voor dezelfde input.
- `temperature` op nul gezet om maximale determinisme te garanderen, wat betekent dat het model altijd de meest waarschijnlijke volgende token kiest zonder willekeur.
- Voor het derde verzoek een andere seed gebruikt om te laten zien dat het veranderen van de seed resulteert in verschillende output, zelfs met dezelfde prompt en temperatuur.

---

## Dynamische Samplingconfiguratie

Intelligente sampling past parameters aan op basis van de context en vereisten van elk verzoek. Dit betekent dat parameters zoals temperature, top_p en straffen dynamisch worden aangepast op basis van het type taak, gebruikersvoorkeuren of historische prestaties.

Laten we bekijken hoe dynamische sampling geïmplementeerd kan worden in verschillende programmeertalen.

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

In bovenstaande code hebben we:

- Een `DynamicSamplingService` klasse gemaakt die adaptieve sampling beheert.
- Sampling presets gedefinieerd voor verschillende taaktypes (creatief, feitelijk, code, analytisch).
- Een basis sampling preset geselecteerd op basis van het taaktype.
- Samplingparameters aangepast op basis van gebruikersvoorkeuren, zoals creativiteitsniveau en diversiteit.
- Het verzoek verzonden met de dynamisch geconfigureerde samplingparameters.
- De gegenereerde tekst teruggegeven samen met de toegepaste samplingparameters en het taaktype voor transparantie.
- `temperature` gebruikt om de willekeur van de output te regelen, waarbij hogere waarden leiden tot creatievere reacties.
- `top_p` gebruikt om de selectie van tokens te beperken tot die bijdragen aan de top cumulatieve waarschijnlijkheid, wat de kwaliteit van de gegenereerde tekst verbetert.
- `frequency_penalty` gebruikt om herhaling te verminderen en diversiteit in de output aan te moedigen.
- `user_preferences` gebruikt om de samplingparameters aan te passen op basis van door de gebruiker gedefinieerde creativiteits- en diversiteitsniveaus.
- `task_type` gebruikt om de juiste samplingstrategie voor het verzoek te bepalen, wat meer op maat gemaakte reacties mogelijk maakt afhankelijk van de aard van de taak.
- `send_request` methode gebruikt om de prompt te verzenden met de geconfigureerde samplingparameters, zodat het model tekst genereert volgens de gespecificeerde eisen.
- `generated_text` gebruikt om de reactie van het model op te halen, die vervolgens samen met de samplingparameters en het taaktype wordt teruggegeven voor verdere analyse of weergave.
- `min` en `max` functies gebruikt om te zorgen dat gebruikersvoorkeuren binnen geldige grenzen blijven, waardoor ongeldige samplingconfiguraties worden voorkomen.

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

In bovenstaande code hebben we:

- Een `AdaptiveSamplingManager` klasse gemaakt die dynamische sampling beheert op basis van taaktype en gebruikersvoorkeuren.
- Samplingprofielen gedefinieerd voor verschillende taaktypes (creatief, feitelijk, code, conversatie).
- Een methode geïmplementeerd om het taaktype uit de prompt te detecteren met eenvoudige heuristieken.
- Samplingparameters berekend op basis van het gedetecteerde taaktype en gebruikersvoorkeuren.
- Geleerde aanpassingen toegepast op basis van historische prestaties om samplingparameters te optimaliseren.
- Prestaties geregistreerd voor toekomstige aanpassingen, zodat het systeem kan leren van eerdere interacties.
- Verzoeken verzonden met dynamisch geconfigureerde samplingparameters en de gegenereerde tekst teruggegeven samen met de toegepaste parameters en het gedetecteerde taaktype.
- Gebruikt:
    - `userPreferences` om de samplingparameters aan te passen op basis van door de gebruiker gedefinieerde creativiteit, precisie en consistentie.
    - `detectTaskType` om de aard van de taak te bepalen op basis van de prompt, wat meer op maat gemaakte reacties mogelijk maakt.
    - `recordPerformance` om de prestaties van gegenereerde reacties te loggen, zodat het systeem zich kan aanpassen en verbeteren.
    - `applyLearnedAdjustments` om samplingparameters aan te passen op basis van historische prestaties, wat de kwaliteit van gegenereerde reacties verbetert.
    - `generateResponse` om het volledige proces van het genereren van een reactie met adaptieve sampling te encapsuleren, zodat het eenvoudig aan te roepen is met verschillende prompts en contexten.
    - `allowedTools` om aan te geven welke tools het model mag gebruiken tijdens generatie, wat contextbewustere reacties mogelijk maakt.
    - `feedbackScore` om gebruikers feedback te laten geven op de kwaliteit van de gegenereerde reactie, wat gebruikt kan worden om de modelprestaties verder te verfijnen.
    - `performanceHistory` om een overzicht bij te houden van eerdere interacties, zodat het systeem kan leren van successen en mislukkingen.
    - `getSamplingParameters` om samplingparameters dynamisch aan te passen op basis van de context van het verzoek, wat flexibeler en responsiever modelgedrag mogelijk maakt.
    - `detectTaskType` om de taak te classificeren op basis van de prompt, zodat het systeem passende samplingstrategieën kan toepassen voor verschillende soorten verzoeken.
    - `samplingProfiles` om basisconfiguraties voor sampling te definiëren voor verschillende taaktypes, wat snelle aanpassingen mogelijk maakt afhankelijk van de aard van het verzoek.

---

## Wat volgt

- [5.7 Scaling](../mcp-scaling/README.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.