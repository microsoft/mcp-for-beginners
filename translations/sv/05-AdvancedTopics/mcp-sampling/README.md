# Sampling i Model Context Protocol

Sampling är en kraftfull MCP-funktion som gör det möjligt för servrar att begära LLM-kompletteringar via klienten, vilket möjliggör avancerade agentliknande beteenden samtidigt som säkerhet och integritet upprätthålls. Rätt samplingkonfiguration kan avsevärt förbättra svarskvalitet och prestanda. MCP erbjuder ett standardiserat sätt att styra hur modeller genererar text med specifika parametrar som påverkar slumpmässighet, kreativitet och sammanhang.

## Introduktion

I denna lektion kommer vi att utforska hur man konfigurerar samplingparametrar i MCP-förfrågningar och förstå de underliggande protokollmekanismerna för sampling.

## Lärandemål

Efter denna lektion kommer du att kunna:

- Förstå de viktigaste samplingparametrarna som finns i MCP.
- Konfigurera samplingparametrar för olika användningsområden.
- Implementera deterministisk sampling för reproducerbara resultat.
- Dynamiskt justera samplingparametrar baserat på kontext och användarpreferenser.
- Använda samplingstrategier för att förbättra modellens prestanda i olika scenarier.
- Förstå hur sampling fungerar i klient-server-flödet i MCP.

## Hur sampling fungerar i MCP

Samplingflödet i MCP följer dessa steg:

1. Server skickar en `sampling/createMessage`-förfrågan till klienten
2. Klienten granskar förfrågan och kan modifiera den
3. Klienten samplar från en LLM
4. Klienten granskar kompletteringen
5. Klienten returnerar resultatet till servern

Denna design med mänsklig inblandning säkerställer att användare behåller kontroll över vad LLM ser och genererar.

## Översikt över samplingparametrar

MCP definierar följande samplingparametrar som kan konfigureras i klientförfrågningar:

| Parameter | Beskrivning | Typiskt intervall |
|-----------|-------------|-------------------|
| `temperature` | Styr slumpmässigheten vid val av token | 0.0 - 1.0 |
| `maxTokens` | Max antal tokens att generera | Heltal |
| `stopSequences` | Anpassade sekvenser som stoppar genereringen när de påträffas | Array av strängar |
| `metadata` | Ytterligare leverantörsspecifika parametrar | JSON-objekt |

Många LLM-leverantörer stödjer ytterligare parametrar via `metadata`-fältet, som kan inkludera:

| Vanlig utökad parameter | Beskrivning | Typiskt intervall |
|-------------------------|-------------|-------------------|
| `top_p` | Nucleus sampling – begränsar tokens till topp kumulativ sannolikhet | 0.0 - 1.0 |
| `top_k` | Begränsar tokenval till topp K alternativ | 1 - 100 |
| `presence_penalty` | Straffar tokens baserat på deras närvaro i texten hittills | -2.0 - 2.0 |
| `frequency_penalty` | Straffar tokens baserat på deras frekvens i texten hittills | -2.0 - 2.0 |
| `seed` | Specifik slumpmässig seed för reproducerbara resultat | Heltal |

## Exempel på förfrågningsformat

Här är ett exempel på hur man begär sampling från en klient i MCP:

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

## Svarsformat

Klienten returnerar ett resultat av komplettering:

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

## Mänsklig inblandning och kontroll

MCP-sampling är designad med mänsklig övervakning i åtanke:

- **För prompts**:
  - Klienter bör visa användare den föreslagna prompten
  - Användare ska kunna ändra eller avvisa prompts
  - Systemprompts kan filtreras eller modifieras
  - Kontextinkludering styrs av klienten

- **För kompletteringar**:
  - Klienter bör visa användare kompletteringen
  - Användare ska kunna ändra eller avvisa kompletteringar
  - Klienter kan filtrera eller modifiera kompletteringar
  - Användare styr vilken modell som används

Med dessa principer i åtanke, låt oss titta på hur sampling implementeras i olika programmeringsspråk, med fokus på parametrar som vanligtvis stöds av LLM-leverantörer.

## Säkerhetsaspekter

När sampling implementeras i MCP bör följande säkerhetsrutiner beaktas:

- **Validera allt meddelandeinnehåll** innan det skickas till klienten
- **Rensa känslig information** från prompts och kompletteringar
- **Implementera hastighetsbegränsningar** för att förhindra missbruk
- **Övervaka samplinganvändning** för ovanliga mönster
- **Kryptera data under överföring** med säkra protokoll
- **Hantera användardataintegritet** enligt gällande regler
- **Granska samplingförfrågningar** för efterlevnad och säkerhet
- **Kontrollera kostnadsexponering** med lämpliga begränsningar
- **Implementera timeout** för samplingförfrågningar
- **Hantera modellfel på ett smidigt sätt** med lämpliga reservlösningar

