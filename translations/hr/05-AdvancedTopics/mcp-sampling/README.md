# Uzorkovanje u Model Context Protocolu

Uzorkovanje je moćna značajka MCP-a koja omogućuje serverima da putem klijenta zatraže LLM dovršetke, omogućujući sofisticirano agentno ponašanje uz održavanje sigurnosti i privatnosti. Prava konfiguracija uzorkovanja može značajno poboljšati kvalitetu i performanse odgovora. MCP pruža standardizirani način kontrole načina na koji modeli generiraju tekst s određenim parametrima koji utječu na nasumičnost, kreativnost i koherentnost.

## Uvod

U ovom ćemo lekciji istražiti kako konfigurirati parametre uzorkovanja u MCP zahtjevima i razumjeti osnovne protokolarne mehanizme uzorkovanja.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Razumjeti ključne parametre uzorkovanja dostupne u MCP-u.
- Konfigurirati parametre uzorkovanja za različite slučajeve upotrebe.
- Implementirati determinističko uzorkovanje za ponovljive rezultate.
- Dinamički prilagođavati parametre uzorkovanja na temelju konteksta i korisničkih preferencija.
- Primijeniti strategije uzorkovanja za poboljšanje performansi modela u različitim scenarijima.
- Razumjeti kako uzorkovanje funkcionira u klijent-server tijeku MCP-a.

## Kako uzorkovanje funkcionira u MCP-u

Tijek uzorkovanja u MCP-u slijedi ove korake:

1. Server šalje `sampling/createMessage` zahtjev klijentu
2. Klijent pregledava zahtjev i može ga izmijeniti
3. Klijent uzorkuje iz LLM-a
4. Klijent pregledava dovršetak
5. Klijent vraća rezultat serveru

Ovaj dizajn s uključenim čovjekom u petlju osigurava da korisnici zadržavaju kontrolu nad onim što LLM vidi i generira.

## Pregled parametara uzorkovanja

MCP definira sljedeće parametre uzorkovanja koje je moguće konfigurirati u zahtjevima klijenta:

| Parametar | Opis | Tipični raspon |
|-----------|-------|---------------|
| `temperature` | Kontrolira nasumičnost u odabiru tokena | 0.0 - 1.0 |
| `maxTokens` | Maksimalan broj tokena za generiranje | Cijeli broj |
| `stopSequences` | Prilagođene sekvence koje zaustavljaju generiranje kad se pojave | Niz stringova |
| `metadata` | Dodatni parametri specifični za pružatelja usluge | JSON objekt |

Mnogi LLM pružatelji podržavaju dodatne parametre kroz polje `metadata`, što može uključivati:

| Uobičajeni dodatni parametar | Opis | Tipični raspon |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - ograničava tokene na one s najvećom kumulativnom vjerojatnošću | 0.0 - 1.0 |
| `top_k` | Ograničava odabir tokena na top K opcija | 1 - 100 |
| `presence_penalty` | Penalizira tokene na temelju njihove prisutnosti u tekstu do sada | -2.0 - 2.0 |
| `frequency_penalty` | Penalizira tokene na temelju njihove učestalosti u tekstu do sada | -2.0 - 2.0 |
| `seed` | Specifični slučajni seed za ponovljive rezultate | Cijeli broj |

## Primjer formata zahtjeva

Evo primjera zahtjeva za uzorkovanje od klijenta u MCP-u:

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

Klijent vraća rezultat dovršetka:

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

## Kontrole s uključenim čovjekom u petlju

MCP uzorkovanje je dizajnirano s nadzorom čovjeka na umu:

- **Za upite (prompts)**:
  - Klijenti bi trebali prikazati korisnicima predloženi upit
  - Korisnici bi trebali moći mijenjati ili odbiti upite
  - Sistemski upiti mogu se filtrirati ili mijenjati
  - Uključivanje konteksta kontrolira klijent

