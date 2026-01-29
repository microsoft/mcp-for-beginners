# Sampling dalam Protokol Konteks Model

Sampling adalah ciri MCP yang kuat yang membolehkan pelayan membuat permintaan penyempurnaan LLM melalui klien, membolehkan tingkah laku agen yang canggih sambil mengekalkan keselamatan dan privasi. Konfigurasi sampling yang tepat boleh meningkatkan kualiti dan prestasi respons dengan ketara. MCP menyediakan cara standard untuk mengawal bagaimana model menjana teks dengan parameter tertentu yang mempengaruhi kebarangkalian, kreativiti, dan koheren.

## Pengenalan

Dalam pelajaran ini, kita akan meneroka cara mengkonfigurasi parameter sampling dalam permintaan MCP dan memahami mekanik protokol sampling yang mendasari.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Memahami parameter sampling utama yang tersedia dalam MCP.
- Mengkonfigurasi parameter sampling untuk pelbagai kegunaan.
- Melaksanakan sampling deterministik untuk hasil yang boleh diulang.
- Melaraskan parameter sampling secara dinamik berdasarkan konteks dan keutamaan pengguna.
- Mengaplikasikan strategi sampling untuk meningkatkan prestasi model dalam pelbagai senario.
- Memahami bagaimana sampling berfungsi dalam aliran klien-pelayan MCP.

## Cara Sampling Berfungsi dalam MCP

Aliran sampling dalam MCP mengikuti langkah-langkah berikut:

1. Pelayan menghantar permintaan `sampling/createMessage` kepada klien  
2. Klien menyemak permintaan dan boleh mengubahnya  
3. Klien melakukan sampling dari LLM  
4. Klien menyemak penyempurnaan  
5. Klien memulangkan hasil kepada pelayan  

Reka bentuk manusia-dalam-laluan ini memastikan pengguna mengekalkan kawalan terhadap apa yang LLM lihat dan hasilkan.

## Gambaran Keseluruhan Parameter Sampling

MCP mentakrifkan parameter sampling berikut yang boleh dikonfigurasi dalam permintaan klien:

| Parameter       | Penerangan                                   | Julat Biasa     |
|-----------------|----------------------------------------------|-----------------|
| `temperature`   | Mengawal kebarangkalian dalam pemilihan token | 0.0 - 1.0       |
| `maxTokens`     | Bilangan maksimum token yang dijana           | Nilai integer   |
| `stopSequences` | Urutan tersuai yang menghentikan penjanaan apabila ditemui | Array string    |
| `metadata`      | Parameter tambahan khusus penyedia             | Objek JSON      |

Banyak penyedia LLM menyokong parameter tambahan melalui medan `metadata`, yang mungkin termasuk:

| Parameter Sambungan Biasa | Penerangan                                         | Julat Biasa     |
|--------------------------|----------------------------------------------------|-----------------|
| `top_p`                  | Sampling nucleus - mengehadkan token kepada kebarangkalian kumulatif teratas | 0.0 - 1.0       |
| `top_k`                  | Mengehadkan pemilihan token kepada pilihan teratas K | 1 - 100         |
| `presence_penalty`       | Menghukum token berdasarkan kehadiran mereka dalam teks setakat ini | -2.0 - 2.0      |
| `frequency_penalty`      | Menghukum token berdasarkan kekerapan mereka dalam teks setakat ini | -2.0 - 2.0      |
| `seed`                   | Benih rawak tertentu untuk hasil yang boleh diulang | Nilai integer   |

## Contoh Format Permintaan

Berikut adalah contoh permintaan sampling dari klien dalam MCP:

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

## Format Respons

Klien memulangkan hasil penyempurnaan:

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

## Kawalan Manusia dalam Laluan

Sampling MCP direka dengan pengawasan manusia dalam fikiran:

- **Untuk prompt**:  
  - Klien harus menunjukkan prompt yang dicadangkan kepada pengguna  
  - Pengguna harus boleh mengubah atau menolak prompt  
  - Prompt sistem boleh ditapis atau diubah  
  - Penyertaan konteks dikawal oleh klien  

