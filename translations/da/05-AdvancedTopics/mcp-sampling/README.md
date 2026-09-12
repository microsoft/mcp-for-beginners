> [!WARNING]
> Sampling er forældet i MCP `2026-07-28`. Denne lektion bevares til
> ældre implementeringer. Nye servere bør integrere direkte med en LLM
> leverandør API.

# Sampling i Model Context Protocol

> Sampling forbliver i `2026-07-28` specifikationen for kompatibilitet og er
> berettiget til fjernelse i den første revision udgivet på eller efter den 28. juli,
> 2027. Eksempler i denne lektion kan bruge SDK API'er, der implementerer `2025-11-25`.
> Se [Hvad er ændret i MCP: Specifikationen 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

I ældre MCP-implementeringer tillader Sampling servere at anmode om LLM
fullføringer gennem klienten. Denne lektion forklarer denne forældede protokol
flow for kompatibilitet og migrationsarbejde.

## Introduktion

I denne lektion vil vi udforske, hvordan man konfigurerer samplingparametre i MCP-forespørgsler og forstå de underliggende protokolmekanismer for sampling.

## Læringsmål

Ved slutningen af denne lektion vil du kunne:

- Forstå de vigtigste samplingparametre tilgængelige i MCP.
- Konfigurere samplingparametre for forskellige anvendelsestilfælde.
- Implementere deterministisk sampling for reproducerbare resultater.
- Justere samplingparametre dynamisk baseret på kontekst og brugerpræferencer.
- Anvende samplingstrategier for at forbedre modelpræstation i forskellige scenarier.
- Forstå, hvordan sampling fungerer i klient-server flow i MCP.

## Hvordan Sampling Fungerer i MCP

Samplingflowet i MCP følger disse trin:

1. Server sender en `sampling/createMessage` forespørgsel til klienten
2. Klienten gennemgår forespørgslen og kan ændre den
3. Klienten samplere fra en LLM
4. Klienten gennemgår completion
5. Klienten returnerer resultatet til serveren

Dette design med mennesket i løkken sikrer, at brugere bevarer kontrol over, hvad LLM’en ser og genererer.

## Oversigt over Samplingparametre

MCP definerer følgende samplingparametre, som kan konfigureres i klientforespørgsler:

| Parameter | Beskrivelse | Typisk Interval |
|-----------|-------------|---------------|
| `temperature` | Styrer tilfældighed i tokenudvælgelse | 0.0 - 1.0 |
| `maxTokens` | Maksimalt antal tokens, der genereres | Heltal |
| `stopSequences` | Egen-definerede sekvenser, der stopper genereringen, når de optræder | Array af strenge |
| `metadata` | Yderligere leverandørspecifikke parametre | JSON objekt |

Mange LLM-leverandører understøtter yderligere parametre via `metadata` feltet, som kan inkludere:

| Almindelig Udvidelsesparameter | Beskrivelse | Typisk Interval |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - begrænser tokens til top kumulativ sandsynlighed | 0.0 - 1.0 |
| `top_k` | Begrænser tokenudvælgelsen til top K muligheder | 1 - 100 |
| `presence_penalty` | Straffer tokens baseret på deres tilstedeværelse i teksten indtil nu | -2.0 - 2.0 |
| `frequency_penalty` | Straffer tokens baseret på deres frekvens i teksten indtil nu | -2.0 - 2.0 |
| `seed` | Specifik tilfældig seed for reproducerbare resultater | Heltal |

## Eksempel på Forespørgselsformat

Her er et eksempel på at anmode om sampling fra en klient i MCP:

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

Klienten returnerer et resultat som completion:

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

## Mennesket i Løkken Kontroller

MCP sampling er designet med menneskelig overvågning i tankerne:

- **For prompts**:
  - Klienter bør vise brugere det foreslåede prompt
  - Brugere bør kunne ændre eller afvise prompts
  - Systemprompts kan filtreres eller ændres
  - Kontekstinklusion styres af klienten

- **For completions**:
  - Klienter bør vise brugere completion
  - Brugere bør kunne ændre eller afvise completions
  - Klienter kan filtrere eller ændre completions
  - Brugere kontrollerer hvilken model, der anvendes

Med disse principper i tankerne, lad os se på, hvordan man implementerer sampling i forskellige programmeringssprog med fokus på de parametre, der almindeligvis understøttes på tværs af LLM-leverandører.

## Sikkerhedsovervejelser

Når sampling implementeres i MCP, skal følgende sikkerhedspraksis overvejes:

- **Valider alt beskedindhold** inden det sendes til klienten
- **Rens følsomme oplysninger** fra prompts og completions
- **Implementer ratebegrænsninger** for at forhindre misbrug
- **Overvåg samplingbrug** for usædvanlige mønstre
- **Krypter data under overførsel** ved brug af sikre protokoller
- **Håndter brugerens dataprivatliv** i overensstemmelse med relevante regler
- **Audit sampling-forespørgsler** for compliance og sikkerhed
- **Kontroller omkostningseksponering** med passende begrænsninger
- **Implementer timeouts** for sampling-forespørgsler
- **Håndter model-fejl yndefuldt** med passende fallback-mekanismer

Samplingparametre tillader finjustering af sprogmodel-adfærden for at opnå den ønskede balance mellem deterministiske og kreative output.

Lad os se på, hvordan man konfigurerer disse parametre i forskellige programmeringssprog.

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

I den foregående kode har vi:

- Oprettet en MCP-klient med en specifik server-URL.
- Konfigureret en forespørgsel med samplingparametre som `temperature`, `top_p` og `top_k`.
- Sendt forespørgslen og udskrevet den genererede tekst.
- Brugte:
    - `allowedTools` til at specificere hvilke værktøjer modellen kan bruge under genereringen. I dette tilfælde tillod vi `ideaGenerator` og `marketAnalyzer` værktøjerne til at assistere med at generere kreative app-idéer.
    - `frequencyPenalty` og `presencePenalty` til at styre gentagelse og mangfoldighed i outputtet.
    - `temperature` til at kontrollere tilfældigheden i output, hvor højere værdier fører til mere kreative svar.
    - `top_p` til at begrænse udvælgelsen af tokens til dem, som bidrager til det øverste kumulative sandsynlighedsmængde, hvilket forbedrer kvaliteten af den genererede tekst.
    - `top_k` til at begrænse modellen til de top K mest sandsynlige tokens, hvilket kan hjælpe med at generere mere sammenhængende svar.
    - `frequencyPenalty` og `presencePenalty` til at reducere gentagelse og fremme mangfoldighed i den genererede tekst.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript-eksempel: Temperatur- og Top-P-prøveudtagningskonfiguration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialiser MCP-klienten
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Konfigurer forespørgsel med forskellige prøveudtagningsparametre
  const creativeSampling = {
    temperature: 0.9,    // Højere temperatur = mere tilfældighed/kreativitet
    topP: 0.92,          // Overvej tokens med top 92 % sandsynlighedsmængde
    frequencyPenalty: 0.6, // Reducer gentagelse af token-sekvenser
    presencePenalty: 0.4   // Straf tokens, der er optrådt i teksten indtil videre
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lavere temperatur = mere deterministisk/faktuel
    topP: 0.85,          // Lidt mere fokuseret token-udvælgelse
    frequencyPenalty: 0.2, // Minimal gentagelsesstraf
    presencePenalty: 0.1   // Minimal tilstedeværelsesstraf
  };
  
  try {
    // Send to forespørgsler med forskellige prøveudtagningskonfigurationer
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
- Konfigureret to sæt samplingparametre: ét til kreative opgaver og et andet til faktuelle opgaver.
- Sendt forespørgsler med disse konfigurationer, som tillader modellen at bruge specifikke værktøjer for hver opgave.
- Udskrevet de genererede svar for at demonstrere effekten af forskellige samplingparametre.
- Brugte `allowedTools` til at specificere hvilke værktøjer modellen kan bruge under genereringen. I dette tilfælde tillod vi `ideaGenerator` og `environmentalImpactTool` til kreative opgaver, og `factChecker` og `dataAnalysisTool` til faktuelle opgaver.
- Brugte `temperature` til at kontrollere tilfældigheden i output, hvor højere værdier fører til mere kreative svar.
- Brugte `top_p` til at begrænse udvælgelsen af tokens til dem, som bidrager til det øverste kumulative sandsynlighedsmængde, hvilket forbedrer kvaliteten af den genererede tekst.
- Brugte `frequencyPenalty` og `presencePenalty` til at reducere gentagelse og fremme mangfoldighed i output.
- Brugte `top_k` til at begrænse modellen til de top K mest sandsynlige tokens, hvilket kan hjælpe med at generere mere sammenhængende svar.

---

## Deterministisk Sampling

For applikationer, der kræver konsistente output, sikrer deterministisk sampling reproducerbare resultater. Det gør den ved at bruge en fast tilfældig seed og sætte temperaturen til nul.

Lad os se på nedenstående eksempel-implementering for at demonstrere deterministisk sampling i forskellige programmeringssprog.

# [Java](#tab/java)

```java
// Java eksempel: Deterministiske svar med fast seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Brug af fast seed for deterministiske resultater
        
        // Første forespørgsel med fast seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Temperatur nul for maksimal determinisme
            .build();
            
        // Anden forespørgsel med samme seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Udfør begge forespørgsler
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Svarene skal være identiske på grund af samme seed og temperatur=0
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
- Demonstreret at svarene er identiske på grund af den deterministiske karakter af samplingkonfigurationen (samme seed og temperatur).
- Brugte `setSeed` for at angive en fast tilfældig seed, hvilket sikrer modellen genererer samme output for samme input hver gang.
- Sat `temperature` til nul for at sikre maksimal determinisme, således at modellen altid vælger den mest sandsynlige næste token uden tilfældighed.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript Eksempel: Deterministiske svar med styring af frø
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Første anmodning med fast frø
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Nul temperatur for maksimal determinisme
    });
    
    // Anden anmodning med samme frø og temperatur
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Tredje anmodning med forskelligt frø men samme temperatur
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
- Demonstreret at svarene er identiske på grund af den deterministiske karakter af samplingkonfigurationen (samme seed og temperatur).
- Brugte `seed` for at angive en fast tilfældig seed, hvilket sikrer modellen genererer samme output for samme input hver gang.
- Sat `temperature` til nul for at sikre maksimal determinisme, således at modellen altid vælger den mest sandsynlige næste token uden tilfældighed.
- Brugte en anden seed for den tredje forespørgsel for at vise, at ændring af seed resulterer i forskellige output, selv med samme prompt og temperatur.

---

## Dynamisk Sampling Konfiguration

Intelligent sampling tilpasser parametre baseret på konteksten og kravene i hver forespørgsel. Det vil sige dynamisk justering af parametre som temperature, top_p og strafparametre baseret på opgavetype, brugerpræferencer eller historisk præstation.

Lad os se på, hvordan man implementerer dynamisk sampling i forskellige programmeringssprog.

# [Python](#tab/python)

```python
# Python-eksempel: Dynamisk sampling baseret på anmodningskontekst
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definér sampleforudindstillinger for forskellige opgavetyper
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Vælg grundlæggende forudindstilling
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Juster baseret på brugerpræferencer, hvis angivet
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Skaler temperatur baseret på præference for kreativitet (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Juster top_p baseret på ønsket svardiversitet
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Opret og send anmodning med brugerdefinerede sampleparametre
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Returnér svar med samplemetadata for gennemsigtighed
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

I den foregående kode har vi:

- Oprettet en `DynamicSamplingService` klasse, der styrer adaptiv sampling.
- Defineret sampling presets for forskellige opgavetyper (kreativ, faktuel, kode, analytisk).
- Valgt et basis sampling preset baseret på opgavetypen.
- Justeret samplingparametrene baseret på brugerpræferencer såsom kreativitet og diversitet.
- Sendt forespørgslen med de dynamisk konfigurerede samplingparametre.
- Returneret den genererede tekst sammen med anvendte samplingparametre og opgavetype for gennemsigtighed.
- Brugte `temperature` til at styre tilfældigheden i output, hvor højere værdier fører til mere kreative svar.
- Brugte `top_p` til at begrænse udvælgelsen af tokens til dem, som bidrager til det øverste kumulative sandsynlighedsmængde, hvilket forbedrer kvaliteten af den genererede tekst.
- Brugte `frequency_penalty` til at reducere gentagelse og fremme mangfoldighed i output.
- Brugte `user_preferences` til at tillade tilpasning af samplingparametre baseret på brugerdefinerede niveauer af kreativitet og diversitet.
- Brugte `task_type` til at bestemme den passende samplingstrategi for forespørgslen, hvilket tillader mere skræddersyede svar baseret på opgavens natur.
- Brugte `send_request` metoden til at sende prompten med de konfigurerede samplingparametre, hvilket sikrer at modellen genererer tekst ifølge de specificerede krav.
- Brugte `generated_text` til at hente modellens svar, som derefter returneres sammen med samplingparametre og opgavetype til yderligere analyse eller visning.
- Brugte `min` og `max` funktioner til at sikre, at brugerpræferencer holdes inden for gyldige intervaller, hvilket forhindrer ugyldige samplingkonfigurationer.

# [JavaScript Dynamisk](#tab/javascript-dynamic)

```javascript
// JavaScript Eksempel: Dynamisk prøveudtagningskonfiguration baseret på brugerens kontekst
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Definer grundlæggende prøveudtagningsprofiler
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Spor historisk ydeevne
    this.performanceHistory = [];
  }
  
  // Registrer opgavetype ud fra prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Simpel heuristisk detektion - kan forbedres med ML-klassificering
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
    
    // Standard til samtale, hvis ingen klar type detekteres
    return 'conversational';
  }
  
  // Beregn prøveudtagningsparametre baseret på kontekst og brugerpræferencer
  getSamplingParameters(prompt, context = {}) {
    // Registrer opgavetype
    const taskType = this.detectTaskType(prompt, context);
    
    // Få grundprofil
    let params = {...this.samplingProfiles[taskType]};
    
    // Juster baseret på brugerpræferencer
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Skaler fra 1-10 til passende temperaturinterval
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Højere præcision betyder lavere topP (mere fokuseret udvælgelse)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Højere konsistens betyder lavere straffe
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Anvend lærte justeringer fra præstationshistorik
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Simpel adaptiv logik - kan forbedres med mere sofistikerede algoritmer
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Overvej kun nylig historie
    
    if (relevantHistory.length > 0) {
      // Beregn gennemsnitlige præstationsscore
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Hvis præstation er under tærsklen, juster parametre
      if (avgScore < 0.7) {
        // Let justering hen imod sikrere værdier
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Registrer præstation til fremtidige justeringer
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 vurdering af svar kvalitet
    });
    
    // Begræns størrelsen på historikken
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Få optimerede prøveudtagningsparametre
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Send forespørgsel med optimerede parametre
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Hvis bruger giver feedback, registrer den til fremtidig optimering
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

// Eksempel på anvendelse
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Kreativ opgave med brugerdefinerede præferencer
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Høj kreativitet (1-10)
          consistency: 3  // Lav konsistens (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Opgave med kodegenerering
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Lav kreativitet
          precision: 8,   // Høj præcision
          consistency: 9  // Høj konsistens
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

- Oprettet en `AdaptiveSamplingManager` klasse, der styrer dynamisk sampling baseret på opgavetype og brugerpræferencer.
- Defineret samplingprofiler for forskellige opgavetyper (kreativ, faktuel, kode, konverserende).
- Implementeret en metode til at opdage opgavetypen fra prompten ved hjælp af simple heuristikker.
- Beregnet samplingparametre baseret på den opdagede opgavetype og brugerpræferencer.
- Anvendt lærte justeringer baseret på historiske præstationer for at optimere samplingparametrene.
- Registreret præstation for fremtidige justeringer, hvilket tillader systemet at lære af tidligere interaktioner.
- Sendt forespørgsler med dynamisk konfigurerede samplingparametre og returneret genereret tekst sammen med anvendte parametre og opdaget opgavetype.
- Brugte:
    - `userPreferences` til at tillade tilpasning af samplingparametre baseret på brugerdefinerede niveauer af kreativitet, præcision og konsistens.
    - `detectTaskType` til at bestemme opgavens natur baseret på prompten, hvilket tillader mere skræddersyede svar.
    - `recordPerformance` til at logge præstationen af genererede svar, hvilket gør systemet i stand til at tilpasse og forbedre over tid.
    - `applyLearnedAdjustments` til at ændre samplingparametre baseret på historisk præstation, hvilket forbedrer modellens evne til at generere svar af høj kvalitet.
    - `generateResponse` til at indkapsle hele processen med at generere et svar med adaptiv sampling, hvilket gør det nemt at kalde med forskellige prompts og kontekster.
    - `allowedTools` til at specificere hvilke værktøjer modellen kan bruge under generering, hvilket tillader mere kontekstbevidste svar.
    - `feedbackScore` til at tillade brugere at give feedback på kvaliteten af det genererede svar, som kan bruges til yderligere at forbedre modellens præstation over tid.
    - `performanceHistory` til at opretholde en log over tidligere interaktioner, så systemet kan lære af tidligere succeser og fejl.
    - `getSamplingParameters` til dynamisk at justere samplingparametre baseret på konteksten i forespørgslen, hvilket tillader mere fleksibel og responsiv modeladfærd.
    - `detectTaskType` til at klassificere opgaven baseret på prompten, hvilket gør systemet i stand til at anvende passende samplingstrategier for forskellige typer forespørgsler.
    - `samplingProfiles` til at definere basis samplingkonfigurationer for forskellige opgavetyper, hvilket tillader hurtige justeringer baseret på forespørgslens natur.

---

## Hvad er det næste

- [5.7 Skalering](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->