- **Za dovršetke (completions)**:
  - Klijenti bi trebali prikazati korisnicima dovršetak
  - Korisnici bi trebali moći mijenjati ili odbiti dovršetke
  - Klijenti mogu filtrirati ili mijenjati dovršetke
  - Korisnici kontroliraju koji se model koristi

S ovim principima na umu, pogledajmo kako implementirati uzorkovanje u različitim programskim jezicima, fokusirajući se na parametre koje većina LLM pružatelja podržava.

## Sigurnosne napomene

Prilikom implementacije uzorkovanja u MCP-u, razmotrite sljedeće sigurnosne preporuke:

- **Validirajte sav sadržaj poruka** prije slanja klijentu
- **Očistite osjetljive informacije** iz upita i dovršetaka
- **Implementirajte ograničenja brzine** kako biste spriječili zloupotrebu
- **Nadzor uzorkovanja** za neuobičajene obrasce
- **Šifrirajte podatke u prijenosu** koristeći sigurne protokole
- **Postupajte s privatnošću korisničkih podataka** u skladu s relevantnim propisima
- **Revizija zahtjeva za uzorkovanje** radi usklađenosti i sigurnosti
- **Kontrolirajte izloženost troškovima** s odgovarajućim ograničenjima
- **Implementirajte vremenska ograničenja** za zahtjeve uzorkovanja
- **Rukujte pogreškama modela** na prikladan način s rezervnim opcijama

Parametri uzorkovanja omogućuju fino podešavanje ponašanja jezičnih modela kako bi se postigla željena ravnoteža između determinističkih i kreativnih izlaza.

Pogledajmo kako konfigurirati ove parametre u različitim programskim jezicima.

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

U prethodnom kodu smo:

- Kreirali MCP klijenta s određenim URL-om servera.
- Konfigurirali zahtjev s parametrima uzorkovanja poput `temperature`, `top_p` i `top_k`.
- Poslali zahtjev i ispisali generirani tekst.
- Koristili:
    - `allowedTools` za specificiranje alata koje model može koristiti tijekom generiranja. U ovom slučaju, dozvolili smo alate `ideaGenerator` i `marketAnalyzer` za pomoć u generiranju kreativnih ideja za aplikacije.
    - `frequencyPenalty` i `presencePenalty` za kontrolu ponavljanja i raznolikosti u izlazu.
    - `temperature` za kontrolu nasumičnosti izlaza, gdje veće vrijednosti vode do kreativnijih odgovora.
    - `top_p` za ograničavanje odabira tokena na one koji doprinose najvećoj kumulativnoj vjerojatnosti, čime se poboljšava kvaliteta generiranog teksta.
    - `top_k` za ograničavanje modela na top K najvjerojatnijih tokena, što može pomoći u generiranju koherentnijih odgovora.
    - `frequencyPenalty` i `presencePenalty` za smanjenje ponavljanja i poticanje raznolikosti u generiranom tekstu.

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

U prethodnom kodu smo:

- Inicijalizirali MCP klijenta s URL-om servera i API ključem.
- Konfigurirali dva seta parametara uzorkovanja: jedan za kreativne zadatke, drugi za faktualne zadatke.
- Poslali zahtjeve s tim konfiguracijama, dopuštajući modelu korištenje specifičnih alata za svaki zadatak.
- Ispisali generirane odgovore kako bismo pokazali učinke različitih parametara uzorkovanja.
- Koristili `allowedTools` za specificiranje alata koje model može koristiti tijekom generiranja. U ovom slučaju, dozvolili smo `ideaGenerator` i `environmentalImpactTool` za kreativne zadatke, te `factChecker` i `dataAnalysisTool` za faktualne zadatke.
- Koristili `temperature` za kontrolu nasumičnosti izlaza, gdje veće vrijednosti vode do kreativnijih odgovora.
- Koristili `top_p` za ograničavanje odabira tokena na one koji doprinose najvećoj kumulativnoj vjerojatnosti, čime se poboljšava kvaliteta generiranog teksta.
- Koristili `frequencyPenalty` i `presencePenalty` za smanjenje ponavljanja i poticanje raznolikosti u izlazu.
- Koristili `top_k` za ograničavanje modela na top K najvjerojatnijih tokena, što može pomoći u generiranju koherentnijih odgovora.

