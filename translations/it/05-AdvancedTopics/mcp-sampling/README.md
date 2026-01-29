# Campionamento nel Protocollo Model Context

Il campionamento è una potente funzionalità di MCP che permette ai server di richiedere completamenti LLM tramite il client, abilitando comportamenti agentici sofisticati mantenendo sicurezza e privacy. La configurazione corretta del campionamento può migliorare notevolmente la qualità e le prestazioni delle risposte. MCP fornisce un modo standardizzato per controllare come i modelli generano testo con parametri specifici che influenzano casualità, creatività e coerenza.

## Introduzione

In questa lezione esploreremo come configurare i parametri di campionamento nelle richieste MCP e capire i meccanismi di protocollo sottostanti al campionamento.

## Obiettivi di Apprendimento

Al termine di questa lezione sarai in grado di:

- Comprendere i principali parametri di campionamento disponibili in MCP.
- Configurare i parametri di campionamento per diversi casi d’uso.
- Implementare il campionamento deterministico per risultati riproducibili.
- Regolare dinamicamente i parametri di campionamento in base al contesto e alle preferenze dell’utente.
- Applicare strategie di campionamento per migliorare le prestazioni del modello in vari scenari.
- Capire come funziona il campionamento nel flusso client-server di MCP.

## Come Funziona il Campionamento in MCP

Il flusso di campionamento in MCP segue questi passaggi:

1. Il server invia una richiesta `sampling/createMessage` al client  
2. Il client esamina la richiesta e può modificarla  
3. Il client esegue il campionamento da un LLM  
4. Il client rivede il completamento  
5. Il client restituisce il risultato al server  

Questo design con l’intervento umano garantisce che gli utenti mantengano il controllo su ciò che l’LLM vede e genera.

## Panoramica dei Parametri di Campionamento

MCP definisce i seguenti parametri di campionamento configurabili nelle richieste client:

| Parametro | Descrizione | Intervallo Tipico |
|-----------|-------------|-------------------|
| `temperature` | Controlla la casualità nella selezione dei token | 0.0 - 1.0 |
| `maxTokens` | Numero massimo di token da generare | Valore intero |
| `stopSequences` | Sequenze personalizzate che interrompono la generazione quando incontrate | Array di stringhe |
| `metadata` | Parametri aggiuntivi specifici del provider | Oggetto JSON |

Molti provider LLM supportano parametri aggiuntivi tramite il campo `metadata`, che possono includere:

| Parametro Estensione Comune | Descrizione | Intervallo Tipico |
|----------------------------|-------------|-------------------|
| `top_p` | Campionamento a nucleo - limita i token alla probabilità cumulativa più alta | 0.0 - 1.0 |
| `top_k` | Limita la selezione dei token alle prime K opzioni | 1 - 100 |
| `presence_penalty` | Penalizza i token in base alla loro presenza nel testo finora | -2.0 - 2.0 |
| `frequency_penalty` | Penalizza i token in base alla loro frequenza nel testo finora | -2.0 - 2.0 |
| `seed` | Seed casuale specifico per risultati riproducibili | Valore intero |

## Esempio di Formato della Richiesta

Ecco un esempio di richiesta di campionamento da un client in MCP:

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

## Formato della Risposta

Il client restituisce un risultato di completamento:

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

## Controlli con Intervento Umano

Il campionamento MCP è progettato tenendo conto della supervisione umana:

- **Per i prompt**:
  - I client dovrebbero mostrare agli utenti il prompt proposto  
  - Gli utenti dovrebbero poter modificare o rifiutare i prompt  
  - I prompt di sistema possono essere filtrati o modificati  
  - L’inclusione del contesto è controllata dal client  

- **Per i completamenti**:
  - I client dovrebbero mostrare agli utenti il completamento  
  - Gli utenti dovrebbero poter modificare o rifiutare i completamenti  
  - I client possono filtrare o modificare i completamenti  
  - Gli utenti controllano quale modello viene utilizzato  

Con questi principi in mente, vediamo come implementare il campionamento in diversi linguaggi di programmazione, concentrandoci sui parametri comunemente supportati dai provider LLM.

## Considerazioni sulla Sicurezza

Quando si implementa il campionamento in MCP, considera queste best practice di sicurezza:

- **Valida tutto il contenuto dei messaggi** prima di inviarlo al client  
- **Sanifica le informazioni sensibili** da prompt e completamenti  
- **Implementa limiti di frequenza** per prevenire abusi  
- **Monitora l’uso del campionamento** per rilevare pattern insoliti  
- **Cripta i dati in transito** usando protocolli sicuri  
- **Gestisci la privacy dei dati utente** secondo le normative vigenti  
- **Audita le richieste di campionamento** per conformità e sicurezza  
- **Controlla l’esposizione ai costi** con limiti appropriati  
- **Implementa timeout** per le richieste di campionamento  
- **Gestisci gli errori del modello con fallback appropriati**  

