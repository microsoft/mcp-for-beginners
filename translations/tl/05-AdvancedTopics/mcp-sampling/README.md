# Sampling sa Model Context Protocol

Ang sampling ay isang makapangyarihang tampok ng MCP na nagpapahintulot sa mga server na humiling ng LLM completions sa pamamagitan ng client, na nagbibigay-daan sa mas sopistikadong mga agentic na kilos habang pinananatili ang seguridad at privacy. Ang tamang sampling configuration ay maaaring malaki ang maitutulong sa pagpapabuti ng kalidad at performance ng tugon. Nagbibigay ang MCP ng isang standardized na paraan upang kontrolin kung paano bumubuo ng teksto ang mga modelo gamit ang mga partikular na parameter na nakakaapekto sa randomness, creativity, at coherence.

## Panimula

Sa araling ito, tatalakayin natin kung paano i-configure ang mga sampling parameter sa mga MCP request at unawain ang mga mekanismo ng protocol sa likod ng sampling.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Maunawaan ang mga pangunahing sampling parameter na available sa MCP.
- I-configure ang mga sampling parameter para sa iba't ibang gamit.
- Magpatupad ng deterministic sampling para sa mga resulta na maaaring ulitin.
- Dynamic na i-adjust ang mga sampling parameter base sa konteksto at kagustuhan ng user.
- I-apply ang mga sampling strategy upang mapabuti ang performance ng modelo sa iba't ibang sitwasyon.
- Maunawaan kung paano gumagana ang sampling sa daloy ng client-server ng MCP.

## Paano Gumagana ang Sampling sa MCP

Ang daloy ng sampling sa MCP ay sumusunod sa mga hakbang na ito:

1. Nagpapadala ang server ng `sampling/createMessage` na request sa client  
2. Sinusuri ng client ang request at maaaring baguhin ito  
3. Nagsasagawa ang client ng sampling mula sa isang LLM  
4. Sinusuri ng client ang completion  
5. Ibinabalik ng client ang resulta sa server  

Ang disenyo na may human-in-the-loop ay nagsisiguro na may kontrol ang mga user sa kung ano ang nakikita at nililikha ng LLM.

## Pangkalahatang-ideya ng Mga Sampling Parameter

Itinakda ng MCP ang mga sumusunod na sampling parameter na maaaring i-configure sa mga client request:

| Parameter | Paglalarawan | Karaniwang Saklaw |
|-----------|--------------|-------------------|
| `temperature` | Kinokontrol ang randomness sa pagpili ng token | 0.0 - 1.0 |
| `maxTokens` | Pinakamataas na bilang ng token na bubuuin | Integer na halaga |
| `stopSequences` | Mga custom na sequence na humihinto sa pagbuo kapag na-encounter | Array ng mga string |
| `metadata` | Karagdagang provider-specific na mga parameter | JSON object |

Maraming LLM provider ang sumusuporta sa karagdagang mga parameter sa pamamagitan ng `metadata` field, na maaaring kabilang ang:

| Karaniwang Extension Parameter | Paglalarawan | Karaniwang Saklaw |
|-------------------------------|--------------|-------------------|
| `top_p` | Nucleus sampling - nililimitahan ang mga token sa top cumulative probability | 0.0 - 1.0 |
| `top_k` | Nililimitahan ang pagpili ng token sa top K na opsyon | 1 - 100 |
| `presence_penalty` | Pinaparusahan ang mga token base sa kanilang presensya sa teksto hanggang ngayon | -2.0 - 2.0 |
| `frequency_penalty` | Pinaparusahan ang mga token base sa kanilang dalas sa teksto hanggang ngayon | -2.0 - 2.0 |
| `seed` | Tiyak na random seed para sa reproducible na resulta | Integer na halaga |

## Halimbawa ng Format ng Request

Narito ang isang halimbawa ng paghingi ng sampling mula sa client sa MCP:

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

## Mga Kontrol ng Human in the Loop

Dinisenyo ang MCP sampling na may pagsasaalang-alang sa human oversight:

- **Para sa mga prompt**:
  - Dapat ipakita ng client sa user ang iminungkahing prompt  
  - Dapat may kakayahan ang user na baguhin o tanggihan ang mga prompt  
  - Maaaring i-filter o baguhin ang mga system prompt  
  - Ang pagsasama ng konteksto ay kontrolado ng client  

