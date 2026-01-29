# Model Bağlam Protokolünde Örnekleme

Örnekleme, sunucuların istemci aracılığıyla LLM tamamlamaları talep etmesini sağlayan güçlü bir MCP özelliğidir. Bu, gelişmiş ajan davranışlarını mümkün kılarken güvenlik ve gizliliği korur. Doğru örnekleme yapılandırması, yanıt kalitesini ve performansını önemli ölçüde artırabilir. MCP, modellerin metin üretimini rastgelelik, yaratıcılık ve tutarlılığı etkileyen belirli parametrelerle kontrol etmek için standart bir yol sunar.

## Giriş

Bu derste, MCP isteklerinde örnekleme parametrelerinin nasıl yapılandırılacağını ve örneklemenin temel protokol mekaniklerini inceleyeceğiz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- MCP’de bulunan temel örnekleme parametrelerini anlamak.
- Farklı kullanım senaryoları için örnekleme parametrelerini yapılandırmak.
- Tekrarlanabilir sonuçlar için deterministik örneklemeyi uygulamak.
- Bağlama ve kullanıcı tercihlerine göre örnekleme parametrelerini dinamik olarak ayarlamak.
- Model performansını çeşitli senaryolarda artırmak için örnekleme stratejileri uygulamak.
- MCP’nin istemci-sunucu akışında örneklemenin nasıl çalıştığını anlamak.

## MCP’de Örnekleme Nasıl Çalışır

MCP’de örnekleme akışı şu adımları izler:

1. Sunucu, istemciye `sampling/createMessage` isteği gönderir
2. İstemci isteği inceler ve gerekirse değişiklik yapabilir
3. İstemci bir LLM’den örnekleme yapar
4. İstemci tamamlamayı gözden geçirir
5. İstemci sonucu sunucuya geri gönderir

Bu insan-döngüsünde tasarım, kullanıcıların LLM’nin ne gördüğü ve ne ürettiği üzerinde kontrol sahibi olmasını sağlar.

## Örnekleme Parametreleri Genel Bakış

MCP, istemci isteklerinde yapılandırılabilen aşağıdaki örnekleme parametrelerini tanımlar:

| Parametre | Açıklama | Tipik Aralık |
|-----------|----------|--------------|
| `temperature` | Token seçiminde rastgeleliği kontrol eder | 0.0 - 1.0 |
| `maxTokens` | Üretilecek maksimum token sayısı | Tam sayı değeri |
| `stopSequences` | Üretimi durduran özel diziler | String dizisi |
| `metadata` | Sağlayıcıya özgü ek parametreler | JSON nesnesi |

Birçok LLM sağlayıcısı, `metadata` alanı aracılığıyla aşağıdaki ek parametreleri destekler:

| Yaygın Uzantı Parametresi | Açıklama | Tipik Aralık |
|---------------------------|----------|--------------|
| `top_p` | Nucleus örnekleme - tokenları en yüksek kümülatif olasılığa göre sınırlar | 0.0 - 1.0 |
| `top_k` | Token seçiminde en yüksek K seçeneği ile sınırlar | 1 - 100 |
| `presence_penalty` | Metinde daha önce geçen tokenları cezalandırır | -2.0 - 2.0 |
| `frequency_penalty` | Metindeki token tekrar sıklığını cezalandırır | -2.0 - 2.0 |
| `seed` | Tekrarlanabilir sonuçlar için belirli rastgele tohum | Tam sayı değeri |

## Örnek İstek Formatı

İşte MCP’de istemciden örnekleme talep etme örneği:

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

## Yanıt Formatı

İstemci bir tamamlanma sonucu döner:

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

## İnsan Denetimi Kontrolleri

MCP örneklemesi insan gözetimi düşünülerek tasarlanmıştır:

- **İstemler için**:
  - İstemciler, kullanıcılara önerilen istemi göstermelidir
  - Kullanıcılar istemleri değiştirebilmeli veya reddedebilmelidir
  - Sistem istemleri filtrelenebilir veya değiştirilebilir
  - Bağlam dahil edilmesi istemci tarafından kontrol edilir

