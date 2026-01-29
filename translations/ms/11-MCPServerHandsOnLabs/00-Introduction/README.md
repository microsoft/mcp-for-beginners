# Pengenalan kepada Integrasi Pangkalan Data MCP

## 🎯 Apa yang Diliputi oleh Makmal Ini

Makmal pengenalan ini memberikan gambaran menyeluruh tentang cara membina pelayan Model Context Protocol (MCP) dengan integrasi pangkalan data. Anda akan memahami kes perniagaan, seni bina teknikal, dan aplikasi dunia sebenar melalui kes penggunaan analitik Zava Retail di https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Gambaran Keseluruhan

**Model Context Protocol (MCP)** membolehkan pembantu AI mengakses dan berinteraksi dengan sumber data luaran secara selamat dalam masa nyata. Apabila digabungkan dengan integrasi pangkalan data, MCP membuka potensi besar untuk aplikasi AI yang didorong oleh data.

Laluan pembelajaran ini mengajar anda cara membina pelayan MCP yang sedia untuk pengeluaran, yang menghubungkan pembantu AI kepada data jualan runcit melalui PostgreSQL, dengan melaksanakan corak perusahaan seperti Keselamatan Tahap Baris (Row Level Security), carian semantik, dan akses data pelbagai penyewa.

## Objektif Pembelajaran

Pada akhir makmal ini, anda akan dapat:

- **Mendefinisikan** Model Context Protocol dan manfaat utamanya untuk integrasi pangkalan data
- **Mengenal pasti** komponen utama seni bina pelayan MCP dengan pangkalan data
- **Memahami** kes penggunaan Zava Retail dan keperluan perniagaannya
- **Mengenali** corak perusahaan untuk akses pangkalan data yang selamat dan boleh diskalakan
- **Menyenaraikan** alat dan teknologi yang digunakan sepanjang laluan pembelajaran ini

## 🧭 Cabaran: AI Bertemu Data Dunia Sebenar

### Keterbatasan AI Tradisional

Pembantu AI moden sangat berkuasa tetapi menghadapi keterbatasan besar apabila bekerja dengan data perniagaan dunia sebenar:

| **Cabaran** | **Penerangan** | **Kesan Perniagaan** |
|-------------|----------------|-----------------------|
| **Pengetahuan Statik** | Model AI yang dilatih pada set data tetap tidak dapat mengakses data perniagaan semasa | Wawasan yang ketinggalan zaman, peluang terlepas |
| **Silo Data** | Maklumat terkunci dalam pangkalan data, API, dan sistem yang tidak dapat dicapai oleh AI | Analisis tidak lengkap, aliran kerja terpecah |
| **Kekangan Keselamatan** | Akses langsung ke pangkalan data menimbulkan kebimbangan keselamatan dan pematuhan | Penggunaan terhad, penyediaan data secara manual |
| **Pertanyaan Kompleks** | Pengguna perniagaan memerlukan pengetahuan teknikal untuk mendapatkan wawasan data | Penggunaan berkurang, proses tidak efisien |

### Penyelesaian MCP

Model Context Protocol menangani cabaran ini dengan menyediakan:

- **Akses Data Masa Nyata**: Pembantu AI membuat pertanyaan kepada pangkalan data dan API secara langsung
- **Integrasi Selamat**: Akses terkawal dengan pengesahan dan kebenaran
- **Antara Muka Bahasa Semula Jadi**: Pengguna perniagaan bertanya dalam bahasa biasa
- **Protokol Standard**: Berfungsi merentasi platform dan alat AI yang berbeza

## 🏪 Kenali Zava Retail: Kajian Kes Pembelajaran Kita https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Sepanjang laluan pembelajaran ini, kita akan membina pelayan MCP untuk **Zava Retail**, sebuah rangkaian runcit DIY fiksyen dengan pelbagai lokasi kedai. Senario realistik ini menunjukkan pelaksanaan MCP peringkat perusahaan.

### Konteks Perniagaan

**Zava Retail** mengendalikan:
- **8 kedai fizikal** di seluruh negeri Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 kedai dalam talian** untuk jualan e-dagang
- **Katalog produk yang pelbagai** termasuk alat, perkakasan, bekalan taman, dan bahan binaan
- **Pengurusan pelbagai peringkat** dengan pengurus kedai, pengurus wilayah, dan eksekutif

### Keperluan Perniagaan

Pengurus kedai dan eksekutif memerlukan analitik berkuasa AI untuk:

1. **Menganalisis prestasi jualan** di seluruh kedai dan tempoh masa
2. **Menjejaki tahap inventori** dan mengenal pasti keperluan pengisian semula
3. **Memahami tingkah laku pelanggan** dan corak pembelian
4. **Menemui wawasan produk** melalui carian semantik
5. **Menjana laporan** dengan pertanyaan bahasa semula jadi
6. **Menjaga keselamatan data** dengan kawalan akses berdasarkan peranan

