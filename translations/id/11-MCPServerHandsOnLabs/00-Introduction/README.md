# Pengantar Integrasi Database MCP

## 🎯 Apa yang Dibahas dalam Lab Ini

Lab pengantar ini memberikan gambaran menyeluruh tentang cara membangun server Model Context Protocol (MCP) dengan integrasi database. Anda akan memahami kasus bisnis, arsitektur teknis, dan aplikasi dunia nyata melalui studi kasus analitik Zava Retail di https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Gambaran Umum

**Model Context Protocol (MCP)** memungkinkan asisten AI untuk mengakses dan berinteraksi dengan sumber data eksternal secara aman dan real-time. Ketika digabungkan dengan integrasi database, MCP membuka kemampuan yang kuat untuk aplikasi AI berbasis data.

Jalur pembelajaran ini mengajarkan Anda cara membangun server MCP siap produksi yang menghubungkan asisten AI ke data penjualan ritel melalui PostgreSQL, dengan menerapkan pola perusahaan seperti Row Level Security, pencarian semantik, dan akses data multi-tenant.

## Tujuan Pembelajaran

Pada akhir lab ini, Anda akan dapat:

- **Mendefinisikan** Model Context Protocol dan manfaat utamanya untuk integrasi database
- **Mengidentifikasi** komponen utama arsitektur server MCP dengan database
- **Memahami** studi kasus Zava Retail dan kebutuhan bisnisnya
- **Mengenali** pola perusahaan untuk akses database yang aman dan skalabel
- **Mendaftar** alat dan teknologi yang digunakan sepanjang jalur pembelajaran ini

## 🧭 Tantangan: AI Bertemu Data Dunia Nyata

### Keterbatasan AI Tradisional

Asisten AI modern sangat kuat tetapi menghadapi keterbatasan signifikan saat bekerja dengan data bisnis dunia nyata:

| **Tantangan** | **Deskripsi** | **Dampak Bisnis** |
|---------------|-----------------|-------------------|
| **Pengetahuan Statis** | Model AI yang dilatih pada dataset tetap tidak dapat mengakses data bisnis terkini | Wawasan usang, peluang terlewatkan |
| **Silo Data** | Informasi terkunci dalam database, API, dan sistem yang tidak dapat dijangkau AI | Analisis tidak lengkap, alur kerja terfragmentasi |
| **Kendala Keamanan** | Akses langsung ke database meningkatkan risiko keamanan dan kepatuhan | Penerapan terbatas, persiapan data manual |
| **Kueri Kompleks** | Pengguna bisnis membutuhkan pengetahuan teknis untuk mendapatkan wawasan data | Adopsi berkurang, proses tidak efisien |

### Solusi MCP

Model Context Protocol mengatasi tantangan ini dengan menyediakan:

- **Akses Data Real-time**: Asisten AI dapat melakukan kueri ke database dan API secara langsung
- **Integrasi Aman**: Akses terkontrol dengan autentikasi dan izin
- **Antarmuka Bahasa Alami**: Pengguna bisnis dapat bertanya dengan bahasa sehari-hari
- **Protokol Standar**: Dapat digunakan di berbagai platform dan alat AI

## 🏪 Kenali Zava Retail: Studi Kasus Pembelajaran Kita https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Sepanjang jalur pembelajaran ini, kita akan membangun server MCP untuk **Zava Retail**, sebuah rantai ritel DIY fiktif dengan beberapa lokasi toko. Skenario realistis ini menunjukkan implementasi MCP tingkat perusahaan.

### Konteks Bisnis

**Zava Retail** mengoperasikan:
- **8 toko fisik** di negara bagian Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 toko online** untuk penjualan e-commerce
- **Katalog produk beragam** termasuk alat, perangkat keras, perlengkapan taman, dan bahan bangunan
- **Manajemen multi-level** dengan manajer toko, manajer regional, dan eksekutif

### Kebutuhan Bisnis

Manajer toko dan eksekutif membutuhkan analitik berbasis AI untuk:

1. **Menganalisis kinerja penjualan** di berbagai toko dan periode waktu
2. **Melacak tingkat inventaris** dan mengidentifikasi kebutuhan restocking
3. **Memahami perilaku pelanggan** dan pola pembelian
4. **Menemukan wawasan produk** melalui pencarian semantik
5. **Menghasilkan laporan** dengan kueri bahasa alami
6. **Menjaga keamanan data** dengan kontrol akses berbasis peran

### Kebutuhan Teknis

Server MCP harus menyediakan:

- **Akses data multi-tenant** di mana manajer toko hanya melihat data toko mereka
- **Kueri fleksibel** yang mendukung operasi SQL kompleks
- **Pencarian semantik** untuk penemuan produk dan rekomendasi
- **Data real-time** yang mencerminkan kondisi bisnis terkini
- **Autentikasi aman** dengan keamanan tingkat baris (Row Level Security)
- **Arsitektur skalabel** yang mendukung banyak pengguna secara bersamaan

## 🏗️ Gambaran Arsitektur Server MCP

Server MCP kita menerapkan arsitektur berlapis yang dioptimalkan untuk integrasi database:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Komponen Utama

#### **1. Lapisan Server MCP**
- **FastMCP Framework**: Implementasi server MCP modern dengan Python
- **Pendaftaran Alat**: Definisi alat deklaratif dengan keamanan tipe
- **Konteks Permintaan**: Manajemen identitas pengguna dan sesi
- **Penanganan Kesalahan**: Manajemen kesalahan dan logging yang kuat

#### **2. Lapisan Integrasi Database**
- **Connection Pooling**: Manajemen koneksi asyncpg yang efisien
- **Schema Provider**: Penemuan skema tabel dinamis
- **Query Executor**: Eksekusi SQL yang aman dengan konteks RLS
- **Manajemen Transaksi**: Kepatuhan ACID dan penanganan rollback

#### **3. Lapisan Keamanan**
- **Row Level Security**: PostgreSQL RLS untuk isolasi data multi-tenant
- **Identitas Pengguna**: Autentikasi dan otorisasi manajer toko
- **Kontrol Akses**: Izin yang terperinci dan jejak audit
- **Validasi Input**: Pencegahan injeksi SQL dan validasi kueri

#### **4. Lapisan Peningkatan AI**
- **Pencarian Semantik**: Embedding vektor untuk penemuan produk
- **Integrasi Azure OpenAI**: Pembuatan embedding teks
- **Algoritma Kemiripan**: Pencarian kemiripan cosine pgvector
- **Optimasi Pencarian**: Pengindeksan dan penyetelan kinerja

## 🔧 Teknologi yang Digunakan

### Teknologi Inti

| **Komponen** | **Teknologi** | **Tujuan** |
|---------------|----------------|-------------|
| **Framework MCP** | FastMCP (Python) | Implementasi server MCP modern |
| **Database** | PostgreSQL 17 + pgvector | Data relasional dengan pencarian vektor |
| **Layanan AI** | Azure OpenAI | Embedding teks dan model bahasa |
| **Kontainerisasi** | Docker + Docker Compose | Lingkungan pengembangan |
| **Platform Cloud** | Microsoft Azure | Penerapan produksi |
| **Integrasi IDE** | VS Code | AI Chat dan alur kerja pengembangan |

### Alat Pengembangan

| **Alat** | **Tujuan** |
|----------|-------------|
| **asyncpg** | Driver PostgreSQL berkinerja tinggi |
| **Pydantic** | Validasi dan serialisasi data |
| **Azure SDK** | Integrasi layanan cloud |
| **pytest** | Kerangka kerja pengujian |
| **Docker** | Kontainerisasi dan penerapan |

### Stack Produksi

| **Layanan** | **Sumber Daya Azure** | **Tujuan** |
|-------------|-----------------------|-------------|
| **Database** | Azure Database for PostgreSQL | Layanan database terkelola |
| **Kontainer** | Azure Container Apps | Hosting kontainer tanpa server |
| **Layanan AI** | Azure AI Foundry | Model OpenAI dan endpoint |
| **Pemantauan** | Application Insights | Observabilitas dan diagnostik |
| **Keamanan** | Azure Key Vault | Manajemen rahasia dan konfigurasi |

## 🎬 Skenario Penggunaan Dunia Nyata

Mari kita eksplorasi bagaimana pengguna berinteraksi dengan server MCP kita:

### Skenario 1: Tinjauan Kinerja Manajer Toko

**Pengguna**: Sarah, Manajer Toko Seattle  
**Tujuan**: Menganalisis kinerja penjualan kuartal terakhir

**Kueri Bahasa Alami**:
> "Tunjukkan 10 produk teratas berdasarkan pendapatan untuk toko saya di Q4 2024"

**Apa yang Terjadi**:
1. VS Code AI Chat mengirimkan kueri ke server MCP
2. Server MCP mengidentifikasi konteks toko Sarah (Seattle)
3. Kebijakan RLS memfilter data hanya untuk toko Seattle
4. Kueri SQL dibuat dan dijalankan
5. Hasil diformat dan dikembalikan ke AI Chat
6. AI memberikan analisis dan wawasan