- **Tamamlamalar için**:
  - İstemciler, kullanıcılara tamamlamayı göstermelidir
  - Kullanıcılar tamamlamaları değiştirebilmeli veya reddedebilmelidir
  - İstemciler tamamlamaları filtreleyebilir veya değiştirebilir
  - Kullanıcılar hangi modelin kullanılacağını kontrol eder

Bu ilkeler ışığında, farklı programlama dillerinde örneklemenin nasıl uygulanacağına ve LLM sağlayıcıları arasında yaygın olarak desteklenen parametrelere odaklanacağız.

## Güvenlik Hususları

MCP’de örnekleme uygularken şu güvenlik en iyi uygulamalarını göz önünde bulundurun:

- İstemciye göndermeden önce tüm mesaj içeriğini doğrulayın
- İstemlerden ve tamamlamalardan hassas bilgileri temizleyin
- Kötüye kullanımı önlemek için hız sınırları uygulayın
- Olağandışı örnekleme kullanımını izleyin
- Verileri güvenli protokollerle şifreleyin
- Kullanıcı veri gizliliğini ilgili düzenlemelere uygun şekilde yönetin
- Uyumluluk ve güvenlik için örnekleme isteklerini denetleyin
- Maliyet riskini uygun sınırlarla kontrol edin
- Örnekleme istekleri için zaman aşımı uygulayın
- Model hatalarını uygun yedeklerle nazikçe yönetin

Örnekleme parametreleri, dil modellerinin davranışını ince ayarlayarak deterministik ve yaratıcı çıktılar arasında istenen dengeyi sağlar.

Şimdi bu parametrelerin farklı programlama dillerinde nasıl yapılandırıldığına bakalım.

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

Yukarıdaki kodda:

- Belirli bir sunucu URL’si ile MCP istemcisi oluşturduk.
- `temperature`, `top_p` ve `top_k` gibi örnekleme parametreleriyle bir istek yapılandırdık.
- İsteği gönderdik ve oluşturulan metni yazdırdık.
- Şunları kullandık:
    - `allowedTools` ile modelin üretim sırasında kullanabileceği araçları belirttik. Bu örnekte, yaratıcı uygulama fikirleri üretmek için `ideaGenerator` ve `marketAnalyzer` araçlarını kullandık.
    - `frequencyPenalty` ve `presencePenalty` ile çıktıdaki tekrarları ve çeşitliliği kontrol ettik.
    - `temperature` ile çıktının rastgeleliğini kontrol ettik; daha yüksek değerler daha yaratıcı yanıtlar sağlar.
    - `top_p` ile token seçimlerini en yüksek kümülatif olasılık kütlesine katkıda bulunanlarla sınırlandırarak metin kalitesini artırdık.
    - `top_k` ile modeli en olası K token ile sınırlandırarak daha tutarlı yanıtlar elde ettik.
    - `frequencyPenalty` ve `presencePenalty` ile tekrarları azaltıp çeşitliliği teşvik ettik.

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

Yukarıdaki kodda:

- Sunucu URL’si ve API anahtarı ile MCP istemcisi başlattık.
- Yaratıcı görevler ve gerçekçi görevler için iki farklı örnekleme parametre seti yapılandırdık.
- Bu yapılandırmalarla istekler gönderdik ve modelin her görev için belirli araçları kullanmasına izin verdik.
- Farklı örnekleme parametrelerinin etkilerini göstermek için oluşturulan yanıtları yazdırdık.
- `allowedTools` ile modelin üretim sırasında kullanabileceği araçları belirttik. Yaratıcı görevlerde `ideaGenerator` ve `environmentalImpactTool`, gerçekçi görevlerde ise `factChecker` ve `dataAnalysisTool` araçlarını kullandık.
- `temperature` ile çıktının rastgeleliğini kontrol ettik; daha yüksek değerler daha yaratıcı yanıtlar sağlar.
- `top_p` ile token seçimlerini en yüksek kümülatif olasılık kütlesine katkıda bulunanlarla sınırlandırarak metin kalitesini artırdık.
- `frequencyPenalty` ve `presencePenalty` ile tekrarları azaltıp çeşitliliği teşvik ettik.
- `top_k` ile modeli en olası K token ile sınırlandırarak daha tutarlı yanıtlar elde ettik.

