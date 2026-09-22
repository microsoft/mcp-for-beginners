> [!WARNING]
> Sampling är föråldrat i MCP `2026-07-28`. Denna lektion behålls för
> äldre implementationer. Nya servrar bör integrera direkt med en LLM
> leverantörs-API.

# Sampling i Model Context Protocol

> Sampling finns kvar i `2026-07-28`-specifikationen för kompatibilitet och är
> kvalificerad för borttagning i den första revisionen som släpps den 28 juli
> 2027 eller senare. Exempel i denna lektion kan använda SDK-API:er som implementerar `2025-11-25`.
> Se [Vad som ändrats i MCP: Specifikationen 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

I äldre MCP-implementationer tillåter Sampling servrar att begära LLM-
avslut via klienten. Denna lektion förklarar det föråldrade protokollflödet
för kompatibilitet och migrationsarbete.

## Introduktion

I denna lektion utforskar vi hur man konfigurerar sampling-parametrar i MCP-förfrågningar och förstår de underliggande protokollmekanismerna för sampling.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Förstå de viktigaste sampling-parametrarna som finns tillgängliga i MCP.
- Konfigurera sampling-parametrar för olika användningsfall.
- Implementera deterministisk sampling för reproducerbara resultat.
- Dynamiskt justera sampling-parametrar baserat på kontext och användarpreferenser.
- Använda sampling-strategier för att förbättra modellens prestanda i olika scenarier.
- Förstå hur sampling fungerar i klient-server-flödet för MCP.

## Hur sampling fungerar i MCP

Sampling-flödet i MCP följer dessa steg:

1. Server skickar en `sampling/createMessage`-förfrågan till klienten
2. Klienten granskar förfrågan och kan modifiera den
3. Klienten sample från en LLM
4. Klienten granskar resultatet
5. Klienten returnerar resultatet till servern

Denna människa-i-loopen-design säkerställer att användare behåller kontrollen över vad LLM ser och genererar.

## Översikt över sampling-parametrar

MCP definierar följande sampling-parametrar som kan konfigureras i klientförfrågningar:

| Parameter | Beskrivning | Typiskt intervall |
|-----------|-------------|---------------|
| `temperature` | Styr slumpmässighet vid tokenval | 0.0 - 1.0 |
| `maxTokens` | Max antal tokens att generera | Heltal |
| `stopSequences` | Anpassade sekvenser som stoppar generering när de träffas | Array av strängar |
| `metadata` | Ytterligare leverantörsspecifika parametrar | JSON-objekt |

Många LLM-leverantörer stödjer ytterligare parametrar genom `metadata`-fältet, vilket kan inkludera:

| Vanlig utökningsparameter | Beskrivning | Typiskt intervall |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - begränsar tokens till den högsta kumulativa sannolikheten | 0.0 - 1.0 |
| `top_k` | Begränsar tokenval till de topp K alternativen | 1 - 100 |
| `presence_penalty` | Straffar tokens baserat på deras närvaro i texten hittills | -2.0 - 2.0 |
| `frequency_penalty` | Straffar tokens baserat på deras frekvens i texten hittills | -2.0 - 2.0 |
| `seed` | Specifik slumpmässig seed för reproducerbara resultat | Heltal |

## Exempel på förfrågningsformat

Här är ett exempel på en förfrågan om sampling från en klient i MCP:

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

Klienten returnerar ett genereringsresultat:

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

## Kontroll av människa i loopen

MCP-sampling är designad med mänsklig övervakning i åtanke:

- **För prompts**:
  - Klienter bör visa användarna den föreslagna prompten
  - Användare bör kunna modifiera eller avvisa prompts
  - Systemprompts kan filtreras eller modifieras
  - Kontextinkludering styrs av klienten

- **För avslut**:
  - Klienter bör visa användarna avslutningen
  - Användare bör kunna modifiera eller avvisa avslutningar
  - Klienter kan filtrera eller modifiera avslutningar
  - Användare kontrollerar vilken modell som används

Med dessa principer i åtanke, låt oss titta på hur sampling implementeras i olika programmeringsspråk, med fokus på parametrar som ofta stöds av LLM-leverantörer.

## Säkerhetsöverväganden

När du implementerar sampling i MCP, överväg dessa bästa säkerhetspraxis:

- **Verifiera allt meddelandeinnehåll** innan det skickas till klienten
- **Sanera känslig information** från prompts och avslut
- **Implementera begränsningar av antalet förfrågningar** för att förhindra missbruk
- **Övervaka samplinganvändning** för ovanliga mönster
- **Kryptera data under överföring** med säkra protokoll
- **Hantera användardataskydd** enligt relevanta regleringar
- **Granska samplingförfrågningar** för efterlevnad och säkerhet
- **Kontrollera kostnadsexponering** med lämpliga begränsningar
- **Implementera timeout för samplingförfrågningar**
- **Hantera modellfel smidigt** med lämpliga fallbacklösningar

Sampling-parametrar möjliggör finjustering av språkmodellers beteende för att uppnå önskad balans mellan deterministiska och kreativa utskrifter.

Låt oss titta på hur man konfigurerar dessa parametrar i olika programmeringsspråk.

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

I koden ovan har vi:

- Skapat en MCP-klient med en specifik server-URL.
- Konfigurerat en förfrågan med sampling-parametrar som `temperature`, `top_p` och `top_k`.
- Skickat förfrågan och skrivit ut den genererade texten.
- Använt:
    - `allowedTools` för att specificera vilka verktyg modellen kan använda under genereringen. I detta fall tillät vi verktygen `ideaGenerator` och `marketAnalyzer` att hjälpa till att generera kreativa appidéer.
    - `frequencyPenalty` och `presencePenalty` för att kontrollera upprepning och mångfald i resultatet.
    - `temperature` för att styra slumpmässigheten i utskriften, där högre värden leder till mer kreativa svar.
    - `top_p` för att begränsa urvalet av tokens till de som bidrar till den högsta kumulativa sannolikhetsmassan, vilket förbättrar kvaliteten på genererad text.
    - `top_k` för att begränsa modellen till topp K mest sannolika tokens, vilket kan hjälpa till att generera mer sammanhängande svar.
    - `frequencyPenalty` och `presencePenalty` för att minska upprepning och uppmuntra mångfald i den genererade texten.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript-exempel: Temperatur- och Top-P-samplingskonfiguration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initiera MCP-klienten
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Konfigurera förfrågan med olika samplingsparametrar
  const creativeSampling = {
    temperature: 0.9,    // Högre temperatur = mer slumpmässighet/skapande
    topP: 0.92,          // Beakta tokens med topp 92% sannolikhetsmassa
    frequencyPenalty: 0.6, // Minska upprepning av tokensekvenser
    presencePenalty: 0.4   // Straffa tokens som redan förekommit i texten
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lägre temperatur = mer deterministisk/faktabaserad
    topP: 0.85,          // Lite mer fokuserat tokenval
    frequencyPenalty: 0.2, // Minimal upprepningsstraff
    presencePenalty: 0.1   // Minimal närvarostraff
  };
  
  try {
    // Skicka två förfrågningar med olika samplingskonfigurationer
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
- Konfigurerat två uppsättningar sampling-parametrar: en för kreativa uppgifter och en annan för faktabaserade uppgifter.
- Skickat förfrågningar med dessa konfigurationer, vilket tillåter modellen att använda specifika verktyg för varje uppgift.
- Skrivit ut de genererade svaren för att visa effekterna av olika sampling-parametrar.
- Använt `allowedTools` för att specificera vilka verktyg modellen kan använda under genereringen. I detta fall tillät vi `ideaGenerator` och `environmentalImpactTool` för kreativa uppgifter, samt `factChecker` och `dataAnalysisTool` för faktabaserade uppgifter.
- Använt `temperature` för att styra slumpmässigheten i utskriften, där högre värden leder till mer kreativa svar.
- Använt `top_p` för att begränsa urvalet av tokens till de som bidrar till den högsta kumulativa sannolikhetsmassan, vilket förbättrar kvaliteten på genererad text.
- Använt `frequencyPenalty` och `presencePenalty` för att minska upprepning och uppmuntra mångfald i resultatet.
- Använt `top_k` för att begränsa modellen till topp K mest sannolika tokens, vilket kan hjälpa till att generera mer sammanhängande svar.

---

## Deterministisk sampling

För applikationer som kräver konsekventa resultat säkerställer deterministisk sampling reproducerbara resultat. Det gör den genom att använda en fast slumpfrö (seed) och sätta temperatur till noll.

Låt oss titta på nedanstående exempelimplementation för att demonstrera deterministisk sampling i olika programmeringsspråk.

# [Java](#tab/java)

```java
// Java Exempel: Deterministiska svar med fast frö
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Använder ett fast frö för deterministiska resultat
        
        // Första förfrågan med fast frö
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Noll temperatur för maximal determinism
            .build();
            
        // Andra förfrågan med samma frö
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Kör båda förfrågningarna
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Svaren bör vara identiska på grund av samma frö och temperatur=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

I koden ovan har vi:

- Skapat en MCP-klient med en specificerad server-URL.
- Konfigurerat två förfrågningar med samma prompt, fast seed och temperatur noll.
- Skickat båda förfrågningarna och skrivit ut den genererade texten.
- Visat att svaren är identiska tack vare sampling-konfigurationens deterministiska natur (samma seed och temperatur).
- Använt `setSeed` för att ange ett fast slumpfrö, vilket säkerställer att modellen genererar samma resultat för samma input varje gång.
- Satt `temperature` till noll för att säkerställa maximal determinism, vilket betyder att modellen alltid väljer den mest sannolika nästa token utan slumpmässighet.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript-exempel: Deterministiska svar med frökontroll
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Första förfrågan med fast frö
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Noll temperatur för maximal determinism
    });
    
    // Andra förfrågan med samma frö och temperatur
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Tredje förfrågan med annat frö men samma temperatur
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
- Visat att svaren är identiska tack vare sampling-konfigurationens deterministiska natur (samma seed och temperatur).
- Använt `seed` för att ange ett fast slumpfrö, vilket säkerställer att modellen genererar samma output för samma input varje gång.
- Satt `temperature` till noll för att säkerställa maximal determinism, vilket betyder att modellen alltid väljer den mest sannolika nästa token utan slumpmässighet.
- Använt ett annat seed för den tredje förfrågan för att visa att ändring av seed ger olika resultat, även med samma prompt och temperatur.

---

## Dynamisk samplingkonfiguration

Intelligent sampling anpassar parametrar baserat på kontext och krav för varje förfrågan. Det betyder att dynamiskt justera parametrar som temperature, top_p och straff baserat på uppgiftstyp, användarpreferenser eller historisk prestanda.

Låt oss se hur man implementerar dynamisk sampling i olika programmeringsspråk.

# [Python](#tab/python)

```python
# Python Exempel: Dynamisk provtagning baserad på förfrågningskontext
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definiera provtagningsförinställningar för olika uppgiftstyper
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Välj basförinställning
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Justera baserat på användarpreferenser om tillhandahålls
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Skala temperatur baserat på kreativitetspreferens (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Justera top_p baserat på önskad svarsmångfald
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Skapa och skicka förfrågan med anpassade provtagningsparametrar
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Returnera svar med provtagningsmetadata för transparens
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

I koden ovan har vi:

- Skapat en `DynamicSamplingService`-klass som hanterar adaptiv sampling.
- Definierat samplingförinställningar för olika uppgiftstyper (kreativ, faktabaserad, kod, analytisk).
- Vald en bas-samplingförinställning baserat på uppgiftstyp.
- Justerat sampling-parametrarna baserat på användarpreferenser som kreativitet och mångfald.
- Skickat förfrågan med dynamiskt konfigurerade sampling-parametrar.
- Returnerat den genererade texten tillsammans med använda sampling-parametrar och uppgiftstyp för transparens.
- Använt `temperature` för att styra slumpmässigheten i utskriften, där högre värden ger mer kreativa svar.
- Använt `top_p` för att begränsa urvalet av tokens till de som bidrar till den högsta kumulativa sannolikhetsmassan, vilket förbättrar kvaliteten på genererad text.
- Använt `frequency_penalty` för att minska upprepning och uppmuntra mångfald i resultatet.
- Använt `user_preferences` för att tillåta anpassning av sampling-parametrar baserat på användardefinierade nivåer av kreativitet och mångfald.
- Använt `task_type` för att bestämma lämplig samplingstrategi för förfrågan och möjliggöra mer skräddarsydda svar baserat på uppgiftens karaktär.
- Använt `send_request`-metoden för att skicka prompten med konfigurerade sampling-parametrar och säkerställa att modellen genererar text enligt specificerade krav.
- Använt `generated_text` för att hämta modellens svar, som sedan returneras tillsammans med sampling-parametrar och uppgiftstyp för vidare analys eller visning.
- Använt `min` och `max`-funktioner för att säkerställa att användarpreferenser är inom giltiga intervall, vilket förhindrar ogiltiga sampling-konfigurationer.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript-exempel: Dynamisk konfigurationsprovtagning baserat på användarkontext
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Definiera grundläggande provtagningsprofiler
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Spåra historisk prestanda
    this.performanceHistory = [];
  }
  
  // Upptäck uppgiftstyp från prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Enkel heuristisk detektion - kan förbättras med ML-klassificering
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
    
    // Standard till konversation om ingen tydlig typ upptäcks
    return 'conversational';
  }
  
  // Beräkna provtagningsparametrar baserat på kontext och användarpreferenser
  getSamplingParameters(prompt, context = {}) {
    // Upptäck vilken typ av uppgift det är
    const taskType = this.detectTaskType(prompt, context);
    
    // Hämta grundprofil
    let params = {...this.samplingProfiles[taskType]};
    
    // Justera baserat på användarpreferenser
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Skala från 1-10 till lämpligt temperaturområde
        params.temperature = 0.1 + (creativity * 0.09); // 0,1-1,0
      }
      
      if (precision !== undefined) {
        // Högre precision betyder lägre topP (mer fokuserat urval)
        params.topP = 1.0 - (precision * 0.05); // 0,5-1,0
      }
      
      if (consistency !== undefined) {
        // Högre konsekvens betyder lägre straff
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0,1-0,9
      }
    }
    
    // Tillämpa inlärda justeringar från prestandahistorik
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Enkel adaptiv logik - kan förbättras med mer sofistikerade algoritmer
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Ta endast hänsyn till aktuell historik
    
    if (relevantHistory.length > 0) {
      // Beräkna genomsnittliga prestandapoäng
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Om prestanda är under tröskel, justera parametrar
      if (avgScore < 0.7) {
        // Liten justering mot säkrare värden
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Registrera prestanda för framtida justeringar
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 betyg av svarskvalitet
    });
    
    // Begränsa historikstorlek
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Hämta optimerade provtagningsparametrar
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Skicka förfrågan med optimerade parametrar
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Om användaren ger feedback, registrera det för framtida optimering
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

