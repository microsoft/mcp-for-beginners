# Mudeli konteksti protokolli proovivõtmine

Proovivõtmine on võimas MCP funktsioon, mis võimaldab serveritel taotleda LLM-i täiendusi kliendi kaudu, pakkudes keerukaid agentlikke käitumisi, säilitades samal ajal turvalisuse ja privaatsuse. Õige proovivõtmise konfiguratsioon võib märkimisväärselt parandada vastuste kvaliteeti ja jõudlust. MCP pakub standardiseeritud viisi, kuidas kontrollida mudelite tekstigeneratsiooni konkreetsete parameetritega, mis mõjutavad juhuslikkust, loovust ja sidusust.

## Sissejuhatus

Selles õppetükis uurime, kuidas konfigureerida proovivõtmise parameetreid MCP taotlustes ja mõista proovivõtmise aluseks olevaid protokollimehhanisme.

## Õppe-eesmärgid

Selle õppetüki lõpuks oskate:

- Mõista MCP-s saadaval olevaid proovivõtmise põhiparameetreid.
- Konfigureerida proovivõtmise parameetreid erinevate kasutusjuhtude jaoks.
- Rakendada deterministlikku proovivõtmist reprodutseeritavate tulemuste saavutamiseks.
- Dünaamiliselt kohandada proovivõtmise parameetreid vastavalt kontekstile ja kasutaja eelistustele.
- Rakendada proovivõtmise strateegiaid mudeli jõudluse parandamiseks erinevates olukordades.
- Mõista, kuidas proovivõtmine toimib MCP kliendi-serveri voos.

## Kuidas proovivõtmine MCP-s toimib

Proovivõtmise voog MCP-s järgib järgmisi samme:

1. Server saadab kliendile `sampling/createMessage` taotluse.
2. Klient vaatab taotluse üle ja võib seda muuta.
3. Klient teeb LLM-i põhjal proovivõtmise.
4. Klient vaatab täienduse üle.
5. Klient tagastab tulemuse serverile.

See inimese-kontrolli-mehhanism tagab, et kasutajad säilitavad kontrolli selle üle, mida LLM näeb ja genereerib.

## Proovivõtmise parameetrite ülevaade

MCP määratleb järgmised proovivõtmise parameetrid, mida saab kliendi taotlustes konfigureerida:

| Parameeter | Kirjeldus | Tüüpiline vahemik |
|------------|-----------|-------------------|
| `temperature` | Kontrollib juhuslikkust tokenite valikul | 0.0 - 1.0 |
| `maxTokens` | Maksimaalne genereeritavate tokenite arv | Täisarv |
| `stopSequences` | Kohandatud järjestused, mis peatavad genereerimise nende ilmumisel | Stringide massiiv |
| `metadata` | Täiendavad teenusepakkuja-spetsiifilised parameetrid | JSON objekt |

Paljud LLM-i teenusepakkujad toetavad täiendavaid parameetreid `metadata` välja kaudu, mis võivad sisaldada:

| Tavaline laiendusparameeter | Kirjeldus | Tüüpiline vahemik |
|-----------------------------|-----------|-------------------|
| `top_p` | Tuumaproovivõtmine - piirab tokenid kumulatiivse tõenäosuse järgi | 0.0 - 1.0 |
| `top_k` | Piirab tokenite valiku top K valikutega | 1 - 100 |
| `presence_penalty` | Karistab tokenite kordumist tekstis | -2.0 - 2.0 |
| `frequency_penalty` | Karistab tokenite sagedust tekstis | -2.0 - 2.0 |
| `seed` | Konkreetne juhuslik seeme reprodutseeritavate tulemuste jaoks | Täisarv |

## Näidistaotluse formaat

Siin on näide, kuidas taotleda proovivõtmist MCP kliendilt:

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

## Vastuse formaat

Klient tagastab täienduse tulemuse:

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

## Inimese kontrolli mehhanismid

MCP proovivõtmine on loodud inimeste järelevalvega:

- **Päringute jaoks**:
  - Kliendid peaksid kasutajatele näitama kavandatud päringut.
  - Kasutajatel peaks olema võimalus päringut muuta või tagasi lükata.
  - Süsteemi päringuid saab filtreerida või muuta.
  - Konteksti lisamine on kliendi kontrolli all.

