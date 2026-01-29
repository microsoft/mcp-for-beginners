# Changelog: Kurikulum MCP untuk Pemula

Dokumen ini berfungsi sebagai catatan semua perubahan signifikan yang dibuat pada kurikulum Model Context Protocol (MCP) untuk Pemula. Perubahan didokumentasikan dalam urutan kronologis terbalik (perubahan terbaru terlebih dahulu).

## 18 Desember 2025

### Pembaruan Dokumentasi Keamanan - Spesifikasi MCP 2025-11-25

#### Praktik Terbaik Keamanan MCP (02-Security/mcp-best-practices.md) - Pembaruan Versi Spesifikasi
- **Pembaruan Versi Protokol**: Diperbarui untuk merujuk Spesifikasi MCP terbaru 2025-11-25 (dirilis 25 November 2025)
  - Memperbarui semua referensi versi spesifikasi dari 2025-06-18 ke 2025-11-25
  - Memperbarui referensi tanggal dokumen dari 18 Agustus 2025 ke 18 Desember 2025
  - Memverifikasi semua URL spesifikasi mengarah ke dokumentasi terkini
- **Validasi Konten**: Validasi menyeluruh praktik terbaik keamanan terhadap standar terbaru
  - **Solusi Keamanan Microsoft**: Memverifikasi terminologi dan tautan terkini untuk Prompt Shields (sebelumnya "deteksi risiko Jailbreak"), Azure Content Safety, Microsoft Entra ID, dan Azure Key Vault
  - **Keamanan OAuth 2.1**: Mengonfirmasi kesesuaian dengan praktik terbaik keamanan OAuth terbaru
  - **Standar OWASP**: Memvalidasi referensi OWASP Top 10 untuk LLM tetap terkini
  - **Layanan Azure**: Memverifikasi semua tautan dokumentasi Microsoft Azure dan praktik terbaik
- **Kesesuaian Standar**: Semua standar keamanan yang direferensikan dikonfirmasi terkini
  - Kerangka Manajemen Risiko AI NIST
  - ISO 27001:2022
  - Praktik Terbaik Keamanan OAuth 2.1
  - Kerangka keamanan dan kepatuhan Azure
- **Sumber Daya Implementasi**: Memverifikasi semua tautan panduan implementasi dan sumber daya
  - Pola otentikasi Azure API Management
  - Panduan integrasi Microsoft Entra ID
  - Manajemen rahasia Azure Key Vault
  - Pipeline dan solusi pemantauan DevSecOps

### Jaminan Kualitas Dokumentasi
- **Kepatuhan Spesifikasi**: Memastikan semua persyaratan keamanan MCP wajib (MUST/MUST NOT) sesuai dengan spesifikasi terbaru
- **Keterkinian Sumber Daya**: Memverifikasi semua tautan eksternal ke dokumentasi Microsoft, standar keamanan, dan panduan implementasi
- **Cakupan Praktik Terbaik**: Mengonfirmasi cakupan komprehensif otentikasi, otorisasi, ancaman khusus AI, keamanan rantai pasokan, dan pola perusahaan

## 6 Oktober 2025

### Perluasan Bagian Memulai – Penggunaan Server Lanjutan & Otentikasi Sederhana

#### Penggunaan Server Lanjutan (03-GettingStarted/10-advanced)
- **Bab Baru Ditambahkan**: Memperkenalkan panduan komprehensif penggunaan server MCP lanjutan, mencakup arsitektur server reguler dan tingkat rendah.
  - **Server Reguler vs. Tingkat Rendah**: Perbandingan rinci dan contoh kode dalam Python dan TypeScript untuk kedua pendekatan.
  - **Desain Berbasis Handler**: Penjelasan manajemen alat/sumber daya/prompt berbasis handler untuk implementasi server yang skalabel dan fleksibel.
  - **Pola Praktis**: Skenario dunia nyata di mana pola server tingkat rendah bermanfaat untuk fitur dan arsitektur lanjutan.

