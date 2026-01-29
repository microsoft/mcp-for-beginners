# Sampling dalam Model Context Protocol

Sampling adalah fitur MCP yang kuat yang memungkinkan server untuk meminta penyelesaian LLM melalui klien, sehingga memungkinkan perilaku agen yang canggih sambil menjaga keamanan dan privasi. Konfigurasi sampling yang tepat dapat secara dramatis meningkatkan kualitas respons dan kinerja. MCP menyediakan cara standar untuk mengontrol bagaimana model menghasilkan teks dengan parameter spesifik yang memengaruhi keacakan, kreativitas, dan koherensi.

## Pendahuluan

Dalam pelajaran ini, kita akan mempelajari cara mengonfigurasi parameter sampling dalam permintaan MCP dan memahami mekanisme protokol sampling yang mendasarinya.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Memahami parameter sampling utama yang tersedia di MCP.
- Mengonfigurasi parameter sampling untuk berbagai kasus penggunaan.
- Menerapkan sampling deterministik untuk hasil yang dapat direproduksi.
- Menyesuaikan parameter sampling secara dinamis berdasarkan konteks dan preferensi pengguna.
- Menerapkan strategi sampling untuk meningkatkan kinerja model dalam berbagai skenario.
- Memahami cara kerja sampling dalam alur klien-server MCP.

## Cara Kerja Sampling di MCP

Alur sampling di MCP mengikuti langkah-langkah berikut:

1. Server mengirim permintaan `sampling/createMessage` ke klien
2. Klien meninjau permintaan dan dapat memodifikasinya
3. Klien melakukan sampling dari LLM
4. Klien meninjau hasil penyelesaian
5. Klien mengembalikan hasil ke server

Desain human-in-the-loop ini memastikan pengguna tetap mengontrol apa yang dilihat dan dihasilkan oleh LLM.

## Ikhtisar Parameter Sampling

MCP mendefinisikan parameter sampling berikut yang dapat dikonfigurasi dalam permintaan klien:

| Parameter | Deskripsi | Rentang Umum |
|-----------|-----------|--------------|
| `temperature` | Mengontrol keacakan dalam pemilihan token | 0.0 - 1.0 |
| `maxTokens` | Jumlah maksimum token yang dihasilkan | Nilai integer |
| `stopSequences` | Urutan khusus yang menghentikan generasi saat ditemukan | Array string |
| `metadata` | Parameter tambahan spesifik penyedia | Objek JSON |

Banyak penyedia LLM mendukung parameter tambahan melalui bidang `metadata`, yang mungkin meliputi:

| Parameter Ekstensi Umum | Deskripsi | Rentang Umum |
|------------------------|-----------|--------------|
| `top_p` | Nucleus sampling - membatasi token pada probabilitas kumulatif teratas | 0.0 - 1.0 |
| `top_k` | Membatasi pemilihan token pada K opsi teratas | 1 - 100 |
| `presence_penalty` | Memberi penalti pada token berdasarkan kemunculannya dalam teks sejauh ini | -2.0 - 2.0 |
| `frequency_penalty` | Memberi penalti pada token berdasarkan frekuensinya dalam teks sejauh ini | -2.0 - 2.0 |
| `seed` | Seed acak spesifik untuk hasil yang dapat direproduksi | Nilai integer |

## Contoh Format Permintaan

Berikut contoh permintaan sampling dari klien di MCP:

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

Klien mengembalikan hasil penyelesaian:

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

## Kontrol Human in the Loop

Sampling MCP dirancang dengan pengawasan manusia:

- **Untuk prompt**:
  - Klien harus menampilkan prompt yang diusulkan kepada pengguna
  - Pengguna harus dapat memodifikasi atau menolak prompt
  - Prompt sistem dapat difilter atau dimodifikasi
  - Penyertaan konteks dikendalikan oleh klien