I parametri di campionamento permettono di affinare il comportamento dei modelli linguistici per raggiungere il giusto equilibrio tra output deterministici e creativi.

Vediamo come configurare questi parametri in diversi linguaggi di programmazione.

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

Nel codice precedente abbiamo:

- Creato un client MCP con un URL server specifico.  
- Configurato una richiesta con parametri di campionamento come `temperature`, `top_p` e `top_k`.  
- Inviato la richiesta e stampato il testo generato.  
- Usato:  
    - `allowedTools` per specificare quali strumenti il modello può usare durante la generazione. In questo caso, abbiamo permesso gli strumenti `ideaGenerator` e `marketAnalyzer` per assistere nella generazione di idee creative per app.  
    - `frequencyPenalty` e `presencePenalty` per controllare ripetizioni e diversità nell’output.  
    - `temperature` per controllare la casualità dell’output, dove valori più alti portano a risposte più creative.  
    - `top_p` per limitare la selezione dei token a quelli che contribuiscono alla massa cumulativa di probabilità più alta, migliorando la qualità del testo generato.  
    - `top_k` per restringere il modello ai primi K token più probabili, aiutando a generare risposte più coerenti.  
    - `frequencyPenalty` e `presencePenalty` per ridurre la ripetizione e incoraggiare la diversità nel testo generato.

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

Nel codice precedente abbiamo:

- Inizializzato un client MCP con un URL server e una chiave API.  
- Configurato due set di parametri di campionamento: uno per compiti creativi e un altro per compiti fattuali.  
- Inviato richieste con queste configurazioni, permettendo al modello di usare strumenti specifici per ogni compito.  
- Stampato le risposte generate per mostrare gli effetti di diversi parametri di campionamento.  
- Usato `allowedTools` per specificare quali strumenti il modello può usare durante la generazione. In questo caso, abbiamo permesso `ideaGenerator` e `environmentalImpactTool` per compiti creativi, e `factChecker` e `dataAnalysisTool` per compiti fattuali.  
- Usato `temperature` per controllare la casualità dell’output, dove valori più alti portano a risposte più creative.  
- Usato `top_p` per limitare la selezione dei token a quelli che contribuiscono alla massa cumulativa di probabilità più alta, migliorando la qualità del testo generato.  
- Usato `frequencyPenalty` e `presencePenalty` per ridurre la ripetizione e incoraggiare la diversità nell’output.  
- Usato `top_k` per limitare il modello ai primi K token più probabili, aiutando a generare risposte più coerenti.

---

## Campionamento Deterministico

Per applicazioni che richiedono output consistenti, il campionamento deterministico garantisce risultati riproducibili. Lo fa usando un seed casuale fisso e impostando la temperatura a zero.

Vediamo un esempio di implementazione per dimostrare il campionamento deterministico in diversi linguaggi di programmazione.

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

Nel codice precedente abbiamo:

- Creato un client MCP con un URL server specificato.  
- Configurato due richieste con lo stesso prompt, seed fisso e temperatura zero.  
- Inviato entrambe le richieste e stampato il testo generato.  
- Dimostrato che le risposte sono identiche grazie alla natura deterministica della configurazione di campionamento (stesso seed e temperatura).  
- Usato `setSeed` per specificare un seed casuale fisso, assicurando che il modello generi sempre lo stesso output per lo stesso input.  
- Impostato `temperature` a zero per garantire massima determinismo, cioè il modello selezionerà sempre il token successivo più probabile senza casualità.

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

Nel codice precedente abbiamo:

- Inizializzato un client MCP con un URL server.  
- Configurato due richieste con lo stesso prompt, seed fisso e temperatura zero.  
- Inviato entrambe le richieste e stampato il testo generato.  
- Dimostrato che le risposte sono identiche grazie alla natura deterministica della configurazione di campionamento (stesso seed e temperatura).  
- Usato `seed` per specificare un seed casuale fisso, assicurando che il modello generi sempre lo stesso output per lo stesso input.  
- Impostato `temperature` a zero per garantire massima determinismo, cioè il modello selezionerà sempre il token successivo più probabile senza casualità.  
- Usato un seed diverso per la terza richiesta per mostrare che cambiando il seed si ottengono output differenti, anche con lo stesso prompt e temperatura.

---

## Configurazione Dinamica del Campionamento

