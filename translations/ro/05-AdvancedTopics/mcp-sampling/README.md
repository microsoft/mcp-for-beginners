# Sampling în Protocolul Model Context

Sampling-ul este o funcționalitate puternică a MCP care permite serverelor să solicite completări LLM prin client, facilitând comportamente agentice sofisticate, menținând în același timp securitatea și confidențialitatea. Configurarea corectă a sampling-ului poate îmbunătăți semnificativ calitatea răspunsurilor și performanța. MCP oferă o metodă standardizată de a controla modul în care modelele generează text, prin parametri specifici care influențează aleatorietatea, creativitatea și coerența.

## Introducere

În această lecție, vom explora cum să configurăm parametrii de sampling în cererile MCP și să înțelegem mecanismele de bază ale protocolului de sampling.

## Obiective de învățare

La finalul acestei lecții, vei putea:

- Înțelege principalii parametri de sampling disponibili în MCP.
- Configura parametrii de sampling pentru diferite cazuri de utilizare.
- Implementa sampling determinist pentru rezultate reproductibile.
- Ajusta dinamic parametrii de sampling în funcție de context și preferințele utilizatorului.
- Aplica strategii de sampling pentru a îmbunătăți performanța modelului în diverse scenarii.
- Înțelege cum funcționează sampling-ul în fluxul client-server al MCP.

## Cum funcționează Sampling-ul în MCP

Fluxul de sampling în MCP urmează acești pași:

1. Serverul trimite o cerere `sampling/createMessage` către client
2. Clientul analizează cererea și poate să o modifice
3. Clientul realizează sampling-ul dintr-un LLM
4. Clientul verifică completarea
5. Clientul returnează rezultatul către server

Acest design cu om în buclă asigură că utilizatorii păstrează controlul asupra a ceea ce vede și generează LLM-ul.

## Prezentare generală a parametrilor de sampling

MCP definește următorii parametri de sampling care pot fi configurați în cererile clientului:

| Parametru | Descriere | Interval tipic |
|-----------|-----------|---------------|
| `temperature` | Controlează aleatorietatea în selecția tokenilor | 0.0 - 1.0 |
| `maxTokens` | Numărul maxim de tokeni de generat | Valoare întreagă |
| `stopSequences` | Secvențe personalizate care opresc generarea când sunt întâlnite | Array de stringuri |
| `metadata` | Parametri suplimentari specifici furnizorului | Obiect JSON |

Mulți furnizori LLM suportă parametri adiționali prin câmpul `metadata`, care pot include:

| Parametru Extensie Comun | Descriere | Interval tipic |
|-------------------------|-----------|----------------|
| `top_p` | Sampling nucleu - limitează tokenii la probabilitatea cumulativă de top | 0.0 - 1.0 |
| `top_k` | Limitează selecția tokenilor la primele K opțiuni | 1 - 100 |
| `presence_penalty` | Penalizează tokenii în funcție de prezența lor în textul generat până acum | -2.0 - 2.0 |
| `frequency_penalty` | Penalizează tokenii în funcție de frecvența lor în textul generat până acum | -2.0 - 2.0 |
| `seed` | Seed aleator fix pentru rezultate reproductibile | Valoare întreagă |

## Exemplu de format al cererii

Iată un exemplu de cerere pentru sampling de la un client în MCP:

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

## Formatul răspunsului

Clientul returnează un rezultat de completare:

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

## Controlul cu om în buclă

Sampling-ul MCP este conceput cu supraveghere umană în minte:

- **Pentru prompturi**:
  - Clienții ar trebui să afișeze utilizatorilor promptul propus
  - Utilizatorii ar trebui să poată modifica sau respinge prompturile
  - Prompturile de sistem pot fi filtrate sau modificate
  - Includerea contextului este controlată de client

- **Pentru completări**:
  - Clienții ar trebui să afișeze utilizatorilor completarea
  - Utilizatorii ar trebui să poată modifica sau respinge completările
  - Clienții pot filtra sau modifica completările
  - Utilizatorii controlează ce model este folosit

Având aceste principii în vedere, să vedem cum să implementăm sampling în diferite limbaje de programare, concentrându-ne pe parametrii susținuți în mod obișnuit de furnizorii LLM.

## Considerații de securitate

Când implementezi sampling în MCP, ia în considerare următoarele bune practici de securitate:

- **Validează tot conținutul mesajelor** înainte de a le trimite clientului
- **Curăță informațiile sensibile** din prompturi și completări
- **Implementează limite de rată** pentru a preveni abuzurile
- **Monitorizează utilizarea sampling-ului** pentru tipare neobișnuite
- **Criptează datele în tranzit** folosind protocoale sigure
- **Gestionează confidențialitatea datelor utilizatorilor** conform reglementărilor relevante
- **Audită cererile de sampling** pentru conformitate și securitate
- **Controlează expunerea costurilor** cu limite adecvate
- **Implementează timeout-uri** pentru cererile de sampling
- **Gestionează erorile modelului cu fallback-uri adecvate**

