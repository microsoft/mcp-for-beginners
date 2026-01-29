# Sampling in Model Context Protocol

Samplingは、サーバーがクライアントを通じてLLMの補完をリクエストできる強力なMCP機能であり、高度なエージェント的動作を実現しつつ、セキュリティとプライバシーを維持します。適切なSampling設定は、応答の品質とパフォーマンスを大幅に向上させることができます。MCPは、ランダム性、創造性、一貫性に影響を与える特定のパラメータを使って、モデルのテキスト生成を制御する標準化された方法を提供します。

## はじめに

このレッスンでは、MCPリクエストにおけるSamplingパラメータの設定方法と、Samplingのプロトコルの仕組みについて学びます。

## 学習目標

このレッスンの終了時には、以下ができるようになります：

- MCPで利用可能な主要なSamplingパラメータを理解する。
- さまざまなユースケースに応じたSamplingパラメータの設定。
- 再現可能な結果を得るための決定論的Samplingの実装。
- コンテキストやユーザーの好みに応じてSamplingパラメータを動的に調整する。
- さまざまなシナリオでモデルのパフォーマンスを向上させるSampling戦略の適用。
- MCPのクライアント-サーバーフローにおけるSamplingの動作理解。

## MCPにおけるSamplingの仕組み

MCPのSamplingフローは以下のステップで進みます：

1. サーバーがクライアントに`sampling/createMessage`リクエストを送信
2. クライアントがリクエストを確認し、必要に応じて修正
3. クライアントがLLMからサンプリングを実行
4. クライアントが補完結果を確認
5. クライアントが結果をサーバーに返却

このヒューマン・イン・ザ・ループ設計により、ユーザーはLLMが何を見て生成するかをコントロールできます。

## Samplingパラメータの概要

MCPはクライアントリクエストで設定可能な以下のSamplingパラメータを定義しています：

| パラメータ | 説明 | 一般的な範囲 |
|-----------|-------------|---------------|
| `temperature` | トークン選択のランダム性を制御 | 0.0 - 1.0 |
| `maxTokens` | 生成する最大トークン数 | 整数値 |
| `stopSequences` | 生成を停止するカスタムシーケンス | 文字列の配列 |
| `metadata` | プロバイダー固有の追加パラメータ | JSONオブジェクト |

多くのLLMプロバイダーは`metadata`フィールドを通じて以下のような追加パラメータをサポートしています：

| 一般的な拡張パラメータ | 説明 | 一般的な範囲 |
|-----------|-------------|---------------|
| `top_p` | ニュークリアスサンプリング - トークンを上位累積確率に制限 | 0.0 - 1.0 |
| `top_k` | トークン選択を上位K個に制限 | 1 - 100 |
| `presence_penalty` | これまでのテキストに出現したトークンをペナルティ | -2.0 - 2.0 |
| `frequency_penalty` | これまでのテキストでの頻度に基づくペナルティ | -2.0 - 2.0 |
| `seed` | 再現可能な結果のための特定の乱数シード | 整数値 |

## リクエスト例フォーマット

以下はMCPでクライアントにSamplingをリクエストする例です：

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

## レスポンスフォーマット

クライアントは補完結果を返します：

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

## ヒューマン・イン・ザ・ループ制御

MCPのSamplingは人間の監督を前提に設計されています：

- **プロンプトに関して**：
  - クライアントはユーザーに提案されたプロンプトを表示すべき
  - ユーザーはプロンプトを修正または拒否できるべき
  - システムプロンプトはフィルタリングや修正が可能
  - コンテキストの含有はクライアントが制御

- **補完に関して**：
  - クライアントはユーザーに補完結果を表示すべき
  - ユーザーは補完を修正または拒否できるべき
  - クライアントは補完をフィルタリングや修正可能
  - ユーザーが使用モデルを選択可能

これらの原則を踏まえ、LLMプロバイダー間で共通してサポートされるパラメータに焦点を当て、さまざまなプログラミング言語でのSampling実装方法を見ていきましょう。

## セキュリティ上の考慮点

MCPでSamplingを実装する際は、以下のセキュリティベストプラクティスを考慮してください：

