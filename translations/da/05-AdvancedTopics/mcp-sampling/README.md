# Sampling i Model Context Protocol

Sampling er en kraftfuld MCP-funktion, der gør det muligt for servere at anmode om LLM-fuldførelser via klienten, hvilket muliggør avancerede agent-lignende adfærd samtidig med, at sikkerhed og privatliv bevares. Den rette sampling-konfiguration kan markant forbedre svarenes kvalitet og ydeevne. MCP tilbyder en standardiseret måde at styre, hvordan modeller genererer tekst med specifikke parametre, der påvirker tilfældighed, kreativitet og sammenhæng.

## Introduktion

I denne lektion vil vi udforske, hvordan man konfigurerer sampling-parametre i MCP-forespørgsler og forstå de underliggende protokolmekanismer for sampling.

## Læringsmål

Når du har gennemført denne lektion, vil du kunne:

- Forstå de vigtigste sampling-parametre, der er tilgængelige i MCP.
- Konfigurere sampling-parametre til forskellige anvendelsestilfælde.
- Implementere deterministisk sampling for reproducerbare resultater.
- Dynamisk justere sampling-parametre baseret på kontekst og brugerpræferencer.
- Anvende sampling-strategier for at forbedre modelpræstation i forskellige scenarier.
- Forstå, hvordan sampling fungerer i klient-server-flowet i MCP.

## Hvordan Sampling Fungerer i MCP

Sampling-flowet i MCP følger disse trin:

1. Serveren sender en `sampling/createMessage`-forespørgsel til klienten  
2. Klienten gennemgår forespørgslen og kan ændre den  
3. Klienten sampler fra en LLM  
4. Klienten gennemgår fuldførelsen  
5. Klienten returnerer resultatet til serveren  

Dette design med mennesket i loop sikrer, at brugerne bevarer kontrollen over, hvad LLM’en ser og genererer.

## Oversigt over Sampling-parametre

MCP definerer følgende sampling-parametre, som kan konfigureres i klientforespørgsler:

| Parameter       | Beskrivelse                              | Typisk interval    |
|-----------------|----------------------------------------|--------------------|
| `temperature`   | Styrer tilfældighed i token-udvælgelse | 0.0 - 1.0          |
| `maxTokens`     | Maksimalt antal tokens, der genereres  | Heltal             |
| `stopSequences` | Egendefinerede sekvenser, der stopper generering ved opdagelse | Array af strenge   |
| `metadata`      | Yderligere leverandørspecifikke parametre | JSON-objekt        |

Mange LLM-udbydere understøtter yderligere parametre via `metadata`-feltet, som kan inkludere:

| Almindelig Udvidelsesparameter | Beskrivelse                                         | Typisk interval    |
|-------------------------------|----------------------------------------------------|--------------------|
| `top_p`                       | Nucleus sampling - begrænser tokens til top kumulativ sandsynlighed | 0.0 - 1.0          |
| `top_k`                       | Begrænser token-udvælgelse til top K muligheder    | 1 - 100            |
| `presence_penalty`            | Straffer tokens baseret på deres tilstedeværelse i teksten hidtil | -2.0 - 2.0          |
| `frequency_penalty`           | Straffer tokens baseret på deres hyppighed i teksten hidtil | -2.0 - 2.0          |
| `seed`                        | Specifik tilfældig seed for reproducerbare resultater | Heltal             |

## Eksempel på Forespørgselsformat

Her er et eksempel på, hvordan man anmoder om sampling fra en klient i MCP:

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

## Svarformat

Klienten returnerer et fuldførelsesresultat:

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

## Mennesket i Loop-kontroller

MCP-sampling er designet med menneskelig overvågning for øje:

- **For prompts**:  
  - Klienter bør vise brugerne den foreslåede prompt  
  - Brugere skal kunne ændre eller afvise prompts  
  - Systemprompts kan filtreres eller ændres  
  - Inklusion af kontekst styres af klienten  

- **For fuldførelser**:  
  - Klienter bør vise brugerne fuldførelsen  
  - Brugere skal kunne ændre eller afvise fuldførelser  
  - Klienter kan filtrere eller ændre fuldførelser  
  - Brugere styrer, hvilken model der anvendes  

Med disse principper in mente, lad os se på, hvordan sampling implementeres i forskellige programmeringssprog med fokus på de parametre, der ofte understøttes på tværs af LLM-udbydere.

## Sikkerhedsovervejelser

Når sampling implementeres i MCP, bør følgende sikkerhedspraksis overvejes:

- **Valider alt beskedindhold** før det sendes til klienten  
- **Rens følsomme oplysninger** fra prompts og fuldførelser  
- **Implementer ratebegrænsninger** for at forhindre misbrug  
- **Overvåg sampling-brug** for usædvanlige mønstre  
- **Krypter data under overførsel** med sikre protokoller  
- **Håndter brugerdata-privatliv** i overensstemmelse med gældende regler  
- **Revider sampling-forespørgsler** for overholdelse og sikkerhed  
- **Kontroller omkostningseksponering** med passende grænser  
- **Implementer timeouts** for sampling-forespørgsler  
- **Håndter model-fejl yndefuldt** med passende fallback-mekanismer  

