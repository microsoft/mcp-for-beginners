> [!WARNING]
> Sampling is afgeschaft in MCP `2026-07-28`. Deze les wordt bewaard voor
> legacy-implementaties. Nieuwe servers zouden direct met een LLM
> provider-API moeten integreren.

# Sampling in Model Context Protocol

> Sampling blijft opgenomen in de specificatie van `2026-07-28` voor compatibiliteit en komt
> in aanmerking voor verwijdering in de eerste revisie die wordt uitgebracht op of na 28 juli
> 2027. Voorbeelden in deze les gebruiken mogelijk SDK-API's die `2025-11-25` implementeren.
> Zie [Wat is veranderd in MCP: De specificatie van 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

In legacy MCP-implementaties maakt Sampling het mogelijk dat servers LLM
voltooiingen via de client opvragen. Deze les legt die verouderde protocol
flow uit voor compatibiliteit en migratiewerk.

## Introductie

In deze les verkennen we hoe samplingparameters in MCP-verzoeken geconfigureerd kunnen worden en begrijpen we de onderliggende protocolmechanismen van sampling.

## Leerdoelen

Aan het einde van deze les kun je:

- De belangrijkste samplingparameters in MCP begrijpen.
- Samplingparameters configureren voor verschillende gebruikssituaties.
- Deterministische sampling implementeren voor reproduceerbare resultaten.
- Samplingparameters dynamisch aanpassen op basis van context en gebruikersvoorkeuren.
- Samplingstrategieën toepassen om modelprestaties in diverse scenario's te verbeteren.
- Begrijpen hoe sampling werkt in de client-server flow van MCP.

## Hoe Sampling Werkt in MCP

De samplingflow in MCP volgt deze stappen:

1. Server stuurt een `sampling/createMessage` verzoek naar de client
2. Client bekijkt het verzoek en kan het aanpassen
3. Client sampelt van een LLM
4. Client beoordeelt de voltooiing
5. Client retourneert het resultaat aan de server

Dit ontwerp met mens-in-de-lus zorgt ervoor dat gebruikers controle houden over wat de LLM ziet en genereert.

## Overzicht Samplingparameters

MCP definieert de volgende samplingparameters die in clientverzoeken geconfigureerd kunnen worden:

| Parameter | Beschrijving | Typisch bereik |
|-----------|-------------|---------------|
| `temperature` | Bepaalt de willekeur bij tokenselectie | 0.0 - 1.0 |
| `maxTokens` | Maximaal aantal tokens om te genereren | Integer waarde |
| `stopSequences` | Aangepaste reeksen die generatie stoppen bij tegenkomen | Array van strings |
| `metadata` | Aanvullende provider-specifieke parameters | JSON-object |

Veel LLM-providers ondersteunen extra parameters via het veld `metadata`, waaronder:

| Veelvoorkomende Extensieparameter | Beschrijving | Typisch bereik |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - beperkt tokens tot top cumulatieve waarschijnlijkheid | 0.0 - 1.0 |
| `top_k` | Beperkt tokenselectie tot top K opties | 1 - 100 |
| `presence_penalty` | Straft tokens op basis van hun aanwezigheid tot nu toe | -2.0 - 2.0 |
| `frequency_penalty` | Straft tokens op basis van hun frequentie tot nu toe | -2.0 - 2.0 |
| `seed` | Specifieke random seed voor reproduceerbare resultaten | Integer waarde |

## Voorbeeld Verzoekformaat

Hier is een voorbeeld van een samplingsverzoek van een client in MCP:

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

De client retourneert een voltooiingsresultaat:

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

## Mens in de Lus Bedieningselementen

MCP sampling is ontworpen met menselijke toezicht in gedachten:

- **Voor prompts**:
  - Clients moeten gebruikers de voorgestelde prompt tonen
  - Gebruikers moeten prompts kunnen aanpassen of afwijzen
  - System prompts kunnen worden gefilterd of aangepast
  - Contextinclusie wordt geregeld door de client

- **Voor voltooiingen**:
  - Clients moeten gebruikers de voltooiing tonen
  - Gebruikers moeten voltooiingen kunnen aanpassen of afwijzen
  - Clients kunnen voltooiingen filteren of aanpassen
  - Gebruikers bepalen welke model wordt gebruikt

Met deze principes in gedachten, bekijken we hoe sampling in verschillende programmeertalen geïmplementeerd kan worden, met focus op de parameters die algemeen worden ondersteund door LLM-providers.

## Beveiligingsoverwegingen

Bij het implementeren van sampling in MCP, overweeg de volgende beveiligingspraktijken:

- **Valideer alle berichtinhoud** voordat het naar de client wordt gestuurd
- **Saniteer gevoelige informatie** uit prompts en voltooiingen
- **Implementeer snelheidslimieten** om misbruik te voorkomen
- **Monitor samplinggebruik** voor ongewone patronen
- **Versleutel data tijdens overdracht** met veilige protocollen
- **Behandel gebruikersprivacy** volgens relevante regelgeving
- **Controleer samplingverzoeken** op naleving en veiligheid
- **Beperk kostenblootstelling** met passende limieten
- **Implementeer timeouts** voor samplingverzoeken
- **Behandel model fouten netjes** met gepaste noodoplossingen

Samplingparameters maken het mogelijk het gedrag van taalmodellen fijn af te stemmen om de gewenste balans tussen deterministisch en creatief output te bereiken.

Laten we bekijken hoe we deze parameters in verschillende programmeertalen kunnen configureren.

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

In bovenstaande code hebben we:

- Een MCP-client gemaakt met een specifieke server-URL.
- Een verzoek geconfigureerd met samplingparameters zoals `temperature`, `top_p`, en `top_k`.
- Het verzoek verzonden en de gegenereerde tekst afgedrukt.
- Gebruikt:
    - `allowedTools` om te specificeren welke tools het model mag gebruiken tijdens generatie. In dit geval hebben we de `ideaGenerator` en `marketAnalyzer` tools toegestaan om te helpen bij het genereren van creatieve app-ideeën.
    - `frequencyPenalty` en `presencePenalty` om herhaling en diversiteit in de output te regelen.
    - `temperature` om de willekeur van de output te beheersen, waarbij hogere waarden leiden tot creatievere antwoorden.
    - `top_p` om de selectie van tokens te beperken tot die bijdragen aan de top cumulatieve waarschijnlijkheidsmassa, wat de kwaliteit van de gegenereerde tekst verbetert.
    - `top_k` om het model te beperken tot de top K meest waarschijnlijke tokens, wat kan helpen bij het genereren van coherente antwoorden.
    - `frequencyPenalty` en `presencePenalty` om herhaling te verminderen en diversiteit in de gegenereerde tekst aan te moedigen.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript Voorbeeld: Temperatuur- en Top-P samplingconfiguratie
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialiseer de MCP-client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configureer verzoek met verschillende samplingparameters
  const creativeSampling = {
    temperature: 0.9,    // Hogere temperatuur = meer willekeur/creativiteit
    topP: 0.92,          // Beschouw tokens met top 92% waarschijnlijkheidsmassa
    frequencyPenalty: 0.6, // Verminder herhaling van tokenreeksen
    presencePenalty: 0.4   // Straf tokens die tot nu toe in de tekst zijn verschenen
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lagere temperatuur = meer deterministisch/factueel
    topP: 0.85,          // Iets meer gerichte tokenselectie
    frequencyPenalty: 0.2, // Minimale herhalingsstraf
    presencePenalty: 0.1   // Minimale aanwezigheidsstraf
  };
  
  try {
    // Verstuur twee verzoeken met verschillende samplingconfiguraties
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
- Verzoeken verzonden met deze configuraties, waarbij het model specifieke tools voor elke taak mocht gebruiken.
- De gegenereerde antwoorden afgedrukt om de effecten van verschillende samplingparameters te tonen.
- `allowedTools` gebruikt om te specificeren welke tools het model mag gebruiken tijdens generatie. In dit geval hebben we de `ideaGenerator` en `environmentalImpactTool` voor creatieve taken toegestaan, en `factChecker` en `dataAnalysisTool` voor feitelijke taken.
- `temperature` gebruikt om de willekeur van de output te beheersen, waarbij hogere waarden leiden tot creatievere antwoorden.
- `top_p` gebruikt om de selectie van tokens te beperken tot die bijdragen aan de top cumulatieve waarschijnlijkheidsmassa, wat de kwaliteit van de gegenereerde tekst verbetert.
- `frequencyPenalty` en `presencePenalty` gebruikt om herhaling te verminderen en diversiteit aan te moedigen in de output.
- `top_k` gebruikt om het model te beperken tot de top K meest waarschijnlijke tokens, wat kan helpen bij het genereren van coherente antwoorden.

---

## Deterministische Sampling

Voor toepassingen die consistente output vereisen, zorgt deterministische sampling voor reproduceerbare resultaten. Dit wordt bereikt door een vaste random seed te gebruiken en de temperatuur op nul te zetten.

Hieronder zien we een voorbeeldimplementatie die deterministische sampling in verschillende programmeertalen demonstreert.

# [Java](#tab/java)

```java
// Java Voorbeeld: Deterministische reacties met vaste zaadwaarde
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Gebruik van een vaste zaadwaarde voor deterministische resultaten
        
        // Eerste verzoek met vaste zaadwaarde
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Nul temperatuur voor maximale determinisme
            .build();
            
        // Tweede verzoek met dezelfde zaadwaarde
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Voer beide verzoeken uit
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Reacties zouden identiek moeten zijn vanwege dezelfde zaadwaarde en temperatuur=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

In bovenstaande code hebben we:

- Een MCP-client gemaakt met een opgegeven server-URL.
- Twee verzoeken geconfigureerd met dezelfde prompt, vaste seed en nul temperatuur.
- Beide verzoeken verzonden en de gegenereerde tekst afgedrukt.
- Aangetoond dat de reacties identiek zijn vanwege de deterministische aard van de samplingconfiguratie (zelfde seed en temperatuur).
- `setSeed` gebruikt om een vaste random seed te specificeren, waardoor het model bij dezelfde invoer steeds dezelfde output genereert.
- `temperature` op nul gezet om maximale determinisme te garanderen, wat betekent dat het model altijd de meest waarschijnlijke volgende token kiest zonder willekeur.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript Voorbeeld: Deterministische antwoorden met zaadcontrole
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Eerste verzoek met vaste zaadwaarde
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Nul temperatuur voor maximale determinisme
    });
    
    // Tweede verzoek met dezelfde zaadwaarde en temperatuur
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Derde verzoek met andere zaadwaarde maar dezelfde temperatuur
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
- Twee verzoeken geconfigureerd met dezelfde prompt, vaste seed en nul temperatuur.
- Beide verzoeken verzonden en de gegenereerde tekst afgedrukt.
- Aangetoond dat de reacties identiek zijn vanwege de deterministische aard van de samplingconfiguratie (zelfde seed en temperatuur).
- `seed` gebruikt om een vaste random seed te specificeren, waardoor het model bij dezelfde invoer steeds dezelfde output genereert.
- `temperature` op nul gezet om maximale determinisme te garanderen, wat betekent dat het model altijd de meest waarschijnlijke volgende token kiest zonder willekeur.
- Voor het derde verzoek een andere seed gebruikt om te laten zien dat het wijzigen van de seed resulteert in verschillende outputs, zelfs met dezelfde prompt en temperatuur.

---

## Dynamische Samplingconfiguratie

Intelligente sampling past parameters aan op basis van de context en vereisten van elk verzoek. Dat betekent het dynamisch aanpassen van parameters zoals temperatuur, top_p en straffen, op basis van het type taak, gebruikersvoorkeuren of historische prestaties.

Laten we bekijken hoe dynamische sampling in verschillende programmeertalen geïmplementeerd kan worden.

# [Python](#tab/python)

```python
# Python voorbeeld: Dynamische sampling gebaseerd op de context van het verzoek
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definieer sampleerinstellingen voor verschillende taaktypen
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Selecteer basisvoorinstelling
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Pas aan op basis van gebruikersvoorkeuren indien opgegeven
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Schaal temperatuur op basis van creativiteitsvoorkeur (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Pas top_p aan op basis van gewenste responsdiversiteit
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Maak en verstuur verzoek met aangepaste sampleerparameters
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Retourneer respons met sampleermetadata voor transparantie
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

In bovenstaande code hebben we:

- Een `DynamicSamplingService` klasse gemaakt die adaptieve sampling beheert.
- Samplingpresets gedefinieerd voor verschillende taaktypes (creatief, feitelijk, code, analytisch).
- Een basis samplingpreset geselecteerd op basis van het taaktype.
- De samplingparameters aangepast op basis van gebruikersvoorkeuren, zoals mate van creativiteit en diversiteit.
- Het verzoek verstuurd met de dynamisch geconfigureerde samplingparameters.
- De gegenereerde tekst plus toegepaste samplingparameters en taaktype teruggegeven voor transparantie.
- `temperature` gebruikt om de willekeur van de output te beheersen, waarbij hogere waarden leiden tot creatievere antwoorden.
- `top_p` gebruikt om de selectie van tokens te beperken tot die bijdragen aan de top cumulatieve waarschijnlijkheidsmassa, wat de kwaliteit van gegenereerde tekst verbetert.
- `frequency_penalty` gebruikt om herhaling te verminderen en diversiteit aan te moedigen in de output.
- `user_preferences` gebruikt om de samplingparameters aan te passen op basis van door de gebruiker gedefinieerde niveaus van creativiteit en diversiteit.
- `task_type` gebruikt om de juiste samplingstrategie voor het verzoek te bepalen, waardoor meer op maat gemaakte antwoorden ontstaan gebaseerd op het karakter van de taak.
- De `send_request` methode gebruikt om de prompt te verzenden met de geconfigureerde samplingparameters, zodat het model tekst genereert volgens de opgegeven eisen.
- `generated_text` gebruikt om het antwoord van het model te krijgen, dat vervolgens samen met samplingparameters en taaktype wordt teruggegeven voor verdere analyse of weergave.
- `min` en `max` functies gebruikt om ervoor te zorgen dat gebruikersvoorkeuren binnen geldige grenzen blijven, waardoor ongeldige samplingconfiguraties worden voorkomen.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript Voorbeeld: Dynamische samplingconfiguratie gebaseerd op gebruikerscontext
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Basis samplingprofielen definiëren
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Historische prestaties bijhouden
    this.performanceHistory = [];
  }
  
  // Taaktype detecteren uit prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Eenvoudige heuristische detectie - kan worden verbeterd met ML-classificatie
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
    
    // Standaard naar conversatie als er geen duidelijk type wordt gedetecteerd
    return 'conversational';
  }
  
  // Samplingparameters berekenen op basis van context en gebruikersvoorkeuren
  getSamplingParameters(prompt, context = {}) {
    // Het type taak detecteren
    const taskType = this.detectTaskType(prompt, context);
    
    // Basisprofiel ophalen
    let params = {...this.samplingProfiles[taskType]};
    
    // Aanpassen op basis van gebruikersvoorkeuren
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Schalen van 1-10 naar passende temperatuurbereik
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Hogere precisie betekent lagere topP (meer gerichte selectie)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Hogere consistentie betekent lagere straffen
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Geleerde aanpassingen toepassen vanuit prestatiegeschiedenis
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Eenvoudige adaptieve logica - kan worden verbeterd met meer geavanceerde algoritmen
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Alleen recente geschiedenis overwegen
    
    if (relevantHistory.length > 0) {
      // Gemiddelde prestatie scores berekenen
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Als prestaties onder drempel liggen, parameters aanpassen
      if (avgScore < 0.7) {
        // Kleine aanpassing richting veiligere waarden
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Prestaties registreren voor toekomstige aanpassingen
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 beoordeling van reactiekwaliteit
    });
    
    // Historiegrootte beperken
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Geoptimaliseerde samplingparameters ophalen
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Verzoek verzenden met geoptimaliseerde parameters
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Als gebruiker feedback geeft, deze opnemen voor toekomstige optimalisatie
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

// Voorbeeld gebruik
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Creatieve taak met aangepaste gebruikersvoorkeuren
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Hoge creativiteit (1-10)
          consistency: 3  // Lage consistentie (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Taak code generatie
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Lage creativiteit
          precision: 8,   // Hoge precisie
          consistency: 9  // Hoge consistentie
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
- Aangeleerde aanpassingen toegepast op basis van historische prestaties om samplingparameters te optimaliseren.
- Prestaties vastgelegd voor toekomstige aanpassingen, zodat het systeem kan leren van eerdere interacties.
- Verzoeken verzonden met dynamisch geconfigureerde samplingparameters en de gegenereerde tekst plus toegepaste parameters en gedetecteerd taaktype teruggegeven.
- Gebruikt:
    - `userPreferences` om de samplingparameters aan te passen op basis van door de gebruiker gedefinieerde niveaus van creativiteit, precisie en consistentie.
    - `detectTaskType` om de aard van de taak te bepalen op basis van de prompt, waardoor meer op maat gemaakte antwoorden mogelijk zijn.
    - `recordPerformance` om de prestatie van gegenereerde antwoorden vast te leggen, zodat het systeem zich kan aanpassen en verbeteren in de loop der tijd.
    - `applyLearnedAdjustments` om samplingparameters aan te passen op basis van historische prestaties, waardoor het model beter in staat is kwalitatief hoogwaardige antwoorden te genereren.
    - `generateResponse` om het volledige proces van antwoorden genereren met adaptieve sampling te encapsuleren, zodat het eenvoudig is aan te roepen met verschillende prompts en contexten.
    - `allowedTools` om te specificeren welke tools het model mag gebruiken tijdens generatie, wat contextbewustere antwoorden mogelijk maakt.
    - `feedbackScore` om gebruikers feedback op de kwaliteit van het gegenereerde antwoord te laten geven, die gebruikt kan worden om de prestaties van het model verder te verfijnen.
    - `performanceHistory` om een record bij te houden van eerdere interacties, waardoor het systeem kan leren van successen en fouten uit het verleden.
    - `getSamplingParameters` om samplingparameters dynamisch aan te passen op basis van de context van het verzoek, wat meer flexibele en responsieve modelgedragingen mogelijk maakt.
    - `detectTaskType` om de taak te classificeren op basis van de prompt, zodat het systeem geschikte samplingstrategieën op verschillende typen verzoeken kan toepassen.
    - `samplingProfiles` om basis-samplingconfiguraties te definiëren voor verschillende taaktypes, waardoor snelle aanpassingen mogelijk zijn afhankelijk van het karakter van het verzoek.

---

## Wat volgt

- [5.7 Schalen](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->