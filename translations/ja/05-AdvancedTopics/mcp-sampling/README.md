> [!WARNING]
> MCPの`2026-07-28`ではSamplingは非推奨です。このレッスンは
> レガシー実装向けに残されています。新しいサーバーは直接LLM
> プロバイダーAPIと統合すべきです。

# Model Context ProtocolにおけるSampling

> Samplingは互換性のため`2026-07-28`仕様で残っており、
> 2027年7月28日以降にリリースされる最初の改訂で削除される予定です。
> このレッスンの例は`2025-11-25`を実装するSDK APIを使う場合があります。
> 詳細は[What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md)を参照してください。

レガシーなMCP実装において、Samplingはサーバーがクライアントを通じてLLMの完了を要求する方法です。このレッスンでは
非推奨になったこのプロトコルの流れを互換性と移行作業のために説明します。




Samplingの基礎となるプロトコルの仕組みを理解します。

## 学習目標

このレッスンの終わりには、以下ができるようになります：

- MCPで使用可能な主要なSamplingパラメータを理解すること。
- さまざまなユースケースのためにSamplingパラメータを設定すること。
- 再現性のある結果を得るための決定論的Samplingを実装すること。
- コンテキストやユーザーの好みに基づいてSamplingパラメータを動的に調整すること。
- さまざまなシナリオでモデルの性能を向上させるSampling戦略を適用すること。
- MCPのクライアント-サーバーフローにおけるSamplingの動作を理解すること。

## MCPにおけるSamplingの仕組み

MCPでのSamplingの流れは以下のステップです：

1. サーバーがクライアントに`sampling/createMessage`リクエストを送信
2. クライアントはリクエストを確認し、修正可能
3. クライアントがLLMからサンプリングを実施
4. クライアントが完了結果をレビュー
5. クライアントがサーバーに結果を返す

この人間が介在する設計により、ユーザーがLLMが見る内容と生成する内容を制御できます。

## Samplingパラメータの概要

MCPはクライアントリクエストで設定可能な以下のSamplingパラメータを定義しています：

| パラメータ | 説明 | 一般的な範囲 |
|-----------|-------------|---------------|
| `temperature` | トークン選択のランダム性を制御 | 0.0 - 1.0 |
| `maxTokens` | 生成される最大トークン数 | 整数値 |
| `stopSequences` | 生成を停止する特定のシーケンス | 文字列の配列 |
| `metadata` | プロバイダー固有の追加パラメータ | JSONオブジェクト |

多くのLLMプロバイダーは`metadata`フィールドを通じて追加パラメータをサポートしています。例えば：

| よくある拡張パラメータ | 説明 | 一般的な範囲 |
|-----------|-------------|---------------|
| `top_p` | ニュークリアスサンプリング - トップ累積確率に制限 | 0.0 - 1.0 |
| `top_k` | トップKのオプションに制限 | 1 - 100 |
| `presence_penalty` | テキスト中の出現に基づくペナルティ | -2.0 - 2.0 |
| `frequency_penalty` | テキスト中の頻度に基づくペナルティ | -2.0 - 2.0 |
| `seed` | 再現性のための特定の乱数シード | 整数値 |

## リクエスト例フォーマット

以下はMCPでクライアントからSamplingを要求する例です：

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

クライアントは完了結果を返します：

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

## 人間が介在するコントロール

MCPのSamplingは人間の監視を念頭に設計されています：

- <strong>プロンプトについて</strong>：
  - クライアントは提案されたプロンプトをユーザーに表示すべきです
  - ユーザーはプロンプトを修正または拒否できるべきです
  - システムプロンプトはフィルタリングまたは修正可能
  - コンテキストの含有はクライアントが制御します

- <strong>完了について</strong>：
  - クライアントは完了結果をユーザーに見せるべきです
  - ユーザーは完了結果を修正または拒否できるべきです
  - クライアントは完了結果をフィルタリングまたは修正可能
  - ユーザーは使用モデルを選択できます

これらの原則を踏まえ、共通のLLMプロバイダーでサポートされているパラメータに焦点を当てて、さまざまなプログラミング言語でのSampling実装方法を見てみましょう。

## セキュリティ上の考慮点

MCPでSamplingを実装する際は、以下のセキュリティベストプラクティスを考慮してください：

