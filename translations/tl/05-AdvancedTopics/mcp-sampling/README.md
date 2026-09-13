> [!WARNING]
> Ang Sampling ay hindi na gagamitin sa MCP `2026-07-28`. Itong aralin ay pinananatili para sa
> mga legacy na implementasyon. Ang mga bagong server ay dapat direktang mag-integrate sa isang LLM
> provider API.

# Sampling sa Model Context Protocol

> Ang Sampling ay nananatili sa `2026-07-28` na espesipikasyon para sa compatibility at
> maaaring alisin sa unang rebisyon na ilalabas sa o pagkatapos ng Hulyo 28,
> 2027. Ang mga halimbawa sa araling ito ay maaaring gumamit ng SDK APIs na nag-iimplement ng `2025-11-25`.
> Tingnan ang [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md).

Sa mga legacy na implementasyon ng MCP, pinapayagan ng Sampling ang mga server na humiling ng LLM
completions sa pamamagitan ng kliyente. Ipinaliwanag ng araling ito ang deprecated na daloy ng protocol
para sa compatibility at gawain sa migrasyon.

## Panimula

Sa araling ito, susuriin natin kung paano i-configure ang mga parameter ng sampling sa mga MCP requests at unawain ang mga mekanismo ng underlying protocol ng sampling.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Maunawaan ang mga pangunahing parameter ng sampling na available sa MCP.
- I-configure ang mga parameter ng sampling para sa iba't ibang gamit.
- Magpatupad ng deterministic sampling para sa reproducible na resulta.
- Dynamic na i-adjust ang mga parameter ng sampling base sa konteksto at mga kagustuhan ng user.
- Ilapat ang mga estratehiya ng sampling para mapabuti ang performance ng modelo sa iba't ibang senaryo.
- Maunawaan kung paano gumagana ang sampling sa daloy ng client-server ng MCP.

## Paano Gumagana ang Sampling sa MCP

Ang daloy ng sampling sa MCP ay sumusunod sa mga hakbang na ito:

1. Nagpapadala ang server ng request na `sampling/createMessage` sa client
2. Sinusuri ng client ang request at maaaring baguhin ito
3. Nagsasagawa ang client ng sampling mula sa isang LLM
4. Sinusuri ng client ang completion
5. Ibinabalik ng client ang resulta sa server

Tinitiyak ng disenyo na ito na may human-in-the-loop na kontrol ang mga user sa nakikita at nililikha ng LLM.

## Pangkalahatang Pagsusuri sa mga Parameter ng Sampling

Itinatakda ng MCP ang mga sumusunod na parameter ng sampling na maaaring i-configure sa mga client requests:

| Parameter | Deskripsyon | Karaniwang Saklaw |
|-----------|-------------|-------------------|
| `temperature` | Kumokontrol sa pagkakaiba-iba sa pagpili ng token | 0.0 - 1.0 |
| `maxTokens` | Pinakamataas na bilang ng token na gagawin | Buong bilang |
| `stopSequences` | Mga custom na sequence na humihinto sa generation kapag na-encounter | Array ng mga string |
| `metadata` | Karagdagang provider-specific na mga parameter | JSON object |

Sinusuportahan ng maraming LLM provider ang karagdagang mga parameter sa pamamagitan ng `metadata` field, na maaaring kabilang ang:

| Karaniwang Extension Parameter | Deskripsyon | Karaniwang Saklaw |
|-----------|-------------|-------------------|
| `top_p` | Nucleus sampling - nililimitahan ang mga token sa top cumulative probability | 0.0 - 1.0 |
| `top_k` | Nililimitahan ang pagpili ng mga token sa top K na opsyon | 1 - 100 |
| `presence_penalty` | Pinaparusahan ang mga token base sa presensya nila sa teksto hanggang noon | -2.0 - 2.0 |
| `frequency_penalty` | Pinaparusahan ang mga token base sa kadalasan ng paglitaw sa teksto hanggang noon | -2.0 - 2.0 |
| `seed` | Tiyak na random seed para sa reproducible na resulta | Buong bilang |

## Halimbawa ng Request Format

Narito ang isang halimbawa ng paghingi ng sampling mula sa isang client sa MCP:

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

## Format ng Tugon

Ibinabalik ng client ang resulta ng completion:

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

## Mga Kontrol ng Tao sa Loop

Dinisenyo ang MCP sampling para sa human oversight:

- **Para sa mga prompt**:
  - Dapat ipakita ng mga client sa mga user ang iminungkahing prompt
  - Dapat kayang baguhin o tanggihan ng user ang mga prompt
  - Puwedeng i-filter o baguhin ang mga system prompt
  - Nakokontrol ng client kung isasama ang konteksto

