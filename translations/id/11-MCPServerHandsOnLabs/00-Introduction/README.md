# Pengenalan Integrasi Database MCP

> [!NOTE]
> Diagram atau kode dalam jalur pembelajaran ini yang menggunakan HTTP/SSE atau opsi inisialisasi
> mencerminkan ketergantungan MCP `2025-11-25` dari contoh. Untuk
> implementasi baru, gunakan permintaan tanpa status `2026-07-28` dan HTTP yang Dapat Dialirkan.

## 🎯 Apa yang Dicakup oleh Lab Ini

Lab pengenalan ini memberikan ikhtisar komprehensif tentang membangun server Model Context Protocol (MCP) dengan integrasi database. Anda akan memahami kasus bisnis, arsitektur teknis, dan aplikasi dunia nyata melalui studi kasus analitik Zava Retail di https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Ikhtisar

**Model Context Protocol (MCP)** memungkinkan asisten AI mengakses dan berinteraksi dengan sumber data eksternal secara real-time dengan aman. Ketika digabungkan dengan integrasi database, MCP membuka kemampuan kuat untuk aplikasi AI yang didorong oleh data.

Jalur pembelajaran ini mengajarkan Anda membangun server MCP yang siap produksi yang menghubungkan asisten AI ke data penjualan ritel melalui PostgreSQL, mengimplementasikan pola perusahaan seperti Row Level Security, pencarian semantik, dan akses data multi-penyewa.

## Tujuan Pembelajaran

Pada akhir lab ini, Anda akan dapat:

- **Mendefinisikan** Model Context Protocol dan manfaat inti untuk integrasi database
- **Mengidentifikasi** komponen kunci arsitektur server MCP dengan database
- **Memahami** studi kasus Zava Retail dan kebutuhan bisnisnya
- **Mengenali** pola perusahaan untuk akses database yang aman dan skalabel
- **Mendaftar** alat dan teknologi yang digunakan sepanjang jalur pembelajaran ini

## 🧭 Tantangan: AI Bertemu Data Dunia Nyata

### Keterbatasan AI Tradisional

Asisten AI modern sangat kuat tetapi menghadapi keterbatasan signifikan saat bekerja dengan data bisnis dunia nyata:

| **Tantangan** | **Deskripsi** | **Dampak Bisnis** |
|---------------|-----------------|-------------------|
| **Pengetahuan Statis** | Model AI yang dilatih pada dataset tetap tidak dapat mengakses data bisnis terkini | Wawasan usang, peluang terlewat |
| **Silo Data** | Informasi terkunci di database, API, dan sistem yang tidak bisa dijangkau AI | Analisis tidak lengkap, alur kerja terfragmentasi |
| **Keterbatasan Keamanan** | Akses langsung ke database menimbulkan kekhawatiran keamanan dan kepatuhan | Penerapan terbatas, persiapan data manual |
| **Query Kompleks** | Pengguna bisnis membutuhkan pengetahuan teknis untuk mengekstrak wawasan data | Adopsi berkurang, proses tidak efisien |

### Solusi MCP

Model Context Protocol mengatasi tantangan ini dengan menyediakan:

- **Akses Data Real-time**: Asisten AI mengquery database dan API secara langsung
- **Integrasi Aman**: Akses terkontrol dengan autentikasi dan izin
- **Antarmuka Bahasa Alami**: Pengguna bisnis mengajukan pertanyaan dalam bahasa Inggris biasa
- **Protokol Standar**: Bekerja di berbagai platform dan alat AI

## 🏪 Kenalan dengan Zava Retail: Studi Kasus Pembelajaran Kami https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Sepanjang jalur pembelajaran ini, kita akan membangun server MCP untuk **Zava Retail**, sebuah rantai ritel DIY fiktif dengan beberapa lokasi toko. Skenario realistis ini menunjukkan implementasi MCP kelas perusahaan.

### Konteks Bisnis

**Zava Retail** mengoperasikan:
- **8 toko fisik** di seluruh negara bagian Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 toko online** untuk penjualan e-commerce
- **Katalog produk beragam** termasuk alat, perangkat keras, perlengkapan taman, dan bahan bangunan
- **Manajemen berjenjang** dengan manajer toko, manajer regional, dan eksekutif

### Kebutuhan Bisnis

Manajer toko dan eksekutif membutuhkan analitik bertenaga AI untuk:

1. **Menganalisis kinerja penjualan** di seluruh toko dan periode waktu
2. **Melacak tingkat inventaris** dan mengidentifikasi kebutuhan pengisian ulang
3. **Memahami perilaku pelanggan** dan pola pembelian
4. **Menemukan wawasan produk** melalui pencarian semantik
5. **Menghasilkan laporan** dengan query bahasa alami
6. **Menjaga keamanan data** dengan kontrol akses berbasis peran

### Kebutuhan Teknis

Server MCP harus menyediakan:

- **Akses data multi-penyewa** di mana manajer toko hanya melihat data toko mereka
- **Query fleksibel** mendukung operasi SQL kompleks
- **Pencarian semantik** untuk penemuan produk dan rekomendasi
- **Data real-time** yang mencerminkan kondisi bisnis terkini
- **Autentikasi aman** dengan row-level security
- **Arsitektur skalabel** mendukung banyak pengguna bersamaan

## 🏗️ Ikhtisar Arsitektur Server MCP

Server MCP kami mengimplementasikan arsitektur berlapis yang dioptimalkan untuk integrasi database:

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

### Komponen Kunci

#### **1. Lapisan Server MCP**
- **FastMCP Framework**: Implementasi server MCP modern dengan Python
- **Registrasi Alat**: Definisi alat deklaratif dengan keamanan tipe
- **Konteks Permintaan**: Manajemen identitas pengguna dan sesi
- **Penanganan Error**: Manajemen error dan pencatatan yang kuat

#### **2. Lapisan Integrasi Database**
- **Connection Pooling**: Manajemen koneksi asyncpg yang efisien
- **Penyedia Skema**: Penemuan skema tabel dinamis
- **Eksekutor Query**: Eksekusi SQL aman dengan konteks RLS
- **Manajemen Transaksi**: Kepatuhan ACID dan penanganan rollback

#### **3. Lapisan Keamanan**
- **Row Level Security**: PostgreSQL RLS untuk isolasi data multi-penyewa
- **Identitas Pengguna**: Autentikasi dan otorisasi manajer toko
- **Kontrol Akses**: Izin rinci dan jejak audit
- **Validasi Input**: Pencegahan injeksi SQL dan validasi query

#### **4. Lapisan Peningkatan AI**
- **Pencarian Semantik**: Embedding vektor untuk penemuan produk
- **Integrasi Azure OpenAI**: Pembuatan embedding teks
- **Algoritma Kemiripan**: Pencarian kemiripan kosinus pgvector
- **Optimasi Pencarian**: Pengindeksan dan penyetelan kinerja

## 🔧 Tumpukan Teknologi

### Teknologi Inti

| **Komponen** | **Teknologi** | **Tujuan** |
|---------------|----------------|-------------|
| **Kerangka MCP** | FastMCP (Python) | Implementasi server MCP modern |
| **Database** | PostgreSQL 17 + pgvector | Data relasional dengan pencarian vektor |
| **Layanan AI** | Azure OpenAI | Embedding teks dan model bahasa |
| **Kontainerisasi** | Docker + Docker Compose | Lingkungan pengembangan |
| **Platform Cloud** | Microsoft Azure | Deployment produksi |
| **Integrasi IDE** | VS Code | Chat AI dan alur kerja pengembangan |

### Alat Pengembangan

| **Alat** | **Tujuan** |
|----------|-------------|
| **asyncpg** | Driver PostgreSQL berperforma tinggi |
| **Pydantic** | Validasi data dan serialisasi |
| **Azure SDK** | Integrasi layanan cloud |
| **pytest** | Kerangka pengujian |
| **Docker** | Kontainerisasi dan deployment |

### Tumpukan Produksi

| **Layanan** | **Sumber Daya Azure** | **Tujuan** |
|-------------|-------------------|-------------|
| **Database** | Azure Database for PostgreSQL | Layanan database terkelola |
| **Kontainer** | Azure Container Apps | Hosting kontainer tanpa server |
| **Layanan AI** | Microsoft Foundry | Model dan endpoint OpenAI |
| **Monitoring** | Application Insights | Observabilitas dan diagnostik |
| **Keamanan** | Azure Key Vault | Pengelolaan rahasia dan konfigurasi |

## 🎬 Skenario Penggunaan Dunia Nyata

Mari jelajahi bagaimana berbagai pengguna berinteraksi dengan server MCP kami:

### Skenario 1: Tinjauan Kinerja Manajer Toko