- <strong>メッセージ内容をすべて検証</strong>しクライアントに送信すること
- <strong>プロンプトや完了結果の機密情報のサニタイズ</strong>
- <strong>乱用防止のためレート制限を実装</strong>
- **異常なパターンのSampling使用を監視**
- <strong>安全なプロトコルで通信中のデータを暗号化</strong>
- <strong>関連規制に準拠したユーザーデータのプライバシー保護</strong>
- **コンプライアンスとセキュリティのためSamplingリクエストを監査**
- <strong>適切な制限でコストの露出をコントロール</strong>
- **Samplingリクエストにタイムアウトを実装**
- <strong>モデルエラーは適切に回避可能なフォールバックで扱う</strong>

Samplingパラメータは、決定論的な出力と創造的な出力の望ましいバランスを取るために言語モデルの動作を微調整することを可能にします。

それでは、さまざまなプログラミング言語でこれらのパラメータをどのように設定するかを見てみましょう。

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

前述のコードでは以下を行いました：

- 特定のサーバーURLでMCPクライアントを作成しました。
- `temperature`、`top_p`、`top_k`などSamplingパラメータを設定したリクエストを構成しました。
- リクエストを送信し、生成されたテキストを出力しました。
- 使用したもの：
    - `allowedTools`で生成時にモデルが使用可能なツールを指定しました。この場合、クリエイティブなアプリのアイデア生成を支援する`ideaGenerator`と`marketAnalyzer`ツールを許可しました。
    - 出力の繰り返しと多様性を制御するための`frequencyPenalty`と`presencePenalty`。
    - 出力のランダム性を制御する`temperature`。値が高いほど創造的な応答になります。
    - 生成品質を向上させるための累積確率上位に限定する`top_p`。
    - モデルをトップKの最も確率の高いトークンに制限し、一貫性のある応答生成に寄与する`top_k`。
    - 出力の繰り返しを減らし、多様性を促進するための`frequencyPenalty`と`presencePenalty`。

# [JavaScript](#tab/javascript)

```javascript
// JavaScriptの例：温度およびTop-Pサンプリングの設定
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // MCPクライアントを初期化する
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // 異なるサンプリングパラメータでリクエストを設定する
  const creativeSampling = {
    temperature: 0.9,    // 温度が高いほどランダム性/創造性が高くなる
    topP: 0.92,          // 上位92％の確率質量を持つトークンを考慮する
    frequencyPenalty: 0.6, // トークンシーケンスの繰り返しを減らす
    presencePenalty: 0.4   // これまでのテキストに出現したトークンをペナルティする
  };
  
  const factualSampling = {
    temperature: 0.2,    // 温度が低いほど決定的/事実的になる
    topP: 0.85,          // やや絞り込まれたトークン選択
    frequencyPenalty: 0.2, // 最小限の繰り返しペナルティ
    presencePenalty: 0.1   // 最小限のプレゼンスペナルティ
  };
  
  try {
    // 異なるサンプリング設定で2つのリクエストを送信する
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

前述のコードでは以下を行いました：

- サーバーURLとAPIキーでMCPクライアントを初期化しました。
- クリエイティブ用と事実ベース用の2つのSamplingパラメータセットを設定しました。
- これらの設定でリクエストを送り、各タスクに特定のツールをモデルが使用できるようにしました。
- 生成された応答を出力し、Samplingパラメータの効果を示しました。
- 生成時にモデルが使えるツールとして、クリエイティブ用に`ideaGenerator`と`environmentalImpactTool`、事実ベース用に`factChecker`と`dataAnalysisTool`を指定しました。
- 出力のランダム性を制御する`temperature`を使用しました。値が高いほど創造的な応答が得られます。

- 最上位の累積確率質量に寄与するトークンの選択を制限するために `top_p` を使用し、生成されるテキストの品質を向上させました。
- 繰り返しを減らし出力の多様性を促進するために `frequencyPenalty` と `presencePenalty` を使用しました。
- モデルを最も確率の高い上位K個のトークンに制限するために `top_k` を使用し、より一貫性のある応答の生成に役立てました。

---

## 決定的サンプリング

一貫した出力が必要なアプリケーションでは、決定的サンプリングにより再現可能な結果が保証されます。その方法は、固定されたランダムシードを使用し、温度をゼロに設定することです。

以下のサンプル実装を見て、異なるプログラミング言語での決定的サンプリングを示します。

# [Java](#tab/java)

```java
// Javaの例：固定シードによる決定論的な応答
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // 決定論的な結果のために固定シードを使用
        
        // 固定シードでの最初のリクエスト
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // 最大の決定論を得るための温度0
            .build();
            
        // 同じシードでの2回目のリクエスト
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // 両方のリクエストを実行
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // 同じシードと温度0のため、応答は同一のはず
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

上記のコードでは以下を行いました:

- 指定されたサーバーURLでMCPクライアントを作成しました。
- 同じプロンプト、固定シード、温度ゼロで2つのリクエストを構成しました。
- 両方のリクエストを送信し、生成されたテキストを出力しました。
- シードと温度が同じため、サンプリング設定が決定的であり応答が同一であることを示しました。
- 固定ランダムシードを指定するために `setSeed` を使用し、同じ入力に対して常に同じ出力を生成するようにしました。
- 最大の決定性を保証するために温度をゼロに設定し、モデルは常に最も確率の高い次のトークンを選択します。

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScriptの例：シード制御による決定論的な応答
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // 固定シードでの最初のリクエスト
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // 最大限の決定性のためのゼロ温度
    });
    
    // 同じシードと温度での2回目のリクエスト
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // 異なるシードだが同じ温度での3回目のリクエスト
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

上記のコードでは以下を行いました:

- サーバーURLでMCPクライアントを初期化しました。
- 同じプロンプト、固定シード、温度ゼロで2つのリクエストを構成しました。
- 両方のリクエストを送信し、生成されたテキストを出力しました。
- シードと温度が同じため、サンプリング設定が決定的であり応答が同一であることを示しました。
- 固定ランダムシードを指定するために `seed` を使用し、同じ入力に対して常に同じ出力を生成するようにしました。
- 最大の決定性を保証するために温度をゼロに設定し、モデルは常に最も確率の高い次のトークンを選択します。
- 3回目のリクエストでは異なるシードを使用し、同じプロンプトと温度でもシードを変えると出力が異なることを示しました。

---

## 動的サンプリング設定

インテリジェントなサンプリングは、各リクエストの文脈や要件に応じてパラメーターを適応的に調整します。これは、タスクの種類、ユーザーの好み、あるいは過去のパフォーマンスに基づき温度、top_p、ペナルティなどのパラメーターを動的に変えることを意味します。

異なるプログラミング言語における動的サンプリングの実装方法を見てみましょう。

# [Python](#tab/python)

