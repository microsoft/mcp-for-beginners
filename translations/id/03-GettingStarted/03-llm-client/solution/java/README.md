# Klien Kalkulator LLM

Aplikasi Java yang mendemonstrasikan cara menggunakan LangChain4j untuk terhubung ke layanan kalkulator MCP (Model Context Protocol) melalui API MiniMax yang kompatibel dengan OpenAI.

## Prasyarat

- Java 21 atau lebih tinggi
- Maven 3.6+ (atau gunakan pembungkus Maven yang disertakan)
- Kunci API MiniMax
- Layanan kalkulator MCP berjalan di `http://localhost:8080`

## Mendapatkan Kunci API

Aplikasi ini menggunakan API MiniMax yang kompatibel dengan OpenAI. Ikuti langkah-langkah ini untuk mendapatkan kunci dan endpoint Anda:

### 1. Pilih endpoint
1. Gunakan `https://api.minimax.io/v1` untuk endpoint global
2. Gunakan `https://api.minimaxi.com/v1` untuk endpoint China

### 2. Buat kunci API
1. Buat kunci API MiniMax dari akun MiniMax Anda
2. Simpan kunci tersebut di tempat yang aman

### 3. Atur Variabel Lingkungan

#### Di Windows (Command Prompt):
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

1. **Clone atau navigasikan ke direktori proyek**

2. **Instal dependensi**:
   ```cmd
   mvnw clean install
   ```
   Atau jika Anda sudah menginstal Maven secara global:
   ```cmd
   mvn clean install
   ```

3. **Atur variabel lingkungan** (lihat bagian "Mendapatkan Kunci API" di atas)

4. **Mulai Layanan Kalkulator MCP**:
   Pastikan Anda telah menjalankan layanan kalkulator MCP dari bab 1 pada `http://localhost:8080/sse`. Ini harus berjalan sebelum Anda memulai klien.

## Menjalankan Aplikasi

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

Saat berjalan dengan sukses, Anda harus melihat output yang mirip dengan:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Pemecahan Masalah

### Masalah Umum

1. **"Variabel lingkungan OPENAI_API_KEY belum diatur"**
   - Pastikan Anda sudah mengatur variabel lingkungan `OPENAI_API_KEY`
   - Restart terminal/command prompt Anda setelah mengatur variabel tersebut

2. **"Koneksi ditolak ke localhost:8080"**
   - Pastikan layanan kalkulator MCP berjalan di port 8080
   - Periksa apakah ada layanan lain yang menggunakan port 8080

3. **"Autentikasi gagal"**
   - Verifikasi bahwa kunci API Anda valid
   - Periksa bahwa `OPENAI_BASE_URL` sesuai dengan endpoint yang Anda gunakan

4. **Kesalahan build Maven**
   - Pastikan Anda menggunakan Java 21 atau lebih tinggi: `java -version`
   - Coba bersihkan build: `mvnw clean`

### Debugging

Untuk mengaktifkan logging debug, tambahkan argumen JVM berikut saat menjalankan:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurasi

Aplikasi dikonfigurasi untuk:
- Menggunakan MiniMax-M3 secara default, atau MiniMax-M2.7 saat `MINIMAX_MODEL_ID` diatur
- Terhubung ke `OPENAI_BASE_URL` saat disetel; jika tidak gunakan `https://api.minimaxi.com/v1` saat `MINIMAX_REGION=cn_zh`, atau `https://api.minimax.io/v1` secara default
- Terhubung ke layanan MCP di `http://localhost:8080/sse`
- Menggunakan timeout 60 detik untuk permintaan

## Dependensi

Dependensi utama yang digunakan dalam proyek ini:
- **LangChain4j**: Untuk integrasi AI dan manajemen alat
- **LangChain4j MCP**: Untuk dukungan Model Context Protocol
- **LangChain4j OpenAI resmi**: Untuk integrasi API MiniMax yang kompatibel dengan OpenAI
- **Spring Boot**: Untuk kerangka kerja aplikasi dan dependency injection

## Lisensi

Proyek ini dilisensikan di bawah Apache License 2.0 - lihat file [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) untuk detail.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->