#### Otentikasi Sederhana (03-GettingStarted/11-simple-auth)
- **Bab Baru Ditambahkan**: Panduan langkah demi langkah untuk mengimplementasikan otentikasi sederhana di server MCP.
  - **Konsep Auth**: Penjelasan jelas tentang otentikasi vs. otorisasi, dan penanganan kredensial.
  - **Implementasi Auth Dasar**: Pola otentikasi berbasis middleware dalam Python (Starlette) dan TypeScript (Express), dengan contoh kode.
  - **Progresi ke Keamanan Lanjutan**: Panduan memulai dengan otentikasi sederhana dan melanjutkan ke OAuth 2.1 dan RBAC, dengan referensi ke modul keamanan lanjutan.

Penambahan ini menyediakan panduan praktis dan langsung untuk membangun implementasi server MCP yang lebih kuat, aman, dan fleksibel, menjembatani konsep dasar dengan pola produksi lanjutan.

## 29 September 2025

### Laboratorium Integrasi Database Server MCP - Jalur Pembelajaran Praktis Komprehensif

#### 11-MCPServerHandsOnLabs - Kurikulum Lengkap Integrasi Database Baru
- **Jalur Pembelajaran 13-Lab Lengkap**: Menambahkan kurikulum praktis komprehensif untuk membangun server MCP siap produksi dengan integrasi database PostgreSQL
  - **Implementasi Dunia Nyata**: Kasus penggunaan analitik Zava Retail yang menunjukkan pola tingkat perusahaan
  - **Progresi Pembelajaran Terstruktur**:
    - **Lab 00-03: Dasar** - Pengenalan, Arsitektur Inti, Keamanan & Multi-Tenancy, Pengaturan Lingkungan
    - **Lab 04-06: Membangun Server MCP** - Desain & Skema Database, Implementasi Server MCP, Pengembangan Alat  
    - **Lab 07-09: Fitur Lanjutan** - Integrasi Pencarian Semantik, Pengujian & Debugging, Integrasi VS Code
    - **Lab 10-12: Produksi & Praktik Terbaik** - Strategi Penyebaran, Pemantauan & Observabilitas, Praktik Terbaik & Optimasi
  - **Teknologi Perusahaan**: Kerangka FastMCP, PostgreSQL dengan pgvector, embedding Azure OpenAI, Azure Container Apps, Application Insights
  - **Fitur Lanjutan**: Keamanan Tingkat Baris (RLS), pencarian semantik, akses data multi-tenant, embedding vektor, pemantauan waktu nyata

#### Standarisasi Terminologi - Konversi Modul ke Lab
- **Pembaruan Dokumentasi Komprehensif**: Memperbarui secara sistematis semua file README di 11-MCPServerHandsOnLabs untuk menggunakan terminologi "Lab" menggantikan "Module"
  - **Header Bagian**: Memperbarui "What This Module Covers" menjadi "What This Lab Covers" di semua 13 lab
  - **Deskripsi Konten**: Mengubah "This module provides..." menjadi "This lab provides..." di seluruh dokumentasi
  - **Tujuan Pembelajaran**: Memperbarui "By the end of this module..." menjadi "By the end of this lab..."
  - **Tautan Navigasi**: Mengonversi semua referensi "Module XX:" menjadi "Lab XX:" dalam referensi silang dan navigasi
  - **Pelacakan Penyelesaian**: Memperbarui "After completing this module..." menjadi "After completing this lab..."
  - **Referensi Teknis Terjaga**: Mempertahankan referensi modul Python dalam file konfigurasi (misal, `"module": "mcp_server.main"`)