### Keperluan Teknikal

Pelayan MCP mesti menyediakan:

- **Akses data pelbagai penyewa** di mana pengurus kedai hanya melihat data kedai mereka
- **Pertanyaan fleksibel** yang menyokong operasi SQL yang kompleks
- **Carian semantik** untuk penemuan dan cadangan produk
- **Data masa nyata** yang mencerminkan keadaan perniagaan semasa
- **Pengesahan selamat** dengan keselamatan tahap baris
- **Seni bina yang boleh diskalakan** menyokong pengguna serentak yang banyak

## 🏗️ Gambaran Keseluruhan Seni Bina Pelayan MCP

Pelayan MCP kita melaksanakan seni bina berlapis yang dioptimumkan untuk integrasi pangkalan data:

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
- **Kerangka FastMCP**: Pelaksanaan pelayan MCP moden menggunakan Python
- **Pendaftaran Alat**: Definisi alat secara deklaratif dengan keselamatan jenis
- **Konteks Permintaan**: Pengurusan identiti pengguna dan sesi
- **Pengendalian Ralat**: Pengurusan ralat yang kukuh dan log

#### **2. Lapisan Integrasi Pangkalan Data**
- **Pengumpulan Sambungan**: Pengurusan sambungan asyncpg yang efisien
- **Penyedia Skema**: Penemuan skema jadual secara dinamik
- **Pelaksana Pertanyaan**: Pelaksanaan SQL yang selamat dengan konteks RLS
- **Pengurusan Transaksi**: Pematuhan ACID dan pengendalian rollback

#### **3. Lapisan Keselamatan**
- **Keselamatan Tahap Baris**: PostgreSQL RLS untuk pengasingan data pelbagai penyewa
- **Identiti Pengguna**: Pengesahan dan kebenaran pengurus kedai
- **Kawalan Akses**: Kebenaran yang terperinci dan jejak audit
- **Pengesahan Input**: Pencegahan suntikan SQL dan pengesahan pertanyaan

#### **4. Lapisan Peningkatan AI**
- **Carian Semantik**: Penemuan produk menggunakan vektor embedding
- **Integrasi Azure OpenAI**: Penjanaan embedding teks
- **Algoritma Keserupaan**: Carian keserupaan cosine pgvector
- **Pengoptimuman Carian**: Pengindeksan dan penalaan prestasi

## 🔧 Teknologi yang Digunakan

### Teknologi Teras

| **Komponen** | **Teknologi** | **Tujuan** |
|--------------|---------------|------------|
| **Kerangka MCP** | FastMCP (Python) | Pelaksanaan pelayan MCP moden |
| **Pangkalan Data** | PostgreSQL 17 + pgvector | Data relasional dengan carian vektor |
| **Perkhidmatan AI** | Azure OpenAI | Embedding teks dan model bahasa |
| **Kontainerisasi** | Docker + Docker Compose | Persekitaran pembangunan |
| **Platform Awan** | Microsoft Azure | Penggunaan pengeluaran |
| **Integrasi IDE** | VS Code | AI Chat dan aliran kerja pembangunan |

### Alat Pembangunan

| **Alat** | **Tujuan** |
|----------|------------|
| **asyncpg** | Pemacu PostgreSQL berprestasi tinggi |
| **Pydantic** | Pengesahan dan serialisasi data |
| **Azure SDK** | Integrasi perkhidmatan awan |
| **pytest** | Kerangka ujian |
| **Docker** | Kontainerisasi dan penggunaan |

### Tumpukan Pengeluaran

| **Perkhidmatan** | **Sumber Azure** | **Tujuan** |
|------------------|------------------|------------|
| **Pangkalan Data** | Azure Database for PostgreSQL | Perkhidmatan pangkalan data terurus |
| **Kontainer** | Azure Container Apps | Hosting kontainer tanpa pelayan |
| **Perkhidmatan AI** | Azure AI Foundry | Model dan titik akhir OpenAI |
| **Pemantauan** | Application Insights | Pemerhatian dan diagnostik |
| **Keselamatan** | Azure Key Vault | Pengurusan rahsia dan konfigurasi |

## 🎬 Senario Penggunaan Dunia Sebenar

Mari kita terokai bagaimana pengguna berbeza berinteraksi dengan pelayan MCP kita:

### Senario 1: Kajian Prestasi Pengurus Kedai

**Pengguna**: Sarah, Pengurus Kedai Seattle  
**Matlamat**: Menganalisis prestasi jualan suku terakhir

**Pertanyaan Bahasa Semula Jadi**:
> "Tunjukkan kepada saya 10 produk teratas mengikut hasil untuk kedai saya pada Q4 2024"