- **Untuk penyelesaian**:
  - Klien harus menampilkan hasil penyelesaian kepada pengguna
  - Pengguna harus dapat memodifikasi atau menolak hasil penyelesaian
  - Klien dapat memfilter atau memodifikasi hasil penyelesaian
  - Pengguna mengontrol model mana yang digunakan

Dengan prinsip-prinsip ini, mari kita lihat cara mengimplementasikan sampling dalam berbagai bahasa pemrograman, dengan fokus pada parameter yang umum didukung oleh penyedia LLM.

## Pertimbangan Keamanan

Saat mengimplementasikan sampling di MCP, perhatikan praktik keamanan terbaik berikut:

- **Validasi semua konten pesan** sebelum mengirim ke klien
- **Bersihkan informasi sensitif** dari prompt dan hasil penyelesaian
- **Terapkan batasan laju** untuk mencegah penyalahgunaan
- **Pantau penggunaan sampling** untuk pola yang tidak biasa
- **Enkripsi data saat transit** menggunakan protokol aman
- **Tangani privasi data pengguna** sesuai regulasi yang berlaku
- **Audit permintaan sampling** untuk kepatuhan dan keamanan
- **Kontrol eksposur biaya** dengan batasan yang sesuai
- **Terapkan timeout** untuk permintaan sampling
- **Tangani kesalahan model dengan baik** menggunakan fallback yang sesuai

Parameter sampling memungkinkan penyetelan perilaku model bahasa untuk mencapai keseimbangan yang diinginkan antara keluaran deterministik dan kreatif.

Mari kita lihat cara mengonfigurasi parameter ini dalam berbagai bahasa pemrograman.

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

Dalam kode sebelumnya kami telah:

- Membuat klien MCP dengan URL server tertentu.
- Mengonfigurasi permintaan dengan parameter sampling seperti `temperature`, `top_p`, dan `top_k`.
- Mengirim permintaan dan mencetak teks yang dihasilkan.
- Menggunakan:
    - `allowedTools` untuk menentukan alat mana yang dapat digunakan model selama generasi. Dalam kasus ini, kami mengizinkan alat `ideaGenerator` dan `marketAnalyzer` untuk membantu menghasilkan ide aplikasi kreatif.
    - `frequencyPenalty` dan `presencePenalty` untuk mengontrol pengulangan dan keberagaman dalam keluaran.
    - `temperature` untuk mengontrol keacakan keluaran, di mana nilai lebih tinggi menghasilkan respons yang lebih kreatif.
    - `top_p` untuk membatasi pemilihan token pada token yang menyumbang massa probabilitas kumulatif teratas, meningkatkan kualitas teks yang dihasilkan.
    - `top_k` untuk membatasi model pada K token paling mungkin, yang dapat membantu menghasilkan respons yang lebih koheren.
    - `frequencyPenalty` dan `presencePenalty` untuk mengurangi pengulangan dan mendorong keberagaman dalam teks yang dihasilkan.

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

Dalam kode sebelumnya kami telah:

- Menginisialisasi klien MCP dengan URL server dan API key.
- Mengonfigurasi dua set parameter sampling: satu untuk tugas kreatif dan satu lagi untuk tugas faktual.
- Mengirim permintaan dengan konfigurasi ini, memungkinkan model menggunakan alat tertentu untuk setiap tugas.
- Mencetak respons yang dihasilkan untuk menunjukkan efek dari parameter sampling yang berbeda.
- Menggunakan `allowedTools` untuk menentukan alat mana yang dapat digunakan model selama generasi. Dalam kasus ini, kami mengizinkan `ideaGenerator` dan `environmentalImpactTool` untuk tugas kreatif, serta `factChecker` dan `dataAnalysisTool` untuk tugas faktual.
- Menggunakan `temperature` untuk mengontrol keacakan keluaran, di mana nilai lebih tinggi menghasilkan respons yang lebih kreatif.
- Menggunakan `top_p` untuk membatasi pemilihan token pada token yang menyumbang massa probabilitas kumulatif teratas, meningkatkan kualitas teks yang dihasilkan.
- Menggunakan `frequencyPenalty` dan `presencePenalty` untuk mengurangi pengulangan dan mendorong keberagaman dalam keluaran.
- Menggunakan `top_k` untuk membatasi model pada K token paling mungkin, yang dapat membantu menghasilkan respons yang lebih koheren.