#### Peningkatan Panduan Studi (study_guide.md)
- **Peta Kurikulum Visual**: Menambahkan bagian baru "11. Database Integration Labs" dengan visualisasi struktur lab komprehensif
- **Struktur Repositori**: Memperbarui dari sepuluh menjadi sebelas bagian utama dengan deskripsi detail 11-MCPServerHandsOnLabs
- **Panduan Jalur Pembelajaran**: Meningkatkan instruksi navigasi untuk mencakup bagian 00-11
- **Cakupan Teknologi**: Menambahkan detail integrasi FastMCP, PostgreSQL, layanan Azure
- **Hasil Pembelajaran**: Menekankan pengembangan server siap produksi, pola integrasi database, dan keamanan perusahaan

#### Peningkatan Struktur README Utama
- **Terminologi Berbasis Lab**: Memperbarui README.md utama di 11-MCPServerHandsOnLabs untuk konsisten menggunakan struktur "Lab"
- **Organisasi Jalur Pembelajaran**: Progresi jelas dari konsep dasar hingga implementasi lanjutan dan penyebaran produksi
- **Fokus Dunia Nyata**: Penekanan pada pembelajaran praktis dengan pola dan teknologi tingkat perusahaan

### Peningkatan Kualitas & Konsistensi Dokumentasi
- **Penekanan Pembelajaran Praktis**: Memperkuat pendekatan berbasis lab di seluruh dokumentasi
- **Fokus Pola Perusahaan**: Menyoroti implementasi siap produksi dan pertimbangan keamanan perusahaan
- **Integrasi Teknologi**: Cakupan komprehensif layanan Azure modern dan pola integrasi AI
- **Progresi Pembelajaran**: Jalur terstruktur jelas dari konsep dasar hingga penyebaran produksi

## 26 September 2025

### Peningkatan Studi Kasus - Integrasi GitHub MCP Registry

#### Studi Kasus (09-CaseStudy/) - Fokus Pengembangan Ekosistem
- **README.md**: Perluasan besar dengan studi kasus komprehensif GitHub MCP Registry
  - **Studi Kasus GitHub MCP Registry**: Studi kasus komprehensif baru yang mengkaji peluncuran GitHub MCP Registry pada September 2025
    - **Analisis Masalah**: Pemeriksaan rinci tantangan penemuan dan penyebaran server MCP yang terfragmentasi
    - **Arsitektur Solusi**: Pendekatan registry terpusat GitHub dengan instalasi VS Code satu klik
    - **Dampak Bisnis**: Peningkatan terukur dalam onboarding dan produktivitas pengembang
    - **Nilai Strategis**: Fokus pada penyebaran agen modular dan interoperabilitas lintas alat
    - **Pengembangan Ekosistem**: Posisi sebagai platform dasar untuk integrasi agenik
  - **Struktur Studi Kasus Ditingkatkan**: Memperbarui semua tujuh studi kasus dengan format konsisten dan deskripsi komprehensif
    - Agen Perjalanan Azure AI: Penekanan orkestrasi multi-agen
    - Integrasi Azure DevOps: Fokus otomatisasi alur kerja
    - Pengambilan Dokumentasi Waktu Nyata: Implementasi klien konsol Python
    - Generator Rencana Studi Interaktif: Aplikasi web percakapan Chainlit
    - Dokumentasi Dalam Editor: Integrasi VS Code dan GitHub Copilot
    - Azure API Management: Pola integrasi API perusahaan
    - GitHub MCP Registry: Pengembangan ekosistem dan platform komunitas
  - **Kesimpulan Komprehensif**: Bagian kesimpulan ditulis ulang menyoroti tujuh studi kasus yang mencakup berbagai dimensi implementasi MCP
    - Integrasi Perusahaan, Orkestrasi Multi-Agen, Produktivitas Pengembang
    - Pengembangan Ekosistem, Kategori Aplikasi Pendidikan
    - Wawasan diperluas tentang pola arsitektur, strategi implementasi, dan praktik terbaik
    - Penekanan pada MCP sebagai protokol matang dan siap produksi

