# Generator Rencana Belajar dengan Chainlit & Microsoft Learn Docs MCP

## Prasyarat

- Python 3.8 atau lebih tinggi
- pip (manajer paket Python)
- Akses internet untuk terhubung ke server Microsoft Learn Docs MCP

## Instalasi

1. Clone repositori ini atau unduh file proyek.
2. Instal dependensi yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

## Penggunaan

### Skenario 1: Query Sederhana ke Docs MCP
Klien command-line yang terhubung ke server Docs MCP, mengirimkan query, dan mencetak hasilnya.

1. Jalankan skrip:
   ```bash
   python scenario1.py
   ```
2. Masukkan pertanyaan dokumentasi Anda di prompt.

### Skenario 2: Generator Rencana Belajar (Aplikasi Web Chainlit)
Antarmuka berbasis web (menggunakan Chainlit) yang memungkinkan pengguna untuk membuat rencana belajar yang dipersonalisasi, minggu demi minggu, untuk topik teknis apa pun.

1. Mulai aplikasi Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Buka URL lokal yang diberikan di terminal Anda (misalnya, http://localhost:8000) di browser Anda.
3. Di jendela chat, masukkan topik belajar Anda dan jumlah minggu yang ingin Anda pelajari (misalnya, "sertifikasi AI-900, 8 minggu").
4. Aplikasi akan merespons dengan rencana belajar minggu demi minggu, termasuk tautan ke dokumentasi Microsoft Learn yang relevan.

**Variabel Lingkungan yang Diperlukan:**

Untuk menggunakan Skenario 2 (aplikasi web Chainlit dengan Azure OpenAI), Anda harus mengatur variabel lingkungan berikut dalam file `.env` di direktori `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Isi nilai-nilai ini dengan detail sumber daya Azure OpenAI Anda sebelum menjalankan aplikasi.

> [!TIP]
> Anda dapat dengan mudah menerapkan model Anda sendiri menggunakan [Azure AI Foundry](https://ai.azure.com/).

### Skenario 3: Dokumentasi Dalam Editor dengan Server MCP di VS Code

Alih-alih beralih tab browser untuk mencari dokumentasi, Anda dapat membawa Microsoft Learn Docs langsung ke VS Code menggunakan server MCP. Ini memungkinkan Anda untuk:
- Mencari dan membaca dokumentasi di dalam VS Code tanpa meninggalkan lingkungan coding Anda.
- Merujuk dokumentasi dan menyisipkan tautan langsung ke README atau file kursus Anda.
- Menggunakan GitHub Copilot dan MCP bersama untuk alur kerja dokumentasi yang mulus dan didukung AI.

**Contoh Penggunaan:**
- Menambahkan tautan referensi dengan cepat ke README saat menulis dokumentasi kursus atau proyek.
- Menggunakan Copilot untuk menghasilkan kode dan MCP untuk langsung menemukan serta mengutip dokumentasi yang relevan.
- Tetap fokus di editor Anda dan meningkatkan produktivitas.

> [!IMPORTANT]
> Pastikan Anda memiliki konfigurasi [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) yang valid di workspace Anda (lokasi: `.vscode/mcp.json`).

## Mengapa Chainlit untuk Skenario 2?

Chainlit adalah kerangka kerja open-source modern untuk membangun aplikasi web percakapan. Ini mempermudah pembuatan antarmuka pengguna berbasis chat yang terhubung ke layanan backend seperti server Microsoft Learn Docs MCP. Proyek ini menggunakan Chainlit untuk menyediakan cara interaktif yang sederhana untuk membuat rencana belajar yang dipersonalisasi secara real-time. Dengan memanfaatkan Chainlit, Anda dapat dengan cepat membangun dan menerapkan alat berbasis chat yang meningkatkan produktivitas dan pembelajaran.

## Apa yang Dilakukan Aplikasi Ini

Aplikasi ini memungkinkan pengguna untuk membuat rencana belajar yang dipersonalisasi hanya dengan memasukkan topik dan durasi. Aplikasi akan memproses input Anda, melakukan query ke server Microsoft Learn Docs MCP untuk konten yang relevan, dan mengorganisasikan hasilnya ke dalam rencana terstruktur minggu demi minggu. Rekomendasi setiap minggu ditampilkan di chat, sehingga mudah diikuti dan dilacak kemajuannya. Integrasi ini memastikan Anda selalu mendapatkan sumber belajar terbaru dan paling relevan.

## Contoh Query

Coba query berikut di jendela chat untuk melihat bagaimana aplikasi merespons:

- `sertifikasi AI-900, 8 minggu`
- `Belajar Azure Functions, 4 minggu`
- `Azure DevOps, 6 minggu`
- `Rekayasa data di Azure, 10 minggu`
- `Dasar-dasar keamanan Microsoft, 5 minggu`
- `Power Platform, 7 minggu`
- `Layanan AI Azure, 12 minggu`
- `Arsitektur cloud, 9 minggu`

Contoh-contoh ini menunjukkan fleksibilitas aplikasi untuk berbagai tujuan belajar dan jangka waktu.

## Referensi

- [Dokumentasi Chainlit](https://docs.chainlit.io/)
- [Dokumentasi MCP](https://github.com/MicrosoftDocs/mcp)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.