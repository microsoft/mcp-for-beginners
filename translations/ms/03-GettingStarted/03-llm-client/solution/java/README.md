# Calculator LLM Client

Aplikasi Java yang menunjukkan cara menggunakan LangChain4j untuk berhubung dengan perkhidmatan kalkulator MCP (Model Context Protocol) dengan integrasi GitHub Models.

## Prasyarat

- Java 21 atau lebih tinggi
- Maven 3.6+ (atau gunakan Maven wrapper yang disertakan)
- Akaun GitHub dengan akses ke GitHub Models
- Perkhidmatan kalkulator MCP berjalan di `http://localhost:8080`

## Mendapatkan Token GitHub

Aplikasi ini menggunakan GitHub Models yang memerlukan token akses peribadi GitHub. Ikuti langkah berikut untuk mendapatkan token anda:

### 1. Akses GitHub Models
1. Pergi ke [GitHub Models](https://github.com/marketplace/models)
2. Log masuk dengan akaun GitHub anda
3. Mohon akses ke GitHub Models jika anda belum berbuat demikian

### 2. Buat Token Akses Peribadi
1. Pergi ke [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Klik "Generate new token" → "Generate new token (classic)"
3. Beri nama token anda yang jelas (contoh: "MCP Calculator Client")
4. Tetapkan tarikh luput mengikut keperluan
5. Pilih skop berikut:
   - `repo` (jika mengakses repositori peribadi)
   - `user:email`
6. Klik "Generate token"
7. **Penting**: Salin token segera - anda tidak akan dapat melihatnya lagi!

### 3. Tetapkan Pembolehubah Persekitaran

#### Pada Windows (Command Prompt):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Pada Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### Pada macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Persediaan dan Pemasangan

1. **Clone atau navigasi ke direktori projek**

2. **Pasang kebergantungan**:
   ```cmd
   mvnw clean install
   ```
   Atau jika Maven sudah dipasang secara global:
   ```cmd
   mvn clean install
   ```

3. **Tetapkan pembolehubah persekitaran** (rujuk bahagian "Mendapatkan Token GitHub" di atas)

4. **Mulakan Perkhidmatan Kalkulator MCP**:
   Pastikan perkhidmatan kalkulator MCP bab 1 berjalan di `http://localhost:8080/sse`. Ia perlu berjalan sebelum anda memulakan klien.

## Menjalankan Aplikasi

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Apa Yang Aplikasi Lakukan

Aplikasi ini menunjukkan tiga interaksi utama dengan perkhidmatan kalkulator:

1. **Penambahan**: Mengira jumlah 24.5 dan 17.3
2. **Punca Kuasa Dua**: Mengira punca kuasa dua bagi 144
3. **Bantuan**: Menunjukkan fungsi kalkulator yang tersedia

## Output Dijangka

Apabila berjaya dijalankan, anda akan melihat output seperti berikut:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Penyelesaian Masalah

### Isu Lazim

1. **"GITHUB_TOKEN environment variable not set"**
   - Pastikan anda telah menetapkan pembolehubah persekitaran `GITHUB_TOKEN`
   - Mulakan semula terminal/command prompt selepas menetapkan pembolehubah

2. **"Connection refused to localhost:8080"**
   - Pastikan perkhidmatan kalkulator MCP berjalan pada port 8080
   - Semak jika ada perkhidmatan lain menggunakan port 8080

3. **"Authentication failed"**
   - Sahkan token GitHub anda sah dan mempunyai kebenaran yang betul
   - Semak jika anda mempunyai akses ke GitHub Models

4. **Ralat binaan Maven**
   - Pastikan anda menggunakan Java 21 atau lebih tinggi: `java -version`
   - Cuba bersihkan binaan: `mvnw clean`

### Debugging

Untuk mengaktifkan log debug, tambah argumen JVM berikut semasa menjalankan:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurasi

Aplikasi ini dikonfigurasikan untuk:
- Menggunakan GitHub Models dengan model `gpt-4.1-nano`
- Berhubung ke perkhidmatan MCP di `http://localhost:8080/sse`
- Menggunakan masa tamat 60 saat untuk permintaan
- Mengaktifkan log permintaan/respon untuk debugging

## Kebergantungan

Kebergantungan utama yang digunakan dalam projek ini:
- **LangChain4j**: Untuk integrasi AI dan pengurusan alat
- **LangChain4j MCP**: Untuk sokongan Model Context Protocol
- **LangChain4j GitHub Models**: Untuk integrasi GitHub Models
- **Spring Boot**: Untuk rangka kerja aplikasi dan suntikan kebergantungan

## Lesen

Projek ini dilesenkan di bawah Apache License 2.0 - lihat fail [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) untuk maklumat lanjut.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.