> [!WARNING]
> Sampling bị loại bỏ trong MCP `2026-07-28`. Bài học này được giữ lại cho
> các triển khai kế thừa. Các máy chủ mới nên tích hợp trực tiếp với API nhà cung cấp LLM.


# Sampling trong Giao thức Ngữ cảnh Mô hình

> Sampling vẫn tồn tại trong đặc tả `2026-07-28` để tương thích và có thể
> bị loại bỏ trong lần sửa đổi đầu tiên được phát hành vào hoặc sau ngày 28 tháng 7,
> 2027. Các ví dụ trong bài học này có thể sử dụng các API SDK thực hiện `2025-11-25`.
> Xem [Có gì thay đổi trong MCP: Đặc tả 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

Trong các triển khai MCP kế thừa, Sampling cho phép máy chủ yêu cầu các hoàn thành LLM
thông qua client. Bài học này giải thích luồng giao thức đã bị loại bỏ đó
để tương thích và phục vụ công việc di trú.

## Giới thiệu

Trong bài học này, chúng ta sẽ khám phá cách cấu hình các tham số sampling trong các yêu cầu MCP và hiểu các cơ chế giao thức nền tảng của sampling.

## Mục tiêu học tập

Sau bài học này, bạn sẽ có thể:

- Hiểu các tham số sampling chính có trong MCP.
- Cấu hình các tham số sampling cho các trường hợp sử dụng khác nhau.
- Triển khai sampling xác định để có kết quả lặp lại được.
- Điều chỉnh động các tham số sampling dựa trên ngữ cảnh và sở thích người dùng.
- Áp dụng các chiến lược sampling để nâng cao hiệu suất mô hình trong các kịch bản khác nhau.
- Hiểu cách hoạt động của sampling trong luồng client-server của MCP.

## Cách Sampling Hoạt động trong MCP

Luồng sampling trong MCP theo các bước sau:

1. Máy chủ gửi yêu cầu `sampling/createMessage` đến client
2. Client xem xét yêu cầu và có thể chỉnh sửa nó
3. Client thực hiện sampling từ một LLM
4. Client xem lại kết quả hoàn thành
5. Client trả kết quả về cho máy chủ

Thiết kế có người kiểm soát trong vòng lặp này đảm bảo người dùng giữ quyền kiểm soát những gì LLM nhìn thấy và tạo ra.

## Tổng quan các Tham số Sampling

MCP định nghĩa các tham số sampling có thể cấu hình trong các yêu cầu của client như sau:

| Tham số | Mô tả | Phạm vi điển hình |
|-----------|-------------|---------------|
| `temperature` | Điều khiển tính ngẫu nhiên trong chọn token | 0.0 - 1.0 |
| `maxTokens` | Số lượng token tối đa được tạo ra | Giá trị nguyên |
| `stopSequences` | Các chuỗi tùy chỉnh dừng tạo khi gặp | Mảng các chuỗi |
| `metadata` | Các tham số riêng nhà cung cấp bổ sung | Đối tượng JSON |

Nhiều nhà cung cấp LLM hỗ trợ các tham số bổ sung thông qua trường `metadata`, có thể bao gồm:

| Tham số Mở rộng Thông dụng | Mô tả | Phạm vi điển hình |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - giới hạn token vào xác suất tích lũy hàng đầu | 0.0 - 1.0 |
| `top_k` | Giới hạn chọn token trong top K lựa chọn | 1 - 100 |
| `presence_penalty` | Phạt token dựa trên sự xuất hiện của chúng trong văn bản đã có | -2.0 - 2.0 |
| `frequency_penalty` | Phạt token dựa trên tần suất xuất hiện trong văn bản đã có | -2.0 - 2.0 |
| `seed` | Hạt giống ngẫu nhiên cụ thể để tái tạo kết quả | Giá trị nguyên |

## Ví dụ Định dạng Yêu cầu

Đây là ví dụ yêu cầu sampling từ một client trong MCP:

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

## Định dạng Phản hồi

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

## Điều khiển Người dùng trong Vòng lặp

Sampling trong MCP được thiết kế với sự giám sát của con người:

- **Đối với các lời nhắc**:
  - Client nên hiển thị lời nhắc đề xuất cho người dùng
  - Người dùng nên có khả năng chỉnh sửa hoặc từ chối các lời nhắc
  - Các lời nhắc hệ thống có thể được lọc hoặc chỉnh sửa
  - Việc bao gồm ngữ cảnh được kiểm soát bởi client

- **Đối với các kết quả hoàn thành**:
  - Client nên hiển thị kết quả hoàn thành cho người dùng
  - Người dùng nên có khả năng chỉnh sửa hoặc từ chối các kết quả hoàn thành
  - Client có thể lọc hoặc chỉnh sửa các kết quả hoàn thành
  - Người dùng kiểm soát việc lựa chọn mô hình sử dụng

Với những nguyên tắc này, chúng ta cùng xem cách triển khai sampling trong các ngôn ngữ lập trình khác nhau, tập trung vào các tham số được hỗ trợ phổ biến bởi các nhà cung cấp LLM.

## Các Lưu ý về Bảo mật

Khi triển khai sampling trong MCP, hãy cân nhắc các thực hành bảo mật tốt sau:

- **Xác thực mọi nội dung thông điệp** trước khi gửi tới client
- **Khử thông tin nhạy cảm** khỏi các lời nhắc và kết quả hoàn thành
- **Áp dụng giới hạn tần suất** để ngăn chặn lạm dụng
- **Giám sát sử dụng sampling** để phát hiện các mẫu bất thường
- **Mã hóa dữ liệu khi truyền tải** bằng các giao thức bảo mật
- **Xử lý quyền riêng tư dữ liệu người dùng** theo các quy định liên quan
- **Kiểm toán các yêu cầu sampling** để đảm bảo tuân thủ và bảo mật
- **Kiểm soát chi phí** với các giới hạn phù hợp
- **Thiết lập thời gian chờ** cho các yêu cầu sampling
- **Xử lý lỗi mô hình một cách mềm dẻo** với các phương án dự phòng thỏa đáng

Các tham số sampling cho phép tinh chỉnh hành vi của các mô hình ngôn ngữ để đạt được sự cân bằng mong muốn giữa các kết quả xác định và sáng tạo.

Hãy xem cách cấu hình các tham số này trong các ngôn ngữ lập trình khác nhau.

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

Trong đoạn mã trước, chúng tôi đã:

- Tạo một client MCP với URL máy chủ cụ thể.
- Cấu hình một yêu cầu với các tham số sampling như `temperature`, `top_p`, và `top_k`.
- Gửi yêu cầu và in văn bản tạo ra.
- Đã sử dụng:
    - `allowedTools` để chỉ định những công cụ mô hình có thể sử dụng trong quá trình tạo. Trong trường hợp này, chúng tôi cho phép công cụ `ideaGenerator` và `marketAnalyzer` hỗ trợ tạo ý tưởng ứng dụng sáng tạo.
    - `frequencyPenalty` và `presencePenalty` để kiểm soát sự lặp lại và đa dạng trong đầu ra.
    - `temperature` để điều khiển tính ngẫu nhiên của đầu ra, giá trị cao hơn dẫn đến các phản hồi sáng tạo hơn.
    - `top_p` để giới hạn lựa chọn token vào các token đóng góp vào khối xác suất tích lũy hàng đầu, nâng cao chất lượng văn bản tạo ra.
    - `top_k` để hạn chế mô hình chỉ chọn trong top K token có xác suất cao nhất, giúp tạo các phản hồi mạch lạc hơn.
    - `frequencyPenalty` và `presencePenalty` để giảm lặp lại và khuyến khích đa dạng trong văn bản tạo ra.

# [JavaScript](#tab/javascript)

```javascript
// Ví dụ JavaScript: Cấu hình nhiệt độ và lấy mẫu Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Khởi tạo khách hàng MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Cấu hình yêu cầu với các tham số lấy mẫu khác nhau
  const creativeSampling = {
    temperature: 0.9,    // Nhiệt độ cao hơn = ngẫu nhiên/sáng tạo hơn
    topP: 0.92,          // Xem xét các token với khối lượng xác suất top 92%
    frequencyPenalty: 0.6, // Giảm lặp lại các chuỗi token
    presencePenalty: 0.4   // Trừng phạt các token đã xuất hiện trong văn bản đến nay
  };
  
  const factualSampling = {
    temperature: 0.2,    // Nhiệt độ thấp hơn = xác định/chính xác hơn
    topP: 0.85,          // Lựa chọn token tập trung hơn một chút
    frequencyPenalty: 0.2, // Trừng phạt lặp lại tối thiểu
    presencePenalty: 0.1   // Trừng phạt sự xuất hiện tối thiểu
  };
  
  try {
    // Gửi hai yêu cầu với các cấu hình lấy mẫu khác nhau
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

Trong đoạn mã trước, chúng tôi đã:

- Khởi tạo một client MCP với URL máy chủ và khóa API.
- Cấu hình hai bộ tham số sampling: một cho nhiệm vụ sáng tạo và một cho nhiệm vụ chính xác.
- Gửi các yêu cầu với cấu hình này, cho phép mô hình sử dụng công cụ cụ thể cho từng nhiệm vụ.
- In các phản hồi tạo ra để minh họa ảnh hưởng của các tham số sampling khác nhau.
- Đã sử dụng `allowedTools` để chỉ định các công cụ mà mô hình có thể sử dụng trong quãng trình tạo. Trong trường hợp này, chúng tôi cho phép công cụ `ideaGenerator` và `environmentalImpactTool` cho các nhiệm vụ sáng tạo, và `factChecker` và `dataAnalysisTool` cho các nhiệm vụ thực tế.
- Đã sử dụng `temperature` để điều khiển tính ngẫu nhiên của đầu ra, giá trị cao hơn dẫn đến các phản hồi sáng tạo hơn.

- Đã sử dụng `top_p` để giới hạn việc lựa chọn các token vào những token góp phần vào xác suất tích lũy hàng đầu, nâng cao chất lượng văn bản được tạo ra.
- Đã sử dụng `frequencyPenalty` và `presencePenalty` để giảm sự lặp lại và khuyến khích sự đa dạng trong kết quả.
- Đã sử dụng `top_k` để giới hạn mô hình chỉ ở trên K token có xác suất cao nhất, giúp tạo ra các phản hồi mạch lạc hơn.

---

## Lấy mẫu xác định

Đối với các ứng dụng cần đầu ra nhất quán, lấy mẫu xác định đảm bảo kết quả có thể tái tạo. Cách thực hiện là sử dụng hạt ngẫu nhiên cố định và đặt nhiệt độ bằng 0.

Hãy cùng xem ví dụ triển khai dưới đây để minh họa lấy mẫu xác định trong các ngôn ngữ lập trình khác nhau.

# [Java](#tab/java)

```java
// Ví dụ Java: Phản hồi xác định với hạt giống cố định
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Sử dụng hạt giống cố định để có kết quả xác định
        
        // Yêu cầu đầu tiên với hạt giống cố định
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Nhiệt độ bằng không để có độ xác định tối đa
            .build();
            
        // Yêu cầu thứ hai với cùng hạt giống
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Thực thi cả hai yêu cầu
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Phản hồi nên giống hệt nhau do cùng hạt giống và nhiệt độ=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Trong đoạn mã phía trên chúng ta đã:

- Tạo một client MCP với URL máy chủ được chỉ định.
- Cấu hình hai yêu cầu với cùng một prompt, hạt cố định và nhiệt độ bằng 0.
- Gửi cả hai yêu cầu và in ra văn bản được tạo ra.
- Minh họa rằng các phản hồi giống hệt nhau do tính chất xác định của cấu hình lấy mẫu (cùng hạt và nhiệt độ).
- Dùng `setSeed` để chỉ định hạt ngẫu nhiên cố định, đảm bảo mô hình luôn tạo ra cùng một đầu ra cho cùng một đầu vào.
- Đặt `temperature` bằng 0 để đảm bảo tính xác định tối đa, nghĩa là mô hình sẽ luôn chọn token kế tiếp có xác suất cao nhất mà không có yếu tố ngẫu nhiên.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Ví dụ JavaScript: Các phản hồi xác định với việc kiểm soát seed
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Yêu cầu đầu tiên với seed cố định
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Nhiệt độ bằng 0 để có tính xác định tối đa
    });
    
    // Yêu cầu thứ hai với cùng seed và nhiệt độ
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Yêu cầu thứ ba với seed khác nhưng cùng nhiệt độ
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