---

## Deterministik Örnekleme

Tutarlı çıktılar gerektiren uygulamalar için deterministik örnekleme tekrarlanabilir sonuçlar sağlar. Bunu, sabit bir rastgele tohum kullanarak ve sıcaklığı sıfıra ayarlayarak yapar.

Aşağıdaki örnek uygulamalar, farklı programlama dillerinde deterministik örneklemeyi göstermektedir.

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

Yukarıdaki kodda:

- Belirtilen sunucu URL’si ile MCP istemcisi oluşturduk.
- Aynı istem için sabit tohum ve sıfır sıcaklıkla iki istek yapılandırdık.
- Her iki isteği gönderdik ve oluşturulan metni yazdırdık.
- Yanıtların deterministik örnekleme yapılandırması (aynı tohum ve sıcaklık) nedeniyle aynı olduğunu gösterdik.
- `setSeed` ile sabit rastgele tohum belirledik, böylece model aynı girdi için her zaman aynı çıktıyı üretir.
- `temperature` değerini sıfıra ayarlayarak maksimum deterministikliği sağladık; model her zaman en olası sonraki tokenı rastgelelik olmadan seçer.

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

Yukarıdaki kodda:

- Sunucu URL’si ile MCP istemcisi başlattık.
- Aynı istem için sabit tohum ve sıfır sıcaklıkla iki istek yapılandırdık.
- Her iki isteği gönderdik ve oluşturulan metni yazdırdık.
- Yanıtların deterministik örnekleme yapılandırması (aynı tohum ve sıcaklık) nedeniyle aynı olduğunu gösterdik.
- `seed` ile sabit rastgele tohum belirledik, böylece model aynı girdi için her zaman aynı çıktıyı üretir.
- `temperature` değerini sıfıra ayarlayarak maksimum deterministikliği sağladık; model her zaman en olası sonraki tokenı rastgelelik olmadan seçer.
- Üçüncü istek için farklı bir tohum kullanarak, aynı istem ve sıcaklıkla tohum değişikliğinin farklı çıktılar ürettiğini gösterdik.

---

## Dinamik Örnekleme Yapılandırması

Akıllı örnekleme, her isteğin bağlamı ve gereksinimlerine göre parametreleri uyarlamayı içerir. Bu, görev türü, kullanıcı tercihleri veya geçmiş performansa bağlı olarak `temperature`, `top_p` ve cezalar gibi parametrelerin dinamik olarak ayarlanması anlamına gelir.

Farklı programlama dillerinde dinamik örneklemenin nasıl uygulanacağına bakalım.

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

Yukarıdaki kodda:

- Uyarlanabilir örneklemeyi yöneten `DynamicSamplingService` sınıfı oluşturduk.
- Farklı görev türleri için (yaratıcı, gerçekçi, kod, analitik) örnekleme ön ayarları tanımladık.
- Görev türüne göre temel örnekleme ön ayarını seçtik.
- Kullanıcı tercihleri (yaratıcılık seviyesi, çeşitlilik) doğrultusunda örnekleme parametrelerini ayarladık.
- Dinamik yapılandırılmış örnekleme parametreleriyle isteği gönderdik.
- Üretilen metni, uygulanan örnekleme parametreleri ve görev türü ile birlikte şeffaflık için döndürdük.
- `temperature` ile çıktının rastgeleliğini kontrol ettik; daha yüksek değerler daha yaratıcı yanıtlar sağlar.
- `top_p` ile token seçimlerini en yüksek kümülatif olasılık kütlesine katkıda bulunanlarla sınırlandırarak metin kalitesini artırdık.
- `frequency_penalty` ile tekrarları azaltıp çeşitliliği teşvik ettik.
- `user_preferences` ile kullanıcı tanımlı yaratıcılık ve çeşitlilik seviyelerine göre örnekleme parametrelerinin özelleştirilmesine izin verdik.
- `task_type` ile isteğin doğasına göre uygun örnekleme stratejisini belirledik, böylece daha hedefe yönelik yanıtlar sağladık.
- `send_request` yöntemiyle yapılandırılmış örnekleme parametreleriyle istem göndererek modelin belirtilen gereksinimlere göre metin üretmesini sağladık.
- `generated_text` ile model yanıtını alıp, örnekleme parametreleri ve görev türü ile birlikte döndürdük.
- `min` ve `max` fonksiyonlarıyla kullanıcı tercihlerini geçerli aralıklarda tutarak geçersiz örnekleme yapılandırmalarını önledik.

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

