# Changelog: Kurikulum MCP untuk Pemula

Dokumen ini berfungsi sebagai catatan semua perubahan signifikan yang dibuat pada kurikulum Model Context Protocol (MCP) untuk Pemula. Perubahan didokumentasikan dalam urutan kronologis terbalik (perubahan terbaru di awal).

## 11 April 2026

### Pelajaran Baru, Perbaikan Dokumentasi, dan Pembaruan Dependensi

#### Konten Kurikulum Baru Ditambahkan

**Modul 05 - Topik Lanjutan**  
- **Pelajaran 5.17: Penalaran Multi-Agen Adversarial dengan MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Panduan komprehensif baru yang membahas pola debat adversarial untuk sistem multi-agen  
  - Diagram arsitektur Mermaid: dua agen → server MCP bersama → transkrip debat → juri → keputusan  
  - Server alat MCP bersama (`web_search` + `run_python`) diimplementasikan dalam Python dan TypeScript  
  - Prompt sistem yang berlawanan (FOR / AGAINST / Juri) dengan persyaratan penggunaan alat yang eksplisit  
  - Orkestrator debat dalam Python, TypeScript, dan C# mengelola putaran dan mengarahkan argumen  
  - Koneksi `ClientSession` MCP untuk orkestrator ke panggilan alat nyata  
  - Tabel kasus penggunaan (deteksi halusinasi, pemodelan ancaman, tinjauan desain API, verifikasi fakta, pemilihan teknologi)  
  - Pertimbangan keamanan: eksekusi dalam sandbox, validasi panggilan alat, pembatasan laju, pencatatan audit  
  - Latihan terstruktur dengan tiga skenario praktis (tinjauan kode, keputusan arsitektur, moderasi konten)  

#### Perbaikan Dokumentasi

**Modul 03 - Memulai**  
- **05-stdio-server/README.md**: Memperbaiki contoh server stdio TypeScript yang tidak lengkap — menambahkan instansiasi transport yang hilang (`new StdioServerTransport()`) dan panggilan `server.connect(transport)` agar sesuai dengan contoh Python dan .NET di bagian yang sama  
- **14-sampling/README.md**: Memperbaiki typo — mengoreksi `"Sampling is an davanced features"` menjadi `"Sampling is an advanced feature"`  

#### Pembaruan Kurikulum

**Main README.md**  
- Menambahkan entri 5.17 (Penalaran Multi-Agen Adversarial dengan MCP) ke tabel kurikulum dengan tautan langsung ke pelajaran baru  

**05-AdvancedTopics/README.md**  
- Menambahkan baris Pelajaran 5.17 ke tabel pelajaran  

**study_guide.md**  
- Menambahkan topik Penalaran Multi-Agen Adversarial ke mind-map dan deskripsi naratif Topik Lanjutan  

#### Perbaikan Kode dan Keamanan

**Modul 05 - Agen Adversarial (`mcp-adversarial-agents`)**  
- **Perbaikan keamanan — injeksi perintah**: Mengganti interpolasi shell `execSync` dengan `execFile` + `promisify` dalam alat TypeScript `run_python`, menghilangkan permukaan injeksi perintah (kode yang dikontrol LLM sekarang diteruskan sebagai elemen argv literal tanpa keterlibatan shell)  
- **Pengkabelan loop alat MCP**: Memperbarui orkestrator debat Python untuk menggunakan klien `AsyncAnthropic` (mengganti `Anthropic` sinkron yang memblokir), meneruskan `ClientSession` langsung ke setiap giliran agen, mengambil definisi alat lewat `session.list_tools()` setiap giliran, dan mengirim blok `tool_use` melalui `session.call_tool()` secara berulang hingga model menghasilkan respons teks akhir  

#### Pembaruan Dependensi

- Meningkatkan `hono` ke versi 4.12.12 di berbagai paket (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)  
- Meningkatkan `@hono/node-server` dari 1.19.11 ke 1.19.13 dalam paket TypeScript  
- Meningkatkan `cryptography` dari 46.0.5 ke 46.0.7 dalam paket Python (lab 3 dan 4 10-StreamliningAIWorkflows)  
- Meningkatkan `lodash` dari 4.17.23 ke 4.18.1 dalam inspector 10-StreamliningAIWorkflows  

#### Terjemahan

- Menyinkronkan terjemahan untuk lebih dari 48 bahasa sesuai dengan perubahan sumber terbaru (pembaruan i18n)  

---

## 5 Februari 2026

### Validasi dan Perbaikan Navigasi Seluruh Repositori

#### Konten Kurikulum Baru Ditambahkan

**Modul 03 - Memulai**  
- **12-mcp-hosts/README.md**: Panduan komprehensif baru untuk mengatur host MCP  
  - Contoh konfigurasi Claude Desktop, VS Code, Cursor, Cline, Windsurf  
  - Template konfigurasi JSON untuk semua host utama  
  - Tabel perbandingan tipe transport (stdio, SSE/HTTP, WebSocket)  
  - Pemecahan masalah masalah koneksi umum  
  - Praktik terbaik keamanan untuk konfigurasi host  

- **13-mcp-inspector/README.md**: Panduan debugging baru untuk MCP Inspector  
  - Metode instalasi (npx, npm global, dari sumber)  
  - Menghubungkan ke server lewat stdio dan HTTP/SSE  
  - Pengujian alat, sumber daya, dan alur kerja prompt  
  - Integrasi VS Code dengan MCP Inspector  
  - Skenario debugging umum dengan solusi  

**Modul 04 - Implementasi Praktis**  
- **pagination/README.md**: Panduan implementasi pagination baru  
  - Pola pagination berbasis cursor dalam Python, TypeScript, Java  
  - Penanganan pagination sisi klien  
  - Strategi desain cursor (opaque vs structured)  
  - Rekomendasi optimasi performa  

