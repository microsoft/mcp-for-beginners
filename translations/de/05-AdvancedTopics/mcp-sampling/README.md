> [!WARNING]
> Sampling wird im MCP `2026-07-28` als veraltet betrachtet. Diese Lektion wird für
> Altsysteme aufbewahrt. Neue Server sollten direkt mit einer LLM-Anbieter-API integriert werden.


# Sampling im Model Context Protocol

> Sampling bleibt in der Spezifikation `2026-07-28` zur Kompatibilität enthalten und ist
> berechtigt, in der ersten Revision entfernt zu werden, die am oder nach dem 28. Juli
> 2027 veröffentlicht wird. Beispiele in dieser Lektion können SDK-APIs verwenden, die `2025-11-25` implementieren.
> Siehe [Was sich im MCP geändert hat: Die Spezifikation 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

In Legacy-MCP-Implementierungen erlaubt Sampling Servern, LLM-Vervollständigungen über den Client anzufordern. Diese Lektion erklärt diesen veralteten Protokollablauf zur Kompatibilität und für Migrationsarbeiten.







## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Die wichtigsten Sampling-Parameter im MCP zu verstehen.
- Sampling-Parameter für verschiedene Anwendungsfälle zu konfigurieren.
- Deterministisches Sampling für reproduzierbare Ergebnisse umzusetzen.
- Sampling-Parameter basierend auf Kontext und Benutzerpräferenzen dynamisch anzupassen.
- Sampling-Strategien anzuwenden, um die Modellleistung in verschiedenen Szenarien zu verbessern.
- Zu verstehen, wie Sampling im Client-Server-Fluss des MCP funktioniert.

## Wie Sampling im MCP funktioniert

Der Sampling-Ablauf im MCP folgt diesen Schritten:

1. Server sendet eine `sampling/createMessage`-Anfrage an den Client
2. Client prüft die Anfrage und kann sie modifizieren
3. Client führt Sampling von einem LLM durch
4. Client prüft die Vervollständigung
5. Client gibt das Ergebnis an den Server zurück

Dieses Design mit Mensch-in-der-Schleife stellt sicher, dass Benutzer die Kontrolle darüber behalten, was das LLM sieht und generiert.

## Übersicht über Sampling-Parameter

MCP definiert folgende Sampling-Parameter, die in Client-Anfragen konfiguriert werden können:

| Parameter | Beschreibung | Typischer Bereich |
|-----------|-------------|---------------|
| `temperature` | Steuert die Zufälligkeit bei der Token-Auswahl | 0.0 - 1.0 |
| `maxTokens` | Maximale Anzahl zu generierender Tokens | Ganzzahliger Wert |
| `stopSequences` | Benutzerdefinierte Sequenzen, die die Generierung stoppen | Array von Strings |
| `metadata` | Zusätzliche anbieter-spezifische Parameter | JSON-Objekt |

Viele LLM-Anbieter unterstützen zusätzliche Parameter über das `metadata`-Feld, welches enthalten kann:

| Häufiger Erweiterungsparameter | Beschreibung | Typischer Bereich |
|-----------|-------------|---------------|
| `top_p` | Nucleus Sampling - begrenzt Tokens auf die top kumulative Wahrscheinlichkeit | 0.0 - 1.0 |
| `top_k` | Begrenzt die Token-Auswahl auf die top K Optionen | 1 - 100 |
| `presence_penalty` | Bestraft Tokens basierend auf deren Präsenz im bisherigen Text | -2.0 - 2.0 |
| `frequency_penalty` | Bestraft Tokens basierend auf ihrer Häufigkeit im bisherigen Text | -2.0 - 2.0 |
| `seed` | Spezifischer Zufallssamen für reproduzierbare Ergebnisse | Ganzzahliger Wert |

## Beispiel für Anfragenformat

Hier ein Beispiel, wie Sampling von einem Client im MCP angefragt wird:

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

Der Client liefert ein Vervollständigungsergebnis zurück:

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

## Mensch-in-der-Schleife-Kontrollen

MCP Sampling ist mit menschlicher Aufsicht konzipiert:

- **Für Eingabeaufforderungen**:
  - Clients sollten Benutzern die vorgeschlagene Eingabeaufforderung zeigen
  - Benutzer sollten Eingabeaufforderungen ändern oder ablehnen können
  - Systemaufforderungen können gefiltert oder modifiziert werden
  - Die Kontextaufnahme wird vom Client gesteuert

- **Für Vervollständigungen**:
  - Clients sollten Benutzern die Vervollständigung zeigen
  - Benutzer sollten Vervollständigungen ändern oder ablehnen können
  - Clients können Vervollständigungen filtern oder modifizieren
  - Benutzer kontrollieren, welches Modell verwendet wird

Mit diesen Prinzipien im Hinterkopf sehen wir uns an, wie Sampling in verschiedenen Programmiersprachen implementiert wird, mit Fokus auf die Parameter, die allgemein bei LLM-Anbietern unterstützt werden.

## Sicherheitsüberlegungen

Beim Implementieren von Sampling im MCP sollten folgende Sicherheitsbest Practices berücksichtigt werden:

- **Validieren Sie alle Nachrichteninhalte**, bevor diese an den Client gesendet werden
- **Bereinigen Sie sensible Informationen** aus Eingabeaufforderungen und Vervollständigungen
- **Implementieren Sie Ratenbegrenzungen** zur Missbrauchsverhinderung
- **Überwachen Sie Sampling-Nutzung** auf ungewöhnliche Muster
- **Verschlüsseln Sie Daten während der Übertragung** mit sicheren Protokollen
- **Behandeln Sie den Datenschutz der Benutzer** gemäß relevanter Vorschriften
- **Auditieren Sie Sampling-Anfragen** für Compliance und Sicherheit
- **Kontrollieren Sie Kosten durch angemessene Limits**
- **Implementieren Sie Timeouts** für Sampling-Anfragen
- **Behandeln Sie Modellfehler angemessen** mit geeigneten Fallback-Strategien

Sampling-Parameter ermöglichen eine Feinabstimmung des Verhaltens von Sprachmodellen, um das gewünschte Gleichgewicht zwischen deterministischen und kreativen Ausgaben zu erzielen.

Schauen wir uns an, wie man diese Parameter in verschiedenen Programmiersprachen konfiguriert.

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

Im vorhergehenden Code haben wir:

- Einen MCP-Client mit einer bestimmten Server-URL erstellt.
- Eine Anfrage mit Sampling-Parametern wie `temperature`, `top_p` und `top_k` konfiguriert.
- Die Anfrage gesendet und den generierten Text ausgegeben.
- Verwendet:
    - `allowedTools` um anzugeben, welche Tools das Modell während der Generierung verwenden darf. In diesem Fall erlaubten wir die Tools `ideaGenerator` und `marketAnalyzer`, um bei der Generierung kreativer App-Ideen zu unterstützen.
    - `frequencyPenalty` und `presencePenalty`, um Wiederholungen zu kontrollieren und Vielfalt in der Ausgabe zu fördern.
    - `temperature`, um die Zufälligkeit der Ausgabe zu steuern, wobei höhere Werte zu kreativeren Antworten führen.
    - `top_p`, um die Auswahl der Tokens auf diejenigen zu beschränken, die zur obersten kumulativen Wahrscheinlichkeitsmasse beitragen, was die Qualität des generierten Textes verbessert.
    - `top_k`, um das Modell auf die top K wahrscheinlichsten Tokens zu beschränken, was bei der Erzeugung kohärenterer Antworten hilft.
    - `frequencyPenalty` und `presencePenalty`, um Wiederholungen zu reduzieren und Vielfalt beim generierten Text zu fördern.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript Beispiel: Temperatur- und Top-P Sampling-Konfiguration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Initialisiere den MCP-Client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Anfrage mit unterschiedlichen Sampling-Parametern konfigurieren
  const creativeSampling = {
    temperature: 0.9,    // Höhere Temperatur = mehr Zufälligkeit/Kreativität
    topP: 0.92,          // Berücksichtige Tokens mit einer kumulativen Wahrscheinlichkeit von 92 %
    frequencyPenalty: 0.6, // Wiederholung von Token-Sequenzen reduzieren
    presencePenalty: 0.4   // Bestrafe Tokens, die bisher im Text aufgetaucht sind
  };
  
  const factualSampling = {
    temperature: 0.2,    // Niedrigere Temperatur = deterministischer/faktischer
    topP: 0.85,          // Etwas fokussiertere Token-Auswahl
    frequencyPenalty: 0.2, // Minimale Wiederholungsstrafe
    presencePenalty: 0.1   // Minimale Präsenzstrafe
  };
  
  try {
    // Zwei Anfragen mit unterschiedlichen Sampling-Konfigurationen senden
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

Im vorhergehenden Code haben wir:

- Einen MCP-Client mit Server-URL und API-Schlüssel initialisiert.
- Zwei Sätze von Sampling-Parametern konfiguriert: einen für kreative Aufgaben und einen für faktische Aufgaben.
- Anfragen mit diesen Konfigurationen gesendet, wodurch das Modell für jede Aufgabe spezifische Tools nutzen kann.
- Die generierten Antworten ausgegeben, um die Wirkung verschiedener Sampling-Parameter zu demonstrieren.
- `allowedTools` verwendet, um anzugeben, welche Tools das Modell während der Generierung verwenden darf. In diesem Fall erlaubten wir für kreative Aufgaben die Tools `ideaGenerator` und `environmentalImpactTool` sowie für faktische Aufgaben `factChecker` und `dataAnalysisTool`.
- `temperature` verwendet, um die Zufälligkeit der Ausgabe zu steuern, wobei höhere Werte zu kreativeren Antworten führen.

- Verwendete `top_p`, um die Auswahl der Tokens auf diejenigen zu beschränken, die zur obersten kumulativen Wahrscheinlichkeitsmasse beitragen, wodurch die Qualität des generierten Textes verbessert wird.
- Verwendete `frequencyPenalty` und `presencePenalty`, um Wiederholungen zu reduzieren und Vielfalt im Output zu fördern.
- Verwendete `top_k`, um das Modell auf die Top-K wahrscheinlichsten Tokens zu beschränken, was dabei helfen kann, kohärentere Antworten zu erzeugen.

---

## Deterministisches Sampling

Für Anwendungen, die konsistente Ausgaben benötigen, sorgt deterministisches Sampling für reproduzierbare Ergebnisse. Dies erreicht es durch Verwendung eines festen Zufallssamens und Setzen der Temperatur auf null.

Schauen wir uns die folgende Beispielimplementierung an, um deterministisches Sampling in verschiedenen Programmiersprachen zu demonstrieren.

# [Java](#tab/java)

```java
// Java Beispiel: Deterministische Antworten mit festem Seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Verwendung eines festen Seeds für deterministische Ergebnisse
        
        // Erste Anfrage mit festem Seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Temperatur Null für maximale Determinismus
            .build();
            
        // Zweite Anfrage mit demselben Seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Beide Anfragen ausführen
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Die Antworten sollten aufgrund desselben Seeds und Temperatur=0 identisch sein
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Im vorangegangenen Code haben wir:

- Einen MCP-Client mit einer angegebenen Server-URL erstellt.
- Zwei Anfragen mit demselben Prompt, festem Seed und Temperatur null konfiguriert.
- Beide Anfragen gesendet und den generierten Text ausgegeben.
- Demonstriert, dass die Antworten aufgrund der deterministischen Natur der Sampling-Konfiguration identisch sind (gleicher Seed und Temperatur).
- `setSeed` verwendet, um einen festen Zufallssamen anzugeben, wodurch sichergestellt wird, dass das Modell bei derselben Eingabe immer dieselbe Ausgabe erzeugt.
- `temperature` auf null gesetzt, um maximale Determiniertheit sicherzustellen, d.h. das Modell wählt immer das wahrscheinlichste nächste Token ohne Zufall aus.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript Beispiel: Deterministische Antworten mit Seed-Steuerung
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Erste Anfrage mit festem Seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Temperatur Null für maximale Determinismus
    });
    
    // Zweite Anfrage mit gleichem Seed und Temperatur
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Dritte Anfrage mit anderem Seed aber gleicher Temperatur
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

Im vorangegangenen Code haben wir:

- Einen MCP-Client mit einer Server-URL initialisiert.
- Zwei Anfragen mit demselben Prompt, festem Seed und Temperatur null konfiguriert.
- Beide Anfragen gesendet und den generierten Text ausgegeben.
- Demonstriert, dass die Antworten aufgrund der deterministischen Natur der Sampling-Konfiguration identisch sind (gleicher Seed und Temperatur).
- `seed` verwendet, um einen festen Zufallssamen anzugeben, wodurch sichergestellt wird, dass das Modell bei derselben Eingabe immer dieselbe Ausgabe erzeugt.
- `temperature` auf null gesetzt, um maximale Determiniertheit sicherzustellen, d.h. das Modell wählt immer das wahrscheinlichste nächste Token ohne Zufall aus.
- Für die dritte Anfrage einen anderen Seed verwendet, um zu zeigen, dass eine Änderung des Seeds zu unterschiedlichen Ausgaben führt, selbst bei demselben Prompt und Temperatur.

---

## Dynamische Sampling-Konfiguration

Intelligentes Sampling passt Parameter basierend auf dem Kontext und den Anforderungen jeder Anfrage an. Das bedeutet, dass Parameter wie Temperatur, top_p und Strafwerte dynamisch je nach Aufgabentyp, Benutzerpräferenzen oder historischer Leistung angepasst werden.

Schauen wir uns an, wie man dynamisches Sampling in verschiedenen Programmiersprachen implementiert.

# [Python](#tab/python)

```python
# Python Beispiel: Dynamisches Sampling basierend auf dem Anfragekontext
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definieren von Sampling-Voreinstellungen für verschiedene Aufgabentypen
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Basis-Voreinstellung auswählen
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Anpassung basierend auf Benutzerpräferenzen, falls angegeben
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Skalierung der Temperatur basierend auf der Kreativitätspräferenz (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Anpassung von top_p basierend auf der gewünschten Antwortdiversität
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Erstellen und Senden der Anfrage mit benutzerdefinierten Sampling-Parametern
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Rückgabe der Antwort mit Sampling-Metadaten zur Transparenz
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Im vorangegangenen Code haben wir:

- Eine `DynamicSamplingService`-Klasse erstellt, die adaptives Sampling verwaltet.
- Sampling-Presets für verschiedene Aufgabentypen (kreativ, faktisch, Code, analytisch) definiert.
- Ein Basissampling-Preset basierend auf dem Aufgabentyp ausgewählt.
- Die Sampling-Parameter basierend auf Benutzerpräferenzen wie Kreativitätsgrad und Vielfalt angepasst.
- Die Anfrage mit den dynamisch konfigurierten Sampling-Parametern gesendet.
- Den generierten Text zusammen mit den angewandten Sampling-Parametern und dem Aufgabentyp zur Transparenz zurückgegeben.
- `temperature` verwendet, um die Zufälligkeit der Ausgabe zu steuern; höhere Werte führen zu kreativere Antworten.
- `top_p` verwendet, um die Auswahl der Tokens auf diejenigen zu beschränken, die zur obersten kumulativen Wahrscheinlichkeitsmasse beitragen, wodurch die Qualität des generierten Textes verbessert wird.
- `frequency_penalty` verwendet, um Wiederholungen zu reduzieren und Vielfalt im Output zu fördern.
- `user_preferences` verwendet, um die Sampling-Parameter auf Basis benutzerdefinierter Kreativitäts- und Vielfaltsstufen anzupassen.
- `task_type` verwendet, um die passende Sampling-Strategie für die Anfrage zu bestimmen, sodass Antworten besser auf die Natur der Aufgabe abgestimmt sind.
- `send_request`-Methode verwendet, um den Prompt mit den konfigurierten Sampling-Parametern zu senden, sodass das Modell Text gemäß den angegebenen Anforderungen generiert.
- `generated_text` verwendet, um die Antwort des Modells abzurufen, die dann zusammen mit den Sampling-Parametern und dem Aufgabentyp für weitere Analyse oder Anzeige zurückgegeben wird.
- `min`- und `max`-Funktionen verwendet, um sicherzustellen, dass Benutzerpräferenzen innerhalb gültiger Bereiche liegen und ungültige Sampling-Konfigurationen verhindert werden.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript-Beispiel: Dynamische Sampling-Konfiguration basierend auf dem Benutzerkontext
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Basis-Sampling-Profile definieren
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Historische Leistung verfolgen
    this.performanceHistory = [];
  }
  
  // Aufgabentyp aus Eingabeaufforderung erkennen
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Einfache heuristische Erkennung - könnte mit ML-Klassifikation verbessert werden
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
    
    // Standardmäßig auf Gesprächsmodus, wenn kein klarer Typ erkannt wird
    return 'conversational';
  }
  
  // Sampling-Parameter basierend auf Kontext und Benutzerpräferenzen berechnen
  getSamplingParameters(prompt, context = {}) {
    // Aufgabentyp erkennen
    const taskType = this.detectTaskType(prompt, context);
    
    // Basisprofil abrufen
    let params = {...this.samplingProfiles[taskType]};
    
    // Anpassung basierend auf Benutzerpräferenzen
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Von 1-10 auf den geeigneten Temperaturbereich skalieren
        params.temperature = 0.1 + (creativity * 0.09); // 0,1-1,0
      }
      
      if (precision !== undefined) {
        // Höhere Präzision bedeutet niedrigere topP (fokussiertere Auswahl)
        params.topP = 1.0 - (precision * 0.05); // 0,5-1,0
      }
      
      if (consistency !== undefined) {
        // Höhere Konsistenz bedeutet geringere Strafen
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0,1-0,9
      }
    }
    
    // Gelernte Anpassungen aus der Leistungshistorie anwenden
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Einfache adaptive Logik - könnte mit komplexeren Algorithmen verbessert werden
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Nur jüngste Historie berücksichtigen
    
    if (relevantHistory.length > 0) {
      // Durchschnittliche Leistungswerte berechnen
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Wenn die Leistung unter dem Schwellenwert liegt, Parameter anpassen
      if (avgScore < 0.7) {
        // Geringfügige Anpassung in Richtung sicherer Werte
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Leistung für zukünftige Anpassungen aufzeichnen
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Bewertung der Antwortqualität von 0-1
    });
    
    // Historiengröße begrenzen
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Optimierte Sampling-Parameter abrufen
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Anfrage mit optimierten Parametern senden
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Wenn der Benutzer Feedback gibt, dieses für zukünftige Optimierung aufzeichnen
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

