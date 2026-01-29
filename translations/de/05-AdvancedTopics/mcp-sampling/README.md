# Sampling im Model Context Protocol

Sampling ist eine leistungsstarke MCP-Funktion, die es Servern ermöglicht, LLM-Vervollständigungen über den Client anzufordern. Dadurch werden ausgeklügelte agentenbasierte Verhaltensweisen ermöglicht, während Sicherheit und Datenschutz gewahrt bleiben. Die richtige Sampling-Konfiguration kann die Antwortqualität und Leistung erheblich verbessern. MCP bietet eine standardisierte Möglichkeit, zu steuern, wie Modelle Text mit bestimmten Parametern generieren, die Zufälligkeit, Kreativität und Kohärenz beeinflussen.

## Einführung

In dieser Lektion werden wir untersuchen, wie Sampling-Parameter in MCP-Anfragen konfiguriert werden und die zugrunde liegenden Protokollmechanismen des Samplings verstehen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Die wichtigsten Sampling-Parameter in MCP zu verstehen.
- Sampling-Parameter für verschiedene Anwendungsfälle zu konfigurieren.
- Deterministisches Sampling für reproduzierbare Ergebnisse umzusetzen.
- Sampling-Parameter dynamisch basierend auf Kontext und Benutzerpräferenzen anzupassen.
- Sampling-Strategien anzuwenden, um die Modellleistung in verschiedenen Szenarien zu verbessern.
- Zu verstehen, wie Sampling im Client-Server-Ablauf von MCP funktioniert.

## Wie Sampling in MCP funktioniert

Der Sampling-Ablauf in MCP folgt diesen Schritten:

1. Der Server sendet eine `sampling/createMessage`-Anfrage an den Client
2. Der Client prüft die Anfrage und kann sie anpassen
3. Der Client führt Sampling an einem LLM durch
4. Der Client überprüft die Vervollständigung
5. Der Client gibt das Ergebnis an den Server zurück

Dieses Human-in-the-Loop-Design stellt sicher, dass Nutzer die Kontrolle darüber behalten, was das LLM sieht und generiert.

## Überblick über Sampling-Parameter

MCP definiert folgende Sampling-Parameter, die in Client-Anfragen konfiguriert werden können:

| Parameter | Beschreibung | Typischer Bereich |
|-----------|--------------|-------------------|
| `temperature` | Steuert die Zufälligkeit bei der Token-Auswahl | 0,0 - 1,0 |
| `maxTokens` | Maximale Anzahl der zu generierenden Tokens | Ganzzahl |
| `stopSequences` | Benutzerdefinierte Sequenzen, die die Generierung stoppen | Array von Strings |
| `metadata` | Zusätzliche anbieter-spezifische Parameter | JSON-Objekt |

Viele LLM-Anbieter unterstützen zusätzliche Parameter über das `metadata`-Feld, darunter:

| Häufiger Erweiterungsparameter | Beschreibung | Typischer Bereich |
|-------------------------------|--------------|-------------------|
| `top_p` | Nucleus Sampling – begrenzt Tokens auf die oberste kumulative Wahrscheinlichkeit | 0,0 - 1,0 |
| `top_k` | Beschränkt die Token-Auswahl auf die Top-K-Optionen | 1 - 100 |
| `presence_penalty` | Bestraft Tokens basierend auf ihrer bisherigen Präsenz im Text | -2,0 - 2,0 |
| `frequency_penalty` | Bestraft Tokens basierend auf ihrer bisherigen Häufigkeit im Text | -2,0 - 2,0 |
| `seed` | Spezifischer Zufalls-Seed für reproduzierbare Ergebnisse | Ganzzahl |

## Beispiel für Anfrageformat

Hier ein Beispiel, wie Sampling von einem Client in MCP angefragt wird:

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

## Antwortformat

Der Client gibt ein Vervollständigungsergebnis zurück:

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

## Human-in-the-Loop-Kontrollen

MCP-Sampling ist mit menschlicher Aufsicht konzipiert:

- **Für Prompts**:
  - Clients sollten den Nutzern den vorgeschlagenen Prompt anzeigen
  - Nutzer sollten Prompts ändern oder ablehnen können
  - System-Prompts können gefiltert oder angepasst werden
  - Die Kontext-Einbindung wird vom Client gesteuert