**Modul 05 - Topik Lanjutan**  
- **mcp-protocol-features/README.md**: Penjelasan mendalam fitur protokol baru  
  - Implementasi notifikasi progres  
  - Pola pembatalan permintaan  
  - Template sumber daya dengan pola URI  
  - Manajemen siklus hidup server  
  - Kontrol level pencatatan  
  - Pola penanganan kesalahan dengan kode JSON-RPC  

#### Perbaikan Navigasi (lebih dari 24 file diperbarui)

**README Modul Utama**  
 Sekarang tautan ke pelajaran pertama DAN modul berikutnya  

**02-Security Sub-file**  
- Kelima dokumen keamanan pendukung kini memiliki navigasi "Apa Selanjutnya":  

**09-CaseStudy Files**  
- Semua file studi kasus sekarang memiliki navigasi berurutan:  

**10-StreamliningAI Labs**  
Menambahkan bagian Apa Selanjutnya ke tinjauan Modul 10 dan Modul 11  

#### Perbaikan Kode dan Konten

**Pembaruan SDK dan Dependensi**  
Memperbaiki versi openai kosong menjadi `^4.95.0`  
Memperbarui SDK dari `^1.8.0` ke `>=1.26.0`  
Memperbarui pin versi mcp ke `>=1.26.0`  

**Perbaikan Kode**  
Memperbaiki model tidak valid `gpt-4o-mini` menjadi `gpt-4.1-mini`  

**Perbaikan Konten**  
Memperbaiki tautan rusak `READMEmd` → `README.md`, memperbaiki header kurikulum `Module 1-3` → `Module 0-3`, memperbaiki path yang case-sensitive  
Menghapus konten duplikat studi kasus 5 yang rusak  

**Peningkatan Panduan Pemula**  
Menambahkan pengenalan yang tepat, tujuan belajar, dan prasyarat bagi pemula  

#### Pembaruan Kurikulum

**Main README.md**  
- Menambahkan entri 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Protocol Features) ke tabel kurikulum  

**Module README**  
Menambahkan pelajaran 12 dan 13 ke daftar pelajaran  
Menambahkan bagian Panduan Praktis dengan tautan pagination  
Menambahkan pelajaran 5.15 (Custom Transport) dan 5.16 (Protocol Features)  

**study_guide.md**  
- Memperbarui mindmap dengan semua topik baru: Pengaturan MCP Hosts, MCP Inspector, Strategi Pagination, Penjelasan Mendalam Fitur Protokol  

## 28 Januari 2026

### Tinjauan Kepatuhan Spesifikasi MCP 2025-11-25

#### Peningkatan Konsep Inti (01-CoreConcepts/)  
- **Primitive Klien Baru - Roots**: Menambahkan dokumentasi komprehensif tentang primitive klien Roots yang memungkinkan server memahami batas sistem berkas dan izin akses  
- **Anotasi Alat**: Menambahkan dokumentasi tentang anotasi perilaku alat (`readOnlyHint`, `destructiveHint`) untuk pengambilan keputusan eksekusi alat yang lebih baik  
- **Pemanggilan Alat dalam Sampling**: Memperbarui dokumentasi Sampling untuk menyertakan parameter `tools` dan `toolChoice` untuk pemanggilan alat yang didorong model saat permintaan sampling  
- **Elicitation Mode URL**: Menambahkan dokumentasi tentang elicitation berbasis URL untuk interaksi web eksternal yang diinisiasi server  
- **Tugas (Eksperimental)**: Menambahkan bagian baru yang mendokumentasikan fitur tugas eksperimental untuk pembungkus eksekusi tahan lama dan pengambilan hasil tertunda  
- **Dukungan Ikon**: Mencatat bahwa alat, sumber daya, template sumber daya, dan prompt kini dapat menyertakan ikon sebagai metadata tambahan  

#### Pembaruan Dokumentasi  
- **README.md**: Menambahkan referensi versi Spesifikasi MCP 2025-11-25 dan penjelasan versi berdasarkan tanggal  
- **study_guide.md**: Memperbarui peta kurikulum untuk menyertakan Tugas dan Anotasi Alat di bagian Konsep Inti; memperbarui timestamp dokumen  

#### Verifikasi Kepatuhan Spesifikasi  
- **Versi Protokol**: Memverifikasi semua dokumentasi mengacu pada Spesifikasi MCP 2025-11-25 terkini  
- **Keselarasan Arsitektur**: Mengonfirmasi akurasi dokumentasi arsitektur dua lapis (Lapisan Data + Lapisan Transport)  
- **Dokumentasi Primitives**: Memvalidasi primitives server (Resources, Prompts, Tools) dan primitives klien (Sampling, Elicitation, Logging, Roots)  
- **Mekanisme Transport**: Memverifikasi akurasi dokumentasi transport STDIO dan Streamable HTTP  
- **Panduan Keamanan**: Mengonfirmasi kesesuaian dengan dokumentasi Praktik Terbaik Keamanan MCP saat ini  

#### Fitur Kunci MCP 2025-11-25 yang Didokumentasikan  
- **Penemuan OpenID Connect**: Penemuan server autentikasi melalui OIDC  
- **Dokumen Metadata OAuth Client ID**: Mekanisme pendaftaran klien yang direkomendasikan  
- **JSON Schema 2020-12**: Dialek default untuk definisi skema MCP  
- **Sistem Tingkat SDK**: Persyaratan formal untuk dukungan dan pemeliharaan fitur SDK  
- **Struktur Tata Kelola**: Formalisasi Kelompok Kerja dan Kelompok Minat dalam tata kelola MCP  

### Pembaruan Besar Dokumentasi Keamanan (02-Security/)

#### Integrasi Workshop MCP Security Summit (Sherpa)  
- **Sumber Pelatihan Praktis Baru**: Menambahkan integrasi komprehensif dengan [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) di seluruh dokumentasi keamanan  
- **Jalur Ekspedisi Tercover**: Mendokumentasikan progresi lengkap dari Base Camp ke Summit  
- **Kesesuaian OWASP**: Semua panduan keamanan sekarang dipetakan ke risiko OWASP MCP Azure Security Guide  