Sampling-parametre tillader finjustering af sprogmodellers adfærd for at opnå den ønskede balance mellem deterministiske og kreative output.

Lad os se på, hvordan disse parametre konfigureres i forskellige programmeringssprog.

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

I den foregående kode har vi:

- Oprettet en MCP-klient med en specifik server-URL.  
- Konfigureret en forespørgsel med sampling-parametre som `temperature`, `top_p` og `top_k`.  
- Sendt forespørgslen og udskrevet den genererede tekst.  
- Brugte:  
    - `allowedTools` til at specificere, hvilke værktøjer modellen kan bruge under genereringen. I dette tilfælde tillod vi `ideaGenerator` og `marketAnalyzer` til at hjælpe med at generere kreative app-idéer.  
    - `frequencyPenalty` og `presencePenalty` til at kontrollere gentagelse og variation i output.  
    - `temperature` til at styre tilfældigheden i output, hvor højere værdier fører til mere kreative svar.  
    - `top_p` til at begrænse udvælgelsen af tokens til dem, der bidrager til den øverste kumulative sandsynlighed, hvilket forbedrer kvaliteten af den genererede tekst.  
    - `top_k` til at begrænse modellen til de top K mest sandsynlige tokens, hvilket kan hjælpe med at generere mere sammenhængende svar.  
    - `frequencyPenalty` og `presencePenalty` til at reducere gentagelse og fremme variation i den genererede tekst.

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

I den foregående kode har vi:

- Initialiseret en MCP-klient med en server-URL og API-nøgle.  
- Konfigureret to sæt sampling-parametre: et til kreative opgaver og et andet til faktuelle opgaver.  
- Sendt forespørgsler med disse konfigurationer, hvor modellen fik lov til at bruge specifikke værktøjer til hver opgave.  
- Udskrevet de genererede svar for at demonstrere effekten af forskellige sampling-parametre.  
- Brugte `allowedTools` til at specificere, hvilke værktøjer modellen kan bruge under genereringen. I dette tilfælde tillod vi `ideaGenerator` og `environmentalImpactTool` til kreative opgaver, og `factChecker` og `dataAnalysisTool` til faktuelle opgaver.  
- Brugte `temperature` til at styre tilfældigheden i output, hvor højere værdier fører til mere kreative svar.  
- Brugte `top_p` til at begrænse udvælgelsen af tokens til dem, der bidrager til den øverste kumulative sandsynlighed, hvilket forbedrer kvaliteten af den genererede tekst.  
- Brugte `frequencyPenalty` og `presencePenalty` til at reducere gentagelse og fremme variation i output.  
- Brugte `top_k` til at begrænse modellen til de top K mest sandsynlige tokens, hvilket kan hjælpe med at generere mere sammenhængende svar.

---

## Deterministisk Sampling

For applikationer, der kræver konsistente output, sikrer deterministisk sampling reproducerbare resultater. Det opnås ved at bruge en fast tilfældig seed og sætte temperaturen til nul.

Lad os se på nedenstående eksempelimplementering, der demonstrerer deterministisk sampling i forskellige programmeringssprog.

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

I den foregående kode har vi:

- Oprettet en MCP-klient med en specificeret server-URL.  
- Konfigureret to forespørgsler med samme prompt, fast seed og temperatur nul.  
- Sendt begge forespørgsler og udskrevet den genererede tekst.  
- Demonstreret, at svarene er identiske på grund af den deterministiske karakter af sampling-konfigurationen (samme seed og temperatur).  
- Brugte `setSeed` til at angive en fast tilfældig seed, hvilket sikrer, at modellen genererer det samme output for samme input hver gang.  
- Satte `temperature` til nul for at sikre maksimal determinisme, hvilket betyder, at modellen altid vælger den mest sandsynlige næste token uden tilfældighed.

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

I den foregående kode har vi:

- Initialiseret en MCP-klient med en server-URL.  
- Konfigureret to forespørgsler med samme prompt, fast seed og temperatur nul.  
- Sendt begge forespørgsler og udskrevet den genererede tekst.  
- Demonstreret, at svarene er identiske på grund af den deterministiske karakter af sampling-konfigurationen (samme seed og temperatur).  
- Brugte `seed` til at angive en fast tilfældig seed, hvilket sikrer, at modellen genererer det samme output for samme input hver gang.  
- Satte `temperature` til nul for at sikre maksimal determinisme, hvilket betyder, at modellen altid vælger den mest sandsynlige næste token uden tilfældighed.  
- Brugte en anden seed til den tredje forespørgsel for at vise, at ændring af seed resulterer i forskellige output, selv med samme prompt og temperatur.

---

## Dynamisk Sampling-konfiguration

