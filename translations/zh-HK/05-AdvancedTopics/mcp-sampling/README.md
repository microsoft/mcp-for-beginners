> [!WARNING]
> MCP `2026-07-28` 版本中取樣已被棄用。本課程為保留遺留實作而設。新服務器應直接與 LLM 提供者 API 整合。
> New servers should integrate directly with an LLM
> provider API.

# 模型上下文協定中的取樣

> 取樣在 `2026-07-28` 規範中仍存在以保持相容性，並可於2027年7月28日或之後發布的第一次修訂中移除。本課程中的範例可能使用實作 `2025-11-25` 的 SDK API。詳見 [MCP 變更說明：2026-07-28 規範](../../01-CoreConcepts/mcp-2026-07-28.md).
> eligible for removal in the first revision released on or after July 28,
> 2027. Examples in this lesson may use SDK APIs that implement `2025-11-25`.
> See [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md).

在舊版 MCP 實作中，取樣允許伺服器透過客戶端請求 LLM 補全文字。此課程說明該已棄用協定流程以利相容與遷移工作。
completions through the client. This lesson explains that deprecated protocol
flow for compatibility and migration work.

## 簡介

本課程將探討如何在 MCP 請求中設定取樣參數，並理解取樣背後的協定機制。

## 學習目標

完成本課程後，您將能夠：

- 了解 MCP 中可用的主要取樣參數。
- 為不同使用情境設定取樣參數。
- 實作確定性取樣以獲得可重現結果。
- 根據上下文與用戶偏好動態調整取樣參數。
- 應用取樣策略提升模型在多種場景中的效能。
- 了解取樣在 MCP 客戶端-伺服器流程中的運作方式。

## MCP 中取樣的運作方式

MCP 的取樣流程包含以下步驟：

1. 伺服器發送 `sampling/createMessage` 請求至客戶端
2. 客戶端審核請求並可進行修改
3. 客戶端從 LLM 取樣
4. 客戶端審核補全文字
5. 客戶端將結果回傳給伺服器

此人機互動設計確保用戶掌控 LLM 見到及生成的內容。

## 取樣參數概覽

MCP 定義可在客戶端請求中設定的取樣參數如下：

| 參數 | 說明 | 典型範圍 |
|-----------|-------------|---------------|
| `temperature` | 控制選詞隨機程度 | 0.0 - 1.0 |
| `maxTokens` | 生成詞元的最大數量 | 整數值 |
| `stopSequences` | 遇到這些自訂序列時停止生成 | 字串陣列 |
| `metadata` | 提供者特定的額外參數 | JSON 物件 |

許多 LLM 提供者透過 `metadata` 欄位支援其他參數，可能包括：

| 常見擴充參數 | 說明 | 典型範圍 |
|-----------|-------------|---------------|
| `top_p` | 核心取樣 - 限制詞元於最高累積機率之內 | 0.0 - 1.0 |
| `top_k` | 限制詞元選擇於前 K 名內 | 1 - 100 |
| `presence_penalty` | 根據詞元在文本中出現最多審核 | -2.0 - 2.0 |
| `frequency_penalty` | 根據詞元在文本中出現頻率懲罰 | -2.0 - 2.0 |
| `seed` | 特定隨機種子以產生可重現結果 | 整數值 |

## 範例請求格式

以下為 MCP 中客戶端請求取樣的範例：

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

## 回應格式

客戶端回傳補全文字結果：

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

## 人機互動控制

MCP 取樣設計考量到人類監督：


- <strong>針對提示詞</strong>：
  - 用戶端應向使用者顯示建議的提示詞
  - 使用者應能夠修改或拒絕提示詞
  - 系統提示詞可以被過濾或修改
  - 上下文的包含由用戶端控制

- <strong>針對完成結果</strong>：
  - 用戶端應向使用者顯示完成結果
  - 使用者應能夠修改或拒絕完成結果
  - 用戶端可以過濾或修改完成結果
  - 使用者控制使用哪個模型

