# Sampling in Model Context Protocol

Sampling is a powerful MCP feature that allows servers to request LLM completions through the client, enabling sophisticated agentic behaviors while maintaining security and privacy. The right sampling configuration can significantly improve response quality and performance. MCP provides a standardized way to control how models generate text with specific parameters that influence randomness, creativity, and coherence.

## Introduction

In this lesson, we will explore how to configure sampling parameters in MCP requests and understand the underlying protocol mechanics of sampling.

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand the key sampling parameters available in MCP.
- Configure sampling parameters for different use cases.
- Implement deterministic sampling for reproducible results.
- Dynamically adjust sampling parameters based on context and user preferences.
- Apply sampling strategies to enhance model performance in various scenarios.
- Understand how sampling works in the client-server flow of MCP.

## How Sampling Works in MCP

The sampling flow in MCP follows these steps:

1. Server sends a `sampling/createMessage` request to the client  
2. Client reviews the request and can modify it  
3. Client samples from an LLM  
4. Client reviews the completion  
5. Client returns the result to the server  

This human-in-the-loop design ensures users maintain control over what the LLM sees and generates.

## Sampling Parameters Overview

MCP defines the following sampling parameters that can be configured in client requests:

| Parameter       | Description                          | Typical Range  |
|-----------------|----------------------------------|----------------|
| `temperature`   | Controls randomness in token selection | 0.0 - 1.0     |
| `maxTokens`     | Maximum number of tokens to generate | Integer value |
| `stopSequences` | Custom sequences that stop generation when encountered | Array of strings |
| `metadata`      | Additional provider-specific parameters | JSON object   |

Many LLM providers support additional parameters through the `metadata` field, which may include:

| Common Extension Parameter | Description                                         | Typical Range  |
|----------------------------|-----------------------------------------------------|----------------|
| `top_p`                    | Nucleus sampling - limits tokens to top cumulative probability | 0.0 - 1.0     |
| `top_k`                    | Limits token selection to top K options             | 1 - 100        |
| `presence_penalty`         | Penalizes tokens based on their presence in the text so far | -2.0 - 2.0    |
| `frequency_penalty`        | Penalizes tokens based on their frequency in the text so far | -2.0 - 2.0    |
| `seed`                     | Specific random seed for reproducible results       | Integer value  |

## Example Request Format

Here's an example of requesting sampling from a client in MCP:

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

The client returns a completion result:

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

MCP sampling is designed with human oversight in mind:

- **For prompts**:  
  - Clients should show users the proposed prompt  
  - Users should be able to modify or reject prompts  
  - System prompts can be filtered or modified  
  - Context inclusion is controlled by the client  

- **For completions**:  
  - Clients should show users the completion  
  - Users should be able to modify or reject completions  
  - Clients can filter or modify completions  
  - Users control which model is used  

With these principles in mind, let's look at how to implement sampling in different programming languages, focusing on the parameters that are commonly supported across LLM providers.

## Security Considerations

When implementing sampling in MCP, consider these security best practices:

- **Validate all message content** before sending it to the client  
- **Sanitize sensitive information** from prompts and completions  
- **Implement rate limits** to prevent abuse  
- **Monitor sampling usage** for unusual patterns  
- **Encrypt data in transit** using secure protocols  
- **Handle user data privacy** according to relevant regulations  
- **Audit sampling requests** for compliance and security  
- **Control cost exposure** with appropriate limits  
- **Implement timeouts** for sampling requests  
- **Handle model errors gracefully** with appropriate fallbacks  

Sampling parameters allow fine-tuning the behavior of language models to achieve the desired balance between deterministic and creative outputs.

Let's look at how to configure these parameters in different programming languages.

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

In the preceding code we've:

- Created an MCP client with a specific server URL.  
- Configured a request with sampling parameters like `temperature`, `top_p`, and `top_k`.  
- Sent the request and printed the generated text.  
- Used:  
    - `allowedTools` to specify which tools the model can use during generation. In this case, we allowed the `ideaGenerator` and `marketAnalyzer` tools to assist in generating creative app ideas.  
    - `frequencyPenalty` and `presencePenalty` to control repetition and diversity in the output.  
    - `temperature` to control the randomness of the output, where higher values lead to more creative responses.  
    - `top_p` to limit the selection of tokens to those that contribute to the top cumulative probability mass, enhancing the quality of generated text.  
    - `top_k` to restrict the model to the top K most probable tokens, which can help in generating more coherent responses.  
    - `frequencyPenalty` and `presencePenalty` to reduce repetition and encourage diversity in the generated text.  

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

In the preceding code we've:

- Initialized an MCP client with a server URL and API key.  
- Configured two sets of sampling parameters: one for creative tasks and another for factual tasks.  
- Sent requests with these configurations, allowing the model to use specific tools for each task.  
- Printed the generated responses to demonstrate the effects of different sampling parameters.  
- Used `allowedTools` to specify which tools the model can use during generation. In this case, we allowed the `ideaGenerator` and `environmentalImpactTool` for creative tasks, and `factChecker` and `dataAnalysisTool` for factual tasks.  
- Used `temperature` to control the randomness of the output, where higher values lead to more creative responses.  
- Used `top_p` to limit the selection of tokens to those that contribute to the top cumulative probability mass, enhancing the quality of generated text.  
- Used `frequencyPenalty` and `presencePenalty` to reduce repetition and encourage diversity in the output.  
- Used `top_k` to restrict the model to the top K most probable tokens, which can help in generating more coherent responses.  

