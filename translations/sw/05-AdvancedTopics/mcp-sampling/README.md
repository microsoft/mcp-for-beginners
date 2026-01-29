# Sampuli katika Itifaki ya Muktadha wa Mfano

Sampuli ni kipengele chenye nguvu cha MCP kinachowezesha seva kuomba ukamilishaji wa LLM kupitia mteja, kuruhusu tabia za wakala wa hali ya juu huku ikidumisha usalama na faragha. Usanidi sahihi wa sampuli unaweza kuboresha kwa kiasi kikubwa ubora wa majibu na utendaji. MCP hutoa njia ya kawaida ya kudhibiti jinsi mifano inavyotengeneza maandishi kwa vigezo maalum vinavyoathiri nasibu, ubunifu, na muendelezo.

## Utangulizi

Katika somo hili, tutaangazia jinsi ya kusanidi vigezo vya sampuli katika maombi ya MCP na kuelewa mbinu za msingi za itifaki ya sampuli.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelewa vigezo muhimu vya sampuli vinavyopatikana katika MCP.
- Kusanidi vigezo vya sampuli kwa matumizi tofauti.
- Kutekeleza sampuli ya uhakika kwa matokeo yanayoweza kurudiwa.
- Kubadilisha vigezo vya sampuli kwa nguvu kulingana na muktadha na mapendeleo ya mtumiaji.
- Kutumia mikakati ya sampuli kuboresha utendaji wa mfano katika hali mbalimbali.
- Kuelewa jinsi sampuli inavyofanya kazi katika mtiririko wa mteja-seva wa MCP.

## Jinsi Sampuli Inavyofanya Kazi katika MCP

Mtiririko wa sampuli katika MCP unafuata hatua hizi:

1. Seva inatuma ombi la `sampling/createMessage` kwa mteja
2. Mteja anakagua ombi na anaweza kulibadilisha
3. Mteja huchukua sampuli kutoka kwa LLM
4. Mteja anakagua ukamilishaji
5. Mteja hurudisha matokeo kwa seva

Muundo huu wa mtu katika mzunguko unahakikisha watumiaji wanadumisha udhibiti juu ya kile LLM kinachoona na kutengeneza.

## Muhtasari wa Vigezo vya Sampuli

MCP inaeleza vigezo vifuatavyo vya sampuli vinavyoweza kusanidiwa katika maombi ya mteja:

| Kigezo | Maelezo | Mzunguko wa Kawaida |
|--------|----------|---------------------|
| `temperature` | Hudhibiti nasibu katika uchaguzi wa tokeni | 0.0 - 1.0 |
| `maxTokens` | Idadi kubwa ya tokeni za kuzalisha | Thamani ya nambari kamili |
| `stopSequences` | Mfululizo maalum unaosimamisha uzalishaji ukipatikana | Orodha ya mistari |
| `metadata` | Vigezo vya ziada maalum kwa mtoa huduma | Kitu cha JSON |

Watoa huduma wengi wa LLM huunga mkono vigezo vya ziada kupitia uwanja wa `metadata`, ambao unaweza kujumuisha:

| Kigezo cha Ziada Kinachojulikana | Maelezo | Mzunguko wa Kawaida |
|----------------------------------|----------|---------------------|
| `top_p` | Sampuli ya Nucleus - huweka kikomo tokeni kwa uwezekano wa juu wa jumla | 0.0 - 1.0 |
| `top_k` | Huweka kikomo uchaguzi wa tokeni kwa chaguzi K bora | 1 - 100 |
| `presence_penalty` | Hulaumu tokeni kulingana na uwepo wake katika maandishi hadi sasa | -2.0 - 2.0 |
| `frequency_penalty` | Hulaumu tokeni kulingana na mara ngapi zimeonekana katika maandishi hadi sasa | -2.0 - 2.0 |
| `seed` | Mbegu maalum ya nasibu kwa matokeo yanayoweza kurudiwa | Thamani ya nambari kamili |

## Mfano wa Muundo wa Ombi

Hapa kuna mfano wa kuomba sampuli kutoka kwa mteja katika MCP:

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

## Muundo wa Jibu

Mteja hurudisha matokeo ya ukamilishaji:

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

## Udhibiti wa Mtu Katika Mzunguko

Sampuli ya MCP imeundwa kwa kuzingatia usimamizi wa binadamu:

- **Kwa maelekezo**:
  - Wateja wanapaswa kuonyesha watumiaji maelekezo yaliyopendekezwa
  - Watumiaji wanapaswa kuwa na uwezo wa kubadilisha au kukataa maelekezo
  - Maelekezo ya mfumo yanaweza kuchujwa au kubadilishwa
  - Ujumuishaji wa muktadha unadhibitiwa na mteja

- **Kwa ukamilishaji**:
  - Wateja wanapaswa kuonyesha watumiaji ukamilishaji
  - Watumiaji wanapaswa kuwa na uwezo wa kubadilisha au kukataa ukamilishaji
  - Wateja wanaweza kuchuja au kubadilisha ukamilishaji
  - Watumiaji wanadhibiti ni mfano gani unatumika

Kwa misingi hii, tuchunguze jinsi ya kutekeleza sampuli katika lugha mbalimbali za programu, tukizingatia vigezo vinavyoungwa mkono kwa kawaida na watoa huduma wa LLM.

## Mambo ya Usalama Kuzingatia

Unapotekeleza sampuli katika MCP, zingatia mbinu bora za usalama zifuatazo:

- **Thibitisha maudhui yote ya ujumbe** kabla ya kuutuma kwa mteja
- **Safisha taarifa nyeti** kutoka kwa maelekezo na ukamilishaji
- **Tekeleza mipaka ya kiwango** ili kuzuia matumizi mabaya
- **Fuatilia matumizi ya sampuli** kwa mifumo isiyo ya kawaida
- **Fichua data wakati wa usafirishaji** kwa kutumia itifaki salama
- **Dhibiti faragha ya data za watumiaji** kulingana na kanuni husika
- **Fanya ukaguzi wa maombi ya sampuli** kwa ufuatiliaji na usalama
- **Dhibiti matumizi ya gharama** kwa mipaka inayofaa
- **Tekeleza muda wa kusubiri** kwa maombi ya sampuli
- **Shughulikia makosa ya mfano kwa upole** kwa mbadala zinazofaa

Vigezo vya sampuli huruhusu kurekebisha tabia za mifano ya lugha ili kufikia usawa unaotakiwa kati ya matokeo ya uhakika na ubunifu.

Tuchunguze jinsi ya kusanidi vigezo hivi katika lugha mbalimbali za programu.

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

Katika msimbo uliotangulia tumefanya:

- Kuunda mteja wa MCP na URL maalum ya seva.
- Kusanidi ombi na vigezo vya sampuli kama `temperature`, `top_p`, na `top_k`.
- Kutuma ombi na kuchapisha maandishi yaliyotengenezwa.
- Kutumia:
    - `allowedTools` kubainisha zana gani mfano anaweza kutumia wakati wa uzalishaji. Katika kesi hii, tuliruhusu zana za `ideaGenerator` na `marketAnalyzer` kusaidia kuzalisha mawazo ya ubunifu ya programu.
    - `frequencyPenalty` na `presencePenalty` kudhibiti kurudia na utofauti katika matokeo.
    - `temperature` kudhibiti nasibu ya matokeo, ambapo thamani kubwa huleta majibu yenye ubunifu zaidi.
    - `top_p` kupunguza uchaguzi wa tokeni kwa zile zinazochangia uwezekano wa juu wa jumla, kuboresha ubora wa maandishi yaliyotengenezwa.
    - `top_k` kuzuia mfano kutumia tokeni K bora zaidi, ambayo inaweza kusaidia kuzalisha majibu yenye muendelezo mzuri.
    - `frequencyPenalty` na `presencePenalty` kupunguza kurudia na kuhimiza utofauti katika maandishi yaliyotengenezwa.

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

Katika msimbo uliotangulia tumefanya:

- Kuanza mteja wa MCP na URL ya seva na API key.
- Kusanidi seti mbili za vigezo vya sampuli: moja kwa kazi za ubunifu na nyingine kwa kazi za ukweli.
- Kutuma maombi na usanidi huu, kuruhusu mfano kutumia zana maalum kwa kila kazi.
- Kuchapisha majibu yaliyotengenezwa kuonyesha athari za vigezo tofauti vya sampuli.
- Kutumia `allowedTools` kubainisha zana gani mfano anaweza kutumia wakati wa uzalishaji. Katika kesi hii, tuliruhusu `ideaGenerator` na `environmentalImpactTool` kwa kazi za ubunifu, na `factChecker` na `dataAnalysisTool` kwa kazi za ukweli.
- Kutumia `temperature` kudhibiti nasibu ya matokeo, ambapo thamani kubwa huleta majibu yenye ubunifu zaidi.
- Kutumia `top_p` kupunguza uchaguzi wa tokeni kwa zile zinazochangia uwezekano wa juu wa jumla, kuboresha ubora wa maandishi yaliyotengenezwa.
- Kutumia `frequencyPenalty` na `presencePenalty` kupunguza kurudia na kuhimiza utofauti katika matokeo.
- Kutumia `top_k` kuzuia mfano kutumia tokeni K bora zaidi, ambayo inaweza kusaidia kuzalisha majibu yenye muendelezo mzuri.