- **Para sa mga completion**:
  - Dapat ipakita ng client sa user ang completion  
  - Dapat may kakayahan ang user na baguhin o tanggihan ang mga completion  
  - Maaaring i-filter o baguhin ng client ang mga completion  
  - Kontrolado ng user kung aling modelo ang gagamitin  

Sa mga prinsipyong ito, tingnan natin kung paano ipatupad ang sampling sa iba't ibang programming language, na nakatuon sa mga parameter na karaniwang sinusuportahan ng mga LLM provider.

## Mga Pagsasaalang-alang sa Seguridad

Kapag nagpapatupad ng sampling sa MCP, isaalang-alang ang mga sumusunod na best practice sa seguridad:

- **I-validate ang lahat ng nilalaman ng mensahe** bago ito ipadala sa client  
- **Linisin ang sensitibong impormasyon** mula sa mga prompt at completion  
- **Magpatupad ng rate limits** upang maiwasan ang pang-aabuso  
- **I-monitor ang paggamit ng sampling** para sa mga kakaibang pattern  
- **I-encrypt ang data habang ipinapadala** gamit ang secure na mga protocol  
- **Pangasiwaan ang privacy ng user data** ayon sa mga kaukulang regulasyon  
- **I-audit ang mga sampling request** para sa pagsunod at seguridad  
- **Kontrolin ang exposure sa gastos** gamit ang angkop na limitasyon  
- **Magpatupad ng timeout** para sa mga sampling request  
- **Harapin nang maayos ang mga error ng modelo** gamit ang angkop na fallback  

Pinapayagan ng mga sampling parameter ang masusing pag-aayos ng kilos ng mga language model upang makamit ang nais na balanse sa pagitan ng deterministic at creative na output.

Tingnan natin kung paano i-configure ang mga parameter na ito sa iba't ibang programming language.

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

Sa naunang code ay:

- Nilikha ang isang MCP client gamit ang isang partikular na server URL.  
- In-configure ang request gamit ang mga sampling parameter tulad ng `temperature`, `top_p`, at `top_k`.  
- Ipinadala ang request at ipinrint ang nabuo na teksto.  
- Ginamit ang:  
    - `allowedTools` upang tukuyin kung aling mga tool ang maaaring gamitin ng modelo habang bumubuo. Sa kasong ito, pinayagan namin ang `ideaGenerator` at `marketAnalyzer` na mga tool upang tumulong sa pagbuo ng mga malikhaing ideya para sa app.  
    - `frequencyPenalty` at `presencePenalty` upang kontrolin ang pag-uulit at pagkakaiba-iba sa output.  
    - `temperature` upang kontrolin ang randomness ng output, kung saan ang mas mataas na halaga ay nagreresulta sa mas malikhaing tugon.  
    - `top_p` upang limitahan ang pagpili ng mga token sa mga nag-aambag sa top cumulative probability mass, na nagpapabuti sa kalidad ng nabuo na teksto.  
    - `top_k` upang limitahan ang modelo sa top K na pinaka-malamang na mga token, na makakatulong sa pagbuo ng mas coherent na mga tugon.  
    - `frequencyPenalty` at `presencePenalty` upang mabawasan ang pag-uulit at hikayatin ang pagkakaiba-iba sa nabuo na teksto.

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

Sa naunang code ay:

- In-initialize ang MCP client gamit ang server URL at API key.  
- In-configure ang dalawang set ng sampling parameter: isa para sa mga malikhaing gawain at isa para sa mga factual na gawain.  
- Nagpadala ng mga request gamit ang mga configuration na ito, pinapayagan ang modelo na gumamit ng partikular na mga tool para sa bawat gawain.  
- Ipinrint ang mga nabuo na tugon upang ipakita ang epekto ng iba't ibang sampling parameter.  
- Ginamit ang `allowedTools` upang tukuyin kung aling mga tool ang maaaring gamitin ng modelo habang bumubuo. Sa kasong ito, pinayagan namin ang `ideaGenerator` at `environmentalImpactTool` para sa mga malikhaing gawain, at `factChecker` at `dataAnalysisTool` para sa mga factual na gawain.  
- Ginamit ang `temperature` upang kontrolin ang randomness ng output, kung saan ang mas mataas na halaga ay nagreresulta sa mas malikhaing tugon.  
- Ginamit ang `top_p` upang limitahan ang pagpili ng mga token sa mga nag-aambag sa top cumulative probability mass, na nagpapabuti sa kalidad ng nabuo na teksto.  
- Ginamit ang `frequencyPenalty` at `presencePenalty` upang mabawasan ang pag-uulit at hikayatin ang pagkakaiba-iba sa output.  
- Ginamit ang `top_k` upang limitahan ang modelo sa top K na pinaka-malamang na mga token, na makakatulong sa pagbuo ng mas coherent na mga tugon.