Trong đoạn mã phía trên chúng ta đã:

- Khởi tạo một client MCP với URL máy chủ.
- Cấu hình hai yêu cầu với cùng một prompt, hạt cố định và nhiệt độ bằng 0.
- Gửi cả hai yêu cầu và in ra văn bản được tạo ra.
- Minh họa rằng các phản hồi giống hệt nhau do tính chất xác định của cấu hình lấy mẫu (cùng hạt và nhiệt độ).
- Dùng `seed` để chỉ định hạt ngẫu nhiên cố định, đảm bảo mô hình luôn tạo ra cùng một đầu ra cho cùng một đầu vào.
- Đặt `temperature` bằng 0 để đảm bảo tính xác định tối đa, nghĩa là mô hình sẽ luôn chọn token kế tiếp có xác suất cao nhất mà không có yếu tố ngẫu nhiên.
- Dùng một hạt khác cho yêu cầu thứ ba để minh họa rằng thay đổi hạt sẽ tạo ra đầu ra khác, dù cùng prompt và nhiệt độ.

---

## Cấu hình lấy mẫu động

Lấy mẫu thông minh điều chỉnh các tham số dựa trên ngữ cảnh và yêu cầu của từng yêu cầu. Điều này có nghĩa là điều chỉnh động các tham số như nhiệt độ, top_p và các hình phạt dựa trên loại tác vụ, sở thích người dùng hoặc hiệu suất lịch sử.

