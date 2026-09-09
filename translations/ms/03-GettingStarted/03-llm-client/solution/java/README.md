# Pelanggan LLM Kalkulator

Aplikasi Java yang menunjukkan cara menggunakan LangChain4j untuk menyambung ke perkhidmatan kalkulator MCP (Model Context Protocol) melalui API MiniMax yang serasi dengan OpenAI.

## Prasyarat

- Java 21 atau lebih tinggi
- Maven 3.6+ (atau gunakan pembungkus Maven yang disertakan)
- Kunci API MiniMax
- Perkhidmatan kalkulator MCP berjalan di `http://localhost:8080`

## Mendapatkan Kunci API

Aplikasi ini menggunakan API MiniMax yang serasi dengan OpenAI. Ikuti langkah-langkah ini untuk mendapatkan kunci dan titik hujung anda:

### 1. Pilih titik hujung
1. Gunakan `https://api.minimax.io/v1` untuk titik hujung global
2. Gunakan `https://api.minimaxi.com/v1` untuk titik hujung China

### 2. Buat kunci API
1. Buat kunci API MiniMax dari akaun MiniMax anda
2. Simpan kunci itu di tempat yang selamat

### 3. Tetapkan Pemboleh Ubah Persekitaran

#### Pada Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Pada Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Pada macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Persediaan dan Pemasangan

1. **Klona atau navigasi ke direktori projek**

2. **Pasang kebergantungan**:
   ```cmd
   mvnw clean install
   ```
   Atau jika anda mempunyai Maven dipasang secara global:
   ```cmd
   mvn clean install
   ```

3. **Tetapkan pemboleh ubah persekitaran** (lihat bahagian "Mendapatkan Kunci API" di atas)

4. **Mulakan Perkhidmatan Kalkulator MCP**:
   Pastikan anda mempunyai perkhidmatan kalkulator MCP bab 1 berjalan di `http://localhost:8080/sse`. Ini harus berjalan sebelum anda memulakan pelanggan.

## Menjalankan Aplikasi

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Apa yang Aplikasi Lakukan

Aplikasi ini menunjukkan tiga interaksi utama dengan perkhidmatan kalkulator:

1. **Penambahan**: Mengira jumlah 24.5 dan 17.3
2. **Akar Kuasa Dua**: Mengira akar kuasa dua bagi 144
3. **Bantuan**: Menunjukkan fungsi kalkulator yang tersedia

## Output Dijangka

Apabila berjalan dengan jayanya, anda harus melihat output serupa:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Penyelesaian Masalah

### Masalah Biasa

1. **"Pemboleh ubah persekitaran OPENAI_API_KEY tidak ditetapkan"**
   - Pastikan anda telah menetapkan pemboleh ubah persekitaran `OPENAI_API_KEY`
   - Mulakan semula terminal/command prompt anda selepas menetapkan pemboleh ubah itu

2. **"Sambungan ditolak ke localhost:8080"**
   - Pastikan perkhidmatan kalkulator MCP berjalan pada port 8080
   - Semak jika perkhidmatan lain menggunakan port 8080

3. **"Pengesahan gagal"**
   - Sahkan kunci API anda adalah sah
   - Semak bahawa `OPENAI_BASE_URL` sepadan dengan titik hujung yang anda ingin gunakan

4. **Ralat binaan Maven**
   - Pastikan anda menggunakan Java 21 atau lebih tinggi: `java -version`
   - Cuba bersihkan binaan: `mvnw clean`

### Pengesanan Ralat

Untuk mengaktifkan log debug, tambah argumen JVM berikut ketika menjalankan:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurasi

Aplikasi ini dikonfigurasikan untuk:
- Menggunakan MiniMax-M3 secara lalai, atau MiniMax-M2.7 apabila `MINIMAX_MODEL_ID` ditetapkan
- Menyambung ke `OPENAI_BASE_URL` apabila ia ditetapkan; jika tidak gunakan `https://api.minimaxi.com/v1` apabila `MINIMAX_REGION=cn_zh`, atau `https://api.minimax.io/v1` secara lalai
- Menyambung ke perkhidmatan MCP di `http://localhost:8080/sse`
- Menggunakan masa tamat 60 saat untuk permintaan

## Kebergantungan

Kebergantungan utama yang digunakan dalam projek ini:
- **LangChain4j**: Untuk integrasi AI dan pengurusan alat
- **LangChain4j MCP**: Untuk sokongan Model Context Protocol
- **LangChain4j OpenAI rasmi**: Untuk integrasi API MiniMax yang serasi dengan OpenAI
- **Spring Boot**: Untuk rangka kerja aplikasi dan suntikan kebergantungan

## Lesen

Projek ini dilesenkan di bawah Lesen Apache 2.0 - lihat fail [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) untuk butiran.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->