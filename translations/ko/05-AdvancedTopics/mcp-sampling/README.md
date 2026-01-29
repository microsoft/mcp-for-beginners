# 모델 컨텍스트 프로토콜에서의 샘플링

샘플링은 서버가 클라이언트를 통해 LLM 완성을 요청할 수 있게 하는 강력한 MCP 기능으로, 보안과 프라이버시를 유지하면서 정교한 에이전트 행동을 가능하게 합니다. 적절한 샘플링 설정은 응답 품질과 성능을 크게 향상시킬 수 있습니다. MCP는 무작위성, 창의성, 일관성에 영향을 주는 특정 매개변수를 통해 모델이 텍스트를 생성하는 방식을 표준화된 방법으로 제어합니다.

## 소개

이번 강의에서는 MCP 요청에서 샘플링 매개변수를 설정하는 방법과 샘플링의 기본 프로토콜 메커니즘을 살펴봅니다.

## 학습 목표

이 강의를 마치면 다음을 할 수 있습니다:

- MCP에서 제공하는 주요 샘플링 매개변수를 이해한다.
- 다양한 사용 사례에 맞게 샘플링 매개변수를 구성한다.
- 재현 가능한 결과를 위한 결정론적 샘플링을 구현한다.
- 상황과 사용자 선호도에 따라 샘플링 매개변수를 동적으로 조정한다.
- 다양한 시나리오에서 모델 성능 향상을 위한 샘플링 전략을 적용한다.
- MCP의 클라이언트-서버 흐름에서 샘플링이 어떻게 작동하는지 이해한다.

## MCP에서 샘플링 작동 방식

MCP의 샘플링 흐름은 다음과 같습니다:

1. 서버가 클라이언트에 `sampling/createMessage` 요청을 보냄
2. 클라이언트가 요청을 검토하고 수정 가능
3. 클라이언트가 LLM에서 샘플링 수행
4. 클라이언트가 완성 결과를 검토
5. 클라이언트가 결과를 서버에 반환

이 인간 개입형 설계는 사용자가 LLM이 보는 내용과 생성하는 내용을 직접 제어할 수 있도록 보장합니다.

## 샘플링 매개변수 개요

MCP는 클라이언트 요청에서 설정할 수 있는 다음과 같은 샘플링 매개변수를 정의합니다:

| 매개변수 | 설명 | 일반 범위 |
|-----------|-------------|---------------|
| `temperature` | 토큰 선택의 무작위성 제어 | 0.0 - 1.0 |
| `maxTokens` | 생성할 최대 토큰 수 | 정수 값 |
| `stopSequences` | 생성 중단을 유발하는 사용자 정의 시퀀스 | 문자열 배열 |
| `metadata` | 추가 제공자별 매개변수 | JSON 객체 |

많은 LLM 제공자는 `metadata` 필드를 통해 다음과 같은 추가 매개변수를 지원합니다:

| 일반 확장 매개변수 | 설명 | 일반 범위 |
|-----------|-------------|---------------|
| `top_p` | 누클리어스 샘플링 - 누적 확률 상위 토큰으로 제한 | 0.0 - 1.0 |
| `top_k` | 토큰 선택을 상위 K개 옵션으로 제한 | 1 - 100 |
| `presence_penalty` | 이미 등장한 토큰에 대한 페널티 부여 | -2.0 - 2.0 |
| `frequency_penalty` | 토큰 빈도에 따른 페널티 부여 | -2.0 - 2.0 |
| `seed` | 재현 가능한 결과를 위한 고정 랜덤 시드 | 정수 값 |

## 요청 예시 형식

다음은 MCP에서 클라이언트에 샘플링을 요청하는 예시입니다:

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

## 응답 형식

클라이언트는 완성 결과를 반환합니다:

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

## 인간 개입형 제어

MCP 샘플링은 인간 감독을 염두에 두고 설계되었습니다:

- **프롬프트에 대해**:
  - 클라이언트는 사용자에게 제안된 프롬프트를 보여야 합니다.
  - 사용자는 프롬프트를 수정하거나 거부할 수 있어야 합니다.
  - 시스템 프롬프트는 필터링하거나 수정할 수 있습니다.
  - 컨텍스트 포함 여부는 클라이언트가 제어합니다.

- **완성에 대해**:
  - 클라이언트는 사용자에게 완성 결과를 보여야 합니다.
  - 사용자는 완성 결과를 수정하거나 거부할 수 있어야 합니다.
  - 클라이언트는 완성 결과를 필터링하거나 수정할 수 있습니다.
  - 사용자가 사용할 모델을 선택할 수 있습니다.

이 원칙을 바탕으로, 다양한 프로그래밍 언어에서 공통적으로 지원되는 매개변수에 초점을 맞춰 샘플링 구현 방법을 살펴봅니다.

## 보안 고려사항

MCP에서 샘플링을 구현할 때 다음 보안 모범 사례를 고려하세요:

- 클라이언트에 보내기 전 모든 메시지 내용을 검증합니다.
- 프롬프트와 완성에서 민감한 정보를 정제합니다.
- 남용 방지를 위한 속도 제한을 구현합니다.
- 비정상적인 샘플링 사용 패턴을 모니터링합니다.
- 안전한 프로토콜을 사용해 전송 중 데이터를 암호화합니다.
- 관련 규정에 따라 사용자 데이터 프라이버시를 처리합니다.
- 준수 및 보안을 위해 샘플링 요청을 감사합니다.
- 적절한 제한으로 비용 노출을 통제합니다.
- 샘플링 요청에 타임아웃을 설정합니다.
- 모델 오류 발생 시 적절한 대체 방안을 마련합니다.

샘플링 매개변수는 결정론적 출력과 창의적 출력을 적절히 조절할 수 있도록 모델 동작을 미세 조정할 수 있게 합니다.

다음으로 다양한 프로그래밍 언어에서 이 매개변수를 설정하는 방법을 살펴보겠습니다.

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

위 코드에서는:

- 특정 서버 URL로 MCP 클라이언트를 생성했습니다.
- `temperature`, `top_p`, `top_k` 같은 샘플링 매개변수를 포함한 요청을 구성했습니다.
- 요청을 보내고 생성된 텍스트를 출력했습니다.
- 다음을 사용했습니다:
    - `allowedTools`로 모델이 생성 중 사용할 수 있는 도구를 지정했습니다. 여기서는 `ideaGenerator`와 `marketAnalyzer` 도구를 허용해 창의적인 앱 아이디어 생성에 도움을 주었습니다.
    - `frequencyPenalty`와 `presencePenalty`로 출력의 반복성과 다양성을 제어했습니다.
    - `temperature`로 출력의 무작위성을 조절했으며, 값이 높을수록 더 창의적인 응답이 생성됩니다.
    - `top_p`로 누적 확률 상위 토큰만 선택하도록 제한해 생성 텍스트 품질을 향상시켰습니다.
    - `top_k`로 모델이 상위 K개의 가장 가능성 높은 토큰만 선택하도록 제한해 더 일관된 응답을 생성하도록 했습니다.
    - `frequencyPenalty`와 `presencePenalty`를 사용해 반복을 줄이고 다양성을 촉진했습니다.

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

위 코드에서는:

- 서버 URL과 API 키로 MCP 클라이언트를 초기화했습니다.
- 창의적 작업과 사실적 작업을 위한 두 가지 샘플링 매개변수 세트를 구성했습니다.
- 각 구성으로 요청을 보내고, 모델이 각 작업에 맞는 특정 도구를 사용하도록 허용했습니다.
- 생성된 응답을 출력해 다양한 샘플링 매개변수의 효과를 보여주었습니다.
- `allowedTools`로 모델이 생성 중 사용할 수 있는 도구를 지정했습니다. 창의적 작업에는 `ideaGenerator`와 `environmentalImpactTool`을, 사실적 작업에는 `factChecker`와 `dataAnalysisTool`을 허용했습니다.
- `temperature`로 출력의 무작위성을 조절했으며, 값이 높을수록 더 창의적인 응답이 생성됩니다.
- `top_p`로 누적 확률 상위 토큰만 선택하도록 제한해 생성 텍스트 품질을 향상시켰습니다.
- `frequencyPenalty`와 `presencePenalty`로 반복을 줄이고 다양성을 촉진했습니다.
- `top_k`로 모델이 상위 K개의 가장 가능성 높은 토큰만 선택하도록 제한해 더 일관된 응답을 생성하도록 했습니다.

---

## 결정론적 샘플링

일관된 출력을 요구하는 애플리케이션에서는 결정론적 샘플링이 재현 가능한 결과를 보장합니다. 이는 고정된 랜덤 시드를 사용하고 온도를 0으로 설정함으로써 구현됩니다.

다음은 다양한 프로그래밍 언어에서 결정론적 샘플링을 시연하는 예시입니다.

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

위 코드에서는:

- 지정된 서버 URL로 MCP 클라이언트를 생성했습니다.
- 동일한 프롬프트, 고정 시드, 온도 0으로 두 개의 요청을 구성했습니다.
- 두 요청을 보내고 생성된 텍스트를 출력했습니다.
- 샘플링 설정(같은 시드와 온도) 덕분에 응답이 동일함을 보여주었습니다.
- `setSeed`를 사용해 고정 랜덤 시드를 지정해 동일 입력에 대해 항상 같은 출력을 생성하도록 했습니다.
- `temperature`를 0으로 설정해 최대한 결정론적으로, 즉 무작위성 없이 가장 가능성 높은 다음 토큰을 항상 선택하도록 했습니다.

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

위 코드에서는:

- 서버 URL로 MCP 클라이언트를 초기화했습니다.
- 동일한 프롬프트, 고정 시드, 온도 0으로 두 개의 요청을 구성했습니다.
- 두 요청을 보내고 생성된 텍스트를 출력했습니다.
- 샘플링 설정(같은 시드와 온도) 덕분에 응답이 동일함을 보여주었습니다.
- `seed`를 사용해 고정 랜덤 시드를 지정해 동일 입력에 대해 항상 같은 출력을 생성하도록 했습니다.
- `temperature`를 0으로 설정해 최대한 결정론적으로, 즉 무작위성 없이 가장 가능성 높은 다음 토큰을 항상 선택하도록 했습니다.
- 세 번째 요청에는 다른 시드를 사용해, 같은 프롬프트와 온도임에도 시드 변경으로 다른 출력이 생성됨을 보여주었습니다.

---

## 동적 샘플링 구성

지능형 샘플링은 각 요청의 상황과 요구에 따라 매개변수를 조정합니다. 즉, 작업 유형, 사용자 선호도, 과거 성과에 따라 `temperature`, `top_p`, 페널티 등을 동적으로 변경합니다.

다음은 다양한 프로그래밍 언어에서 동적 샘플링을 구현하는 방법입니다.

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

위 코드에서는:

- 적응형 샘플링을 관리하는 `DynamicSamplingService` 클래스를 만들었습니다.
- 창의적, 사실적, 코드, 분석 작업 유형별 샘플링 프리셋을 정의했습니다.
- 작업 유형에 따라 기본 샘플링 프리셋을 선택했습니다.
- 사용자 선호도(창의성 수준, 다양성 등)에 따라 샘플링 매개변수를 조정했습니다.
- 동적으로 구성된 샘플링 매개변수로 요청을 보냈습니다.
- 생성된 텍스트와 적용된 샘플링 매개변수, 작업 유형을 함께 반환했습니다.
- `temperature`로 출력 무작위성을 조절해 값이 높을수록 더 창의적인 응답을 생성했습니다.
- `top_p`로 누적 확률 상위 토큰만 선택하도록 제한해 생성 텍스트 품질을 향상시켰습니다.
- `frequency_penalty`로 반복을 줄이고 다양성을 촉진했습니다.
- `user_preferences`를 사용해 사용자 정의 창의성 및 다양성 수준에 따라 샘플링 매개변수를 맞춤 설정했습니다.
- `task_type`을 사용해 요청에 적합한 샘플링 전략을 결정해 작업 특성에 맞는 응답을 가능하게 했습니다.
- `send_request` 메서드로 구성된 샘플링 매개변수와 함께 프롬프트를 보내 모델이 요구사항에 맞게 텍스트를 생성하도록 했습니다.
- `generated_text`로 모델 응답을 받아 샘플링 매개변수 및 작업 유형과 함께 반환해 투명성을 높였습니다.
- `min`과 `max` 함수를 사용해 사용자 선호도가 유효 범위 내에 있도록 제한했습니다.

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

위 코드에서는:

- 작업 유형과 사용자 선호도에 따라 동적 샘플링을 관리하는 `AdaptiveSamplingManager` 클래스를 만들었습니다.
- 창의적, 사실적, 코드, 대화형 작업 유형별 샘플링 프로필을 정의했습니다.
- 간단한 휴리스틱을 사용해 프롬프트에서 작업 유형을 감지하는 메서드를 구현했습니다.
- 감지된 작업 유형과 사용자 선호도에 따라 샘플링 매개변수를 계산했습니다.
- 과거 성과를 기반으로 학습된 조정을 적용해 샘플링 매개변수를 최적화했습니다.
- 향후 조정을 위해 성과를 기록해 시스템이 과거 상호작용에서 학습할 수 있도록 했습니다.
- 동적으로 구성된 샘플링 매개변수로 요청을 보내고, 생성된 텍스트와 적용된 매개변수, 감지된 작업 유형을 반환했습니다.
- 다음을 사용했습니다:
    - `userPreferences`로 사용자 정의 창의성, 정밀성, 일관성 수준에 따라 샘플링 매개변수를 맞춤 설정했습니다.
    - `detectTaskType`으로 프롬프트를 분석해 작업 특성을 파악, 보다 맞춤화된 응답을 가능하게 했습니다.
    - `recordPerformance`로 생성된 응답의 성과를 기록해 시스템이 적응하고 개선할 수 있도록 했습니다.
    - `applyLearnedAdjustments`로 과거 성과를 반영해 샘플링 매개변수를 조정, 고품질 응답 생성을 지원했습니다.
    - `generateResponse`로 적응형 샘플링을 적용한 응답 생성 과정을 캡슐화해 다양한 프롬프트와 컨텍스트에 쉽게 호출할 수 있도록 했습니다.
    - `allowedTools`로 모델이 생성 중 사용할 수 있는 도구를 지정해 더 상황에 맞는 응답을 가능하게 했습니다.
    - `feedbackScore`로 사용자가 생성된 응답 품질에 대한 피드백을 제공할 수 있게 해, 모델 성능을 지속적으로 개선할 수 있도록 했습니다.
    - `performanceHistory`로 과거 상호작용 기록을 유지해 시스템이 이전 성공과 실패에서 학습할 수 있도록 했습니다.
    - `getSamplingParameters`로 요청 상황에 따라 샘플링 매개변수를 동적으로 조정해 더 유연하고 반응성 높은 모델 동작을 가능하게 했습니다.
    - `detectTaskType`으로 프롬프트를 기반으로 작업을 분류해 다양한 요청 유형에 적합한 샘플링 전략을 적용했습니다.
    - `samplingProfiles`로 작업 유형별 기본 샘플링 구성을 정의해 요청 특성에 따라 빠르게 조정할 수 있도록 했습니다.

---

## 다음 단계

- [5.7 확장](../mcp-scaling/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.