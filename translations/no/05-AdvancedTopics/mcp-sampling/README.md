# Sampling i Model Context Protocol

Sampling er en kraftig MCP-funksjon som lar servere be om LLM-kompletteringer gjennom klienten, noe som muliggjør avanserte agent-lignende oppførsel samtidig som sikkerhet og personvern opprettholdes. Riktig sampling-konfigurasjon kan dramatisk forbedre responskvalitet og ytelse. MCP gir en standardisert måte å kontrollere hvordan modeller genererer tekst med spesifikke parametere som påvirker tilfeldighet, kreativitet og sammenheng.

## Introduksjon

I denne leksjonen skal vi utforske hvordan man konfigurerer sampling-parametere i MCP-forespørsler og forstå de underliggende protokollmekanismene for sampling.

## Læringsmål

Etter denne leksjonen vil du kunne:

- Forstå de viktigste sampling-parametrene som er tilgjengelige i MCP.
- Konfigurere sampling-parametere for ulike bruksområder.
- Implementere deterministisk sampling for reproduserbare resultater.
- Dynamisk justere sampling-parametere basert på kontekst og brukerpreferanser.
- Anvende sampling-strategier for å forbedre modellens ytelse i ulike scenarier.
- Forstå hvordan sampling fungerer i klient-server-flyten i MCP.

## Hvordan sampling fungerer i MCP

Sampling-flyten i MCP følger disse stegene:

1. Server sender en `sampling/createMessage`-forespørsel til klienten
2. Klienten gjennomgår forespørselen og kan endre den
3. Klienten sampler fra en LLM
4. Klienten gjennomgår kompletteringen
5. Klienten returnerer resultatet til serveren

Dette designet med menneskelig involvering sikrer at brukerne beholder kontroll over hva LLM ser og genererer.

## Oversikt over sampling-parametere

MCP definerer følgende sampling-parametere som kan konfigureres i klientforespørsler:

| Parameter | Beskrivelse | Typisk område |
|-----------|-------------|---------------|
| `temperature` | Styrer tilfeldighet i valg av tokens | 0.0 - 1.0 |
| `maxTokens` | Maksimalt antall tokens som skal genereres | Heltall |
| `stopSequences` | Egne sekvenser som stopper generering når de oppdages | Array av strenger |
| `metadata` | Ytterligere leverandørspesifikke parametere | JSON-objekt |

Mange LLM-leverandører støtter ekstra parametere gjennom `metadata`-feltet, som kan inkludere:

| Vanlig utvidelsesparameter | Beskrivelse | Typisk område |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - begrenser tokens til topp kumulativ sannsynlighet | 0.0 - 1.0 |
| `top_k` | Begrenser token-valg til topp K alternativer | 1 - 100 |
| `presence_penalty` | Straffer tokens basert på om de allerede er til stede i teksten | -2.0 - 2.0 |
| `frequency_penalty` | Straffer tokens basert på hvor ofte de forekommer i teksten | -2.0 - 2.0 |
| `seed` | Spesifikk tilfeldig seed for reproduserbare resultater | Heltall |

## Eksempel på forespørselsformat

Her er et eksempel på hvordan man ber om sampling fra en klient i MCP:

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

## Responsformat

Klienten returnerer et kompletteringsresultat:

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

## Menneskelig kontroll i løkken

MCP-sampling er designet med menneskelig tilsyn i tankene:

- **For prompts**:
  - Klienter bør vise brukerne den foreslåtte prompten
  - Brukere bør kunne endre eller avvise prompts
  - Systemprompter kan filtreres eller endres
  - Inkludering av kontekst styres av klienten

- **For kompletteringer**:
  - Klienter bør vise brukerne kompletteringen
  - Brukere bør kunne endre eller avvise kompletteringer
  - Klienter kan filtrere eller endre kompletteringer
  - Brukere kontrollerer hvilken modell som brukes

Med disse prinsippene i bakhodet, la oss se på hvordan sampling kan implementeres i ulike programmeringsspråk, med fokus på parametere som ofte støttes av LLM-leverandører.

## Sikkerhetshensyn

Når du implementerer sampling i MCP, bør du vurdere disse sikkerhetspraksisene:

- **Valider alt meldingsinnhold** før det sendes til klienten
- **Rens sensitiv informasjon** fra prompts og kompletteringer
- **Implementer ratebegrensninger** for å forhindre misbruk
- **Overvåk sampling-bruk** for uvanlige mønstre
- **Krypter data under overføring** med sikre protokoller
- **Håndter personvern for brukerdata** i henhold til gjeldende regelverk
- **Revider sampling-forespørsler** for samsvar og sikkerhet
- **Kontroller kostnadseksponering** med passende begrensninger
- **Implementer tidsavbrudd** for sampling-forespørsler
- **Håndter modellfeil på en robust måte** med passende fallback-løsninger