- **メッセージ内容をすべて検証**してからクライアントに送信
- **プロンプトや補完から機密情報を除去**
- **悪用防止のためレート制限を実装**
- **異常なSampling使用パターンを監視**
- **安全なプロトコルで通信データを暗号化**
- **関連法規に従いユーザーデータのプライバシーを保護**
- **コンプライアンスとセキュリティのためSamplingリクエストを監査**
- **コスト管理のため適切な制限を設ける**
- **Samplingリクエストにタイムアウトを設定**
- **モデルエラーは適切なフォールバックで優雅に処理**

Samplingパラメータは、決定論的な出力と創造的な出力のバランスを調整するための微調整を可能にします。

次に、これらのパラメータをさまざまなプログラミング言語で設定する方法を見ていきましょう。

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

上記コードでは：

- 特定のサーバーURLでMCPクライアントを作成しました。
- `temperature`、`top_p`、`top_k`などのSamplingパラメータを設定したリクエストを構成しました。
- リクエストを送信し、生成されたテキストを出力しました。
- 以下を使用しました：
    - `allowedTools`で生成時にモデルが使用できるツールを指定。ここでは`ideaGenerator`と`marketAnalyzer`を許可し、創造的なアプリアイデアの生成を支援。
    - `frequencyPenalty`と`presencePenalty`で出力の繰り返しや多様性を制御。
    - `temperature`で出力のランダム性を制御。値が高いほど創造的な応答に。
    - `top_p`で累積確率の上位トークンに選択を制限し、生成テキストの質を向上。
    - `top_k`でモデルを上位K個の最も確率の高いトークンに制限し、一貫性のある応答を促進。
    - `frequencyPenalty`と`presencePenalty`で繰り返しを減らし、多様性を促進。

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

上記コードでは：

- サーバーURLとAPIキーでMCPクライアントを初期化しました。
- 創造的タスク用と事実ベースタスク用の2種類のSamplingパラメータセットを設定。
- それぞれの設定でリクエストを送信し、モデルが特定のツールを使用できるようにしました。
- 生成された応答を出力し、異なるSamplingパラメータの効果を示しました。
- `allowedTools`で生成時にモデルが使用できるツールを指定。創造的タスクには`ideaGenerator`と`environmentalImpactTool`、事実タスクには`factChecker`と`dataAnalysisTool`を許可。
- `temperature`で出力のランダム性を制御。値が高いほど創造的な応答に。
- `top_p`で累積確率の上位トークンに選択を制限し、生成テキストの質を向上。
- `frequencyPenalty`と`presencePenalty`で繰り返しを減らし、多様性を促進。
- `top_k`でモデルを上位K個の最も確率の高いトークンに制限し、一貫性のある応答を促進。

---

## 決定論的Sampling

一貫した出力が求められるアプリケーションでは、決定論的Samplingにより再現可能な結果を保証します。これは固定の乱数シードを使い、temperatureをゼロに設定することで実現します。

以下のサンプル実装で、さまざまなプログラミング言語における決定論的Samplingを示します。

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

上記コードでは：

- 指定したサーバーURLでMCPクライアントを作成しました。
- 同じプロンプト、固定シード、temperatureゼロの2つのリクエストを設定。
- 両方のリクエストを送信し、生成されたテキストを出力。
- 同じシードとtemperatureのため、応答が同一であることを示しました。
- `setSeed`で固定乱数シードを指定し、同じ入力に対して常に同じ出力を生成。
- `temperature`をゼロに設定し、最大限の決定論性を確保。モデルは常に最も確率の高い次のトークンを選択。

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

上記コードでは：

- サーバーURLでMCPクライアントを初期化。
- 同じプロンプト、固定シード、temperatureゼロの2つのリクエストを設定。
- 両方のリクエストを送信し、生成されたテキストを出力。
- 同じシードとtemperatureのため、応答が同一であることを示しました。
- `seed`で固定乱数シードを指定し、同じ入力に対して常に同じ出力を生成。
- `temperature`をゼロに設定し、最大限の決定論性を確保。モデルは常に最も確率の高い次のトークンを選択。
- 3つ目のリクエストでは異なるシードを使用し、同じプロンプトとtemperatureでも異なる出力になることを示しました。