- **Para sa mga completion**:
  - Dapat ipakita ng mga client sa user ang completion
  - Dapat kayang baguhin o tanggihan ng user ang mga completion
  - Puwedeng i-filter o baguhin ng client ang mga completion
  - Kontrolado ng user kung anong modelo ang gagamitin

Sa mga prinsipyong ito, tingnan natin kung paano ipapatupad ang sampling sa iba't ibang programming language, na nakatutok sa mga parameter na karaniwang sinusuportahan sa mga LLM provider.

## Mga Pagsasaalang-alang sa Seguridad

Kapag nagpapatupad ng sampling sa MCP, isaalang-alang ang mga pinakamahuhusay na kasanayan sa seguridad:

- **I-validate ang lahat ng nilalaman ng mensahe** bago ito ipadala sa client
- **Linisin ang sensitibong impormasyon** mula sa mga prompt at completion
- **Magpatupad ng rate limits** para maiwasan ang abuso
- **I-monitor ang paggamit ng sampling** para sa mga di-pangkaraniwang pattern
- **I-encrypt ang data habang naghahatid** gamit ang mga secure na protocol
- **Pangasiwaan ang privacy ng data ng user** ayon sa mga kaukulang regulasyon
- **I-audit ang mga hiling ng sampling** para sa pagsunod at seguridad
- **Kontrolin ang exposure sa gastos** gamit ang angkop na mga limitasyon
- **Magpatupad ng timeouts** para sa mga hiling ng sampling
- **Ayusin ang mga error ng modelo nang maayos** gamit ang angkop na fallback

Pinapayagan ng mga parameter ng sampling ang fine-tuning ng pag-uugali ng mga language model upang makamit ang nais na balanse sa pagitan ng deterministic at malikhaing mga output.

Tingnan natin kung paano i-configure ang mga parameter na ito sa iba't ibang programming language.

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

Sa code na nakaraang ipinakita ay:

- Nalikha ang isang MCP client na may tiyak na server URL.
- Na-configure ang isang request na may mga parameter ng sampling tulad ng `temperature`, `top_p`, at `top_k`.
- Naipadala ang request at na-print ang generated na teksto.
- Ginamit ang:
    - `allowedTools` para tukuyin kung aling mga tool ang pwedeng gamitin ng modelo habang nagge-generate. Sa kasong ito, pinayagan namin ang mga tool na `ideaGenerator` at `marketAnalyzer` upang tumulong sa pagbuo ng mga malikhaing ideya ng app.
    - `frequencyPenalty` at `presencePenalty` para kontrolin ang pag-uulit at pagkakaiba-iba sa output.
    - `temperature` para kontrolin ang randomness ng output, kung saan ang mas mataas na halaga ay nagreresulta sa mas malikhaing tugon.
    - `top_p` para limitahan ang pagpili ng mga token sa mga nakakatulong sa top cumulative probability mass, pinapabuti ang kalidad ng generated na teksto.
    - `top_k` para higpitan ang modelo sa top K na pinaka-malamang na mga token, na makatutulong sa pagbuo ng mas coherent na mga tugon.
    - `frequencyPenalty` at `presencePenalty` upang mabawasan ang pag-uulit at hikayatin ang pagkakaiba-iba sa generated na teksto.

# [JavaScript](#tab/javascript)