### Skenario 2: Penemuan Produk dengan Pencarian Semantik

**Pengguna**: Mike, Manajer Inventaris  
**Tujuan**: Menemukan produk yang mirip dengan permintaan pelanggan

**Kueri Bahasa Alami**:
> "Produk apa yang kita jual yang mirip dengan 'konektor listrik tahan air untuk penggunaan luar ruangan'?"

**Apa yang Terjadi**:
1. Kueri diproses oleh alat pencarian semantik
2. Azure OpenAI menghasilkan vektor embedding
3. pgvector melakukan pencarian kemiripan
4. Produk terkait diberi peringkat berdasarkan relevansi
5. Hasil mencakup detail produk dan ketersediaan
6. AI menyarankan alternatif dan peluang bundling

### Skenario 3: Analitik Lintas Toko

**Pengguna**: Jennifer, Manajer Regional  
**Tujuan**: Membandingkan kinerja di semua toko

**Kueri Bahasa Alami**:
> "Bandingkan penjualan berdasarkan kategori untuk semua toko dalam 6 bulan terakhir"

**Apa yang Terjadi**:
1. Konteks RLS diatur untuk akses manajer regional
2. Kueri multi-toko kompleks dibuat
3. Data diaggregasi di seluruh lokasi toko
4. Hasil mencakup tren dan perbandingan
5. AI mengidentifikasi wawasan dan rekomendasi

## 🔒 Pendalaman Keamanan dan Multi-Tenancy

Implementasi kita memprioritaskan keamanan tingkat perusahaan:

### Row Level Security (RLS)

PostgreSQL RLS memastikan isolasi data:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Manajemen Identitas Pengguna

Setiap koneksi MCP mencakup:
- **ID Manajer Toko**: Pengidentifikasi unik untuk konteks RLS
- **Penugasan Peran**: Izin dan tingkat akses
- **Manajemen Sesi**: Token autentikasi yang aman
- **Logging Audit**: Riwayat akses lengkap

### Perlindungan Data

Lapisan keamanan yang beragam:
- **Enkripsi Koneksi**: TLS untuk semua koneksi database
- **Pencegahan Injeksi SQL**: Hanya kueri yang diparameterkan
- **Validasi Input**: Validasi permintaan yang komprehensif
- **Penanganan Kesalahan**: Tidak ada data sensitif dalam pesan kesalahan

## 🎯 Poin Penting

Setelah menyelesaikan pengantar ini, Anda seharusnya memahami:

✅ **Nilai MCP**: Bagaimana MCP menjembatani asisten AI dan data dunia nyata  
✅ **Konteks Bisnis**: Kebutuhan dan tantangan Zava Retail  
✅ **Gambaran Arsitektur**: Komponen utama dan interaksinya  
✅ **Teknologi yang Digunakan**: Alat dan kerangka kerja yang digunakan sepanjang jalur ini  
✅ **Model Keamanan**: Akses data multi-tenant dan perlindungan  
✅ **Pola Penggunaan**: Skenario kueri dunia nyata dan alur kerja  

## 🚀 Langkah Selanjutnya

Siap untuk mendalami lebih jauh? Lanjutkan dengan:

**[Lab 01: Konsep Arsitektur Inti](../01-Architecture/README.md)**

Pelajari pola arsitektur server MCP, prinsip desain database, dan implementasi teknis mendetail yang mendukung solusi analitik ritel kita.

## 📚 Sumber Daya Tambahan

### Dokumentasi MCP
- [Spesifikasi MCP](https://modelcontextprotocol.io/docs/) - Dokumentasi resmi protokol
- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners) - Panduan pembelajaran MCP yang komprehensif
- [Dokumentasi FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Dokumentasi SDK Python

### Integrasi Database
- [Dokumentasi PostgreSQL](https://www.postgresql.org/docs/) - Referensi lengkap PostgreSQL
- [Panduan pgvector](https://github.com/pgvector/pgvector) - Dokumentasi ekstensi vektor
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Panduan RLS PostgreSQL

### Layanan Azure
- [Dokumentasi Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrasi layanan AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Layanan database terkelola
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Kontainer tanpa server

---

**Disclaimer**: Ini adalah latihan pembelajaran menggunakan data ritel fiktif. Selalu ikuti kebijakan tata kelola dan keamanan data organisasi Anda saat menerapkan solusi serupa di lingkungan produksi.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.