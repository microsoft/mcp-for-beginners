# Catatan Perubahan: Kurikulum MCP untuk Pemula

Dokumen ini berfungsi sebagai catatan semua perubahan signifikan yang dibuat pada kurikulum Model Context Protocol (MCP) untuk Pemula. Perubahan didokumentasikan dalam urutan kronologis terbalik (perubahan terbaru di depan).

## 29 Juli 2026

### Modul Baru 08 Pendamping: Sidecar Keandalan dan Percobaan Ulang Aman

Menambahkan pelajaran pendamping yang netral vendor untuk alat MCP yang menciptakan efek dunia nyata,
selaras dengan spesifikasi final `2026-07-28`.

- **Baru**: Pelajaran pendamping [sidecar keandalan][reliability-sidecar]
  menggunakan satu cerita tiket dukungan, dua diagram Mermaid, dan alur keputusan percobaan ulang
  untuk menjelaskan kunci operasi stabil, penerimaan duplikat atomik,
  rekonsiliasi, bukti, dan batas ekstensi Tasks.
- **Baru**: Latihan injeksi kegagalan Python dan SQLite perpustakaan standar
  menggunakan toko operasi dan tiket terpisah untuk menunjukkan respons yang hilang
  setelah efek eksternal dikomit. Enam tes deterministik mencakup duplikasi naif,
  pemulihan restart terjaga, konflik payload, hasil yang di-cache,
  klaim aktif, dan penerimaan duplikat bersamaan.
- **Diperbarui**: Modul 08 sekarang menautkan pelajaran pendamping, mengidentifikasi
  model permintaan tanpa status final `2026-07-28`, membedakan observabilitas OpenTelemetry
  dari fitur logging MCP yang sudah usang, dan membatasi contoh percobaan ulang generik
  hanya pada operasi baca saja.
- **Opsional**: Pelajaran memetakan konsep portabelnya ke satu implementasi komunitas bertanda tanpa
  menjadikan layanan yang dihosting atau panggilan jaringan sebagai bagian dari
  latihan.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 Juli 2026

### Pelajaran Baru: Kandidat Rilis Spesifikasi MCP 2026-07-28

Menambahkan cakupan kandidat rilis spesifikasi MCP `2026-07-28` yang akan datang (diumumkan 21 Mei 2026; rilis final dijadwalkan 28 Juli 2026), dirangkum dari [posting blog pengumuman resmi](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Baseline kurikulum tetap **Spesifikasi MCP 2025-11-25** sampai versi baru dirilis, jadi ini disajikan sebagai panduan ke depan dan bukan penulisan ulang pelajaran yang ada.

- **Baru**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — pelajaran lengkap yang mencakup inti protokol tanpa status (penghapusan handshake `initialize` dan `Mcp-Session-Id`), header routing baru `Mcp-Method`/`Mcp-Name`, metadata caching `ttlMs`/`cacheScope`, W3C Trace Context dalam `_meta`, kerangka Extensions formal (MCP Apps dan ekstensi Tasks baru), enam SEP penguatan otorisasi, penghapusan Roots/Sampling/Logging, dan perpindahan ke skema lengkap JSON Schema 2020-12 untuk skema alat.
- **Diperbarui** dengan penunjuk ke depan yang menautkan ke pelajaran baru:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): catatan versi protokol, bagian Sampling/Roots/Logging/Tasks, dan "Apa selanjutnya"

  - [02-Security/README.md](./02-Security/README.md): panggilan penguatan otorisasi
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): panggilan transport stateless
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): panggilan penghentian Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): panggilan penghentian Logging dan ekstensi Tasks
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): panggilan stateless/session-routing
  - [README.md](./README.md): catatan "Melihat ke depan" di bagian spesifikasi dan entri baru `1.1` di tabel modul kurikulum
  - [study_guide.md](./study_guide.md): poin yang menatap ke depan di bawah gambaran Konsep Inti dan catatan tambahan yang diberi tanggal
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): panggilan pada peta transport `mcp-session-id` sebelum model permintaan stateless
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): panggilan gambaran modul tentang Penghentian Root Contexts/Sampling dan ekstensi Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): panggilan penguatan otorisasi

## 24 Juni, 2026

### Pelajaran Baru: Menggunakan MCP di aplikasi Copilot

- [Bagian Tooling](./12-tooling/README.md) Ditambahkan bagian tooling.
- [MCP di aplikasi Copilot](./12-tooling/01-copilot-app/README.md)

## 16 Juni, 2026

### Penyelarasan Spesifikasi MCP & Validasi Contoh

Memvalidasi kurikulum terhadap **Spesifikasi MCP 2025-11-25** saat ini dan SDK resmi terbaru, kemudian memperbaiki referensi spesifikasi yang masih usang dan memastikan contoh inti masih dapat dibangun dan dijalankan.

#### Koreksi Versi Spesifikasi (2025-06-18 / 2025-03-26 → 2025-11-25)

Memperbarui konten bahasa Inggris di mana masih mengklaim revisi spesifikasi yang lebih lama sebagai standar *saat ini/terbaru*, dan mengarahkan ulang tautan ke jalur spesifikasi kanonik `modelcontextprotocol.io`:
- **05-AdvancedTopics/mcp-security/README.md**: Memperbarui spanduk "Standar Saat Ini", pengantar, judul prinsip keamanan inti, judul persyaratan wajib, bagian Microsoft Entra ID, tautan Referensi & Sumber Daya, dan pemberitahuan keamanan penutup (8 referensi) ke 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Memperbarui tautan spesifikasi Sumber Daya Tambahan dan spanduk "Standar Saat Ini" ke 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Mengganti tautan keamanan-dan-kepercayaan `2025-03-26` yang usang dengan halaman praktik terbaik keamanan 2025-11-25 saat ini

- **03-GettingStarted/14-sampling/README.md**: Memperbarui tautan dokumen sampling resmi ke 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: Diperbarui referensi "spesifikasi MCP saat ini" dalam tense sekarang dan tautan spesifikasi Sumber Daya Tambahan ke 2025-11-25 (catatan historis penghapusan SSE dibiarkan utuh untuk akurasi)

#### Validasi Contoh terhadap SDK Saat Ini

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` berhasil menyelesaikan `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` berhasil tanpa kesalahan tipe — API `McpServer`/`StdioServerTransport` yang ada tetap valid
- **Python (03-GettingStarted/01-first-server/solution/python)**: Divalidasi dalam `.venv` terisolasi dengan `mcp[cli]` (1.27.2); `py_compile` berhasil dan `FastMCP.list_tools()` mengembalikan dengan benar alat `add` dan `subtract`
- Dikonfirmasi semua rentang versi contoh `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) terselesaikan dengan bersih ke versi `1.29.0` saat ini tanpa perubahan API yang merusak

#### Penyelarasan Pin Ketergantungan (menutup celah versi)

Memperbarui pin SDK yang usang agar setiap contoh mengikuti rilis MCP saat ini, sesuai konvensi repositori secara umum:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Meningkatkan `@modelcontextprotocol/sdk` dari `^1.8.0` → `>=1.26.0` dan memperbarui deskripsi paket "updated for MCP 2025-06-18" yang ketinggalan menjadi "aligned with MCP Specification 2025-11-25"
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** dan **lab4/code/github_mcp_server/pyproject.toml**: Meningkatkan pin spesifik `mcp==1.23.0` → `mcp>=1.26.0`; menghasilkan ulang kedua file `uv.lock` (`uv lock`) sehingga lockfile terselesaikan ke `mcp 1.27.2` yang sekarang dan tetap sinkron dengan manifes