Samplingparametrar möjliggör finjustering av språkmodellers beteende för att uppnå önskad balans mellan deterministiska och kreativa svar.

Låt oss se hur man konfigurerar dessa parametrar i olika programmeringsspråk.

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

I koden ovan har vi:

- Skapat en MCP-klient med en specifik server-URL.
- Konfigurerat en förfrågan med samplingparametrar som `temperature`, `top_p` och `top_k`.
- Skickat förfrågan och skrivit ut den genererade texten.
- Använt:
    - `allowedTools` för att specificera vilka verktyg modellen kan använda under genereringen. I detta fall tillät vi verktygen `ideaGenerator` och `marketAnalyzer` för att hjälpa till att generera kreativa appidéer.
    - `frequencyPenalty` och `presencePenalty` för att kontrollera upprepning och mångfald i output.
    - `temperature` för att styra slumpmässigheten i output, där högre värden leder till mer kreativa svar.
    - `top_p` för att begränsa tokenvalet till de som bidrar till den högsta kumulativa sannolikhetsmassan, vilket förbättrar kvaliteten på genererad text.
    - `top_k` för att begränsa modellen till de topp K mest sannolika tokens, vilket kan hjälpa till att generera mer sammanhängande svar.
    - `frequencyPenalty` och `presencePenalty` för att minska upprepning och uppmuntra mångfald i den genererade texten.

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

I koden ovan har vi:

- Initierat en MCP-klient med en server-URL och API-nyckel.
- Konfigurerat två uppsättningar samplingparametrar: en för kreativa uppgifter och en annan för faktabaserade uppgifter.
- Skickat förfrågningar med dessa konfigurationer, där modellen tillåts använda specifika verktyg för varje uppgift.
- Skrivit ut de genererade svaren för att visa effekterna av olika samplingparametrar.
- Använt `allowedTools` för att specificera vilka verktyg modellen kan använda under genereringen. I detta fall tillät vi `ideaGenerator` och `environmentalImpactTool` för kreativa uppgifter, samt `factChecker` och `dataAnalysisTool` för faktabaserade uppgifter.
- Använt `temperature` för att styra slumpmässigheten i output, där högre värden leder till mer kreativa svar.
- Använt `top_p` för att begränsa tokenvalet till de som bidrar till den högsta kumulativa sannolikhetsmassan, vilket förbättrar kvaliteten på genererad text.
- Använt `frequencyPenalty` och `presencePenalty` för att minska upprepning och uppmuntra mångfald i output.
- Använt `top_k` för att begränsa modellen till de topp K mest sannolika tokens, vilket kan hjälpa till att generera mer sammanhängande svar.

---

## Deterministisk sampling

För applikationer som kräver konsekventa resultat säkerställer deterministisk sampling reproducerbara svar. Det görs genom att använda en fast slumpmässig seed och sätta temperaturen till noll.

Låt oss titta på följande exempel som demonstrerar deterministisk sampling i olika programmeringsspråk.

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

I koden ovan har vi:

- Skapat en MCP-klient med en angiven server-URL.
- Konfigurerat två förfrågningar med samma prompt, fast seed och temperatur noll.
- Skickat båda förfrågningarna och skrivit ut den genererade texten.
- Visat att svaren är identiska tack vare den deterministiska naturen i samplingkonfigurationen (samma seed och temperatur).
- Använt `setSeed` för att specificera en fast slumpmässig seed, vilket säkerställer att modellen genererar samma output för samma input varje gång.
- Satt `temperature` till noll för att säkerställa maximal determinism, vilket innebär att modellen alltid väljer den mest sannolika nästa token utan slumpmässighet.

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

I koden ovan har vi:

- Initierat en MCP-klient med en server-URL.
- Konfigurerat två förfrågningar med samma prompt, fast seed och temperatur noll.
- Skickat båda förfrågningarna och skrivit ut den genererade texten.
- Visat att svaren är identiska tack vare den deterministiska naturen i samplingkonfigurationen (samma seed och temperatur).
- Använt `seed` för att specificera en fast slumpmässig seed, vilket säkerställer att modellen genererar samma output för samma input varje gång.
- Satt `temperature` till noll för att säkerställa maximal determinism, vilket innebär att modellen alltid väljer den mest sannolika nästa token utan slumpmässighet.
- Använt en annan seed för den tredje förfrågan för att visa att ändring av seed ger olika output, även med samma prompt och temperatur.

---

## Dynamisk samplingkonfiguration

Intelligent sampling anpassar parametrar baserat på kontext och krav för varje förfrågan. Det innebär att dynamiskt justera parametrar som temperature, top_p och straff baserat på uppgiftstyp, användarpreferenser eller historisk prestanda.