// Exempel på användning
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Kreativ uppgift med egna användarpreferenser
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Hög kreativitet (1-10)
          consistency: 3  // Låg konsekvens (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Kodgenereringsuppgift
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Låg kreativitet
          precision: 8,   // Hög precision
          consistency: 9  // Hög konsekvens
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

- Skapat en `AdaptiveSamplingManager`-klass som hanterar dynamisk sampling baserat på uppgiftstyp och användarpreferenser.
- Definierat samplingprofiler för olika uppgiftstyper (kreativ, faktabaserad, kod, konversationell).
- Implementerat en metod för att upptäcka uppgiftstypen från prompten med hjälp av enkla heuristiker.
- Beräknat sampling-parametrar baserat på upptäckt uppgiftstyp och användarpreferenser.
- Tillämpat inlärda justeringar baserat på historisk prestanda för att optimera sampling-parametrar.
- Registrerat prestanda för framtida justeringar, vilket gör det möjligt för systemet att lära från tidigare interaktioner.
- Skickat förfrågningar med dynamiskt konfigurerade sampling-parametrar och returnerat genererad text tillsammans med använda parametrar och upptäckt uppgiftstyp.
- Använt:
    - `userPreferences` för att tillåta anpassning av sampling-parametrar baserat på användardefinierade nivåer för kreativitet, precision och konsekvens.
    - `detectTaskType` för att avgöra uppgiftens natur baserat på prompten och möjliggöra mer skräddarsydda svar.
    - `recordPerformance` för att logga prestandan för genererade svar, vilket tillåter systemet att anpassa sig och förbättras över tid.
    - `applyLearnedAdjustments` för att modifiera sampling-parametrar baserat på historisk prestanda och förbättra modellens förmåga att generera högkvalitativa svar.
    - `generateResponse` för att kapsla in hela processen att generera ett svar med adaptiv sampling, vilket gör det enkelt att anropa med olika prompts och kontexter.
    - `allowedTools` för att specificera vilka verktyg modellen kan använda under generering, vilket ger mer kontextmedvetna svar.
    - `feedbackScore` för att tillåta användare att ge feedback på kvaliteten på det genererade svaret, vilket kan användas för att ytterligare förfina modellens prestanda över tid.
    - `performanceHistory` för att upprätthålla en historik över tidigare interaktioner, vilket gör det möjligt för systemet att lära av tidigare framgångar och misslyckanden.
    - `getSamplingParameters` för att dynamiskt justera sampling-parametrar baserat på förfrågans kontext, vilket möjliggör ett mer flexibelt och responsivt modellbeteende.
    - `detectTaskType` för att klassificera uppgiften baserat på prompten och möjliggöra att systemet kan tillämpa lämpliga samplingstrategier för olika typer av förfrågningar.
    - `samplingProfiles` för att definiera bas-samplingkonfigurationer för olika uppgiftstyper och möjliggöra snabba justeringar baserat på uppgiftens karaktär.

---

## Vad händer härnäst

- [5.7 Skalning](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->