**Pengguna**: Sarah, Manajer Toko Seattle  
**Tujuan**: Menganalisis kinerja penjualan kuartal terakhir

**Query Bahasa Alami**:
> "Tampilkan 10 produk teratas berdasarkan pendapatan untuk toko saya di Q4 2024"

**Yang Terjadi**:
1. Chat AI VS Code mengirim query ke server MCP
2. Server MCP mengidentifikasi konteks toko Sarah (Seattle)
3. Kebijakan RLS memfilter data hanya untuk toko Seattle
4. Query SQL dibuat dan dijalankan
5. Hasil dipformat dan dikembalikan ke Chat AI
6. AI memberikan analisis dan wawasan

### Skenario 2: Penemuan Produk dengan Pencarian Semantik

**Pengguna**: Mike, Manajer Inventaris  
**Tujuan**: Menemukan produk yang mirip dengan permintaan pelanggan

**Query Bahasa Alami**:
> "Produk apa yang kami jual yang mirip dengan 'konektor listrik tahan air untuk penggunaan luar ruangan'?"

**Yang Terjadi**:
1. Query diproses oleh alat pencarian semantik
2. Azure OpenAI menghasilkan vektor embedding
3. pgvector melakukan pencarian kemiripan
4. Produk terkait diberi peringkat berdasarkan relevansi
5. Hasil menyertakan detail produk dan ketersediaan
6. AI menyarankan alternatif dan peluang bundling

### Skenario 3: Analitik Lintas Toko

**Pengguna**: Jennifer, Manajer Regional  
**Tujuan**: Membandingkan kinerja di seluruh toko

**Query Bahasa Alami**:
> "Bandingkan penjualan berdasarkan kategori untuk semua toko dalam 6 bulan terakhir"

**Yang Terjadi**:
1. Konteks RLS diset untuk akses manajer regional
2. Query multi-toko kompleks dibuat
3. Data digabungkan di seluruh lokasi toko
4. Hasil menyertakan tren dan perbandingan
5. AI mengidentifikasi wawasan dan rekomendasi

## 🔒 Penjelasan Mendalam Keamanan dan Multi-Penyewa

Implementasi kami memprioritaskan keamanan kelas perusahaan:

### Row Level Security (RLS)

PostgreSQL RLS menjamin isolasi data:

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
- **ID Manajer Toko**: Identifier unik untuk konteks RLS
- **Penetapan Peran**: Izin dan tingkat akses
- **Manajemen Sesi**: Token autentikasi yang aman
- **Audit Logging**: Riwayat akses lengkap

### Perlindungan Data

Beberapa lapisan keamanan:
- **Enkripsi Koneksi**: TLS untuk semua koneksi database
- **Pencegahan Injeksi SQL**: Hanya query terparameterisasi
- **Validasi Input**: Validasi permintaan yang komprehensif
- **Penanganan Error**: Tidak ada data sensitif dalam pesan error

## 🎯 Poin-Poin Penting

Setelah menyelesaikan pengenalan ini, Anda seharusnya memahami:

✅ **Proposisi Nilai MCP**: Bagaimana MCP menjembatani asisten AI dan data dunia nyata  
✅ **Konteks Bisnis**: Kebutuhan dan tantangan Zava Retail  
✅ **Ikhtisar Arsitektur**: Komponen kunci dan interaksi mereka  
✅ **Tumpukan Teknologi**: Alat dan kerangka kerja yang digunakan sepanjang jalur  
✅ **Model Keamanan**: Akses data multi-penyewa dan perlindungan  
✅ **Pola Penggunaan**: Skenario query dunia nyata dan alur kerja  

## 🚀 Selanjutnya

Siap untuk menyelami lebih dalam? Lanjutkan dengan:

**[Lab 01: Konsep Arsitektur Inti](../01-Architecture/README.md)**

Pelajari pola arsitektur server MCP, prinsip desain database, dan implementasi teknis rinci yang menggerakkan solusi analitik ritel kami.

## 📚 Sumber Daya Tambahan

### Dokumentasi MCP
- [Spesifikasi MCP](https://modelcontextprotocol.io/docs/) - Dokumentasi protokol resmi
- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners) - Panduan pembelajaran MCP komprehensif
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

**Penafian**: Ini adalah latihan pembelajaran menggunakan data ritel fiktif. Selalu ikuti kebijakan tata kelola data dan keamanan organisasi Anda saat mengimplementasikan solusi serupa dalam lingkungan produksi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->