#### Integrasi OWASP MCP Top 10  
- **Bagian Baru**: Menambahkan tabel Risiko Keamanan OWASP MCP Top 10 dengan mitigasi Azure di README utama Keamanan  
- **Dokumentasi Berbasis Risiko**: Memperbarui mcp-security-controls-2025.md dengan referensi risiko OWASP MCP untuk setiap domain keamanan  
- **Arsitektur Referensi**: Menautkan ke arsitektur referensi OWASP MCP Azure Security Guide dan pola implementasi  

#### File Keamanan yang Diperbarui  
- **README.md**: Menambahkan tinjauan Workshop Sherpa, tabel jalur ekspedisi, ringkasan risiko OWASP MCP Top 10, dan bagian pelatihan praktis  
- **mcp-security-controls-2025.md**: Memperbarui header ke Februari 2026, menambahkan referensi risiko OWASP (MCP01-MCP08), memperbaiki inkonsistensi versi spesifikasi  
- **mcp-security-best-practices-2025.md**: Menambahkan bagian sumber daya Sherpa dan OWASP, memperbarui timestamp  
- **mcp-best-practices.md**: Menambahkan bagian pelatihan praktis dengan tautan Sherpa dan OWASP  
- **azure-content-safety-implementation.md**: Menambahkan referensi OWASP MCP06, keselarasan Sherpa Camp 3, dan bagian sumber daya tambahan  

#### Tautan Sumber Daya Baru Ditambahkan  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- Halaman risiko OWASP MCP individual (MCP01-MCP10)  

### Penyelarasan Spesifikasi MCP 2025-11-25 Seluruh Kurikulum

#### Modul 03 - Memulai  
- **Dokumentasi SDK**: Menambahkan Go SDK ke daftar SDK resmi; memperbarui semua referensi SDK untuk selaras dengan Spesifikasi MCP 2025-11-25  
- **Klarifikasi Transport**: Memperbarui deskripsi transport STDIO dan HTTP Streaming dengan referensi spesifikasi eksplisit  

#### Modul 04 - Implementasi Praktis  
- **Pembaruan SDK**: Menambahkan Go SDK; memperbarui daftar SDK dengan referensi versi spesifikasi  
- **Spesifikasi Otorisasi**: Memperbarui tautan spesifikasi MCP Authorization ke versi 2025-11-25 yang terbaru  

#### Modul 05 - Topik Lanjutan  
- **Fitur Baru**: Menambahkan catatan mengenai fitur baru Spesifikasi MCP 2025-11-25 (Tugas, Anotasi Alat, Elicitation Mode URL, Roots)  
- **Sumber Daya Keamanan**: Menambahkan tautan OWASP MCP Top 10 dan workshop Sherpa ke referensi tambahan  

#### Modul 06 - Kontribusi Komunitas  
- **Daftar SDK**: Menambahkan SDK Swift dan Rust; memperbarui tautan spesifikasi ke 2025-11-25  
- **Referensi Spesifikasi**: Memperbarui tautan Spesifikasi MCP ke URL spesifikasi langsung  

#### Modul 07 - Pelajaran dari Adopsi Awal  
- **Pembaruan Sumber Daya**: Menambahkan tautan MCP Specification 2025-11-25 dan OWASP MCP Top 10 ke sumber daya tambahan  

#### Modul 08 - Praktik Terbaik  
- **Versi Spesifikasi**: Memperbarui referensi Spesifikasi MCP ke 2025-11-25  
- **Sumber Daya Keamanan**: Menambahkan OWASP MCP Top 10 dan workshop Sherpa ke referensi tambahan  

#### Modul 10 - Streamlining AI Workflows  
- **Pembaruan Lencana**: Mengubah lencana versi MCP dari versi SDK (1.9.3) ke versi spesifikasi (2025-11-25)  
- **Tautan Sumber Daya**: Memperbarui tautan MCP Specification; menambahkan OWASP MCP Top 10  

#### Modul 11 - MCP Server Hands-On Labs  
- **Referensi Spesifikasi**: Memperbarui tautan MCP Specification ke versi 2025-11-25  
- **Sumber Daya Keamanan**: Menambahkan OWASP MCP Top 10 ke sumber daya resmi  

## 18 Desember 2025
### Pembaruan Dokumentasi Keamanan - Spesifikasi MCP 2025-11-25

#### Praktik Keamanan Terbaik MCP (02-Security/mcp-best-practices.md) - Pembaruan Versi Spesifikasi
- **Pembaruan Versi Protokol**: Diperbarui untuk merujuk Spesifikasi MCP terbaru 2025-11-25 (dirilis 25 November 2025)
  - Memperbarui semua referensi versi spesifikasi dari 2025-06-18 ke 2025-11-25
  - Memperbarui referensi tanggal dokumen dari 18 Agustus 2025 ke 18 Desember 2025
  - Memastikan semua URL spesifikasi mengarah ke dokumentasi terkini
- **Validasi Konten**: Validasi menyeluruh atas praktik keamanan terbaik terhadap standar terbaru
  - **Solusi Keamanan Microsoft**: Memverifikasi terminologi dan tautan terkini untuk Prompt Shields (sebelumnya "deteksi risiko jailbreak"), Azure Content Safety, Microsoft Entra ID, dan Azure Key Vault
  - **Keamanan OAuth 2.1**: Memastikan keselarasan dengan praktik keamanan OAuth terbaru
  - **Standar OWASP**: Memvalidasi referensi OWASP Top 10 untuk LLM tetap mutakhir
  - **Layanan Azure**: Memverifikasi semua tautan dokumentasi dan praktik terbaik Microsoft Azure
