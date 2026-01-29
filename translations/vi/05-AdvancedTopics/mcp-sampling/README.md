# Sampling trong Giao thức Model Context Protocol

Sampling là một tính năng mạnh mẽ của MCP cho phép server yêu cầu các kết quả hoàn thành từ LLM thông qua client, giúp tạo ra các hành vi tác nhân phức tạp đồng thời đảm bảo an ninh và quyền riêng tư. Cấu hình sampling phù hợp có thể cải thiện đáng kể chất lượng và hiệu suất phản hồi. MCP cung cấp một cách chuẩn hóa để kiểm soát cách các mô hình tạo văn bản với các tham số cụ thể ảnh hưởng đến độ ngẫu nhiên, sáng tạo và tính mạch lạc.

## Giới thiệu

Trong bài học này, chúng ta sẽ tìm hiểu cách cấu hình các tham số sampling trong các yêu cầu MCP và hiểu cơ chế giao thức sampling bên dưới.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Hiểu các tham số sampling chính có trong MCP.
- Cấu hình các tham số sampling cho các trường hợp sử dụng khác nhau.
- Triển khai sampling xác định để có kết quả có thể tái tạo.
- Điều chỉnh tham số sampling một cách linh hoạt dựa trên ngữ cảnh và sở thích người dùng.
- Áp dụng các chiến lược sampling để nâng cao hiệu suất mô hình trong nhiều tình huống.
- Hiểu cách sampling hoạt động trong luồng client-server của MCP.

## Cách Sampling hoạt động trong MCP

Luồng sampling trong MCP theo các bước sau:

1. Server gửi yêu cầu `sampling/createMessage` đến client
2. Client xem xét yêu cầu và có thể chỉnh sửa nó
3. Client thực hiện sampling từ LLM
4. Client xem lại kết quả hoàn thành
5. Client trả kết quả về server

Thiết kế có sự tham gia của con người này đảm bảo người dùng kiểm soát được những gì LLM nhìn thấy và tạo ra.

## Tổng quan các tham số Sampling

MCP định nghĩa các tham số sampling sau có thể cấu hình trong yêu cầu của client:

| Tham số | Mô tả | Phạm vi điển hình |
|---------|--------|-------------------|
| `temperature` | Điều khiển độ ngẫu nhiên trong việc chọn token | 0.0 - 1.0 |
| `maxTokens` | Số lượng token tối đa được tạo ra | Giá trị nguyên |
| `stopSequences` | Các chuỗi tùy chỉnh dừng việc tạo khi gặp phải | Mảng chuỗi |
| `metadata` | Các tham số bổ sung theo nhà cung cấp | Đối tượng JSON |

Nhiều nhà cung cấp LLM hỗ trợ các tham số mở rộng qua trường `metadata`, có thể bao gồm:

| Tham số mở rộng phổ biến | Mô tả | Phạm vi điển hình |
|-------------------------|--------|-------------------|
| `top_p` | Nucleus sampling - giới hạn token trong xác suất tích lũy hàng đầu | 0.0 - 1.0 |
| `top_k` | Giới hạn lựa chọn token trong top K lựa chọn | 1 - 100 |
| `presence_penalty` | Phạt token dựa trên sự xuất hiện của chúng trong văn bản trước đó | -2.0 - 2.0 |
| `frequency_penalty` | Phạt token dựa trên tần suất xuất hiện trong văn bản trước đó | -2.0 - 2.0 |
| `seed` | Hạt giống ngẫu nhiên cố định để có kết quả tái tạo | Giá trị nguyên |

## Ví dụ định dạng yêu cầu

Dưới đây là ví dụ yêu cầu sampling từ client trong MCP:

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

## Định dạng phản hồi

Client trả về kết quả hoàn thành:

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

## Kiểm soát có sự tham gia của con người

Sampling trong MCP được thiết kế với sự giám sát của con người:

- **Đối với prompt**:
  - Client nên hiển thị prompt đề xuất cho người dùng
  - Người dùng có thể chỉnh sửa hoặc từ chối prompt
  - Prompt hệ thống có thể được lọc hoặc chỉnh sửa
  - Việc đưa ngữ cảnh vào được client kiểm soát

