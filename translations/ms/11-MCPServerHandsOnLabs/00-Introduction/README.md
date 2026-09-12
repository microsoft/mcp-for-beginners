# Pengenalan Integrasi Pangkalan Data MCP

> [!NOTE]
> Rajah atau kod dalam laluan pembelajaran ini yang menggunakan HTTP/SSE atau pilihan permulaan
> mencerminkan kebergantungan MCP contoh `2025-11-25`. Untuk pelaksanaan baru,
> gunakan permintaan tanpa status `2026-07-28` dan HTTP Boleh Alir.

## 🎯 Apa Yang Diliputi dalam Makmal Ini

Makmal pengenalan ini menyediakan gambaran menyeluruh tentang membina pelayan Model Context Protocol (MCP) dengan integrasi pangkalan data. Anda akan memahami kes perniagaan, seni bina teknikal, dan aplikasi dunia sebenar melalui kes penggunaan analitik Zava Retail di https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Gambaran Keseluruhan

**Model Context Protocol (MCP)** membolehkan pembantu AI mengakses dan berinteraksi dengan sumber data luaran secara masa nyata dengan selamat. Apabila digabungkan dengan integrasi pangkalan data, MCP membuka kebolehan yang kuat untuk aplikasi AI berasaskan data.

Laluan pembelajaran ini mengajar anda membina pelayan MCP sedia produksi yang menghubungkan pembantu AI ke data jualan runcit melalui PostgreSQL, melaksanakan corak perusahaan seperti Keselamatan Tahap Baris, carian semantik, dan akses data berbilang penyewa.

## Objektif Pembelajaran

Pada akhir makmal ini, anda akan dapat:

- **Mentakrifkan** Model Context Protocol dan faedah terasnya untuk integrasi pangkalan data
- **Mengenal pasti** komponen utama seni bina pelayan MCP dengan pangkalan data
- **Memahami** kes penggunaan Zava Retail dan keperluan perniagaannya
- **Mengenali** corak perusahaan untuk akses pangkalan data yang selamat dan boleh diskala
- **Menyenaraikan** alat dan teknologi yang digunakan sepanjang laluan pembelajaran ini

## 🧭 Cabaran: AI Bertemu Data Dunia Sebenar

### Had Tradisional AI

Pembantu AI moden sangat berkuasa tetapi menghadapi had ketara apabila bekerja dengan data perniagaan dunia sebenar:

| **Cabaran** | **Penerangan** | **Impak Perniagaan** |
|---------------|-----------------|-------------------|
| **Pengetahuan Statik** | Model AI yang dilatih pada set data tetap tidak dapat mengakses data perniagaan semasa | Wawasan lama, peluang terlepas |
| **Silo Data** | Maklumat terkunci dalam pangkalan data, API, dan sistem yang AI tidak dapat capai | Analisis tidak lengkap, aliran kerja terpecah |
| **Sekatan Keselamatan** | Akses langsung pangkalan data menimbulkan kebimbangan keselamatan dan pematuhan | Pelaksanaan terhad, penyediaan data manual |
| **Pertanyaan Kompleks** | Pengguna perniagaan memerlukan pengetahuan teknikal untuk mengekstrak wawasan data | Penggunaan berkurang, proses tidak cekap |

### Penyelesaian MCP

Model Context Protocol mengatasi cabaran ini dengan menyediakan:

- **Akses Data Masa Nyata**: Pembantu AI membuat pertanyaan ke pangkalan data dan API secara langsung
- **Integrasi Selamat**: Akses terkawal dengan pengesahan dan kebenaran
- **Antara Muka Bahasa Semula Jadi**: Pengguna perniagaan bertanya soalan dalam bahasa Inggeris biasa
- **Protokol Piawai**: Berfungsi di pelbagai platform dan alat AI

## 🏪 Kenali Zava Retail: Kajian Kes Pembelajaran Kami https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Sepanjang laluan pembelajaran ini, kita akan membina pelayan MCP untuk **Zava Retail**, rangkaian runcit DIY fiksyen dengan beberapa lokasi kedai. Senario realistik ini menunjukkan pelaksanaan MCP tahap perusahaan.

### Konteks Perniagaan

**Zava Retail** mengendalikan:
- **8 kedai fizikal** di seluruh negeri Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 kedai dalam talian** untuk jualan e-dagang
- **Katalog produk pelbagai** termasuk alatan, perkakasan, bekalan taman, dan bahan binaan
- **Pengurusan berbilang tahap** dengan pengurus kedai, pengurus serantau, dan eksekutif

### Keperluan Perniagaan

Pengurus kedai dan eksekutif memerlukan analitik yang dikuasakan AI untuk:

1. **Menganalisis prestasi jualan** merentasi kedai dan tempoh masa
2. **Mengawasi tahap inventori** dan mengenal pasti keperluan pengisian semula
3. **Memahami tingkah laku pelanggan** dan corak pembelian
4. **Meneroka wawasan produk** melalui carian semantik
5. **Menjana laporan** dengan pertanyaan bahasa semula jadi
6. **Memelihara keselamatan data** dengan kawalan akses berdasarkan peranan

