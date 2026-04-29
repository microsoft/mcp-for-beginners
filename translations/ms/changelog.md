# Changelog: Kurikulum MCP untuk Pemula

Dokumen ini berfungsi sebagai rekod semua perubahan penting yang dibuat pada kurikulum Model Context Protocol (MCP) untuk Pemula. Perubahan didokumentasikan dalam urutan terbalik kronologi (perubahan terbaru dahulu).

## 11 April, 2026

### Pelajaran Baru, Pembetulan Dokumentasi, dan Kemas Kini Kebergantungan

#### Kandungan Kurikulum Baru Ditambah

**Modul 05 - Topik Lanjutan**
- **Pelajaran 5.17: Penalaran Multi-Ejen Berlawanan dengan MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Panduan menyeluruh baru yang merangkumi corak perdebatan berlawanan untuk sistem multi-ejen
  - Rajah arkitektur Mermaid: dua ejen → pelayan MCP berkongsi → transkrip perdebatan → hakim → keputusan
  - Pelayan alat MCP berkongsi (`web_search` + `run_python`) dilaksanakan dalam Python dan TypeScript
  - Arahan sistem bertentangan (UNTUK / MENENTANG / Hakim) dengan keperluan penggunaan alat yang jelas
  - Pengatur perdebatan dalam Python, TypeScript, dan C# yang mengurus pusingan dan penghalaan hujah
  - Penyambungan MCP `ClientSession` untuk pengatur kepada panggilan alat sebenar
  - Jadual kes penggunaan (pengesanan halusinasi, pemodelan ancaman, ulasan reka bentuk API, pengesahan fakta, pemilihan teknologi)
  - Pertimbangan keselamatan: pelaksanaan dalam sandbox, pengesahan panggilan alat, had kadar, log audit
  - Latihan berstruktur dengan tiga senario praktikal (ulasan kod, keputusan arkitektur, pengawalan kandungan)

#### Pembetulan Dokumentasi