---

## 動的Sampling設定

インテリジェントなSamplingは、リクエストのコンテキストや要件に応じてパラメータを適応的に調整します。つまり、タスクの種類、ユーザーの好み、過去のパフォーマンスに基づいて、temperature、top_p、ペナルティなどを動的に変更します。

以下に、さまざまなプログラミング言語での動的Sampling実装例を示します。

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

上記コードでは：

- 適応的Samplingを管理する`DynamicSamplingService`クラスを作成。
- 創造的、事実ベース、コード、分析などのタスクタイプごとにSamplingプリセットを定義。
- タスクタイプに基づいて基本Samplingプリセットを選択。
- ユーザーの創造性や多様性の好みに応じてSamplingパラメータを調整。
- 動的に設定したSamplingパラメータでリクエストを送信。
- 生成されたテキストと適用されたSamplingパラメータ、タスクタイプを返却し透明性を確保。
- `temperature`で出力のランダム性を制御。値が高いほど創造的な応答に。
- `top_p`で累積確率の上位トークンに選択を制限し、生成テキストの質を向上。
- `frequency_penalty`で繰り返しを減らし、多様性を促進。
- `user_preferences`でユーザー定義の創造性や多様性レベルに基づくSamplingパラメータのカスタマイズを可能に。
- `task_type`でリクエストに適したSampling戦略を決定し、タスクの性質に応じた応答を実現。
- `send_request`メソッドで設定したSamplingパラメータを使いプロンプトを送信し、モデルが指定要件に沿ったテキストを生成。
- `generated_text`でモデルの応答を取得し、Samplingパラメータとタスクタイプと共に返却。
- `min`と`max`関数でユーザーの好みを有効範囲内に制限し、不正なSampling設定を防止。

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

上記コードでは：

- タスクタイプとユーザーの好みに基づく動的Samplingを管理する`AdaptiveSamplingManager`クラスを作成。
- 創造的、事実ベース、コード、会話などのタスクタイプごとにSamplingプロファイルを定義。
- プロンプトから単純なヒューリスティックでタスクタイプを検出するメソッドを実装。
- 検出したタスクタイプとユーザーの好みに基づいてSamplingパラメータを計算。
- 過去のパフォーマンスに基づく学習済み調整を適用しSamplingパラメータを最適化。
- 将来の調整のためにパフォーマンスを記録し、システムが過去のやり取りから学習可能に。
- 動的に設定したSamplingパラメータでリクエストを送信し、生成テキストと適用パラメータ、検出したタスクタイプを返却。
- 以下を使用：
    - `userPreferences`でユーザー定義の創造性、精度、一貫性レベルに基づくSamplingパラメータのカスタマイズを可能に。
    - `detectTaskType`でプロンプトからタスクの性質を判別し、適切なSampling戦略を適用。
    - `recordPerformance`で生成応答のパフォーマンスを記録し、システムの適応と改善を促進。
    - `applyLearnedAdjustments`で過去のパフォーマンスに基づきSamplingパラメータを修正し、高品質な応答生成を強化。
    - `generateResponse`で適応Samplingを用いた応答生成プロセスをカプセル化し、異なるプロンプトやコンテキストで簡単に呼び出し可能に。
    - `allowedTools`で生成時にモデルが使用できるツールを指定し、よりコンテキストに即した応答を実現。
    - `feedbackScore`でユーザーが生成応答の品質にフィードバックを提供し、モデルの性能向上に活用。
    - `performanceHistory`で過去のやり取りの記録を保持し、成功や失敗から学習。
    - `getSamplingParameters`でリクエストのコンテキストに応じてSamplingパラメータを動的に調整し、柔軟で応答性の高いモデル動作を実現。
    - `detectTaskType`でプロンプトに基づきタスクを分類し、異なるタイプのリクエストに適したSampling戦略を適用。
    - `samplingProfiles`でタスクタイプごとの基本Sampling設定を定義し、リクエストの性質に応じた迅速な調整を可能に。

---

## 次に進むこと

- [5.7 Scaling](../mcp-scaling/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。