本著這些原則，我們來看看如何在不同程式語言中實作取樣，並聚焦於各大大型語言模型供應商普遍支援的參數。

## 安全性考量

在 MCP 中實作取樣時，請考慮以下安全最佳實踐：

- <strong>驗證所有訊息內容</strong>，再發送給用戶端
- <strong>從提示詞及完成結果中清理敏感資訊</strong>
- <strong>實作速率限制</strong>以防止濫用
- <strong>監控取樣使用情況</strong>以偵測異常模式
- <strong>使用安全協定加密傳輸資料</strong>
- <strong>依相關規範處理使用者資料隱私</strong>
- <strong>稽核取樣請求</strong>以符合合規與安全要求
- <strong>透過適當限制控制成本暴露</strong>
- <strong>為取樣請求實作逾時機制</strong>
- <strong>優雅處理模型錯誤</strong>並採用適當的備援策略

取樣參數能微調語言模型的行為，以達成決定性與創意性輸出之間的理想平衡。

接著我們來看看如何在不同程式語言中設定這些參數。

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

在前述程式碼中，我們已經：

- 建立了一個 MCP 用戶端並指定伺服器 URL。
- 配置了一個請求，包含取樣參數如 `temperature`、`top_p` 與 `top_k`。
- 發送請求並列印生成的文字。
- 使用了：
    - `allowedTools` 指定模型在生成過程中可使用的工具。這裡允許了 `ideaGenerator` 與 `marketAnalyzer` 工具協助產生創意應用程式點子。
    - `frequencyPenalty` 與 `presencePenalty` 控制輸出的重複與多樣性。
    - `temperature` 控制輸出隨機度，值越高響應越具創意。
    - `top_p` 限制選擇的詞元累積機率，提升生成文本質量。
    - `top_k` 限制模型只選擇機率最高的 K 個詞元，有助於生成更連貫的回答。
    - `frequencyPenalty` 與 `presencePenalty` 用於減少重複並增加生成文本的多樣性。

# [JavaScript](#tab/javascript)

```javascript
// JavaScript 範例：溫度與 Top-P 取樣設定
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // 初始化 MCP 用戶端
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // 配置帶有不同取樣參數的請求
  const creativeSampling = {
    temperature: 0.9,    // 溫度越高 = 隨機性／創意越多
    topP: 0.92,          // 考慮累積機率質量達到 92% 的標記
    frequencyPenalty: 0.6, // 減少標記序列重複
    presencePenalty: 0.4   // 懲罰迄今文本中已出現的標記
  };
  
  const factualSampling = {
    temperature: 0.2,    // 溫度越低 = 趨向決定性／事實性
    topP: 0.85,          // 稍微更專注的標記選擇
    frequencyPenalty: 0.2, // 最小重複懲罰
    presencePenalty: 0.1   // 最小出現懲罰
  };
  
  try {
    // 用不同取樣配置送出兩個請求
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

在前述程式碼中，我們已經：

- 使用伺服器 URL 和 API 金鑰初始化 MCP 用戶端。
- 配置了兩套取樣參數，一套用於創意任務，另一套用於事實任務。
- 發送帶有這些配置的請求，允許模型為每個任務使用特定工具。
- 列印生成的回應，展示不同取樣參數的效果。
- 使用 `allowedTools` 指定模型在生成過程可使用的工具。這裡為創意任務允許了 `ideaGenerator` 和 `environmentalImpactTool`，為事實任務則允許了 `factChecker` 和 `dataAnalysisTool`。
- 使用 `temperature` 控制輸出隨機度，數值越高輸出越具創意。

- 使用了 `top_p` 限制選擇的 token 僅包含對累積機率質量頂端貢獻的部分，提升生成文本的質量。
- 使用了 `frequencyPenalty` 和 `presencePenalty` 以減少重複並鼓勵輸出多樣性。
- 使用了 `top_k` 限制模型僅從概率最高的 K 個 token 中選擇，有助生成更連貫的回應。

---

## 決定性取樣

對於需要一致輸出的應用，決定性取樣確保結果可重現。其作法是使用固定的隨機種子並將溫度設為零。

下面讓我們看看不同程式語言中的決定性取樣範例實作。

# [Java](#tab/java)

```java
// Java 範例：使用固定種子獲得確定性回應
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // 使用固定種子以獲得確定性結果
        
        // 第一次使用固定種子發送請求
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // 溫度設為零以達到最大確定性
            .build();
            
        // 第二次使用相同種子發送請求
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // 執行兩個請求
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // 由於使用相同種子且溫度為0，回應應該相同
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

