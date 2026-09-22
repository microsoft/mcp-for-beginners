# 🚀 Server MCP dengan PostgreSQL - Panduan Pembelajaran Lengkap

## 🧠 Gambaran Jalur Pembelajaran Integrasi Database MCP

Panduan pembelajaran komprehensif ini mengajarkan Anda cara membangun **server Model Context Protocol (MCP)** siap produksi yang terintegrasi dengan database melalui implementasi praktis analitik ritel. Anda akan mempelajari pola kelas perusahaan termasuk **Row Level Security (RLS)**, **pencarian semantik**, **integrasi Azure AI**, dan **akses data multi-tenant**.

Baik Anda seorang pengembang backend, insinyur AI, atau arsitek data, panduan ini menyediakan pembelajaran terstruktur dengan contoh dunia nyata dan latihan langsung yang memandu Anda melalui server MCP berikut https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Sumber Resmi MCP

- 📘 [Dokumentasi MCP](https://modelcontextprotocol.io/) – Tutorial rinci dan panduan pengguna
- 📜 [Spesifikasi MCP (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Arsitektur protokol dan referensi teknis
- 🧑‍💻 [Repositori GitHub MCP](https://github.com/modelcontextprotocol) – SDK open-source, alat, dan contoh kode
- 🌐 [Komunitas MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Bergabung dalam diskusi dan kontribusi komunitas
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Praktik keamanan terbaik dan mitigasi risiko


## 🧭 Jalur Pembelajaran Integrasi Database MCP

### 📚 Struktur Pembelajaran Lengkap untuk https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Lab | Topik | Deskripsi | Tautan |
|--------|-------|-------------|------|
| **Lab 1-3: Dasar-dasar** | | | |
| 00 | [Pengenalan Integrasi Database MCP](./00-Introduction/README.md) | Gambaran MCP dengan integrasi database dan kasus penggunaan analitik ritel | [Mulai Di Sini](./00-Introduction/README.md) |
| 01 | [Konsep Arsitektur Inti](./01-Architecture/README.md) | Memahami arsitektur server MCP, lapisan database, dan pola keamanan | [Pelajari](./01-Architecture/README.md) |
| 02 | [Keamanan dan Multi-Tenancy](./02-Security/README.md) | Row Level Security, autentikasi, dan akses data multi-tenant | [Pelajari](./02-Security/README.md) |
| 03 | [Penyiapan Lingkungan](./03-Setup/README.md) | Menyiapkan lingkungan pengembangan, Docker, sumber daya Azure | [Siapkan](./03-Setup/README.md) |
| **Lab 4-6: Membangun Server MCP** | | | |
| 04 | [Desain Database dan Skema](./04-Database/README.md) | Pengaturan PostgreSQL, desain skema ritel, dan data sampel | [Bangun](./04-Database/README.md) |
| 05 | [Implementasi Server MCP](./05-MCP-Server/README.md) | Membangun server FastMCP dengan integrasi database | [Bangun](./05-MCP-Server/README.md) |
| 06 | [Pengembangan Alat](./06-Tools/README.md) | Membuat alat kueri database dan introspeksi skema | [Bangun](./06-Tools/README.md) |
| **Lab 7-9: Fitur Lanjutan** | | | |
| 07 | [Integrasi Pencarian Semantik](./07-Semantic-Search/README.md) | Mengimplementasikan embedding vektor dengan Azure OpenAI dan pgvector | [Lanjutkan](./07-Semantic-Search/README.md) |
| 08 | [Pengujian dan Debugging](./08-Testing/README.md) | Strategi pengujian, alat debugging, dan pendekatan validasi | [Uji](./08-Testing/README.md) |
| 09 | [Integrasi VS Code](./09-VS-Code/README.md) | Mengonfigurasi integrasi VS Code MCP dan penggunaan AI Chat | [Integrasi](./09-VS-Code/README.md) |
| **Lab 10-12: Produksi dan Praktik Terbaik** | | | |
| 10 | [Strategi Penyebaran](./10-Deployment/README.md) | Penyebaran Docker, Azure Container Apps, dan pertimbangan skala | [Sebarkan](./10-Deployment/README.md) |
| 11 | [Pemantauan dan Observabilitas](./11-Monitoring/README.md) | Application Insights, pencatatan, pemantauan kinerja | [Pantau](./11-Monitoring/README.md) |
| 12 | [Praktik Terbaik dan Optimisasi](./12-Best-Practices/README.md) | Optimisasi kinerja, penguatan keamanan, dan tips produksi | [Optimalkan](./12-Best-Practices/README.md) |

### 💻 Apa yang Akan Anda Bangun

Di akhir jalur pembelajaran ini, Anda akan membangun **Server MCP Analitik Ritel Zava** lengkap yang menampilkan:

- **Database ritel multi-tabel** dengan order pelanggan, produk, dan inventaris
- **Row Level Security** untuk isolasi data berbasis toko
- **Pencarian produk semantik** menggunakan embedding Azure OpenAI
- **Integrasi AI Chat VS Code** untuk kueri bahasa alami
- **Penyebaran siap produksi** dengan Docker dan Azure
- **Pemantauan menyeluruh** dengan Application Insights

## 🎯 Prasyarat untuk Belajar

Untuk mendapatkan hasil maksimal dari jalur pembelajaran ini, Anda harus memiliki:

- **Pengalaman Pemrograman**: Familiar dengan Python (lebih disukai) atau bahasa serupa
- **Pengetahuan Database**: Pemahaman dasar SQL dan database relasional
- **Konsep API**: Memahami REST API dan konsep HTTP
- **Alat Pengembangan**: Pengalaman menggunakan command line, Git, dan editor kode
- **Dasar Cloud**: (Opsional) Pengetahuan dasar Azure atau platform cloud serupa
- **Familiaritas Docker**: (Opsional) Memahami konsep containerisasi

### Alat yang Dibutuhkan

- **Docker Desktop** - Untuk menjalankan PostgreSQL dan server MCP
- **Azure CLI** - Untuk penyebaran sumber daya cloud
- **VS Code** - Untuk pengembangan dan integrasi MCP
- **Git** - Untuk kontrol versi
- **Python 3.8+** - Untuk pengembangan server MCP

## 📚 Panduan Studi & Sumber Daya

Jalur pembelajaran ini mencakup sumber daya lengkap untuk membantu Anda menavigasi secara efektif:

### Panduan Studi

Setiap lab mencakup:
- **Tujuan pembelajaran jelas** - Apa yang akan Anda capai
- **Instruksi langkah demi langkah** - Panduan implementasi rinci
- **Contoh kode** - Contoh kerja dengan penjelasan
- **Latihan** - Kesempatan praktik langsung
- **Panduan pemecahan masalah** - Masalah umum dan solusinya
- **Sumber tambahan** - Bacaan dan eksplorasi lebih lanjut

### Pemeriksaan Prasyarat

Sebelum memulai setiap lab, Anda akan menemukan:
- **Pengetahuan yang diperlukan** - Apa yang harus Anda ketahui sebelumnya
- **Validasi penyiapan** - Cara memverifikasi lingkungan Anda
- **Estimasi waktu** - Perkiraan waktu penyelesaian
- **Hasil pembelajaran** - Apa yang akan Anda ketahui setelah selesai

### Jalur Pembelajaran yang Direkomendasikan

Pilih jalur Anda berdasarkan tingkat pengalaman:

#### 🟢 **Jalur Pemula** (Baru di MCP)
1. Pastikan Anda telah menyelesaikan 0-10 dari [MCP untuk Pemula](https://aka.ms/mcp-for-beginners) terlebih dahulu
2. Selesaikan lab 00-03 untuk memperkuat dasar-dasar Anda
3. Ikuti lab 04-06 untuk praktik langsung membangun
4. Cobalah lab 07-09 untuk penggunaan praktis

#### 🟡 **Jalur Menengah** (Berpengalaman Sedikit MCP)
1. Tinjau lab 00-01 untuk konsep khusus database
2. Fokus pada lab 02-06 untuk implementasi
3. Selami lab 07-12 untuk fitur lanjutan

#### 🔴 **Jalur Lanjutan** (Berpengalaman dengan MCP)
1. Baca sekilas lab 00-03 untuk konteks
2. Fokus pada lab 04-09 untuk integrasi database
3. Konsentrasikan pada lab 10-12 untuk penyebaran produksi

## 🛠️ Cara Menggunakan Jalur Pembelajaran Ini Secara Efektif

### Pembelajaran Berurutan (Direkomendasikan)

Kerjakan lab secara berurutan untuk pemahaman menyeluruh:

1. **Baca gambaran** - Pahami apa yang akan Anda pelajari
2. **Periksa prasyarat** - Pastikan Anda memiliki pengetahuan yang diperlukan
3. **Ikuti panduan langkah demi langkah** - Implementasi saat belajar
4. **Selesaikan latihan** - Perkuat pemahaman Anda
5. **Tinjau poin penting** - Kuatkan hasil pembelajaran

### Pembelajaran Terfokus

Jika Anda membutuhkan keterampilan khusus:

- **Integrasi Database**: Fokus pada lab 04-06
- **Implementasi Keamanan**: Konsentrasikan pada lab 02, 08, 12
- **AI/Pencarian Semantik**: Selami lab 07
- **Penyebaran Produksi**: Pelajari lab 10-12

### Latihan Praktis

Setiap lab mencakup:
- **Contoh kode yang bekerja** - Salin, modifikasi, dan bereksperimen
- **Skenario dunia nyata** - Kasus penggunaan analitik ritel praktis
- **Kompleksitas bertahap** - Membangun dari sederhana ke lanjutan
- **Langkah validasi** - Verifikasi implementasi Anda berhasil

## 🌟 Komunitas dan Dukungan

### Dapatkan Bantuan

- **Azure AI Discord**: [Bergabung untuk dukungan ahli](https://discord.com/invite/ByRwuEEgH4)
- **Repo GitHub dan Contoh Implementasi**: [Contoh Penyebaran dan Sumber Daya](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Komunitas MCP**: [Bergabung dalam diskusi MCP yang lebih luas](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Siap Memulai?

Mulailah perjalanan Anda dengan **[Lab 00: Pengenalan Integrasi Database MCP](./00-Introduction/README.md)**

---

*Kuasi membangun server MCP siap produksi dengan integrasi database melalui pengalaman pembelajaran langsung dan komprehensif ini.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->