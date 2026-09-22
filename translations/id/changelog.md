# Catatan Perubahan: Kurikulum MCP untuk Pemula

Dokumen ini berfungsi sebagai catatan semua perubahan signifikan yang dibuat pada kurikulum Model Context Protocol (MCP) untuk Pemula. Perubahan didokumentasikan dalam urutan kronologis terbalik (perubahan terbaru dahulu).

## 9 September 2026

### Penyesuaian Spesifikasi Akhir MCP 2026-07-28

Memperbarui kurikulum Bahasa Inggris dari panduan baseline rilis-kandidat dan `2025-11-25`
ke spesifikasi MCP akhir `2026-07-28`.

- **Diperbarui**: Referensi versi saat ini, tautan spesifikasi, panduan permintaan tanpa status,
  `server/discover`, header HTTP Streamable, dan siklus hidup ekstensi Tugas
  di 38 berkas dokumentasi Bahasa Inggris.
- **Diperbaiki**: Elicitation sekarang menggunakan `elicitation/create`, Sampling menggunakan
  `sampling/createMessage`, dan `InputRequiredResult.resultType` menggunakan
  `"input_required"`.
- **Diganti**: Pelajaran status percakapan Root Context yang tidak akurat diganti dengan
  pelajaran Roots yang akurat protokol yang mencakup petunjuk sistem berkas informasional,
  alur multi-perjalanan saat ini, batas keamanan, dan opsi migrasi.
- **Diperjelas**: Roots, Sampling, Logging, dan Dynamic Client Registration sudah
  usang di `2026-07-28`, dengan pengganti yang direkomendasikan dan tanggal penghapusan
  paling awal yang didokumentasikan.
- **Diberi Label**: Sampel yang masih bergantung pada MCP `2025-11-25`, HTTP+SSE,
  handshake inisialisasi, atau sesi protokol disimpan sebagai contoh kompatibilitas
  warisan daripada disajikan sebagai implementasi saat ini.
- **Panduan keamanan**: Memperbarui panduan keamanan mandiri untuk menggunakan
  otorisasi per permintaan dan pegangan status aplikasi eksplisit alih-alih
  ID sesi protokol yang dihapus. Dokumen Metadata Client ID sekarang menjadi
  jalur pendaftaran yang disukai, dengan DCR didokumentasikan hanya sebagai kompatibilitas.
- **Materi pendukung**: Memperbarui panduan belajar, daftar periksa kontributor,
  studi kasus Publora, dan studi kasus APIM. Panduan APIM sekarang merekomendasikan
  titik akhir HTTP Streamable `/mcp` saat ini alih-alih `/sse` yang sudah usang.
- **Tautan kanonik**: Mengganti URL spesifikasi yang sudah pensiun dan draf di
  sumber Markdown Bahasa Inggris dengan tautan versi `2026-07-28`, sambil mempertahankan
  tautan eksplisit ke versi warisan di mana sampel tetap terkait dengan alat lama.
- **Nama berkas stabil**: Mengganti nama panduan spesifikasi akhir dan dua panduan keamanan
  untuk menghapus akhiran rilis-kandidat dan tahun, kemudian memperbarui semua
  hyperlink Bahasa Inggris ke jalur stabil mereka.
- **Sampel otorisasi baru**: Menambahkan
  [server sumber daya MCP TypeScript `2026-07-28`](./02-Security/samples/cimd-dcr-auth/README.md)
  yang diuji yang membandingkan Dokumen Metadata Client ID yang disukai dengan fallback
  Dynamic Client Registration yang sudah usang. Sampel ini mencakup penemuan RFC 9728, pemeriksaan JWKS,
  ruang lingkup per alat, dua belas pengujian, dan panduan penyiapan Auth0.
- **Ruang lingkup terjemahan**: Hanya berkas sumber Bahasa Inggris yang diedit; terjemahan
  yang dihasilkan dan gambar terjemahan tetap tidak berubah karena terjemahan otomatis.

## 29 Juli 2026

### Modul Pendamping Baru 08: Sidecars Keandalan dan Percobaan Ulang Aman

Menambahkan pelajaran pendamping netral vendor untuk alat MCP yang menciptakan efek dunia nyata,
yang selaras dengan spesifikasi akhir `2026-07-28`.


- **Baru**: Pelajaran pendamping [reliability sidecar][reliability-sidecar]
  menggunakan satu cerita tiket dukungan, dua diagram Mermaid, dan alur keputusan
  retry untuk menjelaskan kunci operasi stabil, penerimaan duplikat atomik,
  rekonsiliasi, bukti, dan batas ekstensi Tasks.
- **Baru**: Latihan injeksi kegagalan Python dan SQLite pustaka standar
  menggunakan penyimpanan operasi dan tiket terpisah untuk mendemonstrasikan respons yang hilang
  setelah efek eksternal dikomit. Enam tes deterministik mencakup duplikasi naif,
  pemulihan restart yang dijaga, konflik payload, hasil yang di-cache,
  klaim aktif, dan penerimaan duplikat konkuren.
- **Diperbarui**: Modul 08 sekarang menautkan pelajaran pendamping, mengidentifikasi
  model permintaan tanpa status final `2026-07-28`, membedakan observabilitas OpenTelemetry
  dari fitur logging MCP yang kedaluwarsa, dan membatasi contoh retry generiknya
  pada operasi hanya-baca.
- **Opsional**: Pelajaran memetakan konsep portabelnya ke satu implementasi komunitas yang ditandai
  tanpa membuat layanan yang dihosting atau panggilan jaringan menjadi bagian dari
  latihan.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 Juli 2026

### Pelajaran Baru: Kandidat Rilis Spesifikasi MCP 2026-07-28

Menambahkan cakupan kandidat rilis spesifikasi MCP yang akan datang `2026-07-28` (diumumkan 21 Mei 2026; rilis final dijadwalkan 28 Juli 2026), dirangkum dari [postingan blog pengumuman resmi](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Baseline kurikulum tetap **Spesifikasi MCP 2025-11-25** sampai versi baru dirilis, jadi ini disajikan sebagai panduan ke depan bukan sebagai penulisan ulang pelajaran yang ada.

- **Baru**: [01-CoreConcepts/mcp-2026-07-28.md](./01-CoreConcepts/mcp-2026-07-28.md) — pelajaran lengkap yang mencakup inti protokol tanpa status (penghapusan handshake `initialize` dan `Mcp-Session-Id`), header routing baru `Mcp-Method`/`Mcp-Name`, metadata caching `ttlMs`/`cacheScope`, W3C Trace Context dalam `_meta`, kerangka Extensions formal (Aplikasi MCP dan ekstensi Tasks baru), enam SEP penguatan otorisasi, penghapusan Roots/Sampling/Logging, dan perpindahan ke JSON Schema 2020-12 penuh untuk skema alat.
- **Diperbarui** dengan panggilan ke depan yang menautkan ke pelajaran baru:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): catatan versi protokol, bagian Sampling/Roots/Logging/Tasks, dan "Apa selanjutnya"
  - [02-Security/README.md](./02-Security/README.md): panggilan penguatan otorisasi
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): panggilan transport stateless
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): panggilan penghapusan Sampling

  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Peringatan penghentian logging dan panggilan ekstensi Tasks

  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): penjelasan stateless/session-routing
  - [README.md](./README.md): catatan "Melihat ke depan" di bagian spesifikasi dan entri baru `1.1` di tabel modul kurikulum
  - [study_guide.md](./study_guide.md): poin ke depan di bawah tinjauan Konsep Inti dan catatan addendum yang diberi tanggal
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): penjelasan tentang peta transport `mcp-session-id` sebelum model permintaan stateless
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): penjelasan tinjauan modul tentang Depresiasi Root Contexts/Sampling dan ekstensi Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): penjelasan penguatan otorisasi

## 24 Juni 2026

### Pelajaran Baru: Menggunakan MCP di aplikasi Copilot