#### Analisis Celah Kurikulum — Cakupan Fitur Spesifikasi Terbaru

Diverifikasi kurikulum sudah mencakup semua primitif yang diperkenalkan/diperluas di MCP 2025-11-25, jadi tidak ada celah konten yang tersisa:
- **Sampling**: Pelajaran 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (termasuk mode URL)**: Didokumentasikan di 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Didokumentasikan di 00-Introduction, 01-CoreConcepts, dan 05-AdvancedTopics/mcp-root-contexts
- **Tasks (eksperimen, operasi jangka panjang)**: Didokumentasikan di 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features
- **Tool Annotations** (`readOnlyHint` / `destructiveHint`): Didokumentasikan di 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features

### Penguatan Keamanan & Perbaikan Kerentanan Ketergantungan

Melakukan pemeriksaan keamanan penuh pada setiap manifes ketergantungan dan kode sumber contoh, kemudian memperbaiki semua laporan advisory npm dan satu temuan di tingkat kode. Setelah perbaikan, `npm audit` melaporkan **0 kerentanan** di setiap direktori yang diaudit.

#### Kerentanan Ketergantungan npm (transitif) — Diperbaiki

Diaudit semua 15 file `package-lock.json` yang dikomit. Kerentanan terbatas pada ketergantungan transitif yang diambil oleh alat dev MCP Inspector, klien OpenAI, dan SDK MCP; semuanya kini terselesaikan tanpa merusak contoh:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** dan **lab3/code/weather_mcp/inspector**: Meningkatkan `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), yang menghapus advisory bundel `ajv`, `brace-expansion`, `diff`, `path-to-regexp` dan `ws`. Menambahkan entri npm `overrides` yang memaksa `shell-quote@1.8.4` yang telah diperbaiki untuk menghilangkan advisory kritis tersisa yang dibawa oleh `concurrently`; menghasilkan ulang kedua lockfile (sekarang 0 kerentanan)
- **03-GettingStarted/samples/typescript**: `npm audit fix` memperbarui `qs` transitif (sedang) ke rilis yang diperbaiki
- **03-GettingStarted/samples/javascript**: `npm audit fix` memperbarui `hono` transitif (sedang) ke rilis yang diperbaiki
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` memperbarui `form-data` transitif (tinggi) ke rilis yang diperbaiki
- **03-GettingStarted/11-simple-auth/solution/typescript**: Menghasilkan `package-lock.json` yang hilang sehingga proyek dapat direproduksi dan diaudit (0 kerentanan)

#### Perbaikan Keamanan Tingkat Kode (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Menghapus `shell=True` dari alat `open_in_vscode`. `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` sebelumnya memungkinkan metakarakter shell dalam jalur folder diinterpretasikan oleh `cmd.exe` (vektor injeksi perintah). Sekarang meluncurkan `Code.exe` yang sudah di-resolve langsung dengan folder sebagai argumen — tanpa shell — yang secara fungsional setara dan aman

#### Audit Ketergantungan Python

- Diaudit semua set persyaratan Python dengan `pip-audit`. `05-AdvancedTopics` dan `03-GettingStarted/samples/python` melaporkan **tidak ada kerentanan yang diketahui** (rentang `mcp` / `httpx` / `pydantic` / `python-dotenv` mereka terselesaikan ke rilis perbaikan saat ini)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` menandai ketergantungan transitif **`werkzeug` 3.1.1** dengan tiga advisory DoS nama perangkat Windows `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, dan `CVE-2026-27199` (semua diperbaiki di 3.1.6). Menambahkan pin keamanan eksplisit `werkzeug>=3.1.6` sehingga rilis yang diperbaiki terselesaikan; diverifikasi batasan terselesaikan dengan bersih dengan tumpukan `chainlit` / `mcp` / `semantic-kernel`

### Penggantian Merek Nama Produk

Memperbarui semua konten kurikulum untuk mencerminkan penggantian merek produk Microsoft:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Tautan komunitas Discord yang diperbarui

- **AGENTS.md**: Referensi server Discord diperbarui
- **README.md**: Referensi ekosistem teknologi diperbarui
- **study_guide.md**: Referensi studi kasus diperbarui
- **05-AdvancedTopics/README.md**: Judul dan deskripsi Modul 5.13 diperbarui
- **05-AdvancedTopics/mcp-integration/README.md**: Judul bagian dan deskripsi diperbarui
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Pembaruan penuh judul modul dan konten
- **05-AdvancedTopics/mcp-security-entra/README.md**: Tautan referensi silang diperbarui
- **07-LessonsfromEarlyAdoption/README.md**: Referensi studi kasus diperbarui
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Judul Bagian 9, lencana, dan kemampuan diperbarui
- **08-BestPractices/README.md**: Tautan komunitas Discord diperbarui
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Referensi saluran Discord diperbarui
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Referensi penempatan model diperbarui
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Tabel Layanan AI diperbarui
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Referensi sumber daya diperbarui

#### AI Toolkit / AITK → Ekstensi Microsoft Foundry Toolkit untuk VS Code
- **README.md**: Referensi kurikulum utama diperbarui
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Judul modul, gambaran umum, dan semua judul modul diperbarui
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Judul, tujuan pembelajaran, instruksi pengaturan, dan sumber daya diperbarui
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Judul, tujuan pembelajaran, tabel host MCP, dan referensi silang diperbarui
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Judul, lencana, prasyarat, dan sumber daya diperbarui
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Referensi Agent Builder dan tautan umpan balik diperbarui
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Prasyarat dan referensi ekstensi diperbarui

---

## 11 April 2026

### Pelajaran Baru, Perbaikan Dokumentasi, dan Pembaruan Ketergantungan

#### Konten Kurikulum Baru Ditambahkan

**Modul 05 - Topik Lanjutan**
- **Pelajaran 5.17: Penalaran Multi-Agen Adversarial dengan MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Panduan komprehensif baru yang membahas pola debat adversarial untuk sistem multi-agen
  - Diagram arsitektur Mermaid: dua agen → server MCP bersama → transkrip debat → juri → putusan
  - Server alat MCP bersama (`web_search` + `run_python`) diimplementasikan dalam Python dan TypeScript
  - Prompt sistem yang berlawanan (UNTUK / MENENTANG / Juri) dengan persyaratan penggunaan alat yang eksplisit
  - Orkestra debat dalam Python, TypeScript, dan C# yang mengelola putaran dan mengarahkan argumen
  - Pengkabelan MCP `ClientSession` untuk orkestrator ke panggilan alat nyata
  - Tabel kasus penggunaan (deteksi halusinasi, pemodelan ancaman, tinjauan desain API, verifikasi faktual, pemilihan teknologi)
  - Pertimbangan keamanan: eksekusi sandboxed, validasi panggilan alat, pembatasan laju, pencatatan audit
  - Latihan terstruktur dengan tiga skenario praktis (tinjauan kode, keputusan arsitektur, moderasi konten)

#### Perbaikan Dokumentasi