Sampling-parametere gjør det mulig å finjustere oppførselen til språkmodeller for å oppnå ønsket balanse mellom deterministiske og kreative resultater.

La oss se på hvordan disse parameterne kan konfigureres i ulike programmeringsspråk.

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

I koden ovenfor har vi:

- Opprettet en MCP-klient med en spesifikk server-URL.
- Konfigurert en forespørsel med sampling-parametere som `temperature`, `top_p` og `top_k`.
- Sendt forespørselen og skrevet ut den genererte teksten.
- Brukt:
    - `allowedTools` for å spesifisere hvilke verktøy modellen kan bruke under generering. I dette tilfellet tillot vi `ideaGenerator` og `marketAnalyzer` for å hjelpe med å generere kreative app-ideer.
    - `frequencyPenalty` og `presencePenalty` for å kontrollere repetisjon og variasjon i output.
    - `temperature` for å styre tilfeldigheten i output, der høyere verdier gir mer kreative svar.
    - `top_p` for å begrense valg av tokens til de som bidrar til topp kumulativ sannsynlighet, noe som forbedrer kvaliteten på generert tekst.
    - `top_k` for å begrense modellen til topp K mest sannsynlige tokens, noe som kan hjelpe med å generere mer sammenhengende svar.
    - `frequencyPenalty` og `presencePenalty` for å redusere repetisjon og oppmuntre til variasjon i generert tekst.

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

I koden ovenfor har vi:

- Initialisert en MCP-klient med server-URL og API-nøkkel.
- Konfigurert to sett med sampling-parametere: ett for kreative oppgaver og ett for faktabaserte oppgaver.
- Sendt forespørsler med disse konfigurasjonene, og tillatt modellen å bruke spesifikke verktøy for hver oppgave.
- Skrevet ut de genererte svarene for å demonstrere effekten av ulike sampling-parametere.
- Brukt `allowedTools` for å spesifisere hvilke verktøy modellen kan bruke under generering. I dette tilfellet tillot vi `ideaGenerator` og `environmentalImpactTool` for kreative oppgaver, og `factChecker` og `dataAnalysisTool` for faktabaserte oppgaver.
- Brukt `temperature` for å styre tilfeldigheten i output, der høyere verdier gir mer kreative svar.
- Brukt `top_p` for å begrense valg av tokens til de som bidrar til topp kumulativ sannsynlighet, noe som forbedrer kvaliteten på generert tekst.
- Brukt `frequencyPenalty` og `presencePenalty` for å redusere repetisjon og oppmuntre til variasjon i output.
- Brukt `top_k` for å begrense modellen til topp K mest sannsynlige tokens, noe som kan hjelpe med å generere mer sammenhengende svar.

---

## Deterministisk sampling

For applikasjoner som krever konsistente resultater, sikrer deterministisk sampling reproduserbare resultater. Dette gjøres ved å bruke en fast tilfeldig seed og sette temperaturen til null.

La oss se på et eksempel som demonstrerer deterministisk sampling i ulike programmeringsspråk.

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

I koden ovenfor har vi:

- Opprettet en MCP-klient med en spesifisert server-URL.
- Konfigurert to forespørsler med samme prompt, fast seed og temperatur satt til null.
- Sendt begge forespørslene og skrevet ut den genererte teksten.
- Demonstrert at svarene er identiske på grunn av den deterministiske naturen til sampling-konfigurasjonen (samme seed og temperatur).
- Brukt `setSeed` for å spesifisere en fast tilfeldig seed, som sikrer at modellen genererer samme output for samme input hver gang.
- Satt `temperature` til null for å sikre maksimal determinisme, noe som betyr at modellen alltid velger det mest sannsynlige neste token uten tilfeldighet.

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

I koden ovenfor har vi:

- Initialisert en MCP-klient med en server-URL.
- Konfigurert to forespørsler med samme prompt, fast seed og temperatur satt til null.
- Sendt begge forespørslene og skrevet ut den genererte teksten.
- Demonstrert at svarene er identiske på grunn av den deterministiske naturen til sampling-konfigurasjonen (samme seed og temperatur).
- Brukt `seed` for å spesifisere en fast tilfeldig seed, som sikrer at modellen genererer samme output for samme input hver gang.
- Satt `temperature` til null for å sikre maksimal determinisme, noe som betyr at modellen alltid velger det mest sannsynlige neste token uten tilfeldighet.
- Brukt en annen seed for den tredje forespørselen for å vise at endring av seed gir forskjellige resultater, selv med samme prompt og temperatur.

---

## Dynamisk sampling-konfigurasjon