Låt oss se hur man implementerar dynamisk sampling i olika programmeringsspråk.

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

I koden ovan har vi:

- Skapat en klass `DynamicSamplingService` som hanterar adaptiv sampling.
- Definierat samplingförinställningar för olika uppgiftstyper (kreativ, faktabaserad, kod, analytisk).
- Vald en grundläggande samplingförinställning baserat på uppgiftstyp.
- Justerat samplingparametrarna baserat på användarpreferenser, såsom kreativitet och mångfald.
- Skickat förfrågan med de dynamiskt konfigurerade samplingparametrarna.
- Returnerat den genererade texten tillsammans med de använda samplingparametrarna och uppgiftstypen för transparens.
- Använt `temperature` för att styra slumpmässigheten i output, där högre värden leder till mer kreativa svar.
- Använt `top_p` för att begränsa tokenvalet till de som bidrar till den högsta kumulativa sannolikhetsmassan, vilket förbättrar kvaliteten på genererad text.
- Använt `frequency_penalty` för att minska upprepning och uppmuntra mångfald i output.
- Använt `user_preferences` för att möjliggöra anpassning av samplingparametrar baserat på användardefinierade nivåer av kreativitet och mångfald.
- Använt `task_type` för att bestämma lämplig samplingstrategi för förfrågan, vilket möjliggör mer skräddarsydda svar baserat på uppgiftens natur.
- Använt metoden `send_request` för att skicka prompten med de konfigurerade samplingparametrarna, vilket säkerställer att modellen genererar text enligt de angivna kraven.
- Använt `generated_text` för att hämta modellens svar, som sedan returneras tillsammans med samplingparametrar och uppgiftstyp för vidare analys eller visning.
- Använt `min` och `max` för att säkerställa att användarpreferenser hålls inom giltiga intervall, vilket förhindrar ogiltiga samplingkonfigurationer.

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

I koden ovan har vi:

- Skapat en klass `AdaptiveSamplingManager` som hanterar dynamisk sampling baserat på uppgiftstyp och användarpreferenser.
- Definierat samplingprofiler för olika uppgiftstyper (kreativ, faktabaserad, kod, konversation).
- Implementerat en metod för att upptäcka uppgiftstyp från prompten med enkla heuristiker.
- Beräknat samplingparametrar baserat på den upptäckta uppgiftstypen och användarpreferenser.
- Tillämpat inlärda justeringar baserat på historisk prestanda för att optimera samplingparametrarna.
- Registrerat prestanda för framtida justeringar, vilket gör att systemet kan lära sig av tidigare interaktioner.
- Skickat förfrågningar med dynamiskt konfigurerade samplingparametrar och returnerat den genererade texten tillsammans med använda parametrar och upptäckt uppgiftstyp.
- Använt:
    - `userPreferences` för att möjliggöra anpassning av samplingparametrar baserat på användardefinierade nivåer av kreativitet, precision och konsekvens.
    - `detectTaskType` för att bestämma uppgiftens natur baserat på prompten, vilket möjliggör mer skräddarsydda svar.
    - `recordPerformance` för att logga prestandan hos genererade svar, vilket gör att systemet kan anpassa sig och förbättras över tid.
    - `applyLearnedAdjustments` för att modifiera samplingparametrar baserat på historisk prestanda, vilket förbättrar modellens förmåga att generera högkvalitativa svar.
    - `generateResponse` för att kapsla in hela processen att generera ett svar med adaptiv sampling, vilket gör det enkelt att anropa med olika prompts och kontexter.
    - `allowedTools` för att specificera vilka verktyg modellen kan använda under genereringen, vilket möjliggör mer kontextmedvetna svar.
    - `feedbackScore` för att låta användare ge feedback på kvaliteten av det genererade svaret, vilket kan användas för att ytterligare förbättra modellens prestanda över tid.
    - `performanceHistory` för att hålla en historik över tidigare interaktioner, vilket gör att systemet kan lära sig av tidigare framgångar och misslyckanden.
    - `getSamplingParameters` för att dynamiskt justera samplingparametrar baserat på kontexten i förfrågan, vilket möjliggör mer flexibel och responsiv modellbeteende.
    - `detectTaskType` för att klassificera uppgiften baserat på prompten, vilket gör att systemet kan tillämpa lämpliga samplingstrategier för olika typer av förfrågningar.
    - `samplingProfiles` för att definiera grundläggande samplingkonfigurationer för olika uppgiftstyper, vilket möjliggör snabba justeringar baserat på uppgiftens natur.

---

## Vad händer härnäst

- [5.7 Scaling](../mcp-scaling/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.