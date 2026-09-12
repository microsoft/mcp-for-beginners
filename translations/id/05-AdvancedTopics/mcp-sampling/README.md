> [!WARNING]
> Sampling tidak lagi digunakan (deprecated) di MCP `2026-07-28`. Pelajaran ini dipertahankan untuk
> implementasi legacy. Server baru harus terintegrasi langsung dengan API penyedia LLM.


# Sampling dalam Model Context Protocol

> Sampling tetap ada di spesifikasi `2026-07-28` untuk kompatibilitas dan
> berpotensi dihapus dalam revisi pertama yang dirilis pada atau setelah 28 Juli,
> 2027. Contoh dalam pelajaran ini mungkin menggunakan API SDK yang mengimplementasikan `2025-11-25`.
> Lihat [Apa yang Berubah dalam MCP: Spesifikasi 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md).

Dalam implementasi MCP legacy, Sampling memungkinkan server meminta penyelesaian dari LLM
melalui klien. Pelajaran ini menjelaskan alur protokol yang sudah tidak digunakan tersebut
untuk kompatibilitas dan pekerjaan migrasi.

## Pendahuluan

Dalam pelajaran ini, kita akan menjelajahi bagaimana mengonfigurasi parameter sampling dalam permintaan MCP dan memahami mekanisme protokol sampling yang mendasarinya.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Memahami parameter sampling utama yang tersedia di MCP.
- Mengonfigurasi parameter sampling untuk berbagai kasus penggunaan.
- Mengimplementasikan sampling deterministik untuk hasil yang dapat direproduksi.
- Menyesuaikan parameter sampling secara dinamis berdasarkan konteks dan preferensi pengguna.
- Menerapkan strategi sampling untuk meningkatkan kinerja model dalam berbagai skenario.
- Memahami cara kerja sampling dalam alur klien-server MCP.

## Cara Kerja Sampling di MCP

Alur sampling di MCP mengikuti langkah-langkah berikut:

1. Server mengirimkan permintaan `sampling/createMessage` ke klien
2. Klien meninjau permintaan dan dapat memodifikasinya
3. Klien melakukan sampling dari LLM
4. Klien meninjau hasil penyelesaian
5. Klien mengembalikan hasil ke server

Desain human-in-the-loop ini memastikan pengguna mempertahankan kontrol atas apa yang dilihat dan dihasilkan oleh LLM.

## Ikhtisar Parameter Sampling

MCP mendefinisikan parameter sampling berikut yang dapat dikonfigurasi dalam permintaan klien:

| Parameter | Deskripsi | Rentang Umum |
|-----------|-------------|---------------|
| `temperature` | Mengontrol randomness dalam pemilihan token | 0.0 - 1.0 |
| `maxTokens` | Jumlah maksimum token yang dihasilkan | Nilai integer |
| `stopSequences` | Urutan khusus yang menghentikan generasi saat ditemui | Array string |
| `metadata` | Parameter tambahan spesifik penyedia | Objek JSON |

Banyak penyedia LLM mendukung parameter tambahan melalui bidang `metadata`, yang mungkin meliputi:

| Parameter Ekstensi Umum | Deskripsi | Rentang Umum |
|-----------|-------------|---------------|
| `top_p` | Nucleus sampling - membatasi token ke probabilitas kumulatif teratas | 0.0 - 1.0 |
| `top_k` | Membatasi pemilihan token ke opsi K teratas | 1 - 100 |
| `presence_penalty` | Memberi penalti pada token berdasarkan kemunculannya dalam teks sejauh ini | -2.0 - 2.0 |
| `frequency_penalty` | Memberi penalti pada token berdasarkan frekuensinya dalam teks sejauh ini | -2.0 - 2.0 |
| `seed` | Benih acak spesifik untuk hasil yang dapat direproduksi | Nilai integer |

## Contoh Format Permintaan

Berikut adalah contoh permintaan sampling dari klien di MCP:

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

## Format Respon

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

Sampling MCP dirancang dengan pengawasan manusia dalam pikiran:

- **Untuk prompt**:
  - Klien harus menampilkan prompt yang diusulkan kepada pengguna
  - Pengguna harus dapat memodifikasi atau menolak prompt
  - Prompt sistem dapat disaring atau dimodifikasi
  - Penyertaan konteks dikendalikan oleh klien

- **Untuk penyelesaian**:
  - Klien harus menampilkan penyelesaian kepada pengguna
  - Pengguna harus dapat memodifikasi atau menolak penyelesaian
  - Klien dapat menyaring atau memodifikasi penyelesaian
  - Pengguna mengontrol model mana yang digunakan

