> [!WARNING]
> Eșantionarea este depreciată în MCP `2026-07-28`. Această lecție este păstrată pentru
> implementările vechi. Serverele noi ar trebui să se integreze direct cu un API
> al unui furnizor LLM.

# Eșantionarea în Protocolul Contextului Modelului

> Eșantionarea rămâne în specificația `2026-07-28` pentru compatibilitate și este
> eligibilă pentru eliminare în prima revizie lansată în sau după 28 iulie,
> 2027. Exemplele din această lecție pot folosi API-uri SDK care implementează `2025-11-25`.
> Vezi [Ce s-a schimbat în MCP: Specificația 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

În implementările vechi MCP, Eșantionarea permite serverelor să solicite completări LLM
prin client. Această lecție explică fluxul protocolului depreciat
pentru compatibilitate și lucrări de migrare.

## Introducere

În această lecție, vom explora cum să configurăm parametrii de eșantionare în cererile MCP și să înțelegem mecanica protocolului de eșantionare subiacente.

## Obiective de Învățare

La sfârșitul acestei lecții, vei putea să:

- Înțelegi principalii parametri de eșantionare disponibili în MCP.
- Configurezi parametrii de eșantionare pentru diferite cazuri de utilizare.
- Implementezi eșantionarea deterministă pentru rezultate reproductibile.
- Ajustezi dinamic parametrii de eșantionare în funcție de context și preferințele utilizatorului.
- Aplici strategii de eșantionare pentru a îmbunătăți performanța modelului în diverse scenarii.
- Înțelegi cum funcționează eșantionarea în fluxul client-server din MCP.

## Cum Funcționează Eșantionarea în MCP

Fluxul de eșantionare în MCP urmează acești pași:

1. Serverul trimite o cerere `sampling/createMessage` către client
2. Clientul revizuiește cererea și o poate modifica
3. Clientul realizează un eșantion dintr-un LLM
4. Clientul revizuiește completarea
5. Clientul returnează rezultatul serverului

Acest design cu participarea umană asigură că utilizatorii păstrează controlul asupra a ceea ce vede și generează LLM-ul.

## Prezentare Generală a Parametrilor de Eșantionare

MCP definește următorii parametri de eșantionare care pot fi configurați în cererile clientului:

| Parametru | Descriere | Interval Tipic |
|-----------|-------------|---------------|
| `temperature` | Controlează aleatorietatea în selecția token-urilor | 0.0 - 1.0 |
| `maxTokens` | Numărul maxim de token-uri de generat | Valoare întreagă |
| `stopSequences` | Secvențe personalizate ce opresc generarea când sunt întâlnite | Array de șiruri |
| `metadata` | Parametri suplimentari specifici furnizorului | Obiect JSON |

Mulți furnizori LLM susțin parametri suplimentari prin câmpul `metadata`, care pot include:

| Parametru Comun Extensie | Descriere | Interval Tipic |
|-----------|-------------|---------------|
| `top_p` | Eșantionare Nucleus - limitează token-urile la probabilitatea cumulativă de top | 0.0 - 1.0 |
| `top_k` | Limitează selecția token-urilor la primele K opțiuni | 1 - 100 |
| `presence_penalty` | Penalizează token-urile în funcție de prezența lor în textul până acum | -2.0 - 2.0 |
| `frequency_penalty` | Penalizează token-urile în funcție de frecvența lor în textul până acum | -2.0 - 2.0 |
| `seed` | Sămânță aleatorie specifică pentru rezultate reproductibile | Valoare întreagă |

## Exemplu Format Cerere

Iată un exemplu de cerere pentru eșantionare de la un client în MCP:

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

## Format Răspuns

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

## Controlul cu Implicare Umană

Eșantionarea MCP este proiectată cu supraveghere umană în minte:

- **Pentru sugestii**:
  - Clienții ar trebui să afișeze utilizatorilor sugestia propusă
  - Utilizatorii ar trebui să poată modifica sau respinge sugestiile
  - Sugestiile sistemului pot fi filtrate sau modificate
  - Incluziunea contextului este controlată de client

- **Pentru completări**:
  - Clienții ar trebui să afișeze utilizatorilor completarea
  - Utilizatorii ar trebui să poată modifica sau respinge completările
  - Clienții pot filtra sau modifica completările
  - Utilizatorii controlează care model este folosit

Având aceste principii în minte, să vedem cum să implementăm eșantionarea în diferite limbaje de programare, concentrându-ne pe parametrii comun susținuți de furnizorii LLM.

## Considerații de Securitate

Când implementezi eșantionarea în MCP, ia în considerare aceste bune practici de securitate:

- **Validează tot conținutul mesajelor** înainte de a-l trimite clientului
- **Sanitizează informațiile sensibile** din sugestii și completări
- **Implementează limite de rată** pentru a preveni abuzul
- **Monitorizează utilizarea eșantionării** pentru tipare neobișnuite
- **Criptează datele în tranzit** folosind protocoale sigure
- **Gestionează confidențialitatea datelor utilizatorilor** conform reglementărilor relevante
- **Auditarea cererilor de eșantionare** pentru conformitate și securitate
- **Controlează expunerea costurilor** cu limite adecvate
- **Implementează timeout-uri** pentru cererile de eșantionare
- **Gestionează elegant erorile modelului** cu alternative adecvate

Parametrii de eșantionare permit reglarea fină a comportamentului modelelor lingvistice pentru a atinge echilibrul dorit între rezultate deterministe și creative.

Să vedem cum să configurăm acești parametri în diferite limbaje de programare.

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

În codul precedent am:

- Creat un client MCP cu un URL specific al serverului.
- Configurat o cerere cu parametrii de eșantionare precum `temperature`, `top_p` și `top_k`.
- Trimis cererea și afișat textul generat.
- Folosit:
    - `allowedTools` pentru a specifica ce unelte poate folosi modelul în timpul generării. În acest caz, am permis instrumentele `ideaGenerator` și `marketAnalyzer` pentru a ajuta la generarea ideilor creative de aplicații.
    - `frequencyPenalty` și `presencePenalty` pentru a controla repetarea și diversitatea în output.
    - `temperature` pentru a controla aleatorietatea rezultatelor, unde valori mai mari conduc la răspunsuri mai creative.
    - `top_p` pentru a limita selecția token-urilor la cele care contribuie la masa cumulativă de probabilitate de vârf, îmbunătățind calitatea textului generat.
    - `top_k` pentru a restricționa modelul la primele K token-uri cele mai probabile, ceea ce poate ajuta la generarea unor răspunsuri mai coerente.
    - `frequencyPenalty` și `presencePenalty` pentru a reduce repetarea și a încuraja diversitatea în textul generat.

# [JavaScript](#tab/javascript)

```javascript
// Exemplu JavaScript: Configurarea temperaturii și a eșantionării Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Inițializează clientul MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Configurează cererea cu parametri diferiți de eșantionare
  const creativeSampling = {
    temperature: 0.9,    // Temperatura mai mare = mai multă aleatorietate/creativitate
    topP: 0.92,          // Ia în considerare tokenii cu masa probabilității top 92%
    frequencyPenalty: 0.6, // Reduce repetarea secvențelor de tokeni
    presencePenalty: 0.4   // Penalizează tokenii care au apărut deja în textul de până acum
  };
  
  const factualSampling = {
    temperature: 0.2,    // Temperatura mai mică = mai determinist/factual
    topP: 0.85,          // Selecție de tokeni ușor mai concentrată
    frequencyPenalty: 0.2, // Penalizare minimă pentru repetare
    presencePenalty: 0.1   // Penalizare minimă pentru prezență
  };
  
  try {
    // Trimite două cereri cu configurații de eșantionare diferite
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

- Inițializat un client MCP cu URL server și cheie API.
- Configurat două seturi de parametri de eșantionare: unul pentru sarcini creative și altul pentru sarcini factuale.
- Trimis cereri cu aceste configurații, permițând modelului să folosească unelte specifice pentru fiecare sarcină.
- Afișat răspunsurile generate pentru a demonstra efectele diferiților parametri de eșantionare.
- Folosit `allowedTools` pentru a specifica ce unelte poate folosi modelul în timpul generării. În acest caz, am permis `ideaGenerator` și `environmentalImpactTool` pentru sarcini creative și `factChecker` și `dataAnalysisTool` pentru sarcini factuale.
- Folosit `temperature` pentru a controla aleatorietatea rezultatelor, unde valori mai mari conduc la răspunsuri mai creative.
- Folosit `top_p` pentru a limita selecția token-urilor la cele care contribuie la masa cumulativă de probabilitate de vârf, îmbunătățind calitatea textului generat.
- Folosit `frequencyPenalty` și `presencePenalty` pentru a reduce repetarea și a încuraja diversitatea în output.
- Folosit `top_k` pentru a restricționa modelul la primele K token-uri cele mai probabile, ceea ce poate ajuta la generarea unor răspunsuri mai coerente.

---

## Eșantionare Deterministă

Pentru aplicațiile care necesită rezultate consistente, eșantionarea deterministă asigură rezultate reproductibile. Cum face asta este prin utilizarea unei sămânțe aleatorii fixe și setarea temperaturii la zero.

Să vedem mai jos un exemplu de implementare pentru a demonstra eșantionarea deterministă în diferite limbaje de programare.

# [Java](#tab/java)

```java
// Exemplu Java: Răspunsuri deterministe cu sămânță fixă
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Folosind o sămânță fixă pentru rezultate deterministe
        
        // Prima cerere cu sămânță fixă
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Temperatura zero pentru determinism maxim
            .build();
            
        // A doua cerere cu aceeași sămânță
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Execută ambele cereri
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Răspunsurile ar trebui să fie identice datorită aceleiași sămânțe și temperaturii=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

În codul precedent am:

- Creat un client MCP cu un URL specific al serverului.
- Configurat două cereri cu aceeași sugestie, sămânță fixă și temperatură zero.
- Trimis ambele cereri și afișat textul generat.
- Demonstrat că răspunsurile sunt identice datorită naturii deterministe a configurației de eșantionare (aceeași sămânță și temperatură).
- Folosit `setSeed` pentru a specifica o sămânță aleatorie fixă, asigurând că modelul generează același output pentru același input de fiecare dată.
- Setat `temperature` la zero pentru a asigura determinismul maxim, ceea ce înseamnă că modelul va selecta întotdeauna token-ul următor cel mai probabil fără aleatorietate.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Exemplu JavaScript: Răspunsuri deterministe cu control al seminței
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Prima solicitare cu sămânță fixă
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Temperatura zero pentru determinism maxim
    });
    
    // A doua solicitare cu aceeași sămânță și temperatură
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // A treia solicitare cu sămânță diferită dar aceeași temperatură
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