#### Pembaruan Panduan Studi (study_guide.md)
- **Peta Kurikulum Visual**: Memperbarui mindmap untuk memasukkan GitHub MCP Registry di bagian Studi Kasus
- **Deskripsi Studi Kasus**: Ditingkatkan dari deskripsi umum menjadi rincian tujuh studi kasus komprehensif
- **Struktur Repositori**: Memperbarui bagian 10 untuk mencerminkan cakupan studi kasus komprehensif dengan detail implementasi spesifik
- **Integrasi Changelog**: Menambahkan entri 26 September 2025 yang mendokumentasikan penambahan GitHub MCP Registry dan peningkatan studi kasus
- **Pembaruan Tanggal**: Memperbarui cap waktu footer untuk mencerminkan revisi terbaru (26 September 2025)

### Peningkatan Kualitas Dokumentasi
- **Peningkatan Konsistensi**: Standarisasi format dan struktur studi kasus di semua tujuh contoh
- **Cakupan Komprehensif**: Studi kasus kini mencakup skenario perusahaan, produktivitas pengembang, dan pengembangan ekosistem
- **Posisi Strategis**: Fokus diperkuat pada MCP sebagai platform dasar untuk penyebaran sistem agenik
- **Integrasi Sumber Daya**: Memperbarui sumber daya tambahan untuk menyertakan tautan GitHub MCP Registry

## 15 September 2025

### Perluasan Topik Lanjutan - Transportasi Kustom & Rekayasa Konteks

#### Transportasi Kustom MCP (05-AdvancedTopics/mcp-transport/) - Panduan Implementasi Lanjutan Baru
- **README.md**: Panduan implementasi lengkap untuk mekanisme transportasi MCP kustom
  - **Transportasi Azure Event Grid**: Implementasi transportasi event-driven serverless komprehensif
    - Contoh C#, TypeScript, dan Python dengan integrasi Azure Functions
    - Pola arsitektur event-driven untuk solusi MCP yang skalabel
    - Penerima webhook dan penanganan pesan berbasis push
  - **Transportasi Azure Event Hubs**: Implementasi transportasi streaming throughput tinggi
    - Kemampuan streaming waktu nyata untuk skenario latensi rendah
    - Strategi partisi dan manajemen checkpoint
    - Pengelompokan pesan dan optimasi performa
  - **Pola Integrasi Perusahaan**: Contoh arsitektur siap produksi
    - Pemrosesan MCP terdistribusi di beberapa Azure Functions
    - Arsitektur transportasi hibrida yang menggabungkan beberapa jenis transportasi
    - Strategi daya tahan pesan, keandalan, dan penanganan kesalahan
  - **Keamanan & Pemantauan**: Integrasi Azure Key Vault dan pola observabilitas
    - Otentikasi identitas terkelola dan akses prinsip hak minimum
    - Telemetri Application Insights dan pemantauan performa
    - Circuit breaker dan pola toleransi kesalahan
  - **Kerangka Pengujian**: Strategi pengujian komprehensif untuk transportasi kustom
    - Pengujian unit dengan test double dan framework mocking
    - Pengujian integrasi dengan Azure Test Containers
    - Pertimbangan pengujian performa dan beban

#### Rekayasa Konteks (05-AdvancedTopics/mcp-contextengineering/) - Disiplin AI yang Berkembang
- **README.md**: Eksplorasi komprehensif rekayasa konteks sebagai bidang yang sedang berkembang
  - **Prinsip Inti**: Berbagi konteks lengkap, kesadaran pengambilan keputusan aksi, dan manajemen jendela konteks
  - **Kesesuaian Protokol MCP**: Bagaimana desain MCP mengatasi tantangan rekayasa konteks
    - Batasan jendela konteks dan strategi pemuatan progresif
    - Penentuan relevansi dan pengambilan konteks dinamis
    - Penanganan konteks multi-modal dan pertimbangan keamanan
  - **Pendekatan Implementasi**: Arsitektur single-threaded vs. multi-agen
    - Teknik pemecahan dan prioritisasi konteks
    - Pemuatan konteks progresif dan strategi kompresi
    - Pendekatan konteks berlapis dan optimasi pengambilan
  - **Kerangka Pengukuran**: Metrik yang berkembang untuk evaluasi efektivitas konteks
    - Efisiensi input, performa, kualitas, dan pertimbangan pengalaman pengguna
    - Pendekatan eksperimental untuk optimasi konteks
    - Analisis kegagalan dan metodologi perbaikan