Dengan prinsip-prinsip ini, mari kita lihat bagaimana mengimplementasikan sampling dalam berbagai bahasa pemrograman, fokus pada parameter yang umum didukung di penyedia LLM.

## Pertimbangan Keamanan

Saat mengimplementasikan sampling di MCP, pertimbangkan praktik terbaik keamanan berikut:

- **Validasi semua isi pesan** sebelum mengirim ke klien
- **Sanitasi informasi sensitif** dari prompt dan penyelesaian
- **Terapkan batas laju (rate limits)** untuk mencegah penyalahgunaan
- **Pantau penggunaan sampling** untuk pola yang tidak biasa
- **Enkripsi data saat transit** menggunakan protokol aman
- **Tangani privasi data pengguna** sesuai regulasi yang relevan
- **Audit permintaan sampling** untuk kepatuhan dan keamanan
- **Kontrol eksposur biaya** dengan batasan yang sesuai
- **Terapkan batas waktu (timeouts)** untuk permintaan sampling
- **Tangani kesalahan model dengan cara yang baik** menggunakan fallback yang tepat

Parameter sampling memungkinkan penyesuaian perilaku model bahasa untuk mencapai keseimbangan yang diinginkan antara keluaran deterministik dan kreatif.

Mari kita lihat cara mengonfigurasi parameter ini dalam berbagai bahasa pemrograman.

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

Dalam kode sebelumnya kita telah:

- Membuat klien MCP dengan URL server tertentu.
- Mengonfigurasi permintaan dengan parameter sampling seperti `temperature`, `top_p`, dan `top_k`.
- Mengirim permintaan dan mencetak teks yang dihasilkan.
- Menggunakan:
    - `allowedTools` untuk menentukan alat mana yang dapat digunakan model selama generasi. Dalam kasus ini, kami mengizinkan alat `ideaGenerator` dan `marketAnalyzer` untuk membantu menghasilkan ide aplikasi kreatif.
    - `frequencyPenalty` dan `presencePenalty` untuk mengontrol pengulangan dan keberagaman dalam keluaran.
    - `temperature` untuk mengontrol randomness output, di mana nilai lebih tinggi menghasilkan respons yang lebih kreatif.
    - `top_p` untuk membatasi pemilihan token hanya pada token yang menyumbang massa probabilitas kumulatif teratas, meningkatkan kualitas teks yang dihasilkan.
    - `top_k` untuk membatasi model pada token K teratas yang paling mungkin, yang dapat membantu menghasilkan respons yang lebih koheren.
    - `frequencyPenalty` dan `presencePenalty` untuk mengurangi pengulangan dan mendorong keberagaman teks yang dihasilkan.

# [JavaScript](#tab/javascript)