**Modul 03 - Memulakan**
- **05-stdio-server/README.md**: Memperbaiki contoh pelayan stdio TypeScript yang tidak lengkap — menambah instansiasi pengangkutan yang hilang (`new StdioServerTransport()`) dan panggilan `server.connect(transport)` untuk memadankan contoh Python dan .NET dalam bahagian yang sama
- **14-sampling/README.md**: Memperbaiki kesilapan taip — membetulkan `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Kemas Kini Kurikulum

**Main README.md**
- Ditambah entri 5.17 (Penalaran Multi-Ejen Berlawanan dengan MCP) ke jadual kurikulum dengan pautan terus ke pelajaran baru

**05-AdvancedTopics/README.md**
- Ditambah baris Pelajaran 5.17 ke jadual pelajaran

**study_guide.md**
- Ditambah topik Penalaran Multi-Ejen Berlawanan ke peta minda dan keterangan prosa Topik Lanjutan

#### Pembetulan Kod dan Keselamatan

**Modul 05 - Ejen Berlawanan (`mcp-adversarial-agents`)**
- **Pembetulan keselamatan — suntikan arahan**: Menggantikan interpolasi shell `execSync` dengan `execFile` + `promisify` dalam alat `run_python` TypeScript, menghapuskan permukaan suntikan arahan (kod yang dikawal LLM kini dihantar sebagai elemen argv literal tanpa penglibatan shell)
- **Penyambungan gelung alat MCP**: Mengemas kini pengatur perdebatan Python untuk menggunakan klien `AsyncAnthropic` (menggantikan `Anthropic` sync yang menghalang), menghantar `ClientSession` langsung ke setiap giliran ejen, mendapatkan definisi alat melalui `session.list_tools()` setiap giliran, dan mengedar blok `tool_use` melalui `session.call_tool()` dalam gelung sehingga model mengeluarkan respons teks akhir

#### Kemas Kini Kebergantungan

- Menaik taraf `hono` ke 4.12.12 di pelbagai pakej (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Menaik taraf `@hono/node-server` dari 1.19.11 ke 1.19.13 dalam pakej TypeScript
- Menaik taraf `cryptography` dari 46.0.5 ke 46.0.7 dalam pakej Python (makmal 3 dan 4 10-StreamliningAIWorkflows)
- Menaik taraf `lodash` dari 4.17.23 ke 4.18.1 dalam pemeriksa 10-StreamliningAIWorkflows

#### Terjemahan

- Penyelarasan terjemahan untuk 48+ bahasa dengan perubahan sumber terkini (kemas kini i18n)

---

## 5 Februari, 2026

### Pengesahan dan Penambahbaikan Navigasi Sepanjang Repositori

#### Kandungan Kurikulum Baru Ditambah

**Modul 03 - Memulakan**
- **12-mcp-hosts/README.md**: Panduan menyeluruh baru untuk menyediakan hos MCP
  - Contoh konfigurasi Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Templat konfigurasi JSON untuk semua hos utama
  - Jadual perbandingan jenis pengangkutan (stdio, SSE/HTTP, WebSocket)
  - Penyelesaian masalah isu sambungan biasa
  - Amalan keselamatan terbaik untuk konfigurasi hos

- **13-mcp-inspector/README.md**: Panduan penyahpepijatan baru untuk MCP Inspector
  - Kaedah pemasangan (npx, npm global, dari sumber)
  - Menyambung ke pelayan melalui stdio dan HTTP/SSE
  - Alat ujian, sumber, dan aliran kerja arahan
  - Integrasi VS Code dengan MCP Inspector
  - Senario penyahpepijatan biasa dengan penyelesaian

**Modul 04 - Pelaksanaan Praktikal**
- **pagination/README.md**: Panduan pelaksanaan pagination baru
  - Corak pagination berasaskan kursor dalam Python, TypeScript, Java
  - Pengendalian pagination sisi klien
  - Strategi reka bentuk kursor (tersembunyi vs struktur)
  - Cadangan pengoptimuman prestasi

**Modul 05 - Topik Lanjutan**
- **mcp-protocol-features/README.md**: Kajian mendalam ciri protokol baru
  - Pelaksanaan notifikasi kemajuan
  - Corak pembatalan permintaan
  - Templat sumber dengan corak URI
  - Pengurusan kitaran hayat pelayan
  - Kawalan tahap log
  - Corak pengendalian ralat dengan kod JSON-RPC

#### Pembetulan Navigasi (24+ fail dikemas kini)

**Modul Utama READMEs**
 Kini pautan ke pelajaran pertama DAN modul seterusnya

**Fail Sub-Sekuriti 02**
- Kesemua 5 dokumen sokongan keselamatan kini mempunyai navigasi "Apa Yang Seterusnya":

**Fail Kajian Kes 09**
- Semua fail kajian kes kini mempunyai navigasi berurutan:

**Makmal 10-StreamliningAI**
Ditambah bahagian Apa Yang Seterusnya ke gambaran keseluruhan Modul 10 dan Modul 11

#### Pembetulan Kod dan Kandungan

**Kemas Kini SDK dan Kebergantungan**
Memperbaiki versi openai kosong ke `^4.95.0`
Mengemas kini SDK dari `^1.8.0` ke `>=1.26.0`
Mengemas kini pin versi mcp ke `>=1.26.0`

**Pembetulan Kod**
Memperbaiki model tidak sah `gpt-4o-mini` ke `gpt-4.1-mini`

**Pembetulan Kandungan**
Memperbaiki pautan rosak `READMEmd` → `README.md`, membetulkan tajuk kurikulum `Module 1-3` → `Module 0-3`, membetulkan laluan bersesuaian huruf
Mengeluarkan kandungan duplikat Kajian Kes 5 yang rosak

**Penambahbaikan Panduan Pemula**
Menambah pengenalan yang betul, objektif pembelajaran, dan prasyarat untuk pemula

#### Kemas Kini Kurikulum

**Main README.md**
- Ditambah entri 3.12 (Hos MCP), 3.13 (Inspektor MCP), 4.1 (Pagination), 5.16 (Ciri Protokol) ke jadual kurikulum

**Modul READMEs**
Ditambah pelajaran 12 dan 13 ke senarai pelajaran
Ditambah seksyen Panduan Praktikal dengan pautan pagination
Ditambah pelajaran 5.15 (Pengangkutan Tersuai) dan 5.16 (Ciri Protokol)

**study_guide.md**
- Dikemas kini peta minda dengan semua topik baru: Penetapan Hos MCP, Inspektor MCP, Strategi Pagination, Kajian Mendalam Ciri Protokol

## 28 Jan, 2026

### Semakan Pematuhan Spesifikasi MCP 2025-11-25

#### Peningkatan Konsep Teras (01-CoreConcepts/)
- **Primitive Klien Baru - Roots**: Menambah dokumentasi menyeluruh mengenai primitive klien Roots, membolehkan pelayan memahami sempadan sistem fail dan kebenaran akses
- **Anotasi Alat**: Menambah dokumentasi pada anotasi tingkah laku alat (`readOnlyHint`, `destructiveHint`) untuk keputusan pelaksanaan alat yang lebih baik
- **Panggilan Alat dalam Sampling**: Mengemas kini dokumentasi Sampling untuk memasukkan parameter `tools` dan `toolChoice` bagi pemanggilan alat dipacu model semasa permintaan sampling
- **Elicitation Mod URL**: Menambah dokumentasi mengenai elicitation berdasarkan URL untuk interaksi web luaran yang dimulakan oleh pelayan
- **Tugas (Eksperimen)**: Menambah bahagian baru yang mendokumentasikan ciri Tugas eksperimen untuk pembalut pelaksanaan tahan lama dan pengambilan hasil tertunda
- **Sokongan Ikon**: Menyatakan bahawa alat, sumber, templat sumber, dan arahan kini boleh memasukkan ikon sebagai metadata tambahan

#### Kemas Kini Dokumentasi
- **README.md**: Ditambah rujukan versi Spesifikasi MCP 2025-11-25 dan penjelasan versi berdasarkan tarikh
- **study_guide.md**: Dikemas kini peta kurikulum untuk memasukkan Tugas dan Anotasi Alat dalam bahagian Konsep Teras; dikemas kini cap masa dokumen

#### Pengesahan Pematuhan Spesifikasi
- **Versi Protokol**: Mengesahkan semua dokumentasi merujuk Spesifikasi MCP 2025-11-25 terkini
- **Penjajaran Arkitektur**: Mengesahkan ketepatan dokumentasi arkitektur dua lapisan (Lapisan Data + Lapisan Pengangkutan)
- **Dokumentasi Primitives**: Mengesahkan primitives pelayan (Sumber, Arahan, Alat) dan primitives klien (Sampling, Elicitation, Logging, Roots)
- **Mekanisme Pengangkutan**: Mengesahkan ketepatan dokumentasi pengangkutan STDIO dan HTTP Boleh-Aliran
- **Panduan Keselamatan**: Mengesahkan penjajaran dengan dokumentasi Amalan Terbaik Keselamatan MCP terkini

#### Ciri Utama MCP 2025-11-25 Didokumentasikan
- **Penemuan OpenID Connect**: Penemuan pelayan pengesahan melalui OIDC
- **Dokumen Metadata ID Klien OAuth**: Mekanisme pendaftaran klien yang disyorkan
- **JSON Schema 2020-12**: Dialek lalai untuk definisi skema MCP
- **Sistem Tahap SDK**: Keperluan formal untuk sokongan ciri dan penyelenggaraan SDK
- **Struktur Tadbir Urus**: Pengelasan formal Kumpulan Kerja dan Kumpulan Minat dalam tadbir urus MCP

### Kemas Kini Dokumentasi Keselamatan Utama (02-Security/)

#### Integrasi Bengkel Kemuncak Keselamatan MCP (Sherpa)
- **Sumber Latihan Amali Baru**: Menambah integrasi menyeluruh dengan [Bengkel Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/) dalam semua dokumentasi keselamatan
- **Liputan Laluan Ekspedisi**: Mendokumentasikan kemajuan lengkap kem dari Base Camp hingga Summit
- **Penjajaran OWASP**: Semua panduan keselamatan kini dipetakan kepada risiko Buku Panduan Keselamatan Azure MCP OWASP

#### Integrasi OWASP MCP Top 10
- **Bahagian Baru**: Menambah jadual Risiko Keselamatan OWASP MCP Top 10 dengan mitigasi Azure ke README Keselamatan utama
- **Dokumentasi Berdasarkan Risiko**: Mengemas kini mcp-security-controls-2025.md dengan rujukan risiko OWASP MCP untuk setiap domain keselamatan
- **Arkitektur Rujukan**: Memaut kepada arkitektur rujukan dan corak pelaksanaan Buku Panduan Keselamatan Azure OWASP MCP

#### Fail Keselamatan Dikemas Kini
- **README.md**: Menambah gambaran bengkel Sherpa, jadual laluan ekspedisi, ringkasan risiko OWASP MCP Top 10, dan seksyen latihan amali
- **mcp-security-controls-2025.md**: Dikemas kini tajuk ke Februari 2026, menambah rujukan risiko OWASP (MCP01-MCP08), membetulkan ketidakkonsistenan versi spesifikasi
- **mcp-security-best-practices-2025.md**: Menambah seksyen sumber Sherpa dan OWASP, dikemas kini cap masa
- **mcp-best-practices.md**: Menambah seksyen latihan amali dengan pautan Sherpa dan OWASP
- **azure-content-safety-implementation.md**: Menambah rujukan OWASP MCP06, penjajaran Kem 3 Sherpa, dan seksyen sumber tambahan

#### Pautan Sumber Baru Ditambah
- [Bengkel Kemuncak Keselamatan MCP (Sherpa)](https://azure-samples.github.io/sherpa/)
- [Buku Panduan Keselamatan Azure OWASP MCP](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Halaman risiko OWASP MCP individu (MCP01-MCP10)

### Penjajaran Spesifikasi MCP 2025-11-25 Sepanjang Kurikulum

#### Modul 03 - Memulakan
- **Dokumentasi SDK**: Menambah Go SDK ke senarai SDK rasmi; mengemas kini semua rujukan SDK agar selari dengan Spesifikasi MCP 2025-11-25
- **Penjelasan Pengangkutan**: Mengemas kini penerangan pengangkutan STDIO dan Streaming HTTP dengan rujukan spesifikasi yang jelas

#### Modul 04 - Pelaksanaan Praktikal
- **Kemas Kini SDK**: Menambah Go SDK; mengemas kini senarai SDK dengan rujukan versi spesifikasi
- **Spesifikasi Kebenaran**: Mengemas kini pautan spesifikasi Authorisasi MCP ke versi terkini 2025-11-25

#### Modul 05 - Topik Lanjutan
- **Ciri Baru**: Menambah nota mengenai ciri Spesifikasi MCP 2025-11-25 baru (Tugas, Anotasi Alat, Elicitation Mod URL, Roots)
- **Sumber Keselamatan**: Menambah pautan OWASP MCP Top 10 dan bengkel Sherpa kepada rujukan tambahan

#### Modul 06 - Sumbangan Komuniti
- **Senarai SDK**: Menambah Swift dan Rust SDK; mengemas kini pautan spesifikasi ke 2025-11-25
- **Rujukan Spesifikasi**: Mengemas kini pautan Spesifikasi MCP ke URL spesifikasi langsung

#### Modul 07 - Pengajaran dari Penggunaan Awal
- **Kemas Kini Sumber**: Menambah pautan Spesifikasi MCP 2025-11-25 dan OWASP MCP Top 10 ke sumber tambahan

#### Modul 08 - Amalan Terbaik
- **Versi Spesifikasi**: Mengemas kini rujukan Spesifikasi MCP ke 2025-11-25
- **Sumber Keselamatan**: Menambah OWASP MCP Top 10 dan bengkel Sherpa ke rujukan tambahan

#### Modul 10 - Memperkemas Aliran Kerja AI
- **Kemas Kini Lencana**: Menukar lencana versi MCP dari versi SDK (1.9.3) ke versi spesifikasi (2025-11-25)
- **Pautan Sumber**: Mengemas kini pautan Spesifikasi MCP; menambah OWASP MCP Top 10

#### Modul 11 - Makmal Amali MCP Server
- **Rujukan Spesifikasi**: Mengemas kini pautan Spesifikasi MCP ke versi 2025-11-25
- **Sumber Keselamatan**: Menambah OWASP MCP Top 10 ke sumber rasmi

## 18 Disember, 2025
### Kemas Kini Dokumentasi Keselamatan - Spesifikasi MCP 2025-11-25

#### Amalan Terbaik Keselamatan MCP (02-Security/mcp-best-practices.md) - Kemas Kini Versi Spesifikasi
- **Kemas Kini Versi Protokol**: Dikemaskini untuk merujuk Spesifikasi MCP terbaru 2025-11-25 (dikeluarkan 25 November 2025)
  - Dikemaskini semua rujukan versi spesifikasi dari 2025-06-18 ke 2025-11-25
  - Dikemaskini rujukan tarikh dokumen dari 18 Ogos 2025 ke 18 Disember 2025
  - Disahkan semua URL spesifikasi menunjuk kepada dokumentasi terkini
- **Pengesahan Kandungan**: Pengesahan menyeluruh terhadap amalan terbaik keselamatan mengikut piawaian terkini
  - **Penyelesaian Keselamatan Microsoft**: Disahkan istilah dan pautan semasa untuk Prompt Shields (sebelumnya "Pengesanan risiko Jailbreak"), Azure Content Safety, Microsoft Entra ID, dan Azure Key Vault
  - **Keselamatan OAuth 2.1**: Disahkan kesesuaian dengan amalan keselamatan OAuth terkini
  - **Piawaian OWASP**: Dilengkapi pengesahan rujukan OWASP Top 10 untuk LLMs masih terkini
  - **Perkhidmatan Azure**: Disahkan semua pautan dokumentasi Microsoft Azure dan amalan terbaik
- **Pematuhan Piawaian**: Semua piawaian keselamatan yang dirujuk disahkan masih terkini
  - Kerangka Pengurusan Risiko AI NIST
  - ISO 27001:2022
  - Amalan Terbaik Keselamatan OAuth 2.1
  - Kerangka keselamatan dan pematuhan Azure
- **Sumber Pelaksanaan**: Disahkan semua pautan panduan pelaksanaan dan sumber
  - Corak pengesahan Azure API Management
  - Panduan integrasi Microsoft Entra ID
  - Pengurusan rahsia Azure Key Vault
  - Saluran DevSecOps dan penyelesaian pemantauan

### Jaminan Kualiti Dokumentasi
- **Pematuhan Spesifikasi**: Memastikan semua keperluan keselamatan MCP wajib (MESTI/MESTI TIDAK) sejajar dengan spesifikasi terkini
- **Kemas Kini Sumber**: Disahkan semua pautan luaran ke dokumentasi Microsoft, piawaian keselamatan, dan panduan pelaksanaan
- **Liputan Amalan Terbaik**: Disahkan liputan menyeluruh berkaitan pengesahan, kebenaran, ancaman khusus AI, keselamatan rantaian bekalan, dan corak perusahaan

## 6 Oktober 2025

### Perluasan Seksyen Memulakan – Penggunaan Pelayan Lanjutan & Pengesahan Mudah

#### Penggunaan Pelayan Lanjutan (03-GettingStarted/10-advanced)
- **Bab Baru Ditambah**: Memperkenalkan panduan menyeluruh penggunaan pelayan MCP lanjutan, merangkumi seni bina pelayan biasa dan tahap rendah.
  - **Pelayan Biasa vs Tahap Rendah**: Perbandingan terperinci dan contoh kod dalam Python dan TypeScript untuk kedua-dua pendekatan.
  - **Reka Bentuk Berasaskan Pengendali**: Penjelasan pengurusan alat/sumber/prompt berasaskan pengendali untuk pelaksanaan pelayan berskala dan fleksibel.
  - **Corak Praktikal**: Senario dunia sebenar di mana corak pelayan tahap rendah bermanfaat untuk ciri dan seni bina lanjutan.

#### Pengesahan Mudah (03-GettingStarted/11-simple-auth)
- **Bab Baru Ditambah**: Panduan langkah demi langkah melaksanakan pengesahan mudah dalam pelayan MCP.
  - **Konsep Auth**: Penjelasan jelas antara pengesahan vs kebenaran, dan pengurusan kelayakan.
  - **Pelaksanaan Auth Asas**: Corak pengesahan berasaskan middleware dalam Python (Starlette) dan TypeScript (Express), dengan contoh kod.
  - **Perkembangan ke Keselamatan Lanjutan**: Panduan memulakan dengan pengesahan mudah dan beralih ke OAuth 2.1 dan RBAC, dengan rujukan modul keselamatan lanjutan.

Penambahan ini menyediakan panduan praktikal dan langsung untuk membina pelaksanaan pelayan MCP yang lebih kukuh, selamat, dan fleksibel, menghubungkan konsep asas dengan corak pengeluaran lanjutan.

## 29 September 2025

### Makmal Integrasi Pangkalan Data MCP Server - Jalur Pembelajaran Amali Menyeluruh

#### 11-MCPServerHandsOnLabs - Kurikulum Lengkap Integrasi Pangkalan Data Baru
- **Jalur Pembelajaran 13 Makmal Lengkap**: Ditambah kurikulum amali menyeluruh untuk membina pelayan MCP sedia pengeluaran dengan integrasi pangkalan data PostgreSQL
  - **Pelaksanaan Dunia Sebenar**: Kes penggunaan analitik Zava Retail yang mempamerkan corak setaraf perusahaan
  - **Progresi Pembelajaran Berstruktur**:
    - **Makmal 00-03: Asas** - Pengenalan, Seni Bina Teras, Keselamatan & Multi-Tenancy, Penyediaan Persekitaran
    - **Makmal 04-06: Membina Pelayan MCP** - Reka Bentuk & Skema Pangkalan Data, Pelaksanaan Pelayan MCP, Pembangunan Alat  
    - **Makmal 07-09: Ciri Lanjutan** - Integrasi Carian Semantik, Ujian & Debug, Integrasi VS Code
    - **Makmal 10-12: Pengeluaran & Amalan Terbaik** - Strategi Pengeluaran, Pemantauan & Kebolehamatan, Amalan Terbaik & Pengoptimuman
  - **Teknologi Perusahaan**: Rangka kerja FastMCP, PostgreSQL dengan pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Ciri Lanjutan**: Keselamatan Tahap Baris (RLS), carian semantik, akses data pelbagai penyewa, penyerapan vektor, pemantauan waktu nyata

#### Penyeragaman Terminologi - Penukaran Modul ke Makmal
- **Kemas Kini Dokumentasi Menyeluruh**: Kemas kini sistematik semua fail README dalam 11-MCPServerHandsOnLabs menggunakan istilah "Makmal" menggantikan "Modul"
  - **Tajuk Seksyen**: Dikemaskini dari "Apa Yang Dibahaskan Modul Ini" ke "Apa Yang Dibahaskan Makmal Ini" di kesemua 13 makmal
  - **Penerangan Kandungan**: Diubah "Modul ini menyediakan..." ke "Makmal ini menyediakan..." di seluruh dokumentasi
  - **Objektif Pembelajaran**: Dikemaskini "Menjelang akhir modul ini..." ke "Menjelang akhir makmal ini..."
  - **Pautan Navigasi**: Ditukar semua rujukan "Modul XX:" ke "Makmal XX:" dalam silang rujukan dan navigasi
  - **Penjejakan Penyelesaian**: Dikemaskini "Selepas menyiapkan modul ini..." ke "Selepas menyiapkan makmal ini..."
  - **Rujukan Teknikal Dipelihara**: Mengekalkan rujukan modul Python dalam fail konfigurasi (contoh, `"module": "mcp_server.main"`)

#### Peningkatan Panduan Kajian (study_guide.md)
- **Peta Kurikulum Visual**: Ditambah bahagian baru "11. Makmal Integrasi Pangkalan Data" dengan visualisasi struktur makmal menyeluruh
- **Struktur Repositori**: Dikemaskini dari sepuluh kepada sebelas seksyen utama dengan penerangan terperinci 11-MCPServerHandsOnLabs
- **Panduan Laluan Pembelajaran**: Ditingkatkan arahan navigasi untuk meliputi seksyen 00-11
- **Liputan Teknologi**: Ditambah perincian integrasi FastMCP, PostgreSQL, dan perkhidmatan Azure
- **Hasil Pembelajaran**: Ditekankan pembangunan pelayan sedia pengeluaran, corak integrasi pangkalan data, dan keselamatan perusahaan

#### Peningkatan Struktur README Utama
- **Terminologi Berasaskan Makmal**: Dikemaskini README.md utama di 11-MCPServerHandsOnLabs untuk menggunakan struktur "Makmal" secara konsisten
- **Organisasi Laluan Pembelajaran**: Progresi jelas dari konsep asas melalui pelaksanaan lanjutan ke pengeluaran
- **Fokus Dunia Sebenar**: Penekanan pada pembelajaran praktikal dengan corak dan teknologi setaraf perusahaan

### Peningkatan Kualiti & Konsistensi Dokumentasi
- **Penekanan Pembelajaran Amali**: Memperkuat pendekatan berasaskan makmal di seluruh dokumentasi
- **Fokus Corak Perusahaan**: Mengutamakan pelaksanaan sedia pengeluaran dan pertimbangan keselamatan perusahaan
- **Integrasi Teknologi**: Liputan menyeluruh perkhidmatan Azure moden dan corak integrasi AI
- **Progresi Pembelajaran**: Laluan terstruktur dan jelas dari konsep asas ke pengeluaran

## 26 September 2025

### Peningkatan Kajian Kes - Integrasi Daftar MCP GitHub

#### Kajian Kes (09-CaseStudy/) - Fokus Pembangunan Ekosistem
- **README.md**: Perluasan utama dengan kajian kes Daftar MCP GitHub secara menyeluruh
  - **Kajian Kes Daftar MCP GitHub**: Kajian kes baru menyeluruh meneliti pelancaran Daftar MCP GitHub pada September 2025
    - **Analisis Masalah**: Pemeriksaan terperinci cabaran penemuan dan penempatan pelayan MCP yang terpecah-pecah
    - **Reka Bentuk Penyelesaian**: Pendekatan daftar berpusat oleh GitHub dengan pemasangan VS Code satu klik
    - **Impak Perniagaan**: Penambahbaikan nyata dalam penerimaan dan produktiviti pembangun
    - **Nilai Strategik**: Fokus pada penempatan agen modular dan interoperabiliti merentasi alat
    - **Pembangunan Ekosistem**: Penempatan sebagai platform asas untuk integrasi agen
  - **Struktur Kajian Kes Dipertingkatkan**: Dikemaskini semua tujuh kajian kes dengan format konsisten dan keterangan menyeluruh
    - Agen Perjalanan AI Azure: Penekanan orkestrasi multi-agen
    - Integrasi Azure DevOps: Fokus automasi aliran kerja
    - Pengambilan Dokumentasi Masa Nyata: Pelaksanaan klien konsol Python
    - Penjana Pelan Kajian Interaktif: Aplikasi web perbualan Chainlit
    - Dokumentasi Dalam Editor: Integrasi VS Code dan GitHub Copilot
    - Azure API Management: Corak integrasi API perusahaan
    - Daftar MCP GitHub: Pembangunan ekosistem dan platform komuniti
  - **Kesimpulan Menyeluruh**: Bahagian kesimpulan ditulis semula menyorot tujuh kajian kes merangkumi pelbagai dimensi pelaksanaan MCP
    - Integrasi Perusahaan, Orkestrasi Multi-Agen, Produktiviti Pembangun
    - Pembangunan Ekosistem, Kategori Aplikasi Pendidikan
    - Insight lanjutan tentang corak seni bina, strategi pelaksanaan, dan amalan terbaik
    - Penekanan MCP sebagai protokol matang dan sedia pengeluaran

#### Kemas Kini Panduan Kajian (study_guide.md)
- **Peta Kurikulum Visual**: Dikemaskini mindmap untuk memasukkan Daftar MCP GitHub dalam seksyen Kajian Kes
- **Penerangan Kajian Kes**: Ditingkatkan dari penerangan umum ke perincian tujuh kajian kes menyeluruh
- **Struktur Repositori**: Dikemaskini seksyen 10 mencerminkan liputan kajian kes komprehensif dengan butiran pelaksanaan khusus
- **Integrasi Penukaran Perubahan**: Ditambah entri 26 September 2025 mendokumentasikan penambahan Daftar MCP GitHub dan peningkatan kajian kes
- **Kemas Kini Tarikh**: Dikemaskini cap waktu kaki untuk mencerminkan semakan terkini (26 September 2025)

### Peningkatan Kualiti Dokumentasi
- **Penyeragaman Format**: Menyeragamkan format dan struktur kajian kes di ketujuh-tujuh contoh
- **Liputan Menyeluruh**: Kajian kes merangkumi perusahaan, produktiviti pembangun, dan senario pembangunan ekosistem
- **Penempatan Strategik**: Fokus dipertingkatkan pada MCP sebagai platform asas untuk penempatan sistem agen
- **Integrasi Sumber**: Dikemaskini sumber tambahan dengan pautan Daftar MCP GitHub

## 15 September 2025

### Perluasan Topik Lanjutan - Penghantaran Tersuai & Kejuruteraan Konteks

#### Penghantaran Tersuai MCP (05-AdvancedTopics/mcp-transport/) - Panduan Pelaksanaan Lanjutan Baru
- **README.md**: Panduan pelaksanaan lengkap untuk mekanisme penghantaran MCP tersuai
  - **Penghantaran Azure Event Grid**: Pelaksanaan penghantaran tanpa pelayan berasaskan acara menyeluruh
    - Contoh C#, TypeScript, dan Python dengan integrasi Azure Functions
    - Corak seni bina berasaskan acara untuk penyelesaian MCP berskala
    - Penerima webhook dan pengendalian mesej berasaskan push
  - **Penghantaran Azure Event Hubs**: Pelaksanaan penghantaran aliran data berkapasiti tinggi
    - Keupayaan penstriman waktu nyata untuk senario latensi rendah
    - Strategi pembahagian partisi dan pengurusan titik semakan
    - Pengumpulan mesej dan pengoptimuman prestasi
  - **Corak Integrasi Perusahaan**: Contoh seni bina sedia pengeluaran
    - Pemprosesan MCP diedarkan merentasi beberapa Azure Functions
    - Seni bina penghantaran hibrid menggabungkan pelbagai jenis penghantaran
    - Ketahanan mesej, kebolehpercayaan, dan strategi pengendalian ralat
  - **Keselamatan & Pemantauan**: Integrasi Azure Key Vault dan corak kebolehamatan
    - Pengesahan identiti terkawal dan akses paling minima
    - Telemetri Application Insights dan pemantauan prestasi
    - Pemutus litar dan corak ketahanan kegagalan
  - **Rangka Kerja Ujian**: Strategi ujian menyeluruh untuk penghantaran tersuai
    - Ujian unit dengan test doubles dan rangka kerja mock
    - Ujian integrasi dengan Azure Test Containers
    - Pertimbangan ujian prestasi dan beban

#### Kejuruteraan Konteks (05-AdvancedTopics/mcp-contextengineering/) - Disiplin AI Berkembang
- **README.md**: Eksplorasi menyeluruh kejuruteraan konteks sebagai bidang baru
  - **Prinsip Teras**: Perkongsian konteks lengkap, kesedaran keputusan tindakan, dan pengurusan tingkap konteks
  - **Penyelarasan Protokol MCP**: Cara reka bentuk MCP menangani cabaran kejuruteraan konteks
    - Had tingkap konteks dan strategi pemuatan progresif
    - Penentuan kaitan dan pengambilan konteks dinamik
    - Pengendalian konteks pelbagai modaliti dan pertimbangan keselamatan
  - **Pendekatan Pelaksanaan**: Seni bina berasaskan satu utas vs multi-agen
    - Teknik penghirisan dan keutamaan konteks
    - Pemuatan progresif dan strategi pemampatan konteks
    - Pendekatan berlapis konteks dan pengoptimuman pengambilan
  - **Rangka Kerja Pengukuran**: Metrik muncul untuk penilaian keberkesanan konteks
    - Kecekapan input, prestasi, kualiti, dan pertimbangan pengalaman pengguna
    - Pendekatan eksperimen untuk pengoptimuman konteks
    - Analisis kegagalan dan metodologi peningkatan

#### Kemas Kini Navigasi Kurikulum (README.md)
- **Struktur Modul Ditingkatkan**: Jadual kurikulum dikemaskini untuk memasukkan topik lanjutan baru
  - Ditambah entri Kejuruteraan Konteks (5.14) dan Penghantaran Tersuai (5.15)
  - Format dan pautan navigasi konsisten merentasi semua modul
  - Penerangan dikemaskini mencerminkan skop kandungan terkini

### Penambahbaikan Struktur Direktori
- **Penyeragaman Penamaan**: "mcp transport" dinamakan semula kepada "mcp-transport" selaras dengan folder topik lanjutan lain
- **Pengorganisasian Kandungan**: Semua folder 05-AdvancedTopics kini mengikuti corak penamaan konsisten (mcp-[topic])

### Penambahbaikan Kualiti Dokumentasi
- **Penyelarasan Spesifikasi MCP**: Semua kandungan baru merujuk Spesifikasi MCP terkini 2025-06-18
- **Contoh Pelbagai Bahasa**: Contoh kod menyeluruh dalam C#, TypeScript, dan Python
- **Fokus Perusahaan**: Corak sedia pengeluaran dan integrasi awan Azure sepanjang masa
- **Dokumentasi Visual**: Carta Mermaid untuk seni bina dan visualisasi aliran

## 18 Ogos 2025

### Kemas Kini Komprehensif Dokumentasi - Piawaian MCP 2025-06-18

#### Amalan Terbaik Keselamatan MCP (02-Security/) - Pemodenan Lengkap
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Penulisan semula lengkap selaras dengan Spesifikasi MCP 2025-06-18  
  - **Keperluan Mandatori**: Ditambah keperluan MUST/MUST NOT yang eksplisit daripada spesifikasi rasmi dengan penunjuk visual yang jelas  
  - **12 Amalan Teras Keselamatan**: Disusun semula daripada senarai 15 item kepada domain keselamatan yang menyeluruh  
    - Keselamatan Token & Pengesahan dengan integrasi pembekal identiti luaran  
    - Pengurusan Sesi & Keselamatan Pengangkutan dengan keperluan kriptografi  
    - Perlindungan Ancaman Khusus AI dengan integrasi Microsoft Prompt Shields  
    - Kawalan Akses & Kebenaran dengan prinsip hak terendah  
    - Keselamatan Kandungan & Pemantauan dengan integrasi Azure Content Safety  
    - Keselamatan Rantaian Bekalan dengan pengesahan komponen menyeluruh  
    - Keselamatan OAuth & Pencegahan Confused Deputy dengan pelaksanaan PKCE  
    - Respons Insiden & Pemulihan dengan keupayaan automatik  
    - Pematuhan & Tadbir Urus dengan penjajaran peraturan  
    - Kawalan Keselamatan Lanjutan dengan seni bina zero trust  
    - Integrasi Ekosistem Keselamatan Microsoft dengan solusi menyeluruh  
    - Evolusi Keselamatan Berterusan dengan amalan adaptif  
  - **Penyelesaian Keselamatan Microsoft**: Panduan integrasi dipertingkatkan untuk Prompt Shields, Azure Content Safety, Entra ID, dan GitHub Advanced Security  
  - **Sumber Pelaksanaan**: Pautan sumber menyeluruh dikategorikan mengikut Dokumentasi Rasmi MCP, Penyelesaian Keselamatan Microsoft, Standard Keselamatan, dan Panduan Pelaksanaan  

#### Kawalan Keselamatan Lanjutan (02-Security/) - Pelaksanaan Perusahaan  
- **MCP-SECURITY-CONTROLS-2025.md**: Penstrukturan semula lengkap dengan rangka kerja keselamatan setaraf perusahaan  
  - **9 Domain Keselamatan Menyeluruh**: Dikembangkan daripada kawalan asas kepada rangka kerja perusahaan terperinci  
    - Pengesahan & Pemberi Kuasa Lanjutan dengan integrasi Microsoft Entra ID  
    - Keselamatan Token & Kawalan Anti-Passthrough dengan pengesahan menyeluruh  
    - Kawalan Keselamatan Sesi dengan pencegahan perampasan  
    - Kawalan Keselamatan Khusus AI dengan pencegahan suntikan prompt dan keracunan alat  
    - Pencegahan Serangan Confused Deputy dengan keselamatan proksi OAuth  
    - Keselamatan Pelaksanaan Alat dengan sandboxing dan pengasingan  
    - Kawalan Keselamatan Rantaian Bekalan dengan pengesahan kebergantungan  
    - Kawalan Pemantauan & Pengesanan dengan integrasi SIEM  
    - Respons Insiden & Pemulihan dengan keupayaan automatik  
  - **Contoh Pelaksanaan**: Ditambah blok konfigurasi YAML terperinci dan contoh kod  
  - **Integrasi Penyelesaian Microsoft**: Liputan menyeluruh perkhidmatan keselamatan Azure, GitHub Advanced Security, dan pengurusan identiti perusahaan  

#### Topik Lanjutan Keselamatan (05-AdvancedTopics/mcp-security/) - Pelaksanaan Sedia Produksi  
- **README.md**: Penulisan semula lengkap untuk pelaksanaan keselamatan perusahaan  
  - **Penjajaran Spesifikasi Semasa**: Dikemas kini mengikut Spesifikasi MCP 2025-06-18 dengan keperluan keselamatan mandatori  
  - **Pengesahan Dipertingkat**: Integrasi Microsoft Entra ID dengan contoh menyeluruh .NET dan Java Spring Security  
  - **Integrasi Keselamatan AI**: Pelaksanaan Microsoft Prompt Shields dan Azure Content Safety dengan contoh terperinci Python  
  - **Mitigasi Ancaman Lanjutan**: Contoh pelaksanaan menyeluruh untuk  
    - Pencegahan Serangan Confused Deputy dengan PKCE dan pengesahan keizinan pengguna  
    - Pencegahan Token Passthrough dengan pengesahan audien dan pengurusan token selamat  
    - Pencegahan Perampasan Sesi dengan pengikatan kriptografi dan analisis tingkah laku  
  - **Integrasi Keselamatan Perusahaan**: Pemantauan Azure Application Insights, saluran pengesanan ancaman, dan keselamatan rantaian bekalan  
  - **Senarai Semak Pelaksanaan**: Kawalan keselamatan mandatori vs disyorkan dengan manfaat ekosistem keselamatan Microsoft  

### Kualiti Dokumentasi & Penjajaran Standard  
- **Rujukan Spesifikasi**: Dikemas kini semua rujukan ke Spesifikasi MCP 2025-06-18 terkini  
- **Ekosistem Keselamatan Microsoft**: Panduan integrasi dipertingkat di seluruh dokumentasi keselamatan  
- **Pelaksanaan Praktikal**: Ditambah contoh kod terperinci dalam .NET, Java, dan Python dengan corak perusahaan  
- **Pengurusan Sumber**: Pengkategorian menyeluruh dokumentasi rasmi, standard keselamatan, dan panduan pelaksanaan  
- **Penunjuk Visual**: Penandaan jelas keperluan mandatori vs amalan disyorkan  

#### Konsep Teras (01-CoreConcepts/) - Pemodenan Lengkap  
- **Kemas Kini Versi Protokol**: Dikemaskini untuk merujuk Spesifikasi MCP 2025-06-18 dengan versi berasaskan tarikh (format YYYY-MM-DD)  
- **Penambahbaikan Seni Bina**: Penerangan dipertingkat mengenai Hos, Klien, dan Pelayan untuk mencerminkan corak seni bina MCP semasa  
  - Hos kini ditakrifkan dengan jelas sebagai aplikasi AI yang menyelaras pelbagai sambungan klien MCP  
  - Klien diterangkan sebagai penyambung protokol yang mengekalkan hubungan satu-ke-satu dengan pelayan  
  - Pelayan dipertingkat dengan senario pelaksanaan tempatan vs jauh  
- **Penstrukturan Semula Primitif**: Penstrukturan semula lengkap primitif pelayan dan klien  
  - Primitif Pelayan: Sumber (punca data), Prompt (templat), Alat (fungsi boleh laksana) dengan penjelasan dan contoh terperinci  
  - Primitif Klien: Pensampelan (penyempurnaan LLM), Elicitation (input pengguna), Logging (debugging/pemantauan)  
  - Dikemaskini dengan corak kaedah penemuan (`*/list`), pengambilan (`*/get`), dan pelaksanaan (`*/call`) semasa  
- **Seni Bina Protokol**: Memperkenalkan model seni bina dua lapisan  
  - Lapisan Data: Asas JSON-RPC 2.0 dengan pengurusan kitaran hayat dan primitif  
  - Lapisan Pengangkutan: STDIO (tempatan) dan HTTP Boleh Alir dengan SSE (jauh) mekanisme pengangkutan  
- **Rangka Kerja Keselamatan**: Prinsip keselamatan menyeluruh termasuk keizinan pengguna eksplisit, perlindungan privasi data, keselamatan pelaksanaan alat, dan keselamatan lapisan pengangkutan  
- **Corak Komunikasi**: Dikemaskini mesej protokol untuk menunjukkan inisialisasi, penemuan, pelaksanaan, dan aliran pemberitahuan  
- **Contoh Kod**: Contoh pelbagai bahasa (.NET, Java, Python, JavaScript) dikemaskini mencerminkan corak SDK MCP semasa  

#### Keselamatan (02-Security/) - Penstrukturan Semula Keselamatan Menyeluruh  
- **Penjajaran Standard**: Penjajaran penuh dengan keperluan keselamatan Spesifikasi MCP 2025-06-18  
- **Evolusi Pengesahan**: Didokumentasikan evolusi daripada pelayan OAuth khusus ke delegasi pembekal identiti luaran (Microsoft Entra ID)  
- **Analisis Ancaman Khusus AI**: Liputan dipertingkat vektor serangan AI moden  
  - Senario serangan suntikan prompt terperinci dengan contoh dunia sebenar  
  - Mekanisme keracunan alat dan corak serangan "rug pull"  
  - Keracunan tingkap konteks dan serangan kekeliruan model  
- **Penyelesaian Keselamatan AI Microsoft**: Liputan menyeluruh ekosistem keselamatan Microsoft  
  - AI Prompt Shields dengan pengesanan maju, spotlighting, dan teknik delimiter  
  - Corak integrasi Azure Content Safety  
  - GitHub Advanced Security untuk perlindungan rantaian bekalan  
- **Mitigasi Ancaman Lanjutan**: Kawalan keselamatan terperinci untuk  
  - Perampasan sesi dengan senario serangan khusus MCP dan keperluan ID sesi kriptografi  
  - Masalah confused deputy dalam senario proksi MCP dengan keperluan keizinan eksplisit  
  - Kelemahan passthrough token dengan kawalan pengesahan mandatori  
- **Keselamatan Rantaian Bekalan**: Liputan diperluas rantaian bekalan AI termasuk model asas, perkhidmatan embedding, penyedia konteks, dan API pihak ketiga  
- **Keselamatan Asas**: Integrasi dipertingkat dengan corak keselamatan perusahaan termasuk seni bina zero trust dan ekosistem keselamatan Microsoft  
- **Pengurusan Sumber**: Pautan sumber menyeluruh dikategorikan mengikut jenis (Dokumen Rasmi, Standard, Penyelidikan, Penyelesaian Microsoft, Panduan Pelaksanaan)  

### Penambahbaikan Kualiti Dokumentasi  
- **Objektif Pembelajaran Berstruktur**: Objektif pembelajaran dipertingkat dengan hasil khusus dan boleh dilaksanakan  
- **Rujukan Silang**: Ditambah pautan antara topik keselamatan dan konsep teras yang berkaitan  
- **Maklumat Terkini**: Dikemas kini semua rujukan tarikh dan pautan spesifikasi kepada standard terkini  
- **Panduan Pelaksanaan**: Ditambah panduan pelaksanaan spesifik dan boleh dilaksanakan di kedua-dua bahagian  

## 16 Julai 2025  

### README dan Penambahbaikan Navigasi  
- Reka bentuk semula sepenuhnya navigasi kurikulum dalam README.md  
- Menggantikan tag `<details>` dengan format berasaskan jadual yang lebih mudah diakses  
- Mewujudkan pilihan susun atur alternatif dalam folder baru "alternative_layouts"  
- Ditambah contoh navigasi berasaskan kad, bergaya tab, dan bergaya akordion  
- Dikemaskini bahagian struktur repositori untuk memasukkan semua fail terkini  
- Dipertingkatkan bahagian "Cara Menggunakan Kurikulum Ini" dengan cadangan jelas  
- Dikemaskini pautan spesifikasi MCP kepada URL yang betul  
- Ditambah seksyen Kejuruteraan Konteks (5.14) ke struktur kurikulum  

### Kemaskini Panduan Kajian  
- Disemak sepenuhnya panduan kajian untuk menyerasikan dengan struktur repositori semasa  
- Ditambah seksyen baru untuk Klien MCP dan Alat, serta Pelayan MCP Popular  
- Dikemaskini Peta Kurikulum Visual untuk mencerminkan semua topik dengan tepat  
- Dipertingkatkan keterangan Topik Lanjutan untuk merangkumi semua bidang khusus  
- Dikemaskini bahagian Kajian Kes untuk mencerminkan contoh sebenar  
- Ditambah log perubahan komprehensif ini  

### Sumbangan Komuniti (06-CommunityContributions/)  
- Ditambah maklumat terperinci mengenai pelayan MCP untuk penjanaan imej  
- Ditambah seksyen menyeluruh mengenai menggunakan Claude dalam VSCode  
- Ditambah arahan penetapan dan penggunaan klien terminal Cline  
- Dikemaskini bahagian klien MCP untuk memasukkan semua pilihan klien popular  
- Dipertingkatkan contoh sumbangan dengan sampel kod lebih tepat  

### Topik Lanjutan (05-AdvancedTopics/)  
- Mengatur semua folder topik khusus dengan penamaan konsisten  
- Ditambah bahan dan contoh kejuruteraan konteks  
- Ditambah dokumentasi integrasi ejen Foundry  
- Dipertingkatkan dokumentasi integrasi keselamatan Entra ID  

## 11 Jun 2025  

### Penciptaan Awal  
- Melancarkan versi pertama kurikulum MCP untuk Pemula  
- Mewujudkan struktur asas untuk semua 10 bahagian utama  
- Melaksanakan Peta Kurikulum Visual untuk navigasi  
- Ditambah projek contoh awal dalam pelbagai bahasa pengaturcaraan  

### Memulakan (03-GettingStarted/)  
- Membuat contoh pelaksanaan pelayan pertama  
- Menambah panduan pembangunan klien  
- Menyertakan arahan integrasi klien LLM  
- Ditambah dokumentasi integrasi VS Code  
- Melaksanakan contoh pelayan Server-Sent Events (SSE)  

### Konsep Teras (01-CoreConcepts/)  
- Ditambah penerangan terperinci mengenai seni bina klien-pelayan  
- Mewujudkan dokumentasi mengenai komponen utama protokol  
- Mendokumentasikan corak mesej dalam MCP  

## 23 Mei 2025  

### Struktur Repositori  
- Memulakan repositori dengan struktur folder asas  
- Membuat fail README bagi setiap bahagian utama  
- Menyiapkan infrastruktur penterjemahan  
- Menambah aset imej dan diagram  

### Dokumentasi  
- Membuat README.md awal dengan gambaran keseluruhan kurikulum  
- Menambah CODE_OF_CONDUCT.md dan SECURITY.md  
- Menyiapkan SUPPORT.md dengan panduan mendapatkan bantuan  
- Membuat struktur panduan kajian awal  

## 15 April 2025  

### Perancangan dan Rangka Kerja  
- Perancangan awal untuk kurikulum MCP untuk Pemula  
- Menetapkan objektif pembelajaran dan khalayak sasaran  
- Merangka struktur 10 bahagian kurikulum  
- Membangunkan rangka kerja konseptual untuk contoh dan kajian kes  
- Membuat prototaip contoh awal untuk konsep utama

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->