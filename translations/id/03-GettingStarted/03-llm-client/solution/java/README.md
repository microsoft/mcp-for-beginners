# Klien LLM Kalkulator

> [!NOTE]
> Solusi ini terhubung ke layanan kalkulator HTTP+SSE warisan dari kursus dan
> menargetkan API SDK MCP `2025-11-25`. Ini bukan contoh HTTP Streamable `2026-07-28`.






- Maven 3.6+ (atau gunakan pembungkus Maven yang disertakan)
- Kunci API MiniMax
- Layanan kalkulator MCP berjalan di `http://localhost:8080`






1. Gunakan `https://api.minimax.io/v1` untuk titik akhir global
2. Gunakan `https://api.minimaxi.com/v1` untuk titik akhir China


1. Buat kunci API MiniMax dari akun MiniMax Anda
2. Simpan kunci tersebut di tempat yang aman




```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Di Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### Di macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Pengaturan dan Instalasi




   ```cmd
   mvnw clean install
   ```
   Atau jika Anda sudah menginstal Maven secara global:
   ```cmd
   mvn clean install
   ```

3. **Siapkan variabel lingkungan** (lihat bagian "Mendapatkan Kunci API" di atas)


   Pastikan layanan kalkulator MCP bab 1 berjalan di `http://localhost:8080/sse`. Layanan ini harus berjalan sebelum Anda memulai klien.




```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Apa yang Dilakukan Aplikasi

Aplikasi ini mendemonstrasikan tiga interaksi utama dengan layanan kalkulator:

1. **Penjumlahan**: Menghitung jumlah dari 24.5 dan 17.3
2. **Akar Kuadrat**: Menghitung akar kuadrat dari 144
3. **Bantuan**: Menampilkan fungsi kalkulator yang tersedia

## Output yang Diharapkan

Ketika berjalan dengan sukses, Anda harus melihat output serupa dengan:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Pemecahan Masalah

### Masalah Umum

1. **"Variabel lingkungan OPENAI_API_KEY belum disetel"**
   - Pastikan Anda telah menyetel variabel lingkungan `OPENAI_API_KEY`
   - Mulai ulang terminal/command prompt Anda setelah menyetel variabel

2. **"Koneksi ditolak ke localhost:8080"**
   - Pastikan layanan kalkulator MCP berjalan di port 8080
   - Periksa apakah ada layanan lain yang menggunakan port 8080

3. **"Autentikasi gagal"**
   - Verifikasi bahwa kunci API Anda valid
   - Periksa bahwa `OPENAI_BASE_URL` cocok dengan endpoint yang Anda maksudkan untuk digunakan

4. **Kesalahan build Maven**
   - Pastikan Anda menggunakan Java 21 atau lebih baru: `java -version`
   - Coba bersihkan build: `mvnw clean`

### Debugging

Untuk mengaktifkan logging debug, tambahkan argumen JVM berikut saat menjalankan:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurasi

Aplikasi ini dikonfigurasi untuk:
- Gunakan MiniMax-M3 secara default; atur `MINIMAX_MODEL_ID` untuk memilih antara `MiniMax-M3` atau `MiniMax-M2.7`
- Terhubung ke `OPENAI_BASE_URL` saat disetel; jika tidak gunakan `https://api.minimaxi.com/v1` saat `MINIMAX_REGION=cn_zh`, atau `https://api.minimax.io/v1` secara default
- Terhubung ke layanan MCP di `http://localhost:8080/sse`
- Gunakan batas waktu 60 detik untuk permintaan

## Dependensi

Dependensi utama yang digunakan dalam proyek ini:
- **LangChain4j**: Untuk integrasi AI dan manajemen alat
- **LangChain4j MCP**: Untuk dukungan Model Context Protocol
- **LangChain4j OpenAI resmi**: Untuk integrasi API MiniMax kompatibel OpenAI
- **Spring Boot**: Untuk kerangka kerja aplikasi dan injeksi dependensi

## Lisensi

Proyek ini dilisensikan di bawah Apache License 2.0 - lihat file [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) untuk detailnya.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->