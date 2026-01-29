# Penjana Pelan Pembelajaran dengan Chainlit & Microsoft Learn Docs MCP

## Prasyarat

- Python 3.8 atau lebih tinggi
- pip (pengurus pakej Python)
- Akses internet untuk menyambung ke pelayan Microsoft Learn Docs MCP

## Pemasangan

1. Klon repositori ini atau muat turun fail projek.
2. Pasang kebergantungan yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

## Penggunaan

### Senario 1: Pertanyaan Mudah kepada Docs MCP
Klien baris perintah yang menyambung ke pelayan Docs MCP, menghantar pertanyaan, dan mencetak hasilnya.

1. Jalankan skrip:
   ```bash
   python scenario1.py
   ```
2. Masukkan soalan dokumentasi anda di prompt.

### Senario 2: Penjana Pelan Pembelajaran (Aplikasi Web Chainlit)
Antara muka berasaskan web (menggunakan Chainlit) yang membolehkan pengguna menjana pelan pembelajaran peribadi, minggu demi minggu, untuk mana-mana topik teknikal.

1. Mulakan aplikasi Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Buka URL tempatan yang disediakan di terminal anda (contohnya, http://localhost:8000) dalam pelayar anda.
3. Dalam tetingkap sembang, masukkan topik pembelajaran anda dan bilangan minggu yang anda ingin belajar (contohnya, "Sijil AI-900, 8 minggu").
4. Aplikasi akan memberikan pelan pembelajaran minggu demi minggu, termasuk pautan ke dokumentasi Microsoft Learn yang berkaitan.

**Pembolehubah Persekitaran Diperlukan:**

Untuk menggunakan Senario 2 (aplikasi web Chainlit dengan Azure OpenAI), anda mesti menetapkan pembolehubah persekitaran berikut dalam fail `.env` di direktori `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Isi nilai ini dengan butiran sumber Azure OpenAI anda sebelum menjalankan aplikasi.

> [!TIP]
> Anda boleh dengan mudah melancarkan model anda sendiri menggunakan [Azure AI Foundry](https://ai.azure.com/).

### Senario 3: Dokumentasi Dalam Penyunting dengan Pelayan MCP di VS Code

Daripada bertukar tab pelayar untuk mencari dokumentasi, anda boleh membawa Microsoft Learn Docs terus ke dalam VS Code menggunakan pelayan MCP. Ini membolehkan anda:
- Mencari dan membaca dokumentasi dalam VS Code tanpa meninggalkan persekitaran pengkodan anda.
- Merujuk dokumentasi dan memasukkan pautan terus ke README atau fail kursus anda.
- Menggunakan GitHub Copilot dan MCP bersama untuk aliran kerja dokumentasi berkuasa AI yang lancar.

**Contoh Kegunaan:**
- Menambah pautan rujukan dengan cepat ke README semasa menulis dokumentasi kursus atau projek.
- Menggunakan Copilot untuk menjana kod dan MCP untuk segera mencari serta memetik dokumentasi yang berkaitan.
- Kekal fokus dalam penyunting anda dan meningkatkan produktiviti.

> [!IMPORTANT]
> Pastikan anda mempunyai konfigurasi [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) yang sah dalam ruang kerja anda (lokasi adalah `.vscode/mcp.json`).

## Kenapa Chainlit untuk Senario 2?

Chainlit adalah kerangka kerja sumber terbuka moden untuk membina aplikasi web perbualan. Ia memudahkan penciptaan antara muka pengguna berasaskan sembang yang menyambung ke perkhidmatan backend seperti pelayan Microsoft Learn Docs MCP. Projek ini menggunakan Chainlit untuk menyediakan cara interaktif yang mudah untuk menjana pelan pembelajaran peribadi secara masa nyata. Dengan memanfaatkan Chainlit, anda boleh dengan cepat membina dan melancarkan alat berasaskan sembang yang meningkatkan produktiviti dan pembelajaran.

## Apa yang Aplikasi Ini Lakukan

Aplikasi ini membolehkan pengguna mencipta pelan pembelajaran peribadi dengan hanya memasukkan topik dan tempoh. Aplikasi ini menganalisis input anda, membuat pertanyaan ke pelayan Microsoft Learn Docs MCP untuk kandungan yang berkaitan, dan menyusun hasilnya ke dalam pelan berstruktur minggu demi minggu. Cadangan setiap minggu dipaparkan dalam sembang, menjadikannya mudah untuk diikuti dan menjejaki kemajuan anda. Integrasi ini memastikan anda sentiasa mendapat sumber pembelajaran terkini dan paling relevan.

## Contoh Pertanyaan

Cuba pertanyaan ini di tetingkap sembang untuk melihat bagaimana aplikasi bertindak balas:

- `Sijil AI-900, 8 minggu`
- `Belajar Azure Functions, 4 minggu`
- `Azure DevOps, 6 minggu`
- `Kejuruteraan data di Azure, 10 minggu`
- `Asas keselamatan Microsoft, 5 minggu`
- `Power Platform, 7 minggu`
- `Perkhidmatan AI Azure, 12 minggu`
- `Seni bina awan, 9 minggu`

Contoh ini menunjukkan fleksibiliti aplikasi untuk pelbagai matlamat pembelajaran dan jangka masa.

## Rujukan

- [Dokumentasi Chainlit](https://docs.chainlit.io/)
- [Dokumentasi MCP](https://github.com/MicrosoftDocs/mcp)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.