---

## Deterministic Sampling

Para sa mga aplikasyon na nangangailangan ng pare-parehong output, tinitiyak ng deterministic sampling ang mga resulta na maaaring ulitin. Ginagawa ito sa pamamagitan ng paggamit ng fixed random seed at pagtatakda ng temperature sa zero.

Tingnan natin ang sumusunod na halimbawa ng implementasyon upang ipakita ang deterministic sampling sa iba't ibang programming language.

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

Sa naunang code ay:

- Nilikha ang isang MCP client gamit ang tinukoy na server URL.  
- In-configure ang dalawang request gamit ang parehong prompt, fixed seed, at zero temperature.  
- Ipinadala ang parehong request at ipinrint ang nabuo na teksto.  
- Ipinakita na magkapareho ang mga tugon dahil sa deterministic na katangian ng sampling configuration (parehong seed at temperature).  
- Ginamit ang `setSeed` upang tukuyin ang fixed random seed, na nagsisiguro na ang modelo ay lilikha ng parehong output para sa parehong input sa bawat pagkakataon.  
- Itinakda ang `temperature` sa zero upang matiyak ang maximum na determinismo, ibig sabihin, palaging pipiliin ng modelo ang pinaka-malamang na susunod na token nang walang randomness.

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

Sa naunang code ay:

- In-initialize ang MCP client gamit ang server URL.  
- In-configure ang dalawang request gamit ang parehong prompt, fixed seed, at zero temperature.  
- Ipinadala ang parehong request at ipinrint ang nabuo na teksto.  
- Ipinakita na magkapareho ang mga tugon dahil sa deterministic na katangian ng sampling configuration (parehong seed at temperature).  
- Ginamit ang `seed` upang tukuyin ang fixed random seed, na nagsisiguro na ang modelo ay lilikha ng parehong output para sa parehong input sa bawat pagkakataon.  
- Itinakda ang `temperature` sa zero upang matiyak ang maximum na determinismo, ibig sabihin, palaging pipiliin ng modelo ang pinaka-malamang na susunod na token nang walang randomness.  
- Gumamit ng ibang seed para sa ikatlong request upang ipakita na ang pagbabago ng seed ay nagreresulta sa ibang output, kahit na pareho ang prompt at temperature.

---

## Dynamic Sampling Configuration

Ang intelligent sampling ay inaangkop ang mga parameter base sa konteksto at pangangailangan ng bawat request. Ibig sabihin nito ay dynamic na ina-adjust ang mga parameter tulad ng temperature, top_p, at penalties base sa uri ng gawain, kagustuhan ng user, o nakaraang performance.

Tingnan natin kung paano ipatupad ang dynamic sampling sa iba't ibang programming language.

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

Sa naunang code ay:

- Nilikha ang `DynamicSamplingService` class na namamahala sa adaptive sampling.  
- Tinukoy ang mga sampling preset para sa iba't ibang uri ng gawain (creative, factual, code, analytical).  
- Pinili ang base sampling preset base sa uri ng gawain.  
- In-adjust ang mga sampling parameter base sa kagustuhan ng user, tulad ng antas ng creativity at diversity.  
- Ipinadala ang request gamit ang dynamic na na-configure na sampling parameter.  
- Ibinalik ang nabuo na teksto kasama ang mga ginamit na sampling parameter at uri ng gawain para sa transparency.  
- Ginamit ang `temperature` upang kontrolin ang randomness ng output, kung saan ang mas mataas na halaga ay nagreresulta sa mas malikhaing tugon.  
- Ginamit ang `top_p` upang limitahan ang pagpili ng mga token sa mga nag-aambag sa top cumulative probability mass, na nagpapabuti sa kalidad ng nabuo na teksto.  
- Ginamit ang `frequency_penalty` upang mabawasan ang pag-uulit at hikayatin ang pagkakaiba-iba sa output.  
- Ginamit ang `user_preferences` upang payagan ang custom na pagsasaayos ng sampling parameter base sa antas ng creativity at diversity na itinakda ng user.  
- Ginamit ang `task_type` upang tukuyin ang angkop na sampling strategy para sa request, na nagbibigay-daan sa mas angkop na tugon base sa kalikasan ng gawain.  
- Ginamit ang `send_request` method upang ipadala ang prompt kasama ang na-configure na sampling parameter, na nagsisiguro na ang modelo ay bumubuo ng teksto ayon sa tinukoy na mga pangangailangan.  
- Ginamit ang `generated_text` upang kunin ang tugon ng modelo, na ibinabalik kasama ang sampling parameter at uri ng gawain para sa karagdagang pagsusuri o pagpapakita.  
- Ginamit ang `min` at `max` functions upang matiyak na ang mga kagustuhan ng user ay nasa loob ng wastong saklaw, na pumipigil sa mga invalid na sampling configuration.

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

Sa naunang code ay:

- Nilikha ang `AdaptiveSamplingManager` class na namamahala sa dynamic sampling base sa uri ng gawain at kagustuhan ng user.  
- Tinukoy ang mga sampling profile para sa iba't ibang uri ng gawain (creative, factual, code, conversational).  
- Nagpatupad ng method upang tuklasin ang uri ng gawain mula sa prompt gamit ang simpleng heuristics.  
- Kinuwenta ang mga sampling parameter base sa natukoy na uri ng gawain at kagustuhan ng user.  
- Inapply ang mga natutunang adjustment base sa nakaraang performance upang i-optimize ang mga sampling parameter.  
- Nirekord ang performance para sa mga susunod na adjustment, na nagpapahintulot sa sistema na matuto mula sa mga nakaraang interaksyon.  
- Nagpadala ng mga request gamit ang dynamic na na-configure na sampling parameter at ibinalik ang nabuo na teksto kasama ang mga ginamit na parameter at natukoy na uri ng gawain.  
- Ginamit ang:  
    - `userPreferences` upang payagan ang custom na pagsasaayos ng sampling parameter base sa antas ng creativity, precision, at consistency na itinakda ng user.  
    - `detectTaskType` upang tukuyin ang kalikasan ng gawain base sa prompt, na nagbibigay-daan sa mas angkop na tugon.  
    - `recordPerformance` upang i-log ang performance ng mga nabuo na tugon, na nagpapahintulot sa sistema na mag-adapt at mag-improve sa paglipas ng panahon.  
    - `applyLearnedAdjustments` upang baguhin ang mga sampling parameter base sa nakaraang performance, na nagpapahusay sa kakayahan ng modelo na bumuo ng mataas na kalidad na tugon.  
    - `generateResponse` upang ipaloob ang buong proseso ng pagbuo ng tugon gamit ang adaptive sampling, na nagpapadali sa pagtawag gamit ang iba't ibang prompt at konteksto.  
    - `allowedTools` upang tukuyin kung aling mga tool ang maaaring gamitin ng modelo habang bumubuo, na nagbibigay-daan sa mas kontekstuwal na tugon.  
    - `feedbackScore` upang payagan ang mga user na magbigay ng feedback sa kalidad ng nabuo na tugon, na maaaring gamitin upang lalo pang pagbutihin ang performance ng modelo sa paglipas ng panahon.  
    - `performanceHistory` upang panatilihin ang talaan ng mga nakaraang interaksyon, na nagpapahintulot sa sistema na matuto mula sa mga nagdaang tagumpay at pagkabigo.  
    - `getSamplingParameters` upang dynamic na i-adjust ang mga sampling parameter base sa konteksto ng request, na nagbibigay-daan sa mas flexible at responsive na kilos ng modelo.  
    - `detectTaskType` upang i-klasipika ang gawain base sa prompt, na nagpapahintulot sa sistema na mag-apply ng angkop na sampling strategy para sa iba't ibang uri ng request.  
    - `samplingProfiles` upang tukuyin ang base sampling configuration para sa iba't ibang uri ng gawain, na nagpapadali sa mabilisang adjustment base sa kalikasan ng request.

---

## Ano ang Susunod

- [5.7 Scaling](../mcp-scaling/README.md)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.