Parametrii de sampling permit reglarea fină a comportamentului modelelor lingvistice pentru a obține echilibrul dorit între rezultate deterministe și creative.

Să vedem cum să configurăm acești parametri în diferite limbaje de programare.

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

În codul precedent am:

- Creat un client MCP cu un URL specific al serverului.
- Configurat o cerere cu parametri de sampling precum `temperature`, `top_p` și `top_k`.
- Trimite cererea și afișează textul generat.
- Folosit:
    - `allowedTools` pentru a specifica ce unelte poate folosi modelul în timpul generării. În acest caz, am permis uneltele `ideaGenerator` și `marketAnalyzer` pentru a ajuta la generarea de idei creative pentru aplicații.
    - `frequencyPenalty` și `presencePenalty` pentru a controla repetiția și diversitatea în output.
    - `temperature` pentru a controla aleatorietatea output-ului, unde valori mai mari duc la răspunsuri mai creative.
    - `top_p` pentru a limita selecția tokenilor la cei care contribuie la masa cumulativă de probabilitate de top, îmbunătățind calitatea textului generat.
    - `top_k` pentru a restricționa modelul la primii K tokeni cei mai probabili, ceea ce poate ajuta la generarea unor răspunsuri mai coerente.
    - `frequencyPenalty` și `presencePenalty` pentru a reduce repetiția și a încuraja diversitatea în textul generat.

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

În codul precedent am:

- Inițializat un client MCP cu un URL de server și o cheie API.
- Configurat două seturi de parametri de sampling: unul pentru sarcini creative și altul pentru sarcini factuale.
- Trimite cereri cu aceste configurații, permițând modelului să folosească unelte specifice pentru fiecare sarcină.
- Afișat răspunsurile generate pentru a demonstra efectele diferiților parametri de sampling.
- Folosit `allowedTools` pentru a specifica ce unelte poate folosi modelul în timpul generării. În acest caz, am permis `ideaGenerator` și `environmentalImpactTool` pentru sarcini creative, și `factChecker` și `dataAnalysisTool` pentru sarcini factuale.
- Folosit `temperature` pentru a controla aleatorietatea output-ului, unde valori mai mari duc la răspunsuri mai creative.
- Folosit `top_p` pentru a limita selecția tokenilor la cei care contribuie la masa cumulativă de probabilitate de top, îmbunătățind calitatea textului generat.
- Folosit `frequencyPenalty` și `presencePenalty` pentru a reduce repetiția și a încuraja diversitatea în output.
- Folosit `top_k` pentru a restricționa modelul la primii K tokeni cei mai probabili, ceea ce poate ajuta la generarea unor răspunsuri mai coerente.

---

## Sampling determinist

Pentru aplicațiile care necesită rezultate consistente, sampling-ul determinist asigură rezultate reproductibile. Acest lucru se realizează prin utilizarea unui seed aleator fix și setarea temperaturii la zero.

Să vedem mai jos o implementare exemplu care demonstrează sampling-ul determinist în diferite limbaje de programare.

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

În codul precedent am:

- Creat un client MCP cu un URL specificat al serverului.
- Configurat două cereri cu același prompt, seed fix și temperatură zero.
- Trimite ambele cereri și afișează textul generat.
- Demonstrat că răspunsurile sunt identice datorită naturii deterministe a configurației de sampling (același seed și temperatură).
- Folosit `setSeed` pentru a specifica un seed aleator fix, asigurând că modelul generează același output pentru aceeași intrare de fiecare dată.
- Setat `temperature` la zero pentru a asigura maximă determinare, ceea ce înseamnă că modelul va selecta întotdeauna tokenul următor cel mai probabil, fără aleatorietate.

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

În codul precedent am:

- Inițializat un client MCP cu un URL de server.
- Configurat două cereri cu același prompt, seed fix și temperatură zero.
- Trimite ambele cereri și afișează textul generat.
- Demonstrat că răspunsurile sunt identice datorită naturii deterministe a configurației de sampling (același seed și temperatură).
- Folosit `seed` pentru a specifica un seed aleator fix, asigurând că modelul generează același output pentru aceeași intrare de fiecare dată.
- Setat `temperature` la zero pentru a asigura maximă determinare, ceea ce înseamnă că modelul va selecta întotdeauna tokenul următor cel mai probabil, fără aleatorietate.
- Folosit un seed diferit pentru a treia cerere pentru a arăta că schimbarea seed-ului duce la output-uri diferite, chiar și cu același prompt și temperatură.

---

## Configurare dinamică a sampling-ului