```python
# Python例：リクエストコンテキストに基づく動的サンプリング
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # さまざまなタスクタイプに対するサンプリングプリセットを定義
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # ベースプリセットを選択
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # ユーザーの好みが提供されていればそれに基づいて調整
        if user_preferences:
            if "creativity_level" in user_preferences:
                # 創造性の好み（1-10）に基づいて温度をスケール
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # 望ましい応答の多様性に基づいてtop_pを調整
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # カスタムサンプリングパラメータでリクエストを作成し送信
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # 透明性のためにサンプリングメタデータを含む応答を返す
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

上記のコードでは以下を行いました:

- 適応的サンプリングを管理する `DynamicSamplingService` クラスを作成しました。
- クリエイティブ、事実、コード、分析など異なるタスク種別のサンプリングプリセットを定義しました。
- タスク種別に基づき基本のサンプリングプリセットを選択しました。
- 創造性レベルや多様性などユーザーの好みに基づいてサンプリングパラメーターを調整しました。
- 動的に設定されたサンプリングパラメーターでリクエストを送信しました。
- 生成されたテキストと適用されたサンプリングパラメーターおよびタスク種別を返して透明性を維持しました。
- 出力のランダム性を制御するために `temperature` を使用し、高い値はより創造的な応答へと繋がります。
- 最上位の累積確率質量に寄与するトークンの選択を制限するために `top_p` を使用し、生成テキストの品質を向上させました。
- 繰り返しを減らし出力の多様性を促進するために `frequency_penalty` を使用しました。
- ユーザー定義の創造性および多様性レベルに基づくサンプリングパラメーターのカスタマイズを可能にするために `user_preferences` を使用しました。
- リクエストのタスク種別に応じて適切なサンプリング戦略を決定するために `task_type` を使用しました。
- 設定されたサンプリングパラメーターでプロンプトを送信するために `send_request` メソッドを使用し、指定された要件に従ってテキストを生成しました。
- モデルの応答を取得するために `generated_text` を使用し、これをサンプリングパラメーターおよびタスク種別とともに返しました。これによりさらなる分析や表示が可能となります。
- `min` と `max` 関数を使用し、ユーザーの好みが有効範囲内に制限されるようにして、無効なサンプリング設定を防止しました。

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// JavaScriptの例：ユーザーコンテキストに基づく動的サンプリング設定
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // 基本サンプリングプロファイルを定義
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // 過去のパフォーマンスを追跡
    this.performanceHistory = [];
  }
  
  // プロンプトからタスクタイプを検出
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // 簡単なヒューリスティック検出 - 機械学習分類で強化可能
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
    
    // 明確なタイプが検出されない場合は会話形式をデフォルトに設定
    return 'conversational';
  }
  
  // コンテキストとユーザーの好みに基づいてサンプリングパラメータを計算
  getSamplingParameters(prompt, context = {}) {
    // タスクのタイプを検出
    const taskType = this.detectTaskType(prompt, context);
    
    // 基本プロファイルを取得
    let params = {...this.samplingProfiles[taskType]};
    
    // ユーザーの好みに基づいて調整
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // 1〜10の範囲を適切な温度範囲にスケーリング
        params.temperature = 0.1 + (creativity * 0.09); // 0.1〜1.0
      }
      
      if (precision !== undefined) {
        // より高い精度はより低いtopPを意味する（より焦点を絞った選択）
        params.topP = 1.0 - (precision * 0.05); // 0.5〜1.0
      }
      
      if (consistency !== undefined) {
        // より高い一貫性はより低いペナルティを意味する
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1〜0.9
      }
    }
    
    // パフォーマンス履歴から学習した調整を適用
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // シンプルな適応ロジック - より高度なアルゴリズムで強化可能
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // 最近の履歴のみを考慮
    
    if (relevantHistory.length > 0) {
      // 平均パフォーマンススコアを計算
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // パフォーマンスが閾値を下回った場合、パラメータを調整
      if (avgScore < 0.7) {
        // より安全な値へのわずかな調整
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // 今後の調整のためにパフォーマンスを記録
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // 応答品質の0〜1評価
    });
    
    // 履歴サイズを制限
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // 最適化されたサンプリングパラメータを取得
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // 最適化されたパラメータでリクエストを送信
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // ユーザーがフィードバックを提供した場合、将来の最適化のために記録
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

// 使用例
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // カスタムユーザー設定によるクリエイティブなタスク
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // 高い創造性（1〜10）
          consistency: 3  // 低い一貫性（1〜10）
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // コード生成タスク
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // 低い創造性
          precision: 8,   // 高い精度
          consistency: 9  // 高い一貫性
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

上記のコードでは以下を行いました:

- タスク種別とユーザーの好みに基づいた動的サンプリングを管理する `AdaptiveSamplingManager` クラスを作成しました。
- クリエイティブ、事実、コード、会話など異なるタスク種別のサンプリングプロファイルを定義しました。
- 簡単なヒューリスティックを用いてプロンプトからタスク種別を検出するメソッドを実装しました。
- 検出されたタスク種別とユーザーの好みに基づいてサンプリングパラメーターを計算しました。
- 過去のパフォーマンスに基づく学習調整を適用し、サンプリングパラメーターを最適化しました。
- 将来の調整のためにパフォーマンスを記録し、過去の対話から学習できるようにしました。
- 動的に設定されたサンプリングパラメーターでリクエストを送信し、生成されたテキストと適用パラメーターおよび検出されたタスク種別を返しました。
- 以下を使用しました:
    - `userPreferences` はユーザー定義の創造性、精度、および一貫性のレベルに基づきサンプリングパラメーターをカスタマイズ可能にします。
    - `detectTaskType` はプロンプトに基づいてタスクの性質を判断し、より適切な応答を可能にします。
    - `recordPerformance` は生成応答のパフォーマンスを記録し、システムが適応・改善できるようにします。
    - `applyLearnedAdjustments` は過去のパフォーマンスに基づいてサンプリングパラメーターを変更し、高品質な応答生成能力を強化します。
    - `generateResponse` は適応サンプリングを用いた応答生成の全過程をカプセル化し、異なるプロンプトやコンテキストで簡単に呼び出せるようにします。
    - `allowedTools` はモデルが生成中に使用可能なツールを指定し、よりコンテキストに即した応答を可能にします。
    - `feedbackScore` はユーザーが生成応答の品質にフィードバックを提供できるようにし、モデルの性能をさらに改善します。
    - `performanceHistory` は過去の対話記録を保持し、システムが成功や失敗から学習できるようにします。
    - `getSamplingParameters` はリクエストの文脈に基づきサンプリングパラメーターを動的に調整し、より柔軟で応答性の高いモデル動作を実現します。
    - `detectTaskType` はプロンプトに基づいてタスクを分類し、異なる種類のリクエストに適切なサンプリング戦略を適用します。
    - `samplingProfiles` は異なるタスク種別の基本サンプリング設定を定義し、リクエストの性質に応じた迅速な調整を可能にします。

---

## 次に進むこと

- [5.7 スケーリング](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->