> [!WARNING]
> Örnekleme, MCP `2026-07-28` sürümünde kullanımdan kaldırılmıştır. Bu ders, 
> eski uygulamalar için saklanmıştır. Yeni sunucular doğrudan bir LLM sağlayıcı API'si 
> ile entegre olmalıdır.

# Model Context Protocol'de Örnekleme

> Örnekleme, `2026-07-28` spesifikasyonunda uyumluluk için kalmaya devam etmekte olup
> 28 Temmuz 2027 veya sonrası yayımlanacak ilk revizyonunda kaldırılabilir. Bu derste
> yer alan örnekler `2025-11-25` sürümünü uygulayan SDK API'lerini kullanabilir.
> Bakınız [MCP'de Neler Değişti: 2026-07-28 Spesifikasyonu](../../01-CoreConcepts/mcp-2026-07-28.md).

Eski MCP uygulamalarında, Örnekleme sunucuların istemci aracılığıyla LLM tamamlamaları 
talep etmelerine olanak tanır. Bu ders, uyumluluk ve geçiş çalışmaları için kullanımdan
kaldırılan bu protokol akışını açıklar.

## Giriş

Bu derste, MCP isteklerinde örnekleme parametrelerini nasıl yapılandıracağımızı ve örneklemenin






- MCP'de bulunan temel örnekleme parametrelerini anlamak.
- Farklı kullanım durumları için örnekleme parametrelerini yapılandırmak.
- Yeniden üretilebilir sonuçlar için deterministik örnekleme uygulamak.
- Bağlama ve kullanıcı tercihine göre örnekleme parametrelerini dinamik olarak ayarlamak.
- Çeşitli senaryolarda model performansını artırmak için örnekleme stratejileri uygulamak.






1. Sunucu, istemciye `sampling/createMessage` isteği gönderir
2. İstemci isteği inceler ve gerektiğinde değişiklik yapabilir
3. İstemci LLM'den örnekleme yapar
4. İstemci tamamlamayı inceler








| Parametre | Açıklama | Tipik Aralık |
|-----------|-------------|---------------|
| `temperature` | Token seçiminde rastgeleliği kontrol eder | 0.0 - 1.0 |
| `maxTokens` | Üretilecek maksimum token sayısı | Tamsayı değeri |
| `stopSequences` | Karşılaşıldığında üretimi durduran özel diziler | String dizisi |




| Yaygın Uzantı Parametresi | Açıklama | Tipik Aralık |
|-----------|-------------|---------------|
| `top_p` | Nucleus örnekleme - tokenleri en yüksek kümülatif olasılığa göre sınırlar | 0.0 - 1.0 |
| `top_k` | Token seçimlerini en iyi K seçenekle sınırlar | 1 - 100 |
| `presence_penalty` | Metinde daha önce yer alan tokenlere ceza uygular | -2.0 - 2.0 |
| `frequency_penalty` | Metindeki tokenlerin sıklığına göre ceza uygular | -2.0 - 2.0 |






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





- **İstemler için**:
  - İstemciler kullanıcıya önerilen istemi göstermelidir
  - Kullanıcılar istemleri değiştirebilmeli veya reddedebilmelidir
  - Sistem istemleri filtrelenebilir veya değiştirilebilir


- **Tamamlamalar için**:
  - İstemciler kullanıcıya tamamlamayı göstermelidir
  - Kullanıcılar tamamlamaları değiştirebilmeli veya reddedebilmelidir
  - İstemciler tamamlamaları filtreleyebilir veya değiştirebilir








- İstemciye göndermeden önce tüm mesaj içeriğini doğrulayın
- İstemlerden ve tamamlamalardan hassas bilgileri temizleyin
- Kötüye kullanımı önlemek için oran limitleri uygulayın
- Örnekleme kullanımını olağan dışı desenler için izleyin
- Veriyi güvenli protokollerle iletin
- Kullanıcı veri gizliliğini ilgili düzenlemeler doğrultusunda yönetin
- Uyumluluk ve güvenlik için örnekleme isteklerini denetleyin
- Maliyet maruziyetini uygun limitlerle kontrol edin
- Örnekleme hatalarını uygun geri dönüşlerle nazikçe yönetin

Örnekleme parametreleri, dil modellerinin davranışını ince ayar yaparak deterministik ve yaratıcı çıktılar arasında istenen dengeyi sağlar.

Bu parametrelerin çeşitli programlama dillerinde nasıl yapılandırılacağına bakalım.

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

Önceki kodda:

- Belirli bir sunucu URL'si ile MCP istemcisi oluşturuldu.
- `temperature`, `top_p` ve `top_k` gibi örnekleme parametreleri ile istek yapılandırıldı.
- İstek gönderilip üretilen metin yazdırıldı.
- Kullanılanlar:
    - Modelin üretim sırasında kullanabileceği araçları belirlemek için `allowedTools`. Bu durumda, yaratıcı uygulama fikirleri üretimi için `ideaGenerator` ve `marketAnalyzer` araçlarının kullanımı izin verildi.
    - Çıktıda tekrarları ve çeşitliliği kontrol etmek için `frequencyPenalty` ve `presencePenalty`.
    - Daha yaratıcı yanıtlar için çıktının rastgeleliğini kontrol eden `temperature`.
    - Üretilen metnin kalitesini artırmak için token seçimlerini en yüksek kümülatif olasılık kütlesine göre sınırlandıran `top_p`.
    - Modeli en olası K token ile sınırlayarak daha tutarlı yanıtların üretilmesini sağlayan `top_k`.
    - Üretilen metindeki tekrarları azaltıp çeşitliliği teşvik etmek için `frequencyPenalty` ve `presencePenalty`.

# [JavaScript](#tab/javascript)

```javascript
// JavaScript Örneği: Sıcaklık ve Top-P örnekleme yapılandırması
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // MCP istemcisini başlat
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Farklı örnekleme parametreleriyle isteği yapılandır
  const creativeSampling = {
    temperature: 0.9,    // Daha yüksek sıcaklık = daha fazla rastgelelik/yaratıcılık
    topP: 0.92,          // En yüksek %92 olasılık kütlesine sahip tokenları dikkate al
    frequencyPenalty: 0.6, // Token dizilerinin tekrarını azalt
    presencePenalty: 0.4   // Şimdiye kadar metinde geçen tokenları cezalandır
  };
  
  const factualSampling = {
    temperature: 0.2,    // Daha düşük sıcaklık = daha belirleyici/gerçekçi
    topP: 0.85,          // Biraz daha odaklanmış token seçimi
    frequencyPenalty: 0.2, // Minimum tekrar cezası
    presencePenalty: 0.1   // Minimum varlık cezası
  };
  
  try {
    // Farklı örnekleme yapılandırmaları ile iki istek gönder
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

Önceki kodda:

- Sunucu URL'si ve API anahtarı ile MCP istemcisi başlatıldı.
- Yaratıcı ve gerçekçi görevler için farklı iki örnekleme parametresi seti yapılandırıldı.
- Modele her görev için belirli araçları kullanma izni veren istekler gönderildi.
- Farklı örnekleme parametrelerinin etkilerini göstermek için üretilen yanıtlar yazdırıldı.
- Yaratıcı görevlerde `ideaGenerator` ve `environmentalImpactTool`, gerçekçi görevlerde ise `factChecker` ve `dataAnalysisTool` araçlarının kullanımına izin veren `allowedTools` kullanıldı.
- Daha yaratıcı yanıtlar için çıktının rastgeleliğini kontrol eden `temperature` kullanıldı.

- Üretilen metnin kalitesini artırmak için, seçilen tokenları en yüksek kümülatif olasılık kütlesine katkıda bulunanlarla sınırlamak için `top_p` kullanıldı.
- Çıktıda tekrarı azaltmak ve çeşitliliği teşvik etmek için `frequencyPenalty` ve `presencePenalty` kullanıldı.
- Daha tutarlı yanıtlar üretmeye yardımcı olmak için modeli en olası K token ile sınırlandırmak amacıyla `top_k` kullanıldı.

---

## Deterministik Örnekleme

Tutarlı çıktılar gerektiren uygulamalar için, deterministik örnekleme tekrarlanabilir sonuçlar sağlar. Bunu yapmak için sabit bir rastgele tohum kullanılır ve sıcaklık sıfıra ayarlanır.

Aşağıdaki örnek implementasyona bakalım; deterministik örneklemeyi farklı programlama dillerinde göstermek için.

# [Java](#tab/java)

```java
// Java Örneği: Sabit tohum ile deterministik yanıtlar
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Deterministik sonuçlar için sabit tohum kullanımı
        
        // Sabit tohum ile ilk istek
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Maksimum deterministiklik için sıfır sıcaklık
            .build();
            
        // Aynı tohum ile ikinci istek
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Her iki isteği çalıştır
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Aynı tohum ve sıcaklık=0 nedeniyle yanıtlar aynı olmalıdır
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Yukarıdaki kodda:

- Belirtilen sunucu URL'si ile bir MCP istemcisi oluşturuldu.
- Aynı istem ile, sabit tohum ve sıfır sıcaklık kullanılarak iki istek yapılandırıldı.
- Her iki istek gönderildi ve üretilen metin yazdırıldı.
- Örnekleme yapılandırmasının deterministik doğası (aynı tohum ve sıcaklık) nedeniyle yanıtların aynı olduğu gösterildi.
- `setSeed` kullanılarak sabit bir rastgele tohum belirtildi, böylece model her seferinde aynı girdi için aynı çıktıyı üretir.
- Maksimum deterministikliği sağlamak için `temperature` sıfıra ayarlandı; yani model her zaman en olası sonraki tokenı rastgelelik olmadan seçer.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// JavaScript Örneği: Tohum kontrolü ile belirleyici yanıtlar
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Sabit tohum ile ilk istek
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Maksimum deterministik için sıfır sıcaklık
    });
    
    // Aynı tohum ve sıcaklık ile ikinci istek
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Farklı tohum ama aynı sıcaklık ile üçüncü istek
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

