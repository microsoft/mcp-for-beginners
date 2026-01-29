# Contoh Lengkap Klien MCP

Direktori ini mengandungi contoh lengkap dan berfungsi untuk klien MCP dalam pelbagai bahasa pengaturcaraan. Setiap klien menunjukkan fungsi penuh seperti yang diterangkan dalam tutorial README.md utama.

## Klien Yang Tersedia

### 1. Klien Java (`client_example_java.java`)

- **Pengangkutan**: SSE (Server-Sent Events) melalui HTTP
- **Pelayan Sasaran**: `http://localhost:8080`
- **Ciri-ciri**:
  - Penubuhan sambungan dan ping
  - Senarai alat
  - Operasi kalkulator (tambah, tolak, darab, bahagi, bantuan)
  - Pengendalian ralat dan pengekstrakan hasil

**Untuk menjalankan:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. Klien C# (`client_example_csharp.cs`)

- **Pengangkutan**: Stdio (Input/Output Standard)
- **Pelayan Sasaran**: Pelayan MCP .NET tempatan melalui dotnet run
- **Ciri-ciri**:
  - Permulaan pelayan automatik melalui pengangkutan stdio
  - Senarai alat dan sumber
  - Operasi kalkulator
  - Penguraian hasil JSON
  - Pengendalian ralat yang menyeluruh

**Untuk menjalankan:**

```bash
dotnet run
```

### 3. Klien TypeScript (`client_example_typescript.ts`)

- **Pengangkutan**: Stdio (Input/Output Standard)
- **Pelayan Sasaran**: Pelayan MCP Node.js tempatan
- **Ciri-ciri**:
  - Sokongan penuh protokol MCP
  - Operasi alat, sumber, dan prompt
  - Operasi kalkulator
  - Pembacaan sumber dan pelaksanaan prompt
  - Pengendalian ralat yang kukuh

**Untuk menjalankan:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Klien Python (`client_example_python.py`)

- **Pengangkutan**: Stdio (Input/Output Standard)  
- **Pelayan Sasaran**: Pelayan MCP Python tempatan
- **Ciri-ciri**:
  - Corak async/await untuk operasi
  - Penemuan alat dan sumber
  - Ujian operasi kalkulator
  - Pembacaan kandungan sumber
  - Organisasi berasaskan kelas

**Untuk menjalankan:**

```bash
python client_example_python.py
```

## Ciri-ciri Umum Dalam Semua Klien

Setiap implementasi klien menunjukkan:

1. **Pengurusan Sambungan**
   - Menubuhkan sambungan ke pelayan MCP
   - Mengendalikan ralat sambungan
   - Pembersihan dan pengurusan sumber yang betul

2. **Penemuan Pelayan**
   - Menyenaraikan alat yang tersedia
   - Menyenaraikan sumber yang tersedia (jika disokong)
   - Menyenaraikan prompt yang tersedia (jika disokong)

3. **Pelaksanaan Alat**
   - Operasi kalkulator asas (tambah, tolak, darab, bahagi)
   - Perintah bantuan untuk maklumat pelayan
   - Penghantaran argumen dan pengendalian hasil yang betul

4. **Pengendalian Ralat**
   - Ralat sambungan
   - Ralat pelaksanaan alat
   - Kegagalan yang terkawal dan maklum balas kepada pengguna

5. **Pemprosesan Hasil**
   - Mengekstrak kandungan teks daripada respons
   - Memformat output untuk kebolehbacaan
   - Mengendalikan format respons yang berbeza

## Prasyarat

Sebelum menjalankan klien ini, pastikan anda mempunyai:

1. **Pelayan MCP yang sepadan sedang berjalan** (dari `../01-first-server/`)
2. **Kebergantungan yang diperlukan dipasang** untuk bahasa pilihan anda
3. **Sambungan rangkaian yang betul** (untuk pengangkutan berasaskan HTTP)

## Perbezaan Utama Antara Implementasi

| Bahasa     | Pengangkutan | Permulaan Pelayan | Model Async | Pustaka Utama       |
|------------|--------------|-------------------|-------------|---------------------|
| Java       | SSE/HTTP     | Luaran            | Sync        | WebFlux, MCP SDK    |
| C#         | Stdio        | Automatik         | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio        | Automatik         | Async/Await | Node MCP SDK        |
| Python     | Stdio        | Automatik         | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio        | Automatik         | Async/Await | Rust MCP SDK, Tokio |

## Langkah Seterusnya

Selepas meneroka contoh klien ini:

1. **Ubah suai klien** untuk menambah ciri atau operasi baharu
2. **Cipta pelayan anda sendiri** dan uji dengan klien ini
3. **Eksperimen dengan pengangkutan yang berbeza** (SSE vs. Stdio)
4. **Bina aplikasi yang lebih kompleks** yang mengintegrasikan fungsi MCP

## Penyelesaian Masalah

### Isu Biasa

1. **Sambungan ditolak**: Pastikan pelayan MCP sedang berjalan pada port/laluan yang dijangka
2. **Modul tidak dijumpai**: Pasang MCP SDK yang diperlukan untuk bahasa anda
3. **Kebenaran ditolak**: Semak kebenaran fail untuk pengangkutan stdio
4. **Alat tidak dijumpai**: Sahkan pelayan melaksanakan alat yang dijangka

### Petua Debug

1. **Aktifkan log verbose** dalam MCP SDK anda
2. **Semak log pelayan** untuk mesej ralat
3. **Sahkan nama dan tandatangan alat** sepadan antara klien dan pelayan
4. **Uji dengan MCP Inspector** terlebih dahulu untuk mengesahkan fungsi pelayan

## Dokumentasi Berkaitan

- [Tutorial Klien Utama](./README.md)
- [Contoh Pelayan MCP](../../../../03-GettingStarted/01-first-server)
- [MCP dengan Integrasi LLM](../../../../03-GettingStarted/03-llm-client)
- [Dokumentasi Rasmi MCP](https://modelcontextprotocol.io/)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.