Sampling-ul inteligent adaptează parametrii în funcție de context și cerințele fiecărei cereri. Aceasta înseamnă ajustarea dinamică a parametrilor precum temperature, top_p și penalizări în funcție de tipul sarcinii, preferințele utilizatorului sau performanța istorică.

Să vedem cum să implementăm sampling dinamic în diferite limbaje de programare.

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

În codul precedent am:

- Creat o clasă `DynamicSamplingService` care gestionează sampling-ul adaptiv.
- Definit presetări de sampling pentru diferite tipuri de sarcini (creative, factuale, cod, analitice).
- Selectat o presetare de sampling de bază în funcție de tipul sarcinii.
- Ajustat parametrii de sampling în funcție de preferințele utilizatorului, cum ar fi nivelul de creativitate și diversitate.
- Trimite cererea cu parametrii de sampling configurați dinamic.
- Returnat textul generat împreună cu parametrii de sampling aplicați și tipul sarcinii pentru transparență.
- Folosit `temperature` pentru a controla aleatorietatea output-ului, unde valori mai mari duc la răspunsuri mai creative.
- Folosit `top_p` pentru a limita selecția tokenilor la cei care contribuie la masa cumulativă de probabilitate de top, îmbunătățind calitatea textului generat.
- Folosit `frequency_penalty` pentru a reduce repetiția și a încuraja diversitatea în output.
- Folosit `user_preferences` pentru a permite personalizarea parametrilor de sampling în funcție de nivelurile de creativitate și diversitate definite de utilizator.
- Folosit `task_type` pentru a determina strategia de sampling potrivită pentru cerere, permițând răspunsuri mai adaptate în funcție de natura sarcinii.
- Folosit metoda `send_request` pentru a trimite promptul cu parametrii de sampling configurați, asigurând că modelul generează text conform cerințelor specificate.
- Folosit `generated_text` pentru a prelua răspunsul modelului, care este apoi returnat împreună cu parametrii de sampling și tipul sarcinii pentru analiză sau afișare.
- Folosit funcțiile `min` și `max` pentru a asigura că preferințele utilizatorului sunt limitate în intervale valide, prevenind configurații invalide de sampling.

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

În codul precedent am:

- Creat o clasă `AdaptiveSamplingManager` care gestionează sampling-ul dinamic în funcție de tipul sarcinii și preferințele utilizatorului.
- Definit profile de sampling pentru diferite tipuri de sarcini (creative, factuale, cod, conversaționale).
- Implementat o metodă pentru a detecta tipul sarcinii din prompt folosind euristici simple.
- Calculat parametrii de sampling pe baza tipului de sarcină detectat și a preferințelor utilizatorului.
- Aplicat ajustări învățate pe baza performanței istorice pentru a optimiza parametrii de sampling.
- Înregistrat performanța pentru ajustări viitoare, permițând sistemului să învețe din interacțiunile anterioare.
- Trimite cereri cu parametrii de sampling configurați dinamic și returnează textul generat împreună cu parametrii aplicați și tipul sarcinii detectat.
- Folosit:
    - `userPreferences` pentru a permite personalizarea parametrilor de sampling în funcție de nivelurile de creativitate, precizie și consistență definite de utilizator.
    - `detectTaskType` pentru a determina natura sarcinii pe baza promptului, permițând răspunsuri mai adaptate.
    - `recordPerformance` pentru a înregistra performanța răspunsurilor generate, facilitând adaptarea și îmbunătățirea în timp.
    - `applyLearnedAdjustments` pentru a modifica parametrii de sampling pe baza performanței istorice, sporind capacitatea modelului de a genera răspunsuri de calitate.
    - `generateResponse` pentru a encapsula întregul proces de generare a unui răspuns cu sampling adaptiv, făcând ușor apelul cu prompturi și contexte diferite.
    - `allowedTools` pentru a specifica ce unelte poate folosi modelul în timpul generării, permițând răspunsuri mai conștiente de context.
    - `feedbackScore` pentru a permite utilizatorilor să ofere feedback asupra calității răspunsului generat, care poate fi folosit pentru a rafina performanța modelului în timp.
    - `performanceHistory` pentru a menține un istoric al interacțiunilor anterioare, permițând sistemului să învețe din succese și eșecuri.
    - `getSamplingParameters` pentru a ajusta dinamic parametrii de sampling în funcție de contextul cererii, permițând un comportament mai flexibil și receptiv al modelului.
    - `detectTaskType` pentru a clasifica sarcina pe baza promptului, permițând aplicarea strategiilor de sampling potrivite pentru diferite tipuri de cereri.
    - `samplingProfiles` pentru a defini configurații de sampling de bază pentru diferite tipuri de sarcini, permițând ajustări rapide în funcție de natura cererii.

---

## Ce urmează

- [5.7 Scalare](../mcp-scaling/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.