- **Für Vervollständigungen**:
  - Clients sollten den Nutzern die Vervollständigung anzeigen
  - Nutzer sollten Vervollständigungen ändern oder ablehnen können
  - Clients können Vervollständigungen filtern oder anpassen
  - Nutzer bestimmen, welches Modell verwendet wird

Mit diesen Prinzipien im Hinterkopf sehen wir uns an, wie Sampling in verschiedenen Programmiersprachen implementiert wird, mit Fokus auf die Parameter, die von den meisten LLM-Anbietern unterstützt werden.

## Sicherheitsaspekte

Beim Implementieren von Sampling in MCP sollten folgende Sicherheitsbest Practices beachtet werden:

- **Validieren Sie alle Nachrichteninhalte**, bevor sie an den Client gesendet werden
- **Sensible Informationen aus Prompts und Vervollständigungen bereinigen**
- **Ratenbegrenzungen implementieren**, um Missbrauch zu verhindern
- **Sampling-Nutzung auf ungewöhnliche Muster überwachen**
- **Daten während der Übertragung mit sicheren Protokollen verschlüsseln**
- **Datenschutz der Nutzer gemäß geltender Vorschriften gewährleisten**
- **Sampling-Anfragen auf Compliance und Sicherheit prüfen**
- **Kostenkontrolle durch geeignete Limits sicherstellen**
- **Timeouts für Sampling-Anfragen implementieren**
- **Modellfehler mit geeigneten Fallbacks abfangen**

Sampling-Parameter ermöglichen es, das Verhalten von Sprachmodellen fein abzustimmen, um die gewünschte Balance zwischen deterministischen und kreativen Ausgaben zu erreichen.

Sehen wir uns an, wie diese Parameter in verschiedenen Programmiersprachen konfiguriert werden.

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

Im obigen Code haben wir:

- Einen MCP-Client mit einer spezifischen Server-URL erstellt.
- Eine Anfrage mit Sampling-Parametern wie `temperature`, `top_p` und `top_k` konfiguriert.
- Die Anfrage gesendet und den generierten Text ausgegeben.
- Folgendes verwendet:
    - `allowedTools`, um festzulegen, welche Tools das Modell während der Generierung nutzen darf. In diesem Fall erlaubten wir die Tools `ideaGenerator` und `marketAnalyzer`, um kreative App-Ideen zu unterstützen.
    - `frequencyPenalty` und `presencePenalty`, um Wiederholungen zu steuern und Vielfalt im Output zu fördern.
    - `temperature`, um die Zufälligkeit der Ausgabe zu steuern, wobei höhere Werte zu kreativeren Antworten führen.
    - `top_p`, um die Auswahl der Tokens auf diejenigen zu beschränken, die zur obersten kumulativen Wahrscheinlichkeitsmasse beitragen, was die Qualität des generierten Texts verbessert.
    - `top_k`, um das Modell auf die Top-K wahrscheinlichsten Tokens zu beschränken, was zu kohärenteren Antworten führen kann.
    - `frequencyPenalty` und `presencePenalty`, um Wiederholungen zu reduzieren und Vielfalt im generierten Text zu fördern.

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

Im obigen Code haben wir:

- Einen MCP-Client mit Server-URL und API-Schlüssel initialisiert.
- Zwei Sets von Sampling-Parametern konfiguriert: eines für kreative Aufgaben und eines für faktische Aufgaben.
- Anfragen mit diesen Konfigurationen gesendet, wobei das Modell für jede Aufgabe bestimmte Tools nutzen durfte.
- Die generierten Antworten ausgegeben, um die Auswirkungen unterschiedlicher Sampling-Parameter zu demonstrieren.
- Folgendes verwendet:
    - `allowedTools`, um festzulegen, welche Tools das Modell während der Generierung nutzen darf. Für kreative Aufgaben erlaubten wir `ideaGenerator` und `environmentalImpactTool`, für faktische Aufgaben `factChecker` und `dataAnalysisTool`.
    - `temperature`, um die Zufälligkeit der Ausgabe zu steuern, wobei höhere Werte zu kreativeren Antworten führen.
    - `top_p`, um die Auswahl der Tokens auf diejenigen zu beschränken, die zur obersten kumulativen Wahrscheinlichkeitsmasse beitragen, was die Qualität des generierten Texts verbessert.
    - `frequencyPenalty` und `presencePenalty`, um Wiederholungen zu reduzieren und Vielfalt im Output zu fördern.
    - `top_k`, um das Modell auf die Top-K wahrscheinlichsten Tokens zu beschränken, was zu kohärenteren Antworten führen kann.