---

## Sampuli ya Uhakika

Kwa programu zinazohitaji matokeo thabiti, sampuli ya uhakika huhakikisha matokeo yanayoweza kurudiwa. Inavyofanya hivyo ni kwa kutumia mbegu ya nasibu iliyowekwa na kuweka joto (`temperature`) kuwa sifuri.

Tuchunguze mfano wa utekelezaji hapa chini kuonyesha sampuli ya uhakika katika lugha mbalimbali za programu.

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

Katika msimbo uliotangulia tumefanya:

- Kuunda mteja wa MCP na URL maalum ya seva.
- Kusanidi maombi mawili na maelekezo sawa, mbegu thabiti, na joto sifuri.
- Kutuma maombi yote na kuchapisha maandishi yaliyotengenezwa.
- Kuonyesha kuwa majibu ni sawa kutokana na asili ya uhakika ya usanidi wa sampuli (mbegu na joto sawa).
- Kutumia `setSeed` kubainisha mbegu thabiti ya nasibu, kuhakikisha mfano unazalisha matokeo sawa kwa ingizo sawa kila wakati.
- Kuweka `temperature` kuwa sifuri kuhakikisha uhakika wa juu, maana mfano daima huchagua tokeni inayowezekana zaidi bila nasibu.

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

Katika msimbo uliotangulia tumefanya:

- Kuanza mteja wa MCP na URL ya seva.
- Kusanidi maombi mawili na maelekezo sawa, mbegu thabiti, na joto sifuri.
- Kutuma maombi yote na kuchapisha maandishi yaliyotengenezwa.
- Kuonyesha kuwa majibu ni sawa kutokana na asili ya uhakika ya usanidi wa sampuli (mbegu na joto sawa).
- Kutumia `seed` kubainisha mbegu thabiti ya nasibu, kuhakikisha mfano unazalisha matokeo sawa kwa ingizo sawa kila wakati.
- Kuweka `temperature` kuwa sifuri kuhakikisha uhakika wa juu, maana mfano daima huchagua tokeni inayowezekana zaidi bila nasibu.
- Kutumia mbegu tofauti kwa ombi la tatu kuonyesha kuwa kubadilisha mbegu huleta matokeo tofauti, hata kwa maelekezo na joto sawa.

---

## Usanidi wa Sampuli unaobadilika

Sampuli ya akili hubadilisha vigezo kulingana na muktadha na mahitaji ya kila ombi. Hii inamaanisha kurekebisha vigezo kama joto, top_p, na adhabu kulingana na aina ya kazi, mapendeleo ya mtumiaji, au utendaji wa kihistoria.

Tuchunguze jinsi ya kutekeleza sampuli inayobadilika katika lugha mbalimbali za programu.

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

Katika msimbo uliotangulia tumefanya:

- Kuunda darasa la `DynamicSamplingService` linalosimamia sampuli inayobadilika.
- Kueleza mipangilio ya sampuli kwa aina tofauti za kazi (ubunifu, ukweli, msimbo, uchambuzi).
- Kuchagua mpangilio wa msingi wa sampuli kulingana na aina ya kazi.
- Kurekebisha vigezo vya sampuli kulingana na mapendeleo ya mtumiaji, kama kiwango cha ubunifu na utofauti.
- Kutuma ombi na vigezo vya sampuli vilivyosanidiwa kwa nguvu.
- Kurudisha maandishi yaliyotengenezwa pamoja na vigezo vya sampuli vilivyotumika na aina ya kazi kwa uwazi.
- Kutumia `temperature` kudhibiti nasibu ya matokeo, ambapo thamani kubwa huleta majibu yenye ubunifu zaidi.
- Kutumia `top_p` kupunguza uchaguzi wa tokeni kwa zile zinazochangia uwezekano wa juu wa jumla, kuboresha ubora wa maandishi yaliyotengenezwa.
- Kutumia `frequency_penalty` kupunguza kurudia na kuhimiza utofauti katika matokeo.
- Kutumia `user_preferences` kuruhusu ubinafsishaji wa vigezo vya sampuli kulingana na viwango vya ubunifu na utofauti vilivyoainishwa na mtumiaji.
- Kutumia `task_type` kubaini mkakati unaofaa wa sampuli kwa ombi, kuruhusu majibu yaliyobinafsishwa zaidi kulingana na asili ya kazi.
- Kutumia njia ya `send_request` kutuma maelekezo na vigezo vya sampuli vilivyosanidiwa, kuhakikisha mfano unazalisha maandishi kulingana na mahitaji yaliyobainishwa.
- Kutumia `generated_text` kupata jibu la mfano, ambalo hurudishwa pamoja na vigezo vya sampuli na aina ya kazi kwa uchambuzi au onyesho zaidi.
- Kutumia `min` na `max` kuhakikisha mapendeleo ya mtumiaji yamefungwa ndani ya mipaka halali, kuzuia usanidi usio sahihi wa sampuli.

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

Katika msimbo uliotangulia tumefanya:

- Kuunda darasa la `AdaptiveSamplingManager` linalosimamia sampuli inayobadilika kulingana na aina ya kazi na mapendeleo ya mtumiaji.
- Kueleza wasifu wa sampuli kwa aina tofauti za kazi (ubunifu, ukweli, msimbo, mazungumzo).
- Kutekeleza njia ya kugundua aina ya kazi kutoka kwa maelekezo kwa kutumia mbinu rahisi.
- Kukokotoa vigezo vya sampuli kulingana na aina ya kazi iliyogunduliwa na mapendeleo ya mtumiaji.
- Kutumia marekebisho yaliyojifunza kulingana na utendaji wa kihistoria kuboresha vigezo vya sampuli.
- Kurekodi utendaji kwa marekebisho ya baadaye, kuruhusu mfumo kujifunza kutokana na mwingiliano wa zamani.
- Kutuma maombi na vigezo vya sampuli vilivyosanidiwa kwa nguvu na kurudisha maandishi yaliyotengenezwa pamoja na vigezo vilivyotumika na aina ya kazi iliyogunduliwa.
- Kutumia:
    - `userPreferences` kuruhusu ubinafsishaji wa vigezo vya sampuli kulingana na viwango vya ubunifu, usahihi, na uthabiti vilivyoainishwa na mtumiaji.
    - `detectTaskType` kubaini asili ya kazi kulingana na maelekezo, kuruhusu majibu yaliyobinafsishwa zaidi.
    - `recordPerformance` kurekodi utendaji wa majibu yaliyotengenezwa, kuwezesha mfumo kubadilika na kuboresha kwa muda.
    - `applyLearnedAdjustments` kurekebisha vigezo vya sampuli kulingana na utendaji wa kihistoria, kuboresha uwezo wa mfano kuzalisha majibu ya ubora wa juu.
    - `generateResponse` kufunika mchakato mzima wa kuzalisha jibu kwa sampuli inayobadilika, kurahisisha kuitwa kwa maelekezo na muktadha tofauti.
    - `allowedTools` kubainisha zana gani mfano anaweza kutumia wakati wa uzalishaji, kuruhusu majibu yenye ufahamu zaidi wa muktadha.
    - `feedbackScore` kuruhusu watumiaji kutoa maoni juu ya ubora wa jibu lililotengenezwa, ambalo linaweza kutumika kuboresha utendaji wa mfano kwa muda.
    - `performanceHistory` kudumisha rekodi ya mwingiliano ya zamani, kuwezesha mfumo kujifunza kutokana na mafanikio na makosa ya zamani.
    - `getSamplingParameters` kurekebisha vigezo vya sampuli kwa nguvu kulingana na muktadha wa ombi, kuruhusu tabia ya mfano kuwa rahisi na ya haraka kujibu.
    - `detectTaskType` kuainisha kazi kulingana na maelekezo, kuwezesha mfumo kutumia mikakati inayofaa ya sampuli kwa aina tofauti za maombi.
    - `samplingProfiles` kufafanua usanidi wa msingi wa sampuli kwa aina tofauti za kazi, kuruhusu marekebisho ya haraka kulingana na asili ya ombi.

---

## Nini Kifuatacho

- [5.7 Kupanua](../mcp-scaling/README.md)

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.