- **Đối với kết quả hoàn thành**:
  - Client nên hiển thị kết quả hoàn thành cho người dùng
  - Người dùng có thể chỉnh sửa hoặc từ chối kết quả
  - Client có thể lọc hoặc chỉnh sửa kết quả
  - Người dùng kiểm soát mô hình được sử dụng

Với các nguyên tắc này, hãy cùng xem cách triển khai sampling trong các ngôn ngữ lập trình khác nhau, tập trung vào các tham số được hỗ trợ phổ biến bởi các nhà cung cấp LLM.

## Các lưu ý về bảo mật

Khi triển khai sampling trong MCP, hãy cân nhắc các thực hành bảo mật sau:

- **Xác thực toàn bộ nội dung tin nhắn** trước khi gửi đến client
- **Làm sạch thông tin nhạy cảm** từ prompt và kết quả hoàn thành
- **Áp dụng giới hạn tốc độ** để ngăn chặn lạm dụng
- **Giám sát việc sử dụng sampling** để phát hiện các mẫu bất thường
- **Mã hóa dữ liệu khi truyền tải** bằng các giao thức an toàn
- **Xử lý quyền riêng tư dữ liệu người dùng** theo các quy định liên quan
- **Kiểm tra các yêu cầu sampling** để đảm bảo tuân thủ và an ninh
- **Kiểm soát chi phí** với các giới hạn phù hợp
- **Áp dụng timeout** cho các yêu cầu sampling
- **Xử lý lỗi mô hình một cách mềm dẻo** với các phương án dự phòng thích hợp

Các tham số sampling cho phép tinh chỉnh hành vi của mô hình ngôn ngữ để đạt được sự cân bằng mong muốn giữa kết quả xác định và sáng tạo.

Hãy cùng xem cách cấu hình các tham số này trong các ngôn ngữ lập trình khác nhau.

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

Trong đoạn mã trên, chúng ta đã:

- Tạo một client MCP với URL server cụ thể.
- Cấu hình yêu cầu với các tham số sampling như `temperature`, `top_p`, và `top_k`.
- Gửi yêu cầu và in ra văn bản được tạo.
- Sử dụng:
    - `allowedTools` để chỉ định các công cụ mà mô hình có thể sử dụng trong quá trình tạo. Trong trường hợp này, chúng ta cho phép các công cụ `ideaGenerator` và `marketAnalyzer` hỗ trợ tạo ý tưởng ứng dụng sáng tạo.
    - `frequencyPenalty` và `presencePenalty` để kiểm soát sự lặp lại và đa dạng trong đầu ra.
    - `temperature` để điều khiển độ ngẫu nhiên của kết quả, giá trị cao hơn dẫn đến phản hồi sáng tạo hơn.
    - `top_p` để giới hạn lựa chọn token trong tập hợp có xác suất tích lũy hàng đầu, nâng cao chất lượng văn bản tạo ra.
    - `top_k` để giới hạn mô hình chỉ chọn trong top K token có xác suất cao nhất, giúp tạo ra phản hồi mạch lạc hơn.
    - `frequencyPenalty` và `presencePenalty` để giảm sự lặp lại và khuyến khích đa dạng trong văn bản tạo ra.

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

Trong đoạn mã trên, chúng ta đã:

- Khởi tạo một client MCP với URL server và khóa API.
- Cấu hình hai bộ tham số sampling: một cho tác vụ sáng tạo và một cho tác vụ thực tế.
- Gửi các yêu cầu với các cấu hình này, cho phép mô hình sử dụng các công cụ cụ thể cho từng tác vụ.
- In ra các phản hồi được tạo để minh họa hiệu quả của các tham số sampling khác nhau.
- Sử dụng `allowedTools` để chỉ định các công cụ mà mô hình có thể sử dụng trong quá trình tạo. Trong trường hợp này, chúng ta cho phép `ideaGenerator` và `environmentalImpactTool` cho tác vụ sáng tạo, và `factChecker` cùng `dataAnalysisTool` cho tác vụ thực tế.
- Sử dụng `temperature` để điều khiển độ ngẫu nhiên của kết quả, giá trị cao hơn dẫn đến phản hồi sáng tạo hơn.
- Sử dụng `top_p` để giới hạn lựa chọn token trong tập hợp có xác suất tích lũy hàng đầu, nâng cao chất lượng văn bản tạo ra.
- Sử dụng `frequencyPenalty` và `presencePenalty` để giảm sự lặp lại và khuyến khích đa dạng trong đầu ra.
- Sử dụng `top_k` để giới hạn mô hình chỉ chọn trong top K token có xác suất cao nhất, giúp tạo ra phản hồi mạch lạc hơn.