Hãy xem cách triển khai lấy mẫu động trong các ngôn ngữ lập trình khác nhau.

# [Python](#tab/python)

```python
# Ví dụ Python: Lấy mẫu động dựa trên ngữ cảnh yêu cầu
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Định nghĩa các mẫu lấy mẫu trước cho các loại nhiệm vụ khác nhau
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Chọn mẫu lấy mẫu cơ sở
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Điều chỉnh dựa trên sở thích người dùng nếu được cung cấp
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Điều chỉnh nhiệt độ dựa trên sở thích sáng tạo (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Điều chỉnh top_p dựa trên sự đa dạng phản hồi mong muốn
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Tạo và gửi yêu cầu với các tham số lấy mẫu tùy chỉnh
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Trả về phản hồi với metadata lấy mẫu để minh bạch
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Trong đoạn mã phía trên chúng ta đã:

- Tạo một lớp `DynamicSamplingService` quản lý lấy mẫu thích ứng.
- Định nghĩa các cấu hình lấy mẫu mặc định cho các loại tác vụ khác nhau (sáng tạo, thực tế, mã, phân tích).
- Lựa chọn cấu hình lấy mẫu cơ sở dựa trên loại tác vụ.
- Điều chỉnh các tham số lấy mẫu dựa trên sở thích người dùng, như mức độ sáng tạo và đa dạng.
- Gửi yêu cầu với các tham số lấy mẫu được cấu hình động.
- Trả về văn bản được tạo ra cùng với tham số lấy mẫu và loại tác vụ để minh bạch.
- Dùng `temperature` để điều khiển độ ngẫu nhiên của đầu ra, trong đó giá trị cao hơn dẫn đến các phản hồi sáng tạo hơn.
- Dùng `top_p` để giới hạn việc lựa chọn token vào các token góp phần vào xác suất tích lũy hàng đầu, nâng cao chất lượng văn bản được tạo ra.
- Dùng `frequency_penalty` để giảm sự lặp lại và khuyến khích sự đa dạng trong kết quả.
- Dùng `user_preferences` cho phép tùy chỉnh các tham số lấy mẫu dựa trên mức độ sáng tạo và đa dạng do người dùng định nghĩa.
- Dùng `task_type` để xác định chiến lược lấy mẫu phù hợp cho yêu cầu, cho phép phản hồi được tùy biến hơn dựa trên bản chất của tác vụ.
- Dùng phương thức `send_request` để gửi prompt với các tham số lấy mẫu đã cấu hình, đảm bảo mô hình tạo ra văn bản theo yêu cầu đã chỉ định.
- Dùng `generated_text` để lấy phản hồi của mô hình, sau đó trả về cùng với tham số lấy mẫu và loại tác vụ để phân tích hoặc hiển thị thêm.
- Dùng các hàm `min` và `max` để đảm bảo sở thích người dùng được giới hạn trong khoảng hợp lệ, tránh các cấu hình lấy mẫu không hợp lệ.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// Ví dụ JavaScript: Cấu hình lấy mẫu động dựa trên ngữ cảnh người dùng
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Định nghĩa các hồ sơ lấy mẫu cơ bản
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Theo dõi hiệu suất lịch sử
    this.performanceHistory = [];
  }
  
  // Phát hiện loại tác vụ từ lời nhắc
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Phát hiện theo heuristics đơn giản - có thể cải tiến bằng phân loại ML
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
    
    // Mặc định là giao tiếp nếu không phát hiện được loại rõ ràng
    return 'conversational';
  }
  
  // Tính toán tham số lấy mẫu dựa trên ngữ cảnh và sở thích người dùng
  getSamplingParameters(prompt, context = {}) {
    // Phát hiện loại tác vụ
    const taskType = this.detectTaskType(prompt, context);
    
    // Lấy hồ sơ cơ bản
    let params = {...this.samplingProfiles[taskType]};
    
    // Điều chỉnh dựa trên sở thích người dùng
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Chuyển đổi từ thang 1-10 sang phạm vi nhiệt độ phù hợp
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Độ chính xác cao hơn nghĩa là topP thấp hơn (lựa chọn tập trung hơn)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Độ nhất quán cao hơn nghĩa là mức phạt thấp hơn
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Áp dụng điều chỉnh học được từ lịch sử hiệu suất
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Logic thích nghi đơn giản - có thể được cải thiện bằng các thuật toán tinh vi hơn
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Chỉ xem xét lịch sử gần đây
    
    if (relevantHistory.length > 0) {
      // Tính điểm hiệu suất trung bình
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Nếu hiệu suất dưới ngưỡng, điều chỉnh tham số
      if (avgScore < 0.7) {
        // Điều chỉnh nhẹ hướng đến các giá trị an toàn hơn
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Ghi lại hiệu suất để điều chỉnh trong tương lai
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Đánh giá chất lượng phản hồi từ 0-1
    });
    
    // Giới hạn kích thước lịch sử
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Lấy tham số lấy mẫu tối ưu
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Gửi yêu cầu với tham số tối ưu
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Nếu người dùng cung cấp phản hồi, ghi lại để tối ưu hóa sau này
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

// Ví dụ sử dụng
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Tác vụ sáng tạo với sở thích người dùng tùy chỉnh
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Sáng tạo cao (1-10)
          consistency: 3  // Độ nhất quán thấp (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Tác vụ tạo mã
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Sáng tạo thấp
          precision: 8,   // Độ chính xác cao
          consistency: 9  // Độ nhất quán cao
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

Trong đoạn mã phía trên chúng ta đã:

- Tạo một lớp `AdaptiveSamplingManager` quản lý lấy mẫu động dựa trên loại tác vụ và sở thích người dùng.
- Định nghĩa các hồ sơ lấy mẫu cho các loại tác vụ khác nhau (sáng tạo, thực tế, mã, hội thoại).
- Triển khai phương pháp phát hiện loại tác vụ từ prompt sử dụng các heuristic đơn giản.
- Tính toán tham số lấy mẫu dựa trên loại tác vụ được phát hiện và sở thích người dùng.
- Áp dụng các điều chỉnh học được dựa trên hiệu suất lịch sử để tối ưu hóa tham số lấy mẫu.
- Ghi lại hiệu suất để điều chỉnh trong tương lai, cho phép hệ thống học hỏi từ các tương tác trước.
- Gửi yêu cầu với các tham số lấy mẫu được cấu hình động và trả về văn bản tạo ra cùng với tham số áp dụng và loại tác vụ được phát hiện.
- Đã dùng:
    - `userPreferences` cho phép tùy chỉnh tham số lấy mẫu dựa trên mức độ sáng tạo, chính xác, và nhất quán do người dùng định nghĩa.
    - `detectTaskType` để xác định bản chất của tác vụ dựa trên prompt, cho phép phản hồi được tùy chỉnh hơn.
    - `recordPerformance` để ghi lại hiệu suất của các phản hồi tạo ra, giúp hệ thống thích ứng và cải thiện theo thời gian.
    - `applyLearnedAdjustments` để sửa đổi tham số lấy mẫu dựa trên hiệu suất lịch sử, nâng cao khả năng tạo phản hồi chất lượng cao của mô hình.
    - `generateResponse` để đóng gói toàn bộ quy trình tạo phản hồi với lấy mẫu thích ứng, giúp dễ dàng gọi với các prompt và ngữ cảnh khác nhau.
    - `allowedTools` để xác định công cụ mà mô hình có thể sử dụng trong quá trình tạo phản hồi, cho phép phản hồi phù hợp hơn với ngữ cảnh.
    - `feedbackScore` để người dùng có thể phản hồi về chất lượng phản hồi được tạo, sử dụng để cải thiện hiệu suất mô hình theo thời gian.
    - `performanceHistory` để duy trì hồ sơ các tương tác trước đây, cho phép hệ thống học hỏi từ thành công và thất bại trước đó.
    - `getSamplingParameters` để điều chỉnh tham số lấy mẫu động dựa trên ngữ cảnh yêu cầu, cho phép mô hình hoạt động linh hoạt và phản ứng tốt hơn.
    - `detectTaskType` để phân loại tác vụ dựa trên prompt, cho phép hệ thống áp dụng các chiến lược lấy mẫu phù hợp cho từng loại yêu cầu.
    - `samplingProfiles` để định nghĩa các cấu hình lấy mẫu cơ bản cho các loại tác vụ khác nhau, giúp điều chỉnh nhanh chóng dựa trên bản chất của yêu cầu.

---

## Tiếp theo là gì

- [5.7 Mở rộng quy mô](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->