- Inițializat un client MCP cu un URL al serverului.
- Configurat două cereri cu aceeași sugestie, sămânță fixă și temperatură zero.
- Trimis ambele cereri și afișat textul generat.
- Demonstrat că răspunsurile sunt identice datorită naturii deterministe a configurației de eșantionare (aceeași sămânță și temperatură).
- Folosit `seed` pentru a specifica o sămânță aleatorie fixă, asigurând că modelul generează același output pentru același input de fiecare dată.
- Setat `temperature` la zero pentru a asigura determinismul maxim, ceea ce înseamnă că modelul va selecta întotdeauna token-ul următor cel mai probabil fără aleatorietate.
- Folosit o sămânță diferită pentru a treia cerere pentru a arăta că schimbarea sămânței generează outputuri diferite, chiar și cu aceeași sugestie și temperatură.

---

## Configurare Dinamică a Eșantionării

Eșantionarea inteligentă adaptează parametrii pe baza contextului și cerințelor fiecărei cereri. Aceasta înseamnă ajustarea dinamică a parametrilor precum temperature, top_p și penalizări în funcție de tipul sarcinii, preferințele utilizatorului sau performanța istorică.

Să vedem cum să implementăm eșantionarea dinamică în diferite limbaje de programare.

# [Python](#tab/python)