---

## Sampling xác định

Đối với các ứng dụng cần kết quả nhất quán, sampling xác định đảm bảo kết quả có thể tái tạo. Cách thực hiện là sử dụng hạt giống ngẫu nhiên cố định và đặt nhiệt độ bằng 0.

Hãy xem ví dụ triển khai dưới đây để minh họa sampling xác định trong các ngôn ngữ lập trình khác nhau.

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

Trong đoạn mã trên, chúng ta đã:

- Tạo một client MCP với URL server được chỉ định.
- Cấu hình hai yêu cầu với cùng một prompt, hạt giống cố định và nhiệt độ bằng 0.
- Gửi cả hai yêu cầu và in ra văn bản được tạo.
- Minh họa rằng các phản hồi giống hệt nhau do tính xác định của cấu hình sampling (cùng hạt giống và nhiệt độ).
- Sử dụng `setSeed` để chỉ định hạt giống ngẫu nhiên cố định, đảm bảo mô hình tạo ra cùng một kết quả cho cùng một đầu vào mỗi lần.
- Đặt `temperature` bằng 0 để đảm bảo tính xác định tối đa, nghĩa là mô hình luôn chọn token tiếp theo có xác suất cao nhất mà không có ngẫu nhiên.

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

Trong đoạn mã trên, chúng ta đã:

- Khởi tạo một client MCP với URL server.
- Cấu hình hai yêu cầu với cùng một prompt, hạt giống cố định và nhiệt độ bằng 0.
- Gửi cả hai yêu cầu và in ra văn bản được tạo.
- Minh họa rằng các phản hồi giống hệt nhau do tính xác định của cấu hình sampling (cùng hạt giống và nhiệt độ).
- Sử dụng `seed` để chỉ định hạt giống ngẫu nhiên cố định, đảm bảo mô hình tạo ra cùng một kết quả cho cùng một đầu vào mỗi lần.
- Đặt `temperature` bằng 0 để đảm bảo tính xác định tối đa, nghĩa là mô hình luôn chọn token tiếp theo có xác suất cao nhất mà không có ngẫu nhiên.
- Sử dụng hạt giống khác cho yêu cầu thứ ba để cho thấy việc thay đổi hạt giống sẽ tạo ra kết quả khác, ngay cả khi cùng prompt và nhiệt độ.

---

## Cấu hình Sampling động

Sampling thông minh điều chỉnh các tham số dựa trên ngữ cảnh và yêu cầu của từng yêu cầu. Điều này có nghĩa là điều chỉnh linh hoạt các tham số như temperature, top_p và các hình phạt dựa trên loại tác vụ, sở thích người dùng hoặc hiệu suất lịch sử.

Hãy xem cách triển khai sampling động trong các ngôn ngữ lập trình khác nhau.

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

Trong đoạn mã trên, chúng ta đã:

- Tạo lớp `DynamicSamplingService` quản lý sampling thích ứng.
- Định nghĩa các cấu hình sampling mặc định cho các loại tác vụ khác nhau (sáng tạo, thực tế, mã, phân tích).
- Chọn cấu hình sampling cơ bản dựa trên loại tác vụ.
- Điều chỉnh các tham số sampling dựa trên sở thích người dùng, như mức độ sáng tạo và đa dạng.
- Gửi yêu cầu với các tham số sampling được cấu hình động.
- Trả về văn bản được tạo cùng với các tham số sampling và loại tác vụ để minh bạch.
- Sử dụng `temperature` để điều khiển độ ngẫu nhiên của kết quả, giá trị cao hơn dẫn đến phản hồi sáng tạo hơn.
- Sử dụng `top_p` để giới hạn lựa chọn token trong tập hợp có xác suất tích lũy hàng đầu, nâng cao chất lượng văn bản tạo ra.
- Sử dụng `frequency_penalty` để giảm sự lặp lại và khuyến khích đa dạng trong đầu ra.
- Sử dụng `user_preferences` để cho phép tùy chỉnh các tham số sampling dựa trên mức độ sáng tạo và đa dạng do người dùng định nghĩa.
- Sử dụng `task_type` để xác định chiến lược sampling phù hợp cho yêu cầu, cho phép phản hồi được cá nhân hóa dựa trên tính chất của tác vụ.
- Sử dụng phương thức `send_request` để gửi prompt với các tham số sampling đã cấu hình, đảm bảo mô hình tạo văn bản theo yêu cầu.
- Sử dụng `generated_text` để lấy phản hồi của mô hình, sau đó trả về cùng với các tham số sampling và loại tác vụ để phân tích hoặc hiển thị.
- Sử dụng các hàm `min` và `max` để đảm bảo sở thích người dùng nằm trong phạm vi hợp lệ, tránh cấu hình sampling không hợp lệ.

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

Trong đoạn mã trên, chúng ta đã:

- Tạo lớp `AdaptiveSamplingManager` quản lý sampling động dựa trên loại tác vụ và sở thích người dùng.
- Định nghĩa các cấu hình sampling cho các loại tác vụ khác nhau (sáng tạo, thực tế, mã, hội thoại).
- Triển khai phương pháp phát hiện loại tác vụ từ prompt bằng các quy tắc đơn giản.
- Tính toán các tham số sampling dựa trên loại tác vụ được phát hiện và sở thích người dùng.
- Áp dụng các điều chỉnh học được dựa trên hiệu suất lịch sử để tối ưu hóa các tham số sampling.
- Ghi lại hiệu suất để điều chỉnh trong tương lai, cho phép hệ thống học hỏi từ các tương tác trước.
- Gửi các yêu cầu với tham số sampling được cấu hình động và trả về văn bản tạo cùng với các tham số áp dụng và loại tác vụ được phát hiện.
- Sử dụng:
    - `userPreferences` để cho phép tùy chỉnh các tham số sampling dựa trên mức độ sáng tạo, chính xác và nhất quán do người dùng định nghĩa.
    - `detectTaskType` để xác định bản chất của tác vụ dựa trên prompt, cho phép phản hồi được cá nhân hóa hơn.
    - `recordPerformance` để ghi lại hiệu suất của các phản hồi tạo ra, giúp hệ thống thích nghi và cải thiện theo thời gian.
    - `applyLearnedAdjustments` để điều chỉnh các tham số sampling dựa trên hiệu suất lịch sử, nâng cao khả năng tạo phản hồi chất lượng cao của mô hình.
    - `generateResponse` để bao gói toàn bộ quá trình tạo phản hồi với sampling thích ứng, giúp dễ dàng gọi với các prompt và ngữ cảnh khác nhau.
    - `allowedTools` để chỉ định các công cụ mà mô hình có thể sử dụng trong quá trình tạo, cho phép phản hồi phù hợp với ngữ cảnh hơn.
    - `feedbackScore` để người dùng có thể đánh giá chất lượng phản hồi tạo ra, từ đó cải thiện hiệu suất mô hình theo thời gian.
    - `performanceHistory` để lưu trữ các tương tác trước đó, giúp hệ thống học hỏi từ thành công và thất bại.
    - `getSamplingParameters` để điều chỉnh tham số sampling một cách linh hoạt dựa trên ngữ cảnh yêu cầu, cho phép mô hình hoạt động linh hoạt và phản ứng tốt hơn.
    - `detectTaskType` để phân loại tác vụ dựa trên prompt, giúp áp dụng các chiến lược sampling phù hợp cho từng loại yêu cầu.
    - `samplingProfiles` để định nghĩa các cấu hình sampling cơ bản cho các loại tác vụ khác nhau, cho phép điều chỉnh nhanh chóng dựa trên tính chất yêu cầu.

---

## Tiếp theo là gì

- [5.7 Scaling](../mcp-scaling/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.