#### Pembaruan Navigasi Kurikulum (README.md)
- **Struktur Modul Ditingkatkan**: Memperbarui tabel kurikulum untuk memasukkan topik lanjutan baru
  - Menambahkan Rekayasa Konteks (5.14) dan Transportasi Kustom (5.15)
  - Format dan tautan navigasi konsisten di semua modul
  - Memperbarui deskripsi untuk mencerminkan cakupan konten saat ini

### Peningkatan Struktur Direktori
- **Standarisasi Penamaan**: Mengganti nama "mcp transport" menjadi "mcp-transport" agar konsisten dengan folder topik lanjutan lainnya
- **Organisasi Konten**: Semua folder 05-AdvancedTopics kini mengikuti pola penamaan konsisten (mcp-[topic])

### Peningkatan Kualitas Dokumentasi
- **Kesesuaian Spesifikasi MCP**: Semua konten baru merujuk Spesifikasi MCP 2025-06-18 terkini
- **Contoh Multi-Bahasa**: Contoh kode komprehensif dalam C#, TypeScript, dan Python
- **Fokus Perusahaan**: Pola siap produksi dan integrasi cloud Azure secara menyeluruh
- **Dokumentasi Visual**: Diagram Mermaid untuk visualisasi arsitektur dan alur

## 18 Agustus 2025

### Pembaruan Komprehensif Dokumentasi - Standar MCP 2025-06-18

#### Praktik Terbaik Keamanan MCP (02-Security/) - Modernisasi Lengkap
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Penulisan ulang lengkap sesuai Spesifikasi MCP 2025-06-18
  - **Persyaratan Wajib**: Menambahkan persyaratan MUST/MUST NOT eksplisit dari spesifikasi resmi dengan indikator visual yang jelas
  - **12 Praktik Keamanan Inti**: Direstrukturisasi dari daftar 15 item menjadi domain keamanan yang komprehensif
    - Keamanan Token & Autentikasi dengan integrasi penyedia identitas eksternal
    - Manajemen Sesi & Keamanan Transportasi dengan persyaratan kriptografi
    - Perlindungan Ancaman Khusus AI dengan integrasi Microsoft Prompt Shields
    - Kontrol Akses & Izin dengan prinsip hak istimewa paling sedikit
    - Keamanan Konten & Pemantauan dengan integrasi Azure Content Safety
    - Keamanan Rantai Pasokan dengan verifikasi komponen yang komprehensif
    - Keamanan OAuth & Pencegahan Confused Deputy dengan implementasi PKCE
    - Respons & Pemulihan Insiden dengan kemampuan otomatis
    - Kepatuhan & Tata Kelola dengan keselarasan regulasi
    - Kontrol Keamanan Lanjutan dengan arsitektur zero trust
    - Integrasi Ekosistem Keamanan Microsoft dengan solusi komprehensif
    - Evolusi Keamanan Berkelanjutan dengan praktik adaptif
  - **Solusi Keamanan Microsoft**: Panduan integrasi yang ditingkatkan untuk Prompt Shields, Azure Content Safety, Entra ID, dan GitHub Advanced Security
  - **Sumber Daya Implementasi**: Mengkategorikan tautan sumber daya komprehensif berdasarkan Dokumentasi MCP Resmi, Solusi Keamanan Microsoft, Standar Keamanan, dan Panduan Implementasi