- **Untuk penyempurnaan**:  
  - Klien harus menunjukkan penyempurnaan kepada pengguna  
  - Pengguna harus boleh mengubah atau menolak penyempurnaan  
  - Klien boleh menapis atau mengubah penyempurnaan  
  - Pengguna mengawal model yang digunakan  

Dengan prinsip ini, mari kita lihat cara melaksanakan sampling dalam pelbagai bahasa pengaturcaraan, dengan fokus pada parameter yang biasanya disokong oleh penyedia LLM.

## Pertimbangan Keselamatan

Apabila melaksanakan sampling dalam MCP, pertimbangkan amalan keselamatan terbaik berikut:

- **Sahkan semua kandungan mesej** sebelum menghantarnya kepada klien  
- **Bersihkan maklumat sensitif** daripada prompt dan penyempurnaan  
- **Laksanakan had kadar** untuk mengelakkan penyalahgunaan  
- **Pantau penggunaan sampling** untuk corak yang luar biasa  
- **Sulitkan data semasa penghantaran** menggunakan protokol selamat  
- **Urus privasi data pengguna** mengikut peraturan yang berkaitan  
- **Audit permintaan sampling** untuk pematuhan dan keselamatan  
- **Kawal pendedahan kos** dengan had yang sesuai  
- **Laksanakan masa tamat** untuk permintaan sampling  
- **Urus ralat model dengan baik** menggunakan pelan sandaran yang sesuai  

Parameter sampling membolehkan penalaan tingkah laku model bahasa untuk mencapai keseimbangan yang diingini antara output deterministik dan kreatif.

Mari kita lihat cara mengkonfigurasi parameter ini dalam pelbagai bahasa pengaturcaraan.

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

Dalam kod sebelum ini kami telah:

- Mencipta klien MCP dengan URL pelayan tertentu.  
- Mengkonfigurasi permintaan dengan parameter sampling seperti `temperature`, `top_p`, dan `top_k`.  
- Menghantar permintaan dan mencetak teks yang dijana.  
- Menggunakan:  
    - `allowedTools` untuk menentukan alat yang boleh digunakan model semasa penjanaan. Dalam kes ini, kami membenarkan alat `ideaGenerator` dan `marketAnalyzer` untuk membantu menjana idea aplikasi yang kreatif.  
    - `frequencyPenalty` dan `presencePenalty` untuk mengawal pengulangan dan kepelbagaian dalam output.  
    - `temperature` untuk mengawal kebarangkalian output, di mana nilai lebih tinggi menghasilkan respons yang lebih kreatif.  
    - `top_p` untuk mengehadkan pemilihan token kepada yang menyumbang kepada jisim kebarangkalian kumulatif teratas, meningkatkan kualiti teks yang dijana.  
    - `top_k` untuk mengehadkan model kepada token paling berkemungkinan teratas K, yang boleh membantu menghasilkan respons yang lebih koheren.  
    - `frequencyPenalty` dan `presencePenalty` untuk mengurangkan pengulangan dan menggalakkan kepelbagaian dalam teks yang dijana.

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

Dalam kod sebelum ini kami telah:

- Memulakan klien MCP dengan URL pelayan dan kunci API.  
- Mengkonfigurasi dua set parameter sampling: satu untuk tugasan kreatif dan satu lagi untuk tugasan faktual.  
- Menghantar permintaan dengan konfigurasi ini, membenarkan model menggunakan alat tertentu untuk setiap tugasan.  
- Mencetak respons yang dijana untuk menunjukkan kesan parameter sampling yang berbeza.  
- Menggunakan `allowedTools` untuk menentukan alat yang boleh digunakan model semasa penjanaan. Dalam kes ini, kami membenarkan `ideaGenerator` dan `environmentalImpactTool` untuk tugasan kreatif, dan `factChecker` serta `dataAnalysisTool` untuk tugasan faktual.  
- Menggunakan `temperature` untuk mengawal kebarangkalian output, di mana nilai lebih tinggi menghasilkan respons yang lebih kreatif.  
- Menggunakan `top_p` untuk mengehadkan pemilihan token kepada yang menyumbang kepada jisim kebarangkalian kumulatif teratas, meningkatkan kualiti teks yang dijana.  
- Menggunakan `frequencyPenalty` dan `presencePenalty` untuk mengurangkan pengulangan dan menggalakkan kepelbagaian dalam output.  
- Menggunakan `top_k` untuk mengehadkan model kepada token paling berkemungkinan teratas K, yang boleh membantu menghasilkan respons yang lebih koheren.

