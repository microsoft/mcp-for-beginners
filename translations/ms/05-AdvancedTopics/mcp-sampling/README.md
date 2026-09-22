> [!WARNING]
> Sampling tidak lagi digunakan dalam MCP `2026-07-28`. Pelajaran ini dikekalkan untuk
> pelaksanaan warisan. Pelayan baru harus berintegrasi terus dengan API pembekal LLM.


# Sampling dalam Protokol Konteks Model

> Sampling kekal dalam spesifikasi `2026-07-28` untuk keserasian dan layak untuk
> dikeluarkan dalam semakan pertama yang dikeluarkan pada atau selepas 28 Julai,
> 2027. Contoh dalam pelajaran ini mungkin menggunakan API SDK yang melaksanakan `2025-11-25`.
> Lihat [Apa yang Berubah dalam MCP: Spesifikasi 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

Dalam pelaksanaan MCP warisan, Sampling membenarkan pelayan meminta penyelesaian LLM
melalui klien. Pelajaran ini menerangkan aliran protokol yang usang
untuk keserasian dan kerja migrasi.

## Pengenalan

Dalam pelajaran ini, kita akan meneroka cara mengkonfigurasi parameter sampling dalam permintaan MCP dan memahami mekanik protokol asas sampling.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:

- Memahami parameter sampling utama yang tersedia dalam MCP.
- Mengkonfigurasi parameter sampling untuk pelbagai kes penggunaan.
- Melaksanakan sampling deterministik untuk hasil yang boleh dihasilkan semula.
- Melaraskan parameter sampling secara dinamik berdasarkan konteks dan keutamaan pengguna.
- Menerapkan strategi sampling untuk meningkatkan prestasi model dalam pelbagai senario.
- Memahami bagaimana sampling berfungsi dalam aliran klien-pelayan MCP.

## Cara Sampling Berfungsi dalam MCP

Aliran sampling dalam MCP mengikuti langkah-langkah berikut:

1. Pelayan menghantar permintaan `sampling/createMessage` kepada klien
2. Klien menyemak permintaan tersebut dan boleh mengubahnya
3. Klien membuat sampling dari LLM
4. Klien menyemak hasil penyelesaian
5. Klien mengembalikan hasil kepada pelayan

Reka bentuk dengan manusia dalam gelung ini memastikan pengguna mengekalkan kawalan ke atas apa yang LLM lihat dan hasilkan.

## Gambaran Keseluruhan Parameter Sampling

MCP mentakrifkan parameter sampling berikut yang boleh dikonfigurasi dalam permintaan klien:

| Parameter | Penerangan | Julat Tipikal |
|-----------|-------------|---------------|
| `temperature` | Mengawal kebarangkalian dalam pemilihan token | 0.0 - 1.0 |
| `maxTokens` | Bilangan maksimum token untuk dijana | Nilai integer |
| `stopSequences` | Rangkaian tersuai yang menghentikan penjanaan apabila ditemui | Array string |
| `metadata` | Parameter tambahan khusus pembekal | Objek JSON |

Ramai pembekal LLM menyokong parameter tambahan melalui medan `metadata`, yang mungkin termasuk:

| Parameter Sambungan Umum | Penerangan | Julat Tipikal |
|-----------|-------------|---------------|
| `top_p` | Sampling nucleus - mengehadkan token kepada kebarangkalian kumulatif teratas | 0.0 - 1.0 |
| `top_k` | Mengehadkan pemilihan token kepada pilihan K teratas | 1 - 100 |
| `presence_penalty` | Memberi penalti pada token berdasarkan kehadirannya dalam teks setakat ini | -2.0 - 2.0 |
| `frequency_penalty` | Memberi penalti pada token berdasarkan kekerapan mereka dalam teks setakat ini | -2.0 - 2.0 |
| `seed` | Benih rawak tertentu untuk hasil boleh dihasilkan semula | Nilai integer |

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

## Kawalan Manusia dalam Gelung

Sampling MCP direka dengan pengawasan manusia dalam fikiran:


- **Untuk prompt**:
  - Pelanggan harus menunjukkan prompt yang dicadangkan kepada pengguna
  - Pengguna harus dapat mengubah atau menolak prompt
  - Prompt sistem boleh ditapis atau diubahsuai
  - Penyertaan konteks dikawal oleh pelanggan

- **Untuk penyelesaian**:
  - Pelanggan harus menunjukkan penyelesaian kepada pengguna
  - Pengguna harus dapat mengubah atau menolak penyelesaian
  - Pelanggan boleh menapis atau mengubah penyelesaian
  - Pengguna mengawal model yang digunakan

Dengan prinsip-prinsip ini dalam fikiran, mari kita lihat bagaimana untuk melaksanakan pensampelan dalam pelbagai bahasa pengaturcaraan, dengan fokus pada parameter yang biasanya disokong oleh pembekal LLM.

## Pertimbangan Keselamatan

Apabila melaksanakan pensampelan dalam MCP, pertimbangkan amalan terbaik keselamatan ini:

- **Sahkan semua kandungan mesej** sebelum menghantarnya ke pelanggan
- **Bersihkan maklumat sensitif** dari prompt dan penyelesaian
- **Laksanakan had kadar** untuk mengelakkan penyalahgunaan
- **Pantau penggunaan pensampelan** untuk corak yang luar biasa
- **Menyulitkan data semasa transit** menggunakan protokol selamat
- **Urus privasi data pengguna** mengikut peraturan yang berkaitan
- **Audit permintaan pensampelan** untuk kepatuhan dan keselamatan
- **Kawal pendedahan kos** dengan had yang sesuai
- **Laksanakan waktu tamat** untuk permintaan pensampelan
- **Urus kesilapan model dengan baik** menggunakan fallback yang sesuai

Parameter pensampelan membolehkan penyesuaian tingkah laku model bahasa untuk mencapai keseimbangan yang diingini antara output yang deterministik dan kreatif.

Mari kita lihat cara mengkonfigurasi parameter ini dalam pelbagai bahasa pengaturcaraan.

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

Dalam kod sebelumnya kami telah:

- Mencipta pelanggan MCP dengan URL server tertentu.
- Mengkonfigurasi permintaan dengan parameter pensampelan seperti `temperature`, `top_p`, dan `top_k`.
- Menghantar permintaan dan mencetak teks yang dijana.
- Menggunakan:
    - `allowedTools` untuk menentukan alat mana yang boleh digunakan model semasa penjanaan. Dalam kes ini, kami membenarkan alat `ideaGenerator` dan `marketAnalyzer` untuk membantu menjana idea aplikasi kreatif.
    - `frequencyPenalty` dan `presencePenalty` untuk mengawal pengulangan dan kepelbagaian dalam output.
    - `temperature` untuk mengawal keacakkan output, di mana nilai yang lebih tinggi menghasilkan respons yang lebih kreatif.
    - `top_p` untuk mengehadkan pilihan token kepada yang menyumbang kepada jisim kebarangkalian kumulatif tertinggi, meningkatkan kualiti teks yang dijana.
    - `top_k` untuk mengehadkan model kepada token paling probable teratas K, yang boleh membantu menjana respons yang lebih koheren.
    - `frequencyPenalty` dan `presencePenalty` untuk mengurangkan pengulangan dan menggalakkan kepelbagaian dalam teks yang dijana.

# [JavaScript](#tab/javascript)

```javascript
// Contoh JavaScript: Konfigurasi pensampelan Suhu dan Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Memulakan klien MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Konfigurasikan permintaan dengan parameter pensampelan yang berbeza
  const creativeSampling = {
    temperature: 0.9,    // Suhu yang lebih tinggi = lebih rawak/berkreativiti
    topP: 0.92,          // Pertimbangkan token dengan jisim kebarangkalian 92% teratas
    frequencyPenalty: 0.6, // Kurangkan pengulangan susunan token
    presencePenalty: 0.4   // Beri penalti kepada token yang telah muncul dalam teks setakat ini
  };
  
  const factualSampling = {
    temperature: 0.2,    // Suhu yang lebih rendah = lebih deterministik/berasas fakta
    topP: 0.85,          // Pemilihan token yang sedikit lebih fokus
    frequencyPenalty: 0.2, // Penalti pengulangan yang minimum
    presencePenalty: 0.1   // Penalti kehadiran yang minimum
  };
  
  try {
    // Hantar dua permintaan dengan konfigurasi pensampelan yang berbeza
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

Dalam kod sebelumnya kami telah:

- Memulakan pelanggan MCP dengan URL server dan kekunci API.
- Mengkonfigurasi dua set parameter pensampelan: satu untuk tugasan kreatif dan satu lagi untuk tugasan faktual.
- Menghantar permintaan dengan konfigurasi ini, membenarkan model menggunakan alat tertentu untuk setiap tugasan.
- Mencetak respons yang dijana untuk menunjukkan kesan parameter pensampelan yang berbeza.
- Menggunakan `allowedTools` untuk menentukan alat yang boleh digunakan model semasa penjanaan. Dalam kes ini, kami membenarkan `ideaGenerator` dan `environmentalImpactTool` untuk tugasan kreatif, serta `factChecker` dan `dataAnalysisTool` untuk tugasan faktual.
- Menggunakan `temperature` untuk mengawal keacakkan output, di mana nilai yang lebih tinggi menghasilkan respons yang lebih kreatif.

- Menggunakan `top_p` untuk mengehadkan pemilihan token kepada mereka yang menyumbang kepada jumlah kebarangkalian kumulatif teratas, meningkatkan kualiti teks yang dijana.
- Menggunakan `frequencyPenalty` dan `presencePenalty` untuk mengurangkan pengulangan dan menggalakkan kepelbagaian dalam output.
- Menggunakan `top_k` untuk mengehadkan model kepada K token paling berkemungkinan, yang boleh membantu menghasilkan respons yang lebih koheren.

---

## Pensampelan Deterministik

Untuk aplikasi yang memerlukan output yang konsisten, pensampelan deterministik memastikan keputusan yang boleh dihasilkan semula. Caranya adalah dengan menggunakan benih rawak tetap dan menetapkan suhu kepada sifar.

Mari lihat contoh pelaksanaan di bawah untuk menunjukkan pensampelan deterministik dalam pelbagai bahasa pengaturcaraan.

# [Java](#tab/java)

```java
// Contoh Java: Respons deterministik dengan benih tetap
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Menggunakan benih tetap untuk hasil deterministik
        
        // Permintaan pertama dengan benih tetap
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Suhu sifar untuk determinisme maksimum
            .build();
            
        // Permintaan kedua dengan benih yang sama
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Jalankan kedua-dua permintaan
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Respons mesti sama kerana benih dan suhu=0 yang sama
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Dalam kod sebelumnya kami telah:

- Membuat klien MCP dengan URL pelayan yang ditetapkan.
- Mengkonfigurasi dua permintaan dengan isyarat yang sama, benih tetap, dan suhu sifar.
- Menghantar kedua-dua permintaan dan mencetak teks yang dihasilkan.
- Menunjukkan bahawa respons adalah sama kerana sifat deterministik konfigurasi pensampelan (benih dan suhu yang sama).
- Menggunakan `setSeed` untuk menetapkan benih rawak tetap, memastikan model menghasilkan output yang sama untuk input yang sama setiap masa.
- Menetapkan `temperature` kepada sifar untuk memastikan determinisme maksimum, bermakna model akan sentiasa memilih token seterusnya yang paling berkemungkinan tanpa kebarangkalian rawak.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Contoh JavaScript: Respons deterministik dengan kawalan benih
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Permintaan pertama dengan benih tetap
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Suhu sifar untuk determinisme maksimum
    });
    
    // Permintaan kedua dengan benih dan suhu yang sama
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Permintaan ketiga dengan benih berbeza tetapi suhu yang sama
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