**Apa yang Berlaku**:
1. VS Code AI Chat menghantar pertanyaan ke pelayan MCP
2. Pelayan MCP mengenal pasti konteks kedai Sarah (Seattle)
3. Polisi RLS menapis data hanya untuk kedai Seattle
4. Pertanyaan SQL dijana dan dilaksanakan
5. Hasil diformatkan dan dikembalikan ke AI Chat
6. AI memberikan analisis dan wawasan

### Senario 2: Penemuan Produk dengan Carian Semantik

**Pengguna**: Mike, Pengurus Inventori  
**Matlamat**: Mencari produk yang serupa dengan permintaan pelanggan

**Pertanyaan Bahasa Semula Jadi**:
> "Apakah produk yang kita jual yang serupa dengan 'penyambung elektrik kalis air untuk kegunaan luar'?"

**Apa yang Berlaku**:
1. Pertanyaan diproses oleh alat carian semantik
2. Azure OpenAI menjana vektor embedding
3. pgvector melaksanakan carian keserupaan
4. Produk berkaitan disenaraikan mengikut relevansi
5. Hasil termasuk butiran produk dan ketersediaan
6. AI mencadangkan alternatif dan peluang bundling

### Senario 3: Analitik Merentas Kedai

**Pengguna**: Jennifer, Pengurus Wilayah  
**Matlamat**: Membandingkan prestasi di semua kedai

**Pertanyaan Bahasa Semula Jadi**:
> "Bandingkan jualan mengikut kategori untuk semua kedai dalam 6 bulan terakhir"

**Apa yang Berlaku**:
1. Konteks RLS ditetapkan untuk akses pengurus wilayah
2. Pertanyaan kompleks merentas kedai dijana
3. Data diagregatkan di seluruh lokasi kedai
4. Hasil termasuk trend dan perbandingan
5. AI mengenal pasti wawasan dan cadangan

## 🔒 Penyelaman Mendalam Keselamatan dan Pelbagai Penyewa

Pelaksanaan kita mengutamakan keselamatan peringkat perusahaan:

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

Setiap sambungan MCP termasuk:
- **ID Pengurus Kedai**: Pengenal unik untuk konteks RLS
- **Penugasan Peranan**: Kebenaran dan tahap akses
- **Pengurusan Sesi**: Token pengesahan yang selamat
- **Log Audit**: Sejarah akses lengkap

### Perlindungan Data

Lapisan keselamatan berganda:
- **Penyulitan Sambungan**: TLS untuk semua sambungan pangkalan data
- **Pencegahan Suntikan SQL**: Pertanyaan yang diparameterkan sahaja
- **Pengesahan Input**: Pengesahan permintaan yang menyeluruh
- **Pengendalian Ralat**: Tiada data sensitif dalam mesej ralat

## 🎯 Poin Penting

Selepas melengkapkan pengenalan ini, anda seharusnya memahami:

✅ **Nilai MCP**: Bagaimana MCP menghubungkan pembantu AI dan data dunia sebenar  
✅ **Konteks Perniagaan**: Keperluan dan cabaran Zava Retail  
✅ **Gambaran Seni Bina**: Komponen utama dan interaksinya  
✅ **Tumpukan Teknologi**: Alat dan kerangka kerja yang digunakan sepanjang  
✅ **Model Keselamatan**: Akses data pelbagai penyewa dan perlindungan  
✅ **Corak Penggunaan**: Senario pertanyaan dunia sebenar dan aliran kerja  

## 🚀 Langkah Seterusnya

Sedia untuk mendalami lebih lanjut? Teruskan dengan:

**[Makmal 01: Konsep Seni Bina Teras](../01-Architecture/README.md)**

Pelajari tentang corak seni bina pelayan MCP, prinsip reka bentuk pangkalan data, dan pelaksanaan teknikal terperinci yang menggerakkan penyelesaian analitik runcit kita.

## 📚 Sumber Tambahan

### Dokumentasi MCP
- [Spesifikasi MCP](https://modelcontextprotocol.io/docs/) - Dokumentasi rasmi protokol
- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners) - Panduan pembelajaran MCP yang komprehensif
- [Dokumentasi FastMCP](https://github.com/modelcontextprotocol/python-sdk) - Dokumentasi SDK Python

### Integrasi Pangkalan Data
- [Dokumentasi PostgreSQL](https://www.postgresql.org/docs/) - Rujukan lengkap PostgreSQL
- [Panduan pgvector](https://github.com/pgvector/pgvector) - Dokumentasi sambungan vektor
- [Keselamatan Tahap Baris](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Panduan RLS PostgreSQL

### Perkhidmatan Azure
- [Dokumentasi Azure OpenAI](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integrasi perkhidmatan AI
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Perkhidmatan pangkalan data terurus
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Kontainer tanpa pelayan

---

**Penafian**: Ini adalah latihan pembelajaran menggunakan data runcit fiksyen. Sentiasa ikuti dasar tadbir urus data dan keselamatan organisasi anda apabila melaksanakan penyelesaian serupa dalam persekitaran pengeluaran.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.