---

## Determinističko uzorkovanje

Za aplikacije koje zahtijevaju konzistentne izlaze, determinističko uzorkovanje osigurava ponovljive rezultate. To se postiže korištenjem fiksnog slučajnog seeda i postavljanjem temperature na nulu.

Pogledajmo donji primjer implementacije koji demonstrira determinističko uzorkovanje u različitim programskim jezicima.

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

U prethodnom kodu smo:

- Kreirali MCP klijenta s određenim URL-om servera.
- Konfigurirali dva zahtjeva s istim upitom, fiksnim seedom i temperaturom postavljenom na nulu.
- Poslali oba zahtjeva i ispisali generirani tekst.
- Pokazali da su odgovori identični zbog determinističke prirode konfiguracije uzorkovanja (isti seed i temperatura).
- Koristili `setSeed` za specificiranje fiksnog slučajnog seeda, osiguravajući da model uvijek generira isti izlaz za isti ulaz.
- Postavili `temperature` na nulu kako bismo osigurali maksimalnu determinističnost, što znači da će model uvijek odabrati najvjerojatniji sljedeći token bez nasumičnosti.

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

U prethodnom kodu smo:

- Inicijalizirali MCP klijenta s URL-om servera.
- Konfigurirali dva zahtjeva s istim upitom, fiksnim seedom i temperaturom postavljenom na nulu.
- Poslali oba zahtjeva i ispisali generirani tekst.
- Pokazali da su odgovori identični zbog determinističke prirode konfiguracije uzorkovanja (isti seed i temperatura).
- Koristili `seed` za specificiranje fiksnog slučajnog seeda, osiguravajući da model uvijek generira isti izlaz za isti ulaz.
- Postavili `temperature` na nulu kako bismo osigurali maksimalnu determinističnost, što znači da će model uvijek odabrati najvjerojatniji sljedeći token bez nasumičnosti.
- Koristili drugačiji seed za treći zahtjev kako bismo pokazali da promjena seeda rezultira različitim izlazima, čak i s istim upitom i temperaturom.

---

## Dinamička konfiguracija uzorkovanja

Inteligentno uzorkovanje prilagođava parametre na temelju konteksta i zahtjeva svakog zahtjeva. To znači dinamičko podešavanje parametara poput temperature, top_p i penalizacija na temelju vrste zadatka, korisničkih preferencija ili povijesnih performansi.

Pogledajmo kako implementirati dinamičko uzorkovanje u različitim programskim jezicima.

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

U prethodnom kodu smo:

- Kreirali klasu `DynamicSamplingService` koja upravlja adaptivnim uzorkovanjem.
- Definirali predloške uzorkovanja za različite vrste zadataka (kreativni, faktualni, kod, analitički).
- Odabrali osnovni predložak uzorkovanja na temelju vrste zadatka.
- Prilagodili parametre uzorkovanja na temelju korisničkih preferencija, poput razine kreativnosti i raznolikosti.
- Poslali zahtjev s dinamički konfiguriranim parametrima uzorkovanja.
- Vratili generirani tekst zajedno s primijenjenim parametrima uzorkovanja i vrstom zadatka radi transparentnosti.
- Koristili `temperature` za kontrolu nasumičnosti izlaza, gdje veće vrijednosti vode do kreativnijih odgovora.
- Koristili `top_p` za ograničavanje odabira tokena na one koji doprinose najvećoj kumulativnoj vjerojatnosti, čime se poboljšava kvaliteta generiranog teksta.
- Koristili `frequency_penalty` za smanjenje ponavljanja i poticanje raznolikosti u izlazu.
- Koristili `user_preferences` za prilagodbu parametara uzorkovanja na temelju korisnički definiranih razina kreativnosti i raznolikosti.
- Koristili `task_type` za određivanje odgovarajuće strategije uzorkovanja za zahtjev, omogućujući prilagođenije odgovore ovisno o prirodi zadatka.
- Koristili metodu `send_request` za slanje upita s konfiguriranim parametrima uzorkovanja, osiguravajući da model generira tekst prema specificiranim zahtjevima.
- Koristili `generated_text` za dohvat odgovora modela, koji se zatim vraća zajedno s parametrima uzorkovanja i vrstom zadatka za daljnju analizu ili prikaz.
- Koristili funkcije `min` i `max` kako bismo osigurali da su korisničke preferencije unutar valjanih granica, sprječavajući nevažeće konfiguracije uzorkovanja.

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

U prethodnom kodu smo:

- Kreirali klasu `AdaptiveSamplingManager` koja upravlja dinamičkim uzorkovanjem na temelju vrste zadatka i korisničkih preferencija.
- Definirali profile uzorkovanja za različite vrste zadataka (kreativni, faktualni, kod, konverzacijski).
- Implementirali metodu za detekciju vrste zadatka iz upita koristeći jednostavne heuristike.
- Izračunali parametre uzorkovanja na temelju detektirane vrste zadatka i korisničkih preferencija.
- Primijenili naučene prilagodbe na temelju povijesnih performansi za optimizaciju parametara uzorkovanja.
- Evidentirali performanse za buduće prilagodbe, omogućujući sustavu učenje iz prošlih interakcija.
- Poslali zahtjeve s dinamički konfiguriranim parametrima uzorkovanja i vratili generirani tekst zajedno s primijenjenim parametrima i detektiranom vrstom zadatka.
- Koristili:
    - `userPreferences` za prilagodbu parametara uzorkovanja na temelju korisnički definiranih razina kreativnosti, preciznosti i konzistentnosti.
    - `detectTaskType` za određivanje prirode zadatka na temelju upita, omogućujući prilagođenije odgovore.
    - `recordPerformance` za evidentiranje performansi generiranih odgovora, što omogućuje sustavu prilagodbu i poboljšanje tijekom vremena.
    - `applyLearnedAdjustments` za izmjenu parametara uzorkovanja na temelju povijesnih performansi, poboljšavajući sposobnost modela da generira kvalitetne odgovore.
    - `generateResponse` za obuhvaćanje cijelog procesa generiranja odgovora s adaptivnim uzorkovanjem, olakšavajući pozivanje s različitim upitima i kontekstima.
    - `allowedTools` za specificiranje alata koje model može koristiti tijekom generiranja, omogućujući kontekstualnije odgovore.
    - `feedbackScore` za omogućavanje korisnicima da daju povratnu informaciju o kvaliteti generiranog odgovora, što se može koristiti za daljnje usavršavanje performansi modela.
    - `performanceHistory` za održavanje evidencije prošlih interakcija, omogućujući sustavu učenje iz prethodnih uspjeha i neuspjeha.
    - `getSamplingParameters` za dinamičko prilagođavanje parametara uzorkovanja na temelju konteksta zahtjeva, omogućujući fleksibilnije i responzivnije ponašanje modela.
    - `detectTaskType` za klasifikaciju zadatka na temelju upita, omogućujući sustavu primjenu odgovarajućih strategija uzorkovanja za različite vrste zahtjeva.
    - `samplingProfiles` za definiranje osnovnih konfiguracija uzorkovanja za različite vrste zadataka, omogućujući brze prilagodbe ovisno o prirodi zahtjeva.

---

## Što slijedi

- [5.7 Skaliranje](../mcp-scaling/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.