### Keperluan Teknikal

Pelayan MCP mesti menyediakan:

- **Akses data berbilang penyewa** di mana pengurus kedai hanya melihat data kedai mereka sendiri
- **Pertanyaan fleksibel** menyokong operasi SQL kompleks
- **Carian semantik** untuk penemuan produk dan cadangan
- **Data masa nyata** mencerminkan keadaan perniagaan semasa
- **Pengesahan selamat** dengan keselamatan tahap baris
- **Seni bina boleh diskala** menyokong berbilang pengguna serentak

## 🏗️ Gambaran Seni Bina Pelayan MCP

Pelayan MCP kami melaksanakan seni bina berlapis yang dioptimumkan untuk integrasi pangkalan data:

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

#### **1. Lapisan Pelayan MCP**
- **Rangka Kerja FastMCP**: Pelaksanaan pelayan MCP Python moden
- **Pendaftaran Alat**: Definisi alat deklaratif dengan keselamatan jenis
- **Konteks Permintaan**: Identiti pengguna dan pengurusan sesi
- **Pengendalian Ralat**: Pengurusan ralat dan pencatatan yang mantap

#### **2. Lapisan Integrasi Pangkalan Data**
- **Kolam Sambungan**: Pengurusan sambungan asyncpg yang cekap
- **Pembekal Skema**: Penemuan skema jadual dinamik
- **Pelaksana Pertanyaan**: Pelaksanaan SQL selamat dengan konteks RLS
- **Pengurusan Transaksi**: Pematuhan ACID dan pengendalian rollback

#### **3. Lapisan Keselamatan**
- **Keselamatan Tahap Baris**: PostgreSQL RLS untuk pengasingan data berbilang penyewa
- **Identiti Pengguna**: Pengesahan dan kebenaran pengurus kedai
- **Kawalan Akses**: Kebenaran halus dan jejak audit
- **Pengesahan Input**: Pencegahan suntikan SQL dan pengesahan pertanyaan

#### **4. Lapisan Peningkatan AI**
- **Carian Semantik**: Penyerapan vektor untuk penemuan produk
- **Integrasi Azure OpenAI**: Penjanaan penyerapan teks
- **Algoritma Kesamaan**: Carian kesamaan kosinus pgvector
- **Pengoptimuman Carian**: Pengindeksan dan penalaan prestasi

## 🔧 Tumpukan Teknologi

### Teknologi Teras

| **Komponen** | **Teknologi** | **Tujuan** |
|---------------|----------------|-------------|
| **Rangka MCP** | FastMCP (Python) | Pelaksanaan pelayan MCP moden |
| **Pangkalan Data** | PostgreSQL 17 + pgvector | Data berhubung dengan carian vektor |
| **Perkhidmatan AI** | Azure OpenAI | Penyerapan teks dan model bahasa |
| **Containerization** | Docker + Docker Compose | Persekitaran pembangunan |
| **Platform Awan** | Microsoft Azure | Pelaksanaan produksi |
| **Integrasi IDE** | VS Code | Sembang AI dan aliran kerja pembangunan |

### Alat Pembangunan

| **Alat** | **Tujuan** |
|----------|-------------|
| **asyncpg** | Pemandu PostgreSQL berprestasi tinggi |
| **Pydantic** | Pengesahan dan serialisasi data |
| **Azure SDK** | Integrasi perkhidmatan awan |
| **pytest** | Rangka kerja pengujian |
| **Docker** | Containerisasi dan pelaksanaan |

### Tumpukan Produksi

| **Perkhidmatan** | **Sumber Azure** | **Tujuan** |
|-------------|-------------------|-------------|
| **Pangkalan Data** | Azure Database for PostgreSQL | Perkhidmatan pangkalan data terurus |
| **Kontena** | Azure Container Apps | Hos kontena tanpa pelayan |
| **Perkhidmatan AI** | Microsoft Foundry | Model dan titik akhir OpenAI |
| **Pemantauan** | Application Insights | Kebolehpantauan dan diagnostik |
| **Keselamatan** | Azure Key Vault | Pengurusan rahsia dan konfigurasi |

## 🎬 Senario Penggunaan Dunia Sebenar

Mari teroka bagaimana pengguna berbeza berinteraksi dengan pelayan MCP kami:

### Senario 1: Ulasan Prestasi Pengurus Kedai

**Pengguna**: Sarah, Pengurus Kedai Seattle  
**Matlamat**: Menganalisis prestasi jualan suku terakhir

**Pertanyaan Bahasa Semula Jadi**:
> "Tunjukkan 10 produk teratas mengikut hasil untuk kedai saya dalam S4 2024"