- **Täienduste jaoks**:
  - Kliendid peaksid kasutajatele näitama täiendust.
  - Kasutajatel peaks olema võimalus täiendust muuta või tagasi lükata.
  - Kliendid võivad täiendusi filtreerida või muuta.
  - Kasutajad kontrollivad, millist mudelit kasutatakse.

Nende põhimõtete järgimisel vaatame, kuidas rakendada proovivõtmist erinevates programmeerimiskeeltes, keskendudes parameetritele, mida LLM-i teenusepakkujad tavaliselt toetavad.

## Turvalisuse kaalutlused

MCP-s proovivõtmise rakendamisel arvestage järgmiste turvalisuse parimate tavadega:

- **Kontrollige kogu sõnumi sisu**, enne kui see kliendile saadetakse.
- **Eemaldage tundlik teave** päringutest ja täiendustest.
- **Rakendage kiiruspiiranguid**, et vältida kuritarvitamist.
- **Jälgige proovivõtmise kasutust**, et tuvastada ebatavalisi mustreid.
- **Krüpteerige andmed edastamisel**, kasutades turvalisi protokolle.
- **Käsitlege kasutajaandmete privaatsust** vastavalt kehtivatele regulatsioonidele.
- **Auditeerige proovivõtmise taotlusi**, et tagada vastavus ja turvalisus.
- **Kontrollige kulude piiramist** sobivate limiitidega.
- **Rakendage taotluste ajalimiite**.
- **Käsitlege mudeli vigu sujuvalt**, kasutades sobivaid varulahendusi.

Proovivõtmise parameetrid võimaldavad keelemudelite käitumist peenhäälestada, et saavutada soovitud tasakaal deterministlike ja loovate väljundite vahel.

Vaatame, kuidas neid parameetreid konfigureerida erinevates programmeerimiskeeltes.

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

Eelnevas koodis oleme:

- Loonud MCP kliendi konkreetse serveri URL-iga.
- Konfigureerinud taotluse proovivõtmise parameetritega nagu `temperature`, `top_p` ja `top_k`.
- Saatnud taotluse ja printinud genereeritud teksti.
- Kasutanud:
    - `allowedTools`, et määrata, milliseid tööriistu mudel võib genereerimise ajal kasutada. Antud juhul lubasime tööriistadel `ideaGenerator` ja `marketAnalyzer` aidata loovate rakenduste ideede genereerimisel.
    - `frequencyPenalty` ja `presencePenalty`, et kontrollida kordusi ja mitmekesisust väljundis.
    - `temperature`, et kontrollida väljundi juhuslikkust, kus kõrgemad väärtused viivad loovamate vastusteni.
    - `top_p`, et piirata tokenite valikut nendele, mis aitavad kaasa kumulatiivse tõenäosuse massile, parandades genereeritud teksti kvaliteeti.
    - `top_k`, et piirata mudelit top K kõige tõenäolisemate tokenite valikuga, mis aitab genereerida sidusamaid vastuseid.
    - `frequencyPenalty` ja `presencePenalty`, et vähendada kordusi ja soodustada mitmekesisust genereeritud tekstis.

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

Eelnevas koodis oleme:

- Initsialiseerinud MCP kliendi serveri URL-i ja API võtmega.
- Konfigureerinud kaks proovivõtmise parameetrite komplekti: ühe loovate ülesannete jaoks ja teise faktipõhiste ülesannete jaoks.
- Saatnud taotlused nende konfiguratsioonidega, võimaldades mudelil kasutada konkreetseid tööriistu iga ülesande jaoks.
- Printinud genereeritud vastused, et näidata erinevate proovivõtmise parameetrite mõju.
- Kasutanud `allowedTools`, et määrata, milliseid tööriistu mudel võib genereerimise ajal kasutada. Antud juhul lubasime tööriistadel `ideaGenerator` ja `environmentalImpactTool` loovate ülesannete jaoks ning `factChecker` ja `dataAnalysisTool` faktipõhiste ülesannete jaoks.
- Kasutanud `temperature`, et kontrollida väljundi juhuslikkust, kus kõrgemad väärtused viivad loovamate vastusteni.
- Kasutanud `top_p`, et piirata tokenite valikut nendele, mis aitavad kaasa kumulatiivse tõenäosuse massile, parandades genereeritud teksti kvaliteeti.
- Kasutanud `frequencyPenalty` ja `presencePenalty`, et vähendada kordusi ja soodustada mitmekesisust väljundis.
- Kasutanud `top_k`, et piirata mudelit top K kõige tõenäolisemate tokenite valikuga, mis aitab genereerida sidusamaid vastuseid.