---

## Deterministisches Sampling

Für Anwendungen, die konsistente Ausgaben erfordern, sorgt deterministisches Sampling für reproduzierbare Ergebnisse. Dies wird erreicht, indem ein fester Zufalls-Seed verwendet und die Temperatur auf null gesetzt wird.

Sehen wir uns die folgende Beispielimplementierung an, die deterministisches Sampling in verschiedenen Programmiersprachen demonstriert.

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

Im obigen Code haben wir:

- Einen MCP-Client mit einer angegebenen Server-URL erstellt.
- Zwei Anfragen mit demselben Prompt, festem Seed und Temperatur null konfiguriert.
- Beide Anfragen gesendet und den generierten Text ausgegeben.
- Demonstriert, dass die Antworten aufgrund der deterministischen Sampling-Konfiguration (gleicher Seed und Temperatur) identisch sind.
- `setSeed` verwendet, um einen festen Zufalls-Seed anzugeben, der sicherstellt, dass das Modell bei gleichem Input immer dieselbe Ausgabe erzeugt.
- Die `temperature` auf null gesetzt, um maximale Determiniertheit zu gewährleisten, sodass das Modell immer das wahrscheinlichste nächste Token ohne Zufälligkeit auswählt.

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

Im obigen Code haben wir:

- Einen MCP-Client mit einer Server-URL initialisiert.
- Zwei Anfragen mit demselben Prompt, festem Seed und Temperatur null konfiguriert.
- Beide Anfragen gesendet und den generierten Text ausgegeben.
- Demonstriert, dass die Antworten aufgrund der deterministischen Sampling-Konfiguration (gleicher Seed und Temperatur) identisch sind.
- `seed` verwendet, um einen festen Zufalls-Seed anzugeben, der sicherstellt, dass das Modell bei gleichem Input immer dieselbe Ausgabe erzeugt.
- Die `temperature` auf null gesetzt, um maximale Determiniertheit zu gewährleisten, sodass das Modell immer das wahrscheinlichste nächste Token ohne Zufälligkeit auswählt.
- Für die dritte Anfrage einen anderen Seed verwendet, um zu zeigen, dass sich die Ausgaben ändern, selbst bei gleichem Prompt und Temperatur.

---

## Dynamische Sampling-Konfiguration

Intelligentes Sampling passt Parameter basierend auf dem Kontext und den Anforderungen jeder Anfrage an. Das bedeutet, dass Parameter wie temperature, top_p und Penalties dynamisch je nach Aufgabentyp, Benutzerpräferenzen oder bisheriger Leistung angepasst werden.

Sehen wir uns an, wie dynamisches Sampling in verschiedenen Programmiersprachen implementiert wird.

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

Im obigen Code haben wir:

- Eine Klasse `DynamicSamplingService` erstellt, die adaptives Sampling verwaltet.
- Sampling-Voreinstellungen für verschiedene Aufgabentypen definiert (kreativ, faktisch, Code, analytisch).
- Eine Basis-Sampling-Voreinstellung basierend auf dem Aufgabentyp ausgewählt.
- Die Sampling-Parameter basierend auf Benutzerpräferenzen wie Kreativitätsgrad und Vielfalt angepasst.
- Die Anfrage mit den dynamisch konfigurierten Sampling-Parametern gesendet.
- Den generierten Text zusammen mit den angewendeten Sampling-Parametern und dem Aufgabentyp zur Transparenz zurückgegeben.
- `temperature` verwendet, um die Zufälligkeit der Ausgabe zu steuern, wobei höhere Werte zu kreativeren Antworten führen.
- `top_p` verwendet, um die Auswahl der Tokens auf diejenigen zu beschränken, die zur obersten kumulativen Wahrscheinlichkeitsmasse beitragen, was die Qualität des generierten Texts verbessert.
- `frequency_penalty` verwendet, um Wiederholungen zu reduzieren und Vielfalt im Output zu fördern.
- `user_preferences` genutzt, um die Sampling-Parameter basierend auf benutzerdefinierten Kreativitäts- und Vielfaltsstufen anzupassen.
- `task_type` verwendet, um die passende Sampling-Strategie für die Anfrage zu bestimmen und so maßgeschneiderte Antworten je nach Aufgabenart zu ermöglichen.
- Die Methode `send_request` genutzt, um den Prompt mit den konfigurierten Sampling-Parametern zu senden und sicherzustellen, dass das Modell Text gemäß den Vorgaben generiert.
- `generated_text` verwendet, um die Antwort des Modells abzurufen, die zusammen mit den Sampling-Parametern und dem Aufgabentyp für weitere Analyse oder Anzeige zurückgegeben wird.
- `min` und `max` Funktionen genutzt, um sicherzustellen, dass Benutzerpräferenzen innerhalb gültiger Bereiche liegen und ungültige Sampling-Konfigurationen vermieden werden.

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

Im obigen Code haben wir:

- Eine Klasse `AdaptiveSamplingManager` erstellt, die dynamisches Sampling basierend auf Aufgabentyp und Benutzerpräferenzen verwaltet.
- Sampling-Profile für verschiedene Aufgabentypen definiert (kreativ, faktisch, Code, konversationell).
- Eine Methode implementiert, die den Aufgabentyp anhand des Prompts mit einfachen Heuristiken erkennt.
- Sampling-Parameter basierend auf dem erkannten Aufgabentyp und den Benutzerpräferenzen berechnet.
- Gelernte Anpassungen basierend auf historischer Leistung angewendet, um Sampling-Parameter zu optimieren.
- Die Leistung für zukünftige Anpassungen protokolliert, sodass das System aus vergangenen Interaktionen lernt.
- Anfragen mit dynamisch konfigurierten Sampling-Parametern gesendet und den generierten Text zusammen mit den angewendeten Parametern und dem erkannten Aufgabentyp zurückgegeben.
- Folgendes verwendet:
    - `userPreferences`, um die Sampling-Parameter basierend auf benutzerdefinierten Kreativitäts-, Präzisions- und Konsistenzstufen anzupassen.
    - `detectTaskType`, um die Art der Aufgabe anhand des Prompts zu bestimmen und so maßgeschneiderte Antworten zu ermöglichen.
    - `recordPerformance`, um die Leistung der generierten Antworten zu protokollieren und das System so adaptiv zu machen.
    - `applyLearnedAdjustments`, um Sampling-Parameter basierend auf historischer Leistung zu modifizieren und die Qualität der Antworten zu verbessern.
    - `generateResponse`, um den gesamten Prozess der Antwortgenerierung mit adaptivem Sampling zu kapseln und so eine einfache Nutzung mit verschiedenen Prompts und Kontexten zu ermöglichen.
    - `allowedTools`, um festzulegen, welche Tools das Modell während der Generierung nutzen darf und so kontextbewusste Antworten zu ermöglichen.
    - `feedbackScore`, um Nutzern die Möglichkeit zu geben, Feedback zur Qualität der generierten Antwort zu geben, was zur weiteren Optimierung des Modells genutzt werden kann.
    - `performanceHistory`, um eine Historie vergangener Interaktionen zu führen, damit das System aus Erfolgen und Fehlern lernt.
    - `getSamplingParameters`, um Sampling-Parameter dynamisch basierend auf dem Kontext der Anfrage anzupassen und so flexibleres und reaktiveres Modellverhalten zu ermöglichen.
    - `detectTaskType`, um die Aufgabe anhand des Prompts zu klassifizieren und passende Sampling-Strategien anzuwenden.
    - `samplingProfiles`, um Basis-Sampling-Konfigurationen für verschiedene Aufgabentypen zu definieren und so schnelle Anpassungen je nach Aufgabenart zu ermöglichen.

---

## Was kommt als Nächstes

- [5.7 Scaling](../mcp-scaling/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.