**Apa Yang Berlaku**:
1. Sembang AI VS Code menghantar pertanyaan ke pelayan MCP
2. Pelayan MCP mengenal pasti konteks kedai Sarah (Seattle)
3. Polisi RLS menapis data hanya untuk kedai Seattle
4. Pertanyaan SQL dijana dan dilaksanakan
5. Keputusan diformatkan dan dihantar balik ke Sembang AI
6. AI menyediakan analisis dan wawasan

### Senario 2: Penemuan Produk dengan Carian Semantik

**Pengguna**: Mike, Pengurus Inventori  
**Matlamat**: Cari produk yang serupa dengan permintaan pelanggan

**Pertanyaan Bahasa Semula Jadi**:
> "Apakah produk yang kami jual yang serupa dengan 'penyambung elektrik kalis air untuk penggunaan luar'?"

**Apa Yang Berlaku**:
1. Pertanyaan diproses oleh alat carian semantik
2. Azure OpenAI menjana vektor penyerapan
3. pgvector melaksanakan carian kesamaan
4. Produk berkaitan disenaraikan mengikut kepentingan
5. Keputusan termasuk butiran produk dan ketersediaan
6. AI mencadangkan alternatif dan peluang bundling

### Senario 3: Analitik Rentas Kedai

**Pengguna**: Jennifer, Pengurus Serantau  
**Matlamat**: Bandingkan prestasi di semua kedai

**Pertanyaan Bahasa Semula Jadi**:
> "Bandingkan jualan mengikut kategori untuk semua kedai dalam 6 bulan terakhir"

**Apa Yang Berlaku**:
1. Konteks RLS disetkan untuk akses pengurus serantau
2. Pertanyaan multi-kedai yang kompleks dijana
3. Data diagregat merentasi lokasi kedai
4. Keputusan termasuk trend dan perbandingan
5. AI mengenal pasti wawasan dan cadangan

## 🔒 Perincian Keselamatan dan Multi-Penyewa

Pelaksanaan kami mengutamakan keselamatan tahap perusahaan:

### Keselamatan Tahap Baris (RLS)

PostgreSQL RLS memastikan pengasingan data:

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

### Pengurusan Identiti Pengguna

Setiap sambungan MCP menyertakan:
- **ID Pengurus Kedai**: Pengenal unik untuk konteks RLS
- **Penugasan Peranan**: Kebenaran dan tahap akses
- **Pengurusan Sesi**: Token pengesahan selamat
- **Pencatatan Audit**: Sejarah akses lengkap

### Perlindungan Data

Berbilang lapisan keselamatan:
- **Penyulitan Sambungan**: TLS untuk semua sambungan pangkalan data
- **Pencegahan Suntikan SQL**: Hanya pertanyaan berpembolehubah
- **Pengesahan Input**: Pengesahan permintaan menyeluruh
- **Pengendalian Ralat**: Tiada data sensitif dalam mesej ralat

## 🎯 Petua Utama

Selepas melengkapkan pengenalan ini, anda harus faham:

✅ **Cadangan Nilai MCP**: Bagaimana MCP menjembatani pembantu AI dan data dunia sebenar  
✅ **Konteks Perniagaan**: Keperluan dan cabaran Zava Retail  
✅ **Gambaran Seni Bina**: Komponen utama dan interaksi mereka  
✅ **Tumpukan Teknologi**: Alat dan rangka kerja yang digunakan sepanjang laluan  
✅ **Model Keselamatan**: Akses data berbilang penyewa dan perlindungan  
✅ **Corak Penggunaan**: Senario pertanyaan dan aliran kerja dunia sebenar  

## 🚀 Apa Seterusnya

Bersedia untuk mendalami lagi? Teruskan dengan:

**[Makmal 01: Konsep Seni Bina Teras](../01-Architecture/README.md)**

Pelajari tentang corak seni bina pelayan MCP, prinsip reka bentuk pangkalan data, dan pelaksanaan teknikal terperinci yang menggerakkan penyelesaian analitik runcit kami.

## 📚 Sumber Tambahan

### Dokumentasi MCP
- [Spesifikasi MCP](https://modelcontextprotocol.io/docs/) - Dokumentasi protokol rasmi
- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners) - Panduan pembelajaran MCP menyeluruh
- [Dokumentasi FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Dokumentasi SDK Python

### Integrasi Pangkalan Data
- [Dokumentasi PostgreSQL](https://www.postgresql.org/docs/) - Rujukan lengkap PostgreSQL
- [Panduan pgvector](https://github.com/pgvector/pgvector) - Dokumentasi sambungan vektor
- [Keselamatan Tahap Baris](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Panduan RLS PostgreSQL

### Perkhidmatan Azure
- [Dokumentasi Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrasi perkhidmatan AI
- [Azure Database untuk PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Perkhidmatan pengurusan pangkalan data
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Kontena tanpa pelayan

---

**Penafian**: Ini adalah latihan pembelajaran menggunakan data runcit fiksyen. Sentiasa ikut polisi tadbir urus data dan keselamatan organisasi anda apabila melaksanakan penyelesaian serupa dalam persekitaran produksi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->