Yukarıdaki kodda:

- Görev türü ve kullanıcı tercihlerine göre dinamik örneklemeyi yöneten `AdaptiveSamplingManager` sınıfı oluşturduk.
- Farklı görev türleri için (yaratıcı, gerçekçi, kod, sohbet) örnekleme profilleri tanımladık.
- Basit sezgisel yöntemlerle istemden görev türünü tespit eden bir yöntem uyguladık.
- Tespit edilen görev türü ve kullanıcı tercihlerine göre örnekleme parametrelerini hesapladık.
- Geçmiş performansa dayalı öğrenilmiş ayarlamaları uygulayarak örnekleme parametrelerini optimize ettik.
- Gelecekteki ayarlamalar için performansı kaydettik, böylece sistem geçmiş etkileşimlerden öğrenebilsin.
- Dinamik yapılandırılmış örnekleme parametreleriyle istekler gönderdik ve oluşturulan metni, uygulanan parametreler ve tespit edilen görev türü ile birlikte döndürdük.
- Şunları kullandık:
    - `userPreferences` ile kullanıcı tanımlı yaratıcılık, hassasiyet ve tutarlılık seviyelerine göre örnekleme parametrelerinin özelleştirilmesine izin verdik.
    - `detectTaskType` ile isteme dayalı görev türünü belirleyerek daha hedefe yönelik yanıtlar sağladık.
    - `recordPerformance` ile oluşturulan yanıtların performansını kaydederek sistemin zamanla uyum sağlamasını sağladık.
    - `applyLearnedAdjustments` ile geçmiş performansa dayalı örnekleme parametrelerini değiştirerek modelin yüksek kaliteli yanıtlar üretme yeteneğini artırdık.
    - `generateResponse` ile uyarlanabilir örnekleme ile yanıt üretme sürecini kapsülledik, böylece farklı istemler ve bağlamlarla kolayca çağrılabilir hale getirdik.
    - `allowedTools` ile modelin üretim sırasında kullanabileceği araçları belirledik, böylece daha bağlama duyarlı yanıtlar sağladık.
    - `feedbackScore` ile kullanıcıların oluşturulan yanıtın kalitesi hakkında geri bildirim vermesine olanak tanıdık, bu da model performansının zamanla iyileştirilmesini destekler.
    - `performanceHistory` ile geçmiş etkileşimlerin kaydını tutarak sistemin önceki başarı ve başarısızlıklardan öğrenmesini sağladık.
    - `getSamplingParameters` ile isteğin bağlamına göre örnekleme parametrelerini dinamik olarak ayarladık, böylece model davranışını daha esnek ve duyarlı hale getirdik.
    - `detectTaskType` ile isteme dayalı görev sınıflandırması yaparak farklı istek türleri için uygun örnekleme stratejileri uyguladık.
    - `samplingProfiles` ile farklı görev türleri için temel örnekleme yapılandırmaları tanımlayarak isteğin doğasına göre hızlı ayarlamalar yaptık.

---

## Sonraki Adımlar

- [5.7 Ölçeklendirme](../mcp-scaling/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.