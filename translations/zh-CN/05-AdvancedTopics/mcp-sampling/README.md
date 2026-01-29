# Sampling in Model Context Protocol

Sampling 是 MCP 的一个强大功能，允许服务器通过客户端请求 LLM 完成，从而实现复杂的代理行为，同时保持安全性和隐私。合适的采样配置可以显著提升响应质量和性能。MCP 提供了一种标准化方式，通过特定参数控制模型生成文本的随机性、创造力和连贯性。

## 介绍

本课将探讨如何在 MCP 请求中配置采样参数，并理解采样的底层协议机制。

## 学习目标

完成本课后，您将能够：

- 理解 MCP 中可用的关键采样参数。
- 针对不同用例配置采样参数。
- 实现确定性采样以获得可复现的结果。
- 根据上下文和用户偏好动态调整采样参数。
- 应用采样策略提升模型在各种场景下的表现。
- 理解采样在 MCP 客户端-服务器流程中的工作原理。

## MCP 中采样的工作原理

MCP 中的采样流程如下：

1. 服务器向客户端发送 `sampling/createMessage` 请求
2. 客户端审核请求并可进行修改
3. 客户端从 LLM 中采样
4. 客户端审核完成结果
5. 客户端将结果返回给服务器

这种人机交互设计确保用户对 LLM 所见和生成内容保持控制。

## 采样参数概览

MCP 定义了以下可在客户端请求中配置的采样参数：

| 参数 | 描述 | 典型范围 |
|-----------|-------------|---------------|
| `temperature` | 控制选词的随机性 | 0.0 - 1.0 |
| `maxTokens` | 最大生成 token 数量 | 整数值 |
| `stopSequences` | 遇到自定义序列时停止生成 | 字符串数组 |
| `metadata` | 额外的提供商特定参数 | JSON 对象 |

许多 LLM 提供商通过 `metadata` 字段支持额外参数，可能包括：

| 常见扩展参数 | 描述 | 典型范围 |
|-----------|-------------|---------------|
| `top_p` | 核采样 - 限制 token 到累计概率最高部分 | 0.0 - 1.0 |
| `top_k` | 限制选词范围到前 K 个选项 | 1 - 100 |
| `presence_penalty` | 根据文本中 token 出现情况进行惩罚 | -2.0 - 2.0 |
| `frequency_penalty` | 根据文本中 token 频率进行惩罚 | -2.0 - 2.0 |
| `seed` | 固定随机种子以实现可复现结果 | 整数值 |

## 请求示例格式

以下是 MCP 中向客户端请求采样的示例：

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

## 响应格式

客户端返回完成结果：

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

## 人机交互控制

MCP 采样设计时考虑了人工监督：

- **针对提示**：
  - 客户端应向用户展示拟定的提示
  - 用户应能修改或拒绝提示
  - 系统提示可被过滤或修改
  - 上下文包含由客户端控制

- **针对完成结果**：
  - 客户端应向用户展示完成内容
  - 用户应能修改或拒绝完成结果
  - 客户端可过滤或修改完成内容
  - 用户控制所用模型

基于这些原则，下面将展示如何在不同编程语言中实现采样，重点关注各 LLM 提供商普遍支持的参数。

## 安全注意事项

在 MCP 中实现采样时，请考虑以下安全最佳实践：

- **验证所有消息内容**，确保发送给客户端前无误
- **清理提示和完成内容中的敏感信息**
- **实施速率限制**，防止滥用
- **监控采样使用情况**，发现异常模式
- **使用安全协议加密传输数据**
- **根据相关法规处理用户数据隐私**
- **审计采样请求**，确保合规和安全
- **控制成本暴露**，设置适当限制
- **为采样请求设置超时**
- **优雅处理模型错误**，提供合适的降级方案

采样参数允许微调语言模型的行为，实现确定性与创造性输出之间的理想平衡。

接下来看看如何在不同编程语言中配置这些参数。

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

在上述代码中我们：

- 创建了一个带有特定服务器 URL 的 MCP 客户端。
- 配置了包含 `temperature`、`top_p` 和 `top_k` 等采样参数的请求。
- 发送请求并打印生成的文本。
- 使用了：
    - `allowedTools` 指定模型生成时可使用的工具。本例中允许 `ideaGenerator` 和 `marketAnalyzer` 工具协助生成创意应用点子。
    - `frequencyPenalty` 和 `presencePenalty` 控制输出的重复性和多样性。
    - `temperature` 控制输出的随机性，数值越高，响应越具创造性。
    - `top_p` 限制选词范围为累计概率最高的部分，提升生成文本质量。
    - `top_k` 限制模型仅从概率最高的 K 个 token 中选择，有助于生成更连贯的响应。
    - `frequencyPenalty` 和 `presencePenalty` 用于减少重复并鼓励多样性。

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

在上述代码中我们：