// Beispielhafte Verwendung
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Kreative Aufgabe mit benutzerspezifischen Präferenzen
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Hohe Kreativität (1-10)
          consistency: 3  // Niedrige Konsistenz (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Programmieraufgabe
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Niedrige Kreativität
          precision: 8,   // Hohe Präzision
          consistency: 9  // Hohe Konsistenz
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

Im vorangegangenen Code haben wir:

- Eine `AdaptiveSamplingManager`-Klasse erstellt, die dynamisches Sampling basierend auf Aufgabentyp und Benutzerpräferenzen verwaltet.
- Sampling-Profile für verschiedene Aufgabentypen (kreativ, faktisch, Code, konversationell) definiert.
- Eine Methode implementiert, um den Aufgabentyp aus dem Prompt mit einfachen Heuristiken zu erkennen.
- Sampling-Parameter basierend auf dem erkannten Aufgabentyp und Benutzerpräferenzen berechnet.
- Gelernte Anpassungen basierend auf historischer Leistung angewandt, um Sampling-Parameter zu optimieren.
- Leistung für zukünftige Anpassungen protokolliert, sodass das System aus vergangenen Interaktionen lernen kann.
- Anfragen mit dynamisch konfigurierten Sampling-Parametern gesendet und den generierten Text zusammen mit den angewandten Parametern und erkannten Aufgabentyp zurückgegeben.
- Verwendet:
    - `userPreferences`, um die Sampling-Parameter basierend auf benutzerdefinierten Kreativitäts-, Präzisions- und Konsistenzstufen anzupassen.
    - `detectTaskType`, um die Natur der Aufgabe basierend auf dem Prompt zu bestimmen und so gezieltere Antworten zu ermöglichen.
    - `recordPerformance`, um die Leistung der generierten Antworten zu protokollieren, wodurch das System sich im Laufe der Zeit anpassen und verbessern kann.
    - `applyLearnedAdjustments`, um Sampling-Parameter basierend auf historischer Leistung zu modifizieren und so die Fähigkeit des Modells zur Erzeugung hochwertiger Antworten zu verbessern.
    - `generateResponse`, um den gesamten Prozess der Antwortgenerierung mit adaptivem Sampling zu kapseln, sodass er einfach mit unterschiedlichen Prompts und Kontexten aufgerufen werden kann.
    - `allowedTools`, um anzugeben, welche Werkzeuge das Modell während der Generierung nutzen darf, wodurch kontextbewusstere Antworten möglich sind.
    - `feedbackScore`, um Benutzern Feedback zur Qualität der generierten Antwort zu ermöglichen, das zur weiteren Verfeinerung der Modellleistung genutzt werden kann.
    - `performanceHistory`, um eine Aufzeichnung vergangener Interaktionen zu führen, sodass das System aus früheren Erfolgen und Misserfolgen lernen kann.
    - `getSamplingParameters`, um Sampling-Parameter dynamisch basierend auf dem Kontext der Anfrage anzupassen und so flexibleres und reaktionsschnelleres Modellverhalten zu erzielen.
    - `detectTaskType`, um die Aufgabe basierend auf dem Prompt zu klassifizieren, sodass das System geeignete Sampling-Strategien für verschiedene Anfragetypen anwenden kann.
    - `samplingProfiles`, um Basissampling-Konfigurationen für verschiedene Aufgabentypen zu definieren und schnelle Anpassungen basierend auf der Natur der Anfrage zu ermöglichen.

---

## Was kommt als Nächstes

- [5.7 Skalierung](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->