Dalam kod sebelumnya kami telah:

- Memulakan klien MCP dengan URL pelayan.
- Mengkonfigurasi dua permintaan dengan isyarat yang sama, benih tetap, dan suhu sifar.
- Menghantar kedua-dua permintaan dan mencetak teks yang dihasilkan.
- Menunjukkan bahawa respons adalah sama kerana sifat deterministik konfigurasi pensampelan (benih dan suhu yang sama).
- Menggunakan `seed` untuk menetapkan benih rawak tetap, memastikan model menghasilkan output yang sama untuk input yang sama setiap masa.
- Menetapkan `temperature` kepada sifar untuk memastikan determinisme maksimum, bermakna model akan sentiasa memilih token seterusnya yang paling berkemungkinan tanpa kebarangkalian rawak.
- Menggunakan benih yang berbeza untuk permintaan ketiga untuk menunjukkan bahawa menukar benih menghasilkan output yang berbeza, walaupun dengan isyarat dan suhu yang sama.

---

## Konfigurasi Pensampelan Dinamik

Pensampelan pintar menyesuaikan parameter berdasarkan konteks dan keperluan setiap permintaan. Ini bermakna menyesuaikan parameter secara dinamik seperti suhu, top_p, dan penalti berdasarkan jenis tugas, keutamaan pengguna, atau prestasi sejarah.