---

## Sampling Deterministik

Untuk aplikasi yang memerlukan output konsisten, sampling deterministik memastikan hasil yang boleh diulang. Caranya adalah dengan menggunakan benih rawak tetap dan menetapkan suhu kepada sifar.

Mari kita lihat contoh pelaksanaan di bawah untuk menunjukkan sampling deterministik dalam pelbagai bahasa pengaturcaraan.

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

Dalam kod sebelum ini kami telah:

- Mencipta klien MCP dengan URL pelayan yang ditetapkan.  
- Mengkonfigurasi dua permintaan dengan prompt yang sama, benih tetap, dan suhu sifar.  
- Menghantar kedua-dua permintaan dan mencetak teks yang dijana.  
- Menunjukkan bahawa respons adalah sama kerana sifat deterministik konfigurasi sampling (benih dan suhu yang sama).  
- Menggunakan `setSeed` untuk menentukan benih rawak tetap, memastikan model menjana output yang sama untuk input yang sama setiap kali.  
- Menetapkan `temperature` kepada sifar untuk memastikan determinisme maksimum, bermakna model sentiasa memilih token seterusnya yang paling berkemungkinan tanpa kebarangkalian.

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

Dalam kod sebelum ini kami telah:

- Memulakan klien MCP dengan URL pelayan.  
- Mengkonfigurasi dua permintaan dengan prompt yang sama, benih tetap, dan suhu sifar.  
- Menghantar kedua-dua permintaan dan mencetak teks yang dijana.  
- Menunjukkan bahawa respons adalah sama kerana sifat deterministik konfigurasi sampling (benih dan suhu yang sama).  
- Menggunakan `seed` untuk menentukan benih rawak tetap, memastikan model menjana output yang sama untuk input yang sama setiap kali.  
- Menetapkan `temperature` kepada sifar untuk memastikan determinisme maksimum, bermakna model sentiasa memilih token seterusnya yang paling berkemungkinan tanpa kebarangkalian.  
- Menggunakan benih berbeza untuk permintaan ketiga untuk menunjukkan bahawa perubahan benih menghasilkan output berbeza, walaupun dengan prompt dan suhu yang sama.

---

## Konfigurasi Sampling Dinamik

Sampling pintar menyesuaikan parameter berdasarkan konteks dan keperluan setiap permintaan. Ini bermakna melaraskan parameter seperti temperature, top_p, dan penalti berdasarkan jenis tugasan, keutamaan pengguna, atau prestasi sejarah.

Mari kita lihat cara melaksanakan sampling dinamik dalam pelbagai bahasa pengaturcaraan.

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

Dalam kod sebelum ini kami telah:

- Mencipta kelas `DynamicSamplingService` yang mengurus sampling adaptif.  
- Mentakrifkan preset sampling untuk pelbagai jenis tugasan (kreatif, faktual, kod, analitik).  
- Memilih preset sampling asas berdasarkan jenis tugasan.  
- Melaraskan parameter sampling berdasarkan keutamaan pengguna, seperti tahap kreativiti dan kepelbagaian.  
- Menghantar permintaan dengan parameter sampling yang dikonfigurasi secara dinamik.  
- Memulangkan teks yang dijana bersama parameter sampling dan jenis tugasan untuk ketelusan.  
- Menggunakan `temperature` untuk mengawal kebarangkalian output, di mana nilai lebih tinggi menghasilkan respons yang lebih kreatif.  
- Menggunakan `top_p` untuk mengehadkan pemilihan token kepada yang menyumbang kepada jisim kebarangkalian kumulatif teratas, meningkatkan kualiti teks yang dijana.  
- Menggunakan `frequency_penalty` untuk mengurangkan pengulangan dan menggalakkan kepelbagaian dalam output.  
- Menggunakan `user_preferences` untuk membenarkan penyesuaian parameter sampling berdasarkan tahap kreativiti dan kepelbagaian yang ditetapkan pengguna.  
- Menggunakan `task_type` untuk menentukan strategi sampling yang sesuai untuk permintaan, membolehkan respons yang lebih disesuaikan berdasarkan sifat tugasan.  
- Menggunakan kaedah `send_request` untuk menghantar prompt dengan parameter sampling yang dikonfigurasi, memastikan model menjana teks mengikut keperluan yang ditetapkan.  
- Menggunakan `generated_text` untuk mendapatkan respons model, yang kemudian dipulangkan bersama parameter sampling dan jenis tugasan untuk analisis atau paparan lanjut.  
- Menggunakan fungsi `min` dan `max` untuk memastikan keutamaan pengguna berada dalam julat sah, mengelakkan konfigurasi sampling yang tidak sah.

