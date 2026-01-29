# Calculator LLM Client

Aplikasi Java yang menunjukkan cara menggunakan LangChain4j untuk terhubung ke layanan kalkulator MCP (Model Context Protocol) dengan integrasi GitHub Models.

## Prasyarat

- Java 21 atau lebih baru
- Maven 3.6+ (atau gunakan Maven wrapper yang disertakan)
- Akun GitHub dengan akses ke GitHub Models
- Layanan kalkulator MCP berjalan di `http://localhost:8080`

## Mendapatkan Token GitHub

Aplikasi ini menggunakan GitHub Models yang memerlukan token akses pribadi GitHub. Ikuti langkah-langkah berikut untuk mendapatkan token Anda:

### 1. Akses GitHub Models
1. Buka [GitHub Models](https://github.com/marketplace/models)
2. Masuk dengan akun GitHub Anda
3. Minta akses ke GitHub Models jika belum memiliki

### 2. Buat Personal Access Token
1. Buka [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Klik "Generate new token" → "Generate new token (classic)"
3. Beri nama token yang deskriptif (misalnya, "MCP Calculator Client")
4. Atur masa berlaku sesuai kebutuhan
5. Pilih scope berikut:
   - `repo` (jika mengakses repositori privat)
   - `user:email`
6. Klik "Generate token"
7. **Penting**: Salin token segera - Anda tidak akan bisa melihatnya lagi!

### 3. Atur Variabel Lingkungan

#### Di Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Di Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Di macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Pengaturan dan Instalasi

1. **Clone atau masuk ke direktori proyek**

2. **Pasang dependensi**:
   ```cmd
   mvnw clean install
   ```
   Atau jika Maven sudah terpasang secara global:
   ```cmd
   mvn clean install
   ```

3. **Atur variabel lingkungan** (lihat bagian "Mendapatkan Token GitHub" di atas)

4. **Jalankan Layanan Kalkulator MCP**:
   Pastikan layanan kalkulator MCP dari bab 1 berjalan di `http://localhost:8080/sse`. Layanan ini harus aktif sebelum Anda menjalankan client.

## Menjalankan Aplikasi

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Fungsi Aplikasi

Aplikasi ini menunjukkan tiga interaksi utama dengan layanan kalkulator:

1. **Penjumlahan**: Menghitung jumlah 24.5 dan 17.3
2. **Akar Kuadrat**: Menghitung akar kuadrat dari 144
3. **Bantuan**: Menampilkan fungsi kalkulator yang tersedia

## Output yang Diharapkan

Saat berjalan dengan sukses, Anda akan melihat output seperti:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Pemecahan Masalah

### Masalah Umum

1. **"GITHUB_TOKEN environment variable not set"**
   - Pastikan Anda sudah mengatur variabel lingkungan `GITHUB_TOKEN`
   - Restart terminal/command prompt setelah mengatur variabel

2. **"Connection refused to localhost:8080"**
   - Pastikan layanan kalkulator MCP berjalan di port 8080
   - Periksa apakah ada layanan lain yang menggunakan port 8080

3. **"Authentication failed"**
   - Pastikan token GitHub Anda valid dan memiliki izin yang benar
   - Periksa apakah Anda memiliki akses ke GitHub Models

4. **Error build Maven**
   - Pastikan Anda menggunakan Java 21 atau lebih baru: `java -version`
   - Coba bersihkan build: `mvnw clean`

### Debugging

Untuk mengaktifkan logging debug, tambahkan argumen JVM berikut saat menjalankan:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurasi

Aplikasi dikonfigurasi untuk:
- Menggunakan GitHub Models dengan model `gpt-4.1-nano`
- Terhubung ke layanan MCP di `http://localhost:8080/sse`
- Menggunakan timeout 60 detik untuk permintaan
- Mengaktifkan logging request/response untuk debugging

## Dependensi

Dependensi utama yang digunakan dalam proyek ini:
- **LangChain4j**: Untuk integrasi AI dan manajemen alat
- **LangChain4j MCP**: Untuk dukungan Model Context Protocol
- **LangChain4j GitHub Models**: Untuk integrasi GitHub Models
- **Spring Boot**: Untuk framework aplikasi dan dependency injection

## Lisensi

Proyek ini dilisensikan di bawah Apache License 2.0 - lihat file [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) untuk detail.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.