- **Keselarasan Standar**: Semua standar keamanan yang dirujuk dikonfirmasi mutakhir
  - Kerangka Kerja Manajemen Risiko AI NIST
  - ISO 27001:2022
  - Praktik Keamanan Terbaik OAuth 2.1
  - Kerangka keamanan dan kepatuhan Azure
- **Sumber Daya Implementasi**: Memvalidasi semua tautan panduan implementasi dan sumber daya
  - Pola otentikasi Azure API Management
  - Panduan integrasi Microsoft Entra ID
  - Manajemen rahasia Azure Key Vault
  - Pipeline DevSecOps dan solusi pemantauan

### Penjaminan Mutu Dokumentasi
- **Kepatuhan Spesifikasi**: Memastikan semua persyaratan keamanan MCP wajib (HARUS/TIDAK BOLEH) selaras dengan spesifikasi terbaru
- **Kelengkapan Sumber Daya**: Memeriksa semua tautan eksternal ke dokumentasi Microsoft, standar keamanan, dan panduan implementasi
- **Cakupan Praktik Terbaik**: Memastikan cakupan komprehensif atas otentikasi, otorisasi, ancaman khusus AI, keamanan rantai pasokan, dan pola perusahaan

## 6 Oktober 2025

### Perluasan Bagian Memulai – Penggunaan Server Lanjutan & Otentikasi Sederhana

#### Penggunaan Server Lanjutan (03-GettingStarted/10-advanced)
- **Bab Baru Ditambahkan**: Memperkenalkan panduan lengkap penggunaan server MCP lanjutan, mencakup arsitektur server reguler dan tingkat rendah.
  - **Server Reguler vs. Tingkat Rendah**: Perbandingan detail dan contoh kode dalam Python dan TypeScript untuk kedua pendekatan.
  - **Desain Berbasis Handler**: Penjelasan manajemen alat/sumber daya/prompt berbasis handler untuk implementasi server yang scalable dan fleksibel.
  - **Pola Praktis**: Skenario dunia nyata di mana pola server tingkat rendah bermanfaat untuk fitur dan arsitektur lanjutan.

#### Otentikasi Sederhana (03-GettingStarted/11-simple-auth)
- **Bab Baru Ditambahkan**: Panduan langkah demi langkah untuk mengimplementasikan otentikasi sederhana di server MCP.
  - **Konsep Auth**: Penjelasan jelas tentang otentikasi vs. otorisasi, dan penanganan kredensial.
  - **Implementasi Auth Dasar**: Pola otentikasi berbasis middleware dalam Python (Starlette) dan TypeScript (Express), dengan contoh kode.
  - **Kemajuan ke Keamanan Lanjutan**: Panduan memulai dengan otentikasi sederhana dan berkembang ke OAuth 2.1 dan RBAC, lengkap dengan referensi modul keamanan lanjutan.

Penambahan ini menyediakan panduan praktis dan langsung untuk membangun implementasi server MCP yang lebih kuat, aman, dan fleksibel, menghubungkan konsep dasar dengan pola produksi lanjutan.

## 29 September 2025

### Laboratorium Integrasi Database Server MCP - Jalur Pembelajaran Praktik Komprehensif

#### 11-MCPServerHandsOnLabs - Kurikulum Integrasi Database Lengkap Baru
- **Jalur Pembelajaran 13-Lab Lengkap**: Menambahkan kurikulum praktik menyeluruh untuk membangun server MCP siap produksi dengan integrasi database PostgreSQL
  - **Implementasi Dunia Nyata**: Studi kasus analitik Zava Retail yang menunjukkan pola tingkat enterprise
  - **Progresi Pembelajaran Berstruktur**:
    - **Lab 00-03: Dasar** - Pengenalan, Arsitektur Inti, Keamanan & Multi-Tenant, Persiapan Lingkungan
    - **Lab 04-06: Membangun Server MCP** - Desain & Skema Database, Implementasi Server MCP, Pengembangan Alat  
    - **Lab 07-09: Fitur Lanjutan** - Integrasi Pencarian Semantik, Pengujian & Debugging, Integrasi VS Code
    - **Lab 10-12: Produksi & Praktik Terbaik** - Strategi Deployment, Pemantauan & Observabilitas, Praktik Terbaik & Optimasi
  - **Teknologi Enterprise**: Kerangka FastMCP, PostgreSQL dengan pgvector, embedding Azure OpenAI, Azure Container Apps, Application Insights
  - **Fitur Lanjutan**: Row Level Security (RLS), pencarian semantik, akses data multi-tenant, embedding vektor, pemantauan waktu nyata

#### Standarisasi Terminologi - Konversi Modul ke Lab
- **Pembaruan Dokumentasi Menyeluruh**: Memperbarui seluruh file README di 11-MCPServerHandsOnLabs untuk menggunakan terminologi "Lab" menggantikan "Modul"
  - **Judul Bagian**: Memperbarui "What This Module Covers" menjadi "What This Lab Covers" di semua 13 lab
  - **Deskripsi Konten**: Mengubah "This module provides..." menjadi "This lab provides..." di seluruh dokumentasi
  - **Tujuan Pembelajaran**: Memperbarui "By the end of this module..." menjadi "By the end of this lab..."
  - **Tautan Navigasi**: Mengonversi semua referensi "Module XX:" menjadi "Lab XX:" dalam referensi silang dan navigasi
  - **Pelacakan Penyelesaian**: Memperbarui "After completing this module..." menjadi "After completing this lab..."
  - **Referensi Teknis Tetap**: Mempertahankan referensi modul Python dalam berkas konfigurasi (misalnya `"module": "mcp_server.main"`)

#### Peningkatan Panduan Studi (study_guide.md)
- **Peta Kurikulum Visual**: Menambahkan bagian baru "11. Database Integration Labs" dengan visualisasi struktur lab yang komprehensif
- **Struktur Repository**: Memperbarui dari sepuluh menjadi sebelas bagian utama dengan deskripsi detail 11-MCPServerHandsOnLabs
- **Panduan Jalur Pembelajaran**: Memperbaiki instruksi navigasi untuk mencakup bagian 00-11
- **Cakupan Teknologi**: Menambahkan detil integrasi FastMCP, PostgreSQL, dan layanan Azure
- **Hasil Pembelajaran**: Menekankan pengembangan server siap produksi, pola integrasi database, dan keamanan enterprise

