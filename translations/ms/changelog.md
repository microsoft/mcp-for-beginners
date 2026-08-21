# Changelog: Kurikulum MCP untuk Pemula

Dokumen ini berfungsi sebagai rekod semua perubahan penting yang dibuat pada kurikulum Model Context Protocol (MCP) untuk Pemula. Perubahan didokumentasikan dalam urutan kronologi songsang (perubahan terbaru dahulu).

## 29 Julai, 2026

### Modul 08 Teman Baharu: Reliability Sidecars dan Safe Retries

Ditambahkan pelajaran teman vendor-neutral untuk alat MCP yang mencipta kesan dunia sebenar,
sejajar dengan spesifikasi akhir `2026-07-28`.

- **Baharu**: [pelajaran teman reliability sidecar][reliability-sidecar]
  menggunakan satu cerita tiket sokongan, dua rajah Mermaid, dan aliran
  keputusan cuba semula untuk menerangkan kunci operasi stabil, kemasukan pendua atom,
  reconciliations, bukti, dan sempadan sambungan Tasks.
- **Baharu**: Latihan suntikan kegagalan Python dan SQLite perpustakaan standard
  menggunakan simpanan operasi dan tiket berasingan untuk menunjukkan respons hilang
  selepas kesan luaran komit. Enam ujian deterministik merangkumi penduaan naif,
  pemulihan mulakan semula terjaga, konflik muatan, keputusan dalam cache,
  tuntutan aktif, dan kemasukan pendua serentak.
- **Dikemas kini**: Modul 08 kini memautkan pelajaran teman, mengenal pasti model
  permintaan tanpa keadaan `2026-07-28` akhir, membezakan observabiliti OpenTelemetry
  dari ciri logging MCP yang sudah lapuk, dan mengehadkan contoh cuba semula umum
  hanya untuk operasi baca sahaja.
- **Pilihan**: Pelajaran memetakan konsep mudah alihnya kepada satu pelaksanaan
  komuniti yang ditanda tanpa menjadikan perkhidmatan dihoskan atau panggilan
  rangkaian sebagai sebahagian latihan.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 Julai, 2026

### Pelajaran Baharu: Calon Rilis Spesifikasi MCP 2026-07-28

Ditambahkan liputan calon rilis spesifikasi MCP yang akan datang `2026-07-28` (diumumkan 21 Mei, 2026; rilis akhir dijadualkan 28 Julai, 2026), diringkaskan dari [pos blog pengumuman rasmi](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Garis asas kurikulum kekal **Spesifikasi MCP 2025-11-25** sehingga versi baru dihantar, jadi ini disampaikan sebagai panduan ke hadapan dan bukan sebagai penulisan semula pelajaran sedia ada.

- **Baharu**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — pelajaran lengkap yang meliputi teras protokol tanpa keadaan (penyingkiran jabat tangan `initialize` dan `Mcp-Session-Id`), pengepala penghalaan `Mcp-Method`/`Mcp-Name` baharu, metadata cache `ttlMs`/`cacheScope`, W3C Trace Context dalam `_meta`, rangka kerja rasmi Extensions (Aplikasi MCP dan sambungan Tasks baharu), enam SEP pengukuhan kebenaran, penghapusan Roots/Sampling/Logging, dan peralihan ke JSON Schema 2020-12 penuh untuk skema alat.
- **Dikemas kini** dengan penerangan hadapan yang memaut ke pelajaran baharu:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): nota versi protokol, bahagian Sampling/Roots/Logging/Tasks, dan "Apa seterusnya"

  - [02-Security/README.md](./02-Security/README.md): seruan pengukuhan kebenaran
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): seruan pengangkutan tanpa keadaan
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): Seruan penarikan balik Pensampelan
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): Seruan penarikan balik Logging dan peluasan Tugas
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): seruan pengangkutan tanpa keadaan/pemilihan sesi
  - [README.md](./README.md): nota "Melihat ke hadapan" dalam bahagian spesifikasi dan entri `1.1` baru dalam jadual modul kurikulum
  - [study_guide.md](./study_guide.md): peluru berwawasan ke hadapan di bawah gambaran Kes Impak Teras dan nota tambahan bertarikh
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): seruan pada peta pengangkutan `mcp-session-id` sebelum model permintaan tanpa keadaan
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): seruan gambaran modul tentang Penarikan Balik Konteks Akar/Pensampelan dan peluasan Tugas
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): seruan pengukuhan kebenaran

## 24 Jun 2026

### Pelajaran Baru: Menggunakan MCP dalam aplikasi Copilot

- [Bahagian Perkakas](./12-tooling/README.md) Ditambah bahagian perkakas.
- [MCP dalam aplikasi Copilot](./12-tooling/01-copilot-app/README.md)

## 16 Jun, 2026

### Penyerasian Spesifikasi MCP & Pengesahan Sampel

Telah mengesahkan kurikulum terhadap **Spesifikasi MCP 2025-11-25** yang terkini dan SDK rasmi terkini, kemudian membetulkan baki rujukan spesifikasi yang lapuk dan mengesahkan sampel teras masih boleh dibina dan dijalankan.

#### Pembetulan Versi Spesifikasi (2025-06-18 / 2025-03-26 → 2025-11-25)

Dikemas kini kandungan Bahasa Inggeris di mana ia masih mendakwa semakan spes lama adalah piawaian *terkini/terkini*, dan pautan ditukar ke laluan spes `modelcontextprotocol.io` kanonik:
- **05-AdvancedTopics/mcp-security/README.md**: Dikemas kini banner "Piawaian Semasa", pengenalan, tajuk prinsip keselamatan teras, tajuk keperluan mandatori, bahagian Microsoft Entra ID, pautan Rujukan & Sumber, dan notis keselamatan penutup (8 rujukan) ke 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Dikemas kini pautan sumber tambahan spes dan banner "Piawaian Semasa" ke 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Menggantikan pautan keselamatan-dan-kepercayaan `2025-03-26` yang lapuk dengan halaman amalan terbaik keselamatan 2025-11-25 terkini

- **03-GettingStarted/14-sampling/README.md**: Dikemas kini pautan doc sampling rasmi kepada 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: Dikemas kini rujukan "spesifikasi MCP semasa" dalam bentuk masa kini dan pautan spesifikasi Sumber Tambahan kepada 2025-11-25 (nota sejarah penghapusan SSE dibiarkan untuk ketepatan)

#### Contoh Pengesahan Terhadap SDK Terkini

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` berjaya menyelesaikan `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` lulus tanpa ralat jenis — API `McpServer`/`StdioServerTransport` yang sedia ada masih sah
- **Python (03-GettingStarted/01-first-server/solution/python)**: Disahkan dalam `.venv` terpencil dengan `mcp[cli]` (1.27.2); `py_compile` lulus dan `FastMCP.list_tools()` mengembalikan alat `add` dan `subtract` dengan betul
- Disahkan semua julat versi sampel `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) menyelesaikan dengan bersih kepada versi semasa `1.29.0` tanpa perubahan API yang memecahkan

#### Penyelarasan Pin Pergantungan (menutup jurang versi)

