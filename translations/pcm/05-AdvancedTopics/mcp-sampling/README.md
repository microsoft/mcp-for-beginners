# Sampling for Model Context Protocol

Sampling na one strong MCP feature wey go allow server dem request LLM completions through di client. E fit help do beta agent behavior while e still dey keep security and privacy. If you set sampling well, e fit make response quality and performance beta well well. MCP don give one standard way to control how model go dey generate text with di parameters wey go affect randomness, creativity, and coherence.

## Introduction

For dis lesson, we go learn how to set sampling parameters for MCP requests and understand di protocol mechanics wey dey behind sampling.

## Wetin You Go Learn

By di end of dis lesson, you go fit:

- Sabi di main sampling parameters wey dey MCP.
- Set sampling parameters for different kind use cases.
- Do deterministic sampling to get results wey you fit repeat.
- Adjust sampling parameters based on context and wetin user like.
- Use sampling strategies to make model performance beta for different situations.
- Understand how sampling dey work for di client-server flow of MCP.

## How Sampling Dey Work for MCP

Di sampling flow for MCP dey follow dis steps:

1. Server go send `sampling/createMessage` request go meet di client.
2. Client go check di request and fit change am.
3. Client go sample from one LLM.
4. Client go check di completion.
5. Client go return di result go meet di server.

Dis human-in-the-loop design dey make sure say users dey control wetin di LLM dey see and wetin e dey generate.

## Sampling Parameters Overview

MCP get di following sampling parameters wey you fit set for client requests:

| Parameter | Wetin E Mean | Typical Range |
|-----------|-------------|---------------|
| `temperature` | E dey control randomness for token selection | 0.0 - 1.0 |
| `maxTokens` | Di maximum number of tokens wey e go generate | Integer value |
| `stopSequences` | Custom sequences wey go stop generation if e see am | Array of strings |
| `metadata` | Extra provider-specific parameters | JSON object |

Plenty LLM providers dey support extra parameters through di `metadata` field, like:

| Common Extension Parameter | Wetin E Mean | Typical Range |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - e dey limit tokens to di top cumulative probability | 0.0 - 1.0 |
| `top_k` | E dey limit token selection to di top K options | 1 - 100 |
| `presence_penalty` | E dey penalize tokens based on how dem don show for di text before | -2.0 - 2.0 |
| `frequency_penalty` | E dey penalize tokens based on how many times dem don show for di text before | -2.0 - 2.0 |
| `seed` | Specific random seed to get results wey you fit repeat | Integer value |

## Example Request Format

See example of how to request sampling from client for MCP:

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

## Response Format

Di client go return di completion result:

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

## Human in the Loop Controls

MCP sampling dey designed make human dey oversee am:

- **For prompts**:
  - Clients suppose show users di proposed prompt.
  - Users suppose fit change or reject prompts.
  - System prompts fit dey filtered or changed.
  - Context inclusion dey controlled by di client.

- **For completions**:
  - Clients suppose show users di completion.
  - Users suppose fit change or reject completions.
  - Clients fit filter or change completions.
  - Users dey control which model dem go use.

With dis principles, make we see how to implement sampling for different programming languages, focusing on di parameters wey plenty LLM providers dey support.

## Security Considerations

When you dey implement sampling for MCP, make you consider dis security best practices:

- **Check all message content** before you send am go meet di client.
- **Remove sensitive information** from prompts and completions.
- **Set rate limits** to stop abuse.
- **Monitor sampling usage** for any strange pattern.
- **Encrypt data wey dey move** with secure protocols.
- **Handle user data privacy** based on di law wey dey your area.
- **Audit sampling requests** to make sure say e dey secure and follow rules.
- **Control cost exposure** with correct limits.
- **Set timeouts** for sampling requests.
- **Handle model errors well** with correct fallback plans.

Sampling parameters dey allow you fine-tune how language models go behave to balance deterministic and creative outputs.

Make we see how to set dis parameters for different programming languages.

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

For di code wey dey above, we don:

- Create MCP client with specific server URL.
- Set request with sampling parameters like `temperature`, `top_p`, and `top_k`.
- Send di request and print di generated text.
- Use:
    - `allowedTools` to specify di tools wey di model fit use during generation. For dis case, we allow `ideaGenerator` and `marketAnalyzer` tools to help generate creative app ideas.
    - `frequencyPenalty` and `presencePenalty` to control repetition and diversity for di output.
    - `temperature` to control randomness of di output, higher values dey give more creative responses.
    - `top_p` to limit token selection to di top cumulative probability mass, to make di generated text beta.
    - `top_k` to restrict di model to di top K most probable tokens, to help generate more coherent responses.
    - `frequencyPenalty` and `presencePenalty` to reduce repetition and encourage diversity for di generated text.

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

For di code wey dey above, we don:

- Initialize MCP client with server URL and API key.
- Set two sets of sampling parameters: one for creative tasks and another for factual tasks.
- Send requests with dis configurations, allow di model use specific tools for each task.
- Print di generated responses to show di effects of different sampling parameters.
- Use `allowedTools` to specify di tools wey di model fit use during generation. For dis case, we allow `ideaGenerator` and `environmentalImpactTool` for creative tasks, and `factChecker` and `dataAnalysisTool` for factual tasks.
- Use `temperature` to control randomness of di output, higher values dey give more creative responses.
- Use `top_p` to limit token selection to di top cumulative probability mass, to make di generated text beta.
- Use `frequencyPenalty` and `presencePenalty` to reduce repetition and encourage diversity for di output.
- Use `top_k` to restrict di model to di top K most probable tokens, to help generate more coherent responses.

---

## Deterministic Sampling

For applications wey need consistent outputs, deterministic sampling dey make sure say results go dey repeatable. E dey do am by using fixed random seed and setting temperature to zero.

Make we see example implementation to show deterministic sampling for different programming languages.

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

For di code wey dey above, we don:

- Create MCP client with specified server URL.
- Set two requests with di same prompt, fixed seed, and zero temperature.
- Send di two requests and print di generated text.
- Show say di responses dey identical because of di deterministic nature of di sampling configuration (same seed and temperature).
- Use `setSeed` to specify fixed random seed, to make sure say di model go generate di same output for di same input every time.
- Set `temperature` to zero to make sure say e dey deterministic, meaning di model go always select di most probable next token without randomness.

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

For di code wey dey above, we don:

- Initialize MCP client with server URL.
- Set two requests with di same prompt, fixed seed, and zero temperature.
- Send di two requests and print di generated text.
- Show say di responses dey identical because of di deterministic nature of di sampling configuration (same seed and temperature).
- Use `seed` to specify fixed random seed, to make sure say di model go generate di same output for di same input every time.
- Set `temperature` to zero to make sure say e dey deterministic, meaning di model go always select di most probable next token without randomness.
- Use different seed for di third request to show say if you change di seed, e go give different outputs, even if di prompt and temperature dey di same.

---

## Dynamic Sampling Configuration

Smart sampling dey adjust parameters based on di context and wetin di request need. E mean say e dey adjust parameters like temperature, top_p, and penalties based on di task type, wetin user like, or past performance.

Make we see how to implement dynamic sampling for different programming languages.

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

For di code wey dey above, we don:

- Create `DynamicSamplingService` class wey dey manage adaptive sampling.
- Define sampling presets for different task types (creative, factual, code, analytical).
- Select base sampling preset based on di task type.
- Adjust di sampling parameters based on wetin user like, like creativity level and diversity.
- Send di request with di dynamically configured sampling parameters.
- Return di generated text with di applied sampling parameters and task type for transparency.
- Use `temperature` to control randomness of di output, higher values dey give more creative responses.
- Use `top_p` to limit token selection to di top cumulative probability mass, to make di generated text beta.
- Use `frequency_penalty` to reduce repetition and encourage diversity for di output.
- Use `user_preferences` to allow customization of di sampling parameters based on wetin user like for creativity and diversity levels.
- Use `task_type` to determine di correct sampling strategy for di request, to make di response fit di task well.
- Use `send_request` method to send di prompt with di configured sampling parameters, to make sure say di model go generate text based on wetin you want.
- Use `generated_text` to get di model response, wey dem go return with di sampling parameters and task type for further analysis or display.
- Use `min` and `max` functions to make sure say wetin user like dey valid range, to stop invalid sampling configurations.

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

For di code wey dey above, we don:

- Create `AdaptiveSamplingManager` class wey dey manage dynamic sampling based on task type and wetin user like.
- Define sampling profiles for different task types (creative, factual, code, conversational).
- Implement method to detect di task type from di prompt using simple heuristics.
- Calculate sampling parameters based on di detected task type and wetin user like.
- Apply learned adjustments based on past performance to optimize sampling parameters.
- Record performance for future adjustments, to make di system dey learn from past interactions.
- Send requests with dynamically configured sampling parameters and return di generated text with applied parameters and detected task type.
- Use:
    - `userPreferences` to allow customization of di sampling parameters based on wetin user like for creativity, precision, and consistency levels.
    - `detectTaskType` to determine di nature of di task based on di prompt, to make di response fit di task well.
    - `recordPerformance` to log di performance of generated responses, to make di system dey adapt and improve over time.
    - `applyLearnedAdjustments` to change sampling parameters based on past performance, to make di model dey generate better responses.
    - `generateResponse` to handle di whole process of generating response with adaptive sampling, to make am easy to call with different prompts and contexts.
    - `allowedTools` to specify di tools wey di model fit use during generation, to make di response dey more context-aware.
    - `feedbackScore` to allow users give feedback on di quality of di generated response, wey fit help refine di model performance over time.
    - `performanceHistory` to keep record of past interactions, to make di system dey learn from wetin e don do before.
    - `getSamplingParameters` to adjust sampling parameters based on di request context, to make di model behavior dey flexible and responsive.
    - `detectTaskType` to classify di task based on di prompt, to make di system apply correct sampling strategies for different requests.
    - `samplingProfiles` to define base sampling configurations for different task types, to make quick adjustments based on di request nature.

---

## Wetin Next

- [5.7 Scaling](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am correct, abeg make you sabi say transleshion wey machine do fit get mistake or no dey accurate well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->