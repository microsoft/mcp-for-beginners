# Klien Kalkulator LLM

> [!NOTE]
> Penyelesaian ini menyambung ke perkhidmatan kalkulator HTTP+SSE warisan kursus dan
> menyasarkan API SDK MCP `2025-11-25`. Ia bukan contoh HTTP Streamable `2026-07-28`.






- Maven 3.6+ (atau gunakan pembungkus Maven yang disediakan)
- Kunci API MiniMax
- Perkhidmatan kalkulator MCP yang berjalan pada `http://localhost:8080`






1. Gunakan `https://api.minimax.io/v1` untuk titik hujung global
2. Gunakan `https://api.minimaxi.com/v1` untuk titik hujung China


1. Buat kunci API MiniMax dari akaun MiniMax anda
2. Simpan kunci itu di tempat yang selamat




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




   ```cmd
   mvnw clean install
   ```
   Atau jika anda telah memasang Maven secara global:
   ```cmd
   mvn clean install
   ```

3. **Tetapkan pembolehubah persekitaran** (rujuk bahagian "Mendapatkan Kunci API" di atas)


   Pastikan anda telah menjalankan perkhidmatan kalkulator MCP bab 1 pada `http://localhost:8080/sse`. Ini harus berjalan sebelum anda memulakan klien.




```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Apa yang Aplikasi Lakukan

Aplikasi ini menunjukkan tiga interaksi utama dengan perkhidmatan kalkulator:

1. **Penambahan**: Mengira jumlah 24.5 dan 17.3
2. **Punca Kuasa Dua**: Mengira punca kuasa dua bagi 144
3. **Bantuan**: Menunjukkan fungsi kalkulator yang tersedia

## Output yang Dijangka

Apabila berjalan dengan jayanya, anda sepatutnya melihat output yang serupa dengan:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Penyelesaian Masalah

### Isu Lazim

1. **"Pembolehubah persekitaran OPENAI_API_KEY tidak diset"**
   - Pastikan anda telah menetapkan pembolehubah persekitaran `OPENAI_API_KEY`
   - Mulakan semula terminal/command prompt anda selepas menetapkan pembolehubah tersebut

2. **"Sambungan ditolak ke localhost:8080"**
   - Pastikan perkhidmatan kalkulator MCP berjalan pada port 8080
   - Semak jika perkhidmatan lain menggunakan port 8080

3. **"Pengesahan gagal"**
   - Sahkan API key anda adalah sah
   - Periksa bahawa `OPENAI_BASE_URL` sepadan dengan endpoint yang anda ingin gunakan

4. **Ralat binaan Maven**
   - Pastikan anda menggunakan Java 21 atau lebih tinggi: `java -version`
   - Cuba bersihkan binaan: `mvnw clean`

### Penyahpepijatan

Untuk mengaktifkan log debug, tambahkan argumen JVM berikut semasa menjalankan:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurasi

Aplikasi dikonfigurasikan untuk:
- Menggunakan MiniMax-M3 secara lalai; tetapkan `MINIMAX_MODEL_ID` untuk memilih sama ada `MiniMax-M3` atau `MiniMax-M2.7`
- Sambung ke `OPENAI_BASE_URL` apabila ia diset; jika tidak gunakan `https://api.minimaxi.com/v1` apabila `MINIMAX_REGION=cn_zh`, atau `https://api.minimax.io/v1` secara lalai
- Sambung ke perkhidmatan MCP di `http://localhost:8080/sse`
- Gunakan masa tamat 60 saat untuk permintaan

## Kebergantungan

Kebergantungan utama yang digunakan dalam projek ini:
- **LangChain4j**: Untuk integrasi AI dan pengurusan alat
- **LangChain4j MCP**: Untuk sokongan Protokol Konteks Model
- **LangChain4j OpenAI rasmi**: Untuk integrasi API MiniMax yang serasi dengan OpenAI
- **Spring Boot**: Untuk rangka kerja aplikasi dan suntikan kebergantungan

## Lesen

Projek ini dilisensikan di bawah Lesen Apache 2.0 - lihat fail [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) untuk butiran.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->