在前述程式碼中我們：

- 建立了一個 MCP 客戶端並指定伺服器 URL。
- 配置了兩個使用相同提示詞、固定種子及溫度為零的請求。
- 發送兩個請求並印出生成的文本。
- 展示因為取樣配置的決定性（相同種子與溫度）而使回應相同。
- 使用 `setSeed` 設定固定隨機種子，確保模型對相同輸入每次輸出相同結果。
- 將 `temperature` 設為零以確保最大決定性，也就是模型總是選擇最高機率的下一個 token，沒有隨機性。

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript 範例：使用種子控制實現確定性回應
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // 第一個請求，使用固定種子
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // 零溫度以達到最大確定性
    });
    
    // 第二個請求，使用相同的種子和溫度
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // 第三個請求，使用不同的種子但相同的溫度
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

在前述程式碼中我們：

- 初始化 MCP 客戶端並指定伺服器 URL。
- 配置了兩個使用相同提示詞、固定種子及溫度為零的請求。
- 發送兩個請求並印出生成的文本。
- 展示取樣配置的決定性特性（相同種子和溫度）令回應一致。
- 使用 `seed` 指定固定隨機種子，確保模型對相同輸入每次輸出相同結果。
- 將 `temperature` 設為零以確保最大決定性，模型總是採用最高機率的下一個 token。
- 為第三個請求使用不同種子，顯示即使提示詞和溫度相同，變更種子會產生不同輸出。

---

## 動態取樣配置

智能取樣會根據每個請求的上下文和需求調整參數，動態調整如溫度、top_p 和懲罰等，根據任務類型、用戶偏好或歷史表現。

讓我們看看如何在不同程式語言中實現動態取樣。

# [Python](#tab/python)