#### Kontrol Keamanan Lanjutan (02-Security/) - Implementasi Perusahaan
- **MCP-SECURITY-CONTROLS-2025.md**: Perombakan lengkap dengan kerangka kerja keamanan tingkat perusahaan
  - **9 Domain Keamanan Komprehensif**: Diperluas dari kontrol dasar menjadi kerangka kerja perusahaan yang terperinci
    - Autentikasi & Otorisasi Lanjutan dengan integrasi Microsoft Entra ID
    - Keamanan Token & Kontrol Anti-Passthrough dengan validasi komprehensif
    - Kontrol Keamanan Sesi dengan pencegahan pembajakan
    - Kontrol Keamanan Khusus AI dengan pencegahan injeksi prompt dan keracunan alat
    - Pencegahan Serangan Confused Deputy dengan keamanan proxy OAuth
    - Keamanan Eksekusi Alat dengan sandboxing dan isolasi
    - Kontrol Keamanan Rantai Pasokan dengan verifikasi ketergantungan
    - Kontrol Pemantauan & Deteksi dengan integrasi SIEM
    - Respons & Pemulihan Insiden dengan kemampuan otomatis
  - **Contoh Implementasi**: Menambahkan blok konfigurasi YAML terperinci dan contoh kode
  - **Integrasi Solusi Microsoft**: Cakupan komprehensif layanan keamanan Azure, GitHub Advanced Security, dan manajemen identitas perusahaan

#### Topik Keamanan Lanjutan (05-AdvancedTopics/mcp-security/) - Implementasi Siap Produksi
- **README.md**: Penulisan ulang lengkap untuk implementasi keamanan perusahaan
  - **Keselarasan Spesifikasi Saat Ini**: Diperbarui ke Spesifikasi MCP 2025-06-18 dengan persyaratan keamanan wajib
  - **Autentikasi yang Ditingkatkan**: Integrasi Microsoft Entra ID dengan contoh lengkap .NET dan Java Spring Security
  - **Integrasi Keamanan AI**: Implementasi Microsoft Prompt Shields dan Azure Content Safety dengan contoh Python terperinci
  - **Mitigasi Ancaman Lanjutan**: Contoh implementasi komprehensif untuk
    - Pencegahan Serangan Confused Deputy dengan PKCE dan validasi persetujuan pengguna
    - Pencegahan Token Passthrough dengan validasi audiens dan manajemen token yang aman
    - Pencegahan Pembajakan Sesi dengan pengikatan kriptografi dan analisis perilaku
  - **Integrasi Keamanan Perusahaan**: Pemantauan Azure Application Insights, pipeline deteksi ancaman, dan keamanan rantai pasokan
  - **Daftar Periksa Implementasi**: Kontrol keamanan wajib vs. yang direkomendasikan dengan manfaat ekosistem keamanan Microsoft

### Kualitas Dokumentasi & Keselarasan Standar
- **Referensi Spesifikasi**: Memperbarui semua referensi ke Spesifikasi MCP 2025-06-18 saat ini
- **Ekosistem Keamanan Microsoft**: Panduan integrasi yang ditingkatkan di seluruh dokumentasi keamanan
- **Implementasi Praktis**: Menambahkan contoh kode terperinci dalam .NET, Java, dan Python dengan pola perusahaan
- **Organisasi Sumber Daya**: Kategorisasi komprehensif dokumentasi resmi, standar keamanan, dan panduan implementasi
- **Indikator Visual**: Penandaan jelas persyaratan wajib vs. praktik yang direkomendasikan


#### Konsep Inti (01-CoreConcepts/) - Modernisasi Lengkap
- **Pembaruan Versi Protokol**: Diperbarui untuk merujuk Spesifikasi MCP 2025-06-18 dengan versi berbasis tanggal (format YYYY-MM-DD)
- **Penyempurnaan Arsitektur**: Deskripsi yang ditingkatkan tentang Host, Client, dan Server untuk mencerminkan pola arsitektur MCP saat ini
  - Host kini didefinisikan dengan jelas sebagai aplikasi AI yang mengoordinasikan banyak koneksi klien MCP
  - Client dijelaskan sebagai penghubung protokol yang mempertahankan hubungan satu-ke-satu dengan server
  - Server ditingkatkan dengan skenario penyebaran lokal vs. jarak jauh