Il campionamento intelligente adatta i parametri in base al contesto e alle esigenze di ogni richiesta. Ciò significa regolare dinamicamente parametri come temperature, top_p e penalità in base al tipo di compito, alle preferenze dell’utente o alle prestazioni storiche.

Vediamo come implementare il campionamento dinamico in diversi linguaggi di programmazione.

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

Nel codice precedente abbiamo:

- Creato una classe `DynamicSamplingService` che gestisce il campionamento adattivo.  
- Definito preset di campionamento per diversi tipi di compito (creativo, fattuale, codice, analitico).  
- Selezionato un preset base di campionamento in base al tipo di compito.  
- Regolato i parametri di campionamento in base alle preferenze dell’utente, come livello di creatività e diversità.  
- Inviato la richiesta con i parametri di campionamento configurati dinamicamente.  
- Restituito il testo generato insieme ai parametri di campionamento applicati e al tipo di compito per trasparenza.  
- Usato `temperature` per controllare la casualità dell’output, dove valori più alti portano a risposte più creative.  
- Usato `top_p` per limitare la selezione dei token a quelli che contribuiscono alla massa cumulativa di probabilità più alta, migliorando la qualità del testo generato.  
- Usato `frequency_penalty` per ridurre la ripetizione e incoraggiare la diversità nell’output.  
- Usato `user_preferences` per permettere la personalizzazione dei parametri di campionamento basata sui livelli di creatività e diversità definiti dall’utente.  
- Usato `task_type` per determinare la strategia di campionamento appropriata per la richiesta, permettendo risposte più mirate in base alla natura del compito.  
- Usato il metodo `send_request` per inviare il prompt con i parametri di campionamento configurati, assicurando che il modello generi testo secondo i requisiti specificati.  
- Usato `generated_text` per recuperare la risposta del modello, che viene poi restituita insieme ai parametri di campionamento e al tipo di compito per ulteriori analisi o visualizzazione.  
- Usato le funzioni `min` e `max` per assicurare che le preferenze dell’utente siano limitate a intervalli validi, evitando configurazioni di campionamento non valide.

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

Nel codice precedente abbiamo:

- Creato una classe `AdaptiveSamplingManager` che gestisce il campionamento dinamico basato sul tipo di compito e sulle preferenze dell’utente.  
- Definito profili di campionamento per diversi tipi di compito (creativo, fattuale, codice, conversazionale).  
- Implementato un metodo per rilevare il tipo di compito dal prompt usando euristiche semplici.  
- Calcolato i parametri di campionamento in base al tipo di compito rilevato e alle preferenze dell’utente.  
- Applicato aggiustamenti appresi basati sulle prestazioni storiche per ottimizzare i parametri di campionamento.  
- Registrato le prestazioni per aggiustamenti futuri, permettendo al sistema di apprendere dalle interazioni passate.  
- Inviato richieste con parametri di campionamento configurati dinamicamente e restituito il testo generato insieme ai parametri applicati e al tipo di compito rilevato.  
- Usato:  
    - `userPreferences` per permettere la personalizzazione dei parametri di campionamento basata sui livelli di creatività, precisione e coerenza definiti dall’utente.  
    - `detectTaskType` per determinare la natura del compito basandosi sul prompt, permettendo risposte più mirate.  
    - `recordPerformance` per registrare le prestazioni delle risposte generate, consentendo al sistema di adattarsi e migliorare nel tempo.  
    - `applyLearnedAdjustments` per modificare i parametri di campionamento basandosi sulle prestazioni storiche, migliorando la capacità del modello di generare risposte di alta qualità.  
    - `generateResponse` per incapsulare l’intero processo di generazione di una risposta con campionamento adattivo, facilitando l’uso con prompt e contesti diversi.  
    - `allowedTools` per specificare quali strumenti il modello può usare durante la generazione, permettendo risposte più contestualizzate.  
    - `feedbackScore` per permettere agli utenti di fornire feedback sulla qualità della risposta generata, che può essere usato per affinare ulteriormente le prestazioni del modello nel tempo.  
    - `performanceHistory` per mantenere un registro delle interazioni passate, consentendo al sistema di apprendere da successi e insuccessi precedenti.  
    - `getSamplingParameters` per regolare dinamicamente i parametri di campionamento in base al contesto della richiesta, permettendo un comportamento del modello più flessibile e reattivo.  
    - `detectTaskType` per classificare il compito basandosi sul prompt, consentendo al sistema di applicare strategie di campionamento appropriate per diversi tipi di richieste.  
    - `samplingProfiles` per definire configurazioni base di campionamento per diversi tipi di compito, permettendo aggiustamenti rapidi in base alla natura della richiesta.

---

## Cosa c’è dopo

- [5.7 Scaling](../mcp-scaling/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.