```python
# Python 範例：基於請求上下文的動態取樣
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # 定義不同任務類型的取樣預設值
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # 選擇基本預設
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # 如有提供，根據用戶偏好調整
        if user_preferences:
            if "creativity_level" in user_preferences:
                # 根據創意偏好（1-10）調整溫度參數
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # 根據期望的回應多樣性調整 top_p
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # 建立並送出帶有自訂取樣參數的請求
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # 回傳帶有取樣元資料的回應以保持透明度
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

在前述程式碼中我們：

- 創建了 `DynamicSamplingService` 類別管理自適應取樣。
- 為不同任務類型（創意、事實、程式碼、分析）定義取樣預設。
- 根據任務類型選擇基本取樣預設。
- 根據用戶偏好如創意度和多樣性調整取樣參數。
- 使用動態配置的取樣參數發送請求。
- 回傳生成文本，連同應用的取樣參數與任務類型以供透明化。
- 使用 `temperature` 控制輸出隨機性，數值越高回應越具創造力。
- 使用 `top_p` 限制 token 選擇在累積概率頂部，有助提升生成文本質量。
- 使用 `frequency_penalty` 減少重複並提倡多樣性。
- 使用 `user_preferences` 允許根據用戶定義的創意和多樣性層級自訂取樣參數。
- 使用 `task_type` 判斷適合的取樣策略，基於任務性質提供更加貼切的回應。
- 使用 `send_request` 方法帶著配置好的取樣參數送出提示詞，確保模型根據指定需求生成文字。
- 使用 `generated_text` 取得模型回覆，並連同取樣參數與任務類型一同回傳以便分析或展示。
- 使用 `min` 與 `max` 函式確保用戶偏好值限制在有效範圍，避免無效取樣配置。

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScript 範例：基於用戶上下文的動態採樣配置
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // 定義基本採樣配置檔
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // 跟蹤歷史性能
    this.performanceHistory = [];
  }
  
  // 從提示中檢測任務類型
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // 簡單的啟發式檢測 - 可通過機器學習分類進行增強
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
    
    // 若無明確類型則默認為對話型
    return 'conversational';
  }
  
  // 根據上下文及用戶偏好計算採樣參數
  getSamplingParameters(prompt, context = {}) {
    // 檢測任務類型
    const taskType = this.detectTaskType(prompt, context);
    
    // 獲取基本配置檔
    let params = {...this.samplingProfiles[taskType]};
    
    // 根據用戶偏好進行調整
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // 將1-10比例縮放到合適的溫度範圍
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // 較高精度意味著較低topP（更專注的選擇）
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // 較高一致性意味著較低懲罰
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // 應用從性能歷史中學習的調整
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // 簡單自適應邏輯 - 可用更複雜的算法增強
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // 僅考慮近期歷史
    
    if (relevantHistory.length > 0) {
      // 計算平均性能分數
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // 如果性能低於閾值，調整參數
      if (avgScore < 0.7) {
        // 朝向更安全值的小幅調整
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // 記錄性能以供日後調整
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 0-1 的回應質量評分
    });
    
    // 限制歷史大小
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // 獲取優化後的採樣參數
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // 使用優化參數發送請求
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // 如果用戶提供反饋，記錄以便未來優化
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

// 範例用法
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // 創作任務和自訂用戶偏好
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // 高創意（1-10）
          consistency: 3  // 低一致性（1-10）
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // 程式碼生成任務
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // 低創意
          precision: 8,   // 高精度
          consistency: 9  // 高一致性
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

在前述程式碼中我們：

- 創建了 `AdaptiveSamplingManager` 類別管理基於任務類型及用戶偏好的動態取樣。
- 為不同任務類型（創意、事實、程式碼、對話）定義取樣配置檔。
- 實作簡單啟發式方法從提示詞偵測任務類型。
- 根據偵測出的任務類型及用戶偏好計算取樣參數。
- 根據歷史績效套用學習調整以優化取樣參數。
- 紀錄績效以供未來調整，讓系統能從過去互動學習。
- 使用動態配置的取樣參數發送請求，並回傳生成的文本、套用參數和偵測到的任務類型。
- 使用了：
    - `userPreferences` 允許根據用戶定義的創意、精確度和一致性層級自訂取樣參數。
    - `detectTaskType` 根據提示詞判定任務性質，以提供更貼切的回應。
    - `recordPerformance` 記錄生成回應的績效，使用系統能適應並持續優化。
    - `applyLearnedAdjustments` 根據歷史績效調整取樣參數，提升模型生成高品質回應能力。
    - `generateResponse` 封裝整個動態取樣生成流程，方便針對不同提示詞與上下文呼叫。
    - `allowedTools` 指定模型生成時可使用的工具，以提供更多上下文感知回應。
    - `feedbackScore` 允許用戶對生成回應質量提供反饋，可進一步優化模型表現。
    - `performanceHistory` 保存過往互動紀錄，使系統能從成功與失敗中學習。
    - `getSamplingParameters` 根據請求上下文動態調整取樣參數，使模型行為更靈活反應。
    - `detectTaskType` 根據提示詞分類任務，讓系統可套用適合不同請求的取樣策略。
    - `samplingProfiles` 定義各任務類型的基本取樣配置，方便依請求性質快速調整。

---

## 後續內容

- [5.7 擴充](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->