#### Peningkatan Struktur README Utama
- **Terminologi Berbasis Lab**: Memperbarui README.md utama di 11-MCPServerHandsOnLabs agar konsisten menggunakan struktur "Lab"
- **Organisasi Jalur Pembelajaran**: Progresi yang jelas dari konsep dasar melalui implementasi lanjutan hingga deployment produksi
- **Fokus Dunia Nyata**: Penekanan pada pembelajaran praktis dengan pola dan teknologi tingkat enterprise

### Peningkatan Kualitas & Konsistensi Dokumentasi
- **Penekanan Pembelajaran Praktik**: Memperkuat pendekatan berbasis lab sepanjang dokumentasi
- **Fokus Pola Enterprise**: Menyoroti implementasi siap produksi dan pertimbangan keamanan enterprise
- **Integrasi Teknologi**: Cakupan lengkap layanan Azure modern dan pola integrasi AI
- **Progresi Pembelajaran**: Jalur terstruktur dan jelas dari konsep dasar ke deployment produksi

## 26 September 2025

### Peningkatan Studi Kasus - Integrasi GitHub MCP Registry

#### Studi Kasus (09-CaseStudy/) - Fokus Pengembangan Ekosistem
- **README.md**: Perluasan besar dengan studi kasus lengkap GitHub MCP Registry
  - **Studi Kasus GitHub MCP Registry**: Studi kasus mendalam menelaah peluncuran MCP Registry GitHub pada September 2025
    - **Analisis Masalah**: Pemeriksaan rinci tantangan fragmentasi penemuan dan deployment server MCP
    - **Arsitektur Solusi**: Pendekatan registry terpusat GitHub dengan pemasangan VS Code sekali klik
    - **Dampak Bisnis**: Perbaikan terukur dalam onboarding dan produktivitas developer
    - **Nilai Strategis**: Fokus pada deployment agen modular dan interoperabilitas lintas alat
    - **Pengembangan Ekosistem**: Posisi sebagai platform dasar untuk integrasi agentic
  - **Struktur Studi Kasus Ditingkatkan**: Memperbarui semua tujuh studi kasus dengan format konsisten dan deskripsi lengkap
    - Azure AI Travel Agents: Penekanan orkestrasi multi-agen
    - Integrasi Azure DevOps: Fokus otomatisasi alur kerja
    - Pengambilan Dokumentasi Real-Time: Implementasi klien konsol Python
    - Generator Rencana Studi Interaktif: Aplikasi web percakapan Chainlit
    - Dokumentasi Dalam Editor: Integrasi VS Code dan GitHub Copilot
    - Azure API Management: Pola integrasi API enterprise
    - GitHub MCP Registry: Pengembangan ekosistem dan platform komunitas
  - **Kesimpulan Komprehensif**: Bagian kesimpulan diperbarui menyoroti tujuh studi kasus yang mencakup berbagai dimensi implementasi MCP
    - Integrasi Enterprise, Orkestrasi Multi-Agen, Produktivitas Developer
    - Pengembangan Ekosistem, Kategori Aplikasi Pendidikan
    - Wawasan ditingkatkan tentang pola arsitektur, strategi implementasi, dan praktik terbaik
    - Penekanan MCP sebagai protokol matang siap produksi

#### Pembaruan Panduan Studi (study_guide.md)
- **Peta Kurikulum Visual**: Memperbarui mindmap untuk memasukkan GitHub MCP Registry dalam bagian Studi Kasus
- **Deskripsi Studi Kasus**: Ditingkatkan dari deskripsi umum menjadi rincian tujuh studi kasus komprehensif
- **Struktur Repository**: Memperbarui bagian 10 untuk mencerminkan cakupan studi kasus lengkap dengan detail implementasi spesifik
- **Integrasi Changelog**: Menambahkan entri 26 September 2025 yang mendokumentasikan penambahan GitHub MCP Registry dan peningkatan studi kasus
- **Pembaruan Tanggal**: Memperbarui cap waktu footer untuk mencerminkan revisi terbaru (26 September 2025)

### Peningkatan Kualitas Dokumentasi
- **Peningkatan Konsistensi**: Memstandarkan format dan struktur studi kasus di semua tujuh contoh
- **Cakupan Komprehensif**: Studi kasus kini meliputi skenario enterprise, produktivitas developer, dan pengembangan ekosistem
- **Posisi Strategis**: Fokus yang diperkuat pada MCP sebagai platform dasar untuk deployment sistem agentic
- **Integrasi Sumber Daya**: Memperbarui sumber daya tambahan untuk memasukkan tautan GitHub MCP Registry

## 15 September 2025

### Perluasan Topik Lanjutan - Transport Kustom & Rekayasa Konteks

#### Transport Kustom MCP (05-AdvancedTopics/mcp-transport/) - Panduan Implementasi Lanjutan Baru
- **README.md**: Panduan implementasi lengkap untuk mekanisme transport MCP kustom
  - **Transport Azure Event Grid**: Implementasi transport event-driven serverless yang komprehensif
    - Contoh C#, TypeScript, dan Python dengan integrasi Azure Functions
    - Pola arsitektur event-driven untuk solusi MCP yang skalabel
    - Penerima webhook dan penanganan pesan berbasis push
  - **Transport Azure Event Hubs**: Implementasi transport streaming berkapasitas tinggi
    - Kapabilitas streaming waktu nyata untuk skenario latensi rendah
    - Strategi partisi dan manajemen checkpoint
    - Pengelompokan pesan dan optimasi kinerja
  - **Pola Integrasi Enterprise**: Contoh arsitektur siap produksi
    - Pemrosesan MCP terdistribusi di beberapa Azure Functions
    - Arsitektur transport hybrid menggabungkan beberapa jenis transport
    - Strategi daya tahan pesan, keandalan, dan penanganan kesalahan
  - **Keamanan & Pemantauan**: Integrasi Azure Key Vault dan pola observabilitas
    - Otentikasi managed identity dan akses prinsip hak minimum
    - Telemetri Application Insights dan pemantauan kinerja
    - Pemutus sirkuit dan pola toleransi kesalahan
  - **Kerangka Pengujian**: Strategi pengujian lengkap untuk transport kustom
    - Pengujian unit dengan test double dan mocking framework
    - Pengujian integrasi dengan Azure Test Containers
    - Pertimbangan pengujian performa dan beban