- Bir sunucu URL'si ile MCP istemcisi başlatıldı.
- Aynı istem ile, sabit tohum ve sıfır sıcaklık kullanılarak iki istek yapılandırıldı.
- Her iki istek gönderildi ve üretilen metin yazdırıldı.
- Örnekleme yapılandırmasının deterministik doğası (aynı tohum ve sıcaklık) nedeniyle yanıtların aynı olduğu gösterildi.
- `seed` kullanılarak sabit bir rastgele tohum belirtildi, böylece model her seferinde aynı girdi için aynı çıktıyı üretir.
- Maksimum deterministikliği sağlamak için `temperature` sıfıra ayarlandı; yani model her zaman en olası sonraki tokenı rastgelelik olmadan seçer.
- Aynı istem ve sıcaklıkla üçüncü istek için farklı bir tohum kullanıldı; böylece tohum değiştiğinde farklı çıktılar oluştuğu gösterildi.

---

## Dinamik Örnekleme Yapılandırması

Akıllı örnekleme, her isteğin bağlamına ve gereksinimlerine göre parametreleri uyarlayabilir. Yani görev türü, kullanıcı tercihleri veya önceki performansa göre sıcaklık, top_p ve cezalar gibi parametreler dinamik olarak ayarlanır.

Dinamik örneklemenin farklı programlama dillerinde nasıl uygulanacağına bakalım.