- [Bagian Tooling](./12-tooling/README.md) Ditambahkan bagian tooling.
- [MCP di aplikasi Copilot](./12-tooling/01-copilot-app/README.md)

## 16 Juni 2026

### Penyesuaian Spesifikasi MCP & Validasi Contoh

Memvalidasi kurikulum terhadap **Spesifikasi MCP 2025-11-25** saat ini dan SDK resmi terbaru, kemudian memperbaiki referensi spesifikasi yang kadaluarsa dan memastikan contoh inti masih dapat dibangun dan dijalankan.

#### Koreksi Versi Spesifikasi (2025-06-18 / 2025-03-26 → 2025-11-25)

Memperbarui konten bahasa Inggris yang masih mengklaim revisi spes lama sebagai standar *saat ini/terbaru*, dan mengarahkan ulang tautan ke jalur spesifikasi kanonik `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Memperbarui banner "Standar Saat Ini", pengantar, heading prinsip keamanan inti, heading persyaratan wajib, bagian Microsoft Entra ID, tautan Referensi & Sumber Daya, dan pemberitahuan keamanan penutup (8 referensi) ke 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Memperbarui tautan spesifikasi Sumber Daya Tambahan dan banner "Standar Saat Ini" ke 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Mengganti tautan keamanan-dan-kepercayaan `2025-03-26` yang usang dengan halaman praktik keamanan terbaik 2025-11-25 saat ini
- **03-GettingStarted/14-sampling/README.md**: Memperbarui tautan dokumen sampel resmi ke 2025-11-25
- **03-GettingStarted/05-stdio-server/README.md**: Memperbarui referensi present tense "spesifikasi MCP saat ini" dan tautan spesifikasi Sumber Daya Tambahan ke 2025-11-25 (catatan historis penghentian SSE tetap utuh untuk akurasi)

#### Validasi Contoh Terhadap SDK Saat Ini

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` berhasil dengan `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` lulus tanpa error tipe — API `McpServer`/`StdioServerTransport` yang ada tetap berlaku
- **Python (03-GettingStarted/01-first-server/solution/python)**: Diverifikasi di `.venv` terisolasi dengan `mcp[cli]` (1.27.2); `py_compile` lulus dan `FastMCP.list_tools()` mengembalikan alat `add` dan `subtract` dengan benar
- Memastikan semua rentang versi contoh `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) menyelesaikan dengan bersih ke `1.29.0` dengan tanpa perubahan API yang merusak

#### Penyesuaian Pin Ketergantungan (menutup celah versi)

Meningkatkan pin SDK yang kadaluarsa sehingga setiap contoh mengikuti rilis MCP saat ini, sesuai konvensi repositori secara keseluruhan:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Meningkatkan `@modelcontextprotocol/sdk` dari `^1.8.0` → `>=1.26.0` dan memperbarui deskripsi paket "ditingkatkan untuk MCP 2025-06-18" yang kadaluarsa menjadi "selaras dengan Spesifikasi MCP 2025-11-25"
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** dan **lab4/code/github_mcp_server/pyproject.toml**: Meningkatkan pin tepat `mcp==1.23.0` → `mcp>=1.26.0`; meregenerasi kedua file `uv.lock` (`uv lock`) sehingga file kunci menyelesaikan ke `mcp 1.27.2` saat ini dan tetap sinkron dengan manifes

#### Analisis Celah Kurikulum — Cakupan Fitur Spesifikasi Terbaru

Memverifikasi kurikulum sudah mencakup semua primitif yang diperkenalkan/diperluas di MCP 2025-11-25, sehingga tidak ada celah konten yang tersisa:
- **Sampling**: Pelajaran 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (termasuk mode URL)**: Didokumentasikan di 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Didokumentasikan di 00-Introduction, 01-CoreConcepts, dan 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimen, operasi jangka panjang)**: Didokumentasikan di 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features
- **Anotasi Alat** (`readOnlyHint` / `destructiveHint`): Didokumentasikan di 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features

### Penguatan Keamanan & Perbaikan Kerentanan Dependency

Melakukan pemeriksaan keamanan menyeluruh pada setiap manifes ketergantungan dan kode sumber contoh, kemudian memperbaiki semua advisori npm yang dilaporkan dan satu temuan tingkat kode. Setelah perbaikan, `npm audit` melaporkan **0 kerentanan** di setiap direktori yang diaudit.

#### Kerentanan Ketergantungan npm (transitif) — Diperbaiki

Mengaudit semua 15 file `package-lock.json` yang dikomit. Kerentanan terbatas pada ketergantungan transitif yang dibawa oleh alat dev MCP Inspector, klien OpenAI, dan MCP SDK; semuanya sekarang terselesaikan tanpa merusak contoh:

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** dan **lab3/code/weather_mcp/inspector**: Meningkatkan `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), yang menghapus advisori yang terbungkus `ajv`, `brace-expansion`, `diff`, `path-to-regexp` dan `ws`. Menambahkan entri `overrides` npm yang memaksa `shell-quote@1.8.4` yang telah diperbaiki untuk menghilangkan advisori kritis yang tersisa yang dibawa oleh `concurrently`; menghasilkan ulang kedua lockfile (sekarang 0 kerentanan)
- **03-GettingStarted/samples/typescript**: `npm audit fix` memperbarui `qs` transitif (sedang) ke rilis yang telah diperbaiki
- **03-GettingStarted/samples/javascript**: `npm audit fix` memperbarui `hono` transitif (sedang) ke rilis yang telah diperbaiki
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` memperbarui `form-data` transitif (tinggi) ke rilis yang telah diperbaiki
- **03-GettingStarted/11-simple-auth/solution/typescript**: Menghasilkan `package-lock.json` yang hilang sehingga proyek dapat direproduksi dan diaudit (0 kerentanan)

#### Perbaikan Keamanan Tingkat Kode (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Menghapus `shell=True` dari alat `open_in_vscode`. `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` sebelumnya memungkinkan metakarakter shell dalam jalur folder diinterpretasikan oleh `cmd.exe` (vektor injeksi perintah). Sekarang meluncurkan `Code.exe` yang sudah diselesaikan secara langsung dengan folder sebagai argumen — tanpa shell — yang secara fungsional setara dan aman

#### Audit Ketergantungan Python

- Mengaudit setiap set persyaratan Python dengan `pip-audit`. `05-AdvancedTopics` dan `03-GettingStarted/samples/python` melaporkan **tidak ada kerentanan yang diketahui** (rentang `mcp` / `httpx` / `pydantic` / `python-dotenv` mereka menyelesaikan ke rilis perbaikan saat ini)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` menandai ketergantungan transitif **`werkzeug` 3.1.1** dengan tiga advisori DoS nama perangkat Windows `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, dan `CVE-2026-27199` (semua diperbaiki di 3.1.6). Menambahkan pin keamanan eksplisit `werkzeug>=3.1.6` sehingga rilis yang diperbaiki dapat diselesaikan; memverifikasi batasan dapat diselesaikan dengan bersih dengan tumpukan `chainlit` / `mcp` / `semantic-kernel`

### Rebranding Nama Produk

Memperbarui semua konten kurikulum untuk mencerminkan rebranding produk Microsoft:

#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Memperbarui tautan komunitas Discord
- **AGENTS.md**: Memperbarui referensi server Discord
- **README.md**: Memperbarui referensi ekosistem teknologi
- **study_guide.md**: Memperbarui referensi studi kasus
- **05-AdvancedTopics/README.md**: Memperbarui judul dan deskripsi Modul 5.13
- **05-AdvancedTopics/mcp-integration/README.md**: Memperbarui header bagian dan deskripsi
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Pembaruan lengkap judul dan isi modul
- **05-AdvancedTopics/mcp-security-entra/README.md**: Memperbarui tautan referensi silang
- **07-LessonsfromEarlyAdoption/README.md**: Memperbarui referensi studi kasus
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Memperbarui header Bagian 9, lencana, dan kemampuan
- **08-BestPractices/README.md**: Memperbarui tautan komunitas Discord
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Memperbarui referensi saluran Discord
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Memperbarui referensi deployment model
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Memperbarui tabel Layanan AI
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Memperbarui referensi sumber daya

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension untuk VS Code
- **README.md**: Memperbarui referensi kurikulum utama
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Memperbarui judul modul, gambaran umum, dan semua header modul
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Memperbarui judul, tujuan pembelajaran, instruksi pengaturan, dan sumber daya
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Memperbarui judul, tujuan pembelajaran, tabel host MCP, dan referensi silang
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Memperbarui judul, lencana, prasyarat, dan sumber daya
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Memperbarui referensi Agent Builder dan tautan umpan balik
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Memperbarui prasyarat dan referensi ekstensi

---

## 11 April 2026

### Pelajaran Baru, Perbaikan Dokumentasi, dan Pembaruan Ketergantungan

#### Konten Kurikulum Baru Ditambahkan

**Modul 05 - Topik Lanjutan**
- **Pelajaran 5.17: Penalaran Multi-Agen Adversarial dengan MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Panduan komprehensif baru yang membahas pola debat adversarial untuk sistem multi-agen
  - Diagram arsitektur Mermaid: dua agen → server MCP bersama → transkrip debat → hakim → putusan
  - Server alat MCP bersama (`web_search` + `run_python`) diimplementasikan dalam Python dan TypeScript
  - Prompt sistem yang berlawanan (FOR / AGAINST / Hakim) dengan persyaratan penggunaan alat eksplisit
  - Pengatur debat dalam Python, TypeScript, dan C# yang mengelola putaran dan rute argumen
  - Pengkabelan MCP `ClientSession` untuk pengatur menuju panggilan alat nyata
  - Tabel kasus penggunaan (deteksi halusinasi, pemodelan ancaman, tinjauan desain API, verifikasi faktual, pemilihan teknologi)
  - Pertimbangan keamanan: eksekusi dalam sandbox, validasi panggilan alat, pembatasan laju, pencatatan audit
  - Latihan terstruktur dengan tiga skenario praktis (tinjauan kode, keputusan arsitektur, moderasi konten)

#### Perbaikan Dokumentasi

**Modul 03 - Memulai**
- **05-stdio-server/README.md**: Memperbaiki contoh server stdio TypeScript yang tidak lengkap — menambahkan instansiasi transport yang hilang (`new StdioServerTransport()`) dan panggilan `server.connect(transport)` agar sesuai dengan contoh Python dan .NET di bagian yang sama
- **14-sampling/README.md**: Memperbaiki typo — mengoreksi `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Pembaruan Kurikulum