```javascript
// Contoh JavaScript: Konfigurasi Suhu dan Pengambilan Sampel Top-P
const { McpClient } = require('@mcp/client');

async function demonstrateSampling() {
  // Inisialisasi klien MCP
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com',
    apiKey: process.env.MCP_API_KEY
  });
  
  // Konfigurasikan permintaan dengan parameter sampling berbeda
  const creativeSampling = {
    temperature: 0.9,    // Suhu lebih tinggi = lebih banyak randomness/kreativitas
    topP: 0.92,          // Pertimbangkan token dengan massa probabilitas top 92%
    frequencyPenalty: 0.6, // Kurangi pengulangan urutan token
    presencePenalty: 0.4   // Beri penalti pada token yang sudah muncul dalam teks sejauh ini
  };
  
  const factualSampling = {
    temperature: 0.2,    // Suhu lebih rendah = lebih deterministik/faktual
    topP: 0.85,          // Pemilihan token yang sedikit lebih fokus
    frequencyPenalty: 0.2, // Penalti pengulangan minimal
    presencePenalty: 0.1   // Penalti kehadiran minimal
  };
  
  try {
    // Kirim dua permintaan dengan konfigurasi sampling berbeda
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

Dalam kode sebelumnya kita telah:

- Menginisialisasi klien MCP dengan URL server dan kunci API.
- Mengonfigurasi dua set parameter sampling: satu untuk tugas kreatif dan satu lagi untuk tugas faktual.
- Mengirim permintaan dengan konfigurasi ini, memungkinkan model menggunakan alat spesifik untuk setiap tugas.
- Mencetak respons yang dihasilkan untuk menunjukkan efek parameter sampling yang berbeda.
- Menggunakan `allowedTools` untuk menentukan alat mana yang dapat digunakan model selama generasi. Dalam kasus ini, kami mengizinkan `ideaGenerator` dan `environmentalImpactTool` untuk tugas kreatif, dan `factChecker` dan `dataAnalysisTool` untuk tugas faktual.
- Menggunakan `temperature` untuk mengontrol randomness output, di mana nilai lebih tinggi menghasilkan respons yang lebih kreatif.
- Menggunakan `top_p` untuk membatasi pemilihan token hanya pada token yang menyumbang massa probabilitas kumulatif teratas, meningkatkan kualitas teks yang dihasilkan.
- Menggunakan `frequencyPenalty` dan `presencePenalty` untuk mengurangi pengulangan dan mendorong keberagaman dalam output.
- Menggunakan `top_k` untuk membatasi model pada token K teratas yang paling mungkin, yang dapat membantu menghasilkan respons yang lebih koheren.

---

## Sampling Deterministik

Untuk aplikasi yang membutuhkan keluaran konsisten, sampling deterministik memastikan hasil yang dapat direproduksi. Cara kerjanya adalah dengan menggunakan benih acak tetap dan mengatur temperature menjadi nol.

Mari lihat contoh implementasi di bawah untuk mendemonstrasikan sampling deterministik dalam berbagai bahasa pemrograman.

# [Java](#tab/java)

```java
// Contoh Java: Respons deterministik dengan seed tetap
public class DeterministicSamplingExample {
    public void demonstrateDeterministicResponses() {
        McpClient client = new McpClient.Builder()
            .setServerUrl("https://mcp-server-example.com")
            .build();
            
        long fixedSeed = 12345; // Menggunakan seed tetap untuk hasil yang deterministik
        
        // Permintaan pertama dengan seed tetap
        McpRequest request1 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0) // Suhu nol untuk determinisme maksimal
            .build();
            
        // Permintaan kedua dengan seed yang sama
        McpRequest request2 = new McpRequest.Builder()
            .setPrompt("Generate a random number between 1 and 100")
            .setSeed(fixedSeed)
            .setTemperature(0.0)
            .build();
        
        // Eksekusi kedua permintaan
        McpResponse response1 = client.sendRequest(request1);
        McpResponse response2 = client.sendRequest(request2);
        
        // Respons harus identik karena seed yang sama dan suhu=0
        System.out.println("Response 1: " + response1.getGeneratedText());
        System.out.println("Response 2: " + response2.getGeneratedText());
        System.out.println("Are responses identical: " + 
            response1.getGeneratedText().equals(response2.getGeneratedText()));
    }
}
```

Dalam kode sebelumnya kita telah:

- Membuat klien MCP dengan URL server tertentu.
- Mengonfigurasi dua permintaan dengan prompt yang sama, benih tetap, dan temperature nol.
- Mengirim kedua permintaan dan mencetak teks yang dihasilkan.
- Menunjukkan bahwa respons identik karena sifat deterministik konfigurasi sampling (benih dan temperature sama).
- Menggunakan `setSeed` untuk menentukan benih acak tetap, memastikan model menghasilkan keluaran yang sama untuk input yang sama setiap saat.
- Mengatur `temperature` ke nol agar determinisme maksimal, berarti model selalu memilih token berikutnya yang paling mungkin tanpa randomness.

# [JavaScript](#tab/javascript-deterministic)

```javascript
// Contoh JavaScript: Respon deterministik dengan kontrol seed
const { McpClient } = require('@mcp/client');

async function deterministicSampling() {
  const client = new McpClient({
    serverUrl: 'https://mcp-server-example.com'
  });
  
  const fixedSeed = 12345;
  const prompt = "Generate a random password with 8 characters";
  
  try {
    // Permintaan pertama dengan seed tetap
    const response1 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0  // Suhu nol untuk determinisme maksimum
    });
    
    // Permintaan kedua dengan seed dan suhu yang sama
    const response2 = await client.sendPrompt(prompt, {
      seed: fixedSeed,
      temperature: 0.0
    });
    
    // Permintaan ketiga dengan seed berbeda tetapi suhu yang sama
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

Dalam kode sebelumnya kita telah:

- Menginisialisasi klien MCP dengan URL server.
- Mengonfigurasi dua permintaan dengan prompt yang sama, benih tetap, dan temperature nol.
- Mengirim kedua permintaan dan mencetak teks yang dihasilkan.
- Menunjukkan bahwa respons identik karena sifat deterministik konfigurasi sampling (benih dan temperature sama).
- Menggunakan `seed` untuk menentukan benih acak tetap, memastikan model menghasilkan keluaran yang sama untuk input yang sama setiap saat.
- Mengatur `temperature` ke nol agar determinisme maksimal, berarti model selalu memilih token berikutnya yang paling mungkin tanpa randomness.
- Menggunakan benih berbeda untuk permintaan ketiga untuk menunjukkan bahwa mengganti benih menghasilkan keluaran berbeda, meskipun prompt dan temperature sama.

---

## Konfigurasi Sampling Dinamis

Sampling cerdas menyesuaikan parameter berdasarkan konteks dan kebutuhan setiap permintaan. Ini berarti menyesuaikan parameter seperti temperature, top_p, dan penalti berdasarkan jenis tugas, preferensi pengguna, atau performa historis.

Mari lihat bagaimana mengimplementasikan sampling dinamis dalam berbagai bahasa pemrograman.

# [Python](#tab/python)

```python
# Contoh Python: Sampling dinamis berdasarkan konteks permintaan
class DynamicSamplingService:
    def __init__(self, mcp_client):
        self.client = mcp_client
        
    async def generate_with_adaptive_sampling(self, prompt, task_type, user_preferences=None):
        """Uses different sampling strategies based on task type and user preferences"""
        
        # Definisikan preset sampling untuk berbagai jenis tugas
        sampling_presets = {
            "creative": {"temperature": 0.9, "top_p": 0.95, "frequency_penalty": 0.7},
            "factual": {"temperature": 0.2, "top_p": 0.85, "frequency_penalty": 0.2},
            "code": {"temperature": 0.3, "top_p": 0.9, "frequency_penalty": 0.5},
            "analytical": {"temperature": 0.4, "top_p": 0.92, "frequency_penalty": 0.3}
        }
        
        # Pilih preset dasar
        sampling_params = sampling_presets.get(task_type, sampling_presets["factual"])
        
        # Sesuaikan berdasarkan preferensi pengguna jika diberikan
        if user_preferences:
            if "creativity_level" in user_preferences:
                # Skala temperatur berdasarkan preferensi kreativitas (1-10)
                creativity = min(max(user_preferences["creativity_level"], 1), 10) / 10
                sampling_params["temperature"] = 0.1 + (0.9 * creativity)
            
            if "diversity" in user_preferences:
                # Sesuaikan top_p berdasarkan keberagaman respons yang diinginkan
                diversity = min(max(user_preferences["diversity"], 1), 10) / 10
                sampling_params["top_p"] = 0.6 + (0.39 * diversity)
        
        # Buat dan kirim permintaan dengan parameter sampling kustom
        response = await self.client.send_request(
            prompt=prompt,
            temperature=sampling_params["temperature"],
            top_p=sampling_params["top_p"],
            frequency_penalty=sampling_params["frequency_penalty"]
        )
        
        # Kembalikan respons dengan metadata sampling untuk transparansi
        return {
            "text": response.generated_text,
            "applied_sampling": sampling_params,
            "task_type": task_type
        }
```

Dalam kode sebelumnya kita telah:

- Membuat kelas `DynamicSamplingService` yang mengelola sampling adaptif.
- Mendefinisikan preset sampling untuk berbagai jenis tugas (kreatif, faktual, kode, analitis).
- Memilih preset sampling dasar berdasarkan jenis tugas.
- Menyesuaikan parameter sampling berdasarkan preferensi pengguna, seperti tingkat kreativitas dan keberagaman.
- Mengirim permintaan dengan parameter sampling yang dikonfigurasi secara dinamis.
- Mengembalikan teks yang dihasilkan bersama parameter sampling dan jenis tugas untuk transparansi.
- Menggunakan `temperature` untuk mengontrol randomness output, di mana nilai lebih tinggi menghasilkan respons yang lebih kreatif.
- Menggunakan `top_p` untuk membatasi pemilihan token pada token yang ikut menyumbang massa probabilitas kumulatif teratas, meningkatkan kualitas teks yang dihasilkan.
- Menggunakan `frequency_penalty` untuk mengurangi pengulangan dan mendorong keberagaman dalam output.
- Menggunakan `user_preferences` untuk mengizinkan kustomisasi parameter sampling berdasarkan tingkat kreativitas dan keberagaman yang ditentukan pengguna.
- Menggunakan `task_type` untuk menentukan strategi sampling yang tepat untuk permintaan, memungkinkan respons yang lebih disesuaikan berdasarkan sifat tugas.
- Menggunakan metode `send_request` untuk mengirim prompt dengan parameter sampling terkonfigurasi, memastikan model menghasilkan teks sesuai kebutuhan yang ditentukan.
- Menggunakan `generated_text` untuk mendapatkan respons model, yang kemudian dikembalikan bersama parameter sampling dan jenis tugas untuk analisis atau tampilan lebih lanjut.
- Menggunakan fungsi `min` dan `max` untuk memastikan preferensi pengguna dibatasi dalam rentang valid, mencegah konfigurasi sampling tidak valid.