---

## Deterministlik proovivõtmine

Rakenduste jaoks, mis vajavad järjepidevaid väljundeid, tagab deterministlik proovivõtmine reprodutseeritavad tulemused. Seda tehakse, kasutades fikseeritud juhuslikku seemet ja määrates temperatuuri nulliks.

Vaatame allpool näidisrakendust, et demonstreerida deterministlikku proovivõtmist erinevates programmeerimiskeeltes.

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

Eelnevas koodis oleme:

- Loonud MCP kliendi määratud serveri URL-iga.
- Konfigureerinud kaks taotlust sama päringu, fikseeritud seemne ja nulltemperatuuriga.
- Saatnud mõlemad taotlused ja printinud genereeritud teksti.
- Näidanud, et vastused on identsed tänu proovivõtmise konfiguratsiooni deterministlikule olemusele (sama seeme ja temperatuur).
- Kasutanud `setSeed`, et määrata fikseeritud juhuslik seeme, tagades, et mudel genereerib sama sisendi jaoks alati sama väljundi.
- Määranud `temperature` nulliks, et tagada maksimaalne determinism, mis tähendab, et mudel valib alati kõige tõenäolisema järgmise tokeni ilma juhuslikkuseta.

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

Eelnevas koodis oleme:

- Initsialiseerinud MCP kliendi serveri URL-iga.
- Konfigureerinud kaks taotlust sama päringu, fikseeritud seemne ja nulltemperatuuriga.
- Saatnud mõlemad taotlused ja printinud genereeritud teksti.
- Näidanud, et vastused on identsed tänu proovivõtmise konfiguratsiooni deterministlikule olemusele (sama seeme ja temperatuur).
- Kasutanud `seed`, et määrata fikseeritud juhuslik seeme, tagades, et mudel genereerib sama sisendi jaoks alati sama väljundi.
- Määranud `temperature` nulliks, et tagada maksimaalne determinism, mis tähendab, et mudel valib alati kõige tõenäolisema järgmise tokeni ilma juhuslikkuseta.
- Kasutanud erinevat seemet kolmandas taotluses, et näidata, et seemne muutmine toob kaasa erinevad väljundid, isegi sama päringu ja temperatuuri korral.

---

## Dünaamiline proovivõtmise konfiguratsioon

Intelligentne proovivõtmine kohandab parameetreid vastavalt iga taotluse kontekstile ja nõuetele. See tähendab parameetrite nagu temperatuur, top_p ja karistused dünaamilist kohandamist vastavalt ülesande tüübile, kasutaja eelistustele või ajaloolisele jõudlusele.

Vaatame, kuidas rakendada dünaamilist proovivõtmist erinevates programmeerimiskeeltes.

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

Eelnevas koodis oleme:

- Loonud klassi `DynamicSamplingService`, mis haldab adaptiivset proovivõtmist.
- Määratlenud proovivõtmise eelseaded erinevate ülesannetüüpide jaoks (loov, faktipõhine, kood, analüütiline).
- Valinud baaseelseade proovivõtmise jaoks vastavalt ülesande tüübile.
- Kohandanud proovivõtmise parameetreid vastavalt kasutaja eelistustele, nagu loovuse tase ja mitmekesisus.
- Saatnud taotluse dünaamiliselt konfigureeritud proovivõtmise parameetritega.
- Tagastanud genereeritud teksti koos rakendatud proovivõtmise parameetrite ja ülesande tüübiga läbipaistvuse huvides.
- Kasutanud `temperature`, et kontrollida väljundi juhuslikkust, kus kõrgemad väärtused viivad loovamate vastusteni.
- Kasutanud `top_p`, et piirata tokenite valikut nendele, mis aitavad kaasa kumulatiivse tõenäosuse massile, parandades genereeritud teksti kvaliteeti.
- Kasutanud `frequency_penalty`, et vähendada kordusi ja soodustada mitmekesisust väljundis.
- Kasutanud `user_preferences`, et võimaldada proovivõtmise parameetrite kohandamist vastavalt kasutaja määratud loovuse ja mitmekesisuse tasemele.
- Kasutanud `task_type`, et määrata taotluse jaoks sobiv proovivõtmise strateegia, võimaldades ülesande olemusest lähtuvaid vastuseid.
- Kasutanud `send_request` meetodit, et saata päring konfigureeritud proovivõtmise parameetritega, tagades, et mudel genereerib teksti vastavalt määratud nõuetele.
- Kasutanud `generated_text`, et saada mudeli vastus, mis seejärel tagastatakse koos proovivõtmise parameetrite ja ülesande tüübiga edasiseks analüüsiks või kuvamiseks.
- Kasutanud `min` ja `max` funktsioone, et tagada kasutaja eelistuste piiramine kehtivate vahemikega, vältides kehtetuid proovivõtmise konfiguratsioone.

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

Eelnevas koodis oleme:

- Loonud klassi `AdaptiveSamplingManager`, mis haldab dünaamilist proovivõtmist vastavalt ülesande tüübile ja kasutaja eelistustele.
- Määratlenud proovivõtmise profiilid erinevate ülesandetüüpide jaoks (loov, faktipõhine, kood, vestlus).
- Rakendanud meetodi ülesande tüübi tuvastamiseks päringust, kasutades lihtsaid heuristikuid.
- Arvutanud proovivõtmise parameetrid tuvastatud ülesande tüübi ja kasutaja eelistuste põhjal.
- Rakendanud õpitud kohandusi ajaloolise jõudluse põhjal, et optimeerida proovivõtmise parameetreid.
- Salvestanud jõudluse tulevaseks kohandamiseks, võimaldades süsteemil varasematest interaktsioonidest õppida.
- Saatnud taotlused dünaamiliselt konfigureeritud proovivõtmise parameetritega ja tagastanud genereeritud teksti koos rakendatud parameetrite ja tuvastatud ülesande tüübiga.
- Kasutanud:
    - `userPreferences`, et võimaldada proovivõtmise parameetrite kohandamist vastavalt kasutaja määratud loovuse, täpsuse ja järjepidevuse tasemele.
    - `detectTaskType`, et määrata ülesande olemus päringu põhjal, võimaldades täpsemaid vastuseid.
    - `recordPerformance`, et logida genereeritud vastuste jõudlust, võimaldades süsteemil kohaneda ja aja jooksul paraneda.
    - `applyLearnedAdjustments`, et muuta proovivõtmise parameetreid ajaloolise jõudluse põhjal, parandades mudeli võimet genereerida kvaliteetseid vastuseid.
    - `generateResponse`, et kapseldada kogu protsess vastuse genereerimiseks adaptiivse proovivõtmisega, muutes selle lihtsaks erinevate päringute ja kontekstide jaoks.
    - `allowedTools`, et määrata, milliseid tööriistu mudel võib genereerimise ajal kasutada, võimaldades kontekstiteadlikumaid vastuseid.
    - `feedbackScore`, et võimaldada kasutajatel anda tagasisidet genereeritud vastuse kvaliteedi kohta, mida saab kasutada mudeli jõudluse edasiseks täiendamiseks.
    - `performanceHistory`, et säilitada varasemate interaktsioonide arvestust, võimaldades süsteemil õppida varasematest õnnestumistest ja ebaõnnestumistest.
    - `getSamplingParameters`, et dünaamiliselt kohandada proovivõtmise parameetreid vastavalt taotluse kontekstile, võimaldades paindlikumat ja reageerivamat mudeli käitumist.
    - `detectTaskType`, et klassifitseerida ülesanne päringu põhjal, võimaldades süsteemil rakendada sobivaid proovivõtmise strateegiaid erinevat tüüpi taotluste jaoks.
    - `samplingProfiles`, et määratleda baaskonfiguratsioonid erinevate ülesandetüüpide jaoks, võimaldades kiiret kohandamist vastavalt taotluse olemusele.

---

## Mis edasi

- [5.7 Skaalumine](../

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.