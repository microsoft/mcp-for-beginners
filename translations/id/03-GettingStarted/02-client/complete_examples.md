# Contoh Lengkap Klien MCP

Direktori ini berisi contoh lengkap dan berfungsi dari klien MCP dalam berbagai bahasa pemrograman. Setiap klien menunjukkan seluruh fungsionalitas yang dijelaskan dalam tutorial README.md utama.

## Klien yang Tersedia

### 1. Klien Java (`client_example_java.java`)

- **Transport**: SSE (Server-Sent Events) melalui HTTP
- **Server Target**: `http://localhost:8080`
- **Fitur**:
  - Pembentukan koneksi dan ping
  - Daftar alat
  - Operasi kalkulator (tambah, kurang, kali, bagi, bantuan)
  - Penanganan kesalahan dan ekstraksi hasil

**Cara menjalankan:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. Klien C# (`client_example_csharp.cs`)

- **Transport**: Stdio (Input/Output Standar)
- **Server Target**: Server MCP .NET lokal melalui dotnet run
- **Fitur**:
  - Startup server otomatis melalui transport stdio
  - Daftar alat dan sumber daya
  - Operasi kalkulator
  - Parsing hasil JSON
  - Penanganan kesalahan yang komprehensif

**Cara menjalankan:**

```bash
dotnet run
```

### 3. Klien TypeScript (`client_example_typescript.ts`)

- **Transport**: Stdio (Input/Output Standar)
- **Server Target**: Server MCP Node.js lokal
- **Fitur**:
  - Dukungan penuh untuk protokol MCP
  - Operasi alat, sumber daya, dan prompt
  - Operasi kalkulator
  - Membaca sumber daya dan eksekusi prompt
  - Penanganan kesalahan yang tangguh

**Cara menjalankan:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Klien Python (`client_example_python.py`)

- **Transport**: Stdio (Input/Output Standar)  
- **Server Target**: Server MCP Python lokal
- **Fitur**:
  - Pola async/await untuk operasi
  - Penemuan alat dan sumber daya
  - Pengujian operasi kalkulator
  - Membaca konten sumber daya
  - Organisasi berbasis kelas

**Cara menjalankan:**

```bash
python client_example_python.py
```

## Fitur Umum di Semua Klien

Setiap implementasi klien menunjukkan:

1. **Manajemen Koneksi**
   - Membentuk koneksi ke server MCP
   - Menangani kesalahan koneksi
   - Pembersihan dan manajemen sumber daya yang tepat

2. **Penemuan Server**
   - Daftar alat yang tersedia
   - Daftar sumber daya yang tersedia (jika didukung)
   - Daftar prompt yang tersedia (jika didukung)

3. **Pemanggilan Alat**
   - Operasi kalkulator dasar (tambah, kurang, kali, bagi)
   - Perintah bantuan untuk informasi server
   - Pengiriman argumen yang tepat dan penanganan hasil

4. **Penanganan Kesalahan**
   - Kesalahan koneksi
   - Kesalahan eksekusi alat
   - Kegagalan yang terkelola dan umpan balik kepada pengguna

5. **Pemrosesan Hasil**
   - Ekstraksi konten teks dari respons
   - Format output untuk keterbacaan
   - Penanganan berbagai format respons

## Prasyarat

Sebelum menjalankan klien ini, pastikan Anda memiliki:

1. **Server MCP yang sesuai berjalan** (dari `../01-first-server/`)
2. **Dependensi yang diperlukan terinstal** untuk bahasa yang Anda pilih
3. **Konektivitas jaringan yang memadai** (untuk transport berbasis HTTP)

## Perbedaan Utama Antara Implementasi

| Bahasa     | Transport | Startup Server | Model Async | Pustaka Utama       |
|------------|-----------|----------------|-------------|---------------------|
| Java       | SSE/HTTP  | Eksternal      | Sinkron     | WebFlux, MCP SDK    |
| C#         | Stdio     | Otomatis       | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | Otomatis       | Async/Await | Node MCP SDK        |
| Python     | Stdio     | Otomatis       | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | Otomatis       | Async/Await | Rust MCP SDK, Tokio |

## Langkah Selanjutnya

Setelah menjelajahi contoh klien ini:

1. **Modifikasi klien** untuk menambahkan fitur atau operasi baru
2. **Buat server Anda sendiri** dan uji dengan klien ini
3. **Eksperimen dengan transport yang berbeda** (SSE vs. Stdio)
4. **Bangun aplikasi yang lebih kompleks** yang mengintegrasikan fungsionalitas MCP

## Pemecahan Masalah

### Masalah Umum

1. **Koneksi ditolak**: Pastikan server MCP berjalan di port/jalur yang diharapkan
2. **Modul tidak ditemukan**: Instal MCP SDK yang diperlukan untuk bahasa Anda
3. **Izin ditolak**: Periksa izin file untuk transport stdio
4. **Alat tidak ditemukan**: Verifikasi server mengimplementasikan alat yang diharapkan

### Tips Debug

1. **Aktifkan logging yang lebih rinci** di MCP SDK Anda
2. **Periksa log server** untuk pesan kesalahan
3. **Verifikasi nama dan tanda tangan alat** cocok antara klien dan server
4. **Uji dengan MCP Inspector** terlebih dahulu untuk memvalidasi fungsionalitas server

## Dokumentasi Terkait

- [Tutorial Klien Utama](./README.md)
- [Contoh Server MCP](../../../../03-GettingStarted/01-first-server)
- [MCP dengan Integrasi LLM](../../../../03-GettingStarted/03-llm-client)
- [Dokumentasi Resmi MCP](https://modelcontextprotocol.io/)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.