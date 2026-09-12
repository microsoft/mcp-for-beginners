> [!WARNING]
> Sampling don old for MCP `2026-07-28`. Dis lesson na to still keep for
> old way dem dey do am. New servers suppose connect straight to one LLM
> provider API.

# Sampling for Model Context Protocol

> Sampling still dey for `2026-07-28` specification for compatibility and e
> fit comot anytime for di first change wey go release on or after July 28,
> 2027. Di examples inside dis lesson fit use SDK APIs wey implement `2025-11-25`.
> See [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md).

For old MCP tins wen dem dey do am, Sampling dey allow servers make dem request LLM
completions through di client. Dis lesson go explain dat old protocol
wey dem no dey use again for compatibility and migration work.

## Introduction

For dis lesson, we go check how to set sampling parameters for MCP requests and understand how di sampling protocol run.

## Learning Objectives

By di time you finish dis lesson, you go fit:

- Understand di main sampling parameters wey dey MCP.
- Configure sampling parameters for different use cases.
- Make deterministic sampling wey go produce result wey fit replicate.
- Change sampling parameters on top context and wetin user like dynamically.
- Use sampling strategies to make model work better for different situation.
- Understand how sampling dey work inside di client-server flow for MCP.

## How Sampling Dey Work for MCP

Di sampling process for MCP dey follow dis steps:

1. Server go send `sampling/createMessage` request go client
2. Client go check di request and fit change am
3. Client go sample from one LLM
4. Client go check di completion
5. Client go return di result go server

Dis human-in-the-loop design make sure say users get control for wetin di LLM dey see and how e generate.

## Sampling Parameters Overview

MCP get dis sampling parameters wey you fit set for client requests:

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| `temperature` | Controls randomness for how tokens dem dey select | 0.0 - 1.0 |
| `maxTokens` | Maximum number of tokens wey e go generate | Integer value |
| `stopSequences` | Custom sequences wey go stop generation if dem find am | Array of strings |
| `metadata` | Extra provider-specific parameters | JSON object |

Plenty LLM providers dey support extra parameters through di `metadata` field, like:

| Common Extension Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - dey limit tokens to top cumulative probability | 0.0 - 1.0 |
| `top_k` | Dey limit token selection to top K options | 1 - 100 |
| `presence_penalty` | Dey punish tokens based on how dem dey appear for text so far | -2.0 - 2.0 |
| `frequency_penalty` | Dey punish tokens based on how dem repeat for text so far | -2.0 - 2.0 |
| `seed` | One specific random seed to fit get same result | Integer value |

## Example Request Format

Dis na example wen you go request sampling from client for MCP:

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

Client go return completion result:

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

## Human inside Loop Controls

MCP sampling na e be like say human dey oversee am:

- **For prompts**:
  - Clients suppose show users di proposed prompt
  - Users suppose fit change or reject prompts
  - System prompts fit be filtered or change
  - Context inclusion dey under control of client

- **For completions**:
  - Clients suppose show users di completion
  - Users suppose fit change or reject completions
  - Clients fit filter or change completions
  - Users get control of which model to use

With dis things for mind, make we see how to implement sampling for different programming languages, focus on parameters wey dey common for LLM providers.

## Security Considerations

When you dey implement sampling for MCP, make you remember these security best practices:

- **Check all message content** before you send am go client
- **Clean up sensitive info** from prompts and completions
- **Put rate limits** to prevent abuse
- **Watch sampling usage** for any unusual pattern
- **Encrypt data when e dey travel** using secure protocols
- **Handle user data privacy** as per relevant law dem
- **Audit sampling requests** for compliance and security
- **Control cost exposure** with correct limits
- **Put timeouts** for sampling requests
- **Handle model errors nicely** with correct fallback plans

Sampling parameters dey allow fine-tune how language models go behave to get the right balance between deterministic and creative outputs.

Make we check how to set these parameters for different programming languages.

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

For di code wey dey before, we:

- Create MCP client with one specific server URL.
- Configure request with sampling parameters like `temperature`, `top_p`, and `top_k`.
- Send request and print di text wey dem generate.
- Use:
    - `allowedTools` to specify which tools model fit use as e dey generate. For dis case, we allow `ideaGenerator` and `marketAnalyzer` tools to help generate creative app ideas.
    - `frequencyPenalty` and `presencePenalty` to control repetition and diversity inside output.
    - `temperature` to control how random output go be, if e high e mean say response go dey more creative.
    - `top_p` to limit token selection to tokens wey get top cumulative probability mass, this one dey improve quality of text wey dem generate.
    - `top_k` to limit model to top K most probable tokens, wey fit help get more coherent responses.
    - `frequencyPenalty` and `presencePenalty` to reduce repetition and make generated text get more variety.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript Example: Temperature and Top-P sampling configuration
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Start di MCP client
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Set request wit different sampling parameters
  const creativeSampling = {
    temperature: 0.9,    // Higher temperature mean more randomness/creativity
    topP: 0.92,          // Take tokens wey get top 92% probability mass
    frequencyPenalty: 0.6, // Make repetition of token sequences small
    presencePenalty: 0.4   // Punish tokens wey don show for di text till now
  };
  
  const factualSampling = {
    temperature: 0.2,    // Lower temperature mean more deterministic/factual
    topP: 0.85,          // Small more focused token selection
    frequencyPenalty: 0.2, // Small repetition penalty
    presencePenalty: 0.1   // Small presence penalty
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

For di code wey dey before, we:

- Initialize MCP client with server URL and API key.
- Configure two sets of sampling parameters: one for creative tasks and one for factual tasks.
- Send requests with dis settings, make model fit use specific tools for each task.
- Print di responses wey dem generate to show how different sampling parameters work.
- Use `allowedTools` to specify which tools model fit use as e dey generate. For dis case, we allow `ideaGenerator` and `environmentalImpactTool` for creative tasks, and `factChecker` and `dataAnalysisTool` for factual tasks.
- Use `temperature` to control how random output go be, if e high, e mean say response go dey more creative.
- Use `top_p` to limit token selection to tokens wey get top cumulative probability mass, this one dey improve quality of generated text.
- Use `frequencyPenalty` and `presencePenalty` to reduce repetition and make output get more variety.
- Use `top_k` to limit model to top K most probable tokens, wey fit help get more coherent responses.

---

## Deterministic Sampling

For applications wey need same output every time, deterministic sampling dey ensure say result fit happen again. E dey do dis by using fixed random seed and set temperature to zero.

Make we check the sample implementation below to show deterministic sampling for different programming languages.

# [Java](#tab/java)

```java
// Java Example: Deterministic responses wit fixed seed
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Using one fixed seed for deterministic results
        
        // First request wit fixed seed
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Zero temperature for maximum determinism
            .build();
            
        // Second request wit di same seed
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Run both requests
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Responses suppose be di same because dem get di same seed and temperature=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

For di code wey dey before, we:

- Create MCP client with one server URL.
- Configure two requests with same prompt, fixed seed, and zero temperature.
- Send both requests and print di generated text.
- Show say response be same because sampling configuration get fixed seed and zero temperature.
- Use `setSeed` to specify fixed random seed, make sure model go generate same output for same input anytime.
- Set `temperature` to zero to make sure say e go always choose most probable next token without randomness.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript Example: Deterministic responses wit seed control
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // First request wit fixed seed
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Zero temperature for maximum determinism
    });
    
    // Second request wit same seed and temperature
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Third request wit different seed but same temperature
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

For di code wey dey before, we:

- Initialize MCP client with server URL.
- Configure two requests with same prompt, fixed seed, and zero temperature.
- Send both requests and print di generated text.
- Show say response be same because sampling configuration get fixed seed and zero temperature.
- Use `seed` to specify fixed random seed, make sure model go generate same output for same input anytime.
- Set `temperature` to zero to make sure say e go always choose most probable next token without randomness.
- Use one different seed for third request to show say if you change seed, output go different even if prompt and temperature be same.

---

## Dynamic Sampling Configuration

Intelligent sampling fit change parameters based on context and wetin each request need. E mean say e go dynamically adjust parameters like temperature, top_p, and penalties depending on task type, user preferences, or past performance.

Make we check how to implement dynamic sampling for different programming languages.

# [Python](#tab/python)

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

For di code wey dey before, we:

- Create `DynamicSamplingService` class wey dey manage adaptive sampling.
- Define sampling presets for different task types (creative, factual, code, analytical).
- Choose base sampling preset based on task type.
- Change sampling parameters based on user preferences like creativity level and diversity.
- Send request with dynamically set sampling parameters.
- Return generated text plus sampling parameters and task type for clear understanding.
- Use `temperature` to control how random output go be, if e high, e mean say response go dey more creative.
- Use `top_p` to limit token selection to tokens wey get top cumulative probability mass, this one dey improve quality of generated text.
- Use `frequency_penalty` to reduce repetition and encourage variety for output.
- Use `user_preferences` to allow customization of sampling parameters based on user-defined creativity and diversity levels.
- Use `task_type` to decide sampling strategy for request, make responses fit match task nature.
- Use `send_request` method to send prompt plus configured sampling parameters, make model generate text as required.
- Use `generated_text` to get model response, then return am with sampling parameters and task type for more analysis or display.
- Use `min` and `max` functions to make sure say user preferences dey inside valid range, avoid bad sampling configs.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript example: Dynamic sampling setup based on how user dey
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
    
    // Track how performance don dey before
    this.performanceHistory = [];
  }
  
  // Detect type of task from prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Simple way wey we dey use detect - fit beta improve wit ML classification
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
    
    // Default to talk talk if no clear type show
    return 'conversational';
  }
  
  // Calculate sampling parameters based on context and wetin user like
  getSamplingParameters(prompt, context = {}) {
    // Detect task type
    const taskType = this.detectTaskType(prompt, context);
    
    // Collect base profile
    let params = {...this.samplingProfiles[taskType]};
    
    // Change am based on wetin user like
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Convert from 1-10 go correct temperature range
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // More precision mean lower topP (selection go focused pass)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // More consistency mean penalty go reduce
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Use wetin we don learn from past performance to adjust
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Simple adaptive logic - fit beta improve wit beta sharper algorithm dem
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Only check recent history
    
    if (relevantHistory.length > 0) {
      // Calculate average performance score dem
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // If performance low pass threshold, change parameters
      if (avgScore < 0.7) {
        // Small adjustment go safer values
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Record performance for next adjustment
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 rating of how good response be
    });
    
    // Keep history size small
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
    
    // If user give feedback, record am for better optimization later
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

// Example how to use am
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Creative task with custom settings from user
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

For di code wey dey before, we:

- Create `AdaptiveSamplingManager` class wey dey manage dynamic sampling based on task type and user preferences.
- Define sampling profiles for different task types (creative, factual, code, conversational).
- Implement one method to detect task type from prompt using simple checks.
- Calculate sampling parameters based on detected task type and user preferences.
- Apply learnt adjustments based on past performance to make sampling parameters better.
- Record performance for future adjustments, make system learn from past interactions.
- Send requests with dynamically set sampling parameters, return generated text and applied parameters plus detected task type.
- Use:
    - `userPreferences` to allow customize sampling parameters based on user-defined creativity, precision, and consistency levels.
    - `detectTaskType` to understand task nature from prompt, make responses fit task well.
    - `recordPerformance` to save how generated responses perform, help system adapt and improve over time.
    - `applyLearnedAdjustments` to change sampling parameters based on past performance, make model generate better responses.
    - `generateResponse` to handle whole process of generating response with adaptive sampling, make am easy to call with different prompts and contexts.
    - `allowedTools` to say which tools model fit use while generating, make responses fit context well.
    - `feedbackScore` to allow users give feedback on quality of answer, wey system fit use to improve performance later.
    - `performanceHistory` to keep record of past interactions, make system learn from success and failures.
    - `getSamplingParameters` to dynamically adjust sampling parameters based on request context, make model respond better and flexible.
    - `detectTaskType` to classify task based on prompt, make system apply correct sampling styles for different requests.
    - `samplingProfiles` to set base sampling configs for different task types, make quick change based on request nature.

---

## Wetin dey next

- [5.7 Scaling](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->