Menaik taraf pin SDK yang sudah lapuk supaya setiap sampel mengikuti siaran MCP semasa, memadankan konvensyen di seluruh repo:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Meningkatkan `@modelcontextprotocol/sdk` dari `^1.8.0` → `>=1.26.0` dan mengemas kini deskripsi pakej lapuk `"updated for MCP 2025-06-18"` kepada `"selaras dengan Spesifikasi MCP 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** dan **lab4/code/github_mcp_server/pyproject.toml**: Meningkatkan pin tepat `mcp==1.23.0` → `mcp>=1.26.0`; menjana semula kedua-dua fail `uv.lock` (`uv lock`) supaya fail kunci menyelesaikan kepada `mcp 1.27.2` semasa dan sentiasa seiring dengan manifes

#### Analisis Jurang Kurikulum — Liputan Ciri Spesifikasi Terkini

Disahkan kurikulum sudah meliputi semua primitif yang diperkenalkan/dikembangkan dalam MCP 2025-11-25, jadi tiada jurang kandungan:
- **Pengambilan Sampel**: Pelajaran 03-GettingStarted/14-sampling serta 05-AdvancedTopics/mcp-sampling
- **Pengeluar Maklumat (termasuk mod URL)**: Didokumentasikan dalam 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features
- **Akar**: Didokumentasikan dalam 00-Introduction, 01-CoreConcepts, dan 05-AdvancedTopics/mcp-root-contexts
- **Tugas (eksperimen, operasi jangka panjang)**: Didokumentasikan dalam 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features
- **Anotasi Alat** (`readOnlyHint` / `destructiveHint`): Didokumentasikan dalam 01-CoreConcepts dan 05-AdvancedTopics/mcp-protocol-features

### Pengukuhan Keselamatan & Pembetulan Kerentanan Pergantungan

Menjalankan pemeriksaan keselamatan penuh ke atas setiap manifes pergantungan dan kod sumber sampel, kemudian membaiki semua amaran npm yang dilaporkan dan satu penemuan di peringkat kod. Selepas pembetulan, `npm audit` melaporkan **0 kerentanan** dalam setiap direktori yang diaudit.

#### Kerentanan Pergantungan npm (transitif) — Dibaiki

Diaudit ke semua 15 fail `package-lock.json` yang dikomit. Kerentanan terhad kepada pergantungan transitif yang dibawa oleh alat dev MCP Inspector, klien OpenAI, dan MCP SDK; semua kini diselesaikan tanpa memecahkan sampel:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** dan **lab3/code/weather_mcp/inspector**: Meningkatkan `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), yang membersihkan amaran berbungkus `ajv`, `brace-expansion`, `diff`, `path-to-regexp` dan `ws`. Menambah entri `overrides` npm memaksa `shell-quote@1.8.4` yang telah tampal untuk menghapuskan amaran kritikal tinggal yang dibawa oleh `concurrently`; menjana semula kedua-dua fail kunci (kini 0 kerentanan)
- **03-GettingStarted/samples/typescript**: `npm audit fix` mengemas kini `qs` transitif (moderat) ke pelepasan yang ditampal
- **03-GettingStarted/samples/javascript**: `npm audit fix` mengemas kini `hono` transitif (moderat) ke pelepasan yang ditampal
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` mengemas kini `form-data` transitif (tinggi) ke pelepasan yang ditampal
- **03-GettingStarted/11-simple-auth/solution/typescript**: Menjana `package-lock.json` yang hilang supaya projek boleh dihasilkan semula dan diaudit (0 kerentanan)

#### Pembetulan Keselamatan di Peringkat Kod (OWASP A03: Injection)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Mengeluarkan `shell=True` dari alat `open_in_vscode`. `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` sebelumnya membenarkan metakarakter shell dalam laluan folder ditafsirkan oleh `cmd.exe` (vektor serangan suntikan perintah). Kini ia melancarkan `Code.exe` yang telah diselesaikan secara langsung dengan folder sebagai hujah — tanpa shell — yang secara fungsinya setara dan selamat

#### Audit Pergantungan Python

- Diaudit setiap set keperluan Python dengan `pip-audit`. `05-AdvancedTopics` dan `03-GettingStarted/samples/python` melaporkan **tiada kerentanan diketahui** (julatan `mcp` / `httpx` / `pydantic` / `python-dotenv` mereka menyelesaikan kepada pelepasan tampal semasa)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` menandakan pergantungan transitif **`werkzeug` 3.1.1** dengan tiga amaran DoS nama peranti Windows `safe_join` — `CVE-2025-66221`, `CVE-2026-21860`, dan `CVE-2026-27199` (semuanya dibetulkan dalam 3.1.6). Menambah pin keselamatan eksplisit `werkzeug>=3.1.6` supaya pelepasan tampal diselesaikan; mengesahkan sekatan menyelesaikan dengan bersih bersama tumpukan `chainlit` / `mcp` / `semantic-kernel`

### Penjenamaan Semula Nama Produk

Dikemas kini semua kandungan kurikulum untuk mencerminkan penjenamaan semula produk Microsoft:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Dikemas kini pautan komuniti Discord

- **AGENTS.md**: Rujukan pelayan Discord dikemas kini
- **README.md**: Rujukan ekosistem teknologi dikemas kini
- **study_guide.md**: Rujukan kajian kes dikemas kini
- **05-AdvancedTopics/README.md**: Tajuk dan penerangan Modul 5.13 dikemas kini
- **05-AdvancedTopics/mcp-integration/README.md**: Tajuk seksyen dan penerangan dikemas kini
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Tajuk modul penuh dan kandungan dikemas kini
- **05-AdvancedTopics/mcp-security-entra/README.md**: Pautan silang rujukan dikemas kini
- **07-LessonsfromEarlyAdoption/README.md**: Rujukan kajian kes dikemas kini
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Tajuk Seksyen 9, lencana, dan keupayaan dikemas kini
- **08-BestPractices/README.md**: Pautan komuniti Discord dikemas kini
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Rujukan saluran Discord dikemas kini
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Rujukan penghantaran model dikemas kini
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Jadual Perkhidmatan AI dikemas kini
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Rujukan sumber dikemas kini

#### AI Toolkit / AITK → Sambungan Microsoft Foundry Toolkit untuk VS Code
- **README.md**: Rujukan kurikulum utama dikemas kini
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Tajuk modul, gambaran keseluruhan, dan semua tajuk modul dikemas kini
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Tajuk, objektif pembelajaran, arahan persediaan, dan sumber dikemas kini
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Tajuk, objektif pembelajaran, jadual hos MCP, dan silang rujukan dikemas kini
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Tajuk, lencana, prasyarat, dan sumber dikemas kini
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Rujukan Pembina Ejen dan pautan maklum balas dikemas kini
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Prasyarat dan rujukan sambungan dikemas kini

---

## 11 April 2026

### Pelajaran Baru, Pembetulan Dokumentasi, dan Kemas Kini Pergantungan

#### Kandungan Kurikulum Baru Ditambah

**Modul 05 - Topik Lanjutan**
- **Pelajaran 5.17: Penalaran Multi-Ejen Berlawanan dengan MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Panduan menyeluruh baru yang merangkumi pola perdebatan berlawanan untuk sistem multi-ejen
  - Diagram seni bina Mermaid: dua agen → pelayan MCP kongsi → transkrip perdebatan → hakim → keputusan
  - Pelayan alat MCP kongsi (`web_search` + `run_python`) dilaksanakan dalam Python dan TypeScript
  - Prompt sistem bertentangan (UNTUK / MENENTANG / Hakim) dengan keperluan penggunaan alat yang jelas
  - Pengatur perdebatan dalam Python, TypeScript, dan C# menguruskan pusingan dan menghala hujah
  - Pendawaian `ClientSession` MCP untuk pengatur kepada panggilan alat sebenar
  - Jadual kes penggunaan (pengesanan halusinasi, pemodelan ancaman, semakan reka bentuk API, pengesahan fakta, pemilihan teknologi)
  - Pertimbangan keselamatan: pelaksanaan berpasir, pengesahan panggilan alat, pengehad kadar, log audit
  - Latihan berstruktur dengan tiga senario praktikal (semakan kod, keputusan seni bina, pengawalan kandungan)

#### Pembetulan Dokumentasi

