# 🚀 Pelayan MCP dengan PostgreSQL - Panduan Pembelajaran Lengkap

## 🧠 Gambaran Keseluruhan Laluan Pembelajaran Integrasi Pangkalan Data MCP

Panduan pembelajaran menyeluruh ini mengajar anda cara membina **pelayan Model Context Protocol (MCP)** yang sedia untuk pengeluaran yang berintegrasi dengan pangkalan data melalui pelaksanaan analitik runcit praktikal. Anda akan mempelajari corak tahap perusahaan termasuk **Keselamatan Tahap Baris (RLS)**, **carian semantik**, **integrasi Azure AI**, dan **akses data berbilang penyewa**.

Sama ada anda seorang pembangun backend, jurutera AI, atau arkitek data, panduan ini menyediakan pembelajaran berstruktur dengan contoh dunia sebenar dan latihan praktikal yang membimbing anda melalui pelayan MCP berikut https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Sumber Rasmi MCP

- 📘 [Dokumentasi MCP](https://modelcontextprotocol.io/) – Tutorial terperinci dan panduan pengguna
- 📜 [Spesifikasi MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Seni bina protokol dan rujukan teknikal
- 🧑‍💻 [Repositori GitHub MCP](https://github.com/modelcontextprotocol) – SDK sumber terbuka, alat, dan contoh kod
- 🌐 [Komuniti MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Sertai perbincangan dan sumbang kepada komuniti
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Amalan keselamatan terbaik dan mitigasi risiko


## 🧭 Laluan Pembelajaran Integrasi Pangkalan Data MCP

### 📚 Struktur Pembelajaran Lengkap untuk https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Makmal | Tajuk | Penerangan | Pautan |
|--------|-------|-------------|------|
| **Makmal 1-3: Asas** | | | |
| 00 | [Pengenalan kepada Integrasi Pangkalan Data MCP](./00-Introduction/README.md) | Gambaran keseluruhan MCP dengan integrasi pangkalan data dan kes penggunaan analitik runcit | [Mula Di Sini](./00-Introduction/README.md) |
| 01 | [Konsep Seni Bina Teras](./01-Architecture/README.md) | Memahami seni bina pelayan MCP, lapisan pangkalan data, dan corak keselamatan | [Belajar](./01-Architecture/README.md) |
| 02 | [Keselamatan dan Multi-Penyewa](./02-Security/README.md) | Keselamatan Tahap Baris, pengesahan, dan akses data berbilang penyewa | [Belajar](./02-Security/README.md) |
| 03 | [Persediaan Persekitaran](./03-Setup/README.md) | Menyediakan persekitaran pembangunan, Docker, sumber Azure | [Persediaan](./03-Setup/README.md) |
| **Makmal 4-6: Membina Pelayan MCP** | | | |
| 04 | [Reka Bentuk Pangkalan Data dan Skema](./04-Database/README.md) | Penyediaan PostgreSQL, reka bentuk skema runcit, dan data contoh | [Bina](./04-Database/README.md) |
| 05 | [Pelaksanaan Pelayan MCP](./05-MCP-Server/README.md) | Membina pelayan FastMCP dengan integrasi pangkalan data | [Bina](./05-MCP-Server/README.md) |
| 06 | [Pembangunan Alat](./06-Tools/README.md) | Mencipta alat pertanyaan pangkalan data dan introspeksi skema | [Bina](./06-Tools/README.md) |
| **Makmal 7-9: Ciri-ciri Lanjutan** | | | |
| 07 | [Integrasi Carian Semantik](./07-Semantic-Search/README.md) | Melaksanakan penyerapan vektor dengan Azure OpenAI dan pgvector | [Maju](./07-Semantic-Search/README.md) |
| 08 | [Pengujian dan Penyahpepijatan](./08-Testing/README.md) | Strategi pengujian, alat penyahpepijatan, dan pendekatan pengesahan | [Uji](./08-Testing/README.md) |
| 09 | [Integrasi VS Code](./09-VS-Code/README.md) | Mengkonfigurasi integrasi MCP VS Code dan penggunaan Chat AI | [Integrasi](./09-VS-Code/README.md) |
| **Makmal 10-12: Pengeluaran dan Amalan Terbaik** | | | |
| 10 | [Strategi Penempatan](./10-Deployment/README.md) | Pelaksanaan Docker, Azure Container Apps, dan pertimbangan skala | [Tempatkan](./10-Deployment/README.md) |
| 11 | [Pemantauan dan Kebolehpantauan](./11-Monitoring/README.md) | Application Insights, log, pemantauan prestasi | [Pantau](./11-Monitoring/README.md) |
| 12 | [Amalan Terbaik dan Pengoptimuman](./12-Best-Practices/README.md) | Pengoptimuman prestasi, pengukuhan keselamatan, dan petua pengeluaran | [Optimakan](./12-Best-Practices/README.md) |

### 💻 Apa Yang Akan Anda Bina

Pada akhir laluan pembelajaran ini, anda akan membina **Pelayan MCP Analitik Runcit Zava** lengkap yang mempunyai:

- **Pangkalan data runcit berbilang jadual** dengan pesanan pelanggan, produk, dan inventori
- **Keselamatan Tahap Baris** untuk pengasingan data berdasarkan kedai
- **Carian produk semantik** menggunakan penyerapan Azure OpenAI
- **Integrasi Chat AI VS Code** untuk pertanyaan bahasa semula jadi
- **Penempatan sedia produksi** dengan Docker dan Azure
- **Pemantauan menyeluruh** dengan Application Insights

## 🎯 Prasyarat untuk Pembelajaran

Untuk mendapatkan manfaat maksimum daripada laluan pembelajaran ini, anda harus:

- **Pengalaman Pengaturcaraan**: Kefahaman dengan Python (lebih digalakkan) atau bahasa serupa
- **Pengetahuan Pangkalan Data**: Pemahaman asas SQL dan pangkalan data berhubung
- **Konsep API**: Memahami API REST dan konsep HTTP
- **Alat Pembangunan**: Pengalaman menggunakan baris arahan, Git, dan penyunting kod
- **Asas Awan**: (Pilihan) Pengetahuan asas Azure atau platform awan serupa
- **Familiariti Docker**: (Pilihan) Memahami konsep pengkontenan

### Alat Diperlukan

- **Docker Desktop** - Untuk menjalankan PostgreSQL dan pelayan MCP
- **Azure CLI** - Untuk penempatan sumber awan
- **VS Code** - Untuk pembangunan dan integrasi MCP
- **Git** - Untuk kawalan versi
- **Python 3.8+** - Untuk pembangunan pelayan MCP

## 📚 Panduan Kajian & Sumber

Laluan pembelajaran ini merangkumi sumber menyeluruh untuk membantu anda menavigasi dengan berkesan:

### Panduan Kajian

Setiap makmal mengandungi:
- **Objektif pembelajaran yang jelas** - Apa yang akan anda capai
- **Arahan langkah demi langkah** - Panduan pelaksanaan terperinci
- **Contoh kod** - Sampel berfungsi dengan penjelasan
- **Latihan** - Peluang amali secara langsung
- **Panduan penyelesaian masalah** - Isu biasa dan penyelesaian
- **Sumber tambahan** - Bacaan dan penerokaan lanjut

### Semakan Prasyarat

Sebelum memulakan setiap makmal, anda akan menemui:
- **Pengetahuan diperlukan** - Apa yang harus anda tahu terlebih dahulu
- **Pengesahan persediaan** - Cara mengesahkan persekitaran anda
- **Anggaran masa** - Jangka masa yang dijangkakan untuk selesai
- **Hasil pembelajaran** - Apa yang anda akan tahu selepas selesai

### Laluan Pembelajaran Disyorkan

Pilih laluan anda berdasarkan tahap pengalaman anda:

#### 🟢 **Laluan Permulaan** (Baru kepada MCP)
1. Pastikan anda telah menamatkan 0-10 dari [MCP untuk Pemula](https://aka.ms/mcp-for-beginners) terlebih dahulu
2. Lengkapkan makmal 00-03 untuk mengukuhkan asas anda
3. Ikuti makmal 04-06 untuk pembinaan praktikal
4. Cuba makmal 07-09 untuk penggunaan praktikal

#### 🟡 **Laluan Pertengahan** (Sedikit Pengalaman MCP)
1. Tinjau makmal 00-01 untuk konsep khusus pangkalan data
2. Fokus pada makmal 02-06 untuk pelaksanaan
3. Selami makmal 07-12 untuk ciri lanjutan

#### 🔴 **Laluan Lanjutan** (Berkemahiran dengan MCP)
1. Lihat makmal 00-03 untuk konteks
2. Fokus pada makmal 04-09 untuk integrasi pangkalan data
3. Tumpukan pada makmal 10-12 untuk penempatan pengeluaran

## 🛠️ Cara Menggunakan Laluan Pembelajaran Ini dengan Berkesan

### Pembelajaran Berurutan (Disyorkan)

Kerjakan makmal mengikut urutan untuk pemahaman menyeluruh:

1. **Baca gambaran keseluruhan** - Fahami apa yang akan anda pelajari
2. **Semak prasyarat** - Pastikan anda mempunyai pengetahuan yang diperlukan
3. **Ikuti panduan langkah demi langkah** - Laksanakan semasa belajar
4. **Lengkapkan latihan** - Kukuhkan pemahaman anda
5. **Ulas perkara penting** - Kukuhkan hasil pembelajaran

### Pembelajaran Bertarget

Jika anda memerlukan kemahiran tertentu:

- **Integrasi Pangkalan Data**: Fokus pada makmal 04-06
- **Pelaksanaan Keselamatan**: Kelompok pada makmal 02, 08, 12
- **Carian AI/Semantik**: Selami makmal 07
- **Penempatan Pengeluaran**: Kajian makmal 10-12

### Amali Praktikal

Setiap makmal mengandungi:
- **Contoh kod yang berfungsi** - Salin, ubah suai, dan eksperimen
- **Senario dunia sebenar** - Kes penggunaan analitik runcit praktikal
- **Kerumitan progresif** - Membina dari mudah ke lanjutan
- **Langkah pengesahan** - Sahkan pelaksanaan berfungsi

## 🌟 Komuniti dan Sokongan

### Dapatkan Bantuan

- **Azure AI Discord**: [Sertai untuk sokongan pakar](https://discord.com/invite/ByRwuEEgH4)
- **Repositori GitHub dan Contoh Pelaksanaan**: [Contoh Penempatan dan Sumber](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Komuniti MCP**: [Sertai perbincangan MCP yang lebih luas](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Sedia untuk Bermula?

Mulakan perjalanan anda dengan **[Makmal 00: Pengenalan kepada Integrasi Pangkalan Data MCP](./00-Introduction/README.md)**

---

*Menguasai pembangunan pelayan MCP sedia produksi dengan integrasi pangkalan data melalui pengalaman pembelajaran praktikal yang lengkap ini.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->