---

## Sampling Deterministik

Untuk aplikasi yang membutuhkan keluaran konsisten, sampling deterministik memastikan hasil yang dapat direproduksi. Caranya adalah dengan menggunakan seed acak tetap dan mengatur temperature ke nol.

Mari kita lihat contoh implementasi di bawah ini untuk mendemonstrasikan sampling deterministik dalam berbagai bahasa pemrograman.

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

Dalam kode sebelumnya kami telah:

- Membuat klien MCP dengan URL server yang ditentukan.
- Mengonfigurasi dua permintaan dengan prompt yang sama, seed tetap, dan temperature nol.
- Mengirim kedua permintaan dan mencetak teks yang dihasilkan.
- Menunjukkan bahwa respons identik karena sifat deterministik konfigurasi sampling (seed dan temperature sama).
- Menggunakan `setSeed` untuk menentukan seed acak tetap, memastikan model menghasilkan keluaran yang sama untuk input yang sama setiap kali.
- Mengatur `temperature` ke nol untuk memastikan determinisme maksimum, artinya model selalu memilih token berikutnya yang paling mungkin tanpa keacakan.

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

Dalam kode sebelumnya kami telah:

- Menginisialisasi klien MCP dengan URL server.
- Mengonfigurasi dua permintaan dengan prompt yang sama, seed tetap, dan temperature nol.
- Mengirim kedua permintaan dan mencetak teks yang dihasilkan.
- Menunjukkan bahwa respons identik karena sifat deterministik konfigurasi sampling (seed dan temperature sama).
- Menggunakan `seed` untuk menentukan seed acak tetap, memastikan model menghasilkan keluaran yang sama untuk input yang sama setiap kali.
- Mengatur `temperature` ke nol untuk memastikan determinisme maksimum, artinya model selalu memilih token berikutnya yang paling mungkin tanpa keacakan.
- Menggunakan seed berbeda untuk permintaan ketiga untuk menunjukkan bahwa mengubah seed menghasilkan keluaran berbeda, meskipun prompt dan temperature sama.

---

## Konfigurasi Sampling Dinamis

Sampling cerdas menyesuaikan parameter berdasarkan konteks dan kebutuhan setiap permintaan. Ini berarti menyesuaikan parameter seperti temperature, top_p, dan penalti secara dinamis berdasarkan jenis tugas, preferensi pengguna, atau kinerja historis.

Mari kita lihat cara mengimplementasikan sampling dinamis dalam berbagai bahasa pemrograman.

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

Dalam kode sebelumnya kami telah:

- Membuat kelas `DynamicSamplingService` yang mengelola sampling adaptif.
- Mendefinisikan preset sampling untuk berbagai jenis tugas (kreatif, faktual, kode, analitis).
- Memilih preset sampling dasar berdasarkan jenis tugas.
- Menyesuaikan parameter sampling berdasarkan preferensi pengguna, seperti tingkat kreativitas dan keberagaman.
- Mengirim permintaan dengan parameter sampling yang dikonfigurasi secara dinamis.
- Mengembalikan teks yang dihasilkan bersama dengan parameter sampling dan jenis tugas untuk transparansi.
- Menggunakan `temperature` untuk mengontrol keacakan keluaran, di mana nilai lebih tinggi menghasilkan respons yang lebih kreatif.
- Menggunakan `top_p` untuk membatasi pemilihan token pada token yang menyumbang massa probabilitas kumulatif teratas, meningkatkan kualitas teks yang dihasilkan.
- Menggunakan `frequency_penalty` untuk mengurangi pengulangan dan mendorong keberagaman dalam keluaran.
- Menggunakan `user_preferences` untuk memungkinkan kustomisasi parameter sampling berdasarkan tingkat kreativitas dan keberagaman yang ditentukan pengguna.
- Menggunakan `task_type` untuk menentukan strategi sampling yang sesuai untuk permintaan, memungkinkan respons yang lebih disesuaikan berdasarkan sifat tugas.
- Menggunakan metode `send_request` untuk mengirim prompt dengan parameter sampling yang dikonfigurasi, memastikan model menghasilkan teks sesuai kebutuhan yang ditentukan.
- Menggunakan `generated_text` untuk mengambil respons model, yang kemudian dikembalikan bersama parameter sampling dan jenis tugas untuk analisis atau tampilan lebih lanjut.
- Menggunakan fungsi `min` dan `max` untuk memastikan preferensi pengguna berada dalam rentang valid, mencegah konfigurasi sampling yang tidak valid.

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