---

## Deterministic Sampling

For applications requiring consistent outputs, deterministic sampling ensures reproducible results. It achieves this by using a fixed random seed and setting the temperature to zero.

Let's look at the sample implementation below to demonstrate deterministic sampling in different programming languages.

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

In the preceding code we've:

- Created an MCP client with a specified server URL.  
- Configured two requests with the same prompt, fixed seed, and zero temperature.  
- Sent both requests and printed the generated text.  
- Demonstrated that the responses are identical due to the deterministic nature of the sampling configuration (same seed and temperature).  
- Used `setSeed` to specify a fixed random seed, ensuring that the model generates the same output for the same input every time.  
- Set `temperature` to zero to ensure maximum determinism, meaning the model will always select the most probable next token without randomness.  

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

In the preceding code we've:

- Initialized an MCP client with a server URL.  
- Configured two requests with the same prompt, fixed seed, and zero temperature.  
- Sent both requests and printed the generated text.  
- Demonstrated that the responses are identical due to the deterministic nature of the sampling configuration (same seed and temperature).  
- Used `seed` to specify a fixed random seed, ensuring that the model generates the same output for the same input every time.  
- Set `temperature` to zero to ensure maximum determinism, meaning the model will always select the most probable next token without randomness.  
- Used a different seed for the third request to show that changing the seed results in different outputs, even with the same prompt and temperature.  

---

## Dynamic Sampling Configuration

Intelligent sampling adapts parameters based on the context and requirements of each request. This means dynamically adjusting parameters like temperature, top_p, and penalties based on the task type, user preferences, or historical performance.

Let's look at how to implement dynamic sampling in different programming languages.

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

In the preceding code we've:

- Created a `DynamicSamplingService` class that manages adaptive sampling.  
- Defined sampling presets for different task types (creative, factual, code, analytical).  
- Selected a base sampling preset based on the task type.  
- Adjusted the sampling parameters based on user preferences, such as creativity level and diversity.  
- Sent the request with the dynamically configured sampling parameters.  
- Returned the generated text along with the applied sampling parameters and task type for transparency.  
- Used `temperature` to control the randomness of the output, where higher values lead to more creative responses.  
- Used `top_p` to limit the selection of tokens to those that contribute to the top cumulative probability mass, enhancing the quality of generated text.  
- Used `frequency_penalty` to reduce repetition and encourage diversity in the output.  
- Used `user_preferences` to allow customization of the sampling parameters based on user-defined creativity and diversity levels.  
- Used `task_type` to determine the appropriate sampling strategy for the request, allowing for more tailored responses based on the nature of the task.  
- Used `send_request` method to send the prompt with the configured sampling parameters, ensuring that the model generates text according to the specified requirements.  
- Used `generated_text` to retrieve the model's response, which is then returned along with the sampling parameters and task type for further analysis or display.  
- Used `min` and `max` functions to ensure that user preferences are clamped within valid ranges, preventing invalid sampling configurations.  

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

In the preceding code we've:

- Created an `AdaptiveSamplingManager` class that manages dynamic sampling based on task type and user preferences.  
- Defined sampling profiles for different task types (creative, factual, code, conversational).  
- Implemented a method to detect the task type from the prompt using simple heuristics.  
- Calculated sampling parameters based on the detected task type and user preferences.  
- Applied learned adjustments based on historical performance to optimize sampling parameters.  
- Recorded performance for future adjustments, allowing the system to learn from past interactions.  
- Sent requests with dynamically configured sampling parameters and returned the generated text along with applied parameters and detected task type.  
- Used:  
    - `userPreferences` to allow customization of the sampling parameters based on user-defined creativity, precision, and consistency levels.  
    - `detectTaskType` to determine the nature of the task based on the prompt, allowing for more tailored responses.  
    - `recordPerformance` to log the performance of generated responses, enabling the system to adapt and improve over time.  
    - `applyLearnedAdjustments` to modify sampling parameters based on historical performance, enhancing the model's ability to generate high-quality responses.  
    - `generateResponse` to encapsulate the entire process of generating a response with adaptive sampling, making it easy to call with different prompts and contexts.  
    - `allowedTools` to specify which tools the model can use during generation, allowing for more context-aware responses.  
    - `feedbackScore` to allow users to provide feedback on the quality of the generated response, which can be used to further refine the model's performance over time.  
    - `performanceHistory` to maintain a record of past interactions, enabling the system to learn from previous successes and failures.  
    - `getSamplingParameters` to dynamically adjust sampling parameters based on the context of the request, allowing for more flexible and responsive model behavior.  
    - `detectTaskType` to classify the task based on the prompt, enabling the system to apply appropriate sampling strategies for different types of requests.  
    - `samplingProfiles` to define base sampling configurations for different task types, allowing for quick adjustments based on the nature of the request.  

---

## What's next

- [5.7 Scaling](../mcp-scaling/README.md)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.