Mari lihat bagaimana melaksanakan pensampelan dinamik dalam pelbagai bahasa pengaturcaraan.

# [Python](#tab/python)

```python
# Contoh Python: Pensampelan dinamik berdasarkan konteks permintaan
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Tetapkan pratetap pensampelan untuk jenis tugas yang berbeza
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Pilih pratetap asas
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Laraskan berdasarkan keutamaan pengguna jika disediakan
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Skala suhu berdasarkan keutamaan kreativiti (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Laraskan top_p berdasarkan kepelbagaian respons yang dikehendaki
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Cipta dan hantar permintaan dengan parameter pensampelan tersuai
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Kembalikan respons dengan metadata pensampelan untuk ketelusan
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Dalam kod sebelumnya kami telah:

- Membuat kelas `DynamicSamplingService` yang mengurus pensampelan adaptif.
- Mendefinisikan pratetap pensampelan untuk jenis tugas yang berbeza (kreatif, faktual, kod, analitik).
- Memilih pratetap pensampelan asas berdasarkan jenis tugas.
- Melaraskan parameter pensampelan berdasarkan keutamaan pengguna, seperti tahap kreativiti dan kepelbagaian.
- Menghantar permintaan dengan parameter pensampelan yang dikonfigurasikan secara dinamik.
- Memulangkan teks yang dijana bersama dengan parameter pensampelan yang digunakan dan jenis tugas untuk ketelusan.
- Menggunakan `temperature` untuk mengawal kebarangkalian rawak output, di mana nilai lebih tinggi membawa kepada respons yang lebih kreatif.
- Menggunakan `top_p` untuk mengehadkan pemilihan token kepada mereka yang menyumbang kepada jumlah kebarangkalian kumulatif teratas, meningkatkan kualiti teks yang dijana.
- Menggunakan `frequency_penalty` untuk mengurangkan pengulangan dan menggalakkan kepelbagaian dalam output.
- Menggunakan `user_preferences` untuk membenarkan penyesuaian parameter pensampelan berdasarkan tahap kreativiti dan kepelbagaian yang ditetapkan oleh pengguna.
- Menggunakan `task_type` untuk menentukan strategi pensampelan yang sesuai untuk permintaan, membolehkan respons yang lebih disesuaikan berdasarkan sifat tugas.
- Menggunakan kaedah `send_request` untuk menghantar isyarat dengan parameter pensampelan yang dikonfigurasikan, memastikan model menjana teks mengikut keperluan yang ditetapkan.
- Menggunakan `generated_text` untuk mendapatkan respons model, yang kemudian dipulangkan bersama parameter pensampelan dan jenis tugas untuk analisis atau paparan selanjutnya.
- Menggunakan fungsi `min` dan `max` untuk memastikan keutamaan pengguna dikekang dalam julat yang sah, menghalang konfigurasi pensampelan yang tidak sah.

# [JavaScript Dynamic](#tab/javascript-dynamic)

```javascript
// Contoh JavaScript: Konfigurasi pensampelan dinamik berdasarkan konteks pengguna
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Tetapkan profil pensampelan asas
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Jejak prestasi sejarah
    this.performanceHistory = [];
  }
  
  // Kenal pasti jenis tugasan dari arahan
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Pengesanan heuristik mudah - boleh dipertingkatkan dengan klasifikasi ML
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
    
    // Lalai kepada perbualan jika tiada jenis jelas dikesan
    return 'conversational';
  }
  
  // Kira parameter pensampelan berdasarkan konteks dan keutamaan pengguna
  getSamplingParameters(prompt, context = {}) {
    // Kenal pasti jenis tugasan
    const taskType = this.detectTaskType(prompt, context);
    
    // Dapatkan profil asas
    let params = {...this.samplingProfiles[taskType]};
    
    // Laraskan berdasarkan keutamaan pengguna
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Skala dari 1-10 ke julat suhu yang sesuai
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Ketepatan lebih tinggi bermakna topP lebih rendah (pemilihan lebih fokus)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Konsistensi lebih tinggi bermakna penalti lebih rendah
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Terapkan penyesuaian yang dipelajari dari sejarah prestasi
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Logik adaptif mudah - boleh dipertingkatkan dengan algoritma lebih sofistikated
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Hanya pertimbangkan sejarah terkini
    
    if (relevantHistory.length > 0) {
      // Kira purata skor prestasi
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Jika prestasi di bawah had, laraskan parameter
      if (avgScore < 0.7) {
        // Penyesuaian sedikit ke arah nilai yang lebih selamat
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Rekod prestasi untuk penyesuaian masa depan
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Penarafan 0-1 bagi kualiti jawapan
    });
    
    // Hadkan saiz sejarah
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Dapatkan parameter pensampelan yang dioptimumkan
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Hantar permintaan dengan parameter yang dioptimumkan
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Jika pengguna memberikan maklum balas, rekod untuk pengoptimuman masa depan
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

// Contoh penggunaan
async function demonstrateAdaptiveSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const samplingManager = new AdaptiveSamplingManager(client);
  
  try {
    // Tugasan kreatif dengan keutamaan pengguna tersuai
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Kreativiti tinggi (1-10)
          consistency: 3  // Konsistensi rendah (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Tugasan penjanaan kod
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Kreativiti rendah
          precision: 8,   // Ketepatan tinggi
          consistency: 9  // Konsistensi tinggi
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

Dalam kod sebelumnya kami telah:

- Membuat kelas `AdaptiveSamplingManager` yang mengurus pensampelan dinamik berdasarkan jenis tugas dan keutamaan pengguna.
- Mendefinisikan profil pensampelan untuk jenis tugas yang berbeza (kreatif, faktual, kod, perbualan).
- Melaksanakan kaedah untuk mengesan jenis tugas daripada isyarat menggunakan heuristik mudah.
- Mengira parameter pensampelan berdasarkan jenis tugas yang dikesan dan keutamaan pengguna.
- Menerapkan pelarasan yang dipelajari berdasarkan prestasi sejarah untuk mengoptimumkan parameter pensampelan.
- Merekodkan prestasi untuk pelarasan masa depan, membolehkan sistem belajar daripada interaksi lepas.
- Menghantar permintaan dengan parameter pensampelan yang dikonfigurasikan secara dinamik dan memulangkan teks yang dijana bersama parameter yang digunakan dan jenis tugas yang dikesan.
- Menggunakan:
    - `userPreferences` untuk membenarkan penyesuaian parameter pensampelan berdasarkan tahap kreativiti, ketepatan, dan konsistensi yang ditetapkan pengguna.
    - `detectTaskType` untuk menentukan sifat tugas berdasarkan isyarat, membolehkan respons yang lebih disesuaikan.
    - `recordPerformance` untuk merekod prestasi respons yang dijana, membolehkan sistem menyesuaikan dan memperbaiki dari masa ke masa.
    - `applyLearnedAdjustments` untuk mengubah suai parameter pensampelan berdasarkan prestasi sejarah, meningkatkan keupayaan model untuk menghasilkan respons berkualiti tinggi.
    - `generateResponse` untuk merangkum keseluruhan proses menjana respons dengan pensampelan adaptif, memudahkan panggilan dengan isyarat dan konteks yang berbeza.
    - `allowedTools` untuk menentukan alat yang boleh digunakan model semasa penjanaan, membolehkan respons yang lebih berorientasikan konteks.
    - `feedbackScore` untuk membenarkan pengguna memberi maklum balas mengenai kualiti respons yang dijana, yang boleh digunakan untuk menambah baik prestasi model dari masa ke masa.
    - `performanceHistory` untuk menyimpan rekod interaksi lepas, membolehkan sistem belajar daripada kejayaan dan kegagalan terdahulu.
    - `getSamplingParameters` untuk menyesuaikan parameter pensampelan secara dinamik berdasarkan konteks permintaan, membolehkan tingkah laku model yang lebih fleksibel dan responsif.
    - `detectTaskType` untuk mengklasifikasikan tugas berdasarkan isyarat, membolehkan sistem menggunakan strategi pensampelan yang sesuai untuk pelbagai jenis permintaan.
    - `samplingProfiles` untuk mendefinisikan konfigurasi pensampelan asas untuk jenis tugas yang berbeza, membolehkan pelarasan pantas berdasarkan sifat permintaan.

---

## Apa seterusnya

- [5.7 Skala](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->