# [JavaScript Dinamis](#tab/javascript-dynamic)

```javascript
// Contoh JavaScript: Konfigurasi pengambilan sampel dinamis berdasarkan konteks pengguna
class AdaptiveSamplingManager {
  constructor(mcpClient) {
    this.client = mcpClient;
    
    // Mendefinisikan profil pengambilan sampel dasar
    this.samplingProfiles = {
      creative: { temperature: 0.85, topP: 0.94, frequencyPenalty: 0.7, presencePenalty: 0.5 },
      factual: { temperature: 0.2, topP: 0.85, frequencyPenalty: 0.3, presencePenalty: 0.1 },
      code: { temperature: 0.25, topP: 0.9, frequencyPenalty: 0.4, presencePenalty: 0.3 },
      conversational: { temperature: 0.7, topP: 0.9, frequencyPenalty: 0.6, presencePenalty: 0.4 }
    };
    
    // Melacak performa historis
    this.performanceHistory = [];
  }
  
  // Mendeteksi jenis tugas dari prompt
  detectTaskType(prompt, context = {}) {
    const promptLower = prompt.toLowerCase();
    
    // Deteksi heuristik sederhana - bisa ditingkatkan dengan klasifikasi ML
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
    
    // Default ke percakapan jika tipe tidak jelas terdeteksi
    return 'conversational';
  }
  
  // Menghitung parameter pengambilan sampel berdasarkan konteks dan preferensi pengguna
  getSamplingParameters(prompt, context = {}) {
    // Mendeteksi jenis tugas
    const taskType = this.detectTaskType(prompt, context);
    
    // Mendapatkan profil dasar
    let params = {...this.samplingProfiles[taskType]};
    
    // Menyesuaikan berdasarkan preferensi pengguna
    if (context.userPreferences) {
      const { creativity, precision, consistency } = context.userPreferences;
      
      if (creativity !== undefined) {
        // Mengubah skala dari 1-10 ke rentang suhu yang sesuai
        params.temperature = 0.1 + (creativity * 0.09); // 0.1-1.0
      }
      
      if (precision !== undefined) {
        // Presisi lebih tinggi berarti topP lebih rendah (pemilihan lebih fokus)
        params.topP = 1.0 - (precision * 0.05); // 0.5-1.0
      }
      
      if (consistency !== undefined) {
        // Konsistensi lebih tinggi berarti penalti lebih rendah
        params.frequencyPenalty = 0.1 + ((10 - consistency) * 0.08); // 0.1-0.9
      }
    }
    
    // Menerapkan penyesuaian yang dipelajari dari riwayat performa
    this.applyLearnedAdjustments(params, taskType);
    
    return params;
  }
  
  applyLearnedAdjustments(params, taskType) {
    // Logika adaptif sederhana - bisa ditingkatkan dengan algoritma yang lebih canggih
    const relevantHistory = this.performanceHistory
      .filter(entry => entry.taskType === taskType)
      .slice(-5); // Hanya mempertimbangkan riwayat terbaru
    
    if (relevantHistory.length > 0) {
      // Menghitung skor performa rata-rata
      const avgScore = relevantHistory.reduce((sum, entry) => sum + entry.score, 0) / relevantHistory.length;
      
      // Jika performa di bawah ambang, sesuaikan parameter
      if (avgScore < 0.7) {
        // Penyesuaian ringan menuju nilai yang lebih aman
        params.temperature = Math.max(params.temperature * 0.9, 0.1);
        params.topP = Math.max(params.topP * 0.95, 0.5);
      }
    }
  }
  
  recordPerformance(prompt, samplingParams, response, score) {
    // Mencatat performa untuk penyesuaian di masa depan
    this.performanceHistory.push({
      timestamp: Date.now(),
      taskType: this.detectTaskType(prompt),
      samplingParams,
      responseLength: response.generatedText.length,
      score // Peringkat 0-1 dari kualitas respons
    });
    
    // Membatasi ukuran riwayat
    if (this.performanceHistory.length > 100) {
      this.performanceHistory.shift();
    }
  }
  
  async generateResponse(prompt, context = {}) {
    // Mendapatkan parameter pengambilan sampel yang dioptimalkan
    const samplingParams = this.getSamplingParameters(prompt, context);
    
    // Mengirim permintaan dengan parameter yang dioptimalkan
    const response = await this.client.sendPrompt(prompt, {
      ...samplingParams,
      allowedTools: context.allowedTools || []
    });
    
    // Jika pengguna memberikan umpan balik, catat untuk optimasi di masa depan
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
    // Tugas kreatif dengan preferensi pengguna kustom
    const creativeResult = await samplingManager.generateResponse(
      "Write a short poem about artificial intelligence",
      {
        userPreferences: {
          creativity: 9,  // Kreativitas tinggi (1-10)
          consistency: 3  // Konsistensi rendah (1-10)
        }
      }
    );
    
    console.log('Creative Task:');
    console.log(`Detected type: ${creativeResult.detectedTaskType}`);
    console.log('Applied sampling:', creativeResult.appliedSamplingParams);
    console.log(creativeResult.response.generatedText);
    
    // Tugas pembuatan kode
    const codeResult = await samplingManager.generateResponse(
      "Write a JavaScript function to calculate the Fibonacci sequence",
      {
        userPreferences: {
          creativity: 2,  // Kreativitas rendah
          precision: 8,   // Presisi tinggi
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

Dalam kode sebelumnya kita telah:

- Membuat kelas `AdaptiveSamplingManager` yang mengelola sampling dinamis berdasarkan jenis tugas dan preferensi pengguna.
- Mendefinisikan profil sampling untuk berbagai jenis tugas (kreatif, faktual, kode, percakapan).
- Mengimplementasikan metode untuk mendeteksi jenis tugas dari prompt menggunakan heuristik sederhana.
- Menghitung parameter sampling berdasarkan jenis tugas yang terdeteksi dan preferensi pengguna.
- Menerapkan penyesuaian yang dipelajari berdasarkan performa historis untuk mengoptimalkan parameter sampling.
- Mencatat performa untuk penyesuaian di masa depan, memungkinkan sistem belajar dari interaksi sebelumnya.
- Mengirim permintaan dengan parameter sampling terkonfigurasi secara dinamis dan mengembalikan teks yang dihasilkan beserta parameter yang diterapkan dan jenis tugas yang terdeteksi.
- Menggunakan:
    - `userPreferences` untuk mengizinkan kustomisasi parameter sampling berdasarkan tingkat kreativitas, presisi, dan konsistensi yang ditentukan pengguna.
    - `detectTaskType` untuk menentukan sifat tugas berdasarkan prompt, memungkinkan respons yang lebih disesuaikan.
    - `recordPerformance` untuk mencatat performa respons yang dihasilkan, memungkinkan sistem beradaptasi dan berkembang seiring waktu.
    - `applyLearnedAdjustments` untuk memodifikasi parameter sampling berdasarkan performa historis, meningkatkan kemampuan model menghasilkan respons berkualitas.
    - `generateResponse` untuk mengenkapsulasi seluruh proses menghasilkan respons dengan sampling adaptif, memudahkan pemanggilan dengan berbagai prompt dan konteks.
    - `allowedTools` untuk menentukan alat mana yang dapat digunakan model selama generasi, memungkinkan respons yang lebih peka konteks.
    - `feedbackScore` untuk mengizinkan pengguna memberikan umpan balik tentang kualitas respons yang dihasilkan, yang dapat digunakan untuk menyempurnakan performa model dari waktu ke waktu.
    - `performanceHistory` untuk memelihara catatan interaksi masa lalu, memungkinkan sistem belajar dari keberhasilan dan kegagalan sebelumnya.
    - `getSamplingParameters` untuk menyesuaikan paramater sampling secara dinamis berdasarkan konteks permintaan, memungkinkan perilaku model yang lebih fleksibel dan responsif.
    - `detectTaskType` untuk mengklasifikasikan tugas berdasarkan prompt, memungkinkan sistem menerapkan strategi sampling yang sesuai untuk tipe permintaan yang berbeda.
    - `samplingProfiles` untuk mendefinisikan konfigurasi sampling dasar untuk berbagai tipe tugas, memungkinkan penyesuaian cepat berdasarkan sifat permintaan.

---

## Selanjutnya

- [5.7 Scaling](../mcp-scaling/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->