- **Restrukturisasi Primitif**: Perombakan lengkap primitif server dan klien
  - Primitif Server: Resources (sumber data), Prompts (template), Tools (fungsi yang dapat dieksekusi) dengan penjelasan dan contoh terperinci
  - Primitif Klien: Sampling (penyelesaian LLM), Elicitation (input pengguna), Logging (debugging/pemantauan)
  - Diperbarui dengan pola metode penemuan (`*/list`), pengambilan (`*/get`), dan eksekusi (`*/call`) saat ini
- **Arsitektur Protokol**: Memperkenalkan model arsitektur dua lapis
  - Lapisan Data: dasar JSON-RPC 2.0 dengan manajemen siklus hidup dan primitif
  - Lapisan Transportasi: STDIO (lokal) dan HTTP Streamable dengan SSE (jarak jauh) sebagai mekanisme transportasi
- **Kerangka Keamanan**: Prinsip keamanan komprehensif termasuk persetujuan pengguna eksplisit, perlindungan privasi data, keamanan eksekusi alat, dan keamanan lapisan transportasi
- **Pola Komunikasi**: Memperbarui pesan protokol untuk menunjukkan alur inisialisasi, penemuan, eksekusi, dan notifikasi
- **Contoh Kode**: Menyegarkan contoh multi-bahasa (.NET, Java, Python, JavaScript) untuk mencerminkan pola SDK MCP saat ini

#### Keamanan (02-Security/) - Perombakan Keamanan Komprehensif  
- **Keselarasan Standar**: Keselarasan penuh dengan persyaratan keamanan Spesifikasi MCP 2025-06-18
- **Evolusi Autentikasi**: Mendokumentasikan evolusi dari server OAuth kustom ke delegasi penyedia identitas eksternal (Microsoft Entra ID)
- **Analisis Ancaman Khusus AI**: Cakupan yang ditingkatkan dari vektor serangan AI modern
  - Skenario serangan injeksi prompt terperinci dengan contoh dunia nyata
  - Mekanisme keracunan alat dan pola serangan "rug pull"
  - Keracunan jendela konteks dan serangan kebingungan model
- **Solusi Keamanan AI Microsoft**: Cakupan komprehensif ekosistem keamanan Microsoft
  - AI Prompt Shields dengan deteksi lanjutan, spotlighting, dan teknik delimiter
  - Pola integrasi Azure Content Safety
  - GitHub Advanced Security untuk perlindungan rantai pasokan
- **Mitigasi Ancaman Lanjutan**: Kontrol keamanan terperinci untuk
  - Pembajakan sesi dengan skenario serangan spesifik MCP dan persyaratan ID sesi kriptografi
  - Masalah confused deputy dalam skenario proxy MCP dengan persyaratan persetujuan eksplisit
  - Kerentanan token passthrough dengan kontrol validasi wajib
- **Keamanan Rantai Pasokan**: Perluasan cakupan rantai pasokan AI termasuk model dasar, layanan embedding, penyedia konteks, dan API pihak ketiga
- **Keamanan Fondasi**: Integrasi yang ditingkatkan dengan pola keamanan perusahaan termasuk arsitektur zero trust dan ekosistem keamanan Microsoft
- **Organisasi Sumber Daya**: Mengkategorikan tautan sumber daya komprehensif berdasarkan tipe (Dokumentasi Resmi, Standar, Riset, Solusi Microsoft, Panduan Implementasi)

### Peningkatan Kualitas Dokumentasi
- **Tujuan Pembelajaran Terstruktur**: Meningkatkan tujuan pembelajaran dengan hasil yang spesifik dan dapat ditindaklanjuti
- **Referensi Silang**: Menambahkan tautan antar topik keamanan dan konsep inti terkait
- **Informasi Terkini**: Memperbarui semua referensi tanggal dan tautan spesifikasi ke standar saat ini
- **Panduan Implementasi**: Menambahkan panduan implementasi spesifik dan dapat ditindaklanjuti di seluruh kedua bagian