#### Rekayasa Konteks (05-AdvancedTopics/mcp-contextengineering/) - Disiplin AI yang Berkembang
- **README.md**: Eksplorasi mendalam tentang rekayasa konteks sebagai bidang yang berkembang
  - **Prinsip Inti**: Berbagi konteks lengkap, kesadaran pengambilan keputusan aksi, dan manajemen jendela konteks
  - **Keselarasan Protokol MCP**: Bagaimana desain MCP menangani tantangan rekayasa konteks
    - Batasan jendela konteks dan strategi pemuatan progresif
    - Penentuan relevansi dan pengambilan konteks dinamis
    - Penanganan konteks multimodal dan pertimbangan keamanan
  - **Pendekatan Implementasi**: Arsitektur single-threaded vs. multi-agen
    - Teknik pemecahan potongan konteks dan prioritisasi
    - Pemuatan konteks progresif dan strategi kompresi
    - Pendekatan konteks berlapis dan optimasi pengambilan
  - **Kerangka Pengukuran**: Metrik baru untuk evaluasi efektivitas konteks
    - Efisiensi input, kinerja, kualitas, dan pertimbangan pengalaman pengguna
    - Pendekatan eksperimental untuk optimasi konteks
    - Analisis kegagalan dan metodologi peningkatan

#### Pembaruan Navigasi Kurikulum (README.md)
- **Struktur Modul Ditingkatkan**: Memperbarui tabel kurikulum untuk memasukkan topik lanjutan baru
  - Menambahkan Rekayasa Konteks (5.14) dan Transport Kustom (5.15)
  - Format konsisten dan tautan navigasi di semua modul
  - Deskripsi diperbarui untuk mencerminkan cakupan konten saat ini

### Peningkatan Struktur Direktori
- **Standarisasi Penamaan**: Mengubah nama "mcp transport" menjadi "mcp-transport" agar konsisten dengan folder topik lanjutan lainnya
- **Organisasi Konten**: Semua folder 05-AdvancedTopics kini mengikuti pola penamaan konsisten (mcp-[topik])

### Peningkatan Kualitas Dokumentasi
- **Keselarasan Spesifikasi MCP**: Semua konten baru merujuk Spesifikasi MCP 2025-06-18 saat ini
- **Contoh Multi-Bahasa**: Contoh kode lengkap dalam C#, TypeScript, dan Python
- **Fokus Enterprise**: Pola siap produksi dan integrasi cloud Azure sepanjang dokumentasi
- **Dokumentasi Visual**: Diagram Mermaid untuk visualisasi arsitektur dan alur

## 18 Agustus 2025

### Pembaruan Dokumentasi Komprehensif - Standar MCP 2025-06-18

#### Praktik Keamanan Terbaik MCP (02-Security/) - Modernisasi Lengkap
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Pengubahan lengkap yang disesuaikan dengan Spesifikasi MCP 2025-06-18  
  - **Persyaratan Wajib**: Ditambahkan persyaratan HARUS/TIDAK BOLEH eksplisit dari spesifikasi resmi dengan indikator visual yang jelas  
  - **12 Praktik Keamanan Inti**: Disusun ulang dari daftar 15 item menjadi domain keamanan komprehensif  
    - Keamanan Token & Otentikasi dengan integrasi penyedia identitas eksternal  
    - Manajemen Sesi & Keamanan Transportasi dengan persyaratan kriptografi  
    - Perlindungan Ancaman Khusus AI dengan integrasi Microsoft Prompt Shields  
    - Kontrol Akses & Izin dengan prinsip hak istimewa paling sedikit  
    - Keamanan & Pemantauan Konten dengan integrasi Azure Content Safety  
    - Keamanan Rantai Pasokan dengan verifikasi komponen komprehensif  
    - Keamanan OAuth & Pencegahan Confused Deputy dengan implementasi PKCE  
    - Respons Insiden & Pemulihan dengan kapabilitas otomatis  
    - Kepatuhan & Tata Kelola dengan keselarasan regulasi  
    - Kontrol Keamanan Lanjutan dengan arsitektur zero trust  
    - Integrasi Ekosistem Keamanan Microsoft dengan solusi komprehensif  
    - Evolusi Keamanan Berkelanjutan dengan praktik adaptif  
  - **Solusi Keamanan Microsoft**: Panduan integrasi ditingkatkan untuk Prompt Shields, Azure Content Safety, Entra ID, dan GitHub Advanced Security  
  - **Sumber Implementasi**: Tautan sumber daya komprehensif dikategorikan oleh Dokumentasi Resmi MCP, Solusi Keamanan Microsoft, Standar Keamanan, dan Panduan Implementasi  