# [JavaScript Dinamik](../../../../05-AdvancedTopics/mcp-sampling)

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

Dalam kod sebelum ini kami telah:

- Mencipta kelas `AdaptiveSamplingManager` yang mengurus sampling dinamik berdasarkan jenis tugasan dan keutamaan pengguna.  
- Mentakrifkan profil sampling untuk pelbagai jenis tugasan (kreatif, faktual, kod, perbualan).  
- Melaksanakan kaedah untuk mengesan jenis tugasan dari prompt menggunakan heuristik mudah.  
- Mengira parameter sampling berdasarkan jenis tugasan yang dikesan dan keutamaan pengguna.  
- Mengaplikasikan pelarasan yang dipelajari berdasarkan prestasi sejarah untuk mengoptimumkan parameter sampling.  
- Merekod prestasi untuk pelarasan masa depan, membolehkan sistem belajar dari interaksi lalu.  
- Menghantar permintaan dengan parameter sampling yang dikonfigurasi secara dinamik dan memulangkan teks yang dijana bersama parameter yang digunakan dan jenis tugasan yang dikesan.  
- Menggunakan:  
    - `userPreferences` untuk membenarkan penyesuaian parameter sampling berdasarkan tahap kreativiti, ketepatan, dan konsistensi yang ditetapkan pengguna.  
    - `detectTaskType` untuk menentukan sifat tugasan berdasarkan prompt, membolehkan respons yang lebih disesuaikan.  
    - `recordPerformance` untuk merekod prestasi respons yang dijana, membolehkan sistem menyesuaikan dan memperbaiki dari masa ke masa.  
    - `applyLearnedAdjustments` untuk mengubah parameter sampling berdasarkan prestasi sejarah, meningkatkan keupayaan model menjana respons berkualiti tinggi.  
    - `generateResponse` untuk merangkum keseluruhan proses menjana respons dengan sampling adaptif, memudahkan panggilan dengan prompt dan konteks berbeza.  
    - `allowedTools` untuk menentukan alat yang boleh digunakan model semasa penjanaan, membolehkan respons yang lebih peka konteks.  
    - `feedbackScore` untuk membenarkan pengguna memberikan maklum balas tentang kualiti respons yang dijana, yang boleh digunakan untuk memperbaiki prestasi model dari masa ke masa.  
    - `performanceHistory` untuk menyimpan rekod interaksi lalu, membolehkan sistem belajar dari kejayaan dan kegagalan sebelumnya.  
    - `getSamplingParameters` untuk melaraskan parameter sampling secara dinamik berdasarkan konteks permintaan, membolehkan tingkah laku model yang lebih fleksibel dan responsif.  
    - `detectTaskType` untuk mengklasifikasikan tugasan berdasarkan prompt, membolehkan sistem menggunakan strategi sampling yang sesuai untuk pelbagai jenis permintaan.  
    - `samplingProfiles` untuk mentakrifkan konfigurasi sampling asas bagi pelbagai jenis tugasan, membolehkan pelarasan cepat berdasarkan sifat permintaan.

---

## Apa Seterusnya

- [5.7 Scaling](../mcp-scaling/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.