Dalam kode sebelumnya kami telah:

- Membuat kelas `AdaptiveSamplingManager` yang mengelola sampling dinamis berdasarkan jenis tugas dan preferensi pengguna.
- Mendefinisikan profil sampling untuk berbagai jenis tugas (kreatif, faktual, kode, percakapan).
- Mengimplementasikan metode untuk mendeteksi jenis tugas dari prompt menggunakan heuristik sederhana.
- Menghitung parameter sampling berdasarkan jenis tugas yang terdeteksi dan preferensi pengguna.
- Menerapkan penyesuaian yang dipelajari berdasarkan kinerja historis untuk mengoptimalkan parameter sampling.
- Mencatat kinerja untuk penyesuaian di masa depan, memungkinkan sistem belajar dari interaksi sebelumnya.
- Mengirim permintaan dengan parameter sampling yang dikonfigurasi secara dinamis dan mengembalikan teks yang dihasilkan bersama parameter yang diterapkan dan jenis tugas yang terdeteksi.
- Menggunakan:
    - `userPreferences` untuk memungkinkan kustomisasi parameter sampling berdasarkan tingkat kreativitas, presisi, dan konsistensi yang ditentukan pengguna.
    - `detectTaskType` untuk menentukan sifat tugas berdasarkan prompt, memungkinkan respons yang lebih disesuaikan.
    - `recordPerformance` untuk mencatat kinerja respons yang dihasilkan, memungkinkan sistem beradaptasi dan meningkat seiring waktu.
    - `applyLearnedAdjustments` untuk memodifikasi parameter sampling berdasarkan kinerja historis, meningkatkan kemampuan model menghasilkan respons berkualitas tinggi.
    - `generateResponse` untuk mengenkapsulasi seluruh proses menghasilkan respons dengan sampling adaptif, memudahkan pemanggilan dengan prompt dan konteks berbeda.
    - `allowedTools` untuk menentukan alat mana yang dapat digunakan model selama generasi, memungkinkan respons yang lebih kontekstual.
    - `feedbackScore` untuk memungkinkan pengguna memberikan umpan balik tentang kualitas respons yang dihasilkan, yang dapat digunakan untuk menyempurnakan kinerja model dari waktu ke waktu.
    - `performanceHistory` untuk menyimpan catatan interaksi sebelumnya, memungkinkan sistem belajar dari keberhasilan dan kegagalan sebelumnya.
    - `getSamplingParameters` untuk menyesuaikan parameter sampling secara dinamis berdasarkan konteks permintaan, memungkinkan perilaku model yang lebih fleksibel dan responsif.
    - `detectTaskType` untuk mengklasifikasikan tugas berdasarkan prompt, memungkinkan sistem menerapkan strategi sampling yang sesuai untuk berbagai jenis permintaan.
    - `samplingProfiles` untuk mendefinisikan konfigurasi sampling dasar untuk berbagai jenis tugas, memungkinkan penyesuaian cepat berdasarkan sifat permintaan.

---

## Selanjutnya

- [5.7 Scaling](../mcp-scaling/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.