#### Kontrol Keamanan Lanjutan (02-Security/) - Implementasi Perusahaan  
- **MCP-SECURITY-CONTROLS-2025.md**: Revisi lengkap dengan kerangka keamanan tingkat perusahaan  
  - **9 Domain Keamanan Komprehensif**: Diperluas dari kontrol dasar menjadi kerangka kerja perusahaan terperinci  
    - Otentikasi & Otorisasi Lanjutan dengan integrasi Microsoft Entra ID  
    - Keamanan Token & Kontrol Anti-Passthrough dengan validasi komprehensif  
    - Kontrol Keamanan Sesi dengan pencegahan pembajakan  
    - Kontrol Keamanan Khusus AI dengan pencegahan injeksi prompt dan keracunan alat  
    - Pencegahan Serangan Confused Deputy dengan keamanan proxy OAuth  
    - Keamanan Eksekusi Alat dengan sandboxing dan isolasi  
    - Kontrol Keamanan Rantai Pasokan dengan verifikasi dependensi  
    - Kontrol Pemantauan & Deteksi dengan integrasi SIEM  
    - Respons Insiden & Pemulihan dengan kapabilitas otomatis  
  - **Contoh Implementasi**: Ditambahkan blok konfigurasi YAML dan contoh kode terperinci  
  - **Integrasi Solusi Microsoft**: Cakupan komprehensif layanan keamanan Azure, GitHub Advanced Security, dan manajemen identitas perusahaan  

#### Topik Keamanan Lanjutan (05-AdvancedTopics/mcp-security/) - Implementasi Siap Produksi  
- **README.md**: Penulisan ulang lengkap untuk implementasi keamanan perusahaan  
  - **Keselarasan Spesifikasi Saat Ini**: Diperbarui ke Spesifikasi MCP 2025-06-18 dengan persyaratan keamanan wajib  
  - **Otentikasi yang Ditingkatkan**: Integrasi Microsoft Entra ID dengan contoh lengkap .NET dan Java Spring Security  
  - **Integrasi Keamanan AI**: Implementasi Microsoft Prompt Shields dan Azure Content Safety dengan contoh Python terperinci  
  - **Mitigasi Ancaman Lanjutan**: Contoh implementasi komprehensif untuk  
    - Pencegahan Serangan Confused Deputy dengan PKCE dan validasi persetujuan pengguna  
    - Pencegahan Token Passthrough dengan validasi audiens dan pengelolaan token aman  
    - Pencegahan Pembajakan Sesi dengan pengikatan kriptografis dan analisis perilaku  
  - **Integrasi Keamanan Perusahaan**: Pemantauan Azure Application Insights, pipeline deteksi ancaman, dan keamanan rantai pasokan  
  - **Daftar Periksa Implementasi**: Kontrol keamanan wajib vs. yang direkomendasikan dengan manfaat ekosistem keamanan Microsoft yang jelas  

### Kualitas Dokumentasi & Keselarasan Standar  
- **Referensi Spesifikasi**: Memperbarui semua referensi ke Spesifikasi MCP terbaru 2025-06-18  
- **Ekosistem Keamanan Microsoft**: Panduan integrasi ditingkatkan di seluruh dokumentasi keamanan  
- **Implementasi Praktis**: Ditambahkan contoh kode terperinci dalam .NET, Java, dan Python dengan pola perusahaan  
- **Organisasi Sumber Daya**: Kategorisasi komprehensif dokumentasi resmi, standar keamanan, dan panduan implementasi  
- **Indikator Visual**: Penandaan jelas persyaratan wajib vs. praktik yang disarankan  

#### Konsep Inti (01-CoreConcepts/) - Modernisasi Lengkap  
- **Pembaharuan Versi Protokol**: Diperbarui untuk merujuk Spesifikasi MCP saat ini 2025-06-18 dengan format penanggalan (YYYY-MM-DD)  
- **Penyempurnaan Arsitektur**: Deskripsi ditingkatkan tentang Host, Klien, dan Server untuk mencerminkan pola arsitektur MCP terkini  
  - Host kini didefinisikan jelas sebagai aplikasi AI yang mengoordinasikan beberapa koneksi klien MCP  
  - Klien dijelaskan sebagai penghubung protokol yang mempertahankan hubungan satu-ke-satu dengan server  
  - Server diperluas dengan skenario penyebaran lokal dan jarak jauh  
- **Restrukturisasi Primitif**: Revisi lengkap primitif server dan klien  
  - Primitif Server: Resources (sumber data), Prompts (template), Tools (fungsi eksekusi) dengan penjelasan dan contoh terperinci  
  - Primitif Klien: Sampling (penyelesaian LLM), Elicitation (input pengguna), Logging (debugging/pemantauan)  
  - Diperbarui dengan pola metode discovery (`*/list`), retrieval (`*/get`), dan execution (`*/call`) saat ini  
- **Arsitektur Protokol**: Memperkenalkan model arsitektur dua lapisan  
  - Lapisan Data: Fondasi JSON-RPC 2.0 dengan manajemen siklus hidup dan primitif  
  - Lapisan Transportasi: STDIO (lokal) dan HTTP Streamable dengan SSE (remote)  
- **Kerangka Keamanan**: Prinsip keamanan komprehensif termasuk persetujuan eksplisit pengguna, perlindungan privasi data, keamanan eksekusi alat, dan keamanan lapisan transportasi  
- **Pola Komunikasi**: Pembaruan pesan protokol menampilkan aliran inisialisasi, penemuan, eksekusi, dan notifikasi  
- **Contoh Kode**: Penyegaran contoh multi-bahasa (.NET, Java, Python, JavaScript) sesuai pola SDK MCP saat ini  

#### Keamanan (02-Security/) - Revisi Keamanan Komprehensif  
- **Keselarasan Standar**: Penyelarasan penuh dengan persyaratan keamanan Spesifikasi MCP 2025-06-18  
- **Evolusi Otentikasi**: Dokumentasi evolusi dari server OAuth kustom ke delegasi penyedia identitas eksternal (Microsoft Entra ID)  
- **Analisis Ancaman Khusus AI**: Cakupan ditingkatkan terkait vektor serangan AI modern  
  - Skenario serangan injeksi prompt terperinci dengan contoh dunia nyata  
  - Mekanisme keracunan alat dan pola serangan "rug pull"  
  - Keracunan jendela konteks dan serangan kebingungan model  