```python
# Exemplu Python: Eșantionare dinamică bazată pe contextul cererii
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definește presetări de eșantionare pentru diferite tipuri de sarcini
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Selectează presetarea de bază
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Ajustează în funcție de preferințele utilizatorului, dacă sunt furnizate
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Scalează temperatura în funcție de preferința de creativitate (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Ajustează top_p în funcție de diversitatea răspunsului dorită
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Creează și trimite cererea cu parametri personalizați de eșantionare
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Returnează răspunsul cu metadate de eșantionare pentru transparență
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

În codul precedent am:

- Creat o clasă `DynamicSamplingService` care gestionează eșantionarea adaptivă.
- Definit presetări de eșantionare pentru diferite tipuri de sarcini (creative, factuale, cod, analitice).
- Selectat o presetare de bază pe baza tipului de sarcină.
- Ajustat parametrii de eșantionare în funcție de preferințele utilizatorului, cum ar fi nivelul de creativitate și diversitate.
- Trimis cererea cu parametrii de eșantionare configurați dinamic.
- Returnat textul generat împreună cu parametrii aplicați și tipul sarcinii pentru transparență.
- Folosit `temperature` pentru a controla aleatorietatea rezultatului, unde valori mai mari conduc la răspunsuri mai creative.
- Folosit `top_p` pentru a limita selecția token-urilor la cele care contribuie la masa cumulativă de probabilitate de vârf, îmbunătățind calitatea textului generat.
- Folosit `frequency_penalty` pentru a reduce repetarea și a încuraja diversitatea în output.
- Folosit `user_preferences` pentru a permite personalizarea parametrilor de eșantionare pe baza nivelurilor definite de utilizator de creativitate și diversitate.
- Folosit `task_type` pentru a determina strategia de eșantionare potrivită pentru cerere, permițând răspunsuri mai adaptate nevoilor sarcinii.
- Folosit metoda `send_request` pentru a trimite sugestia cu parametrii de eșantionare configurați, asigurând că modelul generează text conform cerințelor specificate.
- Folosit `generated_text` pentru a prelua răspunsul modelului, care este apoi returnat împreună cu parametrii de eșantionare și tipul sarcinii pentru analiză sau afișare suplimentară.
- Folosit funcțiile `min` și `max` pentru a se asigura că preferințele utilizatorului sunt limitate în intervale valide, prevenind configurații invalide de eșantionare.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// Exemplu JavaScript: Configurare de eșantionare dinamică bazată pe contextul utilizatorului
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Definirea profilurilor de eșantionare de bază
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Urmărirea performanței istorice
    this.performanceHistory = [];
  }
  
  // Detectarea tipului de sarcină din prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Detectare heuristica simplă - poate fi îmbunătățită cu clasificare ML
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
    
    // Implicit la conversațional dacă nu se detectează un tip clar
    return 'conversational';
  }
  
  // Calcularea parametrilor de eșantionare bazată pe context și preferințele utilizatorului
  getSamplingParameters(prompt, context = {}) {
    // Detectarea tipului de sarcină
    const taskType = this.detectTaskType(prompt, context);
    
    // Obținerea profilului de bază
    let params = {...this.samplingProfiles[taskType]};
    
    // Ajustarea bazată pe preferințele utilizatorului
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Scara de la 1-10 la intervalul de temperatură potrivit
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Precizie mai mare înseamnă topP mai mic (selecție mai concentrată)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Consistență mai mare înseamnă penalizări mai mici
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Aplicarea ajustărilor învățate din istoricul performanței
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Logică adaptivă simplă - poate fi îmbunătățită cu algoritmi mai sofisticați
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Se ia în considerare doar istoricul recent
    
    if (relevantHistory.length > 0) {
      // Calcularea scorurilor medii de performanță
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Dacă performanța este sub prag, se ajustează parametrii
      if (avgScore < 0.7) {
        // Ajustare ușoară către valori mai sigure
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Înregistrarea performanței pentru ajustări viitoare
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Evaluare 0-1 a calității răspunsului
    });
    
    // Limitarea dimensiunii istoricului
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Obținerea parametrilor de eșantionare optimizați
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Trimiterea cererii cu parametrii optimizați
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Dacă utilizatorul oferă feedback, acesta se înregistrează pentru optimizare viitoare
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

// Exemplu de utilizare
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Sarcină creativă cu preferințe personalizate ale utilizatorului
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Creativitate ridicată (1-10)
          consistency: 3  // Consistență scăzută (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Sarcină de generare cod
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Creativitate scăzută
          precision: 8,   // Precizie ridicată
          consistency: 9  // Consistență ridicată
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

- Creat o clasă `AdaptiveSamplingManager` care gestionează eșantionarea dinamică pe baza tipului de sarcină și a preferințelor utilizatorului.
- Definit profiluri de eșantionare pentru diferite tipuri de sarcini (creative, factuale, cod, conversaționale).
- Implementat o metodă de a detecta tipul de sarcină din sugestie folosind euristici simple.
- Calculat parametrii de eșantionare bazat pe tipul de sarcină detectat și preferințele utilizatorului.
- Aplicat ajustări învățate pe baza performanței istorice pentru a optimiza parametrii de eșantionare.
- Înregistrat performanțele pentru ajustări viitoare, permițând sistemului să învețe din interacțiunile trecute.
- Trimis cereri cu parametri de eșantionare configurați dinamic și returnat textul generat împreună cu parametrii aplicați și tipul sarcinii detectat.
- Folosit:
    - `userPreferences` pentru a permite personalizarea parametrilor de eșantionare pe baza nivelurilor definite de utilizator de creativitate, precizie și consistență.
    - `detectTaskType` pentru a determina natura sarcinii pe baza sugestiei, permițând răspunsuri mai adaptate.
    - `recordPerformance` pentru a înregistra performanța răspunsurilor generate, facilitând adaptarea și îmbunătățirea în timp a sistemului.
    - `applyLearnedAdjustments` pentru a modifica parametrii de eșantionare pe baza performanței istorice, sporind capacitatea modelului de a genera răspunsuri de înaltă calitate.
    - `generateResponse` pentru a încapsula întregul proces de generare a unui răspuns cu eșantionare adaptivă, făcând ușor apelul cu sugestii și contexte diferite.
    - `allowedTools` pentru a specifica ce unelte poate folosi modelul în timpul generării, permițând răspunsuri mai conștiente de context.
    - `feedbackScore` pentru a permite utilizatorilor să ofere feedback asupra calității răspunsului generat, care poate fi folosit pentru a rafina performanța modelului în timp.
    - `performanceHistory` pentru a menține un istoric al interacțiunilor trecute, cu scopul de a învăța din succesele și eșecurile anterioare.
    - `getSamplingParameters` pentru a ajusta dinamic parametrii de eșantionare în funcție de contextul cererii, permițând un comportament mai flexibil și receptiv al modelului.
    - `detectTaskType` pentru a clasifica sarcina bazat pe sugestie, permițând sistemului să aplice strategii de eșantionare adecvate pentru diferite tipuri de cereri.
    - `samplingProfiles` pentru a defini configurații de bază de eșantionare pentru diferite tipuri de sarcini, permițând ajustări rapide în funcție de natura cererii.

---

## Ce urmează

- [5.7 Scălare](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->