```javascript
// Halimbawa sa JavaScript: Pag-configure ng temperatura at Top-P sampling
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // I-initialize ang MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // I-configure ang request gamit ang iba't ibang mga parameter ng sampling
  const creativeSampling = {
    temperature: 0.9,    // Mas mataas na temperatura = mas maraming randomness/kreatibidad
    topP: 0.92,          // Isaalang-alang ang mga token na may nangungunang 92% na probability mass
    frequencyPenalty: 0.6, // Bawasan ang pag-uulit ng mga pagkakasunud-sunod ng token
    presencePenalty: 0.4   // Parusahan ang mga token na lumitaw na sa teksto hanggang ngayon
  };
  
  const factualSampling = {
    temperature: 0.2,    // Mas mababang temperatura = mas deterministic/totoo sa katotohanan
    topP: 0.85,          // Bahagyang mas nakatutok na pagpili ng token
    frequencyPenalty: 0.2, // Minimal na parusa sa pag-uulit
    presencePenalty: 0.1   // Minimal na parusa sa presensya
  };
  
  try {
    // Magpadala ng dalawang request na may iba't ibang sampling na mga configuration
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

Sa code na nakaraang ipinakita ay:

- Na-initialize ang isang MCP client na may server URL at API key.
- Na-configure ang dalawang set ng sampling parameters: isa para sa malikhaing gawain at isa pa para sa mga factual na gawain.
- Naipadala ang mga request na may ganitong mga configuration, pinapayagan ang modelo na gumamit ng mga specific na tool para sa bawat gawain.
- Na-print ang mga generated na tugon upang ipakita ang epekto ng iba't ibang mga parameter ng sampling.
- Ginamit ang `allowedTools` para tukuyin kung aling mga tool ang pwedeng gamitin ng modelo habang nagge-generate. Sa kasong ito, pinayagan namin ang mga tool na `ideaGenerator` at `environmentalImpactTool` para sa malikhaing gawain, at `factChecker` at `dataAnalysisTool` para sa mga factual na gawain.
- Ginamit ang `temperature` para kontrolin ang randomness ng output, kung saan ang mas mataas na halaga ay nagreresulta sa mas malikhaing tugon.
- Ginamit ang `top_p` para limitahan ang pagpili ng mga token sa mga nakakatulong sa top cumulative probability mass, pinapabuti ang kalidad ng generated na teksto.
- Ginamit ang `frequencyPenalty` at `presencePenalty` upang mabawasan ang pag-uulit at hikayatin ang pagkakaiba-iba sa output.
- Ginamit ang `top_k` upang higpitan ang modelo sa top K na pinaka-malamang na mga token, na makatutulong sa pagbuo ng mas coherent na mga tugon.

---

## Deterministic Sampling

Para sa mga aplikasyon na nangangailangan ng consistent na output, tinitiyak ng deterministic sampling ang reproducible na resulta. Ginagawa ito sa pamamagitan ng paggamit ng fixed na random seed at pag-set ng temperature sa zero.

Tingnan natin ang sample na implementasyon sa ibaba upang ipakita ang deterministic sampling sa iba't ibang programming language.

# [Java](#tab/java)

```java
// Halimbawa sa Java: Deterministikong mga sagot gamit ang nakatakdang buto
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Paggamit ng nakatakdang buto para sa deterministikong mga resulta
        
        // Unang kahilingan gamit ang nakatakdang buto
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperatura para sa pinakamataas na determinismo
            .build();
            
        // Pangalawang kahilingan gamit ang parehong buto
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Ipatupad ang parehong mga kahilingan
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Dapat magkapareho ang mga sagot dahil sa parehong buto at temperatura=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Sa code na nakaraang ipinakita ay:

- Nalikha ang isang MCP client na may tinukoy na server URL.
- Na-configure ang dalawang request na may parehong prompt, fixed seed, at zero temperature.
- Naipadala ang parehong request at na-print ang generated na teksto.
- Ipinakita na magkapareho ang mga tugon dahil sa deterministic na katangian ng sampling configuration (parehong seed at temperature).
- Ginamit ang `setSeed` para tukuyin ang fixed random seed, tinitiyak na lilikha ang modelo ng parehong output para sa parehong input sa lahat ng pagkakataon.
- In-set ang `temperature` sa zero upang matiyak ang maximum na determinismo, ibig sabihin ay palaging pipiliin ng modelo ang pinaka-malamang susunod na token nang walang randomness.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Halimbawa ng JavaScript: Deterministikong mga tugon na may kontrol sa binhi
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Unang kahilingan na may nakapirming binhi
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero na temperatura para sa pinakamataas na determinismo
    });
    
    // Pangalawang kahilingan na may parehong binhi at temperatura
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Pangatlong kahilingan na may ibang binhi ngunit parehong temperatura
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

Sa code na nakaraang ipinakita ay:

- Na-initialize ang isang MCP client na may server URL.
- Na-configure ang dalawang request na may parehong prompt, fixed seed, at zero temperature.
- Naipadala ang parehong request at na-print ang generated na teksto.
- Ipinakita na magkapareho ang mga tugon dahil sa deterministic na katangian ng sampling configuration (parehong seed at temperature).
- Ginamit ang `seed` para tukuyin ang fixed random seed, tinitiyak na lilikha ang modelo ng parehong output para sa parehong input sa lahat ng pagkakataon.
- In-set ang `temperature` sa zero upang matiyak ang maximum na determinismo, ibig sabihin ay palaging pipiliin ng modelo ang pinaka-malamang susunod na token nang walang randomness.
- Ginamit ang ibang seed para sa ikatlong request upang ipakita na ang pagbabago ng seed ay nagreresulta sa ibang mga output, kahit na pareho ang prompt at temperature.

