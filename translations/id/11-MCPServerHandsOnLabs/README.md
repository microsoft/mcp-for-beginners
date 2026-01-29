# 🚀 Server MCP dengan PostgreSQL - Panduan Belajar Lengkap

## 🧠 Gambaran Umum Jalur Pembelajaran Integrasi Database MCP

Panduan belajar ini mengajarkan cara membangun **server Model Context Protocol (MCP)** yang siap produksi dengan integrasi database melalui implementasi analitik ritel yang praktis. Anda akan mempelajari pola tingkat perusahaan seperti **Row Level Security (RLS)**, **pencarian semantik**, **integrasi Azure AI**, dan **akses data multi-tenant**.

Baik Anda seorang pengembang backend, insinyur AI, atau arsitek data, panduan ini menyediakan pembelajaran terstruktur dengan contoh dunia nyata dan latihan langsung yang akan membawa Anda melalui server MCP https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Sumber Daya Resmi MCP

- 📘 [Dokumentasi MCP](https://modelcontextprotocol.io/) – Tutorial dan panduan pengguna yang mendetail
- 📜 [Spesifikasi MCP](https://modelcontextprotocol.io/docs/) – Arsitektur protokol dan referensi teknis
- 🧑‍💻 [Repositori GitHub MCP](https://github.com/modelcontextprotocol) – SDK open-source, alat, dan contoh kode
- 🌐 [Komunitas MCP](https://github.com/orgs/modelcontextprotocol/discussions) – Bergabunglah dalam diskusi dan berkontribusi pada komunitas

## 🧭 Jalur Pembelajaran Integrasi Database MCP

### 📚 Struktur Pembelajaran Lengkap untuk https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Lab | Topik | Deskripsi | Tautan |
|--------|-------|-------------|------|
| **Lab 1-3: Dasar-Dasar** | | | |
| 00 | [Pengantar Integrasi Database MCP](./00-Introduction/README.md) | Gambaran umum MCP dengan integrasi database dan kasus penggunaan analitik ritel | [Mulai di Sini](./00-Introduction/README.md) |
| 01 | [Konsep Arsitektur Inti](./01-Architecture/README.md) | Memahami arsitektur server MCP, lapisan database, dan pola keamanan | [Pelajari](./01-Architecture/README.md) |
| 02 | [Keamanan dan Multi-Tenancy](./02-Security/README.md) | Row Level Security, autentikasi, dan akses data multi-tenant | [Pelajari](./02-Security/README.md) |
| 03 | [Pengaturan Lingkungan](./03-Setup/README.md) | Menyiapkan lingkungan pengembangan, Docker, sumber daya Azure | [Pengaturan](./03-Setup/README.md) |
| **Lab 4-6: Membangun Server MCP** | | | |
| 04 | [Desain Database dan Skema](./04-Database/README.md) | Pengaturan PostgreSQL, desain skema ritel, dan data sampel | [Bangun](./04-Database/README.md) |
| 05 | [Implementasi Server MCP](./05-MCP-Server/README.md) | Membangun server FastMCP dengan integrasi database | [Bangun](./05-MCP-Server/README.md) |
| 06 | [Pengembangan Alat](./06-Tools/README.md) | Membuat alat kueri database dan introspeksi skema | [Bangun](./06-Tools/README.md) |
| **Lab 7-9: Fitur Lanjutan** | | | |
| 07 | [Integrasi Pencarian Semantik](./07-Semantic-Search/README.md) | Mengimplementasikan embedding vektor dengan Azure OpenAI dan pgvector | [Lanjutkan](./07-Semantic-Search/README.md) |
| 08 | [Pengujian dan Debugging](./08-Testing/README.md) | Strategi pengujian, alat debugging, dan pendekatan validasi | [Uji](./08-Testing/README.md) |
| 09 | [Integrasi VS Code](./09-VS-Code/README.md) | Mengonfigurasi integrasi MCP di VS Code dan penggunaan AI Chat | [Integrasi](./09-VS-Code/README.md) |
| **Lab 10-12: Produksi dan Praktik Terbaik** | | | |
| 10 | [Strategi Penerapan](./10-Deployment/README.md) | Penerapan Docker, Azure Container Apps, dan pertimbangan skalabilitas | [Terapkan](./10-Deployment/README.md) |
| 11 | [Pemantauan dan Observabilitas](./11-Monitoring/README.md) | Application Insights, logging, pemantauan kinerja | [Pantau](./11-Monitoring/README.md) |
| 12 | [Praktik Terbaik dan Optimasi](./12-Best-Practices/README.md) | Optimasi kinerja, penguatan keamanan, dan tips produksi | [Optimalkan](./12-Best-Practices/README.md) |

### 💻 Apa yang Akan Anda Bangun

Pada akhir jalur pembelajaran ini, Anda akan membangun **Server MCP Zava Retail Analytics** yang lengkap dengan fitur:

- **Database ritel multi-tabel** dengan pesanan pelanggan, produk, dan inventaris
- **Row Level Security** untuk isolasi data berbasis toko
- **Pencarian produk semantik** menggunakan embedding Azure OpenAI
- **Integrasi AI Chat di VS Code** untuk kueri bahasa alami
- **Penerapan siap produksi** dengan Docker dan Azure
- **Pemantauan komprehensif** dengan Application Insights

## 🎯 Prasyarat untuk Belajar

Untuk mendapatkan manfaat maksimal dari jalur pembelajaran ini, Anda sebaiknya memiliki:

- **Pengalaman Pemrograman**: Familiar dengan Python (disarankan) atau bahasa serupa
- **Pengetahuan Database**: Pemahaman dasar tentang SQL dan database relasional
- **Konsep API**: Pemahaman tentang REST API dan konsep HTTP
- **Alat Pengembangan**: Pengalaman dengan command line, Git, dan editor kode
- **Dasar-Dasar Cloud**: (Opsional) Pengetahuan dasar tentang Azure atau platform cloud serupa
- **Familiaritas Docker**: (Opsional) Pemahaman tentang konsep kontainerisasi

### Alat yang Dibutuhkan

- **Docker Desktop** - Untuk menjalankan PostgreSQL dan server MCP
- **Azure CLI** - Untuk penerapan sumber daya cloud
- **VS Code** - Untuk pengembangan dan integrasi MCP
- **Git** - Untuk kontrol versi
- **Python 3.8+** - Untuk pengembangan server MCP

## 📚 Panduan Belajar & Sumber Daya

Jalur pembelajaran ini mencakup sumber daya komprehensif untuk membantu Anda belajar secara efektif:

### Panduan Belajar

Setiap lab mencakup:
- **Tujuan pembelajaran yang jelas** - Apa yang akan Anda capai
- **Instruksi langkah demi langkah** - Panduan implementasi yang mendetail
- **Contoh kode** - Sampel kerja dengan penjelasan
- **Latihan** - Kesempatan untuk praktik langsung
- **Panduan pemecahan masalah** - Masalah umum dan solusinya
- **Sumber daya tambahan** - Bacaan dan eksplorasi lebih lanjut

### Pemeriksaan Prasyarat

Sebelum memulai setiap lab, Anda akan menemukan:
- **Pengetahuan yang diperlukan** - Apa yang harus Anda ketahui sebelumnya
- **Validasi pengaturan** - Cara memverifikasi lingkungan Anda
- **Estimasi waktu** - Perkiraan waktu penyelesaian
- **Hasil pembelajaran** - Apa yang akan Anda ketahui setelah selesai

### Jalur Pembelajaran yang Direkomendasikan

Pilih jalur berdasarkan tingkat pengalaman Anda:

#### 🟢 **Jalur Pemula** (Baru mengenal MCP)
1. Pastikan Anda telah menyelesaikan 0-10 dari [MCP untuk Pemula](https://aka.ms/mcp-for-beginners) terlebih dahulu
2. Selesaikan lab 00-03 untuk memperkuat pemahaman dasar
3. Ikuti lab 04-06 untuk praktik langsung
4. Coba lab 07-09 untuk penggunaan praktis

#### 🟡 **Jalur Menengah** (Memiliki pengalaman MCP)
1. Tinjau lab 00-01 untuk konsep spesifik database
2. Fokus pada lab 02-06 untuk implementasi
3. Pelajari lebih dalam lab 07-12 untuk fitur lanjutan

#### 🔴 **Jalur Lanjutan** (Berpengalaman dengan MCP)
1. Tinjau sekilas lab 00-03 untuk konteks
2. Fokus pada lab 04-09 untuk integrasi database
3. Konsentrasi pada lab 10-12 untuk penerapan produksi

## 🛠️ Cara Menggunakan Jalur Pembelajaran Ini Secara Efektif

### Pembelajaran Berurutan (Direkomendasikan)

Kerjakan lab secara berurutan untuk pemahaman yang komprehensif:

1. **Baca gambaran umum** - Pahami apa yang akan Anda pelajari
2. **Periksa prasyarat** - Pastikan Anda memiliki pengetahuan yang diperlukan
3. **Ikuti panduan langkah demi langkah** - Implementasikan sambil belajar
4. **Selesaikan latihan** - Perkuat pemahaman Anda
5. **Tinjau poin penting** - Perkuat hasil pembelajaran

### Pembelajaran Terarah

Jika Anda membutuhkan keterampilan tertentu:

- **Integrasi Database**: Fokus pada lab 04-06
- **Implementasi Keamanan**: Konsentrasi pada lab 02, 08, 12
- **AI/Pencarian Semantik**: Pelajari lebih dalam lab 07
- **Penerapan Produksi**: Pelajari lab 10-12

### Praktik Langsung

Setiap lab mencakup:
- **Contoh kode yang berfungsi** - Salin, modifikasi, dan eksperimen
- **Skenario dunia nyata** - Kasus penggunaan analitik ritel yang praktis
- **Kompleksitas progresif** - Membangun dari dasar hingga lanjutan
- **Langkah validasi** - Verifikasi bahwa implementasi Anda berfungsi

## 🌟 Komunitas dan Dukungan

### Dapatkan Bantuan

- **Discord Azure AI**: [Bergabung untuk dukungan ahli](https://discord.com/invite/ByRwuEEgH4)
- **Repositori GitHub dan Sampel Implementasi**: [Sampel Penerapan dan Sumber Daya](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **Komunitas MCP**: [Bergabunglah dalam diskusi MCP yang lebih luas](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Siap Memulai?

Mulailah perjalanan Anda dengan **[Lab 00: Pengantar Integrasi Database MCP](./00-Introduction/README.md)**

---

*Kuasi pembangunan server MCP yang siap produksi dengan integrasi database melalui pengalaman belajar yang komprehensif dan langsung.*

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.