**README.md Utama**
- Menambahkan entri 5.17 (Penalaran Multi-Agen Adversarial dengan MCP) ke tabel kurikulum dengan tautan langsung ke pelajaran baru

**05-AdvancedTopics/README.md**
- Menambahkan baris Pelajaran 5.17 ke tabel pelajaran

**study_guide.md**
- Menambahkan topik Penalaran Multi-Agen Adversarial ke peta pikiran dan deskripsi prosa dari Topik Lanjutan

#### Perbaikan Kode dan Keamanan

**Modul 05 - Agen Adversarial (`mcp-adversarial-agents`)**
- **Perbaikan keamanan — injeksi perintah**: Mengganti interpolasi shell `execSync` dengan `execFile` + `promisify` dalam alat TypeScript `run_python`, menghilangkan permukaan injeksi perintah (kode yang dikontrol LLM sekarang diteruskan sebagai elemen argv literal tanpa keterlibatan shell)
- **Pengkabelan loop alat MCP**: Memperbarui pengatur debat Python untuk menggunakan klien `AsyncAnthropic` (menggantikan `Anthropic` sinkron yang memblokir), meneruskan `ClientSession` langsung yang aktif ke setiap giliran agen, mengambil definisi alat melalui `session.list_tools()` setiap giliran, dan mengirim blok `tool_use` melalui `session.call_tool()` dalam loop sampai model mengeluarkan respons teks akhir

#### Pembaruan Ketergantungan