**Modul 03 - Memulai**
- **05-stdio-server/README.md**: Memperbaiki contoh server stdio TypeScript yang tidak lengkap — menambahkan instansiasi transport yang hilang (`new StdioServerTransport()`) dan panggilan `server.connect(transport)` agar sesuai dengan contoh Python dan .NET di bagian yang sama
- **14-sampling/README.md**: Memperbaiki kesalahan ketik — mengoreksi `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Pembaruan Kurikulum

**README.md Utama**
- Menambahkan entri 5.17 (Penalaran Multi-Agen Adversarial dengan MCP) ke tabel kurikulum dengan tautan langsung ke pelajaran baru

**05-AdvancedTopics/README.md**
- Menambahkan baris Pelajaran 5.17 ke tabel pelajaran

**study_guide.md**
- Menambahkan topik Penalaran Multi-Agen Adversarial ke peta pikiran dan deskripsi prosa Topik Lanjutan

#### Perbaikan Kode dan Keamanan

**Modul 05 - Agen Adversarial (`mcp-adversarial-agents`)**
- **Perbaikan keamanan — injeksi perintah**: Mengganti interpolasi shell `execSync` dengan `execFile` + `promisify` dalam alat `run_python` TypeScript, menghilangkan permukaan injeksi perintah (kode yang dikendalikan LLM sekarang dilewatkan sebagai elemen argv literal tanpa keterlibatan shell)
- **Pengkabelan loop alat MCP**: Memperbarui orkestrator debat Python untuk menggunakan klien `AsyncAnthropic` (mengganti `Anthropic` sinkron yang memblokir), meneruskan `ClientSession` langsung ke setiap giliran agen, mengambil definisi alat melalui `session.list_tools()` setiap giliran, dan mengirim blok `tool_use` melalui `session.call_tool()` dalam loop hingga model mengeluarkan respons teks akhir

#### Pembaruan Ketergantungan

- Meningkatkan `hono` ke 4.12.12 di banyak paket (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Meningkatkan `@hono/node-server` dari 1.19.11 ke 1.19.13 di paket TypeScript
- Meningkatkan `cryptography` dari 46.0.5 ke 46.0.7 di paket Python (lab 3 dan 4 10-StreamliningAIWorkflows)
- Meningkatkan `lodash` dari 4.17.23 ke 4.18.1 di inspector 10-StreamliningAIWorkflows

#### Penerjemahan

- Menyetel sinkronisasi terjemahan untuk 48+ bahasa dengan perubahan sumber terbaru (pembaruan i18n)

---

## 5 Februari 2026

### Peningkatan Validasi dan Navigasi Seluruh Repositori

#### Konten Kurikulum Baru Ditambahkan

**Modul 03 - Memulai**
- **12-mcp-hosts/README.md**: Panduan komprehensif baru untuk pengaturan host MCP
  - Contoh konfigurasi Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - Template konfigurasi JSON untuk semua host utama
  - Tabel perbandingan jenis transport (stdio, SSE/HTTP, WebSocket)
  - Pemecahan masalah masalah koneksi umum
  - Praktik terbaik keamanan untuk konfigurasi host

- **13-mcp-inspector/README.md**: Panduan debugging baru untuk MCP Inspector
  - Metode instalasi (npx, npm global, dari sumber)
  - Menghubungkan ke server melalui stdio dan HTTP/SSE
  - Menguji alat, sumber daya, dan alur kerja prompt
  - Integrasi VS Code dengan MCP Inspector
  - Skenario debugging umum dengan solusi

**Modul 04 - Implementasi Praktis**
- **pagination/README.md**: Panduan penerapan pagination baru
  - Pola pagination berbasis cursor di Python, TypeScript, Java
  - Penanganan pagination sisi klien
  - Strategi desain cursor (opaque vs. terstruktur)
  - Rekomendasi optimasi performa

**Modul 05 - Topik Lanjutan**
- **mcp-protocol-features/README.md**: Penjelasan mendalam fitur protokol baru
  - Implementasi notifikasi kemajuan
  - Pola pembatalan permintaan
  - Template sumber daya dengan pola URI
  - Manajemen siklus hidup server
  - Kontrol tingkat pencatatan
  - Pola penanganan kesalahan dengan kode JSON-RPC

#### Perbaikan Navigasi (24+ file diperbarui)

**README Modul Utama**
 Sekarang menautkan baik pelajaran pertama DAN modul berikutnya

**Sub-file Keamanan 02**
- Semua 5 dokumen keamanan tambahan sekarang memiliki navigasi "Apa Selanjutnya":

**File Studi Kasus 09**
- Semua file studi kasus sekarang memiliki navigasi berurutan:

**Lab 10-StreamliningAI**
Ditambahkan bagian Apa Selanjutnya ke gambaran Modul 10 dan Modul 11

#### Perbaikan Kode dan Konten

**Pembaruan SDK dan Ketergantungan**
Memperbaiki versi openai kosong menjadi `^4.95.0`
Memperbarui SDK dari `^1.8.0` menjadi `>=1.26.0`
Memperbarui pin versi mcp menjadi `>=1.26.0`

**Perbaikan Kode**
Memperbaiki model tidak valid `gpt-4o-mini` menjadi `gpt-4.1-mini`

**Perbaikan Konten**
Memperbaiki tautan rusak `READMEmd` → `README.md`, memperbaiki header kurikulum `Module 1-3` → `Module 0-3`, memperbaiki path yang peka huruf besar-kecil
Menghapus duplikat konten Studi Kasus 5 yang rusak

**Peningkatan Panduan Pemula**
Menambahkan pengantar tepat, tujuan pembelajaran, dan prasyarat untuk pemula

#### Pembaruan Kurikulum

**README.md Utama**
- Menambahkan entri 3.12 (Host MCP), 3.13 (Inspektur MCP), 4.1 (Pagination), 5.16 (Fitur Protokol) ke tabel kurikulum

**README Modul**
Menambahkan pelajaran 12 dan 13 ke daftar pelajaran
Menambahkan bagian Panduan Praktis dengan tautan pagination
Menambahkan pelajaran 5.15 (Transportasi Kustom) dan 5.16 (Fitur Protokol)

**study_guide.md**
- Memperbarui mindmap dengan semua topik baru: Pengaturan Host MCP, Inspektur MCP, Strategi Pagination, Penjelasan Mendalam Fitur Protokol

## 28 Jan 2026

### Tinjauan Kepatuhan Spesifikasi MCP 2025-11-25

#### Peningkatan Konsep Inti (01-CoreConcepts/)
- **Primitive Klien Baru - Roots**: Menambahkan dokumentasi komprehensif tentang primitive klien Roots, memungkinkan server memahami batas sistem file dan izin akses
- **Anotasi Alat**: Menambahkan dokumentasi tentang anotasi perilaku alat (`readOnlyHint`, `destructiveHint`) untuk keputusan eksekusi alat yang lebih baik
- **Pemanggilan Alat dalam Sampling**: Memperbarui dokumentasi Sampling untuk memasukkan parameter `tools` dan `toolChoice` untuk pemanggilan alat yang dipandu model selama permintaan sampling
- **Penggalian Mode URL**: Menambahkan dokumentasi tentang penggalian berbasis URL untuk interaksi web eksternal yang diprakarsai server
- **Tugas (Eksperimental)**: Menambahkan bagian baru yang mendokumentasikan fitur tugas eksperimental untuk pembungkus eksekusi tahan lama dan pengambilan hasil tertunda
- **Dukungan Ikon**: Dicatat bahwa alat, sumber daya, template sumber daya, dan prompt kini dapat menyertakan ikon sebagai metadata tambahan

#### Pembaruan Dokumentasi
- **README.md**: Menambahkan referensi versi Spesifikasi MCP 2025-11-25 dan penjelasan pemversian berbasis tanggal
- **study_guide.md**: Memperbarui peta kurikulum untuk memasukkan Tugas dan Anotasi Alat di bagian Konsep Inti; memperbarui timestamp dokumen

#### Verifikasi Kepatuhan Spesifikasi
- **Versi Protokol**: Memverifikasi semua dokumentasi merujuk ke Spesifikasi MCP 2025-11-25 terkini
- **Keselarasan Arsitektur**: Mengonfirmasi akurasi dokumentasi arsitektur dua lapis (Lapisan Data + Lapisan Transportasi)
- **Dokumentasi Primitif**: Memvalidasi primitive server (Sumber Daya, Prompt, Alat) dan primitive klien (Sampling, Penggalian, Logging, Roots)
- **Mekanisme Transportasi**: Memverifikasi akurasi dokumentasi transportasi STDIO dan HTTP Streamable
- **Panduan Keamanan**: Mengonfirmasi keselarasan dengan dokumentasi Praktik Terbaik Keamanan MCP terkini

#### Fitur Utama MCP 2025-11-25 yang Didokumentasikan
- **Penemuan OpenID Connect**: Penemuan server otentikasi melalui OIDC
- **Dokumen Metadata OAuth Client ID**: Rekomendasi mekanisme pendaftaran klien
- **JSON Schema 2020-12**: Dialek default untuk definisi skema MCP
- **Sistem Tingkatan SDK**: Formalisasi persyaratan dukungan dan pemeliharaan fitur SDK
- **Struktur Tata Kelola**: Formalisasi Kelompok Kerja dan Kelompok Minat dalam tata kelola MCP

### Pembaruan Besar Dokumentasi Keamanan (02-Security/)

#### Integrasi Workshop MCP Security Summit (Sherpa)
- **Sumber Pelatihan Praktis Baru**: Menambahkan integrasi komprehensif dengan [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) di seluruh dokumentasi keamanan
- **Cakupan Rute Ekspedisi**: M mendokumentasikan progresi lengkap dari Base Camp ke Summit
- **Keselarasan OWASP**: Semua panduan keamanan sekarang memetakan ke risiko OWASP MCP Azure Security Guide

#### Integrasi OWASP MCP Top 10
- **Bagian Baru**: Menambahkan tabel Risiko Keamanan OWASP MCP Top 10 dengan mitigasi Azure ke README Keamanan utama
- **Dokumentasi Berbasis Risiko**: Memperbarui mcp-security-controls-2025.md dengan referensi risiko OWASP MCP untuk setiap domain keamanan
- **Arsitektur Referensi**: Menautkan ke arsitektur referensi dan pola implementasi OWASP MCP Azure Security Guide

#### File Keamanan yang Diperbarui
- **README.md**: Menambahkan gambaran Workshop Sherpa, tabel rute ekspedisi, ringkasan risiko OWASP MCP Top 10, dan bagian pelatihan praktis
- **mcp-security-controls-2025.md**: Memperbarui header ke Februari 2026, menambahkan referensi risiko OWASP (MCP01-MCP08), memperbaiki ketidaksesuaian versi spesifikasi
- **mcp-security-best-practices-2025.md**: Menambahkan bagian sumber daya Sherpa dan OWASP, memperbarui timestamp
- **mcp-best-practices.md**: Menambahkan bagian pelatihan praktis dengan tautan Sherpa dan OWASP
- **azure-content-safety-implementation.md**: Menambahkan referensi OWASP MCP06, keselarasan Sherpa Camp 3, dan bagian sumber daya tambahan

#### Tautan Sumber Daya Baru Ditambahkan
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [Panduan Keamanan OWASP MCP Azure](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Halaman risiko individu OWASP MCP (MCP01-MCP10)

### Penyelarasan Spesifikasi MCP Seluruh Kurikulum 2025-11-25

#### Modul 03 - Memulai
- **Dokumentasi SDK**: Menambahkan Go SDK ke daftar SDK resmi; memperbarui semua referensi SDK agar sesuai dengan Spesifikasi MCP 2025-11-25
- **Klarifikasi Transportasi**: Memperbarui deskripsi transport STDIO dan HTTP Streaming dengan referensi spesifikasi yang eksplisit

#### Modul 04 - Implementasi Praktis
- **Pembaruan SDK**: Menambahkan Go SDK; memperbarui daftar SDK dengan referensi versi spesifikasi
- **Spesifikasi Otorisasi**: Memperbarui tautan spesifikasi Otorisasi MCP ke versi terbaru 2025-11-25

#### Modul 05 - Topik Lanjutan
- **Fitur Baru**: Menambahkan catatan tentang fitur baru Spesifikasi MCP 2025-11-25 (Tugas, Anotasi Alat, Peng elicitan Mode URL, Roots)
- **Sumber Keamanan**: Menambahkan tautan OWASP MCP Top 10 dan lokakarya Sherpa ke referensi tambahan

#### Modul 06 - Kontribusi Komunitas
- **Daftar SDK**: Menambahkan Swift dan Rust SDK; memperbarui tautan spesifikasi ke 2025-11-25
- **Referensi Spesifikasi**: Memperbarui tautan Spesifikasi MCP ke URL spesifikasi langsung

#### Modul 07 - Pelajaran dari Adopsi Awal
- **Pembaruan Sumber**: Menambahkan tautan Spesifikasi MCP 2025-11-25 dan OWASP MCP Top 10 ke sumber tambahan

#### Modul 08 - Praktik Terbaik
- **Versi Spesifikasi**: Memperbarui referensi Spesifikasi MCP ke 2025-11-25
- **Sumber Keamanan**: Menambahkan OWASP MCP Top 10 dan lokakarya Sherpa ke referensi tambahan

#### Modul 10 - Mempermudah Alur Kerja AI
- **Pembaruan Badge**: Mengubah badge versi MCP dari versi SDK (1.9.3) ke versi spesifikasi (2025-11-25)
- **Tautan Sumber**: Memperbarui tautan Spesifikasi MCP; menambahkan OWASP MCP Top 10

#### Modul 11 - Lab Praktik MCP Server
- **Referensi Spesifikasi**: Memperbarui tautan Spesifikasi MCP ke versi 2025-11-25
- **Sumber Keamanan**: Menambahkan OWASP MCP Top 10 ke sumber resmi

## 18 Desember 2025

### Pembaruan Dokumentasi Keamanan - Spesifikasi MCP 2025-11-25

#### Praktik Terbaik Keamanan MCP (02-Security/mcp-best-practices.md) - Pembaruan Versi Spesifikasi
- **Pembaruan Versi Protokol**: Memperbarui untuk merujuk Spesifikasi MCP terbaru 2025-11-25 (dirilis 25 November 2025)
  - Memperbarui semua referensi versi spesifikasi dari 2025-06-18 ke 2025-11-25
  - Memperbarui referensi tanggal dokumen dari 18 Agustus 2025 ke 18 Desember 2025
  - Memastikan semua URL spesifikasi mengarah ke dokumentasi saat ini
- **Validasi Konten**: Validasi menyeluruh praktik terbaik keamanan terhadap standar terbaru
  - **Solusi Keamanan Microsoft**: Memastikan terminologi dan tautan terkini untuk Prompt Shields (sebelumnya "deteksi risiko jailbreak"), Azure Content Safety, Microsoft Entra ID, dan Azure Key Vault
  - **Keamanan OAuth 2.1**: Memastikan keselarasan dengan praktik terbaik keamanan OAuth terbaru
  - **Standar OWASP**: Validasi referensi OWASP Top 10 untuk LLM tetap mutakhir
  - **Layanan Azure**: Memeriksa semua tautan dokumentasi Microsoft Azure dan praktik terbaik
- **Keselarasan Standar**: Semua standar keamanan yang dirujuk dikonfirmasi mutakhir
  - Kerangka Manajemen Risiko AI NIST
  - ISO 27001:2022
  - Praktik Terbaik Keamanan OAuth 2.1
  - Kerangka keamanan dan kepatuhan Azure
- **Sumber Implementasi**: Memvalidasi semua tautan panduan implementasi dan sumber daya
  - Pola otentikasi Azure API Management
  - Panduan integrasi Microsoft Entra ID
  - Manajemen rahasia Azure Key Vault
  - Pipeline DevSecOps dan solusi pemantauan

### Penjaminan Mutu Dokumentasi
- **Kepatuhan Spesifikasi**: Memastikan semua persyaratan keamanan MCP wajib (MUST/MUST NOT) sesuai dengan spesifikasi terbaru
- **Ketersediaan Sumber**: Memeriksa semua tautan eksternal ke dokumentasi Microsoft, standar keamanan, dan panduan implementasi
- **Cakupan Praktik Terbaik**: Memastikan cakupan menyeluruh otentikasi, otorisasi, ancaman spesifik AI, keamanan rantai pasokan, dan pola enterprise

## 6 Oktober 2025

### Perluasan Bagian Memulai – Penggunaan Server Tingkat Lanjut & Otentikasi Sederhana

#### Penggunaan Server Tingkat Lanjut (03-GettingStarted/10-advanced)
- **Bab Baru Ditambahkan**: Memperkenalkan panduan komprehensif penggunaan server MCP tingkat lanjut, mencakup arsitektur server reguler dan tingkat rendah.
  - **Server Reguler vs Tingkat Rendah**: Perbandingan detail dan contoh kode dalam Python dan TypeScript untuk kedua pendekatan.
  - **Desain Berbasis Handler**: Penjelasan pengelolaan alat/sumber daya/prompt berbasis handler untuk implementasi server yang skalabel dan fleksibel.
  - **Pola Praktis**: Skenario nyata di mana pola server tingkat rendah bermanfaat untuk fitur tingkat lanjut dan arsitektur.

#### Otentikasi Sederhana (03-GettingStarted/11-simple-auth)
- **Bab Baru Ditambahkan**: Panduan langkah demi langkah untuk mengimplementasikan otentikasi sederhana pada server MCP.
  - **Konsep Auth**: Penjelasan jelas tentang otentikasi vs otorisasi, dan penanganan kredensial.
  - **Implementasi Auth Dasar**: Pola otentikasi berbasis middleware dalam Python (Starlette) dan TypeScript (Express), dengan contoh kode.
  - **Kemajuan ke Keamanan Lanjutan**: Panduan memulai dengan otentikasi sederhana dan melanjutkan ke OAuth 2.1 dan RBAC, dengan referensi modul keamanan lanjutan.

Tambahan ini menyediakan panduan praktis langsung untuk membangun implementasi server MCP yang lebih tahan banting, aman, dan fleksibel, menjembatani konsep dasar dengan pola produksi canggih.

## 29 September 2025

### Lab Integrasi Database MCP Server - Jalur Pembelajaran Praktis Komprehensif

#### 11-MCPServerHandsOnLabs - Kurikulum Lengkap Integrasi Database Baru
- **Jalur Pembelajaran 13 Lab Lengkap**: Menambahkan kurikulum praktis lengkap untuk membangun server MCP siap produksi dengan integrasi database PostgreSQL
  - **Implementasi Dunia Nyata**: Kasus penggunaan analitik ritel Zava yang menunjukkan pola kelas enterprise
  - **Progresi Pembelajaran Terstruktur**:
    - **Lab 00-03: Dasar-Dasar** - Pengenalan, Arsitektur Inti, Keamanan & Multi-Tenancy, Pengaturan Lingkungan
    - **Lab 04-06: Membangun Server MCP** - Desain & Skema Database, Implementasi Server MCP, Pengembangan Alat  
    - **Lab 07-09: Fitur Lanjutan** - Integrasi Pencarian Semantik, Pengujian & Debugging, Integrasi VS Code
    - **Lab 10-12: Produksi & Praktik Terbaik** - Strategi Penyebaran, Pemantauan & Observabilitas, Praktik Terbaik & Optimasi
  - **Teknologi Enterprise**: Kerangka kerja FastMCP, PostgreSQL dengan pgvector, embedding Azure OpenAI, Azure Container Apps, Application Insights
  - **Fitur Lanjutan**: Row Level Security (RLS), pencarian semantik, akses data multi-tenant, embedding vektor, pemantauan waktu nyata

#### Standardisasi Terminologi - Konversi Modul ke Lab
- **Pembaruan Dokumentasi Komprehensif**: Sistematis memperbarui semua file README di 11-MCPServerHandsOnLabs untuk menggunakan terminologi "Lab" menggantikan "Modul"
  - **Judul Bagian**: Memperbarui "Apa yang Cakup Modul Ini" menjadi "Apa yang Cakup Lab Ini" di seluruh 13 lab
  - **Deskripsi Konten**: Mengganti "Modul ini menyediakan..." menjadi "Lab ini menyediakan..." di seluruh dokumentasi
  - **Tujuan Pembelajaran**: Memperbarui "Pada akhir modul ini..." menjadi "Pada akhir lab ini..." 
  - **Tautan Navigasi**: Mengonversi semua referensi "Modul XX:" menjadi "Lab XX:" dalam referensi silang dan navigasi
  - **Pelacakan Penyelesaian**: Memperbarui "Setelah menyelesaikan modul ini..." menjadi "Setelah menyelesaikan lab ini..."
  - **Referensi Teknis Terjaga**: Mempertahankan referensi modul Python dalam file konfigurasi (misalnya, `"module": "mcp_server.main"`)

#### Peningkatan Panduan Studi (study_guide.md)
- **Peta Kurikulum Visual**: Menambahkan bagian baru "11. Lab Integrasi Database" dengan visualisasi struktur lab komprehensif
- **Struktur Repositori**: Memperbarui dari sepuluh menjadi sebelas bagian utama dengan deskripsi rinci 11-MCPServerHandsOnLabs
- **Panduan Jalur Pembelajaran**: Meningkatkan instruksi navigasi untuk mencakup bagian 00-11
- **Cakupan Teknologi**: Menambahkan detail integrasi FastMCP, PostgreSQL, layanan Azure
- **Hasil Pembelajaran**: Menekankan pengembangan server siap produksi, pola integrasi database, dan keamanan enterprise

#### Peningkatan Struktur README Utama
- **Terminologi Berbasis Lab**: Memperbarui README.md utama di 11-MCPServerHandsOnLabs untuk konsisten menggunakan struktur "Lab"
- **Organisasi Jalur Pembelajaran**: Progresi jelas dari konsep dasar melalui implementasi lanjutan hingga penyebaran produksi
- **Fokus Dunia Nyata**: Penekanan pada pembelajaran praktis langsung dengan pola dan teknologi kelas enterprise

### Peningkatan Kualitas & Konsistensi Dokumentasi
- **Penekanan Pembelajaran Praktis**: Memperkuat pendekatan berbasis lab secara menyeluruh dalam dokumentasi
- **Fokus Pola Enterprise**: Menyoroti implementasi siap produksi dan pertimbangan keamanan enterprise
- **Integrasi Teknologi**: Cakupan komprehensif layanan Azure modern dan pola integrasi AI
- **Progresi Pembelajaran**: Jalur jelas dan terstruktur dari konsep dasar ke penyebaran produksi

## 26 September 2025

### Peningkatan Studi Kasus - Integrasi GitHub MCP Registry

#### Studi Kasus (09-CaseStudy/) - Fokus Pengembangan Ekosistem
- **README.md**: Perluasan besar dengan studi kasus GitHub MCP Registry yang komprehensif
  - **Studi Kasus GitHub MCP Registry**: Studi kasus lengkap baru yang mengkaji peluncuran GitHub MCP Registry pada September 2025
    - **Analisis Masalah**: Pemeriksaan rinci tantangan penemuan dan penyebaran server MCP yang terfragmentasi
    - **Arsitektur Solusi**: Pendekatan registry terpusat GitHub dengan instalasi VS Code satu-klik
    - **Dampak Bisnis**: Peningkatan terukur dalam onboarding dan produktivitas pengembang
    - **Nilai Strategis**: Fokus pada penyebaran agen modular dan interoperabilitas lintas-alat
    - **Pengembangan Ekosistem**: Pemosisian sebagai platform dasar untuk integrasi agenik
  - **Struktur Studi Kasus yang Ditingkatkan**: Memperbarui ketujuh studi kasus dengan format konsisten dan deskripsi komprehensif
    - Agen Perjalanan AI Azure: Penekanan orkestrasi multi-agen
    - Integrasi Azure DevOps: Fokus otomasi alur kerja
    - Pengambilan Dokumentasi Waktu Nyata: Implementasi klien konsol Python
    - Generator Rencana Studi Interaktif: Aplikasi web percakapan Chainlit
    - Dokumentasi Dalam Editor: Integrasi VS Code dan GitHub Copilot
    - Azure API Management: Pola integrasi API enterprise
    - GitHub MCP Registry: Pengembangan ekosistem dan platform komunitas
  - **Kesimpulan Komprehensif**: Bagian kesimpulan yang ditulis ulang menyoroti tujuh studi kasus mencakup berbagai dimensi implementasi MCP
    - Integrasi Enterprise, Orkestrasi Multi-Agen, Produktivitas Pengembang
    - Pengembangan Ekosistem, Kategorisasi Aplikasi Pendidikan
    - Wawasan yang diperluas tentang pola arsitektur, strategi implementasi, dan praktik terbaik
    - Penekanan pada MCP sebagai protokol matang dan siap produksi

#### Pembaruan Panduan Studi (study_guide.md)
- **Peta Kurikulum Visual**: Memperbarui mindmap untuk memasukkan GitHub MCP Registry di bagian Studi Kasus
- **Deskripsi Studi Kasus**: Meningkatkan dari deskripsi umum menjadi uraian rinci tujuh studi kasus komprehensif
- **Struktur Repositori**: Memperbarui bagian 10 untuk mencerminkan cakupan studi kasus lengkap dengan detail implementasi spesifik
- **Integrasi Changelog**: Menambahkan entri 26 September 2025 yang mendokumentasikan penambahan GitHub MCP Registry dan peningkatan studi kasus
- **Pembaruan Tanggal**: Memperbarui timestamp footer untuk mencerminkan revisi terbaru (26 September 2025)

### Peningkatan Kualitas Dokumentasi
- **Peningkatan Konsistensi**: Standarisasi format dan struktur studi kasus di semua tujuh contoh
- **Cakupan Komprehensif**: Studi kasus kini mencakup skenario enterprise, produktivitas pengembang, dan pengembangan ekosistem
- **Pemosisian Strategis**: Fokus diperkuat pada MCP sebagai platform dasar untuk penyebaran sistem agenik
- **Integrasi Sumber Daya**: Memperbarui sumber tambahan untuk menyertakan tautan GitHub MCP Registry

## 15 September 2025

### Perluasan Topik Lanjutan - Transportasi Kustom & Rekayasa Konteks

#### Transportasi Kustom MCP (05-AdvancedTopics/mcp-transport/) - Panduan Implementasi Lanjutan Baru
- **README.md**: Panduan implementasi lengkap untuk mekanisme transportasi MCP kustom
  - **Transportasi Azure Event Grid**: Implementasi transportasi event-driven tanpa server yang komprehensif
    - Contoh C#, TypeScript, dan Python dengan integrasi Azure Functions
    - Pola arsitektur event-driven untuk solusi MCP yang skalabel
    - Penerima webhook dan penanganan pesan berbasis push
  - **Transportasi Azure Event Hubs**: Implementasi transportasi streaming throughput tinggi
    - Kemampuan streaming waktu nyata untuk skenario latensi rendah
    - Strategi partisi dan manajemen checkpoint
    - Pengelolaan batch pesan dan optimasi performa
  - **Pola Integrasi Enterprise**: Contoh arsitektur siap produksi
    - Pemrosesan MCP terdistribusi di banyak Azure Functions
    - Arsitektur transportasi hibrida menggabungkan beberapa tipe transportasi
    - Strategi ketahanan pesan, keandalan, dan penanganan kesalahan
  - **Keamanan & Pemantauan**: Integrasi Azure Key Vault dan pola observabilitas
    - Otentikasi identitas terkelola dan akses dengan hak istimewa paling rendah
    - Telemetri Application Insights dan pemantauan performa
    - Pemutus sirkuit dan pola toleransi kesalahan
  - **Kerangka Pengujian**: Strategi pengujian komprehensif untuk transportasi kustom
    - Pengujian unit dengan test doubles dan framework mocking
    - Pengujian integrasi dengan Azure Test Containers
    - Pertimbangan pengujian performa dan beban

#### Rekayasa Konteks (05-AdvancedTopics/mcp-contextengineering/) - Disiplin AI yang Berkembang
- **README.md**: Eksplorasi komprehensif tentang rekayasa konteks sebagai bidang yang berkembang
  - **Prinsip Inti**: Berbagi konteks lengkap, kesadaran keputusan tindakan, dan pengelolaan jendela konteks

  - **Penyesuaian Protokol MCP**: Bagaimana desain MCP mengatasi tantangan rekayasa konteks
    - Batasan jendela konteks dan strategi pemuatan progresif
    - Penentuan relevansi dan pengambilan konteks dinamis
    - Penanganan konteks multi-modal dan pertimbangan keamanan
  - **Pendekatan Implementasi**: Arsitektur single-threaded vs. multi-agent
    - Teknik pemotongan konteks dan prioritisasi
    - Strategi pemuatan dan kompresi konteks progresif
    - Pendekatan berlapis untuk konteks dan optimisasi pengambilan
  - **Kerangka Pengukuran**: Metrik baru untuk evaluasi efektivitas konteks
    - Efisiensi input, kinerja, kualitas, dan pertimbangan pengalaman pengguna
    - Pendekatan eksperimental untuk optimisasi konteks
    - Analisis kegagalan dan metodologi perbaikan

#### Pembaruan Navigasi Kurikulum (README.md)
- **Struktur Modul yang Ditingkatkan**: Tabel kurikulum diperbarui untuk memasukkan topik lanjutan baru
  - Ditambahkan entri Rekayasa Konteks (5.14) dan Transportasi Kustom (5.15)
  - Format dan tautan navigasi konsisten di semua modul
  - Deskripsi diperbarui untuk mencerminkan cakupan konten saat ini

### Peningkatan Struktur Direktori
- **Standarisasi Penamaan**: Mengubah nama "mcp transport" menjadi "mcp-transport" agar konsisten dengan folder topik lanjutan lainnya
- **Organisasi Konten**: Semua folder 05-AdvancedTopics sekarang mengikuti pola penamaan konsisten (mcp-[topik])

### Peningkatan Kualitas Dokumentasi
- **Penyesuaian Spesifikasi MCP**: Semua konten baru merujuk pada Spesifikasi MCP 2025-06-18 saat ini
- **Contoh Multi-Bahasa**: Contoh kode lengkap dalam C#, TypeScript, dan Python
- **Fokus Enterprise**: Pola siap produksi dan integrasi cloud Azure di seluruh dokumentasi
- **Dokumentasi Visual**: Diagram Mermaid untuk visualisasi arsitektur dan aliran

## 18 Agustus 2025

### Pembaruan Komprehensif Dokumentasi - Standar MCP 2025-06-18

#### Praktik Terbaik Keamanan MCP (02-Security/) - Modernisasi Lengkap
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Penulisan ulang lengkap sesuai Spesifikasi MCP 2025-06-18
  - **Persyaratan Wajib**: Ditambahkan persyaratan HARUS/TIDAK BOLEH eksplisit dari spesifikasi resmi dengan indikator visual yang jelas
  - **12 Praktik Keamanan Inti**: Restrukturisasi dari daftar 15 item menjadi domain keamanan komprehensif
    - Keamanan Token & Autentikasi dengan integrasi penyedia identitas eksternal
    - Manajemen Sesi & Keamanan Transportasi dengan persyaratan kriptografi
    - Perlindungan Ancaman Khusus AI dengan integrasi Microsoft Prompt Shields
    - Kontrol Akses & Izin dengan prinsip hak istimewa minimum
    - Keamanan Konten & Pemantauan dengan integrasi Azure Content Safety
    - Keamanan Rantai Pasokan dengan verifikasi komponen komprehensif
    - Keamanan OAuth & Pencegahan Confused Deputy dengan implementasi PKCE
    - Respons & Pemulihan Insiden dengan kapabilitas otomatisasi
    - Kepatuhan & Tata Kelola dengan keselarasan regulasi
    - Kontrol Keamanan Lanjutan dengan arsitektur zero trust
    - Integrasi Ekosistem Keamanan Microsoft dengan solusi komprehensif
    - Evolusi Keamanan Berkelanjutan dengan praktik adaptif
  - **Solusi Keamanan Microsoft**: Panduan integrasi yang ditingkatkan untuk Prompt Shields, Azure Content Safety, Entra ID, dan GitHub Advanced Security
  - **Sumber Daya Implementasi**: Tautan sumber daya komprehensif yang dikategorikan menurut Dokumentasi Resmi MCP, Solusi Keamanan Microsoft, Standar Keamanan, dan Panduan Implementasi

#### Kontrol Keamanan Lanjutan (02-Security/) - Implementasi Enterprise
- **MCP-SECURITY-CONTROLS-2025.md**: Pembaruan menyeluruh dengan kerangka kerja keamanan kelas enterprise
  - **9 Domain Keamanan Komprehensif**: Perluasan dari kontrol dasar ke kerangka enterprise terperinci
    - Autentikasi & Otorisasi Lanjutan dengan integrasi Microsoft Entra ID
    - Keamanan Token & Kontrol Anti-Passthrough dengan validasi komprehensif
    - Kontrol Keamanan Sesi dengan pencegahan pembajakan
    - Kontrol Keamanan Khusus AI dengan pencegahan prompt injection dan tool poisoning
    - Pencegahan Serangan Confused Deputy dengan keamanan proxy OAuth
    - Keamanan Eksekusi Alat dengan sandboxing dan isolasi
    - Kontrol Keamanan Rantai Pasokan dengan verifikasi dependensi
    - Kontrol Pemantauan & Deteksi dengan integrasi SIEM
    - Respons & Pemulihan Insiden dengan kapabilitas otomatisasi
  - **Contoh Implementasi**: Ditambahkan blok konfigurasi YAML terperinci dan contoh kode
  - **Integrasi Solusi Microsoft**: Cakupan lengkap layanan keamanan Azure, GitHub Advanced Security, dan manajemen identitas enterprise

#### Keamanan Topik Lanjutan (05-AdvancedTopics/mcp-security/) - Implementasi Siap Produksi
- **README.md**: Penulisan ulang lengkap untuk implementasi keamanan enterprise
  - **Penyesuaian Spesifikasi Saat Ini**: Diperbarui ke Spesifikasi MCP 2025-06-18 dengan persyaratan keamanan wajib
  - **Autentikasi yang Ditingkatkan**: Integrasi Microsoft Entra ID dengan contoh lengkap .NET dan Java Spring Security
  - **Integrasi Keamanan AI**: Implementasi Microsoft Prompt Shields dan Azure Content Safety dengan contoh Python terperinci
  - **Mitigasi Ancaman Lanjutan**: Contoh implementasi komprehensif untuk
    - Pencegahan Serangan Confused Deputy dengan PKCE dan validasi persetujuan pengguna
    - Pencegahan Token Passthrough dengan validasi audiens dan manajemen token aman
    - Pencegahan Pembajakan Sesi dengan pengikatan kriptografi dan analisis perilaku
  - **Integrasi Keamanan Enterprise**: Pemantauan Azure Application Insights, pipeline deteksi ancaman, dan keamanan rantai pasokan
  - **Daftar Periksa Implementasi**: Kontrol keamanan wajib vs. yang direkomendasikan dengan keuntungan ekosistem keamanan Microsoft

### Kualitas Dokumentasi & Penyesuaian Standar
- **Referensi Spesifikasi**: Memperbarui semua referensi ke Spesifikasi MCP 2025-06-18 saat ini
- **Ekosistem Keamanan Microsoft**: Panduan integrasi yang ditingkatkan di seluruh dokumentasi keamanan
- **Implementasi Praktis**: Menambahkan contoh kode terperinci dalam .NET, Java, dan Python dengan pola enterprise
- **Organisasi Sumber Daya**: Kategori komprehensif dokumentasi resmi, standar keamanan, dan panduan implementasi
- **Indikator Visual**: Penandaan jelas antara persyaratan wajib dan praktik yang direkomendasikan


#### Konsep Inti (01-CoreConcepts/) - Modernisasi Lengkap
- **Pembaruan Versi Protokol**: Diperbarui untuk merujuk Spesifikasi MCP 2025-06-18 dengan versi berbasis tanggal (format YYYY-MM-DD)
- **Penyempurnaan Arsitektur**: Deskripsi yang diperluas tentang Host, Client, dan Server sesuai pola arsitektur MCP saat ini
  - Host kini didefinisikan jelas sebagai aplikasi AI yang mengoordinasikan beberapa koneksi klien MCP
  - Klien dideskripsikan sebagai penghubung protokol yang mempertahankan hubungan satu-ke-satu dengan server
  - Server diperbarui dengan skenario penyebaran lokal vs. jarak jauh
- **Restrukturisasi Primitive**: Perombakan lengkap pada primitif server dan klien
  - Primitif Server: Sumber Daya (sumber data), Prompt (templat), Alat (fungsi eksekusi) dengan penjelasan dan contoh terperinci
  - Primitif Klien: Sampling (penyelesaian LLM), Elicitation (input pengguna), Logging (debugging/pemantauan)
  - Diperbarui dengan pola metode penemuan (`*/list`), pengambilan (`*/get`), dan eksekusi (`*/call`) saat ini
- **Arsitektur Protokol**: Memperkenalkan model arsitektur dua lapis
  - Lapisan Data: Fondasi JSON-RPC 2.0 dengan manajemen siklus hidup dan primitif
  - Lapisan Transportasi: STDIO (lokal) dan HTTP Streamable dengan SSE (jarak jauh) sebagai mekanisme transportasi
- **Kerangka Keamanan**: Prinsip keamanan komprehensif termasuk persetujuan eksplisit pengguna, perlindungan privasi data, keamanan eksekusi alat, dan keamanan lapisan transportasi
- **Pola Komunikasi**: Memperbarui pesan protokol untuk menampilkan inisialisasi, penemuan, eksekusi, dan aliran notifikasi
- **Contoh Kode**: Memperbarui contoh multi-bahasa (.NET, Java, Python, JavaScript) agar mencerminkan pola MCP SDK saat ini

#### Keamanan (02-Security/) - Pengawasan Keamanan Komprehensif  
- **Penyesuaian Standar**: Penyesuaian lengkap dengan persyaratan keamanan Spesifikasi MCP 2025-06-18
- **Evolusi Autentikasi**: Dokumentasi evolusi dari server OAuth kustom ke delegasi penyedia identitas eksternal (Microsoft Entra ID)
- **Analisis Ancaman Khusus AI**: Cakupan yang diperluas terhadap vektor serangan AI modern
  - Skenario serangan prompt injection terperinci dengan contoh dunia nyata
  - Mekanisme keracunan alat dan pola serangan "rug pull"
  - Keracunan jendela konteks dan serangan kebingungan model
- **Solusi Keamanan AI Microsoft**: Cakupan komprehensif ekosistem keamanan Microsoft
  - AI Prompt Shields dengan deteksi lanjutan, spotlighting, dan teknik delimiter
  - Pola integrasi Azure Content Safety
  - GitHub Advanced Security untuk perlindungan rantai pasokan
- **Mitigasi Ancaman Lanjutan**: Kontrol keamanan terperinci untuk
  - Pembajakan sesi dengan skenario serangan spesifik MCP dan persyaratan ID sesi kriptografi
  - Masalah Confused Deputy dalam skenario proxy MCP dengan persyaratan persetujuan eksplisit
  - Kerentanan token passthrough dengan kontrol validasi wajib
- **Keamanan Rantai Pasokan**: Perluasan cakupan rantai pasokan AI termasuk model fondasi, layanan embeddings, penyedia konteks, dan API pihak ketiga
- **Keamanan Fondasi**: Integrasi yang diperluas dengan pola keamanan enterprise termasuk arsitektur zero trust dan ekosistem keamanan Microsoft
- **Organisasi Sumber Daya**: Kategori tautan sumber daya komprehensif menurut tipe (Dokumentasi Resmi, Standar, Riset, Solusi Microsoft, Panduan Implementasi)

### Peningkatan Kualitas Dokumentasi
- **Tujuan Pembelajaran Terstruktur**: Peningkatan tujuan pembelajaran dengan hasil spesifik dan dapat ditindaklanjuti 
- **Referensi Silang**: Menambahkan tautan antar topik terkait keamanan dan konsep inti
- **Informasi Terbaru**: Memperbarui semua referensi tanggal dan tautan spesifikasi ke standar saat ini
- **Panduan Implementasi**: Menambahkan panduan implementasi spesifik dan dapat ditindaklanjuti di kedua bagian

## 16 Juli 2025

### Perbaikan README dan Navigasi
- Merancang ulang total navigasi kurikulum di README.md
- Mengganti tag `<details>` dengan format berbasis tabel yang lebih mudah diakses
- Membuat opsi tata letak alternatif di folder "alternative_layouts" baru
- Menambahkan contoh navigasi bergaya kartu, tab, dan akordion
- Memperbarui bagian struktur repositori untuk menyertakan semua file terbaru
- Meningkatkan bagian "Cara Menggunakan Kurikulum Ini" dengan rekomendasi yang jelas
- Memperbarui tautan spesifikasi MCP agar mengarah ke URL yang benar
- Menambahkan bagian Rekayasa Konteks (5.14) ke struktur kurikulum

### Pembaruan Panduan Studi
- Merevisi total panduan studi agar sesuai dengan struktur repositori saat ini
- Menambahkan bagian baru untuk MCP Clients dan Tools, dan Server MCP Populer
- Memperbarui Peta Kurikulum Visual agar mencerminkan semua topik dengan akurat
- Meningkatkan deskripsi Topik Lanjutan untuk mencakup semua area khusus
- Memperbarui bagian Studi Kasus agar mencerminkan contoh nyata
- Menambahkan changelog komprehensif ini

### Kontribusi Komunitas (06-CommunityContributions/)
- Menambahkan informasi terperinci tentang server MCP untuk pembuatan gambar
- Menambahkan bagian komprehensif tentang menggunakan Claude di VSCode
- Menambahkan petunjuk pengaturan dan penggunaan klien terminal Cline
- Memperbarui bagian klien MCP untuk memasukkan semua opsi klien populer
- Meningkatkan contoh kontribusi dengan sampel kode yang lebih akurat

### Topik Lanjutan (05-AdvancedTopics/)
- Mengorganisasi semua folder topik khusus dengan penamaan yang konsisten
- Menambahkan materi dan contoh rekayasa konteks
- Menambahkan dokumentasi integrasi agen Foundry
- Meningkatkan dokumentasi integrasi keamanan Entra ID

## 11 Juni 2025

### Pembuatan Awal
- Merilis versi pertama kurikulum MCP untuk Pemula
- Membuat struktur dasar untuk semua 10 bagian utama
- Menerapkan Peta Kurikulum Visual untuk navigasi
- Menambahkan proyek contoh awal dalam berbagai bahasa pemrograman

### Memulai (03-GettingStarted/)
- Membuat contoh implementasi server pertama
- Menambahkan panduan pengembangan klien
- Menyertakan instruksi integrasi klien LLM
- Menambahkan dokumentasi integrasi VS Code
- Menerapkan contoh server Server-Sent Events (SSE)

### Konsep Inti (01-CoreConcepts/)
- Menambahkan penjelasan terperinci tentang arsitektur klien-server
- Membuat dokumentasi komponen protokol kunci
- Mendokumentasikan pola pesan di MCP

## 23 Mei 2025

### Struktur Repositori
- Menginisialisasi repositori dengan struktur folder dasar
- Membuat file README untuk setiap bagian utama
- Menyiapkan infrastruktur terjemahan
- Menambahkan aset gambar dan diagram

### Dokumentasi
- Membuat README.md awal dengan gambaran kurikulum
- Menambahkan CODE_OF_CONDUCT.md dan SECURITY.md
- Menyiapkan SUPPORT.md dengan panduan mendapatkan bantuan
- Membuat struktur panduan studi awal

## 15 April 2025

### Perencanaan dan Kerangka Kerja
- Perencanaan awal untuk kurikulum MCP untuk Pemula
- Mendefinisikan tujuan pembelajaran dan audiens sasaran
- Menjabarkan struktur 10 bagian dari kurikulum
- Mengembangkan kerangka konseptual untuk contoh dan studi kasus
- Membuat contoh prototipe awal untuk konsep kunci

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->