# [Python](#tab/python)

```python
# Python Örneği: İstek bağlamına dayalı dinamik örnekleme
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Farklı görev türleri için örnekleme ön ayarlarını tanımla
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Temel ön ayarı seç
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Sağlanmışsa kullanıcı tercihlerine göre ayarla
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Yaratıcılık tercihlerine göre sıcaklığı ölçeklendir (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # İstenen yanıt çeşitliliğine göre top_p'yi ayarla
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Özel örnekleme parametreleri ile istek oluştur ve gönder
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Şeffaflık için örnekleme meta verisi ile yanıtı döndür
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Yukarıdaki kodda:

- Uyarlanabilir örneklemeyi yöneten `DynamicSamplingService` sınıfı oluşturuldu.
- Farklı görev türleri (yaratıcı, gerçek, kod, analitik) için örnekleme ön ayarları tanımlandı.
- Görev türüne göre bir temel örnekleme ön ayarı seçildi.
- Yaratıcılık seviyesi ve çeşitlilik gibi kullanıcı tercihleri temel alınarak örnekleme parametreleri ayarlandı.
- Dinamik olarak yapılandırılmış örnekleme parametreleriyle istek gönderildi.
- Şeffaflık için, üretilen metin örnekleme parametreleri ve görev türüyle birlikte döndürüldü.
- Çıktının rastgeleliğini kontrol etmek için `temperature` kullanıldı; daha yüksek değerler daha yaratıcı yanıtlar sağlar.
- Üretilen metnin kalitesini artırmak için `top_p` ile token seçimi kümülatif olasılık kütlesine katkıda bulunanlarla sınırlandırıldı.
- Tekrarı azaltmak ve çeşitliliği artırmak için `frequency_penalty` kullanıldı.
- Kullanıcı tarafından tanımlanan yaratıcılık ve çeşitlilik seviyelerine göre örnekleme parametrelerinin özelleştirilmesine izin vermek için `user_preferences` kullanıldı.
- Görev türüne bağlı olarak uygun örnekleme stratejisini belirlemek için `task_type` kullanıldı; böylece görevin doğasına göre daha özelleştirilmiş yanıtlar sağlandı.
- Yapılandırılmış örnekleme parametreleri ile istem gönderilmesi için `send_request` yöntemi kullanıldı; model belirlenen gereksinimlere göre metin üretti.
- Modelin yanıtını elde etmek için `generated_text` kullanıldı; bu, daha fazla analiz veya gösterim için örnekleme parametreleri ve görev türüyle birlikte döndürüldü.
- Kullanıcı tercihleri geçerli aralıklarda tutulması için `min` ve `max` fonksiyonlarıyla sınırlandırıldı; böylece geçersiz örnekleme yapılandırmaları önlendi.

# [JavaScript Dinamik](#tab/javascript-dynamic)

```javascript
// JavaScript Örneği: Kullanıcı bağlamına dayalı dinamik örnekleme yapılandırması
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Temel örnekleme profillerini tanımla
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Tarihsel performansı takip et
    this.performanceHistory = [];
  }
  
  // İpucundan görev türünü tespit et
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Basit sezgi tespiti - ML sınıflandırmasıyla geliştirilebilir
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
    
    // Açık bir tür tespit edilmezse varsayılan olarak konuşma moduna geç
    return 'conversational';
  }
  
  // Bağlam ve kullanıcı tercihlerine göre örnekleme parametrelerini hesapla
  getSamplingParameters(prompt, context = {}) {
    // Görev türünü tespit et
    const taskType = this.detectTaskType(prompt, context);
    
    // Temel profili al
    let params = {...this.samplingProfiles[taskType]};
    
    // Kullanıcı tercihlerine göre ayarla
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // 1-10 aralığından uygun sıcaklık aralığına ölçeklendir
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Daha yüksek kesinlik, daha düşük topP anlamına gelir (daha odaklı seçim)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Daha yüksek tutarlılık daha düşük ceza anlamına gelir
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Performans geçmişinden öğrenilen ayarları uygula
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Basit uyarlanabilir mantık - daha gelişmiş algoritmalarla geliştirilebilir
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Sadece yakın geçmişi dikkate al
    
    if (relevantHistory.length > 0) {
      // Ortalama performans puanlarını hesapla
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Performans eşik altında ise parametreleri ayarla
      if (avgScore < 0.7) {
        // Daha güvenli değerlere hafif ayar
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Gelecek ayarlamalar için performansı kaydet
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Yanıt kalitesinin 0-1 arası değerlendirmesi
    });
    
    // Geçmiş boyutunu sınırlandır
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Optimize edilmiş örnekleme parametrelerini al
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Optimize edilmiş parametrelerle isteği gönder
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Kullanıcı geri bildirim sağlarsa, gelecek optimizasyon için kaydet
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

// Örnek kullanım
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Özel kullanıcı tercihleri ile yaratıcı görev
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Yüksek yaratıcılık (1-10)
          consistency: 3  // Düşük tutarlılık (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Kod oluşturma görevi
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Düşük yaratıcılık
          precision: 8,   // Yüksek kesinlik
          consistency: 9  // Yüksek tutarlılık
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

- Görev türüne ve kullanıcı tercihlerine göre dinamik örneklemeyi yöneten `AdaptiveSamplingManager` sınıfı oluşturuldu.
- Farklı görev türleri (yaratıcı, gerçek, kod, konuşma) için örnekleme profilleri tanımlandı.
- Basit sezgisel yöntemler kullanarak istemden görev türü tespit eden bir yöntem uygulandı.
- Algılanan görev türüne ve kullanıcı tercihlerine göre örnekleme parametreleri hesaplandı.
- Tarihsel performansa dayalı öğrenilmiş ayarlamalar uygulandı; örnekleme parametreleri optimize edildi.
- Gelecek ayarlamalar için performans kaydı tutuldu; sistem geçmiş etkileşimlerden öğrenebilsin diye.
- Dinamik yapılandırılmış örnekleme parametreleriyle istekler gönderildi ve üretilen metin uygulanan parametreler ve algılanan görev türüyle birlikte döndürüldü.
- Kullanıldı:
    - Kullanıcı tarafından tanımlanan yaratıcılık, kesinlik ve tutarlılık seviyelerine bağlı olarak örnekleme parametrelerinin özelleştirilmesini sağlamak için `userPreferences`.
    - İstemden görevin doğasını belirleyerek daha özelleştirilmiş yanıtlar için `detectTaskType`.
    - Üretilen yanıtların performansını kaydetmek ve sistemin zamanla adapte olmasını sağlamak için `recordPerformance`.
    - Modelin yüksek kaliteli yanıtlar üretebilme yeteneğini geliştirmek için tarihsel performansa göre örnekleme parametrelerini değiştiren `applyLearnedAdjustments`.
    - Farklı istemler ve bağlamlar için yanıt üretme sürecini kapsayan `generateResponse`.
    - Üretim sırasında modelin kullanabileceği araçları belirtmek için `allowedTools`; böylece daha bağlama duyarlı yanıtlar sağlanır.
    - Kullanıcıların üretilen yanıt kalitesi hakkında geri bildirim vermesini sağlayarak model performansını geliştirebilen `feedbackScore`.
    - Geçmiş etkileşimlerin kaydını tutan `performanceHistory`, sistemin önceki başarı ve başarısızlıklardan öğrenmesini sağlar.
    - İstek bağlamına göre örnekleme parametrelerini dinamik olarak ayarlayan `getSamplingParameters`, model davranışını daha esnek ve duyarlı kılar.
    - İsteme dayalı olarak görevi sınıflandıran `detectTaskType`, farklı istek türleri için uygun örnekleme stratejileri uygulanmasını sağlar.
    - Farklı görev türleri için temel örnekleme yapılandırmalarını tanımlayan `samplingProfiles`; böylece isteğin doğasına göre hızlı ayarlamalar yapılabilir.

---

## Sonraki Adımlar

- [5.7 Ölçeklendirme](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->