## 16 Juli 2025

### Perbaikan README dan Navigasi
- Mendesain ulang navigasi kurikulum di README.md secara menyeluruh
- Mengganti tag `<details>` dengan format tabel yang lebih mudah diakses
- Membuat opsi tata letak alternatif di folder baru "alternative_layouts"
- Menambahkan contoh navigasi berbasis kartu, gaya tab, dan gaya akordeon
- Memperbarui bagian struktur repositori untuk menyertakan semua file terbaru
- Meningkatkan bagian "Cara Menggunakan Kurikulum Ini" dengan rekomendasi yang jelas
- Memperbarui tautan spesifikasi MCP agar mengarah ke URL yang benar
- Menambahkan bagian Context Engineering (5.14) ke struktur kurikulum

### Pembaruan Panduan Studi
- Menyusun ulang panduan studi agar sesuai dengan struktur repositori saat ini
- Menambahkan bagian baru untuk MCP Clients dan Tools, serta MCP Servers Populer
- Memperbarui Peta Kurikulum Visual agar mencerminkan semua topik secara akurat
- Meningkatkan deskripsi Topik Lanjutan untuk mencakup semua area khusus
- Memperbarui bagian Studi Kasus agar mencerminkan contoh nyata
- Menambahkan changelog komprehensif ini

### Kontribusi Komunitas (06-CommunityContributions/)
- Menambahkan informasi terperinci tentang server MCP untuk pembuatan gambar
- Menambahkan bagian komprehensif tentang penggunaan Claude di VSCode
- Menambahkan instruksi pengaturan dan penggunaan klien terminal Cline
- Memperbarui bagian klien MCP untuk menyertakan semua opsi klien populer
- Meningkatkan contoh kontribusi dengan sampel kode yang lebih akurat

### Topik Lanjutan (05-AdvancedTopics/)
- Mengorganisir semua folder topik khusus dengan penamaan yang konsisten
- Menambahkan materi dan contoh rekayasa konteks
- Menambahkan dokumentasi integrasi agen Foundry
- Meningkatkan dokumentasi integrasi keamanan Entra ID

## 11 Juni 2025

### Pembuatan Awal
- Merilis versi pertama kurikulum MCP untuk Pemula
- Membuat struktur dasar untuk semua 10 bagian utama
- Mengimplementasikan Peta Kurikulum Visual untuk navigasi
- Menambahkan proyek contoh awal dalam berbagai bahasa pemrograman

### Memulai (03-GettingStarted/)
- Membuat contoh implementasi server pertama
- Menambahkan panduan pengembangan klien
- Menyertakan instruksi integrasi klien LLM
- Menambahkan dokumentasi integrasi VS Code
- Mengimplementasikan contoh server Server-Sent Events (SSE)

### Konsep Inti (01-CoreConcepts/)
- Menambahkan penjelasan terperinci tentang arsitektur klien-server
- Membuat dokumentasi tentang komponen protokol utama
- Mendokumentasikan pola pesan dalam MCP

## 23 Mei 2025

### Struktur Repositori
- Menginisialisasi repositori dengan struktur folder dasar
- Membuat file README untuk setiap bagian utama
- Menyiapkan infrastruktur terjemahan
- Menambahkan aset gambar dan diagram

### Dokumentasi
- Membuat README.md awal dengan gambaran kurikulum
- Menambahkan CODE_OF_CONDUCT.md dan SECURITY.md
- Menyiapkan SUPPORT.md dengan panduan untuk mendapatkan bantuan
- Membuat struktur panduan studi awal

## 15 April 2025

### Perencanaan dan Kerangka Kerja
- Perencanaan awal untuk kurikulum MCP untuk Pemula
- Mendefinisikan tujuan pembelajaran dan audiens target
- Menguraikan struktur 10 bagian kurikulum
- Mengembangkan kerangka konseptual untuk contoh dan studi kasus
- Membuat contoh prototipe awal untuk konsep kunci

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->