- Meningkatkan `hono` ke 4.12.12 di berbagai paket (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Meningkatkan `@hono/node-server` dari 1.19.11 ke 1.19.13 di paket TypeScript
- Meningkatkan `cryptography` dari 46.0.5 ke 46.0.7 di paket Python (lab 3 dan 4 di 10-StreamliningAIWorkflows)
- Meningkatkan `lodash` dari 4.17.23 ke 4.18.1 di inspector 10-StreamliningAIWorkflows

#### Terjemahan

- Menyinkronkan terjemahan untuk lebih dari 48 bahasa dengan perubahan sumber terbaru (pembaruan i18n)

---

## 5 Februari 2026

### Validasi dan Peningkatan Navigasi Seluruh Repositori

#### Konten Kurikulum Baru Ditambahkan

**Modul 03 - Memulai**
- **12-mcp-hosts/README.md**: Panduan komprehensif baru untuk mengatur host MCP
  - Contoh konfigurasi Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Template konfigurasi JSON untuk semua host utama
  - Tabel perbandingan jenis transport (stdio, SSE/HTTP, WebSocket)
  - Pemecahan masalah masalah koneksi umum
  - Praktik keamanan terbaik untuk konfigurasi host

- **13-mcp-inspector/README.md**: Panduan debugging baru untuk MCP Inspector
  - Metode instalasi (npx, npm global, dari sumber)
  - Menghubungkan ke server melalui stdio dan HTTP/SSE
  - Alat pengujian, sumber daya, dan alur kerja prompt
  - Integrasi VS Code dengan MCP Inspector
  - Skenario debugging umum dengan solusi

**Modul 04 - Implementasi Praktis**
- **pagination/README.md**: Panduan implementasi pagination baru
  - Pola pagination berbasis cursor dalam Python, TypeScript, Java
  - Penanganan pagination sisi klien
  - Strategi desain cursor (opaque vs. structured)
  - Rekomendasi optimisasi performa

**Modul 05 - Topik Lanjutan**
- **mcp-protocol-features/README.md**: Pendalaman fitur protokol baru
  - Implementasi notifikasi kemajuan
  - Pola pembatalan permintaan
  - Template sumber daya dengan pola URI
  - Manajemen siklus hidup server
  - Kontrol level logging
  - Pola penanganan kesalahan dengan kode JSON-RPC

#### Perbaikan Navigasi (24+ file diperbarui)

**README Modul Utama**
 Sekarang menautkan ke pelajaran pertama DAN modul berikutnya

**Sub-file Keamanan 02**
- Kelima dokumen keamanan tambahan kini memiliki navigasi "Apa Selanjutnya":

**File Studi Kasus 09**
- Semua file studi kasus kini memiliki navigasi berurutan:

**Lab 10-StreamliningAI**
Menambahkan bagian Apa Selanjutnya ke gambaran Modul 10 dan Modul 11

#### Perbaikan Kode dan Konten

**Pembaruan SDK dan Ketergantungan**
Memperbaiki versi openai kosong menjadi `^4.95.0`
Memperbarui SDK dari `^1.8.0` ke `>=1.26.0`
Memperbarui pin versi mcp ke `>=1.26.0`

**Perbaikan Kode**
Memperbaiki model tidak valid `gpt-4o-mini` menjadi `gpt-4.1-mini`

**Perbaikan Konten**
Memperbaiki tautan rusak `READMEmd` → `README.md`, memperbaiki header kurikulum `Module 1-3` → `Module 0-3`, memperbaiki jalur sensitif huruf besar-kecil
Menghapus konten duplikat Studi Kasus 5 yang rusak

**Peningkatan Panduan Pemula**
Menambahkan pengantar yang tepat, tujuan pembelajaran, dan prasyarat untuk pemula

#### Pembaruan Kurikulum

**README.md Utama**
- Menambahkan entri 3.12 (Host MCP), 3.13 (MCP Inspector), 4.1 (Pagination), 5.16 (Fitur Protokol) ke tabel kurikulum

**README Modul**
Menambahkan pelajaran 12 dan 13 ke daftar pelajaran
Menambahkan bagian Panduan Praktis dengan tautan pagination
Menambahkan pelajaran 5.15 (Transport Kustom) dan 5.16 (Fitur Protokol)

**study_guide.md**
- Memperbarui peta pikiran dengan semua topik baru: Pengaturan Host MCP, MCP Inspector, Strategi Pagination, Pendalaman Fitur Protokol

## 28 Jan 2026

### Tinjauan Kepatuhan MCP Spesifikasi 2025-11-25

#### Peningkatan Konsep Inti (01-CoreConcepts/)
- **Primitive Klien Baru - Roots**: Menambahkan dokumentasi komprehensif tentang primitive klien Roots, memungkinkan server memahami batasan sistem file dan izin akses
- **Anotasi Alat**: Menambahkan dokumentasi tentang anotasi perilaku alat (`readOnlyHint`, `destructiveHint`) untuk keputusan eksekusi alat yang lebih baik
- **Pemanggilan Alat dalam Sampling**: Memperbarui dokumentasi Sampling untuk mencakup parameter `tools` dan `toolChoice` untuk pemanggilan alat yang dikendalikan model selama permintaan sampling
- **Pemetaan Mode URL**: Menambahkan dokumentasi tentang pemetaan berbasis URL untuk interaksi web eksternal yang diinisiasi server
- **Tugas (Eksperimental)**: Menambahkan bagian baru yang mendokumentasikan fitur Tugas eksperimental untuk wrapper eksekusi tahan lama dan pengambilan hasil tertunda

- **Dukungan Ikon**: Diketahui bahwa alat, sumber daya, template sumber daya, dan prompt sekarang dapat menyertakan ikon sebagai metadata tambahan

#### Pembaruan Dokumentasi
- **README.md**: Ditambahkan referensi versi Spesifikasi MCP 2025-11-25 dan penjelasan versioning berbasis tanggal
- **study_guide.md**: Diperbarui peta kurikulum untuk memasukkan Tugas dan Anotasi Alat di bagian Konsep Inti; diperbarui cap waktu dokumen

#### Verifikasi Kepatuhan Spesifikasi
- **Versi Protokol**: Diverifikasi semua dokumentasi merujuk pada Spesifikasi MCP 2025-11-25 terbaru
- **Keselarasan Arsitektur**: Dikonfirmasi akurasi dokumentasi arsitektur dua lapis (Lapisan Data + Lapisan Transportasi)
- **Dokumentasi Primitif**: Divalidasi primitif server (Sumber Daya, Prompt, Alat) dan primitif klien (Sampling, Elicitation, Logging, Roots)
- **Mekanisme Transportasi**: Diverifikasi keakuratan dokumentasi transportasi STDIO dan HTTP Streaming
- **Panduan Keamanan**: Dikonfirmasi kesesuaian dengan dokumentasi Praktik Terbaik Keamanan MCP terbaru

#### Fitur Utama MCP 2025-11-25 yang Didokumentasikan
- **Penemuan OpenID Connect**: Penemuan server otentikasi melalui OIDC
- **Dokumen Metadata Client ID OAuth**: Mekanisme pendaftaran klien yang direkomendasikan
- **JSON Schema 2020-12**: Dialek default untuk definisi skema MCP
- **Sistem Tingkatan SDK**: Persyaratan formal untuk dukungan fitur dan pemeliharaan SDK
- **Struktur Pemerintahan**: Kelompok Kerja dan Kelompok Minat yang diformalkan dalam tata kelola MCP

### Pembaruan Besar Dokumentasi Keamanan (02-Security/)

#### Integrasi MCP Security Summit Workshop (Sherpa)
- **Sumber Daya Pelatihan Praktis Baru**: Ditambahkan integrasi komprehensif dengan [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) di seluruh dokumentasi keamanan
- **Cakupan Rute Ekspedisi**: Didokumentasikan progresi lengkap dari Base Camp ke Summit
- **Kesesuaian OWASP**: Semua panduan keamanan kini sesuai dengan risiko pada OWASP MCP Azure Security Guide

#### Integrasi OWASP MCP Top 10
- **Bagian Baru**: Ditambahkan tabel Risiko Keamanan OWASP MCP Top 10 dengan mitigasi Azure ke README utama Keamanan
- **Dokumentasi Berbasis Risiko**: Diperbarui mcp-security-controls-2025.md dengan referensi risiko OWASP MCP untuk setiap domain keamanan
- **Arsitektur Referensi**: Ditautkan ke arsitektur referensi dan pola implementasi OWASP MCP Azure Security Guide

#### Berkas Keamanan yang Diperbarui
- **README.md**: Ditambahkan ikhtisar Sherpa Workshop, tabel rute ekspedisi, ringkasan risiko OWASP MCP Top 10, dan bagian pelatihan praktis
- **mcp-security-controls-2025.md**: Diperbarui header ke Februari 2026, ditambahkan referensi risiko OWASP (MCP01-MCP08), diperbaiki inkonsistensi versi spesifikasi
- **mcp-security-best-practices-2025.md**: Ditambahkan bagian sumber daya Sherpa dan OWASP, diperbarui cap waktu
- **mcp-best-practices.md**: Ditambahkan bagian pelatihan praktis dengan tautan Sherpa dan OWASP
- **azure-content-safety-implementation.md**: Ditambahkan referensi OWASP MCP06, keselarasan Sherpa Camp 3, dan bagian sumber daya tambahan

#### Tautan Sumber Daya Baru Ditambahkan
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Halaman risiko OWASP MCP individual (MCP01-MCP10)

### Keselarasan Spesifikasi MCP 2025-11-25 di Seluruh Kurikulum

#### Modul 03 - Memulai
- **Dokumentasi SDK**: Ditambahkan Go SDK ke daftar SDK resmi; diperbarui semua referensi SDK untuk selaras dengan Spesifikasi MCP 2025-11-25
- **Klarifikasi Transportasi**: Deskripsi transportasi STDIO dan HTTP Streaming diperbarui dengan referensi spesifikasi eksplisit

#### Modul 04 - Implementasi Praktis
- **Pembaruan SDK**: Ditambahkan Go SDK; daftar SDK diperbarui dengan referensi versi spesifikasi
- **Spesifikasi Otorisasi**: Tautan spesifikasi Otorisasi MCP diperbarui ke versi 2025-11-25 saat ini

#### Modul 05 - Topik Lanjutan
- **Fitur Baru**: Ditambahkan catatan tentang fitur baru Spesifikasi MCP 2025-11-25 (Tugas, Anotasi Alat, URL Mode Elicitation, Roots)
- **Sumber Daya Keamanan**: Ditambahkan tautan OWASP MCP Top 10 dan workshop Sherpa ke referensi tambahan

#### Modul 06 - Kontribusi Komunitas
- **Daftar SDK**: Ditambahkan Swift dan Rust SDK; tautan spesifikasi diperbarui ke 2025-11-25
- **Referensi Spesifikasi**: Tautan Spesifikasi MCP diperbarui ke URL spesifikasi langsung

#### Modul 07 - Pelajaran dari Adopsi Awal
- **Pembaruan Sumber Daya**: Ditambahkan tautan Spesifikasi MCP 2025-11-25 dan OWASP MCP Top 10 ke sumber daya tambahan

#### Modul 08 - Praktik Terbaik
- **Versi Spesifikasi**: Referensi Spesifikasi MCP diperbarui ke 2025-11-25
- **Sumber Daya Keamanan**: Ditambahkan OWASP MCP Top 10 dan workshop Sherpa ke referensi tambahan

#### Modul 10 - Menyederhanakan Alur Kerja AI
- **Pembaruan Lencana**: Mengubah lencana versi MCP dari versi SDK (1.9.3) ke versi spesifikasi (2025-11-25)
- **Tautan Sumber Daya**: Diperbarui tautan Spesifikasi MCP; ditambahkan OWASP MCP Top 10

#### Modul 11 - Lab Praktek MCP Server
- **Referensi Spesifikasi**: Tautan Spesifikasi MCP diperbarui ke versi 2025-11-25
- **Sumber Daya Keamanan**: Ditambahkan OWASP MCP Top 10 ke sumber daya resmi

## 18 Desember 2025

### Pembaruan Dokumentasi Keamanan - Spesifikasi MCP 2025-11-25

#### Praktik Terbaik Keamanan MCP (02-Security/mcp-best-practices.md) - Pembaruan Versi Spesifikasi
- **Pembaruan Versi Protokol**: Diperbarui untuk merujuk Spesifikasi MCP 2025-11-25 terbaru (rilis 25 November 2025)
  - Memperbarui semua referensi versi spesifikasi dari 2025-06-18 ke 2025-11-25
  - Memperbarui referensi tanggal dokumen dari 18 Agustus 2025 ke 18 Desember 2025
  - Memverifikasi semua URL spesifikasi menunjuk ke dokumentasi terkini
- **Validasi Konten**: Validasi komprehensif praktik terbaik keamanan terhadap standar terbaru
  - **Solusi Keamanan Microsoft**: Diverifikasi terminologi dan tautan terkini untuk Prompt Shields (sebelumnya "deteksi risiko Jailbreak"), Azure Content Safety, Microsoft Entra ID, dan Azure Key Vault
  - **Keamanan OAuth 2.1**: Dikonfirmasi kesesuaian dengan praktik terbaik keamanan OAuth terbaru
  - **Standar OWASP**: Validasi referensi OWASP Top 10 untuk LLM tetap mutakhir
  - **Layanan Azure**: Diverifikasi semua tautan dokumentasi Microsoft Azure dan praktik terbaik
- **Kesesuaian Standar**: Semua standar keamanan yang direferensikan dikonfirmasi mutakhir
  - Kerangka Manajemen Risiko AI NIST
  - ISO 27001:2022
  - Praktik Terbaik Keamanan OAuth 2.1
  - Kerangka keamanan dan kepatuhan Azure
- **Sumber Daya Implementasi**: Diverifikasi semua tautan dan sumber daya panduan implementasi
  - Pola otentikasi Azure API Management
  - Panduan integrasi Microsoft Entra ID
  - Manajemen rahasia Azure Key Vault
  - Pipeline DevSecOps dan solusi pemantauan

### Jaminan Kualitas Dokumentasi
- **Kepatuhan Spesifikasi**: Memastikan semua persyaratan keamanan wajib MCP (HARUS/TIDAK HARUS) sesuai dengan spesifikasi terbaru
- **Keterkinian Sumber Daya**: Memverifikasi semua tautan eksternal ke dokumentasi Microsoft, standar keamanan, dan panduan implementasi
- **Cakupan Praktik Terbaik**: Mengonfirmasi cakupan komprehensif autentikasi, otorisasi, ancaman spesifik AI, keamanan rantai pasokan, dan pola perusahaan

## 6 Oktober 2025

### Perluasan Bagian Memulai – Penggunaan Server Lanjutan & Autentikasi Sederhana

#### Penggunaan Server Lanjutan (03-GettingStarted/10-advanced)
- **Bab Baru Ditambahkan**: Memperkenalkan panduan komprehensif penggunaan server MCP lanjutan, mencakup arsitektur server reguler dan tingkat rendah.
  - **Server Reguler vs Tingkat Rendah**: Perbandingan rinci dan contoh kode dalam Python dan TypeScript untuk kedua pendekatan.
  - **Desain Berbasis Handler**: Penjelasan tentang pengelolaan alat/sumber daya/prompt berbasis handler untuk implementasi server yang skalabel dan fleksibel.
  - **Pola Praktis**: Skenario dunia nyata dimana pola server tingkat rendah bermanfaat untuk fitur dan arsitektur lanjutan.

#### Autentikasi Sederhana (03-GettingStarted/11-simple-auth)
- **Bab Baru Ditambahkan**: Panduan langkah demi langkah untuk mengimplementasikan autentikasi sederhana di server MCP.
  - **Konsep Auth**: Penjelasan jelas antara autentikasi vs otorisasi, dan penanganan kredensial.
  - **Implementasi Auth Dasar**: Pola autentikasi berbasis middleware dalam Python (Starlette) dan TypeScript (Express), dengan contoh kode.
  - **Progresi ke Keamanan Lanjutan**: Panduan memulai dengan autentikasi sederhana dan beralih ke OAuth 2.1 dan RBAC, dengan referensi ke modul keamanan lanjutan.

Penambahan ini menyediakan panduan praktis dan langsung untuk membangun implementasi server MCP yang lebih tangguh, aman, dan fleksibel, menjembatani konsep dasar dengan pola produksi tingkat lanjut.

## 29 September 2025

### Lab Integrasi Database MCP Server - Jalur Pembelajaran Praktis Komprehensif

#### 11-MCPServerHandsOnLabs - Kurikulum Lengkap Integrasi Database Baru
- **Jalur Pembelajaran 13-Lab Lengkap**: Menambahkan kurikulum praktis komprehensif untuk membangun server MCP siap produksi dengan integrasi database PostgreSQL
  - **Implementasi Dunia Nyata**: Studi kasus analitik Zava Retail yang menunjukkan pola kelas perusahaan
  - **Progresi Pembelajaran Terstruktur**:
    - **Lab 00-03: Fondasi** - Pengantar, Arsitektur Inti, Keamanan & Multi-Tenancy, Pengaturan Lingkungan
    - **Lab 04-06: Membangun Server MCP** - Desain & Skema Database, Implementasi Server MCP, Pengembangan Alat  
    - **Lab 07-09: Fitur Lanjutan** - Integrasi Pencarian Semantik, Pengujian & Debugging, Integrasi VS Code
    - **Lab 10-12: Produksi & Praktik Terbaik** - Strategi Penyebaran, Pemantauan & Observabilitas, Praktik Terbaik & Optimisasi
  - **Teknologi Perusahaan**: Kerangka FastMCP, PostgreSQL dengan pgvector, embedding Azure OpenAI, Azure Container Apps, Application Insights
  - **Fitur Lanjutan**: Row Level Security (RLS), pencarian semantik, akses data multi-tenant, embedding vektor, pemantauan real-time

#### Standarisasi Terminologi - Konversi Modul ke Lab
- **Pembaruan Dokumentasi Komprehensif**: Sistematis memperbarui semua file README di 11-MCPServerHandsOnLabs untuk menggunakan terminologi "Lab" menggantikan "Modul"
  - **Header Bagian**: Memperbarui "Apa yang Dicakup Modul Ini" menjadi "Apa yang Dicakup Lab Ini" di semua 13 lab
  - **Deskripsi Konten**: Mengubah "Modul ini menyediakan..." menjadi "Lab ini menyediakan..." di seluruh dokumentasi
  - **Tujuan Pembelajaran**: Memperbarui "Pada akhir modul ini..." menjadi "Pada akhir lab ini..." 
  - **Tautan Navigasi**: Mengonversi semua referensi "Modul XX:" menjadi "Lab XX:" dalam referensi silang dan navigasi
  - **Pelacakan Penyelesaian**: Memperbarui "Setelah menyelesaikan modul ini..." menjadi "Setelah menyelesaikan lab ini..."
  - **Referensi Teknis Dipertahankan**: Mempertahankan referensi modul Python dalam file konfigurasi (misal, `"module": "mcp_server.main"`)

#### Peningkatan Panduan Studi (study_guide.md)
- **Peta Kurikulum Visual**: Ditambahkan bagian baru "11. Database Integration Labs" dengan visualisasi struktur lab yang komprehensif
- **Struktur Repositori**: Diperbarui dari sepuluh menjadi sebelas bagian utama dengan deskripsi detail 11-MCPServerHandsOnLabs
- **Panduan Jalur Pembelajaran**: Ditingkatkan instruksi navigasi untuk mencakup bagian 00-11
- **Cakupan Teknologi**: Ditambahkan FastMCP, PostgreSQL, rincian integrasi layanan Azure
- **Hasil Pembelajaran**: Menekankan pengembangan server siap produksi, pola integrasi database, dan keamanan kelas perusahaan

#### Peningkatan Struktur README Utama
- **Terminologi Berbasis Lab**: Memperbarui README.md utama di 11-MCPServerHandsOnLabs untuk menggunakan struktur "Lab" secara konsisten
- **Organisasi Jalur Pembelajaran**: Progresi jelas dari konsep dasar melalui implementasi lanjutan hingga penyebaran produksi
- **Fokus Dunia Nyata**: Penekanan pada pembelajaran praktis dengan pola dan teknologi kelas perusahaan

### Peningkatan Kualitas & Konsistensi Dokumentasi
- **Penekanan Pembelajaran Praktis**: Memperkuat pendekatan berbasis lab secara menyeluruh dalam dokumentasi
- **Fokus Pola Perusahaan**: Menyoroti implementasi siap produksi dan pertimbangan keamanan perusahaan
- **Integrasi Teknologi**: Cakupan komprehensif layanan Azure modern dan pola integrasi AI
- **Progresi Pembelajaran**: Jalur terstruktur yang jelas dari konsep dasar hingga penyebaran produksi

## 26 September 2025

### Peningkatan Studi Kasus - Integrasi Registri MCP GitHub

#### Studi Kasus (09-CaseStudy/) - Fokus Pengembangan Ekosistem
- **README.md**: Perluasan besar dengan studi kasus lengkap registri MCP GitHub
  - **Studi Kasus Registri MCP GitHub**: Studi kasus komprehensif baru yang meneliti peluncuran Registri MCP GitHub pada September 2025
    - **Analisis Masalah**: Pemeriksaan detail tentang fragmentasi penemuan dan tantangan penyebaran server MCP
    - **Arsitektur Solusi**: Pendekatan registri terpusat GitHub dengan instalasi VS Code satu klik
    - **Dampak Bisnis**: Peningkatan terukur dalam onboarding dan produktivitas pengembang
    - **Nilai Strategis**: Fokus pada penyebaran agen modular dan interoperabilitas lintas alat
    - **Pengembangan Ekosistem**: Posisi sebagai platform dasar untuk integrasi agen
  - **Struktur Studi Kasus Ditingkatkan**: Memperbarui semua tujuh studi kasus dengan format yang konsisten dan deskripsi komprehensif
    - Agen Perjalanan AI Azure: Penekanan orkestrasi multi-agen
    - Integrasi Azure DevOps: Fokus automasi alur kerja
    - Pengambilan Dokumentasi Real-Time: Implementasi klien konsol Python
    - Generator Rencana Studi Interaktif: Aplikasi web percakapan Chainlit

    - Dokumentasi Dalam Editor: Integrasi VS Code dan GitHub Copilot
    - Manajemen API Azure: Pola integrasi API perusahaan
    - Registri GitHub MCP: Pengembangan ekosistem dan platform komunitas
  - **Kesimpulan Komprehensif**: Bagian kesimpulan yang ditulis ulang menyoroti tujuh studi kasus yang mencakup berbagai dimensi implementasi MCP
    - Integrasi Perusahaan, Orkestrasi Multi-Agen, Produktivitas Pengembang
    - Pengembangan Ekosistem, Kategori Aplikasi Pendidikan
    - Wawasan yang ditingkatkan ke dalam pola arsitektur, strategi implementasi, dan praktik terbaik
    - Penekanan pada MCP sebagai protokol matang dan siap produksi

#### Pembaruan Panduan Studi (study_guide.md)
- **Peta Kurikulum Visual**: Mindmap diperbarui untuk memasukkan Registri GitHub MCP di bagian Studi Kasus
- **Deskripsi Studi Kasus**: Ditingkatkan dari deskripsi umum menjadi rincian tujuh studi kasus komprehensif
- **Struktur Repository**: Bagian 10 diperbarui untuk mencerminkan cakupan studi kasus komprehensif dengan detail implementasi spesifik
- **Integrasi Changelog**: Ditambahkan entri 26 September 2025 yang mendokumentasikan penambahan Registri GitHub MCP dan peningkatan studi kasus
- **Pembaruan Tanggal**: Footer timestamp diperbarui mencerminkan revisi terbaru (26 September 2025)

### Peningkatan Kualitas Dokumentasi
- **Peningkatan Konsistensi**: Standarisasi format dan struktur studi kasus di semua tujuh contoh
- **Cakupan Komprehensif**: Studi kasus sekarang mencakup skenario perusahaan, produktivitas pengembang, dan pengembangan ekosistem
- **Posisi Strategis**: Fokus yang diperkuat pada MCP sebagai platform dasar untuk penerapan sistem agentik
- **Integrasi Sumber Daya**: Sumber daya tambahan diperbarui untuk memasukkan tautan Registri GitHub MCP

## 15 September 2025

### Perluasan Topik Lanjutan - Transportasi Kustom & Rekayasa Konteks

#### Transportasi Kustom MCP (05-AdvancedTopics/mcp-transport/) - Panduan Implementasi Lanjutan Baru
- **README.md**: Panduan lengkap implementasi mekanisme transportasi kustom MCP
  - **Transportasi Azure Event Grid**: Implementasi transportasi event-driven serverless yang komprehensif
    - Contoh C#, TypeScript, dan Python dengan integrasi Azure Functions
    - Pola arsitektur berbasis event untuk solusi MCP yang skalabel
    - Penerima webhook dan penanganan pesan berbasis push
  - **Transportasi Azure Event Hubs**: Implementasi transportasi streaming dengan throughput tinggi
    - Kemampuan streaming real-time untuk skenario latensi rendah
    - Strategi partisi dan manajemen checkpoint
    - Pengelompokan pesan dan optimasi kinerja
  - **Pola Integrasi Perusahaan**: Contoh arsitektur siap produksi
    - Pemrosesan MCP terdistribusi di berbagai Azure Functions
    - Arsitektur transportasi hibrida yang menggabungkan berbagai jenis transportasi
    - Ketahanan pesan, keandalan, dan strategi penanganan error
  - **Keamanan & Pemantauan**: Integrasi Azure Key Vault dan pola observabilitas
    - Autentikasi identitas terkelola dan akses dengan hak minimal
    - Telemetri Application Insights dan pemantauan kinerja
    - Circuit breaker dan pola toleransi kesalahan
  - **Kerangka Pengujian**: Strategi pengujian lengkap untuk transportasi kustom
    - Pengujian unit dengan test doubles dan framework mocking
    - Pengujian integrasi dengan Azure Test Containers
    - Pertimbangan pengujian kinerja dan beban

#### Rekayasa Konteks (05-AdvancedTopics/mcp-contextengineering/) - Disiplin AI yang Muncul
- **README.md**: Eksplorasi komprehensif rekayasa konteks sebagai bidang yang berkembang
  - **Prinsip Inti**: Berbagi konteks penuh, kesadaran pengambilan keputusan aksi, dan pengelolaan jendela konteks
  - **Keselarasan Protokol MCP**: Bagaimana desain MCP mengatasi tantangan rekayasa konteks
    - Batasan jendela konteks dan strategi pemuatan progresif
    - Penentuan relevansi dan pengambilan konteks dinamis
    - Penanganan konteks multimodal dan pertimbangan keamanan
  - **Pendekatan Implementasi**: Arsitektur single-threaded vs. multi-agent
    - Teknik pemecahan dan prioritas konteks
    - Strategi pemuatan progresif dan kompresi konteks
    - Pendekatan konteks berlapis dan optimasi pengambilan
  - **Kerangka Pengukuran**: Metrik yang muncul untuk evaluasi efektivitas konteks
    - Efisiensi input, kinerja, kualitas, dan pertimbangan pengalaman pengguna
    - Pendekatan eksperimental untuk optimasi konteks
    - Analisis kegagalan dan metodologi perbaikan

#### Pembaruan Navigasi Kurikulum (README.md)
- **Struktur Modul yang Ditingkatkan**: Tabel kurikulum diperbarui untuk memasukkan topik lanjutan baru
  - Ditambahkan entri Rekayasa Konteks (5.14) dan Transportasi Kustom (5.15)
  - Format dan tautan navigasi konsisten di semua modul
  - Deskripsi diperbarui untuk mencerminkan cakupan konten saat ini

### Perbaikan Struktur Direktori
- **Standarisasi Penamaan**: Mengganti nama "mcp transport" menjadi "mcp-transport" untuk konsistensi dengan folder topik lanjutan lainnya
- **Organisasi Konten**: Semua folder 05-AdvancedTopics kini mengikuti pola penamaan konsisten (mcp-[topik])

### Peningkatan Kualitas Dokumentasi
- **Keselarasan Spesifikasi MCP**: Semua konten baru merujuk MCP Specification 2025-06-18 saat ini
- **Contoh Multi-Bahasa**: Contoh kode komprehensif dalam C#, TypeScript, dan Python
- **Fokus Perusahaan**: Pola siap produksi dan integrasi cloud Azure secara menyeluruh
- **Dokumentasi Visual**: Diagram Mermaid untuk visualisasi arsitektur dan alur

## 18 Agustus 2025

### Pembaruan Komprehensif Dokumentasi - Standar MCP 2025-06-18

#### Praktik Terbaik Keamanan MCP (02-Security/) - Modernisasi Lengkap
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Penulisan ulang lengkap diselaraskan dengan MCP Specification 2025-06-18
  - **Persyaratan Wajib**: Ditambahkan persyaratan HARUS/TIDAK BOLEH eksplisit dari spesifikasi resmi dengan indikator visual yang jelas
  - **12 Praktik Keamanan Inti**: Direstrukturisasi dari daftar 15 item menjadi domain keamanan komprehensif
    - Keamanan Token & Autentikasi dengan integrasi penyedia identitas eksternal
    - Manajemen Sesi & Keamanan Transportasi dengan kebutuhan kriptografi
    - Perlindungan Ancaman Khusus AI dengan integrasi Microsoft Prompt Shields
    - Kontrol Akses & Izin dengan prinsip hak istimewa minimum
    - Keamanan Konten & Pemantauan dengan integrasi Azure Content Safety
    - Keamanan Rantai Pasokan dengan verifikasi komponen komprehensif
    - Keamanan OAuth & Pencegahan Confused Deputy dengan implementasi PKCE
    - Respons Insiden & Pemulihan dengan kemampuan otomatisasi
    - Kepatuhan & Tata Kelola dengan keselarasan regulasi
    - Kontrol Keamanan Lanjutan dengan arsitektur zero trust
    - Integrasi Ekosistem Keamanan Microsoft dengan solusi komprehensif
    - Evolusi Keamanan Berkelanjutan dengan praktik adaptif
  - **Solusi Keamanan Microsoft**: Panduan integrasi lanjutan untuk Prompt Shields, Azure Content Safety, Entra ID, dan GitHub Advanced Security
  - **Sumber Daya Implementasi**: Kategori tautan sumber daya komprehensif menurut Dokumentasi MCP Resmi, Solusi Keamanan Microsoft, Standar Keamanan, dan Panduan Implementasi

#### Kontrol Keamanan Lanjutan (02-Security/) - Implementasi Perusahaan
- **MCP-SECURITY-CONTROLS-2025.md**: Revisi total dengan kerangka kerja keamanan tingkat perusahaan
  - **9 Domain Keamanan Komprehensif**: Diperluas dari kontrol dasar ke kerangka perusahaan yang rinci
    - Autentikasi & Otorisasi Lanjutan dengan integrasi Microsoft Entra ID
    - Keamanan Token & Kontrol Anti-Passthrough dengan validasi komprehensif
    - Kontrol Keamanan Sesi dengan pencegahan pembajakan
    - Kontrol Keamanan Khusus AI dengan pencegahan injeksi prompt dan racun alat
    - Pencegahan Serangan Confused Deputy dengan keamanan proxy OAuth
    - Keamanan Eksekusi Alat dengan sandboxing dan isolasi
    - Kontrol Keamanan Rantai Pasokan dengan verifikasi ketergantungan
    - Kontrol Pemantauan & Deteksi dengan integrasi SIEM
    - Respons Insiden & Pemulihan dengan kemampuan otomatisasi
  - **Contoh Implementasi**: Ditambahkan blok konfigurasi YAML dan contoh kode rinci
  - **Integrasi Solusi Microsoft**: Cakupan komprehensif layanan keamanan Azure, GitHub Advanced Security, dan manajemen identitas perusahaan

#### Keamanan Topik Lanjutan (05-AdvancedTopics/mcp-security/) - Implementasi Siap Produksi
- **README.md**: Penulisan ulang lengkap untuk implementasi keamanan perusahaan
  - **Keselarasan Spesifikasi Terkini**: Diperbarui ke MCP Specification 2025-06-18 dengan persyaratan keamanan wajib
  - **Autentikasi Ditingkatkan**: Integrasi Microsoft Entra ID dengan contoh lengkap .NET dan Java Spring Security
  - **Integrasi Keamanan AI**: Implementasi Microsoft Prompt Shields dan Azure Content Safety dengan contoh Python rinci
  - **Mitigasi Ancaman Lanjutan**: Contoh implementasi komprehensif untuk
    - Pencegahan Serangan Confused Deputy dengan validasi PKCE dan persetujuan pengguna
    - Pencegahan Passthrough Token dengan validasi audiens dan manajemen token aman
    - Pencegahan Pembajakan Sesi dengan pengikatan kriptografi dan analisis perilaku
  - **Integrasi Keamanan Perusahaan**: Pemantauan Azure Application Insights, pipeline deteksi ancaman, dan keamanan rantai pasokan
  - **Daftar Periksa Implementasi**: Kontrol keamanan wajib vs. yang direkomendasikan dengan manfaat ekosistem keamanan Microsoft

### Kualitas Dokumentasi & Keselarasan Standar
- **Referensi Spesifikasi**: Memperbarui semua referensi ke MCP Specification 2025-06-18 saat ini
- **Ekosistem Keamanan Microsoft**: Panduan integrasi yang diperkuat di seluruh dokumentasi keamanan
- **Implementasi Praktis**: Menambahkan contoh kode rinci dalam .NET, Java, dan Python dengan pola perusahaan
- **Organisasi Sumber Daya**: Klasifikasi komprehensif dokumentasi resmi, standar keamanan, dan panduan implementasi
- **Indikator Visual**: Penandaan jelas persyaratan wajib vs. praktik yang direkomendasikan


#### Konsep Inti (01-CoreConcepts/) - Modernisasi Lengkap
- **Pembaruan Versi Protokol**: Merujuk MCP Specification 2025-06-18 dengan penomoran versi berbasis tanggal (format YYYY-MM-DD)
- **Penyempurnaan Arsitektur**: Deskripsi diperkuat tentang Host, Klien, dan Server yang mencerminkan pola arsitektur MCP saat ini
  - Host kini jelas didefinisikan sebagai aplikasi AI yang mengoordinasi banyak koneksi klien MCP
  - Klien dijelaskan sebagai penghubung protokol yang mempertahankan hubungan satu-ke-satu dengan server
  - Server diperkuat dengan skenario penerapan lokal vs. jarak jauh
- **Restrukturisasi Primitif**: Perombakan total primitif server dan klien
  - Primitif Server: Sumber Daya (sumber data), Prompt (template), Alat (fungsi yang dapat dieksekusi) dengan penjelasan dan contoh rinci
  - Primitif Klien: Sampling (penyelesaian LLM), Elicitation (input pengguna), Logging (debugging/pemantauan)
  - Diperbarui dengan pola metode penemuan (`*/list`), pengambilan (`*/get`), dan eksekusi (`*/call`) saat ini
- **Arsitektur Protokol**: Memperkenalkan model arsitektur dua lapis
  - Lapisan Data: Dasar JSON-RPC 2.0 dengan manajemen siklus hidup dan primitif
  - Lapisan Transportasi: STDIO (lokal) dan HTTP Streamable dengan SSE (jarak jauh) sebagai mekanisme transportasi
- **Kerangka Keamanan**: Prinsip keamanan komprehensif termasuk persetujuan pengguna eksplisit, perlindungan privasi data, keamanan eksekusi alat, dan keamanan lapisan transportasi
- **Pola Komunikasi**: Memperbarui pesan protokol untuk menunjukkan inisialisasi, penemuan, eksekusi, dan alur notifikasi
- **Contoh Kode**: Menyegarkan contoh multi-bahasa (.NET, Java, Python, JavaScript) untuk mencerminkan pola SDK MCP saat ini

#### Keamanan (02-Security/) - Perombakan Keamanan Komprehensif  
- **Keselarasan Standar**: Keselarasan penuh dengan persyaratan keamanan MCP Specification 2025-06-18
- **Evolusi Autentikasi**: Mendokumentasikan evolusi dari server OAuth kustom ke delegasi penyedia identitas eksternal (Microsoft Entra ID)
- **Analisis Ancaman Khusus AI**: Cakupan ditingkatkan dari vektor serangan AI modern
  - Skenario serangan injeksi prompt rinci dengan contoh dunia nyata
  - Mekanisme racun alat dan pola serangan "rug pull"
  - Keracunan jendela konteks dan serangan kebingungan model
- **Solusi Keamanan AI Microsoft**: Cakupan komprehensif ekosistem keamanan Microsoft
  - AI Prompt Shields dengan deteksi lanjutan, spotlighting, dan teknik delimiter
  - Pola integrasi Azure Content Safety
  - GitHub Advanced Security untuk perlindungan rantai pasokan
- **Mitigasi Ancaman Lanjutan**: Kontrol keamanan rinci untuk
  - Pembajakan sesi dengan skenario serangan spesifik MCP dan persyaratan ID sesi kriptografi
  - Masalah Confused Deputy dalam skenario proxy MCP dengan persyaratan persetujuan eksplisit
  - Kerentanan passthrough token dengan kontrol validasi wajib
- **Keamanan Rantai Pasokan**: Perluasan cakupan rantai pasokan AI termasuk model fondasi, layanan embeddings, penyedia konteks, dan API pihak ketiga
- **Keamanan Fondasi**: Integrasi yang diperkuat dengan pola keamanan perusahaan termasuk arsitektur zero trust dan ekosistem keamanan Microsoft
- **Organisasi Sumber Daya**: Kategori tautan sumber daya komprehensif menurut jenis (Dokumen Resmi, Standar, Riset, Solusi Microsoft, Panduan Implementasi)

### Peningkatan Kualitas Dokumentasi
- **Tujuan Pembelajaran Terstruktur**: Peningkatan tujuan pembelajaran dengan hasil spesifik yang dapat dilakukan
- **Referensi Silang**: Menambahkan tautan antar topik keamanan dan konsep inti terkait
- **Informasi Terkini**: Memperbarui semua referensi tanggal dan tautan spesifikasi ke standar saat ini
- **Panduan Implementasi**: Menambahkan panduan implementasi spesifik dan dapat dilakukan di kedua bagian

## 16 Juli 2025

### Peningkatan README dan Navigasi
- Mendesain ulang penuh navigasi kurikulum di README.md
- Mengganti tag `<details>` dengan format berbasis tabel yang lebih mudah diakses
- Membuat opsi tata letak alternatif di folder baru "alternative_layouts"
- Menambahkan contoh navigasi berbasis kartu, tab, dan akordeon
- Memperbarui bagian struktur repository untuk memasukkan semua file terbaru
- Meningkatkan bagian "Cara Menggunakan Kurikulum Ini" dengan rekomendasi yang jelas
- Memperbarui tautan spesifikasi MCP untuk mengarah ke URL yang benar
- Menambahkan bagian Rekayasa Konteks (5.14) ke struktur kurikulum

### Pembaruan Panduan Studi
- Merevisi sepenuhnya panduan studi agar sesuai dengan struktur repository saat ini
- Menambahkan bagian baru untuk Klien dan Alat MCP, serta Server MCP Populer
- Memperbarui Peta Kurikulum Visual untuk mencerminkan semua topik secara akurat
- Meningkatkan deskripsi Topik Lanjutan untuk mencakup semua area khusus
- Memperbarui bagian Studi Kasus untuk mencerminkan contoh sebenarnya
- Menambahkan changelog komprehensif ini

### Kontribusi Komunitas (06-CommunityContributions/)
- Menambahkan informasi rinci tentang server MCP untuk generasi gambar
- Menambahkan bagian komprehensif tentang penggunaan Claude di VSCode
- Menambahkan instruksi setup dan penggunaan klien terminal Cline
- Memperbarui bagian klien MCP untuk mencakup semua opsi klien populer
- Meningkatkan contoh kontribusi dengan contoh kode yang lebih akurat

### Topik Lanjutan (05-AdvancedTopics/)
- Mengorganisasi semua folder topik khusus dengan penamaan konsisten
- Menambahkan materi dan contoh rekayasa konteks
- Menambahkan dokumentasi integrasi agen Foundry
- Meningkatkan dokumentasi integrasi keamanan Entra ID

## 11 Juni 2025

### Pembuatan Awal
- Merilis versi pertama kurikulum MCP untuk Pemula

- Membuat struktur dasar untuk semua 10 bagian utama
- Mengimplementasikan Visual Curriculum Map untuk navigasi
- Menambahkan contoh proyek awal dalam berbagai bahasa pemrograman

### Memulai (03-GettingStarted/)
- Membuat contoh implementasi server pertama
- Menambahkan panduan pengembangan klien
- Menyertakan instruksi integrasi klien LLM
- Menambahkan dokumentasi integrasi VS Code
- Mengimplementasikan contoh server Server-Sent Events (SSE)

### Konsep Inti (01-CoreConcepts/)
- Menambahkan penjelasan detail tentang arsitektur klien-server
- Membuat dokumentasi tentang komponen protokol utama
- Mendokumentasikan pola pesan dalam MCP

## 23 Mei 2025

### Struktur Repository
- Menginisialisasi repository dengan struktur folder dasar
- Membuat file README untuk setiap bagian utama
- Menyiapkan infrastruktur terjemahan
- Menambahkan aset gambar dan diagram

### Dokumentasi
- Membuat README.md awal dengan gambaran kurikulum
- Menambahkan CODE_OF_CONDUCT.md dan SECURITY.md
- Menyiapkan SUPPORT.md dengan panduan untuk mendapatkan bantuan
- Membuat struktur panduan studi awal

## 15 April 2025

### Perencanaan dan Kerangka
- Perencanaan awal untuk kurikulum MCP untuk Pemula
- Mendefinisikan tujuan pembelajaran dan audiens target
- Menguraikan struktur kurikulum 10 bagian
- Mengembangkan kerangka konseptual untuk contoh dan studi kasus
- Membuat contoh prototipe awal untuk konsep utama

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->