- **Solusi Keamanan AI Microsoft**: Cakupan komprehensif ekosistem keamanan Microsoft  
  - AI Prompt Shields dengan deteksi lanjutan, spotlighting, dan teknik delimiter  
  - Pola integrasi Azure Content Safety  
  - GitHub Advanced Security untuk perlindungan rantai pasokan  
- **Mitigasi Ancaman Lanjutan**: Kontrol keamanan rinci untuk  
  - Pembajakan sesi dengan skenario serangan khusus MCP dan persyaratan ID sesi kriptografi  
  - Masalah confused deputy dalam skenario proxy MCP dengan persyaratan persetujuan eksplisit  
  - Kerentanan token passthrough dengan kontrol validasi wajib  
- **Keamanan Rantai Pasokan**: Perluasan cakupan rantai pasokan AI termasuk model dasar, layanan embeddings, penyedia konteks, dan API pihak ketiga  
- **Keamanan Fondasi**: Integrasi ditingkatkan dengan pola keamanan perusahaan termasuk arsitektur zero trust dan ekosistem keamanan Microsoft  
- **Organisasi Sumber Daya**: Kategorisasi tautan sumber daya lengkap berdasarkan tipe (Dokumen Resmi, Standar, Riset, Solusi Microsoft, Panduan Implementasi)  

### Peningkatan Kualitas Dokumentasi  
- **Tujuan Pembelajaran Terstruktur**: Peningkatan tujuan pembelajaran dengan hasil spesifik dan dapat ditindaklanjuti  
- **Referensi Silang**: Penambahan tautan antar topik keamanan dan konsep inti terkait  
- **Informasi Terbaru**: Memperbarui semua referensi tanggal dan tautan spesifikasi ke standar terkini  
- **Panduan Implementasi**: Tambahan pedoman implementasi spesifik dan dapat ditindaklanjuti di seluruh bagian  

## 16 Juli 2025  

### Perbaikan README dan Navigasi  
- Mendesain ulang navigasi kurikulum di README.md secara menyeluruh  
- Mengganti tag `<details>` dengan format tabel yang lebih mudah diakses  
- Membuat opsi tata letak alternatif di folder baru "alternative_layouts"  
- Menambahkan contoh navigasi berbasis kartu, gaya tab, dan gaya akordeon  
- Memperbarui bagian struktur repositori untuk memasukkan semua file terbaru  
- Meningkatkan bagian "Cara Menggunakan Kurikulum Ini" dengan rekomendasi yang jelas  
- Memperbarui tautan spesifikasi MCP agar mengarah ke URL yang tepat  
- Menambahkan bagian Context Engineering (5.14) ke struktur kurikulum  

### Pembaruan Panduan Studi  
- Merevisi total panduan studi untuk menyesuaikan dengan struktur repositori saat ini  
- Menambahkan bagian baru untuk MCP Clients dan Tools, serta MCP Servers populer  
- Memperbarui Peta Kurikulum Visual agar mencerminkan semua topik dengan akurat  
- Memperbaiki deskripsi Topik Lanjutan untuk mencakup semua area spesialisasi  
- Memperbarui bagian Studi Kasus untuk mencerminkan contoh nyata  
- Menambahkan changelog komprehensif ini  

### Kontribusi Komunitas (06-CommunityContributions/)  
- Menambahkan informasi rinci tentang server MCP untuk generasi gambar  
- Menambahkan bagian komprehensif tentang penggunaan Claude di VSCode  
- Menambahkan instruksi pemasangan dan penggunaan klien terminal Cline  
- Memperbarui bagian klien MCP untuk memasukkan semua opsi klien populer  
- Meningkatkan contoh kontribusi dengan sampel kode yang lebih akurat  

### Topik Lanjutan (05-AdvancedTopics/)  
- Mengorganisasi semua folder topik khusus dengan penamaan konsisten  
- Menambahkan materi dan contoh rekayasa konteks  
- Menambahkan dokumentasi integrasi agen Foundry  
- Memperbaiki dokumentasi integrasi keamanan Entra ID  

## 11 Juni 2025  

### Pembuatan Awal  
- Merilis versi pertama kurikulum MCP untuk Pemula  
- Membuat struktur dasar untuk semua 10 bagian utama  
- Mengimplementasikan Peta Kurikulum Visual untuk navigasi  
- Menambahkan proyek sampel awal dalam berbagai bahasa pemrograman  

### Memulai (03-GettingStarted/)  
- Membuat contoh implementasi server pertama  
- Menambahkan panduan pengembangan klien  
- Menyertakan instruksi integrasi klien LLM  
- Menambahkan dokumentasi integrasi VS Code  
- Mengimplementasikan contoh Server-Sent Events (SSE) server  

### Konsep Inti (01-CoreConcepts/)  
- Menambahkan penjelasan rinci mengenai arsitektur klien-server  
- Membuat dokumentasi komponen utama protokol  
- Mendokumentasikan pola pesan dalam MCP  

## 23 Mei 2025  

### Struktur Repositori  
- Menginisialisasi repositori dengan struktur folder dasar  
- Membuat file README untuk setiap bagian utama  
- Menyiapkan infrastruktur penerjemahan  
- Menambahkan aset gambar dan diagram  

### Dokumentasi  
- Membuat README.md awal dengan gambaran kurikulum  
- Menambahkan CODE_OF_CONDUCT.md dan SECURITY.md  
- Menyiapkan SUPPORT.md dengan panduan bantuan  
- Membuat struktur panduan studi awal  

## 15 April 2025  

### Perencanaan dan Kerangka Kerja  
- Perencanaan awal untuk kurikulum MCP untuk Pemula  
- Mendefinisikan tujuan pembelajaran dan audiens sasaran  
- Menggarisbawahi struktur kurikulum 10 bagian  
- Mengembangkan kerangka konseptual untuk contoh dan studi kasus  
- Membuat contoh prototipe awal untuk konsep kunci

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menerjemahkan secara profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->