---

## Dynamic na Pag-configure ng Sampling

Ang intelligent sampling ay ina-adjust ang mga parameter base sa konteksto at pangangailangan ng bawat request. Ibig sabihin, dynamic na ina-adjust ang mga parameter tulad ng temperature, top_p, at penalties base sa uri ng gawain, mga kagustuhan ng user, o historical performance.

Tingnan natin kung paano ipapatupad ang dynamic sampling sa iba't ibang programming language.

# [Python](#tab/python)

```python
# Halimbawa ng Python: Dinamikong sampling batay sa konteksto ng kahilingan
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Tukuyin ang mga preset ng sampling para sa iba't ibang uri ng gawain
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Piliin ang base na preset
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Ayusin batay sa mga kagustuhan ng user kung ibinigay
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Iskalara ang temperatura batay sa kagustuhan sa pagiging malikhain (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Ayusin ang top_p batay sa nais na pagkakaiba-iba ng tugon
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Lumikha at magpadala ng kahilingan gamit ang pasadyang mga parameter ng sampling
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Ibalik ang tugon na may metadata ng sampling para sa transparency
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Sa code na nakaraang ipinakita ay:

- Nalikha ang isang `DynamicSamplingService` class na namamahala ng adaptive sampling.
- Nag-define ng mga sampling preset para sa iba't ibang uri ng gawain (malikhain, totoo, code, analytical).
- Pinili ang base sampling preset batay sa uri ng gawain.
- In-adjust ang mga parameter ng sampling base sa mga kagustuhan ng user, tulad ng antas ng creativity at pagkakaiba-iba.
- Naipadala ang request na may dynamic na naka-configure na mga parameter ng sampling.
- Ibinalik ang generated na teksto kasama ang mga inilapat na parameter ng sampling at uri ng gawain para sa transparency.
- Ginamit ang `temperature` para kontrolin ang randomness ng output, kung saan ang mas mataas na halaga ay nagreresulta sa mas malikhaing tugon.
- Ginamit ang `top_p` para limitahan ang pagpili ng mga token sa mga nakakatulong sa top cumulative probability mass, pinapabuti ang kalidad ng generated na teksto.
- Ginamit ang `frequency_penalty` upang mabawasan ang pag-uulit at hikayatin ang pagkakaiba-iba sa output.
- Ginamit ang `user_preferences` upang payagan ang pag-customize ng mga parameter ng sampling base sa antas ng creativity at diversity na itinakda ng user.
- Ginamit ang `task_type` upang tukuyin ang angkop na estratehiya ng sampling para sa request, na nagbibigay-daan sa mas angkop na mga tugon base sa kalikasan ng gawain.
- Ginamit ang `send_request` method upang ipadala ang prompt na may naka-configure na mga parameter ng sampling, tinitiyak na ang modelo ay gagawa ng teksto ayon sa tinukoy na mga pangangailangan.
- Ginamit ang `generated_text` upang makuha ang tugon ng modelo, na pagkatapos ay ibinalik kasama ang mga parameter ng sampling at uri ng gawain para sa karagdagang pagsusuri o pagpapakita.
- Ginamit ang mga `min` at `max` na function upang tiyakin na ang mga kagustuhan ng user ay nasa loob ng wastong mga saklaw, na pumipigil sa invalid na configuration ng sampling.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// Halimbawa ng JavaScript: Dinamikong pagsasaayos ng sampling batay sa konteksto ng user
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Tukuyin ang mga pangunahing profiling ng sampling
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Subaybayan ang kasaysayan ng pagganap
    this.performanceHistory = [];
  }
  
  // Tuklasin ang uri ng gawain mula sa prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Simpleng heuristic na pagtuklas - maaaring mapabuti gamit ang ML classification
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
    
    // Default sa conversational kung walang malinaw na uri na natuklasan
    return 'conversational';
  }
  
  // Kalkulahin ang mga parameter ng sampling batay sa konteksto at mga kagustuhan ng user
  getSamplingParameters(prompt, context = {}) {
    // Tuklasin ang uri ng gawain
    const taskType = this.detectTaskType(prompt, context);
    
    // Kuhanin ang pangunahing profile
    let params = {...this.samplingProfiles[taskType]};
    
    // I-adjust batay sa mga kagustuhan ng user
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Iskalahin mula 1-10 sa angkop na saklaw ng temperatura
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Mas mataas na precision ay nangangahulugan ng mas mababang topP (mas nakatuon na pagpili)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Mas mataas na consistency ay nangangahulugan ng mas mababang penalties
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Ilapat ang mga natutunang pagbabago mula sa kasaysayan ng pagganap
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Simpleng adaptive na lohika - maaaring mapahusay gamit ang mas sopistikadong mga algorithm
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Isaalang-alang lamang ang kamakailang kasaysayan
    
    if (relevantHistory.length > 0) {
      // Kalkulahin ang average na mga puntos ng pagganap
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Kung ang pagganap ay mababa sa threshold, i-adjust ang mga parameter
      if (avgScore < 0.7) {
        // Bahagyang pagbabago patungo sa mas ligtas na mga halaga
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Irekord ang pagganap para sa mga susunod na pagbabago
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 na rating ng kalidad ng tugon
    });
    
    // Limitahan ang laki ng kasaysayan
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Kuhanin ang naoptimize na mga parameter ng sampling
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Magpadala ng kahilingan gamit ang naoptimize na mga parameter
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Kung magbibigay ng feedback ang user, irekord ito para sa susunod na pag-optimize
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

// Halimbawa ng paggamit
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Malikhaing gawain na may pasadyang kagustuhan ng user
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Mataas na pagkamalikhain (1-10)
          consistency: 3  // Mababang consistency (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Gawain sa paggawa ng code
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Mababang pagkamalikhain
          precision: 8,   // Mataas na precision
          consistency: 9  // Mataas na consistency
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

Sa code na nakaraang ipinakita ay:

- Nalikha ang isang `AdaptiveSamplingManager` class na namamahala ng dynamic sampling base sa uri ng gawain at mga kagustuhan ng user.
- Nag-define ng mga sampling profile para sa iba't ibang uri ng gawain (malikhain, totoo, code, conversational).
- Nagpatupad ng method upang tukuyin ang uri ng gawain mula sa prompt gamit ang simpleng heuristics.
- Kinuwenta ang mga parameter ng sampling base sa natukoy na uri ng gawain at mga kagustuhan ng user.
- Inaplay ang mga natutunang adjustment base sa historical performance upang i-optimize ang mga parameter ng sampling.
- Naitala ang performance para sa mga susunod na adjustment, na nagbibigay-daan sa sistema na matuto mula sa mga nakaraang interaksyon.
- Naipadala ang mga request na may dynamic na naka-configure na mga parameter ng sampling at ibinalik ang generated na teksto kasama ang inilapat na mga parameter at natukoy na uri ng gawain.
- Ginamit ang:
    - `userPreferences` upang payagan ang pag-customize ng mga parameter ng sampling base sa itinakdang antas ng creativity, precision, at consistency ng user.
    - `detectTaskType` upang tukuyin ang kalikasan ng gawain base sa prompt, na nagbibigay-daan sa mas angkop na mga tugon.
    - `recordPerformance` upang i-log ang performance ng mga generated na tugon, na nagpapahintulot sa sistema na umangkop at mapabuti sa paglipas ng panahon.
    - `applyLearnedAdjustments` upang baguhin ang mga parameter ng sampling base sa historical performance, pinapahusay ang kakayahan ng modelo na lumikha ng mataas na kalidad na mga tugon.
    - `generateResponse` upang gawing buo ang proseso ng paggawa ng tugon gamit ang adaptive sampling, na nagpapadali ng pagtawag sa iba't ibang prompt at konteksto.
    - `allowedTools` upang tukuyin kung aling mga tool ang maaaring gamitin ng modelo habang nagge-generate, na nagpapahintulot ng mas konteksto-aware na mga tugon.
    - `feedbackScore` upang payagan ang mga user na magbigay ng feedback sa kalidad ng generated na tugon, na maaaring gamitin upang lalong pinuhin ang performance ng modelo sa paglipas ng panahon.
    - `performanceHistory` upang panatilihin ang talaan ng mga nakaraang interaksyon, na nagpapahintulot sa sistema na matuto mula sa mga tagumpay at pagkabigo.
    - `getSamplingParameters` upang dynamic na ia-adjust ang mga parameter ng sampling base sa konteksto ng request, na nagbibigay-daan para sa mas flexible at responsive na pag-uugali ng modelo.
    - `detectTaskType` upang klasipikahin ang gawain base sa prompt, na nagpapahintulot sa sistema na mag-aplay ng angkop na mga estratehiya ng sampling para sa iba't ibang uri ng request.
    - `samplingProfiles` upang magtakda ng base sampling configuration para sa iba't ibang uri ng gawain, na nagpapahintulot ng mabilis na adjustment base sa kalikasan ng request.

---

## Ano ang susunod

- [5.7 Scaling](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->