- 使用服务器 URL 和 API 密钥初始化了 MCP 客户端。
- 配置了两组采样参数：一组用于创意任务，另一组用于事实任务。
- 发送了带有这些配置的请求，允许模型针对不同任务使用特定工具。
- 打印生成的响应，展示不同采样参数的效果。
- 使用 `allowedTools` 指定模型生成时可用的工具。本例中创意任务允许 `ideaGenerator` 和 `environmentalImpactTool`，事实任务允许 `factChecker` 和 `dataAnalysisTool`。
- 使用 `temperature` 控制输出随机性，数值越高响应越具创造性。
- 使用 `top_p` 限制选词范围为累计概率最高部分，提升生成文本质量。
- 使用 `frequencyPenalty` 和 `presencePenalty` 减少重复并鼓励多样性。
- 使用 `top_k` 限制模型仅从概率最高的 K 个 token 中选择，有助于生成更连贯的响应。

---

## 确定性采样

对于需要一致输出的应用，确定性采样确保结果可复现。其方法是使用固定随机种子并将温度设为零。

下面示例展示了如何在不同编程语言中实现确定性采样。

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

在上述代码中我们：

- 创建了一个指定服务器 URL 的 MCP 客户端。
- 配置了两个请求，使用相同提示、固定种子和零温度。
- 发送两个请求并打印生成文本。
- 演示了由于采样配置的确定性（相同种子和温度），响应内容完全一致。
- 使用 `setSeed` 指定固定随机种子，确保相同输入每次生成相同输出。
- 将 `temperature` 设为零，确保最大确定性，模型总是选择最可能的下一个 token，无随机性。

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

在上述代码中我们：

- 使用服务器 URL 初始化 MCP 客户端。
- 配置了两个请求，使用相同提示、固定种子和零温度。
- 发送两个请求并打印生成文本。
- 演示了由于采样配置的确定性（相同种子和温度），响应内容完全一致。
- 使用 `seed` 指定固定随机种子，确保相同输入每次生成相同输出。
- 将 `temperature` 设为零，确保最大确定性，模型总是选择最可能的下一个 token，无随机性。
- 对第三个请求使用不同种子，展示即使提示和温度相同，改变种子也会产生不同输出。

---

## 动态采样配置

智能采样根据每个请求的上下文和需求调整参数。这意味着根据任务类型、用户偏好或历史表现动态调整 temperature、top_p 和惩罚参数。

下面展示如何在不同编程语言中实现动态采样。

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

在上述代码中我们：

- 创建了一个管理自适应采样的 `DynamicSamplingService` 类。
- 定义了针对不同任务类型（创意、事实、代码、分析）的采样预设。
- 根据任务类型选择基础采样预设。
- 根据用户偏好（如创造力和多样性）调整采样参数。
- 发送带有动态配置采样参数的请求。
- 返回生成文本及所用采样参数和任务类型，确保透明度。
- 使用 `temperature` 控制输出随机性，数值越高响应越具创造性。
- 使用 `top_p` 限制选词范围为累计概率最高部分，提升生成文本质量。
- 使用 `frequency_penalty` 减少重复并鼓励多样性。
- 使用 `user_preferences` 允许基于用户定义的创造力和多样性水平自定义采样参数。
- 使用 `task_type` 确定请求的合适采样策略，实现更针对性的响应。
- 使用 `send_request` 方法发送带有配置采样参数的提示，确保模型按要求生成文本。
- 使用 `generated_text` 获取模型响应，并连同采样参数和任务类型一并返回，便于后续分析或展示。
- 使用 `min` 和 `max` 函数确保用户偏好值在有效范围内，防止无效采样配置。

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

在上述代码中我们：

- 创建了一个基于任务类型和用户偏好的动态采样管理类 `AdaptiveSamplingManager`。
- 定义了针对不同任务类型（创意、事实、代码、对话）的采样配置档案。
- 实现了一个简单启发式方法从提示中检测任务类型。
- 根据检测到的任务类型和用户偏好计算采样参数。
- 应用基于历史表现的学习调整，优化采样参数。
- 记录性能以便未来调整，使系统能从过去交互中学习。
- 发送带有动态配置采样参数的请求，返回生成文本及应用的参数和检测到的任务类型。
- 使用了：
    - `userPreferences` 允许基于用户定义的创造力、精确度和一致性水平自定义采样参数。
    - `detectTaskType` 根据提示确定任务性质，实现更针对性的响应。
    - `recordPerformance` 记录生成响应的表现，使系统能适应和改进。
    - `applyLearnedAdjustments` 基于历史表现调整采样参数，提升模型生成高质量响应的能力。
    - `generateResponse` 封装整个自适应采样生成过程，方便不同提示和上下文调用。
    - `allowedTools` 指定模型生成时可用的工具，实现更具上下文感知的响应。
    - `feedbackScore` 允许用户对生成响应质量提供反馈，用于进一步优化模型表现。
    - `performanceHistory` 维护过去交互记录，使系统能从成功和失败中学习。
    - `getSamplingParameters` 根据请求上下文动态调整采样参数，实现更灵活响应。
    - `detectTaskType` 对提示进行分类，应用适合不同请求类型的采样策略。
    - `samplingProfiles` 定义不同任务类型的基础采样配置，便于根据请求性质快速调整。

---

## 后续内容

- [5.7 Scaling](../mcp-scaling/README.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。