**Modul 03 - Memulakan**
- **05-stdio-server/README.md**: Betulkan contoh pelayan stdio TypeScript yang tidak lengkap — tambah penciptaan pengangkutan yang hilang (`new StdioServerTransport()`) dan panggilan `server.connect(transport)` untuk padankan contoh Python dan .NET dalam seksyen yang sama
- **14-sampling/README.md**: Betulkan ralat taip — betulkan `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Kemas Kini Kurikulum

**README.md utama**
- Tambah entri 5.17 (Penalaran Multi-Ejen Berlawanan dengan MCP) ke jadual kurikulum dengan pautan langsung ke pelajaran baru

**05-AdvancedTopics/README.md**
- Tambah baris Pelajaran 5.17 ke jadual pelajaran

**study_guide.md**
- Tambah topik Penalaran Multi-Ejen Berlawanan ke peta minda dan penerangan naratif Topik Lanjutan

#### Pembetulan Kod dan Keselamatan

**Modul 05 - Ejen Berlawanan (`mcp-adversarial-agents`)**
- **Pembetulan keselamatan — suntikan arahan**: Gantikan interpolasi shell `execSync` dengan `execFile` + `promisify` dalam alat TypeScript `run_python`, menghapuskan permukaan suntikan arahan (kod dikawal LLM kini dihantar sebagai elemen argv literal tanpa penglibatan shell)
- **Pendawaian gelung alat MCP**: Kemas kini pengatur perdebatan Python untuk menggunakan klien `AsyncAnthropic` (menggantikan `Anthropic` sync blok), menghantar `ClientSession` langsung yang hidup ke setiap giliran agen, mendapatkan definisi alat melalui `session.list_tools()` setiap giliran, dan menghantar blok `tool_use` melalui `session.call_tool()` dalam gelung sehingga model mengeluarkan respon teks akhir

#### Kemas Kini Pergantungan

- Naik taraf `hono` ke 4.12.12 merentasi berbilang pakej (03-Memulakan, 04-Pelaksanaan Praktikal, 10-Pelarasan Aliran Kerja AI)
- Naik taraf `@hono/node-server` dari 1.19.11 ke 1.19.13 dalam pakej TypeScript
- Naik taraf `cryptography` dari 46.0.5 ke 46.0.7 dalam pakej Python (makmal 10-Pelarasan Aliran Kerja AI 3 dan 4)
- Naik taraf `lodash` dari 4.17.23 ke 4.18.1 dalam pemeriksa 10-Pelarasan Aliran Kerja AI

#### Terjemahan

- Selaraskan terjemahan untuk 48+ bahasa dengan perubahan sumber terkini (kemas kini i18n)

---

## 5 Februari 2026

### Peningkatan Pengesahan dan Navigasi Sepanjang Repositori

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
  - Alat ujian, sumber, dan aliran kerja prompt
  - Integrasi VS Code dengan MCP Inspector
  - Senario penyahpepijatan biasa dengan penyelesaian

**Modul 04 - Pelaksanaan Praktikal**
- **pagination/README.md**: Panduan pelaksanaan penomboran halaman baru
  - Corak penomboran berasaskan kursor dalam Python, TypeScript, Java
  - Pengendalian penomboran halaman sisi klien
  - Strategi reka bentuk kursor (kabur vs berstruktur)
  - Cadangan pengoptimuman prestasi

**Modul 05 - Topik Lanjutan**
- **mcp-protocol-features/README.md**: Pendalaman ciri protokol baru
  - Pelaksanaan notifikasi kemajuan
  - Corak pembatalan permintaan
  - Templat sumber dengan corak URI
  - Pengurusan kitaran hayat pelayan
  - Kawalan tahap log
  - Corak pengendalian ralat dengan kod JSON-RPC

#### Pembetulan Navigasi (24+ fail dikemas kini)

**README Modul Utama**
 Kini pautkan kepada pelajaran pertama DAN modul seterusnya

**Sub-fail Keselamatan 02**
- Semua 5 dokumen keselamatan tambahan kini ada navigasi "Apa Seterusnya":

**Fail Kajian Kes 09**
- Semua fail kajian kes kini ada navigasi berurutan:

**Makmal 10-Pelarasan AI**
Tambah seksyen Apa Seterusnya pada gambaran keseluruhan Modul 10 dan Modul 11

#### Pembetulan Kod dan Kandungan

**Kemas Kini SDK dan Pergantungan**
Betulkan versi openai kosong kepada `^4.95.0`
Kemas kini SDK dari `^1.8.0` ke `>=1.26.0`
Kemas kini pin versi mcp ke `>=1.26.0`

**Pembetulan Kod**
Betulkan model tidak sah `gpt-4o-mini` kepada `gpt-4.1-mini`

**Pembetulan Kandungan**
Betulkan pautan rosak `READMEmd` → `README.md`, betulkan tajuk kurikulum `Module 1-3` → `Module 0-3`, betulkan laluan sensitif huruf
Buang kandungan duplikat kajian kes 5 yang rosak

**Peningkatan Panduan untuk Pemula**
Tambah pengenalan yang betul, objektif pembelajaran, dan prasyarat untuk pemula

#### Kemas Kini Kurikulum

**README.md Utama**
- Tambah entri 3.12 (Hos MCP), 3.13 (Pemeriksa MCP), 4.1 (Penomboran), 5.16 (Ciri Protokol) ke jadual kurikulum

**README Modul**
Tambah pelajaran 12 dan 13 ke senarai pelajaran
Tambah seksyen Panduan Praktikal dengan pautan penomboran
Tambah pelajaran 5.15 (Pengangkutan Tersuai) dan 5.16 (Ciri Protokol)

**study_guide.md**
- Kemas kini peta minda dengan semua topik baru: Persediaan Hos MCP, Pemeriksa MCP, Strategi Penomboran, Pendalaman Ciri Protokol

## 28 Jan 2026

### Semakan Pematuhan Spesifikasi MCP 2025-11-25

#### Peningkatan Konsep Teras (01-CoreConcepts/)
- **Primitif Pelanggan Baru - Roots**: Tambah dokumentasi menyeluruh tentang primitif pelanggan Roots, membolehkan pelayan memahami sempadan sistem fail dan kebenaran akses
- **Anotasi Alat**: Tambah dokumentasi tentang anotasi tingkah laku alat (`readOnlyHint`, `destructiveHint`) untuk keputusan pelaksanaan alat yang lebih baik
- **Panggilan Alat dalam Sampling**: Kemas kini dokumentasi Sampling untuk termasuk parameter `tools` dan `toolChoice` bagi pemanggilan alat dipacu model semasa permintaan sampling
- **Elicitation Mod URL**: Tambah dokumentasi tentang elicitation berasaskan URL untuk interaksi web luaran yang dimulakan pelayan
- **Tugas (Eksperimen)**: Tambah seksyen baru yang mendokumentasikan ciri Eksperimen Tugas untuk pembalut pelaksanaan tahan lama dan pengambilan hasil ditangguhkan
- **Sokongan Ikon**: Catatkan bahawa alat, sumber, templat sumber, dan prompt kini boleh merangkumi ikon sebagai metadata tambahan

#### Kemas Kini Dokumentasi
- **README.md**: Tambah rujukan versi Spesifikasi MCP 2025-11-25 dan penjelasan penversian berdasarkan tarikh
- **study_guide.md**: Kemas kini peta kurikulum untuk memasukkan Tugas dan Anotasi Alat dalam seksyen Konsep Teras; kemas kini cap masa dokumen

#### Pengesahan Pematuhan Spesifikasi
- **Versi Protokol**: Sahkan semua dokumentasi merujuk Spesifikasi MCP 2025-11-25 terkini
- **Penyesuaian Seni Bina**: Sahkan ketepatan dokumentasi seni bina dua lapisan (Lapisan Data + Lapisan Pengangkutan)
- **Dokumentasi Primitif**: Sahkan primitif pelayan (Sumber, Prompt, Alat) dan primitif pelanggan (Sampling, Elicitation, Logging, Roots)
- **Mekanisme Pengangkutan**: Sahkan ketepatan dokumentasi pengangkutan STDIO dan Streamable HTTP
- **Panduan Keselamatan**: Sahkan penyesuaian dengan dokumentasi Amalan Terbaik Keselamatan MCP terkini

#### Ciri Utama MCP 2025-11-25 Didokumentasikan
- **Penemuan OpenID Connect**: Penemuan pelayan pengesahan melalui OIDC
- **Dokumen Metadata ID Klien OAuth**: Mekanisme pendaftaran klien yang disyorkan
- **JSON Schema 2020-12**: Dialek lalai untuk definisi skema MCP
- **Sistem Tahap SDK**: Formalisasi keperluan sokongan dan penyelenggaraan ciri SDK
- **Struktur Tadbir Urus**: Formalisasi Kumpulan Kerja dan Kumpulan Kepentingan dalam tadbir urus MCP

### Kemas Kini Besar Dokumentasi Keselamatan (02-Security/)

#### Integrasi Bengkel MCP Security Summit (Sherpa)
- **Sumber Latihan Amali Baru**: Tambah integrasi menyeluruh dengan [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) di seluruh dokumentasi keselamatan
- **Liputan Laluan Ekspedisi**: Dokumentasi kemajuan penuh kem ke kem dari Base Camp ke Summit
- **Penyesuaian OWASP**: Semua panduan keselamatan kini memetakan risiko Panduan Keselamatan Azure OWASP MCP

#### Integrasi OWASP MCP Top 10
- **Seksian Baru**: Tambah jadual Risiko Keselamatan OWASP MCP Top 10 dengan mitigasi Azure ke README Keselamatan utama
- **Dokumentasi Berasaskan Risiko**: Kemas kini mcp-security-controls-2025.md dengan rujukan risiko OWASP MCP untuk setiap domain keselamatan
- **Seni Bina Rujukan**: Pautan kepada seni bina rujukan dan corak pelaksanaan Panduan Keselamatan Azure OWASP MCP

#### Fail Keselamatan Dikemas Kini
- **README.md**: Tambah gambaran keseluruhan Bengkel Sherpa, jadual laluan ekspedisi, ringkasan risiko OWASP MCP Top 10, dan seksyen latihan amali
- **mcp-security-controls-2025.md**: Kemas kini tajuk ke Februari 2026, tambah rujukan risiko OWASP (MCP01-MCP08), baiki ketidakseragaman versi spesifikasi
- **mcp-security-best-practices-2025.md**: Tambah seksyen sumber Sherpa dan OWASP, kemas kini cap masa
- **mcp-best-practices.md**: Tambah seksyen latihan amali dengan pautan Sherpa dan OWASP
- **azure-content-safety-implementation.md**: Tambah rujukan OWASP MCP06, penjajaran Sherpa Camp 3, dan seksyen sumber tambahan

#### Pautan Sumber Baru Ditambah
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)

- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Laman risiko OWASP MCP individu (MCP01-MCP10)

### Penyesuaian Spesifikasi MCP Menyeluruh Kurikulum 2025-11-25

#### Modul 03 - Memulakan
- **Dokumentasi SDK**: Menambah Go SDK ke dalam senarai SDK rasmi; mengemas kini semua rujukan SDK untuk menyelaraskan dengan Spesifikasi MCP 2025-11-25
- **Penjelasan Pengangkutan**: Mengemas kini penerangan pengangkutan STDIO dan HTTP Streaming dengan rujukan spesifikasi yang jelas

#### Modul 04 - Pelaksanaan Praktikal
- **Kemas Kini SDK**: Menambah Go SDK; mengemas kini senarai SDK dengan rujukan versi spesifikasi
- **Spesifikasi Kebenaran**: Mengemas kini pautan spesifikasi MCP Authorization ke versi terkini 2025-11-25

#### Modul 05 - Topik Lanjutan
- **Ciri Baru**: Menambah nota mengenai ciri baru Spesifikasi MCP 2025-11-25 (Tugas, Anotasi Alat, Elicitation Mod URL, Akar)
- **Sumber Keselamatan**: Menambah pautan OWASP MCP Top 10 dan bengkel Sherpa ke rujukan tambahan

#### Modul 06 - Sumbangan Komuniti
- **Senarai SDK**: Menambah Swift dan Rust SDK; mengemas kini pautan spesifikasi ke 2025-11-25
- **Rujukan Spesifikasi**: Mengemas kini pautan Spesifikasi MCP ke URL spesifikasi langsung

#### Modul 07 - Pengajaran dari Penggunaan Awal
- **Kemas Kini Sumber**: Menambah pautan Spesifikasi MCP 2025-11-25 dan OWASP MCP Top 10 ke sumber tambahan

#### Modul 08 - Amalan Terbaik
- **Versi Spesifikasi**: Mengemas kini rujukan Spesifikasi MCP ke 2025-11-25
- **Sumber Keselamatan**: Menambah OWASP MCP Top 10 dan bengkel Sherpa ke rujukan tambahan

#### Modul 10 - Melancarkan Aliran Kerja AI
- **Kemas Kini Lencana**: Menukar lencana versi MCP daripada versi SDK (1.9.3) kepada versi spesifikasi (2025-11-25)
- **Pautan Sumber**: Mengemas kini pautan Spesifikasi MCP; menambah OWASP MCP Top 10

#### Modul 11 - Makmal Praktikal Pelayan MCP
- **Rujukan Spesifikasi**: Mengemas kini pautan Spesifikasi MCP ke versi 2025-11-25
- **Sumber Keselamatan**: Menambah OWASP MCP Top 10 ke sumber rasmi

## 18 Disember 2025

### Kemas Kini Dokumentasi Keselamatan - Spesifikasi MCP 2025-11-25

#### Amalan Terbaik Keselamatan MCP (02-Security/mcp-best-practices.md) - Kemas Kini Versi Spesifikasi
- **Kemas Kini Versi Protokol**: Dikemas kini untuk merujuk Spesifikasi MCP terkini 2025-11-25 (dikeluarkan 25 November 2025)
  - Dikemas kini semua rujukan versi spesifikasi dari 2025-06-18 ke 2025-11-25
  - Dikemas kini rujukan tarikh dokumen dari 18 Ogos 2025 ke 18 Disember 2025
  - Disahkan semua URL spesifikasi merujuk dokumentasi semasa
- **Pengesahan Kandungan**: Pengesahan menyeluruh amalan keselamatan terbaik mengikut piawaian terkini
  - **Penyelesaian Keselamatan Microsoft**: Disahkan istilah dan pautan terkini untuk Prompt Shields (dahulu "Pengesanan risiko Jailbreak"), Azure Content Safety, Microsoft Entra ID, dan Azure Key Vault
  - **Keselamatan OAuth 2.1**: Disahkan penyelarasan dengan amalan keselamatan OAuth terkini
  - **Piawaian OWASP**: Disahkan rujukan OWASP Top 10 untuk LLM kekal terkini
  - **Perkhidmatan Azure**: Disahkan semua pautan dokumentasi Microsoft Azure dan amalan terbaik
- **Penyelarasan Piawaian**: Semua piawaian keselamatan yang dirujuk disahkan terkini
  - Rangka Kerja Pengurusan Risiko AI NIST
  - ISO 27001:2022
  - Amalan Terbaik Keselamatan OAuth 2.1
  - Rangka kerja keselamatan dan pematuhan Azure
- **Sumber Pelaksanaan**: Disahkan semua pautan panduan pelaksanaan dan sumber
  - Corak pengesahan Azure API Management
  - Panduan integrasi Microsoft Entra ID
  - Pengurusan rahsia Azure Key Vault
  - Saluran DevSecOps dan penyelesaian pemantauan

### Jaminan Kualiti Dokumentasi
- **Pematuhan Spesifikasi**: Memastikan semua keperluan keselamatan MCP wajib (MESTI/TIDAK MESTI) selaras dengan spesifikasi terkini
- **Kesegaran Sumber**: Disahkan semua pautan luaran kepada dokumentasi Microsoft, piawaian keselamatan, dan panduan pelaksanaan
- **Liputan Amalan Terbaik**: Disahkan liputan menyeluruh tentang pengesahan, kebenaran, ancaman khusus AI, keselamatan rantaian bekalan, dan corak perusahaan

## 6 Oktober 2025

### Pengembangan Bahagian Memulakan – Penggunaan Pelayan Lanjutan & Pengesahan Mudah

#### Penggunaan Pelayan Lanjutan (03-GettingStarted/10-advanced)
- **Bab Baru Ditambah**: Memperkenalkan panduan komprehensif penggunaan pelayan MCP lanjutan, merangkumi seni bina pelayan biasa dan tahap rendah.
  - **Pelayan Biasa vs. Tahap Rendah**: Perbandingan terperinci dan contoh kod dalam Python dan TypeScript untuk kedua-dua pendekatan.
  - **Reka Bentuk Berasaskan Pengendali**: Penjelasan mengenai pengurusan alat/sumber/prompt berasaskan pengendali untuk pelaksanaan pelayan yang boleh diskala dan fleksibel.
  - **Corak Praktikal**: Senario dunia sebenar di mana corak pelayan tahap rendah berguna untuk ciri dan seni bina lanjutan.

#### Pengesahan Mudah (03-GettingStarted/11-simple-auth)
- **Bab Baru Ditambah**: Panduan langkah demi langkah untuk melaksanakan pengesahan mudah dalam pelayan MCP.
  - **Konsep Auth**: Penjelasan jelas mengenai pengesahan berbanding kebenaran, dan pengendalian kelayakan.
  - **Pelaksanaan Auth Asas**: Corak pengesahan berasaskan middleware dalam Python (Starlette) dan TypeScript (Express), dengan contoh kod.
  - **Perkembangan ke Keselamatan Lanjutan**: Panduan bermula dengan auth mudah dan maju ke OAuth 2.1 dan RBAC, dengan rujukan kepada modul keselamatan lanjutan.

Penambahan ini menyediakan panduan praktikal dan langsung untuk membina pelaksanaan pelayan MCP yang lebih kukuh, selamat, dan fleksibel, merapatkan konsep asas dengan corak pengeluaran lanjutan.

## 29 September 2025

### Makmal Integrasi Pangkalan Data Pelayan MCP - Jalur Pembelajaran Praktikal Menyeluruh

#### 11-MCPServerHandsOnLabs - Kurikulum Integrasi Pangkalan Data Lengkap Baru
- **Jalur Pembelajaran 13-Makmal Lengkap**: Menambah kurikulum praktikal menyeluruh untuk membina pelayan MCP sedia produksi dengan integrasi pangkalan data PostgreSQL
  - **Pelaksanaan Dunia Sebenar**: Kes penggunaan analitik Zava Retail menunjukkan corak tahap perusahaan
  - **Progression Pembelajaran Berstruktur**:
    - **Makmal 00-03: Asas** - Pengenalan, Seni Bina Teras, Keselamatan & Multi-Penyewa, Persediaan Persekitaran
    - **Makmal 04-06: Membina Pelayan MCP** - Reka Bentuk & Skema Pangkalan Data, Pelaksanaan Pelayan MCP, Pembangunan Alat
    - **Makmal 07-09: Ciri Lanjutan** - Integrasi Carian Semantik, Ujian & Penyenaraian, Integrasi VS Code
    - **Makmal 10-12: Pengeluaran & Amalan Terbaik** - Strategi Penyebaran, Pemantauan & Kebolehlihatan, Amalan Terbaik & Pengoptimuman
  - **Teknologi Perusahaan**: Rangka kerja FastMCP, PostgreSQL dengan pgvector, penanam Azure OpenAI, Azure Container Apps, Application Insights
  - **Ciri Lanjutan**: Keselamatan Tahap Baris (RLS), carian semantik, akses data multi-penyewa, penanam vektor, pemantauan masa nyata

#### Penyeragaman Terminologi - Penukaran Modul ke Makmal
- **Kemas Kini Dokumentasi Menyeluruh**: Mengemas kini semua fail README di 11-MCPServerHandsOnLabs untuk menggunakan terminologi "Makmal" menggantikan "Modul"
  - **Tajuk Seksyen**: Mengemas kini "Apa Yang Modul Ini Selenggara" kepada "Apa Yang Makmal Ini Selenggara" di semua 13 makmal
  - **Penerangan Kandungan**: Mengubah "Modul ini menyediakan..." kepada "Makmal ini menyediakan..." di seluruh dokumentasi
  - **Objektif Pembelajaran**: Mengemas kini "Menjelang akhir modul ini..." kepada "Menjelang akhir makmal ini..."
  - **Pautan Navigasi**: Menukarkan semua rujukan "Modul XX:" kepada "Makmal XX:" dalam rujukan silang dan navigasi
  - **Penjejakan Penyelesaian**: Mengemas kini "Selepas menyelesaikan modul ini..." kepada "Selepas menyelesaikan makmal ini..."
  - **Rujukan Teknikal Terpelihara**: Mengekalkan rujukan modul Python dalam fail konfigurasi (cth., `"module": "mcp_server.main"`)

#### Penambahbaikan Panduan Kajian (study_guide.md)
- **Peta Kurikulum Visual**: Menambah bahagian baru "11. Makmal Integrasi Pangkalan Data" dengan visualisasi struktur makmal komprehensif
- **Struktur Repositori**: Dikemas kini daripada sepuluh kepada sebelas seksyen utama dengan penerangan terperinci 11-MCPServerHandsOnLabs
- **Panduan Jalur Pembelajaran**: Ditingkatkan arahan navigasi untuk meliputi seksyen 00-11
- **Liputan Teknologi**: Menambah maklumat FastMCP, PostgreSQL, integrasi perkhidmatan Azure
- **Hasil Pembelajaran**: Menekankan pembangunan pelayan sedia produksi, corak integrasi pangkalan data, dan keselamatan perusahaan

#### Penambahbaikan Struktur README Utama
- **Terminologi Berasaskan Makmal**: Mengemas kini README.md utama dalam 11-MCPServerHandsOnLabs untuk sentiasa menggunakan struktur "Makmal"
- **Organisasi Jalur Pembelajaran**: Progresi jelas daripada konsep asas melalui pelaksanaan lanjutan ke penyebaran produksi
- **Fokus Dunia Sebenar**: Penekanan pembelajaran praktikal, langsung dengan corak dan teknologi kelas perusahaan

### Penambahbaikan Kualiti & Konsistensi Dokumentasi
- **Penekanan Pembelajaran Praktikal**: Memperkuat pendekatan berasaskan makmal di seluruh dokumentasi
- **Fokus Corak Perusahaan**: Menonjolkan pelaksanaan sedia produksi dan pertimbangan keselamatan perusahaan
- **Integrasi Teknologi**: Liputan komprehensif perkhidmatan Azure moden dan corak integrasi AI
- **Progresi Pembelajaran**: Laluan terstruktur dan jelas daripada konsep asas ke penyebaran produksi

## 26 September 2025

### Penambahbaikan Kajian Kes - Integrasi Daftar MCP GitHub

#### Kajian Kes (09-CaseStudy/) - Fokus Pembangunan Ekosistem
- **README.md**: Pengembangan utama dengan kajian kes Daftar MCP GitHub menyeluruh
  - **Kajian Kes Daftar MCP GitHub**: Kajian kes komprehensif baru meneliti pelancaran Daftar MCP GitHub pada September 2025
    - **Analisis Masalah**: Pemeriksaan terperinci cabaran penemuan pelayan MCP yang terpecah dan penyebaran
    - **Seni Bina Penyelesaian**: Pendekatan daftar terpusat GitHub dengan pemasangan VS Code satu klik
    - **Impak Perniagaan**: Peningkatan yang diukur dalam penerimaan pembangun dan produktiviti
    - **Nilai Strategik**: Fokus pada penyebaran agen modular dan interoperabiliti antara alat
    - **Pembangunan Ekosistem**: Penempatan sebagai platform asas untuk integrasi agen
  - **Struktur Kajian Kes Ditingkatkan**: Mengemas kini semua tujuh kajian kes dengan format konsisten dan penerangan menyeluruh
    - Ejen Perjalanan AI Azure: Penekanan orkestrasi multi-agen
    - Integrasi Azure DevOps: Fokus automasi aliran kerja
    - Pengambilan Dokumentasi Masa Nyata: Pelaksanaan klien konsol Python
    - Penjana Pelan Kajian Interaktif: Aplikasi web perbualan Chainlit
    - Dokumentasi Dalam Editor: Integrasi VS Code dan GitHub Copilot
    - Azure API Management: Corak integrasi API perusahaan
    - Daftar MCP GitHub: Pembangunan ekosistem dan platform komuniti
  - **Kesimpulan Komprehensif**: Bahagian kesimpulan ditulis semula menyorot tujuh kajian kes merangkumi pelbagai dimensi pelaksanaan MCP
    - Integrasi Perusahaan, Orkestrasi Multi-Agen, Produktiviti Pembangun
    - Pembangunan Ekosistem, Pengelasan Aplikasi Pendidikan
    - Wawasan ditambah ke dalam corak seni bina, strategi pelaksanaan, dan amalan terbaik
    - Penekanan pada MCP sebagai protokol matang dan sedia produksi

#### Kemas Kini Panduan Kajian (study_guide.md)
- **Peta Kurikulum Visual**: Dikemas kini peta minda untuk memasukkan Daftar MCP GitHub dalam bahagian Kajian Kes
- **Penerangan Kajian Kes**: Ditingkatkan daripada penerangan umum kepada pecahan terperinci tujuh kajian kes komprehensif
- **Struktur Repositori**: Dikemas kini seksyen 10 untuk mencerminkan liputan kajian kes komprehensif dengan butiran pelaksanaan khusus
- **Integrasi Log Perubahan**: Ditambah entri 26 September 2025 mendokumentasikan penambahan Daftar MCP GitHub dan penambahbaikan kajian kes
- **Kemas Kini Tarikh**: Dikemas kini cap masa kaki halaman kepada semakan terkini (26 September 2025)

### Penambahbaikan Kualiti Dokumentasi
- **Peningkatan Konsistensi**: Memperkemas format kajian kes dan struktur di semua tujuh contoh
- **Liputan Komprehensif**: Kajian kes kini meliputi perusahaan, produktiviti pembangun, dan senario pembangunan ekosistem
- **Penempatan Strategik**: Memperkuat fokus MCP sebagai platform asas untuk penyebaran sistem agen
- **Integrasi Sumber**: Dikemas kini sumber tambahan untuk merangkumi pautan Daftar MCP GitHub

## 15 September 2025

### Pengembangan Topik Lanjutan - Pengangkutan Tersuai & Kejuruteraan Konteks

#### Pengangkutan Tersuai MCP (05-AdvancedTopics/mcp-transport/) - Panduan Pelaksanaan Lanjutan Baru
- **README.md**: Panduan pelaksanaan lengkap untuk mekanisme pengangkutan tersuai MCP
  - **Pengangkutan Azure Event Grid**: Pelaksanaan pengangkutan berasaskan peristiwa tanpa pelayan yang komprehensif
    - Contoh C#, TypeScript, dan Python dengan integrasi Azure Functions
    - Corak seni bina berasaskan peristiwa untuk penyelesaian MCP boleh diskala
    - Penerima webhook dan pengendalian mesej berasaskan push
  - **Pengangkutan Azure Event Hubs**: Pelaksanaan pengangkutan streaming berkelajuan tinggi
    - Keupayaan streaming masa nyata untuk senario latensi rendah
    - Strategi pembahagian dan pengurusan checkpoint
    - Pengumpulan mesej dan pengoptimuman prestasi
  - **Corak Integrasi Perusahaan**: Contoh seni bina sedia produksi
    - Pemprosesan MCP diedar merentasi pelbagai Azure Functions
    - Seni bina pengangkutan hibrid menggabungkan pelbagai jenis pengangkutan
    - Ketahanan mesej, kebolehpercayaan, dan strategi pengendalian ralat
  - **Keselamatan & Pemantauan**: Integrasi Azure Key Vault dan corak kebolehlihatan
    - Pengesahan identiti terurus dan akses keistimewaan minimum
    - Telemetri Application Insights dan pemantauan prestasi
    - Pemutus litar dan corak ketahanan kesilapan
  - **Rangka Kerja Ujian**: Strategi pengujian komprehensif untuk pengangkutan tersuai
    - Ujian unit dengan test doubles dan rangka kerja mocking
    - Ujian integrasi dengan Azure Test Containers
    - Pertimbangan ujian prestasi dan beban

#### Kejuruteraan Konteks (05-AdvancedTopics/mcp-contextengineering/) - Disiplin AI yang Muncul
- **README.md**: Eksplorasi komprehensif kejuruteraan konteks sebagai bidang yang muncul
  - **Prinsip Teras**: Perkongsian konteks lengkap, kesedaran keputusan tindakan, dan pengurusan tetingkap konteks

  - **Penjajaran Protokol MCP**: Bagaimana reka bentuk MCP menangani cabaran kejuruteraan konteks
    - Had tetingkap konteks dan strategi pemuatan progresif
    - Penentuan kaitan dan pengambilan konteks dinamik
    - Pengendalian konteks pelbagai mod dan pertimbangan keselamatan
  - **Pendekatan Pelaksanaan**: Senibina berutas tunggal vs multi-ejen
    - Teknik pemecahan dan pengutamaan konteks
    - Strategi pemuatan konteks progresif dan pemampatan
    - Pendekatan konteks berlapis dan pengoptimuman pengambilan
  - **Rangka Kerja Pengukuran**: Metri baru untuk penilaian keberkesanan konteks
    - Kecekapan input, prestasi, kualiti, dan pertimbangan pengalaman pengguna
    - Pendekatan eksperimen untuk pengoptimuman konteks
    - Analisis kegagalan dan metodologi penambahbaikan

#### Kemaskini Navigasi Kurikulum (README.md)
- **Struktur Modul Dipertingkat**: Jadual kurikulum dikemaskini untuk memasukkan topik lanjutan baru
  - Ditambah entri Kejuruteraan Konteks (5.14) dan Pengangkutan Tersuai (5.15)
  - Pemformatan dan pautan navigasi konsisten di semua modul
  - Keterangan dikemaskini untuk mencerminkan skop kandungan semasa

### Penambahbaikan Struktur Direktori
- **Penyeragaman Penamaan**: Nama semula "mcp transport" kepada "mcp-transport" untuk konsistensi dengan folder topik lanjutan lain
- **Pengaturan Kandungan**: Semua folder 05-AdvancedTopics kini mengikuti corak penamaan konsisten (mcp-[topic])

### Penambahbaikan Kualiti Dokumentasi
- **Penjajaran Spesifikasi MCP**: Semua kandungan baru merujuk Spesifikasi MCP 2025-06-18 semasa
- **Contoh Pelbagai Bahasa**: Contoh kod komprehensif dalam C#, TypeScript, dan Python
- **Fokus Perusahaan**: Corak sedia produksi dan integrasi Azure cloud menyeluruh
- **Dokumentasi Visual**: Diagram Mermaid untuk visualisasi seni bina dan aliran

## 18 Ogos 2025

### Kemaskini Menyeluruh Dokumentasi - Standard MCP 2025-06-18

#### Amalan Terbaik Keselamatan MCP (02-Security/) - Pengubahsuaian Menyeluruh
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Penulisan semula lengkap sejajar dengan Spesifikasi MCP 2025-06-18
  - **Keperluan Wajib**: Ditambah keperluan MUST/MUST NOT jelas dari spesifikasi rasmi dengan penunjuk visual jelas
  - **12 Amalan Teras Keselamatan**: Disusun semula dari senarai 15 item ke domain keselamatan komprehensif
    - Keselamatan Token & Pengesahan dengan integrasi penyedia identiti luaran
    - Pengurusan Sesi & Keselamatan Pengangkutan dengan keperluan kriptografi
    - Perlindungan Ancaman Khusus AI dengan integrasi Microsoft Prompt Shields
    - Kawalan Akses & Kebenaran dengan prinsip keistimewaan paling minimum
    - Keselamatan Kandungan & Pemantauan dengan integrasi Azure Content Safety
    - Keselamatan Rantaian Bekalan dengan pengesahan komponen menyeluruh
    - Keselamatan OAuth & Pencegahan Confused Deputy dengan pelaksanaan PKCE
    - Respons Insiden & Pemulihan dengan kebolehan automatik
    - Pematuhan & Tadbir Urus dengan penjajaran peraturan
    - Kawalan Keselamatan Lanjutan dengan seni bina zero trust
    - Integrasi Ekosistem Keselamatan Microsoft dengan penyelesaian menyeluruh
    - Evolusi Keselamatan Berterusan dengan amalan adaptif
  - **Penyelesaian Keselamatan Microsoft**: Panduan integrasi dipertingkat untuk Prompt Shields, Azure Content Safety, Entra ID, dan GitHub Advanced Security
  - **Sumber Pelaksanaan**: Pautan sumber komprehensif dikategorikan mengikut Dokumentasi Rasmi MCP, Penyelesaian Keselamatan Microsoft, Standard Keselamatan, dan Panduan Pelaksanaan

#### Kawalan Keselamatan Lanjutan (02-Security/) - Pelaksanaan Perusahaan
- **MCP-SECURITY-CONTROLS-2025.md**: Penstrukturan semula dengan rangka kerja keselamatan gred perusahaan
  - **9 Domain Keselamatan Komprehensif**: Diperluas dari kawalan asas ke rangka kerja perusahaan terperinci
    - Pengesahan & Pautan Lanjutan dengan integrasi Microsoft Entra ID
    - Keselamatan Token & Kawalan Anti-Passthrough dengan pengesahan menyeluruh
    - Kawalan Keselamatan Sesi dengan pencegahan rampasan
    - Kawalan Keselamatan Khusus AI dengan pencegahan suntikan prompt dan racun alat
    - Pencegahan Serangan Confused Deputy dengan keselamatan proksi OAuth
    - Keselamatan Pelaksanaan Alat dengan sandboxing dan pengasingan
    - Kawalan Keselamatan Rantaian Bekalan dengan pengesahan pergantungan
    - Kawalan Pemantauan & Pengesanan dengan integrasi SIEM
    - Respons Insiden & Pemulihan dengan kebolehan automatik
  - **Contoh Pelaksanaan**: Ditambah blok konfigurasi YAML terperinci dan contoh kod
  - **Integrasi Penyelesaian Microsoft**: Liputan menyeluruh perkhidmatan keselamatan Azure, GitHub Advanced Security, dan pengurusan identiti perusahaan

#### Keselamatan Topik Lanjutan (05-AdvancedTopics/mcp-security/) - Pelaksanaan Sedia Produksi
- **README.md**: Penulisan semula lengkap untuk pelaksanaan keselamatan perusahaan
  - **Penjajaran Spesifikasi Semasa**: Dikemas kini ke Spesifikasi MCP 2025-06-18 dengan keperluan keselamatan wajib
  - **Pengesahan Dipertingkat**: Integrasi Microsoft Entra ID dengan contoh lengkap .NET dan Java Spring Security
  - **Integrasi Keselamatan AI**: Pelaksanaan Microsoft Prompt Shields dan Azure Content Safety dengan contoh terperinci Python
  - **Mitigasi Ancaman Lanjutan**: Contoh pelaksanaan komprehensif untuk
    - Pencegahan Serangan Confused Deputy dengan PKCE dan pengesahan persetujuan pengguna
    - Pencegahan Passthrough Token dengan pengesahan audiens dan pengurusan token selamat
    - Pencegahan Rampasan Sesi dengan pengikatan kriptografi dan analisis kelakuan
  - **Integrasi Keselamatan Perusahaan**: Pemantauan Azure Application Insights, saluran pengesanan ancaman, dan keselamatan rantaian bekalan
  - **Senarai Semak Pelaksanaan**: Kawalan keselamatan wajib vs disyorkan dengan manfaat ekosistem keselamatan Microsoft yang jelas

### Kualiti Dokumentasi & Penjajaran Standard
- **Rujukan Spesifikasi**: Dikemas kini semua rujukan ke Spesifikasi MCP 2025-06-18 semasa
- **Ekosistem Keselamatan Microsoft**: Panduan integrasi dipertingkat di seluruh dokumentasi keselamatan
- **Pelaksanaan Praktikal**: Ditambah contoh kod terperinci dalam .NET, Java, dan Python dengan corak perusahaan
- **Pengaturan Sumber**: Pengkategorian komprehensif dokumentasi rasmi, standard keselamatan, dan panduan pelaksanaan
- **Penunjuk Visual**: Penandaan jelas keperluan wajib vs amalan disyorkan


#### Konsep Teras (01-CoreConcepts/) - Pengubahsuaian Menyeluruh
- **Kemas Kini Versi Protokol**: Dikemas kini untuk merujuk Spesifikasi MCP 2025-06-18 dengan penomboran versi berasaskan tarikh (format YYYY-MM-DD)
- **Pemurnian Seni Bina**: Keterangan dipertingkat mengenai Hos, Klien, dan Pelayan untuk mencerminkan corak seni bina MCP semasa
  - Hos kini didefinisikan dengan jelas sebagai aplikasi AI yang menyelaras pelbagai sambungan klien MCP
  - Klien diterangkan sebagai penyambung protokol yang mengekalkan hubungan satu-ke-satu dengan pelayan
  - Pelayan dipertingkat dengan senario penyebaran tempatan dan jauh
- **Penstrukturan Semula Primitif**: Penstrukturan lengkap semula primitif pelayan dan klien
  - Primitif Pelayan: Sumber (sumber data), Prompts (templat), Alat (fungsi boleh laksana) dengan penjelasan dan contoh terperinci
  - Primitif Klien: Persampelan (penyelesaian LLM), Pengelusan (input pengguna), Pencatatan (debug/pemantauan)
  - Dikemas kini dengan corak kaedah penemuan (`*/list`), pengambilan (`*/get`), dan pelaksanaan (`*/call`) semasa
- **Seni Bina Protokol**: Memperkenalkan model seni bina berlapis dua
  - Lapisan Data: Asas JSON-RPC 2.0 dengan pengurusan kitaran hayat dan primitif
  - Lapisan Pengangkutan: STDIO (tempatan) dan HTTP Boleh Alir dengan SSE (jauh) mekanisme pengangkutan
- **Rangka Kerja Keselamatan**: Prinsip keselamatan komprehensif termasuk persetujuan pengguna eksplisit, perlindungan privasi data, keselamatan pelaksanaan alat, dan keselamatan lapisan pengangkutan
- **Corak Komunikasi**: Kemas kini mesej protokol untuk menunjukkan inisialisasi, penemuan, pelaksanaan, dan aliran pemberitahuan
- **Contoh Kod**: Menyegarkan contoh pelbagai bahasa (.NET, Java, Python, JavaScript) untuk mencerminkan corak SDK MCP semasa

#### Keselamatan (02-Security/) - Pengubahsuaian Keselamatan Menyeluruh  
- **Penjajaran Standard**: Penjajaran penuh dengan keperluan keselamatan Spesifikasi MCP 2025-06-18
- **Evolusi Pengesahan**: Mendokumentasi evolusi dari pelayan OAuth tersuai kepada delegasi penyedia identiti luaran (Microsoft Entra ID)
- **Analisis Ancaman Khusus AI**: Liputan dipertingkat vektor serangan AI moden
  - Senario serangan suntikan prompt terperinci dengan contoh dunia sebenar
  - Mekanisme racun alat dan corak serangan "rug pull"
  - Serangan pencemaran tetingkap konteks dan kekeliruan model
- **Penyelesaian Keselamatan AI Microsoft**: Liputan komprehensif ekosistem keselamatan Microsoft
  - AI Prompt Shields dengan pengesanan lanjutan, penyinaran, dan teknik pembatas
  - Corak integrasi Azure Content Safety
  - GitHub Advanced Security untuk perlindungan rantaian bekalan
- **Mitigasi Ancaman Lanjutan**: Kawalan keselamatan terperinci untuk
  - Rampasan sesi dengan senario serangan khusus MCP dan keperluan ID sesi kriptografi
  - Masalah Confused Deputy dalam senario proksi MCP dengan keperluan persetujuan eksplisit
  - Kelemahan passthrough token dengan kawalan pengesahan wajib
- **Keselamatan Rantaian Bekalan**: Liputan diperluaskan rantaian bekalan AI termasuk model asas, perkhidmatan embedding, penyedia konteks, dan API pihak ketiga
- **Keselamatan Asas**: Integrasi dipertingkat dengan corak keselamatan perusahaan termasuk seni bina zero trust dan ekosistem keselamatan Microsoft
- **Pengaturan Sumber**: Pautan sumber komprehensif dikategorikan mengikut jenis (Dokumentasi Rasmi, Standard, Penyelidikan, Penyelesaian Microsoft, Panduan Pelaksanaan)

### Penambahbaikan Kualiti Dokumentasi
- **Objektif Pembelajaran Berstruktur**: Objektif pembelajaran dipertingkat dengan hasil khusus dan boleh dilaksanakan
- **Rujukan Silang**: Ditambah pautan antara topik keselamatan dan konsep teras yang berkaitan
- **Maklumat Semasa**: Dikemaskini semua rujukan tarikh dan pautan spesifikasi ke standard semasa
- **Panduan Pelaksanaan**: Ditambah garis panduan pelaksanaan spesifik dan boleh dilaksanakan di kedua-dua bahagian

## 16 Julai 2025

### Penambahbaikan README dan Navigasi
- Reka bentuk semula sepenuhnya navigasi kurikulum dalam README.md
- Menggantikan tag `<details>` dengan format jadual yang lebih mudah diakses
- Mewujudkan pilihan susun atur alternatif dalam folder baru "alternative_layouts"
- Ditambah contoh navigasi berasaskan kad, ber-tab, dan ber-akordion
- Dikemaskini bahagian struktur repositori untuk memasukkan semua fail terkini
- Dipertingkat bahagian "Cara Menggunakan Kurikulum Ini" dengan cadangan jelas
- Dikemaskini pautan spesifikasi MCP ke URL yang betul
- Ditambah bahagian Kejuruteraan Konteks (5.14) ke struktur kurikulum

### Kemaskini Panduan Kajian
- Revisi sepenuhnya panduan kajian untuk selaras dengan struktur repositori semasa
- Ditambah bahagian baru untuk Klien MCP dan Alat, serta Pelayan MCP Popular
- Dikemaskini Peta Kurikulum Visual untuk mencerminkan semua topik dengan tepat
- Dipertingkat keterangan Topik Lanjutan untuk meliputi semua bidang khusus
- Dikemaskini bahagian Kajian Kes untuk mencerminkan contoh sebenar
- Ditambah changelog komprehensif ini

### Sumbangan Komuniti (06-CommunityContributions/)
- Ditambah maklumat terperinci tentang pelayan MCP untuk penjanaan imej
- Ditambah bahagian komprehensif mengenai penggunaan Claude dalam VSCode
- Ditambah arahan pemasangan dan penggunaan klien terminal Cline
- Dikemaskini bahagian klien MCP untuk memasukkan semua pilihan klien popular
- Dipertingkat contoh sumbangan dengan sampel kod lebih tepat

### Topik Lanjutan (05-AdvancedTopics/)
- Mengatur semua folder topik khusus dengan penamaan konsisten
- Ditambah bahan dan contoh kejuruteraan konteks
- Ditambah dokumentasi integrasi ejen Foundry
- Dipertingkat dokumentasi integrasi keselamatan Entra ID

## 11 Jun 2025

### Penciptaan Awal
- Mengeluarkan versi pertama kurikulum MCP untuk Pemula
- Mewujudkan struktur asas untuk semua 10 bahagian utama
- Melaksanakan Peta Kurikulum Visual untuk navigasi
- Ditambah projek sampel awal dalam pelbagai bahasa pengaturcaraan

### Memulakan (03-GettingStarted/)
- Mewujudkan contoh pelaksanaan pelayan pertama
- Ditambah panduan pembangunan klien
- Termasuk arahan integrasi klien LLM
- Ditambah dokumentasi integrasi VS Code
- Melaksanakan contoh Server-Sent Events (SSE)

### Konsep Teras (01-CoreConcepts/)
- Ditambah penjelasan terperinci seni bina klien-pelayan
- Mewujudkan dokumentasi komponen utama protokol
- Mendokumentasikan corak mesej dalam MCP

## 23 Mei 2025

### Struktur Repositori
- Memulakan repositori dengan struktur folder asas
- Mewujudkan fail README untuk setiap bahagian utama
- Menyediakan infrastruktur terjemahan
- Ditambah aset imej dan diagram

### Dokumentasi
- Mewujudkan README.md permulaan dengan gambaran kurikulum
- Ditambah CODE_OF_CONDUCT.md dan SECURITY.md
- Menyediakan SUPPORT.md dengan panduan mendapatkan bantuan
- Mewujudkan struktur panduan kajian awal

## 15 April 2025

### Perancangan dan Rangka Kerja
- Perancangan awal untuk kurikulum MCP untuk Pemula
- Mendefinisikan objektif pembelajaran dan audiens sasaran
- Membuat garis besar struktur kurikulum 10 bahagian
- Membangunkan rangka kerja konseptual untuk contoh dan kajian kes
- Mewujudkan contoh prototaip awal untuk konsep utama

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->