Intelligent sampling tilpasser parametre baseret på konteksten og kravene i hver forespørgsel. Det betyder dynamisk justering af parametre som temperature, top_p og strafparametre baseret på opgavetype, brugerpræferencer eller historisk præstation.

Lad os se på, hvordan man implementerer dynamisk sampling i forskellige programmeringssprog.

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

I den foregående kode har vi:

- Oprettet en `DynamicSamplingService`-klasse, der håndterer adaptiv sampling.  
- Defineret sampling-forudindstillinger for forskellige opgavetyper (kreativ, faktuel, kode, analytisk).  
- Valgt en grundlæggende sampling-forudindstilling baseret på opgavetypen.  
- Justeret sampling-parametre baseret på brugerpræferencer som kreativitet og variation.  
- Sendt forespørgslen med de dynamisk konfigurerede sampling-parametre.  
- Returneret den genererede tekst sammen med de anvendte sampling-parametre og opgavetypen for gennemsigtighed.  
- Brugte `temperature` til at styre tilfældigheden i output, hvor højere værdier fører til mere kreative svar.  
- Brugte `top_p` til at begrænse udvælgelsen af tokens til dem, der bidrager til den øverste kumulative sandsynlighed, hvilket forbedrer kvaliteten af den genererede tekst.  
- Brugte `frequency_penalty` til at reducere gentagelse og fremme variation i output.  
- Brugte `user_preferences` til at tillade tilpasning af sampling-parametre baseret på brugerdefinerede niveauer af kreativitet og variation.  
- Brugte `task_type` til at bestemme den passende sampling-strategi for forespørgslen, hvilket muliggør mere skræddersyede svar baseret på opgavens karakter.  
- Brugte `send_request`-metoden til at sende prompten med de konfigurerede sampling-parametre, hvilket sikrer, at modellen genererer tekst i overensstemmelse med de specificerede krav.  
- Brugte `generated_text` til at hente modellens svar, som derefter returneres sammen med sampling-parametre og opgavetype til yderligere analyse eller visning.  
- Brugte `min` og `max` funktioner til at sikre, at brugerpræferencer holdes inden for gyldige intervaller og forhindrer ugyldige sampling-konfigurationer.

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

I den foregående kode har vi:

- Oprettet en `AdaptiveSamplingManager`-klasse, der håndterer dynamisk sampling baseret på opgavetype og brugerpræferencer.  
- Defineret sampling-profiler for forskellige opgavetyper (kreativ, faktuel, kode, samtale).  
- Implementeret en metode til at opdage opgavetypen ud fra prompten ved hjælp af simple heuristikker.  
- Beregnet sampling-parametre baseret på den opdagede opgavetype og brugerpræferencer.  
- Anvendt lærte justeringer baseret på historisk præstation for at optimere sampling-parametre.  
- Registreret præstation for fremtidige justeringer, hvilket gør det muligt for systemet at lære af tidligere interaktioner.  
- Sendt forespørgsler med dynamisk konfigurerede sampling-parametre og returneret den genererede tekst sammen med anvendte parametre og opdaget opgavetype.  
- Brugte:  
    - `userPreferences` til at tillade tilpasning af sampling-parametre baseret på brugerdefinerede niveauer af kreativitet, præcision og konsistens.  
    - `detectTaskType` til at bestemme opgavens karakter baseret på prompten, hvilket muliggør mere skræddersyede svar.  
    - `recordPerformance` til at logge præstationen af genererede svar, så systemet kan tilpasse og forbedre sig over tid.  
    - `applyLearnedAdjustments` til at ændre sampling-parametre baseret på historisk præstation, hvilket forbedrer modellens evne til at generere svar af høj kvalitet.  
    - `generateResponse` til at indkapsle hele processen med at generere et svar med adaptiv sampling, hvilket gør det nemt at kalde med forskellige prompts og kontekster.  
    - `allowedTools` til at specificere, hvilke værktøjer modellen kan bruge under genereringen, hvilket muliggør mere kontekstbevidste svar.  
    - `feedbackScore` til at lade brugere give feedback på kvaliteten af det genererede svar, som kan bruges til yderligere at forbedre modellens præstation over tid.  
    - `performanceHistory` til at opretholde en oversigt over tidligere interaktioner, hvilket gør det muligt for systemet at lære af tidligere succeser og fejl.  
    - `getSamplingParameters` til dynamisk at justere sampling-parametre baseret på konteksten i forespørgslen, hvilket muliggør mere fleksibel og responsiv modeladfærd.  
    - `detectTaskType` til at klassificere opgaven baseret på prompten, hvilket gør det muligt for systemet at anvende passende sampling-strategier for forskellige typer forespørgsler.  
    - `samplingProfiles` til at definere grundlæggende sampling-konfigurationer for forskellige opgavetyper, hvilket muliggør hurtige justeringer baseret på opgavens karakter.

---

## Hvad er det næste

- [5.7 Scaling](../mcp-scaling/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.