Intelligent sampling tilpasser parametere basert på kontekst og krav for hver forespørsel. Det betyr at man dynamisk justerer parametere som temperature, top_p og straffer basert på oppgavetypen, brukerpreferanser eller historisk ytelse.

La oss se på hvordan man implementerer dynamisk sampling i ulike programmeringsspråk.

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

I koden ovenfor har vi:

- Opprettet en `DynamicSamplingService`-klasse som håndterer adaptiv sampling.
- Definert sampling-presets for ulike oppgavetyper (kreativ, faktabasert, kode, analytisk).
- Valgt en grunnleggende sampling-preset basert på oppgavetypen.
- Justert sampling-parametere basert på brukerpreferanser, som kreativitet og variasjon.
- Sendt forespørselen med de dynamisk konfigurerte sampling-parametrene.
- Returnert den genererte teksten sammen med de brukte sampling-parametrene og oppgavetypen for åpenhet.
- Brukt `temperature` for å styre tilfeldigheten i output, der høyere verdier gir mer kreative svar.
- Brukt `top_p` for å begrense valg av tokens til de som bidrar til topp kumulativ sannsynlighet, noe som forbedrer kvaliteten på generert tekst.
- Brukt `frequency_penalty` for å redusere repetisjon og oppmuntre til variasjon i output.
- Brukt `user_preferences` for å tillate tilpasning av sampling-parametere basert på brukerdefinerte nivåer for kreativitet og variasjon.
- Brukt `task_type` for å bestemme passende sampling-strategi for forespørselen, noe som gir mer skreddersydde svar basert på oppgavens natur.
- Brukt `send_request`-metoden for å sende prompten med konfigurerte sampling-parametere, og sikre at modellen genererer tekst i henhold til spesifiserte krav.
- Brukt `generated_text` for å hente modellens svar, som deretter returneres sammen med sampling-parametere og oppgavetypen for videre analyse eller visning.
- Brukt `min` og `max` for å sikre at brukerpreferanser holdes innen gyldige områder, og unngå ugyldige sampling-konfigurasjoner.

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

I koden ovenfor har vi:

- Opprettet en `AdaptiveSamplingManager`-klasse som håndterer dynamisk sampling basert på oppgavetype og brukerpreferanser.
- Definert sampling-profiler for ulike oppgavetyper (kreativ, faktabasert, kode, samtale).
- Implementert en metode for å oppdage oppgavetypen fra prompten ved hjelp av enkle heuristikker.
- Beregnet sampling-parametere basert på oppdaget oppgavetype og brukerpreferanser.
- Anvendt lærte justeringer basert på historisk ytelse for å optimalisere sampling-parametere.
- Registrert ytelse for fremtidige justeringer, slik at systemet kan lære av tidligere interaksjoner.
- Sendt forespørsler med dynamisk konfigurerte sampling-parametere og returnert generert tekst sammen med brukte parametere og oppdaget oppgavetype.
- Brukt:
    - `userPreferences` for å tillate tilpasning av sampling-parametere basert på brukerdefinerte nivåer for kreativitet, presisjon og konsistens.
    - `detectTaskType` for å bestemme oppgavens natur basert på prompten, noe som gir mer skreddersydde svar.
    - `recordPerformance` for å logge ytelsen til genererte svar, slik at systemet kan tilpasse og forbedre seg over tid.
    - `applyLearnedAdjustments` for å modifisere sampling-parametere basert på historisk ytelse, og forbedre modellens evne til å generere svar av høy kvalitet.
    - `generateResponse` for å kapsle inn hele prosessen med å generere et svar med adaptiv sampling, noe som gjør det enkelt å kalle med ulike prompts og kontekster.
    - `allowedTools` for å spesifisere hvilke verktøy modellen kan bruke under generering, noe som gir mer kontekstbevisste svar.
    - `feedbackScore` for å la brukere gi tilbakemelding på kvaliteten av det genererte svaret, som kan brukes til å forbedre modellens ytelse over tid.
    - `performanceHistory` for å opprettholde en oversikt over tidligere interaksjoner, slik at systemet kan lære av tidligere suksesser og feil.
    - `getSamplingParameters` for å dynamisk justere sampling-parametere basert på konteksten i forespørselen, noe som gir mer fleksibel og responsiv modelloppførsel.
    - `detectTaskType` for å klassifisere oppgaven basert på prompten, slik at systemet kan anvende passende sampling-strategier for ulike typer forespørsler.
    - `samplingProfiles` for å definere grunnleggende sampling-konfigurasjoner for ulike oppgavetyper, noe som muliggjør raske justeringer basert på oppgavens natur.

---

## Hva skjer videre

- [5.7 Skalering](../mcp-scaling/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.